"""Prospective cost/type-diagnostic successor, not a regrading of frozen originals."""
import argparse, collections, copy, hashlib, json, platform, sqlite3
from pathlib import Path
from fractions import Fraction
import cryptography
import adapters

HERE=Path(__file__).resolve().parent
def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def dump(path,value):
    with Path(path).open('x',encoding='utf-8',newline='\n') as stream:
        json.dump(value,stream,ensure_ascii=False,indent=2);stream.write('\n')

def inputs(name):
    c=adapters.card(name)
    if name!='hew':return c['cases'],c.get('parameters',{})
    rows=[]
    for s in c['scenarios']:
        for position,(public,authority,private) in enumerate(zip(s['public_cases'],s['environment_authority_inputs'],s['private_worlds'])):
            rows.append({'id':public['operation_id'],'scenario_id':s['scenario_id'],'position':position,
                         'narrative':s['human_narrative'],'public':public,'authority':authority,'private':private,
                         'expected': 'P' if s.get('expected_violation',False) else 'I' if s['expected_sufficient_delivery'][position] else 'Ø'})
    return rows,{}

def expected(case):
    if 'expected' in case:return case['expected']
    if 'expected_qualified_outcome' in case:return {'incomplete':'Ø'}.get(case['expected_qualified_outcome'],case['expected_qualified_outcome'])
    return 'I' if case['expected_qualified_delivery'] else 'Ø'

def meaningful_closure(row,name):
    if row['outcome'] not in ('I','M'):return False
    if name=='hew':return row['model_work_units']<=row['model_work_budget']
    if name=='durable-workflows-retries':return row['logical_elapsed_ticks']<=adapters.card(name)['parameters']['deadline_ticks']
    return row['cost']['C_selected_api_units']<=256

def run(name,case,p,out,mode):
    out.mkdir(parents=True,exist_ok=False)
    result=adapters.ADAPTERS[name](copy.deepcopy(case),p,out,mode)
    ledger=result['cost']
    assert ledger['candidate_trace_sha256_before_adjudication'], 'No candidate seal'
    assert ledger['C_selected_api_units']==sum(ledger['candidate_components'].values())
    assert all(e['units']>=0 for e in ledger['events'])
    if name=='hew':assert result['model_work_units']==sum(result['model_work_components'].values())
    result['source_case_id']=case['id'];result['policy']=mode
    return result

def diagnose(row, witnesses, name, eligible_record):
    good=[w for w in witnesses if meaningful_closure(w,name)]
    admitted=bool(good)
    # Admission is frozen in the first phase, before this candidate's adjudication.
    assert admitted==eligible_record['M_admitted']
    primary=lambda x:x['model_work_units'] if name=='hew' else x['cost']['C_selected_api_units']
    winner=min(good,key=primary) if good else None
    t1=admitted and row['outcome']=='Ø'
    t2=row['outcome']=='P' and row['T2_mechanism']
    assert not(t1 and t2)
    witness=primary(winner) if winner else None
    observed=primary(row)
    cause=row['cause']
    accessible_G = None
    if name=='spiffe-jwt' and winner:
        # Mandatory primitives in the registered selected API convention:
        # two JSON parses, one actual signature verify, identity qualification,
        # and one receiving policy check per requested delivery/replay response.
        accessible_G=4+winner['cost']['candidate_components']['resource.policy']
        assert winner['cost']['C_selected_api_units']==accessible_G
    return {'source_case_id':row['source_case_id'],'M_admission':eligible_record,
       'C_observed_primary':observed,'primary_unit':'declared HEW model work' if name=='hew' else 'selected API operation units',
       'C_private_min_G':witness,'minimum_domain':'two frozen admitted qualification graphs G; not all software/algorithms',
       'witness_policy':winner['policy'] if winner else None,
       'witness_api_cost':winner['cost']['C_selected_api_units'] if winner else None,
       'private_excess_signed':observed-witness if witness is not None else None,
       'private_excess_nonnegative':max(0,observed-witness) if witness is not None else None,
       'lower_cost_without_closure_is_not_a_saving':bool(witness is not None and observed<witness and row['outcome'] not in ('I','M')),
       'accessible_information_global_lower_bound':None,
       'accessible_information_global_bound_status':'NOT_ESTABLISHED',
       'accessible_information_lower_bound_G':accessible_G,
       'accessible_G_certificate':'2 JSON parses + 1 native verify + 1 identity policy + required resource policy calls; sole trust domain known to actor' if accessible_G is not None else None,
       'accessible_feasible_witness_cost':witness,
       'accessible_witness_uses_evaluator_labels':False,
       'witness_is_not_claimed_global_optimum':True,
       'Type1_eligible':admitted,'Type1':t1,'Type2_eligible':True,'Type2':t2,
       'P_without_diagnosed_Type2':row['outcome']=='P' and not t2,
       'terminal_cause':cause,'ineligible_no_closure_is_not_Type1':row['outcome']=='Ø' and not admitted,
       'search_and_validation_components':row['cost']['candidate_components'],
       'excess_by_component_against_witness':{key:row['cost']['candidate_components'].get(key,0)-winner['cost']['candidate_components'].get(key,0)
           for key in sorted(set(row['cost']['candidate_components'])|set(winner['cost']['candidate_components']))} if winner else None}

def aggregate(rows):
    diag=[r['diagnostics'] for r in rows]
    d1=sum(r['Type1_eligible'] for r in diag);n1=sum(r['Type1'] for r in diag)
    d2=sum(r['Type2_eligible'] for r in diag);n2=sum(r['Type2'] for r in diag)
    def fraction(n,d):return {'numerator':n,'denominator':d,'fraction':str(Fraction(n,d)) if d else None,
        'meaning':'descriptive fraction over named authored fixtures; no deployment/population probability',
        'statistical_uncertainty':'NOT_APPLICABLE_NO_RANDOM_POPULATION_SAMPLE'}
    return {'cases':len(rows),'outcomes':dict(collections.Counter(r['candidate']['outcome'] for r in rows)),
      'Type1':fraction(n1,d1),'Type2':fraction(n2,d2),'P_without_Type2':sum(r['P_without_diagnosed_Type2'] for r in diag),
      'Type1_exclusions':sum(not r['Type1_eligible'] for r in diag),
      'total_selected_api_units':sum(r['candidate']['cost']['C_selected_api_units'] for r in rows),
      'sum_is_not_money_or_a_cross_technology_ranking':True}

def main(output):
    freeze=json.loads((HERE/'FREEZE.json').read_text());registration=json.loads((HERE/'RUN_CARD.json').read_text())
    for path,sha in freeze['files'].items():assert digest(HERE/path)==sha,('input freeze mismatch',path)
    assert platform.python_version()==registration['runtime']['python']
    assert sqlite3.sqlite_version==registration['runtime']['sqlite']
    assert cryptography.__version__==registration['runtime']['cryptography']
    out=Path(output);out.mkdir(parents=True,exist_ok=False)
    profiles={};qualified={};prepared=[]
    try:
        # Phase 1: compute the complete evaluator map / reachable minimum before candidate runs.
        for name in registration['profiles']:
            cases,p=inputs(name);state={};qualified[name]={};prepared.append((name,cases,p))
            for c in cases:
                if name=='hew':c['prior_reservations']=state.get(c['scenario_id'],[])
                witnesses=[]
                for mode in ['baseline','reference']:
                    w=run(name,c,p,out/'witnesses'/name/c['id']/mode,mode);witnesses.append(w)
                good=[w for w in witnesses if meaningful_closure(w,name)]
                admission={'M_admitted':bool(good),'nontrivial_qualification_work':all(w['cost']['C_selected_api_units']>0 for w in good) if good else None,
                  'closure_floor':'original sufficient legitimate closure; original I/M may collapse the value distinction',
                  'witness_policies':[w['policy'] for w in good],
                  'capability_and_interface_basis':'same original selected actor APIs; reference policy removes only declared redundant restarts or chooses admitted bounded deferment',
                  'within_registered_budget_and_horizon':bool(good),'private_expected_outcome_sent_to_actor':False,
                  'exclusion_if_not_admitted':'no qualifying closure in frozen G: source/scope/state/authority/capacity/effect-contract barrier; no Type1 label',
                  'admission_not_based_on_candidate_outcome':True}
                qualified[name][c['id']]={'witnesses':witnesses,'admission':admission}
                if name=='hew':state[c['scenario_id']]=witnesses[0]['reservations']
        admission={name:{key:value['admission'] for key,value in cases.items()} for name,cases in qualified.items()}
        dump(out/'M_ADMISSION_BEFORE_CANDIDATES.json',admission)
        admission_hash=digest(out/'M_ADMISSION_BEFORE_CANDIDATES.json')
        for name,cases,p in prepared:
            rows=[];state={}
            for c in cases:
                if name=='hew':c['prior_reservations']=state.get(c['scenario_id'],[])
                result=run(name,c,p,out/'candidate'/name/c['id'],'baseline')
                assert result['outcome']==expected(c),(name,c['id'],result['outcome'],expected(c))
                q=qualified[name][c['id']]
                diag=diagnose(result,q['witnesses'],name,q['admission'])
                rows.append({'id':c['id'],'narrative':c.get('narrative',c.get('human_narrative','')),'candidate':result,'diagnostics':diag})
                if name=='hew':state[c['scenario_id']]=result['reservations']
            # Fault controls are reported in a separate cohort, never pooled with the original-world rows.
            control_spec=registration['fault_controls'][name]
            controls=[]
            for mode,target in control_spec.items():
                c=copy.deepcopy(next(c for c in cases if c['id']==target))
                if name=='hew':c['prior_reservations']=[]
                q=qualified[name][c['id']]
                result=run(name,c,p,out/'controls'/name/mode,mode)
                diag=diagnose(result,q['witnesses'],name,q['admission'])
                assert diag['Type1'] if mode=='review_only' else diag['Type2'],(name,mode,result)
                controls.append({'id':target+'-'+mode,'narrative':'Deliberate defect control; not the native technology or qualified actor performance.',
                                 'candidate':result,'diagnostics':diag})
            profiles[name]={'original_world_replay':aggregate(rows),'fault_controls':aggregate(controls),
                           'rows':rows,'controls':controls,'M_admission_artifact_sha256':admission_hash}
            dump(out/(name+'.json'),profiles[name])
            print(json.dumps({'profile':name,'baseline':profiles[name]['original_world_replay'],'controls':profiles[name]['fault_controls']},ensure_ascii=True),flush=True)
        final={'status':'PASS_PROSPECTIVE_SELECTED_COST_AND_TYPE_DIAGNOSTICS','profiles':profiles,
          'canonical_stage':'A','mode':'same-author selected native/local/finite-model evidence',
          'source_commit':registration['source_commit'],'run_card_sha256':digest(HERE/'RUN_CARD.json'),
          'freeze_sha256':digest(HERE/'FREEZE.json'),'M_admission_artifact_sha256':admission_hash,
          'native_product_or_human_validation':False,'Stage_B_or_C_established':False,
          'case_fractions_are_not_population_rates':True,'global_minimum_or_superiority_established':False,
          'original_frozen_results_changed':False}
        dump(out/'RESULTS.json',final)
    except Exception as error:
        dump(out/'FAILED_ATTEMPT.json',{'error':repr(error),'completed_profiles':list(profiles),'prospective_freeze_sha256':digest(HERE/'FREEZE.json')})
        raise

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);main(parser.parse_args().output)
