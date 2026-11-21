"""Canonical joint-feasibility and exact-threshold controls for local closure."""
from copy import deepcopy
from fractions import Fraction
from itertools import product
import json
from pathlib import Path
import unittest

import campaign as source

CASES = json.loads(Path(__file__).with_name("CASES.json").read_text(encoding="utf-8"))["cases"]


def case(**changes):
    item = deepcopy(next(c for c in CASES if c["kind"] == "closure" and c["L"] is not None))
    item.update(changes)
    return item


class JointExactClosureTests(unittest.TestCase):
    def test_conflicting_samples_at_one_position_are_not_local_proof(self):
        item = case(L=1, x=1, threshold=1, samples=[[0, 0, 0], [0, 2, 2]])
        original = deepcopy(item)
        result = source.result(item)
        self.assertEqual(result["status"], "INCONSISTENT_ASSUMPTIONS")
        self.assertEqual(result["bounds"], [1, 1])
        self.assertIs(result["global_D_open"], True)
        self.assertEqual(item, original)

    def test_reversed_sample_interval_cannot_be_repaired_by_distance(self):
        result = source.result(case(L=1, x=1, threshold=1, samples=[[0, 2, 0]]))
        self.assertEqual(result["status"], "INCONSISTENT_ASSUMPTIONS")
        self.assertEqual(result["bounds"], [1, 1])

    def test_sub_ulp_joint_contradiction_is_not_erased(self):
        eps = 2**-54
        result = source.result(case(L=1, x=0, threshold=1,
                                    samples=[[0, 1, 1], [1, -eps, -eps]]))
        self.assertEqual(result["status"], "INCONSISTENT_ASSUMPTIONS")

    def test_rounded_lower_bound_cannot_cross_the_exact_threshold(self):
        eps = 2**-54
        result = source.result(case(L=eps, x=1, threshold=1, samples=[[0, 1, 1]]))
        self.assertEqual(result["status"], "PREDICATE_UNDETERMINED")
        lo, hi = map(Fraction, result["bounds"])
        self.assertLessEqual(lo, Fraction(1) - Fraction(eps))
        self.assertGreaterEqual(hi, Fraction(1) + Fraction(eps))

    def test_exact_upper_bound_can_refute_despite_wider_display_float(self):
        eps = 2**-54
        value = 1 - 2**-53
        result = source.result(case(L=eps, x=1, threshold=1, samples=[[0, value, value]]))
        self.assertEqual(result["status"], "PREDICATE_REFUTED_IN_FRAME")
        self.assertGreaterEqual(Fraction(result["bounds"][1]), Fraction(value) + Fraction(eps))
        self.assertIs(result["global_D_open"], True)

    def test_raw_integer_coordinate_is_not_rounded_before_distance(self):
        pos = 2**53
        result = source.result(case(L=1, x=pos + 1, threshold=0,
                                    samples=[[pos, 0, 0]]))
        self.assertEqual(result["status"], "PREDICATE_UNDETERMINED")
        self.assertEqual(result["bounds"], [-1, 1])

    def test_underflow_does_not_turn_positive_uncertainty_into_zero(self):
        tiny = 2**-1074
        result = source.result(case(L=tiny, x=tiny, threshold=0, samples=[[0, 0, 0]]))
        self.assertEqual(result["status"], "PREDICATE_UNDETERMINED")
        self.assertLess(result["bounds"][0], 0)
        self.assertGreater(result["bounds"][1], 0)

    def test_small_integer_world_enumeration_matches_all_three_verdicts(self):
        intervals = [(lo, hi) for lo in range(4) for hi in range(lo, 4)]
        checked = 0
        for (lo0, hi0), (lo2, hi2) in product(intervals, repeat=2):
            # Complete finite control for three positions 0,1,2, L=1.
            # Integer endpoints make the feasible query extrema integer here.
            feasible = [middle for left in range(lo0, hi0 + 1)
                        for right in range(lo2, hi2 + 1) for middle in range(-1, 5)
                        if abs(left - middle) <= 1 and abs(right - middle) <= 1]
            for threshold in range(-1, 6):
                result = source.result(case(L=1, x=1, threshold=threshold,
                                            samples=[[0, lo0, hi0], [2, lo2, hi2]]))
                if not feasible:
                    expected = "INCONSISTENT_ASSUMPTIONS"
                elif all(value >= threshold for value in feasible):
                    expected = "PREDICATE_SUPPORTED_IN_FRAME"
                elif all(value < threshold for value in feasible):
                    expected = "PREDICATE_REFUTED_IN_FRAME"
                else:
                    expected = "PREDICATE_UNDETERMINED"
                self.assertEqual(result["status"], expected,
                                 ((lo0, hi0), (lo2, hi2), threshold))
                if feasible:
                    self.assertEqual(result["bounds"], [min(feasible), max(feasible)])
                self.assertIs(result["global_D_open"], True)
                checked += 1
        self.assertEqual(checked, 700)


if __name__ == "__main__":
    unittest.main()
