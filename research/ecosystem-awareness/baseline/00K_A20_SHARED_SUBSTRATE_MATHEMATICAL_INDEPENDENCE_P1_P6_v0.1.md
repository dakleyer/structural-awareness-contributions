# 00K-A20 — Shared-Substrate Mathematical Independence of P1–P6 — v0.1

| | |
|---|---|
| **Parent** | [00K — Six-Principle Sufficiency & Adversarial Ablation Test](./00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md) |
| **Earlier formal sketch** | [00K-A18](./00K_A18_PURE_MATHEMATICAL_INDEPENDENCE_P1_P6_v0.1.md) |
| **Corpus-grounded counterpart** | [00K-A16](./00K_A16_FORMAL_RELATIVE_INDEPENDENCE_PROOF_P1_P6_v0.1.md) |
| **Traceability proof** | [00K-A19](./00K_A19_PRINCIPLE_REQUIREMENT_TRACEABILITY_AND_CONSERVATION_PROOF_v0.1.md) |
| **Full-cube / Boolean diagnostic minimality** | [00K-A22](./00K_A22_FULL_CUBE_BOOLEAN_DIAGNOSTIC_MINIMALITY_v0.1.md) |
| **Status** | **shared-substrate model-theoretic independence proof** |
| **Date** | 25 September 2026 |
| **Premises used** | common semantic substrate + explicit background coherence theory B + P1–P6 definitions |
| **Premises not used** | 00E–00J outcomes, pytest counts, repair-search outcomes, CI results, product behaviour |

> **Result.** Relative to the shared semantic substrate and background coherence theory \(B\) below, each P1–P6 has a finite countermodel satisfying \(B\) and the other five principles. Hence \(B\cup(T\setminus\{P_i\})\not\models P_i\) for every \(i\). Unlike A18, the result is not obtained by assigning each principle its own unconstrained Boolean content variable.

---

## 1. Why A20 exists

A18 proved a correct but weak fact: six chosen formulas over mostly separate Boolean coordinates do not imply one another.

That is useful as a syntax/logic sanity check, but it leaves an obvious objection: if P4, P5 and P6 are represented respectively by independent variables \(a,c,d\), their independence is largely built into the representation.

A20 removes that shortcut.

All six principles are interpreted over the **same records, same provenance graph, same scopes, same validity intervals, same decision/action objects and same determination process**. A countermodel is accepted only if it also satisfies background constraints that couple those objects.

---

## 2. Shared semantic structure

A model is a finite relational structure:

\[
\mathcal M=
(R,Q,A,T,
src,root,scope,valid,kind,support,value,
material,uses,grant,conflict,counted,requalify,\leadsto).
\]

### Sets

- \(R\): records/signals/claims available to the participant.
- \(Q\): propositions.
- \(A\): candidate actions.
- \(T\): ordered times, containing at least qualification time \(t_0\) and action time \(t_1\), with \(t_0<t_1\).

### Functions shared by all principles

For every \(r\in R\):

- \(src(r)\): immediate source;
- \(root(r)\): transitive material provenance root;
- \(scope(r)\subseteq A\): actions for which the record is scoped;
- \(valid(r)\subseteq T\): times at which the record is current;
- \(kind(r)\): ordinary evidence, authority, condition/policy, etc.;
- \(value(r,t)\): decision-material value represented at time \(t\), where applicable.

### Relations shared by all principles

- \(support(r,q,t)\): record \(r\) supports proposition \(q\) at time \(t\);
- \(material(r,a)\): \(r\) is material to action \(a\);
- \(uses(a,r,t)\): action/determination at time \(t\) relies on \(r\);
- \(grant(r,a)\): authority record \(r\) purports to authorize \(a\);
- \(conflict(r,s,q,t)\): current records \(r,s\) materially conflict about \(q\);
- \(counted(r,s,a)\): the composition for \(a\) treats \(r,s\) as independent corroboration;
- \(requalify(a,t_1)\): the action basis was reopened and qualified at action time;
- \(z\leadsto z'\): one further determination/search/review step is available from process state \(z\).

Derived predicates are not free variables:

\[
current(r,t)\iff t\in valid(r)
\]

\[
scopefit(r,a)\iff a\in scope(r)
\]

\[
independent(r,s)\iff root(r)\neq root(s)
\]

\[
changed(r,t_0,t_1)\iff value(r,t_0)\neq value(r,t_1)
\]

and material unresolved conflict for \(a\) at \(t\) is derived from current conflicting records used by the decision.

---

## 3. Background coherence theory B

Every admissible model must satisfy the following common constraints.

### B1 — common metadata discipline

Every record has one source, one material provenance root, a declared scope and a validity relation. Authority, policy and ordinary evidence are **not different mathematical universes**.

### B2 — provenance is shared

The same \(root(\cdot)\) relation is used for:

- evidence lineage;
- authority lineage;
- source-dependence analysis; and
- independence/corroboration judgments.

P4 and P6 therefore cannot receive unrelated provenance variables.

### B3 — time is shared

The same \(T,t_0,t_1,valid(\cdot)\) structure governs ordinary evidence, authority records and material condition/policy records.

P4 and P5 therefore cannot receive unrelated notions of currentness.

### B4 — scope is shared

The same \(scope(\cdot)\) relation is used when a record is relied on as evidence or as authority.

### B5 — action basis is shared

If \(uses(a,r,t)\), the same record \(r\) is visible to all applicable principle predicates. A record cannot be “present for P4” but mathematically absent from P1/P5/P6 merely by changing representation.

### B6 — material change is derived

Whether a material basis changed is determined from \(value(r,t_0)\) and \(value(r,t_1)\); there is no free Boolean “P5 failed” variable.

### B7 — source independence is derived

Whether two records are independent is determined from \(root(r)\neq root(s)\); there is no free Boolean “P6 failed” variable.

### B8 — unresolved conflict is derived

Material unresolved state is produced by current conflicting records about a proposition relevant to the action; there is no free Boolean “P3 failed” variable.

### B9 — authority insufficiency is structural

Authority sufficiency is determined from authority-kind records, currentness, scope fit and grant/non-amplification relation. There is no free Boolean “P4 failed” variable.

### B10 — P1 is proposition-level, P6 is composition-level

P1 evaluates whether each proposition asserted/relied upon is supported or explicitly unresolved for its declared subject/scope. P6 evaluates whether the **composition operator** is entitled to treat multiple locally qualified records as independent/compatible support for a larger composed conclusion.

This prevents P1 from trivially swallowing P6 while keeping both on the same records.

### B11 — initial qualification and continued validity are distinct times

P1 can be satisfied at \(t_0\) while P5 later fails at \(t_1\). A correct original determination is not defined to remain correct after a material state change.

This prevents P1 from trivially swallowing P5.

---

## 4. P1–P6 over the shared substrate

Let \(a\in A\) be a material action.

### P1 — qualified determination / explicit residual

Every proposition asserted or relied upon at its qualification time is supported by the records used for that proposition, or is explicitly represented as unresolved. A record supporting a narrower proposition is not promoted to a stronger proposition.

### P2 — bounded viable determination

The active determination relation \(\leadsto\) is well-founded over the useful decision horizon: there is a finite ranking/remaining-budget function for unresolved work, with an explicit bounded fallback.

### P3 — no false closure

If the shared records induce a material unresolved conflict for \(a\) at action time, \(a\) is not promoted to executable closure.

### P4 — current decision-sufficient authority

If \(a\) executes at \(t_1\), there is an authority-kind record \(g\) such that:

\[
uses(a,g,t_1)\land grant(g,a)\land current(g,t_1)\land scopefit(g,a)
\]

and the grant relation does not amplify beyond its provenance/root authority boundary.

### P5 — action-time material-basis validity

If \(a\) executes at \(t_1\), then for every record \(r\) material to the qualified basis:

\[
changed(r,t_0,t_1)\Rightarrow requalify(a,t_1).
\]

### P6 — non-substituting composition

If \(a\)'s composition counts records \(r,s\) as independent corroboration, then:

\[
counted(r,s,a)\Rightarrow independent(r,s)
\]

and materially incompatible scoped claims are not silently collapsed into one ecosystem conclusion.

Let \(T=\{P_1,\ldots,P_6\}\).

---

## 5. Strong independence criterion

A20 proves independence **relative to B**:

\[
\forall i\in\{1,\ldots,6\},
\quad
B\cup(T\setminus\{P_i\})
\not\models P_i.
\]

Equivalently, for each \(i\) there must exist one finite structure \(\mathcal M_i\) such that:

\[
\mathcal M_i\models B,
\]

\[
\mathcal M_i\models P_j\quad\forall j\neq i,
\]

and:

\[
\mathcal M_i\not\models P_i.
\]

---

## 6. Common base used by the six countermodels

All six witnesses use the same kinds of objects:

- one material action \(\alpha\);
- qualification time \(t_0\) and action time \(t_1\);
- ordinary evidence records \(e,e_1,e_2\);
- an authority record \(g\);
- a material condition/policy record \(m\);
- provenance roots \(\rho_1,\rho_2\);
- a finite determination process unless P2 is the omitted principle.

Unless a witness says otherwise:

1. all used records are current at the relevant time;
2. \(g\) is scoped to and authorizes \(\alpha\);
3. the material basis does not change between \(t_0,t_1\);
4. records counted as independent have distinct roots;
5. no unresolved material conflict exists;
6. determination is bounded;
7. every asserted local proposition is adequately supported;
8. \(\alpha\) executes.

The witnesses modify **relations/functions of this common structure**, not a principle-specific truth flag.

---

## 7. Countermodel M1 — violate P1 only

Add propositions \(q\) and the stronger \(q^+\).

Let:

\[
support(e,q,t_0)
\]

hold, but:

\[
support(e,q^+,t_0)
\]

not hold.

The system nevertheless asserts/relies on \(q^+\).

Everything else remains in the common base:

- bounded process;
- no unresolved material conflict;
- valid current authority \(g\);
- unchanged material basis;
- independent composition.

Therefore:

\[
\mathcal M_1\models B\land P_2\land P_3\land P_4\land P_5\land P_6
\]

but:

\[
\mathcal M_1\not\models P_1.
\]

P1 is not derivable from the other five even when all records share the same provenance/scope/time substrate.

---

## 8. Countermodel M2 — violate P2 only

Keep the executable action \(\alpha\) fully qualified, authorized, current and composition-safe.

Add one unresolved determination state \(z\) with:

\[
z\leadsto z.
\]

There is no finite decreasing rank for this open-ended determination branch and no bounded fallback.

The unresolved branch is **not** promoted into execution, so P3 remains true. The executing action \(\alpha\) uses a different already-qualified proposition; P1/P4/P5/P6 remain true.

Hence:

\[
\mathcal M_2\models B\land P_1\land P_3\land P_4\land P_5\land P_6
\]

and:

\[
\mathcal M_2\not\models P_2.
\]

The failure is a property of the same determination system, not an independent Boolean.

---

## 9. Countermodel M3 — violate P3 only

Let current records \(e_1,e_2\) both be used for \(\alpha\) and satisfy:

\[
conflict(e_1,e_2,q,t_1).
\]

The system correctly represents that \(q\) is unresolved. Thus P1 is satisfied: the epistemic status itself is correctly qualified.

Nevertheless \(\alpha\) executes.

Authority \(g\) is valid and scoped, the material basis is unchanged, composition does not falsely claim source independence, and determination is bounded.

Therefore:

\[
\mathcal M_3\models B\land P_1\land P_2\land P_4\land P_5\land P_6
\]

but:

\[
\mathcal M_3\not\models P_3.
\]

This separates **knowing that the state is unresolved** from **refusing to convert that state into permission**.

---

## 10. Countermodel M4 — violate P4 only

The same authority record \(g\) is:

- current at \(t_1\);
- fully provenance-qualified;
- correctly understood by the system;
- unchanged since \(t_0\).

But its shared scope function satisfies:

\[
\alpha\notin scope(g).
\]

The action \(\alpha\) nevertheless executes.

P1 remains true because the system has sufficient evidence about what \(g\) actually authorizes; epistemic correctness does not manufacture permission.

P5 remains true because no material record changed after qualification.

P6 remains true because any records counted as independent have distinct shared provenance roots.

Thus:

\[
\mathcal M_4\models B\land P_1\land P_2\land P_3\land P_5\land P_6
\]

and:

\[
\mathcal M_4\not\models P_4.
\]

This is the key nontrivial separation:

> **correct/current knowledge of an insufficient grant is still not sufficient authority.**

P4 therefore does not follow from P1 or P5 even though all three inspect the same record \(g\), same scope relation and same time structure.

---

## 11. Countermodel M5 — violate P5 only

At qualification time \(t_0\), material record \(m\) has:

\[
value(m,t_0)=v_0.
\]

At action time \(t_1\):

\[
value(m,t_1)=v_1,\qquad v_1\neq v_0.
\]

So:

\[
changed(m,t_0,t_1).
\]

The original determination at \(t_0\) was correct, and P1 is therefore satisfied for that qualification event.

Authority record \(g\) remains current, scoped and non-amplifying. No unresolved conflict exists. Composition roots remain independent.

But:

\[
\neg requalify(\alpha,t_1)
\]

and \(\alpha\) executes.

Hence:

\[
\mathcal M_5\models B\land P_1\land P_2\land P_3\land P_4\land P_6
\]

while:

\[
\mathcal M_5\not\models P_5.
\]

Because currentness/change is derived from the common time/value structure, this separation cannot be produced by simply toggling a private P5 variable.

---

## 12. Countermodel M6 — violate P6 only

Let \(e_1,e_2\) be current records from distinct immediate sources:

\[
src(e_1)\neq src(e_2),
\]

but the shared provenance relation gives:

\[
root(e_1)=root(e_2)=\rho_1.
\]

Each record locally supports its own declared proposition correctly, so P1 is satisfied at the local proposition level.

The action composition nevertheless records:

\[
counted(e_1,e_2,\alpha)
\]

as if the two records were independent corroboration.

Authority \(g\) is valid and scoped; the material basis is unchanged; there is no unresolved conflict; determination is bounded.

Thus:

\[
\mathcal M_6\models B\land P_1\land P_2\land P_3\land P_4\land P_5
\]

but:

\[
\mathcal M_6\not\models P_6.
\]

This separates **local proposition sufficiency** from **correct composition of dependence** using the same evidence records and the same provenance graph.

---

## 13. Theorem

### Shared-substrate independence theorem

For every \(i\in\{1,\ldots,6\}\), Sections 7–12 exhibit a finite structure \(\mathcal M_i\) satisfying the common background theory \(B\), all \(P_j\) for \(j\neq i\), and not \(P_i\).

Therefore:

\[
\boxed{
\forall i,\;
B\cup(T\setminus\{P_i\})\not\models P_i
}
\]

and P1–P6 are logically independent **relative to the shared semantic substrate and coherence theory \(B\)**. ∎

---

## 14. Why this is stronger than A18

A18 used separate Boolean coordinates for several principle contents. A critic could reasonably say that the independence was largely encoded in those coordinates.

A20 removes that shortcut in four important places:

1. **P1/P4 share records, scope and time.** P4 can fail even when the system correctly knows the grant is insufficient.
2. **P1/P5 share the same qualification record across \(t_0,t_1\).** Original evidential sufficiency can hold while continued validity fails after change.
3. **P1/P6 share the same evidence records.** Local support can be correct while the composition operator misclassifies shared provenance as independence.
4. **P4/P5/P6 share the same provenance/scope/validity substrate.** Authority, currentness and dependence are not independent truth switches.

The countermodels are therefore separations **inside one semantic structure**, not assignments to six nearly orthogonal variables.

---

## 15. What A20 still does not prove

A20 does not prove:

- empirical necessity in real systems;
- completeness of P1–P6 for every possible failure;
- that the chosen shared substrate is the only legitimate semantics;
- that no stronger background theory could entail one principle from others;
- minimal cardinality among all logically equivalent axiom bases; or
- uniqueness of the P1–P6 formulation.

The correct external statement is:

> **A20 gives a shared-substrate model-theoretic independence result. The executable fixtures remain the stronger operational falsification layer and are not replaced by the theorem.**

That boundary should remain explicit.

---

## 16. Relationship to the rest of 00K

- [A18](./00K_A18_PURE_MATHEMATICAL_INDEPENDENCE_P1_P6_v0.1.md) remains as the simpler formal sketch / sanity check.
- **A20 is the preferred pure mathematical independence argument.**
- [A22](./00K_A22_FULL_CUBE_BOOLEAN_DIAGNOSTIC_MINIMALITY_v0.1.md) constructs all 64 P-signatures in its simplified executable model and proves the corresponding six-coordinate counting bound. Lifting all 64 witnesses to the complete B1–B11 substrate remains unverified; this dependency must not be treated as already closed.
- [A16](./00K_A16_FORMAL_RELATIVE_INDEPENDENCE_PROOF_P1_P6_v0.1.md) shows fixture-derived countermodels inside the corpus.
- [A1–A6 / A15](./00K_A15_COMPLETE_SIX_PRINCIPLE_ABLATION_TESTBOOK_v0.1.md) perform the hard operational repair search.
- [A19](./00K_A19_PRINCIPLE_REQUIREMENT_TRACEABILITY_AND_CONSERVATION_PROOF_v0.1.md) proves the semantic chain from principles into requirements and scenario/ablation routes.

The layers are complementary and deliberately non-substituting.
