"""Validate the 00E-00J case-study extensibility registry.

This is a structural integrity check. It validates that the six case families,
their parent scenarios and profiles are mutually routed, and that the declared
three-axis extensibility contract is present. It does not prove empirical
equivalence of the listed domain examples.
"""
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
A25_BASENAME="00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md"

def assert_path(path:str)->Path:
    target=ROOT/path
    assert target.exists(), f"missing path: {path}"
    return target

def main()->int:
    assert set(M["families"])==EXPECTED_FAMILIES
    assert set(M["directions"])==EXPECTED_DIRECTIONS
    assert_path(M["method"])
    assert_path(M["source_extensibility"])

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

        parent_text=parent.read_text(encoding="utf-8")
        profile_name=Path(spec["profile"]).name
        assert profile_name in parent_text, (
            f"{fid}: parent scenario does not route to canonical extensibility profile"
        )
        assert A25_BASENAME in parent_text, (
            f"{fid}: parent scenario does not route to A25 admission/transfer method"
        )

        profile_text=profile.read_text(encoding="utf-8")
        assert A25_BASENAME in profile_text, f"{fid}: profile does not route to A25"
        for heading in (
            "Upward / vertical extensibility",
            "Downward extensibility",
            "Horizontal extensibility",
            "Conformance transfer",
        ):
            assert heading in profile_text, f"{fid}: missing section '{heading}'"

        # A profile must state a structural family boundary/falsifier rather than
        # relying on superficial analogy.
        assert ("Boundary" in profile_text or "falsifier" in profile_text.lower()), (
            f"{fid}: no explicit family boundary/falsifier"
        )

    print("Failure case-study extensibility registry: PASS")
    print("Families: 6/6")
    print("Directions per family: 3/3")
    print("Parent ↔ profile routes: 6/6")
    print("A25 routes: 6/6")
    print("Conformance-transfer sections: 6/6")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
