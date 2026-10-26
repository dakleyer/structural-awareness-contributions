"""Primary exact reference for the first bounded R01 C02 fixture family.

This method exhaustively enumerates explicitly frozen complete trajectories.
It has privileged access to private world truth and must never be imported by a
technology adapter.
"""

from __future__ import annotations

from typing import Any, Mapping


def _element_values(element: Mapping[str, Any]) -> tuple[int, bool, bool]:
    benefit = element.get("benefit", 0)
    admissible = element.get("admissible")
    completed = element.get("completed", True)
    if type(benefit) is not int:
        raise ValueError("reference benefit must be an integer")
    if type(admissible) is not bool:
        raise ValueError("reference admissible must be a boolean")
    if type(completed) is not bool:
        raise ValueError("reference completed must be a boolean")
    return benefit, admissible, completed


def evaluate_world(world: Mapping[str, Any]) -> dict[str, Any]:
    trajectories = world.get("trajectories")
    if not isinstance(trajectories, list) or not trajectories:
        raise ValueError("private world requires a non-empty trajectories list")

    rows = []
    enumeration_units = 0
    for trajectory in trajectories:
        if not isinstance(trajectory, Mapping):
            raise ValueError("trajectory must be an object")
        trajectory_id = trajectory.get("trajectory_id")
        if not isinstance(trajectory_id, str) or not trajectory_id:
            raise ValueError("trajectory_id must be a non-empty string")
        steps = trajectory.get("steps")
        if not isinstance(steps, list) or not steps:
            raise ValueError(f"{trajectory_id}: steps must be a non-empty list")

        enumeration_units += 1
        total = 0
        admissible = True
        complete = True

        for step in steps:
            if not isinstance(step, Mapping):
                raise ValueError(f"{trajectory_id}: step must be an object")
            benefit, step_admissible, step_complete = _element_values(step)
            total += benefit
            admissible = admissible and step_admissible
            complete = complete and step_complete

        connectors = trajectory.get("connectors", [])
        if not isinstance(connectors, list):
            raise ValueError(f"{trajectory_id}: connectors must be a list")
        for connector in connectors:
            if not isinstance(connector, Mapping):
                raise ValueError(f"{trajectory_id}: connector must be an object")
            benefit, connector_admissible, connector_complete = _element_values(connector)
            total += benefit
            admissible = admissible and connector_admissible
            complete = complete and connector_complete

        rows.append({
            "trajectory_id": trajectory_id,
            "J": total,
            "admissible": admissible,
            "complete": complete,
        })

    candidates = [r for r in rows if r["admissible"] and r["complete"]]
    if not candidates:
        return {
            "reference_status": "NOT_ESTABLISHED",
            "reason": "no_complete_admissible_trajectory",
            "optimum_J": None,
            "optimum_trajectory_ids": [],
            "rows": rows,
            "enumeration_units": enumeration_units,
        }
    optimum = max(r["J"] for r in candidates)
    ids = sorted(r["trajectory_id"] for r in candidates if r["J"] == optimum)
    return {
        "reference_status": "ESTABLISHED",
        "optimum_J": optimum,
        "optimum_trajectory_ids": ids,
        "rows": rows,
        "enumeration_units": enumeration_units,
    }
