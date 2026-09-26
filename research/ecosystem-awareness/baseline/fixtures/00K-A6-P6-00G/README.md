# 00K-A6 — P6 / 00G deterministic symbolic ablation

> **Audit corrections — 26 September 2026:** [A14](./../../00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A14_CORRECCIONES_AUDITORIA_v0.1.md) describes current behavior and regression evidence. Prior execution records below remain historical; current implementations and replay outputs are versioned separately.

**Removed principle:** P6 — no local-to-ecosystem promotion / silent substitution  
**Scenario:** 00G — *Ciber Napoleon Goes to Russia*  
**Status:** deterministic symbolic execution; not a live robot, agent or product benchmark

## Isolation rule

To test P6 rather than authority provenance, Branch F and Branch G use the **same current transition authority**, same number of authenticated agents, same freshness and same confidence. The material difference is source dependence:

- **F:** five authenticated agents inherit one source (`SRC_N`);
- **G:** five authenticated agents draw from three materially independent sources.

The transition authority requires at least two independent sources.

## Repairs tested

P6 is removed and the fixture tries:

- identity/message quorum;
- higher confidence threshold;
- P4 provenance preservation without composition semantics;
- human majority approval;
- deny-all;
- a strong peer that deduplicates/corroborates by source lineage.

## Result

**17/17** tests pass after additive source-diversity/Sybil grid hardening.

Identity quorum, confidence, preserved provenance and human majority all false-transition Branch F. Deny-all blocks F but fails genuine Branch G. A source-independence strong peer passes both branches, but does so by explicitly computing materially independent evidence paths — **SEMANTIC RECONSTRUCTION of P6**.

No TRUE SUBSTITUTE is found in the tested repair surface.

## Boundary

This is a deliberately simplified executable fixture for the 00G principle question. It does not simulate physical robots marching anywhere, and it does not test OpenAI or another agent platform. A future mechanism that passes the same F/G controls without source-independence/non-substitution semantics is a valid counterexample to P6 necessity.


## Serious-repair hardening — transitive dependency

The canonical A6 fixture now also includes:

- [`p6_serious_repairs.py`](./p6_serious_repairs.py)
- [`test_p6_serious_repairs.py`](./test_p6_serious_repairs.py)
- [00K-A12 — P6 Transitive-Dependency & Strongest-Repair Audit](../../00K_A12_P6_TRANSITIVE_DEPENDENCY_AND_STRONGEST_REPAIR_AUDIT_v0.1.md)

This layer attacks a weakness in direct source counting: several visibly distinct
source IDs can still inherit one upstream material root.

The hardened branch pair equalizes identity count, organization diversity,
immediate source count, signatures, freshness, confidence, timing and content
diversity. Only the transitive dependency graph differs.

Serious alternatives — identity quorum, organization diversity, direct source
count, confidence weighting, temporal/content diversity, human committee and
source reputation — cannot separate the branches.

A transitive dependency-graph / effective-material-root peer does pass, but only
by reconstructing P6's dependency/non-substitution composition invariant.

Additive execution:

```text
57 passed
```

Current canonical A6 core:

```text
74 tests
```

A6a (the original confounded 00G falsifier) and A6b (independent 00F isolation)
remain separate supplemental packages.
