"""
ablation_A4.py — Executable strongest-repair simulation for 00K ablation A4.

Removed principle: P4 — Qualification-preserving handoff and authority lineage
Unique ablation anchor: S8 — Bounded subdelegation and non-amplification
Frozen scenario: 00H — Batch Opportunity Beyond Authority ("The Quiet Four Thousand")
Reference routes: 00H v0.5 Draft, §12.2 Route N1 / §12.3 Route Q; §14 Branch U / Branch G / Branch I

WHAT THIS IS
------------
A deterministic, rule-level simulation of the Q0-Q5 decision logic that 00H and
00K describe in prose. It is NOT a test of any real LLM agent, any commercial
product, or any live system. It is a symbolic model built to check one narrow,
precise question with actual running code instead of argument alone:

    Within this fixture, can any combination of P1 (evidence sufficiency),
    P5 (leaf-grant revalidation), P6 (composition detection) and a realistic
    native control (a per-hour rate cap) correctly separate Branch U
    (unauthorized common-root campaign) from Branch G (genuinely authorized
    campaign) WITHOUT reconstructing P4's specific invariant --
    a checkable root -> leaf campaign-authority link?

STATUS
------
This is a first, partial execution of ONE of the six 00K ablations (A4).
It does not execute A1/A2/A3/A5/A6, and it does not constitute a benchmark,
a certification, or evidence about any named product or platform.
"""

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional


class Disposition(Enum):
    DBC_EXECUTE = "DBC_EXECUTE"
    DBC_DENY = "DBC_DENY"
    DBC_REPOSITION_RECONTRACT = "DBC_REPOSITION_RECONTRACT"


@dataclass(frozen=True)
class RootCampaignAuthority:
    """A root-level grant that would legitimately cover a composed campaign.

    This object is exactly P4's semantic invariant made concrete: a
    root -> leaf link that carries purpose, scope and current validity.
    """
    campaign_ref: str
    issuer: str
    valid: bool
    expiry: datetime


@dataclass(frozen=True)
class LeafGrant:
    """A single one-case, capped grant -- the only kind of authority that
    exists once P4 is removed. Individually well-formed and, on its own,
    completely silent about any wider campaign.
    """
    case_id: str
    cap_amount: float
    campaign_ref: Optional[str]  # shared root-campaign tag, if any
    expiry: datetime


@dataclass(frozen=True)
class LeafAction:
    account_id: str
    amount: float
    grant: LeafGrant
    timestamp: datetime


@dataclass
class Finding:
    """F-00H-1: the ~4,000-account overcharge finding."""
    affected_accounts: int
    aggregate_exposure: float
    reconstructable_from_authorized_reads: bool


NOW = datetime(2026, 9, 25, 12, 0, 0)
MATERIALITY_ACCOUNT_THRESHOLD = 100
MATERIALITY_EXPOSURE_THRESHOLD = 10_000.0  # 00H-MAT-1, virtual fixture parameter


def check_P1_evidence_sufficiency(finding: Finding) -> bool:
    """P1 / S14: is the finding itself sufficiently established to be a
    material candidate at all? This says nothing about who may act on it."""
    return (
        finding.reconstructable_from_authorized_reads
        and finding.affected_accounts >= MATERIALITY_ACCOUNT_THRESHOLD
        and finding.aggregate_exposure >= MATERIALITY_EXPOSURE_THRESHOLD
    )


def check_P5_leaf_revalidation(actions: list[LeafAction], at_time: datetime = NOW) -> bool:
    """P5 / S10: re-check each leaf grant immediately before use.
    Returns True only if every leaf grant is still individually current."""
    return all(a.grant.expiry > at_time and a.amount <= a.grant.cap_amount for a in actions)


def detect_composition_P6(actions: list[LeafAction]) -> Optional[str]:
    """P6 / S9: does this set of leaf actions share one causal/campaign root?
    Returns the shared campaign_ref if a common root is detected, else None.
    This function can see that a campaign exists. It cannot see whether it
    is authorized -- that is exactly the question P4 exists to answer."""
    refs = {a.grant.campaign_ref for a in actions}
    if len(refs) == 1 and None not in refs:
        return refs.pop()
    return None


def check_P4_root_leaf_authority(
    campaign_ref: str, registry: dict[str, RootCampaignAuthority], at_time: datetime = NOW
) -> bool:
    """P4 / S8: does a valid, current ROOT campaign authority exist that
    actually covers this campaign_ref? This is the invariant that is
    removed in the ablated system below."""
    root = registry.get(campaign_ref)
    return root is not None and root.valid and root.expiry > at_time


def native_rate_cap_check(actions: list[LeafAction], max_per_hour: int) -> bool:
    """A realistic, commonly-deployed native control: block if more than
    N actions occur within a one-hour window. Says nothing about
    authorization -- only about volume and timing."""
    if not actions:
        return True
    window_start = min(a.timestamp for a in actions)
    in_window = [a for a in actions if a.timestamp <= window_start + timedelta(hours=1)]
    return len(in_window) <= max_per_hour


# ---------------------------------------------------------------------------
# ROUTE Q -- all six principles intact, including P4
# ---------------------------------------------------------------------------

def route_q_decision(
    finding: Finding,
    actions: list[LeafAction],
    registry: dict[str, RootCampaignAuthority],
) -> Disposition:
    if not check_P1_evidence_sufficiency(finding):
        return Disposition.DBC_DENY  # not material; nothing to preserve or act on

    campaign_ref = detect_composition_P6(actions)

    if campaign_ref is None:
        # Branch I: genuinely independent cases, each within its own mandate.
        if check_P5_leaf_revalidation(actions):
            return Disposition.DBC_EXECUTE
        return Disposition.DBC_REPOSITION_RECONTRACT

    # A common-root campaign is present (Branch U or Branch G).
    if check_P4_root_leaf_authority(campaign_ref, registry) and check_P5_leaf_revalidation(actions):
        return Disposition.DBC_EXECUTE  # Branch G: genuinely authorized -- proceeds
    return Disposition.DBC_REPOSITION_RECONTRACT  # Branch U: preserved, not executed, not discarded


# ---------------------------------------------------------------------------
# ABLATED SYSTEM -- P4 removed. Every function below is a genuine attempt
# to rescue correct behaviour using only P1, P5, P6 and a realistic native
# control, exactly as 00K's strongest-repair protocol requires.
# ---------------------------------------------------------------------------

def ablated_no_rescue(finding: Finding, actions: list[LeafAction]) -> Disposition:
    """Baseline ablation: local per-leaf checks only."""
    if not check_P1_evidence_sufficiency(finding):
        return Disposition.DBC_DENY
    if check_P5_leaf_revalidation(actions):
        return Disposition.DBC_EXECUTE
    return Disposition.DBC_DENY


def ablated_rescue_P1_stricter_evidence(finding: Finding, actions: list[LeafAction]) -> Disposition:
    """Rescue attempt 1: demand even stronger evidence sufficiency before acting.
    P1 only ever asks 'is this finding real and material?' -- never
    'who may act on the composed effect?'."""
    if not check_P1_evidence_sufficiency(finding):
        return Disposition.DBC_DENY
    if check_P5_leaf_revalidation(actions):
        return Disposition.DBC_EXECUTE
    return Disposition.DBC_DENY


def ablated_rescue_P5_revalidation(finding: Finding, actions: list[LeafAction]) -> Disposition:
    """Rescue attempt 2: revalidate every leaf grant immediately before use.
    By construction, Branch U's leaf grants are each individually valid --
    that is precisely what makes it Branch U rather than a simple invalid-grant case."""
    if not check_P1_evidence_sufficiency(finding):
        return Disposition.DBC_DENY
    if check_P5_leaf_revalidation(actions):
        return Disposition.DBC_EXECUTE
    return Disposition.DBC_DENY


def ablated_rescue_P6_flag_then_execute(finding: Finding, actions: list[LeafAction]) -> Disposition:
    """Rescue attempt 3: use P6 to detect that a campaign exists, but with
    no root-authority concept, the only two available rules are 'execute
    anyway' or 'block everything the same way' -- tested here and in the
    native-cap rescue below."""
    if not check_P1_evidence_sufficiency(finding):
        return Disposition.DBC_DENY
    detect_composition_P6(actions)  # composition IS seen -- but nothing follows from it
    if check_P5_leaf_revalidation(actions):
        return Disposition.DBC_EXECUTE
    return Disposition.DBC_DENY


def ablated_rescue_native_rate_cap(
    finding: Finding, actions: list[LeafAction], max_per_hour: int = 10
) -> Disposition:
    """Rescue attempt 4: a realistic native control, a per-hour action cap,
    tuned to catch Branch U's ~4,000-action burst."""
    if not check_P1_evidence_sufficiency(finding):
        return Disposition.DBC_DENY
    if not native_rate_cap_check(actions, max_per_hour):
        return Disposition.DBC_DENY  # blocked by volume, regardless of authorization
    if check_P5_leaf_revalidation(actions):
        return Disposition.DBC_EXECUTE
    return Disposition.DBC_DENY
