"""Deterministic controls for the illustrative writing-to-model campaign."""
import copy
import math
import unittest

from scenario_campaign import load_catalog, run_campaign


class CampaignExperimentControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_catalog()
        cls.results = run_campaign(cls.catalog)
        cls.lookup = {
            item["id"]: item
            for rows in cls.results["results"].values()
            for item in rows
        }

    def option(self, case_id, name):
        return next(item for item in self.lookup[case_id]["options"] if item["name"] == name)

    def test_registered_case_count_and_unique_ids(self):
        self.assertEqual(self.results["count_cases"], 20)
        self.assertEqual(len(self.lookup), 20)

    def test_synthetic_boundary_is_explicit(self):
        self.assertEqual(self.results["status"], "SYNTHETIC_CONDITIONAL_NOT_EMPIRICAL")
        self.assertNotIn("F_observed", str(self.results))

    def test_reference_reproduction_deterministic(self):
        self.assertEqual(self.results, run_campaign(copy.deepcopy(self.catalog)))
        self.assertEqual(len(self.results["input_sha256"]), 64)

    def test_telework_preserves_declared_service_and_frees_resources(self):
        onsite = self.option("EX01_TELEWORK", "ONSITE")
        remote = self.option("EX01_TELEWORK", "REMOTE")
        self.assertEqual(onsite["service_value"], remote["service_value"])
        self.assertEqual(remote["net_difference_from_baseline"], 15)
        self.assertEqual(self.lookup["EX01_TELEWORK"]["social_surplus_winner_under_declared_guardrails"], "REMOTE")

    def test_physical_task_rejects_under_servicing_remote_choice(self):
        remote = self.option("EX01B_PHYSICAL_WORK_CONTROL", "REMOTE_UNDER_SERVICE")
        self.assertFalse(remote["eligible_under_stipulated_guardrails"])
        self.assertEqual(self.lookup["EX01B_PHYSICAL_WORK_CONTROL"]["social_surplus_winner_under_declared_guardrails"], "ONSITE")

    def test_garden_recursive_spend_can_raise_activity_while_lowering_net(self):
        names = ["SOIL", "TILES", "WOOD_ON_TILES", "PURCHASED_SOIL_ON_WOOD"]
        rows = [self.option("EX02_GARDEN_RECURSION", name) for name in names]
        net = [row["social_net_value"] for row in rows]
        trans = [row["commercial_transactions_not_social_value"] for row in rows]
        self.assertEqual(net, [89, 75, 65, 46])
        self.assertEqual(trans, [10, 25, 48, 80])

    def test_genuine_garden_innovation_can_create_more_value(self):
        renovated = self.option("EX02_GARDEN_RECURSION", "GENUINELY_BENEFICIAL_RENOVATION")
        self.assertEqual(renovated["net_difference_from_baseline"], 18)
        self.assertEqual(self.lookup["EX02_GARDEN_RECURSION"]["social_surplus_winner_under_declared_guardrails"],
                         "GENUINELY_BENEFICIAL_RENOVATION")

    def test_platform_low_added_reach_and_high_value_controls(self):
        low = self.option("EX03_SOCIAL_PLATFORM", "LOW_ADDED_REACH")
        high = self.option("EX03_SOCIAL_PLATFORM", "HIGH_ADDED_REACH")
        self.assertEqual(low["net_difference_from_baseline"], -18)
        self.assertEqual(high["net_difference_from_baseline"], 30)
        self.assertGreater(high["commercial_transactions_not_social_value"],
                           self.option("EX03_SOCIAL_PLATFORM", "DIRECT_RELATIONS")["commercial_transactions_not_social_value"])

    def test_climate_avoided_demand_beats_vehicle_upgrade_conditionally(self):
        ev = self.option("EX04_CITY_CLIMATE", "VEHICLE_EFFICIENCY_UPGRADE")
        avoided = self.option("EX04_CITY_CLIMATE", "AVOID_UNNECESSARY_TRIP")
        self.assertEqual(ev["social_net_value"], 48)
        self.assertEqual(avoided["social_net_value"], 78)
        self.assertEqual(self.lookup["EX04_CITY_CLIMATE"]["social_surplus_winner_under_declared_guardrails"],
                         "AVOID_UNNECESSARY_TRIP")

    def test_private_incentive_and_social_welfare_need_not_align(self):
        case = self.lookup["EX04_CITY_CLIMATE"]
        self.assertTrue(case["private_social_rankings_diverge"])
        self.assertEqual(case["private_actor_winner_under_declared_preferences"], "VEHICLE_EFFICIENCY_UPGRADE")

    def test_non_replaceable_physical_travel_is_not_conceded(self):
        physical = self.option("EX04_CITY_CLIMATE", "AVOID_REQUIRED_PHYSICAL_TRIP_INVALID")
        self.assertFalse(physical["eligible_under_stipulated_guardrails"])

    def test_rare_junction_does_not_justify_roundabout_by_activity(self):
        case = self.lookup["EX05_RARE_INTERSECTION"]
        build = self.option("EX05_RARE_INTERSECTION", "BUILD_ROUNDABOUT")
        self.assertEqual(case["social_surplus_winner_under_declared_guardrails"], "KEEP_SAFE_JUNCTION")
        self.assertLess(build["net_difference_from_baseline"], 0)
        self.assertGreater(build["activity_difference_from_baseline"], 0)

    def test_busy_junction_legitimately_supports_roundabout(self):
        case = self.lookup["EX05B_BUSY_INTERSECTION_CONTROL"]
        self.assertEqual(case["social_surplus_winner_under_declared_guardrails"], "BUILD_USEFUL_ROUNDABOUT")

    def test_parent_can_prefer_symbolic_care_while_child_account_is_negative(self):
        case = self.lookup["EX06_UNDERUSED_CHILD_PARK"]
        self.assertEqual(case["parent_private_gain_from_symbolic_care"], 28)
        self.assertEqual(case["child_net_of_allocated_future_tax"], -191.04)
        self.assertTrue(case["parent_prefers_build_in_simplified_two_choice_problem"])
        self.assertEqual(case["child_service_minus_real_resources_NOT_full_social_welfare"], -211.04)
        self.assertEqual(case["future_tax_pv_is_transfer_not_extra_social_cost"], 200)

    def test_used_park_positive_control(self):
        used = self.lookup["EX06B_USED_CHILD_PARK_CONTROL"]
        self.assertEqual(used["child_service_minus_real_resources_NOT_full_social_welfare"], 68.8)
        self.assertGreater(used["child_net_of_allocated_future_tax"], 0)
        self.assertTrue(used["child_service_exceeds_real_resources_before_unaggregated_preferences"])

    def test_park_probabilities_and_budget_are_not_assumed_unbounded(self):
        bad = copy.deepcopy(self.catalog)
        bad["park_cases"][0]["prob_use"] = 1.1
        with self.assertRaises(ValueError):
            run_campaign(bad)
        bad = copy.deepcopy(self.catalog)
        bad["park_cases"][0]["future_tax_liability_pv"] += 3
        with self.assertRaises(ValueError):
            run_campaign(bad)

    def test_same_gamma_and_more_mean_can_still_mean_stay(self):
        early = self.lookup["EX07_MIGRATION_EARLY"]
        later = self.lookup["EX07_MIGRATION_LATE"]
        self.assertEqual((early["stay_ce"], early["redesign_ce_after_one_transition_cost"]), (9, 7))
        self.assertEqual((later["stay_ce"], later["redesign_ce_after_one_transition_cost"]), (13, 9))
        self.assertGreater(later["redesign_mean_gain_before_cost"], early["redesign_mean_gain_before_cost"])
        self.assertEqual(early["gamma_fixed_within_case"], later["gamma_fixed_within_case"])

    def test_pessimism_distress_and_persistence_are_not_incompatible(self):
        later = self.lookup["EX07_MIGRATION_LATE"]
        self.assertTrue(later["stipulations_not_human_observations"]["forecast_future_stay_below_current"])
        self.assertEqual(later["stipulations_not_human_observations"]["synthetic_discomfort_F"], 13)
        self.assertEqual(later["preferred_under_characterized_cara_normal"], "STAY")

    def test_insuring_exit_reverses_choice(self):
        case = self.lookup["EX07B_INSURED_EXIT_CONTROL"]
        self.assertEqual(case["preferred_under_characterized_cara_normal"], "REDESIGN")
        self.assertEqual(case["redesign_excess_variance"], 0)

    def test_care_bonus_changes_total_utility_even_without_material_risk_change(self):
        case = self.lookup["EX07C_CARE_AS_UTILITY"]["defense"]
        self.assertTrue(case["same_material_payoff_as_stay"])
        self.assertTrue(case["same_variance_as_stay"])
        self.assertEqual(case["intrinsic_utility_added_to_material_mean"], 1)
        self.assertEqual(case["certainty_equivalents"]["DEFEND_STAY"], 13.5)
        self.assertEqual(case["preferred"], "DEFEND_STAY")

    def test_truman_social_validation_has_an_identifiable_utility_threshold(self):
        weak = self.lookup["EX07E_WEAK_SOCIAL_VALIDATION"]["defense"]
        strong = self.lookup["EX07F_STRONG_SOCIAL_VALIDATION"]["defense"]
        self.assertEqual(weak["preferred"], "STAY")
        self.assertEqual(strong["preferred"], "DEFEND_STAY")
        self.assertTrue(weak["same_material_payoff_as_stay"])
        self.assertTrue(strong["same_material_payoff_as_stay"])
        self.assertEqual(strong["intrinsic_utility_added_to_material_mean"], 1)

    def test_neutral_risk_control_chooses_higher_mean(self):
        case = self.lookup["EX07D_NEUTRAL_RISK_CONTROL"]
        self.assertEqual(case["preferred_under_characterized_cara_normal"], "REDESIGN")
        self.assertIsNone(case["strict_stay_if_redesign_variance_exceeds"])

    def test_sierra_three_steps_and_twenty_five_diverge(self):
        short = self.lookup["EX08_SIERRA_SHORT"]
        long = self.lookup["EX08_SIERRA_LONG"]
        self.assertAlmostEqual(short["expected_change_in_G_versus_stay"], -11.4425)
        self.assertAlmostEqual(long["expected_change_in_G_versus_stay"], 23.3566256127)
        self.assertTrue(short["expected_G_decreases"])
        self.assertFalse(long["expected_G_decreases"])

    def test_sierra_better_step_reliability_reverses_expected_effect(self):
        fixed = self.lookup["EX08B_MODULAR_RECOVERY_CONTROL"]
        self.assertTrue(fixed["expected_G_decreases"])
        self.assertLess(fixed["expected_change_in_G_versus_stay"], 0)

    def test_probabilistic_route_validation(self):
        bad = copy.deepcopy(self.catalog)
        bad["route_cases"][0]["step_success_probability"] = -0.01
        with self.assertRaises(ValueError):
            run_campaign(bad)
        bad = copy.deepcopy(self.catalog)
        bad["route_cases"][0]["steps"] = 2.5
        with self.assertRaises(ValueError):
            run_campaign(bad)

    def test_intergenerational_ratio_is_only_a_synthetic_index(self):
        case = self.lookup["EX09_INTERGENERATIONAL_RATIOS"]
        self.assertFalse(case["statistical_estimate"])
        self.assertEqual(case["gross_housing_price_to_wage_multiplier"], 8)
        self.assertAlmostEqual(case["net_after_declared_transfer_multiplier"], 11.9402985075)

    def test_same_parameters_generate_both_positive_and_negative_cases(self):
        self.assertTrue(any(row["net_difference_from_baseline"] > 0
                            for case in self.results["results"]["static_cases"]
                            for row in case["options"]))
        self.assertTrue(any(row["net_difference_from_baseline"] < 0
                            for case in self.results["results"]["static_cases"]
                            for row in case["options"]))

    def test_risk_grid_contains_both_exit_and_persistence_with_same_means(self):
        rows = self.results["sensitivity"]["risk_sign_grid"]
        self.assertEqual(len(rows), 25)
        winners = {row["preferred"] for row in rows}
        self.assertIn("STAY", winners)
        self.assertIn("REDESIGN", winners)
        by_gamma = [row for row in rows if row["gamma"] == 0.5]
        self.assertEqual(len(by_gamma), 5)
        self.assertEqual(next(r for r in by_gamma if r["redesign_variance"] == 64)["preferred"], "STAY")

    def test_park_grid_crosses_the_material_resource_break_even(self):
        rows = self.results["sensitivity"]["park_real_resource_grid"]
        self.assertEqual(len(rows), 6)
        self.assertTrue(any(row["positive_excluding_unaggregated_preferences"] for row in rows))
        self.assertTrue(any(not row["positive_excluding_unaggregated_preferences"] for row in rows))

    def test_route_grid_is_not_universally_harmful_or_beneficial(self):
        rows = self.results["sensitivity"]["route_composition_grid"]
        self.assertEqual(len(rows), 8)
        self.assertTrue(any(row["expected_G_decreases"] for row in rows))
        self.assertTrue(any(not row["expected_G_decreases"] for row in rows))

    def test_invalid_parameter_grid_rejected(self):
        bad = copy.deepcopy(self.catalog)
        bad["sensitivity"]["gamma_grid"] = [0.5, -0.2]
        with self.assertRaises(ValueError):
            run_campaign(bad)

    def test_invalid_authority_is_not_a_small_cost(self):
        bad = copy.deepcopy(self.catalog)
        option = bad["static_cases"][0]["options"][1]
        option["rights_authorized"] = False
        result = run_campaign(bad)
        case = next(x for x in result["results"]["static_cases"] if x["id"] == "EX01_TELEWORK")
        remote = next(x for x in case["options"] if x["name"] == "REMOTE")
        self.assertFalse(remote["eligible_under_stipulated_guardrails"])

    def test_static_budget_bucket_nonoverlap_is_required(self):
        bad = copy.deepcopy(self.catalog)
        bad["static_cases"][0]["cost_buckets_nonoverlapping_stipulated"] = False
        with self.assertRaises(ValueError):
            run_campaign(bad)

    def test_intergenerational_cashflows_require_common_present_value_date(self):
        bad = copy.deepcopy(self.catalog)
        bad["park_cases"][0]["all_intertemporal_values_same_pv_date_stipulated"] = False
        with self.assertRaises(ValueError):
            run_campaign(bad)

    def test_no_unproven_park_independence(self):
        bad = copy.deepcopy(self.catalog)
        bad["park_cases"][0]["independent_use_and_functionality_stipulated"] = False
        with self.assertRaises(ValueError):
            run_campaign(bad)

    def test_normality_and_comparable_actor_horizon_are_explicit(self):
        bad = copy.deepcopy(self.catalog)
        bad["risk_cases"][0]["normal_lotteries_characterized_stipulated"] = False
        with self.assertRaises(ValueError):
            run_campaign(bad)

    def test_sierra_iid_does_not_carry_to_dependent_steps(self):
        bad = copy.deepcopy(self.catalog)
        bad["route_cases"][0]["independent_identical_steps_stipulated"] = False
        with self.assertRaises(ValueError):
            run_campaign(bad)

    def test_generational_analogy_requires_comparable_housing(self):
        bad = copy.deepcopy(self.catalog)
        bad["distribution_cases"][0]["comparable_housing_and_wage_units_stipulated"] = False
        with self.assertRaises(ValueError):
            run_campaign(bad)

    def test_gross_activity_does_not_enter_social_value_identity(self):
        bad = copy.deepcopy(self.catalog)
        bad["static_cases"][0]["options"][0]["gross_transactions"] += 999999
        a = run_campaign(bad)["results"]["static_cases"][0]
        b = self.results["results"]["static_cases"][0]
        self.assertEqual(a["options"][0]["social_net_value"], b["options"][0]["social_net_value"])


if __name__ == "__main__":
    unittest.main()
