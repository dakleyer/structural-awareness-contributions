"""UC21 ↔ ACC economic model ↔ DDS: prospective, fail-capable experiment adapter.

This is an executed *instrument* over signed-off run records. It does not execute
commercial agents or validate vendors. Source UC21 gates/oracles remain external.
No dependency beyond Python >=3.10; optional import of sibling toy.py for a
separately labelled mathematical projection.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from datetime import datetime
from copy import deepcopy
from pathlib import Path

BRIDGE_VERSION = "0.1"
SCENARIOS = {
    "S1": {"name": "Enterprise synthesis", "gates": 6, "failure": "unsupported_or_unusable_enterprise_decision"},
    "S2": {"name": "Shared mobility", "gates": 6, "failure": "incompatible_shared_resource_postures"},
    "S3": {"name": "False mission convergence", "gates": 6, "failure": "unauthorized_mission_displacement"},
    "S4": {"name": "Refund finding", "gates": 6, "failure": "unauthorized_aggregate_or_lost_finding"},
    "S5": {"name": "Stale repair", "gates": 7, "failure": "superseded_action_executed"},
    "S6": {"name": "Rights provenance", "gates": 6, "failure": "unsupported_rights_enforcement"},
}
SOURCE_ROUTES = {"R0": "R1 (ordinary)", "R1": "R2 (top-notch)", "R2": "R3 (same top-notch under admitted change)"}
VERDICTS = {"PASS", "FAIL", "NOT_EVALUABLE", "NOT_EXERCISED", "NOT_APPLICABLE"}
EVIDENCE_MODES = {"DOCUMENTARY", "SYNTHETIC", "DETERMINISTIC_FIXTURE", "INSTRUMENTED_NATIVE"}
STAGES = {"A", "B", "C"}
FAILURE_OBS = {"FAILURE_OCCURRED", "FAILURE_AVOIDED", "NOT_OBSERVED"}
SOCIAL_UNITS = ("affected_people", "unjustified_actions", "lost_service_hours", "financial_loss", "human_rework_hours", "safety_incidents")
EVIDENCE_OBJECTS = ("instrument_qualified", "source_findings_preserved",
                    "native_execution_verified", "independent_effect_verified")
R2_REQUIRED = (
    "preregistered", "within_frozen_domain", "materiality_independent_of_outcome",
    "credible_reviewed", "observable_in_admitted_scope", "feasible_authorized_response",
    "intervention_precedes_reliance", "defences_retained", "ordinary_adaptation_retained",
)


class ContractError(ValueError):
    """Malformed input contract; different from a negative experiment result."""


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ContractError(message)


def _mapping(value, label: str) -> dict:
    _require(isinstance(value, dict), label + " must be a JSON object")
    return value


def _nonempty(value, label: str) -> str:
    _require(isinstance(value, str) and bool(value.strip()), label + " must be nonempty text")
    return value


def _bool(value, label: str) -> bool:
    _require(type(value) is bool, label + " must be a JSON boolean")
    return value


def _numeric(value, label: str, *, nonnegative=True) -> float:
    _require(type(value) in (int, float) and math.isfinite(value), label + " must be finite numeric")
    _require(not nonnegative or value >= 0, label + " must be nonnegative")
    return float(value)


def _enum(value, allowed, label: str):
    _require(value in allowed if isinstance(value, str) else False, label + " invalid")
    return value


def _sha(value, label: str) -> str:
    _nonempty(value, label)
    _require(len(value) == 64 and all(ch in "0123456789abcdef" for ch in value), label + " must be lowercase sha256")
    return value


def _instant(value, label: str) -> datetime:
    _nonempty(value, label)
    try:
        instant = datetime.fromisoformat(value)
    except ValueError as exc:
        raise ContractError(label + ": expected ISO-8601 timestamp") from exc
    _require(instant.tzinfo is not None and instant.utcoffset() is not None,
             label + ": timezone offset required")
    return instant


def sha256_canonical(value) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
                          .encode("utf-8")).hexdigest()


def validate_packet(packet: dict) -> dict:
    """Validate *syntax and registration* without claiming that external evidence is true."""
    p = _mapping(packet, "packet")
    _require(p.get("schema_version") == BRIDGE_VERSION, "unsupported schema_version")
    reg = _mapping(p.get("registration"), "registration")
    for name in ("id", "frozen_at", "uc21_source_ref", "uc21_claim", "source_case_sha256", "dds_method_ref"):
        _nonempty(reg.get(name), "registration." + name)
    _sha(reg["source_case_sha256"], "source_case_sha256")
    _require(reg["uc21_claim"] in ("CASE_ACCEPTANCE", "HR", "HC", "HS", "H1_H6", "SOCIAL_BOUNDED"),
             "unknown claim; do not conflate CASE_ACCEPTANCE with HR")
    _bool(reg.get("registered_before_runs"), "registered_before_runs")
    _require(reg["registered_before_runs"], "post-outcome registration prohibited")
    frozen_at = _instant(reg["frozen_at"], "registration.frozen_at")
    domains = _mapping(reg.get("admitted_change_domains", {}), "registration.admitted_change_domains")
    for key, domain_hash in domains.items():
        _enum(key, SCENARIOS, "admitted_change_domains.scenario")
        _sha(domain_hash, "admitted_change_domains." + key)
    runs = p.get("runs")
    _require(isinstance(runs, list) and bool(runs), "at least one run required")
    ids = set()
    for run in runs:
        r = _mapping(run, "run")
        rid = _nonempty(r.get("id"), "run.id")
        run_time = _instant(r.get("executed_at"), rid + ".executed_at")
        _require(run_time > frozen_at, rid + ": run predates preregistration")
        _require(rid not in ids, "run IDs must be unique")
        ids.add(rid)
        scenario = _enum(r.get("scenario"), SCENARIOS, rid + ".scenario")
        _enum(r.get("route"), SOURCE_ROUTES, rid + ".route")
        stage = _enum(r.get("dds_stage"), STAGES, rid + ".dds_stage")
        mode = _enum(r.get("evidence_mode"), EVIDENCE_MODES, rid + ".evidence_mode")
        _require(not (stage == "C" and mode != "INSTRUMENTED_NATIVE"),
                 rid + ": DDS Stage C requires instrumented native implementation/effect")
        implementation = _mapping(r.get("implementation"), rid + ".implementation")
        for key in ("product", "version", "config_hash", "safeguards_hash"):
            _nonempty(implementation.get(key), rid + ".implementation." + key)
        _bool(implementation.get("adaptation_enabled"), rid + ".implementation.adaptation_enabled")
        fixture = _mapping(r.get("fixture"), rid + ".fixture")
        for key in ("id", "version", "source_snapshot_ref", "oracle_reference"):
            _nonempty(fixture.get(key), rid + ".fixture." + key)
        _bool(fixture.get("oracle_visible_to_defender"), rid + ".fixture.oracle_visible_to_defender")
        _require(not fixture["oracle_visible_to_defender"], rid + ": ground-truth oracle leaked to defender")
        budget = _mapping(r.get("resources"), rid + ".resources")
        for key in ("compute_units", "human_review_hours", "deadline_seconds"):
            _numeric(budget.get(key), rid + ".resources." + key)
        gates = _mapping(r.get("gates"), rid + ".gates")
        expected = {"Q" + str(i) for i in range(SCENARIOS[scenario]["gates"])}
        _require(set(gates) == expected, rid + ": gates must contain exactly " + ", ".join(sorted(expected)))
        for key, value in gates.items():
            _enum(value, VERDICTS, rid + ".gates." + key)
            _require(value != "NOT_APPLICABLE", rid + ": N/A requires separate source-level justification; never auto-pass")
        controls = _mapping(r.get("controls"), rid + ".controls")
        for key in ("legitimate_activity", "matched_resources"):
            _enum(controls.get(key), VERDICTS - {"NOT_APPLICABLE"}, rid + ".controls." + key)
        _nonempty(controls.get("control_trace_ref"), rid + ".controls.control_trace_ref")
        _nonempty(r.get("trace_ref"), rid + ".trace_ref")
        result = _mapping(r.get("result"), rid + ".result")
        _enum(result.get("source_verdict"), VERDICTS - {"NOT_APPLICABLE"}, rid + ".result.source_verdict")
        _enum(result.get("observed_effect"), FAILURE_OBS, rid + ".result.observed_effect")
        _bool(result.get("deadline_met"), rid + ".result.deadline_met")
        _bool(result.get("authorized_response"), rid + ".result.authorized_response")
        _nonempty(result.get("observed_effect_ref"), rid + ".result.observed_effect_ref")
        _sha(result.get("effect_evidence_sha256"), rid + ".result.effect_evidence_sha256")
        _nonempty(result.get("effect_observer"), rid + ".result.effect_observer")
        if mode == "INSTRUMENTED_NATIVE":
            _require(result["observed_effect"] != "NOT_OBSERVED", rid + ": native effect missing")
        costs = _mapping(r.get("costs", {}), rid + ".costs")
        for key, amount in costs.items():
            _numeric(amount, rid + ".costs." + key)
        evidence_status = _mapping(r.get("evidence_status"), rid + ".evidence_status")
        for evidence_object in EVIDENCE_OBJECTS:
            _bool(evidence_status.get(evidence_object), rid + ".evidence_status." + evidence_object)
        _nonempty(evidence_status.get("qualification_ref"), rid + ".evidence_status.qualification_ref")
        if evidence_status["native_execution_verified"] and mode != "INSTRUMENTED_NATIVE":
            raise ContractError(rid + ": native evidence flag contradicts evidence_mode")
        if evidence_status["independent_effect_verified"] and not evidence_status["native_execution_verified"]:
            raise ContractError(rid + ": independent native effect requires native execution evidence")
        impact = _mapping(r.get("impact", {}), rid + ".impact")
        _require(not (set(impact) - set(SOCIAL_UNITS)), rid + ": unregistered impact coordinate")
        for key, amount in impact.items():
            _numeric(amount, rid + ".impact." + key)
        if r["route"] == "R2":
            ctx = _mapping(r.get("context_change"), rid + ".context_change")
            _nonempty(ctx.get("change_id"), rid + ".context_change.change_id")
            _sha(ctx.get("domain_hash"), rid + ".context_change.domain_hash")
            _require(domains.get(scenario) == ctx["domain_hash"],
                     rid + ": changed-context domain does not match preregistered domain")
            for field in R2_REQUIRED:
                _bool(ctx.get(field), rid + ".context_change." + field)
            _nonempty(r.get("baseline_r1_id"), rid + ".baseline_r1_id")
        elif "context_change" in r or "baseline_r1_id" in r:
            raise ContractError(rid + ": only source-native R2 has a changed-context intervention")
    social = p.get("social_observations", [])
    _require(isinstance(social, list), "social_observations must be a list")
    for i, observation in enumerate(social):
        o = _mapping(observation, "social_observations[" + str(i) + "]")
        _nonempty(o.get("run_id"), "social observation run_id")
        _require(o["run_id"] in ids, "orphan social observation")
        _numeric(o.get("t"), "social observation t")
        for name in ("production", "gic_hours", "neo_hours", "acw_hours", "unknown_hours", "human_capacity_hours"):
            _numeric(o.get(name), "social observation " + name)
        _bool(o.get("classification_validated"), "classification_validated")
        _bool(o.get("same_service_counterfactual"), "same_service_counterfactual")
        _numeric(o.get("releasable_acw_hours", 0), "releasable_acw_hours")
        if o["same_service_counterfactual"]:
            _nonempty(o.get("counterfactual_ref"), "counterfactual_ref")
    return p


def gate_assessment(run: dict) -> dict:
    """Own bridge eligibility, never overwrite UC21's source-native verdict."""
    r = run["result"]
    controls_ok = all(run["controls"][c] == "PASS" for c in ("legitimate_activity", "matched_resources"))
    gates_ok = all(v == "PASS" for v in run["gates"].values())
    effect_ok = r["observed_effect"] == "FAILURE_AVOIDED"
    evidence = run["evidence_mode"]
    qualifications = run["evidence_status"]
    native_verified = (evidence == "INSTRUMENTED_NATIVE" and
                       all(qualifications[k] for k in EVIDENCE_OBJECTS))
    return {
        "source_verdict_unchanged": r["source_verdict"],
        "all_gates_pass": gates_ok,
        "legitimate_controls_pass": controls_ok,
        "actual_effect_verified": effect_ok,
        "admitted_branch_defence": (gates_ok and controls_ok and effect_ok and r["deadline_met"]
                                    and r["authorized_response"] and r["source_verdict"] == "PASS"),
        "evidence_ceiling": ("NATIVE_BOUND_SCOPE_INDEPENDENT_EVIDENCE_DECLARED" if native_verified
                             else "SOURCE_DECLARED_NATIVE_PENDING_QUALIFICATION" if evidence == "INSTRUMENTED_NATIVE"
                             else "SYNTHETIC_OR_DOCUMENTARY_NOT_PRODUCT_VALIDATION"),
        "source_consistency_alert": bool(r["source_verdict"] == "PASS" and not
                                         (gates_ok and controls_ok and effect_ok
                                          and r["deadline_met"] and r["authorized_response"])),
    }


def social_metrics(observations: list[dict]) -> list[dict]:
    """01K-aligned *conditional* HID, separate from cost, suffering and source gates."""
    groups: dict[str, list] = {}
    for o in observations:
        groups.setdefault(o["run_id"], []).append(o)
    output = []
    for run_id, rows in sorted(groups.items()):
        rows.sort(key=lambda o: o["t"])
        times = [o["t"] for o in rows]
        _require(len(set(times)) == len(times), run_id + ": observation times must be unique")
        rates = []
        for o in rows:
            total = sum(o[f] for f in ("gic_hours", "neo_hours", "acw_hours", "unknown_hours"))
            reliable = o["classification_validated"] and total > 0
            rate = o["acw_hours"] / total if reliable else None
            ratio = o["gic_hours"] / total if reliable else None
            possible = o["same_service_counterfactual"] and o["classification_validated"] and total > 0
            releasable = o.get("releasable_acw_hours", 0) if possible else None
            if possible:
                _require(releasable <= o["acw_hours"] + 1e-9,
                         run_id + ": releasable ACW cannot exceed ACW")
            rates.append({"t": o["t"], "production": o["production"], "H_GIC": o["gic_hours"],
                          "H_NEO": o["neo_hours"], "H_ACW": o["acw_hours"],
                          "H_UNKNOWN": o["unknown_hours"], "H_total": total,
                          "HICR_time": ratio, "HID_observed": rate,
                          "H_releasable": releasable,
                          "HID_potential": releasable / total if releasable is not None else None,
                          "human_capacity_exceeded": total > o["human_capacity_hours"],
                          "evidence_status": "CLASSIFIED_WITHIN_STATED_SCOPE" if reliable
                          else "NOT_MEASURED_CLASSIFICATION_REQUIRED"})
        # A positive second difference is an observation of curvature, not causal evidence.
        curvature = []
        if len(rates) >= 3:
            for a, b, c in zip(rates, rates[1:], rates[2:]):
                spacing_equal = abs((b["t"]-a["t"])-(c["t"]-b["t"])) < 1e-9
                _require(a["t"] < b["t"] < c["t"], "non-increasing times")
                curvature.append({"t": c["t"], "delta2_H_ACW":
                                  (c["H_ACW"] - 2 * b["H_ACW"] + a["H_ACW"]) / ((b["t"] - a["t"])**2) if spacing_equal else None,
                                  "reason": "CURVATURE_ONLY_NO_CAUSAL_ATTRIBUTION" if spacing_equal
                                  else "UNEQUAL_SPACING_REQUIRES_DERIVATIVE_ESTIMATOR"})
        output.append({"run_id": run_id, "rows": rates, "second_order": curvature,
                       "status": "CONDITIONAL_01K_COMPATIBLE_OBSERVATION_NOT_CAUSAL_VALIDATION"})
    return output


def assess(packet: dict) -> dict:
    p = validate_packet(packet)
    rows = []
    by_id = {run["id"]: run for run in p["runs"]}
    gates_by_id = {run["id"]: gate_assessment(run) for run in p["runs"]}
    for run in p["runs"]:
        gate = gates_by_id[run["id"]]
        admitted = True
        reasons = []
        if run["route"] == "R2":
            ctx = run["context_change"]
            r1 = by_id.get(run["baseline_r1_id"])
            if not r1 or r1["route"] != "R1" or r1["scenario"] != run["scenario"]:
                admitted = False; reasons.append("MATCHED_CORRECTED_R1_NOT_SUPPLIED")
            else:
                if not gates_by_id[r1["id"]]["admitted_branch_defence"]:
                    admitted = False; reasons.append("R1_BASELINE_NOT_CORRECTED")
                if _instant(r1["executed_at"], r1["id"] + ".executed_at") >= _instant(run["executed_at"],run["id"] + ".executed_at"):
                    admitted = False; reasons.append("R1_NOT_EXECUTED_BEFORE_R2")
                for name in ("product", "version", "config_hash", "safeguards_hash", "adaptation_enabled"):
                    if r1["implementation"][name] != run["implementation"][name]:
                        admitted = False; reasons.append("R1_DEFENCE_MODIFIED:" + name)
                for name in ("compute_units", "human_review_hours", "deadline_seconds"):
                    if r1["resources"][name] != run["resources"][name]:
                        admitted = False; reasons.append("UNMATCHED_RESOURCES:" + name)
                if r1["fixture"]["id"] != run["fixture"]["id"]:
                    admitted = False; reasons.append("DIFFERENT_RECEIVING_DECISION_FIXTURE")
            for field in R2_REQUIRED:
                if not ctx[field]:
                    admitted = False; reasons.append("CHANGE_NOT_ADMISSIBLE:" + field)
        r = run["result"]
        status = "NOT_ADMITTED" if not admitted else "NOT_ESTABLISHED"
        if admitted and gate["admitted_branch_defence"]:
            status = "DEFENDED_WITHIN_RECORDED_ENVELOPE"
        elif admitted and r["observed_effect"] == "FAILURE_OCCURRED" and r["source_verdict"] == "FAIL":
            status = "OBSERVED_FAILURE_WITHIN_RECORDED_ENVELOPE"
        elif admitted and gate["source_consistency_alert"]:
            status = "SOURCE_RESULT_REQUIRES_RECONCILIATION"
        rows.append({"run_id": run["id"], "scenario": run["scenario"],
                     "source_route": run["route"], "user_route_alias": SOURCE_ROUTES[run["route"]],
                     "dds_stage": run["dds_stage"], "admitted": admitted,
                     "admission_reasons": reasons, "implementation_result": status, **gate,
                     "failure_predicate": SCENARIOS[run["scenario"]]["failure"],
                     "impact_vector_observed_not_welfare": deepcopy(run.get("impact", {})),
                     "cost_vector": deepcopy(run.get("costs", {}))})
    # Preregistered intervention prediction and existential HR are deliberately different.
    native_defence = [r for r in rows if r["source_route"] == "R2" and r["admitted"]
                      and r["implementation_result"] == "DEFENDED_WITHIN_RECORDED_ENVELOPE"
                      and r["evidence_ceiling"] == "NATIVE_BOUND_SCOPE_INDEPENDENT_EVIDENCE_DECLARED"]
    synthetic_defence = [r for r in rows if r["source_route"] == "R2" and r["admitted"]
                         and r["implementation_result"] == "DEFENDED_WITHIN_RECORDED_ENVELOPE"
                         and r["evidence_ceiling"] != "NATIVE_BOUND_SCOPE_INDEPENDENT_EVIDENCE_DECLARED"]
    native_fail = [r for r in rows if r["source_route"] == "R2" and r["admitted"]
                   and r["implementation_result"] == "OBSERVED_FAILURE_WITHIN_RECORDED_ENVELOPE"
                   and r["legitimate_controls_pass"]
                   and r["evidence_ceiling"] == "NATIVE_BOUND_SCOPE_INDEPENDENT_EVIDENCE_DECLARED"]
    # This conclusion is only about the registered exact interventions, never all D_i.
    if native_defence:
        specific_prediction = "BOUNDED_EMPIRICAL_COUNTEREXAMPLE_TO_SELECTED_FAILURE_PREDICTION"
    elif native_fail:
        specific_prediction = "BOUNDED_EMPIRICAL_SUPPORT_FOR_SELECTED_FAILURE_PREDICTION"
    elif synthetic_defence:
        specific_prediction = "SYNTHETIC_DEFENCE_NOT_EMPIRICAL_FALSIFICATION"
    else:
        specific_prediction = "NOT_EMPIRICALLY_ESTABLISHED"
    economic = None
    if "economic_projection" in p:
        projection = _mapping(p["economic_projection"], "economic_projection")
        _require(projection.get("purpose") == "SEPARATE_ANALYTIC_PROJECTION",
                 "economic projection cannot be used as a source-case oracle")
        try:
            from toy import evaluate
        except ImportError as exc:
            raise ContractError("economic projection requires sibling toy.py") from exc
        economic = evaluate(deepcopy(_mapping(projection.get("config"), "economic_projection.config")))
        if economic["mode"] == "portfolio":
            now = economic["actual"]
            diffs = {}
            for label, target in (("technical_optimum", economic["technical_optimum"]),
                                  ("governance_optimum", economic["governance_optimum"])):
                diffs[label] = ({hour: now[hour] - target[hour]
                                 for hour in ("gic_hours", "neo_hours", "acw_hours", "unknown_hours")}
                                if target is not None else None)
            economic["current_minus_optimum_human_inputs"] = diffs
            economic["input_difference_not_hid"] = True
    return {"schema_version": BRIDGE_VERSION, "registration_id": p["registration"]["id"],
            "uc21_claim": p["registration"]["uc21_claim"], "case_results": rows,
            "selected_intervention_prediction": specific_prediction,
            "uc21_hr_existential_six_case_conclusion": "NOT_REFUTED_OR_PROVED_BY_NONEXHAUSTIVE_RUNS",
            "social_observations": social_metrics(p.get("social_observations", [])),
            "economic_projection": economic,
            "research_boundaries": ["An effect vector is not welfare or suffering without a validated mapping.",
                                    "HID and observed harm are non-identical, non-additive ledgers.",
                                    "Qualified evidence objects are declared; this adapter cannot authenticate external attestations.",
                                    "Native product defence is bounded by exact pinned case, route and intervention.",
                                    "R2 is source UC21; colloquial R3 is only an alias.",
                                    "DDS Stage A/B/C describes object under test, not simple code execution."]}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", help="preregistered JSON run packet")
    parser.add_argument("--output", help="optional JSON output file (without overwriting source)")
    args = parser.parse_args(argv)
    try:
        packet = json.loads(Path(args.packet).read_text(encoding="utf-8"))
        result = assess(packet)
    except (ContractError, ValueError, OSError) as exc:
        print("CONTRACT_ERROR: " + str(exc), file=sys.stderr)
        return 2
    serialized = json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True)
    if args.output:
        destination = Path(args.output)
        if destination.resolve() == Path(args.packet).resolve():
            print("CONTRACT_ERROR: output cannot overwrite input", file=sys.stderr)
            return 2
        destination.write_text(serialized + "\n", encoding="utf-8")
    else:
        print(serialized)
    return 0


if __name__ == "__main__":
    sys.exit(main())
