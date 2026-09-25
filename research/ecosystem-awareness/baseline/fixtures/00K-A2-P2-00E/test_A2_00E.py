from ablation_A2_00E import *


def resolvable():
    return SearchFixture((False, True, True, True, True), deadline_steps=5)


def unresolved():
    return SearchFixture((False, False, False, False, False, False), deadline_steps=5)


def test_route_q_executes_resolvable_case():
    assert route_q_p2(resolvable()) == Disposition.EXECUTE


def test_route_q_closes_unresolved_case_before_deadline():
    assert route_q_p2(unresolved()) == Disposition.NO_COMMITMENT


def test_unbounded_search_resolves_when_lucky():
    assert ablated_keep_searching(resolvable()) == Disposition.EXECUTE


def test_unbounded_search_misses_viable_closure_on_unresolved_case():
    assert ablated_keep_searching(unresolved()) == Disposition.STILL_SEARCHING


def test_more_reviewers_does_not_create_stop_rule():
    assert ablated_more_reviewers(unresolved()) == Disposition.STILL_SEARCHING


def test_timeout_default_forces_false_closure_when_unresolved():
    assert timeout_default_execute(unresolved()) == Disposition.FORCED_EXECUTE


def test_timeout_default_executes_resolvable_case_if_evidence_arrives():
    assert timeout_default_execute(resolvable()) == Disposition.EXECUTE


def test_deny_all_closes_unresolved_case():
    assert deny_all(unresolved()) == Disposition.NO_COMMITMENT


def test_deny_all_fails_resolvable_positive_control():
    assert deny_all(resolvable()) != Disposition.EXECUTE


def test_fixed_budget_peer_passes_both_branches():
    assert fixed_budget_peer(resolvable()) == Disposition.EXECUTE
    assert fixed_budget_peer(unresolved()) == Disposition.NO_COMMITMENT


def test_fixed_budget_peer_reconstructs_p2_semantics():
    assert fixed_budget_peer(unresolved(), budget_steps=2) == Disposition.NO_COMMITMENT
