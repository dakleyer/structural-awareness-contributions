"""Run the complete 00K symbolic regression campaign.

Core A1–A6 count: 175 tests.
Supplemental robustness/falsification count: 33 tests.
Expected total: 208 tests.

This runner intentionally executes each fixture in its own working directory so
module names cannot collide across independently authored harnesses.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import subprocess
import sys


HERE = Path(__file__).resolve().parent
FIXTURES = HERE.parent


@dataclass(frozen=True)
class Harness:
    label: str
    directory: str
    expected: int
    evidence_class: str


HARNESSES = (
    Harness("A1 P1 / 00J", "00K-A1-P1-00J", 42, "core"),
    Harness("A2 P2 / 00E", "00K-A2-P2-00E", 58, "core"),
    Harness("A3 P3 / 00F", "00K-A3-P3-00F", 15, "core"),
    Harness("A4 P4 / 00H", "00K-A4-P4-00H", 29, "core"),
    Harness("A5 P5 / 00I", "00K-A5-P5-00I", 14, "core"),
    Harness("A6 P6 / 00G matched-authority", "00K-A6-P6-00G", 17, "core"),
    Harness("P6 naive 00G falsifier", "00K-A6a-P6-00G", 10, "supplemental"),
    Harness("P6 independent 00F isolation", "00K-A6b-P6-00F", 11, "supplemental"),
    Harness("Cross-scenario independent kernels", "00K-cross-scenario-independent", 12, "supplemental"),
)


def run_one(h: Harness) -> tuple[bool, str]:
    cwd = FIXTURES / h.directory
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "-q"],
        cwd=cwd,
        text=True,
        capture_output=True,
    )
    output = (proc.stdout + "\n" + proc.stderr).strip()
    m = re.search(r"(\d+) passed", output)
    count = int(m.group(1)) if m else None
    ok = proc.returncode == 0 and count == h.expected
    return ok, output


def main() -> int:
    failures = []
    core = 0
    supplemental = 0

    for h in HARNESSES:
        ok, output = run_one(h)
        mark = "PASS" if ok else "FAIL"
        print(f"[{mark}] {h.label}: expected {h.expected}")
        print(output)
        print("-" * 72)
        if ok:
            if h.evidence_class == "core":
                core += h.expected
            else:
                supplemental += h.expected
        else:
            failures.append(h.label)

    print(f"Core passing regression count: {core}/175")
    print(f"Supplemental passing count: {supplemental}/33")
    print(f"Campaign total: {core + supplemental}/208")

    if failures:
        print("FAILED HARNESS(ES):", ", ".join(failures))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
