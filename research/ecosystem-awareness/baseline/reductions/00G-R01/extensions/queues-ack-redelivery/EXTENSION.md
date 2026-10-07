# Extension — Queues, acknowledgement and application closure

Documentation 0.2 · 7 October 2026 · Simplified DDS Stage A.

The [single DDS Index](../../../../../DDS_CANONICAL_METHOD_INDEX_v0.1.md) governs this study. The local base is **QUEUES-ACK-REDELIVERY-BOUNDED-RECEIVER-0.1** and the object is a bounded candidate receiving/mechanism specification. Its [candidate package](./CANDIDATE_SPECIFICATION_PACKAGE.json), [scope/card](./CURRENT_RUN_CARD.json) and [current record](./CURRENT_STUDY_RECORD.json) identify the selected obligations. Native execution here means the named local library/state, not validation of a provider product.

## Step 1 — technology–problem extension and correspondence

Question: **When do broker acknowledgement, redelivery and an application receipt establish sufficient local completion?**

Human/process contexts and actual parameter changes are explicit in all 11 registered [scenarios](./CURRENT_RUN_CARD.json). The receiver receives permitted requests, configuration and source/resource observations; the evaluator retains expected labels, truth and target state. Scenario/policy simulation-kind markers remain visible to these local models; there is no claim of blind generated-world search or hostile-code isolation.

RabbitMQ documents publisher confirms and consumer acknowledgements as separate protocol concerns, with delivery tags scoped to channels and possible redelivery. Application effect/receipt obligations are declared by this study.

The correspondence is local: task→request/effect, scope→tenant/resource, qualification→current permitted observations, closure→the actual response/receipt/disposition and useful window. It is **not a proved R01/native-product isomorphism**. R01 probability/cost laws, rates and all-policy bounds do not transfer. Any claimed transfer requires a separate admissible relation with preserved inputs, actions, information, cost and acceptance. These conditions are the limits of this Step 1 finding.

## Step 2 — non-isomorphic/additional mechanisms

| Mechanism | Producer/authority | Measured burden and falsifier |
|---|---|---|
| Transport versus application closure | Publisher, broker, consumer and resource each produce a distinct observation | Publisher-only Q02 stays incomplete; Q11 false promotion is P |
| Channel-scoped acknowledgement | Consumer owns the delivery channel/tag relation | Selected SQLite ack policy; Q06 wrong channel cannot complete the declared task |
| Effect/receipt deduplication | Resource/consumer own operation key and durable receipt | Effect+receipt transaction/recovery reads; Q03 closes one effect, Q04 retains duplication |
| Early acknowledgement and recovery limits | Consumer/broker environment model | Q05 removes the task before the effect; no admitted recovery witness is manufactured |
| Scope, current authority, TTL and dead letter | Task/resource owner admits scope and poison fallback | Q07 records M; Q08/Q09/Q10 denial/expiry/tenant mismatch stay incomplete |

Composition: Lost acknowledgements trigger retries. A conventional receiver can recover its local receipt before another non-idempotent effect; early acknowledgement plus crash remains outside that recovery path. Different mechanisms may be supplied by conventional application logic. No extra-architecture advantage is presumed; a competent conventional peer is credited fully.

## Sources and boundaries

- [RabbitMQ consumer acknowledgements/publisher confirms](https://www.rabbitmq.com/docs/confirms) — primary reference for selected semantics; reviewed 2026-10-07; no named-product execution.
- [RabbitMQ reliability](https://www.rabbitmq.com/docs/reliability) — primary reference for selected semantics; reviewed 2026-10-07; no named-product execution.

actual SQLite message/effect/receipt state with authored broker/channel/redelivery model; no RabbitMQ/AMQP product execution. Publisher confirmation, delivery acknowledgement and business completion have different boundaries. Local atomicity does not establish distributed exactly-once or broker product reliability.
