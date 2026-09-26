"""Structural integrity check for the 00K semantic traceability chain.

This validator checks graph coverage and repository paths. Syntactic closure is
owned separately by fixtures/00K-CLOSURE.
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE
while ROOT != ROOT.parent:
    if (ROOT / ".github").exists() and (ROOT / "research").exists():
        break
    ROOT = ROOT.parent
else:
    raise RuntimeError("repository root not found")

MANIFEST = json.loads((HERE / "traceability_manifest.json").read_text(encoding="utf-8"))

EXPECTED_P = {f"P{i}" for i in range(1, 7)}
EXPECTED_S = {f"S{i}" for i in range(1, 15)}
EXPECTED_SCENARIOS = dict(zip(sorted(EXPECTED_P), ("00J", "00E", "00F", "00H", "00I", "00G")))
EXPECTED_ANCHORS = {
    "P1": "S14",
    "P2": "S4",
    "P3": "S5",
    "P4": "S8",
    "P5": "S10",
    "P6": "S9",
}


def assert_path(path: str) -> None:
    target = ROOT / path
    assert target.exists(), f"missing referenced path: {path}"


def main() -> int:
    principles = MANIFEST["principles"]
    requirements = MANIFEST["requirements"]
    anchors = MANIFEST["ablation_anchors"]

    assert set(principles) == EXPECTED_P
    assert set(requirements) == EXPECTED_S
    assert anchors == EXPECTED_ANCHORS

    for sid, spec in requirements.items():
        p = spec["primary_principle"]
        assert p in EXPECTED_P, f"{sid}: invalid primary principle {p}"

    primary_range = {spec["primary_principle"] for spec in requirements.values()}
    assert primary_range == EXPECTED_P

    for p, spec in principles.items():
        declared = set(spec["primary_requirements"])
        reverse = {
            sid for sid, rspec in requirements.items()
            if rspec["primary_principle"] == p
        }
        assert declared == reverse, (
            f"{p}: primary requirement mismatch: principle={declared}, reverse={reverse}"
        )

        anchor = anchors[p]
        assert anchor in declared, f"{p}: ablation anchor {anchor} is not primary"
        assert spec["scenario"] == EXPECTED_SCENARIOS[p], (p, "scenario mismatch")
        assert Path(spec["scenario_file"]).name.startswith(spec["scenario"] + "_"), (p, "scenario path mismatch")
        assert spec["corpus_witness"]
        assert spec["math_witness"]

        assert_path(spec["scenario_file"])
        assert_path(spec["harness"])
        assert_path(spec["harness"] + "/README.md")
        for upstream in spec["upstream"]:
            assert_path(upstream)

    for path in MANIFEST["proofs"].values():
        assert_path(path)

    math_witnesses = [principles[p]["math_witness"] for p in sorted(EXPECTED_P)]
    corpus_witnesses = [principles[p]["corpus_witness"] for p in sorted(EXPECTED_P)]
    assert len(set(math_witnesses)) == 6
    assert len(set(corpus_witnesses)) == 6

    print("00K semantic traceability integrity: PASS")
    print("Principles: 6/6")
    print("Requirements: 14/14")
    print("Anchor routes: 6/6")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
