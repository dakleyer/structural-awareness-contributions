# Auditoría científica incremental — ACC, Conscientia y reducción agéntica

**Estado:** abierta, incremental. Cada ronda añade hallazgos; ninguno se borra. Un hallazgo sólo cambia de estado (`ABIERTO` → `RESPONDIDO` → `CERRADO` / `RECHAZADO`) con una nota que diga quién lo decidió y por qué.
**Revisor:** Claude (Anthropic), asistido por IA, a petición del propietario. **No es la revisión científica humana independiente** que solicita la nota de revisión externa; es una auditoría previa para preparar esa revisión.
**Método:** lectura del código y de los documentos en los commits fijados abajo; desde la ronda 5, cálculos independientes en `audit_companion.py`. En la ronda 2 no se pudo ejecutar el código (el entorno del revisor bloqueó la ejecución de código externo); las cifras se derivaron analíticamente del código y coinciden con las declaradas en los PRs.

## Anexo y ayudas visuales

El [anexo](incremental-audit-2026-10-26/ANNEX.md) reúne lo que hace utilizable cada hallazgo en el PR auditado: mapa de hallazgos, diagramas, figuras con su vista en tabla, bocetos de corrección ejecutables, una tabla de enriquecimiento por PR, referencias bibliográficas por hallazgo y un glosario provisional. Las cifras se recalculan de forma independiente con [`audit_companion.py`](incremental-audit-2026-10-26/audit_companion.py), que reproduce los recuentos publicados por los PRs (por ejemplo, 107/14/39 en el barrido de #57) sin importar su código.

## Commits auditados

| Objeto | Commit |
|---|---|
| `main` | [`3e58fc6`](https://github.com/dakleyer/structural-awareness-contributions/tree/3e58fc6997a439b9783fd6b92ccee3f4292772dd) |
| PR #54 (abierto) | [`c332dfa`](https://github.com/dakleyer/structural-awareness-contributions/tree/c332dfac84d66f58ed424cee20ad6ad40060aec7) |
| PR #57 (abierto) | [`fb79df2`](https://github.com/dakleyer/structural-awareness-contributions/tree/fb79df2ce93c0730ed49c3454a6ebef033ebbe5e) |

Si cualquiera de estos commits cambia, los hallazgos afectados deben revalidarse antes de cerrarse.

**Revalidación (ronda 6):** el PR #57 avanzó a [`7b45341`](https://github.com/dakleyer/structural-awareness-contributions/tree/7b45341). Entre `fb79df2` y `7b45341` sólo cambian tres documentos (`README.md`, `SOURCE_MAP.md` y un nuevo anexo de linaje matemático y «Given Universe»); el código no cambia, así que F-01 a F-05 siguen vigentes. **El nuevo anexo no está cubierto por esta auditoría.**

## Registro de rondas

| Ronda | Fecha | Objeto | Hallazgos |
|---|---|---|---|
| 1 | 2026-10-26 | Nota «Solicitud de revisión científica independiente» (borrador del 26-10-2026) | N-01 a N-09 |
| 2 | 2026-10-26 | Código de PR #57 y PR #54 | F-01 a F-07 |
| 3 | 2026-10-26 | Campaña de PR #48/#49 en `main` (`conscientia-campaign-v0.1`) | G-01 a G-06 |
| 4 | 2026-10-26 | Modelo social: PR #42 (`bounded-traps-v0.1`) y PR #43 (`nested-composition-suffering-v0.1`) | H-01 a H-06 |
| 5 | 2026-10-26 | Ayudas visuales, cálculos independientes, propuestas ejecutables, referencias y glosario ([anexo](incremental-audit-2026-10-26/ANNEX.md)) | Sin hallazgos nuevos; confirma de forma independiente F-03, F-04, G-01, G-02, H-02 y H-03 |
| 6 | 2026-10-26 | Contraste con la revisión diaria del corpus (PR #59) y el comentario de revisión de Codex en este PR; `qualify` de PR #45 | I-01; cambios de estado de F-01, F-03, G-01 y G-05 |
| 7 | 2026-10-27 | Reconciliación de Codex con PR #59, TAX26 y la promoción a VNext propietarias ([sección al final](#corpus-reconciliation-and-promotion-review-27-october-2026); [anexo §7](incremental-audit-2026-10-26/ANNEX.md#7-corpus-reconciliation-and-promotion-readiness-27-october-2026)) | Sin hallazgos nuevos; revisa los bocetos de corrección |
| 8 | 2026-10-27 | Corpus matemático, revisión de Codex ([sección al final](#ronda-8); [anexo §8](incremental-audit-2026-10-26/ANNEX.md#8-mathematical-review-and-development-opportunities)) | M27-01 a M27-19 y oportunidades M27-O1 a M27-O5; M27-20 (alcance del argumento de Cantor en «The Given Universe» §6) registrado en un [comentario del PR](https://github.com/dakleyer/structural-awareness-contributions/pull/58#issuecomment-6446350643) |
| 9 | 2026-10-27 | Claridad de comparaciones y reparación transversal de lectura ([ronda 9](#ronda-9), [guía y fichas](incremental-audit-2026-10-26/INTERPRETATION_AND_COMPARISON_REPAIR_2026-10-27.md)) | Desarrolla M27-09: 36 unidades propuestas en 24 fuentes/ediciones; no aplica cambios canónicos |

Pendiente: modelo social #44–#46 (de #45 sólo se ha revisado `qualify`, I-01), anexo matemático nuevo de #57, núcleo #28/#40/#51, #21/#22 (00M_VNext) y los diferidos #5/#18 (linaje A/B/C/D).

---

## Ronda 6 — Contraste con la revisión diaria (PR #59) y defecto en PR #45

**Origen.** Comentario de revisión de **Codex** en este PR (26-10-2026): auditoría asistida por IA solicitada por Iván y publicada desde la cuenta del repositorio. No es una declaración personal de Iván ni una decisión de implementación. Contrasta esta auditoría con la revisión diaria publicada en [PR #59](https://github.com/dakleyer/structural-awareness-contributions/pull/59). Cada afirmación se ha recomprobado aquí contra el código; la recomprobación aritmética la hace Claude, también asistida por IA, y **no es una validación humana ciega**.

### Cambios de estado

| Hallazgo | Nuevo estado | Motivo |
|---|---|---|
| F-01 | `RESPONDIDO` | La revisión de Codex confirma que el brazo equivalente comparte rama de decisión. Pendiente de corrección o de reencuadre en #57. |
| F-03 | `RESPONDIDO` | Confirmada la ausencia del brazo equivalente en el barrido de tres brazos. |
| G-01 | `RESPONDIDO` | Confirmado: los 48 veredictos adjudicables del peer están estipulados como correctos. |
| G-05 | `RESPONDIDO` | Confirmado el solapamiento de 8 celdas de red con #49. |

Ningún hallazgo pasa a `CERRADO`: la confirmación del diagnóstico no es todavía su corrección. «Confirmado» significa aquí coincidencia entre dos revisiones asistidas por IA (Codex y Claude), no validación humana independiente.

### Precisiones de alcance aceptadas

- **Ámbito positivo.** Los argumentos finitos de fibras y conteo (H-06) y los de valor de la información son sólidos bajo sus supuestos. Ningún hallazgo de esta auditoría exige que un algoritmo sea imposible para código convencional; F-01 sólo pide que la comparación no se presente como evidencia de un diferencial.
- **F-02 no es evidencia.** Un `h` por brazo, como propone el anexo, hace explícita la hipótesis; no la apoya. Cualquier inferencia económica exige medir `h_convencional − h_agéntico` fuera del modelo.
- **Frontera de #57.** El anexo matemático nuevo y la reutilización externa de versiones Rxx no quedan cubiertos por haber revisado el código en `fb79df2` (ver revalidación arriba).
- **PR #22.** La revisión diaria señala una celda de reproducibilidad en Python 3.9 no ejecutada por configuración del runner. No se ha verificado aquí; es una cuestión de reproducibilidad, independiente de la validez matemática.

### I-01 · Alta · `ABIERTO` — `qualify` puede declarar «verdadero» con un intervalo vacío

**Identificado en:** revisión de Codex en PR #59 (D26-F01, propuesta D26-C01). **Recomprobado aquí** por Claude leyendo el código y reproduciendo la aritmética en [`audit_companion.py`](incremental-audit-2026-10-26/audit_companion.py) (`I01_empty_intersection_PR45`).

**Evidencia.** `.../studies/scoped-closure-metacognition-v0.1/metacognition.py` en `3e58fc6`, l. 171–187: `lo = max(lows)`, `hi = min(highs)`; la incoherencia sólo se declara si `lo > hi + 1e-12` (l. 178) y después se decide con `lo >= threshold` (l. 182). Contraejemplo: dos puntos atestiguados en x = 0 con intervalos [1e-13, 1e-13] y [0, 0], L = 0, umbral 5e-14. Resultado: lo = 1e-13 > hi = 0 (intersección vacía), la tolerancia absoluta lo deja pasar y el estado es `LOCALLY_SUPPORTED_TRUE`.

**Consecuencia.** Es un defecto real de implementación en el borde numérico, no una refutación de la inferencia de Lipschitz ni del modelo. Con una tolerancia absoluta fija, la decisión depende de la escala de los datos: cualquier par de evidencias contradictorias separado por menos de 1e-12 puede producir apoyo positivo. Las pruebas de regresión actuales no cubren este caso.

**Acción propuesta.** Rechazar cualquier `lo > hi` antes de decidir (con la regla estricta, el contraejemplo devuelve `EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT`). Si se quiere tolerancia numérica, que sea relativa a la escala de los datos y que el caso dentro de la tolerancia nunca produzca `SUPPORTED_*`. Añadir el contraejemplo como prueba de regresión y revisar si cambia algún resultado congelado.

---

## Ronda 4 — Modelo social: PR #42 y PR #43

Rutas abreviadas: `BT/` = `.../studies/bounded-traps-v0.1/`; `NC/` = `.../studies/nested-composition-suffering-v0.1/`.

### H-01 · Alta · `ABIERTO` — «Subóptimo racional» no está modelado: la trampa es de factibilidad, no de elección

> **Precisión posterior (ronda 10):** hallazgo válido para el toy binario, NO ausencia de teoría de coordinación en ACC. El modelo integrado ya documenta saturación de recursos, dimensión operativa de coordinación, codependencia, transferencias y NO GO. [Recepción y propuesta de precisión en PR #63](https://github.com/dakleyer/structural-awareness-contributions/pull/63).

**Evidencia.** `BT/bounded_traps.py`, `coupled_trap` (l. 74–99): las restricciones `x1 ≤ x2` y `x2 ≤ x1` (l. 80–82) hacen infactibles los estados intermedios (1,0) y (0,1). Desde (0,0) ningún paso unilateral es admisible (`reachable_by_unilateral_additions`, l. 51–71). Las utilidades (4,4) → (5,5) se escriben a mano (l. 86–87), no se derivan del estado. `NC/nested_model.py`, `agent_unilateral_reachability` (l. 45–58) repite el mismo caso.

**Consecuencia.** El resultado es correcto, pero muestra que un estado Pareto-dominado puede ser inalcanzable por pasos unilaterales cuando los intermedios están prohibidos. No muestra que permanecer sea *racional*: no hay agentes que elijan, ni pagos por agente, ni incentivos a desviarse. Un subóptimo racional exige que la desviación unilateral sea posible pero no rentable (equilibrio de Nash Pareto-inferior, como en la caza del ciervo). Además, el resultado es conocido (fallos de coordinación, equilibrios Pareto-inferiores, dependencia de trayectoria); el revisor pedirá situarlo en esa literatura.

**Acción propuesta.** Añadir una forma de juego mínima: dos agentes, pagos por perfil, desviación unilateral factible pero perjudicial, y verificar que (0,0) es equilibrio y (1,1) lo domina. Declarar qué aporta ACC frente a la literatura de coordinación.

### H-02 · Alta · `ABIERTO` — La brecha creciente con n es un supuesto reutilizado en tres PRs

**Evidencia.** `BT/bounded_traps.py`, `relative_gap` (l. 144–167): producción `b·n + α·E`, brecha `g·E` (l. 160). La misma especificación reaparece en `network_gap` de #49 (G-05) y en la familia `network` de #54 (F-06). En red densa con b = 10, g = 0,2, α = 0, la brecha relativa es `0,01·(n − 1)`: crece sin cota y supera el 100 % de la producción a partir de n = 102.

**Consecuencia.** La «acumulación de brechas» que la nota pide revisar (punto crítico 1) no la produce el modelo: es la hipótesis de que cada enlace aporta una ganancia conjunta no realizada y la producción realizada sólo escala con n. Que se ejecute en tres sitios no la convierte en tres evidencias; es la misma ecuación tres veces.

![Brecha supuesta frente a n](incremental-audit-2026-10-26/figures/H02_network_gap.svg)

**Acción propuesta.** Derivar la brecha de un mecanismo (por ejemplo, coste de coordinación por enlace frente a ganancia por enlace) con parámetros que permitan que la brecha se cierre, y declarar en un único lugar que las tres apariciones comparten supuesto.

### H-03 · Alta · `ABIERTO` — En #43 la pérdida informacional no viene de la composición anidada

> **Precisión posterior (ronda 10):** separar origen local de la censura en el código #43 y profundidad/perímetro de exploración desde el receptor. La primera crítica continúa válida; no refuta por sí misma la segunda tesis arquitectónica. [Propuesta explicativa y prueba pendiente en PR #63](https://github.com/dakleyer/structural-awareness-contributions/pull/63).

**Evidencia.** `NC/nested_model.py`: `hierarchical_current_output` (l. 112–126) devuelve exactamente la suma plana de `current_nested_output` (l. 105–109); el propio código lo afirma con `assert` (l. 162). La pérdida procede de la censura en las hojas: cada rama entrega `min(8, capacidad)` = 8 tanto si su capacidad es 8 como 10.

**Consecuencia.** El modelo demuestra no identificabilidad de la capacidad bajo observación censurada por la demanda. Eso ocurriría igual con n ramas que informaran por separado, sin anidamiento. La afirmación del título de #43 («composición anidada → pérdida informacional») no está sustentada por este código.

**Acción propuesta.** Añadir un caso sin censura donde el anidamiento por sí mismo pierda información (el padre sólo ve sumas de salidas distintas) y compararlo con informes planos al mismo ancho de banda. Si no se distingue de la censura, retitular el resultado.

### H-04 · Media · `ABIERTO` — «Sufrimiento estructural» es una brecha de contribución con nombre de bienestar

**Evidencia.** `NC/nested_model.py`, `structural_suffering_proxy` (l. 72–95): el indicador es `max(0, z − a)` cuando cuatro booleanos estipulados son verdaderos, y 0 en otro caso. El caso del informe (l. 185–191) los fija todos a verdadero.

**Consecuencia.** La magnitud no tiene contenido de bienestar: se mide en unidades de contribución y su valor depende sólo de la brecha estipulada. El código marca `subjective_suffering: NOT_MEASURED`, pero el término «sufrimiento» en títulos y documentos atraerá la objeción principal del revisor.

**Acción propuesta.** Llamarlo «brecha de desarrollo estructural» en el modelo y reservar «sufrimiento» para cuando exista un instrumento humano.

### H-05 · Media · `ABIERTO` — Utilidades no monótonas estipuladas, no derivadas

**Evidencia.** `BT/bounded_traps.py`, `apple_utility` (l. 118–123): la curva `(0, 4, 7, 8, 7, 5, 5, 9, 10)` es un literal. El docstring atribuye el valle a costes de almacenamiento y el pico a un umbral de mercado, pero ninguno de los dos está modelado.

**Consecuencia.** Es un ejemplo de existencia válido (una búsqueda local se detiene en q = 3 con máximo global en q = 8), y conocido. No sustenta afirmaciones sobre cuándo aparecen valles en economías reales.

**Acción propuesta.** Presentarlo como ejemplo de existencia, o derivar la curva de una función de ingreso con umbral menos una de coste de almacenamiento para que sus parámetros sean auditables.

### H-06 · Informativo · `VERIFICADO` — Cotas de información de #43 correctas

**Evidencia.** `NC/nested_model.py`, l. 129–169: con n ramas de capacidad 8 o 10 y salida actual constante 8n, hay 2ⁿ estados ocultos; responder exactamente a las n consultas por rama exige n bits, y una única consulta agregada exige ⌈log₂(n + 1)⌉ bits (`n.bit_length()`, correcto para n ≥ 1). `cnf_satisfiable` es búsqueda exhaustiva finita correcta.

**Consecuencia.** El argumento de conteo es sólido dentro del mundo finito declarado; su alcance real lo delimita H-03 (la causa es la censura).

---

## Ronda 3 — Campaña de PR #48/#49 (`main`)

Ruta abreviada: `CEC/` = `research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/conscientia-campaign-v0.1/`. La tabulación de `CASE_REGISTRY.json` se hizo leyendo el JSON, sin ejecutar el código del repositorio.

**Respuesta a la pregunta pendiente de F-06:** sí, el patrón se repite, y en la matriz de decisiones es más fuerte, porque la exactitud de los comparadores no se calcula: se estipula caso a caso.

### G-01 · Alta · `RESPONDIDO` (ronda 6) — La matriz 60 × 5 mide el diseño del fixture, no las estrategias

**Evidencia.** `CEC/campaign.py`, `public_policy` (l. 53–110): cada brazo copia un veredicto escrito en el caso (`q["verdict"]`, `peer["verdict"]`, `full["verdict"]`) o la acción base. Tabulación de `CEC/CASE_REGISTRY.json`:
- `CONVENTIONAL_TARGETED`: `has_direct_evidence = true` y `verdict == verdad privada` en los 48 casos adjudicables. Es un oráculo con coste; su resultado 48 correctas / 0 equivocadas está escrito en los datos.
- `EXPANDED_A`: cuando está disponible, su veredicto coincide con la verdad en todos los casos.
- Los brazos Q son los únicos con error inyectado: en las 12 variantes `FALSE_Q` el veredicto de Q es `ALLOW` con verdad `BLOCK`.
- Precios: el peer cuesta 0,5 o 1,6; Q cuesta 1,0 o 2,2 (más 0,3 de auditoría). Utilidades idénticas en los 60 casos.

**Consecuencia.** El ranking de `RUN_SUMMARY.md` (convencional 200,40; Q −52,80; A completo −262,00) se sigue directamente de qué brazo recibió veredictos correctos y de los precios asignados. El diseño está sesgado contra Q (honesto como control negativo) y, a la vez, no informa sobre Q: ningún brazo decide a partir de la información que tendría disponible.

**Acción propuesta.** Que el veredicto de cada comparador se derive de la información que ese comparador observa (misma restricción informativa para todos los brazos), con una tasa de error explícita también para el peer convencional. Mientras tanto, describir la tabla como «comprobación de que la función de puntuación aplica correctamente las pérdidas», no como resultado comparativo.

### G-02 · Media · `ABIERTO` — La «auditoría independiente» de Q es un booleano del fixture

**Evidencia.** `PARTIAL_Q_AUDIT_GATED` (l. 77–85) acepta una Q `CURRENT_BUT_FALSE` si `q["independent_audit"]` es verdadero. En 4 de los 12 casos `FALSE_Q`, ese indicador está activado: son exactamente las 4 equivocadas de ese brazo.

**Consecuencia.** El brazo no modela ninguna auditoría; modela que alguien declaró que hubo una. Su mejor resultado frente a `QUALIFIED_Q` (4 frente a 12 equivocadas) es el número de casos en que el fixture desactivó el indicador.

**Acción propuesta.** Modelar la auditoría con una probabilidad de detección y un coste, o renombrar el brazo para que no sugiera un mecanismo.

### G-03 · Media · `ABIERTO` — Varios «microexperimentos» son literales, no cálculos

**Evidencia.**
- `finite_information` (l. 225–238): define dos mundos, pero las entropías salen de distribuciones escritas a mano (`[0.5, 0.5]`, `[1.0, 0.0]`, l. 229); los mundos no se usan en el cálculo.
- `FINITE_XOR_SYNERGY` (l. 331–334): la información mutua (0, 0, 1 bits) es un literal. El valor es correcto, pero no se calcula.
- `IQ03_EFFICIENCY_GAP` (l. 248–251): la brecha 20 → 45 es resta de constantes; «el servicio aumenta y la brecha aumenta» está en los datos de entrada.
- Varias entradas (naranjas, educación, ministerios, oficios, liceo) son diccionarios de etiquetas `NOT_ESTABLISHED` / `NOT_OBSERVED`: puertas de evidencia, no ensayos.

**Consecuencia.** «Doce microexperimentos» y «61 pruebas» sobreafirman. Lo que se reproduce es la tabla de valores escrita por el autor.

**Acción propuesta.** Calcular las cantidades informativas a partir de los mundos definidos (por ejemplo, entropía condicional desde la tabla de mundos) y renombrar el bloque como «ilustraciones y puertas de evidencia».

### G-04 · Media · `ABIERTO` — Factorial y ablaciones FH-C son tautológicos por construcción

**Evidencia.** `factorial_joint_information` (l. 163–174): la salida es `atomic_joint and (q_available or not proof_required)`; la conclusión «Q sin mecanismo físico no genera recursos» es la propia fórmula. `fh_c_competing_ablations` (l. 177–205): los indicadores de cada perfil se fijan a mano para producir predicciones opuestas, y el resumen lo reconoce.

**Consecuencia.** Son especificaciones ejecutables, útiles para documentar la regla, pero no pruebas de nada que no esté en la regla.

**Acción propuesta.** Etiquetarlos como especificación; si se quiere poner a prueba FH-C, el comparador tiene que poder fallar por razones que no fije el autor del caso.

### G-05 · Baja · `RESPONDIDO` (ronda 6) — PR #54 duplica parcialmente la red de #49

**Evidencia.** `network_gap` (`CEC/campaign.py`, l. 208–222) usa densa/estrella, n = 5/10/20/40, b = 10, g = 0,2, α = 0. La rejilla `network` de `CAC/sensitivity.py` (PR #54) es un superconjunto: las 8 celdas con g = 0,2 y α = 0 reproducen exactamente las de #49.

**Consecuencia.** La afirmación de #54 de que «no duplica» la campaña anterior no es exacta para esta familia; 8 de sus 88 barridos ya estaban.

**Acción propuesta.** Declarar el solapamiento o eliminar esas celdas.

### G-06 · Baja · `ABIERTO` — Recuento de fuentes «cribadas»

**Evidencia.** `build_campaign` (l. 441) informa `source_documents_screened = len(SOURCE_REGISTER["sources"])`, que hoy es 23. El número cuenta entradas del registro, no documentos efectivamente cribados.

**Consecuencia.** Se suma a la discrepancia histórica 17/19 ya señalada (N-03): hay al menos tres cifras de «documentos cribados» en el corpus.

**Acción propuesta.** Distinguir en el registro «registrado», «leído» y «usado como fuente de un caso», y reconciliar 17/19/23 en un único lugar.

---

## Ronda 2 — Código de PR #57 y PR #54

Rutas abreviadas: `AGR/` = `research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/agentic-ecosystem-reduction-v0.1/` (PR #57); `CAC/` = `.../studies/conscientia-additional-cases-v0.1/` (PR #54).

### F-01 · Alta · `RESPONDIDO` (ronda 6) — En v0.1 el metaprotocolo es, en código, el brazo convencional con Q equivalente

**Evidencia.** `AGR/agentic_reduction.py`, `plan_public` (l. 129 y ss.): `Q_META_PROTOCOL` y `CONVENTIONAL_EQUIVALENT_Q` recorren la misma rama (l. 144); la única diferencia es el precio (`equivalent_Q_cost`, l. 147). Las compuertas de liberación, consentimiento, autoridad y protocolo conjunto (l. 182) se aplican igual a todos los brazos que transfieren, incluidos los convencionales. En `AGR/make_cases.py` el precio equivalente por defecto es igual al de Q (0,3; l. 21 y 24); sólo AG22 lo abarata (l. 71).

**Consecuencia.** El modelo no puede producir una ventaja del metaprotocolo sobre un sistema convencional con la misma Q: por construcción empata (mismo precio) o pierde (convencional más barato). La frase «un peer convencional con Q equivalente empata o gana» no es un resultado ni un falsador superado; es una identidad del código.

**Lo que ya reconoce el PR.** `ISOMORPHISM_AND_BOUNDARY_AUDIT.md` §2 (AG-R3) admite que un sistema no agéntico con la misma Q puede ejecutar el mismo algoritmo y que el diferencial queda en parámetros no probados. El hallazgo no contradice eso: lo confirma en código y señala que la descripción del PR y la nota de revisión siguen presentando la comparación de brazos como si fuera informativa.

**Acción propuesta.** Presentar #57 como **prueba de reducción completa en v0.1** (el metaprotocolo es una parametrización de ACC), no como evaluación del metaprotocolo. Para que la hipótesis agéntica sea falsable hace falta un operador o estado que no sea un precio, con un caso pareado donde el peer convencional con igual información y permisos no pueda replicarlo (criterio 2 de la propia auditoría de isomorfismo, §3).

### F-02 · Alta · `ABIERTO` — La única vía hacia un diferencial agéntico es H5, que no está probada y además no compara arquitecturas

**Evidencia.** El overhead `h` (`overhead_resources`) es un parámetro público del mundo, común a todos los brazos (`physical_response`, l. 100). AG23/AG24 cambian `h` para todos, no para una arquitectura frente a otra.

**Consecuencia.** Aun en el mejor caso, AG23/AG24 no pueden mostrar que una arquitectura agéntica tenga menor coste de reconfiguración: el mundo cambia, no el comparador. El PR ya declara H5 «no probada»; el problema es que, tras F-01, H5 es la **única** hipótesis que sostendría el diferencial agéntico.

**Acción propuesta.** Hacer `h` dependiente del brazo (p. ej. `h_agentic`, `h_conventional`) y declarar explícitamente que la ventaja agéntica, si existe, es exactamente la diferencia de esos dos parámetros, que debe medirse fuera del modelo.

### F-03 · Media · `RESPONDIDO` (ronda 6) — Los conteos del barrido (107/14/39 de 160) son artefactos del diseño de la rejilla

**Evidencia.** `AGR/sensitivity.py`:
- l. 17: la mitad de la rejilla usa `true_rate = 0,6`, menor que `donor_marginal_rate = 1`. Ninguna transferencia puede mejorar la producción, y los brazos con información pagan su coste aunque no actúen (`plan_public`, l. 175). Resultado: A-only es ganador exclusivo **por construcción** en esas 80 celdas.
- l. 31–32: el barrido compara sólo `A_ONLY`, `Q_META_PROTOCOL` y `CONVENTIONAL_DIRECTED`; **excluye** `CONVENTIONAL_EQUIVALENT_Q`.
- Derivación analítica de las 14 victorias exclusivas de Q+meta: con `true_rate = 2`, Q (cota 1,6, tope 2) sólo propone transferir si `h ∈ {0,1; 0,25; 0,5}` y su precio está por debajo de la ganancia condicional (7 configuraciones). Gana exclusivamente sólo cuando el instrumento dirigido cuesta 3 o 5, es decir, cuando no actúa o apenas gana: 7 × 2 = 14. Coincide con el PR.

**Consecuencia.** Las cifras describen la rejilla, no el mecanismo. Con el brazo convencional equivalente incluido al mismo precio, las 14 victorias serían empates (F-01).

![Ganador por celda del barrido de #57](incremental-audit-2026-10-26/figures/F03_sweep_winners.svg)

**Acción propuesta.** No citar los conteos como resultado. Incluir el brazo equivalente en el barrido, separar las celdas sin mejora posible y reportar las regiones del espacio de parámetros (fronteras de decisión) en lugar de recuentos.

### F-04 · Media · `ABIERTO` — En el caso insignia AG01 el convencional dirigido alcanza el óptimo técnico

**Evidencia.** Con los valores por defecto (`make_cases.py`, l. 50): A-only 10; Q+meta transfiere 2 → producción 11,5, neto 11,2; dirigido (tasa medida 2,0, tope 4, coste 1,2) transfiere 4 → producción 13,5 (el óptimo técnico), neto 12,3; A completo descartado por coste (cota 5,375 < 8).

**Consecuencia.** El PR resume AG01 como «Q+meta permite 11,5 frente al óptimo técnico 13,5» sin decir que, en el mismo caso, el comparador convencional lo alcanza y le gana en neto.

**Acción propuesta.** Reportar AG01 con todos los brazos.

### F-05 · Media · `ABIERTO` — Modelo lineal y conmensurabilidad no justificada

**Evidencia.** `physical_response`, l. 100: la producción es lineal en la transferencia; el óptimo cae siempre en una esquina (0 o máximo). `score_after_plan`, l. 219: el valor neto resta el coste informacional (utilidad sintética) de la producción física.

**Consecuencia.** (a) Los puntos de la nota sobre rendimientos decrecientes y no linealidad no aplican a #57 (el propio PR lo excluye en su alcance, pero la nota no lo dice). (b) Restar utilidad de producción exige una tasa de conversión explícita; hoy está fijada implícitamente en 1.

**Acción propuesta.** Declarar la conversión como parámetro y añadir un caso con rendimientos decrecientes del receptor para comprobar que las conclusiones cualitativas sobreviven.

### F-06 · Alta · `ABIERTO` — PR #54: casos trabajados, no experimentos

**Evidencia.** `CAC/campaign.py`, función `result`: cada «experimento» aplica una regla cerrada a entradas estipuladas en `CASES.json`.
- `distribution` (l. 38): comprueba `suma(mínimos) ≤ total`.
- `q_cost` (l. 94): asume el mismo beneficio realizado en todos los modos; el mejor modo es siempre el instrumento más barato. Las 24 variaciones `qualification` de `sensitivity.py` son, por tanto, triviales.
- `network` (l. 110): la brecha hipotética se define como `g × número de enlaces`; su crecimiento cuadrático en red densa es un supuesto, no un hallazgo.
- `kl` (l. 80): `log2(m/n)` es la divergencia KL correcta sólo para distribuciones uniformes; el supuesto no se declara.
- `closure` (l. 99) es la excepción: las cotas de Lipschitz producen inferencia no trivial a partir de muestras.
- Las 65 pruebas comparan la salida con `REFERENCE_RESULTS.json` / `REFERENCE_SWEEPS.json`: son pruebas de regresión, no de validación.

**Consecuencia.** El término «experimento» sobreafirma. El resultado de cada caso es consecuencia aritmética de su entrada; lo que se pone a prueba es la regla de clasificación, no una hipótesis sobre el mundo. Encaja exactamente en el riesgo de circularidad que la nota pide revisar.

**Acción propuesta.** Renombrar como «casos trabajados» o «fixtures de especificación»; declarar el supuesto de uniformidad en `kl`; destacar `closure` como el único mecanismo inferencial. Verificar si #48/#49 comparten el patrón (pendiente).

### F-07 · Baja · `ABIERTO` — Código muerto en `nonmonotone`

**Evidencia.** `CAC/campaign.py`, l. 45: la variable `loc` se calcula y no se usa.

**Acción propuesta.** Eliminarla o usarla; no afecta a resultados.

---

## Ronda 1 — Nota de solicitud de revisión externa

### N-01 · Alta · `ABIERTO` — Inventario incompleto
La auditoría #50 integra 11 PRs, incluidos #21 y #22; #22 añade 188 líneas a `00M_VNext`, que #47 vincula con el modelo social. La nota no los menciona, ni a los diferidos #5 y #18 (#5 es el linaje histórico de A/B/C/D, objeto del punto crítico 3), ni a #53, fusionado después.

### N-02 · Media · `ABIERTO` — Alcance de #50 sobredeclarado
#50 no audita #54 ni #57, que son posteriores. La sección E de la nota sugiere lo contrario.

### N-03 · Alta · `ABIERTO` — Limitaciones conocidas no declaradas
Los propios PRs declaran: evaluación asistida por IA sin revisión humana independiente (#50); discrepancia de procedencia 17/19 documentos cribados en #48/#49 sin reconciliar; H5 no probada (#57); 19 referencias a Google Docs pendientes de derechos/visibilidad; los 9 documentos que sustentan directamente los casos de #54 son Google Docs. La nota debe darlas de entrada.

### N-04 · Alta · `ABIERTO` — Autoría y procedencia
Buena parte del código, campañas y auditorías se ha generado con agentes (Codex aparece en #54; #50 menciona «otro bot»). La nota debe distinguir la autoría del propietario (hipótesis, modelo, IP) de lo producido con asistencia.

### N-05 · Alta · `ABIERTO` — Falta registro de afirmaciones
Se pide identificar «afirmaciones válidas» sin listarlas. Hace falta un registro H1…Hn con documento y sección.

### N-06 · Alta · `ABIERTO` — Encuadre de #57 y #54
Tras F-01 a F-06: #57 debe presentarse como prueba de reducción, no como evaluación del metaprotocolo; los conteos del barrido no deben citarse como resultado; #54 debe describirse como casos trabajados.

### N-07 · Media · `ABIERTO` — Objetivo móvil
`main` ya iba siete commits por delante del merge de #50 (`1f662a6`) al abrir esta auditoría. La nota debe fijar commits (ver tabla de arriba).

### N-08 · Media · `ABIERTO` — Siglas sin definir
ACC, 00M, UC21, DDS, HID, Q, A/B/C/D, Stage A/C. Hace falta glosario mínimo o enlace al índice.

### N-09 · Baja · `ABIERTO` — Logística y forma
Quitar el encabezado del agente; convertir el párrafo final en «Orden de lectura» (omite #40, #50, #51); añadir plazo, esfuerzo estimado, honorario, conflicto de intereses, confidencialidad, instrucciones de reproducción y formato de entrega; valorar dividir la revisión en matemático-económica (#28–#47) y experimental (#48–#57); idioma según el revisor.


## Corpus reconciliation and promotion review (27 October 2026)

**Contributor:** Codex, AI-assisted review requested by Iván. This continuation joins the existing finding log with the source-owned VNext work; it is not an independent human validation or a seventh global scientific pass.

The [annex promotion discussion](./incremental-audit-2026-10-26/ANNEX.md#7-corpus-reconciliation-and-promotion-readiness-27-october-2026) is the common receiving view. Exact source edits remain in their one existing owning VNext, transported by PR59. Earlier evidence, objections and finding states remain complete. A candidate passing software tests does not close a defect still present in published source.

- **I-01 / D26-C01:** unchanged baseline passes 60 unit tests. The private predicate-plus-test candidate passes 61 tests, including 18adverse gap/threshold subcases; generated synthetic_report dictionaries are equal. The full literal test companion is now published in 01I VNext with the original predicate pair.
- **First documentary promotion selection:** TAX26-02/04. All nine TAX26 source pairs still match the actual main source blobs and are not already applied. Their full original/proposed texts remain in their owners.
- **Current corpus cut:** main cc4f94605c329963747221a231c108bda0a61e20 is carried unchanged into this branch. New Structural Awareness mathematics, PR57 residual-cartography overlay and PR60 Theme18 annex/fixture are additional material; previous core findings do not automatically audit these extensions. The core studied functions and the nine TAX26 sources retain their original blobs.
- **PR60 integration:** its new annex uses A-conditioned supplementary evidence, but source 02/03 and 05/06 retain the passages targeted by D26-C04–07. This is a useful explicit response, not an applied source correction. Its workflow addition is a separate selection from the research-note content.
- **One reader-route repair:** a new mathematical citation omits one hyphen in its intended heading fragment. Source and target were read; the complete literal pair is in EP README VNext. This does not change the theorem or promote the working note.

No historical result, source, code, fixture, workflow, authority setting, earlier finding or proposal is removed or applied by this continuation. Actual canonical promotion remains the named source-wave decision and its verified execution.

Publication revalidation: current main 2d9e4509447910a8541827edfc82c592d42e3520 retains the nine TAX26 target blobs and the interval-study source/test blobs unchanged. Its concurrent research additions/edits are inherited without modification; this continuation does not certify their scientific content.


## Ronda 8

**Corpus matemático: hallazgos, correcciones de revisión y oportunidades · 27 octubre 2026.** Codex, revisión asistida por IA solicitada por Iván. Instrucción de recepción: todos los fallos y oportunidades encontrados en esta revisión se incorporan a este PR de auditoría compartida. Esta ronda agrega registros; no aplica las correcciones a las fuentes ni cambia los estados históricos de otros revisores.

### Lectura humana del resultado

El núcleo de factorización por fibras, preservación de distinciones, expresividad relativa, argumentos finitos de información y reutilización cualificada conserva contenido matemático bajo sus hipótesis. La revisión encontró un problema adicional de **consistencia conjunta** que el control del intervalo vacío no resuelve, varias integraciones documentales pendientes y condiciones que deben hacerse explícitas al extender el corpus a dinámica temporal.

Las nuevas líneas con más desarrollo son suficiencia de una representación durante una evolución, cotas de error ligadas a una pregunta y horizonte, renovación de poblaciones, carga de revisión con plazos y estabilidad de anclajes. Se registran como oportunidades matemáticas, separadas de los defectos. Las bases de proyección de campos vectoriales, Grönwall y transporte por edades son clásicas; su posible contribución aquí requiere precisar composición, evidencia y contratos.

**Corrección de esta propia revisión:** mi resumen en el chat generalizó indebidamente un control de reproducción de mecanismo a una valoración general de la aportación. Retiro esa extrapolación (M27-09). Un ejecutor que recibe la solución ya elegida no evalúa su descubrimiento, selección o adaptación; la Parte I §8 ya distingue estas actividades. La identidad de código de F-01 sigue siendo un hecho local del fixture, sin convertirse en una objeción automática a todo el corpus.

### Corte, cobertura y recepción

- Corte de la primera revisión: main `891af45a75b245082859147c0f7233cf85dd9035`; PR57 `553678e15e1ee3591736a4b8428abd4af4efc6fd`; PR60 `29ad055e107f40bdb458995f6b473ab50fe0ea0f`; PR54 `c332dfac84d66f58ed424cee20ad6ad40060aec7`.
- Revalidación de recepción: main `86cd02fe06ecfb7de883375a1952b73b5fa27150`; rama de auditoría antes de esta incorporación `92db1660167cf7bdde954652da821bf163a5b17b`. Los cuatro blobs usados por el nuevo acompañante se comprueban por su hash Git. El blob de `metacognition.py` coincide en el corte inicial y en la rama auditora.
- Ocho notas matemáticas de la primera revisión; anexos y código pertinentes de PR57/60; relectura focal de R01/R04/R05/R09/R10/R12/R19, dos manuscritos Semantic Window y fuentes D28/D34/D37. D08/D19 se consultaron mediante sus expedientes. Las compilaciones largas y las 60 entradas del catálogo no se presentan como 60 lecturas integrales nuevas.
- Entre los cambios posteriores al primer corte hay rutas/editorial y una nota/fixture de promoción de residual colectivo. Esa nota nueva `SA_COLLECTIVE_RESIDUAL_INTERSECTION_AND_EVENT_PROMOTION_v0.1.md` no hereda la cobertura de esta ronda. No se incorporan sus cambios a esta rama.
- Las pasadas efectivamente realizadas son focales de argumento y evidencia, más notación/legibilidad donde se indica. No se declaran completas las cuatro pasadas de cada documento ni la conciliación de todo el corpus.
- Los candidatos de corrección de fuente siguen en sus VNext propietarios, especialmente 01I y DDS en PR59. Esta ronda es su recepción en el registro de auditoría; no abre VNext competidoras ni aplica propuestas.

### Registro consolidado

| ID | Clase / estado de esta ronda | Evidencia y consecuencia | Acción o oportunidad |
|---|---|---|---|
| **M27-01** | Alta · ABIERTO · nuevo diagnóstico | [qualify, PR45](https://github.com/dakleyer/structural-awareness-contributions/blob/891af45a75b245082859147c0f7233cf85dd9035/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/scoped-closure-metacognition-v0.1/metacognition.py): con L=1, fuentes distintas f(0)=0 y f(0)=2 y pregunta f(1)≥1, devuelve `LOCALLY_SUPPORTED_TRUE`, [1,1]. No existe una función conjunta compatible. | Añadir una obligación de factibilidad conjunta o limitar explícitamente el significado de la cualificación local. El rechazo estricto del intervalo vacío no resuelve este caso. Prueba y control consistente en el anexo y acompañante. |
| **M27-02** | Alta · ABIERTO · conocido I-01 / D26-F01 | La tolerancia admite [1e-13,0] y una respuesta positiva; reproducción del fallo ya registrado. | Mantener el único candidato D26-C01 y sus controles en 01I VNext; agregar M27-01 como caso adicional, sin cerrar I-01 por haber preparado un parche. |
| **M27-03** | Alta · ABIERTO · conocido D26-F08 | [PR60 D3](https://github.com/dakleyer/structural-awareness-contributions/blob/29ad055e107f40bdb458995f6b473ab50fe0ea0f/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/mathematical-lineage-social-agentic-v0.1/02_FORMAL_CORE_AND_PROOFS.md) caracteriza bien Q sola; la selección suplementaria debe conservar A/o ya disponible. Cuatro mundos: seis pares totales, dos tras A; Q sola deja dos sin separar, A+Q no deja ninguno. | Mantener D3 en su alcance y usar conflictos condicionados por o para su aplicación suplementaria. Reconciliar fuente 02/03 con los anexos más recientes; candidatos D26-C04/05 ya propietarios de la propuesta. |
| **M27-04** | Alta · ABIERTO · conocido D26-F09 | PR60 05/06 mezcla la numeración nativa UC21 R0/R1/R2 con DDS prospectivo R1/R2/R3. | Distinguir nombres de espacio y preservar fallo real, reparación y predecesor aprobado; continuar D26-C06/07, sin duplicar el arreglo. |
| **M27-05** | Clarificación de fuente · confirmada | R12 enlaza a `primitiva-entropica.tex`, 10.822 bytes; el expediente ya declara el PDF temporal compilado por el revisor. El original no es un PDF histórico ni el manuscrito R11 firmado. La aplicación a certificados es una reconstrucción posterior. | Preservar la distinción TeX original / render posterior / adaptación. La fórmula espectral necesita una construcción de pesos dependiente del estado; el contraejemplo con Ω fija no debe confundirse con una refutación de toda asignación posible. No hay un nuevo fallo de MIME en el expediente que ya lo declara. |
| **M27-06** | Corrección del revisor · alegación retirada | DC-GH-01 v1.0.3 permite rutas subordinadas/opcionales y registro progresivo. La ausencia de una fila explícita no prueba por sí sola una infracción de las nuevas notas. | Se retira la inferencia de incumplimiento. Resolver identidad/propietario en la conciliación del registro; no convertir el predecesor genérico en una segunda política vigente. |
| **M27-07** | Baja · ABIERTO · procedencia | [Overlay PR57](https://github.com/dakleyer/structural-awareness-contributions/blob/553678e15e1ee3591736a4b8428abd4af4efc6fd/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/agentic-ecosystem-reduction-v0.1/residual_cartography_stage.py): `first_capture_observer_id=None` permite regla de etapa III y salida 11,5. | Precisar si el identificador es obligatorio. Si lo es, comprobarlo; si se admite ausencia, informar procedencia incompleta y no atribuir el primer captor. El evento puede conservarse; no es una refutación de De Morgan ni de la mejora condicional. |
| **M27-08** | Baja · ABIERTO · notación | En el núcleo económico, la expresión de segunda diferencia de M0 coincide con una convención central, mientras §9 usa una atrasada y M3 otra indexación. Para n=19,q=.9: central≈0 y atrasada≈.001853. | Rotular índice y convención en cada fórmula y consumidor; no presentar la diferencia de índices como una refutación algebraica. |
| **M27-09** | Corrección del revisor · retirada la extrapolación | SA-O2, última frase de §3, abrevia una equivalencia informativa. Mi resumen la convirtió en una conclusión general; PR57 entrega la misma Q y el mismo planificador al control. Parte I §8 distingue descubrir, seleccionar, compilar y ejecutar. | Corregir la lectura del revisor y precisar aquella frase si se acepta una edición. Misma información no implica igualdad de procedimientos, coste, tiempo o adaptación. Propuesta literal acotada en el anexo. |
| **M27-10** | Alta · ABIERTO · ecuación fuente R19 | Original §4.1, ecuación (4): Ṡ=(r+q)S−qH. Para r,q,H>0, la derivada lineal es positiva y [0,H] no es invariante. | Distinguir equilibrio de estabilidad. El cambio Ṡ=q(H−S)−rS es otro modelo de realimentación; demostrar sus propiedades y volver a justificar cualquier lectura física. |
| **M27-11** | Media · ABIERTO · alcance de la ventana | Las formulaciones de ambos Semantic Window pasan de información refinada/mejor política posible a mejora de todo estimador. Una media de diez datos actuales tiene MSE=.1; mezclar noventa de otro régimen con Δ=.1 da .0181 aunque introduce sesgo. | Formular el resultado sobre políticas elegibles/óptimas o una clase de estimadores y pérdida especificada. Conservar el resultado cualificado ya utilizado por la Parte II actual. |
| **M27-12** | Media · ABIERTO · suficiencia exacta y práctica | A2 permite agrupar instancias anteriores del mismo tipo. Esa historia puede cambiar el posterior de θ de .75 a .9 frente a una sola muestra actual: la ventana contigua actual no es automáticamente suficiente respecto de toda H. | Separar representación ordenada de historia, ventana contigua, suficiencia posterior exacta y adecuación bajo tolerancia. A3 ya supone estimabilidad; no presentarla como una prueba independiente de que se dispone de suficientes muestras hoy. |
| **M27-13** | Media · ABIERTO · estabilidad del anclaje | Prop.5 y construcción multiescala: una cota de la señal primaria no da automáticamente una cota del indicador ni controla reinicios. En tiempo discreto la cota de permanencia puede ser un solo paso. | Acotar el indicador real, especificar reinicios y probar Δt≥(θon−θoff)/v. Excluir cambios en cada muestra exige una condición adicional sobre el salto máximo o permanencia mínima. |
| **M27-14** | Media · ABIERTO · D28 Prop.3 | No-inferioridad frente a inacción no prueba dominancia sobre otra acción. En dos estados: inacción=(0,0), segura=(0,1), alternativa=(−1,100). La primera es segura; la segunda tiene mayor esperanza con probabilidades iguales. | Mantener el contrato de seguridad y retirar la inferencia de dominancia entre competidores salvo hipótesis adicionales. Diferenciar esos dos criterios. |
| **M27-15** | Media · ABIERTO · D34 | Haber salido una vez de d(P0,Pt)≤ε no implica permanecer fuera. Bernoulli(.5)→Bernoulli(.7)→Bernoulli(.5), ε=.1 en variación total, sale y vuelve. | Indexar la validez por tiempo; para afirmar no retorno hace falta otra hipótesis. La pérdida y recuperación para una pregunta puntual no borra un incumplimiento histórico. |
| **M27-16** | Media · ABIERTO · D34 / R09 / D08 | λ>μ durante un episodio no implica divergencia. λ=4,μ=2 por tres unidades; λ=0 después: carga máxima 6 y cola vacía en t=6. | Separar sobrecarga persistente, episodio y plazo perdido; usar llegadas brutas y servicio en unidades comunes, y llevar ahorro contrafactual en otro balance. |
| **M27-17** | Contraste de versión · aclaración ya presente | La fuente web D37 leída ya escribe P(A)P(P∣A)=P(A∩P), explica la independencia si se sustituye una marginal y separa severidad. | No reabrir como fallo vigente la lectura abreviada anterior. Conservar versión y procedencia al reutilizar el resultado. |
| **M27-18** | Media · ABIERTO · D37 | Podar/amplificar nodos define configuraciones candidatas; no establece por sí solo atractores estables de una dinámica. | Definir campo/mapa de evolución, dominio, equilibrio y criterio de estabilidad, o mantener la descripción como hipótesis operacional. |
| **M27-19** | Oportunidad de especificación · PROPUESTA · D37 | D_i=a_i+b_ix y S_i=c_i−d_ix, o extensión cuadrática, necesitan dominio y selección de raíz para producir un precio interpretable. | Para el caso afín, x*=(c−a)/(b+d) si b+d≠0; comprobar admisibilidad, unidades y significado presión/precio. Si b+d=0 puede no haber solución o haber muchas. |
| **M27-O1** | Desarrollo matemático · PROPUESTA | Extender R01/R04 y la Parte I a proyección de una dinámica. | Criterio DhF constante por fibra de h, con regularidad y dominio; ejemplo estable donde la observación actual deja de determinar una pregunta futura. |
| **M27-O2** | Desarrollo matemático · PROPUESTA | Extender SA-O5 y el horizonte de R19 a adecuación aproximada. | Cota de Grönwall y envolvente exacta del ejemplo; margen de decisión y pregunta/horizonte explícitos. |
| **M27-O3** | Desarrollo matemático · PROPUESTA | Extender la distinción de cohortes R10 y residual colectivo. | Transporte por edades: mejora individual e influjo exponencial pueden producir media residual γ/(γ+β); llegada constante produce media tendente a cero. |
| **M27-O4** | Desarrollo de capacidad · PROPUESTA | R09/D08/D34 y balance de R05. | Cola fluida reflejada, plazos útiles y contabilidad por incidencia sin sumar dos veces el mismo flujo; mantener separadas las magnitudes físicas y de esfuerzo. |
| **M27-O5** | Desarrollo de ventana · PROPUESTA | Semantic Window, D28 y D37. | Familia finita factible, error cualificado, coste y plazo; lema de histéresis con velocidad del indicador y tratamiento de reinicios. |

### Evidencia y siguiente acción

El [anexo §8](incremental-audit-2026-10-26/ANNEX.md#8-mathematical-review-and-development-opportunities) contiene los detalles, demostraciones internas y propuesta literal. El [acompañante estándar](incremental-audit-2026-10-26/math_audit_companion_2026-10-27.py) verifica cuatro blobs fijados y reproduce los defectos y controles seleccionados. Sus [resultados](incremental-audit-2026-10-26/MATH_AUDIT_RESULTS_2026-10-27.json) registran 32/32 comprobaciones internas; no son 32 estudios independientes.

La reproducción anterior de la primera revisión pasó 85 pruebas de PR57, seis de PR60, 65 de PR54 y 60 de PR45; los nueve programas matemáticos ejecutaron 10.062 aserciones finitas. Es una evidencia reproducible de esos cortes y ejemplos. Esta ronda no vuelve a ejecutar ni suma esos recuentos como nuevas observaciones.

Prioridad de corrección: M27-01/02, seguida de la integración M27-03/04. Prioridad de desarrollo: M27-O1/O2 como una línea conjunta de suficiencia temporal; M27-O5 para concretar ventanas; M27-O3 como línea distinta de renovación poblacional. Los cambios de fuentes y admisión DDS permanecen pendientes de sus decisiones y verificaciones propias.


## Ronda 9

**Claridad de comparaciones y prevención de extrapolaciones en todo el corpus · 27 de octubre de 2026.** Codex, asistencia de IA, por instrucción expresa de Iván. Esta ronda desarrolla M27-09 como un problema de redacción, lectura y traslado entre fuentes que puede afectar a cualquier autor o revisor. La propuesta se formula de manera asertiva sobre lo demostrado y conserva las críticas y resultados desfavorables que sí corresponden a una afirmación concreta.

**Entregable principal:** [Interpretar comparaciones sin borrar la aportación ni exagerarla](incremental-audit-2026-10-26/INTERPRETATION_AND_COMPARISON_REPAIR_2026-10-27.md). Contiene 36 fichas literales, verificadas en 24 fuentes/ediciones, con texto antes/después, dimensión de la comparación, explicación del riesgo, resultado que se conserva y ruta de incorporación. Dos fichas conservan una formulación ya correcta y aportan una pauta para citarla; las disposiciones históricas se añaden sin borrar la entrada anterior.

### Pauta de lectura vigente para F-01 y M27-09

Una reproducción de la decisión con el mismo procedimiento suministrado es un resultado de esa ejecución. La igualdad de información se refiere a las distinciones disponibles; requiere además un decodificador pertinente para hablar de decisiones, y costes/etapas definidos para hablar de utilidad neta. Ninguna de esas observaciones decide por sí sola el trabajo de descubrimiento, adquisición, selección, adaptación o mantenimiento.

Se mantiene el contenido positivo: un contrato enriquecido puede conservar una distinción necesaria que otro contrato perdió; una guarda cualificada puede ahorrar comprobaciones bajo su desigualdad de costes; las operaciones metasyntácticas son implementables en software ordinario. Cada proposición conserva su pregunta, clase y condiciones al trasladarse a índices, matrices, gráficos o resúmenes.

Un incumbente independiente que realmente alcanza el resultado con igual o menor carga completa sigue siendo evidencia contra el diferencial que se contrastaba. Su semejanza funcional con las operaciones propuestas no lo excluye de la comparación. A su vez, la programabilidad de una operación no demuestra que el método ya existiera ni que carezca de aportación. La guía desarrolla ambos límites sin convertirlos en una reserva automática tras cada resultado.

### Alcance y evidencia editorial

- Main fijado en `43203858893325b9cbc1c3e3b75f72a7d35e6f1d` y cambios fijados de los ocho PR abiertos 5/18/54/56/57/58/59/60. Se procesaron 2.725 archivos/ediciones (2.509 blobs distintos); 7.830 coincidencias amplias en 1.157 archivos/ediciones. Son coincidencias de búsqueda, no un recuento de fallos.
- La cobertura incluye texto de 6 PDF, 6 PPTX, 13 DOCX y 40 SVG entre las instantáneas. Veinte archivos de main —rasteres y evidencia/paquetes comprimidos— quedan identificados fuera de extracción textual. No se declara una revisión visual exhaustiva ni una nueva lectura de todos los originales privados.
- [Cobertura y exclusiones](incremental-audit-2026-10-26/INTERPRETATION_COVERAGE_2026-10-27.json), [índice completo por archivo](incremental-audit-2026-10-26/INTERPRETATION_COVERAGE_INDEX_2026-10-27.csv.gz) y [fichas estructuradas](incremental-audit-2026-10-26/INTERPRETATION_REPAIR_CANDIDATES_2026-10-27.json).
- El [verificador de propuestas](incremental-audit-2026-10-26/verify_interpretation_repair_2026-10-27.py) comprueba blob, unidad literal, localización, conservación individual y combinación de candidatos sobre una misma fuente. [36/36 fichas verificadas](incremental-audit-2026-10-26/INTERPRETATION_REPAIR_VERIFICATION_2026-10-27.json), cero ediciones de fuentes aplicadas.
- La propuesta cubre tesis/resúmenes, teoremas, código/datos, fixtures, tablas/figuras, README, matrices/linaje, auditorías, VNext, históricos, presentaciones e informes. Incluye plantillas, primera ola sugerida, rutas propietarias y una prueba de comprensión propuesta para nuevos lectores; esa prueba humana no se presenta como ya realizada.

Las fichas son propuestas para sus fuentes y propietarios. Esta publicación amplía la recepción del PR58, conserva los resultados y estados anteriores y no aplica cambios a los estudios, canon o datos. La incorporación posterior se selecciona por unidad y se verifica en su fuente y receptores.


## Ronda 10 — alcance de H-01 y H-03 y prevención de extrapolaciones (27-10-2026)

**Origen:** observaciones y corrección conceptual del autor, Iván Abril Palma, en diálogo con Codex; revisión documental asistida por IA, no arbitraje científico humano independiente. **Recepción documental propuesta:** [PR #63](https://github.com/dakleyer/structural-awareness-contributions/pull/63), sin merge ni promoción a Canonical a la fecha de esta ronda. Se preservan íntegros los hallazgos originales y su trazabilidad; las siguientes son **precisiones de alcance**, no borrados ni pruebas nuevas.

### R10-H01 — El bloqueo binario no agota la teoría multidimensional ACC

- **Hecho local válido que conserva H-01:** en `bounded_traps.py/coupled_trap`, las restricciones `x1≤x2` y `x2≤x1` excluyen desviaciones unilaterales. El ejemplo comprueba inaccesibilidad de (1,1) desde (0,0) por esos pasos; no comprueba un equilibrio de Nash Pareto-inferior.
- **Alcance indebidamente ampliado:** inferir que ACC «no explica por qué» se bloquea una mejora o que debe inventarse la coordinación como dimensión futura. `MODEL.md`, «Del caso de una dimensión al modelo abierto», «Mecanismo primario de bloqueo: saturación y codependencia» y «Propuestas aceptación y reajuste», ya caracterizan recursos, límites de coordinación, codependencia, transferencias factibles, autoridad y NO GO. `ECONOMIC_MODEL_TECHNICAL_CORE_v0.1.md` contiene la misma línea de investigación.
- **Criterio anti-regresión:** ninguna nueva dimensión se añade por conveniencia analítica. Debe existir una restricción o función operativa identificable, recursos propios/transferidos/externos, efectos de transferencia y condición de continuidad. «Oportunidad», «capacidad», «coste» y «brecha» pueden ser variables o salidas; no son cuatro dimensiones nuevas. Si una dimensión indispensable no puede mantenerse, la transición es NO GO bajo el régimen actual.
- **Tratamiento:** conservar H-01 abierto exclusivamente para corregir el rótulo y/o añadir, si se desea esa afirmación adicional, un modelo de elección con desviaciones factibles y pagos; **no** exigir reconstruir un modelo de coordinación que ya existe en ACC. [Propuesta source-owned](https://github.com/dakleyer/structural-awareness-contributions/pull/63) deja la lectura explícita para cualquier auditor posterior.

### R10-H03 — Lugar de la pérdida, profundidad de la causa y alcance de exploración son preguntas distintas

- **Hecho local válido que conserva H-03:** el runner v0.1 de #43 tiene `hierarchical_current_output == current_nested_output` y censura capacidades en las hojas con `min(8,capacidad)`. Ese runner no demuestra una pérdida adicional de bits causada *únicamente* por la suma jerárquica frente a una interfaz plana con la misma observabilidad.
- **Mecanismo arquitectónico que la crítica local no descarta:** el agente receptor observa una interfaz de su proveedor, que a su vez consume inputs y depende de restricciones de otros proveedores. El origen de una distinción perdida puede hallarse a varios niveles de distancia, más allá del ecosistema accesible para el receptor. Conocer todo el A que efectivamente expone el proveedor inmediato no otorga acceso a la capacidad de los proveedores de ese proveedor. El número de saltos relevantes, las facultades de acceso y el coste de inspección pueden ser desconocidos para ese agente.
- **Apertura simulada, no metafísica:** un árbol **finito y conocido por el simulador**, con revelación selectiva por nivel y límites de consulta, puede presentar un **exterior abierto relativo al receptor**. Ello no demuestra infinitud física, pérdida estricta en cada capa, complejidad intratable universal o indecidibilidad turingiana. Si todo el árbol y los fundamentos relevantes son accesibles con tiempo suficiente, la exploración exhaustiva del toy puede resolver la pregunta.
- **Contrato de falsación pendiente:** (i) fijar actor, pregunta, acceso, permisos, presupuesto y horizonte; (ii) controlar dónde se retienen/ocultan distinciones en varias capas; (iii) construir mundos `w0,w1` con el mismo transcript para todas las consultas disponibles al receptor hasta profundidad `k` y respuestas reales diferentes; (iv) variar profundidad/origen y coste, registrar si se descubre la fuente; (v) comparar con control plano de información y coste equiparables y un control con certificado suficiente. Si el control de información completa resuelve, debe constar. Este protocolo todavía **no se ha ejecutado en #43**.
- **Fuentes ya existentes:** `nested-composition-suffering-v0.1/README.md` §§2–3, `intrinsic-abcd-economics-v0.1/README.md` §§1–4 y `MODEL.md` §«A/B/C/D como frontera intrínseca...» distinguen fuente, interfaz, pregunta y ruta de adquisición. [PR #63](https://github.com/dakleyer/structural-awareness-contributions/pull/63) añade el puente explícito para que esa distinción sea visible en el punto auditado.

### Regla transversal para futuras rondas

Antes de etiquetar una «ausencia conceptual» se deben contrastar **(a)** la función efectivamente implementada, **(b)** el alcance del caso, **(c)** los documentos integradores y ejemplos de la misma familia, y **(d)** los estudios arquitectónicos/matemáticos conexos. Reportar explícitamente «falta en esta prueba» frente a «falta en el corpus». Las medidas de un mecanismo no generan dimensiones operativas arbitrarias. Una crítica a un toy no debe promoverse como refutación del programa general sin una prueba que conecte ambos alcances.

**Estados y promoción:** H-01/H-03 permanecen `ABIERTO` en su alcance ejecutable. R10-H01/R10-H03 documentan la respuesta del autor y la delimitación; PR #63 contiene propuestas en tres documentos vivos y permanece separado de esta auditoría. No hay cierre, aprobación de evidencia independiente, ejecución de los nuevos controles ni merge automático.
