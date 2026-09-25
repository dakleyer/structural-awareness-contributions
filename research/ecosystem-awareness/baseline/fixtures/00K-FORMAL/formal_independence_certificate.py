"""Machine-checkable finite-model certificate for 00K P1–P6 independence.

Mathematical claim:
For T={P1,...,P6}, the family is relatively logically independent in the
declared model class iff for every Pi there exists a model Mi satisfying all
Pj (j != i) and violating Pi.

The six witnesses below are reduced semantic traces grounded in the corrected
A1–A6 fixtures. The script checks the complete 6x6 countermodel matrix.

This is a proof certificate for the formalized predicates, not a proof of
universal AI-safety minimality.
"""
from __future__ import annotations

from dataclasses import dataclass


PRINCIPLES = ("P1", "P2", "P3", "P4", "P5", "P6")


@dataclass(frozen=True)
class Trace:
    name: str
    scenario: str

    # P1: evidence is sufficient for the actual receiving proposition/decision.
    evidence_supports_decision: bool

    # P2: unresolved determination effort is finite/viable and has bounded fallback.
    effort_bounded_and_viable: bool

    # P3: known unresolved material state is not promoted into permission/certainty.
    unresolved_not_promoted: bool

    # P4 (refined): current decision-sufficient non-amplifying authority basis exists.
    authority_basis_sufficient: bool

    # P5: the action-time material decision basis is current or requalification occurs.
    material_basis_current_or_requalified: bool

    # P6: material dependence/compatibility is composed without silent substitution.
    composition_non_substituting: bool

    expected_failure: str


def satisfies(trace: Trace, principle: str) -> bool:
    return {
        "P1": trace.evidence_supports_decision,
        "P2": trace.effort_bounded_and_viable,
        "P3": trace.unresolved_not_promoted,
        "P4": trace.authority_basis_sufficient,
        "P5": trace.material_basis_current_or_requalified,
        "P6": trace.composition_non_substituting,
    }[principle]


WITNESSES = {
    # 00J matched-semantic negative branch:
    # everything is current/bounded/provenanced/non-composed, but the evidence
    # supports a narrower proposition than the enforcement decision.
    "P1": Trace(
        "M1_00J_wrong_proposition",
        "00J",
        False, True, True, True, True, True,
        "unsupported rights-enforcement conclusion",
    ),

    # 00E unresolved-search branch:
    # UNKNOWN is explicit and not false-closed; handoff/current/composition
    # properties can all hold while search/review effort remains unbounded.
    "P2": Trace(
        "M2_00E_unbounded_determination",
        "00E",
        True, False, True, True, True, True,
        "capacity exhaustion / terminal unresolved search",
    ),

    # 00F matched conflict:
    # conflict is visible, fresh, bounded and fully preserved, but the system
    # still promotes one unresolved posture to executable permission.
    "P3": Trace(
        "M3_00F_false_closure",
        "00F",
        True, True, False, True, True, True,
        "incompatible corridor posture is executed",
    ),

    # 00H Branch U:
    # finding is real, process bounded, leaves fresh and campaign composition
    # visible, but no current authority basis covers the composed campaign.
    "P4": Trace(
        "M4_00H_authority_amplification",
        "00H",
        True, True, True, False, True, True,
        "unauthorized composed campaign executes or is misclassified",
    ),

    # 00I stale-action branch:
    # original decision/provenance/conflict visibility remain intact, but the
    # action-time material basis changed and is not requalified.
    "P5": Trace(
        "M5_00I_semantic_toctou",
        "00I",
        True, True, True, True, False, True,
        "stale but technically valid action executes",
    ),

    # 00G hidden-common-root branch:
    # every local claim is qualified/current/provenanced and process bounded;
    # the missing property is transitive dependence/non-substitution.
    "P6": Trace(
        "M6_00G_hidden_dependency",
        "00G",
        True, True, True, True, True, False,
        "dependent evidence is promoted as independent ecosystem support",
    ),
}


def truth_matrix():
    return {
        witness_name: {p: satisfies(w, p) for p in PRINCIPLES}
        for witness_name, w in WITNESSES.items()
    }


def validate_countermodels() -> None:
    assert set(WITNESSES) == set(PRINCIPLES)

    for missing in PRINCIPLES:
        w = WITNESSES[missing]
        assert not satisfies(w, missing), (
            f"{w.name} must violate {missing}"
        )
        for other in PRINCIPLES:
            if other == missing:
                continue
            assert satisfies(w, other), (
                f"{w.name} must satisfy {other} while violating {missing}"
            )


def validate_irredundancy() -> None:
    # Removing Pi strictly enlarges the model class because Mi is then
    # admissible under all remaining axioms while it is excluded by full T.
    for missing in PRINCIPLES:
        w = WITNESSES[missing]
        reduced_theory_holds = all(
            satisfies(w, p) for p in PRINCIPLES if p != missing
        )
        full_theory_holds = all(satisfies(w, p) for p in PRINCIPLES)
        assert reduced_theory_holds
        assert not full_theory_holds


def main() -> int:
    validate_countermodels()
    validate_irredundancy()

    print("      " + " ".join(f"{p:>3}" for p in PRINCIPLES))
    for missing in PRINCIPLES:
        w = WITNESSES[missing]
        bits = " ".join(
            f"{int(satisfies(w,p)):>3}" for p in PRINCIPLES
        )
        print(f"{missing:>3}:  {bits}   {w.name}")

    print()
    print("00K formal relative-independence certificate: PASS (6/6 countermodels)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
