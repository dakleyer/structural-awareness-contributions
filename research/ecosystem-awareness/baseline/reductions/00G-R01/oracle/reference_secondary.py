"""Separate exact cross-check path for the first bounded R01 fixture.

This intentionally does not call reference.evaluate_world or share its scoring
helper. It is a second implementation path, not independent external validation.
"""

from __future__ import annotations

from typing import Any, Mapping


def evaluate_world_secondary(world: Mapping[str, Any]) -> dict[str, Any]:
    scores: dict[str, int] = {}
    rejected: set[str] = set()
    incomplete: set[str] = set()
    units = 0

    for item in world["trajectories"]:
        units += 1
        tid = item["trajectory_id"]
        score = 0
        for element in list(item["steps"]) + list(item.get("connectors", [])):
            score += int(element.get("benefit", 0))
            if element.get("admissible") is not True:
                rejected.add(tid)
            if element.get("completed", True) is not True:
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
