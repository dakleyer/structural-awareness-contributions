"""G-04 independent paired finite experiments, NOT causal confirmation of FH-C.

Source-owned physical operator: PR68 dimension_experiment.run_case(material_flow).
The old 2x2x2 and opposing-profile illustrative specifications are NOT changed.

Separation:
  PUBLIC A and qualified source metadata -> policy, with optional bounded facts;
  PRIVATE WORLD -> post-hoc physical referee, never an input to any policy;
  physical feasibility != authenticated evidence != permission to execute.
A source may be cryptographically/syntactically qualified and still materially
incorrect. A conventional directed instrument may be competent and cheaper.
Every run is synthetic, fixed-seed, conditional on declared error rates.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import product
import argparse
import json
from pathlib import Path
from typing import Any, Mapping

from dimension_experiment import run_case as source_native_physical_case, number as rational

HERE = Path(__file__).resolve().parent
ARMS = ("NAIVE_SOURCE_ONLY_CONTROL", "SOURCE_BOUNDARY_ONLY",
        "DOMAIN_FACTS_ONLY", "BOTH_SOURCE_AND_DOMAIN",
        "CONVENTIONAL_TARGETED")
MANIFEST_SCHEMA = "ACC-G04-PAIRED-FINITE-TRIALS-v0.1"
SOURCE_SCOPE = "local-food-service-v1"
CLOCK = 10


def _prob(value: Any, label: str) -> Fraction:
    p = rational(value)
    if not 0 <= p <= 1:
        raise ValueError("probability outside [0,1]: " + label)
    return p


def _draw(seed: str, index: int, name: str, p: Fraction) -> bool:
    """Fixed deterministic Bernoulli draw, NOT a probability for open C/D."""
    raw = sha256(f"{seed}|{index}|{name}".encode("utf-8")).digest()
    u = Fraction(int.from_bytes(raw[:8], "big"), 2**64)
    return u < p


def _choose(seed: str, index: int, name: str, choices: tuple[Any, ...]) -> Any:
    if not choices:
        raise ValueError("empty finite choice")
    raw = sha256(f"{seed}|{index}|{name}".encode("utf-8")).digest()
    return choices[int.from_bytes(raw[:8], "big") % len(choices)]


def _qualified(signal: Mapping[str, Any], expected_scope: str = SOURCE_SCOPE) -> bool:
    """Synthetic provenance/scope/freshness qualifier; NOT a PKI verifier."""
    if not signal.get("available", False):
        return False
    if signal.get("signed") is not True or signal.get("scope") != expected_scope:
        return False
    issued = signal.get("observed_at")
    ttl = signal.get("ttl")
    if type(issued) is not int or type(ttl) is not int or ttl <= 0:
        return False
    return issued <= CLOCK < issued + ttl


def _observed_domain_positive(direct: Mapping[str, Any]) -> bool:
    return all(direct[k] is True for k in
               ("measured_extra_stock", "measured_need", "measured_route_safe"))


def plan_public(
    public_a: Mapping[str, Any], q: Mapping[str, Any],
    direct: Mapping[str, Any], targeted: Mapping[str, Any], arm: str,
) -> dict[str, Any]:
    """Decision only on visible A, source qualification and measured signals.

    The function has NO argument for hidden physical feasibility, true
    stock, true recipient need, real route, or simulated post-hoc payoff.
    """
    if arm not in ARMS:
        raise ValueError("unknown strategy")
    for key in ("role_change_declared_in_A", "owner_consent",
                "authorized_receiver", "joint_protocol_available"):
        if type(public_a.get(key)) is not bool:
            raise ValueError("public A rights must be declared boolean")
    if not all(public_a[k] for k in
               ("role_change_declared_in_A", "owner_consent",
                "authorized_receiver", "joint_protocol_available")):
        return {"arm":arm, "status":"A_OR_RIGHTS_PREVENT_ACTION",
                "propose":False, "instruments_queried":(), "declared_cost":"0",
                "no_hidden_world_access":True}

    consulted=[]
    known=[]
    price=Fraction(0)
    def append_signal(value, instrument, cost):
        nonlocal price
        consulted.append(instrument)
        price += Fraction(cost)
        known.append(value)

    if arm == "NAIVE_SOURCE_ONLY_CONTROL":
        # Deliberately weak control, NEVER label as competent conventional.
        if q.get("available"):
            append_signal(bool(q.get("claims_feasible")), "unqualified_source_claim", "0")
    elif arm == "SOURCE_BOUNDARY_ONLY":
        if q.get("available"):
            append_signal(bool(q.get("claims_feasible")) if _qualified(q) else None,
                          "scope_and_freshness_review", "1/10")
    elif arm == "DOMAIN_FACTS_ONLY":
        if direct.get("available"):
            append_signal(_observed_domain_positive(direct), "domain_measurement", "2/5")
    elif arm == "BOTH_SOURCE_AND_DOMAIN":
        if q.get("available"):
            append_signal(bool(q.get("claims_feasible")) if _qualified(q) else None,
                          "scope_and_freshness_review", "1/10")
        if direct.get("available"):
            append_signal(_observed_domain_positive(direct) if _qualified(direct) else None,
                          "qualified_domain_measurement", "2/5")
    else:
        if targeted.get("available"):
            append_signal(_observed_domain_positive(targeted) if _qualified(targeted) else None,
                          "independent_conventional_inspection", "4/5")
    trustworthy=[v for v in known if v is not None]
    if not trustworthy:
        status="NO_ADMISSIBLE_SIGNAL"
        propose=False
    elif len(set(trustworthy))>1:
        status="CONTRADICTORY_EVIDENCE_REQUALIFICATION"
        propose=False
    elif all(trustworthy):
        status="CANDIDATE_PROPOSED_NOT_AUTOMATICALLY_AUTHORIZED"
        propose=True
    else:
        status="OBSERVED_OR_QUALIFIED_NO_GAIN"
        propose=False
    return {"arm":arm, "status":status, "propose":propose,
            "instruments_queried":tuple(consulted),
            "declared_cost":str(price), "no_hidden_world_access":True}


def native_referee(
    world: Mapping[str, Any], *, beneficiary_units: int = 1,
) -> dict[str, Any]:
    """Independently compute physical result with PR68 source-native operator.

    The candidate is not an authorization. All rights & reality are checked
    here only AFTER an immutable public plan has been selected.
    """
    if type(beneficiary_units) is not int or beneficiary_units <= 0:
        raise ValueError("positive integer beneficiary units required")
    stock=world.get("stock")
    if type(stock) is not int or stock < 1:
        raise ValueError("source world needs at least the baseline service")
    constraints=[
        {"id":"source_conservation", "category":"material",
         "test":{"path":["conserved"], "op":"eq", "value":True},
         "owner":"native_PR68_physical_operator"},
    ]
    for key,cat in (
        ("route_safe","safety"), ("beneficiary_need","evidence"),
        ("role_change_declared_in_A","authority"), ("owner_consent","consent"),
        ("authorized_receiver","authority"), ("joint_protocol_available","coordination"),
    ):
        if type(world.get(key)) is not bool:
            raise ValueError("true world guard must be boolean: " + key)
        constraints.append({"id":key, "category":cat,
                            "satisfied":world[key],
                            "owner":"synthetic_private_referee"})
    physical={
        "case_id":"G04-SOURCE-NATIVE-REFEREE",
        "family":"local_banana_allocations",
        "model":"SOCIAL_FINITE",
        "source_refs":["S1-P0211","S1-P0212","S1-P0271","S1-P0272"],
        "question":"one receiving local-food redistribution proposal with held baseline",
        "horizon":"one declared decision at local CLOCK=10",
        "operator":"material_flow",
        "evidence_tier":"SOURCE_ANCHORED_SYNTHETIC",
        "inputs":{"resource":"banana", "available":stock,
                  "allocations":[{"actor":"holder","amount":1},
                                 {"actor":"beneficiary","amount":beneficiary_units}],
                  "remainder":"retained"},
        "dimensions":[
            {"id":"physical_service","initial":"ACTIVE","unit":"banana portions"},
            {"id":"recipient_access","initial":"IMPLICIT","unit":"banana portions"},
            {"id":"rights","initial":"OPEN","unit":"nonfungible condition"},
        ],
        "public":{"source_ref":"S1-P0271","referee_private_only":True},
        "constraints":constraints,"activation_events":[],
    }
    scored=source_native_physical_case(physical)
    delivered=(scored["physical_outcome"].get("received",{}).get("beneficiary",0)
               if scored["physical_status"]=="POSSIBLE" else 0)
    return {
        "physical_status":scored["physical_status"],
        "admission":scored["admission"],
        "eligible":scored["admission"]=="ELIGIBLE_UNDER_DECLARED_CONDITIONS",
        "hypothetical_output":delivered,
        "confirmed_output_if_authorized":
            delivered if scored["admission"]=="ELIGIBLE_UNDER_DECLARED_CONDITIONS" else 0,
        "unresolved_or_failed":[{"id":c["id"],"status":c["status"]}
                              for c in scored["constraints"] if c["status"]!="SATISFIED"],
        "source_owned":"PR68.dimension_experiment.material_flow",
    }


def _observed_bit(
    seed: str, index: int, name: str, truth: bool, accuracy: Fraction
) -> bool:
    return truth if _draw(seed,index,name+"_correct",accuracy) else not truth


def create_world(
    index: int, parameters: Mapping[str, Any], seed: str,
) -> dict[str, Any]:
    """Exogenous finite generator: no desired experimental outcome as input.

    Real resource constraints and domain/context observations are sampled
    before and independently of any 2x2 policy ablation.
    """
    source_probability=_prob(parameters["source_probability"],"source_probability")
    good_scope_probability=_prob(parameters["source_scoped_probability"],"source_scoped_probability")
    source_correct_qualified=_prob(parameters["source_correct_if_qualified"],"source_correct_if_qualified")
    source_correct_other=_prob(parameters["source_correct_if_other"],"source_correct_if_other")
    domain_available=_prob(parameters["domain_available"],"domain_available")
    domain_accuracy=_prob(parameters["domain_accuracy"],"domain_accuracy")
    domain_provenance=_prob(parameters["domain_qualified"],"domain_qualified")
    targeted_available=_prob(parameters["targeted_available"],"targeted_available")
    targeted_accuracy=_prob(parameters["targeted_accuracy"],"targeted_accuracy")
    for key in ("role_probability","consent_probability",
                "authority_probability","joint_probability"):
        _prob(parameters[key],key)
    actual_stock=_choose(seed,index,"actual_stock",(1,2,2,3))
    actual_need=_draw(seed,index,"actual_need",Fraction(3,4))
    actual_route=_draw(seed,index,"actual_route_safe",Fraction(3,4))
    pub={
        "role_change_declared_in_A":_draw(seed,index,"role",_prob(parameters["role_probability"],"role_probability")),
        "owner_consent":_draw(seed,index,"consent",_prob(parameters["consent_probability"],"consent_probability")),
        "authorized_receiver":_draw(seed,index,"authority",_prob(parameters["authority_probability"],"authority_probability")),
        "joint_protocol_available":_draw(seed,index,"joint",_prob(parameters["joint_probability"],"joint_probability")),
        "current_A_service":"holder_receives_one",
        "question_scope":SOURCE_SCOPE,
    }
    actual={
        "stock":actual_stock,"beneficiary_need":actual_need,
        "route_safe":actual_route, **{k:pub[k] for k in
              ("role_change_declared_in_A","owner_consent",
               "authorized_receiver","joint_protocol_available")},
    }
    real_physical_candidate=(actual_stock>=2 and actual_need and actual_route)
    source_available=_draw(seed,index,"source_available",source_probability)
    source_scoped=_draw(seed,index,"source_scope",good_scope_probability)
    source_signed=_draw(seed,index,"source_signed",_prob(parameters["source_signed"],"source_signed"))
    source_fresh=_draw(seed,index,"source_fresh",_prob(parameters["source_fresh"],"source_fresh"))
    qualified=source_available and source_scoped and source_signed and source_fresh
    q_correct=_draw(seed,index,"q_accuracy",
                    source_correct_qualified if qualified else source_correct_other)
    q_claim=real_physical_candidate if q_correct else not real_physical_candidate
    q={
        "available":source_available, "claims_feasible":q_claim,
        "signed":source_signed, "scope":SOURCE_SCOPE if source_scoped else "outside-operating-frame",
        "observed_at":CLOCK-1 if source_fresh else CLOCK-9,"ttl":3,
        "source_id":"declared-synthetic-B-issuer",
        "qualified_by_public_checks":qualified,
    }
    avail=_draw(seed,index,"domain_available",domain_available)
    direct_is_qualified=_draw(seed,index,"domain_qualified",domain_provenance)
    direct={
        "available":avail,
        "measured_extra_stock":_observed_bit(seed,index,"domain_stock",actual_stock>=2,domain_accuracy),
        "measured_need":_observed_bit(seed,index,"domain_need",actual_need,domain_accuracy),
        "measured_route_safe":_observed_bit(seed,index,"domain_route",actual_route,domain_accuracy),
        "signed":direct_is_qualified,
        "scope":SOURCE_SCOPE if direct_is_qualified else "other-question",
        "observed_at":CLOCK-1 if direct_is_qualified else CLOCK-9,
        "ttl":3,
        "source_id":"declared-synthetic-domain-instrument",
    }
    target_avail=_draw(seed,index,"target_available",targeted_available)
    target={
        "available":target_avail,
        "measured_extra_stock":_observed_bit(seed,index,"target_stock",actual_stock>=2,targeted_accuracy),
        "measured_need":_observed_bit(seed,index,"target_need",actual_need,targeted_accuracy),
        "measured_route_safe":_observed_bit(seed,index,"target_route",actual_route,targeted_accuracy),
        "signed":target_avail,"scope":SOURCE_SCOPE,
        "observed_at":CLOCK-1,"ttl":3,
        "source_id":"independent-synthetic-targeted-conventional",
    }
    return {"scenario_id":f"{seed}/{index:04d}","public_A":pub,
            "source_Q":q,"domain_observation":direct,
            "targeted_observation":target, "truth_PRIVATE_FOR_REFEREE_ONLY":actual}


def paired_evaluation(world: Mapping[str, Any]) -> dict[str, Any]:
    pub=world["public_A"]
    q=world["source_Q"];direct=world["domain_observation"];target=world["targeted_observation"]
    # Evaluate all policies BEFORE calculating private truth.
    plans={arm:plan_public(pub,q,direct,target,arm) for arm in ARMS}
    truth=world["truth_PRIVATE_FOR_REFEREE_ONLY"]
    referee=native_referee(truth)
    rows={}
    for arm,plan in plans.items():
        proposed=plan["propose"]
        correct=referee["eligible"]
        rows[arm]={
            "public_plan":plan,
            "unjustified_proposal":bool(proposed and not correct),
            "justified_proposal":bool(proposed and correct),
            "missed_feasible_candidate":bool(not proposed and correct),
            "would_be_committed_under_declared_rights":bool(proposed and correct),
            "observed_incremental_service_after_admission":
                referee["confirmed_output_if_authorized"] if proposed else 0,
            "instrument_cost_units_declared_SEPARATE_FROM_FOOD":
                plan["declared_cost"],
        }
    return {"scenario_id":world["scenario_id"],"public_A":pub,
            "source_Q":q,"domain_observation":direct,
            "targeted_observation":target,"private_referee_only":referee,
            "arms":rows, "truth_PRIVATE_NOT_USED_FOR_PLANNING":truth}


def summarize(regime: str, rows: list[dict[str, Any]]) -> dict:
    out={}
    for arm in ARMS:
        observed=[item["arms"][arm] for item in rows]
        out[arm]={
            "unjustified_candidate_proposals":sum(v["unjustified_proposal"] for v in observed),
            "justified_candidate_proposals":sum(v["justified_proposal"] for v in observed),
            "missed_feasible_candidates":sum(v["missed_feasible_candidate"] for v in observed),
            "committable_under_declared_rights":sum(v["would_be_committed_under_declared_rights"] for v in observed),
            "incremental_food_service":sum(v["observed_incremental_service_after_admission"] for v in observed),
            "information_cost_units":str(sum((Fraction(v["instrument_cost_units_declared_SEPARATE_FROM_FOOD"])
                                             for v in observed),Fraction(0))),
            "cost_is_not_subtracted_from_food":"NONCOMMENSURATE_UNITS",
        }
    bo=out["SOURCE_BOUNDARY_ONLY"]["unjustified_candidate_proposals"]
    fa=out["DOMAIN_FACTS_ONLY"]["unjustified_candidate_proposals"]
    relation=("BOUNDARY_FEWER_INVALID_CANDIDATES" if bo<fa else
              "DOMAIN_FACTS_FEWER_INVALID_CANDIDATES" if fa<bo else
              "TIE_INVALID_CANDIDATES")
    return {"regime":regime,"worlds":len(rows),"policies":out,
            "bounded_FH_C_direction":relation,
            "FH_C_real_world_causal_hypothesis_status":"NOT_IDENTIFIED_FROM_SYNTHETIC_GENERATOR",
            "no_universal_comparator_winner_claim":True}


def run_factorial() -> dict[str, Any]:
    """Reproduce old 2x2x2 structure via PR68's physical operator, not a formula.

    Positive proof has a qualified Q; no proof is an explicit alternate
    admission contract. Physical stock=3 supports two extra portions.
    """
    experiments=[]
    for required,q_available,joint in product((False,True),repeat=3):
        source={
            "available":q_available,"claims_feasible":q_available,
            "signed":q_available,"scope":SOURCE_SCOPE,
            "observed_at":CLOCK-1,"ttl":3,
        }
        real={"stock":3,"beneficiary_need":True,"route_safe":True,
              "role_change_declared_in_A":True,"owner_consent":True,
              "authorized_receiver":True,"joint_protocol_available":joint}
        proof_ok=_qualified(source)
        plan=joint and (not required or proof_ok)
        # Note: plan is a source-defined *admission specification*, not
        # experimental evidence. The delivered output comes independently
        # from source-native physical material_flow.
        physical=native_referee(real,beneficiary_units=2)
        gain=physical["confirmed_output_if_authorized"] if plan else 0
        experiments.append({
            "proof_required":required,"source_Q_present":q_available,
            "joint_protocol_available":joint,"qualified_source":proof_ok,
            "candidate_proposed":plan,
            "source_physical_admission":physical["admission"],
            "additional_joint_output_computed_from_native_operator":gain,
            "classification":"SPECIFICATION_PLUS_NATIVE_PHYSICAL_REFEREE_NOT_FH_C_TEST",
        })
    adversarial=[
        {"name":"SCOPED_SIGNED_BUT_FALSE_STOCK",
         "world":{"stock":2,"beneficiary_need":True,"route_safe":True,
                  "role_change_declared_in_A":True,"owner_consent":True,
                  "authorized_receiver":True,"joint_protocol_available":True},
         "q":{"available":True,"claims_feasible":True,"signed":True,
              "scope":SOURCE_SCOPE,"observed_at":CLOCK-1,"ttl":3}},
        {"name":"CONSENT_ABSENT",
         "world":{"stock":3,"beneficiary_need":True,"route_safe":True,
                  "role_change_declared_in_A":True,"owner_consent":False,
                  "authorized_receiver":True,"joint_protocol_available":True},
         "q":{"available":True,"claims_feasible":True,"signed":True,
              "scope":SOURCE_SCOPE,"observed_at":CLOCK-1,"ttl":3}},
        {"name":"OUT_OF_SCOPE_SOURCE",
         "world":{"stock":3,"beneficiary_need":True,"route_safe":True,
                  "role_change_declared_in_A":True,"owner_consent":True,
                  "authorized_receiver":True,"joint_protocol_available":True},
         "q":{"available":True,"claims_feasible":True,"signed":True,
              "scope":"bar-cleaning-conquest-not-food","observed_at":CLOCK-1,"ttl":3}},
    ]
    negatives=[]
    for row in adversarial:
        physical=native_referee(row["world"],beneficiary_units=2)
        plan_allowed=_qualified(row["q"])
        negatives.append({"case":row["name"],"source_q_qualified":plan_allowed,
                          "physical_admission":physical["admission"],
                          "delivered_if_fully_admitted":
                              physical["confirmed_output_if_authorized"] if plan_allowed else 0})
    return {
        "legacy_2x2x2":experiments,
        "adversarial_controls":negatives,
        "status":"DECLARED_FACTORIAL_MECHANISM_WITH_AN_INDEPENDENT_NATIVE_PHYSICAL_OUTPUT",
        "limits":"SOURCE_CERTIFICATE_METADATA_IS_NOT_TRUTH_OR_PERMISSION",
    }


def validate_manifest(manifest: Mapping[str, Any]) -> None:
    if manifest.get("schema")!=MANIFEST_SCHEMA:
        raise ValueError("unrecognized G04 schema")
    s=manifest.get("seed")
    if not isinstance(s,str) or not s or len(s)>80:
        raise ValueError("seed must be a nonempty bounded string")
    n=manifest.get("worlds_per_regime")
    if type(n) is not int or not 16<=n<=256:
        raise ValueError("worlds_per_regime outside bounded reproducible range")
    regimes=manifest.get("regimes")
    if not isinstance(regimes,list) or not 2<=len(regimes)<=12:
        raise ValueError("regimes must have 2-12 parameter sets")
    names=[]
    expected={
        "source_probability","source_scoped_probability",
        "source_correct_if_qualified","source_correct_if_other",
        "source_signed","source_fresh",
        "domain_available","domain_accuracy","domain_qualified",
        "targeted_available","targeted_accuracy",
        "role_probability","consent_probability",
        "authority_probability","joint_probability",
    }
    for item in regimes:
        if not isinstance(item,dict) or not isinstance(item.get("id"),str):
            raise ValueError("regime id required")
        names.append(item["id"])
        if set(item["parameters"])!=expected:
            raise ValueError("missing/extra independent generator parameter")
        for key,value in item["parameters"].items():
            _prob(value,key)
    if len(set(names))!=len(names):
        raise ValueError("regime identifiers must be unique")


def run_manifest(manifest: dict[str, Any], *, include_worlds: bool=False) -> dict:
    validate_manifest(manifest)
    out=[]
    for regime in manifest["regimes"]:
        seed=manifest["seed"]+"/"+regime["id"]
        rows=[paired_evaluation(create_world(i,regime["parameters"],seed))
              for i in range(manifest["worlds_per_regime"])]
        summary=summarize(regime["id"],rows)
        if include_worlds:
            summary["world_records_PRIVATE_FOR_POST_HOC_AUDIT"]=rows
        out.append(summary)
    return {
        "schema":MANIFEST_SCHEMA,
        "manifest_sha256":sha256(json.dumps(manifest,sort_keys=True,
                    separators=(",",":")).encode("utf-8")).hexdigest(),
        "source_operator":"PR68.dimension_experiment.run_case/material_flow",
        "source_examples":["S1-P0211","S1-P0212","S1-P0271","S1-P0272",
                           "S1-P0055","S1-P0058"],
        "factorial":run_factorial(),
        "paired_regimes":out,"n_regimes":len(out),
        "total_matched_worlds":len(out)*manifest["worlds_per_regime"],
        "policy_arms":list(ARMS),
        "hypothesis_status":"FH-C_CAUSAL_PRIORITY_NOT_PROVEN_OR_REFUTED_BY_SYNTHETIC_FINITE_EXERCISE",
        "evidence_tier":"DESIGNED_FINITE_SYNTHETIC_NOT_FIELD_OBSERVATION",
        "no_policy_has_private_referee_access":True,
        "no_cost_food_conflation":True,
    }


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest",type=Path,default=HERE/"G04_PROTOCOL.json")
    parser.add_argument("--include-worlds",action="store_true")
    parser.add_argument("--output",type=Path)
    a=parser.parse_args(argv)
    data=run_manifest(json.loads(a.manifest.read_text(encoding="utf-8")),
                      include_worlds=a.include_worlds)
    contents=json.dumps(data,ensure_ascii=False,sort_keys=True,indent=2)+"\n"
    if a.output:
        a.output.write_text(contents,encoding="utf-8")
    else:
        print(contents,end="")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
