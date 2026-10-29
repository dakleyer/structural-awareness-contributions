"""ACC narrative acceptance laboratory, v0.1 (finite, source-anchored, synthetic).

No social generalisation, human observation, ABCD epistemic categorisation,
agentic authority, or field technology certification is performed here.
A dimension is an evaluation criterion; a guard is an actual transition condition.
"""
from __future__ import annotations

from collections import deque
from decimal import Decimal
from fractions import Fraction
from itertools import product
import argparse
import json
from pathlib import Path
from typing import Any

PASS, FAIL, UNKNOWN = "PASS", "FAIL", "UNKNOWN"
STATUSES = frozenset((PASS, FAIL, UNKNOWN))


def number(value: Any) -> Fraction:
    """Exact source-facing number. Missing evidence is None, never zero."""
    if type(value) is bool or value is None:
        raise ValueError("missing/boolean cannot stand for a measured number")
    if isinstance(value, Fraction):
        return value
    if isinstance(value, Decimal):
        if not value.is_finite():
            raise ValueError("non-finite number")
        return Fraction(value)
    if type(value) in (int, float):
        if type(value) is float and not __import__('math').isfinite(value):
            raise ValueError("non-finite number")
        return Fraction(str(value))
    if isinstance(value, str) and value.strip():
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise ValueError("invalid rational") from exc
    raise ValueError("not a valid number")


def _value(mapping: dict, key: str) -> Fraction | None:
    value = mapping.get(key)
    return None if value is None else number(value)


def combine(statuses: list[str]) -> str:
    if FAIL in statuses:
        return FAIL
    if UNKNOWN in statuses:
        return UNKNOWN
    return PASS


def compare_vector(left: dict, right: dict, directions: dict[str, str], axes: list[str]) -> dict:
    """Independent oriented coordinates, NOT Pareto over unlisted human preferences."""
    deltas = {}
    for axis in axes:
        before, after = _value(left, axis), _value(right, axis)
        if before is None or after is None:
            deltas[axis] = None
        else:
            d = after - before
            if directions[axis] == "min":
                d = -d
            deltas[axis] = d
    present = [v for v in deltas.values() if v is not None]
    if len(present) != len(axes):
        classification = "NOT_ESTABLISHED"
    elif any(v > 0 for v in present) and any(v < 0 for v in present):
        classification = "TRADEOFF"
    elif any(v < 0 for v in present):
        classification = "WORSE_OR_INCOMPARABLE"
    elif any(v > 0 for v in present):
        classification = "DOMINATES_ON_DECLARED_AXES"
    else:
        classification = "TIE_ON_DECLARED_AXES"
    return {"status": classification,
            "oriented_deltas": {k: None if v is None else str(v) for k, v in deltas.items()}}


def state_checks(scenario: dict, state: dict) -> dict:
    facts = state.get("facts", {})
    issues=[]
    statuses=[]
    for rule in scenario.get("state_invariants", []):
        kind = rule["kind"]
        if kind in ("sum_equals", "sum_at_most"):
            values = [_value(facts, key) for key in rule["fields"]]
            target = _value(facts, rule["target_field"]) if "target_field" in rule else number(rule["limit"])
            status = UNKNOWN if target is None or any(v is None for v in values) else (
                PASS if sum(values) == target else FAIL) if kind == "sum_equals" else (
                PASS if sum(values) <= target else FAIL)
        elif kind == "equal_fields":
            v1,v2=_value(facts,rule["fields"][0]),_value(facts,rule["fields"][1])
            status=UNKNOWN if v1 is None or v2 is None else PASS if v1 == v2 else FAIL
        elif kind == "nonnegative":
            values=[_value(facts, x) for x in rule["fields"]]
            status=UNKNOWN if any(v is None for v in values) else PASS if all(v >= 0 for v in values) else FAIL
        elif kind == "welfare_identity":
            b,f,w=(_value(state.get("welfare",{}),x) for x in ("B","F","W"))
            status=UNKNOWN if None in (b,f,w) else PASS if b-f==w else FAIL
        else:
            raise ValueError("unsupported state invariant: "+str(kind))
        if rule.get("enforcement", "PHYSICAL") == "PHYSICAL":
            statuses.append(status)
        if status != PASS:
            issues.append({"rule": rule.get("id", kind), "status":status,
                           "enforcement":rule.get("enforcement", "PHYSICAL")})
    return {"status": combine(statuses), "issues": issues}


def transition_checks(scenario: dict, edge: dict, validity: dict[str, dict],
                      balances: dict[str, Fraction] | None = None) -> dict:
    """Material constraints and legitimacy are different questions."""
    pools={name:number(val) for name,val in scenario.get("resource_budgets",{}).items()}
    if balances is None:
        balances=pools
    consumption={k:number(v) for k,v in edge.get("consumes",{}).items()}
    if any(v < 0 for v in consumption.values()):
        raise ValueError("negative resource consumption")
    if set(consumption)-set(pools):
        raise ValueError("undefined resource budget")
    material=[validity[edge["from"]]["status"],validity[edge["to"]]["status"]]
    for name,needed in consumption.items():
        material.append(PASS if needed<=balances[name] else FAIL)
    technical=combine(material)
    governance=[]
    for guard in edge.get("guards",[]):
        if guard["status"] not in STATUSES:
            raise ValueError("unknown guard status")
        if guard["category"] not in ("consent","authority","coordination","safety","evidence","recognition","continuity"):
            raise ValueError("unknown guard category")
        governance.append(guard["status"])
    # Endogenous agreement: positive total is not enough if actor loses.
    if edge.get("actor_nondecrease"):
        a=scenario["states"][edge["from"]].get("payoffs",{})
        b=scenario["states"][edge["to"]].get("payoffs",{})
        ids=set(a)|set(b)
        vals=[(_value(a,k),_value(b,k)) for k in ids]
        governance.append(UNKNOWN if any(x is None or y is None for x,y in vals)
                          else PASS if all(y>=x for x,y in vals) else FAIL)
    institutional=combine(governance)
    return {"technical":technical,"institutional":institutional,
            "admissible":combine([technical,institutional]),
            "resource_use":{k:str(v) for k,v in consumption.items()},
            "unresolved": [g["id"] for g in edge.get("guards",[]) if g["status"]==UNKNOWN],
            "failed": [g["id"] for g in edge.get("guards",[]) if g["status"]==FAIL]}


def reachable(scenario: dict, validity: dict[str, dict], protocol: str) -> dict:
    """Breadth-first search on states AND remaining nonrenewable resource budgets."""
    if protocol not in ("unilateral_only","joint_allowed"):
        raise ValueError("unsupported transition protocol")
    budgets={k:number(v) for k,v in scenario.get("resource_budgets",{}).items()}
    keys=tuple(sorted(budgets))
    start=scenario["initial"]
    first=(start,tuple(budgets[k] for k in keys))
    q=deque([(first,[start])]); seen={first}; paths={start:[start]}
    while q:
        (position,remaining),path=q.popleft()
        available=dict(zip(keys,remaining))
        for edge in scenario["transitions"]:
            if edge["from"] != position or (protocol=="unilateral_only" and edge["mode"]=="joint"):
                continue
            report=transition_checks(scenario,edge,validity,available)
            if report["admissible"] != PASS:
                continue
            new_balances=tuple(available[k]-number(edge.get("consumes",{}).get(k,0)) for k in keys)
            key=(edge["to"],new_balances)
            if key in seen:
                continue
            seen.add(key)
            next_path=path+[edge["to"]]
            paths.setdefault(edge["to"],next_path)
            q.append((key,next_path))
    return {"protocol":protocol,"reachable_states":sorted(paths),"paths":paths}


def validate(scenario: dict) -> None:
    if scenario.get("evidence_tier") != "AUTHOR_HYPOTHETICAL_TOY":
        raise ValueError("source example must preserve its synthetic evidence classification")
    if not scenario.get("source_anchor") or not scenario.get("case_id"):
        raise ValueError("untraceable source example")
    dims=scenario["dimensions"]
    if not dims or any(info.get("direction") not in ("min","max") or not info.get("unit") for info in dims.values()):
        raise ValueError("all finite evaluated axes need explicit unit and orientation")
    for stage in scenario["stages"]:
        if not stage["axes"] or len(stage["axes"]) != len(set(stage["axes"])) or set(stage["axes"])-set(dims):
            raise ValueError("undefined or duplicate stage dimensions")
    states=scenario["states"]
    if not states or scenario["initial"] not in states:
        raise ValueError("missing initial state")
    for name,state in states.items():
        if not isinstance(state.get("metrics",{}),dict):
            raise ValueError("invalid state metrics")
        if set(state["metrics"])-set(dims):
            raise ValueError("unknown dimension")
        for field in ("metrics","facts","payoffs","welfare"):
            for val in state.get(field,{}).values():
                if val is not None:
                    number(val)
    for value in scenario.get("resource_budgets",{}).values():
        if number(value)<0:raise ValueError("negative budget")
    ids=[]
    for e in scenario["transitions"]:
        if e["from"] not in states or e["to"] not in states or e["mode"] not in ("joint","unilateral"):
            raise ValueError("invalid transition")
        ids.append(e["id"])
        for g in e.get("guards",[]):
            if not g.get("id") or not g.get("source_of_status"):
                raise ValueError("every gate needs a named source of the declared test value")
    if len(ids)!=len(set(ids)):
        raise ValueError("duplicate transition ID")
    for c in scenario.get("comparisons",[]):
        if c["from"] not in states or c["to"] not in states:
            raise ValueError("unknown comparison endpoints")


def run_case(scenario: dict) -> dict:
    validate(scenario)
    validity={name:state_checks(scenario,s) for name,s in scenario["states"].items()}
    transitions={e["id"]:transition_checks(scenario,e,validity) for e in scenario["transitions"]}
    directions={k:d["direction"] for k,d in scenario["dimensions"].items()}
    comparisons=[]
    for pair in scenario.get("comparisons",[]):
        left,right=scenario["states"][pair["from"]],scenario["states"][pair["to"]]
        stages=[]
        previously_material=set()
        for stg in scenario["stages"]:
            axes=stg["axes"]
            stages.append({"stage":stg["id"],"axes":axes,
                           "newly_material_axes":sorted(set(axes)-previously_material),
                           "comparison":compare_vector(left["metrics"],right["metrics"],directions,axes)})
            previously_material=set(axes)
        actors=sorted(set(left.get("payoffs",{}))|set(right.get("payoffs",{})))
        pareto=compare_vector(left.get("payoffs",{}),right.get("payoffs",{}),{k:"max" for k in actors},actors) if actors else {"status":"NOT_REPRESENTED"}
        comparisons.append({"from":pair["from"],"to":pair["to"],"stages":stages,
                            "target_state_physically_admissible_in_declared_model":validity[pair["to"]]["status"],
                            "individual_payoffs":pareto})
    return {"case_id":scenario["case_id"],"evidence_tier":scenario["evidence_tier"],
            "source_anchor":scenario["source_anchor"],"interpretation":scenario.get("interpretation",""),
            "state_validity":validity,"transitions":transitions,"comparisons":comparisons,
            "reachability":{"unilateral_only":reachable(scenario,validity,"unilateral_only"),
                            "joint_allowed":reachable(scenario,validity,"joint_allowed")},
            "welfare":{name:{"B":s.get("welfare",{}).get("B"),"F":s.get("welfare",{}).get("F"),
                              "W":s.get("welfare",{}).get("W"),"status":"STIPULATED_TOY_NOT_HUMAN_MEASUREMENT"}
                       for name,s in scenario["states"].items() if "welfare" in s}}


def run_manifest(manifest: dict) -> dict:
    if manifest.get("schema") != "ACC-NARRATIVE-EXPERIMENTS-v0.1":
        raise ValueError("unknown manifest version")
    cases=manifest["cases"]
    ids=[c["case_id"] for c in cases]
    if len(set(ids))!=len(ids):raise ValueError("duplicate case")
    reports=[run_case(c) for c in cases]
    return {"schema":manifest["schema"],"case_count":len(reports),"cases":reports,
            "evidence":"SYNTHETIC_DECLARED_EXERCISES_NOT_FIELD_OBSERVATION",
            "limit":"No hidden empirical truth, global objective, permission grant or epistemic A/B/C/D inventory"}


def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--manifest",type=Path,default=Path(__file__).with_name("cases.json"))
    ap.add_argument("--output",type=Path,default=None)
    args=ap.parse_args(argv)
    output=run_manifest(json.loads(args.manifest.read_text(encoding="utf-8")))
    data=json.dumps(output,indent=2,ensure_ascii=False,sort_keys=True)+"\n"
    if args.output: args.output.write_text(data,encoding="utf-8")
    else: print(data,end="")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
