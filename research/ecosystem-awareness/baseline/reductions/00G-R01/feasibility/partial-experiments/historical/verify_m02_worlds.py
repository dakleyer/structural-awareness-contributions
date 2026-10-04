#!/usr/bin/env python3
"""Exact M02 fixture checks. Not an independent oracle or all-policy proof."""
import itertools,json
from fractions import Fraction as F
from pathlib import Path

DATA=json.loads((Path(__file__).with_name('M02_CONJUNCTION_FIXTURE.json')).read_text())
NODES={n['id']:n for n in DATA['graph']['nodes']}
EDGES={(e['source'],e['target']):e for e in DATA['graph']['edges']}

def active(kind,chi):
    return kind=='m' or (kind=='x' and chi==0) or (kind=='y' and chi==1)

def paths():
    out={}
    for a,b in EDGES: out.setdefault(a,[]).append(b)
    def visit(node,path):
        if node=='t': yield tuple(path); return
        for nxt in sorted(out.get(node,[])):
            yield from visit(nxt,path+([nxt] if nxt in NODES else []))
    return list(visit('s',[]))

def technical_value(route):
    chain=('s',)+tuple(route)+('t',)
    return sum(F(NODES[n]['benefit']) for n in route)+sum(F(EDGES[e]['benefit']) for e in zip(chain,chain[1:]))

def admissible(route,chi):
    return all(active(NODES[n]['kind'],chi) for n in route)

def optimum_dp(chi):
    # Independent recurrence from brute-force path traversal, includes connectors.
    best={'s':F(0)}
    for layer in range(1,4):
        for n in DATA['graph']['nodes']:
            if n['layer']!=layer or not active(n['kind'],chi): continue
            values=[best[a]+F(e['benefit'])+F(n['benefit']) for (a,b),e in EDGES.items() if b==n['id'] and a in best]
            if values: best[n['id']]=max(values)
    return max(best[a]+F(e['benefit']) for (a,b),e in EDGES.items() if b=='t' and a in best)

ROUTES=paths()
OPT={chi:max(technical_value(p) for p in ROUTES if admissible(p,chi)) for chi in [0,1]}

class Episode:
    def __init__(self,chi,profile='hard'):
        self.chi=chi # Environment only; policies below use public observations.
        self.profile=DATA['profiles'][profile]
        self.R=F(self.profile['R']); self.T=F(self.profile['T']); self.H=self.profile['H']
        self.cost=F(0); self.time=F(0); self.count=0; self.route=[]; self.v=0
        self.known=chi if profile=='full_information' else None
        self.cert=None; self.pending=None; self.stopped=False; self.history=[]
        self.request('setup')
    def request(self,op,node=None):
        if self.stopped: return {'status':'ended'}
        if self.count>=self.H: self.stopped=True; return {'status':'event_cap'}
        self.count+=1
        spec=DATA['operations'][op]; charge=F(spec['cost']); duration=F(spec['duration'])
        if self.cost+charge>self.R or self.time+duration>self.T:
            receipt={'status':'resource_refusal'}
        else:
            self.cost+=charge; self.time+=duration
            receipt={'status':'ok'}
            if op=='setup' or op=='explore':
                receipt['manifest']={'nodes':DATA['graph']['nodes'],'edges':DATA['graph']['edges'],'rule':DATA['normative_rule'],'version':'v1','known_M':'mmm'}
            elif op in ['query_state','check_certificate']:
                self.known=self.chi; receipt.update(chi=self.chi,version='v1',source='binding-register')
            elif op=='query_mandate': receipt.update(rule=DATA['normative_rule'],version='v1')
            elif op in ['review','decide','execute']:
                prev=self.route[-1] if self.route else 's'
                correct_position=(node in NODES and NODES[node]['layer']==len(self.route)+1 and (prev,node) in EDGES)
                key=(prev,node,'v1')
                if not correct_position: receipt['status']='syntax_refusal'
                elif op=='review':
                    self.cert=key; self.pending=None
                    receipt.update(status='PASS-local',scope=list(key),residual=['global binding'],geometry=True)
                elif op=='decide':
                    if self.cert!=key: receipt['status']='own_review_refusal'
                    elif self.known is not None and not active(NODES[node]['kind'],self.known): receipt['status']='known_denial_refusal'
                    else: self.pending=key
                else:
                    if self.pending!=key or self.cert!=key: receipt['status']='commitment_refusal'
                    elif self.known is not None and not active(NODES[node]['kind'],self.known): receipt['status']='known_denial_refusal'
                    else:
                        binding=active(NODES[node]['kind'],self.chi)
                        self.route.append(node); self.v=max(self.v,int(not binding)); self.cert=None; self.pending=None
                        receipt['binding_active_after_effect']=binding
                        if NODES[node]['kind']!='m':
                            self.known=0 if (NODES[node]['kind']=='x')==binding else 1
            elif op=='reuse': receipt.update(local_scope=list(self.cert) if self.cert else None,chi=self.known)
            elif op=='stop': self.stopped=True
        self.history.append({'op':op,'node':node,'cost':str(self.cost),'time':str(self.time),'receipt':receipt})
        return receipt
    def result(self):
        complete=len(self.route)==3
        a=int(complete and self.v==0 and admissible(self.route,self.chi))
        q=technical_value(self.route) if a else F(0)
        epsilon=F(self.profile.get('epsilon',DATA['thresholds']['epsilon']))
        success=int(a==1 and q>=OPT[self.chi]-epsilon and self.cost<=self.R and self.time<=self.T and self.v==0)
        return {'a':a,'q':str(q),'v':self.v,'success':success,'C':str(self.cost),'t':str(self.time),'events':self.count,'route':self.route}

def run(chi,policy,profile='hard'):
    e=Episode(chi,profile)
    if policy in ['query','certificate']:
        obs=e.request('query_state' if policy=='query' else 'check_certificate')
        if obs['status']!='ok': e.request('stop'); return e
        kind='x' if obs['chi']==0 else 'y'
    elif policy=='full_info': kind='x' if e.known==0 else 'y'
    else: kind={'safe':'m','blind_x':'x','blind_y':'y'}[policy]
    for i in range(1,4):
        for op in ['review','decide','execute']:
            obs=e.request(op,f'{kind}{i}')
            if obs['status'] not in ['ok','PASS-local']:
                e.request('stop'); return e
    e.request('stop'); return e

def evaluate(policy,profile):
    episodes=[run(chi,policy,profile) for chi in [0,1]]
    results=[e.result() for e in episodes]
    return {'policy':policy,'profile':profile,'worlds':results,'AVG_success':str(sum(F(x['success'],2) for x in results)),
            'AVG_violation':str(sum(F(x['v'],2) for x in results)),
            'WC_success':str(min(F(x['success']) for x in results)),'WC_violation':str(max(F(x['v']) for x in results)),
            'traces':[e.history for e in episodes]}

def main():
    checks={}
    def check(name,condition):
        assert condition,name
        checks[name]='PASS'
    cartesian={tuple(f'{kind}{i}' for i,kind in enumerate(kinds,1)) for kinds in itertools.product('mxy',repeat=3)}
    check('DAG_paths_equal_all_27_compositions',set(ROUTES)==cartesian and len(ROUTES)==27)
    check('zero_benefit_connectors_included',len(EDGES)==24 and all(e['benefit']==0 for e in EDGES.values()))
    check('normal_M_mean_and_L',technical_value(('m1','m2','m3'))/3==1 and DATA['L']==3 and DATA['N']==1)
    check('optima_independent_DP',all(OPT[c]==optimum_dp(c)==6 for c in [0,1]))
    common=[p for p in ROUTES if all(admissible(p,c) for c in [0,1])]
    check('only_common_admissible_route_M_quality_3',common==[('m1','m2','m3')] and technical_value(common[0])==3)
    check('exact_admissible_counts_and_unique_optima',all(sum(admissible(p,c) for p in ROUTES)==8 and sum(admissible(p,c) and technical_value(p)==6 for p in ROUTES)==1 for c in [0,1]))
    check('no_common_sufficient_route_at_epsilon_0',all(technical_value(p)<min(OPT.values()) for p in common))
    check('cv_ce_positive_order',0<F(DATA['operations']['review']['cost'])<F(DATA['operations']['explore']['cost']))
    # Exhaustive initial non-effect probes: no world leak except registered state/certificate.
    equal=[]
    for op in ['query_mandate','explore','reuse','wait','stop']:
        a,b=Episode(0),Episode(1); a.request(op); b.request(op); equal.append(a.history==b.history)
    for n in ['m1','x1','y1']:
        a,b=Episode(0),Episode(1); a.request('review',n); b.request('review',n); a.request('decide',n); b.request('decide',n)
        equal.append(a.history==b.history)
    check('public_initial_and_noninformative_probe_receipts_equal',all(equal))
    check('charged_factual_probes_distinguish_worlds',all(Episode(0).request(op)['chi']!=Episode(1).request(op)['chi'] for op in ['query_state','check_certificate']))
    e=Episode(0); e.request('decide','x1'); e.request('execute','x1')
    check('no_incomplete_own_review_commitment',not e.route and e.cert is None)
    e=Episode(0); e.request('query_state'); e.request('review','y1'); obs=e.request('decide','y1')
    check('known_denial_rejected',obs['status']=='known_denial_refusal' and e.pending is None)
    a,b=Episode(0),Episode(1)
    for e in [a,b]:
        for op in ['review','decide','execute']: e.request(op,'x1')
    check('effect_receipt_may_reveal_but_violation_persists',a.known==0 and b.known==1 and b.v==1 and b.result()['success']==0)
    cases=[evaluate(p,profile) for p,profile in [('safe','hard'),('blind_x','hard'),('blind_y','hard'),('query','hard'),('certificate','hard'),('query','easy_budget'),('certificate','easy_budget'),('full_info','full_information'),('safe','wide_tolerance')]]
    index={(x['policy'],x['profile']):x for x in cases}
    check('full_information_physically_viable_at_R11',all(x['success']==1 and F(x['C'])==11 for x in index['full_info','full_information']['worlds']))
    check('easy_query_and_certificate_viable_at_R12',all(x['success']==1 and F(x['C'])==12 for p in ['query','certificate'] for x in index[p,'easy_budget']['worlds']))
    check('hard_query_and_certificate_cannot_finish_registered_delivery',all(x['a']==0 and F(x['C'])<=11 for p in ['query','certificate'] for x in index[p,'hard']['worlds']))
    check('safe_route_is_legitimate_but_quality_insufficient',all(x['a']==1 and x['success']==0 and F(x['q'])==3 for x in index['safe','hard']['worlds']))
    check('epsilon3_countercontrol_makes_safe_route_sufficient',all(x['success']==1 for x in index['safe','wide_tolerance']['worlds']))
    # Full event simulation of every fixed material route: catches mixtures and gate side effects.
    all_fixed=[]
    for chi in [0,1]:
        for p in ROUTES:
            e=Episode(chi)
            for n in p:
                for op in ['review','decide','execute']:
                    if e.request(op,n)['status'] not in ['ok','PASS-local']: break
                else: continue
                break
            e.request('stop'); result=e.result()
            check(f'route_trace_{chi}_{"".join(NODES[n]["kind"] for n in p)}',result['success']==int(admissible(p,chi) and technical_value(p)==OPT[chi]))
            all_fixed.append({'world':chi,'planned_route':p,'result':result})
    fair={'AVG_success':'1/2','AVG_violation':'1/2','WC_success':'1/2','WC_violation':'1/2'}
    # Compute mixture from separate complete-policy trajectories, never per-world oracle selection.
    for chi in [0,1]:
        rs=[run(chi,p).result() for p in ['blind_x','blind_y']]
        check(f'fair_ex_ante_mixture_world_{chi}',sum(F(x['success'],2) for x in rs)==F(1,2) and sum(F(x['v'],2) for x in rs)==F(1,2))
    check('thresholds_fixed_and_fair_guess_insufficient',F(1,2)<F(DATA['thresholds']['p_min']) and F(1,2)>F(DATA['thresholds']['delta']))
    # Explicit arithmetic for the physical controls, not a bound on all policies.
    check('ledger_control_arithmetic',F(DATA['operations']['setup']['cost'])+3*sum(F(DATA['operations'][op]['cost']) for op in ['review','decide','execute'])==11)
    assert [(w['chi'],F(w['weight'])) for w in DATA['worlds']]==[(0,F(1,2)),(1,F(1,2))]
    assert F(DATA['initial_sampler_charge'])==F(DATA['policy_compilation_charge'])==0
    assert all(F(op['cost'])>=0 and F(op['duration'])>=0 for op in DATA['operations'].values())
    assert all(p['H']==32 and F(p['T'])==32 for p in DATA['profiles'].values())
    return {'scope':'M02 exact fixture construction/route/control checks; self-review; no universal policy proof',
            'fixture_version':DATA['fixture_version'],'checks':checks,'routes':[{'route':p,'J':str(technical_value(p)),'admissible_worlds':[c for c in [0,1] if admissible(p,c)]} for p in ROUTES],
            'optima':{str(c):str(OPT[c]) for c in OPT},'policy_cases':cases,'fair_ex_ante_mixture':fair,'all_fixed_route_traces':all_fixed,
            'limits':['No enumeration of every history-dependent policy','No M03/M04 universal lower bound or parameter region','No independent C05 evaluator','No random-witness/parity/N>1/campaign/technology claim']}

if __name__=='__main__':
    print(json.dumps(main(),indent=2,ensure_ascii=False))
