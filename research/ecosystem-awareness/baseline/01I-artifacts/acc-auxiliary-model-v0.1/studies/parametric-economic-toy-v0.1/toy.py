"""ACC auxiliary open economic toy (v0.1).

A research instrument, not the normative ACC runtime, UC21/R01 or an HID instrument.
Only Python's standard library is required.
"""
from __future__ import annotations

from math import isfinite

EPS = 1e-9


class ToyError(ValueError):
    """The scenario violates the executable model contract."""


def number(value, name, lower=None, upper=None):
    if type(value) not in (float, int):
        raise ToyError(name + ": expected a finite JSON number")
    result = float(value)
    if not isfinite(result) or (lower is not None and result < lower - EPS) or (upper is not None and result > upper + EPS):
        raise ToyError(name + ": number outside its admitted domain")
    return result


def boolean(value, name):
    if type(value) is not bool:
        raise ToyError(name + ": expected JSON boolean")
    return value


def integer(value, name, lower, upper):
    if type(value) is not int or value < lower or value > upper:
        raise ToyError(name + ": expected integer in allowed range")
    return value


def nonempty_labels(value, name):
    if not isinstance(value, list) or not value or any(not isinstance(v, str) or not v.strip() for v in value):
        raise ToyError(name + ": expected nonempty list of names")
    if len(set(value)) != len(value):
        raise ToyError(name + ": duplicate label")
    return value


def actor_values(value, actors, label):
    if not isinstance(value, dict):
        raise ToyError(label + ": expected object")
    if set(value) - set(actors):
        raise ToyError(label + ": unknown actor")
    return {a: number(value.get(a, 0), label + "." + a) for a in actors}


def output_vector(value, name):
    if not isinstance(value, dict) or not value:
        raise ToyError(name + ": nonempty output vector required")
    if any(not isinstance(k, str) or not k for k in value):
        raise ToyError(name + ": invalid output key")
    return {k: number(v, name + "." + k) for k, v in value.items()}


def compatible_outputs(one, other):
    return set(one) == set(other) and all(abs(one[k] - other[k]) < EPS for k in one)


def human_input_vector(value, name, expected_keys=None):
    """Disjoint genuine human-information contributions; never inferred from ACW."""
    if not isinstance(value, dict) or not value:
        raise ToyError(name + ": expected nonempty human information input vector")
    if any(not isinstance(key, str) or not key for key in value):
        raise ToyError(name + ": input dimensions must have nonempty names")
    if expected_keys is not None and set(value) != set(expected_keys):
        raise ToyError(name + ": incomparable information input dimensions")
    return {k: number(v, name + "." + k, lower=0) for k, v in value.items()}


def direct_hid_comparison(actual_inputs, reference_inputs, human_capacity, label,
                          same_resources=True, same_service=True):
    """A per-optimum subtraction, with no ACW->GIC conversion assumption."""
    capacity = number(human_capacity, label + ".human_capacity", lower=EPS)
    if set(actual_inputs) != set(reference_inputs):
        raise ToyError(label + ": information input names differ")
    differences = {k: reference_inputs[k] - actual_inputs[k] for k in actual_inputs}
    output = {
        "reference": label,
        "same_resources": same_resources,
        "same_service": same_service,
        "input_difference_hours": differences,
        "HICR_input_ratio": sum(actual_inputs.values()) / capacity,
        "HICT_reference_input_ratio": sum(reference_inputs.values()) / capacity,
        "HID_direct_hours": None,
        "HID_direct_ratio": None,
    }
    if not same_resources or not same_service:
        output["status"] = "NOT_COMPARABLE_SAME_RESOURCES_AND_SERVICE_REQUIRED"
    elif any(delta < -EPS for delta in differences.values()):
        output["status"] = "NOT_INPUTWISE_DOMINATING"
    else:
        output["status"] = "SYNTHETIC_DIRECT_HICT_MINUS_HICR"
        output["HID_direct_hours"] = sum(differences.values())
        output["HID_direct_ratio"] = output["HID_direct_hours"] / capacity
    return output


def portfolio(config):
    """Enumerate a finite F^T and F^G with a separate, observed current state.

    Utility is a fictitious transferable common numeraire. Physical production,
    resource inputs and HID are different ledgers and never added by default.
    """
    if config.get("mode") != "portfolio":
        raise ToyError("portfolio mode required")
    actors = nonempty_labels(config.get("actors"), "actors")
    dimensions = nonempty_labels(config.get("dimensions"), "dimensions")
    approvals = config.get("approvals", {})
    if not isinstance(approvals, dict) or any(not isinstance(k, str) or type(v) is not bool for k, v in approvals.items()):
        raise ToyError("approvals: expected gate -> boolean")
    parameters = config.get("parameters", {})
    if not isinstance(parameters, dict):
        raise ToyError("parameters: expected object")
    shadow = number(parameters.get("acw_shadow_price", 0), "acw_shadow_price", lower=0)
    rho = number(parameters.get("recovery_fraction", 0), "recovery_fraction", lower=0, upper=1)
    budget = number(parameters.get("transition_budget", 1e12), "transition_budget", lower=0)
    resources_limit = number(parameters.get("resources_limit", 1e12), "resources_limit", lower=0)
    require_pareto = boolean(parameters.get("require_pareto", True), "require_pareto")
    acw_classified = boolean(parameters.get("acw_classified_synthetically", False), "acw_classified_synthetically")
    top_k = integer(parameters.get("top_k", 8), "top_k", 1, 100)
    baseline = config.get("baseline")
    if not isinstance(baseline, dict):
        raise ToyError("baseline: expected object")
    base = {
        "production": number(baseline.get("production"), "baseline.production", lower=0),
        "resources": number(baseline.get("resources"), "baseline.resources", lower=0),
        "gic": number(baseline.get("gic_hours"), "baseline.gic_hours", lower=0),
        "neo": number(baseline.get("neo_hours"), "baseline.neo_hours", lower=0),
        "acw": number(baseline.get("acw_hours"), "baseline.acw_hours", lower=0),
        "unknown": number(baseline.get("unknown_hours", 0), "baseline.unknown_hours", lower=0),
        "human_capacity": number(baseline.get("human_capacity_hours"), "baseline.human_capacity_hours", lower=EPS),
        "outputs": output_vector(baseline.get("outputs"), "baseline.outputs"),
    }
    if base["gic"] + base["neo"] + base["acw"] + base["unknown"] > base["human_capacity"] + EPS:
        raise ToyError("baseline human workload exceeds declared capacity")
    base_inputs = human_input_vector(
        baseline.get("human_information_inputs", {"GIC_total": base["gic"]}),
        "baseline.human_information_inputs")
    if abs(sum(base_inputs.values()) - base["gic"]) > EPS:
        raise ToyError("baseline human information inputs must sum to baseline GIC; no ACW inference")
    projects = config.get("projects", [])
    if not isinstance(projects, list) or len(projects) > 16:
        raise ToyError("projects must be an array of at most 16 entries; larger n belongs in formulas/network")
    ids = [p.get("id") for p in projects if isinstance(p, dict)]
    if len(ids) != len(projects) or any(not isinstance(i, str) or not i for i in ids) or len(set(ids)) != len(ids):
        raise ToyError("projects have invalid or duplicate IDs")
    ids_set = set(ids)
    norm_projects = []
    for item in projects:
        pid = item["id"]
        gates = item.get("required_approvals", [])
        if not isinstance(gates, list) or any(g not in approvals for g in gates):
            raise ToyError(pid + ": gates must exist in approvals")
        if not isinstance(item.get("rights_preserved", True), bool):
            raise ToyError(pid + ": rights_preserved must be boolean")
        payoffs = actor_values(item.get("gross_payoffs", {}), actors, pid + ".gross_payoffs")
        transfers = actor_values(item.get("transfers", {}), actors, pid + ".transfers")
        if abs(sum(transfers.values())) > EPS:
            raise ToyError(pid + ": transfers must sum to zero")
        costs = item.get("adjustment_costs_by_actor", {})
        if not isinstance(costs, dict) or set(costs) - set(actors):
            raise ToyError(pid + ": adjustment costs require named actors")
        costs_by_actor = {a: 0.0 for a in actors}
        costs_by_category = {}
        for actor, categories in costs.items():
            if not isinstance(categories, dict):
                raise ToyError(pid + ": cost categories must be an object")
            for category, raw in categories.items():
                if category not in ("discovery", "verification", "communication", "negotiation",
                                    "contracts", "reconfiguration", "risk_resolution"):
                    raise ToyError(pid + ": invalid adjustment cost category " + str(category))
                cost = number(raw, pid + "." + category, lower=0)
                costs_by_actor[actor] += cost
                costs_by_category[category] = costs_by_category.get(category, 0.0) + cost
        delta = {field: number(item.get("delta_" + field, 0), pid + ".delta_" + field)
                 for field in ("production", "resources", "gic_hours", "neo_hours", "acw_hours", "unknown_hours")}
        raw_input_delta = item.get("delta_human_information_inputs")
        if raw_input_delta is None:
            if set(base_inputs) == {"GIC_total"}:
                input_delta = {"GIC_total": delta["gic_hours"]}
            elif abs(delta["gic_hours"]) <= EPS:
                input_delta = {k: 0.0 for k in base_inputs}
            else:
                raise ToyError(pid + ": explicit vector changes required when GIC dimensions are declared")
        else:
            if not isinstance(raw_input_delta, dict) or set(raw_input_delta) - set(base_inputs):
                raise ToyError(pid + ": human input delta uses undeclared dimensions")
            input_delta = {k: number(raw_input_delta.get(k, 0),
                                     pid + ".delta_human_information_inputs." + k)
                           for k in base_inputs}
            if abs(sum(input_delta.values()) - delta["gic_hours"]) > EPS:
                raise ToyError(pid + ": vector delta must sum to declared delta_gic_hours")
        bearer = item.get("acw_bearer")
        if abs(delta["acw_hours"]) > EPS and shadow > EPS and bearer not in actors:
            raise ToyError(pid + ": acw_bearer required when valuing ACW")
        output_deltas = item.get("output_deltas", {})
        if not isinstance(output_deltas, dict) or set(output_deltas) - set(base["outputs"]):
            raise ToyError(pid + ": output_deltas must use baseline output labels")
        output_deltas = {k: number(v, pid + ".output_deltas." + k) for k, v in output_deltas.items()}
        requires = item.get("requires", [])
        excludes = item.get("excludes", [])
        if (not isinstance(requires, list) or not isinstance(excludes, list)
                or any(x not in ids_set or x == pid for x in requires + excludes)):
            raise ToyError(pid + ": bad requires/excludes")
        norm_projects.append({"id": pid, "gates": gates, "rights": item.get("rights_preserved", True),
                              "payoffs": payoffs, "transfers": transfers, "costs": costs_by_actor,
                              "costs_by_category": costs_by_category, "delta": delta, "bearer": bearer,
                              "input_delta": input_delta, "output_deltas": output_deltas,
                              "requires": requires, "excludes": excludes})
    current_ids = config.get("current_projects", [])
    if not isinstance(current_ids, list) or len(current_ids) != len(set(current_ids)) or set(current_ids) - ids_set:
        raise ToyError("current_projects are not a valid unique subset")

    # v0.1 only models additive transitions from the declared current state.
    # Removing a live project would require a separately specified rollback cost and permission.
    current_set = set(current_ids)
    feasible = []
    for mask in range(1 << len(norm_projects)):
        selected = [p for index, p in enumerate(norm_projects) if mask & (1 << index)]
        selected_ids = set(p["id"] for p in selected)
        if not current_set.issubset(selected_ids):
            continue
        if any(not p["rights"] or set(p["requires"]) - selected_ids
               or set(p["excludes"]) & selected_ids for p in selected):
            continue
        state = {key: base[key] for key in ("production", "resources", "gic", "neo", "acw", "unknown")}
        human_inputs = dict(base_inputs)
        outputs = dict(base["outputs"])
        actor_net = {a: 0.0 for a in actors}
        category_costs = {}
        transitions = 0.0
        additional_transition_cost = 0.0
        for p in selected:
            d = p["delta"]
            for label, field in (("production", "production"), ("resources", "resources"),
                                 ("gic", "gic_hours"), ("neo", "neo_hours"),
                                 ("acw", "acw_hours"), ("unknown", "unknown_hours")):
                state[label] += d[field]
            for label, delta in p["input_delta"].items():
                human_inputs[label] += delta
            for key, delta in p["output_deltas"].items():
                outputs[key] += delta
            for a in actors:
                actor_net[a] += p["payoffs"][a] + p["transfers"][a] - p["costs"][a]
            if p["bearer"] is not None:
                actor_net[p["bearer"]] -= shadow * d["acw_hours"]
            transitions += sum(p["costs"].values())
            if p["id"] not in current_set:
                additional_transition_cost += sum(p["costs"].values())
            for category, amount in p["costs_by_category"].items():
                category_costs[category] = category_costs.get(category, 0.0) + amount
        if (state["production"] < -EPS or state["resources"] < -EPS
                or state["resources"] > resources_limit + EPS or additional_transition_cost > budget + EPS
                or any(state[k] < -EPS for k in ("gic", "neo", "acw", "unknown"))
                or any(v < -EPS for v in human_inputs.values())
                or abs(sum(human_inputs.values()) - state["gic"]) > EPS
                or sum(state[k] for k in ("gic", "neo", "acw", "unknown")) > base["human_capacity"] + EPS
                or any(amount < -EPS for amount in outputs.values())):
            continue
        gates_missing = sorted(set(g for p in selected for g in p["gates"] if not approvals[g]))
        utility = sum(actor_net.values())
        row = {"projects": sorted(selected_ids), "production": state["production"],
               "resources": state["resources"], "outputs": outputs,
               "gic_hours": state["gic"], "human_information_inputs": human_inputs,
               "neo_hours": state["neo"], "acw_hours": state["acw"],
               "unknown_hours": state["unknown"], "utility": utility,
               "actor_net": actor_net, "C_adj": transitions,
               "new_C_adj": additional_transition_cost, "cost_categories": category_costs,
               "missing_approvals": gates_missing}
        feasible.append(row)
    by_state = {tuple(s["projects"]): s for s in feasible}
    key = tuple(sorted(current_ids))
    if key not in by_state:
        raise ToyError("current state is not technically feasible")
    actual = by_state[key]
    # Pareto/actor consent is relative to the presently realized portfolio, not to t=0.
    for row in feasible:
        negative_actors = [a for a in actors if row["actor_net"][a] - actual["actor_net"][a] < -EPS]
        row["negative_actors"] = negative_actors
        row["governable"] = not row["missing_approvals"] and (not require_pareto or not negative_actors)
    ordered = sorted(feasible, key=lambda x: (-x["utility"], x["resources"], x["projects"]))
    technical = ordered[0]
    gov_states = [s for s in ordered if s["governable"]]
    governed = gov_states[0] if gov_states else None
    g_technical = max(0.0, technical["utility"] - actual["utility"])
    g_governance = (max(0.0, governed["utility"] - actual["utility"])
                    if actual["governable"] and governed is not None else None)

    matching = [s for s in feasible if compatible_outputs(s["outputs"], actual["outputs"])]
    best_resources = min(matching, key=lambda s: (s["resources"], -s["utility"], s["projects"]))
    g_efficiency = max(0.0, actual["resources"] - best_resources["resources"])

    def primary_comparison(row):
        return direct_hid_comparison(
            actual["human_information_inputs"], row["human_information_inputs"],
            base["human_capacity"], "/".join(row["projects"]) or "<current-empty>",
            same_resources=abs(row["resources"] - actual["resources"]) <= EPS,
            same_service=compatible_outputs(row["outputs"], actual["outputs"]))

    technical_optima = [s for s in ordered if abs(s["utility"] - technical["utility"]) <= EPS]
    governed_optima = ([s for s in gov_states
                        if abs(s["utility"] - governed["utility"]) <= EPS]
                       if governed is not None else [])
    comparable_inputs = [
        s for s in matching
        if abs(s["resources"] - actual["resources"]) <= EPS
        and s["utility"] >= actual["utility"] - EPS
        and all(s["human_information_inputs"][k] >= actual["human_information_inputs"][k] - EPS
                for k in base_inputs)]

    def information_frontier(states):
        """All non-dominated feasible configurations, not coordinatewise maxima."""
        front = [
            s for s in states
            if not any(other is not s
                       and all(other["human_information_inputs"][k]
                               >= s["human_information_inputs"][k] - EPS for k in base_inputs)
                       and any(other["human_information_inputs"][k]
                               > s["human_information_inputs"][k] + EPS for k in base_inputs)
                       for other in states)]
        return [primary_comparison(s) for s in sorted(front, key=lambda x: x["projects"])]

    primary = {
        "definition": "HID = HICT - HICR = sum(reference_human_input - current_human_input) / common_human_hours",
        "unit": "disjoint hours of genuine human informational contribution; not ACW",
        "common_human_hours": base["human_capacity"],
        "actual_inputs": actual["human_information_inputs"],
        "technical_utility_optima": [primary_comparison(s) for s in technical_optima],
        "governance_utility_optima": [primary_comparison(s) for s in governed_optima],
        "technical_human_input_frontier": information_frontier(comparable_inputs),
        "governable_human_input_frontier": information_frontier(
            [s for s in comparable_inputs if s["governable"]]),
        "evidence": "DECLARED_SYNTHETIC_INPUTS; independent human measurement belongs to 01K"}

    human_time = sum(actual[k] for k in ("gic_hours", "neo_hours", "acw_hours", "unknown_hours"))
    if acw_classified and human_time > EPS:
        # Counterfactual is constrained to one joint state, identical service, no lower utility.
        witnesses = [s for s in matching if s["utility"] >= actual["utility"] - EPS
                     and s["acw_hours"] < actual["acw_hours"] - EPS]
        best_hid = min(witnesses, key=lambda s: (s["acw_hours"], -s["utility"])) if witnesses else None
        releasable = max(0.0, actual["acw_hours"] - best_hid["acw_hours"]) if best_hid else 0.0
        hicr = actual["gic_hours"] / human_time
        hid_observed = actual["acw_hours"] / human_time
        hid_potential = releasable / human_time
        hid = {"status": "SYNTHETIC_CONDITIONAL_NOT_EMPIRICAL", "HICR_time": hicr,
               "HID_observed": hid_observed, "H_releasable_hours": releasable,
               "HICT_conditional": hicr + hid_potential, "HID_potential": hid_potential,
               "F_HICT_conditional": hicr + rho * hid_potential,
               "HID_spent_conditional": (1 - rho) * hid_potential,
               "releasable_witness": best_hid["projects"] if best_hid else []}
    else:
        hid = {"status": "NOT_MEASURED_CLASSIFICATION_REQUIRED", "H_releasable_hours": None,
               "HID_observed": None, "HICR_time": None, "HID_potential": None}
    hid["primary_optimum_input_gap"] = primary
    hid["auxiliary_role"] = "ACW, GIC/NEO and rho contextualise; they do not define HID from the optimum"
    return {
        "mode": "portfolio", "status": "SYNTHETIC_RESEARCH_TOY",
        "dimension_count": len(dimensions), "dimension_labels": dimensions,
        "transition_scope": "ADDITIONS_ONLY_FROM_CURRENT; NO_UNMODELLED_ROLLBACK",
        "state_count_F_T": len(feasible), "state_count_F_G": len(gov_states),
        "actual": actual, "technical_optimum": technical, "governance_optimum": governed,
        "G_technical": g_technical, "G_governable": g_governance,
        "G_efficiency_same_service_resources": g_efficiency,
        "best_efficiency_same_service": best_resources["projects"],
        "suboptimal_technical": g_technical > EPS,
        "suboptimal_governable": g_governance is not None and g_governance > EPS,
        "governability_of_actual": actual["governable"],
        "technical_optimum_block_reason": {
            "missing_approvals": technical["missing_approvals"],
            "negative_actors": technical["negative_actors"] if require_pareto else []},
        "hid": hid,
        "frontier_top": [dict(s, distance_to_technical=max(0.0, technical["utility"] - s["utility"]))
                         for s in ordered[:top_k]],
        "caveats": ["F^T contains technical options, not automatic legal authority.",
                    "Payoffs exclude adjustment and ACW shadow charges, which are booked once.",
                    "Pareto checks and transition budget are relative to current; no project removal is simulated.",
                    "Efficiency compares identical declared output vectors; rights/service quality are input assumptions.",
                    "HID direct comes from per-optimum declared human input differences, not ACW release.",
                    "Only identical resource use and service produce a comparable primary HID; all optima are within the enumerated space.",
                    "ACW, NEO and recovery remain auxiliary and 01K human validation is not claimed."]}


def network_edges(n, topology):
    if topology == "dense":
        return n                 # Source toy: one hub plus n cross-links per incorporation.
    if topology in ("sparse", "star"):
        return 1
    if topology == "modular":
        return 1 + int(n % 3 == 0)
    raise ToyError("unsupported topology: " + str(topology))


def network(config):
    """Expected-value trajectories; no random trials or historical-run authentication."""
    if config.get("mode") != "network":
        raise ToyError("network mode required")
    horizon = integer(config.get("horizon"), "horizon", 3, 500)
    b = number(config.get("production_per_dimension"), "production_per_dimension", lower=0)
    synergy = number(config.get("synergy_per_compatible_link", 0), "synergy_per_compatible_link", lower=0)
    unit_value = number(config.get("production_unit_value", 1), "production_unit_value", lower=0)
    hours = number(config.get("human_hours_per_obligation"), "human_hours_per_obligation", lower=0)
    shadow = number(config.get("acw_shadow_price"), "acw_shadow_price", lower=0)
    maintenance = number(config.get("maintenance_cost_per_obligation", 0), "maintenance_cost_per_obligation", lower=0)
    per_gic = number(config.get("gic_hours_per_dimension", 0), "gic_hours_per_dimension", lower=0)
    per_neo = number(config.get("neo_hours_per_dimension", 0), "neo_hours_per_dimension", lower=0)
    per_unknown = number(config.get("unknown_hours_per_dimension", 0), "unknown_hours_per_dimension", lower=0)
    cap = number(config.get("capacity_hours_per_dimension"), "capacity_hours_per_dimension", lower=EPS)
    base_info_rates = human_input_vector(
        config.get("human_information_input_rates_per_dimension", {"GIC_total": per_gic}),
        "human_information_input_rates_per_dimension")
    if abs(sum(base_info_rates.values()) - per_gic) > EPS:
        raise ToyError("human input rates must sum to gic_hours_per_dimension")
    loss_raw = config.get("unqualified_dependency_input_loss_rates",
                          {k: 0 for k in base_info_rates})
    if not isinstance(loss_raw, dict) or set(loss_raw) != set(base_info_rates):
        raise ToyError("unqualified_dependency_input_loss_rates must match input dimensions")
    loss_rates = {k: number(v, "unqualified_dependency_input_loss_rates." + k, lower=0)
                  for k, v in loss_raw.items()}
    if per_gic + per_neo + per_unknown > cap + EPS:
        raise ToyError("baseline human work exceeds capacity per dimension")
    rho = number(config.get("recovery_fraction", 0), "recovery_fraction", lower=0, upper=1)
    same_service = boolean(config.get("same_service_counterfactual", False), "same_service_counterfactual")
    acw_classified = boolean(config.get("acw_classified_synthetically", False), "acw_classified_synthetically")
    arms = config.get("arms")
    if not isinstance(arms, dict) or not arms:
        raise ToyError("arms must be nonempty mapping")
    actual_id = config.get("actual_arm")
    if actual_id not in arms:
        raise ToyError("actual_arm must be listed")
    forecast_id = config.get("forecast_arm", actual_id)
    if forecast_id not in arms:
        raise ToyError("forecast_arm must be listed")
    normalized = {}
    for name, item in arms.items():
        if not isinstance(name, str) or not name or not isinstance(item, dict):
            raise ToyError("bad arm name or object")
        topology = item.get("topology", "dense")
        network_edges(3, topology)
        interoperability = item.get("interoperability", "flat")
        if interoperability not in ("flat", "inverse_time"):
            raise ToyError("invalid interoperability")
        epistemic = item.get("epistemic_process")
        if epistemic is not None:
            if (not isinstance(epistemic, dict)
                    or epistemic.get("position") not in ("A", "B", "C", "D")
                    or not isinstance(epistemic.get("question"), str)
                    or not epistemic["question"].strip()):
                raise ToyError(name + ": ABCD position requires a process-relative qualification question")
            if epistemic.get("qualified_new_links_policy") not in ("all", "one", "none"):
                raise ToyError(name + ": explicit qualified-new-links action policy required")
            epistemic = {
                "position": epistemic["position"], "question": epistemic["question"],
                "policy": epistemic["qualified_new_links_policy"],
                "requalify": number(epistemic.get("requalification_rate", 0),
                                    name + ".requalification_rate", lower=0, upper=1),
                "neo_per_qualified": number(epistemic.get("neo_hours_per_qualified_link", 0),
                                             name + ".neo_hours_per_qualified_link", lower=0)}
        normalized[name] = {"topology": topology, "interoperability": interoperability,
            "p": number(item.get("p_incompatible"), name + ".p_incompatible", lower=0, upper=1),
            "r": number(item.get("retirement_rate", 0), name + ".retirement_rate", lower=0, upper=1),
            "setup": number(item.get("setup_cost", 0), name + ".setup_cost", lower=0),
            "new_link_cost": number(item.get("cost_per_new_link", 0), name + ".cost_per_new_link", lower=0),
            "gov": boolean(item.get("governance_available", True), name + ".governance_available"),
            "technical": boolean(item.get("technically_available", True), name + ".technically_available"),
            "rights": boolean(item.get("rights_preserved", True), name + ".rights_preserved"),
            "service": boolean(item.get("full_service_preserved", True), name + ".full_service_preserved"),
            "epistemic": epistemic}
    if not normalized[actual_id]["technical"] or not normalized[actual_id]["rights"] or not normalized[actual_id]["service"]:
        raise ToyError("actual arm needs technical feasibility, rights and full-service preservation")
    state = {a: {"active": 0.0, "edges": 0, "unqualified_oracle": 0.0,
                 "total_acw": 0.0, "cumulative_net": 0.0,
                 "production_path": [], "rows": []} for a in arms}
    rows = []
    first_negative = None
    first_overflow = None
    actual_flows = []
    hid_hours_flows = []
    hid_ratio_flows = []
    hid_reference_id = config.get("hid_reference_arm")
    if hid_reference_id is not None and hid_reference_id not in arms:
        raise ToyError("hid_reference_arm must be an existing arm")
    prior_flow = None
    for t in range(1, horizon + 1):
        for name, arm in normalized.items():
            st = state[name]
            new_edges = network_edges(t, arm["topology"])
            ep = arm["epistemic"]
            qualified_new = 0.0
            additional_neo = 0.0
            if ep is not None:
                qualified_new = (new_edges if ep["policy"] == "all"
                                 else min(1.0, new_edges) if ep["policy"] == "one" else 0.0)
                previously_unqualified = st["unqualified_oracle"]
                requalified = previously_unqualified * ep["requalify"]
                st["unqualified_oracle"] = (
                    previously_unqualified - requalified + new_edges - qualified_new)
                additional_neo = ep["neo_per_qualified"] * (qualified_new + requalified)
            human_inputs = {k: base_info_rates[k] * t - loss_rates[k] * st["unqualified_oracle"]
                            for k in base_info_rates}
            if any(v < -EPS for v in human_inputs.values()):
                raise ToyError(name + ": synthetic human information inputs below zero; narrow horizon or coefficients")
            gic = sum(human_inputs.values())
            p_t = arm["p"] / t if arm["interoperability"] == "inverse_time" else arm["p"]
            retired_obligations = arm["r"] * st["active"]
            new_obligations = p_t * new_edges
            st["active"] = st["active"] + new_obligations - retired_obligations
            st["edges"] += new_edges
            acw = hours * st["active"]
            st["total_acw"] += acw
            produced = b * t + synergy * (st["edges"] - st["active"])
            C_adj_t = (arm["setup"] if t == 1 else 0.0) + arm["new_link_cost"] * new_edges
            gross_output_value = unit_value * produced
            acw_opportunity_cost = shadow * acw
            maintenance_cost = maintenance * st["active"]
            flow = gross_output_value - acw_opportunity_cost - maintenance_cost - C_adj_t
            st["cumulative_net"] += flow
            st["production_path"].append(produced)
            st["rows"].append({"arm": name, "t": t, "new_edges": new_edges, "edges": st["edges"],
                               "epistemic_position": ep["position"] if ep else None,
                               "qualified_new_links": qualified_new,
                               "unqualified_true_links_oracle_only": st["unqualified_oracle"] if ep else None,
                               "human_information_inputs": human_inputs, "H_GIC": gic,
                               "H_NEO_additional": additional_neo,
                               "new_obligations_N_t": new_obligations,
                               "retired_obligations_R_t": retired_obligations,
                               "active_obligations_O_t": st["active"], "d_t": acw, "D_T": st["total_acw"],
                               "production": produced, "gross_output_value": gross_output_value,
                               "ACW_opportunity_cost": acw_opportunity_cost,
                               "maintenance_cost": maintenance_cost, "C_adj_t": C_adj_t,
                               "flow_value": flow, "cumulative_value": st["cumulative_net"]})
        actual = state[actual_id]["rows"][-1]
        d_hat = state[forecast_id]["rows"][-1]["d_t"]
        forecast_error = actual["d_t"] - d_hat
        comparable = [name for name, arm in normalized.items()
                      if arm["technical"] and arm["rights"] and arm["service"] and same_service
                      and all((state[name]["rows"][j]["H_GIC"] + per_neo*(j+1)
                               + state[name]["rows"][j]["H_NEO_additional"] + per_unknown*(j+1))
                              + state[name]["rows"][j]["d_t"] <= cap*(j+1) + EPS
                              and abs(state[name]["production_path"][j]
                                      - state[actual_id]["production_path"][j]) < EPS
                              for j in range(t))]
        actual_time = (actual["H_GIC"] + per_neo*t + actual["H_NEO_additional"]
                       + per_unknown*t + actual["d_t"])
        capacity = cap * t
        overflow = actual_time > capacity + EPS
        if overflow and first_overflow is None:
            first_overflow = t
        path_overflow = first_overflow is not None
        if not path_overflow and any(name != actual_id for name in comparable):
            best_t = min(comparable, key=lambda n: (-state[n]["cumulative_net"], n))
            available = [n for n in comparable if normalized[n]["gov"]]
            best_g = min(available, key=lambda n: (-state[n]["cumulative_net"], n)) if available else None
            G_t = max(0.0, state[best_t]["cumulative_net"] - actual["cumulative_value"])
            G_g = (max(0.0, state[best_g]["cumulative_net"] - actual["cumulative_value"])
                   if best_g and normalized[actual_id]["gov"] else None)
            valid_witnesses = [n for n in comparable if
                               state[n]["cumulative_net"] >= actual["cumulative_value"] - EPS
                               and state[n]["rows"][-1]["d_t"] < actual["d_t"] - EPS]
            most_releasable = min(valid_witnesses, key=lambda n: state[n]["rows"][-1]["d_t"]) if valid_witnesses else None
            releasable = max(0.0, actual["d_t"] - state[most_releasable]["rows"][-1]["d_t"]) if most_releasable else 0.0
        else:
            best_t = best_g = None
            G_t = G_g = None
            releasable = None
            most_releasable = None
        primary = {"status": "NOT_COMPARABLE", "reference_arm": hid_reference_id,
                   "direct_gap_hours": None, "direct_gap_ratio": None,
                   "technical_utility_optima": [], "governance_utility_optima": [],
                   "human_input_frontier": [], "comparison": None}
        if not path_overflow and actual_id in comparable:
            max_value = max(state[name]["rows"][-1]["cumulative_value"] for name in comparable)
            technical_optima = [name for name in comparable
                                if abs(state[name]["rows"][-1]["cumulative_value"] - max_value) <= EPS]
            gov_eligible = [name for name in comparable if normalized[name]["gov"]]
            governed_optima = []
            if gov_eligible:
                gov_value = max(state[name]["rows"][-1]["cumulative_value"] for name in gov_eligible)
                governed_optima = [name for name in gov_eligible
                                   if abs(state[name]["rows"][-1]["cumulative_value"] - gov_value) <= EPS]
            def compare_arm(name):
                return direct_hid_comparison(
                    actual["human_information_inputs"],
                    state[name]["rows"][-1]["human_information_inputs"],
                    cap*t, name)
            candidates = [name for name in comparable
                          if all(state[name]["rows"][-1]["human_information_inputs"][k]
                                 >= actual["human_information_inputs"][k] - EPS
                                 for k in base_info_rates)]
            frontier = [name for name in candidates if not any(
                other != name
                and all(state[other]["rows"][-1]["human_information_inputs"][k]
                        >= state[name]["rows"][-1]["human_information_inputs"][k] - EPS
                        for k in base_info_rates)
                and any(state[other]["rows"][-1]["human_information_inputs"][k]
                        > state[name]["rows"][-1]["human_information_inputs"][k] + EPS
                        for k in base_info_rates)
                for other in candidates)]
            selected_ref = hid_reference_id if hid_reference_id is not None else (best_t or actual_id)
            reference = compare_arm(selected_ref) if selected_ref in comparable else None
            primary.update({
                "status": reference["status"] if reference is not None else "REFERENCE_INCOMPARABLE",
                "reference_arm": selected_ref,
                "reference_is_technical_utility_optimum": selected_ref in technical_optima,
                "reference_is_governance_utility_optimum": selected_ref in governed_optima,
                "direct_gap_hours": reference["HID_direct_hours"] if reference else None,
                "direct_gap_ratio": reference["HID_direct_ratio"] if reference else None,
                "technical_utility_optima": [compare_arm(n) for n in technical_optima],
                "governance_utility_optima": [compare_arm(n) for n in governed_optima],
                "human_input_frontier": [compare_arm(n) for n in sorted(frontier)],
                "comparison": reference})
        if acw_classified and actual_time > EPS:
            hicr = actual["H_GIC"] / actual_time
            hid_obs = actual["d_t"] / actual_time
            potential = releasable / actual_time if releasable is not None else None
            human = {"status": "SYNTHETIC_CONDITIONAL_NOT_EMPIRICAL",
                     "H_GIC": actual["H_GIC"],
                     "H_NEO": per_neo*t + actual["H_NEO_additional"], "H_ACW": actual["d_t"],
                     "H_UNKNOWN": per_unknown * t, "H_total": actual_time,
                     "HICR_time": hicr, "HID_observed": hid_obs, "H_releasable": releasable,
                     "HID_potential": potential, "HICT_conditional": hicr + potential if potential is not None else None,
                     "F_HICT_conditional": hicr + rho * potential if potential is not None else None,
                     "HID_spent_conditional": (1-rho) * potential if potential is not None else None,
                     "best_releasable_witness": most_releasable, "human_capacity_overflow": overflow,
                     "historical_capacity_overflow": path_overflow}
        else:
            human = {"status": "NOT_MEASURED_CLASSIFICATION_REQUIRED", "HID_observed": None,
                     "H_releasable": None, "human_capacity_overflow": overflow,
                     "historical_capacity_overflow": path_overflow}
        human["primary_optimum_input_gap"] = primary
        human["actual_human_information_inputs"] = actual["human_information_inputs"]
        human["common_human_capacity_hours"] = cap*t
        new_gap = primary["direct_gap_hours"]
        new_ratio = primary["direct_gap_ratio"]
        delta2_hid = (new_gap - 2*hid_hours_flows[-1] + hid_hours_flows[-2]
                      if new_gap is not None and len(hid_hours_flows) >= 2
                      and hid_hours_flows[-1] is not None and hid_hours_flows[-2] is not None
                      else None)
        delta2_hid_ratio = (new_ratio - 2*hid_ratio_flows[-1] + hid_ratio_flows[-2]
                            if new_ratio is not None and len(hid_ratio_flows) >= 2
                            and hid_ratio_flows[-1] is not None and hid_ratio_flows[-2] is not None
                            else None)
        hid_hours_flows.append(new_gap)
        hid_ratio_flows.append(new_ratio)
        delta2 = (actual["d_t"] - 2 * actual_flows[-1] + actual_flows[-2] if len(actual_flows) >= 2 else None)
        actual_flows.append(actual["d_t"])
        marginal = actual["flow_value"] - prior_flow if prior_flow is not None else None
        prior_flow = actual["flow_value"]
        if marginal is not None and marginal < -EPS and first_negative is None:
            first_negative = t
        rows.append({"t": t, "n_dimensions": t, "actual_arm": actual_id, "production": actual["production"],
                     "d_t": actual["d_t"], "d_hat_t": d_hat, "forecast_error_e_t": forecast_error,
                     "D_T": actual["D_T"], "delta2_d_t": delta2,
                     "HID_direct_hours": new_gap, "HID_direct_ratio": new_ratio,
                     "delta2_HID_direct_hours": delta2_hid,
                     "delta2_HID_direct_ratio": delta2_hid_ratio,
                     "flow_value": actual["flow_value"], "marginal_flow_value": marginal,
                     "cumulative_value": actual["cumulative_value"],
                     "G_path_technical": G_t, "G_path_governable": G_g,
                     "path_optimum_technical_arm": best_t, "path_optimum_governable_arm": best_g,
                     "suboptimal_path_technical": G_t is not None and G_t > EPS,
                     "suboptimal_path_governable": G_g is not None and G_g > EPS,
                     "comparable_arms": comparable, "human": human})
    curvature = [x["delta2_d_t"] for x in rows if x["delta2_d_t"] is not None]
    convex_last = len(curvature) >= 3 and all(c > EPS for c in curvature[-3:])
    epistemic_arms = {name: arm["epistemic"] for name, arm in normalized.items()
                     if arm["epistemic"] is not None}
    matched_physics = None
    if epistemic_arms:
        keys = ("topology", "interoperability", "p", "r", "setup",
                "new_link_cost", "technical", "gov", "rights", "service")
        signatures = {tuple(normalized[name][k] for k in keys) for name in epistemic_arms}
        matched_physics = (len(epistemic_arms) == len(normalized) == 4
                           and len(signatures) == 1
                           and {ep["position"] for ep in epistemic_arms.values()}
                           == {"A", "B", "C", "D"}
                           and len({ep["question"] for ep in epistemic_arms.values()}) == 1)
    epistemic_comparison = {
        "status": ("MATCHED_SYNTHETIC_PROCESS_CONTRAST" if matched_physics else
                   "NOT_AN_ISOLATED_ABCD_CONTRAST" if epistemic_arms else "NOT_CONFIGURED"),
        "arms": {name: {"position": ep["position"], "process_question": ep["question"],
                        "chosen_action_policy": ep["policy"],
                        "last_oracle_unqualified_links": state[name]["unqualified_oracle"]}
                 for name, ep in epistemic_arms.items()},
        "boundary": "A/B/C/D classify a process-relative result, reserve, exploration frontier and non-evaluable residual; no probabilities, coverage shares or enumerated C/D are inferred from letters; oracle scoring is post hoc"}
    return {"mode": "network", "status": "ANALYTIC_EXPECTATION_TOY_NO_RUNS",
            "actual_arm": actual_id, "forecast_arm": forecast_id, "horizon": horizon, "rows": rows,
            "arms": {name: st["rows"] for name, st in state.items()},
            "epistemic_ABCD_experiment": epistemic_comparison,
            "summary": {"first_negative_marginal_t": first_negative,
                        "first_human_capacity_overflow_t": first_overflow,
                        "convex_last_three": convex_last,
                        "last_G_path_technical": rows[-1]["G_path_technical"],
                        "last_G_path_governable": rows[-1]["G_path_governable"],
                        "last_HID_observed": rows[-1]["human"]["HID_observed"],
                        "last_d_t": rows[-1]["d_t"], "last_forecast_error_e_t": rows[-1]["forecast_error_e_t"],
                        "last_D_T": rows[-1]["D_T"],
                        "last_production": rows[-1]["production"],
                        "last_delta2_d_t": rows[-1]["delta2_d_t"],
                        "last_HID_direct_hours": rows[-1]["HID_direct_hours"],
                        "last_HID_direct_ratio": rows[-1]["HID_direct_ratio"],
                        "last_delta2_HID_direct_hours": rows[-1]["delta2_HID_direct_hours"],
                        "last_delta2_HID_direct_ratio": rows[-1]["delta2_HID_direct_ratio"]},
            "caveats": ["Arms compare histories from a common t=0, not an instantaneous feasible reset at t.",
                        "G_path requires exactly matched production history plus declared same-service and rights assumption.",
                        "Once human workload exceeds capacity, G and HID potential are not reported.",
                        "HID direct is the per-reference input subtraction; ACW, NEO and recovery are explanatory only.",
                        "ABCD labels do not numerically determine knowledge; policies and synthetic human input response are independently declared.",
                        "C and D remain unenumerable from the acting process; the experimental oracle does not grant runtime knowledge.",
                        "Probabilities and classifications are toy inputs, not measured HID or social dynamics.",
                        "Second differences identify curvature, not causal second-order feedback."]}


def formulas(config):
    """Independent analytic M0–M3 study of dimensions; rejected ≠ recoverable."""
    if config.get("mode") != "formulas":
        raise ToyError("formulas mode required")
    ns = config.get("n_values")
    if not isinstance(ns, list) or not ns or any(type(n) is not int or n < 2 or n > 10000 for n in ns):
        raise ToyError("n_values: integers between 2 and 10000 required")
    if ns != sorted(set(ns)):
        raise ToyError("n_values: increasing and unique required")
    q = number(config.get("q_accept"), "q_accept", lower=0, upper=1)
    p = number(config.get("p_incompatible"), "p_incompatible", lower=0, upper=1)
    g = number(config.get("value_per_veto_proposal"), "value_per_veto_proposal", lower=0)
    k = number(config.get("proposals_per_pair"), "proposals_per_pair", lower=0)
    b = number(config.get("production_per_dimension"), "production_per_dimension", lower=0)
    a = number(config.get("production_per_accepted_relation"), "production_per_accepted_relation", lower=0)
    c = number(config.get("loss_per_incompatible_relation"), "loss_per_incompatible_relation", lower=0)
    v = number(config.get("value_per_rejected_proposal"), "value_per_rejected_proposal", lower=0)
    topology = config.get("topology", "complete")
    if topology not in ("complete", "star", "ring"):
        raise ToyError("invalid topology")
    rows = []
    for n in ns:
        e = n * (n-1)/2 if topology == "complete" else (n-1 if topology == "star" else n)
        pass_fraction = q ** (n-1)
        m = k * n * (n-1)
        accepted = m * pass_fraction
        rejected = m - accepted
        rows.append({"n": n, "E_edges": e, "approval_fraction": pass_fraction,
                     "D_veto_M0": g * n * (1-pass_fraction),
                     "D_inter_M1": p*c*e,
                     "P_real_M2": b*n + a*(1-p)*e,
                     "D_opportunity_M2": a*p*e,
                     "M_proposals_M3": m, "A_approved_M3": accepted,
                     "R_rejected_M3": rejected, "D_bruta_M3": v*rejected,
                     "P_endogenous_M3": b*n + a*accepted})
    return {"mode": "formulas", "status": "FORMULA_IDENTITIES_ONLY_NOT_EMPIRICAL",
            "topology": topology, "rows": rows,
            "caveats": ["Independence, uniform q/p and n-dimensional scaling are explicit toy assumptions.",
                        "D_bruta is rejected proposal value, not a jointly attainable welfare gap.",
                        "M2 output interactions may themselves make total production nonlinear.",
                        "Neither curvature nor a model-imposed veto establishes human HID."]}


def evaluate(config):
    if not isinstance(config, dict):
        raise ToyError("scenario must be a JSON object")
    mode = config.get("mode")
    if mode == "portfolio":
        return portfolio(config)
    if mode == "network":
        return network(config)
    if mode == "formulas":
        return formulas(config)
    raise ToyError("mode must be portfolio, network or formulas")
