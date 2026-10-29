"""Conscientia Ecosystemica -- synthetic bounded experimental campaign.

Never treats literature/GDocs as observed participant data, nor UC21 fixtures
as actual technology tests. All evidence claims and private oracles are scoped.
"""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
import json
import math
import os
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]  # caller should use full repo paths from HERE.parent
STUDIES = HERE.parent
RESULTS_SCHEMA = "CE-CAMPAIGN-0.1"
ARMS = ("A_ONLY", "QUALIFIED_Q", "PARTIAL_Q_AUDIT_GATED", "CONVENTIONAL_TARGETED", "EXPANDED_A")


def read_json(name: str) -> dict:
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def validate_cases(source_register: dict, case_register: dict) -> None:
    sources = {s["source_id"] for s in source_register["sources"]}
    if len(sources) != len(source_register["sources"]):
        raise ValueError("Duplicate source ID")
    cases = case_register["cases"]
    if len(cases) != case_register["frozen_case_count"]:
        raise ValueError("Case count changed after fixture freeze")
    if len({c["case_id"] for c in cases}) != len(cases):
        raise ValueError("Duplicate case")
    if {c["variant"] for c in cases} != {"VALID_GO","VALID_BLOCK","STALE","FALSE_Q","OPEN_RESIDUAL"}:
        raise ValueError("Changed variant universe")
    for c in cases:
        if c["primary_source_id"] not in sources:
            raise ValueError("Untraced case "+c["case_id"])
        if not c["not_a_real_person_or_product"] or c["test_evidence_tier"] != "SYNTHETIC_FIXTURE":
            raise ValueError("False empirical classification")
        if c["Q"]["scope_id"] != c["public"]["scope_id"]:
            raise ValueError("Misaligned Q scope")
        if c["truth_private_for_scoring"] not in ("ALLOW","BLOCK","NOT_ADJUDICABLE"):
            raise ValueError("Invalid truth status")
        if c["expanded_A"]["available"] and c["expanded_A"]["verdict"] is None:
            raise ValueError("Expanded A declared available without instrument")


def public_policy(public: dict, q: dict | None, peer: dict | None, full: dict | None, arm: str) -> dict:
    """The private truth is not an input. All instrument signals are separately declared.

    Q source identity and freshness are synthetically stated; checking a label
    and time DOES NOT authenticate external assertions (false-Q variant).
    """
    base = public["baseline_action"]
    cost = 0.0
    mode = "A_BASELINE"
    decision = base
    if arm == "A_ONLY":
        pass
    elif arm == "QUALIFIED_Q":
        if q is None:
            raise ValueError("Q arm requires a Q payload (even if unavailable)")
        cost = float(q["cost"])
        if q["kind"] == "B" and q["status"] in ("CURRENT_VALID", "CURRENT_BUT_FALSE") and q["fresh"] and q["scope_id"] == public["scope_id"] and q["provenance_established"]:
            decision = q["verdict"]
            mode = "ACCEPTED_B_QUALIFICATION"
        elif q["kind"] in ("C", "D"):
            decision = "REVIEW"
            mode = "OPEN_FRONTIER_NO_DECISION"
        else:
            mode = "REJECTED_STALE_OR_INVALID_B"
    elif arm == "PARTIAL_Q_AUDIT_GATED":
        if q is None:
            raise ValueError("Q auditable arm requires metadata")
        cost=float(q["cost"])+float(q["audit_cost"])
        if q["kind"] == "B" and q["status"] in ("CURRENT_VALID","CURRENT_BUT_FALSE") and q["fresh"] and q["independent_audit"] and q["scope_id"] == public["scope_id"]:
            decision=q["verdict"]
            mode="INDEPENDENTLY_AUDITED_B_TOY"
        else:
            mode="NO_AUDITED_B_FOR_THIS_QUESTION"
    elif arm == "CONVENTIONAL_TARGETED":
        if peer is None:
            raise ValueError("Peer metadata missing")
        if peer["has_direct_evidence"]:
            decision = peer["verdict"]
            cost = float(peer["cost"])
            mode = "TARGETED_CONVENTIONAL_EVIDENCE"
        else:
            mode = "NO_TARGETED_EVIDENCE"
    elif arm == "EXPANDED_A":
        if full is None:
            raise ValueError("Expanded metadata missing")
        if full["available"]:
            decision = full["verdict"]
            cost = float(full["cost"])
            mode = "FULL_INFORMATION_INSTRUMENT_SYNTHETIC"
        else:
            mode = "FULL_RECONSTRUCTION_UNAVAILABLE"
    else:
        raise ValueError("Unknown arm")
    if decision not in ("ALLOW","BLOCK","REVIEW"):
        raise ValueError("Bad public evidence action")
    if cost < 0 or not math.isfinite(cost):
        raise ValueError("Invalid cost")
    return {"action":decision,"acquisition_cost_synthetic":round(cost,4),"evidence_mode":mode}


def score_private(result: dict, truth: str, utility: dict) -> dict:
    """Separate scoring, never accessible to public_policy."""
    out = dict(result)
    if truth == "NOT_ADJUDICABLE":
        out.update({"correctness":"NOT_ADJUDICABLE", "decision_value_synthetic":None,"net_value_synthetic":None,"false_allow":None,"false_block":None})
        return out
    action = result["action"]
    if action == "REVIEW":
        value=float(utility["review"])
        correct="UNRESOLVED"
    elif action == truth:
        value=float(utility["correct_allow" if truth == "ALLOW" else "correct_block"])
        correct="CORRECT"
    else:
        value=float(utility["false_allow" if action == "ALLOW" else "false_block"])
        correct="WRONG"
    out.update({"correctness":correct,"decision_value_synthetic":round(value,4),
                "net_value_synthetic":round(value-result["acquisition_cost_synthetic"],4),
                "false_allow":int(action=="ALLOW" and truth=="BLOCK"),
                "false_block":int(action=="BLOCK" and truth=="ALLOW")})
    return out


def run_decisions(case_register: dict) -> dict:
    rows=[]
    for c in case_register["cases"]:
        # IMPORTANT: public_policy does not receive the hidden truth or private full case.
        strategies={}
        for arm in ARMS:
            signal=public_policy(c["public"],c["Q"],c["peer"],c["expanded_A"],arm)
            strategies[arm]=score_private(signal,c["truth_private_for_scoring"],c["utility"])
        rows.append({"case_id":c["case_id"],"family":c["family"],"variant":c["variant"],
                     "source_id":c["primary_source_id"],"example_id":c["example_id"],
                     "truth_PRIVATE":c["truth_private_for_scoring"],"arms":strategies})
    totals={}
    for arm in ARMS:
        v=[r["arms"][arm] for r in rows]
        scored=[x for x in v if x["net_value_synthetic"] is not None]
        totals[arm]={"cases":len(v),"adjudicable":len(scored),"unknown":len(v)-len(scored),
            "correct":sum(x["correctness"]=="CORRECT" for x in scored),
            "wrong":sum(x["correctness"]=="WRONG" for x in scored),
            "unresolved":sum(x["correctness"]=="UNRESOLVED" for x in scored),
            "false_allow":sum(x["false_allow"] for x in scored),
            "false_block":sum(x["false_block"] for x in scored),
            "instrument_cost_all_cases":round(sum(x["acquisition_cost_synthetic"] for x in v),4),
            "net_utility_adjudicable_synthetic":round(sum(x["net_value_synthetic"] for x in scored),4)}
    return {"case_count":len(rows),"arm_count":len(ARMS),"arm_decisions":len(rows)*len(ARMS),
            "totals":totals,"results":rows,"population_warning":"Deliberately constructed 12x5 test matrix. These totals are NOT prevalence, measured welfare, randomization or evidence of EA advantage."}


def factorial_joint_information() -> list[dict]:
    rows=[]
    # Q + ability to perform an atomic joint transition are distinct necessary inputs.
    # If Q not actually required, a competent joint controller can still complete.
    for proof_required in (False,True):
        for q_available in (False,True):
            for atomic_joint in (False,True):
                allowed=atomic_joint and (q_available or not proof_required)
                rows.append({"proof_required":proof_required,"valid_Q_available":q_available,
                    "joint_mechanism_available":atomic_joint,"additional_joint_output_synthetic":2 if allowed else 0,
                    "interpretation":"Q cannot create a physical joint transition when none exists."})
    return rows


def fh_c_competing_ablations() -> list[dict]:
    """Two opposing synthetic profiles for the FH-C causal-priority question.

    This does NOT estimate causal priority in populations. The source boundary
    and extra domain facts are entirely controlled fixture signals, so BOTH a
    favorable and a contradicting parameter class must be published.
    """
    outcomes=[]
    for profile in ("BOUNDARY_SIGNAL_STRONGER", "DOMAIN_FACTS_STRONGER"):
        # Four proposals; the first two are invalid, the next two valid.
        true_valid=[False,False,True,True]
        if profile=="BOUNDARY_SIGNAL_STRONGER":
            boundary_flags=(True,True,False,False)
            domain_flags=(True,False,False,False)
        else:
            boundary_flags=(True,False,False,False)
            domain_flags=(True,True,False,False)
        for use_boundary in (False,True):
            for use_domain in (False,True):
                accepted=[]
                for i,valid in enumerate(true_valid):
                    warning=(use_boundary and boundary_flags[i]) or (use_domain and domain_flags[i])
                    accepted.append(not warning)
                outcomes.append({"profile":profile,"with_boundary_Q":use_boundary,
                    "with_extra_domain_facts":use_domain,
                    "invalid_mission_pivots":sum(a and not v for a,v in zip(accepted,true_valid)),
                    "valid_changes_preserved":sum(a and v for a,v in zip(accepted,true_valid)),
                    "status":"SOURCE_INSPIRED_SYNTHETIC_ABLATION_ONLY"})
    return outcomes


def network_gap() -> list[dict]:
    rows=[]
    for topology in ("dense","star"):
        for n in (5,10,20,40):
            edges=n*(n-1)//2 if topology=="dense" else n-1
            b=10.0; g=0.2; alpha=0.0
            output=b*n + alpha*edges
            gap=g*edges
            rows.append({"topology":topology,"dimensions":n,"modeled_links":edges,
                "current_output_synthetic":round(output,4),
                "best_feasible_value_ASSUMED":round(output+gap,4),
                "gap_ASSUMED":round(gap,4),
                "gap_over_output_pct_ASSUMED":round(100*gap/output,4),
                "note":"The joint feasible counterfactual is ASSUMED, not independently proved for a social economy."})
    return rows


def _finite_information_engine():
    """Load the adjacent finite kernel by path, including source-replay imports."""
    from importlib.util import module_from_spec, spec_from_file_location
    spec = spec_from_file_location("_acc_conscientia_finite_info", HERE / "finite_information.py")
    if spec is None or spec.loader is None:
        raise RuntimeError("finite information source unavailable")
    engine = module_from_spec(spec)
    spec.loader.exec_module(engine)
    return engine


def finite_information() -> dict:
    # Explicit two-world, equal-weight finite witness; the output is CALCULATED.
    # Nothing assigns a distribution to the open epistemic exterior C or D.
    engine = _finite_information_engine()
    worlds = [{"a": "READY", "b": 0, "r": 0},
              {"a": "READY", "b": 1, "r": 1}]
    weights = [1, 1]
    h_before = engine.conditional_entropy(worlds, "r", ("a",), weights)
    h_after = engine.conditional_entropy(worlds, "r", ("a", "b"), weights)
    coverage = engine.original_uniform_coverage()
    return {"finite_worlds": worlds, "h_response_given_A_bits": h_before,
            "h_response_given_A_and_B_bits": h_after,
            "conditional_mutual_information_bits": h_before - h_after,
            "preimage_theoretical_m": coverage["m"],
            "preimage_constructible_n": coverage["n"],
            "finite_log_coverage_bits": coverage["log_coverage_bits"],
            "KL_P_to_Q_bits": coverage["kl_p_to_q"],
            "KL_Q_to_P_bits": coverage["kl_q_to_p"],
            "scope": "FINITE_UNIFORM_TOY_ONLY. No entropy or probability assigned to open C/D."}


def source_anchored_microexperiments() -> dict:
    """Small transparent witnesses for concrete passages of the source GDocs.

    These results are arithmetic or bounded tests on DECLARED synthetic data,
    never observational findings about people, organisations or markets.
    """
    # IQ-03 (CE-NOTES paragraph under heading): within each period, same service.
    service_t0, current_r0, valid_alt_r0 = 100, 100, 80
    service_t1, current_r1, valid_alt_r1 = 140, 110, 65
    resource_gap_t0 = current_r0 - valid_alt_r0
    resource_gap_t1 = current_r1 - valid_alt_r1

    # Two bananas, explicitly conditional on feasible route, consent and safety.
    banana_worlds = {
        "S0": {"bananas_produced": 0, "consumed_by_holder": 0, "received_by_child": 0, "wasted": 0},
        "S1": {"bananas_produced": 2, "consumed_by_holder": 1, "received_by_child": 0, "wasted": 1},
        "S2": {"bananas_produced": 2, "consumed_by_holder": 1, "received_by_child": 1, "wasted": 0},
    }
    assert all(d["consumed_by_holder"]+d["received_by_child"]+d["wasted"]==d["bananas_produced"] for d in banana_worlds.values())

    # A physical donation and a participant's consent are independent questions.
    donation = {
        "capacity_if_already_collected": 1,
        "delivery_possible_if_route_safe": True,
        "actual_authorized_donation_without_donor_consent": False,
        "charity_public_credit_assumed_misappropriated": False,
        "actual_third_party_behaviour": "NOT_OBSERVED",
    }

    # Credit/share floor is conditional on functional necessity, not proof of egoism.
    credit = {
        "total": 10,
        "seven_plus_four": {"required": [7, 4], "feasible": 7 + 4 <= 10},
        "seven_plus_three": {"required": [7, 3], "feasible": 7 + 3 <= 10},
        "necessity_of_share": "SOURCE_SPECIFIC_VALIDATION_PENDING",
    }

    # Per the author's discrete apples example: crossing a utility valley requires
    # a mechanism that can legitimately pay for / bridge a non-monotone move.
    apples = [0, 4, 7, 8, 7, 5, 5, 9, 10]
    local_peak = 3
    next_step_is_decline = apples[local_peak + 1] < apples[local_peak]
    best_global = max(range(len(apples)), key=lambda i: apples[i])

    # An independent source's repetition is not independent corroboration.
    source_ids = ["archive-A", "archive-A", "archive-B"]

    # A finite XOR example of relational information not present in each one
    # individual bit. No probability distribution is inferred for real C or D.
    q1_states = [(0, 0), (0, 1), (1, 0), (1, 1)]
    xor_rows = [{"q1": a, "q2": b, "r": a ^ b} for a, b in q1_states]
    xor_outputs = [row["r"] for row in xor_rows]
    info = _finite_information_engine()
    xor_weights = [1] * len(xor_rows)  # explicit finite uniform assumption
    xor_i1 = info.mutual_information(xor_rows, "r", ("q1",), xor_weights)
    xor_i2 = info.mutual_information(xor_rows, "r", ("q2",), xor_weights)
    xor_joint = info.mutual_information(xor_rows, "r", ("q1", "q2"), xor_weights)

    # Orange harvest/price scenario cannot identify price manipulation or
    # feasible redirection without actual safety, title and cost evidence.
    oranges = {"discarded_fruit_reported": True,
               "authorized_harvest_quantity": "UNKNOWN",
               "price_collusion": "NOT_ESTABLISHED",
               "recoverable_output": "NOT_ESTABLISHED",
               "actor_experienced_suffering": "NOT_MEASURED"}

    # Simulated educational architecture comparison refuses to hide health,
    # minors' welfare, inclusivity or learning quality behind narrow efficiency.
    education = {"candidate_passes_algebra": True,
                 "child_protection": "UNKNOWN",
                 "transfer_of_learning": "UNKNOWN",
                 "accessibility": "UNKNOWN",
                 "full_architecture_adoption": "NOT_ESTABLISHED"}

    return {
        "evidence_tier": "DECLARED_FINITE_SOURCE_ILLUSTRATIONS_NOT_OBSERVATIONS",
        "IQ03_EFFICIENCY_GAP": {"service_t0": service_t0, "service_t1": service_t1,
                                "resource_gap_t0": resource_gap_t0,
                                "resource_gap_t1": resource_gap_t1,
                                "output_increased": service_t1 > service_t0,
                                "gap_increased": resource_gap_t1 > resource_gap_t0,
                                "alt_feasible":"ASSUMED_WITHIN_EACH_PERIOD"},
        "BANANA_THREE_STATES": {"states": banana_worlds,
                                  "conditional_recovery_of_wasted_one": 1,
                                  "legality_and_safety":"ASSUMED_NOT_TESTED"},
        "BANANA_DONATION_AND_CARITAS": donation,
        "CREDIT_RELATIVE_FLOORS": credit,
        "NONMONOTONE_APPLES": {"utilities":apples,
                                "local_peak_quantity":local_peak,
                                "best_global_quantity":best_global,
                                "local_step_decreases_utility":next_step_is_decline,
                                "jump_legally_executable":"NOT_ESTABLISHED"},
        "NONFUNGIBLE_PROVENANCE": {"three_messages":len(source_ids),
                                    "distinct_origins":len(set(source_ids)),
                                    "fully_independent_observations":"NOT_ESTABLISHED"},
        "FINITE_XOR_SYNERGY": {"joint_states": len(q1_states),
                               "target_outputs": xor_outputs,
                               "I_R_Q1_bits": xor_i1,
                               "I_R_Q2_bits": xor_i2,
                               "I_R_Q1Q2_bits": xor_joint,
                               "no_open_D_probability": True},
        "ORANGE_RESEARCH_GATE": oranges,
        "EDUCATION_ARCHITECTURE_GATE": education,
        "TWO_MINISTRIES_700_APPLICATIONS": {
            "illustrative_start_applications":700,
            "illustrative_candidate_applications":2,
            "same_service_and_rights_evidence":"NOT_ESTABLISHED",
            "certified_recoverable_savings":"NOT_ESTABLISHED"},
        "CRAFT_TRANSMISSION": {
            "artifacts_still_exist":True,
            "master_apprentice_capacity":"NOT_OBSERVED",
            "ability_to_reproduce_craft":"NOT_ESTABLISHED",
            "historical_labour_outcome":"NOT_OBSERVED"},
        "HUMAN_SCENARIO_LYCEE": {
            "structural_hypothesis":"POSSIBLE_IF_JOINTLY_FEASIBLE_AND_PERSON_ENDORSES_GOAL",
            "observed_french_student":"NOT_OBSERVED",
            "experienced_distress":"NOT_MEASURED",
            "person_worth_metric":"NONE"},
    }


def gap_and_human_limits() -> dict:
    candidate={"development_now":4.0,"development_feasible_joint":7.0,
               "desired_positive_contribution":True,"blocked_externally":True,
               "limit_from_actor_view_attested":True}
    gap=candidate["development_feasible_joint"]-candidate["development_now"]
    return {"role_development_proxy_synthetic":gap,
            "human_suffering_experienced":"NOT_MEASURED", "self_determination_scale":"NOT_MEASURED",
            "human_dignity":"NOT_A_PRODUCTIVITY_METRIC","better_awareness_changes_physical_gap":False,
            "HID_task_time_synthetic":{"GIC":40,"NEO":20,"ACW":30,"UNKNOWN":10,
                                       "matched_counterfactual_ACW":10,
                                       "ACW_hours_difference_IF_FEASIBLE":20,
                                       "measurement_status":"NOT_OBSERVED; NOT_01K_CLAIM"},
            "attribution_gap_D02_formula":"BLOCKED_FOR_COMPUTATION__SOURCE_EDITION_CONFLICT",
            "cost_clarity_capture_recapture":"NOT_IDENTIFIED__NO_SAMPLING_OR_INDEPENDENCE",
            "informational_friction_suppression":"NOT_OBSERVED__REQUIRES_COMPARABLE_FIELD_STUDY",
            "solidarity":{"declared_voluntary":True,"real_consent_evidence":"NOT_OBSERVED",
                          "risk_D_unquantified":True,"software_authorization":"NOT_GRANTED"}}


def source_uc21_templates() -> list[dict]:
    labels={"S1":"Enterprise synthesis", "S2":"Shared mobility", "S3":"False mission", 
            "S4":"Refund case", "S5":"Stale repair", "S6":"Rights provenance"}
    return [{"scenario":s,"name":name,"native_routes":["R0","R1","R2"],
             "gate_count":7 if s=="S5" else 6,
             "test_stage":"DDS_STAGE_A_FIXTURE_PLANNED",
             "product_execution":"NOT_RUN","no_native_product_claim":True,
             "falsification":"requires predeclared change, authentic native trace and external effect observer"}
            for s,name in labels.items()]


def reuse_preexisting_studies() -> dict:
    """Execute existing sibling model scripts again and hash-check their JSON output.

    This is one integrative replay, not four newly independent validations.
    """
    variants={
      "PR42_RESOURCE_TRAPS":"bounded-traps-v0.1/bounded_traps.py",
      "PR43_NESTED_COMPOSITION":"nested-composition-suffering-v0.1/nested_model.py",
      "PR44_INTRINSIC_ABCD":"intrinsic-abcd-economics-v0.1/intrinsic_abcd.py",
      "PR45_LOCAL_METACOGNITION":"scoped-closure-metacognition-v0.1/metacognition.py"
    }
    result={}
    for name,relative in variants.items():
        file=STUDIES/relative
        reference=file.parent/"REFERENCE_SYNTHETIC_RESULTS.json"
        if not file.exists() or not reference.exists():
            result[name]={"status":"UNAVAILABLE_LOCAL_SOURCE","evidence":"NO_REPLAY"}
            continue
        run=subprocess.run([sys.executable,"-B",str(file)],capture_output=True,text=True,timeout=25)
        if run.returncode!=0:
            raise RuntimeError("Existing study failed "+name+": "+run.stderr[-1000:])
        got=json.loads(run.stdout)
        expected=json.loads(reference.read_text(encoding="utf-8"))
        if got!=expected:
            raise AssertionError("Existing study replay differs from pinned JSON "+name)
        result[name]={"status":"SYNTHETIC_REPLAY_MATCH","reference":relative.replace(file.name,"REFERENCE_SYNTHETIC_RESULTS.json"),
                      "measure_count":len(got) if isinstance(got,dict) else len(got)}
    return result


def UC21_adapter_replay() -> dict:
    """Executed synthetic adapter only; never says that a product has passed."""
    target=STUDIES/"parametric-economic-toy-v0.1"
    file=target/"uc21_dds_bridge.py"
    fixture=target/"examples/uc21_s4_synthetic_defender.json"
    if not file.exists() or not fixture.exists():
        return {"status":"UNAVAILABLE_SOURCE","native_product":"NOT_RUN"}
    with tempfile.TemporaryDirectory(prefix="ce_campaign_") as temp:
        output=Path(temp)/"uc21.json"
        run=subprocess.run([sys.executable,"-B",str(file),str(fixture),"--output",str(output)],capture_output=True,text=True,timeout=25)
        if run.returncode!=0:
            raise RuntimeError("Source UC21 adapter failed: "+run.stderr[-1000:])
        result=json.loads(output.read_text(encoding="utf-8"))
        assert result["selected_intervention_prediction"] == "SYNTHETIC_DEFENCE_NOT_EMPIRICAL_FALSIFICATION"
        assert result["uc21_hr_existential_six_case_conclusion"]=="NOT_REFUTED_OR_PROVED_BY_NONEXHAUSTIVE_RUNS"
        return {"status":"SYNTHETIC_ADAPTER_REPLAY","selected_intervention_prediction":result["selected_intervention_prediction"],
                "uc21_hr_existential_six_case_conclusion":result["uc21_hr_existential_six_case_conclusion"],
                "native_product":"NOT_RUN","scenario":"S4","routes":["R0","R1","R2"]}


def build_campaign(require_existing: bool=True) -> dict:
    sources=read_json("SOURCE_REGISTER.json")
    cases=read_json("CASE_REGISTRY.json")
    validate_cases(sources,cases)
    report={"schema_version":RESULTS_SCHEMA,"date_cutoff":"2026-10-26",
            "evidence_status":"SYNTHETIC_MODELS_ONLY; SOURCE_DOCUMENT_REVIEW; NO_HUMAN_OR_NATIVE_VENDOR_TEST",
            "source_documents_screened":len(sources["sources"]),
            "decision_experiments":run_decisions(cases),
            "factorial_joint_mechanism":factorial_joint_information(),
            "FH_C_competing_ablations":fh_c_competing_ablations(),
            "network_counterfactuals":network_gap(),
            "source_anchored_microexperiments":source_anchored_microexperiments(),
            "finite_entropic_experiment":finite_information(),
            "human_and_measurement_blockers":gap_and_human_limits(),
            "uc21_case_templates_not_executed":source_uc21_templates(),
            "existing_synthetic_replays":reuse_preexisting_studies() if require_existing else {"status":"LOCAL_ONLY_NO_SIBLING_REPLAY"},
            "uc21_synthetic_adapter":UC21_adapter_replay() if require_existing else {"status":"LOCAL_ONLY_NO_SIBLING_REPLAY"},
            "interpretation_guard":"No experiment here shows observed social harm, historical outcomes, UC21 Stage C, actual HID, papal endorsement or universal performance superiority of EA. Arbitrary monetary coefficients do not validate FH-E."}
    return report


def report_summary(report: dict) -> str:
    d=report["decision_experiments"]
    lines=["# Resultados de campaña sintética — Conscientia Ecosystemica / ACC", "",
           "**Fecha de corte:** 2026-10-26. **Estado:** ejecutado sobre funciones y fixtures sintéticos; no muestra observaciones humanas ni pruebas nativas de tecnología. La selección de escenarios NO es muestra estadística.","",
           "## Matriz de decisiones", "",
           f"{d['case_count']} casos cerrados de laboratorio × {d['arm_count']} estrategias = {d['arm_decisions']} evaluaciones. Doce mecanismos ilustrativos × cinco variantes; la verdad privada sólo puntúa después de que la estrategia decide.","",
           "| Estrategia | Correctas | Equivocadas | Sin resolver | No adjudicables | Coste sintético acumulado | Valor neto sintético en adjudicables |",
           "|---|---:|---:|---:|---:|---:|---:|"]
    for name,t in d["totals"].items():
        lines.append(f"| {name} | {t['correct']} | {t['wrong']} | {t['unresolved']} | {t['unknown']} | {t['instrument_cost_all_cases']:.2f} | {t['net_utility_adjudicable_synthetic']:.2f} |")
    lines += ["", "**Interpretación:** el total económico es un resultado interno de la función de pérdidas definida para este experimento, NO una ganancia real observada ni evaluación independiente del producto EA. El modelo incluye Q falsa, Q caducada, comparador convencional superior y estados sin oráculo legítimo.","",
        "## Pruebas mecánicas y negativas", "",
        "- **Factorial 2×2×2:** evidencia Q × transición conjunta × requisito de acreditación; Q sin mecanismo físico no genera recursos, y mecanismo conjunto sin Q puede ser suficiente cuando la prueba adicional no es necesaria.",
        "- **FH-C con contradicción incluida:** dos perfiles 2×2 ablativos dan predicciones OPUESTAS sobre si retirar cualificación B/C/D causa más pivotes injustificados que retirar hechos del dominio. No hay afirmación de prioridad causal universal.",
        "- **Crecimiento de brecha:** dos topologías (densa/estrella) y n=5/10/20/40; el óptimo superior se presupone y debe certificarse fuera del toy antes de llamarlo deuda recuperable.",
        "- **Doce microensayos de fuente:** IQ-03 sobre eficiencia con mismo servicio por periodo, plátanos S0/S1/S2, consentimiento/coste/atribución, cuotas de crédito 7+4/7+3, manzanas, trazabilidad independiente, XOR, naranjas, educación, ministerios, oficios y liceo. Son modelos y puertas de evidencia, NO datos observados.",
        "- **Shannon:** dos estados con A idéntico, un bit de ambigüedad para una pregunta y cero al recibir B auténtico; sólo sobre espacio finito uniforme; divergencia KL en orientación equivocada da infinito.",
        "- **Persona:** brecha estructural sintética de 3 unidades con las tres condiciones estipuladas; experiencia de sufrimiento y dignidad no cuantificadas.",
        "- **Instrumentos bloqueados:** fórmula D02 Attribution Gap conflictiva entre ediciones; captura-recaptura sin muestreo e independencia; falta de medición longitudinal 01K/psicológica.",
        "- **UC21:** seis perfiles fuente y sus gates reproducidos como contratos de Stage A PENDIENTE; ninguna prueba Stage C ni validación de tecnología real se afirma.","",
        "## Reejecución de artefactos anteriores",""]
    for name,entry in report["existing_synthetic_replays"].items():
        status = entry.get("status") if isinstance(entry,dict) else entry
        lines.append(f"- {name}: **{status}**")
    lines.append(f"- UC21 S4 adapter: **{report['uc21_synthetic_adapter']['status']}**, explicitamente sintético; HR no probado/refutado.")
    lines += ["", "## Qué puede sustentar un PR y qué no", "",
        "**Sí:** ejecución reproducible de un conjunto de modelos explícitos, casos adversos, datos artificiales, comparadores y una disciplina de proveniencia fuente→pregunta→resultado.","",
        "**No:** una inferencia sobre incidencia social de sufrimiento, experimentos en universidades, sanciones o decisiones reales de empresas, costes de tecnologías actuales, superioridad universal EA o estado físico de C/D.","",
        "**Próxima fase:** seleccionar una familia, congelar población/oráculo/recursos/consentimiento; obtener trazas reales autorizadas; comparar un peer fuerte con la misma información y medir humanamente cuando proceda; sólo entonces DDS Stage B/C o estudio causal social.",""]
    return "\n".join(lines)


def main(argv=None):
    parser=argparse.ArgumentParser()
    parser.add_argument("--local",action="store_true",help="Generate only new bounded cases when sibling PR sources unavailable")
    parser.add_argument("--output",default="",help="Write generated JSON; default stdout")
    parser.add_argument("--summary",default="",help="Write Markdown summary")
    args=parser.parse_args(argv)
    report=build_campaign(require_existing=not args.local)
    s=json.dumps(report,ensure_ascii=False,sort_keys=True,indent=2)+"\n"
    if args.output:
        Path(args.output).write_text(s,encoding="utf-8")
    else:
        sys.stdout.write(s)
    if args.summary:
        Path(args.summary).write_text(report_summary(report),encoding="utf-8")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
