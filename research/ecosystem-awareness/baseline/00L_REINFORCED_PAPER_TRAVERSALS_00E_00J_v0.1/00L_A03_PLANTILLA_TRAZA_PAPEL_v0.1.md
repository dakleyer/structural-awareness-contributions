# 00L-A03 — Plantilla de traza de papel

## Separación obligatoria

| Tipo | Significado | Puede presentarse como resultado observado |
|---|---|---|
| Capacidad publicada | Lo que una fuente primaria del proveedor o estándar documenta | No |
| Implementación reforzada | Diseño adicional construido para la comparación | No |
| Hecho sintético | Entrada fijada por el escenario | No |
| Cálculo en papel | Salida derivada de hechos y reglas declarados | No |

## Registro mínimo por paso

| Campo | Contenido requerido |
|---|---|
| Identidad | escenario, rama/control, brazo, paso y versión de la ficha |
| Entrada | hecho, procedencia, hora/versión y observabilidad para el brazo |
| Regla | control documentado o regla propuesta; S/T/H/KPI y umbral |
| Cálculo | estado previo → operación lógica declarada → estado posterior; numerador/denominador si aplica |
| Decisión | acción permitida, responsable, plazo, residual y disposición del gate |
| Comprobación | oráculo limitado, contraejemplo y condición que refutaría la conclusión |

## Disposiciones permitidas

`EXECUTE`, `REQUALIFY`, `CONTAIN`, `NO_COMMITMENT`, `ESCALATE`, `PRESERVE_AND_ROUTE`, `DENY`, `EXPIRE` y `NO CONCLUSION`.

No se permite convertir un KPI aislado en un PASS: la condición `T#` completa y el límite de la fuente deben estar satisfechos.
