from dataclasses import dataclass
from enum import Enum


class Disposition(Enum):
    EXECUTE = "EXECUTE"
    NO_COMMITMENT = "NO_COMMITMENT"
    STILL_SEARCHING = "STILL_SEARCHING"
    FORCED_EXECUTE = "FORCED_EXECUTE"


@dataclass(frozen=True)
class SearchFixture:
    evidence_sufficient_by_step: tuple[bool, ...]
    deadline_steps: int


def route_q_p2(fx: SearchFixture, max_steps: int = 3) -> Disposition:
    limit = min(max_steps, fx.deadline_steps, len(fx.evidence_sufficient_by_step))
    for i in range(limit):
        if fx.evidence_sufficient_by_step[i]:
            return Disposition.EXECUTE
    return Disposition.NO_COMMITMENT


def ablated_keep_searching(fx: SearchFixture) -> Disposition:
    for ok in fx.evidence_sufficient_by_step[: fx.deadline_steps]:
        if ok:
            return Disposition.EXECUTE
    return Disposition.STILL_SEARCHING


def ablated_more_reviewers(fx: SearchFixture) -> Disposition:
    return ablated_keep_searching(fx)


def timeout_default_execute(fx: SearchFixture, timeout: int = 3) -> Disposition:
    for ok in fx.evidence_sufficient_by_step[:timeout]:
        if ok:
            return Disposition.EXECUTE
    return Disposition.FORCED_EXECUTE


def deny_all(fx: SearchFixture) -> Disposition:
    return Disposition.NO_COMMITMENT


def fixed_budget_peer(fx: SearchFixture, budget_steps: int = 3) -> Disposition:
    for ok in fx.evidence_sufficient_by_step[
        : min(budget_steps, fx.deadline_steps)
    ]:
        if ok:
            return Disposition.EXECUTE
    return Disposition.NO_COMMITMENT
