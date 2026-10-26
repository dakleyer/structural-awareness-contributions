"""HEW DDS deterministic model integration, version0.1.

SQLite is the actual local digital actuator/recorder in this fixture. Identity,
attestation and policy facts are supplied model assertions, not native validators.
No private world/expected verdict is accepted by this controller API.
"""
from pathlib import Path
import hashlib
import json
import sqlite3

VERSION = 'HEW-DDS-SQLITE-MODEL-0.2'
PUBLIC_KEYS = frozenset({
    'operation_id','scenario_id','tenant','principal','deputy','resource','action',
    'arrival','ack_deadline','decision_deadline','application_deadline','delivery_deadline',
    'horizon','review_service','application_duration','delivery_duration','gate_latency',
    'owner','reviewers','evidence','identity_accepted','state_appraisal','capacity_observation',
    'grant','request_epoch','token_verified','token_resource','token_actor','installed_floor',
    'human_choice','continuity','command_id','semantic_binding','semantic_contract','restart_count',
    'new_evidence','reply_lost','effect_query_available','work_budget','native_execution',
    'affected_recipients','source_preparation_work'
})


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False)


def earliest_slot(busy, arrival, service):
    candidate = arrival
    for start, end in sorted(busy):
        if end <= candidate:
            continue
        if candidate + service <= start:
            break
        candidate = end
    return candidate


class Runtime:
    def __init__(self, database):
        self.path = str(database)
        self.db = sqlite3.connect(self.path, timeout=10, isolation_level=None)
        self.db.execute('PRAGMA foreign_keys=ON')
        self.db.execute('PRAGMA journal_mode=WAL')
        self.db.executescript('''
        CREATE TABLE IF NOT EXISTS cases(operation_id TEXT PRIMARY KEY, tenant TEXT NOT NULL,
          principal TEXT NOT NULL, owner TEXT NOT NULL, payload TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS events(seq INTEGER PRIMARY KEY AUTOINCREMENT,
          operation_id TEXT NOT NULL REFERENCES cases(operation_id), tick INTEGER NOT NULL,
          kind TEXT NOT NULL, detail TEXT NOT NULL, previous_hash TEXT NOT NULL, hash TEXT NOT NULL);
        CREATE TRIGGER IF NOT EXISTS events_no_update BEFORE UPDATE ON events
          BEGIN SELECT RAISE(ABORT,'append-only event API'); END;
        CREATE TRIGGER IF NOT EXISTS events_no_delete BEFORE DELETE ON events
          BEGIN SELECT RAISE(ABORT,'append-only event API'); END;
        CREATE TABLE IF NOT EXISTS reservations(subject TEXT NOT NULL, operation_id TEXT NOT NULL,
          kind TEXT NOT NULL, start INTEGER NOT NULL, finish INTEGER NOT NULL);
        CREATE TABLE IF NOT EXISTS floors(resource TEXT PRIMARY KEY, epoch INTEGER NOT NULL);
        CREATE TABLE IF NOT EXISTS authority_inputs(operation_id TEXT PRIMARY KEY, payload TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS notifications(operation_id TEXT NOT NULL, recipient TEXT NOT NULL,
          payload TEXT NOT NULL, received_at INTEGER, PRIMARY KEY(operation_id,recipient));
        CREATE TABLE IF NOT EXISTS outbox(operation_id TEXT NOT NULL, recipient TEXT NOT NULL,
          payload TEXT NOT NULL, received_at INTEGER, relayed INTEGER NOT NULL DEFAULT 0,
          PRIMARY KEY(operation_id,recipient));
        CREATE TABLE IF NOT EXISTS effects(command_id TEXT PRIMARY KEY, operation_id TEXT NOT NULL,
          fingerprint TEXT NOT NULL, resource TEXT NOT NULL, action TEXT NOT NULL, epoch INTEGER NOT NULL,
          applied_at INTEGER NOT NULL);
        ''')

    def close(self):
        self.db.close()

    def provision_authority(self, operation_id, source_grant):
        """Environment-owner input, not a controller request or a native issuer.

        Current receiving authority is read here at commit, not trusted from the
        controller's own grant description. Issuer authenticity remains stipulated.
        """
        self.db.execute('INSERT INTO authority_inputs VALUES(?,?) ON CONFLICT(operation_id) DO UPDATE SET payload=excluded.payload',
                        (operation_id,canonical(source_grant)))

    def _event(self, operation_id, tick, kind, detail=None):
        detail = detail or {}
        own_transaction = not self.db.in_transaction
        if own_transaction:self.db.execute('BEGIN IMMEDIATE')
        try:
            last = self.db.execute('SELECT hash FROM events ORDER BY seq DESC LIMIT 1').fetchone()
            previous = last[0] if last else '0' * 64
            body = canonical({'operation_id':operation_id,'tick':tick,'kind':kind,'detail':detail,'previous':previous})
            digest = hashlib.sha256(body.encode('utf-8')).hexdigest()
            self.db.execute('INSERT INTO events(operation_id,tick,kind,detail,previous_hash,hash) VALUES(?,?,?,?,?,?)',
                            (operation_id,tick,kind,canonical(detail),previous,digest))
            if own_transaction:self.db.execute('COMMIT')
        except Exception:
            if own_transaction:self.db.execute('ROLLBACK')
            raise

    def file_case(self, public):
        if set(public) - PUBLIC_KEYS:
            raise ValueError('undeclared/private input keys')
        if public['native_execution']:
            raise ValueError('this runtime cannot claim native/human execution')
        self.db.execute('BEGIN IMMEDIATE')
        try:
            self.db.execute('INSERT INTO cases VALUES(?,?,?,?,?)',
                (public['operation_id'],public['tenant'],public['principal'],public['owner'],canonical(public)))
            self._event(public['operation_id'],public['arrival'],'FILED',{'filer':public['principal'],'standing_changed':False})
            self.db.execute('INSERT INTO floors VALUES(?,?) ON CONFLICT(resource) DO UPDATE SET epoch=max(epoch,excluded.epoch)',
                            (public['resource'],public['installed_floor']))
            for recipient in public['affected_recipients']:
                if not recipient['authorized'] or recipient['tenant'] != public['tenant']:
                    self._event(public['operation_id'],public['arrival'],'NOTIFICATION_DENIED_SCOPE',{'recipient':recipient['id']})
                    continue
                message={'operation_id':public['operation_id'],'resource':public['resource'],
                         'source_root':'evidence-'+public['operation_id'],
                         'evidence_version':public['evidence']['version']}
                receipt=(public['arrival']+recipient['receipt_delay'] if recipient['receipt_delay'] is not None else None)
                self.db.execute('INSERT INTO outbox VALUES(?,?,?,?,0)',
                                (public['operation_id'],recipient['id'],canonical(message),receipt))
            self.db.execute('COMMIT')
        except Exception:
            self.db.execute('ROLLBACK')
            raise

    def _busy(self, person):
        rows = self.db.execute('SELECT start,finish FROM reservations WHERE subject=?',(person['id'],)).fetchall()
        return list(person['busy']) + [list(row) for row in rows]

    def whisper(self, public):
        """Materialize bounded messages and fixture-supplied peer receipts.

        Actual network arrival, authentication and participant behavior are not
        measured. Copies retain one origin and do not create independent evidence.
        """
        charged = 0
        for recipient in public['affected_recipients']:
            charged += 2  # modeled send/receive processing; not a priced network
            self.db.execute('BEGIN IMMEDIATE')
            row=self.db.execute('SELECT payload,received_at,relayed FROM outbox WHERE operation_id=? AND recipient=?',
                                (public['operation_id'],recipient['id'])).fetchone()
            if row is None or row[2]:
                self.db.execute('COMMIT')
                continue
            message=json.loads(row[0]);received_at=row[1]
            self.db.execute('INSERT INTO notifications VALUES(?,?,?,?) ON CONFLICT DO NOTHING',
                            (public['operation_id'],recipient['id'],row[0],received_at))
            self._event(public['operation_id'],public['arrival'],'NOTIFICATION_SENT',
                        {'recipient':recipient['id'],'message':message,'work_charge':2})
            if received_at is not None:
                self._event(public['operation_id'],received_at,'PEER_RECEIPT',{'recipient':recipient['id'],'source_root':message['source_root']})
            self.db.execute('UPDATE outbox SET relayed=1 WHERE operation_id=? AND recipient=?',
                            (public['operation_id'],recipient['id']))
            self.db.execute('COMMIT')
        return charged

    def reserve(self, public, kind, earliest, duration, latest_finish):
        """Check and insert under one SQLite write transaction; capacity is shared."""
        self.db.execute('BEGIN IMMEDIATE')
        try:
            candidates = []
            for person in public['reviewers']:
                if kind == 'ack':
                    eligible = person['id'] == public['owner'] and person['may_ack']
                else:
                    eligible = person['qualified'] and person['may_review']
                if not eligible:
                    continue
                start = earliest_slot(self._busy(person),earliest,duration)
                if start + duration <= latest_finish:
                    candidates.append((start,person['id']))
            if not candidates:
                self._event(public['operation_id'],earliest,'NO_SLOT',{'kind':kind})
                self.db.execute('COMMIT')
                return None
            start, subject = min(candidates)
            finish = start + duration
            self.db.execute('INSERT INTO reservations VALUES(?,?,?,?,?)',
                            (subject,public['operation_id'],kind,start,finish))
            self._event(public['operation_id'],start,'RESERVED',{'kind':kind,'subject':subject,'finish':finish})
            self.db.execute('COMMIT')
            return {'subject':subject,'start':start,'finish':finish}
        except Exception:
            self.db.execute('ROLLBACK')
            raise

    def install_floor(self, resource, epoch):
        self.db.execute('BEGIN IMMEDIATE')
        self.db.execute('INSERT INTO floors VALUES(?,?) ON CONFLICT(resource) DO UPDATE SET epoch=max(epoch,excluded.epoch)',
                        (resource,epoch))
        self.db.execute('COMMIT')

    def actuation_reasons(self, public, tick):
        evidence = public['evidence']
        row = self.db.execute('SELECT payload FROM authority_inputs WHERE operation_id=?',
                              (public['operation_id'],)).fetchone()
        grant = json.loads(row[0]) if row else {}
        state = public['state_appraisal']
        reasons = []
        binding = self.db.execute('SELECT payload FROM cases WHERE operation_id=?',(public['operation_id'],)).fetchone()
        stored = json.loads(binding[0]) if binding else {}
        if any(stored.get(key) != public[key] for key in ('tenant','principal','deputy','resource')):
            reasons.append('CASE_BINDING_MISMATCH')
        if not public['identity_accepted']:
            reasons.append('IDENTITY_NOT_ADMITTED')
        if not (state['accepted'] and state['resource'] == public['resource']
                and state['policy_version'] == 1 and state['as_of'] <= tick < state['expires']):
            reasons.append('STATE_NOT_CURRENT_OR_APPLICABLE')
        if not (evidence['appraised'] and evidence['case'] == public['operation_id']
                and evidence['resource'] == public['resource'] and evidence['complete']
                and evidence['version'] == 1 and evidence['as_of'] <= tick < evidence['expires']):
            reasons.append('BASIS_NOT_CURRENT_OR_APPLICABLE')
        if public['human_choice'] != evidence['recommended_action']:
            reasons.append('DECISION_DISAGREES_WITH_ADMITTED_BASIS')
        expected = {'principal':public['principal'],'actor':public['deputy'],
                    'tenant':public['tenant'],'resource':public['resource'],
                    'action':public['human_choice'],'case':public['operation_id'],'purpose':'HEW-remediation'}
        if not (grant.get('verified') and grant.get('active') and grant.get('policy_version') == 1
                and grant.get('not_before',tick+1) <= tick < grant.get('expires',tick)
                and all(grant.get(key) == value for key,value in expected.items())):
            reasons.append('DELEGATION_NOT_APPLICABLE')
        semantics = public['semantic_contract']
        if not (public['semantic_binding'] and semantics['approval_kind'] == 'action_authorization'
                and semantics['operation_id'] == public['operation_id'] and semantics['version'] == 1):
            reasons.append('SEMANTIC_BINDING_UNRESOLVED')
        if not (public['token_verified'] and public['token_resource'] == public['resource']
                and public['token_actor'] == public['deputy']):
            reasons.append('FENCE_BINDING_NOT_ADMITTED')
        floor_row = self.db.execute('SELECT epoch FROM floors WHERE resource=?',(public['resource'],)).fetchone()
        if floor_row is None:
            reasons.append('FENCE_RESOURCE_UNBOUND')
        elif public['request_epoch'] < floor_row[0]:
            reasons.append('OLD_GENERATION')
        for recipient in stored.get('affected_recipients',[]):
            receipt=self.db.execute('SELECT received_at FROM notifications WHERE operation_id=? AND recipient=?',
                                    (public['operation_id'],recipient['id'])).fetchone()
            if receipt is None or receipt[0] is None or receipt[0]>tick:
                reasons.append('AFFECTED_PEER_RECEIPT_UNRESOLVED')
                break
        if not (public['continuity']['pause_permitted'] or public['continuity']['handover_established']):
            reasons.append('CONTINUITY_TRANSITION_NOT_ESTABLISHED')
        return reasons

    def apply(self, public, tick):
        """Delegation, local floor and digital effect share this model transaction.

        External source truth, distributed revocation and physical effects are
        outside this atomic boundary. No exactly-once external claim is made.
        """
        self.db.execute('BEGIN IMMEDIATE')
        try:
            reasons = self.actuation_reasons(public,tick)
            if reasons:
                self._event(public['operation_id'],tick,'ACTION_DENIED',{'reasons':reasons})
                self.db.execute('COMMIT')
                return {'applied':False,'reasons':reasons}
            fingerprint = canonical({k:public[k] for k in ('operation_id','resource','human_choice','request_epoch')})
            old = self.db.execute('SELECT fingerprint FROM effects WHERE command_id=?',(public['command_id'],)).fetchone()
            if old:
                if old[0] != fingerprint:
                    self._event(public['operation_id'],tick,'ACTION_DENIED',{'reasons':['COMMAND_ID_CONFLICT']})
                    self.db.execute('COMMIT')
                    return {'applied':False,'reasons':['COMMAND_ID_CONFLICT']}
                self._event(public['operation_id'],tick,'DUPLICATE_COMMAND_NO_NEW_EFFECT')
                self.db.execute('COMMIT')
                return {'applied':True,'duplicate':True,'reasons':[]}
            self.db.execute('UPDATE floors SET epoch=max(epoch,?) WHERE resource=?',
                            (public['request_epoch'],public['resource']))
            self.db.execute('INSERT INTO effects VALUES(?,?,?,?,?,?,?)',
                (public['command_id'],public['operation_id'],fingerprint,public['resource'],
                 public['human_choice'],public['request_epoch'],tick))
            self._event(public['operation_id'],tick,'EFFECT_APPLIED',
                        {'resource':public['resource'],'action':public['human_choice'],'epoch':public['request_epoch']})
            self.db.execute('COMMIT')
            return {'applied':True,'duplicate':False,'reasons':[]}
        except Exception:
            self.db.execute('ROLLBACK')
            raise

    def run_case(self, public):
        self.file_case(public)
        tick = public['arrival']
        work = 1  # Filing is performed, not inferred from eventual delivery.
        work += public['source_preparation_work']
        self._event(public['operation_id'],tick,'SOURCE_PREPARATION_CHARGED',{'work_charge':public['source_preparation_work']})
        work += self.whisper(public)
        ack = self.reserve(public,'ack',tick,1,public['ack_deadline'])
        if ack:
            tick = ack['finish']
            work += 1
            self._event(public['operation_id'],tick,'OWNER_ACK',{'owner':public['owner']})
        else:
            tick = public['ack_deadline'] + 1
            self._event(public['operation_id'],public['ack_deadline']+1,'OWNER_NON_RESPONSE',{'failure_of':'owner'})
        for attempt in range(public['restart_count']):
            work += 1
            self._event(public['operation_id'],tick,'RESTART_RECORDED',{'attempt':attempt+1,'new_evidence':public['new_evidence']})
        if public['capacity_observation'] != 'current':
            self._event(public['operation_id'],tick,'CAPACITY_UNKNOWN')
            return {'operation_id':public['operation_id'],'ack':ack,'review':None,'work':work,
                    'applied':False,'confirmed':False,'delivered':False,'reasons':['CAPACITY_UNKNOWN']}
        review = self.reserve(public,'review',tick,public['review_service'],public['decision_deadline'])
        if not review:
            self._event(public['operation_id'],tick,'REVIEW_UNAVAILABLE')
            return {'operation_id':public['operation_id'],'ack':ack,'review':None,'work':work,
                    'applied':False,'confirmed':False,'delivered':False,'reasons':['REVIEW_UNAVAILABLE']}
        tick = review['finish']
        work += public['review_service']
        self._event(public['operation_id'],tick,'REVIEW_COMPLETED',{'reviewer':review['subject'],'choice':public['human_choice']})
        # Each configured check has a declared work charge. Tick latency is separate.
        work += 5  # identity,state,basis,delegation,fence/continuity check bundle
        applied_at = tick + public['gate_latency'] + public['application_duration']
        if applied_at > public['application_deadline'] or work+3 > public['work_budget']:
            reasons = ['APPLICATION_TOO_LATE_OR_OVER_BUDGET']
            self._event(public['operation_id'],tick,'ACTION_DENIED',{'reasons':reasons})
            action = {'applied':False,'reasons':reasons}
        else:
            action = self.apply(public,applied_at)
            work += int(action['applied'])
        confirmed = action['applied'] and (not public['reply_lost'] or public['effect_query_available'])
        if action['applied'] and public['reply_lost']:
            self._event(public['operation_id'],applied_at,'REPLY_LOST')
        if confirmed:
            self._event(public['operation_id'],applied_at,'EFFECT_CONFIRMED',{'method':'SQLite effect query' if public['reply_lost'] else 'local digital effect receipt'})
            work += 1
        elif action['applied']:
            self._event(public['operation_id'],applied_at,'EFFECT_KNOWLEDGE_UNKNOWN')
        delivery_at = applied_at + public['delivery_duration']
        delivered = bool(ack and action['applied'] and confirmed and delivery_at<=public['delivery_deadline']
                         and work+1<=public['work_budget'])
        if delivered:
            work += 1
            self._event(public['operation_id'],delivery_at,'QUALIFIED_REENTRY_AND_DELIVERY')
        return {'operation_id':public['operation_id'],'ack':ack,'review':review,'work':work,
                'applied':action['applied'],'confirmed':confirmed,'delivered':delivered,
                'applied_at':applied_at if action['applied'] else None,
                'delivery_at':delivery_at if delivered else None,'reasons':action['reasons']}

    def events(self, operation_id=None):
        rows = self.db.execute('SELECT seq,operation_id,tick,kind,detail,previous_hash,hash FROM events '
                               + ('WHERE operation_id=? ' if operation_id else '')+'ORDER BY seq',
                               (operation_id,) if operation_id else ()).fetchall()
        return [{'seq':r[0],'operation_id':r[1],'tick':r[2],'kind':r[3],'detail':json.loads(r[4]),
                 'previous_hash':r[5],'hash':r[6]} for r in rows]

    def read_case(self, operation_id, tenant, subject):
        row = self.db.execute('SELECT tenant,principal,owner,payload FROM cases WHERE operation_id=?',(operation_id,)).fetchone()
        if row is None or row[0] != tenant or subject not in (row[1],row[2]):
            raise PermissionError('case view not authorized')
        return json.loads(row[3])

    def request_adverse_action(self, operation_id, based_only_on_filing=True):
        if based_only_on_filing:
            tick = self.db.execute('SELECT max(tick) FROM events WHERE operation_id=?',(operation_id,)).fetchone()[0]
            self._event(operation_id,tick,'ADVERSE_ACTION_DENIED',{'reason':'filing is not adverse-action grounds'})
            return False
        # No adverse-action implementation admitted by this fixture.
        raise NotImplementedError('separate evidence and authority profile required')
