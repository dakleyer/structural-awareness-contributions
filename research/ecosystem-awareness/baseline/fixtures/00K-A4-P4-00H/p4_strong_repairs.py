"""Serious P4 repair search for 00K A4 / 00H.

This layer distinguishes the minimal authority-qualification invariant from the
stronger implementation choice of preserving a full root->leaf delegation
history. 00H's U/G/I/NM fixture can be solved by full lineage, by a scoped
capability, or by an authoritative owner-side PDP attestation.

That distinction is itself an ablation result: full delegation history is not
necessary for this fixture, while a decision-sufficient current authority basis
still appears necessary.
"""
from dataclasses import dataclass
from enum import Enum


class Disposition(Enum):
    EXECUTE = "EXECUTE"
    RECONTRACT = "RECONTRACT"
    DENY = "DENY"


@dataclass(frozen=True)
class Branch:
    material: bool
    common_campaign: bool
    leaf_valid: bool
    campaign_id: str | None
    action_count: int
    aggregate_amount: float
    risk_score: float
    root_authorized: bool


@dataclass(frozen=True)
class ScopedPermit:
    campaign_id: str
    max_actions: int
    max_amount: float
    valid: bool
    issuer: str = "FINOPS-PDP"


@dataclass(frozen=True)
class Capability:
    campaign_id: str
    max_actions: int
    max_amount: float
    valid: bool
    issuer: str = "FINOPS-ROOT"


U = Branch(True, True, True, "CAMP-X", 4000, 240000.0, 0.42, False)
G = Branch(True, True, True, "CAMP-X", 4000, 240000.0, 0.42, True)
I = Branch(True, False, True, None, 3, 120.0, 0.42, False)
NM = Branch(False, True, True, "CAMP-X", 2, 11.0, 0.42, False)


def expected(branch):
    if not branch.material:
        return Disposition.DENY
    if not branch.common_campaign:
        return Disposition.EXECUTE if branch.leaf_valid else Disposition.RECONTRACT
    return (
        Disposition.EXECUTE
        if branch.root_authorized and branch.leaf_valid
        else Disposition.RECONTRACT
    )


def p4_blind_signature(b):
    return (
        b.material,
        b.common_campaign,
        b.leaf_valid,
        b.campaign_id,
        b.action_count,
        b.aggregate_amount,
        b.risk_score,
    )


def leaf_rbac(b):
    if not b.material:
        return Disposition.DENY
    return Disposition.EXECUTE if b.leaf_valid else Disposition.RECONTRACT


def rate_cap(b, max_actions=100):
    if not b.material:
        return Disposition.DENY
    if b.action_count > max_actions:
        return Disposition.DENY
    return Disposition.EXECUTE if b.leaf_valid else Disposition.RECONTRACT


def aggregate_cap(b, max_amount=10000.0):
    if not b.material:
        return Disposition.DENY
    if b.aggregate_amount > max_amount:
        return Disposition.DENY
    return Disposition.EXECUTE if b.leaf_valid else Disposition.RECONTRACT


def risk_gate(b, threshold=0.5):
    if not b.material:
        return Disposition.DENY
    if b.risk_score >= threshold:
        return Disposition.RECONTRACT
    return Disposition.EXECUTE if b.leaf_valid else Disposition.RECONTRACT


def campaign_block_all(b):
    if not b.material:
        return Disposition.DENY
    if b.common_campaign:
        return Disposition.RECONTRACT
    return Disposition.EXECUTE if b.leaf_valid else Disposition.RECONTRACT


def campaign_execute_all(b):
    if not b.material:
        return Disposition.DENY
    return Disposition.EXECUTE if b.leaf_valid else Disposition.RECONTRACT


def nonowner_human_approval(b):
    if not b.material:
        return Disposition.DENY
    return Disposition.EXECUTE if b.leaf_valid else Disposition.RECONTRACT


def static_campaign_allowlist(b, allow=("CAMP-X",)):
    if not b.material:
        return Disposition.DENY
    if not b.common_campaign:
        return Disposition.EXECUTE if b.leaf_valid else Disposition.RECONTRACT
    return (
        Disposition.EXECUTE
        if b.campaign_id in allow and b.leaf_valid
        else Disposition.RECONTRACT
    )


class OpaquePDP:
    """Legitimate owner-side PDP.

    It returns a scoped current authorization result but does not expose the
    historical root->leaf delegation chain to the relying component.
    """

    def decide(self, b):
        if not b.material:
            return Disposition.DENY
        if not b.common_campaign:
            return Disposition.EXECUTE if b.leaf_valid else Disposition.RECONTRACT
        return (
            Disposition.EXECUTE
            if b.root_authorized and b.leaf_valid
            else Disposition.RECONTRACT
        )

    def permit(self, b):
        if b.common_campaign and b.root_authorized:
            return ScopedPermit(
                b.campaign_id, b.action_count, b.aggregate_amount, True
            )
        return None


def decision_from_permit(b, permit):
    if not b.material:
        return Disposition.DENY
    if not b.common_campaign:
        return Disposition.EXECUTE if b.leaf_valid else Disposition.RECONTRACT
    if permit is None or not permit.valid:
        return Disposition.RECONTRACT
    if permit.campaign_id != b.campaign_id:
        return Disposition.RECONTRACT
    if b.action_count > permit.max_actions or b.aggregate_amount > permit.max_amount:
        return Disposition.RECONTRACT
    return Disposition.EXECUTE if b.leaf_valid else Disposition.RECONTRACT


def decision_from_capability(b, cap):
    if not b.material:
        return Disposition.DENY
    if not b.common_campaign:
        return Disposition.EXECUTE if b.leaf_valid else Disposition.RECONTRACT
    if cap is None or not cap.valid:
        return Disposition.RECONTRACT
    if cap.campaign_id != b.campaign_id:
        return Disposition.RECONTRACT
    if b.action_count > cap.max_actions or b.aggregate_amount > cap.max_amount:
        return Disposition.RECONTRACT
    return Disposition.EXECUTE if b.leaf_valid else Disposition.RECONTRACT


def maker_checker(b, approver_is_legitimate_owner):
    if not b.material:
        return Disposition.DENY
    if not b.common_campaign:
        return Disposition.EXECUTE if b.leaf_valid else Disposition.RECONTRACT
    if approver_is_legitimate_owner and b.root_authorized and b.leaf_valid:
        return Disposition.EXECUTE
    return Disposition.RECONTRACT


def enumerate_signature_only_policies():
    # U/G have exactly the same P4-blind signature, so any deterministic
    # policy over that signature must emit the same result on both.
    return list(Disposition)
