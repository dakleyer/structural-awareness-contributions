"""Pure projection of host-delivered native v0.1 public responses; no service calls."""
from copy import deepcopy
from temporal import core, validate


def adapt_native(initial, exchanges, decision, now, timing):
    core.require(core.scope_ok(decision), 'decision scope')
    fixed = {'recipient':'R','task':'T1','resource':'Y','operation':'inspect','claim':'Q'}
    core.require(all(decision[k] == v for k,v in fixed.items()), 'unsupported native decision binding')
    core.require(type(now) is int and now >= 0, 'now')
    core.require(isinstance(initial, dict) and initial.get('recipient') == 'R'
                 and initial.get('task_resources') == {'T0':'X','T1':'Y'}, 'native public scope binding')
    core.require(type(initial.get('now')) is int and 0 <= initial['now'] <= now, 'initial time')
    core.require(isinstance(exchanges, list) and len(exchanges) <= 64, 'exchange bound')
    latest, gaps = {}, []
    end = initial['now']
    for exchange in exchanges:
        core.require(isinstance(exchange, dict) and set(exchange) == {'action','requested_at','response_at','result'}, 'exchange shape')
        action, result = exchange['action'], exchange['result']
        core.require(core.string(action) and action in ('authority','applicability','reports'), 'service action')
        start, finish = exchange['requested_at'], exchange['response_at']
        core.require(type(start) is int and type(finish) is int and end <= start < finish <= now, 'ordered native exchange times')
        end = finish
        core.require(isinstance(result, dict), 'service result')
        if 'error' in result:
            gaps.append({'service':action, 'reason':'service_error', 'observed_at':finish})
            continue
        core.require(type(result.get('observed_at')) is int and result['observed_at'] == finish, 'native service observation time')
        # Validate each successful response before superseding it. A later good
        # response must not silently sanitize a malformed acquisition history.
        if action == 'authority':
            core.require(result.get('task') == 'T1' and result.get('resource') == 'Y', 'authority response scope')
            core.require(type(result.get('transition')) is bool and type(result.get('access')) is bool, 'native authority boolean')
        elif action == 'applicability':
            core.require(result.get('claim') == 'Q' and type(result.get('value')) is bool, 'native applicability scope/value')
        else:
            core.require(isinstance(result.get('reports'), list) and len(result['reports']) <= 64, 'native reports response')
        latest[action] = result
    observations = []
    for name, action, field in [('mandate','authority','transition'),('access','authority','access'),
                                 ('applicability','applicability','value')]:
        result = latest.get(action)
        if result is None:
            gaps.append({'dimension':name,'reason':'missing_service_response'})
            continue
        core.require(type(result.get(field)) is bool, 'native boolean')
        if action == 'authority':
            core.require(result.get('task') == 'T1' and result.get('resource') == 'Y', 'authority response scope')
        else:
            core.require(result.get('claim') == 'Q', 'applicability response scope')
        observations.append({'name':name,'source':core.SOURCES[name], 'decision':deepcopy(decision),
                             'observed_at':result['observed_at'], 'value':result[field],
                             'version':None,'valid_until':None})
        gaps.append({'dimension':name,'reason':'source_version_and_forward_validity_not_supplied'})
    reports = latest.get('reports', {}).get('reports', initial.get('reports'))
    core.require(isinstance(reports, list) and len(reports) <= 64, 'native reports bound')
    mapped, seen = [], set()
    observed = latest.get('reports', {}).get('observed_at', initial['now'])
    for report in reports:
        core.require(isinstance(report, dict) and core.string(report.get('id')), 'native report identity')
        rid = report['id']
        core.require(rid not in seen, 'duplicate native report id')
        seen.add(rid)
        reason = None
        if report.get('kind') != 'report':
            reason = 'instruction_not_evidence_or_grant'
        elif report.get('revoked') is not False:
            reason = 'revoked_or_missing_revocation_status'
        elif report.get('claim') != decision['claim']:
            reason = 'other_claim'
        elif (type(report.get('from')) is not int or type(report.get('until')) is not int
              or not 0 <= report['from'] <= observed < report['until']):
            reason = 'missing_or_noncurrent_native_interval'
        elif (type(report.get('qualified')) is not bool or type(report.get('value')) is not bool
              or not isinstance(report.get('roots'),list) or len(report['roots']) > 16
              or not all(core.string(r) for r in report['roots'])):
            reason = 'malformed_lineage_or_value'
        if reason:
            gaps.append({'record':rid,'reason':reason})
            continue
        mapped.append({'id':rid,'kind':'report','decision':deepcopy(decision),'claim':report['claim'],
                       'value':report['value'],'qualified':report['qualified'],
                       'lineage_source':core.LINEAGE_SOURCE,'roots':deepcopy(report['roots']),
                       'observed_at':observed,'valid_until':report['until']})
    snapshot = {'view':{'decision':deepcopy(decision),'now':now,'timing':deepcopy(timing),
                        'checks':[],'reports':mapped},'point_observations':observations}
    validate(snapshot)
    return {'snapshot':snapshot,'gaps':gaps,'raw_reports':deepcopy(reports),
            'authority_effect':'NONE', 'service_calls_in_projection':len(exchanges),
            'service_elapsed_ticks_in_projection':sum(e['response_at']-e['requested_at'] for e in exchanges),
            'adapter_runtime_calls':0,
            'residual':['T1/Q report scope and lineage are explicit native-fixture host bindings.',
                        'No point observation is promoted to an interval-qualified check.',
                        'Native request/effect guards remain authoritative; UNKNOWN is not their failure.']}
