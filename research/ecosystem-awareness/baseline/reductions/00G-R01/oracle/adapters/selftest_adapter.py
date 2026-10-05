"""Instrumentation-only adapter for R01 C02 Stage-0.

It selects the visible candidate with the largest observed local benefit.
It deliberately does not inspect hidden admissibility, connector truth or oracle
results. Mixed PASS/FAIL results are expected and test harness discrimination.
"""

ADAPTER_MANIFEST = {
    "adapter_id": "R01-SELFTEST-HIGHEST-VISIBLE-BENEFIT",
    "adapter_version": "0.1",
    "implementation_kind": "INSTRUMENTATION_CONTROL_NOT_A_REAL_TECHNOLOGY",
    "source_owner": "R01 maintainer",
    "source_contract_version": "R01 participant-view 0.1",
    "interaction_mode": "BATCH_RESULT",
    "required_capabilities": ["read_frozen_observation", "emit_candidate_result"],
}


def invoke(observation, context):
    candidates = list(observation["candidates"])
    if not candidates:
        return {
            "task_status": "ABSTAINED",
            "selected_trajectory_id": None,
            "events": [{"event": "no_visible_candidate"}],
            "resource_usage": {"operational_cost": 1, "coordination_cost": 0, "latency_steps": 1},
        }

    selected = max(candidates, key=lambda x: (int(x["observed_local_benefit"]), x["trajectory_id"]))
    return {
        "task_status": "COMPLETED",
        "selected_trajectory_id": selected["trajectory_id"],
        "events": [
            {"event": "candidate_observed", "trajectory_id": x["trajectory_id"], "observed_local_benefit": int(x["observed_local_benefit"])}
            for x in candidates
        ] + [{"event": "trajectory_selected", "trajectory_id": selected["trajectory_id"]}],
        "resource_usage": {
            "operational_cost": len(candidates) + 1,
            "coordination_cost": 0,
            "latency_steps": len(candidates) + 1,
        },
    }
