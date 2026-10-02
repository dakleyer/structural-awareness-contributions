# Oráculo de 00G-R01 — estado y verificación pendiente

**2 de octubre de 2026 · En proceso: todavía incompleto para 00G-R01.** Este documento registra la adaptación candidata del instrumento C3 al escenario reducido. No declara implementado ni validado el evaluador completo de C-V.

[Volver a 00G-R01, escenario reducido](../../reductions/00G-R01/README.md) · [Documento completo, §3.7](../../reductions/00G-R01/Escenario-creatividad-validacion.md#37-relación-con-el-trabajo-previo-y-sus-recorridos) · [Fundamento y prueba de la reducción en revisión](../../reductions/00G-R01/README.md#fundamento-y-prueba-de-la-reducción).

## Base conservada y alcance

El [C3 original v0.4](./README.md) conserva su código, documentación y [huellas congeladas](./DESIGN_FREEZE.json). Este documento de estado es una adición posterior, fuera de ese congelado; no redefine sus predicados ni sus resultados.

La reproducción aislada del 2 de octubre verificó las huellas y obtuvo 102 de 102 controles construidos satisfactorios. Ese resultado comprueba el instrumento en su dominio original T0/X y T1/Y, operación `inspect`; no equivale a ejecuciones con agentes ni verifica su adecuación completa a 00G-R01. El primer ensayo original mantiene los pendientes de integración, registro y ejecución descritos en el README y el protocolo de ronda 1.

## Qué está en verificación y qué falta

| Elemento | Estado para 00G-R01 | Evidencia necesaria para cerrarlo |
|---|---|---|
| Proyección hacia C3 | Pendiente de definir y verificar | Correspondencia explícita que conserve identidad, autoridad, aplicabilidad, alcance, compromiso, intento, efecto y tiempos, con controles positivos y negativos. Si pierde una distinción material, hace falta un sucesor versionado. |
| Óptimo admisible y calidad | Evaluador C-V pendiente de implementación | Mapa congelado, reglas de admisibilidad y comprobación exacta del óptimo según §2.17 del escenario. |
| Costes de búsqueda, validación y coordinación | Pendiente | Libro de costes que incluya descartes, reutilización, mantenimiento y tiempo; comprobaciones de consistencia antes de comparar configuraciones. |
| Mediación social y pertenencia a 00G | Aplicación de la reducción en revisión | Traza realizable y correspondencia con §3.5, conservación del predicado relacional y control positivo. Un PASS de C3 no decide la pertenencia a 00G. |
| Integración experimental | Pendiente | Implementación identificada, recursos y presupuestos fijados, recorder, trazas y registro previo del ensayo. |
| Evaluación colectiva y estadística | Pendiente | Métricas, tamaño y análisis predefinidos. `population_result=NOT_ASSESSED` no es aprobación colectiva. |
| Comparación de EA | Candidata; sin resultado propio | Implementación y comparación controlada bajo criterios comunes, admitiendo resultados favorables, adversos o indeterminados. |

Las obligaciones anteriores están abiertas; no se afirma que existan verificaciones experimentales en ejecución. El cierre documental de los enlaces no constituye el cierre de estas pruebas.

## Relación con la prueba de reducción

La [sección de fundamento de 00G-R01](../../reductions/00G-R01/README.md#fundamento-y-prueba-de-la-reducción) enlaza el argumento unidireccional previo, su revisión y las obligaciones de la especialización C-V-G. La prueba de reducción y la validación del oráculo son tareas relacionadas pero distintas: una comprueba qué relaciones se conservan; la otra, qué decisiones puede evaluar correctamente el instrumento.
