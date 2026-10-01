"""Bounded view qualification; no world, oracle, network, tools or model imports."""
from copy import deepcopy

PROFILE = 'EA_QUALIFICATION_VIEW_v1'
SCOPE = {'id', 'recipient', 'task', 'resource', 'operation', 'claim', 'basis_version'}
SOURCES = {'mandate': 'principal-service', 'access': 'asset-service',
           'applicability': 'applicability-service'}
LINEAGE_SOURCE = 'lineage-service'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def string(value):
    return isinstance(value, str) and bool(value)


def scope_ok(value):
    return isinstance(value, dict) and set(value) == SCOPE and all(string(x) for x in value.values())


def validate(view):
    require(isinstance(view, dict) and set(view) == {'decision','now','timing','checks','reports'}, 'view keys')
    require(scope_ok(view['decision']), 'decision scope')
    require(type(view['now']) is int and view['now'] >= 0, 'now')
    timing = view['timing']
    require(isinstance(timing, dict) and set(timing) == {'transport_ticks','response_ticks','last_useful_at'}, 'timing keys')
    require(all(type(v) is int and v >= 0 for v in timing.values()), 'timing values')
    for name in ('checks', 'reports'):
        require(isinstance(view[name], list) and len(view[name]) <= 64, name + ' bound')
        for r in view[name]:
            require(isinstance(r, dict), 'record shape')
            if name == 'reports':
                require(string(r.get('id')) and r.get('kind') in ('report','instruction'), 'report identity/type')
                if r['kind'] == 'instruction':
                    continue
                require(string(r.get('claim')) and type(r.get('qualified')) is bool, 'report qualification')
                require(string(r.get('lineage_source')), 'lineage source')
                require(isinstance(r.get('roots'), list) and len(r['roots']) <= 16 and all(string(x) for x in r['roots']), 'root labels')
                require(type(r.get('value')) is bool, 'report value')
            else:
                require(string(r.get('name')) and r['name'] in SOURCES and string(r.get('source')) and string(r.get('version')), 'check identity')
                require('value' in r and (r['value'] is None or type(r['value']) is bool), 'check value')
            require(scope_ok(r.get('decision')), 'record scope')
            require(type(r.get('observed_at')) is int and r['observed_at'] >= 0, 'record observation time')
            require(type(r.get('valid_until')) is int and r['valid_until'] > r['observed_at'], 'record validity interval')
    ids = [r['id'] for r in view['reports']]
    require(len(ids) == len(set(ids)), 'duplicate report id')


def out_of_scope_or_time(record, view):
    if record['decision'] != view['decision']:
        return 'other_decision_scope'
    if record['observed_at'] > view['now']:
        return 'not_yet_observed'
    if record['valid_until'] <= view['now']:
        return 'expired'
    return None


def assess(view):
    """Return a qualified signal from the delivered view, never from hidden facts."""
    validate(view)
    rejected, expiries, checks = [], [], {}
    for name, source in SOURCES.items():
        accepted = []
        for index, r in enumerate(view['checks']):
            if r['name'] != name:
                continue
            reason = out_of_scope_or_time(r, view)
            if r['source'] != source:
                reason = 'unaccepted_source_binding'
            if reason:
                rejected.append({'record': 'check:' + str(index), 'reason': reason})
            else:
                accepted.append(r)
                expiries.append(r['valid_until'])
        values = {r['value'] for r in accepted if r['value'] is not None}
        has_unknown = any(r['value'] is None for r in accepted)
        if values == {True, False}:
            status = 'CONFLICT'
        elif False in values:
            status = 'CONTRADICTED'
        elif values == {True} and not has_unknown:
            status = 'SUPPORTED'
        else:
            status = 'UNKNOWN'
        checks[name] = {'status': status, 'accepted_source': source,
                        'versions': sorted({r['version'] for r in accepted}),
                        'records': deepcopy(accepted)}
    roots, evidence_ids, negative_ids = set(), [], []
    for r in view['reports']:
        if r['kind'] == 'instruction':
            rejected.append({'record': r['id'], 'reason': 'instruction_not_evidence_or_grant'})
            continue
        reason = out_of_scope_or_time(r, view)
        if r['claim'] != view['decision']['claim']:
            reason = 'other_claim'
        elif not r['qualified'] or r['lineage_source'] != LINEAGE_SOURCE or not r['roots']:
            reason = 'unqualified_lineage'
        if reason:
            rejected.append({'record': r['id'], 'reason': reason})
            continue
        expiries.append(r['valid_until'])
        evidence_ids.append(r['id'])
        if r['value']:
            roots.update(r['roots'])
        else:
            negative_ids.append(r['id'])
    evidence_status = 'CONTRADICTED' if negative_ids else 'SUPPORTED' if len(roots) >= 2 else 'UNKNOWN'
    dimensions = {k:v['status'] for k,v in checks.items()}
    dimensions['evidence'] = evidence_status
    contradicted = sorted(k for k,v in dimensions.items() if v in ('CONTRADICTED','CONFLICT'))
    missing = sorted(k for k,v in dimensions.items() if v == 'UNKNOWN')
    sufficiency = 'CONTRADICTED' if contradicted else 'UNKNOWN' if missing else 'SUFFICIENT_WITHIN_VIEW'
    posture = {'CONTRADICTED':'REQUALIFY','UNKNOWN':'PRESERVE_UNKNOWN','SUFFICIENT_WITHIN_VIEW':'QUALIFIED_WITHIN_SCOPE'}[sufficiency]
    timing = view['timing']
    received = view['now'] + timing['transport_ticks']
    qualified_until = min(expiries) if expiries else None
    boundary = min(timing['last_useful_at'], qualified_until) if qualified_until is not None else timing['last_useful_at']
    margin = boundary - received - timing['response_ticks']
    return {
        'profile': PROFILE, 'decision': deepcopy(view['decision']),
        'basis_sufficiency': sufficiency, 'posture': posture,
        'checks': checks,
        'evidence': {'status':evidence_status, 'qualified_positive_roots':sorted(roots),
                     'admitted_ids':sorted(evidence_ids), 'negative_ids':sorted(negative_ids),
                     'independence_claim':'DECLARED_LINEAGE_ONLY_NOT_STATISTICAL'},
        'unqualified_records':rejected, 'missing':missing, 'contradicted':contradicted,
        'directed_checks':[{'dimension':k, 'owner':SOURCES.get(k, LINEAGE_SOURCE),
                            'request':'requalify_for_this_decision_before_use'} for k in sorted(set(missing+contradicted))],
        'emitted_at':view['now'], 'received_at':received,
        'last_useful_at':timing['last_useful_at'], 'qualified_until':qualified_until,
        'response_margin_ticks':margin, 'timely':margin > 0,
        'authority_effect':'NONE', 'temporal_change_assessed':False,
        'residual':['Bounded to the supplied decision view and declared service bindings.',
                    'Unseen changes or compromised provenance can invalidate apparently current statements.',
                    'Root labels do not establish statistical independence or population representativeness.'],
    }
