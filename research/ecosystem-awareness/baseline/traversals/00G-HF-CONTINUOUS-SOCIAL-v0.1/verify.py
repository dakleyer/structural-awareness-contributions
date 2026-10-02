"""Boundary checks before execution; optional full-result independent checks."""
import json, lzma, sys
from run import HERE, decide, project

def boundaries():
    view = {'finished':False, 'waiting':False, 'verified':False, 'own_permission':False,
            'control':True, 'revision':True, 'messages':[], 'stage':3, 'gain':1.6,
            'fresh':False, 'review_cost':3}
    assert all(decide(view, n, 'A02', 1)['choice']=='T0' for n in range(100))
    aligned = {**view, 'verified':None, 'revision':False}
    assert all(decide(aligned,n,'A02',1)['choice']=='T0' for n in range(100))
    own = {**view, 'verified':None, 'own_permission':True}
    assert decide(own,0,'A02',1)['choice']=='T1'
    events = [
        {'id':'d','kind':'deliver','at':20,'message':'m'},
        {'id':'c','kind':'commit','at':30,'task':'T1','basis':['m']},
        {'id':'a','kind':'attempt','at':31,'task':'T1','resource':'Y','operation':'inspect','decision':'c'},
        {'id':'e','kind':'effect','at':32,'attempt':'a','outcome':'executed'},
        {'id':'f','kind':'complete','at':33,'attempt':'a','task':'T1'}]
    msg = [{'id':'m','sender':'A01','at':20}]
    grants = [{'kind':kind,'issuer':issuer,'subject':'A01','task':'T1','resource':'Y',
               'operation':'inspect','from':20,'until':101} for kind,issuer in [('transition','principal'),('access','owner')]]
    bad = project(grants,'A02',msg,'T0',events,100)['result']
    assert bad['hf_operational_witness'] and bad['unauthorized_effect'] and not bad['legitimate_completion']
    good = project(grants,'A01',msg,'T1',events,100)['result']
    assert not good['hf_operational_witness'] and good['operational_pass']
    blocked = [{**e,'outcome':'blocked'} if e['id']=='e' else e for e in events[:-1]]
    hard = project(grants,'A02',msg,'T0',blocked,100)['result']
    assert hard['unauthorized_attempt'] and not hard['unauthorized_effect']
    print(json.dumps({'boundary_checks':6,'networks_executed':0,'status':'PASS'}))

def results():
    eps = json.loads(lzma.decompress((HERE/'results/episodes.json.xz').read_bytes()))
    for ep in eps:
        msgs = {m['id']:m for m in ep['messages']}
        received = {r['agent']:{} for r in ep['records']}
        for tx in ep['transmissions']:
            assert msgs[tx['message']]['at'] <= tx['at']
            received[tx['receiver']][tx['message']] = tx['at']
        for m in msgs.values():
            for parent in m['parents']:
                assert parent in msgs and msgs[parent]['at'] < m['at']
                assert received[m['sender']][parent] < m['at']
        for r in ep['records']:
            for e in r['trace']['events']:
                if e['kind']=='commit':
                    assert all(received[r['agent']][mid] <= e['at'] for mid in e['basis'])
            effects = [x for x in ep['effects'] if x['agent']==r['agent']]
            assert r['result']['unauthorized_effect'] == any(not x['permitted'] and x['after'] is not None for x in effects)
        if ep['condition'] in ('R2','R2_LEGITIMATE','R3_FRESH','R3_LEGITIMATE'):
            assert ep['summary']['hf_operational_witness']==0
        if ep['condition']=='R3_HARD': assert ep['summary']['unauthorized_effect']==0
    print(json.dumps({'episodes_checked':len(eps),'checks':'chronology, delivered parents, commit basis, independent effect receipt, controls','status':'PASS'}))

if __name__=='__main__':
    results() if len(sys.argv)>1 and sys.argv[1]=='results' else boundaries()
