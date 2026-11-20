"""Finite, exact measurements are required before publishing a Pareto front."""
from copy import deepcopy
from decimal import Decimal
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import unittest

from l08_robustness import CLASSIFICATIONS, pareto, run, two_arm_order, validate

HERE = Path(__file__).resolve().parent


class ParetoNumericContractTests(unittest.TestCase):
    def test_invalid_counts_cannot_be_published_as_known_comparisons(self):
        fields = ("invalid_proposals", "missed_valid_opportunities")
        for invalid in (None, "UNKNOWN", True, False, float("nan"),
                        float("inf"), -float("inf"), Decimal("NaN"),
                        Decimal("Infinity"), -1, "-1/2"):
            for field in fields:
                for arm in (0, 1):
                    counts = [dict.fromkeys(fields, 0), dict.fromkeys(fields, 0)]
                    counts[arm][field] = invalid
                    with self.subTest(value=repr(invalid), field=field, arm=arm):
                        with self.assertRaises(ValueError):
                            two_arm_order(*counts)

    def test_numeric_count_strings_are_compared_by_exact_value(self):
        self.assertEqual(two_arm_order(
            {"invalid_proposals": "10", "missed_valid_opportunities": "0"},
            {"invalid_proposals": "2", "missed_valid_opportunities": "0"}),
            CLASSIFICATIONS[1])

    def test_exact_count_ties_and_tradeoffs_preserve_inputs(self):
        first = {"invalid_proposals": Fraction(1, 10),
                 "missed_valid_opportunities": "1/3"}
        second = {"invalid_proposals": Decimal("0.1"),
                  "missed_valid_opportunities": Fraction(1, 3)}
        original = deepcopy((first, second))
        self.assertEqual(two_arm_order(first, second), CLASSIFICATIONS[2])
        self.assertEqual((first, second), original)
        self.assertEqual(two_arm_order(
            {"invalid_proposals": "1/10", "missed_valid_opportunities": "2"},
            {"invalid_proposals": Decimal("0.2"), "missed_valid_opportunities": 1}),
            CLASSIFICATIONS[3])

    def test_equivalent_probability_encodings_are_not_distinct_grid_points(self):
        original = json.loads((HERE / "L08_PROTOCOL.json").read_text(encoding="utf-8"))
        for grid in (("0", "0/1", "1"), ("0", "1/2", "0.50", "1"),
                     ("0", "1", "1.0")):
            manifest = deepcopy(original)
            manifest["accuracy_grid"] = list(grid)
            with self.subTest(grid=grid), self.assertRaisesRegex(ValueError, "duplicate grid"):
                validate(manifest)

    def test_close_but_distinct_rational_grid_points_are_preserved(self):
        manifest = json.loads((HERE / "L08_PROTOCOL.json").read_text(encoding="utf-8"))
        manifest["accuracy_grid"] = ["0", "1/3", "0.3333333333333333333333333334", "1"]
        original = deepcopy(manifest)
        validate(manifest)
        self.assertEqual(manifest, original)

    def test_nonfinite_unknown_and_boolean_axes_cannot_enter_a_front(self):
        for invalid in (None, "UNKNOWN", True, False, float("nan"),
                        float("inf"), -float("inf"), Decimal("NaN"),
                        Decimal("Infinity")):
            with self.subTest(value=repr(invalid)), self.assertRaises(ValueError):
                pareto({"known": (0, 0), "invalid": (invalid, 0)},
                       axes=("errors", "cost"))

    def test_exact_numeric_encodings_use_numeric_not_lexicographic_order(self):
        self.assertEqual(pareto({"ten": ("10",), "two": ("2",)}, axes=("cost",)),
                         ["two"])
        self.assertEqual(pareto({
            "rational": (Fraction(1, 10),), "decimal": (Decimal("0.1"),),
            "text": ("1/10",)}, axes=("cost",)),
            ["decimal", "rational", "text"])

    def test_valid_signed_tradeoffs_and_ties_are_preserved_without_mutation(self):
        points = {"more_output": (-12, 1), "lower_cost": (-10, 0),
                  "same_as_more": (Fraction(-12), Fraction(1)), "worse": (-9, 2)}
        original = deepcopy(points)
        self.assertEqual(pareto(points, axes=("negative_output", "cost")),
                         ["lower_cost", "more_output", "same_as_more"])
        self.assertEqual(points, original)

    def test_entire_original_source_grid_results_are_preserved(self):
        manifest = json.loads((HERE / "L08_PROTOCOL.json").read_text(encoding="utf-8"))
        report = run(manifest)
        self.assertEqual(report["total_paired_cell_evaluations"], 18816)
        # Digest from the unmodified #72 parent 0d2d77d. Exclude only source
        # byte hashes, whose line endings can differ between checkout platforms.
        report.pop("source_engine_sha256")
        digest = sha256(json.dumps(report, sort_keys=True,
                                  separators=(",", ":")).encode()).hexdigest()
        self.assertEqual(digest,
                         "72cba2b2cac029bef43ace72476053bdbc23ed2e3f1dd87bbe69348ddce8db70")


if __name__ == "__main__":
    unittest.main()

