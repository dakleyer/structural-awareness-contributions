#!/usr/bin/env python3
"""Proposed DDS Stage A v0.4 checker successor for audit T05 and T06.

Preserves frozen v0.2 unchanged. T06 checks that every NOT_APPLICABLE
result provides a nonblank rationale (not its preregistration). T05 projects
Stage A declaration separately from Stage B realization/runtime assurance
for runtime-named claims. A Stage A pass is not runtime verification.
This remains an unadmitted audit candidate, not an independently accepted
instrument or a Stage B/C implementation result.
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
    """New v0.4 result-admission condition failed."""


def require_na_rationale(result: dict[str, Any]) -> None:
    """Enforce typed NA substitution and rationale before running frozen v0.2.

    Whether a reason predates the inspected outcomes remains a separate
    preregistration and reviewer obligation.
    """
    for position, row in enumerate(result.get("gates", [])):
        if not isinstance(row, dict):
            raise ApplicabilityContractError(f"non_object_gate_row:{position}")
        if ("na_substitute_satisfied" in row
                and not isinstance(row["na_substitute_satisfied"], bool)):
            gid = row.get("gate_id", f"row-{position}")
            raise ApplicabilityContractError(
                f"na_substitute_satisfied_must_be_boolean:{gid}"
            )
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


def project_cross_stage_claims(compiled: dict[str, Any], catalog: dict[str, Any]) -> None:
    """Separate Stage A declaration from runtime assurance in named claims.

    Preserve v0.2's Stage A profile_outcome. Its authoritative reference is
    the frozen Challenge/specification, not a Stage B/C execution trace.
    Never trust participant-supplied Stage B status in a Stage A result.
    """
    catalog_claims = catalog.get("named_claims", {})
    runtime_named = (
        "CLAIM-RUNTIME-ENFORCEABILITY",
        "CLAIM-TRACEABLE-DISPOSITION-TO-ENFORCEMENT",
    )
    for name in runtime_named:
        if name in catalog_claims and not catalog_claims[name].get(
                "stage_b_required_for_runtime_claim"):
            raise RuntimeError(f"stage_b_requirement_missing_for:{name}")

    projected = []
    for claim in compiled.get("named_claims", []):
        name = claim.get("claim")
        source_claim = catalog_claims.get(name, {})
        if not source_claim.get("stage_b_required_for_runtime_claim", False):
            continue
        stage_a = claim["status"]
        claim["stage_a_declaration_status"] = stage_a
        claim["stage_b_realization_status"] = "NOT_ESTABLISHED"
        claim["runtime_assurance_status"] = "NOT_ESTABLISHED"
        claim["claim_scope"] = "STAGE_A_DECLARATION_ONLY"
        claim["runtime_assurance_note"] = (
            "Stage A evaluates the declared rule, not Stage B architecture "
            "realization or observed Stage C effects."
        )
        # A consumer inspecting only 'status' can no longer mistake a
        # Stage A declaration PASS for runtime enforcement verification.
        if stage_a == "PASS":
            claim["status"] = "CONDITIONAL_ON(STAGE_B_VERIFICATION)"
        elif stage_a.startswith("FAIL"):
            claim["status"] = stage_a
        else:
            claim["status"] = (
                "CONDITIONAL_ON(STAGE_A_DECLARATION,STAGE_B_VERIFICATION)"
            )
        projected.append(name)

    summary = compiled.setdefault("summary", {})
    summary["profile_outcome_scope"] = "DDS_STAGE_A_ONLY"
    summary["stage_b_realization_status"] = "NOT_ESTABLISHED"
    summary["runtime_assurance_status"] = "NOT_ESTABLISHED"
    summary["cross_stage_claims_projected"] = sorted(projected)


def compile_successor(catalog: dict[str, Any], result: dict[str, Any]) -> dict[str, Any]:
    require_na_rationale(result)
    base = load_frozen_checker()
    compiled = base.compile_result(catalog, result)
    project_cross_stage_claims(compiled, catalog)
    compiled["diagnostic_checker_successor"] = {
        "revision": "v0.4-audit-candidate",
        "additional_control": "T06-not-applicable-rationale-present",
        "additional_controls": [
            "T05-stage-a-declaration-versus-stage-b-runtime-claim-projection",
            "T06-not-applicable-rationale-present",
            "C74-typed-not-applicable-substitution",
        ],
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
