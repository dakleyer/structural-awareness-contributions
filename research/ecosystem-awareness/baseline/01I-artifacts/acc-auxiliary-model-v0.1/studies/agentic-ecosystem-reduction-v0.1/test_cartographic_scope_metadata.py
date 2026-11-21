"""Named scope binding preserves local information without guessing provenance."""
from copy import deepcopy
from dataclasses import replace
import unittest

import residual_cartography_stage as source


def event():
    return source.example_events()[-1]


INVALID = (None, True, False, 0, 1, "", "   ", "\t", [], {})


class CartographicScopeMetadataTests(unittest.TestCase):
    def test_matching_unnamed_scopes_cannot_qualify_a_joint_context(self):
        for invalid in INVALID:
            with self.subTest(scope=repr(invalid)):
                observation = replace(event(), source_scope=invalid)
                verdict = source.qualified_event(observation, required_scope=invalid)
                self.assertFalse(verdict["joint_region"])
                self.assertEqual(verdict["reason"], "INVALID_SOURCE_SCOPE")

    def test_receiver_scope_must_be_named_even_when_local_source_is_known(self):
        for invalid in INVALID:
            with self.subTest(scope=repr(invalid)):
                verdict = source.qualified_event(event(), required_scope=invalid)
                self.assertFalse(verdict["joint_region"])
                self.assertEqual(verdict["reason"], "INVALID_SOURCE_SCOPE")

    def test_unknown_scope_is_rejected_before_temporal_history_inference(self):
        for invalid in INVALID:
            bad = replace(event(), time=1, source_scope=invalid)
            for observations in ((bad,), (event(), bad), (bad, event())):
                with self.subTest(scope=repr(invalid), events=len(observations)):
                    original = deepcopy(observations)
                    with self.assertRaisesRegex(ValueError, "source_scope"):
                        source.three_stages(events=observations)
                    self.assertEqual(observations, original)

    def test_arbitrary_named_scopes_and_known_scope_mismatches_are_preserved(self):
        for name in ("other-scope", " scope ", "ámbito-ñ"):
            observation = replace(event(), time=1, source_scope=name)
            with self.subTest(scope=name):
                self.assertTrue(source.qualified_event(
                    observation, required_scope=name)["joint_region"])
                verdict = source.qualified_event(
                    observation, required_scope=source.CROSS_SOURCE_SCOPE)
                self.assertFalse(verdict["joint_region"])
                self.assertEqual(verdict["reason"], "SOURCE_OR_EVENT_MISMATCH")
                result = source.three_stages(events=(observation, event()))
                self.assertEqual(result["candidate_event_id"], event().event_id)
                self.assertEqual(result["stage_2_source_cartography"]["prior_qualified_hit_ids"], [])
                self.assertEqual(result["stage_3"]["observed_by_referee_only"]["output"], 11.5)

    def test_claim_join_rejects_unnamed_scope_before_hashing(self):
        claims = [source.local_claim(event(), i) for i in range(source.N_OBSERVERS)]
        for invalid in INVALID:
            modified = deepcopy(claims)
            for claim in modified:
                claim["source_scope"] = invalid
            with self.subTest(scope=repr(invalid)):
                verdict = source.common_cartographic_label(
                    modified, source_scope=source.CROSS_SOURCE_SCOPE)
                self.assertFalse(verdict["joint_region"])
                self.assertEqual(verdict["reason"], "INVALID_SOURCE_SCOPE")

    def test_unknown_scope_preserves_local_predicates_and_geometric_information(self):
        observation = replace(event(), source_scope=None)
        claims = [source.local_claim(observation, i) for i in range(source.N_OBSERVERS)]
        self.assertTrue(all(c["finding"] == "CERTIFIED_OUTSIDE_LOCAL_A" for c in claims))
        self.assertTrue(all(c["source_scope"] is None for c in claims))
        self.assertEqual(source.geometric_referee_value(observation.features), 0.98125)
        self.assertFalse(source.qualified_event(
            observation, required_scope=source.CROSS_SOURCE_SCOPE)["joint_region"])
        known = replace(event(), first_capture_observer_id=None)
        result = source.three_stages(events=(known,))
        self.assertIsNone(result["first_capture_observer_id"])
        self.assertEqual(result["stage_3"]["observed_by_referee_only"]["output"], 11.5)


if __name__ == "__main__":
    unittest.main()
