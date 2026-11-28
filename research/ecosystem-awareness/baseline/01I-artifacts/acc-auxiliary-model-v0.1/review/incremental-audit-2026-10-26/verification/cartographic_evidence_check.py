"""Round 44: explicit evidence flags in the cartographic overlay (PR #94) and L-11.

Usage: python3 -B cartographic_evidence_check.py <checkout of #57> <checkout of #94>

Runs the same probes against residual_cartography_stage.py in both trees,
each tree in its own subprocess. Reference event: AG01, time 7, features
(.9, .85, .8, .95), source scope of the overlay. Reported per probe:
(candidate id, stage 3 output, transfer, "no matched event as of exchange").

  A. Defects fixed by #94 (expected: parent 11.5 with transfer 2, #94 not):
     captured_before_admission="UNKNOWN"; assumed_class_to_q_source_valid="UNKNOWN".
  B. Preservation: all 30 CASES x 4 Boolean (captured, link) combinations,
     full reports, and the complete main() report, equal in both trees
     (compared directly, not through the PR's digests).
  C. L-11 (audit's own probe, open on both trees): an arrival time of NaN or
     infinity passes the post-exchange arrival gate, enables the transfer
     and output 11.5, and is invisible to the prior-hit check.

Exit code 1 if A or B fail, or if C no longer reproduces (then L-11 needs
re-reading). Writes nothing.
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
def row(r):
    return [r["candidate_event_id"], r["stage_3"]["observed_by_referee_only"]["output"],
            r["stage_3"]["plan"]["transfer"], r["stage_2_source_cartography"]["no_matched_event_as_of_meta_exchange"]]
out = {}
for name, kw, link in (("valid", {}, True),
                       ("captured_UNKNOWN", {"captured_before_admission": "UNKNOWN"}, True),
                       ("link_UNKNOWN", {}, "UNKNOWN"),
                       ("time_NaN", {"time": float("nan")}, True),
                       ("time_inf", {"time": float("inf")}, True)):
    out[name] = row(s.three_stages(events=(ev(**kw),), assumed_class_to_q_source_valid=link))
cases = json.load(open("CASES.json", encoding="utf-8"))["cases"]
out["grid"] = json.dumps([s.three_stages(case_id=c["id"],
                          events=(replace(ev(captured_before_admission=cap), source_scope=c["public"]["scope"]),),
                          assumed_class_to_q_source_valid=lk)
                          for c in cases for cap, lk in product((False, True), repeat=2)], sort_keys=True)
out["grid_n"] = len(cases) * 4
out["main"] = json.dumps(s.main(), sort_keys=True)
print(json.dumps(out))
'''


def probe(root):
    here = os.path.join(root, STUDY)
    res = subprocess.run([sys.executable, "-B", "-c", PROBE], cwd=here, capture_output=True, text=True,
                         check=True, env=dict(os.environ, PYTHONPATH=here))
    return json.loads(res.stdout)


p, c = probe(sys.argv[1]), probe(sys.argv[2])
ok = True


def check(label, cond):
    global ok
    ok &= bool(cond)
    print(f"{'OK ' if cond else 'BAD'} {label}")


for name in ("valid", "captured_UNKNOWN", "link_UNKNOWN", "time_NaN", "time_inf"):
    print(f"   {name:17s} #57={p[name]}  #94={c[name]}")
check("valid event: 11.5 with transfer 2 on both", p["valid"] == c["valid"] == ["e", 11.5, 2, True])
check("captured='UNKNOWN': transfer on #57, no candidate and no transfer on #94",
      p["captured_UNKNOWN"][1:3] == [11.5, 2] and c["captured_UNKNOWN"][:3] == [None, 10, 0])
check("link='UNKNOWN': transfer on #57, candidate kept without transfer on #94",
      p["link_UNKNOWN"][1:3] == [11.5, 2] and c["link_UNKNOWN"][:3] == ["e", 10, 0])
check(f"{c['grid_n']} valid full reports identical", p["grid"] == c["grid"] and c["grid_n"] == 120)
check("complete main() report identical", p["main"] == c["main"])
check("L-11 reproduces on #94: NaN/inf arrival time enables transfer, no prior hit",
      c["time_NaN"] == ["e", 11.5, 2, True] and c["time_inf"] == ["e", 11.5, 2, True])
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
