"""Pinned finite counterexamples for PR58 round12; no source edits.

Default: stdout. --output creates a NEW file exclusively. Sources are read
from --snapshot-root or downloaded at immutable public revisions into a
temporary directory. This is AI-assisted desk verification, not field evidence.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, math, sys, tempfile
from fractions import Fraction
from pathlib import Path
from urllib.request import urlopen, Request

BASE='research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/'
SOURCES={
 'metacognition':('PR64','0229bf9439be8459680dce4f7fe0376a9cd31306',BASE+'scoped-closure-metacognition-v0.1/metacognition.py','d4f6cf172ec8b3a17d30d9993a03c5a1eb4c6a28'),
 'online':('PR60','3a846c6bb0fed6c25bf6deaa7af084a69ea242b5',BASE+'mathematical-lineage-social-agentic-v0.1/test_theme18_online_context.py','e8518ca15964b91ac925adf727ddae70d192a138'),
 'admission':('PR60','3a846c6bb0fed6c25bf6deaa7af084a69ea242b5',BASE+'mathematical-lineage-social-agentic-v0.1/test_theme18_candidate_admission.py','57794f4c2605443170b1f8b9f523ee53a1d6f9c5'),
}
def blob(data): return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def load_sources(snapshot_root,tmp):
    modules={};verified=[]
    for name,(label,ref,path,expected) in SOURCES.items():
        if snapshot_root is not None: data=(snapshot_root/label/path).read_bytes()
        else:
            url='https://raw.githubusercontent.com/dakleyer/structural-awareness-contributions/'+ref+'/'+path
            with urlopen(Request(url,headers={'User-Agent':'IMSV-bounded-audit'}),timeout=60) as r:data=r.read()
        assert blob(data)==expected,(name,'source blob mismatch')
        p=tmp/(name+'.py');p.write_bytes(data)
        spec=importlib.util.spec_from_file_location('_audit28_'+name,p)
        m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
        modules[name]=m;verified.append({'label':label,'ref':ref,'path':path,'blob':expected})
    return modules,verified
def evaluate(modules,verified):
    m=modules['metacognition'];o=modules['online'];a=modules['admission'];checks=[];facts={}
    def check(name,condition):
        checks.append({'name':name,'passed':bool(condition)})
        assert condition,name
    def point(cid,x,y):return m.Point(cid,cid,'x','v1',4,x,x,y,y)
    eps=2.0**-54
    f=m.Frame('x','v1',5,5,0,2,1,True)
    ps=(point('a',0.0,1.0),point('b',1.0,-eps))
    r=m.qualify(f,m.DecisionQuestion(0.0,1.0),ps)
    exact_excess=Fraction(1)-Fraction(-eps)-Fraction(1)
    check('M28-01a exact binary inputs violate Lipschitz by 2^-54',exact_excess==Fraction(1,2**54))
    check('M28-01a current float candidate incorrectly supports TRUE',r['local_answer_status']=='LOCALLY_SUPPORTED_TRUE')
    check('M28-01a rounded pair guard misses that inconsistency',m._joint_evidence_status(list(ps),1)=='CONSISTENT')
    f2=m.Frame('x','v1',5,5,0,2,eps,True)
    r2=m.qualify(f2,m.DecisionQuestion(1.0,1.0),(point('a',0.0,1.0),))
    exact_lo=Fraction(1)-Fraction(eps)
    check('M28-01b compatible single-point model admits values below threshold',exact_lo<Fraction(1))
    check('M28-01b float lower-bound rounding nevertheless supports TRUE',r2['local_answer_status']=='LOCALLY_SUPPORTED_TRUE')
    facts['M28-01']={'epsilon':eps,'exact_pair_excess':str(exact_excess),'pair_status':r['local_answer_status'],'single_point_status':r2['local_answer_status'],'required_pair_status':'EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT','required_single_point_status':'UNDETERMINED_FROM_AVAILABLE_EVIDENCE'}
    # These original examples ARE repaired in the candidate.
    normal=(point('a',0,0),point('b',0,2))
    check('original M27-01 is rejected by PR64',m.qualify(f,m.DecisionQuestion(1,1),normal)['local_answer_status']=='EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT')
    f0=m.Frame('x','v1',5,5,0,2,0,True)
    tiny=(point('a',0,1e-13),point('b',0,0))
    check('original I01/M27-02 is rejected by PR64',m.qualify(f0,m.DecisionQuestion(0,5e-14),tiny)['local_answer_status']=='EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT')
    try:o.full_verdict(12);full_rejects=False
    except ValueError:full_rejects=True
    guarded=o.guarded_verdict(12,guard_validated=True,proof_scope=o.DOMAIN)
    check('M28-02 full evaluator rejects input outside proof domain',full_rejects)
    check('M28-02 shortcut nevertheless skips outside its proof domain',guarded==('REJECT',True))
    check('M28-02 in-domain positive control agrees',o.guarded_verdict(2,guard_validated=True,proof_scope=o.DOMAIN)==(o.full_verdict(2),True))
    facts['M28-02']={'x':12,'domain':list(o.DOMAIN),'full':'ValueError','guarded':list(guarded)}
    kw=dict(received_after_exchange=True,source_to_value_link_qualified=True,action_authorized=True,decision_budget_ok=True)
    nan_result=a.assess_candidate(a.reports(),source_value_lower_bound=float('nan'),**kw)
    inf_result=a.assess_candidate(a.reports(),source_value_lower_bound=float('inf'),**kw)
    check('M28-03 NaN bypasses purported positive lower bound',nan_result['candidate_status']=='SCOPED_PROPOSAL_FOR_EXTERNAL_ACTION_CHECK')
    check('M28-03 infinite lower bound also accepted',inf_result['candidate_status']=='SCOPED_PROPOSAL_FOR_EXTERNAL_ACTION_CHECK')
    check('M28-03 genuinely absent lower bound retains uncertainty',a.assess_candidate(a.reports(),source_value_lower_bound=None,**kw)['candidate_status']=='UTILITY_NOT_ESTABLISHED')
    check('M28-03 no action is executed by this fixture',nan_result['execution']=='NEVER' and inf_result['execution']=='NEVER')
    facts['M28-03']={'NaN_status':nan_result['candidate_status'],'infinite_status':inf_result['candidate_status'],'execution':nan_result['execution']}
    rec=o.capture_pre_admission('new-route',permitted=True,capture_enabled=True)
    cert={'verified':True,'source_scope':'route-v1','expires_before':3,'target_event':'new-route'}
    check('M28-04 expiry helper only compares with old capture time',o.requalify(rec,cert)=='ADMISSIBLE_FOR_NEW_REVIEW')
    check('M28-04 hypothetical later decision lies beyond expiry',10>cert['expires_before'])
    facts['M28-04']={'classification':'missing time parameter / scope clarification; no deployed runtime failure asserted','capture_time':1,'expiry':3,'hypothetical_decision_time':10,'helper_status':o.requalify(rec,cert)}
    # Independent finite check of the received conditional-query correction.
    X=range(4);obs=lambda x:x//2;q=lambda x:x%2
    conflicts=[(x,y) for x in X for y in X if x<y and obs(x)==obs(y)]
    check('M27-03 conditional conflict universe has exactly two pairs',conflicts==[(0,1),(2,3)])
    check('M27-03 one supplemental query separates all remaining pairs',all(q(x)!=q(y) for x,y in conflicts))
    check('M27-03 Q-only does not identify every state',q(0)==q(2))
    # New conditional expected-work opportunity, not a measured selector.
    D=100;s=10;h=5;p=Fraction(1,2)
    expected=Fraction(h)+p*s+(1-p)*D
    check('M28-O1 exact success/fallback cost identity',expected==h+D-p*(D-s))
    check('M28-O1 declared example saves work against full-grid procedure',expected==60 and expected<D)
    check('M28-O1 no-hit negative control loses overhead',h+D>D)
    check('M28-O1 expensive selection negative control can lose',50+D-p*(D-s)>D)
    facts['M28-O1']={'scope':'conditional algebra against declared full-grid procedure only; not measured gain','D':D,'s':s,'h':h,'p':str(p),'expected_bound':str(expected),'strict_gain_condition':'h < p*(D-s)'}
    return {'scope':'AI-assisted pinned finite reproductions and algebra, not independent human validation or source repair','sources_verified':verified,'checks':checks,'passed':sum(c['passed'] for c in checks),'total':len(checks),'facts':facts}
def main():
    p=argparse.ArgumentParser();p.add_argument('--snapshot-root',type=Path);p.add_argument('--output',type=Path);args=p.parse_args()
    with tempfile.TemporaryDirectory(prefix='imsv-pr58-r12-') as tmp:
        modules,verified=load_sources(args.snapshot_root,Path(tmp));result=evaluate(modules,verified)
    payload=json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n'
    if args.output:
        with args.output.open('x',encoding='utf-8',newline='\n') as f:f.write(payload)
        print(json.dumps({'passed':result['passed'],'total':result['total']}))
    else:print(payload,end='')
if __name__=='__main__':main()
