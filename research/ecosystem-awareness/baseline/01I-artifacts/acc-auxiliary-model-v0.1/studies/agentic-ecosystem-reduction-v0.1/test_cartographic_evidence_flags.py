"""Explicit evidence flags in the downstream cartographic overlay."""
from dataclasses import replace
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import unittest

import residual_cartography_stage as source

HERE = Path(__file__).resolve().parent


def event(captured=True):
    return source.Observation("paired-source-event", 7, source.CROSS_SOURCE_SCOPE,
                              (.9, .85, .8, .95), captured_before_admission=captured)


class ExplicitCartographicEvidenceTests(unittest.TestCase):
    def test_unestablished_capture_never_supplies_negative_local_evidence(self):
        for invalid in (None, "UNKNOWN", "yes", 1, 2, {}, {"captured": True}, [], [True]):
            with self.subTest(value=repr(invalid)):
                observation = event(invalid)
                for index in range(source.N_OBSERVERS):
                    claim = source.local_claim(observation, index)
                    self.assertEqual(claim["finding"], "UNKNOWN_BAD_OR_UNCAPTURED_INPUT")
                result = source.three_stages(events=(observation,))
                self.assertIsNone(result["candidate_event_id"])
                self.assertIsNone(result["stage_3_meta_syntax_message"])
                self.assertEqual(result["stage_3"], result["stage_2"])

    def test_unestablished_class_link_retains_candidate_but_cannot_enable_transfer(self):
        for invalid in (None, "UNKNOWN", "yes", 1, 2, {"qualified": True}, [True]):
            with self.subTest(value=repr(invalid)):
                result = source.three_stages(events=(event(),),
                                            assumed_class_to_q_source_valid=invalid)
                self.assertEqual(result["candidate_event_id"], "paired-source-event")
                self.assertEqual(result["stage_3"], result["stage_2"])
                self.assertEqual(result["stage_3_meta_syntax_message"]["accepted_ordinary_action"],
                                 "NO_ACTION_ALLOWED")
                self.assertEqual(result["new_source_class_to_q_link_is_synthetic_assumption"],
                                 invalid)

    def test_missing_first_capture_identity_remains_explicit_without_rejecting_event(self):
        result = source.three_stages(events=(event(),))
        self.assertIsNone(result["first_capture_observer_id"])
        self.assertIsNone(result["stage_3_meta_syntax_message"]["first_capture_observer_id"])
        self.assertEqual(result["candidate_event_id"], "paired-source-event")
        self.assertEqual(result["stage_3"]["observed_by_referee_only"]["output"], 11.5)

    def test_complete_original_example_report_is_preserved(self):
        report = source.main()
        digest = sha256(json.dumps(report, sort_keys=True,
                                  separators=(",", ":")).encode()).hexdigest()
        self.assertEqual(digest, "d484073be0dafc1fefe4d7f8d4bda5ca23604e6c4f07cf3a5f37ed7f1dc1f4a7")

    def test_all_30_source_cases_and_four_boolean_combinations_are_preserved(self):
        cases = json.loads((HERE / "CASES.json").read_text(encoding="utf-8"))["cases"]
        reports = [
            {"case":case["id"], "captured":captured, "link":linked,
             "report":source.three_stages(case_id=case["id"], events=(
                 replace(event(captured), source_scope=case["public"]["scope"]),),
                 assumed_class_to_q_source_valid=linked)}
            for case in cases for captured, linked in product((False, True), repeat=2)
        ]
        self.assertEqual(len(reports), 120)
        # Full reports from unmodified parent #57 a989404, not selected fields.
        digest = sha256(json.dumps(reports, sort_keys=True,
                                  separators=(",", ":")).encode()).hexdigest()
        self.assertEqual(digest, "bbac109a928ca286333dbad621957a27e44b723a56e1057a78c3ccf7a36b3974")


if __name__ == "__main__":
    unittest.main()
