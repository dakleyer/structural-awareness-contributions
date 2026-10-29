"""Independent native-source concordance, no rewrite of ACC physical/economic engines.

Cross-checks fixtures against actual source calculators, not copied reference
numbers. Distinguishes source-native equivalence, newly stipulated variants,
and examples without a source-native executable implementation.
"""
from __future__ import annotations
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
import argparse
import json
from pathlib import Path
import sys

from engine import run_manifest

HERE=Path(__file__).resolve().parent
STUDIES=HERE.parent

def _load(name: str, path: Path):
    spec=spec_from_file_location(name,path)
    if spec is None or spec.loader is None:
        raise RuntimeError('missing original source: '+str(path))
    mod=module_from_spec(spec)
    sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod


def run() -> dict:
    f1=STUDIES/'conscientia-campaign-v0.1/campaign.py'
    f2=STUDIES/'bounded-traps-v0.1/bounded_traps.py'
    campaign=_load('_acc_source_conscientia_replay',f1)
    traps=_load('_acc_source_bounded_traps_replay',f2)
    original=campaign.source_anchored_microexperiments()
    bounded=traps.example_report()
    fixture=json.loads((HERE/'cases.json').read_text(encoding='utf-8'))
    current=run_manifest(fixture)
    scenarios={c['case_id']:c for c in fixture['cases']}
    runs={c['case_id']:c for c in current['cases']}
    results={}

    # Fidelity of the exact author's fruit counts, not just the label S0/S1/S2.
    for name,entry in original['BANANA_THREE_STATES']['states'].items():
        ours=scenarios['EX-BAN-04']['states'][name]['facts']
        assert (ours['produced'],ours['holder'],ours['child'],ours['waste']) == (
            entry['bananas_produced'],entry['consumed_by_holder'],entry['received_by_child'],entry['wasted'])
    assert runs['EX-BAN-04']['welfare']['S1']=={'B':5,'F':7,'W':-2,
                                               'status':'STIPULATED_TOY_NOT_HUMAN_MEASUREMENT'}
    results['EX-BAN-04']='SOURCE_NATIVE_MICROCASE_MATCH_WITH_AUTHOR_TOY_WELFARE'

    donation=original['BANANA_DONATION_AND_CARITAS']
    assert donation['actual_authorized_donation_without_donor_consent'] is False
    assert donation['charity_public_credit_assumed_misappropriated'] is False
    assert runs['EX-BAN-03']['transitions']['proposed_donation_declined']['admissible']=='FAIL'
    results['EX-BAN-03']='SOURCE_NATIVE_NEGATIVE_GATE_MATCH; ALTERNATE_ACCEPTANCE_IS_NEW_TOY'

    raw=original['CREDIT_RELATIVE_FLOORS']
    assert raw['total']==10 and raw['seven_plus_four']=={'required':[7,4],'feasible':False}
    assert raw['seven_plus_three']=={'required':[7,3],'feasible':True}
    assert runs['EX-CREDIT-01']['state_validity']['shares_7_4']['status']=='FAIL'
    results['EX-CREDIT-01']='SOURCE_NATIVE_NUMERIC_AND_PHYSICAL_GATE_MATCH'

    apples=bounded['nonmonotone_apples']
    source_curve=original['NONMONOTONE_APPLES']['utilities']
    ours=[scenarios['EX-APPLE-01']['states'][f'q{i}']['payoffs']['buyer'] for i in range(9)]
    assert apples['values']==source_curve==ours
    assert apples['best_global_quantity']==original['NONMONOTONE_APPLES']['best_global_quantity']==8
    assert apples['local_non_loss_reachable']==[3] and original['NONMONOTONE_APPLES']['local_step_decreases_utility']
    assert runs['EX-APPLE-01']['reachability']['unilateral_only']['reachable_states']==['q3']
    # The original DOES NOT provide a jump. Our joint jump is a *labelled new
    # hypothetical positive control*. Never claim it was source-authorized.
    assert apples['direct_jump_assumed_available'] is False
    assert 'q8' in runs['EX-APPLE-01']['reachability']['joint_allowed']['reachable_states']
    results['EX-APPLE-01']='ORIGINAL_NONMONOTONE_AND_LOCAL_PATH_MATCH; JOINT_JUMP_IS_NEW_POSITIVE_CONTROL'

    linear=bounded['joint_trap']
    assert linear['feasible']==[[0,0],[1,1]] and linear['pareto_dominates']
    assert linear['reachable_without_joint_transition'] is False
    assert linear['reachable_with_joint_transition'] is True
    assert runs['EX-LINEAR-01']['reachability']['unilateral_only']['reachable_states']==['00']
    assert runs['EX-LINEAR-01']['reachability']['joint_allowed']['reachable_states']==['00','11']
    results['EX-LINEAR-01']='SOURCE_NATIVE_FEASIBILITY_AND_REACHABILITY_MATCH'

    ministry=original['TWO_MINISTRIES_700_APPLICATIONS']
    assert ministry['illustrative_start_applications']==scenarios['EX-MIN-01']['states']['fragmented']['metrics']['E_apps']==700
    assert ministry['illustrative_candidate_applications']==scenarios['EX-MIN-01']['states']['unified']['metrics']['E_apps']==2
    assert ministry['same_service_and_rights_evidence']=='NOT_ESTABLISHED'
    assert runs['EX-MIN-01']['transitions']['consolidate']['admissible']=='UNKNOWN'
    results['EX-MIN-01']='SOURCE_NATIVE_ILLUSTRATIVE_COUNTS_AND_UNVERIFIED_RIGHTS_MATCH'

    orange=original['ORANGE_RESEARCH_GATE']
    assert orange['price_collusion']=='NOT_ESTABLISHED' and orange['actor_experienced_suffering']=='NOT_MEASURED'
    assert runs['EX-ORANGE-01']['comparisons'][0]['stages'][0]['comparison']['status']=='NOT_ESTABLISHED'
    results['EX-ORANGE-01']='SOURCE_NATIVE_NOT_ESTABLISHED_MATCH'

    person=original['HUMAN_SCENARIO_LYCEE']
    assert person['observed_french_student']=='NOT_OBSERVED' and person['experienced_distress']=='NOT_MEASURED'
    assert runs['EX-HUMAN-01']['comparisons'][0]['stages'][0]['comparison']['status']=='NOT_ESTABLISHED'
    results['EX-HUMAN-01']='SOURCE_NATIVE_UNOBSERVED_HUMAN_MEASURES_MATCH'

    # These examples are source ANCHORED but not executed as a native case in
    # either of the above original programs. Our finite fixture is a distinct
    # operationalisation and cannot be counted as replication of source code.
    for name in ('EX-BAN-01','EX-BAN-02','EX-ROBIN-01','EX-SOLIDAR-01','EX-SUPER-01','EX-BUSINESS-01'):
        assert name in runs
        results[name]='NO_SAME_QUESTION_NATIVE_SOURCE_EXECUTOR; NEW_DECLARED_TOY_ONLY'
    assert set(results)==set(scenarios)
    return {'schema':'ACC-NARRATIVE-SOURCE-CONCORDANCE-v0.1',
            'source_sha256':{str(f.relative_to(STUDIES)):sha256(f.read_bytes()).hexdigest() for f in (f1,f2)},
            'source_match_count':8,'new_fixture_only_count':6,
            'cases':results,
            'qualification':'A source-native match is bounded synthetic consistency; it is not empirical confirmation or an independently observed effect.'}


def main(argv=None):
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args=parser.parse_args(argv)
    value=json.dumps(run(),indent=2,sort_keys=True,ensure_ascii=False)+'\n'
    if args.output: args.output.write_text(value,encoding='utf-8')
    else: print(value,end='')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
