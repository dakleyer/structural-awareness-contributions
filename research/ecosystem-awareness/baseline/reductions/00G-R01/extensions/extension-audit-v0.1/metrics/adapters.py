"""Original selected actors, new prospective observer/accounting adapters.

This is a same-author functional information boundary, not OS isolation.
Case expectations/private verdicts are never passed into the source actor APIs.
"""
import copy, hashlib, importlib.util, json, sqlite3, sys
from pathlib import Path
from ledger import Ledger, Counter, PublicKey, charge, connect, instrument_crypto

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'source'
sqlite3.connect = connect
sys.path.insert(0, str(SOURCE/'independent-dds-exercises-v0.1'))
sys.path.insert(0, str(SOURCE/'dds-hew-v0.1'))
import crypto_fixture as crypto
instrument_crypto(crypto)

PATHS = {
 'rag': 'rag/study.py', 'oauth-oidc': 'oauth-oidc/study.py',
 'mcp-tool-calling': 'mcp-tool-calling/study.py',
 'sql-transactions-idempotency': 'sql-transactions-idempotency/study.py',
 'durable-workflows-retries': 'durable-workflows-retries/study.py',
 'stamp-stpa': 'independent-dds-exercises-v0.1/stamp-stpa/run.py',
 'spiffe-jwt': 'independent-dds-exercises-v0.1/spiffe-jwt/run.py',
 'rats-jws': 'independent-dds-exercises-v0.1/rats-jws/run.py',
 'hew': 'dds-hew-v0.1/hew_runtime.py'
}
MODULES = {}
for name, path in PATHS.items():
    spec = importlib.util.spec_from_file_location('selected_'+name.replace('-','_'), SOURCE/path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    MODULES[name] = module
import hew_oracle

def card(name):
    return json.loads((SOURCE/Path(PATHS[name]).parent/'RUN_CARD.json').read_text(encoding='utf-8'))

def observe_effects(path, table='effects'):
    c = sqlite3.connect(path)
    rows = c.execute('select * from '+table).fetchall()
    c.close()
    return rows

def stamp(case, parameters, out, mode='baseline'):
    m = MODULES['stamp-stpa']; world = copy.deepcopy(case['world'])
    view = {k: world[k] for k in ('pump_running','maintenance','critical_supply','backup','authority','sensor_current','allow_defer')}
    plant = m.Plant(world); ledger = Ledger()
    with ledger.role('candidate'):
        charge('control.decide')
        def effect():
            charge('control.command_and_feedback')
            return plant.stop_and_observe()
        if mode == 'false_closure':
            # Deliberate open-loop control: observed failed stop is promoted to entry permission.
            if view['pump_running']: effect()
            result = {'stop': view['pump_running'], 'entry': True, 'defer': False,
                      'trace': ['stop-request-is-promoted-to-confirmed-stop']}
        elif mode == 'review_only':
            for _ in range(12): charge('control.repeated_state_review')
            result = {'stop': False, 'entry': False, 'defer': False, 'trace': ['unresolved-review']}
        else:
            result = m.decide(view, effect)
    with ledger.role('evaluator'):
        grade = m.judge(world, result)
        # Reconstruct actual plant state separately from the decision trace.
        assert plant.running == (world['pump_running'] and not(result['stop'] and world['stop_applied']))
    outcome = {'incomplete':'Ø'}.get(grade['outcome'],grade['outcome'])
    return {'outcome': outcome, 'cause': result['trace'][-1], 'effects': grade.get('hazards',[]),
            'cost': ledger.result(), 'logical_work': result.get('work'),
            'T2_mechanism': bool(outcome == 'P' and mode == 'false_closure'), 'actor_inputs': sorted(view)}

def spiffe(case, parameters, out, mode='baseline'):
    m = MODULES['spiffe-jwt']; c = card('spiffe-jwt'); mutations = case['mutations']
    trusted, other, rotated = crypto.FixtureIssuer(), crypto.FixtureIssuer(), crypto.FixtureIssuer('fixture-rotated')
    claims = dict(c['claim_base']); claims.update(mutations.get('claims',{}))
    for key in mutations.get('remove_claims',[]): claims.pop(key,None)
    issuer = rotated if mutations.get('rotated_key') else other if mutations.get('wrong_signer') else trusted
    raw = json.dumps(claims,separators=(',',':'))[:-1]+',"exp":1791299000}' if mutations.get('duplicate_claims') else None
    token = issuer.issue(claims,mutations.get('headers'),raw)
    if mutations.get('tamper_signature'):
        a,b,s = token.split('.'); token = a+'.'+b+'.'+('A' if s[0]!='A' else 'B')+s[1:]
    if mutations.get('oversized'): token = 'x'*8193
    keys = {trusted.kid:PublicKey(trusted.public_key)}
    if mutations.get('retired_key'): keys = {}
    if mutations.get('rotated_key'): keys = {rotated.kid:PublicKey(rotated.public_key)}
    context = {'sender':'spiffe://example.org/batch/client','tenant':'tenant-A','purpose':'batch-remediation',
               'capacity':mutations.get('capacity',True),'operation':case['id'],
               'grant':{'active':mutations.get('grant_active',True),'tenant':mutations.get('grant_tenant','tenant-A'),
                        'purpose':mutations.get('grant_purpose','batch-remediation')}}
    ledger = Ledger(); work = Counter(signature_verifications=0,application_policy_checks=0)
    result = None; reason = 'unresolved'; effects = {}
    with ledger.role('candidate'):
        for _ in range(12 if mode=='review_only' else 1):
            charge('identity.policy')
            try:
                if mode == 'reference':
                    # The sole admitted domain/bundle is already legitimate caller-visible information.
                    # Verify once, then qualify the signed subject; no untrusted payload preparse is needed.
                    result = crypto.verify(token,keys,'batch-service',mutations.get('now',c['reference_time']),work)
                    subject=result.get('sub')
                    if not isinstance(subject,str):raise crypto.Rejected('spiffe-subject-required')
                    u=m.urlsplit(subject)
                    if u.scheme!='spiffe' or u.netloc!='example.org' or u.query or u.fragment or '@' in u.netloc or ':' in u.netloc:
                        raise crypto.Rejected('invalid-selected-spiffe-id-or-domain')
                else:
                    result = m.identity(token,{'example.org':keys},mutations.get('now',c['reference_time']),work)
            except crypto.Rejected as error: reason = str(error); result = None; break
        if result is not None and mode != 'review_only':
            if mode == 'false_closure':
                charge('resource.unqualified_effect')
                effects[context['operation']] = {'tenant':context['tenant'],'purpose':context['purpose'],'action':'apply-batch'}
                reason = 'identity-is-promoted-to-complete-permission'
            else:
                for _ in range(2 if mutations.get('replay') else 1):
                    charge('resource.policy')
                    reason = m.qualified_receiver(result,context,effects,work)
    with ledger.role('evaluator'):
        authorized = context['grant']['active'] and context['grant']['tenant']==context['tenant'] and context['grant']['purpose']==context['purpose'] and context['capacity']
        outcome = 'P' if effects and not authorized else 'I' if effects else 'Ø'
    return {'outcome':outcome,'cause':reason,'effects':list(effects.values()),'cost':ledger.result(),
            'T2_mechanism':outcome=='P' and mode=='false_closure',
            'actor_inputs':['compact token','admitted bundles','time','application context'],
            'native_keys_or_tokens_exported':False}

def rats(case, parameters, out, mode='baseline'):
    m = MODULES['rats-jws']; c = card('rats-jws'); mu=case['mutations']; now=c['reference_time']; nonce='request-'+case['id']
    attester, bad_attester=crypto.FixtureIssuer('attester-key'),crypto.FixtureIssuer('attester-key')
    verifier,bad_verifier=crypto.FixtureIssuer('verifier-key'),crypto.FixtureIssuer('verifier-key')
    good=SOURCE/'independent-dds-exercises-v0.1/rats-jws/fixture_good.py'
    bad=SOURCE/'independent-dds-exercises-v0.1/rats-jws/fixture_changed.py'
    software=bad if mu.get('software')=='bad' else good
    reference=hashlib.sha256(good.read_bytes()).hexdigest()
    ledger=Ledger(); work=Counter(file_hash_reads=0,signature_verifications=0,application_policy_checks=0)
    with ledger.role('source_production'):
        evidence={'sub':mu.get('evidence_subject','case-service'),'aud':'local-verifier',
                  'exp':now-1 if mu.get('evidence_expired') else now+120,'nonce':mu.get('evidence_nonce',nonce),
                  'policy':mu.get('evidence_policy','software-policy-v1'),m.PREDICATE:m.measure(software,work)}
        if mu.get('false_measurement'): evidence[m.PREDICATE]=reference
        if mu.get('omit_measurement'): evidence.pop(m.PREDICATE)
        evidence_token=(bad_attester if mu.get('wrong_attester') else attester).issue(evidence)
        charge('crypto.sign')
    appraised=None; result_token=None; effect=None; reason='unresolved'
    with ledger.role('candidate'):
        for _ in range(12 if mode=='review_only' else 1):
            charge('attestation.appraisal')
            try: appraised=m.appraise(evidence_token,PublicKey(attester.public_key),{'id':'software-policy-v1','reference':reference},nonce,now,work)
            except crypto.Rejected as error: reason=str(error); appraised=None; break
    if appraised is not None and mode!='review_only':
        claims={'sub':'case-service','aud':mu.get('result_audience','local-relying-party'),
                'exp':now-1 if mu.get('result_expired') else now+60,'nonce':nonce,'policy':'software-policy-v1',
                m.PREDICATE:appraised[m.PREDICATE],'status':mu.get('result_status','PASS')}
        with ledger.role('source_production'):
            result_token=(bad_verifier if mu.get('wrong_verifier') else verifier).issue(claims);charge('crypto.sign')
        if mu.get('change_after_appraisal'): software=bad
        context={'now':now,'subject':'case-service','nonce':nonce,'policy':mu.get('receiving_policy','software-policy-v1'),
                 'grant':mu.get('grant_active',True),'capacity':mu.get('capacity',True),'current_source':mu.get('current_source',True),
                 'applied':mu.get('applied',True),'software_path':software}
        with ledger.role('candidate'):
            charge('attestation.receiving_policy')
            try:
                if mode=='false_closure':
                    accepted=crypto.verify(result_token,{'verifier-key':PublicKey(verifier.public_key)},'local-relying-party',now,work)
                    if accepted.get('status')=='PASS' and accepted.get('policy')==context['policy'] and context['grant'] and context['capacity']:
                        effect={'applied_software_sha256':accepted[m.PREDICATE],'subject':context['subject'],'policy':context['policy']}
                else: effect=m.consume(result_token,PublicKey(verifier.public_key),context,work)
                reason='local-confirmation' if mode!='false_closure' else 'snapshot-pass-is-promoted-to-current-state'
            except crypto.Rejected as error: reason=str(error)
    with ledger.role('evaluator'):
        actual=hashlib.sha256(software.read_bytes()).hexdigest()
        outcome='P' if effect and (actual!=reference or effect['applied_software_sha256']!=reference) else 'I' if effect else 'Ø'
    return {'outcome':outcome,'cause':reason,'effects':effect,'cost':ledger.result(),
            'T2_mechanism':outcome=='P' and mode=='false_closure','actor_inputs':['evidence/result JWS','public keys','policy','nonce','current file source'],
            'application_confirmation_remains_modelled':True,'native_keys_or_tokens_exported':False}

def rag(case, p, out, mode='baseline'):
    m=MODULES['rag']; ledger=Ledger(); path=out/'resource.sqlite'
    with ledger.role('fixture'):
        db=m.DB(path);m.setup(db,case['kind'],p['now'])
    private={'truth':p['truth'],'epoch':1}; params={k:p[k] for k in ['query','tenant','now']}
    response=None; reason='unresolved'
    with ledger.role('candidate'):
        for _ in range(12 if mode=='review_only' else 1):
            rows=m.retrieve(db,params,qualified=mode!='false_closure')
        if case['kind']=='change-before-use':
            with ledger.role('fixture'):
                db.q('update docs set revision=2,value=2000 where tenant=?',('tenant-a',));db.c.commit()
                private={'truth':2000,'epoch':2}
        charge('retrieval.qualification')
        if mode=='review_only': response={'kind':'UNRESOLVED','disclosed':[],'value':None}
        elif mode=='false_closure':
            response={'kind':'ANSWER','value':int(rows[0]['value']),'disclosed':[{'tenant':rows[0]['tenant'],'revision':int(rows[0]['revision']),'expires':int(rows[0]['expires'])}]} if rows else {'kind':'UNRESOLVED','disclosed':[],'value':None}
        else: response=m.answer(db,params,rows,case['fallback'])
    with ledger.role('evaluator'):
        outcome=m.adjudicate(response,private,params,case['fallback'])
    db.c.close()
    return {'outcome':outcome,'cause':response['kind'],'effects':response,'cost':ledger.result(),
            'T2_mechanism':outcome=='P','actor_inputs':['query','tenant','now','retrieved rows','admitted fallback'],
            'source_truth_limit':case['kind']=='false-source'}

def oauth(case,p,out,mode='baseline'):
    m=MODULES['oauth-oidc'];kind=case['kind'];is_id=kind in ['id-token','wrong-nonce']
    from cryptography.hazmat.primitives.asymmetric import rsa
    good=rsa.generate_private_key(public_exponent=65537,key_size=2048);bad=rsa.generate_private_key(public_exponent=65537,key_size=2048)
    claims={'iss':p['issuer'],'sub':'subject-a','aud':p['client'] if is_id else p['resource'],'exp':p['expires'],'iat':900,
            'jti':case['id'],'client_id':p['client'],'scope':'write','tenant':p['tenant']}
    if is_id:claims['nonce']=p['nonce']
    if kind=='wrong-audience':claims['aud']='resource-b'
    if kind=='expired':claims['exp']=p['now']
    if kind=='missing-scope':claims['scope']='read'
    if kind=='wrong-nonce':claims['nonce']='other-request'
    token=m.sign({'alg':'RS256','typ':'JWT' if is_id else 'at+jwt','kid':'fixture'},claims,bad if kind=='wrong-signer' else good)
    ledger=Ledger();work=Counter(signature_verifications=0,application_policy_checks=0,operational_sql_statements=0)
    path=out/'resource.sqlite'
    with ledger.role('fixture'):
        db=sqlite3.connect(path);db.execute('create table effects(operation text primary key,subject text)');db.commit()
    verified=None; reason='unresolved';identity=False
    with ledger.role('candidate'):
        for _ in range(12 if mode=='review_only' else 1):
            charge('token.validation');verified,reason=m.validate(token,PublicKey(good.public_key()),p,'login' if mode=='false_closure' and is_id else case['purpose'],work)
        ctx={'use_time':1011 if kind=='late-use' else p['now'],'current_grant':kind!='revoked-grant','operation':'operation-a'}
        if mode!='review_only':
            identity=bool(verified and case['purpose']=='login')
            if verified and case['purpose']=='resource':
                for _ in range(2 if kind=='duplicate' else 1):
                    if mode=='false_closure':
                        charge('resource.false_permission');db.execute('insert or ignore into effects values(?,?)',(ctx['operation'],verified['sub']));db.commit()
                    else:
                        charge('resource.policy');m.apply(db,verified,p,ctx,work)
    with ledger.role('evaluator'):
        effects=observe_effects(path)
        authority=kind not in ['wrong-audience','expired','wrong-signer','missing-scope','revoked-grant','late-use','wrong-nonce'] and not(kind=='id-token' and case['purpose']=='resource')
        outcome=m.adjudicate(len(effects),identity,{'purpose':case['purpose']},authority)
    db.close()
    return {'outcome':outcome,'cause':reason,'effects':effects,'cost':ledger.result(),
            'T2_mechanism':outcome=='P' and mode=='false_closure','actor_inputs':['token','issuer key','validation context','current resource grant'],
            'native_keys_or_tokens_exported':False}

def mcp(case,p,out,mode='baseline'):
    m=MODULES['mcp-tool-calling'];kind=case['kind'];ledger=Ledger()
    with ledger.role('fixture'):
        db=m.DB(out/'resource.sqlite')
        if kind=='self-reported-admin':db.c.execute('update grants set allowed=0');db.c.commit()
    meta={'io.modelcontextprotocol/protocolVersion':'2026-07-28','io.modelcontextprotocol/clientCapabilities':{},
          'io.modelcontextprotocol/clientInfo':{'name':'admin' if kind=='self-reported-admin' else 'fixture','version':'0.1'}}
    if kind=='missing-meta':meta.pop('io.modelcontextprotocol/clientCapabilities')
    args={'tenant':17 if kind=='wrong-args' else p['tenant'],'tier':p['tier'],'operation':'operation-a','expected_revision':1}
    request={'jsonrpc':'2.0','id':case['id'],'method':'tools/unsupported' if kind=='unknown-method' else 'tools/call',
             'params':{'name':p['tool'],'arguments':args,'_meta':meta}}
    registry={'name':p['tool'],'revision':2 if kind=='catalog-change' else 1,'annotations':{'readOnlyHint':kind=='misleading-annotation'}}
    def revoke():
        with ledger.role('fixture'):
            db.q('update grants set allowed=0');db.c.commit()
    wire=json.dumps(request,separators=(',',':'));responses=[]
    with ledger.role('candidate'):
        if mode=='review_only':
            for _ in range(12):charge('rpc.repeated_review');json.loads(wire)
        elif mode=='false_closure':
            charge('rpc.false_client_identity_permission')
            db.q('insert or ignore into effects values(?,?,?)',('operation-a','tenant-a','silver'));db.c.commit()
            responses=[{'result':'self-reported-client-is-promoted-to-authority'}]
        else:
            for _ in range(2 if kind=='duplicate' else 1):
                charge('rpc.qualification');responses.append(m.handle(wire,db,registry,revoke if kind=='grant-change' else None))
    with ledger.role('evaluator'):
        effects=observe_effects(out/'resource.sqlite')
        allowed=kind not in ['self-reported-admin','grant-change','catalog-change','wrong-args','unknown-method','missing-meta']
        outcome='Ø' if not effects else 'I' if len(effects)==1 and tuple(effects[0][1:])==('tenant-a','silver') and allowed else 'P'
    db.c.close()
    return {'outcome':outcome,'cause':'RPC reply' if responses else 'unresolved review','effects':effects,'cost':ledger.result(),
            'T2_mechanism':outcome=='P' and mode=='false_closure','actor_inputs':['serialized RPC','registry','resource grant queries']}

def sql(case,p,out,mode='baseline'):
    m=MODULES['sql-transactions-idempotency'];kind=case['kind'];ledger=Ledger();path=out/'resource.sqlite'
    with ledger.role('fixture'):
        db=m.DB(path)
        if kind=='no-grant':db.q('update grants set allowed=0');db.c.commit()
    operation='operation-a';payload='payload-a';history=[];external=0;false_receipt=False
    with ledger.role('candidate'):
        def apply(**kw):
            charge('transaction.policy')
            return m.operation(db,operation,payload,**kw)
        if mode=='review_only':
            for _ in range(12):db.q('select payload from ledger where operation=?',(operation,))
        elif kind=='stale-precheck':
            second=sqlite3.connect(path)
            db.q('select count(*) from ledger');db.q('select count(*) from ledger',c=second)
            history.extend([apply(),apply(c=second)]);second.close()
        elif kind=='payload-conflict':
            history.append(apply());payload='payload-b'
            if mode=='false_closure':
                db.q('select payload from receipt where operation=?',(operation,));false_receipt=True
                history.append('OLD_RECEIPT_IS_PROMOTED_TO_CURRENT_CLOSURE')
            else:history.append(apply())
        elif kind=='outside-domain':
            ext=sqlite3.connect(out/'external.sqlite');ext.execute('create table effects(value text)');ext.execute("insert into effects values('outside-primary')");ext.commit();ext.close()
            external=1;history.append(apply(rollback=True))
        else:
            history.append(apply(rollback=kind=='rollback',outbox=kind=='outbox-pending'))
            if kind=='duplicate':history.append(apply())
            if kind=='lost-ack':db.c.close();db.c=sqlite3.connect(path);history.append(apply())
    with ledger.role('evaluator'):
        actual=m.audit(path);matching=(operation,payload) in actual['receipt'] and (operation,payload) in actual['ledger']
        outcome='P' if external and not actual['ledger'] or false_receipt and not matching else 'I' if matching and kind!='outbox-pending' else 'Ø'
    db.c.close()
    return {'outcome':outcome,'cause':history[-1] if history else 'unresolved review','effects':actual,'cost':ledger.result(),
            'T2_mechanism':outcome=='P' and false_receipt,'P_without_T2':outcome=='P' and not false_receipt,
            'actor_inputs':['operation/payload','current grant','local receipt and ledger'], 'external_effect':external}

def workflow(case,p,out,mode='baseline'):
    m=MODULES['durable-workflows-retries'];kind=case['kind'];ledger=Ledger()
    source={'latency':10 if kind=='too-late' else 1,'fail_attempts':999 if kind in ['bounded-defer','retry-to-horizon'] else 2 if kind=='transient' else 0,
            'idempotent':kind!='non-idempotent','lose_first_ack':kind in ['lost-ack','non-idempotent'],
            'revoke_before_effect':kind=='grant-revoked','fallback_admitted':case['fallback']}
    with ledger.role('fixture'):
        db=m.DB(out/'resource.sqlite',source['idempotent'],2 if kind=='stale-worker' else 1)
    policy='bounded' if mode=='reference' and case['fallback'] else 'horizon' if kind in ['retry-to-horizon','transient'] else 'bounded'
    with ledger.role('candidate'):
        if mode=='review_only':
            for _ in range(12):db.q('select status,tick,attempts from workflow')
            controller={'reported_status':'RUNNING','tick':p['deadline_ticks'],'attempts':0}
        else:
            charge('workflow.policy');controller=m.run(db,p,source,policy)
    db.c.close()
    with ledger.role('evaluator'):
        actual=m.inspect(db.path,p,case['fallback'])
    return {'outcome':actual['outcome'],'cause':controller['reported_status'],'effects':actual,'cost':ledger.result(),
            'logical_elapsed_ticks':controller['tick'],
            'T2_mechanism':actual['outcome']=='P' and kind=='non-idempotent',
            'actor_inputs':['registered source simulation law','current SQLite grant','deadline','policy'],
            'source_simulation_law_is_visible_to_original_model':True}

def hew(case,p,out,mode='baseline'):
    m=MODULES['hew'];public=copy.deepcopy(case['public']);authority=copy.deepcopy(case['authority']);private=case['private']
    if mode=='reference' and not public['new_evidence']:public['restart_count']=0
    if mode=='review_only':public['restart_count']=public['work_budget']+1
    ledger=Ledger();path=out/'resource.sqlite'
    with ledger.role('fixture'):
        runtime=m.Runtime(path);runtime.provision_authority(public['operation_id'],authority)
        for subject,operation,kind,start,finish in case.get('prior_reservations',[]):
            runtime.db.execute('insert into reservations values(?,?,?,?,?)',(subject,operation,kind,start,finish))
    with ledger.role('candidate'):
        result=runtime.run_case(public)
    with ledger.role('evaluator'):
        grade=hew_oracle.judge(path,public,private,result)
        events=runtime.events();reservations=runtime.db.execute('select subject,operation_id,kind,start,finish from reservations').fetchall()
    runtime.close()
    outcome='P' if grade['violation_observed'] else 'I' if grade['sufficient_delivery'] else 'Ø'
    return {'outcome':outcome,'cause':result['reasons'],'effects':grade,'cost':ledger.result(),
            'model_work_units':grade['work_units'],'model_work_budget':public['work_budget'],
            'model_work_components':{'filing':1,'source_preparation':public['source_preparation_work'],
             'communication':2*len(public['affected_recipients']),
             'ack':sum(e['kind']=='OWNER_ACK' for e in events),
             'restarts':sum(e['kind']=='RESTART_RECORDED' for e in events),
             'review':public['review_service'] if any(e['kind']=='REVIEW_COMPLETED' for e in events) else 0,
             'qualification_bundle':5 if any(e['kind']=='REVIEW_COMPLETED' for e in events) else 0,
             'effect_confirmation_delivery':sum(e['kind'] in ['EFFECT_APPLIED','EFFECT_CONFIRMED','QUALIFIED_REENTRY_AND_DELIVERY'] for e in events)},
            'T2_mechanism':outcome=='P' and not private['basis_truth'],
            'actor_inputs':sorted(public),'reservations':reservations,
            'candidate_summary_cost_trusted':False,'physical_human_calibration':False}

ADAPTERS={'stamp-stpa':stamp,'spiffe-jwt':spiffe,'rats-jws':rats,'rag':rag,'oauth-oidc':oauth,
          'mcp-tool-calling':mcp,'sql-transactions-idempotency':sql,'durable-workflows-retries':workflow,'hew':hew}
