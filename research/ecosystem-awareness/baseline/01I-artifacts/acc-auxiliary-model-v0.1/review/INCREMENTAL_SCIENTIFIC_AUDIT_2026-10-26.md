# Auditoría científica incremental — ACC, Conscientia y reducción agéntica

> **Actualización de lectura — ronda16:** el [suplemento actual](#ronda-16) reconfirma los cierres numéricos en main, recibe la corrección de dominio en la rama60 y examina la nueva§15 del puente62. La guía conserva su estado tras la ronda15; esta actualización añade sus consecuencias y seis propuestas concretas sin reabrir los defectos corregidos.

> **Lectura vigente — 28 octubre 2026, tras la ronda 14:** para orientarse, empiece por la [guía de lectura](incremental-audit-2026-10-26/GUIA_DE_LECTURA.md): estado vigente de los 71 registros, ideas clave en lenguaje llano, mapa de rondas y glosario. I-01 está **cerrado** (corregido en `main` por PR #64 y reconfirmado en la [ronda 13](#ronda-13)). Los encabezados de cada hallazgo conservan el estado que tenían al escribirse; el estado vigente está en la guía y en [`STATUS_LEDGER_2026-10-28.json`](incremental-audit-2026-10-26/STATUS_LEDGER_2026-10-28.json).
>
> *Lectura anterior, previa a la ronda 13 (se conserva):* **Lectura vigente — 28 octubre 2026:** la [ronda12](#ronda-12--relectura-del-corpus-y-estado-real-de-la-auditoría-28-octubre-2026) actualiza mejoras, observaciones y pendientes. PR60 recibió D3-A y nombres UC21/DDS; PR64 repara los ejemplos originales pero conserva un problema numérico nuevo; P5/Python3.9 ya tiene sucesor correcto en main. Los encabezados históricos se leen con las delimitaciones9–11: no expresan una valoración general del programa matemático. Las propuestas IP siguen pendientes de incorporación.

**Estado:** abierta, incremental. Cada ronda añade hallazgos; ninguno se borra. Un hallazgo sólo cambia de estado (`ABIERTO` → `RESPONDIDO` → `CERRADO` / `RECHAZADO`) con una nota que diga quién lo decidió y por qué. Además se usan `VERIFICADO` (revisado y correcto), `PROPUESTA` (mejora, no defecto), `RETIRADO` (el revisor retira su crítica) e `INFORMATIVO` (aclaración); las variantes que aparecen en rondas posteriores («corrección propuesta en fuente», «recibido», «confirmada») se normalizan a estos siete estados en la [guía de lectura](incremental-audit-2026-10-26/GUIA_DE_LECTURA.md#3-cómo-está-todo-ahora) (ronda 14).
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
| 10 | 2026-10-27 | [Alcance H01/H03 y respuesta del autor](#ronda-10--alcance-de-h-01-y-h-03-y-prevención-de-extrapolaciones-27-10-2026); candidato63 | Preserva críticas locales; diferencia ausencia en test y ausencia en corpus |
| 11 | 2026-10-27 | [Recepción64/comparadores/casos54](#ronda-11--resolución-técnica-de-i-01-delimitación-de-comparadores-y-clasificación-de-casos-27-10-2026) | Respuesta a I01/M27-01/02, G01/F01 y F06; sin cierre por publicación |
| 12 | 2026-10-28 | [Relectura y cola vigente](#ronda-12--relectura-del-corpus-y-estado-real-de-la-auditoría-28-octubre-2026); [anexo10](incremental-audit-2026-10-26/ANNEX.md#10-corpus-refresh-and-open-audit-work--28-october-2026) | M28-01…07; oportunidadesO1/O2; revalidación IP01–36 y propuestas IP37–42 |
| 13 | 2026-10-28 | [Reconfirmación de I-01 en `main`](#ronda-13--reconfirmación-de-i-01--m27-01--m28-01-en-main-28-10-2026) tras fusionar PR #64 | I-01 `CERRADO`; M27-01/M28-01 reconfirmados |
| 14 | 2026-10-28 | [Revisión formal del expediente y guía de lectura](#ronda-14) | J-01 a J-08; [guía](incremental-audit-2026-10-26/GUIA_DE_LECTURA.md), registro de estados y 74 anclas estables |
| 15 | 2026-10-28 | [Reconfirmación de M28-02 en la rama de #60](#ronda-15) | M28-02 `RESPONDIDO` (implementado en rama, pendiente de `main`) |
| 16 | 2026-10-28 | [Relectura de cambios y cinco mecanismos](#ronda-16); [propuestas](incremental-audit-2026-10-26/ANNEX.md#11-ronda-16--recepción-y-propuestas-acotadas) | Cierres numéricos recibidos, dominio60 reconfirmado, próximos controles matemáticos y recepción59 |
| 17 | 2026-10-28 | [Modelo social #44, #45 (resto) y #46](#ronda-17) | K-01 a K-08 |
| 18 | 2026-10-28 | [Precisión de alias en la guía (D28-C03)](#ronda-18) | Sin hallazgos nuevos; precisión añadida a la guía |

Pendiente: modelo social #44–#46 (de #45 sólo se ha revisado `qualify`, I-01), anexo matemático nuevo de #57, núcleo #28/#40/#51, #21/#22 (00M_VNext) y los diferidos #5/#18 (linaje A/B/C/D).

---

<a id="ronda-06"></a>

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

<a id="i-01"></a>

### I-01 · Alta · `CERRADO` (ronda 13, 28-10-2026) — `qualify` puede declarar «verdadero» con un intervalo vacío

**Identificado en:** revisión de Codex en PR #59 (D26-F01, propuesta D26-C01). **Recomprobado aquí** por Claude leyendo el código y reproduciendo la aritmética en [`audit_companion.py`](incremental-audit-2026-10-26/audit_companion.py) (`I01_empty_intersection_PR45`).

**Evidencia.** `.../studies/scoped-closure-metacognition-v0.1/metacognition.py` en `3e58fc6`, l. 171–187: `lo = max(lows)`, `hi = min(highs)`; la incoherencia sólo se declara si `lo > hi + 1e-12` (l. 178) y después se decide con `lo >= threshold` (l. 182). Contraejemplo: dos puntos atestiguados en x = 0 con intervalos [1e-13, 1e-13] y [0, 0], L = 0, umbral 5e-14. Resultado: lo = 1e-13 > hi = 0 (intersección vacía), la tolerancia absoluta lo deja pasar y el estado es `LOCALLY_SUPPORTED_TRUE`.

**Consecuencia.** Es un defecto real de implementación en el borde numérico, no una refutación de la inferencia de Lipschitz ni del modelo. Con una tolerancia absoluta fija, la decisión depende de la escala de los datos: cualquier par de evidencias contradictorias separado por menos de 1e-12 puede producir apoyo positivo. Las pruebas de regresión actuales no cubren este caso.

**Acción propuesta.** Rechazar cualquier `lo > hi` antes de decidir (con la regla estricta, el contraejemplo devuelve `EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT`). Si se quiere tolerancia numérica, que sea relativa a la escala de los datos y que el caso dentro de la tolerancia nunca produzca `SUPPORTED_*`. Añadir el contraejemplo como prueba de regresión y revisar si cambia algún resultado congelado.

---

<a id="ronda-04"></a>

## Ronda 4 — Modelo social: PR #42 y PR #43

Rutas abreviadas: `BT/` = `.../studies/bounded-traps-v0.1/`; `NC/` = `.../studies/nested-composition-suffering-v0.1/`.

<a id="h-01"></a>

### H-01 · Alta · `ABIERTO` — «Subóptimo racional» no está modelado: la trampa es de factibilidad, no de elección

> **Precisión posterior (ronda 10):** hallazgo válido para el toy binario, NO ausencia de teoría de coordinación en ACC. El modelo integrado ya documenta saturación de recursos, dimensión operativa de coordinación, codependencia, transferencias y NO GO. [Recepción y propuesta de precisión en PR #63](https://github.com/dakleyer/structural-awareness-contributions/pull/63).

**Evidencia.** `BT/bounded_traps.py`, `coupled_trap` (l. 74–99): las restricciones `x1 ≤ x2` y `x2 ≤ x1` (l. 80–82) hacen infactibles los estados intermedios (1,0) y (0,1). Desde (0,0) ningún paso unilateral es admisible (`reachable_by_unilateral_additions`, l. 51–71). Las utilidades (4,4) → (5,5) se escriben a mano (l. 86–87), no se derivan del estado. `NC/nested_model.py`, `agent_unilateral_reachability` (l. 45–58) repite el mismo caso.

**Consecuencia.** El resultado es correcto, pero muestra que un estado Pareto-dominado puede ser inalcanzable por pasos unilaterales cuando los intermedios están prohibidos. No muestra que permanecer sea *racional*: no hay agentes que elijan, ni pagos por agente, ni incentivos a desviarse. Un subóptimo racional exige que la desviación unilateral sea posible pero no rentable (equilibrio de Nash Pareto-inferior, como en la caza del ciervo). Además, el resultado es conocido (fallos de coordinación, equilibrios Pareto-inferiores, dependencia de trayectoria); el revisor pedirá situarlo en esa literatura.

**Acción propuesta.** Añadir una forma de juego mínima: dos agentes, pagos por perfil, desviación unilateral factible pero perjudicial, y verificar que (0,0) es equilibrio y (1,1) lo domina. Declarar qué aporta ACC frente a la literatura de coordinación.

<a id="h-02"></a>

### H-02 · Alta · `ABIERTO` — La brecha creciente con n es un supuesto reutilizado en tres PRs

**Evidencia.** `BT/bounded_traps.py`, `relative_gap` (l. 144–167): producción `b·n + α·E`, brecha `g·E` (l. 160). La misma especificación reaparece en `network_gap` de #49 (G-05) y en la familia `network` de #54 (F-06). En red densa con b = 10, g = 0,2, α = 0, la brecha relativa es `0,01·(n − 1)`: crece sin cota y supera el 100 % de la producción a partir de n = 102.

**Consecuencia.** La «acumulación de brechas» que la nota pide revisar (punto crítico 1) no la produce el modelo: es la hipótesis de que cada enlace aporta una ganancia conjunta no realizada y la producción realizada sólo escala con n. Que se ejecute en tres sitios no la convierte en tres evidencias; es la misma ecuación tres veces.

![Brecha supuesta frente a n](incremental-audit-2026-10-26/figures/H02_network_gap.svg)

**Acción propuesta.** Derivar la brecha de un mecanismo (por ejemplo, coste de coordinación por enlace frente a ganancia por enlace) con parámetros que permitan que la brecha se cierre, y declarar en un único lugar que las tres apariciones comparten supuesto.

<a id="h-03"></a>

### H-03 · Alta · `ABIERTO` — En #43 la pérdida informacional no viene de la composición anidada

> **Precisión posterior (ronda 10):** separar origen local de la censura en el código #43 y profundidad/perímetro de exploración desde el receptor. La primera crítica continúa válida; no refuta por sí misma la segunda tesis arquitectónica. [Propuesta explicativa y prueba pendiente en PR #63](https://github.com/dakleyer/structural-awareness-contributions/pull/63).

**Evidencia.** `NC/nested_model.py`: `hierarchical_current_output` (l. 112–126) devuelve exactamente la suma plana de `current_nested_output` (l. 105–109); el propio código lo afirma con `assert` (l. 162). La pérdida procede de la censura en las hojas: cada rama entrega `min(8, capacidad)` = 8 tanto si su capacidad es 8 como 10.

**Consecuencia.** El modelo demuestra no identificabilidad de la capacidad bajo observación censurada por la demanda. Eso ocurriría igual con n ramas que informaran por separado, sin anidamiento. La afirmación del título de #43 («composición anidada → pérdida informacional») no está sustentada por este código.

**Acción propuesta.** Añadir un caso sin censura donde el anidamiento por sí mismo pierda información (el padre sólo ve sumas de salidas distintas) y compararlo con informes planos al mismo ancho de banda. Si no se distingue de la censura, retitular el resultado.

<a id="h-04"></a>

### H-04 · Media · `ABIERTO` — «Sufrimiento estructural» es una brecha de contribución con nombre de bienestar

**Evidencia.** `NC/nested_model.py`, `structural_suffering_proxy` (l. 72–95): el indicador es `max(0, z − a)` cuando cuatro booleanos estipulados son verdaderos, y 0 en otro caso. El caso del informe (l. 185–191) los fija todos a verdadero.

**Consecuencia.** La magnitud no tiene contenido de bienestar: se mide en unidades de contribución y su valor depende sólo de la brecha estipulada. El código marca `subjective_suffering: NOT_MEASURED`, pero el término «sufrimiento» en títulos y documentos atraerá la objeción principal del revisor.

**Acción propuesta.** Llamarlo «brecha de desarrollo estructural» en el modelo y reservar «sufrimiento» para cuando exista un instrumento humano.

<a id="h-05"></a>

### H-05 · Media · `ABIERTO` — Utilidades no monótonas estipuladas, no derivadas

**Evidencia.** `BT/bounded_traps.py`, `apple_utility` (l. 118–123): la curva `(0, 4, 7, 8, 7, 5, 5, 9, 10)` es un literal. El docstring atribuye el valle a costes de almacenamiento y el pico a un umbral de mercado, pero ninguno de los dos está modelado.

**Consecuencia.** Es un ejemplo de existencia válido (una búsqueda local se detiene en q = 3 con máximo global en q = 8), y conocido. No sustenta afirmaciones sobre cuándo aparecen valles en economías reales.

**Acción propuesta.** Presentarlo como ejemplo de existencia, o derivar la curva de una función de ingreso con umbral menos una de coste de almacenamiento para que sus parámetros sean auditables.

<a id="h-06"></a>

### H-06 · Informativo · `VERIFICADO` — Cotas de información de #43 correctas

**Evidencia.** `NC/nested_model.py`, l. 129–169: con n ramas de capacidad 8 o 10 y salida actual constante 8n, hay 2ⁿ estados ocultos; responder exactamente a las n consultas por rama exige n bits, y una única consulta agregada exige ⌈log₂(n + 1)⌉ bits (`n.bit_length()`, correcto para n ≥ 1). `cnf_satisfiable` es búsqueda exhaustiva finita correcta.

**Consecuencia.** El argumento de conteo es sólido dentro del mundo finito declarado; su alcance real lo delimita H-03 (la causa es la censura).

---

<a id="ronda-03"></a>

## Ronda 3 — Campaña de PR #48/#49 (`main`)

Ruta abreviada: `CEC/` = `research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/conscientia-campaign-v0.1/`. La tabulación de `CASE_REGISTRY.json` se hizo leyendo el JSON, sin ejecutar el código del repositorio.

**Respuesta a la pregunta pendiente de F-06:** sí, el patrón se repite, y en la matriz de decisiones es más fuerte, porque la exactitud de los comparadores no se calcula: se estipula caso a caso.

<a id="g-01"></a>

### G-01 · Alta · `RESPONDIDO` (ronda 6) — La matriz 60 × 5 mide el diseño del fixture, no las estrategias

**Evidencia.** `CEC/campaign.py`, `public_policy` (l. 53–110): cada brazo copia un veredicto escrito en el caso (`q["verdict"]`, `peer["verdict"]`, `full["verdict"]`) o la acción base. Tabulación de `CEC/CASE_REGISTRY.json`:
- `CONVENTIONAL_TARGETED`: `has_direct_evidence = true` y `verdict == verdad privada` en los 48 casos adjudicables. Es un oráculo con coste; su resultado 48 correctas / 0 equivocadas está escrito en los datos.
- `EXPANDED_A`: cuando está disponible, su veredicto coincide con la verdad en todos los casos.
- Los brazos Q son los únicos con error inyectado: en las 12 variantes `FALSE_Q` el veredicto de Q es `ALLOW` con verdad `BLOCK`.
- Precios: el peer cuesta 0,5 o 1,6; Q cuesta 1,0 o 2,2 (más 0,3 de auditoría). Utilidades idénticas en los 60 casos.

**Consecuencia.** El ranking de `RUN_SUMMARY.md` (convencional 200,40; Q −52,80; A completo −262,00) se sigue directamente de qué brazo recibió veredictos correctos y de los precios asignados. El diseño está sesgado contra Q (honesto como control negativo) y, a la vez, no informa sobre Q: ningún brazo decide a partir de la información que tendría disponible.

**Acción propuesta.** Que el veredicto de cada comparador se derive de la información que ese comparador observa (misma restricción informativa para todos los brazos), con una tasa de error explícita también para el peer convencional. Mientras tanto, describir la tabla como «comprobación de que la función de puntuación aplica correctamente las pérdidas», no como resultado comparativo.

<a id="g-02"></a>

### G-02 · Media · `ABIERTO` — La «auditoría independiente» de Q es un booleano del fixture

**Evidencia.** `PARTIAL_Q_AUDIT_GATED` (l. 77–85) acepta una Q `CURRENT_BUT_FALSE` si `q["independent_audit"]` es verdadero. En 4 de los 12 casos `FALSE_Q`, ese indicador está activado: son exactamente las 4 equivocadas de ese brazo.

**Consecuencia.** El brazo no modela ninguna auditoría; modela que alguien declaró que hubo una. Su mejor resultado frente a `QUALIFIED_Q` (4 frente a 12 equivocadas) es el número de casos en que el fixture desactivó el indicador.

**Acción propuesta.** Modelar la auditoría con una probabilidad de detección y un coste, o renombrar el brazo para que no sugiera un mecanismo.

<a id="g-03"></a>

### G-03 · Media · `ABIERTO` — Varios «microexperimentos» son literales, no cálculos

**Evidencia.**
- `finite_information` (l. 225–238): define dos mundos, pero las entropías salen de distribuciones escritas a mano (`[0.5, 0.5]`, `[1.0, 0.0]`, l. 229); los mundos no se usan en el cálculo.
- `FINITE_XOR_SYNERGY` (l. 331–334): la información mutua (0, 0, 1 bits) es un literal. El valor es correcto, pero no se calcula.
- `IQ03_EFFICIENCY_GAP` (l. 248–251): la brecha 20 → 45 es resta de constantes; «el servicio aumenta y la brecha aumenta» está en los datos de entrada.
- Varias entradas (naranjas, educación, ministerios, oficios, liceo) son diccionarios de etiquetas `NOT_ESTABLISHED` / `NOT_OBSERVED`: puertas de evidencia, no ensayos.

**Consecuencia.** «Doce microexperimentos» y «61 pruebas» sobreafirman. Lo que se reproduce es la tabla de valores escrita por el autor.

**Acción propuesta.** Calcular las cantidades informativas a partir de los mundos definidos (por ejemplo, entropía condicional desde la tabla de mundos) y renombrar el bloque como «ilustraciones y puertas de evidencia».

<a id="g-04"></a>

### G-04 · Media · `ABIERTO` — Factorial y ablaciones FH-C son tautológicos por construcción

**Evidencia.** `factorial_joint_information` (l. 163–174): la salida es `atomic_joint and (q_available or not proof_required)`; la conclusión «Q sin mecanismo físico no genera recursos» es la propia fórmula. `fh_c_competing_ablations` (l. 177–205): los indicadores de cada perfil se fijan a mano para producir predicciones opuestas, y el resumen lo reconoce.

**Consecuencia.** Son especificaciones ejecutables, útiles para documentar la regla, pero no pruebas de nada que no esté en la regla.

**Acción propuesta.** Etiquetarlos como especificación; si se quiere poner a prueba FH-C, el comparador tiene que poder fallar por razones que no fije el autor del caso.

<a id="g-05"></a>

### G-05 · Baja · `RESPONDIDO` (ronda 6) — PR #54 duplica parcialmente la red de #49

**Evidencia.** `network_gap` (`CEC/campaign.py`, l. 208–222) usa densa/estrella, n = 5/10/20/40, b = 10, g = 0,2, α = 0. La rejilla `network` de `CAC/sensitivity.py` (PR #54) es un superconjunto: las 8 celdas con g = 0,2 y α = 0 reproducen exactamente las de #49.

**Consecuencia.** La afirmación de #54 de que «no duplica» la campaña anterior no es exacta para esta familia; 8 de sus 88 barridos ya estaban.

**Acción propuesta.** Declarar el solapamiento o eliminar esas celdas.

<a id="g-06"></a>

### G-06 · Baja · `ABIERTO` — Recuento de fuentes «cribadas»

**Evidencia.** `build_campaign` (l. 441) informa `source_documents_screened = len(SOURCE_REGISTER["sources"])`, que hoy es 23. El número cuenta entradas del registro, no documentos efectivamente cribados.

**Consecuencia.** Se suma a la discrepancia histórica 17/19 ya señalada (N-03): hay al menos tres cifras de «documentos cribados» en el corpus.

**Acción propuesta.** Distinguir en el registro «registrado», «leído» y «usado como fuente de un caso», y reconciliar 17/19/23 en un único lugar.

---

<a id="ronda-02"></a>

## Ronda 2 — Código de PR #57 y PR #54

Rutas abreviadas: `AGR/` = `research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/agentic-ecosystem-reduction-v0.1/` (PR #57); `CAC/` = `.../studies/conscientia-additional-cases-v0.1/` (PR #54).

<a id="f-01"></a>

### F-01 · Alta · `RESPONDIDO` (ronda 6) — En v0.1 el metaprotocolo es, en código, el brazo convencional con Q equivalente

**Evidencia.** `AGR/agentic_reduction.py`, `plan_public` (l. 129 y ss.): `Q_META_PROTOCOL` y `CONVENTIONAL_EQUIVALENT_Q` recorren la misma rama (l. 144); la única diferencia es el precio (`equivalent_Q_cost`, l. 147). Las compuertas de liberación, consentimiento, autoridad y protocolo conjunto (l. 182) se aplican igual a todos los brazos que transfieren, incluidos los convencionales. En `AGR/make_cases.py` el precio equivalente por defecto es igual al de Q (0,3; l. 21 y 24); sólo AG22 lo abarata (l. 71).

**Consecuencia.** El modelo no puede producir una ventaja del metaprotocolo sobre un sistema convencional con la misma Q: por construcción empata (mismo precio) o pierde (convencional más barato). La frase «un peer convencional con Q equivalente empata o gana» no es un resultado ni un falsador superado; es una identidad del código.

**Lo que ya reconoce el PR.** `ISOMORPHISM_AND_BOUNDARY_AUDIT.md` §2 (AG-R3) admite que un sistema no agéntico con la misma Q puede ejecutar el mismo algoritmo y que el diferencial queda en parámetros no probados. El hallazgo no contradice eso: lo confirma en código y señala que la descripción del PR y la nota de revisión siguen presentando la comparación de brazos como si fuera informativa.

**Acción propuesta.** Presentar #57 como **prueba de reducción completa en v0.1** (el metaprotocolo es una parametrización de ACC), no como evaluación del metaprotocolo. Para que la hipótesis agéntica sea falsable hace falta un operador o estado que no sea un precio, con un caso pareado donde el peer convencional con igual información y permisos no pueda replicarlo (criterio 2 de la propia auditoría de isomorfismo, §3).

<a id="f-02"></a>

### F-02 · Alta · `ABIERTO` — La única vía hacia un diferencial agéntico es H5, que no está probada y además no compara arquitecturas

**Evidencia.** El overhead `h` (`overhead_resources`) es un parámetro público del mundo, común a todos los brazos (`physical_response`, l. 100). AG23/AG24 cambian `h` para todos, no para una arquitectura frente a otra.

**Consecuencia.** Aun en el mejor caso, AG23/AG24 no pueden mostrar que una arquitectura agéntica tenga menor coste de reconfiguración: el mundo cambia, no el comparador. El PR ya declara H5 «no probada»; el problema es que, tras F-01, H5 es la **única** hipótesis que sostendría el diferencial agéntico.

**Acción propuesta.** Hacer `h` dependiente del brazo (p. ej. `h_agentic`, `h_conventional`) y declarar explícitamente que la ventaja agéntica, si existe, es exactamente la diferencia de esos dos parámetros, que debe medirse fuera del modelo.

<a id="f-03"></a>

### F-03 · Media · `RESPONDIDO` (ronda 6) — Los conteos del barrido (107/14/39 de 160) son artefactos del diseño de la rejilla

**Evidencia.** `AGR/sensitivity.py`:
- l. 17: la mitad de la rejilla usa `true_rate = 0,6`, menor que `donor_marginal_rate = 1`. Ninguna transferencia puede mejorar la producción, y los brazos con información pagan su coste aunque no actúen (`plan_public`, l. 175). Resultado: A-only es ganador exclusivo **por construcción** en esas 80 celdas.
- l. 31–32: el barrido compara sólo `A_ONLY`, `Q_META_PROTOCOL` y `CONVENTIONAL_DIRECTED`; **excluye** `CONVENTIONAL_EQUIVALENT_Q`.
- Derivación analítica de las 14 victorias exclusivas de Q+meta: con `true_rate = 2`, Q (cota 1,6, tope 2) sólo propone transferir si `h ∈ {0,1; 0,25; 0,5}` y su precio está por debajo de la ganancia condicional (7 configuraciones). Gana exclusivamente sólo cuando el instrumento dirigido cuesta 3 o 5, es decir, cuando no actúa o apenas gana: 7 × 2 = 14. Coincide con el PR.

**Consecuencia.** Las cifras describen la rejilla, no el mecanismo. Con el brazo convencional equivalente incluido al mismo precio, las 14 victorias serían empates (F-01).

![Ganador por celda del barrido de #57](incremental-audit-2026-10-26/figures/F03_sweep_winners.svg)

**Acción propuesta.** No citar los conteos como resultado. Incluir el brazo equivalente en el barrido, separar las celdas sin mejora posible y reportar las regiones del espacio de parámetros (fronteras de decisión) en lugar de recuentos.

<a id="f-04"></a>

### F-04 · Media · `ABIERTO` — En el caso insignia AG01 el convencional dirigido alcanza el óptimo técnico

**Evidencia.** Con los valores por defecto (`make_cases.py`, l. 50): A-only 10; Q+meta transfiere 2 → producción 11,5, neto 11,2; dirigido (tasa medida 2,0, tope 4, coste 1,2) transfiere 4 → producción 13,5 (el óptimo técnico), neto 12,3; A completo descartado por coste (cota 5,375 < 8).

**Consecuencia.** El PR resume AG01 como «Q+meta permite 11,5 frente al óptimo técnico 13,5» sin decir que, en el mismo caso, el comparador convencional lo alcanza y le gana en neto.

**Acción propuesta.** Reportar AG01 con todos los brazos.

<a id="f-05"></a>

### F-05 · Media · `ABIERTO` — Modelo lineal y conmensurabilidad no justificada

**Evidencia.** `physical_response`, l. 100: la producción es lineal en la transferencia; el óptimo cae siempre en una esquina (0 o máximo). `score_after_plan`, l. 219: el valor neto resta el coste informacional (utilidad sintética) de la producción física.

**Consecuencia.** (a) Los puntos de la nota sobre rendimientos decrecientes y no linealidad no aplican a #57 (el propio PR lo excluye en su alcance, pero la nota no lo dice). (b) Restar utilidad de producción exige una tasa de conversión explícita; hoy está fijada implícitamente en 1.

**Acción propuesta.** Declarar la conversión como parámetro y añadir un caso con rendimientos decrecientes del receptor para comprobar que las conclusiones cualitativas sobreviven.

<a id="f-06"></a>

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

<a id="f-07"></a>

### F-07 · Baja · `ABIERTO` — Código muerto en `nonmonotone`

**Evidencia.** `CAC/campaign.py`, l. 45: la variable `loc` se calcula y no se usa.

**Acción propuesta.** Eliminarla o usarla; no afecta a resultados.

---

<a id="ronda-01"></a>

## Ronda 1 — Nota de solicitud de revisión externa

<a id="n-01"></a>

### N-01 · Alta · `ABIERTO` — Inventario incompleto
La auditoría #50 integra 11 PRs, incluidos #21 y #22; #22 añade 188 líneas a `00M_VNext`, que #47 vincula con el modelo social. La nota no los menciona, ni a los diferidos #5 y #18 (#5 es el linaje histórico de A/B/C/D, objeto del punto crítico 3), ni a #53, fusionado después.

<a id="n-02"></a>

### N-02 · Media · `ABIERTO` — Alcance de #50 sobredeclarado
#50 no audita #54 ni #57, que son posteriores. La sección E de la nota sugiere lo contrario.

<a id="n-03"></a>

### N-03 · Alta · `ABIERTO` — Limitaciones conocidas no declaradas
Los propios PRs declaran: evaluación asistida por IA sin revisión humana independiente (#50); discrepancia de procedencia 17/19 documentos cribados en #48/#49 sin reconciliar; H5 no probada (#57); 19 referencias a Google Docs pendientes de derechos/visibilidad; los 9 documentos que sustentan directamente los casos de #54 son Google Docs. La nota debe darlas de entrada.

<a id="n-04"></a>

### N-04 · Alta · `ABIERTO` — Autoría y procedencia
Buena parte del código, campañas y auditorías se ha generado con agentes (Codex aparece en #54; #50 menciona «otro bot»). La nota debe distinguir la autoría del propietario (hipótesis, modelo, IP) de lo producido con asistencia.

<a id="n-05"></a>

### N-05 · Alta · `ABIERTO` — Falta registro de afirmaciones
Se pide identificar «afirmaciones válidas» sin listarlas. Hace falta un registro H1…Hn con documento y sección.

<a id="n-06"></a>

### N-06 · Alta · `ABIERTO` — Encuadre de #57 y #54
Tras F-01 a F-06: #57 debe presentarse como prueba de reducción, no como evaluación del metaprotocolo; los conteos del barrido no deben citarse como resultado; #54 debe describirse como casos trabajados.

<a id="n-07"></a>

### N-07 · Media · `ABIERTO` — Objetivo móvil
`main` ya iba siete commits por delante del merge de #50 (`1f662a6`) al abrir esta auditoría. La nota debe fijar commits (ver tabla de arriba).

<a id="n-08"></a>

### N-08 · Media · `ABIERTO` — Siglas sin definir
ACC, 00M, UC21, DDS, HID, Q, A/B/C/D, Stage A/C. Hace falta glosario mínimo o enlace al índice.

<a id="n-09"></a>

### N-09 · Baja · `ABIERTO` — Logística y forma
Quitar el encabezado del agente; convertir el párrafo final en «Orden de lectura» (omite #40, #50, #51); añadir plazo, esfuerzo estimado, honorario, conflicto de intereses, confidencialidad, instrucciones de reproducción y formato de entrega; valorar dividir la revisión en matemático-económica (#28–#47) y experimental (#48–#57); idioma según el revisor.


<a id="ronda-07"></a>

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


<a id="ronda-08"></a>

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
| <a id="m27-01"></a>**M27-01** | Alta · ABIERTO · nuevo diagnóstico | [qualify, PR45](https://github.com/dakleyer/structural-awareness-contributions/blob/891af45a75b245082859147c0f7233cf85dd9035/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/scoped-closure-metacognition-v0.1/metacognition.py): con L=1, fuentes distintas f(0)=0 y f(0)=2 y pregunta f(1)≥1, devuelve `LOCALLY_SUPPORTED_TRUE`, [1,1]. No existe una función conjunta compatible. | Añadir una obligación de factibilidad conjunta o limitar explícitamente el significado de la cualificación local. El rechazo estricto del intervalo vacío no resuelve este caso. Prueba y control consistente en el anexo y acompañante. |
| <a id="m27-02"></a>**M27-02** | Alta · ABIERTO · conocido I-01 / D26-F01 | La tolerancia admite [1e-13,0] y una respuesta positiva; reproducción del fallo ya registrado. | Mantener el único candidato D26-C01 y sus controles en 01I VNext; agregar M27-01 como caso adicional, sin cerrar I-01 por haber preparado un parche. |
| <a id="m27-03"></a>**M27-03** | Alta · ABIERTO · conocido D26-F08 | [PR60 D3](https://github.com/dakleyer/structural-awareness-contributions/blob/29ad055e107f40bdb458995f6b473ab50fe0ea0f/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/mathematical-lineage-social-agentic-v0.1/02_FORMAL_CORE_AND_PROOFS.md) caracteriza bien Q sola; la selección suplementaria debe conservar A/o ya disponible. Cuatro mundos: seis pares totales, dos tras A; Q sola deja dos sin separar, A+Q no deja ninguno. | Mantener D3 en su alcance y usar conflictos condicionados por o para su aplicación suplementaria. Reconciliar fuente 02/03 con los anexos más recientes; candidatos D26-C04/05 ya propietarios de la propuesta. |
| <a id="m27-04"></a>**M27-04** | Alta · ABIERTO · conocido D26-F09 | PR60 05/06 mezcla la numeración nativa UC21 R0/R1/R2 con DDS prospectivo R1/R2/R3. | Distinguir nombres de espacio y preservar fallo real, reparación y predecesor aprobado; continuar D26-C06/07, sin duplicar el arreglo. |
| <a id="m27-05"></a>**M27-05** | Clarificación de fuente · confirmada | R12 enlaza a `primitiva-entropica.tex`, 10.822 bytes; el expediente ya declara el PDF temporal compilado por el revisor. El original no es un PDF histórico ni el manuscrito R11 firmado. La aplicación a certificados es una reconstrucción posterior. | Preservar la distinción TeX original / render posterior / adaptación. La fórmula espectral necesita una construcción de pesos dependiente del estado; el contraejemplo con Ω fija no debe confundirse con una refutación de toda asignación posible. No hay un nuevo fallo de MIME en el expediente que ya lo declara. |
| <a id="m27-06"></a>**M27-06** | Corrección del revisor · alegación retirada | DC-GH-01 v1.0.3 permite rutas subordinadas/opcionales y registro progresivo. La ausencia de una fila explícita no prueba por sí sola una infracción de las nuevas notas. | Se retira la inferencia de incumplimiento. Resolver identidad/propietario en la conciliación del registro; no convertir el predecesor genérico en una segunda política vigente. |
| <a id="m27-07"></a>**M27-07** | Baja · ABIERTO · procedencia | [Overlay PR57](https://github.com/dakleyer/structural-awareness-contributions/blob/553678e15e1ee3591736a4b8428abd4af4efc6fd/research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/agentic-ecosystem-reduction-v0.1/residual_cartography_stage.py): `first_capture_observer_id=None` permite regla de etapa III y salida 11,5. | Precisar si el identificador es obligatorio. Si lo es, comprobarlo; si se admite ausencia, informar procedencia incompleta y no atribuir el primer captor. El evento puede conservarse; no es una refutación de De Morgan ni de la mejora condicional. |
| <a id="m27-08"></a>**M27-08** | Baja · ABIERTO · notación | En el núcleo económico, la expresión de segunda diferencia de M0 coincide con una convención central, mientras §9 usa una atrasada y M3 otra indexación. Para n=19,q=.9: central≈0 y atrasada≈.001853. | Rotular índice y convención en cada fórmula y consumidor; no presentar la diferencia de índices como una refutación algebraica. |
| <a id="m27-09"></a>**M27-09** | Corrección del revisor · retirada la extrapolación | SA-O2, última frase de §3, abrevia una equivalencia informativa. Mi resumen la convirtió en una conclusión general; PR57 entrega la misma Q y el mismo planificador al control. Parte I §8 distingue descubrir, seleccionar, compilar y ejecutar. | Corregir la lectura del revisor y precisar aquella frase si se acepta una edición. Misma información no implica igualdad de procedimientos, coste, tiempo o adaptación. Propuesta literal acotada en el anexo. |
| <a id="m27-10"></a>**M27-10** | Alta · ABIERTO · ecuación fuente R19 | Original §4.1, ecuación (4): Ṡ=(r+q)S−qH. Para r,q,H>0, la derivada lineal es positiva y [0,H] no es invariante. | Distinguir equilibrio de estabilidad. El cambio Ṡ=q(H−S)−rS es otro modelo de realimentación; demostrar sus propiedades y volver a justificar cualquier lectura física. |
| <a id="m27-11"></a>**M27-11** | Media · ABIERTO · alcance de la ventana | Las formulaciones de ambos Semantic Window pasan de información refinada/mejor política posible a mejora de todo estimador. Una media de diez datos actuales tiene MSE=.1; mezclar noventa de otro régimen con Δ=.1 da .0181 aunque introduce sesgo. | Formular el resultado sobre políticas elegibles/óptimas o una clase de estimadores y pérdida especificada. Conservar el resultado cualificado ya utilizado por la Parte II actual. |
| <a id="m27-12"></a>**M27-12** | Media · ABIERTO · suficiencia exacta y práctica | A2 permite agrupar instancias anteriores del mismo tipo. Esa historia puede cambiar el posterior de θ de .75 a .9 frente a una sola muestra actual: la ventana contigua actual no es automáticamente suficiente respecto de toda H. | Separar representación ordenada de historia, ventana contigua, suficiencia posterior exacta y adecuación bajo tolerancia. A3 ya supone estimabilidad; no presentarla como una prueba independiente de que se dispone de suficientes muestras hoy. |
| <a id="m27-13"></a>**M27-13** | Media · ABIERTO · estabilidad del anclaje | Prop.5 y construcción multiescala: una cota de la señal primaria no da automáticamente una cota del indicador ni controla reinicios. En tiempo discreto la cota de permanencia puede ser un solo paso. | Acotar el indicador real, especificar reinicios y probar Δt≥(θon−θoff)/v. Excluir cambios en cada muestra exige una condición adicional sobre el salto máximo o permanencia mínima. |
| <a id="m27-14"></a>**M27-14** | Media · ABIERTO · D28 Prop.3 | No-inferioridad frente a inacción no prueba dominancia sobre otra acción. En dos estados: inacción=(0,0), segura=(0,1), alternativa=(−1,100). La primera es segura; la segunda tiene mayor esperanza con probabilidades iguales. | Mantener el contrato de seguridad y retirar la inferencia de dominancia entre competidores salvo hipótesis adicionales. Diferenciar esos dos criterios. |
| <a id="m27-15"></a>**M27-15** | Media · ABIERTO · D34 | Haber salido una vez de d(P0,Pt)≤ε no implica permanecer fuera. Bernoulli(.5)→Bernoulli(.7)→Bernoulli(.5), ε=.1 en variación total, sale y vuelve. | Indexar la validez por tiempo; para afirmar no retorno hace falta otra hipótesis. La pérdida y recuperación para una pregunta puntual no borra un incumplimiento histórico. |
| <a id="m27-16"></a>**M27-16** | Media · ABIERTO · D34 / R09 / D08 | λ>μ durante un episodio no implica divergencia. λ=4,μ=2 por tres unidades; λ=0 después: carga máxima 6 y cola vacía en t=6. | Separar sobrecarga persistente, episodio y plazo perdido; usar llegadas brutas y servicio en unidades comunes, y llevar ahorro contrafactual en otro balance. |
| <a id="m27-17"></a>**M27-17** | Contraste de versión · aclaración ya presente | La fuente web D37 leída ya escribe P(A)P(P∣A)=P(A∩P), explica la independencia si se sustituye una marginal y separa severidad. | No reabrir como fallo vigente la lectura abreviada anterior. Conservar versión y procedencia al reutilizar el resultado. |
| <a id="m27-18"></a>**M27-18** | Media · ABIERTO · D37 | Podar/amplificar nodos define configuraciones candidatas; no establece por sí solo atractores estables de una dinámica. | Definir campo/mapa de evolución, dominio, equilibrio y criterio de estabilidad, o mantener la descripción como hipótesis operacional. |
| <a id="m27-19"></a>**M27-19** | Oportunidad de especificación · PROPUESTA · D37 | D_i=a_i+b_ix y S_i=c_i−d_ix, o extensión cuadrática, necesitan dominio y selección de raíz para producir un precio interpretable. | Para el caso afín, x*=(c−a)/(b+d) si b+d≠0; comprobar admisibilidad, unidades y significado presión/precio. Si b+d=0 puede no haber solución o haber muchas. |
| <a id="m27-o1"></a>**M27-O1** | Desarrollo matemático · PROPUESTA | Extender R01/R04 y la Parte I a proyección de una dinámica. | Criterio DhF constante por fibra de h, con regularidad y dominio; ejemplo estable donde la observación actual deja de determinar una pregunta futura. |
| <a id="m27-o2"></a>**M27-O2** | Desarrollo matemático · PROPUESTA | Extender SA-O5 y el horizonte de R19 a adecuación aproximada. | Cota de Grönwall y envolvente exacta del ejemplo; margen de decisión y pregunta/horizonte explícitos. |
| <a id="m27-o3"></a>**M27-O3** | Desarrollo matemático · PROPUESTA | Extender la distinción de cohortes R10 y residual colectivo. | Transporte por edades: mejora individual e influjo exponencial pueden producir media residual γ/(γ+β); llegada constante produce media tendente a cero. |
| <a id="m27-o4"></a>**M27-O4** | Desarrollo de capacidad · PROPUESTA | R09/D08/D34 y balance de R05. | Cola fluida reflejada, plazos útiles y contabilidad por incidencia sin sumar dos veces el mismo flujo; mantener separadas las magnitudes físicas y de esfuerzo. |
| <a id="m27-o5"></a>**M27-O5** | Desarrollo de ventana · PROPUESTA | Semantic Window, D28 y D37. | Familia finita factible, error cualificado, coste y plazo; lema de histéresis con velocidad del indicador y tratamiento de reinicios. |

### Evidencia y siguiente acción

El [anexo §8](incremental-audit-2026-10-26/ANNEX.md#8-mathematical-review-and-development-opportunities) contiene los detalles, demostraciones internas y propuesta literal. El [acompañante estándar](incremental-audit-2026-10-26/math_audit_companion_2026-10-27.py) verifica cuatro blobs fijados y reproduce los defectos y controles seleccionados. Sus [resultados](incremental-audit-2026-10-26/MATH_AUDIT_RESULTS_2026-10-27.json) registran 32/32 comprobaciones internas; no son 32 estudios independientes.

La reproducción anterior de la primera revisión pasó 85 pruebas de PR57, seis de PR60, 65 de PR54 y 60 de PR45; los nueve programas matemáticos ejecutaron 10.062 aserciones finitas. Es una evidencia reproducible de esos cortes y ejemplos. Esta ronda no vuelve a ejecutar ni suma esos recuentos como nuevas observaciones.

Prioridad de corrección: M27-01/02, seguida de la integración M27-03/04. Prioridad de desarrollo: M27-O1/O2 como una línea conjunta de suficiencia temporal; M27-O5 para concretar ventanas; M27-O3 como línea distinta de renovación poblacional. Los cambios de fuentes y admisión DDS permanecen pendientes de sus decisiones y verificaciones propias.


<a id="ronda-09"></a>

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


<a id="ronda-10"></a>

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


---

<a id="ronda-11"></a>

## Ronda 11 — resolución técnica de I-01, delimitación de comparadores y clasificación de casos (27-10-2026)

**Recepción del propietario.** Iván Abril Palma autoriza la corrección técnica del cuarto hallazgo; solicita aclarar la premisa del quinto sin oponer artificialmente ABCD a los procedimientos convencionales; acepta reclasificar los 46 casos del sexto como ejemplos sintéticos, de manera sobria. Esta respuesta está documentada por Codex, asistente de IA; **no sustituye** validación científica independiente. Se mantienen los hallazgos y estados anteriores para conservar la secuencia.

### R11-I01/M27-01/M27-02 — Corrección de fuente propuesta en PR #64

**Nueva propuesta de implementación:** [PR #64](https://github.com/dakleyer/structural-awareness-contributions/pull/64) (draft) modifica sólo `metacognition.py`, sus pruebas y el README propietario de `scoped-closure-metacognition-v0.1`. El control estricto de `lo > hi` impide que la tolerancia absoluta `1e-12` produzca un falso `LOCALLY_SUPPORTED_TRUE` sobre un intervalo vacío (I-01/M27-02). Además, la intersección local **no es prueba de consistencia global**: para L=1, fuentes f(0)=0 y f(0)=2 generan una intersección aparente [1,1] al preguntar por x=1, pero no admiten una función conjunta. La nueva guarda contrasta desigualdades entre todos los pares elegibles antes de declarar apoyo TRUE/FALSE.

- Coordenadas exactas e intervalos de valores: la condición por pares es suficiente y necesaria para una selección finita Lipschitz-compatible, extensible al dominio bajo el supuesto de regularidad declarado.
- Coordenadas inciertas: separación mínima certifica compatibilidad robusta; separación máxima puede probar inconsistencia. Si el análisis no certifica ninguno de ambos extremos, la salida es `JOINT_CONSISTENCY_NOT_ESTABLISHED`, sin apoyo positivo/negativo ni permiso de actuar.
- **Evidencia de revisión:** 66/66 tests del módulo superados en ejecución local contra el candidato (base 60; seis nuevos), incluidos dos contraejemplos negativos y controles positivos; [Documentation integrity del head 19072ab](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/40557800724) concluyó `success`.
- **Relación con PR #59:** su D26-C01 original proponía únicamente el arreglo de tolerancia; el PR #64 es su candidato **de fuente** ampliado para la consistencia conjunta. No aplicar ambos parches como propuestas separadas ni interpretar PR #59 como incorporación al código.
- **Límites:** compatibilidad formal de testimonios elegibles en el marco finito, no autenticidad empírica de declaraciones, licitud de recursos, validez externa de L ni cierre de B/C/D.

**Estado editorial:** I-01/M27-01/M27-02 quedan `RESPONDIDO — CORRECCIÓN PROPUESTA EN FUENTE`, **no `CERRADO`** hasta revisión del propietario, comprobación CI y promoción explícita del PR #64. No se altera el estado original de las tablas por sobrescritura.

### R11-G01/F01 — El quinto hallazgo no exige un falso adversario «convencional sin ABCD»

**Rectificación de interpretación:** ACC/ABCD puede ejecutar el método convencional íntegro mientras las restricciones y la información del A operativo lo permitan. Puede además caracterizar las fronteras B/C/D relativas a la pregunta, coordinar, transferir recursos entre dimensiones **operativas realmente justificadas**, pivotar o emitir NO GO. La dimensión no se crea por conveniencia del comparador.

**El defecto auditado es local al diseño de los fixtures, no a esta capacidad arquitectónica:**

1. En `conscientia-campaign-v0.1`, 48 veredictos adjudicables del brazo `CONVENTIONAL_TARGETED` ya son correctos por estipulación del registro; `EXPANDED_A` recibe también verdad correcta en su alcance y Q concentra la inyección de ciertos errores. Los rangos calculados verifican la función de coste/pérdida para **esas entradas**; no estiman por sí mismos cuál procedimiento descubriría el veredicto, con qué información y coste total.
2. En `agentic-ecosystem-reduction-v0.1`, `Q_META_PROTOCOL` y `CONVENTIONAL_EQUIVALENT_Q` usan la misma rama decisoria salvo sus precios. Su empate o divergencia monetaria es legítimo como **control de ejecución equivalente**, pero no demuestra ni refuta un diferencial de adquisición, descubrimiento, selección, adaptación o mantenimiento.
3. Propuesta para una comparación nueva, **sin imponer resultados**: distinguir pruebas unitarias de reglas frente a contrastes entre procesos completos; fijar misma tarea, régimen, derechos, presupuesto, información inicial y acceso permitido a fuentes; dejar que cada brazo use libremente optimización/reorganización/convencionalidad donde pueda; medir qué información adicional logra adquirir legítimamente, tiempo, coordinación y costes de obtención, calidad de salida, abstenciones y fallos. Una alternativa convencional robusta que obtenga la misma Q cuenta de forma honesta como empate o ventaja convencional; no se excluye por ser convencional. Separar escenario R1 actual, R2 configurado de forma óptima y R3 contrafáctico condicionado por cambio de régimen cuando se aplique UC21/DDS, sin cambiar unilateralmente los recursos.
4. Las campañas actuales se conservan como **tests/ilustraciones bajo parámetros declarados**; no se reetiquetan como estimaciones empíricas ni se exige al programa matemático demostrar una superioridad arquitectónica universal.

**Estado:** G-01 y F-01 conservan `RESPONDIDO` en cuanto a diagnóstico del fixture y `NO CERRADO` en cuanto a capacidad comparativa integral. Cualquier estudio pareado nuevo requiere su propio diseño; aquí no se inventan resultados.

### R11-F06 — 46 casos ilustrativos con resultados reproducibles, no 46 experimentos externos

**Recepción limitada en [PR #54](https://github.com/dakleyer/structural-awareness-contributions/pull/54):** encabezados y README propietario reclasifican los 46 como **ejemplos trabajados/fixtures sintéticos ejecutables** y los 88 barridos como sensibilidad estipulada. Las 65 pruebas son de regresión. El apartado KL declara distribuciones uniformes en soporte finito para `log2(m/n)`; `closure` se mantiene como inferencia condicional Lipschitz, no validación física de su supuesto. Se conservan los 46 resultados, sus 88 barridos, fuentes, código, test y JSON sin cambios; se evita una reconstrucción innecesaria del estudio.

**Estado:** F-06 `RESPONDIDO — PRECISIÓN DOCUMENTAL EN PR #54`, no certificado como experimento externo y no cerrado hasta revisar/promover el PR. Las distinciones entre programa matemático, principios arquitectónicos y ejemplos ejecutables se señalan **sólo donde cambian el alcance de una conclusión**; no se introduce una taxonomía repetitiva o una jerarquía rígida en cada caso.

### Gate de promoción de esta ronda

Los PR #64 y #54 permanecen separados del PR #58 (registro crítico). Mantener PR #59 como seguimiento de auditoría documental y de D26-C01; al promover #64, verificar que cualquier VNext que represente D26-C01 apunte al arreglo conjunto vigente y no deje un parche competidor. No hay merge ni promoción a Canonical o main en esta ronda.


<a id="ronda-12"></a>

## Ronda 12 — relectura del corpus y estado real de la auditoría (28 octubre 2026)

**Auditoría realizada por Codex, asistencia de IA, por nueva instrucción de Iván.** Esta es una actualización de argumento, evidencia, legibilidad y pendientes sobre cambios identificados; no se atribuye revisión humana independiente ni cuatro pasadas completas de todo el corpus. Las rondas anteriores conservan su texto, atribución y fecha.

### Lo que ha mejorado y debe reconocerse

El corpus distingue ahora mejor tres trabajos que antes podían mezclarse: conservar una distinción pertinente, encontrar/recalificar una oportunidad y hacer efectivo un cambio autorizado. El nuevo puente de PR62 explica SA → EA → EP sin trasladar a EP la propiedad de DDS/UC21; su anexo desarrolla selección de restricciones, reutilización localizada, costes completos y un ciclo de aprendizaje. La parte matemática es una contribución concreta: inclusión de conjuntos factibles, determinación relativa a condiciones revisadas y separación de trabajo frente a un procedimiento exhaustivo declarado, con sus hipótesis. Su valor no desaparece porque sea programable mediante software ordinario.

PR60 ha recibido la corrección de las consultas suplementarias: mantiene el teorema Q-only y añade el problema condicionado por la observación A ya disponible. También distingue los identificadores UC21/DDS. PR57 ha añadido controles de reproducción del procedimiento Q y precio normalizado sobre las30 fichas y las160 celdas, conservando resultados originales y el beneficio físico condicionado. PR64 incorpora una reparación efectiva del código candidato para los dos ejemplos originales de intervalos y añade factibilidad conjunta. PR63 hace visible que ACC ya trata coordinación, saturación y dimensiones operativas; la pregunta de acceso a fuentes a N niveles sigue siendo un ensayo distinto. PR54 aclara el carácter sintético de sus casos.

Estas mejoras sí han ocurrido en las ramas indicadas. Sólo las precisiones S2 de PR61 y el ajuste del entorno P5 están incorporados en main en el corte de esta ronda. No se atribuye a esta recepción el merge de PR54/60/62/63/64.

### Corte y alcance que permiten comprobarlo

Main: **b7147330506b37567a7821be6f4cb2237da06bda**, comparado con el corte de ronda9 **43203858893325b9cbc1c3e3b75f72a7d35e6f1d**: seis commits y cinco archivos modificados. PR58 antes de esta ronda: **5046bbf4ac6dcbd6b7c2393929986868bb5d254d**, con las rondas10/11 y sus comentarios ya leídos. La lista de rondas se actualiza sin suprimir entradas.

| Rama revisada | Head fijado | Cambio respecto del corte anterior / base propia |
|---|---|---|
| PR54 | e225216950fb424c64acd8e7f274f5e3c7ad59c3 | Dos documentos, cinco líneas añadidas/tres retiradas; código y resultados intactos |
| PR57 | a98940490e8a84051ad314f2392c15338dbf1de9 | Cuatro archivos, 64 adiciones/una supresión; dos tests nuevos y precisión de lectura; código y JSON originales intactos |
| PR59 | 051ff62059b8652b9e0d46fa0bbb9251896ec750 | Sin avance; debe recibir los estados posteriores de los candidatos originales |
| PR60 | 3a846c6bb0fed6c25bf6deaa7af084a69ea242b5 | Doce archivos; correcciones 02/03/05/06, nueva recepción11/12 y tests; 550 adiciones/ocho supresiones |
| PR62 | f3f5e2078ba75443ea6e17ea2af9800f8d8ccec3 | Dos notas nuevas: puente y anexo de reutilización/adaptación |
| PR63 | 2193705ef13adec08068f49f355a632e4c35f450 | Tres documentos vivos; 17 líneas añadidas sobre H-01/H-03 |
| PR64 | 0229bf9439be8459680dce4f7fe0376a9cd31306 | Fuente, tests y README; 106 adiciones/dos supresiones |

Inventario diferencial: **32 archivos/ediciones** entre main y esas seis ramas cambiadas. Se hizo lectura focal de las unidades matemáticas y ejecutables afectadas, del registro completo de rondas y de los 15 comentarios de PR58; PR58 no tiene hilos de revisión inline en este corte. Se recibió el avance concurrente de57/64 antes de publicar: en64 se añadieron un control de falso FALSE y un positivo conjunto; metacognition.py no cambió y conserva los contraejemplos M28-01. En57 los tests normalizan precio y verifican reproducción del procedimiento compartido; no son dos procesos de adquisición independientes. El índice de [cortes y cambios](incremental-audit-2026-10-26/CORPUS_REFRESH_SCOPE_2026-10-28.json) conserva los paths exactos. Los PR5/18/56/59 mantienen sus heads anteriores. Esto no convierte sus fuentes en una nueva auditoría integral.

### Verificación nueva y lo que realmente dice

- **PR64: 68/68 tests; PR60: 30/30; PR54: 65/65; PR57: 87/87.** Ejecutados sobre las fuentes fijadas. El informe sintético de PR64 coincide por contenido con su JSON de referencia. Son pruebas de regresión finitas, no 250 experimentos ni medidas de eficacia.
- El acompañante de esta ronda reproduce **23/23 comprobaciones**, con tres blobs verificados, tanto desde las copias exactas como descargando los fuentes fijados. Incluye los fallos nuevos, controles favorables y dos cálculos independientes; encontrar el fallo hace pasar la comprobación diagnóstica, no corrige la fuente.
- **Pendiente técnico P5/Python3.9 actualizado:** el trabajo real en main [terminó correctamente](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/40546671257/job/122339003753) después de fijar Ubuntu24.04. Los trabajos 3.12/3.13 y la campaña379 también terminaron correctamente en ese mismo run. La incidencia del entorno está resuelta en el sucesor; el fallo histórico de PR22 sigue conservado. Esto no cierra la revisión sustantiva de 00M.
- Los checks de integridad de [PR64](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/40557800724/job/122378430135) y [PR60](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/40557663048/job/122377936718) pasan. Los contraejemplos siguientes muestran por qué ese PASS no basta para cerrar la corrección matemática.

### Nuevos hallazgos y mejoras, con alcance concreto

| ID | Estado / prioridad | Qué ocurre y por qué importa | Próxima unidad concreta |
|---|---|---|---|
| <a id="m28-01"></a>**M28-01** | ABIERTO · alta · precisión numérica del candidato64 | Con ε=2^-54, x0=0,y0=1; x1=1,y1=-ε y L=1, la desigualdad exacta se viola en ε; la resta flotante redondea 1+ε a1. La guarda devuelve CONSISTENT y qualify certifica TRUE en x=0. Además, con un único dato f(0)=1 y L=ε, el límite inferior en x=1 es exactamente 1-ε<1, pero el código lo redondea a1 y certifica TRUE para umbral1. | Dos regresiones explícitas. Usar aritmética exacta sobre los números representados, o intervalos con redondeo dirigido y abstención cuando no hay certificado; cubrir tanto factibilidad como decisión, no sólo la nueva guarda. No cerrar I-01 por68 tests. El lema Lipschitz exacto permanece válido. |
| <a id="m28-02"></a>**M28-02** | ABIERTO · media · dominio de la guarda60 | DOMAIN=0..9; full_verdict(12) rechaza por estar fuera del dominio. guarded_verdict(12, proof_scope=DOMAIN, guard_validated=True) devuelve REJECT y omite la evaluación: confunde «certificado para D» con «este x pertenece a D». | Comprobar pertenencia antes de usar la guarda y añadir controles fuera del dominio. Corregir el pequeño fixture, sin atribuir el fallo a un monitor RA real que no está implementado. |
| <a id="m28-03"></a>**M28-03** | ABIERTO · media · cota de utilidad60 | assess_candidate acepta NaN e infinito como source_value_lower_bound y produce una propuesta de acción externa porque la comparación <= no los descarta. El fixture mantiene execution=NEVER: no hay una actuación no autorizada ejecutada. | Validar tipo y finitud de la cota antes de comparar, preservar UTILITY_NOT_ESTABLISHED para una cota no válida, y probar NaN/±∞/booleanos. No convertir un campo inválido en certificado positivo. |
| <a id="m28-04"></a>**M28-04** | PROPUESTA · media · tiempo de uso60 | requalify sólo compara caducidad con la fecha antigua del evento y no recibe la fecha de decisión. El caso positivo a t=1 con caducidad3 no comprueba una reevaluación en t=10. | Declarar si se prueba validez histórica o validez al uso. Para esta última, pasar tiempo de decisión y comprobar vigencia allí, con límite inclusivo/exclusivo explícito. No se afirma un fallo desplegado; es una obligación temporal que el fixture todavía no representa. |
| <a id="m28-05"></a>**M28-05** | ABIERTO editorial · prevención de extrapolaciones | Dos tests nuevos llaman dos veces a la misma función y los nombran como comparación con un peer fuerte. PR62 §13.3 y PR60 §11 vuelven a abreviar reproducción/capacidad de implementar como conclusión de igualdad. El método, la adquisición y los costes no quedan comparados por esos nombres. | Seis fichas nuevas IP37–42 en el anexo: describir reproducción determinista con procedimiento suministrado y afirmar primero el resultado positivo pertinente. Mantener las pruebas y controles adversos reales. |
| <a id="m28-06"></a>**M28-06** | RECIBIDO en esta ronda · estado y navegación | La cabecera conservaba pendientes anteriores a las respuestas10/11; el registro de rondas acababa en9 y seguía pendiente el entorno3.9 ya resuelto. PR59 conserva candidatos previos a los cambios de60/64. | Panel vigente, filas10/11/12 y esta matriz. En PR59, recibir C04–07 como aplicados en la rama60, con revisión/promoción aún pendientes; hacer que C01 remita al candidato conjunto64 y su nuevo problema numérico, sin dos parches competidores. |
| <a id="m28-07"></a>**M28-07** | PROPUESTA · baja · higiene del acompañante8 | El comentario del27Oct señala que math_audit_companion sin --output reescribe su JSON versionado y crea caché dentro del paquete. El código conserva ese comportamiento. No se ha ejecutado aquí sobre su referencia sin destino. | Salida por defecto a stdout, destino explícito creado sin sobrescribir y caché temporal. El acompañante nuevo de esta ronda ya sigue esa pauta; el antiguo necesita su propia corrección acotada. |
| <a id="m28-o1"></a>**M28-O1** | DESARROLLO PROPUESTO · positivo | CA-1 reconoce un ahorro cuando ya se supone C_SEL<C_EXH; CA-4 sí deriva una separación asintótica frente a la rejilla exhaustiva bajo hipótesis cuantitativas. Conviene convertir el rendimiento del selector en obligación medible. | Lema de coste esperado con selección y retorno exhaustivo: E[C]≤h+D-p(D-s), ahorro si h<p(D-s), con p cualificado, costes comunes y misma tarea. Demostración y controles en el anexo; no se atribuye un p real ni una mejora general. |
| <a id="m28-o2"></a>**M28-O2** | DESARROLLO PROPUESTO · continuidad temporal | El ciclo de aprendizaje/contexto de62 da un receptor concreto a M27-O1/O2/O5. Cambiar ventana o reglas cambia también la representación cuya suficiencia se evalúa. | Modelo híbrido con versión de contexto, flujo, saltos de contrato y reloj de caducidad; demostrar suficiencia/error entre saltos y revalidar al cambiar de versión. No declarar estabilidad/convergencia a partir de una interfaz Update. |

[Detalles, contraejemplos y propuestas literales](incremental-audit-2026-10-26/ANNEX.md#10-corpus-refresh-and-open-audit-work--28-october-2026) · [Acompañante](incremental-audit-2026-10-26/refresh_audit_companion_2026-10-28.py) · [Resultado](incremental-audit-2026-10-26/CORPUS_REFRESH_CHECKS_2026-10-28.json).

### Estado actualizado de mis observaciones anteriores

| Observación | Disposición vigente al28Oct | Qué falta exactamente |
|---|---|---|
| M27-01/02; I-01; D26-C01 | Los dos casos originales están reparados en el candidato64; el parche de sólo tolerancia de59 ya no es suficiente como candidato completo | M28-01, regresiones/certificación numérica y revisión del candidato64; después decisión de incorporación y recepción en01I |
| M27-03; D26-C04/05 | **Aplicado en la rama60:** D3-A condicionado por A en02 y consumidor03. Contraejemplo de cuatro estados comprobado de nuevo | Revisión de integración y promoción propia; no volver a ofrecer el antiguo par como si siguiera sin aplicar allí |
| M27-04; D26-C06/07 | **Aplicado en la rama60:** separación de nombres UC21/DDS en05/06 | Recepción de estado en59; revisar fuente y consumidores al incorporar, sin volver a mezclar los nombres en resúmenes |
| M27-05 | Clarificación de procedencia ya registrada | Contraste completo del original/edición R12 cuando se pretenda reutilizar su física; no inventar un error MIME actual |
| M27-06 | Alegación de navegación retirada | Mantener la rectificación; registro progresivo no equivale a infracción automática |
| M27-07 | Sigue abierto; el avance57 sólo modifica docs y tests | Contrato de first_capture_observer_id y prueba de ausencia; los nuevos tests57 y la rama60 no modifican aquel código |
| M27-08 | Sigue abierto; fuente económica sin cambio en este corte | Elegir y rotular convención de segunda diferencia y revisar consumidores, preservando fórmulas históricas |
| M27-09; IP01–36 | Propuesta transversal publicada, no incorporada a las fuentes. Autor de F01/F02/anexo acepta IP30–32 en comentario | 36 unidades ANTES siguen presentes; 29 mantienen blob exacto, siete cambian de blob pero conservan el pasaje. Las dos fichas de referencia ya eran correctas. Seleccionar/recibir las34 operaciones reales; extender con IP37–42 |
| M27-10 | R19 sigue abierto en el alcance histórico auditado | Modelo de realimentación justificado, invariancia y estabilidad; no nueva lectura íntegra de ese original en esta ronda |
| M27-11/12/13 | Semantic Window: alcance estadístico, historia suficiente e histéresis siguen abiertos | Clase de estimadores/pérdida, recurrencia de régimen, indicador realmente acotado y reinicios. La ParteII cualificada no se invalida por la fuente histórica |
| M27-14 | D28 sigue abierto en su inferencia de dominancia | Separar seguridad frente a inacción y comparación entre acciones; conservar el contrato de seguridad |
| M27-15/16 | D34/R09/D08: retorno de región y sobrecarga transitoria siguen abiertos | Hipótesis temporal para no retorno; carga reflejada y plazos, sin confundir episodio con divergencia |
| M27-17 | Aclaración ya presente, no defecto activo | Mantener versión y no reabrir una abreviatura histórica como fallo actual |
| M27-18/19 | D37: dinámica de atractores y dominio/precio siguen abiertos/propuestos | Campo o mapa de evolución y estabilidad; dominio, unidades y selección de raíz |
| M27-20 | Recibido en el comentario de ronda8; no corregido en el original | Distinguir mapas/cuántificadores de Cantor, representación y computabilidad. Las notas actuales no dependen del salto universal |
| M27-O1/O2/O5 | Desarrollo preparado en el anexo8; receptor nuevo en el ciclo62 | Línea conjunta de suficiencia temporal, error y cambios de ventana; M28-O2 concreta siguiente entregable |
| M27-O3 | Renovación poblacional, línea distinta | Precisar dinámica de entradas/cohortes y observabilidad; no inferir mejora poblacional de la individual |
| M27-O4 | Capacidad y cola, línea distinta | Modelo de llegadas/servicio/plazo y contabilidad sin doble conteo |

La revalidación de IP01–36 es **literal y contextual acotada**, no una prueba de que ya no habrá errores de lectura. [Resultado por ficha](incremental-audit-2026-10-26/IP_REVALIDATION_2026-10-28.json). Los comentarios de aceptación y las rondas10/11 mejoran la interpretación, pero no autorizan a declarar aplicados todos los reemplazos. Esta actualización tampoco vuelve a resumir el corpus mediante una igualdad global entre arquitecturas.

### Pendientes completos del registro compartido

| Familia / IDs | Estado que corresponde conservar | Entregable o decisión que permite avanzar |
|---|---|---|
| **N01–N09**, nota inicial de solicitud externa | Abiertos respecto de aquella nota; no se ha recuperado una nueva edición de la nota privada en esta ronda | Reconciliar inventario, alcance50, autoría/procedencia, matriz de afirmaciones, siglas y encargo/plazo/honorarios/conflictos. No inferir cierre porque un documento posterior contenga uno de esos elementos |
| **F01 / G01** | Respondidos en6/11; controles locales de ejecución y entradas estipuladas | Proceso prospectivo completo si se pretende estudiar adquisición/adaptación. Mantener resultado matemático y uso convencional pleno dentro de ACC |
| **F02** | Abierto y **encabezado históricamente sobre-generalizado**, como acepta su autor en IP31 | Disposición contextual visible: la frase sobre H5 sólo describe el fixture57. Aplicar la corrección aceptada en su unidad propia cuando se seleccione; no trasladarla al programa matemático |
| **F03** | Respondido; el barrido histórico sigue exacto y la rama57 añade el control equivalente-Q/precio en sus160 celdas | Recibir el nuevo test como control complementario del procedimiento, preservando el JSON original; el grid sigue sin estimar prevalencias |
| **F04 / F05** | Crítica local AG01 y modelo lineal/conmensurable siguen abiertas | Comparar escenarios con mismas restricciones y horizonte; justificar agregación. El overlay posterior no reescribe el óptimo13,5 del original |
| **F06** | Precisado en documentos de la rama54, recibido en11 | Revisar/promover esa edición y sincronizar su presentación; 46 fixtures/88 barridos no son estudios empíricos |
| **F07** | Abierto | Retirar o activar justificadamente la rama muerta de nonmonotone con comparación de resultados |
| **G02 / G03 / G04** | Abiertos | Comparador observacional sin verdad del referee; microejemplos realmente calculados cuando se alegue cálculo; factorial con mecanismos/fallos no impuestos por la regla generadora |
| **G05 / G06** | G05 respondido; solapamiento y denominadores de fuente sin cierre | Declarar ocho celdas reutilizadas y reconciliar17/19 cribados con identidad/versión; reutilización no equivale a replicación independiente |
| **H01 / H03** | Abiertos sólo para el ejemplo ejecutable; precisión de alcance en10 y candidato63 | H01: si se mantiene «racional», juego/incentivos adecuados o rótulo de bloqueo factible. H03: ensayo nuevo de profundidad/acceso; no volver a pedir coordinación como ausente del ACC integrado |
| **H02 / H04 / H05** | Abiertos en sus afirmaciones/modelos concretos | Derivar o medir brecha por enlace; separar brecha operacional y experiencia vivida; justificar utilidad no monótona. Ningún cambio de etiqueta sustituye evidencia |
| **H06** | Verificado dentro de hipótesis finitas | Conservar la cota positiva; no reabrirla porque otras afirmaciones carezcan de datos |
| **I01** | Candidato64 revisado y tests originales reparados; sigue abierto por M28-01 | Solidez numérica antes del cierre; después recepción y promoción explícita |
| **TAX26-01…09**, reparación de cita SA-U2, D26-C02/03 | Propuestas preparadas; no aplicadas en este corte | Selección concreta; TAX26-02/04 siguen primera ola documental pequeña. Mantener un propietario por fuente |
| **D26-C04…07** | Cambios recibidos en rama60 | Actualizar estado del registro59 antes de una aplicación repetida |
| **Cobertura #44–46** | Auditoría sustantiva general pendiente; el parche de qualify no la completa | #44: balance y frontera de costes; #45: resto de funciones/contratos; #46: mecanismos/controles causales y lectores |
| **Cobertura núcleo #28/#40/#51, #21/#22, diferidos #5/#18** | Pendiente dentro de la auditoría compartida, aunque varios PRs ya estén fusionados | Leer unidad lógica/edición, argumentos y consumidores; «pendiente de auditar» no significa «pendiente de merge». La incidencia3.9 sí tiene sucesor ejecutado correcto |
| **PR57 extensión / PR60 integración** | La lectura anterior y las pruebas nuevas cubren partes distintas | Completar linaje/originales, profundidad/acceso y ensayo real Theme18 con RA, fuentes, recepción y límites de autorización |
| **PR62** | Puente y resultados condicionales de investigación, sin promoción | Cualificar selector y coste; algoritmo Update efectivo/ensayo futuro; matriz de madurez M1–M8 con evidencias. Licencia/alcance futuro y ruta de incorporación son decisiones separadas del examen matemático |
| **Control documental / evidencia externa** | Registro lógico y salvaguardas nativas siguen su programa separado | No convertir PASS de integridad en cierre de clasificación, derechos sobre fuentes, revisión científica externa o validación de las hipótesis |

### Orden de trabajo recomendado

1. **Solidez de certificados:** M28-01 en64 y dominio/cota/tiempo en60. Son cambios pequeños de alcance y verificables; las propuestas exactas están en el anexo.
2. **Recibir lo ya cambiado:** C04–07 en rama60, precisión54/63, éxito3.9 y aceptación IP30–32. Evita que otro revisor repita diagnósticos ya contestados o aplique un parche antiguo.
3. **Prevenir el error de interpretación en la fuente:** seleccionar fichas IP y sincronizar tests, tablas, resúmenes y lectura de los nuevos anexos. La regla viaja con la afirmación; no añadir una reserva global automática a cada resultado.
4. **Fortalecer matemática operativa:** coste esperado del selector, suficiencia temporal del ciclo62 y validación de indicadores/caducidad; conservar renovación poblacional y cola como líneas distintas.
5. **Completar la auditoría de fondo pendiente:** leer las familias de la tabla anterior por unidad lógica y registrar las cuatro pasadas efectivamente realizadas, sin simular independencia ni cerrar por volumen de tests.

Esta ronda publica revisión y propuestas en el **mismo PR58**. No incorpora código en64/60, no aplica las fichas a las fuentes científicas, no fusiona ramas ni modifica main. Las nuevas regresiones se presentan como criterios de reparación; no como una implementación que ya haya pasado sus pruebas.


<a id="ronda-13"></a>

## Ronda 13 — reconfirmación de I-01 / M27-01 / M28-01 en `main` (28-10-2026)

**Auditor:** Claude, asistencia de IA, a petición de Iván. Es una reconfirmación técnica por un segundo revisor de IA, **no** una validación humana independiente.

**Objeto:** `main` en [`51fc686`](https://github.com/dakleyer/structural-awareness-contributions/commit/51fc686f45b6ef10c53b69f4c26d0e381b007ff8), fusión de [PR #64](https://github.com/dakleyer/structural-awareness-contributions/pull/64) (`Fraction` exacto en factibilidad conjunta, envolvente y umbral; abstención ante rango irrepresentable).

**Comprobado en ese commit:**

| Comprobación | Resultado |
|---|---|
| Suite `test_metacognition.py` | 72/72 |
| Salida de `metacognition.py` frente a `REFERENCE_SYNTHETIC_RESULTS.json` | Idéntica |
| I-01: [1e-13] y [0], L = 0, umbral 5e-14 | `EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT` (antes `TRUE`) |
| M27-01: f(0)=0 y f(0)=2, L = 1, f(1) ≥ 1 | `EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT` (antes `TRUE`) |
| M28-01 caso 1: (0, 1) y (1, −2⁻⁵⁴), L = 1, x = 0, umbral 1 | `EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT` (antes `TRUE`) |
| M28-01 caso 2: f(0)=1, L = 2⁻⁵⁴, x = 1, umbral 1 | `UNDETERMINED_FROM_AVAILABLE_EVIDENCE` (antes `TRUE`) |
| Control positivo: f(0)=1, f(1)=2, L = 1, x = 0,5, umbral 1,25 | `LOCALLY_SUPPORTED_TRUE` (se conserva) |
| Fuzz de 20 000 casos con coordenadas exactas frente a un oráculo racional exacto (factibilidad por pares, necesaria y suficiente; envolvente ajustada), incluyendo L y diferencias de 2⁻⁵⁴ | 0 certificados `TRUE`/`FALSE` incorrectos; 0 inconsistencias no detectadas |
| De esos casos, los 6 523 exactamente decidibles | 0 abstenciones o respuestas distintas: la corrección no se vuelve más conservadora de lo necesario |

Reproducción: [`reconfirm_I01_2026-10-28.py`](incremental-audit-2026-10-26/reconfirm_I01_2026-10-28.py) `<ruta al estudio en 51fc686>`. No escribe archivos.

**Disposición:** I-01 pasa a `CERRADO`. M27-01 y M28-01 (registros de Codex) quedan reconfirmados como corregidos en `main` con las mismas pruebas. El fuzz cubre coordenadas exactas; para coordenadas inciertas se mantiene la abstención `JOINT_CONSISTENCY_NOT_ESTABLISHED` verificada en la ronda 11, que es conservadora y no se ha medido aquí su completitud. El cierre se limita a la solidez numérica de este runner sintético: no autentica fuentes, no valida el exterior B/C/D ni convierte el certificado local en decisión. M28-02 a M28-04 (#60), F/G/H e IP37–42 siguen en sus estados.


<a id="ronda-14"></a>

## Ronda 14 — revisión formal del expediente y guía de lectura (28-10-2026)

**Auditor:** Claude, asistencia de IA, a petición de Iván. **Objeto:** la forma del propio expediente (este archivo, su anexo y la guía de comparaciones de la ronda 9) en `a58e10b`, no el contenido científico de los estudios. **Propósito:** que una persona no especialista pueda saber qué está abierto, qué está cerrado y dónde leer cada cosa.

**Entregable:** [Guía de lectura](incremental-audit-2026-10-26/GUIA_DE_LECTURA.md), con resumen de 30 segundos, autoría por ronda, panel de estado con figura y tabla, anatomía de un hallazgo, seis ideas clave con comparaciones cotidianas, el recorrido completo de I-01, una tabla de alias, el camino de cierre, rutas de lectura por perfil, el mapa de rondas, los registros uno por uno y un glosario llano. El registro de estados ([`STATUS_LEDGER_2026-10-28.json`](incremental-audit-2026-10-26/STATUS_LEDGER_2026-10-28.json)) y las figuras se regeneran con [`reader_guide_build.py`](incremental-audit-2026-10-26/reader_guide_build.py), que además comprueba identificadores y enlaces.

| ID | Gravedad · estado | Qué ocurre | Qué se ha hecho / qué falta |
|---|---|---|---|
| <a id="j-01"></a>**J-01** | Media · `RESPONDIDO` | La «lectura vigente» de la cabecera seguía diciendo que PR #64 conservaba un problema numérico, ya resuelto en la ronda 13. | Nueva cabecera vigente; la anterior se conserva marcada como previa. Falta que otro revisor lo confirme. |
| <a id="j-02"></a>**J-02** | Media · `RESPONDIDO` | El estado vigente no se puede leer en los encabezados: conservan el estado histórico (F-06 dice `ABIERTO` y la ronda 11 lo pasó a respondido; las filas M27-01/02 y M28-01 dicen `ABIERTO` y la ronda 13 los cerró). | Registro de estados con la ronda que fijó cada uno y panel en la guía, sin reescribir encabezados. |
| <a id="j-03"></a>**J-03** | Media · `RESPONDIDO` | Las anclas de los hallazgos dependían del texto del estado (`#f-01--alta--respondido-ronda-6--…`); cada cambio de estado rompía los enlaces externos. | 74 anclas estables añadidas sin cambiar texto: `#f-01`, `#m27-10`, `#ronda-07`, etc. Las anclas antiguas siguen funcionando. |
| <a id="j-04"></a>**J-04** | Baja · `RESPONDIDO` | Las rondas aparecen en orden 6, 4, 3, 2, 1 y después de la 7 a la 13; la 7 no tiene título «Ronda 7» y está en inglés, y la 5 sólo existe en el anexo. | Mapa de rondas ordenado en la guía (§10) y ancla `#ronda-07`. No se reordena el archivo. |
| <a id="j-05"></a>**J-05** | Baja · `RESPONDIDO` | Hay más de diez prefijos de identificadores, y un mismo defecto recibe hasta cinco nombres (I-01 = D26-F01 = M27-02; M27-01 y M28-01 lo amplían). Riesgo de contarlo varias veces. | Tabla de alias y de prefijos en la guía (§7). |
| <a id="j-06"></a>**J-06** | Baja · `RESPONDIDO` | La cabecera declaraba cuatro estados y las rondas usan al menos siete, con variantes. | Vocabulario de siete estados en la cabecera y explicado en la guía (§3). |
| <a id="j-07"></a>**J-07** | Baja · `ABIERTO` | El expediente mezcla español e inglés (la ronda 7 y las secciones 7–10 del anexo están en inglés). | Decisión del propietario: fijar un idioma o añadir un resumen en el otro. No se traduce aquí para no alterar textos de otros autores. |
| <a id="j-08"></a>**J-08** | Informativo · `VERIFICADO` | Enlaces internos y versiones fijadas. | 0 anclas locales rotas en la auditoría, el anexo, la guía de comparaciones y la guía de lectura; los 15 enlaces a archivos en commits fijados resuelven a archivos existentes. |

**Límites:** revisión de forma, no de contenido científico. Los estados del registro resumen las decisiones ya escritas en las rondas 1–13; esta ronda sólo añade los estados de J-01 a J-08. No cambia ningún texto de hallazgo, código, resultado ni otro PR.


<a id="ronda-15"></a>

## Ronda 15 — reconfirmación de M28-02 en la rama de PR #60 (28-10-2026)

**Auditor:** Claude, asistencia de IA. No es validación humana independiente.

**Objeto:** commit [`cb72bb65`](https://github.com/dakleyer/structural-awareness-contributions/commit/cb72bb65ab148de1c7396d9cb8f9c1b7af6edc25) de PR #60, `test_theme18_online_context.py`. La comprobación de pertenencia al dominio entero `0..9` va ahora antes del atajo de la guarda y también en la evaluación completa.

**Comprobado:**

| Comprobación | Resultado |
|---|---|
| Suite del fichero | 15/15, incluidas tres regresiones nuevas |
| x = 12 con prueba validada y `proof_scope = DOMAIN` | Lanza «outside qualified domain»; ya no devuelve `REJECT` con el atajo |
| Barrido adversarial: 27 entradas (−3…14, `True`, `False`, `2.0`, `9.0`, `1e9`, `-0.0`, `NaN`, `'2'`, `None`) × prueba válida o no × tres alcances de prueba (0..9, 0..5, 0..12) = 162 combinaciones | 0 violaciones: ninguna entrada fuera del dominio produce veredicto; todas las de dentro coinciden con la evaluación completa; el atajo sólo se usa con prueba válida de alcance exacto `0..9` |

**Disposición:** M28-02 pasa a `RESPONDIDO`: implementado en la rama de #60 y reconfirmado, pendiente de incorporarse a `main`. Se cerrará cuando #60 entre en `main` con este cambio. La corrección aplica el principio de que un certificado vale para su alcance y no más allá; no dice nada sobre la eficacia de un monitor desplegado. M28-03 y M28-04 mantienen su estado. Guía y registro de estados actualizados.



<a id="ronda-16"></a>

## Ronda 16 — cambios nuevos, cierres reconfirmados y desarrollo de cinco mecanismos (28-10-2026)

**Auditoría realizada por Codex, asistencia de IA, por nueva instrucción de Iván.** Relectura incremental después de la ronda12, recibiendo también las rondas13–15 publicadas durante este trabajo. Se continúa el mismo PR58 y se conserva la guía de lectura creada por Claude. Es un examen focal de cambios y sus consumidores, no una auditoría integral nueva ni revisión humana independiente.

### Qué ha avanzado realmente

**Reconozco como corregidos mis hallazgos I01/M27-01/M27-02/M28-01 en el alcance numérico del runner de main51fc686.** El arreglo usa racionales exactos para factibilidad, envolvente y umbral, y redondeo exterior para presentar las cotas. He reejecutado72/72 pruebas y el comprobador de la ronda13:20.000 casos, cero certificados incorrectos,6.523 casos decidibles sin abstenciones adicionales. Los cuatro adversarios publicados y el testigo decimal de59 ya no producen el certificado falso. El positivo f(0)=1,f(1)=2,L=1 sigue apoyando f(0,5)≥1,25 con[1,5;1,5]; el informe sintético permanece igual. Se mantiene el cierre limitado que ya registró Claude; no conservar esos casos en mi cola de reparaciones pendientes.

**M28-02 también está corregido y reconfirmado en la rama60, todavía fuera de main.** El commitcb72bb65 comprueba dominio entero antes de la guarda y de la evaluación completa; rechaza también alias booleanos/flotantes. He ejecutado33/33 pruebas del paquete, incluidas15 del fichero afectado, y repetido el adversario x=12 y controles de dominio. Mantener RESPONDIDO hasta incorporación, de acuerdo con la ronda15. M28-03(NaN/infinito) y el contrato temporal M28-04 siguen pendientes en su propio alcance.

PR59 ya recibió las unidades técnicas de la ronda12 en la única01I VNext, con impacto/riesgo/esfuerzo, y retiró C01 de la cola de implementación al incorporarse64. D26-C04–07 figuran aplicados en la rama60. La recepción final de59(a3326843) ya retira también M28-02 de implementación: quedan siete unidades técnicas sin aplicar. Su propuesta D28-C03 distingue correctamente los alias de hallazgos relacionados: la tabla ayuda a navegar y el cierre no se transporta automáticamente entre registros distintos. No duplicar esta propuesta. Esa recepción era un pendiente de mi ronda12 y ahora está hecha. No volver a ofrecer el parche parcial de tolerancia como una alternativa al arreglo integrado.

PR62 añadió§15: **cinco funciones intercambiables** para búsqueda de cambios de arquitectura: preselección estructural; mapa local de indeterminación con denominador; composición no fungible de posiciones; verificación acotada y gradiente/ACC; y RA independiente. Se distingue su objetivo de cambiar interfaces/roles/dependencias frente a ajustar parámetros de una arquitectura fija. Esta separación hace más claras las preguntas y pruebas de cada contribución, sin reemplazar los ocho propietarios de módulos EP.

### Corte y lectura realizada

| Fuente | Corte leído | Alcance efectivo |
|---|---|---|
| main / PR64 fusionado |51fc686f45b6ef10c53b69f4c26d0e381b007ff8| Tres archivos numéricos modificados; código, tests, lectura de README y referencia intacta |
| PR58 |a02f2d3180cd4ceb00cdc38e1224ba3cdd5f7872| Rondas13–15, guía, registro, herramientas y comentarios; se distingue main heredado de la nueva revisión |
| PR59 |a3326843aa9822b1d7a4c774531fc51818300125| Cuatro archivos de revisión con deltas nuevos: EP,01I,DDS y auditoría documental; siete propietarios en su diff contra main, tres sin cambio nuevo respecto del corte anterior |
| PR62 |4421ff535f9b6c3d70f34882e505af35924f234c| Dos notas; nueva§15 y recepción en el puente |
| PR60 |cb72bb65ab148de1c7396d9cb8f9c1b7af6edc25| Reparación de dominio; restantes fixtures y preguntas separadas |

No atribuir los cambios de main recibidos como segundo padre de un PR de revisión a su autoría ni a una nueva aplicación de aquella revisión. Las fuentes históricas y rondas anteriores conservan su alcance. El registro y los hashes del acompañante fijan qué código se comprobó.

### Dictamen sobre la matemática nueva y próximos entregables

La inclusión de conjuntos al retirar una condición y la determinación relativa a una nueva regla conservan su demostración condicionada. La ventaja de trabajo frente a la rejilla completa de§13 también conserva sus hipótesis y procedimiento de referencia. §15 es, además, una **hipótesis arquitectónica y un protocolo de evaluación**: su aportación actual consiste en separar funciones, contratos y resultados a medir. No hace falta que cada primitiva sea nueva para investigar su integración; sí hace falta identificar el incremento comprobado y su receptor.

1. **Coste del selector / M28-O1:** concretar la cautela ya escrita en FA-4. Coste medio condicionado al éxito compara subconjuntos distintos, incluso con la misma tasa de éxito. En100 tareas, A tiene50 éxitos de coste1 y50 fallos de coste100; B tiene50 éxitos de coste10 y50 fallos de coste1. El coste sobre éxitos favorece A(1<10), pero el coste completo favorece B(50,5>5,5). Propuesta: medir éxito, coste de todos los intentos y tiempo truncado hasta certificado en tareas pareadas; no declarar esto una refutación de CA-4. La fuente ya exige incluir fallos: la ficha hace esa exigencia explícita en la fórmula.
2. **Composición no fungible / H06 y§15.3:** un control clásico XOR concreta la diferencia entre duplicar una fuente y complementarla. Cada fuente deja1bit sobre la pregunta; dos copias conservan1bit, pero la pareja complementaria deja0. Las tasas locales de UNKNOWN son iguales. Añadir alcance/versiones/permisos como controles separados. Es una ilustración matemática útil para probar el módulo, no una implementación de MSCA privado ni un teorema nuevo de información.
3. **Comparación de mecanismos / F01-G01:** fijar quién proporciona etiquetas de consultas, ejemplos negativos, hipótesis, condición inicial segura y mutaciones permitidas, contando su coste. La bibliografía reúne métodos con contratos diferentes; un adaptador no disponible se declara como límite de aplicabilidad y no como fracaso de aquel método.
4. **Suficiencia temporal / M28-O2:** sigue abierta la propuesta del modelo híbrido del anexo10. Añadir§15 y RA no demuestra por sí solo estabilidad, vigencia al uso ni aprendizaje. El siguiente artefacto debe definir flujo, cambio de versión, dato que cruza el cambio y cota/error relevante para la pregunta.

Estas son concreciones de líneas y controles ya abiertos, no cuatro defectos científicos nuevos. Los ejemplos finitos se reproducen en el [acompañante16](incremental-audit-2026-10-26/recheck_corpus_round16_2026-10-28.py) y sus [resultados](incremental-audit-2026-10-26/ROUND16_RECHECK_2026-10-28.json):23 comprobaciones, cuatro blobs fijados. La copia local y la descarga pública dan el mismo contenido. Los diagnósticos aún abiertos pasan precisamente al reproducir el comportamiento pendiente; el PASS del acompañante no los repara.

### Revisión de las propuestas y de la lectura

La guía nueva mejora la consulta: estados, alias y anclas estables hacen visible el cierre. J01–J06 ya tienen esa respuesta documental; no se vuelven a denunciar como carencias sin atenderla. Mantengo la misma estructura y sus estados. La cronología dibujada sigue siendo el corte de15 rondas; esta ronda se enlaza como suplemento.

La recepción59 también identifica trabajo restante de mis fichas:33 rutas siguen genéricas y el registro original no tiene valoración individual de impacto/riesgo/esfuerzo. Eso limita su preparación para incorporar, no el valor de la explicación. Hay que completar la identidad/receptor de cada operación en su propietario existente; no abrir otra VNext. Las fichas IP y la aceptación de sus autores no se convierten en aplicación por esta recepción.

Se proponen **seis unidades exactas**, en el [anexo11](incremental-audit-2026-10-26/ANNEX.md#11-ronda-16--recepción-y-propuestas-acotadas), con receptor e impacto/riesgo/esfuerzo: señal de fallo del comprobador13; estimando FA-4; control XOR; contrato de consultas; puntero vigente en01I; e IP43 para que el nuevo resumen de lectura afirme primero los resultados concretos conservados. La mejora del comprobador es de uso futuro y no bloquea el cierre numérico reconfirmado: el resultado observado fue realmente cero errores.

### Pendientes vigentes tras recibir las correcciones

| Unidad | Estado y siguiente acción |
|---|---|
| I01 / M27-01/02 / M28-01 / familia D28-F01 | Corregido en main y reconfirmado; cierre numérico acotado recibido. Autenticidad de fuentes y validez empírica de L son premisas distintas, no reapertura de este fallo |
| M28-02 | Implementado y reconfirmado en rama60; falta incorporación y recepción final |
| M28-03/04 | Validación de cota finita y vigencia al uso pendientes; fuente60 conserva el casoNaN y carece de reloj de decisión |
| M28-07 y herramienta13 | Higiene de salida/caché ya propuesta; señal de discrepancia mediante código de salida ahora precisada; no aplicar ambas cosas como un cambio científico |
| M28-06 / recepción59 | Recepción realizada; punteros iniciales «Current» necesitan transportar el estado más reciente, preservando cortes66/68 como historia |
| IP01–42 y nuevo resumen IP43 | Incorporación editorial pendiente. La guía y las respuestas mejoran comprensión, pero no sustituyen los reemplazos de las fuentes. Mantener crítica local y contribución positiva con su dimensión |
| TAX26 y D28 documentales | Selección de unidades fuente pendiente. C01 ya no pertenece a esa selección; C04–07 no deben aplicarse dos veces en60 |
| N/F/G/H, originales y líneas temporales/poblacionales | Conservan los estados de la guía y los límites de revisión efectiva. El cierre de un runner o el nuevo mapa§15 no completa las lecturas pendientes de#44–46/#28/#40/#51/#21/#22/#5/#18 |

La recepción y los seis candidatos viven en este mismo PR. Esta ronda no incorpora cambios en fuentes científicas ni en otros PR; la guía y su registro conservan sus estados71. Se actualiza la lectura actual del expediente y se mantiene abierta la siguiente unidad concreta de trabajo.


<a id="ronda-17"></a>

## Ronda 17 — modelo social: #44, resto de #45 y #46 (28-10-2026)

**Auditor:** Claude, asistencia de IA. No es validación humana independiente. *Escrita en paralelo a la [ronda 16](#ronda-16) de Codex y numerada 17 al integrarse después; ambas se conservan íntegras.* **Objeto:** `main` en [`51fc686`](https://github.com/dakleyer/structural-awareness-contributions/commit/51fc686f45b6ef10c53b69f4c26d0e381b007ff8). Estudios `intrinsic-abcd-economics-v0.1` (#44), `scoped-closure-metacognition-v0.1` salvo `qualify` (#45) y `risk-aversion-persistence-v0.1` (#46). Rutas abreviadas: `IA/`, `SC/` y `RA/`.

**Regla de la ronda 10 aplicada:** antes de cada hallazgo se contrastaron el README y la revisión científica del estudio. Cuando el estudio ya reconoce una limitación, el hallazgo lo dice y sólo añade lo que falta.

**Ejecución:** pruebas de los tres estudios en verde en `51fc686`. Las cifras nuevas de K-01 y K-02 se han obtenido ejecutando las funciones del propio estudio con parámetros nuevos; no se ha modificado su código.

| ID | Gravedad · estado | Qué ocurre | Evidencia | Qué se propone |
|---|---|---|---|---|
| <a id="k-01"></a>**K-01** | Media · `ABIERTO` | La ventaja de B sobre la inspección dirigida depende del tamaño del sistema. Con los costes por defecto, B cuesta 0,25·L + 0,75, con L = log₂ n + 2 nodos en el trayecto, y la inspección cuesta 3 fijo. B gana hasta 64 hojas, empata en 128 y pierde después (3,25 frente a 3 con 256 hojas). El README ya advierte que un comparador barato puede ganar; lo que falta es que la ordenación de su tabla (n = 16) cambia con n a costes fijos. Además, el coste de la inspección dirigida no crece con la profundidad y el de B sí. | `IA/intrinsic_abcd.py`, `Costs` y `policy`; [figura](incremental-audit-2026-10-26/figures/K01_B_vs_targeted_by_size.svg) | Declarar el punto de empate L* = (C_target − 0,75)/0,25 = 9 (n = 128). O bien cobrar la inspección dirigida también por nodo del trayecto y comparar las constantes por nodo. Mostrar el valor neto frente a n en lugar de un único n. |
| <a id="k-02"></a>**K-02** | Media · `ABIERTO` | Los certificados B no son componibles. Con un cuello en la raíz de 129 (salida actual 128), `upstream_B` emite para source-3 y para source-8 un incremento de 1 cada uno, y los dos son válidos para el receptor. Juntos prometen 2; la ganancia conjunta real es 1. El README limita B a «una pregunta concreta», así que no es un error del código; es un riesgo de lectura si un receptor acumula certificados. | `IA/intrinsic_abcd.py`, `upstream_B` y `receiver_B_valid`, ejecutados con `cap_root=129` | Declarar la no componibilidad en el README. Si se quiere planificar varias preguntas, emitir un certificado conjunto o reservar la holgura del cuello compartido. Añadir el caso como prueba. |
| <a id="k-03"></a>**K-03** | Baja · `ABIERTO` | `sample_report` escribe a mano `baseline_world_private_selected_gain: 2` y `root_bottleneck_world_private_selected_gain: 0`. Ambos valores son correctos; recalculados con `deliver`: 130 − 128 y 128 − 128. Mismo patrón que G-03. | `IA/intrinsic_abcd.py`, `sample_report` | Calcularlos con `deliver`, como ya hace `policy`. |
| <a id="k-04"></a>**K-04** | Informativo · `VERIFICADO` | Correctos: dos mundos con el mismo A = 128 y respuestas futuras 2 y 0 (separación por fibras, como 00M §4); el certificado que recorre todo el trayecto y respeta el cuello de cualquier antecesor; las cotas de comunicación n y ⌈log₂(n+1)⌉ (como H-06); la desigualdad de `bounded_roi_gate`, acotada a una pregunta. | `IA/intrinsic_abcd.py` | — |
| <a id="k-05"></a>**K-05** | Informativo · `VERIFICADO` | `advisory` evalúa en este orden: derechos, autorización, consentimiento y, por último, la evidencia. `automatic_action` es siempre `False`. `cost_comparison` reutiliza los costes 2,25 / 3 / 32 de #44, así que K-01 se aplica también a su lectura. `structural_exposure` repite el patrón de H-04 (brecha condicionada por tres booleanos); no es un hallazgo nuevo. | `SC/metacognition.py`, l. 275–364 | Enlazar K-01 desde el README de #45. |
| <a id="k-06"></a>**K-06** | Informativo · `VERIFICADO` | Correcto el equivalente cierto CARA-normal μ − γσ²/2. Recalculados los ejemplos: temprano, quedarse 9 frente a rediseñar 7; tardío, 13 frente a 9; defensa activa 13,25, que es la preferida. El umbral cerrado de la campaña, σ_R² > σ_S² + 2(μ_R − μ_S − C)/γ, se deriva correctamente de CE(R) − C < CE(S). | `RA/risk_model.py`; `RA/experiments-from-escritos-v0.1/scenario_campaign.py`, l. 185 | — |
| <a id="k-07"></a>**K-07** | Media · `ABIERTO` | `late_stay_future_forecast_below_current` compara la media de la lotería de quedarse (14) con el bienestar neto estipulado actual (30 − 13 = 17) y concluye «por debajo». Según los propios docstrings son construcciones distintas: `WelfareSnapshot` es una entrada F independiente y no se infiere de la brecha. No se declara que compartan escala. | `RA/risk_model.py`, `declared_examples` | Declarar una escala común y su justificación, o retirar la comparación. Mismo tipo de problema que F-05 (conmensurabilidad). |
| <a id="k-08"></a>**K-08** | — · `PROPUESTA` | Conexión H-01 ↔ #46. H-01 pedía una elección racional para sostener «subóptimo racional». #46 ya la tiene para un actor: preferir quedarse cuando el rediseño es más incierto, incluso con mayor media. Con dos actores y la restricción conjunta de #42, esa regla da un juego de coordinación en el que quedarse puede ser dominante en riesgo, como en la caza del ciervo del anexo §3. Se reutiliza maquinaria existente; no hace falta una dimensión nueva. | `RA/risk_model.py`; `BT/bounded_traps.py`; anexo §3 | Construir el ejemplo de dos actores con `certainty_equivalent` y la restricción de #42. |

**Ayudas añadidas:** [figura de K-01](incremental-audit-2026-10-26/figures/K01_B_vs_targeted_by_size.svg), tres ideas nuevas en lenguaje llano en la [guía](incremental-audit-2026-10-26/GUIA_DE_LECTURA.md#añadido-en-la-ronda-17), registros K en el registro de estados y una comprobación nueva que avisa si la fila de totales de la guía deja de coincidir con el registro.

**Límites:** no se revisan `EXTERNAL_RESEARCH_NOVELTY_REVIEW`, `CROSS_PR_RESEARCH_NOVELTY_SYNTHESIS` ni los documentos de investigación comparativa de #46. Ningún texto anterior se modifica: la ronda sólo añade.


<a id="ronda-18"></a>

## Ronda 18 — recepción de D28-C03: alias frente a hallazgos relacionados (28-10-2026)

**Auditor:** Claude, asistencia de IA. **Origen:** la propuesta D28-C03 de Codex en el [PR #59](https://github.com/dakleyer/structural-awareness-contributions/blob/a3326843aa9822b1d7a4c774531fc51818300125/research/ecosystem-awareness/baseline/01I_VNext.md) y su comentario en este PR. Codex señala que la tabla de alias de la guía (§7) agrupaba alias exactos con hallazgos distintos de una misma familia. Tiene razón: F-01 y F-03 no son el mismo hallazgo, ni tampoco G-05, H-02 y F-06. Además, la fila «Brecha supuesta» mostraba 🔵 Abierto para todo el grupo aunque G-05 y F-06 están respondidos.

**Aplicado como añadido, sin retirar texto:** se conserva la tabla y su frase de introducción. Debajo se añaden el párrafo propuesto en D28-C03, una nota que aclara que la columna «Estado» resume el grupo y una tabla nueva, [registro por registro](incremental-audit-2026-10-26/GUIA_DE_LECTURA.md#7-un-mismo-problema-varios-nombres), con el tipo de relación (mismo defecto, lo amplía, relacionado) y el estado propio de cada registro. Ningún estado cambia en esta ronda.

