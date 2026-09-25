"""Bounded-grid hardening for 00K A2 / P2–00E."""
from ablation_A2 import (
    Disposition, EvidenceStep, SearchFixture,
    ablated_search_until_capacity, strong_peer_budgeted_search,
)


def fixture_resolves_at(k, capacity=8):
    stream = tuple(
        EvidenceStep(decision_relevant=(i >= k - 1), resolves=(i == k - 1))
        for i in range(capacity)
    )
    return SearchFixture(stream, hard_capacity=capacity, useful_horizon=capacity)


def unresolved(capacity=8):
    return SearchFixture(
        tuple(EvidenceStep(False, False) for _ in range(capacity + 3)),
        hard_capacity=capacity,
        useful_horizon=capacity,
    )


def test_budget_resolution_grid_has_exact_finite_boundary():
    for resolve_at in range(1, 7):
        f = fixture_resolves_at(resolve_at)
        for budget in range(1, 8):
            expected = Disposition.EXECUTE if budget >= resolve_at else Disposition.NO_CONCLUSION
            assert strong_peer_budgeted_search(f, budget) == expected


def test_unresolved_grid_closes_without_resource_exhaustion_only_with_bound():
    for capacity in range(2, 9):
        f = unresolved(capacity)
        assert ablated_search_until_capacity(f) == Disposition.RESOURCE_EXHAUSTED
        for budget in range(1, capacity + 1):
            assert strong_peer_budgeted_search(f, budget) == Disposition.NO_CONCLUSION
