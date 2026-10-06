"""Exact analytical calendar checker. No STPA tool, SPIRE, RATS device or human is executed."""
from pathlib import Path
from fractions import Fraction
from copy import deepcopy
import hashlib, json
ROOT=Path(__file__).resolve().parent
CARD=ROOT/'run_card_v0.3_2026-10-06.json'

def overlaps(start,finish,interval):
    return start < interval[1] and interval[0] < finish

def first_slot(reviewer,arrival,service):
    candidate=arrival
    for start,end in sorted(reviewer['busy_intervals']):
        if end<=candidate:
            continue
        if candidate+service<=start:
            break
        candidate=end
    return candidate

def timing(case,reviewer,start):
    decision=start+case['service']
    application=decision+case['application_duration']
    delivery=application+case['delivery_duration']
    return {'reviewer':reviewer['id'],'start':start,
            'decision_at':decision,'application_at':application,'mission_at':delivery}

def fits_deadlines(case,record):
    return (record['decision_at']<=case['decision_deadline'] and
            record['application_at']<=case['application_deadline'] and
            record['mission_at']<=case['mission_deadline'])

def eligible(reviewer):
    return reviewer['qualified'] and reviewer['review_authority']

def closed_form(case,reviewers=None):
    pool=case['reviewers'] if reviewers is None else reviewers
    candidates=[]
    for reviewer in pool:
        if not eligible(reviewer):
            continue
        start=first_slot(reviewer,case['arrival'],case['service'])
        record=timing(case,reviewer,start)
        if record['mission_at']<=case['horizon'] and fits_deadlines(case,record):
            candidates.append(record)
    return min(candidates,key=lambda x:(x['decision_at'],x['reviewer'])) if candidates else None

def exhaustive(case,reviewers=None):
    pool=case['reviewers'] if reviewers is None else reviewers
    candidates=[]
    enumerated=0
    for reviewer in pool:
        if not eligible(reviewer):
            continue
        for start in range(case['arrival'],case['horizon']-case['service']+1):
            enumerated+=1
            finish=start+case['service']
            if any(overlaps(start,finish,busy) for busy in reviewer['busy_intervals']):
                continue
            record=timing(case,reviewer,start)
            if record['mission_at']<=case['horizon'] and fits_deadlines(case,record):
                candidates.append(record)
    best=min(candidates,key=lambda x:(x['decision_at'],x['reviewer'])) if candidates else None
    return best,enumerated

def assess(case):
    actual=closed_form(case)
    other,steps=exhaustive(case)
    assert actual==other,(case['id'],actual,other)
    observed=closed_form(case,case.get('observed_reviewers',case['reviewers']))
    ack_at=case.get('owner_ack_at')
    ack_timely=(ack_at is not None and case.get('owner_ack_authorized',False)
                and case['arrival']<=ack_at<=case['ack_deadline'])
    capacity_report=('UNKNOWN' if case['capacity_observation']!='current'
                     else 'AVAILABLE' if actual and ack_timely
                     else 'DEGRADED' if actual or ack_timely else 'UNAVAILABLE')
    gates=all(case[k] for k in ('identity_accepted','execution_authority',
                               'basis_sufficient','attestation_accepted'))
    effect=case.get('application_observed',True)
    possible=bool(actual) and gates and effect
    supported=possible and capacity_report=='AVAILABLE'
    timely_path_complete=possible and ack_timely
    result={'case_id':case['id'],'reference_calendar':actual,
            'calendar_reference_feasible':bool(actual),'observed_calendar':observed,
            'capacity_report':capacity_report,'owner_ack_at_stipulation':ack_at,
            'owner_ack_timely':ack_timely,'timely_owner_response_path_complete':timely_path_complete,
            'gates_stipulated_satisfied':gates,
            'application_observed_stipulation':effect,
            'completion_possible_under_model_stipulations':possible,
            'guarded_completion_supported_by_capacity_observation':supported,
            'named_primary_earliest':timing(case,case['reviewers'][0],
                 first_slot(case['reviewers'][0],case['arrival'],case['service'])),
            'exhaustive_start_options_checked':steps,
            'crypto_validation_executed':False,
            'nonretaliation_or_immutable_storage_implementation_tested':False}
    expected=case['expected']
    assert bool(actual)==expected['schedule'],(case['id'],result)
    for key in ('reviewer','decision_at','mission_at'):
        if key in expected:
            assert actual[key]==expected[key],(case['id'],key,actual)
    if 'admissible_completion' in expected:
        assert possible==expected['admissible_completion'],case['id']
    for key in ('owner_ack_timely','timely_owner_response_path_complete'):
        if key in expected:
            assert result[key]==expected[key],(case['id'],key,result)
    if 'capacity_claim' in expected:
        assert capacity_report==expected['capacity_claim'],case['id']
    if 'observed_schedule' in expected:
        assert bool(observed)==expected['observed_schedule'],case['id']
    if 'attestation_fresh' in expected:
        fresh=(case['attestation_appraised_at']-case['attestation_generated_at']
               <=case['attestation_max_age'])
        assert fresh==expected['attestation_fresh'],case['id']
        result['attestation_within_declared_age_bound']=fresh
        result['snapshot_false_available']=bool(observed) and not bool(actual)
    # Filing protection remains a contract stipulation, not a tested storage/reputation subsystem.
    return result

def check():
    raw=CARD.read_bytes()
    card=json.loads(raw)
    case_results=[assess(case) for case in card['cases']]
    grid_cases=0
    enumerated=0
    for arrival in range(7):
        for service in range(1,5):
            for slack in range(9):
                for busy_start in range(6):
                    for length in range(1,5):
                        case={'id':'GRID','arrival':arrival,'service':service,
                            'ack_deadline':arrival+8,'decision_deadline':arrival+slack,
                            'application_deadline':arrival+slack+1,
                            'mission_deadline':arrival+slack+2,
                            'application_duration':1,'delivery_duration':1,'horizon':24,
                            'reviewers':[{'id':'H','qualified':True,'review_authority':True,
                                 'busy_intervals':[[busy_start,busy_start+length]]}]}
                        reference=closed_form(case)
                        brute,starts=exhaustive(case)
                        assert reference==brute,(case,reference,brute)
                        grid_cases+=1
                        enumerated+=starts
    # Source-scoped observational equivalence; this is illustrative algebra, not calibration.
    blind_rows=[]
    for beta in (Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)):
        tpr=beta
        fpr=beta
        accuracy=Fraction(1,2)*beta+Fraction(1,2)*(1-beta)
        assert tpr==fpr and accuracy==Fraction(1,2)
        blind_rows.append({'available_output_probability':str(beta),
                          'true_available_rate':str(tpr),'false_available_rate':str(fpr),
                          'binary_accuracy_under_equal_prior':str(accuracy)})
    by_id={x['case_id']:x for x in case_results}
    assert by_id['HEW-DDS-02-ONE-BUSY']['named_primary_earliest']['decision_at']==13
    assert by_id['HEW-DDS-03-QUALIFIED-BACKUP']['reference_calendar']['decision_at']==5
    assert by_id['HEW-DDS-07-STALE-BUT-FRESH']['snapshot_false_available']
    assert by_id['HEW-DDS-06-UNKNOWN-CAPACITY']['capacity_report']=='UNKNOWN'
    result={'result':'BOUNDED_ANALYTICAL_CHECK_PASS','run_card_id':card['id'],
            'run_card_sha256':hashlib.sha256(raw).hexdigest(),
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'registered_cases':len(case_results),'calendar_grid_cases':grid_cases,
            'grid_integer_start_options_checked':enumerated,
            'case_results':case_results,'indistinguishable_world_algebra':blind_rows,
            'scope':'Calendar necessity/sufficiency and stipulated logical gates in the declared finite model',
            'limits':['No STPA tool or native SPIRE/RATS implementation executed',
                      'No actual crypto, device, attestation or human validation',
                      'No empirical risk/latency/prices calibrated',
                      'No all-domain proof, superiority, conformance or official C02 admission',
                      'Protected storage and no-retaliation remain design obligations'],
            'native_technologies_executed':False,'new_human_campaigns':0}
    (ROOT/'analytical_fixture_results_v0.3_2026-10-06.json').write_text(
        json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'result':result['result'],'registered_cases':len(case_results),
                     'calendar_grid_cases':grid_cases,'integer_start_options':enumerated,
                     'ack_and_review_separated':True,'one_busy_primary_decision_at':13,'backup_decision_at':5,
                     'stale_but_fresh_false_available':True,
                     'native_technologies_executed':False},indent=2))
if __name__=='__main__':
    check()
