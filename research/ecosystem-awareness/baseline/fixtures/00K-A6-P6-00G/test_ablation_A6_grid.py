"""Bounded-grid hardening for 00K A6 / P6–00G."""
from ablation_A6 import (
    Disposition, Claim, CANDIDATE_FRAME, AUTHORITY,
    ablated_identity_quorum, strong_peer_source_independence,
)


def claims(n, source_count):
    sources = [f"SRC-{i}" for i in range(source_count)]
    return [
        Claim(
            agent_id=f"agent-{i}",
            frame=CANDIDATE_FRAME,
            source_lineage=sources[i % source_count],
            signed=True,
            fresh=True,
            confidence=0.95,
        )
        for i in range(n)
    ]


def test_source_diversity_grid_matches_declared_independence_threshold():
    required = AUTHORITY.required_independent_sources
    for n in range(1, 9):
        for source_count in range(1, n + 1):
            result = strong_peer_source_independence(claims(n, source_count))
            expected = (
                Disposition.TRANSITION_FRAME
                if source_count >= required
                else Disposition.PRESERVE_CURRENT_FRAME
            )
            assert result == expected


def test_sybil_scaling_does_not_create_independent_evidence_for_strong_peer():
    for n in range(2, 21):
        xs = claims(n, 1)
        assert strong_peer_source_independence(xs) == Disposition.PRESERVE_CURRENT_FRAME
        assert ablated_identity_quorum(xs, quorum=2) == Disposition.TRANSITION_FRAME
