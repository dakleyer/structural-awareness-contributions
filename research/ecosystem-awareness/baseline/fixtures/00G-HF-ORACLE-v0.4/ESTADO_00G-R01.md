# 00G-R01 oracle — status and pending verification

**4 October 2026 · In progress: still incomplete for 00G-R01. Limited design work has started.** This document records the candidate adaptation of the C3 instrument to the reduced scenario and the reuse-first direction for a neutral R01 oracle/harness. It does not declare the complete C-V evaluator implemented or validated, and no real technology has been executed through it.

[Back to 00G-R01, reduced scenario](../../reductions/00G-R01/README.md) · [Complete document, §3.7](../../reductions/00G-R01/Escenario-creatividad-validacion.md#37-relación-con-el-trabajo-previo-y-sus-recorridos) · [Foundation and proof of the reduction under review](../../reductions/00G-R01/README.md#fundamento-y-prueba-de-la-reducción).

## Preserved base and scope

The [original C3 v0.4](./README.md) preserves its code, documentation and [frozen fingerprints](./DESIGN_FREEZE.json). This status document is a later addition, outside that freeze; it does not redefine its predicates or results.

The isolated reproduction on 2 October verified the fingerprints and obtained 102 of 102 satisfactory constructed controls. That result checks the instrument in its original T0/X and T1/Y domain, operation `inspect`; it is not equivalent to executions with agents and does not verify its complete suitability for 00G-R01. The original first trial retains the pending integration, registration and execution items described in the README and the round-1 protocol.

## Limits before further design

This status file is deliberately **not** upgraded into a claim of an implemented oracle. The current work is architecture preparation only.

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


## What is under verification and what remains

| Element | Status for 00G-R01 | Evidence needed to close it |
|---|---|---|
| Projection to C3 | Pending definition and verification | Explicit correspondence preserving identity, authority, applicability, scope, commitment, attempt, effect and timing, with positive and negative controls. If it loses a material distinction, a versioned successor is required. |
| Admissible optimum and quality | C-V evaluator pending implementation | Frozen map, admissibility rules and exact optimum check according to scenario §2.17. |
| Search, validation and coordination costs | Pending | Cost ledger including discards, reuse, maintenance and time; consistency checks before comparing configurations. |
| Social mediation and membership in 00G | Application of the reduction under review | Realizable trace and correspondence with §3.5, preservation of the relational predicate and positive control. A C3 PASS does not decide membership in 00G. |
| Experimental integration | Pending | Identified implementation, fixed resources and budgets, recorder, traces and prior registration of the trial. |
| Collective and statistical evaluation | Pending | Predefined metrics, size and analysis. `population_result=NOT_ASSESSED` is not collective approval. |
| EA comparison | Candidate; no result of its own | Implementation and controlled comparison under common criteria, allowing favorable, adverse or indeterminate results. |

The obligations above remain open; no experimental verifications are claimed to be in execution. Documentary closure of links does not constitute closure of these tests.

## Relation to the reduction proof

The [00G-R01 foundation section](../../reductions/00G-R01/README.md#fundamento-y-prueba-de-la-reducción) links the prior one-way argument, its review and the obligations of the C-V-G specialization. The reduction proof and oracle validation are related but distinct tasks: one checks which relations are preserved; the other checks which decisions the instrument can evaluate correctly.
