"""Round 41: dimensional identities in PR #92 (child of #76).

Usage: python3 -B dimensional_identity_check.py <checkout of #76> <checkout of #92>

Runs the same probes against `compare_dimensions` in both trees, each tree in
its own subprocess (reloading the module in one process mixes identities):

  1. int/str alias components {1: 3, "1": 3}: two keys that collapse to one
     after a JSON roundtrip of the report.
  2. a blank unit "   ".
  3. duplicate unknowns ("E", "E").
  4. a blank dimension name "   ".
  5. distinct literal strings [" actor ", "01", "1", "ñ"]: must be kept as
     they are, without normalization, and survive a JSON roundtrip.

Then compares the full H-01 report (`run_manifest` over
H01_STRATEGIC_STUDY.json) between both trees byte by byte.

Expected: on #76 probes 1-4 are accepted (the defect); on #92 they raise
ValueError; probe 5 is kept on both; the full report is identical.
Exit code 1 on a mismatch. Writes nothing.
"""
import json
import os
import subprocess
import sys

STUDY = ("research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/"
         "studies/bounded-traps-v0.1")

PROBE = r'''
import json, sys
from dimensional_contract import compare_dimensions as cd
import strategic_choice as sc
def run(before, after, dirs, unknown=()):
    try:
        r = cd(before, after, declared_directions=dirs, explicitly_unknown=unknown)
    except ValueError:
        return "REJECTED"
    return r["known_K_partial_order"]
def st(comp, unit="units", dim="R"):
    return {dim: {"unit": unit, "components": comp}}
out = {}
out["alias"] = run(st({1: "3", "1": "3"}), st({1: "4", "1": "2"}), {"R": "INCREASE"})
out["blank_unit"] = run(st({"a": "3"}, "   "), st({"a": "4"}, "   "), {"R": "INCREASE"})
out["dup_unknown"] = run(st({"a": "3"}), st({"a": "4"}), {"R": "INCREASE"}, ("E", "E"))
out["blank_dim"] = run(st({"a": "3"}, dim="   "), st({"a": "4"}, dim="   "), {"   ": "INCREASE"})
keys = [" actor ", "01", "1", "ñ"]
r = cd(st({k: "3" for k in keys}), st({k: "4" for k in keys}), declared_directions={"R": "INCREASE"})
ch = r["per_dimension"]["R"]["component_changes"]
out["distinct_kept"] = sorted(ch) == sorted(keys) and json.loads(json.dumps(r)) == r
m = json.load(open("H01_STRATEGIC_STUDY.json"))
out["report"] = json.dumps(sc.run_manifest(m), sort_keys=True, default=str)
print(json.dumps(out))
'''


def probe(root):
    here = os.path.join(root, STUDY)
    res = subprocess.run([sys.executable, "-B", "-c", PROBE], cwd=here,
                         capture_output=True, text=True, check=True)
    return json.loads(res.stdout)


parent, child = probe(sys.argv[1]), probe(sys.argv[2])
ok = True
for name in ("alias", "blank_unit", "dup_unknown", "blank_dim"):
    good = parent[name] != "REJECTED" and child[name] == "REJECTED"
    ok &= good
    print(f"{name:12s} parent={parent[name]:28s} #92={child[name]:10s} {'OK' if good else 'MISMATCH'}")
good = parent["distinct_kept"] and child["distinct_kept"]
ok &= good
print(f"distinct     parent={parent['distinct_kept']!s:28s} #92={child['distinct_kept']!s:10s} {'OK' if good else 'MISMATCH'}")
same = parent["report"] == child["report"]
ok &= same
print(f"full H-01 report identical ({len(child['report'])} bytes):", same)
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
