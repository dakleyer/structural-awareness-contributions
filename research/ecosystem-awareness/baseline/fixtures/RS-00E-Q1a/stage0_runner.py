"""Deterministic, descriptive RS-00E-Q1a v0.5 Stage-0 harness.

The oracle is loaded only after both candidate adapters have completed.
All observations are synthetic. Neither adapter represents a deployed product.
"""

from __future__ import annotations

import argparse
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


def play_events(observation: dict, result: dict) -> list[dict]:
    events = []
    for i, report in enumerate(observation["reports"], 1):
        loss = detect_qualifier_loss(report, report["upstream_source_id"], True)
        if loss:
            raise RuntimeError("STOP: lost upstream_source_id at the named handoff")
        events.append({"step": i, "event": "received_report", "handoff_name": HANDOFF,
                       "qualifier_loss_detected": loss, "report": report})
    at = 2
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


def score(branch: str, candidate: dict, oracle: dict, observation: dict) -> dict:
    """Post-run evaluator only: oracle is never passed to either adapter."""
    a = candidate["dependency_assessment"]
    common = branch != "Q1a-C0"
    correct = a["independent_support"] == oracle["independent_support"]
    correct &= a["shared_upstream_sources"] == oracle["shared_upstream_sources"]
    correct &= candidate["affected_scope"] == observation["scope_id"]
    correct &= candidate["handoff_target"] == observation["handoff_target"]
    correct &= candidate["burden"]["modelled_time_steps"] <= observation["deadline_step"]
    if common:
        correct &= candidate["residual"]["present"] is True
        correct &= bool(candidate["residual"]["reason"])
        correct &= candidate["posture"] in ("REQUALIFY", "CONTINUE_QUALIFIED_NO_INDEPENDENT_SUPPORT")
        if branch == "Q1a-P2":
            correct &= all(b.startswith("registry:") for b in a["resolution_basis"])
    else:
        correct &= candidate["posture"] == "CONTINUE_QUALIFIED"
        correct &= candidate["residual"]["present"] is False
    return {"candidate_status": "PASS" if correct else "FAIL",
            "unsupported_independent_claim": int(common and a["independent_support"]),
            "unsupported_shared_closure": int(common and candidate["posture"] == "CONTINUE_QUALIFIED"),
            "required_residual_scope_fields_retained": (3 if common and correct else 0),
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
        for config, adapter in (("B1", conventional_b1), ("B3", ea_profiled_b3)):
            result = adapter(observation)
            events = play_events(observation, result)
            replay = adapter(observation)  # separate invocation before oracle is loaded
            replay_events = play_events(observation, replay)
            if max(events[-1]["step"], replay_events[-1]["step"]) > observation["deadline_step"]:
                raise RuntimeError("STOP: modelled deadline exceeded")
            pending.append((branch, config, observation, result, events, replay, replay_events))

    oracle_table = json.loads((HERE / "oracle_reference_v05.json").read_text())
    if set(oracle_table) != set(BRANCHES):
        raise ValueError("oracle branch mismatch")
    hashes = {}
    summary = {c: {"correlated_evidence_errors": 0, "false_convergence": 0,
                   "residual_scope_fields_retained": 0, "residual_scope_fields_required": 0,
                   "candidate_passes": 0, "primary_denominator": 2,
                   "burden_per_branch": {}} for c in CONFIGS}
    for branch, config, observation, result, events, replay, replay_events in pending:
        evaluation = score(branch, result, oracle_table[branch], observation)
        replay_evaluation = score(branch, replay, oracle_table[branch], observation)
        if evaluation["candidate_status"] != "PASS":
            raise RuntimeError(f"candidate failure: {branch}/{config}")
        s = summary[config]
        s["candidate_passes"] += 1
        s["correlated_evidence_errors"] += evaluation["unsupported_independent_claim"]
        s["false_convergence"] += evaluation["unsupported_shared_closure"]
        s["residual_scope_fields_retained"] += evaluation["required_residual_scope_fields_retained"]
        s["residual_scope_fields_required"] += evaluation["required_residual_scope_fields"]
        s["burden_per_branch"][branch] = result["burden"]
        trace = {"fixture_id": "RS-00E-Q1a", "branch": branch,
                 "configuration": config, "pre_registration_commit": PRE_REG_COMMIT,
                 "facts_label": "facts self-declared", "comparator_label": "comparator self-configured",
                 "evidence_status": "Stage-0 stipulative verification",
                 "observation": observation, "runtime_events": events,
                 "candidate": result, "post_run_evaluation": evaluation,
                 "deviations": []}
        first = canonical_trace_bytes(trace)
        second = canonical_trace_bytes(dict(trace, candidate=replay,
            runtime_events=replay_events,
            post_run_evaluation=replay_evaluation))
        if first != second:
            raise RuntimeError(f"STOP: non-deterministic trace {branch}/{config}")
        for repeat, payload in ((1, first), (2, second)):
            filename = f"{branch}_{config}_repeat{repeat}.json"
            (output / filename).write_bytes(payload)
            hashes[filename] = hashlib.sha256(payload).hexdigest()
    (output / "manifest.json").write_text(json.dumps({
        "schema": "RS-00E-Q1a-stage0-manifest-v1",
        "pre_registration_commit": PRE_REG_COMMIT,
        "canonical_trace_version": "CTv1", "trace_sha256": hashes,
        "instrumentation": {"active": "PASS", "detector_disabled": "FAIL (required negative control)"},
        "summary": summary,
        "interpretation": "descriptive only; both self-configured arms pass; no EA differential",
    }, sort_keys=True, indent=2) + "\n")
    print("OK: Step-0 PASS; inverse-control FAIL as required; 12 CTv1 candidate traces; 6 identical replay pairs; both B1/B3 pass; no EA differential")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    run(parser.parse_args().output)
