"""Own selected MCP-related JSON-RPC DDS pilot; no SDK, transport or external tool."""
import argparse,collections,hashlib,json,sqlite3,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def unique(items):
    d={}
    for k,v in items:
        if k in d:raise ValueError("duplicate member")
        d[k]=v
    return d
def frozen():
    c=json.loads((HERE/"RUN_CARD.json").read_text(encoding="utf-8"));f=json.loads((HERE/"FREEZE.json").read_text())
    for n,h in f["files"].items():
        if sha(HERE/n)!=h:raise RuntimeError("freeze mismatch "+n)
    if sys.version.split()[0]!=c["technology"]["python"] or sqlite3.sqlite_version!=c["technology"]["sqlite"]:raise RuntimeError("runtime mismatch")
    return c
class DB:
    def __init__(self,path):
        self.c=sqlite3.connect(path);self.work=0;self.trace=[]
        self.c.execute("create table grants(tenant text primary key,allowed integer)")
        self.c.execute("create table effects(operation text primary key,tenant text,tier text)")
        self.c.execute("insert into grants values('tenant-a',1)");self.c.commit()
    def q(self,sql,p=()):
        self.work+=1;self.trace.append({"sql":sql,"event":sql.split()[0]});return self.c.execute(sql,p)
def handle(wire,db,registry,before_use=None):
    try:
        r=json.loads(wire,object_pairs_hook=unique)
        if r.get("jsonrpc")!="2.0" or not isinstance(r.get("id"),(int,str)):return {"error":-32600}
        if r.get("method")!="tools/call":return {"error":-32601}
        p=r["params"];meta=p.get("_meta",{})
        if meta.get("io.modelcontextprotocol/protocolVersion")!="2026-07-28" or not isinstance(meta.get("io.modelcontextprotocol/clientCapabilities"),dict):return {"error":-32602}
        if p.get("name")!=registry["name"]:return {"error":-32602}
        a=p["arguments"]
        if set(a)!={"tenant","tier","operation","expected_revision"} or any(type(a[k]) is not str for k in ["tenant","tier","operation"]) or type(a["expected_revision"]) is not int:return {"error":-32602}
        if a["tier"]!="silver" or a["expected_revision"]!=registry["revision"]:return {"error":-32000,"reason":"local-contract"}
        allowed=db.q("select allowed from grants where tenant=?",(a["tenant"],)).fetchone()
        if not allowed or not allowed[0]:return {"error":-32000,"reason":"local-authority"}
        if before_use:before_use()
        db.q("begin immediate")
        current=db.q("select allowed from grants where tenant=?",(a["tenant"],)).fetchone()
        if not current or not current[0]:
            db.c.rollback();return {"error":-32000,"reason":"current-local-authority"}
        db.q("insert or ignore into effects values(?,?,?)",(a["operation"],a["tenant"],a["tier"]));db.c.commit()
        return {"jsonrpc":"2.0","id":r["id"],"result":{"content":[{"type":"text","text":"local effect admitted"}],"isError":False}}
    except (ValueError,KeyError,TypeError):return {"error":-32602}
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",required=True);args=ap.parse_args();card=frozen();out=Path(args.output);out.mkdir(parents=True,exist_ok=False)
    results=[]
    for case in card["cases"]:
        db=DB(out/(case["id"]+".sqlite"));kind=case["kind"];p=card["parameters"]
        meta={"io.modelcontextprotocol/protocolVersion":"2026-07-28","io.modelcontextprotocol/clientCapabilities":{},"io.modelcontextprotocol/clientInfo":{"name":"fixture","version":"0.1"}}
        if kind=="missing-meta":meta.pop("io.modelcontextprotocol/clientCapabilities")
        if kind=="self-reported-admin":
            meta["io.modelcontextprotocol/clientInfo"]["name"]="admin";db.c.execute("update grants set allowed=0");db.c.commit()
        a={"tenant":p["tenant"],"tier":p["tier"],"operation":"operation-a","expected_revision":1}
        if kind=="wrong-args":a["tenant"]=17
        request={"jsonrpc":"2.0","id":case["id"],"method":"tools/call" if kind!="unknown-method" else "tools/unsupported","params":{"name":p["tool"],"arguments":a,"_meta":meta}}
        registry={"name":p["tool"],"revision":2 if kind=="catalog-change" else 1,"annotations":{"readOnlyHint":kind=="misleading-annotation"}}
        def revoke():db.q("update grants set allowed=0");db.c.commit()
        wire=json.dumps(request,separators=(",",":"));responses=[]
        for _ in range(2 if kind=="duplicate" else 1):responses.append(handle(wire,db,registry,revoke if kind=="grant-change" else None))
        audit=sqlite3.connect(out/(case["id"]+".sqlite"));effects=audit.execute("select operation,tenant,tier from effects").fetchall();audit.close()
        allowed_contract=kind not in ["self-reported-admin","grant-change","catalog-change","wrong-args","unknown-method","missing-meta"]
        outcome="Ø" if not effects else "I" if len(effects)==1 and effects[0][1:]==("tenant-a","silver") and allowed_contract else "P"
        assert outcome==case["expected"],(case["id"],outcome);assert len(effects)==case["effects"]
        results.append({"id":case["id"],"narrative":case["narrative"],"outcome":outcome,"actual_local_effect_count":len(effects),"rpc_responses":responses,"request_bytes":len(wire.encode()),"operational_sql_statements":db.work,"trace":db.trace,"readOnly_hint":registry["annotations"]["readOnlyHint"],"annotation_enforced_as_authority":False,"native_transport_executed":False})
        db.c.close()
    x={"schema":"DDS-EXTENSION-RESULT-0.1","study":card["study"],"status":"PASS_REGISTERED_LOCAL_EXPECTATIONS","case_count":len(results),"assertions":2*len(results),"outcome_counts":dict(collections.Counter(r["outcome"] for r in results)),"results":results,"python":sys.version.split()[0],"sqlite":sqlite3.sqlite_version,"protocol_reference":"2026-07-28","card_sha256":sha(HERE/"RUN_CARD.json"),"freeze_sha256":sha(HERE/"FREEZE.json"),"population_estimate":False,"native_MCP_SDK_transport_or_full_conformance":False,"independent_validation":False}
    with (out/"RESULTS.json").open("x",encoding="utf-8",newline="\n") as f:json.dump(x,f,ensure_ascii=False,indent=2);f.write("\n")
    print(json.dumps({k:x[k] for k in ["study","status","case_count","assertions","outcome_counts"]},ensure_ascii=True))
if __name__=="__main__":main()

