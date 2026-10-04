# R01 C02 — neutral oracle / harness

**Status: limited implementation + successful Stage-0 instrumentation self-test · 5 October 2026.** This directory contains the executable C02 instrument slice requested for R01. It is not a real-technology campaign, not an externally validated oracle, and not an FG-TIDA deliverable.

The design is deliberately **UC-4-first**. Nelson Trasatti's UC #4 testbed contribution is the primary interoperability target. R01 adds only the minimum private-world/reference machinery needed to evaluate the R01 scenario without redefining Theme #13, authority/delegation, human oversight or other contributor-owned semantics.

## Upstream sources and attribution

Primary source:

- Nelson Trasatti, **FG-TIDA UC #4 — Federated ecosystem defense across independently governed organizations**  
  https://github.com/FG-TIDA/use-cases/issues/4
- UC #4 experiment-cycle proposal and mapping approach  
  https://github.com/FG-TIDA/use-cases/issues/4#issuecomment-5846988611
- UC #4 candidate experiment input package v1.1.1 / schema 1.0.0  
  https://github.com/FG-TIDA/use-cases/issues/4#issuecomment-5847245589
- UC #4 public experiment schema 1.1.0-r1, adding assessment time, consumed-determination reference, provenance, capabilities and separate review states  
  https://github.com/FG-TIDA/use-cases/issues/4#issuecomment-5871266911
- Theme #13 — Ecosystem-level Agent Defense  
  https://github.com/FG-TIDA/themes/issues/13
- Nelson's revised Theme #13 mapping v0.4.1-r1  
  https://github.com/FG-TIDA/themes/issues/13#issuecomment-5900725441
- Nelson's UC-6 / Theme #13 Stage-0 result (64 reference assertions plus corruption, malformed-record, replay and order controls)  
  https://github.com/FG-TIDA/themes/issues/13#issuecomment-5949120841

Corpus reuse:

- R01 scenario §§1.4, 2.6, 2.15–2.17: ../Escenario-creatividad-validacion.md
- Existing partial C3 oracle: ../../../fixtures/00G-HF-ORACLE-v0.4/README.md
- Bounded oracle / fixture method: ../../../00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md
- Deterministic harness pattern: ../../../00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1.md
- Canonical Trace v1 source implementation: ../../../fixtures/RS-00E-Q1a/canonical_trace_v1.py

## Interoperability rule

R01 does **not** fork Nelson's experiment contract. The intended composition is:

```text
UC-4 experiment package
  common experiment metadata
  source/version/review/capability declarations
  one or more attributed adapters
  frozen positive / boundary / rejection cases
             |
             +--> R01 sidecar (this directory)
                    private world reference
                    participant-view projection
                    R01 operation/cost contract
                    exact reference methods
                    candidate trace seal
                    post-run R01 evaluation
```

Until Nelson's schema package itself is vendored or directly consumed, this directory claims **semantic alignment**, not byte-level/schema-validator compatibility. The bridge is documented in [UC4_INTEROPERABILITY_PROFILE.md](./UC4_INTEROPERABILITY_PROFILE.md).

## Executed self-test evidence

The current instrument was executed in the repository CI and its complete workflow concluded **success**:

https://github.com/dakleyer/structural-awareness-contributions/actions/runs/37240286062

Evidence:
- [Stage-0 self-test record v0.3](./SELFTEST_RECORD_v0.3.md)
- [Machine-readable result v0.3](./selftest_result_v0.3.json)

This is evidence about the **instrumentation path**, not about any real technology.

## What is executable now

The current Stage-0 self-test is intentionally small and now reuses several control patterns already demonstrated in Nelson's Stage-0 calibration. It verifies that the harness can:

1. keep private admissibility and optimum data out of the adapter view;
2. invoke an adapter before computing/loading the reference result;
3. seal a candidate trace before post-run evaluation;
4. enumerate a finite R01 world exactly;
5. recompute the same reference through a separate implementation path;
6. distinguish positive, boundary and rejection fixtures;
7. retain operational cost separately from oracle/evaluator work;
8. detect permanent abstention as non-completion rather than treating it as safe success;
9. reject a malformed adapter record explicitly without contaminating valid records;
10. reproduce the same sealed candidate hash on deterministic replay;
11. preserve case results under case-order reversal;
12. preserve substantive results when neutral trajectory identifiers are permuted;
13. return `INCONCLUSIVE` when a bounded reference cannot be established rather than manufacturing truth;
14. expose the §2.6 operation surface through a bounded [tool broker](./TOOL_BROKER_CONTRACT.md), keeping participant-visible and private environment traces separate.

Run locally from this directory:

```sh
python3 verify.py
```

The bundled adapter is an **instrumentation self-test only**. It is not a product, agent, conventional comparator, EA implementation or human-escalation implementation.

## Directory

```text
oracle/
  README.md
  UC4_INTEROPERABILITY_PROFILE.md
  NELSON_BASELINE_IMPORT.md
  NELSON_REVIEW_REQUEST.md
  TOOL_BROKER_CONTRACT.md
  TECHNOLOGY_ADAPTER_GUIDE.md
  REAL_TECHNOLOGY_REGISTRATION_TEMPLATE.json
  SELFTEST_RECORD_v0.3.md
  selftest_result_v0.3.json
  adapter_api.py
  canonical_trace_v1.py
  reference.py
  reference_secondary.py
  harness.py
  interactive_harness.py
  tool_broker.py
  verify.py
  schemas/
    r01_uc4_sidecar.schema.json
  adapters/
    selftest_adapter.py
    malformed_selftest_adapter.py
    abstain_selftest_adapter.py
    interactive_selftest_adapter.py
  fixtures/stage0/
    experiment_sidecar.json
    worlds.json
    expected_selftest.json
    tool_profile.json
    interactive_tool_profile.json
    interactive_case.json
```

## Claim boundary

A passing self-test means only that this first instrument path behaves as specified on author-constructed synthetic controls. It does not establish the correctness of the complete R01 C-V evaluator, scalability, statistical performance, an EA differential or suitability of any real technology. C11 registration and T03 real-technology execution remain later gates.
