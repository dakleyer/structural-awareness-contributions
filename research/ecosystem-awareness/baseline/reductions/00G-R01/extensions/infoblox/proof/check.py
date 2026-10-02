"""Exact finite MODEL check, not an Infoblox/DNS deployment test.
Python 3 standard library only. Run: python3 check.py
Costs are synthetic work units; identities and transport are modeled as valid.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json, hashlib

def subsets(n):
    for k in range(n+1):
        yield from combinations(range(n),k)

def weights(n):
    return (F(1,2),)+(F(1,2*n),)*n

def allowed(world,j):
    return world != j+1

def best_success(n,budget,strict=False,certificate=False):
    """Enumerate all adaptive choices by exact belief-state dynamic programming.
    Optimistic mode may commit A without full proof; strict mode cannot.
    Certificate mode adds a sufficient, scoped aggregate at unit access cost.
    """
    prior=weights(n)
    @lru_cache(None)
    def solve(possible,seen,left):
        mass=sum(prior[w] for w in possible)
        a=prior[0] if 0 in possible else F(0)
        b=mass-a
        # Delivering B succeeds precisely in the worlds where A is disallowed.
        choices=[b]
        if not strict or len(seen)==n or 0 not in possible:
            choices.append(a)
        if left:
            if certificate:
                choices.append(mass) # true aggregate selects A or B correctly
            for j in range(n):
                if j in seen:continue
                total=F(0)
                for ans in (False,True):
                    group=tuple(w for w in possible if allowed(w,j)==ans)
                    if group:total+=solve(group,tuple(sorted(seen+(j,))),left-1)
                choices.append(total)
        return max(choices)
    return solve(tuple(range(n+1)),(),budget)

def compile_world(n,world,sigma,tau):
    """Domain encoding: four alternative chains, no cross-chain connectors.
    Directory contains all operations. No search restriction supplies the bound.
    Receipts are transparent model records, not cryptographic objects.
    """
    terms=[F(2*j-(n-1),max(1,n-1)) for j in range(n)]
    routes={};store={};catalog=[]
    for route,mu in [('M',1),('B',2),('A',3),('C',4)]:
        ops=[]
        for j in range(n):
            rid=hashlib.sha256(f'{route}:{j}'.encode()).hexdigest()[:12]
            ops.append({'id':rid,'benefit':str(F(mu)+sigma*terms[j]),
                        'position':str(F(0) if route=='M' else F(mu+2)+tau*terms[j]),
                        'next':None,'source':rid+'.source'})
            permit=allowed(world,j) if route=='A' else route!='C'
            store[rid+'.source']={'source':rid+'.source','mission':'dns-diagnosis',
                'recipient':'specialist.example','version':1,'permitted':permit}
            catalog.append({'id':rid,'endpoint':'https://'+rid+'.example',
                'identity_verified':True,'discovery_integrity_verified':True,
                'intent':'dns-diagnosis','trust_signal':90})
        for j in range(n-1):ops[j]['next']=ops[j+1]['id']
        routes[route]=ops
    return {'routes':routes,'catalog':catalog,'permission_store':store}

def app_verdict(app,route):
    ops=app['routes'][route]
    ok=all(app['permission_store'][o['source']]['permitted'] for o in ops)
    return ok,sum(F(o['benefit']) for o in ops)

def gateway(app,route,receipts,version=1):
    # Full evidence is mandatory; missing/false/wrong-scope evidence is denied.
    for op in app['routes'][route]:
        r=receipts.get(op['source'])
        if not r or r['source']!=op['source'] or not r['permitted']:return False
        if (r['mission'],r['recipient'],r['version'])!=('dns-diagnosis','specialist.example',version):return False
    return True

def run():
    counts={'route_preservation':0,'complete_view_pairs':0,'metadata_invariance':0,
            'gateway_checks':0,'population_cost_checks':0,'dp_values':0,
            'benefit_and_distance_profiles':0,'relay_coverage_checks':0}
    curves=[]
    for n in (2,4,8):
        for budget in range(n+1):
            optimistic=best_success(n,budget)
            strict=best_success(n,budget,strict=True)
            certified=best_success(n,budget,strict=True,certificate=True)
            assert optimistic==F(1,2)+F(budget,2*n)
            assert strict==(F(1) if budget==n else F(1,2))
            assert certified==(F(1) if budget else F(1,2))
            counts['dp_values']+=3
            curves.append({'U':n,'budget':budget,'optimistic_upper_bound':str(optimistic),
                'strict_gate_success':str(strict),'with_unit_cost_scoped_certificate':str(certified)})
        for sigma in (F(0),F(1,4)):
            for tau in (F(0),F(1,2)):
                apps=[compile_world(n,w,sigma,tau) for w in range(n+1)]
                for world,app in enumerate(apps):
                    assert app['catalog']==apps[0]['catalog'];counts['metadata_invariance']+=1
                    for route,mu in [('M',1),('B',2),('A',3),('C',4)]:
                        ref_ok=(world==0) if route=='A' else route!='C'
                        assert app_verdict(app,route)==(ref_ok,F(mu*n))
                        counts['route_preservation']+=1
                        dist=[F(o['position']) for o in app['routes'][route]]
                        assert sum(dist)/n==(F(0) if route=='M' else F(mu+2))
                        if route!='M':assert max(dist)-min(dist)==2*tau
                        vals=[F(o['benefit']) for o in app['routes'][route]]
                        assert max(vals)-min(vals)==2*sigma
                        counts['benefit_and_distance_profiles']+=1
                    assert max((app_verdict(app,r)[1],r) for r in app['routes'] if app_verdict(app,r)[0])[1]==('A' if world==0 else 'B')
                    assert not gateway(app,'A',{})
                    full={o['source']:app['permission_store'][o['source']] for o in app['routes']['A']}
                    assert gateway(app,'A',full)==(world==0)
                    assert not gateway(app,'A',full,version=2)
                    bfull={o['source']:app['permission_store'][o['source']] for o in app['routes']['B']}
                    assert gateway(app,'B',bfull)
                    counts['gateway_checks']+=4
                    for agents in (1,2,4):
                        assigned=[list(range(a,n,agents)) for a in range(agents)]
                        assert sorted(j for jobs in assigned for j in jobs)==list(range(n))
                        assert sum(map(len,assigned))==n # shared acquisition, no N*n inflation
                        counts['population_cost_checks']+=1
                        first=app['routes']['A'][0]['source']
                        shared={first:app['permission_store'][first]}
                        relayed={k:v for _ in range(agents) for k,v in shared.items()}
                        assert len(relayed)==1
                        assert not gateway(app,'A',relayed)
                        counts['relay_coverage_checks']+=1
                # Full declared view includes public recipes/catalog and all queried records.
                for s in subsets(n):
                    if len(s)==n:continue
                    omitted=next(j for j in range(n) if j not in s)
                    w0,w1=apps[0],apps[omitted+1]
                    def view(app):
                        return (app['routes'],app['catalog'],[
                            app['permission_store'][app['routes']['A'][j]['source']] for j in s])
                    assert view(w0)==view(w1)
                    assert app_verdict(w0,'A')[0]!=app_verdict(w1,'A')[0]
                    counts['complete_view_pairs']+=1
    result={'status':'all_assertions_passed','scope':'finite synthetic model only; no vendor APIs, DNS traffic, cryptography or LLM agents executed',
            'prior':'valid world probability 1/2; each single invalid condition probability 1/(2U)',
            'counts':counts,'curves':curves,
            'finding':'Sufficient scoped aggregate certificate removes the query obstruction in the modeled hot-cache regime.'}
    p=Path(__file__).with_name('results.json');p.write_text(json.dumps(result,indent=2))
    print(json.dumps({'status':result['status'],'counts':counts},indent=2))
if __name__=='__main__':run()
