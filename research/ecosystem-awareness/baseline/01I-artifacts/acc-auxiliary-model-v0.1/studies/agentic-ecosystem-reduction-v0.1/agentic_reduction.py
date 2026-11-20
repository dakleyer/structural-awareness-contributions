"""ACC Conscientia: bounded agentic-ecosystem REDUCTION of the social model.

Neither an AI subjective-affect model nor a Turing oracle. The decision-making
part sees only public A, declared role transformations and optional qualified Q.
Hidden true recipient marginal productivity is used ONLY by score_after_plan.
"""
from __future__ import annotations
from dataclasses import dataclass
import json
import math
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
ARMS = ("A_ONLY", "Q_REVIEW_ONLY", "Q_META_PROTOCOL", "CONVENTIONAL_EQUIVALENT_Q",
        "CONVENTIONAL_DIRECTED", "FULL_A_IF_AVAILABLE")
SCHEMA = "ACC-AGENTIC-REDUCTION-v0.1"


def finite(x: Any, name: str) -> float:
    if type(x) not in (int, float) or not math.isfinite(float(x)):
        raise ValueError(name + " must be finite numeric")
    return float(x)


def declared_public(s: dict) -> dict:
    """No world truth. Real agent roles, handoff rights and contracts ARE A.

    The interface exposes current I/O, contract, budget, authorized role modes,
    not the internal marginal of the supplier under different future demands.
    """
    p = s["public"]
    keys = ("scope", "total_resources", "donor_current", "recipient_current",
            "donor_marginal_rate", "donor_minimum", "transfer_maximum",
            "overhead_resources", "metamorph_declared_in_A", "release_declared_in_A",
            "release_consent", "meta_owner_authority", "joint_protocol_available",
            "mission_target", "known_upper_rate_bound", "material_D_for_joint_decision")
    v = {k: p[k] for k in keys}
    v["current_A_total_output"] = p["donor_current"] * p["donor_marginal_rate"] + p["recipient_current"]
    return v


def valid_contract(p: dict) -> None:
    numeric = ("total_resources", "donor_current", "recipient_current", "donor_marginal_rate",
               "donor_minimum", "transfer_maximum", "overhead_resources", "mission_target", "known_upper_rate_bound")
    for k in numeric:
        finite(p[k], k)
    if min(p[k] for k in numeric) < 0:
        raise ValueError("negative physical input")
    if not math.isclose(p["donor_current"] + p["recipient_current"], p["total_resources"], abs_tol=1e-9):
        raise ValueError("physical resource budget inconsistent")
    if p["donor_minimum"] > p["donor_current"] or p["transfer_maximum"] > p["donor_current"]:
        raise ValueError("invalid donor bound")
    if p["overhead_resources"] >= p["transfer_maximum"] and p["transfer_maximum"] > 0:
        raise ValueError("coordination would consume every transferable unit")
    for k in ("metamorph_declared_in_A", "release_declared_in_A", "release_consent", "meta_owner_authority", "joint_protocol_available", "material_D_for_joint_decision"):
        if type(p[k]) is not bool:
            raise ValueError("boolean required: " + k)


def claimed_q(q: dict | None, p: dict, *, time: int = 10) -> tuple[bool, str]:
    """Syntactic validity ONLY, not independent proof that claimed facts are true."""
    if q is None:
        return False, "NO_QUALIFICATION"
    if q["kind"] != "B":
        return False, "C_OR_D_NOT_A_CHARACTERIZED_MARGIN"
    if q["scope"] != p["scope"]:
        return False, "OUT_OF_SCOPE"
    if q["valid_until"] < time:
        return False, "STALE"
    if not q["source_named"]:
        return False, "NO_NAMED_SOURCE"
    if q.get("material_D_for_question", False):
        return False, "MATERIAL_D_NOT_EVALUABLE"
    finite(q["lower_rate"], "lower_rate")
    if not 0 <= q["lower_rate"] <= p["known_upper_rate_bound"] or q["transfer_ceiling"] < 1:
        return False, "UNSUPPORTED_RANGE"
    return True, "APPARENTLY_SCOPED_B_NOT_INDEPENDENTLY_AUTHENTICATED"


def physical_response(s: dict, transfer: int) -> dict:
    """Independent referee after the plan. Same total resource; overhead comes out of it."""
    p = declared_public(s)
    valid_contract(p)
    true_rate = finite(s["truth_private"]["recipient_incremental_rate"], "hidden truth")
    if true_rate < 0 or true_rate > p["known_upper_rate_bound"]:
        raise ValueError("world violates declared public rate upper bound")
    if transfer < 0 or type(transfer) is not int or transfer > min(p["transfer_maximum"], p["donor_current"]-p["donor_minimum"]):
        raise ValueError("illegal amount of donor resources")
    if transfer and not p["metamorph_declared_in_A"]:
        raise ValueError("metamorphosis not in public A capability")
    overhead = p["overhead_resources"] if transfer else 0.0
    if transfer and transfer <= overhead:
        raise ValueError("no positive recipient resource after coordination")
    donor = p["donor_current"] - transfer
    recipient = p["recipient_current"] + transfer - overhead
    if not math.isclose(donor + recipient + overhead, p["total_resources"], abs_tol=1e-8):
        raise AssertionError("resource creation or disappearance")
    # Only the incremental recipient allocation benefits from its mode change.
    output = donor*p["donor_marginal_rate"] + p["recipient_current"] + (transfer-overhead)*true_rate if transfer else p["current_A_total_output"]
    return {"donor_resources_after":round(donor,4), "recipient_resources_after":round(recipient,4),
            "coordination_resources_spent":round(overhead,4),"total_resources_same":p["total_resources"],
            "output":round(output,4),"mission_target_met":output+1e-9>=p["mission_target"]}


def source_proposed_near_gain(p: dict, q: dict | None) -> tuple[float | None, int, str]:
    """Visible *conditional lower bound*; not a known true world or a full optimum."""
    valid, reason=claimed_q(q,p)
    if not valid:
        return None,0,reason
    if not p["metamorph_declared_in_A"]:
        return None,0,"NO_DECLARED_ROLE_TRANSFORMATION"
    cap = int(min(p["transfer_maximum"], p["donor_current"]-p["donor_minimum"], q["transfer_ceiling"]))
    if cap < 1:
        return 0.0,0,"NO_SPARE_TRANSFER_WITHIN_ROLE"
    candidates=[]
    for k in range(1,cap+1):
        net_recipient = k-p["overhead_resources"]
        if net_recipient <= 0:
            continue
        lower_gain = net_recipient*q["lower_rate"]-k*p["donor_marginal_rate"]
        candidates.append((round(lower_gain,6),k))
    if not candidates:
        return 0.0,0,"NO_POSITIVE_RESOURCE_TRANSFER"
    gain,amount=max(candidates)
    return max(0.0,gain),amount,"COND_BOUND_ONLY_SOURCE_NOT_AUTHENTICATED"


def plan_public(p: dict, q: dict | None, *, arm: str, directed: dict, full: dict) -> dict:
    """Public planner cannot access `truth_private`. Q/data-source protocols are input."""
    valid_contract(p)
    if arm not in ARMS:
        raise ValueError("unknown arm")
    cost=0.0; method="A_ONLY"; selected_q=q
    if arm=="A_ONLY":
        return {"arm":arm,"transfer":0,"status":"KEEP_A","instrument_cost":0.0,
                "conditional_near_gain":None,"qualified_proposal":False,"evidence":"A_ONLY"}
    # A material open-world witness shared through the ecosystem contract must
    # constrain all planners, not just the candidate with a particular brand.
    if p["material_D_for_joint_decision"]:
        return {"arm":arm,"transfer":0,"status":"MATERIAL_D_UNASSESSED_SHARED_GATE",
                "instrument_cost":0.0,"conditional_near_gain":None,
                "qualified_proposal":False,"evidence":"SHARED_MATERIAL_D_WITNESS"}
    if arm in ("Q_REVIEW_ONLY", "Q_META_PROTOCOL", "CONVENTIONAL_EQUIVALENT_Q"):
        cost=finite((q or {}).get("cost",0),"Q cost")
        if arm=="CONVENTIONAL_EQUIVALENT_Q":
            cost=finite(directed.get("equivalent_Q_cost",cost),"equivalent Q cost")
        method="SOURCE_Q_PARTIAL"
    elif arm=="CONVENTIONAL_DIRECTED":
        if not directed.get("available"):
            return {"arm":arm,"transfer":0,"status":"DIRECTED_NOT_AVAILABLE","instrument_cost":0.0,
                    "conditional_near_gain":None,"qualified_proposal":False,"evidence":"NO_DIRECTED_SIGNAL"}
        cost=finite(directed["cost"],"directed cost")
        selected_q={"kind":"B","scope":p["scope"],"valid_until":99,"source_named":True,
                    "lower_rate":finite(directed["measured_rate"],"directed rate"),
                    "transfer_ceiling":int(p["transfer_maximum"]),"material_D_for_question":False}
        method="CONVENTIONAL_DIRECTED_INSTRUMENT"
    elif arm=="FULL_A_IF_AVAILABLE":
        if not full.get("available"):
            return {"arm":arm,"transfer":0,"status":"FULL_A_NOT_AVAILABLE","instrument_cost":0.0,
                    "conditional_near_gain":None,"qualified_proposal":False,"evidence":"NO_FULL_A"}
        cost=finite(full["cost"],"full cost")
        # A rigorous public upper bound avoids buying clearly uneconomic full reconstruction.
        max_physical_gain=(p["transfer_maximum"]-p["overhead_resources"])*p["known_upper_rate_bound"]-p["transfer_maximum"]*p["donor_marginal_rate"]
        if cost>=max(0.0,max_physical_gain):
            return {"arm":arm,"transfer":0,"status":"FULL_A_TOO_COSTLY_TO_ACQUIRE","instrument_cost":0.0,
                    "conditional_near_gain":None,"qualified_proposal":False,"evidence":"COST_BOUND_ON_A"}
        selected_q={"kind":"B","scope":p["scope"],"valid_until":99,"source_named":True,
                    "lower_rate":finite(full["fully_measured_rate"],"full rate"),
                    "transfer_ceiling":int(p["transfer_maximum"]),"material_D_for_question":False}
        method="FULL_A_REAL_INSTRUMENT_ASSUMED"
    if cost < 0:
        raise ValueError("negative price")
    near,amount,quality=source_proposed_near_gain(p,selected_q)
    if near is None or near<=0:
        return {"arm":arm,"transfer":0,"status":quality,"instrument_cost":cost,
                "conditional_near_gain":near,"qualified_proposal":False,"evidence":method}
    if arm=="Q_REVIEW_ONLY":
        return {"arm":arm,"transfer":0,"status":"NEARER_CANDIDATE_VISIBLE_NOT_TRANSFERRED","instrument_cost":cost,
                "conditional_near_gain":near,"qualified_proposal":True,"evidence":method}
    # 1) Metamorphosis is predefined in A; 2) no actor is forced to release; 3) meta owner must be empowered.
    for key,status in (("release_declared_in_A","DONOR_RELEASE_NOT_IN_CAPABILITIES"),
                       ("release_consent","DONOR_CONSENT_NOT_GIVEN"),
                       ("meta_owner_authority","META_AUTHORITY_MISSING"),
                       ("joint_protocol_available","NO_JOINT_TRANSFER_PROTOCOL")):
        if not p[key]:
            return {"arm":arm,"transfer":0,"status":status,"instrument_cost":cost,
                    "conditional_near_gain":near,"qualified_proposal":True,"evidence":method}
    if selected_q.get("material_D_for_question",False):
        return {"arm":arm,"transfer":0,"status":"MATERIAL_D_UNKNOWN","instrument_cost":cost,
                "conditional_near_gain":None,"qualified_proposal":False,"evidence":method}
    if near<=cost:
        return {"arm":arm,"transfer":0,"status":"NO_NET_GAIN_AFTER_INFORMATION_COST","instrument_cost":cost,
                "conditional_near_gain":near,"qualified_proposal":True,"evidence":method}
    return {"arm":arm,"transfer":amount,"status":"TRANSFER_PROPOSED_AND_AUTHORIZED",
            "instrument_cost":cost,"conditional_near_gain":near,"qualified_proposal":True,"evidence":method}


def score_after_plan(s: dict, plan: dict) -> dict:
    """Only this scorer knows true rate and full technical optimum for audit."""
    p=declared_public(s)
    out=physical_response(s,plan["transfer"])
    maxk=int(min(p["transfer_maximum"],p["donor_current"]-p["donor_minimum"]))
    # Only capabilities that are publicly predeclared are technically admissible.
    admissible_moves=[k for k in range(maxk+1) if k == 0 or k > p["overhead_resources"]]
    possible=[physical_response(s,k)["output"] for k in admissible_moves] if p["metamorph_declared_in_A"] else [p["current_A_total_output"]]
    best=max(possible)
    current=p["current_A_total_output"]
    gap=max(0.0,best-out["output"])
    near=plan["conditional_near_gain"]
    awareness=near if (plan["transfer"]==0 and near is not None and near>0) else 0.0
    labelled_q=(s.get("Q") or {}).get("lower_rate")
    claim_true = (labelled_q is None or labelled_q <= s["truth_private"]["recipient_incremental_rate"])
    # Structural indicators are not human emotion or autonomous AI experience.
    return {"plan":plan,"observed_by_referee_only":out,
        "mission_output_gap_to_same_budget_technical_optimum":round(gap,4),
        "technical_optimum_referee_only":round(best,4),
        "mission_output_before":round(current,4),
        "mission_net_value_after_information_cost":round(out["output"]-plan["instrument_cost"],4),
        "second_order_claimed_but_blocked_lower_bound":round(awareness,4) if awareness else 0.0,
        "source_B_claim_supported_by_lab_truth":claim_true,
        "experience_of_suffering":"NOT_MEASURED_NOT_ATTRIBUTED_TO_AI",
        "residual_C_D_exhaustiveness":"NOT_CLOSED",
        "evidence_level":"SYNTHETIC_ONLY"}


def run_case(s: dict) -> dict:
    p=declared_public(s)
    valid_contract(p)
    cases={}
    for arm in ARMS:
        plan=plan_public(p,s.get("Q"),arm=arm,directed=s["directed"],full=s["full_A"])
        cases[arm]=score_after_plan(s,plan)
    return {"id":s["id"],"source_ids":s["source_ids"],"public_A":p,
            "truth_PRIVATE_FOR_SCORING_ONLY":s["truth_private"],
            "arms":cases,"evidence":"DESIGNED_SYNTHETIC_CASE_NOT_REAL_DEPLOYMENT"}


def report() -> dict:
    cases=json.loads((HERE/"CASES.json").read_text(encoding="utf-8"))
    if cases["schema"]!=SCHEMA:
        raise ValueError("unsupported fixture schema")
    ids=[s["id"] for s in cases["cases"]]
    if len(ids)!=len(set(ids)):
        raise ValueError("duplicate case ID")
    rows=[run_case(s) for s in cases["cases"]]
    totals={arm:{"acted":sum(row["arms"][arm]["plan"]["transfer"]>0 for row in rows),
         "nonzero_technical_gap":sum(row["arms"][arm]["mission_output_gap_to_same_budget_technical_optimum"]>0 for row in rows),
         "net_value_synthetic":round(sum(row["arms"][arm]["mission_net_value_after_information_cost"] for row in rows),3),
         "information_cost_synthetic":round(sum(row["arms"][arm]["plan"]["instrument_cost"] for row in rows),3),
         "second_order_claim_visible_but_blocked":sum(row["arms"][arm]["second_order_claimed_but_blocked_lower_bound"]>0 for row in rows)} for arm in ARMS}
    return {"schema_version":SCHEMA,"cases":len(rows),"policies":list(ARMS),"policy_decisions":len(rows)*len(ARMS),
            "scoped_results":rows,"summary":totals,
            "disclaimer":"Finite synthetic agentic reduction. No measured human distress, no observed vendor agent behavior, no real costs, no Turing oracle, no globally closed B/C/D."}

if __name__ == "__main__":
    print(json.dumps(report(),sort_keys=True,ensure_ascii=False,indent=2))
