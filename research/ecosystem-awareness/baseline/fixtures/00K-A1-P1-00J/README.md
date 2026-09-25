# 00K-A1 — P1 / 00J deterministic symbolic ablation

**Removed principle:** P1 — qualified determination and explicit residual  
**Scenario:** 00J — *The Author Pays for Their Own Work*  
**Status:** deterministic symbolic execution; not a live rights platform or product benchmark

The A1 fixture now has two explicitly separated layers.

## 1. Preserved original layer

The original negative branch contains a valid, signed, fresh **generation-provenance** record. The original positive branch contains an actual rights-grant record supporting the enforcement proposition.

That layer plus the first bounded grid contributed **13 tests**. It remains preserved for lineage.

## 2. Falsification-first correction

The original pair also changed issuer/source and record class. That creates a genuine confound: a P1-blind rule that trusts `RIGHTS-OWNER` can reject the old negative branch and accept the old positive branch without evaluating evidence→proposition sufficiency.

This is now an explicit methodological result, not hidden.

See [00K-A07 — P1 Confound Falsifier & Matched-Semantic Isolation](../../00K_A07_P1_CONFOUND_FALSIFIER_AND_MATCHED_SEMANTIC_ISOLATION_v0.1.md).

## 3. Corrected matched-semantic isolation

The corrected pair holds equal:

- source/issuer;
- signature;
- freshness;
- record class;
- record count;
- provenance completeness; and
- authority context.

Only the **semantic proposition supported by the valid evidence** differs.

Serious repair attempts include:

- trusted-issuer allow-list;
- complete provenance;
- generic schema allow-list;
- confidence/risk scoring;
- independent quorum;
- human approval without a new rights fact;
- source reputation;
- threshold sweeps; and
- replicated valid-but-wrong propositions.

None separates the corrected negative and positive branches.

A vendor-neutral evidence-semantics / proposition / decision policy matrix does separate them, but only by implementing the operational P1 invariant: **SEMANTIC RECONSTRUCTION of P1**.

## Result

- preserved original + grid: **13**
- serious-repair/falsifier layer: **29**
- **current A1 total: 42/42**

No TRUE SUBSTITUTE is found in the corrected matched-semantic repair surface.

This does not establish universal P1 necessity. A future repair that correctly separates the matched branches without an evidence→proposition→decision sufficiency invariant or operational equivalent is a valid counterexample.
