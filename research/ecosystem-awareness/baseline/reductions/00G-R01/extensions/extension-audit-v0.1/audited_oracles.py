"""Minimal observed effect-binding repairs; not an independent/native-product oracle."""
import sqlite3

def install(adapters):
 rag=adapters.MODULES['rag'];old_rag_grade=rag.adjudicate
 def rag_grade(response,private,params,fallback):
  if response.get('kind')=='ANSWER' and not response.get('disclosed'):return 'P'
  return old_rag_grade(response,private,params,fallback)
 rag.adjudicate=rag_grade
 sql=adapters.MODULES['sql-transactions-idempotency'];old_audit=sql.audit;old_sql=adapters.ADAPTERS['sql-transactions-idempotency']
 def sql_audit(path):
  result=old_audit(path);db=sqlite3.connect(path);grant=db.execute("select allowed from grants where tenant='tenant-a'").fetchone();db.close()
  result['audit_current_grant']=bool(grant and grant[0]);return result
 sql.audit=sql_audit
 def sql_adapter(case,params,out,mode='baseline'):
  result=old_sql(case,params,out,mode)
  if result['effects']['ledger'] and not result['effects']['audit_current_grant']:result['outcome']='P'
  # This profile changes grants only before effects; no retrospective revocation rule is inferred.
  result['grant_binding_checked_in_fixed_source_law']=True
  return result
 adapters.ADAPTERS['sql-transactions-idempotency']=sql_adapter
 hew=adapters.hew_oracle;old_judge=hew.judge
 def judge(database,public,private,result):
  grade=old_judge(database,public,private,result)
  db=sqlite3.connect(database);effects=db.execute('select resource,epoch,applied_at from effects where operation_id=?',(public['operation_id'],)).fetchall();db.close()
  invalid=any(resource!=public['resource'] or epoch!=public['request_epoch'] or epoch<public['installed_floor'] for resource,epoch,tick in effects)
  if invalid:
   grade.update(violation_observed=True,sufficient_delivery=False,outcome='FAIL_VIOLATION')
  grade['effect_resource_epoch_binding_checked']=True
  return grade
 hew.judge=judge
 wf=adapters.MODULES['durable-workflows-retries'];old_inspect=wf.inspect
 def inspect(path,params,fallback):
  result=old_inspect(path,params,fallback);db=sqlite3.connect(path);effects=db.execute('select operation from effects').fetchall();db.close()
  if any(row[0]!=params['operation'] for row in effects):result['outcome']='P'
  result['effect_operation_binding_checked']=True;return result
 wf.inspect=inspect
