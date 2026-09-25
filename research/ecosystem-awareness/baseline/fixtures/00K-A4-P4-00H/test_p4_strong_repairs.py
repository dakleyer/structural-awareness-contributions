import pytest
from p4_strong_repairs import *


def test_U_G_are_identical_on_P4_blind_surface():
    assert p4_blind_signature(U) == p4_blind_signature(G)


def test_expected_oracle_is_opposite_on_matched_U_G():
    assert expected(U) == Disposition.RECONTRACT
    assert expected(G) == Disposition.EXECUTE


def test_no_deterministic_signature_only_policy_can_pass_U_and_G():
    for out in enumerate_signature_only_policies():
        assert not (out == expected(U) and out == expected(G))


@pytest.mark.parametrize(
    "repair", [leaf_rbac, nonowner_human_approval, campaign_execute_all]
)
def test_leaf_or_nonowner_repairs_false_execute_U(repair):
    assert repair(U) == Disposition.EXECUTE


@pytest.mark.parametrize(
    "repair", [leaf_rbac, nonowner_human_approval, campaign_execute_all]
)
def test_leaf_or_nonowner_repairs_allow_G(repair):
    assert repair(G) == Disposition.EXECUTE


@pytest.mark.parametrize("cap", [1, 10, 100, 1000, 3999, 4000, 5000, 10000])
def test_rate_cap_cannot_distinguish_matched_U_G(cap):
    assert rate_cap(U, cap) == rate_cap(G, cap)


@pytest.mark.parametrize(
    "cap", [100, 1000, 10000, 100000, 239999, 240000, 500000]
)
def test_aggregate_cap_cannot_distinguish_matched_U_G(cap):
    assert aggregate_cap(U, cap) == aggregate_cap(G, cap)


@pytest.mark.parametrize(
    "threshold", [0.0, 0.2, 0.41, 0.42, 0.43, 0.5, 0.9, 1.0]
)
def test_risk_gate_cannot_distinguish_matched_U_G(threshold):
    assert risk_gate(U, threshold) == risk_gate(G, threshold)


def test_campaign_block_all_is_safe_on_U_but_fails_G():
    assert campaign_block_all(U) == Disposition.RECONTRACT
    assert campaign_block_all(G) != Disposition.EXECUTE


def test_static_campaign_allowlist_false_executes_U():
    assert static_campaign_allowlist(U) == Disposition.EXECUTE
    assert static_campaign_allowlist(G) == Disposition.EXECUTE


def test_opaque_PDP_passes_U_G_I_NM():
    pdp = OpaquePDP()
    for b in [U, G, I, NM]:
        assert pdp.decide(b) == expected(b)


def test_opaque_PDP_does_not_return_delegation_history():
    p = OpaquePDP().permit(G)
    assert isinstance(p, ScopedPermit)
    assert not hasattr(p, "delegation_chain")
    assert not hasattr(p, "history")


def test_scoped_PDP_permit_passes_G():
    p = OpaquePDP().permit(G)
    assert decision_from_permit(G, p) == Disposition.EXECUTE


def test_absent_PDP_permit_blocks_U_without_denying_I():
    assert decision_from_permit(U, OpaquePDP().permit(U)) == Disposition.RECONTRACT
    assert decision_from_permit(I, None) == Disposition.EXECUTE


def test_stale_or_invalid_PDP_permit_does_not_execute():
    p = ScopedPermit("CAMP-X", 4000, 240000.0, False)
    assert decision_from_permit(G, p) == Disposition.RECONTRACT


def test_wrong_campaign_PDP_permit_does_not_execute():
    p = ScopedPermit("OTHER", 4000, 240000.0, True)
    assert decision_from_permit(G, p) == Disposition.RECONTRACT


def test_under_scoped_PDP_permit_does_not_execute():
    p = ScopedPermit("CAMP-X", 100, 1000.0, True)
    assert decision_from_permit(G, p) == Disposition.RECONTRACT


def test_capability_token_passes_G_and_blocks_U():
    cap = Capability("CAMP-X", 4000, 240000.0, True)
    assert decision_from_capability(G, cap) == Disposition.EXECUTE
    assert decision_from_capability(U, None) == Disposition.RECONTRACT


def test_capability_caveats_enforce_non_amplification():
    cap = Capability("CAMP-X", 100, 1000.0, True)
    assert decision_from_capability(G, cap) == Disposition.RECONTRACT


def test_legitimate_maker_checker_passes_G_and_blocks_U():
    assert maker_checker(G, True) == Disposition.EXECUTE
    assert maker_checker(U, True) == Disposition.RECONTRACT


def test_nonowner_maker_checker_cannot_create_authority():
    assert maker_checker(G, False) == Disposition.RECONTRACT
    assert maker_checker(U, False) == Disposition.RECONTRACT


def test_blind_repairs_have_no_true_substitute():
    repairs = [
        leaf_rbac,
        nonowner_human_approval,
        campaign_execute_all,
        campaign_block_all,
        static_campaign_allowlist,
    ]
    winners = []
    for fn in repairs:
        if fn(U) == expected(U) and fn(G) == expected(G) and fn(I) == expected(I):
            winners.append(fn.__name__)
    assert winners == []


def test_minimal_scoped_attestation_is_sufficient_without_full_lineage():
    pdp = OpaquePDP()
    p = pdp.permit(G)
    assert decision_from_permit(G, p) == Disposition.EXECUTE
    assert p.issuer == "FINOPS-PDP"
    assert not hasattr(p, "delegation_chain")
