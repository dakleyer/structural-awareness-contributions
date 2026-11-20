"""H-01 root-cause diagnostics: reject misleading 114/66 average-only reading."""
from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from fractions import Fraction
import json
import unittest

import h01_failure_diagnostics as explain
import strategic_choice as source

HERE=Path(__file__).resolve().parent
MANIFEST=json.loads((HERE/"H01_STRATEGIC_STUDY.json").read_text(encoding="utf-8"))
RUN=source.run_manifest(MANIFEST)
D=explain.examine(MANIFEST,RUN)


def cell(r,c,s,b):
    return next(x for x in RUN["sensitivity"]["rows"] if x["params"]=={
        "private_return":str(r),
        "investment_cost":str(c),
        "pairwise_complementarity":str(s),
        "joint_burden":str(b),
    })


class ExplainMechanismNotAverages(unittest.TestCase):
    def test_cross_tab_has_exact_conditional_trap_and_admission_counts(self):
        a=D["classification_by_joint_admission"]
        self.assertEqual(a["STRICT_RATIONAL_COORDINATION_TRAP"],
                         {"joint_admitted":24,"joint_rejected":15,"count":39})
        self.assertEqual(a["PROFITABLE_UNILATERAL_ESCAPE_NOT_A_NASH_TRAP"],
                         {"joint_admitted":66,"joint_rejected":6,"count":72})
        self.assertEqual(a["WEAK_NASH_NO_STRICT_UNILATERAL_GAIN"],
                         {"joint_admitted":24,"joint_rejected":3,"count":27})
        self.assertEqual(a["NO_PARETO_SUPERIOR_TARGET_ON_ACTOR_UTILITIES"],
                         {"joint_admitted":0,"joint_rejected":42,"count":42})
        self.assertEqual(D["potentially_fixable_strict_traps"],24)
        self.assertEqual(D["strict_traps_unremedied"],15)
        self.assertEqual(D["admitted_cases_not_strict_traps"],90)
        self.assertEqual(sum(x["joint_admitted"] for x in a.values()),114)
        self.assertEqual(sum(x["joint_rejected"] for x in a.values()),66)

    def test_failures_have_four_nonoverlapping_economic_explanations(self):
        self.assertEqual(D["net_failure_reasons"],{
            "JOINT_ALTERNATIVE_HARMS_EACH_ACTOR":30,
            "JOINT_ALTERNATIVE_BREAK_EVEN_BEFORE_COORDINATION":12,
            "BURDEN_GREATER_THAN_JOINT_GAIN":12,
            "BURDEN_EQUALS_JOINT_GAIN_STRICT_RULE_REJECTS":12,
        })
        self.assertEqual(sum(D["net_failure_reasons"].values()),66)

    def test_burden_slices_show_not_only_how_many_but_why(self):
        by=D["conditional_slices"]["by_joint_burden"]
        self.assertEqual({k:(v["joint_accepted"],v["joint_rejected"])
                          for k,v in by.items()},
                         {"0":(46,14),"1":(40,20),"3":(28,32)})
        self.assertEqual({k:(v["genuine_strict_traps"],
                              v["strict_traps_with_admissible_remedy"])
                          for k,v in by.items()},
                         {"0":(13,13),"1":(13,8),"3":(13,3)})
        self.assertEqual(sum(v["strict_traps_with_rejected_remedy"]
                             for v in by.values()),15)

    def test_synergy_zero_has_no_strict_traps_even_when_actions_are_admitted(self):
        by=D["conditional_slices"]["by_pairwise_complementarity"]
        self.assertEqual({k:v["joint_accepted"] for k,v in by.items()},
                         {"0":13,"2":25,"4":35,"6":41})
        self.assertEqual({k:v["genuine_strict_traps"] for k,v in by.items()},
                         {"0":0,"2":6,"4":15,"6":18})
        self.assertEqual({k:v["strict_traps_with_admissible_remedy"]
                          for k,v in by.items()},
                         {"0":0,"2":2,"4":8,"6":14})
        self.assertTrue(all(v["configurations"]==45 for v in by.values()))

    def test_exact_first_move_joint_gain_and_cost_margin(self):
        with_no_cost=explain.phase(cell(0,3,4,0),Fraction(3))
        break_even=explain.phase(cell(0,3,4,1),Fraction(3))
        over_cost=explain.phase(cell(0,3,4,3),Fraction(3))
        for v in (with_no_cost,break_even,over_cost):
            self.assertEqual(v["unilateral_increment_D"],"-3")
            self.assertEqual(v["joint_increment_before_burden_J"],"1")
            self.assertEqual(v["strategic_mechanism"],
                             "STRICT_RATIONAL_COORDINATION_TRAP")
        self.assertEqual(with_no_cost["net_increment_after_burden_N"],"1")
        self.assertEqual(break_even["net_increment_after_burden_N"],"0")
        self.assertEqual(over_cost["net_increment_after_burden_N"],"-2")
        self.assertTrue(with_no_cost["coordination_admitted"])
        self.assertFalse(break_even["coordination_admitted"])
        self.assertFalse(over_cost["coordination_admitted"])

    def test_burden_only_counterfactuals_hold_all_other_input_identical(self):
        sw=D["matched_burden_counterfactuals"]
        self.assertEqual(sw["distinct_return_cost_synergy_conditions"],60)
        self.assertEqual(sw["lost_admissibility_when_only_burden_increases"],18)
        self.assertEqual(sw["strict_traps_losing_admissibility"],10)
        self.assertEqual(len(sw["examples"]),18)
        self.assertTrue(all(x["status"]=="ONLY_BURDEN_CHANGED_STRICT_ACCEPTANCE_LOST"
                            and x["baseline_burden"]=="0"
                            and x["increased_burden"]=="3"
                            for x in sw["examples"]))

    def test_strict_gain_policy_is_an_assumption_not_a_physical_law(self):
        scenario=deepcopy(MANIFEST["base_game"])
        scenario["joint"]["burden_payoff_units"]={"A":"1","B":"1"}
        for agent in scenario["actors"]:
            agent["complementarity_from"]={k:"4" for k in agent["complementarity_from"]}
        self.assertEqual(source.coordinated_joint_candidate(scenario)["status"],
                         "VOLUNTARY_PARTICIPATION_NOT_SUPPORTED_BY_PAYOFFS")
        scenario["joint"]["strict_gain_required"]=False
        self.assertEqual(source.coordinated_joint_candidate(scenario)["status"],
                         "ADMISSIBLE_UNDER_SYNTHETIC_ASSUMPTIONS")
        # Even worse, a weakly permitted zero-benefit state is not a
        # Pareto improvement; keeping classification separate is essential.
        for agent in scenario["actors"]:
            agent["complementarity_from"]={k:"3" for k in agent["complementarity_from"]}
        scenario["joint"]["burden_payoff_units"]={"A":"0","B":"0"}
        self.assertEqual(source.classify(scenario)["classification"],
                         "NO_PARETO_SUPERIOR_TARGET_ON_ACTOR_UTILITIES")
        self.assertEqual(source.coordinated_joint_candidate(scenario)["status"],
                         "ADMISSIBLE_UNDER_SYNTHETIC_ASSUMPTIONS")

    def test_every_rejection_has_a_grounded_named_scenario_explanation(self):
        by={x["case_id"]:x for x in D["named_scenarios_explained"]}
        self.assertEqual(len(by),22)
        cases={
            "H01_NO_PARETO_JOINT_GAIN":"INDIVIDUAL_NET_PAYOFF_BELOW_RESERVATION_OR_STRICT_GAIN",
            "H01_TOO_EXPENSIVE_COORDINATION":"INDIVIDUAL_NET_PAYOFF_BELOW_RESERVATION_OR_STRICT_GAIN",
            "H01_NO_CONSENT":"EXPLICIT_AUTHORIZATION_OR_CONSENT_FAILURE",
            "H01_UNKNOWN_AUTHORITY":"EVIDENCE_OF_AUTHORITY_OR_CONSENT_UNKNOWN",
            "H01_NO_JOINT_PROTOCOL":"EXPLICIT_AUTHORIZATION_OR_CONSENT_FAILURE",
            "H01_INSUFFICIENT_TRANSITION_BUDGET":"JOINT_SETUP_EXCEEDS_AVAILABLE_PHYSICAL_BUDGET",
            "H01_TECHNICAL_TARGET_INFEASIBLE":"TARGET_TECHNICALLY_INFEASIBLE",
            "H01_CREDIT_INSUFFICIENT_SOURCE_BALANCE":"UNFUNDED_COMMON_CREDIT_TRANSFER",
            "H01_CREDIT_NO_VALUE_TO_RECEIVER":"INDIVIDUAL_NET_PAYOFF_BELOW_RESERVATION_OR_STRICT_GAIN",
            "H01_CREDIT_TRANSFER_NO_AUTHORITY":"EVIDENCE_OF_AUTHORITY_OR_CONSENT_UNKNOWN",
        }
        for case,reason in cases.items():
            with self.subTest(case=case):
                self.assertIn(reason,by[case]["specific_reasons"])
                self.assertNotEqual(by[case]["joint_status"],
                                    "ADMISSIBLE_UNDER_SYNTHETIC_ASSUMPTIONS")
        self.assertEqual(by["H01_CREDIT_NO_VALUE_TO_RECEIVER"]["failing_actor_ids"],
                         ["B"])

    def test_source_models_enforce_permissions_independently_from_economic_grid(self):
        a=D["evidence_scope"]
        self.assertEqual(a["physical_resource_use"],"4")
        self.assertEqual(a["physical_resource_budget"],"10")
        self.assertEqual(a["consent_and_authority"],
                         "PASS_BY_FIXTURE_NOT_OBSERVED")
        self.assertEqual(a["participation_rule"],
                         "EACH_ACTOR_MUST_IMPROVE_STRICTLY")
        self.assertEqual(D["grid_cell_counts_are_NOT_real_world_probabilities"],
                         True)
        self.assertEqual(D["total_cells"],180)

    def test_tampered_source_classification_or_admission_cannot_pass(self):
        broken=deepcopy(RUN)
        broken["sensitivity"]["rows"][0]["classification"]="PRETEND_NASH"
        with self.assertRaisesRegex(AssertionError,"classification"):
            explain.examine(MANIFEST,broken)
        broken=deepcopy(RUN)
        broken["sensitivity"]["rows"][0]["joint_admissibility"]="PRETEND_PASS"
        with self.assertRaisesRegex(AssertionError,"admission"):
            explain.examine(MANIFEST,broken)
        broken=deepcopy(RUN)
        broken["sensitivity"]["rows"][0]["target_payoffs"]=["999","999"]
        with self.assertRaisesRegex(AssertionError,"payoff"):
            explain.examine(MANIFEST,broken)

    def test_sensitivity_contract_rejects_incompatible_beliefs_or_unauthorized_base(self):
        m=deepcopy(MANIFEST)
        m["base_game"]["governance"]["authority"]="UNKNOWN"
        with self.assertRaisesRegex(ValueError,"PASS governance"):
            explain.examine(m,RUN)
        m=deepcopy(MANIFEST)
        m["base_game"]["joint"]["strict_gain_required"]=False
        with self.assertRaisesRegex(ValueError,"strict"):
            explain.examine(m,RUN)
        m=deepcopy(MANIFEST)
        m["base_game"]["linear_constraints"]=[{
            "coefficients":["1","-1"],"capacity":"0"}]
        with self.assertRaisesRegex(ValueError,"constrained"):
            explain.examine(m,RUN)


if __name__=="__main__":
    unittest.main()
