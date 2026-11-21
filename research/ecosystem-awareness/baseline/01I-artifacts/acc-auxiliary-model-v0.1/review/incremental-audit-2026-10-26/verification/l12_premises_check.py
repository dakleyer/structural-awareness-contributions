"""Round 53: L-12 repair in PR #102 (child of #100).

Usage: python3 -B l12_premises_check.py <checkout of #100> <checkout of #102>

Real cases from CASES.json with one premise replaced by "UNKNOWN", run in
both trees (separate subprocesses):

  1. L-12: mission (MISSION-01 with both flags "UNKNOWN" and 3 independent
     sources), q_cost (QUAL-03 valid_Q="UNKNOWN"), knowledge (CAPACITY-01
     independent_evidence="UNKNOWN"). Expected: positive path on #100;
     MISSION_BASIS_NOT_ESTABLISHED, no SOURCE_B and EVIDENCE_INSUFFICIENT on
     #102, with the raw flag kept in the q_cost report.
  2. Known False stays False: MISSION-01 as published remains
     UNSUPPORTED_MISSION_CHANGE (mission_change=False) on both.
  3. Attribution (found by the author's file-wide review): ATTR-01 with the
     three fields "UNKNOWN" is CONSISTENT_IN_TOY on #100 and
     ATTRIBUTION_NOT_ESTABLISHED on #102, keeping the raw values.
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
U = "UNKNOWN"
def run(cid, **upd):
    x = copy.deepcopy(cases[cid]); x.update(upd)
    r = c.result(x)
    return {k: r.get(k) for k in ("status", "mission_change", "best_mode", "certificate_qualified",
                                   "listed", "verified", "credited", "social_fact_established") if k in r}
out = {
 "mission_unknown": run("MISSION-01-ONE-SOURCE-REPLICATED", authorized_change=U, source_basis_valid=U, actual_independent=3),
 "mission_false": run("MISSION-01-ONE-SOURCE-REPLICATED"),
 "q_cost_unknown": run("QUAL-03-Q-NOT-VALID", valid_Q=U),
 "knowledge_unknown": run("CAPACITY-01-ORANGE-COLLUSION-NOT-INFERRED", independent_evidence=U),
 "attribution_unknown": run("ATTR-01-LISTED-BUT-NO-DEPENDENCY", reported_dependency=U, verified_dependency=U, assigned_credit=U),
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


for k in ("mission_unknown", "mission_false", "q_cost_unknown", "knowledge_unknown", "attribution_unknown"):
    print(f"   {k:20s} #100={p[k]}\n   {'':20s} #102={c[k]}")
check("L-12 mission: authorized change on #100, basis not established on #102",
      p["mission_unknown"]["mission_change"] is True
      and c["mission_unknown"] == {"status": "MISSION_BASIS_NOT_ESTABLISHED", "mission_change": None})
check("known False kept: MISSION-01 unsupported on both",
      p["mission_false"] == c["mission_false"] and c["mission_false"]["mission_change"] is False)
check("L-12 q_cost: SOURCE_B on #100, not on #102; raw flag kept",
      p["q_cost_unknown"]["best_mode"] == "SOURCE_B" and c["q_cost_unknown"]["best_mode"] != "SOURCE_B"
      and c["q_cost_unknown"]["certificate_qualified"] == "UNKNOWN")
check("L-12 knowledge: validation path on #100, insufficient evidence on #102; no social fact on either",
      p["knowledge_unknown"]["status"] == "REQUIRES_INDEPENDENT_VALIDATION"
      and c["knowledge_unknown"]["status"] == "EVIDENCE_INSUFFICIENT_FOR_CLAIM"
      and p["knowledge_unknown"]["social_fact_established"] is False is c["knowledge_unknown"]["social_fact_established"])
check("attribution: CONSISTENT_IN_TOY on #100, ATTRIBUTION_NOT_ESTABLISHED on #102 with raw values",
      p["attribution_unknown"]["status"] == "CONSISTENT_IN_TOY"
      and c["attribution_unknown"]["status"] == "ATTRIBUTION_NOT_ESTABLISHED"
      and c["attribution_unknown"]["listed"] == "UNKNOWN")
check("full campaign (46 cases) identical", p["campaign"] == c["campaign"])
check("sensitivity sweep identical", p["sensitivity"] == c["sensitivity"] and len(c["sensitivity"]) > 0)
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
