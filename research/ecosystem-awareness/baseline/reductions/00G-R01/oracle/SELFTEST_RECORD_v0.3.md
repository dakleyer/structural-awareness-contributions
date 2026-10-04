# R01 C02 neutral oracle — Stage-0 self-test record v0.3

**Executed:** 5 October 2026  
**Scope:** instrumentation only; no real technology executed.  
**Result:** **SELFTEST_PASS**

GitHub Actions run:
https://github.com/dakleyer/structural-awareness-contributions/actions/runs/37240286062

Head commit:
`dc6bb1c047293f42dc836c7a729053cb30924fff`

Workflow:
`.github/workflows/r01-audit-v2.yml`

The complete workflow concluded **success**. The R01 C02 neutral-oracle self-test step also concluded success.

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

All current controls reported **PASS**:

- two separately coded reference methods agree;
- deterministic replay reproduces the candidate trace hash;
- reversing case order preserves case results;
- neutral identifier permutation preserves substantive result;
- explicit oracle/private-field leak control is detected;
- malformed candidate output is rejected as a candidate-contract failure rather than infrastructure failure;
- malformed-record rejection does not contaminate a later valid run;
- permanent abstention is not accepted as success;
- tool-broker participant visibility and resource accounting remain separated from private adjudication;
- the interactive adapter → broker → sealed trace → private oracle path completes successfully;
- the interactive path reproduces the same deterministic candidate-trace hash.

Machine-readable record:
[`selftest_result_v0.3.json`](./selftest_result_v0.3.json)

## Nelson / UC-4 relationship

The control design reuses testbed patterns already demonstrated in Nelson Trasatti's UC-4 / Theme #13 Stage-0 work: frozen expectations, corrupted/malformed controls, deterministic replay and case-order checks.

Nelson source/result references are recorded in:
[`NELSON_BASELINE_IMPORT.md`](./NELSON_BASELINE_IMPORT.md)

This result **does not** mean UC-4 schema compatibility has been established. The bridge remains `R01-BRIDGE-DRAFT` until source-contributor review and exact schema validation are completed.

## Limits

This result establishes only that the current author-constructed instrumentation path executes consistently under the registered synthetic controls.

It does **not** establish:

- correctness of the complete R01 C-V evaluator;
- independent validation of either reference method;
- performance or suitability of a real technology;
- human-escalation cost or effectiveness;
- EA superiority;
- production scalability;
- FG-TIDA approval or adoption.
