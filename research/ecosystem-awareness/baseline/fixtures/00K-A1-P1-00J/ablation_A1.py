"""00K A1 — deterministic symbolic ablation of P1 on 00J.

Removed principle: P1 — qualified determination and explicit residual.
Scenario: 00J — Rights-Provenance Inversion / "The Author Pays for Their Own Work".

The fixture distinguishes a technically valid generation-provenance record
from evidence that actually supports an enforceable rights proposition.
"""

from dataclasses import dataclass
from enum import Enum


class Disposition(Enum):
    ENFORCE_LICENSE = "ENFORCE_LICENSE"
    REQUALIFY = "REQUALIFY"
    NO_CONCLUSION = "NO_CONCLUSION"
    DENY_ALL = "DENY_ALL"


@dataclass(frozen=True)
class Evidence:
    record_id: str
    evidence_type: str
    proposition_supported: str
    signed: bool
    fresh: bool
    source: str


REQUIRED_PROPOSITION = "RIGHT_TO_ENFORCE_AGAINST_AUTHOR"


def p4_preserve_record(e: Evidence) -> bool:
    return bool(e.record_id and e.source and e.signed)


def p5_record_current(e: Evidence) -> bool:
    return e.fresh


def p1_supports_required_proposition(e: Evidence) -> bool:
    return e.signed and e.fresh and e.proposition_supported == REQUIRED_PROPOSITION


def route_q(evidence: list[Evidence]) -> Disposition:
    if not evidence or not all(p4_preserve_record(e) for e in evidence):
        return Disposition.REQUALIFY
    if any(p1_supports_required_proposition(e) for e in evidence):
        return Disposition.ENFORCE_LICENSE
    return Disposition.NO_CONCLUSION


def ablated_any_signed_record_is_enough(evidence: list[Evidence]) -> Disposition:
    return Disposition.ENFORCE_LICENSE if any(e.signed and e.fresh for e in evidence) else Disposition.NO_CONCLUSION


def ablated_p4_perfect_provenance_only(evidence: list[Evidence]) -> Disposition:
    if all(p4_preserve_record(e) for e in evidence):
        return Disposition.ENFORCE_LICENSE
    return Disposition.REQUALIFY


def ablated_p5_refresh_every_record(evidence: list[Evidence]) -> Disposition:
    if all(p5_record_current(e) for e in evidence):
        return Disposition.ENFORCE_LICENSE
    return Disposition.REQUALIFY


def ablated_p6_independent_replication(evidence: list[Evidence], required_sources: int = 2) -> Disposition:
    sources = {e.source for e in evidence if e.signed and e.fresh}
    return Disposition.ENFORCE_LICENSE if len(sources) >= required_sources else Disposition.NO_CONCLUSION


def deny_all(evidence: list[Evidence]) -> Disposition:
    return Disposition.DENY_ALL


def strong_peer_typed_evidence_schema(evidence: list[Evidence]) -> Disposition:
    for e in evidence:
        if p1_supports_required_proposition(e):
            return Disposition.ENFORCE_LICENSE
    return Disposition.NO_CONCLUSION
