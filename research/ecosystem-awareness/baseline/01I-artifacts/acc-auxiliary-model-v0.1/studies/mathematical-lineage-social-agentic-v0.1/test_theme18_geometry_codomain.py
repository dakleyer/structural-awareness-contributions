"""L-01 regression: preserve valid geometry gains, reject impossible evidence."""
from decimal import Decimal
from fractions import Fraction
import unittest

from qualified_gain import ValueInterval, compare_gain
from test_theme18_candidate_admission import assess_candidate, reports


def candidate(bound):
    return assess_candidate(
        reports(), received_after_exchange=True,
        source_to_value_link_qualified=True, source_value_lower_bound=bound,
        action_authorized=True, decision_budget_ok=True)


class GeometryCodomainRegression(unittest.TestCase):
    def test_finite_lower_bound_above_attainable_maximum_is_not_evidence(self):
        for bound in (1.5, 10**21, 1e308, Fraction(1001, 1000),
                      Decimal("1.0000000000000000000000000001")):
            with self.subTest(bound=bound):
                result = candidate(bound)
                self.assertEqual(result["candidate_status"], "UTILITY_NOT_ESTABLISHED")
                self.assertEqual(result["execution"], "NEVER")

    def test_all_valid_hundredth_bounds_preserve_the_original_sign(self):
        for numerator in range(101):
            bound = Fraction(numerator, 100)
            with self.subTest(bound=bound):
                expected = ("SCOPED_PROPOSAL_FOR_EXTERNAL_ACTION_CHECK"
                            if bound > Fraction(3, 4)
                            else "NO_CERTIFIED_STRICT_VALUE_GAIN")
                self.assertEqual(candidate(bound)["candidate_status"], expected)

    def test_loose_conservative_lower_bound_is_not_an_impossible_score_claim(self):
        # A lower bound below the minimum remains conservative, not a
        # contradiction. Preserve its original no-strict-gain classification.
        self.assertEqual(candidate(Fraction(-1, 10))["candidate_status"],
                         "NO_CERTIFIED_STRICT_VALUE_GAIN")

    def test_other_metrics_do_not_inherit_the_geometry_range(self):
        baseline = ValueInterval(
            "throughput", "items", "production", "OBSERVED", "baseline",
            100, 100, verification="SUPPORTED")
        proposed = ValueInterval(
            "throughput", "items", "production", "PROPOSED_BOUND", "source",
            lower=120, verification="SUPPORTED")
        self.assertEqual(compare_gain(baseline, proposed).status,
                         "CERTIFIED_STRICT_GAIN")


if __name__ == "__main__":
    unittest.main()

