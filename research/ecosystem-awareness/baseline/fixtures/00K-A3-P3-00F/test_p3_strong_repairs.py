import pytest
from p3_strong_repairs import (
    Disposition, Signal, matched_conflict, positive_plan_a, positive_normal,
    old_confounded_branch, old_hold_marker_shortcut, authority_priority,
    confidence_priority, freshest_priority, majority_default_normal,
    human_approval_without_new_evidence, timeout_default_normal,
    risk_priority_plan_a, supermajority_nonpermission, unanimity_gate,
    robust_action_intersection, explicit_unresolved_containment,
    correct_conflict, correct_a, correct_normal,
)

def test_old_base_conflict_is_confounded_by_explicit_HOLD_marker():
    assert old_hold_marker_shortcut(old_confounded_branch()) == Disposition.HOLD_REQUALIFY
    assert old_hold_marker_shortcut(positive_plan_a()) == Disposition.EXECUTE_PLAN_A
    assert old_hold_marker_shortcut(positive_normal()) == Disposition.EXECUTE_NORMAL

def test_corrected_conflict_removes_HOLD_marker_shortcut():
    assert all(s.posture != "HOLD" for s in matched_conflict())
    assert not correct_conflict(old_hold_marker_shortcut(matched_conflict()))

def test_matched_conflict_equalizes_authority_confidence_freshness():
    s = matched_conflict()
    assert len({x.authority_rank for x in s}) == 1
    assert len({x.confidence for x in s}) == 1
    assert len({x.fresh for x in s}) == 1

@pytest.mark.parametrize("repair", [
    authority_priority, confidence_priority, freshest_priority,
    majority_default_normal, human_approval_without_new_evidence,
    timeout_default_normal, risk_priority_plan_a,
])
def test_priority_default_repairs_false_close_matched_conflict(repair):
    assert not correct_conflict(repair(matched_conflict()))

@pytest.mark.parametrize("repair", [
    authority_priority, confidence_priority, freshest_priority,
    human_approval_without_new_evidence, risk_priority_plan_a,
])
def test_priority_repairs_still_allow_plan_a_positive(repair):
    assert correct_a(repair(positive_plan_a()))

def test_majority_default_allows_uniform_positive_controls():
    assert correct_a(majority_default_normal(positive_plan_a()))
    assert correct_normal(majority_default_normal(positive_normal()))

@pytest.mark.parametrize("threshold", [0.51,0.6,0.66,0.75,0.9,1.0])
def test_supermajority_gate_holds_equal_conflict_and_allows_uniform_positive(threshold):
    assert correct_conflict(supermajority_nonpermission(matched_conflict(),threshold))
    assert correct_a(supermajority_nonpermission(positive_plan_a(),threshold))
    assert correct_normal(supermajority_nonpermission(positive_normal(),threshold))

def test_unanimity_gate_passes_all_matched_controls_but_reconstructs_P3():
    assert correct_conflict(unanimity_gate(matched_conflict()))
    assert correct_a(unanimity_gate(positive_plan_a()))
    assert correct_normal(unanimity_gate(positive_normal()))

def test_robust_action_intersection_passes_without_false_certainty_but_is_P3_action_level_reconstruction():
    assert correct_conflict(robust_action_intersection(matched_conflict()))
    assert correct_a(robust_action_intersection(positive_plan_a()))
    assert correct_normal(robust_action_intersection(positive_normal()))

def test_explicit_unresolved_containment_passes_controls():
    assert correct_conflict(explicit_unresolved_containment(matched_conflict()))
    assert correct_a(explicit_unresolved_containment(positive_plan_a()))
    assert correct_normal(explicit_unresolved_containment(positive_normal()))

@pytest.mark.parametrize("width", [2,4,6,8])
def test_equal_split_conflict_defeats_majority_and_priority_shortcuts(width):
    sigs = tuple(
        [Signal("PLAN_A") for _ in range(width//2)] +
        [Signal("PLAN_B") for _ in range(width//2)]
    )
    assert not correct_conflict(authority_priority(sigs))
    assert not correct_conflict(confidence_priority(sigs))
    assert not correct_conflict(majority_default_normal(sigs))
    assert correct_conflict(unanimity_gate(sigs))
    assert correct_conflict(robust_action_intersection(sigs))

@pytest.mark.parametrize("a_count,b_count", [(1,3),(3,1),(2,4),(4,2)])
def test_non_tied_mixed_conflicts_defeat_simple_majority_but_nonpermission_gate_holds(a_count,b_count):
    sigs = tuple([Signal("PLAN_A")]*a_count + [Signal("PLAN_B")]*b_count)
    assert not correct_conflict(majority_default_normal(sigs))
    assert correct_conflict(unanimity_gate(sigs))
    assert correct_conflict(robust_action_intersection(sigs))

def test_no_true_substitute_in_serious_P3_blind_repair_set():
    blind = [
        authority_priority, confidence_priority, freshest_priority,
        majority_default_normal, human_approval_without_new_evidence,
        timeout_default_normal, risk_priority_plan_a,
    ]
    winners=[]
    for fn in blind:
        if correct_conflict(fn(matched_conflict())) and correct_a(fn(positive_plan_a())) and correct_normal(fn(positive_normal())):
            winners.append(fn.__name__)
    assert winners == []
