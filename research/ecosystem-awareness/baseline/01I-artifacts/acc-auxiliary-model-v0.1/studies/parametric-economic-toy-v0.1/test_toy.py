"""Self-contained invariants and regression examples for the parametric ACC toy."""
from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import io
import unittest
from unittest.mock import patch
from contextlib import redirect_stdout

from toy import ToyError, evaluate, network, portfolio, formulas
from run import update_path, run_cli


def fixture(name):
    return json.loads((Path(__file__).resolve().parent / "scenarios" / (name + ".json"))
                      .read_text(encoding="utf-8"))


class PortfolioTests(unittest.TestCase):
    def setUp(self):
        self.s = fixture("portfolio")

    def test_joint_optimum_and_all_ledgers(self):
        r = portfolio(self.s)
        self.assertEqual(r["state_count_F_T"], 2)
        self.assertEqual(r["state_count_F_G"], 2)
        self.assertEqual(r["actual"]["projects"], ["SCALE"])
        self.assertEqual(r["technical_optimum"]["projects"], ["INTEGRATE", "SCALE"])
        self.assertAlmostEqual(r["G_technical"], 58)
        self.assertAlmostEqual(r["G_governable"], 58)
        self.assertAlmostEqual(r["G_efficiency_same_service_resources"], 20)
        self.assertAlmostEqual(r["technical_optimum"]["C_adj"], 24)  # 15+9 booked once.
        self.assertAlmostEqual(r["technical_optimum"]["utility"], 77)  # 70+30−24+1.
        self.assertTrue(r["suboptimal_governable"])

    def test_cfo_veto_is_not_physical_impossibility(self):
        self.s["approvals"]["CFO"] = False
        r = portfolio(self.s)
        self.assertAlmostEqual(r["G_technical"], 58)
        self.assertAlmostEqual(r["G_governable"], 0)
        self.assertEqual(r["state_count_F_G"], 1)
        self.assertIn("CFO", r["technical_optimum_block_reason"]["missing_approvals"])
        self.assertFalse(r["suboptimal_governable"])

    def test_no_transfer_can_make_joint_win_nonpareto(self):
        self.s["projects"][0]["transfers"] = {}
        r = portfolio(self.s)
        self.assertAlmostEqual(r["G_technical"], 58)
        self.assertAlmostEqual(r["G_governable"], 0)
        self.assertIn("Systems", r["technical_optimum_block_reason"]["negative_actors"])

    def test_pareto_is_relative_to_current_not_initial_baseline(self):
        self.s["projects"][0]["gross_payoffs"]["Marketing"] = 46.5
        r = portfolio(self.s)
        self.assertGreater(r["technical_optimum"]["actor_net"]["Marketing"], 0)
        self.assertLess(r["technical_optimum"]["actor_net"]["Marketing"],
                        r["actual"]["actor_net"]["Marketing"])
        self.assertAlmostEqual(r["G_technical"], 44.5)
        self.assertAlmostEqual(r["G_governable"], 0)
        self.assertIn("Marketing", r["technical_optimum_block_reason"]["negative_actors"])

    def test_no_unmodelled_rollback_and_incremental_adjustment_cost(self):
        r = portfolio(self.s)
        self.assertTrue(all("SCALE" in x["projects"] for x in r["frontier_top"]))
        self.assertEqual(r["transition_scope"], "ADDITIONS_ONLY_FROM_CURRENT; NO_UNMODELLED_ROLLBACK")
        self.assertAlmostEqual(r["technical_optimum"]["new_C_adj"], 15)

    def test_transfer_is_zero_sum(self):
        self.s["projects"][0]["transfers"]["Marketing"] = -39
        with self.assertRaises(ToyError):
            portfolio(self.s)

    def test_bad_rights_excluded_from_both_frontiers(self):
        self.s["projects"][0]["rights_preserved"] = False
        r = portfolio(self.s)
        self.assertEqual(r["state_count_F_T"], 1)
        self.assertAlmostEqual(r["G_technical"], 0)

    def test_costly_transition_can_rationally_be_rejected(self):
        self.s["parameters"]["transition_budget"] = 10
        r = portfolio(self.s)
        self.assertAlmostEqual(r["G_technical"], 0)
        self.assertEqual(r["technical_optimum"]["projects"], ["SCALE"])

    def test_efficiency_only_compares_identical_outputs(self):
        self.s["projects"][0]["output_deltas"]["service_units"] = 1
        r = portfolio(self.s)
        self.assertAlmostEqual(r["G_efficiency_same_service_resources"], 0)
        self.assertAlmostEqual(r["G_technical"], 58)  # Distinct utility question.

    def test_hid_observed_potential_and_recovery_are_distinct(self):
        r = portfolio(self.s)["hid"]
        self.assertEqual(r["status"], "SYNTHETIC_CONDITIONAL_NOT_EMPIRICAL")
        self.assertAlmostEqual(r["HICR_time"], 3/12)
        self.assertAlmostEqual(r["HID_observed"], 7/12)
        self.assertAlmostEqual(r["H_releasable_hours"], 3)
        self.assertAlmostEqual(r["HID_potential"], 3/12)
        self.assertAlmostEqual(r["F_HICT_conditional"], 3/12+0.7*3/12)

    def test_no_classification_does_not_invent_hid(self):
        self.s["parameters"]["acw_classified_synthetically"] = False
        self.assertIsNone(portfolio(self.s)["hid"]["HID_observed"])

    def test_no_implicit_governance_when_current_not_approved(self):
        self.s["approvals"]["Marketing"] = False
        r = portfolio(self.s)
        self.assertFalse(r["governability_of_actual"])
        self.assertIsNone(r["G_governable"])

    def test_resource_and_human_constraints(self):
        self.s["parameters"]["resources_limit"] = 120
        with self.assertRaises(ToyError):
            portfolio(self.s)  # SCALE is above the cap.
        self.s = fixture("portfolio")
        self.s["baseline"]["human_capacity_hours"] = 10
        with self.assertRaises(ToyError):
            portfolio(self.s)  # Current SCALE exceeds capacity.

    def test_duplicate_or_unbounded_projects_rejected(self):
        self.s["projects"].append(deepcopy(self.s["projects"][0]))
        with self.assertRaises(ToyError):
            portfolio(self.s)
        self.s = fixture("portfolio")
        self.s["projects"] = [dict(id="P"+str(i)) for i in range(17)]
        with self.assertRaises(ToyError):
            portfolio(self.s)


class NetworkTests(unittest.TestCase):
    def setUp(self):
        self.s = fixture("network")

    def test_source_closed_forms_and_negative_marginal(self):
        r = network(self.s)
        self.assertAlmostEqual(r["rows"][-1]["d_t"], 126)
        self.assertAlmostEqual(r["rows"][-1]["d_hat_t"], 12)
        self.assertAlmostEqual(r["rows"][-1]["forecast_error_e_t"], 114)
        self.assertAlmostEqual(r["rows"][-1]["D_T"], 924)
        self.assertAlmostEqual(r["arms"]["L"][-1]["d_t"], 12)
        self.assertAlmostEqual(r["arms"]["E"][-1]["d_t"], 12)
        self.assertAlmostEqual(r["arms"]["R"][-1]["d_t"], 58.21188270458232)
        self.assertAlmostEqual(r["rows"][15]["flow_value"], 78.4)
        self.assertAlmostEqual(r["rows"][19]["flow_value"], 74)
        self.assertEqual(r["summary"]["first_negative_marginal_t"], 17)
        self.assertTrue(r["summary"]["convex_last_three"])
        self.assertAlmostEqual(r["rows"][19]["delta2_d_t"], 0.6)

    def test_path_gap_vs_technically_unavailable_analytical_arm(self):
        r = network(self.s)
        self.assertNotIn("L", r["rows"][-1]["comparable_arms"])
        self.assertEqual(r["rows"][-1]["path_optimum_technical_arm"], "E")
        self.assertEqual(r["rows"][-1]["path_optimum_governable_arm"], "R")
        self.assertAlmostEqual(r["summary"]["last_G_path_technical"], 781.5)
        self.assertGreater(r["summary"]["last_G_path_governable"], 0)

    def test_high_setup_cost_removes_technical_gap_when_all_alternatives_costly(self):
        self.s["arms"]["E"]["setup_cost"] = 1e6
        self.s["arms"]["R"]["setup_cost"] = 1e6
        r = network(self.s)
        self.assertAlmostEqual(r["rows"][-1]["G_path_technical"], 0)

    def test_capacity_overflow_qualifies_metrics(self):
        self.s["capacity_hours_per_dimension"] = 4
        r = network(self.s)
        self.assertIsNotNone(r["summary"]["first_human_capacity_overflow_t"])
        self.assertIsNone(r["rows"][-1]["G_path_technical"])
        self.assertIsNone(r["rows"][-1]["human"]["HID_potential"])

    def test_positive_synergy_can_break_same_service_comparison(self):
        self.s["synergy_per_compatible_link"] = 1
        r = network(self.s)
        self.assertIsNone(r["rows"][-1]["G_path_technical"])
        self.assertEqual(r["rows"][-1]["comparable_arms"], ["N"])
        self.assertGreater(r["rows"][-1]["production"], 200)

    def test_zero_incompatibility_no_acceleration(self):
        for arm in self.s["arms"].values():
            arm["p_incompatible"] = 0
        r = network(self.s)
        self.assertAlmostEqual(r["summary"]["last_d_t"], 0)
        self.assertFalse(r["summary"]["convex_last_three"])
        self.assertIsNone(r["summary"]["first_negative_marginal_t"])

    def test_obligation_ledger_identity_and_real_costs(self):
        r = network(self.s)
        prior = 0.0
        for row in r["arms"]["R"]:
            self.assertAlmostEqual(row["active_obligations_O_t"],
                                   prior + row["new_obligations_N_t"] - row["retired_obligations_R_t"])
            prior = row["active_obligations_O_t"]
            self.assertGreaterEqual(row["maintenance_cost"], 0)
            self.assertGreaterEqual(row["C_adj_t"], 0)

    def test_retirement_and_interoperability_are_true_ablations(self):
        baseline = network(self.s)
        self.s["arms"]["N"]["retirement_rate"] = 0.15
        after = network(self.s)
        self.assertAlmostEqual(after["rows"][-1]["d_t"], baseline["arms"]["R"][-1]["d_t"])
        self.assertLess(after["rows"][-1]["d_t"], baseline["rows"][-1]["d_t"])
        self.s["arms"]["N"]["interoperability"] = "inverse_time"
        after_standard = network(self.s)
        self.assertLess(after_standard["rows"][-1]["d_t"], after["rows"][-1]["d_t"])

    def test_hid_is_conditional_on_classification_and_counterfactual(self):
        r = network(self.s)
        human = r["rows"][-1]["human"]
        self.assertAlmostEqual(human["HID_observed"], 126/186)
        self.assertAlmostEqual(human["HID_potential"], 114/186)
        self.s["acw_classified_synthetically"] = False
        self.assertIsNone(network(self.s)["rows"][-1]["human"]["HID_observed"])
        self.s["acw_classified_synthetically"] = True
        self.s["same_service_counterfactual"] = False
        self.assertIsNone(network(self.s)["rows"][-1]["human"]["HID_potential"])

    def test_bad_probabilities_rejected(self):
        self.s["arms"]["N"]["p_incompatible"] = 1.1
        with self.assertRaises(ToyError):
            network(self.s)


class FormulaAndCLITests(unittest.TestCase):
    def test_formulas_reproduce_M0_to_M3(self):
        r = formulas(fixture("formulas"))
        at20 = next(v for v in r["rows"] if v["n"] == 20)
        self.assertAlmostEqual(at20["D_veto_M0"], 51.89488969396204)
        self.assertAlmostEqual(at20["D_inter_M1"], 114)
        self.assertAlmostEqual(at20["M_proposals_M3"], 380)
        self.assertAlmostEqual(at20["A_approved_M3"], 51.33236527157373)
        self.assertAlmostEqual(at20["P_endogenous_M3"], 251.33236527157374)

    def test_sparse_topology_is_linear_not_dense(self):
        cfg = fixture("formulas")
        cfg["topology"] = "star"
        r = formulas(cfg)
        self.assertEqual(r["rows"][2]["E_edges"], 19)
        self.assertAlmostEqual(r["rows"][2]["D_inter_M1"], 0.2*3*19)

    def test_rejected_proposals_not_proven_hid(self):
        cfg = fixture("formulas")
        cfg["q_accept"] = 1
        r = formulas(cfg)
        self.assertTrue(all(row["R_rejected_M3"] == 0 for row in r["rows"]))
        self.assertTrue(all(row["D_veto_M0"] == 0 for row in r["rows"]))
        self.assertNotIn("HID_observed", r)

    def test_override_typing_and_typo(self):
        cfg = fixture("network")
        update_path(cfg, "arms.N.p_incompatible=0.5")
        self.assertAlmostEqual(cfg["arms"]["N"]["p_incompatible"], 0.5)
        with self.assertRaises(ToyError):
            update_path(cfg, "arms.N.unknown=0.1")
        with self.assertRaises(ToyError):
            update_path(cfg, "arms.N.governance_available=1")

    def test_formulas_reject_unsorted_dimension_values(self):
        cfg = fixture("formulas")
        cfg["n_values"] = [20, 5]
        with self.assertRaises(ToyError):
            formulas(cfg)

    def test_cli_sweep_parameter_matrix_json(self):
        cfg = fixture("network")
        buffer = io.StringIO()
        with patch.object(Path, "read_text", return_value=json.dumps(cfg)):
            with redirect_stdout(buffer):
                code = run_cli(["network", "dummy.json", "--sweep",
                                "arms.N.p_incompatible=[0.1,0.2]", "--sweep",
                                "arms.N.retirement_rate=[0.0,0.15]", "--summary"])
        self.assertEqual(code, 0)
        cases = json.loads(buffer.getvalue())["cases"]
        self.assertEqual(len(cases), 4)
        self.assertLess(cases[0]["d_t"], cases[2]["d_t"])
        self.assertLess(cases[1]["d_t"], cases[0]["d_t"])

    def test_cli_sweep_csv_and_override_guard(self):
        cfg = fixture("network")
        buffer = io.StringIO()
        with patch.object(Path, "read_text", return_value=json.dumps(cfg)):
            with redirect_stdout(buffer):
                code = run_cli(["network", "dummy.json", "--sweep",
                                "arms.N.retirement_rate=[0.0,0.15]", "--format", "csv"])
        self.assertEqual(code, 0)
        self.assertIn("last_d_t", buffer.getvalue())
        self.assertEqual(len(buffer.getvalue().splitlines()), 3)

    def test_noninteger_horizon_rejected(self):
        cfg = fixture("network")
        cfg["horizon"] = 20.5
        with self.assertRaises(ToyError):
            network(cfg)

    def test_counterfactual_rights_or_full_service_denied(self):
        cfg = fixture("network")
        cfg["arms"]["E"]["rights_preserved"] = False
        cfg["arms"]["R"]["full_service_preserved"] = False
        r = network(cfg)
        self.assertIsNone(r["rows"][-1]["G_path_technical"])
        self.assertIsNone(r["rows"][-1]["human"]["HID_potential"])



if __name__ == "__main__":
    unittest.main()
