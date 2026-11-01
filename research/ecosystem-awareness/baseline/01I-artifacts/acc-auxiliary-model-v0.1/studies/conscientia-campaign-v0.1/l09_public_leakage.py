"""L-09: finite paired worlds that remove accidental public-label leakage.

This module retains every original G02 source file and source experiment.
It creates *derived, explicitly counterfactual* valid/false B questions with
equal public A, source Q metadata, issuer, scope, baseline, and pre-read
instrument metadata. The same synthetic world can differ in PRIVATE truth
but not in any of those public signals. Acquired audit/direct RESULTS may
legitimately distinguish those worlds after measurement.

The original source fixture is NOT a prevalence sample. Exact finite
conditional information is only over the explicit balanced binary worlds,
never the open epistemic C/D exterior, real people, or real agent behaviour.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from math import log2
from pathlib import Path
import argparse
import json
from typing import Any, Mapping, Sequence

import campaign
import g02_evidence_audit as source

HERE=Path(__file__).resolve().parent
SCHEMA="ACC-L09-MATCHED-PUBLIC-TRUTH-v0.1"
TRUTH=("ALLOW","BLOCK")
BASELINES=("ALLOW","REVIEW")
VARIANTS=("VALID_GO","FALSE_Q")
PRIVATE_ONLY="POST_HOC_REFEREE_ONLY"


def _key(value: Any)->str:
    return json.dumps(value,ensure_ascii=False,sort_keys=True,
                      separators=(",",":"),allow_nan=False)


def explicit_information(records:Sequence[tuple[object,str]])->dict[str,Any]:
    """Count-derived Bayes bound and Shannon bits on FINITE labelled records.

    Every equally weighted record is part of the stipulated synthetic sample.
    The predictor may use the declared public observation, never private
    case labels, truth fields, or the original source fixture row identity.
    """
    if not records:
        raise ValueError("no finite records")
    groups:dict[str,Counter]=defaultdict(Counter)
    marginal=Counter()
    for view,truth in records:
        if truth not in TRUTH:
            raise ValueError("open/unknown truth cannot be silently scored")
        groups[_key(view)][truth]+=1
        marginal[truth]+=1
    n=sum(marginal.values())
    if len(marginal)<2:
        raise ValueError("both source truth alternatives must be present")
    def entropy(counts:Counter)->float:
        total=sum(counts.values())
        return -sum((x/total)*log2(x/total) for x in counts.values() if x)
    prior=entropy(marginal)
    posterior=sum((sum(g.values())/n)*entropy(g) for g in groups.values())
    Bayes=sum(max(g.values()) for g in groups.values())
    return {
        "finite_observations":n,
        "distinct_visible_signatures":len(groups),
        "truth_counts":dict(sorted(marginal.items())),
        "optimal_public_only_accuracy":str(Fraction(Bayes,n)),
        "optimal_public_only_correct":Bayes,
        "prior_truth_entropy_bits":prior,
        "conditional_truth_entropy_bits":posterior,
        "visible_mutual_information_bits":max(0.0,prior-posterior),
        "source":"EXACT_FINITE_COUNTS_WITH_EQUAL_CASE_WEIGHTS",
        "not_a_distribution_over_open_C_D":True,
    }


def _original_pairs(cases:Sequence[Mapping[str,Any]])->list[dict]:
    by_family:dict[str,dict]=defaultdict(dict)
    for row in cases:
        v=row["variant"]
        if v in VARIANTS:
            f=row["family"]
            if v in by_family[f]:
                raise ValueError("duplicate original variant in "+f)
            by_family[f][v]=row
    if not by_family:
        raise ValueError("no finite original true/false pairs")
    pairs=[]
    for family, variants in sorted(by_family.items()):
        if set(variants)!=set(VARIANTS):
            raise ValueError("missing counterfactual Q pair for "+family)
        yes,no=variants["VALID_GO"],variants["FALSE_Q"]
        if (yes["truth_private_for_scoring"],no["truth_private_for_scoring"]) != TRUTH:
            raise ValueError("source truth orientation changed in "+family)
        if yes["Q"]["verdict"]!="ALLOW" or no["Q"]["verdict"]!="ALLOW":
            raise ValueError("both source Q claims must address same action")
        if (yes["public"]["scope_id"]!=no["public"]["scope_id"] or
            yes["public"]["decision_question"]!=no["public"]["decision_question"]):
            raise ValueError("source decision question/rights mismatched")
        if yes["utility"]!=no["utility"]:
            raise ValueError("cannot silently change native source utility")
        yesQ=source.public_Q(yes)
        noQ=source.public_Q(no)
        if yesQ!=noQ:
            raise ValueError("source public Q signals are already different in "+family)
        pairs.append({"family":family,"yes":yes,"no":no})
    return pairs


def original_fixture_metadata_diagnostic(cases:Sequence[Mapping[str,Any]])->dict:
    """Show the actual original 24-case bias before any derived matching."""
    p=_original_pairs(cases)
    records=[]
    for family in p:
        for original in (family["yes"],family["no"]):
            records.append((
                {"public_A":original["public"],
                 "public_Q":source.public_Q(original)},
                original["truth_private_for_scoring"]
            ))
    return explicit_information(records)


def make_public_matched_pairs(cases:Sequence[Mapping[str,Any]],
                              baselines:Sequence[str]=BASELINES)->list[dict]:
    """Counterfactual pair construction, independent of original case names.

    Source original case IDs are kept strictly in provenance fields. The
    derived IDs are identical for both private truth twins, so an accidental
    case-name predictor cannot distinguish them even if that label leaks.
    """
    if not baselines or len(baselines)!=len(set(baselines)):
        raise ValueError("baselines must be nonempty and distinct")
    if any(a not in ("ALLOW","BLOCK","REVIEW") for a in baselines):
        raise ValueError("illegal source baseline")
    pairlist=[]
    for origin in _original_pairs(cases):
        for baseline in baselines:
            group="L09-"+origin["family"]+"-"+baseline
            derived=[]
            for name in ("yes","no"):
                original=origin[name]
                row=deepcopy(original)
                row["case_id"]=group  # identical across counterfactual truth worlds
                row["public"]["baseline_action"]=baseline
                derived.append(row)
            if derived[0]["public"]!=derived[1]["public"]:
                raise ValueError("derived public A differs across twins")
            if source.public_Q(derived[0])!=source.public_Q(derived[1]):
                raise ValueError("derived public Q differs across twins")
            pairlist.append({
                "pair_id":group,
                "source_family":origin["family"],
                "source_rows_PRIVATE_FOR_REVIEWER_ONLY":[
                    origin["yes"]["case_id"],origin["no"]["case_id"]],
                "is_counterfactual_not_modified_frozen_fixture":True,
                "worlds":derived,
            })
    return pairlist


def public_metadata(env:Mapping[str,Any])->dict:
    """All pre-result public details, never the private truth or audit verdict."""
    def evidence_metadata(x):
        return {name:value for name,value in x.items() if name!="value"}
    return {
        "public_A":deepcopy(env["public"]),
        "public_Q":deepcopy(env["q"]),
        "audit_pre_read_metadata":evidence_metadata(env["audit"]),
        "conventional_pre_read_metadata":evidence_metadata(env["direct"]),
    }


def visible_after_measurement(env:Mapping[str,Any],kind:str)->dict:
    """A relevant qualified observation may add *legitimate* information."""
    if kind not in ("AUDITOR","CONVENTIONAL"):
        raise ValueError("unknown observation type")
    item=env["audit"] if kind=="AUDITOR" else env["direct"]
    signal=item["value"] if source.qualified(
        item,env["q"],env["public"],kind) else "NOT_QUALIFIED"
    return {**public_metadata(env),
            "new_qualified_reading":signal,
            "instrument_role":kind}


def _check_twins(a:Mapping[str,Any],b:Mapping[str,Any])->None:
    if {a["truth_PRIVATE_FOR_REFEREE_ONLY"],
        b["truth_PRIVATE_FOR_REFEREE_ONLY"]}!=set(TRUTH):
        raise ValueError("paired worlds require opposite private truth")
    if public_metadata(a)!=public_metadata(b):
        raise ValueError("counterfactual pair leaks private truth through public metadata")
    if a["source_case_id"]!=b["source_case_id"]:
        raise ValueError("paired source sampling identifier drift")
    if (a["audit"]["issuer_id"]==b["audit"]["issuer_id"] and
        a["direct"]["issuer_id"]==b["direct"]["issuer_id"]):
        return
    raise ValueError("matched observation source identity changed")


def _validate_manifest(manifest:Mapping[str,Any])->None:
    if manifest.get("schema")!=SCHEMA:
        raise ValueError("wrong L09 model schema")
    if manifest.get("source_manifest")!="G02_AUDIT_PROTOCOL.json":
        raise ValueError("unrecognized source owner manifest")
    n=manifest.get("replicates_per_pair")
    if type(n) is not int or n<8 or n>128:
        raise ValueError("unbounded paired repetitions")
    seed=manifest.get("seed")
    if not isinstance(seed,str) or not seed or len(seed)>120:
        raise ValueError("missing bounded random stream seed")
    bases=manifest.get("baseline_actions")
    if not isinstance(bases,list) or len(bases)!=len(set(bases)) or set(bases)!=set(BASELINES):
        raise ValueError("L09 must test both original A baseline shapes")
    chosen=manifest.get("source_regimes")
    if not isinstance(chosen,list) or not chosen or len(chosen)!=len(set(chosen)):
        raise ValueError("source regime list must be nonempty and distinct")


def run(manifest:Mapping[str,Any],*,include_private_samples:bool=False)->dict:
    _validate_manifest(manifest)
    raw=campaign.read_json("CASE_REGISTRY.json")
    campaign.validate_cases(campaign.read_json("SOURCE_REGISTER.json"),raw)
    source_manifest=campaign.read_json(manifest["source_manifest"])
    source.validate(source_manifest)
    registry={x["id"]:x for x in source_manifest["regimes"]}
    if len(registry)!=len(source_manifest["regimes"]):
        raise ValueError("source regimes not unique")
    if set(manifest["source_regimes"])-set(registry):
        raise ValueError("L09 contains unsupported source regime")
    pairs=make_public_matched_pairs(raw["cases"],manifest["baseline_actions"])
    historical=original_fixture_metadata_diagnostic(raw["cases"])
    reports=[]
    for regime_id in manifest["source_regimes"]:
        regime=registry[regime_id]
        pre=[]
        post_audit=[]
        post_direct=[]
        rows=[]
        samples=[]
        n=len(manifest["baseline_actions"])*len(pairs)//len(manifest["baseline_actions"])
        for pair in pairs:
            for rep in range(manifest["replicates_per_pair"]):
                twins=[
                    source.generate(case,regime["parameters"],seed=manifest["seed"],
                                    replicate=rep)
                    for case in pair["worlds"]
                ]
                _check_twins(*twins)
                for env in twins:
                    truth=env["truth_PRIVATE_FOR_REFEREE_ONLY"]
                    pre.append((public_metadata(env),truth))
                    post_audit.append((visible_after_measurement(env,"AUDITOR"),truth))
                    post_direct.append((visible_after_measurement(env,"CONVENTIONAL"),truth))
                    rows.append(source.evaluate(env,regime["prices"]))
                if include_private_samples and rep==0 and len(samples)<4:
                    samples.append({
                        "pair_id":pair["pair_id"],
                        "counterfactual_true_and_false_WORLD_ONLY":[
                            {"truth":t["truth_PRIVATE_FOR_REFEREE_ONLY"],
                             "audit_result":t["audit"]["value"],
                             "direct_result":t["direct"]["value"]}
                            for t in twins],
                        "same_public_metadata_in_both_worlds":True,
                    })
        no_read=explicit_information(pre)
        if no_read["optimal_public_only_accuracy"]!="1/2" or abs(no_read["visible_mutual_information_bits"])>1e-12:
            raise AssertionError("failed L09: public-only metadata reveals private label")
        measured=source.summarize(rows,regime_id)
        report={
            "regime":regime_id,
            "paired_binary_source_worlds":len(rows),
            "matched_public_pairs":len(pairs),
            "public_only_before_measuring":no_read,
            "after_fallible_qualified_audit":explicit_information(post_audit),
            "after_fallible_qualified_conventional":explicit_information(post_direct),
            "native_G02_policy_results":measured["new_policy_outcomes"],
            "source_variants_private_referee":measured["source_variant_counts"],
            "no_probabilities_for_open_C_D":True,
        }
        if include_private_samples:
            report["synthetic_private_referee_samples_NOT_PLANNER_INPUT"]=samples
        reports.append(report)
    return {
        "schema":SCHEMA,
        "manifest_sha256":sha256(_key(manifest).encode("utf-8")).hexdigest(),
        "source_input_sha256":{
            name:sha256((HERE/name).read_bytes()).hexdigest()
            for name in ("CASE_REGISTRY.json","SOURCE_REGISTER.json",
                         "G02_AUDIT_PROTOCOL.json","g02_evidence_audit.py","campaign.py")
        },
        "original_source_cases_not_modified":len(raw["cases"]),
        "original_source_true_false_Q_families":len(_original_pairs(raw["cases"])),
        "source_legacy_public_view_leakage":historical,
        "derived_matched_pairs":len(pairs),
        "replicates_per_pair":manifest["replicates_per_pair"],
        "total_source_world_evaluations":sum(x["paired_binary_source_worlds"]
                                             for x in reports),
        "regimes":reports,
        "source_owner":"PR73 G02 observation experiment / PR68 frozen 60-case campaign",
        "source_fixtures_preserved":True,
        "interpretation":"FINITE_SYNTHETIC_MATCHED_BINARY_Q_ONLY_NO_REAL_AUDIT_METRICS_OR_OPEN_C_D_PROBABILITY",
        "not_an_adaptive_agent_or_empirical_classifier_benchmark":True,
    }


def main(argv=None)->int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest",type=Path,default=HERE/"L09_MATCHING_PROTOCOL.json")
    parser.add_argument("--private-samples",action="store_true")
    parser.add_argument("--output",type=Path)
    args=parser.parse_args(argv)
    result=run(json.loads(args.manifest.read_text(encoding="utf-8")),
               include_private_samples=args.private_samples)
    txt=json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+"\n"
    if args.output:
        args.output.write_text(txt,encoding="utf-8")
    else:
        print(txt,end="")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
