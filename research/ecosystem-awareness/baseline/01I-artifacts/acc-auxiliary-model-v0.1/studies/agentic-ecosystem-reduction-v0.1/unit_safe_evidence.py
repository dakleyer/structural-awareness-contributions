"""Physical and information evidence from unchanged #57 source policies.

Run this entry point for architectural review. It preserves native plans and
reports physical gains, matched-output information prices and awareness signals
without converting prices into output or equating instrument axes with ACC K.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "intrinsic-abcd-economics-v0.1"))
from unit_safe_envelope import project_case
import agentic_reduction as source


def control_status(value):
    if value is None:
        return "UNKNOWN"
    if type(value) is not bool:
        raise ValueError("control needs explicit boolean evidence or None")
    return "PASS" if value else "FAIL"


def project_run(run):
    public = run["public_A"]
    arms = []
    resources = {}
    awareness = {}
    for name, result in run["arms"].items():
        plan = result["plan"]
        physical = result["observed_by_referee_only"]
        arms.append({"arm": name, "gross": str(physical["output"]),
                     "cost": str(plan["instrument_cost"]),
                     "components": {"source_instrument_price": str(plan["instrument_cost"])},
                     "status": plan["status"], "source": "agentic_reduction.run_case/" + name})
        resources[name] = {key: physical[key] for key in (
            "donor_resources_after", "recipient_resources_after",
            "coordination_resources_spent", "total_resources_same")}
        awareness[name] = {
            "conditional_near_gain": plan["conditional_near_gain"],
            "qualified_proposal": plan["qualified_proposal"],
            "evidence": plan["evidence"],
            "source_claim_supported_by_posthoc_truth": result["source_B_claim_supported_by_lab_truth"],
            "unit": "output_units",
            "meaning": "SOURCE_CONDITIONAL_INFORMATION_SIGNAL_NOT_EXECUTED_OUTPUT"}
    projected = project_case({
        "frame": {
            "case_id": run["id"], "model": "ACC_AGENTIC_REDUCTION_57",
            "scope": public["scope"], "question": "source-native mission transfer",
            "output_unit": "output_units", "cost_unit": "synthetic_value_units",
            "horizon": "one original decision",
            "public_contract_id": sha256(json.dumps(public, sort_keys=True).encode()).hexdigest(),
            "baseline_a": str(public["current_A_total_output"])},
        "baseline_arm": "A_ONLY", "arms": arms})
    projected["source_controls"] = {
        "capabilities": {key: control_status(public[key]) for key in (
            "metamorph_declared_in_A", "release_declared_in_A")},
        "governance": {key: control_status(public[key]) for key in (
            "release_consent", "meta_owner_authority")},
        "protocol": {"joint_protocol_available": control_status(public["joint_protocol_available"])},
        "epistemic": {"material_D_for_joint_decision": public["material_D_for_joint_decision"]}}
    projected["physical_resource_accounting"] = resources
    projected["source_awareness_signals"] = awareness
    projected["resource_accounting_rule"] = "OVERHEAD_IN_SOURCE_PHYSICAL_BUDGET_NO_SECOND_PRICE_CHARGE"
    projected["action_authorized_by_this_report"] = False
    return projected


def report():
    document = json.loads((HERE / "CASES.json").read_text(encoding="utf-8"))
    if document["schema"] != source.SCHEMA:
        raise ValueError("source fixture schema mismatch")
    cases = [project_run(source.run_case(case)) for case in document["cases"]]
    ids = [case["frame"]["case_id"] for case in cases]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate source case")
    base = next(case for case in document["cases"] if case["id"] == "AG01-QUALIFIED-NEAR-OPTIMUM")
    sweep = []
    for rate, overhead, qcost, peer_cost in product(
            (0.6, 2.0), (0.1, 0.25, 0.5, 0.75, 1.5),
            (0.05, 0.3, 0.8, 1.5), (0.1, 1.0, 3.0, 5.0)):
        case = deepcopy(base)
        case["id"] = f"SW-{rate}-{overhead}-{qcost}-{peer_cost}"
        case["truth_private"]["recipient_incremental_rate"] = rate
        case["public"]["overhead_resources"] = overhead
        case["Q"]["lower_rate"] = 1.6 if rate == 2.0 else 0.5
        case["Q"]["cost"] = qcost
        case["directed"]["measured_rate"] = rate
        case["directed"]["cost"] = peer_cost
        case["full_A"]["fully_measured_rate"] = rate
        sweep.append(project_run(source.run_case(case)))
    pins = {name: sha256((HERE / name).read_bytes()).hexdigest()
            for name in ("agentic_reduction.py", "CASES.json", "sensitivity.py")}
    return {"schema": "ACC-AGENTIC-UNIT-SAFE-EVIDENCE-v0.1", "cases": cases, "sweep": sweep,
            "case_count": len(cases), "sweep_count": len(sweep), "source_sha256": pins,
            "comparison": "PHYSICAL_GAINS_AND_MATCHED_OUTPUT_PRICES_NO_NETTING",
            "dimension_mapping": "AUTHOR_OWNED_NOT_INFERRED",
            "policy_decisions": "ORIGINAL_SOURCE_UNCHANGED",
            "evidence": "SYNTHETIC_STAGE_A"}


if __name__ == "__main__":
    print(json.dumps(report(), sort_keys=True, indent=2))

