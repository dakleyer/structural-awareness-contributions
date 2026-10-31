import copy, json, unittest
from pathlib import Path
from sensitivity import run

class SweepControls(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.x=run();cls.g=cls.x['grids']
 def test_fixed_grid_count(self):self.assertEqual(self.x['total_sweep_runs'],88)
 def test_exact_reference(self):
  self.assertEqual(json.loads(json.dumps(self.x)),json.loads((Path(__file__).parent/'REFERENCE_SWEEPS.json').read_text()))
 def test_all_run_ids_unique(self):
  ids=[r['id'] for group in self.g.values() for r in group]
  self.assertEqual(len(ids),len(set(ids)))
 def test_dense_high_n_grows_and_zero_g_is_zero(self):
  dense=[x for x in self.g['network'] if x['parameters'][0]=='dense' and x['parameters'][2]==.2 and x['parameters'][3]==0.]
  self.assertEqual([x['ratio_percent'] for x in dense],[4,9,19,39])
  self.assertTrue(all(x['hypothetical_gap']==0 for x in self.g['network'] if x['parameters'][2]==0))
 def test_star_not_same_as_dense(self):
  star=[x for x in self.g['network'] if x['parameters'][0]=='star' and x['parameters'][2]==.2 and x['parameters'][3]==0.]
  self.assertTrue(max(x['ratio_percent'] for x in star)<2.01)
 def test_cost_profiles_where_conventional_wins(self):
  self.assertTrue(any(x['best_mode']=='TARGETED_CONVENTIONAL' for x in self.g['qualification']))
 def test_cost_profiles_where_B_wins(self):
  self.assertTrue(any(x['best_mode']=='SOURCE_B' for x in self.g['qualification']))
 def test_Aonly_is_rational_if_no_gain(self):
  self.assertTrue(any(x['best_mode']=='A_ONLY' for x in self.g['qualification']))
 def test_credit_has_both_feasible_and_infeasible(self):
  s={x['status'] for x in self.g['credit']}
  self.assertEqual(s,{'RELATIVE_CREDIT_FEASIBLE','RELATIVE_CREDIT_IMPOSSIBLE'})
 def test_closure_abstains_without_regularity(self):
  self.assertTrue(all(x['status']=='REGULARITY_NOT_ESTABLISHED' for x in self.g['closure'] if x['parameters'][0] is None))
 def test_closure_positive_negative_and_unknown(self):
  s={x['status'] for x in self.g['closure']}
  self.assertTrue({'PREDICATE_SUPPORTED_IN_FRAME','PREDICATE_REFUTED_IN_FRAME','PREDICATE_UNDETERMINED'}.issubset(s))
 def test_no_empirical_claim(self):self.assertEqual(self.x['evidence'],'SYNTHETIC_CONDITIONAL_NOT_EMPIRICAL')

if __name__=='__main__':unittest.main()
