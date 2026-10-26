# Auditoría científica incremental — ACC, Conscientia y reducción agéntica

**Estado:** abierta, incremental. Cada ronda añade hallazgos; ninguno se borra. Un hallazgo sólo cambia de estado (`ABIERTO` → `RESPONDIDO` → `CERRADO` / `RECHAZADO`) con una nota que diga quién lo decidió y por qué.
**Revisor:** Claude (Anthropic), asistido por IA, a petición del propietario. **No es la revisión científica humana independiente** que solicita la nota de revisión externa; es una auditoría previa para preparar esa revisión.
**Método:** lectura del código y de los documentos en los commits fijados abajo. En la ronda 2 no se pudo ejecutar el código (el entorno del revisor bloqueó la ejecución de código externo); las cifras se derivaron analíticamente del código y coinciden con las declaradas en los PRs.

## Commits auditados

| Objeto | Commit |
|---|---|
| `main` | [`3e58fc6`](https://github.com/dakleyer/structural-awareness-contributions/tree/3e58fc6997a439b9783fd6b92ccee3f4292772dd) |
| PR #54 (abierto) | [`c332dfa`](https://github.com/dakleyer/structural-awareness-contributions/tree/c332dfac84d66f58ed424cee20ad6ad40060aec7) |
| PR #57 (abierto) | [`fb79df2`](https://github.com/dakleyer/structural-awareness-contributions/tree/fb79df2ce93c0730ed49c3454a6ebef033ebbe5e) |

Si cualquiera de estos commits cambia, los hallazgos afectados deben revalidarse antes de cerrarse.

## Registro de rondas

| Ronda | Fecha | Objeto | Hallazgos |
|---|---|---|---|
| 1 | 2026-10-26 | Nota «Solicitud de revisión científica independiente» (borrador del 26-10-2026) | N-01 a N-09 |
| 2 | 2026-10-26 | Código de PR #57 y PR #54 | F-01 a F-07 |
| 3 | 2026-10-26 | Campaña de PR #48/#49 en `main` (`conscientia-campaign-v0.1`) | G-01 a G-06 |

Pendiente: modelo social #42–#46, núcleo #28/#40/#51, #21/#22 (00M_VNext) y los diferidos #5/#18 (linaje A/B/C/D).

---

## Ronda 3 — Campaña de PR #48/#49 (`main`)

Ruta abreviada: `CEC/` = `research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/conscientia-campaign-v0.1/`. La tabulación de `CASE_REGISTRY.json` se hizo leyendo el JSON, sin ejecutar el código del repositorio.

**Respuesta a la pregunta pendiente de F-06:** sí, el patrón se repite, y en la matriz de decisiones es más fuerte, porque la exactitud de los comparadores no se calcula: se estipula caso a caso.

### G-01 · Alta · `ABIERTO` — La matriz 60 × 5 mide el diseño del fixture, no las estrategias

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

### G-05 · Baja · `ABIERTO` — PR #54 duplica parcialmente la red de #49

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

### F-01 · Alta · `ABIERTO` — En v0.1 el metaprotocolo es, en código, el brazo convencional con Q equivalente

**Evidencia.** `AGR/agentic_reduction.py`, `plan_public` (l. 129 y ss.): `Q_META_PROTOCOL` y `CONVENTIONAL_EQUIVALENT_Q` recorren la misma rama (l. 144); la única diferencia es el precio (`equivalent_Q_cost`, l. 147). Las compuertas de liberación, consentimiento, autoridad y protocolo conjunto (l. 182) se aplican igual a todos los brazos que transfieren, incluidos los convencionales. En `AGR/make_cases.py` el precio equivalente por defecto es igual al de Q (0,3; l. 21 y 24); sólo AG22 lo abarata (l. 71).

**Consecuencia.** El modelo no puede producir una ventaja del metaprotocolo sobre un sistema convencional con la misma Q: por construcción empata (mismo precio) o pierde (convencional más barato). La frase «un peer convencional con Q equivalente empata o gana» no es un resultado ni un falsador superado; es una identidad del código.

**Lo que ya reconoce el PR.** `ISOMORPHISM_AND_BOUNDARY_AUDIT.md` §2 (AG-R3) admite que un sistema no agéntico con la misma Q puede ejecutar el mismo algoritmo y que el diferencial queda en parámetros no probados. El hallazgo no contradice eso: lo confirma en código y señala que la descripción del PR y la nota de revisión siguen presentando la comparación de brazos como si fuera informativa.

**Acción propuesta.** Presentar #57 como **prueba de reducción completa en v0.1** (el metaprotocolo es una parametrización de ACC), no como evaluación del metaprotocolo. Para que la hipótesis agéntica sea falsable hace falta un operador o estado que no sea un precio, con un caso pareado donde el peer convencional con igual información y permisos no pueda replicarlo (criterio 2 de la propia auditoría de isomorfismo, §3).

### F-02 · Alta · `ABIERTO` — La única vía hacia un diferencial agéntico es H5, que no está probada y además no compara arquitecturas

**Evidencia.** El overhead `h` (`overhead_resources`) es un parámetro público del mundo, común a todos los brazos (`physical_response`, l. 100). AG23/AG24 cambian `h` para todos, no para una arquitectura frente a otra.

**Consecuencia.** Aun en el mejor caso, AG23/AG24 no pueden mostrar que una arquitectura agéntica tenga menor coste de reconfiguración: el mundo cambia, no el comparador. El PR ya declara H5 «no probada»; el problema es que, tras F-01, H5 es la **única** hipótesis que sostendría el diferencial agéntico.

**Acción propuesta.** Hacer `h` dependiente del brazo (p. ej. `h_agentic`, `h_conventional`) y declarar explícitamente que la ventaja agéntica, si existe, es exactamente la diferencia de esos dos parámetros, que debe medirse fuera del modelo.

### F-03 · Media · `ABIERTO` — Los conteos del barrido (107/14/39 de 160) son artefactos del diseño de la rejilla

**Evidencia.** `AGR/sensitivity.py`:
- l. 17: la mitad de la rejilla usa `true_rate = 0,6`, menor que `donor_marginal_rate = 1`. Ninguna transferencia puede mejorar la producción, y los brazos con información pagan su coste aunque no actúen (`plan_public`, l. 175). Resultado: A-only es ganador exclusivo **por construcción** en esas 80 celdas.
- l. 31–32: el barrido compara sólo `A_ONLY`, `Q_META_PROTOCOL` y `CONVENTIONAL_DIRECTED`; **excluye** `CONVENTIONAL_EQUIVALENT_Q`.
- Derivación analítica de las 14 victorias exclusivas de Q+meta: con `true_rate = 2`, Q (cota 1,6, tope 2) sólo propone transferir si `h ∈ {0,1; 0,25; 0,5}` y su precio está por debajo de la ganancia condicional (7 configuraciones). Gana exclusivamente sólo cuando el instrumento dirigido cuesta 3 o 5, es decir, cuando no actúa o apenas gana: 7 × 2 = 14. Coincide con el PR.

**Consecuencia.** Las cifras describen la rejilla, no el mecanismo. Con el brazo convencional equivalente incluido al mismo precio, las 14 victorias serían empates (F-01).

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
