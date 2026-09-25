"""00K A2 — deterministic symbolic ablation of P2 on 00E.

Removed principle: P2 — bounded unresolved effort and viable oversight.
Scenario: 00E — 100 Million Tokens / compounded epistemic collapse.
"""

from dataclasses import dataclass
from enum import Enum


class Disposition(Enum):
    EXECUTE = "EXECUTE"
    NO_CONCLUSION = "NO_CONCLUSION"
    RESOURCE_EXHAUSTED = "RESOURCE_EXHAUSTED"
    DENY_ALL = "DENY_ALL"


@dataclass(frozen=True)
class EvidenceStep:
    decision_relevant: bool
    resolves: bool


@dataclass(frozen=True)
class SearchFixture:
    stream: tuple[EvidenceStep, ...]
    hard_capacity: int
    useful_horizon: int


def route_q_bounded_search(fixture: SearchFixture, max_steps: int = 3) -> Disposition:
    steps = 0
    for item in fixture.stream:
        if steps >= min(max_steps, fixture.hard_capacity, fixture.useful_horizon):
            return Disposition.NO_CONCLUSION
        steps += 1
        if item.resolves:
            return Disposition.EXECUTE
        if not item.decision_relevant and steps >= max_steps:
            return Disposition.NO_CONCLUSION
    return Disposition.NO_CONCLUSION


def ablated_search_until_capacity(fixture: SearchFixture) -> Disposition:
    steps = 0
    for item in fixture.stream:
        steps += 1
        if item.resolves:
            return Disposition.EXECUTE
        if steps >= fixture.hard_capacity:
            return Disposition.RESOURCE_EXHAUSTED
    return Disposition.RESOURCE_EXHAUSTED


def ablated_p1_explicit_unknown_but_keep_searching(fixture: SearchFixture) -> Disposition:
    return ablated_search_until_capacity(fixture)


def ablated_p3_no_false_closure_but_keep_holding(fixture: SearchFixture) -> Disposition:
    return ablated_search_until_capacity(fixture)


def ablated_p4_perfect_handoff_but_keep_searching(fixture: SearchFixture) -> Disposition:
    return ablated_search_until_capacity(fixture)


def fixed_timeout_deny_all(fixture: SearchFixture, timeout_steps: int = 1) -> Disposition:
    for i, item in enumerate(fixture.stream, start=1):
        if item.resolves:
            return Disposition.EXECUTE
        if i >= timeout_steps:
            return Disposition.DENY_ALL
    return Disposition.DENY_ALL


def strong_peer_budgeted_search(fixture: SearchFixture, budget: int = 3) -> Disposition:
    return route_q_bounded_search(fixture, max_steps=budget)
