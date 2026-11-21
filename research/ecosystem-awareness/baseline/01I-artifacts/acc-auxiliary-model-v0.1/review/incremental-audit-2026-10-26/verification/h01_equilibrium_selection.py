"""H-01 and L-10 (round 33): Nash, Pareto and equilibrium selection for PR #76.

Usage: python3 -B h01_equilibrium_selection.py <checkout of PR #76>

1. For the base game in H01_STRATEGIC_STUDY.json: feasibility and payoffs of
   the four profiles, pure Nash equilibria and Pareto order, computed here
   from payoff() alone (not from classify()).
2. Harsanyi-Selten risk dominance between (0,0) and (1,1): products of the
   unilateral deviation losses, and the belief threshold p* that the other
   actor moves above which moving is the best response.
3. Rebuilds the 180 cells of the declared sensitivity grid exactly as
   strategic_choice.sensitivity_grid patches them and, for every cell where
   (0,0) and (1,1) are both strict Nash and (1,1) Pareto-dominates (0,0),
   reports whether (0,0) is risk-dominant, (1,1) is, or they tie.
4. Checks that bounded_traps.py and REFERENCE_SYNTHETIC_RESULTS.json are
   byte-identical to main.
Writes nothing.
"""
import collections
import json
import os
import subprocess
import sys
from copy import deepcopy
from fractions import Fraction
from itertools import product

root = sys.argv[1]
REL = "research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/bounded-traps-v0.1"
here = os.path.join(root, REL)
sys.path.insert(0, here)
os.chdir(here)
import strategic_choice as sc  # noqa: E402

study = json.load(open("H01_STRATEGIC_STUDY.json"))
S = ((0, 0), (0, 1), (1, 0), (1, 1))


def analyse(g):
    if not all(sc.feasible(s, g) for s in S):
        return None
    P = {s: tuple(Fraction(x) for x in sc.payoff(s, g)) for s in S}
    flip = lambda s, i: tuple(1 - v if j == i else v for j, v in enumerate(s))  # noqa: E731
    strict = {s: all(P[s][i] > P[flip(s, i)][i] for i in (0, 1)) for s in S}
    nash = [s for s in S if all(P[s][i] >= P[flip(s, i)][i] for i in (0, 1))]
    l00 = (P[(0, 0)][0] - P[(1, 0)][0]) * (P[(0, 0)][1] - P[(0, 1)][1])
    l11 = (P[(1, 1)][0] - P[(0, 1)][0]) * (P[(1, 1)][1] - P[(1, 0)][1])
    # player 0 moves iff p*P11 + (1-p)*P10 > p*P01 + (1-p)*P00
    a, b = P[(1, 1)][0] - P[(0, 1)][0], P[(0, 0)][0] - P[(1, 0)][0]
    pstar = b / (a + b) if a + b else None
    return P, nash, strict, l00, l11, pstar


P, nash, strict, l00, l11, pstar = analyse(study["base_game"])
print("base payoffs:", {s: tuple(str(x) for x in v) for s, v in P.items()})
print("pure Nash:", nash, "| strict:", [s for s in S if strict[s]],
      "| (1,1) Pareto-dominates (0,0):", all(P[(1, 1)][i] > P[(0, 0)][i] for i in (0, 1)))
print(f"risk dominance: deviation-loss product at (0,0) = {l00}, at (1,1) = {l11}; belief threshold p* = {pstar}")

plan = study["sensitivity"]
dims = ("standalone_returns", "investment_costs", "pairwise_synergies", "individual_joint_burdens")
tally = collections.Counter()
cells = 0
for ret, cost, gain, burden in product(*(plan[k] for k in dims)):
    g = deepcopy(study["base_game"])
    for actor in g["actors"]:
        actor["standalone_return"] = ret
        actor["investment_cost"] = cost
        actor["complementarity_from"] = {k: gain for k in actor["complementarity_from"]}
    for k in g["joint"]["burden_payoff_units"]:
        g["joint"]["burden_payoff_units"][k] = burden
    cells += 1
    res = analyse(g)
    if not res:
        continue
    P, nash, strict, l00, l11, _ = res
    if strict[(0, 0)] and strict[(1, 1)] and all(P[(1, 1)][i] > P[(0, 0)][i] for i in (0, 1)):
        tally["(0,0) risk-dominant" if l00 > l11 else "(1,1) risk-dominant" if l11 > l00 else "tie"] += 1
print(f"grid cells: {cells} | Pareto-inferior strict traps by risk dominance: {dict(tally)}")

for name in ("bounded_traps.py", "REFERENCE_SYNTHETIC_RESULTS.json"):
    same = subprocess.run(["git", "-C", root, "diff", "--quiet", "origin/main", "--", f"{REL}/{name}"]).returncode == 0
    print(f"{name} identical to main: {same}")
