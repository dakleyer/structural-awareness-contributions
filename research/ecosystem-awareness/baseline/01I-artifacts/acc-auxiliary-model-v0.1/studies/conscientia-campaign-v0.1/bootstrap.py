import json
from pathlib import Path
root=Path(__file__).resolve().parent
S=[
('CE-NOTES','NOTAS DE TRABAJO — Conscientia Ecosystemica para Magnifica Humanitas — One-pager 1: elección, solidaridad y dos mecanismos','1QUzDHPp-yjrgCsjpXq7HLVMldNUO4iOFZ-4W2t4mHuI','working','§10A–10E; IQ-01–IQ-06; HID §6A; status mixes modelling and hypothetical examples'),
('CE-SOLIDARITY-V3','De la dependencia sufrida a la solidaridad elegida — Conscientia Ecosystemica para Magnifica Humanitas — v3','1aKYkPlmuaiNv51QtW51q30fiNDdXrZ-1LQOJ2EGKhrg','working','Three contributions: economic gap, UC21 technical falsifier, voluntary solidarity'),
('CE-DIALOGUE-V4','De la dependencia sufrida a la solidaridad elegida — Diálogo experimental con Magnifica Humanitas — v4','1Y2xQduM_P4PnGs3Z9-d3ZypBfoNLW7b2Pl4ZC0ntvaQ','working','Three contributions; social burden and genuine voluntary choice; not a Vatican endorsement'),
('CE-SCHEME','Conscientia Ecosystematis — Saber lo que no sabemos, deriva de misión y elección humana','1YRehP7BuSOR9qBhFs3OOrYrPjH3TDvoL4hPJ9eFV-TY','working','FH-C / FH-E, mission changes, A/B/C/D, falsification and UC21 S1–S6'),
('CE-ANTS','A/B/C/D y reposicionamiento: hormigas metamórficas','1ZBCAoni5TUVxGkbFGeTY0uRSBaS14vWYK3hhHDXlmww','historical','Analogical historical vocabulary; for experiment use canonical 00M, not its earlier B/C meanings'),
('CE-CAPACITY','Preservación de capacidades — Clausura arquitectónica, inteligencia humana y coherencia democrática','1QHzTPaEGY0OCgUr-ObswadFGgrh7JP8XIxX-t36tj1M','working','Six cases: incapacity, equations learning, professional accountability, France, crafts, administrative usability; hypothesis of feasible alternatives'),
('CE-CORRESPONDENCE','Conscientia Ecosystematis para Magnifica Humanitas — Correspondencia técnica y social','1rJTg__x4xKYRQbo63hFH3V-BNtkxsgnCUwgQ-oUCPck','working','Attribution Gap/HID/Informational Friction/Cost of Clarity; custody of essential capabilities'),
('CE-SOCIAL-WORK','DOCUMENTO DE TRABAJO — Composición abierta de indeterminación y modelo social multiagente — v0.6','1qpBDFBZa7nGKlTD2D5poYuStCf0oJcAogBtUuzEjD90','research-note','Parts I–VII; mathematical conditions, toy hypotheses, previously run analyses, no external validation'),
('AG-D01','RESEARCH DOSSIER 01 — The Attribution Gap and Capability Loss v8','1FXSKDD9sxXUXaqM99FgM3tFPe4UD3vAcT0rA5V3FVCI','dossier','Claim A dependency–attribution discrepancy; controls listed-without-dependency and unlisted-dependent; not field-observed'),
('AG-D02','RESEARCH DOSSIER 02 — Measuring the Attribution Gap v2','1wgFHAKE9sZFWrgvCIe4HUcK5cO3tuSidC2q24BVEFKU','dossier','Five signatures S1–S5; source PDF vs HTML disagree on E formula — BLOCK_FOR_COMPUTATION'),
('HID-D06','RESEARCH DOSSIER 06 — The Human Intelligence Debt Dilemma','1UXDkojn5NjQCB6wZeiB7Y9Rg3ysLzpL92lA3uUHnAvk','dossier','productive, blocking and integrator agents; incentives and roles, no observed motives'),
('IF-D10','RESEARCH DOSSIER 10 — Optimization, Coherence, and the Frame','1sMuoAcfAqq8uQeeR98NBkr8-NChS2mZBQ1DmKSdAMuA','dossier','Attribution vs coherent frame, suppression beyond cost; distinct causal question'),
('CC-D17','RESEARCH DOSSIER 17 — How to Measure the Cost of Not Knowing','12GPkA8fYZvqIrhsC1SF2mg9-JStmbJPeYy4wcBJU7jc','dossier','Capture-recapture assumptions and source-owner observation effects; no empirical sample'),
('HID-D20','RESEARCH DOSSIER 20 — What Goes Unpriced Is Paid in Human Intelligence','1vwTSpSK_f4ePjg3ayRwI3fDkB9fqzYpWA4BiYL8n7qk','dossier','Human ACW GIC NEO UNKNOWN categories and causal feedback; need independent measurement'),
('ENT-DIST','Distorsión Entrópica: Método y Laboratorio','19VwS524d9Kx3RVXbZjSdUn5yi9gRYAF-H66Mut540EU','historical','Finite preimage coverage; original orientation of KL has a mathematical counterexample'),
('ENT-AUDIT','MATHEMATICAL_CLAIM_AUDIT — Entropic Primitive, Incompleteness and EA Transfer','1lBdXV47NjRY9pIbQlfYsdCcwGjSz_3k85P7m47Zw9J8','mathematical-audit','Finite coverage log2(m/n) not Shannon entropy; KL support and Landauer transfer cautions'),
('CE-MH-NOTE','Ciencia ecosistémica y Magnifica Humanitas — Nota breve para comentarios','1P-b6PNdYW4iEQ4s37U6VJQc9XbANWpRiUSt3rIDCYr4','working','Human-development framing and UC21 S4 discussion; not empirical'),
('CE-MH-ONEPAGER','2026-10-25 — Conscientia Ecosystemica — copia íntegra previa al plan de 14 inserciones','1EOMd1wwuXTp3BdVDjJ3vVed8an1H4EZ2pbTJbZUmHpo','historical','Historical copy, reference only; no independent new observations'),
('CE-PRESCIENCE','2026-09-07 Ecosystem Awareness Conceptual Foundations and Minimum Sufficient Awareness','1EKkIX4BGTUE7ehApKDGGnzz4G20J26ZPcTxOydHGnRc','conceptual','Minimum sufficient awareness — antecedent, not test observation'),
]
records=[{'source_id':sid,'title':title,'url':f'https://docs.google.com/document/d/{id}/edit','role':role,'relevant_passage':anchor,'source_evidence_tier':'AUTHOR_CONCEPT_OR_INTERNAL_REVIEW'} for sid,title,id,role,anchor in S]
records += [
 {'source_id':'00M-CANON','title':'00M v0.8 A/B/C/D and mathematical plausibility','url':'https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md','role':'canonical-semantics','relevant_passage':'§1 A/B/C/D and §4 task sufficiency','source_evidence_tier':'FORMAL_DEFINITION_AND_BOUNDED_THEOREM'},
 {'source_id':'01K-HID','title':'01K HC-HID capacity component','url':'https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/01K_A01_HUMAN_CAPACITY_HID_COMPONENT_SPEC_v0.1.md','role':'measurement-owner','relevant_passage':'§6 task-time GIC/NEO/ACW/UNKNOWN; §7 costs','source_evidence_tier':'EXISTING_CONTRACT_NOT_OBSERVATION'},
 {'source_id':'UC21-SOURCE','title':'UC21 frozen source and Annex R','url':'https://github.com/dakleyer/structural-awareness-contributions/blob/main/governance/preserved-public-snapshots/UC21_aec08fb5_source/contributions/when-controls-work-system-fails/USE_CASE.md','role':'source-owner','relevant_passage':'S1–S6, R0/R1/R2, 37 source-local gates; no native product tests','source_evidence_tier':'FROZEN_CASE_AND_CONTRACT'},
 {'source_id':'ACC-EXAMPLES','title':'ACC example ledger PR42','url':'https://github.com/dakleyer/structural-awareness-contributions/blob/research/acc-rational-bottlenecks-nonmonotone-20261026/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/bounded-traps-v0.1/EXAMPLE_LEDGER.md','role':'example-provenance','relevant_passage':'EX-BAN/ORANGE/ANT/VERS/CREDIT/LINEAR/APPLE/SUPER/HUMAN/SOLIDAR/PRICES','source_evidence_tier':'AUTHOR_HYPOTHETICAL_AND_TOY'}]
(root/'SOURCE_REGISTER.json').write_text(json.dumps({'schema_version':'0.1','source_cutoff':'2026-10-26','note':'Registry of referenced sources, NOT evidence that all texts were screened. See SOURCE_REVIEW_CLAIMS.json and source_provenance.py for dated review claims and case-level usage. Source-derived assertions remain separate from synthetic assumptions.','sources':records},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

profiles=[
 ('VERS','version and joint-interface compatibility','CE-SCHEME','EX-VERS-01'),
 ('LINEAGE','correlated evidence/mission drift','CE-SCHEME','EX-ANT-01'),
 ('AUTH','scope and authority in composed decisions','CE-CORRESPONDENCE','EX-MIN-01'),
 ('CAP','provider capacity and shared root','CE-SOCIAL-WORK','EX-SUPER-01'),
 ('COORD','joint transitions and indispensable coordination','CE-NOTES','EX-LINEAR-01'),
 ('CREDIT','functional status and credit shares','CE-NOTES','EX-CREDIT-01'),
 ('ATTR','dependency versus attribution discrepancy','AG-D01','EX-ORANGE-01'),
 ('FRAME','frame validity and coherent decision','IF-D10','EX-ANT-01'),
 ('CLARITY','cost of partial knowledge and selective review','CC-D17','EX-SUPER-01'),
 ('EDUC','human capabilities and educational opportunities','CE-CAPACITY','EX-HUMAN-01'),
 ('SOLID','voluntary contribution and genuine consent','CE-DIALOGUE-V4','EX-SOLIDAR-01'),
 ('RIGHTS','third-party rights and material residual','CE-MH-NOTE','EX-BAN-03'),
]
variants={
 'VALID_GO':('ALLOW','REVIEW','B','ALLOW','CURRENT_VALID','ALLOW',True),
 'VALID_BLOCK':('BLOCK','ALLOW','B','BLOCK','CURRENT_VALID','BLOCK',True),
 'STALE':('BLOCK','REVIEW','B','ALLOW','STALE','BLOCK',True),
 'FALSE_Q':('BLOCK','REVIEW','B','ALLOW','CURRENT_BUT_FALSE','BLOCK',True),
 'OPEN_RESIDUAL':('NOT_ADJUDICABLE','REVIEW','D',None,'UNEVALUABLE','NOT_AVAILABLE',False)
}
cases=[]
for j,(key,name,src,ex) in enumerate(profiles):
 for v,(truth,baseline,q_kind,q_verdict,q_status,peer_verdict,peer_avail) in variants.items():
  no_full=j in (7,9,10,11) or v=='OPEN_RESIDUAL'
  # Half of the routine cases are correctly handled by ordinary A-only controls.
  if v=='VALID_GO' and j%2==0: baseline='ALLOW'
  if v=='VALID_BLOCK' and j%2==1: baseline='BLOCK'
  # Some selected panels have costlier source-native Q than existing ordinary peer
  q_cost=1.0 if j%4 in (0,1) else 2.2
  peer_cost=0.5 if j%4==0 else 1.6
  if v=='OPEN_RESIDUAL': q_kind='C' if j%2==0 else 'D'
  cases.append({
   'case_id':f'{key}-{v}', 'family':key,'label':name,'variant':v,
   'primary_source_id':src,'example_id':ex,
   'truth_private_for_scoring':truth,
   'public':{'A':'READY','decision_question':'admissibility_of_declared_transition',
             'baseline_action':baseline,'version':'toy-v1','scope_id':f'{key}-SCOPED'},
   'Q':{'kind':q_kind,'verdict':q_verdict,'status':q_status,'source_id':f'{key}-SOURCE',
        'scope_id':f'{key}-SCOPED','fresh':q_status in ('CURRENT_VALID','CURRENT_BUT_FALSE'),
        'provenance_established':True,'independent_audit':v in ('VALID_GO','VALID_BLOCK') or (v=='FALSE_Q' and j%3==0),
        'audit_cost':0.3,'cost':q_cost},
   'peer':{'has_direct_evidence':peer_avail,'verdict':peer_verdict,'cost':peer_cost},
   'expanded_A':{'available':not no_full,'verdict':truth if truth!='NOT_ADJUDICABLE' else None,'cost':14.0},
   'utility':{'correct_allow':10.0,'correct_block':4.0,'false_allow':-12.0,'false_block':-5.0,'review':0.0},
   'test_evidence_tier':'SYNTHETIC_FIXTURE','not_a_real_person_or_product':True,
  })
reg={'schema_version':'0.1','frozen_case_count':len(cases),'design':'Twelve illustrative source-mapped mechanisms × five preregistered positive/negative variants; outcomes deliberately synthetic, not a statistically representative sample.','cases':cases}
(root/'CASE_REGISTRY.json').write_text(json.dumps(reg,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print('sources',len(records),'cases',len(cases))
