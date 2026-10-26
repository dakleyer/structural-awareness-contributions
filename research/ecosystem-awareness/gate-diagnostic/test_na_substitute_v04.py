"""C74 local admission controls for the v0.4 audit candidate."""
import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location(
    "dds_v04", Path(__file__).with_name("check_gate_profile_v0.4_audit_candidate.py"))
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class TypedSubstitutionControls(unittest.TestCase):
    def row(self, value):
        return {"gate_id": "SA-G03", "applicability": "NOT_APPLICABLE",
                "own_verdict": "NOT_APPLICABLE",
                "applicability_rationale": "Outside the registered scope",
                "na_substitute_satisfied": value}

    def test_boolean_true_and_false_are_preserved(self):
        for value in (True, False):
            with self.subTest(value=value):
                result = {"gates": [self.row(value)]}
                checker.require_na_rationale(result)
                self.assertIs(result["gates"][0]["na_substitute_satisfied"], value)

    def test_missing_substitute_is_left_to_the_base_contract(self):
        row = self.row(False)
        del row["na_substitute_satisfied"]
        checker.require_na_rationale({"gates": [row]})
        self.assertNotIn("na_substitute_satisfied", row)

    def test_strings_numbers_lists_objects_and_null_are_rejected(self):
        for value in ("false", "true", "", "0", 0, 1, 0.0, [], [False], {}, None):
            with self.subTest(value=value):
                with self.assertRaisesRegex(checker.ApplicabilityContractError,
                                            "na_substitute_satisfied_must_be_boolean:SA-G03"):
                    checker.require_na_rationale({"gates": [self.row(value)]})

    def test_invalid_field_on_applicable_row_is_also_rejected(self):
        row = self.row("false")
        row.update(applicability="APPLICABLE", own_verdict="PASS")
        with self.assertRaises(checker.ApplicabilityContractError):
            checker.require_na_rationale({"gates": [row]})

    def test_bad_value_never_reaches_frozen_compiler(self):
        with patch.object(checker, "load_frozen_checker") as loader:
            with self.assertRaises(checker.ApplicabilityContractError):
                checker.compile_successor({}, {"gates": [self.row("false")]})
            loader.assert_not_called()

    def diagnostic(self, value, present=True):
        catalog = {"gates": [{"id": "SA-G03"},
                              {"id": "SA-G04", "requires_all": ["SA-G03"]}],
                   "verdicts": ["PASS", "NOT_APPLICABLE"],
                   "test_roles": ["SUPPORT"], "named_claims": {}}
        row = self.row(value)
        row.update(test_role="SUPPORT", level="L0", required_min_level="L0",
                   required_for_profile=False)
        if not present:
            del row["na_substitute_satisfied"]
        result = {"profile": {"required_named_claims": []}, "gates": [row,
                  {"gate_id": "SA-G04", "applicability": "APPLICABLE",
                   "own_verdict": "PASS", "test_role": "SUPPORT", "level": "L0",
                   "required_min_level": "L0", "required_for_profile": True}]}
        return checker.compile_successor(catalog, result)

    def test_real_frozen_dependency_true_false_and_absence(self):
        for value, present, expected in ((True, True, "PASS"),
                                         (False, True, "BLOCKED_BY(SA-G03)"),
                                         (None, False, "BLOCKED_BY(SA-G03)")):
            with self.subTest(value=value, present=present):
                out = self.diagnostic(value, present)
                self.assertEqual(out["gates"][1]["effective_status"], expected)

    def test_real_pipeline_rejects_false_string(self):
        with self.assertRaisesRegex(checker.ApplicabilityContractError,
                                    "na_substitute_satisfied_must_be_boolean"):
            self.diagnostic("false")


if __name__ == "__main__":
    unittest.main(verbosity=2)
