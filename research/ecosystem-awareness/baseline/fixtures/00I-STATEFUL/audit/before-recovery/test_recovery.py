"""Bounded re-entry must regain continuity without bypassing current evidence."""
import unittest
from model import run_case


def recovery_case(extra=(), **options):
    return dict(id="recovery-probe", mode="guarded", recovery=True,
                events=[dict(at=2519, field="observation", value="freeze", fault="unavailable"),
                        *extra], **options)


def returns(at=2521):
    return dict(at=at, field="observation", value="freeze", fault=None)


class RecoveryTests(unittest.TestCase):
    def test_recovered_evidence_restores_continuity_before_deadline(self):
        for at in (2521, 2523, 2524):
            with self.subTest(return_at=at):
                result = run_case(recovery_case([returns(at)]))
                self.assertEqual(result["disposition"], "EXECUTE")
                self.assertEqual(result["effects"], 1)
                self.assertLess(result["control_burden"]["elapsed_seconds"], 5)

    def test_returning_source_does_not_restore_superseded_decision(self):
        result = run_case(recovery_case([dict(at=2521, field="patch_b", value=218), returns()]))
        self.assertEqual(result["disposition"], "DENY")
        self.assertEqual(result["final_generation"], 218)
        self.assertEqual(result["effects"], 0)

    def test_reentry_reloads_new_dependency(self):
        result = run_case(recovery_case([dict(at=2521, field="manifest", value="v18"), returns()]))
        self.assertEqual(result["disposition"], "DENY")
        self.assertTrue(any(e.get("observation", {}).get("source") == "freeze_b" for e in result["trace"]))

    def test_unchanged_unknown_has_finite_attempts_and_fixed_deadline(self):
        result = run_case(recovery_case())
        attempts = [e for e in result["trace"] if e["event"] == "recovery_attempt"]
        self.assertEqual([e["at"] for e in attempts], [2520, 2522, 2524])
        self.assertEqual(result["disposition"], "ESCALATE")
        self.assertEqual(result["control_burden"]["elapsed_seconds"], 5)
        self.assertEqual(result["effects"], 0)

    def test_exact_deadline_recovery_does_not_silently_extend_permission(self):
        result = run_case(recovery_case([returns(2525)]))
        self.assertEqual(result["disposition"], "ESCALATE")
        self.assertEqual(result["effects"], 0)

    def test_recovered_action_still_rejects_change_between_recheck_and_act(self):
        result = run_case(recovery_case([returns(), dict(at=2523, field="freeze", value=True)], act_at=2524))
        self.assertEqual(result["disposition"], "DENY")
        self.assertEqual(result["effects"], 0)
        self.assertTrue(any(e.get("reason") == "revision_binding_lost" for e in result["trace"]))

    def test_recovery_does_not_renew_expired_grant(self):
        result = run_case(recovery_case([returns()], grant_expires=2522))
        self.assertEqual(result["disposition"], "DENY")
        self.assertEqual(result["effects"], 0)

    def test_duplicate_delivery_after_recovery_has_one_effect(self):
        result = run_case(recovery_case([returns()], duplicate=True))
        self.assertEqual(result["effects"], 1)
        self.assertTrue(any(e.get("reason") == "already_applied" for e in result["trace"]))

    def test_deadline_also_bounds_permit_and_dispatch(self):
        result = run_case(recovery_case([returns()], act_at=2526))
        self.assertEqual(result["disposition"], "ESCALATE")
        self.assertEqual(result["effects"], 0)
        permits = [e["permit"] for e in result["trace"] if e["event"] == "permit_issued"]
        self.assertTrue(permits)
        self.assertLessEqual(permits[-1]["expires"], 2525)
        self.assertEqual(result["control_burden"]["elapsed_seconds"], 5)

    def test_clear_prohibition_is_not_automatically_reopened(self):
        case = dict(id="denied", mode="guarded", recovery=True,
                    events=[dict(at=2519, field="freeze", value=True),
                            dict(at=2521, field="freeze", value=False)])
        result = run_case(case)
        self.assertEqual(result["disposition"], "DENY")
        self.assertEqual(result["effects"], 0)
        self.assertEqual(sum(e["event"] == "recovery_attempt" for e in result["trace"]), 1)


if __name__ == "__main__":
    unittest.main()
