"""Check frozen author controls and exact preservation of every C1 output."""
import hashlib
import json
from copy import deepcopy
from pathlib import Path
from core import evaluate as evaluate_core
from oracle import evaluate

HERE=Path(__file__).resolve().parent
if not __debug__:
    raise SystemExit('Use standard Python without -O: the preserved C1 validator uses assertions.')
freeze=json.loads((HERE/'DESIGN_FREEZE.json').read_text())
for name,digest in freeze['sha256'].items():
    if hashlib.sha256((HERE/name).read_bytes()).hexdigest()!=digest:
        raise SystemExit('Freeze mismatch: '+name)
results=[]
for filename in ('controls.json','extension_controls.json','round1_controls.json'):
    for original in json.loads((HERE/filename).read_text())['cases']:
        case=deepcopy(original)
        if case.get('mutation')=='nan_deadline': case['world']['deadline']=float('nan')
        if case.get('mutation')=='nan_horizon': case['trace']['observed_until']=float('nan')
        if case.get('assessment_mutation')=='nan_response':
            case['assessment']['timing']['response_effective_at']=float('nan')
        try:
            output=evaluate(case['world'],case['trace'],case.get('assessment'))
            expectations=case.get('expected_paths',case.get('expected',{}))
            errors={}
            for path,expected in expectations.items():
                actual=output
                try:
                    for part in path.split('.'):
                        actual=actual[int(part)] if isinstance(actual,list) else actual[part]
                except (KeyError,TypeError,IndexError,ValueError): actual='MISSING'
                if actual!=expected: errors[path]={'expected':expected,'actual':actual}
            baseline=evaluate_core(case['world'],case['trace'])
            kept={k:v for k,v in output.items() if k not in ('scope','population_result','assessment')}
            if kept!=baseline: errors['core_regression']='C1 outcome changed'
        except Exception as exc:
            errors={'unexpected_exception':repr(exc)}
            output={}
        results.append({'id':case['id'],'passed':not errors,'errors':errors,'output':output})
report={'status':'AUTHOR_ORACLE_CONTROLS_ONLY','agent_runs':0,'human_annotation_runs':0,
        'blind':False,'externally_authored':False,'historical_replay':False,
        'passed':sum(r['passed'] for r in results),'total':len(results),
        'preserved_controls':60,'supplementary_controls':28,'round1_controls':14,'scenario_cells':6,
        'freeze_sha256':hashlib.sha256((HERE/'DESIGN_FREEZE.json').read_bytes()).hexdigest(),
        'results':results}
(HERE/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='results'},indent=2))
if not all(r['passed'] for r in results):
    print(json.dumps([r for r in results if not r['passed']],indent=2))
    raise SystemExit(1)
