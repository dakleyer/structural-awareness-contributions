# Ecosystem Awareness — Functional Architecture — v0.4

## Technology-neutral functional model

&nbsp;

# Status and purpose

This document defines the functional architecture of Ecosystem Awareness after the problem model and epistemic-safety principles have been fixed. It is an internal working architecture, not an adopted FG-TIDA or ITU-T deliverable.

Architecture Candidate v0.4 reconciliation/readability release. This version preserves the complete v0.3 functional model, including the validation-gated F2.APQ Acquisition Pathway Qualification sub-capability and pathway-to-signal-to-composition-to-requalification-to-learning handoffs, while adding the final plain-language map and interface-trace completeness required by the reconciliation plan. It does not add F10 or any new interface/control family. Architecture Candidate v0.2 and v0.3 remain retained as predecessors.

&nbsp;

&nbsp;

The objective is not to prescribe one component, agent, model, protocol or uncertainty algorithm. The objective is to specify the functions that an agentic system must be able to perform if it is to maintain a justified epistemic position across local reasoning, external signals and ecosystem composition.

&nbsp;

Ecosystem Awareness is not an auditor that merely recommends more controls. It is an active information and requalification capability. It helps the rest of the system establish an adequate observation frame, interprets certainty and uncertainty emitted by local and external participants, composes those states by domain, determines whether the current operating frame remains justified, and supplies requalification information back to operational functions.

&nbsp;

# 1\. Functional design boundary

The functional model is based on five boundaries.

&nbsp;

First, Ecosystem Awareness does not own the mission, business objective or utility function. It consumes enough mission context to determine what level of epistemic qualification is required.

&nbsp;

Second, Ecosystem Awareness does not own the ordinary operational decision of every agent. Workers, planners, policy engines, human-oversight functions, safety controllers and other domain functions retain their own responsibilities.

&nbsp;

Third, Ecosystem Awareness does not create authority. A signal, assessment or human approval may change available evidence, but authority and permitted action remain governed by the applicable policy, mandate and control functions.

&nbsp;

Fourth, Ecosystem Awareness does not require complete internal-state disclosure. It requires sufficient epistemic qualification: scope, determination state, residual uncertainty, freshness, provenance/dependency information and other qualifiers needed for the receiving decision.

&nbsp;

Fifth, Ecosystem Awareness does not seek complete ecosystem knowledge. It maintains minimum sufficient awareness for the current mission while preserving the structural residual that cannot be guaranteed to enter any finite observation window.

&nbsp;

# 2\. Double-loop reference architecture

The architecture contains two coupled loops rather than one linear pipeline.

&nbsp;

## Loop A — Epistemic framing and window qualification

The first loop establishes the frame within which determination is expected to be meaningful.

&nbsp;

Mission / objective / criticality

+ constraints and applicable authority

+ ecosystem sensitivity / exposure and consequence profile

+ available observation / determination capacity and cost

+ reachable response capability

+ time horizon and reversibility

+ dependency assumptions

→ F1 Mission & Decision Context Qualification

→ F2 Decision-Relevant Window Qualification & Management

→ qualified working frame W(d)

&nbsp;

The result is not a claim that W(d) equals the ecosystem. It is a bounded statement that W(d) is the current minimum sufficient working frame for domain d under stated assumptions.

&nbsp;

In v0.2 the same relation is made explicitly dynamic as W(d,t). 'Minimum sufficient' means that window breadth, freshness, source diversity and determination effort are calibrated to the domain's current sensitivity to ecosystem change, consequence severity, reversibility, tolerated residual, available observation/determination capacity and remaining response horizon. This is a qualification problem, not a promise of mathematical global optimality.

&nbsp;

## Loop B — Runtime epistemic re-evaluation and composition

Operational agents, tools, humans and external peers act inside or around that frame and emit results together with whatever epistemic qualification is available.

&nbsp;

local outputs and local epistemic states

+ external certainty / uncertainty signals

+ measurement, drift and dependency evidence

→ F3 Local Epistemic State Qualification

+ F4 External Epistemic Signal Qualification

→ F5 Scope-Indexed Epistemic Composition & Coupling Assessment

→ F6 Systemic Epistemic & Operating-Frame Assessment

→ epistemic condition + operating posture

→ F7 Requalification & Corrective Directive Generation

→ back to F1/F2 and to the relevant operational functions

&nbsp;

In parallel:

F6 → F8 Epistemic Statement & Envelope Generation

observed outcomes / changed conditions → F9 Outcome Feedback & Revalidation → F1/F2/F3/F4 as required

&nbsp;

The loops are continuous. A system can begin with a well-qualified frame and later lose that qualification because sources, dependencies, human capacity, policy, regime assumptions or ecosystem conditions change.

&nbsp;

# 3\. Two orthogonal result axes

Ecosystem Awareness must not collapse epistemic condition and operational posture into one label.

&nbsp;

## Axis A — Epistemic management status and structural qualification

The epistemic assessment separates management quality from structural non-determination. These outputs are related but not mutually exclusive.

&nbsp;

Management verdict: Sound — the four epistemic categories remain distinct and correctly scoped for the material domains, with no identified Type 1 or Type 2 management fault.

&nbsp;

Structural qualification: Type 0 markers record in-window determination limits and the open structural residual beyond the current bounded window. Type 0 is not a management failure and may coexist with a Sound management verdict and Normal operation when it is correctly represented and acceptable for the mission.

&nbsp;

Management fault Type 1 — uncertainty is being acknowledged but not bounded into legitimate closure, including unbounded search, escalation, HOLD or window expansion.

&nbsp;

Management fault Type 2 — uncertainty, scope limitation or inherited residual is being suppressed or promoted into unjustified certainty.

&nbsp;

Mixed management status — different domains or dependencies contain different Type 1 and Type 2 management faults, potentially alongside correctly represented Type 0 structural conditions. Mixed states are expected in real ecosystems and must remain scope-indexed.

&nbsp;

## Axis B — Operating posture

The posture describes what operating frame remains justified.

&nbsp;

Normal — the current qualified operating envelope remains sufficient. Type 0 residual may exist, but it is recognized and remains within the tolerated frame.

&nbsp;

Containment / Mitigation — material degradation, uncertainty or epistemic error exists, but a bounded known response can preserve or recover a qualified operating frame by reducing exposure, autonomy or scope, or by targeted requalification.

&nbsp;

Migration / Regime Transition — the current qualified operating envelope can no longer establish a sufficiently valid mission-level response mapping. Continued investment in preserving the old frame is not enough; the system must prepare or execute transition to a newly qualified frame.

&nbsp;

Type 1 and Type 2 detection therefore do not mechanically select a posture. They create requalification pressure. Posture depends on mission criticality, affected domains, available response capability, and whether a qualified frame can still be maintained or recovered.

&nbsp;

Presentation projection. F6's normative output remains scope-indexed. For display, alerting or routing, F8 or a downstream adapter may expose a deliberately lossy \`Posture(D\_receiver)\` plus material qualifiers such as response-capacity sufficiency, response-window state, frame recoverability and transition readiness where relevant. The projection must identify its receiving decision scope and the domain(s) driving it, must not be treated as a composition input or averaged back into E\*(d), and must not be represented as a single global ecosystem posture. If a defensible single projection cannot be produced for a multi-domain consumer, the system preserves the multi-domain posture state rather than fabricating a scalar or universal label.

&nbsp;

# Model reconciliation — normative interpretation

Ω — open class of potentially decision-relevant ecosystem state; it is not treated as a closed or exhaustively enumerable set.

U — bounded represented operational universe used in the foundational development.

W(d) — active, domain- and decision-time-scoped working observation/context frame used by this functional architecture; it refines the operational boundary without closing Ω.

A/B/C/D — epistemic classifications relative to the active scope/window; they are not a set-theoretic partition of Ω. C and D are not defined as subsets whose union equals the open residual R\_U; no normative identity R = C ∪ D is assumed.

Type 0 — structural qualification; Type 1/Type 2 — failures of epistemic management.

I/O and E controls — surfaces on which those conditions are tested for own state and received signals.

Normal / Containment-Mitigation / Migration-Regime Transition — operating posture, orthogonal to the management verdict and Type 0 structural qualification.

Dependency space is treated as open and potentially interdependent. Absence of a represented coupling is not evidence of independence; compensation across domains requires sufficient positive coupling evidence for the specific requalification claimed.

# 

# 4\. Functional model

# F1 — What must be justified for this mission?

# F2 — What should we observe, and through which sufficiently qualified path?

# F3 — What does this local result actually establish?

# F4 — What does this external result actually establish?

# F5 — Can these results be composed without losing scope or double-counting evidence?

# F6 — Is the current frame still justified, and what operating posture is supported?

# F7 — What is the smallest requalification action needed?

# F8 — What bounded epistemic statement can safely be handed off?

# F9 — What did the outcome teach us about the previous frame?

# The detailed definitions below remain controlling.

&nbsp;

## F1 — Mission & Decision Context Qualification

Purpose

Establish what must be epistemically justified for the current operation before deciding what information must be observed, including how sensitive the mission is to ecosystem change and what observation/determination burden is proportionate to that risk.

&nbsp;

Inputs

- mission, task or objective envelope;

- material decision domains and intended outputs;

- criticality and stakes;

- ecosystem sensitivity/exposure: which environmental, human, agentic or dependency changes could materially alter the decision and how quickly;

- consequence severity and tolerated residual by domain;

- hard constraints, applicable policy and authority;

- reversibility and acceptable failure consequences;

- time horizon and decision deadline;

- autonomy and action scope;

- known human, agentic and environmental dependencies;

- reachable response capabilities, including containment, fallback, human intervention and migration capabilities;

- available observation/determination capacity and burden: compute, context, latency, bandwidth, privacy/disclosure cost, evidence access and human attention;

- current operating-frame assumptions.

&nbsp;

Required behaviour

F1 translates the mission into epistemic requirements. It determines which domains are material, what degree of determination is sufficient for each, which dependencies can change the decision, and how much warning or response time is required for corrective action to remain useful.

&nbsp;

F1 also produces the risk/capacity basis for observation. It estimates, at an implementation-appropriate level, how sensitive each material domain is to ecosystem change, how costly a miss would be, how reversible the decision remains, what residual can be tolerated, and what observation/determination/response capacity is actually available. This does not require one universal risk score; categorical or domain-specific assessments are valid.

&nbsp;

F1 must not assume that maximum information is optimal. The required determination level and observation burden are proportional to mission criticality, ecosystem sensitivity/exposure, consequence severity, reversibility, tolerated residual, available observation/determination capacity and reachable response capacity. A higher-risk mission may justify a wider or fresher frame; a low-risk reversible decision may legitimately accept a larger explicit residual.

&nbsp;

Outputs

- Operation Context Profile;

- material domain set D = {d1…dn};

- required determination/sufficiency criteria by domain;

- dependency and coupling hypotheses;

- response and warning horizon;

- criticality, ecosystem-sensitivity/exposure and reversibility profile;

- observation/determination capacity and burden profile;

- tolerated residual / decision-risk tolerance by domain;

- applicable validity assumptions;

- triggers requiring context requalification.

&nbsp;

Primary interfaces

Planner/orchestrator, policy/authority functions, safety/action controller, human-oversight capability, mission/business logic.

&nbsp;

## F2 — Decision-Relevant Window Qualification & Management

Purpose

Construct and continuously maintain the minimum sufficient observation/context window for each material domain, including qualification of the available acquisition pathway or combination of pathways by which decision-relevant state can enter that window, dynamically calibrated to mission sensitivity/risk, finite observation/determination capacity, pathway burden and remaining response horizon.

&nbsp;

Inputs

- Operation Context Profile from F1;

- technically observable sources, sensors, memory, retrieval systems, tools and peer interfaces;

- current W(d);

- evidence availability and access constraints;

- compute, latency and context budgets;

- human-attention, evidence-access, communication, privacy/disclosure and other observation-cost constraints;

- domain sensitivity/exposure and tolerated residual from F1;

- source and dependency map;

- freshness requirements;

- feedback and revalidation triggers;

- required response horizon.

&nbsp;

Required behaviour

F2 selects what enters active interpretation and what remains outside it. The window is an allocation of attention, not a declaration of the universe.

&nbsp;

Named sub-capability — F2.APQ Acquisition Pathway Qualification. APQ asks whether an available way of obtaining evidence, or combination of pathways, is sufficient for this decision scope. A pathway may be an explicit signalling protocol, peer message, API/tool, telemetry source, public or regulatory feed, third-party assessment, human report, passive observation, or environmental/action trace. APQ then qualifies only the pathway properties material to the current evidence need. It does not require the pathway owner to publish a capability profile; where self-description is absent, relevant properties may be qualified from observed, attested, independently evaluated, derived or UNKNOWN evidence.

&nbsp;

F2.APQ is decision-relative rather than a global channel-ranking function. It considers the current unresolved domain/evidence need, the active W(d,t), known source/dependency relationships, relevant pathway-property evidence, acquisition cost/latency/privacy burden, mission sensitivity/consequence/reversibility and the remaining response horizon. Its output may identify a sufficient pathway, an insufficient pathway for the present need, a need for independent acquisition, an unresolved pathway qualification, or that no further acquisition is currently justified.

&nbsp;

The central optimization is architectural rather than omniscient: expand, refresh, redirect or narrow W(d,t) only when the expected decision value of doing so is material relative to its resource/privacy/latency burden and the remaining response horizon. F2 therefore guards both sides of the governing contradiction: Type 1 over-observation/over-processing and Type 2 under-observation/stale-frame overconfidence.

Redirect changes which actors, dependencies, domains or acquisition pathways are admitted to or prioritized within W(d,t), or the selection basis used to construct that window. It does not imply a geometric centre, a change of identity or an authority grant. Candidate information/signalling actions may be compared by their decision-scoped epistemic value relative to cost, capacity and response horizon without creating a new F-function.

&nbsp;

For each domain, F2 must keep distinct:

A — sufficiently determined state already inside the window;

B — defined in-window indeterminacy;

C — relevant state that may be brought into the window through additional observation or context expansion;

D — structural residual that cannot be presumed exhaustively discoverable.

&nbsp;

The window must be revisable. F2 may widen, narrow or redirect attention when mission, uncertainty, source quality, dependencies or regime validity change. Expansion must remain bounded so that Pole C does not become unbounded Type 1 search. Narrowing is equally controlled: a smaller window is acceptable only when the residual and missed-change exposure remain proportionate to the current mission sensitivity and response capability.

&nbsp;

Outputs

- qualified Window Profile W(d);

- included scope and material exclusions;

- known limitations and unknown-scope markers;

- coverage and freshness state;

- required evidence/source classes;

- dependency visibility state;

- revalidation conditions and validity interval;

- candidate expansion paths;

- 