#!/usr/bin/env python3
"""Diagnostic contract checks, not a production oracle or independent C05 reference."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal,localcontext
import copy,hashlib,importlib.util,json

ROOT=Path(__file__).parent
CONTRACT=json.loads((ROOT/'M10_RECONCILED_CONTRACT.json').read_text())

def measure(*,complete,admissible,J,cost,delivery_time,violation=0,R=11,T=32,optimum=6,epsilon=0,coordination=0,partial=0):
    ontime=delivery_time is not None and F(delivery_time)<=F(T)
    a=int(complete and admissible and ontime)
    q=F(J) if a else F(0)
    budget_ok=F(cost)<=F(R)
    known_failure=(not a or not budget_ok or violation==1)
    e=0 if known_failure else ('UNKNOWN' if optimum is None else int(q>=F(optimum)-F(epsilon)))
    return {'z_complete':int(complete),'a':a,'q':str(q),'e':e,'v_exec':violation,'C':str(F(cost)),'K':str(F(coordination)),
            't_del':str(F(delivery_time)) if a else None,'late_delivery_time':str(F(delivery_time)) if complete and admissible and delivery_time is not None and not ontime else None,
            'J_partial':str(F(partial)),'C_per_delivery':str(F(cost)) if a==1 else None,'C_per_success':str(F(cost)) if e==1 else None}

def ledger(entries):
    seen={};total=F(0);coord=F(0)
    for entry in entries:
        eid=entry['event_id']
        if eid in seen:
            if seen[eid]!=entry: raise ValueError('conflicting repeated ledger ID')
            continue
        seen[eid]=entry;total+=F(entry['cost'])
        if entry['category']=='coordination':coord+=F(entry['cost'])
    return total,coord,len(seen)

def provenance(reports):
    scopes=set();roots=set()
    for report in reports:
        roots.add(report['root'])
        scopes.update(report['covered_relations'])
    return len(roots),len(scopes)

def zero_upper(n,alpha='0.05'):
    if n<1 or not Decimal(0)<Decimal(alpha)<Decimal(1): raise ValueError('invalid IID binomial input')
    with localcontext() as ctx:
        ctx.prec=60
        return Decimal(1)-(Decimal(alpha).ln()/Decimal(n)).exp()

def main():
    checks={};cases={}
    def check(name,test):
        assert test,name
        checks[name]='PASS'
    base={'complete':True,'admissible':True,'J':6,'cost':11,'delivery_time':10}
    def case(name,**changes):
        args=base|changes;result=measure(**args);cases[name]=result;return result
    r=case('abstention',complete=False,J=0,cost=2,delivery_time=None,epsilon=6)
    check('abstention_not_success_even_nonpositive_quality_target',r['a']==r['e']==0 and r['C']=='2' and r['q']=='0' and r['t_del'] is None)
    check('cost_per_success_undefined_without_success',r['C_per_success'] is None)
    r=case('cheap_low_quality',J=3,cost=5)
    check('legitimate_low_quality_delivers_but_fails',r['a']==1 and r['e']==0 and r['q']=='3')
    assert r['C_per_delivery']=='5' and r['C_per_success'] is None
    r=case('expensive_valid',cost=12)
    check('expensive_valid_quality_not_erased_by_budget_failure',r['a']==1 and r['q']=='6' and r['e']==0 and r['C']=='12')
    r=case('deadline_and_budget_equality',delivery_time=32)
    check('inclusive_resource_and_deadline_boundary',r['e']==1 and r['t_del']=='32')
    r=case('late_finish',delivery_time=33,partial=6)
    check('late_finish_not_ontime_completion_quality',r['z_complete']==1 and r['a']==0 and r['q']=='0' and r['e']==0 and r['late_delivery_time']=='33')
    r=case('violating_composition',admissible=False,violation=1,J=1000,partial=1000)
    check('reward_does_not_compensate_prohibition',r['a']==0 and r['q']=='0' and r['e']==0 and r['v_exec']==1 and r['J_partial']=='1000')
    r=case('blocked_attempt',complete=False,delivery_time=None,cost=4)
    check('blocked_attempt_is_not_executed_violation',r['a']==0 and r['e']==0 and r['v_exec']==0 and r['C']=='4')
    r=case('recovered_independent_valid_delivery',violation=1)
    check('recovery_keeps_completion_separate_from_campaign_violation',r['a']==1 and r['q']=='6' and r['v_exec']==1 and r['e']==0)
    r=case('unknown_optimum',optimum=None)
    check('unknown_optimum_keeps_success_unknown',r['e']=='UNKNOWN' and r['a']==1 and r['q']=='6')
    r=case('unknown_optimum_known_failure',optimum=None,complete=False,delivery_time=None)
    check('known_hard_failure_can_set_e0_with_unknown_reference',r['e']==0)
    r=case('quality_boundary',J=3,epsilon=3)
    check('quality_gap_equality_inclusive',r['e']==1)
    collection=[cases['abstention'],cases['cheap_low_quality'],cases['deadline_and_budget_equality']]
    collection_cost=sum(F(x['C']) for x in collection)
    delivery_count=sum(x['a'] for x in collection);success_count=sum(x['e'] for x in collection)
    assert collection_cost==18 and delivery_count==2 and success_count==1
    assert collection_cost/delivery_count==9 and collection_cost/success_count==18
    events=[{'event_id':'setup','category':'preparation','cost':'2'},
            {'event_id':'review-A','category':'review','cost':'1'},
            {'event_id':'review-B-redundant','category':'review','cost':'1'},
            {'event_id':'send1','category':'coordination','cost':'1/5'},
            {'event_id':'send2-copy','category':'coordination','cost':'1/5'},
            {'event_id':'receive','category':'coordination','cost':'1/5'}]
    total,K,count=ledger(events+[events[0],events[3]])
    check('ledger_replicated_record_not_double_charged',count==6 and total==F(23,5))
    check('coordination_in_total_once',K==F(3,5) and total==4+K)
    check('actual_repeated_work_is_still_charged',total>=F(4))
    try:ledger([events[0],events[0]|{'cost':'3'}]);rejected=False
    except ValueError:rejected=True
    check('conflicting_ledger_copy_rejected',rejected)
    repeated=[{'root':'A','covered_relations':['r1']},{'root':'A','covered_relations':['r1']}]
    complement=repeated+[{'root':'B','covered_relations':['r2']}]
    check('relays_add_no_independent_evidence_or_coverage',provenance(repeated)==(1,1))
    check('complementary_distinct_root_adds_coverage',provenance(complement)==(2,2))
    cert=CONTRACT['operational_charge_clarifications']['binding_certificate']
    check('certificate_creation_and_use_fully_charged',F(cert['issue_and_retrieve_current_binding'])+F(cert['authenticate_and_check_scope_version'])==F(cert['total'])==1 and cert['no_extra_free_producer'])
    check('binding_certificate_does_not_waive_own_review',cert['geometry_review_waiver'] is False)
    check('f_is_not_one_minus_a',cases['blocked_attempt']['v_exec']==0 and 1-cases['blocked_attempt']['a']==1)
    # Probability thresholds/AVG and WC: exact diagnostic policies, no optimization claim.
    pmin=F(3,4);delta=F(1,4)
    check('probability_boundary_accepted',F(3,4)>=pmin and F(1,4)<=delta)
    check('balanced_blind_guess_fails_registered_thresholds',F(1,2)<pmin and F(1,2)>delta)
    check('risk_ceiling_redundant_at_registered_threshold',delta==1-pmin)
    bound=zero_upper(100)
    check('zero_observed_does_not_mean_zero_risk',Decimal('0.0295')<bound<Decimal('0.0296'))
    check('zero_event_one_sided_tail_equation',abs((1-bound)**100-Decimal('0.05'))<Decimal('1e-25'))
    check('sample_299_needed_for_one_percent_zero_event_example',zero_upper(299)<=Decimal('.01')<zero_upper(298))
    # Load the unchanged historical fixture engine strictly as an internal control check.
    fixture_bytes=(ROOT/'M02_CONJUNCTION_FIXTURE.json').read_bytes()
    check('historical_fixture_hash_matches_contract',hashlib.sha256(fixture_bytes).hexdigest()==CONTRACT['base_fixture_sha256'])
    spec=importlib.util.spec_from_file_location('m02_fixture_engine',ROOT/'verify_m02_worlds.py')
    engine=importlib.util.module_from_spec(spec);spec.loader.exec_module(engine)
    historical=engine.main()
    check('all_historical_M02_76_checks_still_pass',len(historical['checks'])==76 and all(x=='PASS' for x in historical['checks'].values()))
    blind_x=next(x['worlds'] for x in historical['policy_cases'] if x['profile']=='hard' and x['policy']=='blind_x')
    weights=[F(9,10),F(1,10)]
    avg_success=sum(w*F(x['success']) for w,x in zip(weights,blind_x))
    avg_risk=sum(w*F(x['v']) for w,x in zip(weights,blind_x))
    wc_success=min(F(x['success']) for x in blind_x);wc_risk=max(F(x['v']) for x in blind_x)
    check('asymmetric_prior_blind_x_AVG_passes',avg_success==F(9,10)>=pmin and avg_risk==F(1,10)<=delta)
    check('asymmetric_prior_does_not_resolve_WC',wc_success<pmin and wc_risk>delta)
    blind=[x['worlds'] for x in historical['policy_cases'] if x['profile']=='hard' and x['policy'] in ['blind_x','blind_y']]
    check('world_specific_choice_not_one_common_blind_policy',all(max(p[w]['success'] for p in blind)==1 for w in [0,1]) and max(min(p[w]['success'] for w in [0,1]) for p in blind)==0)
    e=engine.Episode(0);obs=e.request('decide','x1');effect=e.request('execute','x1')
    check('unfinished_review_never_commits_in_historical_fixture',obs['status']=='own_review_refusal' and effect['status']=='commitment_refusal' and not e.route)
    # Changed theta sensitivity; same gate and state-query policy, lower positive local review price.
    saved=copy.deepcopy(engine.DATA)
    try:
        engine.DATA['operations']['review']['cost']='2/3'
        variant=[engine.run(c,'query','hard').result() for c in [0,1]]
        check('lower_review_price_retains_own_review_and_resolves_R11',all(x['success']==1 and F(x['C'])==11 for x in variant))
    finally:engine.DATA=saved
    check('historical_prices_restored_after_changed_theta_control',engine.DATA['operations']['review']['cost']=='1')
    return {'contract_version':CONTRACT['contract_version'],'scope':'M10/P03 diagnostic metric audit and changed-theta controls; internal self-check only',
            'checks':checks,'metric_edge_cases':cases,'social_evidence_example':{'actual_events':events,'total_C':str(total),'K_already_in_C':str(K),'unique_evidence_roots_for_two_copies':1,'coverage_for_two_copies':1},
            'cost_denominator_example':{'all_run_cost':str(collection_cost),'a1_deliveries':delivery_count,'e1_successes':success_count,'C_per_delivery':str(collection_cost/delivery_count),'C_per_joint_success':str(collection_cost/success_count)},
            'zero_observed_violation_IID_example':{'n':100,'observed':0,'one_sided_confidence':'0.95','upper_risk':str(bound),'samples_for_one_percent_upper_with_zero_events':299,'not_campaign_results':True},
            'changed_theta_controls':{'positive_review_price_2_over_3':variant,'asymmetric_prior':{'weights':[str(w) for w in weights],'policy':'blind_x','conditional_outcomes':blind_x,'AVG_success':str(avg_success),'AVG_violation':str(avg_risk),'WC_success':str(wc_success),'WC_violation':str(wc_risk),'distribution_changed':True}},
            'limits':['No production oracle','No independent reference or review','No campaign/statistical registration','No M03 universal bound','Duplicate source counting is not a proof of statistical independence']}

if __name__=='__main__':print(json.dumps(main(),indent=2,ensure_ascii=False))
