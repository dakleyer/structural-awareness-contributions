"""ACC architectural regression: parameters != dimensions, no R-C scalar mixing."""
import json
import unittest
from copy import deepcopy
from pathlib import Path

from dimensional_contract import compare_dimensions
import strategic_choice as h01

HERE=Path(__file__).resolve().parent
SOURCE=json.loads((HERE/"H01_STRATEGIC_STUDY.json").read_text(encoding="utf-8"))
BASE=SOURCE["base_game"]
BY={x["id"]:x for x in SOURCE["scenarios"]}


def scenario(case_id):
    x=h01.merge(BASE,BY[case_id]["patch"]);x["id"]=case_id
    return x


class CanonicalDimensionContract(unittest.TestCase):
    def test_simple_open_dimension_set_supports_new_dimensions_without_codes(self):
        old={
            "R":{"unit":"actor_payoff","components":{"A":"3","B":"3"}},
            "C":{"unit":"coordination","components":{"A":"0","B":"0"}},
        }
        new={
            "R":{"unit":"actor_payoff","components":{"A":"4","B":"4"}},
            "C":{"unit":"coordination","components":{"A":"1","B":"1"}},
        }
        out=compare_dimensions(
            old,new,declared_directions={"R":"INCREASE","C":"DECREASE"},
            explicitly_unknown=("E","V","d_(n+1)"))
        self.assertEqual(out["known_K_partial_order"],"INCOMPARABLE_K_TRADEOFF")
        self.assertEqual(out["full_open_model_dominance"],"NOT_ESTABLISHED")
        self.assertEqual(out["per_dimension"]["R"]["status"],"IMPROVES")
        self.assertEqual(out["per_dimension"]["C"]["status"],"WORSENS")
        self.assertTrue(out["no_global_scalarization"])
        # New source-defined dimension can be added without a new ad-hoc
        # parameter in a private utility sum.
        old["D_New"]={"unit":"context_native","components":{"x":"10"}}
        new["D_New"]={"unit":"context_native","components":{"x":"10"}}
        out2=compare_dimensions(
            old,new,declared_directions={"R":"INCREASE","C":"DECREASE",
                                        "D_New":"INCREASE"},
            explicitly_unknown=("E","V"))
        self.assertEqual(out2["per_dimension"]["D_New"]["status"],"UNCHANGED")
        self.assertEqual(out2["known_K_partial_order"],"INCOMPARABLE_K_TRADEOFF")

    def test_h01_original_economic_payoff_coefficients_are_not_extra_axes(self):
        out=h01.acc_dimensional_projection(BASE)
        self.assertEqual(out["known_dimension_ids"],["R","C"])
        self.assertEqual(out["other_dimensions_uncharacterized"],
                         ["E","V","d_(n+1)"])
        self.assertTrue(out["r_c_s_are_payoff_generator_coefficients_not_three_dimensions"])
        self.assertEqual(out["per_dimension"]["R"]["component_changes"],
                         {"A":"2","B":"2"})
        self.assertEqual(out["per_dimension"]["C"]["component_changes"],
                         {"A":"1","B":"1"})
        self.assertEqual(out["known_dimension_comparison"],
                         "INCOMPARABLE_K_TRADEOFF")
        self.assertTrue(out["C_is_separate_coordination_dimension_not_subtracted_from_R"])
        self.assertTrue(out["legacy_scalar_joint_status_is_NOT_an_ACC_result"])

    def test_same_actor_payoffs_but_higher_C_cannot_be_called_automatic_loss_in_R(self):
        costfree=deepcopy(BASE)
        costfree["joint"]["burden_payoff_units"]={"A":"0","B":"0"}
        costly=deepcopy(BASE)
        costly["joint"]["burden_payoff_units"]={"A":"3","B":"3"}
        a=h01.run_game(costfree);b=h01.run_game(costly)
        # Original new-game Nash/payoffs are invariant when only C changes.
        self.assertEqual(a["mechanism"]["current_payoffs"],b["mechanism"]["current_payoffs"])
        self.assertEqual(a["mechanism"]["target_payoffs"],b["mechanism"]["target_payoffs"])
        self.assertEqual(a["acc_known_dimensions"]["per_dimension"]["R"],
                         b["acc_known_dimensions"]["per_dimension"]["R"])
        self.assertEqual(a["acc_known_dimensions"]["known_dimension_comparison"],
                         "MONOTONE_IMPROVEMENT_IN_K")
        self.assertEqual(b["acc_known_dimensions"]["known_dimension_comparison"],
                         "INCOMPARABLE_K_TRADEOFF")
        # The older scalarized gate changes its verdict when subtracting C,
        # but that is precisely why it must NOT be the ACC-dimensional result.
        self.assertNotEqual(a["joint_coordination"]["status"],
                            b["joint_coordination"]["status"])
        self.assertEqual(a["joint_coordination_scalar_payoff_gate"],
                         "LEGACY_ASSUMED_C_TO_R_CONVERSION_DIAGNOSTIC_ONLY")

    def test_180_grid_splits_monotone_incomparable_equivalent_without_scalarizing(self):
        report=h01.run_manifest(SOURCE)
        expected={"MONOTONE_IMPROVEMENT_IN_K":46,
                  "INCOMPARABLE_K_TRADEOFF":92,
                  "NO_MONOTONE_IMPROVEMENT_IN_K":38,
                  "EQUIVALENT_IN_K":4}
        self.assertEqual(report["sensitivity"]["acc_known_R_C_dimensional_counts"],
                         expected)
        self.assertEqual(sum(expected.values()),180)
        self.assertEqual(report["sensitivity"]["joint_admission_counts"],{
            "ADMISSIBLE_UNDER_SYNTHETIC_ASSUMPTIONS":114,
            "VOLUNTARY_PARTICIPATION_NOT_SUPPORTED_BY_PAYOFFS":66})
        self.assertTrue(report["sensitivity"]
                        ["legacy_admission_is_assumed_C_to_R_conversion_not_architecture"])

    def test_monotone_dimension_K_does_not_authorize_open_model_or_rights(self):
        g=scenario("H01_NO_CONSENT")
        g["joint"]["burden_payoff_units"]={"A":"0","B":"0"}
        out=h01.run_game(g)
        self.assertEqual(out["acc_known_dimensions"]["known_dimension_comparison"],
                         "MONOTONE_IMPROVEMENT_IN_K")
        self.assertEqual(out["acc_known_dimensions"]["full_open_model_dominance"],
                         "NOT_ESTABLISHED")
        self.assertEqual(out["joint_coordination"]["status"],
                         "BLOCKED_BY_EXPLICIT_GOVERNANCE")
        self.assertEqual(out["acc_known_dimensions"]["rights_and_transition"],
                         "SEPARATE_REQUIRED")

    def test_credit_transfer_without_V_definition_does_not_become_V_improvement(self):
        game=scenario("H01_CREDIT_WITH_BALANCED_TRANSFER")
        out=h01.run_game(game)
        self.assertIn("V",out["acc_known_dimensions"]
                      ["other_dimensions_uncharacterized"])
        self.assertTrue(out["acc_known_dimensions"]
                        ["credit_transfer_requires_independent_attribution_dimension_contract"])
        self.assertNotIn("V",out["acc_known_dimensions"]["per_dimension"])

    def test_heterogeneous_within_dimension_can_be_noncomparable_without_sum(self):
        a={"R":{"unit":"own_pref","components":{"A":"3","B":"3"}}}
        b={"R":{"unit":"own_pref","components":{"A":"4","B":"2"}}}
        out=compare_dimensions(a,b,declared_directions={"R":"INCREASE"})
        self.assertEqual(out["per_dimension"]["R"]["status"],
                         "INTERNALLY_NONCOMPARABLE")
        self.assertEqual(out["known_K_partial_order"],"INCOMPARABLE_K_TRADEOFF")
        self.assertFalse("aggregate_utility" in out)

    def test_unknown_or_conflicting_units_cannot_be_silently_accepted(self):
        a={"R":{"unit":"own_pref","components":{"A":"3"}}}
        b={"R":{"unit":"money","components":{"A":"4"}}}
        with self.assertRaisesRegex(ValueError,"unit mismatch"):
            compare_dimensions(a,b,declared_directions={"R":"INCREASE"})
        b={"R":{"unit":"own_pref","components":{"A":None}}}
        with self.assertRaisesRegex(ValueError,"finite explicit"):
            compare_dimensions(a,b,declared_directions={"R":"INCREASE"})
        b={"R":{"unit":"own_pref","components":{"A":"4"}}}
        with self.assertRaisesRegex(ValueError,"cannot be silently"):
            compare_dimensions(a,b,declared_directions={"R":"INCREASE"},
                               explicitly_unknown=("R",))


if __name__=="__main__":
    unittest.main()
