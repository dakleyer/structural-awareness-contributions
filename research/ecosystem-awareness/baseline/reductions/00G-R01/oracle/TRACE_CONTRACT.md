# R01 oracle auditable trace contract

Working trace contract v0.1 · 5 October 2026.

This document narrows the current harness implementation against R01 §2.16. It does not redefine the scenario.

## 1. Minimum identity

Every participant view used by the current Stage-0 harness carries:

- `task_id`;
- `receiver_id`;
- `principal_id`.

A real profile adds any resource, scope, version or mandate identifiers needed by that task.

## 2. Candidate decision record

Every accepted candidate result carries:

- `task_status`;
- `selected_trajectory_id` or null;
- `decision_basis`;
- native/normalized `events`;
- resource usage.

In batch instrumentation, the adapter resource report is diagnostic only. The evaluator uses a harness-authoritative measurement.

## 3. Interactive broker record

Each broker event records:

- monotonic request index;
- operation;
- request;
- participant-visible response when accepted;
- status;
- declared charge and duration;
- cost before/after;
- clock before/after.

The private environment trace may additionally retain effect/adjudication data. It is never supplied to the candidate during the registered run.

The strict interactive profile enforces the currently implemented causal sequence:

```text
explore / observed
        ↓
inspect_relation
        ↓
REVIEW_CLEAR ── query_mandate where required
        ↓
commit
        ↓
execute
        ↓
effect receipt / private adjudication
```

A later incompatible review supersedes the previous review/commitment state. A commitment is consumed by execution.

## 4. Two seals

The harness maintains two different integrity statements:

1. **candidate trace seal before oracle** — proves which participant-visible inputs, candidate outputs and authoritative pre-oracle measurements existed before reference evaluation;
2. **post-run result seal** — covers the resulting evaluation artifact after the oracle/reference methods have run.

The two hashes must not be confused. The first supports oracle blindness; the second supports result integrity.

## 5. Private evidence disclosure

Interactive private environment evidence receives its own commitment/hash. By default the harness does not return the private trace itself. Disclosure is a separate post-run/campaign policy.

For a real campaign, oracle/reference output must not be released between registered episodes if it could alter later candidate behavior. See [ISOLATION_CONTRACT.md](./ISOLATION_CONTRACT.md).

## 6. Current coverage and remaining scope

The Stage-0 instrument currently covers:

- task/receiver/principal identity;
- visible candidates and benefits;
- operation timing/cost;
- review result;
- mandate query;
- decision basis;
- commitment;
- execution attempt/effect;
- private violation/effect adjudication;
- final task status;
- exact bounded optimum and ties.

Profiles using communication additionally need message lineage, sender/receiver timing, provenance/dependency and receipt semantics. Stateful/stochastic real technologies additionally need registered reset/cache/seed state and native trace references. These remain admission obligations rather than silently assumed fields.
