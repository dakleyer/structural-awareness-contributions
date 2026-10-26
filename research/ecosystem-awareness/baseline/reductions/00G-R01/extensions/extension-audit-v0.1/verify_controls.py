"""Known-defect regression controls plus positives, not a blind/population campaign."""
import argparse,copy,hashlib,importlib.util,json,sys
from pathlib import Path
from cryptography.hazmat.primitives.asymmetric import rsa
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'metrics'))
import adapters
import audited_receivers,audited_oracles
audited_receivers.install(adapters);audited_oracles.install(adapters)
spec=importlib.util.spec_from_file_location('audit_series',HERE/'series2/_series2_support/complete_runner.py');series=importlib.util.module_from_spec(spec);spec.loader.exec_module(series)

def run(output):
 out=Path(output);out.mkdir(parents=True,exist_ok=False);rows=[]
 def capture(id,expected,fn):
  try:
   actual=fn();passed=actual==expected
   rows.append({'id':id,'expected':expected,'actual':actual,'pass':passed})
   assert passed,(id,actual,expected)
  except Exception as error:
   if isinstance(error,AssertionError):raise
   rows.append({'id':id,'expected':expected,'actual':None,'pass':False,'exception':type(error).__name__})
   raise
 def rejected(fn):
  try:fn();return False
  except adapters.crypto.Rejected:return True
 card=lambda name:json.loads((HERE/'series2'/name/'CURRENT_RUN_CARD.json').read_text(encoding='utf-8'))
 def sc(wire):
  c=copy.deepcopy(card('structured-output')['cases'][0]);c['wire']=wire
  return series.run_case('structured-output',c,'qualified',out/('shape-'+str(len(rows))),HERE/'series2/structured-output')['outcome']
 for n,wire in enumerate(['[]','null','17','"scalar"','{"amount":NaN}','{"amount":1e999}']):capture('schema-shape-'+str(n),'Ø',lambda wire=wire:sc(wire))
 mcp=adapters.MODULES['mcp-tool-calling'];db=mcp.DB(out/'mcp.sqlite');reg={'name':'local-tool','revision':1}
 for n,wire in enumerate(['[]','null','{"jsonrpc":"2.0","id":1,"method":"tools/call","params":[]}','{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"_meta":[]}}','{"jsonrpc":"2.0","id":true,"method":"tools/call","params":{}}']):
  capture('mcp-shape-'+str(n),True,lambda wire=wire:'error' in mcp.handle(wire,db,reg))
 db.c.close()
 oauth=adapters.MODULES['oauth-oidc'];param=adapters.card('oauth-oidc')['parameters'];key=rsa.generate_private_key(public_exponent=65537,key_size=2048)
 base={'iss':param['issuer'],'sub':'subject-a','aud':param['resource'],'exp':param['expires'],'scope':param['scope'],'tenant':param['tenant']}
 for n,(head,payload) in enumerate([([],base),({'alg':'RS256','typ':'at+jwt'},[]),({'alg':'RS256','typ':'at+jwt'},{**base,'scope':[]}),({'alg':'RS256','typ':[]},base)]):
  token=oauth.sign(head,payload,key);capture('oauth-shape-'+str(n),True,lambda token=token:oauth.validate(token,key.public_key(),param,'resource',{'signature_verifications':0})[0] is None)
 token=oauth.sign({'alg':'RS256','typ':'at+jwt'},base,key)
 capture('oauth-positive',True,lambda:oauth.validate(token,key.public_key(),param,'resource',{'signature_verifications':0})[0] is not None)
 capture('oauth-signature-invalid-base64url',True,lambda:oauth.validate(token+'$',key.public_key(),param,'resource',{'signature_verifications':0})[0] is None)
 crypto=adapters.crypto;issuer=crypto.FixtureIssuer();keys={issuer.kid:issuer.public_key}
 for n,value in enumerate([float('nan'),float('inf'),float('-inf')]):
  token=issuer.issue({'sub':'spiffe://example.org/batch/client','aud':'batch-service','exp':value})
  capture('jws-nonfinite-'+str(n),True,lambda token=token:rejected(lambda:crypto.verify(token,keys,'batch-service',1000,{'signature_verifications':0})))
 token=issuer.issue({'sub':'spiffe://example.org/batch/client','aud':'batch-service','exp':1010},{'kid':[]})
 capture('jws-kid-shape',True,lambda:rejected(lambda:crypto.verify(token,keys,'batch-service',1000,{'signature_verifications':0})))
 token=issuer.issue({'sub':'spiffe://example.org/batch/client','aud':'batch-service','exp':1010})
 capture('jws-positive',True,lambda:bool(crypto.verify(token,keys,'batch-service',1000,{'signature_verifications':0})))
 spiffe=adapters.MODULES['spiffe-jwt'];capture('spiffe-token-type',True,lambda:rejected(lambda:spiffe.identity(None,{'example.org':keys},1000,{'signature_verifications':0})))
 token=issuer.issue({'sub':'spiffe://[broken','aud':'batch-service','exp':1010})
 capture('spiffe-malformed-uri',True,lambda:rejected(lambda:spiffe.identity(token,{'example.org':keys},1000,{'signature_verifications':0})))
 rats=adapters.MODULES['rats-jws'];verifier=crypto.FixtureIssuer('verifier-key');now=1000
 token=verifier.issue({'sub':'case-service','aud':'local-relying-party','exp':1010,'nonce':'n','policy':'software-policy-v1','status':'PASS'})
 context={'now':now,'subject':'case-service','nonce':'n','policy':'software-policy-v1','grant':True,'capacity':True,'current_source':True,'applied':True,'software_path':adapters.SOURCE/'independent-dds-exercises-v0.1/rats-jws/fixture_good.py'}
 capture('rats-missing-result-measurement',True,lambda:rejected(lambda:rats.consume(token,verifier.public_key,context,{'signature_verifications':0,'application_policy_checks':0,'file_hash_reads':0})))
 def queue_mutant(s,spec,mode):
  s.q("insert into effect values('op')");s.q("insert into receipt values('op')");s.q('update message set acked=1');s.commit();return {'claim':True,'closed':True}
 old=series.queue;series.queue=queue_mutant
 for id in ['Q08','Q09','Q10']:
  c=next(c for c in card('queues-ack-redelivery')['cases'] if c['id']==id)
  capture('queue-illegitimate-'+id,'P',lambda c=c:series.run_case('queues-ack-redelivery',c,'qualified',out/('queue-'+c['id']),HERE/'series2/queues-ack-redelivery')['outcome'])
 def wrong_op(s,spec,mode):
  s.q("insert into effect values('other')");s.q("insert into receipt values('other')");s.q('update message set acked=1');s.commit();return {'claim':True,'closed':True}
 series.queue=wrong_op;c=card('queues-ack-redelivery')['cases'][0];capture('queue-wrong-effect-operation','P',lambda:series.run_case('queues-ack-redelivery',c,'qualified',out/'queue-wrong-op',HERE/'series2/queues-ack-redelivery')['outcome']);series.queue=old
 old=series.schema;series.schema=lambda s,spec,mode:{'claim':True};c=card('structured-output')['cases'][0];capture('schema-ghost-effect','P',lambda:series.run_case('structured-output',c,'qualified',out/'schema-ghost',HERE/'series2/structured-output')['outcome']);series.schema=old
 old=series.cache;series.cache=lambda s,spec,mode,here:{'kind':'ANSWER','answer':1000,'rows':[]};c=card('cache-ttl')['cases'][0];capture('cache-no-source-binding','P',lambda:series.run_case('cache-ttl',c,'qualified',out/'cache-ghost',HERE/'series2/cache-ttl')['outcome']);series.cache=old
 def obs_mutant(s,spec,mode):
  s.q('update grant_state set allowed=0');s.q("update target set state='RECOVERED'");s.commit();return {'claim':True,'kind':'RECOVERED'}
 old=series.observe;series.observe=obs_mutant;c=card('observability-response')['cases'][0];capture('observe-unauthorized-effect','P',lambda:series.run_case('observability-response',c,'qualified',out/'obs-unauth',HERE/'series2/observability-response')['outcome']);series.observe=old
 for variant in ['reset','future','gap']:
  path=out/('obs-'+variant);path.mkdir();c=card('observability-response')['cases'][0];s,private=series.setup('observability-response',c,path)
  if variant=='reset':s.q('update sample set value=0 where as_of=9')
  elif variant=='future':s.q('update sample set as_of=11 where as_of=10')
  else:s.q('update sample set as_of=5 where as_of=8')
  s.commit()
  with s.phase('candidate'):response=series.observe(s,c,'qualified')
  s.c.close();capture('observe-for-'+variant,'UNRESOLVED',lambda response=response:response['kind'])
 wf=adapters.MODULES['durable-workflows-retries'];params=adapters.card('durable-workflows-retries')['parameters'];db=wf.DB(out/'workflow.sqlite');db.q("insert into effects values('wrong-operation')");db.q("update workflow set status='DONE',tick=1");db.c.commit();db.c.close();capture('workflow-wrong-operation','P',lambda:wf.inspect(db.path,params,False)['outcome'])
 rag=adapters.MODULES['rag'];params=adapters.card('rag')['parameters'];capture('rag-answer-no-evidence','P',lambda:rag.adjudicate({'kind':'ANSWER','value':params['truth'],'disclosed':[]},{'truth':params['truth'],'epoch':1},params,False))
 sql=adapters.MODULES['sql-transactions-idempotency'];old_op=sql.operation
 def unauthorized(db,op,payload,**kw):
  db.q('insert into ledger values(?,?)',(op,payload));db.q('insert into receipt values(?,?)',(op,payload));db.c.commit();return 'COMMITTED'
 sql.operation=unauthorized;sc=adapters.card('sql-transactions-idempotency');case=next(c for c in sc['cases'] if c['kind']=='no-grant');path=out/'sql-denied';path.mkdir()
 capture('sql-effect-without-grant','P',lambda:adapters.ADAPTERS['sql-transactions-idempotency'](case,sc['parameters'],path)['outcome']);sql.operation=old_op
 hc=adapters.card('hew')['scenarios'][0];public=hc['public_cases'][0];authority=hc['environment_authority_inputs'][0];private=hc['private_worlds'][0]
 for n,(column,value) in enumerate([('resource','wrong-resource'),('epoch',0)]):
  path=out/('hew-'+column+'.sqlite');r=adapters.MODULES['hew'].Runtime(path);r.provision_authority(public['operation_id'],authority);controller=r.run_case(copy.deepcopy(public));r.db.execute('update effects set '+column+'=?',(value,));r.db.commit();r.close()
  capture('hew-effect-'+column,True,lambda path=path:adapters.hew_oracle.judge(path,public,private,controller)['violation_observed'])
 result={'status':'PASS_KNOWN_DEFECT_REPAIR_CONTROLS','cases':len(rows),'rows':rows,'known_defects_used_to_select_controls':True,'independent_blind_or_population_validation':False,'model_native_product_execution':False}
 (out/'RESULTS.json').open('x',encoding='utf-8').write(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps({'status':result['status'],'cases':len(rows)}))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);run(p.parse_args().output)
