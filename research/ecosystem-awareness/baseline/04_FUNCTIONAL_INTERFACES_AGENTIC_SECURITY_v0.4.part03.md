l / Incident Exchange & Defence

Generic role

Distributes, amends/corroborates and correlates ecosystem-relevant signals; represents affected scope/blast radius and may feed containment/resolution. This aligns closely with FG-TIDA Theme \#13.

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

Signal infrastructure carries and correlates claims. EA assesses what those claims justify epistemically. Signal exchange does not create authority. The current FG-TIDA Theme \#13 / incident-signal-and-blast-radius direction is therefore a concrete IF-S11 peer capability that EA can consume rather than reproduce. EA may also be required when no incident or malicious agent exists—for example, when honest locally correct subsystems remain epistemically fragmented at composition level—so IF-S11 is an important interface, not the semantic boundary of Ecosystem Awareness. EA does not rank or certify IF-S11 mechanisms globally. It qualifies the sufficiency of an available route for a stated decision and preserves the distinction between declared mechanism properties and independently supported properties.

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

**Evidence status — source snapshot: 18 September 2026 (UTC).** The mappings below are **E4 market/standard evidence** in the sense of [00D's evidence-grade definition](./00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md#3-evidence-grades): they support only the documented scope or capability of the named specification, public product/documentation source or current FG-TIDA working direction. They do not establish adoption, universal interoperability, interface completeness or EA effectiveness.

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

# Appendix A — Interface Quality and Conformance Plan for Ecosystem Awareness

## A.1 Status, purpose and scope

**Status.** This is an internal quality and conformance plan for the generic Ecosystem Awareness interface model in this document. It is an additional verification artifact: it does not modify F1–F9, O1–O6, IF-S1–IF-S13, the EHD kernel, the optional Composition-Critical EHD Profile, or any producer's native semantics. It is not a certification scheme, a standards claim, an implementation claim or a quality plan for another architecture.

**Purpose.** The plan determines, for a declared decision scope, whether the available inputs and outputs of actual generic AI components are sufficient for EA to qualify and return an epistemic result without inventing information, taking another component's authority or losing a material qualifier in handoff. It therefore tests the interface, not whether EA is universally effective or whether a producer's underlying domain decision is substantively true.

**In scope.** A test may involve any active subset of O1–O6 and IF-S1–IF-S13, provided that every input has an identified producer or is explicitly UNKNOWN and every EA output has an identified receiving function. The plan covers two bounded levels:

- **Level 1 — internal coordination and integration.** Mission/orchestration, local runtime, context/retrieval, tools, transport and internal trust/control functions exchange qualified state for one declared decision.

- **Level 2 — independent-boundary information.** EA consumes an externally originating signal, record, assessment or other bounded claim through the same EHD discipline. A Level 2 signal changes the receiver's evidence state; it does not transfer authority, prove the whole ecosystem or force a common action.

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
| Materiality control | Frozen set of material qualifiers, the semantic owner who fixed it before execution, rationale and version. A later reduction of that set is a recorded change, not a silent improvement in the result. |
| Boundary | Producing component, consuming EA function, receiving component, semantic owner and adapter/maintenance owner. |
| Evaluation independence | Named reviewer for the mapping, plus any relevant relationship to the producer, receiver or adapter. The reviewer of a mapping cannot be that mapping's adapter/maintenance owner. |
| Native result | The producer's native result and the reference/profile through which it is interpreted. |
| Required qualifiers | Which of scope, provenance/freshness, dependency, unresolved state, capacity, authority, validity/review and privacy constraint are material for this run. |
| Unknown treatment | Explicit UNKNOWN, `not_applicable`, unavailable, not-observed, privacy-restricted or other declared reason where known. |
| Test vector | Positive, boundary or rejection fixture; injected change or limitation; expected EA interpretation and expected receiving consequence. |
| Route shape | Level 1 or Level 2 designation; for Level 2, whether the producer is independently operated; for a chain, the ordered hops; and for an aggregation, input-assertion count and declared transformation or loss. |
| Evidence | Handoff trace, profile/reference, adapter mapping where used, receiving result, observed execution/outcome when available and burden observations. |
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
11. where Level 2 is claimed, the producer is independently operated, or the fixture is explicitly marked as a simulated boundary that does not establish independent interoperability.

Failure to satisfy an entry condition is itself a useful finding: it means the proposed interface cannot yet be tested for that scope without inventing a producer, a receiver, semantics or an oracle.

## A.5 Test method

### A.5.1 Prepare the declared route

1. Select the active interfaces and the relevant EA functions F1–F9.
2. Freeze the decision scope, the available evidence boundary, the useful response horizon, the MCA capacity basis and the disclosure constraint.
3. Identify whether the ordinary EHD kernel is sufficient or whether the Composition-Critical EHD Profile is required.
4. Map native producer fields to the EHD/profile semantics. An adapter may translate representation; it must not silently upgrade UNKNOWN, authority, provenance, independence or determination.

### A.5.2 Exercise three fixture classes

| Fixture class | Minimum situation | Expected interface result |
| --- | --- | --- |
| **Positive** | A producer supplies the material result and qualifiers within scope and validity. | EA preserves the qualification, returns a scoped assessment or no-change result to the identified receiver, and does not claim more than the producer supplied. |
| **Boundary** | One material qualifier is absent, stale, privacy-restricted, capacity-binding, partly scoped or correlated. | The qualifier remains UNKNOWN/limited; EA narrows reliance, requests targeted requalification or records that the available route is insufficient for the decision. |
| **Rejection** | A mapping would collapse UNKNOWN, extend scope, confuse evidence with authority, treat a transport identifier as semantic identity, or send an EA request as an execution command. | The handoff is nonconforming for that use; the ICR identifies the field, ownership or adapter defect rather than manufacturing a value. |
| **Adversarial assertion** | A producer emits a well-formed material qualifier that is false or unsupported in the controlled fixture, such as independence, freshness or scope. | Without independent contradictory evidence, EA preserves the qualifier as declared rather than established and the ICR records the route guarantee as conditional on producer honesty. Where contradictory independent evidence is supplied, EA preserves the conflict or indeterminacy rather than promoting the assertion. |

Composition-Critical tests add at least one vector for each material condition present: a decision-basis/version change, an execution or commitment transition, competing directives over one resource-time segment, and re-entry after changed evidence, authority, dependency or validity.

Where the route has more than one handoff, the fixture includes at least two intermediate hops and evaluates qualifier preservation, transformation and declared loss at each hop, not only end to end. Where a component aggregates two or more prior assertions, the fixture records the input-assertion count and any declared loss, collapse or change of dependency treatment. At least one claimed Level 2 route uses an independently operated producer; a simulated external source is recorded as such and cannot support a claim of established cross-boundary interoperability.

### A.5.3 Evaluate the handoff and return

For each fixture, the reviewer checks:

The named reviewer of an adapter mapping is distinct from that mapping's adapter/maintenance owner; the ICR records any remaining relationship that could affect the review.

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

The plan records observed burden so that a semantically complete handoff is not accepted blindly when it consumes the response opportunity it is meant to protect. It does not prescribe one universal threshold; the declared mission, scope and MCA capacity basis determine materiality.

Where fewer than five applicable vectors or relations are exercised, the ICR reports numerator and denominator as counts and does not present the resulting percentage as a rate estimate. Counts remain useful evidence; they are not statistical generalisation.

## A.7 Conformance findings

The quality conclusion is made **after** the run. It is not a runtime posture or command.

| Finding | Meaning | Required follow-up |
| --- | --- | --- |
| **Sufficient for declared scope** | The ordinary EHD kernel or active generic interface set preserved every material qualifier and produced an owner-preserving EA return for the fixture. | Retain the ICR and repeat only when version, scope or material assumptions change. |
| **Semantically sufficient, operationally non-viable for declared horizon** | Qualifiers and semantics were preserved, but the observed retrieval, communication, review or disclosure burden is not usable within the pre-declared MCA capacity basis or useful horizon. | Do not accept the route as sufficient for that decision; narrow the scope, change the route/profile or record the decision as limited and retest. |
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

This conclusion answers a narrow but necessary question: **whether the interfaces are sufficient for the declared EA test route.** It does not prove that EA is effective for every ecosystem, that all components interoperate without adapters, or that the underlying business/operational decision is correct.
