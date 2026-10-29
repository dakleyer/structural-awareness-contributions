"""Source-anchored regression acceptance, with adversarial controls and third-party use."""
from __future__ import annotations
import json
from pathlib import Path
import unittest
from copy import deepcopy
from fractions import Fraction

from engine import (
    number, compare_vector, state_checks, transition_checks, reachable, run_case, run_manifest,
)

HERE=Path(__file__).resolve().parent
MANIFEST=json.loads((HERE/'cases.json').read_text(encoding='utf-8'))
CASES={s['case_id']:s for s in MANIFEST['cases']}
OUTPUT=run_manifest(MANIFEST)
REPORTS={r['case_id']:r for r in OUTPUT['cases']}

def comparison(case,from_,to,stage=None):
    c=next(c for c in REPORTS[case]['comparisons'] if c['from']==from_ and c['to']==to)
    if stage is None:return c
    return next(s for s in c['stages'] if s['stage']==stage)

class AuthorExamplesAcceptance(unittest.TestCase):
    def test_exhaustive_stable_example_ids_and_provenance(self):
        ids=('EX-BAN-01','EX-BAN-02','EX-BAN-03','EX-BAN-04',
             'EX-ROBIN-01','EX-MIN-01','EX-APPLE-01','EX-LINEAR-01','EX-CREDIT-01',
             'EX-SOLIDAR-01','EX-ORANGE-01','EX-HUMAN-01','EX-SUPER-01','EX-BUSINESS-01')
        self.assertEqual(len(CASES),14)
        self.assertEqual(set(CASES),set(ids))
        self.assertEqual(OUTPUT['case_count'],14)
        self.assertTrue(all(c['source_anchor'].startswith('https://github.com/') for c in OUTPUT['cases']))
        self.assertTrue(all(c['evidence_tier']=='AUTHOR_HYPOTHETICAL_TOY' for c in OUTPUT['cases']))

    def test_banana_extra_transport_genuine_tradeoff(self):
        c=CASES['EX-BAN-02']
        self.assertEqual(comparison(c['case_id'],'held','sent','K_declared')['comparison']['oriented_deltas'],
                         {'E_transport':'-3','R_food':'1'})
        self.assertEqual(comparison(c['case_id'],'held','sent','K_declared')['comparison']['status'],'TRADEOFF')
        self.assertIn('sent',REPORTS[c['case_id']]['reachability']['unilateral_only']['reachable_states'])

    def test_banana_origin_activates_coordination_without_creating_it(self):
        c=REPORTS['EX-BAN-01']
        s=comparison('EX-BAN-01','imported_discard','local_use')
        self.assertEqual([x['comparison']['status'] for x in s['stages']],
                         ['DOMINATES_ON_DECLARED_AXES','TRADEOFF'])
        self.assertEqual(s['stages'][1]['newly_material_axes'],['C_effort'])
        self.assertEqual(c['transitions']['organize_local_route']['admissible'],'UNKNOWN')
        self.assertNotIn('local_use',c['reachability']['joint_allowed']['reachable_states'])
        self.assertEqual(CASES['EX-BAN-01']['states']['imported_discard']['metrics']['E_distance'],14000)

    def test_dana_original_credit_is_not_an_institutional_accusation(self):
        c=REPORTS['EX-BAN-03']
        p=comparison('EX-BAN-03','discard','donate_without_recognition')
        self.assertEqual([s['comparison']['status'] for s in p['stages']],
                         ['DOMINATES_ON_DECLARED_AXES','DOMINATES_ON_DECLARED_AXES','TRADEOFF'])
        self.assertEqual(p['individual_payoffs']['status'],'DOMINATES_ON_DECLARED_AXES')
        self.assertEqual(c['transitions']['proposed_donation_declined']['admissible'],'FAIL')
        self.assertEqual(c['transitions']['alternate_credit_accepted']['admissible'],'PASS')
        self.assertIn('donate_with_recognition',c['reachability']['unilateral_only']['reachable_states'])
        self.assertEqual(p['stages'][2]['newly_material_axes'],['V_donor'])

    def test_two_bananas_original_arithmetic_and_physical_conservation(self):
        c=REPORTS['EX-BAN-04']
        self.assertTrue(all(v['status']=='PASS' for v in c['state_validity'].values()))
        self.assertEqual(c['welfare']['S1']['B'],5)
        self.assertEqual(c['welfare']['S1']['F'],7)
        self.assertEqual(c['welfare']['S1']['W'],-2)
        self.assertEqual(c['welfare']['S1']['status'],'STIPULATED_TOY_NOT_HUMAN_MEASUREMENT')
        self.assertEqual(c['welfare']['S2']['F'],None)
        self.assertEqual(c['transitions']['redistribute_one']['admissible'],'UNKNOWN')
        self.assertEqual(comparison('EX-BAN-04','S1','S2')['stages'][0]['comparison']['status'],
                         'DOMINATES_ON_DECLARED_AXES')
        bad=deepcopy(CASES['EX-BAN-04'])
        bad['states']['S1']['facts']['waste']=2
        self.assertEqual(run_case(bad)['state_validity']['S1']['status'],'FAIL')

    def test_robinson_1_999_source_counts_and_relative_refusal(self):
        s=CASES['EX-ROBIN-01']['states']['unequal']['facts']
        self.assertEqual((s['v_coco'],s['r_coco'],s['v_fish'],s['r_fish']),(1,999,1,999))
        self.assertEqual([x['comparison']['status'] for x in comparison('EX-ROBIN-01','lost','unequal')['stages']],
                         ['DOMINATES_ON_DECLARED_AXES','TRADEOFF'])
        self.assertEqual(REPORTS['EX-ROBIN-01']['transitions']['proposal_with_relative_rejection']['admissible'],'FAIL')

    def test_ministries_efficiency_does_not_establish_pareto_or_legality(self):
        steps=comparison('EX-MIN-01','fragmented','unified')['stages']
        self.assertEqual(steps[0]['comparison']['status'],'DOMINATES_ON_DECLARED_AXES')
        self.assertEqual(steps[1]['comparison']['status'],'NOT_ESTABLISHED')
        self.assertEqual(REPORTS['EX-MIN-01']['transitions']['consolidate']['admissible'],'UNKNOWN')

    def test_apples_nonmonotone_but_pareto_finals_possible(self):
        c=REPORTS['EX-APPLE-01']
        self.assertEqual(c['transitions']['buy_4']['institutional'],'FAIL')
        self.assertEqual(c['reachability']['unilateral_only']['reachable_states'],['q3'])
        self.assertIn('q8',c['reachability']['joint_allowed']['reachable_states'])
        self.assertEqual(comparison('EX-APPLE-01','q3','q8')['individual_payoffs']['status'],
                         'DOMINATES_ON_DECLARED_AXES')

    def test_binary_joint_without_unilateral_intermediate(self):
        c=REPORTS['EX-LINEAR-01']
        self.assertEqual(c['state_validity']['10']['status'],'FAIL')
        self.assertEqual(c['state_validity']['01']['status'],'FAIL')
        self.assertEqual(c['state_validity']['11']['status'],'PASS')
        self.assertEqual(c['reachability']['unilateral_only']['reachable_states'],['00'])
        self.assertEqual(c['reachability']['joint_allowed']['reachable_states'],['00','11'])

    def test_credit_7_plus_4_is_physically_invalid_not_just_unpopular(self):
        c=REPORTS['EX-CREDIT-01']
        self.assertEqual(c['state_validity']['shares_7_4']['status'],'FAIL')
        self.assertEqual(c['transitions']['raise_B_to_four']['technical'],'FAIL')
        self.assertEqual(comparison('EX-CREDIT-01','shares_7_3','shares_7_4')['target_state_physically_admissible_in_declared_model'],'FAIL')

    def test_solidarity_requires_actual_consent_and_no_universal_welfare(self):
        c=REPORTS['EX-SOLIDAR-01']
        self.assertEqual(c['transitions']['no_consent']['admissible'],'UNKNOWN')
        self.assertEqual(c['transitions']['freely_chosen']['admissible'],'PASS')
        self.assertEqual(comparison('EX-SOLIDAR-01','retain','without_choice')['stages'][0]['comparison']['status'],'TRADEOFF')

    def test_oranges_and_student_are_not_numeric_discoveries(self):
        for name in ('EX-ORANGE-01','EX-HUMAN-01'):
            with self.subTest(name=name):
                c=REPORTS[name]
                self.assertEqual(c['comparisons'][0]['stages'][0]['comparison']['status'],'NOT_ESTABLISHED')
                self.assertEqual(next(iter(c['transitions'].values()))['admissible'],'UNKNOWN')

    def test_X_minus_200_does_not_invent_repair_authority(self):
        c=REPORTS['EX-SUPER-01']
        self.assertEqual(CASES['EX-SUPER-01']['states']['limited']['facts']['delivery'],800)
        self.assertEqual(c['transitions']['repair_unknown_bottleneck']['admissible'],'UNKNOWN')

    def test_marketing_offer_accounting_70_to_55_and_authority(self):
        c=REPORTS['EX-BUSINESS-01']
        self.assertEqual(CASES['EX-BUSINESS-01']['states']['raw_offer']['metrics']['E_joint_gain'],70)
        self.assertEqual(CASES['EX-BUSINESS-01']['states']['compensated_after_cost']['metrics']['E_joint_gain'],55)
        pay=CASES['EX-BUSINESS-01']['states']['compensated_after_cost']['payoffs']
        self.assertEqual(sum(pay.values()),55)
        self.assertEqual(c['transitions']['raw_offer_without_compensation']['admissible'],'FAIL')
        self.assertEqual(c['transitions']['compensated_but_approval_unverified']['admissible'],'UNKNOWN')
        self.assertEqual(comparison('EX-BUSINESS-01','status_quo','raw_offer')['stages'][1]['comparison']['status'],'TRADEOFF')
        self.assertEqual(comparison('EX-BUSINESS-01','status_quo','compensated_after_cost')['individual_payoffs']['status'],
                         'DOMINATES_ON_DECLARED_AXES')


class ReusableEngineAdversarialTests(unittest.TestCase):
    def test_integer_fraction_and_decimal_conserve_exactness(self):
        self.assertEqual(number('0.1')+number('0.2'),Fraction(3,10))
        self.assertEqual(number('1/3')*3,1)
        for invalid in (True,False,None,float('nan'),float('inf'),'NaN','',{},object()):
            with self.subTest(invalid=str(invalid)),self.assertRaises(ValueError):
                number(invalid)

    def test_external_dimensions_without_source_case_branches(self):
        fixture={'case_id':'THIRD-PARTY-WATER','source_anchor':'external:water-meter',
          'evidence_tier':'AUTHOR_HYPOTHETICAL_TOY',
          'dimensions':{'litres':{'direction':'min','unit':'litres'},'service':{'direction':'max','unit':'units'}},
          'states':{'old':{'metrics':{'litres':10,'service':2}},'new':{'metrics':{'litres':8,'service':2}}},
          'initial':'old','resource_budgets':{},'state_invariants':[],
          'transitions':[{'id':'save','from':'old','to':'new','mode':'unilateral','guards':[]}],
          'stages':[{'id':'eco-service','axes':['litres','service']}],
          'comparisons':[{'from':'old','to':'new'}]}
        result=run_case(fixture)
        self.assertEqual(result['comparisons'][0]['stages'][0]['comparison']['status'],
                         'DOMINATES_ON_DECLARED_AXES')
        self.assertIn('new',result['reachability']['unilateral_only']['reachable_states'])

    def test_budget_is_cumulative_not_merely_checked_on_each_edge(self):
        scenario=deepcopy(CASES['EX-BAN-02'])
        scenario['states']['second']=deepcopy(scenario['states']['sent'])
        scenario['transitions'].append({'id':'second_delivery','from':'sent','to':'second',
                                         'mode':'unilateral','guards':[], 'consumes':{'logistic_slot':1}})
        results=run_case(scenario)
        self.assertEqual(results['transitions']['second_delivery']['technical'],'PASS')
        self.assertNotIn('second',results['reachability']['unilateral_only']['reachable_states'])

    def test_requirements_not_automatically_inferred_from_dimensions(self):
        s=deepcopy(CASES['EX-BAN-01'])
        s['dimensions']['new_axis']={'direction':'max','unit':'count'}
        s['stages'].append({'id':'K4','axes':['E_distance','R_food','C_effort','new_axis']})
        report=run_case(s)
        self.assertEqual(report['comparisons'][0]['stages'][-1]['comparison']['status'],'NOT_ESTABLISHED')
        self.assertEqual(report['transitions']['organize_local_route']['admissible'],'UNKNOWN')

    def test_fail_closed_mislabelled_evidence_and_permission(self):
        s=deepcopy(CASES['EX-BAN-02'])
        s['evidence_tier']='FIELD_VALIDATED'
        with self.assertRaisesRegex(ValueError,'synthetic evidence'):
            run_case(s)
        s=deepcopy(CASES['EX-BAN-02'])
        s['transitions'][0]['guards'][0]['status']='ASSUMED_YES'
        with self.assertRaisesRegex(ValueError,'unknown guard'):
            run_case(s)
        s=deepcopy(CASES['EX-BAN-02'])
        s['transitions'][0]['guards'][0]['source_of_status']=''
        with self.assertRaisesRegex(ValueError,'named source'):
            run_case(s)

    def test_negative_and_unbounded_resource_budget_fail(self):
        s=deepcopy(CASES['EX-BAN-02'])
        s['resource_budgets']['logistic_slot']=-1
        with self.assertRaisesRegex(ValueError,'negative budget'):
            run_case(s)
        s=deepcopy(CASES['EX-BAN-02'])
        s['transitions'][0]['consumes']['logistic_slot']=-1
        with self.assertRaisesRegex(ValueError,'negative resource'):
            run_case(s)

    def test_unknown_stays_unknown_instead_of_zero(self):
        out=compare_vector({'x':None},{'x':0},{'x':'max'},['x'])
        self.assertEqual(out['status'],'NOT_ESTABLISHED')
        self.assertIsNone(out['oriented_deltas']['x'])

    def test_non_fungible_rights_no_override_from_more_material_value(self):
        s=deepcopy(CASES['EX-BAN-03'])
        s['states']['donate_without_recognition']['metrics']['R_help']=100000
        c=run_case(s)
        self.assertEqual(c['transitions']['proposed_donation_declined']['admissible'],'FAIL')

    def test_per_case_not_global_utility_and_duplicate_rejection(self):
        output=run_manifest(MANIFEST)
        self.assertNotIn('utility_total',output)
        broken=deepcopy(MANIFEST)
        broken['cases'].append(deepcopy(broken['cases'][0]))
        with self.assertRaisesRegex(ValueError,'duplicate case'):
            run_manifest(broken)

if __name__ == '__main__':
    unittest.main()
