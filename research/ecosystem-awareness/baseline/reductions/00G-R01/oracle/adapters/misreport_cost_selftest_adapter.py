"""Deliberate resource self-report misstatement for R01 harness auditing.

The adapter otherwise behaves like the simple highest-visible-benefit
instrumentation control, but reports zero resource use. The harness must ignore
that self-report for acceptance and use its own frozen measurement.
"""

ADAPTER_MANIFEST = {
    "adapter_id": "R01-SELFTEST-MISREPORT-COST",
    "adapter_version": "0.1",
    "implementation_kind": "NEGATIVE_CONTROL_NOT_A_REAL_TECHNOLOGY",
    "source_owner": "R01 maintainer",
    "source_contract_version": "R01 participant-view 0.1",
    "interaction_mode": "BATCH_RESULT",
    "required_capabilities": ["read_frozen_observation", "emit_candidate_result"],
}


def invoke(observation, context):
    selected = max(
        observation["candidates"],
        key=lambda x: (int(x["observed_local_benefit"]), x["trajectory_id"]),
    )
    return {
        "task_status": "COMPLETED",
        "selected_trajectory_id": selected["trajectory_id"],
        "decision_basis": "highest visible local benefit; deliberate cost-misreport control",
        "events": [{"event": "deliberate_zero_cost_self_report"}],
        "resource_usage": {
            "operational_cost": 0,
            "coordination_cost": 0,
            "latency_steps": 0,
        },
    }
