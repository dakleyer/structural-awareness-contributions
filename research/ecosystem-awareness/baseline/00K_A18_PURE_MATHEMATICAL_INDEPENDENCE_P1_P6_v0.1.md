# 00K-A18 — Pure Mathematical Independence of P1–P6 — v0.1

| | |
|---|---|
| **Parent** | [00K — Six-Principle Sufficiency & Adversarial Ablation Test](./00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md) |
| **Related fixture-grounded proof** | [00K-A16 — Formal Relative Independence Proof](./00K_A16_FORMAL_RELATIVE_INDEPENDENCE_PROOF_P1_P6_v0.1.md) |
| **Status** | **Formal independence sketch / sanity check; superseded for the stronger shared-substrate claim by [A20](./00K_A20_SHARED_SUBSTRATE_MATHEMATICAL_INDEPENDENCE_P1_P6_v0.1.md)** |
| **Date** | 25 September 2026 |
| **Premises used** | abstract semantic definitions of P1–P6 only |
| **Premises not used** | 00E–00J scenarios, pytest results, repair searches, GitHub Actions, empirical/product behaviour |

> **Result.** Under the deliberately simple Boolean vocabulary defined below, the six formulas are logically independent. This result is correct but intentionally modest: several principle contents are represented by separate unconstrained coordinates, so the independence is partly facilitated by the representation. It is retained as a formal sanity check, not as the strongest architectural independence claim. See [A20](./00K_A20_SHARED_SUBSTRATE_MATHEMATICAL_INDEPENDENCE_P1_P6_v0.1.md) for the shared-substrate proof.

---

## 1. Purpose

The executable 00K campaign asks an operational question:

> if one principle is removed from a concrete decision scenario, can the remaining controls repair the failure without reconstructing that principle?

That is useful evidence, but it is not the same question as logical independence.

This document asks the purely mathematical question:

> does any one of the six formal principle predicates follow logically from the conjunction of the other five?

The answer is **no** in the abstract base semantics defined here.

---

## 2. Abstract state space

Let the Boolean domain be:

\[
\mathbb B=\{0,1\}.
\]

Define the abstract state space:

\[
\Omega=\mathbb B^8.
\]

A state is an 8-tuple:

\[
\omega=(e,r,b,u,x,a,c,d)
\]

with the following semantic coordinates:

| Coordinate | Meaning |
|---|---|
| \(e\) | available evidence is sufficient for the actual proposition/decision |
| \(r\) | material residual uncertainty is explicit rather than silently erased |
| \(b\) | unresolved determination has a finite viable bound/fallback |
| \(u\) | a material unresolved state is present |
| \(x\) | the action is executed / promoted to operational closure |
| \(a\) | current authority is sufficient, verifiable and non-amplifying for the action |
| \(c\) | the material decision basis is current, or action-time requalification has occurred |
| \(d\) | composition preserves material dependence/compatibility and avoids silent substitution |

No scenario, implementation, technology or test result is assumed. These coordinates are the primitive semantic vocabulary of the proof.

---

## 3. Formal definitions of P1–P6

Define six predicates \(P_i:\Omega\to\mathbb B\).

### P1 — decision-sufficient evidence with explicit residual

\[
P_1(\omega)= e\land r.
\]

### P2 — bounded viable determination

\[
P_2(\omega)= b.
\]

### P3 — no promotion of unresolved material state

\[
P_3(\omega)= \neg(u\land x).
\]

Equivalently:

\[
P_3(\omega)=u\rightarrow\neg x.
\]

### P4 — sufficient non-amplifying authority for execution

\[
P_4(\omega)= x\rightarrow a.
\]

### P5 — current material basis or requalification before execution

\[
P_5(\omega)= x\rightarrow c.
\]

### P6 — non-substituting composition for execution

\[
P_6(\omega)= x\rightarrow d.
\]

Let:

\[
T=\{P_1,P_2,P_3,P_4,P_5,P_6\}.
\]

---

## 4. Definition of logical independence

The family \(T\) is independent over \(\Omega\) iff, for every \(i\in\{1,\ldots,6\}\),

\[
T\setminus\{P_i\}\not\models_{\Omega}P_i.
\]

By the definition of semantic entailment, this is equivalent to:

\[
\forall i\;\exists\omega_i\in\Omega:
\left(\bigwedge_{j\neq i}P_j(\omega_i)\right)
\land
\neg P_i(\omega_i).
\]

So a complete proof requires six countermodels.

---

## 5. Six purely mathematical countermodels

Use the following states, written in coordinate order:

\[
(e,r,b,u,x,a,c,d).
\]

### Countermodel for P1

\[
\omega_1=(0,1,1,0,1,1,1,1).
\]

Then:

- \(P_1(\omega_1)=0\land1=0\);
- \(P_2(\omega_1)=1\);
- \(P_3(\omega_1)=\neg(0\land1)=1\);
- \(P_4(\omega_1)=1\rightarrow1=1\);
- \(P_5(\omega_1)=1\rightarrow1=1\);
- \(P_6(\omega_1)=1\rightarrow1=1\).

Therefore:

\[
P_2\land P_3\land P_4\land P_5\land P_6
\not\models_{\Omega} P_1.
\]

P1 is independent of the other five.

---

### Countermodel for P2

\[
\omega_2=(1,1,0,0,1,1,1,1).
\]

Then \(P_2(\omega_2)=0\), while every other \(P_j(\omega_2)=1\).

Therefore:

\[
P_1\land P_3\land P_4\land P_5\land P_6
\not\models_{\Omega} P_2.
\]

P2 is independent of the other five.

---

### Countermodel for P3

\[
\omega_3=(1,1,1,1,1,1,1,1).
\]

Because \(u=1\) and \(x=1\),

\[
P_3(\omega_3)=\neg(1\land1)=0.
\]

But:

\[
P_1(\omega_3)=P_2(\omega_3)=P_4(\omega_3)=P_5(\omega_3)=P_6(\omega_3)=1.
\]

Therefore:

\[
P_1\land P_2\land P_4\land P_5\land P_6
\not\models_{\Omega} P_3.
\]

P3 is independent of the other five.

---

### Countermodel for P4

\[
\omega_4=(1,1,1,0,1,0,1,1).
\]

Since \(x=1\) and \(a=0\),

\[
P_4(\omega_4)=1\rightarrow0=0.
\]

All other principles evaluate to 1.

Therefore:

\[
P_1\land P_2\land P_3\land P_5\land P_6
\not\models_{\Omega} P_4.
\]

P4 is independent of the other five.

---

### Countermodel for P5

\[
\omega_5=(1,1,1,0,1,1,0,1).
\]

Since \(x=1\) and \(c=0\),

\[
P_5(\omega_5)=1\rightarrow0=0.
\]

All other principles evaluate to 1.

Therefore:

\[
P_1\land P_2\land P_3\land P_4\land P_6
\not\models_{\Omega} P_5.
\]

P5 is independent of the other five.

---

### Countermodel for P6

\[
\omega_6=(1,1,1,0,1,1,1,0).
\]

Since \(x=1\) and \(d=0\),

\[
P_6(\omega_6)=1\rightarrow0=0.
\]

All other principles evaluate to 1.

Therefore:

\[
P_1\land P_2\land P_3\land P_4\land P_5
\not\models_{\Omega} P_6.
\]

P6 is independent of the other five.

---

## 6. Independence theorem

### Theorem

The family

\[
T=\{P_1,P_2,P_3,P_4,P_5,P_6\}
\]

is logically independent over \(\Omega\).

### Proof

For each \(i\in\{1,\ldots,6\}\), Section 5 explicitly constructs a state \(\omega_i\in\Omega\) such that:

\[
\omega_i\models P_j\quad\text{for every }j\neq i
\]

and:

\[
\omega_i\not\models P_i.
\]

Hence, for every \(i\),

\[
T\setminus\{P_i\}\not\models_{\Omega}P_i.
\]

Therefore \(T\) is logically independent over \(\Omega\). ∎

---

## 7. Irredundancy corollary

For each principle define its satisfaction set:

\[
S_i=\{\omega\in\Omega:P_i(\omega)=1\}.
\]

The full admissible set is:

\[
S=\bigcap_{i=1}^{6}S_i.
\]

For every \(i\), countermodel \(\omega_i\) belongs to every \(S_j\) with \(j\neq i\), but not to \(S_i\). Therefore:

\[
\bigcap_{j=1}^{6}S_j
\subsetneq
\bigcap_{j\neq i}S_j.
\]

Thus deleting any one principle strictly enlarges the state set admitted by the theory.

So P1–P6 are not merely independent; the six-principle conjunction is **irredundant** in this semantic basis.

---

## 8. Truth-table form

The countermodels produce the identity-complement pattern:

| State | P1 | P2 | P3 | P4 | P5 | P6 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| \(\omega_1\) | **0** | 1 | 1 | 1 | 1 | 1 |
| \(\omega_2\) | 1 | **0** | 1 | 1 | 1 | 1 |
| \(\omega_3\) | 1 | 1 | **0** | 1 | 1 | 1 |
| \(\omega_4\) | 1 | 1 | 1 | **0** | 1 | 1 |
| \(\omega_5\) | 1 | 1 | 1 | 1 | **0** | 1 |
| \(\omega_6\) | 1 | 1 | 1 | 1 | 1 | **0** |

This table is not experimental data. It is the evaluation of the six formulas on six explicitly constructed mathematical states.

---

## 9. Why this proof is independent of the tests

No step above uses:

- 00E, 00F, 00G, 00H, 00I or 00J;
- any Python harness;
- any pytest result;
- the 379-test campaign;
- a GitHub Actions run;
- any vendor or product behaviour;
- any empirical observation.

The only inputs are:

1. the abstract semantic coordinates \(e,r,b,u,x,a,c,d\); and
2. the formal definitions of P1–P6 over those coordinates.

Therefore the result is **mathematical rather than test-derived**, but it should be read as a clean formal sketch complementary to the fixtures, not as a replacement for their stronger operational falsification burden.

The executable campaign has a different role: it asks whether concrete operational scenarios can be faithfully mapped into these semantic dimensions and whether plausible engineering substitutes escape the corresponding invariant.

---

## 10. Exact boundary of the theorem

This theorem proves:

> **Given the abstract semantic basis above, none of P1–P6 is logically implied by the conjunction of the other five.**

It does not prove that the chosen primitive coordinates are the only possible semantic basis.

In particular, if a stronger background theory \(B\) is later imposed that logically couples coordinates — for example a new axiom of the form \(a\rightarrow c\), or a definitional identification of two coordinates — then independence must be checked relative to \(B\):

\[
B\cup(T\setminus\{P_i\})\not\models P_i.
\]

This is the normal boundary of model-theoretic independence.

The current theorem is therefore stronger than fixture-relative A16 in one respect — it does not rely on the scenario corpus — and more abstract in another — it proves independence of the semantic principles, not empirical adequacy of the semantic vocabulary.

---

## 11. Relationship to A16 and the executable tests

The three evidence layers should remain distinct:

| Layer | Question | Evidence |
|---|---|---|
| **A18 — pure mathematics** | Does any Pi logically follow from the other five under the abstract semantic definitions? | six abstract countermodels; no tests |
| **A16 — corpus-grounded formalization** | Do corrected 00K scenario witnesses instantiate the same independence structure? | six fixture-derived semantic countermodels |
| **A1–A6 / A15 / CI** | Do executable scenario abstractions survive leave-one-principle-out repair searches? | deterministic symbolic tests and falsifiers |

A18 is the independent mathematical proof.

A16 is the bridge between that mathematics and the scenario corpus.

The executable tests are operational evidence, not premises of A18.
