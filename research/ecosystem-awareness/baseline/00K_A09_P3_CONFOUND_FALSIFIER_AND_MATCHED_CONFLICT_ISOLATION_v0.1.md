# 00K-A09 — P3 Confound Falsifier & Matched-Conflict Isolation — v0.1

**Parent:** [00K — Six-Principle Sufficiency & Adversarial Ablation Test](./00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md)  
**Principle:** P3 — no false closure from unresolved material state  
**Scenario:** [00F — Chaos in the Smartcity](./00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_FREEZE_EDITION.md)  
**Status:** methodological correction + serious-repair hardening executed  
**Date:** 25 September 2026

> **Finding.** The original A3 base conflict contained an explicit `HOLD` posture. A narrow rule “if any participant says HOLD, hold; otherwise follow a normal priority” can pass that base branch and the two simple positive controls without implementing a general unresolved-state invariant. The existing mixed-posture grid already reduced that weakness; this hardening now makes it explicit, preserves the shortcut as a falsifier, and defines a corrected matched-conflict fixture with no HOLD marker and equal authority/confidence/freshness across sources.

---

## 1. Why the base branch alone was insufficient

The initial conflict branch was:

```text
PLAN_A / PLAN_B / NORMAL / HOLD
```

A P3-blind shortcut can simply treat the literal `HOLD` token as a veto. That is not evidence that the architecture knows an unresolved material relation must not become permission.

The new test `test_old_base_conflict_is_confounded_by_explicit_HOLD_marker` preserves this as a genuine **TRUE SUBSTITUTE for the old base pair**.

This does not falsify P3. It falsifies the old branch as a necessity isolation by itself.

---

## 2. Corrected matched-conflict isolation

The corrected negative branch uses:

```text
PLAN_A / PLAN_B / PLAN_A / PLAN_B
```

with equal:

- authority rank;
- confidence;
- freshness; and
- branch resources.

Positive controls remain uniform determinate states:

- `PLAN_A / PLAN_A / PLAN_A / PLAN_A`;
- `NORMAL / NORMAL / NORMAL / NORMAL`.

The target distinction is therefore material compatibility/determination rather than a literal HOLD marker or privileged source.

---

## 3. Serious repair attempts

The additive harness tests:

1. authority-priority selection;
2. confidence-priority selection;
3. freshest-source selection;
4. majority + default;
5. human approval without new evidence;
6. timeout/default NORMAL;
7. risk-priority “PLAN_A is safer” heuristic;
8. supermajority thresholds;
9. unanimity;
10. robust intersection of allowed action sets; and
11. explicit unresolved containment.

The first seven mechanisms all false-close at least one matched material conflict.

Supermajority, unanimity and robust action-set intersection can pass the corrected controls, but only by making the operational rule:

> if material support is not sufficiently compatible/determinate, do not promote one posture to executable permission; retain/contain/requalify.

That is an action-level **SEMANTIC RECONSTRUCTION of P3**, not an EA-specific implementation requirement.

---

## 4. Execution result

The new serious-repair layer adds **34 passing tests**.

Local pre-publication execution:

```text
34 passed
```

Together with the existing A3 base + grid layer (**15**):

> **current A3 total: 49/49 symbolic tests**

No TRUE SUBSTITUTE is found in the corrected matched-conflict serious-repair surface.

---

## 5. Current P3 disposition

- **TRUE SUBSTITUTE for the old HOLD-containing base pair:** **YES** — literal HOLD-veto shortcut.
- **Old base pair accepted as P3 necessity isolation:** **NO, not alone**.
- **Corrected matched-conflict isolation:** **YES**.
- **TRUE SUBSTITUTE in corrected serious-repair surface:** **NONE FOUND**.
- **Strong passing peers:** supermajority non-permission, unanimity, robust action-set intersection.
- **Why they pass:** they refuse to promote unresolved/incompatible material state into an executable posture.
- **00K classification:** **SEMANTIC RECONSTRUCTION of P3**.
- **Evidence class:** deterministic symbolic fixture.

---

## 6. Falsifier

P3's bounded necessity claim must be reopened if a repair can, under the matched conflict and positive controls:

1. avoid unsafe promotion of the incompatible corridor postures;
2. continue to execute uniform legitimate NORMAL and PLAN_A states;
3. avoid deny-all / permanent HOLD;
4. do so without a rule that makes unresolved/materially incompatible state non-permission, containment-only, or an operational equivalent.

Such a mechanism is a **TRUE SUBSTITUTE** and counts against P3 necessity.
