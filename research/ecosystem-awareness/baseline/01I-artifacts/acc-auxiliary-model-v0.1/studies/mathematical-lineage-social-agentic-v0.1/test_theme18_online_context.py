"""Stage A tests of retained pre-admission traces and scoped proof-work utility.

Follows main-corpus SA-O2/O4/O5 within a declared finite example. This is NOT
a deployed Theme #18 verifier, a source-authentication service or an RA monitor.
"""
from __future__ import annotations

import unittest

DOMAIN = tuple(range(10))


def capture_pre_admission(event, *, permitted, capture_enabled):
    """Current narrow filter does not know 'new-route'; retain if authorized."""
    if not permitted or not capture_enabled:
        return None
    return {"event": event, "admission": "UNRESOLVED",
            "scope": "route-v1", "time": 1, "source": "observer-A"}


def requalify(retained, certificate):
    """Only a qualified scope-compatible *rule* may reinterpret a retained event."""
    if retained is None:
        return "NO_REPLAY_SOURCE"
    if certificate is None:
        return "UNRESOLVED"
    if (not certificate.get("verified", False)
        or certificate.get("source_scope") != retained["scope"]
        or certificate.get("expires_before") < retained["time"]):
        return "CERTIFICATE_UNSUPPORTED"
    if certificate.get("target_event") != retained["event"]:
        return "NOT_APPLICABLE_TO_EVENT"
    return "ADMISSIBLE_FOR_NEW_REVIEW"


def full_verdict(x):
    """A fixed substantive decision: rejection on even numbers."""
    if x not in DOMAIN:
        raise ValueError("outside qualified domain")
    return "REJECT" if x % 2 == 0 else "ACCEPT"


def guard(x):
    return x % 2 == 0


def prove_guard_sound(domain, predicate):
    """Toy finite proof: guard implies the original substantive REJECT."""
    return all(not predicate(x) or full_verdict(x) == "REJECT"
               for x in domain)


def guarded_verdict(x, *, guard_validated, proof_scope):
    """Never skip substantive decision without matching qualified proof."""
    if not guard_validated or proof_scope != DOMAIN:
        return full_verdict(x), False
    if guard(x):
        return "REJECT", True
    return full_verdict(x), False


def ledger(n, positive_guards, *,
           original_check_cost=10, guard_check_cost=1,
           verified_proof_full_lifecycle_cost=30):
    """Synthetic cost units, not measured runtime or actual inspection price."""
    conventional = n * original_check_cost
    candidate = (n * guard_check_cost
                 + (n - positive_guards) * original_check_cost
                 + verified_proof_full_lifecycle_cost)
    return {"full_check": conventional, "guarded": candidate,
            "gain": conventional - candidate}


class OnlineContextTests(unittest.TestCase):
    def setUp(self):
        self.certificate = {"verified": True, "source_scope": "route-v1",
                            "expires_before": 3, "target_event": "new-route"}

    def test_retained_unresolved_requalifies_with_actual_new_certificate(self):
        record = capture_pre_admission("new-route", permitted=True,
                                       capture_enabled=True)
        self.assertEqual(record["admission"], "UNRESOLVED")
        self.assertEqual(requalify(record, self.certificate),
                         "ADMISSIBLE_FOR_NEW_REVIEW")

    def test_irreversible_loss_has_no_later_recovery(self):
        lost = capture_pre_admission("new-route", permitted=True,
                                     capture_enabled=False)
        self.assertEqual(requalify(lost, self.certificate), "NO_REPLAY_SOURCE")

    def test_no_capture_when_rights_absent(self):
        lost = capture_pre_admission("new-route", permitted=False,
                                     capture_enabled=True)
        self.assertEqual(requalify(lost, self.certificate), "NO_REPLAY_SOURCE")

    def test_unverified_certificate_cannot_promote(self):
        r = capture_pre_admission("new-route", permitted=True,
                                  capture_enabled=True)
        bad = dict(self.certificate, verified=False)
        self.assertEqual(requalify(r, bad), "CERTIFICATE_UNSUPPORTED")

    def test_wrong_scope_or_expired_certificate_cannot_promote(self):
        r = capture_pre_admission("new-route", permitted=True,
                                  capture_enabled=True)
        for bad in (dict(self.certificate, source_scope="other"),
                    dict(self.certificate, expires_before=0)):
            with self.subTest(bad=bad):
                self.assertEqual(requalify(r, bad), "CERTIFICATE_UNSUPPORTED")

    def test_wrong_event_does_not_reinterpret_event(self):
        r = capture_pre_admission("new-route", permitted=True,
                                  capture_enabled=True)
        bad = dict(self.certificate, target_event="another-route")
        self.assertEqual(requalify(r, bad), "NOT_APPLICABLE_TO_EVENT")

    def test_absent_new_certificate_keeps_unknown(self):
        r = capture_pre_admission("new-route", permitted=True,
                                  capture_enabled=True)
        self.assertEqual(requalify(r, None), "UNRESOLVED")

    def test_shortcut_requires_real_finite_proof(self):
        self.assertTrue(prove_guard_sound(DOMAIN, guard))
        self.assertFalse(prove_guard_sound(DOMAIN, lambda x: x % 2 == 1))

    def test_guarded_and_full_agree_on_all_declared_states(self):
        for x in DOMAIN:
            with self.subTest(x=x):
                actual, used = guarded_verdict(
                    x, guard_validated=True, proof_scope=DOMAIN)
                self.assertEqual(actual, full_verdict(x))
                self.assertEqual(used, x % 2 == 0)

    def test_proof_outside_validity_scope_cannot_skip(self):
        x = 2
        v, skipped = guarded_verdict(
            x, guard_validated=True, proof_scope=tuple(range(6)))
        self.assertEqual(v, full_verdict(x))
        self.assertFalse(skipped)

    def test_proof_work_cost_can_save_or_lose(self):
        self.assertEqual(ledger(10, 5)["gain"], 10)
        self.assertEqual(ledger(2, 1)["gain"], -22)

    def test_competent_same_guard_conventional_peer_ties(self):
        our = ledger(10, 5)
        peer = ledger(10, 5)
        self.assertEqual(our, peer)


if __name__ == "__main__":
    unittest.main(verbosity=2)
