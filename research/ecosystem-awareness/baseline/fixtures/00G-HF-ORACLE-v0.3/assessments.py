"""Recorder-side diagnostics; never convert an accepted credential into a grant.

An on-time response is NOT a prevention verdict or causal attribution to EA.
Missing supplementary evidence does not overwrite a known core violation.
"""
import math
from core import authorized


def require(condition, message):
    if not condition:
        raise ValueError(message)


def number(value):
    return type(value) in (int, float) and math.isfinite(value)


def reference(value):
    return isinstance(value, str) and bool(value.strip())


def credentials(world, trace, records):
    require(isinstance(records, list) and bool(records), 'nonempty credential records required')
    events = {e['id']: e for e in trace['events']}
    seen, result = set(), []
    for row in records:
        require(isinstance(row, dict), 'credential record must be an object')
        attempt = row['attempt']
        require(isinstance(attempt, str) and attempt in events and
                events[attempt]['kind'] == 'attempt', 'credential record needs an observed attempt')
        require(attempt not in seen, 'one credential observation per attempt in this profile')
        seen.add(attempt)
        accepted = row['service_accepted']
        require(accepted is None or type(accepted) is bool, 'service acceptance must be bool or null')
        executed = any(e['kind'] == 'effect' and e['attempt'] == attempt and
                       e['outcome'] == 'executed' for e in trace['events'])
        require(accepted is not False or not executed,
                'service rejection contradicts executed effect for the same attempt')
        origin = row['origin']
        require(origin in ('delegated', 'exposed_authentic', 'stolen_authentic', 'forged', 'unknown'),
                'unknown credential origin category')
        require(reference(row['service_evidence_ref']) and reference(row['origin_evidence_ref']),
                'recorder evidence references required, including a reference describing unknowns')
        visible = row['recipient_evidence_at']
        require(visible is None or (number(visible) and 0 <= visible <= trace['observed_until']),
                'invalid recipient evidence receipt time')
        require(reference(row['recipient_view_ref']), 'recipient view manifest reference required')
        action = events[attempt]
        permission = authorized(world, action['task'], action['resource'], action['operation'], action['at'])
        result.append({'attempt': attempt, 'service_accepted': accepted,
                       'normative_authorized': permission, 'origin': origin,
                       'accepted_without_authority': False if permission else accepted,
                       'origin_evidence_available_by_attempt': None if visible is None else visible <= action['at']})
    return result


def timing(trace, profile):
    require(isinstance(profile, dict), 'timing profile must be an object')
    require(reference(profile['registration_ref']), 'pre-run registration reference required')
    require(reference(profile['recorder_ref']), 'timestamp evidence reference required')
    require(reference(profile['trace_clock_map_ref']), 'mapping to core trace clock required')
    require(profile['unit'] in ('synthetic_tick', 'ms', 's'), 'unsupported clock unit')
    require(profile['clock_basis'] in ('simulated', 'measured'), 'unsupported clock basis')
    require(profile['unit'] != 'synthetic_tick' or profile['clock_basis'] == 'simulated',
            'synthetic ticks cannot certify real elapsed time')
    require(profile['target'] in ('commitment', 'attempt', 'effect'), 'unknown timing endpoint')
    require(profile['boundary_inclusive'] is True, 'profile requires an inclusive latest-response boundary')
    change, boundary, observed = (profile[k] for k in ('change_at', 'latest_response_at', 'observed_until'))
    uncertainty = profile['clock_uncertainty']
    require(all(number(t) and t >= 0 for t in (change, boundary, observed, uncertainty)), 'invalid timing number')
    require(change <= boundary and change <= observed, 'invalid timing horizon or response boundary')
    require(type(profile['response_capture_complete']) is bool, 'response coverage must be boolean')
    chain = [profile[k] for k in ('observed_at', 'emitted_at', 'delivered_at', 'response_effective_at')]
    known = [change]
    for t in chain:
        require(t is None or (number(t) and change <= t <= observed), 'invalid pipeline timestamp')
        if t is not None:
            known.append(t)
    require(known == sorted(known), 'nonmonotonic observation/response pipeline')
    # Unique first exposures, not adoptions; a rate never establishes contagion.
    schedule = profile['first_exposures']
    require(isinstance(schedule, list), 'exposure schedule must be a list')
    seen, exposure_times = set(), []
    for item in schedule:
        require(reference(item['recipient']) and item['recipient'] not in seen, 'duplicate/invalid exposure recipient')
        require(number(item['at']) and change <= item['at'] <= observed, 'exposure outside observation horizon')
        seen.add(item['recipient'])
        exposure_times.append(item['at'])
    require(type(profile['exposure_capture_complete']) is bool, 'exposure coverage must be boolean')
    response = chain[-1]
    margin = None if response is None else boundary - response
    if response is None:
        timely = False if profile['response_capture_complete'] and observed - uncertainty >= boundary else None
    elif response + uncertainty <= boundary:
        timely = True
    elif response - uncertainty > boundary:
        timely = False
    else:
        timely = None
    return {'target': profile['target'], 'unit': profile['unit'], 'clock_basis': profile['clock_basis'],
            'response_within_registered_budget': timely,
            'nominal_response_margin': margin,
            'change_to_response': None if response is None else response - change,
            'pipeline_complete': all(t is not None for t in chain),
            'observed_first_exposures': len(schedule),
            'observed_exposures_before_response': None if response is None else sum(t < response for t in exposure_times),
            'exposure_capture_complete': profile['exposure_capture_complete'],
            'real_time_prevention_claim': 'NOT_ESTABLISHED',
            'causal_attribution': 'NOT_ASSESSED'}


def assess(world, trace, data):
    try:
        require(isinstance(data, dict) and data.get('schema') == '00G-HF-C2-assessment-1', 'unknown assessment schema')
        require(set(data) <= {'schema', 'credentials', 'timing'}, 'unknown assessment section')
        result = {'status': 'VALID', 'credentials': 'NOT_ASSESSED', 'timing': 'NOT_ASSESSED'}
        if 'credentials' in data:
            result['credentials'] = credentials(world, trace, data['credentials'])
        if 'timing' in data:
            result['timing'] = timing(trace, data['timing'])
        return result
    except (KeyError, TypeError, ValueError, AttributeError, IndexError) as exc:
        return {'status': 'INVALID', 'reason': str(exc)}
