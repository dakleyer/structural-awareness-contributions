"""Regression tests for A13 counterexamples; separate from the historical 379.

Expected outcomes are explicit assertions, never inferred from Route-Q/peer
agreement. Tests of the harness deliberately inject wrong output and crashes.
"""
from pathlib import Path
from copy import deepcopy
from dataclasses import replace
from datetime import timedelta
import importlib
import json
import sys
import pytest

FIX = Path(__file__).resolve().parent.parent
BASE = FIX.parent

def load(folder, name):
    sys.path.insert(0, str(FIX / folder))
    try:
        return importlib.import_module(name)
    finally:
        sys.path.pop(0)

stage = load('RS-00E-Q1a', 'stage0_runner')
a2 = load('00K-A2-P2-00E', 'ablation_A2')
a4 = load('00K-A4-P4-00H', 'ablation_A4')
peer4 = load('00K-A4-P4-00H', 'a2l_strong_peer')
a6 = load('00K-A6-P6-00G', 'ablation_A6')
graph6 = load('00K-A6-P6-00G', 'p6_serious_repairs')
k = load('00K-cross-scenario-independent', 'kernels')
kp = load('00K-cross-scenario-independent', 'kernels_p1_p3')
tr = load('00K-TRACE', 'validate_traceability')
cl = load('00K-CLOSURE', 'validate_closure')
sys.path.insert(0, str(BASE / '00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1'))
v = importlib.import_module('verify_paired_symbolic')
sys.path.pop(0)

@pytest.fixture
def observed():
    facts = json.loads((stage.HERE / 'frozen_observations_v05.json').read_text())
    oracle = json.loads((stage.HERE / 'oracle_reference_v05.json').read_text())['Q1a-P1']
    obs = stage.frozen_observation(facts['branches']['Q1a-P1'], facts['registry'])
    return obs, stage.conventional_b1(obs), oracle

@pytest.mark.parametrize('mutation', ['changed', 'missing', 'dropped_report', 'duplicate_report'])
def test_handoff_checks_pre_adapter_snapshot(observed, mutation):
    obs, candidate, oracle = observed
    expected = stage.handoff_snapshot(obs)
    corrupt = deepcopy(obs)
    if mutation == 'changed':
        corrupt['reports'][0]['upstream_source_id'] = 'CORRUPTED'
    elif mutation == 'missing':
        del corrupt['reports'][0]['upstream_source_id']
    elif mutation == 'dropped_report':
        corrupt['reports'].pop()
    else:
        corrupt['reports'][1] = deepcopy(corrupt['reports'][0])
    events = stage.play_events(corrupt, candidate, expected)
    assert any(e.get('qualifier_loss_detected') for e in events)
    assert stage.score('Q1a-P1', candidate, oracle, obs, events)['candidate_status'] == 'FAIL'

@pytest.mark.parametrize('field,expected', [('posture', 3), ('present', 2), ('reason', 2), ('reason_whitespace', 2), ('reason_nontext', 2), ('affected_scope', 2)])
def test_residual_metric_counts_fields_not_overall_pass(observed, field, expected):
    obs, candidate, oracle = observed
    if field == 'reason_whitespace':
        candidate['residual']['reason'] = ' '
    elif field == 'reason_nontext':
        candidate['residual']['reason'] = 1
    elif field in ('present', 'reason'):
        candidate['residual'][field] = False if field == 'present' else ''
    else:
        candidate[field] = 'WRONG'
    score = stage.score('Q1a-P1', candidate, oracle, obs)
    assert score['candidate_status'] == 'FAIL'
    assert score['required_residual_scope_fields_retained'] == expected

@pytest.mark.parametrize('processing,time', [(999, 4), (4, -1), (-1, 4), (4, 999), (True, 4), (4, 1.5)])
def test_burden_rejects_invalid_and_over_limit(observed, processing, time):
    obs, candidate, oracle = observed
    candidate['burden'] = {'processing_steps': processing, 'modelled_time_steps': time}
    assert stage.score('Q1a-P1', candidate, oracle, obs)['candidate_status'] == 'FAIL'

def test_burden_matches_event_count(observed):
    obs, candidate, oracle = observed
    events = stage.play_events(obs, candidate, stage.handoff_snapshot(obs))
    candidate['burden'] = {'processing_steps': 1, 'modelled_time_steps': 1}
    assert stage.score('Q1a-P1', candidate, oracle, obs, events)['candidate_status'] == 'FAIL'

@pytest.mark.parametrize('kind', ['wrong_posture', 'crash', 'nondeterministic', 'mutate_input', 'invalid_trace_number'])
def test_run_preserves_failed_repeats_and_other_candidates(tmp_path, monkeypatch, kind):
    original = stage.conventional_b1
    calls = 0
    def faulty(obs):
        nonlocal calls
        calls += 1
        if kind == 'crash':
            raise ValueError('injected adapter error')
        result = original(obs)
        if kind == 'invalid_trace_number':
            result['burden']['modelled_time_steps'] = 1.5
        if kind == 'wrong_posture' or (kind == 'nondeterministic' and calls % 2):
            result['posture'] = 'HOLD'
        if kind == 'mutate_input':
            obs['reports'][0]['upstream_source_id'] = 'CORRUPTED'
        return result
    monkeypatch.setattr(stage, 'conventional_b1', faulty)
    with pytest.raises(RuntimeError, match='all traces preserved'):
        stage.run(tmp_path)
    traces = [json.loads(p.read_text()) for p in tmp_path.glob('Q1a-*.json')]
    assert len(traces) == 12
    assert all(t['post_run_evaluation']['candidate_status'] == 'PASS' for t in traces if t['configuration'] == 'B3')
    assert any(t['post_run_evaluation']['candidate_status'] != 'PASS' for t in traces if t['configuration'] == 'B1')
    manifest = json.loads((tmp_path / 'manifest.json').read_text())
    assert manifest['failures'] and len(manifest['trace_sha256']) == 12
    if kind == 'invalid_trace_number':
        assert all('rejected_trace_representation' in t for t in traces if t['configuration'] == 'B1')
    if kind == 'nondeterministic':
        assert any('NONDETERMINISTIC' in f for f in manifest['failures'])

def test_stage_positive_replay(tmp_path):
    stage.run(tmp_path)
    manifest = json.loads((tmp_path / 'manifest.json').read_text())
    assert manifest['failures'] == []
    for branch in stage.BRANCHES:
        for config in stage.CONFIGS:
            assert (tmp_path / f'{branch}_{config}_repeat1.json').read_bytes() == (tmp_path / f'{branch}_{config}_repeat2.json').read_bytes()
    assert manifest['summary']['B1']['candidate_passes'] == 3

@pytest.mark.parametrize('value', ['false', 0, 1, [], {}])
def test_preflight_rejects_non_boolean(value):
    with pytest.raises(v.IncompleteObservation):
        v.preflight({'resolves_at_step_3': value}, {'resolves_at_step_3'})

@pytest.mark.parametrize('key,value', [('last_root', ''), ('base_root', ' '), ('message_count', 0), ('max_steps', -1), ('hard_capacity', True)])
def test_preflight_rejects_domain_errors(key, value):
    with pytest.raises(v.IncompleteObservation):
        v.preflight({key: value}, {key})

@pytest.mark.parametrize('bad_arm', ['route', 'strong_peer', 'both'])
def test_pair_disagreements_scored_against_oracle_and_saved(tmp_path, monkeypatch, bad_arm):
    original = v.evaluate
    def wrong(case, obs):
        route, peer, weak = original(case, obs)
        if case == '00E':
            if bad_arm in ('route', 'both'): route = 'WRONG'
            if bad_arm in ('strong_peer', 'both'): peer = 'WRONG'
        return route, peer, weak
    monkeypatch.setattr(v, 'evaluate', wrong)
    output = tmp_path / 'traces.jsonl'
    with pytest.raises(AssertionError, match='branch traces preserved'):
        v.verify(output)
    traces = [json.loads(line) for line in output.read_text().splitlines()]
    assert len(traces) == 12
    for trace in traces[:2]:
        assert trace['matches_expected']['route'] == (bad_arm == 'strong_peer')
        assert trace['matches_expected']['strong_peer'] == (bad_arm == 'route')
        assert trace['route_peer_agreement'] == (bad_arm == 'both')

@pytest.mark.parametrize('length,capacity,expected', [(3, 6, 'EVIDENCE_STREAM_ENDED'), (6, 6, 'RESOURCE_EXHAUSTED'), (0, 6, 'EVIDENCE_STREAM_ENDED'), (1, 0, 'RESOURCE_EXHAUSTED')])
def test_a2_exhaustion_requires_capacity(length, capacity, expected):
    fixture = a2.SearchFixture(tuple(a2.EvidenceStep(True, False) for _ in range(length)), capacity, 6)
    assert a2.ablated_search_until_capacity(fixture).value == expected

def leaf(i, ref, expiry=None, timestamp=None):
    return a4.LeafAction(str(i), 40, a4.LeafGrant(str(i), 50, ref, expiry or a4.NOW + timedelta(days=2)), timestamp or a4.NOW)

def root(ref, expiry=None):
    return a4.RootCampaignAuthority(ref, 'OWNER', True, expiry or a4.NOW + timedelta(days=2))

@pytest.mark.parametrize('route', [a4.route_q_decision, peer4.a2l_strong_peer_decision])
@pytest.mark.parametrize('case,expected', [('mixed_missing', 'DBC_REPOSITION_RECONTRACT'), ('mixed_authorized', 'DBC_EXECUTE'), ('mismatched_ref', 'DBC_REPOSITION_RECONTRACT'), ('leaf_expired', 'DBC_REPOSITION_RECONTRACT'), ('root_expired', 'DBC_REPOSITION_RECONTRACT'), ('exact_expiry', 'DBC_REPOSITION_RECONTRACT'), ('independent', 'DBC_EXECUTE')])
def test_a4_batch_authority_and_action_time(route, case, expected):
    actions = [leaf(0, 'X'), leaf(1, 'X'), leaf(2, 'Y')]
    registry = {'X': root('X'), 'Y': root('Y')}
    if case == 'mixed_missing': registry = {}
    if case == 'mismatched_ref': registry['X'] = root('OTHER')
    if case in ('leaf_expired', 'root_expired', 'exact_expiry'):
        expiry = a4.NOW + timedelta(seconds=1)
        timestamp = expiry if case == 'exact_expiry' else expiry + timedelta(seconds=1)
        actions = [leaf(0, 'X', expiry if case != 'root_expired' else None, timestamp)]
        if case == 'root_expired': registry['X'] = root('X', expiry)
    if case == 'independent': actions = [leaf(0, None), leaf(1, None)]
    assert route(a4.Finding(4000, 240000, True), actions, registry).value == expected

def test_rate_limit_sees_later_burst_and_exact_hour_boundary():
    burst = [leaf(0, None)] + [leaf(i, None, timestamp=a4.NOW + timedelta(hours=2, seconds=i)) for i in range(1, 12)]
    assert not a4.native_rate_cap_check(list(reversed(burst)), 10)
    assert a4.native_rate_cap_check(burst, 11)
    exact = [leaf(0, None), leaf(1, None, timestamp=a4.NOW + timedelta(hours=1))]
    assert a4.native_rate_cap_check(exact, 1)

@pytest.mark.parametrize('case,expected', [('wrong_authority', 'PRESERVE_CURRENT_FRAME'), ('empty_source', 'REQUALIFY'), ('valid', 'TRANSITION_FRAME')])
def test_a6_peer_scope_and_provenance(case, expected):
    claims = [a6.Claim('a', a6.CANDIDATE_FRAME, 'R1', True, True, .95), a6.Claim('b', a6.CANDIDATE_FRAME, 'R2', True, True, .95)]
    authority = a6.AUTHORITY
    if case == 'wrong_authority': authority = replace(authority, target_frame='OTHER')
    if case == 'empty_source': claims[-1] = replace(claims[-1], source_lineage='')
    assert a6.strong_peer_source_independence(claims, authority).value == expected
    assert a6.route_q(claims, authority).value == expected

@pytest.mark.parametrize('field,value', [('signed', False), ('fresh', False), ('confidence', 0)])
def test_graph_peer_does_not_count_unqualified_claims(field, value):
    claims, graph = graph6.genuine_independent()
    assert graph6.dependency_graph_peer(claims, graph) == graph6.Disposition.TRANSITION
    invalid = [replace(c, **{field: value}) for c in claims]
    assert graph6.dependency_graph_peer(invalid, graph) == graph6.Disposition.PRESERVE

@pytest.mark.parametrize('qualified,current,keys,expected', [({}, {}, ('freeze',), False), ({'freeze': None}, {'freeze': None}, ('freeze',), False), ({'freeze': False}, {'freeze': False}, ('freeze',), True), ({'freeze': False}, {'freeze': True}, ('freeze',), False), ({'freeze': False}, {'freeze': 0}, ('freeze',), False), ({}, {}, (), False)])
def test_p5_missing_unknown_changed_and_valid(qualified, current, keys, expected):
    assert k.p5_material_basis_current(qualified, current, keys) is expected

@pytest.mark.parametrize('budget', [-1, True, 1.5])
def test_p2_rejects_invalid_budget(budget):
    with pytest.raises(ValueError): kp.p2_bounded_resolution((True, False), budget)

def test_p2_zero_and_valid_budget():
    assert kp.p2_bounded_resolution((True, False), 0) == 'BOUNDED_NO_CONCLUSION'
    assert kp.p2_bounded_resolution((False, True), 1) == 'BOUNDED_NO_CONCLUSION'
    assert kp.p2_bounded_resolution((False, True), 2) == 'RESOLVED'

@pytest.mark.parametrize('mutation', ['scenario_label', 'scenario_path'])
def test_traceability_rejects_wrong_scenario(monkeypatch, mutation):
    manifest = deepcopy(tr.MANIFEST)
    if mutation == 'scenario_label': manifest['principles']['P1']['scenario'] = '00E'
    else: manifest['principles']['P1']['scenario_file'] = manifest['principles']['P2']['scenario_file']
    monkeypatch.setattr(tr, 'MANIFEST', manifest)
    with pytest.raises(AssertionError): tr.main()

@pytest.mark.parametrize('mutation', ['empty', 'delete_atom', 'duplicate_atom'])
def test_closure_rejects_shrunk_or_duplicated_domain(monkeypatch, mutation):
    manifest = deepcopy(cl.M)
    atoms = manifest['requirement_language']['admitted_atoms']
    if mutation == 'empty': atoms.clear()
    if mutation == 'delete_atom': atoms['QUALIFY'].pop()
    if mutation == 'duplicate_atom': atoms['QUALIFY'].append(atoms['QUALIFY'][0])
    monkeypatch.setattr(cl, 'M', manifest)
    with pytest.raises(AssertionError): cl.main()

def test_positive_structural_manifests():
    assert tr.main() == 0
    assert cl.main() == 0
