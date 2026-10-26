<!--
Source-preserving Markdown mirror of a Google Doc historically labelled INTERNAL. The corpus owner expressly authorized public research-corpus promotion on 25 October 2026. Historical source labels remain quoted faithfully; this does not grant rights in third-party underlying evidence, endorse the case, or constitute an experimental result.
Google Docs title: Panodyssey — Industry Challenge Map & FG-TIDA ToR Traceability — v0.1
Google Docs source: https://docs.google.com/document/d/1qA8XG_L7ZJbwBOlOb37r4Qm7J6nG_AcSCddnzEAAPi8/edit
Observed Google Docs revision: AHj4eMTvxsu8vkYtuDc_NpAb7dCQl_a3Wl4EeChKdPUDQKDm3G4ngLt2j5ZMtH1U-2aXKM3TpOClpVGS5IB3kJ6MYwKwFQanIcdyzxvjCcs
Captured: 2026-10-25 (Europe/Madrid)
Status: historical/working source; not an executed validation, a legal conformity assessment, or FG-TIDA endorsement.
-->

**INTERNAL / NOT FOR EXTERNAL CIRCULATION — current additive revision v0.6 — 25 October 2026 — NOT ASSESSED / NOT FROZEN**

# Panodyssey — Industry Challenge Map & FG-TIDA ToR Traceability — v0.1

Working reference • 16 September 2026


# Purpose

This working document captures the complete preliminary industry challenge map for the Panodyssey delegated-authority case. It is a challenge reference, not a product assessment, a solution architecture, an adopted FG-TIDA outcome, or a final mapping.


# Working sequence

1. Case Study — the operational world and facts, as presented by Alexandre.

2. Technical Challenge Map — the recurring industrial problems exposed by that case.

3. ToR mapping — after challenge validation, anchor each confirmed challenge to the relevant FG-TIDA Terms of Reference.

4. Use Cases — select the smallest non-redundant family needed to test the confirmed challenges.


# Validation rule

Each challenge should be marked jointly as Confirmed, Partially covered, Open, Conditional, or Outside scope. The list is deliberately broader than any initial three use cases so that use cases do not silently determine the problem statement.


# Industry Challenge Map (S1–S14)


## S1 — Authority provenance and current applicability

Can the system establish the origin, scope, standing, expiry or revocation of authority, and whether it is binding at the action time?

Preliminary ToR anchors: 4.3; A.1.2; A.2.2. Supporting: A.2.7.


## S2 — Preference fidelity and reviewable decision basis

Can a delegated action remain faithful to the applicable preferences and limits, with a basis that can be reviewed?

Preliminary ToR anchors: 3.4; 4.1; A.2.1. Supporting: A.2.4.


## S3 — Regime and context qualification

Can the system recognize changed conditions and determine whether the original authority or control frame remains valid?

Preliminary ToR anchors: 4.3; A.2.2; A.2.4; A.2.8.


## S4 — Human oversight authority and capacity

Does escalation reach an authority that can meaningfully intervene, with sufficient operational capacity to do so?

Preliminary ToR anchors: 3.4; 4.3; 4.5; A.2.4.


## S5 — Operational indeterminacy and containment

How should incomplete or conflicting authority and trust evidence be contained safely, without pretending it has been resolved?

Preliminary ToR anchors: 3.4; 4.3. Supporting: A.2.2; A.2.7.


## S6 — Interoperable, privacy-preserving trust determination

How can actors exchange machine-readable trust information across systems without unnecessary disclosure?

Preliminary ToR anchors: 3.4; 4.2; 4.4; A.2.5.


## S7 — Identity and representation link

Can the relationship among the actor, its represented principal, and the applicable authority be established and kept attributable?

Preliminary ToR anchors: 2; 4.2; A.1.1; A.1.2.


## S8 — Bounded subdelegation and non-amplification

Can authority pass through a chain without silently expanding its scope, duration, permissions, or revocation conditions?

Preliminary ToR anchors: A.1.2; 4.3. Supporting: A.2.2; A.2.7.


## S9 — Multi-principal composition, non-substitution and conflict

How should the system handle several principals, heterogeneous trust sources, and conflicts without assuming a universal hierarchy?

Preliminary ToR anchors: 2; 4.2; A.2.1; A.2.5; A.2.7.


## S10 — Commitment state and material change

Can the system distinguish recommendation, commitment and action, and trigger re-evaluation when a material change occurs?

Preliminary ToR anchors: 4.3; A.2.2. Supporting: A.2.7.


## S11 — Policy integrity across domains and jurisdictions

Can policy information preserve its origin, scope and meaning across sectors, systems and jurisdictions without attempting to standardise substantive law?

Preliminary ToR anchors: 4.4; A.1.5; A.2.5. Supporting: 4.2.


## S12 — Accountability, challenge and repair

Can a party reconstruct what happened, challenge a decision, and repair the future trust state without rewriting the past?

Preliminary ToR anchors: 3.4; 4.5; A.2.4. Supporting: A.2.2.


## S13 — Authority history versus intervention history

Can the history of authority and the history of later intervention remain distinct while the current operative authority is unambiguous?

Preliminary ToR anchors: 4.3; A.1.2; A.2.4; A.2.7.


## S14 — Evidence-to-decision assessment

Can the system represent the evidence required, its sufficiency and status, the supported decision, and any remaining indeterminacy?

Preliminary ToR anchors: 3.4; 4.5; A.2.2; A.2.4.


# Initial mapping of Olena’s three proposed operational situations

1. Permission change or revocation after prior authorization → S1, S10 and S13; S5 only when the evidence is incomplete or conflicting.

2. Uncertain or insufficiently verified AI/crawler identity → S7, S6 and S14.

3. Rights-holder intent is evidenced but AI compliance cannot be established → S12, S14 and S5; S4 only when a human decision is required.


# What this does and does not say

These mappings identify candidate industry challenges. They do not state that Panodyssey has every challenge, that any particular mechanism is sufficient, or that a component is already standardised. The next step is validation of the challenge list; only then should the ToR map be finalised and the minimum necessary use cases selected.


# References

• Panodyssey email discussion: “Follow-up: Panodyssey Case Mapping for TIDA”, including Olena Pavlenko’s three operational situations and Alexandre Leforestier’s reply.

• FG-TIDA working reference: “05 — ANNEX IV — FG-TIDA ToR Mapping and Traceability — v1.0”.

• Method proposed for this work: Case Study → Technical Challenge Map → Use Cases.


# ADDITIVE v0.2 — 25 October 2026 — INTERNAL REFERENCE MATRIX

The complete v0.1 text above, S1–S14 identities and preliminary ToR anchors are preserved. This additive table extends the same working map with the requested AI Act and other-reference columns; it is not a replacement Challenge Pack.

UC1–UC3 below use their original consolidated titles and scope. Direct/partial describes evidence coverage, not product maturity or a passed Challenge. Source: the 29 September consolidated mapping. Revision v0.3 restores the row-specific evidence cautions; S3 is conditional/emerging in its detailed source row, while that message's summary also grouped it with open/future coverage. No row is forced into the three-case core.

The current pack has one Panodyssey Challenge with three trajectories, one per specific UC (T-UC1, T-UC2, T-UC3); Challenge and trajectory are distinct levels. Earlier draft terminology equating them is superseded. Historical S labels remain dimension identifiers. Neither ToR alignment nor a standards/legal reference establishes compliance, adoption or a guarantee. Reference conditions, editions and sources: https://docs.google.com/document/d/1mLp2Sb1q2dD67FKBqQMiZ9hR__t2snyitFIwcwpi78Y/edit?usp=drivesdk

Original pack and approved field structure: https://docs.google.com/document/d/1lU4zfSA1I5RMPxjoPrRMtp4ZXMIKvebCPko47ZgUMIk/edit?usp=drivesdk

Official live ToR: https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx

The matrix retains selective relevance judgments only. Exact gate-to-provision equivalence/applicability remains PENDING REVIEW.


| **Challenge dimension** | **UC / current evidence coverage** | **Preliminary ToR anchors retained** | **B — EU legislation (conditional: DSM, AI Act, GDPR, eIDAS)** | **C — Other international / technical references** |
| --- | --- | --- | --- | --- |
| S1 — Authority provenance and current applicability | UC1 — DIRECT / PARTIAL. Permission state and modification history are evidenced; downstream recognition and action-time applicability remain open. | [4.3; A.1.2; A.2.2. Supporting: A.2.7.](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx) | [DSM](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=celex%3A32019L0790) Directive (EU) 2019/790 Art. 4(3): TDM reservation, subject to rightsholder, use and national-law review. [AI Act](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-53) (EU) 2024/1689 Art. 53(1)(c): only in-scope GPAI providers. [eIDAS](https://eur-lex.europa.eu/eli/reg/2014/910/) (EU) 910/2014 Art. 41 only if timestamp evidence used; not proof of title. | [ODRL 2.2](https://www.w3.org/TR/2018/REC-odrl-model-20180215/): Policy/Rule/Constraint; [PROV-O](https://www.w3.org/TR/2013/REC-prov-o-20130430/): attribution/history. Expressions and provenance do not establish legal standing. |
| S2 — Preference fidelity and reviewable decision basis | OPEN. Potentially relevant where machine-readable permissions represent only part of rights-holder intent; open in the current three-use-case set. | [3.4; 4.1; A.2.1. Supporting: A.2.4.](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx) | [DSM](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=celex%3A32019L0790) Art. 4(3) may govern a specific TDM reservation; no EU provision here establishes fidelity to unexpressed preferences. No direct [AI Act](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-53) duty mapped. | [ODRL 2.2](https://www.w3.org/TR/2018/REC-odrl-model-20180215/): parties, actions, constraints and profiles. Encoding does not establish fidelity to unexpressed intent. |
| S3 — Regime and context qualification | CONDITIONAL / EMERGING. Relevant to the RAG extension but not yet a fully evidenced current-use-case claim. | [4.3; A.2.2; A.2.4; A.2.8.](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx) | [DSM](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=celex%3A32019L0790) Art. 4(1),(3): qualify lawful-access TDM, reserved rights, actual use and national implementation. Training, RAG and indexing are not presumed equivalent. No general [AI Act](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-53) context-gate duty mapped. | [NIST AI RMF](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) 1.0 MAP/MANAGE: context and change, voluntary guidance; not legal or product conformance. |
| S4 — Human oversight authority and capacity | CONDITIONAL. UC3 only where human/institutional intervention is required; full oversight-capacity architecture is not evidenced by the Panodyssey layer itself. | [3.4; 4.3; 4.5; A.2.4.](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx) | [AI Act](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14) Art. 14(1)–(4): only where high-risk AI-system requirements apply (not presumed). [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) Arts. 5(2), 24 only for a personal-data controller; neither establishes operational human intervention capacity. | [NIST AI RMF](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) GOVERN/MEASURE, voluntary oversight guidance. [ISO/IEC 42001](https://committee.iso.org/cms/live/live/en/sites/isoorg/contents/data/standard/08/12/81230.html):2023 is management-system context only; no clause-to-gate claim. |
| S5 — Operational indeterminacy and containment | UC3; UC1 where updated-permission evidence is incomplete — DIRECT / PARTIAL. Residual indeterminacy is evidenced; containment should not be attributed to Panodyssey unless separately demonstrated. | [3.4; 4.3. Supporting: A.2.2; A.2.7.](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx) | [DSM](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=celex%3A32019L0790) Art. 4(3) may be relevant to rights reservations for TDM; missing evidence is neither proof of infringement nor proof of compliance. No direct general [AI Act](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-53) indeterminacy duty mapped. | [NIST AI RMF](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) MEASURE/MANAGE: assess uncertainty and response. Local unknown/HOLD semantics must be specified separately. |
| S6 — Interoperable, privacy-preserving trust determination | UC2 — DIRECT / PARTIAL. Machine-readable rights and actor references exist; complete interoperable trust determination remains open. | [3.4; 4.2; 4.4; A.2.5.](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx) | [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) (EU) 2016/679 Arts. 5(1)(c),(f), 6, 32 only if trust evidence processes personal data. No general [AI Act](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-53) trust-determination duty mapped. | [W3C VC](https://www.w3.org/TR/2025/REC-vc-data-model-2.0-20250515/) Data Model 2.0: issuer/holder/verifier, trust model and privacy. Data exchange does not establish issuer trust or permission. |
| S7 — Identity and representation link | UC2 — DIRECT / PARTIAL. A technical crawler/agent identifier is not necessarily the accountable organisational/legal actor to whom authority applies. | [2; 4.2; A.1.1; A.1.2.](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx) | [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) Arts. 5, 6 only if a natural person is identifiable. [eIDAS](https://eur-lex.europa.eu/eli/reg/2014/910/) Art. 35 only if electronic-seal evidence is used; seal integrity/origin does not prove organisational mandate. No AI legal-personhood finding. | [W3C VC](https://www.w3.org/TR/2025/REC-vc-data-model-2.0-20250515/) 2.0 claims and issuer/subject binding; [RFC 9334](https://www.rfc-editor.org/info/rfc9334/) RATS roles/appraisal. Attestation state is not organisational mandate or legal representation. |
| S8 — Bounded subdelegation and non-amplification | OPEN. Requires an onward agent/tool/intermediary delegation chain not evidenced in the current three-use-case set. | [A.1.2; 4.3. Supporting: A.2.2; A.2.7.](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx) | No direct EU article-to-subdelegation requirement established here; scope of mandate and onward delegation needs contract/role review. No binding conclusion. | [ODRL 2.2](https://www.w3.org/TR/2018/REC-odrl-model-20180215/) Policy Inheritance and Rule Composition are expression mechanisms; mandate non-amplification needs an explicit application contract. |
| S9 — Multi-principal composition, non-substitution and conflict | OPEN. Potential independent author/publisher/platform/provider/territorial constraints; not directly established by the current three cases. | [2; 4.2; A.2.1; A.2.5; A.2.7.](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx) | [DSM](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=celex%3A32019L0790) Art. 4(3) may supply one rightsholder reservation where applicable; multiple principals, territories and independent constraints need separate legal review. No universal precedence rule inferred. | [ODRL 2.2](https://www.w3.org/TR/2018/REC-odrl-model-20180215/) parties and Rule Composition; independent constraints/conflicts require declared receiver semantics, not an assumed universal hierarchy. |
| S10 — Commitment state and material change | UC1 — DIRECT / PARTIAL. Material change is evidenced; downstream revalidation remains open. | [4.3; A.2.2. Supporting: A.2.7.](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx) | [DSM](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=celex%3A32019L0790) Art. 4(3): review operative reservation for the action if applicable. [eIDAS](https://eur-lex.europa.eu/eli/reg/2014/910/) Art. 41 can support chronology where timestamp evidence is used; not a statutory general revalidation gate. | [PROV-O](https://www.w3.org/TR/2013/REC-prov-o-20130430/) wasRevisionOf / invalidatedAtTime: version and invalidation history. Provenance alone does not execute revalidation. |
| S11 — Policy integrity across domains and jurisdictions | OPEN / EMERGING. Strict separation of training/RAG/indexing is relevant; RAG direction is not a completed current-state capability. | [4.4; A.1.5; A.2.5. Supporting: 4.2.](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx) | [DSM](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=celex%3A32019L0790) Art. 4(1),(3): conditional TDM exception and reservation. [AI Act](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-53) Art. 53(1)(c): in-scope GPAI-provider copyright policy only. Training, RAG and indexing need separate use/legal analysis. | [ODRL 2.2](https://www.w3.org/TR/2018/REC-odrl-model-20180215/) profiles/constraints; [TDMRep](https://w3c-cg.github.io/tdm-reservation-protocol/spec/) Community Group specification and [aipref-vocab-08](https://www.ietf.org/archive/id/draft-ietf-aipref-vocab-08.html) draft as distinct signal references. Neither is evidence of compliance. |
| S12 — Accountability, challenge and repair | UC3 — DIRECT / PARTIAL. Rights-declaration state/history reconstructable; downstream behaviour may remain unknown. | [3.4; 4.5; A.2.4. Supporting: A.2.2.](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx) | Copyright remedies and liability depend on applicable law and competent review; none determined here. [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) Art. 5(2) applies only if relevant personal-data controller accountability arises. | [PROV-O](https://www.w3.org/TR/2013/REC-prov-o-20130430/) derivation/attribution and version history; [NIST AI RMF](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) MANAGE supports response planning, not legal repair. |
| S13 — Authority history versus intervention history | UC1 — DIRECT / PARTIAL. Authority-history side evidenced; separate later intervention history would be an extension. | [4.3; A.1.2; A.2.4; A.2.7.](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx) | [eIDAS](https://eur-lex.europa.eu/eli/reg/2014/910/) Art. 41 if electronic timestamps are relied on; qualified status requires evidence. [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) Arts. 5, 32 only if personal-data event logs are processed. History does not prove later intervention. | [PROV-O](https://www.w3.org/TR/2013/REC-prov-o-20130430/) entities, activities, agents and revisions can distinguish grant history from later intervention; source semantics must remain explicit. |
| S14 — Evidence-to-decision assessment | UC2/UC3 — DIRECT / PARTIAL. Assess what particular decision the evidence is sufficient to support, not merely whether evidence exists. | [3.4; 4.5; A.2.2; A.2.4.](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx) | [DSM](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=celex%3A32019L0790) Art. 4(3) / [AI Act](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-53) Art. 53(1)(c): relevance subject to actor, use and territory. [eIDAS](https://eur-lex.europa.eu/eli/reg/2014/910/) Art. 41 only if electronic timestamp evidence is used. No compliance or sufficiency verdict implied. | [PROV-O](https://www.w3.org/TR/2013/REC-prov-o-20130430/) evidence links; [RFC 9334](https://www.rfc-editor.org/info/rfc9334/) Evidence, Attestation Results and appraisal policy. [ISO/IEC 42001](https://committee.iso.org/cms/live/live/en/sites/isoorg/contents/data/standard/08/12/81230.html) is contextual only; no clause-level conformance asserted. |


## TITLE VARIANTS — SOURCE CROSSWALK, NOT A CANONICAL RENAME

S3: historical map “Regime and context qualification”; Annex III v1.3 “Regime, context, escalation & bounded escape path”.

S4: historical map “Human oversight authority and capacity”; Annex III v1.3 “Human-inclusive oversight authority & capacity”.

S10: historical map “Commitment state and material change”; Annex III v1.3 “Commitment state, material change & normal escalation”.

S11: historical map “Policy integrity across domains and jurisdictions”; Annex III v1.3 “Policy, objective & preference integrity across domains”.

The historical map labels are preserved. Shared S numbers are cross-reference keys, not demonstrated semantic equivalence. Selecting current canonical title authority and reviewing scope differences remain PENDING. Annex III source blob readback: 58cd3f780919d14ab785e56ba537b4e3d7922b47; source: https://github.com/dakleyer/structural-awareness-contributions/blob/e79cae15cbf0f015021718f1b1a95b561643d8da/submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/04_ANNEX_III_Challenges_Exposed_by_the_Case.md A blob ID is not a campaign freeze.


INTERNAL / NOT FOR EXTERNAL CIRCULATION — additive correction v0.3, 25 October 2026. Original v0.1 paragraphs and preliminary ToR anchors remain unchanged; original title retained. Source validation labels are not results. New package NOT ASSESSED / NOT FROZEN. Evidence-route namespace E1–E5; roadmap RM0–RM7; canonical Q0–Q5 unchanged.


Revision v0.5 — 25 October 2026. Original map structure, historical text, preliminary ToR anchors and native 15×5 reference table retained; scoped external-audit corrections only. AI-assisted; source authorship retained; joint acceptance NOT RECORDED. Baseline: https://docs.google.com/document/d/1L5eZFwtFnHWnFL6oiV30_zDIGEhyIJUJfSn2EedCj4Q · Preserved v0.4: https://docs.google.com/document/d/1mTmeCClsdjOKZkWqUfNJTkALUj6CLNiz4m_1OroUaX8/edit?usp=drivesdk


**ADDITIVE v0.6** — 25 October 2026. The original native 15×5 matrix's EU reference column now contains conditional legislation beyond the AI Act (DSM Art. 4, GDPR where personal data are processed, and eIDAS where electronic trust evidence is used); the ToR and S1–S14 columns remain structurally unchanged. The international/technical column is distinct. Gate/trajectory-level crosswalk (T-UC1/T-UC2 without frozen gate IDs; T-UC3 E1–E5 local drafts): https://docs.google.com/document/d/12ekNFP1pfe1eC6uxqN2t5lbbaPzVazL064Ytrz9DWEw/edit. Full legal/technical reference legend: https://docs.google.com/document/d/1mLp2Sb1q2dD67FKBqQMiZ9hR__t2snyitFIwcwpi78Y/edit. All applicability, equivalence, assessment and external release remain PENDING.
