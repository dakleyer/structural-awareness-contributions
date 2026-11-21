"""Known arrival metadata is required before temporal cartographic claims."""
from copy import deepcopy
from dataclasses import replace
from decimal import Decimal
from fractions import Fraction
import unittest

import residual_cartography_stage as source


def event():
    return source.example_events()[-1]


class CartographicArrivalMetadataTests(unittest.TestCase):
    def test_unknown_or_noninteger_time_is_rejected_before_sorting_or_history_claims(self):
        for invalid in (None, True, False, float("nan"), float("inf"),
                        -float("inf"), Decimal("NaN"), Decimal("Infinity"),
                        "7", 7.0, Fraction(7), [], {}):
            bad = replace(event(), time=invalid)
            for observations in ((bad,), (replace(event(), time=1), bad),
                                 (replace(event(), time=7), bad)):
                with self.subTest(value=repr(invalid), events=len(observations)):
                    with self.assertRaisesRegex(ValueError, "integer tick"):
                        source.three_stages(events=observations)

    def test_unnamed_event_identity_cannot_support_local_or_temporal_evidence(self):
        for invalid in (None, True, 1, "", "   ", "\t", [], {}):
            observation = replace(event(), event_id=invalid)
            with self.subTest(value=repr(invalid)):
                self.assertEqual(source.local_claim(observation, 0)["finding"],
                                 "UNKNOWN_BAD_OR_UNCAPTURED_INPUT")
                verdict = source.qualified_event(observation, required_scope=source.CROSS_SOURCE_SCOPE)
                self.assertFalse(verdict["joint_region"])
                self.assertEqual(verdict["reason"], "INVALID_EVENT_ID")
                with self.assertRaisesRegex(ValueError, "event_id"):
                    source.three_stages(events=(observation,))

    def test_exact_integer_boundary_and_pre_exchange_history_are_preserved(self):
        cutoff = source.META_EXCHANGE_TIME
        for time in (-1, 0, cutoff - 1, cutoff, cutoff + 1, 2**64):
            result = source.three_stages(events=(replace(event(), time=time),))
            history = result["stage_2_source_cartography"]
            with self.subTest(time=time):
                if time <= cutoff:
                    self.assertIsNone(result["candidate_event_id"])
                    self.assertEqual(history["prior_qualified_hit_ids"], [event().event_id])
                    self.assertFalse(history["no_matched_event_as_of_meta_exchange"])
                else:
                    self.assertEqual(result["candidate_event_id"], event().event_id)
                    self.assertEqual(history["prior_qualified_hit_ids"], [])
                    self.assertTrue(history["no_matched_event_as_of_meta_exchange"])
                    self.assertEqual(result["stage_3"]["observed_by_referee_only"]["output"], 11.5)

    def test_unknown_arrival_does_not_erase_atemporal_cartographic_information(self):
        for time in (float("nan"), float("inf")):
            observation = replace(event(), time=time)
            with self.subTest(time=repr(time)):
                verdict = source.qualified_event(observation, required_scope=source.CROSS_SOURCE_SCOPE)
                self.assertTrue(verdict["joint_region"])
                self.assertEqual(verdict["meta_label"], "COMMON_RESIDUAL_CANDIDATE")
                with self.assertRaisesRegex(ValueError, "integer tick"):
                    source.three_stages(events=(observation,))

    def test_literal_valid_event_names_survive_without_normalization(self):
        for name in ("1", "01", " event ", "evento-ñ"):
            observation = replace(event(), event_id=name, first_capture_observer_id=None)
            result = source.three_stages(events=(observation,))
            with self.subTest(name=name):
                self.assertEqual(result["candidate_event_id"], name)
                self.assertEqual(result["stage_3_meta_syntax_message"]["event_id"], name)
                self.assertIsNone(result["first_capture_observer_id"])
                self.assertEqual(result["stage_3"]["observed_by_referee_only"]["output"], 11.5)

    def test_claim_join_rejects_unnamed_event_identity_before_hashing(self):
        claims = [source.local_claim(event(), i) for i in range(source.N_OBSERVERS)]
        for invalid in (None, True, 1, "", "   ", [], {}):
            modified = deepcopy(claims)
            for claim in modified:
                claim["event_id"] = invalid
            with self.subTest(value=repr(invalid)):
                verdict = source.common_cartographic_label(
                    modified, source_scope=source.CROSS_SOURCE_SCOPE)
                self.assertFalse(verdict["joint_region"])
                self.assertEqual(verdict["reason"], "INVALID_EVENT_ID")


if __name__ == "__main__":
    unittest.main()
