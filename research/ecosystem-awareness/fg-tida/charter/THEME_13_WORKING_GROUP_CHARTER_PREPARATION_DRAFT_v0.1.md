# Annex 01G — FG-TIDA Theme #13 Phase 2 Charter Preparation Draft

**Status:** Draft v0.1 — living preparation draft; revised 24 September 2026  
**Originating theme:** [FG-TIDA Theme #13 — Ecosystem-level Agent Defense](https://github.com/FG-TIDA/themes/issues/13)  
**Primary public use case:** [FG-TIDA Use Case #4 — Federated ecosystem defense across independently governed organizations](https://github.com/FG-TIDA/use-cases/issues/4)  
**Institutional status:** preparation material only; not submitted as a Phase 2 Charter; not an established Working Group, deliverable, specification, chair/editor assignment or FG-TIDA decision  
**Versioning rule:** this file remains **v0.1** as the first reviewable preparation baseline. Git history carries successive revisions so previously shared links remain stable. Post-v0.1 contributor review is recorded below as preparation input for a later **v0.2 Working Draft**; recording that input here does **not** silently convert or rewrite the v0.1 candidate Charter text.

**Earlier source:** the [pre-restructuring charter-preparation draft](https://github.com/dakleyer/structural-awareness-contributions/blob/6ad0be7378bcc22d5977549d8d7a6adfb998495b/research/ecosystem-awareness/fg-tida/charter/THEME_13_WORKING_GROUP_CHARTER_PREPARATION_DRAFT_v0.1.md) preserves the longer contributor, sequencing and promotion-gate account. Its earlier wording is historical preparation material, not a later FG-TIDA decision.

> **Purpose.** Prepare a compact, reviewable Phase 2 charter candidate for Theme #13 while preserving the boundaries already emerging in public discussion. The draft is intentionally more mature than an Issue comment and less committal than an official Charter PR.

## v0.1 review status — preparation input for v0.2

**Status of this file:** v0.1 remains the initial reviewable Charter-preparation baseline. The candidate Charter text below is **not being silently rewritten in place** as later comments arrive.

**Purpose of this review record:** capture contributor positions, implementation constraints and unresolved architectural decisions that should be reviewed before a successor **v0.2 Working Draft** is opened. This section is therefore a review envelope around v0.1, not a claim that the listed positions have already been adopted by FG-TIDA.

**Current editorial posture:** preserve attribution and source lineage; distinguish supported working positions from still-open decisions; use v0.1 as the stable reference point; and carry reconciled changes into v0.2 only after review.

### Contributor review record feeding v0.2

| Contributor / source | Contribution or review position now carried forward | What this means for a future v0.2 | Status |
|---|---|---|---|
| **Ward Duchamps — originating Theme #13 proposer** | Proposed the signal lifecycle structure **birth → distribution → amendment/corroboration → containment → resolution**; argued that two domains prove protocol/interchange rather than ecosystem behaviour; placed **Ecosystem Awareness within #13**; supported keeping the determinacy envelope and signal lifecycle independently defined/testable; and framed defense as the first concrete use rather than the envelope's exclusive scope. [Lifecycle/scoping comment](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5508513343) · [EA placement / independent mechanisms](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5571476256) | Preserve Ward's lifecycle as a first-class operational mechanism; preserve the broader Theme #13 problem space; keep the EA↔Lifecycle interface explicit; do not reduce #13 to a transport-only or EA-only design. | **Source position recorded.** Final institutional packaging and exact wording remain subject to Ward / FG review. |
| **Nelson Trasatti — UC #4 / progressive testbed** | Turned the lifecycle into a progressive, executable test path: deterministic/frozen fixtures first, then federated exchange, later multi-domain and adversarial stages. UC #4 keeps adjacent mechanisms independently maintained and uses bounded, versioned integration rather than absorbing their internal logic. [Progressive testbed](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5561245975) · [UC #4 submission](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5598536418) | Use **UC #4 as the executable integration spine**, with Stage 0/1 as the initial bounded commitment and stronger ecosystem claims reserved for later multi-participant stages. | **Supported implementation direction.** |
| **Nelson Trasatti — architecture-boundary review** | Confirmed that the **Incident / Signal Lifecycle remains a complete operational mechanism**, not a transport layer for EA; supported a bounded **targeted-refinement loop** from EA into a specific dependency/blast-radius branch; accepted the four-field #13 envelope as a versioned profile of a more general EHD, consumed through a bounded adapter; and proposed Stage 0/1 checks for explicit `UNKNOWN`, independent upstream lineage and targeted graph refinement. [Boundary review](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5639226397) | v0.2 should make the ownership boundary explicit: Lifecycle owns signal/incident operation; EA owns decision-scoped systemic qualification; adapters preserve source-native semantics; targeted refinement is testable without indiscriminate graph expansion. | **Technically compatible working position.** Nelson explicitly leaves two architecture points for Ward / FG confirmation. |
| **Nelson Trasatti — UC #6 → UC #4 execution sequence** | Supported UC #6 as the small semantic control, then a **bounded, versioned UC #4 executable profile** with mapping, fixtures, traces and an expected-vs-observed report; keeps investigation/corroboration/escalation distinct from authorization to intervene. [Execution sequence](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5802619701) | v0.2 should separate **semantic-source review** from the **executable UC #4 profile**, and should avoid creating extra intermediate artefacts unless they exercise a distinct interface or falsifier. | **Current execution path.** |

### Open points intentionally not resolved inside v0.1

The following remain review questions for the successor draft rather than changes silently imposed on v0.1:

1. whether Incident / Signal Lifecycle and Ecosystem Awareness should be described formally as **two peer mechanisms within Theme #13**, or packaged differently;
2. whether the **EHD** is the appropriate reusable general abstraction beyond the concrete #13 profile;
3. how much of the broader Theme #13 surface — identity/accountability, detection, reputation, incentives and privacy-preserving operation — belongs in the first Charter cycle versus later profiles or adjacent work;
4. which UC #4 fixtures provide the first decisive EA differential test, rather than only interface compatibility; and
5. who will own/editorially maintain each deliverable if a Phase 2 structure is agreed.

> **Successor rule:** a future **v0.2 Working Draft** should reconcile the review record above into explicit architecture boundaries, contributor attribution, UC #4 execution scope and unresolved-decision status. Until that successor exists, this v0.1 file remains the stable preparation reference.

---

## About this preparation draft

### What this is about

Theme #13 addresses ecosystem-level defense across independently governed agentic systems: how participants exchange incident-relevant signals, corroborate them, understand affected scope, coordinate locally authorized response and close or revalidate an incident.

The discussion has also exposed a complementary question: **what do independently produced results actually establish for a particular receiving decision when combined, and what remains unresolved?** This draft uses **Ecosystem Awareness (EA)** for that decision-scoped systemic qualification function.

For drafting purposes, the current architecture treats these as **two independently testable mechanisms with a bounded interface**:

1. **Incident / Signal Lifecycle** — operational ecosystem-defense signalling, affected-scope/blast-radius handling, response coordination and resolution.
2. **Ecosystem Awareness** — decision-scoped qualification of what available states support, what uncertainty/dependence remains, and what requires targeted requalification.

This is the current **drafting baseline**, not a claim that FG-TIDA has formally adopted the phrase “peer mechanisms” or decided the final institutional packaging.

### Minimum reading path

A reviewer can understand this draft without reading the full research corpus.

1. Start with [Theme #13](https://github.com/FG-TIDA/themes/issues/13) and [Use Case #4](https://github.com/FG-TIDA/use-cases/issues/4).
2. For the target cross-Theme architecture, read [05 Ideal Interfaces](../interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md) and the [05 Ideal Delta](../interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md).
3. For what the public FG-TIDA record currently supports, read [05A Current-State Bridge](../interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md) and the [05A Current-State Delta](../interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md).

For deeper architectural provenance only:

- [00 — Canonical Requirements](../../baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) + [Requirements vNext Delta](../../baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md);
- [04 — General Functional Interfaces](../../baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md) + [04 vNext Delta](../../baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md);
- [Annex 01F — Specification Preparation](../specifications/EA_FG_TIDA_SPECIFICATION_PREPARATION_v0.3_DRAFT.md).

**Drafting rule:** **05 provides the destination; 05A controls the current admission/pacing.**

---

# Candidate Phase 2 Charter text

The section below is intentionally close to the structure of the official FG-TIDA [CHARTER-TEMPLATE](https://github.com/FG-TIDA/themes/blob/main/CHARTER-TEMPLATE.md) so that it can later be reviewed or projected into a Pull Request without first rewriting the whole document.

# Ecosystem-level Agent Defense — Charter

**Status:** Draft  
**Originating issue:** [Theme #13 — Ecosystem-level Agent Defense](https://github.com/FG-TIDA/themes/issues/13)  
**Proposer(s) / drafter(s):** Ward Duchamps, Thales — originating Theme proposer; Phase 2 charter drafter(s)/editor(s) to be agreed through the FG-TIDA process

## Summary

Agentic ecosystems increasingly connect independently governed agents, services, humans, evaluators, attesters and infrastructure. Each participant may reach a locally valid result while the combined ecosystem still lacks enough qualified information to support a receiving decision, or while harmful effects propagate across organizational boundaries.

Within the existing Theme #13 scope, this charter candidate would develop two related, independently testable capabilities: **(1) an Incident / Signal Lifecycle** for ecosystem-defense signalling, corroboration, affected-scope/blast-radius refinement, locally authorized response coordination and resolution; and **(2) Ecosystem Awareness**, which asks what independently produced results collectively establish for a specific decision, what remains unresolved or inherited through dependencies, and when targeted requalification is needed. The work would connect them through bounded, source-preserving interfaces without creating a central controller or new authority. **Defense is the first concrete implementation context, not a requirement that the reusable qualification/handoff semantics be defense-exclusive.**

The originating Theme #13 is broader than these first two deliverables. Its ecosystem-defense problem space also includes identity/accountability, detection/monitoring, reputation, privacy-preserving operation and incentives/alignment. This charter does **not** silently delete those surfaces. It stages them: the first cycle concentrates on the lifecycle + EA foundation, while the broader Theme capabilities are consumed from adjacent work, retained as later profile/deliverable candidates, or separately scoped if FG-TIDA decides that another Theme/WG should own them.

## Scope

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

Theme-specific profiles should become normative only after review by the relevant semantic owners.

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
- convert research hypotheses or illustrative scenarios into normative requirements without separate review.

## Objectives / Deliverables

The exact deliverable packaging remains subject to FG-TIDA review.

### D1 — Common terminology and architectural boundary

Define the minimum shared terminology needed to keep local results, systemic qualification, authority, uncertainty, affected scope, validity and response timing distinct.

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

D3 remains independently testable from D2.

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

D5 may initially remain an informative/test package rather than a standalone specification.

The first D5 package should include:

- a nominal-continuity control;
- a local-equivalence / systemic-divergence pair;
- a source-dependence / false-corroboration boundary;
- a targeted-requalification branch;
- an independent producer/consumer interoperability route where feasible; and
- explicit falsifiers.

Where a comparative EA claim is made, a **strong native/control configuration should be allowed to reproduce the same behaviour**. If it does so at equal or lower burden, that result counts against an EA differential claim.

A two-domain or deterministic pass establishes only the bounded property actually tested. It must not be reported as proof of ecosystem behaviour. Stronger ecosystem-level evidence requires later composition across multiple independently governed participants/observers with partial, conflicting or source-dependent observations.

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

A formal duplication review should be maintained before any specification is proposed for stronger status.

## Related Themes

The initial **working boundaries** are strongest for:

- **Theme #13 — Ecosystem-level Agent Defense:** originating Theme and owner of the broader ecosystem-defense problem space; the first-cycle charter focuses its lifecycle/EA foundation without deleting the remaining identity, detection, reputation, privacy and incentive questions.
- **Theme #5 — Provenance of Authority:** grant origin, scope, limits, standing/revocation/current applicability.
- **Theme #16 — Operational Human Oversight:** human authority/capacity/decision/execution/re-entry state.
- **Theme #6 — Intent / Policy Runtime Conformance:** source-native conformance/verdict semantics are public; the specific #6→EA adapter remains a candidate profile.

Useful **candidate supporting profiles** include:

- **Theme #7 — Verifier-side requirements:** evidence appraisal/failure semantics and negative vectors.
- **Theme #22 — Remote Attestation:** attested runtime/model/policy/interaction evidence where relevant; a common #22→EA profile is not yet established.

Other Themes may become profiles when a concrete use case requires them. The charter should not turn the complete ideal map into first-cycle scope.

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

For this preparation draft, **independent Incident Lifecycle and Ecosystem Awareness mechanisms are the current technical drafting baseline**. The exact wording, broader Theme #13 partitioning and institutional packaging remain reviewable through the FG-TIDA process.

---

# Supporting preparation notes

The sections below explain why the candidate Charter is written this way. They are not intended to be copied wholesale into a Phase 2 Charter document.

## A. Why the draft is useful now

The public discussion already provides enough structure for a reviewable draft:

- Ward Duchamps placed Ecosystem Awareness within #13 and supported independent definition/testing of the determinacy envelope and signal lifecycle.
- Nelson Trasatti developed the progressive testbed and Use Case #4, and has emphasized versioned adapters, fixtures, traces and bounded executable profiles.
- Lei Gao has supported the bounded Theme #16 interface and approved proceeding with the current UC #6 → matrices → UC #4 sequence.
- Arpita Sarker's UC #6 gives a deliberately small authority-applicability case that can be mapped without inventing new facts.
- Oleksii Voshchak's v0.2 matrix separates qualification validity, epistemic opportunity, operational significance, response timing, computability and re-entry.
- Olena Pavlenko has explicitly cautioned against treating the emerging cross-matrix sequence as a consolidated architecture before testing it against shared cases.
- Olha Borysenko's Theme #16 work separates authority applicability, institutional capacity, decision and execution confirmation.
- Public Use Cases #7, #9 and #10 provide later stressors around persistent identity, action-time state, authority provenance, revocation/composition and capability without conferral.

This is enough to draft. It is not enough to claim final WG packaging, common schemas or adopted cross-Theme profiles.

## B. 05 Ideal versus 05A Current-State

The [05 Ideal Delta](../interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) describes the maximum coherent target architecture.

The [05A Current-State Delta](../interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) classifies each route as:

- **Current source state**
- **Candidate cross-Theme field**
- **Test-only evidence**
- **Not established**

This preparation draft therefore follows:

> **05 for destination; 05A for pacing.**

That allows the Charter to remain architecturally coherent without presenting ideal relationships as already agreed.

## C. Review bandwidth and sequencing

The immediate challenge is no longer a lack of ideas. It is turning the strongest existing contributions into shared, reviewable artefacts without outrunning contributor review bandwidth.

The current public work suggests the following sequence.

### C.1 First deterministic shared mapping

Use [UC #6](https://github.com/FG-TIDA/use-cases/issues/6) as the semantic source.

**UC #6 facts / expected outcomes**  
→ current Theme #16 matrices / bounded interface annotations  
→ relevant Theme #13 risk/response-window/epistemic-opportunity mapping  
→ field-by-field computability / N/A / unresolved items  
→ review by the originating semantic owners

The mapping must not introduce a capacity failure, confidence score, timing variant or grant mutation not present in the source case.

### C.2 Bounded UC #4 executable profile

After semantic review, import the agreed mapping into [UC #4](https://github.com/FG-TIDA/use-cases/issues/4) as:

- versioned mapping/profile;
- bounded adapters;
- frozen fixtures;
- expected outcomes;
- traces; and
- a report/conformance record.

UC #4 keeps its federated signal/corroboration/containment core; the imported case tests one interface rather than replacing the use case.

### C.3 Federated Stage 0/1

Then exercise the #13 mechanism across independently governed participants:

- deterministic/frozen controls;
- signal exchange;
- corroboration/amendment;
- affected-scope refinement;
- locally authorized containment;
- explicit UNKNOWN/source-dependence preservation; and
- revalidation.

This stage should establish the first interoperable/federated route, not claim that two endpoints prove ecosystem behaviour. Before making a stronger ecosystem-level claim, the test programme should expand to multiple independently governed observers/participants with partial, conflicting and shared-lineage evidence. Agent-native / non-adversarial failure should be characterized before deliberate attack classes are added.

### C.4 Minimum Strong-EA Challenge Set

Before claiming that the first cycle exercises **Ecosystem Awareness itself**, rather than only a chain of well-behaved interfaces, the executable package should cover four bounded checks:

1. **Nominal continuity:** same valid local states and no material frame change → no unnecessary systemic HOLD/escalation/requalification.
2. **Local-equivalence / systemic-divergence:** keep the relevant local/native result constant, change one material ecosystem qualifier (for example independent versus shared provenance, current versus stale validity, or sufficient versus exhausted response capacity) → the EA qualification should change only when that difference matters to the receiving decision.
3. **Targeted requalification:** invalidate one specific decision basis/dependency → request/re-enter at that basis, not a generic restart or indiscriminate context expansion.
4. **Independent interoperability:** an external producer and receiver should exchange the admitted profile without sharing internal EA logic; source-native semantics and UNKNOWN must survive.

For comparative evidence, add a strong conventional/native control. If it reproduces the same correct behaviour at equal or lower burden, that is negative evidence for an EA-specific differential.

This is the **minimum challenge floor**, not a request to activate the whole 05 Ideal map in the first cycle.

### C.5 Later stress expansion

Only after the first route is stable, add cases or profiles that expose a distinct interface/falsifier, for example:

- UC #7 — persistent identity versus action-time state;
- UC #9 — authority provenance, composition, revocation and act-time standing;
- UC #10 — capability without conferral / recruited agents;
- UC #5 — model/runtime origin and attestation;
- Theme #17 — rights/identity/registry production case;
- embodied or privilege-lifecycle profiles; and
- later adversarial/resilience campaigns.

Internal EA scenarios or DBC fixtures may supply test pressure but do not replace Theme-owned semantic cases.

## D. Core composition boundaries carried into testing

Where material, test/conformance work should preserve distinctions such as:

- identity ≠ representation ≠ authority;
- capability ≠ conferred authority;
- persistent identity ≠ current action-time state;
- opportunity ≠ admissibility ≠ authority ≠ execution;
- per-action compliance ≠ aggregate/composed authorization;
- policy/conformance verdict ≠ ecosystem truth;
- human decision ≠ attempted execution ≠ externally confirmed outcome;
- local closure ≠ system-level determination;
- incident resolution ≠ ecosystem requalification;
- correlated multiplicity ≠ independent corroboration; and
- technical/token validity ≠ continued semantic applicability.

These are composition boundaries, not a mandatory common runtime vocabulary.

## E. Readiness

### Ready for continued charter drafting

- problem statement;
- Theme #13 origin and EA placement;
- independent Incident Lifecycle / EA drafting boundary;
- general requirements/interfaces;
- ideal versus current FG-TIDA mapping;
- bounded authority/current-applicability interface;
- bounded human-oversight interface;
- source-native handoff principles;
- UC #4 executable/testbed direction;
- UC #6 first deterministic mapping route;
- one EA-differential paired challenge with nominal-continuity control; and
- positive/boundary/rejection test discipline.
- preservation of the broader Theme #13 problem space without forcing all surfaces into the first implementation cycle.

### Still needed before formal Phase 2 promotion

- targeted Theme #13 review of this revised Charter text;
- final WG/document packaging;
- final ownership of the reusable handoff/profile abstraction;
- editor/maintainer commitments;
- semantic-owner confirmation for any normative cross-Theme profiles;
- first reviewed UC #6 cross-interface worked mapping;
- first bounded UC #4 imported executable profile;
- licensing/IP and publication mechanics; and
- co-chair/process confirmation.

Executed interoperability evidence is an evidence gate for stronger status, not a reason to stop maintaining the preparation draft.

## F. Promotion path

1. **Theme #13 review:** problem statement, Incident Lifecycle / EA boundary, deliverable split, #13 profile versus general handoff.
2. **Shared worked mapping:** complete/review UC #6 → current matrices → bounded cross-interface mapping.
3. **UC #4 executable import:** versioned profile, fixtures, traces, expected outcomes and report.
4. **Co-chair/process check:** confirm whether/how Theme #13 should move to Phase 2.
5. **Deliverable ownership:** identify editors, semantic owners, contributors and test maintainers.
6. **Charter PR readiness:** only then project the candidate Charter section above into the official FG-TIDA Charter form.
7. **Specification readiness:** after structure/ownership are accepted, extract specification text through [Annex 01F](../specifications/EA_FG_TIDA_SPECIFICATION_PREPARATION_v0.3_DRAFT.md).

---

## Current determination

The preparation material is now mature enough to support a real FG-TIDA review, but it should remain **v0.1 preparation material** until the Theme/process decides otherwise.

The strongest current work programme is deliberately bounded:

> **Incident / Signal Lifecycle + Ecosystem Awareness → one small reviewed cross-interface mapping → one decisive EA-differential challenge → bounded UC #4 executable profile → federated testbed → later stress/profile expansion.**

The draft should be considered too weak if it only proves that adapters can carry fields correctly. It must also show that a material ecosystem-level qualifier can change the justified systemic assessment while local/native results remain valid, and it must accept as negative evidence any case where strong native controls reproduce that behaviour with equal or lower burden.

This gives Theme #13 a concrete path from discussion to versioned drafting while respecting the central FG-TIDA discipline already visible in the public process: Theme-owned semantics stay with their owners, public Issues retain decisions/attribution, and versioned documents/test artefacts provide stable objects for focused review.
