"""Finite, exact measurements are required before publishing a Pareto front."""
from copy import deepcopy
from decimal import Decimal
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import unittest

from l08_robustness import pareto, run

HERE = Path(__file__).resolve().parent


class ParetoNumericContractTests(unittest.TestCase):
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

