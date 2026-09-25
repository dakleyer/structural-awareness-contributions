from ablation_A3 import (
    Disposition, CorridorState, route_q, ablated_majority_default_normal,
    ablated_timeout_default_normal, ablated_p6_detect_conflict_then_choose_normal,
    ablated_p4_preserve_all_postures_then_choose_normal,
    ablated_p5_refresh_then_choose_normal, deny_all,
    strong_peer_three_valued_closure,
)


def conflict_branch():
    return CorridorState(("PLAN_A", "PLAN_B", "NORMAL", "HOLD"), True, True, True)


def continuity_branch():
    return CorridorState(("NORMAL", "NORMAL", "NORMAL", "NORMAL"), False, True, True)


def authorized_plan_a_branch():
    return CorridorState(("PLAN_A", "PLAN_A", "PLAN_A"), True, True, True)


def test_route_q_holds_unresolved_conflict():
    assert route_q(conflict_branch()) == Disposition.HOLD_REQUALIFY


def test_route_q_executes_continuity():
    assert route_q(continuity_branch()) == Disposition.EXECUTE_NORMAL


def test_route_q_allows_determinate_authorized_plan_a():
    assert route_q(authorized_plan_a_branch()) == Disposition.EXECUTE_PLAN_A


def test_majority_default_false_closes_conflict():
    assert ablated_majority_default_normal(conflict_branch()) == Disposition.EXECUTE_NORMAL


def test_timeout_default_false_closes_conflict():
    assert ablated_timeout_default_normal(conflict_branch()) == Disposition.EXECUTE_NORMAL


def test_P6_conflict_detection_without_P3_still_false_closes():
    assert ablated_p6_detect_conflict_then_choose_normal(conflict_branch()) == Disposition.EXECUTE_NORMAL


def test_P4_full_preservation_without_P3_still_false_closes():
    assert ablated_p4_preserve_all_postures_then_choose_normal(conflict_branch()) == Disposition.EXECUTE_NORMAL


def test_P5_freshness_without_P3_still_false_closes():
    assert ablated_p5_refresh_then_choose_normal(conflict_branch()) == Disposition.EXECUTE_NORMAL


def test_deny_all_blocks_conflict_but_fails_continuity():
    assert deny_all(conflict_branch()) == Disposition.DENY_ALL
    assert deny_all(continuity_branch()) != Disposition.EXECUTE_NORMAL


def test_strong_peer_reconstruction_holds_conflict():
    assert strong_peer_three_valued_closure(conflict_branch()) == Disposition.HOLD_REQUALIFY


def test_strong_peer_reconstruction_preserves_continuity():
    assert strong_peer_three_valued_closure(continuity_branch()) == Disposition.EXECUTE_NORMAL


def test_strong_peer_reconstruction_allows_determinate_plan_a():
    assert strong_peer_three_valued_closure(authorized_plan_a_branch()) == Disposition.EXECUTE_PLAN_A


def test_no_true_substitute_in_tested_P3_blind_repairs():
    repairs = [
        ablated_majority_default_normal, ablated_timeout_default_normal,
        ablated_p6_detect_conflict_then_choose_normal,
        ablated_p4_preserve_all_postures_then_choose_normal,
        ablated_p5_refresh_then_choose_normal, deny_all,
    ]
    true_substitutes = []
    for fn in repairs:
        correct_bad = fn(conflict_branch()) == Disposition.HOLD_REQUALIFY
        correct_good = fn(continuity_branch()) == Disposition.EXECUTE_NORMAL
        if correct_bad and correct_good:
            true_substitutes.append(fn)
    assert true_substitutes == []
