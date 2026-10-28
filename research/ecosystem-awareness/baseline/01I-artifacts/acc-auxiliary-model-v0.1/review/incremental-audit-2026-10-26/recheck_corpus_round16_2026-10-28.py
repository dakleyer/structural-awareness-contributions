"""PR58 round16: pinned closure checks, pending diagnostics and finite examples.

Stdlib; source copies in a temporary directory. Default stdout; --output
creates a new file exclusively. --snapshot-root reads the archived layout.
The known pending diagnostics are expected outcomes, not fixes or field data.
"""
from __future__ import annotations
import argparse,hashlib,importlib.util,itertools,json,math,sys,tempfile
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
from urllib.request import Request,urlopen
B='research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/'
SOURCES={
 'metacognition':('main','51fc686f45b6ef10c53b69f4c26d0e381b007ff8',B+'scoped-closure-metacognition-v0.1/metacognition.py','213c943f1b56f096db47af86af6baf4cac612023'),
 'reference':('main','51fc686f45b6ef10c53b69f4c26d0e381b007ff8',B+'scoped-closure-metacognition-v0.1/REFERENCE_SYNTHETIC_RESULTS.json','27aa4328da00cd05883911a843dee7d3d705b4b4'),
 'online':('PR60_latest','cb72bb65ab148de1c7396d9cb8f9c1b7af6edc25',B+'mathematical-lineage-social-agentic-v0.1/test_theme18_online_context.py','79872a3f3ff98538e37df198fe2e9b2351cda67d'),
 'admission':('PR60_latest','cb72bb65ab148de1c7396d9cb8f9c1b7af6edc25',B+'mathematical-lineage-social-agentic-v0.1/test_theme18_candidate_admission.py','57794f4c2605443170b1f8b9f523ee53a1d6f9c5')}
def blob(b):return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def run(snap,tmp):
    modules={};pins=[]
    for name,(label,ref,path,expected) in SOURCES.items():
        if snap:b=(snap/label/path).read_bytes()
        else:
            u='https://raw.githubusercontent.com/dakleyer/structural-awareness-contributions/'+ref+'/'+path
            with urlopen(Request(u,headers={'User-Agent':'IMSV-pinned-recheck'}),timeout=60) as r:b=r.read()
        assert blob(b)==expected,(name,'pin mismatch')
        pins.append({'name':name,'ref':ref,'path':path,'blob':expected})
        if name=='reference':modules[name]=json.loads(b);continue
        p=tmp/(name+'.py');p.write_bytes(b)
        spec=importlib.util.spec_from_file_location('_r16_'+name,p);m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m);modules[name]=m
    m=modules['metacognition'];o=modules['online'];a=modules['admission'];checks=[];facts={}
    def check(name,ok):
        checks.append({'name':name,'passed':bool(ok)})
        if not ok:raise AssertionError(name)
    def p(cid,x,y):return m.Point(cid,cid,'x','v1',4,x,x,y,y)
    def frame(L):return m.Frame('x','v1',5,5,0,2,L,True)
    def status(ps,L,x,t):return m.qualify(frame(L),m.DecisionQuestion(x,t),tuple(ps))
    eps=2.0**-54
    cases=[('I-01/M27-02',status([p('a',0,1e-13),p('b',0,0)],0,0,5e-14),'EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT'),
           ('M27-01',status([p('a',0,0),p('b',0,2)],1,1,1),'EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT'),
           ('M28-01a',status([p('a',0,1),p('b',1,-eps)],1,0,1),'EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT'),
           ('M28-01b',status([p('a',0,1)],eps,1,1),'UNDETERMINED_FROM_AVAILABLE_EVIDENCE'),
           ('D28-F01 same numerical family',status([p('a',0,0),p('b',.1,.1*.1)],.1,0,0),'EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT'),
           ('positive certificate',status([p('a',0,1),p('b',1,2)],1,.5,1.25),'LOCALLY_SUPPORTED_TRUE')]
    for label,r,want in cases:check(label,r['local_answer_status']==want)
    check('positive envelope preserved',cases[-1][1]['conditional_answer_bounds']==[1.5,1.5])
    lo,hi=cases[3][1]['conditional_answer_bounds']
    check('published lower rounded outward',F(lo)<=1-F(eps))
    check('published upper rounded outward',F(hi)>=1+F(eps))
    check('synthetic report content unchanged',m.synthetic_report()==modules['reference'])
    facts['closure']={label:r['local_answer_status'] for label,r,_ in cases}
    facts['closure_scope']='exact finite-input numerical runner; not source authenticity, open exterior or human independent review'
    try:o.full_verdict(12);out=False
    except ValueError:out=True
    check('M28-02 full evaluator rejects outside domain',out)
    rejected=[]
    for x in (-2,10,12,False,True,2.0,3.0):
        try:o.guarded_verdict(x,guard_validated=True,proof_scope=o.DOMAIN);rejected.append(False)
        except ValueError:rejected.append(True)
    check('M28-02 fixed in branch: domain and alias cases rejected',all(rejected))
    check('M28-02 positive finite domain preserved',all(o.guarded_verdict(x,guard_validated=True,proof_scope=o.DOMAIN)[0]==o.full_verdict(x) for x in o.DOMAIN))
    facts['branch_repair']={'M28-02':'reconfirmed in branch60; incorporation into main pending'}
    kw=dict(received_after_exchange=True,source_to_value_link_qualified=True,action_authorized=True,decision_budget_ok=True)
    r=a.assess_candidate(a.reports(),source_value_lower_bound=float('nan'),**kw)
    check('pending M28-03: invalid bound still yields proposal',r['candidate_status']=='SCOPED_PROPOSAL_FOR_EXTERNAL_ACTION_CHECK')
    check('M28-03 fixture never executes action',r['execution']=='NEVER')
    rec=o.capture_pre_admission('new-route',permitted=True,capture_enabled=True)
    cert={'verified':True,'source_scope':'route-v1','expires_before':3,'target_event':'new-route'}
    check('M28-04 helper still only checks capture-era validity',o.requalify(rec,cert)=='ADMISSIBLE_FOR_NEW_REVIEW')
    facts['pending']={'M28-03':'NaN passes utility gate; execution NEVER','M28-04':'decision time absent; missing temporal scope, no deployed failure asserted'}
    # Equal success rates do not remove success-conditioned cost selection.
    A=[(True,1)]*50+[(False,100)]*50
    C=[(False,1)]*50+[(True,10)]*50
    mean=lambda xs:sum(xs)/len(xs)
    rate=lambda rows:F(sum(s for s,c in rows),len(rows))
    cond=lambda rows:F(sum(c for s,c in rows if s),sum(s for s,c in rows))
    full=lambda rows:F(sum(c for s,c in rows),len(rows))
    check('FA4 illustration matched success rates',rate(A)==rate(C)==F(1,2))
    check('FA4 conditional successful cost favours A',cond(A)==1 and cond(C)==10)
    check('FA4 complete cost reverses that ordering',full(A)==F(101,2) and full(C)==F(11,2))
    facts['FA4']={'scope':'constructed reason to formalize the existing requirement to include misses, not a measured policy ranking','success_rate_A':str(rate(A)),'success_rate_B':str(rate(C)),'conditional_cost_A':str(cond(A)),'conditional_cost_B':str(cond(C)),'all_attempts_cost_A':str(full(A)),'all_attempts_cost_B':str(full(C))}
    worlds=list(itertools.product((0,1),repeat=2));Y=lambda w:w[0]^w[1]
    def H(vals):
        cs=Counter(vals);n=len(vals)
        return -sum(c/n*math.log2(c/n) for c in cs.values())
    def conditional(view):
        groups={}
        for w in worlds:groups.setdefault(view(w),[]).append(Y(w))
        return sum(len(v)/len(worlds)*H(v) for v in groups.values())
    h0=conditional(lambda w:w[0]);h1=conditional(lambda w:w[1]);hd=conditional(lambda w:(w[0],w[0]));hj=conditional(lambda w:(w[0],w[1]))
    check('XOR each local observation retains one target bit',h0==h1==1)
    check('XOR duplicate source adds no target discrimination',hd==1)
    check('XOR complementary pair determines target',hj==0)
    check('XOR each local target question is unresolved on every exposure',all(len({Y(v) for v in worlds if v[i]==w[i]})==2 for i in (0,1) for w in worlds))
    facts['XOR']={'scope':'classical finite complementarity illustration, not a new information theorem or MSCA implementation','H_Y_given_X0':h0,'H_Y_given_X1':h1,'H_Y_given_duplicate_X0':hd,'H_Y_given_X0_X1':hj,'local_unknown_rate_each':1}
    return {'scope':'pinned AI-assisted recheck and constructed mathematics; known failures remain diagnostics','sources':pins,'checks':checks,'passed':sum(c['passed'] for c in checks),'total':len(checks),'facts':facts}
def main():
    p=argparse.ArgumentParser();p.add_argument('--snapshot-root',type=Path);p.add_argument('--output',type=Path);args=p.parse_args()
    with tempfile.TemporaryDirectory(prefix='imsv-r16-') as tmp:r=run(args.snapshot_root,Path(tmp))
    payload=json.dumps(r,ensure_ascii=False,indent=2,allow_nan=False)+'\n'
    if args.output:
        with args.output.open('x',encoding='utf-8',newline='\n') as stream:stream.write(payload)
        print(json.dumps({'passed':r['passed'],'total':r['total']}))
    else:print(payload,end='')
if __name__=='__main__':main()
