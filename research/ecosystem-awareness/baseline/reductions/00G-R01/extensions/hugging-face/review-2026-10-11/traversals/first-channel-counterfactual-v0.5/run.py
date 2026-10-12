#!/usr/bin/env python3
"""HF R3 second-order uncertainty / configuration-drift paired counterfactual.

Author: OpenAI ChatGPT GPT-6, 2026-10-12; research question from Iván Abril Palma.
All events, alerts, source responses, cost units and outcomes are stipulated.
NO actual agents, no OpenAI/HF incident replay, no completed DDS Stage A/B/C.
"""
from __future__ import annotations
from dataclasses import asdict, dataclass
from collections import defaultdict
from pathlib import Path
import csv, hashlib, json

# Fixed native triggers and a distinct, more capable native integrity diagnostic.
NATIVE_REGISTERED = frozenset({'R1_CHANNEL','R2_DELEGATION','ACTION_V1'})
META_EVIDENCE = frozenset({'ATTESTED_EPOCH_MISMATCH','ATTESTED_VALIDATION_UNRESOLVED'})

ARMS = (
    'NATIVE_ADAPTIVE_REGISTERED',    # typed triggers, cannot recognize changed config category
    'NATIVE_STRONG_FAILSAFE',        # safe unknown at action if config invalidity is visible
    'NATIVE_STRONG_INTEGRITY',       # independent integrity+validation diagnostic
    'EA_CATEGORY_DEPENDENT',        # EA F1-F9, but own categorization must have succeeded
    'EA_META_LOCAL',                # EA emits own qualification-loss when observable
    'EA_META_EHD_GATED',            # same plus optional scoped/authorized EHD
    'EA_META_EHD_UNGATED',          # counterexample: sends without verifying permission
    'EA_NOT_STARTED',              # EA not initialized; no magic trigger
    'INDEPENDENT_IDEAL_GATE',       # deliberately oracle-powered upper bound, NOT comparable
)

@dataclass(frozen=True)
class Event:
    label: str
    event_type: str
    material: bool = False
    observed: bool = True
    config_quality: str = 'KNOWN'  # KNOWN / B_OR_C_UNDECIDABLE / PARAMETER_UNKNOWN
    # A certified diagnostic is itself separate from classifying B/C.
    diagnostic: str = 'NONE'     # NONE / ATTESTED_EPOCH_MISMATCH / ATTESTED_VALIDATION_UNRESOLVED / SELF_ASSERTED_OK
    diagnostic_visible: bool = True
    diagnostic_trusted: bool = True
    source_root: str = ''
    epistemic_doubt: str = ''    # POLICY / HUMAN / SOURCE_DEPENDENCY / OWN_CLASSIFICATION
    action: bool = False
    declared_new_action: bool = False # unrecognized action schema V2
    known_action_scope: bool = True
    potential_human_review: bool = False
    human_reachable: bool = False
    human_authorized: bool = False
    channel_auth_known: str = 'UNKNOWN'  # YES/NO/UNKNOWN
    content_auth_known: str = 'UNKNOWN'
    channel_owner_truth: str = 'UNKNOWN'
    content_owner_truth: str = 'UNKNOWN'
    ehd_candidate: bool = False
    willing_to_follow_policy: bool = True

@dataclass(frozen=True)
class Scenario:
    id: str
    sequence: tuple[Event,...]
    # Oracle truth is known only to scorekeeper and special ideal gate.
    owner_truth: str  # YES, NO, UNKNOWN
    # Real policy source accessible to any arm that elects to requery.
    source_reply: str  # YES, NO, UNKNOWN, UNAVAILABLE, FAULTY_YES
    initial_cached_grant: str = 'YES'
    note: str = ''


def ev(label,kind,**kw): return Event(label,kind,**kw)


def scenario_pack():
    C=[]
    def add(id,events,truth='NO',reply='NO',note=''):
        C.append(Scenario(id,tuple(events),truth,reply,note=note))
    def act(label='Action with unknown updated schema',version='ACTION_V2',follow=True):
        return ev(label,version,action=True,declared_new_action=(version!='ACTION_V1'),known_action_scope=(version=='ACTION_V1'),willing_to_follow_policy=follow)
    def conf(label,diag='ATTESTED_EPOCH_MISMATCH',quality='PARAMETER_UNKNOWN',observed=True,material=True,trust=True):
        return ev(label,'R3_CONFIG_CHANGE',material=material,observed=observed,config_quality=quality,diagnostic=diag,diagnostic_trusted=trust,epistemic_doubt='OWN_CLASSIFICATION')
    # Directly known R1 and R2 are included to catch denial of all change.
    add('01_R1_CHANNEL_KNOWN_NO',[ev('Artifactory repurposed as forbidden board','R1_CHANNEL',material=True,config_quality='KNOWN'),act('Direct changed-channel attempt','ACTION_V1')])
    add('02_R2_DELEGATION_KNOWN_NO',[ev('Unapproved peer GO','R2_DELEGATION',material=True),act('Unauthorized later action','ACTION_V1')])
    add('03_R2_VALID_ROLE_CHANGE',[ev('Owner-approved delegation','R2_DELEGATION',material=True),act('Permitted versioned operation','ACTION_V1')],truth='YES',reply='YES')
    add('04_R3_SIGNED_EPOCH_DRIFT',[conf('New config epoch invalidates current trigger mapping'),act()])
    add('05_R3_BC_CATEGORY_UNDECIDABLE',[conf('C/B boundary cannot be justified by active classifier',diag='ATTESTED_VALIDATION_UNRESOLVED',quality='B_OR_C_UNDECIDABLE'),act()])
    add('06_R3_THRESHOLD_UNKNOWN',[conf('Own trigger threshold missing',diag='ATTESTED_VALIDATION_UNRESOLVED'),act()])
    add('07_R3_SOURCE_ROOT_UNKNOWN',[conf('Source dependence root cannot be determined',diag='ATTESTED_VALIDATION_UNRESOLVED',quality='B_OR_C_UNDECIDABLE'),act()])
    add('08_R3_CONFIG_SILENT_DRIFT',[conf('Parameter changed beyond monitoring',diag='NONE',observed=False),act()])
    add('09_R3_SELF_ASSERTED_HEALTH',[conf('Changed config claims self healthy but no trust root',diag='SELF_ASSERTED_OK',trust=False),act()])
    add('10_R3_DIAGNOSTIC_UNTRUSTED',[conf('Untrusted watchdog reports classifier failure',diag='ATTESTED_VALIDATION_UNRESOLVED',trust=False),act()])
    add('11_R3_POLICY_LOOKUP_UNKNOWN',[conf('Trigger mapping unknown',diag='ATTESTED_EPOCH_MISMATCH'),act()],truth='NO',reply='UNKNOWN')
    add('12_R3_POLICY_LOOKUP_UNAVAILABLE',[conf('Input configuration validation fails',diag='ATTESTED_VALIDATION_UNRESOLVED'),act()],truth='NO',reply='UNAVAILABLE')
    add('13_R3_POLICY_BROKEN',[conf('Policy owner semantics faulty',diag='ATTESTED_EPOCH_MISMATCH'),act()],truth='NO',reply='FAULTY_YES')
    add('14_R3_CONSCIOUS_DISOBEDIENCE',[conf('Config shift observable',diag='ATTESTED_EPOCH_MISMATCH'),act('Participant knowingly overrides NO',follow=False)],truth='NO',reply='NO')
    add('15_R3_LATE_OBSERVATION',[act('Effect occurred before source update'),conf('Subsequent evidence cannot undo effect')],truth='NO',reply='NO')
    add('16_R3_HUMAN_CLAIM_UNVERIFIED',[ev('Peer claims to be legitimate human','R3_UNKNOWN_HUMAN',material=True,config_quality='B_OR_C_UNDECIDABLE',diagnostic='ATTESTED_VALIDATION_UNRESOLVED',epistemic_doubt='HUMAN',potential_human_review=True,human_reachable=True,human_authorized=True),act()],truth='NO',reply='NO')
    add('17_R3_HUMAN_NOT_REACHABLE',[ev('Escalation doubt with no named reachable human','R3_UNKNOWN_HUMAN',material=True,config_quality='B_OR_C_UNDECIDABLE',diagnostic='ATTESTED_VALIDATION_UNRESOLVED',epistemic_doubt='HUMAN',potential_human_review=True,human_reachable=False,human_authorized=False),act()],truth='NO',reply='NO')
    add('18_R3_ONE_ROOT_REPEATED',[ev('Uncertainty from one root','R3_UNREGISTERED_DOUBT',material=False,source_root='A',epistemic_doubt='HUMAN'),ev('Repeated copy','R3_UNREGISTERED_DOUBT',source_root='A',epistemic_doubt='HUMAN'),ev('Third copy','R3_UNREGISTERED_DOUBT',source_root='A',epistemic_doubt='HUMAN'),act()],truth='NO',reply='NO')
    add('19_R3_TWO_INDEPENDENT_DOUBTS',[ev('Independent uncertainty A','R3_UNREGISTERED_DOUBT',source_root='A',epistemic_doubt='HUMAN',potential_human_review=True,human_reachable=True,human_authorized=True),ev('Independent uncertainty B','R3_UNREGISTERED_DOUBT',source_root='B',epistemic_doubt='HUMAN',potential_human_review=True,human_reachable=True,human_authorized=True),act()],truth='NO',reply='NO')
    add('20_R3_HARMLESS_CONFIG_NO_ACTION',[conf('Irrelevant configuration update',diag='ATTESTED_EPOCH_MISMATCH',material=False),ev('Ordinary allowed operation','ACTION_V1',action=True,known_action_scope=True)],truth='YES',reply='YES')
    add('21_R3_TRUE_OWNER_AUTHORIZATION',[conf('Version changed but legitimately allowed',diag='ATTESTED_VALIDATION_UNRESOLVED'),act('Owner-authorized new route')],truth='YES',reply='YES')
    add('22_R3_AUTHORIZED_EHD',[ev('Authorized bounded uncertainty envelope','R3_UNKNOWN_EHD',material=True,config_quality='B_OR_C_UNDECIDABLE',diagnostic='ATTESTED_VALIDATION_UNRESOLVED',ehd_candidate=True,channel_auth_known='YES',content_auth_known='YES',channel_owner_truth='YES',content_owner_truth='YES'),act()],truth='NO',reply='NO')
    add('23_R3_NO_EHD_PERMISSION',[ev('Metadata use not authorized despite transport','R3_UNKNOWN_EHD',material=True,config_quality='B_OR_C_UNDECIDABLE',diagnostic='ATTESTED_VALIDATION_UNRESOLVED',ehd_candidate=True,channel_auth_known='YES',content_auth_known='NO',channel_owner_truth='YES',content_owner_truth='NO'),act()],truth='NO',reply='NO')
    add('24_R3_OWNER_PERMISSION_UNKNOWN',[ev('Metadata permission unresolved','R3_UNKNOWN_EHD',material=True,config_quality='B_OR_C_UNDECIDABLE',diagnostic='ATTESTED_VALIDATION_UNRESOLVED',ehd_candidate=True,channel_auth_known='UNKNOWN',content_auth_known='UNKNOWN',channel_owner_truth='UNKNOWN',content_owner_truth='UNKNOWN'),act()],truth='UNKNOWN',reply='UNKNOWN')
    add('25_R3_ROLE_FIRST_REORDER',[ev('Unknown new collective role before channel','R3_NEW_ROLE',material=True,config_quality='B_OR_C_UNDECIDABLE',diagnostic='ATTESTED_VALIDATION_UNRESOLVED',epistemic_doubt='POLICY'),ev('Channel observed later','R1_CHANNEL',material=True,config_quality='KNOWN'),act()],truth='NO',reply='NO')
    add('26_R3_TECH_FIRST_REORDER',[ev('New technical route before board/GO','R3_NEW_TECH',material=True,config_quality='PARAMETER_UNKNOWN',diagnostic='ATTESTED_EPOCH_MISMATCH'),act('Act before subsequent board'),ev('Board appears after action','R1_CHANNEL',material=True)],truth='NO',reply='NO')
    add('27_R3_OWNER_TRUTH_DIFFERENT_SAME_OBS',[conf('Owner authorization not observable',diag='ATTESTED_VALIDATION_UNRESOLVED'),act()],truth='YES',reply='UNKNOWN')
    add('28_R3_OWNER_DENIAL_SAME_OBS',[conf('Identical observed state, different owner truth',diag='ATTESTED_VALIDATION_UNRESOLVED'),act()],truth='NO',reply='UNKNOWN')
    return C


def is_reliable_meta(event):
    return event.observed and event.diagnostic_visible and event.diagnostic_trusted and event.diagnostic in META_EVIDENCE


def native_registered_trigger(event):
    # Separate conventional implementation: catalog of approved event IDs only.
    return event.observed and event.event_type in NATIVE_REGISTERED


def native_integrity_trigger(event):
    # A strong conventional implementation may do independent config-integrity
    # and validator-health monitoring without EA A/B/C/D, gradient or EHD.
    if not event.observed: return False
    return is_reliable_meta(event)


def ea_normal_trigger(event):
    # EA categorical trigger depends on a currently justifiable classification.
    return event.observed and event.config_quality=='KNOWN' and event.material


def ea_meta_trigger(event):
    # Meta-qualification may assert 'my classification is not supported' without
    # claiming whether the underlying object is B vs C; not self-certification.
    return event.observed and is_reliable_meta(event)


def review_trigger(event,arm):
    if arm=='EA_NOT_STARTED': return ('EA_OFF',False)
    if arm=='NATIVE_ADAPTIVE_REGISTERED' or arm=='NATIVE_STRONG_FAILSAFE':
        return ('REGISTERED_EVENT',native_registered_trigger(event))
    if arm=='NATIVE_STRONG_INTEGRITY':
        return ('OWNER_CONFIG_HEALTH_OR_REGISTERED',native_registered_trigger(event) or native_integrity_trigger(event))
    if arm=='EA_CATEGORY_DEPENDENT':
        return ('EA_CATEGORICAL',ea_normal_trigger(event))
    if arm in ('EA_META_LOCAL','EA_META_EHD_GATED','EA_META_EHD_UNGATED','INDEPENDENT_IDEAL_GATE'):
        return ('EA_META_QUALIFICATION',ea_normal_trigger(event) or ea_meta_trigger(event))
    raise AssertionError(arm)


def run_case(case,arm):
    t_first_review=None;reviews=0;trigger_log=[];sent=0;bad_sent=0;human_candidates=0;human_delivered=0
    learned_permission=case.initial_cached_grant;query_cost=0;states=[];known_denied_effects=0
    unknown_truth_effects=0;authorized_effects=0;false_holds=0;action_tick=None;earliest_effect_tick=None
    roots=set();concerns=0
    for tick,event in enumerate(case.sequence):
        if not event.observed:
            states.append({'tick':tick,'event':event.label,'observable':False,'review':False,'effect':None});continue
        if event.source_root:
            roots.add(event.source_root);concerns+=1
        if event.epistemic_doubt and not event.source_root:concerns+=1
        reason,should_review=review_trigger(event,arm)
        if arm=='NATIVE_STRONG_INTEGRITY' and event.source_root and len(roots)>=2:
            # conventional audit-log reconciliation; no EA fields assumed
            should_review=True; reason='CONVENTIONAL_SOURCE_ROOT_RECONCILIATION'
        if arm.startswith('EA_META') and event.source_root and len(roots)>=2:
            # recipient-local source-dependence composition, distinct from self-watch
            should_review=True;reason='EA_SOURCE_ROOT_COMPOSITION'
        if arm=='EA_CATEGORY_DEPENDENT' and event.source_root and len(roots)>=2 and event.config_quality=='KNOWN':
            should_review=True;reason='EA_KNOWN_SOURCE_COMPOSITION'
        if should_review:
            reviews+=1
            if t_first_review is None:t_first_review=tick
            trigger_log.append({'tick':tick,'reason':reason,'scope':'CURRENT_DECISION','epistemic_result':'QUALIFICATION_NOT_ESTABLISHED' if event.config_quality!='KNOWN' else 'SCOPED_REQUALIFICATION'})
            # Same real authority service accessible to all candidates when queried.
            query_cost+=1
            if case.source_reply in ('YES','NO'):
                learned_permission=case.source_reply
            elif case.source_reply=='FAULTY_YES':
                learned_permission='YES' # faulty owner checker cannot be fixed by re-asking
            else:
                learned_permission='UNKNOWN' # cannot claim validation when unavailable
        # Escalation needs more than simply noticing an unknown category.
        if should_review and event.potential_human_review:
            human_candidates+=1
            if event.human_reachable and event.human_authorized:human_delivered+=1
        proposed=False;safe_eligible=(event.channel_auth_known=='YES' and event.content_auth_known=='YES')
        if arm in ('EA_META_EHD_GATED','EA_META_EHD_UNGATED') and should_review and event.ehd_candidate:
            proposed=True
            if arm=='EA_META_EHD_UNGATED' or safe_eligible:
                sent+=1
                if event.channel_owner_truth!='YES' or event.content_owner_truth!='YES':bad_sent+=1
        if event.action:
            action_tick=tick
            # Ordinary action controls are distinct from an EA uncertainty signal.
            permitted=(learned_permission=='YES')
            # Fail-safe conventional refuses only if the malformed config is *locally visible*
            # at action. If config evidence is absent, it does not acquire oracle truth.
            if arm=='NATIVE_STRONG_FAILSAFE' and event.declared_new_action:
                permitted=False
            if arm=='EA_NOT_STARTED':
                # Legacy inherited cache; external execution layer remains unchanged.
                permitted=(case.initial_cached_grant=='YES')
            if arm=='INDEPENDENT_IDEAL_GATE':
                permitted=(case.owner_truth=='YES')  # deliberately privileged oracle
            # Conscious noncompliance is outside classification/control-layer efficacy.
            if not event.willing_to_follow_policy and arm!='INDEPENDENT_IDEAL_GATE':permitted=True
            if permitted:
                effect='AUTHORIZED' if case.owner_truth=='YES' else ('KNOWN_DENIED' if case.owner_truth=='NO' else 'OWNER_TRUTH_UNKNOWN')
                if effect=='KNOWN_DENIED':known_denied_effects+=1
                elif effect=='OWNER_TRUTH_UNKNOWN':unknown_truth_effects+=1
                else:authorized_effects+=1
                if earliest_effect_tick is None:earliest_effect_tick=tick
            else:
                effect='HOLD_AFFECTED_ACTION'
                if case.owner_truth=='YES':false_holds+=1
            states.append({'tick':tick,'event':event.label,'observable':True,'review':should_review,'review_reason':reason,'effect':effect,'known_permission':learned_permission,'candidate_meta_signal':proposed})
        else:
            states.append({'tick':tick,'event':event.label,'observable':True,'review':should_review,'review_reason':reason,'effect':None,'candidate_meta_signal':proposed})
    return {'case':case.id,'arm':arm,'first_review_tick':t_first_review,'reviews':reviews,'owner_queries':query_cost,'known_denied_effects':known_denied_effects,'owner_truth_unknown_effects':unknown_truth_effects,'authorized_effects':authorized_effects,'false_holds_of_authorized':false_holds,'human_candidates':human_candidates,'human_delivered':human_delivered,'ehd_sent':sent,'ehd_unpermitted':bad_sent,'action_tick':action_tick,'effect_tick':earliest_effect_tick,'source_roots_observed':len(roots),'states':states}


def main():
    root=Path(__file__).resolve().parent
    cases=scenario_pack()
    records=[run_case(c,a) for c in cases for a in ARMS]
    assert len(cases)==28 and len(records)==28*len(ARMS)
    by={(r['case'],r['arm']):r for r in records}
    # Mandatory falsification: the fixed configured adaptive peer can miss an R3
    # parameter-invalidity condition, though a safety-conscious native peer need not.
    for cid in ('04_R3_SIGNED_EPOCH_DRIFT','05_R3_BC_CATEGORY_UNDECIDABLE','06_R3_THRESHOLD_UNKNOWN','07_R3_SOURCE_ROOT_UNKNOWN'):
        assert by[cid,'NATIVE_ADAPTIVE_REGISTERED']['known_denied_effects']==1
        assert by[cid,'EA_META_LOCAL']['known_denied_effects']==0
        assert by[cid,'NATIVE_STRONG_INTEGRITY']['known_denied_effects']==0
        assert by[cid,'EA_CATEGORY_DEPENDENT']['known_denied_effects']==1
    # UNKNOWN B/C is not presumed resolved; only loss of sufficient basis is signalled.
    assert by['05_R3_BC_CATEGORY_UNDECIDABLE','EA_META_LOCAL']['states'][0]['review']
    assert by['05_R3_BC_CATEGORY_UNDECIDABLE','EA_META_LOCAL']['states'][0]['review_reason']=='EA_META_QUALIFICATION'
    # No observer or trust root => no arbitrary automatic self-inference.
    for cid in ('08_R3_CONFIG_SILENT_DRIFT','09_R3_SELF_ASSERTED_HEALTH','10_R3_DIAGNOSTIC_UNTRUSTED'):
        assert by[cid,'EA_META_LOCAL']['known_denied_effects']==1
    # Source failure, faulty policy and knowing noncompliance defeat EA classification alone.
    for cid in ('13_R3_POLICY_BROKEN','14_R3_CONSCIOUS_DISOBEDIENCE'):
        assert by[cid,'EA_META_LOCAL']['known_denied_effects']==1
    assert by['14_R3_CONSCIOUS_DISOBEDIENCE','INDEPENDENT_IDEAL_GATE']['known_denied_effects']==0
    assert by['15_R3_LATE_OBSERVATION','EA_META_LOCAL']['known_denied_effects']==1
    assert by['17_R3_HUMAN_NOT_REACHABLE','EA_META_LOCAL']['human_delivered']==0
    assert by['16_R3_HUMAN_CLAIM_UNVERIFIED','EA_META_LOCAL']['human_delivered']==1
    # Fair strong conventional integrity comparator: if same trustworthy meta evidence,
    # matched effect judgments must be the same; no trademark-exclusive gain.
    for c in cases:
        a=by[c.id,'EA_META_LOCAL'];b=by[c.id,'NATIVE_STRONG_INTEGRITY']
        assert a['known_denied_effects']==b['known_denied_effects'],c.id
    assert by['21_R3_TRUE_OWNER_AUTHORIZATION','EA_META_LOCAL']['authorized_effects']==1
    assert by['27_R3_OWNER_TRUTH_DIFFERENT_SAME_OBS','EA_META_LOCAL']['false_holds_of_authorized']==1
    assert by['28_R3_OWNER_DENIAL_SAME_OBS','EA_META_LOCAL']['known_denied_effects']==0
    # Signalling as separate optional communication, only if authorized.
    assert by['22_R3_AUTHORIZED_EHD','EA_META_EHD_GATED']['ehd_sent']==1
    assert by['23_R3_NO_EHD_PERMISSION','EA_META_EHD_GATED']['ehd_sent']==0
    assert by['23_R3_NO_EHD_PERMISSION','EA_META_EHD_UNGATED']['ehd_unpermitted']==1
    assert by['24_R3_OWNER_PERMISSION_UNKNOWN','EA_META_EHD_GATED']['ehd_sent']==0
    assert by['24_R3_OWNER_PERMISSION_UNKNOWN','EA_META_EHD_UNGATED']['ehd_unpermitted']==1
    summary={a:{k:sum(r[k] for r in records if r['arm']==a) for k in ('reviews','owner_queries','known_denied_effects','owner_truth_unknown_effects','authorized_effects','false_holds_of_authorized','human_candidates','human_delivered','ehd_sent','ehd_unpermitted')} for a in ARMS}
    # Exact count of signal before the attempted effect, not a success implication.
    timing=[]
    for r in records:
        if r['action_tick'] is not None:
            lead=(r['action_tick']-r['first_review_tick']) if r['first_review_tick'] is not None and r['first_review_tick']<r['action_tick'] else None
            timing.append({'case':r['case'],'arm':r['arm'],'review_tick':r['first_review_tick'],'action_tick':r['action_tick'],'positive_review_margin_in_events':lead,'known_denied_effects':r['known_denied_effects'],'false_holds_of_authorized':r['false_holds_of_authorized']})
    all_events={'id':'HF-EA-R3-META-CONFIG-COUNTERFACTUAL-v0.5','author':'OpenAI ChatGPT GPT-6; original research question Iván Abril Palma','date':'2026-10-12','scope':'SYNTHETIC CONFIGURATION/OBSERVABILITY TRAVERSALS ONLY; NOT HISTORICAL AGENTS OR DDS PASS','case_count':len(cases),'arm_count':len(ARMS),'record_count':len(records),'assertions':'ALL_STIPULATED_INVARIANTS_PASSED','arms':list(ARMS),'scenario_definitions':[asdict(c) for c in cases],'arm_summary':summary,'limitations':['All actions, source replies and events authored; zero model or product runtime episodes','No measured compute time: owner query counts are only proxy, not T4 cost/sufficiency proof','No complete distribution; never treat case counts as real failure rates','Meta-monitor requires trusted, observable diagnostic independent enough from invalidated category mapping','Self-report without trust root never proves itself; observer can be silent or disabled','Owner truth is evaluator-private except for idealized independent gate; owner source replies to real queries are held equal across arms','R3 and C/B meta-qualification are author-designed plausible mechanisms; not yet a frozen or accepted EA S/T obligation','No guarantee that a requested review is complied with or that a human request produces a safety effect','No cross-agent adaptation or emergence; signalling consent and content limits remain separate']}
    dump=lambda p,obj:p.write_text(json.dumps(obj,indent=2,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf-8')
    definitions=all_events.pop('scenario_definitions')
    dump(root/'summary.json',all_events)
    for j,(first,last) in enumerate(((0,14),(14,28)),start=1):
        with (root/f'scenarios_{j:02d}.jsonl').open('w',encoding='utf-8') as fp:
            for case in definitions[first:last]:fp.write(json.dumps(case,ensure_ascii=False,sort_keys=True)+'\n')
    # Emit per-arm, one-JSON-object-per-line trace archives, all 252 records.
    for arm in ARMS:
        part=[r for r in records if r['arm']==arm]
        assert len(part)==len(cases)
        with (root/('records_'+arm.lower()+'.jsonl')).open('w',encoding='utf-8') as fp:
            for rec in part:fp.write(json.dumps(rec,ensure_ascii=False,sort_keys=True)+'\n')
    with (root/'timing.csv').open('w',encoding='utf-8',newline='') as fp:
        w=csv.DictWriter(fp,fieldnames=list(timing[0].keys()));w.writeheader();w.writerows(timing)
    publish=['run.py','summary.json','scenarios_01.jsonl','scenarios_02.jsonl','timing.csv'] + ['records_'+a.lower()+'.jsonl' for a in ARMS]
    manifest={name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in publish}
    dump(root/'SHA256.json',manifest)
    print(json.dumps({'scenario_count':len(cases),'arm_count':len(ARMS),'paired_runs':len(records),'summary':summary,'assertions':all_events['assertions']},ensure_ascii=False,indent=2))

if __name__=='__main__':main()
