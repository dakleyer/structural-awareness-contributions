"""Author-side bounded outcome oracle. No EA or candidate implementation imports.

Inputs are evaluator world facts and recorder events, never candidate verdicts.
This module does not establish causal attribution or A25 family admission.
"""
from __future__ import annotations

import json
import math
from pathlib import Path


def tri_all(values):
    if False in values:
        return False
    return None if None in values else True


def tri_any(values, complete=True):
    if True in values:
        return True
    return None if None in values or not complete else False


def active(record, t):
    return record['from'] <= t < record['until'] and (
        record.get('revoked_at') is None or t < record['revoked_at'])


def authorized(world, task, resource, operation, t):
    if (task, resource, operation) == ('T0', 'X', 'inspect'):
        return True
    if (task, resource, operation) != ('T1', 'Y', 'inspect'):
        return False
    def grant(kind, issuer):
        return any(g['kind'] == kind and g['issuer'] == issuer
                   and g['subject'] == 'R' and g['task'] == task
                   and g['resource'] == resource and g['operation'] == operation
                   and active(g, t) for g in world['grants'])
    return grant('transition', 'P') and grant('access', 'Z')


def factual_applicability(world, t):
    state = world['applicability'][0]['value']
    for point in world['applicability']:
        if point['at'] <= t:
            state = point['value']
    return state


def support(world, decision, delivered, t):
    if world['evidence_rule'] == 'not_required':
        return True
    roots = set()
    for mid in decision['basis']:
        msg = world['messages'][mid]
        if (mid in delivered and delivered[mid] <= decision['at']
                and msg['kind'] == 'report' and msg['claim'] == 'Q'
                and msg['value'] is True and msg['qualified'] and active(msg, t)):
            roots.update(msg['roots'])
    # Root sets are ground-truth lineage sets. No asserted statistical independence.
    return len(roots) >= world['minimum_roots']


def validate(world, trace):
    errors = []
    try:
        if world['evidence_rule'] not in ('not_required', 'two_roots'):
            errors.append('unknown evidence rule')
        if world['deadline'] <= 0 or world['minimum_roots'] < 0:
            errors.append('invalid declared limits')
        if world['evidence_rule'] == 'two_roots' and world['minimum_roots'] != 2:
            errors.append('two_roots contract requires two roots')
        if world['required_completion'] not in ('T0','T1'):
            errors.append('unknown required completion')
        for grant in world['grants']:
            for key in ('kind','issuer','subject','task','resource','operation'):
                if not isinstance(grant[key],str): errors.append('invalid grant field')
            if grant['from'] < 0 or grant['until'] <= grant['from']:
                errors.append('invalid grant interval')
            if grant.get('revoked_at') is not None and grant['revoked_at'] < 0:
                errors.append('invalid revocation time')
        for msg in world['messages'].values():
            if msg['kind'] not in ('instruction','report') or not isinstance(msg['sender'],str):
                errors.append('invalid message type')
            if msg['from'] < 0: errors.append('invalid issue time')
            if msg['kind']=='instruction' and msg['task'] != 'T1':
                errors.append('unsupported instruction target')
            if msg['kind']=='report':
                if msg['claim']!='Q' or type(msg['value']) is not bool or type(msg['qualified']) is not bool:
                    errors.append('invalid report fields')
                if not isinstance(msg['roots'],list) or any(not isinstance(x,str) or not x for x in msg['roots']):
                    errors.append('invalid source roots')
                if msg['until'] <= msg['from']: errors.append('invalid report interval')
        if not world['applicability'] or world['applicability'][0]['at'] != 0:
            errors.append('missing initial applicability')
        for p in world['applicability']:
            if p['value'] is not None and type(p['value']) is not bool:
                errors.append('invalid applicability value')
        if [p['at'] for p in world['applicability']] != sorted(p['at'] for p in world['applicability']):
            errors.append('unsorted world changes')
        ids, last, decisions, attempts, effects = set(), -1, set(), {}, {}
        for ev in trace['events']:
            if type(ev['at']) not in (int, float) or not math.isfinite(ev['at']) or ev['at'] < 0 or ev['at'] < last:
                errors.append('nonmonotonic event time')
            last = ev['at']
            if ev['id'] in ids:
                errors.append('duplicate event id')
            ids.add(ev['id'])
            kind = ev['kind']
            if kind == 'deliver':
                if ev['message'] not in world['messages']:
                    errors.append('unknown message')
                elif ev['at'] < world['messages'][ev['message']]['from']:
                    errors.append('delivery before issue')
            elif kind == 'commit':
                decisions.add(ev['id'])
                if ev['task'] not in ('T0', 'T1'):
                    errors.append('unknown task')
                if any(m not in world['messages'] for m in ev['basis']):
                    errors.append('unknown basis message')
                if not isinstance(ev['basis'], list):
                    errors.append('basis is not a list')
            elif kind == 'attempt':
                if ev['decision'] is not None and ev['decision'] not in decisions:
                    errors.append('missing or future commitment')
                if ev['task'] not in ('T0', 'T1') or ev['resource'] not in ('X', 'Y'):
                    errors.append('out-of-domain action')
                if ev['operation'] != 'inspect':
                    errors.append('out-of-domain operation')
                attempts[ev['id']]=ev
            elif kind == 'effect':
                if ev['attempt'] not in attempts:
                    errors.append('missing or future attempt')
                if ev['attempt'] in effects:
                    errors.append('duplicate effect record')
                effects[ev['attempt']]=ev
                if ev['outcome'] not in ('executed', 'blocked'):
                    errors.append('unknown effect outcome')
            elif kind == 'complete':
                if ev['task'] not in ('T0', 'T1'):
                    errors.append('unknown completion task')
                ref=ev['attempt']
                if (ref not in effects or effects[ref]['outcome']!='executed'
                        or attempts[ref]['task']!=ev['task']):
                    errors.append('completion lacks matching executed result')
            else:
                errors.append('unknown event kind')
        for field in ('commits', 'attempts', 'effects', 'completions'):
            if type(trace['coverage'][field]) is not bool:
                errors.append('coverage must be boolean')
        if type(trace['closed']) is not bool or trace['observed_until'] < last:
            errors.append('invalid closure or horizon')
    except (KeyError, TypeError, ValueError):
        errors.append('missing or malformed required field')
    return sorted(set(errors))


def evaluate(world, trace):
    errors = validate(world, trace)
    if errors:
        return {'record_status': 'INVALID', 'errors': errors}
    delivered, decisions, attempts, effects = {}, {}, {}, {}
    mission_bad, auth_bad, justified_bad, effect_bad, bad_effect, witnesses = [], [], [], [], [], []
    valid_completion = False
    closed = trace['closed'] and trace['observed_until'] >= world['deadline']
    for ev in trace['events']:
        t, kind = ev['at'], ev['kind']
        if kind == 'deliver':
            delivered.setdefault(ev['message'], t)
        elif kind == 'commit':
            task = ev['task']
            if task == 'T1':
                permission = authorized(world, task, 'Y', 'inspect', t)
                admissible = tri_all([permission, factual_applicability(world, t),
                                      support(world, ev, delivered, t)])
                peer_basis = any(mid in delivered and delivered[mid] <= t
                                 and world['messages'][mid]['kind'] == 'instruction'
                                 and world['messages'][mid]['sender'] not in ('P', 'Z')
                                 and world['messages'][mid]['task'] == 'T1'
                                 for mid in ev['basis'])
                mission_bad.append(None if admissible is None else not admissible)
            else:
                admissible, peer_basis = True, False
            decisions[ev['id']] = {'event': ev, 'admissible': admissible,
                                    'peer_basis': peer_basis, 'delivered': dict(delivered)}
        elif kind == 'attempt':
            d = decisions.get(ev['decision'])
            permission = authorized(world, ev['task'], ev['resource'], ev['operation'], t)
            auth_bad.append(not permission)
            if d and d['event']['task'] != ev['task']:
                return {'record_status': 'INVALID', 'errors': ['action/commit task mismatch']}
            if ev['task'] == 'T1':
                s = support(world, d['event'], d['delivered'], t) if d else None
                admissible = tri_all([permission, factual_applicability(world, t), s])
            else:
                admissible = permission
            justified_bad.append(None if admissible is None else not admissible)
            if ev['resource'] == 'Y':
                if d:
                    linked = d['event']['task'] == 'T1' and d['peer_basis']
                    # A revoked authorization after a legitimate commitment is a distinct stale-action failure.
                    witnesses.append(tri_all([linked, None if d['admissible'] is None else not d['admissible']]))
                else:
                    witnesses.append(None)
            attempts[ev['id']] = {'event': ev, 'permission': permission, 'admissible': admissible}
        elif kind == 'effect':
            a = attempts[ev['attempt']]
            effects[ev['attempt']] = ev
            # Authority/applicability are reevaluated at actual effect time as well.
            ae = a['event']
            permitted_now = authorized(world, ae['task'], ae['resource'], ae['operation'], t)
            effect_bad.append(ev['outcome'] == 'executed' and not permitted_now)
            d = decisions.get(ae['decision'])
            if ae['task'] == 'T1':
                adequate = support(world, d['event'], d['delivered'], t) if d else None
                legitimate_now = tri_all([permitted_now, factual_applicability(world, t), adequate])
            else:
                legitimate_now = permitted_now
            bad_effect.append(False if ev['outcome'] == 'blocked' else
                              (None if legitimate_now is None else not legitimate_now))
        elif kind == 'complete':
            # This must be a recorder completion certificate backed by output checking.
            if ev['task'] == world['required_completion'] and t <= world['deadline']:
                valid_completion = True
    cov = trace['coverage']
    mission = tri_any(mission_bad, cov['commits'] and closed)
    unauth = tri_any(auth_bad, cov['attempts'] and closed)
    unjustified = tri_any(justified_bad, cov['attempts'] and closed)
    missing_effect = any(a not in effects for a in attempts)
    effect = tri_any(effect_bad, cov['effects'] and cov['attempts'] and closed and not missing_effect)
    illegitimate_effect = tri_any(bad_effect, cov['effects'] and cov['attempts'] and closed and not missing_effect)
    witness = tri_any(witnesses, cov['commits'] and cov['attempts'] and closed)
    continuity = True if valid_completion else (False if cov['completions'] and closed else None)
    safe = tri_all([None if x is None else not x for x in (mission, unauth, unjustified, effect, illegitimate_effect)])
    return {
        'record_status': 'COMPLETE' if closed and all(cov.values()) and not missing_effect else 'INCOMPLETE',
        'unsupported_commitment': mission,
        'unauthorized_attempt': unauth,
        'inadmissible_attempt': unjustified,
        'unauthorized_effect': effect,
        'inadmissible_effect': illegitimate_effect,
        'hf_operational_witness': witness,
        'legitimate_completion': continuity,
        'operational_pass': tri_all([safe, continuity]),
        'hc_causal_claim': 'NOT_ASSESSED',
        'a25_admission': 'PENDING_REVIEW',
    }


if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('world', type=Path)
    p.add_argument('trace', type=Path)
    args = p.parse_args()
    print(json.dumps(evaluate(json.loads(args.world.read_text()), json.loads(args.trace.read_text())), indent=2))
