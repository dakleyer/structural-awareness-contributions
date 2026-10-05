"""Semantic admission checks for the R01 oracle/harness artifacts.

These checks complement, but do not replace, Nelson UC-4 schema validation.
They intentionally use only the Python standard library so the local/CI
instrument can reject structurally plausible but semantically unusable inputs.
"""

from __future__ import annotations

from pathlib import PurePosixPath
from typing import Any, Mapping

FORBIDDEN_PUBLIC_KEYS = {
    "admissible",
    "private_label",
    "optimum",
    "optimum_J",
    "expected_outcome",
    "reference_truth",
    "world_truth",
    "executed_violation",
    "J_effect",
}


class ContractError(ValueError):
    pass


def _safe_relative_path(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise ContractError(f"{field} must be a non-empty relative path")
    raw = value.replace("\\", "/")
    path = PurePosixPath(raw)
    if raw.startswith("/") or (len(raw) >= 2 and raw[1] == ":") or ".." in path.parts:
        raise ContractError(f"{field} must stay inside the oracle package")
    return path.as_posix()


def _nonnegative_int(value: Any, field: str) -> int:
    if type(value) is not int or value < 0:
        raise ContractError(f"{field} must be a non-negative integer")
    return value


def _walk_public(value: Any, path: tuple[str, ...] = ()) -> None:
    if isinstance(value, Mapping):
        for key, child in value.items():
            if key in FORBIDDEN_PUBLIC_KEYS:
                joined = ".".join(path + (str(key),))
                raise ContractError(f"public response exposes private/evaluator key: {joined}")
            _walk_public(child, path + (str(key),))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _walk_public(child, path + (str(index),))


def validate_sidecar(sidecar: Mapping[str, Any]) -> None:
    if sidecar.get("schema") != "R01-UC4-SIDECAR-0.1":
        raise ContractError("unsupported R01 sidecar schema")
    if sidecar.get("uc4_link", {}).get("use_case") != "FG-TIDA/use-cases#4":
        raise ContractError("R01 bridge must identify Nelson UC-4")

    ids = sidecar.get("uc4_link", {}).get("test_vector_ids")
    if not isinstance(ids, list) or not ids or not all(isinstance(x, str) and x for x in ids):
        raise ContractError("sidecar test_vector_ids must be non-empty strings")
    if len(ids) != len(set(ids)):
        raise ContractError("sidecar test_vector_ids must be unique")

    reviews = sidecar.get("reviews")
    if not isinstance(reviews, Mapping):
        raise ContractError("sidecar reviews object is required")
    for key in ("technical", "preparer", "source_contributor"):
        if key not in reviews:
            raise ContractError(f"sidecar review state missing: {key}")

    r01 = sidecar.get("r01")
    if not isinstance(r01, Mapping):
        raise ContractError("sidecar r01 object is required")

    world_bundle = r01.get("world_bundle")
    if not isinstance(world_bundle, Mapping):
        raise ContractError("r01.world_bundle is required")
    _safe_relative_path(world_bundle.get("path"), "r01.world_bundle.path")

    adapter = r01.get("adapter")
    if not isinstance(adapter, Mapping):
        raise ContractError("r01.adapter is required")
    _safe_relative_path(adapter.get("path"), "r01.adapter.path")
    if not str(adapter["path"]).replace("\\", "/").startswith("adapters/"):
        raise ContractError("r01.adapter.path must be under adapters/")
    caps = adapter.get("required_capabilities")
    if not isinstance(caps, list) or len(caps) != len(set(caps)):
        raise ContractError("adapter required_capabilities must be a unique list")

    oracle = r01.get("oracle")
    if not isinstance(oracle, Mapping) or oracle.get("candidate_blind") is not True:
        raise ContractError("oracle must explicitly be candidate_blind")

    acceptance = r01.get("acceptance")
    if not isinstance(acceptance, Mapping):
        raise ContractError("r01.acceptance is required")
    epsilon = _nonnegative_int(acceptance.get("epsilon"), "acceptance.epsilon")
    del epsilon
    b = _nonnegative_int(
        acceptance.get("economic_cost_target_b"), "acceptance.economic_cost_target_b"
    )
    physical = _nonnegative_int(
        acceptance.get("physical_budget_R"), "acceptance.physical_budget_R"
    )
    _nonnegative_int(acceptance.get("deadline_T"), "acceptance.deadline_T")
    if b > physical:
        raise ContractError("economic cost target b must not exceed physical budget R")

    ledger = r01.get("resource_ledger")
    if not isinstance(ledger, Mapping):
        raise ContractError("r01.resource_ledger is required")
    for key in (
        "separate_candidate_operational",
        "separate_oracle_evaluator",
        "coordination_counted_once",
    ):
        if ledger.get(key) is not True:
            raise ContractError(f"resource ledger invariant must be true: {key}")

    status = sidecar.get("status")
    source_review = reviews.get("source_contributor")
    if status != "R01-BRIDGE-DRAFT" and source_review == "PENDING":
        raise ContractError("bridge cannot advance beyond draft with source review pending")


def _validate_reference_element(
    element: Mapping[str, Any],
    *,
    field: str,
    nonnegative_benefits: bool,
) -> None:
    benefit = element.get("benefit", 0)
    if type(benefit) is not int:
        raise ContractError(f"{field}.benefit must be an integer")
    if nonnegative_benefits and benefit < 0:
        raise ContractError(f"{field}.benefit violates NONNEGATIVE_BASE")
    if type(element.get("admissible")) is not bool:
        raise ContractError(f"{field}.admissible must be boolean")
    completed = element.get("completed", True)
    if type(completed) is not bool:
        raise ContractError(f"{field}.completed must be boolean")


def validate_world_bundle(
    bundle: Mapping[str, Any],
    *,
    sidecar: Mapping[str, Any],
    expected_status: Mapping[str, Any],
) -> None:
    if bundle.get("schema") != "R01-C02-STAGE0-WORLDS-0.1":
        raise ContractError("unsupported Stage-0 world-bundle schema")
    regime = bundle.get("benefit_regime")
    if regime not in {"NONNEGATIVE_BASE", "EXPLICIT_VARIANT"}:
        raise ContractError("world bundle must declare benefit_regime")
    nonnegative = regime == "NONNEGATIVE_BASE"

    worlds = bundle.get("worlds")
    if not isinstance(worlds, list) or not worlds:
        raise ContractError("world bundle requires a non-empty worlds list")

    seen: set[str] = set()
    for index, world in enumerate(worlds):
        if not isinstance(world, Mapping):
            raise ContractError(f"worlds[{index}] must be an object")
        vector_id = world.get("test_vector_id")
        if not isinstance(vector_id, str) or not vector_id:
            raise ContractError(f"worlds[{index}].test_vector_id is required")
        if vector_id in seen:
            raise ContractError(f"duplicate test_vector_id: {vector_id}")
        seen.add(vector_id)

        participant = world.get("participant_view")
        if not isinstance(participant, Mapping):
            raise ContractError(f"{vector_id}: participant_view is required")
        _walk_public(participant, ("participant_view",))

        candidates = participant.get("candidates")
        if not isinstance(candidates, list) or not candidates:
            raise ContractError(f"{vector_id}: participant candidates must be non-empty")
        public_ids = []
        for c_index, candidate in enumerate(candidates):
            if not isinstance(candidate, Mapping):
                raise ContractError(f"{vector_id}: candidate {c_index} must be an object")
            cid = candidate.get("trajectory_id")
            if not isinstance(cid, str) or not cid:
                raise ContractError(f"{vector_id}: candidate trajectory_id is required")
            public_ids.append(cid)
            if type(candidate.get("observed_local_benefit")) is not int:
                raise ContractError(f"{vector_id}: observed_local_benefit must be integer")
        if len(public_ids) != len(set(public_ids)):
            raise ContractError(f"{vector_id}: participant candidate ids must be unique")

        private_world = world.get("private_world")
        if not isinstance(private_world, Mapping):
            raise ContractError(f"{vector_id}: private_world is required")
        trajectories = private_world.get("trajectories")
        if not isinstance(trajectories, list) or not trajectories:
            raise ContractError(f"{vector_id}: private trajectories must be non-empty")
        private_ids: list[str] = []
        for t_index, trajectory in enumerate(trajectories):
            if not isinstance(trajectory, Mapping):
                raise ContractError(f"{vector_id}: trajectory {t_index} must be an object")
            tid = trajectory.get("trajectory_id")
            if not isinstance(tid, str) or not tid:
                raise ContractError(f"{vector_id}: private trajectory_id is required")
            private_ids.append(tid)
            steps = trajectory.get("steps")
            if not isinstance(steps, list) or not steps:
                raise ContractError(f"{vector_id}/{tid}: steps must be non-empty")
            for e_index, step in enumerate(steps):
                if not isinstance(step, Mapping):
                    raise ContractError(f"{vector_id}/{tid}: step {e_index} must be object")
                _validate_reference_element(
                    step,
                    field=f"{vector_id}/{tid}/step[{e_index}]",
                    nonnegative_benefits=nonnegative,
                )
            connectors = trajectory.get("connectors", [])
            if not isinstance(connectors, list):
                raise ContractError(f"{vector_id}/{tid}: connectors must be list")
            for e_index, connector in enumerate(connectors):
                if not isinstance(connector, Mapping):
                    raise ContractError(
                        f"{vector_id}/{tid}: connector {e_index} must be object"
                    )
                _validate_reference_element(
                    connector,
                    field=f"{vector_id}/{tid}/connector[{e_index}]",
                    nonnegative_benefits=nonnegative,
                )
        if len(private_ids) != len(set(private_ids)):
            raise ContractError(f"{vector_id}: private trajectory ids must be unique")
        if not set(public_ids).issubset(set(private_ids)):
            raise ContractError(
                f"{vector_id}: participant candidate id lacks private reference trajectory"
            )

        measurement = world.get("harness_resource_measurement")
        if not isinstance(measurement, Mapping):
            raise ContractError(f"{vector_id}: harness_resource_measurement is required")
        for key in ("operational_cost", "coordination_cost", "latency_steps"):
            _nonnegative_int(measurement.get(key), f"{vector_id}.measurement.{key}")

    sidecar_ids = set(sidecar["uc4_link"]["test_vector_ids"])
    expected_ids = set(expected_status)
    if seen != sidecar_ids:
        raise ContractError(
            f"world/sidecar vector mismatch: worlds={sorted(seen)} sidecar={sorted(sidecar_ids)}"
        )
    if seen != expected_ids:
        raise ContractError(
            f"world/expected vector mismatch: worlds={sorted(seen)} expected={sorted(expected_ids)}"
        )


def validate_tool_profile(profile: Mapping[str, Any]) -> None:
    _nonnegative_int(profile.get("physical_budget_R"), "tool_profile.physical_budget_R")
    _nonnegative_int(profile.get("deadline_T"), "tool_profile.deadline_T")

    operations = profile.get("operations")
    catalogs = profile.get("catalogs")
    if not isinstance(operations, Mapping) or not operations:
        raise ContractError("tool profile operations are required")
    if not isinstance(catalogs, Mapping):
        raise ContractError("tool profile catalogs are required")

    for name, spec in operations.items():
        if not isinstance(name, str) or not isinstance(spec, Mapping):
            raise ContractError("tool operation entries must be named objects")
        _nonnegative_int(spec.get("charge"), f"operations.{name}.charge")
        _nonnegative_int(spec.get("duration"), f"operations.{name}.duration")
        catalog = spec.get("catalog")
        if catalog is not None and catalog not in catalogs:
            raise ContractError(f"operation {name} references missing catalog {catalog}")

    for catalog_name, entries in catalogs.items():
        if not isinstance(entries, Mapping):
            raise ContractError(f"catalog {catalog_name} must be an object")
        for entry_id, entry in entries.items():
            if not isinstance(entry_id, str) or not isinstance(entry, Mapping):
                raise ContractError(f"catalog {catalog_name} contains invalid entry")
            response = entry.get("response", {})
            if not isinstance(response, Mapping):
                raise ContractError(f"{catalog_name}/{entry_id}: response must be object")
            _walk_public(response, (str(catalog_name), str(entry_id), "response"))
            private = entry.get("private", {})
            if not isinstance(private, Mapping):
                raise ContractError(f"{catalog_name}/{entry_id}: private must be object")

    state_machine = profile.get("state_machine")
    if not isinstance(state_machine, Mapping) or type(state_machine.get("enabled")) is not bool:
        raise ContractError("tool profile must explicitly declare state_machine.enabled")
    if state_machine["enabled"] is False:
        if state_machine.get("admissible_for_standard_operational_result") is not False:
            raise ContractError(
                "state-machine-disabled profile must be non-admissible for standard operational results"
            )
        if not state_machine.get("purpose"):
            raise ContractError("state-machine-disabled profile must declare its control purpose")
    else:
        if state_machine.get("admissible_for_standard_operational_result") is not True:
            raise ContractError(
                "state-machine-enabled standard profile must explicitly be operationally admissible"
            )


def validate_interactive_case(
    case: Mapping[str, Any],
    *,
    tool_profile: Mapping[str, Any],
) -> None:
    if not isinstance(case.get("test_vector_id"), str):
        raise ContractError("interactive case requires test_vector_id")
    participant = case.get("participant_view")
    private_world = case.get("private_world")
    if not isinstance(participant, Mapping) or not isinstance(private_world, Mapping):
        raise ContractError("interactive case requires participant_view and private_world")
    _walk_public(participant, ("interactive_participant_view",))

    handles = participant.get("candidate_handles")
    if not isinstance(handles, list) or not handles:
        raise ContractError("interactive case requires candidate_handles")
    candidates = tool_profile.get("catalogs", {}).get("candidates", {})
    relations = tool_profile.get("catalogs", {}).get("relations", {})
    private_ids = {
        t.get("trajectory_id")
        for t in private_world.get("trajectories", [])
        if isinstance(t, Mapping)
    }
    for item in handles:
        if not isinstance(item, Mapping):
            raise ContractError("candidate handle must be object")
        cid = item.get("candidate_id")
        rid = item.get("relation_id")
        if cid not in candidates:
            raise ContractError(f"interactive candidate handle missing from tool catalog: {cid}")
        if rid not in relations:
            raise ContractError(f"interactive relation handle missing from tool catalog: {rid}")
        if cid not in private_ids:
            raise ContractError(f"interactive candidate lacks private reference trajectory: {cid}")
