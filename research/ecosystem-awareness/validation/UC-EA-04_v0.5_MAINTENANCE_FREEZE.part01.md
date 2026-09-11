# UC-EA-04 — Architecture-Validation Profile — Scope-indexed Composition of Locally Valid Determinations — v0.5 — Maintenance Freeze

Derived from TIDA — Delegated Authority OS under Context Change

&nbsp;

# Status

Maintenance-frozen internal Ecosystem Awareness architecture-validation profile. Legacy identifier UC-EA-04 is retained for continuity, but this document is not an FG-TIDA use-case submission. It tests scope-indexed epistemic composition under Parent Case facts and controlled variants, including dependence, correlated evidence and cross-domain non-substitution. The Parent Case Study remains pre-freeze public working material. A future public FG-TIDA submission should remain one concrete situational use case; this profile is one validation view behind it.

&nbsp;

# 0\. Identification and traceability

Validation Profile ID: UC-EA-04 (legacy UC identifier retained for traceability).

Parent Case Study: TIDA — Delegated Authority OS under Context Change.

Public-submission boundary: the mobility instantiation remains the concrete situation. UC-EA-04 supplies the composition/interop validation profile behind that situation. Upward, downward and horizontal extensibility remain Parent Case boundary tests and may be linked publicly, but they do not turn one mobility use-case issue into a multi-sector submission.

Primary Challenge: S9 — Multi-principal composition, non-substitution & conflict.

Secondary Challenges: S11 — Policy, objective & preference integrity across domains; S14 — Evidence-to-decision assessment; S5 — Operational indeterminacy & containment.

Case-level ToR anchors: 3.3 Use cases; 4.1 Use cases and requirements analysis.

EA functions under test: F2 Decision-Relevant Window Qualification & Management where acquisition-pathway selection is exercised; F3 Local Epistemic State Qualification; F4 External Epistemic Signal Qualification; F5 Scope-Indexed Epistemic Composition & Coupling Assessment; F6 Systemic Epistemic & Operating-Frame Assessment; F7 Requalification & Corrective Directive Generation; F8 Epistemic Statement & Envelope Generation.

Principal EA hypothesis: several subsystems can be locally coherent and individually correct while the organization/system remains epistemically fragmented. Epistemic states and controls are scope-bound and non-fungible; certainty, caution, exploration or residual awareness in one domain does not compensate a failure in another domain unless the dependency actually requalifies that domain.

&nbsp;

v0.4 frozen reconciliation: **awareness-resource allocation is domain-indexed and non-fungible**. Excessive search, verification, compute or human attention in one domain does not compensate an observation window that is too narrow, stale or weakly corroborated in another domain whose ecosystem sensitivity/consequence makes that omission material. This version also fixes the \#13 boundary: Theme \#13 may construct and refine the operational affected-scope/blast-radius graph; F5 composes the epistemic dependency/inherited-indeterminacy graph needed to decide what those operational relationships establish for a specific decision. The two graphs may share nodes and edges, but neither substitutes for the other.

&nbsp;

# 1\. Functional interaction

Plain-language situation

At action time, A1 depends on several separately governed determinations: citizen authority/preferences under G1; municipal policy/applicability under P1; current context from E1; service/capacity conditions; and possibly human intervention H1. Each subsystem may correctly manage its own domain and emit a locally valid result. The relying party must determine whether those results actually compose into one sufficiently qualified current determination without one domain silently replacing another or a “balanced” average hiding multiple local epistemic failures.

&nbsp;

Actor

Citizen principal and personal agent; municipality/public principal and authorized role; bounded municipal agent where used; service/provider or capacity function where used; evidence source E1; human oversight path where used; orchestrator/aggregator/relying party.

&nbsp;

Action

Composition of local determinations into the action-time determination for A1.

&nbsp;

Decision required

Do the locally valid determinations compose into a sufficiently qualified system-level determination for A1 without silent substitution, cross-domain compensation, source duplication or epistemic laundering?

&nbsp;

Problem encountered

Multi-agent architectures often distribute work by role or domain. A route/policy agent, capacity agent, human-review function and planner may each return internally coherent outputs. Because they do not share one epistemic scope, a cautious or exploratory process in one domain may coexist with false certainty in another. Aggregation can therefore produce a sophisticated but globally incoherent world model.

&nbsp;

Current mitigation

Orchestrator-workers; voting/debate; evaluator/critic; confidence aggregation; HITL; provenance; policy checks; multi-agent planning; evidence fusion.

&nbsp;

Residual gap being tested

Whether the architecture keeps E(d) = [A_d, B_d, C_d, D_d] indexed by domain; preserves dependencies and source lineage; detects cross-domain compensation, closure laundering and correlated evidence; and emits a systemic determination that does not average away local imbalance. v0.2 additionally tests whether the system keeps **observation burden and ecosystem sensitivity/capacity indexed by domain**, so that over-observation in one place cannot cosmetically balance under-observation in another.

&nbsp;

# 2\. Parent Case Study facts inherited unchanged

Case Study identity

TIDA — Delegated Authority OS under Context Change is the parent Case Study. The minimal instantiation deliberately contains multiple non-substitutable authority domains and a context change that requires one current action-time determination.

&nbsp;

Core actors

Citizen principal and personal agent/instance under G1.

Municipality/public principal and authorized municipal role under P1.

Bounded municipal agent where used.

One mobility commitment C1 based on decision D1.

Approved observation source E1 and threshold Qnormal/Qcritical.

Later intervention H1 where applicable.

&nbsp;

Key composition fact

Private and public authority records are not competing models: they compose while preserving non-substitutable limits. A personal preference cannot waive P1, and P1 cannot rewrite the citizen’s preferences or create authority beyond its mandate.

&nbsp;

T0 — Setup

G1/P1 and source E1 are current.

&nbsp;

T1 — Commitment

D1/C1 are created using current authority, preferences, timing, price, capacity data and decision basis.

&nbsp;

T2 — Context change

E1 reports Qcritical crossed; P1 requires reassessment. The system must combine the current authority, context, evidence, capacity and any intervention state into one action-time determination.

&nbsp;

Nested objective extension

Annex II allows objectives and KPIs to be decomposed into nested objective systems with owner, scope, priority, hard/soft status, KPI/target, measurement source, time horizon, dependencies and escalation condition. A lower-level objective does not gain authority merely because it is optimized.

&nbsp;

Governing regime

The legal regime is not yet frozen and remains TBD.

&nbsp;

# 3\. Domain-indexed composition model under test

The validation profile models several material domains without asserting that these are the only possible decomposition:

d1 — citizen authority, commitment and hard-limit domain;

d2 — municipal policy/applicability domain;

d3 — current context/evidence domain;

d4 — service/capacity domain where relevant;

d5 — human intervention/capacity domain where H1 is used.

&nbsp;

For each domain, EA maintains a qualified epistemic position E(d) = [A_d, B_d, C_d, D_d] at the abstraction required for the decision. Where adaptation matters, the same position is read as E(d,t) together with that domain's current ecosystem-sensitivity/consequence, tolerated-residual and observation/determination-capacity profile.

&nbsp;

General composition rule

&nbsp;

A control or cautious state in d2 does not compensate an epistemic error in d1 unless d2 materially requalifies d1 or a demonstrated dependency through which d1 is inferred.

Operational / epistemic graph boundary

Operational/epistemic graph boundary: \#13 incident infrastructure may answer “what agents, services, actions or downstream assets are observed or potentially affected?” EA/F5 answers “what decision-relevant conclusions inherit uncertainty or dependence through those relations, which corroborations are genuinely independent, and which domains remain unresolved?” EA may request targeted blast-radius/dependency refinement from \#13 when a particular branch could change the decision, but it does not duplicate the \#13 graph engine.

&nbsp;

Examples

Type2(d1) + Type1Control(d5) ≠ epistemic balance.

Type2(d2) + exploration(d4) ≠ correction(d2).

HumanApproval(d5) ≠ validation(d1/d2/d3) unless the review actually requalifies those domains.

Many locally independent roles ≠ many independent evidence sources.

OverObservation(d5) + UnderObservation(d3) ≠ balanced awareness.

High compute/token volume(d4) ≠ sufficient window(d2/d3).

&nbsp;

# 4\. Challenge traceability

Challenge S9 — Multi-principal composition, non-substitution & conflict

The Challenge asks whether independently valid citizen, employer/provider/operator/public authorities can compose without one silently replacing another. It tests concurrence, conflict, priority, hold and escalation without assuming one universal hierarchy.

Primary ToR anchors: 2 Scope; 4.2 architectures for identity/trust/agent discovery/interoperability; A.2.1 agentic AI trust management; A.2.5 trust interoperability; A.2.7 trust control plane.

&nbsp;

Challenge S11 — Policy, objective & preference integrity across domains

The Challenge asks whether each policy, objective and preference retains owner/source, version, scope, priority and conditions across public/private systems, organizations or jurisdictions; whether lower-priority preferences avoid overwriting hard limits; and whether one actor’s policy/objective/preference avoids substituting for another’s merely because both concern the same action.

Primary ToR anchors: 4.4 technical-policy and machine-readable trust metadata; A.1.5 access-policy languages; A.2.5 trust interoperability. Supporting anchor: 4.2.

&nbsp;

Challenge S14 — Evidence-to-decision assessment

The Challenge asks what must be demonstrated, what evidence is required, whether that evidence is sufficient/insufficient/inconclusive, and which decision it supports.

Primary ToR anchors: 3.4; 4.5; A.2.2; A.2.4.

&nbsp;

Challenge S5 — Operational indeterminacy & containment

The Challenge requires the system to manage indeterminacy created by incomplete/conflicting/stale facts and composition rather than silently convert it to permission.

Primary ToR anchors: 3.4; 4.3. Supporting: A.2.2; A.2.7.

&nbsp;

# 5\. EA functional traceability

F3 qualifies each local subsystem closure with scope/window/uncertainty/dependency state.

F4 performs the equivalent qualification for external/independently governed sources.

F5 is the primary function under test: compose by domain, preserve source/dependency graphs, detect cross-domain compensation, conflicting closures, correlated/duplicated evidence, inherited uncertainty loss and locally coherent/global fragmented states. In v0.2 it also preserves whether the awareness burden and capacity state relevant to each domain are materially mismatched to that domain's sensitivity/consequence profile.

F6 evaluates whether the composed epistemic state is sufficient for the current operating frame and produces the current scope-indexed posture. It may also expose a sensitivity/capacity mismatch wit