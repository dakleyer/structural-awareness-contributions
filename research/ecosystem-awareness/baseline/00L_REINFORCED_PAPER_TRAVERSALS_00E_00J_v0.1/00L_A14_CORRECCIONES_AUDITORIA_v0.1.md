# 00L-A14 — Correcciones tras la auditoría transversal

**Fecha:** 26/09/2026, Europe/Madrid. **Base pública corregida:** `28b7666d8db26634a0f92458146b86f6b25c304f`. La auditoría A13 estudió el código de `8f17843`; el commit base añadió su informe, sin modificar esas implementaciones.

Esta entrega corrige 18 comportamientos observados por A13 y añade sus regresiones. Los otros dos hallazgos —el puente semántico A22 y el alcance del guard A23— reciben aclaración documental y siguen abiertos en el plano de la demostración. El código compartido de los comparadores sigue siendo código compartido: no se ha convertido en una comparación independiente.

[Registro acumulativo A12](./00L_A12_REGISTRO_MEJORAS_ARTICULO_README_v0.1.md) · [Auditoría histórica A13](./00L_A13_AUDITORIA_TRANSVERSAL_PRUEBAS_v0.1.md) · [Pruebas de corrección](../fixtures/00K-AUDIT-CORRECTIONS/test_audit_corrections.py) · [Resultados y reproducción](../fixtures/00K-AUDIT-CORRECTIONS/README.md).

## 1. Qué cambia y cómo se comprueba

| Observación A13 | Corrección / estado actual | Prueba dirigida |
|---|---|---|
| STAGE-HOOK | Snapshot inmutable de identificadores y fuentes antes de que el adaptador reciba su copia. Se detectan cambio, pérdida, eliminación y duplicación de reportes. El fallo queda en los eventos y en la evaluación. | `test_handoff_checks_pre_adapter_snapshot`; mutación dentro del adaptador en `test_run_preserves_failed_repeats_and_other_candidates` |
| STAGE-METRIC | Se cuentan por separado residual presente, motivo no vacío y scope conservado. Una postura incorrecta no pone artificialmente esos tres campos a cero. | `test_residual_metric_counts_fields_not_overall_pass` |
| STAGE-BURDEN | Ambos costes deben ser enteros no negativos, respetar sus techos y coincidir con los pasos de eventos observados cuando se ejecuta el runner. | `test_burden_rejects_invalid_and_over_limit`; `test_burden_matches_event_count` |
| STAGE-FAILURE-LOSS | Se guardan las doce trazas y el manifiesto antes de devolver fallo; error de ejecución, fallo del candidato y no determinismo quedan diferenciados. Cada repetición y cada candidato reciben una copia propia. | `test_run_preserves_failed_repeats_and_other_candidates`: postura, excepción, no determinismo, mutación y valor no serializable en CTv1 |
| 00L-TYPE | Contrato explícito de tipos, identificadores no vacíos y cantidades no negativas; `"false"`, `0` y `1` no son booleanos. | `test_preflight_rejects_non_boolean`; `test_preflight_rejects_domain_errors` |
| 00L-PEER-DIVERGES | El guard rechaza el identificador vacío; el peer 00G incorpora además los mismos requisitos declarados de scope y procedencia al decidir. | Guard de dominio y `test_a6_peer_scope_and_provenance` |
| 00L-AGREEMENT-GATE | Se puntúa cada brazo contra el resultado esperado después de ejecutar. Se registra también su acuerdo, sin usarlo como oráculo. Una divergencia o dos respuestas incorrectas iguales dejan las doce trazas antes de fallar. | `test_pair_disagreements_scored_against_oracle_and_saved`: ruta, peer y ambos |
| A2-SHORT-STREAM | Fin de evidencia antes del límite se registra como `EVIDENCE_STREAM_ENDED`; `RESOURCE_EXHAUSTED` exige alcanzar capacidad. | `test_a2_exhaustion_requires_capacity` |
| A4-MIXED-ROOTS | Cada acción etiquetada debe estar cubierta por su propia autoridad de campaña; añadir otra raíz no elimina la comprobación. Se corrige tanto Route Q como A2-L. | `test_a4_batch_authority_and_action_time`: lote mixto autorizado/no autorizado |
| A4-ROOT-SCOPE | La referencia de la autoridad debe coincidir con la clave consultada. | Misma prueba: `mismatched_ref` |
| A4-TIME | Hoja y autoridad raíz se comprueban frente al timestamp de la acción; el instante exacto de expiración ya no es vigente. | Misma prueba: expiración de hoja, raíz y frontera exacta |
| A4-RATE-WINDOW | Se comprueban todas las ventanas móviles de una hora, con intervalo semiabierto y entrada ordenada internamente. | `test_rate_limit_sees_later_burst_and_exact_hour_boundary` |
| A6-PEER-SCOPE | El peer exige autoridad para el marco objetivo y procedencia no vacía. | `test_a6_peer_scope_and_provenance` |
| A6-GRAPH-QUALIFICATION | Solo cuentan evidencias firmadas, frescas y con confianza suficiente; grafos ausentes/cíclicos siguen requiriendo recualificación. Este kernel sigue sin modelar autoridad. | `test_graph_peer_does_not_count_unqualified_claims` y regresiones A6 existentes |
| CROSS-P5-MISSING | Campo ausente, nulo, de tipo distinto o conjunto material vacío no acredita vigencia. | `test_p5_missing_unknown_changed_and_valid` |
| CROSS-P2-NEGATIVE-BUDGET | Se rechazan presupuestos negativos/no enteros y streams no booleanos; cero permite cero consultas. | `test_p2_rejects_invalid_budget`; `test_p2_zero_and_valid_budget` |
| TRACE-LABEL-CHECK | Mapa P→escenario fijado y coherencia con el nombre del archivo, además de comprobar su existencia. | `test_traceability_rejects_wrong_scenario` |
| CLOSURE-EMPTY-ATOMS | Contrato versionado de átomos; vaciar, recortar o duplicar el dominio no puede producir cobertura aparente 0/0. | `test_closure_rejects_shrunk_or_duplicated_domain` |
| A22-COHERENCE-BRIDGE | **Abierto.** Se aclara que las 64 firmas pertenecen al modelo simplificado. Falta comprobar su extensión al B1–B11 de A20, incluida derivación del conflicto y grafo de indagación. El argumento de conteo no se retira. | Evidencia de A13 conservada; no se declara una corrección del teorema |
| A23-DISTRIBUTED-SHORTCUT-LIMIT | **Abierto.** El guard opera por cláusula; repartir el objetivo entre cláusulas no es una propiedad que este guard descarte. Ello tampoco demuestra circularidad por sí solo. P1/P2/P4 siguen siendo resultados de proyección; P3/P5/P6 siguen abiertos. | Evidencia de A13 conservada; se precisa el alcance en A23 y su README |

## 2. Evidencia de esta entrega

- **379/379** regresiones existentes (346 core y 33 suplementarias), sin cambiar sus aserciones ni sus cuentas.
- **77/77** comprobaciones adicionales en una batería separada. Con el mismo archivo de pruebas sobre la base anterior: **65 fallos y 12 pases**. Algunos fallos previos constatan la ausencia del nuevo contrato/API de snapshot o trazas; no son 65 defectos independientes ni ensayos de campo.
- **00L:** doce ramas, 128 rechazos de omisión/null y tres fronteras monetarias. El esquema de traza v2 puntúa cada brazo por separado.
- **Stage-0:** doce trazas, seis pares de repetición idénticos y los dos controles de instrumentación. Los fallos se ejercitan mediante inyección en la batería adicional.
- La ejecución local se identifica en [results.json](../fixtures/00K-AUDIT-CORRECTIONS/results.json), con comandos, salidas y hashes de fuentes. No atribuir esos resultados al CI: cada ejecución remota tiene su propio estado.

Las cuentas tienen alcances distintos y no se presentan sumadas como ensayos independientes. No se han ejecutado productos ni ha intervenido un revisor humano independiente.

## 3. Trazas y corrección de interpretación en 00E

Se conservan sin reescribir las [trazas históricas A11](./00L_A11_TRAZAS_EJECUTADAS.jsonl) y el [run histórico Stage-0](../fixtures/RS-00E-Q1a/runs/stage0_v05_4193199/manifest.json). Las referencias nuevas son [A14 JSONL](./00L_A14_TRAZAS_CORREGIDAS.jsonl) y [Stage-0 corregido](../fixtures/RS-00E-Q1a/runs/stage0_audit_corrections_v1/manifest.json). Los workflows comparan ahora contra estas nuevas salidas y preservan los artefactos de fallo.

**La rama negativa 00E de A11 no demostró agotamiento de capacidad:** ofrecía tres evidencias y declaraba capacidad seis. Su salida corregida es `EVIDENCE_STREAM_ENDED`, mientras la ruta acotada devuelve `NO_CONCLUSION`. La diferencia de etiquetas no acredita una ventaja de eficiencia: ese microfixture no mide cuánto trabajo habría seguido realizando un sistema ni si agotaría los seis pasos. Los fixtures A2 que sí llegan a capacidad conservan su resultado `RESOURCE_EXHAUSTED`.

Las fuentes y el oráculo congelados de Stage-0 no cambian. El nuevo run es una **reejecución posterior a la auditoría con instrumentación corregida**, no la ejecución histórica de la prerregistración ni una nueva comparación prospectivamente prerregistrada. El identificador v0.5 se conserva como referencia del diseño de partida, junto con la desviación explícita del harness.

## 4. Límites que permanecen

1. La independencia de implementaciones/comparadores no queda acreditada por estos arreglos. B1/B3 y varios peers comparten lógica o contrato; los resultados son controles de instrumentación y regresión.
2. `campaign_ref=None` sigue significando **independencia estipulada por el fixture de Branch I**. No significa que un sistema real pueda inferir independencia cuando falta metadata. La corrección cubre grupos explícitamente etiquetados, no descubrimiento de campañas ocultas.
3. Burden es conteo de eventos simbólicos; no latencia, tokens o coste real. Tampoco se modela atomicidad de autorización/actuación distribuida.
4. El cierre y los enlaces siguen siendo verificaciones estructurales de un contrato declarado, no pruebas de completitud semántica del mundo.
5. El puente A22, la fidelidad semántica de A23, R2/V11 y las comparaciones de producto requieren trabajo adicional. No se cambian requisitos canónicos ni se declara validación integral.
6. El artículo Word revisado no se modifica en esta entrega; A12 §11 contiene el texto y los enlaces preparados para su actualización quirúrgica. Los adjuntos fiscales/societarios no forman parte de estas correcciones del repositorio.

## 5. Reproducción

Desde la raíz del repositorio:

```bash
python -m pip install pytest
python research/ecosystem-awareness/baseline/fixtures/00K-AUDIT-CORRECTIONS/reproduce.py --output /tmp/audit-corrections-replay
```

Las pruebas históricas de `fixtures/AUDIT-20260926` describen el snapshot auditado; deben ejecutarse sobre ese snapshot para reproducir los fallos originales. No se convierten en tests de aceptación del código corregido.
