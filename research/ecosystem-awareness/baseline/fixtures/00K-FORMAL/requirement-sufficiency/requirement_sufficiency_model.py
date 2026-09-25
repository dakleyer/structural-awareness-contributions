from __future__ import annotations

from dataclasses import dataclass, fields
from itertools import product
from typing import Iterable, Tuple


@dataclass(frozen=True)
class State:
    evidence_fit: bool = False
    residual_explicit: bool = False
    bounded_progress: bool = False
    fallback_defined: bool = False
    deadline_viable: bool = False
    unresolved_material: bool = False
    executes: bool = False
    authority_current: bool = False
    authority_scoped: bool = False
    authority_verifiable: bool = False
    authority_nonamplifying: bool = False
    material_changed: bool = False
    requalified: bool = False
    composition_active: bool = False
    dependency_independent: bool = False
    compatibility_preserved: bool = False

    # Independent observations/obligations required by the canonical S/T text.
    # These are input facts, never computed from a target P predicate.
    permission_from_uncertainty: bool = False
    material_break_detected: bool = False
    change_disposition_recorded: bool = False
    changed_basis_carried: bool = False
    response_authorized: bool = False
    response_failure_declared: bool = False
    response_reversibility_declared: bool = False
    response_externalities_declared: bool = False
    response_downside_declared: bool = False
    null_action_declared: bool = False
    strong_response_claimed: bool = False
    no_worse_than_null: bool = False
    cost_ledger_declared: bool = False
    expansion_value_declared: bool = False
    composition_effects_declared: bool = False
    dependency_qualifiers_carried: bool = False
    dependent_support_promoted: bool = False


# --- Principle predicates: independent semantic target layer ---

def p1(s: State) -> bool:
    return s.evidence_fit and s.residual_explicit


def p2(s: State) -> bool:
    return s.bounded_progress and s.fallback_defined and s.deadline_viable


def p3(s: State) -> bool:
    return not (s.unresolved_material and s.executes)


def p4(s: State) -> bool:
    return (not s.executes) or (
        s.authority_current
        and s.authority_scoped
        and s.authority_verifiable
        and s.authority_nonamplifying
    )


def p5(s: State) -> bool:
    return (not s.executes) or (not s.material_changed) or s.requalified


def p6(s: State) -> bool:
    return (not s.composition_active) or (
        s.dependency_independent and s.compatibility_preserved
    )


P = (p1, p2, p3, p4, p5, p6)


# --- Source-led clause projections (not complete canonical conformance) ---
# Canonical source: 00 §§2-3. See CLAUSE_AUDIT.md for field meanings,
# omitted dimensions and why P3/P5/P6 remain unproved in this abstraction.

def s14_evidence_to_decision(s: State) -> bool:
    return s.evidence_fit


def t2_qualified_residual(s: State) -> bool:
    return s.residual_explicit


def s5_residual_nonpermission(s: State) -> bool:
    return s.residual_explicit and not s.permission_from_uncertainty


def s3_bounded_escape(s: State) -> bool:
    return s.fallback_defined


def t4_viable_requalification(s: State) -> bool:
    # Partial projection: finite effort, useful horizon, cost/value and effects.
    # Fallback is represented separately by S3, not hidden in the P2 formula.
    return (s.bounded_progress and s.deadline_viable
            and s.cost_ledger_declared and s.expansion_value_declared
            and ((not s.composition_active) or s.composition_effects_declared))


def s4_human_capacity_surface(s: State) -> bool:
    return s.deadline_viable


def s5_no_false_permission(s: State) -> bool:
    # No conversion of uncertainty into permission. A bounded authorized
    # response under uncertainty is not itself such a conversion.
    return not s.permission_from_uncertainty


def t3_bounded_authorized_response(s: State) -> bool:
    # One T3 projection shared by R3 and R4. The no-worse bit stands for an
    # externally supplied per-state certificate, not a utility proof here.
    return ((not s.executes) or
            (s.response_authorized and s.response_failure_declared
             and s.response_reversibility_declared and s.response_externalities_declared
             and s.response_downside_declared and s.null_action_declared
             and ((not s.strong_response_claimed) or s.no_worse_than_null)))


def s1_authority_current_scope(s: State) -> bool:
    return (not s.executes) or (s.authority_current and s.authority_scoped)


def s6_receiver_can_verify_authority(s: State) -> bool:
    return (not s.executes) or s.authority_verifiable


def s8_nonamplification(s: State) -> bool:
    return (not s.executes) or s.authority_nonamplifying


def s10_material_change_path(s: State) -> bool:
    # S10 detects and records the required confirmation/revalidation/cancel/
    # authority-change disposition; this alone is not an actuation interlock.
    return ((not s.material_changed) or
            (s.material_break_detected and s.change_disposition_recorded))


def t1_material_break_visible(s: State) -> bool:
    return (not s.material_changed) or s.material_break_detected


def t2_changed_basis_carried(s: State) -> bool:
    return (not s.material_changed) or s.changed_basis_carried


def s9_non_substituting_composition(s: State) -> bool:
    # Correlation may exist; promoting dependent records as independent support
    # is the prohibited transition. Merely demanding independence is stronger.
    return (not s.composition_active) or (not s.dependent_support_promoted)


def s11_cross_domain_coupling_preserved(s: State) -> bool:
    return (not s.composition_active) or s.compatibility_preserved


def t2_composition_qualifiers_preserved(s: State) -> bool:
    return (not s.composition_active) or s.dependency_qualifiers_carried


# Explicit inventory used by both evaluation and the permanent audit.
BUNDLE_CLAUSES = (
    (s14_evidence_to_decision, t2_qualified_residual, s5_residual_nonpermission),
    (s3_bounded_escape, t4_viable_requalification, s14_evidence_to_decision),
    (s5_no_false_permission, t2_qualified_residual, t3_bounded_authorized_response),
    (s1_authority_current_scope, s6_receiver_can_verify_authority,
     s8_nonamplification, t3_bounded_authorized_response),
    (s10_material_change_path, t1_material_break_visible, t2_changed_basis_carried,
     t4_viable_requalification, s5_no_false_permission),
    (s9_non_substituting_composition, s11_cross_domain_coupling_preserved,
     t2_composition_qualifiers_preserved, t4_viable_requalification),
)


def _bundle(clauses):
    return lambda s: all(clause(s) for clause in clauses)


R = tuple(_bundle(clauses) for clauses in BUNDLE_CLAUSES)
r1, r2, r3, r4, r5, r6 = R


def states(names=None) -> Iterable[State]:
    # No silent 16-bit enumeration after adding independent source facts.
    # Full enumeration is possible; the certificate uses exact support
    # projections proved complete by its restricted-expression validator.
    selected = tuple(names) if names is not None else tuple(f.name for f in fields(State))
    for bits in product((False, True), repeat=len(selected)):
        yield State(**dict(zip(selected, bits)))


def p_signature(s: State) -> Tuple[bool, ...]:
    return tuple(f(s) for f in P)


def r_signature(s: State) -> Tuple[bool, ...]:
    return tuple(f(s) for f in R)
