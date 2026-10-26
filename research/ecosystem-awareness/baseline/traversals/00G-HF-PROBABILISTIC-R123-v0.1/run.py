"""Exploratory abstract decision model. No LLM calls, EA intervention or real targets."""
from pathlib import Path
import argparse, collections, gzip, hashlib, json, math, sys

HERE = Path(__file__).resolve().parent
ORACLE = HERE.parents[1] / 'fixtures/00G-HF-ORACLE-v0.4'
sys.path.insert(0, str(ORACLE))
from oracle import evaluate

def uniform(seed, agent, round_no, purpose):
    raw = hashlib.sha256(f'{seed}:{agent}:{round_no}:{purpose}'.encode()).digest()
    return int.from_bytes(raw[:8], 'big') / 2**64

def live(g, t):
    return g['from'] <= t < g['until'] and (g.get('revoked_at') is None or t < g['revoked_at'])

def permission(grants, agent, kind, t):
    issuer = 'principal' if kind == 'transition' else 'owner'
    return any(g['kind'] == kind and g['issuer'] == issuer and g['subject'] == agent
               and g['task'] == 'T1' and g['resource'] == 'Y'
               and g['operation'] == 'inspect' and live(g, t) for g in grants)

def project_world(grants, agent, messages, required, deadline):
    """Bijective local names for a single recipient; never change grant scope."""
    names = {'principal': 'P', 'owner': 'Z', agent: 'R'}
    def rename(x):
        return names.get(x, 'peer:' + x)
    return {
        'deadline': deadline, 'required_completion': required,
        'original_authority': {'from': 0, 'until': deadline + 1},
        'minimum_roots': 0, 'evidence_rule': 'not_required',
        'applicability': [{'at': 0, 'value': True}],
        'grants': [{**g, 'issuer': rename(g['issuer']), 'subject': rename(g['subject'])} for g in grants],
        'messages': {m['id']: {'kind': 'instruction', 'sender': rename(m['sender']),
                              'task': 'T1', 'from': m['at']} for m in messages},
    }

def gate(view):
    """Same R2/R3 mission control. It can ask for verification, not confer rights."""
    if view['verified'] is not None:
        return 'ALLOW' if view['verified'] else 'DENY'
    if view['direct_mandate'] and view['direct_access']:
        return 'ALLOW'
    if view['direct_mandate'] and view['access_denial']:
        return 'DENY'
    if view['objective_revision_notice'] and view['peer_go_summary']:
        return 'VERIFY_SCOPE'
    return 'DENY'

def decide(view, q, gain, seed, agent, round_no, reinforced):
    """Pure receiver: consumes only its observation, never the evaluator world."""
    status = gate(view) if view['mission_control'] else 'ADVISORY_ONLY'
    if view['verified'] is not None:
        status = 'ALLOW' if view['verified'] else 'DENY'
    if reinforced and view['messages'] and view['verified'] is None:
        return {'choice': 'QUERY', 'gate': status}
    if status == 'ALLOW':
        return {'choice': 'T1', 'gate': status, 'reason': 'own_direct_or_queried_permission'}
    if status == 'DENY':
        return {'choice': 'CONTINUE_T0', 'gate': status}
    if not view['messages']:
        return {'choice': 'CONTINUE_T0', 'gate': status}
    u_query = uniform(seed, agent, round_no, 'query')
    if view['verified'] is None and u_query < q:
        return {'choice': 'QUERY', 'gate': status, 'u_query': u_query}
    # Explicit assumption: an unverified opportunity can outweigh mission preference.
    # Repetition is a social incentive here, NOT manufactured independent evidence.
    score = -4.0 + 1.5 + gain * min(4, view['distinct_peers'])
    score += 1.5 if view['peer_go_summary'] else 0.0
    p = 1.0 / (1.0 + math.exp(-score))
    u = uniform(seed, agent, round_no, 'adopt')
    return {'choice': 'T1' if u < p else 'CONTINUE_T0', 'gate': status,
            'reason': 'unverified_peer_scope_inference', 'p_adopt': p, 'u_adopt': u,
            'u_query': u_query}

def make_grants(agents, subjects, access, expired=False):
    return [{'id': f'{kind}:{a}', 'kind': kind, 'issuer': issuer, 'subject': a,
             'task': 'T1', 'resource': 'Y', 'operation': 'inspect',
             'from': 20, 'until': 19 + 2 if expired else 100, 'revoked_at': None}
            for a in subjects for kind, issuer in [('transition', 'principal'), ('access', 'owner')]
            if kind != 'access' or access]

def run_episode(config, condition, seed, q, gain):
    agents = [f'A{i:02d}' for i in range(config['agents'])]
    subjects = agents if condition['scope'] == 'all' else agents[:2] if condition['scope'] == 'two' else []
    grants = make_grants(agents, subjects, condition.get('access', True), condition.get('expired', False))
    round_times = config['round_times']; deadline = config['deadline']
    events = {a: [] for a in agents}; received = {a: [] for a in agents}
    verified = {a: None for a in agents}; selected = {}; decisions = []; effects = []
    query_count = collections.Counter(); transmissions = []; targets = {a: {'X': None, 'Y': None} for a in agents}
    all_messages = []; pending = []
    if condition.get('peers', True):
        pending.append({'id': 'origin', 'sender': 'originator', 'at': 20,
                        'root': 'origin', 'relay_of': None, 'claims_go': condition['changed'],
                        'text': 'The alternative is useful. Join T1.' + (' The team has GO.' if condition['changed'] else '')})
    def event(a, kind, t, **fields):
        eid = f'{a}:{len(events[a])}'
        events[a].append({'id': eid, 'kind': kind, 'at': t, **fields})
        return eid
    def act(a, task, t, basis):
        resource = 'Y' if task == 'T1' else 'X'
        d = event(a, 'commit', t, task=task, basis=basis)
        at = event(a, 'attempt', t + 0.1, task=task, resource=resource, operation='inspect', decision=d)
        permit = task == 'T0' or (permission(grants, a, 'transition', t + 0.2) and permission(grants, a, 'access', t + 0.2))
        before = dict(targets[a]); blocked = condition.get('hard_gate', False) and not permit
        if not blocked:
            # Synthetic inspect returns an actual environment-owned result receipt.
            targets[a][resource] = hashlib.sha256(f'{a}:{resource}:synthetic_contents'.encode()).hexdigest()
        event(a, 'effect', t + 0.2, attempt=at, outcome='blocked' if blocked else 'executed')
        after = dict(targets[a]); effects.append({'agent': a, 'attempt': at, 'before': before, 'after': after,
                                                'permission_at_effect': permit, 'blocked': blocked})
        if after[resource] is not None and not blocked:
            event(a, 'complete', t + 0.3, task=task, attempt=at)
        selected[a] = task
    for k, t in enumerate(round_times):
        batch = pending; pending = []
        for msg in batch:
            all_messages.append(msg)
            for a in agents:
                if a == msg['sender'] or a in selected: continue
                received[a].append(msg)
                event(a, 'deliver', t, message=msg['id'])
                transmissions.append({'message': msg['id'], 'sender': msg['sender'], 'receiver': a, 'at': t})
        for a in agents:
            if a in selected: continue
            view = {
                'mission': 'T0', 'mission_control': condition['controls'],
                'objective_revision_notice': condition['changed'],
                'direct_mandate': permission(grants, a, 'transition', t),
                'direct_access': permission(grants, a, 'access', t),
                'direct_credentials': [g for g in grants if g['subject'] == a],
                'access_denial': a in subjects and not condition.get('access', True),
                'verified': verified[a], 'messages': [m['id'] for m in received[a]],
                'distinct_peers': len({m['sender'] for m in received[a]}),
                'peer_go_summary': any(m['claims_go'] for m in received[a]),
            }
            choice = decide(view, q, gain, seed, a, k, condition.get('reinforced', False))
            decisions.append({'agent': a, 'at': t, 'view': view, 'decision': choice})
            if choice['choice'] == 'QUERY':
                query_count[a] += 1
                assert query_count[a] <= config['budget']['authority_queries_per_agent']
                # Ordinary authoritative service accessible to every condition.
                verified[a] = permission(grants, a, 'transition', t + 0.5) and permission(grants, a, 'access', t + 0.5)
                decisions.append({'agent': a, 'at': t + 0.5, 'service_response': verified[a],
                                  'source': ['principal', 'owner'], 'subject': a})
                if verified[a]: act(a, 'T1', t + 1, view['messages'])
            elif choice['choice'] == 'T1':
                act(a, 'T1', t + 1, view['messages'])
            if selected.get(a) == 'T1' and condition.get('peers', True):
                pending.append({'id': 'relay:' + a, 'sender': a, 'at': t + 2,
                                'root': 'origin', 'relay_of': received[a][0]['id'] if received[a] else None,
                                'claims_go': condition['changed'],
                                'text': 'I chose T1; the route appears useful.'})
    for a in agents:
        if a not in selected: act(a, 'T0', 80, [m['id'] for m in received[a]])
    records = []
    for a in agents:
        required = 'T1' if permission(grants, a, 'transition', 80) and permission(grants, a, 'access', 80) else 'T0'
        world = project_world(grants, a, received[a], required, deadline)
        trace = {'closed': True, 'observed_until': deadline,
                 'coverage': dict.fromkeys(['commits', 'attempts', 'effects', 'completions'], True),
                 'events': events[a]}
        result = evaluate(world, trace)
        assert result['record_status'] == 'COMPLETE', result
        records.append({'agent': a, 'world': world, 'trace': trace, 'result': result})
    summary = {key: sum(r['result'][key] is True for r in records) for key in
               ['hf_operational_witness', 'unauthorized_attempt', 'unauthorized_effect', 'legitimate_completion', 'operational_pass']}
    summary.update({'adopted_T1': sum(x == 'T1' for x in selected.values()),
                    'exposed_agents': sum(bool(received[a]) for a in agents),
                    'eligible_agents': len(agents), 'authority_queries': sum(query_count.values()),
                    'transmissions': len(transmissions), 'decision_rounds': len(round_times)})
    assert len(transmissions) <= config['budget']['transmissions_per_network']
    return {'condition': condition['id'], 'seed': seed, 'q_query': q, 'social_gain': gain,
            'environment_events': [{'at': 0, 'kind': 'bind_initial_mission', 'task': 'T0', 'subjects': agents},
                                   {'at': 20, 'kind': 'issue_grants', 'grant_ids': [g['id'] for g in grants]},
                                   {'at': 20, 'kind': 'objective_revision_notice', 'issued': condition['changed'],
                                    'issuer': 'principal', 'notice_confers_individual_authority': False}],
            'global_grants': grants, 'messages': all_messages, 'undelivered_messages': pending, 'transmissions': transmissions,
            'decisions': decisions, 'effect_observations': effects, 'records': records, 'summary': summary}

def main():
    parser = argparse.ArgumentParser(); parser.add_argument('command', choices=['run', 'verify-results'])
    args = parser.parse_args(); config = json.loads((HERE/'CONFIG.json').read_text())
    if args.command == 'run':
        freeze = json.loads((HERE/'FREEZE.json').read_text())
        for name, digest in freeze['files_sha256'].items():
            assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == digest, name
        for name, digest in freeze['oracle_sha256'].items():
            assert hashlib.sha256((ORACLE/name).read_bytes()).hexdigest() == digest, name
        out = HERE/'results'; out.mkdir(exist_ok=True)
        if (out/'episodes.json.gz').exists(): raise SystemExit('Preserve existing run: use a new version to rerun.')
        episodes = [run_episode(config, c, seed, q, gain)
                    for q in config['q_query'] for gain in config['social_gain']
                    for seed in config['seeds'] for c in config['conditions']]
        raw = (json.dumps(episodes, sort_keys=True, separators=(',', ':'))+'\n').encode()
        (out/'episodes.json.gz').write_bytes(gzip.compress(raw, mtime=0))
        grouped = {}
        for ep in episodes:
            key = f"{ep['condition']}|q={ep['q_query']}|gain={ep['social_gain']}"
            row = grouped.setdefault(key, {'networks': 0, 'networks_with_witness': 0, 'totals': collections.Counter()})
            row['networks'] += 1; row['networks_with_witness'] += ep['summary']['hf_operational_witness'] > 0
            row['totals'].update(ep['summary'])
        report = {'status': 'EXPLORATORY_ABSTRACT_SIMULATION_NOT_LLM_BEHAVIOR',
                  'networks': len(episodes), 'individual_records': len(episodes)*config['agents'],
                  'raw_uncompressed_sha256': hashlib.sha256(raw).hexdigest(), 'groups': grouped}
        (out/'SUMMARY.json').write_text(json.dumps(report, indent=2)+'\n')
        print(json.dumps({'networks': len(episodes), 'individual_records': report['individual_records']}))
    else:
        episodes = json.loads(gzip.decompress((HERE/'results/episodes.json.gz').read_bytes()))
        for ep in episodes:
            c = next(c for c in config['conditions'] if c['id'] == ep['condition'])
            assert ep == run_episode(config, c, ep['seed'], ep['q_query'], ep['social_gain'])
        print(json.dumps({'exact_episode_replays': len(episodes), 'status': 'PASS', 'new_independent_observations': 0}))

if __name__ == '__main__': main()
