"""Finite, source-limited ACC research examples of rational bottlenecks.

Pure Python standard library. This does NOT model, enumerate or measure the
uncharacterized B/C/D exterior and cannot infer welfare or observed HID.

A state may be Pareto-dominated in the joint feasible set while unreachable
by a sequence of *unilateral admissible* transitions. Relative output gaps
are conditional on a separately justified matched-resource counterfactual.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import product
import json
from typing import Iterable


@dataclass(frozen=True)
class Constraint:
    """Linear inequality sum(a_i*x_i) <= capacity over explicitly listed variables."""
    coefficients: tuple[float, ...]
    capacity: float

    def permits(self, state: tuple[int, ...], tolerance: float = 1e-10) -> bool:
        if len(self.coefficients) != len(state):
            raise ValueError("dimension mismatch")
        return sum(w * x for w, x in zip(self.coefficients, state)) <= self.capacity + tolerance


def feasible_states(n: int, constraints: Iterable[Constraint]) -> list[tuple[int, ...]]:
    """Enumerate an explicitly bounded *binary* study universe (not external W)."""
    if not isinstance(n, int) or not (1 <= n <= 14):
        raise ValueError("finite explicit dimensions in [1, 14] required")
    checks = tuple(constraints)
    if any(len(c.coefficients) != n for c in checks):
        raise ValueError("constraint width mismatch")
    return [x for x in product((0, 1), repeat=n) if all(c.permits(x) for c in checks)]


def dominates(reference: Iterable[float], candidate: Iterable[float], eps: float = 1e-10) -> bool:
    """True if candidate improves at least one coordinate and harms none."""
    current = tuple(reference)
    target = tuple(candidate)
    if not current or len(current) != len(target):
        raise ValueError("same nonempty coordinate vector required")
    return all(v + eps >= u for u, v in zip(current, target)) and any(
        v > u + eps for u, v in zip(current, target))


def reachable_by_unilateral_additions(
    start: tuple[int, ...], admissible_states: Iterable[tuple[int, ...]]
) -> set[tuple[int, ...]]:
    """States reachable by adding *one* project while remaining feasible."""
    admissible = set(admissible_states)
    if start not in admissible:
        raise ValueError("start is infeasible")
    if any(len(x) != len(start) for x in admissible):
        raise ValueError("inconsistent dimension count")
    visited = {start}
    queue = deque([start])
    while queue:
        current = queue.popleft()
        for i, value in enumerate(current):
            if value:
                continue
            next_state = current[:i] + (1,) + current[i+1:]
            if next_state in admissible and next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)
    return visited


def coupled_trap() -> dict:
    """Joint improvement exists; neither individually feasible first move exists.

    x1 <= x2, x2 <= x1; both linear, monotone in local utility.
    Requires a joint atomic transition mechanism, not another resource.
    """
    feasible = feasible_states(2, (
        Constraint((1, -1), 0), Constraint((-1, 1), 0)
    ))
    start = (0, 0)
    target = (1, 1)
    reached = reachable_by_unilateral_additions(start, feasible)
    current_utility = (4.0, 4.0)
    target_utility = (5.0, 5.0)
    return {
        "evidence": "SYNTHETIC_FINITE_LINEAR_BINARY",
        "feasible": [list(x) for x in feasible],
        "current": list(start),
        "joint_target": list(target),
        "pareto_dominates": dominates(current_utility, target_utility),
        "reachable_without_joint_transition": target in reached,
        "reachable_with_joint_transition": target in feasible,
        "transition_mechanism": "ATOMIC_JOINT_SWITCH_REQUIRED",
        "utility_current": list(current_utility),
        "utility_target": list(target_utility),
    }


def saturation_without_redesign() -> dict:
    """No reserve: activity consumes a fully utilized resource; infeasible."""
    states = feasible_states(1, (Constraint((2,), 0),))
    return {"feasible": [list(x) for x in states],
            "project_feasible": (1,) in states,
            "source": "SYNTHETIC_RESOURCE_SATURATION"}


def saturation_with_redesign() -> dict:
    """Existing accessible redesign y releases 2 capacity for project x."""
    states = feasible_states(2, (Constraint((2, -2), 0),))
    return {"feasible": [list(x) for x in states],
            "joint_project_feasible": (1, 1) in states,
            "source": "SYNTHETIC_RELEASE_ASSUMED_ACCESSIBLE"}


def apple_utility(q: int) -> int:
    """Discrete apples: storage costs generate a valley; market threshold a peak."""
    curve = (0, 4, 7, 8, 7, 5, 5, 9, 10)
    if type(q) is not int or not 0 <= q < len(curve):
        raise ValueError("only quantity q=0..8 is characterized")
    return curve[q]


def market_jump() -> dict:
    start = 3
    all_quantities = tuple(range(9))
    # A local-only agent refuses any immediately reducing step.
    reachable = {start}
    q = start
    while q < 8 and apple_utility(q + 1) >= apple_utility(q):
        q += 1
        reachable.add(q)
    return {"quantities": list(all_quantities),
            "values": [apple_utility(q) for q in all_quantities],
            "current": start,
            "local_non_loss_reachable": sorted(reachable),
            "best_global_quantity": max(all_quantities, key=apple_utility),
            "direct_jump_assumed_available": False,
            "source": "SYNTHETIC_NONMONOTONE_DISCRETE_UTILITY"}


def relative_gap(n: int, b: float, g: float, alpha: float = 0, topology: str = "dense") -> dict:
    """Parametric gap: matched-resource global counterfactual is an explicit assumption.

    Actual output P = b*n + alpha*E; reachable global comparison adds g*E.
    This is NOT demonstrated governability, genuine HID, or observed welfare.
    """
    if type(n) is not int or n < 1:
        raise ValueError("n >= 1 integer")
    if any(not isinstance(x, (int, float)) or x < 0 for x in (b, g, alpha)):
        raise ValueError("finite nonnegative coefficients required")
    if topology not in ("dense", "star", "none"):
        raise ValueError("only declared finite topologies")
    e = n*(n-1)//2 if topology == "dense" else n-1 if topology == "star" else 0
    actual = b*n + alpha*e
    if actual <= 0:
        raise ValueError("positive realized output required for relative ratio")
    gain = g*e
    return {"n": n, "topology": topology, "edges": e,
            "production_actual": actual,
            "gap_to_assumed_joint_optimum": gain,
            "production_joint_optimum": actual + gain,
            "gap_over_actual": gain / actual,
            "gap_over_joint_optimum": gain / (actual + gain),
            "status": "MODEL_ASSUMPTION_NOT_VERIFIED_OPTIMUM_OR_HID"}


def example_report() -> dict:
    return {"scope": "FINITE_SYNTHETIC_ONLY_OPEN_BCD_NOT_QUANTIFIED",
            "joint_trap": coupled_trap(),
            "saturation_no_reallocation": saturation_without_redesign(),
            "saturation_with_reallocation": saturation_with_redesign(),
            "nonmonotone_apples": market_jump(),
            "growth_dense": [relative_gap(n, 10, 0.2) for n in (5, 10, 20, 40)],
            "growth_sparse": [relative_gap(n, 10, 0.2, topology="star") for n in (5, 10, 20, 40)],
            "growth_realized_pair_synergy": [relative_gap(n, 10, 0.2, alpha=0.5)
                                           for n in (5, 10, 20, 40)]}


if __name__ == "__main__":
    print(json.dumps(example_report(), ensure_ascii=False, indent=2))
