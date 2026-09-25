# 00L-00E — Traza de papel emparejada: síntesis bajo capacidad finita

**Base:** 00E v0.1, 00E-A01 v0.2 y 00E-A02 v0.2. **Estado:** traza calculada en papel sobre hechos sintéticos; no ejecución de Agent 365, LangGraph/LangSmith ni EA.

## Ficha congelada

La decisión es producir una síntesis útil para cuatro departamentos dentro de un presupuesto fijo de tokens. En el estado inicial las fuentes son suficientes y relativamente independientes. En el cambio H2 la evidencia útil cae y dos fuentes pasan a depender de una misma cadena; el presupuesto y el objetivo no cambian.

## Recorrido H0/H1/H2 y ruta positiva

| Paso | H0 — síntesis ordinaria | H1 — implementación reforzada | H2 — mismo H1 bajo cambio de régimen | Ruta positiva EA/diseño |
|---|---|---|---|---|
| Entrada | documentos, consultas y respuestas disponibles; se prioriza la respuesta final | conserva trazas, fuente, dependencia, coste y destinatario | mismas entradas formales, pero evidencia independiente y horizonte útil disminuyen | recibe evidencia, dependencia, capacidad y residual separados |
| Regla | `best_answer → compress → deliver` | incluir procedencia, alternativas, incertidumbre y presupuesto en la evaluación | la regla H1 debe detectar caída de independencia/valor antes de cerrar | S1/S3/S10/S14: calificar suficiencia y preservar residual |
| Cálculo | una respuesta plausible ocupa el presupuesto; residuo puede desaparecer | `useful_evidence ∧ budget_ok → QUALIFIED`; si no, `REQUALIFY` | `independence=0` o `useful_horizon<deadline` → `NO_COMMITMENT/REQUALIFY` | dividir presupuesto entre evidencia decisiva, verificación y explicación mínima |
| Decisión | posible `PASS` por fluidez aunque no cubra los cuatro usos | conservar fuentes y hacer visible la celda no decidible | no cerrar como PASS; identificar qué información falta y quién puede obtenerla | `QUALIFIED SYNTHESIS` solo si S/T/H/KPI completos; si no, `PASS WITH EXPLICIT LIMIT` |
| Oráculo | falla si pierde un hecho material sin marcarlo | pasa si preserva el hecho material y el residual dentro del presupuesto | falla si continúa con la síntesis antigua como si el régimen no hubiera cambiado | la conclusión se refuta si H1 convencional obtiene igual resultado con igual/menor carga |

## Controles emparejados

| Rama | Hecho | Salida calculada | Condición de refutación |
|---|---|---|---|
| Continuidad | mismas fuentes, dependencia y capacidad | sintetizar y entregar dentro del presupuesto | HOLD o búsqueda ilimitada |
| Cambio autorizado | nueva fuente independiente, objetivo actualizado y presupuesto confirmado | reabrir la síntesis y recalcular | ignorar la nueva fuente o reemplazar sin trazabilidad |
| Dependencia oculta | tres respuestas proceden del mismo origen | contar una ruta de evidencia, no tres | aumentar confianza por número de mensajes |
| Capacidad insuficiente | no caben verificación y salida antes de plazo | `NO_COMMITMENT`/`PRESERVE_RESIDUAL` | declarar completitud no demostrada |

## Traza de los cuatro fallos no compensables

La síntesis no es un único gate. [00E](../00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) §§1, 5–8 fija cinco etapas, cuatro subsistemas/Q1–Q4, enmarcado Q0 y composición Q5; un techo de **100 millones de tokens**, recursos humanos y deadlines finitos. Ese techo no es presupuesto individual de cada brazo ni evidencia de que se gastó realmente. El fixture debe congelar snapshots, modelo, denominadores y asignación entre subsistemas (§7.2). La tabla inicial «evidencia cae» es una rama ilustrativa, **no equivale** a los cuatro modos originales.

| Paso | O / F del escenario | K | D condicionado |
|---|---|---|---|
| E0 marco | cuatro departamentos y decisión empresarial; presupuesto total común | Q0 alcance, fuente, capacidades, asignación, ventana | sin presupuesto por etapa y deadline explícitos, no afirmar que una ruta cabe. |
| E1 producción I2 | banca/seguros/fraude/resiliencia pueden heredar misma dependencia de datos (§5.1) | Q1 preservar hechos materiales, dependencia y residual | «cuatro dicen estable» no son cuatro corroboraciones; la compresión falsa no pasa. |
| E2 revisión I1 | dirección recibe representación ya empobrecida (§5.2) | Q2 capacidad humana/cola/alternativas para comprobar | repetir aprobación no corrige I2; escalar ilimitadamente tampoco. |
| E3 estrategia O2 | hipótesis plausibles de otros dominios (§5.3) | Q3 no promover posibilidad a estrategia sin evidencia pertinente | conservar opciones como candidatas, no decisión confirmada. |
| E4 despliegue O1 | residual estructural persiste (§5.4) | Q4 acción acotada y reversible si autorizada, plazo y residual | ni despliegue incierto como certeza ni veto infinito. |
| E5 composición | salidas de Q1–Q4 pueden parecer complementarias | Q5 no compensar gates fallidos con aprobaciones/fluidéz | fallo material en un gate no se promedia; síntesis cualificada o límite explícito. |

| Control/falsador | Resultado lógico |
|---|---|
| continuidad, snapshots/independencia estables | entregar decisión dentro de techo y plazo conservando lo decisivo; HOLD/búsqueda infinita falla. |
| dependencia compartida revelada | revisar Q1 y Q5, no inflar evidencia por conteo de mensajes. |
| nueva fuente independiente y autoridad aplicable | reabrir solo base afectada; cambio genuino no es sospechoso por definición. |
| cómputo insuficiente | preservar hechos y residual; `NO_COMMITMENT` a cierre no justificado, con owner/plazo. |
| peer fuerte | Agent 365 y LangGraph/LangSmith pueden instrumentar controles propuestos; si el peer preserva gates dentro del mismo techo/coste, no diferencial EA. |

No hay numeradores ni trazas de ejecución para cobertura/latencia. Una asignación de tokens no fijada impide demostrar que Q0–Q5 y la respuesta final caben bajo 100M; la celda cuantitativa queda `NO CONCLUSION`.

## KPI en papel

`Cobertura material = afirmaciones materiales conservadas / afirmaciones materiales del fixture`. La fracción no es una medición de producto: solo comprueba el cálculo sobre el denominador sintético fijado. Sin denominador fijado por el autor: `NO CONCLUSION`.
