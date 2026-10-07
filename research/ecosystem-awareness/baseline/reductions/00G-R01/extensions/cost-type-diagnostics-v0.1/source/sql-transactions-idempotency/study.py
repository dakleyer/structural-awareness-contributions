"""DDS actual SQLite transaction/resource-key pilot, scoped to local digital effects."""
import argparse,collections,hashlib,json,sqlite3,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def frozen():
    c=json.loads((HERE/"RUN_CARD.json").read_text(encoding="utf-8"));f=json.loads((HERE/"FREEZE.json").read_text())
    for n,h in f["files"].items():
        if sha(HERE/n)!=h:raise RuntimeError("freeze mismatch "+n)
    if sys.version.split()[0]!=c["technology"]["python"] or sqlite3.sqlite_version!=c["technology"]["sqlite"]:raise RuntimeError("runtime mismatch")
    return c
class DB:
    def __init__(self,path):
        self.path=path;self.c=sqlite3.connect(path);self.ops=0;self.trace=[]
        self.c.execute("pragma foreign_keys=on");self.c.execute("pragma journal_mode=DELETE")
        self.c.execute("create table grants(tenant text primary key,allowed integer)")
        self.c.execute("create table ledger(operation text primary key,payload text)")
        self.c.execute("create table receipt(operation text primary key,payload text)")
        self.c.execute("create table outbox(operation text primary key,published integer)")
        self.c.execute("insert into grants values('tenant-a',1)");self.c.commit()
    def q(self,sql,p=(),c=None):
        self.ops+=1;self.trace.append({"sql":sql,"connection":"primary" if c is None else "second"});return (c or self.c).execute(sql,p)
def operation(db,op,payload,rollback=False,outbox=False,c=None):
    c=c or db.c;db.q("begin immediate",c=c)
    g=db.q("select allowed from grants where tenant=?",("tenant-a",),c).fetchone()
    if not g or not g[0]:c.rollback();return "REFUSED"
    old=db.q("select payload from ledger where operation=?",(op,),c).fetchone()
    if old:
        c.rollback();return "RECOVERED" if old[0]==payload else "REFUSED_PAYLOAD_CONFLICT"
    db.q("insert into ledger values(?,?)",(op,payload),c)
    db.q("insert into receipt values(?,?)",(op,payload),c)
    if outbox:db.q("insert into outbox values(?,0)",(op,),c)
    if rollback:c.rollback();return "ABORTED"
    c.commit();return "COMMITTED"
def audit(path):
    c=sqlite3.connect(path)
    ledger=c.execute("select operation,payload from ledger").fetchall()
    receipt=c.execute("select operation,payload from receipt").fetchall()
    outbox=c.execute("select operation,published from outbox").fetchall();c.close()
    return {"ledger":ledger,"receipt":receipt,"outbox":outbox}
def main():
    a=argparse.ArgumentParser();a.add_argument("--output",required=True);args=a.parse_args();card=frozen();out=Path(args.output);out.mkdir(parents=True,exist_ok=False);results=[]
    for case in card["cases"]:
        path=out/(case["id"]+".sqlite");db=DB(path);kind=case["kind"];op="operation-a";payload="payload-a";history=[]
        if kind=="no-grant":db.q("update grants set allowed=0");db.c.commit()
        if kind=="stale-precheck":
            second=sqlite3.connect(path)
            history.append({"both_initial_absent":[db.q("select count(*) from ledger").fetchone()[0]==0,db.q("select count(*) from ledger",c=second).fetchone()[0]==0]})
            history.extend([operation(db,op,payload),operation(db,op,payload,c=second)]);second.close()
        elif kind=="payload-conflict":
            history.append(operation(db,op,payload));payload="payload-b";history.append(operation(db,op,payload))
        elif kind=="outside-domain":
            ext=sqlite3.connect(out/(case["id"]+"-external.sqlite"));ext.execute("create table effects(value text)");ext.execute("insert into effects values('committed-outside-primary')");ext.commit();ext.close()
            history.append(operation(db,op,payload,rollback=True))
        else:
            history.append(operation(db,op,payload,rollback=kind=="rollback",outbox=kind=="outbox-pending"))
            if kind=="duplicate":history.append(operation(db,op,payload))
            if kind=="lost-ack":
                db.c.close();db.c=sqlite3.connect(path);history.append(operation(db,op,payload))
        db.c.close();actual=audit(path)
        external=0
        if kind=="outside-domain":
            e=sqlite3.connect(out/(case["id"]+"-external.sqlite"));external=e.execute("select count(*) from effects").fetchone()[0];e.close()
        matching=(op,payload) in actual["receipt"] and (op,payload) in actual["ledger"]
        sufficient=matching and kind!="outbox-pending"
        outcome="P" if external and not actual["ledger"] else "I" if sufficient else "Ø"
        assert outcome==case["expected"],(case["id"],outcome);assert (len(actual["ledger"]),external)==(case["ledger"],case["external"])
        results.append({"id":case["id"],"narrative":case["narrative"],"outcome":outcome,"actual":actual,"external_local_database_effects":external,"current_requested_payload":payload,"matching_current_receipt":matching,"controller_history":history,"operational_sql_statements":db.ops,"trace":db.trace,"setup_sql_statements":7,"diagnostic":case.get("diagnostic"),"native_distributed_service_executed":False})
    x={"schema":"DDS-EXTENSION-RESULT-0.1","study":card["study"],"status":"PASS_REGISTERED_LOCAL_EXPECTATIONS","case_count":len(results),"assertions":2*len(results),"outcome_counts":dict(collections.Counter(r["outcome"] for r in results)),"results":results,"python":sys.version.split()[0],"sqlite":sqlite3.sqlite_version,"card_sha256":sha(HERE/"RUN_CARD.json"),"freeze_sha256":sha(HERE/"FREEZE.json"),"population_estimate":False,"independent_validation":False,"all_concurrency_interleavings_proved":False}
    with (out/"RESULTS.json").open("x",encoding="utf-8",newline="\n") as f:json.dump(x,f,ensure_ascii=False,indent=2);f.write("\n")
    print(json.dumps({k:x[k] for k in ["study","status","case_count","assertions","outcome_counts"]},ensure_ascii=True))
if __name__=="__main__":main()

