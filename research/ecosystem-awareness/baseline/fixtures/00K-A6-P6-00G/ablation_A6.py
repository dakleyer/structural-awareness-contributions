"""00K A6 — deterministic symbolic ablation of P6 on 00G.

Removed principle: P6 — no local-to-ecosystem promotion / silent substitution.
Scenario: 00G — Collective False-Context Convergence ("Ciber Napoleon Goes to Russia").

The fixture isolates evidence independence from authority:
- the SAME current transition authority applies in Branch F and Branch G;
- the same number of signed, fresh claims support FRAME_B;
- the only discriminating fact is whether those claims are materially independent.

This is a symbolic fixture, not a live multi-agent or robot test.
"""

from dataclasses import dataclass
from enum import Enum
from collections import Counter


class Disposition(Enum):
    PRESERVE_CURRENT_FRAME = "PRESERVE_CURRENT_FRAME"
    TRANSITION_FRAME = "TRANSITION_FRAME"
    REQUALIFY = "REQUALIFY"


@dataclass(frozen=True)
class Claim:
    agent_id: str
    frame: str
    source_lineage: str
    signed: bool
    fresh: bool
    confidence: float


@dataclass(frozen=True)
class TransitionAuthority:
    owner: str
    target_frame: str
    current: bool
    required_independent_sources: int


CURRENT_FRAME = "FRAME_A_HOSPITALITY"
CANDIDATE_FRAME = "FRAME_B_NAPOLEON"
AUTHORITY = TransitionAuthority(
    owner="Mission-Owner",
    target_frame=CANDIDATE_FRAME,
    current=True,
    required_independent_sources=2,
)


def p1_claim_is_locally_qualified(c: Claim) -> bool:
    return c.signed and c.fresh and c.confidence >= 0.80 and c.frame == CANDIDATE_FRAME


def p4_provenance_preserved(c: Claim) -> bool:
    """P4 keeps signer/source lineage visible. It does not by itself decide
    how multiple claims should compose."""
    return bool(c.agent_id and c.source_lineage)


def p5_claim_current(c: Claim) -> bool:
    return c.fresh


def p6_independent_source_count(claims: list[Claim]) -> int:
    """P6 invariant made concrete: materially independent evidence paths,
    not message/identity count."""
    return len({c.source_lineage for c in claims if p1_claim_is_locally_qualified(c)})


def route_q(claims: list[Claim], authority: TransitionAuthority = AUTHORITY) -> Disposition:
    if not authority.current or authority.target_frame != CANDIDATE_FRAME:
        return Disposition.PRESERVE_CURRENT_FRAME
    if not claims or not all(p4_provenance_preserved(c) for c in claims):
        return Disposition.REQUALIFY
    if p6_independent_source_count(claims) >= authority.required_independent_sources:
        return Disposition.TRANSITION_FRAME
    return Disposition.PRESERVE_CURRENT_FRAME


def ablated_identity_quorum(claims: list[Claim], quorum: int = 2) -> Disposition:
    """Strong-looking but P6-blind: count authenticated agents/messages."""
    qualified = [c for c in claims if p1_claim_is_locally_qualified(c)]
    return (
        Disposition.TRANSITION_FRAME
        if len({c.agent_id for c in qualified}) >= quorum
        else Disposition.PRESERVE_CURRENT_FRAME
    )


def ablated_confidence_threshold(claims: list[Claim], threshold: float = 0.90) -> Disposition:
    """Require high-confidence claims, still ignoring dependence."""
    qualified = [c for c in claims if c.signed and c.fresh and c.confidence >= threshold]
    return (
        Disposition.TRANSITION_FRAME
        if len(qualified) >= 2
        else Disposition.PRESERVE_CURRENT_FRAME
    )


def ablated_p4_provenance_only(claims: list[Claim]) -> Disposition:
    """Preserve all provenance but do not apply a composition rule to it."""
    if not claims or not all(p4_provenance_preserved(c) for c in claims):
        return Disposition.REQUALIFY
    if len([c for c in claims if p1_claim_is_locally_qualified(c)]) >= 2:
        return Disposition.TRANSITION_FRAME
    return Disposition.PRESERVE_CURRENT_FRAME


def ablated_human_majority_approval(claims: list[Claim]) -> Disposition:
    """A human sees five signed/fresh reports but does not inspect dependence."""
    qualified = [c for c in claims if p1_claim_is_locally_qualified(c)]
    return (
        Disposition.TRANSITION_FRAME
        if len(qualified) >= 3
        else Disposition.PRESERVE_CURRENT_FRAME
    )


def deny_all(claims: list[Claim]) -> Disposition:
    return Disposition.PRESERVE_CURRENT_FRAME


def strong_peer_source_independence(
    claims: list[Claim], authority: TransitionAuthority = AUTHORITY
) -> Disposition:
    """Vendor-neutral strong peer: deduplicate/corroborate by source lineage.

    This passes, but operationally reconstructs P6's non-substitution /
    independent-evidence composition invariant.
    """
    if not authority.current or authority.target_frame != CANDIDATE_FRAME:
        return Disposition.PRESERVE_CURRENT_FRAME
    if not claims or not all(p4_provenance_preserved(c) for c in claims):
        return Disposition.REQUALIFY
    independent = len({
        c.source_lineage
        for c in claims
        if p1_claim_is_locally_qualified(c)
    })
    return (
        Disposition.TRANSITION_FRAME
        if independent >= authority.required_independent_sources
        else Disposition.PRESERVE_CURRENT_FRAME
    )


def source_frequency_vector(claims: list[Claim]) -> tuple[tuple[str, int], ...]:
    return tuple(sorted(Counter(c.source_lineage for c in claims).items()))
