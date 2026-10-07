# Durable workflows and bounded retries — technology extension

Version0.2 ·6 October2026 · own persisted local model.

**DDS classification:** Simplified **Gate A — Specification Discovery** under the [DDS Canonical Method Index](../../../../../DDS_CANONICAL_METHOD_INDEX_v0.1.md), using the [Gate-A challenge–trajectory contract](../../../../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md). Base DURABLE-LOCAL-CLOSURE0.1 is a declared local workflow/resource task; it does not inherit R01's laws, establish Gate-B architecture verification or instantiate/validate native Temporal under Gate C.

## Problem and configured technology

A request must reach one admitted effect with a completed local workflow, or an explicitly admitted minimum deferment, within useful logical deadline5. Losing an acknowledgement must not duplicate a resource effect. A stale worker or revoked grant must not keep acting just because the workflow persists.

The selected technology is an authored SQLite journal/worker/retry model. Actual files persist status/effects, connections close/reopen, and resource keys/generation/grants are checked. Service readiness, latency and acknowledgements are synthetic controlled conditions. No Temporal SDK/service, native queue/network, real operator or calibrated physical deadline was executed.

Durable execution and service-enforced idempotency are established conventional mechanisms [WF01–03]. They receive full credit. Persistence alone does not supply permission, source truth, correct retry policy or useful human capacity.

## Stage1 — technology–problem extension and isomorphism profile

**Performed within scope; documentary mechanism semantics plus finite local realization, no proved native/R01 isomorphism.**

|Surface|Concrete counterpart|Transfer limit|
|---|---|---|
|Objects/relations|Request, persisted workflow, attempts, worker generation, grant, resource effect key|One local task/state schema, not complete product semantics|
|Events|Attempt/failure, write/ack-loss, restart, retry, done/deferment|Actual SQLite; source readiness and time are model laws|
|Information|Selected ready/failure conditions and resource state|No native source authentication or independent human readiness|
|Authority|Current local grant/generation checked at the effect|Real cancellation/identity/OS/admin source unvalidated|
|Cost/time|Explicit SQL calls, attempts and logical ticks|Not real service latency, prices or complete primitive work|
|Quality/outcome|One admitted effect+completion, or admitted M; duplicate P/insufficient Ø|Persisted status alone is not sufficient evidence of correct effects|
|Coverage/policies|Nine configured local cases plus WF04 bounded M witness|No every-policy failure law or native-system simulation proof|

R01 E1–E7 would require complete preserved relations/enablement/laws/views/accounting/outcomes/coverage and proper transfer direction. A journal or workflow label is not that proof. New sources, resource behavior, additional obligations or deadlines can change the attainable region and need their own study.

## Stage2 — additional mechanisms and composition

**Performed within scope.**

|Mechanism|Producer/invoker and validity|Work/interaction/failure limit|
|---|---|---|
|Persistence/restart|Local database journal/state and worker|Writes/recovery; a stored status can coexist with an unobserved or wrong effect|
|Bounded retry|Selected controller and observable failure schedule|Attempts/waiting; useful window can be consumed without legitimate closure|
|Resource-side idempotency|Actual stable operation key at resource|Lookup/storage; retry alone does not enforce a unique effect|
|Explicit M deferment|Owner-admitted alternative, persisted locally|Closure work/tick; no human service executed and M is not a default|
|Current grant/generation/time|Resource source plus admitted logical contract|Checks/revalidation; stale workers and late routes are refused|

The W6 counterexample removes resource idempotency while preserving acknowledgement loss/retry; two actual effects result. It is an application/resource condition, not a Temporal platform defect. The bounded conventional M route is separately demonstrated for W4 under the same outage/window/fallback.

## Scenarios and assumptions

- **WF-01:** The local worker is ready and one admitted effect is durably recorded as completed.
- **WF-02:** Two observable transient failures precede a successful third attempt within the selected useful window.
- **WF-03:** The service remains unavailable. After two attempts the owner admits a recorded deferment that closes the minimum route in time.
- **WF-04:** Under the same permanent outage/admitted deferment, the selected retry-to-horizon policy consumes the useful window and never closes M.
- **WF-05:** The resource effect commits but the worker loses its acknowledgement. Restart/retry uses the same resource key and produces one effect.
- **WF-06:** The same lost acknowledgement occurs against a non-idempotent resource. Retrying creates two actual local effects.
- **WF-07:** A stale worker's generation1 meets resource generation2 after cancellation/replacement.
- **WF-08:** Declared service latency10 exceeds the useful logical deadline5 and no fallback is admitted.
- **WF-09:** An initially admitted grant is revoked before resource effect. The current resource check must refuse execution.

The [Card](./RUN_CARD.json) fixes deadline5, bounded attempts2 and declared scenario variants. Expected outcome labels stay with the driver/adjudicator; worker/environment share the selected model's readiness/latency law. This is not a blind agent experiment or hostile-code isolation.

Material assumptions include stable operation identity, complete idempotent effect paths, correct current source/authority/generation, useful time and an explicitly admissible reachable M. The battery challenges these selected boundaries; real queue/service/cancellation behavior and producer/human calibration remain unestablished.

## Primary sources

- [WF01 — Temporal activity execution](https://docs.temporal.io/activity-execution), selected persistence/retry/cancellation semantics.
- [WF02 — Temporal retry policies](https://docs.temporal.io/encyclopedia/retry-policies), selected policy/time limits.
- [WF03 — Temporal activity definition/idempotency](https://docs.temporal.io/activity-definition), activity retries and resource-enforced keys.
- [DB02 — SQLite transaction control](https://www.sqlite.org/lang_transaction.html), actual local persistence context.

Primary sources reviewed6 October2026. Temporal's documented capabilities are credited; no product was measured. [DDS evidence, Type1 witness, cost/value and closure](./DDS_STUDY.md).

