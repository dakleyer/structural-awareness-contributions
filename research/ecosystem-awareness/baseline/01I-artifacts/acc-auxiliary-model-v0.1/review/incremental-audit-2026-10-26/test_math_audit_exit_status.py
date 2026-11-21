"""Fault-injected CLI result status; not additional mathematical findings."""
from contextlib import redirect_stdout
from copy import deepcopy
import importlib.util
import io
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "_acc_math_audit_exit_status", HERE / "math_audit_companion_2026-10-27.py")
tool = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(tool)
VALID = {"scope": "CLI status fixture only", "sources_verified": [],
         "passed": 2, "total": 2, "checks": [
             {"check": "first", "passed": True},
             {"check": "second", "passed": True}], "findings": {}}


def emitted(report):
    output = io.StringIO()
    with patch.object(tool, "run_checks", return_value=report), redirect_stdout(output):
        status = tool.main([])
    return status, json.loads(output.getvalue())


class MathAuditExitStatusTests(unittest.TestCase):
    def test_complete_nonempty_report_returns_success_without_rewriting_result(self):
        original = deepcopy(VALID)
        self.assertEqual(emitted(VALID), (0, VALID))
        self.assertEqual(VALID, original)

    def test_consistent_failed_report_returns_failure_and_preserves_findings(self):
        report = deepcopy(VALID)
        report["passed"] = 1
        report["checks"][1]["passed"] = False
        report["findings"] = {"retained": "failure evidence"}
        original = deepcopy(report)
        self.assertEqual(emitted(report), (1, original))
        self.assertEqual(report, original)

    def test_inconsistent_unknown_or_empty_counts_cannot_report_success(self):
        cases = []
        for field in ("passed", "total"):
            for value in (None, True, False, "2", 2.0, -1, 0, 1, 3):
                report = deepcopy(VALID)
                report[field] = value
                cases.append(report)
        for checks in (None, {}, [], [VALID["checks"][0]]):
            report = deepcopy(VALID)
            report["checks"] = checks
            cases.append(report)
        report = deepcopy(VALID)
        report.update(passed=0, total=0, checks=[])
        cases.append(report)
        for report in cases:
            with self.subTest(report=report):
                original = deepcopy(report)
                self.assertEqual(emitted(report), (1, original))
                self.assertEqual(report, original)

    def test_summary_cannot_turn_unknown_check_evidence_into_success(self):
        for evidence in (None, False, 1, "True", "UNKNOWN", {}, []):
            report = deepcopy(VALID)
            report["checks"][1]["passed"] = evidence
            with self.subTest(value=repr(evidence)):
                self.assertEqual(emitted(report), (1, report))
        for check in ({}, "unknown check", None):
            report = deepcopy(VALID)
            report["checks"][1] = check
            with self.subTest(check=check):
                self.assertEqual(emitted(report), (1, report))

    def test_explicit_failed_result_is_saved_to_new_file_and_returns_failure(self):
        report = deepcopy(VALID)
        report["passed"] = 1
        report["checks"][1]["passed"] = False
        with TemporaryDirectory() as scratch:
            destination = Path(scratch) / "failed-result.json"
            with patch.object(tool, "run_checks", return_value=report), redirect_stdout(io.StringIO()):
                status = tool.main(["--output", str(destination)])
            self.assertEqual(status, 1)
            self.assertEqual(json.loads(destination.read_text(encoding="utf-8")), report)


if __name__ == "__main__":
    unittest.main()
