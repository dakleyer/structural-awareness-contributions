"""Audited local Stage-A successor; predecessor source remains frozen separately."""
import argparse,contextlib,copy,hashlib,importlib.util,json,platform,sqlite3,time
from pathlib import Path
from typing import Literal
from pydantic import BaseModel,ConfigDict,Field,ValidationError
import pydantic

class Record(BaseModel):
    model_config=ConfigDict(strict=True,extra='forbid')
    tenant:str
    amount:int=Field(ge=0)
    currency:Literal['EUR']
    status:Literal['ready']

class Store:
    def __init__(self,path):
        self.c=sqlite3.connect(path);self.path=path;self.role='fixture';self.events=[]
    def q(self,sql,args=()):
        self.events.append({'n':len(self.events)+1,'role':self.role,'primitive':'sqlite.'+sql.split()[0].upper(),'units':1})
        return self.c.execute(sql,args)
    def commit(self):
        self.events.append({'n':len(self.events)+1,'role':self.role,'primitive':'sqlite.commit','units':1});self.c.commit()
    def mark(self,kind):
        self.events.append({'n':len(self.events)+1,'role':self.role,'primitive':kind,'units':1})
    @contextlib.contextmanager
    def phase(self,role):
        old=self.role;self.role=role
        try:yield
        finally:self.role=old
    def seal(self):
        actor=[e for e in self.events if e['role']=='candidate']
        return hashlib.sha256(json.dumps(actor,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    def ledger(self):
        counts={}
        for e in self.events:
            if e['role']=='candidate':counts[e['primitive']]=counts.get(e['primitive'],0)+e['units']
        return {'C_selected_units':sum(counts.values()),'components':counts,'events':self.events,
                'prices_human_network_tokens_lifecycle':None,'unit':'frozen selected API/policy units, weights1'}

def reject_duplicate(pairs):
    d={}
    for key,value in pairs:
        if key in d:raise ValueError('duplicate-member')
        d[key]=value
    return d

def setup(kind,spec,out):
    s=Store(out/'resource.sqlite');w=copy.deepcopy(spec['world'])
    if kind=='cache-ttl':
        for sql in ['create table cache(tenant text,key text,value integer,version integer,expires integer,primary key(tenant,key))',
                    'create table origin(tenant text,key text,value integer,version integer,available integer,primary key(tenant,key))',
                    'create table grants(tenant text primary key,allowed integer)']:s.q(sql)
        k=spec['kind'];version=2 if k=='source-new-generation' else 1;value=9999 if k=='false-source' else 2000 if version==2 else 1000
        s.q('insert into origin values(?,?,?,?,?)',('tenant-a','policy',value,version,int(k not in ['tenant-collision','offline-defer'])))
        s.q('insert into grants values(?,?)',('tenant-a',int(k!='revoked')))
        if k!='miss':s.q('insert into cache values(?,?,?,?,?)',('tenant-b' if k=='tenant-collision' else 'tenant-a','policy',9999 if k=='false-source' else 1000,1,10 if k in ['expired','offline-defer'] else 11))
    elif kind=='queues-ack-redelivery':
        s.q('create table message(op text,tenant text,valid integer,expires integer,acked integer,channel text,tag integer)')
        s.q('insert into message values(?,?,?,?,0,?,1)',('op','tenant-b' if spec['kind']=='other-tenant' else 'tenant-a',int(spec['kind']!='poison'),10 if spec['kind']=='expired' else 20,'channel-a'))
        s.q('create table grant_state(allowed integer)');s.q('insert into grant_state values(?)',(int(spec['kind']!='revoked'),))
        s.q('create table effect(op text'+('' if spec['kind']=='non-idempotent' else ' primary key')+')')
        s.q('create table receipt(op text primary key)');s.q('create table disposition(kind text)')
    elif kind=='structured-output':
        s.q('create table grant_state(tenant text,allowed integer,limit_value integer)');s.q('insert into grant_state values(?,?,?)',('tenant-a',int(spec['kind']!='revoked'),9999 if spec['kind']=='false-source' else 1000))
        s.q('create table effect(tenant text,amount integer)');s.q('create table disposition(kind text)')
    else:
        s.q('create table sample(tenant text,value integer,as_of integer,expires integer)')
        k=spec['kind'];values=[] if k=='missing' else [0,0,0] if k in ['healthy','lying-source'] else [1,1,1]
        for i,v in enumerate(values):s.q('insert into sample values(?,?,?,?)',('tenant-b' if k=='other-tenant' else 'tenant-a',v,min(10,9+i) if k=='pending' else 8+i,10 if k=='expired' else 11))
        s.q('create table target(state text)');s.q('insert into target values(?)',('HEALTHY' if k=='healthy' else 'FAULT',))
        s.q('create table grant_state(allowed integer)');s.q('insert into grant_state values(1)')
        s.q('create table notification(received integer)');s.q('create table disposition(kind text)')
    s.commit();return s,w

def cache(s,spec,mode,here):
    modspec=importlib.util.spec_from_file_location('frozen_cache_actor',here.parent/'cache-ttl/study.py')
    module=importlib.util.module_from_spec(modspec);modspec.loader.exec_module(module)
    fallback=spec.get('fallback',False)
    if mode=='review-only':
        for _ in range(12):s.q('select allowed from grants where tenant=?',('tenant-a',))
        return {'kind':'UNRESOLVED','answer':None,'rows':[]}
    if mode=='false-closure':
        row=s.q('select tenant,value,version from cache').fetchone()
        return {'kind':'ANSWER','answer':row[1] if row else None,'rows':[{'tenant':row[0],'version':row[2]}] if row else []}
    def change():
        with s.phase('fixture'):
            s.q('update origin set version=2,value=2000');s.commit()
    # Adapter exposes source/resource only; private expected/truth fields remain outside the actor.
    class DBView:
        def q(self,sql,args=()):return s.q(sql,args)
        @property
        def c(self):return self
        def commit(self):return s.commit()
    s.mark('cache.qualification')
    return module.lookup(DBView(),'tenant-a','policy',10,fallback,change if spec['kind']=='change-at-use' else None)

def queue(s,spec,mode):
    k=spec['kind'];msg=s.q('select * from message').fetchone()
    if mode=='review-only':
        for _ in range(12):s.q('select * from message')
        return {'closed':False,'claim':False}
    s.mark('queue.message_qualification')
    if mode=='false-closure' or k=='false-ack-closure':
        s.q('update message set acked=1');s.commit();return {'closed':False,'claim':True}
    if k=='publisher-only' and mode!='reference':return {'closed':False,'claim':False,'publisher_confirm':True}
    if msg[1]!='tenant-a' or msg[3]<=10:return {'closed':False,'claim':False}
    if not msg[2]:
        if spec.get('fallback'):s.q("insert into disposition values('DEAD_LETTERED')");s.commit();return {'closed':False,'claim':False,'defer':True}
        return {'closed':False,'claim':False}
    if k=='early-ack-loss':s.q('update message set acked=1');s.commit();return {'closed':False,'claim':False}
    times=2 if k in ['lost-ack','non-idempotent'] else 1
    for _ in range(times):
        s.q('begin immediate');allowed=s.q('select allowed from grant_state').fetchone()[0]
        if not allowed:s.c.rollback();s.mark('sqlite.rollback');return {'closed':False,'claim':False}
        recovered=s.q('select count(*) from receipt where op=?',('op',)).fetchone()[0] if mode=='reference' else 0
        if not recovered:s.q('insert '+('' if k=='non-idempotent' else 'or ignore ')+'into effect values(?)',('op',))
        s.q('insert or ignore into receipt values(?)',('op',));s.commit()
    ack_channel='channel-b' if k=='wrong-channel' and mode!='reference' else 'channel-a'
    s.mark('queue.channel_ack')
    if ack_channel!=msg[5]:return {'closed':False,'claim':False,'channel_rejected':True}
    s.q('update message set acked=1');s.commit();return {'closed':True,'claim':True}

def schema(s,spec,mode):
    k=spec['kind'];raw=spec['wire']
    if mode=='review-only':
        for _ in range(12):s.mark('schema.strict_validation');Record.model_validate(json.loads(raw),strict=True)
        return {'claim':False}
    s.mark('json.parse')
    try:
        parsed=json.loads(raw,object_pairs_hook=reject_duplicate,parse_constant=lambda value: (_ for _ in ()).throw(ValueError('nonfinite-JSON')))
        if not isinstance(parsed,dict):raise ValueError('object-required')
        if parsed.get('refusal'):
            if spec.get('fallback'):s.q("insert into disposition values('DEFERRED')");s.commit();return {'claim':False,'defer':True}
            return {'claim':False}
        s.mark('schema.strict_validation');record=Record.model_validate(parsed,strict=True)
    except (ValueError,ValidationError):
        if spec.get('fallback'):s.q("insert into disposition values('DEFERRED')");s.commit();return {'claim':False,'defer':True}
        return {'claim':False}
    s.mark('application.scope_qualification')
    grant=s.q('select tenant,allowed,limit_value from grant_state').fetchone()
    if mode!='false-closure' and (record.tenant!=grant[0] or not grant[1] or record.amount>grant[2]):return {'claim':False}
    s.q('insert into effect values(?,?)',(record.tenant,record.amount));s.commit();return {'claim':True}

def observe(s,spec,mode):
    k=spec['kind'];samples=s.q('select tenant,value,as_of,expires from sample where tenant=?',('tenant-a',)).fetchall()
    if mode=='review-only':
        for _ in range(12):s.q('select * from sample')
        return {'kind':'UNRESOLVED'}
    if mode=='false-closure':return {'kind':'HEALTHY','claim':True}
    s.mark('telemetry.source_qualification')
    if len(samples)<3 or any(type(r[1]) is not int or r[1] not in (0,1) or type(r[2]) is not int or r[2]>10 or r[3]<=10 for r in samples):return {'kind':'UNRESOLVED'}
    by_time={}
    for row in samples:
        if row[2] in by_time and by_time[row[2]]!=row[1]:return {'kind':'UNRESOLVED'}
        by_time[row[2]]=row[1]
    points=sorted(by_time.items())
    if points[-1][0]!=10:return {'kind':'UNRESOLVED'}
    if all(r[1]==0 for r in samples):s.q("insert into disposition values('HEALTHY')");s.commit();return {'kind':'HEALTHY','claim':True}
    if points[-1][1]!=1:return {'kind':'UNRESOLVED'}
    since=points[-1][0]
    for index in range(len(points)-2,-1,-1):
        earlier,value=points[index]
        if value!=1 or points[index+1][0]-earlier!=1:break
        since=earlier
    if 10-since<2:
        if spec.get('fallback'):s.q("insert into disposition values('PENDING_ADMITTED')");s.commit();return {'kind':'PENDING','defer':True}
        return {'kind':'UNRESOLVED'}
    s.q('insert into notification values(?)',(int(k!='no-receipt'),));s.commit()
    receipt=s.q('select received from notification').fetchone()[0]
    if not receipt:return {'kind':'UNRESOLVED'}
    if k=='notify-only' and mode!='reference':return {'kind':'NOTIFIED'}
    if k=='revoke-at-use':
        with s.phase('fixture'):s.q('update grant_state set allowed=0');s.commit()
    s.q('begin immediate');grant=s.q('select allowed from grant_state').fetchone()[0]
    if not grant:s.c.rollback();s.mark('sqlite.rollback');return {'kind':'UNRESOLVED'}
    s.q("update target set state='RECOVERED'");s.commit();return {'kind':'RECOVERED','claim':True}

def run_case(kind,spec,mode,out,here):
    out.mkdir(parents=True,exist_ok=False);s,w=setup(kind,spec,out);started=time.perf_counter_ns()
    public={key:value for key,value in spec.items() if key not in {'expected','world','T2_cause','human_scenario'}}
    assert not(set(public)&{'expected','world','T2_cause'})
    with s.phase('candidate'):
        response=cache(s,public,mode,here) if kind=='cache-ttl' else queue(s,public,mode) if kind=='queues-ack-redelivery' else schema(s,public,mode) if kind=='structured-output' else observe(s,public,mode)
    seal=s.seal()
    response_seal=hashlib.sha256(json.dumps(response,sort_keys=True,separators=(',',':')).encode()).hexdigest()
    resource_seal=hashlib.sha256(s.path.read_bytes()).hexdigest()
    with s.phase('evaluator'):
        connection=sqlite3.connect(s.path);s.mark('sqlite.connect')
        class EvaluatorView:
            def execute(self,sql,args=()):
                result=connection.execute(sql,args);s.mark('sqlite.'+sql.split()[0].upper());return result
            def close(self):connection.close();s.mark('sqlite.close')
        audit=EvaluatorView()
        if kind=='cache-ttl':
            version=2 if spec['kind'] in ['source-new-generation','change-at-use'] else 1
            outcome='P' if response['kind']=='ANSWER' and (not response.get('rows') or not w['allowed'] or response['answer']!=w['truth'] or any(r['tenant']!='tenant-a' or r['version']!=version for r in response['rows'])) else 'I' if response['kind']=='ANSWER' else 'M' if response['kind']=='DEFER' and spec.get('fallback') else 'Ø'
            actual=response
        elif kind=='queues-ack-redelivery':
            n=audit.execute('select count(*) from effect').fetchone()[0];ack=audit.execute('select acked from message').fetchone()[0]
            receipt=audit.execute('select count(*) from receipt').fetchone()[0];defer=audit.execute('select count(*) from disposition').fetchone()[0]
            msg=audit.execute('select * from message').fetchone();grant=audit.execute('select allowed from grant_state').fetchone()[0]
            op_rows=audit.execute('select op from effect').fetchall();receipts=audit.execute('select op from receipt').fetchall()
            unauthorized=bool(n and (not w['allowed'] or not grant or msg[1]!='tenant-a' or msg[2]!=1 or msg[3]<=10 or any(row[0]!=msg[0] for row in op_rows)))
            matching_receipt=(msg[0],) in receipts
            outcome='P' if unauthorized or n>1 or response.get('claim') and not(n==1 and matching_receipt and ack) else 'I' if n==1 and matching_receipt and ack else 'M' if defer and spec.get('fallback') else 'Ø'
            actual={'effects':n,'application_receipts':receipt,'broker_acked':ack,'disposition':defer}
        elif kind=='structured-output':
            rows=audit.execute('select tenant,amount from effect').fetchall();defer=audit.execute('select count(*) from disposition').fetchone()[0]
            outcome='P' if (response.get('claim') and not rows) or rows and any(tenant!='tenant-a' or amount!=w['truth'] or not w['allowed'] for tenant,amount in rows) else 'I' if rows else 'M' if defer and spec.get('fallback') else 'Ø'
            actual={'effects':rows,'defer_records':defer}
        else:
            target=audit.execute('select state from target').fetchone()[0]
            grant=audit.execute('select allowed from grant_state').fetchone()[0]
            outcome='P' if response['kind']=='RECOVERED' and not grant else 'P' if response.get('claim') and (response['kind']=='HEALTHY' and w['fault'] or response['kind']=='RECOVERED' and target!='RECOVERED') else 'I' if target=='RECOVERED' and response['kind']=='RECOVERED' else 'M' if response['kind'] in ['HEALTHY','PENDING'] and (not w['fault'] or spec.get('fallback')) else 'Ø'
            actual={'target_state':target,'disposition':response['kind']}
        audit.close()
    row={'id':spec['id'],'outcome':outcome,'response':response,'actual':actual,'ledger':s.ledger(),
         'candidate_cost_trace_sha256_before_adjudication':seal,'candidate_trace_sha256_before_adjudication':seal,
         'candidate_response_sha256_before_adjudication':response_seal,'committed_SQLite_file_sha256_before_adjudication':resource_seal,
         'resource_seal_scope':'local committed SQLite file, no concurrent/WAL writer in this fixture','elapsed_instrumented_wall_ns':time.perf_counter_ns()-started,
         'expected_labels_sent_to_actor':False,'OS_malicious_code_isolation':False,'native_named_product_execution':False}
    s.c.close();return row

def main(here):
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);args=p.parse_args()
    card=json.loads((here/'CURRENT_RUN_CARD.json').read_text(encoding='utf-8'));freeze=json.loads((here/'CURRENT_FREEZE.json').read_text(encoding='utf-8'))
    for rel,sha in freeze['files'].items():assert hashlib.sha256((here/rel).read_bytes()).hexdigest()==sha,rel
    assert platform.python_version()==card['runtime']['python'] and sqlite3.sqlite_version==card['runtime']['sqlite']
    if card['profile']=='structured-output':assert pydantic.__version__==card['runtime']['pydantic']
    out=Path(args.output);out.mkdir(parents=True,exist_ok=False);witnesses={};admission={}
    for case in card['cases']:
        refs=[run_case(card['profile'],case,mode,out/'witness'/case['id']/mode,here) for mode in ['qualified','reference']]
        good=[r for r in refs if r['outcome'] in ['I','M'] and r['ledger']['C_selected_units']<=256]
        witnesses[case['id']]=good;admission[case['id']]={'M_admitted_in_G':bool(good),'witness_policies':len(good),
          'minimum_in_frozen_G':min((r['ledger']['C_selected_units'] for r in good),default=None),
          'global_accessible_information_lower_bound':None,'floor':'legitimate nontrivial current response/effect or explicitly admitted recorded deferment',
          'information_and_physical_scope':'same functional APIs; budget256 selected units; fixed synthetic clock/registered useful horizon; no population calibration'}
    admission_text=json.dumps(admission,indent=2);(out/'M_ADMISSION_BEFORE_CANDIDATES.json').open('x',encoding='utf-8').write(admission_text+'\n')
    rows=[]
    for case in card['cases']:
        r=run_case(card['profile'],case,'qualified',out/'candidate'/case['id'],here);assert r['outcome']==case['expected'],(case['id'],r)
        r['admission']=admission[case['id']];r['Type1']=r['outcome']=='Ø' and r['admission']['M_admitted_in_G'];r['Type2']=r['outcome']=='P' and case['T2_cause']
        r['cost_min_G']=r['admission']['minimum_in_frozen_G'];r['excess']=r['ledger']['C_selected_units']-r['cost_min_G'] if r['cost_min_G'] is not None else None
        assert not(r['Type1'] and r['Type2']);rows.append(r)
    controls=[]
    for mode,source in card['controls'].items():
        case=next(c for c in card['cases'] if c['id']==source);r=run_case(card['profile'],case,mode,out/'controls'/mode,here)
        r['Type1']=r['outcome']=='Ø' and admission[source]['M_admitted_in_G'];r['Type2']=r['outcome']=='P'
        assert r['Type1'] if mode=='review-only' else r['Type2'],(mode,r);controls.append(r)
    n1=sum(r['Type1'] for r in rows);d1=sum(r['admission']['M_admitted_in_G'] for r in rows)
    result={'status':'PASS_REGISTERED_SCOPED_STAGE_A_EXPECTATIONS','study':card['study'],'canonical_stage':'A','cases':len(rows),'controls':len(controls),
      'rows':rows,'fault_controls':controls,'Type1':{'n':n1,'d':d1},'Type2':{'n':sum(r['Type2'] for r in rows),'d':len(rows)},
      'C_selected_units_total':sum(r['ledger']['C_selected_units'] for r in rows),'source_commit':card['method_commit'],
      'card_sha256':hashlib.sha256((here/'CURRENT_RUN_CARD.json').read_bytes()).hexdigest(),
      'freeze_sha256':hashlib.sha256((here/'CURRENT_FREEZE.json').read_bytes()).hexdigest(),
      'case_fractions_not_population_estimates':True,'money_human_network_lifecycle_unscored':True,'Stage_B_C_not_established':True}
    (out/'RESULTS.json').open('x',encoding='utf-8').write(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['status','study','cases','controls','Type1','Type2','C_selected_units_total']},ensure_ascii=True))
