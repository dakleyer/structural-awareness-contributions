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


## Mathematical supplement — matched blind-signature pair

The [blind-signature proof supplement](../00K-FORMAL/p5-blind-signature/README.md) preserves the compact STALE/FRESH construction supplied during the formalization work.

It proves the projection-separation result directly: STALE and FRESH are identical on token validity, scope and elapsed time but require opposite dispositions because the current material condition differs. No deterministic policy restricted to that blind surface can classify both correctly.

The supplement passes **18/18** tests but is deliberately **not counted** in the canonical P5 total (**47/47**) or the registered 00K campaign (**379/379**). Its role is mathematical readability; A11 remains the stronger exhaustive operational P5 audit.

## Audit clarification — 6 October 2026

This section records a third-party-review clarification. It does not change the frozen P5 invariant, the 47-test canonical count, or any historical result.

1. **What 47/47 means.** The number is a pytest regression count: 47 declared checks produced their expected outcome. Some checks expect EXECUTE, some REQUALIFY/HOLD, and some expect a candidate repair to fail a branch. It is not “47 successful defences”, 47 independent experiments, or product evidence.
2. **What is exhaustive.** The 16-case claim is exhaustive only over the inclusion/omission power set of the four declared material-basis fields `generation`, `incident_open`, `freeze_active`, and `source_version` in this reduced model. It is not exhaustive over each field's value domain, temporal ordering, timestamps, latency, or all possible repair algorithms.
3. **Attribution in the serious grid.** The single-field mutation branches change exactly one declared material field while keeping the other declared basis fields fixed. Therefore a full-basis REQUALIFY on those branches is attributable to the sole changed field by construction. This is not a stage-tagged mutation-kill framework like the S5 harness; the original multi-change stale branch is not used to infer which individual field caused requalification.
4. **Specification agreement.** [`fixture_spec.json`](./fixture_spec.json) records the reduced branch oracle separately from the implementation functions, and [`validate_fixture_spec.py`](./validate_fixture_spec.py) checks code/spec agreement as a meta-integrity control. It prevents silent spec/code drift but does not constitute independent human adjudication because the corpus remains author-produced.
5. **Compressed peers are conditional models.** State-hash, version-vector, event-invalidation and material-epoch peers count as passing only under the explicit condition that their compressed representation changes on every declared material-basis change. The symbolic tests do not establish that a real product's epoch/event source satisfies that condition.
6. **Blind-signature supplement.** The STALE/FRESH blind-signature package is executed in CI as a separate mathematical certificate and remains excluded from both the 47 canonical P5 checks and the 379 registered 00K campaign.

The CI cross-version/hash-seed replays are reproducibility checks, not additional scientific test cases.

