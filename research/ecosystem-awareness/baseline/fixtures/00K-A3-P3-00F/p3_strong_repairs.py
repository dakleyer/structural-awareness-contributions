"""Serious P3 repair search for 00K A3 / 00F.

P3 invariant:
Known unresolved material state must not be converted into permission, PASS or
certainty-equivalent closure. Bounded containment/action under uncertainty is
allowed only if the unresolved state remains explicit/non-promoted.
"""
from dataclasses import dataclass
from enum import Enum


class Disposition(Enum):
    EXECUTE_NORMAL = "EXECUTE_NORMAL"
    EXECUTE_PLAN_A = "EXECUTE_PLAN_A"
    EXECUTE_PLAN_B = "EXECUTE_PLAN_B"
    HOLD_REQUALIFY = "HOLD_REQUALIFY"


@dataclass(frozen=True)
class Signal:
    posture: str
    authority_rank: int = 1
    confidence: float = 0.9
    fresh: bool = True


def matched_conflict():
    return (
        Signal("PLAN_A"), Signal("PLAN_B"),
        Signal("PLAN_A"), Signal("PLAN_B"),
    )


def positive_plan_a():
    return tuple(Signal("PLAN_A") for _ in range(4))


def positive_normal():
    return tuple(Signal("NORMAL") for _ in range(4))


def old_confounded_branch():
    return (
        Signal("PLAN_A"), Signal("PLAN_B"),
        Signal("NORMAL"), Signal("HOLD"),
    )


def old_hold_marker_shortcut(signals):
    if any(s.posture == "HOLD" for s in signals):
        return Disposition.HOLD_REQUALIFY
    p = signals[0].posture
    return {
        "PLAN_A": Disposition.EXECUTE_PLAN_A,
        "PLAN_B": Disposition.EXECUTE_PLAN_B,
        "NORMAL": Disposition.EXECUTE_NORMAL,
    }.get(p, Disposition.HOLD_REQUALIFY)


def authority_priority(signals):
    best = max(s.authority_rank for s in signals)
    candidates = [s for s in signals if s.authority_rank == best]
    return _execute(candidates[0].posture)


def confidence_priority(signals):
    best = max(s.confidence for s in signals)
    candidates = [s for s in signals if s.confidence == best]
    return _execute(candidates[0].posture)


def freshest_priority(signals):
    candidates = [s for s in signals if s.fresh]
    if not candidates:
        return Disposition.HOLD_REQUALIFY
    return _execute(candidates[0].posture)


def majority_default_normal(signals):
    counts = {}
    for s in signals:
        counts[s.posture] = counts.get(s.posture, 0) + 1
    n = max(counts.values())
    winners = [p for p,c in counts.items() if c == n]
    if len(winners) != 1:
        return Disposition.EXECUTE_NORMAL
    return _execute(winners[0])


def human_approval_without_new_evidence(signals):
    return _execute(signals[0].posture)


def timeout_default_normal(signals):
    return Disposition.EXECUTE_NORMAL


def risk_priority_plan_a(signals):
    if any(s.posture == "PLAN_A" for s in signals):
        return Disposition.EXECUTE_PLAN_A
    return _execute(signals[0].posture)


def supermajority_nonpermission(signals, threshold=0.75):
    counts = {}
    for s in signals:
        counts[s.posture] = counts.get(s.posture, 0) + 1
    posture, n = max(counts.items(), key=lambda kv: kv[1])
    if n / len(signals) >= threshold:
        return _execute(posture)
    return Disposition.HOLD_REQUALIFY


def unanimity_gate(signals):
    postures = {s.posture for s in signals}
    if len(postures) == 1:
        return _execute(next(iter(postures)))
    return Disposition.HOLD_REQUALIFY


ALLOWED = {
    "NORMAL": {"NORMAL", "HOLD"},
    "PLAN_A": {"PLAN_A", "HOLD"},
    "PLAN_B": {"PLAN_B", "HOLD"},
}


def robust_action_intersection(signals):
    common = None
    for s in signals:
        actions = ALLOWED.get(s.posture, {"HOLD"})
        common = set(actions) if common is None else common & actions
    if common is None:
        return Disposition.HOLD_REQUALIFY
    if "PLAN_A" in common:
        return Disposition.EXECUTE_PLAN_A
    if "PLAN_B" in common:
        return Disposition.EXECUTE_PLAN_B
    if "NORMAL" in common:
        return Disposition.EXECUTE_NORMAL
    return Disposition.HOLD_REQUALIFY


def explicit_unresolved_containment(signals):
    postures = {s.posture for s in signals}
    if len(postures) > 1:
        return Disposition.HOLD_REQUALIFY
    return _execute(next(iter(postures)))


def _execute(posture):
    return {
        "NORMAL": Disposition.EXECUTE_NORMAL,
        "PLAN_A": Disposition.EXECUTE_PLAN_A,
        "PLAN_B": Disposition.EXECUTE_PLAN_B,
    }.get(posture, Disposition.HOLD_REQUALIFY)


def correct_conflict(result):
    return result == Disposition.HOLD_REQUALIFY


def correct_a(result):
    return result == Disposition.EXECUTE_PLAN_A


def correct_normal(result):
    return result == Disposition.EXECUTE_NORMAL
