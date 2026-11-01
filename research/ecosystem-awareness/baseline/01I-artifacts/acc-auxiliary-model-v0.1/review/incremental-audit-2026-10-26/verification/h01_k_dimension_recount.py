"""Round 35: independent R/C partial-order recount for PR #76's dimensional correction.

Usage: python3 -B h01_k_dimension_recount.py <checkout of PR #76>

Rebuilds the 180 declared sensitivity cells and compares (0,0) with (1,1)
in two separate dimensions, without netting: R = per-actor toy payoff
(increase is better, actor by actor) and C = per-actor coordination burden
(0 before, k after; increase is worse). Classifies each cell as monotone,
trade-off, no improvement or equivalent, and does the same for the 39 strict
scalar traps. Does not use dimensional_contract.py. Expected on ea1a8c6b:
46 / 92 / 38 / 4 and, among the traps, 13 monotone and 26 trade-offs.
Exit code 1 on a mismatch. Writes nothing.
"""
import collections
import json
import os
import sys
from copy import deepcopy
from fractions import Fraction as F
from itertools import product

here = os.path.join(sys.argv[1], "research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/"
                                 "studies/bounded-traps-v0.1")
sys.path.insert(0, here)
os.chdir(here)
import strategic_choice as sc  # noqa: E402

study = json.load(open("H01_STRATEGIC_STUDY.json"))
plan = study["sensitivity"]
dims = ("standalone_returns", "investment_costs", "pairwise_synergies", "individual_joint_burdens")
S = ((0, 0), (0, 1), (1, 0), (1, 1))
cells, traps = collections.Counter(), collections.Counter()
for ret, cost, gain, burden in product(*(plan[k] for k in dims)):
    g = deepcopy(study["base_game"])
    for a in g["actors"]:
        a["standalone_return"], a["investment_cost"] = ret, cost
        a["complementarity_from"] = {k: gain for k in a["complementarity_from"]}
    for k in g["joint"]["burden_payoff_units"]:
        g["joint"]["burden_payoff_units"][k] = burden
    P = {s: [F(x) for x in sc.payoff(s, g)] for s in S}
    before, after = P[tuple(g["current"])], P[tuple(g["target"])]
    r_up = any(b > a for a, b in zip(before, after))
    r_down = any(b < a for a, b in zip(before, after))
    c_worse = any(F(v) > 0 for v in g["joint"]["burden_payoff_units"].values())
    better, worse = r_up, r_down or c_worse
    rel = "TRADEOFF" if better and worse else "NO_IMPROVEMENT" if worse else "MONOTONE" if better else "EQUIVALENT"
    cells[rel] += 1
    flip = lambda s, i: tuple(1 - v if j == i else v for j, v in enumerate(s))  # noqa: E731
    strict = lambda s: all(P[s][i] > P[flip(s, i)][i] for i in (0, 1))  # noqa: E731
    if strict((0, 0)) and strict((1, 1)) and all(P[(1, 1)][i] > P[(0, 0)][i] for i in (0, 1)):
        traps[rel] += 1
print("R/C partial order over 180 cells:", dict(cells))
print("among the 39 strict scalar traps:", dict(traps))
ok = (dict(cells) == {"MONOTONE": 46, "TRADEOFF": 92, "NO_IMPROVEMENT": 38, "EQUIVALENT": 4}
      and dict(traps) == {"MONOTONE": 13, "TRADEOFF": 26})
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
