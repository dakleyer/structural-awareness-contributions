"""Finite checks for Stage-A Theme 18/Regime Awareness fixture expectations.

No real RA detector, operator measurement, authority service or agentic system
is implemented here. The independently frozen JSON supplies miniature inputs
and predictions. REFERENCE_ONLY cases are deliberately not scored.
Python standard library only.
"""
from __future__ import annotations

import json
import unittest
from pathlib import Path


FIXTURE = Path(__file__).with_name("09_THEME18_FINITE_FIXTURE_CASES_v0.1.json")


def pairs(n):
    for i in range(n):
        for j in range(i + 1, n):
            yield i, j


def quotient_adequate(observation, question, operations):
    """Check exact deterministic D1 within an enumerated closed state domain.

    Integer op targets are state indices, not labels in a production API.
    Returns the first same-observation, decision- or successor-conflicting pair.
    """
    n = len(observation)
    assert len(question) == n
    assert all(len(op) == n and all(0 <= k < n for k in op) for op in operations)
    for i, j in pairs(n):
        if observation[i] != observation[j]:
            continue
        if question[i] != question[j]:
            return False, [i, j]
        for op in operations:
            if observation[op[i]] != observation[op[j]]:
                return False, [i, j]
    return True, None


def calculate(case):
    kind, p = case["kind"], case["input"]

    if kind == "MULTIOBJECTIVE_FRAME":
        # No agent/regulator implementation: a fixed mathematical choice rule.
        # An independently qualified safety input, NOT the RA direction alone,
        # establishes the post-change admissible candidate set.
        assert p["operator"] == "lexicographic-safety-veto-then-service-minus-cost"
        def choose(options):
            allowed = [x for x in options if x["safety_ok"]]
            if not allowed:
                return None
            return max(allowed, key=lambda x: (x["service"] - x["cost"], x["id"]))["id"]
        signal = None if not p["context_qualified"] else (
            0 if abs(p["current"]-p["baseline"]) < p["threshold"]
            else (1 if p["current"] > p["baseline"] else -1)
        )
        return {
            "ra_signal": signal,
            "before_choice": choose(p["old_candidates"]),
            "after_choice_given_qualified_evidence":
                choose(p["post_candidates_after_independent_safety_evidence"])
                if p["post_safety_evidence_qualified"] else None,
            "operator_unchanged": True,
        }

    if kind == "QUALIFIED_RA_SIGNAL":
        # Illustrative threshold calculation only. NOT a contextual sufficiency
        # validator, true RA structural invariant, or causal detector.
        if not p["context_qualified"]:
            return {"signal": None}
        diff = p["current"] - p["baseline"]
        return {"signal": 0 if abs(diff) < p["threshold"] else (1 if diff > 0 else -1)}

    if kind == "EXACT_QUOTIENT":
        old_ok, _ = quotient_adequate(p["observation"], p["question"],
                                       p["old_operations"])
        new_ok, witness = quotient_adequate(p["observation"], p["question"],
                                            p["new_operations"])
        return {
            "old_adequate": old_ok,
            "new_adequate": new_ok,
            "first_new_operation_witness": witness,
        }

    if kind == "SUPPLEMENTARY_Q":
        observation, question, queries = (
            p["observation"], p["question"], p["queries"]
        )
        n = len(observation)
        assert all(len(q) == n for q in queries)
        unresolved = [
            [i, j] for i, j in pairs(n)
            if observation[i] == observation[j] and question[i] != question[j]
        ]
        q_only = all(
            any(q[i] != q[j] for q in queries)
            for i, j in pairs(n) if question[i] != question[j]
        )
        combined = all(
            any(q[i] != q[j] for q in queries)
            for i, j in unresolved
        )
        # This miniature has ONE selected eligible Q and additive cost;
        # it does NOT solve the general minimum-cost subset problem.
        assert len(queries) == 1 and len(p["query_costs"]) == 1
        return {
            "required_pairs": unresolved,
            "q_only_adequate": q_only,
            "observation_plus_q_adequate": combined,
            "incremental_cost": p["query_costs"][0] if combined else None,
        }

    if kind == "PINNED_REFERENCE":
        return {"version_mismatch": (
            p["pinned_voter_set_version"] != p["effective_voter_set_version"]
        )}

    if kind == "CONDORCET_PAIR_CYCLE":
        candidates, rankings = p["candidates"], p["rankings"]
        assert all(set(rank) == set(candidates) for rank in rankings)
        winners, edges = [], []
        for a in candidates:
            beats_everyone = True
            for b in candidates:
                if a == b:
                    continue
                preference_count = sum(rank.index(a) < rank.index(b)
                                       for rank in rankings)
                if preference_count > len(rankings) - preference_count:
                    edges.append([a, b])
                else:
                    beats_everyone = False
            if beats_everyone:
                winners.append(a)
        return {"condorcet_winners": winners, "majority_edges": edges}

    if kind == "ALIASED_EXPLANATIONS":
        compatible = [
            h for h in p["hypotheses"]
            if h["matching_trace"] == p["observed_trace"]
        ]
        return {
            "compatible_hypotheses": len(compatible),
            "unique_identification": len(compatible) == 1,
        }

    if kind == "REFERENCE_ONLY":
        return None

    raise ValueError("Unknown fixture kind: " + kind)


class Theme18StageAFixtureChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_manifest_is_bounded_and_explicitly_unvalidated(self):
        m = self.manifest
        self.assertEqual(m["status"], "STAGE_A_PREDICTIONS_NOT_OBSERVED_RESULTS")
        self.assertEqual(len(m["cases"]), 10)
        self.assertEqual({x["id"] for x in m["cases"]},
                         {f"T18-RA-{i:02}" for i in range(1, 11)})
        self.assertTrue(all("expected_interface" in x for x in m["cases"]))

    def test_all_finite_fixture_predictions(self):
        executed = 0
        for fixture in self.manifest["cases"]:
            if fixture["kind"] == "REFERENCE_ONLY":
                self.assertIsNone(fixture["expected_math"])
                continue
            with self.subTest(case=fixture["id"]):
                actual = calculate(fixture)
                self.assertEqual(actual, fixture["expected_math"])
                executed += 1
        self.assertEqual(executed, 8)

    def test_ra_unknown_is_not_compatible(self):
        stale = next(x for x in self.manifest["cases"] if x["id"] == "T18-RA-07")
        self.assertIsNone(calculate(stale)["signal"])

    def test_ra_alert_does_not_invent_safety_fact(self):
        example = next(x for x in self.manifest["cases"] if x["id"] == "T18-RA-01")
        self.assertEqual(calculate(example)["before_choice"], "failover")
        self.assertEqual(calculate(example)["after_choice_given_qualified_evidence"], "stop")
        unqualified = json.loads(json.dumps(example))
        unqualified["input"]["post_safety_evidence_qualified"] = False
        result = calculate(unqualified)
        self.assertEqual(result["ra_signal"], -1)
        self.assertIsNone(result["after_choice_given_qualified_evidence"])

    def test_conditional_query_does_not_rebuy_a(self):
        example = next(x for x in self.manifest["cases"] if x["id"] == "T18-RA-03")
        output = calculate(example)
        self.assertTrue(output["observation_plus_q_adequate"])
        self.assertFalse(output["q_only_adequate"])
        self.assertEqual(output["required_pairs"], [[0, 1], [2, 3]])

    def test_baseline_quota_negative_control(self):
        example = next(x for x in self.manifest["cases"] if x["id"] == "T18-RA-10")
        self.assertTrue(calculate(example)["new_adequate"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
