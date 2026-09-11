# UC-EA-02 — Architecture-Validation Profile — Bounded Determination under Incomplete, Conflicting or Partially Scoped Evidence — v0.6 — Maintenance Freeze

Derived from TIDA — Delegated Authority OS under Context Change

&nbsp;

# Status

Maintenance-frozen internal Ecosystem Awareness architecture-validation profile. Legacy identifier UC-EA-02 is retained for continuity, but this document is not an FG-TIDA use-case submission. It tests bounded evidence qualification, acquisition-pathway selection, interoperable epistemic handoff and external-signal composition against Parent Case facts and controlled validation variants. The Parent Case Study remains pre-freeze public working material. A future public FG-TIDA submission should be one concrete situational use case; this profile remains the deeper validation harness behind it.

&nbsp;

# 0\. Identification and traceability

Validation Profile ID: UC-EA-02 (legacy UC identifier retained for traceability).

Parent Case Study: TIDA — Delegated Authority OS under Context Change.

Public-submission boundary: the mobility scenario is the bounded concrete instantiation for the single public use-case record; UC-EA-02 remains an internal validation profile. The Parent Case's upward, downward and horizontal extensibility may be linked as bounded-reuse evidence, but those extensions do not silently add sectors or facts to the submitted mobility situation.

Primary Challenge: S5 — Operational indeterminacy & containment.

Secondary Challenges: S14 — Evidence-to-decision assessment; S6 — Interoperable, privacy-preserving trust determination.

Case-level ToR anchors: 3.3 Use cases; 4.1 Use cases and requirements analysis.

EA functions under test: F2 Decision-Relevant Window Qualification & Management; F3 Local Epistemic State Qualification; F4 External Epistemic Signal Qualification; F5 Scope-Indexed Epistemic Composition & Coupling Assessment; F6 Systemic Epistemic & Operating-Frame Assessment; F7 Requalification & Corrective Directive Generation; F8 Epistemic Statement & Envelope Generation; F9 Outcome Feedback & Revalidation.

Principal EA hypothesis: incomplete or uncertain evidence should not be forced into either certainty or endless search. The system must preserve what is determined, what is explicitly unresolved, what could justifiably be brought into the current window, and what remains structural residual.

&nbsp;

v0.2 extension hypothesis: the decision to acquire more evidence is itself risk- and capacity-bounded. Type 1 can appear as over-observation/resource depletion after marginal decision value has collapsed; Type 2 can appear as under-observation/hidden exposure when a narrow or stale W(d,t) is cheaper but insufficient for the mission's ecosystem sensitivity.

&nbsp;

v0.5 frozen reconciliation: when more evidence is potentially obtainable, the decision problem is not only how much additional observation to perform but which available acquisition pathway or combination of pathways is sufficiently qualified to reduce the material epistemic gap before its cost or latency removes the option to act. Pathway properties used for that selection must themselves remain epistemically qualified. This version also fixes the interoperability direction: EHD is the general handoff contract; the four-field determinacy envelope used in Theme \#13 is a specialized profile of that contract, not a competing universal schema. Interoperability is to be tested first against an external non-EA producer/consumer in the federated Stage 1 fixture before any new internal branch, function or interface family is introduced.

&nbsp;

# 1\. Functional interaction

Plain-language situation

At T2, the system must determine whether action A1 may proceed after Qcritical has been reported. One or more evidence elements relevant to authority, policy applicability, source freshness, scope, or context are incomplete, conflicting, stale, or only partially scoped. The system must decide whether the current evidence is sufficient, whether a bounded expansion of the observation window is justified, or whether the operative result must remain INDETERMINATE with an appropriate containment or escalation consequence.

&nbsp;

Actor

Citizen principal and personal agent; municipality/public principal and authorized role; evidence source E1; any supporting external source or verifier; relying party/action-admission function; retrieval/research or evidence service where used.

&nbsp;

Action

Action-time determination for A1 after the context change.

&nbsp;

Decision required

Is the available evidence sufficient to close the action-time determination, should the observation window be expanded, narrowed/stopped or redirected in a bounded way, or must the result remain INDETERMINATE? If additional evidence exists, is its expected decision value proportionate to its compute/latency/privacy/human-capacity burden and remaining response horizon?

&nbsp;

Problem encountered

Common architectures may attach a confidence value, call more retrieval, query another agent, or escalate to a human. These mechanisms can be valid but do not by themselves distinguish a legitimately resolvable out-of-window gap from structural residual, or determine when further search has become Type 1\.

&nbsp;

Current mitigation

Uncertainty scores; RAG/search; verifier/appraisal checks; conformance verdicts including INDETERMINATE; additional telemetry; human review.

&nbsp;

Residual gap being tested

Whether the architecture preserves scope and window qualification for each evidence item, prevents an external uncertainty statement from becoming local ecosystem truth, bounds context expansion, preserves structural residual, and emits a decision-usable epistemic envelope without forcing a universal uncertainty metric. v0.2 adds whether the architecture can avoid both wasting scarce awareness capacity and hiding exposure by choosing a window burden proportionate to mission sensitivity/risk.

&nbsp;

# 2\. Parent Case Study facts inherited unchanged

Case Study identity

TIDA — Delegated Authority OS under Context Change is a candidate shared Case Study that exposes authority, delegation, context, oversight, evidence and action-time decision interfaces. Annex I provides the minimal mobility instantiation; Annex II tests upward, downward and horizontal extensibility.

&nbsp;

Actors and authority

The restricted case distinguishes citizen principal, personal agent/instance, municipality/public principal, authorized municipal role, bounded municipal agent where used, G1, P1, decision D1, commitment C1, evidence source E1 and later intervention H1 where applicable.

&nbsp;

Operational sequence

T0 — Setup. G1 and P1 are current; P1 defines Qnormal/Qcritical and approved source E1. Visible evidence includes identities/role mandates, G1/P1 versions/validity, threshold definition, preference profile and source provenance.

&nbsp;

T1 — Commitment. The personal agent records D1 and C1 using current G1/P1, timing, price, capacity data, decision basis and commitment terms. C1 exists only where authority and hard limits were sufficiently established.

&nbsp;

T2 — Context change. E1 reports Qcritical crossed; P1 requires reassessment and temporarily disallows entry to the affected zone unless authorized H1 applies. The system must determine whether A1 may reroute/proceed, hold, escalate or remain INDETERMINATE.

&nbsp;

Evidence boundary

The parent Challenge framework explicitly anticipates incomplete, conflicting or stale authority facts, preferences and delegations. This validation profile does not invent indeterminacy as a new Case Study fact; it instantiates the already-declared Challenge S5 against the controlled T0–T2 structure.

&nbsp;

Governing regime

The legal regime for G1/P1 is not yet frozen in the source and remains TBD.

&nbsp;

# 3\. Epistemic handoff under test

Each local or external producer may provide only the qualifiers it actually knows. Missing qualifiers remain UNKNOWN.

&nbsp;

The minimum general interoperable handoff for this validation profile is the common six-element EHD kernel:

1\. producer-profile reference and version, or an inline-equivalent semantic/profile identifier when no separate profile artifact is used;

2\. subject/proposition/decision-domain together with the scope to which the statement applies;

3\. producer/issuer;

4\. operational result/closure;

5\. determination state;

6\. explicit unknown-qualifier declaration identifying material qualification that was not established.

&nbsp;

Additional fields remain conditional on decision relevance:

uncertainty statement and its semantics where available;

as-of/freshness;

window/observation-boundary descriptor where available;

window-selection basis where available, including sensitivity/consequence/capacity basis on the EA side where represented;

known exclusions;

candidate expansion paths where known;

structural residual statement where available;

provenance and upstream dependency;

direct versus inherited evidence;

capacity binding;

observation/determination burden where material to deciding whether more evidence is justified;

&nbsp;

&nbsp;

The producer need not expose prompts, chain-of-thought or a complete private context.

&nbsp;

Theme \#13 profile relation. The earlier four-field determinacy envelope remains valid as a \#13 specialization of EHD rather than a second universal contract: \`closure\` maps to the EHD operational result/closure kernel element; \`determinacy\_margin\` is a decision/scope-specific qualification field; \`capacity\_binding\` is a conditional capacity qualifier; and \`inherited\_indeterminacy\` is a dependency/residual qualifier. Provenance, freshness, scope and dependency context remain attached where materially required. This reading does not require changing Nelson's Use Case \#4 Requirement 20; it clarifies the profile/general-contract relation.

&nbsp;

Native-semantic preservation rule. A producer's native result vocabulary remains the producer's vocabulary. In particular, Theme \#6 verdicts such as PERMIT, REMEDIATE, BLOCK, ESCALATE or INDETERMINATE are not converted into EA or Theme \#16 states merely to fit the handoff. EHD carries the producer result with issuer, subject/scope, reference/profile semantics and explicit unknown qualifiers; EA separately determines what that result establishes or leaves unresolved for the receiving decision.

&nbsp;

External interoperability test rule. The first interoperability test should use at least one producer or consumer that does not share EA's internal F1–F9 logic, preferably within the two-independently-governed-organization Stage 1 fixture of FG-TIDA Use Case \#4. The test succeeds if both sides can produce/consume the agreed EHD/\#13-profile semantics without sharing their internal assessment algorithm. A failure is first an interface/test finding; the frozen architecture is reopened only if the failure demonstrates a necessary responsibility with no owner in F1–F9 or the existing interface taxonomy.

&nbsp;

# 4\. Challenge traceability

Challenge S5 — Operational indeterminacy & containment

The Challenge states that some indeterminacy is inevitable, especially when agents subdelegate or compose incomplete, conflicting or stale authority facts, preferences and delegations. The system must manage rather than silently convert it into permission; bound uncertainty; preserve evidence and links to canonical authority sources; contain propagation; and define hold, rollback or escalation paths before downstream effects leave control.

Primary ToR anchors: 3.4 Security assessment criteria and benchmarks; 4.3 Trust framework(s) and lifecycle management.

Supporting ToR anchors: A.2.2 trust lifecycle; A.2.7 trust control plane.

&nbsp;

Challenge S14 — Evidence-to-decision assessment

The Challenge asks whether each transition can state what must be demonstrated, what evidence is required, whether evidence is suffici