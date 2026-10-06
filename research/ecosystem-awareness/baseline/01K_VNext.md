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
