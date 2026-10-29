"""Adapters that execute ORIGINAL source-native social and agentic models.

The harness owns no replacement planning theory. These two operators delegate
to PR #44 and PR #57 respectively; private referee scoring runs after planning.
"""
from __future__ import annotations
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

from dimension_experiment import ExperimentError, PhysicalOutcome

HERE = Path(__file__).resolve().parent
STUDIES = HERE.parent
_NATIVE_MODULES: dict[str, Any] = {}


def _native_module(tag: str, folder: str, name: str) -> Any:
    if tag not in _NATIVE_MODULES:
        path = STUDIES / folder / (name + ".py")
        if not path.is_file():
            raise ExperimentError("original source-native module absent: " + str(path))
        spec = importlib.util.spec_from_file_location("acc_native_" + tag, path)
        if spec is None or spec.loader is None:
            raise ExperimentError("cannot load original source module")
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        _NATIVE_MODULES[tag] = module
    return _NATIVE_MODULES[tag]


def social_native(inputs: dict[str, Any]) -> PhysicalOutcome:
    """Run the unchanged intrinsic recursive A/B/C/D source with a declared world."""
    model = _native_module("social44", "intrinsic-abcd-economics-v0.1", "intrinsic_abcd")
    bits = tuple(inputs["bits"])
    if not bits or any(type(b) is not int or b not in (0, 1) for b in bits):
        raise ExperimentError("native social bits are an explicit finite fixture")
    cap = inputs.get("cap_root")
    target_index = inputs["target_index"]
    if type(target_index) is not int or not 0 <= target_index < len(bits):
        raise ExperimentError("target index out of native world")
    world = model.balanced_tree(bits, cap_root=cap)
    target = "source-" + str(target_index)
    costs = model.Costs()
    now = inputs.get("now", 6)
    cert = model.upstream_B(world, target, now=now-1, ttl=2)
    view = model.observe_view(world)
    # The receiver works on A/outlines and scoped B only. World stays with referee.
    plan = model.plan_from_public(view, target, costs,
                                  budget=inputs.get("information_budget", 50),
                                  now=now, b=cert)
    scored = model.score_public_plan(world, plan, costs)
    arms = {}
    for arm in ("A_ONLY", "B_QUALIFIED", "TARGETED_EXPLORATION_OF_A", "FULL_EXPAND_A"):
        record = model.policy(world, target, arm, costs, now=now, b=cert)
        arms[arm] = {
            "source_status": record["status"],
            "promised_increment": record["promised_increment"],
            "net_realized_value_SYNTHETIC": record["net_realized_value_SYNTHETIC"],
            "information_cost_declared": record["information_cost_declared"],
            "referee_true_increment_PRIVATE": record["physical_increment_PRIVATE_ORACLE"],
        }
    return PhysicalOutcome("POSSIBLE", {
        "source_model": "PR44-intrinsic_abcd.py",
        "public_current_A": view.current_A,
        "public_leaf_names": [leaf.name for leaf in model.descendants(world)],
        "selected_question": {"target": target, "extra": 2},
        "private_referee_true_increment": scored["physical_increment_PRIVATE_ORACLE"],
        "source_native_certificate_issued": cert is not None,
        "receiver_plan_public_A_B_only": {
            "decision_rule": plan["decision_rule"],
            "promised_increment": plan["promised_increment"],
            "estimated_information_cost": plan["estimated_information_cost"],
        },
        "receiver_score_private_only": {
            "false_promise": scored["false_promise_PRIVATE_ORACLE"],
            "net_realized_value_SYNTHETIC": scored["net_realized_value_SYNTHETIC"],
        },
        "native_arms": arms,
        "C_D_residual_closed": False,
    })


def agentic_native(inputs: dict[str, Any]) -> PhysicalOutcome:
    """Read immutable AG fixtures and run their ORIGINAL six-arm private referee."""
    model = _native_module("agentic57", "agentic-ecosystem-reduction-v0.1", "agentic_reduction")
    data = json.loads((STUDIES / "agentic-ecosystem-reduction-v0.1" / "CASES.json").read_text(encoding="utf-8"))
    if data["schema"] != model.SCHEMA:
        raise ExperimentError("native agentic fixture schema mismatch")
    case_id = inputs["native_case_id"]
    matches = [x for x in data["cases"] if x["id"] == case_id]
    if len(matches) != 1:
        raise ExperimentError("native agentic case ID unresolved or duplicated")
    native = model.run_case(matches[0])
    arms = {}
    for name, row in native["arms"].items():
        plan = row["plan"]
        physical = row["observed_by_referee_only"]
        if physical["total_resources_same"] != native["public_A"]["total_resources"]:
            raise ExperimentError("source-native agentic resource nonconservation")
        arms[name] = {
            "public_plan": {
                "status": plan["status"], "transfer": plan["transfer"],
                "instrument_cost": plan["instrument_cost"],
            },
            "private_referee_only": {
                "output": physical["output"],
                "total_resources_same": physical["total_resources_same"],
                "mission_target_met": physical["mission_target_met"],
                "technical_optimum": row["technical_optimum_referee_only"],
                "gap_to_same_budget_optimum": row["mission_output_gap_to_same_budget_technical_optimum"],
            },
        }
    return PhysicalOutcome("POSSIBLE", {
        "source_model": "PR57-agentic_reduction.py",
        "native_case_id": case_id,
        "public_current_A_output": native["public_A"]["current_A_total_output"],
        "public_total_resources": native["public_A"]["total_resources"],
        "source_synthetic_arms": arms,
        "private_truth_not_a_public_planner_input": True,
        "C_D_residual_closed": False,
    })


def native_operators():
    return {"source_native_social44": social_native,
            "source_native_agentic57": agentic_native}
