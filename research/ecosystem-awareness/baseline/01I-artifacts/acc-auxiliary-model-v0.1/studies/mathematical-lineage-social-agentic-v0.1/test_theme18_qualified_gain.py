"""Cross-model and third-party contract checks for the reusable interval core."""
from __future__ import annotations

from decimal import Decimal
from fractions import Fraction
from pathlib import Path
import math
import sys
import unittest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "nested-composition-suffering-v0.1"))
from nested_model import ProducerWorld, current_handoff, full_state_joint_capacity

from qualified_gain import ValueInterval, compare_gain
from qualified_gain_adapters import (
    agentic_arm_gains, geometry_score_bounds, social_joint_capacity_gain,
)

# Referee-observed fields from executing PR57 run_case(CASES.json:AG01),
# SHA a98940490e8a84051ad314f2392c15338dbf1de9. Not a copy of the model.
# The adapter consumes real PR57 result dictionaries unchanged when available.
AG01_RUN_SHAPE = {
    "id": "AG01-QUALIFIED-NEAR-OPTIMUM",
    "public_A": {"scope": "vendor-ecosystem-v1"},
    "arms": {
        "A_ONLY": {
            "plan": {"conditional_near_gain": None},
            "observed_by_referee_only": {"output": 10.0},
        },
        "Q_REVIEW_ONLY": {
            "plan": {"conditional_near_gain": 0.8},
            "observed_by_referee_only": {"output": 10.0},
            "source_B_claim_supported_by_lab_truth": True,
        },
        "Q_META_PROTOCOL": {
            "plan": {"conditional_near_gain": 0.8},
            "observed_by_referee_only": {"output": 11.5},
            "source_B_claim_supported_by_lab_truth": True,
        },
        "CONVENTIONAL_EQUIVALENT_Q": {
            "plan": {"conditional_near_gain": 0.8},
            "observed_by_referee_only": {"output": 11.5},
        },
    },
}


class QualifiedGainCoreChecks(unittest.TestCase):
    def snapshot(self, lower=None, upper=None, *, metric="throughput",
                 unit="items", scope="line-1", kind="OBSERVED", evidence="e1",
                 verification="SUPPORTED"):
        return ValueInterval(metric, unit, scope, kind, evidence, lower, upper,
                             verification=verification)

    def test_exact_sign_from_mixed_numeric_inputs(self):
        result = compare_gain(self.snapshot(8, 8), self.snapshot(Decimal("10"), Fraction(10)))
        self.assertEqual(result.status, "CERTIFIED_STRICT_GAIN")
        self.assertEqual((result.gain_lower, result.gain_upper), (2, 2))
        self.assertEqual(result.as_dict()["gain_lower"], "2")

    def test_partial_open_bounds_certify_only_when_separated(self):
        self.assertEqual(
            compare_gain(self.snapshot(10, 10), self.snapshot(lower=Decimal("10.8"))).gain_lower,
            Fraction(4, 5),
        )
        self.assertEqual(
            compare_gain(self.snapshot(10, 10), self.snapshot(lower=10)).status,
            "GAIN_NOT_ESTABLISHED",
        )
        self.assertEqual(
            compare_gain(self.snapshot(10, 10), self.snapshot(upper=9)).status,
            "CERTIFIED_NO_STRICT_GAIN",
        )

    def test_overlap_remains_unresolved(self):
        result = compare_gain(self.snapshot(8, 10), self.snapshot(9, 12))
        self.assertEqual(result.status, "GAIN_NOT_ESTABLISHED")
        self.assertEqual((result.gain_lower, result.gain_upper), (-1, 4))

    def test_scope_metric_and_unit_are_all_part_of_type(self):
        baseline = self.snapshot(8, 8)
        for field, value in (("metric", "energy"), ("unit", "kWh"), ("scope", "line-2")):
            with self.subTest(field=field), self.assertRaisesRegex(ValueError, "incommensurable"):
                compare_gain(baseline, self.snapshot(10, 10, **{field: value}))

    def test_invalid_or_empty_bounds_are_rejected(self):
        for bad in (True, False, float("nan"), float("inf"), -float("inf"),
                    Decimal("NaN"), Decimal("Infinity"), "10", object()):
            with self.subTest(bad=repr(bad)), self.assertRaises(ValueError):
                self.snapshot(lower=bad)
        with self.assertRaisesRegex(ValueError, "empty interval"):
            self.snapshot(11, 10)
        with self.assertRaisesRegex(ValueError, "at least one"):
            self.snapshot()
        with self.assertRaises(ValueError):
            self.snapshot(1, 1, evidence="")

    def test_unverified_and_refuted_bounds_cannot_be_certified(self):
        for verification, expected in (("UNVERIFIED", "UNVERIFIED_EVIDENCE"),
                                       ("REFUTED", "REFUTED_EVIDENCE")):
            with self.subTest(verification=verification):
                result = compare_gain(
                    self.snapshot(10, 10),
                    self.snapshot(lower=12, verification=verification))
                self.assertEqual(result.gain_lower, 2)
                self.assertEqual(result.status, expected)

    def test_third_party_metric_needs_no_acc_import(self):
        a = self.snapshot(Decimal("100.0"), Decimal("100.0"),
                          metric="energy_produced", unit="MWh", scope="factory-c")
        b = self.snapshot(lower=Decimal("103.5"), metric="energy_produced",
                          unit="MWh", scope="factory-c",
                          kind="PROPOSED_BOUND", evidence="instrument-77")
        proof = compare_gain(a, b)
        self.assertEqual(proof.gain_lower, Fraction(7, 2))
        self.assertEqual(proof.as_dict()["candidate_kind"], "PROPOSED_BOUND")


class RealModelAdapterChecks(unittest.TestCase):
    def test_social_feasible_joint_gain_is_two(self):
        result = social_joint_capacity_gain(
            ProducerWorld(True), handoff_fn=current_handoff,
            capacity_fn=full_state_joint_capacity)
        self.assertEqual(result.status, "CERTIFIED_STRICT_GAIN")
        self.assertEqual(result.gain_lower, 2)
        self.assertEqual(result.candidate.kind, "FEASIBLE")

    def test_social_negative_control_has_no_gain(self):
        result = social_joint_capacity_gain(
            ProducerWorld(False), handoff_fn=current_handoff,
            capacity_fn=full_state_joint_capacity)
        self.assertEqual(result.status, "CERTIFIED_NO_STRICT_GAIN")
        self.assertEqual(result.gain_upper, 0)

    def test_agentic_actual_prior_and_strong_peer_are_distinct(self):
        result = agentic_arm_gains(AG01_RUN_SHAPE)
        self.assertEqual(result["executed"].gain_lower, Fraction(3, 2))
        self.assertEqual(result["executed"].candidate.kind, "OBSERVED")
        self.assertEqual(result["proposed"].gain_lower, Fraction(4, 5))
        self.assertEqual(result["proposed"].candidate.kind, "PROPOSED_BOUND")
        self.assertEqual(result["against_peer"].status, "CERTIFIED_NO_STRICT_GAIN")
        self.assertEqual(result["against_peer"].gain_upper, 0)

    def test_agentic_bogus_b_has_negative_physical_result_and_refuted_claim(self):
        # The actual AG11 synthetic output is 8.875; its claimed Q is +0.8.
        from copy import deepcopy
        run = deepcopy(AG01_RUN_SHAPE)
        run["id"] = "AG11-BOGUS-B-CERTIFICATE"
        bad = run["arms"]["Q_META_PROTOCOL"]
        bad["observed_by_referee_only"]["output"] = 8.875
        bad["source_B_claim_supported_by_lab_truth"] = False
        results = agentic_arm_gains(run, peer_arm=None)
        self.assertEqual(results["executed"].gain_lower, -Fraction(9, 8))
        self.assertEqual(results["executed"].status, "CERTIFIED_NO_STRICT_GAIN")
        self.assertEqual(results["proposed"].gain_lower, Fraction(4, 5))
        self.assertEqual(results["proposed"].status, "REFUTED_EVIDENCE")

    def test_independent_directed_instrument_cannot_inherit_original_q_validation(self):
        from copy import deepcopy
        run = deepcopy(AG01_RUN_SHAPE)
        run["arms"]["CONVENTIONAL_DIRECTED"] = {
            "plan": {"conditional_near_gain": 0.8},
            "observed_by_referee_only": {"output": 11.5},
            "source_B_claim_supported_by_lab_truth": True,
        }
        gains = agentic_arm_gains(run, arm="CONVENTIONAL_DIRECTED", peer_arm=None)
        self.assertEqual(gains["executed"].gain_lower, Fraction(3, 2))
        self.assertEqual(gains["proposed"].status, "UNVERIFIED_EVIDENCE")

    def test_agentic_review_only_knows_gain_but_does_not_execute_it(self):
        result = agentic_arm_gains(AG01_RUN_SHAPE, arm="Q_REVIEW_ONLY", peer_arm=None)
        self.assertEqual(result["executed"].gain_upper, 0)
        self.assertEqual(result["proposed"].gain_lower, Fraction(4, 5))
        self.assertIsNone(result["against_peer"])

    def test_geometry_actual_and_threshold_bound_are_exact(self):
        exact_features = [(Decimal(v), Decimal(v))
                          for v in ("0.90", "0.85", "0.80", "0.95")]
        low, high = geometry_score_bounds(exact_features)
        self.assertEqual((low, high), (Fraction(157, 160), Fraction(157, 160)))
        threshold_low, threshold_high = geometry_score_bounds(
            [(Decimal("0.60"), 1)] * 4)
        self.assertEqual((threshold_low, threshold_high), (Fraction(21, 25), 1))
        baseline = ValueInterval("geometry", "score", "theme18-v1",
                                 "OBSERVED", "fixture-baseline", Fraction(3, 4), Fraction(3, 4),
                                 verification="SUPPORTED")
        candidate = ValueInterval("geometry", "score", "theme18-v1",
                                  "PROPOSED_BOUND", "qualified-feature-bounds",
                                  threshold_low, threshold_high,
                                  verification="SUPPORTED")
        self.assertEqual(compare_gain(baseline, candidate).gain_lower, Fraction(9, 100))
        self.assertEqual(compare_gain(
            baseline, ValueInterval("geometry", "score", "theme18-v1",
                                    "OBSERVED", "numeric-evidence", low, high,
                                    verification="SUPPORTED")
        ).gain_lower, Fraction(37, 160))

    def test_geometry_out_of_box_or_nonfinite_input_fails(self):
        for bad in (math.nan, math.inf, True, -0.1, 1.01):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                geometry_score_bounds([(0, 1)] * 3 + [(bad, 1)])
        with self.assertRaises(ValueError):
            geometry_score_bounds([(0, 1)] * 3)
        with self.assertRaises(ValueError):
            geometry_score_bounds([(0.9, 0.8)] * 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
