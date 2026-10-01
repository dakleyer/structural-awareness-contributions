"""Execute frozen author cases; store all outputs separately from model evidence."""
import argparse
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

from component import assess

HERE = Path(__file__).resolve().parent
FREEZE_SHA = '30801c8e95a47310328e72896c87f9835def43a4c44a1a1629552b7cad54d27c'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def get(obj, path):
    for key in path.split('.'):
        obj = obj[key]
    return obj


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    if sha(HERE/'FIXTURE_FREEZE.json') != FREEZE_SHA:
        raise RuntimeError('fixture commitment changed')
    freeze = json.loads((HERE/'FIXTURE_FREEZE.json').read_text())
    for name, expected in freeze['sha256'].items():
        if sha(HERE/name) != expected:
            raise RuntimeError('frozen fixture changed: '+name)
    cases = json.loads((HERE/'CASES.json').read_text())
    args.output_dir.mkdir(parents=True, exist_ok=False)
    write(args.output_dir/'REGISTRATION.json', {
        'status':'LOCAL_AUTHOR_COMPONENT_RUN_NOT_BLIND_OR_EXTERNAL',
        'created_utc':datetime.now(timezone.utc).isoformat(), 'python':sys.version,
        'fixture_freeze_sha256':FREEZE_SHA,
        'code_sha256':{n:sha(HERE/n) for n in ('component.py','verify.py')},
        'case_ids':[r['id'] for r in cases['cases']],
        'extra_checks':['identical_view_pair','four_invalid_views','three_stipulated_consumer_policies'],
        'model_requests':0,'real_agent_episodes':0,'C3_oracle_evaluations':0,
    })
    results, outputs = [], {}
    for row in cases['cases']:
        view = deepcopy(row['view'])
        result = assess(view)  # Only the view, never the id/expected/hidden fields.
        checks = {k:get(result,k)==v for k,v in row['expected'].items()}
        checks.update({'input_not_modified':view==row['view'],
                       'scope_preserved':result['decision']==row['view']['decision'],
                       'authority_not_created':result['authority_effect']=='NONE',
                       'residual_preserved':bool(result['residual']),
                       'no_temporal_change_claim':result['temporal_change_assessed'] is False})
        outputs[row['id']] = result
        results.append({'id':row['id'],'passed':all(checks.values()),'checks':checks,'actual':result})
    supplemental=[]
    indexed={r['id']:r for r in cases['cases']}
    for left,right in cases['paired_identical_views']:
        passed=(indexed[left]['view']==indexed[right]['view'] and
                outputs[left]==outputs[right] and
                indexed[left]['hidden_evaluator']['mandate_valid_at_action'] != indexed[right]['hidden_evaluator']['mandate_valid_at_action'])
        supplemental.append({'id':'information_limit_'+left+'_'+right,'passed':passed,
            'meaning':'Same observation produces same qualification despite different hidden truth; no hidden-change detection demonstrated.'})
    invalid=[]
    v=deepcopy(cases['cases'][0]['view']);v['now']=True;invalid.append(('boolean_clock',v))
    v=deepcopy(cases['cases'][0]['view']);v['reports']*=33;invalid.append(('over_budget_records',v))
    v=deepcopy(cases['cases'][0]['view']);v['oracle_verdict']='PASS';invalid.append(('unexpected_top_level_field',v))
    v=deepcopy(cases['cases'][0]['view']);v['checks'][0]['name']=[];invalid.append(('malformed_check_name',v))
    for name, view in invalid:
        try:
            assess(view)
            rejected=False
        except ValueError:
            rejected=True
        supplemental.append({'id':name,'passed':rejected,'meaning':'Input rejected, no success signal.'})
    # These policies are intentionally stipulated, not actions observed from a model.
    signal=outputs['N01']
    signal_requests_recheck=(signal['posture']=='REQUALIFY' and signal['timely'])
    actual_permission=indexed['N01']['view']['checks'][0]['value']
    consumers=[('follows_signal',not signal_requests_recheck,False),
               ('ignores_signal',True,True),
               ('conventional_guard_without_EA',actual_permission,False)]
    for name, attempts, expected_attempt in consumers:
        supplemental.append({'id':name,'passed':attempts==expected_attempt,
            'attempted_in_stipulated_toy_policy':attempts,
            'meaning':'Conditional toy policy only; no native task completion, tool effect or agent decision observed.'})
    write(args.output_dir/'OUTPUTS.json',results)
    write(args.output_dir/'SUPPLEMENTAL.json',supplemental)
    passed=sum(r['passed'] for r in results)
    passed_extra=sum(r['passed'] for r in supplemental)
    report={'status':'AUTHOR_COMPONENT_CHECKS_COMPLETED','case_checks':{'passed':passed,'total':len(results)},
        'supplemental_checks':{'passed':passed_extra,'total':len(supplemental)},
        'model_requests':0,'real_agent_episodes':0,'C3_oracle_evaluations':0,
        'temporal_change_detector_implemented':False,'empirical_E1_E3_closed':False,
        'observed_limit':'L01/L02 identical output cannot distinguish hidden valid/revoked authority.',
        'consumer_limit':'A correct signal does not stop the stipulated ignoring consumer; native guard can already suffice.',
        'files_sha256':{n:sha(args.output_dir/n) for n in ('REGISTRATION.json','OUTPUTS.json','SUPPLEMENTAL.json')}}
    write(args.output_dir/'REPORT.json',report)
    print(json.dumps(report,indent=2))
    return 0 if passed==len(results) and passed_extra==len(supplemental) else 1


if __name__=='__main__':
    raise SystemExit(main())
