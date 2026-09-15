# UC-EA-01 — Architecture-Validation Profile — Action-time Operating-Frame Requalification under Context Change — v0.3 — Frozen

Derived from TIDA — Delegated Authority OS under Context Change

&nbsp;

# Status

Frozen internal Ecosystem Awareness architecture-validation profile. Legacy identifier UC-EA-01 is retained for continuity, but this document is not an FG-TIDA use-case submission and must not be presented as one. It tests the EA architecture against a bounded scenario derived from the public Parent Case Study. The Parent Case Study remains pre-freeze public working material; this profile must not change its facts to obtain a preferred result. Public representation, if filed, should be one situational FG-TIDA Use Case derived from the Parent Case rather than four architecture-validation submissions.

&nbsp;

# 0\. Identification and traceability

Validation Profile ID: UC-EA-01 (legacy UC identifier retained for traceability).

Parent Case Study: TIDA — Delegated Authority OS under Context Change.

Public-submission boundary: the concrete mobility instantiation may be surfaced through a single situational FG-TIDA Use Case (working title: “Reassessing a delegated mobility commitment after a critical context change”). UC-EA-01 remains the internal validation profile behind that situation, not a separate public use-case record.

Extensibility boundary: mobility is the bounded concrete instantiation. Upward, downward and horizontal extensibility remain properties of the Parent Case and are referenced through Annex II; they do not silently add sectors, actors or facts to this profile.

Primary Challenge: S3 — Regime, context, escalation & bounded escape path.

Secondary Challenges: S10 — Commitment state, material change & normal escalation; S14 — Evidence-to-decision assessment; S5 — Operational indeterminacy & containment.

Case-level ToR anchors: 3.3 Use cases; 4.1 Use cases and requirements analysis.

EA functions under test: F1 Mission & Decision Context Qualification; F2 Decision-Relevant Window Qualification & Management; F5 Scope-Indexed Epistemic Composition & Coupling Assessment; F6 Systemic Epistemic & Operating-Frame Assessment; F7 Requalification & Corrective Directive Generation; F9 Outcome Feedback & Revalidation.

Principal EA hypothesis: a determination that was justified at T1 may cease to be sufficiently qualified at T2 even if no upstream component is individually malfunctioning. The system must be able to requalify the decision-relevant window and operating frame rather than merely execute a pre-existing trigger.

&nbsp;

v0.3 frozen reconciliation: this profile is now explicitly classified as an architecture-validation profile rather than an FG-TIDA submission. The same observable context change can justify different awareness/requalification effort depending on mission sensitivity/exposure, consequence severity, reversibility, tolerated residual, available observation/determination capacity and remaining response horizon. The test therefore evaluates W(d,t), not maximum context collection. Any public use-case issue should expose the concrete situation and relying-party decision first, while this profile retains the deeper architecture-validation branches, peer baseline and falsification logic.

&nbsp;

# 1\. Functional interaction

Plain-language situation

A citizen’s personal agent has created commitment C1 under citizen grant G1 and municipal policy/mandate P1. Before execution, approved source E1 reports that Qcritical has been crossed; P1 requires reassessment and temporarily disallows entry to the affected zone unless an authorized exceptional intervention H1 applies. The relying decision must determine whether the T1 determination can still be used at action time, or whether the system must reroute, hold, enter a bounded intervention path, remain indeterminate, contain, or requalify the operating frame.

&nbsp;

Actor

Citizen principal; citizen personal agent and relevant agent instance; municipality/public principal; authorized municipal role; bounded municipal agent where used; evidence source E1; relevant relying party/action-admission function; human authority where H1 is invoked.

&nbsp;

Action

Action A1 associated with executing the mobility commitment C1 under the current G1/P1 conditions after the T2 context change.

&nbsp;

Decision required

May the determination that justified D1/C1 at T1 still be relied upon for A1 at T2, and if not, what requalification and operating posture are justified?

&nbsp;

Problem encountered

A conventional trigger or policy engine may correctly detect Qcritical and still fail to determine whether the epistemic frame supporting the earlier commitment remains sufficient. The system may therefore over-rely on the earlier closure, over-escalate, or rebuild context without a bounded criterion.

&nbsp;

Current mitigation

Policy/runtime conformance re-evaluation; fresh telemetry; ordinary orchestration; human escalation; rerouting/containment where already defined.

&nbsp;

Residual gap being tested

Whether the architecture explicitly treats the current observation/context window W(d,t) and operating envelope as requalifiable state, separates epistemic condition from operational posture, and directs a bounded response to the affected domain instead of equating “more checking” with correction. v0.2 also tests whether the window burden is proportionate to the mission's actual sensitivity and finite capacity.

&nbsp;

# 2\. Parent Case Study facts inherited unchanged

Case Study identity

TIDA — Delegated Authority OS under Context Change is a candidate shared Case Study intended to expose interfaces among authority, delegation, context, human oversight, evidence and action-time decisions. The concrete mobility narrative is the minimal instantiation, not the domain boundary of the Case Study.

&nbsp;

Actors and authority

The restricted case contains a citizen as human principal; the citizen’s personal agent and relevant agent instance acting under G1; a municipality as public principal; an authorized municipal role and, where used, a bounded municipal agent operating under P1; and one mobility commitment C1. Principal, organization/role, acting agent and agent instance remain distinguishable.

&nbsp;

Private and public authority do not substitute for one another. A personal preference cannot waive P1, and P1 cannot rewrite the citizen’s preferences or create authority beyond its mandate.

&nbsp;

Decision concepts

Preference: desired outcome or trade-off declared by a principal; it does not itself confer authority.

Policy: condition applicable in a defined context; it requires valid origin and applicability.

Grant: authority conferred on an agent within stated bounds.

Decision: selection or commitment made under a grant; it is valid only under current grants, policies and context.

&nbsp;

Operational sequence

T0 — Setup. The citizen issues G1 with hard limits, tradeable preferences and permitted commitments. An authorized municipal role issues P1, including Qnormal/Qcritical and approved observation source E1. Visible evidence includes identities and role mandates, current G1/P1 versions and validity periods, the preference profile, threshold definition and source provenance. The personal agent may plan only inside G1 and P1.

&nbsp;

T1 — Commitment. The personal agent selects an option and records D1 and C1. Visible evidence includes G1 and P1 at commitment time, timing, price and capacity data, decision basis and commitment terms. C1 may be created only if authority and hard limits are sufficiently established; otherwise the system holds or escalates.

&nbsp;

T2 — Context change and action-time determination. Before execution, E1 shows that Qcritical has been crossed. P1 defines crossing as a reassessment trigger and temporarily disallows entry to the affected zone unless authorized exceptional intervention H1 applies. The system must determine the operative authority for A1: reroute and proceed with limits, hold, use a bounded escalation path, or return INDETERMINATE where evidence or applicability cannot be sufficiently established.

&nbsp;

Records

G1 and P1 remain authority/provenance records. D1 and C1 record the decision and commitment. H1 records any later intervention, its authority, evidence and operational effect. None overwrites another.

&nbsp;

Human oversight boundary

A human role may be formally authorized yet unavailable, overloaded, insufficiently informed, unable to understand the case in time or unable to intervene effectively. A nominal role does not manufacture usable capacity or permission.

&nbsp;

Governing regime

The parent Case Study states that the governing legal regime should be declared before freeze where mandate validity, standing or revocation is tested. That regime is not fixed in the current pre-freeze source; this validation profile therefore records it as TBD rather than inventing it. This unresolved Parent Case fact is a freeze gate for any public submission that requires a concrete governing regime, not an invitation to infer one inside EA.

&nbsp;

# 3\. Mandates and authority objects used in this validation profile

G1 — Citizen principal → personal agent / relevant agent instance. Bounded authority to make permitted mobility decisions and commitments within hard limits and tradeable preferences. Governing legal regime: TBD in parent pre-freeze Case Study.

&nbsp;

P1 — Authorized municipal role / public authority. Current policy or mandate defining applicable public conditions, Qnormal/Qcritical, approved source E1 and the T2 reassessment consequence. Governing legal regime: TBD in parent pre-freeze Case Study.

&nbsp;

H1 — Exceptional intervention record, if used. H1 is not treated as a rewrite of G1/P1. It records the later intervention, its authority, evidence and operational effect.

&nbsp;

# 4\. Challenge traceability

Challenge S3 — Regime, context, escalation & bounded escape path

The challenge asks whether a continuously operating system can distinguish normal escalation from an exceptional escape path when context changes. It requires the system to identify who/what may detect and declare the exceptional condition, evidence/thresholds, affected scope, what leaves the ordinary frame, what remains valid, and conditions for review and return. Emergency detection/response must be authenticated and bounded so a false signal cannot silently expand permissions or trigger system-wide suspension.

Primary ToR anchors: 4.3 Trust framework(s) and lifecycle management; A.2.2 trust lifecycle; A.2.4 human oversight integration; A.2.8 behavioural trust signals.

&nbsp;

Challenge S10 — Commitment state, material change & normal escalation

The challenge asks whether the system can distinguish recommendation, negotiation, reservation, binding commitment and execution, and detect when material change of cost, route, time, context, policy or authority requires confirmation, revalidation, cancellation or change of authority. Silence/delay must not become permission.

Primary ToR anchors: 4.3; A.2.2. Supporting anchor: A.2.7 trust control plane.

&nbsp;

Challenge S14 — Evidence-to-decision assessment

The challenge asks whether each transition can state what must be demonstrated, what evidence is required, whether the evidence is sufficient/insufficient/inconclusive, and which decision it can support.

Primary ToR anchors: 3.4 Security assessment criteria and benchmarks; 4.5 guidelines, metrics and standardization recommendations; A.2.2; A.2.4.

&nbsp;

Challenge S5 — Operational indeterminacy & containment

The challenge asks whether unavoidable indeterminacy from incomplete, conflicting or stale authority facts, preferences and delegations can be managed rather than silently converted into permission; whether uncertainty is bounded; evidence and canonical links are preserved; and hold, rollback or escalation paths exist before downstream effects leave control.

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

Downward extension reduces the setting to a private factory or production cell while preserving bounded authority, scarce capacity and runtime change.

Horizontal extension changes service domain — for example appointments, hospital capacity, school rooms/specialist time, compute allocation or logistics — while preserving the same structural distinctions.

Extension fails when the new situation cannot be represented by adding actors, roles, grants, constraints, resources or commitments without redefining the core concepts. At that boundary, a different frozen Case Study should be created. For publication, these extension directions are referenced as evidence of bounded reuse; they are not additional facts or sectors of the mobility use-case issue itself.

&nbsp;

# Annex B — Terms of Reference context

The live FG-TIDA ToR defines the group scope around trust management and interoperable identity for humans and agentic AI in multi-actor ecosystems; identifies use cases under 3.3 and security assessment/benchmarks under 3.4; and defines deliverables for use-case requirements (4.1), architectures (4.2), trust lifecycle (4.3), machine-readable trust metadata (4.4) and metrics/recommendations (4.5).

Relevant Annex A anchors include A.2.1 agentic AI trust management, A.2.2 trust lifecycle, A.2.4 human oversight, A.2.7 trust control plane and A.2.8 behavioural trust signals.

&nbsp;

# Annex C — References

[Parent Case Study package](https://github.com/dakleyer/structural-awareness-contributions/tree/main/submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change)

[Annex I — Minimal Operational Case](https://github.com/dakleyer/structural-awareness-contributions/blob/main/submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/02_ANNEX_I_Minimal_Operational_Case.md)

[Annex II — Case Extensibility](https://github.com/dakleyer/structural-awareness-contributions/blob/main/submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/03_ANNEX_II_Case_Extensibility.md)

[Annex III — Challenges Exposed by the Case](https://github.com/dakleyer/structural-awareness-contributions/blob/main/submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/04_ANNEX_III_Challenges_Exposed_by_the_Case.md)

[Annex IV — FG-TIDA Terms of Reference Mapping and Traceability](https://github.com/dakleyer/structural-awareness-contributions/blob/main/submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/05_ANNEX_IV_FG-TIDA_ToR_Mapping_and_Traceability.md)

[Live ITU-T FG-TIDA Terms of Reference](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx)

[FG-TIDA Use Case \#4 — Federated ecosystem defense](https://github.com/FG-TIDA/use-cases/issues/4)

[FG-TIDA use-cases PR \#2 — Regulated financial services](https://github.com/FG-TIDA/use-cases/pull/2)

[FG-TIDA Theme \#16 — Operational Human Oversight Integration](https://github.com/FG-TIDA/themes/issues/16)

&nbsp;