"""K-03 (round 25): PR #67 refactor is output-equivalent to main and keeps the oracle private.

Usage: python3 -B k03_equivalence.py <checkout of main> <checkout of PR #67>

1. sample_report() is identical in both versions, and its two former literals
   (2 and 0) are now computed.
2. On random worlds (n in 2..32, root caps from free to saturated, extra 1..3,
   every target, every policy mode) policy() and score_public_plan() return
   identical dicts in both versions.
3. The functions that must not see private truth (upstream_B, public_outline,
   receiver_B_valid, plan_from_public, receiver_decision) do not call deliver()
   or private_selected_response() in PR #67.
Exit code 1 on any difference. Writes nothing.
"""
import ast
import importlib.util
import os
import random
import sys

REL = "research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/intrinsic-abcd-economics-v0.1/intrinsic_abcd.py"


def load(name, root):
    spec = importlib.util.spec_from_file_location(name, os.path.join(root, REL))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


old, new = load("abcd_main", sys.argv[1]), load("abcd_pr67", sys.argv[2])
fails = []
ro, rn = old.sample_report(), new.sample_report()
print("sample_report identical:", ro == rn, "| gains:", rn["baseline_world_private_selected_gain"],
      rn["root_bottleneck_world_private_selected_gain"])
if ro != rn:
    fails.append("sample_report")

rng = random.Random(67)
modes = ("A_ONLY", "B_QUALIFIED", "TARGETED_EXPLORATION_OF_A", "FULL_EXPAND_A")
checked = 0
for _ in range(200):
    n = rng.choice([2, 4, 8, 16, 32])
    bits = tuple(rng.randrange(2) for _ in range(n))
    cap = rng.choice([None, 8 * n, 8 * n + 1, 8 * n + 2, 8 * n + 5])
    extra = rng.choice([1, 2, 3])
    worlds = (old.balanced_tree(bits, cap_root=cap), new.balanced_tree(bits, cap_root=cap))
    for k in range(n):
        target = f"source-{k}"
        b_old = old.upstream_B(worlds[0], target, now=5, ttl=10, extra=extra)
        b_new = new.upstream_B(worlds[1], target, now=5, ttl=10, extra=extra)
        for mode in modes:
            po = old.policy(worlds[0], target, mode, old.Costs(), now=6, b=b_old, extra=extra)
            pn = new.policy(worlds[1], target, mode, new.Costs(), now=6, b=b_new, extra=extra)
            checked += 1
            if po != pn:
                fails.append(("policy", n, cap, extra, target, mode))
        plan = {"target": target, "promised_increment": rng.randrange(4), "estimated_information_cost": rng.randrange(4)}
        so = old.score_public_plan(worlds[0], dict(plan), old.Costs(), extra=extra)
        sn = new.score_public_plan(worlds[1], dict(plan), new.Costs(), extra=extra)
        checked += 1
        if so != sn:
            fails.append(("score", n, cap, extra, target))
print("policy/score comparisons:", checked, "| differences:", len(fails))

tree = ast.parse(open(os.path.join(sys.argv[2], REL)).read())
for fn in tree.body:
    if isinstance(fn, ast.FunctionDef) and fn.name in (
            "upstream_B", "public_outline", "receiver_B_valid", "plan_from_public", "receiver_decision"):
        calls = {c.func.id for c in ast.walk(fn) if isinstance(c, ast.Call) and isinstance(c.func, ast.Name)}
        leak = calls & {"deliver", "private_selected_response"}
        print(f"{fn.name}: private calls {sorted(leak) or 'none'}")
        if leak:
            fails.append(("leak", fn.name))
print("RESULT:", "PASS" if not fails else f"FAIL {fails[:5]}")
sys.exit(1 if fails else 0)
