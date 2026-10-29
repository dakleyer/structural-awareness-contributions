"""G-03: IQ03 resource gap should be generated from a finite capability model."""
from __future__ import annotations

import unittest

import campaign
from finite_feasible_gap import optimize, original_iq03_periods


class FeasibleGapMechanismTests(unittest.TestCase):
    def test_original_two_period_source_values_are_computed_not_literals(self):
        early, late = original_iq03_periods()
        self.assertEqual((early["service"], early["current_resources"],
                          early["minimum_resources_among_DECLARED_PASS_modes"],
                          early["gap_relative_to_declared_current"]),
                         ("100", "100", "80", "20"))
        self.assertEqual((late["service"], late["current_resources"],
                          late["minimum_resources_among_DECLARED_PASS_modes"],
                          late["gap_relative_to_declared_current"]),
                         ("140", "110", "65", "45"))
        original = campaign.source_anchored_microexperiments()["IQ03_EFFICIENCY_GAP"]
        self.assertEqual((original["service_t0"],original["service_t1"],
                          original["resource_gap_t0"],original["resource_gap_t1"]),
                         (100,140,20,45))
        self.assertEqual(original["alt_feasible"], "ASSUMED_WITHIN_EACH_PERIOD")

    def test_changed_alt_efficiency_can_eliminate_increasing_gap(self):
        first = optimize(100, [
            {"id":"incumbent","capacity":100,"resource_per_service":1,"eligibility":"PASS"},
            {"id":"alt","capacity":100,"resource_per_service":"4/5","eligibility":"PASS"},
        ], {"incumbent":100})
        next_period = optimize(140, [
            {"id":"incumbent","capacity":140,"resource_per_service":"11/14","eligibility":"PASS"},
            {"id":"alt","capacity":140,"resource_per_service":"11/14","eligibility":"PASS"},
        ], {"incumbent":140})
        self.assertEqual(first["gap_relative_to_declared_current"], "20")
        self.assertEqual(next_period["gap_relative_to_declared_current"], "0")

    def test_setup_and_capacity_are_endogenous_costs_not_ignored(self):
        def modes(startup):
            return [
                {"id":"current","capacity":10,"resource_per_service":1,
                 "eligibility":"PASS"},
                {"id":"new","capacity":10,"resource_per_service":"1/2",
                 "fixed_resource":startup,"eligibility":"PASS"},
            ]
        self.assertEqual(optimize(10,modes(6),{"current":10})
                         ["minimum_resources_among_DECLARED_PASS_modes"],"10")
        self.assertEqual(optimize(10,modes(4),{"current":10})
                         ["minimum_resources_among_DECLARED_PASS_modes"],"9")
        partial = optimize(10, [
            {"id":"current","capacity":10,"resource_per_service":1,"eligibility":"PASS"},
            {"id":"new","capacity":5,"resource_per_service":"1/10",
             "fixed_resource":2,"eligibility":"PASS"},
        ], {"current":10})
        self.assertEqual(partial["minimum_resources_among_DECLARED_PASS_modes"],"15/2")

    def test_unverified_rights_cannot_become_certified_optimum(self):
        result = optimize(10, [
            {"id":"incumbent","capacity":10,"resource_per_service":1,"eligibility":"PASS"},
            {"id":"possibly_cheaper","capacity":10,"resource_per_service":"1/10",
             "eligibility":"UNKNOWN"},
        ], {"incumbent":10})
        self.assertEqual(result["minimum_resources_among_DECLARED_PASS_modes"], "10")
        self.assertEqual(result["coverage"], "OPEN_WITH_UNRESOLVED_OPTIONS")
        self.assertEqual(result["unknown_eligibility_modes"], ["possibly_cheaper"])
        self.assertTrue(result["source_assumptions_are_not_external_feasibility_proof"])

    def test_invalid_capacity_service_or_tech_is_rejected(self):
        current = {"id":"incumbent","capacity":10,"resource_per_service":1,
                   "eligibility":"PASS"}
        for bad in (
            [{"id":"incumbent","capacity":10,"resource_per_service":1,"eligibility":"PASS"},
             {"id":"incumbent","capacity":10,"resource_per_service":1,"eligibility":"PASS"}],
            [{"id":"incumbent","capacity":10,"resource_per_service":-1,"eligibility":"PASS"}],
            [{"id":"incumbent","capacity":10,"resource_per_service":1,"eligibility":"MAYBE"}],
        ):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                optimize(10,bad,{"incumbent":10})
        with self.assertRaisesRegex(ValueError,"does not meet"):
            optimize(10,[current],{"incumbent":9})
        with self.assertRaisesRegex(ValueError,"exceeds"):
            optimize(12,[current],{"incumbent":12})
        with self.assertRaises(ValueError):
            optimize(True,[current],{"incumbent":10})

    def test_conventional_inexpensive_option_is_allowed_to_win(self):
        result = optimize(20, [
            {"id":"source_B","capacity":20,"resource_per_service":"3/5",
             "fixed_resource":3,"eligibility":"PASS"},
            {"id":"targeted_conventional","capacity":20,"resource_per_service":"1/2",
             "fixed_resource":1,"eligibility":"PASS"},
        ], {"source_B":20})
        self.assertEqual(result["current_resources"],"15")
        self.assertEqual(result["minimum_resources_among_DECLARED_PASS_modes"],"11")
        self.assertIn({"targeted_conventional":"20"},result["optimizers_with_ties"])


if __name__ == "__main__":
    unittest.main()
