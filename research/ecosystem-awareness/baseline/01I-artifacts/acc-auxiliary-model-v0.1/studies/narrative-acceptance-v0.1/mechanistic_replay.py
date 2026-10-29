"""G-03: finite operation-first experiment runner for author-anchored ACC cases.

An operation changes declared physical facts. A post-hoc evaluator then computes
metrics and checks constraints; the admissibility decision never sees the
counterfactual result or obtains new authority from apparent improvements.
No epistemic C/D inventory, human welfare measurement, or global objective.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from fractions import Fraction
import json
from pathlib import Path
from typing import Any

from engine import (
    PASS, FAIL, UNKNOWN, number, combine, compare_vector,
    state_checks, transition_checks,
)

SCHEMA = "ACC-SOURCE-MECHANISMS-v0.1"


def _exact(mapping: dict[str, Any]) -> dict[str, Fraction]:
    if not isinstance(mapping, dict):
        raise ValueError("facts must be a mapping")
    return {str(k): number(v) for k, v in mapping.items()}


def _json_state(state: dict[str, Fraction]) -> dict[str, str]:
    return {key: str(value) for key, value in sorted(state.items())}


def evaluate(formula: dict, facts: dict[str, Fraction]) -> Fraction | None:
    """Restricted, no-eval finite measurement DSL; absent evidence stays None."""
    if not isinstance(formula, dict):
        raise ValueError("metric formula must be an object")
    op = formula.get("op")
    if op == "unknown":
        return None
    if op == "field":
        return facts.get(formula["field"])
    if op == "affine":
        value = facts.get(formula["field"])
        return None if value is None else (
            value * number(formula.get("scale", 1)) + number(formula.get("offset", 0)))
    if op in ("sum", "ratio"):
        fields = formula["fields"]
        if not isinstance(fields, list) or not fields:
            raise ValueError("measurement requires fields")
        if any(name not in facts for name in fields):
            return None
        value = sum((facts[name] for name in fields), Fraction(0))
        if op == "sum":
            return value
        denominators = formula["denominator_fields"]
        if not isinstance(denominators, list) or not denominators:
            raise ValueError("ratio requires denominator fields")
        if any(name not in facts for name in denominators):
            return None
        denom = sum((facts[name] for name in denominators), Fraction(0))
        return None if denom == 0 else value / denom
    if op == "lookup":
        index = facts.get(formula["index"])
        if index is None or index.denominator != 1:
            return None
        table = formula["table"]
        idx = int(index)
        return number(table[idx]) if 0 <= idx < len(table) else None
    raise ValueError("unknown finite measurement operation: " + str(op))


def _measure(formulas: dict, facts: dict[str, Fraction]) -> dict[str, Fraction | None]:
    return {name: evaluate(spec, facts) for name, spec in formulas.items()}


def apply_operation(
    before: dict[str, Fraction], action: dict,
    derived_fields: dict[str, dict] | None = None,
) -> dict[str, Fraction]:
    """Calculate a candidate state: transfers, increments, setters, derived laws."""
    after = dict(before)
    for field, expected in action.get("requires", {}).items():
        if after.get(field) != number(expected):
            raise ValueError("action precondition not met: " + action["id"] + "/" + field)
    for transfer in action.get("transfers", []):
        from_field, to_field = transfer["from"], transfer["to"]
        if from_field == to_field or from_field not in after or to_field not in after:
            raise ValueError("invalid source/target of physical transfer")
        qty = number(transfer["amount"])
        if qty < 0:
            raise ValueError("negative transfer")
        if after[from_field] < qty:
            raise ValueError("source has insufficient conserved material")
        after[from_field] -= qty
        after[to_field] += qty
    for field, raw in action.get("delta", {}).items():
        if field not in after:
            raise ValueError("delta references unknown physical field " + field)
        after[field] += number(raw)
    for field, raw in action.get("set", {}).items():
        if field not in after:
            raise ValueError("setter references unknown physical field " + field)
        after[field] = number(raw)
    for field, expression in (derived_fields or {}).items():
        if field not in after:
            raise ValueError("derived destination not declared in initial facts")
        value = evaluate(expression, after)
        if value is None:
            raise ValueError("derived physical field lacks a calculable source")
        after[field] = value
    return after


def _state_valid(case: dict, facts: dict[str, Fraction]) -> dict:
    if any(value < 0 for key, value in facts.items()
           if key in case.get("nonnegative_fields", [])):
        return {"status": FAIL, "issues": [{"rule": "nonnegative_fields", "status": FAIL}]}
    return state_checks(
        {"state_invariants": case.get("invariants", [])},
        {"facts": facts},
    )


def _source_guarded_transition(
    case: dict, action: dict, before: dict, after: dict,
    remaining: dict[str, Fraction],
) -> dict:
    formulas = case.get("actor_payoffs", {})
    a = _measure(formulas, before)
    b = _measure(formulas, after)
    # The native ACC transition checker owns actor nondecrease, all guards
    # and resource debits. A missing actor value is UNKNOWN, never zero.
    compact = {
        "resource_budgets": case.get("resource_budgets", {}),
        "states": {"before": {"payoffs": a}, "after": {"payoffs": b}},
    }
    edge = {
        "id": action["id"], "from": "before", "to": "after",
        "guards": action.get("guards", []),
        "consumes": action.get("consumes", {}),
        "actor_nondecrease": action.get("actor_nondecrease", False),
    }
    return transition_checks(
        compact, edge,
        {"before": _state_valid(case, before), "after": _state_valid(case, after)},
        remaining,
    )


def _staged_comparisons(case: dict, start: dict, candidate: dict) -> list[dict]:
    formulas = case["dimensions"]
    pre = _measure({k: v["formula"] for k, v in formulas.items()}, start)
    post = _measure({k: v["formula"] for k, v in formulas.items()}, candidate)
    oriented = {k: v["direction"] for k, v in formulas.items()}
    out = []
    earlier: set[str] = set()
    for stage in case["stages"]:
        axes = stage["axes"]
        out.append({
            "stage": stage["id"], "axes": axes,
            "first_time_material": sorted(set(axes) - earlier),
            "comparison": compare_vector(pre, post, oriented, axes),
        })
        earlier.update(axes)
    return out


def run_case(case: dict) -> dict:
    if case.get("evidence_tier") != "AUTHOR_HYPOTHETICAL_TOY":
        raise ValueError("cannot promote a synthetic scenario to empirical evidence")
    if not case.get("case_id") or not case.get("source_anchor"):
        raise ValueError("missing case identity/source")
    dimensions = case.get("dimensions", {})
    if not dimensions or any(d.get("direction") not in ("min", "max")
                             or not d.get("unit") or not isinstance(d.get("formula"), dict)
                             for d in dimensions.values()):
        raise ValueError("invalid dimension definition")
    actions = case.get("actions", [])
    identities = [a["id"] for a in actions]
    if len(identities) != len(set(identities)):
        raise ValueError("duplicate operations")
    if len(actions) > 32:
        raise ValueError("bounded finite experiment permits at most 32 operations")
    by_id = {a["id"]: a for a in actions}
    for stage in case.get("stages", []):
        if not stage["axes"] or len(set(stage["axes"])) != len(stage["axes"]) or set(stage["axes"]) - set(dimensions):
            raise ValueError("stage requires distinct declared dimensions")
    initial = _exact(case["initial"])
    base_check = _state_valid(case, initial)
    if base_check["status"] != PASS:
        raise ValueError("initial physical state is not valid in the declared finite model")
    resources = _exact(case.get("resource_budgets", {}))
    if any(value < 0 for value in resources.values()):
        raise ValueError("negative scenario resources")
    reports = []
    paths = case.get("probes", [])
    for probe in paths:
        action_ids = probe["actions"]
        if not isinstance(action_ids, list) or len(action_ids) != len(set(action_ids)) or len(action_ids) > 32:
            raise ValueError("invalid finite operation sequence")
        if set(action_ids) - set(by_id):
            raise ValueError("probe contains undefined operation")
        hypothetical = dict(initial)
        committed = dict(initial)
        budget = dict(resources)
        status_path = []
        steps = []
        all_preceding_pass = True
        for name in action_ids:
            action = by_id[name]
            if action.get("mode", "unilateral") not in ("unilateral", "joint"):
                raise ValueError("unknown action mode")
            if any(type(g.get("source_of_status")) is not str or not g["source_of_status"]
                   for g in action.get("guards", [])):
                raise ValueError("every source gate needs provenance")
            before = dict(hypothetical)
            try:
                after = apply_operation(before, action, case.get("derived_fields"))
                checked = _source_guarded_transition(case, action, before, after, budget)
                label = checked["admissible"]
            except ValueError as exc:
                # A malformed or materially infeasible operation is a failed
                # candidate, never an automatically executable improvement.
                if "precondition" in str(exc) or "insufficient conserved" in str(exc):
                    after = before
                    checked = {"technical": FAIL, "institutional": UNKNOWN,
                               "admissible": FAIL, "resource_use": {},
                               "failed": ["PHYSICAL_PRECONDITION"], "unresolved": []}
                    label = FAIL
                else:
                    raise
            step = {
                "action": name, "mode": action.get("mode", "unilateral"),
                "before": _json_state(before), "candidate_after": _json_state(after),
                "technical": checked["technical"], "institutional": checked["institutional"],
                "admissible": label, "committed": False,
            }
            status_path.append(label)
            steps.append(step)
            if checked["technical"] == FAIL:
                break
            hypothetical = after  # Counterfactual continuation != authorization.
            for key, amount in checked["resource_use"].items():
                budget[key] -= number(amount)
            if all_preceding_pass and label == PASS:
                committed = dict(after)
                step["committed"] = True
            else:
                all_preceding_pass = False
        reports.append({
            "probe": probe["id"],
            "source_experiment": "FINITE_DECLARED_OPERATIONALIZATION",
            "admissibility": combine(status_path),
            "initial_facts": _json_state(initial),
            "candidate_facts": _json_state(hypothetical),
            "actually_committed_facts": _json_state(committed),
            "candidate_stages": _staged_comparisons(case, initial, hypothetical),
            "steps": steps,
            "conditional_counterfactual": combine(status_path) != PASS,
        })
    return {
        "case_id": case["case_id"],
        "source_anchor": case["source_anchor"],
        "evidence_tier": case["evidence_tier"],
        "initial_valid": base_check["status"],
        "probes": reports,
        "no_automatic_real_world_authority": True,
    }


def run_manifest(manifest: dict) -> dict:
    if manifest.get("schema") != SCHEMA:
        raise ValueError("unknown source operation manifest")
    ids = [case["case_id"] for case in manifest["cases"]]
    if len(set(ids)) != len(ids):
        raise ValueError("duplicate case")
    results = [run_case(case) for case in manifest["cases"]]
    return {
        "schema": SCHEMA, "case_count": len(results), "cases": results,
        "interpretation": "FINITE_SYNTHETIC_OPERATIONS_AND_CONDITIONAL_COUNTERFACTUALS_NOT_FIELD_EXECUTION",
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=Path(__file__).with_name("MECHANISM_CASES.json"))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    run = run_manifest(json.loads(args.manifest.read_text(encoding="utf-8")))
    data = json.dumps(run, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.write_text(data, encoding="utf-8")
    else:
        print(data, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
