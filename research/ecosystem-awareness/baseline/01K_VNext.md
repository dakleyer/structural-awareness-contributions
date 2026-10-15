# VNext — Capacidad humana, escalada y deuda 01K

> [!IMPORTANT]
> **Superseding source decision — 6 October 2026.** The current 01K source has been reconciled with the complete Tegrity.AI Human Intelligence Debt / Human Intelligence Gap series under Iván's explicit instruction. Human Intelligence Debt is **not** a runtime queue/capacity deficit and is **not** defined in HIT. The controlling architecture is HICR/HICT/HID, operationalised at task level by GIC/NEO/ACW and the Paper-5 measurement programme. Runtime Human Capacity is a separate 01K surface.
>
> Therefore the earlier HIT-ledger findings and proposed Changes **64 and 67 below are SUPERSEDED / NOT PENDING**. They remain in this file only as audit history showing how the earlier interpretation was rejected. Do not implement them, do not put them back into the priority queue, and do not use their formulas as HID.
>
> Current source: [01K Human Capacity / Human Intelligence Debt](01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md), integration commit `9f397df86fb66217937fbf08b3c99e0f46bc60a6`, blob `cbdf679dd396ed4bf5e13d3368c6834349b31962`.

> **Auditoría realizada por Codex, 6 de octubre de 2026; mismo asistente de IA.** Escrita para lectura y revisión posterior de una persona; no auditor humano independiente. [Fuente actual](01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md), v0.1, texto completo §§1–13 leído en `8757ba614c94f962206912d4896c119a18a924fa`, blob `38fcb757c662e2ea40ca24865f90cad2cca4bc98`. Original intacto. [Plan de Iván](../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md).

## Primera pasada — tiempo, trabajo cognitivo y contabilidad

La idea sostiene que nombrar a una persona, enviarle una alerta o reservarle minutos no acredita competencia, contexto, autoridad o capacidad de revisar a tiempo. Es una extensión consumida por la arquitectura, no un nuevo interrupt humano ni un permiso. La fuente mantiene HIT como unidad relativa, sin medir el valor de una persona o demostrar rendimiento.

**Hallazgo:** §4 descuenta HIT_committed de la capacidad y luego resta la capacidad restante a HIT_demand_committed. Si ambos committed nombran el mismo trabajo, aparece doble cargo. Ejemplo conceptual propio: nominal 10, comprometido 6, degradación 0; disponible 4 y HID 2, aunque el compromiso 6 cabe en 10. No es dato humano ni resultado del corpus.

Convención A: comparar demanda total comprometida con capacidad neta antes de reservas. Convención B: comparar sólo nueva demanda incremental con reserva restante. Las dos pueden servir, pero no se pueden mezclar. 64 propone A dejando explícita B; requiere decidir con Iván y propietarios del perfil.

Otro problema de tipo: §3 admite clases ordinales y §4 hace restas. Una clase “Alta” no es una cantidad aditiva; 67 limita la aritmética a una escala/ledger justificados y preserva estados cualitativos cuando no la hay. No se inventa una conversión universal ni calibración.

## Segunda pasada — fuente y retorno material

Operation nueva §4.1 y Signalling nueva §5.2 consumen 01K opcionalmente, preservando qualification, Cart/RA y gates ACC/autoridad. Un estado AVAILABLE errado podría influir en encaminamiento aunque no otorgue permiso. Por eso 64/67 se registran también en [Operation VNext](../../../standards/minimum-sufficient-control/04_OPERATION_VNext.md) y [Signalling VNext](01J_VNext.md).

La fuente cita UC03 congelado y HEW como rutas de validación, no validación de HIT. Se registra esta dependencia en [UC03 VNext](UC-EA-03_VNext.md); no se reinterpreta el resultado congelado. Contratos, datos y análisis HEW no examinados completos aquí: segunda parcial. La deuda es una definición de ledger por aclarar, no un hallazgo psicológico.

## Tercera pasada — fórmulas y estructura

Texto completo examinado. La advertencia humanos≠tokens y el objetivo preceden a fórmulas y validación. Los bloques hacen visibles dos términos casi iguales que deben distinguir total/reserva/incremental; ese problema afecta sentido, no sóloformat. Las clases AVAILABLE/DEGRADED/UNAVAILABLE/UNKNOWN no son una escala aditiva por llevar nombres. No se propone proliferación de etiquetas.

## Cuarta pasada — lectura humana

Simulación por el mismo asistente. Una persona entiende “estar en la cola” distinto de “haber recibido revisión útil”. La comparación de una hora clicando frente a intervención corta exigente explica por qué minutos no bastan. Pero no aporta una equivalencia medida de HIT. El caso 10/6 permite revisar el ledger sin conocimientos del chat; debe quedar visible para quien decida.

## Quinta pasada — carga subjetiva y propuestas de FG-TIDA

**Contraste específico realizado.** [NASA-TLX, página oficial](https://www.nasa.gov/human-systems-integration-division/nasa-task-load-index-tlx/), NASA Ames / Sandra Hart; página actualizada el 11 de marzo de 2026, marcada como referencia histórica. Se leyeron descripción, seis subescalas y permiso de uso/modificación del tool. Es carga subjetiva multidimensional, no stock de capacidad HIT ni garantía de throughput. Pieza candidata: observación de carga mental/temporal/esfuerzo para una calibración separada; manual antes deuso, sin convertir automáticamente puntuación en HIT. Código, app y datos no seleccionados. Artículo Hart–Staveland de 1988 no recuperado en este intento; no se extiende permiso de la herramienta a reimprimir el artículo. No diferencialHIT demostrado.

[Theme16, comentario de dakleyer29agosto2026](https://github.com/FG-TIDA/themes/issues/16#issuecomment-5462496736) propone capacidad finita/ventana útil; [Theme13, NellInc/NellWatson4octubre2026](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5985312999) propone objeción y dueño accountable. Textos leídos: propuestas, sin adopción demostrada ni experimentos reproducidos. No establecen unidades aditivasHIT o deuda. Derechos de importación no establecidos, código y datos no importados; referencia atribuida. Las investigaciones citadas por esos comentarios no se declaran leídas por leer elcomentario.

## Estado y decisiones

Primera, tercera y cuarta textuales realizadas; segunda material abierta; quinta específica realizada en alcance declarado. Sexta global pendiente.64/67: impactoAlto/riesgoAlto/esfuerzoMedio/prioridad Primera, juntos. La decisión precisa es **qué ledger y escala usa el perfil**, antes devalidación de consumidores o cualquier incorporación. No es autorización para medir personas o recalcular resultados.

## Plan de cambios — viejo visible

### Cambio 64 — Evitar doble conteo de trabajo comprometido en HID

**Fuente/ubicación:** [fuente actual](01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md), commit `8757ba614c94f962206912d4896c119a18a924fa`, blob `38fcb757c662e2ea40ca24865f90cad2cca4bc98`; viejo único. **Impacto esperado: Alto. Riesgo: Alto. Esfuerzo: Medio. Prioridad: Primera. Tanda: 2 — Coherencia entre RA, EA y MSCA.**

**Beneficio:** Que una reserva dentro de capacidad no produzca deuda por contarla dos veces. Es esperado, no eficacia medida. **Riesgo:** Puede cambiar clasificación/human routing y comparacionesHEW/UC03; requiere fijar total frente a incremental. **Coste:** Conciliar ledger, ventana, unidades y consumidores; no recalcular resultados congelados.

**Texto antes — viejo literal completo:**

```markdown
A bounded working definition of **Human Intelligence Debt (HID)** is:

~~~text
HID(W)
=
max(
  0,
  HIT_demand_committed(W) - HIT_available(W)
)
~~~

Human Intelligence Debt means that the system has committed, queued or generated qualified cognitive demand that cannot presently be satisfied within the relevant response window under the declared reviewer pool and assumptions.

```

**Texto después — propuesto completo:**

```markdown
A bounded working definition of **Human Intelligence Debt (HID)** first fixes one ledger and response window. If HIT_demand_committed denotes the same total reserved work already deducted as HIT_committed, compare it with capacity before that reservation deduction:

~~~text
HID(W)
=
max(
  0,
  HIT_committed(W)
  - (HIT_nominal(W) - HIT_degradation(W))
)
~~~

Here HID is committed demand exceeding the qualified capacity available before reservations. HIT_available remains the remaining reserve after reservations; the same committed work is not charged twice.

If a profile instead compares new, additional demand with that remaining reserve, it MUST name that incremental demand separately and show that it excludes the work already represented by HIT_committed. These are different ledger conventions, not interchangeable inputs.

Human Intelligence Debt is a profile-relative capacity deficit within the declared response window and reviewer-pool assumptions; this arithmetic does not establish an empirically calibrated cognitive metric.

```

**Dependencias/orden:** [01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md](01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md) · [04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md](../../../standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md) · [01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md](01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md). Elegir convención con Iván y conciliar67/consumidores; fuentes/resultados intactos. Estado: Pendiente de decisión; autorización existente sólo de publicación. Instrucciones de Iván: conservarviejo, relaciones, prioridades y decisión concreta antes deincorporar; ninguna aplicación por esta revisión.

### Cambio 67 — Limitar la aritmética HIT a unidades aditivas declaradas

**Fuente/ubicación:** [fuente actual](01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md), commit `8757ba614c94f962206912d4896c119a18a924fa`, blob `38fcb757c662e2ea40ca24865f90cad2cca4bc98`; viejo único. **Impacto esperado: Alto. Riesgo: Alto. Esfuerzo: Medio. Prioridad: Primera. Tanda: 2 — Coherencia entre RA, EA y MSCA.**

**Beneficio:** Que aceptar clases ordinales no legitime restas o precisión cognitiva inexistente. Es esperado, no eficacia medida. **Riesgo:** Afecta medición y estados que consumenOperation/01J/UC03/HEW; no inventar conversión universal. **Coste:** Declarar escala, additivity/overlap y ventanas, contraste con calibración; sin pruebas con humanos.

**Texto antes — viejo literal completo:**

```markdown
For a reviewer or reviewer pool J in response window W:

~~~text
HIT_available,J(W)
=
HIT_nominal,J(W)
-
HIT_committed,J(W)
-
HIT_degradation,J(W)
~~~

The degradation term is a working representation of capacity loss associated with fatigue, sustained monitoring, context switching, repetitive approval work or other declared factors. This annex does not prescribe one physiological model.

```

**Texto después — propuesto completo:**

```markdown
For a reviewer or reviewer pool J in response window W, an arithmetic capacity ledger applies only when the deployment declares a common additive HIT scale, compatible task/reviewer scope and consistent window semantics:

~~~text
HIT_available,J(W)
=
HIT_nominal,J(W)
-
HIT_committed,J(W)
-
HIT_degradation,J(W)
~~~

An ordinal workload class is not by itself an additive quantity. Where only ordinal classes are supported, retain a qualified class/capacity state rather than subtracting class labels or reporting a numerical debt.

The degradation term is a profile-defined capacity loss; its calibration, evidence and overlap with already committed work must remain explicit. This annex does not prescribe a physiological model or establish calibration by naming HIT.

```

**Dependencias/orden:** [01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md](01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md) · [04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md](../../../standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md) · [01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md](01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md). Tanda 64/67 y decisión de Iván; no se activa calibración o campaña. Estado: Pendiente de decisión; autorización existente sólo de publicación. Instrucciones de Iván: conservarviejo, relaciones, prioridades y decisión concreta antes deincorporar; ninguna aplicación por esta revisión.


---

## Revisión a fondo de los planes de cambio — 6 octubre 2026

**Evaluación realizada por Codex, mismo asistente de IA, para que una persona pueda decidir.** Se revisan el plan, sus motivos de auditoría, pares literales, impacto, riesgo, esfuerzo y dependencias; no es la sexta pasada científica global ni acredita el cierre de las cinco. Fuente de este cotejo: commit `03db21016d6a0831a43d7a99d3640854ab549777`, [documento propietario](01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md), blob `e52ed065c5d217da73634c7eb28d26c5d990abae`. Los registros anteriores y sus viejos completos permanecen íntegros.

La valoración actual distingue una mejora documental de una modificación conceptual o de contrato. **Candidato para revisión documental significa preparado para leer y decidir, no autorizado para incorporar.** Los originales siguen en sólo lectura; no se ejecuta ninguno de estos pares.

| Cambio | Calidad/estado actual | Impacto esperado | Riesgo | Esfuerzo | Prioridad |
|---|---|---|---|---|---|
| 64 | Superado por la fuente; SUPERSEDED / NOT PENDING | Alto | Alto | Medio | Histórico |
| 67 | Superado por la fuente; SUPERSEDED / NOT PENDING | Alto | Alto | Medio | Histórico |

**Cambio 64 — Superado por la fuente.** El viejo ledgerHIT ya no está en 01K. La definición actual separa capacidad runtime de HICR/HICT/HID; el par64 no es aplicable.

**Beneficio esperado:** Que una reserva dentro de capacidad no produzca deuda por contarla dos veces. **Riesgo concreto:** Puede cambiar clasificación/human routing y comparacionesHEW/UC03; requiere fijar total frente a incremental. **Coste de preparar y mantener:** Conciliar ledger, ventana, unidades y consumidores; no recalcular resultados congelados.

**Localización actual:** viejo completo 0 coincidencia(s); texto propuesto 0 coincidencia(s), fuente actual completa. No se interpreta una cita o una subcadena del encabezado como modificación aplicada.

**Condición y orden de decisión:** Conservar el antes histórico y no reutilizar su fórmula como HID. Examinar la nueva serie/componente dentro de 01K antes de proponer algo contra la fuente actual. Revisar junto con 67. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

**Cambio 67 — Superado por la fuente.** La restaHIT anterior dejó de ser la definiciónHID vigente. Corregirla como si siguiera gobernando mezclaría dos arquitecturas.

**Beneficio esperado:** Que aceptar clases ordinales no legitime restas o precisión cognitiva inexistente. **Riesgo concreto:** Afecta medición y estados que consumenOperation/01J/UC03/HEW; no inventar conversión universal. **Coste de preparar y mantener:** Declarar escala, additivity/overlap y ventanas, contraste con calibración; sin pruebas con humanos.

**Localización actual:** viejo completo 0 coincidencia(s); texto propuesto 0 coincidencia(s), fuente actual completa. No se interpreta una cita o una subcadena del encabezado como modificación aplicada.

**Condición y orden de decisión:** Conservar historia y no recrear64/67. RevisarHC runtime y HID arquitectura separadamente, con fuentes del nuevo01K-A01 y sus consumidores. Revisar junto con 64. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

**Consecuencia entre documentos:** [64](01K_VNext.md#revisión-a-fondo-de-los-planes-de-cambio--6-octubre-2026), [67](01K_VNext.md#revisión-a-fondo-de-los-planes-de-cambio--6-octubre-2026), [68](01J_VNext.md#revisión-a-fondo-de-los-planes-de-cambio--6-octubre-2026), [69](01J_VNext.md#revisión-a-fondo-de-los-planes-de-cambio--6-octubre-2026), [70](01J_VNext.md#revisión-a-fondo-de-los-planes-de-cambio--6-octubre-2026). 64/67 ya no describen la fuente vigente de HID: las antiguas observaciones del ledger quedan como historia, sin volver a la cola. El nuevo componente HC-HID/01K-A01 y sus fuentes mantienen revisión material pendiente dentro del mismo propietario 01K. Estas conexiones conservan el desacuerdo y las condiciones de cada fuente; no fabrican consenso ni permiso de ejecución.

[Visión conjunta y tandas en EP README VNext](../../../architectural-contributions/ecosystem-positioning/README_VNext.md#revisión-a-fondo-de-los-planes-de-cambio--6-octubre-2026). Mantener tres niveles de README, fuentes congeladas, resultados y binarios. Reorganización, nueva campaña, experimentos e incorporación canónica permanecen fuera de esta entrega.

**Recepción del plan de identidad01K-A01:** el contrato del componente tiene ahora [su VNext existente](01K_A01_HUMAN_CAPACITY_HID_COMPONENT_SPEC_v0.1_VNext.md); se revisó su par, ya incorporado. Este expediente01K sigue siendo dueño de investigación/medición y sus fuentes, mientras A01 define implementación. La distinción no reabre 64/67 ni acredita un HID empírico; riesgos de transferir autoridad o evidencia se valoranMedio y requieren fuentes/receptores en una revisión futura.


## Content preservation CP-01 — restore the explicit human-time condition

**14 October 2026 · Codex · change93.** The content review compares the former 01K edition with the rewritten current source, then checks the component consumer. Five metric expressions still exist in current §7; their presentation changed. Runtime capacity, HID architecture use and the bounded signal/ACC interface remain distinct. The specific issue here is the explicit required-human-work condition in §15.

**Historical source gate — complete previous passage**

```markdown
~~~text
HumanEscalationViable_i(τ,W)
=
qualified route exists
AND applicable human authority exists
AND qualified reviewer/case fit exists
AND required HumanTime fits W
AND expected decision latency fits W
~~~
```

The current compact gate omits `AND required HumanTime fits W` while retaining expected latency. The old time-demand condition and the current information-sufficiency condition can coexist. CP-01 restores the former explicit condition while preserving every current condition. 01K-A01's runtime acceptance/scheduling interpretation and UC-EA-03 capacity semantics must be read with it; this review does not infer an implementation failure from the text change.

**Source:** [research/ecosystem-awareness/baseline/01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md](https://github.com/dakleyer/structural-awareness-contributions/blob/f16b3ba1ef36bb3ff62b02eb89748838c66e8073/research/ecosystem-awareness/baseline/01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md) · blob `e52ed065c5d217da73634c7eb28d26c5d990abae · §15 Gate A, runtime viability. This Human Escalation Gate A is not DDS Stage A.

### Text before — current, literal and complete

```markdown
~~~text
HumanEscalationViable_i(tau,W)
=
qualified route exists
AND applicable authority exists
AND qualified reviewer/case fit exists
AND information is sufficient for the requested decision
AND expected latency fits W
~~~
```

### Text after — proposed, complete

```markdown
~~~text
HumanEscalationViable_i(tau,W)
=
qualified route exists
AND applicable authority exists
AND qualified reviewer/case fit exists
AND information is sufficient for the requested decision
AND required HumanTime fits W
AND expected latency fits W
~~~
```

**Expected impact: High. Risk: Medium. Effort: Medium. Priority: First, content-preservation wave.** The benefit is an explicit finite human-work admission condition, so availability/latency alone cannot silently stand in for required work fitting the window. Risk concerns the meaning and units of HumanTime, committed work and scheduling assumptions in component/oversight consumers; no interface field or runtime code is changed by this text proposal. Preparation includes reading those consumers and checking that one source clarification preserves their capacity/timing meanings.

**Dependencies:** 01K-A01 component/runtime acceptance; UC-EA-03 capacity source; Human Escalation and EHD receiving use. **Acceptance:** every current condition remains and exactly the former required-HumanTime condition is added in the registered location; the chosen consumers document the same bounded-time meaning. Current old passage verified once; the proposal is not already in the source.

**Iván's instruction:** retain every part of the information, use existing VNext, show old and proposed text and apply only after the GO for the named wave. **Decision/state:** published proposal; not applied; consumer reconciliation required before incorporation. The [whole-corpus literal review](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#content-within-surviving-files--literal-preservation-review-14-october-2026) provides the supporting record and distinguishes exact preservation from rewriting, review custody and Git-only history.


## Damage-control consumer reconciliation — 14 October 2026

The [plan DC-06](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#damage-control-and-restoration-plan--14-october-2026) adds receiving evidence to CP-01/change93. Current 01K-A01 §§5.2–5.4 already include backlog/service time, response-window state and `sum_i x_ij * ServiceDemand_ij(q) <= AvailableServiceTime_j(W)`, explicitly necessary but not sufficient for all scheduling constraints. The missing compact01K line does not establish a missing component capability. Restore explicit source meaning only after comparing units, concurrent commitments, release/deadline constraints, scheduling proof class, UNKNOWN and receiver qualification.

The complete current component passage is published in DDS VNext; the original before/proposed change93 remains unchanged in01K VNext. Candidate93 stays High impact / Medium risk / Medium effort, not ready or applied. Compare component schema/vectors/verification, UC-EA-03 freeze and working successor, EHD/general-interface and current Flores mapping before choosing a literal restoration, qualified cross-reference or justified no-edit disposition. No schema, scheduling engine, result or frozen source changes by this review.


## Second contract review — capacity and the change93 alternative, 14 October 2026

Reviewer `/root/gate_capacity_adversary`, separate source-first contract reviewer. [Common second-pass record](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#second-damage-review-pass--separate-source-first-reviewers-14-october-2026); [component/schema judgement](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/01K_A01_HUMAN_CAPACITY_HID_COMPONENT_SPEC_v0.1_VNext.md#second-contract-review--complete-component-and-schema-14-october-2026); [UC03 receiver](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/UC-EA-03_VNext.md#second-contract-review--uc-ea-03-working-successor-14-october-2026). All primary source bodies were fully read; complete consumer closure remains distinct.

## 6. 01K: historical/current capacity and full section dispositions

### Exact material runtime passages

Historical 01K §8:

```text
HumanEscalationViable_i(τ,W)
=
qualified route exists
AND applicable human authority exists
AND qualified reviewer/case fit exists
AND required HumanTime fits W
AND expected decision latency fits W
```

Current 01K §14:

```text
RuntimeHumanCapacity_J(W) = [
  route_reachable,
  qualified_reviewer_available,
  competence_case_fit,
  authority,
  information_sufficiency,
  queue_or_committed_work,
  expected_ack_latency,
  expected_decision_latency,
  fallback_or_backup,
  response_horizon
]
```

Current 01K §15:

```text
HumanEscalationViable_i(tau,W)
=
qualified route exists
AND applicable authority exists
AND qualified reviewer/case fit exists
AND information is sufficient for the requested decision
AND expected latency fits W
```

Literal omission is real. Information sufficiency was added and should remain. `expected latency fits W` is ambiguous if a reader treats it as acknowledgement or transport latency; the parent says “expected latency” while §14 distinguishes acknowledgement from decision. Current A01 explicitly models completion, so omission is not proof of lost runtime service-time semantics.

Historical/current 01K substantive preservation by section:

| Current section | Disposition / old contribution / limitation |
|---|---|
| Header and A01 route | Retain source-owner/component split; body v0.2 despite filename v0.1. Version labels are real provenance, not maturity. |
| 1 Purpose | Retains runtime vs architectural questions from old §§2–4; neither answer entails the other. |
| 2 Component contract | New four-surface split; optionality and UNKNOWN/NOT MEASURED preserved. A mandatory runtime consumer still requires its material inputs. |
| 3 Definition | Old §2 conceptual HICT/HICR/HID retained; definition is not empirical measurement. |
| 4 Period/frontier | Expanded counterfactual scope; model imitation alone is not debt. External paper's entire evidence not audited here. |
| 5 Measurement correction | Tiered replaceability evidence retained/expanded; observed benchmark is not an organisation's measurement. |
| 6 GIC/NEO/ACW | Retains exclusive task-time classes and distinguishes necessary oversight from avoidable work. |
| 7 Metric family | Five historical expressions retained plus NOI; HICR vs HICR_time naming needs declared measurement reading, not silent universal units. |
| 8 Harvester multiplication | New detailed mechanism context; app count alone not HID. No source-paper empirical validation asserted. |
| 9 Incentives | New detailed model; explicitly hypothesis, not causal closure. |
| 10 Entropy/recovery | Expanded hypothesis from old §2; rho not inferred from fragmentation. |
| 11 Measurement layers | New context/internal/dynamic structure; cognitive load not classifier, deficit not decay. |
| 12 Evidence Notes | Evidence licensing separate from organisational execution; incompatible panels not pooled. |
| 13 Study gates | Expanded Study0–5; do not construe all later research studies as prerequisites for every descriptive output, but empirical HID gate remains mandatory. |
| 14 Runtime capacity | Receives old §3 and §9; explicit queue/commitments, freshness-related state and dual latencies. Literal Human Time field not listed. |
| 15 Two-gate rule | Receives old §4 and §8; CP-01 omission real, conditional candidate below. Architectural gate is review question, not automatic incident veto. |
| 16 HIT units | Retains old §4 rejection of universal HIT/HID token construct. Do not revive changes64/67. |
| 17 Human Escalation | Receives old §5 (including its duplicated heading only as historical artefact); route receipt ≠ effective intervention ≠ debt-neutral design. |
| 18 Alert | Receives old §6 with optional governance trigger; no fifth primitive signal/command. |
| 19 Subscription | Receives old §7; routing≠authority, notification≠capacity. Authorized silence exception remains scoped. |
| 20 Repositioning | Receives old §8 bounded HOLD/UNRESOLVED and ACC/authority gates; output cannot manufacture capacity. |
| 21 Cost of Clarity bridge | Expanded research context; not an HID formula or transferred proof. |
| 22 Attribution bridge | Independent formal machinery retained; convergence not proof. |
| 23 Informational Friction bridge | Distinct ideal/counterfactual framing preserved; not silently unified. |
| 24 AI Operational Integrity bridge | NOI/threshold prediction, not observed threshold result. |
| 25 AI Integrity Management bridge | Managed-remnant hypothesis with rho uncertainty; no universal implementation mandate. |
| 26 RA bridge | Receives old §10, retains no direct HID→RA output identity; no cross-series proof. |
| 27 Organisational profile | Optional field envelope; qualitative valid, numerical requires instruments/gates. |
| 28 Dashboard | New integration view, not standard or validation. Runtime row not fungible with cognitive hours. |
| 29 Design review | New fourteen architecture questions; value/safety of current necessary NEO cannot be negated by high debt. |
| 30 Claim status | Definition/framework versus diagnostic support versus open hypotheses retained; do not call definitions empirical validation. |
| 31 UC03/HEW | Receives old §12; richer routes cited, no native/human validation inherited. Current link uses v0.4 freeze, successor requires explicit reading. |
| 32 Contributor lineage | Receives old §1 public source links; no institutional adoption follows. |
| Annex A | Research source map, not full external-source audit. |
| Annex B | Bridge meanings/limits preserved separately. |
| Annex C | Minimum organisational study data; instrumentation/independence/source cuts remain required. |
| Annex D | Receives old §13 canonical thesis; current incident necessity, interfaces and optional architecture review kept separate. |

Historical §11 ACC ownership remains across current §§17–20 and Annex D, but there is no complete identical current ACC-example list. Historic protected-objection/non-retaliation, acknowledgement and alternate-owner examples are retained history; their selective absence is not authority to introduce new obligations into every component. Every example is conditional on its actual ACC/profile owner.

Applicability: 01K research/source map and runtime readers. Impact High for capacity admission and external claims, risk Medium for compact phrase changes, effort Medium for bounded wording and High for all-consumer engineering closure. **No numerical HID or token repair is applicable.**

## 9. CP-01/change93: decision and exact alternative candidate

**Current decision:** preserve the published literal candidate unchanged as historical proposal; do not apply it. It is not decision-ready. Changes64/67 remain superseded and must not be restored as HID arithmetic. The new candidate below is a pending alternative for the same existing 01K owner, not a new active contract or approved supersession.

Why the existing candidate is underspecified: `required HumanTime fits W` could mean demand≤elapsed window, per-reviewer residual service capacity, a feasible schedule for concurrent obligations, or a universal cognitive unit. These meanings are not interchangeable. Existing A01 §5.4 deliberately says a demand/capacity inequality is only necessary. A pool may have enough aggregate minutes while no qualified available route can meet a particular deadline; a short transport/ack latency may coexist with long backlog and review time. No code or experiment was run to make those conceptual distinctions.

**BEFORE — literal current 01K §15 Gate A block:**

```text
HumanEscalationViable_i(tau,W)
=
qualified route exists
AND applicable authority exists
AND qualified reviewer/case fit exists
AND information is sufficient for the requested decision
AND expected latency fits W
```

**AFTER — supported narrower cross-reference alternative, pending owner judgement:**

```text
HumanEscalationViable_i(tau,W)
=
qualified route exists
AND applicable authority exists
AND qualified reviewer/case fit exists
AND information is sufficient for the requested decision
AND required qualified human service demand is feasible within W
    under the declared 01K-A01 capacity/timing model and proof class
AND expected review-completion latency fits W
```

**Proposed immediately following interpretive paragraph, pending:**

> Here, human service demand is route- and competence-specific work time, not a universal unit of intelligence or an HID metric. Read feasibility with 01K-A01 §§5.2–5.4, including backlog, current commitments, release times, deadlines, non-preemptible work and any material precedence constraints. The necessary load condition alone is not a sufficient scheduling proof. The consuming policy determines which declared proof classes are admissible; unresolved material inputs remain UNKNOWN. This gate qualifies the human review path and does not establish the correctness, authority, execution or effect of the eventual intervention.

Support: all substantive requirements already appear in A01 §§3.1–3.4/5.1–5.4/8.7/14 and 01K §§1/14/17–20. This is preferable to unqualified literal restoration because it gives required work a bounded, existing-owner meaning and makes review-completion latency explicit. It still needs consumer reconciliation: no generic effect deadline or proof-class policy is invented.

Risk/impact/effort: High impact, Medium risk, Medium preparation effort. It may change how compact-text-only consumers read expected latency and feasibility. Confirm the chosen block does not force every runtime consumer to implement an exact scheduler, upgrade heuristics to proof, or make the optional HID engine mandatory. The same policy must retain the consumer's actuation/effect deadline if that is the material useful horizon.

Acceptance before adoption: pin exact current passage; decide meaning of W and completion for this consumer; identify route/pool/competence, commitments convention, time units/epoch, proof acceptance and unknown handling; compare frozen/working UC03, EHD/01J/Operation/HEW actual receivers; retain original candidate93 pair and rejection/supersession reason; obtain Iván's GO for the exact chosen pair. No new schema or result field follows automatically from adopting prose. **Not approved, not applied, all material consumers not closed.**

For A01 itself, this pass deliberately proposes **no exact active replacement** for the quantile formula, proof-policy pseudocode or metric input contract. Their interpretation depends on facts not established in this delegated cut. Record pending owner questions with exact current passages; do not hide them inside a broad 01K restoration.



### Complete candidate93 alternative — literal current source delimiters retained

The reviewer body above supplies the rationale. The exact pair below retains the source’s tilded delimiters and includes the whole proposed following paragraph; one original match verified. The original93 pair remains visible and pending until a concrete choice.

**Text before — complete current block:**

````markdown
~~~text
HumanEscalationViable_i(tau,W)
=
qualified route exists
AND applicable authority exists
AND qualified reviewer/case fit exists
AND information is sufficient for the requested decision
AND expected latency fits W
~~~
````

**Text after — complete alternative block and paragraph:**

````markdown
~~~text
HumanEscalationViable_i(tau,W)
=
qualified route exists
AND applicable authority exists
AND qualified reviewer/case fit exists
AND information is sufficient for the requested decision
AND required qualified human service demand is feasible within W
    under the declared 01K-A01 capacity/timing model and proof class
AND expected review-completion latency fits W
~~~

Here, human service demand is route- and competence-specific work time, not a universal unit of intelligence or an HID metric. Read feasibility with 01K-A01 §§5.2–5.4, including backlog, current commitments, release times, deadlines, non-preemptible work and any material precedence constraints. The necessary load condition alone is not a sufficient scheduling proof. The consuming policy determines which declared proof classes are admissible; unresolved material inputs remain UNKNOWN. This gate qualifies the human review path and does not establish the correctness, authority, execution or effect of the eventual intervention.
````

High expected impact / Medium risk / Medium effort. Not decision-ready: complete frozen/current UC03, EHD/01J/Operation/HEW and actual adapter judgement remains required. No schema/code/result/freeze change follows from publishing this proposal.


## Unified restoration candidates 15 October 2026

The [independent unified plan](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#unified-restoration-plan-15-october-2026) re-evaluates these existing proposals against their current sources and receivers. The passages below are complete current preparations, pending their stated decision gates. Earlier alternatives and audits remain visible.


### Existing candidate 93

Literal absence is real, but current01K14 and A015.2–5.4 retain capacity semantics. Prefer precise service-demand/proof-class qualification; all consuming deadlines and proof policies still need reconciliation.

**Impact / risk / effort:** Alto / Medio / Medio. **State:** Not decision-ready: consumer timing/proof-policy reconciliation incomplete.

**Source:** [research/ecosystem-awareness/baseline/01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md](https://github.com/dakleyer/structural-awareness-contributions/blob/89273f548f6b5ed8f7e0576040f615b5653ffaf6/research/ecosystem-awareness/baseline/01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md), blob `e52ed065c5d217da73634c7eb28d26c5d990abae`. Dependencies: 01K-A01; UC-EA-03; Human Escalation/EHD consumers

**Text before — complete current passage (1).**

``````text
~~~text
HumanEscalationViable_i(tau,W)
=
qualified route exists
AND applicable authority exists
AND qualified reviewer/case fit exists
AND information is sufficient for the requested decision
AND expected latency fits W
~~~
``````

**Text after — complete proposal.**

``````text
~~~text
HumanEscalationViable_i(tau,W)
=
qualified route exists
AND applicable authority exists
AND qualified reviewer/case fit exists
AND information is sufficient for the requested decision
AND required qualified human service demand is feasible within W
    under the declared 01K-A01 capacity/timing model and proof class
AND expected review-completion latency fits W
~~~

Here, human service demand is route- and competence-specific work time, not a universal unit of intelligence or an HID metric. Read feasibility with 01K-A01 §§5.2–5.4, including backlog, current commitments, release times, deadlines, non-preemptible work and any material precedence constraints. The necessary load condition alone is not a sufficient scheduling proof. The consuming policy determines which declared proof classes are admissible; unresolved material inputs remain UNKNOWN. This gate qualifies the human review path and does not establish the correctness, authority, execution or effect of the eventual intervention.
``````

This is the same pending proposal, with its unified-review assessment, rather than another action under an alias. The complete earlier record remains above. Apply only an explicitly selected pair/wave; preserve every other source byte and its recorded freezes, evidence and results. [Joint plan and acceptance checks](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#unified-restoration-plan-15-october-2026).


## Coupled literal capacity preparation 15 October 2026

Existing93 remains pending and complete above. New107/108 in the [A01 VNext](./01K_A01_HUMAN_CAPACITY_HID_COMPONENT_SPEC_v0.1_VNext.md) supply the full joint timing/proof-policy text;109 in [UC03 VNext](./UC-EA-03_VNext.md) binds the working caller. These form one scoped consumer wave. Its original frozen profiles, schema and results remain unchanged. [Joint acceptance/order](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#literal-restoration-plan-15-october-2026).
