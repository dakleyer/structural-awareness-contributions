# 00K-A14 — GitHub Actions Reproduction Record — 379/379 — v0.1

| | |
|---|---|
| **Parent** | [00K — Six-Principle Sufficiency & Adversarial Ablation Test](./00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md) |
| **Completion review** | [00K-A13 — Six-Principle Serious Ablation Completion Review](./00K_A13_SIX_PRINCIPLE_SERIOUS_ABLATION_COMPLETION_REVIEW_v0.1.md) |
| **Workflow** | [`.github/workflows/00k-symbolic-ablations.yml`](../../../.github/workflows/00k-symbolic-ablations.yml) |
| **Run** | [GitHub Actions run 36108965548](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36108965548) |
| **Commit tested** | `948b493ed88e5788a2827e39c11810edad088d10` |
| **Status** | **COMPLETED / SUCCESS — all 10 jobs** |
| **Date** | 25 September 2026 |
| **Evidence class** | repository-CI reproduction of deterministic symbolic fixtures; not live product/runtime evidence |

> **Result.** The current serious-hardened 00K campaign is independently reproduced by GitHub Actions at **346/346 core + 33/33 supplemental = 379/379 symbolic tests**.

---

## 1. Reproduced core matrix

| Job | Expected current core count | CI result |
|---|---:|---|
| **A1 P1 / 00J** | **42** | SUCCESS |
| **A2 P2 / 00E** | **58** | SUCCESS |
| **A3 P3 / 00F** | **49** | SUCCESS |
| **A4 P4 / 00H** | **76** | SUCCESS |
| **A5 P5 / 00I** | **47** | SUCCESS |
| **A6 P6 / 00G matched-authority + transitive-dependency isolation** | **74** | SUCCESS |

**Core total: 346/346.**

---

## 2. Supplemental anti-confirmation-bias jobs

| Job | Expected count | CI result |
|---|---:|---|
| **A6a P6 / original 00G naive-pair falsifier** | **10** | SUCCESS |
| **A6b P6 / independent 00F composition isolation** | **11** | SUCCESS |
| **Cross-scenario independent P1–P6 kernels** | **12** | SUCCESS |

**Supplemental total: 33/33.**

The supplemental jobs remain deliberately separate from the six core counts because they test methodological falsifiers, independent isolation and reimplementation rather than adding a seventh principle.

---

## 3. Aggregate gate

The aggregate campaign job:

> **00K full campaign (379)**

completed successfully and verified:

```text
Core passing regression count: 346/346
Supplemental passing count: 33/33
Campaign total: 379/379
```

The execution-lock manifest is validated before the aggregate runner.

---

## 4. Why this record matters

Earlier GitHub Actions milestones verified smaller campaign states, including the prior 134/134 surface. Those remain useful history but are not the evidence for the current serious-hardened programme.

This run is the first repository-CI reproduction of the **current 379-test state** after:

- P1 matched-semantic confound correction;
- P2 matched-prefix strongest-repair hardening;
- P3 HOLD-marker confound correction;
- P4 minimal-authority-basis refinement;
- P5 exhaustive material-basis subset audit; and
- P6 transitive-dependency hardening.

The current counts are therefore no longer only local/pre-publication assertions.

---

## 5. Evidence boundary

A clean CI run establishes reproducibility of the committed symbolic fixtures and their declared expected counts.

It does **not** establish:

- independent external scientific replication;
- universal necessity/minimality of P1–P6;
- live execution against named commercial technologies;
- empirical superiority of Ecosystem Positioning;
- production safety/certification; or
- that 379 pytest assertions are 379 independent experiments.

The next evidence level is stateful/runtime execution of selected hardened fixtures under matched resources and strong conventional peers, followed by independent reproduction outside this repository.
