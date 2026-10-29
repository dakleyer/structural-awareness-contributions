"""G-04 adverse/positive regression tests for independent paired finite contrasts."""
from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import inspect
import json
from pathlib import Path
import unittest

import campaign
from g04_factorial import (
    ARMS, SOURCE_SCOPE, CLOCK, _qualified, create_world, native_referee,
    paired_evaluation, plan_public, run_factorial, run_manifest,
    validate_manifest,
)

HERE = Path(__file__).resolve().parent
MANIFEST = json.loads((HERE / "G04_PROTOCOL.json").read_text(encoding="utf-8"))

PUBLIC = {
    "role_change_declared_in_A": True,
    "owner_consent": True,
    "authorized_receiver": True,
    "joint_protocol_available": True,
    "current_A_service": "holder_receives_one",
    "question_scope": SOURCE_SCOPE,
}
AUTHENTIC = {
    "available":True,"claims_feasible":True,
    "signed":True,"scope":SOURCE_SCOPE,"observed_at":CLOCK-1,"ttl":3,
}
DIRECT_POSITIVE = {
    "available":True, "measured_extra_stock":True,
    "measured_need":True,"measured_route_safe":True,
    "signed":True,"scope":SOURCE_SCOPE,"observed_at":CLOCK-1,"ttl":3,
}
WORLD_PASS = {
    "stock":2,"beneficiary_need":True,"route_safe":True,
    "role_change_declared_in_A":True,"owner_consent":True,
    "authorized_receiver":True,"joint_protocol_available":True,
}


def package(world=None,q=None,direct=None):
    return {
        "scenario_id":"hand-constructed/adversarial",
        "public_A":deepcopy(PUBLIC),
        "source_Q":deepcopy(AUTHENTIC if q is None else q),
        "domain_observation":deepcopy(DIRECT_POSITIVE if direct is None else direct),
        "targeted_observation":deepcopy(DIRECT_POSITIVE),
        "truth_PRIVATE_FOR_REFEREE_ONLY":deepcopy(WORLD_PASS if world is None else world),
    }


class HistoricalRulePreservation(unittest.TestCase):
    def test_original_eight_legacy_rows_remain_a_specification(self):
        old = campaign.factorial_joint_information()
        new = run_factorial()["legacy_2x2x2"]
        self.assertEqual(len(old), 8)
        self.assertEqual(len(new), 8)
        for old_row, computed in zip(old,new):
            self.assertEqual(
                old_row["additional_joint_output_synthetic"],
                computed["additional_joint_output_computed_from_native_operator"],
            )
            self.assertEqual(old_row["proof_required"],computed["proof_required"])
            self.assertEqual(old_row["valid_Q_available"],computed["source_Q_present"])
            self.assertEqual(old_row["joint_mechanism_available"],
                             computed["joint_protocol_available"])
            self.assertEqual(
                computed["classification"],
                "SPECIFICATION_PLUS_NATIVE_PHYSICAL_REFEREE_NOT_FH_C_TEST",
            )

    def test_legacy_fh_c_profiles_are_retained_as_assumption_demos(self):
        legacy = campaign.fh_c_competing_ablations()
        self.assertEqual(len(legacy), 8)
        self.assertEqual(
            set(row["profile"] for row in legacy),
            {"BOUNDARY_SIGNAL_STRONGER","DOMAIN_FACTS_STRONGER"},
        )
        self.assertTrue(all(row["status"]=="SOURCE_INSPIRED_SYNTHETIC_ABLATION_ONLY"
                            for row in legacy))


class PhysicalAndEpistemicBoundaries(unittest.TestCase):
    def test_signed_scoped_b_can_be_factually_wrong(self):
        ref=native_referee({**WORLD_PASS,"stock":1})
        self.assertTrue(_qualified(AUTHENTIC))
        self.assertFalse(ref["eligible"])
        self.assertEqual(ref["physical_status"],"IMPOSSIBLE")
        self.assertEqual(ref["confirmed_output_if_authorized"],0)

    def test_negative_factorial_controls_do_not_get_a_fabricated_2(self):
        neg = {r["case"]:r for r in run_factorial()["adversarial_controls"]}
        self.assertTrue(neg["SCOPED_SIGNED_BUT_FALSE_STOCK"]["source_q_qualified"])
        self.assertEqual(neg["SCOPED_SIGNED_BUT_FALSE_STOCK"]
                         ["physical_admission"],"MATERIALLY_INFEASIBLE")
        self.assertEqual(neg["SCOPED_SIGNED_BUT_FALSE_STOCK"]
                         ["delivered_if_fully_admitted"],0)
        self.assertEqual(neg["CONSENT_ABSENT"]["delivered_if_fully_admitted"],0)
        self.assertFalse(neg["OUT_OF_SCOPE_SOURCE"]["source_q_qualified"])

    def test_qualification_is_scoped_fresh_and_authenticated_but_not_truth(self):
        self.assertTrue(_qualified(AUTHENTIC))
        for patch in (
            {"signed":False},{"scope":"military-conquest"},{"observed_at":CLOCK-9},
            {"ttl":0},{"available":False},{"observed_at":CLOCK+1},
        ):
            with self.subTest(patch=patch):
                self.assertFalse(_qualified({**AUTHENTIC,**patch}))

    def test_public_planning_has_no_private_truth_argument(self):
        self.assertNotIn("truth",inspect.signature(plan_public).parameters)
        self.assertNotIn("world",inspect.signature(plan_public).parameters)
        reference=package()
        counterfactual=deepcopy(reference)
        counterfactual["truth_PRIVATE_FOR_REFEREE_ONLY"]={"stock":1,**{
            key:WORLD_PASS[key] for key in WORLD_PASS if key!="stock"}}
        a=paired_evaluation(reference)
        b=paired_evaluation(counterfactual)
        for arm in ARMS:
            with self.subTest(arm=arm):
                self.assertEqual(a["arms"][arm]["public_plan"],
                                 b["arms"][arm]["public_plan"])
        self.assertNotEqual(a["private_referee_only"]["eligible"],
                            b["private_referee_only"]["eligible"])

    def test_material_change_is_computed_by_the_original_pr68_operator(self):
        good=native_referee(WORLD_PASS)
        bad=native_referee({**WORLD_PASS,"stock":1})
        no_route=native_referee({**WORLD_PASS,"route_safe":False})
        no_consent=native_referee({**WORLD_PASS,"owner_consent":False})
        self.assertEqual(good["source_owned"],
                         "PR68.dimension_experiment.material_flow")
        self.assertEqual(good["confirmed_output_if_authorized"],1)
        self.assertTrue(good["eligible"])
        self.assertFalse(bad["eligible"])
        self.assertEqual(bad["confirmed_output_if_authorized"],0)
        self.assertEqual(no_route["admission"],"BLOCKED_BY_CONDITION")
        self.assertEqual(no_consent["admission"],"BLOCKED_BY_CONDITION")

    def test_false_b_is_not_repaired_by_more_belief_in_its_signature(self):
        world={**WORLD_PASS,"stock":1}
        r=paired_evaluation(package(world=world))
        self.assertTrue(r["arms"]["SOURCE_BOUNDARY_ONLY"]["unjustified_proposal"])
        self.assertTrue(r["arms"]["DOMAIN_FACTS_ONLY"]["unjustified_proposal"])
        # Both instruments can be factually wrong in the same direction;
        # double agreement never upgrades either to independently observed truth.
        self.assertTrue(r["arms"]["BOTH_SOURCE_AND_DOMAIN"]["unjustified_proposal"])
        self.assertFalse(r["arms"]["SOURCE_BOUNDARY_ONLY"]
                         ["would_be_committed_under_declared_rights"])

    def test_accurate_domain_measurement_can_block_a_valid_but_false_q(self):
        world={**WORLD_PASS,"stock":1}
        direct={**DIRECT_POSITIVE,"measured_extra_stock":False}
        a=paired_evaluation(package(world=world,direct=direct))
        self.assertTrue(a["arms"]["SOURCE_BOUNDARY_ONLY"]["unjustified_proposal"])
        self.assertFalse(a["arms"]["DOMAIN_FACTS_ONLY"]["unjustified_proposal"])
        self.assertEqual(a["arms"]["BOTH_SOURCE_AND_DOMAIN"]["public_plan"]["status"],
                         "CONTRADICTORY_EVIDENCE_REQUALIFICATION")
        self.assertEqual(a["arms"]["CONVENTIONAL_TARGETED"]
                         ["observed_incremental_service_after_admission"],0)

    def test_unqualified_q_cannot_block_independent_true_domain_evidence(self):
        q={**AUTHENTIC,"scope":"outside-question"}
        a=paired_evaluation(package(q=q))
        self.assertFalse(a["arms"]["SOURCE_BOUNDARY_ONLY"]["public_plan"]["propose"])
        self.assertTrue(a["arms"]["DOMAIN_FACTS_ONLY"]["public_plan"]["propose"])
        self.assertTrue(a["arms"]["BOTH_SOURCE_AND_DOMAIN"]["public_plan"]["propose"])
        self.assertTrue(a["arms"]["NAIVE_SOURCE_ONLY_CONTROL"]["public_plan"]["propose"])

    def test_missing_q_does_not_mandate_inactivity_with_good_direct_facts(self):
        q={**AUTHENTIC,"available":False}
        a=paired_evaluation(package(q=q))
        self.assertFalse(a["arms"]["SOURCE_BOUNDARY_ONLY"]["public_plan"]["propose"])
        self.assertTrue(a["arms"]["DOMAIN_FACTS_ONLY"]["public_plan"]["propose"])
        self.assertTrue(a["arms"]["BOTH_SOURCE_AND_DOMAIN"]["public_plan"]["propose"])

    def test_qualified_good_q_can_beat_wrong_domain_reading(self):
        direct={**DIRECT_POSITIVE,"measured_extra_stock":False}
        a=paired_evaluation(package(direct=direct))
        self.assertTrue(a["arms"]["SOURCE_BOUNDARY_ONLY"]["justified_proposal"])
        self.assertTrue(a["arms"]["DOMAIN_FACTS_ONLY"]["missed_feasible_candidate"])
        self.assertTrue(a["arms"]["BOTH_SOURCE_AND_DOMAIN"]["missed_feasible_candidate"])

    def test_authority_consent_and_mission_a_are_nonfungible_for_all_arms(self):
        for block in ("owner_consent","authorized_receiver",
                      "role_change_declared_in_A","joint_protocol_available"):
            with self.subTest(block=block):
                w=package()
                w["public_A"][block]=False
                w["truth_PRIVATE_FOR_REFEREE_ONLY"][block]=False
                a=paired_evaluation(w)
                for row in a["arms"].values():
                    self.assertFalse(row["public_plan"]["propose"])
                    self.assertEqual(row["public_plan"]["declared_cost"],"0")
                    self.assertFalse(row["would_be_committed_under_declared_rights"])

    def test_info_cost_is_never_subtracted_from_food_or_welfare(self):
        trial=paired_evaluation(package())
        self.assertEqual(trial["arms"]["DOMAIN_FACTS_ONLY"]
                         ["instrument_cost_units_declared_SEPARATE_FROM_FOOD"],"2/5")
        self.assertEqual(trial["arms"]["BOTH_SOURCE_AND_DOMAIN"]
                         ["instrument_cost_units_declared_SEPARATE_FROM_FOOD"],"1/2")
        self.assertEqual(trial["arms"]["CONVENTIONAL_TARGETED"]
                         ["instrument_cost_units_declared_SEPARATE_FROM_FOOD"],"4/5")
        self.assertTrue(trial["arms"]["CONVENTIONAL_TARGETED"]
                        ["would_be_committed_under_declared_rights"])


class ReproduciblePairedGeneratorTests(unittest.TestCase):
    def test_manifest_has_independent_probabilities_and_is_bounded(self):
        validate_manifest(MANIFEST)
        self.assertEqual(len(MANIFEST["regimes"]),6)
        self.assertGreaterEqual(MANIFEST["worlds_per_regime"],16)
        self.assertLessEqual(MANIFEST["worlds_per_regime"],256)
        for invalid in ({"source_probability":"2"},
                        {"source_correct_if_qualified":"-1"},
                        {"domain_accuracy":True}):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                p=deepcopy(MANIFEST)
                p["regimes"][0]["parameters"].update(invalid)
                validate_manifest(p)

    def test_same_worlds_are_paired_across_every_2x2_ablation(self):
        params=MANIFEST["regimes"][0]["parameters"]
        world=create_world(12,params,MANIFEST["seed"])
        record=paired_evaluation(world)
        self.assertEqual(set(record["arms"]),set(ARMS))
        self.assertTrue(all(a["public_plan"]["no_hidden_world_access"]
                            for a in record["arms"].values()))
        self.assertEqual(record["source_Q"],world["source_Q"])
        self.assertEqual(record["truth_PRIVATE_NOT_USED_FOR_PLANNING"],
                         world["truth_PRIVATE_FOR_REFEREE_ONLY"])

    def test_generator_is_seed_stable_but_parameters_change_the_data(self):
        params=MANIFEST["regimes"][0]["parameters"]
        one=create_world(27,params,MANIFEST["seed"])
        two=create_world(27,params,MANIFEST["seed"])
        self.assertEqual(one,two)
        changed={**params,"source_probability":"0"}
        changed_world=create_world(27,changed,MANIFEST["seed"])
        self.assertFalse(changed_world["source_Q"]["available"])
        self.assertEqual(one["truth_PRIVATE_FOR_REFEREE_ONLY"],
                         changed_world["truth_PRIVATE_FOR_REFEREE_ONLY"])
        self.assertEqual(one["public_A"],changed_world["public_A"])

    def test_all_regimes_report_both_refutation_directions_without_fixed_winners(self):
        # Exact finite test of a declared synthetic generator, NOT a market rate.
        result=run_manifest(MANIFEST)
        self.assertEqual(result["total_matched_worlds"],
                         6*MANIFEST["worlds_per_regime"])
        self.assertTrue(result["no_policy_has_private_referee_access"])
        self.assertEqual(len(result["factorial"]["legacy_2x2x2"]),8)
        directions={x["bounded_FH_C_direction"] for x in result["paired_regimes"]}
        self.assertIn("BOUNDARY_FEWER_INVALID_CANDIDATES",directions)
        self.assertIn("DOMAIN_FACTS_FEWER_INVALID_CANDIDATES",directions)
        for group in result["paired_regimes"]:
            self.assertEqual(set(group["policies"]),set(ARMS))
            self.assertEqual(group["worlds"],MANIFEST["worlds_per_regime"])
            for count in group["policies"].values():
                self.assertEqual(count["cost_is_not_subtracted_from_food"],
                                 "NONCOMMENSURATE_UNITS")
                self.assertGreaterEqual(count["information_cost_units"].count("/"),0)
                self.assertLessEqual(count["committable_under_declared_rights"],
                                     count["justified_candidate_proposals"])
            self.assertEqual(group["FH_C_real_world_causal_hypothesis_status"],
                             "NOT_IDENTIFIED_FROM_SYNTHETIC_GENERATOR")

    def test_no_source_abstention_is_not_labelled_a_superior_strategy(self):
        # A "zero wrong proposal" rate caused by zero proposals is NOT
        # evidence of a stronger procedure. The original single metric
        # would create exactly this false-positive advantage.
        report=run_manifest(MANIFEST)
        rows={row["regime"]:row for row in report["paired_regimes"]}
        source_absent=rows["SOURCE_ABSENT_DIRECTED_AVAILABLE"]
        b=source_absent["policies"]["SOURCE_BOUNDARY_ONLY"]
        facts=source_absent["policies"]["DOMAIN_FACTS_ONLY"]
        self.assertEqual(b["unjustified_candidate_proposals"],0)
        self.assertEqual(b["justified_candidate_proposals"],0)
        self.assertGreater(b["missed_feasible_candidates"],
                           facts["missed_feasible_candidates"])
        self.assertEqual(source_absent["source_vs_facts_two_axis_order"],
                         "INCOMPARABLE_ERROR_VS_MISSED_OPPORTUNITY_TRADEOFF")
        self.assertIn("SOURCE_BOUNDARY_ONLY",
                      source_absent["nonfungible_three_axis_pareto_front"])
        self.assertIn("DOMAIN_FACTS_ONLY",
                      source_absent["nonfungible_three_axis_pareto_front"])

    def test_both_scientific_directions_and_a_real_tradeoff_survive_three_axes(self):
        report=run_manifest(MANIFEST)
        rows={row["regime"]:row for row in report["paired_regimes"]}
        self.assertEqual(
            rows["QUALIFIED_SOURCE_RELIABLE_SENSOR_NOISY"]
            ["source_vs_facts_two_axis_order"],
            "BOUNDARY_DOMINATES_ON_ERRORS_AND_MISSED_CANDIDATES")
        self.assertEqual(
            rows["SOURCE_FACTUALLY_WEAK_DIRECT_FACTS_PRECISE"]
            ["source_vs_facts_two_axis_order"],
            "DOMAIN_FACTS_DOMINATES_ON_ERRORS_AND_MISSED_CANDIDATES")
        self.assertEqual(
            rows["SOURCE_ABSENT_DIRECTED_AVAILABLE"]
            ["source_vs_facts_two_axis_order"],
            "INCOMPARABLE_ERROR_VS_MISSED_OPPORTUNITY_TRADEOFF")
        for row in report["paired_regimes"]:
            self.assertEqual(
                row["pareto_axes_minimized"],
                ["unjustified_candidate_proposals","missed_feasible_candidates",
                 "information_cost_units"])
            self.assertTrue(row["nonfungible_three_axis_pareto_front"])
            self.assertTrue(set(row["nonfungible_three_axis_pareto_front"])
                            <=set(ARMS))

    def test_resizing_world_count_does_not_change_a_theory_or_a_source(self):
        small=deepcopy(MANIFEST)
        small["worlds_per_regime"]=16
        result=run_manifest(small)
        self.assertEqual(result["total_matched_worlds"],96)
        self.assertEqual(result["evidence_tier"],
                         "DESIGNED_FINITE_SYNTHETIC_NOT_FIELD_OBSERVATION")
        self.assertEqual(result["hypothesis_status"],
                         "FH-C_CAUSAL_PRIORITY_NOT_PROVEN_OR_REFUTED_BY_SYNTHETIC_FINITE_EXERCISE")



if __name__=="__main__":
    unittest.main()
