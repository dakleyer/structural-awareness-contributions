# 00L-00F — Traza de papel emparejada: requalification de capacidad compartida

**Base:** 00F v0.2 Freeze Edition y perfiles FIWARE/AWS v0.2. **Estado:** traza calculada en papel sobre hechos sintéticos; no ejecución de FIWARE, AWS ni EA.

## Ficha congelada

**Evidencia complementaria:** [A09](./00L_A09_PUENTE_TRAZAS_EVIDENCIA_SIMBOLICA_v0.1.md) traza dos ejecuciones simbólicas anteriores: 00K-A3/P3 (conflicto sin marcador HOLD tras detectar un confusor) y 00K-A6b/P6 (compatibilidad recurso-tiempo con autoridad y frescura emparejadas). No son simulación de ciudad, ni verifican la ventana física de 2/5 minutos.

Varias aplicaciones urbanas usan Central Bridge. R1 debe superar V0/V1 y degradaciones conocidas antes de congelarse. H2/R2 introduce **V8, drift de dependencia, topología o mapeo**, no presupone cambio de prioridad municipal; el broker/twin puede seguir entregando datos formalmente válidos. Una prioridad autorizada nueva es control distinto que también exige recalificación.

## Recorrido H0/H1/H2 y ruta positiva

| Paso | H0 — integración competente | H1 — implementación reforzada | H2 — mismo H1 bajo cambio | Ruta positiva EA/diseño |
|---|---|---|---|---|
| Entrada | cada aplicación recibe contexto local y actúa con su regla | se conservan fuente, freshness, dependencia, capacidad y objetivo común | contexto formalmente válido, pero cambia la relación capacidad–demanda/prioridad | decisión recibe estado compartido, incertidumbre y autoridad vigente |
| Regla | `local_context ∧ local_policy → posture` | comprobar coherencia de capacidad, prioridad y alcance antes de actuate | `material_change=1` → requalification del modelo común | S1/S3/S10/S11/S14; no confundir broker actualizado con misión actual |
| Cálculo | posturas A/B/C individualmente plausibles pero incompatibles | comparar acciones y efectos agregados; detener solo la parte afectada | `capacity_model_stale ∨ priority_changed` → `CONTAIN/REQUALIFY` | recalcular postura compartida; mantener acciones no afectadas |
| Decisión | puede producir divergencia sistémica sin error local | coordina o escala con owner municipal y deadline | no ejecutar con la capacidad/prioridad antigua | `REQUALIFY`, `CONTAIN` o `PASS WITH EXPLICIT LIMIT`; no blanket HOLD |
| Oráculo | falla si la ciudad no obtiene una postura coherente | pasa si evita divergencia y conserva control local válido | falla si continúa con modelo stale o bloquea todo | se refuta si H1 detecta y resuelve el cambio con menor carga |

## Controles emparejados

| Rama | Hecho | Salida calculada | Condición de refutación |
|---|---|---|---|
| Continuidad | demanda, capacidad, prioridad y fuentes sin cambio material | ejecutar posturas coherentes | detener todas las acciones |
| Cambio autorizado | autoridad municipal cambia prioridad y lo publica | requalification de la capacidad afectada | ignorar autoridad o tratarla como dato ordinario |
| Dependencia divergente | dos fuentes derivan de la misma fuente raíz | preservar dependencia; no sumar corroboración | contar señales correlacionadas como independientes |
| Capacidad incierta | capacidad compartida no determinable dentro de la ventana | `CONTAIN`/`NO_COMMITMENT` para la parte material | actuate por promedio implícito o contexto viejo |

## Traza por variante con reloj y recurso compartido

La tabla superior mezcla conflicto conocido y drift: se desambiguan con [00F Freeze Edition](../00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_FREEZE_EDITION.md) §§3, 5–8C. El escenario prescribe **dos minutos para calificar dentro de una ventana de acción de cinco** (parámetros virtuales, no recomendaciones urbanas). Los actores pueden optar A/B/NORMAL/HOLD; el freno local puede funcionar a las 08:21 y aun así fallar la misión por bloqueo del puente. No se fijan aquí capacidad cuantitativa, ocupación ni recuento de operadores.

| Paso | F/O | Regla Q | D en el papel / límite |
|---|---|---|---|
| F0 | Central Bridge compartido; scopes y envolvente normales | Q0 liga decisión recurso-tiempo, autoridades, fallback e invariantes locales | si faltan scopes/owners: UNKNOWN, no permiso implícito. |
| F1 | observaciones discordantes y grafo de fuentes | Q1 examina frescura **semántica** y dependencia, no solo timestamp presente | V2/V3/V4: consenso aparente no basta; dependencia no observable ⇒ límite explícito. |
| F2 | A y B pretenden ocupación incompatible | Q2 compone acciones sobre recurso/intervalo; mantiene freno de emergencia | V1: evitar ocupación simultánea; R1 **debe poder aprobar** este conflicto conocido. |
| F3 | humanos y tiempo finitos | Q3 controla carga/expiración/fallback autorizado | a minuto 2, calificación suficiente o postura acotada; espera infinita falla. |
| F4 | modelo/fuentes cambian tras congelar R1 | Q4 reabre solo bases afectadas; Q5 confirma continuidad/retorno | V8: recalificar relación nueva; no reutilizar mapeo viejo ni HOLD global por defecto. |

| Control | Igualdad entre brazos | Salida deducida; falsador |
|---|---|---|
| V0 | envolvente y capacidad sin cambio | NORMAL compartido; parada sistemática falla. |
| V1 | A/B se oponen en mismo intervalo | bloquear incompatibilidad; si R1 falla, fortalecer peer antes de hablar de EA. |
| V2/V3 | varias fuentes derivan de una raíz | una ruta de evidencia, no quorum; no inventar independencia. |
| V5/V6 | cola humana excede presupuesto / alertas alternan | fallback con vencimiento e histéresis; ni oscilación ni espera sin fin. |
| V7 | actores no representados | residual de cobertura; no afirmar completitud urbana. |
| V8 | dependencia/mapping cambia tras freeze | R2-peer y R2-EA reciben **mismo evento observable, autoridad y presupuesto**; si peer detecta a tiempo y coste ≤, diferencial refutado. |
| V9 | margen comprimido | recalificar solo si aún cabe en plazo; si no, contener parte afectada sin sacrificar control local. |

FIWARE/Orion-LD y AWS IoT TwinMaker/Core son dos trayectorias de integración, no oráculos de misión. Capacidad de transportar contexto/twin ≠ composición de posturas. Resultado de cada producto y KPI de divergencia/coste: `NO CONCLUSION` sin ejecución, unidades, posturas y logs.

## KPI en papel

`Divergencia sistémica = unidades con postura incompatible / unidades afectadas`. Solo se puede calcular si el fixture fija unidades, posturas y denominador. De lo contrario: `NO CONCLUSION`.
