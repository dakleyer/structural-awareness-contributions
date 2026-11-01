"""L-09 tests: fixture leakage must vanish in true/false public-matched pairs."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
import json
import unittest

import campaign
import g02_evidence_audit as g02
import l09_public_leakage as lab


HERE=Path(__file__).resolve().parent
MANIFEST=json.loads((HERE/"L09_MATCHING_PROTOCOL.json").read_text(encoding="utf-8"))
ORIGINAL=campaign.read_json("CASE_REGISTRY.json")
G02_SOURCE=campaign.read_json("G02_AUDIT_PROTOCOL.json")
SOURCE_REGIMES={x["id"]:x for x in G02_SOURCE["regimes"]}


def one_pair(family="VERS",base="REVIEW"):
    names=lab.make_public_matched_pairs(ORIGINAL["cases"])
    return next(x for x in names if x["source_family"]==family
                and x["pair_id"].endswith("-"+base))


def environments(pair,regime="PERFECT_INDEPENDENT_AUDIT_AND_CONVENTIONAL",rep=0):
    params=SOURCE_REGIMES[regime]["parameters"]
    return [g02.generate(x,params,seed=MANIFEST["seed"],replicate=rep)
            for x in pair["worlds"]]


class SourceFixtureAndContractTests(unittest.TestCase):
    def test_original_view_has_real_metadata_label_leak(self):
        report=lab.original_fixture_metadata_diagnostic(ORIGINAL["cases"])
        self.assertEqual(report["finite_observations"],24)
        self.assertEqual(report["truth_counts"],{"ALLOW":12,"BLOCK":12})
        self.assertEqual(report["optimal_public_only_correct"],18)
        self.assertEqual(report["optimal_public_only_accuracy"],"3/4")
        self.assertAlmostEqual(report["visible_mutual_information_bits"],0.5,places=12)
        self.assertAlmostEqual(report["conditional_truth_entropy_bits"],0.5,places=12)
        self.assertTrue(report["not_a_distribution_over_open_C_D"])

    def test_all_original_sources_used_without_mutating_the_frozen_rows(self):
        before=json.dumps(ORIGINAL,sort_keys=True)
        pairs=lab.make_public_matched_pairs(ORIGINAL["cases"])
        self.assertEqual(len(ORIGINAL["cases"]),60)
        self.assertEqual(len(pairs),24)
        self.assertEqual({x["source_family"] for x in pairs},
                         {x["family"] for x in ORIGINAL["cases"]})
        self.assertEqual(json.dumps(ORIGINAL,sort_keys=True),before)
        for pair in pairs:
            with self.subTest(pair=pair["pair_id"]):
                self.assertTrue(pair["is_counterfactual_not_modified_frozen_fixture"])
                self.assertEqual(len(pair["source_rows_PRIVATE_FOR_REVIEWER_ONLY"]),2)
                valid,bad=pair["worlds"]
                self.assertEqual(valid["public"],bad["public"])
                self.assertEqual(g02.public_Q(valid),g02.public_Q(bad))
                self.assertEqual(valid["case_id"],bad["case_id"])
                self.assertEqual(valid["Q"]["verdict"],"ALLOW")
                self.assertEqual(bad["Q"]["verdict"],"ALLOW")
                self.assertEqual(valid["truth_private_for_scoring"],"ALLOW")
                self.assertEqual(bad["truth_private_for_scoring"],"BLOCK")
                self.assertNotEqual(valid["Q"]["status"],bad["Q"]["status"])

    def test_true_and_false_are_indistinguishable_before_measurement(self):
        for pair in lab.make_public_matched_pairs(ORIGINAL["cases"]):
            for sample in (0,17,63):
                with self.subTest(pair=pair["pair_id"],sample=sample):
                    yes,no=environments(pair,rep=sample)
                    lab._check_twins(yes,no)
                    self.assertEqual(lab.public_metadata(yes),
                                     lab.public_metadata(no))
                    public=json.dumps(lab.public_metadata(yes))
                    for forbidden in ("truth_PRIVATE","CURRENT_BUT_FALSE",
                                      "independent_audit","source_variant",
                                      "source_case_id","legacy_audit_flag",
                                      "private_Q_claim_matched"):
                        self.assertNotIn(forbidden,public)

    def test_public_only_plans_equal_across_matched_private_truths(self):
        prices=SOURCE_REGIMES["PERFECT_INDEPENDENT_AUDIT_AND_CONVENTIONAL"]["prices"]
        for pair in lab.make_public_matched_pairs(ORIGINAL["cases"]):
            yes,no=environments(pair)
            with self.subTest(pair=pair["pair_id"]):
                for arm in ("A_ONLY","Q_UNAUDITED_SOURCE"):
                    y=g02.plan_public(yes["public"],yes["q"],yes["audit"],
                                      yes["direct"],prices,arm)
                    n=g02.plan_public(no["public"],no["q"],no["audit"],
                                      no["direct"],prices,arm)
                    self.assertEqual(y,n)
                # Distinct *measured* values can subsequently add evidence:
                auditor_true=g02.plan_public(
                    yes["public"],yes["q"],yes["audit"],yes["direct"],
                    prices,"Q_WITH_AUDIT_OBSERVATION")
                auditor_false=g02.plan_public(
                    no["public"],no["q"],no["audit"],no["direct"],
                    prices,"Q_WITH_AUDIT_OBSERVATION")
                self.assertEqual(auditor_true["action"],"ALLOW")
                self.assertEqual(auditor_false["action"],"REVIEW")
                direct_true=g02.plan_public(
                    yes["public"],yes["q"],yes["audit"],yes["direct"],
                    prices,"CONVENTIONAL_INDEPENDENT_MEASURED")
                direct_false=g02.plan_public(
                    no["public"],no["q"],no["audit"],no["direct"],
                    prices,"CONVENTIONAL_INDEPENDENT_MEASURED")
                self.assertEqual(direct_true["action"],"ALLOW")
                self.assertEqual(direct_false["action"],"BLOCK")

    def test_mismatched_baseline_scope_and_absent_twin_fail_closed(self):
        a,b=environments(one_pair())
        bad=deepcopy(b)
        bad["public"]["baseline_action"]="BLOCK"
        with self.assertRaisesRegex(ValueError,"leaks"):
            lab._check_twins(a,bad)
        bad=deepcopy(b)
        bad["q"]["scope_id"]="DIFFERENT_QUESTION"
        with self.assertRaisesRegex(ValueError,"leaks"):
            lab._check_twins(a,bad)
        bad=deepcopy(b)
        bad["audit"]["scope_id"]="DIFFERENT_QUESTION"
        with self.assertRaisesRegex(ValueError,"leaks"):
            lab._check_twins(a,bad)
        with self.assertRaisesRegex(ValueError,"opposite private truth"):
            lab._check_twins(a,a)

    def test_future_third_party_family_can_use_same_pairing_contract(self):
        pair=one_pair()
        third=[]
        for i,x in enumerate(pair["worlds"]):
            copied=deepcopy(x)
            copied["family"]="THIRD_PARTY_OPEN_ARCHITECTURE_TOY"
            copied["case_id"]="THIRD-"+str(i)
            copied["public"]["scope_id"]="NEW_FINITE_QUESTION"
            copied["Q"]["scope_id"]="NEW_FINITE_QUESTION"
            copied["Q"]["source_id"]="NEW_FINITE_ISSUER"
            third.append(copied)
        res=lab.make_public_matched_pairs(third)
        self.assertEqual(len(res),2)
        twin=environments(res[0])
        lab._check_twins(*twin)

    def test_pairing_rejects_missing_variant_or_unbalanced_public_Q(self):
        case=[x for x in ORIGINAL["cases"] if x["family"]=="VERS"
              and x["variant"] in ("VALID_GO","FALSE_Q")]
        with self.assertRaisesRegex(ValueError,"missing counterfactual"):
            lab.make_public_matched_pairs(case[:1])
        changed=deepcopy(case)
        changed[1]["Q"]["source_id"]="UNMATCHED_SOURCE"
        with self.assertRaisesRegex(ValueError,"public Q signals"):
            lab.make_public_matched_pairs(changed)

    def test_generic_finite_information_does_not_hardcode_fifty_fifty(self):
        none=lab.explicit_information([({"x":1},"ALLOW"),({"x":1},"BLOCK")])
        self.assertEqual(none["optimal_public_only_accuracy"],"1/2")
        self.assertEqual(none["visible_mutual_information_bits"],0)
        revealed=lab.explicit_information([({"x":1},"ALLOW"),({"x":0},"BLOCK")])
        self.assertEqual(revealed["optimal_public_only_accuracy"],"1")
        self.assertAlmostEqual(revealed["visible_mutual_information_bits"],1,places=12)
        with self.assertRaises(ValueError):
            lab.explicit_information([({"x":1},"ALLOW"),({"x":1},"NOT_ADJUDICABLE")])

    def test_frozen_source_still_contains_unscored_C_D_and_original_five_arms(self):
        old=g02.original_flag_baseline(ORIGINAL)
        self.assertEqual((old["cases"],old["source_arms"],old["source_decisions"]),
                         (60,5,300))
        self.assertEqual(old["legacy_flag_arm_wrong"],4)
        self.assertEqual(sum(x["truth_private_for_scoring"]=="NOT_ADJUDICABLE"
                             for x in ORIGINAL["cases"]),12)
        self.assertEqual({x["Q"]["kind"] for x in ORIGINAL["cases"]
                          if x["truth_private_for_scoring"]=="NOT_ADJUDICABLE"},
                         {"C","D"})


class FiniteMatchedEvidenceResults(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full=lab.run(MANIFEST)
        cls.by={x["regime"]:x for x in cls.full["regimes"]}

    def test_eight_regimes_are_paired_and_public_accuracy_is_exactly_one_half(self):
        self.assertEqual(cls_count:=self.full["original_source_true_false_Q_families"],12)
        self.assertEqual(self.full["original_source_cases_not_modified"],60)
        self.assertEqual(self.full["derived_matched_pairs"],24)
        self.assertEqual(self.full["replicates_per_pair"],64)
        self.assertEqual(self.full["total_source_world_evaluations"],8*24*2*64)
        self.assertEqual(len(self.full["source_input_sha256"]),5)
        self.assertTrue(all(len(x)==64 for x in self.full["source_input_sha256"].values()))
        self.assertEqual(len(self.by),8)
        for row in self.by.values():
            with self.subTest(regime=row["regime"]):
                m=row["public_only_before_measuring"]
                self.assertEqual(m["finite_observations"],3072)
                self.assertEqual(m["truth_counts"],{"ALLOW":1536,"BLOCK":1536})
                self.assertEqual(m["optimal_public_only_accuracy"],"1/2")
                self.assertEqual(m["optimal_public_only_correct"],1536)
                self.assertAlmostEqual(m["visible_mutual_information_bits"],0.0,places=12)
                self.assertAlmostEqual(m["conditional_truth_entropy_bits"],1.0,places=12)
                self.assertEqual(row["source_variants_private_referee"],
                                 {"FALSE_Q":1536,"VALID_GO":1536})

    def test_perfect_audit_adds_one_bit_only_after_reading(self):
        p=self.by["PERFECT_INDEPENDENT_AUDIT_AND_CONVENTIONAL"]
        self.assertEqual(p["public_only_before_measuring"]["visible_mutual_information_bits"],0)
        self.assertAlmostEqual(p["after_fallible_qualified_audit"]
                               ["visible_mutual_information_bits"],1,places=12)
        self.assertAlmostEqual(p["after_fallible_qualified_conventional"]
                               ["visible_mutual_information_bits"],1,places=12)
        arm=p["native_G02_policy_results"]
        self.assertEqual(arm["Q_UNAUDITED_SOURCE"]["wrong"],1536)
        self.assertEqual(arm["Q_WITH_AUDIT_OBSERVATION"]["wrong"],0)
        self.assertEqual(arm["Q_WITH_AUDIT_OBSERVATION"]["unresolved"],1536)
        self.assertEqual(arm["CONVENTIONAL_INDEPENDENT_MEASURED"]["wrong"],0)
        self.assertEqual(arm["CONVENTIONAL_INDEPENDENT_MEASURED"]["unresolved"],0)

    def test_blind_or_unavailable_audit_adds_zero_information(self):
        for name in ("BLIND_AUDIT_FALSE_ASSURANCE",
                     "AUDIT_UNAVAILABLE_DIRECT_AVAILABLE",
                     "AUDIT_UNQUALIFIED_WRONG_SCOPE",
                     "AUDIT_FALSE_ALARM_DOMINANT"):
            r=self.by[name]
            with self.subTest(name=name):
                self.assertAlmostEqual(
                    r["after_fallible_qualified_audit"]
                     ["visible_mutual_information_bits"],0,places=12)
        blind=self.by["BLIND_AUDIT_FALSE_ASSURANCE"]["native_G02_policy_results"]
        self.assertEqual(blind["Q_WITH_AUDIT_OBSERVATION"]["wrong"],1536)
        unavailable=self.by["AUDIT_UNAVAILABLE_DIRECT_AVAILABLE"]["native_G02_policy_results"]
        self.assertEqual(unavailable["Q_WITH_AUDIT_OBSERVATION"]["wrong"],0)
        self.assertEqual(unavailable["Q_WITH_AUDIT_OBSERVATION"]["unresolved"],3072)
        self.assertEqual(unavailable["Q_WITH_AUDIT_OBSERVATION"]["missed_justified_allows"],1536)

    def test_noise_produces_graded_information_and_conventional_can_win(self):
        strong=self.by["RELIABLE_AUDIT_NOISY_CONVENTIONAL"]
        weak=self.by["WEAK_AUDIT_STRONG_CONVENTIONAL"]
        for row in (strong,weak):
            i=row["after_fallible_qualified_audit"]["visible_mutual_information_bits"]
            self.assertGreater(i,0)
            self.assertLess(i,1)
        self.assertLess(
            weak["native_G02_policy_results"]["CONVENTIONAL_INDEPENDENT_MEASURED"]["wrong"],
            weak["native_G02_policy_results"]["Q_WITH_AUDIT_OBSERVATION"]["wrong"])
        self.assertLess(
            strong["native_G02_policy_results"]["Q_WITH_AUDIT_OBSERVATION"]["wrong"],
            strong["native_G02_policy_results"]["CONVENTIONAL_INDEPENDENT_MEASURED"]["wrong"])

    def test_price_only_changes_native_accounting_not_observed_decisions(self):
        normal=self.by["RELIABLE_AUDIT_NOISY_CONVENTIONAL"]["native_G02_policy_results"]
        costly=self.by["RELIABLE_AUDIT_BUT_EXPENSIVE"]["native_G02_policy_results"]
        for arm in g02.ARMS:
            for key in ("correct","wrong","unresolved","false_allow","false_block",
                        "missed_justified_allows"):
                self.assertEqual(normal[arm][key],costly[arm][key])
        self.assertNotEqual(
            normal["Q_WITH_AUDIT_OBSERVATION"]["total_synthetic_instrument_cost"],
            costly["Q_WITH_AUDIT_OBSERVATION"]["total_synthetic_instrument_cost"])

    def test_source_fingerprint_and_no_outcome_status_promoted(self):
        self.assertEqual(self.full["interpretation"],
            "FINITE_SYNTHETIC_MATCHED_BINARY_Q_ONLY_NO_REAL_AUDIT_METRICS_OR_OPEN_C_D_PROBABILITY")
        self.assertTrue(self.full["source_fixtures_preserved"])
        self.assertTrue(self.full["not_an_adaptive_agent_or_empirical_classifier_benchmark"])
        self.assertEqual(self.full["source_legacy_public_view_leakage"]
                         ["optimal_public_only_accuracy"],"3/4")

    def test_bad_manifest_fails_before_running_and_valid_resize_replays(self):
        x=deepcopy(MANIFEST)
        x["source_regimes"]=["MISSING_SOURCE_REGIME"]
        with self.assertRaisesRegex(ValueError,"unsupported source regime"):
            lab.run(x)
        x=deepcopy(MANIFEST)
        x["baseline_actions"]=["REVIEW"]
        with self.assertRaisesRegex(ValueError,"both original A baseline"):
            lab.run(x)
        x=deepcopy(MANIFEST)
        x["replicates_per_pair"]=4
        with self.assertRaisesRegex(ValueError,"unbounded"):
            lab.run(x)
        tiny=deepcopy(MANIFEST)
        tiny["replicates_per_pair"]=8
        tiny["source_regimes"]=["PERFECT_INDEPENDENT_AUDIT_AND_CONVENTIONAL"]
        report=lab.run(tiny)
        self.assertEqual(report["total_source_world_evaluations"],24*2*8)
        self.assertEqual(report["regimes"][0]["public_only_before_measuring"]
                         ["optimal_public_only_accuracy"],"1/2")


if __name__=="__main__":
    unittest.main()
