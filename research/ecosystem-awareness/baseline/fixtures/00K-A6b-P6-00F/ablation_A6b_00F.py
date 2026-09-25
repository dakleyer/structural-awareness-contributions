from dataclasses import dataclass
from enum import Enum


class Disposition(Enum):
    EXECUTE_ALL = "EXECUTE_ALL"
    REQUALIFY = "REQUALIFY"
    DENY_ALL = "DENY_ALL"
    EXECUTE_PRIORITY_ONLY = "EXECUTE_PRIORITY_ONLY"


@dataclass(frozen=True)
class LocalPosture:
    actor: str
    corridor: str
    slot: int
    direction: str
    authorized: bool = True
    fresh: bool = True
    determined: bool = True
    priority: int = 0


@dataclass(frozen=True)
class MobilityFixture:
    postures: tuple[LocalPosture, ...]


def local_checks_pass(fx: MobilityFixture) -> bool:
    return all(p.authorized and p.fresh and p.determined for p in fx.postures)


def incompatible_pairs(fx: MobilityFixture):
    pairs = []
    ps = fx.postures
    for i in range(len(ps)):
        for j in range(i + 1, len(ps)):
            a, b = ps[i], ps[j]
            if (
                a.corridor == b.corridor
                and a.slot == b.slot
                and a.direction != b.direction
            ):
                pairs.append((a.actor, b.actor))
    return pairs


def route_q_p6(fx: MobilityFixture) -> Disposition:
    if not local_checks_pass(fx):
        return Disposition.REQUALIFY
    if incompatible_pairs(fx):
        return Disposition.REQUALIFY
    return Disposition.EXECUTE_ALL


def ablated_local_only(fx: MobilityFixture) -> Disposition:
    return Disposition.EXECUTE_ALL if local_checks_pass(fx) else Disposition.REQUALIFY


def ablated_p1_more_local_evidence(fx: MobilityFixture) -> Disposition:
    return Disposition.EXECUTE_ALL if local_checks_pass(fx) else Disposition.REQUALIFY


def ablated_p3_no_unknown_only(fx: MobilityFixture) -> Disposition:
    return (
        Disposition.EXECUTE_ALL
        if all(p.determined for p in fx.postures)
        else Disposition.REQUALIFY
    )


def native_mutex(fx: MobilityFixture) -> Disposition:
    return Disposition.EXECUTE_PRIORITY_ONLY if fx.postures else Disposition.DENY_ALL


def static_priority(fx: MobilityFixture) -> Disposition:
    return Disposition.EXECUTE_PRIORITY_ONLY if fx.postures else Disposition.DENY_ALL


def strong_compatibility_peer(fx: MobilityFixture) -> Disposition:
    # Non-EA peer: explicit resource-time compatibility matrix. The
    # implementation is different, but the invariant is P6 composition /
    # non-substitution over the shared resource.
    if not local_checks_pass(fx):
        return Disposition.REQUALIFY
    return (
        Disposition.REQUALIFY
        if incompatible_pairs(fx)
        else Disposition.EXECUTE_ALL
    )
