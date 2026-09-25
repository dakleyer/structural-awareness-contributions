# 00K-A2 — P2 / 00E deterministic symbolic ablation

**Removed principle:** P2 — bounded unresolved effort and viable oversight  
**Scenario:** 00E — *100 Million Tokens*  
**Status:** deterministic symbolic execution; not a live enterprise-agent benchmark

## Preserved first-pass layer

The original A2 negative branch supplies repeated non-decision-relevant evidence until finite capacity is exhausted. The positive branch becomes resolvable after a bounded number of steps.

That base + first grid contributed **13 tests** and remains preserved.

## Serious-repair hardening

The strengthened fixture now uses a harder matched-prefix family:

- negative and positive branches are identical until the final useful step;
- the positive branch resolves exactly at the horizon;
- the negative branch remains unresolved.

This removes easy content/pattern shortcuts and forces the repair to decide whether to continue or stop under finite capacity.

Serious alternatives tested include fixed TTL/max-step controls, no-progress circuit breakers, parallel fan-out, cached/default decisions, external scheduler deadlines, bounded probes and an exhaustive reduced family of observation-only memoryless policies.

No memoryless observation-only policy passes both matched branches. Passing peers require a finite deadline/budget/patience/probe boundary tied to decision viability — **SEMANTIC RECONSTRUCTION of P2**.

See [00K-A08 — P2 Strongest-Repair & Prefix-Indistinguishability Audit](../../00K_A08_P2_STRONGEST_REPAIR_AND_PREFIX_INDISTINGUISHABILITY_v0.1.md).

## Result

- preserved base + grid: **13**
- serious-repair layer: **45**
- **current A2 total: 58/58**

No TRUE SUBSTITUTE is found in the current serious-repair surface.

This does not establish universal P2 necessity. A future mechanism that terminates unresolved determination, preserves a still-reachable late positive resolution and avoids false closure **without** a finite effort/horizon/fallback invariant or operational equivalent is a valid counterexample.
