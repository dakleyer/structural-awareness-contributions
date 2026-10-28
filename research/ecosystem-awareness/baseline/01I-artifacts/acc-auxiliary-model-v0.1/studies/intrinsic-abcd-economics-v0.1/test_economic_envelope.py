"""Adversarial, source-executed controls of the reusable economic envelope."""
from __future__ import annotations

from copy import deepcopy
from dataclasses import replace
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path
import sys
import unittest

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from economic_envelope import (
    ArmObservation, ComparisonFrame, CostLedger, affine_cost_crossing,
    compare_case, quantity, run_cases, summary,
)
from economic_envelope_adapters import (
    agentic_cost_override, agentic_observations, intrinsic_cost_override,
    intrinsic_observations,
)
from economic_envelope_runner import execute, _bits_for_pattern


def source(name, path):
    spec = spec_from_file_location(name, path)
    module = module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


SOCIAL = source("_social_envelope_test_source", HERE / "intrinsic_abcd.py")
AGENTIC_DIR = HERE.parent / "agentic-ecosystem-reduction-v0.1"
AGENTIC = source("_agentic_envelope_test_source", AGENTIC_DIR / "agentic_reduction.py")
CASES = json.loads((AGENTIC_DIR / "CASES.json").read_text("utf-8"))["cases"]
BY_ID = {row["id"]: row for row in CASES}
ROOT = HERE.parents[5]  # replaced by explicit repository-root search in tests below


def frame(case_id="case-one"):
    return ComparisonFrame(case_id, "EXTERNAL_MODEL", "scope-v1", "question-A",
                           "observed_metric", "units", "credits", "one-step",
                           "public-contract-sha", 12)


def obs(arm, gross, ledger=None, f=None, evidence="POST_HOC_SYNTHETIC_REFEREE"):
    return ArmObservation(f or frame(), arm, gross, ledger or CostLedger(),
                          "SOURCE_REPORTED", "producer/result", evidence)


class ExactKernelAndThirdPartyInterface(unittest.TestCase):
    def test_exact_decimal_and_fraction_prices(self):
        self.assertEqual(quantity("0.1") + quantity("0.2"), Fraction(3, 10))
        self.assertEqual(quantity(Fraction(1, 3)), Fraction(1, 3))
        self.assertEqual(quantity(0.1), Fraction(1, 10))
        self.assertEqual(quantity("1/7"), Fraction(1, 7))

    def test_refuse_boolean_nonfinite_invalid_numeric(self):
        for value in (True, False, float("nan"), float("inf"),
                      float("-inf"), "nan", "", object(), None):
            with self.subTest(value=value), self.assertRaises(ValueError):
                quantity(value)

    def test_cost_ledger_rejects_negative_and_duplicates(self):
        for bad in ({"x": -1}, {"x": float("nan")}, {"x": True}):
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                CostLedger.of(bad)
        with self.assertRaises(ValueError):
            CostLedger((("same", 1), ("same", 2)))
        self.assertEqual(CostLedger.of({"maintenance": "0.25", "transfer": ".5"}).total,
                         Fraction(3, 4))

    def test_native_cost_and_net_reconciliation(self):
        with self.assertRaisesRegex(ValueError, "cost ledger"):
            ArmObservation(frame(), "B", 10, CostLedger.of({"source": 1}),
                           "YES", "native", "POST_HOC_SYNTHETIC_REFEREE",
                           source_cost=2)
        with self.assertRaisesRegex(ValueError, "net calculation"):
            ArmObservation(frame(), "B", 10, CostLedger.of({"source": 1}),
                           "YES", "native", "POST_HOC_SYNTHETIC_REFEREE",
                           source_net=10)
        ok = ArmObservation(frame(), "B", "10.00004",
                            CostLedger.of({"source": 1}), "YES", "native",
                            "POST_HOC_SYNTHETIC_REFEREE", source_net=9,
                            rounding_tolerance="0.0001")
        self.assertEqual(ok.net, Fraction("9.00004"))

    def test_different_question_scope_horizon_metric_public_a_rejected(self):
        a = obs("A_ONLY", 0)
        original = frame()
        variations = (
            replace(original, question="question-B"),
            replace(original, scope="other-scope"),
            replace(original, horizon="later"),
            replace(original, metric="other metric"),
            replace(original, cost_unit="different credits"),
            replace(original, public_contract_id="other contract"),
            replace(original, baseline_a=13),
        )
        for other in variations:
            with self.subTest(other=other), self.assertRaisesRegex(ValueError, "incommensurable"):
                compare_case((a, obs("B", 2, f=other)))

    def test_mixed_evidence_rejected(self):
        with self.assertRaisesRegex(ValueError, "evidence of different kinds"):
            compare_case((obs("A_ONLY", 0), obs("B", 3, evidence="UNQUALIFIED_PROPOSAL")))

    def test_unknown_is_not_zero_and_ranking_remains_partial(self):
        result = compare_case((obs("A_ONLY", 0), obs("B", None)))
        self.assertEqual(result.status, "PARTIAL_RANKING")
        self.assertEqual(result.leaders, ("A_ONLY",))
        self.assertIsNone(result.as_dict()["arms"][1]["net"])

    def test_all_leaders_retained_on_exact_ties(self):
        case = compare_case((obs("A_ONLY", 0), obs("B", 2, CostLedger.of({"x": 2})),
                             obs("DIRECTED", 0)))
        self.assertEqual(case.leaders, ("A_ONLY", "B", "DIRECTED"))
        self.assertEqual(case.as_dict()["arms"][1]["net_delta_vs_baseline"], "0")

    def test_duplicate_arm_missing_baseline_and_unscored_baseline(self):
        with self.assertRaisesRegex(ValueError, "duplicate arm"):
            compare_case((obs("A_ONLY", 0), obs("A_ONLY", 2)))
        with self.assertRaisesRegex(ValueError, "missing baseline"):
            compare_case((obs("B", 0), obs("DIRECTED", 2)))
        with self.assertRaisesRegex(ValueError, "unscored baseline"):
            compare_case((obs("A_ONLY", None), obs("B", 2)))

    def test_no_universal_superiority_or_compulsory_action(self):
        bad = compare_case((obs("A_ONLY", 0),
                            obs("B", 0, CostLedger.of({"issuer": 3})),
                            obs("DIRECTED", 2, CostLedger.of({"observ": 1}))))
        self.assertEqual(bad.leaders, ("DIRECTED",))
        self.assertEqual(bad.as_dict()["arms"][1]["net"], "-3")

    def test_external_model_adapter_and_batch_summary(self):
        inputs = [("a", 0), ("b", 1)]
        def external_adapter(s):
            ident, diff = s
            f = frame(ident)
            return (obs("A_ONLY", 0, f=f), obs("LOCAL_B", diff, f=f))
        cases = run_cases(inputs, external_adapter)
        self.assertEqual(len(cases), 2)
        self.assertEqual(cases[0].leaders, ("A_ONLY", "LOCAL_B"))
        self.assertEqual(cases[1].leaders, ("LOCAL_B",))
        counts = summary(cases)
        self.assertEqual(counts["groups"]["EXTERNAL_MODEL"]["cases"], 2)
        self.assertEqual(counts["aggregation_rule"], "COUNTS_ONLY_NO_CROSS_OBJECTIVE_UTILITY_SUM")
        with self.assertRaisesRegex(ValueError, "duplicate"):
            run_cases(inputs + [inputs[0]], external_adapter)

    def test_price_crossing_exact_and_bidirectional(self):
        cross = affine_cost_crossing(b_fixed="0.75", b_per_path=".25",
                                     peer_fixed=3, peer_per_path=0)
        self.assertEqual(cross.crossing_path_length, 9)
        self.assertEqual([cross.at_path_length(n) for n in (6, 8, 9, 10)],
                         ["B", "B", "TIE", "DIRECTED"])
        reverse = affine_cost_crossing(b_fixed=2, b_per_path=".1",
                                       peer_fixed=0, peer_per_path=".4")
        self.assertEqual(reverse.at_path_length(1), "DIRECTED")
        self.assertEqual(reverse.at_path_length(10), "B")

    def test_equal_slopes_no_crossing_and_bad_schedule(self):
        eq = affine_cost_crossing(b_fixed=1, b_per_path=".25",
                                  peer_fixed=1, peer_per_path=".25")
        self.assertEqual(eq.classification, "EVERYWHERE_TIE")
        no = affine_cost_crossing(b_fixed=3, b_per_path=".25",
                                  peer_fixed=1, peer_per_path=".25")
        self.assertEqual(no.classification, "NO_CROSSING")
        outside = affine_cost_crossing(b_fixed=1, b_per_path=2,
                                       peer_fixed=3, peer_per_path=3)
        self.assertEqual(outside.classification, "CROSSING_OUTSIDE_DOMAIN")
        for bad in ({"b_fixed": -1}, {"peer_per_path": float("nan")},
                    {"b_per_path": True}):
            params = {"b_fixed": 1, "b_per_path": 1, "peer_fixed": 2, "peer_per_path": 0}
            params.update(bad)
            with self.assertRaises(ValueError):
                affine_cost_crossing(**params)


def native_world(n, slack=None, inaccessible=False):
    idx = n // 4
    bits = tuple(int(i == idx) for i in range(n))
    return SOCIAL.balanced_tree(
        bits, cap_root=None if slack is None else 8*n+slack,
        inaccessible_path_leaf=idx if inaccessible else None,
    ), "source-" + str(idx)


class SocialOriginalPolicyTests(unittest.TestCase):
    def test_K01_inversion_is_from_actual_source_policy(self):
        winners = {}
        for n in (16, 64, 128, 256):
            world, target = native_world(n)
            case = compare_case(intrinsic_observations(
                SOCIAL, world, target, SOCIAL.Costs(), scenario_id="n" + str(n)))
            arms = {a.arm: a for a in case.arms}
            self.assertEqual(case.frame.baseline_a, 8*n)
            self.assertEqual(arms["B_QUALIFIED"].gross_value, 10)
            self.assertEqual(arms["TARGETED_EXPLORATION_OF_A"].gross_value, 10)
            winners[n] = (arms["B_QUALIFIED"].net, arms["TARGETED_EXPLORATION_OF_A"].net)
        self.assertEqual(winners[16], (Fraction("7.75"), Fraction(7)))
        self.assertEqual(winners[64], (Fraction("7.25"), Fraction(7)))
        self.assertEqual(winners[128], (Fraction(7), Fraction(7)))
        self.assertEqual(winners[256], (Fraction("6.75"), Fraction(7)))

    def test_source_public_receiver_changes_decision_with_price(self):
        world, target = native_world(16)
        cheap = compare_case(intrinsic_observations(
            SOCIAL, world, target, SOCIAL.Costs(), scenario_id="cheap"))
        costly = intrinsic_cost_override(SOCIAL, {"b_issuance_per_path_node": 10})
        dear = compare_case(intrinsic_observations(
            SOCIAL, world, target, costly, scenario_id="expensive"))
        self.assertGreater(next(a.net for a in cheap.arms if a.arm == "SOURCE_PUBLIC_RECEIVER"), 0)
        self.assertEqual(next(a.net for a in dear.arms if a.arm == "SOURCE_PUBLIC_RECEIVER"), 0)

    def test_saturated_world_makes_staying_optimal(self):
        world, target = native_world(16, slack=0)
        case = compare_case(intrinsic_observations(
            SOCIAL, world, target, SOCIAL.Costs(), scenario_id="saturated"))
        self.assertIn("A_ONLY", case.leaders)
        self.assertIn("SOURCE_PUBLIC_RECEIVER", case.leaders)
        self.assertLess(next(a.net for a in case.arms if a.arm == "B_QUALIFIED"), 0)

    def test_missing_source_access_is_not_invented(self):
        world, target = native_world(16, inaccessible=True)
        case = compare_case(intrinsic_observations(
            SOCIAL, world, target, SOCIAL.Costs(), scenario_id="no-access"))
        statuses = {a.arm: a.source_status for a in case.arms}
        self.assertEqual(statuses["B_QUALIFIED"], "NO_QUALIFICATION")
        self.assertEqual(statuses["TARGETED_EXPLORATION_OF_A"], "TARGETED_NO_EFFECTIVE_ROUTE")
        self.assertEqual(statuses["FULL_EXPAND_A"], "FULL_SCOPE_NOT_ACCESSIBLE")
        self.assertEqual(next(a.net for a in case.arms if a.arm == "A_ONLY"), 0)

    def test_stale_certificate_cost_charged_but_not_accepted(self):
        world, target = native_world(16)
        case = compare_case(intrinsic_observations(
            SOCIAL, world, target, SOCIAL.Costs(), scenario_id="stale",
            issued_at=5, now=20, ttl=10))
        statuses = {a.arm: a.source_status for a in case.arms}
        self.assertEqual(statuses["B_QUALIFIED"], "STALE")
        self.assertEqual(statuses["SOURCE_PUBLIC_RECEIVER"], "STALE")
        b = next(a for a in case.arms if a.arm == "B_QUALIFIED")
        self.assertLess(b.net, 0)
        self.assertEqual(b.costs.total, Fraction("2.25"))

    def test_cost_override_does_not_modify_source_default_or_world(self):
        default = SOCIAL.Costs()
        custom = intrinsic_cost_override(SOCIAL, {"target_observation": "0.10"})
        self.assertEqual(custom.target_observation, 0.1)
        self.assertEqual(default.target_observation, 3.0)
        with self.assertRaises(ValueError):
            intrinsic_cost_override(SOCIAL, {"new_theory_parameter": 0})
        with self.assertRaises(ValueError):
            intrinsic_cost_override(SOCIAL, {"target_observation": -1})

    def test_single_B_question_not_joint_certificate(self):
        world, target = native_world(16, slack=1)
        c = SOCIAL.upstream_B(world, target, now=0, ttl=10)
        self.assertEqual(c.target, target)
        valid, reason = SOCIAL.receiver_B_valid(
            SOCIAL.public_outline(world), c, (target, "source-1"), now=1)
        self.assertFalse(valid)
        self.assertEqual(reason, "WRONG_QUESTION")

    def test_original_reference_calculation_is_unchanged(self):
        report = SOCIAL.sample_report()
        self.assertEqual(report["current_A"], 128)
        self.assertEqual(report["baseline_world_private_selected_gain"], 2)
        self.assertEqual(report["policies"][1]["net_realized_value_SYNTHETIC"], 7.75)


class AgenticOriginalPolicyTests(unittest.TestCase):
    def test_all_original_30_cases_six_arms_are_reconciled(self):
        self.assertEqual(len(CASES), 30)
        for case in CASES:
            with self.subTest(case=case["id"]):
                compared = compare_case(agentic_observations(AGENTIC, case))
                self.assertEqual(len(compared.arms), 6)
                self.assertEqual(compared.status, "COMPLETE_RANKING")
                self.assertEqual(compared.frame.baseline_a,
                                 quantity(AGENTIC.declared_public(case)["current_A_total_output"]))
                self.assertTrue(all(a.costs.total >= 0 for a in compared.arms))

    def test_same_Q_peer_decision_and_cost_reconciled(self):
        compared = compare_case(agentic_observations(
            AGENTIC, BY_ID["AG01-QUALIFIED-NEAR-OPTIMUM"]))
        arms = {a.arm: a for a in compared.arms}
        self.assertEqual(arms["Q_META_PROTOCOL"].gross_value, Fraction("11.5"))
        self.assertEqual(arms["CONVENTIONAL_EQUIVALENT_Q"].gross_value, Fraction("11.5"))
        self.assertEqual(arms["Q_META_PROTOCOL"].net, arms["CONVENTIONAL_EQUIVALENT_Q"].net)
        self.assertEqual(arms["Q_META_PROTOCOL"].net, Fraction("11.2"))

    def test_physical_coordination_overhead_not_charged_twice(self):
        raw = AGENTIC.run_case(BY_ID["AG01-QUALIFIED-NEAR-OPTIMUM"])
        source_result = raw["arms"]["Q_META_PROTOCOL"]
        self.assertGreater(source_result["observed_by_referee_only"]["coordination_resources_spent"], 0)
        compared = compare_case(agentic_observations(
            AGENTIC, BY_ID["AG01-QUALIFIED-NEAR-OPTIMUM"]))
        q = next(a for a in compared.arms if a.arm == "Q_META_PROTOCOL")
        self.assertEqual(q.costs.total, quantity(source_result["plan"]["instrument_cost"]))
        self.assertEqual(q.net, quantity(source_result["mission_net_value_after_information_cost"]))

    def test_cost_sweep_never_changes_mission_resources_or_private_truth(self):
        source_case = BY_ID["AG01-QUALIFIED-NEAR-OPTIMUM"]
        original = deepcopy(source_case)
        changed = agentic_cost_override(source_case, {
            "Q.cost": 4, "directed.cost": ".1", "directed.equivalent_Q_cost": 4,
        })
        self.assertEqual(source_case, original)
        self.assertEqual(changed["public"], original["public"])
        self.assertEqual(changed["truth_private"], original["truth_private"])
        self.assertEqual(changed["Q"]["lower_rate"], original["Q"]["lower_rate"])
        self.assertNotEqual(changed["Q"]["cost"], original["Q"]["cost"])
        compare_case(agentic_observations(AGENTIC, changed))
        for bad in ({"truth_private.recipient_incremental_rate": 9},
                    {"Q.cost": float("inf")}, {"directed.cost": -1}):
            with self.assertRaises(ValueError):
                agentic_cost_override(source_case, bad)

    def test_absent_Q_is_not_synthesized_by_cost_adapter(self):
        no_q = BY_ID["AG03-A-ONLY-Q-ABSENT"]
        self.assertIsNone(no_q.get("Q"))
        with self.assertRaises(ValueError):
            agentic_cost_override(no_q, {"Q.cost": 1})
        self.assertEqual(agentic_cost_override(no_q, {})["Q"], None)

    def test_agentic_negative_controls_keep_A_only_in_some_cases(self):
        for name in ("AG02-LOW-CAPABILITY-SAME-A",
                     "AG07-DONOR-REFUSES",
                     "AG09-MATERIAL-D-UNRESOLVED"):
            with self.subTest(name=name):
                case = compare_case(agentic_observations(AGENTIC, BY_ID[name]))
                baseline = next(a for a in case.arms if a.arm == "A_ONLY")
                self.assertEqual(baseline.costs.total, 0)
                self.assertIn("A_ONLY", case.leaders)


class ManifestAndRunCoverage(unittest.TestCase):
    def test_manifest_exercises_both_original_models_and_all_regimes(self):
        corpus_root = next(p for p in HERE.parents if (p / ".github/workflows/document-integrity.yml").exists())
        manifest = json.loads((HERE / "ECONOMIC_SWEEP_MANIFEST.json").read_text("utf-8"))
        both = execute(manifest, corpus_root)
        self.assertEqual(both["schema"], manifest["schema"])
        self.assertEqual(both["summary"]["groups"]["ACC_SOCIAL_INTRINSIC_44"]["cases"],
                         7 * 3 * 2 * 4)
        self.assertGreaterEqual(both["summary"]["groups"]["ACC_AGENTIC_REDUCTION_57"]["cases"], 90)
        self.assertEqual(both["social_break_even"]["path_nodes"], "9")
        self.assertEqual(len(both["source_sha256"]), 3)
        self.assertEqual(both["cross_question_composition"], "NOT_PERFORMED")
        only_agentic = execute(manifest, corpus_root, model="agentic")
        self.assertNotIn("ACC_SOCIAL_INTRINSIC_44", only_agentic["summary"]["groups"])
        only_social = execute(manifest, corpus_root, model="social")
        self.assertNotIn("ACC_AGENTIC_REDUCTION_57", only_social["summary"]["groups"])

    def test_manifest_schema_and_unrecognized_access_rejected(self):
        corpus_root = next(p for p in HERE.parents if (p / ".github/workflows/document-integrity.yml").exists())
        manifest = json.loads((HERE / "ECONOMIC_SWEEP_MANIFEST.json").read_text("utf-8"))
        malformed = deepcopy(manifest)
        malformed["schema"] = "some-other-exercise"
        with self.assertRaises(ValueError):
            execute(malformed, corpus_root, model="social")
        malformed = deepcopy(manifest)
        malformed["social"]["accesses"] = ["bypass-rights"]
        with self.assertRaises(ValueError):
            execute(malformed, corpus_root, model="social")


    def test_capacity_patterns_do_not_create_new_source_physics(self):
        self.assertEqual(_bits_for_pattern(8, 2, {"mode": "selected"}), (0, 0, 1, 0, 0, 0, 0, 0))
        self.assertEqual(_bits_for_pattern(8, 2, {"mode": "all"}), (1,) * 8)
        self.assertEqual(_bits_for_pattern(8, 2, {"mode": "none"}), (0,) * 8)
        self.assertEqual(_bits_for_pattern(8, 2, {"mode": "indices", "indices": [1, 7]}),
                         (0, 1, 0, 0, 0, 0, 0, 1))
        for bad in ({"mode": "indices", "indices": [1, 1]},
                    {"mode": "indices", "indices": [8]},
                    {"mode": "new-theory"}):
            with self.assertRaises(ValueError):
                _bits_for_pattern(8, 2, bad)

    def test_custom_matrix_exercises_material_capacity_and_budget(self):
        corpus_root = next(p for p in HERE.parents if (p / ".github/workflows/document-integrity.yml").exists())
        manifest = json.loads((HERE / "ECONOMIC_SWEEP_MANIFEST.json").read_text("utf-8"))
        manifest["social"]["sizes"] = [16]
        manifest["social"]["roots"] = [{"id": "free", "slack": None}]
        manifest["social"]["accesses"] = ["full"]
        manifest["social"]["capacity_patterns"] = [
            {"id": "none", "mode": "none"},
            {"id": "all", "mode": "all"},
        ]
        manifest["social"]["prices"] = [
            {"id": "low-budget", "costs": {}, "planner_budget": "0"},
        ]
        results = execute(manifest, corpus_root, model="social", details=True)
        self.assertEqual(results["summary"]["groups"]["ACC_SOCIAL_INTRINSIC_44"]["cases"], 2)
        rows = {r["frame"]["case_id"]: r for r in results["cases"]}
        none, all_cap = next(r for k, r in rows.items() if "/none/" in k), next(
            r for k, r in rows.items() if "/all/" in k)
        none_b = next(a for a in none["arms"] if a["arm"] == "B_QUALIFIED")
        all_b = next(a for a in all_cap["arms"] if a["arm"] == "B_QUALIFIED")
        self.assertEqual(none_b["gross"], "0")
        self.assertEqual(all_b["gross"], "10")
        self.assertEqual(none["frame"]["baseline_a"], all_cap["frame"]["baseline_a"])
        self.assertEqual(next(a["status"] for a in all_cap["arms"]
                              if a["arm"] == "SOURCE_PUBLIC_RECEIVER"),
                         "B_INFO_BEYOND_BUDGET")

if __name__ == "__main__":
    unittest.main()
