"""Verify the R01 C02 neutral-harness Stage-0 instrumentation controls.

No network, vendor runtime, human process or real technology is invoked.
Controls reuse testbed patterns demonstrated in Nelson Trasatti's UC-4 /
Theme #13 Stage-0 calibration: frozen expected outcomes, deterministic replay,
case-order metamorphism and isolated malformed-record rejection.
"""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path

from harness import assert_oracle_blind, load_json, run_case
from tool_broker import R01ToolBroker

HERE = Path(__file__).resolve().parent


def outcome(result):
    return result.get("post_run_evaluation", {}).get("status", result.get("status"))


def run_bundle(worlds, sidecar, adapter_path):
    results = {}
    for world in worlds:
        assert_oracle_blind(world["participant_view"])
        result = run_case(world, sidecar, adapter_path)
        status = outcome(result)
        results[world["test_vector_id"]] = {
            "status": status,
            "candidate_trace_sha256": result.get("candidate_trace_sha256_before_oracle"),
            "result": result,
        }
    return results


def adapter_sidecar(sidecar, *, adapter_id, adapter_path):
    changed = deepcopy(sidecar)
    changed["r01"]["adapter"]["id"] = adapter_id
    changed["r01"]["adapter"]["version"] = "0.1"
    changed["r01"]["adapter"]["path"] = adapter_path
    return changed


def run_tool_broker_controls():
    profile = load_json(HERE / "fixtures/stage0/tool_profile.json")

    broker = R01ToolBroker(profile)
    explore_i = broker.call({"operation": "explore", "target_id": "I"})
    assert_oracle_blind(explore_i)
    if broker.cost != 2 or broker.clock != 1:
        raise AssertionError("explore charge/duration mismatch")

    relation_p = broker.call({"operation": "inspect_relation", "target_id": "rel-P"})
    assert_oracle_blind(relation_p)
    if relation_p.get("compatibility") != "INCOMPATIBILITY_DETECTED":
        raise AssertionError("declared visible incompatibility was not returned")

    mandate = broker.call({"operation": "query_mandate", "target_id": "mission"})
    assert_oracle_blind(mandate)

    execute_i = broker.call({"operation": "execute", "target_id": "I"})
    assert_oracle_blind(execute_i)
    if broker.cost != 5 or broker.clock != 4:
        raise AssertionError("tool ledger mismatch after accepted operations")

    public = broker.public_receipt()
    assert_oracle_blind(public)
    if any("private_adjudication" in event for event in public["events"]):
        raise AssertionError("private adjudication leaked into public trace")

    private = broker.private_environment_trace()
    if private[-1].get("private_adjudication", {}).get("executed_violation") is not False:
        raise AssertionError("private execution adjudication missing")

    # Hard resource rejection occurs before effect and does not consume operation charge/time.
    rejected = broker.call({"operation": "explore", "target_id": "P"})
    if rejected.get("status") != "RESOURCE_REJECTED":
        raise AssertionError("resource ceiling did not reject oversized next operation")
    if broker.cost != 5 or broker.clock != 4:
        raise AssertionError("resource rejection incorrectly consumed operation charge/time")

    # Known operation + invalid target is recorded and charged, without hidden state.
    syntax_broker = R01ToolBroker(profile)
    bad_target = syntax_broker.call({"operation": "inspect_relation", "target_id": "does-not-exist"})
    assert_oracle_blind(bad_target)
    if bad_target.get("status") != "REQUEST_REJECTED" or syntax_broker.cost != 1 or syntax_broker.clock != 1:
        raise AssertionError("syntactic/catalog rejection accounting mismatch")

    # An unreviewed prohibited execution can occur in the synthetic world; violation is oracle-side only.
    violation_broker = R01ToolBroker(profile)
    public_execution = violation_broker.call({"operation": "execute", "target_id": "P"})
    assert_oracle_blind(public_execution)
    if "executed_violation" in public_execution:
        raise AssertionError("execution response leaked evaluator violation verdict")
    private_execution = violation_broker.private_environment_trace()[-1]["private_adjudication"]
    if private_execution.get("executed_violation") is not True:
        raise AssertionError("private environment did not retain executed violation")

    return "PASS"


def main() -> None:
    sidecar = load_json(HERE / "fixtures/stage0/experiment_sidecar.json")
    bundle = load_json(HERE / "fixtures/stage0/worlds.json")
    expected = load_json(HERE / "fixtures/stage0/expected_selftest.json")["expected_status"]
    worlds = list(bundle["worlds"])
    normal_adapter = HERE / sidecar["r01"]["adapter"]["path"]

    first = run_bundle(worlds, sidecar, normal_adapter)

    for vector_id, expected_status in expected.items():
        if first[vector_id]["status"] != expected_status:
            raise AssertionError(
                f"{vector_id}: expected {expected_status}, got {first[vector_id]['status']}"
            )

    for item in first.values():
        result = item["result"]
        if item["status"] != "INFRASTRUCTURE_ERROR" and "reference_primary" in result:
            if result["reference_primary"]["reference_status"] != result["reference_secondary"]["reference_status"]:
                raise AssertionError("reference status mismatch")
            if result["reference_primary"].get("optimum_J") != result["reference_secondary"].get("optimum_J"):
                raise AssertionError("reference optimum mismatch")
            if result["reference_primary"].get("optimum_trajectory_ids") != result["reference_secondary"].get("optimum_trajectory_ids"):
                raise AssertionError("reference optimum-id mismatch")
            if not result["candidate_trace_sha256_before_oracle"]:
                raise AssertionError("candidate trace was not sealed")

    # Nelson-inspired deterministic replay: same frozen case -> same sealed candidate trace.
    replay = run_bundle(worlds, sidecar, normal_adapter)
    for vector_id in first:
        if first[vector_id]["status"] != replay[vector_id]["status"]:
            raise AssertionError(f"{vector_id}: replay status changed")
        if first[vector_id]["candidate_trace_sha256"] != replay[vector_id]["candidate_trace_sha256"]:
            raise AssertionError(f"{vector_id}: deterministic replay hash changed")

    # Nelson-inspired metamorphic control: case order must not alter a stateless Stage-0 result.
    reversed_run = run_bundle(list(reversed(worlds)), sidecar, normal_adapter)
    for vector_id in first:
        if first[vector_id]["status"] != reversed_run[vector_id]["status"]:
            raise AssertionError(f"{vector_id}: case-order reversal changed status")
        if first[vector_id]["candidate_trace_sha256"] != reversed_run[vector_id]["candidate_trace_sha256"]:
            raise AssertionError(f"{vector_id}: case-order reversal changed candidate hash")

    # Explicit private/oracle-field leak negative control.
    try:
        assert_oracle_blind({"candidate": {"admissible": True}})
    except ValueError:
        leak_control = "PASS"
    else:
        raise AssertionError("oracle-blindness negative control did not detect private key")

    # Malformed adapter output is a candidate-contract rejection, not an infrastructure error.
    malformed_sidecar = adapter_sidecar(
        sidecar,
        adapter_id="R01-SELFTEST-MALFORMED",
        adapter_path="adapters/malformed_selftest_adapter.py",
    )
    malformed = run_case(
        worlds[0],
        malformed_sidecar,
        HERE / malformed_sidecar["r01"]["adapter"]["path"],
    )
    if malformed.get("status") != "FAIL" or malformed.get("reason") != "CANDIDATE_CONTRACT_REJECTED":
        raise AssertionError("malformed candidate record was not explicitly rejected")

    # Rejection of one malformed result must not contaminate a valid vector.
    after_malformed = run_case(worlds[0], sidecar, normal_adapter)
    if outcome(after_malformed) != expected[worlds[0]["test_vector_id"]]:
        raise AssertionError("malformed-record control contaminated subsequent valid execution")

    # Anti-shortcut: permanent abstention on a case with a valid attainable result is not success.
    abstain_sidecar = adapter_sidecar(
        sidecar,
        adapter_id="R01-SELFTEST-ALWAYS-ABSTAIN",
        adapter_path="adapters/abstain_selftest_adapter.py",
    )
    abstain = run_case(
        worlds[0],
        abstain_sidecar,
        HERE / abstain_sidecar["r01"]["adapter"]["path"],
    )
    abstain_eval = abstain.get("post_run_evaluation", {})
    if abstain_eval.get("status") != "FAIL" or abstain_eval.get("completion") is not False:
        raise AssertionError("always-abstain shortcut was not rejected as non-completion")
    if abstain_eval.get("executed_violation") is not False:
        raise AssertionError("abstention must remain distinct from an executed violation")

    tool_broker_control = run_tool_broker_controls()

    summary = {
        "instrument": "R01-C02-neutral-harness-0.2",
        "result": "SELFTEST_PASS",
        "vectors": [
            {"test_vector_id": vector_id, "status": first[vector_id]["status"]}
            for vector_id in expected
        ],
        "controls": {
            "two_reference_methods_agree": "PASS",
            "deterministic_replay_hash": "PASS",
            "case_order_reversal": "PASS",
            "oracle_blindness_negative_control": leak_control,
            "malformed_candidate_explicit_rejection": "PASS",
            "malformed_record_isolation": "PASS",
            "always_abstain_not_success": "PASS",
            "tool_broker_visibility_accounting": tool_broker_control,
        },
        "claim": "instrumentation self-test only; no real technology executed",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
