#!/usr/bin/env python3
"""Mechanical replay of the historical HF bot-written deterministic examples.

NOT an independent scientific audit. Original case policies and oracles were
written by ChatGPT GPT-6. Never edit, rewrite, or score historical data in place.
"""
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

BASE = Path("research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/hugging-face")
VERSION_DIR = BASE / "review-2026-10-11" / "traversals"
VERSIONS = ("v0.3", "v0.4", "v0.5", "v0.6")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def root():
    for parent in Path(__file__).resolve().parents:
        if (parent / BASE / "README.md").is_file():
            return parent
    raise RuntimeError("Repository root not found")


def replay(source, temp):
    temp.mkdir(parents=True)
    shutil.copyfile(source / "run.py", temp / "run.py")
    try:
        process = subprocess.run(
            [sys.executable, "run.py"], cwd=temp, capture_output=True,
            text=True, timeout=90, check=False
        )
    except subprocess.TimeoutExpired:
        return {"version": source.name, "status": "TIMEOUT", "files_checked": 0}
    ignore = {"run.py", "README.md", "results.json", "SHA256_MANIFEST.json"}
    wanted = sorted(
        f for f in source.iterdir() if f.is_file() and f.name not in ignore
        and f.suffix in (".json", ".jsonl", ".csv")
    )
    differences = []
    for f in wanted:
        new = temp / f.name
        if not new.is_file():
            differences.append({"file": f.name, "problem": "not generated"})
        elif sha(f) != sha(new):
            differences.append({"file": f.name, "problem": "hash mismatch"})
    return {"version": source.name,
            "status": "PASS" if process.returncode == 0 and wanted and not differences else "FAIL",
            "files_checked": len(wanted), "differences": differences,
            "stderr_tail": process.stderr[-800:]}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix="hf-bot-") as folder:
        rows = [
            replay(root() / VERSION_DIR / ("first-channel-counterfactual-" + version),
                   Path(folder) / version)
            for version in VERSIONS
        ]
    result = {
        "type": "AUTOMATED_DETERMINISTIC_BOT_APPROXIMATION_REPLAY",
        "scientifically_independent": False,
        "original_model_author": "OpenAI ChatGPT GPT-6",
        "historical_llm_agent_episodes": 0,
        "dds_stage_a_b_c_pass": False,
        "v0_2": "archived; not replayed because of absolute legacy output path",
        "status": "PASS" if all(r["status"] == "PASS" for r in rows) else "FAIL",
        "versions": rows
    }
    output = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    print(output)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(output, encoding="utf-8")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
