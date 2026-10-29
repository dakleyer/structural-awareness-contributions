"""G-03 regressions: microexperiment results must be computed from finite rows."""
from __future__ import annotations

from fractions import Fraction
import unittest

import campaign
import finite_information as fin


class GenerativeFiniteInformationTests(unittest.TestCase):
    def test_author_original_ready_witness_is_computed(self):
        output = campaign.finite_information()
        self.assertEqual(output["finite_worlds"], [
            {"a": "READY", "b": 0, "r": 0},
            {"a": "READY", "b": 1, "r": 1},
        ])
        self.assertEqual(output["h_response_given_A_bits"], 1.0)
        self.assertEqual(output["h_response_given_A_and_B_bits"], 0.0)
        self.assertEqual(output["conditional_mutual_information_bits"], 1.0)
        self.assertEqual(output["preimage_theoretical_m"], 4)
        self.assertEqual(output["preimage_constructible_n"], 2)
        self.assertEqual(output["KL_P_to_Q_bits"], "INFINITE_SUPPORT_MISMATCH")
        self.assertEqual(output["KL_Q_to_P_bits"], 1.0)

    def test_source_xor_witness_observations_not_hardcoded_bits(self):
        output = campaign.source_anchored_microexperiments()["FINITE_XOR_SYNERGY"]
        self.assertEqual(output["joint_states"], 4)
        self.assertEqual(output["target_outputs"], [0, 1, 1, 0])
        self.assertEqual((output["I_R_Q1_bits"], output["I_R_Q2_bits"],
                          output["I_R_Q1Q2_bits"]), (0.0, 0.0, 1.0))
        self.assertIs(output["no_open_D_probability"], True)

    def test_nonuniform_worlds_change_joint_information(self):
        rows = [{"q1": a, "q2": b, "r": a ^ b}
                for a in (0, 1) for b in (0, 1)]
        equal = [1, 1, 1, 1]
        uneven = [4, 1, 1, 1]
        self.assertEqual(fin.mutual_information(rows, "r", ("q1",), equal), 0.0)
        self.assertGreater(fin.mutual_information(rows, "r", ("q1",), uneven), 0)
        self.assertLess(fin.mutual_information(rows, "r", ("q1", "q2"), uneven), 1)
        self.assertAlmostEqual(
            fin.mutual_information(rows, "r", ("q1", "q2"), uneven),
            fin.entropy_of(rows, ("r",), uneven), places=12)

    def test_redundant_observers_do_not_create_extra_information(self):
        rows = [{"source": 0, "copy": 0, "r": 0},
                {"source": 1, "copy": 1, "r": 1}]
        self.assertEqual(fin.mutual_information(rows, "r", ("source",), [1, 1]),
                         fin.mutual_information(rows, "r", ("source", "copy"), [1, 1]))

    def test_missing_data_does_not_get_a_probability(self):
        for rows, weights in (([{"x": 1}], []),
                              ([{"x": 1}], [-1]),
                              ([{"x": 1}], [0]),
                              ([{"x": 1}], [float("nan")]),
                              ([{"x": 1}], [True])):
            with self.subTest(rows=rows, weights=weights), self.assertRaises(ValueError):
                fin.joint_distribution(rows, ("x",), weights)
        with self.assertRaisesRegex(ValueError, "missing a declared"):
            fin.joint_distribution([{"x": 1}], ("not_observed",), [1])
        with self.assertRaises(ValueError):
            fin.joint_distribution([{"x": []}], ("x",), [1])

    def test_support_mismatch_has_a_direction(self):
        p = {0: Fraction(1, 2), 1: Fraction(1, 2)}
        q = {0: Fraction(1)}
        self.assertEqual(fin.kl_bits(p, q), float("inf"))
        self.assertEqual(fin.kl_bits(q, p), 1.0)

    def test_null_outcome_entropy_and_equal_observations(self):
        rows = [{"a": "READY", "r": 0}, {"a": "READY", "r": 0}]
        self.assertEqual(fin.conditional_entropy(rows, "r", ("a",), [1, 1]), 0.0)
        self.assertEqual(fin.mutual_information(rows, "r", ("a",), [1, 1]), 0.0)


if __name__ == "__main__":
    unittest.main()
