# R01 C02 — neutral oracle / harness

<!-- DDS terminology revision 1 (2026-10-07): Stage A/B/C only; source scientific version and evidence unchanged. -->

> **DDS incorporation note — 7 October 2026.** This Oracle/harness work predates the canonical three-stage DDS split and retains its original C02, Stage-0, instrument and freeze identities. It is now incorporated into the [DDS Canonical Method Index](../../../../DDS_CANONICAL_METHOD_INDEX_v0.1.md) as **shared test-infrastructure qualification**, not as a separate method and not as a substantive Stage A/B/C result. The historical instrument/freeze labels (`0.3`, `0.4`, `0.7`, freeze `v0.9`) are versions of this Oracle artefact family; they are not DDS method/Stage versions. No old result is re-scored or upgraded by this incorporation. Stage-aware successor work reuses these controls while preserving the frozen v0.9 evidence.

**Status: limited implementation with a successful Stage-0 instrumentation self-test · 5 October 2026.** This directory implements the C02 instrument slice for R01. It compares a recorded candidate choice or execution with the best admissible route in a frozen world, using declared quality, resource and deadline conditions. The evaluator's private information is kept separate from the candidate's observations.

The design is deliberately **UC-4-first**. Nelson Trasatti's UC #4 testbed contribution is the primary interoperability target. R01 adds only the minimum private-world/reference machinery needed to evaluate the R01 scenario without redefining Theme #13, authority/delegation, human oversight or other contributor-owned semantics.

## Upstream sources and attribution

Primary source:

- Nelson Trasatti, **FG-TIDA UC #4 — Federated ecosystem defense across independently governed organizations**  
  https://github.com/FG-TIDA/use-cases/issues/4
- UC #4 experiment-cycle proposal and mapping approach  
  https://github.com/FG-TIDA/use-cases/issues/4#issuecomment-5846988611
- UC #4 candidate experiment input package v1.1.1 / schema 1.0.0  
  https://github.com/FG-TIDA/use-cases/issues/4#issuecomment-5847245589
- UC #4 experiment schema **1.1.0**, published in package **1.1.0-r1**, adding assessment time, consumed-determination reference, provenance, capabilities and separate review states  
  https://github.com/FG-TIDA/use-cases/issues/4#issuecomment-5871266911
- Theme #13 — Ecosystem-level Agent Defense  
  https://github.com/FG-TIDA/themes/issues/13
- Nelson's revised Theme #13 mapping v0.4.1-r1  
  https://github.com/FG-TIDA/themes/issues/13#issuecomment-5900725441
- Nelson's UC-6 / Theme #13 Stage-0 result (64 reference assertions plus corruption, malformed-record, replay and order controls)  
  https://github.com/FG-TIDA/themes/issues/13#issuecomment-5949120841

Corpus reuse:

- [R01 scenario §§1.4, 2.6, 2.15–2.17](../Escenario-creatividad-validacion.md)
- [Existing partial C3 oracle](../../../fixtures/00G-HF-ORACLE-v0.4/README.md)
- [Bounded oracle / fixture method](../../../00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md)
- [Deterministic harness pattern](../../../00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1.md)
- [Canonical Trace v1 source implementation](../../../fixtures/RS-00E-Q1a/canonical_trace_v1.py)

## Reuse of the existing corpus harnesses

R01 builds on an existing test corpus. Reuse must distinguish code or infrastructure already adapted, controls available for a new profile, and a mapping that has actually been tested and admitted. Prior results retain their original scenario, version and evidence scope.

| Existing source | Reusable part | Current R01 integration boundary |
|---|---|---|
| [RS-00E-Q1a](../../../fixtures/RS-00E-Q1a/README.md) | Canonical Trace v1, post-run evaluation, replay and instrumentation controls. | The serialization utility is adapted here; Q1a truth, scoring and shared-logic comparator results do not evaluate R01 routes. |
| [00K symbolic suite](../../../fixtures/00K-SUITE/README.md) | P1–P6 regressions, matched controls, ablations, strong-repair tests and retained falsifiers. | Keep the registered suite as a regression source; importing a control does not create an R01 outcome or a real-technology result. |
| [00L paired traversals](../../../00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/README.md) | Frozen facts, visible observations, prior rules, separate oracle, paired comparisons and requirement/gate traceability. | Normalize observations, dispositions and resource units through a reviewed profile; paper and symbolic results retain their scope. |
| [00I / S5 stateful harness](../../../fixtures/00I-STATEFUL/README.md) | Queue, source reads, guard, permit, executor, target-state observations and bounded recovery. | Candidate backend for a versioned R01/UC-4 adapter; no such admitted adapter or AWS execution is established by this reference. S5 effect expectations remain a specific evaluator. |
| [00G-HF development history](../../../annexes/00G-HF-DEVELOPMENT-HISTORY-v0.1.md) | Recorder, authority controls, episode/seed handling, social messages and dynamic schedules. | Preserve each runner's own oracle, policy and result scope; projection to R01 routes and collective measures requires a declared correspondence. |
| [Earlier R01 diagnostics](../feasibility/partial-experiments/README.md) | Small-world enumeration, budget/measurement countercontrols and historical counterexamples. | Revalidate against the current scenario and conditioned theorem; these are not the complete neutral R01 evaluator. |

The integration direction is a common experiment/trace boundary with versioned scenario backends and specific evaluators. It does not require rewriting the retained harnesses or merging their ground truths. Conventional controls that succeed retain that result.

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

The [v0.9 calibration record](./SELFTEST_RECORD_v0.9.md) has expected PASS outcomes for positive and tied-optimum controls, expected FAIL outcomes for connector-boundary, inadmissible-route and cost/deadline controls, and an expected INCONCLUSIVE outcome for the no-reference control. The self-test succeeds when each control returns its registered outcome.

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

Interpret results by their declared mode. A batch PASS checks the candidate's declared selection against a bounded reference and frozen measurements; it is not proof of an executed effect. The interactive instrumentation additionally checks matching environment execution evidence. Native `completion` and `legitimate_q` fields do not automatically establish the scenario's timely admissible-delivery metrics: the current evaluator checks deadline separately. Full scenario metrics and real-runtime isolation remain profile-specific verification obligations.

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

The self-test checks the instrument against author-constructed synthetic controls. Its reference implementations cross-check the declared synthetic trajectory and finite, nonnegative conjunctive DAG domains. C11 registers the evaluation profile; T03 evaluates a pinned real-technology implementation. Coverage of other R01 profiles and independent validation require their corresponding evidence.

### Next scoped successor decision

The completed documentary work on tasks1/2 retains its bounded receipt. Further tasks3–8 remain inactive until their own scope and decision. A prospective successor packet identifies: the exact UC4/source-schema edition and correspondence; one selected CTv1 profile and admitted clauses; clause → predicate → private reference → fail-capable/positive control mapping; attempted versus observed effect and operation/cost accounting; candidate/caller/private-state isolation; and the accepted adapter/broker/reset/resource/stop conditions.

Backend expansion is optional and separately scoped. Before any C11 registration/T03 admission or real execution, identify the selected reference, remaining schema/caller/isolation gaps and actual native evidence required. Calibration results remain calibration; the packet does not launch those tasks, reopen applied text or manufacture a technology result. The [existing plan review](./README_VNext.md) records the precise successor proposal and decision.



## Reading sequence from registration to result

Follow the record in the order in which its evidence is created:

| Step | Read | What it fixes |
|---|---|---|
| 1. Imported question and semantics | [UC-4 bridge](./UC4_INTEROPERABILITY_PROFILE.md) | Source/version, mapping, capabilities and distinct review states. |
| 2. Candidate and execution envelope | [Adapter guide](./TECHNOLOGY_ADAPTER_GUIDE.md) and [registration template](./REAL_TECHNOLOGY_REGISTRATION_TEMPLATE.json) | Implementation, native mapping, comparisons, resources, reset/cache and disclosure policy. |
| 3. Candidate visibility | [Isolation contract](./ISOLATION_CONTRACT.md) | What the candidate can access and the evidence for that runtime boundary. |
| 4. Actions and acceptance | [Tool broker](./TOOL_BROKER_CONTRACT.md) and [gate policy](./GATE_POLICY_CONTRACT.md) | Available operations, charges, durations, effects and frozen acceptance conditions. |
| 5. Evidence before and after evaluation | [Trace contract](./TRACE_CONTRACT.md) | Candidate/native evidence, attempted action, observed effect, pre-oracle seal and result seal. |
| 6. Instrument calibration | [v0.9 record](./SELFTEST_RECORD_v0.9.md), [result](./selftest_result_v0.9.json) and [freeze](./STAGE0_FREEZE_v0.9.json) | The published calibration of the instrument0.7 under freeze0.9, preserving each control's expected PASS, FAIL or INCONCLUSIVE outcome. |

Use the [DDS method index](../../../../DDS_CANONICAL_METHOD_INDEX_v0.1.md) for the study stage and its authoritative reference. C11 registers the selected campaign; T03 admits its pinned real-technology adapter. The registration template is completed and evidenced before that execution. The existing self-test records remain the calibration history of the instrument.
