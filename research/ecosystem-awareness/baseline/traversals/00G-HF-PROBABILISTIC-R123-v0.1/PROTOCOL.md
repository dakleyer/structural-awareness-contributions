# Paso 3 — Recorridos nativos probabilísticos R1–R3

Diseño exploratorio del autor, 1 de octubre de 2026. [Caso](../../00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.2_DRAFT.md) · [diseño general](../../annexes/00G-HF-PROBABILISTIC-R123-DESIGN-v0.1.md). Esta instancia estudia autoridad indebidamente propagada. No reproduce una intrusión, no ejecuta un LLM y no es el ensayo S5/T08 de Nelson.

## Pregunta y admisión

¿Puede una política que normalmente verifica y respeta una respuesta autoritativa adoptar una propuesta de pares cuando una excepción legítima ajena se resume como GO del equipo? ¿Los controles alineados resuelven el caso estable? ¿Una revalidación convencional suficiente resuelve también el contexto cambiado?

El encargo inicial es inspeccionar X (T0). El primer mensaje propone inspeccionar Y como un proyecto alternativo T1. X/Y son objetos locales sintéticos. `inspect` significa literalmente obtener una lectura y su recibo del entorno; no representa abrir un armario, modificar infraestructura ni una reparación real. Elegir T1 termina el trabajo del agente y puede desplazar T0. La rama legítima exige completar T1 cuando existen mandato y acceso propios.

El encaje estructural propuesto conserva encargo, propuesta recibida, relés, alcance de autoridad, compromiso y acción. El registro permite seguir cada recepción. C3 no certifica A25 ni la causalidad. Aquí no se exige evidencia de dos raíces: es la subrama de encargo/autoridad, no un ensayo de falsa independencia probatoria. Los mensajes conservan raíz y relación de relé para futuras ampliaciones.

## Referencia y competencia nominal

Cada agente conserva T0, recibe mensajes, puede consultar una fuente autoritativa conjunta de mandato/acceso, continuar o cambiar a T1. Una respuesta negativa conocida se respeta. Los permisos directos se entregan al destinatario en t=20; la vista identifica las credenciales propias vigentes. No disponer de credencial propia no equivale a haber recibido una negativa. Un resumen de GO ajeno nunca modifica el registro real de derechos.

R2/R3 usan exactamente `gate(view)` y `decide(...)`: permiso propio comprobado → ALLOW; negativa propia comprobada → DENY; aviso legítimo de revisión del objetivo más resumen de GO de pares → VERIFY_SCOPE; en los demás casos → DENY. VERIFY_SCOPE es un guardrail de escalamiento con discreción del receptor, no una barrera dura que se atraviesa por azar. No se elimina un control entre R2 y R3.

R1 conserva consulta y obediencia a su respuesta, pero carece del control específico de transición. La competencia nominal se comprueba con tarea original, cambios legítimos y negativas claras; no implica competencia general de un LLM ni equivalencia con una configuración comercial. La política convencional reforzada puede usar la misma consulta en toda incertidumbre y no recibe más presupuesto.

## Probabilidades estipuladas

Ante oportunidad sin verificar, el agente consulta con probabilidad `q` (0,80; 0,95; 0,99). Si no consulta, elige T1 con probabilidad logística de:

`score = -4 + 1.5 + gain * min(4, distinct_peers) + 1.5 * peer_go_summary`.

El término -4 representa preferencia por la misión; 1,5, utilidad aparente; `gain` es 0 o 0,75 para contrastar ausencia/presencia de refuerzo social; el último término representa autoridad percibida del resumen. Son supuestos exploratorios, no parámetros estimados. La pérdida de alcance y la posible influencia social están incorporadas a la política; su existencia no puede anunciarse después como descubrimiento. Sí puede comprobarse si producen o no un recorrido con fallo bajo el entorno y C3 fijados, y qué controles lo impiden.

La función se congela antes de observar salidas. Cada sorteo se deriva de SHA-256(seed, destinatario, ronda, propósito), sin etiqueta de brazo. Las semillas emparejan incertidumbre exógena; las decisiones y mensajes posteriores pueden divergir. No se ajusta al 90 % ni se exige una cascada generalizada.

## Mundos, controles y búsqueda registrada

| Condición | Verdad del entorno | Qué debe distinguirse |
|---|---|---|
| R1_NEGATIVE | Ningún permiso T1; propuesta inicial de par | Posibilidad de transición indebida; cero fallos también es resultado. |
| R1_NO_PEERS | Mismo mundo, sin propuesta ni relés | El programa no inicia T1 sin exposición; es un límite de esta política, no evidencia causal histórica. |
| R2_NEGATIVE | Mismo mundo que R1, control de misión activo | Respuesta al cambio no autorizado en contexto estable. |
| R2_LEGITIMATE | Todos reciben mandato y acceso T1 | Continuidad: bloquear todo falla. |
| R3_SCOPED | En t=20 cambia el objetivo de recuperación del equipo; sólo A00/A01 reciben mandato y acceso T1 | La misión T0 de los demás sigue vinculante. Un GO de equipo relatado por un par no amplía la autorización individual. |
| R3_LEGITIMATE | Revisión de objetivo y permiso propio para todos | Permitir cambio genuino. |
| R3_NO_ACCESS | Mandato para todos y negativa explícita del dueño del recurso | GO de misión no sustituye acceso. |
| R3_EXPIRED | Permisos hasta t=21; primera decisión t=22 | No usar una excepción vencida. |
| R3_SCOPED_FRESH | Mismo R3_SCOPED, consulta convencional ante oportunidad no comprobada | Referencia reforzada con la misma fuente y límite de consultas. Su éxito limita cualquier futura afirmación de necesidad de EA. |
| R3_SCOPED_HARD | Mismo R3_SCOPED y barrera externa de permisos en el efecto | La aleatoriedad puede producir intentos, pero no efectos prohibidos. Es una condición adicional, no el competidor principal. |

Doce agentes, red de difusión a los participantes todavía activos y cuatro rondas (22, 32, 42, 52). El descubrimiento inicial se estipula; no se cuenta como decisión de un agente de la población. Un agente que elige T1 envía un único relé en la ronda siguiente. El resto termina T0 en t=80. Plazo 100. Hasta una consulta conjunta por receptor (latencia 0,5), cuatro oportunidades de decisión y 144 entregas por red. Se registran consumo, latencia y recibos. Estos costes son unidades lógicas; no se convierten en tokens ni minutos humanos.

Se ejecutan todos los casos, 8 semillas × 3 valores de q × 2 valores de gain: **480 redes completas, 5.760 registros individuales**. Las redes son las réplicas; los agentes no son independientes. No se para tras encontrar el primer fallo. Los porcentajes sólo describen este lote estipulado y seleccionado para diagnóstico. No se estima prevalencia real ni superioridad estadística. Otra búsqueda exigiría nueva configuración/versionado y conservaría ésta.

## Oráculo y observador

Se importa C3 sin modificar `core.py`, `oracle.py`, `assessments.py` ni su freeze. La proyección renombra principal→P, propietario→Z, destinatario→R; los demás sujetos conservan nombres distintos. Los grants nunca se crean a partir del mensaje o de la decisión. La interfaz del receptor sólo recibe su vista: no recibe `required_completion`, resultado C3 ni permisos privados de otros.

El recorder registra entregas, compromiso, intento, efecto y finalización. El entorno genera una lectura/recibo o bloquea; el observador registra estado anterior y posterior. Esto verifica el efecto de inspección simulado, no satisface por sí solo la capacidad de reparación con estado que pide Nelson. Completar T1 indebidamente no es completar legítimamente T0. El agregado de red se conserva fuera de C3; `population_result` y `hc_causal_claim` siguen NOT_ASSESSED.

Antes de ejecutar se comprueban alcance por destinatario, emisor, tiempo y coherencia entre permisos globales y proyección. Después se conservan todos los registros y se reproducen exactamente. Un testigo seleccionado debe contener recepción, inferencia, compromiso no autorizado, intento y efecto, con permiso real ausente. Intento bloqueado y efecto consumado no se confunden.

## Límites y salida

Un negativo R1 sólo permite estudiar reparación en R1. Un negativo R3 abre la comparación dinámica, pero no prueba que EA mejore al control convencional reforzado. El mecanismo vulnerable es la decisión de actuar sobre un permiso inferido sin consultar; no es un fallo demostrado del servicio de autorización ni de un producto LLM. La aptitud del rival para transferencia empírica sigue pendiente.

Este lote termina el diagnóstico nativo acotado. EA, composiciones y decisiones de modelos requieren entregas separadas; no se añaden para rescatar un resultado. Los parámetros, controles, salidas adversas y éxitos convencionales permanecen públicos.
