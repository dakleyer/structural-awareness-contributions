# A13 — Auditoría transversal de las pruebas y sus conclusiones

**26 de septiembre de 2026, Europe/Madrid. Estado: hallazgos reproducidos; correcciones de implementación pendientes.**

**Corpus auditado:** `8f17843c568114f31cc0ad486b4a1303396021e6`. **Artículo recibido:** `When_the_Controls_Work_but_the_System_Fails_revisado.docx`, SHA-256 `9628884ea0e5117478a734aaca156e8bb02e56a56dd86d3bc018e6a0b4bddf73`, 183 párrafos. Se conserva sin modificación. [Pasajes revisados](../fixtures/AUDIT-20260926/article_review.json). [Registro acumulativo A12](./00L_A12_REGISTRO_MEJORAS_ARTICULO_README_v0.1.md).

## 1. Dictamen

**Hay problemas adicionales al comparador compartido y a la circularidad de A23 ya detectada.** Se reproducen las regresiones originales y, al mismo tiempo, contraejemplos que esas regresiones no cubren. Un resultado verde acredita el comportamiento programado en las entradas probadas; no acredita por sí solo la fidelidad del modelo, la independencia del comparador ni la suficiencia de la instrumentación.

La conclusión anterior de que el «peer fuerte empata» fue presentada con más valor comparativo del que permite el código. El artículo revisado recibido ya corrige buena parte de esa interpretación. Este informe confirma la corrección y añade defectos de instrumentación, oráculos, cobertura y correspondencia entre demostración y código.

**Se mantienen:** los resultados numéricos de las regresiones sobre sus fixtures; los hashes reproducibles de las trazas; la separación parcial P1/P2/P4 frente a P3/P5/P6 en el modelo A23 actual; y el argumento de que 64 estados diagnósticos distintos requieren seis bits. **No quedan certificados por ello:** una comparación independiente EA/no-EA, la corrección de toda Route Q ante otras entradas, las restricciones completas de coherencia de A20 en el certificado A22, ni los escenarios completos o productos.

## 2. Qué se comprobó realmente

Se inventariaron los 65 archivos Python del baseline anteriores a esta auditoría; se revisaron las implementaciones de las familias de pruebas, sus controles, mecanismos de evaluación, workflows y afirmaciones vinculadas. Se ejecutaron todas las suites sueltas encontradas en esas familias, además del ZIP histórico A4. Se contrastaron los modelos formales con sus descripciones y el artículo recibido. El inventario no equivale a una certificación semántica de cada frase del corpus.

| Paquete | Reproducción local | Interpretación correcta |
|---|---:|---|
| A1/P1/00J | 42 tests | Proposición de evidencia y reparaciones simbólicas. |
| A2/P2/00E | 58 tests | Presupuesto y búsqueda acotados; véase el defecto de etiqueta de agotamiento. |
| A3/P3/00F | 49 tests | Conflicto, cierre y controles uniformes en las entradas declaradas. |
| A4/P4/00H | 76 tests | U/G/I/NM y controles; no cubren la mezcla de campañas encontrada aquí. |
| A5/P5/00I | 47 tests | Comparación de cuatro campos materiales declarados; no descubre nuevas dependencias. |
| A6/P6/00G | 74 tests | Dependencia y reparaciones; algunos peers omiten otras comprobaciones. |
| A6a, A6b y núcleos cruzados | 10 + 11 + 12 | Falsador del par antiguo, composición 00F y funciones reutilizables. |
| Campaña vigente anterior | **346 + 33 = 379** | Recuento de regresiones, no ensayos independientes. |
| Históricos A1/A2/A3 | 11 + 11 + 10 | Se conservan como historia; no se suman a los 379 como evidencia nueva. |
| ZIP A4 v0.2 | 21 | SHA-256 histórico intacto; ejecución tras extraerlo. |
| P5 blind-signature | 18 | Paquete separado de los 379; no invocado por el workflow 00K revisado. |
| Full-cube A22 | 68 | 64 firmas del modelo implementado y cuatro comprobaciones auxiliares. |
| A23 | 11 | Incluyen reproducir los contraejemplos esperados; no cierran los seis principios. |
| CTv1 | 8 | Serialización; no prueban el funcionamiento del detector durante el handoff. |
| 00L | 12 ramas, 128 mutaciones missing/null, tres fronteras | Replay idéntico en bytes; el guard es de presencia/nulidad, no de tipos ni semántica. |
| Stage 0 | Dos controles, 12 trazas, seis pares de repeticiones idénticas | Reproducción determinista de adaptadores compartidos. |
| Manifiesto, certificado de seis testigos, trazabilidad, cierre y extensibilidad | PASS | Alcances distintos; los tres últimos son principalmente validadores estructurales. |
| Integridad documental | 3.195 rutas, ocho secciones, tres decks | En el corpus auditado, antes de añadir este informe. |

Entorno local: Python 3.12.14 y pytest 9.1.1. El primer intento carecía de pytest; se instaló desde la caché y se repitieron las suites. No se atribuye esta reproducción al entorno histórico CI 3.13. El directorio del ZIP produjo inicialmente «no tests ran» por contener un archivo comprimido, no tests sueltos; la extracción posterior obtuvo 21/21. Se deja constancia de ambas operaciones.

[Resultados y hashes de fuentes](../fixtures/AUDIT-20260926/baseline_results.json) · [salidas de ejecución](../fixtures/AUDIT-20260926/execution_logs.txt) · [20 observaciones adversas reproducidas](../fixtures/AUDIT-20260926/probe_results.json) · [código de las pruebas adversas](../fixtures/AUDIT-20260926/probe_findings.py).

## 3. Hallazgos prioritarios

### H01 — El empate está incorporado al diseño de varios comparadores

**Confirmado; afecta a la interpretación comparativa, no al hecho de que los archivos se reproduzcan.**

En [Stage 0](../fixtures/RS-00E-Q1a/stage0_runner.py), B1 y B3 llaman a `_roots` y `_assessment`. Con dos informes, `roots[0] == roots[1]` y `len(set(roots)) == 1` son equivalentes. El coste procede de una fórmula común. La igualdad es esperable por construcción y no mide dos arquitecturas independientes.

| Par 00L | Relación efectiva entre las implementaciones |
|---|---|
| 00E | `strong_peer_budgeted_search` llama directamente a Route Q. |
| 00F | Route Q y el peer usan los mismos `local_checks_pass` e `incompatible_pairs`. |
| 00G | Comparten la calificación local y el conteo de raíces; el peer omite controles de ámbito e integridad que sí están en Route Q. |
| 00H | Comparten materialidad, detección de composición y validación de hojas; duplican la comprobación de raíz. Comparten también el fallo H05. |
| 00I | Repiten la misma comparación sobre la misma base de cuatro campos, con validación compartida. |
| 00J | Una tabla de política y la comparación de proposición expresan el mismo contrato sintético; no hay implementación externa ni defensor independiente. |

Además, [00L `verify`](./verify_paired_symbolic.py) contiene `assert strong_peer == route`. Es razonable como prueba de equivalencia de una reconstrucción declarada, pero **no sirve como criterio de éxito de un experimento destinado a poder descubrir diferencias**. Una divergencia aborta antes de escribir el JSONL final. Observaciones `00L-AGREEMENT-GATE` y `00L-PEER-DIVERGES`.

**Corrección necesaria:** conservar este replay como regresión de controles; en una comparación nueva, puntuar cada candidato contra el oráculo, permitir desacuerdo y conservar ambos resultados. No afirmar superioridad ni equivalencia arquitectónica a partir del empate actual.

### H02 — El detector de pérdida no contrasta el handoff contra una referencia independiente

**Defecto de instrumentación confirmado; prioridad alta.** En `play_events` se invoca:

```python
detect_qualifier_loss(report, report["upstream_source_id"], True)
```

Para un diccionario ordinario con ese campo, se compara el valor consigo mismo. El self-test separado sí compara contra `P`, pero no demuestra que el handoff real conserve el valor anterior.

La prueba `STAGE-HOOK` cambia `P` por `CORRUPTED` después de obtener la evaluación del adaptador y antes de reproducir los eventos. Los dos self-tests mantienen PASS/FAIL; ningún evento detecta pérdida y `score` devuelve PASS. Esto muestra una discrepancia entre el resultado evaluado y los eventos publicados. No afirma que las trazas congeladas contengan esa corrupción.

**Corrección necesaria:** instantánea inmutable de lo emitido, comparación con lo recibido y mutaciones introducidas en ese mismo trayecto. Debe fallar también al eliminar, sustituir o alterar el campo durante el handoff, no solo en un diccionario aislado. Hasta entonces, el PASS existente es un self-test local, no evidencia de conservación de extremo a extremo.

### H03 — Un fallo del candidato impide guardar su propia traza

**Defecto confirmado.** Stage 0 lanza `RuntimeError` al obtener `candidate_status != PASS`, antes de serializar la traza. Al cambiar únicamente B1 a la postura no permitida `HOLD`, la ejecución conserva solo los dos archivos Step-0 y ninguna traza del fallo: `STAGE-FAILURE-LOSS`.

Esto contradice el propósito de registrar hallazgos negativos de la preinscripción y hace incompleto el registro de una ejecución fallida. No demuestra que se hayan ocultado fallos históricos: muestra que el mecanismo actual no los preservaría.

**Corrección necesaria:** escribir primero la observación, resultado, evaluación y motivo de fallo; separar fallo del candidato de fallo del harness y completar el resumen conforme a la regla preinscrita.

### H04 — Dos medidas de Stage 0 no validan lo que sus nombres sugieren

**Defectos del evaluador confirmados.**

- `required_residual_scope_fields_retained` vale tres si toda la evaluación es correcta y cero en otro caso. Cambiar solo la postura a `HOLD`, conservando residual y scope, produce **0/3**: mide éxito global, no campos conservados. Prueba `STAGE-METRIC`.
- `score` acepta `processing_steps=999` y `modelled_time_steps=-1`, porque solo comprueba un límite superior del segundo. Prueba `STAGE-BURDEN`. Los adaptadores congelados no generan estos valores, pero la evaluación no es robusta frente a resultados defectuosos.

**Corrección necesaria:** contar cada campo e interpretabilidad por separado; validar tipos, no negatividad y límites de ambas medidas; contrastar el coste con los eventos. Mantener «coste modelado», sin presentarlo como tiempo o esfuerzo medido de una arquitectura real.

### H05 — 00H confunde «no hay una única raíz» con «los casos son independientes»

**Contraejemplo de comportamiento confirmado; prioridad alta para reutilización o ampliación.** En [A4](../fixtures/00K-A4-P4-00H/ablation_A4.py), `detect_composition_P6` devuelve `None` tanto para casos sin raíz como para una mezcla de raíces. Route Q interpreta ambos como Branch I y permite ejecutar con hojas válidas.

Prueba `A4-MIXED-ROOTS`: dos acciones de campaña `X`, sin autorización de raíz, reciben `DBC_REPOSITION_RECONTRACT`. Añadir una acción de `Y`, sin añadir autoridad alguna, cambia el resultado a **`DBC_EXECUTE` para el conjunto**. El peer A2-L comete el mismo error. La mezcla queda fuera de la cuadrícula U/G/I congelada, pero usa los tipos y entradas que acepta la función; invalida extrapolar su suficiencia a campañas mezcladas.

Otros límites reproducidos del mismo módulo:

| Observación | Resultado | Alcance |
|---|---|---|
| `A4-ROOT-SCOPE` | La clave `X` contiene un objeto de campaña `OTHER` y pasa. | La coherencia del registro se presupone; no se comprueba. |
| `A4-TIME` | Grants que expiran en `NOW+1s` permiten acciones fechadas en `NOW+2s`. | Route Q usa el `NOW` fijo; el helper con tiempo explícito sí rechaza. No prueba revalidación por acción. |
| `A4-RATE-WINDOW` | Una acción en la primera hora y once dos horas después pasan un límite de diez. | El supuesto control «por hora» solo examina la primera ventana; no todas las ventanas. |

**Corrección necesaria:** distinguir ausencia de evidencia de composición, independencia demostrada y composición por varias raíces; validar cada grupo sin permitir que otro oculte su obligación. Hacer explícito el tiempo de evaluación y el contrato de integridad del registro; corregir o renombrar el limitador de tasa. Preservar los históricos y repetir los controles positivos.

### H06 — La rama negativa publicada de 00E etiqueta agotamiento sin consumir la capacidad declarada

**Problema presente en el microfixture 00L vigente.** El replay construye tres pasos de evidencia y declara capacidad/horizonte seis. La rama negativa de `ablated_search_until_capacity` termina el iterable y devuelve `RESOURCE_EXHAUSTED`, aunque solo ha recibido tres pasos. Prueba `A2-SHORT-STREAM`.

Esto no refuta la necesidad de acotar búsqueda. Sí impide usar esa etiqueta como evidencia observada de consumo de toda la capacidad en ese replay. El efecto depende de una decisión del modelo al agotarse el iterable.

**Corrección necesaria:** registrar pasos consumidos y diferenciar fin de evidencia, no conclusión y capacidad agotada; o representar explícitamente los pasos restantes y su coste. No cambiar la interpretación a posteriori para mantener el resultado esperado.

## 4. Más huecos de cobertura y supuestos

| ID de prueba | Hallazgo reproducido | Clasificación y corrección necesaria |
|---|---|---|
| `00L-TYPE` | El texto `"false"` pasa el guard y se interpreta como verdadero: Route Q ejecuta en 00E. | El dato congelado es booleano correcto. Las 128 mutaciones no acreditan tipos, rangos ni semántica. Validar esquema o declarar y hacer cumplir la frontera. |
| `00L-PEER-DIVERGES` | Raíz vacía: Route Q 00G requalifica; el peer transiciona. | Preflight admite cadena vacía. La igualdad solo se comprobó en el par limpio. |
| `A6-PEER-SCOPE` | Con autoridad dirigida a otro frame, Route Q conserva el frame y el peer transiciona. | El peer no comprueba `target_frame`; debe heredar las mismas restricciones antes de considerarse equivalente. |
| `A6-GRAPH-QUALIFICATION` | El peer de grafo transiciona con todas las claims sin firma, caducadas y confianza cero. | Es un núcleo de dependencia, no una ruta conforme completa. Componer la validación local o reducir la afirmación. |
| `CROSS-P5-MISSING` | Dos diccionarios sin el campo material, o con `None`, dan base vigente. | `.get` convierte dos ausencias en igualdad. Exigir presencia y validez antes de comparar. |
| `CROSS-P2-NEGATIVE-BUDGET` | Presupuesto −1 puede producir `RESOLVED`. | Slice negativo de Python; dato fuera del presupuesto válido, sin guard. Añadir contrato de entrada. |
| `TRACE-LABEL-CHECK` | Todos los nombres de escenario se sustituyen en memoria por `NOT_THE_SCENARIO`; el validador pasa. | Comprueba estructura/rutas y que haya texto; no correspondencia semántica. |
| `CLOSURE-EMPTY-ATOMS` | El conjunto de átomos admitidos se vacía; el validador pasa con 0/0. | Cobertura vacua no bloqueada. Fijar el conjunto esperado/versionado; no presentar este PASS como prueba semántica de cierre. |

Las mutaciones se aplicaron a objetos en memoria o a entradas adicionales. **No se alteraron los archivos de modelos, manifiestos u oráculos auditados.** Las entradas inválidas no desacreditan por sí mismas los resultados de las entradas válidas congeladas; identifican una frontera que actualmente se presupone o no se valida.

## 5. Auditoría formal: A22 y A23 requieren distinciones diferentes

### H07 — El certificado A22 no comprueba toda la coherencia anunciada

[A20](../00K_A20_SHARED_SUBSTRATE_MATHEMATICAL_INDEPENDENCE_P1_P6_v0.1.md) exige en B8 que el conflicto material no resuelto se derive de registros actuales en conflicto. [A22](../00K_A22_FULL_CUBE_BOOLEAN_DIAGNOSTIC_MINIMALITY_v0.1.md), §4, afirma que sus modelos satisfacen las restricciones de coherencia; §3 habla de derivación desde el grafo de indagación.

El [código full-cube](../fixtures/00K-FORMAL/full-cube/full_cube_model.py) no representa una relación de conflicto ni un grafo de indagación. `Inquiry.unresolved`, `material_to_action` y `cyclic_progress` son entradas booleanas. El constructor fija su valor a partir de la firma solicitada. La función P4 comprueba tipo, ámbito, vigencia y presencia del grant, pero no representa una relación separada de no amplificación.

Prueba `A22-COHERENCE-BRIDGE`: se obtienen `111111` y `110111` con registros idénticos, cambiando la materialidad booleana de la indagación; no hay conflicto de registros representado para contrastar B8. Los 68 tests comprueban la firma resultante, no un validador de B1–B11.

**Conclusión precisa:** la construcción y el conteo son correctos para el modelo simplificado implementado. No queda demostrado por ese código que cada construcción sea un modelo de la teoría de coherencia más fuerte. Esto es un puente sin verificar, **no un contraejemplo al cálculo `2^5 < 64 <= 2^6` ni una demostración de falsedad de toda A20**.

**Corrección necesaria:** explicitar la abstracción y su levantamiento a modelos que satisfagan B, o representar conflicto, proceso y autoridad con sus restricciones y comprobar B antes de aceptar cada firma. Mantener separada la prueba de conteo.

### H08 — El guard de A23 es local a cada cláusula

Se reprodujo el certificado de A23 y se hizo una segunda enumeración de los soportes, obtenidos desde las referencias de campos de las funciones, sin usar el procedimiento de proyección del auditor:

| Principio | Filas proyectadas | Conformes | Conformes que violan P |
|---|---:|---:|---:|
| P1 | 8 | 1 | 0 |
| P2 | 256 | 3 | 0 |
| P3 | 4.096 | 518 | 3 |
| P4 | 8.192 | 4.099 | 0 |
| P5 | 8.192 | 108 | 3 |
| P6 | 1.024 | 34 | 1 |

No apareció un error aritmético nuevo en ese resultado. **No es una revisión externa independiente**, sino otra comprobación en esta auditoría sobre los mismos predicados.

La prueba `A23-DISTRIBUTED-SHORTCUT-LIMIT` separa `evidence_fit AND residual_explicit` en dos cláusulas. Cada una pasa el guard y juntas son exactamente P1. Eso demuestra que el guard no detecta un objetivo distribuido entre cláusulas. **Tampoco significa automáticamente que esa descomposición sea ilegítima:** una derivación fiel puede tener precisamente esa estructura. La prueba de no circularidad requiere justificar la traducción desde el canon; no puede reducirse a comprobar desigualdad de fórmulas.

Se conserva la [auditoría semántica previa](../fixtures/00K-FORMAL/requirement-sufficiency/CLAUSE_AUDIT.md): P3 no distingue toda respuesta autorizada bajo incertidumbre de falsa autorización; P6 exige independencia donde el canon permite correlación correctamente cualificada; P5 separa obligación registrada de ejecución efectiva. Sus contraejemplos no prueban automáticamente una carencia del canon.

## 6. Supuestos que deben seguir visibles en todas las familias

1. **Las entradas contienen hechos semánticos ya resueltos.** `proposition_supported`, raíces materiales, `root_authorized`, vigencia y campos materiales son hechos sintéticos entregados a los modelos. Comprobar que un algoritmo los usa no demuestra que un sistema pueda obtenerlos, validarlos o mantenerlos actualizados a coste viable.
2. **La necesidad por indistinguibilidad es condicional.** Dos mundos con la misma entrada para una política determinista no pueden obtener salidas distintas de esa política. La parte sustantiva es justificar la frontera de información, el oráculo y qué mecanismos alternativos se excluyen. No basta con llamar «reconstrucción del principio» a todo mecanismo que funciona para probar necesidad universal.
3. **Los controles humanos y de producto son sustitutos programados.** Por ejemplo, varias funciones de «aprobación humana» eligen el primer dato o cuentan votos; no son experimentos con personas ni mediciones de gobernanza. Los wrappers de hash/vector de A5 llaman al mismo comparador de campos: no ejecutan protocolos reales de concurrencia o invalidación.
4. **Hay aislamiento declarado, no una comprobación completa de los otros cinco principios en cada ablation.** Muchas propiedades se mantienen por los hechos fijados o por funciones muy reducidas. Los nombres «all six intact» y «strongest repair» no deben extenderse más allá de esa superficie probada.
5. **Los registros de trazabilidad/extensibilidad comprueban documentos y enlaces.** La coherencia de sus matrices y headings es útil, pero no prueba las implicaciones semánticas que los documentos argumentan. El paquete P5 blind-signature tampoco queda ejecutado automáticamente por el workflow 00K actual, aunque se ha ejecutado aquí.

## 7. Consecuencias para el artículo revisado

El artículo recibido **ya distingue correctamente** adaptadores compartidos de comparación independiente y conserva la parcialidad de A23. Deben añadirse o afinarse estos puntos antes de utilizarlo como cierre de la validación:

| Lugar | Cambio recomendado, todavía no aplicado al Word |
|---|---|
| §6 / trazas 00L | Mantener las cifras como replay; indicar que se exige acuerdo y no se conserva la traza final de divergencia. No interpretar `RESOURCE_EXHAUSTED` de 00E como consumo medido de seis pasos. |
| §7 / A22 | Aclarar que los 68 tests verifican el modelo simplificado, quedando pendiente el puente a las restricciones completas de coherencia. |
| §§7–8 / A4 | Limitar la suficiencia a las ramas probadas y registrar el contraejemplo de campañas mezcladas. |
| §9 / Step 0 | Mantener PASS/FAIL como resultado histórico del self-test; retirar la inferencia de que con ello quedó validado el handoff real. |
| §9 / métricas y negativos | Explicar que el contador de preservación y el guard de coste requieren corrección y que actualmente un fallo del candidato aborta antes de guardarse. |
| §2 / R2-V11 | Redactar explícitamente como diseño de prueba pendiente. No se encontró una ejecución R2/V11 en los paquetes Python auditados; el artículo debe evitar que “tests” se lea como resultado ejecutado. |

Frase breve admisible para artículo/README:

> The existing regressions and deterministic traces reproduce, but a later adversarial audit found additional gaps in handoff instrumentation, failure-trace retention, field-preservation scoring, mixed-campaign authorization and the executable bridge to the full-cube coherence assumptions. The shared-logic pairs remain regression controls, not independent architectural comparisons. These findings preserve the historical results while limiting the conclusions drawn from them; implementation corrections and renewed validation remain pending.

## 8. Orden de corrección y reproducción

1. Conservar los resultados actuales y esta auditoría como cortes históricos. Añadir versiones nuevas de los experimentos cuando cambie el contrato; no reescribir la preinscripción v0.5.
2. Corregir H02–H04 y el guard de 00L; registrar resultados negativos antes de terminar una ejecución. Repetir controles activos/inversos a través del trayecto real.
3. Corregir H05/H06 y los núcleos P5/P2; repetir las regresiones anteriores y convertir los contraejemplos pertinentes en tests de comportamiento esperado. Decidir explícitamente qué entradas quedan fuera del contrato y bloquearlas.
4. Resolver H07 mediante un puente formal explícito; mantener H08 como revisión semántica, sin sustituirla por un detector de similitud de fórmulas.
5. Solo después, diseñar una comparación independiente con mecanismos congelados antes de los resultados, oráculo separado, acceso y recursos comparables, y posibilidad real de desacuerdo. La deriva de relevancia R2/V11 necesita su propia ejecución.

Reproducción de los hallazgos, desde la raíz del repositorio que contiene este paquete:

```bash
python research/ecosystem-awareness/baseline/fixtures/AUDIT-20260926/probe_findings.py --output /tmp/ea-audit-probes.json
python research/ecosystem-awareness/baseline/fixtures/AUDIT-20260926/reproduce_baseline.py --output /tmp/ea-audit-baseline
```

El segundo comando requiere pytest. Las pruebas adversas terminan correctamente **cuando reproducen los defectos y límites registrados**, no cuando el sistema los ha corregido. Su recuento de 20 observaciones no se añade a los 379 ni se presenta como veinte experimentos independientes.

**Trabajo de esta fase:** auditoría, reproducciones, contraejemplos y registro; no se han corregido las implementaciones ni modificado el artículo, los requisitos, los modelos u oráculos originales. No se afirma ausencia de otros errores ni revisión humana independiente. La cobertura concreta queda enumerada arriba para que el siguiente revisor pueda continuar sin perder los hallazgos.
