# 00K-A25 — Failure Case-Study Extensibility & Requirements-Conformance Transfer — v0.1

| | |
|---|---|
| **Source extensibility discipline** | [DAOS Annex II — Why the Minimal Case Is Extensible](../../../submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/03_ANNEX_II_Case_Extensibility.md) |
| **Requirements** | [00 — Canonical Requirements](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) |
| **P↔S traceability / sufficiency** | [A19](./00K_A19_PRINCIPLE_REQUIREMENT_TRACEABILITY_AND_CONSERVATION_PROOF_v0.1.md) · [A23](./00K_A23_CANONICAL_REQUIREMENT_CONFORMANCE_SUFFICIENCY_P1_P6_v0.1.md) |
| **Information refinement** | [A24](./00K_A24_PRINCIPLE_REQUIREMENT_INFORMATION_GAIN_AND_NON_EQUIVALENCE_v0.1.md) |
| **Machine-readable registry** | [fixtures/CASE-EXTENSION](./fixtures/CASE-EXTENSION/README.md) |
| **Status** | first-pass structural extensibility framework; logical transfer theorem; listed domain extensions remain design-level until separately executed |
| **Date** | 25 September 2026 |

> **Result.** 00E–00J are treated as **minimum concrete instantiations of six structural failure case-study families**, not as one-off stories. An upward/vertical, downward or horizontal variant belongs to the same family only when it preserves the family's independently stated failure kernel, decision semantics and requirement surface. For every admitted extension, canonical requirements conformance transfers through A23 to the relevant P invariants; because the family failure predicate requires violation of at least one of those invariants, a canonically conforming implementation cannot exhibit that same structural failure. This is a conditional structural theorem, not a claim that every superficially similar real-world situation has already been proved equivalent.

---

## 1. Why failure scenarios need an extensibility layer

A scenario such as:

- “100 million tokens”,
- “a bridge full of robotaxis”,
- “robots believe they are in Napoleonic France”,
- “4,000 refunds”,
- “a queued database rollback”, or
- “the author pays for their own work”

is deliberately memorable.

But those narrative details are not the architectural claim.

The claim concerns a smaller **failure kernel**: a set of relations among evidence, scope, authority, time, composition, residual state, capacity and decision that can appear in many different implementations.

The purpose of case-study extensibility is therefore to separate:

\[
\text{minimum narrative instantiation}
\]

from:

\[
\text{structural case family}.
\]

The minimum case makes the problem inspectable. The family tests how far the same structural problem survives controlled changes in scale and domain.

---

## 2. Reuse of the DAOS extensibility discipline

DAOS Annex II uses three extension directions.

### 2.1 Upward / vertical extension

Increase scale or organizational depth while retaining the same semantic relations.

Typical changes:

- more actors;
- more roles;
- more agents;
- nested objectives;
- additional jurisdictions/owners;
- larger dependency graphs;
- more layers of aggregation/delegation/composition.

This document uses **upward/vertical** as synonyms so the original DAOS “upward” term and the ordinary “vertical extensibility” reading remain aligned.

### 2.2 Downward extension

Reduce the case to the smallest implementation that still contains the structural failure.

Typical changes:

- one team instead of an enterprise;
- one production cell instead of a city;
- one assistant plus memory instead of a multi-agent population;
- two records instead of a large registry;
- one queued action instead of a distributed workflow.

Downward extension is especially important because it distinguishes a true structural mechanism from an artefact that exists only because the story is large.

### 2.3 Horizontal extension

Change the service/business domain while preserving the same structural relations.

The names of resources, organizations, policies and outcomes may change.

The meaning of:

- evidence sufficiency;
- unresolved state;
- authority;
- scope;
- material change;
- provenance/dependence;
- composition; and
- receiving decision

may not silently change.

---

## 3. A failure case-study family

For scenario \(C\), define:

\[
Family(C)=
\langle
K_C,\sigma_C,F_C,I_C,R_C
\rangle
\]

where:

- \(K_C\) — structural failure kernel;
- \(\sigma_C\) — type of subject–proposition–decision boundary;
- \(F_C\) — family failure predicate;
- \(I_C\subseteq\{P1,\ldots,P6\}\) — principle witnesses whose violation is sufficient for the family failure route;
- \(R_C\) — canonical S/T conformance route that protects those invariants.

The story-specific names, amounts, vendors, locations and technologies are **parameters**, not the kernel.

---

## 4. Admission test for an extension

A proposed extension \(C'\) belongs to \(Family(C)\) only if all six tests pass.

### X1 — kernel preservation

There is a mapping:

\[
h:K_C\rightarrow K_{C'}
\]

that preserves every decision-material relation in the kernel.

Changing “bridge” to “hospital bed capacity” is allowed.

Changing “shared scarce resource” into a situation with no shared resource is not an 00F extension.

### X2 — decision-boundary preservation

The extension has an identifiable:

\[
\sigma'(d,t)
\]

with the same structural proposition and decision dependency.

The subject may change; the role played by evidence/scope/authority/time in the final decision may not.

### X3 — failure-predicate preservation

The terminal failure is the same **structural predicate**, not merely a similarly bad outcome.

For example:

- downtime caused by stale queued action may be 00I;
- downtime caused only by hardware failure is not.

### X4 — requirement-route preservation

Every canonical S/T clause that is material to the base kernel remains applicable under the mapped roles.

An extension may activate additional requirements. It may not weaken the inherited route and still claim to be the same family.

### X5 — positive-control preservation

A family includes the legitimate counterpart needed to prevent shortcut solutions.

Examples:

- 00G must accept genuine regime change rather than reject every new frame;
- 00H must accept genuinely authorized campaigns and preserve genuine findings;
- 00J must accept legitimate transfer/independent creation rather than block all downstream rights claims.

### X6 — no hidden new primitive

If the proposed variant needs a new semantic object/operator that does not normalize through the current A21 requirement grammar, it is a **case-family extension candidate**, not yet an admitted member.

It may be evidence for Requirements-vNext or a new case study.

---

## 5. Membership is independent of success

The admission test is not:

> “the requirements work, therefore this is the same case.”

That would be circular.

Membership is established from:

- the structural kernel;
- decision boundary;
- relation mapping;
- requirement applicability; and
- positive/negative control semantics

**before** scoring a candidate implementation.

A requirements-conforming implementation may therefore pass or fail the extension test empirically; its outcome does not determine family membership.

---

## 6. Requirements-conformance transfer theorem

For an admitted extension \(C'\in Family(C)\), each family profile establishes:

\[
F_C(C')\Rightarrow
\bigvee_{i\in I_C}\neg P_i(C').
\]

That statement means that the structural family failure cannot occur without violating at least one of its mapped P invariants.

A23 establishes:

\[
Conf_{R_C}(C')
\Rightarrow
\bigwedge_{i\in I_C}P_i(C').
\]

Therefore:

\[
\boxed{
C'\in Family(C)
\land
Conf_{R_C}(C')
\Rightarrow
\neg F_C(C')
}
\]

by contradiction.

### Interpretation

If:

1. the variant really is an extension of the same case family under X1–X6; and
2. the implementation really satisfies the applicable canonical requirement route;

then it cannot exhibit the **same structural failure** represented by the base scenario.

This is the desired transport from one minimum fixture to a larger case family.

---

## 7. What this theorem does not say

It does not establish that:

- every superficially similar incident belongs to one of 00E–00J;
- every listed first-pass domain example has already been executed;
- requirements conformance prevents every possible failure in that domain;
- P1–P6 or S1–S14 are universally complete for all future case families;
- a system cannot fail for a different mechanism after preventing the mapped one.

The theorem is deliberately scoped:

> **same family kernel + canonical conformance ⇒ no same-family structural failure.**

---

## 8. Six case-study families

| Family | Minimum instantiation | Structural kernel | Primary principle witness | Extensibility profile |
|---|---|---|---|---|
| **00E** | Meridian / 100M-token enterprise strategy | lossy qualification compression + bounded/unbounded uncertainty mismanagement compounded through a composed decision chain | P1/P2/P3/P6 | [00E profile](./00E_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md) |
| **00F** | Aurora City / Central Bridge | locally justified postures become incompatible over a shared decision/resource after heterogeneous windows or frame drift | P6, with P1/P2/P3/P5 branches | [00F profile](./00F_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md) |
| **00G** | Bar-to-Napoleon | repeated/correlated claims are promoted into independent support or authority and displace a still-valid mission/frame | P6, with P1/P3/P4/P5 controls | [00G profile](./00G_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md) |
| **00H** | Quiet Four Thousand | a genuine material opportunity exceeds current authority; system must preserve the finding without unauthorized execution | P4, with P1/P6 composition/preservation branches | [00H profile](./00H_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md) |
| **00I** | Patch That Undid the Fix | decision correct at qualification time becomes stale before actuation while technical reach/authorization remains valid | P5 | [00I profile](./00I_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md) |
| **00J** | Author Pays for Their Own Work | a valid narrow provenance statement is promoted through broken lineage/correlation into a stronger unsupported downstream enforcement proposition | P1, with P4/P6 | [00J profile](./00J_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md) |

---

## 9. First-pass family status

The six profiles distinguish three statuses.

### Strong structural extension

The mapping to the kernel is direct enough to treat the variant as an in-family design case without changing the failure semantics.

This still does not make it an executed benchmark result.

### Candidate extension

The analogy is plausible but one or more mappings need a frozen fixture or additional source/owner definition before admission.

### Out-of-family neighbour

The situation may be important but lacks one of the kernel relations. It should not be used as evidence that the present family generalizes.

---

## 10. Relationship to A24 information refinement

A24 explains why requirements add more information than principles.

A25 uses that extra information to make case transfer possible.

A P signature alone can say:

\[
\{P1,P4,P6\}.
\]

The S/T route additionally tells us whether those invariants are being exercised in:

- a handoff;
- a delegation;
- a composition;
- a historical repair;
- a rights/enforcement decision; or
- another typed decision boundary.

That typed information is what permits a proposed extension to be tested for structural equivalence instead of merely sharing a principle label.

Therefore:

\[
\text{Principles}
\rightarrow
\text{typed requirements}
\rightarrow
\text{case-family extension}
\]

is an information-refinement chain, while A23 supplies the reverse conformance guarantee.

---

## 11. Next evidentiary step

The current profiles are a **first-pass structural generalization**.

The next stronger claim would require, for each family:

1. freeze one or more nontrivial extensions;
2. instantiate the same requirement route;
3. preserve matched facts/resources across nonconforming and conforming arms;
4. execute the family failure predicate;
5. test whether canonical conformance continues to imply no family failure;
6. record any extension that escapes the kernel or requirement language as a falsifier rather than forcing it into the family.

That future work is how the corpus can move from bounded structural extensionality toward a stronger statement about equivalence classes of implementations.
