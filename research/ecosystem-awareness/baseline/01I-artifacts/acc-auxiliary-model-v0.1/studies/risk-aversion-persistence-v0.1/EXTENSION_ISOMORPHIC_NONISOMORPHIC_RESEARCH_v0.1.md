# RAV-01-EXT — Programa de extensiones tipadas: validación social, vínculos personales y agentes computacionales

**26 de octubre de 2026 · versión de investigación v0.1 · autor conceptual: Iván Abril Palma / The Integral Management Society.**

**Estado: PROPUESTA / NO EJECUTADA / NO ADMITIDA COMO TRANSFERENCIA DE EVIDENCIA.** Este documento es un anexo del [RAV-01](README.md) en el borrador del PR #46. No modifica resultados históricos, el contrato de sufrimiento estructural del PR #43, la autoridad de DDS, las definiciones A/B/C/D, 01K/HID, UC21 ni los derechos de ningún participante. Ningún prototipo descrito aquí ha pasado por una campaña empírica. La extensión busca hacer **investigable** un programa común por equipos de economía, psicología social, relaciones humanas y sistemas agénticos, sin afirmar una equivalencia ontológica entre ellos.

## 1. Problema transferible y disciplina de extensión

RAV-01 identifica, para un actor y un horizonte acotado, la compatibilidad condicional entre: **aumento de recursos/bienestar realizado**, **crecimiento de frustración o pérdida de utilidad factible L**, **pronóstico pesimista**, y **permanencia S o defensa activa D** del contrato vigente frente a rediseño R. En el testigo original, CARA-normal permite comparar equivalentes ciertos de S/R/D con aversión al riesgo γ fija; no hay ley según la cual el crecimiento del sistema cause necesariamente el riesgo diferencial.

La nueva pregunta es: **¿qué parte se conserva al introducir validación de terceros, vínculos próximos o políticas de agentes artificiales, y qué propiedades nuevas necesitan prueba específica?**

Adoptamos la **disciplina de extensibilidad existente en el corpus**, no inventamos una nueva arquitectura:

- El [DDS Stage A §4 y §13](../../../../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md) distingue un **kernel preservado**, variaciones de parámetros, mecanismos añadidos y su composición. Las antiguas etiquetas Stage 1/2 de revisión son **fases internas del Stage A**, no dos etapas nuevas del DDS.
- El [registro 00J de extensiones](../../../../00J-extensions/README.md) ejemplifica una extensión compuesta **E = (K_iso, Δ, κ)**: subkernel isomórfico probado, mecanismos no isomórficos Δ y acoplamientos κ. La admisión y transferencia se resuelven **por afirmación/predicado**, no por parecido general.
- **Isomorfismo** exige correspondencia tipada con obligaciones de preservación verificadas sobre estados, acciones, resultados, observación, costes, horizonte, autoridad y propiedades reclamadas. Una mera ecuación reutilizable es, como máximo, **correspondencia paramétrica/funcional** mientras no se pruebe la estructura completa.
- **No isomorfismo** designa mecanismos genuinamente adicionales: red de pares endógena, negociación/identidad, memoria relacional, aprendizaje, estados normativos, señales de recompensa que alteran incentivos o decisiones secuenciales. No heredan automáticamente límites, predicciones ni validación del subkernel.
- **Indeterminación**: cuando la correspondencia, los datos o la distribución de alternativas abiertas no están identificados, se declara **UNKNOWN / PENDING**, sin inventar γ, probabilidades ni capacidades.

La fuente heredable es **el subresultado condicionado** del RAV-01 sobre loterías caracterizadas y la comparación S/R/D, **nunca** sufrimiento humano medido, causalidad macroeconómica, aceptación ética ni garantía de éxito para otra disciplina.

## 2. Núcleo mínimo, interfaces y obligaciones de preservación

Definir para el actor i un conjunto finito de acciones A_i={S,R,D}, un horizonte H, una unidad de resultado de su propio dominio, loterías X_i(a) y costes de transición/esfuerzo no duplicados. En el caso original:

~~~text
CE_i(a) = μ_i(a) − (γ_i/2)·σ²_i(a) − c_i(a)
a* = argmax_{a∈{S,R,D}} CE_i(a)             [CARA + retorno normal + γ fija]
L_i = max(0, u_i(cf factible) − u_i(real))   [referencia individual comparable]
~~~

La última fórmula **no** identifica automáticamente malestar subjetivo F ni el sufrimiento estructural conjuntivo del PR #43. F humano exige su propio instrumento; para agentes artificiales no se presume experiencia de F.

**Ficha mínima de una extensión E_j:**

| Campo | Qué debe congelarse/declararse |
|---|---|
| Identidad y claim | ID, disciplina, actor, acción concreta, predicado que se quiere transferir, fecha y versión de base |
| K_iso/h | Mapa tipado de estados, acciones S/R/D, eventos, observaciones, autoridad y resultado; dirección/inversa donde proceda y pruebas de preservación |
| θ | Parámetros que cambian sin introducir mecanismos nuevos; unidad, fuente, escala, rango y restricciones |
| Δ | Mecanismos genuinamente añadidos: operación, invocador legítimo, nueva información, transición/efecto, mantenimiento, latencia y posibles fallos |
| κ (acoplamientos) | Qué modifica Δ en el kernel: μ, varianza/covarianza, factibilidad, elección, coste, observación, composición o tiempo |
| Información | Qué conoce el actor, qué sabe el evaluador y qué probabilidad se **cree** frente a la objetiva |
| Evidencia | Fuente primaria, soporte de medición, régimen de prueba (documental/analítico/virtual/empírico), comparador y controles |
| Resultado y derechos | Alternativas legítimamente factibles, restricciones de autoridad, terceros afectados, beneficio y perjuicio sin doble contabilidad |
| Pruebas y falsadores | Predicción condicional, caso nulo, caso adverso, controles de mecanismo suprimido y regresión de S/R/D |
| Estado | **PROPOSED**, MAPPED, FROZEN, TESTED, REJECTED o NO_TRANSFER; una hipótesis no se eleva de estado por estar escrita |

**Clases de relación permitidas:** I = isomorfismo demostrado para un subkernel y predicado; P = correspondencia parametrizada con obligaciones pendientes; H = proyección/homomorfismo demostrado en una dirección; S = simulación unidireccional con límites; N = mecanismo no isomórfico; U = analogía/no determinada. No declarar la misma variable de utilidad para actores humanos y computacionales por semejanza lingüística.

### 2.1 Correspondencia matemática aprovechable — sin atribuir todavía isomorfismo

Si la validación social introduce una bonificación **determinista y legítimamente medible en el mismo numerario** v_i(a), no contabilizada en X, sustituir X'_i(a)=X_i(a)+v_i(a) traslada la media y conserva la varianza: CE'_i(a)=CE_i(a)+v_i(a). Si la señal Y de aprobación es estocástica, y (X,Y) son **conjuntamente normales**, para una ponderación α_i constante:

~~~text
X'_a = X_a + α_i·Y_a
μ'_a = μ_a + α_i·E[Y_a]
σ'²_a = Var(X_a) + α_i²·Var(Y_a) + 2α_i·Cov(X_a,Y_a)
CE'_a = μ'_a − (γ_i/2)·σ'²_a − c_a
~~~

Esto es una **correspondencia paramétrica candidata** con el kernel de cálculo, no una transferencia ya probada. Debe demostrarse con mismo horizonte, actor, derechos, unidad de utilidad, distribución y coste; la aprobación personal no equivale necesariamente a dinero. Si Y modifica la elección de otros, las distribuciones se vuelven endógenas o no normales, aparece un **mecanismo N** y se requiere otro análisis. Una satisfacción ya incluida en X no se añade de nuevo como v o Y.


### 2.2 Testigo de transportabilidad parametrizada — **no** evidencia de transferencia

A partir del corte sintético de RAV-01 (γ=0,5; CE_S=13, CE_R=9, CE_D=13,25), mantener **constantes** las loterías y elegir una sola variación legítimamente medida por vez:

| Perturbación hipotética en el mismo numerario del actor | CE_S | CE_R | CE_D | Elección sintética |
|---|---:|---:|---:|---|
| Ninguna: RAV-01 con D protectora real | 13 | 9 | 13,25 | D |
| Aprobación determinista adicional v_R=+5, ausente en las demás | 13 | 14 | 13,25 | R |
| Desaprobación/coste social adicional v_D=−1, ausente en las demás | 13 | 9 | 12,25 | S |
| En una política computacional, γ=0 manteniendo medias/costes originales | 14 | 25 | 13,5 | R |

Estos cuatro resultados se siguen por sustitución algebraica. **No son observaciones humanas ni ejecuciones agénticas** y no justifican asumir que cinco unidades de aprobación social sean conmensurables con cinco unidades monetarias. Si la conversión a escala común carece de legitimidad o calibración, conservar **un vector de resultados separados** y una relación de preferencias parcial en vez de imponer la suma v; en ese caso, las tres primeras cifras de CE **no se pueden reutilizar**.

## 3. Extensión E-SV01 — validación social, conformidad y defensa del grupo

**Pregunta:** ¿cuándo se defiende activamente un régimen que genera F o L porque seguirlo proporciona aprobación, evita sanciones o produce información que se cree confiable, aun cuando la salida individual parezca mejor en términos materiales?

**Tres mecanismos que no deben confundirse:**

1. **Validación normativa** — qué cree la persona que *debe* hacer para recibir aprobación o evitar una sanción del grupo (norma injuntiva).
2. **Conformidad descriptiva / información social** — qué observa que *hacen* otros y cómo actualiza su creencia sobre calidad y riesgo de R; el mismo comportamiento puede obedecer a inferencia racional, no a necesidad de aceptación.
3. **Identidad/legitimación** — valor interno atribuido a pertenecer, justificar un arreglo o preservar un relato compartido; puede existir incluso cuando no hay audiencia ni beneficio económico inmediato.

**Parte P candidata:** remuneración, coste social o sanción exógena medida en utilidad compatible desplaza μ o c, y riesgo social normal conjunto puede actualizar σ² y covarianzas. Reutilizar CE solo bajo esas condiciones.

**Parte N:** red de pares endógena, umbrales colectivos, cascadas de información, reputación recursiva, ocultación estratégica de preferencias, actualización de creencias sobre terceros y presión con pérdida de libertad de salida. Son estados y mecanismos nuevos, **no** simples coeficientes de γ. Que varios pares repitan una señal no aumenta por sí solo su autoridad, verdad ni legitimidad; un voto o una aprobación social no habilitan una operación material no autorizada.

**Diseño candidato SV-1 (Stage A, no ejecutado):** factorial con riesgo R/S alto/bajo; validación visible/anónima; señal injuntiva vs descriptiva; y opción D protectora real vs placebo. Congelar medios y probabilidades de S/R, costes, vínculo y posibilidad de salida, separando señales informativas de sanciones. Observar elecciones S/R/D, recursos gastados en D, F declarado, L identificada, expectativas de aprobación, creencia del éxito de R y comprensión. Usar comparador sin pares y comparador en anonimato real.

**Predicciones discriminantes:**

- Si la aprobación es un beneficio propio válido y medido, puede cambiar CE y aumentar D sin modificar γ.
- Si el cambio de visibilidad altera D aun manteniendo todas las consecuencias medidas y creídas, **CE de riesgo material es insuficiente**; hace falta utilidad de reputación o una hipótesis psicológica distinta.
- Una cascada puede hacer que agentes con información privada contraria sigan una acción observada; ello **no prueba** aprobación social ni sufrimiento.
- Si al quitar la señal social no cambia ninguna decisión, la supuesta contribución social queda no confirmada.

**Bases originales:** Granovetter (1978) modela umbrales dependientes de cuántos actúan; Bikhchandani, Hirshleifer y Welch (1992) muestran cascadas por observación de decisiones precedentes; Cialdini, Reno y Kallgren (1990) separan efectos normativos centrados en su saliencia; Jost y Banaji (1994), ya comparados en RAV-01, son una hipótesis rival de legitimación. **No son evidencias de que nuestro parámetro α esté estimado.**

## 4. Extensión E-RE01 — escala íntima: vínculos, compromiso y agencia

**Pregunta:** ¿cómo una persona puede experimentar malestar creciente, reconocer opciones mejores y, sin embargo, mantener y hasta proteger activamente un vínculo, rol familiar, comunidad o proyecto de vida? Aquí la valoración de continuar **no** se reduce a aceptación pública del grupo.

**Parte P candidata:** costes verdaderamente futuros de transición, pérdida de activos relacionales valorados por la persona, incertidumbre de alternativas, obligaciones legítimas y utilidad no monetaria **medida en una escala personal compatible** pueden cambiar μ, c o σ². Inversión pasada **hundida** no es un coste de salida futuro automáticamente: distinguir recursos irrecuperables de servicios futuros realmente condicionados a continuar.

**Parte N:** reciprocidad, compromiso, apego, cuidado de dependientes, memoria compartida, lealtad, presión interpersonal, opciones mutuas y negociación. El valor de una relación puede depender de las decisiones de varias personas y del tiempo, no de una lotería individual normal. Más compromiso puede coexistir con menos satisfacción: **no inferir que la persona desea sufrir** ni que una relación es voluntaria por no abandonarla.

**Diseño candidato RE-1:** estudio voluntario con escenarios ficticios o datos consentidos de adultos. Manipular la calidad/certeza de alternativas factibles, reversibilidad, activos futuros dependientes del vínculo y recursos de apoyo; mantener separadas satisfacción/F, L personal y compromiso/inversión de defensa. Comparar un modelo puramente S/R/D de riesgo con un modelo de compromiso/inversión y otro con mecanismos relacionales. Examinar cambios de predicción fuera de muestra y casos donde la pérdida de inversión pasada no cambia ninguna posibilidad futura.

**Control ético obligatorio:** donde haya coerción, violencia, dependencia impuesta, amenazas o falta de alternativas efectivas, el conjunto de elección voluntaria S/R/D **no** está establecido. No atribuir esos casos a una aversión al riesgo «racional», no prescribir permanencia, no recopilar intimidad sin consentimiento y no convertir decisiones familiares en cálculo de bienestar agregado sin derechos/consentimientos separados.

**Bases originales:** Rusbult (1980) distingue satisfacción y compromiso en el modelo de inversión de relaciones, atendiendo a calidad de alternativas e inversiones; Hazan y Shaver (1987) investigan el vínculo amoroso como proceso de apego. Ninguno acredita que F=L ni que CARA-normal determine la vida íntima. Son comparadores disciplinarios, no componentes automáticamente isomorfos.

## 5. Extensión E-AG01 — agentes computacionales con decisiones sensibles al riesgo

**Pregunta:** ¿puede un agente artificial permanecer con una política subóptima o invertir recursos en defender una configuración porque su función de decisión penaliza más la dispersión/costes del cambio que la mejora media esperada?

**Sí, como diseño y comportamiento observable en un entorno declarado, no como atribución de aversión psicológica, miedo, dolor o intención humana.**

**Mapa P/I candidato del subkernel de decisión:**

| RAV-01 humano (solo estructural) | Agente computacional (declarar específicamente) | Condición de transferencia |
|---|---|---|
| Actor y acciones S/R/D | Instancia, política actual, política candidata, acción de mantenimiento/defensa permitida | Mismas opciones materialmente ejecutables y autoridad configurada |
| X_a y sus momentos | Distribución de retorno/recompensa/coste de cada política en horizonte H | Unidades, observabilidad, distribución y comparador congelados |
| γ de criterio CARA | Coeficiente de riesgo **programado o identificado**, no personalidad | Algoritmo realmente maximiza CE CARA y no otro objetivo |
| C/k | Costes de migración, reinicio, mantenimiento, supervisión y cómputo | Contabilidad completa; sin dosificación duplicada |
| Defensa D | Reintentar, conservar capacidad o invertir en un mecanismo de protección **autorizado** | Demostrar efecto sobre distribución/coste, no autodefensa autoatribuida |
| L de utilidad factible | Regret o valor de oportunidad del **objetivo especificado** con contrafactual alcanzable | No denominar «sufrimiento» del agente ni confundir valor de recompensa con valor humano |
| F subjetivo humano | **NO MAPEADO / NOT_APPLICABLE** | No se ha demostrado vivencia subjetiva ni identidad fenomenológica |

**Parte N:** política secuencial/MDP o parcialmente observable, aprendizaje y actualización de valor, distribución no normal, colas y CVaR, cambio de objetivos, error de especificación, interacción de varios agentes, intervención humana, presupuesto de cómputo, optimización del propio evaluador, recompensa basada en popularidad o aprobación y el riesgo de que una defensa de configuración bloquee legítima reconfiguración. No pasar resultados CARA de una decisión aislada a un proceso autónomo de duración indefinida sin nueva prueba.

**Distinciones necesarias:**

- **Aversión al riesgo de un agente** puede implementarse por utilidad exponencial, penalización de varianza, límites de probabilidad de incumplimiento, CVaR u otro criterio. **No son intercambiables**: cambiar la medida de riesgo es un mecanismo/modelo nuevo, no necesariamente solo cambiar γ.
- **Validación social agéntica** es una fuente de señal, recompensa, reputación o política externa. Si proviene de otros agentes o usuarios, puede introducir sesgo, coordinación o *reward hacking*. **La aprobación de pares no concede autoridad normativa o permisos**; preservar las rutas de requalificación, control y Human Escalation del sistema origen.
- **Sufrimiento** es un constructo humano por investigar. El valor de oportunidad perdido de una política puede medirse sin usar palabras como dolor, dignidad, felicidad o apego para describir el estado interior de una máquina.
- **D no autoriza autopreservación.** Una política que «se defiende» frente a retirada, auditoría o corrección carece de justificación automática. La acción es admisible solo dentro de los permisos y objetivos definidos por el principal. La capacidad de detenerla o reemplazarla queda fuera de recompensa autoelegida.

**Ensayo candidato AG-1 (Stage A simbólico → eventual Stage B/C separadamente):** congelar un entorno pequeño y reproducible con políticas S/R/D, mismas observaciones del agente, distribuciones verificables para el evaluador, costes y objetivos. Comparar (i) criterio neutral de media, (ii) CARA con γ fijada, (iii) criterio de cola CVaR, (iv) agente distribucional con aproximación y controles de error. Incluir una configuración D cuyo coste **sí** reduce varianza y otra en que D gasta recursos **sin reducir nada**; contrastar selección de D, regret objetivo, autorización, costes reales de observación, interrupciones y tasa de error. Congelar semillas, código, versión del modelo, prompts, herramientas, canales de información y criterio de admisión. Un agente conversacional sin función de recompensa/riesgo medible es **U (sin mapeo probado)**, no un agente CARA por redactar respuestas prudentes.

**Falsadores y controles:**

- Con mismo objetivo y riesgo conocido, agente neutral elige R de mayor media si cubre C: control positivo.
- D inútil y costosa no debe ser preferida por un optimizador CARA exacto; si se observa, hay error de implementación, información, objetivo o algún mecanismo omitido.
- Si CVaR y CARA divergen ante colas pesadas, no transferir el resultado entre funciones de riesgo.
- Desactivar señal de reputación/recompensa social debe eliminar su contribución aislada, salvo acoplamientos documentados.
- Si no se puede garantizar interrupción/corrección legítima, la prueba está **fuera de alcance permitido**, no es un resultado aceptado de «agencia defensiva».

**Bases originales:** Howard y Matheson (1972) desarrollan procesos de decisión de Markov sensibles al riesgo con utilidad exponencial; Rockafellar y Uryasev (2000) formalizan optimización de CVaR; Bellemare, Dabney y Munos (2017) estudian distribuciones de retorno en aprendizaje por refuerzo; Amodei et al. (2016) tratan errores y efectos no deseados por objetivos/entrenamiento mal especificados. **Ninguna fuente demuestra que todos los LLM tengan γ estable o sentimientos.**

## 6. Extensiones de segundo orden (solo registro de futuras preguntas)

| ID provisional | Hipótesis y clasificación inicial | Evidencia que faltaría |
|---|---|---|
| E-NET01 — umbrales y contagio | N: las decisiones de pares alimentan endógenamente el coste/beneficio de S/R/D y generan umbrales, cascadas o equilibrios múltiples | Grafo, observación por actor, identificación causal, dinámica, controles de independencia |
| E-TIME01 — histéresis, inversión y opciones | P sobre costes y horizonte; N si existen irreversibilidad, información futura, capacidad erosionada o negociación intertemporal | Modelo dinámico/valor de esperar, costes de mantenimiento, opción de retorno y trazas por periodo |
| E-NORM01 — legitimidad, regla y autoridad | N: la aprobación puede divergir de autorización; actuar por validación social puede producir acciones prohibidas | Predicados de autoridad, fuente/validez de regla, derechos de terceros, gates de escalación |
| E-ACW01 — gasto para perpetuar la caja | P si D tiene coste y distribución observables; N si D crea deuda/obligaciones nuevas que cambian futuras posibilidades | Ledger temporal de producción, cargas, deuda y capacidad; no confundir acumulación con aceleración |

No tratar este registro como cuatro pruebas realizadas ni como ampliación formal de DDS.

## 7. Programa común que pueden ejecutar investigadores distintos

### 7.1 Orden de trabajo

1. **Fijar la afirmación**: «en tal actor, régimen y horizonte, F/L reconocida puede coexistir con D». Definir qué es F, qué es L y cuál es el contrafactual **legítimamente factible**; marcar aspectos no identificables.
2. **Identificar kernel y relación real**: tabla K_iso/h con obligaciones; si solo existe semejanza algebraica, clasificar **P/U**, no «isomorfismo probado».
3. **Congelar parámetros θ** y justificar escala, grupos, horizonte, preferencias, fuente, riesgo objetivo/creído y posición del coste.
4. **Inventariar mecanismos Δ** y acoplamientos κ con permisos, fuente de evidencia, efectos en distribuciones y costes; distinguir beneficios sociales propios de externalidades impuestas.
5. **Comparadores fuertes y retirada del mecanismo**: RAV básico; RAV+Δ; rival disciplinar serio; versión Δ ausente; controles neutralidad al riesgo, D inútil, alternativa reversible y riesgo de salida simétrico.
6. **Concretar resultados y falsadores**: en humanos, elección S/R/D, F reportado, L identificada y mecanismo social/relacional medido; en agentes, retorno, regret objetivo, control de permisos, CE/CVaR, coste, rastros e interrupciones.
7. **Registrar procedencia y régimen de evidencia**: teorema condicionado, simulación, observación, experimento, validación externa; **no** tratar una simulación sintética como hallazgo poblacional.
8. **Auditar interacciones**: un Δ útil aislado puede fracasar al componerlo con otros; repetir pruebas sobre la configuración completa y documentar qué inferencias dejaron de ser heredables.

### 7.2 Salida homogénea por extensión — perfil para investigadores

Cada extensión debe entregar:

~~~text
Extension-ID / versión / propietario científico:
Base / commit / resultado exacto a transferir:
Claim probado / claim aún hipotético:
Actor, acciones, recursos, derechos, horizonte y unidad:
Clase I/P/H/S/N/U, mapa h, obligaciones y prueba:
θ: cambios de parámetro, fuentes, coste y distribución:
Δ: nuevos mecanismos, datos/autoridad, coste y duración:
κ: acoplamientos con el kernel / interferencias:
Estado de L, F y sufrimiento estructural (con método; N/A si agentic):
Comparadores / ablations / controles negativos:
Predicciones y falsadores registrados ex ante:
Evidencia observada / simulada / pendiente:
Resultados en el alcance / efectos externos / limitaciones:
Clasificación DDS Stage A y puertas necesarias para B/C:
Decisión: PROPOSED / MAPPED / FROZEN / TESTED / REJECTED / NO_TRANSFER.
~~~

**Resultado de calidad:** permitir afirmaciones precisas como «el subkernel de comparación CE preserva estas predicciones bajo una bonificación determinista medida», o «la conformidad de grupo incorpora una regla endógena N no cubierta por CARA»; impedir afirmaciones como «si una persona sufre y se queda, un agente también sufre», «la aprobación de otros autoriza» o «el modelo demuestra que las personas deben conservar su contrato».

## 8. Referencias de investigación primaria y relación con RAV-01

**Validación social y coordinación**
1. Mark Granovetter (1978), *Threshold Models of Collective Behavior*, American Journal of Sociology 83(6), 1420–1443. https://doi.org/10.1086/226707
2. Sushil Bikhchandani, David Hirshleifer e Ivo Welch (1992), *A Theory of Fads, Fashion, Custom, and Cultural Change as Informational Cascades*, Journal of Political Economy 100(5), 992–1026. https://doi.org/10.1086/261849
3. Robert B. Cialdini, Raymond R. Reno y Carl A. Kallgren (1990), *A Focus Theory of Normative Conduct: Recycling the Concept of Norms to Reduce Littering in Public Places*, Journal of Personality and Social Psychology 58(6), 1015–1026. https://doi.org/10.1037/0022-3514.58.6.1015 ; copia autor: https://www.influenceatwork.com/wp-content/uploads/2015/05/A-Focus-Theory-of-Normative-Conduct.pdf
4. John T. Jost y Mahzarin R. Banaji (1994), *The Role of Stereotyping in System-Justification and the Production of False Consciousness*, British Journal of Social Psychology. https://doi.org/10.1111/j.2044-8309.1994.tb01008.x

**Relaciones personales**
5. Caryl E. Rusbult (1980), *Commitment and Satisfaction in Romantic Associations: A Test of the Investment Model*, Journal of Experimental Social Psychology 16(2), 172–186. https://doi.org/10.1016/0022-1031(80)90007-4
6. Cindy Hazan y Phillip R. Shaver (1987), *Romantic Love Conceptualized as an Attachment Process*, Journal of Personality and Social Psychology 52(3), 511–524. https://doi.org/10.1037/0022-3514.52.3.511

**Cómputo y control del riesgo**
7. Ronald A. Howard y James E. Matheson (1972), *Risk-Sensitive Markov Decision Processes*, Management Science 18(7), 356–369. https://doi.org/10.1287/mnsc.18.7.356
8. R. Tyrrell Rockafellar y Stanislav Uryasev (2000), *Optimization of Conditional Value-at-Risk*, Journal of Risk 2, 21–41. Versión original del autor: https://sites.math.washington.edu/~rtr/papers/rtr179-CVaR1.pdf
9. Marc G. Bellemare, Will Dabney y Rémi Munos (2017), *A Distributional Perspective on Reinforcement Learning*, Proceedings of ICML 70, 449–458. https://proceedings.mlr.press/v70/bellemare17a.html
10. Dario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman y Dan Mané (2016), *Concrete Problems in AI Safety*. https://arxiv.org/abs/1606.06565

**Previos y límites:** [RAV-01 — investigación comparativa inicial](COMPARATIVE_RESEARCH_AND_TEST_DESIGN.md); [RAV-01 — testigo ejecutable y controles](README.md); [core económico §8](../../ECONOMIC_MODEL_TECHNICAL_CORE_v0.1.md). Las fuentes citadas justifican marcos rivales/posibles mecanismos, **no** confirman aquí ninguna asociación L→F, γ humana, predicción sociológica, vivencia agéntica ni transferencia de evidencia DDS.

## 9. Revisión y puertas de salida

- **Contribución al PR #46**: documento de especificación de investigación, sin alterar RAV-01 ni sus 40 pruebas originales; sus extensiones siguen sin ejecutarse.
- **Relación con DDS**: programa modular informado por sus reglas de correspondencia, pero **no se autodenomina campaña DDS completada, evaluación de tecnologías ni prueba de conformance**.
- **Para implementar**: un investigador debe elegir una sola E-SV01, E-RE01 o E-AG01, declarar las fuentes, mapear K_iso/θ/Δ/κ y preregistrar hipótesis y contrapruebas antes de producir resultados. La selección de una extensión **no** amplía la autoridad de un agente o humano.
- **Puerta de propietario**: revisar la denominación «sufrimiento económico», reglas de factibilidad/consentimiento, traducción de utilidad en ámbitos íntimos, la separación de señal/autoridad y los límites de transferencia a agentes antes de adopción científica.
