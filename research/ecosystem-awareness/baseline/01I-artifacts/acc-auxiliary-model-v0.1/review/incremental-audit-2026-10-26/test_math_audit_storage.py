"""CLI storage controls for the pinned mathematical audit; no new mathematics."""
from contextlib import redirect_stderr, redirect_stdout
import importlib.util
import io
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "_acc_math_audit_storage", HERE / "math_audit_companion_2026-10-27.py")
tool = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(tool)
RESULT = {"scope": "test payload", "sources_verified": [], "checks": [
    {"check": "sentinel", "passed": True}], "passed": 1, "total": 1, "findings": {}}


def cli(*args):
    with patch.object(sys, "argv", [str(SPEC.origin), *map(str, args)]):
        return tool.main()


class MathAuditStorageTests(unittest.TestCase):
    def test_default_stdout_preserves_reference_and_removes_download_workspace(self):
        roots = []
        def checks(root, *, allow_download):
            self.assertTrue(allow_download)
            roots.append(root)
            (root / "download.py").write_text("# temporary source", encoding="utf-8")
            return RESULT
        with TemporaryDirectory() as scratch:
            package = Path(scratch)
            reference = package / "MATH_AUDIT_RESULTS_2026-10-27.json"
            reference.write_bytes(b"reference sentinel")
            output = io.StringIO()
            with patch.object(tool, "HERE", package), patch.object(
                    tool, "run_checks", side_effect=checks), redirect_stdout(output):
                self.assertEqual(cli(), 0)
            self.assertEqual(json.loads(output.getvalue()), RESULT)
            self.assertEqual(reference.read_bytes(), b"reference sentinel")
            self.assertEqual(set(package.iterdir()), {reference})
            self.assertFalse(roots[0].exists())

    def test_explicit_output_is_new_and_an_existing_destination_is_refused_early(self):
        with TemporaryDirectory() as scratch:
            destination = Path(scratch) / "new.json"
            output = io.StringIO()
            with patch.object(tool, "run_checks", return_value=RESULT) as checks:
                with redirect_stdout(output):
                    self.assertEqual(cli("--output", destination), 0)
                raw = destination.read_bytes()
                self.assertEqual(json.loads(raw), RESULT)
                self.assertEqual(json.loads(output.getvalue()), {
                    "passed": 1, "total": 1, "verified_source_blobs": 0})
                with redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
                    cli("--output", destination)
                self.assertEqual(error.exception.code, 2)
                self.assertEqual(checks.call_count, 1)
                self.assertEqual(destination.read_bytes(), raw)

    def test_output_created_during_checks_is_not_overwritten(self):
        with TemporaryDirectory() as scratch:
            destination = Path(scratch) / "concurrent.json"
            def checks(root, *, allow_download):
                destination.write_bytes(b"other writer")
                return RESULT
            with patch.object(tool, "run_checks", side_effect=checks), redirect_stderr(
                    io.StringIO()), self.assertRaises(SystemExit) as error:
                cli("--output", destination)
            self.assertEqual(error.exception.code, 2)
            self.assertEqual(destination.read_bytes(), b"other writer")

    def test_supplied_archive_is_read_only_and_never_enables_downloads(self):
        with TemporaryDirectory() as scratch:
            archive = Path(scratch)
            source = archive / "source.py"
            source.write_bytes(b"source sentinel")
            def checks(root, *, allow_download):
                self.assertEqual(root, archive)
                self.assertFalse(allow_download)
                return RESULT
            with patch.object(tool, "run_checks", side_effect=checks), patch.object(
                    tool, "TemporaryDirectory", side_effect=AssertionError("no download workspace")), redirect_stdout(
                    io.StringIO()):
                self.assertEqual(cli("--source-archive", archive), 0)
            self.assertEqual(source.read_bytes(), b"source sentinel")
            self.assertEqual(set(archive.iterdir()), {source})

    def test_failed_check_removes_temporary_sources_and_emits_no_result(self):
        roots = []
        def checks(root, *, allow_download):
            roots.append(root)
            (root / "download.py").write_bytes(b"temporary")
            raise AssertionError("audit check failed")
        output = io.StringIO()
        with patch.object(tool, "run_checks", side_effect=checks), redirect_stdout(output):
            with self.assertRaisesRegex(AssertionError, "audit check failed"):
                cli()
        self.assertFalse(roots[0].exists())
        self.assertEqual(output.getvalue(), "")

    def test_loading_archived_sources_creates_no_bytecode_and_restores_process_flag(self):
        name = "_acc_math_audit_bytecode_probe"
        try:
            with TemporaryDirectory() as scratch:
                root = Path(scratch)
                path = root / "probe.py"
                path.write_text("VALUE = 7\n", encoding="utf-8")
                with patch.object(sys, "dont_write_bytecode", False):
                    self.assertEqual(tool.load_module(name, path).VALUE, 7)
                    self.assertFalse(sys.dont_write_bytecode)
                self.assertFalse((root / "__pycache__").exists())
        finally:
            sys.modules.pop(name, None)


if __name__ == "__main__":
    unittest.main()
