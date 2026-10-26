"""Synthetic intrinsic A/B/C/D economic study under recursive composition.

This is not an epistemic classifier, general theorem about complexity,
probability model of the open exterior, or observed measurement of suffering.

Only the *laboratory* knows private capacities. Receivers obtain current A,
optionally an upstream qualified B for one future question, and cost ledgers.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import ceil, log2
from typing import Union
import json


@dataclass(frozen=True)
class Leaf:
    name: str
    capacity: int
    source_can_assess: bool = True
    version: str = "v1"

    def __post_init__(self):
        if not self.name or self.capacity < 0:
            raise ValueError("invalid leaf")


@dataclass(frozen=True)
class Module:
    name: str
    children: tuple["Node", ...]
    throughput_ceiling: int | None = None
    source_can_assess: bool = True
    version: str = "v1"

    def __post_init__(self):
        if not self.name or not self.children:
            raise ValueError("module requires an identity and children")
        if self.throughput_ceiling is not None and self.throughput_ceiling < 0:
            raise ValueError("negative throughput")


Node = Union[Leaf, Module]


@dataclass(frozen=True)
class OutlineLeaf:
    name: str
    version: str


@dataclass(frozen=True)
class OutlineModule:
    name: str
    children: tuple["Outline", ...]
    version: str


Outline = Union[OutlineLeaf, OutlineModule]


def public_outline(node: Node) -> Outline:
    """Projects away capacity and private access; receiver cannot read them."""
    if isinstance(node, Leaf):
        return OutlineLeaf(node.name, node.version)
    return OutlineModule(node.name, tuple(public_outline(c) for c in node.children),
                         node.version)


def outline_path(node: Outline, target: str) -> tuple[Outline, ...]:
    if isinstance(node, OutlineLeaf):
        return (node,) if node.name == target else ()
    if not isinstance(node, OutlineModule):
        raise TypeError("receiver must receive capacity-free public outline")
    for child in node.children:
        p = outline_path(child, target)
        if p:
            return (node,) + p
    return ()


@dataclass(frozen=True)
class PublicView:
    outline: Outline
    current_A: int
    horizon_version: str = "v1"


def observe_view(node: Node, *, minimum: int = 8) -> PublicView:
    return PublicView(public_outline(node), deliver(node, base_demand(node, minimum)))


def descendants(node: Node) -> tuple[Leaf, ...]:
    if isinstance(node, Leaf):
        return (node,)
    return tuple(leaf for child in node.children for leaf in descendants(child))


def node_count(node: Node) -> int:
    return 1 if isinstance(node, Leaf) else 1 + sum(node_count(x) for x in node.children)


def deliver(node: Node, demand_by_leaf: dict[str, int]) -> int:
    """Evaluated by a PRIVATE simulator, not automatically visible upstream."""
    if isinstance(node, Leaf):
        requested = demand_by_leaf.get(node.name)
        if requested is None or type(requested) is not int or requested < 0:
            raise ValueError("demand missing or invalid")
        return min(node.capacity, requested)
    output = sum(deliver(child, demand_by_leaf) for child in node.children)
    return min(output, node.throughput_ceiling) if node.throughput_ceiling is not None else output


def balanced_tree(bits: tuple[int, ...], *, base: int = 8,
                  upper: int = 2, cap_root: int | None = None,
                  inaccessible_path_leaf: int | None = None) -> Module:
    """Builds a known finite test world, not a claim to know D's extension."""
    if len(bits) < 2 or any(bit not in (0, 1) for bit in bits):
        raise ValueError("bits must encode >=2 independently variable capacities")
    if base < 0 or upper < 0:
        raise ValueError("invalid production parameters")
    leaves = tuple(Leaf(f"source-{i}", base + upper * bit,
                        source_can_assess=i != inaccessible_path_leaf)
                   for i, bit in enumerate(bits))

    def make(level: tuple[Node, ...], depth: int) -> Node:
        if len(level) == 1:
            return level[0]
        pairs = []
        for i in range(0, len(level), 2):
            pair = level[i:i + 2]
            pairs.append(Module(f"layer-{depth}-part-{i // 2}", tuple(pair)))
        return make(tuple(pairs), depth + 1)

    top = make(leaves, 1)
    return Module("root", (top,), throughput_ceiling=cap_root)


def base_demand(world: Node, minimum: int = 8) -> dict[str, int]:
    return {leaf.name: minimum for leaf in descendants(world)}


def selected_demand(world: Node, target: str, *, minimum: int = 8,
                    extra: int = 2) -> dict[str, int]:
    demand = base_demand(world, minimum)
    if target not in demand:
        raise ValueError("unknown target")
    if type(extra) is not int or extra < 0:
        raise ValueError("invalid increment")
    demand[target] += extra
    return demand


def path_to(node: Node, target: str) -> tuple[Node, ...]:
    if isinstance(node, Leaf):
        return (node,) if node.name == target else ()
    for child in node.children:
        p = path_to(child, target)
        if p:
            return (node,) + p
    return ()


@dataclass(frozen=True)
class QualifiedB:
    """Synthetic upstream certificate for a *specified* decision. Not cryptographic."""
    source: str
    target: str
    delivered_if_requested: int
    question_input: int
    path_ids: tuple[str, ...]
    path_versions: tuple[str, ...]
    issued_at: int
    expires_at: int
    source_evidence: str


def source_current_log(node: Node, demand: dict[str, int]) -> dict[str, int]:
    """SYNTHETIC PRODUCER'S ALREADY-OPERATED native output ledger.

    Logs are captured while the current service actually operates. In a
    real deployment their creation, retention and accessibility need costs
    and provenance. No future scenario is run to produce this log.
    """
    logs: dict[str, int] = {}

    def visit(n: Node) -> int:
        if isinstance(n, Leaf):
            current = min(n.capacity, demand[n.name])
        else:
            raw = sum(visit(child) for child in n.children)
            current = min(raw, n.throughput_ceiling) if n.throughput_ceiling is not None else raw
        logs[n.name] = current
        return current

    visit(node)
    return logs


def upstream_B(world: Node, target: str, *, now: int, ttl: int,
               minimum: int = 8, extra: int = 2) -> QualifiedB | None:
    """Producer issues a B only when its CURRENT logs + characterized
    headroom of every relevant path node suffice for this fixed demand.

    Critically NO future whole-world simulation is used to obtain the
    qualification; only source-native current log + specific headrooms.
    The source's capability and the logging/maintenance cost are assumptions.
    """
    path = path_to(world, target)
    if not path or ttl < 0 or type(now) is not int:
        raise ValueError("missing target or malformed time")
    if not all(n.source_can_assess for n in path):
        return None
    if minimum < 0 or extra < 0 or type(extra) is not int:
        raise ValueError("invalid question")
    current_outputs = source_current_log(world, base_demand(world, minimum))
    leaf = path[-1]
    if not isinstance(leaf, Leaf):
        raise AssertionError("path must end at source leaf")
    increment = min(extra, max(0, leaf.capacity - current_outputs[leaf.name]))
    for ancestor in path[:-1]:
        if isinstance(ancestor, Module) and ancestor.throughput_ceiling is not None:
            increment = min(increment, max(0, ancestor.throughput_ceiling - current_outputs[ancestor.name]))
    return QualifiedB(source="synthetic-producer-record", target=target,
                      delivered_if_requested=increment, question_input=extra,
                      path_ids=tuple(x.name for x in path),
                      path_versions=tuple(x.version for x in path),
                      issued_at=now, expires_at=now + ttl,
                      source_evidence="DECLARED_SOURCE_NATIVE_NOT_INDEPENDENTLY_ATTESTED")


def receiver_B_valid(world_skeleton: Outline, record: QualifiedB | None,
                     target: str, *, now: int, extra: int = 2) -> tuple[bool, str]:
    """Checks the declared source/scope/time/path of B, not its truthfulness."""
    if not isinstance(world_skeleton, (OutlineLeaf, OutlineModule)):
        raise TypeError("receiver may only validate against public capacity-free outline")
    if record is None:
        return False, "NO_QUALIFICATION"
    if record.source != "synthetic-producer-record":
        return False, "SOURCE_NOT_ALLOWED"
    if record.target != target or record.question_input != extra:
        return False, "WRONG_QUESTION"
    if not record.issued_at <= now <= record.expires_at:
        return False, "STALE"
    path = outline_path(world_skeleton, target)
    if (record.path_ids != tuple(n.name for n in path)
            or record.path_versions != tuple(n.version for n in path)):
        return False, "PATH_OR_VERSION_MISMATCH"
    if (type(record.delivered_if_requested) is not int
            or not 0 <= record.delivered_if_requested <= extra):
        return False, "BAD_BOUND"
    return True, "DECLARED_B_VALID_SCOPE_NOT_AUTHENTICATED"


@dataclass(frozen=True)
class ExplorationC:
    source: str
    grounded_avenue: str
    question_target: str
    targets_and_method_characterized: bool = False

    def __post_init__(self):
        if not self.grounded_avenue or not self.question_target or self.targets_and_method_characterized:
            raise ValueError("C requires a situated avenue, but not a characterized B")


@dataclass(frozen=True)
class MaterialD:
    source: str
    witnessed_material_influence: str
    question_target: str
    has_effective_evaluation_route: bool = False

    def __post_init__(self):
        if not self.witnessed_material_influence or not self.question_target or self.has_effective_evaluation_route:
            raise ValueError("D must be a situated material witness with no effective route")


def route_status(claim: ExplorationC | MaterialD | None) -> str:
    if claim is None:
        return "ROLE_NOT_ESTABLISHED"
    if isinstance(claim, ExplorationC):
        return "C_GROUNDED_AVENUE_UNCHARACTERIZED_ROI"
    if isinstance(claim, MaterialD):
        return "D_MATERIAL_EFFECT_NOT_ASSESSABLE"
    raise TypeError("unrecognized claim")


@dataclass(frozen=True)
class Costs:
    full_node: float = 1.0
    target_observation: float = 3.0
    b_issuance_per_path_node: float = 0.25
    b_transmission: float = 0.50
    b_maintenance: float = 0.25
    false_promise: float = 8.0
    value_per_unit: float = 5.0

    def __post_init__(self):
        if any(type(x) not in (float, int) or x < 0 or x != x or x == float("inf")
               for x in self.__dict__.values()):
            raise ValueError("all cost entries must be finite and nonnegative")


def policy(world: Node, target: str, mode: str, costs: Costs,
           *, now: int = 0, b: QualifiedB | None = None,
           minimum: int = 8, extra: int = 2) -> dict:
    """Finite laboratory score with conservation of the actual operational A.

    Modes: A_ONLY, B_QUALIFIED, TARGETED_EXPLORATION_OF_A, FULL_EXPAND_A.
    The simulator uses private truth to score EFFECTS, never to fabricate B.
    """
    path = path_to(world, target)
    if not path:
        raise ValueError("target not in tree")
    actual_current = deliver(world, base_demand(world, minimum))
    actual_future = deliver(world, selected_demand(world, target,
                                                   minimum=minimum, extra=extra))
    capacity_gain = actual_future - actual_current
    full_cost = node_count(world) * costs.full_node
    b_cost = len(path) * costs.b_issuance_per_path_node + costs.b_transmission + costs.b_maintenance
    promised_increment = 0
    cost = 0.0
    status = "CONSERVATIVE_A"
    if mode == "A_ONLY":
        pass
    elif mode == "FULL_EXPAND_A":
        # Full analysis needs access to every characterized inner component.
        def all_accessible(n: Node) -> bool:
            return n.source_can_assess and (isinstance(n, Leaf) or
                     all(all_accessible(c) for c in n.children))
        if all_accessible(world):
            cost = full_cost
            promised_increment = capacity_gain
            status = "FULL_FINITE_MODEL_ACQUIRED"
        else:
            status = "FULL_SCOPE_NOT_ACCESSIBLE"
    elif mode == "TARGETED_EXPLORATION_OF_A":
        if all(n.source_can_assess for n in path):
            cost = costs.target_observation
            promised_increment = capacity_gain
            status = "TARGETED_SOURCE_ASSESSMENT_ACQUIRED"
        else:
            status = "TARGETED_NO_EFFECTIVE_ROUTE"
    elif mode == "B_QUALIFIED":
        if b is not None:
            cost = b_cost  # communication/maintenance count even if receiver rejects
        valid, status = receiver_B_valid(public_outline(world), b, target, now=now, extra=extra)
        if valid:
            promised_increment = b.delivered_if_requested
    else:
        raise ValueError("unsupported mode")
    observed_mismatch = promised_increment > capacity_gain
    if observed_mismatch:
        gross = -costs.false_promise
    elif promised_increment <= capacity_gain:
        gross = costs.value_per_unit * promised_increment
    else:
        raise AssertionError("unreachable")
    return {
        "mode": mode,
        "observed_current_A": actual_current,
        "question": f"future total incremental output for {target} when extra={extra}",
        "promised_increment": promised_increment,
        "physical_increment_PRIVATE_ORACLE": capacity_gain,
        "false_promise_PRIVATE_ORACLE": observed_mismatch,
        "gross_realized_value_SYNTHETIC": gross,
        "information_cost_declared": cost,
        "net_realized_value_SYNTHETIC": gross - cost,
        "status": status,
        "indeterminacy_of_outside": "NOT_INVENTORIED_NOT_MEASURED",
        "human_development_gap": "NOT_MEASURED",
    }


def plan_from_public(view: PublicView, target: str, costs: Costs, *,
                     budget: float, now: int, b: QualifiedB | None = None,
                     c: ExplorationC | None = None,
                     d: MaterialD | None = None,
                     extra: int = 2) -> dict:
    """Actual receiver planner: NO world, capacity, source-access or oracle input.

    A C-witness has no established ROI, and a D-witness supplies no evaluable
    effect. A truthful B is not assured by these declaration-level checks.
    """
    if type(budget) not in (int, float) or not 0 <= budget < float("inf"):
        raise ValueError("invalid budget")
    path = outline_path(view.outline, target)
    if not path:
        raise ValueError("unknown target")
    plan = {"target": target, "current_A": view.current_A,
            "promised_increment": 0, "estimated_information_cost": 0.0,
            "decision_rule": "EXPLOIT_A_WITH_OPEN_RESIDUAL",
            "open_residual": "NOT_CHARACTERIZED_OUTSIDE_QUESTION"}
    if d is not None and d.question_target == target:
        plan["decision_rule"] = "D_MATERIAL_WITHOUT_EVALUATION_ROUTE_NO_HIGH_PROMISE"
    elif b is not None:
        valid, status = receiver_B_valid(view.outline,b,target,now=now,extra=extra)
        qcost = len(path)*costs.b_issuance_per_path_node + costs.b_transmission + costs.b_maintenance
        if valid and qcost <= budget:
            gross = b.delivered_if_requested*costs.value_per_unit
            if gross > qcost:
                plan.update({"promised_increment": b.delivered_if_requested,
                             "estimated_information_cost": qcost,
                             "decision_rule": "B_INCREMENTAL_GROSS_ABOVE_FULL_QUAL_COST"})
            else:
                plan["decision_rule"] = "B_INFO_NOT_ECONOMIC_FOR_THIS_ONE_QUESTION"
        else:
            plan["decision_rule"] = status if not valid else "B_INFO_BEYOND_BUDGET"
    elif c is not None and c.question_target == target:
        plan["decision_rule"] = "C_GROUNDED_EXPLORATION_FUTURE_RETURN_UNASSESSED"
    return plan


def score_public_plan(world: Node, plan: dict, costs: Costs, *,
                      minimum: int = 8, extra: int = 2) -> dict:
    """Independent synthetic effects oracle; NEVER passed into plan_from_public."""
    target = plan["target"]
    truth = deliver(world, selected_demand(world,target,minimum=minimum,extra=extra)) - deliver(world,base_demand(world,minimum))
    claim=plan["promised_increment"]
    gross=-costs.false_promise if claim > truth else costs.value_per_unit*claim
    result=dict(plan)
    result.update({"physical_increment_PRIVATE_ORACLE":truth,
                   "false_promise_PRIVATE_ORACLE":claim>truth,
                   "gross_realized_value_SYNTHETIC":gross,
                   "net_realized_value_SYNTHETIC":gross-plan["estimated_information_cost"],
                   "human_development_gap":"NOT_MEASURED"})
    return result


def receiver_decision(world: Node, target: str, costs: Costs, *,
                      budget: float, now: int, b: QualifiedB | None = None,
                      c: ExplorationC | None = None,
                      d: MaterialD | None = None,
                      minimum: int = 8, extra: int = 2) -> dict:
    """Laboratory convenience wrapper; public planning strictly precedes scoring."""
    public = observe_view(world, minimum=minimum)
    plan = plan_from_public(public,target,costs,budget=budget,now=now,
                            b=b,c=c,d=d,extra=extra)
    return score_public_plan(world,plan,costs,minimum=minimum,extra=extra)


def bounded_roi_gate(number_of_nodes: int, cost_per_node: float,
                     upper_extra: int, per_unit_value: float) -> dict:
    if (type(number_of_nodes) is not int or number_of_nodes < 1
            or type(upper_extra) is not int or upper_extra < 0
            or any(type(v) not in (float, int) or v < 0 or v != v or v == float("inf")
                   for v in (cost_per_node, per_unit_value))):
        raise ValueError("invalid bound")
    # The ALL-nodes full scan is dominated by conservative A-only if the entire
    # one-query benefit is bounded by value*extra and acquisition costs exceed it.
    full = number_of_nodes * cost_per_node
    value_cap = upper_extra * per_unit_value
    return {"full_acquisition_cost": full,
            "maximum_one_query_gross_gain": value_cap,
            "full_expansion_cannot_beat_conservative_A": full > value_cap,
            "bound_scope": "ONE_QUERY_FIXED_VALUE_FINITE_ACQUISITION_COST_MODEL"}


def communication_lower_bounds(n: int) -> dict:
    if type(n) is not int or not 1 <= n <= 256:
        raise ValueError("n out of bounded study range")
    return {"n": n,
            "full_vector_profiles": 1 << n,
            "one_selected_binary_query_bits_min": 1,
            "all_n_binary_queries_bits_min": n,
            "aggregate_count_profiles": n + 1,
            "aggregate_count_bits_min": (n).bit_length(),
            "scope": "EXACT_FIXED_MESSAGE_WORST_CASE_INDEPENDENT_BITS"}


def sample_report() -> dict:
    n = 16
    bits = tuple(1 if k in (3, 8, 12) else 0 for k in range(n))
    world = balanced_tree(bits)
    target = "source-3"
    cost = Costs()
    cert = upstream_B(world, target, now=5, ttl=10)
    modes = ["A_ONLY", "B_QUALIFIED", "TARGETED_EXPLORATION_OF_A", "FULL_EXPAND_A"]
    outcomes = [policy(world, target, mode, cost, now=6, b=cert) for mode in modes]
    clipped_world = balanced_tree(bits, cap_root=8*n)
    clipped_cert = upstream_B(clipped_world, target, now=5, ttl=10)
    return {
        "scientific_status": "FINITE_SYNTHETIC_ONLY_UNQUANTIFIED_OPEN_RESIDUAL",
        "n_leaves": n, "total_modules": node_count(world),
        "nested_depth_on_target": len(path_to(world, target)),
        "current_A": deliver(world, base_demand(world)),
        "same_current_A_with_root_bottleneck": deliver(clipped_world, base_demand(clipped_world)),
        "baseline_world_private_selected_gain": 2,
        "root_bottleneck_world_private_selected_gain": 0,
        "policies": outcomes,
        "root_bottleneck_B_private_qualified_increment": clipped_cert.delivered_if_requested,
        "communication_query_relative": communication_lower_bounds(n),
        "no_roi_gate": bounded_roi_gate(node_count(world), cost.full_node, 2, cost.value_per_unit),
        "C_status": route_status(ExplorationC("partner", "audit subsystems for missing throughput constraints", question_target=target)),
        "D_status": route_status(MaterialD("partner", "material but unevaluable outside network dependency", question_target=target)),
    }


if __name__ == "__main__":
    print(json.dumps(sample_report(), ensure_ascii=False, indent=2))
