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
)


def a2l_strong_peer_decision(
    finding: Finding,
    actions: list[LeafAction],
    delegation_ledger: dict[str, RootCampaignAuthority],
) -> Disposition:
    if not check_P1_evidence_sufficiency(finding):
        return Disposition.DBC_DENY

    if not check_P5_leaf_revalidation(actions):
        return Disposition.DBC_REPOSITION_RECONTRACT
    for action in actions:
        ref = action.grant.campaign_ref
        if ref is None:  # Stipulated independent cases only; see fixture contract.
            continue
        root = delegation_ledger.get(ref)
        if (not ref or root is None or root.campaign_ref != ref
                or not root.valid or root.expiry <= action.timestamp):
            return Disposition.DBC_REPOSITION_RECONTRACT
    return Disposition.DBC_EXECUTE
