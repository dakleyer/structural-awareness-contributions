# 00K-A04 — Six-Principle Symbolic Execution Campaign Summary — v0.1

**Parent:** [00K — Six-Principle Sufficiency & Adversarial Ablation Test](./00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md)  
**Execution router:** [00K Symbolic Ablation Suite](./fixtures/00K-SUITE/README.md)  
**Status:** current symbolic execution summary · not live product evidence  
**Date:** 25 September 2026

> **Current result.** All six principles now have an executable, fixture-bounded leave-one-principle-out harness. After serious hardening of all six harnesses, the canonical core contains **346 regression tests**. Supplemental falsification, independent-isolation and cross-scenario packages add **33 tests**, for a current registered symbolic campaign surface of **379 tests**.

The test count is a regression count, **not an evidence score**. The important result is the structure of the counterfactuals: negative branch, matched positive/boundary control, strongest fair repair, and explicit classification of any successful repair as TRUE SUBSTITUTE or SEMANTIC RECONSTRUCTION.

---

## 1. Core six-principle execution surface

| Principle | Primary fixture | Core tests | Strongest tested passing repair | Current bounded disposition |
|---|---|---:|---|---|
| **P1 — qualified determination / explicit residual** | [A1 / 00J](./fixtures/00K-A1-P1-00J/README.md) | **42** | evidence-semantics→proposition→decision contract | old naive pair falsified; corrected surface = **SEMANTIC RECONSTRUCTION** |
| **P2 — bounded unresolved effort / viable oversight** | [A2 / 00E](./fixtures/00K-A2-P2-00E/README.md) | **58** | finite horizon/budget/patience/scheduler/probe rules | **SEMANTIC RECONSTRUCTION**; no TRUE SUBSTITUTE found |
| **P3 — no false closure from unresolved state** | [A3 / 00F](./fixtures/00K-A3-P3-00F/README.md) | **49** | supermajority/unanimity/action-set intersection with unresolved non-permission | old HOLD-marked base falsified; corrected surface = **SEMANTIC RECONSTRUCTION** |
| **P4 — qualification-preserving authority basis** | [A4 / 00H](./fixtures/00K-A4-P4-00H/README.md) | **76** | lineage, scoped capability, legitimate maker-checker, opaque owner PDP | **REFINEMENT:** minimal authority qualification survives; full lineage not necessary |
| **P5 — material-change requalification at use time** | [A5 / 00I](./fixtures/00K-A5-P5-00I/README.md) | **47** | full basis compare/hash/vector/event/epoch | **SEMANTIC RECONSTRUCTION**; no TRUE SUBSTITUTE found |
| **P6 — no local→ecosystem promotion / non-substitution** | [A6 / matched-authority 00G](./fixtures/00K-A6-P6-00G/README.md) | **74** | transitive dependency graph / effective material-root peer | original pair falsified; hardened surface = **SEMANTIC RECONSTRUCTION** |

**Core total: 346 tests.**

Each strong peer is deliberately allowed to be conventional and non-EA-branded. A passing peer is not treated as an EA win. If it passes by implementing the same semantic invariant, the result supports principle-level necessity while weakening any claim that one particular architecture owns the implementation.

---

## 2. Supplemental anti-confirmation-bias surface

| Package | Tests | Why it exists | Result |
|---|---:|---|---|
| [A6a — naive 00G F/G falsifier](./fixtures/00K-A6a-P6-00G/README.md) | **10** | asks whether the original scenario pair itself isolates P6 | **TRUE SUBSTITUTE found**: authority-only separates the unmodified pair |
| [A6b — independent 00F P6 isolation](./fixtures/00K-A6b-P6-00F/README.md) | **11** | re-tests P6 where local authority/freshness/determination are matched and only shared-resource composition differs | no TRUE SUBSTITUTE found; compatibility peer reconstructs P6 |
| [Independent cross-scenario kernels](./fixtures/00K-cross-scenario-independent/README.md) | **6** | reimplements P4/P5/P6 without importing A1–A6 helper code | **6/6**; same invariants reuse across a second scenario family |

**Supplemental total: 33 tests.**

**Registered campaign total: 379 tests.**

The A6a negative result is methodologically important. It demonstrates that the programme is capable of rejecting its own first test construction. The P6 claim is retained only after the confound is removed in matched-authority A6 and independently re-isolated in 00F. See [00K-A05](./00K_A05_P6_CONFOUND_FALSIFIER_AND_ISOLATION_NOTE_v0.1.md).

---

## 3. What “sufficiency” means in this campaign

The symbolic sufficiency claim is deliberately narrower than “these six principles solve AI safety.”

For each isolated fixture:

1. the **full principle route** must pass the critical negative branch;
2. it must also pass the matched positive/boundary control;
3. it must not win through deny-all, HOLD-all, accept-all or unbounded search;
4. the same declared authority/resource/fact boundary is used by the ablated repairs; and
5. a strong conventional peer is credited when it reproduces the required behaviour.

On that definition, the current symbolic fixtures provide **fixture-level support for joint sufficiency**: there exists a branch-correct implementation of the six-principle semantics for each selected failure family.

This is not a proof that P1–P6 are sufficient for every possible ecosystem or every future failure class.

---

## 4. What “necessity” means in this campaign

The leave-one-out necessity question is:

> After removing Pk, can the remaining five principles plus the strongest fair native/peer controls pass both the critical branch and its positive control **without reconstructing Pk's invariant**?

Current isolated results:

- P1–P5: no TRUE SUBSTITUTE found in the tested repair surfaces;
- P6: the **unmodified** 00G pair does admit a TRUE SUBSTITUTE, so that pair is rejected as a necessity test;
- corrected matched-authority P6 and independent 00F composition isolation: no TRUE SUBSTITUTE found in their tested repair surfaces.

Accordingly, the present result is **provisional semantic necessity within the declared isolated fixtures**, not mathematical or universal minimality.

---

## 5. Why the code is intentionally simple

The harnesses do not attempt to simulate:

- 4,000 actual bank refunds;
- a live multinational consuming 100 million tokens;
- a city-scale autonomous mobility system;
- robots physically marching toward Russia;
- a real copyright/licensing network; or
- a production patch-management platform.

They instead isolate the **decision invariant** that makes the failure distinguishable.

That is intentional. A small executable counterexample is useful here because it makes hidden circularity visible:

- if two branches are indistinguishable without the removed invariant, a Pk-blind deterministic rule cannot separate them;
- if a “fix” blocks both negative and positive branches, it is exposed as a deny-all shortcut;
- if a strong peer succeeds by rebuilding the same discriminating relation, the implementation is non-unique but the semantic invariant survives;
- if a genuinely different discriminant succeeds, it is a TRUE SUBSTITUTE and counts against the principle.

The code is therefore an executable specification / adversarial model, not a digital twin of the entire real-world scenario.

---

## 6. Reproducibility and continuous regression

The suite router is:

[**fixtures/00K-SUITE**](./fixtures/00K-SUITE/README.md)

Run locally:

```bash
cd research/ecosystem-awareness/baseline/fixtures/00K-SUITE
python run_all.py
```

The repository workflow:

[`.github/workflows/00k-symbolic-ablations.yml`](../../../.github/workflows/00k-symbolic-ablations.yml)

runs each fixture independently and also runs the aggregate campaign gate. The expected regression contract is:

```text
core:         101
supplemental:  27
total:        128
```

A count mismatch or failed assertion makes the workflow fail. The regression count is intended to prevent silent weakening of the fixtures; it is not a score of scientific confidence.

---

## 7. Current bounded claim

The strongest statement supported by the present symbolic campaign is:

> **Across the declared isolated 00E–00J-derived fixtures, P1–P6 jointly admit branch-correct solutions, and leave-one-principle-out strongest-repair tests have not found a TRUE SUBSTITUTE for any principle after known fixture confounds are controlled. Passing alternative architectures repeatedly succeed by reconstructing the removed semantic invariant rather than by eliminating its need.**

The P6 history is part of that claim, not hidden from it: the unmodified 00G pair failed as an isolation test and was corrected.

This does **not** establish:

- universal necessity or minimality;
- empirical failure of named technologies;
- production safety/certification;
- superiority of EA/EP over every conventional architecture;
- independent external replication.

The next evidence level is external/independent reproduction of the symbolic fixtures and then matched-resource execution against concrete implementation profiles.
