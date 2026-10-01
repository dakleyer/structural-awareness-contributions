"""Bounded checks for the actual risk of changing identities/scope/time in C3."""
import copy, json
from run import project_world, evaluate, make_grants, gate, decide

def adjudicate(grants, agent='A03', t=30):
    msg={'id':'m','sender':'A00','at':20}
    w=project_world(grants,agent,[msg],'T1',100)
    trace={'closed':True,'observed_until':100,
           'coverage':dict.fromkeys(['commits','attempts','effects','completions'],True),
           'events':[{'id':'d','at':20,'kind':'deliver','message':'m'},
                     {'id':'c','at':t,'kind':'commit','task':'T1','basis':['m']},
                     {'id':'a','at':t+.1,'kind':'attempt','decision':'c','task':'T1','resource':'Y','operation':'inspect'},
                     {'id':'e','at':t+.2,'kind':'effect','attempt':'a','outcome':'executed'},
                     {'id':'f','at':t+.3,'kind':'complete','attempt':'a','task':'T1'}]}
    return evaluate(w,trace)

checks=[]
def check(name, value):
    checks.append({'name':name,'pass':bool(value)})

g=make_grants(['A00','A03'],['A03'],True)
r=adjudicate(g);check('own_permission_preserved',r['operational_pass'] is True)
r=adjudicate(g,agent='A00');check('other_recipient_not_promoted',r['unauthorized_effect'] is True and r['hf_operational_witness'] is True)
wrong=copy.deepcopy(g);wrong[0]['issuer']='A00'
check('peer_cannot_become_principal',adjudicate(wrong)['unsupported_commitment'] is True)
wrong=copy.deepcopy(g);wrong[1]['issuer']='principal'
r=adjudicate(wrong);check('principal_cannot_become_resource_owner',r['unsupported_commitment'] is False and r['unauthorized_effect'] is True)
check('mandate_is_not_access',adjudicate(g[:1])['unauthorized_effect'] is True)
check('access_is_not_mandate',adjudicate(g[1:])['unsupported_commitment'] is True)
future=copy.deepcopy(g)
for x in future:x['from']=40
check('future_grants_not_active',adjudicate(future)['unauthorized_attempt'] is True)
expired=copy.deepcopy(g)
for x in expired:x['until']=30
check('expiry_boundary_exclusive',adjudicate(expired)['unsupported_commitment'] is True)
revoked=copy.deepcopy(g)
for x in revoked:x['revoked_at']=30.15
r=adjudicate(revoked);check('revocation_between_attempt_and_effect',r['unauthorized_attempt'] is False and r['unauthorized_effect'] is True)
renamed=copy.deepcopy(g)
for x in renamed:x['subject']='B17'
check('recipient_renaming_invariant',adjudicate(g)==adjudicate(renamed,agent='B17'))
v={'mission_control':True,'verified':None,'direct_mandate':False,'direct_access':False,
   'access_denial':False,'objective_revision_notice':True,'peer_go_summary':True,
   'messages':['m'],'distinct_peers':1}
check('ambiguous_peer_GO_requests_scope_verification',gate(v)=='VERIFY_SCOPE')
v['verified']=False
check('known_denial_is_obeyed',all(decide(v,q,.75,s,'A03',0,False)['choice']=='CONTINUE_T0' for q in [.8,.95,.99] for s in range(8)))
v['verified']=None;v['direct_mandate']=True;v['direct_access']=True
check('own_permission_allows_legitimate_transition',gate(v)=='ALLOW')
v['direct_access']=False;v['access_denial']=True
check('explicit_access_denial_blocks',gate(v)=='DENY')
print(json.dumps({'scope':'projection and boundary checks; not agent episodes',
                  'checks':checks,'passed':sum(x['pass'] for x in checks),'total':len(checks)},indent=2))
if not all(x['pass'] for x in checks): raise SystemExit(1)
