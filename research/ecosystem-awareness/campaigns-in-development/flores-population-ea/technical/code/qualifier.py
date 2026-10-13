#!/usr/bin/env python3
"""DDS-FLORES21 example of proof-dependency closure. NOT an EA implementation.
The receipts are synthetic. Authored-key truth is NOT implied by seal validity.
This can be implemented by a competent B2; no performance advantage is claimed.
"""
import argparse
import json
from pathlib import Path

STATES = {"SUPPORTED", "REFUTED", "NOT_ESTABLISHED"}

def check(spec):
    facts, claims, receipt_names = spec["facts"], spec["claims"], set(spec["receipts"])
    for k, value in facts.items():
        if value not in STATES:
            raise ValueError("Bad fact " + k)
    for name, node in claims.items():
        if not node.get("requires"):
            raise ValueError("Empty proof obligation " + name)
        for dep in node["requires"]:
            if dep not in facts and dep not in claims and dep not in receipt_names:
                raise ValueError("Undeclared dependency " + dep)
    for snap, row in spec["snapshots"].items():
        for k, value in row.items():
            if k not in receipt_names or value not in STATES:
                raise ValueError("Bad receipt " + snap + "." + k)

def evaluate(spec, snapshot):
    check(spec)
    states = dict(spec["facts"])
    states.update({k:"NOT_ESTABLISHED" for k in spec["receipts"]})
    states.update(spec["snapshots"][snapshot])
    memo, active = {}, set()
    def visit(key):
        if key in memo:
            return memo[key]
        if key in active:
            raise ValueError("Dependency cycle: " + key)
        active.add(key)
        pairs = [(dep, visit(dep)["status"] if dep in spec["claims"] else states[dep])
                 for dep in spec["claims"][key]["requires"]]
        # A failed proof obligation refutes this *qualified conjunction*.
        # It never refutes the independent key truth from a broken seal,
        # because key truth has a separate, independent proof obligation.
        state = ("REFUTED" if any(v=="REFUTED" for _,v in pairs)
                 else "NOT_ESTABLISHED" if any(v=="NOT_ESTABLISHED" for _,v in pairs)
                 else "SUPPORTED")
        value = {"status":state,
                 "process":spec["claims"][key]["process"],
                 "missing_or_refuted":[{"id":k,"status":v} for k,v in pairs
                                       if v!="SUPPORTED"]}
        active.remove(key)
        memo[key]=value
        return value
    return {key:visit(key) for key in spec["claims"]}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("data",type=Path)
    ap.add_argument("--snapshot",default="P2")
    args=ap.parse_args()
    spec=json.loads(args.data.read_text(encoding="utf-8"))
    print(json.dumps(evaluate(spec,args.snapshot),indent=2,sort_keys=True))

if __name__=="__main__":
    main()
