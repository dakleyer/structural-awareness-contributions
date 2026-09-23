> **Controlled v0.4 release source.** Preserved for release provenance. The current reader successor is [04 — General Functional Interfaces v0.5 Integrated](./04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md); use the successor for current reconciled semantics while retaining this source for the controlled v0.4 record.

# Ecosystem Awareness — Functional Interfaces & Agentic Security Integration — v0.4

## Companion interface model to the fixed F1–F9 Functional Architecture

&nbsp;

# Status and purpose

This document defines the external functional interfaces required by the Ecosystem Awareness architecture. The nine internal functions F1–F9 remain the fixed functional set. v0.4 preserves O1–O6 and IF-S1–IF-S13 exactly as the interface taxonomy, preserves the v0.2 risk/sensitivity and finite-capacity qualification, and adds the validation-gated acquisition-pathway/profile semantics required by F2.APQ. No O7, IF-S14 or new mandatory producer family is introduced. `IF-S#` is an unambiguous namespace prefix only; it does not change any interface family, payload or ownership boundary.

Status boundary. This is an internal working architecture and research object. It is not an ITU-T deliverable, not evidence of FG-TIDA adoption, and not a standards-body endorsement or implementation claim.

&nbsp;

&nbsp;

The model is technology-neutral. It deliberately aligns with common agentic architecture patterns and with the functional boundaries currently emerging in FG-TIDA, but it does not assume that FG-TIDA has adopted any of these interfaces or that every deployment contains every component.

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

Emission-side obligation. The Epistemic Handoff Descriptor does not create a third epistemic control family. A producer remains responsible for applying the internal controls to its own state; the handoff obligation is to preserve the decision-relevant qualifiers needed for downstream interpretation. Where a qualifier cannot be established, it remains UNKNOWN rather than being fabricated. Missing qualification creates downstream Type-2 exposure, not automatic Type 2; the failure materializes only when an intermediary or receiver promotes the missing or bounded qualification into greater determination than was supplied.

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

Four-pole epistemic position

Where the producer can express it, the EHD should make legible:

A — sufficiently determined state inside the active window;

B — defined state inside the window that remains unresolved;

C — recognised state outside the current window that could potentially be brought into it;

D — structural residual that the producer does not presume it can exhaustively eliminate.

&nbsp;

A producer is not required to have a perfect enumeration of B, C or D. The key requirement is that unavailable categories do not silently collapse into A.

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