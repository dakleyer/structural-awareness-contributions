"""New Theme 18/RA/EA candidate-admission miniature (Stage A, Python stdlib).

This test is an independently *reconstructed* semantic fixture following SA
residual logic and the PR57 research overlay. It does NOT import PR57's branch,
run a true RA detector, authenticate sources, broadcast rules, validate a real
collective-choice system or provide action authority.
"""
from __future__ import annotations

import itertools
import unittest

SOURCES = tuple("observer-" + str(i) for i in range(4))
THRESHOLD = 0.6
CURRENT_GEOMETRY_VALUE = 0.75
# Geometry is its own synthetic illustrative utility, NOT AG01 throughput.


def score_geometry(features):
    if len(features) != 4 or any(not 0.0 <= x <= 1.0 for x in features):
        raise ValueError("invalid geometry")
    return 1.0 - sum((1.0 - x) ** 2 for x in features) / 4.0


def reports(event="e7", scope="vendor-ecosystem-v1",
            values=(0.90, 0.85, 0.80, 0.95)):
    """Source labels are fixture assumptions; not signed attestations."""
    return [{"observer_id": SOURCES[i], "event_id": event, "scope": scope,
             "captured": True,
             "finding": "CERTIFIED_OUTSIDE_LOCAL_A" if v > THRESHOLD
             else "IN_LOCAL_A"} for i, v in enumerate(values)]


def qualified_common_rejection(rows, event, scope):
    """Only explicit, captured local admission rejections may be intersected."""
    if len(rows) != 4:
        return False, "INCOMPLETE"
    if {r["observer_id"] for r in rows} != set(SOURCES):
        return False, "MISSING_OR_DUPLICATE_OBSERVER"
    if any(r["event_id"] != event or r["scope"] != scope
           for r in rows):
        return False, "EVENT_OR_SCOPE_MISMATCH"
    if any(not r["captured"] or
           r["finding"] != "CERTIFIED_OUTSIDE_LOCAL_A"
           for r in rows):
        return False, "NEGATIVE_ADMISSION_NOT_PROVEN"
    return True, "COMMON_ADMISSION_COMPLEMENT"


def assess_candidate(rows, *,
                     event="e7",
                     scope="vendor-ecosystem-v1",
                     received_after_exchange=False,
                     source_to_value_link_qualified=False,
                     source_value_lower_bound=None,
                     action_authorized=False,
                     decision_budget_ok=False):
    valid, why = qualified_common_rejection(rows, event, scope)
    # No inference of RA change, actual benefit, or new operator from a
    # common admission complement. This is not the RA/EA/ITU runtime.
    result = {"admission_region": why, "regime_signal": None,
              "operator_changed": False, "execution": "NEVER"}
    if not valid:
        result["candidate_status"] = "UNSUPPORTED_COMMON_COMPLEMENT"
    elif not received_after_exchange:
        result["candidate_status"] = "CANDIDATE_NOT_RECEIVED"
    elif not source_to_value_link_qualified or source_value_lower_bound is None:
        result["candidate_status"] = "UTILITY_NOT_ESTABLISHED"
    elif source_value_lower_bound <= CURRENT_GEOMETRY_VALUE:
        result["candidate_status"] = "NO_CERTIFIED_STRICT_VALUE_GAIN"
    elif not action_authorized:
        result["candidate_status"] = "ACTION_RIGHT_NOT_ESTABLISHED"
    elif not decision_budget_ok:
        result["candidate_status"] = "TRANSITION_BUDGET_NOT_ESTABLISHED"
    else:
        result["candidate_status"] = "SCOPED_PROPOSAL_FOR_EXTERNAL_ACTION_CHECK"
    return result


class CandidateAdmissionResearchChecks(unittest.TestCase):
    def test_positive_region_is_set_relation_only(self):
        valid, reason = qualified_common_rejection(
            reports(), "e7", "vendor-ecosystem-v1")
        self.assertTrue(valid)
        self.assertEqual(reason, "COMMON_ADMISSION_COMPLEMENT")
        self.assertAlmostEqual(score_geometry((.9, .85, .8, .95)), .98125)
        self.assertAlmostEqual(1.0 - (1.0 - THRESHOLD) ** 2, .84)

    def test_all_16_threshold_patterns(self):
        for bits in itertools.product((0.5, 0.9), repeat=4):
            with self.subTest(bits=bits):
                yes, _ = qualified_common_rejection(
                    reports(values=bits), "e7", "vendor-ecosystem-v1")
                self.assertEqual(yes, all(x > THRESHOLD for x in bits))

    def test_unknown_is_not_negative(self):
        r = reports()
        r[2]["finding"] = "UNKNOWN"
        self.assertEqual(assess_candidate(r)["candidate_status"],
                         "UNSUPPORTED_COMMON_COMPLEMENT")

    def test_duplicate_source_not_four_independent_observers(self):
        r = reports()
        r[3]["observer_id"] = "observer-2"
        self.assertEqual(assess_candidate(r)["candidate_status"],
                         "UNSUPPORTED_COMMON_COMPLEMENT")

    def test_different_event_or_scope_fails(self):
        for key, value in (("event_id", "e8"), ("scope", "another")):
            r = reports()
            r[0][key] = value
            self.assertEqual(assess_candidate(r)["candidate_status"],
                             "UNSUPPORTED_COMMON_COMPLEMENT")

    def test_no_candidate_received_has_no_execution(self):
        result = assess_candidate(
            reports(), source_to_value_link_qualified=True,
            source_value_lower_bound=.84, action_authorized=True,
            decision_budget_ok=True)
        self.assertEqual(result["candidate_status"], "CANDIDATE_NOT_RECEIVED")
        self.assertEqual(result["execution"], "NEVER")
        self.assertIsNone(result["regime_signal"])

    def test_positive_bound_requires_independent_link(self):
        result = assess_candidate(
            reports(), received_after_exchange=True,
            source_value_lower_bound=.84, action_authorized=True,
            decision_budget_ok=True)
        self.assertEqual(result["candidate_status"], "UTILITY_NOT_ESTABLISHED")

    def test_same_candidate_is_not_better_without_positive_bound(self):
        result = assess_candidate(
            reports(), received_after_exchange=True,
            source_to_value_link_qualified=True,
            source_value_lower_bound=.5, action_authorized=True,
            decision_budget_ok=True)
        self.assertEqual(result["candidate_status"],
                         "NO_CERTIFIED_STRICT_VALUE_GAIN")

    def test_source_qualification_cannot_mint_authority(self):
        result = assess_candidate(
            reports(), received_after_exchange=True,
            source_to_value_link_qualified=True,
            source_value_lower_bound=.84, action_authorized=False,
            decision_budget_ok=True)
        self.assertEqual(result["candidate_status"], "ACTION_RIGHT_NOT_ESTABLISHED")

    def test_budget_still_needed(self):
        result = assess_candidate(
            reports(), received_after_exchange=True,
            source_to_value_link_qualified=True,
            source_value_lower_bound=.84, action_authorized=True,
            decision_budget_ok=False)
        self.assertEqual(result["candidate_status"],
                         "TRANSITION_BUDGET_NOT_ESTABLISHED")

    def test_bounded_proposal_not_automatic_action(self):
        result = assess_candidate(
            reports(), received_after_exchange=True,
            source_to_value_link_qualified=True,
            source_value_lower_bound=.84, action_authorized=True,
            decision_budget_ok=True)
        self.assertEqual(result["candidate_status"],
                         "SCOPED_PROPOSAL_FOR_EXTERNAL_ACTION_CHECK")
        self.assertFalse(result["operator_changed"])
        self.assertIsNone(result["regime_signal"])
        self.assertEqual(result["execution"], "NEVER")

    def test_strong_peer_with_same_evidence_ties(self):
        args = dict(received_after_exchange=True,
                    source_to_value_link_qualified=True,
                    source_value_lower_bound=.84, action_authorized=True,
                    decision_budget_ok=True)
        # Correct tie for identical algorithm and evidence; does not prove
        # one architecture superior (or test adaptation cost).
        self.assertEqual(assess_candidate(reports(), **args),
                         assess_candidate(reports(), **args))


if __name__ == "__main__":
    unittest.main(verbosity=2)
