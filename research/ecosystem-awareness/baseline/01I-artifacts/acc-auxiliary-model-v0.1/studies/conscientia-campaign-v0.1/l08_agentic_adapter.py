"""L08 independent agentic-source adapter: reuse Pareto without merging objectives.

The original PR57 agentic reducer remains the sole authority for mission output,
plan costs, physical conservation, and post-hoc technical gaps. This module
only *observes* its six policy outcomes for each one-question source case, and
uses the same pure, source-agnostic vector ordering that L08 uses on the
Conscientia source-domain experiments.

DO NOT interpret agentic "technical optimal" as legally feasible, accessible
or proof of actual vendor behavior. No aggregate cross-case utility.
"""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import argparse
import json
import sys

from l08_robustness import pareto

HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/"agentic-ecosystem-reduction-v0.1"


def _load_native(path:Path):
    spec=spec_from_file_location("_acc_l08_agentic_native_immutable",path)
    if spec is None or spec.loader is None:
        raise FileNotFoundError("native agentic source file missing")
    obj=module_from_spec(spec)
    sys.modules[spec.name]=obj
    spec.loader.exec_module(obj)
    return obj


def run(source_folder:Path=SOURCE)->dict:
    source=source_folder/"agentic_reduction.py"
    manifest=source_folder/"CASES.json"
    agentic=_load_native(source)
    fixture=json.loads(manifest.read_text(encoding="utf-8"))
    if fixture.get("schema")!=agentic.SCHEMA:
        raise ValueError("native agentic case schema mismatch")
    cases=fixture["cases"]
    ids=[x["id"] for x in cases]
    if len(set(ids))!=len(ids):
        raise ValueError("duplicate agentic case IDs")
    by_case=[]
    membership={arm:0 for arm in agentic.ARMS}
    for case in cases:
        result=agentic.run_case(case)
        if result["id"]!=case["id"]:
            raise AssertionError("source-native case identity changed")
        if set(result["arms"])!=set(agentic.ARMS):
            raise AssertionError("source-native six policy contract changed")
        arms={}
        points={}
        public=result["public_A"]
        for name,row in result["arms"].items():
            plan=row["plan"]
            result_only=row["observed_by_referee_only"]
            if result_only["total_resources_same"]!=public["total_resources"]:
                raise AssertionError("source changed physical total resources")
            if row["residual_C_D_exhaustiveness"]!="NOT_CLOSED":
                raise AssertionError("source declared a universal closure")
            if row["experience_of_suffering"]!="NOT_MEASURED_NOT_ATTRIBUTED_TO_AI":
                raise AssertionError("agentic welfare was silently invented")
            gap=Fraction(str(row["mission_output_gap_to_same_budget_technical_optimum"]))
            cost=Fraction(str(plan["instrument_cost"]))
            if gap<0 or cost<0:
                raise ValueError("negative mission gap or instrument price")
            points[name]=(gap,cost)
            arms[name]={
                "native_public_decision_status":plan["status"],
                "native_transfer":plan["transfer"],
                "mission_output_referee_only":result_only["output"],
                "technical_gap_referee_only":str(gap),
                "instrument_price_assumption":str(cost),
                "mission_target_met_PRIVATE_referee_only":result_only["mission_target_met"],
                "resource_total_conserved":True,
                "no_subjective_suffering_claim":True,
            }
        front=pareto(points,axes=("same_case_technical_mission_gap",
                                 "source_owned_information_price"))
        for arm in front:
            membership[arm]+=1
        by_case.append({
            "case_id":result["id"],
            "source_document_ids":result["source_ids"],
            "public_question":"mission_output_vs_same_budget_candidate_under_source_declared_A",
            "public_mission_target":public["mission_target"],
            "horizon":"ONE_SOURCE_DECLARED_PR57_DECISION",
            "policy_arms":arms,
            "two_axis_nonfungible_front_referee_only":front,
            "not_an_agentic_exclusive_differential":True,
            "cannot_compare_with_social_banana_utility":True,
        })
    return {
        "schema":"ACC-L08-SOURCE-AGENTIC-PARETO-ADAPTER-v0.1",
        "source_ownership":"PR57.agentic_reduction.py",
        "source_sha256":{
            "agentic_reduction.py":sha256(source.read_bytes()).hexdigest(),
            "CASES.json":sha256(manifest.read_bytes()).hexdigest(),
        },
        "source_native_cases":len(cases),
        "policy_decisions_replayed":len(cases)*len(agentic.ARMS),
        "source_policies_unchanged":list(agentic.ARMS),
        "pareto_dimensions_kept_separate":[
            "source_native_private_referee_mission_gap",
            "source_declared_instrument_cost",
        ],
        "nonfungible_front_memberships_not_aggregate_winner_rates":
            dict(sorted(membership.items())),
        "cases":by_case,
        "interpretation":"POST_HOC_WITHIN_CASE_ONLY; DIFFERENT_QUESTION_THAN_SOCIAL_G04; NO_EMPIRICAL_AI_OR_HUMAN_DATA; C_D_NOT_CLOSED",
    }


def main(argv=None)->int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-folder",type=Path,default=SOURCE)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args(argv)
    report=run(args.source_folder)
    content=json.dumps(report,indent=2,ensure_ascii=False,sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(content,encoding="utf-8")
    else:
        print(content,end="")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
