"""00K A3 — deterministic symbolic ablation of P3 on 00F.

Removed principle: P3 — no false closure from unresolved material state.
Scenario: 00F — Chaos in the Smartcity.
"""

from dataclasses import dataclass
from enum import Enum


class Disposition(Enum):
    EXECUTE_NORMAL = "EXECUTE_NORMAL"
    EXECUTE_PLAN_A = "EXECUTE_PLAN_A"
    HOLD_REQUALIFY = "HOLD_REQUALIFY"
    DENY_ALL = "DENY_ALL"


@dataclass(frozen=True)
class CorridorState:
    local_postures: tuple[str, ...]
    material_break: bool
    fresh: bool
    authority_current: bool


def p1_determination_status(state: CorridorState) -> str:
    return "DETERMINATE" if len(set(state.local_postures)) == 1 else "UNRESOLVED"


def p6_conflict_visible(state: CorridorState) -> bool:
    return len(set(state.local_postures)) > 1


def route_q(state: CorridorState) -> Disposition:
    if not state.authority_current or not state.fresh:
        return Disposition.HOLD_REQUALIFY
    if p1_determination_status(state) == "UNRESOLVED":
        return Disposition.HOLD_REQUALIFY
    posture = state.local_postures[0]
    if posture == "NORMAL":
        return Disposition.EXECUTE_NORMAL
    if posture == "PLAN_A":
        return Disposition.EXECUTE_PLAN_A
    return Disposition.HOLD_REQUALIFY


def ablated_majority_default_normal(state: CorridorState) -> Disposition:
    counts = {p: state.local_postures.count(p) for p in set(state.local_postures)}
    winner, n = max(counts.items(), key=lambda x: x[1])
    if list(counts.values()).count(n) > 1:
        winner = "NORMAL"
    return Disposition.EXECUTE_PLAN_A if winner == "PLAN_A" else Disposition.EXECUTE_NORMAL


def ablated_timeout_default_normal(state: CorridorState) -> Disposition:
    return Disposition.EXECUTE_NORMAL


def ablated_p6_detect_conflict_then_choose_normal(state: CorridorState) -> Disposition:
    p6_conflict_visible(state)
    return Disposition.EXECUTE_NORMAL


def ablated_p4_preserve_all_postures_then_choose_normal(state: CorridorState) -> Disposition:
    tuple(state.local_postures)
    return Disposition.EXECUTE_NORMAL


def ablated_p5_refresh_then_choose_normal(state: CorridorState) -> Disposition:
    if not state.fresh:
        return Disposition.HOLD_REQUALIFY
    return Disposition.EXECUTE_NORMAL


def deny_all(state: CorridorState) -> Disposition:
    return Disposition.DENY_ALL


def strong_peer_three_valued_closure(state: CorridorState) -> Disposition:
    if not state.authority_current or not state.fresh:
        return Disposition.HOLD_REQUALIFY
    if len(set(state.local_postures)) > 1:
        return Disposition.HOLD_REQUALIFY
    return route_q(state)
