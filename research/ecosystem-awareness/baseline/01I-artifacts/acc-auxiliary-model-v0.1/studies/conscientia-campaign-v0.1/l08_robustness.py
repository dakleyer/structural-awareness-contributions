"""L-08: reusable matched evidence/provenance/cost sensitivity laboratory.

Source-owned core remains PR70 G-04 and PR68 dimension_experiment.material_flow.
Never changes the original G-04 public policies, private world, or source math.

This is a *conditional* finite experiment, not an empirical source reliability
estimate, universal EA advantage, causal proof of FH-C, or a new social utility.
Two-dimensional error/miss Pareto and three-dimensional error/miss/price Pareto
are kept separate; monetary/intangible costs are NOT subtracted from food.
"""
from __future__ import annotations

from collections import Counter
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from itertools import product
from pathlib import Path
from typing import Any, Mapping, Sequence
import argparse
import json

from g04_factorial import (
    ARMS as ORIGINAL_ARMS, CLOCK, SOURCE_SCOPE,
    create_world, paired_evaluation, plan_public, _qualified,
)
from dimension_experiment import number as exact_number

HERE=Path(__file__).resolve().parent
SCHEMA="ACC-L08-CALIBRATED-PAIRED-EVIDENCE-v0.1"
NORMALIZED_DOMAIN="QUALIFIED_DOMAIN_FACTS_ONLY"
FAIR_ARMS=(
    "SOURCE_BOUNDARY_ONLY",
    NORMALIZED_DOMAIN,
    "BOTH_SOURCE_AND_DOMAIN",
    "CONVENTIONAL_TARGETED",
)
DIAGNOSTIC_ARMS=("NAIVE_SOURCE_ONLY_CONTROL","DOMAIN_FACTS_ONLY")
ALL_ARMS=(*FAIR_ARMS,*DIAGNOSTIC_ARMS)
PRICES=("source_review","domain_measurement","conventional_directed")
INSTRUMENT_PRICE_KEY={
    "scope_and_freshness_review":"source_review",
    "domain_measurement":"domain_measurement",
    "qualified_domain_measurement":"domain_measurement",
    "independent_conventional_inspection":"conventional_directed",
    "unqualified_source_claim":None,
}
CLASSIFICATIONS=(
    "BOUNDARY_DOMINATES_ON_ERRORS_AND_MISSED_CANDIDATES",
    "DOMAIN_FACTS_DOMINATES_ON_ERRORS_AND_MISSED_CANDIDATES",
    "TIE_ON_ERRORS_AND_MISSED_CANDIDATES",
    "INCOMPARABLE_ERROR_VS_MISSED_OPPORTUNITY_TRADEOFF",
)


def rational(value: Any, *, name: str, nonnegative: bool=True) -> Fraction:
    x=exact_number(value)
    if nonnegative and x < 0:
        raise ValueError("negative "+name)
    return x


def _public_domain_plan(world: Mapping[str,Any]) -> dict[str,Any]:
    """Qualify domain provenance exactly as G-04 qualifies source B metadata.

    This is a new explicitly named fair comparison, not an overwrite of the
    original G-04 DOMAIN_FACTS_ONLY legacy raw-observation control. Qualification
    is only about scope, freshness and hypothetical attestation; not truth.
    """
    public=world["public_A"]
    q=world["source_Q"]
    direct=world["domain_observation"]
    target=world["targeted_observation"]
    raw=plan_public(public,q,direct,target,"DOMAIN_FACTS_ONLY")
    result=dict(raw)
    result["arm"]=NORMALIZED_DOMAIN
    result["parent_policy"]="DOMAIN_FACTS_ONLY"
    result["source_metadata_contract"]="SAME_SCOPED_FRESH_ATTRIBUTED_CONDITIONS_AS_SOURCE_BOUNDARY_ONLY"
    result["qualified_domain_available"]=bool(direct.get("available") and _qualified(direct))
    if not result["qualified_domain_available"] and result["propose"]:
        # Original domain reading was accepted without its scope/freshness.
        # We retain the *consultation cost* and record the rejected evidence.
        result["propose"]=False
        result["status"]="NO_QUALIFIED_DOMAIN_SIGNAL"
    if not result["qualified_domain_available"] and result["status"]=="OBSERVED_OR_QUALIFIED_NO_GAIN":
        result["status"]="NO_QUALIFIED_DOMAIN_SIGNAL"
    return result


def _score_extra(world: Mapping[str,Any], referee: Mapping[str,Any]) -> dict[str,Any]:
    plan=_public_domain_plan(world)
    proposed=plan["propose"]
    eligible=referee["eligible"]
    return {
        "public_plan":plan,
        "unjustified_proposal":bool(proposed and not eligible),
        "justified_proposal":bool(proposed and eligible),
        "missed_feasible_candidate":bool(not proposed and eligible),
        "would_be_committed_under_declared_rights":bool(proposed and eligible),
        "observed_incremental_service_after_admission":
            referee["confirmed_output_if_authorized"] if proposed else 0,
        "instrument_cost_units_declared_SEPARATE_FROM_FOOD":plan["declared_cost"],
    }


def observed_case(world: Mapping[str,Any]) -> dict[str,Any]:
    """One shared world for all original five arms and the fair domain control.

    PR70 paired_evaluation plans first then invokes the PR68 private referee.
    Qualified domain is planned exclusively from A and acquired metadata.
    """
    candidate=_public_domain_plan(world)
    source=paired_evaluation(world)
    referee=source["private_referee_only"]
    extra=_score_extra(world,referee)
    if extra["public_plan"]!=candidate:
        raise AssertionError("normalized public decision changed with private referee")
    arms={**source["arms"], NORMALIZED_DOMAIN:extra}
    return {
        "scenario_id":world["scenario_id"],
        "source_scope":world["public_A"]["question_scope"],
        "eligibility_private_post_hoc":referee["eligible"],
        "native_operator":referee["source_owned"],
        "arms":arms,
        "public_A":world["public_A"],
        "source_qualification_instrument_metadata_only":
            bool(world["source_Q"].get("available") and _qualified(world["source_Q"])),
        "domain_qualification_instrument_metadata_only":
            bool(world["domain_observation"].get("available") and _qualified(world["domain_observation"])),
    }


def checked_price_contract(prices: Mapping[str,Any]) -> dict[str,Fraction]:
    if not isinstance(prices,dict) or set(prices)!=set(PRICES):
        raise ValueError("price contract must contain three instruments")
    return {name:rational(prices[name],name=name) for name in PRICES}


def _instrument_counts(plan: Mapping[str,Any]) -> Counter:
    if not plan.get("no_hidden_world_access"):
        raise AssertionError("public planner may not own private oracle")
    observed=Counter()
    for instrument in plan["instruments_queried"]:
        if instrument not in INSTRUMENT_PRICE_KEY:
            raise ValueError("unregistered instrument "+str(instrument))
        entry=INSTRUMENT_PRICE_KEY[instrument]
        if entry is not None:
            observed[entry]+=1
    return observed


def _measure(records: Sequence[Mapping[str,Any]]) -> dict[str,dict[str,Any]]:
    """Physical and correctness measurements never depend on price profiles."""
    result={}
    n=len(records)
    if not n:
        raise ValueError("no paired case records")
    opportunities=sum(row["eligibility_private_post_hoc"] for row in records)
    for arm in ALL_ARMS:
        samples=[row["arms"][arm] for row in records]
        errors=sum(row["unjustified_proposal"] for row in samples)
        misses=sum(row["missed_feasible_candidate"] for row in samples)
        justified=sum(row["justified_proposal"] for row in samples)
        units=sum(row["observed_incremental_service_after_admission"] for row in samples)
        instrument_usage=Counter()
        for item in samples:
            instrument_usage.update(_instrument_counts(item["public_plan"]))
        if misses+justified!=opportunities:
            raise AssertionError("policy changed the private eligible population")
        if errors+justified!=sum(row["public_plan"]["propose"] for row in samples):
            raise AssertionError("missing or duplicated proposal")
        result[arm]={
            "invalid_proposals":errors,
            "valid_proposals":justified,
            "missed_valid_opportunities":misses,
            "committable_under_declared_conditions":justified,
            "incremental_food_service":units,
            "instrument_consultations":dict(sorted(instrument_usage.items())),
            "policy_is_normalized_provenance_control":arm==NORMALIZED_DOMAIN,
            "competent_comparator":arm in FAIR_ARMS,
        }
    return result


def _cost(item:Mapping[str,Any],price:Mapping[str,Fraction])->Fraction:
    return sum((v*price[k] for k,v in item["instrument_consultations"].items()),
               Fraction(0))


def pareto(
    points:Mapping[str,Sequence[Fraction|int]],
    *, axes:Sequence[str],
) -> list[str]:
    """Vector order: each axis is minimized. No silent scalar weights."""
    if not points or not axes:
        raise ValueError("nonempty dimensions/arms required")
    n=len(axes)
    if any(len(v)!=n for v in points.values()):
        raise ValueError("inconsistent dimension arity")
    for arm,values in points.items():
        if any(v is None for v in values):
            raise ValueError("unknown value cannot become zero in Pareto comparison")
    return sorted(arm for arm,point in points.items() if not any(
        peer!=arm and all(a<=b for a,b in zip(other,point)) and
        any(a<b for a,b in zip(other,point))
        for peer,other in points.items()
    ))


def two_arm_order(first:Mapping[str,Any],second:Mapping[str,Any])->str:
    x=(first["invalid_proposals"],first["missed_valid_opportunities"])
    y=(second["invalid_proposals"],second["missed_valid_opportunities"])
    if all(a<=b for a,b in zip(x,y)) and any(a<b for a,b in zip(x,y)):
        return CLASSIFICATIONS[0]
    if all(b<=a for a,b in zip(x,y)) and any(b<a for a,b in zip(x,y)):
        return CLASSIFICATIONS[1]
    if x==y:
        return CLASSIFICATIONS[2]
    return CLASSIFICATIONS[3]


def _result_for(
    metrics:Mapping[str,Mapping[str,Any]], cost_profiles:Sequence[Mapping[str,Any]],
) -> dict[str,Any]:
    fair={arm:metrics[arm] for arm in FAIR_ARMS}
    no_price={arm:(v["invalid_proposals"],v["missed_valid_opportunities"])
              for arm,v in fair.items()}
    two_front=pareto(no_price,axes=("invalid_proposals","missed_valid_opportunities"))
    price_fronts={}
    for cost in cost_profiles:
        prices=checked_price_contract(cost["unit_prices"])
        values={arm:_cost(v,prices) for arm,v in fair.items()}
        triple={arm:(*no_price[arm],values[arm]) for arm in FAIR_ARMS}
        price_fronts[cost["id"]]={
            "three_axis_pareto_front":pareto(
                triple, axes=("invalid_proposals","missed_valid_opportunities",
                              "instrument_cost")),
            "cost_of_instruments_by_arm":{k:str(v) for k,v in values.items()},
            "price_schedule":{k:str(v) for k,v in prices.items()},
            "cost_paid_for_qualified_but_rejected_evidence":True,
        }
    return {
        "matched_two_axis_source_vs_scoped_domain":two_arm_order(
            metrics["SOURCE_BOUNDARY_ONLY"],metrics[NORMALIZED_DOMAIN]),
        "two_axis_front_no_price":two_front,
        "three_axis_fronts_by_price_contract":price_fronts,
    }


def validate(manifest:Mapping[str,Any])->None:
    if manifest.get("schema")!=SCHEMA:
        raise ValueError("unknown L08 manifest schema")
    if not isinstance(manifest.get("seed"),str) or not manifest["seed"] or len(manifest["seed"])>100:
        raise ValueError("missing bounded common experimental seed")
    n=manifest.get("worlds_per_grid_cell")
    if type(n) is not int or not 16<=n<=512:
        raise ValueError("paired grid size outside bounded reproducible interval")
    grid=manifest.get("accuracy_grid")
    if not isinstance(grid,list) or not 2<=len(grid)<=9:
        raise ValueError("accuracy grid must contain 2-9 declared points")
    if len(set(grid))!=len(grid):
        raise ValueError("duplicate grid probabilities")
    vals=[rational(x,name="signal_accuracy") for x in grid]
    if any(x>1 for x in vals) or vals!=sorted(vals):
        raise ValueError("accuracy grid must be sorted probabilities in [0,1]")
    panels=manifest.get("panels")
    if not isinstance(panels,list) or not 1<=len(panels)<=4:
        raise ValueError("one to four provenance/access panels required")
    panelids=[]
    required={"source_probability","source_scoped_probability",
              "source_correct_if_qualified","source_correct_if_other",
              "source_signed","source_fresh","domain_available",
              "domain_accuracy","domain_qualified","targeted_available",
              "targeted_accuracy","role_probability","consent_probability",
              "authority_probability","joint_probability"}
    for item in panels:
        if not isinstance(item,dict) or not isinstance(item.get("id"),str) or not item["id"]:
            raise ValueError("panel identity required")
        panelids.append(item["id"])
        params=item.get("base_parameters")
        if not isinstance(params,dict) or set(params)!=required:
            raise ValueError("source signal generator parameter contract incomplete")
        for name,value in params.items():
            v=rational(value,name=name)
            if v>1:
                raise ValueError("probability outside [0,1]: "+name)
    if len(set(panelids))!=len(panelids):
        raise ValueError("duplicate panel ID")
    costs=manifest.get("price_contracts")
    if not isinstance(costs,list) or not 2<=len(costs)<=12:
        raise ValueError("two to twelve alternative instrument price schedules required")
    cost_ids=[]
    for row in costs:
        cost_ids.append(row["id"])
        checked_price_contract(row["unit_prices"])
    if len(set(cost_ids))!=len(cost_ids):
        raise ValueError("duplicate price schedule")
    if manifest.get("population")!="SOURCE_ORIGINAL_FINITE_BANANA_TRANSFER_1_HOLDER_1_BENEFICIARY":
        raise ValueError("unsupported finite source example question")
    if manifest.get("horizon")!="ONE_DECLARED_DECISION_AT_CLOCK_10":
        raise ValueError("matched exercise horizon changed")


def _case(
    panel:Mapping[str,Any], source_accuracy:str, domain_accuracy:str,
    *, manifest:Mapping[str,Any], include_sample:bool=False,
)->dict[str,Any]:
    params={
        **panel["base_parameters"],
        "source_correct_if_qualified":source_accuracy,
        "domain_accuracy":domain_accuracy,
    }
    # Identical seed and index -> identical private worlds and PUBLIC A across
    # every accuracy cell of both panels. Source and fact signals may differ,
    # exactly as intentional interventions should.
    common_seed=manifest["seed"]
    records=[]
    world_sample=[]
    for i in range(manifest["worlds_per_grid_cell"]):
        world=create_world(i,params,common_seed)
        res=observed_case(world)
        records.append(res)
        if include_sample and i<3:
            world_sample.append({
                "index":i,"public_A":world["public_A"],
                "source_Q":world["source_Q"],
                "domain_observation":world["domain_observation"],
                "targeted_observation":world["targeted_observation"],
                "PRIVATE_FOR_POST_HOC_AUDIT_ONLY":world["truth_PRIVATE_FOR_REFEREE_ONLY"],
                "plans_by_arm":{k:v["public_plan"] for k,v in res["arms"].items()},
                "physical_eligibility_PRIVATE":res["eligibility_private_post_hoc"],
            })
    measured=_measure(records)
    alternatives=_result_for(measured,manifest["price_contracts"])
    return {
        "cell_id":panel["id"]+"-Q"+source_accuracy+"-DOMAIN"+domain_accuracy,
        "panel":panel["id"],
        "assumed_accuracy_of_qualified_source":source_accuracy,
        "assumed_per_domain_observation_accuracy":domain_accuracy,
        "source_question":SOURCE_SCOPE,
        "matched_worlds":len(records),
        "private_eligible_opportunities":sum(x["eligibility_private_post_hoc"] for x in records),
        "instrumental_arms":measured,
        **alternatives,
        **({"selected_PRIVATE_audit_samples":world_sample} if include_sample else {}),
    }


def run(manifest:dict[str,Any], *, include_audit_samples:bool=False)->dict[str,Any]:
    validate(manifest)
    panels=[]
    all_orders=Counter()
    for panel in manifest["panels"]:
        cells=[]
        for source,domain in product(manifest["accuracy_grid"],repeat=2):
            cell=_case(panel,source,domain,manifest=manifest,
                       include_sample=include_audit_samples and
                       source==manifest["accuracy_grid"][0] and
                       domain==manifest["accuracy_grid"][-1])
            cells.append(cell)
            all_orders[cell["matched_two_axis_source_vs_scoped_domain"]]+=1
        panels.append({
            "id":panel["id"],"base_parameters":panel["base_parameters"],
            "count_cells":len(cells),
            "counts_by_two_axis_source_vs_scoped_domain":dict(sorted(
                Counter(x["matched_two_axis_source_vs_scoped_domain"]
                        for x in cells).items())),
            "cells":cells,
        })
    return {
        "schema":SCHEMA,
        "manifest_sha256":sha256(json.dumps(manifest,sort_keys=True,
                                separators=(",",":")).encode("utf-8")).hexdigest(),
        "source_owner":"PR70.g04_factorial + PR68.dimension_experiment.material_flow",
        "source_engine_sha256":{
            name:sha256((HERE/name).read_bytes()).hexdigest()
            for name in ("g04_factorial.py","dimension_experiment.py",
                         "G04_PROTOCOL.json")
        },
        "source_original_public_policies_unchanged":True,
        "legacy_domain_raw_was_unqualified":True,
        "scoped_domain_requires_same_source_metadata_qualification":True,
        "experiment_not_human_measurement_or_real_source_reliability":True,
        "statistical_limit":"FIXED_SEED_SYNTHETIC_GRID_NOT_POPULATION",
        "external_FH_C_causality":"NOT_IDENTIFIED",
        "source_question":manifest["population"],
        "horizon":manifest["horizon"],
        "total_distinct_matched_worlds":manifest["worlds_per_grid_cell"],
        "total_paired_cell_evaluations":len(panels)*len(manifest["accuracy_grid"])**2
                                           *manifest["worlds_per_grid_cell"],
        "regime_counts_by_two_axis_relation":dict(sorted(all_orders.items())),
        "price_contracts":[row["id"] for row in manifest["price_contracts"]],
        "fair_policies":list(FAIR_ARMS),
        "historical_raw_policies_held_as_diagnostics":list(DIAGNOSTIC_ARMS),
        "panels":panels,
    }


def main(argv:Sequence[str]|None=None)->int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest",type=Path,default=HERE/"L08_PROTOCOL.json")
    parser.add_argument("--output",type=Path)
    parser.add_argument("--include-audit-samples",action="store_true")
    args=parser.parse_args(argv)
    data=run(json.loads(args.manifest.read_text(encoding="utf-8")),
             include_audit_samples=args.include_audit_samples)
    text=json.dumps(data,ensure_ascii=False,sort_keys=True,indent=2)+"\n"
    if args.output:
        args.output.write_text(text,encoding="utf-8")
    else:
        print(text,end="")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
