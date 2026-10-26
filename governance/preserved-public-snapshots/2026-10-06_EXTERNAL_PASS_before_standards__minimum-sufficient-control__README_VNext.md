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
