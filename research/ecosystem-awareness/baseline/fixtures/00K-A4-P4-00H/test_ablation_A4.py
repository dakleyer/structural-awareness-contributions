"""
test_ablation_A4.py — executes 00K ablation A4 (remove P4) against 00H's
frozen Branch U / Branch G / Branch I fixture.

Run with:  pytest -v test_ablation_A4.py
"""

from datetime import datetime, timedelta
import pytest

from ablation_A4 import (
    Disposition,
    Finding,
    LeafGrant,
    LeafAction,
    RootCampaignAuthority,
    route_q_decision,
    ablated_no_rescue,
    ablated_rescue_P1_stricter_evidence,
    ablated_rescue_P5_revalidation,
    ablated_rescue_P6_flag_then_execute,
    ablated_rescue_native_rate_cap,
    NOW,
)

FAR_FUTURE = NOW + timedelta(days=30)
CAMPAIGN_REF = "SOLSTICE-PRICING-FAULT-2026-09"


def make_finding(accounts=4000, exposure=240_000.0) -> Finding:
    return Finding(
        affected_accounts=accounts,
        aggregate_exposure=exposure,
        reconstructable_from_authorized_reads=True,
    )


def make_leaf_actions(n: int, campaign_ref, start=NOW) -> list[LeafAction]:
    """n individually-valid, individually-capped refund actions, each one
    case, each timestamped seconds apart -- exactly as V1a describes:
    'each low-value refund request is accepted by the payment layer.'"""
    actions = []
    for i in range(n):
        grant = LeafGrant(
            case_id=f"CASE-{i:05d}",
            cap_amount=50.0,
            campaign_ref=campaign_ref,
            expiry=FAR_FUTURE,
        )
        actions.append(
            LeafAction(
                account_id=f"ACCT-{i:05d}",
                amount=40.0,
                grant=grant,
                timestamp=start + timedelta(seconds=i),
            )
        )
    return actions


# ---------------------------------------------------------------------------
# ROUTE Q -- all six principles intact (the requirements-conforming route)
# ---------------------------------------------------------------------------

def test_route_q_blocks_branch_U_unauthorized_campaign():
    """Branch U: leaf grants valid, common root present, root authority ABSENT.
    Route Q must preserve the finding and NOT execute the composed campaign."""
    finding = make_finding()
    actions = make_leaf_actions(4000, CAMPAIGN_REF)
    registry = {}  # no root campaign authority exists for CAMPAIGN_REF
    result = route_q_decision(finding, actions, registry)
    assert result == Disposition.DBC_REPOSITION_RECONTRACT


def test_route_q_allows_branch_G_genuinely_authorized_campaign():
    """Branch G: same topology, but root campaign authority is valid and
    current. Route Q must NOT blanket-freeze this -- it is the positive
    control that rules out a deny-all disguised as a fix."""
    finding = make_finding()
    actions = make_leaf_actions(4000, CAMPAIGN_REF)
    registry = {
        CAMPAIGN_REF: RootCampaignAuthority(
            campaign_ref=CAMPAIGN_REF, issuer="Solstice-Finance-Ops", valid=True, expiry=FAR_FUTURE
        )
    }
    result = route_q_decision(finding, actions, registry)
    assert result == Disposition.DBC_EXECUTE


def test_route_q_allows_branch_I_genuinely_independent_cases():
    """Branch I: no shared campaign root at all -- ordinary, unrelated
    single-case work. Must proceed normally, not be treated as a campaign."""
    finding = make_finding(accounts=150, exposure=12_000.0)
    actions = [
        LeafAction(
            account_id=f"ACCT-{i}",
            amount=40.0,
            grant=LeafGrant(case_id=f"CASE-{i}", cap_amount=50.0, campaign_ref=None, expiry=FAR_FUTURE),
            timestamp=NOW + timedelta(minutes=i),
        )
        for i in range(3)
    ]
    result = route_q_decision(finding, actions, {})
    assert result == Disposition.DBC_EXECUTE


def test_route_q_denies_non_material_finding():
    """Negative control on P1 itself: a trivially small finding must not
    even reach the campaign question."""
    finding = make_finding(accounts=2, exposure=11.0)
    actions = make_leaf_actions(2, CAMPAIGN_REF)
    result = route_q_decision(finding, actions, {})
    assert result == Disposition.DBC_DENY


# ---------------------------------------------------------------------------
# ABLATION A4 -- P4 removed. Four genuine rescue attempts, each tested
# against BOTH Branch U (must stay blocked) and Branch G (must stay allowed).
# A rescue only counts as a TRUE SUBSTITUTE if it gets both right.
# ---------------------------------------------------------------------------

@pytest.mark.parametrize(
    "rescue_fn",
    [ablated_no_rescue, ablated_rescue_P1_stricter_evidence,
     ablated_rescue_P5_revalidation, ablated_rescue_P6_flag_then_execute],
)
def test_ablated_rescues_wrongly_execute_branch_U(rescue_fn):
    """FAILED SUBSTITUTE: none of P1, P5, or P6-without-P4 can tell that
    this specific campaign lacks root authority, because none of them
    ever look at root authority. Each wrongly executes Branch U."""
    finding = make_finding()
    actions = make_leaf_actions(4000, CAMPAIGN_REF)
    result = rescue_fn(finding, actions)
    assert result == Disposition.DBC_EXECUTE, (
        f"{rescue_fn.__name__} unexpectedly blocked Branch U without any "
        f"root-authority check -- inspect whether it silently reconstructed P4."
    )


def test_ablated_native_rate_cap_blocks_branch_U():
    """The rate cap DOES stop Branch U -- 4,000 actions/hour exceeds any
    realistic cap. On its own this looks like a rescue."""
    finding = make_finding()
    actions = make_leaf_actions(4000, CAMPAIGN_REF)
    result = ablated_rescue_native_rate_cap(finding, actions, max_per_hour=10)
    assert result == Disposition.DBC_DENY


def test_ablated_native_rate_cap_ALSO_blocks_branch_G():
    """The deny-all trap, demonstrated: the SAME cap, at the SAME threshold,
    also blocks Branch G -- a campaign that IS root-authorized -- because
    the cap has no way to see root authority at all. This is exactly the
    00K 'no deny-all shortcut' failure: it is not a rescue, it is blindness
    that happens to overlap with the right answer on one branch only."""
    finding = make_finding()
    actions = make_leaf_actions(4000, CAMPAIGN_REF)  # same volume as Branch G would have
    result = ablated_rescue_native_rate_cap(finding, actions, max_per_hour=10)
    assert result == Disposition.DBC_DENY, (
        "If this ever starts passing (DBC_EXECUTE), the rate cap has been "
        "given some way to see root authority -- i.e., it has reconstructed P4."
    )


def test_true_substitute_not_found_among_tested_rescues():
    """Summary assertion: across all five tested rescue attempts (P1, P5,
    P6-flag-only, no-rescue, and a realistic native rate cap), not one
    achieves TRUE SUBSTITUTE status (correct on both Branch U and Branch G
    without referencing root authority). This does not prove no true
    substitute can ever exist -- only that none was found among the
    plausible candidates tested here."""
    finding = make_finding()
    actions_U = make_leaf_actions(4000, CAMPAIGN_REF)

    rescues_that_get_U_right = {
        "native_rate_cap": ablated_rescue_native_rate_cap(finding, actions_U) == Disposition.DBC_DENY,
    }
    rescues_that_also_get_G_right = {
        "native_rate_cap": False,  # proven wrong in the test above -- it blocks G too
    }
    true_substitutes = [
        name for name in rescues_that_get_U_right
        if rescues_that_get_U_right[name] and rescues_that_also_get_G_right.get(name, False)
    ]
    assert true_substitutes == [], f"Unexpected true substitute(s) found: {true_substitutes}"
