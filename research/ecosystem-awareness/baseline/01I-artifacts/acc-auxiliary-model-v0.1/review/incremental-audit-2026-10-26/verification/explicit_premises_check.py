"""Round 51: explicit premises in #54's additional cases (PR #100, child of #99), and L-12.

Usage: python3 -B explicit_premises_check.py <checkout of #99> <checkout of #100>

Takes real cases from CASES.json, replaces one Boolean premise with the
string "UNKNOWN" (or empties/breaks the gap support) and runs `result` in
both trees, each in its own subprocess.

  A. Fixed by #100 (expected: positive status on #99, not on #100):
     compare.authorized, eff_gap.feasible, eff_gap with empty periods,
     eff_gap with feasible=True but ideal cost above actual (gap None),
     human_time.same_service.
  B. Same class, NOT touched by #100 (L-12; expected identical, positive in
     both): mission.authorized_change / source_basis_valid = "UNKNOWN",
     q_cost.valid_Q = "UNKNOWN", knowledge.independent_evidence = "UNKNOWN".
  C. The full campaign (46 cases) and the sensitivity sweep, identical.

Exit code 1 if A or C fail, or if B no longer reproduces (then L-12 needs
re-reading). Writes nothing.
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
def mod(cid, fn):
    x = copy.deepcopy(cases[cid]); fn(x)
    try:
        r = c.result(x)
        return {k: r.get(k) for k in ("status", "mission_change", "best_mode", "certificate_qualified") if k in r}
    except Exception as e:
        return {"status": type(e).__name__}
U = "UNKNOWN"
def set_(path, v):
    def f(x):
        o = x
        for p in path[:-1]: o = o[p]
        o[path[-1]] = v
    return f
out = {
 "compare.authorized": mod("BAN-03-LEGITIMATE-DONATION", set_(["alternative", "authorized"], U)),
 "eff_gap.feasible": mod("EFF-02-UNATTAINABLE-IDEAL", set_(["periods", 0, "feasible"], U)),
 "eff_gap.empty": mod("EFF-02-UNATTAINABLE-IDEAL", set_(["periods"], [])),
 "eff_gap.gap_None": mod("EFF-02-UNATTAINABLE-IDEAL", lambda x: x["periods"][0].update(feasible=True, ideal_same_output_cost=200)),
 "human_time.same_service": mod("HID-02-NO-SAME-SERVICE", set_(["same_service"], U)),
 "mission.flags": mod("MISSION-01-ONE-SOURCE-REPLICATED", lambda x: x.update(authorized_change=U, source_basis_valid=U, actual_independent=3)),
 "q_cost.valid_Q": mod("QUAL-03-Q-NOT-VALID", set_(["valid_Q"], U)),
 "knowledge.evidence": mod("CAPACITY-01-ORANGE-COLLUSION-NOT-INFERRED", set_(["independent_evidence"], U)),
}
out["campaign"] = json.dumps(c.run_campaign(), sort_keys=True)
out["sensitivity"] = subprocess.run([sys.executable, "-B", "sensitivity.py"], capture_output=True, text=True).stdout
print(json.dumps(out))
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


fixed = ("compare.authorized", "eff_gap.feasible", "eff_gap.empty", "eff_gap.gap_None", "human_time.same_service")
open_ = ("mission.flags", "q_cost.valid_Q", "knowledge.evidence")
for k in fixed + open_:
    print(f"   {k:24s} #99={p[k]}\n   {'':24s} #100={c[k]}")
check("A: #99 gives the positive status for the five fixed premises",
      p["compare.authorized"]["status"] == "WEAK_PARETO_RESOURCE_SERVICE_GAIN"
      and all(p[k]["status"] == "GAPS_ESTABLISHED_IN_TOY" for k in ("eff_gap.feasible", "eff_gap.empty", "eff_gap.gap_None"))
      and p["human_time.same_service"]["status"] == "HUMAN_INPUT_DIFF_NOT_OBSERVED_HID")
check("A: #100 withholds all five",
      c["compare.authorized"]["status"] == "RIGHTS_BLOCKED"
      and all(c[k]["status"] == "OPTIMUM_NOT_ESTABLISHED" for k in ("eff_gap.feasible", "eff_gap.empty", "eff_gap.gap_None"))
      and c["human_time.same_service"]["status"] == "MATCHED_REFERENCE_MISSING")
check("B (L-12): 'UNKNOWN' still enables mission change, Source-B and the validation path on both trees",
      p["mission.flags"] == c["mission.flags"] and c["mission.flags"]["mission_change"] is True
      and p["q_cost.valid_Q"] == c["q_cost.valid_Q"] and c["q_cost.valid_Q"]["best_mode"] == "SOURCE_B"
      and p["knowledge.evidence"] == c["knowledge.evidence"]
      and c["knowledge.evidence"]["status"] == "REQUIRES_INDEPENDENT_VALIDATION")
check("C: full campaign (46 cases) identical", p["campaign"] == c["campaign"])
check("C: sensitivity sweep output identical", p["sensitivity"] == c["sensitivity"] and len(c["sensitivity"]) > 0)
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
