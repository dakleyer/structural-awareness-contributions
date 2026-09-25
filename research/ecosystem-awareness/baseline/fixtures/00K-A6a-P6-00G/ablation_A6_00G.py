from dataclasses import dataclass
from enum import Enum


class Disposition(Enum):
    EXECUTE = "EXECUTE"
    DENY = "DENY"
    REQUALIFY = "REQUALIFY"


@dataclass(frozen=True)
class Claim:
    sender: str
    source_root: str
    signed: bool
    confidence: float


@dataclass(frozen=True)
class FrameFixture:
    claims: tuple[Claim, ...]
    transition_authority_applicable: bool
    candidate_frame: str = "FRAME_B"


def independent_source_count(fx: FrameFixture) -> int:
    return len({c.source_root for c in fx.claims})


def route_q(fx: FrameFixture) -> Disposition:
    if independent_source_count(fx) < 2:
        return Disposition.DENY
    if not fx.transition_authority_applicable:
        return Disposition.DENY
    return Disposition.EXECUTE


def identity_quorum_without_p6(fx: FrameFixture, quorum=3) -> Disposition:
    signed_senders = {c.sender for c in fx.claims if c.signed}
    return Disposition.EXECUTE if len(signed_senders) >= quorum else Disposition.DENY


def confidence_without_p6(fx: FrameFixture, threshold=.9) -> Disposition:
    avg = sum(c.confidence for c in fx.claims) / len(fx.claims)
    return Disposition.EXECUTE if avg >= threshold else Disposition.DENY


def deny_all(fx: FrameFixture) -> Disposition:
    return Disposition.DENY


def authority_only_without_p6(fx: FrameFixture) -> Disposition:
    # Intentionally does not inspect source_root.
    return Disposition.EXECUTE if fx.transition_authority_applicable else Disposition.DENY


def provenance_preserving_but_identity_counting(fx: FrameFixture) -> Disposition:
    # P4 may preserve source_root while a P6-blind decision still counts
    # authenticated senders as if they were independent evidence.
    return identity_quorum_without_p6(fx)
