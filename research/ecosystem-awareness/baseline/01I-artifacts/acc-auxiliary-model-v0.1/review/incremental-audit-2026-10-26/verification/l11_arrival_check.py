"""Round 46: L-11 repair in PR #96 (child of #94).

Usage: python3 -B l11_arrival_check.py <checkout of #94> <checkout of #96>

Same probes in both trees, each in its own subprocess. Reference event in
AG01: features (.9, .85, .8, .95), overlay scope. Each probe reports
(candidate id, stage 3 output, transfer) or the exception raised.

  1. L-11 inputs: arrival time NaN, inf, True, 7.0; event id 1 and "  ";
     a mixed history (valid event at 7 plus a NaN event).
     Expected: #94 yields a candidate and transfer for NaN/inf/7.0 and for
     the bad ids; #96 raises ValueError for every one of them.
  2. Unchanged integer behaviour: ticks 3 (prior, no candidate), 4, 7,
     -5 and 10**12, identical in both trees.
  3. Atemporal information kept: qualified_event on a NaN-time event is
     still a joint region on #96.
  4. The 120 valid full reports (30 cases x 4 Boolean combinations) and the
     complete main() report, identical in both trees.

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
def run(events):
    try:
        r = s.three_stages(events=events)
    except Exception as e:
        return type(e).__name__
    return [r["candidate_event_id"], r["stage_3"]["observed_by_referee_only"]["output"], r["stage_3"]["plan"]["transfer"]]
out = {"bad": {}, "ints": {}}
for name, events in (("time NaN", (ev(time=float("nan")),)), ("time inf", (ev(time=float("inf")),)),
                     ("time True", (ev(time=True),)), ("time 7.0", (ev(time=7.0),)),
                     ("id 1", (ev(event_id=1),)), ("id blank", (ev(event_id="  "),)),
                     ("mixed 7 + NaN", (ev(event_id="ok"), ev(event_id="n", time=float("nan"))))):
    out["bad"][name] = run(events)
for t in (3, 4, 7, -5, 10**12):
    out["ints"][str(t)] = run((ev(time=t),))
out["atemporal_nan"] = s.qualified_event(ev(time=float("nan")), required_scope=s.CROSS_SOURCE_SCOPE)["joint_region"]
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


for k in p["bad"]:
    print(f"   {k:15s} #94={p['bad'][k]!s:22s} #96={c['bad'][k]}")
check("L-11 reproduced on #94 (NaN, inf, 7.0, id 1, blank id, mixed history -> transfer)",
      all(p["bad"][k][2] == 2 for k in ("time NaN", "time inf", "time 7.0", "id 1", "id blank", "mixed 7 + NaN")))
check("#96 rejects every L-11 input with ValueError", all(v == "ValueError" for v in c["bad"].values()))
for k in p["ints"]:
    print(f"   tick {k:>13s} #94={p['ints'][k]!s:22s} #96={c['ints'][k]}")
check("integer ticks behave identically (3: no candidate; 4, 7, -5 handled as before; 10**12)",
      p["ints"] == c["ints"] and p["ints"]["3"][0] is None and p["ints"]["4"][2] == 2)
check("atemporal classification kept on #96 for unknown arrival", c["atemporal_nan"] is True)
check("120 valid full reports identical", p["grid"] == c["grid"])
check("complete main() report identical", p["main"] == c["main"])
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
