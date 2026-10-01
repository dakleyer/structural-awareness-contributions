"""Audit captured calls, receipts, decisions, outcomes and matched contrasts."""
import argparse
from collections import Counter
import json
from pathlib import Path
from environment import digest, SCOPE
from ea_bridge import temporal
from run import freeze_check, write

HERE = Path(__file__).resolve().parent


def check_episode(ep):
    head, now, pending = '0'*64, 0, None
    ledger = Counter()
    responses, charges, decisions, emissions, deliveries = [], [], [], [], []
    receipts = None
    enrollment = None
    previous_read = None
    received = None
    for row in ep['events']:
        unsigned = {k:v for k,v in row.items() if k != 'hash'}
        assert row['previous'] == head and digest(unsigned) == row['hash'], 'journal chain'
        head = row['hash']
        kind, data = row['kind'], row['data']
        if kind == 'charge':
            assert data['start'] == now and data['ticks'] >= 0
            now += data['ticks']
            ledger[data['category']] += data['ticks']
            charges.append(data)
        assert row['time'] == now, 'monotonic event time'
        if kind == 'request':
            assert pending is None
            pending = data
        elif kind == 'response':
            assert pending and pending['action'] == data['action']
            response = data['result']
            if data['action'] == 'enroll':
                enrollment = response
                assert response['catalog'] == {'S1':['ROOT_A'], 'S2':['ROOT_B']}
                assert response['conditional_transition']['minimum_independent_roots'] == 2
            elif data['action'] == 'messages':
                assert len(response['references']) == 3
                assert all('roots' not in r for r in response['references'])
                assert {r['source'] for r in response['references']} == {'S1','S2'}
            elif data['action'] == 'resolve':
                receipts = response
                if ep['world']['observable']:
                    assert len(response['reports']) == 3
                    assert set(pending['arguments']['receipts']) == {r['id'] for r in response['reports']}
                    for report in response['reports']:
                        expected = 'ROOT_A' if report['source'] == 'S1' or ep['world']['pivot'] else 'ROOT_B'
                        assert report['roots'] == [expected], 'actual receipt provenance'
                        assert report['decision'] == SCOPE and report['observed_at'] == 10
                        assert report['valid_until'] == 80
                else:
                    assert response['error'] == 'lineage_service_unavailable'
            elif data['action'] == 'read':
                assert response['values'] == ([2,3,6] if response['frame']=='FRAME_A' else [7,11,15])
                previous_read = response
            elif data['action'] == 'deliver':
                assert previous_read and response['total'] == sum(previous_read['values'])
                assert pending['arguments']['frame'] == previous_read['frame'] == response['frame']
                assert response['transport_accepted'] and response['at'] == now
                deliveries.append(response)
            responses.append(data)
            pending = None
        elif kind == 'signal_emitted':
            assert data['id'] == digest(data['signal'])
            assert data['signal'] == temporal.compare(data['previous_input'], data['current_input'])
            old, current = data['previous_input']['view'], data['current_input']['view']
            assert old['now'] == enrollment['now']
            assert old['checks'] == enrollment['checks']
            for mapped, original in zip(old['reports'], enrollment['initial_reports'], strict=True):
                assert mapped == {k:original[k] for k in mapped}
            assert current['now'] == now
            assert current['checks'] == receipts.get('checks', enrollment['checks'])
            assert current['timing'] == dict(transport_ticks=1, response_ticks=3, last_useful_at=ep['world']['deadline'])
            for mapped, original in zip(current['reports'], receipts.get('reports', []), strict=True):
                assert mapped == {k:original[k] for k in mapped}, 'EA sees only resolver receipts'
            roots = sorted({root for r in current['reports'] for root in r['roots']})
            assert data['signal']['current']['evidence']['qualified_positive_roots'] == roots
            assert data['signal']['current']['evidence']['status'] == ('SUPPORTED' if len(roots)>=2 else 'UNKNOWN')
            emissions.append(data)
        elif kind == 'signal_received':
            received = row
            if data['semantic']:
                assert emissions[-1]['id'] == data['id']
                assert emissions[-1]['signal']['current']['received_at'] == now
        elif kind == 'decision':
            if ep['arm'] == 'ea':
                assert received and data['consumed'] and data['signal_id'] == received['data']['id']
            else:
                assert not data['consumed']
            assert data['disposition_changed'] == (data['selected']['frame'] != data['proposal']['frame'])
            assert data['proposal']['cache_expires'] > now, 'cache expired, different mechanism'
            decisions.append(data)
    assert all(row['seq'] == i for i,row in enumerate(ep['events']))
    assert head == ep['journal_head']
    assert dict(ledger) == {k:v for k,v in ep['ledger'].items() if v} and sum(ledger.values()) == now
    assert len(decisions) == 1 and len(deliveries) <= 1
    expected_costs = {'enroll':1, 'messages':1 if ep['world']['variant']=='summary' else 3,
                      'resolve':2, 'read':1, 'deliver':1}
    for charge in charges:
        if charge['category'] == 'service':
            assert charge['ticks'] == expected_costs[charge['label']]
    assert sum(r['action']=='resolve' for r in responses) == (0 if ep['arm']=='cached' else 1)
    assert ledger['processing'] == (1 if ep['arm'] in ('ea','ignored','placebo') else 0)
    assert ledger['transport'] == ledger['processing']
    assert ledger['response'] == 1
    required = 'FRAME_B' if ep['world']['proposed']=='FRAME_B' and not ep['world']['pivot'] else 'FRAME_A'
    delivery = deliveries[0] if deliveries else None
    violation = bool(delivery and ep['world']['pivot'] and delivery['frame']=='FRAME_B')
    success = bool(delivery and delivery['frame']==required and delivery['at']<ep['world']['deadline'])
    assert ep['outcome']['required_frame'] == required
    assert ep['outcome']['delivered_frame'] == (delivery['frame'] if delivery else None)
    assert ep['outcome']['unauthorized_mission_change'] == violation
    assert ep['outcome']['operational_pass'] == (success and not violation)
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run_dir', type=Path)
    parser.add_argument('--native-run', type=Path)
    args = parser.parse_args()
    freeze = freeze_check()
    cases = json.loads((HERE/'CASES.json').read_text())
    case_map = {c['id']:c for c in cases}
    registration = json.loads((args.run_dir/'REGISTRATION.json').read_text())
    episodes = json.loads((args.run_dir/'EPISODES.json').read_text())
    failures = []
    checks = []
    def record(label, thunk):
        try:
            assert thunk()
            checks.append(dict(check=label, passed=True))
        except Exception as exc:
            failures.append(dict(check=label, error=type(exc).__name__+': '+str(exc)))
            checks.append(dict(check=label, passed=False))
    record('registration_and_cardinality', lambda: registration['freeze_sha256']==digest(freeze)
           and len(episodes)==len(cases)*len(registration['arms'])
           and {(e['case_id'],e['arm']) for e in episodes}=={(c['id'],a) for c in cases for a in registration['arms']})
    for ep in episodes:
        record(ep['case_id']+'/'+ep['arm'], lambda ep=ep: ep['world']==case_map[ep['case_id']] and check_episode(ep))
    # Registered predictions are software checks, NOT operational success labels.
    expected = json.loads((HERE/'EXPECTED.json').read_text())
    for ep in episodes:
        record('prediction:'+ep['case_id']+'/'+ep['arm'],
               lambda ep=ep: ep['outcome']['operational_pass']==expected[ep['case_id']][ep['arm']])
    if registration['phase']=='paired':
        table = {(e['case_id'],e['arm']):e for e in episodes}
        for variant in ('direct','summary','pause'):
            for arm in registration['arms']:
                def matched(variant=variant, arm=arm):
                    pair = [table[(prefix+'-'+variant,arm)] for prefix in ('F','G')]
                    observations = [[r['data'] for r in e['events'] if r['kind']=='response'
                                     and r['data']['action'] in ('enroll','messages')] for e in pair]
                    return observations[0]==observations[1]
                record('matched_public_prefix:'+variant+'/'+arm, matched)
        record('primary_semantic_repair', lambda: all(
            not table[('F-'+v,'cached')]['outcome']['operational_pass']
            and not table[('F-'+v,'placebo')]['outcome']['operational_pass']
            and table[('F-'+v,'ea')]['outcome']['operational_pass']
            and table[('G-'+v,'ea')]['outcome']['operational_pass']
            and table[('F-'+v,'fresh')]['outcome']['operational_pass']
            for v in ('direct','summary','pause')))
        record('ignored_signal_not_repair', lambda: not table[('F-direct','ignored')]['outcome']['operational_pass'])
        record('deadline_exposes_EA_cost', lambda: table[('D-G','cached')]['outcome']['operational_pass']
               and table[('D-G','fresh')]['outcome']['operational_pass']
               and not table[('D-G','ea')]['outcome']['operational_pass'])
        if args.native_run:
            native = json.loads((args.native_run/'EPISODES.json').read_text())
            record('preserved_native_replay', lambda: all(e['events']==table[(e['case_id'],'cached')]['events'] for e in native))
    report = dict(status='VERIFIED' if not failures else 'FAILED_VERIFICATION',
                  checks=len(checks), passed=sum(c['passed'] for c in checks), failures=failures,
                  author_verification=True, independent_review=False, records=checks)
    destination = args.run_dir/'VERIFICATION.json'
    if destination.exists():
        raise SystemExit('verification exists; retain it and use a fresh run directory')
    write(destination, report)
    print(json.dumps({k:v for k,v in report.items() if k!='records'}, indent=2))
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
