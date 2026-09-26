"""Read-only adversarial audit probes, separate from the historical campaigns.

Successful execution means the documented observations reproduced, NOT that
the audited implementation passed these adversarial requirements. No existing
fixture, oracle, implementation, or committed trace is edited.
"""
from pathlib import Path
import argparse,copy,importlib,inspect,json,sys,tempfile
from dataclasses import replace
from datetime import timedelta

HERE=Path(__file__).resolve().parent
FIX=HERE.parent
BASE=FIX.parent
RESULTS=[]
def load(folder,name):
    sys.path.insert(0,str(FIX/folder))
    try: return importlib.import_module(name)
    finally: sys.path.pop(0)
def record(id,observation):
    RESULTS.append(dict(id=id,observation=observation))

def split_evidence(s):
    return s.evidence_fit
def split_residual(s):
    return s.residual_explicit

def main():
    s=load('RS-00E-Q1a','stage0_runner')
    facts=json.loads((s.HERE/'frozen_observations_v05.json').read_text())
    oracle=json.loads((s.HERE/'oracle_reference_v05.json').read_text())
    obs=s.frozen_observation(facts['branches']['Q1a-P1'],facts['registry'])
    result=s.conventional_b1(obs)
    corrupt=copy.deepcopy(obs)
    corrupt['reports'][0]['upstream_source_id']='CORRUPTED'
    events=s.play_events(corrupt,result)
    score=s.score('Q1a-P1',result,oracle['Q1a-P1'],corrupt)
    assert s.qualifier_loss_self_test(True)['disposition']=='PASS'
    assert s.qualifier_loss_self_test(False)['disposition']=='FAIL'
    assert not any(e.get('qualifier_loss_detected') for e in events)
    assert score['candidate_status']=='PASS'
    record('STAGE-HOOK',dict(injected='P -> CORRUPTED after adapter assessment, before event playback',hook_detected=False,score=score['candidate_status']))

    malformed=copy.deepcopy(result)
    malformed['posture']='HOLD'
    score=s.score('Q1a-P1',malformed,oracle['Q1a-P1'],obs)
    assert malformed['residual']==result['residual'] and malformed['affected_scope']==result['affected_scope']
    assert score['required_residual_scope_fields_retained']==0
    record('STAGE-METRIC',dict(only_change='posture becomes HOLD; residual and scope unchanged',reported_retained=0,denominator=3))

    malformed=copy.deepcopy(result)
    malformed['burden']={'processing_steps':999,'modelled_time_steps':-1}
    score=s.score('Q1a-P1',malformed,oracle['Q1a-P1'],obs)
    assert score['candidate_status']=='PASS'
    record('STAGE-BURDEN',dict(injected=malformed['burden'],candidate_status=score['candidate_status']))

    original=s.conventional_b1
    def wrong(o):
        x=original(o);x['posture']='HOLD';return x
    s.conventional_b1=wrong
    try:
        with tempfile.TemporaryDirectory() as td:
            error=None
            try: s.run(Path(td))
            except RuntimeError as e: error=str(e)
            files=sorted(p.name for p in Path(td).iterdir())
            assert error=='candidate failure: Q1a-P1/B1'
            assert not any('Q1a-' in f for f in files)
            record('STAGE-FAILURE-LOSS',dict(error=error,preserved_files=files,candidate_failure_trace_saved=False))
    finally: s.conventional_b1=original

    lpath=BASE/'00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1'
    sys.path.insert(0,str(lpath));v=importlib.import_module('verify_paired_symbolic');sys.path.pop(0)
    cases=json.loads((lpath/'00L_A10_PARES_CONTROLADOS.json').read_text())['cases']
    c=next(c for c in cases if c['id']=='00E')
    visible=dict(c['common'],**{c['factor']:'false'})
    v.preflight(visible,set(visible))
    outcome=v.evaluate('00E',visible)
    assert outcome[0]=='EXECUTE'
    record('00L-TYPE',dict(resolves_at_step_3='false (string)',preflight='accepted',route=outcome[0]))
    c=next(c for c in cases if c['id']=='00G')
    visible=dict(c['common'],**{c['factor']:''})
    v.preflight(visible,set(visible))
    route,peer,_=v.evaluate('00G',visible)
    assert route=='REQUALIFY' and peer=='TRANSITION_FRAME'
    record('00L-PEER-DIVERGES',dict(last_root='',route=route,strong_peer=peer))
    assert 'assert strong_peer == route' in inspect.getsource(v.verify)
    record('00L-AGREEMENT-GATE',dict(assertion='strong_peer == route',consequence='divergence aborts verify before final trace_jsonl write'))

    a2=load('00K-A2-P2-00E','ablation_A2')
    f=a2.SearchFixture(tuple(a2.EvidenceStep(True,False) for _ in range(3)),6,6)
    assert a2.ablated_search_until_capacity(f).value=='RESOURCE_EXHAUSTED'
    record('A2-SHORT-STREAM',dict(stream_length=3,hard_capacity=6,useful_horizon=6,weak_result='RESOURCE_EXHAUSTED',explicit_steps_available=3))

    a4=load('00K-A4-P4-00H','ablation_A4')
    peer4=load('00K-A4-P4-00H','a2l_strong_peer')
    finding=a4.Finding(4000,240000,True)
    def leaf(i,campaign,expiry=None,timestamp=None):
        return a4.LeafAction('ACCOUNT-'+str(i),40,a4.LeafGrant('CASE-'+str(i),50,campaign,expiry or a4.NOW+timedelta(days=2)),timestamp or a4.NOW)
    uniform=[leaf(0,'X'),leaf(1,'X')]
    mixed=[*uniform,leaf(2,'Y')]
    assert a4.route_q_decision(finding,uniform,{}).value=='DBC_REPOSITION_RECONTRACT'
    assert a4.route_q_decision(finding,mixed,{}).value=='DBC_EXECUTE'
    assert peer4.a2l_strong_peer_decision(finding,mixed,{}).value=='DBC_EXECUTE'
    record('A4-MIXED-ROOTS',dict(before=['X','X'],after=['X','X','Y'],registry={},before_result='DBC_REPOSITION_RECONTRACT',after_result='DBC_EXECUTE',strong_peer='DBC_EXECUTE'))

    registry={'X':a4.RootCampaignAuthority('OTHER','OWNER',True,a4.NOW+timedelta(days=2))}
    assert a4.route_q_decision(finding,uniform,registry).value=='DBC_EXECUTE'
    record('A4-ROOT-SCOPE',dict(lookup_key='X',root_campaign_ref='OTHER',result='DBC_EXECUTE',boundary='registry integrity assumed, not validated'))
    late=[leaf(0,'X',a4.NOW+timedelta(seconds=1),a4.NOW+timedelta(seconds=2))]
    registry={'X':a4.RootCampaignAuthority('X','OWNER',True,a4.NOW+timedelta(seconds=1))}
    assert a4.route_q_decision(finding,late,registry).value=='DBC_EXECUTE'
    assert not a4.check_P5_leaf_revalidation(late,at_time=late[0].timestamp)
    record('A4-TIME',dict(expiry_seconds_after_NOW=1,actuation_seconds_after_NOW=2,route_result='DBC_EXECUTE',explicit_at_action_check=False))
    burst=[leaf(0,None)]+[leaf(i,None,timestamp=a4.NOW+timedelta(hours=2,seconds=i)) for i in range(1,12)]
    assert a4.native_rate_cap_check(burst,10)
    record('A4-RATE-WINDOW',dict(first_hour_count=1,later_hour_count=11,max_per_hour=10,check_passed=True))

    a6=load('00K-A6-P6-00G','ablation_A6')
    claims=[a6.Claim('a',a6.CANDIDATE_FRAME,'R1',True,True,.95),a6.Claim('b',a6.CANDIDATE_FRAME,'R2',True,True,.95)]
    wrong_authority=replace(a6.AUTHORITY,target_frame='OTHER')
    assert a6.route_q(claims,wrong_authority).value=='PRESERVE_CURRENT_FRAME'
    assert a6.strong_peer_source_independence(claims,wrong_authority).value=='TRANSITION_FRAME'
    record('A6-PEER-SCOPE',dict(authority_target='OTHER',route='PRESERVE_CURRENT_FRAME',peer='TRANSITION_FRAME'))
    repair6=load('00K-A6-P6-00G','p6_serious_repairs')
    cs,g=repair6.genuine_independent()
    invalid=[replace(c,signed=False,fresh=False,confidence=0) for c in cs]
    assert repair6.dependency_graph_peer(invalid,g).value=='TRANSITION'
    record('A6-GRAPH-QUALIFICATION',dict(all_claims_unsigned_stale_low_confidence=True,peer='TRANSITION',boundary='dependency-only function; not a complete conforming route'))

    k=load('00K-cross-scenario-independent','kernels')
    assert k.p5_material_basis_current({}, {}, ('freeze_active',))
    assert k.p5_material_basis_current({'freeze_active':None},{'freeze_active':None},('freeze_active',))
    record('CROSS-P5-MISSING',dict(qualified={},current={},required=['freeze_active'],current_basis=True,null_null_also_true=True))
    kp=load('00K-cross-scenario-independent','kernels_p1_p3')
    assert kp.p2_bounded_resolution((True,False),-1)=='RESOLVED'
    record('CROSS-P2-NEGATIVE-BUDGET',dict(budget=-1,stream=[True,False],result='RESOLVED',boundary='invalid input not guarded'))

    audit=load('00K-FORMAL/requirement-sufficiency','audit_requirement_sufficiency')
    model=load('00K-FORMAL/requirement-sufficiency','requirement_sufficiency_model')
    for fn in (split_evidence,split_residual): audit.assert_no_target_shortcut(fn,model.p1)
    assert all((split_evidence(x) and split_residual(x))==model.p1(x) for x in model.states(('evidence_fit','residual_explicit')))
    record('A23-DISTRIBUTED-SHORTCUT-LIMIT',dict(each_clause_passes_guard=True,conjunction_equals_target=True,interpretation='guard is clause-local; source fidelity still requires semantic review, not a new disproof of finite implication'))

    cube=load('00K-FORMAL/full-cube','full_cube_model')
    yes=cube.construct((1,1,1,1,1,1));no=cube.construct((1,1,0,1,1,1))
    assert yes.records==no.records and yes.used_records==no.used_records
    assert cube.signature(yes)==(1,1,1,1,1,1) and cube.signature(no)==(1,1,0,1,1,1)
    assert not hasattr(no,'conflict') and not hasattr(no.inquiry,'edges')
    assert not any(cube.Q_UNRES in r.supports for r in no.records.values())
    record('A22-COHERENCE-BRIDGE',dict(records_identical=True,changed_input='Inquiry.material_to_action',P3_before=True,P3_after=False,conflict_relation_represented=False,inquiry_graph_represented=False,interpretation='64 signatures reproduce in simplified model; no executable check of A20 B8 derived conflict or the stated background theory'))

    tr=load('00K-TRACE','validate_traceability')
    old=copy.deepcopy(tr.MANIFEST)
    try:
        for p in tr.MANIFEST['principles'].values(): p['scenario']='NOT_THE_SCENARIO'
        tr.main()
        record('TRACE-LABEL-CHECK',dict(all_scenario_labels='NOT_THE_SCENARIO',validator='PASS',boundary='path/graph integrity only'))
    finally: tr.MANIFEST=old
    cl=load('00K-CLOSURE','validate_closure')
    old=copy.deepcopy(cl.M)
    try:
        cl.M['requirement_language']['admitted_atoms']={}
        cl.main()
        record('CLOSURE-EMPTY-ATOMS',dict(admitted_atoms={},validator='PASS',coverage='0/0',boundary='no lock on expected atom set'))
    finally: cl.M=old
    print(json.dumps(dict(audited_commit='8f17843c568114f31cc0ad486b4a1303396021e6',probe_count=len(RESULTS),results=RESULTS),indent=2))
    return dict(audited_commit='8f17843c568114f31cc0ad486b4a1303396021e6',probe_count=len(RESULTS),results=RESULTS)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=main()
    if args.output: args.output.write_text(json.dumps(result,indent=2)+'\n')
