"""Decision-open model integration on the unchanged cached-lineage environment."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import sys
import time
from adapter import AccessError, FIELDS

HERE = Path(__file__).resolve().parent
SCENARIO = HERE.parents[1] / 'traversals' / '00G-HF-CACHED-LINEAGE-v0.1'
sys.path.insert(0,str(SCENARIO))
from environment import Environment, Journal, BudgetExceeded, canonical, digest
from ea_bridge import make_signal
from oracle import evaluate

LIMITS = dict(model_turns=20, output_tokens_per_turn=2048, charged_token_stop=32000,
              wall_seconds=300, request_timeout_seconds=45, service_calls=12)
ARMS = ('native','raw','ea')


def write(path, value):
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')


class DurableJournal(Journal):
    def __init__(self,path):
        super().__init__()
        self.path=path
        path.touch(exist_ok=False)

    def add(self,kind,time,data):
        super().add(kind,time,data)
        with self.path.open('a') as out:
            out.write(canonical(self.rows[-1])+'\n')


def valid_arguments(args, advisory_id):
    if not isinstance(args,dict) or set(args)!=set(FIELDS):
        return False
    if args['action'] not in FIELDS['action']['enum'] or args['frame'] not in ('FRAME_A','FRAME_B',None):
        return False
    if not isinstance(args['receipts'],list) or len(args['receipts'])>3 or any(not isinstance(x,str) for x in args['receipts']):
        return False
    if args['total'] is not None and type(args['total']) is not int:
        return False
    if args['signal_id'] is not None and (not isinstance(args['signal_id'],str) or args['signal_id']!=advisory_id):
        return False
    action=args['action']
    if action=='resolve':
        return args['frame'] is None and args['total'] is None and bool(args['receipts'])
    if action=='read':
        return args['frame'] is not None and not args['receipts'] and args['total'] is None
    if action=='deliver':
        return args['frame'] is not None and not args['receipts'] and type(args['total']) is int
    return args['frame'] is None and not args['receipts'] and args['total'] is None


def episode(world, arm, client, journal, limits=None):
    if arm not in ARMS:
        raise ValueError('unknown arm')
    budget=limits or LIMITS
    env=Environment(world,journal)
    started=time.monotonic()
    requests=responses=charged=0
    observed=set()
    advisory_id=None
    infrastructure=False
    reason='model_turn_limit'
    journal.add('episode',0,dict(arm=arm,world_sha256=digest(world)))
    try:
        enrollment=env.call('enroll')
        env.resume()
        packet=env.call('messages')
        initial=dict(enrollment=enrollment,messages=packet)
        if arm in ('raw','ea'):
            resolved=env.call('resolve',dict(receipts=[r['id'] for r in packet['references']]))
            env.spend('processing',1,'advisory_processing')
            advisory=dict(current_evidence=resolved)
            if arm=='ea':
                bundle=make_signal(enrollment,resolved,env.now)
                advisory['assessment']=bundle['signal']
                journal.add('ea_inputs',env.now,bundle)
            advisory_id=digest(advisory)
            journal.add('advisory_emitted',env.now,dict(id=advisory_id,payload=advisory))
            env.spend('transport',1,'advisory_transport')
            initial['advisory']=dict(id=advisory_id,**advisory)
            journal.add('advisory_received',env.now,dict(id=advisory_id))
        initial['now']=env.now
        items=[dict(role='user',content=canonical(initial))]
        previous=None
        for turn in range(budget['model_turns']):
            remaining=budget['wall_seconds']-(time.monotonic()-started)
            if remaining<=0 or charged>=budget['charged_token_stop']:
                reason='resource_limit_before_request'
                break
            client.timeout=min(budget['request_timeout_seconds'],remaining)
            client.max_output_tokens=budget['output_tokens_per_turn']
            journal.add('model_input',env.now,dict(turn=turn,items=items,previous_response_id=previous))
            requests+=1
            response=client.respond(items,previous)
            responses+=1
            if not isinstance(response,dict):
                raise AccessError('malformed_response')
            output=response.get('output')
            usage=response.get('usage')
            valid=(response.get('status')=='completed' and isinstance(response.get('id'),str)
                   and isinstance(response.get('model'),str) and isinstance(output,list)
                   and all(isinstance(v,dict) for v in output) and isinstance(usage,dict)
                   and type(usage.get('total_tokens')) is int and usage['total_tokens']>=0)
            journal.add('model_response',env.now,dict(turn=turn,id=response.get('id'),model=response.get('model'),
                        status=response.get('status'),usage=usage,
                        visible_output=[v for v in output if isinstance(v,dict) and v.get('type')!='reasoning'] if isinstance(output,list) else []))
            if not valid:
                raise AccessError('incomplete_or_malformed_response')
            charged+=usage['total_tokens']
            observed.add(response['model'])
            if time.monotonic()-started>=budget['wall_seconds']:
                reason='wall_limit_before_dispatch'
                break
            if charged>budget['charged_token_stop']:
                reason='token_threshold_exceeded_before_dispatch'
                break
            env.spend('response',1,'model_response_turn')
            calls=[v for v in output if v.get('type')=='function_call']
            if not calls:
                reason='model_final_without_delivery'
                break
            if len(calls)!=1 or calls[0].get('name')!='step' or not isinstance(calls[0].get('call_id'),str):
                raise AccessError('unsupported_tool_response')
            call=calls[0]
            try:
                args=json.loads(call.get('arguments',''))
            except (ValueError,TypeError):
                args=None
            if not valid_arguments(args,advisory_id):
                result=dict(error='invalid_tool_arguments')
                journal.add('arguments_rejected',env.now,dict(call_id=call['call_id']))
            else:
                journal.add('model_action',env.now,dict(call_id=call['call_id'],arguments=args,
                            advisory_acknowledged=args['signal_id'] is not None))
                action=args['action']
                if action=='stop':
                    reason='model_stop'
                    break
                kwargs=dict(receipts=args['receipts']) if action=='resolve' else dict(frame=args['frame'])
                if action=='deliver':
                    kwargs['total']=args['total']
                result=env.call(action,kwargs)
                if action=='deliver' and result.get('transport_accepted'):
                    reason='accepted_delivery'
                    break
            previous=response['id']
            items=[dict(type='function_call_output',call_id=call['call_id'],output=canonical(dict(result=result,now=env.now)))]
    except BudgetExceeded as exc:
        reason=str(exc)
    except AccessError as exc:
        infrastructure=True
        reason='MODEL_ACCESS_ERROR:'+str(exc)
        journal.add('model_error',env.now,dict(reason=reason))
    outcome=evaluate(world,journal.rows)
    journal.add('closure',env.now,dict(reason=reason,ledger=env.ledger,calls=env.calls))
    return dict(arm=arm,case_id=world['id'],model_requests=requests,model_responses=responses,
                observed_models=sorted(observed),charged_tokens=charged,
                wall_seconds=time.monotonic()-started,reason=reason,
                infrastructure_interrupted=infrastructure,operational_result_eligible=responses>0 and not infrastructure,
                outcome=outcome,ledger=env.ledger,journal_head=journal.head)


def audit(world, rows, result):
    head='0'*64
    for i,row in enumerate(rows):
        assert row['seq']==i and row['previous']==head
        assert row['hash']==digest({k:v for k,v in row.items() if k!='hash'})
        head=row['hash']
    assert head==result['journal_head']
    assert result['outcome']==evaluate(world,rows)
    inputs=[r for r in rows if r['kind']=='model_input']
    replies=[r for r in rows if r['kind']=='model_response']
    assert len(inputs)==result['model_requests']
    assert len(replies)<=result['model_responses']
    accepted=[r for r in rows if r['kind']=='response' and r['data']['action']=='deliver'
              and r['data']['result'].get('transport_accepted')]
    for receipt in accepted:
        earlier=[r for r in rows if r['kind']=='model_action' and r['seq']<receipt['seq']
                 and r['data']['arguments']['action']=='deliver']
        assert earlier and earlier[-1]['data']['arguments']['frame']==receipt['data']['result']['frame']
        assert earlier[-1]['data']['arguments']['total']==receipt['data']['result']['total']
    for action in (r for r in rows if r['kind']=='model_action'):
        preceding=[r for r in replies if r['seq']<action['seq']]
        assert preceding
        calls=[o for o in preceding[-1]['data']['visible_output'] if o.get('type')=='function_call']
        assert len(calls)==1 and calls[0]['call_id']==action['data']['call_id']
        assert json.loads(calls[0]['arguments'])==action['data']['arguments']
    for item in inputs:
        serialized=canonical(item['data']['items'])
        assert '"pivot"' not in serialized and '"required_frame"' not in serialized and '"case_id"' not in serialized
    assert sum(r['data']['ticks'] for r in rows if r['kind']=='charge')==sum(result['ledger'].values())
    return dict(status='VERIFIED_AUTHOR_AUDIT',effects_bound_to_visible_model_calls=True,
                chain_verified=True,oracle_replayed=True,private_reasoning_published=False)
