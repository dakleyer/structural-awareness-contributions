Ecosystem Awareness — Provisional Cross-Theme Interface Contracts — v0.4

&nbsp;

Status

&nbsp;

Private working specification for collaborative discussion. This document does not claim FG-TIDA adoption, does not prescribe internal implementations for neighbouring Themes, and does not require any Theme to adopt the Ecosystem Awareness internal theory. It defines provisional producer/consumer contracts that can be tested against frozen architecture-validation profiles and revised collaboratively.

&nbsp;

Purpose

&nbsp;

Ecosystem Awareness (EA) is treated here as a transversal component that consumes qualified outputs from existing trust, security, oversight, evaluation and incident functions; composes those outputs by material decision domain; assesses whether the current system-level determination and operating frame remain sufficiently supported; and returns bounded requalification information without taking ownership of the producing Theme’s function.

&nbsp;

The contract question is bilateral:

&nbsp;

Theme → EA: what decision-relevant state must remain legible at the boundary?

EA → Theme: what systemic qualification can EA return that the Theme can use without surrendering its own authority or internal decision logic?

&nbsp;

The contracts are provisional. Their immediate purpose is to make Validation Profiles UC-EA-01…04 executable without inventing missing state. The interfaces should be changed only when a Use Case or implementation test exposes a concrete insufficiency.

&nbsp;

v0.4 preserves every v0.3 bilateral contract and the risk/sensitivity-capacity rule, and adds the validation-gated acquisition-pathway distinction required by F2.APQ. APQ does not create another Theme contract: it uses existing discovery/context/telemetry/transport/signal/privacy/trust-framework state and, where available, an optional signalling-mechanism profile. Neighbouring Themes are not asked to adopt EA’s path-selection logic or to accept EA as a mechanism certifier.

&nbsp;

Contract anatomy

Theme capability/result → bounded Theme→EA handoff → EA qualification/composition → scoped EA return → Theme/consumer action under its own authority.

Optional pathway profile → F2.APQ → decision-relative sufficiency; never global mechanism certification.

Cross-layer namespace: `IF-S#` denotes Functional Interface S#; `CH-S#` denotes DAOS Challenge S#. Native source identifiers are unchanged.

&nbsp;

1. Common contract rules

&nbsp;

1.1 Qualified assertion, not exhaustive disclosure

&nbsp;

EA does not ask producers to expose internal reasoning, prompts, complete context, complete memory or a universal uncertainty score. A producer emits a qualified assertion: what it concluded, the scope and evidence boundary supporting that conclusion, and which material qualifiers it did not establish.

&nbsp;

1.2 Partial by construction

&nbsp;

A contract is conforming when the producer declares honestly what it can and cannot establish. A missing qualifier is UNKNOWN; completeness is not required. Where the reason is known, it should preferably be supplied (for example not-observed, not-tracked, unavailable, privacy-restricted, unsupported or not-established), because requalification may differ by reason; the reason itself may remain UNKNOWN. `not-applicable` is kept separate because it is a determination, not an unknown state.

&nbsp;

1.3 Stable profile + decision-relevant handoff

&nbsp;

The EHD/interface contract is intended as a lightweight metadata overlay on the Theme’s existing result, not a second full payload and not a request to transmit the producer’s internal history. The semantic contract may be split into:

&nbsp;

A. Producer Epistemic Profile — a stable, versioned description of the producer’s normal coverage model, claim semantics, available qualifier fields, uncertainty/evidence vocabulary, observed-vs-derived policy, provenance/source-relationship semantics and default validity/revalidation rules where meaningful.

&nbsp;

B. Decision-Relevant Handoff — a small per-result/per-interaction delta that binds the operational result to the current action/interaction and carries only information that varies or overrides the profile.

&nbsp;

The handoff may reference the profile by identifier and version; cryptographic binding may be used where the trust model requires it, but is not a universal EA requirement.

&nbsp;

1.4 Decision-scope projection

&nbsp;

EA and downstream consumers need only carry the domains material to the receiving decision, not an ever-growing history of every upstream domain. Projection is valid only if it preserves material coupling, known exclusions and unresolved coupling as UNKNOWN. Projected-out state must not silently become independent or irrelevant.

&nbsp;

1.5 Conditional fields

&nbsp;

A field is mandatory only where its absence can change the relying decision or make the producer’s claim materially ambiguous. Temporal freshness, for example, is required for time-dependent claims where staleness can change reliance; it is not collected merely because the field exists.

&nbsp;

1.6 EA obeys the same discipline

&nbsp;

Every EA output declares its own assessed scope/coverage, known exclusions, unknown qualifiers and residual limitations. EA must not demand epistemic limits from others while presenting its own output as global truth.

&nbsp;

1.7 Ownership boundary

&nbsp;

A Theme keeps ownership of its own semantics and operational decision. EA does not originate authority, perform remote attestation, decide conformance, run human oversight, compute population statistics, operate incident containment or enforce actions. It qualifies and composes their outputs.

&nbsp;

EA also does not rank, score, certify or approve acquisition or signalling mechanisms as globally better or worse. It may determine that an available pathway is sufficient, insufficient or unresolved for a particular receiving decision, scope and operating condition. That decision-relative qualification is not a portable certification of the mechanism.

&nbsp;

1.8 Acquisition pathway profile versus qualification

Where EA must choose among ways of obtaining material evidence, the description of a pathway and EA’s qualification of that pathway remain separate objects. A Pathway Capability Profile, when one exists, is source-attributed evidence about the mechanism. EA Pathway Qualification is the consumer-side assessment of whether the available path is sufficient for the present decision. Any relied-upon pathway property retains its epistemic basis where material; declared, observed, attested, independently evaluated, derived and UNKNOWN are candidate basis classes, not mandatory wire literals.

&nbsp;

An explicit pathway profile is optional. The same qualification can operate over passive observation, public/regulatory evidence, environmental/action traces or other non-cooperative sources using whatever property evidence is actually available. Lack of a profile is neither proof of insufficiency nor proof of trustworthiness.

&nbsp;

Where the acquisition path is itself a tool/API/resource or a human reporting/review channel, the relevant pathway state may come through existing O5 or S6 interfaces, directly or through an explicitly identified O2/O4/F1 mediation; APQ does not create a new Theme contract for that reason.

&nbsp;

2. Common Theme → EA kernel

&nbsp;

Interoperability minimum. Every Theme→EA handoff intended to compose across independently implemented components should preserve the same six-element EHD kernel, even when some values are explicitly `UNKNOWN`: (1) producer-profile/semantic reference and version, or an inline-equivalent identifier; (2) subject/proposition/decision-domain plus scope; (3) producer/issuer; (4) operational result/closure; (5) determination/state kind; and (6) explicit unknown qualifiers. This is the irreducible parseability contract, not a requirement for complete qualification.

&nbsp;

Beyond that kernel, contract-level fields may include:

&nbsp;

- result / claim: what the producer concluded or emitted;
- scope / coverage: the decision domain, action, population, component, geography, time horizon or other boundary to which the claim applies, including known exclusions where material;
- source / provenance: who produced the claim and the relevant provenance/source relationship;
- evidence class: observed/measured versus derived/inferred/aggregated where material;
- temporal validity: as-of, freshness, validity or revalidation condition where time affects reliance;
- unknown qualifiers: material qualifiers the producer did not establish.

&nbsp;

Conditional qualifiers when material to composition:

&nbsp;

Mission-side risk/capacity note. Ecosystem sensitivity/exposure, consequence severity, reversibility, tolerated residual and awareness budget are generally EA/O1/F1 context, not universal Theme→EA fields. A Theme carries them only when it actually owns or observes a relevant part of that state.

&nbsp;

- dependency / correlation / source-independence information;
- human/compute/evidence/authority/time capacity binding;
- uncertainty/confidence/evidence-sufficiency semantics;
- inherited upstream indeterminacy;
- interaction/action binding for ephemeral agents or action-specific claims.

&nbsp;

3. Common EA → Theme kernel

&nbsp;

EA returns four main semantic objects, normally projected to the consumer’s decision scope:

&nbsp;

A. Scope-indexed epistemic assessment

What remains sufficiently determined, unresolved or structurally limited in the domains material to the receiving decision. EA does not require or emit one universal scalar trust score.

&nbsp;

B. Epistemic management condition and structural markers

Management status (for example Sound / Type 1 / Type 2 / Mixed) is kept distinct from structural Type-0 conditions/residual markers.

&nbsp;

C. Operating posture

Normal / Containment-Mitigation / Migration-Regime Transition, or implementation-equivalent categories. Posture is indexed to the receiving decision scope, `Posture(D_receiver)`: different consumers may legitimately receive different postures when their material domains differ, and a global posture must not be inferred unless the assessed scope supports one. Posture summarizes the qualified operational frame; it does not itself execute enforcement. Where useful, it may carry a small conditional posture qualifier derived from already available state: response-capacity sufficiency (sufficient / binding / unavailable / unknown), response-window state (open / at-risk / expired / unknown), frame recoverability (established / not-established / unknown), and for Migration/Regime Transition only, transition readiness (ready / partial / unavailable / unknown). These qualifiers are deliberately not a second universal subposture taxonomy and do not prescribe the downstream action.

&nbsp;

D. Requalification requirement

The domain, dependency, source, authority, evidence class, human capacity, reference or observation frame that must be refreshed, widened, narrowed, independently corroborated or otherwise requalified.

&nbsp;

Every EA output carries EA’s own scope/coverage/unknown/residual qualification.

&nbsp;

4. Provisional contract — Theme #13 Ecosystem-level Agent Defense / Incident Signal Exchange

&nbsp;

Interface role

Theme #13 owns incident-signal lifecycle, corroboration, affected-scope/blast-radius representation and containment/resolution semantics. EA consumes those outputs as one ecosystem evidence source and assesses what they justify when composed with other decision-relevant states.

&nbsp;

#13 → EA

&nbsp;

Stable profile may declare:
- signal type/taxonomy and lifecycle semantics;
- normal observed-versus-derived classification;
- provenance/reporter relationship vocabulary;
- blast-radius/dependency representation semantics;
- containment-response vocabulary and normal validity rules.

&nbsp;

Where #13 exposes stable properties of the signalling mechanism itself, those properties may be referenced through an optional Signalling Capability Profile. EA treats that profile as source-attributed evidence and qualifies only the properties material to the receiving decision. #13 is not required to publish such a profile as a condition of interoperability; absent or non-cooperative acquisition routes may still be qualified from observed, attested, independently evaluated, derived or UNKNOWN state.

&nbsp;

Per handoff where material:
- observed condition / derived determination;
- issuer/reporter and provenance;
- scope and freshness/as-of;
- evidence/confidence semantics;
- affected and potentially affected scope;
- corroboration/amendment history;
- source-dependence/correlation information where known;
- response/containment reach and response window;
- unresolved/unknown qualifiers;
- resolution/correction state.

&nbsp;

What EA does with it

EA qualifies the incident signal as a scoped external epistemic claim; checks whether corroborating signals are genuinely independent or merely share lineage; composes affected-domain state with authority, conformance, oversight, attestation and other evidence; determines whether residual indeterminacy remains material; and assesses whether the current operating frame remains sufficiently supported. Against the O1/F1 sensitivity-capacity profile, it also asks whether additional corroboration/observation is likely to change the decision before the response window closes, or whether further evidence collection would mainly consume capacity.

&nbsp;

If several signalling/acquisition routes are available, EA may use F2.APQ to determine whether the current route is sufficient for the specific incident/evidence need and whether another materially independent route has greater marginal epistemic value before the response window closes. This is not a global ranking of #13’s mechanism.

&nbsp;

EA 