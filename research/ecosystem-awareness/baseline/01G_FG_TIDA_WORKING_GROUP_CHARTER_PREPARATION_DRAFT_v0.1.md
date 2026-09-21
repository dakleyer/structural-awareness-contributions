# Annex 01G — FG-TIDA Working Group / Charter Preparation Draft

**Status:** Draft v0.1 — preparation only  
**Date:** 21 September 2026  
**Source theme:** FG-TIDA Theme #13 — Ecosystem-level Agent Defense  
**EA relation:** Ecosystem Awareness is currently discussed within Theme #13 and across adjacent Themes  
**Institutional status:** not submitted to FG-TIDA; not a Working Group; not a chair/editor/leadership claim; not an adopted charter, deliverable or specification

> **Purpose.** This document prepares a possible Phase 2 charter and Working Group structure without pre-empting the decision of Theme #13 proposer/contributors, FG-TIDA co-chairs or the Focus Group. It follows the public FG-TIDA theme-development process and the structure used by the existing Phase 2 charter proposal in PR #15. It is a drafting aid and decision record, not a proposal unless deliberately promoted through the FG-TIDA process.

## 1. Why prepare a charter draft now

FG-TIDA's public process distinguishes:

1. **Phase 1 — Theme discussion** in Issues;
2. **Phase 2 — Draft Charter** proposed by Pull Request once scope is mature enough and someone is ready to take ownership of writing it properly; and
3. later formalization into Working Groups and specifications if the Focus Group decides that structure is needed.

Theme #13 has already developed beyond an initial brainstorm:

- Ward Duchamps proposed an ecosystem-level defense theme;
- Ward later supported Ecosystem Awareness as belonging within #13;
- Ward described the systemic-capacity / handoff interface as potentially foundational and supported independent definition/testing of the determinacy envelope and signal lifecycle;
- Nelson Trasatti developed a bounded incident-signal / blast-radius testbed direction and formal Use Case #4;
- the public discussion distinguishes incident/signal lifecycle functions from EA qualification;
- Use Case #4 Requirements 19–24 already encode independent mechanisms, determinacy-envelope preservation, #13/#16 bidirectional capacity interaction, versioned adapters and frozen executable vectors; and
- EA now has a public canonical architecture, requirements set, interface model, EHD, validation profiles and specification-preparation map.

This is sufficient to prepare a charter draft. It is **not** sufficient to decide unilaterally that a Working Group exists or that its final scope, name, deliverables or leadership are settled.

## 2. Recommended structural posture

### 2.1 Preferred preparation hypothesis

The least disruptive working hypothesis is:

> **One Theme #13-derived Working Group or equivalent FG-TIDA work structure, with multiple peer mechanisms/deliverables rather than one mechanism absorbing the others.**

Candidate peer mechanisms:

1. **Incident / signal lifecycle and operational blast-radius handling**
2. **Ecosystem Awareness / decision-scoped systemic qualification**
3. **Interoperability and test/conformance profiles** connecting these mechanisms and adjacent Themes

This preserves the discussion to date:

- the incident lifecycle remains a complete operational mechanism;
- EA remains independently testable;
- neither mechanism creates authority merely by producing a signal or assessment;
- the two may interoperate through bounded, versioned interfaces;
- defense/containment is the first concrete use of the interface, not necessarily the full future scope of EA.

### 2.2 Alternatives that remain open

**Alternative A — one integrated WG/specification.**  
A single document could combine incident lifecycle and EA. This is simpler administratively but risks mixing operational incident semantics with epistemic qualification and making ownership harder to maintain.

**Alternative B — one WG, separate specifications.**  
The WG could own several specifications, for example an incident/signal specification and an EA/EHD specification. This currently appears the cleanest technical fit if peer status is confirmed.

**Alternative C — separate EA Working Group.**  
EA could later justify a cross-theme WG because it interfaces with #6, #13, #16, #21 and others. This should not be assumed now because current public placement by Ward is within #13 and the FG has not yet resolved broader structure.

### 2.3 Current recommendation

Prepare for **Alternative B**, while keeping A and C open.

Do not submit or create a `wg<N>-...` repository until:

- Theme #13 placement/peer-mechanism questions are sufficiently resolved;
- co-chairs indicate the appropriate WG structure; and
- editorial ownership for at least the initial deliverables is clear.

## 3. Candidate Charter

The following is a **draft charter skeleton**, written in the structure used by FG-TIDA Phase 2 work. Bracketed or explicitly marked items remain unresolved.

# [Candidate title] Ecosystem-level Agent Defense and Ecosystem Awareness — Charter

**Status:** Draft / preparation only  
**Originating issue:** FG-TIDA Theme #13  
**Proposer(s) / drafter(s):** to be agreed through FG-TIDA process  
**Working Group identifier:** not assigned

## Summary

Agentic ecosystems increasingly consist of independently governed agents, services, humans, evaluators, attesters and infrastructure that exchange claims and depend on each other's outputs without sharing one control plane or internal reasoning model. Local authentication, authorization, policy conformance or human approval may each be valid while the combined ecosystem remains insufficiently qualified for a receiving decision or while harmful effects propagate across organizational boundaries.

The candidate work addresses two related but distinct problems:

1. **operational ecosystem defense:** how incident-relevant signals are created, distributed, corroborated/amended, related into affected scope or blast radius, used to coordinate locally authorized containment, and resolved; and
2. **ecosystem-level qualification:** how a receiving participant determines what independently produced results collectively establish for a specific decision, what remains unresolved or inherited through dependencies, whether capacity and response horizons remain sufficient, and when targeted requalification is required.

The work should remain implementation-neutral and decentralized in control. It should not require a universal trust anchor, central orchestrator, shared private reasoning model or global authority. The common architectural objective is to make the minimum decision-relevant signal, scope, provenance, qualification, capacity and residual state interoperable enough for independently governed participants to reason and act without silently upgrading uncertainty into certainty or assessment into authority.

## Scope

The candidate work would cover the following areas.

### 1. Incident / signal lifecycle

- signal birth and minimum semantics;
- distribution across independently governed participants;
- corroboration, contestation, amendment and supersession;
- observed versus inferred affected scope;
- operational blast-radius/dependency representation;
- response-window information;
- locally authorized graduated containment coordination;
- resolution records and lifecycle closure; and
- preservation of source, provenance, freshness and uncertainty through the lifecycle.

### 2. Ecosystem Awareness

- decision-scoped qualification of local and external states;
- explicit observation/representation boundary;
- preservation of residual and inherited indeterminacy;
- source dependence and independent-corroboration assessment;
- finite evidence, computation, communication and human-review capacity;
- useful response horizon;
- operating-frame validity and targeted requalification;
- distinction between local closure and system-level support; and
- bounded operating posture without creating execution authority.

### 3. Interoperable epistemic handoff

Candidate work includes a minimal semantic handoff allowing different implementations to exchange:

- producer/profile semantics;
- subject/proposition/decision scope;
- issuer/source;
- source-native result or operational closure;
- determination/qualification state;
- explicit UNKNOWN or unresolved qualification; and
- decision-material conditional qualifiers such as freshness, confidence/assurance semantics, capacity, provenance, dependencies and source lineage.

The handoff should preserve source-native vocabulary and should not require disclosure of the producer's complete internal algorithm.

### 4. Cross-theme interfaces

The work may consume, without redefining:

- authority/provenance from Theme #5 or successor work;
- policy/conformance verdicts from Theme #6 or successor work;
- human-oversight capacity and decision state from Theme #16 or successor work;
- attestation/appraisal outputs from Theme #22 or successor work;
- specialised privacy/evaluation outputs from #19/#21 or successor work; and
- execution/enforcement/outcome state from the relevant control owners.

### 5. Testing and conformance

The work may define:

- positive, boundary and rejection fixtures;
- version-pinned adapters;
- interface conformance records;
- cross-implementation interoperability tests;
- preservation of UNKNOWN, scope, provenance and dependency state; and
- bounded testbeds that do not absorb external Theme logic.

## Out of Scope

The following are explicitly out of scope unless FG-TIDA later changes the charter:

- creating legal, institutional, policy or containment authority;
- defining the origination of authority or delegation grants;
- replacing identity, attestation, policy or access-control standards;
- a universal trust/reputation score;
- a mandatory central ecosystem controller;
- requiring all participants to implement one internal EA algorithm;
- requiring disclosure of complete internal reasoning, objectives or private state;
- defining the complete Theme #16 human-oversight lifecycle;
- defining the complete Theme #6 policy-verdict algorithm;
- defining the complete Theme #13 containment enforcement mechanism where enforcement is owned by another actor;
- universal liability allocation;
- universal jurisdiction/legal-compliance determination;
- product certification;
- a requirement to collect maximum context or telemetry;
- treating a signal, assessment, confidence value or human approval as authority by itself; and
- converting research hypotheses or illustrative scenarios into normative requirements without separate WG review.

## Objectives / Deliverables

The exact deliverable split requires FG-TIDA confirmation. A candidate structure is:

### D1 — Common terminology, scope and architectural boundary

Define:

- ecosystem participant / producer / receiver / semantic owner;
- decision domain and scope;
- observed versus derived state;
- local closure versus system-level qualification;
- UNKNOWN/residual/inherited indeterminacy;
- capacity and response horizon;
- affected scope / blast radius;
- operating-frame requalification; and
- authority/non-authority boundaries.

### D2 — Incident / Signal Lifecycle specification

Candidate content:

- signal lifecycle;
- minimum signal semantics;
- provenance/freshness;
- corroboration/amendment;
- affected-scope/blast-radius semantics;
- response-window properties;
- graduated containment coordination;
- resolution; and
- privacy/adversarial considerations.

**Editorial ownership:** to be agreed with Theme #13 contributors. This preparation draft does not assign D2 to any person.

### D3 — Ecosystem Awareness Core Architecture specification

Candidate content:

- requirements and non-goals;
- decision-scoped qualification;
- functional responsibilities;
- residual/inherited indeterminacy;
- source dependence;
- capacity and horizon;
- operating postures;
- targeted requalification;
- no-supercontroller and no-authority-creation rules.

### D4 — Epistemic Handoff / Interoperability profile

Candidate content:

- EHD semantic kernel;
- conditional qualifiers;
- source-native semantics;
- profile/version rules;
- Theme-specific mappings;
- UNKNOWN handling;
- adapter rules; and
- optional reference schema if useful.

D3 and D4 may remain one specification if the WG prefers.

### D5 — Conformance / Reference Test Profiles

Candidate content:

- interface conformance record;
- positive/boundary/rejection fixtures;
- cross-implementation tests;
- version-pinned adapters;
- UC #4 / EA-ITP-derived vectors;
- evidence and trace requirements; and
- reproducible result packages.

D5 may initially be an informative annex rather than a separate specification.

## Related Work

The charter should reference, not reproduce, relevant work including:

- FG-TIDA Themes #5, #6, #10, #13, #16, #19, #21 and #22;
- FG-TIDA Use Case #4;
- IETF RATS/EAT/AR4SI and related workload-identity work;
- STIX/TAXII and incident-exchange practice;
- OpenC2/XACML where command/policy semantics are relevant;
- NIST AI RMF and relevant AI/TEVV work;
- provenance and distributed-observability work;
- agent interoperability substrates such as A2A;
- applicable privacy/security standards; and
- relevant ISO/IEC and IEEE human-oversight/autonomous-system work.

A formal duplication review should be maintained per ITU-T Recommendation A.7.

## Related Themes

### Theme #13

Originating Theme. The charter must preserve the distinction between incident/signal lifecycle and EA qualification unless FG-TIDA deliberately chooses another architecture.

### Theme #5

Provides authority provenance/current applicability. This work consumes authority qualification; it does not create grants.

### Theme #6

Provides policy/conformance verdict semantics where applicable. A verdict remains source-native and does not become ecosystem truth merely by crossing an interface.

### Theme #16

Provides human-oversight lifecycle semantics and relevant human capacity/decision state. EA may consume these states and return decision-scoped requalification information without choosing the human action.

### Theme #22

May provide attestation/appraisal evidence. Attestation proves only what its profile and evidence establish; it does not automatically establish systemic sufficiency.

### Other Themes

#1/#10 may provide action/outcome/enforcement state; #19/#21 may provide privacy/evaluation constraints or scoped evidence. Interfaces remain bounded and owner-preserving.

## Open Questions

The following questions must remain open in the draft until public FG-TIDA discussion resolves them:

1. Should Theme #13's incident/signal lifecycle and EA be formally described as peer mechanisms?
2. Should they live in one WG with separate specifications or in another structure?
3. Is EHD the appropriate reusable abstraction beyond the #13 determinacy-envelope profile?
4. Should D3 and D4 be one document or separate specifications?
5. Which EHD elements are mandatory semantics versus optional profile qualifiers?
6. Should the first specification remain transport-neutral or include a reference schema/API?
7. Which Theme-specific mappings have enough semantic-owner support for normative profiles?
8. What human-review assurance/confidence semantics, if any, should be exposed by Theme #16?
9. How should incident resolution differ from ecosystem requalification in normative text?
10. Which containment semantics belong in this WG versus external enforcement owners?
11. What minimum executed evidence should be required before a candidate profile moves from Draft to stronger status?
12. What licensing/IP terms apply to specifications, fixtures and reference implementations?
13. Who will act as editors/maintainers once the FG chooses the work structure?

## 4. Working Group formation readiness

### Ready now

The following are mature enough for charter drafting:

- clear problem statement;
- explicit Theme #13 origin;
- concrete incident-lifecycle direction;
- independently testable EA architecture;
- explicit cross-theme boundaries;
- a formal Use Case #4;
- public requirements and validation corpus;
- candidate specification structure;
- conformance/test direction;
- documented non-goals.

### Not yet ready for formal WG creation without discussion

The following remain material:

- final peer relationship between signal lifecycle and EA;
- final WG boundary/name;
- deliverable split;
- editor/leadership commitment;
- EHD general ownership;
- final normative profile fields;
- semantic-owner confirmation for adjacent Themes.

## 5. Promotion path

This draft should progress only through explicit gates.

### Gate WG-A — Theme-owner review

Obtain review/correction from Theme #13 proposer/contributors on:

- problem statement;
- peer-mechanism boundary;
- incident-lifecycle scope;
- EA placement.

### Gate WG-B — Co-chair process check

Ask FG-TIDA co-chairs:

- whether Theme #13 should proceed to Phase 2 Charter;
- whether one or several specifications are appropriate;
- whether the WG structure should wait for Paris or can be prepared in advance.

### Gate WG-C — Deliverable ownership

For each candidate deliverable identify:

- editorial owner(s);
- semantic owners;
- expected contributors;
- dependencies;
- first review milestone.

### Gate WG-D — Charter PR readiness

Only then project this preparation draft into the official FG-TIDA charter form and submit by Pull Request.

### Gate WG-E — Specification repository readiness

After charter/WG structure is accepted sufficiently to assign document ownership, use the FG-TIDA specification template to create the appropriate `wg<N>-...` repository/repositories.

## 6. Relationship to Annex 01F

[Annex 01F — EA / FG-TIDA Specification Preparation Map](./01F_EA_FG_TIDA_SPECIFICATION_PREPARATION_ANNEX_v0.1_DRAFT.md) prepares the **document(s)**.

This 01G prepares the **organizational/charter container** that could own those documents.

The separation is deliberate:

- **01F:** what would go into a specification, how source material maps to it, and what is normatively mature;
- **01G:** what WG/charter could own the work, its scope, deliverables, dependencies and open governance questions.

Neither annex creates FG-TIDA status.

## 7. Current determination

It is useful to prepare a Working Group charter now because the technical material is already mature enough to expose the real scope and deliverable choices. It is **not** useful to submit or instantiate a Working Group unilaterally while the Theme #13 peer-mechanism boundary and editorial ownership remain unresolved.

The recommended state is therefore:

**Theme #13 discussion + UC #4 + EA corpus → 01F specification preparation + 01G charter preparation → Theme-owner/co-chair review → Phase 2 Charter PR → WG/specification repositories if approved.**
