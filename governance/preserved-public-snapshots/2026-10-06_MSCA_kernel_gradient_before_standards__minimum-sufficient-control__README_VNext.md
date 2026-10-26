# Revisión del README MSCA — suficiencia, relación y autoridad

**Única VNext del README MSCA.** Auditoría por Codex, 6 de octubre de 2026; asistente de IA del mismo chat. [Fuente](./README.md) · [plan](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md). Iván exige revisar todo Contributions conservando las integraciones.

## Fuente y cobertura real

README leído completo, blob `6fd8e576719d23188f719dd35a004945137153cc` en commit `e80846a0f9cf3b97cf222ed3d1e28b31d145ad3e`. Se cotejaron pasajes de Composition/Operation, 01C y el perfil conjunto 01D completo. No se ha auditado íntegramente cada especificación, ACC, ejemplo, fuente externa o consumidor. La evidencia y conciliación siguen abiertas.

## Primera pasada — argumento

**Auditoría realizada por Codex:** examen de representación, assessment y configuración autorizada.

El texto separa una descripción S/E/C/P/M de una configuración cuya suficiencia está sustentada. UNASSESSED, SUPPORTED, FAILED y UNRESOLVED no se confunden; SUPPORTED sigue condicionado por objetivo, ambiente, evidencia, autoridad y vigencia. No promete un mínimo global ni un único óptimo.

La separación de rol estático y operación/repositioning funciona. Cambiar de configuración o de Objective Envelope no puede inferirse de una señal de régimen. MSCA puede proponer o seleccionar, pero no inventa el mandato que autoriza actuar.

El número “tres documentos estáticos” no excluye el cuarto documento dinámico: la estructura lo presenta aparte. Es una división de contenidos, no cuatro sistemas que deban sustituirse.

## Segunda pasada — relaciones y evidencia

**Auditoría realizada por Codex:** cotejo de productores, consumidores y vuelta de información.

Composition & Control mantiene Cart_i y su change-set; RA consume una porción calificada y devuelve delta, overlay y requests. Operation utiliza esa información junto con objetivo/rol/autoridad; no se vuelve el repositorio de RA ni ejecuta automáticamente contención. La vuelta de feedback debe preservar el mismo scope y vigencia.

[01D](../../research/ecosystem-awareness/baseline/01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md) exige la misma operación, S/E y ventana útil, además de separar permiso de SUPPORTED. RA advisory no requerido no veta una acción independiente. Esto impide convertir la mera conexión de módulos en cumplimiento conjunto.

Hay dos precisiones que merecen conciliación. El README usa “element-wise B_Cart confidence” en su tabla, aunque su propia descripción de 03 incluye soporte y reserva caracterizada. Reducir B_Cart a confianza perdería esa distinción. En [04 Operation VNext](./04_OPERATION_VNext.md) se registra además la abreviatura del input RA “direction/intensity/capability/residual”, que debe cotejarse con 01C y la [revisión del README RA](../../research/regime-awareness/README_VNext.md).

El estado “DEFINED” en una tabla de canonicalización describe una especificación documentada, no un ensayo pasado. Las tablas de evidencia, casos y datos de implementación requieren revisión propia. Ningún paper o input publicado transfiere adopción, certificación o óptimo general.

## Tercera pasada — edición y forma

**Auditoría realizada por Codex:** recorrido de las listas de fuentes y la tabla final.

La apertura explica el problema antes de símbolos y estados. Las dos rutas “document set” y “reading route” repiten parte de los destinos, pero la segunda incorpora origen y contextos. La repetición puede orientar si el lector ve que una lista fija propietarios y otra ofrece lectura; no se elimina durante esta auditoría.

La tabla larga de estados ocupa bastante espacio y usa “DEFINED” repetidamente. Una lectura humana necesitará distinguir lo definido, lo propuesto y lo comprobado. La frontera final de evidencia lo aclara, pero podría situarse cerca de la tabla en una futura propuesta.

El README sigue siendo un router propietario. Las menciones a otros README son referencias laterales a EA/RA o contexto de caso; no crean niveles ilimitados.

## Cuarta pasada — comprensión humana

**Auditoría realizada por Codex:** relectura simulada, sin estudio con personas.

Puede entenderse la pregunta “qué configuración autorizada basta para este objetivo y con qué carga”. La lista de cinco dimensiones ayuda. “SUPPORTED” podría sonar a permiso para usarla; el texto explica la separación, que debe seguir visible en los ejemplos.

El lector debe poder distinguir evaluar, recomendar, autorizar, ejecutar y comprobar efecto. La lectura de una especificación no cumple ninguno de esos actos por sí sola. El ciclo compartido necesita evidencia en sus fronteras.

La precisión de B_Cart importa porque una oportunidad evaluable no realizada puede servir a una revisión posterior aunque no sea un número de confianza. Esta revisión propone expresarlo sin ampliar control o autoridad.

## Conversación

**Codex, auto-revisión:** la fuente da una delimitación útil de su rama. Sus pruebas y fuentes extensas no se cierran aquí. El [mapa de integraciones](../../governance/review/EP_REVIEW_INTEGRATIONS_2026-10-06.md), [EA README VNext](../../research/ecosystem-awareness/README_VNext.md) y [EP README VNext](../../architectural-contributions/ecosystem-positioning/README_VNext.md) conservan el cotejo en ambos extremos.

No se cambia la jerarquía, el ownership o una interfaz para corregir una frase. La propuesta final requiere contrastar consumidores y versiones antes de una incorporación de Iván.

## Propuesta antes/después — expresar todo B_Cart

**Localización:** fila única de canonicalización. **Preparación:** autorización de auditoría de Iván. **Tipo:** precisión semántica de explicación; revisar consumidores antes de incorporar.

**Texto antes:**

```markdown
| Semantic/dependency/process structures inside `A_Cart` with element-wise `B_Cart` confidence | **DEFINED in Composition & Control v0.1** |
```

**Texto después:**

```markdown
| Semantic/dependency/process structures inside `A_Cart` with element-wise `B_Cart` established support, validity limits and characterized assessment reserve; confidence is one qualification within that basis | **DEFINED in Composition & Control v0.1** |
```

**Razón:** conciliar la tabla con la descripción actual de 03; no cambiar A_Cart/B_Cart ni crear campos obligatorios. **Dependencias:** 03, 04, EA/RA y perfiles consumidores. **Compatibilidad:** pendiente; el campo compartido no garantiza interpretación idéntica. **Decisión:** pendiente. **Incorporación:** no ejecutada.


---

## Quinta pasada — investigación externa, diferencial y reutilización

**Instrucción de Iván, 6 de octubre de 2026. Estado: contraste específico pendiente.** Esta quinta pasada se realiza después de las cuatro y queda dentro de esta misma VNext. No se crea otro expediente ni se incorporan propuestas a la fuente por esta anotación.

**Pregunta de este documento:** Comparar suficiencia, objetivos, carga y control con arquitecturas y estándares externos. Identificar ingredientes aprovechables y límites de los óptimos o garantías; no atribuir novedad a disponer de estados o un lifecycle.

Se fijarán trabajos primarios de FG-TIDA y de otras líneas relevantes, incluidos antecedentes y actualizaciones posteriores, con autor, versión, fecha y alcance realmente leído. Aquí se justificará qué coincide, qué diferencia podría sostenerse y qué pieza concreta conviene reutilizar, con sus condiciones de atribución, adaptación y compatibilidad.

El [mapa externo preparatorio](../../governance/review/EP_EXTERNAL_RESEARCH_REVIEW_2026-10-06.md) aporta fuentes iniciales; no completa esta pasada. El [plan 1.6](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#quinta-pasada--trabajos-externos-diferencial-y-reutilización) gobierna método y cierre. Las cuatro lecturas previas mantienen sus estados reales y se reabren si aparece evidencia que las afecte. Codex, mismo asistente de IA; anotación de alcance, sin independencia externa.


---

## Sexta pasada unificadora — preparación y continuidad

**Instrucción de Iván, 6 de octubre de 2026. Preparación registrada por Codex, mismo asistente de IA. Estado: pendiente de lanzamiento después de las cinco pasadas del corpus.** Esta anotación organiza el trabajo futuro; no declara una auditoría unificadora realizada ni cambia el estado de las lecturas anteriores.

**Pregunta de consolidación de este documento:** Conciliar Cartografía, Composition & Control y Operation con EA/RA: quien mantiene el mapa, quien califica, quien selecciona y quien ejecuta conservan funciones distintas.

Los hallazgos concretos se comentarán aquí y en las VNext de los documentos relacionados, conservando respuestas y desacuerdos. Se cotejarán las propuestas con la fuente actual y sus consumidores antes de presentar candidatos consolidados antes/después. La [sexta pasada del plan](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#sexta-pasada-unificadora-y-consolidación) fija el lanzamiento y el método. Se preservan fuente, historia y decisión de Iván para incorporar cambios.


---

## Organización autorizada del trabajo adicional — 6 octubre de 2026

**Lectura y registro realizados por Codex, mismo asistente de IA.** Iván pide explicar y enlazar el material fuera de la ruta principal y conservar los documentos sueltos, sin abrir nuevas auditorías de cada uno. Se mantienen las tres capas canónicas y se usan tres hojas auxiliares no canónicas: [EA y transversal](../../research/ecosystem-awareness/baseline/non-canonical/README.md), [RA](../../research/regime-awareness/ADDITIONAL_WORK_README.md) y [MSCA](ADDITIONAL_WORK_README.md). EA reutiliza su índice existente; RA y MSCA añaden hojas de trabajo, sin crear propietarios nuevos.

El [plan 1.10](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#trabajo-fuera-de-la-ruta-principal--lectura-adicional-sin-nuevas-auditorías) registra la instrucción más reciente. El inventario del corte 4ebb0c89722f1dc36adc11bec031c9d88b07737c tiene 1.306 archivos, 155 snapshots y 1.151 vivos: 800 alcanzables por enlaces de archivo y 351 sin esa ruta, incluidos 62 Markdown. Las fichas, partes y mirrors no se cuentan como 62 nuevas teorías. Los catálogos explican propósito, relaciones y límites y enlazan todos los archivos del corte; las listas exhaustivas quedan plegadas.

Los originales sueltos, canon, código, datos, freezes y binarios no reciben correcciones. Estar en el catálogo no altera autoridad. La lectura es de orientación y organización; no sustituye las cinco pasadas de una fuente vigente ni una dependencia material del argumento.

### Adición de navegación — texto viejo y después completo

**Fuente:** [índice propietario](README.md), blob `6e964aae2fb3e15d3980fd4004a364b892a95cbf`. **Instrucción de Iván:** enlazar trabajo adicional desde el último índice sin tocar los documentos sueltos. **Tipo:** solo navegación; no cambio de contenido técnico. La autorización del usuario cubre esta adición.

**Texto antes — viejo (último párrafo, literal):**

```markdown
**Claim status:** standards-oriented research and a posted focus-group input; no adopted ITU position, universal minimum, completed comparative validation or production certification.
```

**Texto después — adición al final, manteniendo el viejo:**

```markdown
**Claim status:** standards-oriented research and a posted focus-group input; no adopted ITU position, universal minimum, completed comparative validation or production certification.

---

## Additional work and complementary reading

The [additional-work reading catalogue](ADDITIONAL_WORK_README.md) explains preserved drafts, context, review notes, auxiliary evidence and related files. It is an optional, non-canonical reading leaf linked from this technical index; the original documents retain their location and status.

```

El cuerpo entero anterior permanece como prefijo exacto; no se sustituye el último párrafo al ejecutar esta adición. El después muestra el contexto viejo y el bloque nuevo para compararlos. La hoja es auxiliar, no otro nivel canónico.


---

## Prioridades del plan de cambios — revisión del corte

**Revisión realizada por Codex, 6 octubre de 2026, mismo asistente de IA.** Se revisan las auditorías y propuestas ya registradas para valorar impacto esperado, riesgo y esfuerzo. La fuente pública del corte es `7500dd5ee05c1a5052a28d35a8cefaf2c530707f`; los viejos y pares anteriores permanecen íntegros. Esta revisión no completa las pasadas pendientes ni la sexta.

El [plan 1.11](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#prioridad-de-cada-cambio--impacto-riesgo-y-esfuerzo) explica los criterios y el [listado completo](../../governance/review/change-priorities-2026-10-06/priorities.json) conserva las fuentes y los pares. La prioridad sirve para preparar tandas de decisión; la incorporación depende de Iván y de las comprobaciones indicadas.

| Cambio | Prioridad / tanda | Impacto esperado | Riesgo | Esfuerzo | Estado |
|---|---|---|---|---|---|
| 38 · Mostrar todo B_Cart en el índice MSCA | Primera · 2 — Coherencia entre RA, EA y MSCA | Alto | Medio | Medio | Pendiente de decisión |
| 39 · Acceso a trabajo adicional desde MSCA | Histórico · Histórico | Medio | Bajo | No nuevo | Ya publicado |

### Cambio 38 — Mostrar todo B_Cart en el índice MSCA

**Impacto esperado: Alto. Riesgo: Medio. Coste/esfuerzo: Medio. Prioridad: Primera.** Que la tabla no reduzca B a confianza numérica.

**Qué podría quedar desactualizado o afectado:** Otros resúmenes o consumers pueden continuar con confidence-only; el cambio debe referir 03 sin añadir campos obligatorios.

**Qué cuesta prepararlo:** Una celda y lectura cruzada de 03/04/EA/RA.

**Dependencias conocidas:** [00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md](../../research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) · [01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md](../../research/ecosystem-awareness/baseline/01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md) · [README.md](../../research/regime-awareness/README.md) · [03_MSCA_ECOSYSTEM_COMPOSITION_AND_CONTROL.md](03_MSCA_ECOSYSTEM_COMPOSITION_AND_CONTROL.md) · [04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md](04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md) · [01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md](../../research/ecosystem-awareness/baseline/01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md) · [01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md](../../research/ecosystem-awareness/baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md). La lista es el mapa conocido para preparar la decisión, no certificación de todos los consumidores.

**Estado y condición:** Pendiente de decisión. Conciliar contrato y consumidores. Coordinar con 35/37 y conservar el contrato existente.

**Viejo y nuevo:** el par literal sigue en [la entrada anterior](README_VNext.md#propuesta-antesdespués--expresar-todo-bcart); el viejo tiene una coincidencia en [la fuente actual](README.md), blob `0cbbec3e934e25cfcd4e0e79f92fb5d3ab491605`. Localizar el viejo no prueba compatibilidad de la propuesta ni autoriza incorporación.

### Cambio 39 — Acceso a trabajo adicional desde MSCA

**Impacto esperado: Medio. Riesgo: Bajo. Coste/esfuerzo: No nuevo. Prioridad: Histórico.** Distinguir notas de dominio, historia y especificación vigente.

**Qué podría quedar desactualizado o afectado:** Duplicar el bloque confunde lectura canónica y adicional.

**Qué cuesta prepararlo:** Publicado y verificado; no nueva incorporación.

**Dependencias conocidas:** [ADDITIONAL_WORK_README.md](ADDITIONAL_WORK_README.md). La lista es el mapa conocido para preparar la decisión, no certificación de todos los consumidores.

**Estado y condición:** Ya publicado. Fuera de tandas pendientes. No volver a ejecutar.

**Viejo y nuevo:** el par literal sigue en [la entrada anterior](README_VNext.md#adición-de-navegación--texto-viejo-y-después-completo); el viejo tiene una coincidencia en [la fuente actual](README.md), blob `0cbbec3e934e25cfcd4e0e79f92fb5d3ab491605`. El bloque añadido está presente; no se repite la ejecución.


---

## Continuación de 01C — payloads y separación de propietarios

**Auditoría cruzada realizada por Codex, 6 octubre de 2026; mismo asistente de IA.** Las fuentes Role y Composition conservan su texto; se abren sus únicas VNext y fichas externas para registrar esta relación principal. Role sigue siendo fuente estática/contractual y Operation distingue conducta efectiva. El candidato 53 corresponde a la frase de Composition sobre la entrada del slice RA y se prepara con 52 en 01C. Los enlaces de revisión nuevos son solo navegación.

La explicación, cobertura y viejos/nuevos están en [01C VNext](../../research/ecosystem-awareness/baseline/01C_VNext.md#lectura-de-los-payloads-y-sus-propietarios--continuación-sustantiva-de-01c), con el extremo productor en [Composition VNext](03_COMPOSITION_VNext.md) y [Role VNext](02_ROLE_VNext.md). Se preservan todas las conversaciones anteriores, decisiones y riesgos. No se declara ejecución o nueva validación independiente.

### Cambio 55 — adición de acceso a revisión de Role y Composition

**Solo navegación autorizada por el procedimiento. Impacto esperado: Medio. Riesgo: Bajo. Esfuerzo: Bajo.** Los originales Role/Composition permanecen intactos; el índice enlaza las fichas externas y no crea otro nivel canónico. El texto anterior entero es prefijo del índice ampliado.

**Texto antes — viejo completo del último párrafo:**

```markdown
The [additional-work reading catalogue](ADDITIONAL_WORK_README.md) explains preserved drafts, context, review notes, auxiliary evidence and related files. It is an optional, non-canonical reading leaf linked from this technical index; the original documents retain their location and status.
```

**Texto después — mismo contexto y adición al final:**

```markdown
The [additional-work reading catalogue](ADDITIONAL_WORK_README.md) explains preserved drafts, context, review notes, auxiliary evidence and related files. It is an optional, non-canonical reading leaf linked from this technical index; the original documents retain their location and status.

---

## Review workspaces for Role and Composition

The [Role review note](./02_ROLE_REVIEW_CARD.md) and [Composition review note](./03_COMPOSITION_REVIEW_CARD.md) lead to their separate audit workspaces. They record proposed clarifications at the RA boundary; both original specifications retain their current text and status.

```

El después muestra dónde se añade; no sustituye el párrafo viejo. Esta adición se publica con la entrega y se verifica por readback; queda fuera de tandas técnicas pendientes.


---

## Lectura completa de Role y Composition — reevaluación de la auditoría

**Auditoría/reevaluación realizada por Codex, 6 octubre de2026; mismo asistente de IA.** Role y Composition recibieron lecturas completas de lógica, edición y comprensión simulada, con contraste de fuentes/relaciones delimitado.52–54 se reevalúan a prioridad Siguiente, impacto/riesgo Medio; pares y ratings originales preservados.56 es solo título duplicado y necesita revisar el ancla.

[Role VNext](02_ROLE_VNext.md#pasadas-propias-de-role--lectura-completa-y-contraste-del-rol-estático) · [Composition VNext](03_COMPOSITION_VNext.md#pasadas-propias-de-composition--leer-el-mapa-completo-y-sus-límites) · [Fuentes/cobertura](../../governance/review/MSCA-role-composition-2026-10-06/evidence.json). La conversación anterior permanece visible; relectura del mismo agente no es independencia externa.
