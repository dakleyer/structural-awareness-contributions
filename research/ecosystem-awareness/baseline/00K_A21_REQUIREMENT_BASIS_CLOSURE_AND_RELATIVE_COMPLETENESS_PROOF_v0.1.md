# 00K-A21 — Requirement Basis Closure & Relative Completeness Proof — v0.1

| | |
|---|---|
| **Foundational syntax** | [02B — Foundational Syntax Closure](./02B_FOUNDATIONAL_SYNTAX_CLOSURE_AND_P1_P6_NORMAL_FORM_PROOF_v0.1.md) |
| **Principle semantics** | [02A](./02A_FOUNDATION_TO_OPERATIONAL_PRINCIPLE_DERIVATION_PROOF_v0.1.md) |
| **Canonical requirements** | [00 — S1–S14](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) |
| **Traceability proof** | [00K-A19](./00K_A19_PRINCIPLE_REQUIREMENT_TRACEABILITY_AND_CONSERVATION_PROOF_v0.1.md) |
| **Conformance→principle sufficiency** | [00K-A23](./00K_A23_CANONICAL_REQUIREMENT_CONFORMANCE_SUFFICIENCY_P1_P6_v0.1.md) |
| **Information gain / non-equivalence** | [00K-A24](./00K_A24_PRINCIPLE_REQUIREMENT_INFORMATION_GAIN_AND_NON_EQUIVALENCE_v0.1.md) |
| **Post-freeze adversarial review** | [Requirements vNext Review & Delta](./00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) |
| **Status** | relative requirement-basis completeness proof; no modification of frozen S1–S14 semantics |
| **Date** | 25 September 2026 |

> **Result.** Relative to the declared EA decision-frame language and lifecycle operators, S1–S14 form a generator-complete requirement basis: every admissible primitive obligation normalizes to one existing S requirement, and a compound obligation normalizes to a conjunction/specialization of existing S requirements. A legitimate S15 at the same abstraction level must therefore exhibit a new primitive object, lifecycle operator or invariant not expressible in the current language.

---

## 1. Why coverage is not enough

A19 proves that every current S1–S14 maps to P1–P6 and that every P has a direct requirements anchor.

That proves **coverage and non-vacuity**.

It does not by itself prove:

> there is no independent requirement missing from the taxonomy.

A21 addresses that stronger question by defining the admissible requirement language first and then asking whether S1–S14 generate it.

---

## 2. Decision-frame language LR

The canonical requirements already define the test unit as a material subject–proposition–decision boundary \(\sigma(d,t)\) with visible:

- subject / acting entity;
- proposition / decision basis;
- receiving decision;
- legitimate owner/principal;
- time/currentness;
- evidence boundary;
- materiality;
- authority;
- response deadline/horizon;
- available capacity;
- null/safe action.

A requirement in the current EA scope is therefore an obligation that constrains one or more of those fields while the decision moves through a bounded lifecycle.

### 2.1 Typed objects

Let the typed decision objects be:

\[
X=\{
authority,\ preference,\ identity,\ human,\ evidence,\ policy,
commitment,\ history,\ frame,\ unresolved,\ multi\_principal
\}.
\]

These are not inferred from the S# labels. They normalize decision-material objects already present in the pre-requirement Foundation / \(\sigma(d,t)\) / F1–F9 language. Their provenance is fixed below before the S1–S14 normalization is applied.

### 2.1A Independent provenance of typed objects

| Typed object | Pre-requirement source |
|---|---|
| **authority** | legitimate owner/applicable authority in \(\sigma(d,t)\); F1 authority/constraint boundary; Foundation rule that evidence/signalling does not create authority |
| **preference** | principal preference, hard limits and tolerated trade-offs consumed as decision-context facts |
| **identity** | subject/acting entity plus role/representation binding used at participant/interface boundaries |
| **human** | finite human attention, availability and determination/intervention capacity already present in the Foundation |
| **evidence** | subject–proposition–decision test unit and declared evidence/observation boundary |
| **policy** | externally owned mission/policy/objective constraints consumed by F1 and preserved through composition |
| **commitment** | receiving decision, null action, commitment/action boundary and action-time validity |
| **history** | retained state/provenance/outcome history used by F9 re-entry, challenge and repair |
| **frame** | \(W(d,t)\), operating context, regime assumptions and validity envelope |
| **unresolved** | Poles B/C/D, Type 0 state and Type-1/Type-2 management boundaries |
| **multi_principal** | F5 scope-indexed composition across participants/domains/dependencies |

Every object above can therefore be named before consulting the S# taxonomy.

### 2.2 Lifecycle operators

Let the requirement-level operators be:

\[
\Lambda=
\{
QUALIFY,\ ESCALATE,\ CONTAIN,\ HANDOFF,\ BIND,
DELEGATE,\ COMPOSE,\ SHIFT,\ INTERVENE,\ REPAIR,\ ASSESS
\}.
\]

Their meanings are the implementation-neutral lifecycle actions already present in the requirements:

- qualify a source/basis;
- escalate/revalidate under frame change;
- contain unresolved state;
- hand qualified state to another participant;
- bind identity/representation;
- delegate authority;
- compose several principals/domains;
- carry a decision across commitment/time change;
- intervene through human/technical action;
- reconstruct/challenge/repair historical state;
- assess evidence against the receiving decision.

### 2.2A Independent provenance of lifecycle operators

| Operator | Pre-requirement architectural source |
|---|---|
| **QUALIFY** | F1/F3/F4 decision, local-result and received-evidence qualification |
| **ESCALATE** | F7 targeted requalification / bounded escalation |
| **CONTAIN** | F6/F7 bounded posture and corrective response request |
| **HANDOFF** | F4/F8 qualified receive/signal boundary |
| **BIND** | identity/representation and subject binding at the relying boundary |
| **DELEGATE** | externally governed authority propagation / subdelegation relation |
| **COMPOSE** | F5 General Law of Epistemic Composition |
| **SHIFT** | F6/F9 continued validity and requalification across time/context change |
| **INTERVENE** | human/technical intervention as a response distinct from evidence creation |
| **REPAIR** | F9 feedback, re-entry and future-state correction |
| **ASSESS** | evidence/proposition/decision sufficiency assessment used by the receiving decision |

The lifecycle grammar therefore also exists independently of the S# labels.

### 2.3 Principle invariant

Every primitive requirement atom also preserves at least one P1–P6 invariant.

A primitive requirement atom is therefore:

\[
r=\langle x,\lambda,P_i\rangle
\]

for typed object \(x\in X\), lifecycle operator \(\lambda\in\Lambda\), and operational invariant \(P_i\).

As in 02B, \(L_R\) does not admit every arbitrary object/operator pair. The admitted atoms \(\Gamma_R\) are the lifecycle-meaningful combinations already present in the declared decision frame:

- QUALIFY: authority, preference, identity, evidence, policy;
- ESCALATE: frame, human, unresolved, commitment;
- CONTAIN: unresolved;
- HANDOFF: any qualified object crossing participants;
- BIND: identity/representation;
- DELEGATE: authority;
- COMPOSE: multi-principal/domain, authority, preference/policy, evidence;
- SHIFT: frame, commitment, policy, authority, evidence;
- INTERVENE: human, authority/history;
- REPAIR: history, evidence, authority;
- ASSESS: evidence/proposition/decision.

This grammar is derived from the declared decision lifecycle plus 02B; it is not generated from the names S1–S14. A candidate atom outside \(\Gamma_R\) is precisely a proposed language extension and therefore a possible falsifier of the closure theorem.

---

## 3. Canonical requirement normal forms

The non-vacuous primitive combinations normalize as follows.

| Requirement normal form | Typed object / operator pattern | Principle invariant(s) |
|---|---|---|
| **S1 Authority provenance/current applicability** | authority × QUALIFY/SHIFT | P4, P5 |
| **S2 Preference fidelity/reviewable basis** | preference × QUALIFY | P1, P6 |
| **S3 Regime/context/escalation/bounded escape** | frame × ESCALATE/SHIFT | P2, P3, P5 |
| **S4 Human-inclusive oversight authority/capacity** | human × INTERVENE/ESCALATE | P2, P3, P4 |
| **S5 Operational indeterminacy/containment** | unresolved × CONTAIN/ESCALATE/ACT-boundary | P1, P2, P3, P5 |
| **S6 Privacy-preserving trust handoff** | qualified object × HANDOFF | P1, P4, P6 |
| **S7 Identity/representation link** | identity × BIND/QUALIFY | P4, P6 |
| **S8 Bounded subdelegation/non-amplification** | authority × DELEGATE | P4, P6 |
| **S9 Multi-principal composition/non-substitution/conflict** | multi_principal × COMPOSE | P6, with P1/P4 where material |
| **S10 Commitment/material change** | commitment/basis × SHIFT/ESCALATE | P5, with P1/P2 |
| **S11 Policy/objective integrity across domains** | policy/preference × QUALIFY/COMPOSE/SHIFT | P6, P4, P5 |
| **S12 Accountability/challenge/repair** | history/evidence × REPAIR | P4, P5 |
| **S13 Authority history vs intervention history** | authority/history × INTERVENE/REPAIR | P4, P5, P6 |
| **S14 Evidence-to-decision assessment** | evidence × QUALIFY/ASSESS/SHIFT across all transitions | P1–P6 as applicable |

A concrete requirement may invoke several rows. That is composition of requirements, not evidence of a missing primitive generator. Conversely, several distinct requirements may share the same P signature while differing in typed object, lifecycle operator, owner and conformance evidence; [A24](./00K_A24_PRINCIPLE_REQUIREMENT_INFORMATION_GAIN_AND_NON_EQUIVALENCE_v0.1.md) proves that this projection is information-losing rather than a reformulation.

---

## 4. Requirement closure theorem

### Theorem

Let \(r=\langle x,\lambda,P_i\rangle\in\Gamma_R\) be any admitted primitive requirement atom well formed in \(L_R\).

Then \(r\) is covered by at least one clause of S1–S14.

### Proof by lifecycle operator

Take any admissible \(\lambda\).

1. **QUALIFY**  
   - authority → S1;  
   - preference → S2;  
   - identity → S7;  
   - evidence-to-decision → S14;
   - policy/objective basis → S11.

2. **ESCALATE**  
   - frame/context transition → S3;  
   - human capacity/intervention → S4;  
   - unresolved containment → S5;  
   - commitment-state escalation/revalidation → S10.

3. **CONTAIN**  
   - unresolved/incomplete/conflicting state → S5.

4. **HANDOFF**  
   - any qualified cross-participant state → S6;  
   - where identity/authority is material, S7/S1/S8 additionally apply.

5. **BIND**  
   - principal/organization/role/agent representation → S7.

6. **DELEGATE**  
   - authority/representation chain → S8, with S1 for origin/current applicability.

7. **COMPOSE**  
   - several principals/domains/evidence routes → S9;  
   - policy/objective coupling → S11;  
   - authority-bearing composition additionally invokes S1/S8.

8. **SHIFT**  
   - frame/regime transition → S3;  
   - commitment/material basis change → S10;  
   - policy/version change → S11;  
   - authority currentness → S1;  
   - evidence-basis freshness/continued sufficiency → S14 (and S5 where unresolved/stale state is material).

9. **INTERVENE**  
   - human effective oversight → S4;  
   - intervention against authority history → S13.

10. **REPAIR**  
    - reconstruct/challenge/repair historical basis → S12;  
    - authority versus later intervention history → S13.

11. **ASSESS**  
    - evidence/proposition/decision sufficiency and arbitration → S14.

Every lifecycle operator in \(L_R\) is therefore covered. Typed specializations invoke one or more of the same generators.

Hence every primitive requirement atom normalizes to S1–S14. ∎

---

## 5. Compound-requirement corollary

Let a proposed requirement \(R\) contain several primitive atoms:

\[
R=r_1\land r_2\land\cdots\land r_n.
\]

By the theorem, each \(r_k\) normalizes to at least one S requirement.

Therefore \(R\) normalizes to:

- one existing S clause;
- a specialization of an S clause; or
- a conjunction of several existing S clauses.

A new noun, interface object, algorithm or scenario does not create a new canonical requirement merely because its implementation is new.

---

## 6. Criterion for a legitimate S15

A candidate S15 is independent only if all four conditions hold:

1. **New primitive:** it identifies a typed object, lifecycle operator or invariant not expressible in \(L_R\).
2. **Non-reducibility:** its obligation cannot be written as a specialization or conjunction of S1–S14 clauses.
3. **Implementation neutrality:** it is not merely a preferred mechanism, payload, algorithm, component or interface.
4. **Decision relevance:** the new primitive changes what a sufficiently-good solution must preserve/test for the same \(\sigma(d,t)\).

If these conditions are met, A21 is falsified and the requirements taxonomy must expand.

If they are not met, the candidate belongs in clarification, architecture, interface, scenario or KPI material rather than as S15.

---

## 7. Independent adversarial corroboration from vNext review

The post-freeze Requirements vNext review supplies a useful negative search for missing generators.

Later developments stress substantially different surfaces:

- 00G false-context convergence;
- 00H aggregate opportunity versus authority;
- 00I semantic TOCTOU;
- 00J rights-provenance inversion;
- Regime Awareness deltas;
- MSCA control/repositioning;
- ACC admissibility/lineage;
- selective signalling;
- Objective-Conditioned Agentic Gradient;
- Ecosystem Cartography;
- effective-role drift.

The review repeatedly tests whether these developments require S15/T5/H7.

Current outcome:

- no new S15/T5/H7 is justified;
- several concepts are implementation/benchmark projections of existing requirements;
- the strongest residual candidates are wording/traceability clarifications such as effective-role drift and action-time binding;
- even those map to existing S7/S10/S12/S13/S14 or S10/S14 relations.

This empirical/adversarial review does not prove the theorem, but it is consistent with the formal closure result and provides a nontrivial search for counterexamples.

---

## 8. Relationship to principle sufficiency/minimality

A21 proves **requirement-basis closure relative to \(L_R\)**.

It is distinct from:

- A19 — semantic P↔S traceability;
- A15/A1–A6 — operational strongest-repair necessity tests;
- A16/A20 — logical independence/irredundancy of P1–P6;
- A23 — reverse specification-sufficiency: canonical requirement conformance entails the applicable P invariants.

Together they support the chain:

\[
01/02
\overset{02B}{\Longrightarrow}
P1\text{–}P6
\overset{A21}{\Longrightarrow}
S1\text{–}S14
\Longrightarrow
00E\text{–}00J
\Longrightarrow
A1\text{–}A6.
\]

---

## 9. Exact claim boundary

The defensible statement is:

> **S1–S14 are generator-complete for the declared EA decision-frame and lifecycle language. No independent fifteenth requirement has an uncovered primitive failure surface inside that language.**

This does not claim that no future research can enlarge the language itself.

A truly new requirement is possible, but only by showing a new primitive object/operator/invariant rather than renaming or recombining the existing ones.
