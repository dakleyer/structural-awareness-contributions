"""H-01 finite strategic-choice supplement to ACC bounded-traps.

Distinguishes (i) technical feasibility, (ii) voluntary best responses under
actor-specific payoffs, (iii) a jointly preferable target, and (iv) actual
governance/protocol admission. This is a declared synthetic coordination game,
not an inference about actual humans, legal authority, or a new Nash theorem.

Original bounded_traps.coupled_trap() and its frozen results are NOT modified.
No cross-agent sum of utility, no probability distribution for epistemic C/D.
All numerical operations use exact rational arithmetic, standard library only.
"""
from __future__ import annotations

from collections import deque
from copy import deepcopy
from fractions import Fraction
from itertools import product
from pathlib import Path
import argparse
import json
from typing import Any, Mapping, Sequence

from bounded_traps import coupled_trap

HERE=Path(__file__).resolve().parent
SCHEMA="ACC-H01-FINITE-STRATEGIC-CHOICE-v0.1"
MANIFEST="ACC-H01-FINITE-STRATEGIC-STUDY-v0.1"
GATES=("PASS","FAIL","UNKNOWN")
ARMS=("CONVENTIONAL_COORDINATOR","ACC_META_PROTOCOL")


def q(value:Any, *, signed:bool=True)->Fraction:
    """Exact toy units, not booleans, machine floats, or cross-domain money."""
    if isinstance(value,bool) or value is None or isinstance(value,float):
        raise ValueError("declare a finite rational with int/string/Fraction, not float/bool/unknown")
    try:
        a=Fraction(value)
    except (TypeError,ValueError,ZeroDivisionError,OverflowError) as exc:
        raise ValueError("invalid exact rational") from exc
    if a.denominator>1000000 or abs(a)>1000000000:
        raise ValueError("bounded rational precision/magnitude required")
    if not signed and a<0:
        raise ValueError("nonnegative resource/cost required")
    return a


def fmt(a:Fraction)->str:
    return str(a)


def merge(base:Any,change:Any)->Any:
    """Versioned manifest overlays: fail on typo/unknown fields, never mutate."""
    if not isinstance(change,dict):
        return deepcopy(change)
    if not isinstance(base,dict):
        raise ValueError("patch expects a mapping")
    out=deepcopy(base)
    for key,value in change.items():
        if key not in base:
            raise ValueError("patch has undeclared field: "+key)
        out[key]=merge(base[key],value)
    return out


def validate(g:Mapping[str,Any])->None:
    if g.get("schema")!=SCHEMA or g.get("evidence_tier")!="SOURCE_ANCHORED_SYNTHETIC_TOY":
        raise ValueError("unknown synthetic strategic contract")
    actors=g.get("actors")
    if not isinstance(actors,list) or not 2<=len(actors)<=6:
        raise ValueError("2..6 declared actors required")
    ids=[a.get("id") for a in actors]
    if any(not isinstance(x,str) or not x for x in ids) or len(set(ids))!=len(ids):
        raise ValueError("actor IDs must be unique/nonblank")
    n=len(ids)
    for a in actors:
        for name in ("base_payoff","standalone_return","investment_cost",
                     "resource_units_if_active","reservation_floor"):
            if name not in a:
                raise ValueError("actor field missing: "+name)
            q(a[name],signed=(name in ("base_payoff","standalone_return","reservation_floor")))
        for k in ("complementarity_from","inactive_exposure_from"):
            if not isinstance(a.get(k),dict) or set(a[k])!=set(ids)-{a["id"]}:
                raise ValueError("pairwise payoff relation missing/extra participant")
            for value in a[k].values():
                q(value)
    for key in ("current","target"):
        state=g.get(key)
        if (not isinstance(state,list) or len(state)!=n or
            any(type(x) is not int or x not in (0,1) for x in state)):
            raise ValueError("states must be binary profiles of declared actors")
    q(g["resource_budget"],signed=False)
    c=g.get("linear_constraints")
    if not isinstance(c,list):
        raise ValueError("declare linear feasibility constraints, even if empty")
    for line in c:
        if not isinstance(line,dict) or len(line.get("coefficients",[]))!=n:
            raise ValueError("linear constraint dimension mismatch")
        for x in line["coefficients"]:
            q(x)
        q(line["capacity"])
    gov=g.get("governance")
    if not isinstance(gov,dict) or set(gov)!={
        "authority","joint_protocol","transfer_authority","consents"
    } or not isinstance(gov["consents"],dict) or set(gov["consents"])!=set(ids):
        raise ValueError("missing individual consent/authority contract")
    if any(x not in GATES for x in (
            gov["authority"],gov["joint_protocol"],gov["transfer_authority"],
            *gov["consents"].values())):
        raise ValueError("unsupported governance status")
    joint=g.get("joint")
    if not isinstance(joint,dict) or set(joint)!={
        "setup_resource_units","burden_payoff_units",
        "transfers_payoff_units","strict_gain_required"
    }:
        raise ValueError("joint proposal contract incomplete")
    q(joint["setup_resource_units"],signed=False)
    if type(joint["strict_gain_required"]) is not bool:
        raise ValueError("strict individual agreement requirement must be boolean")
    for name,signed in (("burden_payoff_units",False),("transfers_payoff_units",True)):
        vals=joint[name]
        if not isinstance(vals,dict) or set(vals)!=set(ids):
            raise ValueError("joint actor cost/transfer ledger mismatch")
        for value in vals.values():
            q(value,signed=signed)
    if sum((q(v) for v in joint["transfers_payoff_units"].values()),Fraction(0))!=0:
        raise ValueError("payoff transfers must sum to zero; no money created")
    prices=g.get("information_prices")
    if not isinstance(prices,dict) or set(prices)!=set(ARMS):
        raise ValueError("both strong coordinators require comparable instrument cost")
    for amount in prices.values():
        q(amount,signed=False)
    beliefs=g.get("belief_grid")
    if not isinstance(beliefs,list) or len(set(beliefs))!=len(beliefs):
        raise ValueError("unique explicit belief grid needed")
    for value in beliefs:
        prob=q(value,signed=False)
        if prob>1:
            raise ValueError("belief must be within [0,1]")
    if not isinstance(g.get("source_anchor"),str) or not g["source_anchor"]:
        raise ValueError("preserve the original source link")


def actors(g:Mapping[str,Any])->tuple[str,...]:
    return tuple(a["id"] for a in g["actors"])


def _state(state:Sequence[int],g:Mapping[str,Any])->tuple[int,...]:
    x=tuple(state)
    if len(x)!=len(g["actors"]) or any(type(v) is not int or v not in (0,1) for v in x):
        raise ValueError("not a declared binary state")
    return x


def resources(state:Sequence[int],g:Mapping[str,Any])->Fraction:
    x=_state(state,g)
    return sum((x[i]*q(a["resource_units_if_active"],signed=False)
                for i,a in enumerate(g["actors"])),Fraction(0))


def feasible(state:Sequence[int],g:Mapping[str,Any])->bool:
    x=_state(state,g)
    if resources(x,g)>q(g["resource_budget"],signed=False):
        return False
    for rule in g["linear_constraints"]:
        left=sum((q(v)*state_i for v,state_i in
                  zip(rule["coefficients"],x)),Fraction(0))
        if left>q(rule["capacity"]):
            return False
    return True


def profiles(g:Mapping[str,Any])->tuple[tuple[int,...],...]:
    return tuple(x for x in product((0,1),repeat=len(g["actors"])) if feasible(x,g))


def payoff(state:Sequence[int],g:Mapping[str,Any])->tuple[Fraction,...]:
    x=_state(state,g)
    if not feasible(x,g):
        raise ValueError("payoff is not certified for an infeasible profile")
    ids=actors(g)
    v=[]
    for i,a in enumerate(g["actors"]):
        base=q(a["base_payoff"])
        own_active=x[i]*(
            q(a["standalone_return"])-
            q(a["investment_cost"],signed=False))
        gains=sum((x[i]*x[j]*q(a["complementarity_from"][other])
                   for j,other in enumerate(ids) if j!=i),Fraction(0))
        exposure=sum(((1-x[i])*x[j]*q(a["inactive_exposure_from"][other])
                      for j,other in enumerate(ids) if j!=i),Fraction(0))
        v.append(base+own_active+gains-exposure)
    return tuple(v)


def dominance(base:Sequence[Fraction],candidate:Sequence[Fraction])->bool:
    if len(base)!=len(candidate) or not base:
        raise ValueError("dominance needs same actor-space")
    return all(b>=a for a,b in zip(base,candidate)) and any(
        b>a for a,b in zip(base,candidate))


def best_response_evidence(state:Sequence[int],g:Mapping[str,Any])->dict:
    x=_state(state,g)
    if not feasible(x,g):
        raise ValueError("starting state is infeasible")
    current=payoff(x,g)
    options=[]
    for i,actor in enumerate(actors(g)):
        dest=list(x);dest[i]=1-x[i]
        dest=tuple(dest)
        allowed=feasible(dest,g)
        diff=payoff(dest,g)[i]-current[i] if allowed else None
        options.append({
            "actor":actor,"alternate_profile":list(dest),
            "unilateral_alternative_feasible":allowed,
            "current_actor_payoff":fmt(current[i]),
            "alternate_actor_payoff":fmt(current[i]+diff) if allowed else None,
            "personal_deviation_gain":fmt(diff) if allowed else None,
            "strictly_profitable":bool(diff is not None and diff>0),
            "best_responses":[x[i],1-x[i]] if diff==0 else
                [1-x[i]] if diff is not None and diff>0 else [x[i]],
        })
    available=sum(item["unilateral_alternative_feasible"] for item in options)
    profitable=sum(item["strictly_profitable"] for item in options)
    strict=available==len(options) and all(
        q(item["personal_deviation_gain"])<0 for item in options)
    return {
        "profile":list(x),"individual_deviations":options,
        "feasible_unilateral_deviations":available,
        "profitable_unilateral_deviations":profitable,
        "pure_nash_under_feasible_unilateral_choices":profitable==0,
        "strict_equilibrium_with_all_deviations_available":strict,
        "nash_may_be_vacuous_if_moves_infeasible":available<len(options),
    }


def all_equilibria(g:Mapping[str,Any])->list[dict]:
    answer=[]
    for x in profiles(g):
        proof=best_response_evidence(x,g)
        if proof["pure_nash_under_feasible_unilateral_choices"]:
            answer.append({
                "profile":list(x),"payoffs":[fmt(v) for v in payoff(x,g)],
                "strict_all_deviations_feasible":
                    proof["strict_equilibrium_with_all_deviations_available"],
                "unilateral_moves_available":proof["feasible_unilateral_deviations"],
            })
    return answer


def best_response_path(g:Mapping[str,Any])->dict:
    """Bounded strict-better-response dynamics, no invented equilibrium oracle."""
    x=_state(g["current"],g)
    seen={x}
    path=[list(x)]
    steps=[]
    bound=2**len(x)*len(x)+1
    for _ in range(bound):
        check=best_response_evidence(x,g)
        profitable=next(
            (item for item in check["individual_deviations"]
             if item["strictly_profitable"]),None)
        if profitable is None:
            return {"path":path,"steps":steps,
                    "status":"NO_PROFITABLE_UNILATERAL_MOVE",
                    "terminates_at_nash":True}
        next_x=tuple(profitable["alternate_profile"])
        steps.append({"actor":profitable["actor"],
                      "gain":profitable["personal_deviation_gain"],
                      "from":list(x),"to":list(next_x)})
        path.append(list(next_x))
        if next_x in seen:
            return {"path":path,"steps":steps,
                    "status":"STRICT_RESPONSE_CYCLE_NOT_NASH",
                    "terminates_at_nash":False}
        seen.add(next_x);x=next_x
    return {"path":path,"steps":steps,"status":"BOUNDED_NOT_CONVERGED",
            "terminates_at_nash":False}


def belief_best_response(g:Mapping[str,Any],value:Any,player:int)->dict:
    """Two-player independent opponent Bernoulli *declared belief*, not C/D."""
    if len(g["actors"])!=2:
        return {"status":"NOT_DEFINED_BEYOND_TWO_AGENT_DECLARED_BELIEF"}
    p=q(value,signed=False)
    if p>1:
        raise ValueError("probability outside [0,1]")
    opponent=1-player
    out=[]
    for action in (0,1):
        profiles_for_beliefs=[]
        for other_action in (0,1):
            state=[0,0];state[player]=action;state[opponent]=other_action
            if not feasible(state,g):
                return {"status":"UNDEFINED_INFEASIBLE_COUNTERFACTUAL",
                        "belief_other_active":fmt(p),"player":actors(g)[player]}
            profiles_for_beliefs.append(payoff(state,g)[player])
        out.append((1-p)*profiles_for_beliefs[0]+p*profiles_for_beliefs[1])
    return {
        "status":"EXPLICIT_FINITE_TWO_ACTOR_BELIEF_ONLY",
        "player":actors(g)[player],"belief_other_active":fmt(p),
        "expected_stay":fmt(out[0]),"expected_move":fmt(out[1]),
        "rational_choices":[int(x) for x in (
            [0] if out[0]>out[1] else [1] if out[1]>out[0] else [0,1])],
        "not_a_probabilistic_claim_about_other_humans":True,
    }


def classify(g:Mapping[str,Any])->dict:
    current=_state(g["current"],g);target=_state(g["target"],g)
    if not feasible(current,g):
        raise ValueError("original current state must be feasible")
    target_possible=feasible(target,g)
    curr=payoff(current,g)
    superior=target_possible and dominance(curr,payoff(target,g))
    proof=best_response_evidence(current,g)
    if not target_possible:
        label="NO_TECHNICALLY_FEASIBLE_TARGET"
    elif not superior:
        label="NO_PARETO_SUPERIOR_TARGET_ON_ACTOR_UTILITIES"
    elif proof["profitable_unilateral_deviations"]>0:
        label="PROFITABLE_UNILATERAL_ESCAPE_NOT_A_NASH_TRAP"
    elif proof["feasible_unilateral_deviations"]==0:
        label="FEASIBILITY_PROTOCOL_TRAP_NOT_STRATEGIC_CHOICE"
    elif proof["feasible_unilateral_deviations"]<len(g["actors"]):
        label="MIXED_FEASIBILITY_AND_CHOICE_BARRIERS"
    elif proof["strict_equilibrium_with_all_deviations_available"]:
        label="STRICT_RATIONAL_COORDINATION_TRAP"
    else:
        label="WEAK_NASH_NO_STRICT_UNILATERAL_GAIN"
    return {
        "classification":label,
        "current":list(current),"target":list(target),
        "current_payoffs":[fmt(x) for x in curr],
        "target_payoffs":[fmt(x) for x in payoff(target,g)]
                         if target_possible else None,
        "target_feasible":target_possible,
        "target_strictly_pareto_dominates_current":superior,
        "current_individual_deviation_proof":proof,
        "all_pure_nash_equilibria":all_equilibria(g),
        "best_response_dynamics":best_response_path(g),
        "public_observable_payoffs_are_stipulated_not_measured":True,
    }


def coordinated_joint_candidate(g:Mapping[str,Any])->dict:
    """Separates technical, actor incentives, governance and means of change.

    This is an *admissibility evaluation*, not a real transaction or consent.
    Transfers are zero-sum in per-actor payoff units and require authority.
    Instrument prices are in another, non-converted dimension.
    """
    current=tuple(g["current"]);target=tuple(g["target"])
    target_feasible=feasible(target,g)
    setup=q(g["joint"]["setup_resource_units"],signed=False)
    use=resources(target,g)+setup
    budget=q(g["resource_budget"],signed=False)
    physical=target_feasible and use<=budget
    original=payoff(current,g)
    after=payoff(target,g) if target_feasible else None
    final=[]
    reservations=[]
    if after is not None:
        for i,actor in enumerate(g["actors"]):
            name=actor["id"]
            amt=(after[i] -
                 q(g["joint"]["burden_payoff_units"][name],signed=False)+
                 q(g["joint"]["transfers_payoff_units"][name]))
            final.append(amt)
            floor=q(actor["reservation_floor"])
            meets=amt>=floor and (
                amt>original[i] if g["joint"]["strict_gain_required"]
                else amt>=original[i])
            reservations.append(meets)
    needs_transfer=any(q(v)!=0 for v in
                       g["joint"]["transfers_payoff_units"].values())
    gov=g["governance"]
    gates={
        "authority":gov["authority"],
        "joint_protocol":gov["joint_protocol"],
        "transfer_authority":gov["transfer_authority"]
        if needs_transfer else "NOT_NEEDED",
        **{"consent_"+name:value for name,value in gov["consents"].items()},
    }
    applicable=[x for x in gates.values() if x!="NOT_NEEDED"]
    if not physical:
        status="MATERIALLY_INFEASIBLE_OR_RESOURCE_OVERDRAFT"
    elif not all(reservations):
        status="VOLUNTARY_PARTICIPATION_NOT_SUPPORTED_BY_PAYOFFS"
    elif "FAIL" in applicable:
        status="BLOCKED_BY_EXPLICIT_GOVERNANCE"
    elif "UNKNOWN" in applicable:
        status="GOVERNANCE_UNKNOWN_CANNOT_COMMIT"
    else:
        status="ADMISSIBLE_UNDER_SYNTHETIC_ASSUMPTIONS"
    arms=[{
        "mechanism":name,
        "same_candidate_and_information_as_peer":True,
        "admissibility":status,
        "instrument_price_SEPARATE_UNITS":fmt(q(g["information_prices"][name],
                                              signed=False)),
        "not_an_architecture_advantage_claim":True,
    } for name in ARMS]
    cost_values=[q(g["information_prices"][name],signed=False) for name in ARMS]
    if cost_values[0]==cost_values[1]:
        cheapest=list(ARMS)
    else:
        cheapest=[ARMS[cost_values.index(min(cost_values))]]
    return {
        "status":status,
        "technical_candidate_feasible":target_feasible,
        "joint_resource_use_including_setup":fmt(use),
        "resource_budget":fmt(budget),
        "actor_payoffs_before":[fmt(v) for v in original],
        "actor_payoffs_after_burden_and_zero_sum_transfers":[fmt(v) for v in final]
            if after is not None else None,
        "individual_reservation_tests":dict(zip(actors(g),reservations)),
        "governance_evidence":gates,
        "explicit_consent_is_not_inferred_from_preferences":True,
        "counterfactual_admission_not_a_real_committed_action":True,
        "coordinators":arms,
        "least_cost_equivalent_capability_instrument":cheapest,
        "cost_does_not_change_physical_outcome":True,
    }


def run_game(g:Mapping[str,Any])->dict:
    validate(g)
    technical=classify(g)
    qualified=coordinated_joint_candidate(g)
    observations=[]
    for p in g["belief_grid"]:
        for index in range(2):
            observations.append(belief_best_response(g,p,index))
    return {
        "case_id":g["id"],"schema":SCHEMA,
        "source_anchor":g["source_anchor"],
        "actor_count":len(g["actors"]),
        "evidence_tier":g["evidence_tier"],
        "finite_feasible_profiles":[list(s) for s in profiles(g)],
        "mechanism":technical,
        "joint_coordination":qualified,
        "belief_controls":observations,
        "physical_resource_units_are_not_summed_with_actor_payoffs":True,
        "information_price_is_not_subtracted_from_actor_utility":True,
    }


def run_manifest(manifest:Mapping[str,Any])->dict:
    if manifest.get("schema")!=MANIFEST:
        raise ValueError("unsupported source study manifest")
    base=manifest.get("base_game")
    if not isinstance(base,dict):
        raise ValueError("base game required")
    validate(base)
    scenarios=manifest.get("scenarios")
    if not isinstance(scenarios,list) or not scenarios:
        raise ValueError("at least one labeled scenario required")
    ids=[x.get("id") for x in scenarios]
    if any(not isinstance(x,str) or not x for x in ids) or len(set(ids))!=len(ids):
        raise ValueError("each scenario must have a unique ID")
    reports=[]
    for s in scenarios:
        game=merge(base,s.get("patch",{}))
        game["id"]=s["id"]
        reports.append(run_game(game))
    source=coupled_trap()
    if source["reachable_without_joint_transition"] or not source["pareto_dominates"]:
        raise AssertionError("original feasibility example changed")
    return {
        "schema":MANIFEST,
        "source_original_coupled_trap":{
            "feasible":source["feasible"],
            "pareto_dominates":source["pareto_dominates"],
            "reachable_without_joint_transition":
                source["reachable_without_joint_transition"],
            "source_ownership":"bounded_traps.coupled_trap unchanged",
        },
        "scenario_count":len(reports),
        "scenarios":reports,
        "research_scope":"SYNTHETIC_FINITE_GAME_CONDITIONAL_CHOICE_AND_AUTHORIZATION",
        "not_proof_of_novel_game_theory_or_empirical_human_choice":True,
    }


def main(argv=None)->int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest",type=Path,default=HERE/"H01_STRATEGIC_STUDY.json")
    parser.add_argument("--output",type=Path)
    args=parser.parse_args(argv)
    result=run_manifest(json.loads(args.manifest.read_text(encoding="utf-8")))
    data=json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+"\n"
    if args.output:
        args.output.write_text(data,encoding="utf-8")
    else:
        print(data,end="")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
