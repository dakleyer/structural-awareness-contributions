# 00K-A5 — P5 / 00I deterministic symbolic ablation

**Removed principle:** P5 — material-change requalification at time of use  
**Scenario:** 00I — *The Patch That Undid the Fix*  
**Status:** deterministic symbolic fixture execution; not a live system or product benchmark

## Question

Can P1/P2/P3/P4/P6 plus strong native controls keep a previously valid queued action correct after the world changes **without** reconstructing P5's invariant: compare/requalify the decision basis at use time when a material condition changes?

## Frozen branch pair

- **Continuity:** incident/config/freeze/source basis remains the same as when Patch A was qualified → must execute.
- **Stale branch:** Patch B / incident resolution / freeze / generation change makes Patch A's old basis stale → must requalify rather than execute.
- **Unavailable-current-source control:** current state cannot be established → bounded HOLD, not silent execution.

The queued Patch A object, original grant and original decision basis are identical on continuity and stale branches. The declared material difference exists in **current state at use time**.

## Tested repairs

- queue-time-only decision;
- stricter original-basis qualification (P1);
- provenance/intervention preservation without applicability reopening (P4);
- conflict visibility without applicability reopening (P6);
- native serialization only;
- deny-all;
- native generation/version compare.

## Result

The suite passes **14/14** after additive material-basis grid hardening.

The first five P5-blind repairs false-continue the stale branch or cannot discriminate it from continuity. Deny-all blocks the stale branch but fails the continuity positive control.

The original native **generation-only** compare passes the first stale branch, but the grid shows that it is only a partial repair: it misses incident-only, freeze-only and source/policy-version-only changes when the configuration generation is unchanged.

The strengthened peer in `p5_strong_peer.py` binds actuation to the **full declared material decision basis** and reopens qualification on any material mismatch. Under 00K this is **SEMANTIC RECONSTRUCTION of P5**.

No TRUE SUBSTITUTE is established by this fixture execution.

## Re-run

```bash
python -m pytest -q
```

## Boundary

This is a deterministic symbolic execution over a frozen 00I abstraction. It does not prove universal P5 necessity and it does not test AWS, Step Functions, RDS or any other product. A future repair that passes continuity + stale + unavailable-source controls without action-time requalification or an operationally equivalent current-state binding is a valid counterexample.


## Serious-repair hardening — exhaustive material-basis subsets

The additive hardening layer is maintained in:

- [`p5_serious_repairs.py`](./p5_serious_repairs.py)
- [`test_p5_serious_repairs.py`](./test_p5_serious_repairs.py)
- [00K-A11 — P5 Exhaustive Material-Basis Ablation](../../00K_A11_P5_EXHAUSTIVE_MATERIAL_BASIS_ABLATION_v0.1.md)

It enumerates **all 16 subsets** of the declared four-field material basis
(`generation`, `incident_open`, `freeze_active`, `source_version`).

Only the full declared material basis passes continuity, unavailable-source and
all single-field mutation branches. Queue-age TTL, serialization, idempotency
and human reapproval without fresh state remain insufficient; cancel-on-any-event
overblocks irrelevant changes.

Compressed conventional mechanisms — full state hash, version vector, complete
material-event invalidation or material epoch — can pass, but only if they track
the same full material basis. They are therefore alternative implementations of
P5, not TRUE SUBSTITUTES.

Additive execution:

```text
33 passed
```

Current A5 total:

```text
47 tests
```


## Serious-repair hardening — exhaustive material basis

The additive serious-repair layer is maintained in:

- [`p5_serious_repairs.py`](./p5_serious_repairs.py)
- [`test_p5_serious_repairs.py`](./test_p5_serious_repairs.py)
- [00K-A11 — P5 Exhaustive Material-Basis Ablation](../../00K_A11_P5_EXHAUSTIVE_MATERIAL_BASIS_ABLATION_v0.1.md)

It enumerates all **16 subsets** of the four declared material basis fields:
`generation`, `incident_open`, `freeze_active`, and `source_version`.

Only the full set passes continuity, unavailable-source handling and every
single-field material-change branch. TTL, serialization, idempotency, human
reapproval without current facts and partial compares all fail at least one
branch. Full state hashes, version vectors, material epochs and complete event
invalidation pass only when they cover the same full material basis, so they are
classified as **SEMANTIC RECONSTRUCTION of P5**.

Additive layer: **33 tests**.  
Current A5 total: **47/47**.
