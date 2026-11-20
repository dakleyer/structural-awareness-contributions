"""Source-anchored evidence controls; no changes to native #57 experiments."""
from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import unittest

import agentic_reduction as source
from unit_safe_evidence import control_status, project_run, report
import sensitivity

HERE = Path(__file__).resolve().parent
CASES = json.loads((HERE / "CASES.json").read_text())["cases"]


class UnitSafeAgenticEvidence(unittest.TestCase):
    def test_original_30_cases_are_replayed_without_mutation(self):
        before = deepcopy(CASES)
        result = report()
        self.assertEqual(CASES, before)
        self.assertEqual((result["case_count"], result["sweep_count"]), (30, 160))
        for case, projected in zip(CASES, result["cases"]):
            native = source.run_case(case)
            for observation in projected["observations"]:
                arm = native["arms"][observation["arm"]]
                self.assertEqual(Fraction(observation["output"]),
                                 Fraction(str(arm["observed_by_referee_only"]["output"])))
                self.assertEqual(Fraction(observation["information_cost"]),
                                 Fraction(str(arm["plan"]["instrument_cost"])))
                self.assertEqual(observation["source_status"], arm["plan"]["status"])
            self.assertFalse(projected["action_authorized_by_this_report"])

    def test_original_160_cell_parameter_grid_is_exact(self):
        original = sensitivity.run_sweep()["scenarios"]
        projected = report()["sweep"]
        self.assertEqual([r["id"] for r in original],
                         [r["frame"]["case_id"] for r in projected])
        for old, new in zip(original, projected):
            for arm, key in (("Q_META_PROTOCOL", "Q_improvement_physical"),
                             ("CONVENTIONAL_DIRECTED", "peer_improvement_physical")):
                self.assertEqual(Fraction(new["physical_output_gain_vs_baseline"][arm]) > 0,
                                 old[key])

    def test_information_and_physical_gain_remain_visible(self):
        native = source.run_case(CASES[0])
        projected = project_run(native)
        self.assertEqual(projected["physical_output_gain_vs_baseline"]["Q_META_PROTOCOL"], "3/2")
        signal = projected["source_awareness_signals"]["Q_REVIEW_ONLY"]
        self.assertGreater(signal["conditional_near_gain"], 0)
        self.assertEqual(projected["physical_output_gain_vs_baseline"]["Q_REVIEW_ONLY"], "0")
        self.assertEqual(projected["dimension_mapping"] if "dimension_mapping" in projected
                         else projected["ACC_dimension_assignment"],
                         "NOT_INFERRED_FROM_INSTRUMENT_METRICS")

    def test_source_controls_are_separate_and_unknown_is_not_pass(self):
        self.assertEqual(control_status(None), "UNKNOWN")
        self.assertEqual(control_status(False), "FAIL")
        self.assertEqual(control_status(True), "PASS")
        for value in (0, 1, "PASS", "UNKNOWN"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                control_status(value)
        native = source.run_case(CASES[0])
        native["public_A"]["release_consent"] = None
        projected = project_run(native)
        self.assertEqual(projected["source_controls"]["governance"]["release_consent"], "UNKNOWN")
        self.assertFalse(projected["action_authorized_by_this_report"])

    def test_no_cross_unit_net_or_total_winner_is_exported(self):
        for case in report()["cases"]:
            self.assertNotIn("leaders", case)
            self.assertNotIn("net", case)
            self.assertEqual(case["economic_winner"], "NOT_INFERRED")
            self.assertEqual(case["full_open_K_dominance"], "NOT_ESTABLISHED")

    def test_resource_overhead_is_preserved_and_never_charged_as_information(self):
        for case in report()["cases"]:
            for observation in case["observations"]:
                resource = case["physical_resource_accounting"][observation["arm"]]
                conserved = (resource["donor_resources_after"] +
                             resource["recipient_resources_after"] +
                             resource["coordination_resources_spent"])
                self.assertAlmostEqual(conserved, resource["total_resources_same"], places=4)
                self.assertEqual(set(observation["cost_components"]), {"source_instrument_price"})

    def test_false_Q_and_blocked_source_results_remain_evidence(self):
        projected = report()["cases"]
        self.assertTrue(any(not signal["source_claim_supported_by_posthoc_truth"]
                            for case in projected for signal in case["source_awareness_signals"].values()))
        self.assertTrue(any(case["source_controls"]["governance"]["release_consent"] == "FAIL"
                            for case in projected))


if __name__ == "__main__":
    unittest.main()

