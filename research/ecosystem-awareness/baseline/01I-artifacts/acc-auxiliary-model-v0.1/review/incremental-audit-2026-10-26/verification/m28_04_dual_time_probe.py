"""M28-04 and L-02 against the dual-time certificate contract of PR #60 (round 24).

Usage: python3 -B m28_04_dual_time_probe.py <studies/mathematical-lineage-social-agentic-v0.1 on PR #60>

Builds its own signed fixture (event at t=1, rule issued at t=2, use window
[2, 3), CLEAR revocation observed at t=2) with the module's reference HMAC
signer and checks, independently of the PR's tests:
  1. the t1/t2/t3/t10 witness and the false declared decision time;
  2. the half-open [start, end) use window, tick by tick from 0 to 21;
  3. that NaN, floats, booleans, None and text are rejected as clock ticks
     (the L-02 pattern of the old requalify);
  4. no reuse across cases: certificate on another event, CLEAR receipt on a
     re-issued certificate with the same ID, forward and retroactive revocation.
Exit code 1 on any unexpected outcome. Writes nothing.
"""
import sys
from dataclasses import replace
from hashlib import sha256

sys.path.insert(0, sys.argv[1])
from qualified_certificates import (  # noqa: E402
    DecisionUse, RetainedEvent, RevocationReceipt, RuleCertificate,
    evaluate_certificate, sign_hmac, signed_payload, verify_hmac,
)

KO, KI, KR = b"observer-key-material-0001", b"issuer-key-material-00002", b"revocation-key-material-03"
KEYS = {("obs", "k-o"): KO, ("iss", "k-i"): KI, ("rev", "k-r"): KR}
BASIS = "TICKS"
fails = []


def expect(label, got, want):
    ok = got == want
    print(f"{'OK  ' if ok else 'FAIL'} {label}: {got}" + ("" if ok else f"  (expected {want})"))
    if not ok:
        fails.append(label)


def event(eid="ev-1", payload=b"payload-1"):
    return sign_hmac(RetainedEvent(
        event_id=eid, event_kind="new-route", claimed_origin="vendor", payload_sha256=sha256(payload).hexdigest(),
        scope="route-v1", context_version="ctx-1", time_basis=BASIS, observer="obs", observer_key_id="k-o",
        occurred_at=1, captured_at=1, retain_until_exclusive=30, capture_permitted=True), KO)


def certificate(ev, **changes):
    base = RuleCertificate(
        certificate_id="cert-1", issuer="iss", key_id="k-i", source_owner="vendor", source_role="A",
        receiver_role="B", source_method="m", evidence_ref="ref", event_id=ev.event_id, event_kind=ev.event_kind,
        claimed_origin=ev.claimed_origin, payload_sha256=ev.payload_sha256, event_observer=ev.observer,
        event_observer_key_id=ev.observer_key_id, event_record_sha256=sha256(signed_payload(ev)).hexdigest(),
        scope=ev.scope, event_context_version=ev.context_version, receiver="R", purpose="p", question="q",
        rule_version="r1", time_basis=BASIS, event_from=0, event_until_exclusive=3, issued_at=2,
        use_from=2, use_until_exclusive=3)
    return sign_hmac(replace(base, **changes), KI)


def receipt(cert, status="CLEAR", effective=None, observed=2):
    return sign_hmac(RevocationReceipt(
        authority="rev", authority_key_id="k-r", subject_issuer=cert.issuer, subject_key_id=cert.key_id,
        subject_certificate_id=cert.certificate_id,
        subject_certificate_sha256=sha256(signed_payload(cert)).hexdigest(), status=status, time_basis=BASIS,
        observed_at=observed, fresh_until_exclusive=40, effective_at=effective), KR)


def run(ev, cert, rev, *, now, declared=None):
    decision = DecisionUse(decision_id="d", scope="route-v1", context_version="ctx-1", receiver="R", purpose="p",
                           question="q", rule_version="r1", time_basis=BASIS,
                           at_time=now if declared is None else declared)
    yes = lambda *a: True  # noqa: E731
    a = evaluate_certificate(
        ev, cert, decision, verify_attestation=lambda r: verify_hmac(r, KEYS), source_qualified=yes,
        capture_right=yes, request_authenticated=yes, retention_right=yes, payload_available=yes,
        evidence_use_right=yes, revocation=rev, trusted_clock=lambda b: now, max_revocation_age=35,
        revocation_current=yes)
    return a.historical_status, a.use_status


E = event()
C = certificate(E)
R = receipt(C)

print("1. Witness")
expect("t=1", run(E, C, R, now=1), ("UNRESOLVED", "CERTIFICATE_NOT_YET_ISSUED"))
expect("t=2", run(E, C, R, now=2), ("HISTORICALLY_APPLICABLE", "VALID_FOR_CURRENT_REVIEW"))
expect("t=3", run(E, C, R, now=3), ("HISTORICALLY_APPLICABLE", "EXPIRED_AT_USE"))
expect("t=10", run(E, C, R, now=10), ("HISTORICALLY_APPLICABLE", "EXPIRED_AT_USE"))
expect("t=10 declaring t=2", run(E, C, R, now=10, declared=2), ("HISTORICALLY_APPLICABLE", "DECISION_TIME_NOT_CURRENT"))

print("2. Half-open use window, ticks 0..21 (wider window [2, 6))")
C6 = certificate(E, use_until_exclusive=6)
R6 = receipt(C6)
valid = [t for t in range(22) if run(E, C6, R6, now=t)[1] == "VALID_FOR_CURRENT_REVIEW"]
expect("ticks valid for use", valid, [2, 3, 4, 5])

print("3. Non-integer clock ticks are rejected at construction")
for bad in (float("nan"), 2.0, True, None, "2", -1):
    for field in ("issued_at", "use_until_exclusive"):
        try:
            certificate(E, **{field: bad})
            got = "ACCEPTED"
        except (ValueError, TypeError) as exc:
            got = type(exc).__name__
        expect(f"{field}={bad!r}", got != "ACCEPTED", True)
for bad in (float("nan"), True, 2.0):
    try:
        DecisionUse(decision_id="d", scope="s", context_version="c", receiver="R", purpose="p", question="q",
                    rule_version="r", time_basis=BASIS, at_time=bad)
        got = "ACCEPTED"
    except (ValueError, TypeError):
        got = "REJECTED"
    expect(f"DecisionUse.at_time={bad!r}", got, "REJECTED")

print("4. No reuse across cases; revocation")
E2 = event("ev-2", b"payload-2")
expect("certificate of ev-1 on ev-2", run(E2, C, R, now=2)[0], "EVENT_BINDING_MISMATCH")
C_re = certificate(E, purpose="p", question="q", source_method="other-method")  # same ID, other content
expect("old CLEAR on re-issued certificate", run(E, C_re, R, now=2), ("REVOCATION_BINDING_MISMATCH", "REVOCATION_UNKNOWN"))
expect("forward revoked at 2", run(E, C, receipt(C, "FORWARD_REVOKED", 2), now=2),
       ("HISTORICALLY_APPLICABLE", "REVOKED_AT_USE"))
expect("retro revoked at 2", run(E, C, receipt(C, "RETRO_REVOKED", 2), now=2), ("HISTORICAL_BASIS_REVOKED", "REVOKED_AT_USE"))
expect("no receipt", run(E, C, None, now=2), ("REVOCATION_UNKNOWN", "REVOCATION_UNKNOWN"))
expect("receipt observed before issuance", run(E, C, receipt(C, observed=1), now=2)[0], "REVOCATION_PREDATES_CERTIFICATE")

print("RESULT:", "PASS" if not fails else f"FAIL {fails}")
sys.exit(1 if fails else 0)
