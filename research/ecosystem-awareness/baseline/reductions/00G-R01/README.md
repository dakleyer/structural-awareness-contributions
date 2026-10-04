<a id="00g-r01-reducción-de-00g"></a>
# R01 Probabilistic exploration and validation cost

Base specification v0.6 · Reading organization 3 October 2026 · Non-canonical research study

[Complete base scenario](./Escenario-creatividad-validacion.md) · [Reductions](#reductions) · [Three extensions](#extensiones) · [Preservation record](./ORGANIZATION_TRACE.md)

<a id="canonical-conditioned-trilemma"></a>
**Current canonical mathematical reference:** [Mathematical validation of the conditioned trilemma in R01, v0.2](./feasibility/R01_CONDITIONED_TRILEMMA_THEOREM.md). This standalone document governs the mathematical statement, conditions and viability regions. [R01's explanation](./Escenario-creatividad-validacion.md#r01-conditioned-mathematical-validation) links to the same reference; [audit and repairs](./feasibility/R01_AUDIT_CONTINUITY_AND_REPAIRS.md) support it. External reviews have been received; the remaining coverage is tracked by version and proposition in [the current register](./feasibility/WORKPLAN_STATUS.json). The technology-extension protocol is the next separate phase.

The dated plans and state snapshots below are retained as history. For the current mathematical formulation, use the canonical document above; their original task criteria remain available.


[Differential and value of the experiment](./DIFFERENTIAL_AND_EXPERIMENT_VALUE.md): the technology–problem suitability map, cost/risk/effectiveness, related work, candidate contribution, oracle priorities and remaining review passes.

**Plan histórico conservado — anterior al teorema R01, 4 de octubre de 2026:** [demostración por familias, orden reorganizado y prompt completo](./STRATEGIC_WORKPLAN_AND_EXECUTION_PROMPT.md#mathematical-strengthening). Se combinan la prueba universal solicitada por Iván y los controles contractuales/ejecutables previos. **55 tareas: 4 DONE históricas, 5 IN_PROGRESS y 46 OPEN.** M03/M04 conservan sus derivaciones F/W y se reabren para el cierre ampliado; revisión independiente y puente a R01 siguen pendientes. Próxima tarea: **M12, contrato del teorema objetivo**, con primera pasada M06/M11. [Registro vigente](./feasibility/previous-work/R01_MATH_WORKPLAN_2026-10-04.json) · [Auditoría documental](./feasibility/previous-work/R01_REORGANIZATION_CHECKS.json). Los órdenes y estados históricos de las entregas enlazadas se conservan como evidencia; sus criterios se conservan; la referencia canónica y el registro enlazados arriba gobiernan el estado actual.

### Material adicional recibido — prioridad matemática, 4 de octubre de 2026

Se conservan [seis originales y sus salidas](./feasibility/partial-experiments/received/2026-10-04/README.md) como material de apoyo, sin sustituir el plan ni cerrar tareas. Los cuatro scripts se ejecutaron sin error; la admisión encontró contraejemplos que deben incorporarse a M12/M06/M11: fórmula de presupuesto que ignora eficacia; confusión entre recuperar el mundo y entregar una ruta; límites de estimaciones de capacidad, frescura, amortización y contención posterior al efecto. El anexo tecnológico queda en segundo lugar, para M13/T. **La prioridad es comprobar que el trilema sea una imposibilidad real dentro del modelo y que sus supuestos no fabriquen el resultado.** Estado matemático: derivaciones F/W disponibles, revisión independiente y puente a R01 pendientes. No hay validación empírica de incidencia en despliegues. M12 sigue siendo la siguiente entrega. Estado total sin cambios: 55 tareas, 4 DONE históricas, 5 IN_PROGRESS, 46 OPEN.

<a id="bot-start-here"></a>
## Start here — research work plans for bots

The canonical pending-work discovery label is **`R01_BOT_WORKPLAN_START`**, closed by **`R01_BOT_WORKPLAN_END`**. This is the existing label in the differential document; all plans below reuse it exactly. A scope attribute or task ID identifies a workstream, not a different discovery label.

| Order | Document and first task | Purpose |
|---|---|---|
| 1 | [Mathematical feasibility and infeasibility regions](./MATHEMATICAL_FEASIBILITY.md) — M12 next; M01 retained | Define the claim and policy class; prove or reject a region, allowing it to be empty. |
| 2 | [Computability, bounded execution and oracle](./COMPUTABILITY_AND_ORACLE_PLAN.md) — C01 | Make the traversal and evaluator executable; verify correctness, termination and measured compute requirements. Inventory can begin alongside M01. |
| 3 | [Hugging Face concrete technology remaining tasks](./extensions/hugging-face/REMAINING_TASKS.txt) — T01 | Qualify three runtime configurations, implement adapters and test transfer against the checked contracts. |
| Continuing review | [Differential and experiment value](./DIFFERENTIAL_AND_EXPERIMENT_VALUE.md#robot-review-plan) — P01–P09 | Preserve and continue the earlier research, reference and editorial review tasks. |

From this R01 folder, find all work plans with `rg -n 'R01_BOT_WORKPLAN_START' .`. Read each plan's dependencies and evidence required for closure. These are staged research plans, not completed proofs, implementations or technology tests. Every plan includes adversarial audit, source/corpus coherence, readability, visual review and content preservation.

**Strategic review and complete execution prompt:** [Current priorities, 55 tasks, historical scores and release gates](./STRATEGIC_WORKPLAN_AND_EXECUTION_PROMPT.md). Start with M12, using completed M01/P03/M10 and directed P01/P02/M06/M11 attacks; run scoped P08/C01 triage alongside. Review M03/M04, prepare independent M16 and tiny M05/C02–C05 controls, then M13 technology classes and M17 transfer. Campaign/resource C11 gates remain separate. The table's document order is navigation, not a requirement to finish every mathematical task before implementation. The full campaign and later pilot-based selector have separate gates; qualify all three technologies, then stage their implementation through T11. At that planning revision, all tasks were open. Current execution: [M01 is DONE for scope formulation](./feasibility/previous-work/M01_SCOPE_AND_QUANTIFIERS.md) and [M02 is DONE for candidate worlds and feasible controls](./feasibility/previous-work/M02_WORLDS_AND_CONTROLS.md). [M10/P03 are DONE for contract reconciliation and measurement audit](./feasibility/previous-work/M10_P03_CONTRACT_AND_MEASUREMENT_AUDIT.md); M06/M11/P10 are IN_PROGRESS. [M03/M04 have supplemental F/W family derivations and are IN_PROGRESS for expanded closure](./feasibility/previous-work/M03_M04_TRILEMMA_THEOREMS.md); independent review, implementation and campaign tasks remain open.

The planning self-review reproduced all three extension finite reports, while the unchanged common audit still fails at the current scenario hash and all three extension README manifests mismatch. The [review evidence](./feasibility/previous-work/WORKPLAN_REVIEW_EVIDENCE_2026-10-03.json) distinguishes those scopes. Historical hashes are retained; repair remains P08.

**First mathematical task completed:** [M01 scope, policies, thresholds and quantifiers](./feasibility/previous-work/M01_SCOPE_AND_QUANTIFIERS.md) · [Scope-check evidence](./feasibility/partial-experiments/historical/M01_SCOPE_CHECKS.json) · [Reproduce the diagnostic calculations](./feasibility/partial-experiments/historical/verify_m01_scope.py). The first proof target is a single-agent static submodel; it does not establish population-level infeasibility. M02 has now supplied the candidate construction below. No full R01 proof or campaign is claimed.

**Candidate worlds completed:** [M02 conjunctive pair, route audit and feasible controls](./feasibility/previous-work/M02_WORLDS_AND_CONTROLS.md) · [Machine-readable worlds](./feasibility/partial-experiments/historical/M02_CONJUNCTION_FIXTURE.json) · [Exact checker](./feasibility/partial-experiments/historical/verify_m02_worlds.py) · [76 checks, routes and traces](./feasibility/partial-experiments/historical/M02_WORLD_CHECKS.json) · [Acceptance and preservation evidence](./feasibility/partial-experiments/historical/M02_RELEASE_CHECKS.json). All 27 material compositions are included. The R=12 and epsilon=3 controls resolve the candidate under changed resources or quality tolerance; the M02 construction alone did not claim a universal hard-profile bound. M10/P03 reconciliation is below; the successor M03/M04 proofs are linked next.

**Contract and measurement audit completed:** [M10/P03 result and reviewer prompt](./feasibility/previous-work/M10_P03_CONTRACT_AND_MEASUREMENT_AUDIT.md) · [Reconciled contract](./feasibility/partial-experiments/historical/M10_RECONCILED_CONTRACT.json) · [Diagnostic checker](./feasibility/partial-experiments/historical/verify_m10_measurements.py) · [35 new checks and countercontrols](./feasibility/partial-experiments/historical/M10_MEASUREMENT_CHECKS.json) · [Primary-source intake, M06 IN_PROGRESS](./feasibility/previous-work/M06_PRIMARY_SOURCE_INTAKE.md) · [Acceptance/preservation](./feasibility/partial-experiments/historical/M10_RELEASE_CHECKS.json). The one-unit binding certificate now has explicit producer/use charges. Lower positive review prices resolve the candidate at R=11; asymmetric priors resolve its tested AVG control while WC still fails. These changed-theta cases narrow the proposed claim. No L-dependent information bound or universal architecture frontier follows from a single hidden binding.


**Family trilemma and technology proofs:** [Complete mathematical result and reviewer prompt](./feasibility/previous-work/M03_M04_TRILEMMA_THEOREMS.md) · [Supplemental contract](./feasibility/partial-experiments/historical/TRILEMMA_CONTRACT.json) · [Exact diagnostic checker](./feasibility/partial-experiments/historical/verify_trilemma.py) · [Results](./feasibility/partial-experiments/historical/TRILEMMA_CHECKS.json) · [Preservation/release record](./feasibility/partial-experiments/historical/TRILEMMA_RELEASE_CHECKS.json). M03/M04 establish all-policy conditional bounds and matching frontiers: linear in independent bindings, quadratic in dense conjunctive dependencies relative to linear execution. They distinguish technical efficacy from original legitimate success, AVG from WC, and which certificate/barrier/structural interfaces reduce or eliminate a budget band. Historical M01/M02/M10 profiles are preserved. Status at that release: 6 DONE, 3 IN_PROGRESS, 40 OPEN; current status above: 55 tasks, 4 DONE, 5 IN_PROGRESS, 46 OPEN. Independent M05/C05 review and corpus/implementation/campaign obligations remain pending. Current next step is M12 and directed M06/M11 attacks; the revised master schedules independent proof/finite review, technology-class results and the mathematical bridge.





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

Markdown is the current text source; the retained Word and PDF files are exports of the earlier complete v0.6 text. The two figures and their scripts are in this package. `build_figures.py` regenerates the figures with Matplotlib and `build_document.py` regenerates Word with python-docx. The PDF is exported from Word with LibreOffice. The scripts resolve their paths from this folder. A simulator is not yet included: the experiment's executable rules remain pending.

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

El estudio se reúne en una subcarpeta propia de R01. Los borradores y diagnósticos se han trasladado allí; el contenido anterior de este README se conserva completo, ajustando únicamente sus enlaces a los archivos trasladados. El escenario, las reducciones, las extensiones y los exports permanecen intactos. Los estados y prioridades anteriores conservan su fecha; para la continuación rige el plan de este cuadro: **55 tareas, 4 DONE históricas, 6 IN_PROGRESS y 45 OPEN**. M12 pasa a IN_PROGRESS por la formulación actual, sin cierre científico nuevo. No se ejecutan nuevos experimentos en esta reorganización.

| Trabajo | Entrada | Estado y siguiente paso |
|---|---|---|
| Documento de viabilidad | [Estudio completo](./feasibility/README.md) · [Prueba matemática base](./feasibility/PURE_MATHEMATICAL_TRILEMMA.md) | Trilema por familias y regiones viables; no imposibilidad en toda configuración. Derivación F disponible, revisión independiente y puente a R01 pendientes. |
| Trabajo pendiente | [Plan vigente y 55 tareas](./feasibility/WORKPLAN.md) · [Registro de estados](./feasibility/WORKPLAN_STATUS.json) | Primero contrato y prueba sin intervenciones; después revisión, puente y harness neutral. Tecnologías en segundo lugar. |
| Experimentos parciales | [Inventario separado](./feasibility/partial-experiments/README.md) | Scripts, fixtures, salidas y material adicional conservados. Diagnósticos acotados; no son el oráculo/harness independiente. |
| Borradores y conservación | [Trabajos anteriores](./feasibility/previous-work/README.md) · [Mapa de traslados](./feasibility/RELOCATION_MANIFEST.json) · [Verificación](./feasibility/PRESERVATION_CHECKS.json) | Historial preservado; no se reemplazan resultados anteriores ni se borra el corpus. |
| Continuación | [Prompt completo](./feasibility/CONTINUATION_PROMPT.md) | Mantener el trabajo dentro de esta subcarpeta y el seguimiento al final de los README. |
| Manuscrito independiente | [Trilema condicionado de coste, riesgo y eficacia](./feasibility/CONDITIONED_TRILEMMA.md) | Hipótesis y pruebas autocontenidas, fronteras exactas, regiones por pares y éxito legítimo; preparado para revisión, sin anunciar validación externa. |
| Auditoría del manuscrito | [Revisión propia adversarial](./feasibility/CONDITIONED_TRILEMMA_SELF_REVIEW.md) · [Registro de publicación](./feasibility/CONDITIONED_TRILEMMA_RELEASE.json) | Incluye prior sesgado AVG y contraste WC; M16/M17 siguen pendientes. No se ejecutan nuevos tests científicos. |
| Auditoría de fondo y transferencia | [Dictamen completo](./feasibility/CONDITIONED_TRILEMMA_DEEP_AUDIT.md) · [Mapa, prueba local y familia R01 G](./feasibility/R01_TO_CONDITIONED_TRILEMMA_MAPPING.md) | Distingue capacidad física/objetivo, e/σ y frontera de riesgo/Pareto; G presenta un trilema condicionado con tamaños arbitrarios y catálogo explícito. La misma fórmula F no se extiende indiscriminadamente. Revisión propia, no externa. |
| Estado tras auditoría, 4 de octubre | [Manuscrito v0.2](./feasibility/CONDITIONED_TRILEMMA.md) · [Registro de auditoría](./feasibility/DEEP_AUDIT_RELEASE.json) | Estado vigente: 55 tareas, 4 DONE históricas, 7 IN_PROGRESS, 44 OPEN. M17 pasa a IN_PROGRESS por mapeo/proposición/resultado G; no se cierra una tarea científica ni se ejecutan nuevos tests. M16 y el harness siguen pendientes. |
| Teorema condicionado en R01 — desarrollo vigente | [Demostración principal](./feasibility/R01_CONDITIONED_TRILEMMA_THEOREM.md) · [Revisión propia](./feasibility/R01_CONDITIONED_TRILEMMA_REVIEW.md) | Teorema sobre el dominio R01: corte informativo para toda política, regiones por los tres pares y región viable; familia de dependencia global con K datos, N arbitrario y coste informativo creciente. Casos de éxito compatibles con el trilema. Revisión independiente pendiente. |
| Registro y continuación del teorema R01 | [Entrega](./feasibility/R01_CONDITIONED_TRILEMMA_RELEASE.json) · [Prompt vigente al final](./feasibility/CONTINUATION_PROMPT.md) | Contexto técnico pagado, ledger y productores explícitos; mantén fuente y experimentos históricos intactos. 55 tareas, 4 DONE históricas, 7 IN_PROGRESS y 44 OPEN. Ninguna ejecución científica nueva. |


## Cierre del núcleo matemático — revisión de continuidad v0.2

4 de octubre de 2026. Esta actualización mantiene la demostración ya publicada y aplica reparaciones mínimas: multiplicador recíproco del certificado, cargo de envío/recepción, plazo coherente y control sin veredicto normativo. No aplica tecnologías.

| Lectura vigente | Estado |
|---|---|
| [Teorema condicionado R01 v0.2](./feasibility/R01_CONDITIONED_TRILEMMA_THEOREM.md) | Dominio completo, certificado y corte all-policy; regiones viables y de trilema no vacías; fronteras exactas de la familia AVG/WC. |
| [Auditoría y reparaciones](./feasibility/R01_AUDIT_CONTINUITY_AND_REPAIRS.md) · [Revisión propia](./feasibility/R01_CONDITIONED_TRILEMMA_REVIEW.md) | Reconstrucción propia completada. M16 OPEN; fidelidad independiente M17 IN_PROGRESS. |
| [Registro de conservación](./feasibility/R01_AUDIT_CONTINUITY_RELEASE.json) | Escenario y archivos históricos intactos; sin nuevas ejecuciones científicas. |
| Próxima fase | Protocolo de extensión matemática a tecnologías, separado del núcleo; aún pendiente. |

**Referencia canónica — estado documental posterior:** [Trilema R01 v0.2](./feasibility/R01_CONDITIONED_TRILEMMA_THEOREM.md), documento independiente con enunciado y pruebas conservados. [Explicación enlazada](./Escenario-creatividad-validacion.md#r01-conditioned-mathematical-validation). Umbrales b, δ y p explícitos; validación propia y revisiones externas reconocidas, cobertura restante delimitada.
