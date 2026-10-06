# 00K-A11 — P5 Exhaustive Material-Basis Ablation — v0.1

**Parent:** [00K — Six-Principle Sufficiency & Adversarial Ablation Test](./00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md)  
**Principle:** P5 — material-change requalification at time of use  
**Scenario:** [00I — The Patch That Undid the Fix](./00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_FREEZE_EDITION.md)  
**Status:** serious-repair hardening executed  
**Date:** 25 September 2026

> **Finding.** The first A5 grid already exposed generation-only compare as a partial repair. The strengthened test now enumerates **all 16 subsets** of the four declared material basis fields — generation, incident state, freeze state and source/policy version. Only the full declared material basis passes continuity, unavailable-source and every single-field material-change branch. Conventional compressed implementations such as a state hash, version vector, material epoch or event invalidation can pass, but only if they change on the same complete material basis. They are therefore alternative implementations of P5, not substitutes for the invariant.

---

## 1. Why this is stronger than one stale branch

A stale-action test can be accidentally easy if several fields change at once. A generation compare, for example, appears sufficient if every material change also increments generation.

00I already identified this weakness. The new executable layer turns it into an exhaustive reduced model:

```text
material basis =
    generation
    incident_open
    freeze_active
    source_version
```

For each subset of those fields, the harness asks:

1. does continuity still execute?
2. does source unavailability avoid silent execution?
3. does each one-field material mutation reopen qualification?

There are `2^4 = 16` possible field subsets.

Only the full set passes all three requirements.

---

## 2. Serious alternatives tested

The hardening includes:

- every partial/full subset of current-state checks;
- queue-age TTL;
- transaction serialization;
- idempotency;
- human reapproval without fresh state;
- cancel-on-any-event;
- material-event invalidation;
- full state-hash compare;
- version-vector compare; and
- a monotonic material epoch.

The important distinctions are:

### Queue age / TTL

Continuity and stale branches may have exactly the same age. A TTL can therefore:

- allow both; or
- block both.

It does not identify material semantic change.

### Serialization and idempotency

They can make execution technically clean and still execute the obsolete action perfectly after the newer repair.

### Human reapproval without current facts

A new signature is authorization, not evidence that the old decision basis remains current.

### Cancel on any event

This catches material changes only by also invalidating irrelevant changes. It fails the positive-control precision requirement.

### Event invalidation / state hash / version vector / epoch

These mechanisms can pass efficiently. But to pass the full mutation grid they must encode **every declared material basis dimension** and trigger requalification on mismatch.

That is an operationally compressed **SEMANTIC RECONSTRUCTION of P5**.

---

## 3. Execution result

The additive serious-repair layer contributes:

> **33/33 passing tests**

Together with the existing A5 base + grid (**14**):

> **current A5 total: 47/47 symbolic tests**

A particularly useful executable result is:

```text
all 16 material-field subsets enumerated
only {generation, incident_open, freeze_active, source_version}
passes the complete material-change grid
```

No partial subset is a TRUE SUBSTITUTE.

---

## 4. Current P5 disposition

- **TRUE SUBSTITUTE found:** none in the serious-repair surface.
- **Partial repairs found:** many, including generation-only compare.
- **Strong passing peers:** full state hash, version vector, complete event invalidation map, material epoch.
- **Why they pass:** they bind actuation to the current value of the full declared material decision basis.
- **00K classification:** **SEMANTIC RECONSTRUCTION of P5**.
- **Evidence level:** deterministic symbolic fixture.

This remains architecture-neutral. P5 does not require a literal four-field comparison. A compact epoch/hash/event contract is acceptable if it is demonstrated to cover the same material state.

---

## 5. Falsifier

P5 must be reopened if a repair can:

1. execute unchanged continuity;
2. stop/requalify every declared material single-field change;
3. avoid silent execution when current state is unavailable;
4. avoid invalidating irrelevant changes indiscriminately; and
5. do all of that without comparing, binding, invalidating from or otherwise representing the current material decision basis or an operational equivalent.

Such a mechanism is a **TRUE SUBSTITUTE**.

---

## 6. Audit clarification — 6 October 2026

The phrase **“all 16 subsets”** means the complete `2^4` power set of inclusion/omission configurations for the four declared material-basis fields, including the empty and full sets. It does **not** claim exhaustive coverage of field values, temporal orderings, timestamps, latency regimes or the space of all possible repair algorithms.

The **47/47** headline is a regression/check count. It means 47 pytest checks matched their frozen expected outcomes; it does not mean that 47 candidate defences succeeded. The serious-repair layer intentionally includes expected rejections and false-continuation demonstrations.

Field attribution in the 16-subset grid is structurally isolated: every `MUTATIONS[field]` branch changes exactly one material field and keeps the other declared basis fields at the continuity value. Accordingly, the grid does not infer field attribution from the original stale branch where several facts change together.

A machine-readable [fixture contract](./fixtures/00K-A5-P5-00I/fixture_spec.json) and [agreement validator](./fixtures/00K-A5-P5-00I/validate_fixture_spec.py) now guard the reduced branch oracle against silent code/spec drift. This is a meta-integrity control and is not added to the 47/379 counts. It also does not claim independent adjudication: the expected contract remains part of the same research corpus.

Finally, event-invalidation and material-epoch repairs are **conditional compressed mechanisms** in this symbolic surface. Their passing result assumes the event/epoch representation actually changes on every declared material change; a real implementation must establish that mapping separately.

