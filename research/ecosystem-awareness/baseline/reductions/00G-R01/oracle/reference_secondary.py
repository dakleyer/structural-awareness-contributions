"""Separate exact cross-check path for the first bounded R01 fixture.

This intentionally does not call reference.evaluate_world or share its scoring
helper. It is a second implementation path, not independent external validation.
"""

from __future__ import annotations

from typing import Any, Mapping


def evaluate_world_secondary(world: Mapping[str, Any]) -> dict[str, Any]:
    trajectories = world.get("trajectories")
    if not isinstance(trajectories, list) or not trajectories:
        raise ValueError("secondary reference requires non-empty trajectories")

    scores: dict[str, int] = {}
    rejected: set[str] = set()
    incomplete: set[str] = set()
    units = 0

    for item in trajectories:
        if not isinstance(item, Mapping):
            raise ValueError("secondary trajectory must be an object")
        tid = item.get("trajectory_id")
        if not isinstance(tid, str) or not tid:
            raise ValueError("secondary trajectory_id must be a non-empty string")
        if tid in scores:
            raise ValueError(f"duplicate trajectory_id: {tid}")

        steps = item.get("steps")
        connectors = item.get("connectors", [])
        if not isinstance(steps, list) or not steps:
            raise ValueError(f"{tid}: steps must be a non-empty list")
        if not isinstance(connectors, list):
            raise ValueError(f"{tid}: connectors must be a list")

        units += 1
        score = 0
        for element in list(steps) + list(connectors):
            if not isinstance(element, Mapping):
                raise ValueError(f"{tid}: reference element must be an object")
            benefit = element.get("benefit", 0)
            admissible = element.get("admissible")
            completed = element.get("completed", True)
            if type(benefit) is not int:
                raise ValueError(f"{tid}: benefit must be an integer")
            if type(admissible) is not bool:
                raise ValueError(f"{tid}: admissible must be a boolean")
            if type(completed) is not bool:
                raise ValueError(f"{tid}: completed must be a boolean")
            score += benefit
            if admissible is not True:
                rejected.add(tid)
            if completed is not True:
                incomplete.add(tid)
        scores[tid] = score

    eligible = {k: v for k, v in scores.items() if k not in rejected and k not in incomplete}
    if not eligible:
        return {
            "reference_status": "NOT_ESTABLISHED",
            "reason": "no_complete_admissible_trajectory",
            "optimum_J": None,
            "optimum_trajectory_ids": [],
            "enumeration_units": units,
        }

    optimum = max(eligible.values())
    return {
        "reference_status": "ESTABLISHED",
        "optimum_J": optimum,
        "optimum_trajectory_ids": sorted(k for k, v in eligible.items() if v == optimum),
        "enumeration_units": units,
    }
