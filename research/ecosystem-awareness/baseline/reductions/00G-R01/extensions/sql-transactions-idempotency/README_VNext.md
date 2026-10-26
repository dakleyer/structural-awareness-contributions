# SQL transaction/idempotency extension — sole owning scoped review

Version0.2 ·6 October2026 ·same author. Covers this leaf's extension/report/Card/Freeze/code/results under the one DDS.

Nine cases/18 expectations actually execute SQLite transactions, rollback, one bounded two-connection stale-precheck order, payload/key reuse and receipt recovery. 4I/4Ø/1P retained. The P is an effect separately committed in a second local database after primary abort; no external live service or native SQLite defect inferred. TX-05 evaluates the changed request against a prior receipt; TX-06 explicitly requires a consumer result beyond an outbox entry.

Stage1 states local-domain correspondence without R01/global proof transfer. Stage2 credits ordinary atomicity, resource keys, payload binding, recovery and effect-domain separation. SQL counters are explicit instrumented execute calls, not complete primitive/tariff Cost. Zero omitted work or full budget acceptance is not inferred. No population, every-interleaving, power-loss, independent or superiority claim.

Impact medium/high for effect/receipt/domain clarity; risk medium for extending local atomicity to broader service delivery. Controls are pinned pre-run scope, actual-state oracle, retained counterexample and explicit source/time/business/evidence limits. Scoped question closed; native broader-domain work only when agreed. No new method or SOW object.


Current-source reporting addition: canonical09b8fe09082f15612114ebe0fd3be8418be7a061 adds blind/rework/M-admission/T1/T2 surfaces. CURRENT_DDS_COVERAGE declares them not scored/not established as estimates; the old workflow flag is only descriptive local execution evidence. No run/card/freeze/expected outcome changed. Authentic documentation0.1 remains in old/.


## Tanda 5 — campañas, estudios e informes · 12 octubre 2026

**Revisión realizada por Codex, mismo asistente.** Iván autoriza la tanda4 y pide que todas las tandas aprobadas estén en main. Contributions `1897ed9424f58b95a10f2839c8e5b9f7bf741935` incorpora la4; use-cases main `d4fad875d12c1542fff8236ec484d68c6e641327` publica los54archivos UC-21 ya existentes en su rama y una entrada raíz añadida conservando los23archivos previos. Se reutilizan las seis VNext del paquete: ningún expediente nuevo. Continúa este trabajo en main de ambos repositorios. La rama anterior queda como historia. Esta tanda publica revisión y cuatro candidatos nuevos; no los aplica. PDF y entradaFG-TIDA siguen al final.

### sql-transactions-idempotency — informe, retorno y diagnóstico

9 casos:4I,4Ø,1P. Type1 0/4 yType2 0/9 coinciden. Se conserva elP huérfano fuera deType2; resultado prohibido y falsa clausura causal no son etiquetas intercambiables. El sucesor amplía el ledgerAPI sin reescribir el resultado original. Se cotejaron el registro vigente y la evidencia reparada, sin regrading del original. El cierre es de su pregunta StageA/Simplified; no elimina el fallo ni la condición de fuente/tiempo.

[Informe](https://github.com/dakleyer/structural-awareness-contributions/blob/1897ed9424f58b95a10f2839c8e5b9f7bf741935/research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/sql-transactions-idempotency/DDS_STUDY.md) · [Registro](https://github.com/dakleyer/structural-awareness-contributions/blob/1897ed9424f58b95a10f2839c8e5b9f7bf741935/research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/sql-transactions-idempotency/CURRENT_STUDY_RECORD.json) · [Retorno de evidencia](https://github.com/dakleyer/structural-awareness-contributions/blob/1897ed9424f58b95a10f2839c8e5b9f7bf741935/research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/extension-audit-v0.1/runs/2026-10-07-03/metrics/sql-transactions-idempotency.json).

Revisión cruzada: [plan EP](https://github.com/dakleyer/structural-awareness-contributions/blob/1897ed9424f58b95a10f2839c8e5b9f7bf741935/architectural-contributions/ecosystem-positioning/README_VNext.md), [DDS VNext](https://github.com/dakleyer/structural-awareness-contributions/blob/1897ed9424f58b95a10f2839c8e5b9f7bf741935/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md), [extensiones VNext](https://github.com/dakleyer/structural-awareness-contributions/blob/1897ed9424f58b95a10f2839c8e5b9f7bf741935/research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/README_VNext.md), [UC-21 VNext en main](https://github.com/dakleyer/use-cases/blob/d4fad875d12c1542fff8236ec484d68c6e641327/contributions/when-controls-work-system-fails/README_VNext.md). Cada registro conserva su propietario; estas notas son del mismo asistente.
