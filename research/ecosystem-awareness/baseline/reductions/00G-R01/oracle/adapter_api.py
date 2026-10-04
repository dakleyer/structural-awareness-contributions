"""Technology-neutral R01 adapter contract.

Aligned to Nelson Trasatti's UC-4 requirement that imported contracts enter through
versioned adapters. This module defines only the R01 side of that boundary.
"""

from __future__ import annotations

from typing import Any, Mapping, Protocol


class R01Adapter(Protocol):
    ADAPTER_MANIFEST: Mapping[str, Any]

    def invoke(self, observation: Mapping[str, Any], context: Mapping[str, Any]) -> Mapping[str, Any]:
        """Run using only participant-visible observation and bounded context."""


REQUIRED_MANIFEST_FIELDS = {
    "adapter_id",
    "adapter_version",
    "implementation_kind",
    "source_owner",
    "source_contract_version",
    "required_capabilities",
}


def validate_manifest(manifest: Mapping[str, Any]) -> None:
    missing = sorted(REQUIRED_MANIFEST_FIELDS - set(manifest))
    if missing:
        raise ValueError(f"adapter manifest missing fields: {missing}")
    if not isinstance(manifest["required_capabilities"], list):
        raise ValueError("required_capabilities must be a list")


def validate_candidate_result(result: Mapping[str, Any]) -> None:
    required = {"task_status", "selected_trajectory_id", "events", "resource_usage"}
    missing = sorted(required - set(result))
    if missing:
        raise ValueError(f"candidate result missing fields: {missing}")
    if result["task_status"] not in {"COMPLETED", "ABSTAINED", "INCOMPLETE"}:
        raise ValueError("unsupported task_status")
    selected = result["selected_trajectory_id"]
    if selected is not None and not isinstance(selected, str):
        raise ValueError("selected_trajectory_id must be a string or null")
    if not isinstance(result["events"], list):
        raise ValueError("events must be a list")
    usage = result["resource_usage"]
    if not isinstance(usage, Mapping):
        raise ValueError("resource_usage must be an object")
    for key in ("operational_cost", "coordination_cost", "latency_steps"):
        if type(usage.get(key)) is not int or usage[key] < 0:
            raise ValueError(f"resource_usage.{key} must be a non-negative integer")
