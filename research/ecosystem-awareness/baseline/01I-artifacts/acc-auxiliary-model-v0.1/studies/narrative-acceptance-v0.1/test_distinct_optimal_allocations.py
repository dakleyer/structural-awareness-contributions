"""Distinct optimal allocations must not be multiplied by unused-mode subsets."""
from itertools import permutations
import unittest

from finite_feasible_gap import optimize, original_iq03_periods


def mode(name, rate=1):
    return {"id": name, "capacity": 10, "resource_per_service": rate,
            "eligibility": "PASS"}


class DistinctOptimalAllocationTests(unittest.TestCase):
    def test_same_optimum_from_unused_modes_is_reported_once(self):
        result = optimize(10, [mode("current"), mode("cheap", "1/2")],
                          {"current": 10})
        self.assertEqual(result["optimizers_with_ties"], [{"cheap": "10"}])
        self.assertEqual(result["minimum_resources_among_DECLARED_PASS_modes"], "5")
        self.assertEqual(result["gap_relative_to_declared_current"], "5")

    def test_genuinely_distinct_tied_allocations_are_all_retained(self):
        result = optimize(10, [mode("A"), mode("B")], {"A": 10})
        self.assertEqual(result["optimizers_with_ties"], [{"A": "10"}, {"B": "10"}])

    def test_order_of_modes_does_not_multiply_or_reorder_ties(self):
        modes = [mode("current", 2), mode("A"), mode("B")]
        for ordered in permutations(modes):
            with self.subTest(order=[row["id"] for row in ordered]):
                result = optimize(10, list(ordered), {"current": 10})
                self.assertEqual(result["optimizers_with_ties"],
                                 [{"A": "10"}, {"B": "10"}])

    def test_zero_service_has_one_empty_allocation(self):
        result = optimize(0, [mode("A"), mode("B")], {"A": 0})
        self.assertEqual(result["optimizers_with_ties"], [{}])
        self.assertEqual(result["minimum_resources_among_DECLARED_PASS_modes"], "0")

    def test_original_period_values_preserved_with_one_allocation_each(self):
        early, late = original_iq03_periods()
        for result, minimum, gap in ((early, "80", "20"), (late, "65", "45")):
            self.assertEqual(result["minimum_resources_among_DECLARED_PASS_modes"], minimum)
            self.assertEqual(result["gap_relative_to_declared_current"], gap)
            self.assertEqual(len(result["optimizers_with_ties"]), 1)


if __name__ == "__main__":
    unittest.main()

