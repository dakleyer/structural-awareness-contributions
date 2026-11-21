"""Finite operands and derived values for the existing cost/credit calculations."""
from copy import deepcopy
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import unittest

import campaign as source

CASES = json.loads(Path(__file__).with_name("CASES.json").read_text(encoding="utf-8"))["cases"]
BAD_NUMBERS = (float("nan"), float("inf"), float("-inf"), True, False,
               None, "UNKNOWN", "1", {}, [])


def sample(kind):
    return deepcopy(next(c for c in CASES if c["kind"] == kind))


class FiniteCostCreditTests(unittest.TestCase):
    def test_every_consumed_cost_rejects_nonfinite_or_nonnumeric_values(self):
        base = sample("q_cost")
        self.assertIs(base["valid_Q"], True)
        for key in ("qualified_cost", "targeted_cost", "full_cost"):
            for value in BAD_NUMBERS:
                case = deepcopy(base)
                case[key] = value
                with self.subTest(key=key, value=repr(value)):
                    with self.assertRaisesRegex(ValueError, key):
                        source.result(case)
                    self.assertIs(case[key], value)

    def test_unavailable_q_cost_does_not_block_other_known_options(self):
        for flag in (False, None, "UNKNOWN", 1):
            base = sample("q_cost")
            base["valid_Q"] = flag
            supported = source.result(base)
            for value in BAD_NUMBERS:
                case = deepcopy(base)
                case["qualified_cost"] = value
                with self.subTest(flag=repr(flag), value=repr(value)):
                    result = source.result(case)
                    self.assertEqual(result, supported)
                    self.assertIsNone(result["net_values"]["SOURCE_B"])
                    self.assertEqual(result["certificate_qualified"], flag)
                    self.assertIs(case["qualified_cost"], value)

    def test_each_utility_delta_must_be_finite_before_pareto_comparison(self):
        base = sample("distribution")
        for index in range(len(base["delta_utils"])):
            for value in BAD_NUMBERS:
                case = deepcopy(base)
                case["delta_utils"][index] = value
                with self.subTest(index=index, value=repr(value)):
                    with self.assertRaisesRegex(ValueError, "delta_utils"):
                        source.result(case)
                    self.assertIs(case["delta_utils"][index], value)

    def test_overflowing_derived_net_cannot_become_a_winner(self):
        for key, mode in (("qualified_cost", "SOURCE_B"),
                          ("targeted_cost", "TARGETED_CONVENTIONAL"),
                          ("full_cost", "FULL_A_EXPANSION")):
            case = sample("q_cost")
            case["decision_value"] = 1e308
            case[key] = -1e308
            with self.subTest(key=key):
                with self.assertRaisesRegex(ValueError, mode):
                    source.result(case)

    def test_overflowing_total_credit_demand_is_not_reported_as_a_number(self):
        case = sample("distribution")
        case["credit_total"] = 1e308
        case["credit_minimums"] = [1e308, 1e308]
        case["delta_utils"] = [0, 0]
        with self.assertRaisesRegex(ValueError, "credit_demand"):
            source.result(case)

    def test_finite_zero_negative_and_positive_controls_keep_complete_results(self):
        reports = []
        for case in CASES:
            if case["kind"] == "q_cost":
                for flag in (False, True):
                    for costs in product((-8, -.25, 0, .25, 8), repeat=3):
                        item = deepcopy(case)
                        item["valid_Q"] = flag
                        item["qualified_cost"], item["targeted_cost"], item["full_cost"] = costs
                        reports.append({"id": item["id"], "flag": flag, "costs": costs,
                                        "result": source.result(item)})
            elif case["kind"] == "distribution":
                for utils in product((-3, -.5, 0, .5, 3), repeat=len(case["delta_utils"])):
                    item = deepcopy(case)
                    item["delta_utils"] = list(utils)
                    reports.append({"id": item["id"], "utils": utils,
                                    "result": source.result(item)})
        self.assertEqual(len(reports), 1075)
        digest = sha256(json.dumps(reports, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        # Full result dictionaries from captured parent #102 e6bd3a7.
        self.assertEqual(digest, "549eda8990bffdb6e7eb35d335834c3ea07e4cf1c82e21109cb2601318a95069")


if __name__ == "__main__":
    unittest.main()
