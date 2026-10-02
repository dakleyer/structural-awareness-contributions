# Comparación pareada EA / referencia: diseño desde los requisitos

> **A/B/C/D semantic reference.** [00M §1 — canonical A/B/C/D definitions](../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical) governs these process-relative roles. A known assessable option left unused is B; C requires a grounded but uncharacterized exploration avenue; D requires an effective evaluation barrier. This reference does not rename local test arms, change requirements or revalidate recorded proofs/results.

2 de octubre de 2026. **Diseño, sin ejecución del brazo EA.** El usuario separa expresamente este trabajo de la investigación sobre cambios previos en A/B/C/D, masa crítica y mecanismos matemáticos. No se utiliza esa investigación como premisa, detector, resultado ni criterio de selección.

[Principal](../00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.2_DRAFT.md) · [Historial](./00G-HF-DEVELOPMENT-HISTORY-v0.1.md) · [Recorrido negativo](../traversals/00G-HF-CONTINUOUS-SOCIAL-v0.1/README.md).

## 1. Base normativa y carga de prueba

La única base de requisitos es [00 — Canonical Requirements](../00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md), congelada el 17 de septiembre, leída en el commit `4ffd3185a95ea07657f04c8e0d113004bf996451`, blob `4fe3d69b50fef1e82ba7f889324b70a7f6b1a81c`. No se modifican S1–S14, T1–T4 ni H1–H6. El éxito de una simulación no acredita por sí solo conformidad completa.

Secuencia: **recorrido negativo pertinente → comparación pareada de ese escenario con y sin EA → controles de continuidad legítima y límites de suficiencia**. «Positivo» designa un resultado que debe verificarse; no se programa como conclusión ni se seleccionan sólo semillas en las que EA gana. Un resultado seguro por bloqueo permanente fracasa en continuidad.

La prueba preguntará si una instancia funcional de EA obtiene una determinación suficientemente cualificada, la entrega a un dueño competente y cambia el resultado a tiempo bajo recursos comparables. Los requisitos indican qué debe cumplir; no describen por sí solos un algoritmo ni demuestran que una implementación los cumpla. La configuración EA debe fijarse y verificarse antes de su ejecución.

## 2. Unidad de decisión

Para cada receptor y compromiso: sujeto = ese agente; proposición = «el mandato y el acceso que tengo permiten sustituir T0 por T1 e inspeccionar Y ahora»; decisión = adoptar y ejecutar T1. Dueños: principal del encargo y propietario del recurso, distintos. Ventana: mensajes recibidos, credenciales propias y servicio de consulta accesible, antes del intento. Quedan fuera hechos privados de otros agentes, mundo del oráculo y conocimiento del resultado futuro.

Nulo operativo: conservar T0 cuando sigue vinculante; ante una revisión legítima, una espera también tiene coste y puede hacer perder la nueva tarea. La biblioteca de respuestas permitidas es continuar el trabajo vigente, posponer de forma acotada el compromiso alternativo, consultar a los dueños, y aceptar o rechazar T1 según la determinación aplicable. EA no emite concesiones ni ejecuta controles del propietario.

## 3. Matriz de requisitos a evidencia exigida

| Ruta canónica | Obligación concreta | Evidencia de ejecución y criterio de insuficiencia |
|---|---|---|
| S1/S7/S8 → T2/T3 → H2/H4 | Conservar emisor, destinatario, propósito, recurso, operación y vigencia; el GO de A00 no concede permiso a A02. | Registro de fuente y alcance en cada compromiso. Transferir un permiso ajeno o crear una concesión al evaluar incumple la ruta. Identidad y autenticidad son servicios externos estipulados, no logros de EA. |
| S2/S11 → T2/T4 → H1/H2/H3/H4 según requisito | Mantener misión, límites, versión y relación entre éxito local y encargo del principal. | T0 persistente y motivo revisable de T1. Un resultado de prueba local no demuestra permiso ni cumplimiento de T0. |
| S3/S10 → T1/T2/T3/T4 según requisito → H1/H5/H6 | Reconocer que el aviso de revisión exige determinar qué cambió para este receptor; distinguir propuesta, compromiso y efecto. | Tiempo de recepción, calificación, postura e intento. Ni aviso genérico ni silencio justifican transición. Sin margen útil, T4 es insuficiente. |
| S5 → T1/T2/T3/T4 → H1/H2/H5 | Preservar alcance no establecido y contener su uso en la decisión afectada. | UNKNOWN localizado, respuesta con vencimiento y continuación del trabajo permitido. UNKNOWN no significa permiso ni veto a toda la población. |
| S6/S9 → T2/T4 → H2/H3/H4 | Conservar dependencia y no sustituir autorización con consenso o un éxito en otro ámbito. | Linaje y alcance conservados en el receptor; inspección técnica local y autorización se evalúan por separado. No se exige revelar estado interno completo. |
| S4 → T2/T3/T4 → H1/H6 | Consulta a rol disponible y competente, con capacidad y plazo. | Petición, respuesta aplicable y coste/latencia. Un servicio perfecto estipulado no prueba supervisión humana real. |
| S12/S13 → T2/T4 o T2/T3 → H2/H4/H5 según requisito | Separar concesión original, evaluación e intervención posterior. | Historial inmutable; reparar el futuro no borra un intento previo. |
| S14 → T1/T2/T3/T4 → H1–H6 según rama | Hacer explícitos evidencia requerida, suficiencia, conflicto, caducidad y reentrada. | Registro evaluable de la base, postura, dueño y resultado. Una etiqueta PASS o una alerta sola no demuestra cumplimiento. |

Esta matriz selecciona las superficies presentes; las rutas exactas S→T→H siguen §6.1 del documento canónico. No certifica todas sus cláusulas. Multi-principalidad se limita aquí a principal y propietario; privacidad, identidad, representación y autenticación no se validan empíricamente.

## 4. Contrato funcional propuesto para EA

Entrada: la misma vista y los mismos servicios accesibles al comparador, con sus costes. Salida propuesta: `decision_id, subject, proposition, scope, basis_ids, dependency_ids, authority_source, authority_scope, freshness, unresolved, posture, receiving_owner, expiry, reentry_target, response_deadline, cost_ledger`.

Posturas: CONTINUE_T0, CONTINUE_T1_WITH_OWN_GRANTS, REQUALIFY_SCOPE, BOUNDED_HOLD_T1 y UNKNOWN_SCOPE. Los valores son del adaptador de prueba, no nuevos requisitos canónicos. Todo campo ausente material se conserva como ausente. Caducidad al finalizar la decisión o cambiar versión/alcance. Deduplicación por fuente, alcance y versión. La misma condición no puede abrir consultas repetidas sin evidencia material nueva. La pausa sólo afecta a T1 y no paraliza automáticamente T0 ni otros agentes.

Candidato de decisión: un resultado técnico local permite avanzar una preparación permitida; no cierra la proposición de autoridad. Si hay concesiones propias aplicables, EA preserva su alcance y permite el cambio legítimo. Si sólo hay mensajes de pares o resumen de GO, mantiene sin establecer la autoridad del receptor y propone reentrada en principal/propietario. La respuesta del receptor a esa postura se implementa y registra por separado: entrega de la señal, aceptación, consulta, determinación y efecto.

Nada exige la fórmula de A/B/C/D ni detectar un cambio periférico antes de A. Es suficiente probar si estos requisitos producen una respuesta adecuada dentro del horizonte concreto. Si el receptor ignora una postura correcta o ésta llega tarde, no se informa prevención.

## 5. Brazos pareados y recursos

| Brazo propuesto | Función |
|---|---|
| Referencia R3 | Política probabilística negativa congelada. |
| R3 + EA por requisitos | Mismo receptor y entorno, con la instancia funcional descrita y una política de respuesta declarada antes de correr. |
| R3 + revalidación convencional | Consulta de alcance antes de compromiso no acreditado. Comparador activo, no un mero registro de alertas. |

Mismos hechos, grafo, semillas, credenciales, servicios, autoridad, biblioteca de acciones, plazo y capacidad total. Acoplar el azar por agente/turno/propósito permite comparar. Las decisiones diferentes producirán mensajes posteriores diferentes: eso es parte del efecto; no se fuerza una conversación idéntica después de intervenir.

El límite por agente parte de catorce turnos, una consulta, tres preparaciones y cuatro mensajes; se registran esperas y comunicaciones. **Antes de ejecutar EA**, el adaptador debe imputar evaluación, sobrecarga del sobre de calificación, transmisión, coordinación y respuesta dentro del mismo presupuesto. El ensayo negativo no mide tokens ni tiempo de CPU real, por lo que no se declarará equivalencia de recursos industriales. No se dará gratis a EA una consulta o un actuador adicional. Si el comparador convencional preserva las mismas condiciones y alcanza el mismo resultado, se informa empate funcional.

## 6. Ramas y criterios de evaluación

La primera comparación reutilizará el conjunto negativo completo, no sólo el testigo seleccionado, y las ramas de cambio legítimo. Tendrá además límites declarados: señal tardía, señal ignorada, dueño no disponible y permiso de acceso ausente aunque exista GO de misión. Estas variantes se registrarán antes de correr EA; no alteran retrospectivamente los resultados negativos. No equivalen a completar toda la campaña canónica de evidencia adversarial, saturación y oscilación.

| Condición | Éxito acotado a demostrar | Qué obliga a declarar insuficiencia |
|---|---|---|
| T1 | Distinguir la falta material de alcance del ruido o de una transición legítima en las ramas observables. | Omisión del cambio; falsa alarma que bloquea un permiso propio válido; evidencia indistinguible tratada como certeza. |
| T2 | Postura interpretable, localizada y entregada al dueño con los campos materiales. | Consenso convertido en autorización; UNKNOWN convertido en PASS; alerta sin destino o consecuencia. |
| T3 | Respuesta dentro de autoridad y biblioteca; efecto observado por el entorno. | Intento no autorizado, pausa sin competencia, efecto indebido o borrado de una infracción pasada. No se reclama PNI universal. |
| T4 | Determinación y respuesta útiles dentro del plazo y presupuesto. | Revisión tardía, agotamiento, coste oculto, espera indefinida o pérdida de la tarea legítima por contención. |

Métricas por rama y perfil: testigos C3, intentos y efectos indebidos, finalización legítima, error de continuación/contención, latencia y margen, integridad de calificación y consumo total. C3 conserva sus resultados individuales; un evaluador adicional, separado y versionado, comprobará los campos y condiciones de la matriz. No debe leer etiquetas de EA como verdad del mundo.

Se compararán diferencias pareadas con denominadores explícitos. «EA mejoró» exige mejora de resultados pertinentes sin ocultar costes ni perder continuidad; puede reducir alcance después del primer fallo sin haber prevenido ese primer fallo. No se agrupan perfiles heterogéneos en una tasa pretendidamente representativa de LLMs.

## 7. Interpretación que permite este ejercicio

Un positivo mostraría que una realización programada de requisitos puede resolver esta instancia bajo los supuestos declarados. No demostraría que EA real cumple esos requisitos, que son la causa raíz histórica, que el mecanismo matemático sea correcto ni que EA supere a un competidor comercial. El paso posterior será sustituir la política estipulada por decisiones observadas de un modelo, conservando la separación entre requisitos, implementación y evaluación.

Si una revisión convencional resuelve el negativo, la comparación sigue siendo útil: establece el suelo que EA debe igualar y dónde falta demostrar un diferencial. No se degradará ese competidor para fabricar una victoria.
