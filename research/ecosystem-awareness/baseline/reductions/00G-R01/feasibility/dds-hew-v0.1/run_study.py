"""Execute only the frozen, bounded HEW DDS model self-test.

No network, credentials, native product or human. Output never overwrites a run.
Run: python run_study.py --output <fresh directory>
"""
from concurrent.futures import ThreadPoolExecutor
from copy import deepcopy
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
import platform
import sqlite3
import time

from hew_runtime import Runtime, PUBLIC_KEYS, VERSION
from hew_oracle import judge, exhaustive_slot, verify_event_chain, audit_reservations

ROOT=Path(__file__).resolve().parent


def dump(path,value):
    with Path(path).open('x',encoding='utf-8') as handle:
        json.dump(value,handle,indent=2,ensure_ascii=False)
        handle.write('\n')


def reference_reservations(database,public):
    db=sqlite3.connect(str(database))
    busy={p['id']:list(p['busy']) for p in public['reviewers']}
    for person,start,finish in db.execute('SELECT subject,start,finish FROM reservations'):
        if person in busy:busy[person].append([start,finish])
    db.close()
    ack=exhaustive_slot(public['reviewers'],busy,public['arrival'],1,public['ack_deadline'],'ack',public['owner'])
    at=ack[0]+1 if ack else public['ack_deadline']+1
    if ack:busy[ack[1]].append([ack[0],at])
    review=(exhaustive_slot(public['reviewers'],busy,at,public['review_service'],public['decision_deadline'],'review',public['owner'])
            if public['capacity_observation']=='current' else None)
    return ack,review


def selected(record):
    return (record['start'],record['subject']) if record else None


def fresh_public(base,label):
    public=deepcopy(base);operation='CONTROL-'+label
    public['operation_id']=operation;public['scenario_id']=operation;public['command_id']='command-'+operation
    public['evidence']['case']=operation;public['grant']['case']=operation
    public['semantic_contract']['operation_id']=operation
    return public


def analytical(card):
    a=F(99,100);p=F(19,20);delta=F(1,1000);beta=F(941,990)
    rows=[]
    for profile in card['analytical_profiles']:
        q=F(profile['q']);g=(1-a)*q;n=(1-a)*(1-q)
        s=g+a*beta;r=n*beta
        rows.append({'scenario_id':profile['scenario_id'],'modality':'EXACT_ANALYTICAL_RECONSTRUCTION',
          'traversal':profile['traversal'],'q':str(q),'s':str(s),'r':str(r),'cost':40,
          'accepted':40<=profile['b'] and r<=delta and s>=p,
          'human_accuracy_measured':False,'original_world_law':True,'new_theorem':False})
    assert rows[0]['s']=='19/20' and rows[0]['r']=='941/990000' and rows[0]['accepted']
    assert rows[1]['s']=='949/1000' and rows[1]['r']=='941/495000' and not rows[1]['accepted']
    return rows


def controls(directory,base):
    output=[]
    def check(name,test,scope):
        assert test,name
        output.append({'control':name,'assertion':'PASS','scope':scope})
    def environment(label,change=None):
        public=fresh_public(base,label)
        if change:change(public)
        database=directory/(label+'.sqlite')
        runtime=Runtime(database);runtime.provision_authority(public['operation_id'],public['grant'])
        return runtime,database,public
    rt,db,pub=environment('record')
    result=rt.run_case(pub)
    check('nominal_full_model_path',result['delivered'],'ACK+review+current delegation+local digital effect+confirmed delivery')
    messages=rt.db.execute('SELECT payload FROM notifications WHERE operation_id=?',(pub['operation_id'],)).fetchall()
    roots={json.loads(row[0])['source_root'] for row in messages}
    check('whispering_same_source_lineage',len(messages)==2 and len(roots)==1,
          'Two bounded recipient records preserve one source origin; not independent evidence')
    check('whispering_minimum_payload',all(set(json.loads(row[0]))=={'operation_id','resource','source_root','evidence_version'} for row in messages),
          'No reviewer calendar, grant, private world or case-body disclosure in notifications')
    forged=deepcopy(result);forged.update(delivered=False,confirmed=False,work=-999)
    observed=judge(db,pub,{'correct_action':'Y','basis_truth':True,'effect_authorized':True,'continuity_supported':True},forged)
    check('oracle_uses_recorded_effect_delivery_and_work',observed['sufficient_delivery'] and observed['effect_knowledge']=='CONFIRMED'
          and observed['work_units']==result['work'],
          'Adjudicator reconstructs outcome/cost from persisted records, not controller summary claims')
    before=rt.db.execute('SELECT count(*) FROM effects').fetchone()[0]
    try:rt.file_case({**pub,'private_world':{'answer':'Y'}})
    except ValueError:rejected=True
    else:rejected=False
    check('private_input_key_rejected',rejected,'Declared public API keys only; not OS/malicious-code isolation')
    try:rt.read_case(pub['operation_id'],'B','principal-B')
    except PermissionError:rejected=True
    else:rejected=False
    check('cross_tenant_case_view_rejected',rejected,'Model API access policy, not encrypted storage')
    check('authorized_case_view',rt.read_case(pub['operation_id'],'A','principal-A')['operation_id']==pub['operation_id'],'Authorized principal access retained')
    check('filing_does_not_enable_adverse_action',rt.request_adverse_action(pub['operation_id']) is False,
          'No adverse effect from filing in this model API; institution/reputation behavior not tested')
    check('no_adverse_effect_written',rt.db.execute('SELECT count(*) FROM effects').fetchone()[0]==before,'Digital effect count retained')
    for kind,sql in [('update','UPDATE events SET kind=kind'),('delete','DELETE FROM events')]:
        try:rt.db.execute(sql)
        except sqlite3.IntegrityError:rejected=True
        else:rejected=False
        check('append_only_'+kind+'_rejected',rejected,'SQLite event-table trigger; privileged admin can bypass it')
    check('event_hash_chain',bool(verify_event_chain(rt.events())),'Tamper-evident chain only while predecessor anchor is trusted')
    copy=sqlite3.connect(str(directory/'tampered.sqlite'));rt.db.backup(copy)
    copy.execute('DROP TRIGGER events_no_update');copy.execute("UPDATE events SET detail='{}' WHERE seq=1");copy.commit();copy.close()
    tampered=Runtime(directory/'tampered.sqlite')
    try:verify_event_chain(tampered.events())
    except AssertionError:detected=True
    else:detected=False
    tampered.close();check('altered_record_detected',detected,'An unchanged chain anchor detects this specific alteration; no hardware trust root')
    duplicate=rt.apply(pub,8)
    check('duplicate_command_no_new_effect',duplicate.get('duplicate') and rt.db.execute('SELECT count(*) FROM effects').fetchone()[0]==before,
          'One local digital effect per command identity under the selected fingerprint')
    changed=deepcopy(pub);changed['request_epoch']=44
    conflict=rt.apply(changed,8)
    check('conflicting_command_id_rejected','COMMAND_ID_CONFLICT' in conflict['reasons'],'Fingerprint includes generation in this selected profile')
    revoked=deepcopy(pub['grant']);revoked['active']=False
    rt.provision_authority(pub['operation_id'],revoked)
    denied=rt.apply(pub,8)
    check('caller_grant_cannot_override_current_source','DELEGATION_NOT_APPLICABLE' in denied['reasons'],
          'Environment-supplied current authority overrides stale caller description; issuer authentication stipulated')
    rt.provision_authority(pub['operation_id'],pub['grant'])
    rt.install_floor(pub['resource'],44);rt.close()
    rt=Runtime(db)
    check('generation_floor_retained_after_reopen',rt.db.execute('SELECT epoch FROM floors WHERE resource=?',(pub['resource'],)).fetchone()[0]==44,
          'SQLite close/reopen; not hardware power-loss or distributed consensus test')
    old=rt.apply(pub,8)
    check('old_generation_denied_after_reopen','OLD_GENERATION' in old['reasons'],'Guard at local transaction after floor44 installed')
    rt.close()

    rt,db,pub=environment('outbox_recovery')
    rt.file_case(pub)
    check('case_and_pending_notifications_atomic',rt.db.execute('SELECT count(*) FROM outbox').fetchone()[0]==2
          and rt.db.execute('SELECT count(*) FROM notifications').fetchone()[0]==0,
          'Local transaction retains filing and two pending notifications before relay')
    rt.close();rt=Runtime(db);rt.whisper(pub);rt.whisper(pub)
    check('outbox_relay_after_reopen_idempotent',rt.db.execute('SELECT count(*) FROM notifications').fetchone()[0]==2
          and sum(e['kind']=='NOTIFICATION_SENT' for e in rt.events())==2,
          'Two local relays produce only one recipient record per operation/recipient; network effects not tested')
    check('outbox_recovery_chain',bool(verify_event_chain(rt.events())),'Event chain remains coherent after relay replay')
    rt.close()

    rt,db,pub=environment('concurrency')
    # File two additional operations; two connections then race for the same future slot.
    jobs=[fresh_public(base,'reservation-'+name) for name in ('A','B')]
    for job in jobs:
        job['reviewers']=[person for person in job['reviewers'] if person['id']=='H2']
        rt.file_case(job)
    def reserve(job):
        connection=Runtime(db)
        try:return connection.reserve(job,'review',10,3,13)
        finally:connection.close()
    with ThreadPoolExecutor(max_workers=2) as pool:reservations=list(pool.map(reserve,jobs))
    check('atomic_shared_capacity_reservation',sum(r is not None for r in reservations)==1,'Two real SQLite connections; one exclusive reviewer slot')
    check('no_overlapping_reservations',audit_reservations(db)==1,'Post-run independent interval audit')
    rt.close()

    rt,db,pub=environment('midstream_revocation')
    rt.file_case(pub)
    ack=rt.reserve(pub,'ack',2,1,3)
    review=rt.reserve(pub,'review',ack['finish'],3,6)
    rt._event(pub['operation_id'],review['finish'],'REVIEW_COMPLETED',{'reviewer':review['subject']})
    revoked=deepcopy(pub['grant']);revoked['active']=False
    rt.provision_authority(pub['operation_id'],revoked)
    action=rt.apply(pub,7)
    check('revocation_between_review_and_effect','DELEGATION_NOT_APPLICABLE' in action['reasons']
          and rt.db.execute('SELECT count(*) FROM effects').fetchone()[0]==0,
          'Actual model authority-store update after review; no effect under the stale caller description')
    rt.close()

    rt,db,pub=environment('peer_missing',lambda p:p['affected_recipients'][1].update(receipt_delay=None))
    result=rt.run_case(pub)
    check('missing_affected_peer_receipt_keeps_gate',not result['applied'] and 'AFFECTED_PEER_RECEIPT_UNRESOLVED' in result['reasons'],
          'All declared affected receipts required by this profile; filing itself requires no majority')
    rt.close()
    rt,db,pub=environment('recipient_scope',lambda p:p['affected_recipients'][1].update(tenant='B'))
    result=rt.run_case(pub)
    check('unauthorized_recipient_not_given_payload',rt.db.execute('SELECT count(*) FROM notifications WHERE recipient=?',('agent-C',)).fetchone()[0]==0
          and not result['applied'],'One denied cross-domain notification; real federation/privacy not tested')
    rt.close()
    for key,value in [('tenant','B'),('resource','other-resource'),('deputy','other-service')]:
        rt,db,pub=environment('scope-'+key);rt.run_case(pub)
        changed=deepcopy(pub);changed[key]=value
        result=rt.apply(changed,8)
        check('current_case_binding_'+key,not result['applied'] and 'CASE_BINDING_MISMATCH' in result['reasons'],
              'Caller cannot move a filed operation to another principal/resource/actor binding')
        rt.close()

    rt,db,pub=environment('forged_success',lambda p:p['evidence'].update(complete=False))
    result=rt.run_case(pub);forged=deepcopy(result);forged.update(applied=True,confirmed=True,delivered=True,work=0)
    verdict=judge(db,pub,{'correct_action':'Y','basis_truth':True,'effect_authorized':True,'continuity_supported':True},forged)
    check('oracle_rejects_controller_success_without_effect',not verdict['sufficient_delivery'] and verdict['actual_effect_count']==0,
          'No high-quality delivery is inferred from forged controller booleans')
    rt.close()

    for label,change,reason in [
        ('gate_latency',lambda p:p.update(gate_latency=1),'APPLICATION_TOO_LATE_OR_OVER_BUDGET'),
        ('unknown_capacity',lambda p:p.update(capacity_observation='unknown'),'CAPACITY_UNKNOWN'),
        ('stale_state',lambda p:p['state_appraisal'].update(expires=6),'STATE_NOT_CURRENT_OR_APPLICABLE'),
        ('expired_grant',lambda p:p['grant'].update(expires=7),'DELEGATION_NOT_APPLICABLE'),
        ('purpose_inapplicable',lambda p:p['grant'].update(purpose='unrelated-purpose'),'DELEGATION_NOT_APPLICABLE'),
        ('work_budget',lambda p:p.update(work_budget=16),'APPLICATION_TOO_LATE_OR_OVER_BUDGET'),
        ('forged_generation',lambda p:p.update(request_epoch=9999,token_verified=False),'FENCE_BINDING_NOT_ADMITTED')]:
        rt,db,pub=environment(label,change);result=rt.run_case(pub)
        check(label+'_guard',not result['applied'] and reason in result['reasons'],
              'Registered model condition; no native credential/source validation')
        check(label+'_case_preserved',rt.db.execute('SELECT count(*) FROM cases').fetchone()[0]==1,'Denial retains filing')
        rt.close()
    for available in (False,True):
        label='reply_lost_'+str(available)
        rt,db,pub=environment(label,lambda p:p.update(reply_lost=True,effect_query_available=available))
        result=rt.run_case(pub)
        check(label+'_knowledge_state',result['applied'] and result['confirmed']==available and result['delivered']==available,
              'Effect versus knowledge separated; unavailable query leaves unknown')
        check(label+'_effect_count',rt.db.execute('SELECT count(*) FROM effects').fetchone()[0]==1,'Reconciliation never reapplies the digital effect')
        rt.close()
    return output


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    output=Path(args.output).resolve()
    if output.exists():raise FileExistsError('Fresh output directory required; preserve prior runs')
    freeze=json.loads((ROOT/'FREEZE.json').read_text(encoding='utf-8'))
    for entry in freeze['files']:
        assert hashlib.sha256((ROOT/entry['path']).read_bytes()).hexdigest()==entry['sha256'],entry['path']
    card=json.loads((ROOT/'RUN_CARD.json').read_text(encoding='utf-8'))
    output.mkdir(parents=True)
    start=time.perf_counter();scenario_rows=[];operation_count=0;reference_checks=0
    failure={'run_id':card['run_id'],'status':'FAILED_SELFTEST_ATTEMPT','error':None}
    try:
      for spec in card['scenarios']:
        database=output/(spec['scenario_id']+'.sqlite');runtime=Runtime(database)
        rows=[]
        try:
          for index,(public,authority,private,expected) in enumerate(zip(spec['public_cases'],spec['environment_authority_inputs'],spec['private_worlds'],spec['expected_sufficient_delivery'])):
            assert set(public)==PUBLIC_KEYS
            runtime.provision_authority(public['operation_id'],authority)
            ack_reference,review_reference=reference_reservations(database,public)
            result=runtime.run_case(public)
            assert selected(result['ack'])==ack_reference,(spec['scenario_id'],'ack reference')
            assert selected(result['review'])==review_reference,(spec['scenario_id'],'review reference')
            reference_checks+=2
            verdict=judge(database,public,private,result)
            assert verdict['work_units']==result['work'],(spec['scenario_id'],'event-derived work')
            assert verdict['sufficient_delivery']==expected,(spec['scenario_id'],verdict)
            assert verdict['violation_observed']==spec.get('expected_violation',False),(spec['scenario_id'],verdict)
            assert verdict['case_preserved']
            row={'operation_id':public['operation_id'],'controller_result':result,'oracle_verdict':verdict,
                 'private_world_sent_to_controller':False}
            rows.append(row);operation_count+=1
          audit_reservations(database);chain=verify_event_chain(runtime.events())
          scenario_rows.append({'scenario_id':spec['scenario_id'],'family_id':spec['family_id'],
             'modality':spec['modality'],'human_narrative':spec['human_narrative'],
             'selection_note':spec['selection_note'],'operations':rows,
             'event_chain_head':chain,'events':runtime.events(),'fixture_expectations_matched':True,
             'native_or_human_execution':False})
        finally:runtime.close()
      exact=analytical(card)
      base=card['scenarios'][0]['public_cases'][0]
      extra=controls(output,base)
      result={'run_id':card['run_id'],'status':'PASS_MODEL_INSTRUMENT_ASSERTIONS',
        'native_technology_execution':False,'real_human_execution':False,
        'environment':{'python':platform.python_version(),'sqlite':sqlite3.sqlite_version,'platform':platform.system()},
        'run_card_sha256':hashlib.sha256((ROOT/'RUN_CARD.json').read_bytes()).hexdigest(),
        'freeze_sha256':hashlib.sha256((ROOT/'FREEZE.json').read_bytes()).hexdigest(),
        'elapsed_wall_seconds':time.perf_counter()-start,'analytical_reconstructions':exact,
        'registered_scenario_count':20,'sqlite_scenario_count':18,'additional_source_counterexample':1,
        'sqlite_operations_evaluated':operation_count,'reference_schedule_checks':reference_checks,
        'scenario_results':scenario_rows,'functional_controls':extra,'functional_control_assertions':len(extra),
        'outside_contract_counterexample_retained_as_failure':True,
        'full_protected_channel_or_DDS_acceptance':False,'independent_review':False,
        'field_warning':'Instrument assertion PASS includes expected rejection/unresolved outcomes and a retained source-truth counterexample; it is not20 successful human scenarios or native DDS conformance.',
        'population_rate':None,'comparative_superiority':None,'pending':card['claims_pending']}
      dump(output/'RESULTS.json',result)
      print(json.dumps({'run_id':card['run_id'],'status':result['status'],
        'scenarios':20,'additional_counterexample':1,'sqlite_operations':operation_count,
        'functional_controls':len(extra),'schedule_reference_checks':reference_checks,
        'counterexample':'FAIL_VIOLATION retained','results':str(output/'RESULTS.json')}))
    except Exception as error:
      failure['error']=repr(error);failure['partial_scenario_results']=scenario_rows
      dump(output/'FAILED_ATTEMPT.json',failure)
      raise


if __name__=='__main__':main()
