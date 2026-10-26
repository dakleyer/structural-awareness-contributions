"""ACC RAV-01 / EX — preregisterable synthetic case campaign.

The input is a declared, rights-bounded parameter set. Neither a human dataset
nor a probability model for ACC's uncharacterised B/C/D exterior.
No value is inferred from the prose of the private source essay.
"""
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
RAV_DIR = HERE.parent
if str(RAV_DIR) not in sys.path:
    sys.path.insert(0, str(RAV_DIR))

from risk_model import (
    DefencePolicy, RiskChoice, RiskOutcome, change_advantage_ce,
    certainty_equivalent, exit_probability, policy_certainty_equivalents,
    preferred_course, preferred_with_defense,
)

SCHEMA = "ACC-RAV-WRITING-EXPERIMENTS-v0.1"
STATUS = "SYNTHETIC_CONDITIONAL_NOT_EMPIRICAL"


def _number(value: object, name: str, minimum: float | None = None) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{name}: expected finite numeric parameter")
    num = float(value)
    if minimum is not None and num < minimum:
        raise ValueError(f"{name}: must be >= {minimum}")
    return num


def _prob(value: object, name: str) -> float:
    num = _number(value, name, 0.0)
    if num > 1:
        raise ValueError(f"{name}: probabilities must be <= 1")
    return num


def _rounded(value: float) -> float:
    if not math.isfinite(value):
        raise ValueError("computed non-finite result")
    return round(float(value), 10)


def _check_identity(case: dict, group: str, seen: set[str]) -> None:
    name = case.get("id")
    if not isinstance(name, str) or not name or name in seen:
        raise ValueError(f"{group}: missing or repeated experiment id")
    seen.add(name)


def _requires_true(case: dict, *assumptions: str) -> None:
    """No silent promotion: model assumptions must be openly stipulated."""
    for assumption in assumptions:
        if case.get(assumption) is not True:
            raise ValueError(f"{case.get('id', 'case')}: unproven or absent {assumption}")


def _static(case: dict) -> dict:
    """Service-matched social-net accounting. Revenues/transfers excluded."""
    _requires_true(case, "cost_buckets_nonoverlapping_stipulated",
                   "same_service_metric_and_horizon_stipulated")
    floor = _number(case["service_floor"], "service_floor", 0)
    options = case["options"]
    if len(options) < 2:
        raise ValueError("static case needs at least two alternatives")
    names: set[str] = set()
    rows = []
    for option in options:
        name = option["name"]
        if not isinstance(name, str) or not name or name in names:
            raise ValueError("missing/duplicate option")
        names.add(name)
        service = _number(option["service_value"], "service", 0)
        resource = _number(option["real_resource_cost"], "resource", 0)
        maintenance = _number(option["maintenance_cost"], "maintenance", 0)
        external = _number(option["external_cost"], "external", 0)
        activity = _number(option["gross_transactions"], "commercial_activity", 0)
        private = _number(option["private_actor_score"], "private_actor_score")
        if type(option.get("rights_authorized")) is not bool:
            raise ValueError("rights_authorized must be a declared boolean")
        eligible = option["rights_authorized"] and service >= floor
        rows.append({
            "name": name,
            "service_value": _rounded(service),
            "social_net_value": _rounded(service - resource - maintenance - external),
            "commercial_transactions_not_social_value": _rounded(activity),
            "private_actor_score_separate": _rounded(private),
            "rights_authorized_stipulated": option["rights_authorized"],
            "service_matched": service >= floor,
            "eligible_under_stipulated_guardrails": eligible,
        })
    if case["baseline"] not in names:
        raise ValueError("baseline not found")
    base = next(row for row in rows if row["name"] == case["baseline"])
    if not base["eligible_under_stipulated_guardrails"]:
        raise ValueError("invalid baseline guardrails")
    valid = [row for row in rows if row["eligible_under_stipulated_guardrails"]]
    social_winner = max(valid, key=lambda row: row["social_net_value"])
    private_winner = max(valid, key=lambda row: row["private_actor_score_separate"])
    for row in rows:
        row["net_difference_from_baseline"] = _rounded(row["social_net_value"] - base["social_net_value"])
        row["activity_difference_from_baseline"] = _rounded(
            row["commercial_transactions_not_social_value"]
            - base["commercial_transactions_not_social_value"])
        row["extra_service_needed_to_match_baseline"] = _rounded(
            max(0, base["social_net_value"] - row["social_net_value"]))
    return {
        "id": case["id"],
        "baseline": case["baseline"],
        "horizon": case["horizon"],
        "service_floor": floor,
        "social_surplus_winner_under_declared_guardrails": social_winner["name"],
        "private_actor_winner_under_declared_preferences": private_winner["name"],
        "private_social_rankings_diverge": social_winner["name"] != private_winner["name"],
        "options": rows,
    }


def _park(case: dict) -> dict:
    """Distinct parent, child, and resource ledgers. No interpersonal sum."""
    _requires_true(case, "independent_use_and_functionality_stipulated",
                   "all_intertemporal_values_same_pv_date_stipulated")
    p_use = _prob(case["prob_use"], "prob_use")
    p_functional = _prob(case["prob_functional_at_eligibility"], "prob_functional")
    years = _number(case["years_to_eligible"], "years_to_eligible", 0)
    benefit = _number(case["value_if_used_and_functional"], "service_if_used", 0)
    capital = _number(case["capital_resource_cost"], "capital_cost", 0)
    maintenance = _number(case["maintenance_real_cost"], "maintenance", 0)
    current_tax = _number(case["present_tax_revenue_pv"], "present_tax", 0)
    future_levy = _number(case["future_tax_liability_pv"], "future_tax", 0)
    parent_tax = _number(case["parent_current_private_tax"], "parent_tax", 0)
    parent_value = _number(case["parent_identity_value"], "parent_value")
    # Fiscal financing allocates costs across cohorts; do not add levy a second
    # time to real costs, and do not infer TOTAL welfare absent other preferences.
    if not math.isclose(current_tax + future_levy, capital + maintenance, abs_tol=1e-9):
        raise ValueError("present and future tax PV must finance declared real resources")
    if parent_tax > current_tax:
        raise ValueError("parent contribution cannot exceed current tax pool")
    expected_service = p_use * p_functional * benefit
    parent_private = parent_value - parent_tax
    child_private = expected_service - future_levy
    net_resource = expected_service - capital - maintenance
    probability_product_threshold = ((capital + maintenance) / benefit) if benefit else None
    return {
        "id": case["id"],
        "years_until_child_eligible": years,
        "assumed_independent_use_and_functionality": True,
        "probability_product_useful": _rounded(p_use * p_functional),
        "expected_child_service_value": _rounded(expected_service),
        "future_tax_pv_is_transfer_not_extra_social_cost": _rounded(future_levy),
        "parent_private_gain_from_symbolic_care": _rounded(parent_private),
        "child_net_of_allocated_future_tax": _rounded(child_private),
        "child_service_minus_real_resources_NOT_full_social_welfare": _rounded(net_resource),
        "social_break_even_use_times_functional": (
            _rounded(probability_product_threshold) if probability_product_threshold is not None else None),
        "parent_prefers_build_in_simplified_two_choice_problem": parent_private > 0,
        "child_service_exceeds_real_resources_before_unaggregated_preferences": net_resource > 0,
    }


def _risk(case: dict) -> dict:
    _requires_true(case, "normal_lotteries_characterized_stipulated",
                   "same_actor_horizon_numerario_stipulated")
    stay = RiskOutcome(**case["stay"])
    redesign = RiskOutcome(**case["redesign"])
    choice = RiskChoice(
        stay=stay, redesign=redesign,
        gamma=_number(case["gamma"], "gamma", 0),
        transition_cost=_number(case["transition_cost"], "transition_cost", 0),
        choice_sensitivity=_number(case["choice_sensitivity"], "choice_sensitivity", 0),
    )
    if choice.choice_sensitivity == 0:
        raise ValueError("choice sensitivity > 0")
    delta = change_advantage_ce(choice)
    risk_excess = redesign.variance - stay.variance
    # This threshold applies only when gamma>0 and all CARA-normal assumptions hold.
    cutoff = (stay.variance + 2 * (redesign.mean - stay.mean - choice.transition_cost) / choice.gamma
              if choice.gamma else None)
    res = {
        "id": case["id"],
        "gamma_fixed_within_case": choice.gamma,
        "stay_ce": _rounded(certainty_equivalent(stay, choice.gamma)),
        "redesign_ce_after_one_transition_cost": _rounded(
            certainty_equivalent(redesign, choice.gamma) - choice.transition_cost),
        "redesign_mean_gain_before_cost": _rounded(redesign.mean - stay.mean),
        "redesign_excess_variance": _rounded(risk_excess),
        "redesign_ce_advantage": _rounded(delta),
        "preferred_under_characterized_cara_normal": preferred_course(choice),
        "exit_probability_postulated_logit_NOT_success": _rounded(exit_probability(choice)),
        "strict_stay_if_redesign_variance_exceeds": _rounded(cutoff) if cutoff is not None else None,
    }
    if "defend" in case:
        d = case["defend"]
        defense = DefencePolicy(
            defended_stay=RiskOutcome(_number(d["mean"], "defense mean"),
                                      _number(d["variance"], "defense variance", 0)),
            effort_cost=_number(d["effort_cost"], "defense cost", 0),
        )
        material = _number(d["material_mean_if_bonus_removed"], "material mean")
        res["defense"] = {
            "intrinsic_utility_added_to_material_mean": _rounded(d["mean"] - material),
            "same_material_payoff_as_stay": math.isclose(material, stay.mean),
            "same_variance_as_stay": math.isclose(d["variance"], stay.variance),
            "certainty_equivalents": {
                k: _rounded(v) for k, v in policy_certainty_equivalents(choice, defense).items()
            },
            "preferred": preferred_with_defense(choice, defense),
            "not_a_new_nonisomorphic_mechanism_without_a_projection_witness": True,
        }
    if "stipulated_current_welfare" in case:
        current = _number(case["stipulated_current_welfare"], "current welfare")
        distress = _number(case["stipulated_discomfort"], "synthetic F", 0)
        forecast = _number(case["forecast_future_stay"], "stay future forecast")
        res["stipulations_not_human_observations"] = {
            "current_welfare": _rounded(current),
            "synthetic_discomfort_F": _rounded(distress),
            "forecast_future_stay_below_current": forecast < current,
        }
    return res


def _route(case: dict) -> dict:
    _requires_true(case, "independent_identical_steps_stipulated")
    q = _prob(case["step_success_probability"], "q")
    steps_raw = _number(case["steps"], "steps", 1)
    if not steps_raw.is_integer():
        raise ValueError("steps must be integer")
    n = int(steps_raw)
    benefit = _number(case["breach_reduction_on_success"], "B", 0)
    loss = _number(case["breach_increase_on_failure"], "L", 0)
    p = q ** n
    delta_gap = (1 - p) * loss - p * benefit
    bound = loss / (benefit + loss) if benefit + loss else None
    return {
        "id": case["id"], "steps": n, "step_success_probability": q,
        "completion_probability_under_iid_steps": _rounded(p),
        "probability_at_least_one_damaging_failure": _rounded(1 - p),
        "expected_change_in_G_versus_stay": _rounded(delta_gap),
        "expected_G_decreases": delta_gap < 0,
        "success_probability_break_even_if_total_outcomes_positive": (
            _rounded(bound) if bound is not None else None),
        "no_claim_about_human_F_or_choice": True,
    }


def _distribution(case: dict) -> dict:
    _requires_true(case, "comparable_housing_and_wage_units_stipulated")
    base_w = _number(case["reference_wage_index"], "reference wage", 1e-12)
    late_w = _number(case["late_wage_index"], "late wage", 1e-12)
    base_p = _number(case["reference_housing_price_index"], "reference price", 1e-12)
    late_p = _number(case["late_housing_price_index"], "late price", 1e-12)
    early_share = _prob(case["reference_pension_transfer_share"], "reference contribution")
    late_share = _prob(case["late_pension_transfer_share"], "later contribution")
    if early_share == 1 or late_share == 1:
        raise ValueError("residual income cannot be zero in burden comparison")
    return {
        "id": case["id"], "statistical_estimate": False,
        "gross_housing_price_to_wage_multiplier": _rounded(
            (late_p / late_w) / (base_p / base_w)),
        "net_after_declared_transfer_multiplier": _rounded(
            (late_p / (late_w * (1 - late_share)))
            / (base_p / (base_w * (1 - early_share)))),
        "do_not_infer_actual_national_cohort_data": True,
    }


def _sensitivity(catalog: dict) -> dict:
    """Predeclared finite grids. These are sign diagrams, not calibrated forecasts."""
    spec = catalog["sensitivity"]

    def find(group: str, id: str) -> dict:
        return next((x for x in catalog[group] if x["id"] == id), None) or (
            _raise_invalid_reference(group, id))

    base = find("risk_cases", spec["risk_reference_id"])
    risk_grid = []
    for g in spec["gamma_grid"]:
        gamma = _number(g, "gamma grid", 0)
        for v in spec["redesign_variance_grid"]:
            variance = _number(v, "variance grid", 0)
            choice = RiskChoice(
                RiskOutcome(**base["stay"]),
                RiskOutcome(base["redesign"]["mean"], variance), gamma,
                transition_cost=base["transition_cost"])
            risk_grid.append({
                "gamma": _rounded(gamma), "redesign_variance": _rounded(variance),
                "ce_gain_redesign": _rounded(change_advantage_ce(choice)),
                "preferred": preferred_course(choice),
            })

    park = find("park_cases", spec["park_reference_id"])
    park_grid = []
    for u in spec["park_prob_use_grid"]:
        p_use = _prob(u, "use grid")
        for f in spec["park_prob_functional_grid"]:
            p_fun = _prob(f, "function grid")
            expected = p_use * p_fun * park["value_if_used_and_functional"]
            margin = expected - park["capital_resource_cost"] - park["maintenance_real_cost"]
            park_grid.append({
                "prob_use": _rounded(p_use), "prob_functional": _rounded(p_fun),
                "child_service_less_real_resource_cost": _rounded(margin),
                "positive_excluding_unaggregated_preferences": margin > 0,
            })

    route = find("route_cases", spec["route_reference_id"])
    route_grid = []
    for n in spec["step_count_grid"]:
        for q in spec["step_success_grid"]:
            row = _route({
                **route, "steps": n, "step_success_probability": q})
            route_grid.append({
                "steps": row["steps"], "q": row["step_success_probability"],
                "expected_change_in_G": row["expected_change_in_G_versus_stay"],
                "expected_G_decreases": row["expected_G_decreases"],
            })
    return {
        "risk_sign_grid": risk_grid,
        "park_real_resource_grid": park_grid,
        "route_composition_grid": route_grid,
        "grid_status": "PREREGISTERED_SYNTHETIC_PARAMETERS_NO_FITTING",
    }


def _raise_invalid_reference(group: str, id: str):
    raise ValueError(f"{group}: unknown sensitivity reference {id}")


def run_campaign(catalog: dict) -> dict:
    if catalog.get("schema") != SCHEMA or catalog.get("status") != STATUS:
        raise ValueError("incorrect schema or empirical status")
    groups = (
        ("static_cases", _static), ("park_cases", _park),
        ("risk_cases", _risk), ("route_cases", _route),
        ("distribution_cases", _distribution),
    )
    seen: set[str] = set()
    results = {}
    for group, evaluator in groups:
        cases = catalog.get(group)
        if not isinstance(cases, list) or not cases:
            raise ValueError(f"{group}: non-empty array required")
        for case in cases:
            _check_identity(case, group, seen)
        results[group] = [evaluator(case) for case in cases]
    canonical = json.dumps(catalog, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return {
        "schema": SCHEMA,
        "status": STATUS,
        "input_sha256": hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
        "count_cases": len(seen),
        "note": (
            "Finite synthetic counterexamples/positive controls, not estimates. "
            "Only within-case actors/units/horizons may be compared. "
            "F human, B/C/D exterior probabilities, authority and legitimacy not inferred."
        ),
        "results": results,
        "sensitivity": _sensitivity(catalog),
    }


def load_catalog(path: Path | None = None) -> dict:
    file = HERE / "SCENARIO_PARAMETERS.json" if path is None else path
    return json.loads(file.read_text(encoding="utf-8"))


if __name__ == "__main__":
    print(json.dumps(run_campaign(load_catalog()), ensure_ascii=False, sort_keys=True, indent=2))
