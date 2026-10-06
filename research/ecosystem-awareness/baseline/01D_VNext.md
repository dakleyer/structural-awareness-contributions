# Revisión de 01D — que las piezas hablen de la misma operación

**Única VNext del perfil conjunto EA/MSCA/RA.** Auditoría realizada por Codex, 6 de octubre de 2026; asistente de IA del mismo chat. [Fuente](./01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md) · [nota externa](./01D_REVIEW_CARD.md) · [plan](../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md).

## Fuente e instrucciones

Iván confirmó todo Contributions dentro de la revisión y pidió conservar las integraciones. Se leyó completo 01D, §§1–7 y sus tablas: blob `c9cb2d1326f016db89ec41f9945638e25ecbbead`, commit `e80846a0f9cf3b97cf222ed3d1e28b31d145ad3e`.

Hay cuatro lecturas distintas del texto. El cotejo integral de 01B/01C, las fuentes externas y las realizaciones siguen pendiente; **no se declara integración ejecutada ni cierre global**.

## Primera pasada — fondo y lógica

**Auditoría realizada por Codex:** examen de binding, dependency set y precedencia.

Dos informes correctos por separado pueden hablar de decisiones, scopes o versiones distintas. El perfil exige enlazarlos con la misma operación y ventana. Suficiencia de control, seguridad de respuesta y permiso permanecen preguntas distintas.

La excepción de RA advisory es necesaria: un monitor no requerido no veta una acción independiente. Cuando una acción se justifica con RA, su evidencia y límites sí entran en sus condiciones necesarias. Esta diferencia evita un “si falta un campo, parar todo” y evita usar RA como sello opcional para la misma acción que depende de él.

El costo compartido se atribuye una vez; no se suman dos veces minutos de la misma persona. PNI de una respuesta acotada tampoco demuestra cumplimiento del objetivo o mínimo costo del conjunto. El argumento mantiene condiciones y límites.

## Segunda pasada — fuentes y relaciones

**Auditoría realizada por Codex:** cotejo de 01C §2, pasajes de 01B y entradas de MSCA Operation.

01D refiere la proyección amplia Δ_RA en §1, pero su tabla y sus reglas operacionales usan predominantemente P_RA del detector mínimo. No puede suponerse que ambos objetos sean intercambiables. Una operación que consume Δ_RA necesita declarar qué componentes y qualifiers utiliza y si aplica una especialización al contrato mínimo. Hace falta ese mapping; no se deduce del nombre compartido RA.

Las [VNext de 01C](./01C_VNext.md) y de [MSCA Operation](../../../standards/minimum-sufficient-control/04_OPERATION_VNext.md) conservan el contraste del productor y receptor. Los resúmenes de RA/Operation confianza-intensidad no resuelven este binding.

Las citas al paper EWS y a la arquitectura urbana no se verificaron en esta entrada. 01D declara que sus reglas son propuestas propias y no resultados de esos papers; esa separación se mantiene. La frase final “independent review” es una atribución histórica del documento que requiere identificar su evidencia, no independencia demostrada por esta auto-revisión.

## Tercera pasada — edición y formato

**Auditoría realizada por Codex:** lectura horizontal de las tablas y de la secuencia §§1–7.

La tabla de binding relaciona contenido retenido, dueño y consecuencia de mismatch. Se puede seguir de ella a las seis reglas y a ocho pruebas propuestas. La columna de qualifiers hace falta tanto para un valor numérico como para un estado desconocido.

Los tests T1–T8 son nombres locales de este perfil; no deben confundirse con las condiciones canónicas T1–T4. Lo mismo vale para P_RA, P_MSCA y las posturas P1/P2/P3. El texto aclara los P, pero los T requieren una orientación explícita si otro documento los referencia sin ruta/versión.

El estado de qualification separado del valor evita que ausencia de señal se codifique como cero. Sus estados son candidatos de interfaz, no salidas nuevas retroactivamente atribuidas al detector.

## Cuarta pasada — comprensión humana

**Auditoría realizada por Codex:** relectura simulada, sin participación humana independiente.

El ejemplo de señal fresca con permiso viejo es claro: conservar la señal no autoriza despachar la acción. El ejemplo de receipt sin effect también explica por qué recibir una respuesta no cierra la operación.

La diferencia entre monitor opcional y dependencia requerida puede explicarse con una pregunta sencilla: ¿esta acción necesita esa evidencia para estar justificada? La misma falta de dato tiene consecuencias distintas según la respuesta.

Al llegar desde el RA actual, el lector puede esperar Δ_RA y encontrar P_RA en las tablas. Una frase de alcance/mapping ayudaría; no hay que inventar la correspondencia ni un parser universal para hacer el documento más legible.

## Conversación y continuidad

**Codex, auto-revisión:** el perfil documenta condiciones útiles de composición. No prueba que un sistema cumpla esas condiciones ni que cubra todas las nuevas variantes de delta. [Conciliación conjunta](../../../governance/review/EP_REVIEW_INTEGRATIONS_2026-10-06.md).

La propuesta vuelve a los README VNext de [EA](../README_VNext.md), [RA](../../regime-awareness/README_VNext.md), [MSCA](../../../standards/minimum-sufficient-control/README_VNext.md) y [EP](../../../architectural-contributions/ecosystem-positioning/README_VNext.md). Se mantiene una sola VNext y no se desplaza la propiedad del control o permiso.

## Propuesta antes/después — declarar el puente de representación

**Localización:** §2, párrafo único de reconciliación de símbolos. **Instrucción:** revisión completa segura de Iván. **Tipo:** adición que condiciona un perfil de integración; revisar su alcance y consumidores antes de adoptar.

**Texto antes:**

```text
The symbol P_RA denotes the source-defined **RA directional detector output** (called directional posture in the minimal-detector paper); P_MSCA denotes the MSCA intervention/planning dimension. They are **not the same variable**. P_RA is not one of the three EA/Positioning operating postures. In particular, RA neutral (P_RA = 0) is not EA Normal Operation, and RA Pointwise Non-Inferiority (PNI) is not an MSCA proof of S/E/C/P_MSCA/M sufficiency.
```

**Texto después:**

```text
The symbol P_RA denotes the source-defined **RA directional detector output** (called directional posture in the minimal-detector paper); P_MSCA denotes the MSCA intervention/planning dimension. They are **not the same variable**. P_RA is not one of the three EA/Positioning operating postures. In particular, RA neutral (P_RA = 0) is not EA Normal Operation, and RA Pointwise Non-Inferiority (PNI) is not an MSCA proof of S/E/C/P_MSCA/M sufficiency. Where an operation instead consumes the broader Δ_RA=[A_RA,B_RA,C_RA,D_RA] position, its profile must declare the source-qualified mapping and the components and qualifiers actually relied upon. It must not manufacture P_RA from a confidence value or assume that the broader delta inherits every minimal-detector or response-safety claim.
```

**Razón:** hacer explícita la relación entre representaciones preservando permiso, semántica y prueba propios. **Dependencias:** 01C/01B, RA/EA/MSCA, Operation y implementaciones de la composición. **Antes comprobado:** una coincidencia. **Decisión:** pendiente. **Incorporación:** no ejecutada.


---

## Quinta pasada — investigación externa, diferencial y reutilización

**Instrucción de Iván, 6 de octubre de 2026. Estado: contraste específico pendiente.** Esta quinta pasada se realiza después de las cuatro y queda dentro de esta misma VNext. No se crea otro expediente ni se incorporan propuestas a la fuente por esta anotación.

**Pregunta de este documento:** Comparar mecanismos externos de binding, contexto, autorización y evaluación conjunta. Identificar qué componentes ya pueden reutilizarse y qué contrato adicional exige que todos hablen de la misma operación y ventana útil.

Se fijarán trabajos primarios de FG-TIDA y de otras líneas relevantes, incluidos antecedentes y actualizaciones posteriores, con autor, versión, fecha y alcance realmente leído. Aquí se justificará qué coincide, qué diferencia podría sostenerse y qué pieza concreta conviene reutilizar, con sus condiciones de atribución, adaptación y compatibilidad.

El [mapa externo preparatorio](../../../governance/review/EP_EXTERNAL_RESEARCH_REVIEW_2026-10-06.md) aporta fuentes iniciales; no completa esta pasada. El [plan 1.6](../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#quinta-pasada--trabajos-externos-diferencial-y-reutilización) gobierna método y cierre. Las cuatro lecturas previas mantienen sus estados reales y se reabren si aparece evidencia que las afecte. Codex, mismo asistente de IA; anotación de alcance, sin independencia externa.


---

## Sexta pasada unificadora — preparación y continuidad

**Instrucción de Iván, 6 de octubre de 2026. Preparación registrada por Codex, mismo asistente de IA. Estado: pendiente de lanzamiento después de las cinco pasadas del corpus.** Esta anotación organiza el trabajo futuro; no declara una auditoría unificadora realizada ni cambia el estado de las lecturas anteriores.

**Pregunta de consolidación de este documento:** Conciliar la composición EA/MSCA/RA con sus contratos propietarios: misma operación, scope, versión y ventana; separar calificación y permiso y preservar cuándo RA es una dependencia requerida.

Los hallazgos concretos se comentarán aquí y en las VNext de los documentos relacionados, conservando respuestas y desacuerdos. Se cotejarán las propuestas con la fuente actual y sus consumidores antes de presentar candidatos consolidados antes/después. La [sexta pasada del plan](../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#sexta-pasada-unificadora-y-consolidación) fija el lanzamiento y el método. Se preservan fuente, historia y decisión de Iván para incorporar cambios.


---

## Prioridades del plan de cambios — revisión del corte

**Revisión realizada por Codex, 6 octubre de 2026, mismo asistente de IA.** Se revisan las auditorías y propuestas ya registradas para valorar impacto esperado, riesgo y esfuerzo. La fuente pública del corte es `7500dd5ee05c1a5052a28d35a8cefaf2c530707f`; los viejos y pares anteriores permanecen íntegros. Esta revisión no completa las pasadas pendientes ni la sexta.

El [plan 1.11](../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#prioridad-de-cada-cambio--impacto-riesgo-y-esfuerzo) explica los criterios y el [listado completo](../../../governance/review/change-priorities-2026-10-06/priorities.json) conserva las fuentes y los pares. La prioridad sirve para preparar tandas de decisión; la incorporación depende de Iván y de las comprobaciones indicadas.

| Cambio | Prioridad / tanda | Impacto esperado | Riesgo | Esfuerzo | Estado |
|---|---|---|---|---|---|
| 17 · Explicar la correspondencia P_RA y delta RA | Primera · 2 — Coherencia entre RA, EA y MSCA | Alto | Alto | Medio | Pendiente de decisión |

### Cambio 17 — Explicar la correspondencia P_RA y delta RA

**Impacto esperado: Alto. Riesgo: Alto. Coste/esfuerzo: Medio. Prioridad: Primera.** Evitar que dos representaciones distintas se tomen como equivalentes por enlace.

**Qué podría quedar desactualizado o afectado:** Una correspondencia inventada pierde scope, certeza o condiciones de acción; varios perfiles consumen esas salidas.

**Qué cuesta prepararlo:** Cotejo de productor, 01D, Operation y retorno; no solo edición.

**Dependencias conocidas:** [00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md](00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) · [01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md](01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md) · [README.md](../../regime-awareness/README.md) · [03_MSCA_ECOSYSTEM_COMPOSITION_AND_CONTROL.md](../../../standards/minimum-sufficient-control/03_MSCA_ECOSYSTEM_COMPOSITION_AND_CONTROL.md) · [04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md](../../../standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md) · [01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md](01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md) · [01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md](01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md). La lista es el mapa conocido para preparar la decisión, no certificación de todos los consumidores.

**Estado y condición:** Pendiente de decisión. Conciliar contrato y consumidores. Declarar qué mapping está justificado y qué sigue pendiente; no inventar wire fields.

**Viejo y nuevo:** el par literal sigue en [la entrada anterior](01D_VNext.md#propuesta-antesdespués--declarar-el-puente-de-representación); el viejo tiene una coincidencia en [la fuente actual](01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md), blob `c9cb2d1326f016db89ec41f9945638e25ecbbead`. Localizar el viejo no prueba compatibilidad de la propuesta ni autoriza incorporación.


---

## Continuación de 01C — payloads y separación de propietarios

**Auditoría cruzada realizada por Codex, 6 octubre de 2026; mismo asistente de IA.** El cotejo de payloads 01C confirma que 01D §4 impide UNKNOWN→P_RA=0 y §§2/5/6 conserva operación/versión, dependencia condicional y coste. Los nuevos candidatos 52/53 no reemplazan el mapping P_RA/Δ_RA ya propuesto: un perfil amplio aún debe justificarlo. El candidato 54 conserva rol vinculado versus evidencia de conducta; no nueva autoridad ni permit.

La explicación, cobertura y viejos/nuevos están en [01C VNext](01C_VNext.md#lectura-de-los-payloads-y-sus-propietarios--continuación-sustantiva-de-01c), con el extremo productor en [Composition VNext](../../../standards/minimum-sufficient-control/03_COMPOSITION_VNext.md) y [Role VNext](../../../standards/minimum-sufficient-control/02_ROLE_VNext.md). Se preservan todas las conversaciones anteriores, decisiones y riesgos. No se declara ejecución o nueva validación independiente.


---

## Revisión a fondo de los planes de cambio — 6 octubre 2026

**Evaluación realizada por Codex, mismo asistente de IA, para que una persona pueda decidir.** Se revisan el plan, sus motivos de auditoría, pares literales, impacto, riesgo, esfuerzo y dependencias; no es la sexta pasada científica global ni acredita el cierre de las cinco. Fuente de este cotejo: commit `03db21016d6a0831a43d7a99d3640854ab549777`, [documento propietario](01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md), blob `c9cb2d1326f016db89ec41f9945638e25ecbbead`. Los registros anteriores y sus viejos completos permanecen íntegros.

La valoración actual distingue una mejora documental de una modificación conceptual o de contrato. **Candidato para revisión documental significa preparado para leer y decidir, no autorizado para incorporar.** Los originales siguen en sólo lectura; no se ejecuta ninguno de estos pares.

| Cambio | Calidad/estado actual | Impacto esperado | Riesgo | Esfuerzo | Prioridad |
|---|---|---|---|---|---|
| 17 | Cambio acoplado; no listo; Pendiente de decisión | Alto | Alto | Alto | Primera |

**Cambio 17 — Cambio acoplado; no listo.** Δ_RA amplio y P_RA mínimo no son intercambiables. La precisión exige explicar la especialización, no añadir una traducción ficticia.

**Beneficio esperado:** Evitar que dos representaciones distintas se tomen como equivalentes por enlace. **Riesgo concreto:** Una correspondencia inventada pierde scope, certeza o condiciones de acción; varios perfiles consumen esas salidas. **Coste de preparar y mantener:** Esfuerzo Alto: además de redactar, leer y conciliar productor, receptores, perfiles/materiales y casos límite; comprobar compatibilidad y mantenimiento de versiones antes de una decisión.

**Localización actual:** viejo completo 1 coincidencia(s); texto propuesto 0 coincidencia(s), fuente actual completa. No se interpreta una cita o una subcadena del encabezado como modificación aplicada.

**Condición y orden de decisión:** Cotejar01C→01D→Operation y el retorno Composition para el mismo scope/versión/ventana; RA advisory no veta una acción que no dependa de él. Revisar junto con 35, 37, 38. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

[Visión conjunta y tandas en EP README VNext](../../../architectural-contributions/ecosystem-positioning/README_VNext.md#revisión-a-fondo-de-los-planes-de-cambio--6-octubre-2026). Mantener tres niveles de README, fuentes congeladas, resultados y binarios. Reorganización, nueva campaña, experimentos e incorporación canónica permanecen fuera de esta entrega.
