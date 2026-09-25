from dataclasses import dataclass
from enum import Enum


class State(Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    UNRESOLVED = "UNRESOLVED"


class Disposition(Enum):
    EXECUTE = "EXECUTE"
    HOLD = "HOLD"
    DENY = "DENY"


@dataclass(frozen=True)
class CorridorFixture:
    state: State
    evidence_current: bool = True
    authority_valid: bool = True


def route_q_p3(fx: CorridorFixture) -> Disposition:
    if not fx.authority_valid or not fx.evidence_current:
        return Disposition.HOLD
    if fx.state == State.UNRESOLVED:
        return Disposition.HOLD
    if fx.state == State.OPEN:
        return Disposition.EXECUTE
    return Disposition.DENY


def ablated_default_open(fx: CorridorFixture) -> Disposition:
    if fx.state == State.CLOSED:
        return Disposition.DENY
    return Disposition.EXECUTE


def ablated_majority_normal(fx: CorridorFixture) -> Disposition:
    return Disposition.EXECUTE if fx.state != State.CLOSED else Disposition.DENY


def ablated_timeout_execute(fx: CorridorFixture) -> Disposition:
    return (
        Disposition.EXECUTE
        if fx.state in (State.OPEN, State.UNRESOLVED)
        else Disposition.DENY
    )


def blanket_hold(fx: CorridorFixture) -> Disposition:
    return Disposition.HOLD


def native_interlock_on_unresolved(fx: CorridorFixture) -> Disposition:
    if fx.state == State.UNRESOLVED:
        return Disposition.HOLD
    return Disposition.EXECUTE if fx.state == State.OPEN else Disposition.DENY
