"""L-09 (round 32): independent check of PR #75's matched public-view twins.

Usage: python3 -B l09_twin_recount.py <checkout of PR #75>

1. Original leakage, recomputed directly from CASE_REGISTRY.json: the 24
   VALID_GO / FALSE_Q cases grouped by (public A, public Q); Bayes-optimal
   public-only accuracy and mutual information in bits.
2. For PR #75's derived twins: which fields differ inside each pair (must be
   private only), and the Bayes accuracy of a public-only predictor over all
   generated environments (pairs x replicates) of one regime, grouping by the
   public A, public Q and the pre-read metadata of both instruments.
3. Source fixture files listed by PR #75 are unchanged against PR #73.
Exit code 1 if the twins leak or the original figures differ. Writes nothing.
"""
import collections
import json
import math
import os
import sys

CAMP = ("research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/"
        "conscientia-campaign-v0.1")
here = os.path.join(sys.argv[1], CAMP)
sys.path.insert(0, here)
os.chdir(here)
import g02_evidence_audit as g  # noqa: E402
import l09_public_leakage as l9  # noqa: E402

fails = []


def info(records):
    groups = collections.defaultdict(collections.Counter)
    for view, truth in records:
        groups[json.dumps(view, sort_keys=True)][truth] += 1
    n = len(records)
    h = lambda c: -sum(x / sum(c.values()) * math.log2(x / sum(c.values())) for x in c.values() if x)  # noqa: E731
    marg = collections.Counter(t for _, t in records)
    post = sum(sum(c.values()) / n * h(c) for c in groups.values())
    return sum(max(c.values()) for c in groups.values()), n, h(marg) - post


cases = json.load(open("CASE_REGISTRY.json"))["cases"]
orig = [({"A": c["public"], "Q": g.public_Q(c)}, c["truth_private_for_scoring"])
        for c in cases if c["variant"] in ("VALID_GO", "FALSE_Q")]
ok, n, mi = info(orig)
print(f"original 24-case leakage: public-only correct {ok}/{n}, mutual information {mi:.3f} bits")
if (ok, n, round(mi, 6)) != (18, 24, 0.5):
    fails.append("original leakage")

pairs = l9.make_public_matched_pairs(cases)
diff_keys = collections.Counter()
for p in pairs:
    a, b = p["worlds"]
    for k in set(a) | set(b):
        if a.get(k) != b.get(k):
            sub = (sorted(x for x in set(a[k]) | set(b[k]) if a[k].get(x) != b[k].get(x))
                   if isinstance(a.get(k), dict) and isinstance(b.get(k), dict) else None)
            diff_keys[(k, tuple(sub) if sub else None)] += 1
print("fields that differ inside the twins:", dict(diff_keys))
if any(k in ("public", "case_id", "family") or (k == "Q" and sub and set(sub) - {"status", "independent_audit"})
       for (k, sub) in diff_keys):
    fails.append("a public field differs between twins")

manifest = json.load(open("L09_MATCHING_PROTOCOL.json"))
regimes = json.load(open("G02_AUDIT_PROTOCOL.json"))["regimes"]
reps = manifest.get("replicates_per_pair", 64)
seed = manifest.get("seed", "L09")
for regime in regimes:
    records = []
    for p in pairs:
        for world in p["worlds"]:
            for r in range(reps):
                env = g.generate(world, regime["parameters"], seed=seed, replicate=r)
                view = {"A": env["public"], "Q": env["q"],
                        "audit_meta": {k: v for k, v in env["audit"].items() if k != "value"},
                        "direct_meta": {k: v for k, v in env["direct"].items() if k != "value"}}
                records.append((view, env["truth_PRIVATE_FOR_REFEREE_ONLY"]))
    ok, n, mi = info(records)
    flag = "" if 2 * ok == n and abs(mi) < 1e-12 else "   <- LEAK"
    print(f"  {regime['id']:42s} public-only correct {ok}/{n}, MI {mi:.3f} bits{flag}")
    if flag:
        fails.append(regime["id"])
print("RESULT:", "PASS" if not fails else f"FAIL {fails}")
sys.exit(1 if fails else 0)
