"""ACC synthetic mechanism bridges: HID, attribution, map/flow and debt ledger.

These are bounded analytical models, never organisational measurements.
"""

import argparse
import json
from pathlib import Path


class ModelError(ValueError):
    pass


def num(x, name, maximum=None):
    if isinstance(x, bool) or not isinstance(x, (float, int)):
        raise ModelError(f"{name}: expected numeric value")
    x = float(x)
    if not x >= 0 or (maximum is not None and x > maximum):
        raise ModelError(f"{name}: expected nonnegative value within limit")
    return x


def vector(x, name):
    if not isinstance(x, dict) or not x:
        raise ModelError(f"{name}: nonempty input vector required")
    return {k: num(v, f"{name}.{k}") for k, v in x.items()}


def series(x, name):
    if not isinstance(x, list) or not x:
        raise ModelError(f"{name}: nonempty period list required")
    return [num(v, f"{name}[{i}]") for i, v in enumerate(x)]


def curvature(seq):
    return [seq[t] - 2 * seq[t-1] + seq[t-2] for t in range(2, len(seq))]


def hid_against_optima(s):
    """Direct HICT-HICR gap for each feasible, inputwise-dominating optimum.

    Disjoint human informational inputs, same human-hour resource, service
    vector, constraints and rights; no Frankenstein optimum.
    """
    total = num(s["human_hours"], "human_hours")
    if total == 0:
        raise ModelError("human_hours cannot be zero")
    current = s["current"]
    a = vector(current["informational_inputs"], "current")
    if sum(a.values()) > total + 1e-8:
        raise ModelError("current inputs exceed the common human-hour budget")
    usable, rejected = [], []
    for name, candidate in s["optima"].items():
        if candidate.get("resources") != current.get("resources"):
            rejected.append([name, "resources differ"])
            continue
        if candidate.get("service") != current.get("service"):
            rejected.append([name, "service differs"])
            continue
        if candidate.get("rights_preserved") is not True or candidate.get("governance_feasible") is not True:
            rejected.append([name, "rights/governance not established"])
            continue
        b = vector(candidate["informational_inputs"], name)
        if set(a) != set(b) or sum(b.values()) > total + 1e-8:
            raise ModelError(f"{name}: incompatible dimensions or human-hour budget")
        diffs = {k: b[k] - a[k] for k in a}
        if min(diffs.values()) < -1e-8 or max(diffs.values()) <= 1e-8:
            rejected.append([name, "not inputwise dominating"])
            continue
        gap = sum(diffs.values())
        usable.append({"optimum": name, "input_gaps_hours": diffs, "gap_hours": gap,
                       "HICR": sum(a.values()) / total,
                       "HICT_reference": sum(b.values()) / total,
                       "HID_reference": gap / total})
    frontier = []
    for alt in usable:
        v = alt["input_gaps_hours"]
        dominated = any(
            all(other["input_gaps_hours"][k] >= v[k] - 1e-8 for k in v)
            and any(other["input_gaps_hours"][k] > v[k] + 1e-8 for k in v)
            for other in usable if other is not alt
        )
        if dominated:
            rejected.append([alt["optimum"], "dominated by another listed feasible option"])
        else:
            frontier.append(alt)
    return {"comparisons": frontier, "excluded": rejected,
            "HID_hours_range": ([min(x["gap_hours"] for x in frontier),
                                 max(x["gap_hours"] for x in frontier)] if frontier else None),
            "scope": "feasible counterfactual human informational inputs, not distress or accumulated ACW"}


def attribution_signatures(s):
    """AG Claim A and Signature 4; all scores separately sourced and synthetic."""
    snapshots = s["snapshots"]
    if len(snapshots) < 2:
        raise ModelError("attribution requires at least two snapshots")
    rows = []
    for snap in snapshots:
        entries = []
        for pair, item in snap["pairs"].items():
            d = num(item["dependency"], "dependency", 1)
            a = num(item["attribution"], "attribution", 1)
            if not item.get("technical_source") or not item.get("declaration_source"):
                raise ModelError("independent source labels required")
            if item["technical_source"] == item["declaration_source"]:
                raise ModelError("dependency and attribution cannot share evidence source")
            raised = num(item.get("raised", 0), "raised")
            ignored = num(item.get("ignored_after_raised", 0), "ignored_after_raised")
            if ignored > raised:
                raise ModelError("ignored events cannot exceed raised events")
            entries.append({"pair": pair, "dependency": d, "attribution": a,
                            "positive_gap": max(0, d-a), "raised": raised,
                            "ignored_after_raised": ignored,
                            "cant_kill_unlisted_proxy": d >= 0.7 and a <= 0.2})
        if not entries:
            raise ModelError("empty attribution snapshot")
        rows.append({"period": snap["period"], "pairs": entries,
                     "mean_gap": sum(e["positive_gap"] for e in entries)/len(entries),
                     "raised": sum(e["raised"] for e in entries),
                     "ignored": sum(e["ignored_after_raised"] for e in entries)})
    cohorts = [{e["pair"] for e in r["pairs"]} for r in rows]
    if any(c != cohorts[0] for c in cohorts[1:]):
        raise ModelError("longitudinal cohorts differ without a prespecified adjustment")
    return {"snapshots": rows, "mean_gap_change": rows[-1]["mean_gap"]-rows[0]["mean_gap"],
            "claim_B": None, "claim_C_cause": None,
            "note": "signatures only: no contribution gate, neglect controls or causal finding"}


def retirement(s):
    """Expected obligations: vary attribution block with legitimate protections fixed."""
    flow = series(s["new_obligations"], "new_obligations")
    rate = num(s["safe_retirement_rate"], "safe_retirement_rate", 1)
    protection = num(s["legitimate_protection"], "legitimate_protection", 1)
    block = num(s["attribution_block"], "attribution_block", 1)
    hours = num(s["assumed_ACW_hours_per_obligation"], "ACW_cost")
    obligations, rows = 0.0, []
    for period, new in enumerate(flow, 1):
        old = obligations
        retired = old*rate*(1-protection)*(1-block)
        obligations = old + new - retired
        rows.append({"period": period, "opening": old, "new": new, "safely_retired": retired,
                     "closing": obligations, "synthetic_ACW_hours": obligations*hours})
    return {"series": rows, "end_ACW_hours": rows[-1]["synthetic_ACW_hours"],
            "status": "assumed causal retirement rule; not inferred from attribution scores"}


def map_flow(s, *, verification=False, disable_feedback=False):
    """Factual flow vs actor's partial map; back-action creates additional links."""
    arrivals = series(s["exogenous_new_links"], "exogenous_new_links")
    coverage = num(s["map_coverage"], "map_coverage", 1)
    feedback = num(s["backaction_links_per_hidden_link"], "backaction")
    incompatibility = num(s["incompatibility_fraction"], "incompatibility", 1)
    acw_cost = num(s["assumed_ACW_hours_per_incompatible_link"], "ACW_cost")
    verify_hours = num(s["verification_hours_per_period"], "verification_hours")
    product = num(s["production_per_capacity_period"], "production")
    stock, rows = 0.0, []
    for period, new in enumerate(arrivals, 1):
        before = stock + new
        mapped = before if verification else before*coverage
        hidden = before - mapped
        induced = 0.0 if (verification or disable_feedback) else hidden*feedback
        stock = before + induced
        actual_acw = stock*incompatibility*acw_cost
        predicted = mapped*incompatibility*acw_cost
        rows.append({"period": period, "production": period*product,
                     "true_links": stock, "mapped_links": mapped,
                     "backaction_links": induced, "synthetic_ACW_hours": actual_acw,
                     "forecast_ACW_hours": predicted,
                     "forecast_error_hours": actual_acw-predicted,
                     "verification_hours_separate": verify_hours if verification else 0.0})
    loads = [row["synthetic_ACW_hours"] for row in rows]
    return {"rows": rows, "ACW_second_difference": curvature(loads),
            "end_ACW_hours": loads[-1], "ACW_exposure_hours": sum(loads),
            "verification_hours_total": len(arrivals)*verify_hours if verification else 0}


def money_ledger(s):
    """Financial commitments, not a second definition of Human Intelligence Debt."""
    issue = series(s["issued"], "issued")
    paid = series(s["extinguished"], "extinguished")
    if len(issue) != len(paid):
        raise ModelError("money horizon mismatch")
    rate = num(s["explicit_capitalized_rate"], "capitalized_rate")
    balance, rows = 0.0, []
    for period, (new, payment) in enumerate(zip(issue, paid), 1):
        interest = balance*rate
        if payment > balance + new + interest + 1e-8:
            raise ModelError("payment exceeds outstanding monetary obligation")
        next_balance = max(0.0, balance + new + interest - payment)
        rows.append({"period": period, "opening": balance, "new": new,
                     "interest": interest, "extinguished": payment, "closing": next_balance})
        balance = next_balance
    return {"rows": rows, "closing_monetary_obligation": balance,
            "HID": None, "scope": "accounting identity; money != human intelligence debt"}


def evaluate(s):
    attribution = attribution_signatures(s["attribution"])
    retire_blocked = retirement(s["retirement"])
    retire_neutral = retirement({**s["retirement"], "attribution_block": 0})
    flow_partial = map_flow(s["information"])
    flow_complete = map_flow(s["information"], verification=True)
    flow_frozen = map_flow(s["information"], disable_feedback=True)
    money = money_ledger(s["money"])
    zero_interest = money_ledger({**s["money"], "explicit_capitalized_rate": 0})
    return {"status": "SYNTHETIC ONLY — HID2 campaigns NOT RUN",
            "HID_direct_optimum_gap": hid_against_optima(s["HID"]),
            "AG_independent_signatures": attribution,
            "AG_retirement_comparator": {"blocked": retire_blocked,
                                         "neutral": retire_neutral,
                                         "final_ACW_difference": retire_blocked["end_ACW_hours"]-retire_neutral["end_ACW_hours"]},
            "IF_policy_comparator": {"map_only": flow_partial, "verified": flow_complete,
                                     "no_backaction": flow_frozen,
                                     "final_ACW_map_vs_verified": flow_partial["end_ACW_hours"]-flow_complete["end_ACW_hours"],
                                     "final_ACW_due_to_backaction": flow_partial["end_ACW_hours"]-flow_frozen["end_ACW_hours"]},
            "money_as_commitment_ledger": {"with_rate": money, "without_rate": zero_interest,
                                           "balance_difference": money["closing_monetary_obligation"]-zero_interest["closing_monetary_obligation"]}}


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("scenario", type=Path)
    args = cli.parse_args()
    print(json.dumps(evaluate(json.loads(args.scenario.read_text(encoding="utf-8"))),
                     indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False))
