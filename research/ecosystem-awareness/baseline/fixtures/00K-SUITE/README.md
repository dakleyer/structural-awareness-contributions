# 00K Symbolic Ablation Suite

**Status:** executable deterministic/symbolic regression surface  
**Parent:** [00K — Six-Principle Sufficiency & Adversarial Ablation Test](../../00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md)

This directory is the execution router for the six principle-ablation harnesses.
It does not replace the individual fixture READMEs or execution records.

## Current core surface

| Principle | Fixture | Current regression count | Current bounded result |
|---|---|---:|---|
| **P1** | [A1 / 00J](../00K-A1-P1-00J/README.md) | **13** | no TRUE SUBSTITUTE in tested surface; typed proposition/evidence peer reconstructs P1 |
| **P2** | [A2 / 00E](../00K-A2-P2-00E/README.md) | **13** | no TRUE SUBSTITUTE; bounded decision-relevant search reconstructs P2 |
| **P3** | [A3 / 00F](../00K-A3-P3-00F/README.md) | **15** | no TRUE SUBSTITUTE; explicit unresolved/non-permission closure reconstructs P3 |
| **P4** | [A4 / 00H](../00K-A4-P4-00H/README.md) | **29** | no TRUE SUBSTITUTE; A2-L root/delegation lineage reconstructs P4 |
| **P5** | [A5 / 00I](../00K-A5-P5-00I/README.md) | **14** | no TRUE SUBSTITUTE; full action-time material-basis compare reconstructs P5 |
| **P6** | [A6 / matched-authority 00G](../00K-A6-P6-00G/README.md) | **17** | no TRUE SUBSTITUTE in isolated surface; source-independence composition reconstructs P6 |

**Core regression surface: 101 tests.**

These 101 tests are not 101 independent proofs. They are the current regression
surface for six fixture-bounded ablation arguments.

## Supplemental falsification / anti-tailoring surface

| Package | Count | Purpose |
|---|---:|---|
| [A6a / original 00G F/G falsifier](../00K-A6a-P6-00G/README.md) | **10** | demonstrates that the unmodified F/G pair is confounded: authority-only is a TRUE SUBSTITUTE for that pair |
| [A6b / 00F P6 isolation](../00K-A6b-P6-00F/README.md) | **11** | re-tests P6 on shared-resource composition with local authority/freshness/determination held equal |
| [Independent cross-scenario kernels](../00K-cross-scenario-independent/README.md) | **6** | reimplements P4/P5/P6 kernels without importing A1–A6 helper code |

**Supplemental surface: 27 tests.**

**Full campaign surface: 128 tests.**

## Why the P6 falsifier belongs in the suite

A clean pass is not enough. The original 00G false/genuine pair changed two
variables at once: evidence independence and applicable transition authority.
A6a finds an authority-only TRUE SUBSTITUTE for that unmodified pair.

The canonical A6 harness therefore freezes authority equal across F/G and
isolates source dependence. A6b then tests the same composition principle on a
different failure family. See
[00K-A05 — P6 Confound Falsifier & Isolation Note](../../00K_A05_P6_CONFOUND_FALSIFIER_AND_ISOLATION_NOTE_v0.1.md).

This negative result is part of the evidence, not an exception to it.

## Run everything

From this directory:

```bash
python run_all.py
```

The runner executes each harness in its own working directory, checks the
expected regression count, and returns non-zero on any mismatch.

The repository workflow
[`00k-symbolic-ablations.yml`](../../../../../.github/workflows/00k-symbolic-ablations.yml)
runs the same fixture families on pushes and pull requests that touch 00K.

## Claim boundary

Passing this suite provides **deterministic symbolic evidence** that the current
principle formulations survive the declared fixture-level strongest-repair
tests. It does not establish universal minimality, real-world product failure,
or empirical superiority of Ecosystem Positioning.

A future repair that passes an isolated negative + positive-control fixture
without reconstructing the removed invariant is a valid TRUE SUBSTITUTE and
must reduce or overturn the corresponding necessity claim.
