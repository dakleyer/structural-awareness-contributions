# SQL transaction/idempotency extension — sole owning scoped review

Version0.1 ·6 October2026 ·same author. Covers this leaf's extension/report/Card/Freeze/code/results under the one DDS.

Nine cases/18 expectations actually execute SQLite transactions, rollback, one bounded two-connection stale-precheck order, payload/key reuse and receipt recovery. 4I/4Ø/1P retained. The P is an effect separately committed in a second local database after primary abort; no external live service or native SQLite defect inferred. TX-05 evaluates the changed request against a prior receipt; TX-06 explicitly requires a consumer result beyond an outbox entry.

Stage1 states local-domain correspondence without R01/global proof transfer. Stage2 credits ordinary atomicity, resource keys, payload binding, recovery and effect-domain separation. SQL counters are explicit instrumented execute calls, not complete primitive/tariff Cost. Zero omitted work or full budget acceptance is not inferred. No population, every-interleaving, power-loss, independent or superiority claim.

Impact medium/high for effect/receipt/domain clarity; risk medium for extending local atomicity to broader service delivery. Controls are pinned pre-run scope, actual-state oracle, retained counterexample and explicit source/time/business/evidence limits. Scoped question closed; native broader-domain work only when agreed. No new method or SOW object.

