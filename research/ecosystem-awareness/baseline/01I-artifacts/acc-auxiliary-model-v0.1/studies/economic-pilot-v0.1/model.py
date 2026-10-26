"""Deterministic toy model. No native ACC, EA, DDS or UC21 implementation."""
from __future__ import annotations

from copy import deepcopy
from decimal import Decimal, InvalidOperation
import hashlib
import json

ZERO = Decimal(0)


def amount(value):
    if type(value) not in (int, float, str):
        raise ValueError("A numeric amount is required")
    try:
        result = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError("Invalid amount") from exc
    if not result.is_finite():
        raise ValueError("Nonfinite amount")
    return result


def vector(values):
    if not isinstance(values, list) or len(values) != 4:
        raise ValueError("Exactly four actor amounts are required")
    return [amount(value) for value in values]


def merge(state, change):
    result = deepcopy(state)
    for key, value in change.items():
        result[key] = merge(result[key], value) if isinstance(value, dict) and isinstance(result.get(key), dict) else deepcopy(value)
    return result


def fingerprint(snapshot):
    return hashlib.sha256(json.dumps(snapshot, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def grant_valid(state, tick):
    grant = state.get("grant", {})
    expiry = grant.get("expires_at")
    return (grant.get("active") is True and type(expiry) is int and tick <= expiry
            and grant.get("scope") == "company-improvement")


def block_reason(view, tick):
    if not grant_valid(view, tick):
        return "HOLD_GRANT"
    if view.get("purpose_active") is not True:
        return "HOLD_PURPOSE"
    if view.get("freeze") is not False:
        return "HOLD_FREEZE"
    if not view.get("version") or view.get("approved_version") != view.get("version"):
        return "HOLD_APPROVAL"
    if view.get("rights") is not True:
        return "HOLD_RIGHTS"
    if view.get("complete_service") is not True:
        return "HOLD_SERVICE"
    if view.get("participation") != ["yes"] * 4:
        return "HOLD_PARTICIPATION"
    return None


def choose(view, tick, protocol):
    """Receives the admitted observation only, never simulator truth or oracle."""
    hold = block_reason(view, tick)
    if hold:
        return {"action": hold, "basis_version": view.get("version")}
    try:
        benefits = vector(view.get("benefits"))
        costs = vector(view.get("transition_costs"))
        limits = vector(view.get("debit_limits"))
    except ValueError:
        return {"action": "HOLD_INFORMATION", "basis_version": view.get("version")}
    if any(v < ZERO for v in costs + limits):
        return {"action": "HOLD_INFORMATION", "basis_version": view.get("version")}
    fee = amount(protocol["costs"]["review_per_step"])
    for raw_transfer in protocol["transfer_options"]:
        transfer = vector(raw_transfer)
        if sum(transfer) != ZERO or any(-t > limit for t, limit in zip(transfer, limits)):
            continue
        net = [b + t - c - (fee if i == 0 else ZERO) for i, (b, t, c) in enumerate(zip(benefits, transfer, costs))]
        if min(net) >= ZERO:
            return {"action": "EXECUTE_IMMEDIATE" if not any(transfer) else "EXECUTE_ADJUSTED",
                    "basis_version": view["version"], "transfer": raw_transfer,
                    "estimated_net_after_review": [float(x) for x in net]}
    return {"action": "HOLD_NO_AGREEMENT", "basis_version": view.get("version")}


class Policy:
    """Matched decision rules; the qualified arm additionally records changes."""
    def __init__(self, name, protocol):
        self.name = name
        self.protocol = protocol
        self.first_decision = None
        self.previous_fingerprint = None
        self.inquiries = 0

    def decide(self, observation, tick):
        observed_hash = fingerprint(observation)
        changed = self.previous_fingerprint is not None and observed_hash != self.previous_fingerprint
        if self.name == "stale_reference" and self.first_decision is not None:
            decision = deepcopy(self.first_decision)
        elif observation.get("unexplained_block") is True:
            budget = self.protocol["unresolved_cause_rule"]["maximum_inquiries"]
            action = "HOLD_INQUIRY" if self.inquiries < budget else "HOLD_CAUSE_UNRESOLVED"
            if self.inquiries < budget:
                self.inquiries += 1
            decision = {"action": action, "basis_version": observation.get("version")}
        else:
            decision = choose(observation, tick, self.protocol)
        if self.first_decision is None:
            self.first_decision = deepcopy(decision)
        self.previous_fingerprint = observed_hash
        return dict(decision, observation_sha256=observed_hash,
                    material_change_observed=changed,
                    qualified_record=self.name == "qualified_record")


def actual_admissibility(state, tick, request, transfer, fee):
    """Investigator-side effect adjudication, separate from policy selection."""
    failures = []
    for field, expected in [("purpose_active", True), ("freeze", False), ("rights", True), ("complete_service", True)]:
        if state.get(field) is not expected:
            failures.append(field)
    if request.get("basis_version") != state.get("version") or state.get("approved_version") != state.get("version"):
        failures.append("current_basis")
    if state.get("participation") != ["yes"] * 4:
        failures.append("participation")
    benefits, costs, limits = vector(state["benefits"]), vector(state["transition_costs"]), vector(state["debit_limits"])
    actual_net = [b + t - c for b, t, c in zip(benefits, transfer, costs)]
    if sum(transfer) != ZERO or any(-t > bound for t, bound in zip(transfer, limits)):
        failures.append("transfer_feasibility")
    if any(value - (fee if i == 0 else ZERO) < ZERO for i, value in enumerate(actual_net)):
        failures.append("actor_balance")
    return failures, actual_net


def oracle_opportunity(state, tick, protocol):
    """Whether an admissible alternative exists in full simulator information."""
    if not grant_valid(state, tick) or state.get("unexplained_block") is True:
        return False
    for transfer in protocol["transfer_options"]:
        failures, _ = actual_admissibility(state, tick, {"basis_version": state.get("version")}, vector(transfer), amount(protocol["costs"]["review_per_step"]))
        if not failures:
            return True
    return False


def run_case(case, policy_name, protocol):
    policy = Policy(policy_name, protocol)
    actual = deepcopy(case["initial_state"])
    completed = set()
    preparation = amount(protocol["costs"]["preparation"])
    review_fee = amount(protocol["costs"]["review_per_step"])
    actor_ledger = [-preparation, ZERO, ZERO, ZERO]
    operating = ZERO
    trace = []
    effects = legitimate = invalid = missed = duplicates = 0
    for index, step in enumerate(case["steps"]):
        actual = merge(actual, step["actual_change"])
        observation = merge(actual, step["visible_override"])
        tick, job = step["tick"], step["job"]
        actor_ledger[0] -= review_fee
        before = deepcopy(actual)
        decision = policy.decide(observation, tick)
        requested = decision["action"]
        event = {"case_id": case["id"], "policy": policy_name, "step": index, "tick": tick,
                 "job": job, "phase": step["phase"], "request": decision,
                 "attempted": False, "effect": False, "effect_legitimate": None,
                 "violations": [], "review_cost_incurred": float(review_fee)}
        if job in completed:
            event["action"] = "ALREADY_EXECUTED"
            duplicates += 1
        elif not requested.startswith("EXECUTE_"):
            event["action"] = requested
            if step["phase"] == "attempt" and oracle_opportunity(actual, tick, protocol):
                missed += 1
        elif step["phase"] == "plan":
            event["action"] = requested.replace("EXECUTE_", "PLAN_")
        else:
            event["attempted"] = True
            if not grant_valid(actual, tick):
                event["action"] = "ATTEMPT_BLOCKED"
                event["violations"] = ["technical_grant"]
                invalid += 1
            else:
                transfer = vector(decision["transfer"])
                violations, net = actual_admissibility(actual, tick, decision, transfer, review_fee)
                for i, value in enumerate(net):
                    actor_ledger[i] += value
                operating += sum(net)
                effects += 1
                completed.add(job)
                event.update(action=requested, effect=True, effect_legitimate=not violations,
                             violations=violations, transfer=[float(x) for x in transfer],
                             actual_net_before_review=[float(x) for x in net])
                if violations:
                    invalid += 1
                else:
                    legitimate += 1
        # Reserved to the investigator and result trace, never passed to Policy.
        event["investigator_actual_state_sha256"] = fingerprint(before)
        event["cumulative_actor_net"] = [float(x) for x in actor_ledger]
        trace.append(event)
    return {"case_id": case["id"], "policy": policy_name,
            "scenario_outcome": "FAIL" if invalid else ("PASS" if effects else "HOLD"),
            "operating_surplus": float(operating), "full_net": float(sum(actor_ledger)),
            "actor_net": [float(x) for x in actor_ledger], "preparation_cost": float(preparation),
            "review_cost": float(review_fee * len(case["steps"])),
            "actual_effects": effects, "legitimate_effects": legitimate, "invalid_attempts": invalid,
            "oracle_opportunities_unrealized": missed, "duplicate_effects_prevented": duplicates,
            "inquiries": policy.inquiries, "actions": [x["action"] for x in trace], "trace": trace}


def bounded_controls():
    """Separate toy controls, not scales of real happiness or intelligence."""
    benefit, visible_discomfort, hidden_discomfort = amount(5), amount(7), amount(0)
    visible_score, hidden_score = benefit - visible_discomfort, benefit - hidden_discomfort
    total, avoidable, recovered = amount(10), amount(5), amount(2)
    before, after, transition = amount(200), amount(180), amount(3)
    return {
        "information_incentive": {"B": 5, "F_visible": 7, "F_hidden_assumed": 0,
            "W_visible": float(visible_score), "W_hidden": float(hidden_score), "physical_state_changed": False,
            "W_only_gate_visible": "ACCEPT" if visible_score >= ZERO else "REJECT", "W_only_gate_hidden": "ACCEPT" if hidden_score >= ZERO else "REJECT",
            "gate_preserving_agreed_information_access_hidden": "REJECT",
            "human_measurement": False},
        "human_capacity": {"GIC_initial": 3, "NEO": 2, "ACW_avoidable": 5, "denominator": 10,
            "HID_observed": float(avoidable / total), "HID_potential_if_full_conversion_available_and_chosen": float(avoidable / total),
            "additional_GIC_recovered": float(recovered), "recovered_ratio": float(recovered / total), "unrecovered_releasable_ratio": float((avoidable - recovered) / total),
            "rest_is_permitted": True, "heterogeneous_unconvertible_scalar": None,
            "skill_loss_measured": False},
        "equivalent_service": {"same_complete_output": True, "input_before": 200,
            "input_after": 180, "transition_cost": 3, "net_resource_saving": float(before - after - transition),
            "lower_quality_is_equivalent": False},
    }
