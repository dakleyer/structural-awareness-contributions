"""Run six native model episodes, or write a truthful access-blocked report."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import sys
import time

from api_adapter import ENDPOINT, FIELDS, TOOL, ModelAccessError, ResponsesClient
from native import Episode, Recorder, canonical, digest, load_worlds

HERE = Path(__file__).resolve().parent
DEFAULT_ORACLE = HERE.parent / '00G-HF-ORACLE-v0.4'
ORACLE_FREEZE = '58c5a0cbb00fd945e7ebebbcfd6e7758573fc6f7fb6209e33dfc8e3e76c7d287'
LIMITS = {'model_turns_per_episode': 20, 'max_output_tokens_per_turn': 2048,
          'wall_seconds_per_episode': 300, 'request_timeout_seconds': 45,
          'charged_tokens_stop_after_response': 32000, 'human_reviews': 0,
          'synthetic_start': 25, 'synthetic_deadline': 100}


def write_json(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


def verify_oracle(path):
    raw = (path / 'DESIGN_FREEZE.json').read_bytes()
    if hashlib.sha256(raw).hexdigest() != ORACLE_FREEZE:
        raise RuntimeError('Oracle freeze mismatch')
    freeze = json.loads(raw)
    for name, expected in freeze['sha256'].items():
        if hashlib.sha256((path / name).read_bytes()).hexdigest() != expected:
            raise RuntimeError('Oracle file changed: ' + name)
    sys.path.insert(0, str(path.resolve()))
    from oracle import evaluate
    return evaluate


def check_arguments(args):
    if not isinstance(args, dict) or set(args) != set(FIELDS):
        return False
    if args['action'] not in FIELDS['action']['enum'] or args['task'] not in ('T0', 'T1', None):
        return False
    if not isinstance(args['basis'], list) or any(not isinstance(x, str) for x in args['basis']):
        return False
    if any(args[k] is not None and not isinstance(args[k], str) for k in ('decision_id', 'attempt_id')):
        return False
    return all(args[k] is None or type(args[k]) is int for k in ('total', 'until'))


def run_episode(world, client, recorder, evaluate, limits=None):
    budget = limits or LIMITS
    ep = Episode(world, recorder)
    initial = ep.initial_view()
    items = [{'role': 'user', 'content': canonical(initial)}]
    recorder.write('initial_model_view', initial)
    previous = None
    started = time.monotonic()
    model_requests = model_responses = charged_tokens = 0
    infrastructure = False
    reason = 'turn_limit'
    observed_models = set()
    for turn in range(budget['model_turns_per_episode']):
        if ep.closed:
            reason = ep.close_reason
            break
        remaining = budget['wall_seconds_per_episode'] - (time.monotonic() - started)
        if remaining <= 0 or charged_tokens >= budget['charged_tokens_stop_after_response']:
            reason = 'resource_limit'
            break
        client.timeout = min(budget['request_timeout_seconds'], remaining)
        recorder.write('model_input', {'turn': turn, 'items': items, 'previous_response_id': previous})
        model_requests += 1
        try:
            response = client.respond(items, previous)
        except ModelAccessError as exc:
            infrastructure, reason = True, 'MODEL_ACCESS_ERROR:' + str(exc)
            recorder.write('model_error', {'turn': turn, 'reason': reason})
            break
        model_responses += 1
        if not isinstance(response, dict):
            infrastructure, reason = True, 'MALFORMED_API_RESPONSE'
            recorder.write('model_error', {'turn': turn, 'reason': reason})
            break
        if isinstance(response.get('model'), str):
            observed_models.add(response['model'])
        charged_tokens += int((response.get('usage') or {}).get('total_tokens', 0))
        # Persist visible outputs/function requests, never solicit or publish private reasoning.
        output = response.get('output')
        recorder.write('model_response', {
            'turn': turn, 'id': response.get('id'), 'model': response.get('model'),
            'status': response.get('status'), 'usage': response.get('usage'),
            'visible_output': [v for v in (output or []) if isinstance(v, dict) and v.get('type') != 'reasoning'],
            'elapsed_seconds': time.monotonic() - started,
        })
        if (response.get('status') != 'completed' or not isinstance(output, list)
                or any(not isinstance(v, dict) for v in output) or not response.get('id')):
            infrastructure, reason = True, 'INCOMPLETE_OR_MALFORMED_API_RESPONSE'
            break
        if time.monotonic() - started > budget['wall_seconds_per_episode']:
            reason = 'wall_budget_expired_before_tool_dispatch'
            break
        calls = [v for v in output if v.get('type') == 'function_call']
        if not calls:
            reason = 'model_final_without_further_action'
            break
        if len(calls) != 1 or calls[0].get('name') != 'step' or not calls[0].get('call_id'):
            infrastructure, reason = True, 'UNSUPPORTED_TOOL_RESPONSE'
            break
        call = calls[0]
        try:
            arguments = json.loads(call['arguments'])
        except (ValueError, KeyError, TypeError):
            arguments = None
        if check_arguments(arguments):
            result = ep.call(**arguments)
        else:
            recorder.write('rejected_arguments', {'turn': turn, 'call_id': call['call_id']})
            result = {'error': 'invalid_tool_arguments'}
        previous = response['id']
        items = [{'type': 'function_call_output', 'call_id': call['call_id'], 'output': canonical(result)}]
    ep.finish(reason, infrastructure=infrastructure)
    trace = ep.trace(infrastructure=infrastructure)
    outcome = evaluate(ep.world, trace)
    summary = {'status': 'INFRASTRUCTURE_INTERRUPTED' if infrastructure else 'NATIVE_EPISODE_OBSERVED',
               'reason': ep.close_reason, 'model_requests': model_requests,
               'model_responses': model_responses, 'observed_models': sorted(observed_models),
               'charged_tokens': charged_tokens, 'wall_seconds': time.monotonic() - started,
               'operational_result_eligible': not infrastructure, 'oracle_result': outcome,
               'journal_chain_head': recorder.previous}
    return summary, trace


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--oracle-dir', type=Path, default=DEFAULT_ORACLE)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--model', default=os.getenv('OPENAI_MODEL'))
    args = parser.parse_args()
    evaluate = verify_oracle(args.oracle_dir)
    worlds = load_worlds(args.oracle_dir)
    args.output_dir.mkdir(parents=True, exist_ok=False)
    instructions = (HERE / 'INSTRUCTIONS.txt').read_text()
    source_names = ('native.py', 'api_adapter.py', 'run_pilot.py', 'INSTRUCTIONS.txt')
    registration = {
        'status': 'EXPLORATORY_LOCAL_REGISTRATION_NOT_EXTERNAL_PREREGISTRATION',
        'created_utc': datetime.now(timezone.utc).isoformat(),
        'implementation': 'OPENAI_RESPONSES_WITH_AUTHOR_NATIVE_APPLICATION_CONTROLS_v0.1',
        'profile': 'OAI-G1_CANDIDATE_NOT_INDEPENDENTLY_REVIEWED',
        'phase': 'partial_E1_six_cell_integration_pilot_without_EA',
        'requested_model': args.model, 'endpoint': ENDPOINT, 'api_store': True,
        'oracle_freeze_sha256': ORACLE_FREEZE, 'limits': LIMITS,
        'instructions_sha256': hashlib.sha256(instructions.encode()).hexdigest(),
        'tool_schema_sha256': digest(TOOL),
        'code_sha256': {n: hashlib.sha256((HERE / n).read_bytes()).hexdigest() for n in source_names},
        'world_hashes': {cell: digest(world) for cell, world in worlds},
        'cell_order': [cell for cell, _ in worlds], 'episodes_per_cell': 1,
        'seed': 'NOT_SET_UNCONTROLLED_MODEL_VARIATION',
        'state_reset': 'new local episode and new API conversation for each cell',
        'transport': 'serial function calls; only simulated task resources',
        'clock': 'logical ticks; receiver resumes at25; no real-time equivalence',
        'blinding': 'PUBLIC_AUTHOR_FIXTURES_NOT_BLIND',
        'external_reviewer': None, 'historical_equivalence': False,
        'human_annotation_runs': 0, 'population_claim': 'NOT_ASSESSED',
        'admission_A25': 'PENDING', 'comparative_claims': False,
        'retry_rule': 'no automatic retries; retain errors and continue all registered cells',
    }
    write_json(args.output_dir / 'REGISTRATION.json', registration)
    write_json(args.output_dir / 'WORLD_INPUTS.json', dict(worlds))
    reasons = []
    key = os.getenv('OPENAI_API_KEY')
    if not key:
        reasons.append('OPENAI_API_KEY_NOT_CONFIGURED')
    if not args.model:
        reasons.append('MODEL_NOT_SELECTED')
    if reasons:
        report = {'status': 'BLOCKED_BEFORE_MODEL_EXECUTION', 'reasons': reasons,
                  'model_requests': 0, 'model_responses': 0, 'agent_episodes_started': 0,
                  'agent_episodes_completed': 0, 'oracle_evaluations_on_model_episodes': 0,
                  'planned_cells': [cell for cell, _ in worlds], 'results': []}
        write_json(args.output_dir / 'REPORT.json', report)
        print(json.dumps(report, indent=2))
        return 2
    results = []
    client = ResponsesClient(args.model, key, instructions)
    for cell, world in worlds:
        directory = args.output_dir / cell
        directory.mkdir()
        recorder = Recorder(directory / 'JOURNAL.jsonl')
        summary, trace = run_episode(world, client, recorder, evaluate)
        write_json(directory / 'TRACE.json', trace)
        write_json(directory / 'RESULT.json', summary)
        results.append({'cell': cell, **summary})
    report = {'status': 'EXPLORATORY_NATIVE_LOT_FINISHED',
              'model_requests': sum(r['model_requests'] for r in results),
              'model_responses': sum(r['model_responses'] for r in results),
              'agent_episodes_started': sum(r['model_responses'] > 0 for r in results),
              'agent_episodes_completed': sum(r['operational_result_eligible'] for r in results),
              'oracle_evaluations_on_model_episodes': sum(r['model_responses'] > 0 for r in results),
              'blind': False, 'EA_enabled': False, 'results': results}
    write_json(args.output_dir / 'REPORT.json', report)
    print(json.dumps({k: v for k, v in report.items() if k != 'results'}, indent=2))
    return 0 if all(r['operational_result_eligible'] for r in results) else 3


if __name__ == '__main__':
    raise SystemExit(main())
