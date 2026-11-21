"""Predeclared sensitivity grids for the Conscientia synthetic campaign."""
from __future__ import annotations
import json
from campaign import result

GRID={
 'network':[(top,n,g,alpha) for top in ('dense','star') for n in (5,10,20,40) for g in (.0,.2) for alpha in (0.,.1)],
 'qualification':[(b,t,v) for b in (0.,2.25,8.,15.) for t in (1.,3.,10.) for v in (0.,10.)],
 'credit':[(a,b) for a in (3,5,7,9) for b in (1,3,5,7)],
 'closure':[(L,T) for L in (None,.5,1.,3.) for T in (6.,8.,10.,12.)],
}
def run():
 out={'schema':'CONSCIENTIA-SENSITIVITY-v0.1','evidence':'SYNTHETIC_CONDITIONAL_NOT_EMPIRICAL','grids':{}}
 for family, vals in GRID.items():
  rs=[]
  for j,param in enumerate(vals):
   common={'id':f'SW-{family.upper()}-{j:03d}','source':'CE11','group':family}
   if family=='network':
    topology,n,g,alpha=param
    v=result({**common,'kind':'network','topology':topology,'n':n,'b':10,'g':g,'alpha':alpha})
   elif family=='qualification':
    cb,ct,val=param
    v=result({**common,'kind':'q_cost','decision_value':val,'qualified_cost':cb,'targeted_cost':ct,'full_cost':32,'valid_Q':True})
   elif family=='credit':
    a,b=param
    v=result({**common,'kind':'distribution','delta_utils':[1,1],'credit_minimums':[a,b],'credit_total':10})
   elif family=='closure':
    L,T=param
    v=result({**common,'kind':'closure','samples':[[0,9,10],[2,9,10]],'L':L,'x':1,'threshold':T})
   v['parameters']=param
   rs.append(v)
  out['grids'][family]=rs
 out['total_sweep_runs']=sum(map(len,out['grids'].values()))
 return out
if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True,ensure_ascii=False))
