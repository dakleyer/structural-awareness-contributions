# R01 technology adapter guide

Working guide v0.1 · 5 October 2026 · no real technology connected yet.

The adapter is the only technology-specific layer of the R01 C02/T03 path. It should be replaceable without changing the oracle, reference-world semantics or gate policy.

The admission envelope follows Nelson Trasatti's UC-4 approach: version-pinned imported contract, declared capabilities, frozen cases and source-contributor review. R01 adds the bounded execution service needed for its own scenario.

## 1. Two supported adapter modes

### A. `BATCH_RESULT`

Used for deterministic Stage-0 mappings or a technology that can consume one frozen participant view and return one structured result.

Interface:

```python
invoke(observation, context) -> candidate_result
```

The current instrumentation adapter uses this mode.

### B. `INTERACTIVE_TOOL_BROKER`

Preferred for a real agent/runtime, workflow engine or human-escalation mechanism that must actively explore, inspect, query, communicate or execute.

Interface:

```python
run_session(observation, tool_call, context) -> candidate_result
```

`tool_call` is the only R01-world action surface supplied by the harness. It implements the operations admitted by the frozen profile. The adapter must not import or read private world/oracle modules.

## 2. Adapter responsibilities

A real adapter must:

- identify product/runtime/model/workflow and exact versions;
- identify its source owner and source contract/version;
- declare `interaction_mode` and required capabilities;
- map only the admitted participant-visible input into native technology input;
- preserve source identifiers, provenance, scope/version and UNKNOWN/unresolved states where supplied;
- use only admitted tools/permissions;
- preserve raw/native traces where access and licensing permit;
- normalize outputs/events into the R01 candidate-result/event contract without inventing missing evidence;
- report timeouts, refusals and infrastructure errors separately from substantive candidate failure;
- report operational and coordination resource use without including evaluator/oracle computation;
- expose reset/cache/memory behavior for registration.

## 3. Adapter prohibitions

The adapter must not:

- read `private_world`, reference results, expected outcomes or hidden I/P labels;
- infer another Theme's authority, delegation, oversight or identity semantics from R01 labels;
- suppress a failed or malformed run;
- change the fixture, budget, deadline or gate after observing a result;
- translate UNKNOWN/NOT_ESTABLISHED into a positive or negative fact;
- use an undeclared external source, tool, reviewer or memory store;
- count evaluator computation as candidate burden or omit declared tool cost.

## 4. Native evidence and normalization

Keep two representations where possible:

1. **native evidence** — vendor/runtime/human-process trace in its original form;
2. **normalized R01 trace** — only the fields needed for the common evaluator.

The mapping between them is versioned. A normalized field must point to its source event or declare that the native system did not expose one.

For human escalation, the human is not treated as an oracle. The adapter records the request, information supplied, response, timing, scope and subsequent machine action. Human correctness and capacity are empirical observations under the registered protocol.

## 5. Error classes

| Status | Meaning |
|---|---|
| `PASS` | Candidate met the registered R01 acceptance conditions in the bounded case. |
| `FAIL` | Candidate executed but did not meet one or more registered substantive/contract conditions. |
| `INCONCLUSIVE` | The registered evaluator/reference cannot support a determination. |
| `INFRASTRUCTURE_ERROR` | The candidate could not be evaluated because the harness/runtime path failed. |
| `CANDIDATE_CONTRACT_REJECTED` | Candidate output exists but violates the registered adapter/result contract; represented as a scoped FAIL in the current R01 harness. |

The mapping of these labels into Nelson's final UC-4 expected-outcome vocabulary remains subject to his source-contributor review.

## 6. Before T03

A real technology adapter is not admitted until:

- the UC-4 experiment/profile version is pinned;
- the R01 sidecar/profile is pinned;
- capabilities and permissions are present;
- source-contributor review status is recorded;
- world/fixture/tool-profile/adapter hashes are frozen;
- candidate/oracle visibility separation is tested;
- reset/cache/seed rules are fixed;
- error and retry policy is fixed;
- expected outcomes and analysis/stopping rule are frozen before execution.

Use [REAL_TECHNOLOGY_REGISTRATION_TEMPLATE.json](./REAL_TECHNOLOGY_REGISTRATION_TEMPLATE.json) as the R01-side registration checklist; it does not replace Nelson's UC-4 experiment package.
