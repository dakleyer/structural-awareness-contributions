"""Command-line driver for the ACC auxiliary executable economic toy.

No file writes. Results are emitted to stdout as JSON or sweep CSV.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
import csv
from itertools import product
import json
from pathlib import Path
import sys

from toy import ToyError, evaluate


def update_path(config, assignment):
    if "=" not in assignment:
        raise ToyError("override must be dotted.path=JSON_VALUE")
    path, encoded = assignment.split("=", 1)
    try:
        value = json.loads(encoded)
    except json.JSONDecodeError as exc:
        raise ToyError("override value must be valid JSON: " + assignment) from exc
    cursor = config
    parts = path.split(".")
    if not parts or any(not part for part in parts):
        raise ToyError("invalid override path")
    for key in parts[:-1]:
        if not isinstance(cursor, dict) or key not in cursor:
            raise ToyError("unknown override path: " + path)
        cursor = cursor[key]
    if not isinstance(cursor, dict) or parts[-1] not in cursor:
        raise ToyError("unknown override path: " + path)
    prior = cursor[parts[-1]]
    if type(prior) is bool and type(value) is not bool:
        raise ToyError("boolean override must be true/false: " + path)
    if type(prior) in (int, float) and type(value) not in (int, float):
        raise ToyError("numeric override required: " + path)
    if type(prior) is str and type(value) is not str:
        raise ToyError("string override required: " + path)
    cursor[parts[-1]] = value
    return path, value


def compact(result):
    if result["mode"] == "network":
        row = result["rows"][-1]
        return {
            "mode": "network",
            "horizon": result["horizon"],
            "production": row["production"],
            "d_t": row["d_t"],
            "D_T": row["D_T"],
            "delta2_d_t": row["delta2_d_t"],
            "G_path_technical": row["G_path_technical"],
            "G_path_governable": row["G_path_governable"],
            "HID_observed": row["human"]["HID_observed"],
            "HID_potential": row["human"].get("HID_potential"),
            "epistemic_ABCD_status": result["epistemic_ABCD_experiment"]["status"],
            **result["summary"],
        }
    if result["mode"] == "portfolio":
        direct = result["hid"]["primary_optimum_input_gap"]
        technical_hid = [s["HID_direct_hours"] for s in direct["technical_utility_optima"]
                         if s["HID_direct_hours"] is not None]
        governed_hid = [s["HID_direct_hours"] for s in direct["governance_utility_optima"]
                        if s["HID_direct_hours"] is not None]
        return {
            "mode": "portfolio", "n": result["dimension_count"],
            "G_technical": result["G_technical"], "G_governable": result["G_governable"],
            "G_efficiency": result["G_efficiency_same_service_resources"],
            "state_count_F_T": result["state_count_F_T"],
            "state_count_F_G": result["state_count_F_G"],
            "suboptimal_technical": result["suboptimal_technical"],
            "suboptimal_governable": result["suboptimal_governable"],
            "HID_observed": result["hid"]["HID_observed"],
            "HID_potential": result["hid"].get("HID_potential"),
            "HID_direct_technical_optima_count": len(direct["technical_utility_optima"]),
            "HID_direct_comparable_technical_count": len(technical_hid),
            "HID_direct_technical_min_hours": min(technical_hid) if technical_hid else None,
            "HID_direct_technical_max_hours": max(technical_hid) if technical_hid else None,
            "HID_direct_governance_min_hours": min(governed_hid) if governed_hid else None,
            "HID_direct_governance_max_hours": max(governed_hid) if governed_hid else None,
            "technical_optimum_projects": result["technical_optimum"]["projects"],
        }
    return {"mode": "formulas", **result["rows"][-1]}


def run_cli(argv=None):
    parser = argparse.ArgumentParser(
        description="Parametric synthetic ACC economic model; no empirical validation")
    parser.add_argument("mode", choices=("portfolio", "network", "formulas"))
    parser.add_argument("scenario", help="scenario JSON file")
    parser.add_argument("--set", action="append", default=[], metavar="PATH=JSON",
                        help="override existing scenario field; repeatable")
    parser.add_argument("--sweep", action="append", default=[], metavar="PATH=JSON_ARRAY",
                        help="cartesian product over arrays of typed values; repeatable")
    parser.add_argument("--summary", action="store_true", help="compact scalar output")
    parser.add_argument("--format", choices=("json", "csv"), default="json",
                        help="CSV is available for sweeps only")
    args = parser.parse_args(argv)
    try:
        scenario = json.loads(Path(args.scenario).read_text(encoding="utf-8"))
        if scenario.get("mode") != args.mode:
            raise ToyError("CLI mode does not match scenario.mode")
        for assignment in args.set:
            update_path(scenario, assignment)
        if args.sweep:
            grid = []
            for expr in args.sweep:
                if "=" not in expr:
                    raise ToyError("sweep must be PATH=[JSON,VALUES]")
                path, encoded = expr.split("=", 1)
                try:
                    options = json.loads(encoded)
                except json.JSONDecodeError as exc:
                    raise ToyError("invalid JSON sweep array") from exc
                if not isinstance(options, list) or not options:
                    raise ToyError("each sweep must be a nonempty JSON array")
                grid.append((path, options))
            total = 1
            for _, options in grid:
                total *= len(options)
            if total > 256:
                raise ToyError("sweep exceeds 256 combinations")
            results = []
            for values in product(*(opts for _, opts in grid)):
                config = deepcopy(scenario)
                applied = {}
                for (path, _), value in zip(grid, values):
                    _, val = update_path(config, path + "=" + json.dumps(value))
                    applied[path] = val
                results.append({**applied, **compact(evaluate(config))})
            if args.format == "csv":
                fieldnames = list(dict.fromkeys(key for row in results for key in row))
                writer = csv.DictWriter(sys.stdout, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(results)
            else:
                print(json.dumps({"status": "SYNTHETIC_PARAMETER_SWEEP", "cases": results},
                                 indent=2, sort_keys=True, allow_nan=False))
        else:
            if args.format == "csv":
                raise ToyError("CSV format requires --sweep")
            result = evaluate(scenario)
            print(json.dumps(compact(result) if args.summary else result,
                             indent=2, sort_keys=True, allow_nan=False))
        return 0
    except (OSError, json.JSONDecodeError, ToyError) as exc:
        print("Toy error: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(run_cli())
