EA-ITP-01 — EHD / Theme \#13 Cross-Implementation Interoperability Test — v0.1

&nbsp;

STATUS

Frozen test specification supporting the Ecosystem Awareness validation profiles. Internal working artifact; not an FG-TIDA or ITU-T deliverable. It defines an executable interoperability test and does not create a fifth UC-EA profile, F10, O7 or a new interface family.

&nbsp;

1\. PURPOSE

&nbsp;

Test the property identified by Theme \#13 and Nelson Use Case \#4: independently implemented mechanisms must be able to exchange decision-relevant epistemic state through the general Epistemic Handoff Descriptor (EHD), including the Theme \#13 determinacy-envelope profile where applicable, without requiring shared internal assessment logic.

&nbsp;

This test operationalizes requirements already present in UC-EA-02 and UC-EA-04. It does not reopen those profiles.

&nbsp;

2\. EXTERNAL FIXTURE

&nbsp;

Preferred external fixture: FG-TIDA Use Case \#4 Stage 1 — federated cross-theme minimum across independently governed organizations.

&nbsp;

Producer A and Consumer B must be independently implemented. At least one side must not implement, expose or share EA F1–F9 internal logic. The reciprocal direction must also be tested so EA is both consumer and producer across different runs.

&nbsp;

3\. CONTRACT UNDER TEST

&nbsp;

General contract: EHD six-element interoperability kernel:

1\. producer-profile reference/version or inline-equivalent semantic identifier;

2\. subject/proposition/decision-domain plus scope;

3\. producer/issuer;

4\. operational result/closure;

5\. determination/state kind;

6\. explicit unknown-qualifier declaration for material qualification not established.

&nbsp;

Conditional qualifiers remain decision-relative, including freshness/as-of, observed-versus-derived status, evidence class, uncertainty semantics, capacity, provenance, dependency/coupling, source lineage and window-selection information.

&nbsp;

Theme \#13 profile: where the \#13 interface uses the earlier determinacy envelope, \`closure\` maps to the EHD operational-result element; \`determinacy\_margin\`, \`capacity\_binding\` and \`inherited\_indeterminacy\` remain profile qualifiers. This is a specialization of EHD, not a competing universal contract. Nelson Use Case \#4 Requirement 20 therefore remains usable without redefining the general kernel.

&nbsp;

4\. NATIVE-SEMANTICS RULE

&nbsp;

A source-native producer keeps its own vocabulary. For example, a Theme \#6 verdict remains a \#6 verdict with its issuer, scope and reference semantics. The adapter/handoff must not translate it into an EA, \#13 or \#16 state merely to make the interface appear uniform.

&nbsp;

Extra producer fields are permitted. A producer may emit a richer local vocabulary or more qualifiers than the kernel. The receiver must neither ignore a material additional qualifier merely because it is not in the kernel nor over-read an unfamiliar field as if it had EA semantics. Unrecognized but potentially material information must remain source-attributed and unresolved until its semantics are established.

&nbsp;

5\. TEST DIRECTIONS

&nbsp;

Direction A — external producer → EA consumer.

An independently governed non-EA producer emits a source-native result plus EHD/\#13-profile metadata. EA must consume it without access to the producer’s internal reasoning and preserve scope, issuer, qualification and unknowns.

&nbsp;

Direction B — EA producer → external consumer/\#13 lifecycle.

EA emits a bounded handoff or \#13 profile. The receiving lifecycle must be able to use the result without access to F1–F9 internals and without treating the EA assessment as containment authority.

&nbsp;

Direction C — richer-than-kernel producer → EA consumer.

The external producer emits all six kernel elements plus one or more additional native/material qualifiers. EA must preserve and correctly bound the additional information, neither discarding it when material nor assigning semantics not established by the producer/profile.

&nbsp;

Direction D — partial producer → consumer.

One or more conditional qualifiers are unavailable and explicitly UNKNOWN. The receiver must remain interoperable without fabricating defaults or converting partial qualification into binary certainty.

&nbsp;

6\. MINIMUM FIXTURES

&nbsp;

ITP-A — clean interoperable handoff: all required kernel elements present, material conditionals known.

ITP-B — explicit UNKNOWN: one decision-material conditional qualifier unavailable.

ITP-C — source-native verdict: producer uses a native state vocabulary not shared by EA.

ITP-D — shared-lineage condition: nominally distinct paths carry material claims derived from one upstream source.

ITP-E — \#13 determinacy-envelope profile: four profile fields carried with relevant provenance/scope/dependency context.

ITP-F — richer-than-kernel handoff: producer emits an additional material field not present in the base kernel.

ITP-G — unfamiliar optional field: extra field is non-material or its semantics are unavailable; receiver must not infer meaning.

ITP-H — reciprocal EA output: external consumer receives an EA handoff and acts only within its own authority.

&nbsp;

7\. PASS CRITERIA

&nbsp;

The test passes only if:

\- scope survives end to end;

\- producer/issuer and profile/reference semantics survive;

\- source-native operational result remains source-native;

\- material UNKNOWN state remains explicit;

\- dependency/source lineage survives where supplied and material;

\- the receiver can distinguish local result from broader system-level qualification;

\- neither side requires the other side’s private reasoning/internal algorithm to interpret the contract;

\- \#13 containment authority is not created by receiving an EA assessment;

\- richer producer output is preserved when material without becoming an implicit extension of the universal EHD kernel;

\- non-material or semantically unknown extra fields do not acquire invented meaning;

\- a partial producer can interoperate without silent defaulting;

\- reciprocal handoff works in both directions.

&nbsp;

8\. FAILURE CRITERIA

&nbsp;

Fail if any execution exhibits one or more of the following:

F1 Scope loss — a bounded claim is consumed as broader than supplied.

F2 Issuer/profile loss — the receiver cannot identify who produced the result or under which semantics/version.

F3 UNKNOWN promotion — missing/unresolved qualification is silently converted into certainty, permission or a default state.

F4 Semantic laundering — a source-native state is translated into an EA/\#13/\#16 state without an explicit, validated mapping.

F5 Lineage loss — repeated/shared upstream evidence is treated as independent corroboration after handoff.

F6 Hidden implementation coupling — consumer requires producer internal reasoning or producer requires consumer internal algorithm for ordinary interpretation.

F7 Authority leakage — an EA assessment is treated as containment, authorization or enforcement authority.

F8 Material-extra-field loss — producer emits a richer material qualifier beyond the kernel and the receiver drops it in a way that can change the relying decision.

F9 Extra-field over-reading — receiver assigns unstated EA/systemic meaning to a producer-specific field or treats its mere presence as stronger qualification.

F10 Kernel inflation by accident — a successful richer profile is misread as proving that its extra field must become mandatory in every EHD.

F11 Partial-handoff defaulting — absence of a conditional qualifier prevents honest interoperability only because the receiver requires fabricated completeness.

F12 Asymmetric interoperability — one direction works only because the other implementation adopts the first implementation’s internal logic.

&nbsp;

9\. EVIDENCE TO RECORD

&nbsp;

For every run record: producer implementation/version; consumer implementation/version; profile/semantic reference; exact fields emitted; UNKNOWNs; additional native fields; scope; issuer; provenance/lineage where material; output consumed; decision/posture effect; any adapter used; whether either side required internal-logic knowledge; and pass/fail against F1–F12.

&nbsp;

10\. FREEZE / REOPEN RULE

&nbsp;

This test specification is frozen as the first interoperability test definition. A failed run does not automatically justify changing F1–F9, O1–O6, S1–S13 or the EHD kernel. First determine whether the failure is a profile/adapter/semantic-mapping defect. Reopen the architecture only if a necessary responsibility required by the validated test has no existing owner or the general contract cannot express a decision-material distinction without semantic loss.

&nbsp;

TRACEABILITY

\- UC-EA-02 — EHD, source-native semantics, APQ and bounded evidence.

\- UC-EA-04 — composition, source lineage, cross-implementation requirement R18.

\- Theme \#13 — incident-signal lifecycle and operational blast radius.

\- FG-TIDA Use Case \#4 — Requirements 19–24 and Stage 1 federated minimum.

&nbsp;