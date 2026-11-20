"""Adversarial and source-integration tests for the unit-safe #66 report."""
from copy import deepcopy
from decimal import Decimal
from fractions import Fraction
import json
from pathlib import Path
import unittest

import economic_envelope_runner as legacy
from unit_safe_envelope import project_case, project_report, run

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[6]


def case(output="10", price="0"):
    return {
        "frame": {"case_id": "x", "model": "external", "scope": "s", "question": "q",
                  "output_unit": "items", "cost_unit": "currency", "horizon": "t",
                  "public_contract_id": "contract", "baseline_a": "10",
                  "metric": "INVALID_LEGACY_NET_METRIC"},
        "baseline_arm": "A_ONLY",
        "arms": [
            {"arm": "A_ONLY", "gross": "10", "cost": "0", "components": {},
             "status": "KEEP", "source": "source"},
            {"arm": "B", "gross": output, "cost": price,
             "components": {} if price is None else {"acquisition": price},
             "status": "CONSENT_UNKNOWN", "source": "source"}],
        "leaders": ["WRONG_LEGACY_WINNER"],
    }


class UnitSafeContract(unittest.TestCase):
    def test_exact_cost_types_are_serializable_without_input_mutation(self):
        source = case("12", "13/30")
        source["arms"][1]["components"] = {
            "acquisition": Fraction(1, 3), "maintenance": Decimal("0.1")}
        original = deepcopy(source)
        result = project_case(source)
        encoded = json.loads(json.dumps(result))
        self.assertEqual(encoded["observations"][1]["cost_components"],
                         {"acquisition": "1/3", "maintenance": "1/10"})
        self.assertEqual(encoded["observations"][1]["information_cost"], "13/30")
        self.assertEqual(source, original)

    def test_output_improves_price_worsens_is_tradeoff(self):
        result = project_case(case("12", "1"))
        self.assertEqual(result["measurement_frontier"], ["A_ONLY", "B"])
        self.assertEqual(result["economic_winner"], "NOT_INFERRED")
        self.assertEqual(result["observations"][1]["source_status"], "CONSENT_UNKNOWN")
        self.assertNotIn("leaders", result)
        self.assertNotIn("net", json.dumps(result))

    def test_same_unit_does_not_authorize_dimension_compensation(self):
        source = case("12", "1")
        source["frame"]["cost_unit"] = "items"
        self.assertEqual(project_case(source)["measurement_frontier"], ["A_ONLY", "B"])

    def test_known_dominance_and_ties(self):
        self.assertEqual(project_case(case("12", "0"))["measurement_frontier"], ["B"])
        self.assertEqual(project_case(case("10", "0"))["measurement_frontier"], ["A_ONLY", "B"])
        self.assertEqual(project_case(case("9", "1"))["measurement_frontier"], ["A_ONLY"])

    def test_matched_output_cost_claim_needs_no_scalar_conversion(self):
        source = case("10", "1")
        match = project_case(source)["matched_output_cost_order"][0]
        self.assertEqual(match["lower_information_cost_arm"], "A_ONLY")
        self.assertEqual(match["cost_difference_left_minus_right"], "-1")
        self.assertEqual(project_case(case("12", "1"))["matched_output_cost_order"], [])

    def test_unknown_measurements_stay_unknown(self):
        for field in ("gross", "cost"):
            source = case("12", "1")
            source["arms"][1][field] = None
            result = project_case(source)
            self.assertEqual(result["status"], "UNKNOWN_MEASUREMENTS")
            self.assertEqual(result["unknown_measurement_arms"], ["B"])
            self.assertEqual(result["full_open_K_dominance"], "NOT_ESTABLISHED")

    def test_invalid_measurements_fail_closed(self):
        for value in (True, "NaN", "Infinity", "1/0", [], {}):
            source = case()
            source["arms"][1]["gross"] = value
            with self.subTest(value=value), self.assertRaises(ValueError):
                project_case(source)
        for value in ("-1", True, "NaN"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                project_case(case("12", value))

    def test_cost_reconciliation_and_duplicate_arms(self):
        source = case("12", "1")
        source["arms"][1]["components"]["acquisition"] = "2"
        with self.assertRaises(ValueError):
            project_case(source)
        source = case()
        source["arms"][1]["arm"] = "A_ONLY"
        with self.assertRaises(ValueError):
            project_case(source)

    def test_source_receiver_is_diagnostic_only(self):
        source = case("12", "0")
        receiver = deepcopy(source["arms"][1])
        receiver["arm"] = "SOURCE_PUBLIC_RECEIVER"
        source["arms"].append(receiver)
        result = project_case(source)
        self.assertEqual(result["measurement_frontier"], ["B"])
        self.assertEqual(len(result["source_receiver_diagnostics"]), 1)

    def test_legacy_scalars_cannot_affect_projection(self):
        source = case("12", "1")
        expected = project_case(source)
        for arm in source["arms"]:
            arm["net"] = "999999999999"
            arm["net_delta_vs_baseline"] = "NaN"
        source["leaders"] = ["B"]
        self.assertEqual(project_case(source), expected)

    def test_no_detail_or_duplicate_cases_rejected(self):
        with self.assertRaises(ValueError):
            project_report({"summary": {}})
        with self.assertRaises(ValueError):
            project_report({"cases": [case(), case()]})

    def test_K01_cost_claims_hold_at_equal_realized_output(self):
        manifest = json.loads((HERE / "ECONOMIC_SWEEP_MANIFEST.json").read_text())
        manifest["social"].update({
            "sizes": [16, 128, 256], "roots": [{"id": "free", "slack": None}],
            "accesses": ["full"], "prices": [{"id": "original", "costs": {}}]})
        rows = run(manifest, ROOT, model="social")["cases"]
        claims = []
        for row in rows:
            pair = next(pair for pair in row["matched_output_cost_order"]
                        if pair["arms"] == ["B_QUALIFIED", "TARGETED_EXPLORATION_OF_A"])
            self.assertEqual(pair["matched_output"], "10")
            claims.append(pair["lower_information_cost_arm"])
        self.assertEqual(claims, ["B_QUALIFIED", "TIE", "TARGETED_EXPLORATION_OF_A"])

    def test_full_manifest_both_original_engines_without_source_mutation(self):
        manifest = json.loads((HERE / "ECONOMIC_SWEEP_MANIFEST.json").read_text())
        original = legacy.execute(manifest, ROOT, model="both", details=True)
        corrected = run(manifest, ROOT)
        self.assertEqual(legacy.execute(manifest, ROOT, model="both", details=True), original)
        self.assertEqual(corrected["groups"]["ACC_SOCIAL_INTRINSIC_44"]["cases"], 168)
        self.assertGreaterEqual(corrected["groups"]["ACC_AGENTIC_REDUCTION_57"]["cases"], 90)
        self.assertEqual(len(corrected["cases"]), len(original["cases"]))
        for old, new in zip(original["cases"], corrected["cases"]):
            expected = [arm for arm in old["arms"] if arm["arm"] != "SOURCE_PUBLIC_RECEIVER"]
            self.assertEqual([arm["gross"] for arm in expected],
                             [arm["output"] for arm in new["observations"]])
            self.assertEqual([arm["cost"] for arm in expected],
                             [arm["information_cost"] for arm in new["observations"]])
            self.assertNotIn("leaders", new)
            self.assertEqual(new["full_open_K_dominance"], "NOT_ESTABLISHED")


if __name__ == "__main__":
    unittest.main()

