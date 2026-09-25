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

## KPI en papel

`Cobertura material = afirmaciones materiales conservadas / afirmaciones materiales del fixture`. La fracción no es una medición de producto: solo comprueba el cálculo sobre el denominador sintético fijado. Sin denominador fijado por el autor: `NO CONCLUSION`.
