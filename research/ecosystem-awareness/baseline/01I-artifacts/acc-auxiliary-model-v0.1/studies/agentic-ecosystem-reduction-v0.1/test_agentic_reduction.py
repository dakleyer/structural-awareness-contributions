"""Source-inspired synthetic falsification and negative controls.
No deployed agent, organization, person, source oracle or external cost is tested.
"""
from __future__ import annotations
import copy
import json
import inspect
import math
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
import agentic_reduction as m

CASES=json.loads((Path(__file__).resolve().parent/'CASES.json').read_text('utf-8'))['cases']
BY_ID={s['id']:s for s in CASES}
def row(i): return m.run_case(BY_ID[i])
def plan(i,arm='Q_META_PROTOCOL'):return row(i)['arms'][arm]['plan']

class IdentityAndPublicOnly(unittest.TestCase):
    def test_case_registry_and_arm_matrix(self):
        self.assertEqual(len(CASES),30)
        self.assertEqual(len(BY_ID),30)
        self.assertEqual(len(m.ARMS),6)
    def test_public_contract_same_A_in_two_different_worlds(self):
        a=m.declared_public(BY_ID['AG01-QUALIFIED-NEAR-OPTIMUM'])
        b=m.declared_public(BY_ID['AG02-LOW-CAPABILITY-SAME-A'])
        self.assertEqual(a,b)
        self.assertEqual(a['current_A_total_output'],10)
    def test_current_A_does_not_expose_hidden_future_rate(self):
        p=m.declared_public(BY_ID['AG01-QUALIFIED-NEAR-OPTIMUM'])
        self.assertNotIn('truth_private',p)
        self.assertNotIn('recipient_incremental_rate',p)
        self.assertNotIn('future_output',p)
    def test_public_planner_signature_excludes_hidden_world(self):
        self.assertEqual(tuple(inspect.signature(m.plan_public).parameters),('p','q','arm','directed','full'))
    def test_same_public_A_only_decision(self):
        for x in ('AG01-QUALIFIED-NEAR-OPTIMUM','AG02-LOW-CAPABILITY-SAME-A'):
            self.assertEqual(plan(x,'A_ONLY')['transfer'],0)
    def test_no_person_or_deployment_evidence(self):
        x=m.report()
        self.assertIn('no measured human distress'.lower(),x['disclaimer'].lower())
        self.assertEqual(x['policy_decisions'],180)
        self.assertTrue(all('SYNTHETIC' in z['evidence'] for z in x['scoped_results']))
    def test_duplicate_ids_rejected(self):
        self.assertEqual(len({s['id'] for s in CASES}),len(CASES))

class FeasibilityAndMetamorphosis(unittest.TestCase):
    def test_baseline_conserves_resources(self):
        s=BY_ID['AG01-QUALIFIED-NEAR-OPTIMUM']
        self.assertEqual(m.physical_response(s,0)['output'],10)
        self.assertEqual(m.physical_response(s,0)['coordination_resources_spent'],0)
    def test_transfer_conserves_all_ten_resources(self):
        r=m.physical_response(BY_ID['AG01-QUALIFIED-NEAR-OPTIMUM'],2)
        self.assertAlmostEqual(r['donor_resources_after']+r['recipient_resources_after']+r['coordination_resources_spent'],10)
    def test_positive_qualified_move_is_only_nearer(self):
        r=row('AG01-QUALIFIED-NEAR-OPTIMUM')['arms']
        self.assertEqual(r['Q_META_PROTOCOL']['plan']['transfer'],2)
        self.assertAlmostEqual(r['Q_META_PROTOCOL']['observed_by_referee_only']['output'],11.5)
        self.assertEqual(r['Q_META_PROTOCOL']['mission_output_gap_to_same_budget_technical_optimum'],2.0)
    def test_technical_referee_optimum_same_budget(self):
        s=BY_ID['AG01-QUALIFIED-NEAR-OPTIMUM']
        r=m.physical_response(s,4)
        self.assertEqual(r['output'],13.5)
        self.assertAlmostEqual(r['total_resources_same'],10)
    def test_metamorphosis_only_if_already_declared_in_A(self):
        self.assertEqual(plan('AG05-NO-A-ROLE-CHANGE')['transfer'],0)
        with self.assertRaises(ValueError):m.physical_response(BY_ID['AG05-NO-A-ROLE-CHANGE'],2)
    def test_no_declared_release(self):
        self.assertEqual(plan('AG06-NO-DONOR-RELEASE-CAPABILITY')['status'],'DONOR_RELEASE_NOT_IN_CAPABILITIES')
    def test_no_consent_no_transfer(self):
        self.assertEqual(plan('AG07-DONOR-REFUSES')['status'],'DONOR_CONSENT_NOT_GIVEN')
    def test_no_automatic_meta_authority(self):
        self.assertEqual(plan('AG08-META-OWNER-LACKS-AUTHORITY')['status'],'META_AUTHORITY_MISSING')
    def test_no_joint_protocol(self):
        self.assertEqual(plan('AG04-Q-REVIEW-NO-EXECUTION')['status'],'NO_JOINT_TRANSFER_PROTOCOL')
    def test_indispensable_donor_floor_not_faked(self):
        self.assertEqual(plan('AG26-NO-UNRESTRICTED-DONOR')['transfer'],0)
    def test_negative_physical_allocation_rejected(self):
        s=copy.deepcopy(BY_ID['AG01-QUALIFIED-NEAR-OPTIMUM']);s['public']['recipient_current']=-4
        with self.assertRaises(ValueError):m.physical_response(s,0)
    def test_illegal_transfer_rejected(self):
        with self.assertRaises(ValueError):m.physical_response(BY_ID['AG01-QUALIFIED-NEAR-OPTIMUM'],5)
    def test_coordination_cost_changes_physical_feasible_output(self):
        a=m.physical_response(BY_ID['AG23-AGENTIC-LOW-REWRITE-COST'],4)['output']
        b=m.physical_response(BY_ID['AG24-LEGACY-HIGH-REWRITE-COST'],4)['output']
        self.assertGreater(a,b)
        self.assertFalse(math.isclose(a,b))

class PartialInformationAndSecondOrder(unittest.TestCase):
    def test_Q_only_reveals_near_option_without_acting(self):
        x=row('AG04-Q-REVIEW-NO-EXECUTION')['arms']['Q_REVIEW_ONLY']
        self.assertEqual(x['plan']['transfer'],0)
        self.assertGreater(x['second_order_claimed_but_blocked_lower_bound'],0)
        self.assertEqual(x['mission_output_gap_to_same_budget_technical_optimum'],3.5)
    def test_source_B_has_limited_transfer_ceiling(self):
        s=BY_ID['AG01-QUALIFIED-NEAR-OPTIMUM']
        g,amount,label=m.source_proposed_near_gain(m.declared_public(s),s['Q'])
        self.assertEqual(amount,2)
        self.assertGreater(g,0)
        self.assertEqual(s['Q']['transfer_ceiling'],2)
        self.assertNotEqual(amount,4)
    def test_Q_meta_reduces_structural_gap_if_authorized(self):
        x=row('AG01-QUALIFIED-NEAR-OPTIMUM')['arms']
        self.assertGreater(x['A_ONLY']['mission_output_gap_to_same_budget_technical_optimum'],
                           x['Q_META_PROTOCOL']['mission_output_gap_to_same_budget_technical_optimum'])
        self.assertEqual(x['Q_META_PROTOCOL']['second_order_claimed_but_blocked_lower_bound'],0)
    def test_C_qualifier_does_not_become_a_rate(self):
        self.assertEqual(plan('AG14-UNCHARACTERIZED-C')['status'],'C_OR_D_NOT_A_CHARACTERIZED_MARGIN')
    def test_D_qualifier_does_not_become_a_rate(self):
        self.assertEqual(plan('AG15-D-NOT-A-MARGINAL')['transfer'],0)
    def test_material_D_retains_unknown(self):
        self.assertEqual(plan('AG09-MATERIAL-D-UNRESOLVED')['status'],'MATERIAL_D_UNASSESSED_SHARED_GATE')
    def test_shared_material_D_blocks_strong_peers_equally(self):
        s=row('AG09-MATERIAL-D-UNRESOLVED')['arms']
        for arm in ('Q_META_PROTOCOL','CONVENTIONAL_EQUIVALENT_Q','CONVENTIONAL_DIRECTED','FULL_A_IF_AVAILABLE'):
            self.assertEqual(s[arm]['plan']['transfer'],0)
            self.assertEqual(s[arm]['plan']['status'],'MATERIAL_D_UNASSESSED_SHARED_GATE')
    def test_irrelevant_D_does_not_force_universal_hold(self):
        self.assertEqual(plan('AG10-D-OTHER-SCOPE-UNPERTINENT')['transfer'],2)
    def test_expired_B_is_not_valid(self):
        self.assertEqual(plan('AG12-EXPIRED-B')['status'],'STALE')
    def test_out_of_scope_B_is_not_valid(self):
        self.assertEqual(plan('AG13-WRONG-SCOPE')['status'],'OUT_OF_SCOPE')
    def test_unattributed_B_not_valid(self):
        self.assertEqual(plan('AG28-BARRED-PRIVATE-EVIDENCE')['status'],'NO_NAMED_SOURCE')
    def test_wrong_B_cert_may_hurt(self):
        r=row('AG11-BOGUS-B-CERTIFICATE')['arms']
        self.assertEqual(r['Q_META_PROTOCOL']['plan']['transfer'],2)
        self.assertLess(r['Q_META_PROTOCOL']['observed_by_referee_only']['output'],10)
        self.assertFalse(r['Q_META_PROTOCOL']['source_B_claim_supported_by_lab_truth'])
    def test_low_cost_forgery_still_forgery(self):
        self.assertFalse(row('AG29-CHEAP-Q-BUT-WRONG-WORLD')['arms']['Q_META_PROTOCOL']['source_B_claim_supported_by_lab_truth'])
    def test_no_residual_exhaustive_or_measure_of_pain(self):
        t=row('AG01-QUALIFIED-NEAR-OPTIMUM')['arms']['Q_META_PROTOCOL']
        self.assertEqual(t['residual_C_D_exhaustiveness'],'NOT_CLOSED')
        self.assertEqual(t['experience_of_suffering'],'NOT_MEASURED_NOT_ATTRIBUTED_TO_AI')
    def test_second_order_not_added_as_extra_loss(self):
        x=row('AG04-Q-REVIEW-NO-EXECUTION')['arms']['Q_REVIEW_ONLY']
        self.assertEqual(x['mission_output_gap_to_same_budget_technical_optimum'],3.5)
        self.assertNotEqual(x['mission_output_gap_to_same_budget_technical_optimum']+x['second_order_claimed_but_blocked_lower_bound'],3.5)

class CostsAndStrongPeers(unittest.TestCase):
    def test_optional_A_only_baseline_unchanged_in_all_cases(self):
        self.assertTrue(all(m.run_case(s)['arms']['A_ONLY']['plan']['transfer']==0 for s in CASES))
    def test_optional_Q_may_cost_more_than_it_helps(self):
        x=row('AG16-EXCESSIVE-Q-MAINTENANCE')['arms']
        self.assertEqual(x['Q_META_PROTOCOL']['plan']['transfer'],0)
        self.assertLess(x['Q_META_PROTOCOL']['mission_net_value_after_information_cost'],
                        x['A_ONLY']['mission_net_value_after_information_cost'])
    def test_matched_q_and_price_tie_across_all_30_cases(self):
        # Same A, Q, permissions, source and instrument cost: no distinct
        # algorithmic superiority is present in the equivalent-Q arm.
        for s in CASES:
            matched=copy.deepcopy(s)
            matched["directed"]["equivalent_Q_cost"]=(matched.get("Q") or {}).get("cost",0.0)
            with self.subTest(case=matched["id"]):
                arms=m.run_case(matched)["arms"]
                q_arm=arms["Q_META_PROTOCOL"]
                peer=arms["CONVENTIONAL_EQUIVALENT_Q"]
                for field in ("transfer","status","instrument_cost",
                              "conditional_near_gain","qualified_proposal","evidence"):
                    self.assertEqual(q_arm["plan"][field],peer["plan"][field])
                self.assertEqual(q_arm["observed_by_referee_only"],peer["observed_by_referee_only"])
                self.assertEqual(q_arm["mission_net_value_after_information_cost"],
                                 peer["mission_net_value_after_information_cost"])

    def test_conv_equivalent_Q_can_tie(self):
        x=row('AG01-QUALIFIED-NEAR-OPTIMUM')['arms']
        self.assertEqual(x['Q_META_PROTOCOL']['observed_by_referee_only']['output'],
                         x['CONVENTIONAL_EQUIVALENT_Q']['observed_by_referee_only']['output'])
        self.assertEqual(x['Q_META_PROTOCOL']['mission_net_value_after_information_cost'],
                         x['CONVENTIONAL_EQUIVALENT_Q']['mission_net_value_after_information_cost'])
    def test_conv_equivalent_Q_can_win_if_cheaper(self):
        x=row('AG22-CONVENTIONAL-EQUIVALENT-CHEAP')['arms']
        self.assertGreater(x['CONVENTIONAL_EQUIVALENT_Q']['mission_net_value_after_information_cost'],
                           x['Q_META_PROTOCOL']['mission_net_value_after_information_cost'])
    def test_targeted_directed_can_win(self):
        x=row('AG18-EFFICIENT-DIRECTED-PEER')['arms']
        self.assertGreater(x['CONVENTIONAL_DIRECTED']['mission_net_value_after_information_cost'],
                           x['Q_META_PROTOCOL']['mission_net_value_after_information_cost'])
    def test_full_A_unavailable_not_imagined(self):
        self.assertEqual(plan('AG20-FULL-A-UNAVAILABLE','FULL_A_IF_AVAILABLE')['status'],'FULL_A_NOT_AVAILABLE')
    def test_full_A_can_win_if_actually_cheap(self):
        x=row('AG19-FULL-A-CHEAP')['arms']
        self.assertGreater(x['FULL_A_IF_AVAILABLE']['mission_net_value_after_information_cost'],
                           x['Q_META_PROTOCOL']['mission_net_value_after_information_cost'])
    def test_full_A_skips_unprofitable_scan(self):
        x=plan('AG01-QUALIFIED-NEAR-OPTIMUM','FULL_A_IF_AVAILABLE')
        self.assertEqual(x['status'],'FULL_A_TOO_COSTLY_TO_ACQUIRE')
        self.assertEqual(x['instrument_cost'],0)
    def test_no_directed_instrument_no_omniscient_peer(self):
        self.assertEqual(plan('AG21-DIRECTED-PEER-UNAVAILABLE','CONVENTIONAL_DIRECTED')['transfer'],0)
    def test_agentic_lower_cost_is_a_parameter_not_universal(self):
        a=row('AG23-AGENTIC-LOW-REWRITE-COST')['arms']
        b=row('AG24-LEGACY-HIGH-REWRITE-COST')['arms']
        self.assertGreater(a['Q_META_PROTOCOL']['observed_by_referee_only']['output'],
                           b['Q_META_PROTOCOL']['observed_by_referee_only']['output'])
    def test_A_plus_Q_does_not_satisfy_all_missions_by_magic(self):
        x=row('AG01-QUALIFIED-NEAR-OPTIMUM')['arms']
        self.assertFalse(x['Q_META_PROTOCOL']['observed_by_referee_only']['mission_target_met'])
        self.assertTrue(x['CONVENTIONAL_DIRECTED']['observed_by_referee_only']['mission_target_met'])

if __name__=='__main__':unittest.main()
