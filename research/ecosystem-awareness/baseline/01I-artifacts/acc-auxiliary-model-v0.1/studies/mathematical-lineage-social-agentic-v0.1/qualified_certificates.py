"""Source-bound, dual-time finite certificate admission for SA-O2/O5 and EA.

The historical event window and current decision-use window are distinct.
Signatures attest payload integrity under *externally configured* trust keys;
scope/role entitlement, retention, revocation and use rights have independent
checks. No status below grants execution, a new rule, or hidden-world truth.
"""
from __future__ import annotations

from dataclasses import dataclass, fields, replace
from hashlib import sha256
import hmac
import json
import string
from typing import Any, Callable, Mapping


def _required_text(value: Any, name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(name + " must be nonempty")


def _tick(value: Any, name: str) -> None:
    if type(value) is not int or value < 0:
        raise ValueError(name + " must be a nonnegative integer clock tick")


def _digest(value: Any, name: str) -> None:
    if not isinstance(value, str) or len(value) != 64 or any(
            c not in "0123456789abcdef" for c in value):
        raise ValueError(name + " must be a sha256 hex digest")


def _window(start: int, end: int, name: str) -> None:
    _tick(start, name + ".start")
    _tick(end, name + ".end_exclusive")
    if start >= end:
        raise ValueError(name + " must be a nonempty half-open time window")


@dataclass(frozen=True)
class RetainedEvent:
    """Observer-attested occurrence, not proof of a claimed external origin."""
    event_id: str
    event_kind: str
    claimed_origin: str
    payload_sha256: str
    scope: str
    context_version: str
    time_basis: str
    observer: str
    observer_key_id: str
    occurred_at: int
    captured_at: int
    retain_until_exclusive: int
    capture_permitted: bool
    admission: str = "UNRESOLVED"
    signature: str = ""

    def __post_init__(self) -> None:
        for f in ("event_id", "event_kind", "claimed_origin", "scope",
                  "context_version", "time_basis", "observer", "observer_key_id", "admission"):
            _required_text(getattr(self, f), f)
        _digest(self.payload_sha256, "payload_sha256")
        if self.admission != "UNRESOLVED":
            raise ValueError("retained pre-admission event must remain UNRESOLVED")
        for f in ("occurred_at", "captured_at", "retain_until_exclusive"):
            _tick(getattr(self, f), f)
        if not self.occurred_at <= self.captured_at < self.retain_until_exclusive:
            raise ValueError("invalid occurrence/capture/retention sequence")
        if type(self.capture_permitted) is not bool:
            raise ValueError("capture_permitted must be boolean")


@dataclass(frozen=True)
class RuleCertificate:
    """Signed source-backed rule with historical and use-time validity."""
    certificate_id: str
    issuer: str
    key_id: str
    source_owner: str
    source_role: str
    receiver_role: str
    source_method: str
    evidence_ref: str
    event_id: str
    event_kind: str
    claimed_origin: str
    payload_sha256: str
    event_observer: str
    event_observer_key_id: str
    event_record_sha256: str
    scope: str
    event_context_version: str
    receiver: str
    purpose: str
    question: str
    rule_version: str
    time_basis: str
    event_from: int
    event_until_exclusive: int
    issued_at: int
    use_from: int
    use_until_exclusive: int
    signature: str = ""

    def __post_init__(self) -> None:
        for f in ("certificate_id", "issuer", "key_id", "source_owner",
                  "source_role", "receiver_role", "source_method",
                  "evidence_ref", "event_id", "event_kind", "claimed_origin",
                  "event_observer", "event_observer_key_id",
                  "scope", "event_context_version", "receiver", "purpose",
                  "question", "rule_version", "time_basis"):
            _required_text(getattr(self, f), f)
        _digest(self.payload_sha256, "payload_sha256")
        _digest(self.event_record_sha256, "event_record_sha256")
        _window(self.event_from, self.event_until_exclusive, "event_coverage")
        _window(self.use_from, self.use_until_exclusive, "decision_use")
        _tick(self.issued_at, "issued_at")
        if self.use_from < self.issued_at:
            raise ValueError("decision-use window cannot precede issuance")


@dataclass(frozen=True)
class DecisionUse:
    decision_id: str
    scope: str
    context_version: str
    receiver: str
    purpose: str
    question: str
    rule_version: str
    time_basis: str
    at_time: int

    def __post_init__(self) -> None:
        for f in ("decision_id", "scope", "context_version", "receiver",
                  "purpose", "question", "rule_version", "time_basis"):
            _required_text(getattr(self, f), f)
        _tick(self.at_time, "decision_time")


@dataclass(frozen=True)
class RevocationReceipt:
    """Authority-signed status; a stale/unknown receipt cannot justify use."""
    authority: str
    authority_key_id: str
    subject_issuer: str
    subject_key_id: str
    subject_certificate_id: str
    subject_certificate_sha256: str
    status: str  # CLEAR, FORWARD_REVOKED, RETRO_REVOKED, UNKNOWN
    time_basis: str
    observed_at: int
    fresh_until_exclusive: int
    effective_at: int | None = None
    signature: str = ""

    def __post_init__(self) -> None:
        for f in ("authority", "authority_key_id", "subject_issuer",
                  "subject_key_id", "subject_certificate_id", "time_basis"):
            _required_text(getattr(self, f), f)
        _digest(self.subject_certificate_sha256, "subject_certificate_sha256")
        if self.status not in ("CLEAR", "FORWARD_REVOKED", "RETRO_REVOKED", "UNKNOWN"):
            raise ValueError("unknown revocation status")
        _tick(self.observed_at, "revocation.observed_at")
        _tick(self.fresh_until_exclusive, "revocation.fresh_until")
        if self.observed_at >= self.fresh_until_exclusive:
            raise ValueError("empty revocation freshness interval")
        if self.status in ("FORWARD_REVOKED", "RETRO_REVOKED"):
            _tick(self.effective_at, "revocation.effective_at")
        elif self.effective_at is not None:
            raise ValueError("non-revoked status cannot carry revocation time")


@dataclass(frozen=True)
class CertificateAssessment:
    historical_status: str
    use_status: str
    event_id: str | None
    certificate_id: str | None
    decision_id: str
    execution: str = "NEVER"

    def as_dict(self) -> dict[str, str | None]:
        return {
            "historical_status": self.historical_status,
            "use_status": self.use_status,
            "event_id": self.event_id,
            "certificate_id": self.certificate_id,
            "decision_id": self.decision_id,
            "execution": self.execution,
        }


def signed_payload(record: RetainedEvent | RuleCertificate | RevocationReceipt) -> bytes:
    """Domain-separated canonical bytes: changing any signed field invalidates it."""
    if isinstance(record, RetainedEvent):
        kind = "ACC_RETAINED_EVENT_V1"
    elif isinstance(record, RuleCertificate):
        kind = "ACC_RULE_CERTIFICATE_V1"
    elif isinstance(record, RevocationReceipt):
        kind = "ACC_REVOCATION_RECEIPT_V1"
    else:
        raise TypeError("only typed event/certificate/revocation records may be signed")
    contents = {f.name: getattr(record, f.name)
                for f in fields(record) if f.name != "signature"}
    return (kind + "\n").encode("utf-8") + json.dumps(
        contents, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def sign_hmac(record: RetainedEvent | RuleCertificate | RevocationReceipt, key: bytes):
    """Reference signer for declared shared-key test domains; keys stay external."""
    if type(key) is not bytes or len(key) < 16:
        raise ValueError("HMAC signing key must be at least 16 bytes")
    return replace(record, signature=hmac.new(
        key, signed_payload(record), sha256).hexdigest())


def verify_hmac(record: RetainedEvent | RuleCertificate | RevocationReceipt,
                trusted_keys: Mapping[tuple[str, str], bytes]) -> bool:
    """Fail closed if issuer/key is unknown, signature missing or data altered."""
    if isinstance(record, RetainedEvent):
        owner, key_id = record.observer, record.observer_key_id
    elif isinstance(record, RuleCertificate):
        owner, key_id = record.issuer, record.key_id
    elif isinstance(record, RevocationReceipt):
        owner, key_id = record.authority, record.authority_key_id
    else:
        return False
    key = trusted_keys.get((owner, key_id))
    signature = record.signature
    if (type(key) is not bytes or len(key) < 16
            or not isinstance(signature, str) or len(signature) != 64
            or any(c not in string.hexdigits for c in signature)):
        return False
    expected = hmac.new(key, signed_payload(record), sha256).hexdigest()
    return hmac.compare_digest(expected, signature.lower())


def _verified(verifier: Callable[..., bool], record: Any) -> bool:
    """Pluggable public-key, HSM, KMS or HMAC signature backends."""
    try:
        return verifier(record) is True
    except Exception:
        return False


def _call_policy(predicate: Callable[..., bool | None], *args: Any) -> str:
    """Policy outage/error also yields UNKNOWN; never a granted right."""
    try:
        value = predicate(*args)
    except Exception:
        return "UNKNOWN"
    return _policy_truth(value)


def _policy_truth(value: Any) -> str:
    """Missing or non-Boolean evidence is UNKNOWN, never implicit permission."""
    return "YES" if value is True else "NO" if value is False else "UNKNOWN"


def evaluate_certificate(
    event: RetainedEvent | None,
    certificate: RuleCertificate | None,
    decision: DecisionUse,
    *,
    verify_attestation: Callable[[RetainedEvent | RuleCertificate | RevocationReceipt], bool],
    source_qualified: Callable[[RuleCertificate, RetainedEvent], bool | None],
    capture_right: Callable[[RetainedEvent], bool | None],
    request_authenticated: Callable[[DecisionUse], bool | None],
    retention_right: Callable[[RetainedEvent, DecisionUse], bool | None],
    payload_available: Callable[[RetainedEvent], bool | None],
    evidence_use_right: Callable[[RuleCertificate, DecisionUse], bool | None],
    revocation: RevocationReceipt | None,
    trusted_clock: Callable[[str], int],
    max_revocation_age: int,
    revocation_current: Callable[[RevocationReceipt, RuleCertificate, int], bool | None],
) -> CertificateAssessment:
    """Independent historical vs at-use decisions; never an action verdict.

    The signature verifier, source/retention/use policies and revocation receipt
    come from separately configured authorities. No signed self-assertion of 'verified'
    replaces any of these checks.
    """
    def assessment(historical: str, use: str) -> CertificateAssessment:
        return CertificateAssessment(
            historical, use, event.event_id if isinstance(event, RetainedEvent) else None,
            certificate.certificate_id if isinstance(certificate, RuleCertificate) else None,
            decision.decision_id if isinstance(decision, DecisionUse) else "NO_DECISION",
        )

    if event is None:
        return assessment("NO_REPLAY_SOURCE", "NO_LIVE_EVIDENCE")
    if not isinstance(event, RetainedEvent) or not isinstance(decision, DecisionUse):
        raise TypeError("typed event and decision required")
    if not _verified(verify_attestation, event):
        return assessment("EVENT_ATTESTATION_INVALID", "NO_LIVE_EVIDENCE")
    try:
        now = trusted_clock(event.time_basis)
        _tick(now, "trusted clock")
        _tick(max_revocation_age, "max_revocation_age")
        if max_revocation_age == 0:
            raise ValueError("max_revocation_age must be positive")
    except Exception:
        return assessment("CLOCK_OR_FRESHNESS_POLICY_UNAVAILABLE", "NO_LIVE_EVIDENCE")
    if not event.capture_permitted:
        return assessment("CAPTURE_NOT_PERMITTED", "NO_LIVE_EVIDENCE")
    captured = _call_policy(capture_right, event)
    if captured != "YES":
        return assessment("CAPTURE_RIGHT_DENIED" if captured == "NO"
                          else "CAPTURE_RIGHT_UNKNOWN", "NO_LIVE_EVIDENCE")
    if now < event.captured_at:
        return assessment("EVENT_NOT_YET_RETAINED", "NO_LIVE_EVIDENCE")
    if now >= event.retain_until_exclusive:
        return assessment("RETENTION_EXPIRED", "NO_LIVE_EVIDENCE")
    retained = _call_policy(retention_right, event, decision)
    if retained != "YES":
        return assessment(
            "RETENTION_NOT_ALLOWED" if retained == "NO" else "RETENTION_RIGHT_UNKNOWN",
            "NO_LIVE_EVIDENCE",
        )
    available = _call_policy(payload_available, event)
    if available != "YES":
        return assessment("RETAINED_PAYLOAD_MISSING" if available == "NO"
                          else "PAYLOAD_AVAILABILITY_UNKNOWN", "NO_LIVE_EVIDENCE")
    if certificate is None:
        return assessment("UNRESOLVED", "NO_CERTIFICATE")
    if not isinstance(certificate, RuleCertificate):
        raise TypeError("typed rule certificate required")
    if not _verified(verify_attestation, certificate):
        return assessment("CERTIFICATE_ATTESTATION_INVALID",
                                     "NO_LIVE_EVIDENCE")

    if certificate.time_basis != event.time_basis:
        return assessment("CERTIFICATE_CLOCK_DOMAIN_MISMATCH", "NO_LIVE_EVIDENCE")
    if (certificate.event_id, certificate.event_kind,
            certificate.claimed_origin, certificate.payload_sha256,
            certificate.event_observer, certificate.event_observer_key_id,
            certificate.event_record_sha256,
            certificate.scope, certificate.event_context_version) != (
            event.event_id, event.event_kind, event.claimed_origin,
            event.payload_sha256, event.observer, event.observer_key_id,
            sha256(signed_payload(event)).hexdigest(),
            event.scope, event.context_version):
        return assessment("EVENT_BINDING_MISMATCH", "NO_LIVE_EVIDENCE")
    if not certificate.event_from <= event.occurred_at < certificate.event_until_exclusive:
        return assessment("EVENT_OUTSIDE_COVERAGE", "NO_LIVE_EVIDENCE")
    source = _call_policy(source_qualified, certificate, event)
    if source != "YES":
        return assessment(
            "SOURCE_NOT_QUALIFIED" if source == "NO" else "SOURCE_QUALIFICATION_UNKNOWN",
            "NO_LIVE_EVIDENCE",
        )

    if now < certificate.issued_at:
        return assessment("UNRESOLVED", "CERTIFICATE_NOT_YET_ISSUED")

    # Revocation evidence is itself time-qualified; absence/lag is not CLEAR.
    if revocation is None or not isinstance(revocation, RevocationReceipt):
        return assessment("REVOCATION_UNKNOWN", "REVOCATION_UNKNOWN")
    if not _verified(verify_attestation, revocation):
        return assessment("REVOCATION_ATTESTATION_INVALID", "REVOCATION_UNKNOWN")
    if (revocation.subject_issuer, revocation.subject_key_id,
            revocation.subject_certificate_id, revocation.subject_certificate_sha256) != (
            certificate.issuer, certificate.key_id, certificate.certificate_id,
            sha256(signed_payload(certificate)).hexdigest()):
        return assessment("REVOCATION_BINDING_MISMATCH", "REVOCATION_UNKNOWN")
    if revocation.time_basis != event.time_basis:
        return assessment("REVOCATION_CLOCK_DOMAIN_MISMATCH", "REVOCATION_UNKNOWN")
    if revocation.observed_at < certificate.issued_at:
        return assessment("REVOCATION_PREDATES_CERTIFICATE", "REVOCATION_UNKNOWN")
    if (revocation.observed_at > now
            or revocation.fresh_until_exclusive <= now
            or now - revocation.observed_at >= max_revocation_age):
        return assessment("REVOCATION_STALE", "REVOCATION_STALE")
    latest = _call_policy(revocation_current, revocation, certificate, now)
    if latest != "YES":
        return assessment("REVOCATION_SUPERSEDED" if latest == "NO"
                          else "REVOCATION_STATE_UNKNOWN", "REVOCATION_UNKNOWN")
    if revocation.status == "UNKNOWN":
        return assessment("REVOCATION_UNKNOWN", "REVOCATION_UNKNOWN")
    if (revocation.status == "RETRO_REVOKED"
            and revocation.effective_at <= now):
        return assessment("HISTORICAL_BASIS_REVOKED", "REVOKED_AT_USE")

    # A forward-only revocation does not rewrite a valid historical event.
    historical = "HISTORICALLY_APPLICABLE"
    if decision.time_basis != event.time_basis:
        return assessment(historical, "DECISION_CLOCK_DOMAIN_MISMATCH")
    if decision.at_time != now:
        return assessment(historical, "DECISION_TIME_NOT_CURRENT")
    caller = _call_policy(request_authenticated, decision)
    if caller != "YES":
        return assessment(historical, "CALLER_NOT_AUTHENTICATED" if caller == "NO"
                          else "CALLER_AUTHENTICATION_UNKNOWN")
    if (certificate.receiver, certificate.purpose, certificate.question,
            certificate.scope) != (
            decision.receiver, decision.purpose, decision.question, decision.scope):
        return assessment(historical, "RECEIVING_CONTRACT_MISMATCH")
    if revocation.status == "FORWARD_REVOKED" and revocation.effective_at <= decision.at_time:
        return assessment(historical, "REVOKED_AT_USE")
    if decision.at_time < certificate.use_from:
        return assessment(historical, "NOT_YET_VALID_FOR_USE")
    if decision.at_time >= certificate.use_until_exclusive:
        return assessment(historical, "EXPIRED_AT_USE")
    if (decision.context_version != certificate.event_context_version
            or decision.rule_version != certificate.rule_version):
        return assessment(historical, "STALE_DECISION_FRAME")
    permitted = _call_policy(evidence_use_right, certificate, decision)
    if permitted != "YES":
        return assessment(
            historical, "USE_NOT_PERMITTED" if permitted == "NO" else "USE_RIGHT_UNKNOWN",
        )
    return assessment(historical, "VALID_FOR_CURRENT_REVIEW")
