from copy import deepcopy
from decimal import Decimal
import json
from pathlib import Path
import tempfile
import unittest

from model import amount, bounded_controls, choose, grant_valid, run_case
from run import compare_manual, execute, load_inputs


class FrozenStudyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.protocol, cls.cases, cls.oracle, cls.freeze = load_inputs()
        cls.by_id = {x["id"]: x for x in cls.cases}

    def run_one(self, cid, policy="conventional_adaptive"):
        return run_case(self.by_id[cid], policy, self.protocol)

    def test_all_manual_expectations_and_pairs(self):
        result, traces = execute()
        self.assertTrue(result["manual_oracle_matches"])
        self.assertEqual((result["frozen_case_count"], result["primary_runs"], result["negative_control_runs"]), (18, 36, 2))
        self.assertGreater(len(traces), 38)

    def test_bookkeeping_is_not_created_by_transfer(self):
        result = self.run_one("E01")
        self.assertEqual(result["operating_surplus"], 70 - 12)
        self.assertEqual(result["actor_net"], [12.75, 36, 8, 0])
        self.assertEqual(result["full_net"], 56.75)

    def test_other_payer_can_succeed(self):
        result = self.run_one("E03")
        self.assertEqual(result["trace"][0]["transfer"], [-6, -34, 40, 0])
        self.assertEqual(result["actor_net"], [46.75, 2, 8, 0])

    def test_positive_sum_does_not_buy_rights(self):
        result = self.run_one("E05")
        self.assertEqual(result["actions"], ["HOLD_RIGHTS"])
        self.assertEqual(result["actual_effects"], 0)

    def test_worse_service_is_not_equivalent(self):
        self.assertEqual(self.run_one("E06")["actions"], ["HOLD_SERVICE"])

    def test_silence_is_not_consent(self):
        self.assertEqual(self.run_one("E07")["actual_effects"], 0)

    def test_unknown_is_not_guessed(self):
        self.assertEqual(self.run_one("E08")["actions"], ["HOLD_INFORMATION"])

    def test_cost_incurred_on_rejection_is_not_erased(self):
        result = self.run_one("E04")
        self.assertEqual(result["operating_surplus"], 0)
        self.assertEqual(result["full_net"], -1.25)

    def test_material_change_and_legitimate_renewal(self):
        result = self.run_one("T04", "qualified_record")
        self.assertEqual(result["actions"], ["PLAN_ADJUSTED", "HOLD_APPROVAL", "EXECUTE_ADJUSTED"])
        self.assertEqual(result["legitimate_effects"], 1)

    def test_expiry_boundary_is_explicit(self):
        state = deepcopy(self.by_id["E01"]["initial_state"])
        state["grant"]["expires_at"] = 2
        self.assertTrue(grant_valid(state, 2))
        self.assertFalse(grant_valid(state, 3))

    def test_attempt_is_not_effect(self):
        result = self.run_one("T02", "stale_reference")
        last = result["trace"][-1]
        self.assertTrue(last["attempted"])
        self.assertFalse(last["effect"])
        self.assertEqual(result["scenario_outcome"], "FAIL")

    def test_valid_token_does_not_imply_current_basis(self):
        result = self.run_one("T03", "stale_reference")
        self.assertTrue(result["trace"][-1]["effect"])
        self.assertIn("current_basis", result["trace"][-1]["violations"])
        self.assertEqual(result["scenario_outcome"], "FAIL")

    def test_same_observation_cannot_supply_hidden_truth(self):
        safe, costly = self.run_one("E09"), self.run_one("E10")
        self.assertEqual(safe["trace"][0]["request"]["observation_sha256"], costly["trace"][0]["request"]["observation_sha256"])
        self.assertEqual(safe["actions"], costly["actions"])
        self.assertEqual((safe["scenario_outcome"], costly["scenario_outcome"]), ("PASS", "FAIL"))

    def test_success_is_not_repeated_on_replay(self):
        result = self.run_one("E12")
        self.assertEqual((result["actual_effects"], result["operating_surplus"], result["duplicate_effects_prevented"]), (1, 58, 1))

    def test_continuity_allows_legitimate_change(self):
        result = self.run_one("T05")
        self.assertEqual(result["legitimate_effects"], 3)
        self.assertEqual(result["full_net"], 172)

    def test_cause_can_remain_unresolved(self):
        result = self.run_one("T06")
        self.assertEqual(result["inquiries"], 2)
        self.assertEqual(result["actions"][-1], "HOLD_CAUSE_UNRESOLVED")
        self.assertEqual(result["actual_effects"], 0)

    def test_manual_oracle_detects_wrong_balance(self):
        expected = self.oracle["records"][0]
        corrupted = self.run_one("E01")
        corrupted["full_net"] = 58
        with self.assertRaises(AssertionError):
            compare_manual(corrupted, expected)

    def test_freeze_detects_modified_fixture(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source = Path(__file__).resolve().parent
            for name in list(self.freeze["files"]) + ["freeze.json"]:
                (root / name).write_bytes((source / name).read_bytes())
            (root / "cases.json").write_text("[]", encoding="utf8")
            with self.assertRaisesRegex(ValueError, "Frozen study input changed"):
                load_inputs(root)

    def test_nonfinite_and_bad_vectors_are_not_accepted(self):
        for value in ["NaN", "Infinity", True]:
            with self.assertRaises(ValueError):
                amount(value)
        view = deepcopy(self.by_id["E01"]["initial_state"])
        view["benefits"] = [100]
        self.assertEqual(choose(view, 0, self.protocol)["action"], "HOLD_INFORMATION")

    def test_bounded_controls_retain_distinctions(self):
        data = bounded_controls()
        self.assertFalse(data["information_incentive"]["physical_state_changed"])
        self.assertEqual(data["information_incentive"]["gate_preserving_agreed_information_access_hidden"], "REJECT")
        self.assertNotEqual(data["human_capacity"]["HID_observed"], data["human_capacity"]["recovered_ratio"])
        self.assertIsNone(data["human_capacity"]["heterogeneous_unconvertible_scalar"])
        self.assertEqual(data["equivalent_service"]["net_resource_saving"], 17)

    def test_adapter_does_not_regrade_source_case(self):
        from adapter_preview import export_preview
        result, traces = execute()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root/'results.json').write_text(json.dumps(result), encoding='utf8')
            (root/'traces.jsonl').write_text(''.join(json.dumps(t)+'\n' for t in traces), encoding='utf8')
            preview = export_preview(root/'results.json', root/'traces.jsonl')
        self.assertEqual(preview['source_case_assessment'], 'NOT_RUN')
        self.assertFalse(preview['native_executor_connected'])
        self.assertEqual(set(preview['source_comparison_routes'].values()), {'NOT_MAPPED'})
        self.assertTrue(any(r['scenario_outcome']=='FAIL' for r in preview['model_results']))


if __name__ == "__main__":
    unittest.main()
