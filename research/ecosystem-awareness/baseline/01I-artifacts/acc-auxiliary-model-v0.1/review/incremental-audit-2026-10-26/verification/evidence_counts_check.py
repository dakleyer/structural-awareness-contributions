"""Round 58: consumed evidence counts in mission and kl (PR #105, child of #104).

Usage: python3 -B evidence_counts_check.py <checkout of #104> <checkout of #105>

Real cases from CASES.json with one field replaced, both trees, separate
subprocesses. Reports (status, key field) or the exception raised.

  1. Fixed by #105 (classified on #104, ValueError on #105):
     MISSION-02 (both controls True) with actual_independent = inf or NaN;
     KL-01 with m = n = True, and with m = 2, n = True.
  2. Unchanged: MISSION-01 (controls False) with actual_independent = inf is
     still UNSUPPORTED (count not consumed); MISSION-03 (None) still
     MISSION_BASIS_NOT_ESTABLISHED; the published mission and KL cases.
  3. Full campaign (46 cases) and sensitivity sweep identical.
  4. L-13 (round 57) still reproduces on #105: closure with L = -0.4 is
     SUPPORTED_IN_FRAME (informative; #105 does not address it).

Exit code 1 if 1-3 fail. Writes nothing.
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
    return [r["status"], r.get("mission_change", r.get("coverage_delta_bits"))]
inf, nan = float("inf"), float("nan")
out = {
 "m02_inf": run("MISSION-02-AUTHORIZED-NEW-MISSION", actual_independent=inf),
 "m02_nan": run("MISSION-02-AUTHORIZED-NEW-MISSION", actual_independent=nan),
 "kl_true_true": run("KL-01-CORRECT-REVERSE", m=True, n=True),
 "kl_2_true": run("KL-01-CORRECT-REVERSE", m=2, n=True),
 "m01_inf_unused": run("MISSION-01-ONE-SOURCE-REPLICATED", actual_independent=inf),
 "m03_none": run("MISSION-03-UNQUALIFIED-UNKNOWN"),
 "m02": run("MISSION-02-AUTHORIZED-NEW-MISSION"),
 "kl01": run("KL-01-CORRECT-REVERSE"),
 "kl02": run("KL-02-NO-SUPPORT-MISMATCH"),
 "L13": run("CLOSURE-02-CROSSES-THRESHOLD", L=-0.4),
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


for k in ("m02_inf", "m02_nan", "kl_true_true", "kl_2_true", "m01_inf_unused", "m03_none", "m02", "kl01", "kl02", "L13"):
    print(f"   {k:15s} #104={p[k]}  #105={c[k]}")
fixed = ("m02_inf", "m02_nan", "kl_true_true", "kl_2_true")
check("#104 classifies all four (inf -> authorized change, NaN -> refusal, bool supports -> bits)",
      p["m02_inf"] == ["SUPPORTED_AND_AUTHORIZED_CHANGE", True] and p["m02_nan"][1] is False
      and isinstance(p["kl_true_true"], list) and isinstance(p["kl_2_true"], list))
check("#105 rejects all four with ValueError", all(c[k] == "ValueError" for k in fixed))
check("unused count, unknown basis and published cases unchanged",
      all(p[k] == c[k] for k in ("m01_inf_unused", "m03_none", "m02", "kl01", "kl02"))
      and c["m01_inf_unused"][1] is False and c["m03_none"][0] == "MISSION_BASIS_NOT_ESTABLISHED")
check("full campaign (46 cases) identical", p["campaign"] == c["campaign"])
check("sensitivity sweep identical", p["sensitivity"] == c["sensitivity"] and len(c["sensitivity"]) > 0)
print(f"INFO L-13 on #105: {c['L13']}")
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
