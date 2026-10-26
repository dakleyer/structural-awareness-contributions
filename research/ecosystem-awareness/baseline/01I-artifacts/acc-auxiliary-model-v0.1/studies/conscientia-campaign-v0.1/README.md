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
