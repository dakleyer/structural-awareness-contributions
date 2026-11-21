"""Round 57: finite closure samples (PR #104, child of #103), and L-13.

Usage: python3 -B closure_samples_check.py <checkout of #103> <checkout of #104>

Real closure cases from CASES.json with one field replaced, both trees,
separate subprocesses. Reports (status, bounds) or the exception raised.

  1. Fixed by #104 (classified on #103, ValueError on #104): CLOSURE-01 with
     the first sample upper bound NaN; a sole sample [inf, inf]; a sole
     sample [-inf, -inf]; a sample position of 1e308 (projection overflow).
  2. Unchanged: the three published cases; CLOSURE-03 (L = None) with an
     unusable sample still returns REGULARITY_NOT_ESTABLISHED.
  3. L-13 (open on both trees): with CLOSURE-02's samples, L = 0.4 gives
     UNDETERMINED with bounds [8.6, 10.4]; the invalid L = -0.4 narrows the
     bounds to [9.4, 9.6], tighter than the samples themselves, and returns
     SUPPORTED_IN_FRAME. (L = -1 gives INCONSISTENT_ASSUMPTIONS instead.)
  4. Full campaign (46 cases) and sensitivity sweep identical.

Exit code 1 if 1, 2 or 4 fail, or if 3 no longer reproduces (then L-13
needs re-reading). Writes nothing.
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
inf, nan = float("inf"), float("nan")
out = {
 "upper_NaN": run("CLOSURE-01-LOWER-BOUND-SUFFICES", samples=[[0, 9, nan], [2, 9, 10]]),
 "sole_plus_inf": run("CLOSURE-01-LOWER-BOUND-SUFFICES", samples=[[0, inf, inf]]),
 "sole_minus_inf": run("CLOSURE-01-LOWER-BOUND-SUFFICES", samples=[[0, -inf, -inf]]),
 "position_overflow": run("CLOSURE-01-LOWER-BOUND-SUFFICES", samples=[[1e308, 9, 10], [2, 9, 10]], L=1e308),
 "pub_01": run("CLOSURE-01-LOWER-BOUND-SUFFICES"),
 "pub_02": run("CLOSURE-02-CROSSES-THRESHOLD"),
 "pub_03": run("CLOSURE-03-NO-REGULARITY"),
 "noL_bad_sample": run("CLOSURE-03-NO-REGULARITY", samples=[[0, nan, nan]]),
 "positive_L": run("CLOSURE-02-CROSSES-THRESHOLD", L=0.4),
 "negative_L": run("CLOSURE-02-CROSSES-THRESHOLD", L=-0.4),
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


for k in ("upper_NaN", "sole_plus_inf", "sole_minus_inf", "position_overflow", "pub_01", "pub_02", "pub_03",
          "noL_bad_sample", "positive_L", "negative_L"):
    print(f"   {k:18s} #103={p[k]}  #104={c[k]}")
fixed = ("upper_NaN", "sole_plus_inf", "sole_minus_inf", "position_overflow")
check("#103 classifies all four non-finite samples", all(isinstance(p[k], list) for k in fixed)
      and p["upper_NaN"][0] == "PREDICATE_SUPPORTED_IN_FRAME")
check("#104 rejects all four with ValueError", all(c[k] == "ValueError" for k in fixed))
check("published cases and L=None path unchanged",
      all(p[k] == c[k] for k in ("pub_01", "pub_02", "pub_03", "noL_bad_sample"))
      and c["noL_bad_sample"] == ["REGULARITY_NOT_ESTABLISHED", None])
check("L-13 reproduces on both: L=0.4 undetermined, L=-0.4 supported with bounds tighter than the samples",
      p["positive_L"] == c["positive_L"] and c["positive_L"][0] == "PREDICATE_UNDETERMINED"
      and p["negative_L"] == c["negative_L"] and c["negative_L"][0] == "PREDICATE_SUPPORTED_IN_FRAME")
check("full campaign (46 cases) identical", p["campaign"] == c["campaign"])
check("sensitivity sweep identical", p["sensitivity"] == c["sensitivity"] and len(c["sensitivity"]) > 0)
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
