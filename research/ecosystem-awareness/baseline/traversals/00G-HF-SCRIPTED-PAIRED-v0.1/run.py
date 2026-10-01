"""Execute registered complete scripted paths. No models, APIs or hidden-policy inputs."""
import argparse
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
BASE = HERE.parent.parent
sys.path.insert(0,str(BASE/'fixtures/00G-HF-NATIVE-v0.1'))
from native import Episode, Recorder, digest
from run_pilot import verify_oracle
sys.path.insert(0,str(BASE/'fixtures/00G-HF-EA-COMPONENT-v0.2'))
from native_adapter import adapt_native
from temporal import compare
from policy import decide

LIMITS = {'tool_calls':40,'cycles':8,'wall_seconds':10,'response_ticks':1,
          'EA_processing_ticks':1,'EA_transport_ticks':1,'poll_wait_ticks':5}
ARMS = ('native','native_ea')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path,value):
    path.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n')


class BudgetStop(Exception):
    pass


def run_path(world, arm, directory, evaluate):
    recorder=Recorder(directory/'JOURNAL.jsonl')
    ep=Episode(world,recorder)
    initial=ep.initial_view()
    recorder.write('public_initial_view',initial)
    started=time.monotonic()
    cpu_start=time.process_time()
    tools_used=0
    costs={'native_tool_ticks':0,'response_ticks':0,'EA_processing_ticks':0,'EA_transport_ticks':0}
    cycles=0
    signals=[]
    decisions=[]
    submissions=[]
    exchanges=[]
    outcome_error=None
    infra=False
    decision_scope={'id':'public-T1-decision','recipient':'R','task':'T1','resource':'Y',
                    'operation':'inspect','claim':'Q','basis_version':'host-public-v1'}
    timing={'transport_ticks':LIMITS['EA_transport_ticks'],'response_ticks':LIMITS['response_ticks'],
            'last_useful_at':initial['deadline']-4}
    # Only public initial data crosses into the EA adapter.
    previous=(adapt_native(initial,[],decision_scope,ep.now,timing)['snapshot']
              if arm=='native_ea' else None)

    def budget():
        if time.monotonic()-started > LIMITS['wall_seconds']:
            raise TimeoutError('wall_budget')
        if ep.closed or ep.now >= initial['deadline']:
            raise BudgetStop('deadline_or_closed')

    def call(action,**kwargs):
        nonlocal tools_used
        budget()
        if tools_used >= LIMITS['tool_calls']:
            raise BudgetStop('tool_budget')
        start=ep.now
        value=ep.call(action,**kwargs)
        tools_used+=1
        costs['native_tool_ticks']+=ep.now-start
        if action in ('authority','applicability','reports'):
            exchanges.append({'action':action,'requested_at':start,'response_at':ep.now,'result':deepcopy(value)})
        return value

    def charge(kind,ticks):
        budget()
        start=ep.now
        ep.now=min(initial['deadline'],ep.now+ticks)
        costs[kind]+=ep.now-start
        recorder.write('clock_charge',{'kind':kind,'from':start,'to':ep.now,'charged_ticks':ep.now-start})
        if ep.now >= initial['deadline']:
            raise BudgetStop('deadline_during_'+kind)

    def reenter(reason):
        recorder.write('reentry_request',{'at':ep.now,'reason':reason})
        call('wait',until=min(ep.now+LIMITS['poll_wait_ticks'],initial['deadline']))

    try:
        for cycle in range(LIMITS['cycles']):
            budget()
            cycles=cycle+1
            responses={action:call(action) for action in ('authority','applicability','reports')}
            if any('error' in value for value in responses.values()):
                raise RuntimeError('source_error')
            public={'initial':deepcopy(initial),'responses':deepcopy(responses)}
            signal=None
            sid=None
            if arm=='native_ea':
                charge('EA_processing_ticks',LIMITS['EA_processing_ticks'])
                projection=adapt_native(initial,exchanges,decision_scope,ep.now,timing)
                signal=compare(previous,projection['snapshot'])
                previous=projection['snapshot']
                sid='signal-'+str(cycle+1)
                recorder.write('signal_emitted',{'id':sid,'at':ep.now,'projection':projection,'signal':signal})
                charge('EA_transport_ticks',LIMITS['EA_transport_ticks'])
                recorder.write('signal_received',{'id':sid,'at':ep.now,'sha256':digest(signal)})
                signals.append({'id':sid,'emitted_at':signal['current']['emitted_at'],
                                'received_at':ep.now,'signal':signal})
            charge('response_ticks',LIMITS['response_ticks'])
            choice=decide(deepcopy(public),ep.now,deepcopy(signal))
            decision={'cycle':cycle+1,'at':ep.now,'signal_id':sid,'public_input':public,'choice':choice}
            recorder.write('scripted_decision',decision)
            decisions.append(decision)
            if choice['disposition']=='stop':
                ep.finish(choice['reason'])
                break
            if choice['disposition']=='wait':
                reenter(choice['reason'])
                continue
            commit=call('commit',task=choice['task'],basis=choice['basis'])
            if 'decision_id' not in commit:
                reenter('native_commit_denied')
                continue
            inspection=call('inspect',task=choice['task'],decision_id=commit['decision_id'])
            if inspection.get('status')!='executed':
                reenter('native_effect_not_executed')
                continue
            submitted=call('submit',task=choice['task'],attempt_id=inspection['attempt_id'],
                           total=sum(inspection['records']))
            submissions.append(deepcopy(submitted))
            if submitted.get('accepted') is True:
                ep.finish('checked_legitimate_completion')
                break
            reenter('native_completion_rejected')
        else:
            ep.finish('cycle_budget')
    except BudgetStop as exc:
        ep.finish(str(exc))
    except Exception as exc:
        infra=True
        outcome_error=repr(exc)
        recorder.write('infrastructure_error',{'at':ep.now,'error':outcome_error})
        ep.finish('infrastructure_interruption',infrastructure=True)
    elapsed=time.monotonic()-started
    cpu=time.process_time()-cpu_start
    trace=ep.trace(infrastructure=infra)
    oracle=evaluate(deepcopy(world),deepcopy(trace))
    completion=[e['at'] for e in trace['events'] if e['kind']=='complete' and e['task']==initial['required_deliverable']]
    completed=bool(completion and submissions and submissions[-1].get('accepted') is True)
    margin=initial['deadline']-max(completion) if completion else None
    budget_ok=(tools_used<=LIMITS['tool_calls'] and cycles<=LIMITS['cycles'] and elapsed<=LIMITS['wall_seconds'])
    task_pass=bool(not infra and oracle.get('operational_pass') is True and completed and margin>0 and budget_ok)
    summary={'status':'INFRASTRUCTURE_INTERRUPTED' if infra else 'SCRIPTED_PATH_OBSERVED',
             'arm':arm,'reason':ep.close_reason,'error':outcome_error,'registered_task_pass':task_pass,
             'oracle_result':oracle,'accepted_completion':completed,'completion_at':max(completion) if completion else None,
             'completion_margin_ticks':margin,'final_tick':ep.now,'tool_calls':tools_used,'cycles':cycles,
             'signals_emitted':len([r for r in recorder.rows if r['kind']=='signal_emitted']),
             'signals_received':len(signals),'scripted_decisions':len(decisions),
             'EA_disposition_changes':sum(d['choice']['EA_changed_disposition'] for d in decisions),
             'cost_ticks':costs,'logical_elapsed_ticks':ep.now-initial['now'],'wall_seconds':elapsed,'cpu_seconds':cpu,
             'within_resource_ceilings':budget_ok,'journal_chain_head':recorder.previous,
             'model_requests':0,'model_decisions':0,'human_reviews':0,
             'T1':{'status':'PARTIAL_BOUNDED_EVIDENCE','limit':'Current source qualification/resampling; hidden/onset detection and global coverage not established.'},
             'T2':{'status':'PARTIAL_SCRIPTED_HANDOFF','limit':'Explicit policy consumes recorded information; model or external-owner compliance untested.'},
             'T3':{'status':'PENDING_VERIFIER','limit':'Authorization/justification checked by C3; universal PNI and externalities not assessed.'},
             'T4':{'status':'MET_FOR_REGISTERED_TASK' if task_pass else 'NOT_MET_FOR_REGISTERED_TASK',
                   'limit':'Declared logical costs, not calibrated production latency or optimality.'},
             'canonical_T1_T4_sufficiency_closed':False,'empirical_E1_E3_closed':False}
    write(directory/'TRACE.json',trace)
    write(directory/'RESULT.json',summary)
    return summary


def check_freeze():
    freeze=json.loads((HERE/'DESIGN_FREEZE.json').read_text())
    for name,expected in freeze['sha256'].items():
        if sha(HERE/name)!=expected:
            raise RuntimeError('frozen input changed: '+name)
    for name,expected in json.loads((HERE/'DEPENDENCIES.json').read_text()).items():
        if sha(HERE/name)!=expected:
            raise RuntimeError('dependency changed: '+name)
    return freeze


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',type=Path,required=True)
    args=parser.parse_args()
    if not __debug__:
        raise RuntimeError('Run without -O')
    check_freeze()
    evaluate=verify_oracle(BASE/'fixtures/00G-HF-ORACLE-v0.4')
    cases=json.loads((HERE/'CASES.json').read_text())['cases']
    args.output_dir.mkdir(parents=True,exist_ok=False)
    write(args.output_dir/'REGISTRATION.json',{
        'status':'PUBLISHED_FROZEN_AUTHOR_SCRIPTED_COMPARISON_NOT_BLIND_OR_MODEL_EXECUTION',
        'created_utc':datetime.now(timezone.utc).isoformat(),'python':sys.version,
        'design_freeze_sha256':sha(HERE/'DESIGN_FREEZE.json'),
        'case_world_hashes':{c['id']:digest(c['world']) for c in cases},'limits':LIMITS,
        'arms':list(ARMS),'order':'case order, native then native_ea; deterministic fresh state',
        'model_requests':0,'agent_decision_episodes':0,'planned_scripted_paths':len(cases)*len(ARMS),
        'dependency_manifest_sha256':sha(HERE/'DEPENDENCIES.json')})
    write(args.output_dir/'WORLD_INPUTS.json',{c['id']:c['world'] for c in cases})
    rows=[]
    for case in cases:
        pair={}
        for arm in ARMS:
            directory=args.output_dir/case['id']/arm
            directory.mkdir(parents=True)
            pair[arm]=run_path(deepcopy(case['world']),arm,directory,evaluate)
        rows.append({'case':case['id'],'family':case['family'],'arms':pair})
    report={'status':'SCRIPTED_PAIRED_LOT_COMPLETED','pairs':len(rows),'scripted_paths':len(rows)*2,
            'model_requests':0,'model_decisions':0,'empirical_E1_E3_closed':False,
            'canonical_T1_T4_sufficiency_closed':False,'results':rows,
            'note':'Failures and costs are observations; verifier adjudicates frozen expectations and recorder integrity.'}
    write(args.output_dir/'REPORT.json',report)
    print(json.dumps({'pairs':len(rows),'scripted_paths':len(rows)*2,
                     'task_passes':{arm:sum(r['arms'][arm]['registered_task_pass'] for r in rows) for arm in ARMS},
                     'model_requests':0},indent=2))
    return 0 if all(r['arms'][a]['status']=='SCRIPTED_PATH_OBSERVED' for r in rows for a in ARMS) else 2


if __name__=='__main__':
    raise SystemExit(main())
