"""Adversarial contracts for temporal decisions and actual simulated effects."""
import ast
import json
import unittest
from copy import deepcopy
from dataclasses import replace
from pathlib import Path

from model import Executor, Guard, Intent, Permit, Sources, World, run_case, usable
from reproduce import evaluate

HERE = Path(__file__).resolve().parent
CASES = {c["id"]: c for c in json.loads((HERE / "fixtures.json").read_text())["cases"]}
ORACLE = json.loads((HERE / "oracle.json").read_text())


class StatefulTests(unittest.TestCase):
    def test_declared_matrix_including_expected_failures(self):
        failed = []
        for name, case in CASES.items():
            with self.subTest(case=name):
                actual = run_case(case)
                passed = all(evaluate(actual, ORACLE["expectations"][name]).values())
                if not passed:
                    failed.append(name)
                self.assertEqual(passed, name not in ORACLE["expected_failure_cases"])
        self.assertEqual(set(failed), set(ORACLE["expected_failure_cases"]))

    def test_freeze_only_pair_changes_effect_with_same_grant_and_generation(self):
        positive = run_case(CASES["continuity"])
        negative = run_case(CASES["freeze_before_use"])
        self.assertEqual(positive["final_generation"], 216)
        self.assertEqual(negative["final_generation"], 217)
        self.assertEqual(positive["effects"], 1)
        self.assertEqual(negative["effects"], 0)
        queued = lambda r: next(e for e in r["trace"] if e["event"] == "queued")
        self.assertEqual(queued(positive), queued(negative))

    def test_race_permits_then_executor_rejects_without_effect(self):
        result = run_case(CASES["freeze_after_check"])
        self.assertTrue(any(e["event"] == "permit_issued" for e in result["trace"]))
        self.assertTrue(any(e.get("reason") == "revision_binding_lost" for e in result["trace"]))
        self.assertEqual(result["effects"], 0)
        unbound = run_case(CASES["unbound_race"])
        self.assertEqual(unbound["effects"], 1)

    def test_both_reference_omission_and_writer_bypass_remain_visible_failures(self):
        for name in ("shared_omission", "writer_bypass"):
            with self.subTest(case=name):
                result = run_case(CASES[name])
                self.assertTrue(result["final_state"]["freeze"])
                self.assertTrue(result["applied"])

    def test_unknown_evidence_closes_in_bounded_time_and_never_writes(self):
        result = run_case(CASES["source_unavailable"])
        self.assertEqual(result["disposition"], "ESCALATE")
        self.assertEqual(result["control_burden"]["elapsed_seconds"], 5)
        self.assertEqual(result["effects"], 0)
        self.assertTrue(any(e["event"] == "bounded_escalation" for e in result["trace"]))

    def test_dynamic_manifest_peer_passes_both_closed_and_open_new_dependency(self):
        closed = run_case(CASES["d1_dynamic_manifest"])
        opened = run_case(CASES["d1_open_continuity"])
        self.assertFalse(closed["applied"])
        self.assertTrue(opened["applied"])
        self.assertTrue(any(e.get("observation", {}).get("source") == "freeze_b" for e in closed["trace"]))

    def test_duplicate_delivery_does_not_reapply(self):
        result = run_case(CASES["duplicate_delivery"])
        self.assertEqual(result["effects"], 1)
        self.assertEqual(sum(e["event"] == "execution_attempt" for e in result["trace"]), 2)

    def test_candidate_does_not_read_oracle_or_select_on_case_name(self):
        tree = ast.parse((HERE / "model.py").read_text())
        imported = {n.module for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)}
        self.assertEqual(imported, {"copy", "dataclasses"})
        case = deepcopy(CASES["freeze_before_use"])
        original = run_case(case)
        case["id"] = "unseen-case-name"
        changed = run_case(case)
        original.pop("id")
        changed.pop("id")
        self.assertEqual(original, changed)
        # Oracle mutation changes the evaluator's answer, not the runtime output.
        wrong_oracle = dict(disposition="EXECUTE", applied=True, final_generation=216)
        self.assertFalse(all(evaluate(changed, wrong_oracle).values()))

    def test_effect_assertion_detects_success_label_without_state_change(self):
        actual = run_case(CASES["continuity"])
        actual["final_generation"] = 217
        self.assertFalse(all(evaluate(actual, ORACLE["expectations"]["continuity"]).values()))

    def test_freshness_boundary_and_future_observation(self):
        obs = dict(available=True, value=False, owner="owner", sampled_at=0)
        self.assertTrue(usable(obs, "owner", 59, 60))
        self.assertFalse(usable(obs, "owner", 60, 60))
        self.assertFalse(usable(obs, "owner", -1, 60))
        self.assertFalse(run_case(CASES["source_expires_before_act"])["applied"])

    def test_forged_and_substituted_permits_are_rejected(self):
        w = World()
        intent = Intent()
        permit = Permit("fake", intent, w.revision, 200)
        self.assertEqual(Executor(w).attempt(intent, permit), "REJECTED")
        w.permits[permit.id] = permit
        self.assertEqual(Executor(w).attempt(replace(intent, target="db-8"), permit), "REJECTED")
        self.assertEqual(w.writes, 0)

    def test_inconsistent_multi_source_snapshot_is_not_permitted(self):
        w = World()
        sources = Sources(w)
        manifest = w.manifest()
        basis = {k: w.values[k] for k in manifest}
        original = sources.read

        def racing_read(source):
            if source == "freeze":
                w.change(dict(at=w.now, field="freeze", value=True))
            return original(source)

        sources.read = racing_read
        disposition, reason, permit = Guard(w, sources, "guarded").decide(Intent(), basis, manifest)
        self.assertEqual(disposition, "HOLD")
        self.assertEqual(reason, "inconsistent_snapshot")
        self.assertIsNone(permit)

    def test_bounded_event_interleavings_on_both_sides_of_check(self):
        for at in (121, 2519, 2520, 2521, 2522):
            with self.subTest(freeze_at=at):
                case = deepcopy(CASES["freeze_before_use"])
                case["events"][0]["at"] = at
                self.assertFalse(run_case(case)["applied"])

    def test_freshness_update_preserves_previously_added_finance_dependency(self):
        for fields in (("manifest", "freshness_budget"), ("freshness_budget", "manifest")):
            with self.subTest(order=fields):
                case = deepcopy(CASES["d1_dynamic_manifest"])
                case["events"] = [dict(at=1200 + i * 100, field=field,
                                       value="v18" if field == "manifest" else 5)
                                  for i, field in enumerate(fields)]
                result = run_case(case)
                self.assertFalse(result["applied"])
                self.assertTrue(any(e.get("observation", {}).get("source") == "freeze_b" for e in result["trace"]))


if __name__ == "__main__":
    unittest.main()
