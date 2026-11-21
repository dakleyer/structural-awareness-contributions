"""Regressions for L-12's remaining source Boolean premises."""
from copy import deepcopy
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import unittest

import campaign as source

CASES = json.loads(Path(__file__).with_name("CASES.json").read_text(encoding="utf-8"))["cases"]
NONBOOLEAN = (None, "UNKNOWN", "yes", "True", "False", 0, 1, 2, 1.0, {}, {"claim": True}, [], [True])


def sample(kind):
    return deepcopy(next(c for c in CASES if c["kind"] == kind))


class RemainingExplicitPremiseTests(unittest.TestCase):
    def test_mission_unknown_is_not_a_positive_or_negative_decision(self):
        base = next(deepcopy(c) for c in CASES
                    if c["kind"] == "mission" and c["authorized_change"] is True)
        for key in ("authorized_change", "source_basis_valid"):
            for value in NONBOOLEAN:
                case = deepcopy(base)
                case[key] = value
                original = deepcopy(case)
                with self.subTest(key=key, value=repr(value)):
                    result = source.result(case)
                    self.assertEqual(result["status"], "MISSION_BASIS_NOT_ESTABLISHED")
                    self.assertIsNone(result["mission_change"])
                    self.assertEqual(case, original)

    def test_known_mission_controls_and_independence_requirement_remain_distinct(self):
        base = next(deepcopy(c) for c in CASES
                    if c["kind"] == "mission" and c["authorized_change"] is True)
        self.assertIs(source.result(base)["mission_change"], True)
        for key in ("authorized_change", "source_basis_valid"):
            case = deepcopy(base)
            case[key] = False
            result = source.result(case)
            self.assertEqual(result["status"], "UNSUPPORTED_MISSION_CHANGE")
            self.assertIs(result["mission_change"], False)
        case = deepcopy(base)
        case["actual_independent"] = 1
        self.assertIs(source.result(case)["mission_change"], False)
        for key in ("actual_independent", "authorized_change", "source_basis_valid"):
            case = deepcopy(base)
            del case[key]
            self.assertIsNone(source.result(case)["mission_change"])

    def test_unknown_q_retains_raw_qualification_and_other_cost_options(self):
        base = sample("q_cost")
        supported = source.result(base)
        for value in (False,) + NONBOOLEAN:
            case = deepcopy(base)
            case["valid_Q"] = value
            original = deepcopy(case)
            with self.subTest(value=repr(value)):
                result = source.result(case)
                self.assertIsNone(result["net_values"]["SOURCE_B"])
                self.assertEqual(result["certificate_qualified"], value)
                self.assertNotEqual(result["best_mode"], "SOURCE_B")
                for name in ("A_ONLY", "TARGETED_CONVENTIONAL", "FULL_A_EXPANSION"):
                    self.assertEqual(result["net_values"][name], supported["net_values"][name])
                self.assertEqual(case, original)

    def test_unknown_independent_evidence_does_not_advance_validation_path(self):
        base = sample("knowledge")
        for value in (False,) + NONBOOLEAN:
            case = deepcopy(base)
            case["independent_evidence"] = value
            original = deepcopy(case)
            with self.subTest(value=repr(value)):
                result = source.result(case)
                self.assertEqual(result["status"], "EVIDENCE_INSUFFICIENT_FOR_CLAIM")
                self.assertEqual(result["assertion"], case["assertion"])
                self.assertIs(result["social_fact_established"], False)
                self.assertEqual(case, original)
        base["independent_evidence"] = True
        result = source.result(base)
        self.assertEqual(result["status"], "REQUIRES_INDEPENDENT_VALIDATION")
        self.assertIs(result["social_fact_established"], False)

    def test_unknown_attribution_values_cannot_certify_consistency(self):
        base = sample("attribution")
        mapping = {"reported_dependency": "listed", "verified_dependency": "verified",
                   "assigned_credit": "credited"}
        for value in NONBOOLEAN:
            for keys in [tuple(mapping)] + [(key,) for key in mapping]:
                case = deepcopy(base)
                for key in keys:
                    case[key] = value
                original = deepcopy(case)
                with self.subTest(value=repr(value), keys=keys):
                    result = source.result(case)
                    self.assertEqual(result["status"], "ATTRIBUTION_NOT_ESTABLISHED")
                    for key, output in mapping.items():
                        self.assertEqual(result[output], case[key])
                    self.assertEqual(case, original)
        case["requested_metric"] = "E_UNRESOLVED"
        self.assertEqual(source.result(case)["status"], "MEASUREMENT_EDITION_CONFLICT_BLOCKED")

    def test_descriptive_measurement_flag_does_not_gate_hypothetical_value(self):
        case = sample("net_discomfort")
        supported = source.result(case)
        case["subjective_measured"] = "UNKNOWN"
        result = source.result(case)
        self.assertEqual(result["subjective_measured"], "UNKNOWN")
        for key in ("status", "net_welfare_toy"):
            self.assertEqual(result[key], supported[key])

    def test_all_original_boolean_gate_variants_keep_complete_results(self):
        reports = []
        kinds = ("compare", "eff_gap", "human_time", "mission", "q_cost", "knowledge", "attribution")
        for case in CASES:
            kind = case["kind"]
            if kind not in kinds:
                continue
            count = (len(case["periods"]) if kind == "eff_gap" else 2 if kind == "mission"
                     else 3 if kind == "attribution" else 1)
            for flags in product((False, True), repeat=count):
                item = deepcopy(case)
                if kind == "compare":
                    item["alternative"]["authorized"] = flags[0]
                elif kind == "eff_gap":
                    for period, flag in zip(item["periods"], flags):
                        period["feasible"] = flag
                elif kind == "mission":
                    item["authorized_change"], item["source_basis_valid"] = flags
                elif kind == "attribution":
                    item["reported_dependency"], item["verified_dependency"], item["assigned_credit"] = flags
                else:
                    key = {"human_time": "same_service", "q_cost": "valid_Q",
                           "knowledge": "independent_evidence"}[kind]
                    item[key] = flags[0]
                reports.append({"id": item["id"], "flags": flags, "result": source.result(item)})
        self.assertEqual(len(reports), 78)
        digest = sha256(json.dumps(reports, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        # Complete result dictionaries from parent #100 4070dd2.
        self.assertEqual(digest, "2da4643f3ddebd917091598669e9d8b37eab7439b6623d5afe37df59564b67dc")


if __name__ == "__main__":
    unittest.main()
