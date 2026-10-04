# R01 technology-neutral tool broker contract

Working executable contract v0.1 · 5 October 2026.

This is the boundary intended for real-technology adapters. It complements Nelson Trasatti's UC-4 adapter discipline: UC-4 governs how an imported profile is versioned/admitted; this broker governs how an admitted technology can interact with an R01 world **without receiving evaluator truth**.

Primary R01 source: §§2.6–2.8, 2.11–2.12, 2.16–2.17 of [the R01 scenario](../Escenario-creatividad-validacion.md).

The generic operation names are not a universal FG-TIDA API. A concrete experiment freezes which subset exists, its request/response fields, charge, duration and effects.

## 1. Generic operation vocabulary

| Operation | R01 purpose |
|---|---|
| `setup` | Declared preparation/prior acquisition where a profile has it. |
| `explore` | Inspect/reach a candidate and obtain only its declared visible observations. |
| `inspect_relation` | Inspect one known relation/version and its accessible facts. |
| `query_mandate` | Obtain the accessible authority/mandate rule and version from its semantic owner. |
| `verify_evidence` | Check a named certificate/evidence item, scope/version and applicability. |
| `query_state` | Query a declared accessible current state/version. |
| `communicate` | Send/receive a declared message; relaying does not create independent evidence. |
| `decide` | Record a decision/commitment under the candidate's policy. |
| `execute` | Attempt the material action; the environment records the actual effect separately. |
| `wait` | Consume declared time without inventing evidence. |
| `stop` | Terminate without converting incomplete work into delivery. |
| `reuse` | Reuse only evidence/history whose declared applicability still holds. |

A profile may omit operations or split them further. It must not silently merge an oracle read into another operation.

## 2. Manifest requirement

Each available operation must freeze:

```text
operation id
accepted request shape
participant-visible response shape
charge
duration
state transition
evidence produced
possible material effect
failure/rejection behavior
```

This follows the complete-manifest obligation in the conditioned R01 theorem: each operation needs an accessible response, transition, charge, duration, evidence production and possible effect.

The current closed-catalog example in `fixtures/stage0/tool_profile.json` is only an instrumentation profile. It does not replace the richer configuration inventory of R01.

## 3. Visibility separation

The broker keeps two logs:

- **public trace:** requests, participant-visible responses, charge, duration and causal ordering;
- **private environment trace:** the same event plus adjudication/effect data needed later by the oracle.

The adapter receives only public responses. Keys declared `private` in a profile are never copied into a response.

The broker does not provide:

- I/P labels;
- the complete admissible optimum;
- an unqueried full map;
- another participant's private state;
- evaluator verdicts or expected outcomes.

If a real API legitimately supplies stronger information, that capability must be declared in the profile and made available under the same comparison contract.

## 4. Accounting and timing

Every accepted operation consumes its frozen charge and duration. A request that cannot fit the remaining hard budget/deadline is rejected before the effect and exposes no hidden datum. The rejection is still recorded as a request event.

Candidate operational cost, coordination cost and evaluator/oracle computation remain separate ledgers. A breakdown must never double-charge coordination.

## 5. Relation to UC-4

UC-4 remains the intended experiment/testbed envelope:

```text
UC-4 admitted experiment + versioned source adapter
        |
        v
R01 technology adapter
        |
        v
R01 tool broker (declared operations only)
        |
        v
sealed candidate trace
        |
        v
private R01 oracle/evaluator
```

The broker is therefore an **R01-specific execution service behind the UC-4 adapter boundary**, not a proposed replacement for Nelson's testbed core or Theme #13 signal lifecycle.
