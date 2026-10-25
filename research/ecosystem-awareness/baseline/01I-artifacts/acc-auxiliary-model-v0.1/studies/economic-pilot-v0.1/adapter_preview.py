"""Documentary staging only: never assigns a UC21 or R01 source verdict."""
from pathlib import Path
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parent
REPO = next(p for p in ROOT.parents if (p / '.git').exists() or (p / 'DOCUMENT_CONTROL.md').exists())
SOURCE = Path('governance/preserved-public-snapshots/UC21_aec08fb5_source/contributions/when-controls-work-system-fails/annexes/scenarios/S5.md')


def export_preview(result_file, trace_file):
    result = json.loads(result_file.read_text(encoding='utf8'))
    events = [json.loads(line) for line in trace_file.read_text(encoding='utf8').splitlines() if line]
    selected = [e for e in events if e['case_id'] in ['T02', 'T03', 'T04']]
    return {
        'adapter_version':'ACC-AUX-DDS-S5-0.1',
        'status':'DOCUMENTARY_PREPARATION_ONLY',
        'model_study_id':result['study_id'],
        'source':{'repository':'dakleyer/use-cases','revision_label':'aec08fb5',
            'scenario':'S5 / 00I','local_preserved_snapshot':SOURCE.as_posix(),
            'snapshot_sha256':hashlib.sha256((REPO/SOURCE).read_bytes()).hexdigest()},
        'source_case_assessment':'NOT_RUN', 'native_executor_connected':False,
        'source_comparison_routes':{'R0':'NOT_MAPPED','R1':'NOT_MAPPED','R2':'NOT_MAPPED'},
        'R01':'NOT_REQUIRED_FOR_THIS_PILOT',
        'model_results':[{k:r[k] for k in ['case_id','policy','scenario_outcome','actual_effects','invalid_attempts']} for r in result['runs'] if r['case_id'] in ['T02','T03','T04']],
        'staging_events':[{k:e[k] for k in ['case_id','policy','tick','job','phase','action','attempted','effect','effect_legitimate','violations']} for e in selected],
        'limits':['Logical toy time is not the source 14:02/14:42 clock',
            'Fictitious monetary net is not a database-effect oracle',
            'Model policy names do not rename source R0/R1/R2 or R01 M/I/P',
            'Source acceptance and native execution remain unassessed'],
    }


if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output-dir',type=Path,default=ROOT/'results')
    args=p.parse_args()
    preview=export_preview(ROOT/'results/results.json',ROOT/'results/traces.jsonl')
    args.output_dir.mkdir(parents=True,exist_ok=True)
    (args.output_dir/'adapter_preview.json').write_text(json.dumps(preview,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps({'status':preview['status'],'source_case_assessment':preview['source_case_assessment'],'staging_events':len(preview['staging_events'])}))
