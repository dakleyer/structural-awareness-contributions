"""Independent contract/anti-shortcut regression tests for UC21-DDS bridge.

Fixtures are synthetic; these tests check instrument semantics, not vendor safety.
"""
from __future__ import annotations

import json
import math
import sys
import unittest
from copy import deepcopy
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from uc21_dds_bridge import (assess, ContractError, SCENARIOS, SOURCE_ROUTES,
                              gate_assessment, sha256_canonical, social_metrics,
                              validate_packet, main)


def run(case="S4", route="R0", verdict="FAIL", effect="FAILURE_OCCURRED", id="r0", stage="A", mode="SYNTHETIC"):
    gates = {"Q"+str(i): "PASS" for i in range(SCENARIOS[case]["gates"])}
    if verdict == "FAIL":
        gates["Q2"] = "FAIL"
    obj = {"id": id, "scenario": case, "route": route,
           "dds_stage": stage, "evidence_mode": mode,
           "executed_at": {"r0":"2026-10-25T14:10:00+01:00", "r1":"2026-10-25T14:20:00+01:00", "r2":"2026-10-25T14:30:00+01:00"}.get(id,"2026-10-25T14:40:00+01:00"),
           "implementation": {"product": "Synthetic peer", "version": "1.0",
                              "config_hash": "pinned-config-123", "safeguards_hash": "pinned-safeguards-321",
                              "adaptation_enabled": True},
           "fixture": {"id": "fixed-scope-a", "version": "v1", "source_snapshot_ref": "snapshot-v1",
                       "oracle_reference": "private-oracle-v1", "oracle_visible_to_defender": False},
           "resources": {"compute_units": 100, "human_review_hours": 2, "deadline_seconds": 300},
           "gates": gates, "controls": {"legitimate_activity": "PASS", "matched_resources": "PASS", "control_trace_ref":"positive-control-fixture"},
           "result": {"source_verdict": verdict, "observed_effect": effect,
                      "deadline_met": True, "authorized_response": True,
                      "observed_effect_ref": "simulated-effect-log", "effect_evidence_sha256": "a"*64,
                      "effect_observer": "fixture assessor"},
           "evidence_status": {"instrument_qualified": True, "source_findings_preserved": True,
                               "native_execution_verified": False, "independent_effect_verified": False,
                               "qualification_ref": "fixture-selftest-not-native"},
           "trace_ref": "synthetic-trace-ref", "costs": {"compute": 10.0, "review": 2.0},
           "impact": {"affected_people": 4000, "unjustified_actions": 1}}
    if route == "R2":
        obj["baseline_r1_id"] = "r1"
        obj["context_change"] = {"change_id": "delta-01", "domain_hash": "2"*64,
                                  "preregistered": True, "within_frozen_domain": True,
                                  "materiality_independent_of_outcome": True,
                                  "credible_reviewed": True,
                                  "observable_in_admitted_scope": True,
                                  "feasible_authorized_response": True,
                                  "intervention_precedes_reliance": True,
                                  "defences_retained": True,
                                  "ordinary_adaptation_retained": True}
    return obj


def packet(*runs):
    return {"schema_version": "0.1",
            "registration": {"id": "pre-2026-10-25", "frozen_at": "2026-10-25T14:00+01:00",
                             "uc21_source_ref": "UC21@frozen-snapshot", "uc21_claim": "HR",
                             "source_case_sha256": "1"*64, "dds_method_ref": "DDS-index-v0.1",
                             "registered_before_runs": True,
                             "admitted_change_domains": {"S4": "2"*64}},
            "runs": list(runs)}


def example():
    return packet(run(id="r0"), run(route="R1", verdict="PASS", effect="FAILURE_AVOIDED", id="r1"),
                  run(route="R2", verdict="PASS", effect="FAILURE_AVOIDED", id="r2"))


class RegisteredProtocol(unittest.TestCase):
    def test_valid_packet(self):
        self.assertEqual(len(validate_packet(example())["runs"]), 3)

    def test_version_guard(self):
        p=example(); p["schema_version"]="0.2"
        with self.assertRaises(ContractError): assess(p)

    def test_ref_in_registration(self):
        p=example(); p["registration"]["source_case_sha256"]="not-sha"
        with self.assertRaises(ContractError): assess(p)

    def test_no_post_hoc_registration(self):
        p=example(); p["registration"]["registered_before_runs"]=False
        with self.assertRaises(ContractError): assess(p)

    def test_unknown_claim(self):
        p=example(); p["registration"]["uc21_claim"]="HR_PLUS_WELFARE"
        with self.assertRaises(ContractError): assess(p)

    def test_duplicate_id(self):
        p=example(); p["runs"][1]["id"]="r0"
        with self.assertRaises(ContractError): assess(p)

    def test_oracle_leak(self):
        p=example(); p["runs"][0]["fixture"]["oracle_visible_to_defender"]=True
        with self.assertRaises(ContractError): assess(p)

    def test_no_uncontrolled_na(self):
        p=example(); p["runs"][0]["gates"]["Q2"]="NOT_APPLICABLE"
        with self.assertRaises(ContractError): assess(p)

    def test_gate_must_be_present(self):
        p=example(); del p["runs"][0]["gates"]["Q0"]
        with self.assertRaises(ContractError): assess(p)

    def test_gate_no_excess(self):
        p=example(); p["runs"][0]["gates"]["Q9"]="PASS"
        with self.assertRaises(ContractError): assess(p)

    def test_stage_c_requires_native(self):
        p=example(); p["runs"][0]["dds_stage"]="C"
        with self.assertRaises(ContractError): assess(p)

    def test_native_cannot_silently_be_missing_effect(self):
        p=example(); r=p["runs"][0]; r["dds_stage"]="C"; r["evidence_mode"]="INSTRUMENTED_NATIVE"
        r["result"]["observed_effect"]="NOT_OBSERVED"
        with self.assertRaises(ContractError): assess(p)

    def test_native_flag_only_native(self):
        p=example(); p["runs"][0]["evidence_status"]["native_execution_verified"]=True
        with self.assertRaises(ContractError): assess(p)

    def test_independent_effect_requires_native(self):
        p=example(); p["runs"][0]["evidence_status"]["independent_effect_verified"]=True
        with self.assertRaises(ContractError): assess(p)

    def test_negative_harm_invalid(self):
        p=example(); p["runs"][0]["impact"]["affected_people"]=-1
        with self.assertRaises(ContractError): assess(p)

    def test_non_numeric_budget(self):
        p=example(); p["runs"][0]["resources"]["compute_units"]="unlimited"
        with self.assertRaises(ContractError): assess(p)

    def test_na_costs_cannot_be_negative(self):
        p=example(); p["runs"][0]["costs"]["coordination"]=-0.1
        with self.assertRaises(ContractError): assess(p)

    def test_unregistered_harm_dimension(self):
        p=example(); p["runs"][0]["impact"]["happiness_proven"] = 42
        with self.assertRaises(ContractError): assess(p)

    def test_missing_qualification_ref(self):
        p=example(); p["runs"][0]["evidence_status"]["qualification_ref"]=""
        with self.assertRaises(ContractError): assess(p)

    def test_stable_hash(self):
        self.assertEqual(sha256_canonical({"a":1,"b":2}), sha256_canonical({"b":2,"a":1}))

    def test_wrong_context_domain_rejected(self):
        p=example(); p["runs"][2]["context_change"]["domain_hash"]="3"*64
        with self.assertRaises(ContractError): assess(p)

    def test_run_before_registration_rejected(self):
        p=example(); p["runs"][0]["executed_at"]="2026-10-25T13:59:59+01:00"
        with self.assertRaises(ContractError): assess(p)

    def test_non_offset_timestamp_rejected(self):
        p=example(); p["runs"][0]["executed_at"]="2026-10-25T18:00:00"
        with self.assertRaises(ContractError): assess(p)

    def test_missing_effect_hash_rejected(self):
        p=example(); p["runs"][0]["result"]["effect_evidence_sha256"]=""
        with self.assertRaises(ContractError): assess(p)

    def test_source_labels_not_dds(self):
        self.assertIn("top-notch", SOURCE_ROUTES["R1"])
        self.assertIn("R3", SOURCE_ROUTES["R2"])


class CaseAndFalsifiability(unittest.TestCase):
    def test_six_scenario_gate_counts(self):
        for key in SCENARIOS:
            with self.subTest(key=key):
                self.assertEqual(len(assess(packet(run(case=key)))["case_results"]), 1)

    def test_s5_seven_gates(self):
        self.assertEqual(SCENARIOS["S5"]["gates"],7)

    def test_never_call_synthetic_empirical(self):
        r=assess(example())
        self.assertEqual(r["selected_intervention_prediction"],"SYNTHETIC_DEFENCE_NOT_EMPIRICAL_FALSIFICATION")

    def test_hr_not_proved_by_synthetic(self):
        self.assertEqual(assess(example())["uc21_hr_existential_six_case_conclusion"],
                         "NOT_REFUTED_OR_PROVED_BY_NONEXHAUSTIVE_RUNS")

    def test_r1_postdates_r2_invalid(self):
        p=example(); p["runs"][1]["executed_at"]="2026-10-25T15:00:00+01:00"
        self.assertIn("R1_NOT_EXECUTED_BEFORE_R2",assess(p)["case_results"][2]["admission_reasons"])

    def test_r2_missing_baseline(self):
        p=packet(run(route="R2",verdict="PASS",effect="FAILURE_AVOIDED",id="r2"))
        r=assess(p)["case_results"][0]
        self.assertEqual(r["implementation_result"],"NOT_ADMITTED")

    def test_r2_baseline_fail(self):
        p=packet(run(route="R1",id="r1"),run(route="R2",verdict="PASS",effect="FAILURE_AVOIDED",id="r2"))
        r=assess(p)["case_results"][1]
        self.assertIn("R1_BASELINE_NOT_CORRECTED", r["admission_reasons"])

    def test_r2_preserves_product(self):
        p=example(); p["runs"][2]["implementation"]["product"]="another"
        self.assertFalse(assess(p)["case_results"][2]["admitted"])

    def test_r2_preserves_safeguards(self):
        p=example(); p["runs"][2]["implementation"]["safeguards_hash"]="lowered"
        self.assertFalse(assess(p)["case_results"][2]["admitted"])

    def test_r2_preserves_adaptation(self):
        p=example(); p["runs"][2]["implementation"]["adaptation_enabled"]=False
        self.assertFalse(assess(p)["case_results"][2]["admitted"])

    def test_r2_matched_budget(self):
        p=example(); p["runs"][2]["resources"]["compute_units"]+=1
        self.assertFalse(assess(p)["case_results"][2]["admitted"])

    def test_r2_same_scenario(self):
        p=example(); p["registration"]["admitted_change_domains"]["S1"]="2"*64
        p["runs"][2]["scenario"]="S1"
        self.assertFalse(assess(p)["case_results"][2]["admitted"])

    def test_r2_same_decision_fixture(self):
        p=example(); p["runs"][2]["fixture"]["id"]="replacement-problem"
        self.assertFalse(assess(p)["case_results"][2]["admitted"])

    def test_r2_not_credible(self):
        p=example(); p["runs"][2]["context_change"]["credible_reviewed"]=False
        self.assertEqual(assess(p)["case_results"][2]["implementation_result"],"NOT_ADMITTED")

    def test_r2_unobservable_not_admitted(self):
        p=example(); p["runs"][2]["context_change"]["observable_in_admitted_scope"]=False
        self.assertFalse(assess(p)["case_results"][2]["admitted"])

    def test_r2_adaptation_not_retained(self):
        p=example(); p["runs"][2]["context_change"]["ordinary_adaptation_retained"]=False
        self.assertFalse(assess(p)["case_results"][2]["admitted"])

    def test_r2_no_authorized_feasible_response(self):
        p=example(); p["runs"][2]["context_change"]["feasible_authorized_response"]=False
        self.assertFalse(assess(p)["case_results"][2]["admitted"])

    def test_r2_post_hoc_change_disallowed(self):
        p=example(); p["runs"][2]["context_change"]["preregistered"]=False
        self.assertFalse(assess(p)["case_results"][2]["admitted"])

    def test_pass_with_failure_is_inconsistent(self):
        r=run(route="R1",verdict="PASS",effect="FAILURE_OCCURRED",id="r1")
        self.assertTrue(gate_assessment(r)["source_consistency_alert"])

    def test_gate_fail_not_averaged_away(self):
        r=run(route="R1",verdict="PASS",effect="FAILURE_AVOIDED",id="r1")
        r["gates"]["Q5"]="FAIL"
        self.assertFalse(gate_assessment(r)["admitted_branch_defence"])

    def test_deny_all_does_not_pass(self):
        r=run(route="R1",verdict="PASS",effect="FAILURE_AVOIDED",id="r1")
        r["controls"]["legitimate_activity"]="FAIL"
        self.assertFalse(gate_assessment(r)["admitted_branch_defence"])

    def test_no_deadline_pass(self):
        r=run(route="R1",verdict="PASS",effect="FAILURE_AVOIDED",id="r1")
        r["result"]["deadline_met"]=False
        self.assertFalse(gate_assessment(r)["admitted_branch_defence"])

    def test_no_authority_pass(self):
        r=run(route="R1",verdict="PASS",effect="FAILURE_AVOIDED",id="r1")
        r["result"]["authorized_response"]=False
        self.assertFalse(gate_assessment(r)["admitted_branch_defence"])

    def test_all_gates_pass_r1(self):
        self.assertTrue(assess(example())["case_results"][1]["admitted_branch_defence"])

    def test_case_gates_do_not_become_hid(self):
        self.assertEqual(assess(example())["social_observations"], [])

    def test_impact_vector_not_auto_happiness(self):
        r=assess(example())["case_results"][0]
        self.assertNotIn("suffering", r)
        self.assertEqual(r["impact_vector_observed_not_welfare"]["affected_people"],4000)

    def test_documentary_native_flag_not_empirical(self):
        p=example(); p["runs"][2]["evidence_mode"]="INSTRUMENTED_NATIVE";
        p["runs"][2]["dds_stage"]="C"
        self.assertEqual(assess(p)["selected_intervention_prediction"],
                         "SYNTHETIC_DEFENCE_NOT_EMPIRICAL_FALSIFICATION")

    def test_verified_native_r1_r2_counterexample(self):
        p=example()
        for i in (1,2):
            r=p["runs"][i]; r["evidence_mode"]="INSTRUMENTED_NATIVE"; r["dds_stage"]="C"
            r["evidence_status"]["native_execution_verified"]=True
            r["evidence_status"]["independent_effect_verified"]=True
        self.assertEqual(assess(p)["selected_intervention_prediction"],
                         "BOUNDED_EMPIRICAL_COUNTEREXAMPLE_TO_SELECTED_FAILURE_PREDICTION")

    def test_native_failure_supports_only_specific_prediction(self):
        p=example()
        for i in (1,2):
            r=p["runs"][i]; r["evidence_mode"]="INSTRUMENTED_NATIVE"; r["dds_stage"]="C"
            r["evidence_status"]["native_execution_verified"]=True
            r["evidence_status"]["independent_effect_verified"]=True
        r=p["runs"][2]; r["result"]["source_verdict"]="FAIL"
        r["result"]["observed_effect"]="FAILURE_OCCURRED"; r["gates"]["Q2"]="FAIL"
        self.assertEqual(assess(p)["selected_intervention_prediction"],
                         "BOUNDED_EMPIRICAL_SUPPORT_FOR_SELECTED_FAILURE_PREDICTION")

    def test_finite_runs_not_refute_existential_all_six(self):
        p=example()
        for i in (1,2):
            r=p["runs"][i];r["evidence_mode"]="INSTRUMENTED_NATIVE";r["dds_stage"]="C"
            r["evidence_status"]["native_execution_verified"]=True
            r["evidence_status"]["independent_effect_verified"]=True
        self.assertEqual(assess(p)["uc21_hr_existential_six_case_conclusion"],
                         "NOT_REFUTED_OR_PROVED_BY_NONEXHAUSTIVE_RUNS")


class HIDAndEconomics(unittest.TestCase):
    def observation(self,t,acw,prod,validated=True):
        return {"run_id":"r1", "t":t,"production":prod,"gic_hours":10,"neo_hours":5,
                "acw_hours":acw,"unknown_hours":0,"human_capacity_hours":100,
                "classification_validated":validated,"same_service_counterfactual":True,
                "counterfactual_ref":"independent-same-service-witness", "releasable_acw_hours":acw/2}

    def test_hid_ratio_not_hour_count(self):
        o=social_metrics([self.observation(1,5,100)])[0]["rows"][0]
        self.assertAlmostEqual(o["HID_observed"],5/20)
        self.assertAlmostEqual(o["HID_potential"],2.5/20)

    def test_uncalibrated_classes_do_not_count(self):
        o=social_metrics([self.observation(1,5,100,False)])[0]["rows"][0]
        self.assertIsNone(o["HID_observed"])
        self.assertIsNone(o["HID_potential"])

    def test_curvature_with_production_growth(self):
        a=social_metrics([self.observation(1,1,100),self.observation(2,4,140),
                          self.observation(3,9,200)])[0]
        self.assertEqual(a["second_order"][0]["delta2_H_ACW"],2)
        self.assertEqual(a["rows"][-1]["production"],200)

    def test_curvature_normalizes_spacing(self):
        a=social_metrics([self.observation(2,1,100),self.observation(4,4,140),
                          self.observation(6,9,200)])[0]
        self.assertEqual(a["second_order"][0]["delta2_H_ACW"],0.5)

    def test_unequal_spacing_requires_estimator(self):
        a=social_metrics([self.observation(1,1,100),self.observation(2,4,140),
                          self.observation(4,9,200)])[0]
        self.assertIsNone(a["second_order"][0]["delta2_H_ACW"])

    def test_distinct_dates(self):
        with self.assertRaises(ContractError):
            social_metrics([self.observation(1,1,100), self.observation(1,2,120)])

    def test_protect_counterfactual_bounds(self):
        x=self.observation(1,5,100);x["releasable_acw_hours"]=6
        with self.assertRaises(ContractError): social_metrics([x])

    def test_no_witness_no_potential(self):
        x=self.observation(1,5,100);x["same_service_counterfactual"]=False
        row=social_metrics([x])[0]["rows"][0]
        self.assertIsNone(row["HID_potential"])

    def test_human_capacity_overflow_is_reported(self):
        x=self.observation(1,90,100)
        self.assertTrue(social_metrics([x])[0]["rows"][0]["human_capacity_exceeded"])

    def test_no_auto_causal_claim(self):
        x=[self.observation(t,t*t,100+t) for t in (1,2,3)]
        self.assertIn("NO_CAUSAL_ATTRIBUTION",social_metrics(x)[0]["second_order"][0]["reason"])

    def test_social_observation_in_packet(self):
        p=example();p["social_observations"]=[self.observation(1,1,100)]
        self.assertEqual(assess(p)["social_observations"][0]["rows"][0]["H_ACW"],1)

    def test_orphan_social_record(self):
        p=example();o=self.observation(1,1,100);o["run_id"]="unknown";p["social_observations"]=[o]
        with self.assertRaises(ContractError): assess(p)

    def test_no_zero_total_hid_division(self):
        x=self.observation(1,0,100); x["gic_hours"]=0; x["neo_hours"]=0
        self.assertIsNone(social_metrics([x])[0]["rows"][0]["HID_observed"])

    def test_no_result_data_is_made_up(self):
        p=example();self.assertIsNone(assess(p)["economic_projection"])

    def test_projection_not_source_oracle(self):
        p=example();p["economic_projection"]={"purpose":"SOURCE_UC21_VERDICT","config":{"mode":"formulas"}}
        with self.assertRaises(ContractError): assess(p)


if __name__ == "__main__": unittest.main()
