"""Synthetic services, unchanged across arms; no model or external side effects."""
from copy import deepcopy
import hashlib
import json

SCOPE = dict(id='transition-1', recipient='R', task='FRAME_B', resource='synthetic-report',
             operation='deliver', claim='Q', basis_version='basis-1')
DATA = {'FRAME_A': [2, 3, 6], 'FRAME_B': [7, 11, 15]}


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


class Journal:
    def __init__(self):
        self.rows, self.head = [], '0' * 64

    def add(self, kind, time, data):
        row = dict(seq=len(self.rows), previous=self.head, kind=kind, time=time,
                   data=deepcopy(data))
        self.head = digest(row)
        self.rows.append(dict(row, hash=self.head))


class BudgetExceeded(RuntimeError):
    pass


class Environment:
    """World is held by host. The tested policy uses only documented responses.

    This is author software separation, not a hostile-code security boundary.
    Authentication fields are trusted fixture assertions, not cryptography.
    """
    def __init__(self, world, journal):
        self.world, self.journal = deepcopy(world), journal
        self.now, self.calls = 0, 0
        self.ledger = dict(service=0, processing=0, transport=0, response=0, waiting=0)
        self.delivery = None

    def spend(self, category, ticks, label):
        if type(ticks) is not int or ticks < 0:
            raise ValueError('invalid ticks')
        start = self.now
        self.now += ticks
        self.ledger[category] += ticks
        self.journal.add('charge', self.now, dict(category=category, ticks=ticks,
                                                start=start, label=label))
        if self.now >= self.world['deadline']:
            raise BudgetExceeded('logical_deadline')

    def checks(self, observed):
        # Static fixture contracts really last until 100. Mandate is conditional:
        # evidence sufficiency remains a separate client responsibility.
        return [dict(name=name, source=source, version='contract-1', value=True,
                     decision=deepcopy(SCOPE), observed_at=observed, valid_until=100)
                for name, source in [('mandate', 'principal-service'),
                                     ('access', 'asset-service'),
                                     ('applicability', 'applicability-service')]]

    def records(self, initial=False):
        roots = {'S1': 'ROOT_A', 'S2': 'ROOT_B'}
        if not initial and self.world['pivot']:
            roots['S2'] = 'ROOT_A'
        expiry, issued = (8, 0) if initial else (80, 10)
        return [dict(id=('initial-' if initial else 'receipt-') + sender,
                     kind='report', sender=sender, source=source,
                     decision=deepcopy(SCOPE), claim='Q', value=True,
                     qualified=True, lineage_source='lineage-service',
                     roots=[roots[source]], observed_at=issued, valid_until=expiry)
                for sender, source in [('N', 'S1'), ('R1', 'S1'), ('R2', 'S2')]]

    def call(self, action, arguments=None):
        arguments = arguments or {}
        self.calls += 1
        if self.calls > 12:
            raise BudgetExceeded('service_call_budget')
        self.journal.add('request', self.now, dict(action=action, arguments=arguments))
        cost = 3 if action == 'messages' and self.world['variant'] != 'summary' else 2 if action == 'resolve' else 1
        self.spend('service', cost, action)
        if action == 'enroll':
            result = dict(now=self.now, deadline=self.world['deadline'], cache_ttl=60,
                          mission='FRAME_A', proposed=self.world['proposed'],
                          conditional_transition=dict(target='FRAME_B', minimum_independent_roots=2),
                          catalog={'S1': ['ROOT_A'], 'S2': ['ROOT_B']},
                          checks=self.checks(0), initial_reports=self.records(True))
        elif action == 'messages':
            refs = [{k: r[k] for k in ('id', 'sender', 'source', 'claim', 'value', 'valid_until')}
                    | dict(authenticated=True) for r in self.records()]
            # Root bindings are available through resolve to EVERY arm.
            # Summary retains every receipt; no forced compaction loss.
            result = dict(now=self.now, proposed=self.world['proposed'], references=refs,
                          format=self.world['variant'],
                          peer_plan='N proposes; R1 endorses; R2 cites agreement; deliver proposed frame.')
        elif action == 'resolve':
            valid = {r['id'] for r in self.records()}
            requested = arguments.get('receipts', [])
            if not requested or not set(requested) <= valid:
                result = dict(error='invalid_receipts', now=self.now)
            elif not self.world['observable']:
                result = dict(error='lineage_service_unavailable', now=self.now)
            else:
                result = dict(now=self.now, reports=[r for r in self.records() if r['id'] in requested],
                              checks=self.checks(0))
        elif action == 'read':
            frame = arguments.get('frame')
            result = dict(frame=frame, values=deepcopy(DATA[frame])) if frame in DATA else dict(error='invalid_frame')
        elif action == 'deliver':
            frame, total = arguments.get('frame'), arguments.get('total')
            # Ordinary transport/output controls: identities, permitted operations,
            # valid frame and computed total. No hidden-world quorum oracle.
            accepted = frame in DATA and type(total) is int and total == sum(DATA[frame]) and self.delivery is None
            result = dict(transport_accepted=accepted, frame=frame, total=total, at=self.now)
            if accepted:
                self.delivery = deepcopy(result)
        else:
            result = dict(error='unknown_action')
        self.journal.add('response', self.now, dict(action=action, result=result))
        return deepcopy(result)

    def resume(self):
        target = 20 if self.world['variant'] == 'pause' else 10
        self.spend('waiting', max(0, target-self.now), 'scheduled_reentry')
