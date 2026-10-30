"""L08 agentic source interoperability tests, without changing original programs."""
from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
from pathlib import Path
import json
import tempfile
import unittest

from l08_agentic_adapter import run, SOURCE

RESULT=run()
BY_ID={row["case_id"]:row for row in RESULT["cases"]}


class AgenticReuseContract(unittest.TestCase):
    def test_all_thirty_source_cases_and_six_unchanged_policy_arms(self):
        self.assertEqual(RESULT["source_native_cases"],30)
        self.assertEqual(RESULT["policy_decisions_replayed"],180)
        self.assertEqual(len(BY_ID),30)
        self.assertEqual(RESULT["source_ownership"],"PR57.agentic_reduction.py")
        self.assertEqual(len(RESULT["source_policies_unchanged"]),6)
        self.assertTrue(all(len(c["policy_arms"])==6 for c in RESULT["cases"]))
        self.assertTrue(all(len(v)==64 for v in RESULT["source_sha256"].values()))

    def test_ag01_directed_better_physical_but_at_higher_instrument_price(self):
        row=BY_ID["AG01-QUALIFIED-NEAR-OPTIMUM"]
        arms=row["policy_arms"]
        directed=arms["CONVENTIONAL_DIRECTED"]
        q=arms["Q_META_PROTOCOL"]
        self.assertEqual(Fraction(directed["technical_gap_referee_only"]),0)
        self.assertEqual(Fraction(q["technical_gap_referee_only"]),2)
        self.assertEqual(Fraction(directed["instrument_price_assumption"]),Fraction(6,5))
        self.assertEqual(Fraction(q["instrument_price_assumption"]),Fraction(3,10))
        self.assertIn("CONVENTIONAL_DIRECTED",
                      row["two_axis_nonfungible_front_referee_only"])
        self.assertIn("Q_META_PROTOCOL",
                      row["two_axis_nonfungible_front_referee_only"])
        self.assertTrue(row["not_an_agentic_exclusive_differential"])

    def test_equivalent_conventional_q_preserves_agentic_tie(self):
        row=BY_ID["AG01-QUALIFIED-NEAR-OPTIMUM"]
        q=row["policy_arms"]["Q_META_PROTOCOL"]
        peer=row["policy_arms"]["CONVENTIONAL_EQUIVALENT_Q"]
        self.assertEqual(q["mission_output_referee_only"],
                         peer["mission_output_referee_only"])
        self.assertEqual(q["instrument_price_assumption"],
                         peer["instrument_price_assumption"])
        self.assertEqual(q["technical_gap_referee_only"],
                         peer["technical_gap_referee_only"])

    def test_each_case_enforces_source_evidence_and_material_conservation(self):
        for item in RESULT["cases"]:
            with self.subTest(case=item["case_id"]):
                self.assertTrue(item["cannot_compare_with_social_banana_utility"])
                self.assertEqual(item["horizon"],"ONE_SOURCE_DECLARED_PR57_DECISION")
                self.assertTrue(item["source_document_ids"])
                for p in item["policy_arms"].values():
                    self.assertTrue(p["resource_total_conserved"])
                    self.assertTrue(p["no_subjective_suffering_claim"])
                    self.assertGreaterEqual(Fraction(p["technical_gap_referee_only"]),0)
                    self.assertGreaterEqual(Fraction(p["instrument_price_assumption"]),0)

    def test_pareto_counts_are_membership_not_crosscase_value_totals(self):
        memberships=RESULT["nonfungible_front_memberships_not_aggregate_winner_rates"]
        self.assertEqual(set(memberships),set(RESULT["source_policies_unchanged"]))
        self.assertTrue(all(0<=v<=30 for v in memberships.values()))
        self.assertGreaterEqual(sum(memberships.values()),30)
        self.assertFalse("global_net_utility" in RESULT)
        self.assertEqual(RESULT["interpretation"],
                         "POST_HOC_WITHIN_CASE_ONLY; DIFFERENT_QUESTION_THAN_SOCIAL_G04; NO_EMPIRICAL_AI_OR_HUMAN_DATA; C_D_NOT_CLOSED")

    def test_mismatched_or_duplicated_native_case_rejected(self):
        original=json.loads((SOURCE/"CASES.json").read_text(encoding="utf-8"))
        copied=deepcopy(original)
        copied["cases"].append(deepcopy(original["cases"][0]))
        with tempfile.TemporaryDirectory() as name:
            temp=Path(name)
            (temp/"CASES.json").write_text(json.dumps(copied),encoding="utf-8")
            (temp/"agentic_reduction.py").write_bytes(
                (SOURCE/"agentic_reduction.py").read_bytes())
            with self.assertRaisesRegex(ValueError,"duplicate agentic case IDs"):
                run(temp)


if __name__ == "__main__":
    unittest.main()
