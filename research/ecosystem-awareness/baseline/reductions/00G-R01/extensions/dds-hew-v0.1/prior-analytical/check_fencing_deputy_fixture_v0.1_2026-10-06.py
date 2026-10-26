"""Bounded analytical witnesses, not a distributed lock or authorization service.

Run: bundled python this_file.py
Writes a new result; refuses to overwrite an existing result.
"""
import hashlib
import itertools
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CARD = ROOT / "fencing_deputy_run_card_v0.1_2026-10-06.json"
OUT = ROOT / "fencing_deputy_results_v0.1_2026-10-06.json"
REQUIRED = {
    "principal": "principal-A", "actor": "case-service", "tenant": "A",
    "case": "HEW-001", "decision": "D-001", "resource": "actuator-A",
    "action": "apply-safe-pause", "purpose": "HEW-remediation", "audience": "actuator-A",
}


def fence_ok(req, floor):
    # Native verification, exclusive issuer and resource/owner binding are stipulations.
    return (req["token_verified"] and type(req["epoch"]) is int
            and req["epoch"] >= floor
            and req["token_resource"] == req["resource"]
            and req["token_actor"] == req["actor"])


def delegation_ok(req):
    return (req["identity_accepted"] and req["delegation_verified"]
            and req["policy_known"] and req["grant_active"]
            and req["now"] < req["expires"]
            and all(req[k] == value for k, value in REQUIRED.items()))


def atomic_trace(events, initial_floor):
    floor = initial_floor
    writes = []
    rejects = []
    for event, generation in events:
        if event == "install":
            floor = max(floor, generation)
        elif generation < floor:
            rejects.append(generation)
        else:
            writes.append(generation)
            floor = generation
    return {"floor": floor, "writes": writes, "rejects": rejects}


def race_trace(order, recheck_at_commit):
    floor = 42
    checked = {}
    writes = []
    for event in order:
        generation = int(event[-2:])
        if event.startswith("check"):
            checked[generation] = generation >= floor
        elif checked[generation] and (not recheck_at_commit or generation >= floor):
            writes.append(generation)
            floor = max(floor, generation)
    return {"writes": writes,
            "generation_regression": any(b < a for a, b in zip(writes, writes[1:]))}


def main():
    card = json.loads(CARD.read_text(encoding="utf-8"))
    rows = []
    for case in card["cases"]:
        req = {**card["default_request"], **case["overrides"]}
        floor = case.get("floor", card["default_floor"])
        fenced = fence_ok(req, floor)
        delegated = delegation_ok(req)
        combined = fenced and delegated
        # This small suffix uses stipulated review gates. It is not a full HEW evaluator.
        actual = {"fencing_only": fenced, "delegation_only": delegated,
                  "combined": combined,
                  "conditional_hew_path": combined and req["basis_sufficient"] and req["human_capacity"]}
        assert actual == case["expected"], (case["id"], actual, case["expected"])
        rows.append({"id": case["id"], "name": case["name"], "floor": floor,
                     "request": req, "actual": actual, "expected": case["expected"], "matched": True})

    grid = card["finite_trace_grid"]
    events = list(itertools.product(grid["event_types"], grid["generations"]))
    trace_count = 0
    accepted_count = 0
    rejected_count = 0
    for sequence in itertools.product(events, repeat=grid["sequence_length"]):
        trace = atomic_trace(sequence, grid["initial_floor"])
        # Separately audit each observed prefix against the history maximum, not an
        # expected array copied from the implementation's final outcome.
        history = [grid["initial_floor"]]
        expected_writes = []
        expected_rejects = []
        for kind, epoch in sequence:
            if kind == "install":
                history.append(epoch)
            elif epoch >= max(history):
                expected_writes.append(epoch)
                history.append(epoch)
            else:
                expected_rejects.append(epoch)
        assert trace["writes"] == expected_writes
        assert trace["rejects"] == expected_rejects
        assert trace["floor"] == max(history)
        assert all(a <= b for a, b in zip(trace["writes"], trace["writes"][1:]))
        trace_count += 1
        accepted_count += len(trace["writes"])
        rejected_count += len(trace["rejects"])

    races = []
    for order in itertools.permutations(card["race_grid"]["events"]):
        if not all(order.index(f"check{x}") < order.index(f"commit{x}") for x in (42, 43)):
            continue
        broken = race_trace(order, False)
        atomic = race_trace(order, True)
        assert not atomic["generation_regression"]
        races.append({"order": order, "check_then_unchecked_commit": broken,
                      "atomic_resource_recheck": atomic})
    race_failures = sum(row["check_then_unchecked_commit"]["generation_regression"] for row in races)
    assert len(races) == 6 and race_failures == 2

    same_generation = atomic_trace([("write", 43), ("write", 43)], 43)
    assert same_generation["writes"] == [43, 43]
    request_ids = ["request-1", "request-1", "request-2"]
    assert len(request_ids) == 3 and len(set(request_ids)) == 2
    preserved = atomic_trace([("write", 42)], 43)
    rolled_back = atomic_trace([("write", 42)], 0)
    assert preserved["writes"] == [] and rolled_back["writes"] == [42]
    history = atomic_trace([("write", 42), ("install", 43)], 42)
    assert history["writes"] == [42]  # later floor advancement does not undo an effect
    guarded = atomic_trace([("write", 42)], 43)["writes"]
    unguarded = [42]  # explicitly adversarial surface outside the admitted guard
    assert guarded == [] and unguarded == [42]

    result = {
        "run_id": card["run_id"], "version": "0.1",
        "executed_at_utc": datetime.now(timezone.utc).isoformat(),
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "card_sha256": hashlib.sha256(CARD.read_bytes()).hexdigest(),
        "status": "PASS within the declared analytical model",
        "cases_matched": len(rows), "cases": rows,
        "trace_grid": {"sequences": trace_count,
                       "events_evaluated": trace_count * grid["sequence_length"],
                       "accepted_writes_across_grid": accepted_count,
                       "rejected_writes_across_grid": rejected_count,
                       "generation_regressions_under_atomic_guard": 0},
        "races": {"legal_interleavings": len(races),
                  "regressions_with_check_then_unchecked_commit": race_failures,
                  "regressions_with_atomic_resource_recheck": 0, "traces": races},
        "additional_witnesses": {
            "same_generation_distinct_operations": same_generation,
            "repeated_request_ids": {"without_idempotency_effect_count": len(request_ids),
                                     "with_request_id_deduplication_effect_count": len(set(request_ids))},
            "floor_preserved": preserved, "floor_rolled_back": rolled_back,
            "later_fence_preserves_earlier_effect_history": history,
            "effect_path_coverage": {"guarded": guarded, "unguarded": unguarded}},
        "unexecuted": card["evidence_limits"],
        "field_warning": "conditional_hew_path is only the combined predicate plus two stipulated gates, not protected-channel or full mission conformance",
        "comparative_warning": "mechanism ablations are explanatory constructions; a competent peer with both guards can obtain the same outcomes"
    }
    # Avoid rewriting a prior result, including on a routine verification rerun.
    with OUT.open("x", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    print(json.dumps({"result": str(OUT), "cases": len(rows), "sequences": trace_count,
                      "race_interleavings": len(races), "broken_race_witnesses": race_failures,
                      "status": result["status"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
