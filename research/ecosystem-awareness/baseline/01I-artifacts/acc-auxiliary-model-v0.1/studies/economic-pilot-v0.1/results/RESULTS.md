# Resultados del primer modelo determinista

El ejecutable concuerda con el recorrido manual congelado. Esta concordancia cualifica este modelo pequeño; los FAIL previstos siguen siendo fallos de escenario.

| Caso | Procedimiento | Acciones | Saldo completo | Resultado del escenario |
|---|---|---|---:|---|
| E01 | conventional_adaptive | EXECUTE_ADJUSTED | 56.75 | PASS |
| E01 | qualified_record | EXECUTE_ADJUSTED | 56.75 | PASS |
| E02 | conventional_adaptive | EXECUTE_IMMEDIATE | 96.75 | PASS |
| E02 | qualified_record | EXECUTE_IMMEDIATE | 96.75 | PASS |
| E03 | conventional_adaptive | EXECUTE_ADJUSTED | 56.75 | PASS |
| E03 | qualified_record | EXECUTE_ADJUSTED | 56.75 | PASS |
| E04 | conventional_adaptive | HOLD_NO_AGREEMENT | -1.25 | HOLD |
| E04 | qualified_record | HOLD_NO_AGREEMENT | -1.25 | HOLD |
| E05 | conventional_adaptive | HOLD_RIGHTS | -1.25 | HOLD |
| E05 | qualified_record | HOLD_RIGHTS | -1.25 | HOLD |
| E06 | conventional_adaptive | HOLD_SERVICE | -1.25 | HOLD |
| E06 | qualified_record | HOLD_SERVICE | -1.25 | HOLD |
| E07 | conventional_adaptive | HOLD_PARTICIPATION | -1.25 | HOLD |
| E07 | qualified_record | HOLD_PARTICIPATION | -1.25 | HOLD |
| E08 | conventional_adaptive | HOLD_INFORMATION | -1.25 | HOLD |
| E08 | qualified_record | HOLD_INFORMATION | -1.25 | HOLD |
| E09 | conventional_adaptive | EXECUTE_ADJUSTED | 56.75 | PASS |
| E09 | qualified_record | EXECUTE_ADJUSTED | 56.75 | PASS |
| E10 | conventional_adaptive | EXECUTE_ADJUSTED | -43.25 | FAIL |
| E10 | qualified_record | EXECUTE_ADJUSTED | -43.25 | FAIL |
| E11 | conventional_adaptive | HOLD_NO_AGREEMENT | -1.25 | HOLD |
| E11 | qualified_record | HOLD_NO_AGREEMENT | -1.25 | HOLD |
| E12 | conventional_adaptive | EXECUTE_ADJUSTED → ALREADY_EXECUTED | 56.5 | PASS |
| E12 | qualified_record | EXECUTE_ADJUSTED → ALREADY_EXECUTED | 56.5 | PASS |
| T01 | conventional_adaptive | PLAN_ADJUSTED → EXECUTE_ADJUSTED | 56.5 | PASS |
| T01 | qualified_record | PLAN_ADJUSTED → EXECUTE_ADJUSTED | 56.5 | PASS |
| T02 | conventional_adaptive | PLAN_ADJUSTED → HOLD_GRANT | -1.5 | HOLD |
| T02 | qualified_record | PLAN_ADJUSTED → HOLD_GRANT | -1.5 | HOLD |
| T02 | stale_reference | PLAN_ADJUSTED → ATTEMPT_BLOCKED | -1.5 | FAIL |
| T03 | conventional_adaptive | PLAN_ADJUSTED → HOLD_PURPOSE | -1.5 | HOLD |
| T03 | qualified_record | PLAN_ADJUSTED → HOLD_PURPOSE | -1.5 | HOLD |
| T03 | stale_reference | PLAN_ADJUSTED → EXECUTE_ADJUSTED | -13.5 | FAIL |
| T04 | conventional_adaptive | PLAN_ADJUSTED → HOLD_APPROVAL → EXECUTE_ADJUSTED | 56.25 | PASS |
| T04 | qualified_record | PLAN_ADJUSTED → HOLD_APPROVAL → EXECUTE_ADJUSTED | 56.25 | PASS |
| T05 | conventional_adaptive | EXECUTE_ADJUSTED → HOLD_APPROVAL → EXECUTE_ADJUSTED → EXECUTE_ADJUSTED | 172.0 | PASS |
| T05 | qualified_record | EXECUTE_ADJUSTED → HOLD_APPROVAL → EXECUTE_ADJUSTED → EXECUTE_ADJUSTED | 172.0 | PASS |
| T06 | conventional_adaptive | HOLD_INQUIRY → HOLD_INQUIRY → HOLD_CAUSE_UNRESOLVED | -1.75 | HOLD |
| T06 | qualified_record | HOLD_INQUIRY → HOLD_INQUIRY → HOLD_CAUSE_UNRESOLVED | -1.75 | HOLD |

Ambos procedimientos principales empatan en estas instancias. Con una unidad adicional de preparación, el registro cualificado resulta una unidad más caro por caso. E10 conserva el límite de información: ambos ejecutan una transición realmente desfavorable. El control incompleto se mantiene separado y no fundamenta superioridad frente a un proceso convencional competente.

Los controles auxiliares ilustran el incentivo de una puerta basada sólo en W, las distinciones de capacidad humana y un ahorro con servicio equivalente. No miden felicidad, habilidades o prácticas de una organización real. DDS formal y ejecución nativa UC21/R01 permanecen pendientes.
