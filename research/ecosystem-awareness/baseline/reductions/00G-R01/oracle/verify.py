"""Verify the first R01 C02 neutral-harness self-test.

No network, vendor runtime or real technology is invoked.
"""

from __future__ import annotations

import json
from pathlib import Path

from harness import assert_oracle_blind, load_json, run_case

HERE = Path(__file__).resolve().parent


def main() -> None:
    sidecar = load_json(HERE / "fixtures/stage0/experiment_sidecar.json")
    bundle = load_json(HERE / "fixtures/stage0/worlds.json")
    expected = load_json(HERE / "fixtures/stage0/expected_selftest.json")["expected_status"]
    adapter_path = HERE / sidecar["r01"]["adapter"]["path"]

    results = []
    for world in bundle["worlds"]:
        assert_oracle_blind(world["participant_view"])
        result = run_case(world, sidecar, adapter_path)
        status = result.get("post_run_evaluation", {}).get("status", result.get("status"))
        if status != expected[world["test_vector_id"]]:
            raise AssertionError(f"{world['test_vector_id']}: expected {expected[world['test_vector_id']]}, got {status}")
        if status != "INFRASTRUCTURE_ERROR":
            if result["reference_primary"]["reference_status"] != result["reference_secondary"]["reference_status"]:
                raise AssertionError("reference status mismatch")
            if result["reference_primary"].get("optimum_J") != result["reference_secondary"].get("optimum_J"):
                raise AssertionError("reference optimum mismatch")
            if result["reference_primary"].get("optimum_trajectory_ids") != result["reference_secondary"].get("optimum_trajectory_ids"):
                raise AssertionError("reference optimum-id mismatch")
            if not result["candidate_trace_sha256_before_oracle"]:
                raise AssertionError("candidate trace was not sealed")
        results.append({"test_vector_id": world["test_vector_id"], "status": status})

    try:
        assert_oracle_blind({"candidate": {"admissible": True}})
    except ValueError:
        leak_control = "PASS"
    else:
        raise AssertionError("oracle-blindness negative control did not detect private key")

    print(json.dumps({
        "instrument": "R01-C02-neutral-harness-0.1",
        "result": "SELFTEST_PASS",
        "vectors": results,
        "oracle_blindness_negative_control": leak_control,
        "claim": "instrumentation self-test only; no real technology executed"
    }, sort_keys=True))


if __name__ == "__main__":
    main()
