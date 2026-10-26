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
