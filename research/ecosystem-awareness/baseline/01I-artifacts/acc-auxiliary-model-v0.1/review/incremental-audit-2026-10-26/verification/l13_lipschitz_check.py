"""Round 59: L-13 repair in PR #106 (child of #105): nonnegative Lipschitz constant in closure.

Usage: python3 -B l13_lipschitz_check.py <checkout of #105> <checkout of #106>

CLOSURE-02 (threshold 9, samples [9, 10] at distance 1) with L replaced,
both trees, separate subprocesses. Reports (status, bounds) or the exception.

  1. L-13: L = -0.4 and L = -5e-324 classified on #105, ValueError on #106.
  2. Unchanged: L = 0.4, L = 0, L = -0.0, L = None and the three published
     closure cases.
  3. Full campaign (46 cases) and sensitivity sweep identical.

Exit code 1 on a mismatch. Writes nothing.
"""
import json
import os
import subprocess
import sys

STUDY = ("research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/"
         "studies/conscientia-additional-cases-v0.1")

PROBE = r'''
import json, copy, subprocess, sys
import campaign as c
cases = {x["id"]: x for x in json.load(open("CASES.json", encoding="utf-8"))["cases"]}
def run(cid, **upd):
    x = copy.deepcopy(cases[cid]); x.update(upd)
    try:
        r = c.result(x)
    except Exception as e:
        return type(e).__name__
    return [r["status"], r.get("bounds")]
C2 = "CLOSURE-02-CROSSES-THRESHOLD"
out = {
 "L_-0.4": run(C2, L=-0.4), "L_-5e-324": run(C2, L=-5e-324),
 "L_0.4": run(C2, L=0.4), "L_0": run(C2, L=0), "L_-0.0": run(C2, L=-0.0), "L_None": run(C2, L=None),
 "pub_01": run("CLOSURE-01-LOWER-BOUND-SUFFICES"), "pub_02": run(C2), "pub_03": run("CLOSURE-03-NO-REGULARITY"),
}
out["campaign"] = json.dumps(c.run_campaign(), sort_keys=True)
out["sensitivity"] = subprocess.run([sys.executable, "-B", "sensitivity.py"], capture_output=True, text=True).stdout
print(json.dumps(out, default=str))
'''


def probe(root):
    here = os.path.join(root, STUDY)
    r = subprocess.run([sys.executable, "-B", "-c", PROBE], cwd=here, capture_output=True, text=True,
                       check=True, env=dict(os.environ, PYTHONPATH=here))
    return json.loads(r.stdout)


p, c = probe(sys.argv[1]), probe(sys.argv[2])
ok = True


def check(label, cond):
    global ok
    ok &= bool(cond)
    print(f"{'OK ' if cond else 'BAD'} {label}")


keep = ("L_0.4", "L_0", "L_-0.0", "L_None", "pub_01", "pub_02", "pub_03")
for k in ("L_-0.4", "L_-5e-324") + keep:
    print(f"   {k:10s} #105={p[k]}  #106={c[k]}")
check("L-13 reproduced on #105 (L=-0.4 certifies)", p["L_-0.4"][0] == "PREDICATE_SUPPORTED_IN_FRAME")
check("#106 rejects both negative constants", c["L_-0.4"] == c["L_-5e-324"] == "ValueError")
check("L = 0.4, 0, -0.0, None and published cases unchanged", all(p[k] == c[k] for k in keep)
      and c["L_None"] == ["REGULARITY_NOT_ESTABLISHED", None])
check("full campaign (46 cases) identical", p["campaign"] == c["campaign"])
check("sensitivity sweep identical", p["sensitivity"] == c["sensitivity"] and len(c["sensitivity"]) > 0)
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
