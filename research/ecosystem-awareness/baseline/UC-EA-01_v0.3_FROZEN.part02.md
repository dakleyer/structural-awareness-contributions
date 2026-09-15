ve control.

Primary ToR anchors: 3.4; 4.3. Supporting anchors: A.2.2; A.2.7.

&nbsp;

# 5\. EA functional traceability

F1 consumes mission, decision, criticality, ecosystem sensitivity/exposure, consequence/reversibility, tolerated residual, finite observation/determination capacity, authority and available response capability to define what determination is required at T2.

F2 qualifies the current decision-relevant window W(d,t), including what remains inside, what could be brought in, what residual remains outside any guarantee, and whether additional observation is proportionate to the sensitivity/capacity profile.

F5 composes the current authority, context, evidence and capacity states without treating a T1 closure as automatically current.

F6 separately assesses epistemic condition and operating posture.

F7 issues targeted requalification directives: refresh a specific source, widen/narrow/redirect W(d), preserve INDETERMINATE, request bounded human review, reduce scope, contain, or prepare migration/requalification.

F9 compares the observed T2 condition and subsequent action outcome with the assumptions under which D1/C1 were established and re-enters the appropriate loop. It also records whether the chosen awareness burden was too high (wasted requalification/capacity depletion) or too low (missed material change/stale-frame exposure).

&nbsp;

Primary failure surfaces

I0 determination capacity; I1 bounded determination effort; I2 epistemic honesty; O0 structural residual; O1 bounded window expansion; O2 non-collapse of W into ecosystem; relevant external-signal E-surfaces where E1 or another source supplies the context change.

&nbsp;

# 6\. Requirements

R1. The system shall preserve the distinction between the T1 commitment decision and the T2 action-time determination.

R2. The system shall expose or derive a qualified current window/scope sufficient to state what evidence and context support the T2 determination.

R3. A material context change shall trigger requalification of the affected domain rather than automatic reuse of the T1 closure.

R4. The system shall distinguish a recognized Type 0 structural residual from Type 1 unbounded determination and Type 2 false certainty.

R5. Window expansion, retrieval, escalation and human review shall have bounded stopping/requalification conditions proportional to the current mission sensitivity/exposure, consequence/reversibility, available observation/human capacity and response horizon.

R6. The system shall not treat absence from the current window as absence from the ecosystem.

R7. F6 shall keep epistemic condition separate from Normal / Containment-Mitigate / Migration-Regime-Transition posture.

R8. Any corrective directive shall target the affected domain or a demonstrated material dependency rather than add generic checking elsewhere.

R9. Where evidence/applicability cannot be sufficiently established, INDETERMINATE shall remain a legitimate result and shall not be converted into silent permission.

R10. Outcome evidence shall be sufficient to determine whether the previous frame may be reused, must be revised, or must be abandoned/requalified.

R11. The test shall record the sensitivity/exposure and finite-capacity assumptions used to justify W(d,t); different branches may vary those assumptions without altering the parent Case Study facts.

R12. A lower-sensitivity/reversible branch shall not be forced into broad requalification merely because a wider window is technically available.

R13. A higher-sensitivity/irreversible branch shall not reuse a narrow or stale window solely to reduce observation cost.

&nbsp;

# 7\. Test and stress-test branches

Branch A — Positive Normal control

No material change invalidates the T1 frame. Current G1/P1 and supporting evidence remain sufficiently qualified. Expected EA behavior: retain Normal posture; do not expand W or escalate merely because residual uncertainty exists.

&nbsp;

Branch B — Context change with known bounded response

Qcritical is crossed as in T2, the trigger is authentic/current, and a known reroute or scope-reduction path preserves a sufficiently qualified frame. Expected EA behavior: requalify the affected domain and select Containment/Mitigation or bounded reroute as appropriate; do not treat the old D1/C1 as current without reassessment.

&nbsp;

Branch C — Incomplete action-time qualification

Qcritical is reported but scope/applicability/freshness of one material input is insufficient. A specific additional source can reasonably resolve the question within the useful response window. Expected EA behavior: targeted bounded expansion/retrieval; preserve indeterminate until resolved; no blind reuse of T1 certainty.

&nbsp;

Branch D — Type 1 stress

Repeated retrieval, escalation or human review continues after the justified determination path has been exhausted or the useful response window has passed. Expected EA behavior: detect Type 1 and stop unbounded determination; move to bounded operational closure, containment or requalification.

&nbsp;

Branch E — Type 2 stress

The system treats D1/C1, a stale policy status, or an incomplete external signal as sufficient current determination after T2. Expected EA behavior: detect false certainty and requalify.

&nbsp;

Branch F — Regime-transition stress

A test variant deliberately introduces evidence that the assumptions supporting the normal control/oversight frame no longer provide a sufficiently qualified response mapping. This is a stress-test variant, not a frozen parent fact. Expected EA behavior: preserve any known invariant safe actions while selecting Migration/Regime Transition rather than endlessly attempting to restore the old frame.

&nbsp;

Branch G — High-sensitivity / narrow-window stress

The T2 change is materially coupled to a high-consequence or difficult-to-reverse domain, while the baseline reuses the minimum context it used for a lower-sensitivity condition. Expected EA behavior: widen/refresh/redirect W(d,t) only for the material domain, preserving the reason for the stronger awareness requirement.

&nbsp;

Branch H — Low-sensitivity / over-requalification stress

The same class of change affects a reversible/low-consequence domain with a known bounded fallback, while a baseline performs broad system-wide revalidation. Expected EA behavior: retain or narrow the qualified window, use the bounded response, and avoid unnecessary retrieval/verification/human escalation.

&nbsp;

Branch I — Capacity-constrained response-window stress

Additional evidence is potentially available but collecting it would consume enough time or human/compute capacity that the effective response option would expire. Expected EA behavior: compare decision value to the remaining response horizon and prefer bounded closure/containment over epistemic perfectionism.

&nbsp;

# 8\. Assessment criteria

Success criteria

The same Case Study facts produce a current T2 determination that is distinguishable from the T1 commitment.

Normal operation remains possible when residual uncertainty is correctly bounded and material assumptions remain qualified.

A known bounded response is selected without unnecessary global escalation.

Unbounded retrieval/escalation is detected as Type 1\.

Stale/local closure is not promoted to current ecosystem truth.

When the old response mapping is no longer sufficiently qualified, the architecture can indicate Migration/Regime Transition without confusing that posture with Type 0/1/2.

&nbsp;

Measurable evidence

Whether W(d,t), its sensitivity/capacity selection basis and its revalidation condition are explicit.

Whether each material input has scope/freshness/provenance or an explicit UNKNOWN qualifier.

Number and duration of requalification steps before bounded closure.

Observation/requalification burden: retrieval/tool calls, compute/tokens, latency, bandwidth/privacy burden and human-review time.

Whether additional observation changed the decision or merely consumed capacity.

Whether a material context change was missed or handled on a stale/narrow frame.

Whether response options remained available after the chosen requalification effort.

Whether action/posture changes target the affected domain.

Whether prior D1/C1 remains historically recorded but not silently treated as current.

Whether outcome feedback reaches F9 and re-enters the appropriate function.

&nbsp;

# 9\. Peer baseline, similarities and differences

Shared mechanisms already present in peer architectures

Runtime policy/conformance evaluation; retrieval/context refresh; telemetry; HITL/escalation; guardrails; orchestration; containment; persistent state and tracing.

&nbsp;

EA does not claim these mechanisms as new.

&nbsp;

Additional EA behavior under test

Mission/sensitivity/finite-capacity-driven qualification of W(d,t); explicit in-window/out-of-window distinction; four-pole epistemic position; Type 0/1/2 classification; separate epistemic condition and operating posture; targeted requalification of the same domain; selective re-entry through the double loop; and the ability to choose less rather than more observation when additional awareness has low decision value.

&nbsp;

Peer reproduction question

Can the peer composition reproduce the same behavior under the frozen facts without adding a new layer that tracks window sufficiency, external epistemic qualification, structural residual and domain-indexed composition? If yes, the novelty claim must be reduced accordingly.

&nbsp;

# 10\. Non-duplication with current FG-TIDA use cases

FG-TIDA Use Case \#4 focuses federated ecosystem defense, cross-organizational signals, affected scope and coordinated containment. UC-EA-01 does not redefine its incident-signal lifecycle; it tests whether the local/system operating frame remains epistemically qualified after context change. Where this profile is exercised in Nelson's Stage 1 testbed, \#13 may provide incident/signal state and affected-scope or dependency refinement, while EA remains responsible for the decision-scoped systemic requalification.

&nbsp;

Financial-services PR \#2 focuses runtime enforcement/conformance and AVS-0.2 appraisal vectors. UC-EA-01 consumes valid verdicts/appraisal outcomes as evidence; it does not redefine conformance semantics.

&nbsp;

Theme \#16 owns the human-oversight lifecycle. UC-EA-01 may consume human-capacity state but does not implement the oversight mechanism itself.

&nbsp;

# 11\. Maturity, IP and confidentiality

Validation maturity: Frozen hypothetical architecture-validation profile. Not itself a public FG-TIDA Use Case.

Reference implementation: none required for the frozen profile. Deterministic fixtures are recommended for later testing, with controlled sensitivity/capacity parameters so the same Parent Case facts can be rerun under comparable low/high sensitivity and fixed/adaptive window configurations. External Stage 1 interoperability testing may exercise this profile without modifying F1–F9; architecture reopening is warranted only if a required responsibility has no existing owner.

Confidentiality/public boundary: public-source-derived Parent Case facts may be cited externally; the internal challenge decomposition, peer-baseline and architecture-validation apparatus remain working material unless deliberately surfaced. This profile is not an FG-TIDA submission.

IP note: the document reuses public working Case Study facts and challenge/ToR traceability; Ecosystem Awareness requirements and test mappings are internal working contributions.

&nbsp;

# Annex A — Case Study extensibility and public-scope boundary

Upward extension adds principals, agents, services, role chains, objective layers and jurisdictions without redefining principal, role, agent, authority, preference, policy, grant, commitment or decision.

Downward extension reduces the setting to a private factory or production cell while preserving bounded authorit