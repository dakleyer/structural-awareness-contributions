"""Author-side proof-contract checker successor. Not an EA implementation/native run.
Legacy qualifier.py and its results remain unchanged. Receipt trust is stipulated.
"""
import json
from pathlib import Path

STATES={"SUPPORTED","REFUTED","NOT_ESTABLISHED"}

def strict_json(text):
    def object_pairs(pairs):
        result={}
        for key,value in pairs:
            if key in result:
                raise ValueError("Duplicate JSON key: "+key)
            result[key]=value
        return result
    return json.loads(text,object_pairs_hook=object_pairs)

def check(spec):
    if not isinstance(spec,dict):
        raise ValueError("Spec must be an object")
    for key in ("facts","claims","receipts","snapshots"):
        if not isinstance(spec.get(key),dict):
            raise ValueError("Missing object: "+key)
    facts,claims,receipts=spec["facts"],spec["claims"],spec["receipts"]
    names=[set(facts),set(claims),set(receipts)]
    if any(names[i]&names[j] for i in range(3) for j in range(i+1,3)):
        raise ValueError("Ambiguous dependency namespace")
    for name,state in facts.items():
        if not isinstance(state,str) or state not in STATES:
            raise ValueError("Bad fact: "+name)
    for name,node in claims.items():
        if not isinstance(node,dict) or not isinstance(node.get("process"),str) or not node["process"]:
            raise ValueError("Missing process: "+name)
        deps=node.get("requires")
        if not isinstance(deps,list) or not deps or not all(isinstance(d,str) for d in deps):
            raise ValueError("Bad proof obligations: "+name)
        if len(set(deps))!=len(deps):
            raise ValueError("Duplicate dependency: "+name)
        for dep in deps:
            if dep not in facts and dep not in claims and dep not in receipts:
                raise ValueError("Undeclared dependency: "+dep)
    active,done=set(),set()
    def visit(name):
        if name in active:
            raise ValueError("Dependency cycle: "+name)
        if name in done:
            return
        active.add(name)
        for dep in claims[name]["requires"]:
            if dep in claims:
                visit(dep)
        active.remove(name)
        done.add(name)
    for name in claims:
        visit(name)
    for name,row in spec["snapshots"].items():
        if not isinstance(row,dict):
            raise ValueError("Bad snapshot: "+name)
        for key,state in row.items():
            if key not in receipts or not isinstance(state,str) or state not in STATES:
                raise ValueError("Bad receipt: "+name+"."+key)
    return True

def evaluate(spec,snapshot):
    check(spec)
    if snapshot not in spec["snapshots"]:
        raise ValueError("Unknown snapshot: "+str(snapshot))
    states={**spec["facts"],**{key:"NOT_ESTABLISHED" for key in spec["receipts"]},**spec["snapshots"][snapshot]}
    memo={}
    def visit(key):
        if key in memo:
            return memo[key]
        pairs=[(dep,visit(dep)["status"] if dep in spec["claims"] else states[dep]) for dep in spec["claims"][key]["requires"]]
        state="REFUTED" if any(value=="REFUTED" for _,value in pairs) else "NOT_ESTABLISHED" if any(value=="NOT_ESTABLISHED" for _,value in pairs) else "SUPPORTED"
        memo[key]={"status":state,"process":spec["claims"][key]["process"],"missing_or_refuted":[{"id":dep,"status":value} for dep,value in pairs if value!="SUPPORTED"]}
        return memo[key]
    return {key:visit(key) for key in spec["claims"]}

def load(path):
    return strict_json(Path(path).read_text(encoding="utf-8"))
