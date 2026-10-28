"""Guardrails for cost sensitivity: both EA-style and conventional outcomes win somewhere."""
import json
from copy import deepcopy
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from sensitivity import run_sweep, BASE
from agentic_reduction import run_case

class FairRegimeControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.data=run_sweep(); cls.rows=cls.data['scenarios']
    def test_complete_2x5x4x4_grid(self):self.assertEqual(self.data['n_cases'],160)
    def test_no_duplicate_scenario(self):self.assertEqual(len(set(x['id'] for x in self.rows)),160)
    def test_information_is_not_globally_positive(self):
        self.assertGreater(self.data['exclusive_winners']['A_ONLY'],0)
    def test_qualified_Q_can_win_some_cost_regime(self):
        self.assertGreater(self.data['exclusive_winners']['Q_META_PROTOCOL'],0)
    def test_conventional_directed_can_win_other_regime(self):
        self.assertGreater(self.data['exclusive_winners']['CONVENTIONAL_DIRECTED'],0)
    def test_all_outputs_numeric_and_finite(self):
        import math
        self.assertTrue(all(math.isfinite(v) for x in self.rows for v in x['net_gain_vs_A_only'].values()))
    def test_low_rate_Q_never_improves_physical_service(self):
        self.assertTrue(all(not x['Q_improvement_physical'] for x in self.rows if x['rate_PRIVATE_for_score']==0.6))
    def test_peer_no_automatic_win(self):
        self.assertTrue(any(x['net_gain_vs_A_only']['CONVENTIONAL_DIRECTED']<x['net_gain_vs_A_only']['Q_META_PROTOCOL'] for x in self.rows))
    def test_matched_q_peer_ties_in_each_160_price_regime(self):
        # This added comparator is absent from the original three-arm sweep.
        # At equal Q, rights, physical overhead and source price it must tie.
        for record in self.rows:
            s=deepcopy(BASE)
            s["id"]=record["id"]
            rate=record["rate_PRIVATE_for_score"]
            s["truth_private"]["recipient_incremental_rate"]=rate
            s["public"]["overhead_resources"]=record["coordination_resources"]
            s["Q"]["lower_rate"]=1.6 if rate==2.0 else 0.5
            s["Q"]["cost"]=record["Q_cost"]
            s["directed"]["measured_rate"]=rate
            s["directed"]["cost"]=record["conventional_directed_cost"]
            s["directed"]["equivalent_Q_cost"]=record["Q_cost"]
            with self.subTest(regime=record["id"]):
                arms=run_case(s)["arms"]
                q_arm=arms["Q_META_PROTOCOL"]
                peer=arms["CONVENTIONAL_EQUIVALENT_Q"]
                self.assertEqual(q_arm["plan"]["transfer"],peer["plan"]["transfer"])
                self.assertEqual(q_arm["plan"]["status"],peer["plan"]["status"])
                self.assertEqual(q_arm["observed_by_referee_only"],peer["observed_by_referee_only"])
                self.assertEqual(q_arm["mission_net_value_after_information_cost"],
                                 peer["mission_net_value_after_information_cost"])

    def test_Q_is_not_universal_winner(self):
        self.assertLess(self.data['exclusive_winners']['Q_META_PROTOCOL'],160)

if __name__=='__main__':unittest.main()
