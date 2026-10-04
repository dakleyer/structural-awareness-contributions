# Experimentos parciales y diagnósticos de viabilidad

[Estudio de viabilidad](../README.md) · [Prueba matemática actual](../PURE_MATHEMATICAL_TRILEMMA.md).

Este apartado conserva las comprobaciones ya realizadas. Son pruebas parciales y experimentos exploratorios, no el oráculo/harness independiente de R01, una prueba universal ni una campaña registrada. Esta reorganización no ejecuta de nuevo los scripts y no añade resultados científicos. Los scripts, fixtures, salidas y manifiestos JSON se trasladan sin modificar sus bytes. Fechas, conteos y rutas registrados siguen describiendo sus entregas históricas.

| Grupo | Código y entradas | Salidas conservadas | Alcance |
|---|---|---|---|
| M01 | [Checker](./historical/verify_m01_scope.py) | [Scope checks](./historical/M01_SCOPE_CHECKS.json) | Diagnóstico del contrato inicial; no cota en L. |
| M02 | [Checker](./historical/verify_m02_worlds.py) · [Fixture](./historical/M02_CONJUNCTION_FIXTURE.json) | [Mundos y rutas](./historical/M02_WORLD_CHECKS.json) · [Release](./historical/M02_RELEASE_CHECKS.json) | Pareja finita y controles, con su alcance original. |
| M10/P03 | [Checker](./historical/verify_m10_measurements.py) · [Contrato](./historical/M10_RECONCILED_CONTRACT.json) | [Medidas](./historical/M10_MEASUREMENT_CHECKS.json) · [Release](./historical/M10_RELEASE_CHECKS.json) | Auditoría de medición y contracontroles del fixture. |
| F/W | [Checker](./historical/verify_trilemma.py) · [Contrato](./historical/TRILEMMA_CONTRACT.json) | [Checks](./historical/TRILEMMA_CHECKS.json) · [Release](./historical/TRILEMMA_RELEASE_CHECKS.json) | Enumeración propia de tamaños pequeños; no revisión independiente ni prueba para todos los tamaños. |
| Material recibido | [Dossier completo](./received/2026-10-04/README.md) | [Admisión](./received/2026-10-04/INTAKE_CHECKS.json) · [Salidas](./received/2026-10-04/runs/executions.json) | Seis originales y diagnósticos adicionales; tecnologías en cola posterior. |

Los cuatro checkers históricos y sus fixtures quedan juntos en `historical/` para conservar sus dependencias locales. Los hashes originales son los del commit de entrada identificado en [el manifiesto](../RELOCATION_MANIFEST.json). Las rutas literales internas no se actualizan retrospectivamente. Los comandos de entregas anteriores describen su contexto original; para una reproducción futura, identifica el commit y ejecuta desde el directorio que contiene el script y los fixtures. Esa reproducción no cierra C05/M16.

## Seguimiento al final

| Trabajo | Estado | Siguiente obligación |
|---|---|---|
| Diagnósticos anteriores | Conservados y separados | Usarlos como pistas de errores, con su alcance. |
| Nuevos ejemplos científicos | No ejecutados en esta entrega | Congelar antes contrato y harness. |
| Oráculo/harness neutral | Pendiente C01–C05 | Ground truth, óptimo, ledger y medidas; método independiente y cobertura declarada. |
| Prueba universal | En documento matemático separado | Auditar lemas y políticas; no inferirla de estos resultados. |
