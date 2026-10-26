"""RAV-01 deterministic witness tests and negative controls (no empirical claims)."""
import math
import unittest

from risk_model import (
    RiskChoice, RiskOutcome, WelfareSnapshot, certainty_equivalent,
    change_advantage_ce, declared_examples, exit_probability, mean_advantage,
    preferred_course, relative_risk_premium, DefencePolicy,
    foregone_utility_gap, defense_advantage_over_stay,
    policy_certainty_equivalents, preferred_with_defense,
    three_way_choice_probabilities,
)


class RationalPersistenceWitness(unittest.TestCase):
    def setUp(self):
        self.early = RiskChoice(RiskOutcome(10, 4), RiskOutcome(16, 36), gamma=0.5)
        self.late = RiskChoice(RiskOutcome(14, 4), RiskOutcome(25, 64), gamma=0.5)

    def test_aversion_is_constant_across_periods(self):
        self.assertEqual(self.early.gamma, self.late.gamma)

    def test_expected_reward_from_redesign_increases(self):
        self.assertEqual(mean_advantage(self.early), 6)
        self.assertEqual(mean_advantage(self.late), 11)

    def test_risk_premium_grows_with_excess_variance(self):
        self.assertEqual(relative_risk_premium(self.early), 8)
        self.assertEqual(relative_risk_premium(self.late), 15)

    def test_ce_values_both_periods(self):
        self.assertEqual(certainty_equivalent(self.early.stay, 0.5), 9)
        self.assertEqual(certainty_equivalent(self.early.redesign, 0.5), 7)
        self.assertEqual(certainty_equivalent(self.late.stay, 0.5), 13)
        self.assertEqual(certainty_equivalent(self.late.redesign, 0.5), 9)

    def test_better_expected_redesign_yet_stay_is_preferred(self):
        for choice in (self.early, self.late):
            with self.subTest(choice=choice):
                self.assertGreater(mean_advantage(choice), 0)
                self.assertLess(change_advantage_ce(choice), 0)
                self.assertEqual(preferred_course(choice), "STAY")

    def test_later_persistence_is_stronger_despite_higher_exit_mean(self):
        self.assertEqual(change_advantage_ce(self.early), -2)
        self.assertEqual(change_advantage_ce(self.late), -4)
        self.assertLess(exit_probability(self.late), exit_probability(self.early))
        self.assertAlmostEqual(exit_probability(self.early), 0.119202922, places=8)
        self.assertAlmostEqual(exit_probability(self.late), 0.01798621, places=8)

    def test_risk_neutral_control_prefers_exit(self):
        neutral = RiskChoice(self.late.stay, self.late.redesign, gamma=0.0)
        self.assertEqual(preferred_course(neutral), "REDESIGN")
        self.assertEqual(change_advantage_ce(neutral), 11)

    def test_equal_variance_control_prefers_exit(self):
        equal = RiskChoice(self.late.stay, RiskOutcome(25, 4), gamma=0.5)
        self.assertEqual(preferred_course(equal), "REDESIGN")
        self.assertEqual(relative_risk_premium(equal), 0)

    def test_higher_mean_can_overcome_any_given_finite_premium(self):
        superior = RiskChoice(self.late.stay, RiskOutcome(40, 64), gamma=0.5)
        self.assertEqual(preferred_course(superior), "REDESIGN")

    def test_lower_variance_redesign_can_be_preferred(self):
        protected = RiskChoice(self.late.stay, RiskOutcome(25, 1), gamma=0.5)
        self.assertLess(relative_risk_premium(protected), 0)
        self.assertEqual(preferred_course(protected), "REDESIGN")

    def test_transition_cost_is_counted_once(self):
        c = RiskChoice(RiskOutcome(10, 4), RiskOutcome(16, 4), gamma=0.5, transition_cost=3)
        self.assertEqual(change_advantage_ce(c), 3)

    def test_exact_indifference(self):
        c = RiskChoice(RiskOutcome(10, 4), RiskOutcome(10, 4), gamma=0.5)
        self.assertEqual(preferred_course(c), "TIE")
        self.assertEqual(exit_probability(c), 0.5)

    def test_translation_invariance_absolute_aversion(self):
        shifted = RiskChoice(RiskOutcome(114, 4), RiskOutcome(125, 64), gamma=0.5)
        self.assertAlmostEqual(change_advantage_ce(shifted), change_advantage_ce(self.late))

    def test_logit_is_probability_of_choice_not_success(self):
        self.assertGreaterEqual(exit_probability(self.late), 0)
        self.assertLessEqual(exit_probability(self.late), 1)
        lower_kappa = RiskChoice(self.late.stay, self.late.redesign, 0.5, choice_sensitivity=0.5)
        self.assertGreater(exit_probability(lower_kappa), exit_probability(self.late))
        extreme = RiskChoice(RiskOutcome(0, 0), RiskOutcome(-10000, 0), 1)
        self.assertEqual(exit_probability(extreme), 0)
        reverse = RiskChoice(RiskOutcome(0, 0), RiskOutcome(10000, 0), 1)
        self.assertEqual(exit_probability(reverse), 1)


class MoreProsperityAndMoreSufferingControl(unittest.TestCase):
    def test_rising_gross_benefit_non_linear_discomfort_and_rising_welfare(self):
        states = [WelfareSnapshot(12, 2), WelfareSnapshot(20, 6), WelfareSnapshot(30, 13)]
        gross = [x.gross_benefit_excluding_discomfort for x in states]
        discomfort = [x.stipulated_discomfort for x in states]
        welfare = [x.net_welfare for x in states]
        self.assertEqual(welfare, [10, 14, 17])
        self.assertTrue(all(y > x for x, y in zip(gross, gross[1:])))
        self.assertTrue(all(y > x for x, y in zip(discomfort, discomfort[1:])))
        self.assertTrue(all(y > x for x, y in zip(welfare, welfare[1:])))
        self.assertGreater(discomfort[2]-2*discomfort[1]+discomfort[0], 0)

    def test_bad_forecast_does_not_force_exit(self):
        current_realized_net_welfare = WelfareSnapshot(30, 13).net_welfare
        future = RiskChoice(RiskOutcome(14, 4), RiskOutcome(25, 64), gamma=0.5)
        self.assertLess(future.stay.mean, current_realized_net_welfare)
        self.assertGreater(future.redesign.mean, future.stay.mean)
        self.assertEqual(preferred_course(future), "STAY")

    def test_discomfort_not_computed_from_structural_gap(self):
        x = WelfareSnapshot(gross_benefit_excluding_discomfort=40, stipulated_discomfort=21)
        self.assertEqual(x.net_welfare, 19)
        self.assertFalse(hasattr(x, "G"))
        self.assertFalse(hasattr(x, "HID"))


class InvalidModelsRejected(unittest.TestCase):
    def test_invalid_variances(self):
        for bad in (-1, float("nan"), float("inf"), True):
            with self.subTest(v=bad), self.assertRaises(ValueError):
                RiskOutcome(10, bad)

    def test_non_finite_mean(self):
        for bad in (float("nan"), float("inf")):
            with self.subTest(mean=bad), self.assertRaises(ValueError):
                RiskOutcome(bad, 4)

    def test_negative_gamma_or_switching_cost(self):
        with self.assertRaises(ValueError):
            RiskChoice(RiskOutcome(1, 1), RiskOutcome(2, 2), gamma=-0.5)
        with self.assertRaises(ValueError):
            RiskChoice(RiskOutcome(1, 1), RiskOutcome(2, 2), gamma=0.5, transition_cost=-1)

    def test_no_silent_boolean_as_gamma(self):
        with self.assertRaises(ValueError):
            RiskChoice(RiskOutcome(1, 1), RiskOutcome(2, 2), gamma=True)

    def test_invalid_choice_sensitivity(self):
        with self.assertRaises(ValueError):
            RiskChoice(RiskOutcome(1, 1), RiskOutcome(2, 2), gamma=0.5, choice_sensitivity=0)

    def test_no_overflow_claimed_as_valid_ce(self):
        with self.assertRaises(ValueError):
            certainty_equivalent(RiskOutcome(10, 1e308), 1e308)

    def test_reference_is_labeled_non_empirical_and_unknown_open_world(self):
        r = declared_examples()
        self.assertEqual(r["status"], "SYNTHETIC_CONDITIONAL_NOT_EMPIRICAL")
        self.assertEqual(r["outside_probabilities"], "NOT_IDENTIFIED")
        self.assertEqual(r["observed_human_suffering"], "NOT_MEASURED")
        self.assertTrue(r["late_stay_future_forecast_below_current"])
        self.assertEqual(r["early"]["preferred"], "STAY")
        self.assertEqual(r["late"]["preferred"], "STAY")
        self.assertEqual(r["early"]["mean_gain_redesign"], 6)
        self.assertEqual(r["late"]["mean_gain_redesign"], 11)


class EconomicShortfallTests(unittest.TestCase):
    def test_matched_feasible_foregone_utility(self):
        self.assertEqual(foregone_utility_gap(17, 21, justified_reference=True), 4)

    def test_better_than_reference_is_not_negative_suffering(self):
        self.assertEqual(foregone_utility_gap(23, 21, justified_reference=True), 0)

    def test_unverified_reference_is_unknown_not_zero(self):
        self.assertIsNone(foregone_utility_gap(17, 21, justified_reference=False))
        self.assertIsNone(foregone_utility_gap(17, None, justified_reference=False))

    def test_missing_reference_cannot_be_silently_imputed(self):
        with self.assertRaises(ValueError):
            foregone_utility_gap(17, None, justified_reference=True)

    def test_gaps_require_a_valid_common_utility_scale(self):
        for actual, reference in ((float("nan"), 21), (17, float("inf"))):
            with self.subTest(actual=actual, reference=reference):
                with self.assertRaises(ValueError):
                    foregone_utility_gap(actual, reference, justified_reference=True)
        with self.assertRaises(ValueError):
            foregone_utility_gap(17, 21, justified_reference=1)

    def test_not_a_measure_of_reported_discomfort_or_acc_structural_suffering(self):
        result = declared_examples()["matched_feasible_reference_example"]
        self.assertEqual(result["economic_foregone_utility"], 4)
        self.assertEqual(result["subjective_distress"], "NOT_IDENTIFIED")
        self.assertEqual(result["structural_suffering"], "NOT_IDENTIFIED")
        self.assertEqual(result["empirical_feasibility"], "STIPULATED_FOR_TOY_ONLY")


class ActiveDefenceTests(unittest.TestCase):
    def setUp(self):
        self.choice = RiskChoice(RiskOutcome(14, 4), RiskOutcome(25, 64), gamma=0.5)
        self.defense = DefencePolicy(RiskOutcome(14, 1), effort_cost=0.5)

    def test_three_actions_are_distinct_and_defense_cost_paid_once(self):
        ce = policy_certainty_equivalents(self.choice, self.defense)
        self.assertEqual(ce, {"STAY": 13, "REDESIGN": 9, "DEFEND_STAY": 13.25})
        self.assertEqual(defense_advantage_over_stay(self.choice, self.defense), 0.25)
        self.assertEqual(preferred_with_defense(self.choice, self.defense), "DEFEND_STAY")

    def test_active_defense_with_positive_discomfort_and_worse_forecast(self):
        self.assertEqual(WelfareSnapshot(30, 13).stipulated_discomfort, 13)
        self.assertLess(self.choice.stay.mean, WelfareSnapshot(30, 13).net_welfare)
        self.assertEqual(preferred_with_defense(self.choice, self.defense), "DEFEND_STAY")
        self.assertGreater(self.choice.redesign.mean, self.choice.stay.mean)

    def test_defense_without_benefit_is_strictly_dominated(self):
        pointless = DefencePolicy(RiskOutcome(14, 4), effort_cost=0.5)
        self.assertLess(defense_advantage_over_stay(self.choice, pointless), 0)
        self.assertEqual(preferred_with_defense(self.choice, pointless), "STAY")

    def test_too_costly_defense_is_rejected(self):
        costly = DefencePolicy(RiskOutcome(14, 1), effort_cost=2)
        self.assertEqual(preferred_with_defense(self.choice, costly), "STAY")

    def test_risk_neutral_evaluator_does_not_defend(self):
        neutral = RiskChoice(self.choice.stay, self.choice.redesign, gamma=0)
        self.assertEqual(preferred_with_defense(neutral, self.defense), "REDESIGN")

    def test_sufficiently_attractive_redesign_beats_defending(self):
        valuable = RiskChoice(self.choice.stay, RiskOutcome(40, 64), gamma=0.5)
        self.assertEqual(preferred_with_defense(valuable, self.defense), "REDESIGN")

    def test_equal_three_way_options_can_tie(self):
        equal = RiskChoice(RiskOutcome(10, 0), RiskOutcome(10, 0), gamma=0.5)
        zero = DefencePolicy(RiskOutcome(10, 0), effort_cost=0)
        self.assertEqual(preferred_with_defense(equal, zero), "TIE")

    def test_three_way_logit_is_conditional_choice_not_transition_success(self):
        probabilities = three_way_choice_probabilities(self.choice, self.defense)
        self.assertAlmostEqual(sum(probabilities.values()), 1)
        self.assertGreater(probabilities["DEFEND_STAY"], probabilities["STAY"])
        self.assertGreater(probabilities["STAY"], probabilities["REDESIGN"])
        self.assertNotAlmostEqual(probabilities["REDESIGN"], exit_probability(self.choice))

    def test_invalid_defense_cost_and_distribution_rejected(self):
        with self.assertRaises(ValueError):
            DefencePolicy(RiskOutcome(1, 1), effort_cost=-0.01)
        with self.assertRaises(ValueError):
            DefencePolicy(RiskOutcome(1, 1), effort_cost=float("nan"))
        with self.assertRaises(ValueError):
            DefencePolicy(None, effort_cost=0)

    def test_declared_example_demonstrates_active_defense_without_population_claim(self):
        report = declared_examples()
        self.assertEqual(report["late_with_active_defense"]["preferred"], "DEFEND_STAY")
        self.assertEqual(report["late_with_active_defense"]["defend_stay_ce_after_effort"], 13.25)
        self.assertEqual(report["status"], "SYNTHETIC_CONDITIONAL_NOT_EMPIRICAL")



if __name__ == "__main__":
    unittest.main()
