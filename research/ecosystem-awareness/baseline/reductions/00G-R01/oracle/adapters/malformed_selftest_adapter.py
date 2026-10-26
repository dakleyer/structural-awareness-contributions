"""Deliberately malformed R01 adapter result for harness rejection testing."""

ADAPTER_MANIFEST = {
    "adapter_id": "R01-SELFTEST-MALFORMED",
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
        "selected_trajectory_id": observation["candidates"][0]["trajectory_id"],
        "events": [{"event": "deliberately_malformed_result"}]
    }
