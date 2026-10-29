# Matriz de cobertura documental y cola de experimentos reales

> **Actualización ejecutable 29-10-2026.** Los ejemplos CE-NOTES/ACC-EXAMPLES se instrumentan ahora en 40 casos sociales con variantes físicas, distributivas, de coordinación, atribución y derechos; 3 mundos nativos PR44 y 30 nativos PR57. Ver [ORIGINAL_EXPERIMENTS.json](ORIGINAL_EXPERIMENTS.json), [NATIVE_EXPERIMENTS.json](NATIVE_EXPERIMENTS.json), [dimension_experiment.py](dimension_experiment.py), [run_original_experiments.py](run_original_experiments.py). Esta matriz histórica se mantiene como línea base; el campo «pendiente» para validación externa sigue vigente y ya no significa que no exista *representación sintética ejecutable* del ejemplo.


**Corte:** 26-10-2026. `SYNTHETIC_RUN` significa que una representación ilustrativa derivada de la **pregunta** de la fuente fue calculada, NO que el paper/documento haya sido replicado. `REPLAY` repite artefactos Python ya existentes en el repo; `BLOCKED` significa que faltan una definición fuente o datos de observación. Ninguna cita de un documento de trabajo acredita validación social.

| Fuente Google Doc / corpus | Motivo original conservado | Caso(s) registrados / código | Estado y requisito adicional |
|---|---|---|---|
| CE-NOTES, notas de *Conscientia Ecosystemica* | IQ-01 eficiencia, reparto y coordinación; plátanos/Cáritas/Viernes; IQ-03 deuda dinámica; 6A HID | `COORD-*`, `CREDIT-*`, `FH_C_competing_ablations`, `network_counterfactuals`, `source_anchored_microexperiments` (IQ-03/plátanos/crédito) | SYNTHETIC_RUN; los números históricos de horas del texto no se reclaman como reproducidos por el modelo nuevo; distinguir utilidad/disconfort subjetivo |
| CE-SOLIDARITY-V3 | Modelo económico, UC21 refutador, requisitos de solidaridad | `SOLID-*`, `uc21_case_templates_not_executed` | SYNTHETIC_RUN+UC21 NOT_RUN; el texto es diálogo, no encíclica validada por el experimento |
| CE-DIALOGUE-V4 | Dependencia sufrida, agencia y solidaridad elegida | `SOLID-*`, `human_and_measurement_blockers` | SYNTHETIC_RUN; no existe cuestionario humano ni consentimiento real en el toy |
| CE-SCHEME | FH-C, FH-E, evidencias de misión y seis escenarios UC21 | `LINEAGE-*`, `FH_C_competing_ablations`, UC21 stage-A fixtures | SYNTHETIC_RUN; un resultado favorable y uno contrario a FH-C están presentes |
| CE-ANTS | Funciones anidadas y analogía hormigas metamórficas | `FRAME-*`, `finite_entropic_experiment`, `PR43/44 replay` | ANALOGY_AND_REPLAY; no se promueve la semántica histórica sobre el 00M canon |
| CE-CAPACITY | Seis casos: trabajo, ecuaciones, autoridad profesional, Francia, oficios, administración digital | `EDUC-*`, `human_and_measurement_blockers` | Educación ilustrada; **otros cinco casos documentados pero pendientes** de variables/fuente/datos; no afirmar resultados poblacionales |
| CE-CORRESPONDENCE | Attribution Gap, HID, Informational Friction, Cost of Clarity y conservación de oficios | `ATTR-*`, `FRAME-*`, `CLARITY-*`, `HID_task_time_synthetic` | SYNTHETIC_RUN; oficios y transmisión cultural aún sólo conceptual |
| CE-SOCIAL-WORK v0.6 | §5 preimagen/Shannon, §6–9 Pareto, sufrimiento y metaelección | 60-fixture, `factorial_joint_mechanism`, `finite_entropic_experiment`, `gap_and_human_limits` | SYNTHETIC_RUN; respetar su clasificación de teorema/hipótesis |
| AG-D01 | Atribución real versus representación; listada-no-dependida y no-listada-dependida | `ATTR-*`, control de oráculo privado | SYNTHETIC_ANALOGY; Claim A necesita trazas profesionales auditadas |
| AG-D02 | Cinco firmas S1–S5; medición con peritos | salida `BLOCKED_FOR_COMPUTATION__SOURCE_EDITION_CONFLICT` | BLOCKED: la función E difiere entre PDF y HTML; no generar índice hasta que el titular rectifique; Stage 0 fiabilidad de medidas pendiente |
| HID-D06 | Agente productivo, bloqueador e integrador; dependencia y crédito | `CREDIT-*`, `COORD-*` | SYNTHETIC_ANALOGY; no inferir egoísmo/estrategia sin medir incentivos y restricción real |
| IF-D10 | Coherencia, supresión más allá de costes y cambio de frame | `FRAME-*`, `LINEAGE-*`, FH-C ablations | SYNTHETIC_ANALOGY; supresión real y efectos longitudinales NO_OBSERVED |
| CC-D17 | Captura-recaptura, coste de exploración, conocer que una decisión no existe | `CLARITY-*`, `cost_clarity_capture_recapture` | Costes de los brazos son hipótesis; estimación de sistemas no vistos BLOQUEADA sin muestreo y supuestos |
| HID-D20 | Trabajo humano compensatorio, medición por roles y retroalimentación | `HID_task_time_synthetic` | SYNTHETIC_ONLY; sin fuentes humanas longitudinales, sin resultado 01K externo |
| ENT-DIST y ENT-AUDIT | Cobertura de preimágenes, KL, riesgo de inferencias físicas | `finite_entropic_experiment` | FINITE_MATH: Shannon sólo con población definida, orientación KL correcta, no Landauer universal |
| CE-MH-NOTE | Bien común, derechos, UC21/S4 y reflexión | `RIGHTS-*`, `SOLID-*`, UC21 S4 fixture | Analogía; no declaración atribuible oficialmente al Vaticano por este experimento |
| CE-MH-ONEPAGER y CE-PRESCIENCE | Archivos y antecedente de conciencia mínima | fuente por METADATOS; no caso nuevo atribuido | **TEXT_SCREENED_CONCEPTUAL**: recuperados ambos textos y cribados temas y secciones; copia histórica y antecedente de awareness suficiente, sin nueva observación ni replicación |
| 00M y 01K | Semántica B/C/D y medidas humanas propiamente dichas | `finite_entropic_experiment`, bloqueadores humanos, PR47 bridge | Definición y límites en vigor; NO se reescribieron canónicos |
| UC21 S1–S6 | 37 gates fuente, R0/R1/R2 y falsadores | `uc21_case_templates_not_executed` + `UC21_adapter_replay` | **Seis tests nativos NOT_RUN**; se ejecuta únicamente fixture S4 sintético; ningún defensor real aceptado |
| ACC-EXAMPLES | Plátanos, DANA, naranjas, crédito, manzanas, liceo y X−200 | EX-IDs estables en cada familia, cuatro replays de #42–#45 | Historias ilustrativas conservadas, no hechos observados ni pruebas sociológicas |

## Próxima ola por prioridad y dependencia instrumental

**P0 — listo para diseño de ejecución externa (no desplegado):** versiones compatibles READY/v1/v2 con proveedor de datos de prueba; capacidad de coordinación y oráculo de factibilidad independiente; delimitación de autorización UC21/S4 y S5; costes CPU y mantenimiento de Q versus consulta convencional. Se requieren cuentas/testbed, autorización y versiones selladas.

**P1 — medición humana autorizada:** ACW/GIC/NEO/UNKNOWN por episodios con codificadores independientes; autonomía/competencia y eudaimonía con escalas validas; accesibilidad educativa y oficios bajo preferencias de la persona. No solicitar datos reales a menores o poblaciones vulnerables sin protocolo ético.

**P2 — identificación difícil:** captura-recaptura del universo no visto; causalidad de burocracia/credit-gaps; efectos de comunicación pública Q sobre equilibrios; hipótesis de feedback/segundo orden sobre n dimensiones; validación de semánticas físicas de primitivas entrópicas fuera de modelos finitos. Algunos problemas no son evaluables sin nuevos instrumentos, y el plan conserva UNKNOWN.
