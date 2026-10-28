"""Adversarial, dual-time signed certificate checks (finite Stage A)."""
from __future__ import annotations

from dataclasses import replace
from hashlib import sha256
import unittest

from structural_adequacy import FiniteDecisionCase, assess_finite_adequacy

from qualified_certificates import (
    RetainedEvent, RuleCertificate, DecisionUse, RevocationReceipt,
    CertificateAssessment, evaluate_certificate, signed_payload, sign_hmac,
    verify_hmac,
)

_MISSING = object()
_OBSERVER_KEY = b"observer-secret-key-material-32-aaa"
_ISSUER_KEY = b"issuer-secret-key-material-32-bbbb"
_REVOCATION_KEY = b"revocation-authority-key-32-ccc"


class CertificateContractTests(unittest.TestCase):
    def setUp(self):
        self.keys = {
            ("observer-A", "observer-k1"): _OBSERVER_KEY,
            ("rule-issuer", "issuer-k2"): _ISSUER_KEY,
            ("revocation-admin", "revocation-k1"): _REVOCATION_KEY,
        }
        self.event = sign_hmac(RetainedEvent(
            event_id="event-7", event_kind="new-route",
            claimed_origin="vendor-B", payload_sha256=sha256(b"retained payload 7").hexdigest(),
            scope="route-v1", context_version="context-v1",
            time_basis="FIXTURE_TICKS_V1", observer="observer-A", observer_key_id="observer-k1",
            occurred_at=1, captured_at=1, retain_until_exclusive=20,
            capture_permitted=True, admission="UNRESOLVED",
        ), _OBSERVER_KEY)
        self.cert = sign_hmac(RuleCertificate(
            certificate_id="cert-9", issuer="rule-issuer", key_id="issuer-k2",
            source_owner="vendor-B", source_role="A", receiver_role="B",
            source_method="checked-ruleset-v1", evidence_ref="source-ledger:9",
            event_id=self.event.event_id, event_kind=self.event.event_kind,
            claimed_origin=self.event.claimed_origin,
            payload_sha256=self.event.payload_sha256,
            event_observer=self.event.observer,
            event_observer_key_id=self.event.observer_key_id,
            event_record_sha256=sha256(signed_payload(self.event)).hexdigest(),
            scope=self.event.scope, event_context_version=self.event.context_version,
            receiver="reviewer-R", purpose="scope-requalification",
            question="candidate-admission", rule_version="rule-v1",
            time_basis="FIXTURE_TICKS_V1", event_from=0, event_until_exclusive=3,
            issued_at=2, use_from=2, use_until_exclusive=3,
        ), _ISSUER_KEY)
        self.decision = DecisionUse(
            decision_id="review-22", scope="route-v1",
            context_version="context-v1", receiver="reviewer-R",
            purpose="scope-requalification", question="candidate-admission",
            rule_version="rule-v1", time_basis="FIXTURE_TICKS_V1", at_time=2,
        )
        self.revocation = sign_hmac(RevocationReceipt(
            authority="revocation-admin", authority_key_id="revocation-k1",
            subject_issuer="rule-issuer", subject_key_id="issuer-k2",
            subject_certificate_id="cert-9",
            subject_certificate_sha256=sha256(signed_payload(self.cert)).hexdigest(),
            status="CLEAR", time_basis="FIXTURE_TICKS_V1",
            observed_at=2, fresh_until_exclusive=20,
        ), _REVOCATION_KEY)

    def reissue(self, certificate, **changes):
        return sign_hmac(replace(certificate, **changes, signature=""), _ISSUER_KEY)

    def recertify_event(self, event, **changes):
        return sign_hmac(replace(event, **changes, signature=""), _OBSERVER_KEY)

    def revocation_receipt(self, status, *, effect=None, observed_at=2, fresh_until=20,
                           subject_issuer="rule-issuer", subject_certificate_id=None,
                           cert=None, time_basis="FIXTURE_TICKS_V1"):
        checked = self.cert if cert is None else cert
        cert_id = checked.certificate_id if subject_certificate_id is None else subject_certificate_id
        return sign_hmac(RevocationReceipt(
            authority="revocation-admin", authority_key_id="revocation-k1",
            subject_issuer=subject_issuer, subject_key_id="issuer-k2",
            subject_certificate_id=cert_id,
            subject_certificate_sha256=sha256(signed_payload(checked)).hexdigest(),
            status=status, time_basis=time_basis, observed_at=observed_at,
            fresh_until_exclusive=fresh_until, effective_at=effect,
        ), _REVOCATION_KEY)

    def assess(self, *, event=_MISSING, cert=_MISSING, decision=_MISSING,
               revocation=_MISSING, verifier=_MISSING, source=_MISSING,
               capture=_MISSING, retention=_MISSING, payload=_MISSING,
               authenticated=_MISSING, latest=_MISSING,
               use_right=_MISSING, now=_MISSING, max_age=18):
        c = self.cert if cert is _MISSING else cert
        d = self.decision if decision is _MISSING else decision
        return evaluate_certificate(
            self.event if event is _MISSING else event,
            c, d,
            verify_attestation=(lambda record: verify_hmac(record, self.keys))
            if verifier is _MISSING else verifier,
            source_qualified=(lambda cert, event: True) if source is _MISSING else source,
            capture_right=(lambda event: True) if capture is _MISSING else capture,
            request_authenticated=(lambda decision: True)
            if authenticated is _MISSING else authenticated,
            retention_right=(lambda event, decision: True)
            if retention is _MISSING else retention,
            payload_available=(lambda event: True) if payload is _MISSING else payload,
            evidence_use_right=(lambda cert, decision: True)
            if use_right is _MISSING else use_right,
            revocation=(self.revocation_receipt("CLEAR", cert=c)
                        if c is not None and c != self.cert else self.revocation)
            if revocation is _MISSING else revocation,
            trusted_clock=(lambda basis: d.at_time if now is _MISSING else now),
            max_revocation_age=max_age,
            revocation_current=(lambda rev, cert, now: True)
            if latest is _MISSING else latest,
        )

    def test_positive_use_has_separate_qualified_historical_and_current_results(self):
        outcome = self.assess()
        self.assertEqual(outcome.historical_status, "HISTORICALLY_APPLICABLE")
        self.assertEqual(outcome.use_status, "VALID_FOR_CURRENT_REVIEW")
        self.assertEqual(outcome.execution, "NEVER")
        self.assertEqual((outcome.event_id, outcome.certificate_id, outcome.decision_id),
                         ("event-7", "cert-9", "review-22"))
        self.assertEqual(outcome.as_dict()["execution"], "NEVER")

    def test_retrospective_rule_issued_at_two_can_read_preserved_event_at_one(self):
        self.assertEqual(self.event.occurred_at, 1)
        self.assertEqual(self.cert.issued_at, 2)
        self.assertEqual(self.assess().historical_status, "HISTORICALLY_APPLICABLE")

    def test_expired_at_decision_ten_keeps_historical_status(self):
        outcome = self.assess(decision=replace(self.decision, at_time=10))
        self.assertEqual(outcome.historical_status, "HISTORICALLY_APPLICABLE")
        self.assertEqual(outcome.use_status, "EXPIRED_AT_USE")
        self.assertEqual(outcome.execution, "NEVER")

    def test_exact_end_t3_is_excluded_for_live_use(self):
        outcome = self.assess(decision=replace(self.decision, at_time=3))
        self.assertEqual(outcome.historical_status, "HISTORICALLY_APPLICABLE")
        self.assertEqual(outcome.use_status, "EXPIRED_AT_USE")

    def test_valid_just_before_expiry(self):
        self.assertEqual(self.assess(decision=replace(self.decision, at_time=2)
                                     ).use_status, "VALID_FOR_CURRENT_REVIEW")

    def test_certificate_cannot_be_used_before_it_is_issued(self):
        outcome = self.assess(decision=replace(self.decision, at_time=1))
        self.assertEqual(outcome.historical_status, "UNRESOLVED")
        self.assertEqual(outcome.use_status, "CERTIFICATE_NOT_YET_ISSUED")

    def test_no_trace_and_no_certificate_keep_open_state(self):
        self.assertEqual(self.assess(event=None).historical_status, "NO_REPLAY_SOURCE")
        outcome = self.assess(cert=None)
        self.assertEqual((outcome.historical_status, outcome.use_status),
                         ("UNRESOLVED", "NO_CERTIFICATE"))

    def test_irrecoverable_capture_right_and_retention_expiry(self):
        unpermitted = self.recertify_event(self.event, capture_permitted=False)
        self.assertEqual(self.assess(event=unpermitted).historical_status,
                         "CAPTURE_NOT_PERMITTED")
        t20 = self.assess(decision=replace(self.decision, at_time=20))
        self.assertEqual(t20.historical_status, "RETENTION_EXPIRED")

    def test_tampered_signed_event_is_not_accepted(self):
        for changes in ({"scope": "other-scope"},
                        {"event_id": "event-replayed"},
                        {"payload_sha256": sha256(b"different payload").hexdigest()},
                        {"capture_permitted": False},
                        {"retain_until_exclusive": 21},
                        {"claimed_origin": "false-origin"}):
            with self.subTest(changes=changes):
                altered = replace(self.event, **changes)
                self.assertEqual(self.assess(event=altered).historical_status,
                                 "EVENT_ATTESTATION_INVALID")

    def test_tampered_certificate_or_key_unknown_is_rejected(self):
        for changes in ({"source_owner": "another-source"},
                        {"source_role": "C"}, {"receiver": "adversary"},
                        {"purpose": "other"}, {"use_until_exclusive": 99},
                        {"event_id": "another-event"}, {"rule_version": "rule-v2"}):
            with self.subTest(changes=changes):
                altered = replace(self.cert, **changes)
                self.assertEqual(self.assess(cert=altered).historical_status,
                                 "CERTIFICATE_ATTESTATION_INVALID")
        self.assertEqual(self.assess(verifier=lambda record: verify_hmac(record, {})
                                     ).historical_status, "EVENT_ATTESTATION_INVALID")

    def test_event_replay_under_new_signed_payload_fails_binding(self):
        another = self.recertify_event(
            self.event, payload_sha256=sha256(b"other event same ID").hexdigest())
        outcome = self.assess(event=another)
        self.assertEqual(outcome.historical_status, "EVENT_BINDING_MISMATCH")

    def test_event_window_is_half_open(self):
        too_late = self.reissue(self.cert, event_from=1, event_until_exclusive=2)
        self.assertEqual(self.assess(cert=too_late).historical_status,
                         "HISTORICALLY_APPLICABLE")
        too_early = self.reissue(self.cert, event_from=2, event_until_exclusive=5)
        self.assertEqual(self.assess(cert=too_early).historical_status,
                         "EVENT_OUTSIDE_COVERAGE")

    def test_receiver_and_purpose_binding_preserve_history_but_block_current_use(self):
        for field, value in (("receiver", "other-actor"),
                             ("purpose", "other-purpose"),
                             ("question", "other-question"), ("scope", "other-scope")):
            with self.subTest(field=field):
                outcome = self.assess(decision=replace(self.decision, **{field: value}))
                self.assertEqual(outcome.historical_status, "HISTORICALLY_APPLICABLE")
                self.assertEqual(outcome.use_status, "RECEIVING_CONTRACT_MISMATCH")

    def test_context_and_rule_change_requalify_before_reuse(self):
        cert = self.reissue(self.cert, use_until_exclusive=20)
        for field, value in (("context_version", "context-v2"),
                             ("rule_version", "rule-v2")):
            with self.subTest(field=field):
                outcome = self.assess(cert=cert, decision=replace(
                    self.decision, **{field: value}))
                self.assertEqual(outcome.historical_status, "HISTORICALLY_APPLICABLE")
                self.assertEqual(outcome.use_status, "STALE_DECISION_FRAME")

    def test_unknown_or_denied_source_prevents_historical_certification(self):
        for outcome, expected in ((False, "SOURCE_NOT_QUALIFIED"),
                                  (None, "SOURCE_QUALIFICATION_UNKNOWN"),
                                  (1, "SOURCE_QUALIFICATION_UNKNOWN")):
            with self.subTest(policy=outcome):
                result = self.assess(source=lambda cert, event, v=outcome: v)
                self.assertEqual(result.historical_status, expected)
        self.assertEqual(self.assess(source=lambda cert, event: 1 / 0
                                     ).historical_status, "SOURCE_QUALIFICATION_UNKNOWN")

    def test_retention_and_use_rights_are_two_separate_gates(self):
        for permitted, status in ((False, "RETENTION_NOT_ALLOWED"),
                                  (None, "RETENTION_RIGHT_UNKNOWN"),
                                  (1, "RETENTION_RIGHT_UNKNOWN")):
            with self.subTest(retention=permitted):
                result = self.assess(retention=lambda event, decision, p=permitted: p)
                self.assertEqual(result.historical_status, status)
        for permitted, status in ((False, "USE_NOT_PERMITTED"),
                                  (None, "USE_RIGHT_UNKNOWN"),
                                  ("true", "USE_RIGHT_UNKNOWN")):
            with self.subTest(use=permitted):
                result = self.assess(use_right=lambda cert, decision, p=permitted: p)
                self.assertEqual(result.historical_status, "HISTORICALLY_APPLICABLE")
                self.assertEqual(result.use_status, status)

    def test_forward_revocation_preserves_historical_but_blocks_new_use(self):
        cert = self.reissue(self.cert, use_until_exclusive=20)
        rev = self.revocation_receipt("FORWARD_REVOKED", effect=5, cert=cert)
        current = self.assess(cert=cert, revocation=rev, decision=replace(
            self.decision, at_time=2))
        self.assertEqual(current.use_status, "VALID_FOR_CURRENT_REVIEW")
        old = self.assess(cert=cert, revocation=rev, decision=replace(
            self.decision, at_time=10))
        self.assertEqual(old.historical_status, "HISTORICALLY_APPLICABLE")
        self.assertEqual(old.use_status, "REVOKED_AT_USE")

    def test_retroactive_revocation_invalidates_historical_basis(self):
        rev = self.revocation_receipt("RETRO_REVOKED", effect=1)
        outcome = self.assess(revocation=rev)
        self.assertEqual(outcome.historical_status, "HISTORICAL_BASIS_REVOKED")
        self.assertEqual(outcome.use_status, "REVOKED_AT_USE")

    def test_revocation_is_bound_to_issuer_and_signed(self):
        forged = replace(self.revocation, status="RETRO_REVOKED", effective_at=1)
        self.assertEqual(self.assess(revocation=forged).historical_status,
                         "REVOCATION_ATTESTATION_INVALID")
        other = self.revocation_receipt("CLEAR", subject_issuer="another-issuer")
        self.assertEqual(self.assess(revocation=other).historical_status,
                         "REVOCATION_BINDING_MISMATCH")

    def test_revocation_clear_receipt_cannot_be_replayed_for_another_certificate(self):
        other = self.reissue(self.cert, certificate_id="cert-10")
        result = self.assess(cert=other, revocation=self.revocation)
        self.assertEqual(result.historical_status, "REVOCATION_BINDING_MISMATCH")
        updated = self.revocation_receipt("CLEAR", cert=other)
        self.assertEqual(self.assess(cert=other, revocation=updated).use_status,
                         "VALID_FOR_CURRENT_REVIEW")

    def test_certificate_same_id_reissued_content_cannot_reuse_old_clearance(self):
        changed = self.reissue(self.cert, use_until_exclusive=19)
        invalid = self.assess(cert=changed, revocation=self.revocation)
        self.assertEqual(invalid.historical_status, "REVOCATION_BINDING_MISMATCH")
        self.assertEqual(self.assess(cert=changed).use_status, "VALID_FOR_CURRENT_REVIEW")

    def test_stale_declared_decision_cannot_evade_actual_clock(self):
        for clock in (1, 2, 12):
            with self.subTest(clock=clock):
                d = replace(self.decision, at_time=clock)
                result = self.assess(decision=d, now=10)
                self.assertEqual(result.historical_status, "HISTORICALLY_APPLICABLE")
                self.assertEqual(result.use_status, "DECISION_TIME_NOT_CURRENT")

    def test_clock_source_failure_or_bad_type_is_denied(self):
        for clock_value in (None, True, -1, 2.0, "2"):
            with self.subTest(now=clock_value):
                result = self.assess(now=clock_value)
                self.assertEqual(result.historical_status, "CLOCK_OR_FRESHNESS_POLICY_UNAVAILABLE")
        self.assertEqual(self.assess(max_age=0).use_status, "NO_LIVE_EVIDENCE")

    def test_time_domain_mismatch_is_separately_denied(self):
        other_cert = self.reissue(self.cert, time_basis="CLOCK_OTHER_V1")
        self.assertEqual(self.assess(cert=other_cert).historical_status,
                         "CERTIFICATE_CLOCK_DOMAIN_MISMATCH")
        other_use = replace(self.decision, time_basis="CLOCK_OTHER_V1")
        self.assertEqual(self.assess(decision=other_use).use_status,
                         "DECISION_CLOCK_DOMAIN_MISMATCH")
        other_rev = self.revocation_receipt("CLEAR", time_basis="CLOCK_OTHER_V1")
        self.assertEqual(self.assess(revocation=other_rev).historical_status,
                         "REVOCATION_CLOCK_DOMAIN_MISMATCH")

    def test_independent_capture_authority_and_payload_availability(self):
        for outcome, expected in ((False, "CAPTURE_RIGHT_DENIED"),
                                  (None, "CAPTURE_RIGHT_UNKNOWN"),
                                  (1, "CAPTURE_RIGHT_UNKNOWN")):
            with self.subTest(capture=outcome):
                res = self.assess(capture=lambda event, v=outcome: v)
                self.assertEqual(res.historical_status, expected)
        for outcome, expected in ((False, "RETAINED_PAYLOAD_MISSING"),
                                  (None, "PAYLOAD_AVAILABILITY_UNKNOWN"),
                                  ("yes", "PAYLOAD_AVAILABILITY_UNKNOWN")):
            with self.subTest(payload=outcome):
                res = self.assess(payload=lambda event, v=outcome: v)
                self.assertEqual(res.historical_status, expected)

    def test_unsigned_admission_not_allowed_to_self_upgrade(self):
        with self.assertRaises(ValueError):
            replace(self.event, admission="QUALIFIED")

    def test_clearance_observed_before_certificate_issuance_not_valid(self):
        old_clear = self.revocation_receipt("CLEAR", observed_at=1)
        result = self.assess(revocation=old_clear)
        self.assertEqual(result.historical_status, "REVOCATION_PREDATES_CERTIFICATE")
        self.assertEqual(result.use_status, "REVOCATION_UNKNOWN")

    def test_local_freshness_limit_overrides_signed_longer_receipt_ttl(self):
        cert = self.reissue(self.cert, use_until_exclusive=20)
        d = replace(self.decision, at_time=10)
        clearance = self.revocation_receipt("CLEAR", cert=cert, fresh_until=19)
        result = self.assess(cert=cert, decision=d, revocation=clearance, max_age=4)
        self.assertEqual(result.historical_status, "REVOCATION_STALE")
        self.assertEqual(result.use_status, "REVOCATION_STALE")

    def test_signed_event_rebound_by_observer_time_and_payload_record(self):
        updated = self.recertify_event(self.event, captured_at=2)
        self.assertEqual(self.assess(event=updated).historical_status,
                         "EVENT_BINDING_MISMATCH")
        corrected = self.reissue(
            self.cert, event_record_sha256=sha256(signed_payload(updated)).hexdigest())
        self.assertEqual(self.assess(event=updated, cert=corrected).use_status,
                         "VALID_FOR_CURRENT_REVIEW")

    def test_revocation_must_be_latest_not_merely_within_signed_ttl(self):
        superseded = self.assess(latest=lambda receipt, cert, now: False)
        self.assertEqual(superseded.historical_status, "REVOCATION_SUPERSEDED")
        self.assertEqual(superseded.use_status, "REVOCATION_UNKNOWN")
        outage = self.assess(latest=lambda receipt, cert, now: None)
        self.assertEqual(outage.historical_status, "REVOCATION_STATE_UNKNOWN")
        self.assertEqual(outage.use_status, "REVOCATION_UNKNOWN")
        malicious = self.assess(latest=lambda receipt, cert, now: "True")
        self.assertEqual(malicious.use_status, "REVOCATION_UNKNOWN")

    def test_receiver_authentication_is_separate_from_permission(self):
        for auth, expect in ((False, "CALLER_NOT_AUTHENTICATED"),
                             (None, "CALLER_AUTHENTICATION_UNKNOWN"),
                             (1, "CALLER_AUTHENTICATION_UNKNOWN")):
            with self.subTest(auth=auth):
                r = self.assess(authenticated=lambda request, v=auth: v)
                self.assertEqual(r.historical_status, "HISTORICALLY_APPLICABLE")
                self.assertEqual(r.use_status, expect)

    def test_stale_or_missing_revocation_blocks_liveness(self):
        cert = self.reissue(self.cert, use_until_exclusive=20)
        stale = self.revocation_receipt("CLEAR", fresh_until=5, cert=cert)
        result = self.assess(cert=cert, revocation=stale, decision=replace(
            self.decision, at_time=10))
        self.assertEqual(result.historical_status, "REVOCATION_STALE")
        self.assertEqual(result.use_status, "REVOCATION_STALE")
        absent = self.assess(revocation=None)
        self.assertEqual(absent.use_status, "REVOCATION_UNKNOWN")
        unknown = self.assess(revocation=self.revocation_receipt("UNKNOWN"))
        self.assertEqual(unknown.historical_status, "REVOCATION_UNKNOWN")

    def test_revocation_observed_in_future_cannot_be_used_early(self):
        rev = self.revocation_receipt("CLEAR", observed_at=5)
        self.assertEqual(self.assess(revocation=rev).historical_status,
                         "REVOCATION_STALE")

    def test_use_not_before_respected_even_for_old_event(self):
        cert = self.reissue(self.cert, use_from=5, use_until_exclusive=20)
        result = self.assess(cert=cert)
        self.assertEqual(result.historical_status, "HISTORICALLY_APPLICABLE")
        self.assertEqual(result.use_status, "NOT_YET_VALID_FOR_USE")

    def test_malformed_time_and_empty_windows_rejected_before_signing(self):
        for bad in (True, False, 1.0, -1, "2", None):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                replace(self.decision, at_time=bad)
        with self.assertRaises(ValueError):
            replace(self.cert, use_from=3, use_until_exclusive=3)
        with self.assertRaises(ValueError):
            replace(self.cert, issued_at=3, use_from=2)
        with self.assertRaises(ValueError):
            replace(self.event, captured_at=20)

    def test_verifier_backend_outage_or_wrong_type_is_fail_closed(self):
        for verifier in (lambda record: None, lambda record: "true",
                         lambda record: 1, lambda record: 1 / 0):
            with self.subTest(verifier=verifier):
                self.assertEqual(self.assess(verifier=verifier).historical_status,
                                 "EVENT_ATTESTATION_INVALID")

    def test_same_certificate_contract_gates_social_and_agentic_f1_d1_refinement(self):
        # Pinned social finite handoff (8 -> 10 versus 8 -> 8);
        # pinned PR57 AG01/AG02 transfer_2 outputs (11.5 versus 8.875).
        # Actual separate model integrations are in test_theme18_structural_adequacy.
        model_cases = (
            ("social", "nested-social-v0.1", "joint_capacity",
             "joint_reallocation", {"public_current": 8},
             (("SOC-JOINT", 10, True), ("SOC-NO-JOINT", 8, False))),
            ("agentic", "vendor-ecosystem-v1", "transfer_2_response",
             "transfer_2", {"public_output": 10},
             (("AG01", 11.5, 1.6), ("AG02", 8.875, 0.4))),
        )

        for domain, scope, question, operation, visible_a, examples in model_cases:
            with self.subTest(model=domain):
                def build(at, deny_case=None):
                    cases = []
                    outcomes = []
                    for case_id, resulting_value, new_q in examples:
                        payload = sha256(repr((domain, case_id, new_q)).encode()).hexdigest()
                        event = self.recertify_event(
                            self.event, event_id="event-" + case_id,
                            payload_sha256=payload, scope=scope)
                        certificate = self.reissue(
                            self.cert, certificate_id="cert-" + case_id,
                            event_id=event.event_id, payload_sha256=payload,
                            event_record_sha256=sha256(signed_payload(event)).hexdigest(),
                            scope=scope)
                        review = replace(self.decision, scope=scope, question=question,
                                         at_time=at)
                        # Certificate is qualified for the precise receiving question.
                        certificate = self.reissue(certificate, question=question)
                        assessment = self.assess(
                            event=event, cert=certificate, decision=review, now=at,
                            revocation=self.revocation_receipt("CLEAR", cert=certificate),
                            source=lambda cert, event, c=case_id: c != deny_case,
                        )
                        outcomes.append(assessment)
                        eligible_q = assessment.use_status == "VALID_FOR_CURRENT_REVIEW"
                        cases.append(FiniteDecisionCase(
                            case_id, scope, question,
                            (visible_a, new_q) if eligible_q else visible_a,
                            resulting_value, "pinned-" + domain + "-referee",
                            observed_a_qualified=(deny_case is None or eligible_q),
                            successor_a={operation: resulting_value},
                        ))
                    diagnosis = assess_finite_adequacy(
                        cases, frame_id="dual-time-" + domain,
                        scope=scope, question=question, operations=(operation,))
                    return diagnosis, outcomes

                initial, positives = build(at=2)
                self.assertEqual(initial.structural_status,
                                 "ADEQUATE_IN_DECLARED_FINITE_FRAME")
                self.assertTrue(all(o.use_status == "VALID_FOR_CURRENT_REVIEW"
                                    for o in positives))
                expired, retrospectives = build(at=10)
                self.assertEqual(expired.structural_status, "REQUALIFICATION_WITNESSED")
                self.assertTrue(all(o.historical_status == "HISTORICALLY_APPLICABLE"
                                    and o.use_status == "EXPIRED_AT_USE"
                                    for o in retrospectives))
                refused, statuses = build(at=2, deny_case=examples[1][0])
                self.assertEqual(refused.structural_status, "UNKNOWN")
                self.assertEqual(statuses[1].historical_status, "SOURCE_NOT_QUALIFIED")
                self.assertNotEqual(statuses[1].use_status, "VALID_FOR_CURRENT_REVIEW")
                # Missing qualification for one partial A+Q row is UNKNOWN,
                # never a finite-frame adequacy certificate.

    def test_hmac_signatures_are_domain_separated_and_typed(self):
        self.assertTrue(verify_hmac(self.event, self.keys))
        self.assertTrue(verify_hmac(self.cert, self.keys))
        self.assertTrue(verify_hmac(self.revocation, self.keys))
        self.assertNotEqual(signed_payload(self.event), signed_payload(self.cert))
        self.assertFalse(verify_hmac(replace(self.cert, signature=self.event.signature),
                                     self.keys))
        with self.assertRaises(ValueError):
            sign_hmac(self.event, b"short")


if __name__ == "__main__":
    unittest.main(verbosity=2)
