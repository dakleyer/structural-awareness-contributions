"""Validate the declared syntactic closure manifests for 02B / A21.

This is a structural completeness check over the declared languages. The semantic
arguments remain in 02B and A21.
"""
from __future__ import annotations
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
M = json.loads((HERE / "normal_form_manifest.json").read_text(encoding="utf-8"))

EXPECTED_P = {f"P{i}" for i in range(1, 7)}
EXPECTED_S = {f"S{i}" for i in range(1, 15)}

def main() -> int:
    p = M["principle_normal_forms"]
    s = M["requirement_normal_forms"]
    assert set(p) == EXPECTED_P
    assert set(s) == EXPECTED_S

    fops = set(M["foundation_language"]["operators"])
    ftypes = set(M["foundation_language"]["types"])
    quals = set(M["foundation_language"]["qualifiers"])

    for pid, spec in p.items():
        assert set(spec["operators"]) <= fops, (pid, "unknown foundation operator")
        assert set(spec["types"]) <= ftypes, (pid, "unknown type")
        assert set(spec.get("qualifiers", [])) <= quals, (pid, "unknown qualifier")

    rops = set(M["requirement_language"]["operators"])
    robjs = set(M["requirement_language"]["objects"])

    covered_ops = set()
    covered_objs = set()
    covered_p = set()

    for sid, spec in s.items():
        assert set(spec["operators"]) <= rops, (sid, "unknown requirement operator")
        assert set(spec["objects"]) <= robjs, (sid, "unknown requirement object")
        assert set(spec["principles"]) <= EXPECTED_P, (sid, "unknown principle")
        covered_ops.update(spec["operators"])
        covered_objs.update(spec["objects"])
        covered_p.update(spec["principles"])

    assert covered_ops == rops, ("uncovered requirement operators", rops - covered_ops)
    assert covered_objs == robjs, ("uncovered requirement objects", robjs - covered_objs)
    assert covered_p == EXPECTED_P, ("uncovered principles", EXPECTED_P - covered_p)

    print("00K normal-form syntactic closure: PASS")
    print("Foundation positions: 4/4")
    print("Foundation types: 3/3")
    print("Principle normal forms: 6/6")
    print("Requirement normal forms: 14/14")
    print(f"Requirement operators covered: {len(covered_ops)}/{len(rops)}")
    print(f"Requirement objects covered: {len(covered_objs)}/{len(robjs)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
