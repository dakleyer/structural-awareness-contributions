# 00L-00I — Traza de papel emparejada

**Fuente de hechos:** 00I v0.5 Freeze Edition y su perfil AWS Step Functions/RDS. **Estado:** cálculo en papel; no ejecución de AWS ni de EA.

## Ficha congelada para este cálculo

En `T1`, Patch A fue calificado con incidente abierto, diagnóstico y configuración `g9`. Antes de `t_act`, se publica Patch B, el incidente se resuelve y entra un freeze. El contrato exige volver a leer fuente, versión, freeze, diagnóstico e intervención en el límite de acción. La continuidad válida mantiene todas las precondiciones materiales.

## Recorrido R0/R1/R2 y ruta positiva

| Paso | R0 — workflow ordinario | R1 — mismo stack defendido en régimen original | R2 — el mismo R1 bajo cambio material | Ruta positiva de requalification |
|---|---|---|---|---|
| 1. Entrada | decisión T1, token válido, Wait/Task programados | T1 conserva base, versión, fuente y owner | entrada igual, pero `g9 → g10`, incidente cerrado y freeze activo | reabre la base afectada en el límite de uso |
| 2. Regla | token actual → puede invocar Task | Q0–Q5; comprobar base semántica y versión antes de actuar | Q0 puede ser PASS, pero Q2/Q3/Q4 detectan cambio material | S3/S10/S14; freshness/version binding; `REQUALIFY` |
| 3. Cálculo | `authorized(T1) ∧ queued(T1) → EXECUTE(T2)` | `grant ∧ basis_current ∧ no_freeze → EXECUTE` | `grant=1`, `basis_current=0`, `freeze=1` → `REQUALIFY`; Patch A ya no aplica | actualizar observaciones; invalidar A; evaluar B o `DENY` |
| 4. Decisión | puede reintroducir estado superseded/reboot durante freeze | ejecuta sin cambio en continuidad válida | no ejecuta rollback de A; owner y plazo quedan explícitos | `DENY` para A; `ESCALATE` solo si existe excepción autorizada |
| 5. Oráculo | falla si actúa con base stale | pasa si ejecuta continuidad y preserva la base | pasa si no continúa con A y no hace blanket HOLD | refuta la ventaja si R2 convencional ya revalida con igual/menor carga |

## Controles positivos y adversos

| Rama | Hecho fijo | Resultado calculado en papel | Refutación |
|---|---|---|---|
| Continuidad V0 | no cambia condición, fuente ni versión | `EXECUTE` dentro de presupuesto | HOLD/DENY sin causa material falla |
| V2/V9 | freeze o diagnóstico cambia | `REQUALIFY`; A no se ejecuta | ejecutar A es continuación falsa |
| V3/V4 | fuente stale o unavailable | `NO CONCLUSION`/`REQUALIFY`, no PASS | aceptar cache o ausencia como actual falla |
| V10 | cambio entre recheck y actuation | reabrir por version binding | ejecutar después de ruptura falla |

## Traza temporal: observación frente a oráculo

Base: [00I Freeze Edition](../00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_FREEZE_EDITION.md) §7–12 y [perfil AWS](../00I_A01_AWS_STEP_FUNCTIONS_RDS_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md). `INC-5521`/`G-5521`/Patch A/B son sintéticos. El [fixture ASL](../fixtures/00I-AWS/README.md) es artefacto de diseño, no medición del servicio.

| Instante | F/O exigida | K y estado lógico | D; E verifica después |
|---|---|---|---|
| `t0` | incidente abierto, diagnóstico, Patch A, G-5521, gen/config y freeze cualificados | Q0–Q4 identidad/fuente/versión/grant; Q5 continuidad | A elegible **en t0**, no permiso perpetuo. |
| `t1` | evento programado; no nuevo efecto | persistir base/versión; Wait/Task/Choice no hacen por sí solos recheck semántico | WAIT; token de Task no equivale a base vigente. |
| `t2` sin cambio | releer incidente, configuración, freeze, fuente y grant autorizados | `current_basis ∧ applicable_patch ∧ no_freeze ∧ grant_current` | V0 ejecuta A si todos y plazo pasan; lectura ausente ⇒ UNKNOWN. |
| `t2` alterado | cfg=218, RESOLVED, freeze ACTIVE, B supersede A (§10) | `basis_A_current=0`, `freeze_active=1` incluso si grant válido | no ejecutar A; B necesita nueva calificación. E no aporta datos al runtime. |
| `t2→t_act` | cambio entre lectura y efecto V10 | binding de versión/CAS o verificación atómica; Q6 es **clarificación candidata**, no gate canónico | si el vínculo se rompe no actuar; si la primitiva no está descrita, `NO CONCLUSION` de atomicidad. |

| Control | Rama original | Resultado lógico / falsador |
|---|---|---|
| V0 | precondiciones estables | ejecutar dentro de ventana; HOLD infundado falla. |
| V2/V9 | freeze/diagnóstico según variante | recheck e invalidación; **no son el H2/R2 de drift de modelo**. |
| V3/V4 | fuente stale/unavailable | UNKNOWN/REQUALIFY; no aceptar cache ni rechazar eternamente si reaparece. |
| V10 | ruptura check→act | efecto condicionado a versión; sin atomicidad demostrada no PASS. |
| H2/R2 | **mismo peer R1 congelado**, modelo de validez bajo drift §12 | peer puede detectar; no presuponer fallo ni confundir con V2/V9. |

Latencia/freshness requieren `max_requalification_age`, margen check→act y registros concretos: cfg=218 no suministra esos números. Coste incluye lecturas/espera/humanos; no se adjudica diferencial hasta ejecutar brazos emparejados. R1 con lectura condicional y CAS de precisión/carga equivalente refuta ventaja.

## Límite de la conclusión

La tabla anterior es una deducción de diseño, no una salida observada R0/R1/R2. No demuestra latencia, disponibilidad, corrección de AWS, ni superioridad de EA. Si R1 ya detecta todos los cambios con menor carga, la afirmación diferencial queda refutada para esa rama.
