# 00K-A24 — Principle ↔ Requirement Refinement, Information Gain & Non-Equivalence Annex — v0.1

> **A23 audit qualification:** the reverse all-six sufficiency statements below are historical conditional arguments, not a currently closed result. A23 now certifies only its finite P1/P2/P4 projections and records P3/P5/P6 countermodels. The information/non-equivalence discussion does not supply the missing reverse proof. See [current A23](./00K_A23_CANONICAL_REQUIREMENT_CONFORMANCE_SUFFICIENCY_P1_P6_v0.1.md).

| | |
|---|---|
| **Principle semantics** | [02A](./02A_FOUNDATION_TO_OPERATIONAL_PRINCIPLE_DERIVATION_PROOF_v0.1.md) · [02B](./02B_FOUNDATIONAL_SYNTAX_CLOSURE_AND_P1_P6_NORMAL_FORM_PROOF_v0.1.md) |
| **Forward P→S traceability** | [A19](./00K_A19_PRINCIPLE_REQUIREMENT_TRACEABILITY_AND_CONSERVATION_PROOF_v0.1.md) |
| **Requirement-basis closure** | [A21](./00K_A21_REQUIREMENT_BASIS_CLOSURE_AND_RELATIVE_COMPLETENESS_PROOF_v0.1.md) |
| **Reverse S/T→P sufficiency** | [A23](./00K_A23_CANONICAL_REQUIREMENT_CONFORMANCE_SUFFICIENCY_P1_P6_v0.1.md) |
| **Canonical requirements** | [00 — S1–S14 / T1–T4 / H1–H6 / KPI protocol](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) |
| **Case-family transfer** | [00K-A25](./00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md) |
| **Status** | information-structure annex; no change to frozen requirement or principle semantics |
| **Date** | 25 September 2026 |

> **Result.** P1–P6 and S1–S14/T1–T4 are bidirectionally connected by semantic traceability and conformance sufficiency, but they are **not informationally equivalent**. The requirement layer is a strict refinement: it preserves the applicable principle invariant while adding decision-boundary typing, ownership, lifecycle location, conformance conditions and observable evidence obligations. Projecting a conforming requirement record back to P1–P6 is therefore a many-to-one, information-losing operation.

---

## 0. Canonical relationship at a glance

The three layers are related, but they are **not three restatements of the same information**.

\[
\boxed{
Foundation
\;\xrightarrow[\text{02B closure}]{\text{02A derivation}}\;
P1\text{–}P6
\;\underset{\text{A23 conformance sufficiency}}{\overset{\text{A19 semantic refinement}}{\rightleftarrows}}\;
S1\text{–}S14/T1\text{–}T4
}
\]

The arrows have different meanings.

### Foundation → Principles

This direction is **derivation plus operational normalization**, not equivalence.

The Foundation contains the broader explanatory theory:

- A/B/C/D epistemic positions;
- Type 0 / Type 1 / Type 2;
- open residual and bounded representation;
- finite determination capacity;
- received-signal qualification;
- dynamic decision-window validity;
- composition and non-fungibility;
- hypotheses, mechanisms and explanatory consequences.

P1–P6 **compress** that broader theory into six separately testable operational invariants. They add an operational structure that the Foundation does not itself need to expose in six ablation-ready labels:

- a stable six-element invariant basis;
- explicit normal forms;
- leave-one-out identity;
- mathematical independence objects;
- cross-scenario diagnostic coordinates.

So the principles **strengthen operational usability and falsifiability** of the Foundation while intentionally omitting much of its explanatory detail.

Therefore neither statement is correct:

\[
Foundation=P
\]

or:

\[
Info(P)>Info(Foundation)
\]

as a total-information claim.

The correct statement is:

> **P1–P6 are a semantics-preserving operational compression/normalization of the relevant Foundation invariants, enriched with explicit ablation/test identity.**

### Principles → Requirements

This direction is **typed specification refinement**.

The requirements retain the applicable P invariant and add:

- decision-boundary identity;
- typed object;
- lifecycle operator;
- owner/source;
- scope/time;
- handoff/delegation/composition location;
- sufficiently-good T# conditions;
- evidence/KPI/falsification obligations;
- disposition and re-entry semantics.

Thus the requirements are not a paraphrase of P1–P6.

### Requirements → Principles

This direction is **conformance sufficiency**, proved in A23.

A canonically conforming S/T route guarantees the applicable P invariant, but the projection back to P deliberately drops the additional requirement metadata.

Therefore the P↔S relation is bidirectional in **dependency/refinement**, while remaining non-equivalent in information content.

A compact formulation for the whole corpus is:

> **Foundation explains the semantic problem space; Principles normalize its operational invariants; Requirements refine those invariants into typed, owner-aware, observable conformance obligations. Requirements-conformance projects back to the Principles, but neither projection turns the layers into informational equals.**

## 1. Why this annex exists

A19 and A23 establish two strong directions:

\[
P\rightarrow \text{requirement surface}
\]

and:

\[
\text{canonical requirement conformance}\rightarrow P.
\]

That can be misunderstood as:

\[
P\equiv S.
\]

It does **not** mean that.

If P1–P6 and S1–S14 carried exactly the same information, maintaining both layers would add no architectural value.

The correct relationship is:

\[
\boxed{
\text{Principle invariant}
\quad\overset{\text{refinement}}{\Longrightarrow}\quad
\text{typed requirement/conformance obligation}
}
\]

and:

\[
\boxed{
\text{conforming requirement record}
\quad\overset{\text{projection}}{\Longrightarrow}\quad
\text{principle invariant}
}
\]

where the reverse projection deliberately forgets requirement-specific information.

---

## 2. What information exists at the principle layer

P1–P6 are the compact operational invariant basis.

A principle identifies **what semantic property must not be lost**, independently of where in the lifecycle it appears.

| Principle | Information carried at P layer |
|---|---|
| **P1** | evidence/proposition/decision fit + explicit residual |
| **P2** | bounded viable determination effort |
| **P3** | unresolved state must not become certainty/permission |
| **P4** | current decision-sufficient non-amplifying authority basis |
| **P5** | material-change requalification before reuse/action |
| **P6** | non-substituting composition / preserved dependency and compatibility |

The P layer deliberately abstracts away:

- which concrete domain object carries the invariant;
- which lifecycle operator is active;
- who owns the source fact;
- which handoff/interface is involved;
- which T# sufficiently-good condition applies;
- which KPI/evidence must be recorded;
- which historical/accountability record must survive;
- which privacy or human-capacity obligation is activated.

That loss of detail is intentional. It is what makes P1–P6 suitable for:

- ablation;
- independence testing;
- minimal-invariant reasoning;
- cross-scenario comparison;
- compact formalization.

---

## 3. What the requirement layer adds

The canonical requirement layer takes one or more P invariants and binds them to a concrete decision-boundary ontology and lifecycle position.

A requirement-conformance record for one scope can be represented abstractly as:

\[
R_\sigma=
\langle
\sigma,
o,
\lambda,
Owner,
P\text{-signature},
T,
Evidence,
KPI,
Disposition
\rangle.
\]

Where:

- \(\sigma\) = material subject–proposition–decision boundary;
- \(o\) = typed object such as authority, identity, policy, human capacity, evidence, commitment or history;
- \(\lambda\) = lifecycle operator such as QUALIFY, HANDOFF, DELEGATE, COMPOSE, SHIFT, INTERVENE, REPAIR or ASSESS;
- \(Owner\) = legitimate owner/source of the underlying fact or action;
- \(P\)-signature = one or more preserved P invariants;
- \(T\) = applicable sufficiently-good conditions T1–T4;
- \(Evidence/KPI\) = observable proof/falsification instrumentation;
- \(Disposition\) = what the route is entitled to conclude/do for that declared scope.

This is strictly richer than a P label.

---

## 4. Explicit information added by S1–S14/T1–T4

### 4.1 Typed object information

The P layer does not distinguish, by itself, whether the invariant is being applied to:

- authority;
- preference;
- identity/representation;
- human capacity;
- evidence;
- policy/objective;
- commitment;
- history;
- frame/context;
- unresolved state;
- multi-principal composition.

A21 makes these typed objects explicit.

### 4.2 Lifecycle/operator information

The P layer does not specify whether the invariant is exercised during:

- qualification;
- escalation;
- containment;
- handoff;
- binding;
- delegation;
- composition;
- temporal shift/reuse;
- intervention;
- repair;
- assessment.

The requirement grammar does.

### 4.3 Ownership and non-ownership information

Requirements state where the underlying fact/action is externally owned.

Examples:

- S1 does not grant authority;
- S6 does not own identity/trust transport/privacy permission;
- S7 does not infer identity from output similarity;
- S9 does not set a universal hierarchy;
- S10 does not own cancellation/commitment authority;
- S12 does not own the historical record/repair process.

This ownership boundary is operationally important and is not contained in the bare Pi invariant.

### 4.4 Conformance-condition information

T1–T4 add:

- material-break detectability;
- owner-preserving handoff;
- authorized bounded response;
- timely/viable/minimum-sufficient requalification.

A principle may state the invariant; the T layer states when evidence is sufficient to claim that the requirement has actually been met for the current \(\sigma\).

### 4.5 Observable/falsifiable evidence

The canonical requirement route adds:

- named evidence fields;
- branch oracles;
- KPI numerators/denominators;
- response deadline;
- remaining response margin;
- human/compute burden;
- false continuation/containment;
- handoff integrity;
- correlated-evidence errors;
- re-entry precision/recall;
- authorized-response compliance.

The principle layer is intentionally not an instrumentation protocol.

### 4.6 Historical and accountability information

S12/S13 retain:

- reconstructable identity/role/grant/policy/evidence/context;
- original authority history;
- later intervention history;
- future repair without rewriting historical state.

P4/P5/P6 constrain the invariants involved, but do not by themselves define this historical record architecture.

### 4.7 Privacy and disclosure information

S6 adds a bounded-disclosure requirement: enough authority/status must be verifiable without exposing unnecessary private/internal state.

P1/P4/P6 can explain why qualification must survive; they do not specify the privacy-preserving disclosure obligation.

---

## 5. Formal projection from requirements to principles

Define the forgetful projection:

\[
\pi(R_\sigma)=Sig_P(R_\sigma)
\]

where \(Sig_P\subseteq\{P1,\ldots,P6\}\) is the set of P invariants preserved by that requirement record.

The projection discards:

\[
\{\sigma,o,\lambda,Owner,T,Evidence,KPI,Disposition\}.
\]

A23 proves that for a canonically conforming route the projected P invariant(s) hold.

Thus:

\[
Conf(R_\sigma)\Rightarrow \bigwedge_{P_i\in\pi(R_\sigma)}P_i.
\]

---

## 6. Non-injectivity theorem — requirements contain additional information

### Theorem

\(\pi\) is not injective.

### Witness 1 — S6 versus S9

Both can carry the principle signature:

\[
\{P1,P4,P6\}.
\]

But:

- **S6** is a **HANDOFF** obligation: qualified trust/status crosses participant boundaries with bounded disclosure.
- **S9** is a **COMPOSE** obligation: several principal/domain determinations are combined without substitution, hidden correlation or false hierarchy.

Therefore:

\[
\pi(S6)=\pi(S9)
\]

can hold while:

\[
S6\neq S9.
\]

The P signature cannot reconstruct whether the original obligation was handoff or composition.

### Witness 2 — S11 versus S13

Both may involve:

\[
\{P4,P5,P6\}.
\]

But:

- **S11** preserves policy/objective owner/version/scope and cross-domain coupling;
- **S13** preserves the distinction between original authority history and later intervention history.

Again the same principle signature does not recover the requirement identity.

### Witness 3 — S1 versus S8

Both are P4-dominant authority surfaces.

But:

- **S1** asks whether the grant is legitimate/current/applicable;
- **S8** asks whether delegation preserves scope and does not amplify authority.

Knowing “P4 holds” does not tell the assessor which lifecycle authority obligation has been satisfied.

Therefore \(\pi\) is many-to-one. ∎

---

## 7. Consequence: no information equivalence

Because \(\pi\) is many-to-one, there is no inverse function:

\[
\pi^{-1}:Sig_P\rightarrow R
\]

that uniquely reconstructs the original requirement/conformance record.

Therefore:

\[
P1\text{–}P6
\not\equiv_{\text{information}}
S1\text{–}S14/T1\text{–}T4.
\]

The reverse sufficiency theorem A23 does not change this.

A23 says:

\[
Conf(S/T)\Rightarrow P.
\]

It does **not** say:

\[
P\Rightarrow Conf(S/T)
\]

nor:

\[
P=S/T.
\]

---

## 8. Why the two layers are both necessary

### P layer — invariant compression

Use P1–P6 when the question is:

- what semantic invariant failed?
- can it be removed?
- is it independent of the other five?
- does an alternative reconstruct the same invariant?
- what is the compact cross-scenario failure class?

### S/T layer — specification refinement

Use S1–S14/T1–T4 when the question is:

- where does the invariant apply?
- to which object/owner/decision?
- at what lifecycle transition?
- what must cross the interface?
- what evidence demonstrates conformance?
- what deadline/capacity/privacy/history obligation applies?
- who may act and what is outside EA ownership?

Neither layer replaces the other.

---

## 9. Information-growth view

The relationship can be represented as:

\[
P_i
+
\text{typed object}
+
\text{lifecycle operator}
+
\text{ownership}
+
\text{decision boundary}
+
\text{conformance conditions}
+
\text{evidence protocol}
\Longrightarrow
S/T\text{ route}.
\]

More generally:

\[
R_\sigma
=
Refine(P,\sigma,o,\lambda,Owner,T,Evidence,KPI).
\]

Projecting back:

\[
\pi(R_\sigma)=P\text{-signature}
\]

is valid but lossy.

This is the precise sense in which the requirement layer **aggregates information** rather than simply reformulating the principles.

---

## 10. Relation to bidirectional proof

The complete relationship is now:

### Forward — A19

\[
P_i\rightarrow\text{real requirement surface}
\]

with falsifiable semantic anchors.

### Reverse — A23

\[
Conf(S/T)\rightarrow P_i.
\]

### Information structure — A24

\[
Conf(S/T)\rightarrow P
\]

is a **forgetful projection**, not an equivalence.

Therefore the correct notation is:

\[
\boxed{
P1\text{–}P6
\;\underset{\text{conformance sufficiency}}{\overset{\text{semantic refinement}}{\rightleftarrows}}\;
S1\text{–}S14/T1\text{–}T4
}
\]

with:

\[
Info(S/T) > Info(P)
\]

in the specific structural sense established above: requirement identity contains typed object/lifecycle/ownership/conformance data that is not recoverable from the P signature alone.

This “\(>\)” is an information-content relation in the declared representation, not a Shannon-entropy measurement.

---

## 11. Claim boundary

A24 does not claim that every requirement is more important than every principle or that requirements are a different theory.

It establishes only that:

1. P1–P6 are the compact invariant basis;
2. S1–S14/T1–T4 refine those invariants into typed, observable, owner-aware conformance obligations;
3. canonical conformance implies the applicable P invariant;
4. the P signature does not uniquely reconstruct the richer requirement record;
5. therefore the two layers are both necessary and are not redundant.
