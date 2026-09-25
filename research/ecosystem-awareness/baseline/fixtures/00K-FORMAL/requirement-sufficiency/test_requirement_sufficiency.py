from __future__ import annotations

import unittest

from requirement_sufficiency_model import (
    P, R, State, p1, p2, p4,
    s14_evidence_to_decision, s4_human_capacity_surface, s8_nonamplification,
    states,
)


class TestRequirementSufficiency(unittest.TestCase):
    def test_R1_implies_P1_exhaustively(self):
        self.assertFalse(any(R[0](s) and not P[0](s) for s in states()))

    def test_R2_implies_P2_exhaustively(self):
        self.assertFalse(any(R[1](s) and not P[1](s) for s in states()))

    def test_R3_implies_P3_exhaustively(self):
        self.assertFalse(any(R[2](s) and not P[2](s) for s in states()))

    def test_R4_implies_P4_exhaustively(self):
        self.assertFalse(any(R[3](s) and not P[3](s) for s in states()))

    def test_R5_implies_P5_exhaustively(self):
        self.assertFalse(any(R[4](s) and not P[4](s) for s in states()))

    def test_R6_implies_P6_exhaustively(self):
        self.assertFalse(any(R[5](s) and not P[5](s) for s in states()))

    def test_all_six_bundles_imply_all_six_principles(self):
        self.assertFalse(any(all(r(s) for r in R) and not all(p(s) for p in P) for s in states()))

    def test_S14_evidence_clause_alone_does_not_imply_full_P1(self):
        witness = State(
            True, False, True, True, True, False, False,
            True, True, True, True, False, True, False, True, True
        )
        self.assertTrue(s14_evidence_to_decision(witness))
        self.assertFalse(p1(witness))

    def test_S4_surface_alone_does_not_imply_P2(self):
        witness = State(
            True, True, False, False, True, False, False,
            True, True, True, True, False, True, False, True, True
        )
        self.assertTrue(s4_human_capacity_surface(witness))
        self.assertFalse(p2(witness))

    def test_S8_alone_does_not_imply_P4(self):
        witness = State(
            True, True, True, True, True, False, True,
            False, False, True, True, False, True, False, True, True
        )
        self.assertTrue(s8_nonamplification(witness))
        self.assertFalse(p4(witness))


if __name__ == "__main__":
    unittest.main()
