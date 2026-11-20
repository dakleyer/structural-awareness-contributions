"""Unknown or malformed flag values cannot become qualified evidence."""
from itertools import product
import unittest

from test_theme18_candidate_admission import assess_candidate, reports


VALID = {
    "received_after_exchange": True,
    "source_to_value_link_qualified": True,
    "source_value_lower_bound": .84,
    "action_authorized": True,
    "decision_budget_ok": True,
}
NON_BOOLEAN = (None, "UNKNOWN", "False", "True", 1, -1, {"value": True})


class ExplicitEvidenceFlagTests(unittest.TestCase):
    def test_non_boolean_capture_is_not_proven_observation(self):
        for value in NON_BOOLEAN:
            rows = reports()
            rows[0]["captured"] = value
            with self.subTest(captured=value):
                result = assess_candidate(rows, **VALID)
                self.assertEqual(result["candidate_status"], "UNSUPPORTED_COMMON_COMPLEMENT")
                self.assertEqual(result["execution"], "NEVER")

    def test_delivery_and_value_link_need_explicit_true(self):
        for flag, expected in (
                ("received_after_exchange", "CANDIDATE_NOT_RECEIVED"),
                ("source_to_value_link_qualified", "UTILITY_NOT_ESTABLISHED")):
            for value in NON_BOOLEAN:
                options = dict(VALID, **{flag: value})
                with self.subTest(flag=flag, value=value):
                    self.assertEqual(assess_candidate(reports(), **options)["candidate_status"],
                                     expected)

    def test_action_and_budget_remain_separate_explicit_controls(self):
        for flag, expected in (
                ("action_authorized", "ACTION_RIGHT_NOT_ESTABLISHED"),
                ("decision_budget_ok", "TRANSITION_BUDGET_NOT_ESTABLISHED")):
            for value in NON_BOOLEAN:
                options = dict(VALID, **{flag: value})
                with self.subTest(flag=flag, value=value):
                    result = assess_candidate(reports(), **options)
                    self.assertEqual(result["candidate_status"], expected)
                    self.assertEqual(result["execution"], "NEVER")

    def test_all_sixteen_boolean_flag_patterns_preserve_existing_decisions(self):
        flags = ("received_after_exchange", "source_to_value_link_qualified",
                 "action_authorized", "decision_budget_ok")
        failure = ("CANDIDATE_NOT_RECEIVED", "UTILITY_NOT_ESTABLISHED",
                   "ACTION_RIGHT_NOT_ESTABLISHED", "TRANSITION_BUDGET_NOT_ESTABLISHED")
        for values in product((False, True), repeat=4):
            expected = next((status for value, status in zip(values, failure) if not value),
                            "SCOPED_PROPOSAL_FOR_EXTERNAL_ACTION_CHECK")
            options = dict(VALID, **dict(zip(flags, values)))
            with self.subTest(values=values):
                self.assertEqual(assess_candidate(reports(), **options)["candidate_status"],
                                 expected)


if __name__ == "__main__":
    unittest.main()

