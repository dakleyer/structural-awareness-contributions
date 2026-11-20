"""Verify synthetic agentic reduction is reproducible without hidden changes.

This cannot authenticate Google Docs or actual vendors; it validates only the
published fixture, equations and self-contained outputs for CI review.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
from agentic_reduction import report
from sensitivity import run_sweep

HERE=Path(__file__).resolve().parent
expected=json.loads((HERE/'REFERENCE_SYNTHETIC_RESULTS.json').read_text('utf-8'))
observed=report()
assert expected==observed, 'Agentic reference has changed: abort without silently replacing outcomes'
exp_sweep=json.loads((HERE/'REFERENCE_SWEEP.json').read_text('utf-8'))
sweep=run_sweep()
assert exp_sweep==sweep, 'Sensitivity reference changed: publish new revision instead of overwriting'
assert observed['cases']==30 and observed['policy_decisions']==180
assert sweep['n_cases']==160
assert all(sweep['exclusive_winners'][k]>0 for k in ('A_ONLY','Q_META_PROTOCOL','CONVENTIONAL_DIRECTED'))
if len(sys.argv)>1:
    Path(sys.argv[1]).write_text(json.dumps(observed,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
if len(sys.argv)>2:
    Path(sys.argv[2]).write_text(json.dumps(sweep,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':True,'cases':observed['cases'],'arm_decisions':observed['policy_decisions'],
    'factorial_sensitivity_cases':sweep['n_cases'],'winner_classes':sweep['exclusive_winners'],
    'human_suffering_measured':False,'real_agent_product_executed':False},sort_keys=True))
