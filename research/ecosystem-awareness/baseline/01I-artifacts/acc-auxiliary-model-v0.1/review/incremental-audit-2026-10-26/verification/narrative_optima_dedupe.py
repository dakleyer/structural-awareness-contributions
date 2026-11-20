"""Round 38: PR #84's de-duplication of tied optima in #69's finite_feasible_gap.

Usage: python3 -B narrative_optima_dedupe.py <study dir on #69 4cd76d96> <study dir on #84>
       (study dir = studies/narrative-acceptance-v0.1)

On 2 000 random mode sets (1-5 modes, random capacity, fixed resource, rate
and PASS/FAIL/UNKNOWN eligibility; only cases with an admissible current
plan kept) it compares parent and fix: every field except
optimizers_with_ties must be identical, the SET of optimal allocations must
be identical, and the fix must report no allocation twice. Also prints the
two original IQ-03 periods. Exit code 1 on any failure. Writes nothing.
"""
import importlib
import random
import sys


def load(path):
    sys.modules.pop("finite_feasible_gap", None)
    sys.path.insert(0, path)
    try:
        return importlib.import_module("finite_feasible_gap")
    finally:
        sys.path.pop(0)


rng = random.Random(84)
cases = []
for _ in range(2000):
    modes = [{"id": f"m{i}", "capacity": rng.choice([2, 5, 10, 100]), "fixed_resource": rng.choice([0, 1, 3]),
              "resource_per_service": rng.choice([0, 1, 2, "1/2"]),
              "eligibility": rng.choice(["PASS", "PASS", "PASS", "FAIL", "UNKNOWN"])}
             for i in range(rng.randint(1, 5))]
    target = rng.choice([0, 1, 2, 5, 7, 10])
    current = next((m for m in modes if m["eligibility"] == "PASS" and m["capacity"] >= target), None)
    if current:
        cases.append((target, modes, {current["id"]: target}))
key = lambda r: [tuple(sorted(o.items())) for o in r["optimizers_with_ties"]]  # noqa: E731
old = load(sys.argv[1])
before = [old.optimize(*c) for c in cases]
old_iq = old.original_iq03_periods()
new = load(sys.argv[2])
after = [new.optimize(*c) for c in cases]
other = [k for k in before[0] if k != "optimizers_with_ties"]
same_other = all({k: a[k] for k in other} == {k: b[k] for k in other} for a, b in zip(before, after))
same_set = all(set(key(a)) == set(key(b)) for a, b in zip(before, after))
dup_before = sum(len(key(a)) != len(set(key(a))) for a in before)
dup_after = sum(len(key(b)) != len(set(key(b))) for b in after)
print(f"{len(cases)} cases | other fields identical: {same_other} | same set of optima: {same_set} | "
      f"cases with a repeated optimum, before/after: {dup_before}/{dup_after}")
print("IQ-03 optima before:", [p["optimizers_with_ties"] for p in old_iq],
      "| after:", [p["optimizers_with_ties"] for p in new.original_iq03_periods()])
ok = same_other and same_set and dup_after == 0
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
