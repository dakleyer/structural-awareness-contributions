"""Finite counterexamples linking 00M plausibility, optional ACC Q and UC21.

Only checks the mathematical claim ladder and IMPORTS the EXISTING UC21
source adapter for its synthetic demonstration. It does NOT create a second
UC21 oracle, verify native product evidence, or measure social welfare/HID.
"""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


BRIDGE = Path(__file__).resolve().parent
PILOT = BRIDGE.parent / "parametric-economic-toy-v0.1"
sys.path.insert(0, str(PILOT))
from uc21_dds_bridge import SCENARIOS, SOURCE_ROUTES, assess  # noqa: E402


def scoped_sufficiency(states, summary, target):
    """Test exact question-relative sufficiency in a FINITE declared domain."""
    seen = {}
    for state in states:
        key = summary(state)
        answer = target(state)
        if key in seen and seen[key] != answer:
            return False
        seen[key] = answer
    return True


def optional_inclusion(a_policies, aq_policies):
    """Set inclusion; NOT a claim about cost or strategic equilibria."""
    return set(a_policies).issubset(set(aq_policies))


def hr_logic_only(domain_records):
    """Algebra of forall/exists from Annex R; not a UC21 outcome assessor.

    Each entry is a DECLARED logical witness:
    FULL_DOMAIN_DEFENCE_PROOF, ADMITTED_RECURRENCE_WITNESS or OPEN.
    No Stage A record is allowed to call itself such a witness in real use.
    """
    if set(domain_records) != set(SCENARIOS):
        raise ValueError("Must preserve all six native UC21 scenario identifiers")
    values = tuple(domain_records.values())
    permitted = {"FULL_DOMAIN_DEFENCE_PROOF", "ADMITTED_RECURRENCE_WITNESS", "OPEN"}
    if any(x not in permitted for x in values):
        raise ValueError("unknown logical witness status")
    if "FULL_DOMAIN_DEFENCE_PROOF" in values:
        return "HR_REFUTED_WITHIN_SPECIFIED_DOMAINS"
    if all(x == "ADMITTED_RECURRENCE_WITNESS" for x in values):
        return "HR_SCOPED_SUPPORT_NOT_UNIVERSAL_TECH_FAILURE"
    return "HR_OPEN"


class GeneralPlausibility(unittest.TestCase):
    def setUp(self):
        self.worlds = [
            {"a": "READY", "b": "v1", "answer": "GO"},
            {"a": "READY", "b": "v2", "answer": "NO_GO"},
        ]

    def test_a_is_insufficient_for_receiver_question(self):
        self.assertFalse(scoped_sufficiency(self.worlds, lambda w: w["a"],
                                            lambda w: w["answer"]))

    def test_a_plus_true_b_distinguishes(self):
        self.assertTrue(scoped_sufficiency(self.worlds,
                                          lambda w: (w["a"], w["b"]),
                                          lambda w: w["answer"]))

    def test_a_may_suffice_for_another_question(self):
        self.assertTrue(scoped_sufficiency(self.worlds, lambda w: w["a"],
                                          lambda w: w["a"] == "READY"))

    def test_empty_profile_does_not_prove_global_sufficiency(self):
        self.assertTrue(scoped_sufficiency([], lambda w: w["a"], lambda w: w["answer"]))
        # Vacuity here is precisely why a source universe must be declared.

    def test_bad_q_cannot_be_recovered_with_irrelevant_b(self):
        self.assertFalse(scoped_sufficiency(self.worlds,
                                            lambda w: (w["a"], "same-b"),
                                            lambda w: w["answer"]))


class SocialOptionalInformation(unittest.TestCase):
    def test_ignore_q_policy_retained(self):
        self.assertTrue(optional_inclusion(["safe-current", "bounded-review"],
                                           ["safe-current", "bounded-review", "scoped-go"]))

    def test_no_strict_improvement_is_required(self):
        self.assertTrue(optional_inclusion(["safe-current"], ["safe-current"]))

    def test_forced_hold_breaks_policy_inclusion(self):
        self.assertFalse(optional_inclusion(["continue"], ["always-hold"]))

    def test_extra_cost_can_reverse_net_gain(self):
        best_a = 10.0
        best_aq = 10.0
        q_cost = 1.0
        self.assertGreater(best_a, best_aq - q_cost)

    def test_relevant_q_strictly_improves_chosen_scoped_score(self):
        # Fixed two-world score for the registered receiver question.
        worlds = [("v1", "GO"), ("v2", "NO_GO")]
        a_only_best = max(sum(choice == truth for _, truth in worlds)
                          for choice in ("GO", "NO_GO"))
        qualified_correct = sum(("GO" if version == "v1" else "NO_GO") == truth
                                for version, truth in worlds)
        self.assertEqual(a_only_best, 1)
        self.assertEqual(qualified_correct, 2)
        self.assertGreater(qualified_correct, a_only_best)

    def test_public_disclosure_needs_separate_game(self):
        self.assertFalse(optional_inclusion(["old-strategic-equilibrium"],
                                            ["new-strategic-equilibrium"]))


class NativeUC21Custody(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.packet = json.loads((PILOT / "examples" /
                                 "uc21_s4_synthetic_defender.json").read_text("utf-8"))
        cls.report = assess(cls.packet)

    def test_native_source_routes_not_spoken_alias(self):
        self.assertEqual(set(SOURCE_ROUTES), {"R0", "R1", "R2"})
        self.assertNotIn("R3", SOURCE_ROUTES)

    def test_native_six_scenarios_and_37_gates(self):
        self.assertEqual(set(SCENARIOS), {"S1", "S2", "S3", "S4", "S5", "S6"})
        self.assertEqual(sum(case["gates"] for case in SCENARIOS.values()), 37)

    def test_synthetic_defence_is_not_native_refutation(self):
        self.assertEqual(
            self.report["selected_intervention_prediction"],
            "SYNTHETIC_DEFENCE_NOT_EMPIRICAL_FALSIFICATION",
        )

    def test_single_defended_delta_leaves_hr_open(self):
        self.assertEqual(
            self.report["uc21_hr_existential_six_case_conclusion"],
            "NOT_REFUTED_OR_PROVED_BY_NONEXHAUSTIVE_RUNS",
        )
        self.assertEqual(hr_logic_only({k: "OPEN" for k in SCENARIOS}),
                         "HR_OPEN")

    def test_one_exhaustively_covered_scenario_refutes_scope(self):
        vals = {k: "OPEN" for k in SCENARIOS}
        vals["S4"] = "FULL_DOMAIN_DEFENCE_PROOF"
        self.assertEqual(hr_logic_only(vals),
                         "HR_REFUTED_WITHIN_SPECIFIED_DOMAINS")

    def test_six_admitted_recurrence_witnesses_support_scoped_hr(self):
        vals = {k: "ADMITTED_RECURRENCE_WITNESS" for k in SCENARIOS}
        self.assertEqual(hr_logic_only(vals),
                         "HR_SCOPED_SUPPORT_NOT_UNIVERSAL_TECH_FAILURE")

    def test_missing_scenario_is_not_full_hr_coverage(self):
        vals = {k: "OPEN" for k in SCENARIOS if k != "S6"}
        with self.assertRaises(ValueError):
            hr_logic_only(vals)

    def test_one_successful_delta_does_not_equal_full_domain_proof(self):
        vals = {k: "OPEN" for k in SCENARIOS}
        vals["S4"] = "OPEN"
        self.assertEqual(hr_logic_only(vals), "HR_OPEN")

    def test_hr_unrecognized_witness_rejected(self):
        vals = {k: "OPEN" for k in SCENARIOS}
        vals["S2"] = "ONE_DELTA_DEFENDED"
        with self.assertRaises(ValueError):
            hr_logic_only(vals)


if __name__ == "__main__":
    unittest.main()
