"""Meaningful authored successor checks; no scientific independent adjudication.
Distinct external oracle truths stay outside the entire candidate input.
"""
import copy
import hashlib
import itertools
import json
from pathlib import Path
from qualifier import evaluate as legacy
from qualifier_v0_2 import check,evaluate,load,strict_json

ROOT=Path(__file__).parent
SPEC=load(ROOT/"mock_receipts.json")
def sha(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
checks=[]
def require(name,value):
    assert value,name
    checks.append(name)
def reject(name,callback):
    try:
        callback()
    except ValueError:
        checks.append(name)
    else:
        raise AssertionError(name)

# True and false key truth are different world facts, not copied input labels.
packet=copy.deepcopy(SPEC)
worlds=[{"candidate_packet":copy.deepcopy(packet),"oracle_only":{"key_objectively_true":True}},
        {"candidate_packet":copy.deepcopy(packet),"oracle_only":{"key_objectively_true":False}}]
require("Different external truth",worlds[0]["oracle_only"]!=worlds[1]["oracle_only"])
require("Different complete world digest",sha(worlds[0])!=sha(worlds[1]))
require("Identical entire candidate packet",sha(worlds[0]["candidate_packet"])==sha(worlds[1]["candidate_packet"]))
outputs=[evaluate(w["candidate_packet"],"P1") for w in worlds]
require("Identical outputs from equal complete observations",outputs[0]==outputs[1])
require("Neither identifies hidden key truth",all(o["Q_KEY_OBJECTIVELY_TRUE"]["status"]=="NOT_ESTABLISHED" for o in outputs))
positive=copy.deepcopy(packet);positive["facts"]["independent_key_truth"]="SUPPORTED"
negative=copy.deepcopy(packet);negative["facts"]["independent_key_truth"]="REFUTED"
require("Observed positive truth differs and supports",sha(positive)!=sha(packet) and evaluate(positive,"P1")["Q_KEY_OBJECTIVELY_TRUE"]["status"]=="SUPPORTED")
require("Observed refutation differs and refutes",sha(negative)!=sha(packet) and evaluate(negative,"P1")["Q_KEY_OBJECTIVELY_TRUE"]["status"]=="REFUTED")
require("Bad seal never independently refutes key truth",evaluate(packet,"P1_seal_refuted")["Q_KEY_OBJECTIVELY_TRUE"]["status"]=="NOT_ESTABLISHED")
require("All legacy snapshot semantics conserved",all(evaluate(SPEC,name)==legacy(SPEC,name) for name in SPEC["snapshots"]))
reject("Duplicate JSON keys rejected",lambda:strict_json('{"same":1,"same":2}'))
ambiguous=copy.deepcopy(packet);ambiguous["receipts"]["method_frozen"]="collision"
reject("Fact/receipt collision rejected",lambda:check(ambiguous))
collision=copy.deepcopy(packet);collision["facts"]["Q_METHOD"]="SUPPORTED"
reject("Fact/claim collision rejected",lambda:check(collision))
cycle=copy.deepcopy(packet);cycle["claims"]["Q_METHOD"]["requires"].append("Q_METHOD")
reject("Dependency cycle rejected before evaluation",lambda:check(cycle))
dup=copy.deepcopy(packet);dup["claims"]["Q_METHOD"]["requires"].append("method_frozen")
reject("Duplicate dependency rejected",lambda:check(dup))
missing=copy.deepcopy(packet);missing["claims"]["Q_METHOD"]["requires"].append("undeclared")
reject("Undeclared dependency rejected",lambda:check(missing))
reject("Unknown snapshot rejected",lambda:evaluate(packet,"missing"))
bad=copy.deepcopy(packet);bad["snapshots"]["P1"]["seal_join"]="APPROVED"
reject("Unknown evidence state rejected",lambda:check(bad))
blank=copy.deepcopy(packet);blank["claims"]["Q_METHOD"]["process"]=""
reject("Unnamed process rejected",lambda:check(blank))

# Independent three-state conjunction truth table; 27 bounded instrument cases.
truth_table=[]
for values in itertools.product(("SUPPORTED","REFUTED","NOT_ESTABLISHED"),repeat=3):
    spec={"facts":dict(zip(("a","b","c"),values)),"receipts":{},"claims":{"Q":{"process":"bounded conjunction","requires":["a","b","c"]}},"snapshots":{"s":{}}}
    expected={frozenset({"SUPPORTED"}):"SUPPORTED"}.get(frozenset(values),"REFUTED" if "REFUTED" in values else "NOT_ESTABLISHED")
    actual=evaluate(spec,"s")["Q"]["status"]
    assert actual==expected,(values,actual,expected)
    truth_table.append({"inputs":values,"expected":expected,"actual":actual})
result={"schema":"FLORES_AUTHORED_QUALIFIER_SUCCESSOR_CHECKS_0.2","result":"PASS_AUTHORED_CONTRACT_CHECKS","native_run":False,"EA_implementation":False,"independent_scientific_adjudication":False,"named_controls":len(checks),"conjunction_cases":len(truth_table),"checks":checks,"world_truths":[w["oracle_only"] for w in worlds],"world_sha256":[sha(w) for w in worlds],"candidate_packet_sha256":sha(packet),"outputs_sha256":[sha(o) for o in outputs],"legacy_source_rewritten":False,"truth_table":truth_table}
out=ROOT.parent/"QUALIFIER_SUCCESSOR_RESULTS_2026-10-14.json"
out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps({"result":result["result"],"namedControls":len(checks),"boundedConjunctionCases":len(truth_table),"differentHiddenTruths":True,"sameCompleteCandidateInput":True,"nativeRun":False}))
