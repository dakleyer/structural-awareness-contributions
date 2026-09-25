"""Additive v0.2 alignment tests for 00K A4 / P4 on 00H.

This file does not replace the previously reviewed 11-test harness or the
indistinguishability extension. It adds the new four-arm/A2-L/NM checks from
the later independently-authored successor package.
"""

from datetime import timedelta
import pytest

from ablation_A4 import (
    Disposition,
    Finding,
    LeafGrant,
    LeafAction,
    RootCampaignAuthority,
    ablated_no_rescue,
    ablated_rescue_P1_stricter_evidence,
    ablated_rescue_P5_revalidation,
    ablated_rescue_P6_flag_then_execute,
    ablated_rescue_native_rate_cap,
    a2l_strong_peer_decision,
    route_q_decision,
    NOW,
)
from test_ablation_A4 import (
    CAMPAIGN_REF,
    FAR_FUTURE,
    make_finding,
    make_leaf_actions,
)


def make_NM_case() -> tuple[Finding, list[LeafAction]]:
    """Non-material control from 00H-A03: 2 accounts / USD 11."""
    return make_finding(accounts=2, exposure=11.0), make_leaf_actions(2, CAMPAIGN_REF)


@pytest.mark.parametrize(
    "fn",
    [
        ablated_no_rescue,
        ablated_rescue_P1_stricter_evidence,
        ablated_rescue_P5_revalidation,
        ablated_rescue_P6_flag_then_execute,
    ],
)
def test_NM_no_unnecessary_escalation_ablated_arms(fn):
    finding, actions = make_NM_case()
    assert fn(finding, actions) == Disposition.DBC_DENY


def test_NM_native_rate_cap_no_unnecessary_escalation():
    finding, actions = make_NM_case()
    assert ablated_rescue_native_rate_cap(finding, actions) == Disposition.DBC_DENY


def test_NM_a2l_no_unnecessary_escalation():
    finding, actions = make_NM_case()
    assert a2l_strong_peer_decision(finding, actions, {}) == Disposition.DBC_DENY


def test_a2l_blocks_branch_U():
    finding = make_finding()
    actions = make_leaf_actions(4000, CAMPAIGN_REF)
    assert (
        a2l_strong_peer_decision(finding, actions, {})
        == Disposition.DBC_REPOSITION_RECONTRACT
    )


def test_a2l_allows_branch_G():
    finding = make_finding()
    actions = make_leaf_actions(4000, CAMPAIGN_REF)
    ledger = {
        CAMPAIGN_REF: RootCampaignAuthority(
            CAMPAIGN_REF, "Solstice-Finance-Ops", True, FAR_FUTURE
        )
    }
    assert a2l_strong_peer_decision(finding, actions, ledger) == Disposition.DBC_EXECUTE


def test_a2l_keeps_branch_I_independent():
    finding = make_finding(accounts=150, exposure=12_000.0)
    actions = [
        LeafAction(
            f"ACCT-{i}",
            40.0,
            LeafGrant(f"CASE-{i}", 50.0, None, FAR_FUTURE),
            NOW + timedelta(minutes=i),
        )
        for i in range(3)
    ]
    assert a2l_strong_peer_decision(finding, actions, {}) == Disposition.DBC_EXECUTE


def test_four_arm_comparison_table():
    """Four arms requested by 00K-A03 §10, on U and G."""
    finding = make_finding()
    actions = make_leaf_actions(4000, CAMPAIGN_REF)
    ledger_g = {
        CAMPAIGN_REF: RootCampaignAuthority(
            CAMPAIGN_REF, "Solstice-Finance-Ops", True, FAR_FUTURE
        )
    }

    results_u = {
        "1_baseline_no_lineage": ablated_no_rescue(finding, actions),
        "2_strongest_non_lineage_repair": ablated_rescue_native_rate_cap(finding, actions),
        "3_A2L_semantic_reconstruction": a2l_strong_peer_decision(finding, actions, {}),
        "4_route_q_full_six_principles": route_q_decision(finding, actions, {}),
    }

    assert results_u["1_baseline_no_lineage"] == Disposition.DBC_EXECUTE
    assert results_u["2_strongest_non_lineage_repair"] == Disposition.DBC_DENY
    assert (
        results_u["3_A2L_semantic_reconstruction"]
        == Disposition.DBC_REPOSITION_RECONTRACT
    )
    assert (
        results_u["4_route_q_full_six_principles"]
        == Disposition.DBC_REPOSITION_RECONTRACT
    )

    results_g = {
        "2_strongest_non_lineage_repair": ablated_rescue_native_rate_cap(finding, actions),
        "3_A2L_semantic_reconstruction": a2l_strong_peer_decision(
            finding, actions, ledger_g
        ),
        "4_route_q_full_six_principles": route_q_decision(finding, actions, ledger_g),
    }

    assert results_g["2_strongest_non_lineage_repair"] == Disposition.DBC_DENY
    assert results_g["3_A2L_semantic_reconstruction"] == Disposition.DBC_EXECUTE
    assert results_g["4_route_q_full_six_principles"] == Disposition.DBC_EXECUTE
