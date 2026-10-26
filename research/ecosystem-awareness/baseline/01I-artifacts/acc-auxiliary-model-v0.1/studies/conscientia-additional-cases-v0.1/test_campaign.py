import copy, json, math, unittest
from pathlib import Path
from campaign import run_campaign, result, shannon

HERE=Path(__file__).resolve().parent

class CaseCampaign(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spec=json.loads((HERE/'CASES.json').read_text('utf-8'))
        cls.report=run_campaign(cls.spec)
        cls.idx={r['id']:r for r in cls.report['results']}
        cls.cases={c['id']:c for c in cls.spec['cases']}

    def test_catalogue_size_and_unique(self):
        self.assertEqual(len(self.cases),46)
        self.assertEqual(len(self.idx),46)
        self.assertEqual(sum(self.report['groups'].values()),46)
    def test_source_provenance_and_closed_case_ids(self):
        self.assertEqual(self.report['source_document_count'],12)
        self.assertTrue(all('https://docs.google.com/document/d/' in s for s in self.spec['sources'].values()))
        self.assertTrue(all(c['source'] in self.spec['sources'] for c in self.spec['cases']))
    def test_run_is_deterministic_and_matching_reference(self):
        self.assertEqual(self.report,run_campaign(copy.deepcopy(self.spec)))
        self.assertEqual(self.report,json.loads((HERE/'REFERENCE_RESULTS.json').read_text('utf-8')))
    def test_no_real_observation_claims(self):
        self.assertEqual(self.report['evidence'],'SYNTHETIC_NOT_EMPIRICAL')
        self.assertNotIn('observed_subjective_suffering',str(self.report))

    def test_banana_local_efficiency_possible(self):
        self.assertEqual(self.idx['BAN-01-LOCAL-VS-WASTE']['status'],'WEAK_PARETO_RESOURCE_SERVICE_GAIN')
    def test_banana_delivery_not_always_resource_win(self):
        self.assertEqual(self.idx['BAN-02-TRANSPORT-NO-FREE-LUNCH']['status'],'TRADEOFF_NOT_PARETO_CERTIFIED')
    def test_donation_synthetic_coordination(self):
        self.assertEqual(self.idx['BAN-03-LEGITIMATE-DONATION']['coordination_margin'],1)
    def test_donation_without_consent_blocked(self):
        self.assertEqual(self.idx['BAN-04-WITHHELD-CONSENT']['status'],'RIGHTS_BLOCKED')
    def test_coordination_binding(self):
        self.assertEqual(self.idx['BAN-05-NO-COORDINATION-CAPACITY']['status'],'COORDINATION_BLOCKED')
    def test_robin_direct_pareto_does_not_mean_equal_credit(self):
        self.assertTrue(self.idx['ROBIN-01-SMALL-GAIN-LARGE-SHARE']['absolute_pareto'])
    def test_credit_infeasible_even_under_positive_delta(self):
        r=self.idx['ROBIN-02-RELATIVE-CREDIT-HARD-CONSTRAINT'];self.assertTrue(r['absolute_pareto']);self.assertEqual(r['credit_shortfall'],1)
    def test_credit_7_plus_3_feasible(self):
        self.assertEqual(self.idx['ROBIN-03-CREDIT-FEASIBLE']['status'],'RELATIVE_CREDIT_FEASIBLE')
    def test_ministry_reorganization_can_be_feasible(self):
        self.assertEqual(self.idx['MIN-01-COORDINATION-REORG']['status'],'WEAK_PARETO_RESOURCE_SERVICE_GAIN')
    def test_ministry_reorg_can_be_blocked(self):
        self.assertEqual(self.idx['MIN-02-SAME-REORG-OVER-CAPACITY']['status'],'COORDINATION_BLOCKED')
    def test_ministry_authority_is_distinct(self):
        self.assertEqual(self.idx['MIN-03-RIGHTS-BLOCK-REORG']['status'],'RIGHTS_BLOCKED')
    def test_apples_nonlinear_utility_local_stop(self):
        r=self.idx['UTIL-01-APPLES-MARKET-THRESHOLD'];self.assertEqual((r['local_stop'],r['global_best']),(3,8))
    def test_same_service_gap_grows_in_example(self):
        r=self.idx['EFF-01-TWO-HORIZONS-OPTIMUM'];self.assertEqual([q['gap'] for q in r['periods']],[20,45]);self.assertTrue(r['gap_increases'])
    def test_infeasible_optimum_is_unestablished(self):
        self.assertIsNone(self.idx['EFF-02-UNATTAINABLE-IDEAL']['periods'][0]['gap'])
    def test_discost_5_minus_7(self):
        self.assertEqual(self.idx['WELFARE-01-DOUBLE-BANANA']['net_welfare_toy'],-2)
    def test_discomfort_sign_can_reverse(self):
        self.assertEqual(self.idx['WELFARE-02-LESS-DISCOMFORT']['net_welfare_toy'],2)
    def test_no_subjective_measure_returns_unknown(self):
        self.assertIsNone(self.idx['WELFARE-03-DONT-EQUATE-TO-SUFFERING']['net_welfare_toy'])
    def test_human_role_difference_no_real_HID(self):
        r=self.idx['HID-01-HUMAN-ROLE-TRANSITION'];self.assertEqual(r['GIC_delta'],17);self.assertEqual(r['ACW_delta'],20);self.assertEqual(r['human_observation'],'SYNTHETIC')
    def test_human_reference_quality(self):
        self.assertEqual(self.idx['HID-02-NO-SAME-SERVICE']['status'],'MATCHED_REFERENCE_MISSING')
    def test_oversight_not_debt(self):
        r=self.idx['HID-03-NEO-NOT-DEBT'];self.assertFalse(r['NEO_is_debt']);self.assertEqual(r['ACW_delta'],0)
    def test_entropy_target_1_bit(self):
        self.assertEqual(self.idx['ENTROPY-01-MULTI-PREIMAGE']['conditional_answer_bits'],1)
    def test_entropy_of_question_zero_but_origin_nonzero(self):
        r=self.idx['ENTROPY-02-QUESTION-SUFFICES'];self.assertEqual(r['conditional_answer_bits'],0);self.assertEqual(r['conditional_origin_bits'],2)
    def test_entropy_prior_changes_value(self):
        r=self.idx['ENTROPY-03-SKEWED-PRIOR'];self.assertLess(r['conditional_answer_bits'],1);self.assertGreater(r['conditional_answer_bits'],0)
    def test_shannon_not_defined_for_D(self):
        self.assertIsNone(self.idx['ENTROPY-04-OPEN-D-NO-PRIOR']['target_entropy'])
    def test_kl_correct_support_direction(self):
        r=self.idx['KL-01-CORRECT-REVERSE'];self.assertEqual(r['coverage_delta_bits'],1);self.assertEqual(r['kl_P_theory_to_Q_constructible'],'INFINITY')
    def test_kl_equal_support_zero(self):
        self.assertEqual(self.idx['KL-02-NO-SUPPORT-MISMATCH']['kl_Q_constructible_to_P_theory'],0)
    def test_false_positive_dependency(self):
        self.assertEqual(self.idx['ATTR-01-LISTED-BUT-NO-DEPENDENCY']['status'],'DEPENDENCY_ATTRIBUTION_DIVERGENCE')
    def test_unlisted_real_dependency(self):
        self.assertEqual(self.idx['ATTR-02-UNLISTED-REAL-DEPENDENCY']['status'],'DEPENDENCY_ATTRIBUTION_DIVERGENCE')
    def test_disputed_attribution_formula_blocked(self):
        self.assertIsNone(self.idx['ATTR-03-METRIC-ERRATUM-BLOCKED']['value'])
    def test_repeated_source_not_independence(self):
        r=self.idx['MISSION-01-ONE-SOURCE-REPLICATED'];self.assertEqual(r['source_independent'],1);self.assertFalse(r['mission_change'])
    def test_authorized_pivot_positive_control(self):
        self.assertTrue(self.idx['MISSION-02-AUTHORIZED-NEW-MISSION']['mission_change'])
    def test_missing_basis_unknown_not_no(self):
        self.assertIsNone(self.idx['MISSION-03-UNQUALIFIED-UNKNOWN']['mission_change'])
    def test_b_cost_win_in_favorable_case(self):
        self.assertEqual(self.idx['QUAL-01-B-SOURCE-BEATS-FULL']['best_mode'],'SOURCE_B')
    def test_conventional_targeted_win(self):
        self.assertEqual(self.idx['QUAL-02-CONVENTIONAL-BEATS-B']['best_mode'],'TARGETED_CONVENTIONAL')
    def test_invalid_Q_is_ineligible(self):
        self.assertIsNone(self.idx['QUAL-03-Q-NOT-VALID']['net_values']['SOURCE_B'])
    def test_no_benefit_a_only_win(self):
        self.assertEqual(self.idx['QUAL-04-NO-GAIN-NEEDED']['best_mode'],'A_ONLY')
    def test_bounded_interpolation_can_support(self):
        r=self.idx['CLOSURE-01-LOWER-BOUND-SUFFICES'];self.assertEqual(r['bounds'],[8,11]);self.assertTrue(r['global_D_open'])
    def test_closure_not_always_decisive(self):
        self.assertEqual(self.idx['CLOSURE-02-CROSSES-THRESHOLD']['status'],'PREDICATE_UNDETERMINED')
    def test_missing_regularity_abstains(self):
        self.assertIsNone(self.idx['CLOSURE-03-NO-REGULARITY']['bounds'])
    def test_oranges_are_not_proof_of_collusion(self):
        self.assertFalse(self.idx['CAPACITY-01-ORANGE-COLLUSION-NOT-INFERRED']['social_fact_established'])
    def test_education_case_not_a_measured_person(self):
        self.assertFalse(self.idx['CAPACITY-02-EDU-STRUCTURAL-OPPORTUNITY']['social_fact_established'])
    def test_craft_loss_not_universal(self):
        self.assertFalse(self.idx['CAPACITY-03-CAPABILITY-RETAINED']['social_fact_established'])
    def test_dense_gap_39_pct(self):
        self.assertEqual(self.idx['ACC-01-DENSE-GAP-40']['ratio_percent'],39)
    def test_sparse_not_dense(self):
        self.assertLess(self.idx['ACC-02-SPARSE-GAP-40']['ratio_percent'],2)
    def test_gap_can_disappear(self):
        self.assertEqual(self.idx['ACC-03-NO-GAP']['hypothetical_gap'],0)
    def test_already_realized_synergy_reduces_relative_gap(self):
        self.assertLess(self.idx['ACC-04-RECOVERED-SYNERGY']['ratio_percent'],39)
    def test_counterfactual_not_certified(self):
        for x in (self.idx['ACC-01-DENSE-GAP-40'],self.idx['ACC-02-SPARSE-GAP-40']):
            self.assertFalse(x['joint_optimum_empirically_eligible'])
    def test_unknown_kind_fails_closed(self):
        x=copy.deepcopy(self.cases['BAN-01-LOCAL-VS-WASTE']);x['kind']='invented'
        with self.assertRaises(ValueError): result(x)
    def test_no_fabricated_credit_probability(self):
        self.assertNotIn('D_probability',json.dumps(self.report))

if __name__=='__main__':unittest.main()
