"""Execute reusable, source-native economic matrices (ACC #44 and #57).

Usage:
    python -B economic_envelope_runner.py --corpus-root REPO --model both
    python -B economic_envelope_runner.py --corpus-root REPO --model agentic --details
    python -B economic_envelope_runner.py --corpus-root REPO --manifest MY_MATRIX.json
"""
from __future__ import annotations

import argparse
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
import json
from pathlib import Path
import sys
from typing import Any, Mapping

from economic_envelope import (
    affine_cost_crossing, compare_case, quantity, summary,
)
from economic_envelope_adapters import (
    agentic_cost_override, agentic_observations,
    intrinsic_cost_override, intrinsic_observations,
)

HERE = Path(__file__).resolve().parent
REL_STUDIES = Path("research/ecosystem-awareness/baseline/01I-artifacts/"
                   "acc-auxiliary-model-v0.1/studies")
SCHEMA = "ACC-ECONOMIC-ENVELOPE-MATRIX-v0.1"


def _load(name: str, path: Path):
    spec = spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ValueError("cannot load source: " + str(path))
    module = module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def _digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _nonnegative_int(value: Any, label: str) -> int:
    if type(value) is not int or value < 0:
        raise ValueError(label + " must be a nonnegative integer")
    return value


def execute(manifest: Mapping[str, Any], root: Path, *,
            model: str = "both", details: bool = False) -> dict[str, Any]:
    """Run user-specified grids against original policies; never alter their code."""
    if manifest.get("schema") != SCHEMA:
        raise ValueError("unknown comparison matrix schema")
    if model not in ("social", "agentic", "both"):
        raise ValueError("unknown source model")
    root = root.resolve()
    src_social = root / REL_STUDIES / "intrinsic-abcd-economics-v0.1/intrinsic_abcd.py"
    src_agentic = root / REL_STUDIES / "agentic-ecosystem-reduction-v0.1/agentic_reduction.py"
    src_cases = src_agentic.parent / "CASES.json"
    results = []
    pinned = {}
    if model in ("social", "both"):
        producer = _load("_acc_economic_source_social", src_social)
        pinned[str(src_social.relative_to(root))] = _digest(src_social)
        src = manifest["social"]
        sizes = src["sizes"]
        roots = src["roots"]
        accesses = src["accesses"]
        prices = src["prices"]
        if not all(type(n) is int and 2 <= n <= 256 for n in sizes):
            raise ValueError("social sizes must be integer leaf counts 2..256")
        for n, root_cfg, access, price_cfg in product(sizes, roots, accesses, prices):
            if access not in ("full", "target-inaccessible"):
                raise ValueError("unknown accessibility regime")
            idx = n // 4
            bits = tuple(1 if k == idx else 0 for k in range(n))
            slack = root_cfg["slack"]
            cap_root = None if slack is None else 8*n + _nonnegative_int(slack, "root slack")
            world = producer.balanced_tree(
                bits, cap_root=cap_root,
                inaccessible_path_leaf=idx if access == "target-inaccessible" else None,
            )
            changes = dict(price_cfg.get("costs", {}))
            if "peer_path_cost" in price_cfg:
                schedule = price_cfg["peer_path_cost"]
                length = len(producer.path_to(world, "source-" + str(idx)))
                price = quantity(schedule["fixed"]) + length*quantity(schedule["per_node"])
                if price < 0:
                    raise ValueError("negative directed path price")
                changes["target_observation"] = str(price)
            costs = intrinsic_cost_override(producer, changes)
            case_id = f"n{n}/{root_cfg['id']}/{access}/{price_cfg['id']}"
            result = compare_case(intrinsic_observations(
                producer, world, "source-" + str(idx), costs,
                scenario_id=case_id, planner_budget=1000,
            ))
            results.append(result)
    crossing = None
    if model in ("social", "both"):
        default = producer.Costs()
        eq = affine_cost_crossing(
            b_fixed=default.b_transmission + default.b_maintenance,
            b_per_path=default.b_issuance_per_path_node,
            peer_fixed=default.target_observation, peer_per_path=0,
        )
        crossing = {
            "model": "original Costs, fixed targeted source comparison",
            "classification": eq.classification,
            "path_nodes": None if eq.crossing_path_length is None else str(eq.crossing_path_length),
            "checks": {str(k): eq.at_path_length(k) for k in (6, 8, 9, 10)},
        }

    if model in ("agentic", "both"):
        agentic = _load("_acc_economic_source_agentic", src_agentic)
        fixture = json.loads(src_cases.read_text(encoding="utf-8"))
        if fixture["schema"] != agentic.SCHEMA:
            raise ValueError("agentic source fixture version mismatch")
        raw_cases = fixture["cases"]
        ids = [s["id"] for s in raw_cases]
        if len(ids) != len(set(ids)):
            raise ValueError("duplicate source agentic case")
        selection = manifest["agentic"]["case_ids"]
        if selection != "ALL":
            if not isinstance(selection, list) or len(selection) != len(set(selection)):
                raise ValueError("invalid agentic case selection")
            if set(selection) - set(ids):
                raise ValueError("selection references missing source case")
        for case, price_cfg in product(raw_cases, manifest["agentic"]["prices"]):
            if selection != "ALL" and case["id"] not in selection:
                continue
            if price_cfg.get("requires_q") and case.get("Q") is None:
                continue
            changes = dict(price_cfg.get("changes", {}))
            if price_cfg.get("equal_equivalent_q_cost"):
                if not isinstance(case.get("Q"), dict):
                    raise ValueError("equal-Q comparator requires a Q source")
                changes["directed.equivalent_Q_cost"] = case["Q"]["cost"]
            priced_case = agentic_cost_override(case, changes)
            case_id = case["id"] + "/" + price_cfg["id"]
            results.append(compare_case(agentic_observations(
                agentic, priced_case, scenario_id=case_id,
            )))
        pinned[str(src_agentic.relative_to(root))] = _digest(src_agentic)
        pinned[str(src_cases.relative_to(root))] = _digest(src_cases)
    # Never pool utility across different objectives or cases.
    output = {
        "schema": SCHEMA,
        "source_sha256": pinned,
        "social_break_even": crossing,
        "summary": summary(results),
        "evaluation": "POST_HOC_SYNTHETIC_REFEREE",
        "decision_contract": "SOURCE_NATIVE_POLICY_ONLY",
        "cross_question_composition": "NOT_PERFORMED",
    }
    if details:
        output["cases"] = [result.as_dict() for result in results]
    return output


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--corpus-root", type=Path, required=True)
    ap.add_argument("--manifest", type=Path, default=HERE / "ECONOMIC_SWEEP_MANIFEST.json")
    ap.add_argument("--model", choices=("social", "agentic", "both"), default="both")
    ap.add_argument("--details", action="store_true")
    args = ap.parse_args(argv)
    document = json.loads(args.manifest.read_text(encoding="utf-8"))
    output = execute(document, args.corpus_root, model=args.model, details=args.details)
    output["manifest_sha256"] = _digest(args.manifest)
    print(json.dumps(output, sort_keys=True, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
