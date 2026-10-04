# R01 — Estudio de viabilidad del trilema

Trabajo en desarrollo · 4 de octubre de 2026 · Prueba matemática primero; tecnologías después.

Entrada desde el [README completo de R01](../README.md#viability-work-in-progress). Este directorio reúne el estudio, los borradores anteriores y los diagnósticos parciales. El escenario, las reducciones, las extensiones, los documentos exportados y sus figuras conservan su contenido. Este estudio no modifica la especificación canónica ni anuncia una campaña ejecutada.

El objetivo es demostrar una imposibilidad **en familias de configuraciones determinadas**, para todas las políticas de una clase explícita, y demostrar también regiones viables. No se pretende demostrar que las tres condiciones sean incompatibles en toda configuración ni que una misma política falle en todos los mundos.

| Lectura | Documento | Estado |
|---|---|---|
| Documento matemático actual | [Configuraciones, cuantificadores y frontera exacta](./PURE_MATHEMATICAL_TRILEMMA.md) | Derivación simbólica en F; revisión independiente y transferencia a R01 pendientes. |
| Trabajo y prioridades | [Plan vigente](./WORKPLAN.md) · [55 tareas y estados](./WORKPLAN_STATUS.json) | M12 en desarrollo; primero cerrar alcance y demostración sin intervenciones tecnológicas. |
| Continuación y revisión | [Instrucciones completas](./CONTINUATION_PROMPT.md) | No convertir ejemplos o scripts propios en prueba universal. |
| Borradores conservados | [Índice de trabajos anteriores](./previous-work/README.md) | Entregas históricas, con su fecha y alcance. |
| Experimentos parciales | [Inventario separado](./partial-experiments/README.md) | Diagnósticos del autor y material recibido; no constituyen un oráculo/harness independiente. |
| Conservación | [Mapa de traslados](./RELOCATION_MANIFEST.json) · [Verificación documental](./PRESERVATION_CHECKS.json) | Control de almacenamiento, navegación y contenido; sin nuevas ejecuciones científicas. |

Las afirmaciones tecnológicas ya escritas permanecen en el archivo anterior para revisión posterior. No son la prioridad activa. Los comandos y rutas literales de los informes históricos describen su publicación original; el manifiesto conserva ese commit y los blobs de entrada. Para los scripts históricos juntos, el directorio de trabajo actual es `feasibility/partial-experiments/historical/`; fixtures y dependencias de esos scripts se trasladan juntos sin modificar sus bytes. Reproducirlos sigue siendo un diagnóstico parcial, no una validación independiente.

## Seguimiento al final

| Elemento | Disponible | Pendiente |
|---|---|---|
| Trilema por configuraciones | Familia F no vacía, tres controles por pares y región de viabilidad con frontera inclusiva. | Auditoría independiente de la prueba y puente a todas las políticas relevantes de R01. |
| Regiones con un solo objetivo | Distinción formal entre resultados de una política y posibilidades de una configuración. | Precisar si se pide un resultado de política o imposibilidad de todos los pares; esta última no se deriva del modelo con abstención barata y segura. |
| Oracle/harness | Especificación previa y diagnósticos conservados. | Implementación neutral, segundo método y auditoría de cobertura. |
| Tecnologías | Material y derivaciones históricas archivados. | Reanudar después del alcance y los lemas de la prueba base. |
| Manuscrito independiente | [Trilema condicionado](./CONDITIONED_TRILEMMA.md) | Prueba completa para ambas medidas de eficacia; frontera AVG para hechos sesgados y frontera WC; no vaciedad y controles. |
| Revisión del manuscrito | [Auditoría simbólica propia](./CONDITIONED_TRILEMMA_SELF_REVIEW.md) | No sustituye M16. Criterios adversariales disponibles para un revisor externo. |
| Auditoría de fondo | [Reconstrucción y reparaciones](./CONDITIONED_TRILEMMA_DEEP_AUDIT.md) | El lema se conserva; capacidad física B, cortes factibles, éxito por rama y condiciones de transferencia se explicitan en v0.2. |
| Extensión a R01 | [Mapa, prueba local y familia G](./R01_TO_CONDITIONED_TRILEMMA_MAPPING.md) | Familia con contexto técnico inicial pagado, catálogo explícito y tamaños arbitrarios; todos los pares y triple imposible en su banda. Dureza informativa creciente de F y validación externa pendientes. |
| Estado vigente de auditoría | [55 tareas](./WORKPLAN_STATUS.json) · [Release](./DEEP_AUDIT_RELEASE.json) | 4 DONE históricas, 7 IN_PROGRESS, 44 OPEN. M17 en desarrollo; ninguna tarea científica cerrada. Sin nuevas ejecuciones científicas. |
| Teorema principal en R01 — estado posterior | [Trilema condicionado en R01](./R01_CONDITIONED_TRILEMMA_THEOREM.md) | Dominio completo, criterio general, corte y regiones no vacías. Familia con paridad de K datos y coste K: la dureza creciente ya tiene una construcción simbólica, distinta de F. Revisar fidelidad y demostración independientemente. |
| Revisión y conservación de esta entrega | [Revisión propia](./R01_CONDITIONED_TRILEMMA_REVIEW.md) · [Registro](./R01_CONDITIONED_TRILEMMA_RELEASE.json) | No cierra M16/M17 ni transforma campañas pendientes en evidencia. El binding compartido y las configuraciones fáciles no refutan el trilema condicionado. |
