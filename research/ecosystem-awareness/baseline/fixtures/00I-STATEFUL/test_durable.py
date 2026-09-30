"""Real subprocess termination and concurrent delivery; local DB effects only."""
import json
import subprocess
import sys
import tempfile
import unittest
from dataclasses import asdict, replace
from pathlib import Path

from durable_executor import DurableExecutor
from model import Guard, Intent, Sources, World, recover_decision


class DurableTests(unittest.TestCase):
    evidence = []

    def setUp(self):
        self.record = dict(test=self.id(), observations=[])
        self.evidence.append(self.record)
        self.request_number = 0
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.db = self.root / "state.sqlite"
        self.world = World()
        self.executor = DurableExecutor(self.db)
        self.executor.initialize(self.world)
        self.guard = Guard(self.world, Sources(self.world), "guarded")
        self.manifest = self.world.manifest()
        self.basis = {k: self.world.values[k] for k in self.manifest}
        self.request = self.make_request(Intent())

    def make_request(self, intent):
        decision, _, permit = self.guard.decide(intent, self.basis, self.manifest)
        self.assertEqual(decision, "EXECUTE")
        self.executor.register(permit)
        return dict(intent=asdict(intent), permit=asdict(permit), now=122)

    def start(self, request=None, crash="none", non_atomic=False):
        request = self.request if request is None else request
        self.request_number += 1
        path = self.root / (str(self.request_number) + "-request.json")
        path.write_text(json.dumps(request))
        self.record["observations"].append(dict(event="request_submitted", request=json.loads(json.dumps(request)),
                                                crash=crash, non_atomic_control=non_atomic))
        cmd = [sys.executable, "-B", str(Path(__file__).with_name("durable_executor.py")),
               "--database", str(self.db), "--request", str(path), "--crash", crash]
        if non_atomic:
            cmd.append("--non-atomic-control")
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        def cleanup():
            if process.poll() is None:
                process.kill()
                process.wait()
        self.addCleanup(cleanup)
        return process

    def finish(self, process, crash=False):
        stdout, stderr = process.communicate(timeout=15)
        self.record["observations"].append(dict(event="process_result", exit_code=process.returncode,
                                                stdout=stdout.strip(), stderr=stderr.strip()))
        self.assertEqual(process.returncode, 73 if crash else 0, stderr)
        return stdout.strip()

    def assert_state(self, generation, effects, receipts):
        state = DurableExecutor(self.db).snapshot()
        self.record["observations"].append(dict(event="database_snapshot", **state))
        self.assertEqual(state["state"][0][1], generation)
        self.assertEqual(state["state"][0][3], effects)
        self.assertEqual(len(state["receipts"]), receipts)

    def test_guarded_continuity_through_persistent_executor(self):
        self.assertEqual(self.finish(self.start()), "APPLIED")
        self.assert_state(216, 1, 1)

    def test_crash_before_effect_then_retry(self):
        self.finish(self.start(crash="before_effect"), crash=True)
        self.assert_state(217, 0, 0)
        self.assertEqual(self.finish(self.start()), "APPLIED")
        self.assert_state(216, 1, 1)

    def test_crash_after_effect_before_commit_rolls_back_both(self):
        self.finish(self.start(crash="after_effect"), crash=True)
        self.assert_state(217, 0, 0)
        self.assertEqual(self.finish(self.start()), "APPLIED")
        self.assert_state(216, 1, 1)

    def test_crash_after_commit_before_ack_does_not_repeat_effect(self):
        self.finish(self.start(crash="after_commit"), crash=True)
        self.assert_state(216, 1, 1)
        self.assertEqual(self.finish(self.start()), "ALREADY_APPLIED")
        self.assert_state(216, 1, 1)

    def test_four_concurrent_duplicate_deliveries_apply_once(self):
        # Independent processes; scheduling order deliberately unspecified.
        processes = [self.start() for _ in range(4)]
        results = [self.finish(p) for p in processes]
        self.assertEqual(results.count("APPLIED"), 1)
        self.assertEqual(results.count("ALREADY_APPLIED"), 3)
        self.assert_state(216, 1, 1)

    def test_concurrent_distinct_intents_reject_stale_second_operation(self):
        second = self.make_request(replace(Intent(), id="PATCH-C"))
        results = [self.finish(p) for p in (self.start(), self.start(second))]
        self.assertEqual(sorted(results), ["APPLIED", "REJECTED"])
        self.assert_state(216, 1, 1)

    def test_material_change_after_guard_rejects_without_effect(self):
        self.executor.material_change(generation=218)
        self.assertEqual(self.finish(self.start()), "REJECTED")
        self.assert_state(218, 0, 0)

    def test_receipt_payload_conflict_survives_process_restart(self):
        self.assertEqual(self.finish(self.start()), "APPLIED")
        self.request["intent"]["desired_generation"] = 215
        self.assertEqual(self.finish(self.start()), "CONFLICT")
        self.assert_state(216, 1, 1)

    def test_forged_permit_payload_cannot_change_effect(self):
        self.request["permit"]["intent"]["desired_generation"] = 215
        self.request["intent"]["desired_generation"] = 215
        self.assertEqual(self.finish(self.start()), "REJECTED")
        self.assert_state(217, 0, 0)

    def test_exact_expiry_blocks_effect(self):
        self.request["now"] = self.request["permit"]["expires"]
        self.assertEqual(self.finish(self.start()), "REJECTED")
        self.assert_state(217, 0, 0)

    def test_non_atomic_control_leaves_effect_without_receipt(self):
        self.finish(self.start(crash="after_effect", non_atomic=True), crash=True)
        self.assert_state(216, 1, 0)
        # The safe retry cannot acknowledge the unknown prior result. It rejects
        # the stale permit, preserving rather than disguising the receipt gap.
        self.assertEqual(self.finish(self.start()), "REJECTED")
        self.assert_state(216, 1, 0)

    def test_recovery_permit_then_lost_ack_is_not_a_second_execution(self):
        self.world.faults["freeze"] = "unavailable"

        def advance(at):
            self.world.advance(at)
            if at >= 122:
                self.world.faults["freeze"] = None

        disposition, _, permit = recover_decision(
            self.world, self.guard, Intent(), self.basis, self.manifest, advance, 125)
        self.assertEqual(disposition, "EXECUTE")
        self.executor.register(permit)
        request = dict(intent=asdict(Intent()), permit=asdict(permit), now=122)
        self.finish(self.start(request, crash="after_commit"), crash=True)
        self.assert_state(216, 1, 1)
        # After the horizon, acknowledge the already committed result only.
        request["now"] = 126
        self.assertEqual(self.finish(self.start(request)), "ALREADY_APPLIED")
        self.assert_state(216, 1, 1)


if __name__ == "__main__":
    unittest.main()
