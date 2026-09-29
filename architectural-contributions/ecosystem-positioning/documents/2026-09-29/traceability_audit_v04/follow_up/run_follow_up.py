"""Additional review. Run python3 follow_up/run_follow_up.py from package root."""
import json
from itertools import product
from pathlib import Path
import sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent))
import candidates as c
import evaluators as old
import checked_evaluators as checked

def rejects(fn,*args):
    try:fn(*args)
    except ValueError:return True
    return False

def main():
    malformed={
      'invalid_evidence_vacuity':rejects(checked.qualified_support,(2,2,2),[0]),
      'empty_receiving_claim':rejects(checked.qualified_support,(1,1,1),[]),
      'forged_response_charge':rejects(checked.charged_response,[('observe',1),('respond',0)],1,[1],1),
      'omitted_observation_charge':rejects(checked.charged_response,[('observe',0),('respond',1)],1,[2],1),
      'response_without_final_position':rejects(checked.charged_response,[('respond',1),('observe',1)],2,[1],1),
      'unreported_execution_suffix':rejects(checked.history_violation,'QCA',[False]),
      'execution_during_nonaction':rejects(checked.history_violation,'QQ',[False,True]),
      'untyped_execution_record':rejects(checked.history_violation,'QA',[False,1]),
      'unknown_event':rejects(checked.history_violation,'QZA',[False,False,True]),
      'cyclic_source_graph':rejects(checked.root_separation,[(0,1),(1,0)],0,1),
      'unknown_report':rejects(checked.root_separation,[],0,5)}
    assert all(malformed.values())
    p1=0
    for facts in product((-1,0,1),repeat=3):
        for mask in range(1,8):
            claim=[i for i in range(3) if mask & (1<<i)]
            assert checked.qualified_support(facts,claim)==old.entailed(facts,claim)
            p1+=1
    p2=0
    for n in range(1,6):
        for costs in product(range(1,5),repeat=n):
            for budget in range(1,9):
                for response in range(1,min(3,budget)+1):
                    good=c.schedule(costs,budget,response)
                    bad=c.schedule(costs,budget,response,True)
                    assert checked.charged_response(good,budget,costs,response)
                    assert checked.charged_response(bad,budget,costs,response)==old.timely(bad,budget)
                    p2+=1
    p5=0
    for n in range(1,8):
        for events in product('QCRKAX',repeat=n):
            output=c.execution(events)
            assert checked.history_violation(events,output)==old.bad_execution(events,output)
            p5+=1
    continuity={t:c.execution(t)[-1] for t in ('QA','QCQA','QCRA')}
    assert continuity=={'QA':True,'QCQA':True,'QCRA':False}
    # A represented ancestry graph with two roots can coexist with correlated
    # observed source values. The graph says nothing about this joint law.
    root_pair_separate=checked.root_separation([],0,1)
    joint_values=[(0,0),(1,1)]
    p_a=sum(a==1 for a,b in joint_values)/len(joint_values)
    p_b=sum(b==1 for a,b in joint_values)/len(joint_values)
    p_ab=sum(a==1 and b==1 for a,b in joint_values)/len(joint_values)
    assert root_pair_separate and p_ab!=p_a*p_b
    old_results=json.loads((HERE.parent/'results.json').read_text())
    obs=old_results['H4_observation_limit']
    assert obs['total_decoders']==4 and all(len(d['incompatible_contexts'])==2 for d in obs['deterministic_decoders'])
    result=dict(malformed_records_rejected=malformed,
       valid_domain_scores_preserved={'P1':p1,'P2':p2,'P5_atomic_extended_domain':p5},
       continuity_controls=continuity,
       structural_vs_statistical_independence={'root_disjoint':root_pair_separate,'joint_probability':p_ab,'product_of_marginals':p_a*p_b,'conclusion':'Graph-root separation does not imply statistical independence without an additional model assumption.'},
       H4_decoder_counts_checked=True,
       scope='Input hardening and explicit assumptions; no new empirical H1-H6 or all-six HC/HS validation.')
    (HERE/'follow_up_results.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
