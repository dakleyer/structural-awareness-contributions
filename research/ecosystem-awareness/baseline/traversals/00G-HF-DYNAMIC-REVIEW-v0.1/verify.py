"""Constructed boundary/integration checks; never calls the stochastic campaign."""
import copy
import hashlib
import json
from unittest.mock import patch
import run


def main():
    config = json.loads((run.HERE / 'CONFIG.json').read_text())
    checks = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    condition = next(c for c in config['conditions'] if c['id'] == 'R3')
    stable = next(c for c in config['conditions'] if c['id'] == 'R2')
    profile = config['profiles'][0]
    check('declared_campaign_size', len(config['profiles'])*len(config['seeds'])*len(config['conditions']) == config['search']['network_count'])
    check('no_EA_arm', all('EA' not in c['id'] for c in config['conditions']))
    check('three_changes', config['epochs'] == 4)
    check('stable_authority', run.world_at(config, stable, 'A02', 0, 'direct') == run.world_at(config, stable, 'A02', 3, 'direct'))
    check('revocation', run.world_at(config, condition, 'A02', 0, 'direct')['allowed'] and not run.world_at(config, condition, 'A02', 1, 'direct')['allowed'])
    check('renewal', run.world_at(config, condition, 'A02', 3, 'direct')['allowed'])
    check('applicability_change', run.world_at(config, condition, 'A08', 1, 'direct')['applicable'] and not run.world_at(config, condition, 'A08', 2, 'direct')['applicable'])
    snapshot = run.authority_reply(config, condition, 'A02', 0, 'direct', 4)
    message = {'id': 'constructed', 'reported_success': True, 'stage': 'preparation'}
    view = {'agent': 'A02', 'step': 9, 'route': 'direct', 'finished': False, 'pending': False,
            'messages': [message]*8, 'snapshot': snapshot, 'known_version': 0, 'ttl': 10,
            'guard': True, 'fresh': False, 'gain': 100, 'cost': 3, 'latency': 1,
            'queries_left': 4, 'prepared': 2, 'preparation_units': 2, 'just_received': False}
    check('same_view_different_world_truth', snapshot['allowed'] and not run.world_at(config, condition, 'A02', 1, 'direct')['allowed'] and run.usable(snapshot, view))
    check('recipient_scope', not run.usable({**snapshot, 'subject': 'A03'}, view))
    check('route_scope', not run.usable({**snapshot, 'route': 'adapted'}, view))
    check('expiry_boundary', not run.usable(snapshot, {**view, 'step': 14}))
    check('revision_invalidates', not run.usable(snapshot, {**view, 'known_version': 1}))
    denial = {**view, 'snapshot': {**snapshot, 'allowed': False}}
    check('known_denial_not_overruled_by_social_pressure', all(run.decide(denial, s)['choice'] != 'ACT_T1' for s in range(1000, 1100)))
    invalid = {**view, 'snapshot': {**snapshot, 'applicable': False}}
    check('known_inapplicability_not_overruled', all(run.decide(invalid, s)['choice'] != 'ACT_T1' for s in range(1000, 1100)))
    check('unknown_requires_review', run.decide({**view, 'snapshot': None}, 1000)['choice'] == 'QUERY')
    check('budget_exhausted_continues_T0', run.decide({**view, 'snapshot': None, 'queries_left': 0}, 1000)['choice'] == 'WORK_T0')
    check('fresh_review_not_stale_reuse', run.decide({**view, 'fresh': True}, 1000)['choice'] == 'QUERY')
    fresh = {**view, 'fresh': True, 'just_received': True, 'snapshot': {**snapshot, 'observed_step': 8}}
    check('query_reply_resumes_intention', run.decide(fresh, 1000)['choice'] == 'ACT_T1')
    check('waiting_preserves_work', run.decide({**view, 'pending': True}, 1000)['choice'] == 'WORK_T0')
    check('completed_item_not_repeated', run.decide({**view, 'finished': True}, 1000)['choice'] == 'DONE')
    check('randomness_is_event_keyed', run.draw(1000, 'A02', 9, 'refresh') == run.draw(1000, 'A02', 9, 'refresh'))

    # Integration fixtures explicitly replace the policy with scripted actions.
    # They are software checks, not probabilistic evidence or selected witnesses.
    def scripted(view, seed):
        if view['finished']:
            return {'choice': 'DONE'}
        if view['pending']:
            return {'choice': 'WORK_T0'}
        if view['just_received']:
            return {'choice': 'ACT_T1'}
        local = view['step'] % config['rounds_per_epoch']
        return {'choice': 'PREPARE' if local < 2 else 'QUERY' if local == 2 else 'WORK_T0'}

    fixtures = []
    for c in [condition, {**condition, 'id': 'constructed_hard', 'hard': True}, {**condition, 'id': 'constructed_no_relay', 'relay': False}]:
        with patch.object(run, 'decide', scripted):
            ep = run.run_episode(config, c, profile, 1000)
        fixtures.append(ep)
        check(c['id'] + '_C3_complete', all(r['result']['record_status'] == 'COMPLETE' for r in ep['records']))
        check(c['id'] + '_budgets', all(s['queries'] <= config['budget_per_agent_per_epoch']['queries'] and s['publications'] <= config['budget_per_agent_per_epoch']['messages'] and s['attempts'] <= 1 for states in ep['epoch_states'] for s in states.values()))
        lookup = {m['id']: m for m in ep['messages']}
        deliveries = {}
        for t in ep['transmissions']:
            deliveries[(t['receiver'], t['message'])] = t['at']
        check(c['id'] + '_parent_chronology', all(lookup[p]['at'] < m['at'] and deliveries[(m['sender'], p)] < m['at'] for m in ep['messages'] for p in m['parents']))
        check(c['id'] + '_effect_agreement', sum(e['after'] is not None and not e['permission'] for e in ep['effects']) == ep['summary']['unauthorized_effect'])
    check('hard_barrier_never_bypassed', fixtures[1]['summary']['unauthorized_effect'] == 0 and fixtures[1]['summary']['unauthorized_attempt'] > 0)
    check('no_relay_keeps_origin_and_common_notices', len(fixtures[2]['transmissions']) == 1 + config['agents'] * config['epochs'] and all(t['sender'] in ('principal', 'originator') for t in fixtures[2]['transmissions']))
    check('nontrivial_local_outcomes', {x['success'] for x in fixtures[0]['ledger'] if x['kind'] == 'local_preparation'} == {True, False})
    check('actual_results_in_social_messages', {'preparation', 'final'} <= {m['stage'] for m in fixtures[0]['messages']})
    check('false_selection_rejected', not run.qualifies({'inadmissible_attempt': 0, 'inadmissible_effect': 0}, {'hf_operational_witness': 4, 'late_dependent_witnesses': []}, {'hf_operational_witness': 0}))
    result = {'status': 'PASS', 'checks': len(checks), 'names': checks,
              'scripted_integration_fixtures': len(fixtures), 'stochastic_campaign_networks': 0,
              'model_calls': 0, 'ea_execution': 'NOT_RUN',
              'source_sha256': {n: hashlib.sha256((run.HERE/n).read_bytes()).hexdigest() for n in ['CONFIG.json', 'run.py', 'verify.py']}}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
