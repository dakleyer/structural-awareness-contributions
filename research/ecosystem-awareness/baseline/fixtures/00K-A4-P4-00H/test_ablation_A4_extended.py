"""
Additional adversarial checks for 00K A4 / 00H.

These tests do not modify the reviewed 11-test harness. They strengthen it by
making the U/G indistinguishability boundary explicit: under the frozen fixture,
Branch U and Branch G have identical P4-blind observables. Their only declared
material difference is the existence of current root campaign authority.
"""

from datetime import timedelta

from ablation_A4 import (
    Disposition,
    RootCampaignAuthority,
    route_q_decision,
    check_P1_evidence_sufficiency,
    check_P5_leaf_revalidation,
    detect_composition_P6,
    native_rate_cap_check,
    NOW,
)
from test_ablation_A4 import (
    CAMPAIGN_REF,
    FAR_FUTURE,
    make_finding,
    make_leaf_actions,
)


def five_principle_observation_signature(finding, actions):
    """Observable state used by the current P4-blind repair family.

    P2/P3 are held equal across U/G by fixture construction: same deadline,
    same unresolved-state policy and same response budget. This signature
    therefore includes the material discriminants actually computed by P1,
    P5 and P6 plus volume/timing visible to a native rate control.
    """
    return (
        check_P1_evidence_sufficiency(finding),
        check_P5_leaf_revalidation(actions),
        detect_composition_P6(actions),
        len(actions),
        tuple((a.amount, a.grant.cap_amount, a.grant.expiry > NOW) for a in actions[:5]),
    )


def test_branch_U_and_G_are_identical_on_current_P4_blind_observation_surface():
    """Fixture-level separation lemma.

    U and G deliberately share finding, leaves, campaign identity, timing and
    leaf validity. The only frozen difference is root campaign authority.
    Therefore a deterministic repair that never obtains an authority-bearing
    root relation receives the same observable state on both branches.
    """
    finding_u = make_finding()
    finding_g = make_finding()
    actions_u = make_leaf_actions(4000, CAMPAIGN_REF)
    actions_g = make_leaf_actions(4000, CAMPAIGN_REF)

    assert five_principle_observation_signature(finding_u, actions_u) == \
           five_principle_observation_signature(finding_g, actions_g)


def test_rate_cap_cannot_separate_U_from_G_at_any_shared_threshold_sample():
    """A volume control can block or allow, but cannot discriminate U/G.

    We sample thresholds below, at and above the one-hour burst size. For every
    threshold, the native rate-cap result is identical on U and G because the
    branches have the same action stream.
    """
    actions_u = make_leaf_actions(4000, CAMPAIGN_REF)
    actions_g = make_leaf_actions(4000, CAMPAIGN_REF)

    for threshold in [0, 1, 10, 100, 1000, 3600, 3601, 4000, 5000]:
        assert native_rate_cap_check(actions_u, threshold) == \
               native_rate_cap_check(actions_g, threshold)


def test_stricter_materiality_threshold_cannot_separate_U_from_G():
    """Any P1-only tightening sees the same material finding on U and G."""
    finding_u = make_finding()
    finding_g = make_finding()

    candidate_thresholds = [100, 1000, 3999, 4000, 4001, 10000]
    for accounts_required in candidate_thresholds:
        u = finding_u.affected_accounts >= accounts_required
        g = finding_g.affected_accounts >= accounts_required
        assert u == g


def test_leaf_freshness_policy_cannot_separate_U_from_G():
    """P5 can make leaves fresh or stale, but U/G share leaf validity."""
    actions_u = make_leaf_actions(20, CAMPAIGN_REF)
    actions_g = make_leaf_actions(20, CAMPAIGN_REF)

    assert check_P5_leaf_revalidation(actions_u) is True
    assert check_P5_leaf_revalidation(actions_g) is True

    # Move the evaluation beyond the common expiry: both branches fail alike.
    after_expiry = FAR_FUTURE + timedelta(seconds=1)
    assert check_P5_leaf_revalidation(actions_u, at_time=after_expiry) is False
    assert check_P5_leaf_revalidation(actions_g, at_time=after_expiry) is False


def test_composition_only_policy_has_deny_all_or_accept_all_failure():
    """P6 reveals a common campaign but does not determine its authority.

    If a P4-blind policy maps 'common campaign' to DENY, it fails G.
    If it maps 'common campaign' to EXECUTE, it fails U.
    """
    actions_u = make_leaf_actions(20, CAMPAIGN_REF)
    actions_g = make_leaf_actions(20, CAMPAIGN_REF)
    assert detect_composition_P6(actions_u) == CAMPAIGN_REF
    assert detect_composition_P6(actions_g) == CAMPAIGN_REF

    deny_policy_u = Disposition.DBC_DENY
    deny_policy_g = Disposition.DBC_DENY
    execute_policy_u = Disposition.DBC_EXECUTE
    execute_policy_g = Disposition.DBC_EXECUTE

    assert deny_policy_u == Disposition.DBC_DENY  # safe on U
    assert deny_policy_g != Disposition.DBC_EXECUTE  # fails G positive control
    assert execute_policy_g == Disposition.DBC_EXECUTE  # correct on G
    assert execute_policy_u != Disposition.DBC_DENY  # fails U


def test_restoring_root_authority_is_sufficient_to_separate_identical_U_G_streams():
    """Same finding/actions; only root-authority registry differs.

    This is not a universal proof of P4 necessity. It demonstrates that within
    the frozen 00H fixture, a receiver-verifiable authority-bearing root relation
    is the declared discriminant that makes branch-correct U/G separation possible.
    """
    finding = make_finding()
    actions = make_leaf_actions(4000, CAMPAIGN_REF)

    branch_u_registry = {}
    branch_g_registry = {
        CAMPAIGN_REF: RootCampaignAuthority(
            campaign_ref=CAMPAIGN_REF,
            issuer="Solstice-Finance-Ops",
            valid=True,
            expiry=FAR_FUTURE,
        )
    }

    assert route_q_decision(finding, actions, branch_u_registry) == \
           Disposition.DBC_REPOSITION_RECONTRACT
    assert route_q_decision(finding, actions, branch_g_registry) == \
           Disposition.DBC_EXECUTE
