"""Explicit positive premises for source-specific comparison reports."""
from copy import deepcopy
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import unittest

import campaign as source

HERE = Path(__file__).resolve().parent
CASES = json.loads((HERE / "CASES.json").read_text(encoding="utf-8"))["cases"]
UNESTABLISHED = (False, None, "UNKNOWN", "yes", "True", 1, 2, {}, {"claim": True}, [], [True])


def sample(kind):
    return deepcopy(next(c for c in CASES if c["kind"] == kind))


class ExplicitSourcePrerequisiteTests(unittest.TestCase):
    def test_authorization_needs_true_without_erasing_numeric_opportunity(self):
        base = next(deepcopy(c) for c in CASES if c["kind"] == "compare"
                    and source.result(c)["status"] == "WEAK_PARETO_RESOURCE_SERVICE_GAIN")
        supported = source.result(base)
        for value in UNESTABLISHED:
            case = deepcopy(base)
            case["alternative"]["authorized"] = value
            original = deepcopy(case)
            with self.subTest(value=repr(value)):
                result = source.result(case)
                self.assertEqual(result["status"], "RIGHTS_BLOCKED")
                self.assertEqual(result["authorized"], value)
                for key in ("delta_service", "delta_resources", "coordination_margin"):
                    self.assertEqual(result[key], supported[key])
                self.assertEqual(case, original)

    def test_unestablished_feasibility_keeps_unknown_gap_and_known_observations(self):
        base = sample("eff_gap")
        supported = source.result(base)
        for value in UNESTABLISHED:
            case = deepcopy(base)
            case["periods"][0]["feasible"] = value
            original = deepcopy(case)
            with self.subTest(value=repr(value)):
                result = source.result(case)
                self.assertEqual(result["status"], "OPTIMUM_NOT_ESTABLISHED")
                self.assertIsNone(result["periods"][0]["gap"])
                self.assertEqual(result["periods"][0]["certified_feasible"], value)
                for key in ("time", "output"):
                    self.assertEqual(result["periods"][0][key], supported["periods"][0][key])
                self.assertEqual(result["periods"][1], supported["periods"][1])
                self.assertFalse(result["gap_increases"])
                self.assertEqual(case, original)

    def test_global_gap_status_needs_nonempty_computed_support(self):
        case = sample("eff_gap")
        case["periods"] = []
        result = source.result(case)
        self.assertEqual(result["status"], "OPTIMUM_NOT_ESTABLISHED")
        self.assertEqual(result["periods"], [])
        case = sample("eff_gap")
        case["periods"][0]["ideal_same_output_cost"] = case["periods"][0]["actual_cost"] + 1
        result = source.result(case)
        self.assertIsNone(result["periods"][0]["gap"])
        self.assertIs(result["periods"][0]["certified_feasible"], True)
        self.assertEqual(result["status"], "OPTIMUM_NOT_ESTABLISHED")

    def test_measured_zero_gap_is_known_rather_than_unknown(self):
        case = sample("eff_gap")
        for period in case["periods"]:
            period["ideal_same_output_cost"] = period["actual_cost"]
            period["feasible"] = True
        result = source.result(case)
        self.assertEqual(result["status"], "GAPS_ESTABLISHED_IN_TOY")
        self.assertTrue(all(p["gap"] == 0 and p["gap"] is not None for p in result["periods"]))

    def test_unestablished_same_service_does_not_certify_a_matched_comparison(self):
        base = next(deepcopy(c) for c in CASES if c["kind"] == "human_time"
                    and c["same_service"] is True)
        for value in UNESTABLISHED:
            case = deepcopy(base)
            case["same_service"] = value
            original = deepcopy(case)
            with self.subTest(value=repr(value)):
                result = source.result(case)
                self.assertEqual(result["status"], "MATCHED_REFERENCE_MISSING")
                self.assertNotIn("GIC_delta", result)
                self.assertNotIn("ACW_delta", result)
                self.assertEqual(case, original)

    def test_all_original_boolean_control_variants_keep_complete_results(self):
        reports = []
        for case in CASES:
            if case["kind"] not in ("compare", "eff_gap", "human_time"):
                continue
            count = len(case["periods"]) if case["kind"] == "eff_gap" else 1
            for flags in product((False, True), repeat=count):
                item = deepcopy(case)
                if item["kind"] == "compare":
                    item["alternative"]["authorized"] = flags[0]
                elif item["kind"] == "human_time":
                    item["same_service"] = flags[0]
                else:
                    for period, flag in zip(item["periods"], flags):
                        period["feasible"] = flag
                reports.append({"id": item["id"], "flags": flags, "result": source.result(item)})
        self.assertEqual(len(reports), 28)
        digest = sha256(json.dumps(reports, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        # Full result dictionaries from unmodified parent #99 a5a2621.
        self.assertEqual(digest, "3299b3365ac8086731c35b7db49b132950af1e87b8c78cd8e7ffe2bfba7b95df")


if __name__ == "__main__":
    unittest.main()
