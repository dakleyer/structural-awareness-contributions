# Nelson UC-4 / Theme #13 baseline reused by R01

Source-derived interoperability note · 4 October 2026.

This note records which **testbed patterns** R01 is reusing from Nelson Trasatti's UC-4 work. It does not import UC-6 authority semantics into R01 and does not claim ownership of Nelson's testbed contribution.

## Source lineage

UC-4 definition and progressive testbed:
https://github.com/FG-TIDA/use-cases/issues/4

Nelson's Theme #13 boundary confirmation:
https://github.com/FG-TIDA/themes/issues/13#issuecomment-5639226397

Candidate UC-4 input package:
https://github.com/FG-TIDA/use-cases/issues/4#issuecomment-5847245589

Public experiment schema 1.1.0-r1:
https://github.com/FG-TIDA/use-cases/issues/4#issuecomment-5871266911

Theme #13 mapping draft v0.4.0-r1:
https://github.com/FG-TIDA/themes/issues/13#issuecomment-5872258540

Revised Theme #13 mapping v0.4.1-r1:
https://github.com/FG-TIDA/themes/issues/13#issuecomment-5900725441

Stage-0 result:
https://github.com/FG-TIDA/themes/issues/13#issuecomment-5949120841

## What Nelson has already established within his declared Stage-0 scope

According to the published result record:

- all **64 reference assertions pass**;
- G1 remains unchanged while the B branch remains contextually inapplicable after human approval;
- two deliberately corrupted applicability values are detected;
- a malformed-record control rejects one record while preserving the other three;
- replay reproduces the same result hash;
- removing the agent-ID mapping exposes four missing outputs;
- reversing case order preserves assertion values and statuses by case ID;
- six recorded runs were reproduced offline.

These are Nelson's UC-6 / Theme #13 calibration results. They are **not R01 results**.

## Testbed patterns R01 should reuse

| Nelson pattern | R01 reuse | R01-specific extension |
|---|---|---|
| Source facts and expected outcomes are frozen separately from the mapping under test. | Candidate receives only participant-visible facts; expected/reference truth remains oracle-side. | Private R01 world contains admissibility and exact trajectory facts unavailable to the adapter. |
| Versioned adapter consumes source semantics without owning them. | All real technologies enter R01 through a versioned adapter. | Adapter also reports R01 operational cost/latency under the registered resource contract. |
| Explicit determination reference and assessment time. | Sidecar carries assessment time and consumed determination references. | R01 uses those references only as supplied inputs; it may not recalculate another Theme's authority/oversight determination. |
| Positive, boundary and rejection cases. | First R01 fixture family uses those three classes. | R01 adds connector-changing optimum and tied-optimum controls. |
| Corrupted-value controls. | R01 must include deliberate private-field/expected-outcome leak controls and later semantic corruption controls for imported determinations. | The current first self-test checks oracle-blindness; semantic imported-determination corruption follows when a real UC-4 profile is admitted. |
| Malformed record is rejected without corrupting valid records. | Adapter-result validation is isolated per test vector. | A malformed candidate contract becomes an explicit rejected/failed vector, not evidence about another vector. |
| Replay reproduces the same hash. | R01 reuses Canonical Trace v1 and requires identical candidate-trace hash for deterministic replay. | Stochastic technologies later require registered seeds/distributions rather than byte identity. |
| Agent-ID sensitivity exposes missing outputs. | Required bindings must fail explicitly rather than disappear silently. | R01 will extend this to task, principal, mandate, scope/version and connector/evidence bindings as each profile requires. |
| Case-order reversal preserves result by case ID. | Stage-0 verifier runs a reverse-order metamorphic check. | Later stateful technologies must declare reset/cache policy before this invariant is expected. |
| Reference calibration remains stable while later operational experiments are scoped separately. | C02 instrument controls are frozen separately from C11/T03 campaigns. | Material change → requalification → attempted action → observed effect remains a later R01/UC-4 operational profile. |

## Boundary retained

Nelson explicitly keeps the supplied applicability determination, contextualization, authorization and execution distinct. The current calibration does not add an EA authority calculation, measured response window or executed requalification loop.

R01 adopts the same boundary. Its oracle can adjudicate the R01 synthetic world after execution, but EA does not become the owner of authority, delegation, oversight or other imported determinations.

## Current gap

The binary UC-4 attachment containing the exact schema/package is not accessible through the configured GitHub connector's supported file actions. Therefore the R01 bridge remains **semantic/source-aligned but not yet UC4-schema-validated**. No byte-level import or validator-pass claim is made.
