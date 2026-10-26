"""Positive and negative controls for bounded nested compositional ambiguity."""
import unittest

from nested_model import (
    ProducerWorld, HumanDevelopmentCandidate, current_handoff,
    full_state_joint_capacity, receiver_only_decision_classes,
    agent_unilateral_reachability, structural_suffering_proxy, branch_profiles,
    current_nested_output, hierarchical_current_output, minimum_interface_bits_for_total_future,
    answer_future_branch, distinct_future_answer_profiles,
    minimum_interface_bits_for_all_branch_queries, capacity_counterexample,
    cnf_satisfiable, report,
)


class FiberAndReachability(unittest.TestCase):
    def test_same_A_different_joint_potential(self):
        x, y = ProducerWorld(False), ProducerWorld(True)
        self.assertEqual(current_handoff(x), current_handoff(y))
        self.assertEqual((8, 10), (full_state_joint_capacity(x), full_state_joint_capacity(y)))

    def test_receiver_cannot_reconstruct_from_same_A(self):
        self.assertEqual(receiver_only_decision_classes([ProducerWorld(False), ProducerWorld(True)])[(8,8)], {8,10})

    def test_if_only_one_world_no_ambiguity(self):
        self.assertEqual(receiver_only_decision_classes([ProducerWorld(True)])[(8,8)], {10})

    def test_binary_unilateral_trap(self):
        p=agent_unilateral_reachability()
        self.assertEqual(p['unilateral_successors'], [])
        self.assertEqual(p['joint_pareto_superior'], (1,1))

    def test_abstracting_rational_trap_does_not_prove_incomputability(self):
        self.assertEqual(len(agent_unilateral_reachability()['states']), 2)

class StipulatedSuffering(unittest.TestCase):
    def p(self, **changes):
        data=dict(actual_genuine_contribution=8,
                  demonstrated_jointly_feasible_contribution=10,
                  positive_contribution_to_others=True,
                  blocked_without_unilateral_control=True,
                  evidence_of_epistemic_insufficiency=True,
                  rights_and_mission_preserved=True)
        data.update(changes)
        return HumanDevelopmentCandidate(**data)

    def test_all_three_conditions_meet_proxy(self):
        r=structural_suffering_proxy(self.p())
        self.assertEqual(r['structural_suffering_proxy'],2.0)
        self.assertEqual(r['subjective_suffering'],'NOT_MEASURED')

    def test_unknown_feasible_optimum_is_not_zero(self):
        r=structural_suffering_proxy(self.p(demonstrated_jointly_feasible_contribution=None))
        self.assertEqual(r['status'],'NOT_IDENTIFIED')
        self.assertIsNone(r['structural_development_gap'])

    def test_no_positive_external_contribution_fails_three_part_definition(self):
        self.assertEqual(structural_suffering_proxy(self.p(positive_contribution_to_others=False))['structural_suffering_proxy'],0)

    def test_no_external_block_fails_three_part_definition(self):
        self.assertEqual(structural_suffering_proxy(self.p(blocked_without_unilateral_control=False))['structural_suffering_proxy'],0)

    def test_no_epistemic_insufficiency_fails_three_part_definition(self):
        self.assertEqual(structural_suffering_proxy(self.p(evidence_of_epistemic_insufficiency=False))['structural_suffering_proxy'],0)

    def test_rights_not_preserved_fails(self):
        self.assertEqual(structural_suffering_proxy(self.p(rights_and_mission_preserved=False))['structural_suffering_proxy'],0)

    def test_no_gap_not_suffering(self):
        self.assertEqual(structural_suffering_proxy(self.p(demonstrated_jointly_feasible_contribution=8))['status'],'CRITERIA_NOT_ALL_MET')

    def test_unknown_epistemic_status_not_zero(self):
        self.assertEqual(structural_suffering_proxy(self.p(evidence_of_epistemic_insufficiency=None))['status'],'NOT_IDENTIFIED')

    def test_infinite_reference_not_accepted(self):
        with self.assertRaises(ValueError):
            structural_suffering_proxy(self.p(demonstrated_jointly_feasible_contribution=float('inf')))

    def test_infinite_actual_not_accepted(self):
        with self.assertRaises(ValueError):
            structural_suffering_proxy(self.p(actual_genuine_contribution=float('inf')))

    def test_invalid_negative_contribution(self):
        with self.assertRaises(ValueError):
            structural_suffering_proxy(self.p(actual_genuine_contribution=-1))

class NestedInterface(unittest.TestCase):
    def test_all_current_A_equal_for_all_profiles(self):
        for n in range(1,7):
            self.assertEqual({current_nested_output(p) for p in branch_profiles(n)}, {8*n})

    def test_recursive_composition_matches_flat_current_observation(self):
        for n in range(1,7):
            for p in branch_profiles(n):
                self.assertEqual(hierarchical_current_output(p), current_nested_output(p))

    def test_aggregate_query_uses_fewer_bits_than_individual_queries(self):
        self.assertEqual(minimum_interface_bits_for_total_future(4), 3)
        self.assertEqual(minimum_interface_bits_for_total_future(6), 3)
        self.assertLess(minimum_interface_bits_for_total_future(6),
                        minimum_interface_bits_for_all_branch_queries(6))

    def test_recursive_observation_at_future_input_differs(self):
        self.assertEqual(hierarchical_current_output([8,10], request=10),18)
        self.assertEqual(hierarchical_current_output([10,10], request=10),20)

    def test_future_query_witness_is_distinct(self):
        self.assertNotEqual(answer_future_branch((8,10),0), answer_future_branch((10,8),0))

    def test_independent_query_profiles_expand_exponentially(self):
        for n in range(1,7):
            self.assertEqual(len(distinct_future_answer_profiles(n)), 2**n)

    def test_minimum_bits_for_all_queries_grows_linearly(self):
        for n in range(1,7):
            self.assertEqual(minimum_interface_bits_for_all_branch_queries(n), n)

    def test_no_exterior_cardinality_claim(self):
        self.assertEqual(report()['undetermined_open_exterior'],'NOT_ENUMERATED_OR_QUANTIFIED')

    def test_invalid_profile_rejected(self):
        with self.assertRaises(ValueError):
            current_nested_output([7])

    def test_bound_n(self):
        with self.assertRaises(ValueError):
            capacity_counterexample(13)

class LocalClausesComplexSearch(unittest.TestCase):
    def test_boolean_satisfiable(self):
        self.assertTrue(cnf_satisfiable(3,[(1,2,3),(-1,2),(-2,3)])[0])

    def test_boolean_unsatisfiable(self):
        self.assertFalse(cnf_satisfiable(1,[(1,),(-1,)])[0])

    def test_invalid_clause(self):
        with self.assertRaises(ValueError):
            cnf_satisfiable(2,[(3,)])

    def test_report_consistent(self):
        r=report()
        self.assertEqual(r['nested_capacity_cases'][-1]['min_exact_message_bits_for_all_branch_queries'],6)
        self.assertEqual(r['structural_human_analogue']['subjective_suffering'],'NOT_MEASURED')

if __name__=='__main__':
    unittest.main()
