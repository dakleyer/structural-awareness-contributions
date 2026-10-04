# 00G-R01 oracle — status and pending verification

**2 October 2026 · In progress: still incomplete for 00G-R01.** This document records the candidate adaptation of the C3 instrument to the reduced scenario. It does not declare the complete C-V evaluator implemented or validated.

[Back to 00G-R01, reduced scenario](../../reductions/00G-R01/README.md) · [Complete document, §3.7](../../reductions/00G-R01/Escenario-creatividad-validacion.md#37-relación-con-el-trabajo-previo-y-sus-recorridos) · [Foundation and proof of the reduction under review](../../reductions/00G-R01/README.md#fundamento-y-prueba-de-la-reducción).

## Preserved base and scope

The [original C3 v0.4](./README.md) preserves its code, documentation and [frozen fingerprints](./DESIGN_FREEZE.json). This status document is a later addition, outside that freeze; it does not redefine its predicates or results.

The isolated reproduction on 2 October verified the fingerprints and obtained 102 of 102 satisfactory constructed controls. That result checks the instrument in its original T0/X and T1/Y domain, operation `inspect`; it is not equivalent to executions with agents and does not verify its complete suitability for 00G-R01. The original first trial retains the pending integration, registration and execution items described in the README and the round-1 protocol.

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
