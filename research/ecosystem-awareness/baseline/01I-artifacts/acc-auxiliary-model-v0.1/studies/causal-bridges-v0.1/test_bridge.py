import copy
import json
import unittest
from pathlib import Path

from bridge import (
    ModelError, attribution_signatures, curvature, evaluate, hid_against_optima,
    map_flow, money_ledger, retirement,
)


FIXTURE = json.loads(Path(__file__).with_name("scenario.json").read_text())


class BridgeTests(unittest.TestCase):
    def test_gap_is_difference_of_same_resources_input_vectors(self):
        result = hid_against_optima(FIXTURE["HID"])
        self.assertEqual(result["HID_hours_range"], [10.0, 20.0])
        self.assertEqual([x["HID_reference"] for x in result["comparisons"]], [.2, .1])
        self.assertEqual(len(result["excluded"]), 1)

    def test_inaccessible_optimum_never_included(self):
        data = copy.deepcopy(FIXTURE["HID"])
        for x in data["optima"].values():
            x["governance_feasible"] = False
        self.assertIsNone(hid_against_optima(data)["HID_hours_range"])

    def test_multi_optima_no_coordinatewise_fantasy(self):
        data = copy.deepcopy(FIXTURE["HID"])
        data["optima"]["feasible_B"]["informational_inputs"] = {"diagnosis": 30, "judgement": 10, "design": 16}
        result = hid_against_optima(data)
        self.assertEqual(sorted(round(x["gap_hours"]) for x in result["comparisons"]), [16, 20])

    def test_false_dominance_rejected(self):
        data = copy.deepcopy(FIXTURE["HID"])
        data["optima"]["feasible_A"]["informational_inputs"]["judgement"] = 8
        self.assertNotIn("feasible_A", [x["optimum"] for x in hid_against_optima(data)["comparisons"]])

    def test_dominated_candidate_is_not_called_an_optimum(self):
        data = copy.deepcopy(FIXTURE["HID"])
        data["optima"]["feasible_B"]["informational_inputs"] = {
            "diagnosis": 16, "judgement": 12, "design": 16
        }
        result = hid_against_optima(data)
        self.assertEqual([x["optimum"] for x in result["comparisons"]], ["feasible_A"])
        self.assertTrue(any("dominated" in reason for _, reason in result["excluded"]))

    def test_hid_cannot_create_hours(self):
        data = copy.deepcopy(FIXTURE["HID"])
        data["optima"]["feasible_A"]["informational_inputs"]["judgement"] = 80
        with self.assertRaises(ModelError):
            hid_against_optima(data)

    def test_attribution_independent_sources_and_two_times(self):
        result = attribution_signatures(FIXTURE["attribution"])
        self.assertAlmostEqual(result["mean_gap_change"], .35)
        self.assertEqual(result["snapshots"][1]["ignored"], 6)
        self.assertIsNone(result["claim_B"])

    def test_attribution_source_circularity_rejected(self):
        data = copy.deepcopy(FIXTURE["attribution"])
        item = data["snapshots"][0]["pairs"]["appA:source-of-truth"]
        item["declaration_source"] = item["technical_source"]
        with self.assertRaises(ModelError):
            attribution_signatures(data)

    def test_attribution_missing_cohort_rejected(self):
        data = copy.deepcopy(FIXTURE["attribution"])
        data["snapshots"][1]["pairs"].pop("appB:reconciliation")
        with self.assertRaises(ModelError):
            attribution_signatures(data)

    def test_attribution_blocking_contrast(self):
        blocked = retirement(FIXTURE["retirement"])
        safe = retirement({**FIXTURE["retirement"], "attribution_block": 0})
        self.assertGreater(blocked["end_ACW_hours"], safe["end_ACW_hours"])

    def test_no_retire_or_no_cost_removes_blocking_effect(self):
        data = {**FIXTURE["retirement"], "safe_retirement_rate": 0}
        self.assertAlmostEqual(retirement(data)["end_ACW_hours"],
                               retirement({**data, "attribution_block": 0})["end_ACW_hours"])
        data = {**FIXTURE["retirement"], "assumed_ACW_hours_per_obligation": 0}
        self.assertEqual(retirement(data)["end_ACW_hours"], 0)

    def test_full_map_eliminates_unseen_and_backaction(self):
        data = {**FIXTURE["information"], "map_coverage": 1}
        arm = map_flow(data)
        verified = map_flow(data, verification=True)
        self.assertAlmostEqual(arm["end_ACW_hours"], verified["end_ACW_hours"])
        self.assertTrue(all(r["forecast_error_hours"] == 0 for r in arm["rows"]))

    def test_partial_map_backaction_vs_frozen_comparator(self):
        original = map_flow(FIXTURE["information"])
        frozen = map_flow(FIXTURE["information"], disable_feedback=True)
        self.assertGreater(original["end_ACW_hours"], frozen["end_ACW_hours"])
        self.assertTrue(any(d > 0 for d in original["ACW_second_difference"]))

    def test_no_backaction_no_causal_feedback_excess(self):
        data = {**FIXTURE["information"], "backaction_links_per_hidden_link": 0}
        self.assertEqual(map_flow(data)["end_ACW_hours"],
                         map_flow(data, disable_feedback=True)["end_ACW_hours"])

    def test_modularity_can_remove_curvature(self):
        data = {**FIXTURE["information"], "exogenous_new_links": [1]*10,
                "backaction_links_per_hidden_link": 0}
        self.assertTrue(all(abs(x) < 1e-9 for x in map_flow(data)["ACW_second_difference"]))

    def test_monetary_stock_flow_identity(self):
        rows = money_ledger(FIXTURE["money"])["rows"]
        for row in rows:
            self.assertAlmostEqual(row["opening"] + row["new"] +
                                   row["interest"] - row["extinguished"], row["closing"])
        self.assertGreater(rows[-1]["closing"],
                           money_ledger({**FIXTURE["money"], "explicit_capitalized_rate": 0})["closing_monetary_obligation"])

    def test_monetary_liability_is_not_hid(self):
        self.assertIsNone(money_ledger(FIXTURE["money"])["HID"])

    def test_negative_or_impossible_payment_rejected(self):
        with self.assertRaises(ModelError):
            money_ledger({"issued": [1], "extinguished": [2], "explicit_capitalized_rate": 0})
        with self.assertRaises(ModelError):
            retirement({**FIXTURE["retirement"], "attribution_block": 1.2})

    def test_suite_runs_all_arms(self):
        result = evaluate(FIXTURE)
        self.assertEqual(result["status"], "SYNTHETIC ONLY — HID2 campaigns NOT RUN")
        self.assertIn("IF_policy_comparator", result)
        self.assertIn("AG_retirement_comparator", result)
        self.assertIn("HID_direct_optimum_gap", result)


if __name__ == "__main__":
    unittest.main()
