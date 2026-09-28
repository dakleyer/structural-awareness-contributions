# Ecosystem-level Agent Defense — Charter

> **v0.2 Working Draft — work in progress.** This draft will receive further modifications and contributor review before version 0.2 is considered complete. Publication in this repository does not mean that v0.2 is final, frozen or approved by FG-TIDA.

**Status:** Draft v0.2 — editorial working proposal, 28 September 2026  
**Originating issue:** [Theme #13 — Ecosystem-level Agent Defense](https://github.com/FG-TIDA/themes/issues/13)  
**Proposer(s) / drafter(s):** Ward Duchamps, Thales — originating Theme proposer; Iván Abril Palma — preparation-draft synthesis. Nelson Trasatti and Oleksii Voshchak are attributed contributors through the public sources identified below; attribution does not imply approval of this text. Formal editors, maintainers and any WG roles remain to be agreed.

**First-cycle focus:** Ecosystem Awareness and Incident / Signal Lifecycle, connected by bounded, bidirectional interfaces.

**Institutional status:** preparation material for contributor review; not a submitted Phase 2 Charter, established Working Group, adopted interface or FG-TIDA decision. The working filename retains Theme 13 for traceability; it does not assign an official WG number.

**Baseline:** a successor to the v0.1 candidate text, preserving its D1–D5 deliverable structure and broader Theme #13 boundaries. The v0.1 source is unchanged. Architecture/source review is pinned to repository commit `2db60a1fa4faa5ec08c6754cc676b8f70431c32a` and the public contributions recorded in the companion review dossier.

**Reading rule:** this charter defines work and boundaries. Detailed schemas, transition rules, APIs, test fixtures and conformance criteria belong in the resulting deliverables, not in the charter itself. See [review and compatibility dossier](WG13_v0.2_REVIEW_AND_COMPATIBILITY_2026-09-28.md) for source-level mappings, changes from v0.1 and unresolved review items.

## Summary

Agentic ecosystems increasingly connect independently governed agents, services, humans, evaluators, attesters and infrastructure. Each participant may reach a locally valid result while the combined ecosystem still lacks enough qualified information to support a receiving decision, or while harmful effects propagate across organizational boundaries.

Within the existing Theme #13 scope, this charter candidate would develop two related, independently testable capabilities: **(1) an Incident / Signal Lifecycle** for ecosystem-defense signalling, corroboration, affected-scope/blast-radius refinement, locally authorized response coordination and resolution; and **(2) Ecosystem Awareness**, which asks what independently produced results collectively establish for a specific decision, what remains unresolved or inherited through dependencies, and when targeted requalification is needed. The work would connect them through bounded, source-preserving interfaces without creating a central controller or new authority. **Defense is the first concrete implementation context, not a requirement that the reusable qualification/handoff semantics be defense-exclusive.**

The originating Theme #13 is broader than these first two deliverables. Its ecosystem-defense problem space also includes identity/accountability, detection/monitoring, reputation, privacy-preserving operation and incentives/alignment. This charter does **not** silently delete those surfaces. It stages them: the first cycle concentrates on the lifecycle + EA foundation, while the broader Theme capabilities are consumed from adjacent work, retained as later profile/deliverable candidates, or separately scoped if FG-TIDA decides that another Theme/WG should own them.

The originating issue asks whether #13 is too large for one theme and should be split. This charter proposes staging the work, with the Lifecycle and EA foundation first, without prejudging a later FG-TIDA decision to split or redistribute the broader scope. Ward's [public placement and interoperability comment](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5571476256) supports EA within #13 and independent definition and testing of the determinacy envelope and signal lifecycle; it does not constitute approval of this v0.2 text.

## Scope

The first cycle has two independently testable mechanisms, **EA** and **Incident / Signal Lifecycle**. Oleksii's matrix contribution is decomposed into EA-facing qualification and a bounded operational-contextualization function. This is a working functional boundary, not a requirement for a third deployed layer, a new awareness system or an approved FG-TIDA organizational structure.

The work supports participant-local assessment across heterogeneous, independently governed systems. It does not assume a shared objective, common global state, mandatory broadcast, common trust root or central controller. Source-owned determinations remain attributed inputs, not facts that another component silently recreates.

### 1. Incident / Signal Lifecycle

In scope:

- signal birth and minimum semantics;
- issuer/source, provenance and freshness;
- distribution across independently governed participants;
- corroboration, contestation, amendment and supersession;
- observed versus inferred affected scope;
- operational blast-radius/dependency representation;
- response-window information;
- available containment/recovery reach;
- coordination of **locally authorized** graduated response;
- resolution records and lifecycle closure; and
- preservation of material unresolved qualifiers through the lifecycle.

The lifecycle follows the working sequence proposed by Ward: **birth → distribution → amendment/corroboration → containment → resolution**. Containment here includes coordination and recording of locally authorized graduated responses, not conferral of permission on another participant. Each stage should preserve source history, distinguish observations from inferences, and record effective reach, limits and outcome evidence where material. A resolution record closes the incident under its declared criteria; it does not automatically restore every dependent decision's qualification.

Lifecycle-owned affected-scope and blast-radius information can be consumed by EA and by a participant's existing dependency/cartography mechanism. This does not merge their graphs, transfer ownership of a persistent ecosystem map, or require complete ecosystem visibility.

### 2. Ecosystem Awareness

In scope:

- decision-scoped qualification of local and external states;
- explicit observation/representation boundaries;
- source dependence and independent-corroboration assessment;
- residual and inherited indeterminacy;
- finite evidence, compute, communication and human-review capacity;
- semantic / qualification validity;
- response-window constraints;
- distinguishing “more can still be known” from “more knowledge would still be useful for this decision”;
- targeted requalification / re-entry;
- local closure versus system-level support; and
- attempted execution versus externally confirmed outcome where that distinction is material and observable.

EA qualifies a receiving participant's decision under a declared scope and time. A qualified local closure does not establish a complete ecosystem state. In the reference EA architecture, **A** denotes situated assertion/scope; **B**, confidence/support within that frame; **C**, recognized additional knowledge obtainable with current capabilities; and **D**, structural/residual unknown. These are components of one qualified position, not mutually exclusive quadrants, mandatory transmission fields or the four-field Theme #13 envelope.

The EA-facing part of Oleksii's contribution develops semantic-window qualification, residual indeterminacy, bounded epistemic opportunity and dependency/provenance qualification. It consumes current authority-applicability and oversight-capacity determinations from their respective owners. It does not calculate institutional authority, decide grant standing or certify oversight capacity.

Confidence within a represented boundary does not close the open residual beyond it. A stronger result in one domain can qualify another only through an explicit, supported material dependency; absent coupling is neither proven independence nor permission to compensate across domains. More evidence, agents or controls are not assumed to improve determination when they also add correlation, latency, conflict or capacity burden.

#### 2.1 Bounded operational contextualization

The complementary function relates the qualified state to the particular decision: action criticality, exposure, severity, reversibility, affected dependencies, supplied capacity constraints, response timing and explicit contextual thresholds. It produces a structured operational state for legitimate decision owners and, where relevant, Lifecycle.

This function is **decision support, not an intervention decision engine**. A threshold crossing, request for corroboration, investigation or escalation is not permission to act. Derived relations require declared semantics, inputs and units; otherwise the dimensions remain separate. Risk appetite, consequence values, normative preferences and budgets must come from the identified policy/mission owner or a declared test fixture.

Two temporal dimensions remain independent:

- **Qualification validity:** whether the evidence, semantic frame and received authority-applicability determination still apply to this decision.
- **Response opportunity:** whether further evidence or an authorized response can still materially affect the outcome.

One may expire while the other remains open. Missing timing is not inferred from message order, synthetic fixture spacing or an unchanged grant identifier. Available epistemic capacity, response capacity and received institutional oversight capacity likewise retain their distinct meanings and owners.

Further epistemic effort is useful only under the stated decision relevance, capacity, cost and time constraints. Stopping an evidence search does not erase residual uncertainty or authorize execution. Conversely, UNKNOWN is not an automatic ecosystem-wide veto: the affected scope, materiality, legitimate decision rule, fallback and review condition must remain explicit.

#### 2.2 Bidirectional interaction and targeted revalidation

| Direction | Bounded content | Responsibility retained |
|---|---|---|
| Lifecycle → EA | Incident state, observed/inferred affected scope, provenance and corroboration lineage, freshness, response reach/window and unresolved qualifiers | Lifecycle owns incident evolution; EA qualifies reliance for the receiving decision |
| EA → contextualization / decision owner | Qualified state, scope, residual, validity, capacity dependencies and bounded epistemic opportunity | Contextualization preserves distinctions; the legitimate owner selects permitted action |
| EA / contextualization → Lifecycle | Decision-relevant qualification and operational significance, targeted evidence or dependency-branch refinement requests, review conditions | A request is neither a containment command nor an authority grant |
| Lifecycle / execution owner → EA | Amendment, correction, resolution, attempted action and separately evidenced outcome | Material change triggers targeted requalification; resolution alone is not proof of restored applicability |

Revalidation should follow a material change in evidence, scope, context, dependency, authority applicability, capacity, outcome or a declared validity condition. A scheduled validity review can also trigger it when the declared profile requires that review. Reprocessing an unchanged state merely because it crossed a component boundary is not a required feedback cycle. The target and reason for re-entry, version, owner and stopping condition should be recorded.

#### 2.3 Compatibility with Ecosystem Positioning

The contributor reference architecture provides a coherent composition context without becoming a mandatory implementation:

- EA retains decision-scoped qualification and Semantic Window management.
- Regime Awareness can supply a qualified frame-change finding; EA does not replace the source mechanism.
- MSCA retains control-sufficiency assessment; its Composition and Control function maintains participant-local Ecosystem Cartography.
- MSCA Operation and Repositioning retains its explicit posture and role/contract transition logic. The objective-conditioned Gradient ranks candidate transitions; neither that ranking nor contextualization grants permission.
- ACC/participation rules, objectives, policies, identity and authority remain with their legitimate semantic owners.
- Lifecycle retains signal/incident operation and response coordination. Actual enforcement, containment, isolation or recovery is performed only by an authorized control owner.

The charter therefore commissions compatibility and bounded profiles, **not adoption of the entire Ecosystem Positioning, Regime Awareness, MSCA, ACC or Gradient corpus**. Equivalent independently implemented mechanisms are eligible when they preserve the agreed semantic boundaries. The precise matrix-to-F1–F9 assignment remains a reviewable hypothesis; no F10 or new universal interface family is introduced.

### 3. Interoperable handoff

The work may define a lightweight, implementation-neutral handoff/profile allowing different components to exchange enough decision-relevant qualification without revealing complete internal reasoning.

Candidate semantics include:

- producer/profile reference and version;
- subject/proposition/decision scope;
- issuer/source;
- source-native result or closure;
- determination/qualification state;
- explicit UNKNOWN / unresolved qualification; and
- conditional qualifiers such as freshness, assurance semantics, capacity, provenance, dependency/source lineage, validity/review conditions and targeted re-entry references.

The handoff remains partial by construction: missing qualification is represented rather than invented.

The reference **Epistemic Handoff Descriptor (EHD)** is a transport-neutral semantic contract, not a compulsory protocol or central message bus. Its six-element interoperability kernel is: profile/reference and version; subject/proposition/decision scope; issuer; native result/closure; determination state; and an explicit declaration of material unknown qualifiers. Conditional fields are carried when omission would materially change reliance. A stable producer profile plus a small per-decision delta may avoid repeating full context and history.

The existing #13 envelope — `closure`, `determinacy_margin`, `capacity_binding`, `inherited_indeterminacy` — is a **candidate versioned #13 profile**, preserving UC #4 Requirement 20. It is not a replacement for the general kernel, not the A/B/C/D tuple and not a requirement that other Themes translate their native outputs into #13 states. Broader EHD standardization and ownership remain open.

A bounded adapter preserves native meaning and explicit distinctions between UNKNOWN, NOT DECLARED, NOT ESTABLISHED, NOT APPLICABLE and a test's NOT EXERCISED status. A receiver's additional qualification remains receiver-authored. Forwarding or aggregation does not create independent corroboration, and a valid signature or schema does not prove the truth of the asserted qualifier.

Composition-critical extensions may reference the same decision, its basis/version, commitment state, material dependencies, authority/precedence and targeted re-entry. They remain conditional; no full private reasoning, global database or universal scalar is required.

### 4. Cross-Theme interfaces

The work may consume or return bounded state to adjacent Theme-owned functions without redefining them. Initial interface families include:

- identity / representation / principal binding;
- authority / delegation / current applicability / privilege lifecycle;
- policy / intent / runtime conformance;
- verifier-side evidence and attestation;
- human-oversight authority, capacity and decision state;
- accountability / action / execution records;
- enforcement / containment / recovery;
- privacy / minimum disclosure; and
- evaluation or other specialized profiles where a concrete case requires them.

Theme-specific profiles should become normative only after review by the relevant semantic owners and the applicable FG-TIDA process.

The reference mapping maintains three separate levels: **04 general interfaces → 05 ideal FG-TIDA projection → 05A current-state bridge**, including their explicitly versioned deltas. 04 semantics are not redefined by this charter; 05 expresses a proposed target, not present agreement; 05A records what public sources support at a stated date. Later contributions require an explicit dated review record, not silent alteration of frozen baselines.

Each proposed interface should identify its producer, consumer, semantic owner, native meaning, version, material inputs/outputs, unavailable-state handling, authority boundary, review status and test evidence. Transport/API/schema choices are deliverable-level decisions. Reusing a transport or schema does not transfer ownership of the source determination.

### 5. Testing and conformance

The work may define:

- positive, boundary and rejection fixtures;
- version-pinned adapters/profiles;
- source-native expected outcomes or accepted oracles;
- interface conformance records;
- cross-implementation interoperability tests;
- UNKNOWN / not-established handling;
- qualification/provenance/dependency preservation checks;
- decision/execution reconstruction; and
- bounded testbeds that do not absorb adjacent Theme semantics.

At least one early profile should test the **EA-specific differential rather than only interface compatibility**: hold the relevant local/native result constant while changing a decision-material ecosystem qualifier such as source independence, inherited indeterminacy, semantic validity or available response capacity, and verify that the systemic qualification changes only when that qualifier materially changes the receiving decision. A paired nominal-continuity control should verify that EA does not create unnecessary HOLD, escalation or containment when nothing material changed.

### 6. Broader Theme #13 defense surfaces

The originating Theme also raises ecosystem-level capabilities around:

- verifiable identity/accountability and privacy-preserving principal linkage;
- remote or behavioural detection/fingerprinting where the agent does not cooperate;
- reputation and concern-signalling across parties;
- standardized event logging / observability;
- mechanisms for incentives/alignment among otherwise independently governed agents; and
- decentralization constraints intended to avoid one controlling operator or surveillance architecture.

These remain part of the **Theme #13 problem space**, but they are not automatically first-cycle normative deliverables of this charter.

The initial lifecycle/EA work should therefore:

1. define interfaces capable of consuming such outputs where they are source-owned and available;
2. avoid duplicating identity, attestation, enforcement, reputation or incentive mechanisms already owned elsewhere;
3. keep privacy/selective-disclosure and decentralization as design constraints from the start; and
4. allow later admission of a reputation, incentive, detection or identity profile only after duplication/ownership review and a concrete use case demonstrates the need.

This preserves the breadth of Theme #13 without making the first charter cycle unreviewably large.

## Out of Scope

Unless FG-TIDA later changes the charter, this work would not:

- create legal, institutional, policy, privilege or containment authority;
- define the origination of authority/delegation grants;
- replace identity, attestation, policy, access-control or privilege-lifecycle standards;
- determine legal personhood or universal liability;
- define one universal trust/reputation score;
- require a central ecosystem controller or shared private reasoning model;
- require disclosure of complete prompts, internal reasoning, objectives or private state;
- define the complete human-oversight, policy/conformance, model-level or embodied-system lifecycle owned elsewhere;
- define a universal identity-binding scheme, reputation algorithm, incentive/economic mechanism, remote-fingerprinting method or kill-switch enforcement mechanism in the first cycle unless FG-TIDA explicitly assigns that work here after duplication/ownership review;
- treat an assessment, confidence value, reputation value, human approval or signal as authority;
- turn test vocabulary into mandatory runtime ontology;
- force heterogeneous evidence/risk/capacity dimensions into one universal scalar;
- require maximum context or telemetry collection;
- certify products; or
- convert research hypotheses or illustrative scenarios into normative requirements without separate review;
- replace a semantic owner's native determination with a mapping annotation or a simulated oracle;
- equate static fixture correspondence with live component interoperability, copied outcome labels with enforced behavior, or symbolic tests with empirical ecosystem validation; or
- incorporate all of Ecosystem Positioning as compulsory first-cycle WG scope.

## Objectives / Deliverables

The exact deliverable packaging remains subject to FG-TIDA review.

### D1 — Common terminology and architectural boundary

Define the minimum shared terminology needed to keep local results, systemic qualification, authority, uncertainty, affected scope, validity and response timing distinct. Include a responsibility map for EA, bounded operational contextualization, Lifecycle and external authority/control owners; reconcile terminology with the contributor architecture without assigning its entire corpus to Theme #13.

### D2 — Incident / Signal Lifecycle

Candidate content:

- lifecycle states and transitions;
- minimum signal semantics;
- provenance/freshness;
- corroboration/contestation/amendment;
- affected-scope / blast-radius semantics;
- response-window properties;
- locally authorized response coordination;
- resolution; and
- privacy/adversarial considerations.

D2 remains a complete operational mechanism.

### D3 — Ecosystem Awareness Core

Candidate content:

- decision-scoped systemic qualification;
- bounded observation/representation;
- residual/inherited indeterminacy;
- source dependence / independent corroboration;
- finite determination resources;
- semantic/qualification validity;
- epistemic opportunity;
- targeted requalification;
- output validity/limitations; and
- no-supercontroller / no-authority-creation rules.

D3 remains independently testable from D2. It incorporates Oleksii's EA-facing qualification work and identifies the bounded contextualization interface separately. Document native inputs, explicitly derived relations, contextual thresholds and multidimensional outputs, with separate validity and response dimensions. The deliverable must make it possible to test each function without implementing the other contributor's internal logic.

### D4 — Interoperability / Epistemic Handoff Profiles

Candidate content:

- a minimal handoff kernel;
- conditional qualifiers;
- source-native result preservation;
- profile/version rules;
- UNKNOWN/not-established handling;
- bounded adapters;
- composition-critical extensions where needed; and
- Theme/domain-specific profiles.

### D5 — Conformance / Reference Test Profiles

Candidate content:

- interface conformance records;
- positive/boundary/rejection fixtures;
- cross-implementation tests;
- version-pinned adapters;
- trace/evidence requirements;
- reproducible result packages; and
- UC #4 / interoperability / decision-boundary vectors where they test an agreed requirement.

D5 may initially remain an informative/test package rather than a standalone specification. Each campaign declares the question, semantic owners, capabilities, admitted profile, source versions, resource budget, expected observations, falsifiers, review states and stopping point. Nelson's proposed experimental cycle—reference execution, follow-up hypothesis, controlled variation, counter-test and report—is included as a proposed contribution, not an unlimited maintenance commitment.

For routes claiming compatibility with the reference 04 interface-conformance method, retain an Interface Conformance Record: freeze material qualifiers and the ordered route, identify aggregation points and semantic/adapter owners, appoint a mapping reviewer distinct from its adapter maintainer, and record objections. An unresolved material objection blocks an interface-sufficiency conclusion. Label self-declared materiality and simulated independence explicitly. Test at the handoff/aggregation boundaries as well as end to end; a declaration by the producer is not independent evidence of its truth. These are test-review conditions, not new runtime EHD fields or certification requirements.

Version the charter, EHD semantics, profile, adapter, source and fixture independently. Changes to field meaning require an explicit compatibility assessment and, when breaking, a new profile/adapter version; prior results retain the exact versions tested. Unknown extensions must not be silently reinterpreted as established qualification.

The first D5 package should include:

- a nominal-continuity control;
- a local-equivalence / systemic-divergence pair;
- a source-dependence / false-corroboration boundary;
- a targeted-requalification branch;
- an independent producer/consumer interoperability route where feasible; and
- explicit falsifiers.

Where a comparative EA claim is made, a **strong native/control configuration should be allowed to reproduce the same behaviour**. If it does so at equal or lower burden, that result counts against an EA differential claim.

A two-domain or deterministic pass establishes only the bounded property actually tested. It must not be reported as proof of ecosystem behaviour. Stronger ecosystem-level evidence requires later composition across multiple independently governed participants/observers with partial, conflicting or source-dependent observations.

### Delivery sequence and acceptance evidence

| Stage | Intended output | Evidence gate and limit |
|---|---|---|
| Reference semantic review | UC #6 facts and four A/B before/after-approval conditions, mapped through the relevant #13/#16 contributions | Source-owner review of meanings, aliases and proposed synthetic metadata; not a new authority calculation |
| Frozen bounded mapping | Versioned adapter, declared capability/schema, sources, expected values and open-field register | Technical checks, preparer review, contributor review and admission recorded separately |
| Behavioral reference execution | Explicitly implemented transition/action simulator or independently implemented route, with traces and observed outcomes | Copying `revalidation_required` or `must_not_proceed_under_g1` is not evidence of revalidation or prevention |
| EA differential campaign | Independent versus shared-lineage corroboration; useful evidence obtainable versus too late/costly; nominal continuity control | Separate agreed protocol and fixed cost/consequence assumptions; strong native baseline can falsify the claimed benefit |
| Federated extension | UC #4 Stage 0/1 route and, subsequently, separately admitted multi-participant campaigns | Early passes support only their declared scope; later stages require explicit resources and contributor agreement |

The **28 September reference package** is Nelson's `UC4_UC6_Theme13_Mapping_Review_v0.4.0-r1.zip`, using experiment schema 1.1.0. It is a review artifact, not Charter v0.2 or an implementation of EA. The earlier input package v1.1.1 used schema 1.0.0; those versions are different dimensions and must not be relabeled or migrated implicitly. The source worked example's v0.2 title versus v0.3 internal references remains a contributor-review issue.

UC #6 remains unchanged: the same G1 exists in both branches; only the declared purpose changes applicability; human approval under H1 does not expand G1. The fixture's before/after timestamps are synthetic ordering choices, not measured latency or a response window. The wider corroboration/cost investigation remains a separate experiment. Imported source revisions create no automatic obligation for the testbed maintainer to reimplement independently owned mechanisms.

Before freezing the paired #16 mapping, retain Olena's public review clarifications: a general H1 review repertoire is not the branch-specific permitted intervention set; array order is not a semantic ranking; the recorded approval in B has no authorizing effect under G1; and `subject_to_other_controls` is not the complete return-to-operation condition. Attribute UC #6 facts, HO-EDM semantics, institutional authority/capacity semantics and adapter encodings separately to their respective contributors. Source: https://github.com/FG-TIDA/themes/issues/16#issuecomment-5872506565

D1–D5 are proposed work outputs, not five mandatory repositories or already commissioned ITU deliverables. Their form as reports, specifications or informative test packages, editors, schedule, licensing and release gates require agreement. The charter may be reviewed before behavioral testing is complete; stronger technical claims must wait for the corresponding evidence.

## Related Work

The work should coordinate with, rather than reproduce, relevant standards and practices, including where applicable:

- FG-TIDA Themes and Use Cases, especially originating Theme #13 and UC #4;
- the 2026 Singapore Consensus on Global AI Safety Research Priorities and its Agentic Risk Management companion work referenced by Theme #13;
- AI-agent observability work, including OpenTelemetry agent-observability practice;
- decentralized identifier/naming work relevant to meaningful and verifiable agent identifiers, including the IETF DINRG material cited in Theme #13;
- IETF RATS/EAT/AR4SI and related identity/workload assurance work;
- STIX/TAXII and incident-exchange practice;
- policy/enforcement mechanisms such as XACML/OpenC2 where relevant;
- NIST AI RMF and related AI assurance/TEVV work;
- provenance and distributed-observability work;
- agent-interoperability substrates such as A2A; and
- relevant ISO/IEC, IEEE and privacy/security standards.

A formal duplication review should be maintained before any specification is proposed for stronger status. Related standards above are coordination candidates, not claimed implemented integrations.

The public FG-TIDA Terms of Reference provide the institutional fit: terminology (3.1), use-case/requirements analysis (4.1), architecture and interoperability (4.2), trust/lifecycle management (4.3), machine-readable metadata (4.4) and evaluation guidance (4.5). The incident/signal lifecycle is one bounded contribution to that remit, not the whole trust lifecycle. This scope alignment does not establish approval, novelty or absence of duplication.

Process sources: [FG-TIDA charter template](https://github.com/FG-TIDA/themes/blob/main/CHARTER-TEMPLATE.md), [Theme development process](https://github.com/FG-TIDA/themes/blob/main/README.md) and [Terms of Reference](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx). A charter is proposed by Pull Request after theme discussion; organizational structuring and deliverable approval remain governed by FG-TIDA.

## Related Themes

The initial **working boundaries** are strongest for:

- **Theme #13 — Ecosystem-level Agent Defense:** originating Theme and owner of the broader ecosystem-defense problem space; the first-cycle charter focuses its lifecycle/EA foundation without deleting the remaining identity, detection, reputation, privacy and incentive questions.
- **Theme #5 — Provenance of Authority:** grant origin, scope, limits, standing/revocation/current applicability.
- **Theme #16 — Operational Human Oversight:** human authority/capacity/decision/execution/re-entry state.
- **Theme #6 — Intent / Policy Runtime Conformance:** source-native conformance/verdict semantics are public; the specific #6→EA adapter remains a candidate profile.

The following boundaries are also explicitly carried from the originating issue and remain subject to alignment with the respective Themes:

- **[Theme #10 — Network-Native Governance and Trust Enforcement for Agentic AI](https://github.com/FG-TIDA/themes/issues/10):** the network/infrastructure governance and enforcement plane. This charter exchanges qualified signals and consumes enforcement outcomes; it does not define network-level enforcement or grant authority to that plane.
- **[Theme #12 — Agent Trust Mechanics](https://github.com/FG-TIDA/themes/issues/12):** trust mechanisms inside the agent, including credential handling, memory/context assurance and confidential computing. This charter addresses cross-party ecosystem qualification and defence; it does not redefine those internal mechanisms.
- **[Theme #14 — Agent-to-Principal Legal Binding](https://github.com/FG-TIDA/themes/issues/14):** a dependency for principal linkage and mandate/responsibility information. This charter consumes source-owned binding information through privacy-preserving, contestable interfaces; it does not establish legal binding or principal authority.

Useful **candidate supporting profiles** include:

- **Theme #7 — Verifier-side requirements:** evidence appraisal/failure semantics and negative vectors.
- **Theme #22 — Remote Attestation:** attested runtime/model/policy/interaction evidence where relevant; a common #22→EA profile is not yet established.

Other Themes may become profiles when a concrete use case requires them. The charter should not turn the complete ideal map into first-cycle scope.

The #5 boundary is particularly important: grant origination/provenance and current applicability are consumed, never inferred from a credential, a human approval or an EA qualification. #16 retains oversight semantics, effective institutional capacity, human decisions and their distinction from execution. #6 retains native conformance verdicts. #7/#22 evidence remains an attributed input, not a substitute for authority or systemic sufficiency.

Optional references to records/accountability (#1), operating-regime findings (#18), lifecycle privacy (#19) or privilege lifecycle (#23) require a concrete admitted profile and semantic-owner review. Mentioning them does not add those Themes' complete work to the first cycle.

## Open Questions

Reviewers are invited to focus on questions that remain genuinely unresolved.

### Architecture / packaging

1. **Institutional packaging:** one Theme #13-derived WG with separate peer deliverables/specifications, another document structure, or another FG-TIDA arrangement?
2. **Interoperability profile ownership:** should the general handoff abstraction become a reusable specification/profile beyond the #13 envelope, and who maintains it?
3. **Document split:** should Ecosystem Awareness Core and interoperability profiles be one document or separate deliverables?
4. **Profile admission:** which cross-Theme mappings have enough semantic-owner support to become normative rather than candidate/informative?
5. **Wire format:** should the first work remain semantic/transport-neutral or later include a reference schema?
6. **Conformance packaging:** informative annex/profile or separate test document?
7. **Evidence gate:** what executed evidence is needed before moving beyond early draft status?
8. **Editorial ownership:** who is prepared to edit/maintain each deliverable?
9. **Licensing/IP:** what terms should apply to specifications, fixtures and reference implementations?

### Theme #13 defense questions preserved from the originating Issue

10. **Privacy / surveillance boundary:** what minimum signal/provenance state is needed for meaningful blast-radius reduction without creating a surveillance architecture or unnecessary principal disclosure?
11. **Coordination versus authority:** how should the architecture make it impossible to confuse shared defensive coordination, reputation or corroboration with authority to constrain another participant?
12. **Containment authority:** who may authorize high-impact containment/kill-switch actions, on what evidence, and how is that authority itself bounded, contestable and auditable?
13. **Reputation / assurance:** what role, if any, should reputation play, how should source dependence/collusion be handled, and should reputation remain a separate Theme/profile rather than a lifecycle field?
14. **Detection without cooperation:** which behavioural/fingerprinting/detection outputs are legitimate ecosystem-defense inputs, and which mechanisms belong outside this charter?
15. **Incentives / alignment:** should incentives for trustworthy/cooperative behaviour remain a later Theme #13 deliverable, be consumed from another workstream, or be split out?
16. **Operator/decentralization model:** who operates shared infrastructure and what prevents the operator, trust anchor or dominant reporter from becoming a single point of control or failure?
17. **Agent privacy:** what privacy interests, if any, should be represented for agents themselves, separately from the privacy of principals/users?

### v0.2 decisions requiring focused review

18. **Oleksii decomposition:** confirm the EA-internal versus contextualization split, its independently testable boundary and the provisional F1–F9 mapping; do not appoint the whole matrix as a third serial layer.
19. **Contextualization and EP boundary:** which supplied thresholds/cost relations are material to the first profile, and how are risk appetite, control sufficiency, posture selection and authorization kept with their owners?
20. **Evidence labels:** confirm the source worked-example version and the mapping aliases; distinguish test-calibration success from behavioral execution and independent interoperability.
21. **Revalidation contract:** specify material-change, expiry/review and targeted re-entry conditions, and how unchanged-state circulation and unbounded escalation are prevented.
22. **First differential protocol:** agree the independent/shared-lineage/late-evidence branches, fixed budget and consequence model, strong native comparator, available capabilities and stopping criterion.
23. **Current-state update:** record the 27–28 September contributions as a dated 05A review proposal; reconcile obsolete case-availability statements without rewriting frozen sources or claiming FG adoption.

24. **Alignment with #10 and #12:** how should scope and boundaries be aligned with Network-Native Governance and Trust Enforcement and Agent Trust Mechanics? Carried from the originating issue; the Related Themes descriptions are proposed working boundaries, not agreements on behalf of those Themes.

For this preparation draft, **independent Incident Lifecycle and Ecosystem Awareness mechanisms are the current technical drafting baseline**. The exact wording, broader Theme #13 partitioning and institutional packaging remain reviewable through the FG-TIDA process.


---

## Contributor lineage and review status

The content is an editorial reconciliation for review, not a record of collective approval.

- **Ward Duchamps:** Theme origin, lifecycle framing and independently testable EA/Lifecycle direction. Public anchors: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5508513343 and https://github.com/FG-TIDA/themes/issues/13#issuecomment-5571476256
- **Nelson Trasatti:** UC #4, bounded adapters, complete Lifecycle, targeted refinement, the #13 profile and experimental work. Anchors: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5639226397 and https://github.com/FG-TIDA/use-cases/issues/4#issuecomment-5846988611
- **Oleksii Voshchak:** matrix, worked example and revised decomposition; authority/capacity ownership, two clocks, structured state and event-driven revalidation. Anchors: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5783505043 and https://github.com/FG-TIDA/themes/issues/13#issuecomment-5818049343 and https://github.com/FG-TIDA/themes/issues/13#issuecomment-5854694913
- **Arpita Sarker:** UC #6 source facts and expected authority-applicability outcomes. https://github.com/FG-TIDA/use-cases/issues/6
- **Lei Gao, Olena Pavlenko and Olha Borysenko:** adjacent Theme #16 sequencing and bounded oversight contributions; the dossier records specific source anchors and preserves their ownership. This is not attributed approval of the full v0.2.
- **Iván Abril Palma:** EA/EP reference architecture, composition and interface discipline, v0.1 preparation baseline, synthesis and proposed comparative challenge. https://github.com/dakleyer/structural-awareness-contributions/tree/2db60a1fa4faa5ec08c6754cc676b8f70431c32a/architectural-contributions/ecosystem-positioning

**Next review:** contributor review of the technical boundaries and source interpretations, then Ward/process review of scope and packaging. Publication in a contributor repository, if requested, and submission of an official FG-TIDA Charter PR are separate actions. No message, submission, approval or maintainer appointment is implied by saving this draft.
