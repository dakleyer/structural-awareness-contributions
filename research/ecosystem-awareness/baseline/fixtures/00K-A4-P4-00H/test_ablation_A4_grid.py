"""Bounded-grid hardening for 00K A4 / P4–00H."""
from datetime import timedelta
from ablation_A4 import (
    Disposition, RootCampaignAuthority, route_q_decision, NOW,
)
from a2l_strong_peer import a2l_strong_peer_decision
from test_ablation_A4 import CAMPAIGN_REF, make_finding, make_leaf_actions


def test_root_authority_validity_grid_is_the_branch_discriminant():
    actions = make_leaf_actions(50, CAMPAIGN_REF)
    finding = make_finding()

    registries = [
        ({}, Disposition.DBC_REPOSITION_RECONTRACT),
        ({CAMPAIGN_REF: RootCampaignAuthority(CAMPAIGN_REF, "OWNER", False, NOW + timedelta(days=1))},
         Disposition.DBC_REPOSITION_RECONTRACT),
        ({CAMPAIGN_REF: RootCampaignAuthority(CAMPAIGN_REF, "OWNER", True, NOW - timedelta(seconds=1))},
         Disposition.DBC_REPOSITION_RECONTRACT),
        ({CAMPAIGN_REF: RootCampaignAuthority(CAMPAIGN_REF, "OWNER", True, NOW + timedelta(days=1))},
         Disposition.DBC_EXECUTE),
    ]

    for registry, expected in registries:
        assert route_q_decision(finding, actions, registry) == expected
        assert a2l_strong_peer_decision(finding, actions, registry) == expected


def test_U_G_separation_holds_across_campaign_volume_grid():
    finding = make_finding()
    valid = {
        CAMPAIGN_REF: RootCampaignAuthority(
            CAMPAIGN_REF, "OWNER", True, NOW + timedelta(days=1)
        )
    }
    for n in [1, 2, 10, 100, 1000]:
        actions = make_leaf_actions(n, CAMPAIGN_REF)
        assert route_q_decision(finding, actions, {}) == Disposition.DBC_REPOSITION_RECONTRACT
        assert route_q_decision(finding, actions, valid) == Disposition.DBC_EXECUTE
        assert a2l_strong_peer_decision(finding, actions, {}) == Disposition.DBC_REPOSITION_RECONTRACT
        assert a2l_strong_peer_decision(finding, actions, valid) == Disposition.DBC_EXECUTE
