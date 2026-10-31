"""G-02: source-owned, fallible independent audit observation (synthetic only).

The original five campaign arms and 60 frozen cases remain unchanged.
The original Q.independent_audit Boolean is used ONLY in the explicitly
separated legacy diagnostic; it never enters the new public policies.
Hidden true adjudications are known ONLY to the synthetic signal generator and
post-hoc scorer. Distinct issuer metadata is not proof of real independence.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import argparse
import json
from typing import Any, Mapping

import campaign

HERE=Path(__file__).resolve().parent
CLOCK=10
SCHEMA="ACC-G02-OBSERVATION-AUDIT-v0.1"
ARMS=("A_ONLY","Q_UNAUDITED_SOURCE","Q_WITH_AUDIT_OBSERVATION",
      "CONVENTIONAL_INDEPENDENT_MEASURED","BOTH_INDEPENDENT_EVIDENCE")
TRUTH=("ALLOW","BLOCK")
PROB_KEYS=("audit_availability","audit_authenticity","audit_scope_match",
           "audit_freshness","audit_detects_false_claim",
           "audit_false_alarm_on_true_claim","direct_availability",
           "direct_authenticity","direct_scope_match","direct_freshness",
           "direct_observation_correct")
PRICE_KEYS=("independent_audit","conventional_measurement")


def rat(raw: Any, name: str, *, probability: bool=False)->Fraction:
    if raw is None or type(raw) is bool:
        raise ValueError("invalid "+name)
    try:
        if isinstance(raw,float):
            if raw != raw or raw in (float("inf"),float("-inf")):
                raise ValueError("nonfinite")
            value=Fraction(str(raw))
        elif isinstance(raw,(int,Fraction,str)):
            value=Fraction(raw)
        else:
            raise ValueError("unsupported rational")
    except (ValueError,TypeError,ZeroDivisionError,OverflowError) as exc:
        raise ValueError("invalid "+name) from exc
    if value < 0 or probability and value > 1:
        raise ValueError("outside allowed range "+name)
    return value


def draw(seed:str,case_id:str,n:int,channel:str,p:Fraction)->bool:
    if not 0<=p<=1:
        raise ValueError("probability outside [0,1]")
    h=sha256(f"{seed}|{case_id}|{n}|{channel}".encode("utf-8")).digest()
    return Fraction(int.from_bytes(h[:8],"big"),2**64)<p


def public_Q(case:Mapping[str,Any])->dict:
    """Never pass CURRENT_BUT_FALSE or the legacy audit flag to new plans."""
    source=case["Q"]
    label=("CURRENT" if source["status"] in ("CURRENT_VALID","CURRENT_BUT_FALSE")
           else "STALE" if source["status"]=="STALE" else "OPEN")
    return {
        "kind":source["kind"],"source_label":label,
        "claimed_action":source["verdict"],"fresh":source["fresh"],
        "scope_id":source["scope_id"],"issuer_id":source["source_id"],
        "source_provenance_metadata":source["provenance_established"],
        "acquisition_cost":str(rat(source["cost"],"source_cost")),
    }


def q_can_be_used(public:Mapping[str,Any],q:Mapping[str,Any])->bool:
    return (q["kind"]=="B" and q["source_label"]=="CURRENT"
            and q["fresh"] is True and q["scope_id"]==public["scope_id"]
            and q["source_provenance_metadata"] is True
            and q["claimed_action"] in TRUTH)


def source_q_adapter(q:Mapping[str,Any])->dict:
    """Adapter to the unchanged original source campaign's QUALIFIED_Q."""
    return {
        "kind":q["kind"],"status":("CURRENT_VALID" if q["source_label"]=="CURRENT"
                        else "STALE" if q["source_label"]=="STALE"
                        else "UNEVALUABLE"),
        "verdict":q["claimed_action"],"fresh":q["fresh"],
        "scope_id":q["scope_id"],
        "provenance_established":q["source_provenance_metadata"],
        "cost":float(rat(q["acquisition_cost"],"q_cost")),
    }


def observation(role:str, value:str, *,
                available:bool, signed:bool, scoped:bool, fresh:bool,
                issuer:str, scope:str)->dict:
    if role not in ("AUDITOR","CONVENTIONAL"):
        raise ValueError("unsupported instrument")
    return {
        "role":role,"value":value,"available":available,
        "issuer_id":issuer,"signed_TOY":signed,
        "scope_id":scope if scoped else "OTHER_QUESTION",
        "observed_at":CLOCK-1 if fresh else CLOCK-9,"ttl":3,
        "attestation_is_not_a_real_independence_proof":True,
    }


def qualified(item:Mapping[str,Any],q:Mapping[str,Any],
              public:Mapping[str,Any],role:str)->bool:
    """Declared origin, freshness, scope and separate issuer; NOT truth."""
    return (item["role"]==role and item["available"] is True
            and item["signed_TOY"] is True
            and item["scope_id"]==public["scope_id"]
            and item["issuer_id"] not in ("",None,q["issuer_id"])
            and type(item["observed_at"]) is int
            and type(item["ttl"]) is int and item["ttl"]>0
            and item["observed_at"]<=CLOCK<item["observed_at"]+item["ttl"])


def generate(case:Mapping[str,Any],params:Mapping[str,Any],
             *,seed:str,replicate:int)->dict:
    """Synthetic environment derives noisy observations from the frozen truth.

    The private truth is NOT passed to plan_public. A case with open C/D is
    never sampled as if it had an adjudicable unknown-but-finite oracle.
    """
    q=public_Q(case)
    truth=case["truth_private_for_scoring"]
    if truth not in (*TRUTH,"NOT_ADJUDICABLE"):
        raise ValueError("unrecognized private referee truth")
    if q["kind"] in ("C","D") and truth!="NOT_ADJUDICABLE":
        raise ValueError("cannot assign closed ground truth to open C/D")
    p={k:rat(params[k],k,probability=True) for k in PROB_KEYS}
    cid=case["case_id"]
    def sample(name):
        return draw(seed,cid,replicate,name,p[name])
    possible=(q["kind"]=="B" and q["source_label"]=="CURRENT"
              and truth in TRUTH)
    match=(q["claimed_action"]==truth) if possible else None
    if possible:
        flagged=sample("audit_false_alarm_on_true_claim") if match else sample("audit_detects_false_claim")
        evidence="CONTRADICTION" if flagged else "SUPPORT"
    else:
        evidence="INCONCLUSIVE"
    observed=(truth if sample("direct_observation_correct") else
              "BLOCK" if truth=="ALLOW" else "ALLOW") if truth in TRUTH else "INCONCLUSIVE"
    audit=observation(
        "AUDITOR",evidence,available=sample("audit_availability"),
        signed=sample("audit_authenticity"),
        scoped=sample("audit_scope_match"),fresh=sample("audit_freshness"),
        issuer="INDEPENDENT_AUDITOR_TOY",scope=case["public"]["scope_id"])
    direct=observation(
        "CONVENTIONAL",observed,available=sample("direct_availability"),
        signed=sample("direct_authenticity"),
        scoped=sample("direct_scope_match"),fresh=sample("direct_freshness"),
        issuer="INDEPENDENT_DIRECT_TOY",scope=case["public"]["scope_id"])
    return {
        "public":dict(case["public"]),"q":q,"audit":audit,"direct":direct,
        "truth_PRIVATE_FOR_REFEREE_ONLY":truth,
        "private_Q_claim_matched":match,
        "utility_PRIVATE_FOR_REFEREE_ONLY":dict(case["utility"]),
        "source_case_id":cid,"source_variant":case["variant"],
        "legacy_audit_flag_DIAGNOSTIC_ONLY":case["Q"]["independent_audit"],
    }


def plan_public(public:Mapping[str,Any],q:Mapping[str,Any],
                audit:Mapping[str,Any],direct:Mapping[str,Any],
                prices:Mapping[str,Any],arm:str)->dict:
    """Public side takes no truth, variant, source case ID or legacy audit flag."""
    if arm not in ARMS:
        raise ValueError("unknown public arm")
    if not isinstance(prices,dict) or set(prices)!=set(PRICE_KEYS):
        raise ValueError("invalid audit/conventional price contract")
    px={k:rat(prices[k],k) for k in PRICE_KEYS}
    adapter=source_q_adapter(q)
    if arm=="A_ONLY":
        base=campaign.public_policy(dict(public),adapter,None,None,"A_ONLY")
        return {**base,"arm":arm,"consulted":{},"new_audit_evidence_used":False}
    if arm=="Q_UNAUDITED_SOURCE":
        old=campaign.public_policy(dict(public),adapter,None,None,"QUALIFIED_Q")
        return {**old,"arm":arm,"consulted":{"Q_SOURCE":q["acquisition_cost"]},
                "new_audit_evidence_used":False}
    usable=q_can_be_used(public,q)
    a_requested=usable and arm in ("Q_WITH_AUDIT_OBSERVATION","BOTH_INDEPENDENT_EVIDENCE")
    d_requested=arm=="CONVENTIONAL_INDEPENDENT_MEASURED" or (
        usable and arm=="BOTH_INDEPENDENT_EVIDENCE")
    a_valid=qualified(audit,q,public,"AUDITOR") if a_requested else False
    d_valid=qualified(direct,q,public,"CONVENTIONAL") if d_requested else False
    use={}
    if arm in ("Q_WITH_AUDIT_OBSERVATION","BOTH_INDEPENDENT_EVIDENCE"):
        use["Q_SOURCE"]=q["acquisition_cost"]
    if a_requested:
        use["INDEPENDENT_AUDIT"]=str(px["independent_audit"])
    if d_requested:
        use["INDEPENDENT_DIRECT"]=str(px["conventional_measurement"])
    action=public["baseline_action"]
    reason="PUBLIC_A_BASELINE"
    if arm=="Q_WITH_AUDIT_OBSERVATION":
        if not usable:
            reason="CURRENT_SCOPED_B_NOT_AVAILABLE"
        elif not a_valid:
            action="REVIEW"
            reason="INDEPENDENT_AUDIT_NOT_QUALIFIED"
        elif audit["value"]=="SUPPORT":
            action=q["claimed_action"]
            reason="FALLIBLE_AUDIT_SUPPORTS_Q"
        else:
            action="REVIEW"
            reason=("FALLIBLE_AUDIT_CONTRADICTS_Q" if audit["value"]=="CONTRADICTION"
                    else "FALLIBLE_AUDIT_INCONCLUSIVE")
    elif arm=="CONVENTIONAL_INDEPENDENT_MEASURED":
        if d_valid and direct["value"] in TRUTH:
            action=direct["value"]
            reason="MEASURED_CONVENTIONAL_VERDICT"
        else:
            action="REVIEW"
            reason="NO_QUALIFIED_CONVENTIONAL_VERDICT"
    elif arm=="BOTH_INDEPENDENT_EVIDENCE":
        if not usable:
            reason="CURRENT_SCOPED_B_NOT_AVAILABLE"
        elif (a_valid and d_valid and audit["value"]=="SUPPORT"
              and direct["value"]==q["claimed_action"]):
            action=q["claimed_action"]
            reason="TWO_INDEPENDENT_OBSERVATIONS_AGREE_ON_Q"
        else:
            action="REVIEW"
            reason="CONTRADICTORY_OR_INSUFFICIENT_EVIDENCE"
    if action not in ("ALLOW","BLOCK","REVIEW"):
        raise ValueError("public planner emitted invalid verdict")
    cost=sum((rat(x,k) for k,x in use.items()),Fraction(0))
    return {
        "action":action,"arm":arm,"evidence_mode":reason,
        "acquisition_cost_synthetic":round(float(cost),4),
        "consulted":dict(sorted(use.items())),
        "qualified_audit_consumed":a_valid,
        "qualified_direct_consumed":d_valid,
        "public_truth_and_historical_flag_not_accessible":True,
        "evidence_independence_NOT_observed_in_the_field":True,
    }


def evaluate(env:Mapping[str,Any],prices:Mapping[str,Any])->dict:
    """All five public plans are frozen BEFORE the source native post-hoc scorer."""
    plans={arm:plan_public(env["public"],env["q"],env["audit"],env["direct"],prices,arm)
           for arm in ARMS}
    truth=env["truth_PRIVATE_FOR_REFEREE_ONLY"]
    scores={arm:campaign.score_private(plans[arm],truth,
                                      env["utility_PRIVATE_FOR_REFEREE_ONLY"])
            for arm in ARMS}
    return {
        "case_id":env["source_case_id"],"variant":env["source_variant"],
        "truth_PRIVATE_ONLY":truth,"q_claim_match_PRIVATE_ONLY":env["private_Q_claim_matched"],
        "public_A":env["public"],"public_Q":env["q"],
        "audit_public_signal":env["audit"],"direct_public_signal":env["direct"],
        "historical_boolean_DIAGNOSTIC_ONLY":env["legacy_audit_flag_DIAGNOSTIC_ONLY"],
        "arms":scores,
    }


def original_flag_baseline(cases:Mapping[str,Any])->dict:
    """Separate legacy artifact, never a competing evidence-driven policy."""
    old=campaign.run_decisions(dict(cases))
    if old["case_count"]!=len(cases["cases"]) or (
       "PARTIAL_Q_AUDIT_GATED" not in old["totals"]):
        raise AssertionError("original campaign source contract changed")
    return {
        "cases":old["case_count"],"source_arms":old["arm_count"],
        "source_decisions":old["arm_decisions"],
        "legacy_flag_arm_wrong":old["totals"]["PARTIAL_Q_AUDIT_GATED"]["wrong"],
        "ordinary_Q_wrong":old["totals"]["QUALIFIED_Q"]["wrong"],
        "false_Q_with_declared_boolean":sum(
            c["variant"]=="FALSE_Q" and c["Q"]["independent_audit"]
            for c in cases["cases"]),
        "flag_is_not_independent_audit_measurement":True,
    }


def summarize(rows:list[dict],regime_id:str)->dict:
    if not rows:
        raise ValueError("no source cases to score")
    summary={}
    for arm in ARMS:
        scored=[x["arms"][arm] for x in rows
                if x["truth_PRIVATE_ONLY"] in TRUTH]
        all_scores=[x["arms"][arm] for x in rows]
        wrong=sum(x["correctness"]=="WRONG" for x in scored)
        unresolved=sum(x["correctness"]=="UNRESOLVED" for x in scored)
        correct=sum(x["correctness"]=="CORRECT" for x in scored)
        if wrong+correct+unresolved!=len(scored):
            raise AssertionError("source scoring incomplete")
        consultations=Counter()
        for item in all_scores:
            consultations.update(item.get("consulted",{}).keys())
        summary[arm]={
            "correct":correct,"wrong":wrong,"unresolved":unresolved,
            "false_allow":sum(x["false_allow"] for x in scored),
            "false_block":sum(x["false_block"] for x in scored),
            "missed_justified_allows":sum(
                x["truth_PRIVATE_ONLY"]=="ALLOW" and x["arms"][arm]["action"]!="ALLOW"
                for x in rows),
            "adjudicable_count":len(scored),
            "open_unscored_count":len(rows)-len(scored),
            "total_synthetic_instrument_cost":str(sum(
                (rat(x["acquisition_cost_synthetic"],"price") for x in all_scores),
                Fraction(0))),
            "consultations_by_type":dict(sorted(consultations.items())),
            "not_a_real_utility_or_error_rate":True,
        }
    detector=Counter()
    for row in rows:
        if row["variant"]=="FALSE_Q":
            v=row["audit_public_signal"]["value"]
            detector["raw_"+v]+=1
            if row["arms"]["Q_WITH_AUDIT_OBSERVATION"]["qualified_audit_consumed"]:
                detector["qualified_audit_used_in_decision"]+=1
    return {
        "regime":regime_id,"count_source_case_observations":len(rows),
        "source_variant_counts":dict(sorted(Counter(x["variant"] for x in rows).items())),
        "new_policy_outcomes":summary,
        "false_Q_audit_signal_diagnostics":dict(sorted(detector.items())),
        "source_audit_boolean_not_used_for_new_policies":True,
        "no_empirical_independence_claim":True,
    }


def validate(manifest:Mapping[str,Any])->None:
    if manifest.get("schema")!=SCHEMA:
        raise ValueError("wrong G02 protocol schema")
    seed=manifest.get("seed")
    if not isinstance(seed,str) or not seed or len(seed)>96:
        raise ValueError("bounded nonempty common seed required")
    reps=manifest.get("replicates_per_case")
    if type(reps) is not int or not 8<=reps<=256:
        raise ValueError("repetitions out of bounds")
    regimes=manifest.get("regimes")
    if not isinstance(regimes,list) or not 2<=len(regimes)<=12:
        raise ValueError("two to twelve regimes required")
    ids=[]
    for row in regimes:
        if not isinstance(row,dict) or not isinstance(row.get("id"),str) or not row["id"]:
            raise ValueError("regime identifier required")
        ids.append(row["id"])
        params=row.get("parameters")
        price=row.get("prices")
        if not isinstance(params,dict) or set(params)!=set(PROB_KEYS):
            raise ValueError("unrecognized audit reliability contract")
        if not isinstance(price,dict) or set(price)!=set(PRICE_KEYS):
            raise ValueError("unrecognized instrument price contract")
        for key,v in params.items():
            rat(v,key,probability=True)
        for key,v in price.items():
            rat(v,key)
    if len(ids)!=len(set(ids)):
        raise ValueError("duplicate regime")


def run(manifest:Mapping[str,Any], *, traces:bool=False)->dict:
    validate(manifest)
    registry=campaign.read_json("CASE_REGISTRY.json")
    campaign.validate_cases(campaign.read_json("SOURCE_REGISTER.json"),registry)
    baseline=original_flag_baseline(registry)
    outputs=[]
    for regime in manifest["regimes"]:
        rows=[]
        evidence=[]
        for case in registry["cases"]:
            for n in range(manifest["replicates_per_case"]):
                row=evaluate(generate(case,regime["parameters"],seed=manifest["seed"],
                                      replicate=n),regime["prices"])
                rows.append(row)
                if traces and n==0 and case["variant"] in ("FALSE_Q","VALID_BLOCK","OPEN_RESIDUAL"):
                    evidence.append(row)
        group=summarize(rows,regime["id"])
        group["declared_parameters"]={k:str(v) for k,v in regime["parameters"].items()}
        group["declared_instrument_prices"]={k:str(v) for k,v in regime["prices"].items()}
        if traces:
            group["private_referee_sample_traces_NOT_PUBLIC_PLANNER_INPUT"]=evidence
        outputs.append(group)
    return {
        "schema":SCHEMA,
        "source_sha256":{
            name:sha256((HERE/name).read_bytes()).hexdigest()
            for name in ("campaign.py","CASE_REGISTRY.json","SOURCE_REGISTER.json")
        },
        "manifest_sha256":sha256(json.dumps(manifest,sort_keys=True,
                separators=(",",":")).encode("utf-8")).hexdigest(),
        "historical_flag_baseline_UNCHANGED":baseline,
        "original_source_cases":len(registry["cases"]),
        "replicates_per_case":manifest["replicates_per_case"],
        "total_paired_cases":len(registry["cases"])*manifest["replicates_per_case"]*len(outputs),
        "public_policy_arms":list(ARMS),
        "regimes":outputs,
        "interpretation":"FINITE_SYNTHETIC_AUDIT_SIGNAL_NOT_FIELD_OBSERVATION; OPEN_C_D_UNSCORED; CAUSAL_FH_C_NOT_PROVEN",
        "original_cases_and_source_code_not_rewritten":True,
    }


def main(argv=None)->int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest",type=Path,default=HERE/"G02_AUDIT_PROTOCOL.json")
    parser.add_argument("--traces",action="store_true")
    parser.add_argument("--output",type=Path)
    args=parser.parse_args(argv)
    obj=run(json.loads(args.manifest.read_text(encoding="utf-8")),
            traces=args.traces)
    text=json.dumps(obj,ensure_ascii=False,sort_keys=True,indent=2)+"\n"
    if args.output:
        args.output.write_text(text,encoding="utf-8")
    else:
        print(text,end="")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
