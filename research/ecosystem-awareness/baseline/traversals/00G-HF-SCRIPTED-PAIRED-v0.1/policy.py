"""Fixed author policies. Inputs are public views and delivered signals only."""


def conventional(public, now):
    initial, responses = public['initial'], public['responses']
    task = initial['required_deliverable']
    if now + 4 >= initial['deadline']:
        return {'disposition':'stop','task':task,'basis':[], 'reason':'insufficient_completion_margin'}
    if task == 'T0':
        return {'disposition':'proceed','task':'T0','basis':[],
                'reason':'complete_public_original_obligation_subject_to_native_guards'}
    authority = responses['authority']
    applicability = responses['applicability']
    roots, basis = set(), []
    for r in responses['reports']['reports']:
        if (r.get('kind') == 'report' and r.get('claim') == 'Q'
                and r.get('value') is True and r.get('qualified') is True
                and r.get('revoked') is False and r['from'] <= now < r['until']):
            roots.update(r['roots'])
            basis.append(r['id'])
    eligible = (authority.get('transition') is True and authority.get('access') is True
                and applicability.get('value') is True and len(roots) >= 2)
    return {'disposition':'proceed' if eligible else 'wait','task':'T1','basis':basis,
            'reason':'provisional_current_facts_subject_to_native_guards' if eligible
                     else 'reenter_after_missing_or_negative_native_support'}


def decide(public, now, signal=None):
    proposal = conventional(public, now)
    result = {**proposal, 'conventional_proposal':dict(proposal), 'EA_consumed':signal is not None,
              'EA_changed_disposition':False, 'EA_classification':None}
    if signal is None:
        return result
    result['EA_classification'] = signal['classification']
    if proposal['task'] == 'T1':
        if not signal['current']['timely']:
            result.update(disposition='stop', reason='EA_signal_has_no_positive_response_margin')
        elif (signal['current']['basis_sufficiency'] == 'CONTRADICTED'
              or any(r['value'] is False for r in signal['current_point_observations'])):
            # A stop imposed by the common resource rule is never reopened by EA.
            if proposal['disposition'] != 'stop':
                result.update(disposition='wait', reason='EA_requires_requalification')
        elif signal['current']['basis_sufficiency'] == 'UNKNOWN':
            result['reason'] += ';EA_unknown_retained_native_guard_required'
    result['EA_changed_disposition'] = result['disposition'] != proposal['disposition']
    return result
