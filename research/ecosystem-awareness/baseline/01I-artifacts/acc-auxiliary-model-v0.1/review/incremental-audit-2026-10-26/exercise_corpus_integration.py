"""Exercise the actual #44 and #46 source modules with the new reusable kernels."""
from pathlib import Path
from fractions import Fraction
from itertools import combinations
import argparse,hashlib,importlib.util,json,random,sys

from generative_development import best_joint_plan,resource_conflicts,certainty_equivalent
from corpus_development_adapter import producer_offer,common_budget


def load_module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module;spec.loader.exec_module(module);return module


def run(corpus_root):
    base=Path(corpus_root)/'research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies'
    source=base/'intrinsic-abcd-economics-v0.1/intrinsic_abcd.py'
    risk=base/'risk-aversion-persistence-v0.1/risk_model.py'
    p=load_module('_acc_development_producer',source);r=load_module('_acc_development_risk',risk)
    rng=random.Random(28102026);worlds=0;feasible_sets=0;individual_scope=0;old_sum_exceeds_joint=0
    for n in (2,4,8,16):
        for repeat in range(60):
            bits=tuple(rng.randrange(2) for _ in range(n));spare=rng.randrange(4)
            world=p.balanced_tree(bits,cap_root=8*n+spare)
            targets=(f'source-0',f'source-{n-1}')
            records=tuple(p.upstream_B(world,t,now=0,ttl=10,extra=2) for t in targets)
            offers=tuple(producer_offer(p,world,rec,now=0) for rec in records)
            budget=common_budget(offers);actions=tuple(o[0] for o in offers)
            baseline=p.base_demand(world);before=p.deliver(world,baseline)
            full=dict(baseline)
            for t in targets:full[t]+=2
            old_sum_exceeds_joint+=sum(rec.delivered_if_requested for rec in records)>p.deliver(world,full)-before
            for rec in records:
                assert p.receiver_B_valid(p.public_outline(world),rec,rec.target,now=0,extra=2)[0]
                individual_scope+=1
            for count in range(3):
                for chosen in combinations(actions,count):
                    if resource_conflicts(chosen,budget):continue
                    demand=dict(baseline)
                    for action in chosen:demand[action.name]+=int(action.gain)
                    actual=p.deliver(world,demand)-before
                    assert actual==sum(action.gain for action in chosen),(world,chosen,actual)
                    feasible_sets+=1
            plan=best_joint_plan(actions,budget)
            assert not resource_conflicts(plan,budget);worlds+=1
    risk_cases=0
    for mu in (-2,0,3,5):
        for variance in (0,1,4):
            for gamma in (0,0.5,1,2):
                actual=r.certainty_equivalent(r.RiskOutcome(float(mu),float(variance)),float(gamma))
                assert certainty_equivalent(mu,variance,gamma)==Fraction(actual)
                risk_cases+=1
    blob=lambda path:hashlib.sha1(b'blob '+str(len(path.read_bytes())).encode()+b'\0'+path.read_bytes()).hexdigest()
    return {'source_blobs':{source.relative_to(corpus_root).as_posix():blob(source),risk.relative_to(corpus_root).as_posix():blob(risk)},
            'source_worlds':worlds,'existing_individual_scope_checks':individual_scope,
            'source_feasible_action_sets_exact_gain':feasible_sets,'old_sum_overcommitments':old_sum_exceeds_joint,
            'source_risk_equivalent_cases':risk_cases,'status':'PASS'}


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--corpus-root',type=Path,required=True);args=ap.parse_args()
    print(json.dumps(run(args.corpus_root),indent=2))
