"""Source-native adapters for ACC social #44 and agentic #57.

The source's own policy/plan/scorer runs first. This file only transcribes its
actual outputs, costs and public reference into the shared accounting contract.
"""
from __future__ import annotations

from copy import deepcopy
from dataclasses import fields
from hashlib import sha256
import json
from typing import Any, Mapping, Sequence

from economic_envelope import (
    ArmObservation, ComparisonFrame, CostLedger, quantity,
)


def _fingerprint(public_payload: Any) -> str:
    """Bind a comparison to a public contract, not to its private referee."""
    encoded = json.dumps(public_payload, sort_keys=True, separators=(",", ":"),
                         ensure_ascii=False).encode("utf-8")
    return sha256(encoded).hexdigest()


def intrinsic_cost_override(producer: Any, changes: Mapping[str, Any]) -> Any:
    """Build original Costs with caller-supplied prices, preserving its contract."""
    if not isinstance(changes, Mapping):
        raise TypeError("cost override must be a mapping")
    allowed = {field.name for field in fields(producer.Costs)}
    if set(changes) - allowed:
        raise ValueError("unknown intrinsic source cost: " + str(sorted(set(changes) - allowed)))
    defaults = {field.name: getattr(producer.Costs(), field.name) for field in fields(producer.Costs)}
    for name, value in changes.items():
        q = quantity(value)
        if q < 0:
            raise ValueError("negative source cost: " + name)
        defaults[name] = float(q)
    return producer.Costs(**defaults)


def intrinsic_observations(
    producer: Any, world: Any, target: str, costs: Any, *,
    scenario_id: str, minimum: int = 8, extra: int = 2,
    issued_at: int = 5, now: int = 6, ttl: int = 10,
    planner_budget: float = 1000,
) -> tuple[ArmObservation, ...]:
    """Run original #44 fixed arms AND original public-information receiver.

    B is issued for exactly target and extra; this never composes certificates.
    Only source policy sees private world in the referee/scoring stage.
    """
    public = producer.observe_view(world, minimum=minimum)
    path = producer.path_to(world, target)
    if not path:
        raise ValueError("target absent from original world")
    b = producer.upstream_B(world, target, now=issued_at, ttl=ttl,
                            minimum=minimum, extra=extra)
    outline = repr(public.outline)  # dataclass: names/versions only
    frame = ComparisonFrame(
        case_id=scenario_id, model="ACC_SOCIAL_INTRINSIC_44",
        scope="intrinsic-abcd-economics-v0.1",
        question=f"future marginal output: target={target}, minimum={minimum}, extra={extra}",
        metric="synthetic_net_earned_for_one_question",
        output_unit="output_units", cost_unit="synthetic_value_units",
        horizon=f"issued={issued_at};use={now};ttl={ttl}",
        public_contract_id=_fingerprint({"outline": outline, "current_A": public.current_A,
                                         "target": target, "minimum": minimum, "extra": extra}),
        baseline_a=public.current_A,
    )

    def b_ledger() -> CostLedger:
        return CostLedger.of({
            "qualified_path_issuance": len(path) * costs.b_issuance_per_path_node,
            "qualified_transmission": costs.b_transmission,
            "qualified_maintenance": costs.b_maintenance,
        })

    all_accessible = all(n.source_can_assess for n in producer._nodes_all(world)) if hasattr(producer, "_nodes_all") else None
    if all_accessible is None:
        # Same recursive predicate as the original FULL_EXPAND_A mode.
        def accessible(n):
            return n.source_can_assess and (
                isinstance(n, producer.Leaf) or all(accessible(c) for c in n.children))
        all_accessible = accessible(world)
    targeted_accessible = all(n.source_can_assess for n in path)
    arms: list[ArmObservation] = []
    for mode in ("A_ONLY", "B_QUALIFIED", "TARGETED_EXPLORATION_OF_A", "FULL_EXPAND_A"):
        result = producer.policy(world, target, mode, costs, now=now, b=b,
                                 minimum=minimum, extra=extra)
        if quantity(result["observed_current_A"]) != frame.baseline_a:
            raise ValueError("original source has changed physical A between policies")
        if mode == "B_QUALIFIED" and b is not None:
            ledger = b_ledger()
        elif mode == "TARGETED_EXPLORATION_OF_A" and targeted_accessible:
            ledger = CostLedger.of({"targeted_source_observation": costs.target_observation})
        elif mode == "FULL_EXPAND_A" and all_accessible:
            ledger = CostLedger.of({"full_source_nodes": producer.node_count(world) * costs.full_node})
        else:
            ledger = CostLedger()
        arms.append(ArmObservation(
            frame, mode, result["gross_realized_value_SYNTHETIC"], ledger,
            result["status"], "intrinsic_abcd.policy/" + mode,
            "POST_HOC_SYNTHETIC_REFEREE",
            source_net=result["net_realized_value_SYNTHETIC"],
            source_cost=result["information_cost_declared"],
            rounding_tolerance="0.000000001",
        ))

    # Distinct from a fixed policy arm: the source's existing receiver decides
    # using public A/B and budget; only the subsequent scorer sees world truth.
    actual = producer.receiver_decision(
        world, target, costs, budget=planner_budget, now=now, b=b,
        minimum=minimum, extra=extra,
    )
    expense = quantity(actual["estimated_information_cost"])
    ledger = b_ledger() if expense else CostLedger()
    arms.append(ArmObservation(
        frame, "SOURCE_PUBLIC_RECEIVER", actual["gross_realized_value_SYNTHETIC"],
        ledger, actual["decision_rule"], "intrinsic_abcd.receiver_decision",
        "POST_HOC_SYNTHETIC_REFEREE",
        source_net=actual["net_realized_value_SYNTHETIC"],
        source_cost=actual["estimated_information_cost"],
        rounding_tolerance="0.000000001",
    ))
    return tuple(arms)


AGENTIC_COST_FIELDS = frozenset({
    "Q.cost", "directed.cost", "directed.equivalent_Q_cost", "full_A.cost",
})


def agentic_cost_override(scenario: Mapping[str, Any],
                          changes: Mapping[str, Any]) -> dict[str, Any]:
    """Change only declared instrument prices, never world/authority/mission."""
    if not isinstance(scenario, Mapping) or not isinstance(changes, Mapping):
        raise TypeError("scenario and overrides must be mappings")
    if set(changes) - AGENTIC_COST_FIELDS:
        raise ValueError("unknown source cost: " + str(sorted(set(changes) - AGENTIC_COST_FIELDS)))
    copy = deepcopy(dict(scenario))
    for qualified_key, value in changes.items():
        parent, key = qualified_key.split(".", 1)
        if not isinstance(copy.get(parent), dict):
            raise ValueError("cannot override absent cost section " + parent)
        q = quantity(value)
        if q < 0:
            raise ValueError("negative source cost: " + qualified_key)
        copy[parent][key] = float(q)
    return copy


def agentic_observations(agentic: Any, scenario: Mapping[str, Any], *,
                         scenario_id: str | None = None) -> tuple[ArmObservation, ...]:
    """Execute every original #57 arm, with post-hoc scorer kept in that source.

    The physical overhead of transferring resources is already in the source
    output, so it MUST NOT be charged again as an information/cash cost.
    """
    run = agentic.run_case(dict(scenario))
    public = run["public_A"]
    baseline = quantity(public["current_A_total_output"])
    frame = ComparisonFrame(
        case_id=scenario_id or run["id"], model="ACC_AGENTIC_REDUCTION_57",
        scope=public["scope"],
        question=f"one authorized mission transfer, target={public['mission_target']}",
        metric="mission_physical_output_with_source_instrument_cost",
        output_unit="output_units", cost_unit="synthetic_value_units",
        horizon="one source-native decision and referee observation",
        public_contract_id=_fingerprint(public), baseline_a=baseline,
    )
    arms: list[ArmObservation] = []
    for mode in agentic.ARMS:
        result = run["arms"][mode]
        plan = result["plan"]
        posthoc = result["observed_by_referee_only"]
        if abs(quantity(posthoc["total_resources_same"]) - quantity(public["total_resources"])) > quantity("0.00001"):
            raise ValueError("agentic native policy violates conserved resources")
        if abs(quantity(result["mission_output_before"]) - baseline) > quantity("0.0001"):
            raise ValueError("agentic policy uses a different physical A")
        ledger = CostLedger.of({"source_instrument_price": plan["instrument_cost"]})
        arms.append(ArmObservation(
            frame, mode, posthoc["output"], ledger, plan["status"],
            "agentic_reduction.run_case/" + mode,
            "POST_HOC_SYNTHETIC_REFEREE",
            source_net=result["mission_net_value_after_information_cost"],
            source_cost=plan["instrument_cost"],
            rounding_tolerance="0.0001",
        ))
    return tuple(arms)
