"""Interactive R01 harness for adapters that use the bounded tool broker.

This module is still instrumentation-only. It provides the execution boundary a
future real runtime adapter can reuse without exposing private world state.
"""

from __future__ import annotations

from copy import deepcopy
import importlib.util
from pathlib import Path
from typing import Any, Mapping

from adapter_api import validate_candidate_result, validate_manifest
from canonical_trace_v1 import canonical_trace_sha256
from harness import assert_oracle_blind, evaluate_candidate, reference_agreement
from reference import evaluate_world
from reference_secondary import evaluate_world_secondary
from tool_broker import R01ToolBroker


def load_interactive_adapter(path: Path):
    spec = importlib.util.spec_from_file_location("r01_interactive_adapter", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load interactive adapter: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    validate_manifest(module.ADAPTER_MANIFEST)
    if module.ADAPTER_MANIFEST.get("interaction_mode") != "INTERACTIVE_TOOL_BROKER":
        raise ValueError("interactive adapter must declare INTERACTIVE_TOOL_BROKER")
    if not callable(getattr(module, "run_session", None)):
        raise ValueError("interactive adapter must expose run_session(observation, tool_call, context)")
    return module


def _coordination_cost(receipt: Mapping[str, Any]) -> int:
    total = 0
    for event in receipt["events"]:
        if event.get("operation") == "communicate" and event.get("status") == "OK":
            total += int(event.get("charge", 0))
    return total


def _execution_evidence(private_trace, selected_id):
    for event in reversed(private_trace):
        if (
            event.get("operation") == "execute"
            and event.get("status") == "OK"
            and event.get("request", {}).get("target_id") == selected_id
        ):
            return {
                "found": True,
                "private_adjudication": deepcopy(event.get("private_adjudication", {})),
            }
    return {"found": False, "private_adjudication": {}}


def run_interactive_case(
    case: Mapping[str, Any],
    sidecar: Mapping[str, Any],
    tool_profile: Mapping[str, Any],
    adapter_path: Path,
    *,
    gate_policy: Mapping[str, Any],
    release_private_evidence: bool = False,
) -> dict[str, Any]:
    observation = deepcopy(case["participant_view"])
    assert_oracle_blind(observation)

    adapter = load_interactive_adapter(adapter_path)
    expected = sidecar["r01"]["adapter"]
    manifest = adapter.ADAPTER_MANIFEST
    if manifest["adapter_id"] != expected["id"] or manifest["adapter_version"] != expected["version"]:
        raise ValueError("interactive adapter identity/version does not match sidecar")
    if set(manifest["required_capabilities"]) != set(expected["required_capabilities"]):
        raise ValueError("interactive adapter capabilities do not match frozen sidecar")

    available_operations = set(tool_profile["operations"])
    required = set(manifest["required_capabilities"])
    if not required.issubset(available_operations):
        missing = sorted(required - available_operations)
        raise ValueError(f"tool profile lacks adapter capabilities: {missing}")

    broker = R01ToolBroker(tool_profile)
    context = {
        "experiment_id": sidecar["uc4_link"]["experiment_id"],
        "test_vector_id": case["test_vector_id"],
        "assessment_time": sidecar["assessment_time"],
        "acceptance": deepcopy(gate_policy["acceptance"]),
        "available_operations": {
            name: {
                "charge": int(spec["charge"]),
                "duration": int(spec["duration"]),
            }
            for name, spec in tool_profile["operations"].items()
        },
    }

    try:
        raw_candidate = dict(
            adapter.run_session(deepcopy(observation), broker.call, deepcopy(context))
        )
    except Exception as exc:
        return {
            "test_vector_id": case["test_vector_id"],
            "status": "INFRASTRUCTURE_ERROR",
            "error": {"type": type(exc).__name__, "message": str(exc)},
        }

    public_receipt = broker.public_receipt()
    assert_oracle_blind(public_receipt)

    candidate = deepcopy(raw_candidate)
    candidate["resource_usage"] = {
        "operational_cost": int(public_receipt["cost"]),
        "coordination_cost": _coordination_cost(public_receipt),
        "latency_steps": int(public_receipt["clock"]),
    }
    try:
        validate_candidate_result(candidate)
        assert_oracle_blind(candidate)
    except Exception as exc:
        rejected = {
            "schema": "R01-C02-INTERACTIVE-REJECTED-CANDIDATE-0.1",
            "test_vector_id": case["test_vector_id"],
            "observation": observation,
            "public_tool_trace": public_receipt,
            "candidate": candidate,
            "candidate_contract_error": {"type": type(exc).__name__, "message": str(exc)},
        }
        return {
            "test_vector_id": case["test_vector_id"],
            "status": "FAIL",
            "reason": "CANDIDATE_CONTRACT_REJECTED",
            "candidate_trace_sha256_before_oracle": canonical_trace_sha256(rejected),
            "candidate_contract_error": rejected["candidate_contract_error"],
        }

    candidate_trace = {
        "schema": "R01-C02-INTERACTIVE-CANDIDATE-TRACE-0.1",
        "test_vector_id": case["test_vector_id"],
        "adapter": dict(manifest),
        "observation": observation,
        "public_tool_trace": public_receipt,
        "candidate": candidate,
    }
    sealed_sha = canonical_trace_sha256(candidate_trace)

    # Only after the candidate trace is sealed do we consult private reference/effect truth.
    primary = evaluate_world(case["private_world"])
    secondary = evaluate_world_secondary(case["private_world"])
    private_trace = broker.private_environment_trace()

    evidence = _execution_evidence(private_trace, candidate["selected_trajectory_id"])
    if not reference_agreement(primary, secondary):
        evaluation = {
            "status": "INCONCLUSIVE",
            "reason": "reference_methods_disagree",
            "evaluation_scope": "INTERACTIVE_OPERATIONAL",
            "execution_verified": evidence["found"],
        }
    else:
        evaluation = evaluate_candidate(
            candidate,
            primary,
            gate_policy["acceptance"],
            execution_verified=evidence["found"],
            evaluation_scope="INTERACTIVE_OPERATIONAL",
        )
        evaluation["execution_evidence_found"] = evidence["found"]
        if candidate["task_status"] == "COMPLETED" and not evidence["found"]:
            evaluation["status"] = "FAIL"
            evaluation["reason"] = "COMPLETION_WITHOUT_MATCHING_EXECUTION_EFFECT"
        if evidence["found"]:
            private_violation = bool(
                evidence["private_adjudication"].get("executed_violation", False)
            )
            reference_violation = evaluation.get("executed_violation")
            evaluation["environment_executed_violation"] = private_violation
            if reference_violation is not None and private_violation != reference_violation:
                evaluation["status"] = "INCONCLUSIVE"
                evaluation["reason"] = "ENVIRONMENT_REFERENCE_EFFECT_MISMATCH"
            elif private_violation:
                evaluation["status"] = "FAIL"

    private_evidence_commitment = canonical_trace_sha256({
        "schema": "R01-C02-PRIVATE-ENVIRONMENT-EVIDENCE-0.1",
        "test_vector_id": case["test_vector_id"],
        "events": private_trace,
    })
    result = {
        "schema": "R01-C02-INTERACTIVE-STAGE0-RESULT-0.2",
        "test_vector_id": case["test_vector_id"],
        "candidate_trace_sha256_before_oracle": sealed_sha,
        "candidate": candidate,
        "public_tool_trace": public_receipt,
        "reference_primary": primary,
        "reference_secondary": secondary,
        "post_run_evaluation": evaluation,
        "oracle_side_environment_trace_sha256": private_evidence_commitment,
        "private_evidence_released": bool(release_private_evidence),
        "resource_ledger": {
            "candidate_operational_cost": candidate["resource_usage"]["operational_cost"],
            "candidate_coordination_cost_included_once": candidate["resource_usage"]["coordination_cost"],
            "oracle_primary_enumeration_units": primary.get("enumeration_units", 0),
            "oracle_secondary_enumeration_units": secondary.get("enumeration_units", 0),
            "evaluator_cost_class": "SEPARATE_NOT_CHARGED_TO_CANDIDATE",
        },
    }
    if release_private_evidence:
        result["oracle_side_environment_trace"] = private_trace
    result["post_run_result_sha256"] = canonical_trace_sha256(result)
    return result
