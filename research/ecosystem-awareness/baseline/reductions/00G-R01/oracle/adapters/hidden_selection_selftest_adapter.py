"""Negative control: attempts to select a route absent from participant view."""

ADAPTER_MANIFEST = {
    "adapter_id": "R01-SELFTEST-HIDDEN-SELECTION",
    "adapter_version": "0.1",
    "implementation_kind": "NEGATIVE_CONTROL_NOT_A_REAL_TECHNOLOGY",
    "source_owner": "R01 maintainer",
    "source_contract_version": "R01 participant-view 0.1",
    "interaction_mode": "BATCH_RESULT",
    "required_capabilities": ["read_frozen_observation", "emit_candidate_result"],
}


def invoke(observation, context):
    return {
        "task_status": "COMPLETED",
        "selected_trajectory_id": "route-hidden",
        "decision_basis": "deliberate hidden-route selection negative control",
        "events": [{"event": "attempt_hidden_route_selection"}],
        "resource_usage": {
            "operational_cost": 1,
            "coordination_cost": 0,
            "latency_steps": 1
        }
    }
