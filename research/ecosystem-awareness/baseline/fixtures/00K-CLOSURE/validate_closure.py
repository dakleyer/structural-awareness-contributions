"""Canonical structural validator for 02B/A21 syntactic closure.

Semantic arguments remain in 02B and A21. This script validates the declared
grammar, admitted object/operator atoms, normal-form coverage, and proof paths.
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

M = json.loads((HERE / "closure_manifest.json").read_text(encoding="utf-8"))

EXPECTED_P = {f"P{i}" for i in range(1, 7)}
EXPECTED_S = {f"S{i}" for i in range(1, 15)}
# Frozen from the audited manifest: a versioned syntax contract, not a semantic proof.
EXPECTED_ATOMS = {'QUALIFY': ('authority', 'preference', 'identity', 'evidence', 'policy'),
 'ESCALATE': ('frame', 'human', 'unresolved', 'commitment'),
 'CONTAIN': ('unresolved',),
 'HANDOFF': ('authority',
             'preference',
             'identity',
             'human',
             'evidence',
             'policy',
             'commitment',
             'history',
             'frame',
             'unresolved',
             'multi_principal'),
 'BIND': ('identity',),
 'DELEGATE': ('authority',),
 'COMPOSE': ('multi_principal', 'authority', 'preference', 'policy', 'evidence'),
 'SHIFT': ('frame', 'commitment', 'policy', 'authority', 'evidence'),
 'INTERVENE': ('human', 'authority', 'history'),
 'REPAIR': ('history', 'evidence', 'authority'),
 'ASSESS': ('evidence',)}


def main() -> int:
    p = M["principle_normal_forms"]
    s = M["requirement_normal_forms"]
    assert set(p) == EXPECTED_P
    assert set(s) == EXPECTED_S

    fops = set(M["foundation_language"]["operators"])
    ftypes = set(M["foundation_language"]["types"])
    positions = set(M["foundation_language"]["positions"])
    quals = set(M["foundation_language"]["qualifiers"])

    assert positions == {"A", "B", "C", "D"}
    assert ftypes == {"T0", "T1", "T2"}

    for pid, spec in p.items():
        assert set(spec["operators"]) <= fops, (pid, "unknown foundation operator")
        assert set(spec["types"]) <= ftypes, (pid, "unknown type")
        assert set(spec.get("qualifiers", [])) <= quals, (pid, "unknown qualifier")

    admitted_f = M["foundation_language"]["admitted_forms"]
    assert set(admitted_f) == {f"G{i}" for i in range(6)}
    generated_p = set()
    for gid, spec in admitted_f.items():
        assert spec["principle"] in EXPECTED_P
        assert set(spec["operators"]) <= fops
        assert set(spec["types"]) <= ftypes
        assert set(spec.get("qualifiers", [])) <= quals
        generated_p.add(spec["principle"])
    assert generated_p == EXPECTED_P

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

    admitted_atoms = M["requirement_language"]["admitted_atoms"]
    assert {op: tuple(objs) for op, objs in admitted_atoms.items()} == EXPECTED_ATOMS, "admitted atom contract changed"
    missing_pairs = []
    pair_total = 0
    for op, objs in admitted_atoms.items():
        assert op in rops
        for obj in objs:
            pair_total += 1
            assert obj in robjs
            covered = any(
                op in spec["operators"] and obj in spec["objects"]
                for spec in s.values()
            )
            if not covered:
                missing_pairs.append((obj, op))
    assert not missing_pairs, ("uncovered admitted requirement atoms", missing_pairs)

    for pth in M["proofs"].values():
        assert (ROOT / pth).exists(), f"missing proof {pth}"

    print("00K syntactic closure integrity: PASS")
    print("Foundation positions: 4/4")
    print("Foundation types: 3/3")
    print("Principle normal forms: 6/6")
    print("Requirement normal forms: 14/14")
    print(f"Requirement operators covered: {len(covered_ops)}/{len(rops)}")
    print(f"Requirement objects covered: {len(covered_objs)}/{len(robjs)}")
    print(f"Admitted object/operator atoms covered: {pair_total}/{pair_total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
