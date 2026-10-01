# Fichas de ejecución temporal y colectiva

**C2 / 1 de octubre de 2026.** Especificaciones para preregistrar ensayos, no resultados ni requisitos de implementación impuestos a EA. [Oráculo](./README.md) · [protocolo principal](../../00G_HF_CAUSAL_NEGATIVE_TRAVERSAL_PROTOCOL_v0.3_DRAFT.md).

## 1. Perfil temporal antes de afirmar eficacia a tiempo real

Completar y congelar antes de ejecutar; conservar versión, hash y evidencia de fecha del registro. El campo `registration_ref` es un enlace al expediente, no una prueba automática de preregistro.

| Campo | Contenido que debe quedar fijado |
|---|---|
| Contrato y episodio | Mundo, tarea exigida, positivos emparejados, configuración del receptor y límites materiales. |
| Evento objetivo | Compromiso, intento o efecto. Si se miden los tres, producir tres evaluaciones suplementarias etiquetadas de la misma traza; no promediar sus resultados. |
| Reloj y correspondencia | Unidad, origen, reloj monotónico, sincronización, deriva, error combinado máximo y conversión verificable a tiempos de la traza. No atribuir segundos a ticks por conveniencia posterior. |
| Límite de respuesta | Último instante inclusivo para una respuesta efectiva, acción concreta que cuenta como respuesta y fundamento mecánico del límite. Descontar latencia del actuador si la marca es una orden y no el efecto de la respuesta. |
| Observabilidad | Primer cambio material, primera evidencia disponible, recepción en cada componente; separar evento privado del evaluador de evidencia accesible al candidato. |
| Canal | Pérdidas, colas, reintentos, saturación, tiempos observación/emisión/entrega/respuesta. Registrar fases ausentes. |
| Propagación | Receptores elegibles, grafo y calendario o distribución de primeras exposiciones, ráfagas y semillas; rangos de tasas preregistrados. Exposición, aceptación del encargo e intento son eventos distintos. |
| Presupuesto común | Cómputo, herramientas, consultas, ancho de banda, tiempo y esfuerzo humano por brazo. Comparadores convencionales con acceso equivalente a la información y transporte que realmente les corresponda en la comparación. |
| Resultados | Seguridad y continuidad del núcleo; margen de respuesta; latencias por fase; demora de tareas legítimas; lagunas de captura. |
| Estimación | Repeticiones, semillas, incertidumbre, exclusiones, umbrales y regla de parada fijados antes; conservar negativos y positivos. |

Los cambios no observables se analizan por separado. No se exige detectar un hecho privado antes de que exista evidencia accesible. Esto no borra la infracción material del oráculo: separa resultado de detectabilidad y atribución causal. Si el mecanismo ya evita el problema sin señal, conservar ese resultado como control positivo.

Para alegar prevención temporal se necesita el resultado material y un contraste adecuado, además de la latencia. `response_within_registered_budget` solo evalúa la posición temporal de una respuesta registrada contra un límite; no verifica el contenido semántico de esa respuesta. Un fallo por señal tardía y uno por respuesta ineficaz puntual deben quedar distinguibles.

## 2. Estudio colectivo pendiente

**La v0.3 no implementa ni ha ejecutado este estudio.** Su campo `population_result` siempre permanece `NOT_ASSESSED`. La ficha impide extrapolar un receptor al conjunto y prepara el diseño con Nelson, Ward o los participantes pertinentes sin presuponer su colaboración o aprobación.

| Decisión previa | Especificación requerida |
|---|---|
| Población | Número de agentes, tareas, obligaciones individuales y colectivas, entradas/salidas y horizonte. Distinguir receptores observados, expuestos y elegibles. |
| Relaciones | Grafo de comunicación, autoridad, dependencias y recursos; coordinadores, intermediarios y servicios compartidos. |
| Cobertura EA | Fracción y ubicación exacta de agentes/componentes con EA; asignación aleatoria o dirigida y justificación. Registrar quién recibe señales indirectas. |
| Brazos | Nativo, control convencional, EA con transporte/receptor, composiciones adicionales solo si se prueban. Conservar presupuesto e información comparables según la pregunta registrada. |
| Dinámica | Calendario de exposición, adopción, cesión/revocación, incorporación de participantes y caducidad del contexto; mismos escenarios base entre brazos. |
| Interferencia | Un agente tratado puede cambiar el comportamiento de uno no tratado. Unidad de asignación e inferencia compatible: por ejemplo, ecosistemas replicados o grupos realmente separados; no asumir receptores independientes. |
| Seguridad | Agentes con compromiso/intent/efecto indebido, tiempo al primer fallo, propagación de encargos y gravedad del efecto sobre recursos compartidos. Denominadores explícitos y recuentos únicos. |
| Continuidad | Tareas legítimas completadas y su plazo, transiciones genuinas admitidas, falsos bloqueos, carga y coste. Un enjambre paralizado no pasa por ser seguro. |
| Agregación | Umbrales materiales preregistrados; qué infracción local determina fallo colectivo y qué tolerancias, si alguna, son justificables. No promediar para ocultar un efecto grave. |
| Captura | Identidades, enlaces de mensajes/eventos y permisos, cobertura por agente y canal; manejo de pérdida/censura. |
| Incertidumbre | Semillas, repeticiones de ecosistemas, heterogeneidad, sensibilidad a topología y cobertura; reglas de exclusión y parada. |

La pregunta «¿basta con 10 % de cobertura?» se convierte en «¿qué resultado se obtiene con este 10 %, situado aquí, con estas rutas de señal y dependencias, frente a estos controles?». No hay una respuesta derivable del porcentaje por sí solo. El denominador histórico 700/1.200 no se usa como parámetro de esta prueba sin una justificación externa específica.

EA puede consumir un análisis poblacional ajeno, emitir señal contextual o funcionar con controles internos del receptor; cuál composición basta es una pregunta experimental. La ficha no impone control poblacional, autoridad delegada adicional o escalado humano para pasar. Tampoco convierte el porcentaje de agentes equipados con EA en una medida de superioridad del indicador.

## 3. Puertas proporcionadas a la afirmación

| Afirmación prevista | Evidencia requerida |
|---|---|
| El evaluador distingue estas trazas construidas | Controles positivos/negativos/indeterminados reproducibles. Es el alcance actual. |
| El receptor pasa esta instancia | E1 con adaptador, vistas y comprobador de finalización; etiquetar exploratorio mientras falten puertas confirmatorias. |
| EA aporta frente al comparador | Brazos comparables, métricas y recursos registrados, incertidumbre y controles de continuidad. |
| La respuesta llega a tiempo en el entorno | Perfil temporal, medición completa de extremo a extremo, resultado material y contraste pertinente. |
| Mejora el resultado colectivo | Estudio colectivo con interacciones y asignación explícitas; no basta multiplicar éxitos individuales. |
| El mecanismo causal o H2–H5 queda apoyado | Contrastes causales y trazabilidad específicos; no deducirlos del pase del evaluador. |

No se alteran los pasos E1–E5 del protocolo. Cualquier cambio de adjudicación después de observar resultados requiere una versión nueva y repetición/comparación transparente; no se corrige retroactivamente el registro previo.
