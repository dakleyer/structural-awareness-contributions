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

def select(data, view="impact", wave=None, limit=10, include_planning=False):
    rows = [item for item in data["entries"] if item["state"] == "Pendiente de decisión"
            or include_planning and item["state"] == "Por concretar; sin par literal"]
    if view == "decision":
        rows = [item for item in rows if item["decision_ready"]]
    if wave is not None:
        rows = [item for item in rows if item["wave"].startswith(str(wave) + " —")]
    return sorted(rows, key=key)[:limit]

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
    print(json.dumps({"source_commit": data["source_commit"], "view": args.view,
        "authorized_to_apply": False, "items": [
        {name: row[name] for name in ("id", "title", "impact", "risk", "effort", "wave", "state", "preparation", "vnext")}
        for row in rows]}, ensure_ascii=True, indent=2))

if __name__ == "__main__":
    main()
