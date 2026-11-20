"""Independent source-meaning concordance with G-03 source owner PR #68.

Executes PR68's 40 ORIGINAL_EXPERIMENTS against PR68's own unmodified
dimension_experiment. Separately executes PR69's fourteen action sequences.
Checks only the *same source-visible property* where questions coincide.
Never declares the two experiment models, objectives or scopes equivalent.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path
import sys

from mechanistic_replay import run_manifest as run_operations

HERE=Path(__file__).resolve().parent
MODEL = "ACC-PR68-PR69-OWNER-CONCORDANCE-v0.1"


def _load_source(path: Path):
    spec = spec_from_file_location("_acc_owner68_dimension_source", path)
    if spec is None or spec.loader is None:
        raise FileNotFoundError("missing PR68 source-owned social evaluator")
    mod = module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def _check(condition, desc):
    if not condition:
        raise AssertionError("source meaning deviated: "+desc)


def _frac(x):
    return Fraction(str(x))


def run(source_dir: Path):
    src=source_dir/"dimension_experiment.py"
    registry=source_dir/"ORIGINAL_EXPERIMENTS.json"
    owner=_load_source(src)
    source=json.loads(registry.read_text(encoding="utf-8"))
    owner_report=owner.run_manifest(source)
    ours=json.loads((HERE/"MECHANISM_CASES.json").read_text(encoding="utf-8"))
    generated=run_operations(ours)
    if owner_report["case_count"] != 40 or generated["case_count"] != 14:
        raise AssertionError("versioned source and acceptance populations changed")
    s={row["case_id"]:row for row in owner_report["cases"]}
    o={row["case_id"]:row for row in generated["cases"]}

    def p(case, name=None):
        rows=o[case]["probes"]
        return next((x for x in rows if x["probe"]==name), rows[0])

    proofs={}
    # Fruit source states are independent per-case calculations in PR68;
    # PR69 generates them in ONE sequential history from material operations.
    s0,s1,s2=s["BANANA-S0"],s["BANANA-S1"],s["BANANA-S2-UNVERIFIED"]
    toy=s1["physical_outcome"]["hypothetical_welfare"]["holder"]
    a=p("EX-BAN-04","S0_S1_S2_conditional")
    _check(s0["physical_outcome"]["available"]==0 and
           s1["physical_outcome"]["available"]==2 and
           s1["physical_outcome"]["received"]["holder"]==1 and
           s1["physical_outcome"]["wasted"]==1 and
           s2["physical_outcome"]["received"]["child"]==1 and
           s2["physical_outcome"]["wasted"]==0,
           "banana counts in source owner")
    _check(all(_frac(toy[k])==v for k,v in {"B":5,"F":7,"W":-2}.items()),
           "source-stipulated banana B/F/W")
    _check(a["steps"][0]["candidate_after"]==
           {"child":"0","holder":"1","produced":"2","waste":"1"} and
           a["candidate_facts"]=={"child":"1","holder":"1","produced":"2","waste":"0"} and
           s2["admission"]=="UNDETERMINED" and a["admissibility"]=="UNKNOWN",
           "banana sequence, physical outcome, and permission")
    proofs["EX-BAN-04"]="MATCHED_CONSERVATION_S1_WELFARE_TOY_S2_UNRESOLVED"

    bt=s["BANANA-EXTRA-TRANSPORT"]
    a=p("EX-BAN-02")
    _check(_frac(bt["physical_outcome"]["avoided_item_km"])<0 and
           bt["admission"]=="UNDETERMINED" and a["candidate_facts"]["received"]=="1" and
           a["candidate_stages"][0]["comparison"]["status"]=="TRADEOFF",
           "additional transport hurts E, helps R (transport inputs differ)")
    proofs["EX-BAN-02"]="SAME_DIRECTION_ONLY_DIFFERENT_DECLARED_TRANSPORT_UNITS"

    local=s["BANANA-LOCAL-UNVERIFIED"]
    a=p("EX-BAN-01")
    _check(_frac(local["physical_outcome"]["avoided_item_km"])==14000 and
           local["admission"]=="UNDETERMINED" and
           a["candidate_facts"]["route_km"]=="0" and
           a["candidate_facts"]["local_consumed"]=="1" and
           a["admissibility"]=="UNKNOWN", "local banana and unresolved authority")
    proofs["EX-BAN-01"]="SAME_DECLARED_SINGLE_UNIT_DISTANCE_AND_UNVERIFIED_ROUTE"

    dana=s["DONATION-ATTRIBUTION-VETO"]
    a=p("EX-BAN-03","attribution_refusal")
    _check(dana["admission"]=="BLOCKED_BY_CONDITION" and
           _frac(dana["physical_outcome"]["hypothetical_welfare"]["donor"]["B"])>0 and
           a["admissibility"]=="FAIL" and
           a["candidate_facts"]["aid"]=="1" and
           {g["category"]:g["status"] for g in
             next(x for x in ours["cases"] if x["case_id"]=="EX-BAN-03")["actions"][0]["guards"]} ==
           {"consent":"PASS","recognition":"FAIL"},
           "DANA donor can gain directly and still refuse relative attribution")
    proofs["EX-BAN-03"]="MATCHED_DIRECT_GAIN_CONSENT_SEPARATE_ATTRIBUTION_VETO"

    friday=s["FRIDAY-RELATIVE-VETO"]
    a=p("EX-ROBIN-01")
    shares=friday["physical_outcome"]["relative_shares"]
    _check(friday["admission"]=="BLOCKED_BY_CONDITION" and
           shares["Friday"]["coconut"]=="1/1000" and
           shares["Friday"]["fish"]=="1/1000" and
           shares["Robinson"]["coconut"]=="999/1000" and
           a["candidate_facts"]["v_coco"]=="1" and
           a["candidate_facts"]["r_coco"]=="999" and
           a["admissibility"]=="FAIL", "positive Friday gain yet relative objection")
    proofs["EX-ROBIN-01"]="MATCHED_CONSERVED_1_999_AND_RELATIVE_VETO"

    fail=s["CREDIT-7-4"];pass_=s["CREDIT-7-3"]
    a=p("EX-CREDIT-01")
    _check(fail["admission"]=="MATERIALLY_INFEASIBLE" and
           pass_["admission"]=="ELIGIBLE_UNDER_DECLARED_CONDITIONS" and
           a["steps"][0]["technical"]=="FAIL" and
           a["initial_facts"]=={"share_a":"7","share_b":"3"},
           "credit 7+4 budget10")
    proofs["EX-CREDIT-01"]="MATCHED_JOINT_CAPACITY_INFEASIBILITY"

    apple=s["APPLES-BRIDGE-UNKNOWN"]
    neg=p("EX-APPLE-01","local_extra_apple_rejected")
    jump=p("EX-APPLE-01","hypothetical_joint_jump")
    _check(apple["physical_outcome"]["local_choice"]==3 and
           apple["physical_outcome"]["global_best"]==8 and
           apple["admission"]=="UNDETERMINED" and
           neg["candidate_facts"]["utility"]=="7" and
           neg["admissibility"]=="FAIL" and
           jump["candidate_facts"]["utility"]=="10",
           "apple valley and conditional positive joint control")
    proofs["EX-APPLE-01"]="MATCHED_UTILITY_VALLEY_JOINT_BRIDGE_IS_ADDITIONAL_TOY"

    m=s["MINISTRIES-700-TO-2-UNVERIFIED"]
    a=p("EX-MIN-01")
    _check(_frac(m["physical_outcome"]["periods"][0]["resource_gap"])==698 and
           m["admission"]=="UNDETERMINED" and
           a["candidate_facts"]["applications"]=="2" and
           a["admissibility"]=="UNKNOWN", "ministries 700→2 conditional")
    proofs["EX-MIN-01"]="MATCHED_ILLUSTRATIVE_APPLICATION_COUNT_NOT_RESOURCE_COST_PROOF"

    iq=s["IQ03-GAP-GROWS"]
    _check([_frac(z["resource_gap"]) for z in iq["physical_outcome"]["periods"]]==
           [Fraction(20),Fraction(45)], "IQ03 numerical source example")
    proofs["IQ03_SOURCE_ILLUSTRATION"]="SOURCE_OWNER_EXACT_MATCH_NOT_ALTERNATIVE_FEASIBILITY_PROOF"

    orange=s["ORANGES-WITHOUT-QUANTITY"]
    lycee=s["LYCEE-GOAL-UNOBSERVED"]
    _check(orange["admission"]=="UNDETERMINED" and
           lycee["admission"]=="UNDETERMINED" and
           p("EX-ORANGE-01")["admissibility"]=="UNKNOWN" and
           p("EX-HUMAN-01")["admissibility"]=="UNKNOWN",
           "unobserved orange and lycee")
    proofs["EX-ORANGE-01"]="MATCHED_UNKNOWN_NOT_FABRICATED_SOCIAL_FACT"
    proofs["EX-HUMAN-01"]="MATCHED_UNKNOWN_NOT_FABRICATED_HUMAN_DATA"

    owner_unmatched=("EX-SOLIDAR-01","EX-LINEAR-01","EX-SUPER-01","EX-BUSINESS-01")
    _check(all(name in o for name in owner_unmatched),
           "other author examples still independently executable")
    return {
        "schema":MODEL,
        "source_owner":"PR68_CONSCIENTIA_DIMENSION_EXPERIMENT",
        "source_sha256": {"dimension_experiment.py":sha256(src.read_bytes()).hexdigest(),
                          "ORIGINAL_EXPERIMENTS.json":sha256(registry.read_bytes()).hexdigest()},
        "source_owner_case_count":owner_report["case_count"],
        "operation_sequence_case_count":generated["case_count"],
        "shared_source_property_checks":proofs,
        "other_author_cases_retained_as_distinct_questions":list(owner_unmatched),
        "unrun_semantic_equivalences":"NO_CLAIM_THAT_DIFFERENT_EXPERIMENT_OPERATORS_OR_ACTOR_OBJECTIVES_ARE_IDENTICAL",
        "no_automatic_EA_THEORY_CHANGE":True,
    }


def main(argv=None):
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source-dir",type=Path,required=True)
    ap.add_argument("--output",type=Path)
    a=ap.parse_args(argv)
    data=json.dumps(run(a.source_dir),ensure_ascii=False,sort_keys=True,indent=2)+"\n"
    if a.output:
        a.output.write_text(data,encoding="utf-8")
    else:
        print(data,end="")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
