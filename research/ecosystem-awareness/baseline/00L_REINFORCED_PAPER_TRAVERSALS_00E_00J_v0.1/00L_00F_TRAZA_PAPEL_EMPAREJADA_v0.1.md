# 00L-00F — Traza de papel emparejada: requalification de capacidad compartida

**Base:** 00F v0.2 Freeze Edition y perfiles FIWARE/AWS v0.2. **Estado:** traza calculada en papel sobre hechos sintéticos; no ejecución de FIWARE, AWS ni EA.

## Ficha congelada

Varias aplicaciones urbanas usan una capacidad compartida de movilidad. En el estado inicial, demanda, capacidad, prioridad y fuentes están dentro del modelo. H2 introduce un cambio material en una dependencia y en la prioridad autorizada; el broker/twin puede seguir entregando datos formalmente válidos.

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

## KPI en papel

`Divergencia sistémica = unidades con postura incompatible / unidades afectadas`. Solo se puede calcular si el fixture fija unidades, posturas y denominador. De lo contrario: `NO CONCLUSION`.
