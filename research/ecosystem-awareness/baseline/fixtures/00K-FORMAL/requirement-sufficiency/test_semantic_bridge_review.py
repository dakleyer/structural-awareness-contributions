import json
import unittest
from pathlib import Path
from semantic_bridge_review import (Action, certificate, false_corroboration,
                                   qualified_response, replay, stale_executions)


class SemanticBridgeReview(unittest.TestCase):
    def test_historical_counterexamples_survive(self):
        for row in certificate()['historical_counterexamples_retained'].values():
            self.assertTrue(row['bundle'])
            self.assertFalse(row['target'])

    def test_scoped_response_is_not_false_continuation(self):
        rows = certificate()['P3_diagnostic']
        self.assertTrue(rows['response']['permitted_by_partial_policy'])
        self.assertFalse(rows['continuation']['permitted_by_partial_policy'])

    def test_response_label_does_not_override_own_missing_basis_or_authority(self):
        action = Action('stop', frozenset({'stop_available'}), frozenset({'stop'}))
        self.assertFalse(qualified_response(action, frozenset({'stop_available'}), frozenset()))
        other = Action('stop', frozenset({'stop_available'}), frozenset({'continue'}))
        self.assertFalse(qualified_response(other, frozenset(), frozenset({'stop_available'})))

    def test_dependence_only_fails_when_promoted(self):
        roots = {'a': 'same', 'b': 'same'}
        self.assertFalse(false_corroboration(roots, ()))
        self.assertTrue(false_corroboration(roots, (('a', 'b'),)))
        self.assertFalse(false_corroboration({'a': 'one', 'b': 'two'}, (('a', 'b'),)))

    def test_recording_change_is_not_requalification(self):
        events = ('qualify', 'change', 'record', 'act')
        self.assertFalse(replay(events)[-1]['executed'])
        self.assertEqual(stale_executions(events, replay(events, False)), [3])

    def test_requalification_must_follow_latest_change(self):
        self.assertTrue(replay(('qualify', 'change', 'qualify', 'act'))[-1]['executed'])
        self.assertFalse(replay(('qualify', 'change', 'qualify', 'change', 'act'))[-1]['executed'])

    def test_bounded_enumeration_is_nonvacuous_and_detects_missing_interlock(self):
        row = certificate()['P5_bounded_enumeration']
        self.assertEqual(row['traces_checked'], sum(4**i for i in range(1, 7)))
        self.assertEqual(row['stale_execution_traces_with_interlock'], 0)
        self.assertGreater(row['traces_with_permitted_execution'], 0)
        self.assertGreater(row['stale_execution_traces_when_interlock_removed'], 0)

    def test_unknown_event_fails_closed(self):
        with self.assertRaises(ValueError):
            replay(('approval',))

    def test_certificate_is_reproducible(self):
        saved = json.loads(Path(__file__).with_name('semantic_bridge_certificate.json').read_text())
        self.assertEqual(saved, json.loads(json.dumps(certificate())))


if __name__ == '__main__':
    unittest.main()
