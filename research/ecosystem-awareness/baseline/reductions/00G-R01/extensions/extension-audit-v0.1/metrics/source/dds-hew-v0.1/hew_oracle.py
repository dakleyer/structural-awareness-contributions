"""Post-run private-world adjudication; not imported by the controller.

The audit reconstructs facts from the registered private world and stored effects.
Calendar reference enumerates integer starts instead of using the controller's
first-slot construction. Same author; this is not independent external review.
"""
import hashlib
import itertools
import json
import sqlite3


def exhaustive_slot(people, busy_by_person, earliest, service, deadline, kind, owner):
    choices = []
    for person in people:
        eligible = person['id'] == owner and person['may_ack'] if kind == 'ack' else person['qualified'] and person['may_review']
        if not eligible:
            continue
        for start in range(earliest,deadline-service+1):
            if not any(start<end and begin<start+service for begin,end in busy_by_person[person['id']]):
                choices.append((start,person['id']))
    return min(choices) if choices else None


def judge(database, public, private, result):
    db = sqlite3.connect(str(database))
    effects = db.execute('SELECT action,epoch,applied_at FROM effects WHERE operation_id=?',
                         (public['operation_id'],)).fetchall()
    actual_violation = any(action != private['correct_action'] or not private['effect_authorized'] for action,_,_ in effects)
    continuity_kept = not effects or private['continuity_supported']
    actual_sufficient_effect = bool(effects) and not actual_violation and private['basis_truth']
    rows = db.execute('SELECT kind,tick,detail FROM events WHERE operation_id=? ORDER BY seq',
                      (public['operation_id'],)).fetchall()
    ack_timely = any(kind=='OWNER_ACK' and tick<=public['ack_deadline'] for kind,tick,_ in rows)
    review_timely = any(kind=='REVIEW_COMPLETED' and tick<=public['decision_deadline'] for kind,tick,_ in rows)
    confirmation = any(kind=='EFFECT_CONFIRMED' for kind,_,_ in rows)
    delivery_timely = any(kind=='QUALIFIED_REENTRY_AND_DELIVERY' and tick<=public['delivery_deadline'] for kind,tick,_ in rows)
    applied_timely = bool(effects) and all(tick<=public['application_deadline'] for _,_,tick in effects)
    work = 1 + public['source_preparation_work'] + 2*len(public['affected_recipients'])
    work += sum(1 for kind,_,_ in rows if kind in ('OWNER_ACK','RESTART_RECORDED','EFFECT_APPLIED','EFFECT_CONFIRMED','QUALIFIED_REENTRY_AND_DELIVERY'))
    if any(kind=='REVIEW_COMPLETED' for kind,_,_ in rows):work += public['review_service']+5
    sufficient_delivery = bool(actual_sufficient_effect and continuity_kept and ack_timely and review_timely
                              and confirmation and delivery_timely and applied_timely and work<=public['work_budget'])
    case_preserved = db.execute('SELECT count(*) FROM cases WHERE operation_id=?',(public['operation_id'],)).fetchone()[0]==1
    db.close()
    return {'actual_effect_count':len(effects),'violation_observed':actual_violation,
            'sufficient_delivery':sufficient_delivery,'continuity_preserved':continuity_kept,
            'owner_ack_timely':ack_timely,'case_preserved':case_preserved,
            'effect_knowledge':'CONFIRMED' if confirmation else 'UNKNOWN' if effects else 'NOT_APPLIED',
            'outcome':'FAIL_VIOLATION' if actual_violation else 'DELIVERED' if sufficient_delivery else 'UNRESOLVED_OR_NOT_DELIVERED',
            'work_units':work,'controller_work_claim':result['work'],'population_risk_rate':None,'human_accuracy_rate':None,
            'events':[row[0] for row in rows]}


def verify_event_chain(events):
    previous = '0'*64
    for event in events:
        assert event['previous_hash']==previous
        body=json.dumps({'operation_id':event['operation_id'],'tick':event['tick'],'kind':event['kind'],
                         'detail':event['detail'],'previous':previous},sort_keys=True,separators=(',',':'),ensure_ascii=False)
        assert hashlib.sha256(body.encode('utf-8')).hexdigest()==event['hash']
        previous=event['hash']
    return previous


def audit_reservations(database):
    db=sqlite3.connect(str(database))
    rows=db.execute('SELECT subject,operation_id,kind,start,finish FROM reservations ORDER BY subject,start').fetchall()
    for left,right in itertools.combinations(rows,2):
        assert left[0]!=right[0] or not(left[3]<right[4] and right[3]<left[4]),(left,right)
    db.close()
    return len(rows)
