"""Independent synthetic stage-extension checks.

Reuses ORIGINAL PR57 ACC agentic_reduction.py and CASES.json as source of truth.
No empirical claims and no updates to the frozen 30x6 reference results.
"""
import itertools
import math
import unittest

from residual_cartography_stage import (
    CROSS_SOURCE_SCOPE,
    META_EXCHANGE_TIME,
    N_OBSERVERS,
    THRESHOLD,
    Observation,
    common_cartographic_label,
    example_events,
    fixture_case,
    geometric_referee_value,
    local_claim,
    qualified_event,
    region_utility_lower_infimum,
    three_stages,
)


class CartographicStageTest(unittest.TestCase):
    def setUp(self):
        self.s = fixture_case()
        self.events = example_events()

    def test_source_fixture_remains_actual_AG01(self):
        self.assertEqual(self.s["id"], "AG01-QUALIFIED-NEAR-OPTIMUM")
        self.assertEqual(self.s["public"]["total_resources"], 10)
        self.assertEqual(self.s["truth_private"]["recipient_incremental_rate"], 2)
        self.assertEqual(self.s["public"]["overhead_resources"], .25)
        self.assertEqual(self.s["Q"]["lower_rate"], 1.6)
        self.assertEqual(self.s["Q"]["transfer_ceiling"], 2)

    def test_demorgan_on_four_binary_event_projections(self):
        for flags in itertools.product((.5, .9), repeat=N_OBSERVERS):
            e = Observation("candidate", META_EXCHANGE_TIME+1,
                            CROSS_SOURCE_SCOPE, tuple(flags))
            verdict = qualified_event(e, required_scope=CROSS_SOURCE_SCOPE)
            outside_each = all(x > THRESHOLD for x in flags)
            not_any_inside = not any(x <= THRESHOLD for x in flags)
            self.assertEqual(outside_each, not_any_inside)
            self.assertEqual(verdict["joint_region"], outside_each)

    def test_geometry_has_value_bound_not_optimum_claim(self):
        baseline = geometric_referee_value((.5, .5, .5, .5))
        candidate = geometric_referee_value((.9, .85, .8, .95))
        self.assertAlmostEqual(baseline, .75)
        self.assertAlmostEqual(region_utility_lower_infimum(), .84)
        self.assertAlmostEqual(candidate, .98125)
        self.assertGreater(candidate, .84)
        self.assertLess(candidate, 1)
        self.assertGreater(candidate-baseline, .09)

    def test_qualified_conjunction_produces_meta_label(self):
        event = self.events[-1]
        verdict = qualified_event(event, required_scope=CROSS_SOURCE_SCOPE)
        self.assertTrue(verdict["joint_region"])
        self.assertEqual(verdict["meta_label"], "COMMON_RESIDUAL_CANDIDATE")
        self.assertEqual(len(verdict["source_observers"]), 4)

    def test_observer_only_sees_own_scalar(self):
        event = self.events[-1]
        for i in range(N_OBSERVERS):
            record = local_claim(event, i)
            self.assertEqual(record["observer_id"], "observer-" + str(i))
            self.assertEqual(record["finding"], "CERTIFIED_OUTSIDE_LOCAL_A")
            self.assertNotIn("features", record)

    def test_unknown_is_not_logical_negation(self):
        damaged = Observation("damaged", 8, CROSS_SOURCE_SCOPE,
                              (float("nan"), .9, .9, .9))
        verdict = qualified_event(damaged, required_scope=CROSS_SOURCE_SCOPE)
        self.assertFalse(verdict["joint_region"])

    def test_no_capture_is_not_logical_negation(self):
        not_captured = Observation("unseen", 8, CROSS_SOURCE_SCOPE,
                                   (.9, .9, .9, .9),
                                   captured_before_admission=False)
        self.assertFalse(qualified_event(
            not_captured, required_scope=CROSS_SOURCE_SCOPE)["joint_region"])

    def test_scope_mismatch(self):
        wrong = Observation("candidate", 8, "other-scope",
                            (.9, .9, .9, .9))
        self.assertFalse(qualified_event(
            wrong, required_scope=CROSS_SOURCE_SCOPE)["joint_region"])

    def test_different_event_records_do_not_compose(self):
        event = self.events[-1]
        claims = [local_claim(event, i) for i in range(4)]
        claims[2] = dict(claims[2], event_id="other-event")
        self.assertFalse(common_cartographic_label(
            claims, source_scope=CROSS_SOURCE_SCOPE)["joint_region"])

    def test_duplicate_source_not_independent_witness(self):
        event = self.events[-1]
        claims = [local_claim(event, i) for i in range(4)]
        claims[3] = dict(claims[3], observer_id="observer-1")
        self.assertFalse(common_cartographic_label(
            claims, source_scope=CROSS_SOURCE_SCOPE)["joint_region"])

    def test_stages_use_existing_original_ACC_planner(self):
        result = three_stages(events=self.events)
        one, two, three = (result[k] for k in
                           ("stage_1", "stage_2", "stage_3"))
        self.assertEqual(one["observed_by_referee_only"]["output"], 10)
        self.assertEqual(two["observed_by_referee_only"]["output"], 10)
        self.assertEqual(three["observed_by_referee_only"]["output"], 11.5)
        self.assertEqual(three["technical_optimum_referee_only"], 13.5)
        self.assertEqual(three["plan"]["transfer"], 2)
        self.assertEqual(three["plan"]["arm"], "Q_META_PROTOCOL")
        self.assertEqual(result["candidate_event_id"], "previously-unclassifiable-7")
        self.assertEqual(three["mission_output_gap_to_same_budget_technical_optimum"], 2)

    def test_stage_two_has_only_second_order_conditional_claim(self):
        result = three_stages(events=self.events)
        review = result["stage_2"]
        self.assertAlmostEqual(
            review["second_order_claimed_but_blocked_lower_bound"], .8)
        self.assertEqual(review["plan"]["transfer"], 0)
        self.assertEqual(
            review["mission_output_gap_to_same_budget_technical_optimum"], 3.5)

    def test_without_arrival_there_is_no_improvement(self):
        r = three_stages(events=self.events[:2])
        self.assertIsNone(r["candidate_event_id"])
        self.assertEqual(r["stage_3"]["observed_by_referee_only"]["output"], 10)

    def test_event_before_new_arrival_gate_does_not_travel_through_it(self):
        old = Observation("early-record", META_EXCHANGE_TIME-1,
                          CROSS_SOURCE_SCOPE, (.9, .85, .8, .95))
        r = three_stages(events=(old,))
        self.assertEqual(r["stage_3"]["plan"]["transfer"], 0)

    def test_unqualified_Q_to_region_mapping_must_hold(self):
        r = three_stages(events=self.events,
                         assumed_class_to_q_source_valid=False)
        self.assertEqual(r["stage_3"]["plan"]["transfer"], 0)
        self.assertEqual(r["stage_3"]["observed_by_referee_only"]["output"], 10)

    def test_invalid_B_source_protected_in_negative_AG11(self):
        r = three_stages(case_id="AG11-BOGUS-B-CERTIFICATE",
                         events=self.events, assumed_class_to_q_source_valid=False)
        self.assertEqual(r["stage_3"]["observed_by_referee_only"]["output"], 10)

    def test_unchecked_false_B_source_may_harm_in_AG11(self):
        unsafe = three_stages(case_id="AG11-BOGUS-B-CERTIFICATE",
                              events=self.events, assumed_class_to_q_source_valid=True)
        self.assertEqual(unsafe["stage_3"]["observed_by_referee_only"]["output"], 8.875)
        self.assertFalse(unsafe["stage_3"]["source_B_claim_supported_by_lab_truth"])

    def test_consent_is_not_created_by_meta_tag(self):
        refused = three_stages(case_id="AG07-DONOR-REFUSES",
                               events=self.events)
        self.assertEqual(refused["stage_3"]["plan"]["transfer"], 0)
        self.assertEqual(refused["stage_3"]["observed_by_referee_only"]["output"], 10)

    def test_strong_conventional_same_Q_ties(self):
        r = three_stages(events=self.events)
        original = r["stage_3"]["observed_by_referee_only"]["output"]
        conventional = r["matched_conventional_with_same_q"]["observed_by_referee_only"]["output"]
        self.assertEqual(original, conventional)
        self.assertEqual(original, 11.5)

    def test_meta_not_same_as_technical_optimum(self):
        r = three_stages(events=self.events)
        self.assertGreater(r["stage_3"]["technical_optimum_referee_only"],
                           r["stage_3"]["observed_by_referee_only"]["output"])

    def test_arrival_probability_is_external_assumption(self):
        p = (1-THRESHOLD)**N_OBSERVERS
        self.assertAlmostEqual(p, .0256)
        self.assertGreater(1/p, 39)
        self.assertLess(1/p, 40)
        self.assertEqual(self.events[-1].time, 7)


    def test_stage_two_cartography_is_an_observed_prefix_claim(self):
        r = three_stages(events=self.events)
        msg = r["stage_2_source_cartography"]
        self.assertTrue(msg["no_matched_event_as_of_meta_exchange"])
        self.assertEqual(msg["prior_qualified_hit_ids"], [])
        self.assertTrue(msg["unknown_future_encounter_time_and_agent"])
        self.assertAlmostEqual(
            msg["independently_sourced_AG01_near_gain_lower_bound"], .8)

    def test_early_qualifying_event_is_not_falsely_declared_absent(self):
        early = Observation("early-qualified", META_EXCHANGE_TIME-1,
                            CROSS_SOURCE_SCOPE, (.9, .85, .8, .95))
        r = three_stages(events=(early,))
        self.assertFalse(
            r["stage_2_source_cartography"]["no_matched_event_as_of_meta_exchange"])
        self.assertEqual(
            r["stage_2_source_cartography"]["prior_qualified_hit_ids"],
            ["early-qualified"])
        self.assertTrue(
            r["stage_2_source_cartography"]
            ["earlier_retained_hits_are_not_replayed_by_this_new_gate"])
        self.assertEqual(r["stage_3"]["plan"]["transfer"], 0)

    def test_new_meta_syntax_message_has_version_and_provenance(self):
        r = three_stages(events=self.events)
        rule = r["stage_3_meta_syntax_message"]
        self.assertEqual(rule["rule_version"], 1)
        self.assertEqual(rule["event_id"], "previously-unclassifiable-7")
        self.assertEqual(rule["source_scope"], CROSS_SOURCE_SCOPE)
        self.assertEqual(rule["meta_label"], "COMMON_RESIDUAL_CANDIDATE")
        self.assertEqual(len(rule["source_observers"]), 4)
        self.assertEqual(rule["accepted_ordinary_action"],
                         "EXISTING_AUTHORIZED_TRANSFER")
        self.assertEqual(rule["transfer_amount_if_authorized"], 2)
        self.assertFalse(rule["broadcast_performed"])
        self.assertFalse(rule["full_external_population_identified"])
        self.assertIn("consent_and_authority", rule["receiver_must_revalidate"])
        self.assertIn("source_version_and_truth", rule["receiver_must_revalidate"])

    def test_absent_candidate_cannot_emit_revised_rule(self):
        r = three_stages(events=self.events[:2])
        self.assertIsNone(r["stage_3_meta_syntax_message"])
        self.assertFalse(r["meta_label"]["joint_region"])

    def test_unqualified_source_can_emit_unadopted_rule_but_not_act(self):
        r = three_stages(events=self.events,
                         assumed_class_to_q_source_valid=False)
        rule = r["stage_3_meta_syntax_message"]
        self.assertIsNotNone(rule)
        self.assertFalse(rule["class_to_Q_source_is_synthetically_qualified"])
        self.assertEqual(rule["accepted_ordinary_action"], "NO_ACTION_ALLOWED")
        self.assertEqual(rule["transfer_amount_if_authorized"], 0)
        self.assertFalse(rule["broadcast_performed"])

    def test_refused_consent_keeps_candidate_meta_label_but_no_transfer(self):
        r = three_stages(case_id="AG07-DONOR-REFUSES", events=self.events)
        rule = r["stage_3_meta_syntax_message"]
        self.assertEqual(rule["meta_label"], "COMMON_RESIDUAL_CANDIDATE")
        self.assertEqual(rule["accepted_ordinary_action"], "NO_ACTION_ALLOWED")
        self.assertEqual(rule["transfer_amount_if_authorized"], 0)



if __name__ == "__main__":
    unittest.main()
