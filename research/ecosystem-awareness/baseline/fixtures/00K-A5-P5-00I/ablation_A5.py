"""00K A5 — deterministic symbolic ablation of P5 on 00I Semantic TOCTOU.

Removed principle: P5 — material-change requalification at time of use.
Scenario: 00I — The Patch That Undid the Fix.

This is a fixture model, not a live system or product benchmark.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class Disposition(Enum):
    DBC_EXECUTE = "DBC_EXECUTE"
    DBC_DENY = "DBC_DENY"
    DBC_REQUALIFY = "DBC_REQUALIFY"
    DBC_HOLD = "DBC_HOLD"


@dataclass(frozen=True)
class TechnicalGrant:
    grant_id: str
    current: bool


@dataclass(frozen=True)
class DecisionBasis:
    target: str
    qualified_generation: int
    incident_open: bool
    freeze_active: bool
    source_version: str


@dataclass(frozen=True)
class QueuedAction:
    action_id: str
    target: str
    desired_generation: int
    grant: TechnicalGrant
    basis: DecisionBasis


@dataclass(frozen=True)
class CurrentState:
    generation: int
    incident_open: bool
    freeze_active: bool
    source_version: str
    source_available: bool = True


@dataclass(frozen=True)
class InterventionRecord:
    patch_id: str
    target: str
    resulting_generation: int
    legitimate: bool


def p1_basis_is_well_formed(action: QueuedAction) -> bool:
    """P1-style sufficiency at queue time: the original basis is explicit."""
    return bool(action.basis.source_version and action.target == action.basis.target)


def p4_provenance_is_preserved(action: QueuedAction, intervention: Optional[InterventionRecord]) -> bool:
    """P4-style provenance preservation only; no action-time applicability decision."""
    if intervention is None:
        return True
    return intervention.legitimate and intervention.target == action.target


def p6_conflict_is_visible(action: QueuedAction, intervention: Optional[InterventionRecord]) -> bool:
    """P6 can expose a later operation on the same target, but visibility alone
    does not decide whether the earlier action remains applicable."""
    return intervention is not None and intervention.target == action.target


def p5_current_basis_matches(action: QueuedAction, current: CurrentState) -> bool:
    """P5 invariant made concrete: compare the decision basis to action-time state."""
    if not current.source_available:
        return False
    return (
        current.generation == action.basis.qualified_generation
        and current.incident_open == action.basis.incident_open
        and current.freeze_active == action.basis.freeze_active
        and current.source_version == action.basis.source_version
    )


def route_q(action: QueuedAction, current: CurrentState) -> Disposition:
    if not action.grant.current:
        return Disposition.DBC_DENY
    if not p1_basis_is_well_formed(action):
        return Disposition.DBC_DENY
    if not current.source_available:
        return Disposition.DBC_HOLD
    if not p5_current_basis_matches(action, current):
        return Disposition.DBC_REQUALIFY
    return Disposition.DBC_EXECUTE


# P5-ablated repairs ---------------------------------------------------------

def ablated_queue_time_only(action: QueuedAction) -> Disposition:
    """No action-time state check: a once-valid action remains executable."""
    if action.grant.current and p1_basis_is_well_formed(action):
        return Disposition.DBC_EXECUTE
    return Disposition.DBC_DENY


def ablated_p1_stricter_original_basis(action: QueuedAction) -> Disposition:
    """Demand a very explicit original basis, but never compare it to now."""
    basis = action.basis
    strong = (
        p1_basis_is_well_formed(action)
        and basis.qualified_generation > 0
        and basis.source_version.startswith("cfg-")
    )
    return Disposition.DBC_EXECUTE if action.grant.current and strong else Disposition.DBC_DENY


def ablated_p4_provenance_only(action: QueuedAction, intervention: Optional[InterventionRecord]) -> Disposition:
    """Preserve the later intervention record but do not let it invalidate the old decision."""
    if not action.grant.current or not p1_basis_is_well_formed(action):
        return Disposition.DBC_DENY
    p4_provenance_is_preserved(action, intervention)
    return Disposition.DBC_EXECUTE


def ablated_p6_conflict_flag_then_execute(action: QueuedAction, intervention: Optional[InterventionRecord]) -> Disposition:
    """Notice a same-target conflict but do not reopen applicability."""
    if not action.grant.current or not p1_basis_is_well_formed(action):
        return Disposition.DBC_DENY
    p6_conflict_is_visible(action, intervention)
    return Disposition.DBC_EXECUTE


def native_serialization_only(action: QueuedAction, current: CurrentState) -> Disposition:
    """A database can serialize the old action after the new repair and still be wrong."""
    if not action.grant.current:
        return Disposition.DBC_DENY
    return Disposition.DBC_EXECUTE


def native_generation_compare(action: QueuedAction, current: CurrentState) -> Disposition:
    """Strong native repair: compare expected generation to current generation.

    This passes the fixture, but operationally reconstructs P5's check-at-use invariant.
    """
    if not action.grant.current:
        return Disposition.DBC_DENY
    if not current.source_available:
        return Disposition.DBC_HOLD
    if current.generation != action.basis.qualified_generation:
        return Disposition.DBC_REQUALIFY
    return Disposition.DBC_EXECUTE


def deny_all(action: QueuedAction) -> Disposition:
    return Disposition.DBC_DENY
