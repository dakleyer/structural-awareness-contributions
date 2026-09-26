# 00L — Refuerzo de recorridos 00E–00J

> **Evidence correction — 26 September 2026:** [A14](./00L_A14_CORRECCIONES_AUDITORIA_v0.1.md) records corrected handoff checks, failure traces, metrics, authority/time boundaries and input validation: 379 existing regressions and 77 separate correction checks pass locally. Shared-logic peers remain instrumentation controls; the A22 semantic bridge and A23 fidelity obligations remain open. [Cumulative article/README record A12](./00L_A12_REGISTRO_MEJORAS_ARTICULO_README_v0.1.md).

**Estado:** paquete aditivo integrado en `main` el 26 de septiembre de 2026 mediante [PR #1](https://github.com/dakleyer/structural-awareness-contributions/pull/1), merge [`59ca3c4`](https://github.com/dakleyer/structural-awareness-contributions/commit/59ca3c428d1cf28b7d8f4bdb8f2b5af89d852604). Recorridos en papel y ejecuciones simbólicas acotadas; sin ejecución de productos.

Este paquete aplica el plan de refuerzo de recorridos a los seis escenarios 00E–00J. No sustituye, congela ni reescribe los escenarios, perfiles de producto o requisitos canónicos. Sus tablas son **deducciones condicionales en papel sobre hechos sintéticos**.

## Entregables

1. [Inventario de afirmaciones de los nueve perfiles](./00L_A01_INVENTARIO_FUENTES_NUEVE_PERFILES_v0.1.md).
2. [Fichas comunes de hechos y controles](./00L_A02_FICHAS_HECHOS_CONTROLES_00E_00J_v0.1.md).
3. [Plantilla de traza emparejada](./00L_A03_PLANTILLA_TRAZA_PAPEL_v0.1.md).
4. [Anexo 00H — oportunidad más allá de la autoridad](./00L_00H_TRAZA_PAPEL_EMPAREJADA_v0.1.md).
5. [Anexo 00I — revalidación en el momento de actuar](./00L_00I_TRAZA_PAPEL_EMPAREJADA_v0.1.md).
6. [Anexo 00E — síntesis bajo capacidad finita](./00L_00E_TRAZA_PAPEL_EMPAREJADA_v0.1.md).
7. [Anexo 00F — requalification de capacidad compartida](./00L_00F_TRAZA_PAPEL_EMPAREJADA_v0.1.md).
8. [Anexo 00G — estabilidad del marco con procedencia](./00L_00G_TRAZA_PAPEL_EMPAREJADA_v0.1.md).
9. [Anexo 00J — procedencia y derechos por proposición](./00L_00J_TRAZA_PAPEL_EMPAREJADA_v0.1.md).
10. [Anexos 00E–00J y estado de preparación](./00L_A04_ANEXOS_00E_00J_ESTADO_v0.1.md).
11. [Revisión adversarial corta](./00L_A05_REVISION_ADVERSARIAL_v0.1.md).
12. [Índice de afirmaciones publicables](./00L_A06_INDICE_AFIRMACIONES_PUBLICABLES_v0.1.md).
13. [Mapa de integración con los recorridos originales](./00L_A07_MAPA_INTEGRACION_RECORRIDOS_ORIGINALES_v0.1.md).
14. [Protocolo de reproducibilidad, observación y oráculo](./00L_A08_PROTOCOLO_REPRODUCIBILIDAD_v0.1.md).
15. [Puente a fixtures simbólicos ejecutados y falsadores](./00L_A09_PUENTE_TRAZAS_EVIDENCIA_SIMBOLICA_v0.1.md).
16. [Verificación ejecutada de parejas positivas/negativas y paso previo](./00L_A10_VERIFICACION_PARES_Y_PREVUELO_v0.1.md) · [datos](./00L_A10_PARES_CONTROLADOS.json) · [script](./verify_paired_symbolic.py).
17. [Registro de reproducción A11 y CI de la revisión corregida](./00L_A11_REGISTRO_REPRODUCCION_Y_TRAZAS_v0.1.md) · [12 trazas JSONL](./00L_A11_TRAZAS_EJECUTADAS.jsonl).
18. [Registro A12 de mejoras, evidencia y texto para artículo/README](./00L_A12_REGISTRO_MEJORAS_ARTICULO_README_v0.1.md).

## Regla de lectura

`H0`, `H1` y `H2` son brazos de comparación. La ruta positiva es un modelo de éxito de diseño. Ninguna tabla de este paquete informa telemetría, rendimiento observado o resultado de los productos comparados. Sí existen **ejecuciones simbólicas previas de fixtures 00K**, enlazadas con sus límites y falsadores en A09; no equivalen a ejecución de EA en los productos. Cuando los documentos actuales no determinan una celda, se conserva `NO CONCLUSION`.

## Orden de trabajo

Los seis anexos contienen reglas paso a paso y controles adversos; A09 conecta evidencia simbólica existente y el resultado adverso A6a. A10 añade **12 comprobaciones simbólicas nuevas** sobre parejas aisladas, 128 mutaciones de campos interceptadas por el verificador 00L y la corrección de un límite estricto del fixture activo 00H. A11 conserva las doce observaciones/disposiciones con hashes e identifica el run de CI **379/379 del árbol de integración posterior a la corrección**, sin confundirlo con el run histórico. Todavía no hay ejecución de los nueve perfiles ni logs para comparar H0/H1/H2 en producto. El siguiente hito es congelar campos pendientes de A04, registrar observaciones/costes conforme A08, y solo entonces adjudicar resultados. Cada uno de los seis escenarios originales ahora incluye una nota aditiva con enlaces directos a su anexo, A08–A12; [A07](./00L_A07_MAPA_INTEGRACION_RECORRIDOS_ORIGINALES_v0.1.md) conserva la ubicación y el alcance registrados antes del merge. [A12 §8](./00L_A12_REGISTRO_MEJORAS_ARTICULO_README_v0.1.md) documenta la integración, las correcciones A23/A25, la versión 4 del artículo y los pendientes científicos.
