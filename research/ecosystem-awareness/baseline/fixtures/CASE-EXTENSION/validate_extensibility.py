"""Validate the 00E-00J case-study extensibility registry."""
from __future__ import annotations

import json
import re
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

def assert_path(path:str)->None:
    assert (ROOT/path).exists(), f"missing path: {path}"

def main()->int:
    assert set(M["families"])==EXPECTED_FAMILIES
    assert set(M["directions"])==EXPECTED_DIRECTIONS
    assert_path(M["method"])
    assert_path(M["source_extensibility"])

    for fid,spec in M["families"].items():
        assert spec["family_name"].strip()
        assert_path(spec["parent"])
        assert_path(spec["profile"])
        assert set(spec["directions"])==EXPECTED_DIRECTIONS
        for direction,examples in spec["directions"].items():
            assert examples, f"{fid}: no {direction} extension examples"
            assert all(str(x).strip() for x in examples)
        ps=set(spec["core_principles"])
        ss=set(spec["requirement_surfaces"])
        assert ps and ps<=EXPECTED_P, f"{fid}: invalid principles {ps-EXPECTED_P}"
        assert ss and ss<=EXPECTED_S, f"{fid}: invalid requirements {ss-EXPECTED_S}"

    print("Failure case-study extensibility registry: PASS")
    print("Families: 6/6")
    print("Directions per family: 3/3")
    print("Profiles: 6/6")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
