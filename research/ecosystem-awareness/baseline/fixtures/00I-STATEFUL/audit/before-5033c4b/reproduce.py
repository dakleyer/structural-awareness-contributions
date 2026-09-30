"""Run candidates, then evaluate externally; preserve all traces before exit."""
import argparse
import hashlib
import json
import platform
from pathlib import Path

from model import run_case

HERE = Path(__file__).resolve().parent


def evaluate(actual, expected):
    return {key: actual[key] == value for key, value in expected.items()}


def reproduce(output):
    inputs = json.loads((HERE / "fixtures.json").read_text())
    # Execute first: no oracle content is passed to the runtime.
    results = []
    for case in inputs["cases"]:
        try:
            results.append(run_case(case))
        except Exception as exc:
            results.append(dict(id=case["id"], execution_error=type(exc).__name__ + ": " + str(exc)))
    oracle = json.loads((HERE / "oracle.json").read_text())
    rows = []
    for result in results:
        expected = oracle["expectations"][result["id"]]
        assertions = evaluate(result, expected) if "execution_error" not in result else {"execution": False}
        rows.append(dict(id=result["id"], expected=expected,
                         observed={key: result.get(key) for key in expected},
                         assertions=assertions, scenario_pass=all(assertions.values())))
    failures = sorted(row["id"] for row in rows if not row["scenario_pass"])
    errors = [r["id"] for r in results if "execution_error" in r]
    regression_pass = not errors and failures == sorted(oracle["expected_failure_cases"])
    hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sorted(HERE.iterdir()) if p.suffix in (".py", ".json", ".md")}
    summary = dict(schema="00I-stateful-results-v1", evidence_level="bounded_stateful_simulation",
                   python=platform.python_version(), scenario_count=len(rows),
                   scenario_pass_count=len(rows) - len(failures), scenario_fail_count=len(failures),
                   actual_failure_cases=failures, expected_failure_cases=oracle["expected_failure_cases"],
                   execution_errors=errors, regression_pass=regression_pass,
                   regression_meaning="Declared defended cases pass and deliberate controls/limitations fail scenario acceptance.",
                   source_sha256=hashes, rows=rows)
    output.mkdir(parents=True, exist_ok=True)
    (output / "traces.jsonl").write_text("".join(json.dumps(r, sort_keys=True) + "\n" for r in results))
    (output / "results.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: summary[k] for k in ("scenario_count", "scenario_pass_count", "scenario_fail_count", "actual_failure_cases", "execution_errors", "regression_pass")}, indent=2))
    return regression_pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    raise SystemExit(0 if reproduce(args.output) else 1)
