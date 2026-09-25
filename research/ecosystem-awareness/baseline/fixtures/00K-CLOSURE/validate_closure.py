"""Structural validator for 02B/A21 syntactic closure manifests."""
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

M=json.loads((HERE/"closure_manifest.json").read_text(encoding="utf-8"))
P={f"P{i}" for i in range(1,7)}
S={f"S{i}" for i in range(1,15)}
EXPECTED_CONTROLS={
    "I0","I1","I2","O0","O1","O2",
    "E0-I","E1-I","E2-I","E0-O","E1-O","E2-O",
    "temporal_material_change",
    "authority_typed_received_claim",
    "general_composition_law",
}

def main()->int:
    assert set(M["principles"])==P
    controls=M["foundational_controls"]
    assert set(controls)==EXPECTED_CONTROLS
    generated=set()
    for cid, ps in controls.items():
        assert ps, f"{cid}: empty normalization"
        assert set(ps)<=P, f"{cid}: unknown P"
        generated.update(ps)
    assert generated==P, f"not all principles generated: {generated}"

    req=M["requirement_normal_forms"]
    assert set(req)==S
    for sid,spec in req.items():
        assert spec["primary"] in P, f"{sid}: bad primary"
        assert spec["surface"].strip(), f"{sid}: empty surface"

    primary_range={spec["primary"] for spec in req.values()}
    assert primary_range==P, f"not all P own requirement normal forms: {primary_range}"

    for pth in M["proofs"].values():
        assert (ROOT/pth).exists(), f"missing proof {pth}"

    print("00K syntactic closure integrity: PASS")
    print("Foundation/control surfaces: 15/15")
    print("Principle normal forms: 6/6")
    print("Requirement normal forms: 14/14")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
