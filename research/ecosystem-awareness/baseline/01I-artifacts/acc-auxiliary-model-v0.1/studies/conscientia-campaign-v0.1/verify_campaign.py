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
for key in ('schema_version','date_cutoff','decision_experiments',
            'factorial_joint_mechanism','FH_C_competing_ablations','network_counterfactuals','source_anchored_microexperiments','finite_entropic_experiment',
            'human_and_measurement_blockers','uc21_case_templates_not_executed','interpretation_guard'):
    assert observed[key]==expected[key],f'Synthetic experiment reference mismatch: {key}'
# The immutable historical fixture misnamed a REGISTERED count as "screened".
# Preserve the original bytes and explicitly reconcile its meaning, without
# publishing 23 as an active text-read claim or altering synthetic verdicts.
assert 'source_documents_screened' not in observed, 'obsolete source count must not reappear'
lineage=observed['source_provenance']
counts=lineage['counts']
assert expected['source_documents_screened']==counts['registered_total']==23
assert counts['registered_google_docs']==19
assert counts['baseline_text_review_reported_cohort_only']==17
assert counts['baseline_metadata_only_reported']==2
assert counts['later_conceptual_review_reported_without_snapshot']==2
assert counts['independent_source_level_historical_text_reviews_attested']==0
assert counts['registered_sources_used_as_primary_in_frozen_cases']==10
assert counts['frozen_primary_cases']==60
assert counts['narrative_cases_with_source_refs']==40
assert counts['legacy_source_documents_screened_23_meant']=='REGISTERED_TOTAL_NOT_SCREENED_TEXT'
assert len(lineage['source_level_lineage'])==23
assert len(lineage['source_input_sha256'])==5
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
