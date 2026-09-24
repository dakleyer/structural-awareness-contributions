# Annex 01G — FG-TIDA Theme #13 Working Group / Charter Preparation Draft

**Status:** Draft v0.1 — living preparation draft; revised 24 September 2026  
**Source theme:** [FG-TIDA Theme #13 — Ecosystem-level Agent Defense](https://github.com/FG-TIDA/themes/issues/13)  
**Primary public use case:** [FG-TIDA Use Case #4 — Federated ecosystem defense across independently governed organizations](https://github.com/FG-TIDA/use-cases/issues/4)  
**Institutional status:** not submitted to FG-TIDA; not a Working Group; not a chair/editor/leadership claim; not an adopted charter, deliverable or specification  
**Stable-path note:** this file is edited in place while it remains a preparation draft so previously shared review links remain valid.

> **Purpose.** This document prepares a possible Phase 2 charter / Working Group structure around Theme #13 without pre-empting the decisions of Theme contributors, FG-TIDA co-chairs or the Focus Group. It is a drafting aid and convergence record. It becomes a proposal only if deliberately promoted through the FG-TIDA process.

---

## 0. About this draft — what it is, where it comes from, and how to read it

### 0.1 What is FG-TIDA?

[FG-TIDA](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/default.aspx) is the **ITU-T Focus Group on Trust and Identity for Humans and Agentic AI**, established under ITU-T Study Group 17. Its scope includes trust management and interoperable digital-identity infrastructure for humans and agentic AI, including multi-actor ecosystems in which users, agents, service providers and relying parties interact.

This preparation draft addresses one bounded part of that wider problem: **ecosystem-level agent defense and ecosystem-level qualification across independently governed participants**.

### 0.2 What problem is this draft trying to organize?

Theme #13 began from an operational ecosystem-defense problem: independently governed participants need a way to exchange incident-relevant signals, corroborate them, understand affected scope or blast radius, coordinate locally authorized containment and eventually resolve the incident.

The discussion then exposed a second, related problem:

> **A locally valid result does not automatically establish what the ecosystem as a whole knows, what remains unresolved, or whether the current operating frame is still sufficiently supported for a receiving decision.**

That second problem is the role of **Ecosystem Awareness (EA)**.

The current technical working posture is therefore not one mechanism absorbing the other. It is:

1. **Incident / Signal Lifecycle** — the operational ecosystem-defense mechanism; and
2. **Ecosystem Awareness** — the decision-scoped systemic qualification mechanism;

with bounded interoperability and test/conformance material connecting them and adjacent Themes.

### 0.3 Minimum reading path

A reviewer does **not** need to read the whole research corpus before commenting on this draft.

For the shortest useful path, read:

1. [Theme #13](https://github.com/FG-TIDA/themes/issues/13) and [Use Case #4](https://github.com/FG-TIDA/use-cases/issues/4) — the public FG-TIDA origin and executable direction.
2. [00 — Canonical Requirements](../../baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) + [Requirements vNext Delta](../../baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) — what a sufficiently good solution must preserve; the delta records later clarification candidates without rewriting the frozen baseline.
3. [04 — General Functional Interfaces](../../baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md) + [04 vNext Delta](../../baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) — the programme-independent EA interface architecture.
4. [05 — Ideal FG-TIDA Interfaces](../interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md) + [05 Ideal Delta](../interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) — the **maximum coherent target architecture** if FG-TIDA had the necessary semantic owners, implementations and review/test capacity.
5. [05A — Current-State Bridge](../interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md) + [05A Current-State Delta](../interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) — the **realistic current-state filter** showing what the public FG-TIDA record can actually support now.

[Annex 01F — Specification Preparation](../specifications/EA_FG_TIDA_SPECIFICATION_PREPARATION_v0.3_DRAFT.md) is the companion editorial map for what future specification documents could contain. It is useful after the architectural boundary is understood; it is not the source of the architecture.

### 0.4 Drafting rule: target from 05, admission from 05A

This charter-preparation draft uses a simple discipline:

> **05 defines the target. 05A determines what can responsibly enter the current draft as mature/current rather than merely candidate.**

Therefore this document may describe the richer architectural destination while keeping the first work programme deliberately bounded.

The draft must not:

- make an ideal 05 relationship look already adopted;
- turn internal EA test vocabulary into FG-TIDA runtime semantics;
- assign ownership to a contributor merely because they proposed useful work; or
- overload the first drafting cycle with every case, Theme or fixture that could eventually fit.

---

## 1. Why a charter-preparation draft is useful now

Theme #13 has moved beyond an initial brainstorm.

Public discussion now provides several independently useful pieces:

- Ward Duchamps proposed the ecosystem-level defense Theme and later placed Ecosystem Awareness within #13.
- Ward supported independent definition/testing of the **determinacy envelope** and the **signal lifecycle**, so they can interoperate without assuming one binding implementation.
- Nelson Trasatti developed the progressive testbed direction and submitted formal Use Case #4.
- Nelson confirmed from the testbed side that the incident lifecycle remains a complete operational mechanism, EA remains independently testable, and targeted refinement can be exercised without the testbed becoming the owner of general EHD semantics.
- Theme #16 contributors have developed bounded authority/capacity/decision/execution matrices and interfaces.
- Lei Gao has approved the current bounded sequence using UC #6 as semantic source, Theme #16 matrices as annotation, and UC #4 as the downstream executable mapping layer.
- Oleksii Voshchak's v0.2 matrix has made semantic/qualification validity, epistemic opportunity, operational significance, response window, computability and re-entry more explicit.
- Olena Pavlenko has explicitly cautioned against treating the emerging cross-matrix sequence as a consolidated architecture before it is tested against common cases.
- Arpita Sarker's UC #6 supplies a deliberately small deterministic authority-applicability case for that first shared mapping.
- Additional public Use Cases #7, #9 and #10 now provide stronger later stressors around persistent identity, act-time state, authority provenance, revocation/composition and capability without conferral.

This is enough to maintain a **serious preparation draft**.

It is not yet evidence that FG-TIDA has decided:

- the exact WG packaging;
- the final document split;
- the general ownership of EHD;
- the normative profile set;
- editor/maintainer assignments; or
- the evidentiary threshold for moving from working draft to a stronger status.

---

## 2. Current technical posture versus institutional posture

### 2.1 Technical working posture

The strongest current technical reading is:

> **One Theme #13-derived scope containing two independently testable peer mechanisms, connected through bounded interfaces, plus a supporting interoperability/conformance layer.**

The two mechanisms are:

1. **Incident / Signal Lifecycle**
2. **Ecosystem Awareness**

The interoperability/conformance material is **not a third peer operational mechanism**. It is the means by which the two mechanisms and adjacent Theme outputs can be connected and tested without merging ownership.

### 2.2 Why the mechanisms should remain distinct

**Incident / Signal Lifecycle** answers questions such as:

- what signal was created and by whom;
- how it was distributed;
- how it was corroborated, contested, amended or superseded;
- what agents/services/assets may be operationally affected;
- what containment reach exists;
- how locally authorized response is coordinated; and
- when the incident lifecycle is resolved.

**Ecosystem Awareness** answers a different class of questions:

- what the available local/external states establish **for this receiving decision**;
- which conclusions inherit uncertainty or source dependence;
- whether apparent corroboration is materially independent;
- whether the current qualification is still semantically valid;
- what additional state remains obtainable within current capacity;
- whether obtaining more information is still decision-relevant before the response window closes;
- what remains structurally unresolved; and
- which assumption, dependency, authority or evidence source should be requalified next.

The distinction is essential:

- incident resolution ≠ ecosystem requalification;
- operational blast radius ≠ epistemic dependency / inherited-indeterminacy structure;
- signal confidence ≠ systemic determinacy;
- containment reach ≠ containment authority; and
- neither mechanism creates authority merely by producing a signal, assessment or request.

### 2.3 Institutional posture remains open

The technical posture above does **not** settle the institutional packaging.

The current preparation preference is:

> **one Theme #13-derived WG or equivalent work structure, with separate peer deliverables/specifications for Incident/Signal Lifecycle and Ecosystem Awareness, plus shared interoperability/conformance material.**

FG-TIDA may still choose another document or WG packaging. The draft should not create repositories, editor roles or WG identifiers before that process occurs.

---

## 3. Capacity-of-absorption and sequencing rule

The current group is producing useful material quickly. That is a strength, but it creates a real drafting constraint: **the rate of new concepts can exceed the rate at which contributors can read, test and integrate them coherently.**

The public work currently has a natural division:

| Contributor / source | Current visible contribution relevant to this draft | Drafting implication |
|---|---|---|
| **Ward Duchamps** | Theme #13 origin, signal-lifecycle direction, EA placement within #13, independent envelope/lifecycle testing. | Core #13 architecture should remain aligned with this boundary; institutional/document packaging should still be reviewed with him. |
| **Nelson Trasatti** | UC #4, progressive testbed, bounded executable-profile approach, versioned adapters/fixtures/traces. | The draft should provide a clean executable path without turning the testbed into semantic owner. |
| **Oleksii Voshchak** | Operational Risk / Response Window / Epistemic Opportunity matrix v0.2. | First priority is deterministic worked mapping/computability, not another conceptual layer. |
| **Olena Pavlenko** | Human-oversight decision mapping and cross-matrix interface reading; explicit caution against premature consolidation. | Keep the architecture modular; test the shared sequence before freezing a wider interface. |
| **Olha Borysenko** | Institutional authority & oversight capacity matrix v0.2 and the separation of authority applicability, capacity, decision and execution confirmation. | Use bounded interface semantics; do not add fields merely for completeness. |
| **Lei Gao** | Theme #16 boundary and approval of UC #6 → v0.2 matrices → UC #4 sequencing. | #16 route is sufficiently mature for a bounded mapping, not for the draft to absorb the whole human-oversight lifecycle. |
| **Arpita Sarker** | UC #6 semantic case and expected outcomes. | Preserve UC #6 facts; derived test mappings must not rewrite the case. |
| **Pam Dixon / Theme #5 and UCs #9/#10** | Authority provenance, act-time standing, composition/revocation, anchor integrity, capability without conferral. | Strong later stress cases; not all need to enter the first implementation cycle. |

This table records public contribution direction, **not assigned roles or commitments**.

### 3.1 Absorption rule for the first draft

The first serious draft should concentrate on the interfaces already converging:

1. #13 Incident Lifecycle ↔ EA;
2. authority/current-applicability input;
3. #16 human-oversight capacity/decision boundary;
4. source-native policy/evidence/attestation inputs;
5. executable mapping through reviewed cases and bounded adapters.

Later cases and profiles should be admitted only when they add a materially distinct interface/falsifier.

**Do not make the first charter carry the whole 05 Ideal at once.**

---

## 4. Candidate Charter

# [Candidate title] Ecosystem-level Agent Defense and Ecosystem Awareness — Charter

**Status:** Draft / preparation only  
**Originating issue:** FG-TIDA Theme #13  
**Primary implementation use case:** FG-TIDA Use Case #4  
**Proposer(s) / drafter(s):** to be agreed through the FG-TIDA process  
**Working Group identifier:** not assigned

### 4.1 Summary

Agentic ecosystems increasingly consist of independently governed agents, services, humans, evaluators, attesters and infrastructure that exchange claims and depend on one another's outputs without sharing one control plane, one internal reasoning model or one global authority.

Local authentication, authorization, attestation, policy conformance, evaluation or human approval may each be valid while:

- harmful effects propagate across organizational boundaries;
- several participants hold incompatible but locally justified views;
- several apparently corroborating results depend on the same source;
- a previously valid authority/evidence/context condition becomes stale before use;
- a human or automated response arrives after the useful decision window;
- an executed outcome differs from the decision that was recorded; or
- the ecosystem still lacks sufficient support for the receiving decision.

The candidate work therefore combines two related but distinct capabilities:

1. **Operational ecosystem defense** — an Incident / Signal Lifecycle for signal creation, distribution, corroboration/amendment, affected-scope/blast-radius refinement, locally authorized containment coordination and resolution.
2. **Ecosystem Awareness** — decision-scoped systemic qualification of what independently produced states collectively establish, what remains unresolved or inherited through dependencies, whether further epistemic effort is still useful, and what requires targeted requalification.

The work remains decentralized in control and source-owned in semantics. It does not create a universal authority, global trust score or central ecosystem brain.

---

## 5. Scope

### 5.1 Incident / Signal Lifecycle

Candidate scope:

- signal birth and minimum semantics;
- issuer/source and relevant provenance;
- distribution across independently governed participants;
- freshness/expiry and update semantics;
- corroboration, contestation, amendment and supersession;
- observed versus inferred affected scope;
- operational blast-radius/dependency representation;
- response-window information;
- available containment/recovery reach;
- coordination of **locally authorized** graduated response;
- resolution records and lifecycle closure; and
- preservation of relevant unresolved qualifiers through the lifecycle.

### 5.2 Ecosystem Awareness

Candidate scope:

- decision-scoped qualification of local and external states;
- explicit observation/representation boundary;
- source dependence and independent-corroboration assessment;
- preservation of residual and inherited indeterminacy;
- finite evidence, computation, communication and human-review capacity;
- semantic / qualification validity window;
- operational response window as a separate clock;
- what can still be known within current available capacity;
- whether additional knowledge would still be useful for the current decision;
- contextual operational significance without creating authorization;
- effective-role drift where material;
- local closure versus system-level support;
- targeted re-entry/requalification;
- attempted execution versus externally confirmed outcome where available; and
- bounded output without creating execution authority.

### 5.3 Interoperable handoff

The work may define a minimal semantic handoff/profile allowing different implementations to exchange enough decision-relevant qualification without disclosing their complete internal reasoning.

Candidate common semantics include:

- producer/profile reference and version;
- subject/proposition/decision scope;
- issuer/source;
- source-native result/closure;
- determination/qualification state;
- explicit UNKNOWN/unresolved qualifiers; and
- conditional decision-material qualifiers such as freshness, assurance semantics, capacity, provenance, dependency/source lineage, validity/review condition and targeted re-entry reference.

The common handoff should remain **partial by construction**. Missing qualification is represented, not fabricated.

### 5.4 Cross-Theme interface families

The work may consume and return bounded state to adjacent functions without redefining them.

Initial interface families include:

- **identity / representation / principal binding**;
- **authority / delegation / current applicability / privilege lifecycle**;
- **policy / intent / runtime conformance**;
- **verifier-side evidence / attestation**;
- **human oversight authority, capacity and decision state**;
- **accountability / action / execution records**;
- **enforcement / containment / recovery**;
- **privacy / minimum disclosure**;
- **population / external evaluation**; and
- later model-level, embodied or domain-specific profiles where separately justified.

Theme-specific profiles enter normative work only after the relevant semantic-owner review. Otherwise they remain candidate or informative.

### 5.5 Testing and conformance

The work may define:

- positive, boundary and rejection fixtures;
- version-pinned adapters/profiles;
- source-native expected outcomes/oracles;
- interface conformance records;
- cross-implementation interoperability tests;
- explicit UNKNOWN / not-established handling;
- provenance/dependency and qualification-survival checks;
- decision/execution reconstruction;
- burden and response-window evidence; and
- bounded testbeds that do not absorb the logic of adjacent Themes.

---

## 6. Core state-separation rules

The work should preserve, where material:

- identity ≠ representation ≠ authority;
- capability ≠ conferred authority;
- persistent identity ≠ current action-time state;
- opportunity ≠ admissibility ≠ authority ≠ execution;
- per-action compliance ≠ aggregate/composed authorization;
- attestation ≠ truth of every downstream claim;
- policy/conformance verdict ≠ ecosystem truth;
- human authority/decision ≠ epistemic repair;
- human decision ≠ attempted execution ≠ externally confirmed outcome;
- local closure ≠ system-level determination;
- incident resolution ≠ ecosystem requalification;
- correlated multiplicity ≠ independent corroboration;
- technical/token validity ≠ continued semantic applicability; and
- containment reach ≠ containment authority.

These are **composition boundaries**, not a requirement that every producer use one common vocabulary.

---

## 7. Out of Scope

Unless FG-TIDA later changes the charter, the work should not:

- create legal, institutional, policy or containment authority;
- define the origination of authority or delegation grants;
- replace identity, attestation, policy, access-control or privilege-lifecycle standards;
- determine legal personhood or universal liability;
- define one universal trust/reputation score;
- require a mandatory central ecosystem controller;
- require all participants to implement one internal EA algorithm;
- require disclosure of complete prompts, reasoning, objectives or private state;
- define the complete human-oversight lifecycle owned elsewhere;
- define the complete policy/conformance algorithm owned elsewhere;
- define the internal implementation of model-level or embodied trust mechanisms;
- turn assessment, confidence, human approval or a signal into authority;
- treat test vocabulary (including DBC dispositions or internal posture labels) as mandatory runtime ontology;
- require maximum context/telemetry collection;
- force heterogeneous variables into one universal risk/determinacy score;
- certify products;
- convert research hypotheses or illustrative scenarios into normative requirements without separate review; or
- treat private discussion or internal EA material as FG-TIDA adoption.

---

## 8. Candidate deliverables

The exact split remains subject to FG-TIDA review.

### D1 — Common terminology, scope and architectural boundary

Candidate content:

- participant / producer / receiver / relying party / semantic owner;
- decision domain and scope;
- local result versus system-level qualification;
- source-native semantics;
- UNKNOWN / residual / inherited indeterminacy;
- affected scope / blast radius;
- semantic validity versus response window;
- authority/non-authority boundaries;
- requalification / re-entry; and
- incident resolution versus ecosystem requalification.

### D2 — Incident / Signal Lifecycle

Candidate content:

- signal lifecycle;
- minimum signal semantics;
- provenance/freshness;
- corroboration/contestation/amendment;
- affected-scope/blast-radius semantics;
- response-window properties;
- locally authorized response coordination;
- resolution; and
- privacy/adversarial considerations.

**D2 remains a complete peer operational mechanism.**

### D3 — Ecosystem Awareness Core

Candidate content:

- decision-scoped systemic qualification;
- bounded observation/representation;
- residual/inherited indeterminacy;
- source dependence / independent corroboration;
- finite determination resources;
- semantic/qualification window;
- epistemic opportunity;
- contextual significance;
- targeted requalification;
- output validity/limitations;
- no-supercontroller and no-authority-creation rules.

**D3 remains independently testable from D2.**

### D4 — Epistemic Handoff / Interoperability Profiles

Candidate content:

- common semantic kernel;
- conditional qualifiers;
- source-native result preservation;
- profile/version rules;
- UNKNOWN/not-established handling;
- bounded adapters;
- composition-critical extensions where required;
- Theme/domain-specific profiles; and
- optional reference schema only if the WG later finds one useful.

D4 must not become a mechanism that forces every Theme into EA vocabulary.

### D5 — Conformance / Reference Test Profiles

Candidate content:

- interface conformance records;
- positive/boundary/rejection fixtures;
- cross-implementation testing;
- version-pinned adapters;
- trace and evidence requirements;
- reproducible result packages;
- UC #4 / EA-ITP-derived vectors; and
- DBC-derived boundary tests where they test an agreed requirement.

D5 may begin as an informative/test package rather than a standalone specification.

---

## 9. Initial implementation and validation sequence

The draft should deliberately start smaller than the full 05 Ideal map.

### Phase A — establish the shared boundary

Stabilize enough terminology and interface semantics to exercise:

- Incident Lifecycle ↔ EA;
- authority/current-applicability input;
- human-oversight capacity/decision input;
- source-native policy/evidence/attestation input; and
- execution/revalidation output boundaries.

### Phase B — first deterministic cross-interface case

Use [UC #6](https://github.com/FG-TIDA/use-cases/issues/6) as the semantic source.

The current public sequence is:

**UC #6 facts / expected outcomes**  
→ **Theme #16 v0.2 matrices annotate the relevant interfaces**  
→ **the Theme #13 operational-risk / response-window / epistemic-opportunity work is exercised where applicable without changing UC #6 facts**  
→ **field-by-field computability / N/A / unresolved mapping**  
→ **semantic-owner review**

Key rule: the test does not add a capacity failure, confidence score, timing variant or grant mutation that the source case did not define.

### Phase C — bounded UC #4 executable profile

After review of the shared mapping, use [UC #4](https://github.com/FG-TIDA/use-cases/issues/4) as the executable/testbed layer:

- versioned mapping;
- adapters;
- frozen fixtures;
- expected outcomes;
- traces;
- report/conformance record.

UC #4 retains its federated signal/corroboration/containment core. The imported case remains an interface test, not a replacement for that core.

### Phase D — federated Stage 0/1

Exercise the initial #13 mechanism across independently governed participants with:

- deterministic/frozen Stage 0 controls;
- federated Stage 1 signal exchange;
- corroboration/amendment;
- affected-scope refinement;
- locally authorized containment;
- revalidation;
- explicit UNKNOWN and source-dependence preservation.

### Phase E — later stress expansion

Only after the initial route is stable, admit additional public cases/profile families when they add a materially distinct interface condition, for example:

- UC #7 — persistent identity versus action-time state;
- UC #9 — authority provenance, composition, revocation and act-time standing;
- UC #10 — capability without conferral / recruited agents;
- UC #5 — model/runtime origin and attestation;
- Theme #17 — rights/identity/registry production case;
- embodied or privilege-lifecycle profiles; and
- adversarial/resilience campaigns.

Internal EA scenarios/DBC fixtures may provide stress tests, but they do not replace Theme-owned semantic cases.

---

## 10. Relationship to the ideal and current-state interface maps

### 10.1 05 Ideal — target architecture

The [05 Ideal Delta](../interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) shows the maximum coherent mapping if FG-TIDA can eventually support:

- broad Theme-owned profiles;
- multiple independent implementations;
- rich case/fixture coverage;
- cross-sector stress campaigns;
- independent reviewers/challengers; and
- mature conformance/evidence practices.

This charter draft may use that map to avoid designing itself into a dead end.

### 10.2 05A — present admission boundary

The [05A Current-State Delta](../interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) is the current reality check.

It distinguishes:

- **Current source state**
- **Candidate cross-Theme field**
- **Test-only evidence**
- **Not established**

A charter section may describe a candidate future profile, but it should not present it as mature/current unless 05A supports that status.

### 10.3 Why both are necessary

05 without 05A would overstate readiness.

05A without 05 would optimize only for today's partial state and lose the architecture the group may need later.

This draft therefore uses:

> **05 for destination; 05A for pacing.**

---

## 11. Related Themes and work

The charter should reference adjacent work without reproducing it.

### Initial direct interface set

- **Theme #5 — Provenance of Authority:** grant origin, scope, limits, standing/revocation/current applicability.
- **Theme #6 — Intent / Policy Runtime Conformance:** source-native policy/conformance verdicts.
- **Theme #7 — Verifier-side requirements:** appraisal/failure semantics where relevant.
- **Theme #13 — Ecosystem-level Agent Defense:** originating Theme; Incident/Signal Lifecycle.
- **Theme #16 — Operational Human Oversight:** authority/capacity/decision/execution/re-entry lifecycle.
- **Theme #22 — Remote Attestation:** attested runtime/model/policy/interaction evidence where applicable.

### Supporting / later profiles

May include #1, #2, #4, #8, #10, #11, #12, #14, #17, #18, #19, #20, #21 and #23 where a concrete case/profile requires them.

The full ideal mapping is maintained in 05. The charter should **not** reproduce every 05 row as a commitment for the first WG cycle.

---

## 12. Readiness

### 12.1 Technically ready for a living charter draft

The following are sufficiently mature to write and review:

- problem statement;
- Theme #13 origin and EA placement;
- independent Incident Lifecycle / EA technical boundary;
- programme-independent requirements and general interfaces;
- ideal versus current FG-TIDA mapping;
- bounded authority/current-applicability interface;
- bounded human-oversight interface;
- source-native handoff principles;
- UC #4 executable/testbed direction;
- UC #6 first deterministic mapping route;
- positive/boundary/rejection test discipline; and
- explicit non-goals.

### 12.2 Not yet ready for formal Phase 2 promotion

Material items still need review or evidence:

- final WG/document packaging;
- detailed review by Theme #13 contributors of the revised architecture/deliverable split;
- EHD's final reusable ownership and profile boundary;
- editor/maintainer commitments;
- which external profiles are ready for normative rather than candidate/informative treatment;
- first reviewed UC #6 cross-interface worked mapping;
- first bounded UC #4 imported executable profile;
- licensing/IP and publication mechanics; and
- co-chair/process confirmation.

Executed interoperability evidence is desirable but is not a reason to stop maintaining the preparation draft. It is an evidence gate for stronger status.

---

## 13. Open decisions

The draft should keep only genuinely unresolved questions open.

1. **Institutional packaging:** one WG with separate peer specifications, another document structure, or another FG-TIDA arrangement?
2. **EHD ownership:** should EHD become a reusable specification/profile beyond the #13 determinacy-envelope profile, and who maintains it?
3. **Document split:** D3 and D4 together or separate?
4. **Profile admission:** which Theme-specific mappings have enough semantic-owner support to become normative profiles rather than candidate/informative?
5. **Wire format:** remain semantic/transport-neutral initially, or add a reference schema later?
6. **Conformance packaging:** annex/profile or separate test document?
7. **Evidence gate:** what executed evidence is required before moving beyond Working Draft / Review Candidate?
8. **Editorial ownership:** who will edit/maintain each deliverable?
9. **Licensing/IP:** what terms apply to specifications, fixtures and reference implementations?
10. **WG/process timing:** what should be prepared before versus after the next FG-TIDA coordination milestone?

The **technical peer-mechanism boundary itself is no longer treated as the principal open question** in this preparation draft. It is the current working architecture, while institutional packaging remains open.

---

## 14. Promotion path

This draft should progress through explicit, bounded gates.

### Gate WG-A — targeted Theme #13 review

Review with Theme #13 contributors:

- problem statement;
- Incident Lifecycle / EA boundary;
- deliverable split;
- #13 profile versus general EHD;
- what belongs in the first implementation cycle.

### Gate WG-B — first shared worked mapping

Complete and review:

**UC #6 → current matrices → bounded cross-interface mapping**

before adding another conceptual layer.

### Gate WG-C — UC #4 executable import

After semantic review:

- versioned adapter/profile;
- fixtures;
- traces;
- expected outcomes;
- conformance/evidence report.

### Gate WG-D — co-chair / process check

Confirm:

- whether Theme #13 should proceed to Phase 2 Charter;
- preferred WG/document packaging;
- expected timing;
- repository/process requirements.

### Gate WG-E — deliverable ownership

For each candidate deliverable identify:

- editor(s);
- semantic owners;
- expected contributors;
- test/conformance maintainer where applicable;
- dependencies; and
- first review milestone.

### Gate WG-F — Charter PR readiness

Only then project this living preparation draft into the official FG-TIDA charter form and submit it through the agreed process.

### Gate WG-G — specification repository readiness

After the WG/deliverable structure is sufficiently accepted, create the appropriate specification repository/repositories and extract text through the 01F source-to-specification discipline.

---

## 15. Relationship to Annex 01F

[Annex 01F — EA / FG-TIDA Specification Preparation Map](../specifications/EA_FG_TIDA_SPECIFICATION_PREPARATION_v0.3_DRAFT.md) prepares the **document(s)**.

This 01G prepares the **organizational/charter container** that could own those documents.

The separation is deliberate:

- **00/04** define the programme-independent requirements/interfaces;
- **05/05A** define the ideal and current FG-TIDA application boundary;
- **01F** asks what specification text could be extracted and at what normative maturity;
- **01G** asks what WG/charter scope, deliverables, dependencies and governance could own that work.

Neither annex creates FG-TIDA status.

---

## 16. Current determination

A serious Theme #13-derived charter-preparation draft is now justified.

The architecture is sufficiently mature to state a coherent work boundary:

> **Incident / Signal Lifecycle + Ecosystem Awareness, independently testable, interoperating through bounded owner-preserving interfaces, with conformance/test material that does not become the semantic owner.**

The principal constraint is no longer lack of architecture. It is **sequencing and absorption**:

- keep the first work programme bounded;
- finish the UC #6 worked mapping before adding another conceptual layer;
- let the UC #4 executable profile consume reviewed semantics rather than invent them;
- preserve enough room for Ward/Nelson/#16 contributors and other semantic owners to review at their own pace;
- use 05 as the target and 05A as the current admission boundary; and
- add later cases/profiles only when they expose a genuinely distinct interface or falsifier.

Accordingly, the recommended state is:

**Theme #13 + UC #4 + 00/04 architecture + 05 ideal target + 05A current-state filter → living 01G charter draft → bounded shared mapping/test evidence → targeted Theme/co-chair review → Phase 2 Charter PR only when ownership and packaging are ready.**
