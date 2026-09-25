"""Validate the canonical 00E-00J case-study extensibility registry."""
from __future__ import annotations

import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE
while ROOT!=ROOT.parent:
    if (ROOT/".github").exists() and (ROOT/"research").exists():
        break
    ROOT=ROOT.parent
else:
    raise RuntimeError("repository root not found")

M=json.loads((HERE/"extensibility_manifest.json").read_text(encoding="utf-8"))
EXPECTED_FAMILIES={"00E","00F","00G","00H","00I","00J"}
EXPECTED_DIRECTIONS={"upward","downward","horizontal"}
EXPECTED_P={f"P{i}" for i in range(1,7)}
EXPECTED_S={f"S{i}" for i in range(1,15)}

def assert_path(path:str)->Path:
    target=ROOT/path
    assert target.exists(), f"missing path: {path}"
    return target

def main()->int:
    assert set(M["families"])==EXPECTED_FAMILIES
    assert set(M["directions"])==EXPECTED_DIRECTIONS
    method_path=assert_path(M["method"])
    assert_path(M["source_extensibility"])

    # One canonical A25 only.
    baseline=ROOT/"research/ecosystem-awareness/baseline"
    a25s=list(baseline.glob("00K_A25*.md"))
    assert len(a25s)==1, f"expected one canonical A25, found {[p.name for p in a25s]}"
    assert a25s[0].resolve()==method_path.resolve()

    method=method_path.read_text(encoding="utf-8")
    for phrase in (
        "Upward / vertical extension",
        "Downward extension",
        "Horizontal extension",
        "failure-predicate preservation / reflection",
        "requirement-route / conformance preservation",
        "Requirements-conformance transfer theorem",
    ):
        assert phrase in method, f"A25 missing canonical clause: {phrase}"

    for fid,spec in M["families"].items():
        assert spec["family_name"].strip()
        parent=assert_path(spec["parent"])
        profile=assert_path(spec["profile"])
        assert set(spec["directions"])==EXPECTED_DIRECTIONS

        for direction,examples in spec["directions"].items():
            assert examples, f"{fid}: no {direction} extension examples"
            assert all(str(x).strip() for x in examples)

        ps=set(spec["core_principles"])
        ss=set(spec["requirement_surfaces"])
        assert ps and ps<=EXPECTED_P, f"{fid}: invalid principles {ps-EXPECTED_P}"
        assert ss and ss<=EXPECTED_S, f"{fid}: invalid requirements {ss-EXPECTED_S}"

        profile_text=profile.read_text(encoding="utf-8")
        for phrase in (
            "Upward / vertical extensibility",
            "Downward extensibility",
            "Horizontal extensibility",
            "Boundary",
            "Conformance transfer",
        ):
            assert phrase in profile_text, f"{fid}: profile missing {phrase}"

        parent_text=parent.read_text(encoding="utf-8")
        assert "Model Case Study" in parent_text, f"{fid}: parent not marked Model Case Study"
        assert profile.name in parent_text, f"{fid}: parent does not link its extensibility profile"

    print("Failure case-study extensibility registry: PASS")
    print("Canonical A25: 1/1")
    print("Families: 6/6")
    print("Directions per family: 3/3")
    print("Profiles: 6/6")
    print("Parent scenario links: 6/6")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
