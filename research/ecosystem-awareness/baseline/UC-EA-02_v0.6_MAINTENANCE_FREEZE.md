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

The Challenge asks whether each transition can state what must be demonstrated, what evidence is required, whether evidence is sufficient/insufficient/inconclusive, and which decision it can support.

Primary ToR anchors: 3.4; 4.5; A.2.2; A.2.4.

&nbsp;

Challenge S6 — Interoperable, privacy-preserving trust determination

The Challenge asks whether independent personal agents, public systems, providers and relying parties can verify enough authority and status in real time without exposing full agendas, preferences or unnecessary personal data.

Primary ToR anchors: 3.4; 4.2 architectures for identity/trust/interoperability; 4.4 technical-policy and machine-readable trust metadata; A.2.5 trust interoperability across jurisdictions and sectors.

&nbsp;

# 5\. EA functional traceability

F2 decides what evidence/context belongs in W(d,t), records known exclusions and candidate bounded expansion paths, preserves D as structural residual, and stops/narrows/redirects awareness effort when marginal decision value is no longer proportionate to capacity cost.

F3 qualifies local closures and uncertainty: whether local determination is sufficient, open-ended, or falsely certain.

F4 qualifies external signals as attributed claims about a source and scope; it does not silently assign the source’s uncertainty to the receiver/system.

F5 composes the evidence by domain and dependency, preserving inherited uncertainty and source dependence.

F6 decides whether the current epistemic state is Sound/Type 1/Type 2/Mixed, separately records structural Type 0, and assesses what operating posture remains justified. v0.2 also records sensitivity/capacity mismatch rather than inventing a new failure type.

F7 directs the smallest justified action: specific source refresh, bounded retrieval, independent corroboration, stop-search, preserve INDETERMINATE, reduce scope, or invoke containment/oversight.

F8 produces a bounded epistemic statement/envelope sufficient for downstream consumers without exposing private reasoning.

F9 records outcome feedback and retains acquisition-pathway usefulness only as domain/decision/context/time-scoped evidence for later requalification. Prior pathway success may inform a new APQ assessment but does not become a portable global pathway trust or quality score.

&nbsp;

Primary failure surfaces

I0 determination capacity; I1 bounded determination effort; I2 epistemic honesty; O0 structural residual awareness; O1 bounded window expansion; O2 non-collapse of W into ecosystem; E0-I/E1-I/E2-I and E0-O/E1-O/E2-O for received evidence.

&nbsp;

# 6\. Requirements

R1. A received uncertainty/confidence value shall remain attributed to its source, proposition and disclosed scope/window.

R2. Unknown source scope/window shall remain UNKNOWN and shall not be silently treated as ecosystem scope.

R3. Missing qualifiers shall not automatically invalidate a signal, but shall remain explicit unknowns where material.

R4. The system shall distinguish in-window unresolved state from out-of-window potentially knowable state.

R5. The system shall preserve a structural residual and shall not imply that recursive context expansion can eliminate all out-of-window indeterminacy.

R6. Retrieval/window expansion shall have a bounded stopping condition that reflects mission sensitivity/consequence, marginal decision value, finite observation/human capacity and remaining response time.

R7. Where a justified additional source exists and can be obtained within the useful response window, F7 may request targeted expansion.

R8. Where further determination is not justified or cannot succeed within available capacity, the system shall not continue search merely to reduce discomfort with uncertainty. Type-1 awareness effort shall be measurable as resource/capacity consumption, not only as extra iterations.

R9. The system shall prevent missing evidence, unavailable humans, low confidence or unresolved dependencies from being converted into false PASS/FAIL/YES/NO certainty.

R10. Repeated claims derived from the same upstream source shall not be treated as independent corroboration unless independence is established.

R11. The system shall be able to emit a downstream statement that preserves determination state, scope, freshness, provenance/dependency and inherited indeterminacy at the abstraction level required for the decision.

R12. Privacy/minimum-disclosure constraints may leave qualifiers UNKNOWN; the consequence is bounded uncertainty, not forced disclosure.

R13. A cheap/narrow window shall not be treated as sufficient solely because it reduces observation cost when the mission remains materially sensitive to omitted ecosystem state.

R14. The test shall compare at least one fixed-broad, fixed-narrow and sensitivity/capacity-adaptive awareness policy under comparable facts/resources.

&nbsp;

R15. Acquisition-pathway qualification shall be decision-scope-specific. The system shall not convert a pathway’s suitability for one domain/decision/context into a global quality, trust or certification score.

&nbsp;

R16. Any pathway property materially relied upon for acquisition selection shall preserve the epistemic basis on which that property is known. A declared property shall remain distinguishable from observed, attested, independently evaluated, derived or UNKNOWN property state.

&nbsp;

R17. Absence of a producer-published pathway profile shall not be interpreted as either pathway failure or pathway trustworthiness. The system shall be able to qualify non-cooperative/passive pathways from available observed/attested/evaluated/derived evidence and explicit UNKNOWNs.

R18. When reused across time, historical usefulness of an acquisition pathway shall remain indexed to the relevant domain, decision/context and time conditions. Prior success may inform a later APQ qualification as evidence, but shall not be reused as a portable global trust, quality or certification score.

R19. EHD shall remain the general interoperability contract; any Theme-specific envelope, including the four-field Theme \#13 determinacy envelope, shall be represented as a profile or projection rather than silently becoming a second universal schema.

R20. Imported producer vocabularies shall preserve native semantics. No mapping from a producer's verdict/state into an EA or other Theme state is normative merely because such a mapping was useful in discussion.

R21. The interoperability claim shall not be considered established until at least one external cross-implementation campaign demonstrates that a source-native result from an independently governed non-EA producer or consumer can be exchanged through EHD and any applicable Theme profile while preserving material scope, provenance/lineage, UNKNOWN qualification and native semantics without requiring shared internal assessment logic.

FG-TIDA Use Case \#4 Stage 1 is the preferred current fixture for this validation, but it is not a normative dependency of the EA profile.

R22. Failure of that interoperability campaign shall not by itself create a fifth validation profile, new top-level function or new interface family; architecture change requires evidence that the missing responsibility has no current owner.

&nbsp;

# 7\. Test and stress-test branches

Branch A — Sufficient bounded evidence

E1 and all material G1/P1/applicability evidence are current and sufficiently scoped. Expected EA behavior: close the relevant determination without unnecessary search; residual D remains recognized but does not prevent Normal/appropriate operation.

&nbsp;

Branch B — Known resolvable gap

One material fact is not in W(d), but a known primary source can be retrieved within the useful response window. Expected EA behavior: classify it as potentially knowable C, request that source, and re-evaluate after retrieval.

&nbsp;

Branch C — Unknown source window

An external producer reports a confidence/uncertainty value but does not disclose the observation window or coverage. Expected EA behavior: preserve “source S reports x about proposition P” while setting source window/coverage to UNKNOWN; do not store it as ecosystem uncertainty.

&nbsp;

Branch D — Correlated evidence

Several agents repeat or transform a claim originating from the same upstream source. Expected EA behavior: preserve source dependence; do not count repetitions as independent corroboration merely because several agents emitted them.

&nbsp;

Branch E — Type 1 search

The system continues retrieval, debate, evaluator loops or human escalation after the useful response window or justified stopping rule has been reached. Expected EA behavior: classify Type 1 and stop/contain/requalify rather than continue unbounded determination.

&nbsp;

Branch F — Type 2 closure

An agent emits PASS/normal/low-uncertainty after dropping a material unresolved dependency or source-scope limitation. Expected EA behavior: detect closure laundering or false certainty at F3/F4/F5 and preserve the unresolved state.

&nbsp;

Branch G — Structural residual

No additional finite search can guarantee exhaustive knowledge of all ecosystem-relevant state, but the current mission can still proceed safely inside a qualified frame. Expected EA behavior: record Type 0 residual without forcing either search or migration.

&nbsp;

Branch H — Type 1 over-observation / resource depletion

A potentially knowable gap exists, but successive retrieval/critic/human-review steps stop changing the permitted determination while consuming compute, latency or human attention. Expected EA behavior: stop/narrow/redirect the search, preserve the residual and use bounded closure rather than epistemic perfectionism.

&nbsp;

Branch I — Type 2 under-observation / hidden exposure

A cheaper narrow/stale window omits a material dependency in a high-sensitivity domain and produces apparent closure. Expected EA behavior: identify the sensitivity/window mismatch, refresh or widen only the affected domain and prevent cost savings from being interpreted as low risk.

&nbsp;

Branch J — Risk-capacity adaptive comparison

Run the same frozen evidence fixture under low-sensitivity/reversible and high-sensitivity/irreversible decision profiles with comparable budgets. Expected EA behavior: justify different W(d,t) burdens while preserving the same A/B/C/D semantics and explicit residual.

&nbsp;

Branch K — Decision-relative acquisition-pathway discrimination

The same material evidence gap can be addressed through three available pathways.

Pathway A is low-cost, low-latency and fresh but exposes weak provenance and UNKNOWN source independence.

Pathway B is slower and more expensive but has stronger provenance, source-independence evidence and explicit uncertainty preservation.

Pathway C has the strongest assurance profile but cannot return before the current response window is expected to close.

Run at least two otherwise comparable decision profiles: one low-consequence/reversible and one high-sensitivity/high-consequence/poorly reversible. Expected EA behavior: F2.APQ does not rank A/B/C globally. It determines which pathway or combination is sufficient for the present evidence need; preserves unestablished pathway properties as UNKNOWN; may choose a cheaper path when the residual remains acceptable; may require B or another materially independent path when false closure would be consequential; and rejects acquisition whose latency makes the result operationally useless. F4 still qualifies the actual result received from the selected path.

&nbsp;

APQ-PARTIAL — Partial participation / non-cooperation stress profile

One or more relevant pathways publish no capability profile, expose only partial metadata, refuse active cooperation, or are available only as passive/public/environmental traces. Expected EA behavior: profile absence does not cause automatic rejection and does not create trust. APQ uses whatever observed, attested, independently evaluated or derived property evidence exists, leaves the rest UNKNOWN, and determines whether the resulting qualification remains sufficient for the specific decision.

&nbsp;

APQ-CONFLICT — Divergent/adverse incentives stress profile

A pathway operator has an incentive to overstate coverage, freshness, independence or assurance. The declared profile remains internally well-formed. Expected EA behavior: declared properties remain source-attributed declarations; stronger reliance requires the evidence basis appropriate to the decision. The system does not infer aligned objectives or cooperative intent merely from protocol participation.

Pathway-class instantiation. At least one Branch K execution shall instantiate an O5 tool/API/resource as an acquisition pathway, and at least one execution shall instantiate an S6 human report/review channel as an acquisition pathway. The test shall record the pathway state actually available from the owning interface, any mediation through O2/O4/F1, the material UNKNOWNs, and whether F2.APQ can qualify that path without requiring a new interface family or transferring ownership of the tool or human decision into EA.

Outcome-feedback / repeated-run step. After the selected pathway produces an observable downstream outcome, F9 records whether that pathway was useful, stale, redundant, costly or independently informative for the stated domain/decision/context and time profile. Re-run an otherwise comparable decision in which that history is available. F2.APQ may use the historical record as one input to the new qualification, but it must re-check current scope, provenance, freshness, dependence, property basis and response conditions. The test fails if previous success is promoted into a global pathway reputation or substitutes for current qualification.

&nbsp;

External interoperability campaign — deliberately not a new internal Branch L. Run the handoff across two independently governed implementations. One side shall produce a native result under its own logic and expose only the agreed EHD plus the \#13 profile fields that are material; the other side shall consume it and reach a decision-scoped qualification without access to the producer's internal logic. Repeat in the reverse direction where practical. Record semantic-loss, UNKNOWN preservation, scope/provenance retention and whether either implementation required an undocumented shared assumption. This campaign validates the interface before any corpus reopening.

&nbsp;

# 8\. Assessment criteria

Success criteria

Source-local uncertainty remains source-local unless requalified.

A bounded, resolvable gap triggers targeted retrieval rather than generic context expansion.

Repeated/correlated claims do not become false independence.

Unbounded search is detected and stopped.

False closure is detected when uncertainty/scope/dependency is lost.

Structural residual can coexist with Normal operation.

Downstream consumers receive sufficient epistemic qualification without a shared universal uncertainty algorithm.

A non-EA implementation can produce or consume the EHD/\#13 profile without adopting F1–F9 or EA's internal epistemic calculus.

Theme-specific result vocabularies remain distinguishable across the handoff; interoperability does not require semantic collapse.

&nbsp;

Measurable evidence

Presence of explicit source/proposition/scope/freshness fields or UNKNOWN markers.

Number of unnecessary retrieval/escalation iterations prevented.

Compute/tokens, tool/retrieval calls, latency, bandwidth/privacy burden and human-attention time spent on awareness.

Marginal decision changes attributable to each additional evidence acquisition step.

Missed material changes / stale-frame false closures under narrow-window configurations.

Remaining response capacity/time after determination effort.

Whether independent corroboration count excludes known duplicate lineage.

Whether the system preserves INDETERMINATE instead of forcing a binary closure.

Whether structural residual remains represented after a successful local determination.

Whether F8 output is sufficient for a downstream relying party to distinguish local determination from ecosystem completeness.

Whether the external interoperability campaign preserves the six EHD kernel elements and any material \#13 profile qualifiers without undocumented translation.

Whether the consumer can interpret the producer's native result without treating an optional qualifier as a mandatory universal field.

Selected pathway(s) and decision-relative qualification basis.

Pathway property value plus epistemic basis where relied upon.

Profile availability versus actual usable property evidence.

Acquisition cost/latency/privacy burden by pathway.

Marginal decision change attributable to each pathway.

Whether a late but strongly assured pathway closed after the useful response window.

Whether a cheaper path was accepted only when its residual was explicitly tolerable.

Whether any global pathway score was created or reused improperly.

Whether prior pathway history was used in the repeated run.

Whether its original domain/decision/context/time scope remained attached.

Whether current qualification overrode historical success when material conditions changed.

Whether historical success substituted for current qualification.

&nbsp;

# 9\. Peer baseline, similarities and differences

Shared mechanisms

Uncertainty quantification; RAG/search; debate/critics; verifier/appraisal; provenance; confidence signalling; conformance INDETERMINATE; HITL.

&nbsp;

EA does not claim uncertainty communication or propagation as new.

&nbsp;

Closest overlaps

DebUnc-like uncertainty communication can change downstream reasoning.

PropUQ-MAS-like approaches can propagate local and inherited uncertainty through multi-agent graphs.

RATS separates evidence, verifier appraisal and relying-party decision.

Theme \#6 provides conformance verdicts and explicit INDETERMINATE with scope.

&nbsp;

Additional EA behavior under test

Window qualification and sensitivity/capacity selection basis; distinction between B/C/D; structural residual; bounded expansion and bounded narrowing/stopping; generic external epistemic-signal qualification; non-collapse of unknown scope; domain-indexed composition; no required common probability model; and a tested risk/resource frontier rather than a default preference for more observation.

&nbsp;

Peer reproduction question

Can a peer composition reproduce these behaviors without adding explicit window/residual/domain semantics equivalent to EA? If yes, record the overlap and reduce the novelty claim.

&nbsp;

APQ peer baseline. Include a strong conventional source selector/router allowed to use cost, latency, service/QoS metadata, trust/reputation and source-lineage/correlation evidence where available. The test asks whether the peer can reproduce the same scoped pathway choice and non-collapse behavior without an EA-equivalent scope/residual/composition layer. Do not cripple the peer selector to make EA win.

&nbsp;

# 10\. Non-duplication with current FG-TIDA use cases

FG-TIDA Use Case \#4 already provides the preferred external-signal/defense and Stage 1 interoperability fixture, with issuer, freshness, observed scope, residual uncertainty, affected-scope representation and local authority. UC-EA-02 does not duplicate that workflow. It should consume the Stage 1 mechanism as an external validation surface for F4/F5/F8 and APQ. Requirement 20 of Use Case \#4 remains valid as the \#13 determinacy-envelope profile; EHD is the more general handoff contract around which that profile sits.

&nbsp;

Financial-services PR \#2 and Theme \#6 cover runtime conformance and verifier/appraisal semantics. UC-EA-02 treats their verdicts and appraisal outcomes as source-native inputs to epistemic qualification; it does not redefine or translate the native \#6 verdict vocabulary into EA/\#16 states.

&nbsp;

# 11\. Maturity, IP and confidentiality

Validation maturity: Maintenance-frozen hypothetical architecture-validation profile. Not itself a public FG-TIDA Use Case.

Reference implementation: deterministic internal fixtures remain recommended for bounded-evidence/APQ behavior; the interoperability claim additionally requires an external Stage 1 fixture with at least one independently governed non-EA implementation. That external test precedes any architectural expansion.

Confidentiality/public boundary: Parent Case facts and an eventual situational use-case issue may be public. The full branch set, peer baseline, APQ stress apparatus and architecture-validation logic remain internal working material unless deliberately surfaced. This profile is not an FG-TIDA submission.

IP note: parent facts/challenges/ToR mapping are source-derived; EA requirements, handoff semantics and test mappings are internal working contributions.

&nbsp;

# Annex A — Case Study extensibility and publication boundary

Upward extension adds actors, roles, services, objective layers and jurisdictions.

Downward extension reduces to a private factory or production cell.

Horizontal extension changes domain while preserving principal/role/agent/authority/preference/policy/grant/commitment/decision semantics.

The validation profile is intentionally about evidence and determination semantics, so it should survive all three extension directions if those invariants survive. For public filing, however, mobility remains the concrete situation; upward/downward/horizontal extensions are linked as bounded-reuse evidence rather than treated as additional sectors or facts of the same use-case submission.

&nbsp;

# Annex B — Terms of Reference context

Case-level anchors: 3.3 and 4.1.

Primary UC anchors: 3.4 and 4.3.

Supporting architecture/interoperability anchors: 4.2, 4.4, 4.5, A.2.2, A.2.4, A.2.5 and A.2.7 as mapped by Annex IV.

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

[FG-TIDA Theme \#6 — Intent-based Security Policies](https://github.com/FG-TIDA/themes/issues/6)

&nbsp;