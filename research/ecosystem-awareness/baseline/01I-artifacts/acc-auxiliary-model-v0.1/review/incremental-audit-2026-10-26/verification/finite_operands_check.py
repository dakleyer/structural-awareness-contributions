"""Round 56: finite consumed operands in q_cost and distribution (PR #103, child of #102).

Usage: python3 -B finite_operands_check.py <checkout of #102> <checkout of #103>

Real cases from CASES.json with one operand replaced, run in both trees
(separate subprocesses). Each probe reports the status/best mode/Pareto flag
or the exception raised.

  1. Defects (expected: a classification on #102, ValueError on #103):
     QUAL-02 targeted_cost = NaN; ROBIN-01 delta_utils = [1, inf];
     QUAL-01 decision_value = 1e308 with full_cost = -1e308 (overflow);
     ROBIN-03 credit_minimums = [1e308, 1e308] (credit demand overflow).
  2. Not consumed, so kept: QUAL-03 (valid_Q False) with qualified_cost NaN
     still compares the known modes, identically in both trees.
  3. Finite negatives and zero unchanged: QUAL-02 targeted_cost = -3 and 0;
     ROBIN-01 delta_utils = [-1, 0].
  4. Full campaign (46 cases) and sensitivity sweep identical.

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
    return {k: r.get(k) for k in ("status", "best_mode", "absolute_pareto", "net_values") if k in r}
inf, nan = float("inf"), float("nan")
out = {
 "targeted_NaN": run("QUAL-02-CONVENTIONAL-BEATS-B", targeted_cost=nan),
 "delta_inf": run("ROBIN-01-SMALL-GAIN-LARGE-SHARE", delta_utils=[1, inf]),
 "mode_overflow": run("QUAL-01-B-SOURCE-BEATS-FULL", decision_value=1e308, full_cost=-1e308),
 "demand_overflow": run("ROBIN-03-CREDIT-FEASIBLE", credit_minimums=[1e308, 1e308]),
 "inactive_Q_NaN": run("QUAL-03-Q-NOT-VALID", qualified_cost=nan),
 "targeted_neg": run("QUAL-02-CONVENTIONAL-BEATS-B", targeted_cost=-3),
 "targeted_zero": run("QUAL-02-CONVENTIONAL-BEATS-B", targeted_cost=0),
 "delta_neg_zero": run("ROBIN-01-SMALL-GAIN-LARGE-SHARE", delta_utils=[-1, 0]),
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


def short(v):
    return v if isinstance(v, str) else {k: v[k] for k in v if k != "net_values"}


for k in ("targeted_NaN", "delta_inf", "mode_overflow", "demand_overflow", "inactive_Q_NaN",
          "targeted_neg", "targeted_zero", "delta_neg_zero"):
    print(f"   {k:16s} #102={short(p[k])}  #103={short(c[k])}")
defects = ("targeted_NaN", "delta_inf", "mode_overflow", "demand_overflow")
check("#102 classifies all four non-finite inputs", all(isinstance(p[k], dict) for k in defects)
      and p["targeted_NaN"]["best_mode"] == "SOURCE_B" and p["delta_inf"]["absolute_pareto"] is True)
check("#103 rejects all four with ValueError", all(c[k] == "ValueError" for k in defects))
check("inactive Q with NaN cost: known modes still compared, identical", p["inactive_Q_NaN"] == c["inactive_Q_NaN"]
      and isinstance(c["inactive_Q_NaN"], dict) and c["inactive_Q_NaN"]["net_values"]["SOURCE_B"] is None)
check("finite negatives and zero unchanged",
      all(p[k] == c[k] and isinstance(c[k], dict) for k in ("targeted_neg", "targeted_zero", "delta_neg_zero")))
check("full campaign (46 cases) identical", p["campaign"] == c["campaign"])
check("sensitivity sweep identical", p["sensitivity"] == c["sensitivity"] and len(c["sensitivity"]) > 0)
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
