"""Adversarial boundary tests added after the first 33-row simulation."""
import unittest
from dataclasses import replace

from model import Executor, Guard, Intent, Sources, World
from reproduce import evaluate


class ContractEdges(unittest.TestCase):
    def decision(self, mutate, on_source="manifest"):
        w = World()
        s = Sources(w)
        manifest = w.manifest()
        basis = {k: w.values[k] for k in manifest}
        original = s.read

        def altered(source):
            obs = original(source)
            if source == on_source:
                mutate(obs)
            return obs

        s.read = altered
        return Guard(w, s, "guarded").decide(Intent(), basis, manifest)

    def test_empty_manifest_cannot_authorise(self):
        self.assertEqual(self.decision(lambda o: o.update(value={}))[0], "HOLD")

    def test_malformed_rule_is_unknown_not_exception(self):
        self.assertEqual(self.decision(lambda o: o.update(value={"freeze": {}}))[0], "HOLD")

    def test_source_identity_must_match_requested_source(self):
        self.assertEqual(self.decision(lambda o: o.update(source="another-calendar"), "freeze")[0], "HOLD")

    def test_available_requires_boolean_true(self):
        self.assertEqual(self.decision(lambda o: o.update(available="false"), "freeze")[0], "HOLD")

    def test_missing_metadata_is_unknown_not_exception(self):
        self.assertEqual(self.decision(lambda o: o.pop("sampled_at"), "freeze")[0], "HOLD")

    def test_blank_version_does_not_establish_provenance(self):
        self.assertEqual(self.decision(lambda o: o.update(version=""), "freeze")[0], "HOLD")

    def test_boolean_revision_is_not_integer_revision(self):
        self.assertEqual(self.decision(lambda o: o.update(revision=True), "freeze")[0], "HOLD")

    def test_malformed_freshness_budget_is_unknown(self):
        def mutate(o):
            o["value"]["freeze"]["max_age"] = "sixty"
        self.assertEqual(self.decision(mutate)[0], "HOLD")

    def test_zero_budget_is_unknown(self):
        def mutate(o):
            o["value"]["freeze"]["max_age"] = 0
        self.assertEqual(self.decision(mutate)[0], "HOLD")

    def test_permits_for_two_intents_do_not_overwrite_each_other(self):
        w = World()
        g = Guard(w, Sources(w), "guarded")
        manifest = w.manifest()
        basis = {k: w.values[k] for k in manifest}
        first = Intent()
        second = replace(first, id="PATCH-C")
        p1 = g.decide(first, basis, manifest)[2]
        p2 = g.decide(second, basis, manifest)[2]
        self.assertNotEqual(p1.id, p2.id)
        self.assertEqual(Executor(w).attempt(first, p1), "APPLIED")
        self.assertEqual(Executor(w).attempt(second, p2), "REJECTED")

    def test_completed_id_with_different_payload_is_conflict_not_success(self):
        w = World()
        manifest = w.manifest()
        intent = Intent()
        permit = Guard(w, Sources(w), "guarded").decide(
            intent, {k: w.values[k] for k in manifest}, manifest)[2]
        executor = Executor(w)
        self.assertEqual(executor.attempt(intent, permit), "APPLIED")
        self.assertEqual(executor.attempt(replace(intent, desired_generation=215), permit), "REJECTED")
        self.assertEqual(w.writes, 1)

    def test_empty_oracle_cannot_vacuously_pass(self):
        with self.assertRaises(ValueError):
            evaluate(dict(disposition="EXECUTE", applied=True, final_generation=216), {})

    def test_evaluator_rejects_wrong_types(self):
        actual = dict(disposition="EXECUTE", applied=1, final_generation=216)
        expected = dict(disposition="EXECUTE", applied=True, final_generation=216)
        self.assertFalse(all(evaluate(actual, expected).values()))


if __name__ == "__main__":
    unittest.main()
