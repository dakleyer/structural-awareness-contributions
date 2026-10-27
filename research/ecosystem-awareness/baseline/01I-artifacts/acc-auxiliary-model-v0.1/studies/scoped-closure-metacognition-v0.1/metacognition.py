"""Finite, query-relative metacognitive qualification of partial nonfungible evidence.

This is NOT a model of the cardinality of unenumerated B/C/D, a decision
oracle, or a subjective/clinical measure of human suffering. The possible
interval claims are sound only conditional on source/regularity assumptions.
"""
from __future__ import annotations

from dataclasses import dataclass
import json
import math
from typing import Optional


class ContractError(ValueError):
    pass


def number(v: float, name: str) -> float:
    if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v):
        raise ContractError(f"{name}: finite numeric value required")
    return float(v)


@dataclass(frozen=True)
class Point:
    """Source-qualified finite observational witness, not a full cloud."""
    claim_id: str
    origin_id: str
    scope: str
    revision: str
    observed_at: int
    x_min: float
    x_max: float
    y_min: float
    y_max: float
    source_attested: bool = True

    def __post_init__(self) -> None:
        if not self.claim_id or not self.origin_id or not self.scope or not self.revision:
            raise ContractError("point identity/scope/revision must be present")
        if type(self.observed_at) is not int or self.observed_at < 0:
            raise ContractError("observed_at must be an integer >= 0")
        for k in ("x_min", "x_max", "y_min", "y_max"):
            number(getattr(self, k), f"point.{k}")
        if self.x_min > self.x_max or self.y_min > self.y_max:
            raise ContractError("point interval reversed")
        if type(self.source_attested) is not bool:
            raise ContractError("source_attested must be boolean")


@dataclass(frozen=True)
class FrontierWitness:
    """A witnessed C exploration direction or D evaluation barrier.

    Does not enumerate all C or D, assert that a particular effect occurs,
    or imply an ROI/probability.
    """
    witness_id: str
    origin_id: str
    scope: str
    kind: str  # C or D
    material_to_question: bool
    grounded: bool
    effective_evaluation_route: bool

    def __post_init__(self) -> None:
        if not self.witness_id or not self.origin_id or not self.scope:
            raise ContractError("frontier identity/scope required")
        if self.kind not in ("C", "D"):
            raise ContractError("kind must be C or D")
        if any(type(v) is not bool for v in (self.material_to_question, self.grounded, self.effective_evaluation_route)):
            raise ContractError("frontier flags must be boolean")
        if self.kind == "C" and (not self.grounded or not self.effective_evaluation_route):
            raise ContractError("a C witness needs a grounded avenue and plausible exploration route")
        if self.kind == "D" and (not self.grounded or self.effective_evaluation_route):
            raise ContractError("a D witness needs a grounded barrier with no effective evaluation route")


@dataclass(frozen=True)
class Frame:
    scope: str
    revision: str
    now: int
    max_age: int
    domain_min: float
    domain_max: float
    lipschitz: Optional[float] = None
    regularity_qualified: bool = False

    def __post_init__(self) -> None:
        if not self.scope or not self.revision:
            raise ContractError("scope and revision required")
        if any(type(v) is not int or v < 0 for v in (self.now, self.max_age)):
            raise ContractError("now/max_age must be nonnegative integers")
        if number(self.domain_min, "domain_min") > number(self.domain_max, "domain_max"):
            raise ContractError("domain must be ordered")
        if self.lipschitz is not None and number(self.lipschitz, "lipschitz") < 0:
            raise ContractError("lipschitz >= 0 required")
        if type(self.regularity_qualified) is not bool:
            raise ContractError("regularity_qualified must be boolean")


@dataclass(frozen=True)
class DecisionQuestion:
    x: float
    threshold: float
    comparison: str = "at_least"  # true iff f(x)>=threshold

    def __post_init__(self) -> None:
        number(self.x, "query x")
        number(self.threshold, "threshold")
        if self.comparison != "at_least":
            raise ContractError("only explicit at_least predicate supported")


def _joint_evidence_status(points: list[Point], lipschitz: float) -> str:
    """Screen joint feasibility before treating the local envelope as evidence.

    For exact coordinates, all pairwise interval inequalities are necessary
    and sufficient for a shared Lipschitz function on the observed points.
    For uncertain coordinates, minimum separation certifies compatibility for
    every allowed coordinate assignment; maximum separation can prove that no
    assignment works. Other cases remain explicitly unestablished.
    """
    robust = True
    for i, a in enumerate(points):
        for b in points[i + 1:]:
            dmin = max(0.0, a.x_min - b.x_max, b.x_min - a.x_max)
            dmax = max(abs(a.x_min - b.x_max), abs(a.x_max - b.x_min))
            gap_ab = a.y_min - b.y_max
            gap_ba = b.y_min - a.y_max
            if gap_ab > lipschitz * dmax or gap_ba > lipschitz * dmax:
                return "INCONSISTENT"
            if gap_ab > lipschitz * dmin or gap_ba > lipschitz * dmin:
                robust = False
    return "CONSISTENT" if robust else "NOT_ESTABLISHED"


def qualify(frame: Frame, query: DecisionQuestion, points: tuple[Point, ...],
            frontiers: tuple[FrontierWitness, ...] = ()) -> dict:
    """Compute a *conservative, conditional* answer bound.

    No world-state truth, future state, hidden function, unknown D population,
    external authorization, or cost is read by this routine.
    """
    if not isinstance(points, tuple) or not isinstance(frontiers, tuple):
        raise ContractError("immutable tuples required for points/frontiers")
    found = []
    rejected = []
    seen: dict[str, Point] = {}
    origins: set[str] = set()
    for p in points:
        if not isinstance(p, Point):
            raise ContractError("points must be Point witnesses")
        if p.claim_id in seen:
            if p != seen[p.claim_id]:
                return _report("SOURCE_CONFLICT", None, None, (), (), (), ("conflicting-claim-id",))
            continue
        seen[p.claim_id] = p
        if p.scope != frame.scope or p.revision != frame.revision or not p.source_attested:
            rejected.append(p.claim_id)
            continue
        if p.observed_at > frame.now or frame.now-p.observed_at > frame.max_age:
            rejected.append(p.claim_id)
            continue
        if p.x_min < frame.domain_min or p.x_max > frame.domain_max:
            rejected.append(p.claim_id)
            continue
        found.append(p)
        origins.add(p.origin_id)
    seen_frontiers = set()
    relevant_d = []
    for w in frontiers:
        if not isinstance(w, FrontierWitness):
            raise ContractError("frontiers must be FrontierWitness witnesses")
        if w.witness_id in seen_frontiers:
            raise ContractError("duplicate frontier witness ID")
        seen_frontiers.add(w.witness_id)
        if w.scope == frame.scope and w.material_to_question and w.kind == "D":
            relevant_d.append(w.witness_id)
    retained = tuple(p.claim_id for p in found)
    rejected_ids = tuple(rejected)
    origin_ids = tuple(sorted(origins))
    if not frame.domain_min <= query.x <= frame.domain_max:
        return _report("OUTSIDE_DECLARED_DOMAIN", None, None, retained, rejected_ids, origin_ids, tuple(relevant_d))
    if not frame.regularity_qualified or frame.lipschitz is None:
        return _report("NO_JUSTIFIED_REGULARITY", None, None, retained, rejected_ids, origin_ids, tuple(relevant_d))
    if not found:
        return _report("NO_RELEVANT_EVIDENCE", None, None, retained, rejected_ids, origin_ids, tuple(relevant_d))
    # For uncertain x_i and uncertain y_i, use the *maximum* possible
    # distance to x_i to give conservative bounds valid for every allowed
    # coordinate. No distribution over unknown coordinates is assumed.
    L = frame.lipschitz
    lows, highs = [], []
    for p in found:
        d = max(abs(query.x-p.x_min), abs(query.x-p.x_max))
        lows.append(p.y_min-L*d)
        highs.append(p.y_max+L*d)
    lo, hi = max(lows), min(highs)
    # Even a tiny empty intersection is not a valid positive certificate.
    if lo > hi:
        return _report("EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT", lo, hi, retained, rejected_ids, origin_ids, tuple(relevant_d))
    joint_status = _joint_evidence_status(found, L)
    if joint_status == "INCONSISTENT":
        return _report("EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT", None, None, retained, rejected_ids, origin_ids, tuple(relevant_d))
    if relevant_d:
        return _report("MATERIAL_D_NOT_EVALUABLE", lo, hi, retained, rejected_ids, origin_ids, tuple(relevant_d))
    if joint_status == "NOT_ESTABLISHED":
        return _report("JOINT_CONSISTENCY_NOT_ESTABLISHED", lo, hi, retained, rejected_ids, origin_ids, ())
    if lo >= query.threshold:
        status="LOCALLY_SUPPORTED_TRUE"
    elif hi < query.threshold:
        status="LOCALLY_SUPPORTED_FALSE"
    else:
        status="UNDETERMINED_FROM_AVAILABLE_EVIDENCE"
    return _report(status, lo, hi, retained, rejected_ids, origin_ids, ())


def _report(status: str, lo: Optional[float], hi: Optional[float],
            retained: tuple[str, ...], rejected: tuple[str, ...],
            origins: tuple[str, ...], material_d: tuple[str, ...]) -> dict:
    return {
        "local_answer_status": status,
        "conditional_answer_bounds": [lo, hi] if lo is not None else None,
        "retained_claim_ids": list(retained),
        "rejected_claim_ids": list(rejected),
        "distinct_declared_origins": list(origins),
        "material_D_witnesses": list(material_d),
        "residual_exterior": "OPEN_NOT_ENUMERATED_OR_PROBABILIZED",
        "status_not_world_oracle": True,
        "source_authenticity_not_cryptographically_verified": True,
        "subjective_suffering": "NOT_MEASURED",
    }


def advisory(status: str, *, owner_authorized: bool, actor_consent: str,
             solidarity_elected: bool, nonwaivable_rights_preserved: bool) -> dict:
    """A limited meta-cognitive advisory; not an actuation authority."""
    if not isinstance(status, str) or type(owner_authorized) is not bool or type(solidarity_elected) is not bool or type(nonwaivable_rights_preserved) is not bool:
        raise ContractError("invalid meta-advisory parameters")
    valid_status = {"SOURCE_CONFLICT", "OUTSIDE_DECLARED_DOMAIN", "NO_JUSTIFIED_REGULARITY",
                    "NO_RELEVANT_EVIDENCE", "EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT",
                    "JOINT_CONSISTENCY_NOT_ESTABLISHED", "MATERIAL_D_NOT_EVALUABLE", "LOCALLY_SUPPORTED_TRUE",
                    "LOCALLY_SUPPORTED_FALSE", "UNDETERMINED_FROM_AVAILABLE_EVIDENCE"}
    if status not in valid_status:
        raise ContractError("unknown evidence status")
    if actor_consent not in ("GRANTED", "DENIED", "UNESTABLISHED"):
        raise ContractError("invalid consent state")
    if not nonwaivable_rights_preserved:
        result="NOT_ADMISSIBLE_RIGHTS"
    elif not owner_authorized:
        result="REQUIRES_REAL_AUTHORIZATION"
    elif actor_consent == "DENIED":
        result="NOT_ADMISSIBLE_DENIED"
    elif actor_consent != "GRANTED":
        result="CONSENT_NOT_ESTABLISHED"
    elif status == "LOCALLY_SUPPORTED_TRUE":
        result="QUALIFIED_POSITIVE_FOR_OWNER"
    elif status == "LOCALLY_SUPPORTED_FALSE":
        result="NEGATIVE_FOR_DECLARED_QUESTION"
    elif status in ("SOURCE_CONFLICT", "EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT"):
        result="REPAIR_INCONSISTENT_EVIDENCE"
    elif solidarity_elected:
        result="VOLUNTARY_UNQUANTIFIED_RISK_REVIEW_ONLY"
    else:
        result="RETAIN_SCOPED_UNDETERMINED"
    return {
        "advisory_status": result,
        "automatic_action": False,
        "truth_of_unknown_effect_computed": False,
        "human_suffering_changed_by_advisory": "NOT_ESTABLISHED",
        "subjective_harm_measured": False,
    }


def structural_exposure(*, actual_development: Optional[float],
                        feasible_development: Optional[float],
                        contribution_endorsed: Optional[bool],
                        external_block: Optional[bool],
                        perspective_indeterminate: Optional[bool],
                        newly_recognized_gap: bool=False) -> dict:
    """Research construct chosen by author, not a psychometric measurement."""
    for name,v in [("contribution_endorsed",contribution_endorsed),
                   ("external_block",external_block),
                   ("perspective_indeterminate",perspective_indeterminate)]:
        if v is not None and type(v) is not bool:
            raise ContractError(f"{name} requires bool or None")
    if type(newly_recognized_gap) is not bool:
        raise ContractError("newly_recognized_gap requires bool")
    if actual_development is None or feasible_development is None or None in (contribution_endorsed,external_block,perspective_indeterminate):
        value=None
        status="NOT_IDENTIFIED"
    else:
        actual=number(actual_development,"actual_development")
        possible=number(feasible_development,"feasible_development")
        if possible<actual:
            raise ContractError("feasible optimum must not be below current in chosen component")
        value=(possible-actual) if contribution_endorsed and external_block and perspective_indeterminate else 0.0
        status="SYNTHETIC_AUTHOR_DEFINED_GAP"
    return {
        "proxy":value,
        "status":status,
        "new_gap_recognized":newly_recognized_gap,
        "subjective_suffering":"NOT_MEASURED",
        "dignity_not_derived_from_productivity":True,
    }


def cost_comparison(*, benefit_if_correct: float, cost_b: float,
                    cost_target: float, cost_full: float, full_information_accessible: bool=True) -> dict:
    """Counterfactual cost ledger under same verified correctness.

    It does not choose whether the unquantified C or D frontier is valuable.
    """
    gain=number(benefit_if_correct,"benefit")
    vals={"B":number(cost_b,"cost_b"),"targeted_conventional":number(cost_target,"cost_target"),"full_reconstruction":number(cost_full,"cost_full")}
    if gain<0 or any(v<0 for v in vals.values()) or type(full_information_accessible) is not bool:
        raise ContractError("positive costs and valid accessible flag required")
    if not full_information_accessible:
        vals["full_reconstruction"]=None
    return {"A_only_conservative_net":0.0,
            "net_if_correct":{k:None if v is None else gain-v for k,v in vals.items()},
            "costs_include_maintenance_and_source_preparation":"ASSUMED_BY_DECLARED_INPUTS",
            "conditional_not_real_world_roi":True}


def synthetic_report() -> dict:
    frame=Frame(scope="orchard.known-window",revision="v1",now=5,max_age=10,domain_min=0,domain_max=2,lipschitz=1,regularity_qualified=True)
    q=DecisionQuestion(x=1,threshold=7)
    claims=(Point("source-1","archive-A","orchard.known-window","v1",4,0,0,9,10),
            Point("source-2","archive-B","orchard.known-window","v1",4,2,2,9,10))
    measured=qualify(frame,q,claims)
    irrelevant_d=(FrontierWitness("w-d","archive-C","orchard.known-window","D",False,True,False),)
    relevant_d=(FrontierWitness("w-d","archive-C","orchard.known-window","D",True,True,False),)
    return {"study":"FINITE_LOCAL_SUFFICIENCY_NOT_OPEN_WORLD_CLOSURE",
            "base":measured,
            "irrelevant_D":qualify(frame,q,claims,irrelevant_d)["local_answer_status"],
            "material_D":qualify(frame,q,claims,relevant_d)["local_answer_status"],
            "advisory":advisory(measured["local_answer_status"],owner_authorized=True,actor_consent="GRANTED",solidarity_elected=False,nonwaivable_rights_preserved=True),
            "costs":cost_comparison(benefit_if_correct=10,cost_b=2.25,cost_target=3,cost_full=32),
            "structural_exposure":structural_exposure(actual_development=4,feasible_development=6,contribution_endorsed=True,external_block=True,perspective_indeterminate=True,newly_recognized_gap=True)}


if __name__=="__main__":
    print(json.dumps(synthetic_report(),ensure_ascii=False,sort_keys=True,indent=2))
