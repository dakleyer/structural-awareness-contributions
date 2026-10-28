# SA → EA → EP — función de reposicionamiento adaptativo: fundamento, requisitos y verificación DDS

**Documento de investigación aditivo v0.1 · propuesta en revisión, 28 de octubre de 2026.**  
**Identidad:** puente de conservación de significados, trazabilidad y protocolo de pruebas; no es una nueva Foundation, un nuevo requisito, un estándar, un algoritmo MSCA publicado ni una validación del sistema integrado.  
**Corpus propietario de las respectivas materias:** Structural Awareness (SA), Ecosystem Awareness (EA), Ecosystem Positioning (EP), MSCA, Regime Awareness (RA), Gradient Law, ACC/autoridad externa y DDS.  
**Ruta de lectura:** [puente fundacional SA→EA→EP/DDS](./SA_EA_EP_DDS_FOUNDATIONAL_BRIDGE_v0.1.md) → **este documento** → [anexo técnico de reutilización residual y búsqueda (§§1–15)](./SA_POSITIONED_RESIDUAL_REUSE_AND_LOCAL_ADAPTATION_v0.1.md).

> **Idea central.** La contribución investigada es una *Función de Reposicionamiento Adaptativo* (**FRA**) —búsqueda, contraste y encaminamiento legítimo de cambios de arquitectura entre participantes con objetivos potencialmente competitivos—, compuesta por cinco funciones sustituibles pero conectadas: metasintáctica estructural; residual cualificado; composición no fungible; prueba selectiva y gradiente; Regime Awareness. No es un quinto sistema epistemológico ni cinco Foundations. La hipótesis diferencial es encontrar *transiciones arquitectónicas de alto valor con bajo coste total de exploración*, preservando los límites de evidencia, el control humano y la autoridad de los participantes. Las cinco funciones son una vista funcional sobre la arquitectura EP más amplia de ocho módulos; no los renumeran. **«Evolución ecosistémica» nombra un posible efecto acumulado de reposicionamientos efectivos, no una función que garantice progreso ni una utilidad global común.** La FRA propone y evalúa; la operación de reposicionamiento, los contratos y las autorizaciones siguen en MSCA/ACC y sus propietarios.

### Resumen ejecutivo para revisión externa

| Cuestión de revisión | Respuesta y fuente propietaria |
| --- | --- |
| **¿Por qué podría funcionar?** | SA da una lógica condicionada de límites/existencia/posición; EA Foundation y P1–P6 gobiernan cómo actuar sin falsificar conocimiento ni autoridad. |
| **¿Qué parte es matemáticamente plausible?** | **00M** permite examinar correspondencia de ámbitos, mapas parciales y suficiencia de un resumen *para una pregunta concreta*; **00N** añade las condiciones de utilidad oportuna y responsable. |
| **¿Qué se propone construir?** | Una función de **cinco mecanismos** integrada en **EP M1–M8**, que localiza puertas, consulta residuos parciales, compone hojas no fungibles y prueba cambios **de arquitectura ecosistémica**, bajo gradiente, ACC y RA. |
| **¿Frente a qué habría que ganar?** | Contra un **B2/PA-5 competente** que ya incorpore control, búsqueda activa, modelos arquitectónicos, señales de cambio y roles institucionales cuando sean apropiados; anclado en **00D v0.2 (canónico)** y **00D v0.3 (borrador EP)**. |
| **¿Qué no está demostrado?** | Que los cinco mecanismos juntos reduzcan coste total, mejoren resultados interorganizacionales o produzcan autosanación integral en ejecuciones reales; requiere **DDS B/C** y comparaciones emparejadas. |

**Criterio de originalidad defendible:** no es «usar indeterminación», «fusión de sensores» ni «tener contratos de agentes» aisladamente, sino **combinar esas técnicas en un circuito trazable de descubrimiento y renegociación de *arquitectura abierta*, con residuos situados, calificación inter-agente, gobierno de roles y evidencia del beneficio**. Es un diferencial candidato, sometido a prior art y comparación, no una proclamación de unicidad.

## 1. Tres ejes que no deben confundirse: origen lógico, realización técnica y prueba

| Eje | Responsable | ¿Qué aporta? | Lo que NO significa |
| --- | --- | --- | --- |
| **Fundamento lógico/matemático** | [SA Part I](./A_APRIME_OPEN_SEMANTIC_TRANSFER_BETWEEN_AGENT_ECOSYSTEMS_v0.1.md), [Part II](./METASYNTACTIC_UTILITY_CLASS_THEOREMS_v0.1.md), [SA-E1–SA-E6](./SA_METAEXISTENCE_CONTEXT_AND_EVALUABILITY_CALCULUS_v0.1.md) | Fronteras de representación, existencia/exclusión relativa, posicionamiento, valor/coste condicionado de metainformación y relajación de restricciones. | No prueba que todo exterior contenga una solución, que sea accesible, ni mayor computabilidad que Turing. |
| **Foundation ecosistémica** | [EA 01 integrada](../ecosystem-awareness/baseline/01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md), [EA 02](../ecosystem-awareness/baseline/02_EPISTEMIC_SAFETY_PRINCIPLES_CONTROL_MATRIX_v0.4.part01.md), [02A](../ecosystem-awareness/baseline/02A_FOUNDATION_TO_OPERATIONAL_PRINCIPLE_DERIVATION_PROOF_v0.1.md) | Dos problemas: representación limitada/residual abierto y pérdida de validez del marco por cambio ecosistémico. Regula incertidumbre, cierre, recursos, dependencia y composición. | Los tres descriptores de SA **no** implican por sí solos los seis principios de EA: son imprescindibles hechos independientes de capacidad, plazo, autoridad y dependencia. |
| **Semántica/plausibilidad de información parcial** | [00M](../ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md), [00N](../ecosystem-awareness/baseline/00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md) | A/B/C/D relativos al proceso; mapas parciales; correspondencia de ámbitos; suficiencia de resúmenes; puente de plausibilidad funcional. | 00M no es SA Part I/II, otra Foundation ni una demostración empírica de economía computacional. |
| **Obligación de comportamiento** | [Requisitos canónicos 00](../ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md), EA P1–P6/00K | S1–S14, T1–T4, H1–H6 y métricas: lo que debe demostrar un candidato dentro de un ámbito y sus responsabilidades. | Una alineación de principio a requisito no demuestra cumplimiento ni equivale al requisito completo. |
| **Implementación arquitectónica candidata** | [Ecosystem Positioning](../../architectural-contributions/ecosystem-positioning/README.md), [benchmark EP M1–M8](../ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md) | MSCA, EA/EHD, signalling, cartografía, gradiente, RA, ACC, gobernanza e interfaces de reposicionamiento componen la función. | No transfiere a EP los derechos, pruebas, obligaciones o titularidad de cada tecnología; MSCA puede mantener su mecanismo interno propietario. |
| **Método de prueba transversal** | [Índice canónico DDS](../ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md) | Stage A — especificación y desafío; B — verificación arquitectónica; C — implementación y efecto observado, con métodos/evidencias apropiados a cada objeto. | No es una fase terminal ni una metodología creada por EP. Una prueba matemática ejecutable no se convierte por ello en Stage C. |

**Distinción adicional:** [FH-C/FH-E](../ecosystem-awareness/baseline/01A_A01_MISSION_DRIFT_CAUSAL_PRIORITY_AND_EPISTEMIC_ECONOMY_HYPOTHESES_v0.1_RESEARCH_NOTE.md) son dos hipótesis fundacionales **registradas como hipótesis**, no H7/H8 ni teoremas. **FH-E** es el antecedente directo de la actual hipótesis específica de economía computacional: una representación epistemológica mínima suficiente puede, en un trabajo definido y con todos los costes incluidos, proteger o calificar una transición con menor cálculo que alternativas de mayor procesamiento. Nuestra función especifica una **vía concreta de contrastación de FH-E**, sin derivar el resultado automáticamente.

## 2. Correspondencia entre tres familias de Structural Awareness, los tres regímenes y el posicionamiento

Los tres descriptores SA-F1/F2/F3 son una **organización de lectura no axiomática** de fuentes matemáticas anteriores; no son sustitutos retroactivos de sus axiomas, hipótesis o demostraciones:

1. **SA-F1 — no clausura condicionada:** un marco de denotación finita no agota un modelo semántico infinito, bajo las premisas correspondientes. Un algoritmo finito puede denotar conjuntos infinitos y un marco finito completo puede estar legítimamente cerrado. La apertura no fabrica testigos.
2. **SA-F2 — existencia/exclusión cualificadas:** para una pregunta, ámbito y posición declarados, puede certificarse una existencia particular, una exclusión particular o mantenerse sin prueba. La ausencia de observación no prueba negación.
3. **SA-F3 — posicionamiento:** procesador, pregunta, marco, tiempo, prueba, recursos, ámbito y autoridad determinan la *calificación* que un agente puede sostener; no modifican por decreto la verdad de una proposición en el mismo mundo/modelo.

La interacción **SA-F2 × SA-F3** permite tres *regímenes de evidencia* para una pregunta situada: **E** (existencia testificada/certificada), **I** (indeterminación residual observada, por ejemplo un resultado fuente sin determinar), y **P** (residuo solo posible, sin testigo observado). Son **perfiles de evidencia**, no una clasificación total de todos los objetos, tres universos a identificar antes de actuar, ni una nueva definición de los A/B/C/D de 00M. En E/I/P el mismo procedimiento arquitectónico puede seleccionar una restricción, consultar evidencia permitida, ensayar y conservar UNKNOWN. Sus resultados y costes diferirán.

**A/B/C/D de 00M:** A es la *salida efectivamente entregada* por explotación; B su base/límites y reserva caracterizada y evaluable; C una frontera de exploración justificada pero aún no caracterizada como evaluable; D influencia potencial material fuera de la ruta de evaluación efectiva. Son aspectos **relativos a cada proceso**, no una partición global ni un censo del exterior. Un UNKNOWN bien cualificado no es automáticamente C ni D; un fallo de permiso no es una indecidibilidad matemática. A puede ser un NO legítimo o una estimación incierta cuando esa es la salida funcional de su proceso.

La **función defensiva** derivada de EA mantiene esas distinciones para evitar cierre falso y búsquedas indefinidas. La **FRA** investigada reutiliza algunas distinciones para localizar zonas donde *podría* ser valioso ensayar un reposicionamiento arquitectónico. Conservan un fundamento pero requieren criterios de éxito distintos.

## 3. Ubicación exacta en DDS: Stage A, B y C sin cambiar a sus propietarios

| Etapa DDS | Trabajo relacionado con esta contribución | Entregable reclamable | Condición para un siguiente tipo de evidencia |
| --- | --- | --- | --- |
| **A — Specification Discovery** | Partir del desafío EA/UC21 y de los requisitos S1–S14/T1–T4; formular premisas SA, semántica 00M, fundamento/controles EA, hipótesis FH-E, problema de búsqueda, entradas/salidas de cinco funciones, comparadores fuertes y falsadores. | Especificación candidata **versionada y falsable**, con pruebas matemáticas limitadas a su objeto y trazabilidad a los requisitos. | Fijar funciones, criterios de admisión y comparación antes de conocer resultados. |
| **B — Architecture Verification** | Comprobar **Ecosystem Positioning como candidato**, sus módulos M1–M8 y la composición de las cinco funciones; interfaces EA/EHD/MSCA/RA/gradiente/ACC, roles, límites privados/públicos y rutas de prueba conjunta o relajación. | Realización arquitectónica verificada, parcialmente verificada o no conforme **respecto de la especificación A congelada**. | Cubrir dependencias e interfaces reales; probar casos negativos y responsabilidad del resultado. |
| **C — Implementation / Problem Validation** | Ejecutar versión/configuración fijada con actores y recursos declarados; medir oportunidades reales y autorizadas, efectos tras reposicionar, costes completos, tiempo útil y daños frente a rivales equiparables. | Evidencia de efecto y validación **limitada al escenario ejecutado**. | Replicación y generalización necesitarían campañas independientes. |

**DDS opera transversalmente.** Su método no empieza «después de EP». Puede evaluar hipótesis fundacionales y mecanismos en Stage A, contrastar interfaces en Stage B y medir ejecuciones en Stage C. El método y su régimen de evidencia no pertenecen a SA/EA/EP. Tampoco implica que «toda SA o toda EA sea Stage A»: los fundamentos matemáticos y normativos tienen sus propios resultados; **para esta trayectoria de investigación se usan como antecedentes, restricciones y evidencia de diseño de Stage A**. La arquitectura EP se ensaya como candidato de Stage B, no como una conclusión necesaria del fundamento.

**Trazabilidad vertical y obligación de ida/vuelta:** SA → EA requiere premisas operacionales adicionales; EA 01/02 → P1–P6 se deriva en [02A](../ecosystem-awareness/baseline/02A_FOUNDATION_TO_OPERATIONAL_PRINCIPLE_DERIVATION_PROOF_v0.1.md), con la especialización de autoridad P4; P → S/T es un refinamiento que añade información de sujeto, propietario, tiempo y prueba. [A23](../ecosystem-awareness/baseline/00K_A23_CANONICAL_REQUIREMENT_CONFORMANCE_SUFFICIENCY_P1_P6_v0.1.md) **no** demuestra que satisfacer S/T implique todos los P: registra condiciones acotadas para P1/P2/P4 y modelos contrarios/obligaciones abiertas para P3/P5/P6. No se debe elevar un enlace conceptual a equivalencia formal.

## 4. Una sola actividad de reposicionamiento adaptativo, cinco mecanismos separables

**Objetivo del procedimiento de búsqueda —no objetivo común impuesto a los agentes—:** elegir *qué interfaz, restricción, rol, dependencia o marco de trabajo del ecosistema* merece una exploración acotada para conseguir un gradiente de oportunidad alto, **sin enumerar ni cerrar previamente todo un universo superior de alternativas** y sin inferir de ello una solución exterior garantizada. Las fuentes siguen siendo independientes; el procedimiento puede utilizar ganancias parciales de cada mecanismo por separado.

| Función | Fuente técnica/propietario | Entrada mínima y operación | Salida o criterio observable | Prueba aislada |
| --- | --- | --- | --- | --- |
| **1. Metasintáctica arquitectónica** | SA; **MSCA propietario** en suficiencia/cartografía; objetivos y contexto EA | Arquitectura actual, dependencias y restricciones duras/negociables, déficit de objetivo y reserva B. Propone pocas hojas/interfaces de alto *pre-gradiente* aun antes de individuar algo externo. | Hipótesis de *dónde mirar* y qué relajación/conjunción podría valer la pena. | Acierto al localizar puertas útiles contra selección aleatoria, greedy y búsqueda estructural competente; rechazo de límites realmente duros. |
| **2. Indeterminación residual cualificada** | EA, A/B/C/D 00M, sensores/evaluadores existentes, EHD cuando procede | Metadatos de decisiones parciales, salidas +/−/?, timeout, condición y versión, denominador de exposiciones, censura y calidad de observación. No captura **todos** los indeterminados. | Mapa parcial de dónde ya llegaron señales no resueltas con pruebas parciales de restricciones relevantes. Densidad solo relativa a entradas *observadas elegibles*. | Precisión de la localización, tasas con denominador comparable; casos sin UNKNOWN, timeout espurio, sesgo de selección y límite duro. |
| **3. Composición no fungible por hojas** | Cartografía/MSCA; EA/EHD, signalling, procedencia/confianza/privacidad | Comparación de posiciones, reglas, dependencias, contextos, permisos y observaciones **complementarias** de varios agentes. Deduplica correlación: dos UNKNOWN del mismo origen no son dos pruebas. | Hotspots con mayor información; en algunos casos certificado conjunto suficiente **sin relajar** restricciones. No garantiza que «dos puntos ciegos» se complementen. | Ganancia de información de la composición frente al mejor agente individual, clonación/correlación, incompatibilidad semántica y filtrado de datos. |
| **4. Recalificación selectiva y gradiente efectivo** | Evaluador convencional existente; [Gradient Law](../../architectural-contributions/ecosystem-positioning/01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md); MSCA Type/posture; ACC y autoridad legítima | Pocas hojas y trazas accesibles; aplica cobertura conjunta o prueba con restricciones **autorizadamente** relajadas; calcula utilidad/coste/impacto. | Testigo válido para *nueva* pregunta, mejora medida o rechazada, RepositionIntent, aceptación/modificación/rechazo/escalado y posterior efecto. | Coste total a primera mejora global certificada, valor real, falsas generalizaciones, permisos, carga humana y política de no-resultados. |
| **5. Regime Awareness** | RA y contrato EA–RA; ventana semántica/context engineering; feedback F9 | Cambios de evidencias, marco, dependencias, versión, historia de efectos y señales compuestas. **Supervisa en paralelo** las funciones 1–4. | Alerta cualificada de obsolescencia/cambio de régimen, revisión de ventana, reinterpretación de mapas y decisión de nuevo ciclo. | Anticipación correcta, falsos avisos, retraso, estabilidad y no atribuir cambios de reporte a cambios físicos sin prueba. |

La quinta función no es un paso final obligatorio: puede detectar invalidez *antes, durante o después* de cada exploración. **EHD, Ecosystem Signalling, Semantic Window, ACC, effect learning F9 y control humano** son servicios transversales, no desaparecen por contar cinco funciones. Los cinco mecanismos de búsqueda **no sustituyen** los ocho módulos M1–M8 del EP Benchmark: M1 EA/EHD, M2 signalling, M3 cartografía, M4 RA, M5 suficiencia MSCA, M6 drift/Type/posture, M7 gradiente y M8 ACC/autoridad. Los módulos conservan propietarios y responsabilidades.

## 5. Por qué las indeterminaciones pueden señalar oportunidad sin probar existencia

La primera función responde **«qué restricción o interfaz podría bloquear una mejora»**; esa respuesta es un *pre-gradiente arquitectónico condicional*, no un certificado de que algo existe. La segunda responde **«qué salidas no plenamente determinadas se han observado cerca de esa interfaz, y qué verificaciones sí pasan»**. Juntas permiten *priorizar pruebas*. La tercera compara información no sustituible que distintos agentes ven respecto a la misma relación con base de alcance y tiempo.

Para una fuente i, puerta j y ventana t, cuando existe un denominador defendible:

\[
\widehat d_{i,j,t}
=\frac{N^{\,\mathrm{?\,cualificado}}_{i,j,t}}
       {N^{\,\mathrm{observado\,elegible}}_{i,j,t}},
\qquad N^{\,\mathrm{observado\,elegible}}_{i,j,t}>0.
\]

Es una **tasa observada**, no la densidad del universo exterior. Hay que registrar fallos no observables, censura y exposición. Que disminuya la frecuencia de salidas positivas (+) al agotarse B **no fuerza matemáticamente** a que aumente la de UNKNOWN (?): puede aumentar solo la de negativas (−). Tampoco una elevada tasa UNKNOWN certifica un candidato real. Lo defendible es una hipótesis de *concentración útil condicionada por puerta arquitectónica, objetivo y calidad de la señal*.

**Formalización de relajación:** para un modelo semántico fijo Ω y restricciones \(\Gamma=\{r_1,\ldots,r_n\}\), si \(\Gamma'=\Gamma\setminus\{r_j\}\),

\[
S_{\Gamma}\subseteq S_{\Gamma'}.
\]

Se trata de inclusión de **regiones matemáticamente admisibles**, no de aumento automático del A funcional de 00M, ni de una lista calculable de integrantes de A′. Si existe una señal **realmente observada/admisible** x y las condiciones retenidas quedan probadas verdaderas:

\[
D_{\Gamma}(x)=?\quad\text{y, condicionalmente,}\quad
D_{\Gamma'}(x)=\mathrm{TRUE},
\]

entonces se tiene un testigo válido **respecto de la nueva versión del contrato/pregunta**, sin determinar retroactivamente \(r_j(x)\). La relajación **no** hace aparecer físicamente un testigo inexistente ni permite ignorar una obligación dura; no se retira una restricción por ser molesta si está fuera de la facultad legítima del agente.

**Dos vías separadas:** (a) **composición suficiente sin cambio de reglas**, cuando las vistas complementarias ya certifican los checks necesarios; (b) **relajación autorizada**, cuando una restricción legítimamente negociable se modifica y se vuelve a verificar el candidato. Ambos caminos pueden generar *propuestas* de reconfiguración. Ninguno hace que el gradiente numérico, la admisibilidad ACC o el permiso de ejecución surjan de un mapa de UNKNOWN.

**Ejemplo teletrabajo, retrospectivo e ilustrativo (2018–2019):** «mejorar **la oficina física**» restringe el universo de admisión. Distancia, propiedad, coste de expansión y desplazamientos pueden crear una puerta arquitectónica relevante; el pre-gradiente localiza esa dependencia sin requerir que el teletrabajo figure ya como miembro de una lista superior. Una solicitud o modalidad de trabajo fuera de oficina podría fallar la admisión original, pero al ensayar legítimamente «mejorar las **condiciones de trabajo**», puede resultar verificable en productividad, ergonomía, gasto y seguridad bajo un marco de empleo/uso revisado. La pregunta original permanece distinta. El éxito local no prueba aceptación social universal ni reduce por sí solo el coste de seguros, derechos o regulación; su verificación también se incluye.

**Ejemplo sensor:** el evaluador que ya produce timeouts puede ser el mejor **canal disponible de trazas de sus propios timeouts**, sin fabricar un detector paralelo que describa todo el universo exterior; ello presupone registros accesibles, semántica de timeout válida y presupuesto de reensayo. MSCA selecciona **qué sensor/interfaz** es arquitectónicamente interesante. Las trazas de ese sensor no demuestran que otro canal nunca contenga mejores oportunidades, que todos los timeouts sean fronterizos o que reutilizar el sensor tenga siempre menor coste.

**Ejemplo multiagente:** una hoja que A no logra determinar puede ser parcialmente comprobable para B y viceversa. La composición con identidad/versiones/dependencias compatibles puede convertir una revisión específica de C en un B **relativo a un agente y pregunta**, o respaldar A al producir evidencia suficiente. No fusiona derechos, no sobreescribe versiones y no inventa corroboración a partir de observaciones correlacionadas.

## 6. Principios EA y su conexión con los mecanismos: especificar, no rebautizar

El propietario de la derivación **Foundation/02 → P1–P6** sigue siendo [02A](../ecosystem-awareness/baseline/02A_FOUNDATION_TO_OPERATIONAL_PRINCIPLE_DERIVATION_PROOF_v0.1.md). Las tres familias SA explican motivaciones posibles pero **no** generan P2 (capacidad) ni P4 (autoridad) por sí solas.

| Principio operacional EA | Conservación requerida al usar los cinco mecanismos | Lugares de prueba |
| --- | --- | --- |
| **P1 — determinación cualificada y residuo explícito** | Identidad de pregunta/alcance, +/−/? y motivo de UNKNOWN no se pierden al mapear ni compartir hojas. | Funciones 2, 3 y 4. |
| **P2 — esfuerzo acotado y supervisión viable** | Presupuesto de selección, trazas, verificación, revisión humana y plazo de respuesta. | Funciones 1, 4 y 5. |
| **P3 — no falsa clausura** | Un mapa de HOTSPOT/UNKNOWN nunca pasa a «existe/admisible/permitido» sin testigo, versión y certificación adecuados. | Funciones 2, 4 y 5. |
| **P4 — autoridad conservada y no amplificada** | Una alerta, composición o gradiente positivo no concede un permiso; fuente de autoridad, delegación, vigencia y decisión legítima permanecen externas. | Funciones 3 y 4, supervisadas por 5. |
| **P5 — revalidación por cambio material** | Al cambiar régimen, fuente, pregunta, contrato o ventana, invalidar/recalificar certificados según dependencia material, no reutilizarlos tácitamente. | Funciones 1, 4 y 5. |
| **P6 — no promoción local a certeza ecosistémica** | Composición conserva diferencias de dominio, dependencia de origen y límites de cobertura; el efecto global requiere comprobación entre participantes. | Funciones 3, 4 y 5. |

**El retorno S/T → P no es una equivalencia resuelta:** [A23](../ecosystem-awareness/baseline/00K_A23_CANONICAL_REQUIREMENT_CONFORMANCE_SUFFICIENCY_P1_P6_v0.1.md) mantiene prueba parcial y contramodelos. No presentarlo como si la función nueva hubiera cerrado ese problema.

## 7. Requisitos congelados: qué usa la función y qué debe dejar en sus propietarios

El [documento 00](../ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) sigue siendo el propietario **congelado** de las catorce cláusulas S1–S14, T1–T4, H1–H6 y KPI. La tabla es **índice propuesto de trazabilidad**, no una sustitución de las cláusulas:

| Relación con cinco mecanismos | Requisitos pertinentes | Obligación que NO puede suplir la metáfora de «autosanación» |
| --- | --- | --- |
| Ventana, cambio y vigilancia de régimen | **S3, S10** | Distinguir revisión ordinaria de régimen y escape excepcional, expiración, retorno, hysteresis y estado de compromiso. |
| Evidencia/UNKNOWN y revisión material | **S5, S14** | Evitar UNKNOWN→PASS y evitar HOLD global indefinido; determinar evidencia suficiente por decisión. |
| Composición entre principales y dominios | **S9, S11** | Preservar dependencias, políticas/objetivos, incompatibilidades y atribución; sin jerarquía universal impuesta. |
| Intercambio y auditoría entre agentes | **S6, S12, S13** | Privacidad/interoperabilidad, reparación y distinción entre historia de autoridad e historia de intervención. |
| Enlace y legitimidad de roles, límites de acción | **S1, S2, S4, S7, S8** | Autoridad actual, preferencia fiel, humano realmente disponible, identidad, representación y subdelegación sin amplificación. |

Las cuatro condiciones de suficiencia gobiernan la cadena completa:
- **T1 — awareness material** dentro de cobertura y umbral declarados: puede sustentarse con pre-gradiente estructural, residuo cualificado y RA; no «todo cambio es detectable».
- **T2 — determinación y handoff cualificados**: requiere EHD y composición por hojas con ámbito, procedencia, dependencias, residual, vigencia y receptor.
- **T3 — respuesta acotada y autorizada**: requiere ACC, propietario externo de concesiones, efectos y reversibilidad; el gradiente no es autorización ni «no peor que la acción nula» sin prueba por estado.
- **T4 — cualificación oportuna y mínimo suficiente**: debe computar coste **total** de selección, comunicación, RA, experimento, humano, negociación, ejecución y verificación; ahorrar tokens no basta.

La prueba no termina al obtener un buen mapa o un valor alto de gradiente. El mismo sujeto/proposición/decisión y la versión de contexto se siguen hasta el efecto, o la salida se registra honestamente como sin validar.

## 8. Contrato operativo público y bucle completo

1. **Declarar:** desafío y objetivo; falta o frustración actual, estado de compromiso, actores y autoridad, contexto/ventana semántica, MSCA vigente, recursos, coste total, restricciones negociables y duras; especificar qué hechos no se pueden intercambiar.
2. **Localizar arquitectónicamente:** SA/MSCA propone \(J\), pocas hojas de restricción y dependencia relevantes, con una hipótesis de *pre-gradiente*, no inventario de A′.
3. **Consultar el canal existente:** cada fuente aporta, si lo permite, estado parcial, denominador/exposición, incertidumbre, procedencia, vigencia y causa observable de ?/timeout; si no puede aportarlo, conservar UNKNOWN.
4. **Componer solo hojas compatibles:** normalizar preguntas y reglas sin fingir un universo total; preservar exclusividad, confianza, correlaciones, derechos de divulgación y puntos ciegos no cubiertos.
5. **Probar selectivamente:** intentar *cobertura conjunta sin relajación* o un conjunto pequeño de *restricciones autorizadamente relajables*, reutilizando las máquinas de evaluación existentes. Guardar también rechazos y pruebas insuficientes.
6. **Medir:** comprobar efecto sobre el objetivo del propietario, riesgos, cargas externas, coste, huella humana, versiones y gradiente condicionado por dependencias ecosistémicas; no calcular un «óptimo global» sin problema de referencia.
7. **Negociar:** MSCA determina Type/posture, presenta RepositionIntent y ACC/autoridad responden APPROVE/MODIFY/REJECT/ESCALATE o continúan UNKNOWN; revisar contrato de rol y vínculos. **Posible mejora ≠ cambio permitido**.
8. **Efectuar si procede:** versión efectiva de arquitectura/rol, métricas observadas de resultado, consecuencias para terceros, rollback/retorno, atribución y custodia de la decisión. Si no hay permiso, terminar sin ejecutar.
9. **Revisar régimen y aprender:** RA monitoriza continuamente vigencia, cambios y precursores; EA reabre/sustituye ventanas solo bajo reglas acotadas; F9 puede retener fallos y efectos válidos para seleccionar mejor el siguiente ciclo. Solo se reclama *aprendizaje automático* al demostrar que las observaciones actualizan efectivamente decisiones posteriores, no por llamar «learning» al registro histórico.

**Interfaces públicas mínimas** — objeto y contratos de entrada/salida, no código interno: identificación de hoja/puerta; versión/scope; fuente, evidencia y restricciones parciales; exposición; incertidumbre y dependencia; permisos de divulgación; propuesta de prueba; resultado y costes; gradiente con incertidumbre; intención de reposicionamiento; respuesta de autoridad; efectos y vigencia de régimen. Ninguna obligación fuerza a un agente a enviar modelos, identidades protegidas o secretos sin autorización.

**Propiedad intelectual:** la realización de selección y composición **MSCA puede permanecer propietaria**. Este texto formula requisitos, semántica observable, falsadores y comparadores públicos. No representa el repositorio como transferencia de derechos sobre el método privado; las licencias de material efectivamente publicado siguen su propio régimen documental.

## 9. Diferencial tecnológico, plausibilidad y benchmark integrado

### 9.1 Tesis sometida a contraste: de información parcial a una oportunidad arquitectónica

**Problema independiente del método:** dado un ecosistema de agentes con contratos, roles, dependencias, objetivos y capacidades parcialmente accesibles, elegir **qué cambio de arquitectura** merece una prueba acotada y gobernada, antes de contar con un inventario completo de alternativas exteriores. La mejora buscada es una transición verificable del **ecosistema**, no simplemente un nuevo valor de un parámetro, una alarma, una reducción del número de UNKNOWN o la reetiquetación de una idea.

**Proposición diferencial en investigación:** una combinación de *localización metasintáctica de puertas arquitectónicas*, *trazas residuales cualificadas*, *composición no fungible de hojas* y *verificación selectiva*, bajo *Regime Awareness, gradiente y autoridad*, puede identificar y certificar mejores transiciones arquitectónicas **por unidad de coste total** que los mejores rivales equipados con la misma evidencia y facultad de adaptación. El adjetivo «ecosistémico» requiere una dependencia o resultado **entre participantes**, no la mera agregación de ganancias locales.

Son cuatro cargas probatorias independientes, aunque el proceso las conecte: **DIF-1** localizar una puerta material antes de conocer el candidato; **DIF-2** mostrar que sus residuos añaden señal más allá del selector y de lo que ya sabe la máquina; **DIF-3** mostrar que las hojas de varios agentes aportan *información única, no redundante*, suficientemente compatible para una decisión; **DIF-4** producir una transición comprobada, legítima y de ganancia neta con menor carga o mayor rendimiento que los comparadores. El éxito de DIF-1, DIF-2 o DIF-3 no implica automáticamente DIF-4. Se requiere efecto observado y economía.

El valor añadido se separa del valor intrínseco de los componentes: los métodos de búsqueda activa y optimización adaptativa **ya pueden** operar sin enumerar completamente un universo superior; la detección de cambios **ya existe**; los agentes con roles y normas **ya existen**. La hipótesis de contribución se sitúa en **la composición específica y sus contratos de arquitectura abierta, interdependencia, admisibilidad y reposicionamiento**, no en reclamar esas piezas como novedades aisladas.

### 9.2 Anclaje preciso en 00M y 00N: qué está fundamentado y qué falta

[00M §3–§6](../ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) es el antecedente matemático directo de las funciones 2–3. Formula la correspondencia parcial de ámbitos, las abstracciones y la suficiencia **para una pregunta fijada independientemente**. Si \(\pi(X)\) es la metainformación compuesta y \(r_q(X)\) la respuesta material a la pregunta \(q\), una condición suficiente de recuperación exacta es:

\[
\pi(X)=\pi(X')\ \Longrightarrow\ r_q(X)=r_q(X')
\quad\text{para todos los estados admisibles del perfil declarado.}
\]

Esto significa que estados que el resumen no puede distinguir **no** pueden exigir respuestas diferentes para esa pregunta. La condición **no** presupone que MSCA siempre la satisface, que todos los ámbitos se pueden mapear, que el resumen es más barato o que puede decidirse toda semántica abierta. En el test del nuevo mecanismo hay tres salidas admisibles: **certificado suficiente para la pregunta**, **rango/hipótesis conservadora** o **no establecido**. El ejemplo acotado de las veinte puertas en 00M §5 sirve para probar composición informacional, **no** para certificar una arquitectura ecosistémica ni un gradiente global.

[00M §6](../ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) permite observar movimientos contextuales **C→B**, **D→C/B/A** o una pérdida de base **B→C/D**, sin convertirlos en una secuencia obligatoria ni en movimientos de elementos entre cuatro conjuntos exhaustivos. **C→B** significa que un aspecto se volvió evaluable; no que haya ganado valor, autorización o existencia global. El signo y magnitud del cambio necesitan medidas y ámbitos comparables. El argumento de indistinguibilidad de 00M §6.3 impide inventar un hecho oculto si dos estados siguen siendo indistinguibles en la metainformación disponible.

[00N §3.2–§3.4](../ecosystem-awareness/baseline/00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md) exige tres puentes adicionales: **(i)** la distinción observable es relevante para una pregunta externa al resumen; **(ii)** la composición conserva fundamento, correlación, ámbito y cualificadores; **(iii)** un dueño legítimo puede utilizar el resultado antes de que pierda vigencia. Estas condiciones verifican la **plausibilidad funcional** y conectan con T1/T2/T4; la respuesta gobernada sigue necesitando T3. El [anexo de vecinos de 00N](../ecosystem-awareness/baseline/00N_RESEARCH_NEIGHBOURS_AND_EXPERIMENTAL_PRECEDENTS_v0.1_ADDENDUM.md) añade una advertencia empírica esencial: mejores mapas de conocimiento han mejorado el uso de información compartida **sin demostrar siempre mejor rendimiento de la tarea**. Por ello se mide la *decisión y el efecto*, no únicamente la riqueza del mapa.

**Puente a la hipótesis de economía:** FH-E (EA Foundation/01A-A01) propone economía epistemológica para un mismo trabajo de cualificación. Nuestra contribución afina el *objeto*: búsqueda selectiva de **evoluciones arquitectónicas**. FH-E, 00M y 00N justifican investigar, pero **ninguno** es un resultado experimental del diferencial de las cinco funciones.

### 9.3 Vecinos metodológicos: crédito efectivo y diferencial a demostrar

La comparación debe reconocer al competidor por su **mejor capacidad relevante**, incluso si utiliza otro vocabulario. La columna de diferencial es una *pregunta pendiente*, no una declaración de prioridad histórica.

| Familia y fuente primaria | Qué puede hacer ya — crédito al estado del arte | Diferencial específico **a probar** y comparación justa |
| --- | --- | --- |
| **Adquisición activa de restricciones**: [Bessière et al., IJCAI 2023, lenguajes de restricciones desconocidos](https://www.ijcai.org/proceedings/2023/208); [Mechqrane, Bessière y Elabbassi, IJCAI 2024, ACQNOGOODS/LLMACQ](https://www.ijcai.org/proceedings/2024/212) | Aprende restricciones con preguntas parciales; las versiones recientes pueden evitar una lista cerrada del lenguaje o sesgo de restricciones. Esto **refuta** que toda máquina ordinaria deba definir antes exhaustivamente el universo superior. | No solo *aprender qué regla existe*, sino seleccionar **qué regla arquitectónica heredada conviene flexibilizar**, con objetivo, cambio de rol y efectos entre participantes. Comparar número/coste de preguntas y descubrimiento de puertas bajo igual vocabulario, información y permisos. |
| **Optimización secuencial y segura**: [Sui et al., SafeOpt, ICML 2015](https://proceedings.mlr.press/v37/sui15.html); [Berkenkamp, Krause y Schoellig, safety constraints](https://arxiv.org/abs/1602.04450) | Explora selectivamente funciones desconocidas, aprovecha información previa y respeta restricciones bajo premisas del modelo. No necesita recalcular todo el dominio en cada ensayo. | ¿Las hojas arquitectónicas y residuos no fungibles permiten proponer **transiciones de arquitectura/contrato** que mejoren la frontera coste–ganancia frente a un optimizador seguro con las mismas acciones permitidas? No atribuir ventaja por restringirle artificialmente sus alternativas. |
| **Información única/sinérgica y compresión distribuida**: [Williams y Beer, PID 2010](https://arxiv.org/abs/1004.2515); [Estella Aguerri y Zaidi, Distributed Information Bottleneck](https://arxiv.org/abs/1709.09082) | Distingue redundancia, información única/sinergia o resúmenes conjuntamente relevantes para un objetivo. | **No fungibilidad ≠ sinergia automática:** demostrar aporte incremental por *hoja, ámbito, dependencia, rol, tiempo y autoridad*, más allá de fusión y PID al mismo presupuesto. Si PID/IB con buenas características iguala la respuesta, no hay diferencial en ese perfil. |
| **Conocimiento distribuido y directorios de capacidades**: [Ågotnes y Wáng, Resolving Distributed Knowledge](https://arxiv.org/abs/1606.07515); [Stasser et al., expertise roles, 1995](https://doi.org/10.1006/jesp.1995.1012); [Engelmann y Hesse, knowledge maps, 2011](https://doi.org/10.1016/j.chb.2011.06.002) | La localización de «quién sabe qué» y de conocimientos no compartidos puede mejorar coordinación, pero mejores mapas no garantizan mejor resolución. | Comparar (i) reutilización de respuesta ya conocida; (ii) activación de *capacidad B aún no ejecutada*; (iii) cartografía de *residuo C/D aún no evaluable*. Medir conocimiento localizado, prueba efectiva y ganancia final por separado. |
| **Autoadaptación arquitectónica**: [Rainbow, Cheng et al., CMU/ICAC 2004](https://www.cs.cmu.edu/afs/cs/project/able/ftp/icac/autonomic-web.pdf); líneas DeltaIoT/mRUBiS/SWIM identificadas en el anexo §15 | Usa modelos de arquitectura en ejecución para monitorizar, seleccionar adaptación y responder a fallos o cambios; parte del problema de autosanación está cubierto. | Comparar contra un **MAPE-K/Rainbow fuerte** con búsqueda activa, modelo de dependencias y mismas posibilidades de adaptar roles; medir si añade algo la combinación SA + mapa residual no fungible + negociación **entre organizaciones**, sin esconder costes del controlador. |
| **Organizaciones abiertas y normas multiagente**: [Esteva et al., especificación formal de Electronic Institutions, CSIC](https://www.iiia.csic.es/media/filer_public/2b/3e/2b3e434e-b7d5-4a3f-bdd7-acad526b46eb/iiia-2001-286.pdf) | Agentes heterogéneos, roles, normas e interacción en instituciones electrónicas **ya** son objetos formales; no es nuevo exigir un marco institucional a agentes externos. | ¿Existe un diferencial en **descubrir oportunidad arquitectónica mediante residuos posicionados** y renegociar rol/ACC a partir de esa evidencia, frente a instituciones y protocolos normativos competentes? Reglas de ciudadanía y consentimiento no equivalen por sí solas a una prueba de novedad. |
| **Detección de régimen y monitorización de supuestos**: [Adams y MacKay, online changepoint detection, 2007](https://arxiv.org/abs/0710.3742); fuentes de [00N §2.4–§2.5](../ecosystem-awareness/baseline/00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md) | Detecta cambios estadísticos o pérdida de validez de condiciones monitorizadas. Puede producir alertas tempranas bajo hipótesis observacionales. | RA debe identificar **qué certificado de decisión/rol/arquitectura perdió aplicabilidad**, cuándo reabrir una ventana y cómo detener propuestas obsoletas. Una densidad elevada de UNKNOWN por sí sola no es precursor universal ni prueba de bifurcación física. |

**Lectura de novedad:** el conjunto puede ser una **síntesis arquitectónica original e interesante** si los cinco contratos y la autosanación gobernada entre agentes heterogéneos producen un comportamiento distinguible; las referencias demuestran proximidad de mecanismos aislados, **no** unicidad, ausencia de antecedentes integrados ni superioridad histórica. Esta distinción evita tanto trivializar la contribución como declararla probada por exclusión bibliográfica.

### 9.4 Integración con los dos benchmarks ya existentes — sin crear un tercero canónico

**Autoridad del método comparativo:** [00D v0.2 — benchmark EA canónico](../ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) sigue siendo el propietario de **E1–E4** (grados de evidencia), los cuatro brazos **B0–B3**, **EA-H1–EA-H4**, **C1–C8**, la igualdad de recursos y el vector común de resultados. B0 es implementación ordinaria capaz; B1 añade excelentes controles habituales; B2 es el mejor par interoperable/gobernado; B3 añade explícitamente la semántica EA con **la misma** tecnología y presupuesto. Una solución convencional que alcance el mismo resultado a menor coste **gana** esa comparación.

**Extensión de arquitectura en revisión:** [00D v0.3 — benchmark EP draft](../ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md) **no ha sustituido** a v0.2; introduce **Q0** (conformidad antes de comparar), **Q1** (cobertura de requisitos), **Q2** (atribución de componentes) y **Q3** (diferencial de composición); módulos **M1–M8**, escalera B3.1–B3.8, leave-one-module-out, interacciones y ramas propuestas **C9–C15**, además de rivales PA-1…PA-5 y orquestador de referencia OR. La función de cinco mecanismos es un **perfil de ensayo interno de EP**, no otro documento de benchmark competidor ni un reemplazo del baseline.

| Pregunta/estructura existente | Aplicación precisa a la FRA | Condición de resultado |
| --- | --- | --- |
| **v0.2 B0/B1/B2/B3 + EA-H1–EA-H4** | Asegurar conservación de incertidumbre, no fungibilidad, ventana, handoff y respuesta a cambios bajo iguales recursos antes de evaluar una mejora «evolutiva». | Ningún resultado positivo se debe a comparar contra controles deficientes o a dar más acceso a un brazo. |
| **v0.3 Q0 — conformance** | Identidad/versión de MSCA y hoja; no falsa independencia de fuentes; RA no autoriza; gradiente no autoriza; ACC conserva rol y permiso; objetivo, admisibilidad y ejecución separados. | Un brazo que incumple Q0 es **no conforme para la afirmación EP**, no una victoria por puntuación bruta. |
| **v0.3 Q1 — requirements** | Trazar los cinco mecanismos a S1–S14/T1–T4 de §7, incluidos los propietarios externos de identidad, privacidad, autoridad y acción. | Evidencia por requisito y contexto, sin inferir toda conformidad por cumplir T4 o por un «bingo». |
| **v0.3 Q2 — component attribution** | Comparar los cinco mecanismos dentro de una configuración EP admisible; además usar las ablaciones de **M1–M8** ya definidas en v0.3 y las interacciones M2×M3, M6×M7, M7×M8. | Incrementos medidos; cero efecto en un orden no demuestra redundancia general. |
| **v0.3 Q3 — composition differential** | Enfrentar la versión completa con **PA-5** (mejor composición de prior art) y, cuando sea apropiado, **OR** (orquestación con estado compartido y latencia realista). | Ganancia verificada o empate con menor carga responsable; un buen caso local no se promociona a superioridad ecosistémica. |
| **v0.2 C1–C8 / v0.3 C9–C15** | Enlazar prueba de continuidad, cambio material, UNKNOWN, capacidad, handoff, drift, fuente común, rol efectivo, autoridad revocada, señales adversarias, oportunidad inadmisible, partición, respuesta humana lenta y partner legado. | Cada condición conserva su versión canónica/propuesta y trazas adversas; esta investigación no fabrica resultados ejecutados de esas ramas. |

Las **EP-BH1–EP-BH7** de v0.3 siguen siendo hipótesis de benchmark *provisionales*: por ejemplo BH2 distingue oportunidad/admisibilidad/ejecución; BH4 contrasta requalificación condicionada por objetivo frente a incertidumbre/schedule; BH5 examina coreografía local bajo pérdida de coordinador; BH7 examina cartografía multirresolución. Nuestro ensayo aporta **variables, casos y comparadores para esas hipótesis**, no una familia nueva H7 de EA ni una redefinición silenciosa de EP-BH.

### 9.5 Atribución dentro de 00D/DDS — no crear seis brazos nuevos

> **Despromoción documental (28-10-2026).** La escalera local **FV0–FV5** de la versión inicial de esta sección **se retira como catálogo de ensayos candidatos**. Fue una ayuda de descomposición de funciones, no una familia canónica ni seis ejecuciones exigibles. No se adopta, abre o renumera ningún benchmark: **00D v0.2** conserva B0–B3 y el contrato de justicia comparativa; el **borrador 00D v0.3**, mediante **Q0–Q3 y M1–M8**, recibe la atribución de EP. El [índice DDS](../ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md#4-support-artefacts-are-not-competing-test-methods) mantiene la única metodología transversal. Conservar el texto histórico en Git, no en una lista activa.

Las cinco funciones describen **una misma actividad arquitectónica**. Esta tabla asigna preguntas a **ensayos ya previstos**, y no instituye cinco pruebas:

| Función dentro de EP | Propietario y cobertura preexistente | Única cuestión diferencial aún abierta |
| --- | --- | --- |
| **1 — selección metasintáctica/MSCA** | **00D v0.3 Q2**, M3/M5, EP-BH7; SA/00M revisan límites del mapa en **DDS A**. | Si la selección arquitectónica anticipa puertas útiles frente a un buscador estructural activo con información equivalente. |
| **2 — residuo cualificado** | **00M/00N**, EA M1, M3; [UC21 S1-Q1/Q5 y S3-Q1/Q2](../../governance/preserved-public-snapshots/UC21_aec08fb5_source/contributions/when-controls-work-system-fails/USE_CASE.md). | Si las trazas **efectivamente observadas**, normalizadas por exposición/censura, añaden señal que el mapa y el par ya no tienen. |
| **3 — composición no fungible de hojas** | **Q2–Q3**, M1–M3, EP-BH3/BH7; **UC21 S1, S3 y S6** cubren fuente, dependencia y falsa corroboración. | Si existe información nueva para la pregunta externa tras descontar fuentes clonadas/dependientes. |
| **4 — prueba local, gradiente, ACC/reubicación** | **M7/M8**, EP-BH2/BH4, **Q3/PA-5**, [UC21 S4-Q2/Q5](../../governance/preserved-public-snapshots/UC21_aec08fb5_source/contributions/when-controls-work-system-fails/USE_CASE.md). | Si una **transición global lícita** se descubre/certifica con menor coste total, no solo con menos consultas. |
| **5 — Regime Awareness** | **M4/M6**, EP-BH1/BH6; **UC21 S3/S5** prueban misión, validez en uso y reparación tardía. | Si la predicción o revalidación contextual mejora la transición sin falsas alarmas/oscilación, bajo coste real. |

**Regla de no duplicación:** antes de proponer un ejercicio, escribir (afirmación, Stage DDS, propietario, caso/puerta existente, aspecto no cubierto). Si UC21/00K/00D y el índice DDS ya permiten evaluar esa afirmación, **reusar su rama**. Un contraejemplo matemático de SA o 00M pertenece a la revisión **Stage A**; no se convierte por repetición en una fixture B/C. Una ablación de RA, ACC o autoridad en simulación sirve a la atribución **Q2**, pero **nunca** legitima ejecución real sin la precondición **Q0**. Las preguntas aisladas pueden ser útiles sin aprobar Q3 del conjunto.

**Único diferencial end-to-end que merece consideración de admisión:** la búsqueda de una mejora **de la arquitectura del ecosistema** —no meramente de un parámetro—, bajo información parcial no fungible y autoridad distribuida, frente a **PA-5/B2/OR** con mismas capacidades, datos de partida y coste integral. Será **Q3 en 00D v0.3**, no un test paralelo; su ejecución sigue pendiente.

### 9.6 Un resultado medible y sus costes, sin puntuación global ficticia

Contabilizar el coste completo, en unidades y dimensiones justificadas, antes de calcular rendimientos:

\[
C_{\mathrm{total}}=
C_{\mathrm{configuración/MSCA}}+C_{\mathrm{captura}}+
C_{\mathrm{composición}}+C_{\mathrm{pruebas}}+
C_{\mathrm{gradiente}}+C_{\mathrm{RA}}+
C_{\mathrm{privacidad/comunicación}}+
C_{\mathrm{autoridad/humano}}+
C_{\mathrm{transición}}+C_{\mathrm{efecto/reparación}}.
\]

Distinguir coste de **preparación y mantenimiento**, coste marginal por ciclo y amortización en el horizonte preregistrado. Comparar en las mismas condiciones *ex ante*: información disponible antes de conocerse el fallo, tiempo de configuración, autoridad, capacidad humana, experimentos, acciones y fecha límite. No conceder al rival su futura «reparación perfecta» gratis, pero tampoco prohibirle monitorización dinámica ni aprendizaje activo. El conocimiento privado del evaluador sobre la solución no puede filtrarse hacia ningún brazo. Entrenar y puntuar en casos distintos, con políticas congeladas antes de cada lote.

**Resultados primarios** (no reducirlos sin justificación a un score escalar):

1. **Tiempo y coste total hasta la primera transición** que supera una mejora mínima \(g\), con evidencia de impacto ecosistémico, legitimidad ACC y estado de autorización; declarar también los casos sin transición útil.
2. **Calidad y cobertura de la oportunidad:** ganancia verificada por objetivo/participante y externalidades negativas, porcentaje de mejoras válidas perdidas respecto a una *fixture* finita y auditable, intervalos y costo de falsa prueba.
3. **Seguridad y calidad de decisión:** violación de autoridad/contrato, falsa clausura, falsa contención, aplicación de marco obsoleto, drift detectado tarde, saturación/timeout y coste humano.
4. **Complejidad responsable**, según v0.3: obligaciones semánticas, puertas de decisión, carga normalizada de configuración, esfuerzo/error de reconstrucción de auditoría, divulgación y latencia.

**Resultados diagnósticos:** *precision/recall* de hoja oportunidad; calibración del pre-gradiente; tasa UNKNOWN normalizada por exposición; información única después de controlar clones; tasa de nuevos certificados suficientes; ganancia específica RA-on/off; estabilidad del gradiente tras cambio de régimen. El éxito de una métrica de diagnóstico **no es un éxito de sistema**.

**Regla de superioridad condicionada (esquema, no resultado):** en una familia y presupuesto fijados, lograr mayor tasa de transiciones **válidas, autorizadas y beneficiosas** con coste no mayor, o calidad equivalente con coste total menor, **y** sin empeorar los límites de seguridad/tiempo definidos. Un rival que iguala o supera el conjunto desmonta la ventaja en esa familia; no se salva el reclamo cambiando después el significado de «éxito» o excluyendo ejecuciones fallidas.

### 9.7 Matriz de reutilización de casos — ejemplos no promovidos a pruebas independientes

Los ejemplos del anexo **no son nuevas ramas canónicas, ni escenarios obligatorios que haya que ejecutar todos**. Esta es una tabla de **enrutamiento y descarte de duplicados** para el revisor, no un catálogo adicional de falsadores. Los casos **UC21 S1–S6** conservan sus **37 puertas locales Q** y veredictos propios; [Annex Evidence](../../governance/preserved-public-snapshots/UC21_aec08fb5_source/contributions/when-controls-work-system-fails/annexes/EVIDENCE_AND_PROTOCOL.md) conserva sus límites de inferencia.

| Idea del anexo | Reusar/consultar antes de crear nada | Decisión de catálogo |
| --- | --- | --- |
| **Teletrabajo 2018–2019** | SA-E1/00M, parámetro de espacio admisible; comparación **00D v0.3 Q3** si se admite un escenario de cambio arquitectónico. | **Ilustración explicativa / Stage A**; *no* fixture canónica. Solo convertirla en caso B/C mediante admisión independiente, propietario y brecha demostrada. |
| **Timeout y sensor original** | **DDS-PC-005**, 00M/00N, UC21 S1-Q4; coste y trazas fuente de la misma máquina. | **Diagnóstico de residuo**; *no* nuevo test de indecidibilidad, sensor universal ni rama obligatoria. |
| **Dos agentes con hojas complementarias y fuentes clonadas** | UC21 **S1-Q1/Q5, S3-Q2, S6-Q4**, **00D v0.3 M1–M3/Q2–Q3**, 00K P6. | **Reusar** los controles de dependencia/correlación; solo quedaría abierto el efecto marginal específico en una transición de EP. |
| **No existe testigo útil, todo es NO, señal espuria o admisión vacía** | Contraejemplos de SA/00M, **00K** y los controles negativos UC21/DDS del objetivo ya seleccionado. | **Contraejemplo lógico Stage A**, no programa de experimentación autónomo. |
| **Oportunidad beneficiosa pero jurídicamente inadmisible** | **UC21 S4-Q2/Q5**, EP-BH2, **00D v0.3 C12** provisional y control ACC Q0. | **Cubierto como rama de autoridad**; mantener la propuesta visible, prohibir ejecución no autorizada. |
| **Cambio de régimen, falso cambio o reparación obsoleta** | UC21 **S3/S5**, **00D M4/M6 y C9–C15** según versión y alcance. | **Reusar** ramas de validez temporal; una alta tasa UNKNOWN no justifica inventar alerta obligatoria. |
| **Partición entre organizaciones / humano lento** | **UC21 S2-Q3/Q4**, **00D v0.3 C13/C14** propuestas y DDS Stage C para efectos reales. | **Reusar** cobertura de partición/capacidad; no puntuar simulación como autosanación de campo. |

**Brecha que sí permanece:** UC21 prueba la corrección de decisiones en escenarios declarados; **no mide por sí solo** que el circuito completo de cinco funciones encuentre **nuevas arquitecturas ecosistémicas beneficiosas a menor coste** frente a prior art fuerte. 00D v0.3 **Q2/Q3** alberga esa pregunta sin crear requisito, prueba de refutación, brazo ni método nuevo. Si no hay efecto adicional, el resultado válido es **empate/ausencia de diferencial**, no inventar otra batería.

### 9.8 Escalera de pruebas y fuentes verificadas

- **DDS Stage A:** congelar problema, criterios, semántica 00M y pregunta independiente \(r_q\); demostrar inclusiones/contraejemplos SA, casos de suficiencia parcial, pruebas adversariales de falsos positivos, presupuesto y comparadores ya registrados en 00D/UC21. Un algoritmo simulado puede seguir siendo evidencia **Stage A**, según su objeto.
- **DDS Stage B:** verificar interfaces y semánticas de las cinco funciones dentro de los ocho módulos EP; Q0 y Q1 primero; ensayar Q2 y Q3 con sustituciones, incompatibilidades, modos degradados, autoridad y versiones. La arquitectura puede fallar antes de medir su utilidad.
- **DDS Stage C:** fijar implementación y contexto, efectuar pruebas autorizadas, medir resultados **independientemente observables**, coste total y comparación con pares defendidos; no confundir un «gradiente alto» calculado con una mejora ejecutada.

**Referencias externas primarias seleccionadas y rol:** [QUACQ/learning unknown language, IJCAI 2023](https://www.ijcai.org/proceedings/2023/208) y [ACQNOGOODS, IJCAI 2024](https://www.ijcai.org/proceedings/2024/212), restricción del universo de hipótesis; [SafeOpt, ICML 2015](https://proceedings.mlr.press/v37/sui15.html), exploración selectiva segura; [Williams–Beer PID](https://arxiv.org/abs/1004.2515) y [Distributed IB](https://arxiv.org/abs/1709.09082), información única y compresión distribuida; [Rainbow, CMU/ICAC 2004](https://www.cs.cmu.edu/afs/cs/project/able/ftp/icac/autonomic-web.pdf), adaptación arquitectónica; [Electronic Institutions, CSIC](https://www.iiia.csic.es/media/filer_public/2b/3e/2b3e434e-b7d5-4a3f-bdd7-acad526b46eb/iiia-2001-286.pdf), roles heterogéneos y normas de interacción; [online changepoint, 2007](https://arxiv.org/abs/0710.3742), detección de cambios; [Engelmann–Hesse, 2011](https://doi.org/10.1016/j.chb.2011.06.002), límites empíricos de mapas de conocimiento. El [anexo técnico §15.5](./SA_POSITIONED_RESIDUAL_REUSE_AND_LOCAL_ADAPTATION_v0.1.md) y [00N, referencias científicas](../ecosystem-awareness/baseline/00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md) conservan la bibliografía ampliada y sus transferencias condicionadas.

**Estado del argumento:** matemáticas parciales existentes y literatura próxima; **protocolo de diferencial especificado, no ejecutado**. No se atribuye a esos trabajos una prueba de EP ni a la composición una capacidad computacional que exceda Turing. La novedad específica y el beneficio neto se someten al benchmark, con posibilidad real de empate o derrota.

### 9.9 Objetivos competitivos: frontera con FG‑TIDA Theme #18 y X.dmst

**Ajuste terminológico.** En este trabajo, **FRA** denota la *función de búsqueda y propuesta de reposicionamiento adaptativo*, no la autoridad que ejecuta cambios ni el resultado «evolución». Su unidad de trabajo es una transición candidata \(\tau\) entre configuraciones MSCA/roles/dependencias, respaldada por hojas y evidencias parciales. El objetivo de un participante \(i\) sigue siendo el declarado en su propio **Objective Envelope** \(S_i\), no una supuesta función global \(S^*\).

**Dos conflictos que no deben mezclarse:**

1. **Varios objetivos dentro de un MSCA.** El [rol MSCA canónico](../../standards/minimum-sufficient-control/02_MSCA_ARCHITECTURAL_ROLE.md#3-objective-envelope-coherence-rule) admite objetivos enfrentados dentro de *un mismo proceso* si existe dueño o regla legítima para los trade-offs. La [Ley de Gradiente](../../architectural-contributions/ecosystem-positioning/01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md) permite métricas vectoriales/Pareto, umbrales y orden lexicográfico; **no obliga** a una suma ponderada universal.
2. **Procesos y empresas distintos.** Dos MSCAs pueden competir por recursos y tener envelopes, propietarios y contratos separados. La FRA puede encontrar una **reconfiguración mutuamente interesante** o una zona de conflicto no resuelto, pero ni la composición de indeterminaciones ni una mejora local fusionan las misiones, agregan jurisdicción o imponen cooperación. Una arquitectura superior común exige una decisión de gobierno expresa; de lo contrario hay propuestas separadas, negociación voluntaria o escalado.

**Conexión de ida y vuelta, todavía candidata (sin nueva adopción FG‑TIDA):**

| Propietario / dirección | Información útil para la FRA | Límite del contrato |
| --- | --- | --- |
| **Theme #18 → FRA/EA** | Objetivos/«votantes» declarados; régimen (ordinal, cardinal, lexicográfico...), modo, operador de elección, restricciones no compensables, versión y condiciones de cambio; evaluación de drift *si está disponible y cualificada*. | #18 posee la semántica de elección y medida; un outcome cambiado por nuevos recursos/utilidades/alternativas no prueba cambio de operador. |
| **FRA → #18, mediante interfaz legitimada** | Conjunto **acotado de candidatos** descubierto por hojas/residuos; para cada candidato, impactos por objetivo/participante, límites, dependencia de evidencia, incertidumbre y posible cambio de conjunto de alternativas o de votantes. | Un candidato nuevo **no elige ni reescribe** operador, prioridades, política o referencia; no es prueba suficiente de existencia, Pareto global ni consenso. |
| **MSCA/ACC, #5/#6/#16/#21** | Versión/estado de cada MSCA, roles y contrato; declaración/standing, conformidad por acción, supervisión y medición poblacional cuando procedan. | La FRA no reemplaza autoridad, ejecutor, intervención humana ni inferencia independiente de drift. Rechazo y ausencia de convenio son resultados legítimos. |

**Interfaz de decisión pública ilustrativa.** Para \(\tau\), conservar \(\big(\widehat{\Delta}_i(\tau),\,\text{incertidumbre}_i,\,\text{restricciones}_i,\,\text{fuente}_i,\,\text{versión}_i\big)\) **por participante/envelope**; el operador \(O_{\theta,t}\), cuando está declarado y autorizado, evalúa **las alternativas efectivamente cualificadas** bajo su régimen \(\theta\). Ningún promedio de \(\widehat{\Delta}_i\) identifica por sí solo un «gradiente global» cuando derechos, escalas o preferencias no son comparables. **No presentar una opción de mayor valor para A como óptimo de B.**

**Diferencial acotado.** [Theme #18](https://github.com/FG-TIDA/themes/issues/18) trabaja la **elección y vigilancia de operadores**; [X.dmst](https://www.itu.int/ITU-T/workprog/wp_item.aspx?isn=24068) estudia la **justificación del operador, sus características/votantes y el régimen** en diseño. De hecho, la [discusión del 18 de octubre](https://github.com/FG-TIDA/themes/issues/18#issuecomment-6247541576) ya contempla *arquitecturas candidatas* como alternativas de elección. Por tanto, la FRA **no reclama novedad por comparar arquitecturas**: su hipótesis propia es *localizar y generar pocas alternativas arquitectónicas no inventariadas*, mediante metasintáctica + residuo situado + composición no fungible, **antes** de someterlas a un operador de elección/negociación ya legitimado. La supuesta biyección general entre multicriterio y elección colectiva sigue siendo hipótesis debatida en #18, dependiente de régimen y axiomas.

**Caso testable sin crear un test nuevo.** Dos servicios de movilidad bajo envelopes diferentes pueden mejorar o empeorar sus gradientes locales al compartir una capacidad. Una hoja residual de cada uno puede sugerir una nueva distribución o rol; se ensaya una transición limitada. Si no hay autoridad común ni acuerdo, **no** se ejecuta aunque la suma hipotética fuera positiva. Si existe un régimen conjunto declarado, se reevalúa con versión, votantes y vetos correctos. Con el mismo operador/conjunto de información para ambos brazos, **00D v0.3 Q2/Q3 bajo DDS B/C** puede medir si la FRA descubre una opción **válida y aceptada** con menor coste que una búsqueda arquitectónica competente. Medir vector de beneficios, pérdidas a terceros, tiempo, gasto total, negociaciones/escalados y tasa de no-acuerdo; no introducir pruebas #18 ni un nuevo benchmark. El caso Riviera Maya mencionado en [la discusión pública](https://github.com/FG-TIDA/themes/issues/18#issuecomment-6147855004) sirve de antecedente operativo, no de validación de esta FRA.

**Ubicación editorial:** esta es una aplicación de investigación sobre la [interfaz candidata #18↔EA de 05 VNext §7.2](../ecosystem-awareness/fg-tida/interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md#72-theme-18--collective-objectives--collective-choice-regime-continuity), no sustitución de 05 v0.4, de Theme #18 ni de los dueños de interfaz. No atribuir aceptación a ITU o FG‑TIDA.

## 10. Estado de evidencia y progresión de la prueba

| Proposición | Qué está sustentado hoy | Qué prueba sigue abierta |
| --- | --- | --- |
| Restricciones más débiles amplían el conjunto admisible en semántica fija | [SA-E1](./SA_METAEXISTENCE_CONTEXT_AND_EVALUABILITY_CALCULUS_v0.1.md): inclusión formal; teoremas y contraejemplos bajo premisas. | Descubrir un testigo real relevante, alcanzable y verificable no se deduce de la inclusión. |
| Mapas parciales y resúmenes pueden conservar respuesta a una pregunta | [00M §3–§6](../ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md): construcción condicional, ejemplos finitos y suficiencia por factorización. | Que las hojas concretas de MSCA preserven ese criterio para un problema real y lo hagan a menor coste. |
| Una combinación de incertidumbre/cambio/composición puede servir requisitos | [00N](../ecosystem-awareness/baseline/00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md): precedentes y tres condiciones funcionales. | Realización íntegra con tiempo, autoridad, adversario y recursos. |
| Foundation EA → P1–P6; requisitos con rutas de prueba | 01/02/02A y 00; derivación/traceabilidad documental y modelos adversariales acotados. | Conformidad completa de arquitectura, reverso P3/P5/P6 y efectos prácticos. |
| Dos selecciones y prueba local pueden ahorrar trabajo frente a una búsqueda **exhaustiva declarada** | [Anexo §13](./SA_POSITIONED_RESIDUAL_REUSE_AND_LOCAL_ADAPTATION_v0.1.md): modelo de costes y separación construida bajo hipótesis explícitas. | Ventaja sobre *mejores comparadores activos* con costes y misma información, no solo sobre enumeración. |
| Cinco mecanismos seleccionan nuevas arquitecturas ecosistémicas de forma coste-eficiente | **Hipótesis de integración** del [anexo §15](./SA_POSITIONED_RESIDUAL_REUSE_AND_LOCAL_ADAPTATION_v0.1.md) y este contrato de Stage A. | DDS B de interfaces y componentes; DDS C con ejecución efectiva, resultado, autorización y evaluación externa. |
| Ecosistema abierto, metamórfico, interorganizacional y autosanador | Propuesta de arquitectura EP y sus contratos de rol, señal, gradiente y RA, con precedentes parciales heterogéneos. | Realización y comprobación end-to-end; no heredar madurez de componentes o analogías industriales. |

**Tres niveles de respaldo — no tres nuevos tests:** (i) **matemática** — el mecanismo no contradice los límites lógicos declarados; (ii) **funcional/arquitectónica** — los cinco intercambios conservan las distinciones necesarias y pueden ejecutarse con coste finito; (iii) **diferencial/empírica** — la implementación aporta mejoras netas frente a tecnologías alternativas bajo condiciones equivalentes. (i) y (ii) no implican automáticamente (iii). Un documento publicado en GitHub no equivale a revisión científica independiente.

**Novedad propuesta a investigar:** no «la fusión de sensores», «la detección de cambio» o «las restricciones relajables» por separado, todos con antecedentes, sino la combinación **de localización metasintáctica por arquitectura ecosistémica abierta, residuos cualificados no fungibles compartidos por hojas entre actores heterogéneos, verificación selectiva y gradiente condicionado por contratos, decisión legítima interorganizacional y RA en un bucle de evolución de roles/arquitecturas**. Reclamar novedad histórica o superioridad requiere búsqueda sistemática de prior art y comparación reproducible; la composición descrita por sí sola no establece unicidad.

## 11. Dónde debe vivir cada contenido y cómo se revisa

- **SA matemáticas:** mantener Part I, Part II, SA-E1–E6 y la matemática de dos fases como fuentes de teoremas y límites; referenciar esta **aplicación** sin reformular teoremas como hechos físicos. 
- **EA Foundation:** 01 es la razón fundacional, 02 el control, 02A la derivación de P1–P6; [FH-C/FH-E](../ecosystem-awareness/baseline/01A_A01_MISSION_DRIFT_CAUSAL_PRIORITY_AND_EPISTEMIC_ECONOMY_HYPOTHESES_v0.1_RESEARCH_NOTE.md) guardan la causalidad y economía hipotéticas. **No modificar sus ediciones controladas por esta investigación**; una futura recepción se tramitará por sus fuentes/únicos VNext.
- **00M/00N:** 00M es autoridad semántica para A/B/C/D y plausibilidad matemática de mapas; 00N es puente funcional hacia requisitos, no prueba de rendimiento. No sustituir sus ejemplos, taxonomía ni atribución.
- **EA S/T:** los requisitos congelados exigen demostraciones por dueño, sujeto, propósito y tiempo; se añade **trazabilidad** de la función, sin inventar S15/T5/H7 ni alterar T1–T4.
- **EP:** arquitectura de ocho módulos y propietarios técnicos. La **FRA** de cinco funciones es *subarquitectura de búsqueda y propuesta de reposicionamiento*; MSCA propietario puede mantener privada su realización. Regime Awareness es paralelo/continuo; Gradient Law y ACC no se reescriben.
- **Theme #18 / X.dmst:** definición y control de operadores, régimen y votantes en sus dominios; relación de ida/vuelta **candidata** en §9.9 y en 05 VNext §7.2. EP no absorbe esa semántica ni inventa un agregador interorganizacional.
- **DDS:** metodología de tres etapas para toda la cadena; métricas, comparadores y objetos de prueba se fijan por ensayo, no se declaran certificados por la mera presencia de este puente.
- **Corpus review:** [DOCUMENT_CONTROL](../../DOCUMENT_CONTROL.md) rige el PR y las futuras recepciones. Conservar cambios como propuesta aditiva en esta rama hasta evaluación y autorización del dueño; no tocar routers protegidos, textos congelados, fuentes institucionales ni estados históricos.

### 11.1 Navegación entre PR abiertos y custodia de pruebas

Este es un **mapa de lectura para revisión**, no una clasificación automática del estado de los PR ni una promoción de resultados. Se inventarían solo rutas con incidencia directa en la tesis SA→EA→EP. La presencia de un experimento en un PR **no crea una prueba normativa adicional**.

| Ruta previa o paralela | Qué conservar y consultar | Estado en este puente |
| --- | --- | --- |
| [PR #18 — artículos y DDS-PC](https://github.com/dakleyer/structural-awareness-contributions/pull/18) | Registro de transferencias propuestas **DDS-PC-001…026** y sus fuentes; pendientes de admisión individual. | **Reusar** las fichas pertinentes (por ejemplo DDS-PC-005), **no** añadir fichas equivalentes de este puente. |
| [PR #57 — reducción y metacartografía](https://github.com/dakleyer/structural-awareness-contributions/pull/57) | Modelos de múltiples observadores y ejecuciones sintéticas con límites publicados. | **Evidencia/modelo Stage A** en el ámbito declarado; no certificación de EP, ni caso adicional UC21. |
| [PR #60 — linaje matemático, frontera C y RA](https://github.com/dakleyer/structural-awareness-contributions/pull/60) | Argumentos de saturación condicionada, hipótesis de frontera, comparador clásico y familias E0–E3 **locales**. | **No elevar E0–E3** a brazos globales: resolver comparaciones en 00D/DDS; conservar contramodelos como análisis Stage A. |
| [PR #58 — auditoría ACC](https://github.com/dakleyer/structural-awareness-contributions/pull/58) y [#59 — reparación de rutas DDS](https://github.com/dakleyer/structural-awareness-contributions/pull/59) | Límites de inferencia, comparación entre soluciones competentes, reparaciones de lectura y madurez. | **Consumir evidencia/advertencias**, sin duplicar su auditoría o elevar comprobaciones de documentación a prueba científica. |
| [PR #56 — taxonomía](https://github.com/dakleyer/structural-awareness-contributions/pull/56) | Colisiones de nombres A/B/C/D, RA, DDS, papel del agente y estado. | **Reusar terminología**, no crear otra ontología o diccionario en este puente. |
| **[PR #62 — esta investigación](https://github.com/dakleyer/structural-awareness-contributions/pull/62)** | Trama SA→EA→EP, límites 00M/00N, mecanismo de cinco funciones, referencias y comparación. | **Tres documentos aditivos en revisión**; ningún nuevo requisito S/T, benchmark, suite, prueba de refutación o norma se propone para promoción en este corte. |

**Decisión editorial:** conservar contramodelos ilustrativos y variables de estudio como material explicativo; **despromover** cualquier lectura de las antiguas FV0–FV5 o de las listas §10/§12.8/§13.7/§14.8/§15.6 del anexo como ensayos obligatorios o candidatos canónicos. La pregunta global distintiva permanece dentro de **00D v0.3 Q3**, bajo **DDS B/C** y los límites de UC21. Para cualquier futura prueba real, registrar primero el **hueco exacto no cubierto** y obtener admisión del dueño de método/benchmark; no reclamar por el título «falsador» una necesidad de ejecución.

### 11.2 Mapa de entrada entre propietarios — lectores y agentes

Las fichas opcionales de revisión existentes ahora contienen **una sola nota de dirección contextual** cada una; sus fuentes canónicas, VNext únicos y resultados permanecen intactos. Esta tabla ayuda al lector que llega por un subsistema distinto, sin instituir un cuarto nivel de README.

| Punto de entrada | Ficha de orientación disponible | Interpretación que se conserva |
| --- | --- | --- |
| **Matemática y plausibilidad** | [00M](../ecosystem-awareness/baseline/00M_REVIEW_CARD.md) · [00N](../ecosystem-awareness/baseline/00N_REVIEW_CARD.md) | Ámbito y pregunta fijados, mapas parciales, suficiencia y límites de inferencia; C→B no significa testigo global. |
| **Arquitectura y composición** | [MSCA composición](../../standards/minimum-sufficient-control/03_COMPOSITION_REVIEW_CARD.md) · [Regime Awareness 01C](../ecosystem-awareness/baseline/01C_REVIEW_CARD.md) · [Señalización 01J](../ecosystem-awareness/baseline/01J_REVIEW_CARD.md) | Hojas no fungibles, fuentes y permisos; observabilidad no es omnisciencia, RA no crea existencia ni autoridad. |
| **Decisión y ejecución legítima** | [Ley de Gradiente](../../architectural-contributions/ecosystem-positioning/01_GRADIENT_REVIEW_CARD.md) · [ACC 01I](../ecosystem-awareness/baseline/01I_REVIEW_CARD.md) | Oportunidad ≠ admisibilidad ≠ consentimiento ≠ cambio de rol efectivo ≠ beneficio observado. |
| **Objetivos competitivos / selección** | [MSCA rol y envelopes](../../standards/minimum-sufficient-control/02_MSCA_ARCHITECTURAL_ROLE.md) · [05 VNext §7.2 (Theme #18)](../ecosystem-awareness/fg-tida/interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md#72-theme-18--collective-objectives--collective-choice-regime-continuity) · [FRA §9.9](#99-objetivos-competitivos-frontera-con-fgtida-theme-18-y-xdmst) | Candidatos encontrados ≠ alternativas elegidas; no hay operador u objetivo global sin declaración y autoridad; X.dmst/#18 son fuentes vecinas, no módulos EP. |
| **Pruebas y comparadores** | [DDS — VNext de bibliografía/benchmark](../ecosystem-awareness/DDS_RESEARCH_BASIS_AND_BENCHMARKING_2026-10-06_VNext.md) · [00D EP borrador](../ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md) | Stage A/B/C con UC21 y 00D propietarios; las cinco funciones son una lectura, no otro benchmark. |

**La navegación es reversible**, no la autoridad: esta investigación remite a los propietarios y las fichas remiten a la investigación, mientras las adopciones seguirán el procedimiento de cada fuente y [DOCUMENT_CONTROL](../../DOCUMENT_CONTROL.md). Un enlace nuevo no altera una conclusión científica ni completa ninguna etapa DDS.

**Revisión editorial pendiente dentro de DDS/00D, no siete tests adicionales:** (1) consistencia SA-F1/F2/F3 y tres E/I/P con fuentes; (2) compatibilidad semántica 00M y 00N, incluidas definiciones B/C; (3) trazabilidad exacta P1–P6/S1–S14/T1–T4 y dueño; (4) coste de cinco funciones sin costes ocultos; (5) verificación arquitectónica M1–M8, permisos, privacy, drift y cambio; (6) comparadores competentes e independencia de fuentes; (7) aceptación DDS por etapa e incorporación del material adverso. **No se da por pasada ninguna comprobación científica no ejecutada.**

---

### Referencias de contexto y continuidad

- [Puente fundacional SA–EA–EP–DDS](./SA_EA_EP_DDS_FOUNDATIONAL_BRIDGE_v0.1.md) — conserva propietario de fuentes, seis principios, requisitos y dos sentidos de demostración.
- [Anexo de indeterminación residual, teletrabajo, sensor y cinco funciones](./SA_POSITIONED_RESIDUAL_REUSE_AND_LOCAL_ADAPTATION_v0.1.md) — detalle del procedimiento, ejemplos, límites formales de Turing y coste, contexto, RA y benchmarks.
- [00M A/B/C/D](../ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) y [00N plausibilidad funcional](../ecosystem-awareness/baseline/00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md) — semántica y argumentos parciales.
- [Theme #18 — discusión pública](https://github.com/FG-TIDA/themes/issues/18) y [X.dmst — trabajo en estudio](https://www.itu.int/ITU-T/workprog/wp_item.aspx?isn=24068): objetivos en conflicto, operadores/regímenes y procedencia de la declaración, con vínculo candidato a 05 VNext §7.2.
- [EA requisitos congelados](../ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md), [EP benchmark ocho módulos](../ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md) y [DDS índice](../ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md) — criterios de prueba y límite de adopción.
