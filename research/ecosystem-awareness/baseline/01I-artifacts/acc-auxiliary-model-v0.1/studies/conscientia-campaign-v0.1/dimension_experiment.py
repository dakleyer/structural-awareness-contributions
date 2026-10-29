"""Finite, source-anchored experiment runner for the original ACC social examples.

This is an experimental harness, not a new A/B/C/D theory or an agent policy.
Material simulation, consent/authority and participant evaluations stay distinct.
Missing evidence never becomes zero, false, admissible, or a fabricated optimum.
Third parties register a model-owned operator without changing the harness.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import isfinite, log2
from typing import Any, Callable, Mapping, Sequence
import json


class ExperimentError(ValueError):
    pass


def number(value: Any) -> Fraction:
    if type(value) is bool:
        raise ExperimentError("boolean is not a quantity")
    if isinstance(value, Fraction):
        return value
    if isinstance(value, Decimal):
        if not value.is_finite():
            raise ExperimentError("nonfinite quantity")
        return Fraction(value)
    if type(value) is int:
        return Fraction(value)
    if type(value) is float:
        if not isfinite(value):
            raise ExperimentError("nonfinite quantity")
        return Fraction(str(value))
    if isinstance(value, str) and value.strip() and value != "UNKNOWN":
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError):
            pass
    raise ExperimentError("quantity must be finite, exact and declared")


def count(value: Any) -> int:
    amount = number(value)
    if amount < 0 or amount.denominator != 1:
        raise ExperimentError("count must be a nonnegative integer")
    return int(amount)


def shown(value: Fraction | int | None) -> int | str | None:
    if value is None:
        return None
    q = number(value)
    return int(q) if q.denominator == 1 else str(q)


def identity(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ExperimentError("missing " + label)
    return value


def gate(value: Any) -> str:
    if value is True:
        return "SATISFIED"
    if value is False:
        return "FAILED"
    if value == "UNKNOWN" and type(value) is str:
        return "UNKNOWN"
    raise ExperimentError("gate must be true, false or UNKNOWN")


@dataclass(frozen=True)
class PhysicalOutcome:
    status: str
    observations: Mapping[str, Any]
    issues: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.status not in ("POSSIBLE", "IMPOSSIBLE", "UNDETERMINED"):
            raise ExperimentError("invalid material status")
        if not isinstance(self.observations, Mapping):
            raise ExperimentError("physical observations must be a mapping")


def _flow(inputs: Mapping[str, Any]) -> PhysicalOutcome:
    """Conserve one material stock; compute deliveries and unrecovered remainder."""
    resource = identity(inputs["resource"], "resource")
    supply_raw = inputs.get("available", "UNKNOWN")
    if supply_raw == "UNKNOWN":
        return PhysicalOutcome("UNDETERMINED",
                               {"resource": resource, "available": None,
                                "unresolved": ["available"]})
    available = count(supply_raw)
    allocations: dict[str, int] = {}
    for row in inputs.get("allocations", []):
        actor = identity(row["actor"], "recipient")
        amount = count(row["amount"])
        allocations[actor] = allocations.get(actor, 0) + amount
    allocated = sum(allocations.values())
    shortfall = max(0, allocated - available)
    if shortfall:
        return PhysicalOutcome("IMPOSSIBLE",
                               {"resource": resource, "available": available,
                                "requested": allocated, "shortfall": shortfall},
                               ("RESOURCE_NOT_CREATED_BY_ALLOCATION",))
    remainder = available - allocated
    mode = inputs.get("remainder", "retained")
    if mode not in ("wasted", "retained"):
        raise ExperimentError("remainder must be wasted or retained")
    wasted, retained = (remainder, 0) if mode == "wasted" else (0, remainder)
    observations: dict[str, Any] = {
        "resource": resource, "available": available, "received": allocations,
        "allocated": allocated, "wasted": wasted, "retained": retained,
        "conserved": allocated + wasted + retained == available,
    }
    profile = inputs.get("declared_valuation", {})
    # This is a scenario's explicit B and F rule, not a human pain measurement.
    for actor, spec in profile.items():
        identity(actor, "actor")
        per_received = number(spec.get("benefit_per_received", 0))
        per_wasted = number(spec.get("frustration_per_wasted", 0))
        per_donated = number(spec.get("benefit_per_donated", 0))
        benefit = (per_received * allocations.get(actor, 0) +
                   per_donated * (allocated - allocations.get(actor, 0)))
        frustration = per_wasted * wasted
        observations.setdefault("hypothetical_welfare", {})[actor] = {
            "B": shown(benefit), "F": shown(frustration),
            "W": shown(benefit - frustration),
        }
    if "distance_km_per_delivered_unit" in inputs:
        km = number(inputs["distance_km_per_delivered_unit"])
        if km < 0:
            raise ExperimentError("distance must be nonnegative")
        observations["item_km"] = shown(km * allocated)
        observations["distance_unit"] = "item_km_NOT_CARBON_OR_MONEY"
    return PhysicalOutcome("POSSIBLE", observations)


def _capacity(inputs: Mapping[str, Any]) -> PhysicalOutcome:
    available = count(inputs["capacity"])
    requested = [count(x) for x in inputs["requests"]]
    total = sum(requested)
    return PhysicalOutcome("POSSIBLE" if total <= available else "IMPOSSIBLE", {
        "capacity": available, "requests": requested, "total_requested": total,
        "slack": max(0, available - total), "shortfall": max(0, total - available),
    })


def _choice(inputs: Mapping[str, Any]) -> PhysicalOutcome:
    values = [number(x) for x in inputs["utilities"]]
    start = count(inputs["start"])
    if not values or start >= len(values):
        raise ExperimentError("invalid finite choice")
    # Source's local, one-step improving decision is not its global oracle.
    at = start
    while True:
        neighbors = [i for i in (at - 1, at + 1) if 0 <= i < len(values)]
        improving = [i for i in neighbors if values[i] > values[at]]
        if not improving:
            break
        at = max(improving, key=lambda i: (values[i], -i))
    global_best = max(range(len(values)), key=lambda i: (values[i], -i))
    return PhysicalOutcome("POSSIBLE", {
        "utilities": [shown(x) for x in values],
        "local_choice": at, "local_utility": shown(values[at]),
        "global_best": global_best, "global_utility": shown(values[global_best]),
        "gain_if_transition_accessible": shown(values[global_best] - values[at]),
        "global_not_automatically_accessible": True,
    })


def _efficiency(inputs: Mapping[str, Any]) -> PhysicalOutcome:
    periods = inputs["periods"]
    if not isinstance(periods, list) or len(periods) < 1:
        raise ExperimentError("efficiency requires periods")
    results: list[dict[str, Any]] = []
    for p in periods:
        current = p["current"]
        alternative = p["alternative"]
        curr_service = number(current["service"])
        alt_service = number(alternative["service"])
        curr_resource = number(current["resource"])
        alt_resource = number(alternative["resource"])
        equal = curr_service == alt_service
        # A smaller input is an efficiency opportunity ONLY for comparable service.
        results.append({
            "current_service": shown(curr_service),
            "alternative_service": shown(alt_service),
            "current_resource": shown(curr_resource),
            "alternative_resource": shown(alt_resource),
            "service_equal": equal,
            "resource_gap": shown(curr_resource-alt_resource) if equal else None,
        })
    return PhysicalOutcome("POSSIBLE", {
        "periods": results,
        "current_service_increased": (
            number(periods[-1]["current"]["service"]) >
            number(periods[0]["current"]["service"])),
        "efficiency_gap_increased": (
            len(results) >= 2 and
            results[0]["resource_gap"] is not None and
            results[-1]["resource_gap"] is not None and
            number(results[-1]["resource_gap"]) > number(results[0]["resource_gap"])),
    })


def _shares(inputs: Mapping[str, Any]) -> PhysicalOutcome:
    totals = {identity(k, "resource"): count(v)
              for k, v in inputs["totals"].items()}
    allocations: dict[str, dict[str, int]] = {}
    for actor, amounts in inputs["allocations"].items():
        identity(actor, "actor")
        allocations[actor] = {k: count(v) for k, v in amounts.items()}
        if set(allocations[actor]) != set(totals):
            raise ExperimentError("every actor share needs each declared resource")
    assigned = {r: sum(row[r] for row in allocations.values()) for r in totals}
    excess = {r: assigned[r]-total for r,total in totals.items() if assigned[r]>total}
    ratios: dict[str, dict[str, str | None]] = {}
    for actor, row in allocations.items():
        ratios[actor] = {
            r: str(Fraction(row[r], totals[r])) if totals[r] else None
            for r in totals
        }
    return PhysicalOutcome("IMPOSSIBLE" if excess else "POSSIBLE", {
        "totals": totals, "allocated": allocations,
        "unallocated": {r: totals[r]-assigned[r] for r in totals if r not in excess},
        "excess": excess, "relative_shares": ratios,
        "each_actor_positive_absolute_gain": all(any(q>0 for q in row.values())
                                                    for row in allocations.values()),
    })


def _transport(inputs: Mapping[str, Any]) -> PhysicalOutcome:
    amount = count(inputs["units"])
    before_km = number(inputs["distance_before_km"])
    after_km = number(inputs["distance_after_km"])
    if before_km < 0 or after_km < 0:
        raise ExperimentError("invalid distance")
    return PhysicalOutcome("POSSIBLE", {
        "units": amount, "distance_before_km": shown(before_km),
        "distance_after_km": shown(after_km),
        "item_km_before": shown(amount*before_km),
        "item_km_after": shown(amount*after_km),
        "avoided_item_km": shown(amount*(before_km-after_km)),
        "money_savings": None, "carbon_savings": None,
    })


def _capability(inputs: Mapping[str, Any]) -> PhysicalOutcome:
    if any(inputs.get(k, "UNKNOWN") == "UNKNOWN"
           for k in ("mentors", "apprentices", "practice_possible")):
        return PhysicalOutcome("UNDETERMINED", {
            "effective_transmission_capacity": None,
            "incomplete_conditions": [
                k for k in ("mentors","apprentices","practice_possible")
                if inputs.get(k,"UNKNOWN") == "UNKNOWN"],
            "artifacts_available": inputs.get("artifacts", "UNKNOWN"),
        })
    mentors = count(inputs["mentors"])
    apprentices = count(inputs["apprentices"])
    permitted = gate(inputs["practice_possible"])
    capacity = min(mentors,apprentices) if permitted == "SATISFIED" else 0
    return PhysicalOutcome("POSSIBLE", {
        "effective_transmission_capacity": capacity,
        "artifacts_available": inputs.get("artifacts", "UNKNOWN"),
        "practice_possible": permitted,
    })


def _gate_only(inputs: Mapping[str, Any]) -> PhysicalOutcome:
    # A gate-only case executes its admission logic; it cannot invent output.
    return PhysicalOutcome("UNDETERMINED", {
        "stated_inputs": inputs, "measured_utility": None,
        "measured_harm": None, "feasible_output": None,
    })


def _provenance(inputs: Mapping[str, Any]) -> PhysicalOutcome:
    sources = [identity(x, "source") for x in inputs["source_ids"]]
    return PhysicalOutcome("POSSIBLE", {
        "messages": len(sources), "origins": len(set(sources)),
        "source_multiplicity": dict(sorted(Counter(sources).items())),
        "independent_truth_corrob": None,
    })


def _finite_rows(inputs: Mapping[str, Any]) -> list[dict[str, Any]]:
    rows = [dict(x) for x in inputs["worlds"]]
    if not rows:
        raise ExperimentError("finite worlds cannot be empty")
    derived = inputs.get("derived", {})
    for key, rule in derived.items():
        if rule["operator"] != "xor" or len(rule["fields"]) != 2:
            raise ExperimentError("unsupported finite computed column")
        a,b = rule["fields"]
        for row in rows:
            if row[a] not in (0,1) or row[b] not in (0,1):
                raise ExperimentError("xor operands must be bits")
            row[key] = row[a] ^ row[b]
    for row in rows:
        if any(type(v) not in (int,str) for v in row.values()):
            raise ExperimentError("finite states must use discrete keys")
    return rows


def conditional_entropy(rows: Sequence[Mapping[str, Any]], target: str,
                        given: Sequence[str] = ()) -> float:
    """H(target | given) on a declared uniform FINITE table; no open C/D model."""
    if not rows:
        raise ExperimentError("empty finite world table")
    groups: dict[tuple[Any,...], Counter[Any]] = defaultdict(Counter)
    for row in rows:
        key = tuple(row[x] for x in given)
        groups[key][row[target]] += 1
    h = 0.0
    n = len(rows)
    for counts in groups.values():
        m = sum(counts.values())
        h += m/n * -sum((c/m)*log2(c/m) for c in counts.values())
    return h


def conditional_information(rows: Sequence[Mapping[str, Any]], target: str,
                            source: Sequence[str], given: Sequence[str] = ()) -> float:
    return conditional_entropy(rows,target,given) - conditional_entropy(
        rows,target,tuple(given)+tuple(source))


def _observed_value(metrics: Mapping[str, Any], path: Sequence[Any]) -> Any:
    if not isinstance(path, list) or not path:
        raise ExperimentError("observation path must be nonempty")
    value: Any = metrics
    for key in path:
        if isinstance(value, Mapping) and key in value:
            value = value[key]
        elif (isinstance(value, list) and type(key) is int and
              0 <= key < len(value)):
            value = value[key]
        else:
            return None
    return None if value == "UNKNOWN" else value


def _test_observation(rule: Mapping[str, Any], metrics: Mapping[str, Any]) -> str:
    """Bind a gate to a COMPUTED effect, not a prewritten desired verdict."""
    value = _observed_value(metrics, rule["path"])
    if value is None:
        return "UNKNOWN"
    op = rule["op"]
    if op == "eq":
        expected = rule["value"]
        # Boolean truth and numeric one are different measurement contracts.
        if type(value) is bool or type(expected) is bool:
            ok = type(value) is type(expected) and value == expected
        else:
            ok = value == expected
        return "SATISFIED" if ok else "FAILED"
    if op in ("gte", "lte", "gt", "lt"):
        a, b = number(value), number(rule["value"])
        ok = {"gte": a >= b, "lte": a <= b,
              "gt": a > b, "lt": a < b}[op]
        return "SATISFIED" if ok else "FAILED"
    raise ExperimentError("unsupported observed-constraint comparator")


def _information(inputs: Mapping[str, Any]) -> PhysicalOutcome:
    rows = _finite_rows(inputs)
    results: dict[str,float] = {}
    for q in inputs["queries"]:
        name = identity(q["name"], "information query")
        if name in results:
            raise ExperimentError("duplicate information query")
        op = q["measure"]
        if op == "entropy":
            results[name] = conditional_entropy(rows,q["target"],q.get("given",[]))
        elif op == "information":
            results[name] = conditional_information(
                rows,q["target"],q["source"],q.get("given",[]))
        else:
            raise ExperimentError("unsupported finite information measure")
    return PhysicalOutcome("POSSIBLE", {
        "finite_world_count": len(rows),
        "computed_rows": rows,
        "computed_information_bits": results,
        "open_CD_distribution": None,
    })


DEFAULT_OPERATORS: dict[str,Callable[[Mapping[str,Any]], PhysicalOutcome]] = {
    "material_flow": _flow, "capacity": _capacity,
    "finite_choice": _choice, "period_efficiency": _efficiency,
    "joint_shares": _shares, "transport": _transport,
    "capability": _capability, "gate_only": _gate_only,
    "provenance": _provenance, "finite_information": _information,
}


def public_view(case: Mapping[str, Any]) -> dict[str, Any]:
    """Public decision packet. Scenario's physical params are NEVER included."""
    return {
        "case_id": case["case_id"], "question": case["question"],
        "horizon": case["horizon"], "public": dict(case.get("public", {})),
        "declared_dimensions": [d["id"] for d in case["dimensions"]],
    }


def run_case(case: Mapping[str, Any], *,
             operators: Mapping[str,Callable[[Mapping[str,Any]],PhysicalOutcome]] | None = None) -> dict[str, Any]:
    for field in ("case_id", "family", "question", "horizon", "operator", "model"):
        identity(case[field], field)
    sources = case["source_refs"]
    if not isinstance(sources,list) or not sources:
        raise ExperimentError("source paragraph IDs required")
    for source in sources:
        identity(source,"source paragraph")
    if case["evidence_tier"] != "SOURCE_ANCHORED_SYNTHETIC":
        raise ExperimentError("cannot promote source statements to observations")
    dimensions = case["dimensions"]
    if not isinstance(dimensions,list) or not dimensions:
        raise ExperimentError("declare evaluated or latent dimensions")
    seen: set[str] = set()
    dim_states: dict[str,dict[str,Any]] = {}
    for d in dimensions:
        name=identity(d["id"],"dimension")
        if name in seen:
            raise ExperimentError("duplicate dimension")
        seen.add(name)
        if d["initial"] not in ("ACTIVE","IMPLICIT","OPEN"):
            raise ExperimentError("invalid dimension initial state")
        dim_states[name] = {"initial":d["initial"],"at_decision":d["initial"],
                            "unit":identity(d["unit"],"dimension unit")}
    handlers = dict(DEFAULT_OPERATORS)
    if operators:
        for key, handler in operators.items():
            identity(key,"operator")
            if key in DEFAULT_OPERATORS:
                raise ExperimentError("native operators cannot be replaced")
            handlers[key]=handler
    if case["operator"] not in handlers:
        raise ExperimentError("unregistered model operator")
    outcome=handlers[case["operator"]](case["inputs"])
    if not isinstance(outcome,PhysicalOutcome):
        raise ExperimentError("operator must return PhysicalOutcome")
    for event in case.get("activation_events",[]):
        key=event["dimension"]
        if key not in dim_states:
            raise ExperimentError("activation references undeclared dimension")
        if ("occurs" in event) == ("test" in event):
            raise ExperimentError("activation requires exactly one event predicate")
        flag=(gate(event["occurs"]) if "occurs" in event else
              _test_observation(event["test"],outcome.observations))
        if flag=="SATISFIED":
            dim_states[key]["at_decision"]="ACTIVE"
        elif flag=="UNKNOWN":
            dim_states[key]["at_decision"]="UNRESOLVED"
    checks: list[dict[str,Any]]=[]
    seen_conditions:set[str]=set()
    for condition in case.get("constraints",[]):
        key=identity(condition["id"],"constraint")
        if key in seen_conditions:
            raise ExperimentError("duplicate constraint")
        seen_conditions.add(key)
        category=condition["category"]
        if category not in ("material","coordination","safety","consent",
                            "rights","authority","attribution","evidence"):
            raise ExperimentError("unknown constraint category")
        if ("satisfied" in condition) == ("test" in condition):
            raise ExperimentError("constraint requires exactly one evidence or computed test")
        status=(gate(condition["satisfied"]) if "satisfied" in condition else
                _test_observation(condition["test"],outcome.observations))
        checks.append({"id":key,"category":category,"status":status,
                       "owner":identity(condition["owner"],"constraint owner")})
    material_failed = (outcome.status=="IMPOSSIBLE" or
                       any(c["status"]=="FAILED" and c["category"]=="material"
                           for c in checks))
    other_failed = any(c["status"]=="FAILED" and c["category"]!="material"
                       for c in checks)
    unresolved = (outcome.status=="UNDETERMINED" or
                  any(c["status"]=="UNKNOWN" for c in checks))
    if material_failed:
        admission="MATERIALLY_INFEASIBLE"
    elif other_failed:
        admission="BLOCKED_BY_CONDITION"
    elif unresolved:
        admission="UNDETERMINED"
    else:
        admission="ELIGIBLE_UNDER_DECLARED_CONDITIONS"
    physical_status=outcome.status
    public=public_view(case)
    encoded=json.dumps(case,ensure_ascii=False,sort_keys=True,separators=(",",":"))
    return {
        "case_id":case["case_id"],"family":case["family"],"model":case["model"],
        "question":case["question"],"horizon":case["horizon"],
        "source_refs":list(sources),"evidence_tier":case["evidence_tier"],
        "case_sha256":sha256(encoded.encode("utf-8")).hexdigest(),
        "public_view":public,"physical_status":physical_status,
        "physical_outcome":dict(outcome.observations),
        "physical_issues":list(outcome.issues),
        "constraints":checks,"admission":admission,
        "unresolved_conditions":[c["id"] for c in checks if c["status"]=="UNKNOWN"],
        "blocking_conditions":[c["id"] for c in checks if c["status"]=="FAILED"],
        "dimension_states":dim_states,
        "is_empirical_observation":False,
    }


def run_manifest(manifest: Mapping[str,Any], *,
                 operators: Mapping[str,Callable[[Mapping[str,Any]],PhysicalOutcome]] | None = None) -> dict[str,Any]:
    if manifest.get("schema")!="ACC-ORIGINAL-EXPERIMENTS-0.1":
        raise ExperimentError("unknown manifest schema")
    cases=manifest["cases"]
    if not isinstance(cases,list) or not cases:
        raise ExperimentError("empty manifest")
    results=[]
    seen=set()
    for case in cases:
        cid=case["case_id"]
        if cid in seen:
            raise ExperimentError("duplicate case ID")
        seen.add(cid)
        results.append(run_case(case,operators=operators))
    by_model: dict[str,Counter[str]] = defaultdict(Counter)
    for result in results:
        by_model[result["model"]][result["admission"]]+=1
    return {
        "schema":manifest["schema"],"cases":results,"case_count":len(results),
        "admission_by_model":{k:dict(sorted(v.items())) for k,v in sorted(by_model.items())},
        "cross_model_objectives_aggregated":False,
    }
