# 00K-A22 — Full-Cube Realizability & Boolean Diagnostic Minimality — v0.1

| | |
|---|---|
| **Parent** | [00K](./00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md) |
| **Shared-substrate independence** | [A20](./00K_A20_SHARED_SUBSTRATE_MATHEMATICAL_INDEPENDENCE_P1_P6_v0.1.md) |
| **Executable certificate** | [fixtures/00K-FORMAL/full-cube](./fixtures/00K-FORMAL/full-cube/README.md) |
| **Status** | full-cube realizability + information-theoretic lower bound for lossless Boolean diagnostic bases |
| **Date** | 25 September 2026 |
| **Boundary** | not unrestricted axiom-basis minimality; not minimality against non-Boolean or lossy encodings |

> **Result.** On the declared shared semantic substrate, all \(2^6=64\) truth signatures of P1–P6 are realizable. Therefore any family of Boolean predicates from which the full six-principle truth signature must be recoverable without loss requires at least six predicates. This proves **Boolean diagnostic minimality** of the six-coordinate principle basis. It does **not** prove that six separate axioms are necessary merely to recognize the single admissible class \(P_1\land\cdots\land P_6\).

---

## 1. Why this theorem is different from independence

A20 proves, for every \(i\),

\[
B\cup(T\setminus\{P_i\})\not\models P_i.
\]

That establishes logical independence and irredundancy of the current six predicates relative to the shared substrate.

A22 asks a different question:

> how many Boolean coordinates are required if a replacement representation must preserve the complete individual truth/failure state of all six principles?

Define the principle signature:

\[
\Sigma_P(M)=
(P_1(M),P_2(M),P_3(M),P_4(M),P_5(M),P_6(M)).
\]

A20 explicitly constructs seven signatures: \(111111\) and the six signatures with exactly one zero.

A22 constructs all 64.

---

## 2. Shared substrate

The executable certificate uses one decision object and one common record substrate:

- one action \(\alpha\);
- times \(t_0<t_1\);
- evidence records \(e_1,e_2\);
- one authority record \(g\);
- one material condition record \(m\);
- one unresolved inquiry issue \(u\);
- shared source/root/scope/validity/support relations;
- one determination process attached to the same decision;
- one composition relation over \(e_1,e_2\).

No principle truth value is stored as a field.

The six predicates are computed from lower-level relations.

### P1

Whether every asserted proposition is supported for the actual receiving decision or explicitly represented as unresolved.

### P2

Whether further determination of the shared inquiry issue has finite progress / stopping and a bounded fallback.

### P3

Whether the same unresolved inquiry issue, when material to execution, is prevented from becoming permission/certainty-equivalent closure.

### P4

Whether the shared authority record is current, action-scoped and non-amplifying.

### P5

Whether a change in the shared material action basis between \(t_0,t_1\) forces requalification before execution.

### P6

Whether records counted as independent corroboration are actually independent under the shared provenance-root relation.

---

## 3. P2/P3 are coupled, not independent switches

P2 and P3 use the **same unresolved inquiry object** \(u\).

Their distinction is semantic:

- P2 concerns the **process** used to work an unresolved state: can it continue without a finite viable bound?
- P3 concerns the **disposition** of that unresolved state when it is material: may it be promoted into execution/certainty?

The same issue can therefore exhibit:

| P2 | P3 | Shared-issue interpretation |
|---:|---:|---|
| 1 | 1 | inquiry is bounded; unresolved state is not falsely promoted |
| 0 | 1 | inquiry/search is unbounded even though the current unresolved residual is explicitly non-blocking/non-promoted |
| 1 | 0 | inquiry is bounded, but a still-material unresolved state is nevertheless promoted to execution |
| 0 | 0 | determination is unbounded and a material unresolved state is also promoted |

This is not a pair of stored truth flags. The values are derived from the inquiry graph, fallback relation, materiality and action disposition.

---

## 4. Full-cube realizability theorem

Let:

\[
\mathbb B^6=\{0,1\}^6.
\]

### Theorem 1

For every signature:

\[
s\in\mathbb B^6
\]

there exists a finite shared-substrate model \(M_s\) satisfying the background coherence constraints such that:

\[
\Sigma_P(M_s)=s.
\]

### Constructive proof

For a requested signature \(s=(s_1,\ldots,s_6)\), the constructor makes the following lower-level choices on the same substrate:

- if \(s_1=0\), add one asserted proposition stronger than the support relation actually establishes; otherwise every asserted proposition is supported or explicitly unresolved;
- if \(s_2=0\), give the shared inquiry issue a non-decreasing/cyclic determination relation with no bounded fallback; otherwise give it a finite rank and fallback;
- if \(s_3=0\), make that same unresolved issue material to \(\alpha\) while \(\alpha\) executes; otherwise its unresolved residual is explicitly non-promoted for the action;
- if \(s_4=0\), keep authority record \(g\) visible/current but make its declared scope exclude \(\alpha\); otherwise \(g\) covers \(\alpha\);
- if \(s_5=0\), change material record \(m\) between \(t_0,t_1\) without requalification; otherwise keep it unchanged or requalify;
- if \(s_6=0\), use two distinct immediate evidence sources with the same material provenance root and count them as independent; otherwise give them distinct roots.

All metadata remain visible to every applicable predicate. The constructor changes semantic relations, not six stored P-bits.

The executable certificate enumerates all \(64\) signatures and verifies exact equality:

\[
\Sigma_P(M_s)=s.
\]

Therefore \(\Sigma_P\) is surjective onto \(\mathbb B^6\). ∎

---

## 5. Boolean diagnostic minimality theorem

Consider any alternative Boolean diagnostic basis:

\[
Q=(Q_1,\ldots,Q_m)
\]

on the same model class.

Require **lossless principle recovery**: there exists a decoder

\[
D:\mathbb B^m\rightarrow\mathbb B^6
\]

such that for every admissible model \(M\),

\[
D(\Sigma_Q(M))=\Sigma_P(M).
\]

### Theorem 2

Any such lossless Boolean diagnostic basis requires:

\[
m\ge 6.
\]

### Proof

By Theorem 1, \(\Sigma_P\) assumes all \(64\) values in \(\mathbb B^6\).

If \(D\circ\Sigma_Q=\Sigma_P\), then two models with different P-signatures cannot have the same Q-signature; otherwise the deterministic decoder \(D\) would have to map one Q-signature to two different P-signatures.

Hence \(\Sigma_Q\) must realize at least \(64\) distinct signatures.

But \(m\) Boolean predicates can realize at most:

\[
2^m
\]

signatures.

Therefore:

\[
2^m\ge64=2^6
\]

and thus:

\[
\boxed{m\ge6}.
\]

Since the current P-basis itself has six Boolean coordinates, the lower bound is attained. ∎

---

## 6. What “minimal” means here

A22 establishes:

> **P1–P6 are minimal in cardinality among lossless Boolean diagnostic bases that preserve the full individual six-principle truth signature on the declared model class.**

This is a genuine lower bound, not a search over a finite catalogue of candidate repairs.

It is stronger than deletion-irredundancy.

It is different from unrestricted axiom-basis minimality.

---

## 7. Why this does not prove one-axiom impossibility

Suppose the only question is:

> does the model satisfy all six principles?

Then define:

\[
Q(M)=P_1(M)\land P_2(M)\land P_3(M)\land P_4(M)\land P_5(M)\land P_6(M).
\]

One Boolean predicate \(Q\) exactly recognizes the full-pass set.

Therefore no theorem can honestly claim:

> “six predicates are necessary to recognize the conjunction of the six.”

That would be false.

The six-coordinate lower bound arises only when the representation must preserve **which principle(s) pass or fail**, i.e. the full diagnostic / traceability semantics.

That requirement is relevant to this corpus because P1–P6 are separately:

- traced to Foundation normal forms;
- mapped into requirements;
- ablated;
- falsified/repaired;
- tested;
- and used as independent diagnostic obligations.

---

## 8. Non-Boolean encodings

The counting theorem also does not prohibit a single variable with 64 values, a six-bit integer, a vector, a lattice element or another non-Boolean structure from encoding the same diagnostic information.

Such an encoding changes the representation type; it does not reduce the information content.

The lower bound is therefore about the number of **Boolean predicates**, not about the number of fields in every imaginable mathematical representation.

---

## 9. Relationship to the other minimality claims

The corpus now has four distinct results that should not be conflated:

1. **A15 / ablation:** each current minimal invariant survives strongest-repair search within corrected fixtures.
2. **A16 / A20:** each Pi is logically independent / irredundant relative to declared semantics.
3. **A22:** six Boolean coordinates are information-theoretically minimal for losslessly preserving all six individual principle states.
4. **Not proved:** absolute minimality across every possible alternative semantic language or arbitrary non-Boolean representation.

This vocabulary should be used externally without collapsing the four claims.
