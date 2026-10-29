"""G-04 and L-08 (round 28): what decides the winner in PR #70's paired trials.

Usage: python3 -B g04_accuracy_map.py <checkout of PR #70>

1. Reproduces the six published regimes (1 152 paired worlds) and prints, per
   regime, (unjustified proposals, missed candidates, declared cost) per arm.
2. Sweeps the two declared accuracies that the author sets per regime,
   source_correct_if_qualified x domain_accuracy (7 x 7, other parameters of
   BALANCED_UNCERTAIN, 192 worlds each), and prints which of boundary-only and
   domain-facts-only dominates on (errors, misses).
3. Counts in how many cells SOURCE_BOUNDARY_ONLY is on the three-axis Pareto
   front, whose third axis is the author-declared instrument cost.
Writes nothing.
"""
import json
import os
import sys

CAMP = ("research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/"
        "conscientia-campaign-v0.1")
here = os.path.join(sys.argv[1], CAMP)
sys.path.insert(0, here)
os.chdir(here)
import g04_factorial as g  # noqa: E402

manifest = json.load(open("G04_PROTOCOL.json"))
published = g.run_manifest(manifest)
print("published worlds:", published["total_matched_worlds"])
for r in published["paired_regimes"]:
    cells = {a: (v["unjustified_candidate_proposals"], v["missed_feasible_candidates"], v["information_cost_units"])
             for a, v in r["policies"].items()}
    print(f"  {r['regime']:44s} {r['source_vs_facts_two_axis_order'][:34]:34s} {cells}")

base = next(x for x in manifest["regimes"] if x["id"] == "BALANCED_UNCERTAIN")["parameters"]
grid = ["1/2", "3/5", "7/10", "4/5", "9/10", "19/20", "1"]
code = {"B": "B", "D": "D", "T": "T", "I": "I"}
on_front = cells = 0
print("rows: source_correct_if_qualified | cols: domain_accuracy | B boundary dominates, D facts dominate, I incomparable, T tie")
print("       " + " ".join(f"{c:>5}" for c in grid))
for s in grid:
    marks = []
    for d in grid:
        p = dict(base, source_correct_if_qualified=s, domain_accuracy=d)
        m = {"schema": g.MANIFEST_SCHEMA, "seed": "audit-grid", "worlds_per_regime": 192,
             "regimes": [{"id": "a", "parameters": p}, {"id": "b", "parameters": p}]}
        r = g.run_manifest(m)["paired_regimes"][0]
        marks.append(code[r["source_vs_facts_two_axis_order"][0]])
        cells += 1
        on_front += "SOURCE_BOUNDARY_ONLY" in r["nonfungible_three_axis_pareto_front"]
    print(f"{s:>6} " + " ".join(f"{x:>5}" for x in marks))
print(f"SOURCE_BOUNDARY_ONLY on the three-axis Pareto front in {on_front} of {cells} cells")
