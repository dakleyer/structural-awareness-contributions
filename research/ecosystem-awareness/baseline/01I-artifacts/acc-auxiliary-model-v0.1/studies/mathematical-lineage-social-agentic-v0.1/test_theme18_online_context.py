"""Stage A tests of retained pre-admission traces and scoped proof-work utility.

Follows main-corpus SA-O2/O4/O5 within a declared finite example. This is NOT
a deployed Theme #18 verifier, a source-authentication service or an RA monitor.
"""
from __future__ import annotations

import unittest

from qualified_certificates import DecisionUse, evaluate_certificate as requalify

DOMAIN = tuple(range(10))


def _in_qualified_domain(x):
    """The finite proof covers only the declared integer states, not aliases."""
    return type(x) is int and x in DOMAIN


def capture_pre_admission(event, *, permitted, capture_enabled):
    """Current narrow filter does not know 'new-route'; retain if authorized."""
    if not permitted or not capture_enabled:
        return None
    return {"event": event, "admission": "UNRESOLVED",
            "scope": "route-v1", "time": 1, "source": "observer-A"}


# The earlier dict/verified=True requalify shortcut has been replaced by the
# independently signed, scoped, dual-time evaluator qualified_certificates.
# A raw retained trace is not a certificate or an action authorization.

def full_verdict(x):
    """A fixed substantive decision over the declared integer states."""
    if not _in_qualified_domain(x):
        raise ValueError("outside qualified domain")
    return "REJECT" if x % 2 == 0 else "ACCEPT"


def guard(x):
    return x % 2 == 0


def prove_guard_sound(domain, predicate):
    """Toy finite proof: guard implies the original substantive REJECT."""
    return all(not predicate(x) or full_verdict(x) == "REJECT"
               for x in domain)


def guarded_verdict(x, *, guard_validated, proof_scope):
    """Never skip evaluation outside the proof's typed finite domain."""
    # Scope membership is a separate premise from proof validity (M28-02).
    if not _in_qualified_domain(x):
        raise ValueError("outside qualified domain")
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
    def test_retained_unresolved_is_preserved_but_not_auto_qualified(self):
        record = capture_pre_admission("new-route", permitted=True,
                                       capture_enabled=True)
        self.assertEqual(record["admission"], "UNRESOLVED")
        self.assertEqual(record["source"], "observer-A")

    def test_irreversible_loss_has_no_later_replay_source(self):
        lost = capture_pre_admission("new-route", permitted=True,
                                     capture_enabled=False)
        self.assertIsNone(lost)

    def test_no_capture_when_rights_absent(self):
        lost = capture_pre_admission("new-route", permitted=False,
                                     capture_enabled=True)
        self.assertIsNone(lost)

    def test_raw_unsigned_dict_cannot_be_used_as_signed_event(self):
        raw = capture_pre_admission("new-route", permitted=True,
                                    capture_enabled=True)
        decision = DecisionUse(
            decision_id="d1", scope="route-v1", context_version="v1",
            receiver="receiver", purpose="review", question="new-route",
            rule_version="v1", time_basis="FIXTURE_TICKS_V1", at_time=2,
        )
        with self.assertRaises(TypeError):
            requalify(
                raw, None, decision,
                verify_attestation=lambda record: True,
                source_qualified=lambda cert, event: True,
                capture_right=lambda event: True,
                request_authenticated=lambda request: True,
                retention_right=lambda event, request: True,
                payload_available=lambda event: True,
                evidence_use_right=lambda cert, request: True,
                revocation=None,
                trusted_clock=lambda basis: 2,
                max_revocation_age=60,
                revocation_current=lambda rev, cert, now: True,
            )

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

    def test_outside_declared_domain_never_uses_validated_guard(self):
        # A proof for 0..9 says nothing about x=12, even when guard(12).
        for x in (-2, 10, 11, 12):
            with self.subTest(x=x):
                with self.assertRaisesRegex(ValueError, "outside qualified domain"):
                    full_verdict(x)
                with self.assertRaisesRegex(ValueError, "outside qualified domain"):
                    guarded_verdict(x, guard_validated=True, proof_scope=DOMAIN)

    def test_invalid_case_never_gains_scope_from_fallback_or_weak_proof(self):
        # Reject out-of-domain states with or without the proof shortcut.
        for valid, scope in ((False, DOMAIN),
                             (True, tuple(range(6))),
                             (True, tuple(range(13)))):
            with self.subTest(valid=valid, scope=scope):
                with self.assertRaisesRegex(ValueError, "outside qualified domain"):
                    guarded_verdict(12, guard_validated=valid, proof_scope=scope)

    def test_bool_and_float_equality_do_not_extend_integer_proof(self):
        # Python equality makes True == 1 and 2.0 == 2; neither is an
        # enumerated integer input of this typed finite fixture.
        for x in (False, True, 2.0, 3.0):
            with self.subTest(x=repr(x)):
                with self.assertRaisesRegex(ValueError, "outside qualified domain"):
                    full_verdict(x)
                with self.assertRaisesRegex(ValueError, "outside qualified domain"):
                    guarded_verdict(x, guard_validated=True, proof_scope=DOMAIN)

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
