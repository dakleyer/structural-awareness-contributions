"""Resource conservation must follow component values, not a repeated total label."""
from copy import deepcopy
from hashlib import sha256
import json
from types import SimpleNamespace
from unittest.mock import patch
import unittest

import l08_agentic_adapter as adapter

REAL_SOURCE = adapter._load_native(adapter.SOURCE / "agentic_reduction.py")


def altered_source(change):
    def run_case(case):
        result = deepcopy(REAL_SOURCE.run_case(case))
        change(result["arms"]["A_ONLY"]["observed_by_referee_only"])
        return result
    return SimpleNamespace(ARMS=REAL_SOURCE.ARMS, SCHEMA=REAL_SOURCE.SCHEMA,
                           run_case=run_case)


class ComponentConservationTests(unittest.TestCase):
    def test_creation_in_components_is_rejected_even_when_total_label_matches(self):
        def create_resource(row):
            row["donor_resources_after"] += 1
        with patch.object(adapter, "_load_native", return_value=altered_source(create_resource)):
            with self.assertRaisesRegex(AssertionError, "resource"):
                adapter.run()

    def test_invalid_component_values_cannot_claim_conservation(self):
        for invalid in (None, True, float("nan"), float("inf"), -1):
            with self.subTest(value=invalid):
                def corrupt(row):
                    row["recipient_resources_after"] = invalid
                with patch.object(adapter, "_load_native", return_value=altered_source(corrupt)):
                    with self.assertRaises((ValueError, AssertionError)):
                        adapter.run()

    def test_rounding_from_original_four_decimal_contract_remains_allowed(self):
        # Compatible with unrounded 6.00006 + 3.99988 + .00006 = 10.
        adapter._check_resource_conservation(
            {"total_resources": 10},
            {"donor_resources_after": 6.0001,
             "recipient_resources_after": 3.9999,
             "coordination_resources_spent": .0001,
             "total_resources_same": 10})

    def test_every_original_source_result_is_unchanged(self):
        result = adapter.run()
        result.pop("source_sha256")
        digest = sha256(json.dumps(result, sort_keys=True,
                                  separators=(",", ":")).encode()).hexdigest()
        self.assertEqual(digest, "05818b29f210ab6fc7ebbb8d125138f5a0e3fadc5c4cfd9c7cb4b02042a2bafa")


if __name__ == "__main__":
    unittest.main()

