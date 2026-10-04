# R01 — Computability, bounded execution and oracle work plan

Research work plan v0.3 · 4 October 2026 · Limited C02 implementation draft; real-technology execution pending

[Start at R01](./README.md#bot-start-here) · [Mathematical feasibility](./MATHEMATICAL_FEASIBILITY.md) · [Technology integration tasks](./extensions/hugging-face/REMAINING_TASKS.txt)

## Objective and starting point

Make the declared R01 traversal and its evaluation executable, prove termination for the bounded model and measure the resources needed to reproduce it. Keep three costs separate: the agents' operational ledger, evaluator/oracle computation, and total experiment infrastructure. Computability, tractability at a declared scale and practical suitability of a technology are different claims.

The retained [C3 v0.4 oracle](../../fixtures/00G-HF-ORACLE-v0.4/README.md) checks authority, commitments, attempts, effects and completion in its original T0/X and T1/Y inspect domain. Its frozen package was rerun on 3 October 2026: 102/102 author-constructed controls passed and the verifier checked frozen hashes. These are evaluator controls, not R01 agent runs. The [R01 adaptation status](../../fixtures/00G-HF-ORACLE-v0.4/ESTADO_00G-R01.md) leaves the full optimum, resource ledger and collective evaluation open.

Preserve that package. Build a versioned R01 evaluator with explicit projections where C3 semantics actually apply. The existing extension checkers provide reusable witness ideas and independent comparison patterns; their simplified execution and observation rules are not the full receiver.

## Current claim boundary

This revision starts **design preparation for C02 by explicit maintainer instruction**. It does not satisfy the C02 entry criteria, does not authorize C11 registration or T03 execution, and does not report a real-technology result.

The limits are deliberately strict:

- the complete R01 C-V evaluator is **not implemented or validated**;
- no real agent, vendor runtime, human-escalation process or other technology has been executed through this oracle;
- the retained C3 package remains frozen and is not modified by this plan;
- no product or architecture receives oracle truth, hidden I/P labels, the admissible optimum or expected outputs during its run;
- no EA advantage, technology failure rate, production latency or scalability claim follows from this document;
- where an exact reference cannot be established inside the declared bounded domain, the evaluator must return an unresolved status rather than manufacture ground truth.

## First implementation slice

The first neutral instrument now lives at [`oracle/`](./oracle/README.md). It implements the smallest executable slice of the design without changing the frozen C3 package:

- a UC-4-first interoperability profile and R01-private sidecar schema;
- a versioned technology-neutral adapter contract;
- Canonical Trace v1 reuse from the existing RS-00E-Q1a harness;
- two separately coded exact reference paths over the first finite trajectory representation;
- oracle-blind candidate invocation and candidate-trace sealing before reference evaluation;
- separate candidate-operational and evaluator/oracle accounting;
- four author-constructed Stage-0 vectors: positive, connector boundary, rejection and tied optima;
- an instrumentation-only self-test adapter and `verify.py`;
- CI invocation through `.github/workflows/r01-audit-v2.yml`.

This is **not C02 completion**. The current second reference path is a separate implementation by the same maintainer, not independent external validation. The UC-4 bridge is `R01-BRIDGE-DRAFT` until Nelson reviews/corrects the mapping, and the exact upstream UC-4 schema package has not been vendored into this repository. C11/T03 remain blocked.

## Reuse-first strategy

R01 should not build a new testing stack when the corpus or FG-TIDA already contains suitable mechanisms. Reuse is by **versioned reference and bounded adaptation**, preserving the original owner, scope and limitations.

| Existing material | Reuse in R01 | Boundary / attribution |
|---|---|---|
| [C3 v0.4 oracle](../../fixtures/00G-HF-ORACLE-v0.4/README.md) | Authority, commitment, attempt, effect and completion predicates where a verified projection exists. Existing run-registration and recorder expectations are retained. | Frozen C3 semantics remain unchanged; C3 PASS is not R01 truth and does not decide 00G/R01 membership. |
| [00D-A01 bounded-oracle/test design](../../00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md) | Fixture admission, bounded reference-oracle discipline, negative controls, falsifiers and staged testbed logic. | Evidence-design precedent only; it does not make R01 an executed testbed. |
| [00D-A03 deterministic harness](../../00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1.md) and [RS-00E-Q1a](../../fixtures/RS-00E-Q1a/README.md) | Separation of fixture loader, adapter, reference oracle, evaluator and trace writer; Canonical Trace v1; instrumentation self-test; deterministic replay; oracle loaded only after candidate invocation. | Reuse the pattern, not Q1a semantics. Q1a results do not transfer to R01. |
| [FG-TIDA UC #4](https://github.com/FG-TIDA/use-cases/issues/4), Nelson Trasatti | Requirement 22: versioned adapters for imported contracts; Requirement 23: frozen positive, boundary and rejection cases with machine-readable expected outcomes; Stage 0 deterministic harness concept. | Contributor-owned FG-TIDA material. R01 references and adapts these ideas; it does not claim ownership or FG-TIDA approval. |
| [Theme #13 charter preparation](../../../fg-tida/charter/THEME_13_WORKING_GROUP_CHARTER_PREPARATION_DRAFT_v0.2.md) | Bounded adapter discipline, source/contributor validation, expected-vs-observed separation and UC #4/UC #6 mapping lineage. | Preserve Nelson/Oleksii/Arpita/Olena attribution recorded there; do not silently reimplement their semantics. |
| [00K executable harness families](../../fixtures/00K/README.md) | Anti-shortcut discipline: no hidden oracle, no deny-all/accept-all/permanent-HOLD success, explicit positive/boundary controls, serious-repair checks and independent-second-method expectation. | Symbolic/fixture evidence only; no live-runtime validation transfers to R01. |

## Proposed minimal R01 oracle/harness architecture

The simplest robust architecture is a **thin neutral core plus versioned adapters**. The core should never import a vendor SDK or encode a specific technology's internal semantics.

| Module | Responsibility | Must not do |
|---|---|---|
| Frozen-world loader | Load the registered finite R01 world, parameters, graph, benefits, predicates, connectors, budgets, seeds and event horizon. | Expose private labels, hidden map facts or optimum information to the candidate. |
| Scenario/profile adapter | Convert one admitted R01 scenario or extension into the common event/observation contract. | Change R01 semantics to fit a technology. |
| Technology adapter | Invoke one concrete technology or human process with only the admitted observations, tools and budget. Normalize its observable actions/events. | Read oracle files, expected outcomes or hidden world state. |
| Recorder / Canonical Trace | Record inputs actually delivered, tool calls, actions, messages, timing, errors, retries and cost/burden in append-only canonical form. | Infer missing events or rewrite failed runs. |
| Exact reference oracle | From frozen private world state, compute admissibility, valid completion, effects and the exact best admissible trajectory for the declared bounded domain. | Judge by the candidate's own confidence or post-hoc narrative. |
| Constraint evaluator / gate policy | Compare observed trace against oracle facts and registered acceptance rules after the candidate has finished. | Feed results back into the candidate during the same run unless the registered technology itself includes such a feedback channel. |
| Resource ledger | Keep agent operational cost, oracle/evaluator cost and total infrastructure cost separate; include coordination only once. | Charge evaluator-only work to one comparator. |
| Independent cross-check | Recompute the bounded reference with a second implementation/method and compare canonical outputs. | Share the same critical helper path and call that independence. |
| Registration / manifest | Pin world, scenario, adapter, technology/runtime versions, permissions, budgets, seeds, commands, hashes and analysis before execution. | Expand the campaign after observing a failure without a new registration. |

### Ground-truth separation

Use four distinct layers so the candidate can never become its own oracle:

1. **G0 — frozen world truth:** private finite model facts, including labels that participants are not allowed to see.
2. **G1 — reference decision truth:** admissible trajectories, exact optimum/ties, completion and violation facts derived independently from G0.
3. **G2 — candidate observation and trace:** only what the technology actually received, emitted, attempted and caused, with its own declared metadata.
4. **G3 — evaluation result:** post-run comparison of G2 against G1 under the pre-registered gate policy.

`G2` never overwrites `G0/G1`. A technology's verdict, confidence or explanation is evidence about its behavior, not the reference truth.

### Technology-neutral adapter contract

Each adapter should expose the same small external contract even when the implementation behind it is an API, local agent framework, workflow engine or human-escalation process:

```text
adapter identity/version
technology/runtime identity/version
declared permissions and tool surface
accepted observation/event schema
invoke(observation, bounded_context) -> observable events/actions
finalize() -> candidate result + adapter diagnostics
timeout / refusal / infrastructure-error semantics
resource-usage report
```

The adapter may translate vendor-native traces into the canonical event schema, but it must retain the original raw or vendor-native evidence where licensing and access permit. Translation rules are versioned and tested with positive, boundary and rejection vectors, following UC #4's adapter discipline.

### Oracle-blind execution sequence

1. Freeze registration and hashes.
2. Load G0 into an oracle-only process/store.
3. Derive only the permitted participant view and pass it to the technology adapter.
4. Invoke the adapter and recorder; the candidate completes without access to G1 or expected outputs.
5. Seal the candidate trace and resource ledger.
6. Only then load/compute G1 for the post-run evaluator.
7. Evaluate the sealed trace under the registered gate policy.
8. Recompute G1 with the second method and compare canonical reference outputs.
9. Publish `PASS`, `FAIL`, `INCONCLUSIVE` or `INFRASTRUCTURE_ERROR` with the precise tested scope; none of these labels is automatically an EA or vendor-wide verdict.

## Minimum C02 control surface before a real technology run

The first neutral harness should include at least the following frozen vectors before T03:

- legitimate end-to-end admissible trajectory;
- inadmissible executed trajectory, where the tested policy can in fact commit such an error;
- detected/blocked inadmissible alternative;
- incomplete/abstaining trajectory;
- connector case in which the optimal admissible route changes;
- boundary case with a tie or multiple admissible optima;
- negative control in which no special escalation/containment is required;
- anti-shortcut controls against deny-all, accept-all and permanent-HOLD behavior;
- trace-instrumentation self-test plus a disabled-detector negative self-test;
- deterministic replay/canonical-hash check for fixed deterministic components;
- oracle-blindness check demonstrating that adapter-visible inputs exclude hidden labels, optimum and expected outcomes;
- second-method agreement on a small exhaustively enumerable world.

The first bounded exact oracle should prefer a very small world that can be exhaustively enumerated. Optimization comes later. If an optimized solver is introduced, it is accepted only after agreement with the independent exhaustive reference on the shared domain.


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
