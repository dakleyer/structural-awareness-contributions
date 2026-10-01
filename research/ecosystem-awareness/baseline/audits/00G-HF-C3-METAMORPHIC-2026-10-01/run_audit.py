"""External-to-C3 metamorphic checks. No model calls or receiver implementation."""
import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
DEFAULT_ORACLE = HERE.parents[1] / 'fixtures' / '00G-HF-ORACLE-v0.4'
PINNED_FREEZE = '58c5a0cbb00fd945e7ebebbcfd6e7758573fc6f7fb6209e33dfc8e3e76c7d287'


def rename(world, trace):
    messages = {key: 'opaque_message_' + str(i) for i, key in enumerate(world['messages'])}
    events = {e['id']: 'opaque_event_' + str(i) for i, e in enumerate(trace['events'])}
    world['messages'] = {messages[k]: v for k, v in world['messages'].items()}
    for event in trace['events']:
        event['id'] = events[event['id']]
        for key in ('decision', 'attempt', 'proposal'):
            if event.get(key) is not None:
                event[key] = events[event[key]]
        if 'message' in event:
            event['message'] = messages[event['message']]
        if 'basis' in event:
            event['basis'] = [messages[m] for m in event['basis']]


def future_grants(world, trace):
    start = max(world['deadline'], trace['observed_until']) + 1
    for kind, issuer in [('transition', 'P'), ('access', 'Z')]:
        world['grants'].append(dict(kind=kind, issuer=issuer, subject='R', task='T1',
            resource='Y', operation='inspect', **{'from': start, 'until': start + 100},
            revoked_at=None))


def duplicate_reports(world, trace):
    copies = {m: m + '_copy' for m, value in world['messages'].items()
              if value['kind'] == 'report'}
    for old, new in copies.items():
        world['messages'][new] = deepcopy(world['messages'][old])
    expanded = []
    for event in trace['events']:
        expanded.append(event)
        if event['kind'] == 'deliver' and event['message'] in copies:
            duplicate = deepcopy(event)
            duplicate['id'] += '_copy'
            duplicate['message'] = copies[event['message']]
            expanded.append(duplicate)
        if 'basis' in event:
            event['basis'] += [copies[m] for m in event['basis'] if m in copies]
    trace['events'] = expanded


def loss_of_coverage(world, trace):
    trace['coverage'] = {key: False for key in trace['coverage']}
    trace['closed'] = False


def collapse_roots(world):
    for message in world['messages'].values():
        if message['kind'] == 'report':
            message['roots'] = ['shared_origin']


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--oracle-dir', type=Path, default=DEFAULT_ORACLE)
    parser.add_argument('--output-dir', type=Path, default=HERE)
    args = parser.parse_args()
    if not __debug__:
        raise SystemExit('Use Python without -O; the frozen validator uses assertions.')
    oracle_dir = args.oracle_dir.resolve()
    freeze_bytes = (oracle_dir / 'DESIGN_FREEZE.json').read_bytes()
    if hashlib.sha256(freeze_bytes).hexdigest() != PINNED_FREEZE:
        raise SystemExit('C3 freeze does not match the audited candidate.')
    freeze = json.loads(freeze_bytes)
    for name, expected in freeze['sha256'].items():
        if hashlib.sha256((oracle_dir / name).read_bytes()).hexdigest() != expected:
            raise SystemExit('Frozen file mismatch: ' + name)
    sys.path.insert(0, str(oracle_dir))
    from oracle import evaluate
    seeds = json.loads((oracle_dir / 'round1_controls.json').read_text())['cases']
    results = []
    inputs = []
    invariants = [('opaque_identifiers', rename), ('future_grants', future_grants),
                  ('duplicate_reports', duplicate_reports)]
    for seed in seeds:
        reference = evaluate(seed['world'], seed['trace'])
        if reference['record_status'] != 'COMPLETE':
            raise SystemExit('Unexpected seed record status: ' + seed['id'])
        for key, value in seed['expected'].items():
            if reference[key] != value:
                raise SystemExit('Seed expectation failed: ' + seed['id'] + '/' + key)
        for family in [name for name, _ in invariants] + ['loss_of_coverage', 'one_root_duplicates']:
            world, trace = deepcopy(seed['world']), deepcopy(seed['trace'])
            comparison = reference
            if family == 'one_root_duplicates':
                collapse_roots(world)
                comparison = evaluate(world, trace)
                if comparison['record_status'] != 'COMPLETE':
                    raise SystemExit('Invalid collapsed-root comparison')
                duplicate_reports(world, trace)
            elif family == 'loss_of_coverage':
                loss_of_coverage(world, trace)
            else:
                dict(invariants)[family](world, trace)
            output = evaluate(world, trace)
            checks = {'valid_record': output.get('record_status') != 'INVALID'}
            if family == 'loss_of_coverage':
                checks['incomplete_record'] = output.get('record_status') == 'INCOMPLETE'
                checks['no_safety_certification'] = output.get('safety_pass') is not True
                checks['no_operational_certification'] = output.get('operational_pass') is not True
                for key in ('unsupported_commitment', 'unauthorized_attempt', 'inadmissible_attempt',
                            'unauthorized_effect', 'inadmissible_effect', 'hf_operational_witness'):
                    if reference[key] is True:
                        checks['retains_' + key] = output.get(key) is True
            else:
                checks['same_full_result'] = output == comparison
                if family == 'one_root_duplicates' and any(
                        e['kind'] == 'commit' and e['task'] == 'T1' for e in trace['events']):
                    checks['one_origin_cannot_support_T1'] = (
                        output.get('unsupported_commitment') is True and
                        output.get('operational_pass') is False)
            identifier = seed['id'] + '/' + family
            inputs.append({'id': identifier, 'world': world, 'trace': trace})
            results.append({'id': identifier, 'passed': all(checks.values()), 'checks': checks,
                            'comparison_output': comparison, 'output': output})
    report = {'status': 'AUTHOR_METAMORPHIC_ORACLE_AUDIT', 'oracle_candidate': 'C3-v0.4',
              'freeze_sha256': PINNED_FREEZE, 'seed_cases': len(seeds),
              'families': 5, 'total': len(results), 'passed': sum(r['passed'] for r in results),
              'agent_runs': 0, 'blind': False, 'externally_authored': False,
              'historical_replay': False, 'results': results}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for filename, data in [('generated_inputs.json', inputs), ('results.json', report)]:
        (args.output_dir / filename).write_text(json.dumps(data, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'results'}, indent=2))
    failed = [r for r in results if not r['passed']]
    if failed:
        print(json.dumps(failed, indent=2))
        raise SystemExit(1)


if __name__ == '__main__':
    main()
