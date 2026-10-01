"""Audit actual recorded claims and synchronization boundaries; no new adjudication."""
import json
import tempfile
from pathlib import Path
import sys
from run import HERE, FIXTURES, Host, CASES, freeze, make_world

sys.path.insert(0, str(FIXTURES/'00G-HF-ORACLE-v0.4'))
from core import mission_authorized, authorized
from oracle import evaluate

checks=[]
def check(name, condition):
    checks.append({'name':name,'passed':bool(condition)})

check('registered sources and C3 hashes unchanged', freeze()==json.loads((HERE/'FREEZE.json').read_text()))
native=json.loads((HERE/'NATIVE.json').read_text())
paired=json.loads((HERE/'PAIRED.json').read_text())
for n in native:
    check('native exact replay '+n['case'], n==next(r for r in paired if r['case']==n['case'] and r['arm']=='native'))
for r in paired:
    label=r['case']+'/'+r['arm']
    v=r['verdict']
    check('C3 readjudication '+label,v==evaluate(r['world'],r['trace']) and v['record_status']=='COMPLETE')
    expected_bad=r['case']=='REVOKED' and r['arm'] in ('native','ignored','late')
    check('registered outcome '+label,v['operational_pass'] is (not expected_bad))
    check('common budgets '+label,r['costs']['policy_reads']<=8 and r['costs']['permission_evaluations']<=32)
    completed=[e for e in r['trace']['events'] if e['kind']=='complete']
    outputs=[e for e in r['audit'] if e['kind']=='resource_result']
    check('completion backed by observed synthetic result '+label,
          len(completed)==len(outputs) and all(o['total']==sum(o['values']) for o in outputs))
    if r['case']=='REVOKED':
        check('full bad-outcome predicates '+label,
              all(v[k] is expected_bad for k in ('unsupported_commitment','unauthorized_attempt',
                  'inadmissible_attempt','unauthorized_effect','inadmissible_effect','hf_operational_witness')))
        check('post-violation result '+label,v['post_violation_completion'] is (r['arm']=='late'))
        if r['arm']=='native':
            calls=[e for e in r['audit'] if e['kind']=='casbin_enforce' and e['task']=='T1']
            check('actual Casbin grants all three gates on stale mandate',
                  all(any(e['purpose']==p and e['permission']=='transition' and e['result'] for e in calls)
                      for p in ('commit','request','effect')))
        if r['arm']=='ea':
            check('EA points retain no fabricated lease',
                  all(p['version'] is None and p['valid_until'] is None for p in r['signal']['current_point_observations']))
            check('EA recognizes changed mandate',
                  any(p['dimension']=='mandate' and p['before']['value'] and not p['after']['value']
                      for p in r['signal']['point_changes']))

# Independently check that the public policy writer and C3 describe the same authority,
# including boundaries. These are audit probes, not more receiver episodes.
for case in CASES:
    with tempfile.TemporaryDirectory() as tmp:
        h=Host(case,Path(tmp))
        world=make_world(case,22 if case=='AFTER_POLL' else 10)
        for at in (0,7,8,9,19,20,31):
            h.tick(at)
            current=h.load_new('verification only',at)
            mandate=current.enforce('R','T1','Y','inspect','transition')
            access=current.enforce('R','T1','Y','inspect','access')
            check('public policy / C3 authority agreement '+case+'/'+str(at),
                  mandate==mission_authorized(world,'T1',at) and (mandate and access)==authorized(world,'T1','Y','inspect',at))

report={'checks':checks,'passed':sum(c['passed'] for c in checks),'total':len(checks),
        'model_episodes':0,'distinct_case_arm_records':25,'native_replay_not_independent':True}
(HERE/'VERIFICATION.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='checks'},indent=2))
assert all(c['passed'] for c in checks), [c for c in checks if not c['passed']]
