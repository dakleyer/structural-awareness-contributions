from ablation_A6 import (
    Disposition,
    Claim,
    AUTHORITY,
    CANDIDATE_FRAME,
    route_q,
    ablated_identity_quorum,
    ablated_confidence_threshold,
    ablated_p4_provenance_only,
    ablated_human_majority_approval,
    deny_all,
    strong_peer_source_independence,
    source_frequency_vector,
)


def false_branch_F():
    return [
        Claim(f"agent-{i}", CANDIDATE_FRAME, "SRC_N", True, True, 0.95)
        for i in range(5)
    ]


def genuine_branch_G():
    sources = ["SRC_A", "SRC_B", "SRC_C", "SRC_A", "SRC_B"]
    return [
        Claim(f"agent-{i}", CANDIDATE_FRAME, sources[i], True, True, 0.95)
        for i in range(5)
    ]


def test_route_q_preserves_current_frame_on_false_correlated_branch_F():
    assert route_q(false_branch_F()) == Disposition.PRESERVE_CURRENT_FRAME


def test_route_q_allows_genuine_regime_transition_on_branch_G():
    assert route_q(genuine_branch_G()) == Disposition.TRANSITION_FRAME


def test_identity_quorum_false_transitions_branch_F():
    assert ablated_identity_quorum(false_branch_F(), quorum=2) == Disposition.TRANSITION_FRAME


def test_identity_quorum_also_transitions_branch_G():
    assert ablated_identity_quorum(genuine_branch_G(), quorum=2) == Disposition.TRANSITION_FRAME


def test_high_confidence_threshold_does_not_fix_correlation():
    assert ablated_confidence_threshold(false_branch_F(), 0.90) == Disposition.TRANSITION_FRAME


def test_P4_provenance_only_keeps_lineage_but_false_transitions_without_P6():
    assert ablated_p4_provenance_only(false_branch_F()) == Disposition.TRANSITION_FRAME


def test_human_majority_approval_false_transitions_branch_F():
    assert ablated_human_majority_approval(false_branch_F()) == Disposition.TRANSITION_FRAME


def test_deny_all_is_safe_on_F_but_fails_G_positive_control():
    assert deny_all(false_branch_F()) == Disposition.PRESERVE_CURRENT_FRAME
    assert deny_all(genuine_branch_G()) != Disposition.TRANSITION_FRAME


def test_strong_peer_source_independence_blocks_F():
    assert strong_peer_source_independence(false_branch_F()) == Disposition.PRESERVE_CURRENT_FRAME


def test_strong_peer_source_independence_allows_G():
    assert strong_peer_source_independence(genuine_branch_G()) == Disposition.TRANSITION_FRAME


def test_same_identity_count_confidence_freshness_and_authority_on_F_and_G():
    f = false_branch_F()
    g = genuine_branch_G()
    assert len(f) == len(g) == 5
    assert [c.agent_id for c in f] == [c.agent_id for c in g]
    assert [c.signed for c in f] == [c.signed for c in g]
    assert [c.fresh for c in f] == [c.fresh for c in g]
    assert [c.confidence for c in f] == [c.confidence for c in g]
    assert AUTHORITY == AUTHORITY


def test_only_source_dependence_structure_differs_in_declared_fixture():
    assert source_frequency_vector(false_branch_F()) == (("SRC_N", 5),)
    assert source_frequency_vector(genuine_branch_G()) == (
        ("SRC_A", 2), ("SRC_B", 2), ("SRC_C", 1)
    )


def test_quorum_threshold_sweep_cannot_separate_F_and_G():
    f = false_branch_F()
    g = genuine_branch_G()
    for q in [1, 2, 3, 4, 5, 6]:
        assert ablated_identity_quorum(f, q) == ablated_identity_quorum(g, q)


def test_confidence_threshold_sweep_cannot_separate_F_and_G():
    f = false_branch_F()
    g = genuine_branch_G()
    for t in [0.0, 0.5, 0.8, 0.9, 0.95, 0.96, 1.0]:
        assert ablated_confidence_threshold(f, t) == ablated_confidence_threshold(g, t)


def test_no_true_substitute_in_tested_P6_blind_repairs():
    repairs = [
        lambda xs: ablated_identity_quorum(xs, 2),
        lambda xs: ablated_confidence_threshold(xs, 0.90),
        ablated_p4_provenance_only,
        ablated_human_majority_approval,
        deny_all,
    ]
    true_substitutes = []
    for fn in repairs:
        correct_f = fn(false_branch_F()) == Disposition.PRESERVE_CURRENT_FRAME
        correct_g = fn(genuine_branch_G()) == Disposition.TRANSITION_FRAME
        if correct_f and correct_g:
            true_substitutes.append(fn)
    assert true_substitutes == []
