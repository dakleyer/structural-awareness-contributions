"""G-03: bounded resource/service planner for source-declared candidate technologies.

Computes service and resource requirements from explicit candidate capacities,
marginal resource coefficients, startup inputs and named eligibility assumptions.
It NEVER establishes that any technology or rights exist in a real economy.
Unknown eligibility cannot be promoted into a certified feasible optimum.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import isfinite
from typing import Any


def q(raw: Any) -> Fraction:
    if type(raw) is bool or raw is None:
        raise ValueError("amount cannot be boolean or unknown")
    try:
        if type(raw) is float:
            if not isfinite(raw):
                raise ValueError("nonfinite")
            value = Fraction(str(raw))
        elif isinstance(raw, (int, Fraction, str)):
            value = Fraction(raw)
        else:
            raise ValueError("unsupported number")
    except (ValueError, ZeroDivisionError, TypeError, OverflowError) as exc:
        raise ValueError("invalid finite rational") from exc
    if value < 0:
        raise ValueError("negative material magnitude")
    return value


def _modes(modes: list[dict]) -> dict[str, dict]:
    if len(modes) > 12:
        raise ValueError("bounded research solver permits <=12 candidate modes")
    out = {}
    for row in modes:
        name = row["id"]
        if not isinstance(name, str) or not name or name in out:
            raise ValueError("duplicate/invalid technology identity")
        if row["eligibility"] not in ("PASS", "FAIL", "UNKNOWN"):
            raise ValueError("invalid rights/access admissibility")
        out[name] = {
            "id": name,
            "capacity": q(row["capacity"]),
            "rate": q(row["resource_per_service"]),
            "setup": q(row.get("fixed_resource", 0)),
            "eligibility": row["eligibility"],
        }
    return out


def _current_cost(target: Fraction, by_id: dict[str, dict], allocation: dict) -> Fraction:
    if not isinstance(allocation, dict) or not allocation:
        raise ValueError("current operation must have an allocation")
    total = Fraction(0)
    cost = Fraction(0)
    for name, raw in allocation.items():
        if name not in by_id:
            raise ValueError("current operation uses undeclared technology")
        mode = by_id[name]
        amount = q(raw)
        if mode["eligibility"] != "PASS":
            raise ValueError("current operation is not declared legitimate")
        if amount > mode["capacity"]:
            raise ValueError("current service exceeds declared capacity")
        total += amount
        if amount:
            cost += mode["setup"] + mode["rate"] * amount
    if total != target:
        raise ValueError("current service does not meet the exact question")
    return cost


def _subset_allocation(target: Fraction, active: tuple[dict, ...]):
    remaining = target
    assigned = {}
    cost = Fraction(0)
    for m in sorted(active, key=lambda item: (item["rate"], item["id"])):
        amount = min(remaining, m["capacity"])
        if amount:
            assigned[m["id"]] = amount
            cost += amount * m["rate"] + m["setup"]
        remaining -= amount
        if not remaining:
            break
    return None if remaining else (cost, assigned)


def optimize(target: Any, modes: list[dict], current: dict) -> dict:
    """Enumerate bounded combinations; not a global economic feasibility oracle."""
    service = q(target)
    by_id = _modes(modes)
    current_resources = _current_cost(service, by_id, current)
    available = [m for m in by_id.values() if m["eligibility"] == "PASS"]
    unresolved = sorted(name for name,m in by_id.items() if m["eligibility"] == "UNKNOWN")
    candidates = []
    # Enumerating subsets handles nonzero setup costs; marginal allocation
    # within any activated subset is ordered by resource-per-service coefficient.
    for k in range(1, len(available) + 1):
        for subset in combinations(available, k):
            result = _subset_allocation(service, subset)
            if result is not None:
                candidates.append(result)
    if not candidates:
        raise AssertionError("declared current plan must itself be available")
    best_cost = min(cost for cost, _ in candidates)
    optimizers = sorted(
        ({name: str(value) for name,value in sorted(allocation.items())}
         for cost, allocation in candidates if cost == best_cost),
        key=lambda row: repr(sorted(row.items())),
    )
    return {
        "service": str(service),
        "current_resources": str(current_resources),
        "minimum_resources_among_DECLARED_PASS_modes": str(best_cost),
        "gap_relative_to_declared_current": str(current_resources - best_cost),
        "optimizers_with_ties": optimizers,
        "unknown_eligibility_modes": unresolved,
        "coverage": "OPEN_WITH_UNRESOLVED_OPTIONS" if unresolved else
                    "FINITE_DECLARED_MODES_ONLY",
        "source_assumptions_are_not_external_feasibility_proof": True,
    }


def original_iq03_periods() -> tuple[dict, dict]:
    """Source toy numbers, now produced from service and candidate cost laws.

    Values and ratios are stated scenario assumptions, NOT field-calibrated.
    Rights and quality comparability are assumed inside each finite toy period.
    """
    t0 = optimize(100, [
        {"id":"incumbent","capacity":100,"resource_per_service":1,
         "eligibility":"PASS"},
        {"id":"alternative","capacity":100,"resource_per_service":"4/5",
         "eligibility":"PASS"},
    ], {"incumbent":100})
    t1 = optimize(140, [
        {"id":"incumbent","capacity":140,"resource_per_service":"11/14",
         "eligibility":"PASS"},
        {"id":"alternative","capacity":140,"resource_per_service":"13/28",
         "eligibility":"PASS"},
    ], {"incumbent":140})
    return t0, t1
