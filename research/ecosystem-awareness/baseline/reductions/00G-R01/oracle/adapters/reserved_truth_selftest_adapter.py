"""Negative control: candidate attempts to emit an oracle-reserved truth field."""

ADAPTER_MANIFEST = {
    "adapter_id": "R01-SELFTEST-RESERVED-TRUTH",
    "adapter_version": "0.1",
    "implementation_kind": "NEGATIVE_CONTROL_NOT_A_REAL_TECHNOLOGY",
    "source_owner": "R01 maintainer",
    "source_contract_version": "R01 participant-view 0.1",
    "interaction_mode": "BATCH_RESULT",
    "required_capabilities": ["read_frozen_observation", "emit_candidate_result"],
}


def invoke(observation, context):
    selected = observation["candidates"][0]["trajectory_id"]
    return {
        "task_status": "COMPLETED",
        "selected_trajectory_id": selected,
        "decision_basis": "deliberate reserved-oracle-namespace negative control",
        "events": [{"event": "candidate_claim", "optimum_J": 999}],
        "resource_usage": {
            "operational_cost": 1,
            "coordination_cost": 0,
            "latency_steps": 1
        }
    }
