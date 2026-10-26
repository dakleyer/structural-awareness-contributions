"""Regression tests: direct HID input gaps and ABCD matched network contrasts.

The fixtures are synthetic; no original 01K measurement study is run here.
"""

from copy import deepcopy
import json
from pathlib import Path
import unittest

from toy import ToyError, portfolio, network


def scenario(name):
    root = Path(__file__).parent
    canonical = root / "scenarios" / (name + ".json")
    fixture = canonical if canonical.exists() else root / (name + ".json")
    return json.loads(fixture.read_text(encoding="utf-8"))


class HIDOptimumTests(unittest.TestCase):
    def setUp(self):
        self.s = scenario("portfolio_hid")

    def test_each_tied_optimum_reports_its_own_simple_subtraction(self):
        p = portfolio(self.s)["hid"]["primary_optimum_input_gap"]
        self.assertEqual([x["HID_direct_hours"] for x in p["technical_utility_optima"]], [13, 15])
        self.assertEqual([x["HID_direct_ratio"] for x in p["governance_utility_optima"]], [.13, .15])
        self.assertEqual(len(p["technical_human_input_frontier"]), 2)
        self.assertEqual(p["actual_inputs"], {"diagnosis": 10, "design": 10})

    def test_acw_only_change_does_not_change_hid_from_optimum(self):
        before = portfolio(self.s)["hid"]["primary_optimum_input_gap"]
        self.s["projects"][0]["delta_acw_hours"] = -5
        after = portfolio(self.s)["hid"]["primary_optimum_input_gap"]
        self.assertEqual(before, after)

    def test_classification_gates_auxiliaries_not_input_comparison(self):
        self.s["parameters"]["acw_classified_synthetically"] = False
        h = portfolio(self.s)["hid"]
        self.assertIsNone(h["HID_observed"])
        self.assertEqual(h["primary_optimum_input_gap"]["technical_utility_optima"][0]["HID_direct_hours"], 13)

    def test_incorrect_input_sum_rejected(self):
        self.s["projects"][0]["delta_human_information_inputs"]["diagnosis"] = 11
        with self.assertRaises(ToyError):
            portfolio(self.s)

    def test_missing_input_dimensions_not_derived_from_acw(self):
        del self.s["projects"][0]["delta_human_information_inputs"]
        with self.assertRaises(ToyError):
            portfolio(self.s)

    def test_same_resource_usage_gate(self):
        self.s["projects"][0]["delta_resources"] = 1
        cases = portfolio(self.s)["hid"]["primary_optimum_input_gap"]["technical_utility_optima"]
        cases = {x["reference"]: x for x in cases}
        self.assertIsNone(cases["UPGRADE_A"]["HID_direct_hours"])
        self.assertEqual(cases["UPGRADE_B"]["HID_direct_hours"], 15)

    def test_same_service_gate(self):
        self.s["projects"][0]["output_deltas"]["full_service"] = 1
        cases = portfolio(self.s)["hid"]["primary_optimum_input_gap"]["technical_utility_optima"]
        self.assertIsNone(cases[0]["HID_direct_hours"])
        self.assertEqual(cases[1]["HID_direct_hours"], 15)

    def test_blocked_governance_remains_separate(self):
        self.s["approvals"]["Steward"] = False
        p = portfolio(self.s)["hid"]["primary_optimum_input_gap"]
        self.assertEqual(len(p["technical_utility_optima"]), 2)
        self.assertEqual(p["governance_utility_optima"][0]["HID_direct_hours"], 0)

    def test_old_portfolio_does_not_recast_acw_as_direct_hid(self):
        h = portfolio(scenario("portfolio"))["hid"]
        self.assertGreater(h["HID_potential"], 0)
        self.assertIsNone(h["primary_optimum_input_gap"]["technical_utility_optima"][0]["HID_direct_hours"])


class ABCDNetworkTests(unittest.TestCase):
    def setUp(self):
        self.s = scenario("network_abcd")

    def test_same_physics_different_qualifications_comparable(self):
        r = network(self.s)
        self.assertEqual(r["epistemic_ABCD_experiment"]["status"], "MATCHED_SYNTHETIC_PROCESS_CONTRAST")
        self.assertAlmostEqual(r["summary"]["last_HID_direct_hours"], 8.4)
        self.assertAlmostEqual(r["summary"]["last_delta2_HID_direct_hours"], .04)
        self.assertAlmostEqual(r["summary"]["last_delta2_HID_direct_ratio"], 0)
        self.assertEqual(r["rows"][-1]["human"]["primary_optimum_input_gap"]["reference_arm"], "A_result")

    def test_hid_from_inputs_even_if_acw_is_equal(self):
        r = network(self.s)
        at_end = r["arms"]
        self.assertEqual(at_end["D_residual"][-1]["d_t"], at_end["A_result"][-1]["d_t"])
        self.assertLess(at_end["D_residual"][-1]["H_GIC"], at_end["A_result"][-1]["H_GIC"])
        self.assertGreater(r["summary"]["last_HID_direct_hours"], 0)

    def test_null_penalty_blocks_automatic_debt_from_abcd_label(self):
        self.s["unqualified_dependency_input_loss_rates"] = {"diagnosis": 0, "design": 0}
        r = network(self.s)
        self.assertEqual(r["summary"]["last_HID_direct_hours"], 0)
        self.assertAlmostEqual(r["summary"]["last_delta2_HID_direct_hours"], 0)

    def test_sparse_physics_makes_hid_linear_under_same_policy(self):
        for arm in self.s["arms"].values():
            arm["topology"] = "sparse"
        r = network(self.s)
        self.assertGreater(r["summary"]["last_HID_direct_hours"], 0)
        self.assertAlmostEqual(r["summary"]["last_delta2_HID_direct_hours"], 0)

    def test_requalification_reduces_debt_without_claiming_a_label_is_numeric(self):
        self.s["arms"]["D_residual"]["epistemic_process"]["requalification_rate"] = .2
        self.s["arms"]["D_residual"]["epistemic_process"]["neo_hours_per_qualified_link"] = .1
        r = network(self.s)
        self.assertLess(r["summary"]["last_HID_direct_hours"], 8.4)
        self.assertGreater(r["arms"]["D_residual"][-1]["H_NEO_additional"], 0)

    def test_unmatched_physics_is_not_an_abcd_isolation(self):
        self.s["arms"]["A_result"]["p_incompatible"] = .15
        r = network(self.s)
        self.assertEqual(r["epistemic_ABCD_experiment"]["status"], "NOT_AN_ISOLATED_ABCD_CONTRAST")

    def test_no_guaranteed_service_is_an_inadmissible_actual_arm(self):
        self.s["arms"]["D_residual"]["full_service_preserved"] = False
        with self.assertRaises(ToyError):
            network(self.s)

    def test_no_negative_human_contribution_from_penalty(self):
        self.s["unqualified_dependency_input_loss_rates"]["diagnosis"] = 200
        with self.assertRaises(ToyError):
            network(self.s)

    def test_old_network_has_zero_primary_hid_despite_acw_difference(self):
        r = network(scenario("network"))
        self.assertEqual(r["rows"][-1]["HID_direct_hours"], 0)
        self.assertGreater(r["rows"][-1]["human"]["HID_potential"], 0)


if __name__ == "__main__":
    unittest.main()
