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
from interactive_harness import run_interactive_case
from contracts import (
    ContractError,
    validate_interactive_case,
    validate_sidecar,
    validate_tool_profile,
    validate_world_bundle,
)
from reference import evaluate_world
from reference_secondary import evaluate_world_secondary
from integrity import load_and_verify

HERE = Path(__file__).resolve().parent

REQUIRED_FREEZE_PATHS = {
    "adapter_api.py",
    "canonical_trace_v1.py",
    "contracts.py",
    "harness.py",
    "integrity.py",
    "interactive_harness.py",
    "reference.py",
    "reference_secondary.py",
    "tool_broker.py",
    "verify.py",
    "schemas/r01_uc4_sidecar.schema.json",
    "fixtures/stage0/experiment_sidecar.json",
    "fixtures/stage0/worlds.json",
    "fixtures/stage0/expected_selftest.json",
    "fixtures/stage0/tool_profile.json",
    "fixtures/stage0/interactive_tool_profile.json",
    "fixtures/stage0/interactive_case.json",
    "adapters/selftest_adapter.py",
    "adapters/malformed_selftest_adapter.py",
    "adapters/abstain_selftest_adapter.py",
    "adapters/misreport_cost_selftest_adapter.py",
    "adapters/interactive_selftest_adapter.py",
}


def verify_stage0_freeze():
    manifest_path = HERE / "STAGE0_FREEZE_v0.4.json"
    result = load_and_verify(HERE, manifest_path)
    manifest = load_json(manifest_path)
    frozen_paths = {entry["path"] for entry in manifest["files"]}
    missing = sorted(REQUIRED_FREEZE_PATHS - frozen_paths)
    if missing:
        raise AssertionError(f"freeze manifest omitted required Stage-0 paths: {missing}")
    return result


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


def permute_world_ids(world):
    changed = deepcopy(world)
    ids = [x["trajectory_id"] for x in changed["participant_view"]["candidates"]]
    mapping = {
        old: f"perm-{len(ids) - index:02d}"
        for index, old in enumerate(ids)
    }
    for candidate in changed["participant_view"]["candidates"]:
        candidate["trajectory_id"] = mapping[candidate["trajectory_id"]]
    for trajectory in changed["private_world"]["trajectories"]:
        trajectory["trajectory_id"] = mapping[trajectory["trajectory_id"]]
    return changed


def adapter_sidecar(sidecar, *, adapter_id, adapter_path):
    changed = deepcopy(sidecar)
    changed["r01"]["adapter"]["id"] = adapter_id
    changed["r01"]["adapter"]["version"] = "0.1"
    changed["r01"]["adapter"]["path"] = adapter_path
    return changed


def run_tool_broker_controls():
    profile = load_json(HERE / "fixtures/stage0/tool_profile.json")
    strict_profile = load_json(HERE / "fixtures/stage0/interactive_tool_profile.json")
    validate_tool_profile(profile)
    validate_tool_profile(strict_profile)

    if profile.get("state_machine", {}).get("enabled") is not False:
        raise AssertionError("low-level behavioural control must explicitly disable the state machine")

    broker = R01ToolBroker(profile)
    explore_i = broker.call({"operation": "explore", "target_id": "cand-01"})
    assert_oracle_blind(explore_i)
    if broker.cost != 2 or broker.clock != 1:
        raise AssertionError("explore charge/duration mismatch")

    relation_p = broker.call({"operation": "inspect_relation", "target_id": "rel-02"})
    assert_oracle_blind(relation_p)
    if relation_p.get("compatibility") != "INCOMPATIBILITY_DETECTED":
        raise AssertionError("declared visible incompatibility was not returned")

    mandate = broker.call({"operation": "query_mandate", "target_id": "mission"})
    assert_oracle_blind(mandate)

    execute_i = broker.call({"operation": "execute", "target_id": "cand-01"})
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
    rejected = broker.call({"operation": "explore", "target_id": "cand-02"})
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
    public_execution = violation_broker.call({"operation": "execute", "target_id": "cand-02"})
    assert_oracle_blind(public_execution)
    if "executed_violation" in public_execution:
        raise AssertionError("execution response leaked evaluator violation verdict")
    private_execution = violation_broker.private_environment_trace()[-1]["private_adjudication"]
    if private_execution.get("executed_violation") is not True:
        raise AssertionError("private environment did not retain executed violation")

    # Standard operational profile: direct execution without review/commitment is rejected.
    strict_broker = R01ToolBroker(strict_profile)
    state_reject = strict_broker.call({"operation": "execute", "target_id": "cand-01"})
    assert_oracle_blind(state_reject)
    if state_reject.get("status") != "STATE_REJECTED":
        raise AssertionError("strict broker allowed execution without commitment")
    if strict_broker.cost != 1 or strict_broker.clock != 1:
        raise AssertionError("state rejection did not follow declared charge/duration")
    strict_private = strict_broker.private_environment_trace()[-1]
    if "private_adjudication" in strict_private:
        raise AssertionError("state-rejected execution exposed or applied private effect")

    return "PASS"


def main() -> None:
    freeze_result = verify_stage0_freeze()
    sidecar = load_json(HERE / "fixtures/stage0/experiment_sidecar.json")
    bundle = load_json(HERE / "fixtures/stage0/worlds.json")
    expected = load_json(HERE / "fixtures/stage0/expected_selftest.json")["expected_status"]
    worlds = list(bundle["worlds"])
    normal_adapter = HERE / sidecar["r01"]["adapter"]["path"]

    # Semantic admission precedes any candidate execution.
    validate_sidecar(sidecar)
    validate_world_bundle(bundle, sidecar=sidecar, expected_status=expected)

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

    # R01 §2.17 accidental-hint control: identifier permutation must not alter
    # the substantive evaluation for this benefit-driven instrumentation adapter.
    permuted_run = run_bundle([permute_world_ids(w) for w in worlds], sidecar, normal_adapter)
    for vector_id in first:
        if first[vector_id]["status"] != permuted_run[vector_id]["status"]:
            raise AssertionError(f"{vector_id}: identifier permutation changed substantive status")

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
    if abstain_eval.get("executed_violation") is not None:
        raise AssertionError("batch abstention must not manufacture an executed-violation verdict")
    if abstain_eval.get("would_be_violation_if_executed") is not False:
        raise AssertionError("abstention should not be classified as a hypothetical executed violation")

    # Batch cost self-report is diagnostic only. A deliberate zero-cost report must
    # not change the harness-authoritative cost/deadline failure.
    cost_world = next(w for w in worlds if w["test_vector_id"] == "R01-COST-LIMIT-01")
    misreport_sidecar = adapter_sidecar(
        sidecar,
        adapter_id="R01-SELFTEST-MISREPORT-COST",
        adapter_path="adapters/misreport_cost_selftest_adapter.py",
    )
    misreport = run_case(
        cost_world,
        misreport_sidecar,
        HERE / misreport_sidecar["r01"]["adapter"]["path"],
    )
    if outcome(misreport) != "FAIL":
        raise AssertionError("adapter resource self-report changed authoritative batch outcome")
    if misreport["candidate"]["resource_usage"]["operational_cost"] != 11:
        raise AssertionError("batch harness did not override adapter cost with authoritative measurement")
    if misreport["resource_ledger"]["adapter_self_report_matches_authoritative"] is not False:
        raise AssertionError("deliberate resource self-report mismatch was not detected")

    # Without an authoritative batch measurement the result must be inconclusive.
    unmeasured_world = deepcopy(worlds[0])
    unmeasured_world.pop("harness_resource_measurement", None)
    unmeasured = run_case(unmeasured_world, sidecar, normal_adapter)
    if unmeasured.get("status") != "INCONCLUSIVE" or unmeasured.get("reason") != "NO_AUTHORITATIVE_BATCH_RESOURCE_MEASUREMENT":
        raise AssertionError("batch result without harness measurement was not kept inconclusive")

    tool_broker_control = run_tool_broker_controls()

    # Reference methods must reject ambiguous JSON-like typing rather than coerce
    # strings such as "false" into truthy values.
    bad_reference_world = {
        "trajectories": [
            {
                "trajectory_id": "bad",
                "steps": [{"benefit": 1, "admissible": "false"}],
            }
        ]
    }
    for checker in (evaluate_world, evaluate_world_secondary):
        try:
            checker(bad_reference_world)
        except ValueError:
            pass
        else:
            raise AssertionError("reference method accepted non-boolean admissibility")

    # Admission must also reject a negative-benefit world in the NONNEGATIVE_BASE bundle.
    bad_bundle = deepcopy(bundle)
    bad_bundle["worlds"][0]["private_world"]["trajectories"][0]["steps"][0]["benefit"] = -1
    try:
        validate_world_bundle(bad_bundle, sidecar=sidecar, expected_status=expected)
    except ContractError:
        pass
    else:
        raise AssertionError("NONNEGATIVE_BASE admission accepted a negative benefit")

    # End-to-end interactive adapter -> broker -> sealed trace -> private oracle.
    interactive_case = load_json(HERE / "fixtures/stage0/interactive_case.json")
    interactive_profile = load_json(HERE / "fixtures/stage0/interactive_tool_profile.json")
    validate_tool_profile(interactive_profile)
    validate_interactive_case(interactive_case, tool_profile=interactive_profile)
    interactive_sidecar = adapter_sidecar(
        sidecar,
        adapter_id="R01-SELFTEST-INTERACTIVE-REVIEW",
        adapter_path="adapters/interactive_selftest_adapter.py",
    )
    interactive_sidecar["r01"]["adapter"]["required_capabilities"] = [
        "explore", "inspect_relation", "query_mandate", "decide", "execute", "stop"
    ]
    interactive = run_interactive_case(
        interactive_case,
        interactive_sidecar,
        interactive_profile,
        HERE / interactive_sidecar["r01"]["adapter"]["path"],
    )
    interactive_eval = interactive.get("post_run_evaluation", {})
    if interactive_eval.get("status") != "PASS":
        raise AssertionError(f"interactive broker path did not pass: {interactive_eval}")
    if interactive["candidate"]["selected_trajectory_id"] != "cand-01":
        raise AssertionError("interactive adapter did not reject the visible incompatible candidate")
    if interactive["candidate"]["resource_usage"]["operational_cost"] != 9:
        raise AssertionError("interactive broker authoritative cost mismatch")
    if interactive["candidate"]["resource_usage"]["latency_steps"] != 7:
        raise AssertionError("interactive broker authoritative latency mismatch")
    assert_oracle_blind(interactive["public_tool_trace"])

    interactive_replay = run_interactive_case(
        interactive_case,
        interactive_sidecar,
        interactive_profile,
        HERE / interactive_sidecar["r01"]["adapter"]["path"],
    )
    if (
        interactive["candidate_trace_sha256_before_oracle"]
        != interactive_replay["candidate_trace_sha256_before_oracle"]
    ):
        raise AssertionError("interactive deterministic replay hash changed")

    summary = {
        "instrument": "R01-C02-neutral-harness-0.4",
        "result": "SELFTEST_PASS",
        "vectors": [
            {"test_vector_id": vector_id, "status": first[vector_id]["status"]}
            for vector_id in expected
        ],
        "controls": {
            "freeze_manifest_integrity": f"PASS:{freeze_result['files_checked']}",
            "two_reference_methods_agree": "PASS",
            "deterministic_replay_hash": "PASS",
            "case_order_reversal": "PASS",
            "identifier_permutation": "PASS",
            "oracle_blindness_negative_control": leak_control,
            "malformed_candidate_explicit_rejection": "PASS",
            "malformed_record_isolation": "PASS",
            "always_abstain_not_success": "PASS",
            "batch_resource_self_report_non_authoritative": "PASS",
            "batch_missing_measurement_inconclusive": "PASS",
            "semantic_admission_contracts": "PASS",
            "reference_rejects_ambiguous_types": "PASS",
            "nonnegative_base_rejects_negative_benefit": "PASS",
            "strict_state_machine_blocks_uncommitted_execution": "PASS",
            "tool_broker_visibility_accounting": tool_broker_control,
            "interactive_adapter_broker_oracle_path": "PASS",
            "interactive_adapter_replay_hash": "PASS",
        },
        "claim": "instrumentation self-test only; no real technology executed",
    }
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
