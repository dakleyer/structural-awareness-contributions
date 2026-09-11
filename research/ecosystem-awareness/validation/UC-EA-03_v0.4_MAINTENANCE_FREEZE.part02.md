H1 or other intervention and prevents old approval from being reused after material change.

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

[Annex I — Minimal Operational Case](https://github.com/dakleyer/structural-awareness-contributions/blob/main/submissions/it