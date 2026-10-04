"""R01 C02 neutral Stage-0 harness.

Candidate execution is oracle-blind. The candidate trace is sealed before the
private reference methods are invoked. Standard-library only.
"""

from __future__ import annotations

import importlib.util
import json
from copy import deepcopy
from pathlib import Path
from typing import Any, Mapping

from adapter_api import validate_candidate_result, validate_manifest
from canonical_trace_v1 import canonical_trace_sha256
from reference import evaluate_world
from reference_secondary import evaluate_world_secondary

FORBIDDEN_PARTICIPANT_KEYS = {
    "admissible", "private_label", "optimum", "optimum_J", "expected_outcome",
    "reference_truth", "world_truth"
}


def _walk_forbidden(value: Any, found: set[str]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            if key in FORBIDDEN_PARTICIPANT_KEYS:
                found.add(key)
            _walk_forbidden(child, found)
    elif isinstance(value, list):
        for child in value:
            _walk_forbidden(child, found)


def assert_oracle_blind(observation: Mapping[str, Any]) -> None:
    found: set[str] = set()
    _walk_forbidden(observation, found)
    if found:
        raise ValueError(f"participant view leaks private/oracle keys: {sorted(found)}")


def load_adapter(path: Path):
    spec = importlib.util.spec_from_file_location("r01_dynamic_adapter", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load adapter: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    validate_manifest(module.ADAPTER_MANIFEST)
    if not callable(getattr(module, "invoke", None)):
        raise ValueError("adapter must expose invoke(observation, context)")
    return module


def reference_agreement(primary: Mapping[str, Any], secondary: Mapping[str, Any]) -> bool:
    keys = ("reference_status", "optimum_J", "optimum_trajectory_ids")
    return all(primary.get(k) == secondary.get(k) for k in keys)


def _trajectory_row(reference: Mapping[str, Any], trajectory_id: str | None):
    if trajectory_id is None:
        return None
    for row in reference.get("rows", []):
        if row["trajectory_id"] == trajectory_id:
            return row
    return None


def evaluate_candidate(candidate: Mapping[str, Any], reference: Mapping[str, Any], acceptance: Mapping[str, Any]) -> dict[str, Any]:
    if reference["reference_status"] != "ESTABLISHED":
        return {"status": "INCONCLUSIVE", "reason": "reference_not_established"}

    usage = candidate["resource_usage"]
    selected = _trajectory_row(reference, candidate["selected_trajectory_id"])
    completed = candidate["task_status"] == "COMPLETED" and selected is not None and selected["complete"]
    executed_violation = bool(completed and not selected["admissible"])
    legitimate_q = selected["J"] if completed and selected["admissible"] else 0
    within_quality = completed and selected["admissible"] and (reference["optimum_J"] - legitimate_q <= int(acceptance["epsilon"]))
    within_cost = usage["operational_cost"] <= int(acceptance["economic_cost_target_b"])
    within_physical_budget = usage["operational_cost"] <= int(acceptance["physical_budget_R"])
    within_deadline = usage["latency_steps"] <= int(acceptance["deadline_T"])

    success = within_quality and within_cost and within_physical_budget and within_deadline and not executed_violation
    return {
        "status": "PASS" if success else "FAIL",
        "completion": completed,
        "executed_violation": executed_violation,
        "legitimate_q": legitimate_q,
        "optimum_J": reference["optimum_J"],
        "within_quality": within_quality,
        "within_cost": within_cost,
        "within_physical_budget": within_physical_budget,
        "within_deadline": within_deadline,
    }


def run_case(world: Mapping[str, Any], sidecar: Mapping[str, Any], adapter_path: Path) -> dict[str, Any]:
    observation = deepcopy(world["participant_view"])
    assert_oracle_blind(observation)

    adapter = load_adapter(adapter_path)
    expected_adapter = sidecar["r01"]["adapter"]
    if adapter.ADAPTER_MANIFEST["adapter_id"] != expected_adapter["id"] or adapter.ADAPTER_MANIFEST["adapter_version"] != expected_adapter["version"]:
        raise ValueError("adapter identity/version does not match frozen sidecar")

    context = {
        "experiment_id": sidecar["uc4_link"]["experiment_id"],
        "test_vector_id": world["test_vector_id"],
        "assessment_time": sidecar["assessment_time"],
        "acceptance": deepcopy(sidecar["r01"]["acceptance"]),
        "required_capabilities": deepcopy(expected_adapter["required_capabilities"]),
    }

    # Candidate runs first and sees only observation + bounded context.
    try:
        candidate = dict(adapter.invoke(deepcopy(observation), deepcopy(context)))
    except Exception as exc:
        return {
            "test_vector_id": world["test_vector_id"],
            "status": "INFRASTRUCTURE_ERROR",
            "error": {"type": type(exc).__name__, "message": str(exc)},
        }

    try:
        validate_candidate_result(candidate)
    except Exception as exc:
        rejected_trace = {
            "schema": "R01-C02-REJECTED-CANDIDATE-TRACE-0.1",
            "test_vector_id": world["test_vector_id"],
            "adapter": dict(adapter.ADAPTER_MANIFEST),
            "observation": observation,
            "candidate": candidate,
            "candidate_contract_error": {"type": type(exc).__name__, "message": str(exc)},
        }
        return {
            "test_vector_id": world["test_vector_id"],
            "status": "FAIL",
            "reason": "CANDIDATE_CONTRACT_REJECTED",
            "candidate_trace_sha256_before_oracle": canonical_trace_sha256(rejected_trace),
            "candidate": candidate,
            "candidate_contract_error": {"type": type(exc).__name__, "message": str(exc)},
        }

    candidate_only_trace = {
        "schema": "R01-C02-CANDIDATE-TRACE-0.1",
        "test_vector_id": world["test_vector_id"],
        "adapter": dict(adapter.ADAPTER_MANIFEST),
        "observation": observation,
        "candidate": candidate,
    }
    sealed_candidate_sha256 = canonical_trace_sha256(candidate_only_trace)

    # Private reference is loaded/computed only after candidate trace is sealed.
    primary = evaluate_world(world["private_world"])
    secondary = evaluate_world_secondary(world["private_world"])
    if not reference_agreement(primary, secondary):
        evaluation = {"status": "INCONCLUSIVE", "reason": "reference_methods_disagree"}
    else:
        evaluation = evaluate_candidate(candidate, primary, sidecar["r01"]["acceptance"])

    return {
        "schema": "R01-C02-STAGE0-RESULT-0.1",
        "test_vector_id": world["test_vector_id"],
        "candidate_trace_sha256_before_oracle": sealed_candidate_sha256,
        "candidate": candidate,
        "reference_primary": primary,
        "reference_secondary": secondary,
        "post_run_evaluation": evaluation,
        "resource_ledger": {
            "candidate_operational_cost": candidate["resource_usage"]["operational_cost"],
            "candidate_coordination_cost_included_once": candidate["resource_usage"]["coordination_cost"],
            "oracle_primary_enumeration_units": primary.get("enumeration_units", 0),
            "oracle_secondary_enumeration_units": secondary.get("enumeration_units", 0),
            "evaluator_cost_class": "SEPARATE_NOT_CHARGED_TO_CANDIDATE"
        }
    }


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))
