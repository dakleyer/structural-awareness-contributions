# 00K-A6 — P6 / 00G deterministic symbolic ablation

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
