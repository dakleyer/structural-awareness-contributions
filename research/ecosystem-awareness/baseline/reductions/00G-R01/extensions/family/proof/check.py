"""Exact finite fragment of R01 extension obligations; standard library only.

No LLM, Lean, wiki, vendor API or historical replay. See README for coverage.
The domain transition function is implemented separately from the base one.
Run python3 check.py; python3 check.py --verify checks committed results.
"""
from collections import defaultdict, deque
from copy import deepcopy
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parent
CASES = {
    "H": ("resource-step", "in_scope"),
    "L": ("artifact-step", "preserves_specification"),
    "W": ("channel-step", "authorized_effect"),
}
GROUPS = (
    "task", "population", "graph", "generation", "benefit", "route_quality",
    "geometry", "exploration", "composition", "review", "costs", "resources",
    "social", "policy", "volume", "variation", "operational_state", "evaluation",
)


def parameters(radius_multiplier, cost_factor):
    return {"radius": radius_multiplier, "ce": 4, "cv": 2 * cost_factor,
            "cm": 1, "cx": 1, "budget": 6, "time_limit": 6}


def build_domain(case, n, world, params, auxiliary):
    """Four chains: M, B, A, C are evaluator labels, not public actor names.
    M/B are known admissible; A is contingent; C has a visible prohibition.
    Labels are opaque in the domain records; no mixed connectors exist.
    """
    kind, condition = CASES[case]
    records, labels = {}, {}
    for r in range(4):
        ids = [hashlib.sha256(f"{case}/{n}/{r}/{j}".encode()).hexdigest()[:16]
               for j in range(n)]
        labels[r] = tuple(ids)
        for j, oid in enumerate(ids):
            truth = bool(world & (1 << j)) if r == 2 else r != 3
            records[oid] = {
                "kind": kind, "next": ids[j + 1] if j + 1 < n else None,
                "value": F(r + 1) + F(2 * j - n + 1, 4 * n),
                "coordinate": (-1 if r % 2 else 1) * (r + 1),
                "condition_id": oid + ":condition", condition: truth,
                "principal": "principal-1", "mission": "fixed-task",
                "recipient": "actor-1", "version": 1,
            }
    return {"case": case, "records": records, "labels": labels,
            "params": params, "auxiliary": auxiliary,
            "variable_map": {g: case + ":" + g for g in GROUPS}}


def domain_verdict(domain, r):
    rows = [domain["records"][oid] for oid in domain["labels"][r]]
    predicate = CASES[domain["case"]][1]
    return all(row[predicate] for row in rows), sum(row["value"] for row in rows)


def base_verdict(n, world, r):
    return (world == (1 << n) - 1 if r == 2 else r != 3), F((r + 1) * n)


def validate_structure(domain, n, world):
    mapping = domain["variable_map"]
    if set(mapping) != set(GROUPS) or len(set(mapping.values())) != len(GROUPS):
        return False
    if any(mapping[g] != domain["case"] + ":" + g for g in GROUPS):
        return False
    ids = [oid for chain in domain["labels"].values() for oid in chain]
    if len(ids) != len(set(ids)) or set(ids) != set(domain["records"]):
        return False
    for r in range(4):
        chain = domain["labels"][r]
        if len(chain) != n or domain_verdict(domain, r) != base_verdict(n, world, r):
            return False
        for j, oid in enumerate(chain):
            row = domain["records"][oid]
            if row["next"] != (chain[j + 1] if j + 1 < n else None):
                return False
            if row["coordinate"] != (-1 if r % 2 else 1) * (r + 1):
                return False
            expected_truth = bool(world & (1 << j)) if r == 2 else r != 3
            if row[CASES[domain["case"]][1]] != expected_truth:
                return False
            if row["value"] != F(r + 1) + F(2 * j - n + 1, 4 * n):
                return False
            if (row["principal"], row["mission"], row["recipient"], row["version"]) != (
                    "principal-1", "fixed-task", "actor-1", 1):
                return False
    base_best = max(base_verdict(n, world, r)[1] for r in range(4)
                    if base_verdict(n, world, r)[0])
    domain_best = max(domain_verdict(domain, r)[1] for r in range(4)
                      if domain_verdict(domain, r)[0])
    return base_best == domain_best


# State: discovery bitmask, tuple of inspected-condition masks, budget, time, end.
# end=-1 active, 0..3 committed route, 4 abstained.
def actions(n, agents):
    yield ("wait",)
    yield ("stop",)
    for a in range(agents):
        yield ("search", a)
        for j in range(n):
            yield ("inspect", a, j)
            for b in range(agents):
                if a != b:
                    yield ("relay", a, b, j)
        for r in range(4):
            yield ("commit", a, r)


def base_step(state, event, n, world, params):
    seen, masks, budget, clock, end = state
    if end != -1:
        return None
    op = event[0]
    if op == "stop":
        return {(*state[:4], 4): F(1)}
    if op == "wait":
        cost = 1
    elif op == "search":
        if seen & (1 << event[1]):
            return None
        cost = params["ce"]
    elif op == "inspect":
        a, j = event[1:]
        if not seen & (1 << a) or masks[a] & (1 << j):
            return None
        cost = params["cv"]
    elif op == "relay":
        a, b, j = event[1:]
        if not masks[a] & (1 << j) or masks[b] & (1 << j):
            return None
        cost = params["cm"]
    else:
        a, r = event[1:]
        if r == 3 or (r == 2 and (not seen & (1 << a) or masks[a] & ~world)):
            return None
        cost = params["cx"]
    if budget < cost or clock + 1 > params["time_limit"]:
        return None
    budget -= cost
    clock += 1
    if op == "search" and params["radius"] >= 3:
        return {(seen, masks, budget, clock, -1): F(1, 2),
                (seen | (1 << event[1]), masks, budget, clock, -1): F(1, 2)}
    if op == "inspect":
        a, j = event[1:]
        masks = tuple(m | (1 << j) if i == a else m for i, m in enumerate(masks))
    if op == "relay":
        a, b, j = event[1:]
        masks = tuple(m | (1 << j) if i == b else m for i, m in enumerate(masks))
        seen |= 1 << b
    if op == "commit":
        end = event[2]
    return {(seen, masks, budget, clock, end): F(1)}


def encode(state, domain, n):
    seen, masks, budget, clock, end = state
    predicate = CASES[domain["case"]][1]
    chain = domain["labels"][2]
    users = []
    for a, mask in enumerate(masks):
        receipts = {}
        for j, oid in enumerate(chain):
            if mask & (1 << j):
                row = domain["records"][oid]
                receipts[oid] = {"source": row["condition_id"],
                                 "value": row[predicate], "version": 1,
                                 "mission": "fixed-task", "principal": "principal-1"}
        users.append({"found": bool(seen & (1 << a)), "receipts": receipts})
    return {"users": users, "balance": budget, "elapsed": clock, "end": end,
            "extra": domain["auxiliary"]}


def project(state, domain, n):
    seen, masks = 0, []
    for a, user in enumerate(state["users"]):
        if user["found"]:
            seen |= 1 << a
        mask = 0
        for j, oid in enumerate(domain["labels"][2]):
            if oid in user["receipts"]:
                mask |= 1 << j
        masks.append(mask)
    return seen, tuple(masks), state["balance"], state["elapsed"], state["end"]


def domain_step(state, event, domain, mutant=None):
    """Independent implementation on domain records, not base_step(decode())."""
    if state["end"] != -1:
        return None
    out = deepcopy(state)
    op = event[0]
    p = domain["params"]
    if op == "stop":
        out["end"] = 4
        return [(out, F(1))]
    if op == "wait":
        charge = 1
    elif op == "search":
        if out["users"][event[1]]["found"]:
            return None
        charge = p["ce"]
    elif op == "inspect":
        user = out["users"][event[1]]
        oid = domain["labels"][2][event[2]]
        if not user["found"] or oid in user["receipts"]:
            return None
        charge = 0 if mutant == "free_review" else p["cv"]
        row = domain["records"][oid]
        user["receipts"][oid] = {"source": row["condition_id"],
            "value": row[CASES[domain["case"]][1]], "version": 1,
            "mission": "fixed-task", "principal": "principal-1"}
    elif op == "relay":
        sender, receiver = out["users"][event[1]], out["users"][event[2]]
        oid = domain["labels"][2][event[3]]
        if oid not in sender["receipts"] or oid in receiver["receipts"]:
            return None
        charge = p["cm"]
        receiver["found"] = True
        receiver["receipts"][oid] = deepcopy(sender["receipts"][oid])
        if mutant == "launder_source":
            receiver["receipts"][oid]["source"] = "new-independent-source"
    else:
        user, route = out["users"][event[1]], event[2]
        if route == 3:
            return None
        if route == 2:
            if not user["found"]:
                return None
            if any(not receipt["value"] for receipt in user["receipts"].values()):
                if mutant != "ignore_denial":
                    return None
        charge = p["cx"]
        out["end"] = route
    if out["balance"] < charge or out["elapsed"] + 1 > p["time_limit"]:
        return None
    out["balance"] -= charge
    out["elapsed"] += 1
    # Auxiliary coordinates evolve, but are not visible to the participant.
    out["extra"] = (out["extra"] + 1) % 2
    if op == "search" and p["radius"] >= 3:
        found = deepcopy(out)
        found["users"][event[1]]["found"] = True
        prob = F(3, 4) if mutant == "probability" else F(1, 2)
        if mutant == "hidden_influence" and state["extra"]:
            prob = F(1)
        return [(out, 1 - prob), (found, prob)]
    return [(out, F(1))]


def observations_match(base, extended, domain, n, world):
    if "leaked_verdict" in extended:
        return False
    canonical = encode(base, domain, n)
    # Compare the whole actor-visible observation, not merely the masks.
    return all(extended[k] == canonical[k] for k in ("users", "balance", "elapsed", "end"))


def equivalent(state, event, domain, n, world, mutant=None):
    reference = base_step(state, event, n, world, domain["params"])
    for z in (0, 1):
        encoded = encode(state, domain, n)
        encoded["extra"] = z
        actual = domain_step(encoded, event, domain, mutant)
        if (actual is None) != (reference is None):
            return False
        if actual is None:
            continue
        projected = defaultdict(F)
        for next_state, probability in actual:
            decoded = project(next_state, domain, n)
            if not observations_match(decoded, next_state, domain, n, world):
                return False
            projected[decoded] += probability
        if dict(projected) != reference:
            return False
    return True


def reachable(n, world, params, agents):
    initial = (0, (0,) * agents, params["budget"], 0, -1)
    known, queue = {initial}, deque([initial])
    events = tuple(actions(n, agents))
    while queue:
        state = queue.popleft()
        for event in events:
            outcomes = base_step(state, event, n, world, params)
            if outcomes:
                for successor, probability in outcomes.items():
                    if probability and successor not in known:
                        known.add(successor)
                        queue.append(successor)
    return known, events


def run():
    counts = defaultdict(int)
    per_case = {}
    # Exact enumeration of reachable states in a budget/time-bounded fragment.
    # Additional diagnostic states exercise paid review/relay even when search
    # costs exhaust the small campaign budget; they are explicitly counted apart.
    for case in CASES:
        before = counts["reachable_state_event_pairs"]
        for n, multiplier, factor, agents in product((2, 3), (1, 3), (F(1), F(1, 2)), (1, 2)):
            params = parameters(multiplier, factor)
            assert 0 < params["cv"] < params["ce"]
            for world in range(1 << n):
                domain = build_domain(case, n, world, params, 0)
                assert validate_structure(domain, n, world)
                counts["domain_structures"] += 1
                states, events = reachable(n, world, params, agents)
                for state in sorted(states):
                    assert project(encode(state, domain, n), domain, n) == state
                    counts["state_roundtrips"] += 1
                    for event in events:
                        assert equivalent(state, event, domain, n, world), (case, state, event)
                        counts["reachable_state_event_pairs"] += 1
                for masks in product(range(1 << n), repeat=agents):
                    state = ((1 << agents) - 1, masks, F(6), 0, -1)
                    for event in events:
                        assert equivalent(state, event, domain, n, world)
                        counts["diagnostic_state_event_pairs"] += 1
                # Same full view for an unqueried condition, opposite verdicts.
                valid = (1 << n) - 1
                for omitted in range(n):
                    partial = valid ^ (1 << omitted)
                    a = build_domain(case, n, valid, params, 0)
                    b = build_domain(case, n, partial, params, 0)
                    state = (1, (partial,), F(6), 0, -1)
                    assert encode(state, a, n) == encode(state, b, n)
                    assert domain_verdict(a, 2)[0] and not domain_verdict(b, 2)[0]
                    # Full review sees the missing condition and rejects the bad route.
                    full = (1, (valid,), F(6), 0, -1)
                    assert domain_step(encode(full, a, n), ("commit", 0, 2), a)
                    assert domain_step(encode(full, b, n), ("commit", 0, 2), b) is None
                    counts["view_pairs_and_full_review_controls"] += 1
        per_case[case] = counts["reachable_state_event_pairs"] - before

    # Targeted falsifiers: each should be rejected by the relevant obligation.
    rejected = []
    n, world, p = 2, 1, parameters(3, F(1))
    good = build_domain("H", n, world, p, 0)
    oid = good["labels"][2][1]
    for name in ("non_bijective_map", "swapped_roles", "missing_edge", "false_permission",
                 "changed_benefit", "redistributed_benefits", "scope_change", "hidden_shortcut"):
        bad = deepcopy(good)
        if name == "non_bijective_map":
            bad["variable_map"]["graph"] = bad["variable_map"]["task"]
        elif name == "swapped_roles":
            mapping = bad["variable_map"]
            mapping["graph"], mapping["task"] = mapping["task"], mapping["graph"]
        elif name == "missing_edge":
            bad["records"][bad["labels"][2][0]]["next"] = None
        elif name == "false_permission":
            bad["records"][oid]["in_scope"] = True
        elif name == "changed_benefit":
            bad["records"][oid]["value"] += 1
        elif name == "redistributed_benefits":
            bad["records"][oid]["value"] += 1
            bad["records"][bad["labels"][2][0]]["value"] -= 1
        elif name == "scope_change":
            bad["records"][oid]["mission"] = "different-task"
        else:
            bad["records"]["extra-route"] = deepcopy(bad["records"][oid])
        assert not validate_structure(bad, n, world), name
        rejected.append(name)
    diagnostics = {
        "free_review": ((1, (0, 0), F(6), 0, -1), ("inspect", 0, 1)),
        "launder_source": ((3, (1, 0), F(6), 0, -1), ("relay", 0, 1, 0)),
        "ignore_denial": ((1, (2, 0), F(6), 0, -1), ("commit", 0, 2)),
        "probability": ((0, (0, 0), F(6), 0, -1), ("search", 0)),
        "hidden_influence": ((0, (0, 0), F(6), 0, -1), ("search", 0)),
    }
    for name, (state, event) in diagnostics.items():
        assert not equivalent(state, event, good, n, world, name), name
        rejected.append(name)
    state = (1, (0,), F(6), 0, -1)
    leaked = encode(state, good, n)
    leaked["leaked_verdict"] = False
    assert not observations_match(state, leaked, good, n, world)
    rejected.append("oracle_leak")

    # Structural membership is not performance invariance at original parameters.
    s = (0, (0,), F(6), 0, -1)
    small = base_step(s, ("search", 0), 2, 3, parameters(1, F(1)))
    large = base_step(s, ("search", 0), 2, 3, parameters(3, F(1)))
    assert small != large
    queried = (1, (0,), F(1), 0, -1)
    assert base_step(queried, ("inspect", 0, 0), 2, 3, parameters(3, F(1))) is None
    assert base_step(queried, ("inspect", 0, 0), 2, 3, parameters(3, F(1, 2))) is not None
    return {"status": "PASS", "scope": "exact finite constructed fragment only",
            "base_commit": "114ac132bc2be4e7008001fe505bf5bd4c36c515",
            "counts": dict(counts), "state_event_pairs_by_case": per_case,
            "rejected_mutations": rejected,
            "parameter_change_counterexamples": ["radius_changes_discovery", "lower_cost_changes_affordability"],
            "historical_reproduction": False, "full_R01_simulator": False,
            "EA_evaluation": False,
            "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    result = run()
    output = ROOT / "results.json"
    if args.verify:
        assert json.loads(output.read_text()) == result, "Committed report differs"
    else:
        output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(result, indent=2, ensure_ascii=False))
