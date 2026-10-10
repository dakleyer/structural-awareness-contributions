#!/usr/bin/env python3
"""Seven local T06 tests of v0.3 admission condition, not whole DDS approval."""
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).parent
TARGET = ROOT / "check_gate_profile_v0.3_audit_candidate.py"
spec = importlib.util.spec_from_file_location("dds_v03_candidate", TARGET)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class T06RationaleControls(unittest.TestCase):
    def test_complete_na_rationale_is_admitted_by_new_control(self):
        checker.require_na_rationale({"gates": [
            {"gate_id": "SA-G04", "applicability": "NOT_APPLICABLE",
             "own_verdict": "NOT_APPLICABLE",
             "applicability_rationale": "Outside the frozen decision boundary"}
        ]})

    def test_missing_na_rationale_is_rejected(self):
        with self.assertRaisesRegex(checker.ApplicabilityContractError,
                                    "not_applicable_requires_rationale:SA-G04"):
            checker.require_na_rationale({"gates": [
                {"gate_id": "SA-G04", "applicability": "NOT_APPLICABLE",
                 "own_verdict": "NOT_APPLICABLE"}
            ]})

    def test_blank_na_rationale_is_rejected(self):
        with self.assertRaises(checker.ApplicabilityContractError):
            checker.require_na_rationale({"gates": [
                {"gate_id": "SA-G04", "applicability": "NOT_APPLICABLE",
                 "own_verdict": "NOT_APPLICABLE", "applicability_rationale": " \t "}
            ]})

    def test_na_rationale_must_be_text(self):
        with self.assertRaises(checker.ApplicabilityContractError):
            checker.require_na_rationale({"gates": [
                {"gate_id": "SA-G04", "applicability": "NOT_APPLICABLE",
                 "own_verdict": "NOT_APPLICABLE", "applicability_rationale": ["because"]}
            ]})

    def test_normal_applicable_pass_needs_no_na_rationale(self):
        checker.require_na_rationale({"gates": [
            {"gate_id": "SA-G04", "applicability": "APPLICABLE",
             "own_verdict": "PASS"}
        ]})

    def test_non_object_row_is_rejected(self):
        with self.assertRaisesRegex(checker.ApplicabilityContractError,
                                    "non_object_gate_row"):
            checker.require_na_rationale({"gates": ["not a row"]})

    def test_no_fabricated_pre_registration_check(self):
        checker.require_na_rationale({"gates": [
            {"gate_id": "SA-G04", "applicability": "NOT_APPLICABLE",
             "own_verdict": "NOT_APPLICABLE",
             "applicability_rationale": "Created after inspecting the outcome"}
        ]})


if __name__ == "__main__":
    unittest.main()
