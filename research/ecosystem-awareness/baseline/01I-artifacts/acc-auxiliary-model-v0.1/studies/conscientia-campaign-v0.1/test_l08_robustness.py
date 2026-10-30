"""L-08 falsifiers, original-case preservation, exact tradeoffs and reuse tests."""
from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
import unittest

from g04_factorial import (
    ARMS as G04_ARMS, CLOCK, SOURCE_SCOPE, create_world,
    paired_evaluation, run_factorial, run_manifest as g04_manifest_run,
)
from l08_robustness import (
    NORMALIZED_DOMAIN, FAIR_ARMS, ALL_ARMS, _public_domain_plan,
    checked_price_contract, observed_case, _measure, _result_for,
    two_arm_order, pareto, validate, run,
)

HERE=Path(__file__).resolve().parent
L08=json.loads((HERE/"L08_PROTOCOL.json").read_text(encoding="utf-8"))
G04=json.loads((HERE/"G04_PROTOCOL.json").read_text(encoding="utf-8"))


def _world(*, stock=2, source_good=True, domain_good=True, domain_signed=True,
           owner_consent=True) -> dict:
    public={
        "role_change_declared_in_A":True,"owner_consent":owner_consent,
        "authorized_receiver":True,"joint_protocol_available":True,
        "current_A_service":"holder_receives_one",
        "question_scope":SOURCE_SCOPE,
    }
    origin={
        "available":True,"claims_feasible":source_good,
        "signed":True,"scope":SOURCE_SCOPE,"observed_at":CLOCK-1,
        "ttl":3,"source_id":"synthetic-source",
    }
    sensor={
        "available":True,"measured_extra_stock":domain_good,
        "measured_need":True,"measured_route_safe":True,
        "signed":domain_signed,
        "scope":SOURCE_SCOPE if domain_signed else "OTHER-QUESTION",
        "observed_at":CLOCK-1 if domain_signed else CLOCK-9,
        "ttl":3,"source_id":"synthetic-domain",
    }
    return {
        "scenario_id":"HANDCRAFTED-NEGATIVE-CONTROL",
        "public_A":public,"source_Q":origin,"domain_observation":sensor,
        "targeted_observation":deepcopy(sensor),
        "truth_PRIVATE_FOR_REFEREE_ONLY":{
            "stock":stock,"beneficiary_need":True,"route_safe":True,
            "role_change_declared_in_A":True,"owner_consent":owner_consent,
            "authorized_receiver":True,"joint_protocol_available":True,
        },
    }


class L08PhysicalAndHistoricalRegressions(unittest.TestCase):
    def test_original_g04_source_policies_not_edited(self):
        a=paired_evaluation(_world())
        self.assertEqual(set(a["arms"]),set(G04_ARMS))
        self.assertNotIn(NORMALIZED_DOMAIN,a["arms"])
        self.assertEqual(len(run_factorial()["legacy_2x2x2"]),8)
        self.assertEqual(a["private_referee_only"]["source_owned"],
                         "PR68.dimension_experiment.material_flow")

    def test_false_qualified_B_is_not_a_permission_or_physical_truth(self):
        r=observed_case(_world(stock=1))
        self.assertTrue(r["source_qualification_instrument_metadata_only"])
        self.assertTrue(r["arms"]["SOURCE_BOUNDARY_ONLY"]["unjustified_proposal"])
        self.assertFalse(r["arms"]["SOURCE_BOUNDARY_ONLY"]
                         ["would_be_committed_under_declared_rights"])
        self.assertTrue(r["arms"]["SOURCE_BOUNDARY_ONLY"]["public_plan"]["propose"])

    def test_metadata_provenance_symmetry_is_an_explicit_new_comparator(self):
        w=_world(domain_signed=False,domain_good=True)
        a=observed_case(w)
        legacy=a["arms"]["DOMAIN_FACTS_ONLY"]
        scoped=a["arms"][NORMALIZED_DOMAIN]
        self.assertTrue(legacy["public_plan"]["propose"])
        self.assertFalse(scoped["public_plan"]["propose"])
        self.assertEqual(scoped["public_plan"]["status"],
                         "NO_QUALIFIED_DOMAIN_SIGNAL")
        self.assertEqual(scoped["public_plan"]["declared_cost"],"2/5")
        self.assertTrue(scoped["missed_feasible_candidate"])
        self.assertEqual(scoped["public_plan"]["source_metadata_contract"],
                         "SAME_SCOPED_FRESH_ATTRIBUTED_CONDITIONS_AS_SOURCE_BOUNDARY_ONLY")
        self.assertFalse(a["domain_qualification_instrument_metadata_only"])

    def test_qualified_domain_and_legacy_raw_concur_if_source_is_qualified(self):
        a=observed_case(_world())
        self.assertTrue(a["domain_qualification_instrument_metadata_only"])
        self.assertEqual(a["arms"][NORMALIZED_DOMAIN]["public_plan"]["propose"],
                         a["arms"]["DOMAIN_FACTS_ONLY"]["public_plan"]["propose"])
        self.assertEqual(a["arms"][NORMALIZED_DOMAIN]["justified_proposal"],
                         a["arms"]["DOMAIN_FACTS_ONLY"]["justified_proposal"])

    def test_genuine_contradiction_source_and_domain_stays_unresolved(self):
        a=observed_case(_world(source_good=True,domain_good=False))
        self.assertTrue(a["arms"]["SOURCE_BOUNDARY_ONLY"]["justified_proposal"])
        self.assertTrue(a["arms"][NORMALIZED_DOMAIN]["missed_feasible_candidate"])
        self.assertEqual(a["arms"]["BOTH_SOURCE_AND_DOMAIN"]["public_plan"]["status"],
                         "CONTRADICTORY_EVIDENCE_REQUALIFICATION")
        self.assertFalse(a["arms"]["BOTH_SOURCE_AND_DOMAIN"]["public_plan"]["propose"])

    def test_public_planning_does_not_read_private_world(self):
        a=_world(stock=2)
        b=_world(stock=1)
        first=observed_case(a)
        second=observed_case(b)
        for arm in ALL_ARMS:
            with self.subTest(arm=arm):
                self.assertEqual(first["arms"][arm]["public_plan"],
                                 second["arms"][arm]["public_plan"])
        self.assertNotEqual(first["eligibility_private_post_hoc"],
                            second["eligibility_private_post_hoc"])
        self.assertTrue(first["arms"][NORMALIZED_DOMAIN]["justified_proposal"])
        self.assertTrue(second["arms"][NORMALIZED_DOMAIN]["unjustified_proposal"])

    def test_consent_gate_applies_to_all_six_policies(self):
        r=observed_case(_world(owner_consent=False))
        for arm in ALL_ARMS:
            with self.subTest(arm=arm):
                self.assertFalse(r["arms"][arm]["public_plan"]["propose"])
                self.assertFalse(r["arms"][arm]["would_be_committed_under_declared_rights"])
                self.assertEqual(r["arms"][arm]["public_plan"]["declared_cost"],"0")

    def test_legacy_unqualified_control_excluded_from_primary_fair_frontier(self):
        m=_measure([observed_case(_world())])
        prices=L08["price_contracts"]
        fronts=_result_for(m,prices)
        self.assertNotIn("DOMAIN_FACTS_ONLY",
                         fronts["two_axis_front_no_price"])
        self.assertNotIn("NAIVE_SOURCE_ONLY_CONTROL",
                         fronts["two_axis_front_no_price"])
        for profile in fronts["three_axis_fronts_by_price_contract"].values():
            self.assertTrue(set(profile["three_axis_pareto_front"])<=set(FAIR_ARMS))


class SensitivityAndCostMechanisms(unittest.TestCase):
    def test_validation_rejects_invented_probability_and_cost(self):
        validate(L08)
        for field,value in (("source_probability","11/10"),
                            ("domain_accuracy",True),
                            ("consent_probability","-1/10")):
            with self.subTest(field=field):
                broken=deepcopy(L08)
                broken["panels"][0]["base_parameters"][field]=value
                with self.assertRaises(ValueError):
                    validate(broken)
        broken=deepcopy(L08)
        broken["price_contracts"][0]["unit_prices"]["source_review"]="-1/10"
        with self.assertRaisesRegex(ValueError,"negative"):
            validate(broken)
        broken=deepcopy(L08)
        broken["accuracy_grid"]=["1/2","1/2"]
        with self.assertRaisesRegex(ValueError,"duplicate"):
            validate(broken)

    def test_price_cost_is_exact_and_not_converted_into_food(self):
        counts={
            "instrument_consultations":{
                "source_review":2,"domain_measurement":3,"conventional_directed":1
            }
        }
        from l08_robustness import _cost
        schedule=checked_price_contract({
            "source_review":"1/10","domain_measurement":"2/5",
            "conventional_directed":"4/5",
        })
        self.assertEqual(_cost(counts,schedule),Fraction(11,5))
        self.assertEqual(schedule["source_review"],Fraction(1,10))

    def test_two_axis_front_can_be_different_from_price_driven_front(self):
        from l08_robustness import _result_for
        base={
            arm:{"invalid_proposals":1,"missed_valid_opportunities":2,
                 "instrument_consultations":({"source_review":1} if
                   arm=="SOURCE_BOUNDARY_ONLY" else
                   {"domain_measurement":1} if arm==NORMALIZED_DOMAIN else
                   {"source_review":1,"domain_measurement":1}
                   if arm=="BOTH_SOURCE_AND_DOMAIN" else
                   {"conventional_directed":1})}
            for arm in FAIR_ARMS
        }
        res=_result_for(base,L08["price_contracts"])
        self.assertEqual(set(res["two_axis_front_no_price"]),set(FAIR_ARMS))
        cheap=res["three_axis_fronts_by_price_contract"]["SOURCE_CHEAP_ORIGINAL"]
        expensive=res["three_axis_fronts_by_price_contract"]["SOURCE_EXPENSIVE_DIRECT_CHEAP"]
        self.assertEqual(cheap["three_axis_pareto_front"],["SOURCE_BOUNDARY_ONLY"])
        self.assertEqual(set(expensive["three_axis_pareto_front"]),
                         {NORMALIZED_DOMAIN,"CONVENTIONAL_TARGETED"})
        self.assertEqual(base["SOURCE_BOUNDARY_ONLY"]["invalid_proposals"],1)

    def test_two_axis_dominance_and_tradeoff_are_true_partial_orders(self):
        b={"invalid_proposals":0,"missed_valid_opportunities":10}
        d={"invalid_proposals":1,"missed_valid_opportunities":4}
        self.assertEqual(two_arm_order(b,d),
                         "INCOMPARABLE_ERROR_VS_MISSED_OPPORTUNITY_TRADEOFF")
        self.assertEqual(two_arm_order(b,b),"TIE_ON_ERRORS_AND_MISSED_CANDIDATES")
        good={"invalid_proposals":0,"missed_valid_opportunities":2}
        self.assertEqual(two_arm_order(good,d),
                         "BOUNDARY_DOMINATES_ON_ERRORS_AND_MISSED_CANDIDATES")
        self.assertEqual(two_arm_order(d,good),
                         "DOMAIN_FACTS_DOMINATES_ON_ERRORS_AND_MISSED_CANDIDATES")

    def test_matched_seed_changes_accuracy_but_not_true_world_or_A(self):
        panel=L08["panels"][1]["base_parameters"]
        p1={**panel,"source_correct_if_qualified":"1/2","domain_accuracy":"1"}
        p2={**panel,"source_correct_if_qualified":"1","domain_accuracy":"1/2"}
        a=create_world(17,p1,L08["seed"])
        b=create_world(17,p2,L08["seed"])
        self.assertEqual(a["public_A"],b["public_A"])
        self.assertEqual(a["truth_PRIVATE_FOR_REFEREE_ONLY"],
                         b["truth_PRIVATE_FOR_REFEREE_ONLY"])
        self.assertEqual(a["source_Q"]["available"],b["source_Q"]["available"])
        self.assertEqual(a["domain_observation"]["available"],
                         b["domain_observation"]["available"])

    def test_third_party_record_format_reusable_without_model_branches(self):
        # An external simulator may provide its own per-arm public decisions
        # and independent referee truth through the same normalized record API.
        rec=observed_case(_world())
        self.assertEqual(rec["native_operator"],
                         "PR68.dimension_experiment.material_flow")
        m=_measure([rec,rec])
        self.assertEqual(m["SOURCE_BOUNDARY_ONLY"]["valid_proposals"],2)
        self.assertEqual(m[NORMALIZED_DOMAIN]["valid_proposals"],2)
        self.assertEqual(m["CONVENTIONAL_TARGETED"]["incremental_food_service"],2)


class PublishedConditionalResults(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # An exhaustive 7x7 × two panels × 192 source-owned physical
        # evaluations should run once for this regression class.
        cls.full=run(L08)
        cls.panels={p["id"]:p for p in cls.full["panels"]}
        cls.equal={ (c["assumed_accuracy_of_qualified_source"],
                     c["assumed_per_domain_observation_accuracy"]):c
                    for c in cls.panels["EQUAL_PUBLIC_SOURCE_AND_DOMAIN_AVAILABILITY"]["cells"]}

    def test_reproducible_grid_has_18816_paired_decisions(self):
        self.assertEqual(self.full["total_paired_cell_evaluations"],2*49*192)
        self.assertEqual(self.full["total_distinct_matched_worlds"],192)
        self.assertEqual(self.full["horizon"],"ONE_DECLARED_DECISION_AT_CLOCK_10")
        self.assertEqual(len(self.full["panels"]),2)
        self.assertEqual(sum(p["count_cells"] for p in self.full["panels"]),98)
        self.assertTrue(self.full["experiment_not_human_measurement_or_real_source_reliability"])
        self.assertEqual(self.full["external_FH_C_causality"],"NOT_IDENTIFIED")

    def test_perfect_source_beats_noisy_domain_under_equal_access(self):
        a=self.equal[("1","1/2")]
        self.assertEqual(a["matched_two_axis_source_vs_scoped_domain"],
                         "BOUNDARY_DOMINATES_ON_ERRORS_AND_MISSED_CANDIDATES")
        self.assertEqual(a["instrumental_arms"]["SOURCE_BOUNDARY_ONLY"]["invalid_proposals"],0)

    def test_perfect_domain_beats_noisy_source_under_equal_access(self):
        a=self.equal[("1/2","1")]
        self.assertEqual(a["matched_two_axis_source_vs_scoped_domain"],
                         "DOMAIN_FACTS_DOMINATES_ON_ERRORS_AND_MISSED_CANDIDATES")
        self.assertEqual(a["instrumental_arms"][NORMALIZED_DOMAIN]["invalid_proposals"],0)

    def test_both_perfect_have_same_physical_decision_not_forced_b_advantage(self):
        a=self.equal[("1","1")]
        self.assertEqual(a["matched_two_axis_source_vs_scoped_domain"],
                         "TIE_ON_ERRORS_AND_MISSED_CANDIDATES")
        self.assertEqual(a["instrumental_arms"]["SOURCE_BOUNDARY_ONLY"]["invalid_proposals"],0)
        self.assertEqual(a["instrumental_arms"][NORMALIZED_DOMAIN]["invalid_proposals"],0)
        self.assertEqual(a["instrumental_arms"]["SOURCE_BOUNDARY_ONLY"]["missed_valid_opportunities"],
                         a["instrumental_arms"][NORMALIZED_DOMAIN]["missed_valid_opportunities"])

    def test_price_sweeps_never_rewrite_physics_or_error_counts(self):
        for cell in (self.equal[("1","1")],self.equal[("1/2","1")]):
            self.assertEqual(len(cell["three_axis_fronts_by_price_contract"]),4)
            self.assertEqual(set(cell["instrumental_arms"]),set(ALL_ARMS))
            self.assertEqual(cell["two_axis_front_no_price"],
                             sorted(cell["two_axis_front_no_price"]))
            for profile in cell["three_axis_fronts_by_price_contract"].values():
                self.assertTrue(profile["cost_paid_for_qualified_but_rejected_evidence"])
                self.assertTrue(set(profile["three_axis_pareto_front"])<=set(FAIR_ARMS))
        a=self.equal[("1","1")]
        cheap=a["three_axis_fronts_by_price_contract"]["SOURCE_CHEAP_ORIGINAL"]
        expensive=a["three_axis_fronts_by_price_contract"]["SOURCE_EXPENSIVE_DIRECT_CHEAP"]
        self.assertIn("SOURCE_BOUNDARY_ONLY",cheap["three_axis_pareto_front"])
        self.assertNotIn("SOURCE_BOUNDARY_ONLY",expensive["three_axis_pareto_front"])

    def test_original_g04_absent_q_mislabel_is_corrected_by_comparator_identity(self):
        # Independent original experiment: two errors / 18 misses belong
        # to unqualified DOMAIN_FACTS_ONLY, not CONVENTIONAL_TARGETED.
        baseline=g04_manifest_run(G04)
        src=next(p for p in baseline["paired_regimes"]
                 if p["regime"]=="SOURCE_ABSENT_DIRECTED_AVAILABLE")
        b=src["policies"]["SOURCE_BOUNDARY_ONLY"]
        raw=src["policies"]["DOMAIN_FACTS_ONLY"]
        directed=src["policies"]["CONVENTIONAL_TARGETED"]
        self.assertEqual((b["unjustified_candidate_proposals"],
                          b["missed_feasible_candidates"]),(0,57))
        self.assertEqual((raw["unjustified_candidate_proposals"],
                          raw["missed_feasible_candidates"]),(2,18))
        self.assertEqual((directed["unjustified_candidate_proposals"],
                          directed["missed_feasible_candidates"]),(0,11))


if __name__=="__main__":
    unittest.main()
