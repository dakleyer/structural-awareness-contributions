# Minimum Sufficient Control Architecture (MSCA) — Canonical Architecture

**Status:** canonical public working architecture, v0.1, 23 September 2026.

**Canonical role:** this document defines the current generic MSCA architectural kernel, its semantic invariants and its extension contract. It supersedes no historical submission or source paper. It is not an adopted ITU-T architecture, recommendation, production certification, implementation API or proof of a universal/global minimum.

**Corpus entry:** [Minimum Sufficient Control / MSCA](./README.md)

## 1. Purpose

Minimum Sufficient Control Architecture asks:

> **Which authorized control configuration is sufficient to keep an owner-declared Objective Envelope supportable under the current operating conditions, and which supported alternative carries the lowest justified burden among those actually assessed?**

“Minimum” does not mean smallest software stack, weakest control or least data in the abstract. It means **no more control burden than is justified by the declared objective, operating assumptions, uncertainty, authority and response conditions**.

MSCA is therefore a **minimum modular reference architecture**. Its canonical core is intentionally small. Domain-specific control models, governance contracts, signalling protocols and implementation technologies may be substantially richer than the core, provided they remain compatible with its semantics.

The architecture does not require one globally optimal configuration. More than one configuration may be sufficient under the same Objective Envelope and different local conditions, resource allocations or operational histories.

## 2. Canonical kernel — S / E / C / P / M

For participant or system i, decision or mission d and time t, the canonical MSCA representation is a versioned structure:

~~~text
X_i(d,t) = [ S, E, C, P, M ]
~~~

The symbol **X** is used for an MSCA representation/configuration. Older research lineage may use A or other symbols; those are not canonical because **A** is reserved by Ecosystem Awareness for the sufficiently-determined epistemic position.

| Element | Canonical meaning | Architectural boundary |
|---|---|---|
| **S — Objective Envelope** | Owner-declared outcomes, acceptable ranges, hard/non-compensable constraints, relevant trade-off limits and mission/service viability conditions. | MSCA represents and assesses S; it does not self-author or silently relax S. |
| **E — Operating assumptions / environment** | The material conditions under which a sufficiency claim is intended to hold: demand, dependencies, infrastructure, staffing, information quality, actors, applicable regime, time/horizon and other material conditions. | A configuration supported under E1 is not automatically supported under E2. |
| **C — Coordination scope** | Which actors, flows, resources or domains can be observed, coordinated, directly controlled or legitimately influenced, including reach and coverage gaps. | Connectivity does not imply coordination reach, mandate or authority. |
| **P — Intervention mechanisms** | Feasible actions available to maintain, recover, contain, migrate, reconfigure or otherwise influence the objective, with preconditions, latency, reversibility and required authority. | Feasibility is not permission. |
| **M — Enabling means** | Observation, communication, interoperability, computation/processing where material, human/external capacity, actuation and independent effect-measurement capabilities that make C/P usable. | Technology is represented by capability and evidence, not by one mandatory stack. |

S/E/C/P/M are **semantic slots**, not five mandatory software components. The earlier working-note category “response conditions” is retained as cross-cutting binding/operation metadata — thresholds, authority, timing, escalation and return/requalification conditions — rather than promoted to a sixth canonical kernel element.

## 3. Representation is not sufficiency

An MSCA instance may be complete, partial, sparse or empty.

Each material field may be:

- populated with a qualified value;
- **UNKNOWN** — material but currently unresolved/not established;
- **UNPOPULATED** — the representation slot exists but no value is currently supplied for that participant/profile.

An all-UNPOPULATED X is a valid schema instance. It makes no sufficiency claim.

Assessment state is separate:

~~~text
UNASSESSED | SUPPORTED | FAILED | UNRESOLVED
~~~

- **UNASSESSED** — no sufficiency determination has been established for the declared scope.
- **SUPPORTED** — available evidence supports the candidate configuration for the declared S/E conditions, scope, version and time.
- **FAILED** — evidence establishes that the candidate does not satisfy one or more required conditions.
- **UNRESOLVED** — available evidence is insufficient to establish either support or failure for a material condition.

UNKNOWN, UNPOPULATED and UNRESOLVED MUST NOT be silently converted to SUPPORTED.

A representation may therefore be useful for discovery, interoperability, planning, signalling or comparison before it is sufficient for operational reliance.

### 3.1 Qualified MSCA position over S/E/C/P/M

MSCA also exposes a **qualified position** over its own control architecture. This does not replace X=[S,E,C,P,M] and does not create a second control schema. It applies the common EA A/B/C/D qualification form to the MSCA representation.

For an MSCA instance X_i(d,t):

~~~text
Π_MSCA,i(d,t) = [ A_X, B_X, C_X, D_X ]
~~~

where:

- **A_X — situated control scope / represented architecture:** the current S/E/C/P/M scope actually represented for this participant/decision, including version, locality/domain, effective assumptions and material provenance;
- **B_X — confidence / directional support:** the strength and direction of evidence supporting the current MSCA position or a proposed change. This may include confidence/bounds on the current sufficiency claim or on a detected movement away from it. It does **not** replace the separate UNASSESSED/SUPPORTED/FAILED/UNRESOLVED assessment state;
- **C_X — recognized current-capability frontier:** control/configuration information or alternatives that the participant could still establish, test or activate with its current sensing, computation, coordination, authority-request, human-review or other available capabilities, but has not yet established for the current decision;
- **D_X — control residual:** control-relevant state, dependencies or alternatives outside the current represented/recognized-obtainable capability boundary, including compatibility or domain-extension residual where material.

This makes an MSCA position **partial by design**. The system can know exactly which control architecture it currently represents without claiming that its control landscape is complete.

A high B_X means strong support **inside A_X**. It does not eliminate C_X or D_X.

### 3.2 Mechanical alignment with a Regime Awareness delta

Where Regime Awareness supplies a qualified directional change/delta using the same A/B/C/D form, MSCA does not need a separate abstract “gradient algorithm” merely to discover whether the change is relevant.

The first architectural operation is a bounded projection:

~~~text
Δ_RA
→ bind affected scope/dependency
→ project onto [S,E,C,P,M]
→ compare with Π_MSCA
→ classify impact
~~~

The minimum impact classes are:

- **inside A_X:** the regime delta intersects currently represented S/E/C/P/M assumptions or capabilities; the affected MSCA support claim may require reassessment;
- **inside C_X:** the delta points toward a recognized state/capability/configuration that could be determined or activated with current capability; this creates a candidate requalification or repositioning path;
- **into D_X:** the delta reaches beyond the current control-capability representation; the system must preserve the residual and may need discovery, signalling, human/owner input, a new extension/profile, containment or migration rather than fabricate a configuration;
- **not materially coupled:** the delta is qualified but no represented dependency connects it to the current MSCA decision; no control change follows merely from observing change elsewhere.

The **direction and confidence carried in B_RA** determine the strength of the local change pressure. A large, well-qualified directional delta creates a stronger candidate gradient than a weak/noisy delta, but it still does not authorize action.

Only after this mechanical alignment do ACC/admissibility, authority/delegation, burden, timing and sufficiency determine which candidate transition may actually be pursued.

This is the architectural bridge to the pending **MSCA Control Positioning** and **Canonical MSCA Operation** documents. Those future documents will specify transition mechanics and lifecycle in detail; this section fixes the shared representation and matching rule.

## 4. Canonical architecture layers

The minimum architecture contains five logical layers. They may be implemented together or separately.

### 4.1 Objective and frame binding

Binds the MSCA instance to:

- S and its legitimate owner;
- E and its evidence/version;
- decision/mission scope;
- time horizon / expiry;
- material dependencies;
- applicable extension profiles;
- authority owner references.

This prevents a control claim from floating free of the conditions under which it was assessed.

### 4.2 Control representation

Represents C/P/M and their limits, including:

- current reach;
- available mechanisms;
- capability/means;
- preconditions;
- latency and reversibility;
- capacity/burden;
- known gaps;
- UNKNOWN / UNPOPULATED state.

### 4.3 Sufficiency assessment

Evaluates one or more candidate configurations x=(C,P,M) against S and E and returns a scoped assessment state.

It may produce:

- one supported candidate;
- several supported alternatives;
- only failed candidates;
- unresolved candidates;
- no assessed candidate.

MSCA does not fabricate a minimum when no supported candidate has been established.

### 4.4 Extension compatibility

Loads and binds compatible domain, capability, signalling or normative extensions without redefining the kernel.

The extension mechanism is part of the canonical architecture because the minimum core is intentionally smaller than many real deployments.

### 4.5 External authorization and execution boundary

Authorization, dispatch, enforcement and physical/digital actuation are **not created by MSCA assessment**.

A supported configuration may be refused by the legitimate authority. A permit may expire. Execution may fail. A receipt may arrive without the intended effect.

Therefore:

~~~text
MSCA sufficiency ≠ authority/permit ≠ execution ≠ measured effect
~~~

MSCA preserves the references and preconditions needed to join these records without collapsing them into one object.

## 5. Sufficiency region, multi-optima and burden

Let X be the available design/configuration space. For declared S and E:

~~~text
F_sufficient(S,E) = { x in X | x is SUPPORTED for S under E }
~~~

This is a conceptual feasible sufficiency region, not a claim that all possible configurations can be enumerated.

There may be multiple supported configurations. Different participants may occupy different supported configurations because they have different:

- coordination reach;
- intervention options;
- communication/sensing capability;
- human capacity;
- response latency;
- switching cost;
- privacy/security burden;
- redundancy;
- local ecosystem conditions.

A candidate may be preferred among supported alternatives because it has lower justified burden, but the architecture does not require one scalar cost function or one global optimum. Non-compensable constraints remain non-compensable.

The historical multi-optima article remains research lineage; its earlier configuration notation is not the canonical S/E/C/P/M schema.

## 6. Canonical invariants

Any implementation or extension claiming compatibility with this MSCA architecture must preserve the following invariants.

1. **Objective ownership:** S remains externally/legitimately owned; MSCA cannot self-author or silently relax it.
2. **Condition binding:** support is always conditional on E, scope, version and time.
3. **Representation/assessment separation:** having fields does not establish sufficiency.
4. **UNKNOWN preservation:** missing or unresolved material state is not converted to support.
5. **Authority separation:** technical feasibility or sufficiency does not grant permission.
6. **Effect separation:** dispatch/receipt does not establish measured outcome.
7. **Partial validity:** one domain/field/configuration may be supported while another remains unresolved.
8. **No global-minimum claim:** a tested supported set does not prove a universal optimum.
9. **Qualified external evidence:** external signals enter assessment only after applicable semantic/epistemic qualification.
10. **Extension non-redefinition:** an extension may add semantics, constraints and structure but may not silently redefine S/E/C/P/M.
11. **Versioned lineage:** material source, version, scope, freshness and invalidation conditions remain reconstructible.
12. **Targeted invalidation:** material change invalidates dependent claims, not automatically every unrelated MSCA state.

## 7. Extensibility model

MSCA is intentionally extensible because its canonical kernel is smaller than the control, governance and communication structures required by many real systems.

An extension can be richer than MSCA. Compatibility means that the extension can be **bound to the MSCA kernel without changing the canonical meaning of the kernel**.

Four extension directions are canonical.

### 7.1 Downward extensibility / sparse compatibility

A smaller, legacy or low-capability implementation may expose only part of S/E/C/P/M.

Examples:

- a telemetry component may contribute only M-observation capability and a bounded E observation;
- a simple controller may expose P and M but leave broader C unknown;
- a newly instantiated participant may expose an all-UNPOPULATED representation.

Absent material remains UNKNOWN or UNPOPULATED. The receiver may use a verified compatibility profile to enrich receiver-local qualification, but may not invent unsupported state.

Downward compatibility therefore permits participation without requiring every device to implement the complete MSCA model.

### 7.2 Upward structural extensibility

A richer architecture may refine canonical elements into deeper structures.

Examples:

- nested Objective Envelopes beneath S;
- multiple operating assumptions and dependencies beneath E;
- actor/resource/flow graphs beneath C;
- intervention libraries, preconditions and fallback chains beneath P;
- sensing, compute, communication, human capacity, signalling, actuation and effect-measurement subprofiles beneath M.

A richer extension remains compatible only while the parent S/E/C/P/M meaning is preserved.

### 7.3 Horizontal / domain extensibility

A domain profile may specialize the architecture for urban systems, mobility, manufacturing, cloud operations, healthcare, finance, logistics or another bounded environment.

The domain changes the vocabulary, resources, controls and evidence.

It does not change what S, E, C, P and M mean.

A domain profile has exceeded the boundary of MSCA if it can only be represented by redefining the core semantics rather than extending them.

### 7.4 Normative / contractual extensibility

A governance or participation contract may extend MSCA with constraints and obligations that are much richer than the minimum control kernel.

The principal current example is the **Agentic Citizenship Contract (ACC)**.

The pure architectural relation is:

> **ACC is a separate semantic/governance object that may be loaded into a participant's MSCA as a normative extension profile once compatibility is established. It is not an MSCA subset, and MSCA does not subsume ACC's full semantics.**

This resolves two requirements simultaneously:

- ACC retains independent semantic ownership of membership, participation, obligations, prohibitions, lineage, governance and signalling duties;
- MSCA gains a formal way to apply those constraints to its control representation and sufficiency assessment.

An ACC may therefore be **strictly richer** than the MSCA instance it extends.

## 8. ACC as a normative MSCA extension

The canonical lineage/identity/authority binding for this extension is defined in [ACC Lineage, Identity & Authority Binding Profile](./01_ACC_LINEAGE_IDENTITY_AUTHORITY_BINDING_PROFILE.md). This architecture section defines the coupling; the companion profile defines how root, lineage, subject binding, mutation authority, validity and successor continuity are represented.

### 8.1 Extension mapping

A compatible ACC may affect MSCA through the following bindings.

| ACC / governance content | MSCA binding or effect |
|---|---|
| Applicable Objective Envelope references; hard/non-compensable constraints | Constrain or reference **S**; never silently rewrite owner-defined S. |
| Domain, membership scope, effective time, applicability conditions | Qualify **E** and the applicability of the MSCA instance/profile. |
| Role eligibility, participation scope, interaction boundaries | Constrain or refine **C**. |
| Permissions, prohibitions, autonomy bounds, required escalation paths | Constrain admissible **P** candidates; permission still does not equal an authority grant. |
| Signalling duties, evidence/accountability requirements, attestation/communication requirements, resource/control-budget references | Add required or conditional capabilities/constraints to **M** and to the evidence contract. |
| Identity, principal, delegation, grant chain, trust-anchor references | Remain external authority/identity objects referenced by the MSCA operation; they are not converted into S/E/C/P/M values merely to force a mapping. |
| Revocation, suspension, supersession, expiry | Become invalidation/requalification triggers for affected MSCA claims. |
| Conflict/precedence owner or rule | Determines how overlapping normative extensions are resolved where legitimately defined; MSCA does not invent precedence. |

### 8.2 Compatibility before loading

An ACC MUST NOT become active in an MSCA instance merely because it is syntactically available.

A normative extension passes through a compatibility sequence:

~~~text
ACC/profile discovered
→ identity/version/source bound
→ MSCA extension compatibility check
→ mapping of constraints/references to S/E/C/P/M + external authority references
→ unmapped material semantics preserved
→ applicability / precedence qualification
→ COMPATIBLE | BOUNDED_COMPATIBLE | INCOMPATIBLE
→ only then load/bind to the active MSCA instance
~~~

A compatible mapping does not prove that the ACC is legitimate, applicable or truthful. Those claims still depend on legitimate governance, identity/authority and EA qualification where relevant.

### 8.3 Compatibility states

A normative extension may be represented as:

- **COMPATIBLE** — material semantics needed by the current decision can be bound without material loss.
- **BOUNDED_COMPATIBLE** — a usable subset can be bound, while explicit residual/unmapped semantics remain.
- **INCOMPATIBLE** — the extension would require redefining core MSCA semantics or the intended material meaning cannot be responsibly mapped.
- **STALE / EXPIRED / SUPERSEDED** — a previously compatible binding is no longer current.

BOUNDED_COMPATIBLE does not mean “almost compliant.” It means the system knows the boundary of the mapping and preserves the residual.

### 8.4 Extension is not inheritance

ACC should not be modelled as “MSCA plus a few extra fields.”

It may contain semantics that MSCA does not own at all: institutional membership, legal/policy lineage, rights-like permissions, duties, revocation logic, conflict ownership, identity references, delegation chains and specialised signalling contracts.

The relation is therefore **composition by extension**, not class inheritance or subset membership.

MSCA only needs enough of that richer object to:

- determine applicability;
- constrain S/E/C/P/M where appropriate;
- preserve external authority references;
- determine whether the active control configuration remains assessable/sufficient;
- trigger requalification when the extension changes.

## 9. Signalling and protocol extensions

Communication itself is also extensible.

Generic Ecosystem Signalling or an EHD-equivalent handoff may carry a versioned MSCA reference or only the bounded decision-relevant delta. The referenced MSCA object remains source-owned and is not added to the universal EHD/signalling kernel.

Generic Ecosystem Signalling may carry:

- partial MSCA representations;
- bounded S/E/C/P/M deltas;
- capability/coverage state;
- burden/latency state;
- assessment state;
- normative-extension references;
- authority/delegation references.

An ACC may require a specialised signalling contract. Legacy devices may use unrelated telemetry protocols. Both are acceptable if the receiving participant can establish a bounded compatibility mapping.

The generic rule is:

~~~text
signal
→ compatibility mapping
→ receiver-local epistemic qualification
→ bounded normalized state
→ eligible MSCA evidence
~~~

Transport success is not evidence sufficiency.

A compatibility mapping may be preloaded, negotiated, discovered from a registry, inferred from protocol characteristics or proposed by a reasoning component such as an SLM. A discovered/synthesised mapping remains provisional until adequately validated for its intended use.

Any uncertainty introduced by translation remains explicit as a compatibility/capability residual.

## 10. Extension profile contract

A reusable MSCA extension/profile SHOULD declare at least:

- profile ID and version;
- base MSCA architecture version;
- extension class: downward / upward / horizontal / normative / combined;
- owner/source;
- intended domain and scope;
- effective time / expiry;
- S/E/C/P/M mapping;
- external objects deliberately not mapped into S/E/C/P/M;
- mandatory versus optional fields/constraints;
- UNKNOWN / UNPOPULATED semantics;
- compatibility state and residual;
- required evidence / provenance;
- authority or trust-anchor references where relevant;
- invalidation / requalification triggers;
- conflicts/precedence rule or explicit absence thereof.

An extension profile MAY define richer internal schemas. It MUST preserve the canonical kernel semantics at its boundary.

## 11. Relationship to neighbouring architecture

### 11.1 Ecosystem Awareness

EA qualifies what a participant can responsibly rely on for the current decision and retains A/B/C/D epistemic position, source dependence, residual and useful response limits.

EA may provide qualified evidence to MSCA and may consume partial/UNASSESSED/SUPPORTED/FAILED/UNRESOLVED MSCA state.

EA owns the Semantic Window W(d,t). MSCA may change means/capability that justify changing W(d,t), but does not own or directly modify it.

The EA healthy postures **Normal / Containment / Migration-Regime Transition** remain EA epistemic-management/posture semantics. MSCA may represent the control capabilities needed to execute an authorized containment, migration or reconfiguration, but those postures are not redefined as canonical MSCA assessment states.

Current candidate boundary: [EA ↔ MSCA interface 01B v0.2](../../research/ecosystem-awareness/baseline/01B_EA_MSCA_INTERFACE_ANNEX_v0.2.md).

### 11.2 Regime Awareness

Regime Awareness qualifies whether the operating representation/regime remains compatible with observed conditions.

A regime change may invalidate E or another dependency behind an MSCA support claim. It does not itself select or authorize a new control configuration.

Current candidate same-operation composition: [01D EA / MSCA / RA](../../research/ecosystem-awareness/baseline/01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md).

### 11.3 Agentic Citizenship Contract

ACC remains a separately owned governance/participation object, but its **operational coupling to control sufficiency is through the normative-extension mechanism defined here**.

Current working ACC profile: [01I Agentic Citizenship Contract](../../research/ecosystem-awareness/baseline/01I_AGENTIC_CITIZENSHIP_CONTRACT_HUMAN_GOVERNED_PARTICIPATION_PROFILE_v0.1.md).

### 11.4 Ecosystem Signalling

Ecosystem Signalling provides selective disclosure and compatibility-normalization across native, legacy and specialised signalling profiles.

Current working signalling architecture: [01J Ecosystem Signalling](../../research/ecosystem-awareness/baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md).

### 11.5 Identity / delegated authority / execution

These remain external semantic/operational owners.

MSCA may reference their state, require them as preconditions and be invalidated when they change. It does not create them.

## 12. Architecture versus operation versus control positioning

This document defines **architecture**, not the complete runtime protocol.

The following are intentionally separate canonical artefacts:

- **Canonical MSCA Architecture — this document:** objects, invariants, extension rules and boundaries.
- **Canonical MSCA Operation — pending:** lifecycle for declare → represent → qualify → assess → compare → select → authorize → execute → measure → requalify.
- **MSCA Control Positioning — pending:** representation of the participant's current location relative to supported configurations, gaps, available transitions, burden, switching cost, authority constraints and response horizon.

This document may state required boundaries for operation/positioning but does not pre-empt their full semantics.

## 13. Source profiles and provenance

The canonical architecture is a reconciliation of existing public working material. The following remain source/provenance or application artefacts rather than alternative definitions of MSCA:

1. [Architectural and standards working context](./ARCHITECTURE_AND_STANDARDS_CONTEXT.md) — original architectural question and dimensions.
2. [FG-AI4SSC input FGAI4SSC-I-097](../../submissions/itu-fg-ai4ssc/FGAI4SSC-I-097/README.md) — public standards contribution establishing Minimum Sufficient Control as an architectural property for AI-enabled urban systems; posting is not adoption.
3. [Minimum Sufficient Control Architecture working paper](https://tegrity.ai/minimum-sufficient-control-architecture-for-ai-enabled-urban-systems/) — urban/smart-city source architecture and illustrative handoffs/staged assessment.
4. [Article II — Minimum Control Architecture / Multi-Optima](../../research/ecosystem-awareness/baseline/ARTICLE_02_MINIMUM_CONTROL_ARCHITECTURE_MULTI_OPTIMA.md) — research lineage for feasible sufficiency regions and burden trade-offs; its older notation is non-canonical.
5. [EA ↔ MSCA interface 01B v0.2](../../research/ecosystem-awareness/baseline/01B_EA_MSCA_INTERFACE_ANNEX_v0.2.md) — current candidate cross-boundary mapping.
6. [01H Participant-Local Ecosystem Positioning](../../research/ecosystem-awareness/baseline/01H_PARTICIPANT_LOCAL_ECOSYSTEM_POSITIONING_AND_DECISION_SCOPED_EPISTEMIC_OPPORTUNITY_v0.1.md) — sparse/empty participant-local MSCA representation lineage.
7. [01I Agentic Citizenship Contract](../../research/ecosystem-awareness/baseline/01I_AGENTIC_CITIZENSHIP_CONTRACT_HUMAN_GOVERNED_PARTICIPATION_PROFILE_v0.1.md) — normative/governance extension source.
8. [01J Ecosystem Signalling](../../research/ecosystem-awareness/baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md) — signalling/compatibility source.
9. [DAOS extensibility case](../../submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/README.md) — adjacent model case demonstrating upward/downward/horizontal extension discipline; not an MSCA deployment result.

Smart-city, DAOS, ACC and future domain profiles are **examples/extensions of the architecture**, not competing definitions of the architecture.

## 14. Conformance and falsification surface

A candidate implementation/profile should fail MSCA compatibility if any of the following is required for it to work:

- redefining S/E/C/P/M rather than extending them;
- treating UNKNOWN/UNPOPULATED/UNRESOLVED as SUPPORTED;
- allowing a sufficiency verdict to create authority;
- treating permit as evidence that E is current;
- treating dispatch receipt as measured effect;
- silently discarding material compatibility residual;
- loading a normative extension before compatibility/applicability qualification;
- allowing a richer profile to silently relax a non-compensable constraint;
- carrying a support claim across a material E/version/authority change without requalification;
- claiming a global minimum from a bounded candidate set.

Positive conformance to these architectural rules does **not** by itself establish that a deployment is safe, sufficient, optimized or validated.

## 15. Canonical thesis

MSCA is a **small, extensible control-sufficiency kernel**.

Its minimum semantics are S/E/C/P/M plus explicit representation state, sufficiency assessment and extension compatibility. Real deployments may be much richer.

The architecture remains stable by requiring richer systems to extend rather than redefine the kernel.

That permits:

- simple legacy systems to participate through sparse/compatible representations;
- rich domain architectures to refine the control model;
- different industries to reuse the same sufficiency semantics;
- normative contracts such as ACC to be loaded as richer constraints after compatibility is established;
- specialised signalling protocols to contribute qualified evidence without becoming the definition of MSCA.

The result is not a universal controller. It is a bounded reference architecture for determining whether the control available to a participant is sufficient for the objective, conditions and authority that actually apply.
