"""K-03 source-native regression: one-question physical response is computed, not copied.

These tests execute the unchanged finite physical law under varied real fixtures.
The private evaluator is POST-HOC; source B and receiver planning remain distinct.
"""
import unittest
from dataclasses import FrozenInstanceError, replace
from itertools import product
from unittest.mock import patch

import intrinsic_abcd as ia


class SourceNativePhysicalResponseTests(unittest.TestCase):
    def test_original_fibre_witness_and_report_are_computed(self):
        bits = tuple(1 if k in (3, 8, 12) else 0 for k in range(16))
        world = ia.balanced_tree(bits)
        clipped = ia.balanced_tree(bits, cap_root=128)
        intact = ia.private_selected_response(world, "source-3")
        blocked = ia.private_selected_response(clipped, "source-3")
        self.assertEqual((intact.current_A, intact.selected_output, intact.gain),
                         (128, 130, 2))
        self.assertEqual((blocked.current_A, blocked.selected_output, blocked.gain),
                         (128, 128, 0))
        report = ia.sample_report()
        self.assertEqual(report["current_A"], intact.current_A)
        self.assertEqual(report["same_current_A_with_root_bottleneck"], blocked.current_A)
        self.assertEqual(report["baseline_world_private_selected_gain"], intact.gain)
        self.assertEqual(report["root_bottleneck_world_private_selected_gain"], blocked.gain)
        self.assertEqual(report["policies"][0]["physical_increment_PRIVATE_ORACLE"],
                         intact.gain)

    def test_parameterized_response_matches_actual_deliver(self):
        # 16 material patterns x 7 shared caps x 4 targets x 5 increments
        # x 3 baseline demands = 6,720 independent physical questions.
        for bits in product((0, 1), repeat=4):
            for cap in (None, 31, 32, 33, 34, 36, 40):
                world = ia.balanced_tree(bits, cap_root=cap)
                for target_idx in range(4):
                    target = f"source-{target_idx}"
                    for minimum in (7, 8, 9):
                        current = ia.deliver(world, ia.base_demand(world, minimum))
                        for extra in (0, 1, 2, 3, 5):
                            with self.subTest(bits=bits, cap=cap, target=target,
                                              minimum=minimum, extra=extra):
                                response = ia.private_selected_response(
                                    world, target, minimum=minimum, extra=extra)
                                future = ia.deliver(
                                    world, ia.selected_demand(world, target,
                                                              minimum=minimum, extra=extra))
                                self.assertEqual(response.current_A, current)
                                self.assertEqual(response.selected_output, future)
                                self.assertEqual(response.gain, future-current)
                                self.assertGreaterEqual(response.gain, 0)

    def test_one_oracle_is_used_by_policies_and_posthoc_scoring(self):
        for bits in product((0, 1), repeat=4):
            for cap in (None, 32, 33, 34):
                world = ia.balanced_tree(bits, cap_root=cap)
                target = "source-2"
                truth = ia.private_selected_response(world, target).gain
                cert = ia.upstream_B(world, target, now=1, ttl=5)
                for mode in ("A_ONLY", "B_QUALIFIED",
                             "TARGETED_EXPLORATION_OF_A", "FULL_EXPAND_A"):
                    outcome = ia.policy(world, target, mode, ia.Costs(), now=2,b=cert)
                    self.assertEqual(outcome["physical_increment_PRIVATE_ORACLE"], truth)
                public = ia.observe_view(world)
                plan = ia.plan_from_public(public, target, ia.Costs(),
                                           budget=20, now=2, b=cert)
                self.assertNotIn("physical_increment_PRIVATE_ORACLE", plan)
                scored = ia.score_public_plan(world, plan, ia.Costs())
                self.assertEqual(scored["physical_increment_PRIVATE_ORACLE"], truth)

    def test_source_qualification_and_public_planning_do_not_use_private_oracle(self):
        world = ia.balanced_tree((1, 0, 0, 1))
        view = ia.observe_view(world)
        cert = ia.upstream_B(world, "source-0", now=1, ttl=5)
        with patch.object(ia, "private_selected_response",
                          side_effect=AssertionError("private oracle reached public path")):
            # B must still be produced by already-operated source logs and path
            # headroom; no future whole-world simulation is allowed for B.
            same_cert = ia.upstream_B(world, "source-0", now=1, ttl=5)
            plan = ia.plan_from_public(view, "source-0", ia.Costs(),
                                       budget=20, now=2, b=same_cert)
        self.assertEqual(same_cert.delivered_if_requested, cert.delivered_if_requested)
        self.assertEqual(plan["promised_increment"], cert.delivered_if_requested)
        self.assertNotIn("physical_increment_PRIVATE_ORACLE", plan)

    def test_sample_report_tracks_evaluator_not_frozen_literals(self):
        original = ia.private_selected_response

        def instrumentation(world, target, *, minimum=8, extra=2):
            response = original(world, target, minimum=minimum, extra=extra)
            # A wiring probe, not another physical fixture: if report numbers
            # were hardcoded, they would ignore this controlled replacement.
            shift = 7 if world.throughput_ceiling is None else 5
            return replace(response, selected_output=response.selected_output+shift)

        with patch.object(ia, "private_selected_response", side_effect=instrumentation):
            report = ia.sample_report()
        self.assertEqual(report["baseline_world_private_selected_gain"], 9)
        self.assertEqual(report["root_bottleneck_world_private_selected_gain"], 5)

    def test_invalid_question_is_rejected_and_response_immutable(self):
        world = ia.balanced_tree((0, 1, 0, 1))
        for kwargs in (
            {"target": "missing"}, {"target": "source-1", "extra": -1},
            {"target": "source-1", "extra": True},
            {"target": "source-1", "minimum": -1},
        ):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                ia.private_selected_response(world, **kwargs)
        response = ia.private_selected_response(world, "source-1")
        with self.assertRaises(FrozenInstanceError):
            response.current_A = 42


if __name__ == "__main__":
    unittest.main()
