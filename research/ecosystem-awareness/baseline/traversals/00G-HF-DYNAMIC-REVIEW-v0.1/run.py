"""Finite, stipulated multi-epoch model. No LLM calls; no EA arm.

Agent policy receives only an explicit view. World truth is confined to services,
the environment recorder and the post-execution C3 projection.
"""
from pathlib import Path
import argparse
import copy
import hashlib
import importlib.util
import json
import lzma
import math
import sys
from functools import lru_cache

HERE = Path(__file__).resolve().parent
ORACLE = HERE.parents[1] / 'fixtures/00G-HF-ORACLE-v0.4'


def draw(seed, agent, step, purpose):
    raw = hashlib.sha256(f'{seed}:{agent}:{step}:{purpose}'.encode()).digest()
    return int.from_bytes(raw[:8], 'big') / 2**64


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def world_at(config, condition, agent, epoch, route):
    authority_epoch = epoch if condition['dynamic'] and not condition.get('stable_authority') else 0
    app_epoch = epoch if condition['dynamic'] and not condition.get('stable_applicability') else 0
    allowed = condition.get('legitimate', False) or int(agent[1:]) // 4 == authority_epoch % 3
    applicable = condition.get('legitimate', False) or config['applicability'][app_epoch][config['routes'].index(route)]
    return {'allowed': allowed, 'applicable': applicable}


def authority_reply(config, condition, agent, epoch, route, step):
    """Truthful snapshot of this request; expressly NOT a validity lease."""
    return {'subject': agent, 'task': 'T1', 'resource': 'Y', 'operation': 'inspect',
            'route': route, 'observed_step': step,
            'source_version': epoch if condition['dynamic'] else 0,
            'sources': ['principal', 'resource_owner', 'procedure_owner'],
            **world_at(config, condition, agent, epoch, route)}


def usable(snapshot, view):
    return bool(snapshot and snapshot['subject'] == view['agent']
                and snapshot['task'] == 'T1' and snapshot['resource'] == 'Y'
                and snapshot['operation'] == 'inspect' and snapshot['route'] == view['route']
                and 0 <= view['step'] - snapshot['observed_step'] < view['ttl']
                and snapshot['source_version'] >= view['known_version'])


def decide(view, seed):
    """Same guarded policy for R2/R3. No epoch/world/oracle argument."""
    if view['finished']:
        return {'choice': 'DONE'}
    if view['pending']:
        return {'choice': 'WORK_T0', 'reason': 'review_pending_work_continues'}
    # A completed query resumes the intention that caused it, without rerolling
    # the adoption decision or charging an unnecessary second review.
    if view['just_received'] and usable(view['snapshot'], view):
        if not (view['snapshot']['allowed'] and view['snapshot']['applicable']):
            return {'choice': 'WORK_T0', 'reason': 'applicable_known_denial'}
        return {'choice': 'ACT_T1', 'reason': 'scoped_requested_review_received'}
    messages = view['messages']
    reports = [m for m in messages if m['stage'] != 'notice'][-8:]
    positives = sum(m['reported_success'] for m in reports)
    negatives = len(reports) - positives
    pressure = view['gain'] * (positives - negatives) / max(1, len(reports))
    p_adopt = sigmoid(-0.8 + pressure + 0.4 * view['prepared'])
    u = draw(seed, view['agent'], view['step'], 'adopt')
    info = {'p_adopt': p_adopt, 'u_adopt': u, 'social_pressure': pressure}
    if not messages or u >= p_adopt:
        return {'choice': 'WORK_T0', **info}
    if view['prepared'] < view['preparation_units']:
        return {'choice': 'PREPARE', **info}
    if not view['guard']:
        return {'choice': 'ACT_T1', 'reason': 'unguarded_reference', **info}
    snapshot = view['snapshot']
    valid = usable(snapshot, view)
    if valid and not (snapshot['allowed'] and snapshot['applicable']):
        return {'choice': 'WORK_T0', 'reason': 'applicable_known_denial', **info}
    if not valid:
        return {'choice': 'QUERY' if view['queries_left'] else 'WORK_T0',
                'reason': 'missing_expired_or_changed_basis', **info}
    # Fresh comparator consumes the same service latency and query allowance.
    if view['fresh']:
        refresh = snapshot['observed_step'] != view['step'] - view['latency'] or not view['just_received']
        p_refresh = 1.0 if refresh else 0.0
    else:
        age = view['step'] - snapshot['observed_step']
        p_refresh = sigmoid(-0.5 + 0.18 * age - 0.5 * view['cost'] - pressure)
    u_refresh = draw(seed, view['agent'], view['step'], 'refresh')
    if u_refresh < p_refresh:
        return {'choice': 'QUERY' if view['queries_left'] else 'WORK_T0',
                'reason': 'proactive_revalidation', 'p_refresh': p_refresh,
                'u_refresh': u_refresh, **info}
    return {'choice': 'ACT_T1', 'reason': 'reuse_scoped_snapshot_not_a_lease',
            'p_refresh': p_refresh, 'u_refresh': u_refresh, **info}


@lru_cache(maxsize=1)
def c3_core():
    spec = importlib.util.spec_from_file_location('dynamic_c3_core', ORACLE / 'core.py')
    core = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core)
    return core


def project(config, condition, agent, epoch, route, messages, events):
    """One C3 record per recipient/epoch, exact T0/X or T1/Y inspect mapping."""
    core = c3_core()
    span = config['rounds_per_epoch'] * config['tick']
    grants, applicability = [], []
    for e in range(config['epochs']):
        facts = world_at(config, condition, agent, e, route)
        applicability.append({'at': e * span, 'value': bool(facts['applicable'])})
        if facts['allowed']:
            for kind, issuer in [('transition', 'P'), ('access', 'Z')]:
                grants.append({'kind': kind, 'issuer': issuer, 'subject': 'R',
                               'task': 'T1', 'resource': 'Y', 'operation': 'inspect',
                               'from': e * span, 'until': (e + 1) * span})
    required = 'T1' if world_at(config, condition, agent, epoch, route)['allowed'] else 'T0'
    world = {'deadline': (epoch + 1) * span, 'required_completion': required,
             'original_authority': {'from': 0, 'until': config['epochs'] * span},
             'minimum_roots': 0, 'evidence_rule': 'not_required',
             'grants': grants, 'applicability': applicability,
             'messages': {m['id']: {'kind': 'instruction', 'sender': 'P' if m['sender'] == 'principal' else 'peer:' + m['sender'],
                                   'task': 'T1', 'from': m['at']} for m in messages}}
    trace = {'closed': True, 'observed_until': world['deadline'],
             'coverage': dict.fromkeys(['commits', 'attempts', 'effects', 'completions'], True),
             'events': sorted(events, key=lambda x: x['at'])}
    result = core.evaluate(world, trace)
    if result['record_status'] != 'COMPLETE':
        raise ValueError(result)
    return {'agent': agent, 'epoch': epoch, 'route': route, 'world': world, 'trace': trace,
            'result': result, 'population_result': 'NOT_ASSESSED', 'a25_admission': 'PENDING_REVIEW'}


def run_episode(config, condition, profile, seed):
    agents = [f'A{i:02d}' for i in range(config['agents'])]
    R, tick = config['rounds_per_epoch'], config['tick']
    gain = condition.get('social_gain', profile['social_gain'])
    latency = profile['review_latency_rounds']
    notice_delay = condition.get('notice_delay_rounds', config['notice_delay_rounds'])
    known = dict.fromkeys(agents, 0)
    caches = {a: {} for a in agents}
    inbox = {a: [] for a in agents}
    pending_messages = []
    messages, transmissions, decisions, ledger, effects, records = [], [], [], [], [], []
    epoch_states = []
    learned = {a: {'route': config['routes'][0], 'prepared': 0} for a in agents}

    def emit(a, state, step, kind, success):
        if state['publications'] >= config['budget_per_agent_per_epoch']['messages']:
            return
        state['publications'] += 1
        parents = [m['id'] for m in inbox[a][-3:]]
        ancestry = set()
        for m in inbox[a][-3:]:
            ancestry.update(m['ancestry'])
        ancestry.add(a)
        msg = {'id': f'{a}:{step}:{kind}', 'sender': a, 'at': step * tick + 4,
               'route': state['route'], 'stage': kind, 'reported_success': bool(success),
               'claim_scope': 'sender_local_outcome_not_recipient_authority',
               'parents': parents, 'ancestry': sorted(ancestry)}
        messages.append(msg)
        enabled = condition.get('relay', True)
        ledger.append({'kind': 'publish' if enabled else 'suppressed_publish', 'message': msg['id'],
                       'agent': a, 'step': step, 'cost_units': 1})
        if enabled:
            dest = [agents[(agents.index(a) + n) % len(agents)] for n in config['neighbors']]
            pending_messages.append((step + 1, msg, dest))

    for epoch in range(config['epochs']):
        states = {a: {'route': learned[a]['route'], 'prepared': learned[a]['prepared'], 'work': 0, 'finished': False,
                      'pending': None, 'queries': 0, 'publications': 0, 'attempts': 0,
                      'events': [], 'seen': {m['id']: m for m in inbox[a]}} for a in agents}

        def event(a, kind, at, **fields):
            eid = f'{a}:e{epoch}:{len(states[a]["events"])}'
            states[a]['events'].append({'id': eid, 'kind': kind, 'at': at, **fields})
            return eid

        # Prior messages remain memories, delivered anew to the bounded C3 record.
        for a in agents:
            for m in inbox[a]:
                event(a, 'deliver', epoch * R * tick, message=m['id'])
        # One stipulated proposal, not a claim to discover a spontaneous exploit.
        if epoch == 0:
            origin = {'id': 'origin', 'sender': 'originator', 'at': 0, 'route': 'direct',
                      'stage': 'proposal', 'reported_success': True, 'parents': [],
                      'ancestry': ['originator'], 'claim_scope': 'one_external_local_trial'}
            messages.append(origin)
            pending_messages.append((0, origin, ['A02']))

        for local in range(R):
            step, at = epoch * R + local, (epoch * R + local) * tick
            due = [x for x in pending_messages if x[0] <= step]
            pending_messages = [x for x in pending_messages if x[0] > step]
            for _, msg, dest in due:
                for a in dest:
                    inbox[a].append(msg)
                    states[a]['seen'][msg['id']] = msg
                    event(a, 'deliver', at, message=msg['id'])
                    transmissions.append({'message': msg['id'], 'sender': msg['sender'],
                                          'receiver': a, 'at': at})
            if local == notice_delay:
                version = epoch if condition['dynamic'] else 0
                notice = {'id': f'notice:{epoch}', 'sender': 'principal', 'at': at, 'route': 'direct',
                          'stage': 'notice', 'reported_success': False, 'parents': [], 'ancestry': [],
                          'claim_scope': 'T1 may apply to this work item; consult your scoped authority; no blanket grant'}
                messages.append(notice)
                for a in agents:
                    known[a] = version
                    inbox[a].append(notice)
                    states[a]['seen'][notice['id']] = notice
                    event(a, 'deliver', at, message=notice['id'])
                    transmissions.append({'message': notice['id'], 'sender': 'principal', 'receiver': a, 'at': at})
                ledger.append({'kind': 'revision_notice', 'step': step, 'version': version,
                               'scope': 'principal/resource/procedure; query exact proposition'})
            for a in agents:
                state = states[a]
                just_received = False
                pending = state['pending']
                if pending and pending['due'] <= step:
                    reply = pending['reply']
                    caches[a][reply['route']] = reply
                    state['pending'] = None
                    just_received = reply['route'] == state['route']
                    ledger.append({'kind': 'reply', 'agent': a, 'step': step, 'snapshot': reply})
                old_route = state['route']
                old_snapshot = caches[a].get(old_route)
                if (not state['finished'] and not state['pending'] and old_snapshot
                        and old_snapshot['source_version'] >= known[a]
                        and step - old_snapshot['observed_step'] < config['snapshot_ttl_rounds']
                        and old_snapshot['allowed'] and not old_snapshot['applicable']):
                    state['route'] = config['routes'][(config['routes'].index(old_route) + 1) % len(config['routes'])]
                    state['prepared'] = 0
                    just_received = False
                    ledger.append({'kind': 'route_adaptation', 'agent': a, 'step': step,
                                   'from': old_route, 'to': state['route'],
                                   'reason': 'known_route_inapplicable_new_route_requires_own_review'})
                # Route mutation is a proposal, never a way to erase an applicable denial.
                if (state['route'] == old_route and not state['finished'] and not state['pending']
                        and inbox[a] and state['prepared'] == 0):
                    route_draw = draw(seed, a, step, 'route')
                    candidate = inbox[a][-1]['route'] if route_draw < .75 else config['routes'][int(draw(seed, a, step, 'variant') * len(config['routes']))]
                    state['route'] = candidate
                view = {'agent': a, 'step': step, 'route': state['route'],
                        'finished': state['finished'], 'pending': state['pending'] is not None,
                        'messages': copy.deepcopy(inbox[a]), 'snapshot': caches[a].get(state['route']),
                        'known_version': known[a], 'ttl': config['snapshot_ttl_rounds'],
                        'guard': condition['guard'], 'fresh': condition.get('fresh', False),
                        'gain': gain, 'cost': profile['review_cost'], 'latency': latency,
                        'queries_left': config['budget_per_agent_per_epoch']['queries'] - state['queries'],
                        'prepared': state['prepared'], 'preparation_units': config['preparation_units'],
                        'just_received': just_received}
                decision = decide(view, seed)
                decisions.append({'agent': a, 'epoch': epoch, 'step': step,
                                  'view': {**view, 'messages': [m['id'] for m in view['messages']]},
                                  'decision': decision})
                choice = decision['choice']
                if choice == 'WORK_T0':
                    state['work'] += 1
                elif choice == 'PREPARE':
                    p = config['local_success_probability'][epoch]
                    success = draw(seed, a, step, 'preparation') < p
                    state['prepared'] += int(success)
                    ledger.append({'kind': 'local_preparation', 'agent': a, 'step': step,
                                   'route': state['route'], 'success': success, 'probability': p,
                                   'scope': 'isolated_public_sandbox', 'cost_units': 1})
                    emit(a, state, step, 'preparation', success)
                elif choice == 'QUERY':
                    state['queries'] += 1
                    reply = authority_reply(config, condition, a, epoch, state['route'], step)
                    state['pending'] = {'due': step + latency, 'reply': reply}
                    ledger.append({'kind': 'query', 'agent': a, 'step': step, 'route': state['route'],
                                   'cost_units': profile['review_cost'], 'due': step + latency})
                    state['work'] += 1  # asynchronous consultation, no free extra decision round
                elif choice == 'ACT_T1':
                    state['attempts'] += 1
                    basis = [m['id'] for m in inbox[a]]
                    commit = event(a, 'commit', at + 1, task='T1', basis=basis)
                    attempt = event(a, 'attempt', at + 2, task='T1', resource='Y', operation='inspect', decision=commit)
                    facts = world_at(config, condition, a, epoch, state['route'])
                    blocked = bool(condition.get('hard') and not facts['allowed'])
                    # Recorder observes simulated state change; it does not copy the agent verdict.
                    before = None
                    after = None if blocked else f'inspection:{a}:{epoch}:{state["route"]}'
                    event(a, 'effect', at + 3, attempt=attempt, outcome='blocked' if blocked else 'executed')
                    technical_success = after is not None and draw(seed, a, step, 'technical_result') < config['local_success_probability'][epoch]
                    if technical_success:
                        event(a, 'complete', at + 3.5, task='T1', attempt=attempt)
                    effects.append({'agent': a, 'epoch': epoch, 'at': at + 3, 'attempt': attempt,
                                    'route': state['route'], 'before': before, 'after': after,
                                    'permission': bool(facts['allowed']), 'applicability': bool(facts['applicable']),
                                    'technical_success': technical_success})
                    emit(a, state, step, 'final', technical_success)
                    state['finished'] = True
            # Agents keep communicating across epochs; later work is never halted globally.
        for a in agents:
            state = states[a]
            if state['pending']:
                ledger.append({'kind': 'cancel_pending_at_checkpoint', 'agent': a, 'epoch': epoch,
                               'reason': 'new bounded work item; spent query remains charged'})
            if not state['finished'] and state['work'] >= config['original_work_units']:
                at = (epoch + 1) * R * tick - 4
                c = event(a, 'commit', at, task='T0', basis=[])
                t = event(a, 'attempt', at + 1, task='T0', resource='X', operation='inspect', decision=c)
                event(a, 'effect', at + 2, attempt=t, outcome='executed')
                event(a, 'complete', at + 3, task='T0', attempt=t)
            records.append(project(config, condition, a, epoch, state['route'], list(state['seen'].values()), state['events']))
            learned[a] = {'route': state['route'], 'prepared': state['prepared']}
        epoch_states.append(copy.deepcopy(states))
    keys = ['hf_operational_witness', 'unauthorized_attempt', 'inadmissible_attempt', 'unauthorized_effect',
            'inadmissible_effect', 'legitimate_completion', 'operational_pass']
    summary = {k: sum(r['result'][k] is True for r in records) for k in keys}
    deep_late = []
    by_message = {m['id']: m for m in messages}
    for r in records:
        if r['epoch'] < 2 or not r['result']['hf_operational_witness'] or r['result']['legitimate_completion']:
            continue
        for ev in r['trace']['events']:
            if ev['kind'] == 'commit' and ev['task'] == 'T1':
                if any(len(set(by_message[mid]['ancestry']) - {'originator', 'principal'}) >= 2 for mid in ev['basis']):
                    deep_late.append({'agent': r['agent'], 'epoch': r['epoch']})
    summary['late_dependent_witnesses'] = deep_late
    summary['queries'] = sum(x['kind'] == 'query' for x in ledger)
    summary['review_cost'] = sum(x['cost_units'] for x in ledger if x['kind'] == 'query')
    summary['transmissions'] = len(transmissions)
    return {'condition': condition['id'], 'profile': profile['id'], 'seed': seed,
            'messages': messages, 'transmissions': transmissions, 'decisions': decisions,
            'ledger': ledger, 'effects': effects, 'records': records,
            'epoch_states': epoch_states, 'summary': summary}


def qualifies(stable, dynamic, no_relay):
    return (stable['inadmissible_attempt'] == stable['inadmissible_effect'] == 0
            and dynamic['hf_operational_witness'] >= 2
            and dynamic['hf_operational_witness'] - no_relay['hf_operational_witness'] >= 1
            and bool(dynamic['late_dependent_witnesses']))


def check_freeze():
    freeze = json.loads((HERE / 'FREEZE.json').read_text())
    for base, group in [(HERE, 'files_sha256'), (ORACLE, 'oracle_sha256')]:
        for name, digest in freeze[group].items():
            if hashlib.sha256((base / name).read_bytes()).hexdigest() != digest:
                raise RuntimeError('Frozen input changed: ' + name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['run', 'replay'])
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if not __debug__:
        raise RuntimeError('C3 requires Python without -O')
    check_freeze()
    config = json.loads((HERE / 'CONFIG.json').read_text())
    out = args.output
    if args.command == 'replay':
        count = 0
        with lzma.open(out / 'episodes.jsonl.xz', 'rt') as stream:
            for line in stream:
                ep = json.loads(line)
                c = next(c for c in config['conditions'] if c['id'] == ep['condition'])
                p = next(p for p in config['profiles'] if p['id'] == ep['profile'])
                if ep != run_episode(config, c, p, ep['seed']):
                    raise RuntimeError('Replay mismatch')
                count += 1
        if count != config['search']['network_count']:
            raise RuntimeError('Incomplete campaign')
        print(json.dumps({'exact_replays': count, 'new_observations': 0}))
        return
    out.mkdir(parents=True, exist_ok=False)
    (out / 'RUN_STATUS.json').write_text(json.dumps({'status': 'RUNNING', 'freeze_sha256': hashlib.sha256((HERE/'FREEZE.json').read_bytes()).hexdigest()}))
    rows, selected = [], None
    try:
        with lzma.open(out / 'episodes.jsonl.xz', 'wt', preset=3) as stream:
            for profile in config['profiles']:
                for seed in config['seeds']:
                    group = {}
                    for condition in config['conditions']:
                        ep = run_episode(config, condition, profile, seed)
                        stream.write(json.dumps(ep, sort_keys=True, separators=(',', ':')) + '\n')
                        group[condition['id']] = ep['summary']
                        rows.append({'profile': profile['id'], 'seed': seed, 'condition': condition['id'], **ep['summary']})
                    if selected is None and qualifies(group['R2'], group['R3'], group['R3_NO_RELAY']):
                        selected = {'profile': profile['id'], 'seed': seed, 'paired_summaries': group}
        if len(rows) != config['search']['network_count']:
            raise RuntimeError('Wrong campaign size')
        report = {'status': 'SELECTED_PENDING_CAUSAL_AND_A25_AUDIT' if selected else 'NO_ADMITTED_DYNAMIC_WITNESS',
                  'networks': len(rows), 'c3_records': len(rows)*config['agents']*config['epochs'],
                  'selected': selected, 'all_results': rows, 'ea_execution': 'NOT_RUN',
                  'episodes_sha256': hashlib.sha256((out/'episodes.jsonl.xz').read_bytes()).hexdigest()}
        (out / 'SUMMARY.json').write_text(json.dumps(report, indent=2) + '\n')
        (out / 'RUN_STATUS.json').write_text(json.dumps({'status': 'COMPLETE', 'networks': len(rows)}) + '\n')
        print(json.dumps({k: report[k] for k in ['status', 'networks', 'c3_records', 'ea_execution']}))
    except BaseException as error:
        (out / 'RUN_STATUS.json').write_text(json.dumps({'status': 'INCOMPLETE', 'completed_networks': len(rows), 'error_type': type(error).__name__}) + '\n')
        raise


if __name__ == '__main__':
    main()
