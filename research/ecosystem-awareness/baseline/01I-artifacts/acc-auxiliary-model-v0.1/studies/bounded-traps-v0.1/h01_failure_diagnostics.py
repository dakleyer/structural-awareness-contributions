"""H-01 conditions, not averages: conditional source-owned failure diagnostics.

Reads the exact predeclared 180-cell grid and all 22 named source-anchored
scenarios. Independently derives individual deviation D, joint gain J and
net-of-coordination gain N from declared rational parameters and checks them
against the original strategic_choice engine's computed decisions.

This is a diagnostic of *one symmetric, finite two-player toy*, NOT a
probability distribution over social systems or an estimate of real failures.
No original model data, actors, author examples or controlled corpus is edited.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import argparse
import json
from typing import Any, Mapping

import strategic_choice as source

HERE=Path(__file__).resolve().parent
VERSION="ACC-H01-CONDITIONAL-FAILURE-DIAGNOSTICS-v0.1"
CLAIMS=(
    "STRICT_RATIONAL_COORDINATION_TRAP",
    "PROFITABLE_UNILATERAL_ESCAPE_NOT_A_NASH_TRAP",
    "WEAK_NASH_NO_STRICT_UNILATERAL_GAIN",
    "NO_PARETO_SUPERIOR_TARGET_ON_ACTOR_UTILITIES",
)
PASS="ADMISSIBLE_UNDER_SYNTHETIC_ASSUMPTIONS"
REJECT="VOLUNTARY_PARTICIPATION_NOT_SUPPORTED_BY_PAYOFFS"


def n(x:Any)->Fraction:
    return source.q(x)


def _symmetry_contract(manifest:Mapping[str,Any])->dict[str,Any]:
    """This finite diagnostic is valid only for the source's symmetric sweep."""
    base=manifest["base_game"]
    source.validate(base)
    if len(base["actors"])!=2 or base["current"]!=[0,0] or base["target"]!=[1,1]:
        raise ValueError("phase analysis requires 2 agents, current 00 target 11")
    if base["linear_constraints"]:
        raise ValueError("cannot use four-feasible-phase law for constrained topology")
    names=[a["id"] for a in base["actors"]]
    common_base=n(base["actors"][0]["base_payoff"])
    for actor in base["actors"]:
        if n(actor["base_payoff"])!=common_base:
            raise ValueError("symmetric payoff baseline required")
        if n(actor["reservation_floor"])!=common_base:
            raise ValueError("reservation floor must equal personal baseline in this sweep")
    if not base["joint"]["strict_gain_required"]:
        raise ValueError("phase law calibrated to strict, not weak improvement")
    if any(n(v)!=0 for v in base["joint"]["transfers_common_credit_units"].values()):
        raise ValueError("sweep requires zero compensation, not a transfer scenario")
    if any(status!="PASS" for status in (
        base["governance"]["authority"],base["governance"]["joint_protocol"],
        *base["governance"]["consents"].values())):
        raise ValueError("sweep assumes explicit PASS governance; cannot extrapolate")
    if any(n(a["resource_units_if_active"],signed=False)<0 for a in base["actors"]):
        raise ValueError("invalid resource")
    use=sum(n(a["resource_units_if_active"]) for a in base["actors"])+n(
        base["joint"]["setup_resource_units"])
    budget=n(base["resource_budget"])
    if use>budget:
        raise ValueError("sweep requires adequate physical setup budget")
    return {
        "actor_ids":names,
        "actor_initial_payoff":str(common_base),
        "physical_resource_use":str(use),
        "physical_resource_budget":str(budget),
        "consent_and_authority":"PASS_BY_FIXTURE_NOT_OBSERVED",
        "compensation":"ZERO_COMMON_CREDIT_TRANSFER_IN_SWEEP",
        "participation_rule":"EACH_ACTOR_MUST_IMPROVE_STRICTLY",
        "scope":"SYMMETRIC_TWO_ACTOR_DECLARED_FINITE_PARAMETRIC_SWEEP",
    }


def phase(row:Mapping[str,Any],baseline:Fraction)->dict[str,Any]:
    params=row["params"]
    r=n(params["private_return"])
    c=n(params["investment_cost"])
    s=n(params["pairwise_complementarity"])
    b=n(params["joint_burden"])
    D=r-c
    J=D+s
    N=J-b
    if J<=0:
        expected="NO_PARETO_SUPERIOR_TARGET_ON_ACTOR_UTILITIES"
    elif D>0:
        expected="PROFITABLE_UNILATERAL_ESCAPE_NOT_A_NASH_TRAP"
    elif D==0:
        expected="WEAK_NASH_NO_STRICT_UNILATERAL_GAIN"
    else:
        expected="STRICT_RATIONAL_COORDINATION_TRAP"
    accepted=N>0
    expected_status=PASS if accepted else REJECT
    if row["classification"]!=expected:
        raise AssertionError("actual strategic classification violates independent threshold")
    if row["joint_admissibility"]!=expected_status:
        raise AssertionError("actual joint admission violates net actor threshold")
    current=[n(x) for x in row["current_payoffs"]]
    target=[n(x) for x in row["target_payoffs"]]
    if current != [baseline,baseline]:
        raise AssertionError("computed initial payoff drift")
    if target != [baseline+J,baseline+J]:
        raise AssertionError("computed joint payoff does not match independent formula")
    profitable=2 if D>0 else 0
    if row["unilateral_profitable_count"]!=profitable:
        raise AssertionError("computed unilateral profit count drift")
    if expected=="STRICT_RATIONAL_COORDINATION_TRAP" and accepted:
        outcome="GENUINE_STRICT_TRAP_AND_CONDITIONALLY_ACCEPTABLE_REMEDY"
    elif expected=="STRICT_RATIONAL_COORDINATION_TRAP":
        outcome="GENUINE_STRICT_TRAP_BUT_REMEDY_EXHAUSTED"
    elif expected=="PROFITABLE_UNILATERAL_ESCAPE_NOT_A_NASH_TRAP":
        outcome="UNILATERAL_ESCAPE_ALREADY_AVAILABLE"
    elif expected=="WEAK_NASH_NO_STRICT_UNILATERAL_GAIN":
        outcome="WEAK_INDIFFERENCE_NOT_STRICT_REFUSAL"
    else:
        outcome="NO_GROSS_PARETO_GAIN_TO_RECOVER"
    if J<0:
        rejected="JOINT_ALTERNATIVE_HARMS_EACH_ACTOR"
    elif J==0:
        rejected="JOINT_ALTERNATIVE_BREAK_EVEN_BEFORE_COORDINATION"
    elif N<0:
        rejected="BURDEN_GREATER_THAN_JOINT_GAIN"
    elif N==0:
        rejected="BURDEN_EQUALS_JOINT_GAIN_STRICT_RULE_REJECTS"
    else:
        rejected=None
    return {
        "parameters":dict(params),
        "unilateral_increment_D":str(D),
        "joint_increment_before_burden_J":str(J),
        "net_increment_after_burden_N":str(N),
        "strategic_mechanism":expected,
        "coordination_admitted":accepted,
        "outcome":outcome,
        "primary_failure_condition":rejected,
        "strict_trap_remedied":bool(expected=="STRICT_RATIONAL_COORDINATION_TRAP" and accepted),
        "positive_joint_gain_not_automatically_strictly_admissible":bool(J>0 and N<=0),
    }


def _summarize_slices(rows:list[dict],axis:str)->dict[str,Any]:
    keys=sorted({n(x["parameters"][axis]) for x in rows})
    result={}
    for value in keys:
        vals=[x for x in rows if n(x["parameters"][axis])==value]
        strict=[x for x in vals if
                x["strategic_mechanism"]=="STRICT_RATIONAL_COORDINATION_TRAP"]
        result[str(value)]={
            "configurations":len(vals),
            "joint_accepted":sum(x["coordination_admitted"] for x in vals),
            "joint_rejected":sum(not x["coordination_admitted"] for x in vals),
            "genuine_strict_traps":len(strict),
            "strict_traps_with_admissible_remedy":sum(x["coordination_admitted"]
                                                     for x in strict),
            "strict_traps_with_rejected_remedy":sum(not x["coordination_admitted"]
                                                  for x in strict),
        }
    return result


def _named_failure_reason(row:Mapping[str,Any])->dict:
    case=row["case_id"]
    joint=row["joint_coordination"]
    status=joint["status"]
    gate=joint["governance_evidence"]
    reasons=[]
    if not joint["technical_candidate_feasible"]:
        reasons.append("TARGET_TECHNICALLY_INFEASIBLE")
    if n(joint["joint_resource_use_including_setup"])>n(joint["resource_budget"]):
        reasons.append("JOINT_SETUP_EXCEEDS_AVAILABLE_PHYSICAL_BUDGET")
    if not joint["credit_outflow_fully_funded"]:
        reasons.append("UNFUNDED_COMMON_CREDIT_TRANSFER")
    failed=[x for x,v in joint["individual_reservation_tests"].items() if not v]
    if failed:
        reasons.append("INDIVIDUAL_NET_PAYOFF_BELOW_RESERVATION_OR_STRICT_GAIN")
    if any(v=="FAIL" for v in gate.values()):
        reasons.append("EXPLICIT_AUTHORIZATION_OR_CONSENT_FAILURE")
    if any(v=="UNKNOWN" for v in gate.values()):
        reasons.append("EVIDENCE_OF_AUTHORITY_OR_CONSENT_UNKNOWN")
    if not reasons:
        reasons=["ADMITTED_ONLY_UNDER_DECLARED_ASSUMPTIONS"]
    if status==PASS and reasons!=["ADMITTED_ONLY_UNDER_DECLARED_ASSUMPTIONS"]:
        raise AssertionError("admitted proposal with real rejection condition")
    return {
        "case_id":case,
        "mechanism":row["mechanism"]["classification"],
        "joint_status":status,
        "specific_reasons":reasons,
        "failing_actor_ids":failed,
        "evidence_not_real_world_execution":True,
    }


def examine(manifest:Mapping[str,Any],report:Mapping[str,Any])->dict:
    if manifest["schema"]!=source.MANIFEST or report["schema"]!=source.MANIFEST:
        raise ValueError("H01 source identity mismatch")
    assumptions=_symmetry_contract(manifest)
    sweep=report["sensitivity"]
    grid=manifest["sensitivity"]
    count=1
    for k in ("standalone_returns","investment_costs","pairwise_synergies",
              "individual_joint_burdens"):
        count*=len(grid[k])
    if sweep["cells"]!=count or len(sweep["rows"])!=count:
        raise ValueError("incomplete finite parameter sweep")
    baseline=n(assumptions["actor_initial_payoff"])
    parsed=[phase(row,baseline) for row in sweep["rows"]]
    identities=[tuple(sorted(x["parameters"].items())) for x in parsed]
    if len(set(identities))!=len(parsed):
        raise ValueError("duplicate sensitivity input tuple")
    cross=defaultdict(Counter)
    failures=Counter()
    for cell in parsed:
        cross[cell["strategic_mechanism"]][
            "joint_admitted" if cell["coordination_admitted"] else "joint_rejected"]+=1
        if not cell["coordination_admitted"]:
            failures[cell["primary_failure_condition"]]+=1
    classes={}
    for key in source_classes():
        groups=cross[key]
        classes[key]={
            "joint_admitted":groups["joint_admitted"],
            "joint_rejected":groups["joint_rejected"],
            "count":sum(groups.values()),
        }
    if dict(sorted(Counter(x["strategic_mechanism"] for x in parsed).items()))!=sweep["classification_counts"]:
        raise AssertionError("class totals do not match original experiment")
    expected_totals={PASS:sum(x["coordination_admitted"] for x in parsed),
                     REJECT:sum(not x["coordination_admitted"] for x in parsed)}
    if expected_totals!=sweep["joint_admission_counts"]:
        raise AssertionError("admission totals disagree with source engine")
    # Counterfactual burden slice: all three burden levels exist for each
    # exact return/investment/synergy triple, so changing only burden is
    # a supported finite causal mechanism within this declared model.
    burden_levels=sorted({n(v) for v in grid["individual_joint_burdens"]})
    by_unchanged=defaultdict(dict)
    for cell in parsed:
        p=cell["parameters"]
        k=(p["private_return"],p["investment_cost"],p["pairwise_complementarity"])
        by_unchanged[k][n(p["joint_burden"])]=cell
    switches=[]
    for k,series in sorted(by_unchanged.items()):
        if set(series)!=set(burden_levels):
            raise AssertionError("burden counterfactual lacks comparable base world")
        first=series[burden_levels[0]]
        last=series[burden_levels[-1]]
        if first["strategic_mechanism"]!=last["strategic_mechanism"]:
            raise AssertionError("coordination burden changed the Nash equilibrium")
        if first["coordination_admitted"] and not last["coordination_admitted"]:
            switches.append({
                "same_return_cost_synergy":list(k),
                "baseline_burden":str(burden_levels[0]),
                "increased_burden":str(burden_levels[-1]),
                "individual_net_margin_before":first["net_increment_after_burden_N"],
                "individual_net_margin_after":last["net_increment_after_burden_N"],
                "strict_trap_exists":first["strategic_mechanism"]==
                    "STRICT_RATIONAL_COORDINATION_TRAP",
                "status":"ONLY_BURDEN_CHANGED_STRICT_ACCEPTANCE_LOST",
            })
        if not first["coordination_admitted"] and last["coordination_admitted"]:
            raise AssertionError("increasing burden cannot create an individually acceptable remedy")
    statuses=[_named_failure_reason(row) for row in report["scenarios"]]
    return {
        "schema":VERSION,
        "evidence_scope":assumptions,
        "source_report_schema":report["schema"],
        "total_cells":len(parsed),
        "classification_by_joint_admission":classes,
        "net_failure_reasons":dict(sorted(failures.items())),
        "conditional_slices":{
            "by_joint_burden":_summarize_slices(parsed,"joint_burden"),
            "by_pairwise_complementarity":_summarize_slices(parsed,"pairwise_complementarity"),
            "by_private_return":_summarize_slices(parsed,"private_return"),
            "by_investment_cost":_summarize_slices(parsed,"investment_cost"),
        },
        "potentially_fixable_strict_traps":sum(x["strict_trap_remedied"] for x in parsed),
        "strict_traps_unremedied":classes["STRICT_RATIONAL_COORDINATION_TRAP"]["joint_rejected"],
        "admitted_cases_not_strict_traps":sum(x["coordination_admitted"] and
                    x["strategic_mechanism"]!="STRICT_RATIONAL_COORDINATION_TRAP"
                    for x in parsed),
        "matched_burden_counterfactuals":{
            "distinct_return_cost_synergy_conditions":len(by_unchanged),
            "lost_admissibility_when_only_burden_increases":len(switches),
            "strict_traps_losing_admissibility":sum(x["strict_trap_exists"] for x in switches),
            "examples":switches,
        },
        "named_scenarios_explained":statuses,
        "all_source_cells_have_direct_individual_margin_explanation":True,
        "unknown_other_mechanisms_not_reduced_to_zero":True,
        "grid_cell_counts_are_NOT_real_world_probabilities":True,
    }


def source_classes()->tuple[str,...]:
    return (
        "STRICT_RATIONAL_COORDINATION_TRAP",
        "PROFITABLE_UNILATERAL_ESCAPE_NOT_A_NASH_TRAP",
        "WEAK_NASH_NO_STRICT_UNILATERAL_GAIN",
        "NO_PARETO_SUPERIOR_TARGET_ON_ACTOR_UTILITIES",
    )


def main(argv=None)->int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest",type=Path,default=HERE/"H01_STRATEGIC_STUDY.json")
    parser.add_argument("--results",type=Path)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args(argv)
    m=json.loads(args.manifest.read_text(encoding="utf-8"))
    report=(json.loads(args.results.read_text(encoding="utf-8"))
            if args.results else source.run_manifest(m))
    result=examine(m,report)
    text=json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False)+"\n"
    if args.output:
        args.output.write_text(text,encoding="utf-8")
    else:
        print(text,end="")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
