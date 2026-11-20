"""Dimensional identities must remain distinct through report serialization."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import unittest

from dimensional_contract import compare_dimensions
from strategic_choice import run_manifest

HERE = Path(__file__).resolve().parent


class DimensionalIdentityTests(unittest.TestCase):
    def test_numeric_and_text_component_keys_cannot_collapse_in_json(self):
        before = {"R": {"unit": "actor_payoff", "components": {1: "3", "1": "3"}}}
        after = {"R": {"unit": "actor_payoff", "components": {1: "4", "1": "2"}}}
        with self.assertRaisesRegex(ValueError, "identity"):
            compare_dimensions(before, after, declared_directions={"R": "INCREASE"})

    def test_dimensions_components_and_unknowns_require_named_identities(self):
        for invalid in (1, True, None, "", "   ", "\t"):
            with self.subTest(value=repr(invalid), role="dimension"):
                state = {invalid: {"unit": "units", "components": {"actor": "3"}}}
                with self.assertRaisesRegex(ValueError, "identity"):
                    compare_dimensions(state, state, declared_directions={invalid: "INCREASE"})
            with self.subTest(value=repr(invalid), role="component"):
                state = {"R": {"unit": "units", "components": {invalid: "3"}}}
                with self.assertRaisesRegex(ValueError, "identity"):
                    compare_dimensions(state, state, declared_directions={"R": "INCREASE"})
            with self.subTest(value=repr(invalid), role="unknown"):
                state = {"R": {"unit": "units", "components": {"actor": "3"}}}
                with self.assertRaisesRegex(ValueError, "identity"):
                    compare_dimensions(state, state, declared_directions={"R": "INCREASE"},
                                       explicitly_unknown=(invalid,))
        with self.assertRaisesRegex(ValueError, "duplicate unknown"):
            compare_dimensions(state, state, declared_directions={"R": "INCREASE"},
                               explicitly_unknown=("E", "E"))

    def test_blank_or_unnamed_units_cannot_support_a_dimensional_comparison(self):
        for unit in ("", "   ", "\t", None, True, 1):
            before = {"R": {"unit": unit, "components": {"actor": "3"}}}
            after = {"R": {"unit": unit, "components": {"actor": "4"}}}
            with self.subTest(unit=repr(unit)), self.assertRaises(ValueError):
                compare_dimensions(before, after, declared_directions={"R": "INCREASE"})

    def test_open_named_axes_and_distinct_components_roundtrip_without_normalizing(self):
        before = {"Dimensión nueva": {"unit": "context_native", "components": {
            "1": "3", "01": "3", " actor ": "3"}}}
        after = {"Dimensión nueva": {"unit": "context_native", "components": {
            "1": "4", "01": "2", " actor ": "3"}}}
        original = deepcopy((before, after))
        result = compare_dimensions(before, after,
                                    declared_directions={"Dimensión nueva": "INCREASE"},
                                    explicitly_unknown=("E", "V", "d_(n+1)"))
        self.assertEqual(json.loads(json.dumps(result)), result)
        self.assertEqual(result["per_dimension"]["Dimensión nueva"]["component_changes"],
                         {"1": "1", "01": "-1", " actor ": "0"})
        self.assertEqual(result["known_K_partial_order"], "INCOMPARABLE_K_TRADEOFF")
        self.assertEqual((before, after), original)

    def test_entire_original_h01_report_is_unchanged(self):
        manifest = json.loads((HERE / "H01_STRATEGIC_STUDY.json").read_text(encoding="utf-8"))
        report = run_manifest(manifest)
        # Full report digest independently recorded on unchanged #76 ea1a8c6.
        digest = sha256(json.dumps(report, sort_keys=True,
                                  separators=(",", ":")).encode()).hexdigest()
        self.assertEqual(digest, "e4e515c6ac5302424ba0393b7f8d8f6e10f87ebbfc95630dd59c80bba3c289fa")


if __name__ == "__main__":
    unittest.main()
