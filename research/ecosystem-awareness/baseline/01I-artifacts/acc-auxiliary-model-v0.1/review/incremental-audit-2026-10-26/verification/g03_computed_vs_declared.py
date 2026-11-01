"""G-03 and L-07 (round 26): what PR #68 now computes and what it still declares.

Usage: python3 -B g03_computed_vs_declared.py <checkout of PR #66> <checkout of PR #68>

1. campaign.finite_information() and source_anchored_microexperiments() give
   numerically the same report in #66 (literals) and #68 (computed).
2. The information functions respond to the worlds: XOR gives 0/0/1 bits,
   copying q1 gives 1/0/1, and changing the two-world table changes H.
3. For the 40 social cases of ORIGINAL_EXPERIMENTS.json: how many constraints
   are declared statuses versus tests on the computed outcome, and which kind
   decides each non-eligible admission (L-07).
Exit code 1 if 1 or 2 fail. Writes nothing.
"""
import collections
import importlib
import json
import os
import sys

CAMP = "research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/conscientia-campaign-v0.1"
fails = []


def report(root):
    here = os.path.join(root, CAMP)
    sys.path.insert(0, here)
    cwd = os.getcwd()
    os.chdir(here)
    try:
        for name in ("campaign", "dimension_experiment"):
            sys.modules.pop(name, None)
        camp = importlib.import_module("campaign")
        return {"fi": camp.finite_information(), "sam": camp.source_anchored_microexperiments()}
    finally:
        os.chdir(cwd)
        sys.path.remove(here)


def numeric_equal(a, b):
    if isinstance(a, dict) and isinstance(b, dict):
        return a.keys() == b.keys() and all(numeric_equal(a[k], b[k]) for k in a)
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(numeric_equal(x, y) for x, y in zip(a, b))
    return a == b


old, new = report(sys.argv[1]), report(sys.argv[2])
same = numeric_equal(old, new)
print("report blocks numerically identical (#66 vs #68):", same)
if not same:
    fails.append("report")

sys.path.insert(0, os.path.join(sys.argv[2], CAMP))
de = importlib.import_module("dimension_experiment")
I, H = de.conditional_information, de.conditional_entropy
xor = [{"q1": a, "q2": b, "r": a ^ b} for a in (0, 1) for b in (0, 1)]
copy = [{"q1": a, "q2": b, "r": a} for a in (0, 1) for b in (0, 1)]
got = [(I(w, "r", ["q1"]), I(w, "r", ["q2"]), I(w, "r", ["q1", "q2"])) for w in (xor, copy)]
print("XOR bits:", got[0], "| copy-q1 bits:", got[1])
if got != [(0.0, 0.0, 1.0), (1.0, 0.0, 1.0)]:
    fails.append("information")
w1 = [{"a": "READY", "b": 0, "r": 0}, {"a": "READY", "b": 1, "r": 1}]
w2 = [{"a": "READY", "b": 0, "r": 0}, {"a": "READY", "b": 1, "r": 0}]
print("H(r|a), H(r|a,b):", (H(w1, "r", ["a"]), H(w1, "r", ["a", "b"])), "| with r constant:",
      (H(w2, "r", ["a"]), H(w2, "r", ["a", "b"])))

cases = json.load(open(os.path.join(sys.argv[2], CAMP, "ORIGINAL_EXPERIMENTS.json")))["cases"]
declared = computed = 0
table = collections.Counter()
for case in cases:
    kind = {c["id"]: ("declared" if "satisfied" in c else "computed") for c in case.get("constraints", [])}
    declared += sum(v == "declared" for v in kind.values())
    computed += sum(v == "computed" for v in kind.values())
    r = de.run_case(case)
    deciding = sorted({kind[c["id"]] for c in r["constraints"] if c["status"] in ("FAILED", "UNKNOWN")})
    table[(r["admission"], "+".join(deciding) or "-")] += 1
print(f"social cases: {len(cases)} | constraints declared: {declared}, computed on the outcome: {computed}")
for (admission, deciding), n in sorted(table.items()):
    print(f"   {n:3d}  {admission:36s} decided by: {deciding}")
print("RESULT:", "PASS" if not fails else f"FAIL {fails}")
sys.exit(1 if fails else 0)
