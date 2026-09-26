"""Deterministic, descriptive RS-00E-Q1a v0.5 Stage-0 harness.

The oracle is loaded only after both candidate adapters have completed.
All observations are synthetic. Neither adapter represents a deployed product.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys

from canonical_trace_v1 import canonical_trace_bytes

HERE = Path(__file__).resolve().parent
PRE_REG_COMMIT = "00241c5c3ab554dd732467ef0ae4c175f958d144"
BRANCHES = ("Q1a-P1", "Q1a-P2", "Q1a-C0")
CONFIGS = ("B1", "B3")
HANDOFF = "received_reports_to_assessment"


def frozen_observation(case: dict, registry: dict) -> dict:
    """Construct only fields made available to both candidates by v0.5."""
    return {
        "proposition_id": "release_basis_supported",
        "scope_id": "sigma_release_t0",
        "deadline_step": 6,
        "freshness_step": 1,
        "handoff_target": "declared_receiving_owner",
        "reports": [dict(r, proposition_id="release_basis_supported", freshness_step=1,
                         scope_id="sigma_release_t0", deadline_step=6)
                    for r in case["reports"]],
        "registry": dict(registry),
        "processing_step_ceiling": 6,
    }


def qualifier_loss_self_test(detector_enabled: bool) -> dict:
    """Inject loss at one named P1 handoff, then disable the detector as inverse control."""
    lost = {"report_id": "A", "producer_id": "producer_A"}
    observed_loss = detect_qualifier_loss(lost, "P", detector_enabled)
    return {
        "fixture_id": "RS-00E-Q1a", "branch": "Q1a-P1",
        "pre_registration_commit": PRE_REG_COMMIT,
        "control": "qualifier_loss_detector_active" if detector_enabled else "qualifier_loss_detector_disabled",
        "handoff_name": HANDOFF, "step": 1,
        "injected_missing_field": "upstream_source_id",
        "expected_qualifier": "upstream_source_id=P",
        "observed_loss": observed_loss,
        "detector_enabled": detector_enabled,
        "disposition": "PASS" if observed_loss else "FAIL",
        "evidence_status": "Stage-0 stipulative instrumentation self-test",
    }


def detect_qualifier_loss(report: dict, expected_upstream: str, enabled: bool) -> bool:
    """The same named-handoff hook is used by self-tests and candidate event playback."""
    return enabled and report.get("upstream_source_id") != expected_upstream


def _roots(observation: dict) -> tuple[list[str], list[str]]:
    roots, basis = [], []
    direct = observation["reports"][0]["upstream_source_id"] == observation["reports"][1]["upstream_source_id"]
    for report in observation["reports"]:
        raw = report["upstream_source_id"]
        root = raw if direct else observation["registry"].get(raw, raw)
        roots.append(root)
        basis.append("registry:" + raw if not direct and raw in observation["registry"] else "received.upstream_source_id:" + raw)
    return roots, basis


def conventional_b1(observation: dict) -> dict:
    """Frozen B1 provenance-and-registry-join peer; same source access as B3."""
    roots, basis = _roots(observation)
    common = roots[0] == roots[1]
    return _assessment("B1-Q1A-PROVENANCE-JOIN-v0.1", observation, common, roots, basis)


def ea_profiled_b3(observation: dict) -> dict:
    """Frozen B3 dependency-preservation adapter, without extra oracle access."""
    roots, basis = _roots(observation)
    common = len(set(roots)) == 1
    return _assessment("B3-Q1A-EA-PRESERVATION-v0.1", observation, common, roots, basis)


def _assessment(config_id: str, observation: dict, common: bool,
                roots: list[str], basis: list[str]) -> dict:
    registry_reads = sum(b.startswith("registry:") for b in basis)
    steps = 2 + (1 if registry_reads else 0) + 1 + 1  # A,B; registry; assessment; handoff
    return {
        "configuration_id": config_id,
        "dependency_assessment": {
            "independent_support": not common,
            "shared_upstream_sources": [roots[0]] if common else [],
            "resolution_basis": basis,
        },
        "residual": {"present": common, "reason": "shared_source_requires_qualification" if common else "none"},
        "posture": "CONTINUE_QUALIFIED_NO_INDEPENDENT_SUPPORT" if common else "CONTINUE_QUALIFIED",
        "affected_scope": observation["scope_id"],
        "handoff_target": observation["handoff_target"],
        "burden": {"processing_steps": steps, "modelled_time_steps": steps},
    }


def handoff_snapshot(observation: dict) -> tuple[tuple[str, str], ...]:
    """Immutable expected report identities/qualifiers captured before adapter access."""
    return tuple((r["report_id"], r["upstream_source_id"]) for r in observation["reports"])


def play_events(observation: dict, result: dict,
                expected_reports: tuple[tuple[str, str], ...]) -> list[dict]:
    events = []
    expected = dict(expected_reports)
    received = [r.get("report_id") for r in observation["reports"]]
    if len(received) != len(expected_reports) or set(received) != set(expected):
        events.append({"step": 0, "event": "report_set_mismatch",
                       "handoff_name": HANDOFF, "qualifier_loss_detected": True})
    for i, report in enumerate(observation["reports"], 1):
        report_id = report.get("report_id")
        loss = report_id not in expected or detect_qualifier_loss(report, expected[report_id], True)
        events.append({"step": i, "event": "received_report", "handoff_name": HANDOFF,
                       "qualifier_loss_detected": loss, "report": report})
    at = len(observation["reports"])
    if any(b.startswith("registry:") for b in result["dependency_assessment"]["resolution_basis"]):
        at += 1
        events.append({"step": at, "event": "context_registry_join",
                       "source_registry": observation["registry"]})
    at += 1
    events.append({"step": at, "event": "candidate_assessment", "assessment": result["dependency_assessment"]})
    at += 1
    events.append({"step": at, "event": "handoff", "handoff_name": "assessment_to_declared_receiving_owner",
                   "posture": result["posture"], "residual": result["residual"],
                   "affected_scope": result["affected_scope"]})
    return events


def score(branch: str, candidate: dict, oracle: dict, observation: dict,
          events: list[dict] | None = None) -> dict:
    """Post-run evaluator only: oracle is never passed to either adapter."""
    a = candidate["dependency_assessment"]
    common = branch != "Q1a-C0"
    correct = a["independent_support"] == oracle["independent_support"]
    correct &= a["shared_upstream_sources"] == oracle["shared_upstream_sources"]
    correct &= candidate["affected_scope"] == observation["scope_id"]
    correct &= candidate["handoff_target"] == observation["handoff_target"]
    burden = candidate["burden"]
    valid_burden = all(type(burden.get(key)) is int and 0 <= burden[key] <= limit
                       for key, limit in (("processing_steps", observation["processing_step_ceiling"]),
                                          ("modelled_time_steps", observation["deadline_step"])))
    if events is not None:
        measured_steps = max(e["step"] for e in events)
        valid_burden &= all(burden.get(k) == measured_steps for k in ("processing_steps", "modelled_time_steps"))
        correct &= not any(e.get("qualifier_loss_detected", False) for e in events)
    correct &= valid_burden
    retained = sum((candidate["residual"]["present"] is True,
                    isinstance(candidate["residual"]["reason"], str) and bool(candidate["residual"]["reason"].strip()),
                    candidate["affected_scope"] == observation["scope_id"])) if common else 0
    if common:
        correct &= retained == 3
        correct &= candidate["posture"] in ("REQUALIFY", "CONTINUE_QUALIFIED_NO_INDEPENDENT_SUPPORT")
        if branch == "Q1a-P2":
            correct &= all(b.startswith("registry:") for b in a["resolution_basis"])
    else:
        correct &= candidate["posture"] == "CONTINUE_QUALIFIED"
        correct &= candidate["residual"]["present"] is False
    return {"candidate_status": "PASS" if correct else "FAIL",
            "unsupported_independent_claim": int(common and a["independent_support"]),
            "unsupported_shared_closure": int(common and candidate["posture"] == "CONTINUE_QUALIFIED"),
            "required_residual_scope_fields_retained": retained,
            "required_residual_scope_fields": 3 if common else 0,
            "oracle_reference": oracle}


def run(output: Path) -> None:
    facts = json.loads((HERE / "frozen_observations_v05.json").read_text())
    if facts["pre_registration_commit"] != PRE_REG_COMMIT or set(facts["branches"]) != set(BRANCHES):
        raise ValueError("frozen branch or pre-registration mismatch")
    output.mkdir(parents=True, exist_ok=True)
    active = qualifier_loss_self_test(True)
    inactive = qualifier_loss_self_test(False)
    if active["disposition"] != "PASS" or inactive["disposition"] != "FAIL":
        raise RuntimeError("STOP: Step-0 instrumentation is not discriminating")
    for label, trace in (("active", active), ("detector_disabled", inactive)):
        (output / f"step0_{label}.json").write_bytes(canonical_trace_bytes(trace))

    # Candidate runtime runs first. Oracle is deliberately loaded after both
    # candidates have completed all six branch/configuration combinations.
    pending = []
    for branch in BRANCHES:
        observation = frozen_observation(facts["branches"][branch], facts["registry"])
        expected_reports = handoff_snapshot(observation)
        for config, adapter in (("B1", conventional_b1), ("B3", ea_profiled_b3)):
            repeats = []
            for _ in range(2):
                runtime_observation = deepcopy(observation)
                result, events, error = None, [], None
                try:
                    result = deepcopy(adapter(runtime_observation))
                    events = play_events(runtime_observation, result, expected_reports)
                except Exception as exc:
                    # Runtime/schema failure is distinct from a scored candidate failure.
                    error = {"type": type(exc).__name__, "message": str(exc)}
                repeats.append((runtime_observation, result, events, error))
            pending.append((branch, config, observation, repeats))

    oracle_table = json.loads((HERE / "oracle_reference_v05.json").read_text())
    if set(oracle_table) != set(BRANCHES):
        raise ValueError("oracle branch mismatch")
    hashes, failures = {}, []
    summary = {c: {"correlated_evidence_errors": 0, "false_convergence": 0,
                   "residual_scope_fields_retained": 0, "residual_scope_fields_required": 0,
                   "candidate_passes": 0, "runtime_errors": 0, "primary_denominator": 2,
                   "burden_per_branch": {}} for c in CONFIGS}
    for branch, config, observation, repeats in pending:
        payloads = []
        for repeat, (runtime_observation, result, events, error) in enumerate(repeats, 1):
            evaluation = {"candidate_status": "RUNTIME_ERROR"}
            if error is None:
                try:
                    evaluation = score(branch, result, oracle_table[branch], observation, events)
                except Exception as exc:
                    error = {"type": type(exc).__name__, "message": str(exc)}
            if error is not None:
                evaluation = {"candidate_status": "RUNTIME_ERROR", "error": error}
            trace = {"fixture_id": "RS-00E-Q1a", "branch": branch,
                     "configuration": config, "pre_registration_commit": PRE_REG_COMMIT,
                     "harness_revision": "audit-corrections-v1",
                     "facts_label": "facts self-declared", "comparator_label": "shared-logic instrumentation control",
                     "evidence_status": "Stage-0 stipulative verification",
                     "observation": observation, "runtime_observation": runtime_observation,
                     "runtime_events": events, "candidate": result,
                     "post_run_evaluation": evaluation,
                     "deviations": ["Post-audit instrumentation corrections (A14); distinct from the original preregistered execution."]}
            try:
                payload = canonical_trace_bytes(trace)
            except (ValueError, TypeError) as exc:
                # Invalid candidate values (e.g. CTv1-forbidden floats) must not
                # erase the failure. Preserve a textual diagnostic receipt.
                error = {"type": type(exc).__name__, "message": str(exc)}
                evaluation = {"candidate_status": "RUNTIME_ERROR", "error": error}
                trace = {"fixture_id": "RS-00E-Q1a", "branch": branch,
                         "configuration": config, "harness_revision": "audit-corrections-v1",
                         "pre_registration_commit": PRE_REG_COMMIT,
                         "post_run_evaluation": evaluation,
                         "rejected_trace_representation": repr(trace)}
                payload = canonical_trace_bytes(trace)
            if evaluation["candidate_status"] != "PASS":
                failures.append(f"{branch}/{config}/repeat{repeat}: {evaluation['candidate_status']}")
            if repeat == 1:
                row = summary[config]
                row["candidate_passes"] += int(evaluation["candidate_status"] == "PASS")
                row["runtime_errors"] += int(error is not None)
                row["correlated_evidence_errors"] += evaluation.get("unsupported_independent_claim", 0)
                row["false_convergence"] += evaluation.get("unsupported_shared_closure", 0)
                row["residual_scope_fields_retained"] += evaluation.get("required_residual_scope_fields_retained", 0)
                row["residual_scope_fields_required"] += 3 if branch != "Q1a-C0" else 0
                row["burden_per_branch"][branch] = {
                    "declared": (result.get("burden") if error is None and isinstance(result, dict)
                                 else {"runtime_error": True}),
                    "observed_event_steps": max((e["step"] for e in events), default=0)}
            filename = f"{branch}_{config}_repeat{repeat}.json"
            (output / filename).write_bytes(payload)
            hashes[filename] = hashlib.sha256(payload).hexdigest()
            payloads.append(payload)
        if payloads[0] != payloads[1]:
            failures.append(f"{branch}/{config}: NONDETERMINISTIC")
    (output / "manifest.json").write_text(json.dumps({
        "schema": "RS-00E-Q1a-stage0-manifest-v2",
        "pre_registration_commit": PRE_REG_COMMIT,
        "canonical_trace_version": "CTv1", "trace_sha256": hashes,
        "instrumentation": {"active": "PASS", "detector_disabled": "FAIL (required negative control)"},
        "summary": summary, "failures": failures,
        "interpretation": "descriptive shared-logic controls; not independent comparators or an EA differential",
    }, sort_keys=True, indent=2) + "\n")
    if failures:
        raise RuntimeError("evaluation failed; all traces preserved: " + "; ".join(failures))
    print("OK: Step-0 PASS; inverse-control FAIL as required; 12 CTv1 candidate traces; 6 identical replay pairs; both B1/B3 pass; no EA differential")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    run(parser.parse_args().output)
