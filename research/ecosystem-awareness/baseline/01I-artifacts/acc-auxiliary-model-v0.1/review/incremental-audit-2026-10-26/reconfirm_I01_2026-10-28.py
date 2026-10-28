"""Auditor reconfirmation of I-01 / M27-01 / M28-01 on main 51fc686 (PR #64 merged).

Usage: python -B reconfirm_I01_2026-10-28.py <path to studies/scoped-closure-metacognition-v0.1>

Imports the audited qualify() from the given path, replays the published
adversaries and a positive control, then fuzzes 20 000 exact-coordinate cases
against an exact rational (Fraction) oracle: pairwise Lipschitz feasibility
(necessary and sufficient for exact coordinates) and the tight envelope.
Reports unsound TRUE/FALSE certificates and lost decisive answers.
Synthetic finite checks only; no empirical claim. Writes nothing.
"""
import sys, random
from fractions import Fraction as Fr
sys.path.insert(0, sys.argv[1])
from metacognition import Point, Frame, DecisionQuestion, qualify
def P(c,xl,xh,yl,yh): return Point(claim_id=c,origin_id=c,scope="x",revision="v1",observed_at=4,x_min=xl,x_max=xh,y_min=yl,y_max=yh,source_attested=True)
def Fm(L,dmax=2): return Frame(scope="x",revision="v1",now=5,max_age=5,domain_min=0,domain_max=dmax,lipschitz=L,regularity_qualified=True)
st=lambda r:r["local_answer_status"]
print("I-01 [1e-13]&[0], L=0, thr 5e-14:", st(qualify(Fm(0.0),DecisionQuestion(x=0,threshold=5e-14),(P("a",0,0,1e-13,1e-13),P("b",0,0,0,0)))))
print("M27-01 f(0)=0&f(0)=2, L=1, f(1)>=1:", st(qualify(Fm(1.0),DecisionQuestion(x=1,threshold=1),(P("a",0,0,0,0),P("b",0,0,2,2)))))
print("positive control f(0)=1,f(1)=2,L=1,x=.5,thr 1.25:", st(qualify(Fm(1.0),DecisionQuestion(x=0.5,threshold=1.25),(P("a",0,0,1,1),P("b",1,1,2,2)))))
# Soundness fuzz with exact rationals: TRUE => every compatible f has f(x)>=thr; FALSE => every compatible f(x)<thr
def exact(pts,L,x):
    Lq=Fr(L); P_=[(Fr(a),Fr(l),Fr(u)) for a,l,u in pts]
    for i,(xi,li,ui) in enumerate(P_):
        for xj,lj,uj in P_[i+1:]:
            if li-uj>Lq*abs(xi-xj) or lj-ui>Lq*abs(xi-xj): return None
    xq=Fr(x); return max(l-Lq*abs(xq-a) for a,l,u in P_), min(u+Lq*abs(xq-a) for a,l,u in P_)
random.seed(7); bad=0; n=0
vals=[0.0,0.1,0.2,0.3,1/3,0.5,0.7,1.0,1.1,2.0]
for _ in range(20000):
    L=random.choice([0.0,0.1,0.3,1.0,2.0**-54,3.0]); k=random.randint(1,3)
    pts=[(random.choice([0.0,0.1,0.5,1.0,2.0]),) for _ in range(k)]
    pts=[(a,l,l+random.choice([0.0,0.1,2.0**-54])) for (a,),l in zip(pts,[random.choice(vals) for _ in range(k)])]
    x=random.choice([0.0,0.3,1.0,1.7,2.0]); thr=random.choice(vals+[1-2.0**-54])
    r=qualify(Fm(L),DecisionQuestion(x=x,threshold=thr),tuple(P(f"p{i}",a,a,l,u) for i,(a,l,u) in enumerate(pts)))
    e=exact(pts,L,x); s=st(r); n+=1
    if s=="LOCALLY_SUPPORTED_TRUE" and (e is None or e[0]<Fr(thr)): bad+=1; print("BAD TRUE",pts,L,x,thr,e)
    if s=="LOCALLY_SUPPORTED_FALSE" and (e is None or e[1]>=Fr(thr)): bad+=1; print("BAD FALSE",pts,L,x,thr,e)
    if e is None and s not in ("EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT","SOURCE_CONFLICT"): bad+=1; print("MISSED INCONSISTENT",pts,L,s)
print("fuzz cases:",n,"unsound outcomes:",bad)
random.seed(7); lost=0; dec=0
for _ in range(20000):
    L=random.choice([0.0,0.1,0.3,1.0,2.0**-54,3.0]); k=random.randint(1,3)
    pts=[(random.choice([0.0,0.1,0.5,1.0,2.0]),) for _ in range(k)]
    pts=[(a,l,l+random.choice([0.0,0.1,2.0**-54])) for (a,),l in zip(pts,[random.choice(vals) for _ in range(k)])]
    x=random.choice([0.0,0.3,1.0,1.7,2.0]); thr=random.choice(vals+[1-2.0**-54])
    e=exact(pts,L,x)
    if e is None: continue
    want="LOCALLY_SUPPORTED_TRUE" if e[0]>=Fr(thr) else "LOCALLY_SUPPORTED_FALSE" if e[1]<Fr(thr) else None
    if want:
        dec+=1
        s=st(qualify(Fm(L),DecisionQuestion(x=x,threshold=thr),tuple(P(f"p{i}",a,a,l,u) for i,(a,l,u) in enumerate(pts))))
        if s!=want: lost+=1
print("exactly decidable cases:",dec,"| code abstained or differed:",lost)
if bad or lost:  # R16-P01 (Codex, ronda 16): non-zero exit for automatic checks
    raise SystemExit(1)
