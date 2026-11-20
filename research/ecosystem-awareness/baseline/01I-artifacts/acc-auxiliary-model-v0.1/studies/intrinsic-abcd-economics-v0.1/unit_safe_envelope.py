"""Unit-safe replacement report for #66; original policies remain source-owned.

Physical output and acquisition prices are independent measurement axes. Their
Pareto frontier is not an ACC K-vector or a total economic ranking. No scalar
conversion, dimension assignment, permission or action is inferred here.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
from typing import Any, Mapping

from economic_envelope import quantity
from economic_envelope_runner import execute

HERE = Path(__file__).resolve().parent
SCHEMA = "ACC-UNIT-SAFE-ENVELOPE-v0.1"


def _name(value: Any) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("nonempty measurement identity required")
    return value


def project_case(source: Mapping[str, Any]) -> dict[str, Any]:
    """Use source output/cost only; never source net, leaders or scalar deltas."""
    if not isinstance(source, Mapping):
        raise ValueError("source case must be a mapping")
    frame = source["frame"]
    if not isinstance(frame, Mapping):
        raise ValueError("source frame must be a mapping")
    for key in ("case_id", "model", "scope", "question", "output_unit",
                "cost_unit", "horizon", "public_contract_id"):
        _name(frame[key])
    arms = source["arms"]
    if not isinstance(arms, (list, tuple)) or len(arms) < 2:
        raise ValueError("at least two source observations required")
    seen = set()
    rows = []
    diagnostics = []
    for arm in arms:
        name = _name(arm["arm"])
        if name in seen:
            raise ValueError("duplicate source arm")
        seen.add(name)
        gross = None if arm["gross"] is None else quantity(arm["gross"])
        cost = None if arm["cost"] is None else quantity(arm["cost"])
        if cost is not None and cost < 0:
            raise ValueError("negative acquisition price")
        components = arm["components"]
        if not isinstance(components, Mapping):
            raise ValueError("itemized source costs required")
        charged = []
        normalized_components = {}
        for key, value in components.items():
            _name(key)
            value = quantity(value)
            if value < 0:
                raise ValueError("negative cost component")
            charged.append(value)
            normalized_components[key] = str(value)
        if cost is not None and sum(charged, quantity(0)) != cost:
            raise ValueError("cost components disagree with total")
        row = {"arm": name, "output": None if gross is None else str(gross),
               "information_cost": None if cost is None else str(cost),
               "cost_components": normalized_components,
               "source_status": _name(arm["status"]),
               "source": _name(arm["source"]),
               "controls_or_permission": "NOT_INFERRED_FROM_MEASUREMENTS"}
        if name == "SOURCE_PUBLIC_RECEIVER":
            diagnostics.append(row)
        else:
            rows.append(row)
    if source["baseline_arm"] not in {row["arm"] for row in rows}:
        raise ValueError("missing source baseline")
    if len(rows) < 2:
        raise ValueError("at least two competing source policies required")
    known = [row for row in rows if row["output"] is not None
             and row["information_cost"] is not None]
    def dominates(a, b):
        ao, bo = quantity(a["output"]), quantity(b["output"])
        ac, bc = quantity(a["information_cost"]), quantity(b["information_cost"])
        return ao >= bo and ac <= bc and (ao > bo or ac < bc)
    frontier = [row["arm"] for row in known
                if not any(dominates(other, row) for other in known)]
    unknown = [row["arm"] for row in rows if row not in known]
    # The old metric name may describe a scalar net; it is not propagated.
    clean_frame = {key: deepcopy(frame[key]) for key in (
        "case_id", "model", "scope", "question", "output_unit", "cost_unit",
        "horizon", "public_contract_id", "baseline_a")}
    matched = []
    for i, left in enumerate(known):
        for right in known[i + 1:]:
            if quantity(left["output"]) == quantity(right["output"]):
                lc, rc = quantity(left["information_cost"]), quantity(right["information_cost"])
                matched.append({
                    "arms": [left["arm"], right["arm"]],
                    "matched_output": left["output"],
                    "lower_information_cost_arm": left["arm"] if lc < rc else right["arm"] if rc < lc else "TIE",
                    "cost_difference_left_minus_right": str(lc - rc),
                    "scope": "SAME_REALIZED_OUTPUT_WITHIN_THIS_SOURCE_FRAME"})
    baseline = next(row for row in rows if row["arm"] == source["baseline_arm"])
    gains = {row["arm"]: None if row["output"] is None or baseline["output"] is None
             else str(quantity(row["output"]) - quantity(baseline["output"]))
             for row in rows}
    return {
        "frame": clean_frame,
        "measurement_axes": {
            "output": {"unit": frame["output_unit"], "direction": "INCREASE"},
            "information_cost": {"unit": frame["cost_unit"], "direction": "DECREASE"}},
        "baseline_arm": source["baseline_arm"], "observations": rows,
        "source_receiver_diagnostics": diagnostics,
        "measurement_frontier": frontier,
        "physical_output_gain_vs_baseline": gains,
        "matched_output_cost_order": matched,
        "unknown_measurement_arms": unknown,
        "status": "UNKNOWN_MEASUREMENTS" if unknown else "KNOWN_MEASUREMENT_PARTIAL_ORDER",
        "frontier_scope": "KNOWN_OUTPUT_AND_PRICE_ONLY",
        "economic_winner": "NOT_INFERRED",
        "ACC_dimension_assignment": "NOT_INFERRED_FROM_INSTRUMENT_METRICS",
        "full_open_K_dominance": "NOT_ESTABLISHED",
        "governance": "SOURCE_OWNED_SEPARATE_CONTROLS",
        "source_policy_semantics": "LEGACY_SCALAR_POLICY_UNCHANGED_NOT_REVALIDATED",
    }


def project_report(legacy: Mapping[str, Any]) -> dict[str, Any]:
    if "cases" not in legacy:
        raise ValueError("source detail required; scalar summaries are insufficient")
    cases = [project_case(case) for case in legacy["cases"]]
    identities = [(case["frame"]["model"], case["frame"]["case_id"]) for case in cases]
    if len(identities) != len(set(identities)):
        raise ValueError("duplicate source model/case")
    groups = {}
    for case in cases:
        group = groups.setdefault(case["frame"]["model"],
                                  {"cases": 0, "unknown_measurement_cases": 0})
        group["cases"] += 1
        group["unknown_measurement_cases"] += case["status"] == "UNKNOWN_MEASUREMENTS"
    return {"schema": SCHEMA, "cases": cases, "groups": groups,
            "source_sha256": deepcopy(legacy.get("source_sha256", {})),
            "aggregation": "COUNTS_ONLY_NO_NET_NO_TOTAL_RANKING",
            "controls": "PERMISSION_AUTHORITY_FEASIBILITY_NOT_INFERRED",
            "claim_boundary": "SYNTHETIC_POST_HOC_MEASUREMENTS_NOT_ACC_ADMISSION",
            "legacy_scalar_claims": "NOT_PROPAGATED"}


def run(manifest: Mapping[str, Any], root: Path, *, model: str = "both") -> dict:
    # execute retains native decisions and source accounting checks. Invalid
    # cross-unit net/leader fields are deliberately discarded at this boundary.
    return project_report(execute(manifest, root, model=model, details=True))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus-root", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, default=HERE / "ECONOMIC_SWEEP_MANIFEST.json")
    parser.add_argument("--model", choices=("social", "agentic", "both"), default="both")
    args = parser.parse_args()
    manifest_bytes = args.manifest.read_bytes()
    manifest = json.loads(manifest_bytes.decode("utf-8"))
    result = run(manifest, args.corpus_root, model=args.model)
    result["manifest_sha256"] = sha256(manifest_bytes).hexdigest()
    print(json.dumps(result, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

