"""Structural integrity check for the 00K semantic traceability chain.

This script checks repository paths and declared coverage. It intentionally does
not claim to prove semantic truth by itself. Semantic derivation is documented
in 02A/A19; syntactic closure is documented in 02B/A21.
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
FOUNDATION_GRAMMAR = json.loads((HERE / "foundation_principle_grammar.json").read_text(encoding="utf-8"))
REQUIREMENT_GRAMMAR = json.loads((HERE / "requirement_grammar.json").read_text(encoding="utf-8"))

EXPECTED_P = {f"P{i}" for i in range(1, 7)}
EXPECTED_S = {f"S{i}" for i in range(1, 15)}
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

    # Every requirement has exactly one declared primary principle.
    for sid, spec in requirements.items():
        p = spec["primary_principle"]
        assert p in EXPECTED_P, f"{sid}: invalid primary principle {p}"

    # Every principle owns at least one primary requirement.
    primary_range = {spec["primary_principle"] for spec in requirements.values()}
    assert primary_range == EXPECTED_P

    # Principle-side primary lists agree with requirement-side declarations.
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

        # Every P has one operational route and two distinct proof witnesses.
        assert spec["scenario"]
        assert spec["corpus_witness"]
        assert spec["math_witness"]

        assert_path(spec["scenario_file"])
        assert_path(spec["harness"])
        assert_path(spec["harness"] + "/README.md")
        for upstream in spec["upstream"]:
            assert_path(upstream)


    # Foundation -> principle syntactic normal-form integrity.
    assert set(FOUNDATION_GRAMMAR["witnesses"]) == EXPECTED_P
    assert FOUNDATION_GRAMMAR["precedence"] == ["P5", "P4", "P6", "P3", "P2", "P1"]
    for p, witness in FOUNDATION_GRAMMAR["witnesses"].items():
        assert witness["type"] in {"T0", "T1", "T2"}
        assert witness["locus"] in {"I", "O"}
        assert witness["propagation"] in {"L", "R", "C"}
        assert witness["temporal"] in {"S", "DELTA"}
        assert witness["claim_class"] in {"G", "AUT"}

    # Principle -> requirement grammar must generate exactly 14 unique normal forms.
    state_objects = set(REQUIREMENT_GRAMMAR["state_objects"])
    operators = set(REQUIREMENT_GRAMMAR["operators"])
    normal_forms = REQUIREMENT_GRAMMAR["normal_forms"]
    ontology = state_objects | operators
    assert len(state_objects) == 8
    assert len(operators) == 6
    assert state_objects.isdisjoint(operators)
    assert set(normal_forms) == ontology

    generated_requirements = {spec["requirement"] for spec in normal_forms.values()}
    assert generated_requirements == EXPECTED_S

    # Each normal form has a non-empty valid principle signature.
    for name, spec in normal_forms.items():
        sig = set(spec["signature"])
        assert sig, f"{name}: empty principle signature"
        assert sig <= EXPECTED_P, f"{name}: invalid principle in signature {sig - EXPECTED_P}"

    # Independent provenance must cover every ontology element.
    provenance = REQUIREMENT_GRAMMAR["provenance"]
    assert set(provenance) == ontology
    assert all(str(v).strip() for v in provenance.values())

    # A21 anchor declarations must match the operational traceability anchors and
    # each anchor requirement must actually include the corresponding principle.
    grammar_anchors = REQUIREMENT_GRAMMAR["anchors"]
    assert grammar_anchors == EXPECTED_ANCHORS
    req_to_nf = {
        spec["requirement"]: (name, set(spec["signature"]))
        for name, spec in normal_forms.items()
    }
    for p, sid in EXPECTED_ANCHORS.items():
        assert p in req_to_nf[sid][1], (
            f"{p}: anchor {sid} does not include principle in requirement signature"
        )

    # Requirement grammar and traceability manifest agree on all S identifiers.
    assert set(requirements) == generated_requirements

    # All proof/router paths exist.
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
    print("Foundation normal forms: 6/6")
    print("Requirement normal forms: 14/14")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
