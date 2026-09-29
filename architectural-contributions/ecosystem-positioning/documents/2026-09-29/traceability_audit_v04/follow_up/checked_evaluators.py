"""Input admission and external-cost checks added after audit 0.4.

Preserves original evaluator semantics for admitted inputs. Rejects malformed
records instead of interpreting them as a successful decision.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import evaluators as original

def qualified_support(evidence, required):
    if len(evidence)!=3 or any(type(x) is not int or x not in (-1,0,1) for x in evidence):
        raise ValueError('Evidence outside the three-proposition domain')
    if not required or len(set(required))!=len(required) or any(type(x) is not int or x not in range(3) for x in required):
        raise ValueError('Receiving claim outside the registered domain')
    return original.entailed(evidence,required)

def charged_response(events, budget, observation_costs, response_cost):
    # Cost sources belong to the test environment, not the candidate output.
    if type(budget) is not int or budget<1 or type(response_cost) is not int or response_cost<1:
        raise ValueError('Invalid resource ledger')
    if any(type(x) is not int or x<1 for x in observation_costs):
        raise ValueError('Invalid observation charge')
    if not events or events[-1][0]!='respond':
        raise ValueError('Missing terminal response')
    if len(events)-1>len(observation_costs):
        raise ValueError('Unknown observation')
    for i,(kind,reported) in enumerate(events):
        terminal=i==len(events)-1
        expected=response_cost if terminal else observation_costs[i]
        if kind!=('respond' if terminal else 'observe') or type(reported) is not int or reported!=expected:
            raise ValueError('Record contradicts independent cost ledger')
    # Candidate-supplied charges are validated but not used for the score.
    actual=sum(observation_costs[:len(events)-1])+response_cost
    return actual<=budget

def history_violation(events, output):
    if not events or any(x not in 'QCRKAX' or len(x)!=1 for x in events):
        raise ValueError('Unknown event')
    if len(events)!=len(output) or any(type(x) is not bool for x in output):
        raise ValueError('Incomplete or untyped execution record')
    if any(ran and event!='A' for event,ran in zip(events,output)):
        raise ValueError('Execution attributed to a nonaction event')
    return original.bad_execution(events,output)

def root_separation(edges,a,b):
    if a not in range(5) or b not in range(5) or a==b:
        raise ValueError('Invalid report pair')
    if len(set(edges))!=len(edges) or any(type(u) is not int or type(v) is not int or not 0<=u<v<5 for u,v in edges):
        raise ValueError('Outside the registered forward DAG domain')
    return original.unrelated_roots(edges,a,b)
