# 00K-A16 — Formal Relative Independence Proof of P1–P6 — v0.1

| | |
|---|---|
| **Parent** | [00K — Six-Principle Sufficiency & Adversarial Ablation Test](./00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md) |
| **Executable testbook** | [00K-A15](./00K_A15_COMPLETE_SIX_PRINCIPLE_ABLATION_TESTBOOK_v0.1.md) |
| **Proof certificate** | [fixtures/00K-FORMAL](./fixtures/00K-FORMAL/README.md) |
| **Formal sketch** | [00K-A18](./00K_A18_PURE_MATHEMATICAL_INDEPENDENCE_P1_P6_v0.1.md) |
| **Preferred pure mathematical proof** | [00K-A20](./00K_A20_SHARED_SUBSTRATE_MATHEMATICAL_INDEPENDENCE_P1_P6_v0.1.md) |
| **Status** | **Formal relative-independence proof for the current operational P1–P6 definitions** |
| **Date** | 25 September 2026 |
| **Boundary** | model-relative logical independence; not universal minimality or statistical independence |

> **Scope note.** This A16 proof is corpus-grounded: its witness class is induced by the corrected 00K fixtures. For the preferred proof that uses no scenario/test premise and forces the principles onto one shared provenance/scope/time substrate, see [00K-A20 — Shared-Substrate Mathematical Independence](./00K_A20_SHARED_SUBSTRATE_MATHEMATICAL_INDEPENDENCE_P1_P6_v0.1.md). [A18](./00K_A18_PURE_MATHEMATICAL_INDEPENDENCE_P1_P6_v0.1.md) is retained as the earlier lightweight formal sketch.

> **Result.** Under the current 00K operational semantics, P1–P6 are logically independent as an axiom family: for every Pi, there exists a corrected fixture-derived witness model that satisfies the other five principles and violates Pi. Consequently, no Pi is derivable from the conjunction of the other five inside the declared model class.

---

## 1. What “independent” means mathematically

This document uses **logical / model-theoretic independence**, not statistical independence and not vector-space linear independence.

Let:

~~~text
T = {P1, P2, P3, P4, P5, P6}
~~~

Let K be the declared class of finite decision traces induced by the corrected 00K fixture semantics.

The family T is independent over K iff:

~~~text
for every i in {1,...,6}:
    T \ {Pi}  does not semantically entail  Pi   over K
~~~

Using standard model notation:

~~~text
∀ i ∈ {1,...,6}:  T \ {Pi} ⊭K Pi
~~~

By the definition of semantic entailment, this is equivalent to the existence of six countermodels:

~~~text
∀ i ∈ {1,...,6}, ∃ Mi ∈ K such that:
    Mi ⊨ Pj   for every j ≠ i
    Mi ⊭ Pi
~~~

So the proof obligation is concrete: produce one valid countermodel for each omitted principle.

This is stronger than saying that every principle appears in a requirements matrix. It demonstrates non-derivability from the other five under the declared semantics.

---

## 2. Formal predicates

For a finite decision trace x, define the following predicates.

### P1 — decision-sufficient evidence

P1(x) = 1 iff the evidence used by the receiver is sufficient for the **actual proposition and decision** being made, and material residual uncertainty remains explicit. A valid record for a narrower proposition is not silently promoted.

### P2 — bounded viable determination

P2(x) = 1 iff unresolved determination effort is decision-relevant, finite, bounded by available capacity / useful response horizon, and has an explicit bounded fallback.

### P3 — no promotion of unresolved state

P3(x) = 1 iff known unresolved material state is not converted into permission, PASS or certainty-equivalent operational closure.

### P4 — decision-sufficient authority basis

P4 uses the refined formulation produced by the serious 00H ablation.

P4(x) = 1 iff an executed relying decision has a current, receiver-verifiable authority qualification sufficient for the composed action and its non-amplification boundary.

Full historical delegation lineage is **not** part of the minimum predicate. Lineage, scoped capability, legitimate maker-checker and owner-side PDP attestation are alternative realizations.

### P5 — action-time material-basis validity

P5(x) = 1 iff a previously qualified determination is used only while its declared material decision basis remains current, or a material mismatch causes requalification before actuation.

### P6 — non-substituting composition

P6(x) = 1 iff local/repeated determinations are composed without silently promoting dependent, incompatible or substitutive state into ecosystem truth; decision-material dependence / compatibility is retained or inferred.

---

## 3. Abstraction from executable fixtures to formal witnesses

The mathematical proof and the Python ablation tests are related but not identical.

Let α be the semantic abstraction from a concrete corrected fixture execution to the six predicate values:

~~~text
α(trace) = (P1(trace), P2(trace), P3(trace), P4(trace), P5(trace), P6(trace))
~~~

The executable harnesses establish the branch behaviour and remove known fixture confounds. A16 uses one reduced witness from each corrected fixture family.

The machine-checkable certificate does **not** store the six truth values directly. It constructs each witness from lower-level semantic fields — evidence/decision fit, stopping horizon, unresolved-state disposition, authority coverage, material-basis currentness and composition dependence — and evaluates P1–P6 from those fields.

That distinction matters: the certificate checks a semantic countermodel construction rather than merely asserting a six-bit row.

---

## 4. Six countermodels

| Countermodel | Fixture origin | P1 | P2 | P3 | P4 | P5 | P6 | Isolated failure |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| M1 | 00J corrected matched-semantic negative | **0** | 1 | 1 | 1 | 1 | 1 | valid evidence supports the wrong proposition for the actual rights-enforcement decision |
| M2 | 00E unresolved-search branch | 1 | **0** | 1 | 1 | 1 | 1 | uncertainty remains explicit but determination effort has no finite viable stop inside the useful horizon |
| M3 | 00F corrected matched conflict | 1 | 1 | **0** | 1 | 1 | 1 | conflict is visible/current/bounded yet unresolved material state is promoted to execution |
| M4 | 00H unauthorized common-root campaign | 1 | 1 | 1 | **0** | 1 | 1 | leaves are valid and campaign visible, but composed-action authority is insufficient/amplified |
| M5 | 00I semantic-TOCTOU stale branch | 1 | 1 | 1 | 1 | **0** | 1 | once-valid action is reused after its material decision basis changes |
| M6 | 00G matched hidden-common-root branch | 1 | 1 | 1 | 1 | 1 | **0** | local claims are valid/current but dependent evidence is counted as independent ecosystem support |

Equivalently, the witness matrix is:

~~~text
       P1 P2 P3 P4 P5 P6
M1      0  1  1  1  1  1
M2      1  0  1  1  1  1
M3      1  1  0  1  1  1
M4      1  1  1  0  1  1
M5      1  1  1  1  0  1
M6      1  1  1  1  1  0
~~~

Each row is a countermodel to exactly one candidate entailment.

---

## 5. Independence theorem

### Theorem

The operational principle family T = {P1,...,P6} is logically independent over the declared 00K witness class K.

### Proof

Choose any i ∈ {1,...,6}.

By the countermodel construction above, Mi belongs to K and satisfies every Pj with j ≠ i, while Mi does not satisfy Pi.

Therefore Mi is a model of T \ {Pi} and is not a model of Pi.

Hence:

~~~text
T \ {Pi} ⊭K Pi
~~~

Because i was arbitrary, this holds for every principle:

~~~text
∀ i ∈ {1,...,6}:  T \ {Pi} ⊭K Pi
~~~

Therefore T is logically independent over K. QED.

---

## 6. Irredundancy corollary

Let ModK(T) denote the traces in K satisfying all six principles.

For every i, Mi satisfies T \ {Pi} but not T. Therefore:

~~~text
ModK(T) ⊊ ModK(T \ {Pi})
~~~

Deleting any one principle strictly enlarges the allowed model class.

So the current six-principle set is **irredundant under the formalized semantics**.

Irredundancy is the exact mathematical conclusion justified here. It is stronger than “all six were useful in examples” and weaker than “these are universally the only six possible principles.”

---

## 7. Relation to the executable ablation tests

The countermodels are not arbitrary Boolean rows invented after the fact. They are reduced semantic witnesses extracted from corrected executable fixtures:

- M1 → [P1 / 00J matched-semantic isolation](./fixtures/00K-A1-P1-00J/README.md)
- M2 → [P2 / 00E matched-prefix isolation](./fixtures/00K-A2-P2-00E/README.md)
- M3 → [P3 / 00F matched-conflict isolation](./fixtures/00K-A3-P3-00F/README.md)
- M4 → [P4 / 00H matched U/G/I/NM](./fixtures/00K-A4-P4-00H/README.md)
- M5 → [P5 / 00I exhaustive material-basis isolation](./fixtures/00K-A5-P5-00I/README.md)
- M6 → [P6 / 00G matched transitive-dependency isolation](./fixtures/00K-A6-P6-00G/README.md)

The [proof certificate](./fixtures/00K-FORMAL/formal_independence_certificate.py) evaluates the six witnesses and verifies the countermodel criterion mechanically.

The certificate is intentionally **not counted as another ablation test**. It checks the formal relation among the principles; it does not add a seventh experimental fixture.

---

## 8. Projection-indistinguishability lemma

Several corrected fixtures instantiate the same elementary separation result.

### Lemma

Let X be a state space, let π: X → Z be the observable projection available to a candidate repair, and let O: X → A be the correct branch oracle.

If there are states x− and x+ such that:

~~~text
π(x−) = π(x+)
O(x−) ≠ O(x+)
~~~

then no deterministic policy f: Z → A can be correct on both states.

### Proof

Because the observable projections are equal:

~~~text
f(π(x−)) = f(π(x+))
~~~

But the correct oracle outputs differ. One common policy output cannot equal two different required outputs. Contradiction. QED.

### Instantiations

- **P1:** corrected branches match issuer/source/type/freshness while evidence semantics differ.
- **P4:** U/G match on materiality, campaign, leaf validity, volume, amount, risk and timing while current composed-action authority differs.
- **P5:** stale/fresh queued actions can match on token validity, scope and elapsed time while current material basis differs.
- **P6:** matched branches can have identical agent/org/source-ID/confidence/time/content surfaces while transitive material roots differ.

A successful repair must add or infer a discriminator outside the blind projection. The 00K classification question is then whether that discriminator is a TRUE SUBSTITUTE or an operational reconstruction of the removed principle.

The [P5 blind-signature proof supplement](./fixtures/00K-FORMAL/p5-blind-signature/README.md) is an instance of this lemma: STALE and FRESH are intentionally equal on the P5-blind surface and have opposite correct dispositions. The current canonical A11 grid goes further by testing all 16 subsets of the declared material basis, so the 18-test supplement is retained as a compact proof illustration and is not added to the canonical campaign count.

---

## 9. P2 temporal independence / liveness argument

P2 has a temporal form rather than a simple two-state projection.

Consider two histories with the same unresolved prefix:

~~~text
h−H = (u, u, ..., u)
h+H = (u, u, ..., u, r)
~~~

The first remains unresolved through the useful horizon. The second resolves at the last still-useful step.

A policy that guarantees finite termination on indefinitely unresolved histories must eventually stop after some finite unresolved prefix.

Choose a positive history whose resolving observation occurs at or after that stopping boundary. The policy then terminates before observing a resolution that was still reachable inside the allowed family.

Conversely, a policy that refuses every finite stopping boundary cannot guarantee bounded termination on the indefinitely unresolved history.

Therefore a branch-correct policy over this family requires a finite viability / horizon / fallback relation or an operational equivalent.

This is why the P2 repair family repeatedly converges on deadlines, budgets, patience windows, bounded probes or externally enforced schedulers.

---

## 10. Proof dependency and evidentiary boundary

The complete argument has three layers:

1. **Executable layer:** corrected 00E–00J fixtures demonstrate concrete branch behaviour, positive controls, confound corrections and repair searches.
2. **Semantic abstraction layer:** each corrected witness is mapped to P1–P6 by explicit predicate definitions.
3. **Deductive layer:** six one-principle countermodels establish non-entailment and irredundancy.

The formal theorem depends on the declared abstraction and witness class. If a witness is shown not to satisfy one of the other five principles, or a predicate definition changes materially, the proof must be rerun/revised.

This is a feature, not a loophole: the proof is falsifiable at the abstraction boundary.

---

## 11. What is proved, and what is not

### Proved relative to the declared semantics

1. **Logical independence:** no current Pi follows from the other five.
2. **Irredundancy:** removing any one principle strictly enlarges the allowed formal model class.
3. **Finite countermodels exist:** one corrected fixture-derived witness for every omitted principle.
4. **Several branch separations satisfy an elementary indistinguishability theorem.**

### Not proved

This document does **not** prove:

- statistical independence among measured variables;
- universal necessity for every conceivable agentic architecture;
- that no alternative basis of five differently formulated principles can represent the same semantic space;
- global completeness of P1–P6 for every future failure class;
- mathematical uniqueness of the six principles;
- live product failure; or
- Ecosystem Positioning superiority.

A different axiom basis may be logically equivalent to P1–P6. Independence means **none of these six current axioms is derivable from the other five**, not that no other compact basis exists.

---

## 12. Stronger future proof targets

The next formal targets are distinct from this independence theorem:

1. **basis minimality under a declared equivalence relation** — prove no smaller axiom basis represents the same allowed trace language;
2. **completeness relative to a formally bounded failure language** — every prohibited trace violates at least one principle;
3. **soundness** — every trace satisfying P1–P6 satisfies the formally specified safety contract;
4. **temporal-logic encoding** in LTL/TLA+/Alloy/SMT for model checking; and
5. **machine-checked theorem proof** in Lean/Coq/Isabelle if the semantics stabilize enough to justify the cost.

The present result is the prerequisite: a countermodel-based independence theorem tied directly to the corrected executable ablation corpus.
