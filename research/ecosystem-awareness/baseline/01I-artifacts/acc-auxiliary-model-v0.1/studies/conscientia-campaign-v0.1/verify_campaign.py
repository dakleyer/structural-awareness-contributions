"""Re-run the campaign and compare frozen fixtures with prior source studies.

GitHub CI must execute this with all sibling PR study directories present.
"""
from __future__ import annotations
from pathlib import Path
import json
import sys
from campaign import build_campaign, report_summary

HERE=Path(__file__).resolve().parent
expected=json.loads((HERE/'REFERENCE_SYNTHETIC_RESULTS.json').read_text(encoding='utf-8'))
observed=build_campaign(require_existing=True)
# The synthetic decision/factorial/entropy experiment is an exact fixture replay.
for key in ('schema_version','date_cutoff','source_documents_screened','decision_experiments',
            'factorial_joint_mechanism','FH_C_competing_ablations','network_counterfactuals','finite_entropic_experiment',
            'human_and_measurement_blockers','uc21_case_templates_not_executed','interpretation_guard'):
    assert observed[key]==expected[key],f'Synthetic experiment reference mismatch: {key}'
# Prior artefacts are executed again: source code and pinned reference both checked.
assert len(observed['existing_synthetic_replays'])==4
for name,outcome in observed['existing_synthetic_replays'].items():
    assert outcome['status']=='SYNTHETIC_REPLAY_MATCH',(name,outcome)
assert observed['uc21_synthetic_adapter']['status']=='SYNTHETIC_ADAPTER_REPLAY'
assert observed['uc21_synthetic_adapter']['native_product']=='NOT_RUN'
assert observed['uc21_synthetic_adapter']['uc21_hr_existential_six_case_conclusion']=='NOT_REFUTED_OR_PROVED_BY_NONEXHAUSTIVE_RUNS'
output=Path(sys.argv[1]) if len(sys.argv)>1 else HERE/'FULL_EXECUTION.json'
output.write_text(json.dumps(observed,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf-8')
md=output.with_suffix('.md')
md.write_text(report_summary(observed),encoding='utf-8')
print(json.dumps({'passed':True,'scenario_cases':observed['decision_experiments']['case_count'],
                  'arm_decisions':observed['decision_experiments']['arm_decisions'],
                  'prior_studies_replayed':len(observed['existing_synthetic_replays']),
                  'UC21_synthetic_only':True,'full_result_path':str(output)},sort_keys=True))
