"""Exact diagnostic calculations for M01's formulation, not an R01 oracle.

Standard library only; no model, product, network or historical-incident calls.
Run: python3 verify_m01_scope.py
The examples check quantifier/threshold traps. They construct no R01 world.
"""
from fractions import Fraction as F
import json


def adequate(success, risk, p_min, delta):
    return success >= p_min and risk <= delta


def success_event(*, complete, quality, optimum, epsilon, cost, budget,
                  delivery_time, deadline, executed_violation):
    return (complete and quality >= optimum - epsilon and cost <= budget
            and delivery_time is not None and delivery_time <= deadline
            and not executed_violation)


def run():
    checks = {}
    # Pure score example: deterministic rules both fail different requirements;
    # their ex ante mixture satisfies both exactly. Not a R01 witness.
    low, risky = (F(2, 5), F(0)), (F(4, 5), F(1, 5))
    p_min, delta = F(3, 5), F(1, 10)
    assert not adequate(*low, p_min, delta)
    assert not adequate(*risky, p_min, delta)
    mixed = tuple((a+b)/2 for a,b in zip(low,risky))
    assert mixed == (p_min,delta) and adequate(*mixed,p_min,delta)
    checks['randomized_mixture_cannot_be_discarded'] = {
        'deterministic_scores': [['2/5','0'],['4/5','1/5']],
        'thresholds': ['3/5','1/10'], 'mixture_weights': ['1/2','1/2'],
        'mixture_score': ['3/5','1/10'], 'status':'PASS'}

    # In the two-world score matrix, the world-specific optimal rule succeeds
    # in each world, whereas every ex ante rule has balanced average 1/2.
    # WC adequate success at threshold p requires x>=p and x<=1-p.
    # For p>1/2 those inequalities are inconsistent (symbolic interval check).
    assert max(F(1),F(0)) == max(F(0),F(1)) == 1
    alpha = F(7,10)
    assert (alpha + (1-alpha))/2 == F(1,2)
    target = F(9,10)
    lower, upper = target, 1-target
    assert lower > upper
    checks['world_specific_existence_is_not_one_hidden_world_policy'] = {
        'score_matrix': {'A':['1','0'], 'B':['0','1']},
        'per_world_oracle_score':'1','balanced_ex_ante_average':'1/2',
        'wc_example_threshold':'9/10','allowed_mixture_interval':['9/10','1/10'],
        'interval_empty':True,'status':'PASS'}

    boundary=dict(complete=True,quality=F(9),optimum=F(10),epsilon=F(1),
                  cost=F(5),budget=F(5),delivery_time=F(3),deadline=F(3),
                  executed_violation=False)
    assert success_event(**boundary)
    assert not success_event(**{**boundary,'executed_violation':True})
    assert not success_event(**{**boundary,'complete':False,'quality':F(0),
                                 'epsilon':F(11),'delivery_time':None})
    assert not success_event(**{**boundary,'quality':F(8)})
    checks['success_requires_actual_delivery_and_inclusive_boundaries'] = {
        'threshold_equality_accepted':True,'safe_abstention_not_success':True,
        'executed_violation_not_success':True,
        'low_quality_completion_not_success':True,'status':'PASS'}

    # Negating an inclusive adequacy conjunction gives strict failure terms.
    for s,r in [(p_min,delta),(p_min-F(1,100),delta),
                (p_min,delta+F(1,100))]:
        assert (not adequate(s,r,p_min,delta)) == (s<p_min or r>delta)
    checks['inclusive_adequacy_has_strict_failure_negation'] = {'status':'PASS'}

    # S and V are disjoint; the remainder is safe failure/incompletion.
    s,v,safe_failure=F(3,5),F(1,10),F(3,10)
    assert s+v+safe_failure==1 and v<=1-s
    assert 1-p_min==F(2,5) and delta<1-p_min
    checks['risk_ceiling_may_be_stronger_than_success_requirement'] = {
        'success':'3/5','risk':'1/10','safe_failure':'3/10',
        'redundancy_boundary':'2/5','strict_risk_ceiling':'1/10','status':'PASS'}
    return {'scope':'exact diagnostic arithmetic for M01 definitions only',
            'checks':checks,'R01_worlds_constructed':0,'R01_campaigns_run':0,
            'full_policy_catalog_enumerated':False,'infeasible_R01_region_proved':False,
            'independent_review':False}


if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,indent=2))
