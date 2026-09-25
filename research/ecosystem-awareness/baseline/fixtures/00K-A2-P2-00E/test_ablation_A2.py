from ablation_A2 import (
    Disposition, EvidenceStep, SearchFixture, route_q_bounded_search,
    ablated_search_until_capacity, ablated_p1_explicit_unknown_but_keep_searching,
    ablated_p3_no_false_closure_but_keep_holding,
    ablated_p4_perfect_handoff_but_keep_searching,
    fixed_timeout_deny_all, strong_peer_budgeted_search,
)


def unresolved_branch():
    return SearchFixture(tuple(EvidenceStep(False, False) for _ in range(10)), 6, 6)


def resolvable_branch():
    return SearchFixture((
        EvidenceStep(False, False),
        EvidenceStep(True, False),
        EvidenceStep(True, True),
        EvidenceStep(False, False),
    ), 6, 6)


def test_route_q_closes_unresolved_branch_without_capacity_exhaustion():
    assert route_q_bounded_search(unresolved_branch(), 3) == Disposition.NO_CONCLUSION


def test_route_q_reaches_resolution_on_positive_branch():
    assert route_q_bounded_search(resolvable_branch(), 3) == Disposition.EXECUTE


def test_unbounded_search_exhausts_capacity():
    assert ablated_search_until_capacity(unresolved_branch()) == Disposition.RESOURCE_EXHAUSTED


def test_P1_unknown_preservation_alone_does_not_bound_effort():
    assert ablated_p1_explicit_unknown_but_keep_searching(unresolved_branch()) == Disposition.RESOURCE_EXHAUSTED


def test_P3_no_false_closure_alone_does_not_bound_effort():
    assert ablated_p3_no_false_closure_but_keep_holding(unresolved_branch()) == Disposition.RESOURCE_EXHAUSTED


def test_P4_perfect_handoff_alone_does_not_bound_effort():
    assert ablated_p4_perfect_handoff_but_keep_searching(unresolved_branch()) == Disposition.RESOURCE_EXHAUSTED


def test_fixed_timeout_blocks_negative_but_fails_resolvable_positive_branch():
    assert fixed_timeout_deny_all(unresolved_branch(), 1) == Disposition.DENY_ALL
    assert fixed_timeout_deny_all(resolvable_branch(), 1) != Disposition.EXECUTE


def test_strong_peer_budgeted_search_closes_negative():
    assert strong_peer_budgeted_search(unresolved_branch(), 3) == Disposition.NO_CONCLUSION


def test_strong_peer_budgeted_search_allows_positive_resolution():
    assert strong_peer_budgeted_search(resolvable_branch(), 3) == Disposition.EXECUTE


def test_budget_sweep_shows_positive_requires_enough_but_finite_effort():
    fixture = resolvable_branch()
    assert strong_peer_budgeted_search(fixture, 1) == Disposition.NO_CONCLUSION
    assert strong_peer_budgeted_search(fixture, 2) == Disposition.NO_CONCLUSION
    assert strong_peer_budgeted_search(fixture, 3) == Disposition.EXECUTE


def test_no_true_substitute_in_tested_P2_blind_repairs():
    repairs = [
        ablated_search_until_capacity,
        ablated_p1_explicit_unknown_but_keep_searching,
        ablated_p3_no_false_closure_but_keep_holding,
        ablated_p4_perfect_handoff_but_keep_searching,
        lambda f: fixed_timeout_deny_all(f, 1),
    ]
    true_substitutes = []
    for fn in repairs:
        correct_negative = fn(unresolved_branch()) == Disposition.NO_CONCLUSION
        correct_positive = fn(resolvable_branch()) == Disposition.EXECUTE
        if correct_negative and correct_positive:
            true_substitutes.append(fn)
    assert true_substitutes == []
