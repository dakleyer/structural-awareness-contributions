"""M28-02: adversarial sweep of guarded_verdict on PR #60 (round 15).

Usage: python3 -B m28_02_guard_sweep.py <studies/mathematical-lineage-social-agentic-v0.1 on PR #60>
27 inputs x valid/invalid proof x three proof scopes = 162 combinations.
Expected: 0 violations (verified on cb72bb65 and again on 8cd78d58). Writes nothing.
"""
import sys, itertools
sys.path.insert(0, sys.argv[1])
import test_theme18_online_context as t
bad=[]
cands=list(range(-3,15))+[True,False,2.0,9.0,1e9,-0.0,float('nan'),'2',None]
for x in cands:
    for valid,scope in itertools.product((True,False),(t.DOMAIN,tuple(range(6)),tuple(range(13)))):
        try:
            v,used=t.guarded_verdict(x,guard_validated=valid,proof_scope=scope); outcome=('OK',v,used)
        except (ValueError,TypeError) as e: outcome=('RAISE',type(e).__name__)
        inside = type(x) is int and 0<=x<=9
        if not inside and outcome[0]=='OK': bad.append((repr(x),valid,len(scope),outcome))
        if inside and (outcome[0]!='OK' or outcome[1]!=t.full_verdict(x)): bad.append((repr(x),valid,len(scope),outcome))
        if inside and outcome[0]=='OK' and outcome[2] and not (valid and scope==t.DOMAIN): bad.append(('shortcut without matching proof',repr(x),valid,len(scope)))
print('combinations:',len(cands)*6,'violations:',len(bad)); [print(' ',b) for b in bad[:5]]
