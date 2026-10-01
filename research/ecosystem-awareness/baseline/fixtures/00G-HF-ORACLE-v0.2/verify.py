"""Run fixed author-authored controls; these are not E1 candidate-agent runs."""
import hashlib
import json
from copy import deepcopy
from pathlib import Path
from oracle import evaluate

HERE=Path(__file__).resolve().parent
freeze=json.loads((HERE/'DESIGN_FREEZE.json').read_text())
for filename, digest in freeze['sha256'].items():
    actual=hashlib.sha256((HERE/filename).read_bytes()).hexdigest()
    if actual != digest:
        raise SystemExit('Freeze mismatch: '+filename)
suite=json.loads((HERE/'controls.json').read_text())
results=[]
for case in suite['cases']:
    case=deepcopy(case)
    if case.get('mutation')=='nan_deadline': case['world']['deadline']=float('nan')
    if case.get('mutation')=='nan_horizon': case['trace']['observed_until']=float('nan')
    try:
        output=evaluate(case['world'],case['trace'])
    except Exception as exc:
        output={'unexpected_exception':type(exc).__name__, 'message':str(exc)}
    errors={key:{'expected':expected,'actual':output.get(key)}
            for key,expected in case['expected'].items()
            if key not in output or output[key] != expected}
    results.append(dict(id=case['id'],passed=not errors,errors=errors,output=output))
report=dict(status='ORACLE_CONTROL_EXECUTION_ONLY',
            public_author_design=True,externally_authored=False,blind=False,
            agent_runs=0,passed=sum(x['passed'] for x in results),total=len(results),
            freeze_sha256=hashlib.sha256((HERE/'DESIGN_FREEZE.json').read_bytes()).hexdigest(),
            results=results)
(HERE/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='results'},indent=2))
if not all(x['passed'] for x in results):
    print(json.dumps([x for x in results if not x['passed']],indent=2))
    raise SystemExit(1)
