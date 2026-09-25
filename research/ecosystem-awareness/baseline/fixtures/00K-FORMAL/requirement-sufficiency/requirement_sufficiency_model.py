from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Iterable, Tuple


@dataclass(frozen=True)
class State:
    evidence_fit: bool
    residual_explicit: bool
    bounded_progress: bool
    fallback_defined: bool
    deadline_viable: bool
    unresolved_material: bool
    executes: bool
    authority_current: bool
    authority_scoped: bool
    authority_verifiable: bool
    authority_nonamplifying: bool
    material_changed: bool
    requalified: bool
    composition_active: bool
    dependency_independent: bool
    compatibility_preserved: bool


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


# --- Canonical requirement / T-condition clauses ---

def s14_evidence_to_decision(s: State) -> bool:
    return s.evidence_fit


def t2_qualified_residual(s: State) -> bool:
    return s.residual_explicit


def s5_residual_nonpermission(s: State) -> bool:
    return s.residual_explicit and not (s.unresolved_material and s.executes)


def s3_bounded_escape(s: State) -> bool:
    return s.fallback_defined


def t4_viable_requalification(s: State) -> bool:
    return s.bounded_progress and s.deadline_viable


def s4_human_capacity_surface(s: State) -> bool:
    # Deliberately narrower than P2: this models an available/viable human path,
    # not every machine determination loop.
    return s.deadline_viable


def s5_no_false_permission(s: State) -> bool:
    return not (s.unresolved_material and s.executes)


def t3_response_not_evidence(s: State) -> bool:
    # In this reduced model, the relevant P3 consequence is that an unresolved
    # material state cannot be laundered through execution/default.
    return not (s.unresolved_material and s.executes)


def s1_authority_current_scope(s: State) -> bool:
    return (not s.executes) or (s.authority_current and s.authority_scoped)


def s6_receiver_can_verify_authority(s: State) -> bool:
    return (not s.executes) or s.authority_verifiable


def s8_nonamplification(s: State) -> bool:
    return (not s.executes) or s.authority_nonamplifying


def t3_authorized_response(s: State) -> bool:
    return (not s.executes) or (
        s.authority_current and s.authority_scoped
        and s.authority_verifiable and s.authority_nonamplifying
    )


def s10_material_change_path(s: State) -> bool:
    # Detecting a material change creates the obligation to reopen/revalidate
    # before the old commitment is used.
    return (not s.material_changed) or s.requalified or (not s.executes)


def t1_material_break_visible(s: State) -> bool:
    # A material change is not silently missed in the reduced model.
    return (not s.material_changed) or s.requalified or (not s.executes)


def t2_changed_basis_carried(s: State) -> bool:
    return (not s.material_changed) or s.requalified or (not s.executes)


def t4_requalification_timely(s: State) -> bool:
    return (not s.material_changed) or s.requalified or (not s.executes)


def s9_non_substituting_composition(s: State) -> bool:
    return (not s.composition_active) or s.dependency_independent


def s11_cross_domain_coupling_preserved(s: State) -> bool:
    return (not s.composition_active) or s.compatibility_preserved


def t2_composition_qualifiers_preserved(s: State) -> bool:
    return (not s.composition_active) or (
        s.dependency_independent and s.compatibility_preserved
    )


def t4_nonmonotone_composition(s: State) -> bool:
    return (not s.composition_active) or (
        s.dependency_independent and s.compatibility_preserved
    )


# --- Sufficient conformance bundles ---

def r1(s: State) -> bool:
    return s14_evidence_to_decision(s) and t2_qualified_residual(s) and s5_residual_nonpermission(s)


def r2(s: State) -> bool:
    return s3_bounded_escape(s) and t4_viable_requalification(s) and s14_evidence_to_decision(s)


def r3(s: State) -> bool:
    return s5_no_false_permission(s) and t2_qualified_residual(s) and t3_response_not_evidence(s)


def r4(s: State) -> bool:
    return (
        s1_authority_current_scope(s)
        and s6_receiver_can_verify_authority(s)
        and s8_nonamplification(s)
        and t3_authorized_response(s)
    )


def r5(s: State) -> bool:
    return (
        s10_material_change_path(s)
        and t1_material_break_visible(s)
        and t2_changed_basis_carried(s)
        and t4_requalification_timely(s)
        and s5_no_false_permission(s)
    )


def r6(s: State) -> bool:
    return (
        s9_non_substituting_composition(s)
        and s11_cross_domain_coupling_preserved(s)
        and t2_composition_qualifiers_preserved(s)
        and t4_nonmonotone_composition(s)
    )


R = (r1, r2, r3, r4, r5, r6)


def states() -> Iterable[State]:
    for bits in product((False, True), repeat=16):
        yield State(*bits)


def p_signature(s: State) -> Tuple[bool, ...]:
    return tuple(f(s) for f in P)


def r_signature(s: State) -> Tuple[bool, ...]:
    return tuple(f(s) for f in R)
