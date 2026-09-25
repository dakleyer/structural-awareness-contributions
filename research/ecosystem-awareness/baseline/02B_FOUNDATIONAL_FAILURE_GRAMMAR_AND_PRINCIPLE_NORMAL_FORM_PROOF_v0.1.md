# 02B — Foundational Failure Grammar & P1–P6 Syntactic Normal-Form Proof — v0.1

> **Preserved explanatory companion.** The preferred syntactic closure proof is [02B — Foundational Syntax, Normal Forms & Principle Closure](./02B_FOUNDATIONAL_SYNTAX_NORMAL_FORMS_AND_PRINCIPLE_CLOSURE_PROOF_v0.1.md). This file remains useful for the ordered-normalizer presentation but is not the canonical proof route.


| | |
|---|---|
| **Upstream foundation** | [01 — Integrated Foundational Theory](./01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md) · [02 — Epistemic Safety Principles & Control Matrix](./02_EPISTEMIC_SAFETY_PRINCIPLES_CONTROL_MATRIX_v0.4.part01.md) |
| **Semantic derivation companion** | [02A](./02A_FOUNDATION_TO_OPERATIONAL_PRINCIPLE_DERIVATION_PROOF_v0.1.md) |
| **Downstream requirement grammar** | [00K-A21](./00K_A21_REQUIREMENT_GRAMMAR_CLOSURE_AND_UNIQUENESS_PROOF_v0.1.md) |
| **Status** | syntactic normal-form proof relative to the declared foundational grammar |
| **Date** | 25 September 2026 |

> **Result.** Relative to the declared foundational grammar below, every admissible foundational failure/condition expression normalizes to exactly one of P1–P6, and every P1–P6 is reached by at least one expression. P1–P6 are therefore the six syntactic normal forms of the current Foundation/Control-Matrix failure language. This is stronger than semantic resemblance and weaker than a claim that no future extension of the foundational language can add a seventh normal form.

---

## 1. Canonical foundational basis

The current foundation has two orthogonal pieces.

### 1.1 Epistemic position

For a decision domain \(d\) and time \(t\), write the qualified epistemic position as:

\[
E(d,t)=[A,B,C,D].
\]

The current reader-facing semantics are:

- **A** — situated assertion/scope: what is sufficiently supported for the present decision boundary;
- **B** — confidence/intensity and explicit unresolved qualification inside that boundary;
- **C** — recognized current-capability frontier: potentially knowable/reachable state not presently established;
- **D** — structural/residual unknown that cannot be presumed exhaustively discoverable.

The older “known / known-unknown / potentially knowable / structural residual” reading is a coarse explanatory projection of the same four-way distinction, not a competing register.

### 1.2 Condition/failure class

The foundation distinguishes:

- **Type 0** — structural or frame-relative non-determination despite correct management;
- **Type 1** — uncertainty is acknowledged but determination/expansion remains unbounded or cannot reach legitimate closure inside available capacity/time;
- **Type 2** — uncertainty, scope or residual is suppressed/promoted into unjustified certainty or permission.

Type 0 is a condition, not a management failure.

---

## 2. Foundational expression grammar

An admissible foundational expression is a tuple:

\[
f=\langle \tau,\lambda,\rho,\theta,\kappa\rangle
\]

where:

### Failure/condition class

\[
\tau\in\{T0,T1,T2\}.
\]

### Locus

\[
\lambda\in\{I,O\}
\]

with:

- \(I\): inside the active represented/windowed decision frame;
- \(O\): outside the active window / residual-facing boundary.

### Propagation mode

\[
\rho\in\{L,R,C\}
\]

with:

- \(L\): local/internal;
- \(R\): received from another participant/source;
- \(C\): composed across several participants/domains/records.

### Temporal mode

\[
\theta\in\{S,\Delta\}
\]

with:

- \(S\): same qualified decision basis;
- \(\Delta\): a material time/frame change occurs between qualification and use.

### Claim class

\[
\kappa\in\{G,AUT\}
\]

with:

- \(G\): generic evidence/world-state/policy proposition;
- \(AUT\): authority/representation proposition relied on for action.

The grammar is not a Cartesian claim that every combination is meaningful. It is the **typing language** from which well-formed failure expressions are formed.

---

## 3. Well-formedness constraints

A tuple is admitted only if its semantics are meaningful.

### W1 — temporal specialization

\(\theta=\Delta\) is admitted only when a determination was previously qualified and is later reused/acted upon.

### W2 — authority specialization

\(\kappa=AUT\) is admitted only when a receiving decision relies on a claim of legitimate authority/representation for an action.

### W3 — composition specialization

\(\rho=C\) is admitted only when multiple records/domains/participants are being combined, compared, substituted or counted as corroboration.

### W4 — Type-1 meaning

\(T1\) denotes an acknowledged unresolved process whose error is lack of bounded viable closure, not false closure.

### W5 — Type-2 meaning

\(T2\) denotes an unjustified promotion/collapse: unresolved→determined, local→global, stale→current, unauthorised→authorised, or dependent→independent.

### W6 — Type-0 meaning

\(T0\) denotes a legitimate non-determination/residual condition whose category/scope must remain correctly represented.

---

## 4. Normalization rules

Define:

\[
N:F\rightarrow\{P1,P2,P3,P4,P5,P6\}
\]

by the following ordered rules.

### N5 — material temporal invalidation

If \(\theta=\Delta\) and a previously qualified determination is reused without requalification:

\[
N(f)=P5.
\]

This rule has first precedence because stale reuse is a temporal validity error even if the affected proposition is authority-, evidence- or composition-related.

### N4 — authority-typed qualification/non-amplification

Else, if \(\kappa=AUT\) and the relying action lacks a current decision-sufficient non-amplifying authority basis:

\[
N(f)=P4.
\]

### N6 — composition / scope-promotion failure

Else, if \(\rho=C\), or the error is promotion of local/windowed evidence into independent ecosystem-level support:

\[
N(f)=P6.
\]

### N3 — local/received Type-2 false closure

Else, if \(\tau=T2\):

\[
N(f)=P3.
\]

### N2 — Type-1 unbounded determination

Else, if \(\tau=T1\):

\[
N(f)=P2.
\]

### N1 — Type-0 / determination-boundary preservation

Else:

\[
N(f)=P1.
\]

The final case is necessarily \(T0\) under W4–W6.

---

## 5. Why the order is not arbitrary

The precedence removes syntactic overlap by selecting the **smallest discriminating operator**.

1. A material change creates a new qualification event; this is P5 even if the changed record happens to concern authority or composition.
2. Authority validity is a typed action boundary; knowing a grant correctly does not create the grant. This is P4.
3. Composition changes the semantic object from one qualified local claim to a relation among several claims. This is P6.
4. Remaining Type-2 cases are local/received false closure: P3.
5. Type-1 is the bounded-effort class: P2.
6. Remaining Type-0/pole-boundary preservation is P1.

This matches the semantic separations already established by A20: P1/P4, P1/P5 and P1/P6 can share the same records while remaining distinct obligations.

---

## 6. Totality theorem

### Theorem 1 — totality

Every well-formed foundational expression \(f\) has a normal form \(N(f)\in\{P1,\ldots,P6\}\).

### Proof

Take any well-formed \(f\).

- If it satisfies N5, it maps to P5.
- Otherwise, if it satisfies N4, it maps to P4.
- Otherwise, if it satisfies N6, it maps to P6.
- Otherwise, if \(\tau=T2\), it maps to P3.
- Otherwise, if \(\tau=T1\), it maps to P2.
- Otherwise W4–W6 imply \(\tau=T0\), so it maps to P1.

Thus every admitted expression maps to at least one P. ∎

---

## 7. Determinism theorem

### Theorem 2 — unique normal form

Every well-formed foundational expression maps to exactly one P1–P6.

### Proof

The normalization rules are ordered and terminal: once a higher-precedence predicate matches, lower rules are not evaluated as independent owners of the same expression.

The rule guards are therefore mutually exclusive **after precedence normalization**.

Hence \(N\) is a function, not a relation. ∎

This does not claim that an observed incident cannot exercise several principles simultaneously. It claims that **one atomic foundational violation expression has one canonical normal form**.

---

## 8. Surjectivity theorem

### Theorem 3 — all six normal forms are necessary to express the grammar

Each P has at least one admitted preimage.

| P | Example foundational expression | Interpretation |
|---|---|---|
| **P1** | \(\langle T0,O,R,S,G\rangle\) | receiver must preserve structural/residual qualification instead of pretending the received window is complete |
| **P2** | \(\langle T1,I,L,S,G\rangle\) | recognized unresolved in-window determination expands/searches without viable stopping |
| **P3** | \(\langle T2,I,L,S,G\rangle\) | known unresolved material state is promoted to permission/certainty |
| **P4** | \(\langle T2,I,R,S,AUT\rangle\) | a received/local grant is promoted beyond its current action scope |
| **P5** | \(\langle T2,I,R,\Delta,G\rangle\) | a once-valid basis changes before use and is not requalified |
| **P6** | \(\langle T2,O,C,S,G\rangle\) | local/dependent claims are composed as independent ecosystem truth |

Thus:

\[
\operatorname{range}(N)=\{P1,\ldots,P6\}.
\]

∎

---

## 9. Pole × Type closure

The normal forms can also be read directly from the foundation.

| Foundational issue | Pole/Type reading | Normal form |
|---|---|---|
| preserve legitimate non-determination / residual / scope | A/B/C/D distinction + Type 0 | **P1** |
| prevent acknowledged uncertainty from consuming unlimited determination capacity | B/C + Type 1 | **P2** |
| prevent unresolved represented state from becoming certainty/permission | B→A illegitimate collapse + Type 2 | **P3** |
| prevent qualified authority claim from becoming stronger authority | situated scope/authority qualification + Type 2 | **P4** |
| re-evaluate pole/validity assignment after material change | \(E(d,t_0)\not\equiv E(d,t_1)\) under \(\Delta\) | **P5** |
| prevent local/window/source position from becoming ecosystem truth through composition | A/C/D scope boundary + Type 2 composition | **P6** |

This table is a projection of the grammar, not the proof itself.

---

## 10. Syntactic completeness statement

Relative to the declared Foundation/Control-Matrix language:

\[
F/\!\sim_N
=
\{P1,P2,P3,P4,P5,P6\}
\]

where two well-formed expressions are equivalent when they normalize to the same operational invariant.

Therefore P1–P6 are **complete as normal forms of the current foundational failure grammar**.

A proposed seventh principle \(P7\) must do one of two things:

1. normalize to an existing P1–P6, in which case it is a refinement/example rather than an independent principle; or
2. require a new primitive axis, claim class, propagation mode or failure type not present in the current Foundation, in which case it is a **foundation extension**, not a missing normal form.

That is the exact syntactic sense in which the current six close the present foundation.

---

## 11. Boundary

This proof does not claim that:

- A/B/C/D or Type 0/1/2 can never be extended;
- every real incident has only one principle involved;
- P1–P6 are globally unique under every imaginable formal language; or
- the Foundation itself is universally complete.

It proves closure and uniqueness **relative to the current declared foundational syntax**.
