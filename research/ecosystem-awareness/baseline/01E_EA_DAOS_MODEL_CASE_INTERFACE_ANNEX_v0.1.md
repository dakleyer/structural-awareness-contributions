# Annex 01E — Ecosystem Awareness / Model Case Study interface: Delegated Authority OS under Context Change

**Status:** candidate EA corpus interface annex, v0.1, 15 September 2026. The parent case and its Annexes remain unchanged. This annex is a source-grounded architectural/test contract, not a renamed or frozen parent case, an implemented runtime API, four submitted FG-TIDA Use Cases, a completed pilot, or an ITU-T adoption.

## 1. Placement and exact source identity

The public parent is [TIDA — Delegated Authority OS under Context Change](../../../submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/README.md). “DAO/DAOS” here means **Delegated Authority OS**, not a decentralized autonomous organization. “Model Case Study” is an editorial description of its bounded extensibility, **not** a change to the parent's public title. [Annex I](../../../submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/02_ANNEX_I_Minimal_Operational_Case.md) supplies the smallest mobility instantiation; [Annex II](../../../submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/03_ANNEX_II_Case_Extensibility.md) states upward, downward and horizontal extension limits; [Annex III](../../../submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/04_ANNEX_III_Challenges_Exposed_by_the_Case.md) exposes solution challenges CH-S1…14; [Annex IV](../../../submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/05_ANNEX_IV_FG-TIDA_ToR_Mapping_and_Traceability.md) maps those challenges to FG-TIDA ToR. The [EA use-case masterclass](./DAOS_EA_USE_CASES_MASTERCLASS_v0.1.md) gives the detailed case walkthrough and test vectors. This annex identifies the **interface** between that source fixture and the [integrated EA foundation](./01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md), [F1–F9 architecture](./03_FUNCTIONAL_ARCHITECTURE_v0.4.part01.md) and [general interfaces](./04_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.4.part01.md).

The parent case is a **test fixture and architectural neighbour**, not an EA subsystem. Case facts are frozen for a given comparison; a new domain or changed governing regime is a versioned variant, not a silently enlarged mobility claim. The four UC-EA documents are architecture-validation profiles of one T0–T2 scene, not four unrelated situations or four external FG-TIDA submissions.

## 2. Case-to-EA boundary: concrete inputs

| Parent fact/state retained for one case version | EA consumer | Required qualification; never silently infer |
|---|---|---|
| T0 G1: citizen principal grant to personal agent; hard limits, tradeable preferences, scope, standing and validity | F1, F4, F5 | Preference is not permission; agent/instance/representation and retained authority remain distinguishable. EA consumes qualified standing, not a self-issued grant. |
| T0 P1: authorized public role's policy/mandate, Qnormal/Qcritical, origin/version and E1 source | F1, F4, F5, F6 | Public applicability is source-owned. A policy objective is not a private grant; another domain's authority cannot compensate a missing G1/P1 condition. |
| T1 D1 decision and C1 binding commitment | F1, F5, F6, F9 | Historical T1 validity is evidence, **not** a reusable T2 execution permit. Decision, negotiation, reservation, commitment and action remain distinct states. |
| T2 E1 observation reporting Qcritical crossed; event time, source, threshold, coverage and relevance | F2, F4, F5, F6 | An alert can challenge the normal frame but does not certify every dependency, establish a new grant, or itself choose an operating posture. UNKNOWN, stale and incompatible source state remain reportable. |
| T2 candidate A1 and, where applicable, separately authorized exceptional H1 | F1, F5, F6, F7, F9 | Feasibility, permission, human availability, actual intervention and observed effect are separate. H1 must not overwrite G1/P1 provenance or cure contrary evidence by mere approval. |
| Decision horizon, consequence/reversibility, feasible observation/response, reviewer capacity and governing regime | F1, F2, F6, F7 | The selected W(d,t) and determination effort must fit the useful response window. Human attention and disclosure burden are finite; no cross-jurisdiction authority answer is inherited from the common skeleton. |
| Annex III CH-S1…14 and Annex IV ToR mapping | Validation-design consumer, not runtime F10 | Challenge IDs select test seams and ownership boundaries. CH-S3 is **not** functional interface S3; D1–D3 pre-freeze design conditions are not CH-S1…14. |

A source-independent or correlated E1 report, a nominal reviewer, a stale grant and a resource delay are **test variations with named provenance**, not license to mutate the base case to make EA pass. The parent/test owner supplies facts; EA qualifies their scope, freshness, dependencies and residual for a declared decision.

## 3. EA-to-case/test boundary: bounded outputs

| EA output | Receiver/use in the model case | Ownership limit |
|---|---|---|
| F1 mission/decision record: affected domains, consequence, reversibility, residual tolerance and useful deadline | Case-version test harness; authorized decision owner | EA cannot redefine principal preference, public policy or legitimate objective. |
| F2 W(d,t): selected observation boundary, acquisition-pathway basis, freshness, source lineage, stop/expansion criterion and remaining capacity | Evidence acquisition/telemetry owners; test record | More observations or pathways are not automatically more independent knowledge. |
| F3/F4/F5: local/external qualified claims, E(d,t), inherited uncertainty, coupling and source dependence | Case comparison record; producing functions | A valid result in one domain is not fungible with a fault in another; original producer semantics remain source-owned. |
| F6: whether the T1 operating frame still sufficiently supports T2 A1; epistemic status and Normal/Containment/Migration-preparation posture | Legitimate owner and authorized downstream controllers | Posture is assessment, not a new permit or an automatic universal shutdown. |
| F7: affected assumption, smallest targeted requalification request and bounded alternative/hold condition | Relevant grant/policy, evidence, oversight or response owner | EA requests; those owners verify, decide and execute under their own mandates. |
| F8 Epistemic Handoff Descriptor and F9 outcome-to-assumption discrepancy | Inter-agent/Theme consumer and subsequent test replay | A receipt is not measured outcome; UNKNOWN and structural residual remain visible rather than becoming clean binary closure. |

The candidate handoff joins **the same** case ID, operation/decision, source version, domain, T0/T1/T2 event time and useful horizon. A missing source-native field returns UNKNOWN or requests targeted clarification; it is not fabricated into an EA-wide universal schema. EA's general [O/S interface taxonomy](./04_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.4.part01.md) applies across architectures. The preserved [FG-TIDA cross-theme contracts](./05_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md) are one provisional implementation example; this annex does not edit them or require neighbouring Themes to adopt EA internals.

## 4. Four diagnostic lenses, one extensible parent

| EA profile and source seam | What the same T0–T2 case tests | What EA does **not** take over |
|---|---|---|
| [UC-EA-01](./UC-EA-01_v0.3_FROZEN.md) — CH-S3 primary; CH-S10/S14/S5 secondary | Does current Q/W and response capacity requalify T1 C1 before T2 A1, avoiding stale continuation and needless blanket escalation? | Qcritical signal generation, exceptional mandate and containment execution. |
| [UC-EA-02](./UC-EA-02_v0.6_MAINTENANCE_FREEZE.md) — CH-S5 primary; CH-S14/S6 secondary | Which evidence is sufficient, worth acquiring before the deadline, unavailable, correlated or structurally residual? | Identity/trust transport, source-side appraisal and privacy authorization. |
| [UC-EA-03](./UC-EA-03_v0.4_MAINTENANCE_FREEZE.md) — CH-S4 primary; CH-S13/S14/S5 secondary | Is the applicable human effectively available and informed, and what does H1 approval establish without curing the world model? | Human oversight lifecycle, grant origination and intervention mandate. |
| [UC-EA-04](./UC-EA-04_v0.5_MAINTENANCE_FREEZE.md) — CH-S9 primary; CH-S11/S14/S5 secondary | Can local G1/P1/evidence/oversight outputs compose for A1 without wrong-domain compensation, duplicated lineage or closure laundering? | Universal authority hierarchy, policy definition and producer-owned conflict resolution. |

[Validation Profile Family](./VALIDATION_PROFILE_FAMILY_v0.5_FROZEN.md) binds the four lenses. Their detailed stress branches, costs and acceptance evidence belong in the controlled profiles and the [masterclass](./DAOS_EA_USE_CASES_MASTERCLASS_v0.1.md), not in an invented fifth EA use case. CH-S1/S2/S7/S8/S12 remain primarily external-owner/interface or future-fixture surfaces; four EA tests do not establish full DAOS or ToR coverage.

## 5. Extension rule and fair-test gate

The model-case skeleton can be tested **upward** with additional providers/principals/authority layers, **downward** with a factory cell or smaller operating unit, and **horizontally** with other time/resource domains only while grant, role, preference, policy, commitment, action, change-event and bounded authority distinctions retain meaningful counterparts. The governing regime, hard constraints and outcome owner must be declared per variant. A local KPI cannot manufacture public mandate, a factory safety role cannot be relabelled municipal policy, and a mobility result cannot be advertised as a hospital/factory result. If an invariant fails, declare the extension boundary or open a new case/version.

For each comparison, freeze G1/P1/E1/D1/C1/A1/H1, source material, owner, regime, authority and deadline. Compare EA against a **strong** peer with scoped claims, source lineage, risk-aware acquisition, human oversight and exceptions. Pre-register unsupported action, stale-frame reuse, false systemic closure, needless hold, missed useful response, reviewer depletion and cost (calls, compute, latency, privacy, human minutes). If the peer reproduces EA's decision/residual trace at equal or lower burden, the claimed differential contracts; if EA improves trace but makes response too late, the potential benefit also fails. A positive branch is bounded to the stated case/version. This is a test design, **not** evidence that those tests have been run.

## 6. Corpus and status disposition

This annex belongs after the integrated foundation and general F1–F9/O/S architecture, before the validation family. It makes the DAOS relation an explicit EA corpus interface **without importing the parent programme into EA**. Parent facts, ToR, standards status, governance and public submissions remain in their own source records. The already published masterclass remains the detailed reader/test guide in this consolidated EA corpus folder; this annex is the architectural contract, not a duplicate parent Case Study.
