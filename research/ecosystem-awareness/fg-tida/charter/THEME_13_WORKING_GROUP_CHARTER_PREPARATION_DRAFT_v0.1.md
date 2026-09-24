# Annex 01G — FG-TIDA Theme #13 Phase 2 Charter Preparation Draft

**Status:** Draft v0.1 — living preparation draft; revised 24 September 2026  
**Originating theme:** [FG-TIDA Theme #13 — Ecosystem-level Agent Defense](https://github.com/FG-TIDA/themes/issues/13)  
**Primary public use case:** [FG-TIDA Use Case #4 — Federated ecosystem defense across independently governed organizations](https://github.com/FG-TIDA/use-cases/issues/4)  
**Institutional status:** preparation material only; not submitted as a Phase 2 Charter; not an established Working Group, deliverable, specification, chair/editor assignment or FG-TIDA decision  
**Versioning rule:** this file remains **v0.1** while it is a preparation draft. Git history carries the successive revisions so previously shared links remain stable.

> **Purpose.** Prepare a compact, reviewable Phase 2 charter candidate for Theme #13 while preserving the boundaries already emerging in public discussion. The draft is intentionally more mature than an Issue comment and less committal than an official Charter PR.

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

# Ecosystem-level Agent Defense and Ecosystem Awareness — Charter

**Status:** Draft  
**Originating issue:** [Theme #13 — Ecosystem-level Agent Defense](https://github.com/FG-TIDA/themes/issues/13)  
**Proposer(s) / drafter(s):** to be agreed through the FG-TIDA process

## Summary

Agentic ecosystems increasingly connect independently governed agents, services, humans, evaluators, attesters and infrastructure. Each participant may reach a locally valid result while the combined ecosystem still lacks enough qualified information to support a receiving decision, or while harmful effects propagate across organizational boundaries.

This theme would develop two related, independently testable capabilities: **(1) an Incident / Signal Lifecycle** for ecosystem-defense signalling, corroboration, affected-scope/blast-radius refinement, locally authorized response coordination and resolution; and **(2) Ecosystem Awareness**, which asks what independently produced results collectively establish for a specific decision, what remains unresolved or inherited through dependencies, and when targeted requalification is needed. The work would connect them through bounded, source-preserving interfaces without creating a central controller or new authority. **Defense is the first concrete implementation context, not a requirement that the reusable qualification/handoff semantics be defense-exclusive.**

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
- treat an assessment, confidence value, human approval or signal as authority;
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

## Related Work

The work should coordinate with, rather than reproduce, relevant standards and practices, including where applicable:

- FG-TIDA Themes and Use Cases;
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

- **Theme #5 — Provenance of Authority:** grant origin, scope, limits, standing/revocation/current applicability.
- **Theme #16 — Operational Human Oversight:** human authority/capacity/decision/execution/re-entry state.
- **Theme #6 — Intent / Policy Runtime Conformance:** source-native conformance/verdict semantics are public; the specific #6→EA adapter remains a candidate profile.

Useful **candidate supporting profiles** include:

- **Theme #7 — Verifier-side requirements:** evidence appraisal/failure semantics and negative vectors.
- **Theme #22 — Remote Attestation:** attested runtime/model/policy/interaction evidence where relevant; a common #22→EA profile is not yet established.

Other Themes may become profiles when a concrete use case requires them. The charter should not turn the complete ideal map into first-cycle scope.

## Open Questions

Reviewers are invited to focus on questions that remain genuinely unresolved:

1. **Institutional packaging:** one Theme #13-derived WG with separate peer deliverables/specifications, another document structure, or another FG-TIDA arrangement?
2. **Interoperability profile ownership:** should the general handoff abstraction become a reusable specification/profile beyond the #13 envelope, and who maintains it?
3. **Document split:** should Ecosystem Awareness Core and interoperability profiles be one document or separate deliverables?
4. **Profile admission:** which cross-Theme mappings have enough semantic-owner support to become normative rather than candidate/informative?
5. **Wire format:** should the first work remain semantic/transport-neutral or later include a reference schema?
6. **Conformance packaging:** informative annex/profile or separate test document?
7. **Evidence gate:** what executed evidence is needed before moving beyond early draft status?
8. **Editorial ownership:** who is prepared to edit/maintain each deliverable?
9. **Licensing/IP:** what terms should apply to specifications, fixtures and reference implementations?

For this preparation draft, **independent Incident Lifecycle and Ecosystem Awareness mechanisms are the current technical drafting baseline**. The exact wording and institutional packaging remain reviewable through the FG-TIDA process.

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
