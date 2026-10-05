"""Admission gate for a real R01 T03 technology registration.

This validator is intentionally strict. It does not execute a technology; it
checks that the registration contains the minimum evidence needed before a real
candidate is allowed to enter the oracle/harness path.
"""

from __future__ import annotations

from typing import Any, Mapping


class AdmissionError(ValueError):
    pass


ALLOWED_ISOLATION_MODES = {
    "REMOTE_API_NO_ORACLE_STORAGE_ACCESS",
    "CONTAINER_NO_ORACLE_MOUNT",
    "EXTERNAL_SANDBOX_NO_ORACLE_FS",
}
ALLOWED_INTERACTION_MODES = {"BATCH_RESULT", "INTERACTIVE_TOOL_BROKER"}
ALLOWED_DISCLOSURE = {"AFTER_ALL_REGISTERED_RUNS", "AFTER_CAMPAIGN_SEAL"}


def _present(value: Any) -> bool:
    return value is not None and value != "" and value != []


def _require_present(mapping: Mapping[str, Any], keys: tuple[str, ...], prefix: str) -> None:
    for key in keys:
        if key not in mapping or not _present(mapping[key]):
            raise AdmissionError(f"missing admission field: {prefix}.{key}")


def _nonnegative_int(value: Any, field: str) -> int:
    if type(value) is not int or value < 0:
        raise AdmissionError(f"{field} must be a non-negative integer")
    return value


def validate_real_registration(reg: Mapping[str, Any]) -> None:
    if reg.get("schema") != "R01-C02-T03-REGISTRATION-0.1":
        raise AdmissionError("unsupported real-technology registration schema")
    if reg.get("status") != "REGISTERED_BEFORE_EXECUTION":
        raise AdmissionError("registration must be frozen before execution")

    uc4 = reg.get("uc4")
    if not isinstance(uc4, Mapping):
        raise AdmissionError("uc4 registration block is required")
    if uc4.get("use_case") != "FG-TIDA/use-cases#4":
        raise AdmissionError("real interoperable campaign must identify UC-4")
    _require_present(
        uc4,
        ("experiment_schema_version", "experiment_id", "test_vector_ids"),
        "uc4",
    )
    if uc4.get("source_contributor_review") != "ACCEPTED":
        raise AdmissionError("UC-4 source-contributor review must be accepted")
    if uc4.get("schema_validation") != "PASS":
        raise AdmissionError("pinned UC-4 schema validation must pass")

    r01 = reg.get("r01")
    if not isinstance(r01, Mapping):
        raise AdmissionError("r01 registration block is required")
    _require_present(
        r01,
        (
            "scenario_commit",
            "oracle_commit",
            "sidecar_hash",
            "world_bundle_hash",
            "tool_profile_hash",
            "gate_policy_hash",
            "expected_outcomes_hash",
        ),
        "r01",
    )

    technology = reg.get("technology")
    if not isinstance(technology, Mapping):
        raise AdmissionError("technology registration block is required")
    _require_present(
        technology,
        (
            "name",
            "implementation_kind",
            "product_or_project_version",
            "model_or_runtime_version",
            "source_contract_version",
        ),
        "technology",
    )
    if technology.get("access_confirmed") is not True:
        raise AdmissionError("technology access must be confirmed before execution")

    adapter = reg.get("adapter")
    if not isinstance(adapter, Mapping):
        raise AdmissionError("adapter registration block is required")
    _require_present(
        adapter,
        (
            "adapter_id",
            "adapter_version",
            "interaction_mode",
            "adapter_hash",
            "required_capabilities",
            "declared_permissions",
            "native_to_r01_mapping_hash",
        ),
        "adapter",
    )
    if adapter.get("interaction_mode") not in ALLOWED_INTERACTION_MODES:
        raise AdmissionError("unsupported real adapter interaction mode")
    if adapter.get("in_process_python_loader_allowed_for_real_t03") is not False:
        raise AdmissionError("in-process Python loader is not an admitted real-T03 isolation boundary")

    isolation = reg.get("candidate_isolation")
    if not isinstance(isolation, Mapping):
        raise AdmissionError("candidate_isolation block is required")
    if isolation.get("mode") not in ALLOWED_ISOLATION_MODES:
        raise AdmissionError("candidate isolation mode is not admitted")
    for key in (
        "oracle_filesystem_visible",
        "expected_outcomes_visible",
        "private_world_visible",
        "oracle_endpoint_exposed",
    ):
        if isolation.get(key) is not False:
            raise AdmissionError(f"candidate isolation requires {key}=false")
    if isolation.get("working_directory_isolated") is not True:
        raise AdmissionError("candidate working directory must be isolated")
    _require_present(isolation, ("isolation_evidence",), "candidate_isolation")
    if not isinstance(isolation.get("declared_network_destinations"), list):
        raise AdmissionError("declared_network_destinations must be a list")
    if not isinstance(isolation.get("environment_secrets_exposed"), list):
        raise AdmissionError("environment_secrets_exposed must be a list")

    execution = reg.get("execution")
    if not isinstance(execution, Mapping):
        raise AdmissionError("execution registration block is required")
    physical = _nonnegative_int(execution.get("physical_budget_R"), "execution.physical_budget_R")
    economic = _nonnegative_int(
        execution.get("economic_cost_target_b"), "execution.economic_cost_target_b"
    )
    _nonnegative_int(execution.get("deadline_T"), "execution.deadline_T")
    _nonnegative_int(execution.get("epsilon"), "execution.epsilon")
    episodes = execution.get("episode_count")
    if type(episodes) is not int or episodes <= 0:
        raise AdmissionError("execution.episode_count must be a positive integer")
    if economic > physical:
        raise AdmissionError("economic target b must not exceed physical budget R")
    _require_present(
        execution,
        (
            "cell_or_vector_order",
            "state_reset_policy",
            "cache_and_memory_policy",
            "seed_policy",
            "stopping_rule",
            "retry_policy",
        ),
        "execution",
    )
    if not isinstance(execution.get("external_sources_allowed"), list):
        raise AdmissionError("external_sources_allowed must be a list")

    trace = reg.get("trace_and_blinding")
    if not isinstance(trace, Mapping):
        raise AdmissionError("trace_and_blinding block is required")
    if trace.get("canonical_trace_version") != "CTv1":
        raise AdmissionError("current T03 registration requires CTv1")
    if trace.get("candidate_trace_sealed_before_oracle") is not True:
        raise AdmissionError("candidate trace must be sealed before oracle evaluation")
    if trace.get("oracle_blindness_selftest") != "PASS":
        raise AdmissionError("oracle-blindness self-test must pass")
    if trace.get("post_run_oracle_disclosure_policy") not in ALLOWED_DISCLOSURE:
        raise AdmissionError("post-run oracle disclosure policy must be registered")
    _require_present(trace, ("recorder_hash",), "trace_and_blinding")

    accounting = reg.get("accounting")
    if not isinstance(accounting, Mapping):
        raise AdmissionError("accounting block is required")
    for key in (
        "candidate_operational_cost_separate",
        "candidate_coordination_counted_once",
        "oracle_evaluator_cost_separate",
        "infrastructure_cost_reported_separately",
    ):
        if accounting.get(key) is not True:
            raise AdmissionError(f"accounting invariant must be true: {key}")

    analysis = reg.get("analysis")
    if not isinstance(analysis, Mapping):
        raise AdmissionError("analysis block is required")
    _require_present(analysis, ("primary_comparator", "comparison_scope"), "analysis")
    if analysis.get("inconclusive_outcomes_retained") is not True:
        raise AdmissionError("inconclusive outcomes must be retained")
    if analysis.get("negative_results_retained") is not True:
        raise AdmissionError("negative results must be retained")

    reviews = reg.get("reviews")
    if not isinstance(reviews, Mapping):
        raise AdmissionError("reviews block is required")
    if reviews.get("technical") != "PASS":
        raise AdmissionError("technical review must pass")
    if reviews.get("preparer") != "PASS":
        raise AdmissionError("preparer review must pass")
    if reviews.get("source_contributor") != "ACCEPTED":
        raise AdmissionError("source-contributor review must be accepted")
    if reviews.get("independent_oracle_method") != "PASS":
        raise AdmissionError("independent oracle-method review must pass")
