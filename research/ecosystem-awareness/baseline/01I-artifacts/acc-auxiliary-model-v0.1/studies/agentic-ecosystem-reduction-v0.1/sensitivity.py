"""Factorial REGIME comparison of agentic Q, strong conventional peer, A-only.

Everything is a synthetic what-if with assumed prices and source measurements.
"""
from __future__ import annotations
from copy import deepcopy
import json
from pathlib import Path
from agentic_reduction import report, run_case

HERE=Path(__file__).resolve().parent
BASE={s['id']:s for s in json.loads((HERE/'CASES.json').read_text())['cases']}['AG01-QUALIFIED-NEAR-OPTIMUM']


def run_sweep() -> dict:
    scenarios=[]
    for true_rate in (0.6,2.0):
        for overhead in (0.1,0.25,0.5,0.75,1.5):
            for qcost in (0.05,0.3,0.8,1.5):
                for peer_cost in (0.1,1.0,3.0,5.0):
                    s=deepcopy(BASE)
                    s['id']=f'SW-{true_rate}-{overhead}-{qcost}-{peer_cost}'
                    s['truth_private']['recipient_incremental_rate']=true_rate
                    s['public']['overhead_resources']=overhead
                    s['Q']['lower_rate']=1.6 if true_rate==2.0 else 0.5
                    s['Q']['cost']=qcost
                    s['directed']['measured_rate']=true_rate
                    s['directed']['cost']=peer_cost
                    s['full_A']['fully_measured_rate']=true_rate
                    case=run_case(s)
                    gains={key:round(case['arms'][key]['mission_net_value_after_information_cost'] -10,4)
                           for key in ('A_ONLY','Q_META_PROTOCOL','CONVENTIONAL_DIRECTED')}
                    mx=max(gains.values())
                    winner=tuple(key for key,val in gains.items() if val==mx)
                    scenarios.append({'id':s['id'],'rate_PRIVATE_for_score':true_rate,
                        'coordination_resources':overhead,'Q_cost':qcost,'conventional_directed_cost':peer_cost,
                        'net_gain_vs_A_only':gains,'best_arms':list(winner),
                        'Q_improvement_physical':case['arms']['Q_META_PROTOCOL']['observed_by_referee_only']['output']>10,
                        'peer_improvement_physical':case['arms']['CONVENTIONAL_DIRECTED']['observed_by_referee_only']['output']>10})
    summary={arm:sum(arm in s['best_arms'] for s in scenarios)
             for arm in ('A_ONLY','Q_META_PROTOCOL','CONVENTIONAL_DIRECTED')}
    exclusive={arm:sum(s['best_arms']==[arm] for s in scenarios) for arm in summary}
    return {'schema':'ACC-AGENTIC-PARAM-SWEEP-v0.1','n_cases':len(scenarios),
            'param_ranges':{'truth_rate':[0.6,2.0],'coordination_overhead':[0.1,0.25,0.5,0.75,1.5],
             'Q_price':[0.05,0.3,0.8,1.5],'directed_peer_price':[0.1,1.0,3.0,5.0]},
            'co_best_counts':summary,'exclusive_winners':exclusive,'scenarios':scenarios,
            'warning':'SYNTHETIC PARAMETER GRID, not observed relative costs or prevalence; truthful B assumed except adverse cases in base suite.'}

if __name__=='__main__':print(json.dumps(run_sweep(),sort_keys=True,indent=2))
