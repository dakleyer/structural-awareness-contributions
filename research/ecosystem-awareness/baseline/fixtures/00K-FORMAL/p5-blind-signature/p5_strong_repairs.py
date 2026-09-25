"""Serious P5 repair search for 00K A5 / 00I.

P5 = material-change requalification: a grant/token can remain technically
valid (unexpired, correctly signed, correctly scoped) while the real-world
condition that justified issuing it has changed. P5 requires re-checking
that condition LIVE, at the moment of use -- not merely checking that the
token has not expired.

This module isolates that claim from a stronger, unnecessary one: it does
NOT require storing or replaying the full history of every past change to
the condition. It only requires one current, verifiable fact at action
time. That distinction is itself an ablation result, in the same shape as
00K-A10's P4 refinement: a full change-history log is not necessary for
this fixture; a live, current re-check is.
"""
from dataclasses import dataclass
from enum import Enum


class Disposition(Enum):
    EXECUTE = "EXECUTE"
    REQUALIFY = "REQUALIFY"
    DENY = "DENY"


@dataclass(frozen=True)
class Branch:
    material: bool
    token_valid: bool
    scope_match: bool
    time_since_issue_s: int
    condition_currently_true: bool


STALE = Branch(True, True, True, 2400, False)
FRESH = Branch(True, True, True, 2400, True)
NM = Branch(False, True, True, 2400, True)


def expected(branch: Branch) -> Disposition:
    if not branch.material:
        return Disposition.DENY
    if not branch.token_valid or not branch.scope_match:
        return Disposition.REQUALIFY
    return Disposition.EXECUTE if branch.condition_currently_true else Disposition.REQUALIFY


def p5_blind_signature(b: Branch):
    return (b.material, b.token_valid, b.scope_match, b.time_since_issue_s)


def enumerate_signature_only_policies():
    return list(Disposition)


def token_expiry_only(b: Branch) -> Disposition:
    if not b.material:
        return Disposition.DENY
    return Disposition.EXECUTE if b.token_valid and b.scope_match else Disposition.REQUALIFY


def cached_status_at_issue_time(b: Branch, cached_condition_was_true: bool = True) -> Disposition:
    if not b.material:
        return Disposition.DENY
    if not b.token_valid or not b.scope_match:
        return Disposition.REQUALIFY
    return Disposition.EXECUTE if cached_condition_was_true else Disposition.REQUALIFY


def elapsed_time_heuristic(b: Branch, max_age_s: int = 3600) -> Disposition:
    if not b.material:
        return Disposition.DENY
    if not b.token_valid or not b.scope_match:
        return Disposition.REQUALIFY
    return Disposition.EXECUTE if b.time_since_issue_s <= max_age_s else Disposition.REQUALIFY


def always_requalify_if_queued(b: Branch) -> Disposition:
    if not b.material:
        return Disposition.DENY
    return Disposition.REQUALIFY


def always_execute_if_token_and_scope_valid(b: Branch) -> Disposition:
    if not b.material:
        return Disposition.DENY
    return Disposition.EXECUTE if b.token_valid and b.scope_match else Disposition.REQUALIFY


class LiveConditionCheck:
    """Current-state repair: no historical change log is required."""

    def query_live(self, b: Branch) -> bool:
        return b.condition_currently_true

    def decide(self, b: Branch) -> Disposition:
        if not b.material:
            return Disposition.DENY
        if not b.token_valid or not b.scope_match:
            return Disposition.REQUALIFY
        return Disposition.EXECUTE if self.query_live(b) else Disposition.REQUALIFY
