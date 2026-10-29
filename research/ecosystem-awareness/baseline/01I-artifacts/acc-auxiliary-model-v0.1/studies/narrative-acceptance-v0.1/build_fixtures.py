"""Maintainer-only deterministic generator: EX IDs and passages anchored in ACC corpus."""
import json
from pathlib import Path

src='https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/'

def st(metrics=None,facts=None,payoffs=None,welfare=None):
    x={'metrics':metrics or {},'facts':facts or {},'payoffs':payoffs or {}}
    if welfare is not None:x['welfare']=welfare
    return x

def gate(name,status,category,note='DECLARED_SOURCE_INSPIRED_TOY_ASSUMPTION'):
    return {'id':name,'status':status,'category':category,'source_of_status':note}

def edge(name,origin,destination,guards=(),mode='unilateral',consumes=None,actor_nondecrease=False):
    v={'id':name,'from':origin,'to':destination,'mode':mode,'guards':list(guards)}
    if consumes:v['consumes']=consumes
    if actor_nondecrease:v['actor_nondecrease']=True
    return v

def case(name,anchor,dims,states,initial,edges,stages=None,comparisons=None,inv=None,budgets=None,interpretation=''):
    return {'case_id':name,'source_anchor':src+anchor,
       'evidence_tier':'AUTHOR_HYPOTHETICAL_TOY',
       'dimensions':{k:{'unit':u,'direction':d} for k,u,d in dims},
       'states':states,'initial':initial,'transitions':edges,
       'stages':stages or [{'id':'K_declared','axes':[x[0] for x in dims]}],
       'comparisons':comparisons or [],'state_invariants':inv or [],
       'resource_budgets':budgets or {},'interpretation':interpretation}

def co(a,b):return {'from':a,'to':b}

cases=[]
cases.append(case('EX-BAN-02','CASES.md#recorrido-de-variantes-y-condiciones-que-pueden-bloquear',
 [('E_transport','transport effort (toy units)','min'),('R_food','beneficiary portions','max')],
 {'held':st({'E_transport':0,'R_food':0},{'produced':1,'held':1,'received':0}),
 'sent':st({'E_transport':3,'R_food':1},{'produced':1,'held':0,'received':1})},
 'held',[edge('deliver_with_transport','held','sent',[gate('recipient_and_owner_consent','PASS','consent')],consumes={'logistic_slot':1})],
 comparisons=[co('held','sent')],budgets={'logistic_slot':1},
 interpretation='Africa is author clarification, not a field shipment; R improves, E worsens; transport units are invented.'))

cases.append(case('EX-BAN-01','model/01_NOTAS_COMPLETAS.md#s1-p0271',
 [('E_distance','illustrative km','min'),('R_food','beneficiary portions','max'),('C_effort','coordination effort units','min')],
 {'imported_discard':st({'E_distance':14000,'R_food':0,'C_effort':0},{'produced':1,'waste':1,'local_consumed':0}),
 'local_use':st({'E_distance':0,'R_food':1,'C_effort':2},{'produced':1,'waste':0,'local_consumed':1})},
 'imported_discard',[edge('organize_local_route','imported_discard','local_use',[
     gate('coordination_is_effective','UNKNOWN','coordination','NOT_ESTABLISHED_IN_SOURCE'),
     gate('title_and_contract_approvals','UNKNOWN','authority','NOT_ESTABLISHED_IN_SOURCE')])],
 stages=[{'id':'K2_E_R','axes':['E_distance','R_food']},{'id':'K3_E_R_C','axes':['E_distance','R_food','C_effort']}],
 comparisons=[co('imported_discard','local_use')],
 interpretation='14,000 km is hypothetical, not measured. K2 dominance can coexist with K3 tradeoff and no authorized transition.'))

cases.append(case('EX-BAN-03','model/01_NOTAS_COMPLETAS.md#s1-p0214',
 [('E_waste','food portions wasted','min'),('R_help','aid portions','max'),('C_extra','marginal logistics units','min'),('V_donor','donor credit share (toy fraction)','max')],
 {'discard':st({'E_waste':1,'R_help':0,'C_extra':0,'V_donor':1},payoffs={'donor':0,'recipient':0}),
 'donate_without_recognition':st({'E_waste':0,'R_help':1,'C_extra':0,'V_donor':'1/10'},payoffs={'donor':1,'recipient':1}),
 'donate_with_recognition':st({'E_waste':0,'R_help':1,'C_extra':0,'V_donor':1},payoffs={'donor':1,'recipient':1})},
 'discard',[edge('proposed_donation_declined','discard','donate_without_recognition',[
      gate('donor_declines_credit_sharing','FAIL','consent','HYPOTHETICAL_DONOR_PREFERENCE_NOT_REAL_ENTITY_BEHAVIOUR')]),
      edge('alternate_credit_accepted','discard','donate_with_recognition',[
      gate('donor_explicit_acceptance','PASS','consent','INVENTED_POSITIVE_CONTROL_WITH_HYPOTHETICAL_ACCEPTANCE')])],
 stages=[{'id':'K2_E_R','axes':['E_waste','R_help']},{'id':'K3_plus_C','axes':['E_waste','R_help','C_extra']},
         {'id':'K4_plus_V','axes':['E_waste','R_help','C_extra','V_donor']}],
 comparisons=[co('discard','donate_without_recognition'),co('discard','donate_with_recognition')],
 interpretation='Hypothetical donor preference, never attributed to actual Caritas conduct; separate absolute gains, consent and relative recognition.'))

cases.append(case('EX-BAN-04','model/01_NOTAS_COMPLETAS.md#s1-p0639',
 [('E_waste','portions wasted','min'),('R_child','child portions','max')],
 {'S0':st({'E_waste':0,'R_child':0},{'produced':0,'holder':0,'child':0,'waste':0},welfare={'B':0,'F':0,'W':0}),
 'S1':st({'E_waste':1,'R_child':0},{'produced':2,'holder':1,'child':0,'waste':1},welfare={'B':5,'F':7,'W':-2}),
 'S2':st({'E_waste':0,'R_child':1},{'produced':2,'holder':1,'child':1,'waste':0},welfare={'B':None,'F':None,'W':None})},
 'S0',[edge('grow_two','S0','S1'),edge('redistribute_one','S1','S2',[
     gate('safe_authorized_delivery','UNKNOWN','safety','SOURCE_STATES_FEASIBLE_ONLY_IF_ROUTE_SAFE_AND_LEGITIMATE')])],
 comparisons=[co('S0','S1'),co('S1','S2')],
 inv=[{'id':'fruit_conservation','kind':'sum_equals','fields':['holder','child','waste'],'target_field':'produced'},
      {'id':'toy_welfare_B_minus_F','kind':'welfare_identity','enforcement':'REPORT_ONLY'}],
 interpretation='Exact original S0/S1/S2 and B1=5 F1=7 W1=-2; F is stipulated toy, NEVER measured suffering.'))

cases.append(case('EX-ROBIN-01','model/01_NOTAS_COMPLETAS.md#s1-p0277',
 [('E_waste','coco+fish items wasted','min'),('R_both','positive-participant count (toy)','max'),('V_viernes','Viernes fraction of new gains','max')],
 {'lost':st({'E_waste':2000,'R_both':0,'V_viernes':'1/2'},
      {'coco_total':1000,'coco_lost':1000,'v_coco':0,'r_coco':0,'fish_total':1000,'fish_lost':1000,'v_fish':0,'r_fish':0},payoffs={'Viernes':0,'Robinson':0}),
 'unequal':st({'E_waste':0,'R_both':2,'V_viernes':'1/1000'},
      {'coco_total':1000,'coco_lost':0,'v_coco':1,'r_coco':999,'fish_total':1000,'fish_lost':0,'v_fish':1,'r_fish':999},payoffs={'Viernes':1,'Robinson':999})},
 'lost',[edge('proposal_with_relative_rejection','lost','unequal',[gate('Viernes_declines_relative_outcome','FAIL','consent','AUTHOR_HYPOTHETICAL_PREFERENCE')])],
 stages=[{'id':'K2_E_R','axes':['E_waste','R_both']},{'id':'K4_including_V','axes':['E_waste','R_both','V_viernes']}],
 comparisons=[co('lost','unequal')],
 inv=[{'kind':'sum_equals','fields':['coco_lost','v_coco','r_coco'],'target_field':'coco_total'},
      {'kind':'sum_equals','fields':['fish_lost','v_fish','r_fish'],'target_field':'fish_total'}],
 interpretation='Actual source quantity 1 coco+fish vs 999 each; actor payoffs are merely positive toy proxies, not measured preferences.'))

cases.append(case('EX-MIN-01','model/01_NOTAS_COMPLETAS.md#s1-p0104',
 [('E_apps','illustrative application count','min'),('R_affected','net actor well-being (unmeasured)','max')],
 {'fragmented':st({'E_apps':700,'R_affected':None},{'service_flag':1}),
 'unified':st({'E_apps':2,'R_affected':None},{'service_flag':1})},
 'fragmented',[edge('consolidate','fragmented','unified',[
     gate('service_guarantees_are_identical','UNKNOWN','continuity','SOURCE_CONDITIONAL_NOT_VERIFIED'),
     gate('institutional_authorization','UNKNOWN','authority','SOURCE_CONDITIONAL_NOT_VERIFIED')])],
 stages=[{'id':'E_only','axes':['E_apps']},{'id':'E_plus_R','axes':['E_apps','R_affected']}],
 comparisons=[co('fragmented','unified')],
 interpretation='700→2 is an image not field-measured. Nominal service flag is illustrative and does not prove full rights/quality equivalence.'))

utility=[0,4,7,8,7,5,5,9,10]
apple_states={f'q{i}':st({'U_actor':u},{'apples':i},payoffs={'buyer':u}) for i,u in enumerate(utility)}
apple_edges=[edge(f'buy_{i+1}',f'q{i}',f'q{i+1}',actor_nondecrease=True) for i in range(8)]
apple_edges.append(edge('joint_bridge_valley','q3','q8',[
    gate('financing_and_selling_route','PASS','coordination','INVENTED_VALID_JOINT_TRANSITION_POSITIVE_CONTROL')],mode='joint',actor_nondecrease=True))
cases.append(case('EX-APPLE-01','studies/bounded-traps-v0.1/EXAMPLE_LEDGER.md',
 [('U_actor','declared utility units','max')],apple_states,'q3',apple_edges,
 comparisons=[co('q3','q4'),co('q3','q8')],
 interpretation='Original nonmonotone utility table; unilateral nondecrease blocks 3→4, finite joint jump to 8 succeeds only under positive-control financing assumption.'))

cases.append(case('EX-LINEAR-01','ECONOMIC_MODEL_TECHNICAL_CORE_v0.1.md',
 [('U1','actor1 toy utility','max'),('U2','actor2 toy utility','max')],
 {f'{a}{b}':st({'U1':4+a,'U2':4+b},{'x1':a,'x2':b},payoffs={'actor1':4+a,'actor2':4+b}) for a in range(2) for b in range(2)},
 '00',[edge('first_alone','00','10'),edge('second_alone','00','01'),
       edge('atomic_together','00','11',mode='joint')],
 comparisons=[co('00','11')],
 inv=[{'kind':'equal_fields','fields':['x1','x2']}],
 interpretation='Both final 00,11 physically feasible; no feasible unilateral binary intermediate. Atomic joint is a distinct protocol, not new resources.'))

cases.append(case('EX-CREDIT-01','studies/bounded-traps-v0.1/EXAMPLE_LEDGER.md',
 [('V_A','credit to A (toy units)','max'),('V_B','credit to B (toy units)','max')],
 {'shares_7_3':st({'V_A':7,'V_B':3},{'share_A':7,'share_B':3}),
 'shares_7_4':st({'V_A':7,'V_B':4},{'share_A':7,'share_B':4})},
 'shares_7_3',[edge('raise_B_to_four','shares_7_3','shares_7_4')],
 comparisons=[co('shares_7_3','shares_7_4')],
 inv=[{'kind':'sum_at_most','fields':['share_A','share_B'],'limit':10}],
 interpretation='7+4 impossible with budget10; 7+3 compatible. Do not infer that any actor legitimately requires the declared share.'))

cases.append(case('EX-SOLIDAR-01','MODEL.md#fines-y-capacidades',
 [('E_cost','cost to donor (toy units)','min'),('R_received','aid portions','max')],
 {'retain':st({'E_cost':0,'R_received':0}),
 'without_choice':st({'E_cost':1,'R_received':1}),
 'with_choice':st({'E_cost':1,'R_received':1})},
 'retain',[edge('no_consent','retain','without_choice',[
 gate('person_choice_not_evidenced','UNKNOWN','consent','NOT_OBSERVED')]),
 edge('freely_chosen','retain','with_choice',[
 gate('person_affirmatively_consents','PASS','consent','INVENTED_POSITIVE_CONTROL_NOT_HUMAN_DATA')])],
 comparisons=[co('retain','without_choice')],
 interpretation='Same aid and cost can be offered, but legitimate chosen contribution requires own authorization; no scalar solidarity score.'))

cases.append(case('EX-ORANGE-01','studies/bounded-traps-v0.1/EXAMPLE_LEDGER.md',
 [('E_recovery','recoverable fruit count (not established)','max'),('R_need','utility of alternative (not measured)','max')],
 {'reported_waste':st({'E_recovery':None,'R_need':None},{'discard_report':1}),
 'proposed_recovery':st({'E_recovery':None,'R_need':None},{'discard_report':1})},
 'reported_waste',[edge('investigate_recovery','reported_waste','proposed_recovery',[
 gate('ownership_and_safety','UNKNOWN','authority','SOURCE_EXPLICITLY_UNVERIFIED'),
 gate('price_collusion_claim','UNKNOWN','evidence','SOURCE_EXPLICITLY_NOT_ESTABLISHED')])],
 comparisons=[co('reported_waste','proposed_recovery')],
 interpretation='An allegation about price manipulation is NOT a fact; unknown quantities and human distress remain unknown, not zero.'))

cases.append(case('EX-HUMAN-01','studies/bounded-traps-v0.1/EXAMPLE_LEDGER.md',
 [('capacity','realized development opportunities (unmeasured)','max')],
 {'school_then_job':st({'capacity':None}),
 'counterfactual_university':st({'capacity':None})},
 'school_then_job',[edge('access_to_university','school_then_job','counterfactual_university',[
 gate('available_university_place','UNKNOWN','evidence','SOURCE_NARRATIVE_NOT_OBSERVED'),
 gate('personal_choice','UNKNOWN','consent','SOURCE_NARRATIVE_NOT_OBSERVED')])],
 comparisons=[co('school_then_job','counterfactual_university')],
 interpretation='Hypothetical French lycée trajectory. No empirical student, distress, dignity or numerical potential is inferred.'))

cases.append(case('EX-SUPER-01','studies/bounded-traps-v0.1/EXAMPLE_LEDGER.md',
 [('output','delivered interface amount (toy units)','max')],
 {'limited':st({'output':800},{'declared_demand':1000,'delivery':800}),
 'fully_delivered':st({'output':1000},{'declared_demand':1000,'delivery':1000})},
 'limited',[edge('repair_unknown_bottleneck','limited','fully_delivered',[
 gate('root_capacity_evaluated','UNKNOWN','evidence','UNKNOWN_SUBSYSTEM_LIMIT')])],
 comparisons=[co('limited','fully_delivered')],
 interpretation='Source X−200 example instantiated with X=1000 as toy. Not a source-verified repair or physical availability claim.'))

cases.append(case('EX-BUSINESS-01','ECONOMIC_MODEL_TECHNICAL_CORE_v0.1.md',
 [('E_joint_gain','net toy surplus in one numerary','max'),('R_worst_actor','minimum declared affected actor outcome','max')],
 {'status_quo':st({'E_joint_gain':0,'R_worst_actor':0},payoffs={'marketing':0,'operations':0,'systems':0}),
 'raw_offer':st({'E_joint_gain':70,'R_worst_actor':-30},payoffs={'marketing':60,'operations':40,'systems':-30}),
 'compensated_after_cost':st({'E_joint_gain':55,'R_worst_actor':0},payoffs={'marketing':19,'operations':36,'systems':0})},
 'status_quo',[edge('raw_offer_without_compensation','status_quo','raw_offer',actor_nondecrease=True),
 edge('compensated_but_approval_unverified','status_quo','compensated_after_cost',[
 gate('CFO_authorizes','UNKNOWN','authority','NOT_ESTABLISHED_IN_SOURCE')],mode='joint',actor_nondecrease=True)],
 stages=[{'id':'E_only','axes':['E_joint_gain']},{'id':'E_plus_R','axes':['E_joint_gain','R_worst_actor']}],
 comparisons=[co('status_quo','raw_offer'),co('status_quo','compensated_after_cost')],
 interpretation='Source gross 60+40−30=70; transfer35 marketing→systems; hypothetical newly declared real cost split (6,4,5) sums15; no actual CFO consent.'))

manifest={'schema':'ACC-NARRATIVE-EXPERIMENTS-v0.1',
 'source_cutoff':'2026-10-29','fixture_status':'AUTHOR_HYPOTHETICAL_TOY',
 'cases':cases}
out=Path(__file__).with_name('cases.json')
out.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding='utf8')
print('wrote',len(cases),'cases /',out.stat().st_size,'bytes')
