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

F6 evaluates whether the composed epistemic state is sufficient for the current operating frame and produces the current scope-indexed posture. It may also expose a sensitivity/capacity mismatch without collapsing that mismatch into a new Type.

F7 directs requalification to the specific domain/dependency causing imbalance, including reducing low-value awareness effort in one domain or increasing/redirecting observation in another when that is what the domain-specific sensitivity/capacity profile requires.

F8 emits an internal/system or external epistemic statement that preserves scope, uncertainty semantics, inherited indeterminacy and relevant residual without exposing private reasoning.

&nbsp;

Primary failure surfaces

I2/O2 are central for preventing local closure and local windows becoming ecosystem truth. I1/O1 matter where one domain becomes an unbounded verification/search sink. E-surfaces matter for every cross-agent/domain handoff.

&nbsp;

# 6\. Requirements

R1. Every material local determination used in composition shall remain bound to a domain/scope sufficient to interpret its claim.

R2. The system shall not aggregate epistemic positions by assuming that caution, uncertainty or verification in one domain compensates false certainty in another.

R3. The system shall preserve non-substitution between independently valid authority/policy/preference domains.

R4. Local certainty shall not be promoted to ecosystem certainty solely because the local subsystem is authoritative within its scope.

R5. A system shall preserve known source dependence and shall not count duplicated/derived claims as independent corroboration.

R6. A multi-agent sectioning pattern shall not be treated as a multiple-opinion pattern unless more than one agent actually evaluates the same material proposition/domain.

R7. A human approval, policy verdict, attestation result or evaluator output shall retain the epistemic question/scope it actually addresses.

R8. F5 shall expose coupled epistemic imbalance when multiple domains contain different Type 0/1/2 conditions.

R9. Corrective action shall be directed to the affected domain or a demonstrated material dependency.

R10. The final system-level statement shall preserve domain-level unresolved state sufficiently to prevent closure laundering downstream.

R11. Agent count, vote count or token/compute volume shall not be treated as substitutes for epistemic independence.

R12. The system shall be able to remain operational where locally different epistemic positions are legitimate, provided the composition remains sufficiently qualified for the mission.

R13. Observation, verification, compute or human-attention effort in one domain shall not compensate an observation-window deficiency in another domain unless a demonstrated dependency actually requalifies that domain.

R14. The test shall preserve per-domain awareness budgets/sensitivity assumptions sufficiently to distinguish broad coverage from proportionate allocation of awareness resources.

&nbsp;

R15. Distinct acquisition pathways, transports or providers shall not be treated as independent epistemic evidence solely because their pathway identities differ. Evidence independence is a separate qualified relation and remains UNKNOWN where upstream lineage cannot be established.

R16. An operational affected-scope or blast-radius graph supplied by Theme \#13 shall remain distinguishable from EA's decision-relative epistemic dependency/inherited-indeterminacy graph; shared nodes or edges do not merge ownership of the two functions.

R17. EA may request targeted refinement of a \#13 blast-radius/dependency branch only where the unresolved relation is materially capable of changing the receiving decision; it shall not request exhaustive ecosystem graph completion by default.

R18. The interoperability claim shall not be considered established until at least one external cross-implementation campaign demonstrates that a source-native result from an independently governed non-EA producer or consumer can be exchanged through EHD and any applicable Theme profile while preserving material scope, provenance/lineage, UNKNOWN qualification and native semantics without requiring shared internal assessment logic.

FG-TIDA Use Case \#4 Stage 1 is the preferred current fixture for this validation, but it is not a normative dependency of the EA profile.

&nbsp;

# 7\. Test and stress-test branches

Branch A — Healthy heterogeneous composition

Citizen, municipal, context and capacity domains each supply sufficiently qualified current states. Different domains have different uncertainty levels, but each is correctly scoped. Expected EA behavior: compose without forcing uniform confidence; permit Normal/appropriate posture if mission sufficiency is met.

&nbsp;

Branch B — Cross-domain compensation fallacy

The municipal/context domain contains a Type 2 closure, while the human oversight domain is extremely cautious and repeatedly escalates. Expected EA behavior: do not treat system as balanced; preserve Type2(d2/d3) and Type1(d5) as coupled imbalance.

&nbsp;

Branch C — Sectioning without corroboration

Several worker agents each inspect a different part of the system and return local closures. The orchestrator interprets the number of agents as diversified evidence. Expected EA behavior: record broad coverage but no second opinion for the same propositions unless actual overlap/independence exists.

&nbsp;

Branch D — Correlated consensus

Multiple agents evaluate the same proposition but derive their evidence from the same source or copied upstream closure. Expected EA behavior: consensus does not count as independent corroboration; source dependence remains visible.

&nbsp;

Branch E — Closure laundering

A local subsystem has rich epistemic state including unresolved dependencies but exports only PASS/normal. A downstream aggregator treats PASS as determined fact. Expected EA behavior: F3/F5 detect or preserve the missing qualification when known and prevent the output from being promoted beyond its justified scope.

&nbsp;

Branch F — Creativity in the wrong domain

A planning/exploration function expands alternatives in d4 while the unresolved material Type 2 condition remains in d2/d3. Expected EA behavior: exploration in d4 is not classified as correction of d2/d3.

&nbsp;

Branch G — Human caution in the wrong domain

Oversight becomes very conservative and asks repeated questions about d5, but the upstream evidence defect is in d3. Expected EA behavior: identify that the human path has not requalified d3; repeated caution does not cancel upstream false certainty.

&nbsp;

Branch H — Multi-million-token stress

A test harness executes many agents, searches, critics and approvals but keeps producing and recomposing differently scoped closures without preserving epistemic qualification. Expected EA behavior: the compute volume does not count as evidence of balance; the final determination remains limited by the unresolved coupled imbalance.

&nbsp;

Branch I — Asymmetric awareness allocation

A low-sensitivity/reversible domain consumes extensive search, debate or human review, while a high-sensitivity material context/authority domain is evaluated from a narrow or stale window. A naive system appears globally cautious because total verification effort is high. Expected EA behavior: preserve the per-domain mismatch; stop/narrow low-value effort in the first domain and requalify the actual high-sensitivity domain. Total effort is not an averaging variable.

&nbsp;

Branch J — Equal-budget / unequal-sensitivity comparison

Two material domains receive the same observation budget even though one has substantially greater consequence/irreversibility or sensitivity to ecosystem change. Expected EA behavior: reject equal allocation as a definition of balance and justify different W(d,t) burdens without changing the underlying epistemic categories.

&nbsp;

Branch K — Nominally distinct acquisition pathways with shared upstream lineage

Pathway A and Pathway B are different transports/providers and present separate qualified messages, but both material claims derive from upstream source X. Pathway C is less frequent, slower or otherwise operationally less attractive, but its material evidence derives from an independent source Y. The unresolved decision domain specifically benefits from independent corroboration.

&nbsp;

Expected EA behavior: F2.APQ may consider the available pathways, F4 qualifies each received result, and F5 preserves the distinction between pathway diversity and evidence independence. A+B must not become two independent corroborations merely because the transports/providers differ. Where the additional independent evidence is decision-relevant and timely, C may have greater marginal epistemic value despite weaker generic operational characteristics. If the A/B lineage relation or C independence cannot be established, the corresponding relationship remains UNKNOWN. The strong peer baseline is allowed to track correlation/source lineage; if it reproduces the behavior without EA-equivalent semantics, differentiation is reduced.

&nbsp;

Apply UC-EA-02 APQ-PARTIAL and APQ-CONFLICT as cross-cutting profiles to Branch K where the lineage/property evidence is incomplete or the pathway operator has divergent incentives.

&nbsp;

External Stage 1 interoperability campaign — not a new Branch L. Use two independently governed implementations. \#13 may provide the operational incident/affected-scope graph and a source-native signal state; EA consumes the EHD/\#13 profile, builds only the decision-relative epistemic coupling needed for the case, and may return a targeted request to refine one operational dependency. The campaign passes when both graphs remain distinguishable, the producer's native semantics survive, and neither side needs the other's internal algorithm.

&nbsp;

# 8\. Assessment criteria

Success criteria

Locally valid but differently scoped states are preserved without forced homogenization.

Cross-domain Type 1/2 conditions remain visible rather than averaging to “balanced.”

Coverage is distinguished from corroboration.

Consensus is distinguished from evidence independence.

Human approval and exploration are recognized as domain-specific mechanisms.

Closure laundering is detected/prevented where qualification is available.

A final system statement identifies affected domains and unresolved couplings.

Operational blast radius and epistemic dependency/inherited-indeterminacy remain separately inspectable even where they reuse the same underlying relationship evidence.

A non-EA producer/consumer can participate through EHD/\#13-profile semantics without adopting EA's internal composition logic.

&nbsp;

Measurable evidence

Number of material domains with explicit scope/qualification.

Whether duplicated sources are identified in the dependency graph.

Whether agent count is distinguished from independent-evidence count.

Whether the system preserves separate Type1/Type2 states by domain.

Whether the requalification directive targets the actual failing domain.

Per-domain observation/retrieval/compute/human-attention burden and remaining capacity.

Whether awareness resources are reallocated toward the domain where added observation materially changes decision support.

Whether high total system effort masks a stale/narrow window in a material domain.

Whether equal budgets are distinguished from proportionate risk/sensitivity allocation.

Whether downstream F8 output retains enough scope/dependency information to prevent the next receiver from repeating the collapse.

Whether a \#13 operational blast-radius refinement request is targeted to a relation whose result can materially change the decision, rather than becoming generic graph expansion.

Whether the Stage 1 interoperability campaign preserves source-native result semantics, scope, provenance, UNKNOWN qualifiers and the distinction between operational exposure and epistemic inheritance.

Number of distinct pathways versus number of materially independent evidence lineages.

Whether provider/transport diversity was incorrectly counted as independent corroboration.

Marginal decision value of an independent path versus another dependent path.

UNKNOWN lineage handling.

Whether pathway selection remained tied to the unresolved domain rather than a global channel rating.

&nbsp;

# 9\. Peer baseline, similarities and differences

Shared mechanisms

Orchestrator-workers; multi-agent debate/voting; evaluator-optimizer; retrieval; planning; HITL; policy/conformance; UQ; evidence fusion; provenance.

&nbsp;

EA does not claim these mechanisms as new.

&nbsp;

Key peer similarities

Agent frameworks already distribute work across specialized agents.

Multi-agent UQ research propagates uncertainty and can model upstream dependency.

HITL can add review/approval.

Policy/conformance and attestation systems produce scoped claims/verdicts.

&nbsp;

EA differential under test

The system-level object is not one confidence score or one consensus. It is a domain-indexed epistemic map with non-fungible local positions, explicit coupling/dependency, structural residual and targeted requalification. v0.2 adds a domain-indexed awareness-burden/sensitivity view so that total compute, total reviewers or total observations cannot substitute for sufficient awareness in the material domain.

&nbsp;

Peer reproduction question

Can the peer composition detect that its own individually sensible controls — including observation/resource effort — are applied to different epistemic domains and therefore do not compensate one another, without adding an equivalent scope-indexed meta-layer?

&nbsp;

APQ peer baseline. Permit the strongest reasonable peer composition to use source-lineage/correlation information and conventional source-selection criteria. If it detects the shared-lineage condition and makes the same scoped acquisition choice without an EA-equivalent scope/residual/composition layer, the differentiation claim is reduced.

&nbsp;

# 10\. Non-duplication with current FG-TIDA work

FG-TIDA Use Case \#4 addresses independently governed ecosystem defense, partial evidence, affected scope and local containment authority. It is the preferred Stage 1 external interoperability fixture for UC-EA-04. \#13 retains signal/incident lifecycle and operational blast-radius construction/refinement; EA consumes that state to perform decision-scoped epistemic composition and may request targeted refinement without reproducing \#13's operational graph mechanism.

Financial-services PR \#2 addresses runtime enforcement/conformance under collision; it can supply source-native local verdicts for composition tests. Those verdicts remain \#6 semantics and are not translated into EA or \#16 state names merely to fit the composition layer.

Theme \#18 addresses multi-objective agent choice/operator behavior. UC-EA-04 does not redefine the choice operator; it asks whether the epistemic state of the domains feeding/receiving those choices is compositionally valid.

Theme \#16 owns human oversight. Its output is one domain/input, not a global epistemic correction.

&nbsp;

# 11\. Maturity, IP and confidentiality

Validation maturity: Maintenance-frozen hypothetical architecture-validation profile. Not itself a public FG-TIDA Use Case.

Reference implementation: deterministic multi-agent fixtures remain recommended, exposing per-domain sensitivity/consequence and awareness-budget settings so asymmetric allocation can be tested independently of total compute volume. External Stage 1 testing should additionally pair EA with an independently governed \#13/non-EA implementation and preserve the operational-blast-radius / epistemic-dependency distinction.

Confidentiality/public boundary: Parent Case facts and a concise situational public use-case issue may be exposed. The General Law of Epistemic Composition, full branch set, peer baseline and internal validation machinery remain working material unless deliberately surfaced. This profile is not an FG-TIDA submission.

IP note: parent facts/challenges/ToR are source-derived; General Law of Epistemic Composition, domain-indexed EA mapping and stress-test design are internal working contributions.

&nbsp;

# Annex A — Case Study extensibility and publication boundary

This validation profile is deliberately suited to the Parent Case Study’s extensibility model.

Upward: more principals, service providers, agent layers and jurisdictions increase composition pressure.

Downward: a factory cell still has production, maintenance, safety/quality and worker/manager roles with non-universal authority.

Horizontal: hospital beds/staff, appointments, compute allocation, logistics and other constrained-capacity domains preserve the same composition problem where local roles and objectives differ.

A new Case Study is required if the domain cannot preserve meaningful principals, bounded authority relationships or identifiable decision/commitment points. For publication, the current mobility issue should link to these upward/downward/horizontal extension tests rather than claim that all extension domains are already part of the submitted situation.

&nbsp;

# Annex B — Terms of Reference context

Case anchors: 3.3 and 4.1.

Primary composition anchors: 2; 4.2; A.2.1; A.2.5; A.2.7.

Policy/domain integrity anchors: 4.4; A.1.5; A.2.5; supporting 4.2.

Assessment/indeterminacy anchors: 3.4; 4.3; 4.5; A.2.2; A.2.4; A.2.7.

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

[FG-TIDA Theme \#18 — Trustworthiness of multi-objective agentic AI](https://github.com/FG-TIDA/themes/issues/18)

&nbsp;