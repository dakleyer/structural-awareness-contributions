# Recorrido manual del primer estudio económico

Este recorrido fija decisiones y balances antes de implementar el modelo. Los números son ilustrativos. Marketing financia una unidad de preparación y 0,25 por paso; esos recursos se registran incluso cuando se rechaza una propuesta. Las transferencias suman cero y los doce de reconfiguración sólo se consumen cuando existe efecto.

| Actor | Beneficio directo | Transferencia elegida | Reconfiguración | Saldo antes de preparación y revisión |
|---|---:|---:|---:|---:|
| Marketing | 60 | -40 | 6 | 14 |
| Operaciones | 40 | 0 | 4 | 36 |
| Sistemas | -30 | 40 | 2 | 8 |
| Finanzas | 0 | 0 | 0 | 0 |
| Total | 70 | 0 | 12 | 58 |

En un paso, la preparación y revisión consumen 1,25 adicionales, imputados a Marketing: el saldo total completo es 56,75. La alternativa Marketing -6 y Operaciones -34 también compensa a Sistemas y mantiene el saldo agregado; no se impone un pagador único. El gasto de preparación está encargado explícitamente: no se afirma que cada estudio rechazado deje indemnes a sus participantes.

| Caso | Decisiones esperadas de ambos procedimientos principales | Efecto operativo neto | Saldo completo |
|---|---|---:|---:|
| E01 Agreement after feasible compensation | EXECUTE_ADJUSTED | 58 | 56.75 |
| E02 Immediate joint agreement | EXECUTE_IMMEDIATE | 98 | 96.75 |
| E03 Another payer allocation | EXECUTE_ADJUSTED | 58 | 56.75 |
| E04 Negative total surplus | HOLD_NO_AGREEMENT | 0 | -1.25 |
| E05 Positive sum does not override rights | HOLD_RIGHTS | 0 | -1.25 |
| E06 Unchanged output is a hard condition | HOLD_SERVICE | 0 | -1.25 |
| E07 Silent participant is not consent | HOLD_PARTICIPATION | 0 | -1.25 |
| E08 Uncharacterized estimate | HOLD_INFORMATION | 0 | -1.25 |
| E09 Indistinguishable safe world | EXECUTE_ADJUSTED | 58 | 56.75 |
| E10 Indistinguishable costly world | EXECUTE_ADJUSTED | -42 | -43.25 |
| E11 Pessimistic estimate misses a real opportunity | HOLD_NO_AGREEMENT | 0 | -1.25 |
| E12 Duplicate instruction cannot create a second gain | EXECUTE_ADJUSTED → ALREADY_EXECUTED | 58 | 56.5 |
| T01 Unchanged basis across a queue delay | PLAN_ADJUSTED → EXECUTE_ADJUSTED | 58 | 56.5 |
| T02 Expiry between agreement and effect | PLAN_ADJUSTED → HOLD_GRANT | 0 | -1.5 |
| T03 Superseding repair with a still valid token | PLAN_ADJUSTED → HOLD_PURPOSE | 0 | -1.5 |
| T04 Legitimate renewal after scope change | PLAN_ADJUSTED → HOLD_APPROVAL → EXECUTE_ADJUSTED | 58 | 56.25 |
| T05 Continuity through stable changed and novel jobs | EXECUTE_ADJUSTED → HOLD_APPROVAL → EXECUTE_ADJUSTED → EXECUTE_ADJUSTED | 174 | 172 |
| T06 Finite inquiry without manufactured explanation | HOLD_INQUIRY → HOLD_INQUIRY → HOLD_CAUSE_UNRESOLVED | 0 | -1.75 |

T03 es un control de obsolescencia semántica con token todavía válido; T02 es un caso distinto de caducidad técnica. En E10 ambos métodos actúan igual que en E09 y el resultado real falla: reproducir ese fallo no lo convierte en PASS. E11 distingue una abstención fundada en información admitida de la oportunidad que ve el evaluador. T05 representa tres encargos distintos; E12 impide cobrar dos veces un mismo efecto.

Las dos políticas principales pueden empatar. El control stale_reference es deliberadamente incompleto y no se usa para atribuir superioridad frente a un procedimiento convencional competente. La prueba examina una especificación pequeña, no la eficacia de EA ni la integración del ACC.
