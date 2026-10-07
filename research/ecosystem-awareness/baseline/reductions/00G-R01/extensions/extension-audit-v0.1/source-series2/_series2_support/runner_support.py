"""Shared instrumentation for scoped Simplified DDS Gate-A specification pilots."""
import argparse,hashlib,json,sqlite3,sys,collections,platform
from pathlib import Path
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(here):
    card=json.loads((here/"RUN_CARD.json").read_text(encoding="utf-8"));freeze=json.loads((here/"FREEZE.json").read_text())
    for n,h in freeze["files"].items():
        if sha(here/n)!=h:raise RuntimeError("Frozen byte mismatch: "+n)
    if sys.version.split()[0]!=card["runtime"]["python"] or sqlite3.sqlite_version!=card["runtime"]["sqlite"]:raise RuntimeError("Runtime mismatch")
    p=argparse.ArgumentParser();p.add_argument("--output",required=True);a=p.parse_args();out=Path(a.output);out.mkdir(parents=True,exist_ok=False)
    return card,out
class DB:
    def __init__(self,path):
        self.path=path;self.c=sqlite3.connect(path);self.phase="setup";self.trace=[];self.c.set_trace_callback(lambda sql:self.trace.append({"phase":self.phase,"sql":sql}))
    def q(self,sql,p=()):return self.c.execute(sql,p)
    def ready(self):self.c.commit();self.phase="operation"
    def close(self):self.c.close()
    def counts(self):return {phase:sum(x["phase"]==phase for x in self.trace) for phase in ["setup","operation"]}
def write(here,out,card,results,checks,extra=None):
    x={"schema":"SIMPLIFIED-DDS-GATE-A-RESULT-0.1","study":card["study"],"DDS_gate":"A","profile_kind":"Simplified","object_under_test":"candidate mechanism/specification profile","status":"PASS_PREREGISTERED_SPECIFICATION_PILOT_EXPECTATIONS","cases":len(results),"assertions":checks,"outcomes":dict(collections.Counter(r["outcome"] for r in results)),"results":results,"python":sys.version.split()[0],"sqlite":sqlite3.sqlite_version,"platform":platform.system(),"card_sha256":sha(here/"RUN_CARD.json"),"freeze_sha256":sha(here/"FREEZE.json"),"Gate_B_architecture_verified":False,"Gate_C_implementation_validated":False,"native_named_product_execution":False,"population_estimate":False,"blind_search_experiment":False,"independent_validation":False}
    if extra:x.update(extra)
    with (out/"RESULTS.json").open("x",encoding="utf-8",newline="\n") as f:json.dump(x,f,ensure_ascii=False,indent=2);f.write("\n")
    print(json.dumps({k:x[k] for k in ["study","DDS_gate","status","cases","assertions","outcomes"]},ensure_ascii=True))

