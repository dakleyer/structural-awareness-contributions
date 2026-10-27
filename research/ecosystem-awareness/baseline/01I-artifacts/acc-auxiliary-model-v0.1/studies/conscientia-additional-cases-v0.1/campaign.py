"""Conscientia Ecosystemica documents -> reproducible bounded toy experiments.

NOT a test on human subjects, actual organizations or deployed AI products.
All parameters are predeclared in CASES.json; no closed-world claim about C/D.
"""
from __future__ import annotations
import json, math, hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCHEMA='CONSCIENTIA-DOC-EXPERIMENTS-v0.1'

def finite(x, label):
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x):
        raise ValueError(f'{label}: finite numeric required')
    return float(x)

def rnd(x):
    if isinstance(x,float) and not math.isfinite(x): return str(x)
    return round(x,8) if isinstance(x,float) else x

def shannon(p):
    return -sum(x*math.log2(x) for x in p if x>0)

def result(case):
    t=case['kind']; cid=case['id']
    def res(status, **kw): return {'id':cid,'group':case['group'],'source':case['source'],'status':status,**kw}
    if t=='compare':
        a,b=case['actual'],case['alternative'];coord=finite(case['max_coordination'],'cap')
        for item in (a,b):
            for k in ('service','resources','coordination'):finite(item[k],k)
        if not b['authorized']: status='RIGHTS_BLOCKED'
        elif b['coordination']>coord: status='COORDINATION_BLOCKED'
        elif b['service']>=a['service'] and b['resources']<=a['resources']:
            status='WEAK_PARETO_RESOURCE_SERVICE_GAIN' if (b['service']>a['service'] or b['resources']<a['resources']) else 'NO_STRICT_GAIN'
        else:status='TRADEOFF_NOT_PARETO_CERTIFIED'
        return res(status,delta_service=rnd(b['service']-a['service']),delta_resources=rnd(b['resources']-a['resources']),coordination_margin=rnd(coord-b['coordination']),authorized=b['authorized'])
    if t=='distribution':
        u=case['delta_utils']; floors=case['credit_minimums']; total=finite(case['credit_total'],'credit_total')
        if len(u)!=len(floors) or total<=0: raise ValueError('incompatible credits input')
        req=sum(finite(v,'floor') for v in floors);fine=all(v>=0 for v in u)
        return res('RELATIVE_CREDIT_FEASIBLE' if req<=total else 'RELATIVE_CREDIT_IMPOSSIBLE',absolute_pareto=fine and any(v>0 for v in u),credit_demand=req,credit_available=total,credit_shortfall=max(0,req-total))
    if t=='nonmonotone':
        vals=case['table']; start=case['start'];assert 0<=start<len(vals)
        loc=max([k for k in range(start,len(vals)) if all(vals[j]>=vals[start] for j in range(start,k+1))],default=start)
        # Local one-step monotone rule halts at first decrease.
        k=start
        while k+1<len(vals) and vals[k+1]>=vals[k]: k+=1
        opt=max(range(len(vals)),key=lambda j:vals[j]);return res('LOCAL_MONOTONE_STOP_BELOW_BETTER_STATE' if vals[opt]>vals[k] else 'NO_LOCAL_TRAP',local_stop=k,global_best=opt,local_value=vals[k],best_value=vals[opt])
    if t=='eff_gap':
        rows=[]
        for p in case['periods']:
            ac=finite(p['actual_cost'],'actual_cost');best=finite(p['ideal_same_output_cost'],'ideal')
            rows.append({'time':p['time'],'output':p['actual_output'],'gap':rnd(ac-best) if p['feasible'] and ac>=best else None,'certified_feasible':p['feasible']})
        return res('GAPS_ESTABLISHED_IN_TOY' if all(x['certified_feasible'] for x in rows) else 'OPTIMUM_NOT_ESTABLISHED',periods=rows,gap_increases=(len(rows)>1 and all(x['gap'] is not None for x in rows) and rows[-1]['gap']>rows[0]['gap']))
    if t=='net_discomfort':
        if case['stipulated_discomfort'] is None:return res('SUBJECTIVE_NOT_MEASURED',net_welfare_toy=None,subjective_measured=False)
        v=finite(case['benefit'],'benefit')-finite(case['stipulated_discomfort'],'cost')
        return res('HYPOTHETICAL_NET_NEGATIVE' if v<0 else 'HYPOTHETICAL_NET_NONNEGATIVE',net_welfare_toy=rnd(v),subjective_measured=case['subjective_measured'])
    if t=='human_time':
        keys=('GIC','NEO','ACW','UNKNOWN')
        a,r=case['actual'],case['reference'];total=sum(finite(a[k],k) for k in keys)
        if total<=0:raise ValueError('no human time')
        if not case['same_service']:return res('MATCHED_REFERENCE_MISSING',human_observation='NOT_MEASURED')
        return res('HUMAN_INPUT_DIFF_NOT_OBSERVED_HID',actual_total=rnd(total),ACW_share=rnd(a['ACW']/total),GIC_delta=rnd(r['GIC']-a['GIC']),ACW_delta=rnd(a['ACW']-r['ACW']),NEO_is_debt=False,human_observation='SYNTHETIC')
    if t=='entropy':
        prior=case['prior']
        if prior is None:return res('PRIOR_NOT_IDENTIFIED',target_entropy=None,open_exterior_entropy=None)
        if len(prior)!=len(case['projection']) or len(prior)!=len(case['target']) or abs(sum(prior)-1)>1e-9:raise ValueError('probability specification invalid')
        for p in prior:finite(p,'prior')
        if any(p<0 for p in prior):raise ValueError('negative probability')
        prjs=set(case['projection']);H=0.;HX=0.
        for y in prjs:
            ix=[i for i,z in enumerate(case['projection']) if z==y];mass=sum(prior[i] for i in ix)
            if mass<=0:continue
            group={}
            for i in ix:group[case['target'][i]]=group.get(case['target'][i],0)+prior[i]/mass
            H+=mass*shannon(group.values()); HX+=mass*shannon([prior[i]/mass for i in ix])
        return res('FINITE_SHANNON_ONLY',conditional_answer_bits=rnd(H),conditional_origin_bits=rnd(HX),strict_decision_ambiguity=H>1e-9,open_exterior_entropy=None)
    if t=='kl':
        m,n=case['m'],case['n'];
        if not(isinstance(m,int) and isinstance(n,int) and 0<n<=m):raise ValueError('kl finite support')
        return res('FINITE_SUPPORT_DIRECTION_CORRECTED',coverage_delta_bits=rnd(math.log2(m/n)),kl_P_theory_to_Q_constructible='INFINITY' if m>n else 0,kl_Q_constructible_to_P_theory=rnd(math.log2(m/n)))
    if t=='attribution':
        if case.get('requested_metric')=='E_UNRESOLVED':return res('MEASUREMENT_EDITION_CONFLICT_BLOCKED',value=None)
        listed=case['reported_dependency'];actual=case['verified_dependency'];credit=case['assigned_credit']
        return res('DEPENDENCY_ATTRIBUTION_DIVERGENCE' if listed!=actual or credit!=actual else 'CONSISTENT_IN_TOY',listed=listed,verified=actual,credited=credit)
    if t=='mission':
        if any(case.get(key) is None for key in ('actual_independent','authorized_change','source_basis_valid')):
            return res('MISSION_BASIS_NOT_ESTABLISHED',mission_change=None)
        if case['authorized_change'] and case['source_basis_valid'] and case['actual_independent']>=2:
            return res('SUPPORTED_AND_AUTHORIZED_CHANGE',mission_change=True)
        return res('UNSUPPORTED_MISSION_CHANGE',mission_change=False,nominal_sources=case['reported_independent'],source_independent=case['actual_independent'])
    if t=='q_cost':
        v=finite(case['decision_value'],'value');modes={'A_ONLY':0.0,'SOURCE_B':v-case['qualified_cost'] if case['valid_Q'] else None,'TARGETED_CONVENTIONAL':v-case['targeted_cost'],'FULL_A_EXPANSION':v-case['full_cost']}
        # A valid Q does not mean full new throughput is available in all worlds:
        # this is a stipulated maximal value conditional on a truly enabling world.
        win=max((name for name in modes if modes[name] is not None), key=lambda key:modes[key]);return res('COST_COMPARISON_IF_BENEFIT_REALIZED',net_values={k:rnd(x) if x is not None else None for k,x in modes.items()},best_mode=win,certificate_qualified=case['valid_Q'])
    if t=='closure':
        if case['L'] is None:return res('REGULARITY_NOT_ESTABLISHED',bounds=None)
        L=finite(case['L'],'L');x=finite(case['x'],'x');threshold=finite(case['threshold'],'threshold')
        lower=max(l-L*abs(x-pos) for pos,l,u in case['samples']);upper=min(u+L*abs(x-pos) for pos,l,u in case['samples'])
        if lower>upper:status='INCONSISTENT_ASSUMPTIONS'
        elif lower>=threshold:status='PREDICATE_SUPPORTED_IN_FRAME'
        elif upper<threshold:status='PREDICATE_REFUTED_IN_FRAME'
        else:status='PREDICATE_UNDETERMINED'
        return res(status,bounds=[rnd(lower),rnd(upper)],global_D_open=True)
    if t=='knowledge':
        return res('EVIDENCE_INSUFFICIENT_FOR_CLAIM' if not case['independent_evidence'] else 'REQUIRES_INDEPENDENT_VALIDATION',assertion=case['assertion'],social_fact_established=False)
    if t=='network':
        n=case['n']; E=n*(n-1)//2 if case['topology']=='dense' else n-1
        P=case['b']*n+case['alpha']*E;G=case['g']*E
        if P<=0:raise ValueError('production must be >0')
        return res('CONDITIONAL_COUNTERFACTUAL_GAP_NOT_HID',links=E,actual_production=rnd(P),hypothetical_gap=rnd(G),ratio_percent=rnd(100*G/P),joint_optimum_empirically_eligible=False)
    raise ValueError('unknown kind '+t)

def run_campaign(manifest=None):
    if manifest is None:manifest=json.loads((HERE/'CASES.json').read_text('utf-8'))
    if manifest.get('schema')!=SCHEMA:raise ValueError('schema')
    cases=manifest['cases'];ids=[x['id'] for x in cases]
    if len(set(ids))!=len(ids):raise ValueError('duplicate ID')
    if any(x['source'] not in manifest['sources'] for x in cases):raise ValueError('bad source')
    responses=[result(x) for x in cases]
    b=json.dumps(manifest,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode('utf-8')
    groups={k:sum(x['group']==k for x in cases) for k in sorted({x['group'] for x in cases})}
    return {'schema':SCHEMA,'evidence':'SYNTHETIC_NOT_EMPIRICAL','case_count':len(cases),'source_document_count':len(manifest['sources']),'input_sha256':hashlib.sha256(b).hexdigest(),'groups':groups,'results':responses,'excluded_external_validation':['human lived suffering','real estate/education/employment causality','real company attribution','physical entropy/open-D probability','UC21 native product outcomes']}

if __name__=='__main__':print(json.dumps(run_campaign(),indent=2,ensure_ascii=False,sort_keys=True))
