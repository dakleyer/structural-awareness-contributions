#!/usr/bin/env python3
"""DDS Stage A gate-diagnostic checker v0.1.

Validates a gate result against a frozen gate catalog and derives:
- hard dependency status,
- effective gate status,
- named-claim status for unconditional registered requirements,
- root-blocker references,
- potential unlock relationships,
- Stage A remediation and Stage B handoff queues.

It does not execute Stage B/C architecture or implementation tests and it never
turns a recommendation into PASS evidence.
"""

from __future__ import annotations

import argparse
import json
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any

LEVEL_RANK = {"L0": 0, "L1": 1, "L2": 2, "L3": 3, "L4": 4}


class ContractError(ValueError):
    pass


def load_json(path: str) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def gate_map(catalog: dict[str, Any]) -> dict[str, dict[str, Any]]:
    gates = catalog.get("gates", [])
    out = {}
    for gate in gates:
        gid = gate.get("id")
        if not gid or gid in out:
            raise ContractError(f"duplicate_or_missing_gate_id:{gid}")
        out[gid] = gate
    return out


def assert_acyclic_hard_dependencies(gates: dict[str, dict[str, Any]]) -> None:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(gid: str) -> None:
        if gid in visited:
            return
        if gid in visiting:
            raise ContractError(f"hard_dependency_cycle_at:{gid}")
        visiting.add(gid)
        for dep in gates[gid].get("requires_all", []):
            if dep not in gates:
                raise ContractError(f"unknown_hard_dependency:{gid}->{dep}")
            visit(dep)
        visiting.remove(gid)
        visited.add(gid)

    for gid in gates:
        visit(gid)


def level_ok(row: dict[str, Any]) -> bool:
    level = row.get("level")
    minimum = row.get("required_min_level") or "L0"
    if level not in LEVEL_RANK or minimum not in LEVEL_RANK:
        return False
    return LEVEL_RANK[level] >= LEVEL_RANK[minimum]


def validate_result_rows(
    catalog: dict[str, Any], result: dict[str, Any], gates: dict[str, dict[str, Any]]
) -> dict[str, dict[str, Any]]:
    allowed_verdicts = set(catalog.get("verdicts", []))
    allowed_roles = set(catalog.get("test_roles", []))
    allowed_app = set(catalog.get("applicability_values", ["APPLICABLE", "NOT_APPLICABLE"]))

    rows: dict[str, dict[str, Any]] = {}
    for row in result.get("gates", []):
        gid = row.get("gate_id")
        if gid not in gates:
            raise ContractError(f"unknown_result_gate:{gid}")
        if gid in rows:
            raise ContractError(f"duplicate_result_gate:{gid}")
        if row.get("applicability") not in allowed_app:
            raise ContractError(f"invalid_applicability:{gid}:{row.get('applicability')}")
        if row.get("test_role") not in allowed_roles:
            raise ContractError(f"invalid_test_role:{gid}:{row.get('test_role')}")
        if row.get("own_verdict") not in allowed_verdicts:
            raise ContractError(f"invalid_own_verdict:{gid}:{row.get('own_verdict')}")
        if row.get("level") not in LEVEL_RANK:
            raise ContractError(f"invalid_level:{gid}:{row.get('level')}")
        if row.get("required_min_level") not in LEVEL_RANK:
            raise ContractError(
                f"invalid_required_min_level:{gid}:{row.get('required_min_level')}"
            )
        if (
            row.get("applicability") == "NOT_APPLICABLE"
            and row.get("own_verdict") != "NOT_APPLICABLE"
        ):
            raise ContractError(f"na_applicability_requires_na_verdict:{gid}")
        if (
            row.get("applicability") == "APPLICABLE"
            and row.get("own_verdict") == "NOT_APPLICABLE"
        ):
            raise ContractError(f"applicable_gate_cannot_have_na_verdict:{gid}")
        rows[gid] = deepcopy(row)

    missing = sorted(set(gates) - set(rows))
    if missing:
        raise ContractError("missing_gate_rows:" + ",".join(missing))
    return rows


def prerequisite_state(dep_row: dict[str, Any]) -> str:
    verdict = dep_row["own_verdict"]
    if verdict == "PASS":
        return "SATISFIED" if level_ok(dep_row) else "CONDITIONAL"
    if verdict == "NOT_APPLICABLE":
        return "SATISFIED" if dep_row.get("na_substitute_satisfied") else "BLOCKED"
    if verdict == "FAIL":
        return "BLOCKED"
    return "CONDITIONAL"


def derive_gate_status(
    gid: str, row: dict[str, Any], gates: dict[str, dict[str, Any]], rows: dict[str, dict[str, Any]]
) -> tuple[str, str, list[str]]:
    blocked: list[str] = []
    conditional: list[str] = []

    for dep in gates[gid].get("requires_all", []):
        state = prerequisite_state(rows[dep])
        if state == "BLOCKED":
            blocked.append(dep)
        elif state == "CONDITIONAL":
            conditional.append(dep)

    if blocked:
        dep_status = f"BLOCKED_BY({','.join(blocked)})"
        effective = dep_status
        roots = blocked
    elif conditional:
        dep_status = f"CONDITIONAL_ON({','.join(conditional)})"
        effective = dep_status
        roots = conditional
    else:
        dep_status = "SATISFIED"
        roots = []
        if row["own_verdict"] == "NOT_APPLICABLE":
            effective = "NOT_APPLICABLE"
        elif row["own_verdict"] == "FAIL":
            effective = "FAIL"
        elif row["own_verdict"] == "NOT_ESTABLISHED":
            effective = "NOT_ESTABLISHED"
        elif not level_ok(row):
            effective = f"CONDITIONAL_ON(LEVEL>={row['required_min_level']})"
            roots = [gid]
        else:
            effective = "PASS"

    return dep_status, effective, roots


def transitive_downstream(gates: dict[str, dict[str, Any]], root: str) -> set[str]:
    downstream: set[str] = set()
    changed = True
    while changed:
        changed = False
        for gid, gate in gates.items():
            if gid == root or gid in downstream:
                continue
            reqs = set(gate.get("requires_all", []))
            if root in reqs or reqs.intersection(downstream):
                downstream.add(gid)
                changed = True
    return downstream


def unresolved_for_claim(
    claim: dict[str, Any], rows: dict[str, dict[str, Any]]
) -> tuple[list[str], list[str], list[str]]:
    required = list(claim.get("requires", claim.get("stage_a_requires", [])))
    fails: list[str] = []
    conditionals: list[str] = []
    unavailable: list[str] = []
    for gid in required:
        if gid not in rows:
            unavailable.append(gid)
            continue
        eff = rows[gid].get("effective_status")
        if eff == "FAIL":
            fails.append(gid)
        elif eff == "PASS":
            pass
        elif eff == "NOT_APPLICABLE" and rows[gid].get("na_substitute_satisfied"):
            pass
        else:
            conditionals.append(gid)
    return fails, conditionals, unavailable


def derive_claims(catalog: dict[str, Any], rows: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    out = []
    for name, claim in catalog.get("named_claims", {}).items():
        fails, conditional, unavailable = unresolved_for_claim(claim, rows)
        if fails:
            status = f"FAIL({','.join(fails)})"
        elif unavailable:
            status = f"NOT_ESTABLISHED(MISSING:{','.join(unavailable)})"
        elif conditional:
            status = f"CONDITIONAL_ON({','.join(conditional)})"
        else:
            status = "PASS"

        out.append(
            {
                "claim": name,
                "status": status,
                "unresolved_required_gates": conditional,
                "failed_required_gates": fails,
                "manual_conditional_requirements": claim.get("conditional_requires", []),
                "stage_b_required_for_runtime_claim": bool(
                    claim.get("stage_b_required_for_runtime_claim", False)
                ),
            }
        )
    return out


def potential_claim_unlocks(
    catalog: dict[str, Any], root: str
) -> list[str]:
    out = []
    for name, claim in catalog.get("named_claims", {}).items():
        required = set(claim.get("requires", claim.get("stage_a_requires", [])))
        conditional = {x.get("gate") for x in claim.get("conditional_requires", [])}
        if root in required or root in conditional:
            out.append(name)
    return sorted(out)


def compile_result(catalog: dict[str, Any], result: dict[str, Any]) -> dict[str, Any]:
    gates = gate_map(catalog)
    assert_acyclic_hard_dependencies(gates)
    rows = validate_result_rows(catalog, result, gates)

    for gid in gates:
        dep_status, effective, roots = derive_gate_status(gid, rows[gid], gates, rows)
        rows[gid]["dependency_status"] = dep_status
        rows[gid]["effective_status"] = effective
        rows[gid]["blocker_root"] = sorted(set(roots))

    for gid in gates:
        downstream = sorted(transitive_downstream(gates, gid))
        claims = potential_claim_unlocks(catalog, gid)
        rows[gid]["downstream_impacted"] = downstream
        rows[gid]["unlock_candidates"] = claims + downstream

        if rows[gid]["effective_status"] != "PASS":
            if not rows[gid].get("stage_a_remediation"):
                rows[gid]["stage_a_remediation"] = gates[gid].get(
                    "stage_a_remediation_hint"
                )
            if not rows[gid].get("stage_b_handoff"):
                rows[gid]["stage_b_handoff"] = gates[gid].get(
                    "stage_b_handoff_hint"
                )

    claim_results = derive_claims(catalog, rows)

    counts: dict[str, int] = {}
    for row in rows.values():
        key = row["effective_status"].split("(", 1)[0]
        counts[key] = counts.get(key, 0) + 1

    root_blockers = []
    for gid, row in rows.items():
        if row["effective_status"] == "PASS":
            continue
        direct_root = (
            row["own_verdict"] in {"FAIL", "NOT_ESTABLISHED"}
            or not level_ok(row)
            or (
                row["own_verdict"] == "NOT_APPLICABLE"
                and not row.get("na_substitute_satisfied")
            )
        )
        if direct_root:
            root_blockers.append(
                {
                    "gate_id": gid,
                    "effective_status": row["effective_status"],
                    "potential_unlocks": row["unlock_candidates"],
                    "stage_a_remediation": row.get("stage_a_remediation"),
                    "stage_b_handoff": row.get("stage_b_handoff"),
                }
            )

    root_blockers.sort(
        key=lambda x: (-len(x["potential_unlocks"]), x["gate_id"])
    )

    compiled = deepcopy(result)
    compiled["gates"] = [rows[g["id"]] for g in catalog["gates"]]
    compiled["named_claims"] = claim_results
    compiled.setdefault("summary", {})
    compiled["summary"].update(
        {
            "no_aggregate_score": True,
            "counts": counts,
            "root_blockers": root_blockers,
            "remediation_cut_set": [
                {
                    "target_claim": c["claim"],
                    "required_roots": sorted(
                        set(c["unresolved_required_gates"] + c["failed_required_gates"])
                    ),
                    "status_before_remediation": c["status"],
                    "note": "Potential remediation set only; all roots must still be re-adjudicated after change.",
                }
                for c in claim_results
                if c["unresolved_required_gates"] or c["failed_required_gates"]
            ],
            "stage_b_handoff_queue": [
                {
                    "gate_id": x["gate_id"],
                    "handoff": x["stage_b_handoff"],
                    "note": "Architecture realization request only; no Stage A credit.",
                }
                for x in root_blockers
                if x.get("stage_b_handoff")
            ],
        }
    )
    return compiled


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("catalog")
    ap.add_argument("result")
    ap.add_argument("--output")
    args = ap.parse_args()

    try:
        catalog = load_json(args.catalog)
        result = load_json(args.result)
        compiled = compile_result(catalog, result)
    except (OSError, json.JSONDecodeError, ContractError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    payload = json.dumps(compiled, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        Path(args.output).write_text(payload, encoding="utf-8")
    else:
        sys.stdout.write(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
