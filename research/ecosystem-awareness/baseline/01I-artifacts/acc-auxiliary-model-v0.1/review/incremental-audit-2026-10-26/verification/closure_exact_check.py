"""Round 60: joint feasibility and exact thresholds in closure (PR #107, child of #106).

Usage: python3 -B closure_exact_check.py <checkout of #106> <checkout of #107>

Independent oracle (written for this audit, not taken from either PR):
data (pos_i, [l_i, u_i]) admit an L-Lipschitz function f iff the McShane
upper extension F(y) = min_i (u_i + L|y - pos_i|) satisfies F(pos_j) >= l_j
for every j. If so, the set of possible f(x) is exactly
[max_i (l_i - L|x - pos_i|), F(x)]. Everything is computed with Fraction.

  1. Defects on #106 (positive status) fixed on #107 (INCONSISTENT):
     two conflicting intervals at the same position; a reversed interval
     [10, 9] queried far enough away.
  2. Float rounding: a random search over short decimals finds cases where
     #106's float envelope gives a different status from the exact oracle;
     #107 must match the oracle on every case.
  3. Random agreement: 3,000 random closure cases (1-3 samples, decimals
     with up to 2 places, L in {0, 0.5, 1, 2}); #107's status must equal
     the oracle's in all, and its displayed bounds must enclose the exact
     bounds when consistent.
  4. Published campaign (46 cases) and sensitivity sweep identical.

Exit code 1 on a mismatch. Writes nothing.
"""
import json
import os
import random
import subprocess
import sys
from fractions import Fraction as F

STUDY = ("research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/"
         "studies/conscientia-additional-cases-v0.1")


def oracle(case):
    L, x, t = F(case["L"]), F(case["x"]), F(case["threshold"])
    s = [tuple(map(F, v)) for v in case["samples"]]
    up = lambda y: min(u + L * abs(y - p) for p, l, u in s)  # noqa: E731
    if any(up(p) < l for p, l, u in s):
        return "INCONSISTENT_ASSUMPTIONS", None
    lo, hi = max(l - L * abs(x - p) for p, l, u in s), up(x)
    st = ("PREDICATE_SUPPORTED_IN_FRAME" if lo >= t else "PREDICATE_REFUTED_IN_FRAME" if hi < t
          else "PREDICATE_UNDETERMINED")
    return st, (lo, hi)


def gen(rng):
    d = lambda: round(rng.uniform(-3, 13), rng.choice((1, 2)))  # noqa: E731
    samples = []
    for _ in range(rng.randint(1, 3)):
        a, b = sorted((d(), d())) if rng.random() < .9 else (d(), d())
        samples.append([round(rng.uniform(0, 4), rng.choice((0, 1, 2))), a, b])
    return {"id": "probe", "group": "probe", "source": "probe", "kind": "closure",
            "L": rng.choice((0, 0.5, 1, 2)), "x": round(rng.uniform(0, 4), rng.choice((0, 1, 2))),
            "threshold": d(), "samples": samples}


rng = random.Random(20261121)
CASES = [gen(rng) for _ in range(3000)]
SPECIAL = {
    "same_position_conflict": {"id": "s1", "group": "g", "source": "s", "kind": "closure", "L": 1, "x": 1,
                               "threshold": 9, "samples": [[0, 9, 9.5], [0, 10, 10.5]]},
    "reversed_interval": {"id": "s2", "group": "g", "source": "s", "kind": "closure", "L": 1, "x": 2,
                          "threshold": 7, "samples": [[0, 10, 9]]},
}
# Float-rounding search: short decimals where float and exact envelopes disagree.
frng = random.Random(7)
FLOATS = []
while len(FLOATS) < 200:
    l, d, L = round(frng.uniform(0, 1), 2), round(frng.uniform(0, 1), 2), frng.choice((0.1, 0.3, 0.7, 1.1))
    lo_float = l - L * abs(d)
    t = lo_float  # threshold exactly at the float projection
    FLOATS.append({"id": "f", "group": "g", "source": "s", "kind": "closure", "L": L, "x": d,
                   "threshold": t, "samples": [[0, l, l + 1]]})

PROBE = r'''
import json, sys, subprocess
import campaign as c
data = json.loads(sys.stdin.read())
def run(x):
    try:
        r = c.result(x); return [r["status"], r.get("bounds")]
    except Exception as e:
        return [type(e).__name__, None]
out = {k: [run(x) for x in v] for k, v in data.items()}
out["campaign"] = json.dumps(c.run_campaign(), sort_keys=True)
out["sensitivity"] = subprocess.run([sys.executable, "-B", "sensitivity.py"], capture_output=True, text=True).stdout
print(json.dumps(out))
'''
payload = json.dumps({"random": CASES, "special": list(SPECIAL.values()), "floats": FLOATS})


def probe(root):
    here = os.path.join(root, STUDY)
    r = subprocess.run([sys.executable, "-B", "-c", PROBE], cwd=here, input=payload, capture_output=True,
                       text=True, check=True, env=dict(os.environ, PYTHONPATH=here))
    return json.loads(r.stdout)


p, c = probe(sys.argv[1]), probe(sys.argv[2])
ok = True


def check(label, cond):
    global ok
    ok &= bool(cond)
    print(f"{'OK ' if cond else 'BAD'} {label}")


for (name, case), pr, cr in zip(SPECIAL.items(), p["special"], c["special"]):
    print(f"   {name:24s} #106={pr[0]}  #107={cr[0]}  oracle={oracle(case)[0]}")
check("special cases: positive status on #106, INCONSISTENT on #107 and in the oracle",
      all(pr[0] == "PREDICATE_SUPPORTED_IN_FRAME" for pr in p["special"])
      and all(cr[0] == oracle(cs)[0] == "INCONSISTENT_ASSUMPTIONS" for cr, cs in zip(c["special"], SPECIAL.values())))
fl_or = [oracle(x)[0] for x in FLOATS]
fl_p = sum(a[0] != o for a, o in zip(p["floats"], fl_or))
fl_c = sum(a[0] != o for a, o in zip(c["floats"], fl_or))
print(f"   threshold at the float projection: {len(FLOATS)} cases; #106 disagrees with exact oracle in {fl_p}, #107 in {fl_c}")
check("float rounding: #106 disagrees somewhere, #107 never", fl_p > 0 and fl_c == 0)
mism, encl = 0, 0
for case, got in zip(CASES, c["random"]):
    st, b = oracle(case)
    mism += got[0] != st
    if st != "INCONSISTENT_ASSUMPTIONS" and got[1] is not None:
        encl += not (F(got[1][0]) <= b[0] and F(got[1][1]) >= b[1])
n_inc = sum(oracle(x)[0] == "INCONSISTENT_ASSUMPTIONS" for x in CASES)
p_mism = sum(g[0] != oracle(x)[0] for x, g in zip(CASES, p["random"]))
print(f"   random: {len(CASES)} cases ({n_inc} jointly inconsistent); status != oracle: #106 {p_mism}, #107 {mism}; "
      f"#107 bounds not enclosing exact: {encl}")
check("#107 matches the oracle on every random case and its bounds enclose the exact ones", mism == 0 and encl == 0)
check("full campaign (46 cases) identical", p["campaign"] == c["campaign"])
check("sensitivity sweep identical", p["sensitivity"] == c["sensitivity"] and len(c["sensitivity"]) > 0)
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
