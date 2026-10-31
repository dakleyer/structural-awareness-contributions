"""G-02: independent audit evidence vs source fixture Boolean; negative tests."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import inspect
import json
import unittest

import campaign
import g02_evidence_audit as g


HERE=Path(__file__).resolve().parent
MANIFEST=json.loads((HERE/"G02_AUDIT_PROTOCOL.json").read_text("utf-8"))
CASES=campaign.read_json("CASE_REGISTRY.json")["cases"]
BY_ID={c["case_id"]:c for c in CASES}
REGIMES={r["id"]:r for r in MANIFEST["regimes"]}


def env(case_id="VERS-FALSE_Q",regime="PERFECT_INDEPENDENT_AUDIT_AND_CONVENTIONAL"):
    row=REGIMES[regime]
    return g.generate(BY_ID[case_id],row["parameters"],
                      seed=MANIFEST["seed"],replicate=0)


class BoundaryAndSignalTests(unittest.TestCase):
    def test_original_source_has_a_flag_not_an_observed_audit_result(self):
        result=g.original_flag_baseline(campaign.read_json("CASE_REGISTRY.json"))
        self.assertEqual(result["cases"],60)
        self.assertEqual(result["source_decisions"],300)
        self.assertEqual(result["legacy_flag_arm_wrong"],4)
        self.assertEqual(result["ordinary_Q_wrong"],12)
        self.assertEqual(result["false_Q_with_declared_boolean"],4)
        self.assertTrue(result["flag_is_not_independent_audit_measurement"])

    def test_current_false_Q_label_sanitized_before_public_planner(self):
        true=env("VERS-VALID_BLOCK")
        false=env("VERS-FALSE_Q")
        self.assertEqual(true["q"]["source_label"],"CURRENT")
        self.assertEqual(false["q"]["source_label"],"CURRENT")
        self.assertNotIn("CURRENT_BUT_FALSE",json.dumps(false["q"]))
        self.assertNotIn("independent_audit",json.dumps(false["q"]))
        self.assertTrue(g.q_can_be_used(false["public"],false["q"]))
        self.assertNotIn("truth",inspect.signature(g.plan_public).parameters)
        self.assertNotIn("case",inspect.signature(g.plan_public).parameters)

    def test_perfect_audit_detects_false_current_Q_without_overriding_rights(self):
        e=env()
        self.assertEqual(e["truth_PRIVATE_FOR_REFEREE_ONLY"],"BLOCK")
        self.assertEqual(e["audit"]["value"],"CONTRADICTION")
        r=g.evaluate(e,REGIMES["PERFECT_INDEPENDENT_AUDIT_AND_CONVENTIONAL"]["prices"])
        self.assertTrue(r["arms"]["Q_UNAUDITED_SOURCE"]["correctness"]=="WRONG")
        self.assertEqual(r["arms"]["Q_WITH_AUDIT_OBSERVATION"]["action"],"REVIEW")
        self.assertTrue(r["arms"]["Q_WITH_AUDIT_OBSERVATION"]["qualified_audit_consumed"])
        self.assertEqual(r["arms"]["CONVENTIONAL_INDEPENDENT_MEASURED"]["action"],"BLOCK")

    def test_fallible_audit_can_miss_false_q_and_make_a_wrong_decision(self):
        e=env(regime="BLIND_AUDIT_FALSE_ASSURANCE")
        self.assertEqual(e["audit"]["value"],"SUPPORT")
        r=g.evaluate(e,REGIMES["BLIND_AUDIT_FALSE_ASSURANCE"]["prices"])
        self.assertEqual(r["arms"]["Q_WITH_AUDIT_OBSERVATION"]["action"],"ALLOW")
        self.assertEqual(r["arms"]["Q_WITH_AUDIT_OBSERVATION"]["correctness"],"WRONG")

    def test_false_positive_audit_causes_loss_of_valid_allow(self):
        e=env("VERS-VALID_GO","AUDIT_FALSE_ALARM_DOMINANT")
        self.assertEqual(e["audit"]["value"],"CONTRADICTION")
        scored=g.evaluate(e,REGIMES["AUDIT_FALSE_ALARM_DOMINANT"]["prices"])
        self.assertEqual(scored["arms"]["Q_WITH_AUDIT_OBSERVATION"]["action"],"REVIEW")
        self.assertEqual(scored["arms"]["Q_UNAUDITED_SOURCE"]["action"],"ALLOW")
        self.assertEqual(scored["arms"]["Q_WITH_AUDIT_OBSERVATION"]["correctness"],"UNRESOLVED")

    def test_source_boolean_mutation_does_not_change_independent_signal(self):
        case=deepcopy(BY_ID["VERS-FALSE_Q"])
        first=g.generate(case,REGIMES["PERFECT_INDEPENDENT_AUDIT_AND_CONVENTIONAL"]["parameters"],
                         seed=MANIFEST["seed"],replicate=4)
        case["Q"]["independent_audit"]=not case["Q"]["independent_audit"]
        second=g.generate(case,REGIMES["PERFECT_INDEPENDENT_AUDIT_AND_CONVENTIONAL"]["parameters"],
                         seed=MANIFEST["seed"],replicate=4)
        self.assertEqual(first["audit"],second["audit"])
        self.assertEqual(first["direct"],second["direct"])
        self.assertEqual(first["q"],second["q"])
        self.assertNotEqual(first["legacy_audit_flag_DIAGNOSTIC_ONLY"],
                            second["legacy_audit_flag_DIAGNOSTIC_ONLY"])
        prices=REGIMES["PERFECT_INDEPENDENT_AUDIT_AND_CONVENTIONAL"]["prices"]
        for arm in g.ARMS:
            self.assertEqual(
                g.plan_public(first["public"],first["q"],first["audit"],
                              first["direct"],prices,arm),
                g.plan_public(second["public"],second["q"],second["audit"],
                              second["direct"],prices,arm)
            )

    def test_same_public_and_same_evidence_different_truth_same_plan(self):
        case=env("VERS-VALID_GO")
        changed=deepcopy(case)
        changed["truth_PRIVATE_FOR_REFEREE_ONLY"]="BLOCK"
        prices=REGIMES["PERFECT_INDEPENDENT_AUDIT_AND_CONVENTIONAL"]["prices"]
        one=g.evaluate(case,prices)
        two=g.evaluate(changed,prices)
        for arm in g.ARMS:
            self.assertEqual(one["arms"][arm]["action"],two["arms"][arm]["action"])
        self.assertNotEqual(one["arms"]["Q_WITH_AUDIT_OBSERVATION"]["correctness"],
                            two["arms"]["Q_WITH_AUDIT_OBSERVATION"]["correctness"])

    def test_wrong_issuer_scope_or_freshness_fails_independent_qualification(self):
        base=env("VERS-VALID_GO")
        prices=REGIMES["PERFECT_INDEPENDENT_AUDIT_AND_CONVENTIONAL"]["prices"]
        for name,mutation in (
            ("same_issuer",{"issuer_id":base["q"]["issuer_id"]}),
            ("wrong_scope",{"scope_id":"OTHER_QUESTION"}),
            ("stale",{"observed_at":0}),
            ("unsigned",{"signed_TOY":False}),
            ("not_available",{"available":False}),
        ):
            with self.subTest(name=name):
                evidence={**base["audit"],**mutation}
                out=g.plan_public(base["public"],base["q"],evidence,base["direct"],
                                  prices,"Q_WITH_AUDIT_OBSERVATION")
                self.assertEqual(out["action"],"REVIEW")
                self.assertFalse(out["qualified_audit_consumed"])
                self.assertEqual(out["acquisition_cost_synthetic"],1.3)
        self.assertFalse(g.qualified(
            {**base["audit"],"issuer_id":base["q"]["issuer_id"]},
            base["q"],base["public"],"AUDITOR"
        ))

    def test_missing_audit_cannot_turn_into_a_perfect_detector(self):
        e=env(regime="AUDIT_UNAVAILABLE_DIRECT_AVAILABLE")
        prices=REGIMES["AUDIT_UNAVAILABLE_DIRECT_AVAILABLE"]["prices"]
        scored=g.evaluate(e,prices)
        self.assertEqual(scored["arms"]["Q_WITH_AUDIT_OBSERVATION"]["action"],"REVIEW")
        self.assertEqual(scored["arms"]["Q_WITH_AUDIT_OBSERVATION"]["correctness"],"UNRESOLVED")
        self.assertFalse(scored["arms"]["Q_WITH_AUDIT_OBSERVATION"]["qualified_audit_consumed"])
        self.assertEqual(scored["arms"]["Q_WITH_AUDIT_OBSERVATION"]["acquisition_cost_synthetic"],1.3)

    def test_stale_q_and_open_cd_never_become_current_valid_audit_evidence(self):
        for sid in ("VERS-STALE","VERS-OPEN_RESIDUAL"):
            with self.subTest(sid=sid):
                e=env(sid)
                p=REGIMES["PERFECT_INDEPENDENT_AUDIT_AND_CONVENTIONAL"]["prices"]
                scored=g.evaluate(e,p)
                self.assertEqual(e["audit"]["value"],"INCONCLUSIVE")
                self.assertFalse(scored["arms"]["Q_WITH_AUDIT_OBSERVATION"]["qualified_audit_consumed"])
                self.assertEqual(scored["arms"]["Q_WITH_AUDIT_OBSERVATION"]["action"],"REVIEW")
                self.assertNotIn("INDEPENDENT_AUDIT",scored["arms"]["Q_WITH_AUDIT_OBSERVATION"]["consulted"])
                if sid.endswith("OPEN_RESIDUAL"):
                    self.assertEqual(e["direct"]["value"],"INCONCLUSIVE")
                    self.assertIsNone(scored["arms"]["CONVENTIONAL_INDEPENDENT_MEASURED"]["net_value_synthetic"])
                else:
                    self.assertEqual(e["direct"]["value"],"BLOCK")

    def test_qualified_conventional_instrument_not_perfect_oracle(self):
        case=BY_ID["VERS-VALID_BLOCK"]
        params=dict(REGIMES["PERFECT_INDEPENDENT_AUDIT_AND_CONVENTIONAL"]["parameters"])
        p=REGIMES["PERFECT_INDEPENDENT_AUDIT_AND_CONVENTIONAL"]["prices"]
        params["direct_observation_correct"]="0"
        bad=g.evaluate(g.generate(case,params,seed=MANIFEST["seed"],replicate=0),p)
        self.assertEqual(bad["arms"]["CONVENTIONAL_INDEPENDENT_MEASURED"]["action"],"ALLOW")
        self.assertEqual(bad["arms"]["CONVENTIONAL_INDEPENDENT_MEASURED"]["correctness"],"WRONG")
        params["direct_observation_correct"]="1"
        good=g.evaluate(g.generate(case,params,seed=MANIFEST["seed"],replicate=0),p)
        self.assertEqual(good["arms"]["CONVENTIONAL_INDEPENDENT_MEASURED"]["action"],"BLOCK")
        self.assertEqual(good["arms"]["CONVENTIONAL_INDEPENDENT_MEASURED"]["correctness"],"CORRECT")

    def test_price_changes_cost_not_action_or_accuracy(self):
        scenario=env("VERS-VALID_GO","RELIABLE_AUDIT_NOISY_CONVENTIONAL")
        a=REGIMES["RELIABLE_AUDIT_NOISY_CONVENTIONAL"]["prices"]
        b=REGIMES["RELIABLE_AUDIT_BUT_EXPENSIVE"]["prices"]
        first=g.evaluate(scenario,a)
        second=g.evaluate(scenario,b)
        for arm in g.ARMS:
            self.assertEqual(first["arms"][arm]["action"],second["arms"][arm]["action"])
            self.assertEqual(first["arms"][arm]["correctness"],
                             second["arms"][arm]["correctness"])
        self.assertNotEqual(first["arms"]["Q_WITH_AUDIT_OBSERVATION"]["acquisition_cost_synthetic"],
                            second["arms"]["Q_WITH_AUDIT_OBSERVATION"]["acquisition_cost_synthetic"])


class FiniteCampaignRegressions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=g.run(MANIFEST)
        cls.by={x["regime"]:x for x in cls.report["regimes"]}

    def test_manifest_and_full_source_population_are_frozen_and_reusable(self):
        g.validate(MANIFEST)
        self.assertEqual(self.report["original_source_cases"],60)
        self.assertEqual(self.report["replicates_per_case"],64)
        self.assertEqual(self.report["total_paired_cases"],60*64*len(MANIFEST["regimes"]))
        self.assertEqual(len(self.report["source_sha256"]),3)
        self.assertTrue(all(len(v)==64 for v in self.report["source_sha256"].values()))
        self.assertEqual(self.report["historical_flag_baseline_UNCHANGED"]["legacy_flag_arm_wrong"],4)
        self.assertEqual(self.report["historical_flag_baseline_UNCHANGED"]["ordinary_Q_wrong"],12)
        self.assertTrue(all(sum(x["source_variant_counts"].values())==60*64
                            for x in self.report["regimes"]))
        self.assertTrue(all(set(x["new_policy_outcomes"])==set(g.ARMS)
                            for x in self.report["regimes"]))

    def test_perfect_audit_has_no_false_q_wrong_decisions_where_boolean_did(self):
        group=self.by["PERFECT_INDEPENDENT_AUDIT_AND_CONVENTIONAL"]["new_policy_outcomes"]
        self.assertEqual(group["Q_UNAUDITED_SOURCE"]["wrong"],12*64)
        self.assertEqual(group["Q_WITH_AUDIT_OBSERVATION"]["wrong"],0)
        self.assertEqual(group["CONVENTIONAL_INDEPENDENT_MEASURED"]["wrong"],0)
        self.assertEqual(group["CONVENTIONAL_INDEPENDENT_MEASURED"]["correct"],48*64)
        self.assertGreater(group["Q_WITH_AUDIT_OBSERVATION"]["unresolved"],0)

    def test_fallible_audit_yields_wrong_decisions_with_zero_detection(self):
        group=self.by["BLIND_AUDIT_FALSE_ASSURANCE"]["new_policy_outcomes"]
        self.assertEqual(group["Q_WITH_AUDIT_OBSERVATION"]["wrong"],12*64)
        self.assertGreater(group["CONVENTIONAL_INDEPENDENT_MEASURED"]["correct"],0)
        self.assertGreater(g.rat(group["Q_WITH_AUDIT_OBSERVATION"]["total_synthetic_instrument_cost"],"cost"),0)

    def test_when_audit_absent_zero_wrong_must_not_be_called_superior(self):
        group=self.by["AUDIT_UNAVAILABLE_DIRECT_AVAILABLE"]["new_policy_outcomes"]
        audited=group["Q_WITH_AUDIT_OBSERVATION"]
        targeted=group["CONVENTIONAL_INDEPENDENT_MEASURED"]
        self.assertEqual(audited["wrong"],0)
        self.assertEqual(audited["correct"],0)
        self.assertEqual(audited["unresolved"],48*64)
        self.assertGreater(audited["missed_justified_allows"],
                           targeted["missed_justified_allows"])

    def test_realistic_regimes_allow_conventional_to_outperform_weak_audit(self):
        group=self.by["WEAK_AUDIT_STRONG_CONVENTIONAL"]["new_policy_outcomes"]
        self.assertGreater(group["Q_WITH_AUDIT_OBSERVATION"]["wrong"],
                           group["CONVENTIONAL_INDEPENDENT_MEASURED"]["wrong"])
        self.assertLess(group["CONVENTIONAL_INDEPENDENT_MEASURED"]["missed_justified_allows"],
                        group["Q_WITH_AUDIT_OBSERVATION"]["missed_justified_allows"])

    def test_false_alarm_detects_non_superiority_of_auditor(self):
        group=self.by["AUDIT_FALSE_ALARM_DOMINANT"]["new_policy_outcomes"]
        self.assertEqual(group["Q_WITH_AUDIT_OBSERVATION"]["wrong"],0)
        self.assertGreater(group["Q_WITH_AUDIT_OBSERVATION"]["missed_justified_allows"],0)
        self.assertEqual(group["Q_WITH_AUDIT_OBSERVATION"]["unresolved"],48*64)

    def test_same_parameters_with_more_cost_leave_counts_unchanged(self):
        l=self.by["RELIABLE_AUDIT_NOISY_CONVENTIONAL"]["new_policy_outcomes"]
        h=self.by["RELIABLE_AUDIT_BUT_EXPENSIVE"]["new_policy_outcomes"]
        for arm in g.ARMS:
            for k in ("correct","wrong","unresolved","false_allow","false_block",
                      "missed_justified_allows"):
                self.assertEqual(l[arm][k],h[arm][k])
        self.assertNotEqual(l["Q_WITH_AUDIT_OBSERVATION"]["total_synthetic_instrument_cost"],
                            h["Q_WITH_AUDIT_OBSERVATION"]["total_synthetic_instrument_cost"])

    def test_open_c_d_never_scored_as_closed_in_any_regime(self):
        for row in self.report["regimes"]:
            for a in row["new_policy_outcomes"].values():
                self.assertEqual(a["open_unscored_count"],12*64)
                self.assertEqual(a["adjudicable_count"],48*64)

    def test_deterministic_reports_equal_under_replay(self):
        reduced=deepcopy(MANIFEST)
        reduced["replicates_per_case"]=8
        self.assertEqual(g.run(reduced),g.run(reduced))

    def test_fail_closed_on_invalid_manifest_and_unknown_source_variant(self):
        p=deepcopy(MANIFEST)
        p["regimes"][0]["parameters"]["audit_detects_false_claim"]="11/10"
        with self.assertRaises(ValueError):
            g.validate(p)
        p=deepcopy(MANIFEST)
        p["regimes"][0]["prices"]["independent_audit"]="-1"
        with self.assertRaises(ValueError):
            g.validate(p)
        p=deepcopy(MANIFEST)
        p["regimes"][0]["parameters"]["direct_observation_correct"]=True
        with self.assertRaises(ValueError):
            g.validate(p)
        p=deepcopy(MANIFEST)
        p["replicates_per_case"]=10000
        with self.assertRaises(ValueError):
            g.validate(p)
        p=deepcopy(BY_ID["VERS-VALID_GO"])
        p["truth_private_for_scoring"]="INVENTED_TRUTH"
        with self.assertRaises(ValueError):
            g.generate(p,REGIMES["PERFECT_INDEPENDENT_AUDIT_AND_CONVENTIONAL"]["parameters"],
                       seed=MANIFEST["seed"],replicate=0)


if __name__ == "__main__":
    unittest.main()
