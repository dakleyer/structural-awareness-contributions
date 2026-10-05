"""Deliberate abstention adapter for R01 anti-shortcut testing."""

ADAPTER_MANIFEST = {
    "adapter_id": "R01-SELFTEST-ALWAYS-ABSTAIN",
    "adapter_version": "0.1",
    "implementation_kind": "NEGATIVE_CONTROL_NOT_A_REAL_TECHNOLOGY",
    "source_owner": "R01 maintainer",
    "source_contract_version": "R01 participant-view 0.1",
    "interaction_mode": "BATCH_RESULT",
    "required_capabilities": ["read_frozen_observation", "emit_candidate_result"],
}


def invoke(observation, context):
    return {
        "task_status": "ABSTAINED",
        "selected_trajectory_id": None,
        "events": [{"event": "deliberate_abstention"}],
        "resource_usage": {
            "operational_cost": 1,
            "coordination_cost": 0,
            "latency_steps": 1
        }
    }
