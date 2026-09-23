# Ecosystem Awareness — Functional Interfaces & Agentic Security Integration — v0.4

## Companion interface model to the fixed F1–F9 Functional Architecture

&nbsp;

# Status and purpose

This document defines the external functional interfaces required by the Ecosystem Awareness architecture. The nine internal functions F1–F9 remain the fixed functional set. v0.4 preserves O1–O6 and IF-S1–IF-S13 exactly as the interface taxonomy, preserves the v0.2 risk/sensitivity and finite-capacity qualification, and adds the validation-gated acquisition-pathway/profile semantics required by F2.APQ. No O7, IF-S14 or new mandatory producer family is introduced. `IF-S#` is an unambiguous namespace prefix only; it does not change any interface family, payload or ownership boundary.

Status boundary. This is an internal working architecture and research object. It is not an adopted standard, a standards-body deliverable, an endorsement or an implementation claim.

&nbsp;

&nbsp;

The model is technology-neutral. It deliberately aligns with common agentic architecture patterns and independently governed system boundaries, but it does not assume that every deployment contains every component.

&nbsp;

The bilateral Theme-specific mappings are maintained separately in “Ecosystem Awareness — Provisional Cross-Theme Interface Contracts — v0.4”. Those contracts are discussion artifacts derived from this interface model; they do not modify O1–O6 or IF-S1–IF-S13 unless later Use Case/testbed evidence exposes a real interface gap.

&nbsp;

# 1\. Architectural rule — no epistemic super-controller

Ecosystem Awareness is not a central brain and does not reconstruct the complete internal reasoning of every agent.

&nbsp;

Each subsystem remains responsible for its domain function. Ecosystem Awareness consumes only the minimum information necessary to understand what that subsystem is claiming epistemically: what domain the claim concerns, the observation/context boundary supporting it, what was determined, what remains indeterminate, what additional state is recognised as potentially obtainable, what structural residual is acknowledged, how any uncertainty statement should be interpreted, and what relevant provenance, freshness, dependency or capacity qualifiers apply.

&nbsp;

The subsystem need not expose prompts, chain-of-thought, proprietary decision logic, complete memory, complete context or a universal numeric uncertainty score.

&nbsp;

Missing information is not silently reconstructed. If a producer cannot state its window, coverage, method, independence or residual treatment, the corresponding qualifier remains unknown.

&nbsp;

The design objective is distributed epistemic legibility, not centralized epistemic recomputation. Ecosystem Awareness is subject to the same rule: every EA output must carry its own assessed scope/coverage, known exclusions, unknown qualifiers and material residual limitations rather than presenting a projected assessment as ecosystem-wide truth.

&nbsp;

Profile/result versus EA qualification. A producer capability profile, local verdict, Attestation Result, population assessment or signalling-mechanism description is an input evidence object. EA’s scope-indexed qualification is a distinct consumer-side assessment. The same separation applies to acquisition mechanisms: Pathway Capability Profile ≠ EA Pathway Qualification. EA therefore does not convert a self-description, attestation or successful prior use into a global certification of the pathway.

&nbsp;

How to read an interface. Every interface follows one pattern: the surrounding capability produces bounded state or evidence → EA consumes only what is available and leaves missing material qualifiers UNKNOWN → EA qualifies/composes that state through F1–F9 → EA returns a scoped assessment or requalification request → the surrounding capability retains ownership of its own semantics and action.

&nbsp;

Relationship map. Producer result/profile → EHD / decision-relevant handoff → F3/F4/F5 → EA scope-indexed assessment. Pathway Capability Profile (optional) → F2.APQ → decision-relative pathway sufficiency qualification. Profile evidence is never itself the EA qualification, and no profile is required for passive/non-cooperative acquisition.

&nbsp;

# 2\. Common Epistemic Handoff Descriptor

**Current A/B/C/D reconciliation — 23 September 2026.** This integrated interface document retains the frozen v0.4 source lineage, but current reader-facing A/B/C/D semantics follow the [Canonical Architecture Topology](./00_CANONICAL_ARCHITECTURE_TOPOLOGY.md#2-four-component-qualified-epistemic-position): A = situated assertion/scope; B = confidence/intensity; C = recognized current-capability frontier; D = structural/residual unknown. Earlier determined/unresolved wording is preserved only as source lineage, not as a competing current tuple.

Emission-side obligation. The Epistemic Handoff Descriptor does not create a third epistemic control family. A producer remains responsible for applying the internal controls to its own state; the handoff obligation is to preserve the decision-relevant qualifiers needed for downstream interpretation. Where a qualifier cannot be established, it remains UNKNOWN rather than being fabricated. Missing qualification creates downstream Type-2 exposure, not automatic Type 2; the failure materializes only when an intermediary or receiver promotes the missing or bounded qualification into greater determination than was supplied.

EHD exchange does not imply broadcast, reciprocal signalling, consensus or a common ecosystem view. A participant may emit without receiving, receive from one or several peers, or operate without external epistemic signalling.

Where material, a handoff may carry a versioned reference to an applicable Objective Envelope, participation/citizenship profile, operating-frame version or local MSCA representation/profile, or only the bounded decision-relevant delta. These referenced objects remain source-owned and are not added to the universal EHD kernel.

When a claim is re-emitted after material dependence on received handoffs, the applicable mapping/profile must preserve material upstream lineage or source dependence. Forwarding, aggregation or local recomposition does not create independent corroboration.

# 

Any component that emits a decision-relevant certainty, uncertainty, closure, verdict, assessment or recommendation should be able to attach an Epistemic Handoff Descriptor (EHD) at the abstraction level appropriate to the receiving decision.

&nbsp;

The EHD is not a mandatory wire format. It is the common semantic contract that Ecosystem Awareness needs to consume.

&nbsp;

Efficiency and deployment rule. The EHD is a semantic metadata overlay on an existing result, not a requirement to ship a second full message, full context or full history on every claim or hot-path interaction. An implementation may separate a stable, versioned Producer Epistemic Profile from a small Decision-Relevant Handoff delta. The profile may describe stable claim semantics, available qualifier fields, coverage model, uncertainty/evidence vocabulary, observed-versus-derived policy, provenance/source-relationship semantics and default validity rules; the per-handoff delta binds the operational result to the current action/interaction and carries only material instance-specific qualifiers or deviations. A profile identifier and version are sufficient at the semantic level; cryptographic binding is used only where the applicable trust model requires it.

&nbsp;

Decision-scope projection. A handoff or EA output need carry only the domains material to the receiving decision rather than an ever-growing history of all upstream domains. Projection must preserve material coupling, known exclusions and unresolved coupling as UNKNOWN; projected-out state must not silently become independent, irrelevant or determined.

&nbsp;

Conditional-field rule. A qualifier is required when its absence can change the relying decision or make the claim materially ambiguous. For example, freshness/as-of is material for time-dependent claims whose staleness can alter reliance, but need not be collected universally for time-invariant propositions. The descriptor remains partial by construction: conformance means honest declaration of available and unavailable qualification, not complete population of every possible field.

&nbsp;

Irreducible interoperability kernel. To avoid every implementation selecting a mutually incompatible subset, an EHD intended for cross-component interoperability should expose at least six semantic elements, each of which may itself contain an explicit UNKNOWN where the producer cannot establish the value: (1) producer-profile reference and version, or an inline-equivalent semantic/profile identifier when no separate profile artifact is used; (2) subject/proposition/decision-domain together with the scope to which the statement applies; (3) producer/issuer; (4) operational result/closure; (5) determination state; and (6) an explicit unknown-qualifier declaration identifying material qualification that was not established. This is a parseability/interoperability minimum, not a completeness claim. Freshness, observed-versus-derived status, evidence class, window-selection basis, capacity, dependency/coupling and other fields remain conditional when they are material to the relying decision. A producer that cannot establish scope does not omit the element; it carries scope = UNKNOWN.

&nbsp;

Core fields extending the interoperability kernel

- subject / proposition / decision domain: what the statement is about;

- scope: the population, subsystem, geography, time horizon, action, policy domain or other bounded area to which the statement applies;

- producer / issuer: which agent, human, verifier, service or subsystem issued the statement;

- operational result / closure: what the producer decided or emitted;

- determination state: determined, indeterminate, fallback, held or an implementation-equivalent state;

- uncertainty statement: the reported uncertainty/confidence, if any, together with its semantics; a number without semantics is not sufficient;

- as-of / freshness: when the supporting state was valid or observed;

- unknown qualifiers: qualifiers the producer cannot establish and therefore explicitly leaves unknown.

&nbsp;

Window-qualification fields

- window / observation-boundary descriptor: the relevant context or evidence boundary used for the statement, at an abstraction level that does not require disclosure of the private window;

- window-selection basis: why that boundary was considered sufficient for the task, e.g. mission relevance, policy scope, evidence class, coverage rule, criticality, ecosystem sensitivity/exposure, consequence severity, reversibility, tolerated residual, observation/determination burden, response horizon or bounded stopping rule;

- included scope and known exclusions;

- validity interval or revalidation condition;

- coverage statement where meaningful;

- expansion capability: known evidence, sources or context that could in principle be brought into the window if further determination is justified;

- residual statement: what the producer acknowledges cannot be presumed exhaustively known or enumerated.

&nbsp;

Four-component qualified epistemic position

Where the producer can express it, the EHD should make legible:

A — situated assertion/scope: what is represented or asserted, where/from which frame and under which material qualifiers;

B — confidence/intensity: how strongly A is supported within that admitted frame;

C — recognized current-capability frontier: additional decision-relevant state that could still be established with current observation, review, acquisition or computation capability;

D — structural/residual unknown outside the represented and recognized-obtainable capability boundary.

&nbsp;

A producer is not required to have a perfect enumeration of C or D, nor one universal numeric B. The key requirement is that missing qualification does not silently collapse into an unscoped or overconfident A assertion.

&nbsp;

Uncertainty-method fields

When a producer reports confidence or uncertainty, it should identify enough of the interpretation to prevent category error:

- whether the value is probability, model confidence, calibration score, qualitative class, evidence sufficiency, disagreement, residual estimate or another construct;

- the proposition and window/scope to which it applies;

- the method, evaluator, threshold, policy or reference identifier when one exists;

- known calibration or applicability limits when material;

- whether the value is direct, inherited or aggregated from upstream sources.

&nbsp;

Dependency and capacity fields

Where material:

- provenance/source class;

- direct versus inherited evidence;

- source independence or shared-source dependency where known;

- unresolved upstream dependencies;

- human, compute, evidence, authority or time capacity binding;

- observation/determination burden or capacity consumption where material to deciding whether further awareness is proportionate;

- source/producer relationship such as self, contracted or independent where relevant to interpretation.

&nbsp;

## Composition-Critical EHD Profile (optional)

The EHD kernel remains sufficient for ordinary bounded handoff. This optional profile applies only when several components must preserve the basis, continuity or arbitration of the **same material decision** across handoffs: for example, a principal-bound decision basis, a transition from commitment to execution, competing directives over one resource-time segment, or a later requalification of an earlier decision. It introduces no O7, IF-S14, producer family or mandatory wire format.

The profile is a conditional metadata overlay. References may be stable identifiers, versioned semantic references or privacy-preserving record references; they do not require full context, private reasoning or a common global database. If a material relation cannot be established, it remains UNKNOWN rather than being inferred.

Producer → EA fields, where material:

- decision/operation reference and, where a handoff continues an earlier result, parent-handoff or predecessor reference;

- decision-basis reference and version for the relevant principal preference, hard limit, mandate or permitted trade-off;

- commitment state, such as recommendation, negotiation, reservation, binding commitment or execution, or an implementation-equivalent state;

- source-owned validity, review, transition or return condition, including normal versus exceptional path qualification where supplied by its owner;

- shared dependency or resource-time reference, and competing-directive references where the same material action or resource is affected;

- source-owned priority, precedence, veto or arbitration reference where a legitimate owner has supplied one.

EA → receiving function fields, where material:

- the same decision/operation reference and affected scope;

- the qualified residual, capacity, authority or evidence limitation relevant to that decision;

- a targeted re-entry reference: the assumption, evidence, window, dependency, authority or policy/reference that must be refreshed, widened, narrowed or otherwise requalified;

- review/expiry condition and the identified receiving function that retains the authority to decide or execute;

- expected outcome or revalidation criterion, without treating the request itself as execution confirmation.

The profile provides the links needed to test preservation and re-entry. It does not carry KPIs, Q0–Q5 dispositions, quality gates, a universal precedence hierarchy or an EA command. Those remain test, governance or owner-specific artifacts outside the runtime handoff.

&nbsp;

The descriptor may be partial. “Unknown” is a valid value. Silent substitution is not. Where the reason for an unknown is itself known, producers should preferably preserve it (for example not observed, not tracked, unavailable, privacy-restricted, unsupported or not established); the reason itself may remain UNKNOWN. `not_applicable` is separate because it is a determination, not an unknown state.

&nbsp;

Risk/capacity allocation fields are conditional rather than universal producer requirements. Ecosystem sensitivity/exposure, consequence severity, tolerated residual and observation/determination budget normally originate from the mission/context side through O1/F1. A Theme-specific producer should carry such fields only when it actually owns or observes them, for example human-capacity state from IF-S6, measurement burden from IF-S7 or response capability from IF-S12.

&nbsp;

# 3\. Baseline functional landscape

The external architecture is divided into an Operational Agent Plane and a Trust & Security Plane. Ecosystem Awareness interfaces with both but owns neither.

&nbsp;

## Operational Agent Plane

O1 Mission / Objective / Orchestration

O2 Agent Discovery & Capability Description

O3 Agent Runtime / Worker / Model Execution

O4 Context, Memory, State, Retrieval & Research

O5 Tool / Resource Access & Action Execution

O6 Task, Message, Artifact & Inter-Agent Transport

&nbsp;

Trust & Security Plane

Namespace rule. `IF-S1–IF-S13` denotes Functional Interface families in this document. `CH-S#` denotes preserved DAOS challenge identifiers in cross-layer maps. `REQ-S1–REQ-S14` denotes the canonical solution challenges in [00 — Canonical Requirements](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md). No Interface `IF-S14` is created.

IF-S1 Identity, Authentication & Principal Binding

IF-S2 Provenance of Authority, Delegation & Authorization

IF-S3 Remote Attestation & Runtime / Interaction Assurance

IF-S4 Policy / Intent Expression & Runtime Conformance

IF-S5 Evidence Appraisal & Verifier-Side Failure Semantics

IF-S6 Human Oversight & Intervention Capacity

IF-S7 Observability, Telemetry, Evaluation & Drift

IF-S8 Accountability, Attribution & Verifiable Action Records

IF-S9 External / Population-Level Evaluation

IF-S10 Privacy & Minimum Disclosure

IF-S11 Ecosystem Signal / Incident Exchange & Defence

IF-S12 Enforcement, Containment, Revocation, Recovery & Migration

IF-S13 Trust Framework / Assurance Mapping / Jurisdictional Context

&nbsp;

Optional domain profiles such as embodied-system binding or model-level trust can extend these interfaces without changing the core architecture.

&nbsp;

# 4\. Operational Agent Plane interfaces

&nbsp;

## O1 — Mission / Objective / Orchestration

Generic role

Defines the task, workflow, objective, execution graph, dependencies, criticality and termination/continuation conditions. It may be a planner, manager agent, workflow engine or decentralized handoff structure.

&nbsp;

Inputs to Ecosystem Awareness

- mission/task identifier and objective;

- material decision/output domains;

- criticality/stakes and reversibility;

- ecosystem sensitivity/exposure and consequence severity by material domain where available;

- tolerated residual / decision-risk tolerance where defined;

- available observation/determination budget or capacity constraints at the orchestration level;

- expected workflow or dependency graph at the needed abstraction level;

- deadlines/time horizon;

- available fallback/containment/recovery/migration capabilities;

- current task state and material changes to the workflow;

- relevant authority/policy references.

- decision/operation reference and commitment state where the workflow moves from recommendation, negotiation or reservation to commitment or execution;

- principal preference, hard-limit or permitted-trade-off reference and version where it materially defines the decision basis;

- source-owned review, transition or return condition where a material change can distinguish normal revalidation from an exceptional governed path.

&nbsp;

EA outputs to this function

- qualified operating posture from F6;

- affected domains/dependencies;

- domain-targeted requalification directives from F7;

- requests to alter scope, pause boundedly, re-evaluate or change the observation frame;

- epistemic statement explaining what remains determined/indeterminate for orchestration purposes;

- current window-selection / sensitivity-capacity mismatch where observation effort is materially too high or too low for the receiving decision.

- where the Composition-Critical EHD Profile applies, the decision/operation reference, targeted re-entry reference and review/expiry condition.

&nbsp;

Internal EA functions

F1, F6, F7, F9.

&nbsp;

Boundary

The orchestrator remains responsible for workflow execution. EA does not choose every next action.

&nbsp;

## O2 — Agent Discovery & Capability Description

Generic role

Allows a client or orchestrator to discover an agent/service and learn its declared identity, capabilities, skills, endpoints and authentication requirements. A2A Agent Cards are a current protocol example.

&nbsp;

Inputs to Ecosystem Awareness

- discovered agent/service identifier;

- capability/skill claims;

- endpoint/interface information;

- authentication requirements;

- declared version/capability changes;

- discovery source and freshness;

- any provenance or trust metadata supplied by the discovery mechanism.

&nbsp;

EA outputs to this function

- required additional qualification before relying on a capability;

- request for refreshed capability/discovery information;

- reduced reliance/scope if capability evidence is stale or epistemically weak;

- external epistemic envelope where the discovery layer can carry extensions.

&nbsp;

Internal EA functions

F2, F4, F7, F8, F9.

&nbsp;

Boundary

Discovery tells the system what a participant declares itself able to do. It does not by itself establish that the capability is safe, authorized, current or epistemically sufficient.

&nbsp;

## O3 — Agent Runtime / Worker / Model Execution

Generic role

Executes domain reasoning or work using one or more models, instructions, tools and local state.

&nbsp;

Inputs to Ecosystem Awareness

- operational result/closure;

- EHD or equivalent local epistemic state;

- model/runtime identity or version where material;

- local determination/indeterminate state;

- uncertainty semantics and method/reference where available;

- unresolved dependencies;

- local capacity-binding state;

- local scope/window descriptor and selection basis;

- inherited upstream uncertainty.

&nbsp;

EA outputs to this function

- targeted re-evaluation request for the same domain;

- request to preserve INDETERMINATE/fallback rather than force certainty;

- request for a different evidence class or genuinely independent source;

- scope/window adjustment request;

- bounded stop condition when continued re
asoning becomes Type 1\.

&nbsp;

Internal EA functions

F3, F5, F7, F9.

&nbsp;

Boundary

EA does not rerun the worker’s complete domain reasoning. It qualifies what the worker’s output justifies.

&nbsp;

## O4 — Context, Memory, State, Retrieval & Research

Generic role

Provides documents, working/long-term memory, persisted session or checkpoint state, retrieved resources, search results, vector retrieval, external research or other context used by agents. MCP resources, agent-session stores and agentic retrieval systems are current examples.

&nbsp;

Inputs to Ecosystem Awareness

\- available source/resource classes;

\- retrieved evidence identifiers and scope;

\- provenance/source relationship where available;

\- freshness/cache state;

\- session/checkpoint/persistent-state identity, version and resumability where used;

\- retrieval/search bounds and stopping criteria;

\- retrieval/search latency, compute/token, bandwidth, monetary or other resource burden where available and decision-material;

\- coverage or known exclusion information where available;

\- source-dependency/duplication indications;

\- access limitations or unavailable sources.

&nbsp;

EA outputs to this function

\- widen/narrow/redirect window request;

\- request a specific missing evidence/source class;

\- request primary-source retrieval;

\- request independent corroboration rather than more copies of the same source;

\- stop, narrow or redirect condition for unbounded or low-value search;

\- observation-budget or marginal-value bound where supported by the retrieval/research function;

\- refresh request where staleness invalidates the current frame.

&nbsp;

Internal EA functions

F2, F3, F4, F7, F9.

&nbsp;

Boundary

Retrieval increases accessible context; it does not prove that the resulting window is the ecosystem or that additional search will eliminate structural residual.

&nbsp;

## O5 — Tool / Resource Access & Action Execution

Generic role

Exposes callable tools, APIs, services, files, databases or actuators and executes actions. MCP tools and ordinary enterprise APIs are examples.

&nbsp;

Inputs to Ecosystem Awareness

\- tool/resource identity and declared function;

\- action request/result/status;

\- decision/operation and predecessor-handoff reference where the action continues a material decision;

\- read/write/reversibility and material impact characteristics where available;

\- authorization scope and relevant policy/mandate reference;

\- error/failure/partial-completion state;

\- side-effect confirmation or indeterminate execution outcome;

\- latency/availability/capacity state;

\- provenance of returned data where available.

\- shared resource-time segment and competing operation/directive reference where the action can collide with another legitimate action.

&nbsp;

EA outputs to this function

\- request to delay or restrict tool use while a specific domain is requalified;

\- request for read-only, reduced-scope or reversible operation when posture requires it;

\- request for outcome reconciliation when execution status is indeterminate;

\- containment/scope-reduction request sent to the function that actually owns enforcement.

\- where the Composition-Critical EHD Profile applies, the targeted re-entry reference and expected revalidation criterion; this is not an execution command.

&nbsp;

Internal EA functions

F1, F2 where the tool/API is an acquisition pathway, F3, F6, F7, F9.

&nbsp;

Boundary

EA does not grant tool authority. Authorization and enforcement remain separate.

&nbsp;

## O6 — Task, Message, Artifact & Inter-Agent Transport

Generic role

Carries messages, tasks, task status, artifacts, streaming updates and extensions between agents or services. A2A is a current protocol example; other transports may be used.

&nbsp;

Inputs to Ecosystem Awareness

\- message/task/artifact identity and status;

\- sender/receiver or interaction binding available at the transport layer;

\- decision/operation correlation and parent-handoff reference where the message continues or changes a material decision;

\- timestamps/freshness;

\- extension metadata carrying an EHD or external epistemic envelope;

\- delivery/update state;

\- task completion, cancellation, auth-required or other relevant lifecycle state.

&nbsp;

EA outputs to this function

\- Epistemic Envelope from F8 for transport alongside the ordinary operational result;

\- updated scope/freshness qualifiers;

\- requalification or correction signal where the transport supports amendments/status updates.

\- Composition-Critical EHD Profile fields, where material, so that the receiving function can correlate the decision basis, conflict relation or targeted re-entry without interpreting a transport identifier as sufficient semantic identity.

&nbsp;

Internal EA functions

F4, F8, F9.

&nbsp;

Boundary

Transport preserves and conveys information. It does not determine the truth of an epistemic statement.

&nbsp;

# 5\. Trust & Security Plane interfaces

&nbsp;

## IF-S1 — Identity, Authentication & Principal Binding

Generic role

Establishes who/what is interacting and, where relevant, the binding between agent/runtime/interacting system and the human or organization behind it. Authentication proves control of credentials; legal or operational principal binding may be a separate function.

**Standards boundary.** SPIFFE/SPIRE is a representative workload-identity and authentication mechanism; its own documentation explicitly leaves authorization policy to separate mechanisms. EA may consume the resulting authenticated identity/binding state, but a valid identity is not silently promoted into authority for a particular action.

&nbsp;

Inputs to Ecosystem Awareness

\- authenticated subject/agent/service identifier;

\- principal/binding claim when available;

\- authentication assurance/context;

\- credential validity/freshness/revocation status;

\- binding scope and validity interval;

\- identity/binding evidence provenance;

\- unknown or contested identity/binding state.

&nbsp;

EA outputs to this function

\- request for refreshed identity/binding evidence when material;

\- explicit treatment of identity/binding state as unknown or insufficient for the affected domain;

\- requalification request when a previously valid binding is stale, changed or contradicted.

&nbsp;

Internal EA functions

F1, F3, F4, F6, F7.

&nbsp;

Boundary

Identity is evidence about the actor/binding; it does not predict behaviour and does not by itself establish authority, conformance or ecosystem truth.

&nbsp;

## IF-S2 — Provenance of Authority, Delegation & Authorization

Generic role

Specifies where authority originated, the grant/mandate, scope, limits, conditions, delegation chain, version and revocation/standing. This aligns with ordinary authorization, delegation and mandate systems.

**Standards boundary.** RFC 8693 is a relevant subject/actor token-exchange mechanism, but the RFC defines exchange as a one-time event without a general tight linkage between input and output tokens; revocation propagation is implementation-, token-type- or deployment-specific rather than a general protocol property. IF-S2 therefore consumes existing delegation/authorization mechanisms rather than replacing them, while preserving current standing/applicability and revocation state explicitly where they are material to the receiving decision.

&nbsp;

Inputs to Ecosystem Awareness

\- principal/grantor and grantee identifiers;

\- authority/grant identifier;

\- mandate/action scope;

\- limits and conditions;

\- applicable authority/mandate reference for a competing directive, including any source-owned exception, veto or precedence rule where one exists;

\- delegation/redelegation chain where material;

\- policy/reference version linked to the grant;

\- validity/revocation state;

\- authority provenance and standing;

\- contested, absent or fuzzy authority state;

\- authority capacity actually reachable for current intervention where relevant.

&nbsp;

EA outputs to this function

\- request to refresh/resolve authority state;

\- indication that authority uncertainty is binding for the current domain;

\- request to narrow action scope to the currently qualified mandate;

\- requalification trigger when the grant/reference/standing materially changes.

&nbsp;

Internal EA functions

F1, F3, F6, F7, F9.

&nbsp;

Boundary

EA consumes authority state. It does not originate a grant or decide legal standing.

&nbsp;

## IF-S3 — Remote Attestation & Runtime / Interaction Assurance

Generic role

Produces evidence about runtime, code/data/policy/model/harness or interaction state; a verifier appraises that evidence and produces an Attestation Result for a relying party. RFC 9334 RATS provides the canonical Evidence → Verifier → Attestation Result architecture.

**Standards boundary.** RATS deliberately keeps Evidence, Verifier appraisal, Attestation Results and the Relying Party's application-specific decision distinct. EA preserves that separation: an attestation result is qualified evidence, not delegated authority and not the authorized operational decision. NIST NCCoE's 2026 software/AI-agent identity-and-authorization concept work further identifies identification, authorization, auditing and non-repudiation as active agent-IAM questions; this is current standards context, not an EA adoption claim.

&nbsp;

Inputs to Ecosystem Awareness

\- Attestation Result, not necessarily raw private evidence;

\- attested subject/interaction and scope;

\- verifier/issuer identity;

\- appraisal result and relevant claims;

\- reference/policy identifiers and versions where material;

\- freshness/nonce/replay status;

\- appraisal relationship such as self/contracted/independent where available;

\- evidence/appraisal limitations;

\- no-assertion/unknown result distinct from action-side indeterminate.

&nbsp;

EA outputs to this function

\- request for re-attestation when freshness or interaction state changes;

\- request for an independent or differently rooted attestation where source dependence matters;

\- reduction of reliance when attestation scope does not cover the claim being made;

\- bounded epistemic envelope for downstream relying-party decisions.

&nbsp;

Internal EA functions

F4, F5, F6, F7, F8, F9.

&nbsp;

Boundary

A valid Attestation Result establishes what the verifier vouches for under its appraisal policy. It is evidence, not universal truth and not an authorization decision by EA.

&nbsp;

## IF-S4 — Policy / Intent Expression & Runtime Conformance

Generic role

Defines the authored policy/intent reference and evaluates an action against it at runtime.

&nbsp;

Inputs to Ecosystem Awareness

\- named/versioned policy or intent reference;

\- provenance/authority under which the reference was authored;

\- evaluated action/task/domain;

\- conformance verdict such as permit, remediate, block, escalate or indeterminate;

\- scope examined for indeterminate;

\- confidence/threshold semantics where used;

\- issuing evaluator/engine identity;

\- issuer relationship to evaluated party where available;

\- freshness/tamper-evidence of the verdict;

\- competing intents/directives, their shared decision or resource-time reference, and the source-owned priority/precedence basis where material;

\- attested absence of evaluation where no evaluation occurred.

&nbsp;

EA outputs to this function

\- request for re-evaluation under a refreshed/current reference;

\- request to preserve indeterminate instead of forcing a binary verdict;

\- indication that verdict scope is insufficient for the system-level claim;

\- request for independent evaluation where the current evaluator is not sufficient for the affected domain.

&nbsp;

Internal EA functions

F3, F4, F5, F6, F7, F9.

&nbsp;

Boundary

A conformance verdict answers whether observed/action behaviour conforms to a reference. It does not establish that the reference was legitimate, that the world model was complete or that the system-level composition is determined.

&nbsp;

## IF-S5 — Evidence Appraisal & Verifier-Side Failure Semantics

Generic role

Checks whether evidence/records/claims are entitled to be relied upon and produces explicit appraisal or rejection outcomes. This aligns with evidence-appraisal patterns such as RATS appraisal.

&nbsp;

Inputs to Ecosystem Awareness

\- appraisal result;

\- rejection/failure class;

\- checks performed or profile/version;

\- subject/record/claim appraised;

\- freshness/replay/integrity result;

\- issuer/relationship/authorization-scope checks where applicable;

\- absence/null semantics where applicable;

\- limitations or checks not performed.

&nbsp;

EA outputs to this function

\- request to appraise a particular upstream claim or evidence class;

\- request for a different appraisal profile where the current one does not cover the epistemic question;

\- preservation of appraisal failure as evidence-side uncertainty rather than silently mapping it to an action verdict.

&nbsp;

Internal EA functions

F3, F4, F5, F7.

&nbsp;

Boundary

Evidence-side failure and action-side indeterminate remain different semantic categories.

&nbsp;

## IF-S6 — Human Oversight & Intervention Capacity

Generic role

Manages escalation, qualified reviewers, human authority, decision rights, intervention records, bounded mandates and return-to-operation conditions.

&nbsp;

Inputs to Ecosystem Awareness

\- human-capacity state: available, binding, unavailable or implementation-equivalent;

\- required reviewer/role and authority;

\- response deadline/window;

\- current escalation/HOLD/intervention state;

\- human decision and scope;

\- intervention mandate/validity where applicable;

\- evidence considered and evidence sufficiency/limitations;

\- intervention outcome/reconciliation state;

\- return-to-operation/revalidation state.

&nbsp;

EA outputs to this function

\- targeted request for human review only for the affected domain;

\- required information/scope that the reviewer must see for the requested epistemic question;

\- indication that human capacity is itself insufficient/unavailable;

\- stop/escalation boundary when repeated human requests become Type 1;

\- system-level posture and requalification requirement for intervention-path selection.

&nbsp;

Internal EA functions

F1, F2 where the human channel is an acquisition pathway, F3, F5, F6, F7, F9.

&nbsp;

Boundary

Human oversight owns human capacity and intervention. EA consumes human-capacity state as one dependency among many. Human approval does not retroactively validate an upstream world model. Repeated escalation, review and evidence requests also consume finite human attention in the extended human-agent system; EA may therefore identify the human channel itself as capacity-binding or Type-1-amplifying without taking ownership of the human decision.

&nbsp;

## IF-S7 — Observability, Telemetry, Evaluation & Drift

Generic role

Emits traces, metrics, logs, operation/tool/model telemetry, anomaly/drift measurements and evaluation results. OpenTelemetry provides current cross-vendor semantic conventions for agent invocation, model calls, retrieval and tool execution.

&nbsp;

Inputs to Ecosystem Awareness

\- observed operation/task/tool/model identifiers;

\- timestamps/duration/status/error state;

\- instrumentation/measurement coverage and observation burden or latency where available;

\- telemetry/evaluation metric and semantics;

\- drift/anomaly indicators;

\- model/runtime/tool version changes;

\- source/measurement method;

\- observation period/population/scope;

\- measurement confidence/limitations where available;

\- expected versus observed outcome.

&nbsp;

EA outputs to this function

\- request for additional instrumentation/measurement on a specific domain or dependency;

\- request for refreshed observation where telemetry is stale;

\- revalidation trigger when drift invalidates window or operating-frame assumptions;

\- target domains for follow-up evaluation;

\- request to increase, decrease or redirect instrumentation when observed risk/sensitivity and observation cost are materially mismatched.

&nbsp;

Internal EA functions

F2, F3, F4, F6, F7, F9.

&nbsp;

Boundary

EA interprets the epistemic significance of telemetry. It does not replace the telemetry or evaluation method.

&nbsp;

## IF-S8 — Accountability, Attribution & Verifiable Action Records

Generic role

Records at action time enough information for a later party to establish who acted, under what authority and scope, and to verify that the record/claims have not been altered.

&nbsp;

Inputs to Ecosystem Awareness

\- actor/agent/interacting system identity;

\- action/task and timestamp;

\- decision/operation and parent-handoff reference where needed to reconstruct a composition-critical path;

\- authority/provenance reference;

\- declared scope;

\- policy/reference identifier/version where present;

\- carried conformance verdict or attested absence;

\- issuer binding, freshness and tamper-evidence for carried claims;

\- attestation linkage where present;

\- action/result/outcome and record integrity state.

&nbsp;

EA outputs to this function

\- bounded Internal/External Epistemic Statement from F8 suitable for being recorded alongside the action where required;

\- scope, posture, residual/inherited-indeterminacy markers relevant to later reconstruction;

\- request to preserve a material requalification/containment/migration decision and its basis.

\- where material, the targeted re-entry reference, review/expiry condition and observed outcome/revalidation link for the same decision/operation.

&nbsp;

Internal EA functions

F4, F5, F8, F9.

&nbsp;

Boundary

The record preserves evidence for reconstruction. It does not itself prove that every recorded claim was substantively true.

&nbsp;

## IF-S9 — External / Population-Level Evaluation

Generic role

Reads many records/measurements to determine what can be concluded at population or evaluator-family scale when single records cannot establish certain claims.

&nbsp;

Inputs to Ecosystem Awareness

\- assessment claim;

\- defined population;

\- observation period;

\- taxonomy/reference/policy and version;

\- per-type rate or other non-composite measurement;

\- evaluator/evaluator-family characteristics;

\- evaluator independence/diversity information where known;

\- sample size and statistical uncertainty where applicable;

\- residual indeterminacy / identifiability limit;

\- statement of what the result is and is not capable of establishing.

&nbsp;

EA outputs to this function

\- request for a population-level assessment when local records cannot resolve a materially relevant hypothesis;

\- request for a different evaluator family or independent channel where correlation matters;

\- qualified use of the population signal within F4/F5 rather than promotion to ecosystem truth.

&nbsp;

Internal EA functions

F4, F5, F6, F7.

&nbsp;

Boundary

Population size can reduce sampling uncertainty but does not automatically remove structural non-identifiability. Population-level evidence remains scope-bound.

&nbsp;

## IF-S10 — Privacy & Minimum Disclosure

Generic role

Controls what identity, authority, context, trust, behavioural, telemetry and audit information each party may learn, retain or disclose. This aligns with standard privacy-preserving design.

&nbsp;

Inputs to Ecosystem Awareness

\- disclosure policy;

\- recipient/role and decision purpose;

\- permitted/forbidden attributes;

\- retention/linkability/correlation constraints;

\- selective-disclosure or pseudonymity capabilities;

\- privacy risk/criticality constraints.

&nbsp;

EA outputs to this function

\- minimum EHD/envelope field set required for the receiving decision;

\- request for a privacy-preserving substitute or coarser abstraction where full disclosure is unnecessary;

\- indication that insufficient disclosure leaves an epistemic qualifier unknown rather than authorizing inference.

&nbsp;

Internal EA functions

F1, F4, F8.

&nbsp;

Boundary

Privacy can legitimately limit what EA learns. The correct consequence is bounded uncertainty, not forced disclosure or assumed certainty.

&nbsp;

## IF-S11 — Ecosystem Signa
l / Incident Exchange & Defence

Generic role

Distributes, amends/corroborates and correlates ecosystem-relevant signals; represents affected scope/blast radius and may feed containment/resolution.

&nbsp;

Optional IF-S11 Ecosystem Signalling Capability Profile. Where a signalling mechanism can expose stable capability semantics, IF-S11 may make available a versioned profile describing signalling properties it declares or that have been externally established. The profile is evidence about the mechanism, not the EA qualification itself. The candidate inventory is grouped below for scanning; the list remains open and each property remains conditional on decision relevance.

&nbsp;

Semantic/coverage — scope/coverage semantics; semantic compatibility.

Provenance/lineage — provenance support; source-lineage visibility.

Temporal — freshness/expiry; availability; response-window compatibility.

Uncertainty preservation — uncertainty/UNKNOWN preservation.

Lifecycle — amendment/correction/resolution support.

Adversarial/participation — adversarial assumptions/protections; participation/membership assumptions.

Cost/exposure — privacy/disclosure burden; latency/verification/communication cost.

&nbsp;

Property-basis rule. Any profile property relied upon by EA retains its epistemic basis where material: declared, observed, attested, independently evaluated, derived or UNKNOWN, or an implementation-equivalent distinction. A declaration by the signalling operator is not silently promoted to an independently established property.

&nbsp;

Profile absence is not failure and does not exclude a pathway. Passive observation, environmental/action traces, public information, regulatory disclosure and other non-cooperative pathways may be qualified through F2.APQ using observed, attested, independently evaluated, derived or UNKNOWN state without any producer-published profile. The architecture therefore does not require participation, cooperative intent or aligned objectives in order to use ecosystem-relevant information.

&nbsp;

Inputs to Ecosystem Awareness

\- observed condition/event/claim;

\- reporter/source and relationship;

\- confidence/uncertainty semantics;

\- freshness;

\- affected/potentially affected scope;

\- provenance/dependency information;

\- corroboration/amendment history;

\- blast-radius/dependency graph where available;

\- containment reach, response deadline and fallback where supplied;

\- adversarial indicators such as replay, Sybil, collusion or false attribution;

\- resolution/correction signal.

&nbsp;

EA outputs to this function

\- qualified External Epistemic Envelope from F8;

\- scope-qualified residual determinacy/capacity state;

\- request to corroborate a particular domain rather than generic reputation increase;

\- request to mark source dependence/unknown provenance;

\- posture/requalification state for downstream containment consumers;

\- indication, where useful, whether additional corroboration/observation is proportionate to the current incident sensitivity, response capacity and response window rather than automatically desirable;

\- where F2.APQ is active, decision-relative indication that the current signalling route is sufficient/insufficient/unresolved for the specific evidence need, or that a materially independent/alternative route would add more value.

&nbsp;

Internal EA functions

F4, F5, F6, F7, F8, F9.

&nbsp;

Boundary

Signal infrastructure carries and correlates claims. EA assesses what those claims justify epistemically. Signal exchange does not create authority. An incident-signal-and-blast-radius mechanism is therefore a concrete IF-S11 peer capability that EA can consume rather than reproduce. EA may also be required when no incident or malicious agent exists—for example, when honest locally correct subsystems remain epistemically fragmented at composition level—so IF-S11 is an important interface, not the semantic boundary of Ecosystem Awareness. EA does not rank or certify IF-S11 mechanisms globally. It qualifies the sufficiency of an available route for a stated decision and preserves the distinction between declared mechanism properties and independently supported properties.

&nbsp;

## IF-S12 — Enforcement, Containment, Revocation, Recovery & Migration

Generic role

Actually enforces authorization/policy and applies operational controls such as restrict, rate-limit, revoke, isolate, quarantine, suspend, rollback, fallback, substitute, recover or migrate/reconfigure.

&nbsp;

Inputs to Ecosystem Awareness

\- available control/response capabilities and effective reach;

\- decision/operation and shared resource-time reference where a response can collide with another legitimate action;

\- authority required for each response;

\- current response latency and actionability window;

\- execution/status/result of containment or recovery;

\- residual exposure and affected scope;

\- rollback/reversibility state;

\- alternate-provider/alternate-frame readiness;

\- migration/reconfiguration status;

\- failure/indeterminate outcome where response execution cannot be established.

&nbsp;

EA outputs to this function

\- scope-indexed Normal / Containment-Mitigate / Migration-Regime-Transition assessment from F6, optionally accompanied by small conditional posture qualifiers derived from already available response state: response-capacity sufficiency, response-window state, frame recoverability and, for Migration/Regime Transition only, transition readiness. Different receiving scopes may legitimately receive different postures. A global posture must not be inferred unless the assessed scope supports one. These are descriptive qualifiers, not new universal subposture states and not enforcement commands;

\- domain-targeted request to reduce autonomy/scope/exposure;

\- request to invoke a known containment mechanism;

\- request to prepare migration/requalification where the old frame is no longer sufficient;

\- success/revalidation criteria for returning to normal operation.

\- where the Composition-Critical EHD Profile applies, the same decision/operation reference, targeted re-entry reference and review/expiry condition so that a containment or migration result can be reconciled with the decision it qualifies.

&nbsp;

Internal EA functions

F1, F6, F7, F9.

&nbsp;

Boundary

EA identifies the epistemic need and target. Enforcement/recovery functions own the actual authority and execution.

&nbsp;

## IF-S13 — Trust Framework / Assurance Mapping / Jurisdictional Context

Generic role

Provides the trust framework, assurance levels, jurisdictional constraints, mutual-recognition/equivalence mappings and governance references under which identity, authority, evidence and interaction are interpreted. This corresponds to ordinary enterprise and government trust frameworks.

&nbsp;

Inputs to Ecosystem Awareness

\- applicable trust domain/jurisdiction;

\- assurance profile/level and semantics;

\- accepted trust anchors/reference frameworks;

\- equivalence/mutual-recognition rules;

\- applicable policy/regulatory constraints;

\- validity/version and change history;

\- unresolved cross-domain incompatibilities.

&nbsp;

EA outputs to this function

\- indication that a cross-domain equivalence is insufficient for a particular decision domain;

\- request for a different assurance profile/reference where needed;

\- residual/unknown treatment when two trust domains cannot be cleanly mapped.

&nbsp;

Internal EA functions

F1, F4, F6, F7.

&nbsp;

Boundary

EA does not create jurisdictional policy or a global trust authority.

&nbsp;

# 6\. Optional domain profiles

&nbsp;

## Embodied-system binding

For robotics/embodied AI, the trust interface may additionally bind logical agent, runtime/controller, physical device and authority. Relevant inputs include binding identity, device/runtime attestation, binding freshness, control-transfer state and physical-action attribution. These specialize IF-S1, IF-S2, IF-S3 and IF-S8 rather than creating a new EA core function.

&nbsp;

## Model-level trust and lineage

Model identity/version, training/lineage claims, adaptation state and model-level assurance can enter through IF-S3 attestation, IF-S7 evaluation/drift and IF-S8 records. A lineage or provenance claim is evidence; it does not by itself establish behaviour.

&nbsp;

## Credential / wallet / secret / confidential execution

Credential vaults, wallets, key stores and confidential-computing mechanisms support IF-S1 identity/authentication, IF-S2 authorization and IF-S3 runtime assurance. EA should consume only their assurance/availability/validity state, never secret material.

&nbsp;

# 7\. Interface completeness against F1–F9

F1 Mission & Decision Context Qualification consumes principally O1, IF-S2, IF-S6, IF-S10, IF-S12 and IF-S13. In v0.2 O1 supplies the mission-side ecosystem sensitivity/exposure, consequence/reversibility and available observation/determination-budget context; IF-S6 and IF-S12 contribute effective human and response capacity.

&nbsp;

F2 Decision-Relevant Window Qualification & Management consumes principally O2, O4, O6, IF-S7, IF-S10 and IF-S11. It combines F1’s sensitivity/risk basis with source availability, retrieval/instrumentation burden, privacy limits and freshness to maintain W(d,t). When F2.APQ is invoked, IF-S13 contributes assurance/trust-framework context where material; O5 contributes direct tool/API/resource pathway state when a tool or API is itself the acquisition path; and IF-S6 contributes human-channel availability/information-scope/response-window state when human reporting or review is itself the acquisition path. Equivalent pathway descriptions may be mediated through O2/O4/F1, but the mediation remains explicit. No new O/S family is required.

&nbsp;

F3 Local Epistemic State Qualification consumes principally O3, O4, O5, IF-S4, IF-S5, IF-S6 and IF-S7.

&nbsp;

F4 External Epistemic Signal Qualification consumes principally O2, O6, IF-S1, IF-S3, IF-S4, IF-S5, IF-S8, IF-S9, IF-S11 and IF-S13.

&nbsp;

F5 Scope-Indexed Epistemic Composition & Coupling Assessment consumes all qualified local/external states and especially dependency/provenance information from IF-S2, IF-S3, IF-S8, IF-S9 and IF-S11.

&nbsp;

F6 Systemic Epistemic & Operating-Frame Assessment consumes F5 plus mission/criticality and ecosystem-sensitivity/exposure from O1/F1, observation/determination burden from F2/O4/IF-S7, human capacity from IF-S6, response capability from IF-S12 and applicable trust-frame assumptions from IF-S13.

&nbsp;

F7 Requalification & Corrective Directive Generation targets O1, O3, O4, O5, IF-S1–IF-S7, IF-S9, IF-S11, IF-S12 and IF-S13 according to the affected domain. It does not broadcast generic “add control” requests.

&nbsp;

F8 Epistemic Statement & Envelope Generation publishes through O6, IF-S8 and IF-S11, subject to IF-S10 privacy/minimum-disclosure constraints.

&nbsp;

F9 Outcome Feedback & Revalidation consumes O3/O5 execution results, IF-S6 intervention outcomes, IF-S7 telemetry/evaluation, IF-S8 records, IF-S11 resolution/correction signals and IF-S12 containment/recovery/migration outcomes.

&nbsp;

No interface requires one central component to observe every raw event. Implementations may place F1–F9 centrally, distribute them, embed subsets beside subsystems or execute them through cooperating services, provided the epistemic semantics survive the handoffs.

&nbsp;

# 8\. Minimum viable interface set

A deployment does not need all external functions in order to implement Ecosystem Awareness. The minimum viable set is the smallest set that can support the active mission.

&nbsp;

For a simple local agent, the minimum may be:

\- O1 mission/orchestration context, including enough sensitivity/exposure, consequence/reversibility and finite capacity information to calibrate the required awareness burden;

\- O3 local output \+ EHD;

\- O4/O5 context and tool state where used;

\- IF-S2 authority state where actions are delegated;

\- IF-S7 outcome/telemetry;

\- IF-S12 available response capability.

&nbsp;

For an interoperating multi-agent security system, the minimum expands to include:

\- O2/O6 discovery and task/message transport;

\- IF-S1 identity/authentication;

\- IF-S2 authority provenance;

\- IF-S3 attestation where runtime assurance matters;

\- IF-S4 conformance verdicts;

\- IF-S5 appraisal semantics;

\- IF-S6 human-capacity state where humans are in the control path;

\- IF-S8 verifiable records;

\- IF-S10 privacy/minimum disclosure;

\- IF-S11 ecosystem signal exchange;

\- IF-S12 enforcement/containment/recovery.

&nbsp;

IF-S9 population evaluation and IF-S13 cross-domain trust mapping are activated when the problem requires those scales. They are not universal mandatory dependencies.

&nbsp;

F2.APQ may operate over any subset of the existing discovery, context/retrieval, telemetry, transport, signal, privacy and trust-framework interfaces. A dedicated signalling profile is optional and is not a prerequisite for acquisition-pathway qualification.

&nbsp;

# 9\. Non-superpower rule for every interface

Every input to Ecosystem Awareness must be obtainable from an actual producer or remain unknown.

&nbsp;

EA must not assume that:

\- an identity provider knows behaviour;

\- an authority service knows whether an action conformed;

\- an attester knows the truth of every behavioural claim;

\- a verifier knows facts outside its appraisal boundary;

\- a policy engine knows the whole ecosystem;

\- a human reviewer sees the original world rather than the representation presented to them;

\- a telemetry system observes uninstrumented state;

\- an action record proves the truth of every claim it carries;

\- a population evaluator removes structural non-identifiability;

\- a signal reporter represents the ecosystem;

\- an enforcement function knows whether the epistemic basis for its order was correct;

\- a trust framework creates equivalence where none was established.

&nbsp;

When an interface cannot establish a qualifier, Ecosystem Awareness preserves that absence as uncertainty rather than manufacturing a value.

&nbsp;

# 10\. Alignment with current external architectures

**Evidence status — source snapshot: 18 September 2026 (UTC).** The mappings below are **E4 market/standard evidence** in the sense of [00D's evidence-grade definition](./00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md#3-evidence-grades): they support only the documented scope or capability of the named specification, public product/documentation source or external working direction. They do not establish adoption, universal interoperability, interface completeness or EA effectiveness.

Operational plane

Current A2A specifications provide concrete concepts for Agent Cards, discovery, capabilities/skills, authentication requirements, tasks, messages, artifacts, task status and extensions. These fit O2 and O6 directly.

&nbsp;

Current MCP specifications expose resources, prompts and tools, and client-side capabilities such as sampling, roots and elicitation, with explicit authorization and security requirements. These fit O4, O5 and parts of O1/O6.

&nbsp;

OpenTelemetry GenAI semantic conventions increasingly expose agent invocation, model calls, retrieval and tool execution as standardized telemetry operations. These fit IF-S7.

&nbsp;

Trust/security plane

RFC 9334 RATS gives a mature generic architecture for Attester → Evidence → Verifier → Attestation Result → Relying Party, fitting IF-S3/IF-S5.

&nbsp;



&nbsp;



&nbsp;



&nbsp;



&nbsp;



&nbsp;



&nbsp;



&nbsp;



&nbsp;



&nbsp;

Specialized evaluation, embodiment and model/trust mechanisms can provide evidence sources and profiles that can be consumed through the generic interfaces above without changing F1–F9.

&nbsp;

# 11\. Architectural conclusion

The external interface model does not make Ecosystem Awareness a control plane for every agentic function.

&nbsp;

The architecture works by requiring decision-relevant producers to make their epistemic position sufficiently legible at the boundary where their result becomes input to another function.

&nbsp;

A worker says what it concluded and the boundary that supports the conclusion.

A verifier says what it appraised and under what reference.

An attestation service says what it vouches for and its scope.

A human-oversight function says whether qualified human capacity is available and what decision was actually made.

A population evaluator says what a rate can establish and what remains structurally indeterminate.

A signal infrastructure says what was observed, by whom, when and over what affected scope.

An enforcement system says what response capacity exists and what was actually executed.

&nbsp;

Ecosystem Awareness then performs the meta-level task: preserve those distinctions, compose them by domain rather than by average confidence, detect Type 0/1/2 and cross-domain collapse, dynamically calibrate the observation frame to mission sensitivity/risk and finite capacity, requalify that frame where necessary, and emit a bounded epistemic statement that the rest of the system can use.

&nbsp;

# Appendix A — Interface Quality and Conformance Plan for Ecosystem Awareness

## A.1 Status, purpose and scope

**Status.** This is an internal quality and conformance plan for the generic Ecosystem Awareness interface model in this document. It is an additional verification artifact: it does not modify F1–F9, O1–O6, IF-S1–IF-S13, the EHD kernel, the optional Composition-Critical EHD Profile, or any producer's native semantics. It is not a certification scheme, a standards claim, an implementation claim or a quality plan for another architecture.

**Canonicalization note

&nbsp;

This v0.5 integrated document preserves the general O/S interface semantics of the controlled v0.4 source while separating programme-specific mappings from the canonical interface layer. Concrete FG-TIDA Theme mappings, the ideal cross-Theme projection and the current-source-constrained bridge are maintained in the dedicated [EA / FG-TIDA application package](../fg-tida/README.md). The v0.4 split files remain preserved as historical controlled sources and provenance.

&nbsp;

Purpose.** The plan determines, for a declared decision scope, whether the available inputs and outputs of actual generic AI components are sufficient for EA to qualify and return an epistemic result without inventing information, taking another component's authority or losing a material qualifier in handoff. It therefore tests the interface, not whether EA is universally effective or whether a producer's underlying domain decision is substantively true.

**In scope.** A test may involve any active subset of O1–O6 and IF-S1–IF-S13, provided that every input has an identified producer or is explicitly UNKNOWN and every EA output has an identified receiving function. The plan covers two bounded levels:

- **Level 1 — internal coordination and integration.** Mission/orchestration, local runtime, context/retrieval, tools, transport and internal trust/control functions exchange qualified state for one declared decision.

- **Level 2 — independent-boundary information.** EA consumes an externally originating signal, record, assessment or other bounded claim through the same EHD discipline. A Level 2 signal changes the receiver's evidence state; it does not transfer authority, prove the whole ecosystem or force a common action.

For this plan, **independently operated** is assessed relative to the EA/adaptor side: the ICR identifies the producer's operating organisation, the organisation that controls the producer's semantics, and the adapter's authorship/maintenance. A claimed independent boundary requires a distinct producer operation, producer-side semantic control, and an adapter not exclusively authored or maintained by the EA side. If any condition is absent, the ICR records which one and the result is simulated-boundary evidence rather than established independent interoperability.

The Mission/Context Assessment (MCA) remains the basis for deciding before and after a run how much knowledge, retrieval, review or response effort is justified. The plan does not require maximum information collection.

**Out of scope.** This plan does not define a production API, require full internal reasoning or memory disclosure, transmit KPIs, Q0–Q5 dispositions or quality gates in the runtime payload, set a universal policy hierarchy, or execute containment, human intervention or authority decisions.

## A.2 Quality objectives

| Objective | What the plan establishes | What it does not establish |
| --- | --- | --- |
| **Q1 — Boundary ownership** | Each input, output, semantic owner and receiving function is identified. | That EA owns the source function's authority or action. |
| **Q2 — Qualified handoff integrity** | Material scope, provenance/freshness, determination/UNKNOWN state, dependency, capacity, authority and validity/review qualifiers survive where required. | That every possible qualifier is known or universally mandatory. |
| **Q3 — Semantic preservation** | A receiver can interpret the result according to the producer profile/reference and does not confuse observation, attestation, appraisal, verdict, assessment or execution. | That independently implemented components already share one wire format. |
| **Q4 — Bounded disclosure and burden** | The chosen handoff avoids unnecessary private context and records the relevant latency, retrieval, communication and review burden. | That lower overhead is automatically safer or more correct. |
| **Q5 — Correctly bounded EA return** | EA returns a scoped assessment, limitation and targeted requalification to an identified receiver without issuing another owner's command. | That the receiver executed the request or that the request was the best possible action. |
| **Q6 — Composition-critical continuity** | Where the optional profile applies, the decision basis, decision/operation continuity, conflict relation, precedence reference and targeted re-entry remain reconstructible. | A universal precedence hierarchy or a complete history of every upstream system. |
| **Q7 — Revalidation closure** | A material change, execution result or elapsed validity condition can be connected to the affected decision and re-entry point. | That a successful action proves the earlier epistemic basis was complete. |

## A.3 Unit under test: Interface Conformance Record

Every test run creates an **Interface Conformance Record (ICR)**. The ICR is a test artifact, not a new runtime message. It contains:

| ICR element | Required content |
| --- | --- |
| Test identity | ICR identifier, date, interface-model version, profile/delta version and test-vector version. |
| Decision context | Declared subject, proposition, receiving decision, scope, mission/MCA basis, useful horizon and materiality condition. |
| Materiality control | Frozen set of material qualifiers, the semantic owner who fixed it before execution, rationale and version. A later reduction of that set is a recorded change, not a silent improvement in the result. If the semantic owner and adapter/maintenance owner are the same person or organisation, the ICR labels the result **materiality self-declared**. |
| Boundary | Producing component, consuming EA function, receiving component, semantic owner and adapter/maintenance owner. |
| Evaluation independence | Named reviewer for the mapping, plus any relevant relationship to the producer, receiver or adapter. The reviewer of a mapping cannot be that mapping's adapter/maintenance owner. Any unresolved reviewer objection is recorded and blocks a sufficient conclusion. |
| Native result | The producer's native result and the reference/profile through which it is interpreted. |
| Required qualifiers | Which of scope, provenance/freshness, dependency, unresolved state, capacity, authority, validity/review and privacy constraint are material for this run. |
| Unknown treatment | Explicit UNKNOWN, `not_applicable`, unavailable, not-observed, privacy-restricted or other declared reason where known. |
| Test vector | Positive, boundary, rejection or adversarial-assertion fixture; injected change or limitation; expected EA interpretation and expected receiving consequence. |
| Route shape | Level 1 or Level 2 designation; for Level 2, the independent-operation assessment; for a chain, the ordered hops and declared aggregation points before execution; and for an aggregation, input-assertion count and declared transformation or loss. An aggregation later discovered but absent from this declaration is a nonconforming mapping finding. |
| Evidence | Handoff trace, profile/reference, adapter mapping where used, receiving result, observed execution/outcome when available, burden observations and, for a non-deterministic route, repeated-run dispersion. |
| Conclusion | Interface sufficiency finding, open field gap if any, retest decision and responsible maintenance owner. |

For a Composition-Critical test, the ICR additionally records the decision/operation and parent-handoff references, decision-basis reference, commitment state where relevant, shared resource-time or conflict relation, source-owned precedence/arbitration reference where present, and targeted re-entry reference.

## A.4 Entry conditions

A test may start only when the following are declared for its bounded scope:

1. the producer, EA consumer and receiving function are identified;
2. the producer profile/reference and its version are available, or their absence is declared;
3. the native result and the decision it can affect are distinguishable;
4. the material fields and permitted disclosure boundary are specified;
5. the expected result is stated as an interface interpretation or requalification consequence, not as an assumed global truth;
6. the positive, boundary and rejection fixtures have an observable oracle; and
7. the semantic owner and adapter/maintenance owner accept responsibility for the test mapping they control.
8. any material adversarial-assertion fixture has an observable oracle;
9. the semantic owner has fixed the material qualifier set and its rationale before the fixture is executed;
10. a named reviewer, distinct from the adapter/maintenance owner of the mapping under review, is available; and
11. where Level 2 is claimed, the producer is independently operated as defined in A.1, or the fixture is explicitly marked as a simulated boundary that does not establish independent interoperability;
12. the ordered route map and any intended aggregation point are declared in the ICR before execution; and
13. any reviewer objection is resolved, or the fixture is declared unable to support a sufficient conclusion.

Failure to satisfy an entry condition is itself a useful finding: it means the proposed interface cannot yet be tested for that scope without inventing a producer, a receiver, semantics or an oracle.

## A.5 Test method

### A.5.1 Prepare the declared route

1. Select the active interfaces and the relevant EA functions F1–F9.
2. Freeze the decision scope, the available evidence boundary, the useful response horizon, the MCA capacity basis and the disclosure constraint.
3. Identify whether the ordinary EHD kernel is sufficient or whether the Composition-Critical EHD Profile is required.
4. Map native producer fields to the EHD/profile semantics. An adapter may translate representation; it must not silently upgrade UNKNOWN, authority, provenance, independence or determination.
5. Declare the ordered route map, including every intended aggregation point, before execution. A subsequently discovered undeclared aggregation is recorded as a nonconforming mapping rather than normalised into the result.

### A.5.2 Exercise four fixture classes

| Fixture class | Minimum situation | Expected interface result |
| --- | --- | --- |
| **Positive** | A producer supplies the material result and qualifiers within scope and validity. | EA preserves the qualification, returns a scoped assessment or no-change result to the identified receiver, and does not claim more than the producer supplied. |
| **Boundary** | One material qualifier is absent, stale, privacy-restricted, capacity-binding, partly scoped or correlated. | The qualifier remains UNKNOWN/limited; EA narrows reliance, requests targeted requalification or records that the available route is insufficient for the decision. |
| **Rejection** | A mapping would collapse UNKNOWN, extend scope, confuse evidence with authority, treat a transport identifier as semantic identity, or send an EA request as an execution command. | The handoff is nonconforming for that use; the ICR identifies the field, ownership or adapter defect rather than manufacturing a value. |
| **Adversarial assertion** | A producer emits a well-formed material qualifier that is false or unsupported in the controlled fixture, such as independence, freshness or scope. | Without independent contradictory evidence, EA preserves the qualifier as declared rather than established and the ICR records the route guarantee as conditional on producer honesty. Where contradictory independent evidence is supplied, EA preserves the conflict or indeterminacy rather than promoting the assertion. |

Composition-Critical tests add at least one vector for each material condition present: a decision-basis/version change, an execution or commitment transition, competing directives over one resource-time segment, and re-entry after changed evidence, authority, dependency or validity.

Where the route has more than one handoff, the fixture includes at least two intermediate hops and evaluates qualifier preservation, transformation and declared loss at each hop, not only end to end. Where a component aggregates two or more prior assertions, the fixture records the input-assertion count and any declared loss, collapse or change of dependency treatment. An aggregation discovered after execution that was not declared in the route map is a nonconforming mapping. At least one claimed Level 2 route uses an independently operated producer as defined in A.1; a simulated external source is recorded as such and cannot support a claim of established cross-boundary interoperability.

### A.5.3 Evaluate the handoff and return

For each fixture, the reviewer checks:

The named reviewer of an adapter mapping is distinct from that mapping's adapter/maintenance owner; the ICR records any remaining relationship that could affect the review.

An unresolved objection by that reviewer is recorded in the ICR and prevents the run from being concluded sufficient for its declared scope or horizon.

- **Input provenance.** Was every required input produced by the named component and attached to its native/profile semantics?
- **Qualifier preservation.** Did scope, freshness, dependency, capacity, authority, validity/review and UNKNOWN survive the handoff where material?
- **Dependency declaration.** Does each composed input distinguish established independence, known shared dependency, dependency not evaluated, or another stated relation/basis, rather than treating absence of a dependency finding as independence?
- **EA interpretation.** Did EA preserve the distinction between local result, evidence appraisal, systemic assessment, operating posture and execution status?
- **Output ownership.** Did the EA return identify a receiver and stay within assessment/requalification rather than grant, authorize or execute?
- **Re-entry and feedback.** If the vector changes a material condition, does the return identify the exact re-entry target and can the later outcome be associated with the same decision/operation where required?
- **Disclosure and burden.** Did the route remain within the declared disclosure boundary and was its material operational burden observed?

## A.6 Evidence and test measures

These are post-run measures for the ICR. They are not EHD fields, runtime KPIs or automatic release criteria.

| Measure | Calculation or observation |
| --- | --- |
| Field preservation | Material required qualifiers delivered and interpretable at the receiver ÷ material required qualifiers for the declared scope. |
| UNKNOWN preservation | Material unavailable/limited qualifiers still explicit at the receiver ÷ material unavailable/limited qualifiers at the producer. |
| Scope fidelity | Runs in which a receiving conclusion stays within the declared scope, known exclusions and dependency treatment ÷ applicable runs. |
| Semantic mapping integrity | Mappings in which the receiver preserves the producer's result category and profile semantics ÷ mappings exercised. |
| Hop-by-hop qualifier preservation | For every material qualifier in a chained route, the number of hops at which it remains interpretable, explicitly limited or explicitly lost ÷ applicable hops. The ICR reports each hop as well as the end-to-end result. |
| Dependency-declaration completeness | Material composed inputs with an explicit dependency status and stated basis where independence or no dependency is claimed ÷ material composed inputs. `not evaluated` remains distinct from `no dependency detected`. |
| Aggregation transparency | Aggregations in which input-assertion count, dependency treatment and declared transformation/loss remain reconstructible ÷ aggregations exercised. |
| Re-entry traceability | Material changes that produce a specific, reachable re-entry reference and later outcome association ÷ applicable change vectors. |
| Composition continuity | In composition-critical runs, required decision/operation, basis, conflict/precedence and parent-handoff relations retained and interpretable ÷ required relations. |
| Boundedness observation | Relevant latency, retrieval/communication effort, human-review demand and disclosure burden, reported beside the fixture result. |
| Horizon viability | Whether the observed route burden remains usable within the pre-declared MCA capacity basis and useful horizon; recorded as viable, non-viable or indeterminate for that declared route. |
| Non-deterministic route stability | Where any producer, adapter, receiver or material route component is non-deterministic, repeat each applicable fixture and record the run count, outcome distribution and material qualifier/viability dispersion. A single run is not treated as stable evidence. |

The plan records observed burden so that a semantically complete handoff is not accepted blindly when it consumes the response opportunity it is meant to protect. It does not prescribe one universal threshold; the declared mission, scope and MCA capacity basis determine materiality.

Where fewer than five applicable vectors or relations are exercised, the ICR reports numerator and denominator as counts and does not present the resulting percentage as a rate estimate. Counts remain useful evidence; they are not statistical generalisation.

## A.7 Conformance findings

The quality conclusion is made **after** the run. It is not a runtime posture or command.

| Finding | Meaning | Required follow-up |
| --- | --- | --- |
| **Sufficient for declared scope** | The ordinary EHD kernel or active generic interface set preserved every material qualifier and produced an owner-preserving EA return for the fixture. | Retain the ICR and repeat only when version, scope or material assumptions change. |
| **Semantically sufficient, operationally non-viable for declared horizon** | Qualifiers and semantics were preserved, but the observed retrieval, communication, review or disclosure burden is not usable within the pre-declared MCA capacity basis or useful horizon. | Do not accept the route as sufficient for that decision; narrow the scope, change the route/profile or record the decision as limited and retest. |
| **Horizon viability indeterminate** | The available evidence cannot establish whether the route is usable within the declared MCA capacity basis or useful horizon. | Do not accept the route as sufficient for that horizon; retain the limited scope, obtain the missing burden evidence or change the declared route and retest. |
| **Sufficient with Composition-Critical Profile** | The ordinary kernel alone was not enough, but the optional profile preserved the material decision continuity, basis, conflict or re-entry relation. | Version-pin the profile and retain the associated fixtures. |
| **Insufficient field expression** | A material fact exists at a named producer but cannot be expressed or interpreted through the active interface/profile. | Record the smallest candidate field addition, its producer and consumer; retest before changing the baseline. |
| **Producer or receiver unavailable** | The required fact has no available producer, no identified receiving function or no responsible semantic owner. | Preserve UNKNOWN and mark the decision scope limited; do not infer a contract. |
| **Nonconforming mapping** | An adapter, transport or consumer changed scope, meaning, UNKNOWN, authority or ownership. | Correct the mapping or reject the route for that scope; do not patch the result. |
| **Out of declared scope** | The fixture needs a decision, authority, disclosure or execution rule not owned by the tested generic interfaces. | Refer the matter to its legitimate owner; do not expand EA by assertion. |

## A.8 Interface coverage plan

| Interface group | Principal quality question | Minimum evidence |
| --- | --- | --- |
| **O1** mission/orchestration | Is the receiving decision, materiality, capacity basis and decision basis sufficiently declared? | Mission/context record, scope, decision/operation reference where material and EA return. |
| **O2/O6** discovery and transport | Does discovery/transport preserve source, recipient, version and semantic handoff without becoming the truth owner? | Capability/profile reference, transport trace and EHD/profile mapping. |
| **O3/O4/O5** runtime, context and action | Can local result, retrieval boundary, source dependence, tool outcome and re-entry be tied to the affected decision? | Local result, retrieval/tool traces, scope/freshness/dependency qualifiers and observed outcome. |
| **F5 / intermediate aggregation boundary** | When two or more prior assertions are composed, can the receiver reconstruct their count, dependency treatment and any declared transformation or loss? | Ordered input assertions, aggregation output, input-assertion count, dependency declaration, transformation/loss declaration and hop-by-hop mapping. |
| **IF-S1/IF-S2** identity and authority | Are identity/binding and applicable authority kept distinct, current and bounded? | Binding/grant references, validity/revocation condition and receiving scope. |
| **IF-S3/IF-S4/IF-S5** assurance, policy and appraisal | Does EA preserve the distinction among attestation, appraisal, conformance, indeterminate and reference validity? | Native result, issuer relationship, policy/reference version, scope and limitation. |
| **IF-S6/IF-S12** human capacity and response | Does a qualified assessment reach an owner with usable response capacity without treating approval or execution as new evidence? | Capacity/window, authority, actionability, execution result and revalidation link. |
| **IF-S7/IF-S9** telemetry and population evidence | Are measurement scope, method, limitations and correlation preserved before composition? | Measurement/evaluator profile, period, source dependence and stated limit. |
| **IF-S8** records | Can a later reviewer reconstruct the bounded decision path without treating the record as proof of every claim? | Record linkage, result/outcome, re-entry and integrity evidence. |
| **IF-S10** privacy | Does minimum disclosure leave unavailable qualification explicit rather than force disclosure or inference? | Disclosure rule, permitted abstraction and resulting UNKNOWN/limit. |
| **IF-S11/IF-S13** external signal and trust context | Can an external claim or framework condition be consumed as bounded evidence without creating authority or false equivalence? | Signal/framework reference, scope, freshness, provenance/dependence and limitation. |

## A.9 Change and maintenance discipline

1. A failed fixture does not by itself justify a new interface family or a redesign of EA.
2. The ICR must identify the missing fact, its actual producer, intended receiver, semantic owner, test vector and why UNKNOWN is not sufficient for the declared decision.
3. First consider an existing conditional field, profile reference or bounded adapter. Add a new field only when the existing model cannot express the fact without ambiguity.
4. A Composition-Critical requirement remains conditional and versioned; it must not become a metadata tax on simple local decisions.
5. Any approved change is retested against the positive, boundary and rejection fixtures that exposed it, plus a no-regression ordinary-kernel fixture.
6. Source profile, adapter and fixture changes are version-pinned. The named maintenance owner records whether the semantic mapping remains valid after a producer or consumer changes.

7. Any approved change that affects a material asserted qualifier is also retested against the adversarial-assertion fixture that exposed it.
8. The semantic owner freezes the material qualifier set before execution. Adding, removing or reducing a material qualifier between ICR versions is version-pinned, justified and retested; reducing the set is a registrable finding, not evidence of better preservation.
9. An asserted source property remains declared unless its stated basis supports a stronger status. A fixture that depends on producer honesty records that limitation explicitly.
10. A Level 2 claim is retained only when the ICR identifies an independently operated producer; otherwise the result is labelled simulated-boundary evidence.
11. The route map and every intended aggregation point are declared before execution. A later-discovered undeclared aggregation is recorded as a nonconforming mapping and is not normalised by a later ICR version.
12. Where a material route component is non-deterministic, the applicable fixtures are repeated and their outcome dispersion is retained in the ICR.
13. An unresolved reviewer objection blocks a finding of sufficient for the declared scope or horizon.

## A.10 Decision on interface sufficiency

The plan is complete for a declared component route when the relevant ICR set shows that:

1. every material input is available from a named producer or explicitly UNKNOWN;
2. the producer's native semantics and material qualifiers survive to EA and to the identified receiver;
3. EA returns only a bounded assessment, limitation or requalification request within its authority boundary;
4. positive, boundary and rejection fixtures produce the expected interpretation without invented information;
5. a material change can be connected to the appropriate re-entry and later outcome where the route requires it;
6. the observed disclosure and operational burden remain visible against the declared MCA capacity and useful horizon; and
7. any remaining failure is classified as an interface field gap, producer/receiver gap, nonconforming mapping or out-of-scope owner issue.
8. the material qualifier set was frozen by its semantic owner before execution, and any later reduction is recorded and justified;
9. any chained or aggregating route preserves or explicitly declares the loss of material qualifiers at each hop; and
10. any claimed Level 2 result identifies an independently operated producer, or is limited to simulated-boundary evidence.
11. any material asserted qualifier was exercised against an adversarial-assertion fixture, or the route guarantee is explicitly conditional on the declared basis; and
12. a route classified as operationally non-viable is not accepted as sufficient for the declared horizon.
13. a route whose horizon viability is indeterminate is not accepted as sufficient for that horizon;
14. the ordered route map and all intended aggregation points were declared before execution, and any undeclared aggregation discovered later is classified as a nonconforming mapping;
15. any self-declared materiality condition is labelled as such; and
16. any non-deterministic material route component was exercised repeatedly with outcome dispersion retained, while any unresolved reviewer objection blocks a sufficient conclusion.

This conclusion answers a narrow but necessary question: **whether the interfaces are sufficient for the declared EA test route.** It does not prove that EA is effective for every ecosystem, that all components interoperate without adapters, or that the underlying business/operational decision is correct.

## Editorial continuity note — interface snapshot and later consumers

This integrated reader is the current programme-independent general-interface route derived from the 04 lineage and its conformance work. It defines the O1–O6 / IF-S1–IF-S13 interface landscape, EHD semantics and Appendix-A conformance discipline.

Later participant-local positioning, ACC/admissibility, signalling/choreography, Ecosystem Cartography, agentic-gradient and MSCA Operation/Repositioning work may **consume, specialize or test** these interfaces. They do not automatically create new 04 interface families or rewrite earlier 04 semantics. Any new mandatory interface family, field or conformance requirement must be introduced through an explicit versioned interface change.

The controlled/repaired v0.4 source blobs remain preserved separately for historical/freeze reconstruction.
