# 00K-A3 — P3 / 00F deterministic symbolic ablation

**Removed principle:** P3 — no false closure from unresolved material state  
**Scenario:** 00F — *Chaos in the Smartcity*  
**Status:** deterministic symbolic execution; not a live city/mobility benchmark

## Preserved first-pass layer

The original A3 conflict branch used fresh, visible, mutually incompatible local postures over one shared corridor. The original base + bounded grid contributed **15 tests** and remains preserved.

## Methodological correction

The original base conflict included an explicit `HOLD` posture. A narrow rule “if any participant says HOLD, hold; otherwise follow a normal priority” can pass that base branch plus simple positive controls without implementing a general unresolved-state invariant.

That shortcut is now preserved as a genuine falsifier for the **old base pair**.

See [00K-A09 — P3 Confound Falsifier & Matched-Conflict Isolation](../../00K_A09_P3_CONFOUND_FALSIFIER_AND_MATCHED_CONFLICT_ISOLATION_v0.1.md).

## Corrected serious-repair isolation

The corrected negative branch removes the HOLD marker and equalizes authority, confidence and freshness:

```text
PLAN_A / PLAN_B / PLAN_A / PLAN_B
```

Positive controls remain uniform determinate PLAN_A and NORMAL states.

Serious alternatives include authority priority, confidence priority, freshness priority, majority/default, human approval without new evidence, timeout/default, risk-priority heuristics, supermajority, unanimity and robust action-set intersection.

Priority/default mechanisms false-close at least one matched conflict.

Supermajority, unanimity and action-set intersection can pass, but only by operationally enforcing that materially unresolved/incompatible state is **not promoted to executable permission** — **SEMANTIC RECONSTRUCTION of P3**.

## Result

- preserved base + grid: **15**
- serious-repair/falsifier layer: **34**
- **current A3 total: 49/49**

No TRUE SUBSTITUTE is found in the corrected matched-conflict repair surface.

A future repair that safely resolves the matched conflict, preserves legitimate positive execution and does so without a non-permission/containment rule for unresolved material state is a valid counterexample to P3 necessity.
