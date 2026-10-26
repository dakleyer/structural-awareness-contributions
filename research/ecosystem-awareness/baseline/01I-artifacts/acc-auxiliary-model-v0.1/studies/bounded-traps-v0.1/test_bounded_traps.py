"""Deterministic negative and positive controls for an ACC finite research toy."""
import unittest

from bounded_traps import (
    Constraint, apple_utility, coupled_trap, dominates, feasible_states,
    market_jump, relative_gap, reachable_by_unilateral_additions,
    saturation_with_redesign, saturation_without_redesign,
)


class StructuralControls(unittest.TestCase):
    def test_coupled_joint_pareto_target(self):
        r = coupled_trap()
        self.assertTrue(r["pareto_dominates"])
        self.assertTrue(r["reachable_with_joint_transition"])

    def test_unilateral_actions_trapped(self):
        self.assertFalse(coupled_trap()["reachable_without_joint_transition"])

    def test_linear_feasible_set_has_only_two_states(self):
        self.assertEqual(coupled_trap()["feasible"], [[0, 0], [1, 1]])

    def test_saturation_really_infeasible(self):
        self.assertFalse(saturation_without_redesign()["project_feasible"])

    def test_redesign_release_changes_finite_feasible_set(self):
        self.assertTrue(saturation_with_redesign()["joint_project_feasible"])

    def test_no_same_dimensional_mismatch(self):
        with self.assertRaises(ValueError):
            feasible_states(2, [Constraint((1,), 0)])

    def test_unfeasible_start_must_not_be_interpreted_as_reachable(self):
        with self.assertRaises(ValueError):
            reachable_by_unilateral_additions((1, 1), {(0, 0)})

    def test_pareto_noncomparable(self):
        self.assertFalse(dominates((4, 4), (3, 8)))
        self.assertFalse(dominates((3, 8), (4, 4)))

    def test_no_invented_joint_optimum_from_coordinatewise_maxima(self):
        self.assertFalse(dominates((4, 4), (4, 4)))


class NonmonotoneUtilityControls(unittest.TestCase):
    def test_local_peak(self):
        self.assertGreater(apple_utility(3), apple_utility(4))

    def test_later_market_threshold_rebounds(self):
        self.assertGreater(apple_utility(7), apple_utility(3))

    def test_monotone_only_policy_locally_trapped(self):
        r = market_jump()
        self.assertEqual(r["local_non_loss_reachable"], [3])
        self.assertEqual(r["best_global_quantity"], 8)
        self.assertFalse(r["direct_jump_assumed_available"])

    def test_uncharacterized_quantity_is_not_extrapolated(self):
        for bad in (-1, 9, 1.2, True):
            with self.subTest(q=bad), self.assertRaises(ValueError):
                apple_utility(bad)


class GrowthSensitivityControls(unittest.TestCase):
    def test_dense_quadratic_gap_and_positive_second_difference(self):
        r = [relative_gap(n, 10, 0.2) for n in (5, 6, 7)]
        ds = [x["gap_to_assumed_joint_optimum"] for x in r]
        self.assertAlmostEqual(ds[2] - 2*ds[1] + ds[0], 0.2)

    def test_dense_gap_ratio_to_production_increases_conditionally(self):
        s = [relative_gap(n, 10, 0.2)["gap_over_actual"] for n in (5, 10, 20, 40)]
        self.assertTrue(all(y > x for x, y in zip(s, s[1:])))
        self.assertAlmostEqual(s[-1], 0.39)

    def test_star_not_quadratic(self):
        r = [relative_gap(n, 10, 0.2, topology="star") for n in (5, 6, 7)]
        ds = [x["gap_to_assumed_joint_optimum"] for x in r]
        self.assertAlmostEqual(ds[2] - 2*ds[1] + ds[0], 0)

    def test_positive_realized_pair_synergy_changes_relative_asymptotics(self):
        b, g, alpha = 10, 0.2, 0.5
        self.assertLess(relative_gap(500000, b, g, alpha)["gap_over_actual"], g/alpha)
        self.assertGreater(relative_gap(500000, b, g, alpha)["gap_over_actual"], 0.39)

    def test_no_unrealized_gain_means_no_gap(self):
        self.assertEqual(relative_gap(50, 10, 0)["gap_over_actual"], 0)

    def test_gap_over_joint_optimum_bounded_below_one(self):
        for n in (1, 5, 50, 100):
            x = relative_gap(n, 10, 0.2)
            self.assertGreaterEqual(x["gap_over_joint_optimum"], 0)
            self.assertLess(x["gap_over_joint_optimum"], 1)

    def test_no_d_automatically_estimated(self):
        self.assertIn("NOT_VERIFIED", relative_gap(50, 10, 0.2)["status"])

    def test_unsupported_topology_rejected(self):
        with self.assertRaises(ValueError):
            relative_gap(10, 10, 0.2, topology="unknown")


if __name__ == "__main__":
    unittest.main()
