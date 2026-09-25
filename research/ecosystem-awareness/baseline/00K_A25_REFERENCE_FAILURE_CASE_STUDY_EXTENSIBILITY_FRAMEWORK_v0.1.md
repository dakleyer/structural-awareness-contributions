# 00K-A25 — Reference Failure Case-Study Extensibility Framework — v0.1

| | |
|---|---|
| **Source model** | [DAOS Annex II — Case Extensibility](../../../submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/03_ANNEX_II_Case_Extensibility.md) |
| **Canonical requirements** | [00 — S1–S14 / T1–T4](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) |
| **Requirement→principle sufficiency** | [A23](./00K_A23_CANONICAL_REQUIREMENT_CONFORMANCE_SUFFICIENCY_P1_P6_v0.1.md) |
| **Information/refinement boundary** | [A24](./00K_A24_PRINCIPLE_REQUIREMENT_INFORMATION_GAIN_AND_NON_EQUIVALENCE_v0.1.md) |
| **Profiles** | [00E](./00E_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md) · [00F](./00F_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md) · [00G](./00G_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md) · [00H](./00H_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md) · [00I](./00I_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md) · [00J](./00J_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md) |
| **Status** | first-pass bounded extensibility design; not proof of universal implementation equivalence |
| **Date** | 25 September 2026 |

> **Result.** 00E–00J are treated as six bounded **Model Case Studies**, not as six one-off stories. Each case has a frozen structural kernel, a canonical requirement route, upward/downward/horizontal extension directions, an admission boundary and a requirements-preservation obligation. If an extension preserves the case kernel and the canonical conformance mapping, then the case-level design result transports to that extension: a canonically requirements-conforming route cannot realize the same abstract failure predicate. This is a conditional generalization theorem, not yet an empirical claim over every implementation in every domain.

---

## 1. Reuse the DAOS discipline, not merely its vocabulary

DAOS Annex II makes three distinctions:

- **upward extension** adds actors, roles, objective layers, jurisdictions or scale;
- **downward extension** reduces the setting to the smallest bounded deployment that still preserves the structural problem;
- **horizontal extension** changes domain while preserving the same structural meanings.

Its boundary rule is equally important:

> if the new situation cannot be represented by adding/removing/renaming domain instances without redefining the core concepts, it is not an extension of the same case.

A25 applies the same discipline to the six reference failure families.

---

## 2. Case-study object

For each scenario \(s\in\{00E,\ldots,00J\}\), define:

\[
Case_s=
\langle
K_s,
R_s,
F_s,
C_s,
E_s
\rangle
\]

where:

- \(K_s\) — frozen structural kernel: the smallest relation pattern that makes the failure mechanism the same mechanism;
- \(R_s\) — applicable canonical S/T conformance route;
- \(F_s\) — abstract failure predicate;
- \(C_s\) — positive/negative controls preventing trivial deny-all, allow-all or narrative-shortcut solutions;
- \(E_s\) — admitted extension class.

The concrete story — tokens, bridge, Napoleon, 4,000 refunds, database patch or rights registry — is an instantiation of \(K_s\), not the definition of the failure family.

---

## 3. Admissible extension

An extension \(e\) of case \(s\) is admitted only if there is an abstraction map:

\[
h_e:Trace_e\rightarrow Trace_s
\]

satisfying all seven conditions.

### X1 — kernel preservation

Actors, records, resources and technologies may change, but every essential relation in \(K_s\) has an isomorphic or typed-equivalent relation in the extension.

### X2 — failure reflection

If the extension realizes the proposed failure:

\[
F_e(\tau)
\]

then the abstracted trace realizes the base failure:

\[
F_s(h_e(\tau)).
\]

A new failure mechanism that cannot be reflected into \(F_s\) is evidence for another Case Study.

### X3 — conformance preservation

Canonical conformance is not weakened by the translation:

\[
Conf_e(R_s,\tau)
\Rightarrow
Conf_s(R_s,h_e(\tau)).
\]

The extension may activate additional **existing** S/T obligations when new typed objects become material, but it may not silently drop a base obligation.

### X4 — positive-control preservation

A legitimate positive branch remains passable. An extension is invalid if it “solves” the failure only by blocking all actions, all new evidence, all delegation, all frame change or all downstream claims.

### X5 — authority/evidence neutrality

The extension may not make the case easier by silently granting broader authority, a better oracle, independent evidence or a stronger owner than the base comparison permits.

### X6 — finite resource and time declaration

Scale may change, but deadline, capacity, observation cost and response horizon remain explicit. “Upward” cannot mean unlimited resources.

### X7 — no hidden new primitive

If the extension requires a new decision-material object/operator/invariant outside the current requirement grammar, it is a Requirements-vNext / new-case candidate rather than evidence that the old case already covered it.

---

## 4. Three extension directions

### 4.1 Upward

\[
K_s\rightarrow K_s + actors/layers/instances/jurisdictions/resources
\]

without changing the kernel relation.

Purpose: test whether the same failure survives scale and organizational/ecosystem depth.

### 4.2 Downward

\[
K_s\rightarrow K_s^{min}
\]

by removing non-essential actors/steps until one further removal would destroy the mechanism.

Purpose: expose the smallest reproducible case and reduce narrative dependence.

### 4.3 Horizontal

\[
Domain_a\rightarrow Domain_b
\]

while preserving \(K_s\), \(F_s\), \(R_s\) and the control logic.

Purpose: test whether the failure family is structural rather than domain-specific.

---

## 5. Requirements-preserving extension theorem

Each current scenario already defines a requirements-conforming Route Q or equivalent gate interpretation and states a **design-level** sufficiency proposition for its frozen fixture.

Let that proposition be:

\[
Conf_s(R_s,\tau)\Rightarrow\neg F_s(\tau).
\]

This is not an empirical deployment result; it is the current scenario/gate semantics.

Now take an admitted extension \(e\in E_s\).

### Theorem

\[
Conf_e(R_s,\tau)\Rightarrow\neg F_e(\tau).
\]

### Proof

Assume:

\[
Conf_e(R_s,\tau)
\]

and, for contradiction,

\[
F_e(\tau).
\]

By X3:

\[
Conf_s(R_s,h_e(\tau)).
\]

By X2:

\[
F_s(h_e(\tau)).
\]

But the base case design-sufficiency proposition gives:

\[
Conf_s(R_s,h_e(\tau))
\Rightarrow
\neg F_s(h_e(\tau)).
\]

Contradiction.

Therefore:

\[
Conf_e(R_s,\tau)\Rightarrow\neg F_e(\tau).
\]

∎

---

## 6. What this theorem does and does not establish

It establishes a **transport rule**:

> once a new implementation/domain is shown to be an admitted extension of a case, requirements conformance blocks the same abstract failure for that extension under the same declared semantics.

It does **not** establish yet that:

- every implementation that looks similar is an admitted extension;
- the current extension examples exhaust the equivalence class;
- every implementation actually conforms to the requirements;
- an implementation cannot fail by a different mechanism;
- the current requirements are universally complete.

The research programme therefore moves from:

> “the requirements stop this one story”

toward:

> “the requirements stop this structural failure across every admitted member of the case equivalence class.”

The missing empirical/formal work is to expand and test \(E_s\), not to rewrite the requirements for each example.

---

## 7. Portfolio summary

| Case | Structural family | Primary extension question |
|---|---|---|
| **00E** | compounded epistemic loss across heterogeneous decision pipelines | does local competence still collapse under larger/smaller/different composed reasoning pipelines? |
| **00F** | locally correct postures become incompatible over a shared resource after frame change | does local safety remain non-fungible with shared-resource/mission compatibility? |
| **00G** | correlated/repeated external frame displaces a still-valid objective | can message repetition/recency/role drift be separated from independent evidence and legitimate frame change? |
| **00H** | qualified beneficial opportunity lies outside current authority | can discovery be preserved without unauthorized execution at any scale/domain? |
| **00I** | a correct deferred decision becomes stale before use | does action-time semantic requalification survive different queues, workflows and domains? |
| **00J** | a narrower valid provenance claim becomes a stronger downstream entitlement/enforcement claim | does provenance/authority scope survive transformation, replication and downstream reliance? |

---

## 8. Next proof layer

The six profiles below define the first candidate \(E_s\) classes.

The next strong result should be executable **metamorphic extensionality testing**:

1. freeze one base trace;
2. generate upward/downward/horizontal variants through declared transforms;
3. keep the abstract oracle \(F_s\) fixed;
4. run the same canonical requirement route;
5. verify that conformance disposition is invariant under allowed renaming/scale/domain changes;
6. treat any extension that passes all requirements yet realizes \(F_e\) as a Requirements-vNext or case-boundary falsifier.

No such cross-extension execution is claimed by A25 v0.1.
