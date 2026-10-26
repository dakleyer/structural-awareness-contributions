# Preparación del adaptador DDS hacia S5

**Versión ACC AUX DDS S5 0.1. Estado documental.** El receptor es el primer protocolo económico del modelo auxiliar. La fuente es [UC21 S5 aec08fb5](https://github.com/dakleyer/use-cases/blob/aec08fb5/contributions/when-controls-work-system-fails/annexes/scenarios/S5.md), preservada en el repositorio con su hash en la exportación. DDS mantiene la autoridad del método y el caso conserva sus criterios. Esta preparación no ejecuta una base de datos ni el oráculo UC21.

S5 plantea una orden de reparación que era adecuada al ponerse en cola; antes de ejecutarse, otro remedio resuelve el incidente y aparece una congelación de cambios. El token aún puede ser válido. El reto es conservar una base material vigente en el momento del efecto, con un control convencional competente admitido. T03 reproduce sólo ese motivo abstracto; T02 ilustra una caducidad técnica distinta y T04 una renovación legítima.

| Campo del modelo | Correspondencia candidata | Límite |
|---|---|---|
| Job y fase plan intento efecto | Orden en cola y efecto diferido | No es una operación real RDS o PostgreSQL |
| Versión y aprobación | Generación de configuración y base de decisión | Las versiones v1 v2 no son cfg217 cfg218 |
| Objetivo vigente y congelación | Incidente activo y cambio permitido | Requiere fuentes nativas autorizadas y frescas |
| Grant y caducidad | Autenticación y tiempo de concesión | Token vigente no demuestra vigencia semántica |
| Revisión y efecto observado | Control al actuar y verificación del resultado | Un intento bloqueado no se convierte en efecto |
| Saldo económico | Observación adicional del estudio receptor | No redefine el resultado del oráculo de fuente |

[adapter_preview.py](adapter_preview.py) exporta los eventos pertinentes y mantiene `source_case_assessment = NOT_RUN`. Conserva los resultados PASS o FAIL del modelo en su propio espacio y deja R0/R1/R2 sin mapear. El [preview reproducible](results/adapter_preview.json) es una preparación de correspondencia, no el resultado de S5.

Antes de un adaptador ejecutable faltan: seleccionar versión y criterio de fuente completos, congelar variante y brazo legítimo, establecer observabilidad y reloj, conectar una tecnología y sus fuentes actuales, fijar permisos, oráculos y recursos, y observar el efecto independiente. Un comparador convencional que satisfaga el reto obtiene pleno crédito; no se modifica el caso para retirárselo.

R01 no es necesario para este piloto determinista. Una conexión posterior deberá conservar sus rutas M I P y contratos de oráculo; no se equiparan a R0 R1 R2 ni a Stage A B C. El presente trabajo sólo aporta a la especificación de un estudio posterior y no inscribe o cierra una campaña DDS.
