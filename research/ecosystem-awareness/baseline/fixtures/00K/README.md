# 00K — Executable Six-Principle Ablation Harnesses

**Parent:** [00K — Six-Principle Sufficiency & Adversarial Ablation Test](../../00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md)  
**Summary:** [00K-A04 — Six-Principle Symbolic Execution Summary](../../00K_A04_SIX_PRINCIPLE_SYMBOLIC_EXECUTION_SUMMARY_v0.1.md)  
**Status:** first-pass deterministic symbolic harnesses exist for **P1–P6**.

## Current executable matrix

| Principle | Scenario | Harness | Tests | Current result |
|---|---|---|---:|---|
| **P1** Qualified determination / evidence→decision | 00J Rights-Provenance Inversion | [A1 / P1–00J](../00K-A1-P1-00J/README.md) | **11/11** | no TRUE SUBSTITUTE found; typed evidence/proposition peer = SEMANTIC RECONSTRUCTION |
| **P2** Bounded unresolved effort | 00E 100 Million Tokens | [A2 / P2–00E](../00K-A2-P2-00E/README.md) | **11/11** | no TRUE SUBSTITUTE found; budgeted search = SEMANTIC RECONSTRUCTION |
| **P3** No false closure | 00F Chaos in the Smartcity | [A3 / P3–00F](../00K-A3-P3-00F/README.md) | **13/13** | no TRUE SUBSTITUTE found; explicit unresolved/non-permission state = SEMANTIC RECONSTRUCTION |
| **P4** Qualification-preserving handoff / authority lineage | 00H Quiet Four Thousand | [A4 active harness](../00K-A4-P4-00H/README.md) · [reviewed v0.2 ZIP](../00K-A4-P4-00H-v0.2/README.md) | **27/27 active** | no TRUE SUBSTITUTE found; A2-L root/delegation lineage = SEMANTIC RECONSTRUCTION |
| **P5** Material-change requalification | 00I Semantic TOCTOU | [A5 / P5–00I](../00K-A5-P5-00I/README.md) | **12/12** | no TRUE SUBSTITUTE found; generation/version compare = SEMANTIC RECONSTRUCTION |
| **P6** No local→ecosystem promotion / non-substitution | 00G False-Context Convergence | [A6 / P6–00G](../00K-A6-P6-00G/README.md) | **15/15** | no TRUE SUBSTITUTE found; source-independence peer = SEMANTIC RECONSTRUCTION |

**Aggregate regression count: 89 passing symbolic tests.**

Repository CI: [**00K symbolic ablations — successful run #1**](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36091488903). Six matrix jobs independently re-run the expected counts on Python 3.13.

The count is not a score and not 89 independent experiments. It is the current executable regression surface.

## Common test discipline

Every harness follows the same 00K rule:

1. freeze a negative branch and a matched positive/boundary branch;
2. run the full principle route;
3. remove exactly one semantic invariant;
4. try plausible repairs using the other five principles and native controls;
5. reject deny-all, accept-all, infinite-search and oracle shortcuts;
6. classify a successful repair as TRUE SUBSTITUTE only if it does **not** recreate the removed invariant;
7. leave the falsification frontier open.

## What these harnesses establish

At the current symbolic-fixture level:

- P1–P6 can each be operationalized as a branch-discriminating invariant;
- the full route passes the selected negative and positive controls;
- the tested Pk-blind alternatives do not;
- the strongest passing peer in each fixture implements an operationally equivalent form of the removed principle.

This provides **provisional semantic-necessity support inside the declared fixtures**.

## What they do not establish

They do not establish:

- universal minimality of six principles;
- formal necessity across all possible systems;
- empirical failure of any named commercial technology;
- a production certification;
- an EA/EP-exclusive implementation claim; or
- that 89 passing assertions are 89 independent empirical observations.

A new branch-correct mechanism that passes without reconstructing a removed invariant is a valid counterexample and must be credited.
