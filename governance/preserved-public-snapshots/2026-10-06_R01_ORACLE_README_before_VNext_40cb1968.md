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

The current instrument `R01-C02-neutral-harness-0.7` was executed under immutable freeze `v0.9`, and the complete repository workflow concluded **success**:

https://github.com/dakleyer/structural-awareness-contributions/actions/runs/37265543867

Current recorded evidence:
- [Stage-0 self-test record v0.9](./SELFTEST_RECORD_v0.9.md)
- [Machine-readable result v0.9](./selftest_result_v0.9.json)
- [Frozen executable-set manifest v0.9](./STAGE0_FREEZE_v0.9.json)

The v0.3, v0.4 and v0.7 records and the predecessor freeze manifests remain preserved as historical instrumentation evidence for their own runs. They are not rewritten to match the current instrument. None of these records is evidence about a real technology.

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
14. expose the §2.6 operation surface through a bounded [tool broker](./TOOL_BROKER_CONTRACT.md), keeping participant-visible and private environment traces separate;
15. verify the exact Git blob identities of the 30 frozen Stage-0 executable/schema/fixture artifacts before execution;
16. reject malformed or semantically inconsistent Stage-0 inputs before candidate execution;
17. treat harness-observed batch resources as authoritative rather than trusting candidate self-report;
18. enforce the declared review/commitment execution state in the strict interactive profile;
19. require the frozen gate policy to match the sidecar and reject a mismatched policy;
20. reject hidden batch selections and candidate use of oracle-reserved truth namespaces before oracle evaluation;
21. preserve message lineage and relay provenance while rejecting duplicate message identifiers;
22. reject an unrelated mandate, consume commitments on execution and invalidate stale reviews;
23. commit private environment evidence separately and defer its release from the candidate path;
24. cross-check fixed graph controls and 64 generated DAGs with exhaustive and dynamic-programming references;
25. keep the declared nonnegative base and reject ambiguous reference types; and
26. reject incomplete or oracle-visible T03 registrations while admitting a synthetically complete isolated registration control.

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
  GATE_POLICY_CONTRACT.md
  TRACE_CONTRACT.md
  ISOLATION_CONTRACT.md
  REAL_TECHNOLOGY_REGISTRATION_TEMPLATE.json
  SELFTEST_RECORD_v0.9.md
  selftest_result_v0.9.json
  STAGE0_FREEZE_v0.9.json
  SELFTEST_RECORD_v0.7.md
  SELFTEST_RECORD_v0.4.md
  SELFTEST_RECORD_v0.3.md
  STAGE0_FREEZE_v0.4.json ... STAGE0_FREEZE_v0.8.json
  adapter_api.py
  canonical_trace_v1.py
  contracts.py
  integrity.py
  real_admission.py
  reference.py
  reference_secondary.py
  reference_graph_exhaustive.py
  reference_graph_dp.py
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
    misreport_cost_selftest_adapter.py
    hidden_selection_selftest_adapter.py
    reserved_truth_selftest_adapter.py
    interactive_selftest_adapter.py
  fixtures/stage0/
    experiment_sidecar.json
    worlds.json
    expected_selftest.json
    gate_policy.json
    graph_reference_controls.json
    tool_profile.json
    interactive_tool_profile.json
    interactive_case.json
```

## Claim boundary

A passing self-test means only that this first instrument path behaves as specified on author-constructed synthetic controls. It does not establish the correctness of the complete R01 C-V evaluator, scalability, statistical performance, an EA differential or suitability of any real technology. C11 registration and T03 real-technology execution remain later gates.
