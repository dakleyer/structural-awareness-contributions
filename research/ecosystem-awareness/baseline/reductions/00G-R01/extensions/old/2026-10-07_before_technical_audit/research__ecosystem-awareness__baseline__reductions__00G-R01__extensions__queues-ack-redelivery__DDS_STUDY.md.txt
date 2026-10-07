# DDS — Queues, acknowledgement and application closure

Documentation 0.2 · 7 October 2026 · complete within the declared local Stage-A question.

## Finding and decision

A team can distinguish transport progress from fulfilled business work and identify which local effect/receipt obligations prevent loss or duplication. Publisher confirmation, delivery acknowledgement and business completion have different boundaries. Local atomicity does not establish distributed exactly-once or broker product reliability.

The test supports local compositional feasibility and explicit failure limits. It does not establish superiority, a product-wide conclusion or deployment ROI. The [extension](./EXTENSION.md) supplies the two review steps and mechanism/producer/interaction map. The [candidate specification](./CANDIDATE_SPECIFICATION_PACKAGE.json) identifies what a future realization would need to satisfy.

## Registered scope and evidence

**Object/base:** QUEUES-ACK-REDELIVERY-BOUNDED-RECEIVER-0.1. **Runtime/evidence:** actual SQLite message/effect/receipt state with authored broker/channel/redelivery model; no RabbitMQ/AMQP product execution. Inputs and environment law are registered before execution in the [Card](./CURRENT_RUN_CARD.json), with the [actual-byte Freeze](./CURRENT_FREEZE.json). The [current run](./runs/2026-10-07-03/RESULTS.json) passes 11 named-world expectations and 2 separate deliberate Type1/Type2 sensitivity controls. Expected negative and P outcomes are retained.

| Case | Human/process scenario | Observed | Prior M in G | C selected units | Qualified excess / signed gap to G |
|---|---|---|---|---:|---:|
| Q01 | A consumer must apply an admitted tenant-a operation and acknowledge its delivery after a durable effect receipt. | I | True | 10 | 0 |
| Q02 | A publisher has confirmation from the broker while consumer processing is still absent; the same consumer capability is available but this configuration stops early. | Ø | True | 2 | not applicable (gap -9) |
| Q03 | A local effect commits, the first acknowledgement is lost, and redelivery must recover one idempotent effect/receipt. | I | True | 15 | 0 |
| Q04 | The same lost acknowledgement meets a resource without the required stable operation key; two effects are retained. | P | True | 15 | not applicable (gap -1) |
| Q05 | The message is acknowledged and discarded before the application effect; a crash loses the task. | Ø | False | 4 | unavailable |
| Q06 | A committed application receipt is followed by an acknowledgement on another delivery channel; the declared end-to-end task remains incomplete. | Ø | True | 8 | not applicable (gap -3) |
| Q07 | The payload is not admitted; a tenant-scoped dead-letter record is the explicitly accepted minimum closure. | M | True | 4 | 0 |
| Q08 | The current resource grant denies the requested effect. | Ø | False | 5 | unavailable |
| Q09 | The message has expired at the processing boundary. | Ø | False | 2 | unavailable |
| Q10 | Only tenant-b data is delivered to the tenant-a processing request. | Ø | False | 2 | unavailable |
| Q11 | An application falsely promotes a broker acknowledgement into completed business processing with no observed effect. | P | False | 4 | unavailable |

Instrument assertion PASS does not mean all scenarios were delivered. Outcomes here are {"I": 2, "Ø": 6, "P": 2, "M": 1}. The scenarios are authored examples, not a representative population.

## Cost, diagnostics and acceptance

Cost is the sum of the frozen selected actual SQLite API and policy-entry units (weight1), including commit/rollback. Candidate, setup and evaluator entries are separated. Current total candidate units **71**, with every component/trace in the run. Money, tokens, real staffing/network/service times and lifecycle remain unscored, not zero. These heterogeneous units are not a cross-technology ranking.

Private minimum_G is exact only within the two frozen qualifying/reference procedures. The raw run field `excess` is a signed arithmetic gap; [current cost interpretation](./COST_INTERPRETATION.json) credits excess work only for legitimate I/M closures. A negative gap from an incomplete/incorrect trace is not efficiency. The actual witness is meaningful and uses the same actor information/interfaces. The global accessible-information lower bound is not established. Missing legitimate closure witnesses yield unavailable minima; cheap P/Ø traces are not credited as efficiency.

The [M-admission map](./runs/2026-10-07-03/M_ADMISSION_BEFORE_CANDIDATES.json) is sealed before candidate evaluation. Type1 is **2/6** eligible named traces; Type2 is **2/11** registered named traces under the declared causal rule. No P enters the Type1 numerator. Excess alone is not Type1. Raw P is not automatically Type2. Two deliberate fault controls are separately reported, never pooled as product performance. No population estimate or statistical confidence interval is claimed.

Acceptance is the registered scoped expectation/falsifier contract, not native/global deployment acceptance. Positive continuity, malformed/scope/currentness boundaries, expected material violations and control sensitivity all retain their specified results.

## Baseline, residual risk and conditional business value

Native mechanisms are credited according to their documented scope. The same-information conventional qualified/reference procedures can close legitimate cases; no superiority over them is established. The example value is **A team can distinguish transport progress from fulfilled business work and identify which local effect/receipt obligations prevent loss or duplication.**

Residual limits: Publisher confirmation, delivery acknowledgement and business completion have different boundaries. Local atomicity does not establish distributed exactly-once or broker product reliability. Source/authority authenticity, real availability, independent review, native integration, monetary burden, wider action spaces and distributional transfer remain conditional. A material change to source/permission/timing/effect contract needs explicit requalification and, when result-producing, a prospective successor.

## Current coverage, closure and delivery

Challenge/configuration, scenario explanations, Step 1 correspondence/transfer limits, Step 2 producers/burden/interactions, selected route/effect/cost/type controls, acceptance, bibliography, reproducibility, business interpretation and residual limits are present. This is a declared **Simplified Stage A** record. B requires a separate architecture-to-frozen-spec verification package; C requires admitted pinned-implementation/effect validation. Neither is inferred from this execution.

The selected technical question is closed with an evidence-bounded answer. The technical record is this report and its reproducible dossier; fees, Sponsor/seal, DOI, international submission and commissioned long reports retain their separate existing states. No SOW output or fee is added or waived.

Reproduce with the registered runtime: `python -B current_study.py --output <fresh directory>`. [Current status](./CURRENT_STUDY_RECORD.json) is the live reading record; old Cards/results retain their registered identity and dates.

