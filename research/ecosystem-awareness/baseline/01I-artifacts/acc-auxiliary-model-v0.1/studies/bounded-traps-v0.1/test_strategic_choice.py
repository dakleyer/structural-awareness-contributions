"""H-01 regressions: strategic choice must not be a relabelled infeasible move."""
from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
from pathlib import Path
import json
import unittest

import bounded_traps as original
import strategic_choice as model


HERE=Path(__file__).resolve().parent
MANIFEST=json.loads((HERE/"H01_STRATEGIC_STUDY.json").read_text(encoding="utf-8"))
BASE=MANIFEST["base_game"]
REPORT=model.run_manifest(MANIFEST)
BY_ID={s["case_id"]:s for s in REPORT["scenarios"]}


def game(name:str)->dict:
    item=next(x for x in MANIFEST["scenarios"] if x["id"]==name)
    x=model.merge(BASE,item["patch"])
    x["id"]=name
    return x


class AuthorOriginalAndStrategicChoice(unittest.TestCase):
    def test_historical_feasibility_theorem_remains_exactly_original(self):
        old=original.coupled_trap()
        self.assertEqual(old["feasible"],[[0,0],[1,1]])
        self.assertTrue(old["pareto_dominates"])
        self.assertFalse(old["reachable_without_joint_transition"])
        self.assertEqual(old["utility_current"],[4.0,4.0])
        self.assertEqual(old["utility_target"],[5.0,5.0])
        self.assertEqual(REPORT["source_original_coupled_trap"]["feasible"],
                         old["feasible"])
        self.assertFalse(REPORT["source_original_coupled_trap"]
                         ["reachable_without_joint_transition"])

    def test_historical_example_is_not_falsely_called_rational_stag_hunt(self):
        h=BY_ID["H01_ORIGINAL_FEASIBILITY_REFERENCE"]
        self.assertEqual(h["finite_feasible_profiles"],[[0,0],[1,1]])
        self.assertEqual(h["mechanism"]["classification"],
                         "FEASIBILITY_PROTOCOL_TRAP_NOT_STRATEGIC_CHOICE")
        dev=h["mechanism"]["current_individual_deviation_proof"]
        self.assertEqual(dev["feasible_unilateral_deviations"],0)
        self.assertTrue(dev["nash_may_be_vacuous_if_moves_infeasible"])
        self.assertTrue(h["joint_coordination"]["technical_candidate_feasible"])
        self.assertEqual(h["joint_coordination"]["status"],
                         "ADMISSIBLE_UNDER_SYNTHETIC_ASSUMPTIONS")

    def test_strategic_example_all_four_states_are_technically_feasible(self):
        x=BY_ID["H01_STRICT_COORDINATION_TRAP"]
        self.assertEqual(x["finite_feasible_profiles"],
                         [[0,0],[0,1],[1,0],[1,1]])
        self.assertEqual(x["mechanism"]["classification"],
                         "STRICT_RATIONAL_COORDINATION_TRAP")
        self.assertEqual(x["mechanism"]["current_payoffs"],["3","3"])
        self.assertEqual(x["mechanism"]["target_payoffs"],["5","5"])
        self.assertTrue(x["mechanism"]["target_strictly_pareto_dominates_current"])
        self.assertEqual(x["mechanism"]["current_individual_deviation_proof"]
                         ["feasible_unilateral_deviations"],2)

    def test_payoff_matrix_is_calculated_by_declared_components(self):
        expected={(0,0):("3","3"),(0,1):("2","0"),
                  (1,0):("0","2"),(1,1):("5","5")}
        for state,values in expected.items():
            with self.subTest(state=state):
                self.assertTrue(model.feasible(state,BASE))
                self.assertEqual(tuple(map(model.fmt,model.payoff(state,BASE))),values)

    def test_both_nash_equilibria_and_individual_best_responses_found(self):
        x=BY_ID["H01_STRICT_COORDINATION_TRAP"]["mechanism"]
        eqs=x["all_pure_nash_equilibria"]
        self.assertEqual([s["profile"] for s in eqs],[[0,0],[1,1]])
        self.assertTrue(all(e["strict_all_deviations_feasible"] for e in eqs))
        deviations=x["current_individual_deviation_proof"]["individual_deviations"]
        self.assertEqual([d["personal_deviation_gain"] for d in deviations],
                         ["-3","-3"])
        self.assertEqual([d["best_responses"] for d in deviations],[[0],[0]])

    def test_no_unilateral_improvement_under_deterministic_best_response(self):
        x=BY_ID["H01_STRICT_COORDINATION_TRAP"]["mechanism"]["best_response_dynamics"]
        self.assertEqual(x["path"],[[0,0]])
        self.assertEqual(x["steps"],[])
        self.assertTrue(x["terminates_at_nash"])
        self.assertEqual(x["status"],"NO_PROFITABLE_UNILATERAL_MOVE")

    def test_explicit_beliefs_change_rational_action_at_threshold(self):
        for actor in (0,1):
            low=model.belief_best_response(BASE,"1/5",actor)
            boundary=model.belief_best_response(BASE,"1/2",actor)
            high=model.belief_best_response(BASE,"4/5",actor)
            self.assertEqual(low["rational_choices"],[0])
            self.assertEqual(boundary["rational_choices"],[0,1])
            self.assertEqual(high["rational_choices"],[1])
            self.assertEqual(low["expected_stay"],"14/5")
            self.assertEqual(low["expected_move"],"1")
        all_beliefs=BY_ID["H01_STRICT_COORDINATION_TRAP"]["belief_controls"]
        self.assertEqual(len(all_beliefs),2*len(BASE["belief_grid"]))

    def test_modifying_private_incentive_eliminates_inferior_nash(self):
        a=BY_ID["H01_PROFITABLE_UNILATERAL_ESCAPE"]["mechanism"]
        self.assertEqual(a["classification"],
                         "PROFITABLE_UNILATERAL_ESCAPE_NOT_A_NASH_TRAP")
        self.assertEqual(a["current_individual_deviation_proof"]
                         ["profitable_unilateral_deviations"],2)
        self.assertNotIn([0,0],[e["profile"] for e in a["all_pure_nash_equilibria"]])
        self.assertGreater(len(a["best_response_dynamics"]["steps"]),0)

    def test_tie_is_not_invented_as_strict_rational_refusal(self):
        x=BY_ID["H01_WEAK_BEST_RESPONSE_TIE"]["mechanism"]
        self.assertEqual(x["classification"],
                         "WEAK_NASH_NO_STRICT_UNILATERAL_GAIN")
        self.assertFalse(x["current_individual_deviation_proof"]
                         ["strict_equilibrium_with_all_deviations_available"])
        self.assertEqual([d["personal_deviation_gain"]
                          for d in x["current_individual_deviation_proof"]["individual_deviations"]],
                         ["0","0"])

    def test_no_joint_pareto_gain_is_an_accepted_negative_result(self):
        x=BY_ID["H01_NO_PARETO_JOINT_GAIN"]["mechanism"]
        self.assertEqual(x["classification"],
                         "NO_PARETO_SUPERIOR_TARGET_ON_ACTOR_UTILITIES")
        self.assertFalse(x["target_strictly_pareto_dominates_current"])

    def test_original_constraints_are_the_actual_cause_of_feasibility_trap(self):
        old=game("H01_ORIGINAL_FEASIBILITY_REFERENCE")
        self.assertFalse(model.feasible((1,0),old))
        self.assertFalse(model.feasible((0,1),old))
        self.assertEqual(tuple(map(model.fmt,model.payoff((1,1),old))),("5","5"))
        with self.assertRaisesRegex(ValueError,"infeasible"):
            model.payoff((1,0),old)


class GovernanceAndConventionalPeer(unittest.TestCase):
    def test_joint_switch_is_only_conditionally_admissible(self):
        x=BY_ID["H01_STRICT_COORDINATION_TRAP"]["joint_coordination"]
        self.assertEqual(x["status"],"ADMISSIBLE_UNDER_SYNTHETIC_ASSUMPTIONS")
        self.assertEqual(x["actor_payoffs_after_burden_and_zero_sum_transfers"],
                         ["4","4"])
        self.assertEqual(x["joint_resource_use_including_setup"],"4")
        self.assertEqual(x["resource_budget"],"10")
        self.assertTrue(x["explicit_consent_is_not_inferred_from_preferences"])
        self.assertTrue(x["counterfactual_admission_not_a_real_committed_action"])

    def test_costly_joint_switch_can_fail_despite_pareto_target(self):
        r=BY_ID["H01_TOO_EXPENSIVE_COORDINATION"]
        self.assertEqual(r["mechanism"]["classification"],
                         "STRICT_RATIONAL_COORDINATION_TRAP")
        self.assertEqual(r["joint_coordination"]["status"],
                         "VOLUNTARY_PARTICIPATION_NOT_SUPPORTED_BY_PAYOFFS")
        self.assertEqual(r["joint_coordination"]
                         ["actor_payoffs_after_burden_and_zero_sum_transfers"],["2","2"])

    def test_consent_and_authority_must_be_explicit_independent_gates(self):
        for key,status in (
            ("H01_NO_CONSENT","BLOCKED_BY_EXPLICIT_GOVERNANCE"),
            ("H01_UNKNOWN_AUTHORITY","GOVERNANCE_UNKNOWN_CANNOT_COMMIT"),
            ("H01_NO_JOINT_PROTOCOL","BLOCKED_BY_EXPLICIT_GOVERNANCE"),
            ("H01_UNKNOWN_CONSENT","GOVERNANCE_UNKNOWN_CANNOT_COMMIT"),
        ):
            with self.subTest(case=key):
                c=BY_ID[key]["joint_coordination"]
                self.assertEqual(c["status"],status)
                self.assertTrue(c["technical_candidate_feasible"])
                self.assertEqual(c["actor_payoffs_after_burden_and_zero_sum_transfers"],
                                 ["4","4"])

    def test_resource_budget_is_distinct_from_net_private_utility(self):
        a=BY_ID["H01_INSUFFICIENT_TRANSITION_BUDGET"]
        self.assertTrue(a["joint_coordination"]["technical_candidate_feasible"])
        self.assertEqual(a["joint_coordination"]["status"],
                         "MATERIALLY_INFEASIBLE_OR_RESOURCE_OVERDRAFT")
        self.assertEqual(a["joint_coordination"]["joint_resource_use_including_setup"],"4")
        b=BY_ID["H01_TECHNICAL_TARGET_INFEASIBLE"]
        self.assertFalse(b["mechanism"]["target_feasible"])
        self.assertEqual(b["mechanism"]["classification"],
                         "NO_TECHNICALLY_FEASIBLE_TARGET")
        self.assertFalse(b["joint_coordination"]["technical_candidate_feasible"])

    def test_credits_do_not_create_a_second_agent_benefit_automatically(self):
        no=BY_ID["H01_CREDIT_WITHOUT_COMPENSATION"]
        yes=BY_ID["H01_CREDIT_WITH_BALANCED_TRANSFER"]
        self.assertEqual(no["mechanism"]["target_payoffs"],["6","3"])
        self.assertTrue(no["mechanism"]["target_strictly_pareto_dominates_current"])
        self.assertEqual(no["joint_coordination"]["status"],
                         "VOLUNTARY_PARTICIPATION_NOT_SUPPORTED_BY_PAYOFFS")
        self.assertEqual(yes["joint_coordination"]["status"],
                         "ADMISSIBLE_UNDER_SYNTHETIC_ASSUMPTIONS")
        self.assertEqual(yes["joint_coordination"]
                         ["actor_payoffs_after_burden_and_zero_sum_transfers"],["5","4"])
        self.assertEqual(yes["joint_coordination"]["governance_evidence"]
                         ["transfer_authority"],"PASS")

    def test_zero_sum_credit_transfer_still_needs_authority(self):
        x=BY_ID["H01_CREDIT_TRANSFER_NO_AUTHORITY"]["joint_coordination"]
        self.assertEqual(x["status"],"GOVERNANCE_UNKNOWN_CANNOT_COMMIT")
        self.assertEqual(x["governance_evidence"]["transfer_authority"],"UNKNOWN")
        altered=game("H01_CREDIT_WITH_BALANCED_TRANSFER")
        altered["joint"]["transfers_common_credit_units"]["A"]="0"
        with self.assertRaisesRegex(ValueError,"sum to zero"):
            model.validate(altered)

    def test_transfer_is_in_declared_common_credit_and_cannot_overdraft_source(self):
        good=BY_ID["H01_CREDIT_WITH_BALANCED_TRANSFER"]["joint_coordination"]
        self.assertEqual(good["common_credit_units_before"],{"A":"5","B":"0"})
        self.assertEqual(good["common_credit_units_after"],{"A":"4","B":"1"})
        self.assertTrue(good["credit_transfer_units_conserved"])
        self.assertTrue(good["credit_outflow_fully_funded"])
        bad=BY_ID["H01_CREDIT_INSUFFICIENT_SOURCE_BALANCE"]["joint_coordination"]
        self.assertFalse(bad["credit_outflow_fully_funded"])
        self.assertEqual(bad["status"],"INSUFFICIENT_COMMON_CREDIT_FOR_TRANSFER")
        self.assertTrue(bad["technical_candidate_feasible"])
        self.assertTrue(bad["credit_transfer_units_conserved"])
        self.assertEqual(bad["common_credit_units_after"]["A"],"-1")

    def test_actor_specific_credit_to_private_payoff_rates_are_explicit(self):
        base=BY_ID["H01_CREDIT_WITH_BALANCED_TRANSFER"]["joint_coordination"]
        alternate=BY_ID["H01_CREDIT_ASYMMETRIC_PRIVATE_VALUATIONS"]["joint_coordination"]
        self.assertEqual(base["common_credit_units_after"],
                         alternate["common_credit_units_after"])
        self.assertEqual(base["actor_payoffs_after_burden_and_zero_sum_transfers"],
                         ["5","4"])
        self.assertEqual(alternate["actor_payoffs_after_burden_and_zero_sum_transfers"],
                         ["4","4"])
        self.assertEqual(alternate["status"],
                         "ADMISSIBLE_UNDER_SYNTHETIC_ASSUMPTIONS")
        self.assertTrue(alternate["credit_to_payoff_valuation_is_actor_specific_and_declared"])

    def test_credit_without_receiver_valuation_cannot_claim_personal_gain(self):
        x=BY_ID["H01_CREDIT_NO_VALUE_TO_RECEIVER"]["joint_coordination"]
        self.assertEqual(x["actor_payoffs_after_burden_and_zero_sum_transfers"],
                         ["5","3"])
        self.assertEqual(x["status"],
                         "VOLUNTARY_PARTICIPATION_NOT_SUPPORTED_BY_PAYOFFS")
        self.assertTrue(x["credit_outflow_fully_funded"])

    def test_stronger_actor_reservation_can_block_even_positive_raw_gain(self):
        x=BY_ID["H01_RESERVATION_FLOOR_NOT_MET"]["joint_coordination"]
        self.assertEqual(x["status"],
                         "VOLUNTARY_PARTICIPATION_NOT_SUPPORTED_BY_PAYOFFS")
        self.assertFalse(x["individual_reservation_tests"]["B"])

    def test_all_coordinators_same_feasibility_but_cost_comparison_can_reverse(self):
        lower=BY_ID["H01_CONVENTIONAL_COORDINATOR_CHEAPER"]["joint_coordination"]
        higher=BY_ID["H01_META_PROTOCOL_CHEAPER"]["joint_coordination"]
        equal=BY_ID["H01_COORDINATORS_EQUAL_COST"]["joint_coordination"]
        self.assertEqual(lower["least_cost_equivalent_capability_instrument"],
                         ["CONVENTIONAL_COORDINATOR"])
        self.assertEqual(higher["least_cost_equivalent_capability_instrument"],
                         ["ACC_META_PROTOCOL"])
        self.assertEqual(set(equal["least_cost_equivalent_capability_instrument"]),
                         set(model.ARMS))
        for row in (lower,higher,equal):
            self.assertEqual(row["status"],"ADMISSIBLE_UNDER_SYNTHETIC_ASSUMPTIONS")
            self.assertEqual(row["actor_payoffs_after_burden_and_zero_sum_transfers"],
                             ["4","4"])
            self.assertEqual([arm["admissibility"] for arm in row["coordinators"]],
                             ["ADMISSIBLE_UNDER_SYNTHETIC_ASSUMPTIONS"]*2)
            self.assertTrue(row["cost_does_not_change_physical_outcome"])

    def test_cost_and_payoff_cannot_silently_be_summed(self):
        source=BY_ID["H01_STRICT_COORDINATION_TRAP"]
        self.assertTrue(source["physical_resource_units_are_not_summed_with_actor_payoffs"])
        self.assertTrue(source["information_price_is_not_subtracted_from_actor_utility"])
        self.assertTrue(source["joint_coordination"]["coordinators"][0]
                        ["not_an_architecture_advantage_claim"])


class ReusableFiniteMechanismsAndAdversarialCases(unittest.TestCase):
    def test_third_actor_supported_without_hardcoded_two_person_payoff(self):
        g=deepcopy(BASE)
        ids=("A","B","C")
        g["actors"]=[]
        for actor in ids:
            others=set(ids)-{actor}
            g["actors"].append({
                "id":actor,
                "base_payoff":"3","standalone_return":"0",
                "investment_cost":"3","resource_units_if_active":"1",
                "reservation_floor":"3",
                "complementarity_from":{other:"2" for other in others},
                "inactive_exposure_from":{other:"1" for other in others},
            })
        g["current"]=[0,0,0];g["target"]=[1,1,1]
        g["governance"]["consents"]["C"]="PASS"
        g["joint"]["burden_payoff_units"]["C"]="0"
        g["joint"]["transfers_common_credit_units"]["C"]="0"
        g["joint"]["credit_available_by_actor"]["C"]="0"
        g["joint"]["credit_to_private_payoff_rate_by_actor"]["C"]="1"
        g["joint"]["burden_payoff_units"].update({"A":"0","B":"0"})
        result=model.run_game(g)
        self.assertEqual(result["actor_count"],3)
        self.assertEqual(len(result["finite_feasible_profiles"]),8)
        self.assertEqual(result["mechanism"]["classification"],
                         "STRICT_RATIONAL_COORDINATION_TRAP")
        self.assertEqual(result["mechanism"]["target_payoffs"],["4","4","4"])
        self.assertEqual(result["joint_coordination"]["status"],
                         "ADMISSIBLE_UNDER_SYNTHETIC_ASSUMPTIONS")
        self.assertEqual(result["joint_coordination"]["joint_resource_use_including_setup"],"5")
        self.assertEqual(result["belief_controls"],[])
        self.assertEqual(result["belief_control_scope"],
                         "NOT_EVALUATED_FOR_LARGER_GAME")

    def test_no_pure_nash_matching_pennies_negative_control(self):
        g=deepcopy(BASE)
        g["actors"][0].update({
            "base_payoff":"1","standalone_return":"-1","investment_cost":"0",
            "complementarity_from":{"B":"1"},"inactive_exposure_from":{"B":"1"}})
        g["actors"][1].update({
            "base_payoff":"0","standalone_return":"1","investment_cost":"0",
            "complementarity_from":{"A":"-1"},"inactive_exposure_from":{"A":"-1"}})
        model.validate(g)
        self.assertEqual(model.all_equilibria(g),[])
        dynamics=model.best_response_path(g)
        self.assertEqual(dynamics["status"],"STRICT_RESPONSE_CYCLE_NOT_NASH")
        self.assertFalse(dynamics["terminates_at_nash"])
        self.assertEqual(model.classify(g)["classification"],
                         "NO_PARETO_SUPERIOR_TARGET_ON_ACTOR_UTILITIES")

    def test_all_scenario_results_are_computed_and_distinct(self):
        self.assertEqual(REPORT["scenario_count"],22)
        self.assertEqual(len(BY_ID),22)
        self.assertEqual({s["evidence_tier"] for s in REPORT["scenarios"]},
                         {"SOURCE_ANCHORED_SYNTHETIC_TOY"})
        labels={s["mechanism"]["classification"] for s in REPORT["scenarios"]}
        self.assertIn("STRICT_RATIONAL_COORDINATION_TRAP",labels)
        self.assertIn("FEASIBILITY_PROTOCOL_TRAP_NOT_STRATEGIC_CHOICE",labels)
        self.assertIn("PROFITABLE_UNILATERAL_ESCAPE_NOT_A_NASH_TRAP",labels)
        self.assertIn("NO_PARETO_SUPERIOR_TARGET_ON_ACTOR_UTILITIES",labels)
        self.assertIn("WEAK_NASH_NO_STRICT_UNILATERAL_GAIN",labels)

    def test_new_payoff_parameters_change_equilibrium_without_rewriting_fixture(self):
        before=model.run_game(BASE)
        modified=deepcopy(BASE)
        for actor in modified["actors"]:
            actor["standalone_return"]="5"
        after=model.run_game(modified)
        self.assertNotEqual(before["mechanism"]["classification"],
                            after["mechanism"]["classification"])
        self.assertEqual(before["finite_feasible_profiles"],after["finite_feasible_profiles"])
        self.assertEqual(before["joint_coordination"]["resource_budget"],
                         after["joint_coordination"]["resource_budget"])

    def test_illegal_input_and_patch_are_rejected_before_scoring(self):
        for field,value in (
            ("resource_budget","-1"),
            ("belief_grid",["4/3"]),
            ("current",[0,2]),
            ("evidence_tier","REAL_HUMAN_OBSERVATION"),
        ):
            with self.subTest(field=field):
                c=deepcopy(BASE);c[field]=value
                with self.assertRaises(ValueError):
                    model.validate(c)
        with self.assertRaisesRegex(ValueError,"undeclared field"):
            model.merge(BASE,{"made_up_result":"WIN"})
        x=deepcopy(BASE);x["joint"]["credit_available_by_actor"]["A"]="-1"
        with self.assertRaisesRegex(ValueError,"nonnegative"):
            model.validate(x)
        x=deepcopy(BASE);x["joint"]["credit_to_private_payoff_rate_by_actor"]["B"]="-1"
        with self.assertRaisesRegex(ValueError,"nonnegative"):
            model.validate(x)
        x=deepcopy(BASE);x["actors"][0]["investment_cost"]=True
        with self.assertRaises(ValueError):
            model.validate(x)
        x=deepcopy(BASE);x["governance"]["consents"]["B"]="ASSUMED_TRUE"
        with self.assertRaises(ValueError):
            model.validate(x)

    def test_nash_and_pareto_are_per_actor_not_a_global_scalar(self):
        self.assertTrue(model.dominance((Fraction(3),Fraction(3)),
                                        (Fraction(5),Fraction(5))))
        self.assertFalse(model.dominance((Fraction(3),Fraction(3)),
                                         (Fraction(7),Fraction(2))))
        self.assertFalse(model.dominance((Fraction(3),Fraction(3)),
                                         (Fraction(3),Fraction(3))))
        with self.assertRaises(ValueError):
            model.dominance((Fraction(1),),(Fraction(1),Fraction(2)))

    def test_predeclared_sensitivity_has_all_cells_not_only_favourable_ones(self):
        scan=REPORT["sensitivity"]
        self.assertEqual(scan["cells"],180)
        self.assertEqual(len(scan["rows"]),180)
        self.assertEqual(sum(scan["classification_counts"].values()),180)
        self.assertEqual(sum(scan["joint_admission_counts"].values()),180)
        self.assertTrue(scan["no_explicit_winner_or_equilibrium_in_source_parameters"])
        self.assertIn("STRICT_RATIONAL_COORDINATION_TRAP",
                      scan["classification_counts"])
        self.assertIn("PROFITABLE_UNILATERAL_ESCAPE_NOT_A_NASH_TRAP",
                      scan["classification_counts"])
        self.assertIn("NO_PARETO_SUPERIOR_TARGET_ON_ACTOR_UTILITIES",
                      scan["classification_counts"])
        self.assertIn("ADMISSIBLE_UNDER_SYNTHETIC_ASSUMPTIONS",
                      scan["joint_admission_counts"])
        self.assertIn("VOLUNTARY_PARTICIPATION_NOT_SUPPORTED_BY_PAYOFFS",
                      scan["joint_admission_counts"])

    def test_sensitivity_can_keep_rational_trap_but_lose_joint_acceptance(self):
        cells=REPORT["sensitivity"]["rows"]
        def find(ret,cost,comp,burden):
            return next(x for x in cells if x["params"]=={
                "private_return":ret,"investment_cost":cost,
                "pairwise_complementarity":comp,"joint_burden":burden,
            })
        approved=find("0","3","4","0")
        blocked=find("0","3","4","1")
        self.assertEqual(approved["classification"],
                         "STRICT_RATIONAL_COORDINATION_TRAP")
        self.assertEqual(blocked["classification"],
                         "STRICT_RATIONAL_COORDINATION_TRAP")
        self.assertEqual(approved["joint_admissibility"],
                         "ADMISSIBLE_UNDER_SYNTHETIC_ASSUMPTIONS")
        self.assertEqual(blocked["joint_admissibility"],
                         "VOLUNTARY_PARTICIPATION_NOT_SUPPORTED_BY_PAYOFFS")
        self.assertEqual(approved["target_payoffs"],["4","4"])
        self.assertEqual(blocked["target_payoffs"],["4","4"])

    def test_sensitivity_can_make_unilateral_incentive_profitable(self):
        cells=REPORT["sensitivity"]["rows"]
        a=next(x for x in cells if x["params"]=={
            "private_return":"5","investment_cost":"3",
            "pairwise_complementarity":"6","joint_burden":"0",
        })
        b=next(x for x in cells if x["params"]=={
            "private_return":"0","investment_cost":"3",
            "pairwise_complementarity":"6","joint_burden":"0",
        })
        self.assertEqual(a["classification"],
                         "PROFITABLE_UNILATERAL_ESCAPE_NOT_A_NASH_TRAP")
        self.assertEqual(a["unilateral_profitable_count"],2)
        self.assertEqual(b["classification"],
                         "STRICT_RATIONAL_COORDINATION_TRAP")
        self.assertEqual(b["unilateral_profitable_count"],0)

    def test_illegal_sensitivity_overreach_or_duplicate_fails(self):
        p=deepcopy(MANIFEST["sensitivity"])
        p["investment_costs"]=["3","3"]
        with self.assertRaisesRegex(ValueError,"distinct"):
            model.sensitivity_grid(BASE,p)
        p=deepcopy(MANIFEST["sensitivity"])
        p["individual_joint_burdens"]=["0","-1"]
        with self.assertRaisesRegex(ValueError,"nonnegative"):
            model.sensitivity_grid(BASE,p)
        p=deepcopy(MANIFEST["sensitivity"])
        p["unknown_best_winner"]=["ACC"]
        with self.assertRaisesRegex(ValueError,"four separate"):
            model.sensitivity_grid(BASE,p)

    def test_report_determinism_and_source_boundedness(self):
        self.assertEqual(model.run_manifest(MANIFEST),model.run_manifest(MANIFEST))
        self.assertEqual(REPORT["research_scope"],
                         "SYNTHETIC_FINITE_GAME_CONDITIONAL_CHOICE_AND_AUTHORIZATION")
        self.assertTrue(REPORT["not_proof_of_novel_game_theory_or_empirical_human_choice"])
        self.assertEqual(REPORT["source_original_coupled_trap"]
                         ["source_ownership"],"bounded_traps.coupled_trap unchanged")


if __name__=="__main__":
    unittest.main()
