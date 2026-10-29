"""Acceptance tests: original examples, dimension activation, native social+agentic replay."""
import copy
import json
import unittest
from pathlib import Path

from dimension_experiment import (
    DEFAULT_OPERATORS, ExperimentError, PhysicalOutcome, conditional_information,
    run_case, run_manifest, number, public_view,
)
from native_experiment_adapters import native_operators
from run_original_experiments import run

HERE = Path(__file__).resolve().parent


class OriginalSocialExamples(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads((HERE / "ORIGINAL_EXPERIMENTS.json").read_text(encoding="utf-8"))
        cls.results = run_manifest(cls.manifest)
        cls.by_id = {x["case_id"]: x for x in cls.results["cases"]}

    def item(self, name):
        return self.by_id[name]

    def test_all_declared_examples_really_execute(self):
        self.assertEqual(len(self.by_id), 40)
        self.assertEqual(self.results["case_count"], len(self.manifest["cases"]))
        self.assertFalse(self.results["cross_model_objectives_aggregated"])
        self.assertTrue(all(len(x["case_sha256"]) == 64 for x in self.by_id.values()))
        self.assertTrue(all(x["source_refs"] and not x["is_empirical_observation"] for x in self.by_id.values()))

    def test_two_bananas_original_s0_s1_s2_and_toy_B_F(self):
        s0=self.item("BANANA-S0")["physical_outcome"]
        s1=self.item("BANANA-S1")["physical_outcome"]
        s2=self.item("BANANA-S2-ADMITTED-SYNTHETIC")["physical_outcome"]
        self.assertEqual((s0["available"],s0["allocated"],s0["wasted"]),(0,0,0))
        self.assertEqual((s1["available"],s1["received"]["holder"],s1["wasted"]),(2,1,1))
        self.assertEqual((s2["available"],s2["received"]["holder"],s2["received"]["child"],s2["wasted"]),(2,1,1,0))
        self.assertEqual(s1["hypothetical_welfare"]["holder"],{"B":5,"F":7,"W":-2})
        self.assertEqual(s2["hypothetical_welfare"]["holder"],{"B":5,"F":0,"W":5})
        self.assertEqual(self.item("BANANA-S2-UNVERIFIED")["admission"],"UNDETERMINED")
        self.assertEqual(self.item("BANANA-S2-ROUTE-BLOCKED")["admission"],"BLOCKED_BY_CONDITION")
        self.assertEqual(self.item("BANANA-OVERALLOCATION")["admission"],"MATERIALLY_INFEASIBLE")

    def test_implicit_dimensions_activate_on_actual_computed_transition(self):
        self.assertEqual(self.item("BANANA-S0")["dimension_states"]["distribution"]["at_decision"],"IMPLICIT")
        self.assertEqual(self.item("BANANA-S1")["dimension_states"]["distribution"]["at_decision"],"ACTIVE")
        self.assertEqual(self.item("BANANA-S2-UNVERIFIED")["dimension_states"]["coordination"]["at_decision"],"ACTIVE")
        self.assertEqual(self.item("DONATION-ATTRIBUTION-VETO")["dimension_states"]["attribution"]["at_decision"],"ACTIVE")

    def test_banana_transport_not_fake_money_savings(self):
        remote = self.item("BANANA-EXTRA-TRANSPORT")
        local = self.item("BANANA-LOCAL-ASSUMED")
        self.assertEqual(remote["admission"],"UNDETERMINED")
        self.assertEqual(self.item("BANANA-LOCAL-UNVERIFIED")["admission"],"UNDETERMINED")
        self.assertEqual(local["admission"],"ELIGIBLE_UNDER_DECLARED_CONDITIONS")
        self.assertIsNone(local["physical_outcome"]["carbon_savings"])
        self.assertIsNone(local["physical_outcome"]["money_savings"])
        self.assertGreater(local["physical_outcome"]["avoided_item_km"],0)

    def test_donation_positive_direct_benefit_can_still_be_vetoed(self):
        veto=self.item("DONATION-ATTRIBUTION-VETO")
        self.assertEqual(veto["physical_outcome"]["hypothetical_welfare"]["donor"]["B"],5)
        self.assertEqual(veto["physical_outcome"]["hypothetical_welfare"]["donor"]["W"],5)
        self.assertEqual(veto["admission"],"BLOCKED_BY_CONDITION")
        self.assertIn("attribution_acceptance",veto["blocking_conditions"])
        self.assertEqual(self.item("DONATION-CONSENT-ABSENT")["admission"],"BLOCKED_BY_CONDITION")
        self.assertEqual(self.item("DONATION-ROUTE-UNCERTAIN")["admission"],"UNDETERMINED")
        self.assertEqual(self.item("DONATION-ACCEPTED-ALTERNATE-CREDIT")["admission"],"ELIGIBLE_UNDER_DECLARED_CONDITIONS")

    def test_credits_and_friday_not_reduced_to_total_cost(self):
        self.assertEqual(self.item("CREDIT-7-4")["admission"],"MATERIALLY_INFEASIBLE")
        self.assertEqual(self.item("CREDIT-7-3")["admission"],"ELIGIBLE_UNDER_DECLARED_CONDITIONS")
        veto=self.item("FRIDAY-RELATIVE-VETO")
        self.assertTrue(veto["physical_outcome"]["each_actor_positive_absolute_gain"])
        self.assertEqual(veto["physical_outcome"]["relative_shares"]["Friday"]["coconut"],"1/1000")
        self.assertEqual(veto["admission"],"BLOCKED_BY_CONDITION")
        self.assertEqual(self.item("FRIDAY-RELATIVE-ACCEPTED")["admission"],"ELIGIBLE_UNDER_DECLARED_CONDITIONS")

    def test_apples_local_peak_not_conflated_with_global_reachable(self):
        case=self.item("APPLES-BRIDGE-UNKNOWN")
        self.assertEqual(case["physical_outcome"]["local_choice"],3)
        self.assertEqual(case["physical_outcome"]["global_best"],8)
        self.assertEqual(case["admission"],"UNDETERMINED")
        self.assertTrue(case["physical_outcome"]["global_not_automatically_accessible"])
        self.assertEqual(self.item("APPLES-BRIDGE-DENIED")["admission"],"BLOCKED_BY_CONDITION")

    def test_entropy_computed_from_finite_worlds_and_control(self):
        ab=self.item("FINITE-A-B")["physical_outcome"]["computed_information_bits"]
        xor=self.item("FINITE-XOR-INDEPENDENT")["physical_outcome"]["computed_information_bits"]
        dependent=self.item("FINITE-XOR-DEPENDENT")["physical_outcome"]["computed_information_bits"]
        self.assertEqual((ab["H_R_given_A"],ab["H_R_given_AB"],ab["I_R_B_given_A"]),(1,0,1))
        self.assertEqual((xor["I_R_Q1"],xor["I_R_Q2"],xor["I_R_Q1Q2"]),(0,0,1))
        self.assertEqual((dependent["I_R_Q1"],dependent["I_R_Q2"],dependent["I_R_Q1Q2"]),(0,0,0))
        self.assertIsNone(self.item("FINITE-A-B")["physical_outcome"]["open_CD_distribution"])
        self.assertEqual(conditional_information([{"a":0,"r":0},{"a":1,"r":1}],"r",["a"]),1.0)

    def test_efficiency_gap_requires_same_service_not_better_looking_apps(self):
        iq=self.item("IQ03-GAP-GROWS")["physical_outcome"]
        self.assertTrue(iq["efficiency_gap_increased"])
        self.assertEqual([p["resource_gap"] for p in iq["periods"]],[20,45])
        self.assertEqual(self.item("IQ03-SERVICE-NOT-EQUIVALENT")["admission"],"BLOCKED_BY_CONDITION")
        self.assertFalse(self.item("IQ03-GAP-NOT-GROWING")["physical_outcome"]["efficiency_gap_increased"])
        self.assertEqual(self.item("MINISTRIES-700-TO-2-UNVERIFIED")["admission"],"UNDETERMINED")
        self.assertEqual(self.item("MINISTRIES-700-TO-2-SYNTHETIC")["admission"],"ELIGIBLE_UNDER_DECLARED_CONDITIONS")
        self.assertEqual(self.item("MINISTRIES-BROKEN-SERVICE")["admission"],"BLOCKED_BY_CONDITION")

    def test_oranges_education_craft_lycee_preserve_unknowns(self):
        self.assertEqual(self.item("ORANGES-WITHOUT-QUANTITY")["admission"],"UNDETERMINED")
        self.assertEqual(self.item("ORANGES-SIMULATED-RECOVERY")["admission"],"ELIGIBLE_UNDER_DECLARED_CONDITIONS")
        self.assertEqual(self.item("ORANGES-UNSAFE")["admission"],"BLOCKED_BY_CONDITION")
        self.assertEqual(self.item("EDUCATION-ALGEBRA-ONLY")["admission"],"UNDETERMINED")
        self.assertEqual(self.item("EDUCATION-ASSUMED-SEATS")["admission"],"ELIGIBLE_UNDER_DECLARED_CONDITIONS")
        self.assertEqual(self.item("CRAFT-ARTIFACTS-ONLY")["admission"],"UNDETERMINED")
        self.assertEqual(self.item("CRAFT-WITH-PRACTICE")["physical_outcome"]["effective_transmission_capacity"],2)
        self.assertEqual(self.item("CRAFT-NO-TEACHER")["physical_outcome"]["effective_transmission_capacity"],0)
        self.assertEqual(self.item("LYCEE-GOAL-UNOBSERVED")["admission"],"UNDETERMINED")
        self.assertEqual(self.item("LYCEE-SYNTHETIC-ACCESS")["admission"],"ELIGIBLE_UNDER_DECLARED_CONDITIONS")
        self.assertEqual(self.item("REPEATED-SOURCE-NOT-INDEPENDENT")["physical_outcome"]["origins"],2)

    def test_persistent_replay_and_public_private_separation(self):
        manifest=copy.deepcopy(self.manifest)
        report=run_manifest(manifest)
        self.assertEqual(report,self.results)
        self.assertEqual(manifest,self.manifest)
        case=next(c for c in self.manifest["cases"] if c["case_id"]=="DONATION-ATTRIBUTION-VETO")
        pub=json.dumps(public_view(case),sort_keys=True)
        self.assertNotIn("declared_valuation",pub)
        self.assertNotIn("benefit_per_donated",pub)
        self.assertNotIn("allocations",pub)

    def test_different_real_input_changes_actual_computed_outcome(self):
        c=copy.deepcopy(next(c for c in self.manifest["cases"] if c["case_id"]=="BANANA-S1"))
        before=run_case(c)
        c["inputs"]["available"]=3
        after=run_case(c)
        self.assertEqual(after["physical_outcome"]["wasted"],2)
        self.assertEqual(after["physical_outcome"]["hypothetical_welfare"]["holder"]["W"],-9)
        self.assertNotEqual(before["case_sha256"],after["case_sha256"])
        self.assertEqual(after["admission"],"ELIGIBLE_UNDER_DECLARED_CONDITIONS")

    def test_third_party_operator_and_contract(self):
        c=copy.deepcopy(self.manifest["cases"][0])
        c["operator"]="third_party_supply"
        def third_party(params):
            return PhysicalOutcome("POSSIBLE",{"conserved": True,"available":params["available"]})
        result=run_case(c,operators={"third_party_supply":third_party})
        self.assertEqual(result["physical_outcome"]["available"],0)
        with self.assertRaises(ExperimentError):
            run_case(c,operators={"material_flow":third_party})
        with self.assertRaises(ExperimentError):
            run_case(c,operators={"third_party_supply": lambda _: {"status":"POSSIBLE"}})
        with self.assertRaises(ExperimentError):
            number(True)

    def test_negative_control_fake_activation_and_material_veto(self):
        c=copy.deepcopy(self.manifest["cases"][0])
        c["constraints"].append({"id":"forced_right","category":"rights","satisfied":False,"owner":"participant"})
        out=run_case(c)
        self.assertEqual(out["admission"],"BLOCKED_BY_CONDITION")
        self.assertNotIn("forced_right",out["physical_outcome"])


class OriginalNativeModels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=run("both")
        cls.by_id={r["case_id"]:r for r in cls.report["cases"]}

    def test_both_source_models_ran_with_finite_examples(self):
        self.assertEqual(self.report["case_count"],73)
        self.assertEqual(set(self.report["admission_by_model"]),
                         {"SOCIAL_FINITE","SOCIAL_SOURCE_44","AGENTIC_SOURCE_57"})
        self.assertEqual(sum(1 for x in self.by_id.values() if x["model"]=="AGENTIC_SOURCE_57"),30)
        self.assertFalse(self.report["cross_model_objectives_aggregated"])

    def test_intrinsic_native_same_A_private_different_marginal(self):
        free=self.by_id["SOCIAL44-CURRENT-SLACK-16"]["physical_outcome"]
        clipped=self.by_id["SOCIAL44-SAME-A-ROOT-BOTTLENECK"]["physical_outcome"]
        self.assertEqual(free["public_current_A"],clipped["public_current_A"])
        self.assertEqual(free["private_referee_true_increment"],2)
        self.assertEqual(clipped["private_referee_true_increment"],0)
        self.assertEqual(free["native_arms"]["B_QUALIFIED"]["promised_increment"],2)
        self.assertEqual(clipped["native_arms"]["B_QUALIFIED"]["promised_increment"],0)
        self.assertFalse(free["C_D_residual_closed"])

    def test_agentic_native_same_public_A_different_private_worlds(self):
        high=self.by_id["AGENTIC57-AG01-QUALIFIED-NEAR-OPTIMUM"]["physical_outcome"]
        low=self.by_id["AGENTIC57-AG02-LOW-CAPABILITY-SAME-A"]["physical_outcome"]
        self.assertEqual(high["public_current_A_output"],low["public_current_A_output"])
        self.assertEqual(high["public_total_resources"],low["public_total_resources"])
        self.assertGreater(high["source_synthetic_arms"]["A_ONLY"]["private_referee_only"]["technical_optimum"],
                           low["source_synthetic_arms"]["A_ONLY"]["private_referee_only"]["technical_optimum"])
        self.assertEqual(len(high["source_synthetic_arms"]),6)
        self.assertTrue(high["private_truth_not_a_public_planner_input"])

    def test_agentic_consent_authority_and_material_D_act_on_native_plans(self):
        for case in ("AG07-DONOR-REFUSES","AG08-META-OWNER-LACKS-AUTHORITY",
                     "AG09-MATERIAL-D-UNRESOLVED"):
            out=self.by_id["AGENTIC57-"+case]["physical_outcome"]
            self.assertEqual(out["source_synthetic_arms"]["Q_META_PROTOCOL"]["public_plan"]["transfer"],0)

    def test_cli_model_selectors_no_crossmodel_utility(self):
        self.assertEqual(run("social")["case_count"],40)
        self.assertEqual(run("native-social")["case_count"],3)
        self.assertEqual(run("agentic")["case_count"],30)
        self.assertEqual(run("native-agentic")["case_count"],30)



class L07EvidenceOriginAccounting(unittest.TestCase):
    def test_declared_gates_are_not_reported_as_calculated_results(self):
        report = run("social")
        basis = report["social_constraint_evidence_origin"]
        self.assertEqual(basis["source_owned_social_cases"], 40)
        self.assertEqual(basis["declared_conditions"], 74)
        self.assertEqual(basis["calculated_conditions"], 26)
        self.assertEqual(basis["declared_conditions"]+basis["calculated_conditions"], 100)
        self.assertEqual(basis["eligible_conditional"], 18)
        self.assertEqual(basis["non_eligible"], 22)
        self.assertEqual(sum(basis["primary_noneligible_basis"].values()),22)
        self.assertEqual(len(basis["details"]),40)
        self.assertIn("NOT A CAUSAL EXPLANATION",basis["basis_warning"])

    def test_computed_overallocation_vs_declared_attribution_are_separate(self):
        report = run("social")
        rows = {row["case_id"]:row for row in
                report["social_constraint_evidence_origin"]["details"]}
        self.assertEqual(rows["CREDIT-7-4"]["primary_basis"],
                         "COMPUTED_PHYSICAL_IMPOSSIBILITY")
        self.assertEqual(rows["DONATION-ATTRIBUTION-VETO"]["primary_basis"],
                         "SOURCE_DECLARED_FAILURE")
        self.assertEqual(rows["BANANA-S2-UNVERIFIED"]["primary_basis"],
                         "SOURCE_DECLARED_UNKNOWN")
        self.assertEqual(rows["BANANA-S1"]["primary_basis"],
                         "ELIGIBLE_CONDITIONAL")
        self.assertTrue(any(
            c["origin"]=="SOURCE_DECLARED_GATE"
            for c in rows["DONATION-ATTRIBUTION-VETO"]["unresolved_or_failed_conditions"]))
        self.assertTrue(all(not item["admission"]=="FIELD_VALIDATED"
                            for item in rows.values()))

    def test_evidence_accounting_does_not_consume_private_agentic_truth(self):
        social = run("social")["social_constraint_evidence_origin"]
        all_sources = run("both")["social_constraint_evidence_origin"]
        self.assertEqual(social,all_sources)


if __name__ == "__main__":
    unittest.main()
