# 00L-A05 — Revisión adversarial corta

## Objeciones que deben conservarse

| Objeción | Efecto sobre la conclusión |
|---|---|
| Un peer convencional puede reconstruir autoridad raíz o revalidar la base semántica con igual o menor carga | elimina la ventaja diferencial de EA para esa rama; se conserva como resultado favorable al comparador |
| Una ruta positiva puede contener de más o llegar tarde si el cambio no es material | exige continuidad y cambio autorizado; si no se puede decidir, `NO CONCLUSION` |
| La ruta positiva puede actuar sin autoridad si trata una señal útil como permiso | falla S8/S12/S14; la disposición correcta es `PRESERVE_AND_ROUTE`, `REQUALIFY` o `NO_COMMITMENT` |
| Un KPI alto puede ocultar un gate incorrecto | el gate y su oráculo mandan; el KPI no convierte un fallo en PASS |
| Una fuente viva puede haber cambiado desde la consulta | la fila queda no congelada hasta release, historial o extracto permitido |

## Resultado de los pilotos

00H conserva la historia sin atacante, la pérdida silenciosa de preservación y la prueba U/G/I. 00I conserva el control de continuidad y la posibilidad de que el peer convencional ya detecte el drift. Ningún piloto se presenta como producto ejecutado.

## Pruebas que podrían derribar cada anexo ampliado

| Caso | Control que impide ganar con bloqueo | Peer fuerte / resultado adverso que hay que admitir |
|---|---|---|
| 00E | Q1–Q4 y Q5 dentro de 100M tokens y capacidad humana, sin veto infinito | instrumentación convencional conserva dependencias y residual con menor coste |
| 00F | V0 NORMAL, V1 conflicto conocido resuelto; plazo virtual 2/5 min | R2-peer detecta V8 y coordina en tiempo; freno local no prueba misión |
| 00G | Branch G permite transición con evidencia independiente y autoridad; bar continúa en F | peer conserva source-lineage tras compaction y pasa F/G al mismo coste |
| 00H | G autorizado ejecuta, I independiente no se agrega, V8 no material no escala | peer une grants de raíz, ledger y controles de pago sin sobrecarga |
| 00I | V0 ejecuta y V10 no deja hueco check→act | peer revalida bases y liga versión al efecto sin espera/coste excesivo |
| 00J | C0/C1/C2/C4/C6 preservan uso/transferencia/independencia/UNKNOWN/re-entry | sistema de derechos ordinario resuelve la proposición exacta y la disputa igual de bien |

Cada salida comparativa sigue `NO CONCLUSION` sin logs, costes y mismo fixture. El oráculo nunca debe entregarse a un brazo para resolver una rama oculta.
