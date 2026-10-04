# Review request — R01 C02 ↔ Nelson UC-4

**Status:** ready for source-contributor review · not yet delivered through GitHub issue comment.

**Delivery attempt:** 4 October 2026. The configured GitHub integration returned `403 Resource not accessible by integration` when attempting to post to `FG-TIDA/use-cases#4`. This is a tooling/permission limitation; it is not a response from Nelson and does not change the review state.

Target:
https://github.com/FG-TIDA/use-cases/issues/4

Reviewer:
Nelson Trasatti / @T-n-Nelson

## Proposed message

@T-n-Nelson — I have started the first limited implementation of the R01 C02 neutral oracle/harness, using UC-4 as the primary testbed contract rather than creating a competing experiment format.

I treated UC-4 Requirements 22–24 as the main interoperability constraints: versioned adapters, frozen positive/boundary/rejection vectors with machine-readable outcomes, and a mutually agreed/version-pinned integration scope with source-contributor semantic review.

The current approach is deliberately a **R01-private sidecar** around the UC-4 experiment package. It contains only evaluator concerns that I do not think should become Theme #13 signal fields: private frozen-world reference, participant-view projection, R01 operation/cost/deadline contract, exact bounded reference methods, candidate-trace sealing before oracle evaluation, and separate evaluator/oracle accounting.

Current draft:
https://github.com/dakleyer/structural-awareness-contributions/tree/main/research/ecosystem-awareness/baseline/reductions/00G-R01/oracle

Interoperability profile:
https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/UC4_INTEROPERABILITY_PROFILE.md

Sidecar schema:
https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/schemas/r01_uc4_sidecar.schema.json

The current Stage-0 package is still only an instrumentation self-test, but it now contains six synthetic vectors (positive, connector boundary, rejection, tied optima, no-reference/inconclusive and cost/deadline failure), two separately coded exact reference paths, oracle-blind trace sealing, deterministic replay, case-order and identifier-permutation controls, malformed-record isolation, an abstention negative control, and an interactive adapter → tool broker → private oracle path. **No real technology or EA differential is claimed.**

The instrument self-test completed successfully in GitHub Actions:
https://github.com/dakleyer/structural-awareness-contributions/actions/runs/37240286062

Recorded result:
https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/SELFTEST_RECORD_v0.3.md

Before I call this UC-4-compatible, I would appreciate your correction on five points:

1. Would you prefer the R01-private evaluator fields to remain a linked sidecar, or to live under an extension object in your experiment package?
2. What is your preferred identity/reference mechanism for binding such a sidecar to the UC-4 experiment and test-vector ID?
3. Should the sealed pre-oracle candidate-trace hash sit in the common experiment record, adapter result, or an external evidence manifest?
4. How would you represent evaluator-only/oracle resource cost without contaminating the participant/comparator burden?
5. Do `PASS | FAIL | INCONCLUSIVE | INFRASTRUCTURE_ERROR` map cleanly to your expected-outcome semantics, or would you prefer another mapping?

I have kept the bridge at `R01-BRIDGE-DRAFT` and source-contributor review `PENDING` until you have had the opportunity to correct it. Once aligned, the next step would be to package this R01 Stage-0 profile against the pinned UC-4 schema, incorporate any corrections you make to the bridge, and only then admit real technologies through the same adapter/tool-broker boundary.

## Review disposition

- source_contributor: **PENDING**
- UC4-SOURCE-REVIEWED: **NO**
- UC4-SCHEMA-VALIDATED: **NO**
- Stage-0 admission beyond local instrumentation: **NO**
