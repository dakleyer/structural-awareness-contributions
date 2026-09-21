# Annex 01F — Ecosystem Awareness / FG-TIDA Specification Preparation Map

**Status:** Draft v0.1 — specification-preparation control document  
**Date:** 21 September 2026  
**Corpus:** Ecosystem Awareness (EA)  
**Placement:** additive companion to the EA canonical corpus; not part of the frozen v0.4 architecture baseline  
**Institutional status:** preparation only; not an FG-TIDA Working Group charter, specification, deliverable, adopted requirement, editor appointment, leadership claim or ITU-T position

> **Purpose.** This annex prepares the existing Ecosystem Awareness corpus for possible translation into one or more future FG-TIDA Working Group specifications. It does not create new EA theory or silently upgrade research hypotheses, candidate interfaces, external-theme semantics or validation artefacts into normative requirements. The canonical source documents remain authoritative for their own claims. This annex records how they could be projected into a specification, what is mature enough to carry forward, what remains informative or test-only, and what requires FG-TIDA or semantic-owner confirmation before promotion.

## 1. Why this annex exists

EA is already larger and more mature than a single theme comment or concept paper. The public corpus contains:

- a canonical problem and requirements model;
- a shared topology and terminology;
- an implementation-neutral functional architecture;
- a general epistemic handoff model;
- candidate cross-theme contracts and a current-state FG-TIDA bridge;
- reference failure scenarios and product-implementation profiles;
- architecture-validation profiles and an interoperability test;
- benchmark and falsification design;
- research lineage, provenance and governance records; and
- explicit interfaces with independently maintained MSCA, Regime Awareness/EWS and DAOS corpora.

FG-TIDA has now published a Working Group specification template and an initial `wg1-ra-aai` specification repository. The missing object for EA is therefore not another research corpus. It is a controlled editorial bridge from the existing corpus to the structure, status discipline and contribution model expected of a future specification.

This annex has four objectives:

1. define the candidate specification object without pre-empting FG-TIDA placement or Working Group structure;
2. map every specification section to existing canonical source material;
3. distinguish normative candidates from research hypotheses, examples, external-owner semantics and test evidence; and
4. define explicit readiness gates so a future WG repository can be created without losing source lineage or overstating maturity.

## 2. Current FG-TIDA specification model

The current public FG-TIDA tooling establishes the following practical publication model:

- each specification is maintained in its own public repository created from `FG-TIDA/spec-template`;
- repositories use a Working Group naming convention such as `wg<N>-<short-name>`;
- the document has standard front matter: title, subtitle, abstract, history, authors, keywords and foreword;
- document metadata is maintained separately in the specification build configuration;
- chapters are authored as a structured specification rather than as a mirror of a research repository;
- diagrams, tables, figures, cross-references and optional OpenAPI material can be included;
- GitHub pull requests provide review and contribution history;
- accepted changes rebuild a public HTML site and a PDF automatically; and
- the specification repository becomes the editorial source for that WG document.

The first public FG-TIDA example, `wg1-ra-aai`, currently uses a problem-to-gap structure:

1. landscape / industry analysis;
2. problem statement;
3. core challenges;
4. fundamental technical questions;
5. standards building blocks;
6. future directions; and
7. references.

EA does **not** need to copy that chapter structure. The template provides the publication framework; the technical structure should follow the EA problem and any future WG charter.

## 3. Candidate specification identity

### 3.1 Working title

A neutral working title for preparation purposes is:

**Ecosystem Awareness for Independently Governed Agentic Ecosystems**

Candidate subtitle:

**Decision-scoped epistemic qualification, interoperable handoff and bounded requalification across changing dependencies**

These names are placeholders. A future WG or editor group may adopt another title.

### 3.2 Candidate abstract

Ecosystem Awareness addresses a specific interoperability and control problem in agentic ecosystems: locally valid outputs from independently governed humans, agents, policies, evaluators, attesters and infrastructure do not necessarily compose into a sufficiently supported system-level conclusion. The proposed architecture makes the decision scope, evidence boundary, source dependence, residual indeterminacy, capacity constraints and useful response horizon explicit; preserves source-native semantics across handoffs; and supports targeted requalification when the operating frame becomes insufficiently supported. The work is implementation-neutral and does not create authority, replace producer-owned semantics, require disclosure of complete internal reasoning, or assume a central ecosystem controller.

### 3.3 Intended audience

Candidate audience:

- agentic-AI architects and implementers;
- trust, identity, attestation and policy-system designers;
- distributed-system and multi-agent infrastructure teams;
- human-oversight and governance-system designers;
- relying parties consuming independently produced determinations;
- standards contributors defining cross-system interfaces; and
- testbed and conformance-profile authors.

### 3.4 Candidate keywords

Ecosystem Awareness; agentic AI; epistemic handoff; residual indeterminacy; uncertainty preservation; requalification; interoperability; distributed trust; human oversight capacity; source provenance; decision scope; response horizon; conformance.

## 4. Scope and non-goals

### 4.1 Candidate scope

A future EA specification should define, at minimum:

- the decision-scoped problem that EA addresses;
- the common terminology required to describe bounded representation and residual state;
- the minimum functional responsibilities of an EA implementation;
- the distinction between local producer determination and ecosystem-level qualification;
- the minimum semantics required for interoperable epistemic handoff;
- rules for preserving scope, provenance, source-native result, uncertainty, capacity and unresolved qualifiers;
- conditions for targeted requalification rather than indiscriminate context expansion;
- ownership boundaries with authority, identity, policy, attestation, incident lifecycle, human oversight and enforcement mechanisms;
- conformance expectations for adapters and handoffs; and
- informative use cases and test profiles showing how the requirements can be exercised.

### 4.2 Explicit non-goals

A future EA specification should not:

- create or confer legal, institutional, policy or containment authority;
- define a universal trust or reputation score;
- require a central ecosystem controller or common internal reasoning model;
- require every participant to implement EA internally;
- translate source-native outputs into EA states merely for uniformity;
- treat confidence, assurance, authority, capacity or residual indeterminacy as interchangeable;
- require maximum context collection or unrestricted graph expansion;
- define the complete human-oversight lifecycle owned by Theme #16 or its successor;
- redefine authority provenance, delegation, identity, policy-conformance or attestation semantics owned elsewhere;
- make MSCA, Regime Awareness/EWS or DAOS subcomponents of EA;
- convert research hypotheses into standards requirements without separate review;
- claim that an internal freeze, test design or public discussion constitutes FG-TIDA adoption; or
- prescribe implementation-specific algorithms, thresholds or product architectures unless a future profile explicitly chooses to do so.

## 5. Candidate specification family

The corpus can support either one integrated specification or a small family. This annex does not decide the split.

### Option A — one integrated specification

**EA Core Architecture and Interoperability**

One document would contain the core problem, terminology, requirements, functional architecture, EHD, external profiles and conformance method. Use cases and test vectors would remain informative annexes.

This option is editorially simple but may become large and may mix core semantics with cross-theme profile material that has different owners and maturity.

### Option B — two specifications

**EA-CORE — Ecosystem Awareness Core Architecture**

Would cover:

- problem and scope;
- terminology/topology;
- requirements;
- F1–F9 functional responsibilities;
- operating postures and requalification;
- ownership/non-ownership boundaries; and
- core security/privacy considerations.

**EA-EHD — Epistemic Handoff and Interoperability**

Would cover:

- EHD kernel;
- source-native semantics;
- scope/provenance/issuer;
- operational result/closure;
- determination state;
- explicit UNKNOWN qualification;
- conditional qualifiers such as capacity, freshness, lineage and inherited indeterminacy;
- profile extensibility;
- adapter rules;
- cross-implementation conformance; and
- domain/theme profiles.

This split is technically clean if EHD is confirmed as a reusable abstraction beyond Theme #13.

### Option C — later third specification or test document

**EA-CONF — Conformance and Validation Profiles**

This should be considered only after CORE and EHD semantics are stable. It could contain:

- Interface Conformance Record (ICR);
- positive, boundary and rejection fixtures;
- EA-ITP-01-derived interoperability tests;
- profile/version pinning;
- trace and evidence requirements; and
- reusable conformance report structure.

For now, conformance material can remain an annex of an integrated specification or of EA-EHD.

### Split decision rule

Do not split merely because the corpus has many files. Split only if at least one of the following becomes true:

1. different Working Group/editorial ownership is required;
2. EHD has a stable reuse boundary outside EA;
3. normative maturity differs materially between core architecture and external profiles;
4. the integrated document becomes too difficult to review or version coherently; or
5. FG-TIDA explicitly chooses separate deliverables.

## 6. Source-to-specification map

The following table is the primary editorial bridge. A future specification should derive text from these sources rather than reconstructing the architecture from memory or from individual GitHub comments.

| Candidate specification section | Primary canonical source | Secondary/supporting source | Proposed treatment |
|---|---|---|---|
| Purpose / problem statement | `01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md` | canonical README | Normative context / informative rationale |
| Scope and decision boundary | `00_CANONICAL_REQUIREMENTS...` §1.1 | 00 topology | Stable candidate |
| Terminology and topology | `00_CANONICAL_ARCHITECTURE_TOPOLOGY.md` | 01 dictionary, 02 principles | Stable candidate definitions |
| Failure model | 00 requirements + topology | 00E / 00F | Normative distinction; scenarios informative |
| Solution challenges S1–S14 | `00_CANONICAL_REQUIREMENTS...` | DAOS Annex III | Candidate requirements with ownership classification |
| Sufficiently-good conditions T1–T4 | `00_CANONICAL_REQUIREMENTS...` | EWS lineage | Strong candidate requirements; wording requires standards review |
| Research hypotheses H1–H6 | `00_CANONICAL_REQUIREMENTS...` / 01 | 00D | Informative/research only; not automatic normative requirements |
| KPI/falsification protocol | `00_CANONICAL_REQUIREMENTS...` | 00D / 00D-A01 | Conformance/validation support, not core semantics |
| Epistemic safety principles | 02 | 00 requirements | Candidate principles / rationale |
| Functional architecture F1–F9 | 03 | topology | Candidate implementation-neutral functional requirements |
| Operating postures / requalification | 03 | 01E / UC-EA-01 | Candidate functional semantics |
| General interfaces | 04 | Appendix A | Candidate interoperability requirements |
| EHD kernel | 04 + EA-ITP-01 | topology | Candidate interoperability core |
| Theme #13 profile | 05 / 05A / EA-ITP-01 | UC #4 R19–R20 | External-owner pending profile |
| Theme #16 profile | 05 / 05A | UC #4 R21; current #16 public discussion | External-owner pending profile |
| Authority interface | 05 / 05A | Theme #5 / DAOS | External-owner input; EA must not redefine authority |
| Policy / verdict / attestation profiles | 05 / 05A | #6/#22 public sources | Candidate external profiles |
| Human oversight capacity profile | 05A / UC-EA-03 | Theme #16 | Candidate external profile |
| Interface conformance | 04 Appendix A | 05A | Strong candidate annex or separate conformance section |
| Cross-implementation interoperability | EA-ITP-01 | UC #4 | Candidate test annex; not core requirement by itself |
| DAOS illustrative case | 01E + DAOS package | masterclass | Informative case / traceability source |
| Reference failure scenarios | 00E / 00F | product annexes | Informative scenarios and test design |
| Benchmark / falsification | 00D + A01–A03 | requirements map | Informative evidence/test programme |
| Research lineage | Articles I–V | Three Dimensions, derivation maps | Informative bibliography/background |
| Governance / status / provenance | manifests and provenance records | root claim boundaries | Editorial control, not technical requirements |

## 7. Normative maturity model

Before specification drafting, every statement should receive one of the following labels.

### N1 — Stable candidate normative text

Material is sufficiently central and architecture-owned to be considered for MUST/SHALL-level wording, subject to WG review.

Likely N1 candidates include:

- explicit decision/scope binding;
- preservation of material UNKNOWN/unresolved state;
- no silent scope expansion;
- no silent authority creation;
- source-native result preservation;
- explicit producer/issuer/profile semantics;
- preservation of decision-material provenance/dependency information;
- bounded treatment of capacity and response horizon where material; and
- requalification rather than stale reuse after a material frame change.

### N2 — Candidate normative text requiring editorial normalization

Material is strong but currently expressed as research architecture or quality-plan language.

Likely N2 candidates include:

- T1–T4;
- F1–F9;
- selected S3/S5/S9/S10/S14 requirements;
- core EHD conditional-qualifier rules; and
- Appendix A conformance requirements.

### E — External-owner pending

EA can state what it consumes, preserves or returns, but cannot normatively define the producer’s semantics without review from the relevant owner.

Current examples:

- authority provenance/current applicability (#5);
- human-oversight semantics (#16);
- incident-signal lifecycle semantics (#13);
- conformance verdict semantics (#6);
- attestation appraisal semantics (#22);
- specialised privacy/evaluation outputs (#19/#21);
- enforcement/execution semantics (#10 and other control owners).

### I — Informative

Useful for understanding, implementation guidance or examples but not a conformance requirement.

Examples:

- 00E/00F narrative scenarios;
- product implementation profiles;
- Articles I–V;
- DAOS narrative material;
- market/standards landscape;
- historical derivation notes.

### T — Test/conformance only

Material defines how a requirement may be tested without itself becoming a universal runtime requirement.

Examples:

- EA-ITP-01 fixtures;
- UC-EA-01…04;
- benchmark arms;
- deterministic harness design;
- ICR evidence fields that are test-specific rather than runtime fields.

### H — Historical/provenance only

Material retained to explain evolution and conservation; not a source for new normative wording unless deliberately re-promoted.

## 8. Requirements projection: S1–S14

A future specification should not copy S1–S14 as if EA owns every problem. The following projection keeps ownership explicit.

| ID | Specification disposition |
|---|---|
| **S1 Authority provenance/current applicability** | External-owner interface requirement. EA may require a qualified authority input when material but must not issue the grant. |
| **S2 Preference fidelity** | External-owner interface requirement; informative to EA unless a receiving decision depends on it. |
| **S3 Regime/context/escalation/escape** | Direct EA requalification candidate; authority and enforcement remain external. |
| **S4 Human-inclusive oversight authority/capacity** | Mixed: capacity and information sufficiency are direct EA qualification surfaces; human-oversight lifecycle remains external. |
| **S5 Operational indeterminacy/containment** | Direct EA residual/qualification requirement; containment execution external. |
| **S6 Interoperable privacy-preserving trust determination** | Direct EHD/interoperability surface; identity/privacy authorization external. |
| **S7 Identity/representation link** | External identity input; EA preserves qualification and does not infer identity from behaviour. |
| **S8 Bounded subdelegation/non-amplification** | External delegation semantics; EA preserves inherited limits/unknowns. |
| **S9 Multi-principal composition** | Direct EA composition requirement. |
| **S10 Commitment/material change** | Direct EA frame-requalification requirement. |
| **S11 Policy/objective/preference integrity** | Mixed: producer semantics external; non-substitution and cross-domain composition direct EA concern. |
| **S12 Accountability/challenge/repair** | Historical record ownership external; EA may consume outcome/evidence for requalification. |
| **S13 Authority vs intervention history** | External-owner boundary; EA must not collapse the two histories. |
| **S14 Evidence-to-decision assessment** | Direct EA assessment requirement and candidate common quality layer. |

## 9. T1–T4 projection

T1–T4 are strong candidates for specification-level requirement families because they describe what a sufficiently useful EA-capable solution must preserve without prescribing one implementation.

### T1 — Material awareness within a declared boundary

Candidate normative core:

- declare the receiving decision and scope;
- declare the observation/coverage boundary;
- distinguish material frame break from ordinary variation under declared conditions;
- avoid claiming complete ecosystem visibility.

### T2 — Qualified determination and owner-preserving handoff

Candidate normative core:

- expose a reviewable operating posture/determination state;
- preserve source-native result and owner;
- carry decision-material scope, provenance, freshness, dependency, unresolved state and capacity limits;
- preserve UNKNOWN rather than promote it to PASS/permission;
- identify receiving responsibility and re-entry/requalification conditions.

### T3 — Bounded and authorized response

EA should normatively preserve the distinction between qualification and action. It may carry response constraints and supported posture, but permit/authority and execution remain external.

The Pointwise Non-Inferiority formulation remains a research/strong-profile requirement unless a future WG explicitly adopts it for a defined action class.

### T4 — Timely, viable and minimum-sufficient requalification

Candidate normative core:

- preserve useful response horizon;
- treat evidence, compute, communication and human review as finite;
- expand observation only when decision-relevant;
- avoid unbounded search/review as a default safety mechanism;
- expose when qualification can no longer be achieved within the declared horizon.

## 10. EHD candidate specification boundary

The current EA-ITP-01 test defines a six-element interoperability kernel:

1. producer/profile semantic reference;
2. subject/proposition/decision-domain plus scope;
3. producer/issuer;
4. operational result/closure;
5. determination/state kind;
6. explicit unknown-qualifier declaration for material qualification not established.

Conditional qualifiers remain decision-relative, including:

- freshness/as-of;
- observed-versus-derived status;
- evidence class;
- uncertainty/confidence/assurance semantics;
- capacity;
- provenance;
- dependency/coupling;
- source lineage; and
- window-selection information.

### 10.1 Specification principle

The EHD should be specified as a **semantic handoff**, not necessarily as one mandatory wire format.

A future specification may define:

- required semantic elements;
- profile/version rules;
- rules for material optional qualifiers;
- UNKNOWN handling;
- source-native vocabulary preservation; and
- a mapping/conformance mechanism.

It need not force every implementation into one JSON schema, API or transport.

### 10.2 Theme #13 profile

The current #13 profile maps:

- `closure` → operational result;
- `determinacy_margin` → decision/scope-specific determination qualifier;
- `capacity_binding` → capacity qualifier; and
- `inherited_indeterminacy` → residual/dependency qualifier.

This four-field profile is compatible with the EHD model but is not automatically the universal kernel.

### 10.3 Human-oversight profile

The currently defensible #16-related material supports capacity and information-coverage handoff. A more explicit human-output profile may eventually distinguish:

- human decision/result;
- confidence/assurance that the expected human-review event occurred;
- capacity binding/qualification; and
- residual/inherited indeterminacy.

**Status:** do not promote this four-part human profile to normative EA or FG-TIDA text until the relevant Theme #16 discussion provides sufficient public source confirmation and semantic-owner review. Its architectural value is noted here only as a candidate profile direction.

## 11. FG-TIDA interface maturity register

The following register should be maintained as the public discussions evolve.

| Route | EA needs / preserves | Current disposition |
|---|---|---|
| **#13 → EA** | incident state, provenance/source relation, freshness, affected scope/blast radius, response window, containment reach, unresolved qualifiers | Candidate profile; #13 semantic ownership retained |
| **EA → #13** | decision-scoped systemic assessment, explicit UNKNOWN/residual, capacity/window constraints, supported posture, targeted refinement request | Candidate profile |
| **#16 → EA** | effective human capacity, information coverage, decision/intervention state, execution/reconciliation, material change where available | Candidate profile; human semantics remain #16-owned |
| **EA → #16** | affected scope, residual limitation, capacity binding, targeted requalification relevant to intervention path | Candidate profile; no common schema asserted |
| **#5 → #16/EA** | current authority provenance/applicability | External-owner input |
| **#6/#22 → EA** | scoped verdict/attestation result, reference/version, issuer relationship, limitations, indeterminate/no-assertion | Candidate profile pending owner validation |
| **#1/#10 → EA** | action/outcome record and available response capability where recorded | Not established as common contract |
| **#19/#21 → EA** | minimum-disclosure constraint or scoped specialised evaluation result | Candidate/profile-specific |

### Promotion rule

No route becomes a specification profile merely because it appears in this table. Promotion requires:

1. a public source anchor;
2. semantic-owner confirmation or absence of unresolved objection after the agreed review process;
3. producer and receiver identified;
4. scope and version binding;
5. UNKNOWN/limitation preservation;
6. no ownership leakage; and
7. at least one reviewable positive, boundary and rejection vector.

## 12. Conformance architecture

### 12.1 Candidate conformance unit

The preferred unit is the **named interface/profile route**, not an entire product or organization.

A conformance statement should identify:

- producer implementation/version;
- receiver implementation/version;
- profile/semantic reference;
- adapter version if any;
- declared decision scope and horizon;
- fields emitted/consumed;
- UNKNOWNs and material optional qualifiers;
- applicable fixture set; and
- result.

### 12.2 Interface Conformance Record

Appendix A’s ICR should be considered the primary candidate evidence structure for interface conformance.

The specification should distinguish:

- **semantic conformance:** meaning survives the handoff;
- **scope conformance:** the receiver does not broaden the claim;
- **qualification conformance:** UNKNOWN, capacity, provenance and limitations survive;
- **authority conformance:** receiving an assessment does not create action authority;
- **interoperability conformance:** producer and receiver need not share private internal logic; and
- **burden/horizon viability:** the handoff remains useful within its declared operating conditions.

### 12.3 Test artefacts

EA-ITP-01 provides a strong candidate starting set:

- clean handoff;
- explicit UNKNOWN;
- source-native verdict;
- shared-lineage condition;
- #13 determinacy-envelope profile;
- richer-than-kernel handoff;
- unfamiliar optional field;
- reciprocal EA output.

These should remain **test vectors**, not mandatory runtime scenarios.

## 13. Use cases and examples

### 13.1 DAOS

DAOS should remain the principal extensible source case for authority/context-change and cross-theme composition because it already provides:

- parent case facts;
- minimal mobility instantiation;
- controlled extensibility;
- challenge taxonomy;
- FG-TIDA ToR mapping; and
- interface/test mappings through 01E.

In a specification, DAOS should be an **informative worked example or annex**, not a hidden source of universal requirements.

### 13.2 UC-EA-01…04

These remain architecture-validation profiles:

1. action-time operating-frame requalification;
2. bounded determination under incomplete evidence;
3. effective human oversight under bounded capacity;
4. scope-indexed composition.

Do not submit or reproduce them automatically as four FG-TIDA use cases.

### 13.3 UC #4

FG-TIDA Use Case #4 is valuable because it provides:

- an independently maintained external testbed context;
- explicit Theme #13 / EA separation;
- determinacy-envelope requirement R20;
- #13/#16 bidirectional capacity relation R21;
- versioned-adapter/test-vector discipline; and
- progressive implementation stages.

A future specification may reference UC #4 as a conformance/test context without making its testbed architecture normative.

### 13.4 00E / 00F

These are reference failure scenarios useful for explanatory and test design:

- 00E: enterprise information compounding / many-to-one loss;
- 00F: smart-city locally plausible but systemically incompatible postures.

They should remain informative unless a specific test profile explicitly imports their fixture facts.

## 14. Standards and duplication review

A future specification will require a concise, maintained standards-landscape section. The corpus already contains relevant material across:

- ITU-T FG-TIDA Themes and ToR;
- ITU-T FG-AI4SSC work;
- IETF RATS/EAT/AR4SI and related identity/workload efforts;
- policy/enforcement work such as XACML/OpenC2 where relevant;
- STIX/TAXII incident exchange;
- NIST AI RMF and related trust/risk controls;
- OpenTelemetry/agent observability;
- A2A and other agent-interoperability substrates;
- provenance/context/uncertainty research; and
- relevant ISO/IEC and IEEE human-oversight/autonomous-system standards.

The future specification should state the gap narrowly:

> existing work can provide identity, attestation, policy, provenance, observability, incident signalling, transport, uncertainty estimates or local control; EA addresses the decision-scoped composition and preservation of what those independently governed outputs establish, what remains unresolved, and when the receiving operating frame requires targeted requalification.

This gap statement must be kept evidence-based and updated before formal WG submission.

## 15. Security, privacy and governance considerations

A specification draft should include a dedicated section covering at least:

- false attribution and spoofed producer identity;
- stale/replayed handoffs;
- correlated sources misread as independent evidence;
- Sybil/collusion/reputation poisoning where signalling is used;
- qualifier flooding and defensive UNKNOWN as denial-of-service mechanisms;
- privacy/disclosure burden of provenance and context;
- cross-domain scope leakage;
- authority leakage from assessment to action;
- automated over-trust in human-channel outputs;
- adapter semantic laundering;
- malicious or accidental profile/version mismatch;
- response-window exhaustion through excessive requalification; and
- auditability without requiring full internal-reasoning disclosure.

The normative rule should remain proportional: the specification should require preservation of decision-material qualification, not universal disclosure.

## 16. Candidate document outline

If EA proceeds initially as one integrated specification, the following outline is specification-ready:

1. **Introduction**
   - motivation
   - problem statement
   - intended audience
2. **Scope**
   - covered problem
   - non-goals
   - ownership boundaries
3. **Conventions and terminology**
   - decision domain / scope
   - U, R_U, W(d,t)
   - determination / UNKNOWN / residual
   - producer / receiver / semantic owner
4. **Architectural requirements**
   - selected S1–S14 projection
   - T1–T4
5. **Functional architecture**
   - F1–F9
   - qualification/requalification loops
   - postures and response horizon
6. **Epistemic Handoff Descriptor**
   - kernel
   - conditional qualifiers
   - source-native semantics
   - profile/version rules
7. **Interoperability profiles**
   - #13
   - #16
   - authority
   - policy/verdict/attestation
   - specialised profiles
8. **Security, privacy and governance considerations**
9. **Conformance**
   - ICR
   - semantic/scope/qualification/authority/interoperability checks
10. **Illustrative use cases**
    - DAOS
    - selected UC #4 routes
    - 00E / 00F
11. **Implementation and deployment considerations**
    - adapters
    - transport neutrality
    - optional schemas/APIs
12. **Standards landscape and non-duplication**
13. **Open issues / future work**
14. **References**
15. **Informative annexes**
    - source-to-spec mapping
    - conformance fixtures
    - research/evidence map

## 17. FG-TIDA template readiness checklist

Before creating a future `wg<N>-...` repository, prepare:

### Front matter

- final document title;
- subtitle;
- abstract;
- keywords;
- foreword;
- version/date;
- Working Group identifier;
- authors/editors and affiliations;
- status/approval wording.

### Repository metadata

- repository name;
- document acronym;
- release/version;
- public Pages configuration;
- contribution/review policy;
- issue labels;
- editor/maintainer permissions.

### Document structure

- approved chapter outline;
- normative/informative marking convention;
- terminology section;
- reference/bibliography method;
- diagram ownership;
- optional OpenAPI/schema location if adopted.

### Governance

- source corpus citation anchor;
- source-to-spec mapping;
- change-control rule;
- external semantic-owner review list;
- unresolved issue register;
- IP/licensing decision;
- claim boundary.

## 18. Open decisions before formal specification creation

The following questions remain deliberately open:

1. **Placement:** does EA remain a peer mechanism within a WG derived from Theme #13, become a separate specification within that WG, or receive another cross-theme placement?
2. **Theme #13 relation:** are incident/signal lifecycle and EA formally peer mechanisms, and how should their editorial ownership be represented?
3. **EHD ownership:** is EHD the general reusable abstraction beyond the #13 profile, and if so which specification owns it?
4. **Document split:** one integrated EA specification or separate CORE/EHD documents?
5. **Normative core:** which S/T/F requirements should use MUST/SHALL language?
6. **Human-review output:** does Theme #16 expose a separate confidence/assurance qualifier in addition to capacity and residual indeterminacy?
7. **Common profiles:** which cross-theme fields have enough public semantic-owner support to enter a specification profile?
8. **Wire format:** should the first specification remain semantic/transport-neutral, or include a reference JSON/OpenAPI schema?
9. **Conformance:** should ICR/testing remain an annex or become a separate test specification?
10. **Authorship/editorship:** who is responsible for the WG document and profile sections?
11. **Licensing/IP:** what publication/reuse terms apply to the specification and test artefacts?
12. **Evidence gate:** what level of executed test evidence is required before moving beyond draft?

## 19. Readiness gates

### Gate A — scope readiness

Pass when:

- the WG/placement question is resolved enough to name the document owner;
- EA scope/non-goals are reviewed;
- relation to #13 and EHD is not contradictory.

### Gate B — source readiness

Pass when:

- every planned section has a canonical source;
- no section relies only on memory or private discussion;
- source revisions are pinned;
- historical/non-canonical material is identified.

### Gate C — semantic-owner readiness

Pass per external profile when:

- source Theme/owner is identified;
- current public semantics are anchored;
- mapping has been reviewed or remains explicitly pending;
- no EA text redefines external authority or lifecycle semantics.

Profiles that fail Gate C remain informative or omitted.

### Gate D — normative conversion readiness

Pass when:

- each requirement is classified N1/N2/E/I/T/H;
- MUST/SHALL wording has an owner and conformance implication;
- hypotheses and examples have not been promoted accidentally;
- scope and exceptions are explicit.

### Gate E — conformance readiness

Pass when:

- each normative interface requirement has a reviewable pass/fail method;
- positive/boundary/rejection fixtures exist where useful;
- UNKNOWN and source-native semantics are testable;
- at least one cross-implementation route can be exercised without shared internal logic.

### Gate F — publication readiness

Pass when:

- front matter is complete;
- editor/authors are agreed;
- licensing/IP is resolved;
- all links/references build;
- HTML/PDF build succeeds;
- status text accurately reflects WG approval state.

## 20. Change-control rule

This preparation annex must not become a shadow specification.

Until a formal FG-TIDA specification repository exists:

1. canonical EA research/architecture changes are made in their owning source documents;
2. this annex is updated only to reflect their specification disposition;
3. external-theme changes are reflected only from public source evidence;
4. a new test result may change evidence/maturity but does not silently rewrite source semantics;
5. a semantic-owner objection moves the affected mapping to **External-owner pending / Not established** until resolved;
6. the router README remains a router and does not absorb specification material;
7. once an official WG specification exists, that repository becomes the editorial source for specification text, while the EA corpus remains the research/evidence source and provenance record.

## 21. Immediate preparation backlog

The following work can proceed now without pre-empting FG-TIDA:

1. maintain this source-to-specification map as the corpus evolves;
2. prepare a compact consolidated glossary from the topology/dictionary;
3. classify S1–S14 and T1–T4 sentence-by-sentence under N1/N2/E/I/T/H;
4. extract the EHD semantic kernel and conditional qualifiers into a specification-style table without changing semantics;
5. maintain the FG-TIDA interface maturity register from 05A;
6. add the current human-review determinacy question only after public #16 source confirmation;
7. prepare one informative DAOS walkthrough and one 00E/00F example suitable for a specification reader;
8. prepare a concise standards/non-duplication matrix;
9. prepare a draft conformance annex from Appendix A + EA-ITP-01;
10. keep all unresolved placement/editorial decisions explicit rather than solving them unilaterally.

## 22. Current determination

EA is **technically ready for specification preparation**, but **not yet institutionally ready for an official FG-TIDA specification repository**.

The corpus already contains the foundation, requirements, architecture, interfaces, candidate conformance model and validation material needed to draft a serious specification. The remaining constraints are primarily:

- Working Group / document placement;
- external semantic-owner confirmation;
- normative versus informative classification;
- document split and editorial ownership; and
- executed conformance evidence.

Accordingly, the correct next state is:

**canonical corpus → this specification-preparation annex → reviewed candidate outline/profile maturity → official WG specification when placement and ownership are resolved.**

It is **not** necessary to create additional theory or duplicate use cases merely to justify specification drafting.
