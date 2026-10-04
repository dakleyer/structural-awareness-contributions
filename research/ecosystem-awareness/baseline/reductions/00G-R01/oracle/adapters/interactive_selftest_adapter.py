"""Interactive instrumentation adapter for the R01 tool-broker path.

Not a real technology or comparator. It demonstrates that an adapter can use
only neutral handles and the admitted broker operations.
"""

ADAPTER_MANIFEST = {
    "adapter_id": "R01-SELFTEST-INTERACTIVE-REVIEW",
    "adapter_version": "0.1",
    "implementation_kind": "INSTRUMENTATION_CONTROL_NOT_A_REAL_TECHNOLOGY",
    "source_owner": "R01 maintainer",
    "source_contract_version": "R01 tool broker 0.1",
    "interaction_mode": "INTERACTIVE_TOOL_BROKER",
    "required_capabilities": [
        "explore",
        "inspect_relation",
        "query_mandate",
        "decide",
        "execute",
        "stop"
    ],
}


def run_session(observation, tool_call, context):
    events = []
    observed = []

    for item in observation["candidate_handles"]:
        response = tool_call({"operation": "explore", "target_id": item["candidate_id"]})
        events.append({"operation": "explore", "response": response})
        if response.get("status") not in {"RESOURCE_REJECTED", "REQUEST_REJECTED"}:
            observed.append((int(response["observed_benefit"]), item))

    observed.sort(key=lambda x: (x[0], x[1]["candidate_id"]), reverse=True)
    selected = None
    for _, item in observed:
        relation = tool_call({"operation": "inspect_relation", "target_id": item["relation_id"]})
        events.append({"operation": "inspect_relation", "response": relation})
        if relation.get("compatibility") == "INCOMPATIBILITY_DETECTED":
            continue
        if relation.get("status") in {"RESOURCE_REJECTED", "REQUEST_REJECTED"}:
            continue
        selected = item["candidate_id"]
        break

    if selected is None:
        tool_call({"operation": "stop"})
        return {
            "task_status": "ABSTAINED",
            "selected_trajectory_id": None,
            "events": events + [{"event": "no_candidate_survived_review"}],
        }

    mandate = tool_call({"operation": "query_mandate", "target_id": observation["mandate_id"]})
    events.append({"operation": "query_mandate", "response": mandate})

    decision = tool_call({"operation": "decide", "target_id": selected, "decision": "COMMIT"})
    events.append({"operation": "decide", "response": decision})

    execution = tool_call({"operation": "execute", "target_id": selected})
    events.append({"operation": "execute", "response": execution})

    stop = tool_call({"operation": "stop"})
    events.append({"operation": "stop", "response": stop})

    return {
        "task_status": "COMPLETED",
        "selected_trajectory_id": selected,
        "events": events,
    }
