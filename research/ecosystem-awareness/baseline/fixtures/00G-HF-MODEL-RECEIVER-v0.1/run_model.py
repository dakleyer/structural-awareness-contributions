"""Run exploratory native or matched model episodes, or record missing access."""
import argparse
from datetime import datetime,timezone
import hashlib
import json
import os
from pathlib import Path
from adapter import Client, ENDPOINT, TOOL
from runner import HERE, SCENARIO, LIMITS, ARMS, DurableJournal, episode, audit, digest, write


def verify_freeze():
    freeze=json.loads((HERE/'FREEZE.json').read_text())
    for name,expected in freeze['sha256'].items():
        if hashlib.sha256((HERE/name).read_bytes()).hexdigest()!=expected:
            raise RuntimeError('source freeze mismatch: '+name)
    return freeze


def native_witness(directory, model, freeze, cases):
    registration=json.loads((directory/'REGISTRATION.json').read_text())
    report=json.loads((directory/'REPORT.json').read_text())
    assert registration['requested_model']==model and registration['phase']=='native'
    assert registration['decision_source']=='LIVE_RESPONSES_API'
    assert registration['freeze_sha256']==digest(freeze)
    assert len(report['results'])==len(cases)
    expected={c['id']:c for c in cases}
    assert {r['case_id'] for r in report['results']}==set(expected)
    failures=[]
    for result in report['results']:
        assert result['arm']=='native'
        world=expected[result['case_id']]
        path=directory/result['case_id']/'native'/'JOURNAL.jsonl'
        rows=[json.loads(line) for line in path.read_text().splitlines()]
        audit(world,rows,result)
        if result['operational_result_eligible'] and result['outcome']['unauthorized_mission_change'] and world['family']=='primary':
            failures.append(result['case_id'])
    assert failures, 'No observed primary model failure: repair gate remains closed; preserve native success.'
    return dict(cases=failures,report_sha256=hashlib.sha256((directory/'REPORT.json').read_bytes()).hexdigest())


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--phase',choices=['native','paired'],required=True)
    parser.add_argument('--model',default=os.getenv('OPENAI_MODEL'))
    parser.add_argument('--native-run',type=Path)
    parser.add_argument('--output-dir',type=Path,required=True)
    args=parser.parse_args()
    freeze=verify_freeze()
    cases=json.loads((SCENARIO/'CASES.json').read_text())
    key=os.getenv('OPENAI_API_KEY')
    missing=[]
    if not key: missing.append('OPENAI_API_KEY_NOT_CONFIGURED')
    if not args.model: missing.append('MODEL_NOT_SELECTED')
    witness=None
    if not missing and args.phase=='paired':
        if not args.native_run:
            raise SystemExit('--native-run required for repair comparison')
        witness=native_witness(args.native_run,args.model,freeze,cases)
    arms=['native'] if args.phase=='native' else list(ARMS)
    order=[]
    for index,world in enumerate(cases):
        rotated=arms[index%len(arms):]+arms[:index%len(arms)]
        order.extend(dict(case_id=world['id'],arm=a) for a in rotated)
    args.output_dir.mkdir(parents=True,exist_ok=False)
    registration=dict(created_utc=datetime.now(timezone.utc).isoformat(),phase=args.phase,
                      decision_source='LIVE_RESPONSES_API',requested_model=args.model,
                      endpoint=ENDPOINT,store=True,freeze_sha256=digest(freeze),
                      tool_schema_sha256=digest(TOOL),limits=LIMITS,order=order,
                      repetitions=1,seed=None,negative_witness=witness,
                      state_reset='new local environment and new API conversation per episode',
                      source_visibility='PUBLIC_AUTHOR_FIXTURES_NOT_BLIND',external_validation=False,
                      private_reasoning_requested=False,registration_complete=not missing,
                      retry_policy='none; retain failures; continue registered lot',
                      clock='one logical tick per completed model turn; service/advisory charges preserved; wall time separately bounded',
                      token_limit='stop before next request at threshold; reject action if returned total exceeds threshold; final API request can overshoot billing threshold')
    write(args.output_dir/'REGISTRATION.json',registration)
    write(args.output_dir/'WORLD_INPUTS.json',cases)
    if missing:
        report=dict(status='BLOCKED_BEFORE_MODEL_EXECUTION',reasons=missing,model_requests=0,
                    model_responses=0,agent_episodes_started=0,results=[])
        write(args.output_dir/'REPORT.json',report)
        print(json.dumps(report,indent=2))
        return 2
    instructions=(HERE/'INSTRUCTIONS.txt').read_text()
    by_id={c['id']:c for c in cases}
    report=dict(status='RUNNING',model_requests=0,model_responses=0,results=[])
    write(args.output_dir/'REPORT.json',report)
    for item in order:
        destination=args.output_dir/item['case_id']/item['arm']
        destination.mkdir(parents=True,exist_ok=False)
        journal=DurableJournal(destination/'JOURNAL.jsonl')
        client=Client(args.model,key,instructions)
        result=episode(by_id[item['case_id']],item['arm'],client,journal)
        write(destination/'RESULT.json',result)
        checked=audit(by_id[item['case_id']],journal.rows,result)
        write(destination/'VERIFICATION.json',checked)
        report['results'].append(result)
        report['model_requests']+=result['model_requests']
        report['model_responses']+=result['model_responses']
        write(args.output_dir/'REPORT.json',report)
    report['status']='EXPLORATORY_MODEL_LOT_FINISHED'
    report['operational_episodes']=sum(r['operational_result_eligible'] for r in report['results'])
    report['infrastructure_interruptions']=sum(r['infrastructure_interrupted'] for r in report['results'])
    write(args.output_dir/'REPORT.json',report)
    print(json.dumps({k:v for k,v in report.items() if k!='results'},indent=2))
    return 3 if report['infrastructure_interruptions'] else 0


if __name__=='__main__':
    raise SystemExit(main())
