# Priority extractor v1.2 — applies dated assessments; source proposals stay immutable.
"""Extrae prioridades documentales sin modificar el corpus ni ejecutar sus programas."""
import argparse
import json
from pathlib import Path

ORDER = {
    "impact": {"Alto": 0, "Medio": 1, "Bajo": 2, "No vigente": 3},
    "priority": {"Primera": 0, "Siguiente": 1, "Después": 2, "Histórico": 3},
    "risk": {"Bajo": 0, "Medio": 1, "Alto": 2},
    "effort": {"Bajo": 0, "Medio": 1, "Alto": 2, "No estimable todavía": 3, "No nuevo": 4, "No procede": 5},
}

def key(item):
    return tuple(ORDER[name].get(item[name], 99) for name in ("impact", "priority", "risk", "effort")) + (item["id"],)

RATING_FIELDS = {"impact", "risk", "effort", "priority", "wave", "benefit",
                 "riskReason", "costReason", "gate", "preparation", "decision_ready"}

def effective_entries(data):
    # Keep the stored proposal, source and historical state immutable; derive current views.
    rows = [dict(item) for item in data["entries"]]
    by_id = {item["id"]: item for item in rows}
    for epoch in data.get("rating_updates", []):
        for update in epoch["updates"]:
            if update["id"] not in by_id:
                raise ValueError("Assessment targets an unknown proposal")
            for field in RATING_FIELDS:
                if field in update:
                    by_id[update["id"]][field] = update[field]
    # Dated quality assessments do not modify stored source text or the old/new pair.
    quality_fields = RATING_FIELDS | {"state", "quality", "rationale", "acceptance",
                                     "joint_changes", "current_literal_check", "authorized_to_apply"}
    for epoch in data.get("plan_quality_review_epochs", []):
        for update in epoch["proposal_assessments"]:
            if update["id"] not in by_id:
                raise ValueError("Plan review targets an unknown proposal")
            for field in quality_fields:
                if field in update:
                    by_id[update["id"]][field] = update[field]
    return rows

def preparation_order(data, rows):
    """Rank eligible candidates while preserving explicit preparation precedence."""
    remaining = {item["id"]: item for item in rows}
    edges = data.get("plan_order", {}).get("precedence", [])
    ordered = []
    while remaining:
        eligible = [item for ident, item in remaining.items()
                    if not any(after == ident and before in remaining
                               for before, after in edges)]
        if not eligible:
            raise ValueError("Cyclic preparation order")
        chosen = min(eligible, key=key)
        ordered.append(chosen)
        del remaining[chosen["id"]]
    return ordered


def select(data, view="impact", wave=None, limit=10, include_planning=False):
    rows = [item for item in effective_entries(data) if item["state"] == "Pendiente de decisión"
            or include_planning and item["state"] == "Por concretar; sin par literal"]
    if view == "decision":
        rows = [item for item in rows if item["decision_ready"]]
    if wave is not None:
        rows = [item for item in rows if item["wave"].startswith(str(wave) + " —")]
    return preparation_order(data, rows)[:limit]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data", type=Path, default=Path(__file__).with_name("priorities.json"))
    parser.add_argument("--view", choices=("impact", "decision"), default="impact")
    parser.add_argument("--wave", type=int, choices=(1, 2, 3, 4))
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--include-planning", action="store_true")
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be positive")
    data = json.loads(args.data.read_text(encoding="utf-8"))
    rows = select(data, args.view, args.wave, args.limit, args.include_planning)
    print(json.dumps({"source_commit": data.get("review_source_commit", data["source_commit"]), "view": args.view,
        "authorized_to_apply": False, "order_meaning": "preparation only; preserve gates and joint review", "items": [
        {name: row[name] for name in ("id", "title", "impact", "risk", "effort", "wave", "state", "preparation", "vnext", "gate", "dependencies")}
        for row in rows]}, ensure_ascii=True, indent=2))

if __name__ == "__main__":
    main()
