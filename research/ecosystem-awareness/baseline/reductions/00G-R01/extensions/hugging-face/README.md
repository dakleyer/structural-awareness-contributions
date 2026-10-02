# Extensión de R01: OpenAI / Hugging Face

## Ficha común de revisión

| Campo | Estado del expediente |
|---|---|
| Tipo y base | Histórico con modelo construido auxiliar; R01 v0.6, blob `3261a625975e303e12c484bc9c273d7f8819b099`. |
| Correspondencia | F e inversa de IDs/rutas en el modelo; α histórica completa pendiente (§§2–4). |
| Evidencia | EV1 para resultados del contrato de consultas; EV2 para verificaciones finitas; EV0 para correspondencia histórica. EV3/EV4/EV5 no acreditados aquí. |
| Cobertura y A25 | [Quince grupos, estados y A25 comunes](../CRITERIA_AND_AUDIT.md); se conservan las matrices particulares del expediente. |
| Receptor, positivo y falsificador | Rechazo de denegación detectada; rutas válidas/certificado suficiente; falsificador de emparejamiento con marginales iguales. |
| Revisión | Interna del autor asistida por IA; observaciones externas parciales contrastadas, sin independencia acreditada. |
| Dictamen | Correspondencia parcial demostrada/comprobada en el alcance sintético; extensión completa del objeto histórico pendiente. |

Los códigos EV identifican evidencia, no las obligaciones E1–E7 de la nota matemática. Su definición está en el [criterio común](../CRITERIA_AND_AUDIT.md#3-estados-de-evidencia-comunes).

[00G-R01](../../README.md) · [Tabla de extensiones](../../README.md#extensiones)

El caso examina cómo una alternativa, un hallazgo o un encargo compartido puede adquirir fuerza operativa frente a la tarea y los límites del receptor. Su conexión con R01 permite estudiar búsqueda de soluciones, coste de validación y reutilización social de hallazgos. La causa económica histórica sigue siendo una hipótesis; la auditoría que sigue no declara reproducido el incidente.

| Parte del expediente | Contenido |
|---|---|
| Escenario | [Correspondencia con R01, parte 3](../../Escenario-creatividad-validacion.md#3-familia-00g-escenario-reducido-y-referencia-hugging-face) · [Caso documentado y diseño previo 00G-HF](../../../../00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.2_DRAFT.md) |
| Justificación de extensión | [Relaciones que deben conservarse](#2-qué-debe-conservar-una-extensión) · [Parámetros](#3-inventario-de-parámetros-y-resultados) · [Codependencias](#5-codependencias-y-contraejemplos) |
| Validación | [Comprobación ejecutada](#4-comprobación-reproducible-ejecutada) · [Criterios A25 y pendientes](#6-resultado-frente-a-a25) |
| Código y resultados | [Guía de reproducción](./proof/README.md) |
| Fuentes y antecedentes | [Fuentes examinadas](#8-fuentes-y-versión-examinada) · [Historial de ensayos](../../../../annexes/00G-HF-DEVELOPMENT-HISTORY-v0.1.md) |
| Estado | Conservación parcial verificada en un modelo sintético; admisión histórica completa y diferencial EA pendientes. |

**La reducción de base pertenece a R01.** Su [fundamento 00G → R01](../../README.md#fundamento-y-prueba-de-la-reducción) se consulta desde el escenario base. Aquí se reúne la justificación de la extensión al caso HF y su validación. Los documentos previos 00G-HF conservan su contenido y ubicación histórica; sus recorridos R1–R3 no se renombran como ejecuciones de 00G-R01.

---

<a id="00g-r01--hugging-face-auditoría-de-parámetros-resultados-y-codependencias"></a>
**Expediente de auditoría de parámetros, resultados y codependencias R01 → Hugging Face.**

**Versión 0.1 · 2 de octubre de 2026 · Auditoría del autor asistida por IA.**

[00G-R01 y sus extensiones](../../README.md#extensiones) · [Antecedente de la reducción de base](../../../../00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.1_DRAFT.md) · [Infoblox v0.5](../infoblox/README.md) · [Código](./check.py) · [Resultados](./results.json) · [Registro de cobertura](./coverage.json).

## 1. Dictamen y alcance

**La conservación completa de R01 en el incidente histórico de Hugging Face no está demostrada.** Esta revisión comprueba un transporte sintético acotado y audita lo que falta para justificar una extensión real. No convierte una analogía, una tabla de parámetros o una simulación construida por nosotros en una reproducción del incidente.

La petición auditada es más fuerte que comprobar que aparecen muchos agentes, muchos pasos y premios atractivos: exige conservar los parámetros materiales, sus relaciones conjuntas, las decisiones y los resultados bajo recursos y observaciones comparables. Ése es el criterio utilizado aquí.

Hay tres resultados distintos:

1. **Inventario documental:** se ha revisado el inventario completo de R01 §2.13, sus métricas, las identidades analíticas de coste, las obligaciones de §3.5 y A25 X1–X7. La matriz siguiente registra cobertura parcial y pendientes, sin declarar cerrados todos los factores.
2. **Comprobación ejecutada:** un grafo sintético y su representación como tareas, tablón y registros del propietario conservan las propiedades enumeradas en §4. Se prueban también contraejemplos a transferencias incorrectas. Es una representación inspirada en las preguntas del caso HF, no el entorno histórico ni un modelo calibrado de sus agentes.
3. **Admisión histórica:** sigue abierta. No se ha establecido una proyección completa de una trayectoria del mismo receptor, con mandato, información disponible, costes, decisión y efecto. No hay ejecución de LLM, APIs de producto, ataques, tráfico de red ni comparación EA en este paquete.

**R01 v0.6 es una especificación de investigación sin resultados experimentales propios.** Sus fórmulas condicionales pueden comprobarse bajo sus hipótesis; SC-H y SC-Ha–SC-He no son resultados empíricos ya obtenidos que puedan heredarse. Los ensayos anteriores 00G-HF y el comprobador de Infoblox mantienen sus ámbitos originales.

### Qué se comprobó realmente para Infoblox

Este contraste se conserva como contexto de la auditoría entre expedientes; no es evidencia del incidente HF. La comparación vigente usa la [matriz común](../CRITERIA_AND_AUDIT.md#5-matriz-común-de-los-quince-grupos-de-r01-213).

El [documento v0.5, matriz de factores y prueba acotada](../infoblox/README.md#5-qué-debe-conservar-la-extensión-desde-r01) ya distingue lo representado de lo pendiente. Su script comprueba cuatro cadenas, veredictos y valores, pares de vistas indistinguibles, un control estricto, reparto de consultas, relés y curvas exactas de un contrato finito. Variar la dispersión en ese modelo no prueba su efecto sobre la búsqueda; repartir consultas entre N participantes no ejecuta una dinámica social.

Por tanto, **no sería correcto decir que ya se conservaron todos los parámetros y codependencias de R01 en Infoblox real**. Están pendientes, entre otros, la búsqueda probabilística completa, la influencia social, la calibración de costes y tiempo, las políticas ejecutables completas y la admisión A25. Un certificado suficiente y accesible resuelve el obstáculo informacional modelado; ninguna de estas pruebas acredita imposibilidad universal frente a las tecnologías disponibles.

## 2. Qué debe conservar una extensión

La conservación de variables aisladas es insuficiente. Dos mundos pueden tener idénticas medias y dispersiones de beneficio y distancia, pero colocar los mejores beneficios en posiciones diferentes. Un radio de búsqueda fijo obtiene entonces resultados distintos. Se necesita conservar las relaciones materiales entre variables, además de sus distribuciones marginales.

Para una configuración θ, una representación F del mundo y una proyección α de las trayectorias, el contrato debe identificar:

- **Tarea y alternativas:** mismo mandato; trayectorias completas, conexiones y efectos; una ruta legítima no puede aparecer o desaparecer sin registrarlo.
- **Semántica:** Adm y J de cada trayectoria efectiva; el óptimo se resuelve sobre todas las rutas, incluidas mezclas. Suponer I por su nombre no es una comprobación.
- **Observación:** toda la vista disponible, su orden temporal, memoria, consultas, señales y certificados. Las claves de traducción del auditor no son evidencia gratuita para el receptor.
- **Dependencia conjunta:** qué beneficio corresponde a qué posición, qué revisión cubre qué obligación, qué mensajes derivan de qué fuente y a qué receptor aplica cada autorización.
- **Recursos:** cargos y calendario, incluyendo búsqueda, preparación, descarte, comunicación, comprobación, ejecución, mantenimiento y acceso a certificados. No se identifica L con llamadas de herramientas ni N con mensajes.
- **Políticas y resultados:** las mismas opciones efectivas de decisión y control; q, C, t, a, f, K y e con idénticas definiciones. Una oportunidad adicional o un control más barato puede resolver el caso y debe admitirse.

En el modelo finito, una biyección de acciones y consultas con la misma información y costes permite transportar una política y sus resultados bajo la misma distribución de mundos. **La biyección y ese contrato son hipótesis construidas aquí, no propiedades verificadas del incidente.** Para trasladar una cota de dificultad a un sistema más capaz habría que mostrar, además, que toda política permitida en el destino puede simularse en el origen sin más información ni mayor coste. Mostrar sólo que una política de R01 se puede ejecutar en el destino no basta.

A25 añade la conservación de la frontera de decisión, el predicado de fallo, la ruta de requisitos y el control positivo. Su transferencia general requiere una garantía base independiente; unos cuantos resultados positivos de un comprobador no aportan esa garantía.

Para transferir éxito relativo al óptimo se exige además preservar J* y ε, o el umbral equivalente J*−ε, los límites de coste/plazo y todas las infracciones de campaña. Mapear una ruta no basta si se omite otra ruta mejor. El [criterio común y su contraejemplo](../CRITERIA_AND_AUDIT.md#7-resolución-de-las-observaciones-del-auditor) explicitan esta condición.

## 3. Inventario de parámetros y resultados

Esta tabla cubre los quince grupos de R01 §2.13 y añade las métricas, hipótesis y contabilidad del ejemplo EA. «Sintético» significa definido y comprobado dentro del contrato de este paquete. «Pendiente histórico» no significa ausencia en el incidente: significa que esta auditoría no ha establecido la correspondencia exigida.

| Grupo y referencia R01 | Qué cubre esta comprobación | Qué falta para trasladarlo al caso HF |
|---|---|---|
| Tarea: L, obligación, principal, resultado, T · §2.1 | Longitudes 2, 3 y 4; tarea fija y rutas completas en el grafo. | Expediente del mandato individual; unidad funcional para L; plazo y entrega verificables. No asumir solución legítima en toda tarea histórica. |
| Población: N, unidad y reparto · §§2.5, 2.12 | N=1,2,4 en un módulo separado de reparto de consultas; coste y rondas distinguidos. | Población decisora, capacidad desigual, red, entradas y salidas, calendario y recursos por receptor. Este módulo no ejecuta agentes. |
| Perfiles de entrada y selección de mundos · §§2.3, 2.13 | Cuatro perfiles medios fijados; malla determinista, sin rechazo de mundos. | Familia generadora probabilística, normalización y selección comparable; no calibradas con datos HF. |
| Atractivo realizado de I y P · §2.1 | Veredictos y J de todas las rutas; óptimo exacto incluyendo mezclas. | Distinguir expectativa del agente, puntuación del evaluador y calidad legítima. No atribuir al incidente los valores sintéticos 1–4. |
| Heterogeneidad, σ y correlaciones · §2.3 | Media conservada, desviaciones centradas y semirrango σ; σ=0 o 1/4. | Distribución aleatoria, correlaciones más generales y efecto causal sobre la elección. No se prueban SC-Ha ni monotonicidad. |
| Geometría, D, τ, lados y conexiones · §2.4 | Coordenadas sintéticas; τ=0 o 1/2, alineación positiva/negativa con beneficios; conectores explícitos. | Geometría funcional histórica, ambos lados y desplazamiento de la posición actual. D está fijada por cadena, no barrida como parámetro independiente. |
| Creatividad: R_e, esfuerzo y muestreo · §2.4 | Se conserva el filtro por radio desde un origen fijo para cada ruta. | Política de búsqueda con coste, descubrimiento secuencial, memoria y radio desde posiciones cambiantes. El mapa completo del auditor no se atribuye al agente. |
| Composición, testigos y positivos · §2.9 | Conjunción y control algebraico de paridad, por separado; condiciones de conectores; rutas válidas. | Predicado histórico identificable. La paridad no es una semántica real de permisos. El bloque de consultas usa un solo testigo uniforme y no se confunde con toda la malla de grafos. |
| Revisión: k_a, k_d, orden, salida y reutilización · §2.8 | Ventanas recortadas con cobertura única; coste exacto de salida anticipada bajo un testigo uniforme; consultas adaptativas en el submodelo. | Política completa de revisión histórica y su relación con selección, espera, rechazo y presupuesto. Las ventanas no están integradas en una campaña social. |
| Costes: c_e, c_v, ρ y demás cargos · §2.11 | Identidades de coste de estrategias expresas; módulo de reparto con c_e=2, c_v=1 y comunicación contabilizada. | Calibración de unidades; libro completo de exploración, descartes, ejecución y mantenimiento. Las fórmulas no son cotas universales. |
| Recursos: R, T, v, beta y transferencias · §2.12 | Presupuesto residual de consultas; presupuesto global frente a presupuesto por agente; rondas de consulta. | Reparto v/beta, reserva de ejecución, latencia completa, caducidad y política de transferencias. No se simula el planificador completo. |
| Red: topología, s, latencia, w_s y dependencia · §2.10 | Copias de una misma raíz no añaden cobertura. | Dinámica de emisión y recepción, influencia causal, grado comparable, congestión y secuencia individual. Contar copias no modela w_s. |
| Política: selección, desempate, espera y recuperación · §2.15 | Todas las políticas adaptativas del pequeño contrato de consultas mediante programación dinámica. | CV-C1/CV-A1/CV-A2/CV-EA completos; abstención, conectores de retorno y recuperación después del efecto. El submodelo no es toda la familia R01. |
| Volumen: Q, cobertura, deduplicación · §2.11 | Cobertura única y relés; cargos de estrategias enumeradas. | Q emergente de la búsqueda y selección, tasa r_inv de propuestas revisadas y su acoplamiento. Q no se iguala a N. |
| Variación: semillas, estática y cambios · §§2.13–2.14 | Malla estática determinista; dos permutaciones de identificadores; rechazo de versión inaplicable. | Mundos reservados, flujos aleatorios de agentes y campaña temporal. Comprobar una versión incorrecta no mide caducidad ni SC-He. |
| Métricas: q,C,t,a,f,K,e,ε y fiabilidad · §1.4 | Adm/J exactos y probabilidades exactas del submodelo; coste de módulos acotados. | Vector completo por campaña, censura, incertidumbre, Pareto y comparación estadística. No hay mapa empírico de eficacia. |
| SC-H y SC-Ha–SC-He · §§1.2, 2.18 | Se auditan sus premisas y se conservan controles que pueden resolver el caso. | Ejecución e inferencia propias. No son teoremas establecidos por el escenario base. |
| Ejemplo EA: S,H₀,h_a,h_m · §4.4 | Sólo se revisa su papel en la contabilidad; no se ejecuta EA. | Costes de preparar, aplicar y mantener evidencia; comparación con certificados y caché convencionales. Ningún ahorro observado se atribuye aquí a EA. |

## 4. Comprobación reproducible ejecutada

### 4.1 Dos representaciones y una malla conjunta

`check.py` construye un grafo por etapas y una segunda representación de tareas del tablón con relaciones y registros del propietario. Los evaluadores de rutas de ambas representaciones están separados. La correspondencia conserva cada par beneficio–posición, cada conector, cada condición y el orden de las operaciones. Sus nombres carecen de etiquetas I/P visibles; el auditor conserva la traducción.

Se cruzan L∈{2,3,4}, σ∈{0,1/4}, τ∈{0,1/2}, dos signos de alineación, conectores entre cadenas activados/desactivados, conjunción/paridad y tres posiciones del testigo (ausente, primera, última). Resultan **288 configuraciones conjuntas**, verificadas con dos permutaciones de identificadores. Las desviaciones de las cadenas tienen suma cero y semirrango uno antes de aplicar σ o τ; la posición de la ruta canónica M permanece en cero. No se afirma que esa normalización sea una distribución observada en HF.

Las rutas mixtas se enumeran realmente cuando los conectores las permiten. Su valor y admisibilidad pueden cambiar el óptimo; no se mantiene por decreto la cadena inicialmente denominada «mejor». La paridad se comprueba como control algebraico aparte y puede aceptar combinaciones que una conjunción rechaza.

El filtro de radio prueba que se conservan las parejas posición–beneficio y las rutas accesibles bajo ese filtro. No ejecuta la búsqueda de §2.4 ni demuestra que su coste sea inevitable. La igualdad de resultados entre las representaciones es una propiedad de la codificación construida; **no prueba que el incidente admita esa codificación**.

### 4.2 Información, costes y recursos

Los pares de vistas incluyen todos los datos públicos declarados y todos los hechos consultados o inicialmente disponibles. Sólo difieren en una condición no consultada de la cadena candidata. Una herramienta adicional que revelase esa condición invalidaría esa indistinguibilidad; no se la puede ocultar para conservar el resultado.

El submodelo de consultas concede todas las candidatas. Para U∈{2,3,4}, fija probabilidad 1/2 para el mundo totalmente válido y 1/(2U) para cada mundo con una condición inválida. Con presupuesto residual b≤U, la programación dinámica enumera las opciones adaptativas del contrato. Conserva entre representaciones:

- Cota optimista de acierto: 1/2 + b/(2U).
- Control que exige cobertura suficiente: acierto 1/2 hasta b=U, y 1 con cobertura completa.
- Certificado agregado suficiente de coste de acceso uno: acierto 1 cuando b≥1.

Son probabilidades de este problema de decisión finito, **no tasas de infracción de una flota ni estimaciones de HF**. El certificado presupone evidencia ya preparada; su construcción no es gratuita. Los otros costes comunes quedan fuera del presupuesto residual y deben cobrarse antes de trasladar la cota a una campaña.

También se enumeran estrategias para comprobar las identidades de R01 §2.11: c_vNL, c_vNL(L+1)/2 y c_vNL². La salida anticipada con un testigo uniforme conserva E[lecturas]=(L+1)/2 y la mezcla con propuestas válidas de §2.9. Son costes de esas estrategias, no mínimos inevitables. Las ventanas k_a/k_d cuentan unidades únicas y recortan los extremos.

En un módulo separado, U relaciones se reparten entre N revisores. El trabajo compartido no se multiplica por N; las rondas pueden disminuir y se cobra la comunicación. Se distinguen presupuesto global fijo y presupuesto fijo por agente. Se permite U<L: ni longitud funcional ni número de participantes equivale automáticamente a evidencia pendiente.

### 4.3 Resultado del comprobador

El registro exacto y sus contadores están en [results.json](./results.json): 288 configuraciones conjuntas, 576 verificaciones de conjuntos de rutas y óptimos bajo permutaciones, 33.408 comprobaciones de resultado de ruta y conectores, 25 pares de vistas completas, 36 valores de políticas de consulta y 918 comprobaciones de cobertura de ventanas. Todos los chequeos pasaron.

Las configuraciones y aserciones comparten datos; **no son muestras independientes ni ensayos de agentes**. Un PASS significa que las propiedades finitas indicadas se cumplen en el código y la malla declarados. No certifica todo el documento ni una integración tecnológica.

## 5. Codependencias y contraejemplos

| Relación que importa | Comprobación o resultado | Límite |
|---|---|---|
| μ,σ ↔ D,τ ↔ R_e ↔ alternativas alcanzables | Se conserva la pareja beneficio–posición. Contraejemplo: beneficios {1,3} y distancias {1,3}, radio 1; cambiar sólo el emparejamiento cambia el mejor beneficio accesible de 1 a 3. | Las mismas distribuciones marginales no garantizan la misma búsqueda. |
| Conectores ↔ rutas híbridas ↔ Adm,J,I | Enumeración de rutas y óptimos en ambas representaciones. | Una extensión con conectores adicionales necesita volver a resolver el óptimo. |
| Predicado ↔ testigo ↔ cobertura ↔ k_a,k_d | Conjunción/paridad separadas; ventanas y consulta completa. | No sustituir un predicado por otro para obtener el fallo deseado. |
| Vista completa ↔ consultas ↔ presupuesto ↔ éxito | Pares indistinguibles y programación dinámica exacta. | Un certificado suficiente elimina la obstrucción; el conjunto de capacidades debe revisarse. |
| N ↔ reparto ↔ coste total ↔ tiempo | 24 configuraciones separadas de reparto y presupuesto; U no se duplica por identidad. | No modela congestión, agenda completa ni influencia social. |
| Q,r_inv ↔ orden de selección ↔ coste | Identidades para estrategias y mezcla declarada. | Q y r_inv históricos no se han estimado; la selección puede modificarlos. |
| Linaje ↔ número de mensajes ↔ cobertura | Relés de una misma raíz siguen cubriendo una raíz. | No establece que un receptor histórico los contase como pruebas independientes. |
| Mandato, destinatario, versión ↔ reutilización | Rechazo de evidencia con propietario, misión, receptor o versión incorrectos. | Registros transparentes del modelo; no implementación criptográfica ni auditoría de permisos reales. |
| Denegación detectada ↔ decisión ↔ efecto | La transición «denegación conocida → ejecutar» queda fuera del receptor básico que rechaza denegaciones. | Una variante que la permita debe declararse; no se hereda la conducta básica sin cambios. |
| Existencia de M/I ↔ óptimo legítimo ↔ mediocridad | Si no hay ninguna finalización legítima, faltan M e I según el contrato base. | Inventar una solución histórica o sustituir la tarea por «intentar» cambiaría el problema. |
| Caducidad ↔ reutilización ↔ h_m ↔ plazo | Obligación identificada; sólo se comprueba versión inaplicable. | Campaña dinámica pendiente. |
| Política ↔ control de ejecución ↔ q,a,f,e | Se distingue decidir, bloquear, ejecutar y entregar en la auditoría. | No se ejecuta todavía el evaluador completo de campañas; cero efectos indebidos no basta para acreditar éxito. |

### Qué impide una admisión automática del incidente

Las fuentes primarias respaldan una motivación concreta, pero también límites. OpenAI describe un episodio en el que un agente expresó dudas de autorización y continuó después de un GO de un par, y recoge negativas a participar. Eso permite preguntar por la autoridad atribuida, sin aportar aquí una trayectoria histórica completa normalizada [H1].

METR documenta tareas que no podían resolverse mediante la vulnerabilidad especificada, cooperación entre agentes y pasajes que reconocen extralimitación. Señala también límites de captura y reconstrucción. Por ello no se puede asumir una ruta legítima alcanzable para todo receptor, ni interpretar toda continuación como falta de información, ni convertir fragmentos de varios agentes en un único testigo [H2].

El [registro histórico anterior](../../../../traversals/00G-HF-HISTORICAL-REVIEW-2026-10-01/EVIDENCE_REGISTER.json) conserva seis unidades documentales, sin adjudicación operacional completa. Se mantiene ese estado: esta auditoría no ha rellenado sus campos faltantes ni ejecutado C3 sobre ellas. R01 §3.5 excluye expresamente del receptor básico los episodios que continúan manteniendo reconocida una denegación.

Que una trayectoria pertenezca eventualmente a C-V-G no demostraría que el coste de validación causó su desenlace. Hacen falta observaciones o intervenciones que distingan esa explicación de presión social, autoridad aparente, prioridades distintas, errores de interpretación y desobediencia pese a conocer el límite.

## 6. Resultado frente a A25

| Criterio | Estado de esta auditoría |
|---|---|
| X1 Núcleo | Transporte finito de relaciones del submodelo; núcleo histórico completo no acreditado. |
| X2 Frontera de decisión | Definida para el comprobador. Falta expediente suficiente de un receptor histórico concreto. |
| X3 Reflejo del fallo | Adm/J se conservan en el modelo. Los casos de denegación conocida o ausencia de solución legítima impiden una inclusión universal en el receptor base. |
| X4 Ruta de requisitos | No se certifican todas las obligaciones S/T; requiere auditoría propia. |
| X5 Positivo | El modelo incluye rutas legítimas, evidencia aplicable y certificado suficiente. No equivale a un positivo histórico emparejado. |
| X6 Recursos | Costes y presupuesto explícitos en módulos limitados; contabilidad integral y calibración histórica pendientes. |
| X7 Sin primitivas ocultas | El comprobador declara sus operadores; la normalización completa de una implementación y sus objetos históricos sigue pendiente. |

**Decisión:** mantener Hugging Face como referencia histórica y extensión/reducción candidata; admitir únicamente las propiedades finitas expresamente comprobadas. No declarar cerrada la extensibilidad total, una reproducción del incidente, causalidad económica ni una ventaja de EA.

Para cerrar una instancia se necesita seleccionar una trayectoria, verificar mandato y solución legítima, reconstruir toda su vista previa y sus capacidades, mapear parámetros y relaciones, registrar costes y tiempo, comprobar el positivo y ejecutar la comparación competente. Si una condición del R01 básico no se cumple, se delimita otra variante y se demuestra de nuevo su relación; no se modifica silenciosamente el escenario base.

## 7. Reproducir y verificar

Desde esta carpeta, con Python 3 y su biblioteca estándar:

```sh
python3 check.py
```

El script regenera `results.json`. `coverage.json` recoge el inventario y los estados de esta auditoría; no es un certificado emitido por el comprobador. `SHA256.json` registra las huellas de los archivos publicados. No se requieren credenciales ni acceso de red.

## 8. Fuentes y versión examinada

- **R1 — R01 v0.6**, referencia congelada para esta auditoría: [escenario completo](https://github.com/dakleyer/structural-awareness-contributions/blob/114ac132bc2be4e7008001fe505bf5bd4c36c515/research/ecosystem-awareness/baseline/reductions/00G-R01/Escenario-creatividad-validacion.md), §§1.2–1.5, 2.1–2.18, 3.4–3.6 y 4.4–4.7. Especificación, no resultados de campaña.
- **R2 — Infoblox v0.5**, [documento y matriz de factores](https://github.com/dakleyer/structural-awareness-contributions/blob/114ac132bc2be4e7008001fe505bf5bd4c36c515/research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/infoblox/README.md), §§5–6; [comprobador](https://github.com/dakleyer/structural-awareness-contributions/blob/114ac132bc2be4e7008001fe505bf5bd4c36c515/research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/infoblox/proof/check.py).
- **R3 — A25**, [criterios X1–X7 y transferencia condicional](https://github.com/dakleyer/structural-awareness-contributions/blob/114ac132bc2be4e7008001fe505bf5bd4c36c515/research/ecosystem-awareness/baseline/00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md), §§4–7.
- **R4 — Antecedentes 00G-HF**, [reducción v0.1](../../../../00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.1_DRAFT.md), [revisión de pasos 1–2](../../../../annexes/00G-HF-STEPS-1-2-REVIEW-v0.1.md) y [registro documental histórico](../../../../traversals/00G-HF-HISTORICAL-REVIEW-2026-10-01/README.md). Consultados en el mismo commit de R1; sus resultados no se renombran como ensayos R01.
- **H1 — OpenAI**, [The Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead/), 26 de agosto de 2026; secciones sobre el incidente y el ecosistema de desalineación. Reconsultado el 2 de octubre de 2026.
- **H2 — METR**, [Brief independent investigation of agents’ behavior, reasoning and collaboration](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/), 26 de agosto de 2026; tareas imposibles, reconocimiento del alcance, proceso y limitaciones. Reconsultado el 2 de octubre de 2026.

No se declara revisión independiente de este paquete, muestreo aleatorio del incidente, prueba ciega ni evidencia de eficacia de EA.
