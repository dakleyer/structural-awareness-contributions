"""Machine-checkable finite-model certificate for 00K P1–P6 independence.

Mathematical claim
------------------
For T={P1,...,P6}, the family is relatively logically independent in the
declared 00K model class if, for every Pi, there exists a witness model Mi that
satisfies every Pj (j != i) and violates Pi.

This certificate deliberately computes P1–P6 from lower-level semantic fields.
It does not store the six principle truth values directly. The witness states
are reduced semantic models grounded in the corrected A1–A6 fixture families.

The executable fixture suites establish the concrete branch behaviour from
which these reduced witnesses are abstracted. This file checks the formal
countermodel relation; it is not a proof of universal AI-safety minimality.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


PRINCIPLES = ("P1", "P2", "P3", "P4", "P5", "P6")


class Disposition(Enum):
    EXECUTE = "EXECUTE"
    HOLD = "HOLD"
    REQUALIFY = "REQUALIFY"
    DENY = "DENY"


@dataclass(frozen=True)
class Trace:
    name: str
    scenario: str

    # P1 primitives
    evidence_supports_actual_decision: bool = True
    residual_explicit: bool = True

    # P2 primitives
    effort_decision_relevant: bool = True
    determination_stop_step: int | None = 1
    useful_horizon_step: int = 10
    bounded_fallback_defined: bool = True

    # P3 primitives
    unresolved_material: bool = False
    disposition: Disposition = Disposition.EXECUTE

    # P4 primitives
    authority_current: bool = True
    authority_receiver_verifiable: bool = True
    authority_covers_action: bool = True
    authority_non_amplifying: bool = True

    # P5 primitives
    material_basis_current: bool = True
    requalified_before_actuation: bool = False

    # P6 primitives
    dependency_preserved: bool = True
    compatibility_preserved: bool = True
    no_silent_substitution: bool = True


def p1(t: Trace) -> bool:
    """Decision-sufficient evidence + explicit residual."""
    return t.evidence_supports_actual_decision and t.residual_explicit


def p2(t: Trace) -> bool:
    """Finite viable determination with an explicit bounded fallback."""
    return (
        t.effort_decision_relevant
        and t.determination_stop_step is not None
        and t.determination_stop_step <= t.useful_horizon_step
        and t.bounded_fallback_defined
    )


def p3(t: Trace) -> bool:
    """Known unresolved material state is not promoted to execution."""
    return not (
        t.unresolved_material
        and t.disposition is Disposition.EXECUTE
    )


def p4(t: Trace) -> bool:
    """Executed action has current, verifiable, sufficient, non-amplifying authority."""
    return (
        t.disposition is not Disposition.EXECUTE
        or (
            t.authority_current
            and t.authority_receiver_verifiable
            and t.authority_covers_action
            and t.authority_non_amplifying
        )
    )


def p5(t: Trace) -> bool:
    """Execution uses a current material basis or follows requalification."""
    return (
        t.disposition is not Disposition.EXECUTE
        or t.material_basis_current
        or t.requalified_before_actuation
    )


def p6(t: Trace) -> bool:
    """Executed composition preserves dependence/compatibility without substitution."""
    return (
        t.disposition is not Disposition.EXECUTE
        or (
            t.dependency_preserved
            and t.compatibility_preserved
            and t.no_silent_substitution
        )
    )


EVALUATORS = {
    "P1": p1,
    "P2": p2,
    "P3": p3,
    "P4": p4,
    "P5": p5,
    "P6": p6,
}


WITNESSES = {
    # 00J matched-semantic negative:
    # provenance/currentness can remain sound while the evidence supports a
    # narrower proposition than the actual rights-enforcement decision.
    "P1": Trace(
        name="M1_00J_wrong_proposition",
        scenario="00J",
        evidence_supports_actual_decision=False,
    ),

    # 00E unresolved-search branch:
    # uncertainty remains explicit (HOLD), but there is no finite viable
    # determination stopping point inside the useful response horizon.
    "P2": Trace(
        name="M2_00E_unbounded_determination",
        scenario="00E",
        determination_stop_step=None,
        unresolved_material=True,
        disposition=Disposition.HOLD,
    ),

    # 00F matched conflict:
    # conflict is explicit/current/bounded, but unresolved material state is
    # still promoted to executable permission.
    "P3": Trace(
        name="M3_00F_false_closure",
        scenario="00F",
        unresolved_material=True,
        disposition=Disposition.EXECUTE,
    ),

    # 00H unauthorized composed campaign:
    # local leaves can be valid while the composed action lacks sufficient
    # current non-amplifying authority.
    "P4": Trace(
        name="M4_00H_authority_amplification",
        scenario="00H",
        authority_covers_action=False,
        authority_non_amplifying=False,
    ),

    # 00I semantic TOCTOU:
    # the queued action remains technically executable, but the material basis
    # is stale and no action-time requalification occurred.
    "P5": Trace(
        name="M5_00I_semantic_toctou",
        scenario="00I",
        material_basis_current=False,
        requalified_before_actuation=False,
    ),

    # 00G hidden common root:
    # local claims remain qualified/current, but dependent evidence is promoted
    # as if it were independent ecosystem support.
    "P6": Trace(
        name="M6_00G_hidden_dependency",
        scenario="00G",
        dependency_preserved=False,
        no_silent_substitution=False,
    ),
}


def satisfies(trace: Trace, principle: str) -> bool:
    return EVALUATORS[principle](trace)


def truth_matrix() -> dict[str, dict[str, bool]]:
    return {
        missing: {p: satisfies(w, p) for p in PRINCIPLES}
        for missing, w in WITNESSES.items()
    }


def validate_countermodels() -> None:
    assert set(WITNESSES) == set(PRINCIPLES)

    for missing in PRINCIPLES:
        witness = WITNESSES[missing]
        assert not satisfies(witness, missing), (
            f"{witness.name} must violate {missing}"
        )
        for other in PRINCIPLES:
            if other == missing:
                continue
            assert satisfies(witness, other), (
                f"{witness.name} must satisfy {other} while violating {missing}"
            )


def validate_irredundancy() -> None:
    # Removing Pi strictly enlarges the admitted witness class because Mi then
    # satisfies every remaining axiom while failing the complete theory T.
    for missing in PRINCIPLES:
        witness = WITNESSES[missing]
        reduced_theory_holds = all(
            satisfies(witness, p) for p in PRINCIPLES if p != missing
        )
        full_theory_holds = all(
            satisfies(witness, p) for p in PRINCIPLES
        )
        assert reduced_theory_holds
        assert not full_theory_holds


def main() -> int:
    validate_countermodels()
    validate_irredundancy()

    print("      " + " ".join(f"{p:>3}" for p in PRINCIPLES))
    for missing in PRINCIPLES:
        witness = WITNESSES[missing]
        bits = " ".join(
            f"{int(satisfies(witness, p)):>3}" for p in PRINCIPLES
        )
        print(f"{missing:>3}:  {bits}   {witness.name}")

    print()
    print("00K formal relative-independence certificate: PASS (6/6 countermodels)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
