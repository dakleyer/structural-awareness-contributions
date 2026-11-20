"""Cross-model F1/D1 tests: value comparison is downstream, not the mechanism."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import math
import sys
import unittest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "nested-composition-suffering-v0.1"))
from nested_model import ProducerWorld, current_handoff, full_state_joint_capacity

from structural_adequacy import FiniteDecisionCase, assess_finite_adequacy
from qualified_gain import ValueInterval, compare_gain

# Full declared_public(AG01) == declared_public(AG02) in PR57 at
# a98940490e8a84051ad314f2392c15338dbf1de9. Their hidden rates differ.
AGENTIC_PUBLIC_A = {
    "scope": "vendor-ecosystem-v1", "total_resources": 10,
    "donor_current": 6, "recipient_current": 4, "donor_marginal_rate": 1,
    "donor_minimum": 2, "transfer_maximum": 4, "overhead_resources": 0.25,
    "metamorph_declared_in_A": True, "release_declared_in_A": True,
    "release_consent": True, "meta_owner_authority": True,
    "joint_protocol_available": True, "mission_target": 12,
    "known_upper_rate_bound": 2.5, "material_D_for_joint_decision": False,
    "current_A_total_output": 10,
}


def social_cases(question="current_output"):
    worlds = (ProducerWorld(True), ProducerWorld(False))
    return [
        FiniteDecisionCase(
            "SOC-JOINT" if w.joint_reallocation_possible else "SOC-NO-JOINT",
            "nested-social-v0.1", question,
            current_handoff(w),
            current_handoff(w)[1] if question == "current_output"
            else full_state_joint_capacity(w),
            "nested_model/referee",
            successor_a={"joint_reallocation": full_state_joint_capacity(w)},
        )
        for w in worlds
    ]


def agentic_cases(question="current_output", *, add_qualified_q=False):
    cases = []
    for key, after_fixed_transfer, q_rate in (
            ("AG01", 11.5, 1.6), ("AG02", 8.875, 0.4)):
        a = deepcopy(AGENTIC_PUBLIC_A)
        if add_qualified_q:
            # A+Q only *after* the source has separately qualified this B.
            # Never a replacement for PR57's scope/freshness/rights checks.
            a = (a, q_rate)
        cases.append(FiniteDecisionCase(
            key, "vendor-ecosystem-v1", question, a,
            10 if question == "current_output" else after_fixed_transfer >= 10,
            "PR57/physical_response(transfer=2)",
            successor_a={"transfer_2": after_fixed_transfer},
        ))
    return cases


class StructuralCoreChecks(unittest.TestCase):
    def check(self, cases, *, scope="nested-social-v0.1", question="current_output",
              operations=()):
        return assess_finite_adequacy(
            cases, frame_id="finite-review-20261028", scope=scope,
            question=question, operations=operations,
        )

    def test_social_old_question_was_sufficient(self):
        result = self.check(social_cases())
        self.assertEqual(result.decision_status, "ADEQUATE_IN_DECLARED_FINITE_FRAME")
        self.assertEqual(result.structural_status, "ADEQUATE_IN_DECLARED_FINITE_FRAME")
        self.assertEqual(result.decision_witnesses, ())

    def test_social_new_joint_question_exposes_original_a_fiber(self):
        result = self.check(social_cases("joint_capacity"), question="joint_capacity")
        self.assertEqual(result.decision_status, "WITNESSED_RESIDUAL")
        self.assertEqual(result.decision_witnesses, (("SOC-JOINT", "SOC-NO-JOINT"),))

    def test_social_old_question_fails_new_operation_congruence(self):
        result = self.check(social_cases(), operations=("joint_reallocation",))
        self.assertEqual(result.decision_status, "ADEQUATE_IN_DECLARED_FINITE_FRAME")
        self.assertEqual(result.operation_statuses["joint_reallocation"],
                         "WITNESSED_NONCONGRUENCE")
        self.assertEqual(result.structural_status, "REQUALIFICATION_WITNESSED")

    def test_agentic_old_a_adequate_new_action_requires_distinction(self):
        kwargs = dict(scope="vendor-ecosystem-v1")
        old = self.check(agentic_cases(), **kwargs)
        dynamic = self.check(agentic_cases(), operations=("transfer_2",), **kwargs)
        changed = self.check(agentic_cases("can_reach_10_after_transfer2"),
                             question="can_reach_10_after_transfer2", **kwargs)
        self.assertEqual(old.decision_status, "ADEQUATE_IN_DECLARED_FINITE_FRAME")
        self.assertEqual(dynamic.operation_statuses["transfer_2"],
                         "WITNESSED_NONCONGRUENCE")
        self.assertEqual(changed.decision_status, "WITNESSED_RESIDUAL")
        self.assertEqual(changed.decision_witnesses, (("AG01", "AG02"),))

    def test_conditioned_on_existing_a_eligible_q_can_separate(self):
        kwargs = dict(scope="vendor-ecosystem-v1",
                      question="can_reach_10_after_transfer2")
        before = self.check(agentic_cases("can_reach_10_after_transfer2"), **kwargs)
        after = self.check(agentic_cases("can_reach_10_after_transfer2",
                                        add_qualified_q=True), **kwargs)
        self.assertEqual(before.decision_status, "WITNESSED_RESIDUAL")
        self.assertEqual(after.decision_status, "ADEQUATE_IN_DECLARED_FINITE_FRAME")
        # Adding the *same* Q to both still leaves the conflicting pair.
        same_q = [
            FiniteDecisionCase(c.case_id, c.scope, c.question,
                               (AGENTIC_PUBLIC_A, "correlated-copy"),
                               c.answer, c.evidence)
            for c in agentic_cases("can_reach_10_after_transfer2")
        ]
        self.assertEqual(self.check(same_q, **kwargs).decision_status,
                         "WITNESSED_RESIDUAL")

    def test_single_scalar_gain_does_not_establish_a_structural_residual(self):
        cases = [
            FiniteDecisionCase("one", "power-line-3", "output", 8, 8, "sensor-a"),
            FiniteDecisionCase("two", "power-line-3", "output", 10, 10, "sensor-b"),
        ]
        result = self.check(cases, scope="power-line-3", question="output")
        scalar = compare_gain(
            ValueInterval("production", "units", "power-line-3",
                          "OBSERVED", "sensor-a", 8, 8, verification="SUPPORTED"),
            ValueInterval("production", "units", "power-line-3",
                          "OBSERVED", "sensor-b", 10, 10, verification="SUPPORTED"),
        )
        self.assertEqual(result.decision_status, "ADEQUATE_IN_DECLARED_FINITE_FRAME")
        self.assertEqual(scalar.gain_lower, 2)

    def test_residual_does_not_establish_executed_gain(self):
        residual = self.check(social_cases("joint_capacity"), question="joint_capacity")
        self.assertEqual(residual.decision_status, "WITNESSED_RESIDUAL")
        # No joint move made, current production remains 8 in both worlds.
        actual = compare_gain(
            ValueInterval("production", "units", "nested-social-v0.1",
                          "OBSERVED", "before", 8, 8, verification="SUPPORTED"),
            ValueInterval("production", "units", "nested-social-v0.1",
                          "OBSERVED", "after-no-execution", 8, 8, verification="SUPPORTED"),
        )
        self.assertEqual(actual.status, "CERTIFIED_NO_STRICT_GAIN")

    def test_d1_four_state_signature_expansion_original_witness(self):
        # PR60 §02 D1: parity is congruent for s, not added f.
        def case(x):
            successor_f = {0: 1, 1: 1, 2: 0, 3: 3}[x]
            return FiniteDecisionCase(
                str(x), "four-state-demo", "parity", x % 2, x % 2, "D1-proof",
                successor_a={"s": (x + 1) % 2, "f": successor_f % 2},
            )
        base = self.check([case(x) for x in range(4)], scope="four-state-demo",
                          question="parity", operations=("s",))
        extended = self.check([case(x) for x in range(4)], scope="four-state-demo",
                              question="parity", operations=("s", "f"))
        self.assertEqual(base.structural_status, "ADEQUATE_IN_DECLARED_FINITE_FRAME")
        self.assertEqual(extended.operation_statuses["s"],
                         "CONGRUENT_IN_DECLARED_FINITE_FRAME")
        self.assertEqual(extended.operation_statuses["f"],
                         "WITNESSED_NONCONGRUENCE")

    def test_unknown_does_not_become_negative_or_adequate(self):
        rows = social_cases("joint_capacity")
        rows[1] = FiniteDecisionCase(
            rows[1].case_id, rows[1].scope, rows[1].question,
            rows[1].observed_a, None, rows[1].evidence, answer_qualified=False)
        result = self.check(rows, question="joint_capacity")
        self.assertEqual(result.decision_status, "UNKNOWN")
        self.assertEqual(result.structural_status, "UNKNOWN")
        self.assertEqual(result.unknown_case_ids, ("SOC-NO-JOINT",))

    def test_missing_operation_evidence_remains_unknown(self):
        rows = social_cases()
        rows[1] = FiniteDecisionCase(rows[1].case_id, rows[1].scope, rows[1].question,
                                     rows[1].observed_a, rows[1].answer, rows[1].evidence)
        result = self.check(rows, operations=("joint_reallocation",))
        self.assertEqual(result.operation_statuses["joint_reallocation"], "UNKNOWN")

    def test_empty_frame_is_not_a_universal_proof(self):
        result = self.check([], operations=("f",))
        self.assertEqual(result.structural_status, "UNKNOWN")
        self.assertEqual(result.operation_statuses["f"], "UNKNOWN")

    def test_reject_mixed_scope_question_and_duplicate_cases(self):
        base = social_cases("joint_capacity")
        with self.assertRaisesRegex(ValueError, "scope and question"):
            self.check(base, scope="unrelated", question="joint_capacity")
        with self.assertRaisesRegex(ValueError, "scope and question"):
            self.check(base, question="current_output")
        with self.assertRaisesRegex(ValueError, "duplicate case_id"):
            self.check([base[0], base[0]], question="joint_capacity")
        with self.assertRaisesRegex(ValueError, "duplicate operation"):
            self.check(base, question="joint_capacity", operations=("f", "f"))

    def test_python_boolean_numeric_alias_cannot_erase_a_distinction(self):
        rows = [
            FiniteDecisionCase("bool", "typed-schema", "decision", True, "ok", "e1"),
            FiniteDecisionCase("integer", "typed-schema", "decision", 1, "no", "e2"),
        ]
        result = self.check(rows, scope="typed-schema", question="decision")
        self.assertEqual(result.decision_status, "ADEQUATE_IN_DECLARED_FINITE_FRAME")
        # In the other direction, same strict A but different qualified answers
        # must remain a witnessed conflict.
        rows[1] = FiniteDecisionCase("integer", "typed-schema", "decision",
                                      True, "no", "e2")
        self.assertEqual(self.check(rows, scope="typed-schema",
                                    question="decision").decision_status,
                         "WITNESSED_RESIDUAL")

    def test_nonfinite_in_nested_a_or_response_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "nonfinite"):
            FiniteDecisionCase("invalid", "scope", "target", {"a": math.nan},
                               True, "sensor")
        with self.assertRaisesRegex(ValueError, "nonfinite"):
            FiniteDecisionCase("invalid", "scope", "target", "ready",
                               1, "sensor", successor_a={"f": math.inf})

    def test_independently_declared_version_composition_is_not_cost(self):
        # Canonical 00N example: identical ready signals but incompatible versions.
        a = FiniteDecisionCase("same", "service-pair-v1", "same_version_rule",
                               ("READY", "READY"), True, "version-ledger")
        b = FiniteDecisionCase("different", "service-pair-v1", "same_version_rule",
                               ("READY", "READY"), False, "version-ledger")
        result = self.check([a,b], scope="service-pair-v1",
                            question="same_version_rule")
        self.assertEqual(result.decision_status, "WITNESSED_RESIDUAL")
        # If the B qualifiers are validly retained, they distinguish the pair.
        av = FiniteDecisionCase("same", "service-pair-v1", "same_version_rule",
                                ("READY", "READY", "v1", "v1"), True, "qualified-B")
        bv = FiniteDecisionCase("different", "service-pair-v1", "same_version_rule",
                                ("READY", "READY", "v1", "v2"), False, "qualified-B")
        refined = self.check([av,bv], scope="service-pair-v1",
                             question="same_version_rule")
        self.assertEqual(refined.decision_status, "ADEQUATE_IN_DECLARED_FINITE_FRAME")


if __name__ == "__main__":
    unittest.main(verbosity=2)
