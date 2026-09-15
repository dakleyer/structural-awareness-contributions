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

F9 revalidates after H1 or other intervention and prevents old approval from being reused after material change.

&nbsp;

Primary failure surfaces

I0 determination capacity; I1 bounded determination effort; I2 epistemic honesty; O1 bounded expansion/escalation; E1-I/E2-I and E1-O/E2-O where human or external evidence is received.

&nbsp;

# 6\. Requirements

R1. The architecture shall represent effective human-oversight capacity separately from the nominal existence of a human role.

R2. A human-review request shall identify the affected domain, decision required, relevant evidence and useful response window.

R3. The system shall not repeatedly escalate to a human when the required capacity is unavailable, the useful window has expired, or additional review has insufficient expected decision value relative to remaining human/time capacity.

R4. A human approval shall remain distinguishable from the evidence on which it was based and from the final execution decision/outcome.

R5. Human approval shall not repair, overwrite or conceal contrary evidence unless the human process actually supplies new evidence sufficient to resolve the affected domain.

R6. A human decision shall not confer authority beyond the reviewer’s mandate or the action/validity scope to which the decision applies.

R7. Material changes in action, policy, approver roster, authority or validity window shall trigger reevaluation rather than automatic reuse of an earlier approval.

R8. Where provider/action execution may have occurred but the outcome cannot be established, the architecture shall preserve an explicit unresolved execution state until reconciliation. \`INDETERMINATE\` is one current implementation mapping; the profile does not require that vocabulary universally.

R9. Human capacity shall be included in F6 as a system dependency but shall not be treated as proof that the broader system is determined.

R10. Return to operation shall require current-state revalidation, not merely existence of a prior approval record.

R11. Human attention/review effort shall be accounted as finite determination capacity of the extended system, not as a cost-free external oracle.

R12. The test shall distinguish a high-sensitivity branch in which additional expert review is justified from a lower-sensitivity/reversible branch in which repeated review would be Type-1 over-protection.

&nbsp;

# 7\. Test and stress-test branches

Branch A — Effective human capacity

The reviewer is authorized, available, sufficiently informed, competent and able to intervene within the useful window. The reviewer receives the relevant scope/evidence and issues H1 within mandate. Expected EA behavior: incorporate H1 as new bounded evidence/authority state, re-evaluate F5/F6, and preserve prior records.

&nbsp;

Branch B — Nominal but unavailable reviewer

A formally authorized reviewer exists but is unavailable or cannot respond in time. Expected EA behavior: human capacity becomes binding/insufficient; do not loop indefinitely; select another bounded evidence/containment/requalification path.

&nbsp;

Branch C — Overloaded review queue

The same or similar issue is repeatedly escalated, creating attention overload. Expected EA behavior: detect Type 1 from unbounded determination effort and stop generic escalation. The architecture must not infer that eventual clicking “approve” resolves the underlying evidence problem.

&nbsp;

Branch D — Non-curative approval

A human approves A1 while a material contradictory execution/evidence condition remains unresolved. Expected EA behavior: preserve the approval as an authorization/intervention claim while retaining the contrary evidence/indeterminacy. Approval does not convert the world model to determined.

&nbsp;

Branch E — Biased world model presented to human

Upstream agents have already suppressed uncertainty or scope before presenting the case to the reviewer. The human makes a decision based on that representation. Expected EA behavior: human decision is not retroactive validation of the lost upstream qualification; F5 must preserve known lineage/gaps and requalify the affected domain if material.

&nbsp;

Branch F — Material change after approval

Action parameters, policy, reviewer roster, authority, scope or validity change after H1. Expected EA behavior: F9 triggers revalidation; previous approval is not reusable execution authority for the materially changed action.

&nbsp;

Branch G — Unresolved execution outcome / optional INDETERMINATE mapping

Intervention authorizes one bounded action, but it is unclear whether provider/action entry occurred. Expected EA behavior: preserve the unresolved execution state, refuse blind retry/reuse, and request authenticated reconciliation before return to operation. An implementation may label that state \`INDETERMINATE\`, but EA must not require the label in order to preserve the semantics.

&nbsp;

Branch H — Escalation-capacity depletion

Several consecutive uncertainty events are routed to the same human capacity pool. Each request is individually reasonable, but queue growth makes later intervention miss the useful response window. Expected EA behavior: treat human attention as capacity-binding, stop generic escalation, prioritize the material domain or choose a bounded non-human containment/requalification path.

&nbsp;

Branch I — Risk-indexed human-review contrast

Run comparable evidence under two decision profiles: high consequence/low reversibility versus low consequence/high reversibility. Expected EA behavior: justify deeper or more urgent human review in the first case while accepting bounded residual or automated fallback in the second; do not use one universal escalation threshold.

&nbsp;

# 8\. Assessment criteria

Success criteria

Nominal human presence is never confused with effective capacity.

Human decisions remain scope/authority/time-bounded.

Repeated escalation is bounded before human attention becomes the failure mode.

Approval does not erase or overwrite contrary evidence.

Upstream Type 2 is not cured merely because a human reviewed the resulting representation.

Material change invalidates reuse of the previous decision where appropriate.

Intervention history and authority history remain distinct while current operative status stays unambiguous.

&nbsp;

Measurable evidence

Human capacity status and response window recorded at decision time.

Count/duration of repeated escalation attempts.

Cumulative human-review minutes/queue depth and remaining intervention capacity after each request.

Whether additional human review changed the supported determination or only consumed attention.

Whether review delay caused a response window to become at-risk or expire.

Whether reviewer received the domain/scope required for the question.

Whether evidence status, human decision and execution decision/outcome remain separately reconstructable.

Whether prior approval is rejected after a material change.

Whether an unresolved execution outcome prevents blind retry independently of whether the implementation labels that state \`INDETERMINATE\`.

Whether F9 records revalidation before return to normal operation.

&nbsp;

# 9\. Peer baseline, similarities and differences

Shared mechanisms

HITL; review queues; approval gates; escalation; bounded mandates; action holds; audit logs; return-to-operation conditions.

&nbsp;

Theme \#16 already develops these mechanisms and remains the primary peer/owner.

&nbsp;

Existing closely related contribution

Theme \#16's consolidated working structure already states the relevant boundary: a nominal escalation should not create false assurance when the reviewer lacks system-level information, competence, authority or an adequate control frame; and a valid human approval may satisfy an authorization requirement without repairing, overwriting or concealing contrary execution evidence. UC-EA-03 therefore operationalizes/tests an existing \#16 boundary from the EA consumer perspective rather than presenting non-curative approval as a competing Theme \#16 mechanism.

&nbsp;

EA does not claim these oversight mechanisms as new.

&nbsp;

Additional EA behavior under test

Human capacity is one epistemic dependency in the broader system; EA composes it with evidence, scope, uncertainty and other domains, detects Type 1/2 caused by the oversight path, accounts for depletion of human attention as a system resource, and requalifies the system-level epistemic state after intervention.

&nbsp;

Peer reproduction question

Can an ordinary HITL architecture, without an EA-equivalent composition/requalification layer, detect that the reviewer is operating on a biased upstream world model or that caution in the oversight domain does not correct false certainty in another domain?

&nbsp;

# 10\. Non-duplication with current FG-TIDA work

Theme \#16 owns the human-oversight and intervention lifecycle. This validation profile is an interface test, not a competing oversight design. Its normative target is the consolidated lifecycle questions; \`HELD\`, \`INDETERMINATE\`, bounded mandates and admission decisions are implementation mappings where used.

Theme \#6 may supply source-native conformance verdicts, including escalate/indeterminate outcomes, which Theme \#16 may consume during trigger qualification. UC-EA-03 does not translate those verdicts into Theme \#16 or EA states; it consumes the downstream \#16 lifecycle/capacity state after the relevant handoff.

FG-TIDA Use Case \#4 includes a bidirectional \#13/\#16 capacity interface and is the preferred external stress surface for this profile. EA may consume human-oversight capacity from \#16 and return a systemic assessment that changes the appropriate intervention path, without manufacturing human authority.

&nbsp;

# 11\. Maturity, IP and confidentiality

Validation maturity: Maintenance-frozen hypothetical architecture-validation profile. Not itself a public FG-TIDA Use Case.

Reference implementation: deterministic human-capacity fixtures are recommended, including trigger-path, reviewer-availability, queue/response-window, cumulative-attention, non-curative approval, unresolved-execution and revalidation fixtures. Tests should remain valid across different Theme \#16 state-machine implementations as long as the consolidated lifecycle semantics are preserved.

Confidentiality/public boundary: Parent Case facts and Theme \#16 public lifecycle semantics may be cited externally; this profile's full branch/peer-validation apparatus remains internal working material unless deliberately surfaced. This profile is not an FG-TIDA submission.

IP note: parent facts/challenges/ToR and Theme \#16 public discussion are source-derived; EA integration requirements/test mappings are internal working contributions.

&nbsp;

# Annex A — Case Study extensibility and publication boundary

The human-capacity problem extends upward to multi-authority ecosystems, downward to a factory/production-cell supervisor/maintenance/safety arrangement, and horizontally to hospital, appointment, enterprise or logistics settings. The invariant is not a specific “manager”; it is a bounded human-held role with authority, information, time and effective intervention capacity. These are bounded extensibility tests of the Parent Case; they do not convert the single mobility use-case submission into multiple sectors or public cases.

&nbsp;

# Annex B — Terms of Reference context

Case anchors: 3.3 and 4.1.

Primary oversight anchors: 3.4; 4.3; 4.5; A.2.4.

Supporting lifecycle/control anchors: A.2.2; A.2.7; A.1.2 for authority/intervention history.

&nbsp;

# Annex C — References

[Parent Case Study package](https://github.com/dakleyer/structural-awareness-contributions/tree/main/submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change)

[Annex I — Minimal Operational Case](https://github.com/dakleyer/structural-awareness-contributions/blob/main/submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/02_ANNEX_I_Minimal_Operational_Case.md)

[Annex II — Case Extensibility](https://github.com/dakleyer/structural-awareness-contributions/blob/main/submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/03_ANNEX_II_Case_Extensibility.md)

[Annex III — Challenges Exposed by the Case](https://github.com/dakleyer/structural-awareness-contributions/blob/main/submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/04_ANNEX_III_Challenges_Exposed_by_the_Case.md)

[Annex IV — FG-TIDA Terms of Reference Mapping and Traceability](https://github.com/dakleyer/structural-awareness-contributions/blob/main/submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/05_ANNEX_IV_FG-TIDA_ToR_Mapping_and_Traceability.md)

[Live ITU-T FG-TIDA Terms of Reference](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx)

[FG-TIDA Theme \#16 — Operational Human Oversight Integration](https://github.com/FG-TIDA/themes/issues/16)

[FG-TIDA Theme \#6 — Intent-based Security Policies](https://github.com/FG-TIDA/themes/issues/6)

[FG-TIDA Use Case \#4 — Federated ecosystem defense](https://github.com/FG-TIDA/use-cases/issues/4)

&nbsp;