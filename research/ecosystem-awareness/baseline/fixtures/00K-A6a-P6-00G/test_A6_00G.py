from ablation_A6_00G import *


def branch_f():
    claims = tuple(Claim(f"R{i}", "SRC_N", True, .97) for i in range(5))
    return FrameFixture(claims, transition_authority_applicable=False)


def branch_g():
    claims = tuple(Claim(f"R{i}", f"SRC_{i}", True, .97) for i in range(5))
    return FrameFixture(claims, transition_authority_applicable=True)


def test_route_q_rejects_false_frame():
    assert route_q(branch_f()) == Disposition.DENY


def test_route_q_accepts_genuine_change():
    assert route_q(branch_g()) == Disposition.EXECUTE


def test_identity_quorum_fails_false_branch():
    assert identity_quorum_without_p6(branch_f()) == Disposition.EXECUTE


def test_confidence_threshold_fails_false_branch():
    assert confidence_without_p6(branch_f()) == Disposition.EXECUTE


def test_provenance_preserved_but_not_composed_still_fails_false_branch():
    assert provenance_preserving_but_identity_counting(branch_f()) == Disposition.EXECUTE


def test_deny_all_blocks_false_branch():
    assert deny_all(branch_f()) == Disposition.DENY


def test_deny_all_fails_genuine_change_positive_control():
    assert deny_all(branch_g()) != Disposition.EXECUTE


def test_authority_only_is_true_substitute_on_frozen_F_G_pair():
    assert authority_only_without_p6(branch_f()) == Disposition.DENY
    assert authority_only_without_p6(branch_g()) == Disposition.EXECUTE


def test_authority_only_does_not_use_p6_observable():
    independent_but_unauthorized = FrameFixture(
        tuple(Claim(f"R{i}", f"SRC_{i}", True, .97) for i in range(5)),
        False,
    )
    assert (
        authority_only_without_p6(branch_f())
        == authority_only_without_p6(independent_but_unauthorized)
    )


def test_result_is_counterexample_to_P6_necessity_for_this_specific_pair():
    assert authority_only_without_p6(branch_f()) == route_q(branch_f())
    assert authority_only_without_p6(branch_g()) == route_q(branch_g())
