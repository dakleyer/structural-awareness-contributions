# 00K-A21 — Requirement Normal-Form Closure & Relative Completeness Proof — v0.1

> **Preserved alternate formalization.** The preferred requirement-completeness proof is [00K-A21 — Requirement Basis Closure & Relative Completeness](./00K_A21_REQUIREMENT_BASIS_CLOSURE_AND_RELATIVE_COMPLETENESS_PROOF_v0.1.md).


| | |
|---|---|
| **Upstream foundation closure** | [02B](./02B_FOUNDATIONAL_SYNTAX_CLOSURE_AND_P1_P6_NORMAL_FORM_PROOF_v0.1.md) |
| **Semantic P↔S bridge** | [00K-A19](./00K_A19_PRINCIPLE_REQUIREMENT_TRACEABILITY_AND_CONSERVATION_PROOF_v0.1.md) |
| **Canonical requirements** | [00 — S1–S14](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) |
| **Scenario coverage** | [00K-A02](./00K_A02_REQUIREMENTS_COVERAGE_MATRIX_ADDENDUM_v0.1.md) |
| **Status** | requirement normal-form closure / relative completeness proof |
| **Date** | 25 September 2026 |

> **Result.** Relative to the current decision-boundary vocabulary and the six P normal forms, S1–S14 are a complete set of primitive requirement normal forms. A candidate “S15” expressed entirely with the current semantic objects and operators either normalizes to an existing S#, is a measurable refinement/implementation detail of an existing S#, or is outside EA ownership. A genuinely non-reducible S15 would require a new semantic object/relation or a new foundational principle and would therefore falsify this closure result.

---

## 1. Why A19 was not enough

A19 established strong non-vacuous traceability:

\[
P1\text{–}P6\leftrightarrow S1\text{–}S14
\]

and gave six anchor lemmas.

But a critic could still ask:

> Why these fourteen requirements? Could there be an S15 that is equally primitive and simply missing from the matrix?

A21 makes that question explicit and falsifiable.

---

## 2. Canonical decision-boundary syntax

The Requirements document defines the test unit as a material subject–proposition–decision boundary:

\[
\sigma(d,t).
\]

The same scope, owner, time, evidence boundary and response horizon must remain visible through S/T/H/KPI evaluation.

For requirement generation, expand the decision boundary into the semantic fields/relations that the current corpus already recognizes.

### 2.1 Primitive semantic objects

\[
Object=
\{
Actor,
Authority,
DecisionBasis,
Context,
Evidence,
EpistemicState,
Dependency,
Commitment,
Intervention,
History,
Capacity
\}.
\]

These are not new runtime fields. They are normal-form categories over the vocabulary already used by S1–S14.

### 2.2 Primitive relations / lifecycle operators

\[
Relation=
\{
represents,
grants,
supports,
handsOff,
delegates,
composes,
changes,
commits,
intervenes,
records,
repairs
\}.
\]

### 2.3 Principle operators

From 02B:

\[
Operator=
\{
QUALIFY,
BOUND,
NONPROMOTE,
AUTHQUAL,
REQUALIFY,
COMPOSE
\}.
\]

A primitive requirement is therefore a well-typed obligation of the form:

\[
Req(op,obj,rel,\sigma).
\]

The requirement is primitive only if it constrains a decision-material semantic object/relation rather than naming one implementation technology.

---

## 3. Requirement normal forms

Applying the six principle operators to the declared decision-boundary objects yields fourteen non-redundant requirement normal forms.

### Q1 — authority standing/current applicability → S1

\[
AUTHQUAL(Authority,grants,\sigma)
\Rightarrow S1.
\]

This covers origin, standing, purpose/scope, expiry/revocation, applicability and evidence of the authority fact.

### Q2 — principal preference / reviewable decision basis → S2

\[
QUALIFY(DecisionBasis,supports,\sigma)
\Rightarrow S2.
\]

### Q3 — regime/context and governed escape → S3

\[
REQUALIFY(Context,changes,\sigma)
\land BOUND(Context,changes,\sigma)
\Rightarrow S3.
\]

### Q4 — effective human oversight capacity → S4

\[
BOUND(Capacity,intervenes,\sigma)
\land AUTHQUAL(Actor,intervenes,\sigma)
\Rightarrow S4.
\]

### Q5 — operational indeterminacy / containment → S5

\[
NONPROMOTE(EpistemicState,commits,\sigma)
\land BOUND(EpistemicState,changes,\sigma)
\Rightarrow S5.
\]

### Q6 — bounded trust handoff / privacy-preserving qualification → S6

\[
QUALIFY(Evidence,handsOff,\sigma)
\Rightarrow S6.
\]

The privacy constraint is a boundary condition on what qualification is legitimately exposed; it does not create a seventh epistemic operator.

### Q7 — identity / representation link → S7

\[
QUALIFY(Actor,represents,\sigma)
\Rightarrow S7.
\]

### Q8 — bounded subdelegation / non-amplification → S8

\[
AUTHQUAL(Authority,delegates,\sigma)
\Rightarrow S8.
\]

### Q9 — multi-principal composition / non-substitution → S9

\[
COMPOSE(Dependency,composes,\sigma)
\Rightarrow S9.
\]

### Q10 — commitment state + material change → S10

\[
REQUALIFY(Commitment,changes,\sigma)
\Rightarrow S10.
\]

### Q11 — policy/objective integrity across domains → S11

\[
COMPOSE(DecisionBasis,composes,\sigma)
\land QUALIFY(DecisionBasis,supports,\sigma)
\Rightarrow S11.
\]

### Q12 — accountability / challenge / repair → S12

\[
QUALIFY(History,records,\sigma)
\land REQUALIFY(History,repairs,\sigma)
\Rightarrow S12.
\]

This is the persistence/re-entry realizability form of P1/P5: the qualified basis must remain reconstructable enough for challenge and future repair.

### Q13 — authority history vs intervention history → S13

\[
AUTHQUAL(History,intervenes,\sigma)
\land QUALIFY(History,records,\sigma)
\Rightarrow S13.
\]

### Q14 — evidence-to-decision assessment → S14

\[
QUALIFY(Evidence,supports,\sigma)
\]

with the cross-cutting requirement to state sufficiency/insufficiency/inconclusiveness and which receiving decision is supported.

S14 is the assessment normal form spanning all six P operators; it is not an additional seventh principle.

---

## 4. Why fourteen rather than sixty-six arbitrary combinations

The Cartesian product \(Operator\times Object\times Relation\) contains many syntactically possible strings, but most are not well-typed primitive obligations.

Examples:

- \(AUTHQUAL(Evidence,repairs)\) is ill-typed: evidence does not issue authority.
- \(BOUND(History,records)\) is not a distinct safety primitive; retention bounds are implementation/governance parameters unless they change one of the material S12/S13 obligations.
- \(REQUALIFY(Actor,represents)\) normalizes to S7/S10/S13 depending whether the material change concerns representation, commitment, or intervention history.
- \(COMPOSE(Evidence,composes)\) normalizes to S9/S11 and, where the question is whether evidence supports the receiving decision, S14.

A primitive requirement therefore survives normalization only when the object/relation pair has a distinct decision-material failure mode not already owned by another normal form.

The fourteen Q1–Q14 above are those surviving normal forms in the current grammar.

---

## 5. Total normalization rules

For any well-typed candidate requirement \(r\), apply the first matching rule.

### NR1 — authority standing / grant applicability

If the obligation concerns whether authority exists, remains current, or applies to the action:

\[
r\mapsto S1.
\]

### NR2 — preference/decision-basis fidelity

If it concerns whether the decision still represents the principal's declared basis:

\[
r\mapsto S2.
\]

### NR3 — regime/context transition / exceptional escape

If it concerns change of operating frame, bounded escape, re-entry or anti-oscillation:

\[
r\mapsto S3.
\]

### NR4 — human/oversight capability

If it concerns whether an authorized human/role can actually intervene within the useful horizon:

\[
r\mapsto S4.
\]

### NR5 — unresolved state / containment

If it concerns incomplete/conflicting/stale state and whether that becomes permission or unbounded containment:

\[
r\mapsto S5.
\]

### NR6 — trust/evidence handoff

If it concerns preservation of enough qualified status/evidence across a privacy/trust boundary:

\[
r\mapsto S6.
\]

### NR7 — identity / representation

If it concerns who/what acts for whom:

\[
r\mapsto S7.
\]

### NR8 — delegation / non-amplification

If it concerns authority propagation through chains:

\[
r\mapsto S8.
\]

### NR9 — multi-principal / dependency composition

If it concerns concurrence, conflict, dependence, substitution, unsupported convergence or incompatible divergence:

\[
r\mapsto S9.
\]

### NR10 — commitment + material change

If it concerns a previously qualified decision becoming stale before commitment/action:

\[
r\mapsto S10.
\]

### NR11 — policy/objective integrity across domains

If it concerns policy/preference/version/scope relations surviving cross-domain composition:

\[
r\mapsto S11.
\]

### NR12 — reconstructability / challenge / repair

If it concerns reconstructing the qualified basis and repairing future state without rewriting history:

\[
r\mapsto S12.
\]

### NR13 — original authority vs later intervention

If it concerns preserving the distinction between the original authority history and later human/technical intervention:

\[
r\mapsto S13.
\]

### NR14 — evidence sufficiency for receiving decision

If it asks what must be demonstrated, whether evidence is sufficient/inconclusive and which decision it supports:

\[
r\mapsto S14.
\]

---

## 6. Coverage theorem

Let \(G_R\) be the set of primitive, well-typed requirements expressible using:

- the current \(\sigma(d,t)\) decision-boundary vocabulary;
- the Object/Relation grammar in §2; and
- the six principle operators from 02B.

Let \(N_R(r)\) be application of NR1–NR14.

### Theorem

For every \(r\in G_R\):

\[
N_R(r)\in\{S1,\ldots,S14\}.
\]

### Reason

Every declared primitive object/relation has an owner normal form:

| Semantic object/relation | Canonical normal form(s) |
|---|---|
| authority / grant | S1 |
| principal decision basis | S2 |
| context/regime transition | S3 |
| intervention capacity | S4 |
| unresolved epistemic state | S5 |
| evidence/trust handoff | S6 |
| identity/representation | S7 |
| delegation chain | S8 |
| multi-principal dependency/composition | S9 |
| commitment/material change | S10 |
| policy/objective cross-domain integrity | S11 |
| reconstructability/repair | S12 |
| intervention-vs-authority history | S13 |
| evidence→receiving-decision sufficiency | S14 |

No grammar category remains without a normal form.

Therefore the current S1–S14 set is **relatively complete for the current requirement grammar**. ∎

---

## 7. No-missing-primitive corollary

A proposed S15 can have only four dispositions.

### C1 — same primitive, different wording

It normalizes to an existing S#.

Disposition: **not new**.

### C2 — stronger field/threshold/evidence requirement inside an existing normal form

Examples: additional freshness field, different timeout, extra provenance qualifier, stronger privacy mechanism.

Disposition: **refinement / profile / KPI / implementation constraint**, not a new primitive S#.

### C3 — obligation belongs to an external owner

Examples: issuing a legal grant, authenticating an identity, executing physical containment.

Disposition: **ownership/interface requirement**, not a new EA primitive.

### C4 — genuinely new semantic object/relation/operator

It cannot be normalized by NR1–NR14.

Disposition: **valid counterexample**. This reopens the canonical requirement set and normally also requires revisiting 02B/P1–P6.

This makes “no S15 is currently needed” a falsifiable structural result rather than a policy preference.

---

## 8. Bidirectional consistency with P1–P6

A19 already records primary/supporting P projections for every S#.

A21 adds the generative direction:

\[
P\text{-operators} + \sigma\text{-objects/relations}
\Rightarrow S1\text{–}S14.
\]

A19 supplies the reverse interpretive direction:

\[
S1\text{–}S14
\Rightarrow P_{\text{primary}} + P_{\text{supporting}}.
\]

So the relationship is now:

\[
P1\text{–}P6
\;\xleftrightarrow[\text{A19 interpretation}]{\text{A21 generation}}\;
S1\text{–}S14.
\]

This is stronger than a coverage matrix and weaker than claiming every S is logically equivalent to exactly one P.

---

## 9. Relation to the existing vNext review

The existing Requirements vNext review has so far recommended **no S15+, T5+, H7+** despite later 00G/00H/00I/00J developments.

A21 explains structurally why that result is plausible:

the newer cases introduce new fixtures and stress combinations, but their obligations normalize to existing authority, evidence, change, containment and composition normal forms.

This is corroboration, not a premise of the theorem.

---

## 10. Falsifier

A21 is falsified by one concrete counterexample:

> a decision-material requirement expressed entirely in the current \(\sigma(d,t)\), Object/Relation and P-operator vocabulary that cannot be normalized by NR1–NR14 without loss of a genuinely distinct obligation.

Such a counterexample should be recorded as an S15 candidate rather than forced retrospectively into an existing requirement.

---

## 11. Exact claim

The defensible statement is:

> **S1–S14 are a closed and relatively complete primitive requirement basis for the current P1–P6 / decision-boundary grammar. Alternative textual decompositions are possible, but within the declared semantics they normalize to the same fourteen requirement classes unless they introduce a genuinely new primitive object, relation or operator.**

This does not claim universal completeness for every future Structural Awareness problem.
