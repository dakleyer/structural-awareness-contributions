<a id="00g-r01-reducción-de-00g"></a>
# R01 Probabilistic exploration and validation cost

Base specification v0.6 · Reading organization 4 October 2026 · Non-canonical research study

[Complete base scenario](./Escenario-creatividad-validacion.md) · [Reductions](#reductions) · [Three extensions](#extensiones) · [Preservation record](./ORGANIZATION_TRACE.md)

<a id="canonical-conditioned-trilemma"></a>
**Current canonical mathematical reference:** [Mathematical validation of the conditioned trilemma in R01, v0.2](./feasibility/R01_CONDITIONED_TRILEMMA_THEOREM.md). This standalone document governs the mathematical statement, conditions and viability regions. [R01's explanation](./Escenario-creatividad-validacion.md#r01-conditioned-mathematical-validation) links to the same reference; [audit and repairs](./feasibility/R01_AUDIT_CONTINUITY_AND_REPAIRS.md) support it. External reviews have been received; the remaining coverage is tracked by version and proposition in [the current register](./feasibility/WORKPLAN_STATUS.json). The [extension consistency review](./feasibility/EXTENSION_CONSISTENCY_REVIEW.md) is complete as an own review. Continue with [technologies inside the extension protocol](./feasibility/TECHNOLOGY_EXTENSION_PROTOCOL.md#technologies-to-study), starting with human escalation and whispering.

The dated plans and state snapshots below are retained as history. For the current mathematical formulation, use the canonical document above; their original task criteria remain available.


**How to read the evaluation:** [problem + technology → operating scenario → execution strategy → performance → acceptance](./Escenario-creatividad-validacion.md#from-the-practical-problem-to-acceptance). The diagram distinguishes the accepted performance region from whether any permitted strategy can reach it.

[Differential and value of the experiment](./DIFFERENTIAL_AND_EXPERIMENT_VALUE.md): the technology–problem suitability map, cost/risk/effectiveness, related work, candidate contribution, oracle priorities and remaining review passes.

<a id="bot-start-here"></a>
## Start here — current work

[Current queue](./feasibility/WORKPLAN.md) · [task register](./feasibility/WORKPLAN_STATUS.json) · [continuation prompt](./feasibility/CONTINUATION_PROMPT.md).

The sole active queue is discovered by `R01_BOT_WORKPLAN_START` / `R01_BOT_WORKPLAN_END` in `feasibility/WORKPLAN.md`. Other marked documents point to it; they do not create independent pending-task lists.

| Order | Current work | Status |
|---|---|---|
| 1 | [Technologies of the extension protocol](./feasibility/TECHNOLOGY_EXTENSION_PROTOCOL.md#technologies-to-study): [human escalation and whispering first](./feasibility/HUMAN_ESCALATION_WHISPERING.md), then the registered frameworks. | Mathematical contract available; technology review and implementation correspondence in progress. |
| Remaining review | M16 independent coverage, M17 source-clause fidelity, P08 version-aware integrity. | Retain actual gaps; do not repeat completed own repairs or extension consistency review. |
| Later | C02 neutral oracle/harness → C11 registered campaign → T03 real adapter and technology campaign. | No new scientific execution in the task cleanup. |

The 55 historical IDs and criteria remain traceable: four active tasks, three later deliveries, four historical completions, three own-scope deliveries complete, 37 consolidated obligations and four tasks outside the current scope. Consolidation is not scientific validation. [Full old queues](./feasibility/previous-work/QUEUE_SNAPSHOT_2026-10-04.json) · [updated master prompt](./STRATEGIC_WORKPLAN_AND_EXECUTION_PROMPT.md).

The earlier proof records remain accessible through [previous work](./feasibility/previous-work/README.md). The [partial exercises and received Annex T](./feasibility/partial-experiments/received/2026-10-04/README.md) are preparation annexes, not canonical proofs or executed technology validation. Historical hash discrepancies remain P08; do not overwrite their manifests.

<a id="r01-in-plain-language"></a>
## What R01 studies

An agent knows a permitted procedure for completing its task. While working, it explores alternatives that may produce a better result. Each alternative takes effort to discover and to check. Other agents may share findings and checks, but their reports do not by themselves authorize the action.

The study asks when this process finds a good permitted solution within its budget and deadline, and when it instead executes an inadmissible alternative, spends too much on checking, settles for lower quality or leaves the task incomplete. Benefits and distances vary across the fixed world; search and policy randomness are recorded. Failure is a possible result to measure, not a required outcome.

**R01's practical objective is to design small, bounded pilots for choosing an architecture.** They should help determine whether a problem has an adequate solution through an R01-compatible architecture, when another procedure is preferable and when more evidence is needed. Human supervision also has information and cost limits. A small pilot supports conclusions about its tested scope; suitability at scale needs additional justification. Ecosystem Awareness is one candidate add-on for improving that scope, subject to the same comparisons.

| Route | Meaning |
|---|---|
| M — known procedure | A permitted starting plan; it may deliver lower quality. |
| I — ideal permitted alternative | The best complete admissible solution, calculated by the evaluator. |
| P — attractive forbidden alternative | A technically attractive route whose composition violates the obligation. |

These are the known route and two alternative references. Agents are not told which candidate is I or P. They discover candidates, review the relevant relations, decide whether to proceed and record the effect. A local check may leave important conditions unresolved; sufficient applicable evidence may resolve them.

**[Read the complete R01 scenario](./Escenario-creatividad-validacion.md).** It contains the problem, route construction, probabilistic exploration, decision cycle, validation, costs, configurations and required traces. This README is its entrance and extension index. The complete R01 campaign is specified but has not yet been implemented and executed.

| Question | Direct section in the complete document |
|---|---|
| How does R01 support architecture selection with limited pilots? | [Pilot objective and supervision §1.7](./Escenario-creatividad-validacion.md#17-cómo-detectar-el-área-y-qué-aporta-la-supervisión-humana) · [Bounded pilot protocol](./Escenario-creatividad-validacion.md#bounded-pilots-for-architecture-selection) · [Two areas and trilemma §1.2](./Escenario-creatividad-validacion.md#12-dos-áreas-y-un-trilema) |
| What are the routes and how are alternatives found? | [Routes §2.1](./Escenario-creatividad-validacion.md#21-tarea-y-trayectorias-de-referencia-etiquetadas) · [Benefits §2.3](./Escenario-creatividad-validacion.md#23-beneficios-heterogéneos-con-promedio-fijado) · [Search radius §2.4](./Escenario-creatividad-validacion.md#24-proximidad-y-radio-creativo) |
| What does an agent do, step by step? | [Decision cycle §2.7](./Escenario-creatividad-validacion.md#27-secuencia-de-decisión) · [Own review §2.8](./Escenario-creatividad-validacion.md#28-validación-convencional-hacia-atrás-y-hacia-delante) · [Social evidence §2.10](./Escenario-creatividad-validacion.md#210-señalización-y-validación-social) |
| How are costs and resources counted? | [Costs §2.11](./Escenario-creatividad-validacion.md#211-coste-de-exploración-y-coste-de-revisión) · [Budget §2.12](./Escenario-creatividad-validacion.md#212-presupuesto-y-plazo) |
| Where are the traces? | [Required trace fields §2.16](./Escenario-creatividad-validacion.md#216-qué-debe-registrar-una-trayectoria-auditable) · [States §2.17](./Escenario-creatividad-validacion.md#217-estados-y-requisitos-verificables-antes-de-ejecutar) · [Earlier executed trials](./extensions/hugging-face/README.md#retained-oracle-and-trial-history) |

<a id="reductions"></a>
## Reductions

A reduction removes particular details while preserving the relation needed for the stated claim. The documented origin of R01 is listed below; reduction status is separate from the three extensions.

| Documented reduction | What is simplified and retained | Explanation and proof status |
|---|---|---|
| 00G to R01 | Remove the particular narrative; retain the obligation, received interpretation, source dependencies, authority and decision in the candidate social subfamily. | [Reduction document](./reductions/00G-to-R01/README.md). Candidate relation under review; it does not classify every R01 configuration as a 00G instance. |

<a id="extensiones"></a>
## Extensions

An extension applies R01's task and decision questions to a concrete case. Each document starts with the problem, a step-by-step scenario and the parallel with R01, then identifies its proof, results, limits and sources. The mix contains selected parallels; it does not claim that every real incident has every R01 mechanism.

<a id="incident-scope"></a>
**Scope of the constructed extensions.** Their purpose is to study selected failure modes with features compatible with R01, motivated by the documented cases. They do not aim to reconstruct every detail of those cases or exactly reproduce the Hugging Face incident investigated by METR and Redwood. The modeled failure need not be the causal mechanism of the reported incident; this work does not establish that identification, and the mechanisms may differ.

If an R01 failure does not appear, or its assumptions do not fit a historical episode, that limits the claim about the tested model or proposed correspondence. It does not imply that the reported incident did not occur, nor rule out other mechanisms producing similar outcomes. Conversely, producing a similar failure in the model does not establish its historical cause. Formal preservation claims still require their stated contracts; similarity alone does not satisfy them.

The [common scope rule](./extensions/CRITERIA_AND_AUDIT.md#historical-and-constructed-scope) applies to all three cases. The [scope preservation record](./INCIDENT_SCOPE_TRACE.md) verifies retention of the preceding text.

| Extension | The problem in words | Complete case document |
|---|---|---|
| <a id="openai--hugging-face"></a>Hugging Face | Agents share useful alternatives; the receiver must establish whether using an alternative fits its task and permissions. | [Case, scenario, R01 parallel, proof, results and history](./extensions/hugging-face/README.md) |
| <a id="extensión-al-caso-infoblox"></a>Infoblox | A DNS diagnosis combines sources and a specialist; identity and earlier checks may not authorize the new combination or export. | [Case, scenario, R01 parallel, proof, results and history](./extensions/infoblox/README.md) |
| <a id="familia-extendida-con-nucleo-funcional-isomorfo"></a>Mix of other failure modes | Cases involving out-of-scope resources, an accepted answer that misses the real task, or a working but unauthorized communication channel. | [Cases, selected parallels, conditional proof, results and sources](./extensions/family/README.md) |

All three use the [same evidence and review criteria](./extensions/CRITERIA_AND_AUDIT.md). Their detailed statuses and existing evidence remain in their own documents and the [technical table](./extensions/CRITERIA_AND_AUDIT.md#retained-extension-review-table).

<a id="guía-de-lectura"></a>
## Reading guide

| To consult | Entry |
|---|---|
| Problem, rules and base configuration | [R01 scenario v0.6](./Escenario-creatividad-validacion.md). |
| Method governing the three extensions | [Contract, evidence, fifteen groups and A25](./extensions/CRITERIA_AND_AUDIT.md). |
| Proof and scope of transfer | [Kernel and obligations E1–E7](./extensions/family/KERNEL_AND_PROOF.md) · [References and EA–control comparison](./extensions/METHODOLOGICAL_FOUNDATIONS.md). |
| Each case and its checks | [Table of the three extensions](#extensiones). |
| Earlier trials and retained results | [Case history](./extensions/hugging-face/README.md#historial-de-ensayos-y-trabajo-pendiente). |
| Joint reproduction and editorial review | [Common command](#reproducción-conjunta-de-las-comprobaciones) · [Review procedure and outcome](./extensions/EDITORIAL_REVIEW.md). |

The conditional formal proof, finite checks and experiments with agents are different forms of evidence. The first two have documents and bounded results; the full execution of R01 and the EA comparison remain pending. Current verdicts are consulted in the common records; earlier work retains its date and scope.

<a id="reproducción-conjunta-de-las-comprobaciones"></a>
## Joint reproduction of the checks

From this `00G-R01/` folder:

```sh
python3 extensions/verify_audit.py --verify
```

The [common verifier](./extensions/verify_audit.py) runs the three checkers in temporary folders, compares their reports and verifies the textual hashes. It uses Python 3 and its standard library. The [common report](./extensions/audit_results.json) preserves results per package; it does not add them together as independent samples. The individual guides remain available in the extensions table.

This is an internal rerun of the published code, not an independent replication or an EA evaluation. The editorial procedure, content preservation and limits of this review are in the [package review](./extensions/EDITORIAL_REVIEW.md).

<a id="archivos-y-reproducción-editorial"></a>
## Files and editorial reproduction

The existing Word and PDF files preserve **v0.6 before the reading separation**. They include the former case chapter; the current separated reading edition is in Markdown. This section describes the exports of the **base scenario v0.6**. In the extensions, the current review is in Markdown; the Infoblox Word file preserves the v0.5 edition preceding its later additions, identified in its case record.

Markdown is the current text source; the retained Word and PDF files are exports of the earlier complete v0.6 text. The two original figures, the new scenario–acceptance diagram and their generation script are in this package. `build_figures.py` regenerates the figures with Matplotlib and `build_document.py` regenerates Word with python-docx. The PDF is exported from Word with LibreOffice. The scripts resolve their paths from this folder. A simulator is not yet included: the experiment's executable rules remain pending.

The current reading edition separates the base and case documents; the earlier complete text is preserved in the organization record. Local drafts 0.1–0.5, conversational revisions, verification renders and temporary files are not part of the package. Public earlier work remains linked for its documentary role.

## Earlier section links

<a id="lugar-de-la-reducción-dentro-de-00g"></a>
[Reduction explanation](./reductions/00G-to-R01/README.md#lugar-de-la-reducción-dentro-de-00g).

<a id="fundamento-y-prueba-de-la-reducción"></a>
[Reduction explanation](./reductions/00G-to-R01/README.md#fundamento-y-prueba-de-la-reducción).

<a id="cómo-se-hace-la-reducción"></a>
[Reduction explanation](./reductions/00G-to-R01/README.md#cómo-se-hace-la-reducción).

<a id="identificación-y-estado"></a>
[Reduction explanation](./reductions/00G-to-R01/README.md#identificación-y-estado).

<a id="control-del-test-y-alcance-del-oráculo-c3"></a>
[Earlier evaluator and trial history](./extensions/hugging-face/README.md#control-del-test-y-alcance-del-oráculo-c3).

<a id="historial-de-ensayos-y-trabajo-pendiente"></a>
[Earlier evaluator and trial history](./extensions/hugging-face/README.md#historial-de-ensayos-y-trabajo-pendiente).


<a id="viability-work-in-progress"></a>
## Viabilidad del trilema — trabajo en desarrollo

El estudio se reúne en una subcarpeta propia de R01. Los escenarios, reducciones, resultados y exports permanecen intactos. El contenido anterior de las colas se conserva en [el snapshot](./feasibility/previous-work/QUEUE_SNAPSHOT_2026-10-04.json); el único orden actual está en [WORKPLAN.md](./feasibility/WORKPLAN.md): cuatro tareas activas y tres entregas posteriores.

| Trabajo | Entrada | Estado y siguiente paso |
|---|---|---|
| Documento de viabilidad | [Estudio completo](./feasibility/README.md) · [Prueba matemática base](./feasibility/PURE_MATHEMATICAL_TRILEMMA.md) | Trilema por familias y regiones viables; no imposibilidad en toda configuración. Derivación F disponible, revisión independiente y puente a R01 pendientes. |
| Trabajo pendiente | [Plan vigente y 55 tareas](./feasibility/WORKPLAN.md) · [Registro de estados](./feasibility/WORKPLAN_STATUS.json) | Núcleo y revisión propia publicados; continuar con escalación humana y whispering dentro del protocolo de tecnologías. Oráculo y arnés después del contrato. |
| Experimentos parciales | [Inventario separado](./feasibility/partial-experiments/README.md) | Scripts, fixtures, salidas y material adicional conservados. Diagnósticos acotados; no son el oráculo/harness independiente. |
| Borradores y conservación | [Trabajos anteriores](./feasibility/previous-work/README.md) · [Mapa de traslados](./feasibility/RELOCATION_MANIFEST.json) · [Verificación](./feasibility/PRESERVATION_CHECKS.json) | Historial preservado; no se reemplazan resultados anteriores ni se borra el corpus. |
| Continuación | [Prompt completo](./feasibility/CONTINUATION_PROMPT.md) | Mantener el trabajo dentro de esta subcarpeta y el seguimiento al final de los README. |
| Manuscrito independiente | [Trilema condicionado de coste, riesgo y eficacia](./feasibility/CONDITIONED_TRILEMMA.md) | Hipótesis y pruebas autocontenidas, fronteras exactas, regiones por pares y éxito legítimo; preparado para revisión, sin anunciar validación externa. |
| Auditoría del manuscrito | [Revisión propia adversarial](./feasibility/CONDITIONED_TRILEMMA_SELF_REVIEW.md) · [Registro de publicación](./feasibility/CONDITIONED_TRILEMMA_RELEASE.json) | Incluye prior sesgado AVG y contraste WC; M16/M17 siguen pendientes. No se ejecutan nuevos tests científicos. |
| Auditoría de fondo y transferencia | [Dictamen completo](./feasibility/CONDITIONED_TRILEMMA_DEEP_AUDIT.md) · [Mapa, prueba local y familia R01 G](./feasibility/R01_TO_CONDITIONED_TRILEMMA_MAPPING.md) | Distingue capacidad física/objetivo, e/σ y frontera de riesgo/Pareto; G presenta un trilema condicionado con tamaños arbitrarios y catálogo explícito. La misma fórmula F no se extiende indiscriminadamente. Revisión propia, no externa. |
| Estado tras auditoría, 4 de octubre | [Manuscrito v0.2](./feasibility/CONDITIONED_TRILEMMA.md) · [Registro de auditoría](./feasibility/DEEP_AUDIT_RELEASE.json) | Estado histórico de esa entrega; el registro actual depurado gobierna la continuación. M17 pasa a IN_PROGRESS por mapeo/proposición/resultado G; no se cierra una tarea científica ni se ejecutan nuevos tests. M16 y el harness siguen pendientes. |
| Teorema condicionado en R01 — desarrollo vigente | [Demostración principal](./feasibility/R01_CONDITIONED_TRILEMMA_THEOREM.md) · [Revisión propia](./feasibility/R01_CONDITIONED_TRILEMMA_REVIEW.md) | Teorema sobre el dominio R01: corte informativo para toda política, regiones por los tres pares y región viable; familia de dependencia global con K datos, N arbitrario y coste informativo creciente. Casos de éxito compatibles con el trilema. Revisión independiente pendiente. |
| Registro y continuación del teorema R01 | [Entrega](./feasibility/R01_CONDITIONED_TRILEMMA_RELEASE.json) · [Prompt vigente al final](./feasibility/CONTINUATION_PROMPT.md) | Contexto técnico pagado, ledger y productores explícitos; mantén fuente y experimentos históricos intactos. Snapshot histórico de tareas; la cola actual está depurada. Ninguna ejecución científica nueva en esta actualización. |


## Cierre del núcleo matemático — revisión de continuidad v0.2

4 de octubre de 2026. Esta actualización mantiene la demostración ya publicada y aplica reparaciones mínimas: multiplicador recíproco del certificado, cargo de envío/recepción, plazo coherente y control sin veredicto normativo. No aplica tecnologías.

| Lectura vigente | Estado |
|---|---|
| [Teorema condicionado R01 v0.2](./feasibility/R01_CONDITIONED_TRILEMMA_THEOREM.md) | Dominio completo, certificado y corte all-policy; regiones viables y de trilema no vacías; fronteras exactas de la familia AVG/WC. |
| [Auditoría y reparaciones](./feasibility/R01_AUDIT_CONTINUITY_AND_REPAIRS.md) · [Revisión propia](./feasibility/R01_CONDITIONED_TRILEMMA_REVIEW.md) | Reconstrucción propia completada. M16 OPEN; fidelidad independiente M17 IN_PROGRESS. |
| [Registro de conservación](./feasibility/R01_AUDIT_CONTINUITY_RELEASE.json) | Escenario y archivos históricos intactos; sin nuevas ejecuciones científicas. |
| Próxima fase | Protocolo definido; aplicar sus pasos a escalación humana y whispering como primera tecnología. |

**Referencia canónica — estado documental posterior:** [Trilema R01 v0.2](./feasibility/R01_CONDITIONED_TRILEMMA_THEOREM.md), documento independiente con enunciado y pruebas conservados. [Explicación enlazada](./Escenario-creatividad-validacion.md#r01-conditioned-mathematical-validation). Umbrales b, δ y p explícitos; validación propia y revisiones externas reconocidas, cobertura restante delimitada.


## Continuación verificada: revisión de extensiones y tecnologías por mecanismos

4 de octubre de 2026. Se verificó el cierre publicado del núcleo v0.2 y se completó la revisión propia de coherencia de las tres extensiones. Los estados anteriores están archivados íntegramente; la cola actual sustituye sus instrucciones de continuación.

| Trabajo actual | Evidencia y alcance |
|---|---|
| Núcleo matemático | [Teorema único](./feasibility/R01_CONDITIONED_TRILEMMA_THEOREM.md); corte observable explicitado y presupuesto global precisado, sin cambiar fronteras. |
| Tres extensiones existentes | [Revisión de coherencia](./feasibility/EXTENSION_CONSISTENCY_REVIEW.md); alcances conservados y discrepancias heredadas de hashes registradas, sin ejecutar checkers. |
| Extensión tecnológica ordenada | [Protocolo](./feasibility/TECHNOLOGY_EXTENSION_PROTOCOL.md): primero núcleo isomórfico, luego mecanismos adicionales y pruebas de aceptación/persistencia. |
| Escalación humana y whispering | [Primera ficha matemática](./feasibility/HUMAN_ESCALATION_WHISPERING.md): cota con información compartida, frontera de alerta suficiente y controles; coste y plazo condicionados. |
| Validación pendiente | M16 OPEN, M17 IN_PROGRESS; P08 conserva las discrepancias documentales; integración, arnés y campaña sin ejecutar. |
| Estado | Cuatro tareas actuales y tres entregas posteriores; los 55 IDs y criterios históricos siguen trazables. No se declara una nueva validación científica. |


| Recorridos virtuales tecnológicos — actualización al final | Estado |
|---|---|
| [Escalación humana y whispering](./feasibility/HUMAN_ESCALATION_WHISPERING.md#virtual-traversals) | Explicación general incorporada antes de los recorridos; R1/R2/R3 examinados bajo contrato, con controles positivos. R2 recupera escenarios y R3-A conserva una región residual. |
| Continuación | Misma cola: cuatro frentes activos y tres etapas posteriores. La primera entrega virtual está realizada; las siguientes candidatas reutilizan su estructura. |
| Alcance | Revisión propia matemática/virtual; sin tecnología real, campaña ni nueva ejecución científica. Ensayos anteriores siguen como anexos parciales no canónicos. |
