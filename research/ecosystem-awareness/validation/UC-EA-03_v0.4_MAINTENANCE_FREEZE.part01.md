# UC-EA-03 — Architecture-Validation Profile — Human Oversight under Bounded Effective Capacity and Non-curative Approval — v0.4 — Maintenance Freeze

Derived from TIDA — Delegated Authority OS under Context Change

&nbsp;

# Status

Maintenance-frozen internal Ecosystem Awareness architecture-validation profile. Legacy identifier UC-EA-03 is retained for continuity, but this document is not an FG-TIDA use-case submission. Theme \#16 remains the owner of the human-oversight lifecycle; this profile tests the Ecosystem Awareness interface to that lifecycle and must not redefine its universal stages, authority model or enforcement semantics. The Parent Case Study remains pre-freeze public working material.

&nbsp;

# 0\. Identification and traceability

Validation Profile ID: UC-EA-03 (legacy UC identifier retained for traceability).

Parent Case Study: TIDA — Delegated Authority OS under Context Change.

Public-submission boundary: this profile should not become a separate public FG-TIDA Use Case merely because it has its own validation branches. The single situational EA submission should remain grounded in the mobility action-time decision; UC-EA-03 is the Theme \#16 interface profile used to test that situation when human intervention becomes material. Upward/downward/horizontal extensibility remains a Parent Case property, not an automatic expansion of the public issue.

Primary Challenge: S4 — Human-inclusive oversight authority & capacity.

Secondary Challenges: S13 — Authority history vs intervention history; S14 — Evidence-to-decision assessment; S5 — Operational indeterminacy & containment.

Case-level ToR anchors: 3.3 Use cases; 4.1 Use cases and requirements analysis.

EA functions under test: F1 Mission & Decision Context Qualification; F3 Local Epistemic State Qualification; F5 Scope-Indexed Epistemic Composition & Coupling Assessment; F6 Systemic Epistemic & Operating-Frame Assessment; F7 Requalification & Corrective Directive Generation; F9 Outcome Feedback & Revalidation.

Principal EA hypothesis: human oversight is an internal bounded capacity, not an epistemic reset button. A valid human approval can satisfy an authorization/intervention condition but does not automatically repair contrary evidence, expand the reviewer’s information window, or convert an upstream Type 2 world model into truth.

&nbsp;

v0.3 frozen reconciliation: human attention is a finite resource of the extended human-agent system. Repeated escalation, context requests or evidence review can itself become Type 1 when it depletes capacity without materially changing the supported decision. The correct human path is therefore sensitivity/risk- and response-window-qualified, not 'always escalate when uncertain'. This version aligns the profile explicitly to Theme \#16's consolidated implementation-neutral lifecycle rather than to any particular state machine: trust/runtime event → trigger qualification → normal or exceptional intervention path → escalation → applicable human authority → permitted intervention → evidence and decision assessment → execution or containment outcome → state and authority revalidation → return to operation / continued suspension / rollback. \`HELD\`, \`INDETERMINATE\`, bounded mandates and admission decisions remain optional implementation mappings beneath that lifecycle, not mandatory universal stages.

&nbsp;

# 1\. Functional interaction

Plain-language situation

At T2, E1 reports Qcritical crossed and P1 requires reassessment before A1. The ordinary automated path may require or permit a human intervention H1. The system must first qualify whether the event belongs in the normal oversight path or an exceptional intervention path, then determine whether the applicable human authority and current oversight capacity are sufficient, what intervention is actually permitted, and what the resulting evidence/outcome establishes before revalidation or return to operation.

&nbsp;

Actor

Citizen principal; personal agent/instance; municipality/public principal; authorized municipal role; evidence source E1; human reviewer or human-held role; relying party/admission function; oversight workflow; containment/recovery function where needed.

&nbsp;

Action

Human review or intervention concerning whether and how A1 may proceed after the T2 context change.

&nbsp;

Decision required

Does the available human oversight path provide sufficient current authority, information, time and intervention capacity to alter the operative determination, and what epistemic effect does the resulting human decision legitimately have?

&nbsp;

Problem encountered

Many agentic architectures treat escalation as a generic safety valve. If the human path is unavailable, overloaded or insufficiently informed, escalation can become Type 1\. v0.2 makes the resource mechanism explicit: each escalation/review consumes time and attention, potentially shrinking future intervention capacity for the same or other material domains. If the system eventually proceeds because the human clicked approve, that approval can be misread as a correction of the evidence/world model and produce Type 2\.

&nbsp;

Current mitigation

HITL approval; escalation queues; reviewer roles; action holds; bounded mandates; intervention records; return-to-operation checks.

&nbsp;

Residual gap being tested

Whether EA consumes Theme \#16 trigger-qualification, intervention-path, capacity, authority, decision and outcome state without taking ownership of the oversight mechanism; detects when oversight capacity is binding or depleted; preserves evidence/human-decision/execution distinctions; prevents non-curative approval from laundering uncertainty; and requalifies the system after intervention. Human review should be requested only where the affected domain's sensitivity/consequence makes that expenditure of attention decision-relevant. The profile validates EA against Theme \#16's lifecycle questions, not against one preferred implementation state machine.

&nbsp;

# 2\. Parent Case Study facts inherited unchanged

Case Study identity

TIDA — Delegated Authority OS under Context Change is a candidate shared Case Study. Annex I supplies the minimal mobility instantiation and explicitly states that human oversight is more than routing to a nominal role.

&nbsp;

T0 — Setup

G1 and P1 are established; P1 defines Qnormal/Qcritical and source E1.

&nbsp;

T1 — Commitment

D1 and C1 are created only where authority and hard limits are sufficiently established.

&nbsp;

T2 — Context change

E1 shows Qcritical crossed. P1 requires reassessment and disallows entry to the affected zone unless an authorized exceptional intervention H1 applies. The system may reroute/proceed with limits, hold, use a bounded escalation path or return INDETERMINATE.

&nbsp;

Human oversight boundary in the parent Case Study

A person may be formally authorized yet unavailable, overloaded, unable to understand the case in time or unable to intervene effectively. Requirements must represent who can receive escalation, what the person may decide, time available and whether effective capacity exists. A role without usable capacity cannot manufacture permission.

&nbsp;

Record separation

G1/P1 remain authority/provenance records; D1/C1 remain decision/commitment records; H1 records any later intervention, its authority, evidence and operational effect. None overwrites another.

&nbsp;

Governing regime

The parent source requires a governing regime before freeze where mandate validity/standing/revocation is tested. It is not fixed yet and remains TBD.

&nbsp;

# 3\. Theme \#16 lifecycle and human-capacity interface under test

Inputs expected from the oversight function where available:

human-capacity state — available, binding, unavailable or implementation-equivalent;

required reviewer/role and authority;

response deadline/useful intervention window;

current trigger-qualification / normal-or-exceptional intervention-path / escalation state, including implementation-specific \`HELD\` where used;

human decision and scope;

intervention mandate/validity where applicable;

evidence considered and its sufficiency/limitations;

intervention outcome/reconciliation state;

return-to-operation/revalidation state.

&nbsp;

Lifecycle-consumption rule: EA does not require Theme \#16 to expose \`HELD\`, \`AUTHORIZED\`, \`INDETERMINATE\` or any other implementation-specific state. It consumes whatever implementation-neutral fields are sufficient to identify trigger qualification, selected intervention path, applicable authority, effective capacity, permitted intervention, decision/evidence state, execution-or-containment outcome and revalidation/return status.

EA outputs to the oversight function may include:

&nbsp;

&nbsp;

targeted request for human review only for the affected domain;

the information/scope the reviewer needs for the specific epistemic question;

indication that human capacity is itself insufficient/unavailable;

bounded stop/escalation condition when repeated requests become Type 1;

indication that further human review is not currently justified because its expected decision value is low relative to remaining attention/time capacity;

system-level posture and requalification requirement.

&nbsp;

Boundary

EA does not decide the human mandate, execute the intervention or create authority. It consumes human-capacity state as one dependency among many.

&nbsp;

# 4\. Challenge traceability

Challenge S4 — Human-inclusive oversight authority & capacity

The Challenge asks whether escalation can reach a human or human-held role that is formally authorized, available, informed, competent and able to intervene within the useful time window. Human oversight is an internal system capacity, including named roles, required information, availability/response windows and means to pause, redirect or reverse action.

Primary ToR anchors: 3.4 Security assessment criteria and benchmarks; 4.3 trust framework/lifecycle; 4.5 guidelines, metrics and standardization recommendations; A.2.4 human oversight integration.

&nbsp;

Challenge S13 — Authority history vs intervention history

The Challenge asks whether original authority records and later human/technical intervention records remain distinct historical objects while producing one unambiguous current operative determination. Intervention may confirm, restrict, suspend or replace authority without erasing provenance.

Primary ToR anchors: 4.3; A.1.2 delegation artefact; A.2.4 human oversight; A.2.7 trust control plane.

&nbsp;

Challenge S14 — Evidence-to-decision assessment

The Challenge asks whether each transition can state what must be demonstrated, evidence required, evidence status and decision supported.

Primary ToR anchors: 3.4; 4.5; A.2.2; A.2.4.

&nbsp;

Challenge S5 — Operational indeterminacy & containment

The Challenge requires incomplete/conflicting evidence to remain bounded rather than become silent permission, with containment, hold, rollback or escalation before effects leave control.

Primary ToR anchors: 3.4; 4.3. Supporting: A.2.2; A.2.7.

&nbsp;

# 5\. EA functional traceability

F1 includes human response capability, ecosystem sensitivity/consequence and useful intervention horizon when determining what level of epistemic qualification is required and whether human review is proportionate.

F3 qualifies the human decision as a local epistemic/authority event without assuming it is substantively correct about the whole world.

F5 composes human capacity/decision with authority, evidence, context and upstream uncertainty by domain.

F6 assesses system epistemic condition and operating posture separately.

F7 decides whether targeted human review is justified, whether another evidence path is preferable, whether escalation must stop because marginal decision value no longer justifies human-capacity consumption, or whether containment/migration is required.

F9 revalidates after 