l / Incident Exchange & Defence

Generic role

Distributes, amends/corroborates and correlates ecosystem-relevant signals; represents affected scope/blast radius and may feed containment/resolution. This aligns closely with FG-TIDA Theme \#13.

&nbsp;

Optional S11 Ecosystem Signalling Capability Profile. Where a signalling mechanism can expose stable capability semantics, S11 may make available a versioned profile describing signalling properties it declares or that have been externally established. The profile is evidence about the mechanism, not the EA qualification itself. The candidate inventory is grouped below for scanning; the list remains open and each property remains conditional on decision relevance.

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

Signal infrastructure carries and correlates claims. EA assesses what those claims justify epistemically. Signal exchange does not create authority. The current FG-TIDA Theme \#13 / incident-signal-and-blast-radius direction is therefore a concrete S11 peer capability that EA can consume rather than reproduce. EA may also be required when no incident or malicious agent exists—for example, when honest locally correct subsystems remain epistemically fragmented at composition level—so S11 is an important interface, not the semantic boundary of Ecosystem Awareness. EA does not rank or certify S11 mechanisms globally. It qualifies the sufficiency of an available route for a stated decision and preserves the distinction between declared mechanism properties and independently supported properties.

&nbsp;

## S12 — Enforcement, Containment, Revocation, Recovery & Migration

Generic role

Actually enforces authorization/policy and applies operational controls such as restrict, rate-limit, revoke, isolate, quarantine, suspend, rollback, fallback, substitute, recover or migrate/reconfigure.

&nbsp;

Inputs to Ecosystem Awareness

\- available control/response capabilities and effective reach;

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

&nbsp;

Internal EA functions

F1, F6, F7, F9.

&nbsp;

Boundary

EA identifies the epistemic need and target. Enforcement/recovery functions own the actual authority and execution.

&nbsp;

## S13 — Trust Framework / Assurance Mapping / Jurisdictional Context

Generic role

Provides the trust framework, assurance levels, jurisdictional constraints, mutual-recognition/equivalence mappings and governance references under which identity, authority, evidence and interaction are interpreted. This corresponds to ordinary enterprise/government trust frameworks and is adjacent to FG-TIDA Themes \#3 and \#8.

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

For robotics/embodied AI, the trust interface may additionally bind logical agent, runtime/controller, physical device and authority. Relevant inputs include binding identity, device/runtime attestation, binding freshness, control-transfer state and physical-action attribution. These specialize S1, S2, S3 and S8 rather than creating a new EA core function.

&nbsp;

## Model-level trust and lineage

Model identity/version, training/lineage claims, adaptation state and model-level assurance can enter through S3 attestation, S7 evaluation/drift and S8 records. A lineage or provenance claim is evidence; it does not by itself establish behaviour.

&nbsp;

## Credential / wallet / secret / confidential execution

Credential vaults, wallets, key stores and confidential-computing mechanisms support S1 identity/authentication, S2 authorization and S3 runtime assurance. EA should consume only their assurance/availability/validity state, never secret material.

&nbsp;

# 7\. Interface completeness against F1–F9

F1 Mission & Decision Context Qualification consumes principally O1, S2, S6, S10, S12 and S13. In v0.2 O1 supplies the mission-side ecosystem sensitivity/exposure, consequence/reversibility and available observation/determination-budget context; S6 and S12 contribute effective human and response capacity.

&nbsp;

F2 Decision-Relevant Window Qualification & Management consumes principally O2, O4, O6, S7, S10 and S11. It combines F1’s sensitivity/risk basis with source availability, retrieval/instrumentation burden, privacy limits and freshness to maintain W(d,t). When F2.APQ is invoked, S13 contributes assurance/trust-framework context where material; O5 contributes direct tool/API/resource pathway state when a tool or API is itself the acquisition path; and S6 contributes human-channel availability/information-scope/response-window state when human reporting or review is itself the acquisition path. Equivalent pathway descriptions may be mediated through O2/O4/F1, but the mediation remains explicit. No new O/S family is required.

&nbsp;

F3 Local Epistemic State Qualification consumes principally O3, O4, O5, S4, S5, S6 and S7.

&nbsp;

F4 External Epistemic Signal Qualification consumes principally O2, O6, S1, S3, S4, S5, S8, S9, S11 and S13.

&nbsp;

F5 Scope-Indexed Epistemic Composition & Coupling Assessment consumes all qualified local/external states and especially dependency/provenance information from S2, S3, S8, S9 and S11.

&nbsp;

F6 Systemic Epistemic & Operating-Frame Assessment consumes F5 plus mission/criticality and ecosystem-sensitivity/exposure from O1/F1, observation/determination burden from F2/O4/S7, human capacity from S6, response capability from S12 and applicable trust-frame assumptions from S13.

&nbsp;

F7 Requalification & Corrective Directive Generation targets O1, O3, O4, O5, S1–S7, S9, S11, S12 and S13 according to the affected domain. It does not broadcast generic “add control” requests.

&nbsp;

F8 Epistemic Statement & Envelope Generation publishes through O6, S8 and S11, subject to S10 privacy/minimum-disclosure constraints.

&nbsp;

F9 Outcome Feedback & Revalidation consumes O3/O5 execution results, S6 intervention outcomes, S7 telemetry/evaluation, S8 records, S11 resolution/correction signals and S12 containment/recovery/migration outcomes.

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

\- S2 authority state where actions are delegated;

\- S7 outcome/telemetry;

\- S12 available response capability.

&nbsp;

For an interoperating multi-agent security system, the minimum expands to include:

\- O2/O6 discovery and task/message transport;

\- S1 identity/authentication;

\- S2 authority provenance;

\- S3 attestation where runtime assurance matters;

\- S4 conformance verdicts;

\- S5 appraisal semantics;

\- S6 human-capacity state where humans are in the control path;

\- S8 verifiable records;

\- S10 privacy/minimum disclosure;

\- S11 ecosystem signal exchange;

\- S12 enforcement/containment/recovery.

&nbsp;

S9 population evaluation and S13 cross-domain trust mapping are activated when the problem requires those scales. They are not universal mandatory dependencies.

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

Operational plane

Current A2A specifications provide concrete concepts for Agent Cards, discovery, capabilities/skills, authentication requirements, tasks, messages, artifacts, task status and extensions. These fit O2 and O6 directly.

&nbsp;

Current MCP specifications expose resources, prompts and tools, and client-side capabilities such as sampling, roots and elicitation, with explicit authorization and security requirements. These fit O4, O5 and parts of O1/O6.

&nbsp;

OpenTelemetry GenAI semantic conventions increasingly expose agent invocation, model calls, retrieval and tool execution as standardized telemetry operations. These fit S7.

&nbsp;

Trust/security plane

RFC 9334 RATS gives a mature generic architecture for Attester → Evidence → Verifier → Attestation Result → Relying Party, fitting S3/S5.

&nbsp;

FG-TIDA Theme \#5 provides a strong emerging boundary for provenance of authority: origination, grant content, limits, delegation/redelegation, revocation and anchor integrity.

&nbsp;

FG-TIDA Theme \#6 provides a strong emerging boundary for intent/policy expression and runtime conformance verdicts, including explicit indeterminate, scope, issuer binding and named/versioned references.

&nbsp;

FG-TIDA Theme \#7 contributes verifier-side appraisal/rejection semantics and negative vectors rather than a competing standalone layer.

&nbsp;

FG-TIDA Theme \#1 provides a strong emerging boundary for verifiable action records and the properties carried claims need for later reconstruction.

&nbsp;

FG-TIDA Theme \#16 provides the human-oversight lifecycle and, critically for Ecosystem Awareness, human-capacity state as an input rather than transferring oversight ownership into EA.

&nbsp;

FG-TIDA Theme \#21 provides a population-level reading layer that explicitly distinguishes sampling uncertainty from structural indeterminacy and hands operational use back to oversight/EA-like consumers.

&nbsp;

FG-TIDA Theme \#19 provides privacy/minimum-disclosure requirements across identity, authorization and audit artefacts.

&nbsp;

FG-TIDA Theme \#13 provides the closest current ecosystem-signal and defence interface: shared signals, provenance/confidence/freshness/scope, correlation/blast radius and containment lifecycle.

&nbsp;

FG-TIDA Theme \#22 provides the emerging agentic Remote Attestation interface and is already converging with Theme \#6 around attested policy/version, verifier relationship and interaction-bound evidence.

&nbsp;

Themes \#18, \#20 and the model-level/trust-mechanics work provide specialized evidence sources and profiles that can be consumed through the generic interfaces above without changing F1–F9.

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