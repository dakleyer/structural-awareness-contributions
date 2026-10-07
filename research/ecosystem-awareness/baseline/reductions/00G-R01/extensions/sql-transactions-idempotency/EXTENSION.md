# SQL transactions and resource idempotency — technology extension

Version0.2 ·6 October2026 · actual embedded SQLite plus authored task profile.

**DDS classification:** Simplified **Gate A — Specification Discovery** under the [DDS Canonical Method Index](../../../../../DDS_CANONICAL_METHOD_INDEX_v0.1.md), using the [Gate-A challenge–trajectory contract](../../../../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md). Base LOCAL-EFFECT-RECEIPT-ATOMICITY0.1 is the declared local ledger/receipt task; no R01 isomorphism, Gate-B architecture verification or Gate-C native distributed-system result is inherited.

## Problem and configured technology

A permitted operation must change the local ledger once and leave a sufficient receipt bound to the same payload. Retrying or missing an acknowledgement must not create another effect. A row in an outbox is not completed downstream delivery, and a local rollback does not undo separately committed effects outside its transaction.

SQLite3.53.1 actually executes BEGIN IMMEDIATE, inserts, COMMIT/ROLLBACK, operation-key uniqueness and receipt recovery. The selected journal mode is DELETE with foreign_keys enabled. The out-of-domain diagnostic uses another local SQLite file, not a live external service. The two-connection test uses one bounded stale-precheck schedule, not a concurrency/power-loss campaign.

Ordinary transactions and resource-side idempotency are strong conventional capabilities [DB01–03,WF03]; they receive full credit. The extra review does not claim an architecture novelty.

## Stage1 — technology–problem extension and isomorphism profile

**Performed within scope. Actual local SQL semantics plus task correspondence; no global/R01 isomorphism.**

|Surface|Concrete correspondence|Preservation/transfer limit|
|---|---|---|
|Objects/relations|Operation, payload hash/identity, ledger, receipt, outbox, local grant|Chosen operation identity and atomicity domain only|
|Events/actions|Begin, check current state, write, commit/rollback, retry/recover|One database; external service effects not transported into its rollback|
|Observations|Current local grant/key/receipt queries|Producer provenance and real authorization sources stipulated|
|Authority|Admitted local grant and matching requested payload|Receipt for a previous payload cannot authorize a changed request|
|Cost/time|Instrumented explicit execute-call trace; connection/transaction observations|Full primitive/storage/latency/tariff accounting not established|
|Quality/outcome|One permitted matching receipt/effect for current task|Outbox-pending scenario explicitly requires a further consumer result|
|Coverage|Nine selected cases and one two-connection schedule|Not every policy/interleaving/failure/device condition|

R01 E1–E7 would require complete preserved signatures, enabled events, laws, views, normalized charges/time, sufficient quality/optimum and scoped lifting. No such relation is proved here. Expanding from one database to another resource changes the atomicity/effect contract and requires separate justification, not a relabelled source guarantee.

## Stage2 — additional mechanisms and composition

**Performed within scope.**

|Mechanism|Producer/invoker and validity|Burden/failure boundary|
|---|---|---|
|Atomic local effect/receipt|One transaction owns both local records|Lock/write/commit work; does not cover a different file/service|
|Resource key uniqueness|Native primary operation key|Additional key lookup/storage; identity must remain stable across retries|
|Payload binding|Current request compared with stored payload|Hash/identity governance; a reused key for new meaning is refused|
|Receipt recovery|Later actual connection reads committed state|Recovery work; acknowledgement loss differs from missing effect|
|Outbox/effect-domain separation|Producer records pending downstream intent|Storage/publisher/consumer work; pending record is not completed delivery|

Composition can close the local task while leaving a broader business flow incomplete. The separately committed out-of-domain effect is a retained material counterexample to extending the one-database rollback claim, not a SQLite defect.

## Scenarios

- **TX-01:** A permitted local ledger change and its receipt commit in the same SQLite transaction.
- **TX-02:** The application fails after inserting the local effect but before commit. Rollback must leave no effect or receipt.
- **TX-03:** The same admitted operation/payload is retried. Its stable resource key must preserve one effect and recover the receipt.
- **TX-04:** Two actual connections both read initial absence before sequential admitted writes. The unique transaction key must reject a second effect.
- **TX-05:** An earlier operation exists. A new request reuses its identifier with a different payload; its old receipt must not authorize the changed request.
- **TX-06:** The local effect and an outbox record commit, but the selected task additionally requires downstream consumption. No consumer has completed it.
- **TX-07:** A separate local database commits an effect, then the primary business transaction aborts. Its rollback cannot undo that out-of-domain effect.
- **TX-08:** The current admitted local grant denies the requested operation.
- **TX-09:** The effect/receipt committed but the caller missed the acknowledgement. A later connection recovers the one durable local receipt.

[Card](./RUN_CARD.json) fixes each task/effect-domain setting and outcome/effect counts. TX-05 preserves the prior effect while evaluating the changed current request; TX-06 explicitly adds downstream consumption to sufficient closure. They are different declared scenario parameters, not repaired thresholds or inferred delivery.

The transaction receives current request/grant data; expected case labels stay with the driver/oracle. Producer/permission truth, stable payload identity, adequate receipt semantics and complete effect-path coverage are material assumptions. Atomicity-domain, rollback, key/payload reuse, consumer absence and acknowledgement loss are tested boundaries; real hardware, service behavior and source authority remain uncalibrated.

## Primary sources

- [DB01 — SQLite isolation](https://www.sqlite.org/isolation.html).
- [DB02 — SQLite transaction control](https://www.sqlite.org/lang_transaction.html).
- [DB03 — SQLite conflict resolution](https://www.sqlite.org/lang_conflict.html).
- [WF03 — Temporal activity definition/idempotency](https://docs.temporal.io/activity-definition), documentary source on service-enforced stable keys; Temporal not executed.

Selected primary sections reviewed6 October2026. They support ordinary mechanism credit, not independent validation of this task. [DDS findings, accounting and closure](./DDS_STUDY.md).

