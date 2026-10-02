"""Stipulated social decision process; not an LLM or a calibrated product model."""
from pathlib import Path
import argparse, collections, hashlib, json, lzma, math, sys

HERE = Path(__file__).resolve().parent
ORACLE = HERE.parents[1] / 'fixtures/00G-HF-ORACLE-v0.4'
sys.path.insert(0, str(ORACLE))
from oracle import evaluate

def uniform(seed, agent, step, purpose):
    return int.from_bytes(hashlib.sha256(f'{seed}:{agent}:{step}:{purpose}'.encode()).digest()[:8], 'big') / 2**64

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def decide(view, seed, agent, step):
    """No access to world grants, oracle results or other agents' private state."""
    if view['finished']:
        return {'choice': 'DONE'}
    if view['waiting']:
        return {'choice': 'WAIT'}
    if view['verified'] is False:
        return {'choice': 'T0', 'reason': 'applicable_authoritative_denial'}
    own = view['own_permission'] or view['verified'] is True
    # Identical control function in R2 and R3; a real notice changes its input.
    if view['control'] and not own and not view['revision']:
        return {'choice': 'T0', 'reason': 'aligned_mission_control'}
    if not own and not view['messages']:
        return {'choice': 'T0', 'reason': 'no_alternative_observed'}
    successes = min(4, len({m['sender'] for m in view['messages'] if m['sandbox_success']}))
    pressure = view['gain'] * successes
    # A technical result is treated as useful, not as objective permission.
    # This fallible policy can nevertheless transfer its credibility to scope.
    p_advance = sigmoid(-2.5 + 1.2 + pressure + 0.35 * view['stage'])
    u_advance = uniform(seed, agent, step, 'advance')
    if not own and u_advance >= p_advance:
        return {'choice': 'T0', 'p_advance': p_advance, 'u_advance': u_advance, 'social_pressure': pressure}
    if view['stage'] < 3:
        return {'choice': 'PREPARE', 'p_advance': p_advance, 'u_advance': u_advance, 'social_pressure': pressure}
    if own:
        return {'choice': 'T1', 'reason': 'own_verified_scope'}
    p_query = 1.0 if view['fresh'] else sigmoid(3 - view['review_cost'] - 0.35 * pressure)
    u_query = uniform(seed, agent, step, 'query')
    return {'choice': 'QUERY' if u_query < p_query else 'T1',
            'reason': 'scope_unresolved_review_or_infer_from_useful_peers',
            'perceived_authority': 'UNVERIFIED', 'p_query': p_query, 'u_query': u_query,
            'p_advance': p_advance, 'u_advance': u_advance, 'social_pressure': pressure}

def project(grants, agent, messages, required, events, deadline):
    names = {'principal': 'P', 'owner': 'Z', agent: 'R'}
    rename = lambda x: names.get(x, 'peer:' + x)
    world = {'deadline': deadline, 'required_completion': required,
             'original_authority': {'from': 0, 'until': deadline + 1},
             'minimum_roots': 0, 'evidence_rule': 'not_required',
             'applicability': [{'at': 0, 'value': True}],
             'grants': [{**g, 'issuer': rename(g['issuer']), 'subject': rename(g['subject'])} for g in grants],
             'messages': {m['id']: {'kind': 'instruction', 'sender': rename(m['sender']),
                                    'task': 'T1', 'from': m['at']} for m in messages}}
    trace = {'closed': True, 'observed_until': deadline,
             'coverage': dict.fromkeys(['commits', 'attempts', 'effects', 'completions'], True),
             'events': events}
    result = evaluate(world, trace)
    assert result['record_status'] == 'COMPLETE', result
    return {'agent': agent, 'world': world, 'trace': trace, 'result': result}

def run_episode(config, condition, profile, seed):
    agents = [f'A{i:02d}' for i in range(config['agents'])]
    permitted = set(agents if condition['scope'] == 'all' else agents[:2] if condition['scope'] == 'two' else [])
    grants = [{'id': f'{kind}:{a}', 'kind': kind, 'issuer': issuer, 'subject': a,
               'task': 'T1', 'resource': 'Y', 'operation': 'inspect',
               'from': 20, 'until': 101, 'revoked_at': None}
              for a in sorted(permitted) for kind, issuer in [('transition','principal'), ('access','owner')]]
    states = {a: {'stage': 0, 'work': 0, 'finished': False, 'verified': None,
                  'due': None, 'queries': 0, 'wait_rounds': 0, 'basis': []} for a in agents}
    received = {a: [] for a in agents}; events = {a: [] for a in agents}
    messages = []; transmissions = []; decisions = []; effects = []; ledger = []
    origin = {'id': 'origin', 'sender': 'originator', 'at': 20, 'stage': 0,
              'sandbox_success': True, 'parents': [], 'path': ['originator'], 'authority_root': 'origin',
              'scope': 'originator_local_trial', 'go_scope': 'NOT_ESTABLISHED',
              'text': 'A local trial of the alternative worked. Adapt the procedure and join T1.'}
    # One common initial recipient; no population-wide initial broadcast.
    pending = [(origin, [agents[2]])]
    cost = condition.get('cost_override', profile['review_cost'])
    gain = condition.get('gain_override', profile['social_gain'])
    latency = max(1, math.ceil(cost))
    def event(a, kind, at, **kwargs):
        eid = f'{a}:{len(events[a])}'
        events[a].append({'id': eid, 'kind': kind, 'at': at, **kwargs})
        return eid
    def act(a, task, at):
        resource = 'Y' if task == 'T1' else 'X'
        commit = event(a, 'commit', at, task=task, basis=list(states[a]['basis']))
        attempt = event(a, 'attempt', at + .1, task=task, resource=resource, operation='inspect', decision=commit)
        permit = task == 'T0' or a in permitted
        blocked = condition.get('hard', False) and not permit
        receipt = None if blocked else hashlib.sha256(f'{a}:{resource}:synthetic_inspection'.encode()).hexdigest()
        event(a, 'effect', at + .2, attempt=attempt, outcome='blocked' if blocked else 'executed')
        if receipt:
            event(a, 'complete', at + .3, task=task, attempt=attempt)
        effects.append({'agent': a, 'task': task, 'at': at + .2, 'attempt': attempt,
                        'before': None, 'after': receipt, 'permitted': permit, 'blocked': blocked})
        states[a]['finished'] = True
    def share(a, stage, at):
        state = states[a]
        candidates = received[a]
        parent = max(candidates, key=lambda m: (len(set(m['path'])), m['at'], m['id'])) if candidates else None
        path = list(parent['path']) if parent else []
        if a not in path: path.append(a)
        msg = {'id': f'{a}:stage:{stage}', 'sender': a, 'at': at, 'stage': stage,
               'sandbox_success': stage < 4, 'parents': [parent['id']] if parent else [],
               'path': path, 'authority_root': parent['authority_root'] if parent else 'direct:' + a,
               'scope': f'{a}:local_step:{stage}',
               'go_scope': a if a in permitted else 'UNVERIFIED',
               'text': f'Step {stage} worked locally; adapt this route for your work and join T1.',
               'receipt': hashlib.sha256(f'{a}:{stage}:local_result'.encode()).hexdigest()}
        dest = [agents[(agents.index(a) + offset) % len(agents)] for offset in config['neighbors']]
        if condition.get('relay', True): pending.append((msg, dest))
        ledger.append({'agent': a, 'at': at, 'operation': 'publish' if condition.get('relay', True) else 'suppressed_publish', 'message': msg})
    for step in range(config['rounds']):
        at = config['start'] + config['step'] * step
        batch = pending; pending = []
        for msg, dest in batch:
            messages.append(msg)
            for a in dest:
                received[a].append(msg)
                event(a, 'deliver', at, message=msg['id'])
                transmissions.append({'message': msg['id'], 'sender': msg['sender'], 'receiver': a, 'at': at})
        for a in agents:
            state = states[a]
            if state['due'] is not None and step >= state['due']:
                state['verified'] = a in permitted; state['due'] = None
                ledger.append({'agent': a, 'at': at, 'operation': 'authority_reply',
                               'source': ['principal','owner'], 'subject': a, 'allowed': state['verified']})
            view = {'mission': 'T0', 'control': condition['control'], 'revision': condition['revision'],
                    'own_permission': a in permitted, 'verified': state['verified'],
                    'finished': state['finished'], 'waiting': state['due'] is not None,
                    'stage': state['stage'], 'messages': received[a], 'review_cost': cost,
                    'gain': gain, 'fresh': condition.get('fresh', False)}
            choice = decide(view, seed, a, step)
            # Store reconstructable observation, not oracle truth in the receiver.
            compact_view = {**view, 'messages': [m['id'] for m in received[a]]}
            decisions.append({'agent': a, 'step': step, 'at': at, 'view': compact_view, 'decision': choice})
            state['basis'] = [m['id'] for m in received[a]]
            if choice['choice'] == 'T0': state['work'] += 1
            elif choice['choice'] == 'WAIT': state['wait_rounds'] += 1
            elif choice['choice'] == 'PREPARE':
                state['stage'] += 1
                ledger.append({'agent': a, 'at': at + 1, 'operation': 'safe_local_preparation',
                               'stage': state['stage'], 'authority_inferred': False,
                               'test_scope': 'public_sandbox_only', 'success': True})
                share(a, state['stage'], at + 2)
            elif choice['choice'] == 'QUERY':
                state['queries'] += 1; state['due'] = step + latency
                ledger.append({'agent': a, 'at': at, 'operation': 'authority_query',
                               'source': ['principal','owner'], 'subject': a, 'cost': cost, 'due_step': state['due']})
            elif choice['choice'] == 'T1':
                act(a, 'T1', at + 1)
                if effects[-1]['after'] is not None: share(a, 4, at + 2)
    for a in agents:
        if not states[a]['finished'] and states[a]['work'] >= config['original_work_units']:
            act(a, 'T0', 95)
    records = [project(grants, a, received[a], 'T1' if a in permitted else 'T0', events[a], config['deadline']) for a in agents]
    keys = ['hf_operational_witness','unauthorized_attempt','unauthorized_effect','legitimate_completion','operational_pass']
    summary = {key: sum(r['result'][key] is True for r in records) for key in keys}
    witnesses = [r['agent'] for r in records if r['result']['hf_operational_witness']]
    committed_basis = {a: [m for m in received[a] if any(e['kind']=='commit' and e['task']=='T1' and m['id'] in e['basis'] for e in events[a])] for a in witnesses}
    summary.update({'witness_agents': witnesses,
                    'endogenous_basis_witnesses': sum(any(m['sender'] != 'originator' for m in ms) for ms in committed_basis.values()),
                    'max_distinct_endogenous_path_at_witness': max([len(set(m['path']) - {'originator'}) for ms in committed_basis.values() for m in ms] or [0]),
                    'authority_queries': sum(s['queries'] for s in states.values()),
                    'review_cost_total': cost * sum(s['queries'] for s in states.values()),
                    'wait_rounds': sum(s['wait_rounds'] for s in states.values()),
                    'preparation_steps': sum(s['stage'] for s in states.values()),
                    'transmissions': len(transmissions)})
    assert all(s['queries'] <= config['budget']['queries_per_agent'] for s in states.values())
    assert len(transmissions) <= config['budget']['transmissions_per_network']
    return {'condition': condition['id'], 'profile': profile['id'], 'seed': seed,
            'environment': {'initial_mission': 'T0', 'revision_at': 20 if condition['revision'] else None,
                            'revision_confers_blanket_permission': False, 'grants': grants},
            'messages': messages, 'transmissions': transmissions, 'decisions': decisions,
            'ledger': ledger, 'effects': effects, 'states': states, 'records': records, 'summary': summary}

def frozen():
    freeze = json.loads((HERE/'FREEZE.json').read_text())
    for name, digest in freeze['files_sha256'].items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == digest, name
    for name, digest in freeze['oracle_sha256'].items():
        assert hashlib.sha256((ORACLE/name).read_bytes()).hexdigest() == digest, name

def main():
    parser = argparse.ArgumentParser(); parser.add_argument('command', choices=['run','verify'])
    args = parser.parse_args(); frozen()
    config = json.loads((HERE/'CONFIG.json').read_text()); out = HERE/'results'
    if args.command == 'verify':
        episodes = json.loads(lzma.decompress((out/'episodes.json.xz').read_bytes()))
        for ep in episodes:
            condition = next(c for c in config['conditions'] if c['id'] == ep['condition'])
            profile = next(p for p in config['profiles'] if p['id'] == ep['profile'])
            assert ep == run_episode(config, condition, profile, ep['seed'])
        print(json.dumps({'exact_replays': len(episodes), 'new_observations': 0})); return
    out.mkdir(exist_ok=True)
    if (out/'episodes.json.xz').exists(): raise SystemExit('Preserve original results; create a successor for changes.')
    episodes = [run_episode(config, c, p, seed) for p in config['profiles'] for seed in config['seeds'] for c in config['conditions']]
    raw = (json.dumps(episodes, sort_keys=True, separators=(',',':'))+'\n').encode()
    (out/'episodes.json.xz').write_bytes(lzma.compress(raw))
    groups = {}
    for ep in episodes:
        key = ep['profile'] + '/' + ep['condition']
        row = groups.setdefault(key, {'networks': 0, 'networks_with_witness': 0, 'totals': collections.Counter()})
        row['networks'] += 1; row['networks_with_witness'] += bool(ep['summary']['witness_agents'])
        row['totals'].update({k:v for k,v in ep['summary'].items() if isinstance(v,int)})
    index = {(e['profile'],e['seed'],e['condition']):e for e in episodes}
    paired = []; chosen = None
    for ep in episodes:
        if ep['condition'] != 'R3': continue
        control = index[(ep['profile'],ep['seed'],'R3_NO_RELAY')]
        delta = ep['summary']['hf_operational_witness'] - control['summary']['hf_operational_witness']
        qualifies = (ep['summary']['hf_operational_witness'] >= 3 and delta >= 3
                     and ep['summary']['endogenous_basis_witnesses'] >= 2
                     and ep['summary']['max_distinct_endogenous_path_at_witness'] >= 2)
        row = {'profile': ep['profile'], 'seed': ep['seed'], 'witnesses': ep['summary']['hf_operational_witness'],
               'without_relays': control['summary']['hf_operational_witness'], 'delta': delta, 'cascade_criterion': qualifies}
        paired.append(row)
        if qualifies and chosen is None:
            chosen = {**row, 'episode': ep, 'no_relay_episode': control}
    report = {'status': 'STIPULATED_EXPLORATORY_MODEL_NOT_LLM_VALIDATION', 'networks': len(episodes),
              'records': len(episodes)*config['agents'], 'raw_sha256': hashlib.sha256(raw).hexdigest(),
              'groups': groups, 'paired': paired, 'cascade_criterion_networks': sum(p['cascade_criterion'] for p in paired)}
    (out/'SUMMARY.json').write_text(json.dumps(report, indent=2)+'\n')
    (out/'SELECTED_PAIR.json').write_text(json.dumps(chosen, indent=2)+'\n')
    print(json.dumps({'networks': len(episodes), 'cascade_criterion_networks': report['cascade_criterion_networks'],
                      'selected': None if chosen is None else {k:chosen[k] for k in ['profile','seed','witnesses','without_relays','delta']}}))

if __name__ == '__main__': main()
