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

The challenge asks whether unavoidable indeterminacy from incomplete, conflicting or stale authority facts, preferences and delegations can be managed rather than silently converted into permission; whether uncertainty is bounded; evidence and canonical links are preserved; and hold, rollback or escalation paths exist before downstream effects lea