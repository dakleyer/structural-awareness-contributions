"""Round 49: named source scopes in the cartographic overlay (PR #98, child of #96).

Usage: python3 -B scope_identity_check.py <checkout of #96> <checkout of #98>

Same probes in both trees, each in its own subprocess. Reference event:
time 7, features (.9, .85, .8, .95).

  1. qualified_event with event scope == required scope, both unnamed
     (None, "", "  ", True, 1) or unhashable ([]): #96 qualifies the joint
     region (or crashes on []); #98 returns INVALID_SOURCE_SCOPE.
  2. Named scopes: equal Unicode names qualify and a known mismatch stays
     SOURCE_OR_EVENT_MISMATCH, identically in both trees.
  3. Local information kept on #98: with scope None the four local claims
     are still CERTIFIED_OUTSIDE_LOCAL_A, and the geometry is 0.98125.
  4. three_stages with an unnamed event scope: no candidate on #96 (the
     fixture scope is named, so this path was already closed); ValueError
     on #98.
  5. The 120 valid full reports and main(), identical in both trees.

Exit code 1 on a mismatch. Writes nothing.
"""
import json
import os
import subprocess
import sys

STUDY = ("research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/"
         "studies/agentic-ecosystem-reduction-v0.1")

PROBE = r'''
import json
from dataclasses import replace
from itertools import product
import residual_cartography_stage as s
def ev(**k):
    d = dict(event_id="e", time=7, source_scope=s.CROSS_SOURCE_SCOPE, features=(.9, .85, .8, .95))
    d.update(k)
    return s.Observation(**d)
def q(scope, required):
    try:
        r = s.qualified_event(ev(source_scope=scope), required_scope=required)
        return r["reason"] if not r["joint_region"] else "JOINT"
    except Exception as e:
        return type(e).__name__
out = {"unnamed": {}, "named": {}}
for name, v in (("None", None), ("empty", ""), ("blank", "  "), ("True", True), ("1", 1), ("list", [])):
    out["unnamed"][name] = q(v, v)
out["named"]["same Unicode"] = q("ámbito-ñ", "ámbito-ñ")
out["named"]["mismatch"] = q("a", "b")
out["local_None"] = sorted({s.local_claim(ev(source_scope=None), i)["finding"] for i in range(4)})
out["geometry"] = s.geometric_referee_value((.9, .85, .8, .95))
try:
    r = s.three_stages(events=(ev(source_scope=None),))
    out["three_stages_None"] = [r["candidate_event_id"], r["stage_3"]["observed_by_referee_only"]["output"]]
except Exception as e:
    out["three_stages_None"] = type(e).__name__
cases = json.load(open("CASES.json", encoding="utf-8"))["cases"]
out["grid"] = json.dumps([s.three_stages(case_id=c["id"],
                          events=(replace(ev(captured_before_admission=cap), source_scope=c["public"]["scope"]),),
                          assumed_class_to_q_source_valid=lk)
                          for c in cases for cap, lk in product((False, True), repeat=2)], sort_keys=True)
out["main"] = json.dumps(s.main(), sort_keys=True)
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


for k in p["unnamed"]:
    print(f"   scope {k:6s} = required   #96={p['unnamed'][k]:22s} #98={c['unnamed'][k]}")
for k in p["named"]:
    print(f"   {k:21s}   #96={p['named'][k]:22s} #98={c['named'][k]}")
print(f"   three_stages scope None  #96={p['three_stages_None']}  #98={c['three_stages_None']}")
check("#96 qualifies a joint region for matching unnamed scopes",
      all(p["unnamed"][k] == "JOINT" for k in ("None", "empty", "blank", "True", "1")))
check("#98 returns INVALID_SOURCE_SCOPE for every unnamed or unhashable scope",
      all(v == "INVALID_SOURCE_SCOPE" for v in c["unnamed"].values()))
check("named scopes unchanged (same name qualifies, mismatch stays a mismatch)",
      p["named"] == c["named"] == {"same Unicode": "JOINT", "mismatch": "SOURCE_OR_EVENT_MISMATCH"})
check("local claims and geometry kept with unknown scope on #98",
      c["local_None"] == ["CERTIFIED_OUTSIDE_LOCAL_A"] and c["geometry"] == 0.98125)
check("three_stages: no candidate on #96, ValueError on #98",
      p["three_stages_None"] == [None, 10] and c["three_stages_None"] == "ValueError")
check("120 valid full reports identical", p["grid"] == c["grid"])
check("complete main() report identical", p["main"] == c["main"])
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
