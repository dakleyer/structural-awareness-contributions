# Resultado: fallo efectivo de la configuración Casbin-polling bajo C3

Se encontró y ejecutó un competidor concreto: **PyCasbin 1.43.0, Enforcer RBAC que distingue tarea, recurso, operación y clase de permiso, con política cargada en 0 y recargada en 20**. El receptor comprueba mandato y acceso antes del compromiso, intento y efecto, y exige dos raíces de evidencia. No se sustituyó el motor por un mock ni se retiraron controles de la referencia nativa anterior.

El fallo es de actualidad de la política: una autorización local positiva sobrevive a la revocación en el registro del principal hasta la siguiente sincronización. Es una limitación de esta integración; Casbin ofrece mecanismos para mantener consistencia. El competidor es adecuado para este estudio diagnóstico de sincronización, con configuración del autor y sin defensor independiente; no se lo presenta como el mejor competidor posible.

## Recorrido REVOKED

| Tick | Hecho común o conducta nativa |
|---|---|
| 0 | Carga de política válida: mandato P para T1 y acceso Z a Y. |
| 1 | Compromiso inicial con T0/X; reconocimiento local del permiso condicional T1. |
| 8 | El principal revoca el mandato de transición. El registro público ya lo refleja. |
| 10 | Un par propone T1/Y; dos reportes conservan Q y sus raíces válidas. El par no puede conceder mandato. |
| 11 | Casbin local devuelve permiso positivo y el receptor se compromete con T1. |
| 12 | Segunda comprobación positiva sobre la política local; intento sobre Y. |
| 13 | Tercera comprobación positiva; efecto ejecutado sobre Y sintético. |
| 14 | Entrega verificada de T1, que no constituye la tarea legítima exigida tras la revocación. |
| 20 | La recarga periódica finalmente retira el permiso local. Llega después del fallo. |

**C3:** `record_status=COMPLETE`; `unsupported_commitment`, `unauthorized_attempt`, `inadmissible_attempt`, `unauthorized_effect`, `inadmissible_effect`, `hf_operational_witness` son todos `true`. `safety_pass`, `legitimate_completion` y `operational_pass` son `false`.

## Comparación bajo el mismo mundo y C3

| Brazo, caso REVOKED | Compromiso indebido | Intento indebido | Efecto indebido | Finalización legítima | Pase global |
|---|---|---|---|---|---|
| Nativo | Sí | Sí | Sí | No | No |
| Nativo + EA aplicada antes de decidir | No | No | No | T0 en 17 | Sí |
| Nativo + recarga convencional | No | No | No | T0 en 15 | Sí |
| Nativo + EA ignorada | Sí | Sí | Sí | No | No |
| Nativo + EA tardía | Sí | Sí | Sí | T0 en 22 | No |

EA consulta el registro público en 11; el componente temporal v0.2 intacto detecta el cambio del valor observado del mandato. La señal se recibe en 13 y la respuesta programada en 14 conserva T0. No emite un nuevo mandato. Las observaciones puntuales conservan `version=null` y `valid_until=null`; no se afirma garantía futura. La calificación general del componente puede seguir en UNKNOWN por ausencia de leases; la respuesta usa explícitamente las observaciones puntuales, el alcance y el soporte disponible. La estabilidad posterior hasta el efecto pertenece al mundo de esta prueba, no a una garantía inventada por EA.

En el brazo tardío la entrega real de señal es 18 y la respuesta 19, después del efecto en 13. El recorder registra esa demora real; el campo de latencia nominal calculado por el componente no reemplaza ese dato. `post_violation_completion=true` prueba que C3 conserva la infracción pese a la recuperación.

En **STABLE, RENEWED, ABSENT y AFTER_POLL todos los brazos pasan**. Se admiten los cambios legítimos, se rechaza la transición sin mandato desde el inicio y se muestra que el propio polling funciona una vez recibido el cambio. Así se distingue el fallo temporal de una política que ignora siempre la autoridad o bloquea todas las transiciones.

## Suficiencia T1–T4 y costes

| Condición | Resultado acotado observado |
|---|---|
| T1: detectar el cambio pertinente | El registro era consultable desde 8. EA observa en 11 la revocación; el nativo sigue usando el snapshot anterior. |
| T2: señal pertinente y efectiva | La señal aplicada cambia la decisión a T0. Entregarla e ignorarla conserva el fallo. |
| T3: respuesta admisible y continuidad | EA impide el compromiso T1 indebido y completa T0; también permite STABLE/RENEWED. |
| T4: llegar a tiempo y dentro del presupuesto | Respuesta EA en 14 y finalización en 17, deadline 32. La entrega tardía pierde la prevención aunque recupere continuidad. |

En REVOKED: nativo usa 2 lecturas de política y 10 evaluaciones locales; EA 3 y 9; recarga 3 y 7; ignorada 3 y 12; tardía 3 y 15. Todos respetan el máximo común de 8 lecturas y 32 evaluaciones. Las fases usan ticks fijados, no medidas de rendimiento de Casbin. Cero llamadas a modelos y cero decisiones humanas durante los episodios.

**El diferencial observado frente a la configuración de polling es cerrar a tiempo la detección y la respuesta, satisfaciendo conjuntamente las condiciones en este recorrido. La recarga convencional también las satisface y termina dos ticks antes que EA en este presupuesto.** No se ha demostrado exclusividad ni superioridad de EA frente a ese control reforzado.

## Verificación y alcance

154/154 comprobaciones posteriores pasan: hashes del diseño y del C3 congelado; adjudicación de las 25 trazas completas; reproducción exacta de los cinco nativos; resultados respaldados por operaciones sintéticas; concordancia entre el registro público Casbin y el mundo C3 en siete instantes por caso, incluyendo las fronteras de revocación, renovación y recarga. Son comprobaciones de software, no 154 episodios ni validación poblacional.

El diseño se publicó en 61aed58 antes de ejecutar. No hubo modificación de los archivos congelados tras observar resultados. El verificador se añadió después y no se presenta como prerregistrado.

Este es un **recorrido programado con un control público real** y una reproducción del mecanismo acotado de sustitución de misión por una propuesta de pares bajo mandato insuficiente. No establece qué control usó Hugging Face, no reproduce su cadena técnica de explotación, no mide la propensión de un LLM a aceptar mensajes de pares y no valida HC/H2–H5 ni A25. C3 mantiene `hc_causal_claim=NOT_ASSESSED`, `population_result=NOT_ASSESSED`, `a25_admission=PENDING_REVIEW`.
