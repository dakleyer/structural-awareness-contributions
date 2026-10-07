"""Own durable local workflow DDS pilot. Actual SQLite persistence; no Temporal product."""
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
    def __init__(self,path,idempotent=True,epoch=1):
        self.path=path;self.c=sqlite3.connect(path);self.work=0;self.trace=[]
        self.c.execute("create table workflow(status text,tick integer,attempts integer)")
        self.c.execute("insert into workflow values('RUNNING',0,0)")
        self.c.execute("create table grant_state(allowed integer,epoch integer)")
        self.c.execute("insert into grant_state values(1,?)",(epoch,))
        self.c.execute("create table effects(operation text"+(" primary key" if idempotent else "")+")");self.c.commit()
    def q(self,sql,p=()):
        self.work+=1;self.trace.append({"sql":sql});return self.c.execute(sql,p)
    def restart(self):
        self.c.close();self.c=sqlite3.connect(self.path);self.trace.append({"event":"CONNECTION_REOPENED"})
def run(db,params,source,policy):
    t=0;attempts=0;latency=source["latency"];status="RUNNING"
    while t<params["deadline_ticks"]:
        if t+latency>params["deadline_ticks"]:break
        t+=latency;attempts+=1
        db.q("update workflow set tick=?,attempts=?",(t,attempts));db.c.commit()
        ready=attempts>source["fail_attempts"]
        if ready:
            if source["revoke_before_effect"] and attempts==1:db.q("update grant_state set allowed=0");db.c.commit()
            current=db.q("select allowed,epoch from grant_state").fetchone()
            if not current[0] or current[1]!=params["worker_epoch"]:break
            db.q("insert "+("or ignore " if source["idempotent"] else "")+"into effects values(?)",(params["operation"],));db.c.commit()
            if source["lose_first_ack"] and attempts==1:
                db.trace.append({"event":"EFFECT_COMMITTED_ACK_LOST","tick":t});db.restart();continue
            status="DONE";db.q("update workflow set status=?,tick=?",(status,t));db.c.commit();break
        if policy=="bounded" and attempts>=params["bounded_attempts"]:
            if source["fallback_admitted"] and t+1<=params["deadline_ticks"]:
                t+=1;status="DEFERRED";db.q("update workflow set status=?,tick=?",(status,t));db.c.commit()
            break
    return {"attempts":attempts,"tick":t,"reported_status":status}
def inspect(path,params,fallback):
    c=sqlite3.connect(path);effects=c.execute("select operation from effects").fetchall();state=c.execute("select status,tick,attempts from workflow").fetchone();grant=c.execute("select allowed,epoch from grant_state").fetchone();c.close()
    count=len(effects)
    if count>1 or count and (not grant[0] or grant[1]!=params["worker_epoch"]):outcome="P"
    elif count==1 and state[0]=="DONE" and state[1]<=params["deadline_ticks"]:outcome="I"
    elif not count and state[0]=="DEFERRED" and fallback and state[1]<=params["deadline_ticks"]:outcome="M"
    else:outcome="Ø"
    return {"outcome":outcome,"actual_effects":count,"persisted_state":state,"current_resource_grant":grant}
def main():
    a=argparse.ArgumentParser();a.add_argument("--output",required=True);args=a.parse_args();card=frozen();out=Path(args.output);out.mkdir(parents=True,exist_ok=False);results=[];assertions=0
    for case in card["cases"]:
        kind=case["kind"];source={"latency":10 if kind=="too-late" else 1,"fail_attempts":999 if kind in ["bounded-defer","retry-to-horizon"] else 2 if kind=="transient" else 0,"idempotent":kind!="non-idempotent","lose_first_ack":kind in ["lost-ack","non-idempotent"],"revoke_before_effect":kind=="grant-revoked","fallback_admitted":case["fallback"]}
        db=DB(out/(case["id"]+".sqlite"),source["idempotent"],2 if kind=="stale-worker" else 1)
        observed=run(db,card["parameters"],source,"horizon" if kind in ["retry-to-horizon","transient"] else "bounded");db.c.close()
        actual=inspect(db.path,card["parameters"],case["fallback"])
        assert actual["outcome"]==case["expected"],(case["id"],actual);assert actual["actual_effects"]==case["effects"];assertions+=2
        reference=None
        if kind=="retry-to-horizon":
            ref=DB(out/(case["id"]+"-bounded-reference.sqlite"),True,1);run(ref,card["parameters"],dict(source),"bounded");ref.c.close();reference=inspect(ref.path,card["parameters"],case["fallback"])
            assert reference["outcome"]=="M";assert reference["actual_effects"]==0;assertions+=2
            reference["instrumented_execute_calls"]=ref.work;reference["trace"]=ref.trace
        results.append({"id":case["id"],"narrative":case["narrative"],**actual,"controller":observed,"operational_sql_statements":db.work,"trace":db.trace,"same_contract_bounded_M_witness":reference,"EA_Type1_operational_signature_established_in_this_case":bool(reference and actual["outcome"]=="Ø"),"diagnostic":case.get("diagnostic"),"logical_ticks_are_not_real_service_times":True})
    x={"schema":"DDS-EXTENSION-RESULT-0.1","study":card["study"],"status":"PASS_REGISTERED_LOCAL_EXPECTATIONS","case_count":len(results),"assertions":assertions,"outcome_counts":dict(collections.Counter(r["outcome"] for r in results)),"results":results,"python":sys.version.split()[0],"sqlite":sqlite3.sqlite_version,"card_sha256":sha(HERE/"RUN_CARD.json"),"freeze_sha256":sha(HERE/"FREEZE.json"),"population_estimate":False,"native_Temporal_or_real_human":False,"independent_validation":False}
    with (out/"RESULTS.json").open("x",encoding="utf-8",newline="\n") as f:json.dump(x,f,ensure_ascii=False,indent=2);f.write("\n")
    print(json.dumps({k:x[k] for k in ["study","status","case_count","assertions","outcome_counts"]},ensure_ascii=True))
if __name__=="__main__":main()

