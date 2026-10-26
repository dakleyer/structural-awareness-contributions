"""Guardrails for cost sensitivity: both EA-style and conventional outcomes win somewhere."""
import json
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from sensitivity import run_sweep

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
    def test_Q_is_not_universal_winner(self):
        self.assertLess(self.data['exclusive_winners']['Q_META_PROTOCOL'],160)

if __name__=='__main__':unittest.main()
