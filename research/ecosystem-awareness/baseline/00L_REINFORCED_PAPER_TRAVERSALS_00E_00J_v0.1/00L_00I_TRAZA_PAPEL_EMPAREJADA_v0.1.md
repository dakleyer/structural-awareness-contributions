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

## Límite de la conclusión

La tabla demuestra que la ruta puede reconstruirse desde hechos y reglas declaradas. No demuestra latencia, disponibilidad, corrección de AWS, ni superioridad de EA. Si R1 ya detecta todos los cambios con menor carga, la afirmación diferencial queda refutada para esa rama.
