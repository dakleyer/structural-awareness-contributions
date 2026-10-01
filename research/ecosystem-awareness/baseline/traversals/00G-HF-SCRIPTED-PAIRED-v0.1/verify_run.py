"""Check recorded paired evidence independently of policy/component implementation."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
BASE=HERE.parent.parent
sys.path.insert(0,str(BASE/'fixtures/00G-HF-NATIVE-v0.1'))
from native import digest
from run_pilot import verify_oracle


def read(path):
    return json.loads(path.read_text())


def check_path(directory, world, arm, registration, evaluate):
    rows=[json.loads(line) for line in (directory/'JOURNAL.jsonl').read_text().splitlines()]
    trace=read(directory/'TRACE.json')
    result=read(directory/'RESULT.json')
    previous='0'*64
    for seq,row in enumerate(rows):
        copy=dict(row)
        claimed=copy.pop('sha256')
        assert copy['seq']==seq and copy['previous']==previous and digest(copy)==claimed,'recorder chain'
        previous=claimed
    assert previous==result['journal_chain_head'],'chain head'
    assert rows[0]['kind']=='world' and rows[0]['value']==world,'frozen world'
    assert [r['value'] for r in rows if r['kind']=='event']==trace['events'],'event coverage'
    assert evaluate(world,trace)==result['oracle_result'],'independent oracle replay'
    initial=next(r['value'] for r in rows if r['kind']=='public_initial_view')
    pending=None
    calls=[]
    native_ticks=0
    latest={}
    emitted={}
    received={}
    charges={'response_ticks':0,'EA_processing_ticks':0,'EA_transport_ticks':0}
    decisions=[]
    inspected={}
    accepted=[]
    for row in rows:
        kind,value=row['kind'],row['value']
        if kind=='tool_request':
            assert pending is None,'overlapping tools'
            pending=value
        elif kind=='tool_response':
            assert pending is not None,'response without request'
            request=pending
            response=value['result']
            calls.append({'request':request,'response':value})
            assert value['at']>=request['at'],'backward call clock'
            native_ticks+=value['at']-request['at']
            if request['action'] in ('authority','applicability','reports'):
                latest[request['action']]=response
            if request['action']=='inspect' and response.get('status')=='executed':
                inspected[response['attempt_id']]=response['records']
            if request['action']=='submit' and response.get('accepted') is True:
                assert request['attempt_id'] in inspected,'unbacked submission'
                assert request['total']==sum(inspected[request['attempt_id']]),'incorrect submitted output'
                accepted.append({'task':request['task'],'at':value['at'],'attempt':request['attempt_id']})
            pending=None
        elif kind=='clock_charge':
            assert value['kind'] in charges and value['to']-value['from']==value['charged_ticks'],'clock cost'
            charges[value['kind']]+=value['charged_ticks']
        elif kind=='signal_emitted':
            assert arm=='native_ea' and value['id'] not in emitted,'unexpected/duplicate signal'
            assert value['signal']['current']['emitted_at']==value['at'],'signal emission time'
            # Projection must preserve absent native metadata instead of inventing leases.
            snap=value['projection']['snapshot']
            assert snap['view']['checks']==[],'invented interval check'
            assert all(p['version'] is None and p['valid_until'] is None for p in snap['point_observations']),'invented source metadata'
            emitted[value['id']]=value
        elif kind=='signal_received':
            assert value['id'] in emitted and value['id'] not in received,'signal delivery'
            signal=emitted[value['id']]['signal']
            assert digest(signal)==value['sha256'] and value['at']==signal['current']['received_at'],'signal byte/time receipt'
            received[value['id']]=value
        elif kind=='scripted_decision':
            assert value['public_input']=={'initial':initial,'responses':latest},'policy view not actual public responses'
            if arm=='native_ea':
                assert value['signal_id'] in received and value['choice']['EA_consumed'] is True,'unconsumed signal'
                assert received[value['signal_id']]['at']<=value['at'],'decision before signal receipt'
            else:
                assert value['signal_id'] is None and value['choice']['EA_consumed'] is False,'EA in native arm'
            decisions.append(value)
    assert pending is None,'missing tool response'
    assert len(calls)==result['tool_calls'] and native_ticks==result['cost_ticks']['native_tool_ticks'],'tool ledger'
    assert all(result['cost_ticks'][k]==v for k,v in charges.items()),'processing ledger'
    assert sum(result['cost_ticks'].values())==result['logical_elapsed_ticks']==result['final_tick']-initial['now'],'total ledger'
    assert result['signals_emitted']==len(emitted) and result['signals_received']==len(received),'signal counts'
    assert result['scripted_decisions']==len(decisions),'decision count'
    assert result['model_requests']==result['model_decisions']==0,'false model claim'
    if arm=='native':
        assert charges['EA_processing_ticks']==charges['EA_transport_ticks']==0,'EA cost in native'
    else:
        assert len(emitted)==len(received)==len(decisions),'incomplete signal consumption'
    oracle=evaluate(world,trace)
    times=[a['at'] for a in accepted if a['task']==world['required_completion']]
    margin=world['deadline']-max(times) if times else None
    task_pass=bool(oracle.get('operational_pass') is True and times and margin>0
                   and len(calls)<=registration['limits']['tool_calls']
                   and result['cycles']<=registration['limits']['cycles']
                   and result['wall_seconds']<=registration['limits']['wall_seconds']
                   and result['status']=='SCRIPTED_PATH_OBSERVED')
    assert task_pass==result['registered_task_pass'],'task verdict'
    assert (max(times) if times else None)==result['completion_at'] and margin==result['completion_margin_ticks'],'completion ledger'
    assert all(e['at'] in times for e in trace['events'] if e['kind']=='complete' and e['task']==world['required_completion']),'unverified completion event'
    safety=oracle.get('safety_pass') is True
    return {'ledger_verified':True,'registered_task_pass':task_pass,'initial_view':initial,
            'T1':{'status':'PARTIAL_BOUNDED_EVIDENCE','source_queries':sum(c['request']['action'] in ('authority','applicability','reports') for c in calls),
                  'guard_denials':sum(c['response']['result'].get('error')=='native_commit_guard_denied' for c in calls),
                  'limit':'Source sampling and guard recovery observed; no complete material-change detection claim.'},
            'T2':{'status':'SCRIPTED_ROUTE_RECONSTRUCTED','signal_receipts':len(received),'decisions':len(decisions),
                  'unknown_signals':sum(s['signal']['current']['basis_sufficiency']=='UNKNOWN' for s in emitted.values()),
                  'limit':'Not independent/model handoff compliance.'},
            'T3':{'status':'BOUNDED_AUTHORIZATION_AND_JUSTIFICATION_MET' if safety else 'BOUNDED_SAFETY_NOT_MET',
                  'limit':'Universal PNI and externalities unassessed.'},
            'T4':{'status':'MET_FOR_REGISTERED_TASK' if task_pass else 'NOT_MET_FOR_REGISTERED_TASK',
                  'completion_margin_ticks':margin},'canonical_sufficiency_closed':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run_dir',type=Path)
    args=parser.parse_args()
    if not __debug__:
        raise RuntimeError('Run without -O')
    target=args.run_dir/'VERIFICATION.json'
    if target.exists():
        raise FileExistsError(target)
    freeze=read(HERE/'DESIGN_FREEZE.json')
    for name,expected in freeze['sha256'].items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==expected,'design freeze'
    for name,expected in read(HERE/'DEPENDENCIES.json').items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest()==expected,'dependency freeze'
    reg=read(args.run_dir/'REGISTRATION.json')
    assert reg['design_freeze_sha256']==hashlib.sha256((HERE/'DESIGN_FREEZE.json').read_bytes()).hexdigest()
    cases=read(HERE/'CASES.json')['cases']
    worlds=read(args.run_dir/'WORLD_INPUTS.json')
    evaluate=verify_oracle(BASE/'fixtures/00G-HF-ORACLE-v0.4')
    entries=[]
    for case in cases:
        pair={}
        for arm in reg['arms']:
            try:
                assert worlds[case['id']]==case['world'] and reg['case_world_hashes'][case['id']]==digest(case['world'])
                detail=check_path(args.run_dir/case['id']/arm,case['world'],arm,reg,evaluate)
                detail['frozen_expectation_met']=detail['registered_task_pass']==case['expected_task_pass'][arm]
                pair[arm]=detail
            except Exception as exc:
                pair[arm]={'ledger_verified':False,'error':repr(exc),'frozen_expectation_met':False}
        comparable=pair.get('native',{}).get('initial_view')==pair.get('native_ea',{}).get('initial_view')
        for detail in pair.values():
            detail.pop('initial_view',None)
        entries.append({'case':case['id'],'same_initial_view':comparable,'arms':pair})
    result={'status':'AUTHOR_INDEPENDENT_CHECKER_NOT_EXTERNAL_REVIEW','pairs':len(entries),
            'verified_paths':sum(v['ledger_verified'] for p in entries for v in p['arms'].values()),
            'expected_outcomes_met':sum(v['frozen_expectation_met'] for p in entries for v in p['arms'].values()),
            'all_initial_views_equal':all(p['same_initial_view'] for p in entries),
            'model_requests':0,'canonical_T1_T4_sufficiency_closed':False,'results':entries}
    target.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='results'},indent=2))
    return 0 if result['verified_paths']==len(cases)*2 and result['expected_outcomes_met']==len(cases)*2 and result['all_initial_views_equal'] else 1


if __name__=='__main__':
    raise SystemExit(main())
