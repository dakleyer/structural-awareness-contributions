"""A2-L strong peer used by the additive v0.2 00K A4 harness tests.

This deliberately implements the root/delegation-lineage relation outside
Route Q to show that a non-EA peer can satisfy the same semantic invariant.
"""

from ablation_A4 import (
    Disposition,
    RootCampaignAuthority,
    Finding,
    LeafAction,
    check_P1_evidence_sufficiency,
    check_P5_leaf_revalidation,
    detect_composition_P6,
    NOW,
)


def a2l_strong_peer_decision(
    finding: Finding,
    actions: list[LeafAction],
    delegation_ledger: dict[str, RootCampaignAuthority],
) -> Disposition:
    if not check_P1_evidence_sufficiency(finding):
        return Disposition.DBC_DENY

    campaign_ref = detect_composition_P6(actions)
    if campaign_ref is None:
        return (
            Disposition.DBC_EXECUTE
            if check_P5_leaf_revalidation(actions)
            else Disposition.DBC_REPOSITION_RECONTRACT
        )

    root = delegation_ledger.get(campaign_ref)
    root_authority_current = root is not None and root.valid and root.expiry > NOW
    if root_authority_current and check_P5_leaf_revalidation(actions):
        return Disposition.DBC_EXECUTE
    return Disposition.DBC_REPOSITION_RECONTRACT
