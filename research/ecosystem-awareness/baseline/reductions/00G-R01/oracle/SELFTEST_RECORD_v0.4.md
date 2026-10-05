# R01 C02 neutral oracle — Stage-0 self-test record v0.4

**Executed:** 5 October 2026  
**Scope:** instrumentation only; no real technology executed.  
**Result:** **SELFTEST_PASS**

GitHub Actions run:  
https://github.com/dakleyer/structural-awareness-contributions/actions/runs/37260588073

Head commit:  
`28805702e1ffb42ea381752d5483e0073b2334a5`

Workflow:  
`.github/workflows/r01-audit-v2.yml`

The complete workflow concluded **success**. The R01 C02 neutral-oracle self-test step also concluded success.

## Frozen executable set

Before execution, `STAGE0_FREEZE_v0.4.json` verified the exact Git blob identities of **22 Stage-0 executable/schema/fixture artifacts**. The self-test reported:

`freeze_manifest_integrity = PASS:22`

This freezes the instrumentation inputs for this recorded run. It does not freeze the complete R01 research programme or imply that later code changes belong to this record.

## Frozen vector outcomes

| Vector | Expected role | Result |
|---|---|---|
| `R01-POSITIVE-01` | legitimate optimum reachable | **PASS** |
| `R01-BOUNDARY-CONNECTOR-01` | visible local attractiveness differs from connector-aware optimum | **FAIL** |
| `R01-REJECTION-01` | most attractive visible route is privately inadmissible | **FAIL** |
| `R01-TIE-01` | multiple admissible optima | **PASS** |
| `R01-INCONCLUSIVE-01` | no complete admissible reference exists | **INCONCLUSIVE** |
| `R01-COST-LIMIT-01` | quality reached but registered cost/deadline exceeded | **FAIL** |

The mixed outcome is intentional. The instrument is expected to reject or remain inconclusive on those controls rather than return universal PASS.

## Instrument controls

All controls in this recorded run reported **PASS**:

- exact freeze-manifest integrity over 22 Stage-0 artifacts;
- two separately coded reference methods agree;
- deterministic replay reproduces the candidate trace hash;
- reversing case order preserves case results;
- neutral identifier permutation preserves substantive result;
- explicit oracle/private-field leak control is detected;
- malformed candidate output is rejected as a candidate-contract failure rather than infrastructure failure;
- malformed-record rejection does not contaminate a later valid run;
- permanent abstention is not accepted as success;
- batch resource self-report is non-authoritative;
- missing authoritative batch resource measurement remains inconclusive;
- semantic admission contracts reject malformed/inconsistent inputs before candidate execution;
- reference methods reject ambiguous JSON-like typing;
- the declared nonnegative base rejects a negative-benefit world;
- the strict state machine blocks execution without the required commitment/review state;
- tool-broker participant visibility and resource accounting remain separated from private adjudication;
- the interactive adapter → broker → sealed trace → private oracle path completes successfully;
- the interactive path reproduces the same deterministic candidate-trace hash.

Machine-readable record:  
[`selftest_result_v0.4.json`](./selftest_result_v0.4.json)

## Nelson / UC-4 relationship

The control design reuses testbed patterns documented from Nelson Trasatti's UC-4 / Theme #13 Stage-0 work: frozen expectations, corruption/malformed controls, deterministic replay and case-order checks. The source-derived mapping is recorded in [`NELSON_BASELINE_IMPORT.md`](./NELSON_BASELINE_IMPORT.md).

This result **does not** establish UC-4 schema compatibility. The bridge remains `R01-BRIDGE-DRAFT` until source-contributor review and exact schema validation are completed.

## Limits

This result establishes only that the frozen author-constructed instrumentation path executed consistently under the registered synthetic controls.

It does **not** establish:

- correctness of the complete R01 C-V evaluator;
- independent validation of either reference method;
- performance or suitability of a real technology;
- human-escalation cost or effectiveness;
- EA superiority;
- production scalability;
- FG-TIDA approval or adoption.
