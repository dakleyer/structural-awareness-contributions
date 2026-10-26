"""Self-contained local checks for the Conscientia/ACC test matrix.

Do not count these as independent product, social or psychological tests.
"""
import copy
import importlib.util
import json
import math
import unittest
from pathlib import Path

PATH=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('ce_campaign',PATH/'campaign.py')
app=importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)


class CampaignFixtureIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources=app.read_json('SOURCE_REGISTER.json')
        cls.reg=app.read_json('CASE_REGISTRY.json')
        cls.cases=cls.reg['cases']
        cls.report=app.build_campaign(require_existing=False)
    def test_source_count(self): self.assertEqual(len(self.sources['sources']),23)
    def test_case_count(self): self.assertEqual(len(self.cases),60)
    def test_arm_count(self): self.assertEqual(len(app.ARMS),5)
    def test_family_count(self): self.assertEqual(len({x['family'] for x in self.cases}),12)
    def test_five_variants_each(self):
        for f in {x['family'] for x in self.cases}:
            self.assertEqual(len([c for c in self.cases if c['family']==f]),5)
    def test_unique_ids_and_sources(self):
        app.validate_cases(self.sources,self.reg)
    def test_all_cases_explicitly_synthetic(self):
        self.assertTrue(all(c['test_evidence_tier']=='SYNTHETIC_FIXTURE' for c in self.cases))
    def test_no_real_human_data(self):
        self.assertTrue(all(c['not_a_real_person_or_product'] for c in self.cases))
    def test_physical_no_data_oracle(self):
        c=next(c for c in self.cases if c['case_id']=='VERS-VALID_GO')
        r1=app.public_policy(c['public'],c['Q'],c['peer'],c['expanded_A'],'A_ONLY')
        other=copy.deepcopy(c);other['truth_private_for_scoring']='BLOCK'
        r2=app.public_policy(other['public'],other['Q'],other['peer'],other['expanded_A'],'A_ONLY')
        self.assertEqual(r1,r2)
    def test_public_Q_no_private_truth(self):
        c=next(c for c in self.cases if c['case_id']=='VERS-VALID_GO')
        r=app.public_policy(c['public'],c['Q'],c['peer'],c['expanded_A'],'QUALIFIED_Q')
        self.assertNotIn('truth_PRIVATE',r)
        self.assertEqual(r['action'],'ALLOW')
    def test_invalid_arms_rejected(self):
        c=self.cases[0]
        with self.assertRaises(ValueError):
            app.public_policy(c['public'],c['Q'],c['peer'],c['expanded_A'],'imaginary')
    def test_no_implicit_C_Roi(self):
        for c in self.cases:
            if c['variant']=='OPEN_RESIDUAL':
                self.assertIsNone(c['Q']['verdict'])
    def test_D_has_no_fabricated_distribution(self):
        self.assertFalse(any('prior_probability_of_D' in c for c in self.cases))
    def test_report_has_no_empirical_claim(self):
        self.assertIn('NO_HUMAN_OR_NATIVE_VENDOR_TEST',self.report['evidence_status'])
    def test_source_URLs_are_fixed_originals(self):
        for x in self.sources['sources']:
            self.assertIn('https://',x['url'])
            self.assertTrue(x['relevant_passage'])


class ExpectedComparators(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r=app.build_campaign(require_existing=False)['decision_experiments']
        cls.rows=cls.r['results']
        cls.by_case={x['case_id']:x for x in cls.rows}
    def test_deterministic_300_arm_results(self):
        self.assertEqual(self.r['arm_decisions'],300)
    def test_adjudicable_per_arm(self):
        self.assertTrue(all(v['adjudicable']==48 for v in self.r['totals'].values()))
    def test_open_remains_unscored(self):
        for row in self.rows:
            if row['variant']=='OPEN_RESIDUAL':
                self.assertTrue(all(v['correctness']=='NOT_ADJUDICABLE' for v in row['arms'].values()))
    def test_native_valid_Q_can_help(self):
        row=self.by_case['VERS-VALID_BLOCK']
        self.assertEqual(row['arms']['QUALIFIED_Q']['action'],'BLOCK')
        self.assertEqual(row['arms']['QUALIFIED_Q']['correctness'],'CORRECT')
    def test_A_only_some_true_positives(self):
        self.assertGreater(self.r['totals']['A_ONLY']['correct'],0)
    def test_peer_may_win(self):
        self.assertGreater(self.r['totals']['CONVENTIONAL_TARGETED']['net_utility_adjudicable_synthetic'],
                           self.r['totals']['PARTIAL_Q_AUDIT_GATED']['net_utility_adjudicable_synthetic'])
    def test_false_Q_is_not_certified_by_labels(self):
        row=self.by_case['VERS-FALSE_Q']
        self.assertEqual(row['arms']['QUALIFIED_Q']['correctness'],'WRONG')
    def test_audit_gate_has_negative_control(self):
        self.assertGreater(self.r['totals']['PARTIAL_Q_AUDIT_GATED']['wrong'],0)
    def test_audited_gate_improves_naive_Q(self):
        self.assertLess(self.r['totals']['PARTIAL_Q_AUDIT_GATED']['wrong'],
                        self.r['totals']['QUALIFIED_Q']['wrong'])
    def test_audited_gate_cost_is_nonzero(self):
        self.assertGreater(self.r['totals']['PARTIAL_Q_AUDIT_GATED']['instrument_cost_all_cases'],
                           self.r['totals']['QUALIFIED_Q']['instrument_cost_all_cases'])
    def test_full_A_may_be_expensive(self):
        self.assertLess(self.r['totals']['EXPANDED_A']['net_utility_adjudicable_synthetic'],
                        self.r['totals']['A_ONLY']['net_utility_adjudicable_synthetic'])
    def test_stale_B_not_accepted(self):
        row=self.by_case['VERS-STALE']
        self.assertEqual(row['arms']['QUALIFIED_Q']['evidence_mode'],'REJECTED_STALE_OR_INVALID_B')
    def test_expansion_unavailable_not_oracle(self):
        row=self.by_case['EDUC-VALID_BLOCK']
        self.assertEqual(row['arms']['EXPANDED_A']['evidence_mode'],'FULL_RECONSTRUCTION_UNAVAILABLE')
    def test_no_automatic_hold_when_valid_allow(self):
        row=self.by_case['VERS-VALID_GO']
        self.assertEqual(row['arms']['QUALIFIED_Q']['action'],'ALLOW')
    def test_peer_has_independent_signal(self):
        row=self.by_case['SOLID-VALID_GO']
        self.assertEqual(row['arms']['CONVENTIONAL_TARGETED']['evidence_mode'],'TARGETED_CONVENTIONAL_EVIDENCE')
    def test_no_abstract_equivalence_claim(self):
        self.assertIn('NOT prevalence',self.r['population_warning'])


class CausalAndHumanBoundaries(unittest.TestCase):
    def test_factorial_has_all_combinations(self):
        rows=app.factorial_joint_information()
        self.assertEqual(len(rows),8)
        self.assertEqual(len({(r['proof_required'],r['valid_Q_available'],r['joint_mechanism_available']) for r in rows}),8)
    def test_Q_alone_cannot_move_resources(self):
        rows=app.factorial_joint_information()
        self.assertTrue(all(x['additional_joint_output_synthetic']==0 for x in rows if not x['joint_mechanism_available']))
    def test_both_Q_and_joint_can_be_needed(self):
        row=next(r for r in app.factorial_joint_information() if r['proof_required'] and r['valid_Q_available'] and r['joint_mechanism_available'])
        self.assertEqual(row['additional_joint_output_synthetic'],2)
    def test_joint_without_Q_when_no_proof_needed(self):
        row=next(r for r in app.factorial_joint_information() if not r['proof_required'] and not r['valid_Q_available'] and r['joint_mechanism_available'])
        self.assertEqual(row['additional_joint_output_synthetic'],2)
    def test_FH_C_can_be_supported_and_opposed(self):
        rows=app.fh_c_competing_ablations()
        self.assertEqual(len(rows),8)
        for profile in ("BOUNDARY_SIGNAL_STRONGER","DOMAIN_FACTS_STRONGER"):
            q=next(x for x in rows if x['profile']==profile and x['with_boundary_Q'] and not x['with_extra_domain_facts'])
            d=next(x for x in rows if x['profile']==profile and not x['with_boundary_Q'] and x['with_extra_domain_facts'])
            if profile=="BOUNDARY_SIGNAL_STRONGER": self.assertLess(q['invalid_mission_pivots'],d['invalid_mission_pivots'])
            else: self.assertGreater(q['invalid_mission_pivots'],d['invalid_mission_pivots'])
    def test_FH_C_positive_changes_remain(self):
        self.assertTrue(all(x['valid_changes_preserved']==2 for x in app.fh_c_competing_ablations()))
    def test_dense_network_ratio_increases_under_parameters(self):
        x=[r['gap_over_output_pct_ASSUMED'] for r in app.network_gap() if r['topology']=='dense']
        self.assertEqual(x,[4.,9.,19.,39.])
    def test_sparse_network_ratio_not_same_curve(self):
        r=app.network_gap()
        self.assertLess(max(x['gap_over_output_pct_ASSUMED'] for x in r if x['topology']=='star'),2.)
    def test_entropy_from_finite_states_only(self):
        e=app.finite_information()
        self.assertEqual(e['h_response_given_A_bits'],1.)
        self.assertEqual(e['h_response_given_A_and_B_bits'],0.)
        self.assertEqual(e['conditional_mutual_information_bits'],1.)
    def test_KL_orientation(self):
        e=app.finite_information()
        self.assertEqual(e['KL_P_to_Q_bits'],'INFINITE_SUPPORT_MISMATCH')
        self.assertEqual(e['KL_Q_to_P_bits'],1.)
    def test_human_proxy_not_subjective_pain(self):
        r=app.gap_and_human_limits()
        self.assertEqual(r['role_development_proxy_synthetic'],3.)
        self.assertEqual(r['human_suffering_experienced'],'NOT_MEASURED')
    def test_human_functionality_does_not_reduce_dignity(self):
        self.assertEqual(app.gap_and_human_limits()['human_dignity'],'NOT_A_PRODUCTIVITY_METRIC')
    def test_not_infer_HID_from_ACW(self):
        self.assertIn('NOT_01K_CLAIM',app.gap_and_human_limits()['HID_task_time_synthetic']['measurement_status'])
    def test_attribution_edition_conflict_gates_metric(self):
        self.assertIn('BLOCKED_FOR_COMPUTATION',app.gap_and_human_limits()['attribution_gap_D02_formula'])
    def test_no_capture_recapture_without_sampling(self):
        self.assertIn('NOT_IDENTIFIED',app.gap_and_human_limits()['cost_clarity_capture_recapture'])
    def test_solidarity_is_not_automatic_approval(self):
        self.assertEqual(app.gap_and_human_limits()['solidarity']['software_authorization'],'NOT_GRANTED')
    def test_uc21_only_six_pending_templates(self):
        rows=app.source_uc21_templates()
        self.assertEqual(len(rows),6)
        self.assertEqual(sum(r['gate_count'] for r in rows),37)
        self.assertTrue(all(r['product_execution']=='NOT_RUN' for r in rows))
    def test_report_reproducible_locally(self):
        a=app.build_campaign(require_existing=False)
        b=app.read_json('REFERENCE_SYNTHETIC_RESULTS.json')
        self.assertEqual(a,b)


if __name__=='__main__':unittest.main()
