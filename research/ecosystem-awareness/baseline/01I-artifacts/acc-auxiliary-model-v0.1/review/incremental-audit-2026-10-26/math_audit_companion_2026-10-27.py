"""Pinned, read-only mathematical audit checks for PR58. Standard library only.
Run: python math_audit_companion_2026-10-27.py
Optional: --source-archive PATH to the 27-Oct archived source layout.
Downloads are public, immutable source blobs; no credentials or source edits.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, itertools, json, math, sys, urllib.request
from pathlib import Path

HERE=Path(__file__).resolve().parent
BASE="research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/"
SOURCES=[
 ("main/studies/scoped-closure-metacognition-v0.1/metacognition.py", "891af45a75b245082859147c0f7233cf85dd9035", BASE+"scoped-closure-metacognition-v0.1/metacognition.py", "b8b162dfd3112880a4258a2e8a37ea672e075a74"),
 ("pr57/agentic_reduction.py", "553678e15e1ee3591736a4b8428abd4af4efc6fd", BASE+"agentic-ecosystem-reduction-v0.1/agentic_reduction.py", "be7b04af92f3d2dc29b3f9dc79e2052b7418d602"),
 ("pr57/residual_cartography_stage.py", "553678e15e1ee3591736a4b8428abd4af4efc6fd", BASE+"agentic-ecosystem-reduction-v0.1/residual_cartography_stage.py", "eb8cd33989aae14a22a1c2012bfe0da0581a8e3e"),
 ("pr57/CASES.json","553678e15e1ee3591736a4b8428abd4af4efc6fd",BASE+"agentic-ecosystem-reduction-v0.1/CASES.json","be77afef2a1bd3000bbfd1dca373b66db355b5db")
]

def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--source-archive",type=Path)
    parser.add_argument("--output",type=Path,default=HERE/"MATH_AUDIT_RESULTS_2026-10-27.json")
    args=parser.parse_args()
    root=args.source_archive or HERE/".pinned-math-audit-sources"
    verified=[]; locations={}
    for local,revision,remote,expected in SOURCES:
        path=root/local
        if not args.source_archive and not path.exists():
            path.parent.mkdir(parents=True,exist_ok=True)
            url="https://raw.githubusercontent.com/dakleyer/structural-awareness-contributions/"+revision+"/"+remote
            with urllib.request.urlopen(url,timeout=30) as response:raw=response.read()
            path.write_bytes(raw)
        raw=path.read_bytes()
        actual=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
        if actual!=expected:raise RuntimeError("Source pin mismatch: "+local)
        verified.append({"path":remote,"revision":revision,"blob":actual})
        locations[local]=path
    checks=[]; findings={}
    def require(name,condition):
        checks.append({"check":name,"passed":bool(condition)})
        if not condition:raise AssertionError(name)
    m=load_module("audit_m27_metacognition",locations[SOURCES[0][0]])
    load_module("agentic_reduction",locations[SOURCES[1][0]])
    rc=load_module("audit_m27_cartography",locations[SOURCES[2][0]])
    frame=m.Frame("scope","v1",10,20,0,10,1,True)
    def point(name,x,y):return m.Point(name,"source-"+name,"scope","v1",10,x,x,y,y)
    contradictory=m.qualify(frame,m.DecisionQuestion(1,1),(point("a",0,0),point("b",0,2)))
    require("M27-01 original emits positive local status",contradictory["local_answer_status"]=="LOCALLY_SUPPORTED_TRUE")
    require("M27-01 bounds look nonempty at query",contradictory["conditional_answer_bounds"]==[1,1])
    require("M27-01 no joint function at x=0",0!=2)
    consistent=m.qualify(frame,m.DecisionQuestion(1,1),(point("a",0,0),point("b",1,1)))
    require("M27-01 consistent positive control",consistent["local_answer_status"]=="LOCALLY_SUPPORTED_TRUE")
    # Illustrative fixed-coordinate Lipschitz feasibility, not a repair for uncertain x.
    def fixed_feasible(points,L):
        return all(lo<=hi for x,lo,hi in points) and all(
            lo_i<=hi_j+L*abs(x_i-x_j)
            for x_i,lo_i,hi_i in points for x_j,lo_j,hi_j in points)
    require("M27-01 fixed-coordinate global gate rejects conflict",not fixed_feasible([(0,0,0),(0,2,2)],1))
    require("M27-01 fixed-coordinate global gate retains control",fixed_feasible([(0,0,0),(1,1,1)],1))
    findings["M27-01"]={"observed":contradictory,"consistent_control":consistent,"qualification":"global feasibility absent; query-local condition alone is insufficient"}
    near=m.qualify(frame,m.DecisionQuestion(0,0),(point("a",0,1e-13),point("b",0,0)))
    require("M27-02 empty interval admitted by original tolerance",near["conditional_answer_bounds"]==[1e-13,0] and near["local_answer_status"]=="LOCALLY_SUPPORTED_TRUE")
    findings["M27-02"]=near
    event=rc.Observation("missing-first-capture",7,rc.CROSS_SOURCE_SCOPE,(.9,.85,.8,.95))
    stages=rc.three_stages(events=(event,))
    require("M27-07 missing identity retained as None",stages["first_capture_observer_id"] is None)
    require("M27-07 stage3 can still emit rule",stages["stage_3_meta_syntax_message"] is not None)
    findings["M27-07"]={"first_capture_observer_id":None,"output":stages["stage_3"]["observed_by_referee_only"]["output"],"rule_emitted":True,"qualification":"provenance-contract clarification; not a refutation of the conjunction"}
    pairs=list(itertools.combinations(range(4),2))
    residual=[(x,y) for x,y in pairs if x//2==y//2]
    missing_q=[(x,y) for x,y in pairs if x%2==y%2]
    missing_aq=[(x,y) for x,y in residual if x%2==y%2]
    require("M27-03 Q-only misses two pairs",missing_q==[(0,2),(1,3)])
    require("M27-03 A+Q suffices",len(residual)==2 and missing_aq==[])
    findings["M27-03"]={"all_conflicts":len(pairs),"remaining_after_A":len(residual),"Q_only_uncovered":missing_q,"A_plus_Q_uncovered":missing_aq}
    q=.9;n=19;D=lambda k:k*(1-q**(k-1))
    central=D(n+1)-2*D(n)+D(n-1)
    backward=D(n)-2*D(n-1)+D(n-2)
    printed=q**(n-2)*(1-q)*((1+q)-n*(1-q))
    require("M27-08 printed is central in checked case",abs(printed-central)<1e-12)
    require("M27-08 backward differs at same index",abs(printed-backward)>1e-4)
    findings["M27-08"]={"n":n,"q":q,"printed":printed,"central":central,"backward_same_index":backward}
    r=1;q_rate=1;H=1
    original=lambda S:r*S-q_rate*(H-S)
    require("M27-10 positive linearization",r+q_rate>0)
    require("M27-10 interval not invariant",original(0)<0 and original(H)>0)
    require("M27-11 variance-bias counterexample",.01+(.9*.1)**2<.1)
    require("M27-11 opposite regime contrast",.01+(.9*1)**2>.1)
    findings["M27-11"]={"pure_mean_MSE":.1,"mixed_mean_MSE_small_shift":.0181,"mixed_mean_MSE_large_shift":.82}
    posterior_one=.75
    posterior_two=(.5*.75**2)/(.5*.75**2+.5*.25**2)
    require("M27-12 same-type earlier data changes posterior",math.isclose(posterior_two,.9) and posterior_two!=posterior_one)
    findings["M27-12"]={"posterior_current_only":posterior_one,"posterior_with_same_type_past":posterior_two,"qualification":"earlier same-type data must be retained or proved conditionally irrelevant"}
    scores=[-1,1]*5
    require("M27-13 bounded score may switch each sample",all(abs(a-b)<=2 for a,b in zip(scores,scores[1:])) and all(a*b<0 for a,b in zip(scores,scores[1:])))
    require("M27-13 continuous dwell example",math.isclose((.5-(-.5))/2,.5))
    safe=(0,1);other=(-1,100)
    require("M27-14 candidate pointwise safe",all(x>=0 for x in safe))
    require("M27-14 competitor has risky state",other[0]<0)
    require("M27-14 no pointwise or expected dominance",safe[1]<other[1] and sum(safe)/2<sum(other)/2)
    findings["M27-14"]={"inaction":[0,0],"safe":safe,"competitor":other,"equal_probability_expected_values":[sum(safe)/2,sum(other)/2]}
    require("M27-15 certified-region return",abs(.7-.5)>.1 and abs(.5-.5)<=.1)
    queue=lambda t:2*t if t<=3 else max(0,12-2*t)
    require("M27-16 finite overload reaches six",queue(3)==6)
    require("M27-16 finite overload clears",queue(6)==0)
    findings["M27-16"]={"lambda_first_three":4,"lambda_after_three":0,"mu":2,"backlog_at_three":queue(3),"backlog_at_six":queue(6)}
    # Constructed dynamic and population opportunities, not canonical source repairs.
    def rk4(sign,t,steps=2000):
        y=0.;z=float(sign);dt=t/steps
        def f(y,z):return -y+z,-z
        for _ in range(steps):
            a,b=f(y,z);c,d=f(y+dt*a/2,z+dt*b/2);e,fv=f(y+dt*c/2,z+dt*d/2);g,h=f(y+dt*e,z+dt*fv)
            y+=dt*(a+2*c+2*e+g)/6;z+=dt*(b+2*d+2*fv+h)/6
        return y,z
    plus=rk4(1,1)[0];minus=rk4(-1,1)[0]
    require("M27-O1 stable dynamic opposite predicates",plus>.2 and minus<=.2)
    require("M27-O1 numerical versus analytic solution",abs(plus-math.exp(-1))<1e-10)
    require("M27-O2 pointwise error envelope can return",math.exp(-1)>.2 and 3*math.exp(-3)<.2)
    def simpson(f,a,b,N=4000):
        h=(b-a)/N
        return h/3*(f(a)+f(b)+sum((4 if i%2 else 2)*f(a+i*h) for i in range(1,N)))
    t=10.;gamma=1.;beta=1.
    density=lambda age:math.exp(gamma*(t-age))
    mass=simpson(density,0,t)
    mean=simpson(lambda age:density(age)*math.exp(-beta*age),0,t)/mass
    theoretical=gamma/(gamma+beta)*(-math.expm1(-(gamma+beta)*t))/(-math.expm1(-gamma*t))
    require("M27-O3 population integral matches formula",abs(mean-theoretical)<1e-9)
    require("M27-O3 positive limiting mean case",abs(mean-.5)<.0001)
    require("M27-O3 constant-influx negative control",(1-math.exp(-1000))/1000<.00101)
    findings["M27-O1-O3"]={"plus_at_one":plus,"minus_at_one":minus,"population_mean_ten":mean,"population_limit_gamma_beta_one":.5,"limiting_fraction_loss_over_quarter":.75}
    result={"scope":"Pinned source-defect reproductions and constructed finite mathematical checks; not experiments, source repairs, DDS admission or independent human validation",
            "sources_verified":verified,"checks":checks,"passed":sum(c["passed"] for c in checks),"total":len(checks),"findings":findings}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"passed":result["passed"],"total":result["total"],"verified_source_blobs":len(verified)},ensure_ascii=False))
if __name__=="__main__":main()

