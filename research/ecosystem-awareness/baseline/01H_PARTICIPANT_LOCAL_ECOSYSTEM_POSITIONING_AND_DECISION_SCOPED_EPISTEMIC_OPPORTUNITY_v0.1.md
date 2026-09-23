# Annex 01H — Participant-Local Ecosystem Positioning and Decision-Scoped Epistemic Opportunity

**Status:** additive public working annex, v0.1, 21 September 2026. This document is outside the controlled/frozen v0.4 release baseline. It does not create F10, a new O/S interface family, a new epistemic position, a new operating posture, an implemented protocol, an adopted standard or an ITU-T deliverable.

**Reading boundary:** this annex reconciles and makes explicit mechanisms already distributed across the Ecosystem Awareness corpus: individual adaptation and multi-optima control architecture, signalling without required cooperation, partial participation, competing objectives, Semantic Window management, APQ/F9 pathway learning, EHD handoff semantics and the EA↔MSCA boundary. It does not claim those antecedents as newly invented here.

## 1. Purpose, neighbours and non-ownership boundary

Ecosystem Awareness does not require a shared ecosystem state, common objective, central awareness service or mandatory signalling mesh. Each independently governed participant may maintain and requalify a bounded local epistemic position from the observations, handoffs, applicable authority, owner-defined objectives and constraints, dependencies and finite capacity available to it.

This annex makes that distributed reading explicit. It does **not** claim participant-local situation awareness, selective information sharing, adaptive observation, context engineering or value-of-information reasoning as new. Direct neighbours include [Distributed Situation Awareness](https://doi.org/10.1080/00140130600612762), [Value of Information](https://www.nist.gov/publications/value-information-and-decision-pathways-concepts-and-case-studies), and [Knowledge Gradient](https://doi.org/10.1287/ijoc.1080.0314). The candidate EA differential is narrower: explicit composition of decision scope, open residual, A–D epistemic qualification, source/dependency preservation, bounded handoff and targeted requalification under authority, capacity, privacy and useful-response-horizon constraints.

The architecture therefore separates:

- **external semantic owners** — legitimate owners of objectives, mandates, policies, contracts, identity and delegated authority;
- **participant-local representation** — what a participant currently represents about those externally owned objects for one decision;
- **EA qualification** — what that participant can responsibly conclude from its current bounded representation;
- **MSCA assessment** — what local authorized control configuration is supported under the applicable objective and operating assumptions;
- **execution/defence** — actions taken only by a function that already holds legitimate authority.

No EA or MSCA result creates identity, authority, policy, contractual standing or permission to act.

### 1.1 Dependency key for a first-time reader

- **Objective Envelope:** owner-declared outcomes, acceptable ranges and non-compensable constraints applicable to a mission/decision.
- **EHD (Epistemic Handoff Descriptor):** implementation-neutral semantic handoff that preserves the decision-relevant meaning and qualifiers of an ordinary result; it is not a central bus or mandatory wire format.
- **MSCA:** Minimum Sufficient Control Architecture; the separate control-sufficiency line that represents/assesses S/E/C/P/M and never creates authority by itself.
- **APQ:** the existing F2 acquisition-pathway qualification mechanism used to compare whether additional evidence pathways are sufficiently useful for the current decision relative to burden and horizon.
- **F1–F9:** the fixed EA functional architecture; this annex does not add a tenth function.

### 1.2 Plain-language reading key

A participant asks, for a declared receiving decision:

1. What objective, mandate, policy or participation conditions appear applicable here?
2. What ecosystem state is actually represented for that decision?
3. What situated state is being asserted, with what confidence/intensity, what could still be established with current capability, and what remains structurally residual?
4. Would obtaining or exchanging more information materially improve the decision before cost, privacy, capacity or time remove the option to act?
5. Does the current control configuration remain supportable?
6. What bounded state, limitation or requalification request should be handed to another participant or owner?

This is participant-local reasoning. Different participants may answer differently without implying that one global brain exists.

## 2. Participant-local ecosystem position

For participant i, decision d and time t, use participant indices when locality would otherwise be ambiguous:

- U_i(d,t) — bounded represented universe used by participant i;
- W_i(d,t) — active decision-scoped Semantic Window selected from the represented/observable state available to i;
- R_{U_i} — open decision-relevant residual relative to U_i;
- A/B/C/D — the canonical four-component qualified epistemic position: situated scope/assertion (A), confidence/intensity (B), recognized current-capability frontier (C), and structural/residual unknown (D), interpreted relative to the participant's active decision/window;
- Q_i(d,t) — participant-local qualified operating-frame assessment for the declared receiving decision and scope.

When this annex refers to F6 **systemic** assessment, systemic means composition across the domains and dependencies material to the declared receiving decision and scope. It does not denote one global ecosystem state, universal knowledge or a global posture.

The base symbols Ω, U, R_U and W(d,t) retain their canonical meanings. The participant index is a locality clarification, not a new ontology. The current A/B/C/D reconciliation is owned by the [Canonical Architecture Topology](./00_CANONICAL_ARCHITECTURE_TOPOLOGY.md#2-four-component-qualified-epistemic-position); this annex does not create a competing definition.

A participant may also hold **local, versioned references or representations** of:

- an applicable Objective Envelope;
- identity/principal bindings;
- delegated authority or role/capability state;
- policy, contract or participation-profile versions;
- material dependencies;
- response and human capacity;
- relevant MSCA representation.

Those representations do not transfer ownership. If applicability, version, precedence or standing cannot be established, the state remains qualified, unresolved or UNKNOWN rather than becoming self-issued authority.

A newly instantiated participant may begin with an empty or nearly empty represented state, no external handoffs and no populated MSCA fields. EA treats that emptiness explicitly rather than assuming a shared default state. As soon as any local representation, constraint, memory, authority reference or observation exists, it is qualified as participant-local and may remain partly UNKNOWN or UNPOPULATED.

## 3. Optional and resource-bounded epistemic signalling

External epistemic signalling is optional.

A participant may operate with:

- no external signalling;
- one fixed peer;
- a small trusted or task-specific set;
- a broad mesh;
- receive-only behaviour;
- emit-only behaviour;
- asymmetric participation that changes over time.

In this annex, **epistemic signalling** means emitting or receiving a bounded, attributed claim or handoff relevant to a decision. A signal is not a command, consensus vote, authority grant, compliance certificate or global-truth assertion.

Signalling consumes resources. Sending, receiving, verifying, correlating and disclosing handoffs can consume communication, compute, latency, useful response time, privacy/disclosure budget, human review capacity, trust-establishment effort and adversarial-exposure budget.

More signalling is therefore not intrinsically better. Consistent with the preserved signalling lineage, its value is positive only when the expected decision benefit exceeds verification, disclosure, communication, latency and manipulation costs for the receiving decision.

The receiver remains independently governed. It may trust, distrust, weight, corroborate, reject or ignore a signal according to its own legitimate logic and available evidence.

When an external EHD/signalling peer or channel is used as an acquisition pathway, the existing F9 pathway-learning discipline applies: a participant may retain scoped evidence that the route was useful, stale, redundant, costly, misleading or independently informative for a stated decision/context/time profile, but repeated success must not become a portable global trust score for the peer or channel.

Partial participation is an ordinary condition, not an exception. The architecture must remain meaningful when some participants refuse to signal, disclose minimally, disappear, free-ride or operate under incompatible objectives.

## 4. Semantic Window redirection and decision-scoped epistemic opportunity

The existing F2 operation to **expand, refresh, redirect or narrow** W(d,t) is retained.

Here, **redirect** does not imply a geometric centre. It means changing which actors, dependencies, domains or acquisition pathways are admitted to or prioritized within W_i(d,t), or changing the selection basis used to construct the next window.

A participant may compare candidate epistemic actions such as observing or re-observing a source; requesting, receiving or verifying a handoff; sending a bounded handoff to a peer; acquiring a different evidence pathway; redirecting attention toward another material dependency/domain; or requesting targeted requalification from an external owner.

### 4.1 Decision-Scoped Epistemic Opportunity

**Decision-Scoped Epistemic Opportunity** is the working term for a participant-local ordering or value estimate over admissible epistemic actions.

A candidate action a has higher epistemic opportunity for participant i when it is expected to improve material support for the current decision relative to its acquisition/signalling burden, source dependence, authority constraints, privacy cost, finite capacity and useful response horizon.

This working concept is related to Value of Information and Knowledge Gradient prior art. It is **not** claimed in v0.1 to require a differentiable vector field, convergence process or globally optimal policy. The later [Objective-Conditioned Agentic Gradient Law](../../../architectural-contributions/ecosystem-positioning/01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md) reconciles this working ordering into a generalized finite-difference gradient: expected reduction in objective-conditioned MSCA risk after projecting a qualified ecosystem/regime delta, while preserving non-fungible A/B/C/D structure. This annex remains the participant-local/epistemic precursor; it does not create a competing gradient definition.

The concept is advisory, not coercive. A participant may ignore the highest-ranked epistemic action because its policy or objective favours another action, authority does not permit it, the relevant resource is unavailable, it is competitive/adversarial/non-cooperative, or it is programmed only to relay information or follow instructions.

EA does not overwrite the participant's programming, utility function, identity or authority.

## 5. Sparse or empty MSCA representation and the EA↔MSCA boundary

This annex distinguishes an **MSCA representation/schema instance** from an **MSCA sufficiency determination**.

For participant i, let X_i = (S_i, E_i, C_i, P_i, M_i), where, for interchange/discovery purposes, each component may be represented as a qualified value, UNKNOWN or UNPOPULATED. X_i follows the canonical MSCA notation; the symbol X avoids collision with A, which is already a component of the canonical EA qualified-position tuple.

Keep assessment status separate:

UNASSESSED | SUPPORTED | FAILED | UNRESOLVED.

An all-UNPOPULATED X_i is a valid schema/representation instance with status UNASSESSED. It is **not** a supported minimum and makes no sufficiency claim.

This allows a participant to expose that it uses the MSCA structure even when it has not yet established the applicable Objective Envelope, operating assumptions, coordination reach, intervention mechanisms or enabling means.

The ownership boundary remains:

- legitimate owners supply or authorize applicable S, mandates and non-compensable constraints;
- EA qualifies the local ecosystem/decision frame;
- MSCA assesses candidate control configurations against applicable S/E and legitimate authority;
- F2 owns the Semantic Window.

MSCA may return changed observation/signalling means, coordination reach, response capacity or candidate control configuration. Those outputs may cause **F2** to requalify, expand, narrow or redirect W_i(d,t). MSCA does not itself own or modify the Semantic Window.

Where material to downstream interpretation, an EHD may carry a versioned reference to an MSCA representation/profile or a bounded decision-relevant delta. A full MSCA export is not a universal handoff requirement.

## 6. EHD emission, reception, lineage and anti-self-confirmation

Each participant may emit an EHD or equivalent bounded handoff derived from its own qualified state.

The receiving participant consumes that handoff only for its own receiving decision and scope. It does not convert the producer's local result into ecosystem-wide truth.

EHD exchange does not imply broadcast, reciprocal signalling, consensus, common objectives, a common Semantic Window, a common MSCA or transfer of authority.

### 6.1 Candidate conformance rule — lineage preservation

When a participant re-emits a claim derived materially from received handoffs, material upstream lineage or known source dependence must remain reconstructible through the applicable profile/qualifiers.

Repeated forwarding, aggregation or local recomposition does not create independent corroboration.

A participant's earlier output cannot become independent external evidence merely because it returns through another route in the mesh.

Where material, an EHD may reference an applicable Objective Envelope/version, policy/participation-profile version, operating-frame version, MSCA representation/profile, or relevant authority/grant reference. These remain source-owned objects and are not added to the universal EHD kernel by this annex.

## 7. Local adaptation across Normal, Containment and Migration / Regime Transition

The three canonical top-level postures remain unchanged and decision/scope indexed.

### Normal

Normal does **not** mean immobility. The current frame remains sufficiently supported for the declared decision, while the participant may refresh or redirect W_i(d,t), change acquisition/signalling pathways, alter observation burden, re-assess its local MSCA, or preserve/ignore external handoffs according to local decision value.

### Containment / Mitigation

Containment reduces exposure, autonomy or action scope while preserving or attempting to restore a known workable frame. It may combine narrower action scope with wider or more targeted observation in an affected domain, stronger corroboration, reduced delegation/actuation, or requests for external authority/requalification.

Containment is an assessment/posture, not an automatic command.

### Migration / Regime Transition

Migration / Regime Transition applies when the current frame can no longer be relied on sufficiently for the declared decision and a new frame must be qualified. It may preserve invariant/safety behaviour while reducing reliance on the current representation and qualifying alternative dependencies, policies, control configurations or a new W_i(d,t).

No claim is made that the destination frame is already known, safe, authorized or globally shared.

## 8. Research boundaries and falsifiable extensions

This annex assumes neither shared goals nor benevolent cooperation.

Participants may be cooperative, competitive, opportunistic, free-riding, deceptive, adversarial, passive relays, deterministic executors or human-supervised systems with little autonomy.

The architecture does not claim that every participant implements EA or MSCA; more signalling always improves outcomes; local updates converge to one shared epistemic state; a global optimum exists or is found; ecosystem-wide consensus is required; or a participant's locally represented Objective Envelope is self-authored.

Candidate future tests should compare, under matched resource budgets: no external signalling; bilateral signalling; small-mesh signalling; broad-mesh signalling; honest/cooperative, correlated, free-riding and adversarial participation; complete versus sparse/empty MSCA representations; and static versus redirected Semantic Windows.

Useful measures include decision error, false closure, residual preservation, source-dependence error, useful response margin, signalling/verification burden and preservation of legitimate unaffected workflows.

The claim under test is bounded: qualified signalling and local requalification may improve decision support under some ecosystem conditions. Negative and no-difference results remain valid outcomes.

## 9. Source lineage and neighbouring work

Read this annex with:

- [Article II — Minimum Control Architecture / Multi-Optima](./ARTICLE_02_MINIMUM_CONTROL_ARCHITECTURE_MULTI_OPTIMA.md), including Level-1 individual adaptation;
- [Article IV — Ecosystem Signalling Without Required Cooperation](./ARTICLE_04_ECOSYSTEM_SIGNALLING_WITHOUT_REQUIRED_COOPERATION.part01.md) and [part 2](./ARTICLE_04_ECOSYSTEM_SIGNALLING_WITHOUT_REQUIRED_COOPERATION.part02.md);
- [03 — Functional Architecture](./03_FUNCTIONAL_ARCHITECTURE_v0.4.part01.md);
- [04 — General Functional Interfaces & Agentic Security](./04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md);
- [01B — EA / MSCA interface](./01B_EA_MSCA_INTERFACE_ANNEX_v0.2.md);
- [01I — Agentic Citizenship Contract](./01I_AGENTIC_CITIZENSHIP_CONTRACT_HUMAN_GOVERNED_PARTICIPATION_PROFILE_v0.1.md).

Neighbouring prior art includes Distributed Situation Awareness, Value of Information, Knowledge Gradient, context engineering, adaptive observation and established multi-agent communication research. This annex does not claim those primitives as inventions of EA.
