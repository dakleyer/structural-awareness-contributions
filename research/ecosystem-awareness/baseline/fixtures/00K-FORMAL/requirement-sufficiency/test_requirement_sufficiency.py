from __future__ import annotations
import json
import unittest
from dataclasses import replace
from pathlib import Path
from audit_requirement_sufficiency import assert_no_target_shortcut, certificate, support
from requirement_sufficiency_model import (
    P, R, State, p3, p6, t3_bounded_authorized_response,
    t4_viable_requalification, s9_non_substituting_composition,
    s14_evidence_to_decision, s4_human_capacity_surface, s8_nonamplification,
)

def disguised_p6(s):
    return ((s.compatibility_preserved and s.dependency_independent) or not s.composition_active)

def padded_p3(s):
    return not (s.executes and s.unresolved_material) and s.evidence_fit

def hidden_call(s):
    return p3(s)

class TestRequirementSufficiency(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = certificate()

    def test_exhaustive_outcomes_and_no_vacuous_bundles(self):
        self.assertEqual([r['implies_target'] for r in self.result['bundles']],
                         [True, True, False, True, False, False])
        for r in self.result['bundles']:
            self.assertGreater(r['conforming_projected_states'], 0)
            self.assertEqual(r['projected_states_checked'] * r['full_cube_assignments_per_row'],
                             self.result['full_state_count'])

    def test_all_clauses_have_independent_distinguishing_witnesses(self):
        for i, r in enumerate(self.result['bundles']):
            for name, result in r['clauses'].items():
                with self.subTest(principle=i + 1, clause=name):
                    self.assertFalse(result['equivalent_to_target'])
                    self.assertFalse(result['alone_implies_target'])
                    self.assertIsNotNone(result['non_equivalence_witness'])
                    self.assertIsNotNone(result['clause_without_target_witness'])

    def test_known_gaps_retain_replayable_counterexamples(self):
        for i in (2, 4, 5):
            s = State(**self.result['bundles'][i]['counterexample'])
            self.assertTrue(R[i](s))
            self.assertFalse(P[i](s))

    def test_guard_rejects_reordered_target(self):
        with self.assertRaisesRegex(AssertionError, 'equivalent'):
            assert_no_target_shortcut(disguised_p6, p6)

    def test_guard_rejects_target_padded_with_unrelated_conjunct(self):
        with self.assertRaisesRegex(AssertionError, 'alone implies'):
            assert_no_target_shortcut(padded_p3, p3)

    def test_projection_rejects_hidden_target_call(self):
        with self.assertRaisesRegex(ValueError, 'calls'):
            support(hidden_call)

    def test_t3_requires_declared_response_and_conditional_per_state_bound(self):
        s = State(executes=True, response_authorized=True, response_failure_declared=True,
                  response_reversibility_declared=True, response_externalities_declared=True,
                  response_downside_declared=True, null_action_declared=True)
        self.assertTrue(t3_bounded_authorized_response(s))
        for field in ('response_authorized', 'response_failure_declared',
                      'response_reversibility_declared', 'response_externalities_declared',
                      'response_downside_declared', 'null_action_declared'):
            self.assertFalse(t3_bounded_authorized_response(replace(s, **{field: False})))
        self.assertFalse(t3_bounded_authorized_response(replace(s, strong_response_claimed=True)))
        self.assertTrue(t3_bounded_authorized_response(
            replace(s, strong_response_claimed=True, no_worse_than_null=True)))
        self.assertTrue(t3_bounded_authorized_response(replace(s, unresolved_material=True)))

    def test_t4_tracks_horizon_cost_value_and_declared_composition_effects(self):
        s = State(bounded_progress=True, deadline_viable=True, cost_ledger_declared=True,
                  expansion_value_declared=True, composition_active=True, composition_effects_declared=True)
        self.assertTrue(t4_viable_requalification(s))
        for field in ('bounded_progress', 'deadline_viable', 'cost_ledger_declared',
                      'expansion_value_declared', 'composition_effects_declared'):
            self.assertFalse(t4_viable_requalification(replace(s, **{field: False})))
        self.assertTrue(t4_viable_requalification(replace(s, dependency_independent=False)))

    def test_s9_distinguishes_correlation_from_false_independent_support(self):
        s = State(composition_active=True, dependency_independent=False)
        self.assertTrue(s9_non_substituting_composition(s))
        self.assertFalse(s9_non_substituting_composition(replace(s, dependent_support_promoted=True)))

    def test_original_anchor_only_negative_controls(self):
        s = State(evidence_fit=True)
        self.assertTrue(s14_evidence_to_decision(s)); self.assertFalse(P[0](s))
        s = State(deadline_viable=True)
        self.assertTrue(s4_human_capacity_surface(s)); self.assertFalse(P[1](s))
        s = State(executes=True, authority_nonamplifying=True)
        self.assertTrue(s8_nonamplification(s)); self.assertFalse(P[3](s))

    def test_committed_certificate_reproduces_exactly(self):
        saved = json.loads(Path(__file__).with_name('clause_audit_certificate.json').read_text())
        self.assertEqual(saved, json.loads(json.dumps(self.result)))

if __name__ == '__main__':
    unittest.main()
