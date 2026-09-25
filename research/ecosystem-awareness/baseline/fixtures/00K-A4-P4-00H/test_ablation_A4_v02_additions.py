"""Additive v0.2 tests for the preserved 00K A4 harness.

These tests reproduce the reviewed package's NM controls, A2-L semantic-
reconstruction peer, and four-arm U/G comparison without rewriting the
previously reviewed v0.1 source files.
"""
from datetime import timedelta
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
from a2l_strong_peer import a2l_strong_peer_decision

FAR_FUTURE = NOW + timedelta(days=30)
CAMPAIGN_REF = "SOLSTICE-PRICING-FAULT-2026-09"


def make_finding(accounts=4000, exposure=240_000.0):
    return Finding(accounts, exposure, True)


def make_leaf_actions(n, campaign_ref, start=NOW):
    return [
        LeafAction(
            f"ACCT-{i:05d}",
            40.0,
            LeafGrant(f"CASE-{i:05d}", 50.0, campaign_ref, FAR_FUTURE),
            start + timedelta(seconds=i),
        )
        for i in range(n)
    ]


def make_NM_case():
    return make_finding(2, 11.0), make_leaf_actions(2, CAMPAIGN_REF)


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
    assert a2l_strong_peer_decision(
        make_finding(), make_leaf_actions(4000, CAMPAIGN_REF), {}
    ) == Disposition.DBC_REPOSITION_RECONTRACT


def test_a2l_allows_branch_G():
    ledger = {
        CAMPAIGN_REF: RootCampaignAuthority(
            CAMPAIGN_REF, "Solstice-Finance-Ops", True, FAR_FUTURE
        )
    }
    assert a2l_strong_peer_decision(
        make_finding(), make_leaf_actions(4000, CAMPAIGN_REF), ledger
    ) == Disposition.DBC_EXECUTE


def test_a2l_keeps_branch_I_independent():
    actions = [
        LeafAction(
            f"ACCT-{i}",
            40.0,
            LeafGrant(f"CASE-{i}", 50.0, None, FAR_FUTURE),
            NOW + timedelta(minutes=i),
        )
        for i in range(3)
    ]
    assert a2l_strong_peer_decision(
        make_finding(150, 12_000.0), actions, {}
    ) == Disposition.DBC_EXECUTE


def test_four_arm_comparison_table():
    finding = make_finding()
    actions = make_leaf_actions(4000, CAMPAIGN_REF)
    ledger_g = {
        CAMPAIGN_REF: RootCampaignAuthority(
            CAMPAIGN_REF, "Solstice-Finance-Ops", True, FAR_FUTURE
        )
    }

    u = {
        "1_baseline_no_lineage": ablated_no_rescue(finding, actions),
        "2_strongest_non_lineage_repair": ablated_rescue_native_rate_cap(finding, actions),
        "3_A2L_semantic_reconstruction": a2l_strong_peer_decision(finding, actions, {}),
        "4_route_q_full_six_principles": route_q_decision(finding, actions, {}),
    }
    g = {
        "2_strongest_non_lineage_repair": ablated_rescue_native_rate_cap(finding, actions),
        "3_A2L_semantic_reconstruction": a2l_strong_peer_decision(finding, actions, ledger_g),
        "4_route_q_full_six_principles": route_q_decision(finding, actions, ledger_g),
    }

    print("\n--- Branch U ---")
    for name, result in u.items():
        print(f"{name:35s} -> {result.value}")

    print("--- Branch G ---")
    for name, result in g.items():
        print(f"{name:35s} -> {result.value}")

    assert u["1_baseline_no_lineage"] == Disposition.DBC_EXECUTE
    assert u["2_strongest_non_lineage_repair"] == Disposition.DBC_DENY
    assert u["3_A2L_semantic_reconstruction"] == Disposition.DBC_REPOSITION_RECONTRACT
    assert u["4_route_q_full_six_principles"] == Disposition.DBC_REPOSITION_RECONTRACT

    assert g["2_strongest_non_lineage_repair"] == Disposition.DBC_DENY
    assert g["3_A2L_semantic_reconstruction"] == Disposition.DBC_EXECUTE
    assert g["4_route_q_full_six_principles"] == Disposition.DBC_EXECUTE
