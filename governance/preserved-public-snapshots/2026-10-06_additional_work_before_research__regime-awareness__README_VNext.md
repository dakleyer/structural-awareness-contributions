# Revisión del README de Regime Awareness

**Única VNext de este README.** Auditoría realizada por Codex, 6 de octubre de 2026, mismo asistente de IA. [Fuente](./README.md) · [plan](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md). Las propuestas se preparan para que una persona pueda decidirlas; no se aplican a la fuente.

## Instrucción de Iván y cobertura

Iván confirmó todo Contributions dentro del alcance, también las integraciones EA/MSCA/RA. No se limita la revisión a una ruta o a archivos directamente enlazados.

Se leyó el README completo, blob `ce121ac539da72eb62ce1191b2bd24c5bdeebf70` en `e80846a0f9cf3b97cf222ed3d1e28b31d145ad3e`. Se cotejaron los pasajes de 01C sobre el delta y de MSCA Composition/Operation sobre sus entradas y retornos. Se leyó completo 01D. Las fuentes externas del detector, el contexto de programa y todos los consumidores no están revisados íntegramente: **pasada de evidencia e integración global abiertas**.

## Primera pasada — fondo y lógica

**Auditoría realizada por Codex:** la página distingue una pregunta de régimen observable de la decisión operacional del participante. No atribuye a un resultado neutral conocimiento del estado oculto; tampoco exige reconstruirlo todo.

El reparto persistencia/indicación/acción es claro: Composition & Control mantiene la Cartografía, RA devuelve un delta y solicitudes, MSCA Operation selecciona una postura y el dueño autorizado ejecuta. Es una división defendible del argumento, no evidencia de ejecución conjunta.

La descripción de los cuatro roles contiene una tensión concreta. La nota inicial remite a 00M, pero “Current architectural output” describe B_RA como confianza/intensidad, C_RA como frontera de capacidad y D_RA como unknown residual. Eso puede estrechar B a un número, confundir exploración C con reserva evaluable B, o tomar clasificación desconocida por D.

## Segunda pasada — fuentes y consumidores

**Auditoría realizada por Codex:** comparación textual en ambos extremos de la relación.

[01C v0.2, §2](../ecosystem-awareness/baseline/01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md#2-source-defined-ra-operating-chain-and-limits) define B_RA como fundamento establecido y reserva caracterizada; confianza expresa soporte y no magnitud física de cambio ni todo B. C exige vías fundadas aún no caracterizadas y D una barrera efectiva; clasificación incierta permanece UNKNOWN. Esta precisión es más amplia que el resumen del README.

[MSCA Composition & Control](../../standards/minimum-sufficient-control/03_MSCA_ECOSYSTEM_COMPOSITION_AND_CONTROL.md) consume el delta y conserva la actualización de Cart_i. [MSCA Operation](../../standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md) recibe Δ_RA, pero su tabla mantiene “direction/intensity/capability/residual”. La discrepancia del resumen aparece, por tanto, también en un consumidor. Su [VNext](../../standards/minimum-sufficient-control/04_OPERATION_VNext.md) registra el contraste; no se presupone que una implementación haya heredado esa lectura.

[01D](../ecosystem-awareness/baseline/01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md) preserva una regla adicional: RA puede ser opcional para una acción independiente, pero entra en el conjunto requerido si esa acción depende de su evidencia. UNKNOWN no se convierte en neutral ni SUPPORTED en permiso. Cambios de una condición invalidan sus dependientes, no todo el sistema por defecto.

El conjunto ya tiene enlaces en ambos sentidos. Falta verificar en cada perfil/implementación que el receptor preserve ese significado, el mismo scope y la vigencia. La coincidencia de nombres no prueba compatibilidad.

## Tercera pasada — forma y edición

**Auditoría realizada por Codex:** recorrido completo de títulos, listas y tabla producer/consumer.

La página es más manejable que otros índices. Introducción, tres rutas, salida arquitectural e interfaces siguen un orden legible. La tabla de inputs/outputs ayuda a ubicar quién es responsable. Repetir el circuito en prosa y tabla sirve si no cambia el significado entre ambas.

La fila de salida de la tabla conserva “qualified directional change” y no vuelve a equiparar delta con gradiente; el problema está en la lista de componentes del párrafo anterior. Se propone una sustitución precisa de esa lista, sin renombrar fields o rutas.

Los enlaces al contexto y al paper no son otros niveles ilimitados de README: el índice EWS cumple una función técnica local. La organización se mantiene dentro de los tres niveles acordados.

## Cuarta pasada — lectura humana

**Auditoría realizada por Codex:** relectura simulada, sin lector humano independiente.

Una persona puede entender que RA examina si el fundamento de una inferencia sigue siendo aplicable. Le costará más saber si “intensidad” significa tamaño del cambio o confianza en lo observado. Esa diferencia importa incluso antes de leer fórmulas.

El ejemplo de una medición útil que quedó sin hacer aclara B: sigue siendo una evaluación caracterizada, no una frontera C. No hace falta inventar una nueva etiqueta ni modificar el wire contract para explicar esto.

“Delta” y “gradiente” se distinguen razonablemente: el primero informa el cambio observado, el segundo depende de los objetivos del receptor. También debe mantenerse que un delta no elige permiso o contención.

## Conversación y protección de la integración

**Codex, auto-revisión:** el resumen necesita reconciliación editorial con la fuente actual. No se concede a esta auditoría permiso para redefinir el resultado del detector o los estados del consumidor. [01C VNext](../ecosystem-awareness/baseline/01C_VNext.md), [MSCA README VNext](../../standards/minimum-sufficient-control/README_VNext.md), [EA README VNext](../ecosystem-awareness/README_VNext.md) y [EP README VNext](../../architectural-contributions/ecosystem-positioning/README_VNext.md) reciben la relación.

Antes de incorporar el cambio se revisarán implementaciones/perfiles que utilicen la interpretación anterior y se conservará su historia. La identidad Δ_RA y A_RA/B_RA/C_RA/D_RA permanece en el candidato, pero conservar nombres no basta para demostrar preservación de comportamiento. No se ejecutó ninguna prueba nueva.

## Propuesta antes/después — conciliación del resumen, pendiente

**Localización:** lista “Current architectural output”, segundo elemento, una coincidencia. **Fuente:** blob arriba. **Instrucción:** revisión total segura de Iván. **Tipo:** cambio semántico de explicación; no se clasifica como inocuo solo por conservar campos.

**Texto antes:**

```markdown
- The broader Regime Awareness architecture may project that result as the qualified delta **Δ_RA=[A_RA,B_RA,C_RA,D_RA]**: direction (A_RA), confidence/intensity attached to that direction (B_RA), recognized current-capability frontier (C_RA), and structural/residual unknown (D_RA). Scope, Ψ/context/baseline, provenance and freshness qualify the delta but are not themselves the direction.
```

**Texto después:**

```markdown
- The broader Regime Awareness architecture may project that result as the qualified delta **Δ_RA=[A_RA,B_RA,C_RA,D_RA]**: qualified direction (A_RA), established support, validity limits and characterized assessment reserve (B_RA), grounded exploration avenues not yet characterized (C_RA), and potentially material effects beyond effective evaluation under the declared frame (D_RA). Confidence qualifies evidential support; it is not the physical magnitude of change or all of B_RA. Uncertain role classification remains UNKNOWN. Scope, Ψ/context/baseline, provenance and freshness qualify the delta but are not themselves the direction.
```

**Razón:** conciliar el resumen con 01C y 00M sin cambiar nombres de payload. **Dependencias:** 01C, MSCA 03/04, perfiles de signalling y consumidores RA; VNext de sus README. **Compatibilidad:** pendiente, revisar declaraciones históricas y significado recibido. **Decisión de Iván:** pendiente. **Incorporación:** no ejecutada.


---

## Quinta pasada — investigación externa, diferencial y reutilización

**Instrucción de Iván, 6 de octubre de 2026. Estado: contraste específico pendiente.** Esta quinta pasada se realiza después de las cuatro y queda dentro de esta misma VNext. No se crea otro expediente ni se incorporan propuestas a la fuente por esta anotación.

**Pregunta de este documento:** Ampliar la literatura de detección, contextualización y cambios de fundamento, con atención a desarrollos posteriores y sus supuestos. Identificar qué puede alimentar la rama RA y qué requeriría otras evidencias o fuentes.

Se fijarán trabajos primarios de FG-TIDA y de otras líneas relevantes, incluidos antecedentes y actualizaciones posteriores, con autor, versión, fecha y alcance realmente leído. Aquí se justificará qué coincide, qué diferencia podría sostenerse y qué pieza concreta conviene reutilizar, con sus condiciones de atribución, adaptación y compatibilidad.

El [mapa externo preparatorio](../../governance/review/EP_EXTERNAL_RESEARCH_REVIEW_2026-10-06.md) aporta fuentes iniciales; no completa esta pasada. El [plan 1.6](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#quinta-pasada--trabajos-externos-diferencial-y-reutilización) gobierna método y cierre. Las cuatro lecturas previas mantienen sus estados reales y se reabren si aparece evidencia que las afecte. Codex, mismo asistente de IA; anotación de alcance, sin independencia externa.


---

## Sexta pasada unificadora — preparación y continuidad

**Instrucción de Iván, 6 de octubre de 2026. Preparación registrada por Codex, mismo asistente de IA. Estado: pendiente de lanzamiento después de las cinco pasadas del corpus.** Esta anotación organiza el trabajo futuro; no declara una auditoría unificadora realizada ni cambia el estado de las lecturas anteriores.

**Pregunta de consolidación de este documento:** Conciliar el resumen del delta con 01C, 00M y los consumidores MSCA: soporte, reserva evaluable, exploración y barrera efectiva deben seguir distinguiéndose; UNKNOWN no pasa a ser D ni permiso.

Los hallazgos concretos se comentarán aquí y en las VNext de los documentos relacionados, conservando respuestas y desacuerdos. Se cotejarán las propuestas con la fuente actual y sus consumidores antes de presentar candidatos consolidados antes/después. La [sexta pasada del plan](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#sexta-pasada-unificadora-y-consolidación) fija el lanzamiento y el método. Se preservan fuente, historia y decisión de Iván para incorporar cambios.
