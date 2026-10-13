#!/usr/bin/env python3
"""Authored reference-checker tests; NOT a Flores run or an EA/B2 differential."""
import copy
import json
from pathlib import Path
from qualifier import check, evaluate

SPEC=json.loads((Path(__file__).parent/"mock_receipts.json").read_text(encoding="utf-8"))
check(SPEC)
R={name:evaluate(SPEC,name) for name in SPEC["snapshots"]}
V=lambda snap,claim:R[snap][claim]["status"]
checks=[
 ("P0 method",V("P0","Q_METHOD")=="SUPPORTED"),
 ("P0 relative key unknown",V("P0","Q_KEY_RELATIVE_COMPARABILITY")=="NOT_ESTABLISHED"),
 ("P1 relative comparison supported",V("P1","Q_KEY_RELATIVE_COMPARABILITY")=="SUPPORTED"),
 ("P2 reference lost",V("P2","Q_KEY_RELATIVE_COMPARABILITY")=="NOT_ESTABLISHED"),
 ("P2 profile lost",V("P2_profile","Q_KEY_RELATIVE_COMPARABILITY")=="NOT_ESTABLISHED"),
 ("P2 scope lost",V("P2_scope","Q_KEY_RELATIVE_COMPARABILITY")=="NOT_ESTABLISHED"),
 ("P3 recovery",V("P3","Q_KEY_RELATIVE_COMPARABILITY")=="SUPPORTED"),
 ("P2 method intact",V("P2","Q_METHOD")=="SUPPORTED"),
 ("P2 flags intact",V("P2","Q_BLIND_RECEIPT")=="SUPPORTED"),
 ("P1 key truth unknown",V("P1","Q_KEY_OBJECTIVELY_TRUE")=="NOT_ESTABLISHED"),
 ("bad seal not key false",V("P1_seal_refuted","Q_KEY_OBJECTIVELY_TRUE")=="NOT_ESTABLISHED"),
 ("bad seal refutes comparison",V("P1_seal_refuted","Q_KEY_RELATIVE_COMPARABILITY")=="REFUTED"),
 ("ninth content not covered",V("P2","Q_ALL_NINE_COVERED")=="REFUTED"),
 ("record09 not admitted",V("P2","Q_RECORD09_ADMITTED")=="REFUTED"),
 ("shared limit retained",V("P2","Q_SHARED_LIMIT_DOCUMENTED")=="SUPPORTED"),
 ("failure-mode independence unknown",V("P2","Q_FAILURE_MODE_INDEPENDENCE_PROVED")=="NOT_ESTABLISHED"),
 ("benign field no alarm",R["P1"]==R["P1_benign"])
]
for field in ("receiver_role_scope","receiver_reference","receiver_profile"):
    modified=copy.deepcopy(SPEC)
    modified["snapshots"]["P1"].pop(field)
    r=evaluate(modified,"P1")
    checks.append(("withhold "+field,r["Q_KEY_RELATIVE_COMPARABILITY"]["status"]=="NOT_ESTABLISHED" and r["Q_METHOD"]["status"]=="SUPPORTED"))
x=copy.deepcopy(SPEC)
x["facts"]["independent_key_truth"]="NOT_ESTABLISHED"
checks.append(("indistinguishable observation",evaluate(x,"P1")==evaluate(SPEC,"P1")))
assert all(ok for _,ok in checks),[(name,ok) for name,ok in checks if not ok]
print("PASS",len(checks),"authored consistency checks — no EA/Flores-native pass")
