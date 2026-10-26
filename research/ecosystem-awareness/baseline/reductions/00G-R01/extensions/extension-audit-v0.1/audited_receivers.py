"""Selected receiver repairs; own bounded prototypes, not native product implementations."""
import json,math
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def reject_constant(value):raise ValueError('nonfinite-JSON-constant')
def finite_number(value):return type(value) in (int,float) and (type(value) is int or math.isfinite(value))

def install(adapters):
 crypto=adapters.crypto
 def parse(value):
  adapters.charge('json.parse')
  try:
   obj=json.loads(crypto.unb64(value).decode('utf-8'),object_pairs_hook=crypto.no_duplicates,parse_constant=reject_constant)
   if not isinstance(obj,dict):raise crypto.Rejected('object-required')
   return obj
  except (UnicodeError,ValueError,TypeError) as exc:
   if isinstance(exc,crypto.Rejected):raise
   raise crypto.Rejected('invalid-json') from exc
 def verify(token,keys,audience,now,counter):
  if not isinstance(token,str) or len(token)>8192:raise crypto.Rejected('token-size')
  segments=token.split('.')
  if len(segments)!=3:raise crypto.Rejected('compact-jws-required')
  h,p,s=segments;head=parse(h)
  if set(head)-{'alg','kid','typ'}:raise crypto.Rejected('unsupported-header')
  if head.get('alg')!='RS256':raise crypto.Rejected('algorithm-outside-selected-rs256-profile')
  if head.get('typ') not in (None,'JWT','JOSE'):raise crypto.Rejected('invalid-typ')
  kid=head.get('kid')
  if not isinstance(kid,str) or kid not in keys:raise crypto.Rejected('unknown-key')
  counter['signature_verifications']+=1
  try:keys[kid].verify(crypto.unb64(s),(h+'.'+p).encode(),padding.PKCS1v15(),hashes.SHA256())
  except (InvalidSignature,ValueError) as exc:raise crypto.Rejected('invalid-signature') from exc
  claims=parse(p);exp=claims.get('exp');nbf=claims.get('nbf')
  if not finite_number(exp):raise crypto.Rejected('finite-expiration-required')
  if now>=exp:raise crypto.Rejected('expired')
  if nbf is not None and (not finite_number(nbf) or now<nbf):raise crypto.Rejected('not-yet-valid')
  aud=claims.get('aud')
  if not ((isinstance(aud,str) and aud==audience) or (isinstance(aud,list) and aud and all(isinstance(x,str) for x in aud) and audience in aud)):raise crypto.Rejected('audience-required-or-mismatch')
  return claims
 # Preserve instrumented json/native-verify metering; repairs add predicates inside existing policy entries.
 crypto.parse=parse;crypto.verify=verify
 spiffe=adapters.MODULES['spiffe-jwt'];spiffe.parse=parse;spiffe.verify=verify;old_identity=spiffe.identity
 old_split=spiffe.urlsplit
 def split(value):
  try:return old_split(value)
  except (ValueError,TypeError) as exc:raise crypto.Rejected('invalid-selected-spiffe-id') from exc
 spiffe.urlsplit=split
 def identity(token,bundles,now,cost):
  if not isinstance(token,str):raise crypto.Rejected('compact-jws-required')
  try:return old_identity(token,bundles,now,cost)
  except (ValueError,TypeError) as exc:
   if isinstance(exc,crypto.Rejected):raise
   raise crypto.Rejected('invalid-selected-spiffe-id') from exc
 spiffe.identity=identity
 rats=adapters.MODULES['rats-jws'];rats.verify=verify;old_consume=rats.consume
 def consume(token,key,context,cost):
  try:return old_consume(token,key,context,cost)
  except KeyError as exc:raise crypto.Rejected('required-result-claim-missing') from exc
 rats.consume=consume
 oauth=adapters.MODULES['oauth-oidc']
 def validate(token,key,p,purpose,work):
  try:
   if not isinstance(token,str) or len(token)>16000:return None,'oversized-or-type'
   a,b,c=token.split('.');h=json.loads(crypto.unb64(a).decode('utf-8'),object_pairs_hook=oauth.unique,parse_constant=reject_constant);x=json.loads(crypto.unb64(b).decode('utf-8'),object_pairs_hook=oauth.unique,parse_constant=reject_constant)
   if not isinstance(h,dict) or not isinstance(x,dict):return None,'object-required'
   if h.get('alg')!='RS256':return None,'algorithm'
   work['signature_verifications']+=1;key.verify(crypto.unb64(c),(a+'.'+b).encode(),padding.PKCS1v15(),hashes.SHA256())
   if x.get('iss')!=p['issuer']:return None,'issuer'
   if not isinstance(x.get('sub'),str) or not x['sub']:return None,'subject'
   if type(x.get('exp')) is not int or x['exp']<=p['now']:return None,'expired'
   if purpose=='login':
    if h.get('typ')!='JWT' or x.get('aud')!=p['client'] or x.get('nonce')!=p['nonce']:return None,'login-binding'
   else:
    typ=h.get('typ','');scope=x.get('scope','')
    if not isinstance(typ,str) or typ.lower() not in ['at+jwt','application/at+jwt']:return None,'token-purpose'
    if x.get('aud')!=p['resource']:return None,'resource-audience'
    if not isinstance(scope,str) or p['scope'] not in scope.split():return None,'scope'
   return x,'valid'
  except (UnicodeError,ValueError,TypeError,KeyError,InvalidSignature):return None,'signature-or-parse'
 oauth.validate=validate
 mcp=adapters.MODULES['mcp-tool-calling']
 def handle(wire,db,registry,before_use=None):
  try:
   r=json.loads(wire,object_pairs_hook=mcp.unique,parse_constant=reject_constant)
   if not isinstance(r,dict) or type(r.get('id')) not in (int,str):return {'error':-32600}
   if r.get('jsonrpc')!='2.0':return {'error':-32600}
   if r.get('method')!='tools/call':return {'error':-32601}
   p=r.get('params')
   if not isinstance(p,dict) or not isinstance(p.get('_meta',{}),dict) or not isinstance(p.get('arguments'),dict):return {'error':-32602}
   meta=p.get('_meta',{})
   if meta.get('io.modelcontextprotocol/protocolVersion')!='2026-07-28' or not isinstance(meta.get('io.modelcontextprotocol/clientCapabilities'),dict):return {'error':-32602}
   if p.get('name')!=registry['name']:return {'error':-32602}
   a=p['arguments']
   if set(a)!={'tenant','tier','operation','expected_revision'} or any(type(a[k]) is not str for k in ['tenant','tier','operation']) or type(a['expected_revision']) is not int:return {'error':-32602}
   if a['tier']!='silver' or a['expected_revision']!=registry['revision']:return {'error':-32000,'reason':'local-contract'}
   allowed=db.q('select allowed from grants where tenant=?',(a['tenant'],)).fetchone()
   if not allowed or not allowed[0]:return {'error':-32000,'reason':'local-authority'}
   if before_use:before_use()
   db.q('begin immediate');current=db.q('select allowed from grants where tenant=?',(a['tenant'],)).fetchone()
   if not current or not current[0]:db.c.rollback();return {'error':-32000,'reason':'current-local-authority'}
   db.q('insert or ignore into effects values(?,?,?)',(a['operation'],a['tenant'],a['tier']));db.c.commit()
   return {'jsonrpc':'2.0','id':r['id'],'result':{'content':[{'type':'text','text':'local effect admitted'}],'isError':False}}
  except (UnicodeError,ValueError,KeyError,TypeError):return {'error':-32602}
 mcp.handle=handle
