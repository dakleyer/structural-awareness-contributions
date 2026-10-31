# Conscientia Ecosystemica × ACC — campaña experimental de referencia (v0.1)

**Estatus: EJECUTADA EN MODELOS SINTÉTICOS; VALIDACIÓN SOCIAL, EMPRESARIAL, PSICOLÓGICA Y UC21 STAGE C NO EJECUTADA.** Investigación auxiliar apilada sobre PR #47, que depende de #45→#44→#43→#42. Este paquete **no sustituye** las definiciones 00M, 00N, 01K ni los oráculos/gates fuente UC21 o la metodología DDS. La CI prueba ejecución reproducible y límites explícitos, no superioridad de Ecosystem Awareness ni recepción institucional.

## 1. Objetivo y fuentes realmente utilizadas

Convierte varios Google Docs de Conscientia Ecosystemica, el trabajo de composición social y los dosieres de Attribution Gap, Informational Friction, Cost of Clarity y Human Intelligence Debt en una campaña homogénea con **identidad de cada documento, pregunta, hipótesis, variante adversa, estado del ensayo y resultados**. [SOURCE_REGISTER.json](SOURCE_REGISTER.json) identifica **23 fuentes** (19 referencias de Google Docs y cuatro entradas del corpus Github). De los 19 Docs, se inspeccionó texto de **17**; las dos entradas históricas CE-MH-ONEPAGER y CE-PRESCIENCE están catalogadas por título, **no** se atribuye una extracción completa. Son fuentes de conceptos/hipótesis, no experimentos observados. Las referencias siguen siendo **documentos vivos**: para una auditoría externa a largo plazo habrá que custodiar una exportación consentida, fechada e íntegra de sus ediciones; no se supone que el enlace actual sea una edición inmutable.

[CASE_REGISTRY.json](CASE_REGISTRY.json) congela el objeto sintético: **12 familias × cinco variantes = 60 escenarios**; cada una tiene origen y ejemplo establecido por [EXAMPLE_LEDGER PR #42](../bounded-traps-v0.1/EXAMPLE_LEDGER.md). Los originales no se sustituyen ni se presentan como eventos observados. [SOURCE_COVERAGE_AND_BACKLOG.md](SOURCE_COVERAGE_AND_BACKLOG.md) fija qué caso sí está modelado y cuáles sólo son propuestas de futura instrumentación.

## 2. Qué se ha ejecutado

| Componente | Ejecución / límite |
|---|---|
| Matriz de decisiones | **60 casos × 5 brazos = 300 acciones sintéticas**: A-only, Q ingenua, Q con auditoría independiente simulada, inspección dirigida convencional fuerte y ampliación A cuando está declarada disponible. Escenarios con B válida, bloqueo, obsolescencia, Q falsa o C/D no evaluable. |
| FH-C causal | **8 combinaciones**: Q de fronteras sí/no × hechos adicionales sí/no × dos perfiles adversos; se incluyen tanto apoyo como contradicción de FH-C. No es identificación causal real. |
| Composición física / awareness | **8 combinaciones 2×2×2**: Q × transición conjunta × necesidad de fundamento; Q sola no produce recursos. |
| Brecha relativa | **8 situaciones**: cuatro tamaños n con red densa o estrella; el óptimo conjunto contrafactual está supuesto. No equivale a HID medido. |
| Entropía y preimagen | Dos mundos finitos explícitos, Shannon condicional, y contraejemplo de KL en la orientación original errónea. Ninguna entropía atribuida al exterior abierto D. |
| Capacidades humanas, atribución, Cost of Clarity | Una brecha personal estructural sintética sin dolor medido; roles ACW/GIC/NEO/UNKNOWN **no observados**; cálculo D02 bloqueado por discrepancia de ediciones; capture–recapture sin muestreo queda no identificado. |
| Reproducción de PR #42–#45 | Cuatro scripts originales del repositorio se ejecutan **de nuevo** en CI y se comparan con sus propios JSON de referencia. No son cuatro verificaciones empíricas independientes. |
| UC21 fuente | Se regenera el adaptador ya existente con su fixture **sintético** S4 R0/R1/R2 y se comprueba que sigue diciendo que HR NO está probado/refutado. Se listan S1–S6 y sus 37 gates como casos reales **aún sin ejecución nativa**. |

Los resultados detallados de la matriz, con verdad de laboratorio y decisiones por brazo separadas, están en [REFERENCE_SYNTHETIC_RESULTS.json](REFERENCE_SYNTHETIC_RESULTS.json). Se dispone de [RUN_SUMMARY.md](RUN_SUMMARY.md) como lectura rápida del corte sintético local; el registro íntegro que reejecuta las cuatro ramas existentes y UC21 se publica como **artefacto descargable de GitHub Actions** al completar la CI, no como una ejecución real de una empresa o producto.

## 3. Resultados numéricos que pueden citarse sin exagerar

Sobre **48 casos con respuesta sintética adjudicable** (12 casos adicionales C/D abiertos NO adjudicables), las decisiones correctas de los cinco brazos fueron **12 / 24 / 24 / 48 / 36** respectivamente. La Q ingenua comete **12 errores** por certificados falsos autodeclarados. La Q con auditoría simulada reduce los errores a **4**, aunque no garantiza descubrir todos los falsos; el peer dirigido convencional del fixture acierta los 48 porque recibe un instrumento **supuesto exacto** a su coste declarado. Estas tasas no estiman precisión real de ninguna tecnología.

Los valores netos sintéticos de la función de utilidad escogida fueron, respectivamente, **+12, −52,8, +28,8, +200,4 y −262** unidades *inventadas*. Las 60 variantes fueron construidas deliberadamente, no sorteadas de una población representativa; los costes del peer y Q son supuestos. **Por ello no se deben ordenar tecnologías reales con estos totales.** Lo que importa es que el instrumento admite ganancia, daño, empate, abstención y victoria convencional sin cambiar el oráculo.

El caso factorial ofrece una prueba de interacción: con necesidad de prueba, sólo la combinación Q válida **y** cambio conjunto legítimo entrega +2 unidades; ninguna de las dos por sí sola supera el bloqueo. Si la prueba no es necesaria, la coordinación conjunta puede lograrlo sin Q. El experimento enseña cómo separar el valor informacional del valor físico de cambiar la arquitectura.

## 4. Reproducción local y CI

Desde el directorio del estudio, tras obtener **la rama completa** que contiene los cuatro estudios previos:

```bash
python3 -B -m unittest discover -s . -p 'test_campaign.py' -v
python3 -B verify_campaign.py /tmp/conscientia_full_execution.json
```

El segundo comando vuelve a ejecutar las cuatro realizaciones existentes y el adaptador UC21 del corpus, contrasta su resultado con los JSON de referencia conservados en cada estudio y compara los experimentos nuevos con nuestro JSON fijado. `campaign.py --local` sólo ejecuta la matriz local y marca las reproducciones previas como no realizadas: nunca llamar «replay validado» a esa modalidad. [bootstrap.py](bootstrap.py) regenera únicamente fixtures de ensayo **sintéticos** (no reescribe Docs ni obtiene evidencia de personas).

La CI aprovecha el único [workflow de integridad documental](https://github.com/dakleyer/structural-awareness-contributions/blob/main/.github/workflows/document-integrity.yml), ejecuta los tests y deposita un artefacto con resultados íntegros. No crea un método DDS paralelo ni modifica UC21. Para revisión independiente véanse [PROTOCOL_AND_EVIDENCE_LEVELS.md](PROTOCOL_AND_EVIDENCE_LEVELS.md) y [SOURCE_COVERAGE_AND_BACKLOG.md](SOURCE_COVERAGE_AND_BACKLOG.md).

## 5. Necesario antes de una afirmación tecnológica/social

1. Congelar la pregunta, población, recursos, permisos y criterio **antes** de ejecutar la campaña real, incluso si los fixtures de este laboratorio ya fueron vistos al diseñar la batería (no es preregistro prospectivo independiente).
2. Reemplazar verdad interna de laboratorio por pruebas de fuente nativa y observador externo; verificar que el peer realmente está disponible, sus permisos, costes y efectos; dar crédito completo a la tecnología convencional competente.
3. Mantener los contratos **FH-C** (ablación causal de conciencia de límites frente a hechos de dominio), **FH-E** (menor coste computacional a misma corrección), **UC21 R0/R1/R2**, y la medida humana **01K** como resultados separados.
4. Para solidaridad o sufrimiento, estudiar personas sólo mediante protocolo ético y medidas de oportunidad/agencia/bienestar independientes; la ecuación de brecha de desarrollo NO es una encuesta psicológica.
5. No calcular índice D02 con una ecuación inconsistente entre ediciones ni extrapolar frecuencias Shannon/capture–recapture a C/D abiertos.

**Novedad atribuible:** un paquete de pruebas **interoperable y trazable** de composición socioeconómica + cualificación epistémica + derechos y resultados humanos separados, con falsadores y comparadores fuertes. Las ideas de juegos de coordinación, Blackwell, Shannon e interpretación abstracta tienen prior art; esta batería no demuestra una primicia matemática.

## Confirmación de la ejecución integrada en GitHub CI

**Corte verificado tras el commit experimental, sin sustituir las mediciones locales anteriores:** la [ejecución 40350676384](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/40350676384) concluyó SUCCESS. Se verificaron **49 pruebas nuevas**, cuatro replays de módulos sintéticos PR #42–#45 frente a sus resultados de referencia y un único adaptador UC21/S4 **SINTÉTICO**, sin prueba nativa de productos. La salida de `verify_campaign.py` declara `passed=true`, `scenario_cases=60`, `arm_decisions=300`, `prior_studies_replayed=4`, `UC21_synthetic_only=true`.

La ejecución publicó el artifact `conscientia-acc-synthetic-results` (ID 12664160091) con JSON y Markdown de resultados regenerados; es un entregable temporal de Actions, no una observación independiente. Los datos fuente/casos/resultados fijados y los programas permanecen en el repositorio para reproducirlos después del vencimiento del artifact.

**Índice en Google Docs (nuevo, sin cambios a las fuentes originales):** https://docs.google.com/document/d/17ud6Jce6b-Dy2mnV3GSXiqfrhsMMe09xAJzLztNknUc/edit


## Extensión documental con doce microensayos reproducibles (PR #49)

La ampliación [PR #49](https://github.com/dakleyer/structural-awareness-contributions/pull/49) conserva **todo el trabajo ya fusionado** y añade doce verificaciones fuente-ancladas a los ejemplos originales: el plátano en tres estados con conservación de unidades y consentimiento, crédito 7+4/7+3, manzanas y frutería con utilidad no monótona, eficiencia del documento IQ-03, procedencia duplicada, XOR finito, naranjas sin colusión demostrada, educación, ministerios, oficios y alumno de liceo como viñeta. El runner guarda los resultados en `source_anchored_microexperiments`, comparables con el JSON de referencia, **sin convertir ilustraciones en evidencia social observada**.

Las 61 pruebas abarcan los 49 controles previos y doce casos adicionales. Los resultados anteriores y el artefacto CI ya verificado se preservan; los valores económicos/psicológicos de esos nuevos ejemplos siguen siendo sintéticos o NO ESTABLECIDOS. El instrumento D02 Attribution Gap permanece bloqueado por discrepancia de fórmula entre versiones y las métricas humanas necesitan fuente independiente. No existe un segundo protocolo DDS ni un oráculo UC21 reescrito.


## 29-10-2026 — Laboratorio ejecutable de ejemplos originales (extensión aditiva)

**Contrato:** la pregunta, el horizonte, el operador físico, la distribución por actor, las dimensiones declaradas —incluidas las implícitas—, los eventos que las activan y las restricciones de factibilidad/consentimiento/autoridad forman un caso. El motor produce la evaluación física, los estados dimensionales, la admisibilidad y la traza de evidencia. Nunca suma utilidades individuales ni convierte A/B/C/D en una probabilidad inventada. La frustración F, el beneficio B y el bienestar hipotético W se conservan separados por participante; HID y sufrimiento vivido no son equivalentes al resultado sintético.

### Archivos y ejecución

- [ORIGINAL_EXPERIMENTS.json](ORIGINAL_EXPERIMENTS.json): **40 casos ilustrativos sintéticos con operadores finitos**, basadas en el libro de ejemplos y párrafos del corpus, con variaciones materiales y negativas; datos de escenario etiquetados como sintéticos.
- [dimension_experiment.py](dimension_experiment.py): operadores de flujo conservativo, capacidad, reparto, distancia física, elección no monótona, transmisión de oficio, eficiencia por servicio, procedencia e información discreta calculada desde filas. Interfaz pública de planificación sin entradas privadas, evaluación de restricciones sobre resultados computados, dimensiones explícitas/latentes/abiertas, SHA-256 por caso y registro de operadores externos.
- [NATIVE_EXPERIMENTS.json](NATIVE_EXPERIMENTS.json): tres mundos del modelo social original PR #44 y las **30** fichas nativas del modelo agéntico PR #57.
- [native_experiment_adapters.py](native_experiment_adapters.py): dos operadores que **invocan el código fuente sin alterar** de `intrinsic_abcd.py` y `agentic_reduction.py`. La planificación pública y el oráculo privado permanecen en fases distintas. Resultados etiquetados y agrupados por modelo, nunca sumados entre ellos.
- [run_original_experiments.py](run_original_experiments.py) y [test_dimension_experiment.py](test_dimension_experiment.py): ejecución determinista y pruebas de aceptación de la semántica original; CI publica `acc-original-examples-execution`.

```bash
python -B studies/conscientia-campaign-v0.1/run_original_experiments.py --model both --compact
```

Usar la ruta relativa apropiada si se ejecuta desde otro directorio. `--model social` reproduce 40 variantes documentadas; `--model native-social` ejecuta los tres escenarios PR44; `--model agentic` ejecuta las 30 fuentes PR57; `--model both` ejecuta **73** casos sin composición de objetivos.

| Caso original | Qué se ejecuta de verdad | Control de integridad |
|---|---|---|
| Dos plátanos S0/S1/S2 | Producción 0/2/2, conservación, asignación, desperdicio, B1=5, F1=7, W1=-2 | S2 sin ruta/consentimiento queda indeterminado; ruta denegada bloquea; intento de crear un tercer plátano resulta materialmente imposible |
| Plátano lejano y uso local | Distancia por unidad antes/después | El ahorro físico no se transforma sin evidencia en emisiones o euros; título, seguridad y contratos tienen su propia puerta |
| Cáritas/DANA | Un donante puede recibir beneficio sintético directo positivo y aun así rechazar un esquema de atribución | Atribución y consentimiento son condiciones distintas de logística; no se imputa comportamiento real a Cáritas |
| Viernes y Robinson; crédito | 1/999 para dos recursos, veto de reparto relativo; 7+4/7+3 contra capacidad 10 | El veto no borra la ganancia material; demanda 11 no cabe en 10 |
| Manzanas | Pico local 3, máximo discreto 8, transición no monótona | Que exista un máximo no demuestra que el puente sea autorizable |
| IQ03 y 700→2 ministerios | Equivalencia de servicio antes de calcular brecha de recursos | Si falla equivalencia, no se certifica eficiencia; derechos, continuidad y trabajadores permanecen verificables |
| Naranjas, educación, oficio, liceo | Conocimiento parcial, casos de capacidad sintéticos, transmisión mentor-aprendiz | Un objeto conservado no basta para transmitir una destreza; el bienestar humano no se deduce del álgebra |
| Modelo nativo PR44 y agéntico PR57 | Fuente nativa: A actual, Q/B, capacidades ocultas solo para el referee, seis brazos y condiciones de meta-protocolo | Dos mundos con la misma A pública dan resultados privados distintos; C/D no se cierran |

El registro histórico `CASE_REGISTRY.json` (60 casos) y `REFERENCE_SYNTHETIC_RESULTS.json` no se reescriben. El informe previo `campaign.py` sí deriva ahora los plátanos, IQ03 y los bits de información del motor/filas del propio experimento; debe seguir dando exactamente la misma salida de referencia. No cambian los 00M/00N/01K ni el objeto teórico ni los métodos de los dos modelos nativos.

### Extensibilidad

Para un nuevo dominio, aportar un caso con pregunta y horizonte acotados, unidades, fuente, dimensiones iniciales y eventos; registrar un operador que acepte entradas declaradas y devuelva `PhysicalOutcome(status,observations,issues)`. Los controles se aplican al resultado, no a un veredicto preescrito. Para un nuevo modelo nativo, escribir un adaptador análogo que exponga su salida conservando la separación información pública/oráculo privado; no mezclar magnitudes heterogéneas bajo un único ranking.

**Estatus de prueba:** ejecución en un laboratorio finito, con rutas hipotéticas declaradas, controles negativos y procedencia. La admisibilidad condicional de un escenario no se convierte en consentimiento, seguridad o acuerdo histórico verificados.


### L-07 — condiciones declaradas frente a restricciones calculadas (29-10-2026)

Una **representación ejecutable** no convierte automáticamente un consentimiento declarado en evidencia empírica. Por ello se modifica la descripción de «40 pruebas sociales» a **40 casos ilustrativos sintéticos**, y se añade al ejecutor `run_original_experiments.py` el registro `social_constraint_evidence_origin`, sin modificar ni los operadores ni las decisiones.

En los 40 casos de este corte hay **100 comprobaciones:** **74 condiciones declaradas** por el escenario (admisión, derechos, consentimiento, autoridad, coordinación, etc.) y **26 condiciones comprobadas mediante resultados físicos calculados**. Bajo las hipótesis del toy, **18 casos son elegibles** y **22 no son elegibles o siguen indeterminados**. Estas cifras son del fixture, no tasas de la realidad.

Para cada caso se muestran por separado:

- `physical_status` y el resultado de `admission`;
- cada condición bloqueante o desconocida con su **origen: declaración / prueba sobre efecto calculado**;
- `primary_basis`: una agrupación explicativa determinista para facilitar auditoría, con precedencia documentada (imposibilidad física, fallo calculado, fallo declarado, indeterminación declarada, ausencia de evidencia material). **No es una imputación causal al mundo real**. Si concurren varias barreras, todas continúan en `unresolved_or_failed_conditions`.

Así, el exceso 7+4 sobre capacidad10 es una **imposibilidad física calculada**; el rechazo hipotético de atribución en Cáritas/DANA es un **condicionante declarado**. Ningún motor deduce consentimiento, autoridad o la felicidad humana de cantidades materiales. Los tres tests añadidos verifican desglose, origen y conservación de la misma clasificación cuando también se ejecutan los 30 casos agénticos, sin acceder a la verdad privada de sus planificadores.

Hallazgo origen: [auditoría #58, L-07](https://github.com/dakleyer/structural-awareness-contributions/pull/58). Estado: respuesta técnica propuesta para validación independiente; no se declara cerrado antes de la adjudicación.

## G-02 — Audit evidence rather than a declared Boolean (31 October 2026)

[Source-anchored protocol and observed results](G02_AUDIT_OBSERVATION_PROTOCOL.md) · [independent audit and conventional instrument simulator](g02_evidence_audit.py) · [versioned parameter regimes](G02_AUDIT_PROTOCOL.json) · [25 adversarial tests](test_g02_evidence_audit.py).

The original 60 cases and five campaign strategies remain **unchanged**. In their historical test, `Q.independent_audit` is a declaration, **not an audit observation**; its four wrong decisions in false-Q fixtures should not be presented as audited detection quality. This separate laboratory generates an actual synthetic, noisy **SUPPORT/CONTRADICTION/INCONCLUSIVE** observation from a purported independent instrument, with declared sensitivity/false alarms, provenance, scope, freshness, availability and cost. A conventional instrument generates its own (possibly incorrect) independent observation of the same question; it never receives a hand-written perfect verdict by default.

Eight scenarios over 60 original cases × 64 paired replicates (**30,720 synthetic observations**) demonstrate both sides: a perfect audit avoids wrong final decisions but may leave genuine decisions unresolved; blind/weak audits fail, and the measured conventional method can win. Public planners do not receive private truth, the original source's false-Q status, or the historical Boolean. Open C/D never gets a fabricated adjudication. This is **not** a claim about actual auditor performance, real-world frequencies, institutional adoption or causal FH-C validity. [CI and artifact](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/41184352284) are reproducible; source/canonical models are not modified.
