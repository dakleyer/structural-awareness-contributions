# Revisión de 00M-A01 — cómo se conecta el mecanismo con los requisitos

**Una sola VNext del documento lógico 00M-A01.** Auditoría por Codex, 6 de octubre de 2026; asistente de IA del mismo chat, sin auditor independiente. [Fuente v0.1](./00M_A01_MECHANISM_TO_REQUIREMENTS_TRACEABILITY_v0.1_WORKING_PROPOSAL.md) · [procedimiento](../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md).

Este documento permite seguir una pregunta: ¿qué parte de una obligación podría ayudar a cubrir cada operación propuesta y qué tendría que demostrarse todavía? La tabla es una orientación para investigar, no prueba de que el sistema cumpla.

## Instrucciones de Iván y alcance real

Iván pidió preservar los documentos, reutilizar una VNext por documento, hacer pasadas distintas y revisar las relaciones antes de preparar texto antes/después. La publicación de estas notas está autorizada; aplicar propuestas no.

Fuente leída completa, §§1–7, blob `8761f877bace65e3b6ab560e8a79c9ed821f57e5` en commit `2db5a8c17f58008f9268c23c681ba6e14c8dfbdc`. Se contrastó la tabla con 00M §§3–7, 00N §§3.2–3.5 y Requirements §§2–4. Las cuatro lecturas siguientes están documentadas; **no cierran la revisión de todos sus consumidores, pruebas o implementaciones**.

## Primera pasada: fondo y lógica

**Auditoría realizada por Codex:** seguimiento de las cuatro operaciones y examen de cada no-claim.

Reconocer roles no establece verdad ni permiso. Relacionar scopes necesita una correspondencia justificada, y componer debe conservar las distinciones necesarias. Recalificar puede señalar una necesidad de revisión; no ejecuta por sí misma una respuesta. §1 conserva correctamente este orden argumental sin imponer una ejecución serial.

La asociación muchos-a-muchos es razonable: una obligación puede requerir varias operaciones, y una operación puede contribuir a varias obligaciones. No debe interpretarse la columna “Primary routes” como exhaustividad ni la columna de condiciones como condiciones ya satisfechas. La tabla contiene dependencias, no resultados.

La pequeña inconsistencia de exposición es que M1–M4 aparecen como nombres locales en la tabla después de una lista sin esos nombres. Un lector podría pensar que pertenecen a otra arquitectura canónica. La propuesta final los declara como referencias internas de esta tabla.

## Segunda pasada: evidencia y vínculos

**Auditoría realizada por Codex:** comparación de frases, no solo coincidencia de identificadores.

S5/S14 requieren preservar indeterminación y el sentido decisional de la evidencia; M1 ayuda, pero no reemplaza su disposición acotada. S9/S11 requieren no sustituir dominios y conservar conflicto/dependencias; M2/M3 describen una contribución compatible. S6 exige privacidad e interoperabilidad: §3 aclara acertadamente que tamaño pequeño no las prueba. S12/S13 requieren historia y determinación vigente separadas; preservar una referencia no construye el proceso de reparación.

T1 reclama una rotura material observable en una frontera declarada, no cualquier alerta. T2 reclama un resultado con postura y dueño receptor, no solo transporte de metadatos. T3 permanece externo a la indicación, aunque debe estar acoplado al perfil completo. T4 incluye toda la carga y el margen de respuesta: §4 conserva su carácter pendiente. Esto coincide con [00N VNext](./00N_VNext.md).

H1 y H2 no son equivalentes: insuficiencia dentro de una ventana difiere del residual fuera de ella. H3 y H4 tampoco: posible pérdida por composición difiere de suficiente preservación acotada. H5 requiere variación/frescura; un recorrido estático no la prueba. H6 requiere comparación de frontera riesgo/recursos, no contar mensajes ahorrados. La tabla no añade H7.

La referencia entrante desde [04 VNext](./04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) usa este documento como ayuda de trazabilidad. No transfiere autoridad a 00M-A01 ni convierte una operación en requisito. Falta revisar integralmente esa revisión y todos los perfiles que puedan consumirla. Los enlaces a sus tres fuentes existen en el árbol fijado.

## Tercera pasada: edición y estructura

**Auditoría realizada por Codex:** recorrido de §§1–7 y lectura horizontal de la matriz.

El orden funciona: propósito, tabla, requisitos, condiciones, hipótesis y límites. La tabla de seis columnas contiene varias familias por celda y exige mantener abiertos otros documentos. Puede seguir como tabla técnica si recibe antes una explicación corta de S/T/H y del carácter local de M1–M4.

No se detectó en las filas una obligación creada por renumeración. Las expresiones de apoyo (“supports”, “primarily”) deben mantenerse, porque cambiarlas a cumplimiento alteraría el sentido. Las referencias finales repiten las tres fuentes de forma útil.

No se ha probado un render de esa tabla en todos los tamaños de pantalla; la lectura textual no certifica su presentación móvil.

## Cuarta pasada: comprensión humana

**Auditoría realizada por Codex:** relectura simulada desde las preguntas de quien llega sin conocer las siglas.

Puede entenderse la cadena si se lee §1; resulta más difícil reconocer que S son obligaciones, T condiciones conjuntas y H preguntas experimentales. Una breve explicación antes de la tabla evita que la lectura se reduzca a “M2→S9→H4”.

Para valorar una fila, el lector debería preguntar qué información nueva aporta, qué condiciones necesita y qué no resuelve. La columna de no-claim responde la última pregunta, pero la introducción debería formular las tres.

No participó un lector humano independiente. Esa revisión y la conciliación extensa siguen abiertas.

## Conversación y continuidad

**Codex, auto-revisión:** la correspondencia textual es defendible en este alcance. No demuestra que un perfil real implemente las obligaciones ni que ningún requisito nuevo sea posible en el futuro. Se conserva el falsador de un caso admisible que satisfaga realmente la base y aun así falle.

La propuesta de ruta se registra también en la [VNext del README de baseline](./README_VNext.md) y en [EP README VNext](../../../architectural-contributions/ecosystem-positioning/README_VNext.md), sin redistribuir archivos.

## Propuesta quirúrgica — pendiente

**Localización:** §2, encabezado único. **Fuente:** blob anterior. **Instrucción:** preparación autorizada por la revisión de Iván. **Tipo:** orientación añadida, sin cambio de tabla.

**Texto antes:**

```markdown
## 2. Compact traceability
```

**Texto después:**

```markdown
## 2. Compact traceability

Read each row as a research route: what the operation may contribute, which conditions it needs, and what it cannot establish. S1–S14 are specification obligations, T1–T4 are jointly constraining sufficiency conditions, and H1–H6 are hypotheses to test. M1–M4 are local shorthand for the four operations listed above; they are not a new canonical function family. The table does not report conformance.
```

**Efecto:** facilitar lectura sin cambiar S/T/H ni afirmar ejecución. **Dependencias:** ninguna redistribución; 04 y README reciben el límite de autoridad de esta ayuda. **Antes verificado:** una coincidencia. **Decisión de Iván:** pendiente. **Incorporación:** no ejecutada.


---

## Quinta pasada — investigación externa, diferencial y reutilización

**Instrucción de Iván, 6 de octubre de 2026. Estado: contraste específico pendiente.** Esta quinta pasada se realiza después de las cuatro y queda dentro de esta misma VNext. No se crea otro expediente ni se incorporan propuestas a la fuente por esta anotación.

**Pregunta de este documento:** Comparar la trazabilidad mecanismo–función–requisito con métodos externos de conservación y verificación. Comprobar que las correspondencias aporten información revisable y no atribuyan un resultado operativo a una semejanza de vocabulario.

Se fijarán trabajos primarios de FG-TIDA y de otras líneas relevantes, incluidos antecedentes y actualizaciones posteriores, con autor, versión, fecha y alcance realmente leído. Aquí se justificará qué coincide, qué diferencia podría sostenerse y qué pieza concreta conviene reutilizar, con sus condiciones de atribución, adaptación y compatibilidad.

El [mapa externo preparatorio](../../../governance/review/EP_EXTERNAL_RESEARCH_REVIEW_2026-10-06.md) aporta fuentes iniciales; no completa esta pasada. El [plan 1.6](../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#quinta-pasada--trabajos-externos-diferencial-y-reutilización) gobierna método y cierre. Las cuatro lecturas previas mantienen sus estados reales y se reabren si aparece evidencia que las afecte. Codex, mismo asistente de IA; anotación de alcance, sin independencia externa.


---

## Sexta pasada unificadora — preparación y continuidad

**Instrucción de Iván, 6 de octubre de 2026. Preparación registrada por Codex, mismo asistente de IA. Estado: pendiente de lanzamiento después de las cinco pasadas del corpus.** Esta anotación organiza el trabajo futuro; no declara una auditoría unificadora realizada ni cambia el estado de las lecturas anteriores.

**Pregunta de consolidación de este documento:** Seguir cada correspondencia mecanismo–función–requisito hasta su consumidor y evidencia, y verificar que una coincidencia conceptual no se convierta en garantía operativa.

Los hallazgos concretos se comentarán aquí y en las VNext de los documentos relacionados, conservando respuestas y desacuerdos. Se cotejarán las propuestas con la fuente actual y sus consumidores antes de presentar candidatos consolidados antes/después. La [sexta pasada del plan](../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#sexta-pasada-unificadora-y-consolidación) fija el lanzamiento y el método. Se preservan fuente, historia y decisión de Iván para incorporar cambios.


---

## Prioridades del plan de cambios — revisión del corte

**Revisión realizada por Codex, 6 octubre de 2026, mismo asistente de IA.** Se revisan las auditorías y propuestas ya registradas para valorar impacto esperado, riesgo y esfuerzo. La fuente pública del corte es `7500dd5ee05c1a5052a28d35a8cefaf2c530707f`; los viejos y pares anteriores permanecen íntegros. Esta revisión no completa las pasadas pendientes ni la sexta.

El [plan 1.11](../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#prioridad-de-cada-cambio--impacto-riesgo-y-esfuerzo) explica los criterios y el [listado completo](../../../governance/review/change-priorities-2026-10-06/priorities.json) conserva las fuentes y los pares. La prioridad sirve para preparar tandas de decisión; la incorporación depende de Iván y de las comprobaciones indicadas.

| Cambio | Prioridad / tanda | Impacto esperado | Riesgo | Esfuerzo | Estado |
|---|---|---|---|---|---|
| 6 · Explicar cómo leer la tabla mecanismo–requisito | Siguiente · 4 — Lectura humana y rutas | Medio | Bajo | Bajo | Pendiente de decisión |

### Cambio 6 — Explicar cómo leer la tabla mecanismo–requisito

**Impacto esperado: Medio. Riesgo: Bajo. Coste/esfuerzo: Bajo. Prioridad: Siguiente.** Separar obligación, condición, hipótesis y abreviatura local de la tabla.

**Qué podría quedar desactualizado o afectado:** Presentar M1–M4 como nueva familia normativa o confundir trazabilidad con conformidad.

**Qué cuesta prepararlo:** Un párrafo de orientación y cotejo de S/T/H; ningún nuevo campo.

**Dependencias conocidas:** [00M_A01_MECHANISM_TO_REQUIREMENTS_TRACEABILITY_v0.1_WORKING_PROPOSAL.md](00M_A01_MECHANISM_TO_REQUIREMENTS_TRACEABILITY_v0.1_WORKING_PROPOSAL.md) · [00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md](00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md). La lista es el mapa conocido para preparar la decisión, no certificación de todos los consumidores.

**Estado y condición:** Pendiente de decisión. Candidato para revisión documental concreta. Mantener la tabla y límites; confirmar preservación de la fuente fijada antes de incorporar.

**Viejo y nuevo:** el par literal sigue en [la entrada anterior](00M_A01_VNext.md#propuesta-quirúrgica--pendiente); el viejo tiene una coincidencia en [la fuente actual](00M_A01_MECHANISM_TO_REQUIREMENTS_TRACEABILITY_v0.1_WORKING_PROPOSAL.md), blob `8832c255e3775116046273363c131c05878af16d`. Localizar el viejo no prueba compatibilidad de la propuesta ni autoriza incorporación.


---

## Revisión a fondo de los planes de cambio — 6 octubre 2026

**Evaluación realizada por Codex, mismo asistente de IA, para que una persona pueda decidir.** Se revisan el plan, sus motivos de auditoría, pares literales, impacto, riesgo, esfuerzo y dependencias; no es la sexta pasada científica global ni acredita el cierre de las cinco. Fuente de este cotejo: commit `03db21016d6a0831a43d7a99d3640854ab549777`, [documento propietario](00M_A01_MECHANISM_TO_REQUIREMENTS_TRACEABILITY_v0.1_WORKING_PROPOSAL.md), blob `8832c255e3775116046273363c131c05878af16d`. Los registros anteriores y sus viejos completos permanecen íntegros.

La valoración actual distingue una mejora documental de una modificación conceptual o de contrato. **Candidato para revisión documental significa preparado para leer y decidir, no autorizado para incorporar.** Los originales siguen en sólo lectura; no se ejecuta ninguno de estos pares.

| Cambio | Calidad/estado actual | Impacto esperado | Riesgo | Esfuerzo | Prioridad |
|---|---|---|---|---|---|
| 6 | Documental condicionado; Pendiente de decisión | Medio | Bajo | Bajo | Siguiente |

**Cambio 6 — Documental condicionado.** La matriz ya separa contribución y cumplimiento. DeclararM1–M4 como referencias locales reduce confusión, sin convertirlas en canon.

**Beneficio esperado:** Separar obligación, condición, hipótesis y abreviatura local de la tabla. **Riesgo concreto:** Presentar M1–M4 como nueva familia normativa o confundir trazabilidad con conformidad. **Coste de preparar y mantener:** Un párrafo de orientación y cotejo de S/T/H; ningún nuevo campo.

**Localización actual:** viejo completo 1 coincidencia(s); texto propuesto 0 coincidencia(s), fuente actual completa. No se interpreta una cita o una subcadena del encabezado como modificación aplicada.

**Condición y orden de decisión:** Comprobar las cuatro filas y sus no-claims. Fuente identificada: mantener original; decisión sobre una edición futura/ficha, sin aplicar sobre el hash publicado. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

[Visión conjunta y tandas en EP README VNext](../../../architectural-contributions/ecosystem-positioning/README_VNext.md#revisión-a-fondo-de-los-planes-de-cambio--6-octubre-2026). Mantener tres niveles de README, fuentes congeladas, resultados y binarios. Reorganización, nueva campaña, experimentos e incorporación canónica permanecen fuera de esta entrega.
