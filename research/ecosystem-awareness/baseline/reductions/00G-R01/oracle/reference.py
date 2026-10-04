"""Primary exact reference for the first bounded R01 C02 fixture family.

This method exhaustively enumerates explicitly frozen complete trajectories.
It has privileged access to private world truth and must never be imported by a
technology adapter.
"""

from __future__ import annotations

from typing import Any, Mapping


def evaluate_world(world: Mapping[str, Any]) -> dict[str, Any]:
    rows = []
    enumeration_units = 0
    for trajectory in world["trajectories"]:
        enumeration_units += 1
        total = 0
        admissible = True
        complete = True
        for step in trajectory["steps"]:
            total += int(step["benefit"])
            admissible = admissible and bool(step["admissible"])
            complete = complete and bool(step.get("completed", True))
        for connector in trajectory.get("connectors", []):
            total += int(connector.get("benefit", 0))
            admissible = admissible and bool(connector["admissible"])
            complete = complete and bool(connector.get("completed", True))
        rows.append({
            "trajectory_id": trajectory["trajectory_id"],
            "J": total,
            "admissible": admissible,
            "complete": complete,
        })

    candidates = [r for r in rows if r["admissible"] and r["complete"]]
    if not candidates:
        return {
            "reference_status": "NOT_ESTABLISHED",
            "reason": "no_complete_admissible_trajectory",
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
