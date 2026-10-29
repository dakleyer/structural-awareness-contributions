"""Run the original source-anchored experiments across social and agentic models.

python -B run_original_experiments.py --model both
python -B run_original_experiments.py --model social --compact
No original source files or reference results are rewritten.
"""
from __future__ import annotations
import argparse
import json
from hashlib import sha256
from pathlib import Path

from dimension_experiment import run_manifest
from native_experiment_adapters import native_operators

HERE = Path(__file__).resolve().parent
SOCIAL = "ORIGINAL_EXPERIMENTS.json"
NATIVE = "NATIVE_EXPERIMENTS.json"



def evidence_origin_accounting(
    selected_cases: list[dict], selected_results: list[dict],
) -> dict:
    """Separate assumed social gates from computed physical constraints.

    A selected scenario may have multiple independent blockers. The reported
    primary basis uses an explicit diagnostic precedence for counts, and all
    contributing negative/unknown checks remain individually visible.
    This does not infer a causal driver in real social systems.
    """
    original = {c["case_id"]: c for c in selected_cases
                if c["model"] == "SOCIAL_FINITE"}
    observed = {row["case_id"]: row for row in selected_results
                if row["model"] == "SOCIAL_FINITE"}
    if set(original) != set(observed):
        raise ValueError("source/observation mismatch in social audit register")
    totals = {
        "source_owned_social_cases":len(original),
        "declared_conditions":0,"calculated_conditions":0,
        "eligible_conditional":0,"non_eligible":0,
        "primary_noneligible_basis":{},
        "basis_warning":"PRIMARY BASIS IS A DETERMINISTIC AUDIT GROUPING, NOT A CAUSAL EXPLANATION",
        "details":[],
    }
    for key, case in original.items():
        report = observed[key]
        source_constraints = {c["id"]:c for c in case["constraints"]}
        evidence = []
        if set(source_constraints) != {c["id"] for c in report["constraints"]}:
            raise ValueError("constraint identity drift in "+key)
        for c in report["constraints"]:
            origin = ("SOURCE_DECLARED_GATE" if "satisfied" in source_constraints[c["id"]]
                      else "COMPUTED_EFFECT_CONSTRAINT")
            totals["declared_conditions" if origin=="SOURCE_DECLARED_GATE"
                   else "calculated_conditions"] += 1
            evidence.append({
                "id":c["id"],"category":c["category"],"status":c["status"],
                "origin":origin,
            })
        eligible=report["admission"]=="ELIGIBLE_UNDER_DECLARED_CONDITIONS"
        if eligible:
            totals["eligible_conditional"] += 1
            basis="ELIGIBLE_CONDITIONAL"
        else:
            totals["non_eligible"] += 1
            if report["physical_status"] == "IMPOSSIBLE":
                basis="COMPUTED_PHYSICAL_IMPOSSIBILITY"
            elif any(c["origin"]=="COMPUTED_EFFECT_CONSTRAINT"
                     and c["status"]=="FAILED" for c in evidence):
                basis="COMPUTED_EFFECT_FAILURE"
            elif any(c["origin"]=="SOURCE_DECLARED_GATE"
                     and c["status"]=="FAILED" for c in evidence):
                basis="SOURCE_DECLARED_FAILURE"
            elif any(c["origin"]=="SOURCE_DECLARED_GATE"
                     and c["status"]=="UNKNOWN" for c in evidence):
                basis="SOURCE_DECLARED_UNKNOWN"
            elif report["physical_status"]=="UNDETERMINED":
                basis="UNDETERMINED_PHYSICAL_INPUT"
            elif any(c["origin"]=="COMPUTED_EFFECT_CONSTRAINT"
                     and c["status"]=="UNKNOWN" for c in evidence):
                basis="COMPUTED_EFFECT_UNKNOWN"
            else:
                raise ValueError("unclassified non-eligible finite social case: "+key)
            totals["primary_noneligible_basis"][basis] = (
                totals["primary_noneligible_basis"].get(basis,0)+1
            )
        totals["details"].append({
            "case_id":key,
            "admission":report["admission"],
            "physical_status":report["physical_status"],
            "primary_basis":basis,
            "unresolved_or_failed_conditions":[
                c for c in evidence if c["status"] in ("UNKNOWN","FAILED")
            ],
        })
    totals["details"].sort(key=lambda item:item["case_id"])
    totals["primary_noneligible_basis"]=dict(sorted(totals["primary_noneligible_basis"].items()))
    return totals


def run(model: str = "both") -> dict:
    if model not in ("social", "agentic", "native-social", "native-agentic", "both"):
        raise ValueError("unknown model selector")
    social_json = (HERE / SOCIAL).read_bytes()
    native_json = (HERE / NATIVE).read_bytes()
    first = json.loads(social_json)
    native = json.loads(native_json)
    candidates = []
    if model in ("social", "both"):
        candidates.extend(first["cases"])
    if model in ("native-social", "both"):
        candidates.extend(x for x in native["cases"] if x["model"] == "SOCIAL_SOURCE_44")
    if model in ("agentic", "native-agentic", "both"):
        candidates.extend(x for x in native["cases"] if x["model"] == "AGENTIC_SOURCE_57")
    if not candidates:
        raise ValueError("no cases selected")
    results = run_manifest({"schema": first["schema"], "cases": candidates},
                           operators=native_operators())
    results["source_manifests_sha256"] = {
        SOCIAL: sha256(social_json).hexdigest(),
        NATIVE: sha256(native_json).hexdigest(),
    }
    results["source_native_files_unchanged"] = True
    results["social_constraint_evidence_origin"] = evidence_origin_accounting(
        candidates, results["cases"])
    results["experiment_types"] = {
        "SOCIAL_FINITE": "original social cases with finite scenario operators",
        "SOCIAL_SOURCE_44": "actual PR44 source-native intrinsic A/B/C/D",
        "AGENTIC_SOURCE_57": "actual PR57 source-native six-arm reducer",
    }
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", choices=("social", "agentic", "native-social", "native-agentic", "both"), default="both")
    parser.add_argument("--compact", action="store_true",
                        help="only audited counts, manifests and case status, no large private referee traces")
    args = parser.parse_args()
    report = run(args.model)
    if args.compact:
        report["cases"] = [
            {k: row[k] for k in ("case_id", "model", "physical_status", "admission",
                                  "case_sha256", "source_refs", "dimension_states")}
            for row in report["cases"]
        ]
    print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
