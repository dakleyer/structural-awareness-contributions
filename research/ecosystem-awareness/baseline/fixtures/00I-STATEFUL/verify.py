"""Preserve regression evidence, then replay scenario acceptance separately."""
import argparse
import hashlib
import io
import json
import platform
import sqlite3
import unittest
from pathlib import Path

import test_durable
from reproduce import reproduce

HERE = Path(__file__).resolve().parent


def verify(output):
    stream = io.StringIO()
    test_durable.DurableTests.evidence.clear()
    suite = unittest.TestSuite(unittest.defaultTestLoader.loadTestsFromName(name)
                               for name in ("test_stateful", "test_contract_edges", "test_durable", "test_recovery"))
    result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
    output.mkdir(parents=True, exist_ok=True)
    hashes = {str(p.relative_to(HERE)): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sorted(HERE.rglob("*")) if p.is_file()
              and p.suffix in (".py", ".json", ".md")
              and "results" not in p.relative_to(HERE).parts}
    report = dict(schema="00I-validation-extension-v3", python=platform.python_version(),
                  sqlite=sqlite3.sqlite_version, tests_run=result.testsRun,
                  failures=len(result.failures), errors=len(result.errors),
                  regression_pass=result.wasSuccessful(), stdout=stream.getvalue(),
                  source_sha256=hashes, durable_observations=test_durable.DurableTests.evidence,
                  evidence_boundary="Real subprocess exits and SQLite transactions; protected effect remains a local row, not an external operation.")
    (output / "verification.json").write_text(json.dumps(report, indent=2) + "\n")
    print(stream.getvalue())
    scenario_ok = reproduce(output)
    return result.wasSuccessful() and scenario_ok


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    raise SystemExit(0 if verify(args.output) else 1)
