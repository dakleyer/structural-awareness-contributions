# 00K Symbolic Ablation Suite

**Status:** executable deterministic/symbolic regression surface  
**Parent:** [00K — Six-Principle Sufficiency & Adversarial Ablation Test](../../00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md)

This directory is the execution router for the six principle-ablation harnesses.
It does not replace the individual fixture READMEs or execution records.

The [machine-readable principle manifest](./principle_manifest.json) freezes the
six semantic invariants, branch controls, expected counts and known confounds
used by the execution campaign. [`validate_manifest.py`](./validate_manifest.py)
checks that lock before CI runs the aggregate suite. The validator is a
meta-integrity gate and is **not counted** among the 163 ablation tests.

## Current core surface

| Principle | Fixture | Current regression count | Current bounded result |
|---|---|---:|---|
| **P1** | [A1 / 00J](../00K-A1-P1-00J/README.md) | **42** | original naive pair admits a source-authority TRUE SUBSTITUTE; corrected matched-semantic isolation finds no TRUE SUBSTITUTE in the serious repair surface; evidence→proposition→decision peer reconstructs P1 |
| **P2** | [A2 / 00E](../00K-A2-P2-00E/README.md) | **58** | matched-prefix late-resolution audit + serious TTL/circuit-breaker/parallel/scheduler/probe repairs; no TRUE SUBSTITUTE; viable finite stopping/fallback reconstructs P2 |
| **P3** | [A3 / 00F](../00K-A3-P3-00F/README.md) | **49** | old HOLD-marked base pair admits a shortcut TRUE SUBSTITUTE; corrected matched-conflict serious-repair surface finds no TRUE SUBSTITUTE; non-permission/containment semantics reconstruct P3 |
| **P4** | [A4 / 00H](../00K-A4-P4-00H/README.md) | **76** | minimal authority-qualification invariant survives; full lineage is not necessary in 00H because opaque scoped PDP/capability/maker-checker peers pass without exposing delegation history; P4 wording refined |
| **P5** | [A5 / 00I](../00K-A5-P5-00I/README.md) | **47** | all 16 declared basis-field subsets enumerated; partial compares/TTL/serialization/idempotency fail; full hash/vector/event/epoch peers reconstruct P5 |
| **P6** | [A6 / matched-authority 00G](../00K-A6-P6-00G/README.md) | **74** | transitive-dependency hardening: direct source count is partial; identity/org/confidence/time/content/quorum repairs fail; dependency-graph/effective-root peers reconstruct P6 |

**Core regression surface: 346 tests.**

These 346 tests are not 346 independent proofs. They are the current regression
surface for six fixture-bounded ablation arguments.

## Supplemental falsification / anti-tailoring surface

| Package | Count | Purpose |
|---|---:|---|
| [A6a / original 00G F/G falsifier](../00K-A6a-P6-00G/README.md) | **10** | demonstrates that the unmodified F/G pair is confounded: authority-only is a TRUE SUBSTITUTE for that pair |
| [A6b / 00F P6 isolation](../00K-A6b-P6-00F/README.md) | **11** | re-tests P6 on shared-resource composition with local authority/freshness/determination held equal |
| [Independent cross-scenario kernels](../00K-cross-scenario-independent/README.md) | **12** | independently reimplements P1–P6 kernels across a second scenario family without importing A1–A6 helper code |

**Supplemental surface: 33 tests.**

**Full campaign surface: 379 tests.**

Independent repository CI reproduction: the prior [**134/134 full campaign run**](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36100046965) remains a successful milestone. After P1 hardening, the workflow and manifest are configured for a **379-test** campaign; do not cite the older run as reproduction of the enlarged surface.

## Why the P6 falsifier belongs in the suite

A clean pass is not enough. The original 00G false/genuine pair changed two
variables at once: evidence independence and applicable transition authority.
A6a finds an authority-only TRUE SUBSTITUTE for that unmodified pair.

The canonical A6 harness therefore freezes authority equal across F/G and
isolates source dependence. A6b then tests the same composition principle on a
different failure family. See
[00K-A06 — P6 Confound Falsifier & Isolation Note](../../00K_A06_P6_CONFOUND_FALSIFIER_AND_ISOLATION_NOTE_v0.1.md).

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
