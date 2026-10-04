# R01 — Computability, bounded execution and oracle work plan

Research work plan v0.1 · 3 October 2026 · Implementation pending

[Start at R01](./README.md#bot-start-here) · [Mathematical feasibility](./MATHEMATICAL_FEASIBILITY.md) · [Technology integration tasks](./extensions/hugging-face/REMAINING_TASKS.txt)

## Objective and starting point

Make the declared R01 traversal and its evaluation executable, prove termination for the bounded model and measure the resources needed to reproduce it. Keep three costs separate: the agents' operational ledger, evaluator/oracle computation, and total experiment infrastructure. Computability, tractability at a declared scale and practical suitability of a technology are different claims.

The retained [C3 v0.4 oracle](../../fixtures/00G-HF-ORACLE-v0.4/README.md) checks authority, commitments, attempts, effects and completion in its original T0/X and T1/Y inspect domain. Its frozen package was rerun on 3 October 2026: 102/102 author-constructed controls passed and the verifier checked frozen hashes. These are evaluator controls, not R01 agent runs. The [R01 adaptation status](../../fixtures/00G-HF-ORACLE-v0.4/ESTADO_00G-R01.md) leaves the full optimum, resource ledger and collective evaluation open.

Preserve that package. Build a versioned R01 evaluator with explicit projections where C3 semantics actually apply. The existing extension checkers provide reusable witness ideas and independent comparison patterns; their simplified execution and observation rules are not the full receiver.

## Bounded implementation contract to complete

| Component | Required behavior and boundary |
|---|---|
| World generator | Freeze graph, lengths, benefits, geometry, connectors, mandates, predicates and seeds. Use finite encoded values; report conditioning/rejection. Keep I/P labels private. |
| Agent interface | Implement the charged explore, relation-inspection, mandate, evidence, state, communication and execution operations of §2.6. No free full-map answer. |
| Exact reference | Find maximum J over complete admissible effective trajectories, retaining ties and all connectors/mixtures. Small exhaustive enumeration is the first independent reference. |
| Trace evaluator | Reconstruct actual effects, valid completion, q, partial technical value, e, violation events, costs and censored latency under §1.4. Candidate verdicts are not ground truth. |
| Recorder and ledger | Record identity, versions, scope, evidence lineage, receipt times and every charge, including discarded candidates, retries, maintenance and execution. Coordination is included in total cost once. |
| Policy runner | Freeze CV-C0/CV-C1/CV-A0/CV-A1/CV-A2 rules for any executed contrast. A policy name is not an implementation; fixture scripts are not autonomous agents. |
| Reproduction bundle | Pin source, environment, parameters, random streams and commands. Store traces, certificates, rejected worlds, failures and timings with explicit coverage. |

Finite graph size alone does not guarantee finite execution: cycles, unbounded memory or zero-cost/zero-time events may allow arbitrarily long runs. Specify a finite event horizon or another well-founded termination argument, finite observations/actions and computable probabilities. If an added cap truncates legitimate R01 behaviors, declare the narrower submodel and the proof's scope.

Declare numeric encoding and input size. Exact enumeration may be exponential; a small successful run does not establish polynomial complexity or cheap execution at scale. An optimized evaluator must be checked against a separately implemented reference, not merely a second entry point into its own logic.

## First bounded target and acceptance

Use the small static first-campaign domain of R01 §2.15: global budget, common task, fixed profiles, separate conjunction and parity blocks. Declare the finite limits on L, population, branching, connectors, seeds and events before execution. Mixed predicates, changing dependencies, larger networks and EA comparisons remain later extensions.

The first delivery needs an end-to-end legitimate trajectory, an inadmissible executed trajectory where the declared policy permits such an error, a detected/blocked alternative, and an incomplete or abstaining run. Never script an agent to fail and present it as emergent behavior. Include a world where a connector changes the optimal admissible route.

Correctness gates precede cost claims. Set a concrete machine and maximum runtime/memory budget before benchmarking; record cold/warm runs, repetitions, timeout behavior and coverage. Report measurements for the tested sizes and an explicit complexity argument where available. Stop at the registered resource ceiling and retain inconclusive runs.

## Remaining tasks — staged bot work plan

<!-- R01_BOT_WORKPLAN_START version="0.4" role="queue-pointer" -->
The current queue is in [WORKPLAN.md](./feasibility/WORKPLAN.md). This document contributes evidence or criteria within its scope; it does not maintain a second queue. Human escalation and whispering is the first technology in the protocol; repeated reviews are incorporated into each fiche. Independent review, fidelity and integrity retain their open obligations. The previous block is preserved in QUEUE_SNAPSHOT_2026-10-04.json.
<!-- R01_BOT_WORKPLAN_END -->
