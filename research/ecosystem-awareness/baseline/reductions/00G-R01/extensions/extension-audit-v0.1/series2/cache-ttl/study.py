from pathlib import Path
import sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/"_series2_support"))
from runner_support import DB,load,write
def lookup(db,tenant,key,now,fallback,before_use=None):
    grant=db.q("select allowed from grants where tenant=?",(tenant,)).fetchone()
    if not grant or not grant[0]:return {"kind":"UNRESOLVED","answer":None,"rows":[]}
    cached=db.q("select value,version,expires from cache where tenant=? and key=?",(tenant,key)).fetchone()
    source=db.q("select version,available from origin where tenant=? and key=?",(tenant,key)).fetchone()
    hit=bool(cached and cached[2]>now and source and source[1] and cached[1]==source[0])
    if not hit:
        fresh=db.q("select value,version from origin where tenant=? and key=? and available=1",(tenant,key)).fetchone()
        if not fresh:return {"kind":"DEFER" if fallback else "UNRESOLVED","answer":None,"rows":[],"cache_hit":False}
        value,version=fresh;db.q("insert or replace into cache values(?,?,?,?,?)",(tenant,key,value,version,now+1));db.c.commit()
    else:value,version=cached[:2]
    if before_use:before_use()
    current=db.q("select version,available from origin where tenant=? and key=?",(tenant,key)).fetchone()
    allowed=db.q("select allowed from grants where tenant=?",(tenant,)).fetchone()
    if not current or not current[1] or current[0]!=version or not allowed or not allowed[0]:return {"kind":"DEFER" if fallback else "UNRESOLVED","answer":None,"rows":[],"cache_hit":hit}
    return {"kind":"ANSWER","answer":value,"rows":[{"tenant":tenant,"version":version}],"cache_hit":hit}
def adjudicate(reply,world,tenant,fallback):
    if reply["kind"]=="ANSWER":
        if not world["allowed"] or reply["answer"]!=world["truth"] or any(r["tenant"]!=tenant or r["version"]!=world["version"] for r in reply["rows"]):return "P"
        return "I"
    return "M" if reply["kind"]=="DEFER" and fallback else "Ø"
def main():
    card,out=load(HERE);results=[]
    for c in card["cases"]:
        db=DB(out/(c["id"]+".sqlite"))
        db.q("create table cache(tenant text,key text,value integer,version integer,expires integer,primary key(tenant,key))")
        db.q("create table origin(tenant text,key text,value integer,version integer,available integer,primary key(tenant,key))")
        db.q("create table grants(tenant text primary key,allowed integer)")
        kind=c["kind"];value=9999 if kind=="false-source" else 1000;version=2 if kind=="source-new-generation" else 1;origin_value=2000 if version==2 else value
        db.q("insert into origin values(?,?,?,?,?)",("tenant-a","policy",origin_value,version,0 if kind in ["tenant-collision","offline-defer"] else 1))
        db.q("insert into grants values(?,?)",("tenant-a",0 if kind=="revoked" else 1))
        if kind!="miss":db.q("insert into cache values(?,?,?,?,?)",("tenant-b" if kind=="tenant-collision" else "tenant-a","policy",value,1,10 if kind in ["expired","offline-defer"] else 11))
        db.ready();world={"allowed":kind!="revoked","truth":2000 if version==2 else 1000,"version":version}
        def change():
            db.q("update origin set version=2,value=2000");db.c.commit();world.update(truth=2000,version=2)
        fallback=kind in ["offline-defer","change-at-use"]
        reply=lookup(db,"tenant-a","policy",10,fallback,change if kind=="change-at-use" else None)
        outcome=adjudicate(reply,world,"tenant-a",fallback)
        assert outcome==c["expected"],(c["id"],outcome);assert reply["answer"]==c["answer"]
        results.append({"id":c["id"],"story":c["story"],"outcome":outcome,"reply":reply,"sql_counts":db.counts(),"trace":db.trace,"diagnostic":c.get("diagnostic"),"private_truth_supplied_to_receiver":False});db.close()
    write(HERE,out,card,results,2*len(results))
if __name__=="__main__":main()

