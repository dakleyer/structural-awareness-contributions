# 00G-R01 oracle — status and pending verification

**5 October 2026 · In progress: still incomplete for 00G-R01. A limited neutral C02 implementation now exists.** This document records the candidate adaptation of the C3 instrument to the reduced scenario and the reuse-first direction for a neutral R01 oracle/harness. The new implementation is an instrumentation/testbed slice, not the complete C-V evaluator or an externally validated oracle, and no real technology has been executed through it.

[Back to 00G-R01, reduced scenario](../../reductions/00G-R01/README.md) · [Complete document, §3.7](../../reductions/00G-R01/Escenario-creatividad-validacion.md#37-relación-con-el-trabajo-previo-y-sus-recorridos) · [Foundation and proof of the reduction under review](../../reductions/00G-R01/README.md#fundamento-y-prueba-de-la-reducción).

## Preserved base and scope

The [original C3 v0.4](./README.md) preserves its code, documentation and [frozen fingerprints](./DESIGN_FREEZE.json). This status document is a later addition, outside that freeze; it does not redefine its predicates or results.

The isolated reproduction on 2 October verified the fingerprints and obtained 102 of 102 satisfactory constructed controls. That result checks the instrument in its original T0/X and T1/Y domain, operation `inspect`; it is not equivalent to executions with agents and does not verify its complete suitability for 00G-R01. The original first trial retains the pending integration, registration and execution items described in the README and the round-1 protocol.

## Limits before further design

This status file is deliberately **not** upgraded into a claim of a complete or validated oracle. The current work now includes a limited executable instrumentation layer under the R01 reduction, while the full evaluator, UC-4 source/schema admission and real-technology campaign remain open.

- The frozen C3 v0.4 package remains untouched.
- The 102/102 controls are controls of the retained C3 instrument in its own domain, not R01 technology runs.
- No full R01 optimum, collective result, real-runtime result or comparative EA result exists here.
- No candidate technology may receive hidden world labels, expected outputs, reference optimum or oracle state.
- If an exact R01 reference cannot be established within the registered bounded world, the correct status is `NOT_ESTABLISHED`/`INCONCLUSIVE`, not a guessed verdict.

## Reuse-first working direction

The preferred direction is to make the R01 oracle **small, neutral and adapter-based**, reusing established corpus/FG-TIDA test infrastructure by reference instead of rebuilding it inside this folder.

| Reusable source | Intended use for R01 | Limit |
|---|---|---|
| [C3 v0.4](./README.md) | Reuse only predicates whose projection into R01 is explicitly verified: identity, authority/applicability, commitment, attempt, effect, completion and timing where applicable. | C3 remains a partial instrument; it does not compute the R01 optimum, complete resource ledger or collective dynamics. |
| [00D-A01](../../00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md) | Bounded-oracle discipline, fixture admission, falsifiers, negative controls and staged evidence. | Reuse the test-design method, not scenario-specific truth. |
| [00D-A03](../../00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1.md) + [RS-00E-Q1a](../RS-00E-Q1a/README.md) | Thin harness architecture, Canonical Trace v1, instrumentation self-test, deterministic replay and post-run oracle evaluation. | Q1a semantics/results do not transfer to R01. |
| Nelson Trasatti, [FG-TIDA UC #4](https://github.com/FG-TIDA/use-cases/issues/4) | Versioned adapters for imported contracts (Req. 22), frozen positive/boundary/rejection vectors with machine-readable expected outcomes (Req. 23), and Stage-0 deterministic harness. | Reuse with attribution; no claim of FG-TIDA adoption or ownership transfer. |
| [Theme #13 charter preparation](../../../fg-tida/charter/THEME_13_WORKING_GROUP_CHARTER_PREPARATION_DRAFT_v0.2.md) | Bounded adapter and contributor-validation discipline for imported semantics; UC #4 / UC #6 mapping lineage. | Preserve contributor ownership and source semantics; do not silently reimplement them in the oracle core. |
| [00K harness families](../00K/README.md) | Anti-shortcut tests, no hidden-oracle access, positive/boundary controls and independent-method hardening. | Symbolic/fixture evidence only; not live technology validation. |

## Candidate R01 oracle shape — limited draft

The current preferred architecture is:

```text
frozen R01 world (private) ──> exact reference method A ──┐
                         └──> independent method B ───────┤
                                                         v
participant view ──> scenario adapter ──> technology adapter ──> sealed canonical trace
                                                              │
                                                              v
                                          post-run evaluator + registered gate policy
                                                              │
                                                              v
                                      scoped PASS / FAIL / INCONCLUSIVE / INFRA_ERROR
```

The technology adapter is the only implementation-specific layer. It can wrap an API/runtime, an agent framework, a workflow engine or a human-escalation process. The oracle core should not import vendor SDKs or encode a technology's internal reasoning.

### Separation of truth and observation

Maintain four separate records:

1. `world_truth`: frozen private R01 facts and labels;
2. `reference_truth`: independently computed admissibility, completion, effects and bounded optimum/ties;
3. `candidate_trace`: what the tested technology actually received, did, attempted, emitted and cost;
4. `evaluation`: post-run comparison under the frozen policy.

A candidate's own assessment never becomes `reference_truth`.

### Minimum portability contract

A versioned technology adapter should identify the technology/runtime, declare the observation schema and permitted tools, expose bounded invocation/finalization behavior, report timeout/refusal/infrastructure errors, and return resource use. Vendor-native evidence should be retained where possible; any normalization into the R01 canonical event schema must itself be versioned and tested.

### Minimum anti-circularity rules

- Oracle/reference files are unavailable to the technology adapter.
- Expected outcomes are unavailable during candidate invocation.
- Candidate trace is sealed before reference evaluation is loaded/applied.
- The reference optimum for the first implementation is produced by a small exhaustive method.
- Any faster/optimized reference method must agree with a separately implemented method on the shared bounded domain.
- Deny-all, accept-all and permanent-HOLD strategies require explicit negative controls and cannot pass merely by avoiding one failure.

### First bounded control family to build later

Before any real-technology campaign, the neutral harness should cover: a legitimate trajectory, an inadmissible execution, a detected/blocked alternative, an incomplete/abstaining run, a connector-changing optimum, a tie/boundary case, a nominal negative control, instrumentation self-tests, oracle-blindness, deterministic replay where applicable and second-method agreement.

The detailed design and accounting rules are maintained in [R01 — Computability, bounded execution and oracle work plan](../../reductions/00G-R01/COMPUTABILITY_AND_ORACLE_PLAN.md). This file remains the status/compatibility record for the existing partial oracle rather than a second implementation plan.


## Limited C02 implementation now available

The implementation is maintained at:

https://github.com/dakleyer/structural-awareness-contributions/tree/main/research/ecosystem-awareness/baseline/reductions/00G-R01/oracle

It currently contains:

- Nelson UC-4 / Theme #13 interoperability profile and source-attributed baseline;
- R01-private UC-4 sidecar schema;
- batch and interactive adapter contracts;
- Canonical Trace v1 reuse;
- two separately coded exact bounded reference paths;
- oracle-blind candidate-trace sealing;
- positive, boundary, rejection, tied-optimum, no-reference and cost/deadline controls;
- deterministic replay, case-order reversal and identifier-permutation checks;
- malformed-record isolation and permanent-abstention negative control;
- technology-neutral §2.6 tool broker with public versus private environment traces;
- real-technology registration template.

Nelson's published Stage-0 patterns are documented in [NELSON_BASELINE_IMPORT](../../reductions/00G-R01/oracle/NELSON_BASELINE_IMPORT.md). The pending source-contributor questions are in [NELSON_REVIEW_REQUEST](../../reductions/00G-R01/oracle/NELSON_REVIEW_REQUEST.md). A direct GitHub comment attempt could not be delivered because the configured integration lacks write access to the FG-TIDA repository; this is not a contributor response.

The tool-broker and evaluator controls are wired into the repository's R01 CI workflow. The latest successful instrumentation path uses `R01-C02-neutral-harness-0.7` under immutable `STAGE0_FREEZE_v0.9.json` and completed successfully in [GitHub Actions run 37265543867](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/37265543867), including verification of 30 frozen executable/schema/fixture dependencies. The [v0.9 evidence record](../../reductions/00G-R01/oracle/SELFTEST_RECORD_v0.9.md) remains instrumentation evidence only. This status record does **not** claim independent validation or a real-technology result.

## What is under verification and what remains

| Element | Status for 00G-R01 | Evidence needed to close it |
|---|---|---|
| Projection to C3 | Pending definition and verification | Explicit correspondence preserving identity, authority, applicability, scope, commitment, attempt, effect and timing, with positive and negative controls. If it loses a material distinction, a versioned successor is required. |
| Admissible optimum and quality | Bounded Stage-0 reference implemented; complete C-V evaluator still pending | The current oracle has two exact bounded reference paths for the registered synthetic Stage-0 bundle. Full scenario coverage, additional profile semantics and independent external review remain open. |
| Search, validation and coordination costs | Partial instrumentation implemented; full R01 ledger still pending | The Stage-0 harness/tool broker records bounded operational cost, timing and separate evaluator/oracle accounting, including negative controls against candidate self-report. Full discards, reuse, maintenance, coordination and campaign-scale accounting remain open. |
| Social mediation and membership in 00G | Application of the reduction under review | Realizable trace and correspondence with §3.5, preservation of the relational predicate and positive control. A C3 PASS does not decide membership in 00G. |
| Experimental integration | Instrumentation self-test only; real-technology integration pending | The current instrument `0.7` under freeze `v0.9` has executed successfully on synthetic Stage-0 controls. A real implementation still requires fixed resources and budgets, registered adapter/profile, isolation evidence, recorder/native evidence, traces and prior campaign registration. |
| Collective and statistical evaluation | Pending | Predefined metrics, size and analysis. `population_result=NOT_ASSESSED` is not collective approval. |
| EA comparison | Candidate; no result of its own | Implementation and controlled comparison under common criteria, allowing favorable, adverse or indeterminate results. |

The obligations above remain open. The recorded Stage-0 instrumentation self-test is not a real-technology experiment, human calibration or comparative EA campaign. Documentary closure of links and synthetic instrument checks do not constitute closure of those tests.

## Relation to the reduction proof

The [00G-R01 foundation section](../../reductions/00G-R01/README.md#fundamento-y-prueba-de-la-reducción) links the prior one-way argument, its review and the obligations of the C-V-G specialization. The reduction proof and oracle validation are related but distinct tasks: one checks which relations are preserved; the other checks which decisions the instrument can evaluate correctly.
