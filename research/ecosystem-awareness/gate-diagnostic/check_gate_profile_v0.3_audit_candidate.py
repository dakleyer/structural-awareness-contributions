#!/usr/bin/env python3
"""Proposed DDS Stage A v0.3 checker successor for audit T06.

Preserves frozen v0.2 untouched. Adds a result-row completeness check:
NOT_APPLICABLE requires a nonempty, human-readable applicability rationale.
This checks existence of a reason, not that it was preregistered or true.
NOT a promoted or independently accepted DDS instrument.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

FROZEN_BASE = Path(__file__).with_name("check_gate_profile_v0.2.py")


class ApplicabilityContractError(ValueError):
    """New v0.3 result-admission condition failed."""


def require_na_rationale(result: dict[str, Any]) -> None:
    """Enforce per-row NA rationale presence before running frozen v0.2.

    Whether a reason predates the inspected outcomes remains a separate
    preregistration and reviewer obligation.
    """
    for position, row in enumerate(result.get("gates", [])):
        if not isinstance(row, dict):
            raise ApplicabilityContractError(f"non_object_gate_row:{position}")
        if (row.get("applicability") == "NOT_APPLICABLE"
                or row.get("own_verdict") == "NOT_APPLICABLE"):
            rationale = row.get("applicability_rationale")
            if not isinstance(rationale, str) or not rationale.strip():
                gid = row.get("gate_id", f"row-{position}")
                raise ApplicabilityContractError(
                    f"not_applicable_requires_rationale:{gid}"
                )


def load_frozen_checker():
    """Load the original source file without editing it."""
    spec = importlib.util.spec_from_file_location("dds_stage_a_checker_v02", FROZEN_BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError("frozen_v02_checker_unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def compile_successor(catalog: dict[str, Any], result: dict[str, Any]) -> dict[str, Any]:
    require_na_rationale(result)
    base = load_frozen_checker()
    compiled = base.compile_result(catalog, result)
    compiled["diagnostic_checker_successor"] = {
        "revision": "v0.3-audit-candidate",
        "additional_control": "T06-not-applicable-rationale-present",
        "pre_registration_verified": False,
        "independent_review_status": "NOT_ESTABLISHED",
        "stage_b_or_c_validation": "NOT_ESTABLISHED",
    }
    return compiled


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalog")
    parser.add_argument("result")
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        catalog = json.loads(Path(args.catalog).read_text(encoding="utf-8"))
        result = json.loads(Path(args.result).read_text(encoding="utf-8"))
        payload = json.dumps(compile_successor(catalog, result), indent=2, ensure_ascii=False) + "\n"
        if args.output:
            Path(args.output).write_text(payload, encoding="utf-8")
        else:
            sys.stdout.write(payload)
        return 0
    except (ApplicabilityContractError, ValueError, OSError, ImportError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
