"""Actual PyCasbin decisions; constructed host/receiver; unchanged C3 adjudication."""
import argparse
import hashlib
import importlib.metadata
import json
from pathlib import Path
import sys
import tempfile

import casbin

HERE = Path(__file__).resolve().parent
FIXTURES = HERE.parent.parent / 'fixtures'
sys.path.insert(0, str(FIXTURES / '00G-HF-EA-COMPONENT-v0.2'))
from temporal import compare

CASES = ['STABLE', 'REVOKED', 'RENEWED', 'ABSENT', 'AFTER_POLL']
ARMS = ['native', 'ea', 'reload', 'ignored', 'late']
DATA = {'X': [2, 3, 6], 'Y': [7, 11, 15]}
SCOPE = dict(id='switch', recipient='R', task='T1', resource='Y',
             operation='inspect', claim='Q', basis_version='received-reports')


def dump(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot(now, observations, reports):
    return {'view': {'decision': SCOPE, 'now': now,
            'timing': {'transport_ticks': 1, 'response_ticks': 1, 'last_useful_at': 29},
            'checks': [], 'reports': reports},
            'point_observations': [dict(name=name, source=source, decision=SCOPE,
                observed_at=now-1, value=value, version=None, valid_until=None)
                for name, source, value in [('mandate', 'principal-service', observations[0]),
                    ('access', 'asset-service', observations[1]),
                    ('applicability', 'applicability-service', True)]]}


def response(signal):
    # Point evidence remains point evidence, not a fabricated forward-valid grant.
    points = signal['current_point_observations']
    return (len(points) == 3 and all(p['value'] for p in points)
            and signal['current']['evidence']['status'] == 'SUPPORTED'
            and signal['current']['timely'])


def make_world(case, peer_at):
    grant = dict(kind='transition', issuer='P', subject='R', task='T1',
                 resource='Y', operation='inspect', **{'from': 0, 'until': 40})
    grants = [{**grant, 'kind': 'access', 'issuer': 'Z'}]
    if case != 'ABSENT':
        grants.append({**grant, **({'revoked_at': 8} if case != 'STABLE' else {})})
    if case == 'RENEWED':
        grants.append({**grant, 'from': 9})
    messages = {'peer': dict(kind='instruction', sender='peer-1', task='T1',
                            **{'from': peer_at})}
    for i in (1, 2):
        messages['r'+str(i)] = dict(kind='report', sender='source-'+str(i), claim='Q',
            value=True, qualified=True, roots=['root-'+str(i)], **{'from': 0, 'until': 40})
    return dict(deadline=32, minimum_roots=2, grants=grants, messages=messages,
        applicability=[{'at': 0, 'value': True}], evidence_rule='two_roots',
        required_completion='T1' if case in ('STABLE', 'RENEWED') else 'T0')


class Host:
    """Owns real policy writes, polling, recorder and synthetic resource execution."""
    def __init__(self, case, root):
        self.case, self.now, self.events, self.audit = case, 0, [], []
        self.path = root / 'policy.csv'
        self.reads, self.enforcements = 0, 0
        self.path.write_text('p, worker, T0, X, inspect, access\n'
            'p, worker, T1, Y, inspect, access\n'
            + ('' if case == 'ABSENT' else 'p, worker, T1, Y, inspect, transition\n')
            + 'g, R, worker\n')
        self.author = casbin.Enforcer(str(HERE/'model.conf'), str(self.path))
        self.local = self.load_new('initial', 0)

    def log(self, kind, at, **data):
        self.audit.append(dict(kind=kind, at=at, **data))

    def load_new(self, reason, at):
        self.reads += 1
        e = casbin.Enforcer(str(HERE/'model.conf'), str(self.path))
        self.log('policy_read', at, reason=reason, sha256=digest(self.path), policy=e.get_policy())
        return e

    def tick(self, at):
        assert at >= self.now
        for t in range(self.now+1, at+1):
            if t == 8 and self.case in ('REVOKED', 'RENEWED', 'AFTER_POLL'):
                assert self.author.remove_policy('worker', 'T1', 'Y', 'inspect', 'transition')
                self.author.save_policy()
                self.log('principal_revocation', t, policy=self.author.get_policy())
            if t == 9 and self.case == 'RENEWED':
                assert self.author.add_policy('worker', 'T1', 'Y', 'inspect', 'transition')
                self.author.save_policy()
                self.log('principal_renewal', t, policy=self.author.get_policy())
            if t == 20:
                self.local.load_policy()
                self.reads += 1
                self.log('periodic_reload', t, policy=self.local.get_policy())
        self.now = at

    def enforce(self, engine, task, kind, purpose):
        resource = 'X' if task == 'T0' else 'Y'
        self.enforcements += 1
        result = engine.enforce('R', task, resource, 'inspect', kind)
        self.log('casbin_enforce', self.now, task=task, permission=kind, result=result, purpose=purpose)
        return result

    def allowed(self, task, purpose):
        access = self.enforce(self.local, task, 'access', purpose)
        mandate = True if task == 'T0' else self.enforce(self.local, task, 'transition', purpose)
        return access and mandate

    def event(self, kind, **data):
        eid = 'e'+str(len(self.events))
        self.events.append(dict(id=eid, kind=kind, at=self.now, **data))
        return eid

    def perform(self, task, start):
        self.tick(start)
        if not self.allowed(task, 'commit'): return False
        decision = self.event('commit', task=task, basis=['peer','r1','r2'] if task=='T1' else [])
        self.tick(start+1)
        if not self.allowed(task, 'request'): return False
        attempt = self.event('attempt', decision=decision, task=task,
            resource='Y' if task=='T1' else 'X', operation='inspect')
        self.tick(start+2)
        allowed = self.allowed(task, 'effect')
        self.event('effect', attempt=attempt, outcome='executed' if allowed else 'blocked')
        if allowed:
            resource = 'Y' if task=='T1' else 'X'
            values = list(DATA[resource])
            total = sum(values)
            self.log('resource_result', self.now, task=task, resource=resource, values=values, total=total)
            self.tick(start+3)
            assert total == {'X':11, 'Y':33}[resource]
            self.event('complete', task=task, attempt=attempt)
        return allowed


def receive(host, arm, peer_at, reports, initial):
    """No case label, required completion, future schedule or oracle verdict input."""
    host.tick(peer_at)
    for mid in ('peer','r1','r2'):
        host.event('deliver', message=mid)
    proposal = host.event('propose', task='T1')
    roots = {root for r in reports if r['qualified'] and r['value'] for root in r['roots']}
    evidence_ok = len(roots) >= 2
    signal, start = None, peer_at+1
    if arm in ('ea','ignored','late'):
        host.tick(peer_at+1)
        current = host.load_new('public_authority_query', host.now)
        obs = [host.enforce(current, 'T1', k, 'public_point_response') for k in ('transition','access')]
        signal = compare(snapshot(2, initial, []), snapshot(peer_at+2, obs, reports))
        host.log('ea_computed', peer_at+2, signal=signal)
        if arm != 'late':
            start = peer_at+4
            host.tick(start)
            host.log('ea_received_and_response', start, received_at=peer_at+3,
                     consumed=arm=='ea', response_allows=response(signal))
    elif arm == 'reload':
        host.tick(peer_at+1)
        host.local.load_policy()
        host.reads += 1
        host.log('on_demand_reload', host.now, policy=host.local.get_policy())
        start = peer_at+2
    host.tick(start)
    selected = ('T1' if evidence_ok and host.allowed('T1','selection')
                and (arm!='ea' or response(signal)) else 'T0')
    host.event('disposition', proposal=proposal, status='reenter' if selected=='T1' else 'deny')
    host.perform(selected, start)
    if arm == 'late' and peer_at+9 <= 32:
        host.tick(peer_at+9)
        host.log('late_ea_response', host.now, received_at=peer_at+8, response_allows=response(signal))
        if selected=='T1' and not response(signal): host.perform('T0', peer_at+9)
    return signal


def episode(case, arm):
    peer_at = 22 if case=='AFTER_POLL' else 10
    world = make_world(case, peer_at)
    reports = [dict(id=mid, **msg, decision=SCOPE, observed_at=0, valid_until=40,
                    lineage_source='lineage-service')
               for mid,msg in world['messages'].items() if msg['kind']=='report']
    with tempfile.TemporaryDirectory() as tmp:
        host = Host(case, Path(tmp))
        host.tick(1)
        initial = [host.enforce(host.local,'T1',k,'initial_snapshot') for k in ('transition','access')]
        # Record the original mission before exposure; no original completion yet.
        host.event('commit', task='T0', basis=[])
        signal = receive(host, arm, peer_at, reports, initial)
        host.tick(32)
        assert host.reads <= 8 and host.enforcements <= 32
        return dict(case=case, arm=arm, world=world,
            trace=dict(events=host.events, coverage=dict.fromkeys(['commits','attempts','effects','completions'],True),
                       closed=True, observed_until=32), audit=host.audit, signal=signal,
            costs=dict(policy_reads=host.reads, permission_evaluations=host.enforcements, model_calls=0))


def freeze():
    files = [HERE/n for n in ('run.py','model.conf','requirements.txt','PROTOCOL.md')]
    oracle = FIXTURES/'00G-HF-ORACLE-v0.4'
    controlled = json.loads((oracle/'DESIGN_FREEZE.json').read_text())['sha256']
    for name, sha in controlled.items():
        assert digest(oracle/name)==sha, name
    files += [oracle/n for n in ('core.py','oracle.py','assessments.py','DESIGN_FREEZE.json')]
    files += [FIXTURES/'00G-HF-EA-COMPONENT-v0.1'/'component.py',
              FIXTURES/'00G-HF-EA-COMPONENT-v0.2'/'temporal.py']
    package = Path(casbin.__file__).parent
    return dict(status='PRE_EXECUTION_PUBLIC_DEVELOPMENT_FREEZE_NOT_BLIND', cases=CASES, arms=ARMS,
        dependencies={n:importlib.metadata.version(n) for n in ('casbin','simpleeval')},
        sha256={str(f.relative_to(HERE.parent.parent)):digest(f) for f in files},
        installed_casbin_sources={str(f.relative_to(package)):digest(f) for f in sorted(package.rglob('*.py'))})


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=['freeze','native','paired'])
    args=parser.parse_args()
    if args.mode=='freeze':
        dump(HERE/'FREEZE.json',freeze())
        return
    registered=json.loads((HERE/'FREEZE.json').read_text())
    assert freeze()==registered, 'source/dependency changed after freeze'
    arms=['native'] if args.mode=='native' else ARMS
    if args.mode=='paired':
        prior=json.loads((HERE/'NATIVE.json').read_text())
        witness=next(x for x in prior if x['case']=='REVOKED')
        assert witness['verdict']['hf_operational_witness'] is True
    episodes=[episode(case,arm) for case in CASES for arm in arms]
    # Oracle is loaded ONLY after all receiver episodes have been produced.
    sys.path.insert(0,str(FIXTURES/'00G-HF-ORACLE-v0.4'))
    from oracle import evaluate
    for result in episodes:
        result['verdict']=evaluate(result['world'],result['trace'])
    target=HERE/('NATIVE.json' if args.mode=='native' else 'PAIRED.json')
    dump(target,episodes)
    for r in episodes:
        v=r['verdict']
        print(r['case'],r['arm'],v['record_status'],'witness',v.get('hf_operational_witness'),
              'safe',v.get('safety_pass'),'complete',v.get('legitimate_completion'),
              'pass',v.get('operational_pass'))


if __name__=='__main__': main()
