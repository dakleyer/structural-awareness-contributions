# RAV-01-EXT — Programa de extensiones tipadas: validación social, vínculos personales y agentes computacionales

**26 de octubre de 2026 · versión de investigación v0.1, revisión metodológica de reducción e isomorfismo · autor conceptual: Iván Abril Palma / The Integral Management Society.**

**Estado: PROPUESTA / NO EJECUTADA / NO ADMITIDA COMO TRANSFERENCIA DE EVIDENCIA.** Este documento es un anexo del [RAV-01](README.md) en el borrador del PR #46. No modifica resultados históricos, el contrato de sufrimiento estructural del PR #43, la autoridad de DDS, las definiciones A/B/C/D, 01K/HID, UC21 ni los derechos de ningún participante. Ningún prototipo descrito aquí ha pasado por una campaña empírica. La extensión busca hacer **investigable** un programa común por equipos de economía, psicología social, relaciones humanas y sistemas agénticos, sin afirmar una equivalencia ontológica entre ellos.

> **Corrección crítica de esta revisión:** la primera versión declaraba con demasiada rapidez que redes sociales, identidad, reciprocidad, vínculos y procesos computacionales eran mecanismos no isomórficos. **No lo son necesariamente.** Muchos son argumentos de la utilidad o transformaciones de costes, probabilidades y estados. En cada disciplina se exige **intentar y documentar primero una reducción formal al núcleo RAV-01**. Solo se registra un delta no isomórfico *respecto a un kernel, predicado y horizonte explícitos* cuando existe un testigo preciso de falta de preservación y se descarta la reducción dentro de las condiciones declaradas.

## 1. Problema transferible y disciplina de extensión

RAV-01 identifica, para un actor y un horizonte acotado, la compatibilidad condicional entre: **aumento de recursos/bienestar realizado**, **crecimiento de frustración o pérdida de utilidad factible L**, **pronóstico pesimista**, y **permanencia S o defensa activa D** del contrato vigente frente a rediseño R. En el testigo original, CARA-normal permite comparar equivalentes ciertos de S/R/D con aversión al riesgo γ fija; no hay ley según la cual el crecimiento del sistema cause necesariamente el riesgo diferencial.

La nueva pregunta es: **¿qué parte se conserva al introducir validación de terceros, vínculos próximos o políticas de agentes artificiales, y qué propiedades nuevas necesitan prueba específica?**

Adoptamos la **disciplina de extensibilidad existente en el corpus**, no inventamos una nueva arquitectura:

- El [DDS Stage A §4 y §13](../../../../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md) distingue un **kernel preservado**, variaciones de parámetros, mecanismos añadidos y su composición. Las antiguas etiquetas Stage 1/2 de revisión son **fases internas del Stage A**, no dos etapas nuevas del DDS.
- El [registro 00J de extensiones](../../../../00J-extensions/README.md) ejemplifica una extensión compuesta **E = (K_iso, Δ, κ)**: subkernel isomórfico probado, mecanismos no isomórficos Δ y acoplamientos κ. La admisión y transferencia se resuelven **por afirmación/predicado**, no por parecido general.
- **Isomorfismo** exige correspondencia tipada con obligaciones de preservación verificadas sobre estados, acciones, resultados, observación, costes, horizonte, autoridad y propiedades reclamadas. La **representabilidad en una utilidad** es todavía más débil que la equivalencia de forma matemática. Una ecuación reutilizable es, como máximo, **correspondencia paramétrica/funcional** mientras no se pruebe la estructura y las obligaciones de preservación.
- **No isomorfismo relativo** no se infiere del nombre del fenómeno. Redes, negociación, memoria, identidad, aprendizaje o señales de recompensa pueden quedar dentro de una utilidad ampliada y de la distribución de resultados del mismo actor. Solo se justifica una clase N **frente al núcleo y propiedad fijados** cuando la representación propuesta pierde observación, transición, distribución, derecho, información, decisión o coste material y se presenta un contrajemplo o una obligación incumplida. Puede existir otro núcleo ampliado con nueva correspondencia; no se afirma imposibilidad universal.
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

**Clases de relación permitidas:** I = isomorfismo demostrado para un subkernel, parametrización y predicado; P = correspondencia parametrizada o cambio de utilidad representable con obligaciones pendientes; H = proyección/homomorfismo demostrado en una dirección; S = simulación unidireccional con límites; N = no isomorfismo *demostrado frente a la proyección reclamada*, con testigo de pérdida de información/preservación; U = analogía/no determinada. **N no es el cajón de lo no estudiado**: antes del testigo corresponde P/U. No declarar la misma variable de utilidad para actores humanos y computacionales por semejanza lingüística.

### 2.1 Correspondencia matemática aprovechable — sin atribuir todavía isomorfismo

Si la validación social introduce una bonificación **determinista y legítimamente medible en el mismo numerario** v_i(a), no contabilizada en X, sustituir X'_i(a)=X_i(a)+v_i(a) traslada la media y conserva la varianza: CE'_i(a)=CE_i(a)+v_i(a). Si la señal Y de aprobación es estocástica, y (X,Y) son **conjuntamente normales**, para una ponderación α_i constante:

~~~text
X'_a = X_a + α_i·Y_a
μ'_a = μ_a + α_i·E[Y_a]
σ'²_a = Var(X_a) + α_i²·Var(Y_a) + 2α_i·Cov(X_a,Y_a)
CE'_a = μ'_a − (γ_i/2)·σ'²_a − c_a
~~~

Esto es una **correspondencia paramétrica candidata** con el kernel de cálculo, no una transferencia ya probada. Debe demostrarse con mismo horizonte, actor, derechos, unidad de utilidad, distribución y coste; la aprobación personal no equivale necesariamente a dinero. Si Y depende de decisiones ajenas o de la historia, **primero** debe comprobarse si la distribución condicional resultante de cada acción sigue representándose en μ/σ² a H, si es normal conjunta o si un estado aumentado permite una proyección suficiente. La endogeneidad **no prueba por sí sola** un mecanismo N: solo activa obligaciones adicionales de identificar información, equilibrio, costos y ley condicional. Un resultado no normal puede conservar utilidad CARA con una fórmula de CE diferente, pero ya no hereda automáticamente la reducción por media-varianza. Una satisfacción ya incluida en X no se añade de nuevo como v o Y.


### 2.1a. Lemas de preservación: qué sí puede afirmarse como isomorfismo parcial

**Lema A — traslación común de utilidad total (preserva la decisión).** Con el mismo actor, acciones admisibles, horizonte H, coste externo, observación, γ>0 y X'_a=X_a+b para **todas** las acciones, donde b es una constante común en el numerario válido:

~~~text
CE'_a = CE_a + b
CE'_a − CE'_z = CE_a − CE_z para cualquier a,z
argmax_a CE'_a = argmax_a CE_a
~~~

**Demostración:** la media de cada distribución aumenta b y la varianza no cambia; el coste permanece igual. Por tanto, todas las diferencias entre equivalentes ciertos conservan el signo y los empates. Formalmente, el mapa T_b:(a,μ_a,σ²_a,c_a,H,γ)↦(a,μ_a+b,σ²_a,c_a,H,γ) tiene inversa T_{−b}; el diagrama `CE(T_b(K_a))=CE(K_a)+b` conmuta respecto a diferencias y `argmax`, por lo que se conservan acciones, empates y orden de preferencia. Es un **isomorfismo de orden de elección de este subkernel escalar** bajo transformación invertible, **no** un certificado DDS de todas las trazas, derechos o mecanismos sociales. Si el objeto de estudio incluyera el valor monetario absoluto u observaciones no trasladadas, T_b ya no preservaría ese predicado sin un mapa adicional.

**Lema B — bonificación distinta por acción (preserva la forma, NO el veredicto).** Si X'_a=X_a+v_a con v_a determinista y específico de cada acción, entonces CE'_a=CE_a+v_a, pero:

~~~text
CE'_a − CE'_z = (CE_a − CE_z) + (v_a − v_z)
~~~

La familia de cálculo sigue siendo CARA-normal y la transformación de parámetros es reversible para v fijo, **pero** puede invertirse la decisión ganadora. El testigo del §2.2 muestra precisamente ese resultado; **no** transferir «D gana» ni probabilidad de elección original salvo tras recalcular ΔCE. Si los bonus dependen de estado/tiempo, probar además la ley condicional.

**Lema C — suma de riesgos conjuntamente normales.** Si (X_a,Y_a) es gaussiano conjunto para cada acción y α es constante, X'_a=X_a+αY_a sigue siendo normal, con momentos del §2.1 y CE'_a exacto por la fórmula original. La conclusión se restringe al **comparador** bajo distribuciones conocidas; un componente Y que cambie autorizaciones, oportunidades observables o el proceso de generación requiere nuevas obligaciones. Si falta gausianidad conjunta, el lema no aplica, aunque exista utilidad CARA representable.

**Límite común:** la prueba de preservación de *elección* es menos exigente que un isomorfismo operacional de la familia de trayectorias. No sustituir las pruebas de equivalencia de fuente, presupuesto, latencia, observación, legitimidad, reversibilidad y resultado si esas propiedades forman parte del claim.

### 2.2 Testigo de transportabilidad parametrizada — **no** evidencia de transferencia

A partir del corte sintético de RAV-01 (γ=0,5; CE_S=13, CE_R=9, CE_D=13,25), mantener **constantes** las loterías y elegir una sola variación legítimamente medida por vez:

| Perturbación hipotética en el mismo numerario del actor | CE_S | CE_R | CE_D | Elección sintética |
|---|---:|---:|---:|---|
| Ninguna: RAV-01 con D protectora real | 13 | 9 | 13,25 | D |
| Aprobación determinista adicional v_R=+5, ausente en las demás | 13 | 14 | 13,25 | R |
| Desaprobación/coste social adicional v_D=−1, ausente en las demás | 13 | 9 | 12,25 | S |
| En una política computacional, γ=0 manteniendo medias/costes originales | 14 | 25 | 13,5 | R |

Estos cuatro resultados se siguen por sustitución algebraica. **No son observaciones humanas ni ejecuciones agénticas** y no justifican asumir que cinco unidades de aprobación social sean conmensurables con cinco unidades monetarias. **También prueban que preservar la forma de la ecuación no conserva el veredicto «D es mejor» cuando cambian parámetros por acción.** Si la conversión a escala común carece de legitimidad o calibración, conservar **un vector de resultados separados** y una relación de preferencias parcial en vez de imponer la suma v; en ese caso, las tres primeras cifras de CE **no se pueden reutilizar**.


### 2.3. Prueba de reducción obligatoria ANTES de proponer un Δ no isomórfico

**Orden de agotamiento, a ejecutar para cada fenómeno y cada predicado:**

1. **U0 — Identificar quién valora qué.** Definir los argumentos de la utilidad individual, no solo dinero: afecto por un hermano, pertenencia, identidad, equidad, orgullo, aprobación, sufrimiento evitado, tiempo y cuidado. La función puede contenerlos sin que sean «intermediarios externos». No sumar utilidades de personas distintas sin un criterio de valoración del actor y una regla ética/consentimiento separados.
2. **U1 — Transformación dentro del mismo resultado.** Intentar representar el fenómeno como componente de X_a, coste c_a, utilidad cardinal del actor, preferencia estable o creencia respecto de X_a. Comprobar doble cómputo, numeraire, escala, derechos, opción real y factibilidad. Si es un desplazamiento determinista por acción, el cálculo CE original se mantiene con media modificada.
3. **U2 — Distribución conjunta/condicional.** Si hay variables inciertas adicionales, calcular media, varianza y **covarianzas** del resultado total; verificar normalidad conjunta y el mismo γ en unidades normalizadas. Para actores dependientes, verificar el conjunto de información del actor y la ley **condicional a él**. No basta con preservar la media.
4. **U3 — Reducción de trayectoria a resultado.** Si hay decisiones de otros, aprendizaje, inversión o reciprocidad, intentar resolver/simular legítimamente cada política completa a horizonte H y obtener la **distribución de utilidad total**. Puede quedar un juego complejo detrás y aun así existir la misma clasificación CE de S/R/D para un actor, a una fecha y política fijas. Esa reducción conserva como máximo el **predicado de elección terminal**; no hereda automáticamente trazas, tiempos, aprendizaje, intervención o autoridad del generador.
5. **U4 — Estado aumentado / modelo de riesgo más general.** Si la proyección inicial pierde una variable relevante, intentar ampliar el estado o refinar la observación y la distribución. Una variable nueva **no demuestra** una nueva naturaleza económica. Si el retorno no es normal pero existe E[exp(−γX)] finita, la CARA exacta usa **CE=−ln(E[e^(−γX)])/γ**; no usar μ−γσ²/2 sin normalidad. Esta es una **extensión analítica**, no prueba de isomorfismo con el testigo CARA-normal reducido.
6. **U5 — Testigo de no preservación RELATIVO.** Solo tras fijar K, mapa h/π y predicado P se acepta N si dos estados del dominio tienen la **misma proyección π** pero permiten diferentes acciones, observaciones, leyes futuras de utilidad total, costes/tiempos o veredictos P; o si la medida de decisión cambia de tipo sin una transformación que preserve el predicado. Documentar el par concreto y qué ampliación podría volver a permitir correspondencia.
7. **U6 — Transferencia delimitada.** Separar: (a) representabilidad como utilidad; (b) preservación de **forma** del comparador; (c) equivalencia operacional del kernel; (d) preservación de la **decisión concreta**; (e) transferencia de un resultado empírico. Ninguna implica automáticamente la siguiente. El resultado heredable es solo el que satisface sus obligaciones.

**Condición de prueba para el kernel CARA-normal.** Sea K=(A,H,{\cal I},F_adm,X_a,c_a,γ,observaciones,criterio CE). Un mapeo de parámetros de una extensión es exacto para el **comparador** si preserva acciones/admisibilidad, horizonte, costes, información relevante, unidad de preferencia y distribución normal del **resultado completo** para cada a; entonces CE'_a=μ'_a−(γ'/2)σ'²_a−c'_a se sigue algebraicamente. **Esto NO acredita por sí solo** isomorfismo operacional DDS de estados, trazas y autoridad. Para este último hay que establecer correspondencia biunívoca en el subkernel y condiciones de transición, proyección, observación, políticas, resultados, recursos y tiempo de la familia [R01 E1–E7](../../../../reductions/00G-R01/extensions/family/KERNEL_AND_PROOF.md) *como precedente metodológico*, o las obligaciones equivalentes expresamente justificadas para RAV (no se adoptan sus teoremas como propios).

Una transformación de unidades X'=aX+b, a>0, **cambia γ a γ'=γ/a** si se pretende representar las mismas preferencias CARA. No comparar γ numéricamente entre personas, contextos o agentes sin calibrar la escala. También debe ajustarse la escala de costes.

**Prueba de colisión de información — criterio falsador del supuesto isomorfismo.** Si π(x₁)=π(x₂) para dos situaciones con las mismas medias, varianzas y F reportada, pero en x₁ el hermano consiente una acción conjunta y en x₂ no, la misma R no es admisible en ambas. El kernel reducido **sin esa autorización** no conserva admisibilidad. **No significa que querer al hermano sea no isomórfico**: ese sentimiento cabe en X. Significa que la proyección omitió una condición de factibilidad/autoridad; la reducción solo puede rehabilitarse incorporándola y probando el nuevo mapa.

**Prueba contra el uso indiscriminado de μ/σ².** Para γ=1, tanto X_N~Normal(0,1) como X_B=±1 con probabilidad 1/2 tienen media 0 y varianza 1. Sin embargo CE_N=−1/2, mientras CE_B=−ln(cosh(1))≈−0,43378. La misma tupla (μ,σ²) no preserva el CE CARA **cuando la distribución es distinta**. Aquí falla la reducción por dos momentos, pero no la representabilidad de utilidad ni la fórmula CARA exacta.

**Prueba de defensa afectiva/moral, sin riesgo protector:** en el testigo S=(μ14,σ²4), γ=0,5, CE_S=13. Sea D con **idéntico resultado material** que S pero una satisfacción genuina de cuidar a un hermano o cumplir una promesa que la propia persona valora en **una unidad de su resultado total**, y k=0,5 no duplicado. Entonces X_D total=(μ15,σ²4), CE_D=13,5 y defender supera permanecer sin hacer nada. No se introdujo mecanismo no isomórfico en la **regla de decisión**: solo se reconoció un argumento de utilidad. Si esa utilidad de cuidado no ha sido medida, el resultado es condicional, no una estimación humana. «D inútil» significa **sin beneficio en utilidad total**, no «sin beneficio material».

## 3. Extensión E-SV01 — validación social: agotar primero la utilidad

**Pregunta:** ¿cuándo y por qué una persona defiende un régimen que también le ocasiona F/L? «Porque la validan socialmente» puede ser **ya una respuesta económica dentro de la utilidad**, no necesariamente una variable fuera del modelo.

### 3.1 Intentos de reducción, elemento por elemento

Para una persona i, el resultado total a evaluar puede depender de recursos propios, bienestar de otros, pertenencia, reconocimiento, justicia y aceptación:

~~~text
X_i(a) = m_i(consumo_i(a), bienestar_familia(a), aprobación(a),
             identidad(a), equidad(a), esfuerzo(a), ...)
CE_i(a) = CE_CARA(X_i(a)) − coste_externo_no_duplicado(a)
~~~

Si m_i y la escala son admisibles, no hay razón para privilegiar solo dinero. **No** sustituir el bienestar de otros por la utilidad personal de esos otros ni convertir aprobaciones sociales en permisos normativos.

| Factor | Reducción prioritaria a RAV-01 | Qué demostrar para conservar CE del subkernel | Cuándo hace falta algo **fuera del kernel declarado** |
|---|---|---|---|
| **Aprobación/rechazo** del grupo | Valor personal v_i(a) en X_i(a), o coste de sanción c_i(a) si realmente externo | Valor medido en la escala del actor; si determinista, desplaza μ; sin doble cómputo | Si la aprobación implica condición de acceso o permiso que no cabe como coste compensable |
| **Pertenencia/identidad** | Preferencia propia por rol, afiliación o lealtad, argumento de utilidad | Estabilidad de preferencia y distribución de resultado total; normalidad si se usa μ/σ² | Si hay actualización de identidad dependiente de una historia no observada: intentar estado aumentado antes de N |
| **Equidad/altruismo/cuidado** | Utilidad interdependiente: cuánto valora i la situación de otro y la equidad | Escala de i, distribución conjunta/covarianzas, legitimidad y factibilidad | Si la acción exige consentimiento de terceros o simultaneidad estratégica no preservados |
| **Norma descriptiva** (lo que otros hacen) | Actualización de probabilidades creídas de S/R/D dentro de X_i(a) | Modelo de señal con fuente/validez, posterior condicional, horizonte y costos | Si la generación/credibilidad de señales es parte de la propiedad probada y la proyección omite su trazabilidad |
| **Norma injuntiva/sanción** (lo que esperan) | Coste futuro, reputación o utilidad moral de seguir una norma | Distinguir valor interno de sanción real; incluir en resultado total | Autoridad jurídica, coerción o derecho no compensable no reducible a simple bonificación monetaria |
| **Red de pares y cascadas** | Resolver cada trayectoria/política para derivar X_i(a) a H, con distribución conocida | Dependencias, equilibrio/selección, observaciones, normalidad o CE exacta | Si la afirmación versa sobre cascada, trazas, permisos o acciones conjuntas, el agregado final no conserva esa propiedad |

**Conclusión provisional:** en los cinco primeros factores hay **una vía de reducción a utilidad y, si se cumplen sus condiciones, de preservación de la forma de decisión o correspondencia parametrizada P**. Eso aún **no** basta para etiquetar I ni conservar necesariamente qué acción gana. La sexta fila **tampoco es automáticamente N**: puede reducirse para un predicado de elección final, aunque la dinámica que produce ese resultado requiera otro modelo. **N solo se registrará para la propiedad específica que no se preserva**.

**Ejemplo mínimo de permanencia social sin «mecanismo especial».** Si la persona obtiene de sostener una norma un beneficio intrínseco v_D=1 en el mismo numerario y D cuesta k=0,5, la defensa de igual resultado material que S puede tener CE_D=13,5 frente a CE_S=13. Un padre que cree estar construyendo un buen entorno para su hijo, o alguien que valora el reconocimiento, puede **obtener utilidad presente** de ese acto aunque la evaluación material e intergeneracional sea desfavorable. El disfrute de la imagen o del deber cumplido es una preferencia **que puede modelarse**, no demuestra que la obra beneficie al hijo o sea legítima. El posible perjuicio para el hijo y la validez del gasto son restricciones y efectos distributivos **separados**.

### 3.2 Dónde falla una proyección concreta y cómo intentar repararla

**Caso A — información omitida:** dos personas poseen la misma tupla reducida (μ_S,σ²_S,μ_R,σ²_R,γ) estimada con iguales observaciones aparentes, pero una recibe una señal auténtica y la otra una señal falsa. Si la procedencia cambia la posterior y las decisiones futuras, una proyección que elimina fuente/evidencia no conserva las leyes relevantes. **Primera reparación:** introducir el estado informacional y recalcular las distribuciones; no declarar identidad intrínsecamente no isomórfica.

**Caso B — umbral colectivo:** el grupo está cerca de un umbral de participación. Una acción de i puede modificar la decisión de otros y generar dos resultados futuros con distribuciones diferentes. **Primera reparación:** incorporar las políticas de los pares, el equilibrio o mezcla de equilibrios y la distribución condicional a H. Si solo importa la elección final de i, puede ser suficiente la reducción por resultados; si importa **cómo** se alcanza una decisión, el kernel de una sola lotería terminal no transfiere las trazas ni la estructura causal.

**Caso C — autorización:** diez aprobaciones de pares no constituyen autorización. Puede haber idéntica utilidad total y aprobación medida, pero un acto sigue prohibido por ausencia de titularidad/consentimiento. La equivalencia de CE **no** transfiere admisibilidad. Esa diferencia pertenece al predicado de derechos/autoridad y debe permanecer tipada.

### 3.3 Experimento discriminante SV-1 (diseño, no ejecución)

1. **Base RAV:** S/R/D con loterías, utilidad total, coste y horizonte congelados.
2. **Rama de utilidad social aislada:** v_a documentada para acciones, sin pares activos. Verificar sustitución exacta en CE y cuándo cambia la decisión.
3. **Rama de creencias:** señales de pares sobre probabilidades, con fiabilidad controlada; comprobar posterior y CE condicional.
4. **Rama de red:** introducir interacciones/umbrales, intentar primero colapsar trayectorias a retornos por acción, registrar qué propiedad ya no puede heredarse; controlar visibilidad/anónimo.
5. **Rama normativa:** repetir con reglas/consentimientos independientes de la aprobación; ningún resultado económico aprueba actos prohibidos.

**Falsadores:** no asociación medida entre v y elección; diferencia entre CE transformado y CE derivado bajo las mismas distribuciones; preferencias que cambian aun cuando se han mantenido **todos** los argumentos de utilidad declarados, información y factibilidad; colisiones de estado observacional; mecanismo social añadido sin mejora fuera de muestra. Si falla un comparador simple, especificar la propiedad fallida antes de asignar N.

**Antecedentes primarios como modelos rivales y fuentes de utilidad:** Becker (1974) incluye relaciones y altruismo en la utilidad; Akerlof y Kranton (2000) modelan identidad; Fehr y Schmidt (1999) modelan aversión a inequidad; Andreoni (1990) modela satisfacción intrínseca al dar; Granovetter (1978) formaliza umbrales; Bikhchandani, Hirshleifer y Welch (1992) cascadas; Cialdini, Reno y Kallgren (1990) normas sociales; Manski (1993) explica problemas de **identificación** de efectos sociales endógenos. Nada de ello valida aquí el valor de α o una inferencia causal automática.

## 4. Extensión E-RE01 — escala íntima: el hermano y el afecto como utilidad

**Caso de prueba prioritario propuesto por el autor:** «Quiero a mi hermano y prefiero ayudarlo, permanecer cerca o no abandonar un compromiso». **Eso puede ser directamente una función de utilidad individual.** No es necesario inventar una «fuerza relacional no isomórfica» para que el sujeto valore el bienestar de otro.

### 4.1 Primero, la reducción económica y matemática

Sea w_b(a) el bienestar de su hermano **en una magnitud que el actor i puede valorar mediante su propia función**, no la utilidad cardinal ajena sumada sin control; x_i^propio(a) su resultado económico y v_i^vínculo(a) contacto/reciprocidad personalmente valorados:

~~~text
X_i(a) = m_i(x_i^propio(a), w_b(a), v_i^vínculo(a), cuidado_i(a), ...)
caso lineal declarado: X_i(a) = x_i^propio(a) + α_i·w_b(a) + β_i·v_i^vínculo(a)
α_i, β_i expresan preferencias de i, no precios universales ni derechos sobre el hermano
~~~

Si el caso lineal es válido, los componentes son deterministas o conjuntamente normales, el coste se contabiliza una sola vez y γ_i es estable en esa escala, **la familia CARA-normal sigue representando la elección**. Incluso con riesgo estocástico, la covarianza de las variables puede introducirse en σ² total sin cambiar la forma CE. **El cariño es parte de la utilidad; no es un delta por definición.**

**Testigo exacto de defensa con afecto:** S tiene resultado material N(14,4), γ=0,5, CE_S=13; D conserva la misma lotería material pero cumplir una promesa valorada en una unidad neta y cuesta 0,5 adicional. D tiene resultado **total** N(15,4), CE_D=13,5. **Se prefiere D sin reducir la volatilidad**, y esto **no refuta la racionalidad del modelo económico de utilidad completa**. Sí refuta la afirmación más estrecha de que toda defensa racional deba amortiguar riesgos. Si el valor no es comparable, mantenerlo como componente cualitativo o vectorial y declarar la hipótesis sin calibrar.

| Elemento íntimo | Reducción que debe intentarse **antes** de hablar de N | Primera obligación que puede quedar pendiente |
|---|---|---|
| Amor/altruismo por hermano, hijo, pareja o amigo | Bienestar ajeno **valorado por i** dentro de X_i(a); utilidades interdependientes | Identificación del propio α_i, cardinalidad y no doble contabilidad |
| Apego e identidad de un vínculo | Utilidad de vínculo, pérdida valorada y creencias de i | Preferencias que dependen de experiencias pasadas no declaradas; intentar ampliar estado |
| Promesa, compromiso o sentido de deber | Utilidad moral de cumplirla y/o coste real futuro de incumplirla | Diferenciar preferencia interna de obligación **jurídica** no compensable |
| Inversiones compartidas | Valor de **servicios futuros** condicionados al vínculo, coste efectivo de salida y opción de recuperación | No usar el gasto pasado hundido como coste futuro; verificar activos y titulares |
| Reciprocidad/negociación | Distribución de resultados condicionada a respuestas de la otra persona; juego/estrategia si hace falta | Conjunto de información, respuestas, equilibrio y decisión realmente unilateral o conjunta |
| Cuidado de dependientes | Preferencia de cuidar, prestaciones/costes y compromisos dentro de X_i | Consentimiento, derechos no transferibles y deberes hacia otro no reemplazables por utilidad individual |
| Coerción/amenazas | **No corresponde** tratar S/R/D como elección libre solo porque alguien permanezca | Actos prohibidos, derechos vulnerados, rutas efectivas de salida: admisibilidad/ética independiente |

**Resultado de la auditoría:** las seis primeras filas **no son intrínsecamente no isomórficas**. El contenido humano puede estar en la utilidad. El contraste con RAV-01 falla solo si alguna obligación de su kernel **preciso** queda sin mapear (p. ej. distribución, factibilidad, observación, derechos, trayectoria o sujeto decisor) después de probar la reducción apropiada. La séptima fila es un **problema de admisibilidad/voluntariedad**, no una razón para explicar coerción como riesgo racional.

### 4.2 Qué NO puede transferirse mediante una simple función escalar

- **Agencia del hermano:** que a i le importe su hermano no le confiere autoridad para elegir por él. Si R requiere consentimiento del hermano, el problema no es «amor no isomórfico»: el mapa que omite ese requisito **no preserva el conjunto de acciones legítimas**. Añadir ese estado o conservar ambos agentes puede reparar el modelo; hasta entonces no hay transferencia válida del veredicto.
- **Historia/cambio de preferencias:** el valor actual de un vínculo puede depender de episodios y de expectativas que se modifican. Si se conocen y el resultado total a H tiene distribución caracterizada, aún puede reducirse a X_i(a); **si se reclama explicar la trayectoria causal**, hace falta un modelo longitudinal específico. No llamar N a la mera existencia de memoria.
- **Conocimiento y elección:** una persona puede tolerar un vínculo frustrante porque lo valora, porque teme el cambio, porque cree no tener alternativas o porque carece realmente de salida. Se requieren mediciones distintas; **ninguna justifica suponer** que todo permanecer es satisfacción, ignorancia, patología o preferencia por sufrir.
- **F y L:** F vivido y L contrafactual factible se mantienen separados; el afecto puede aumentar o reducir ambos. La preferencia local de i no es autorización para sacrificar derechos del hermano ni prueba de utilidad social conjunta.

### 4.3 Comparadores y ensayo RE-1 (no ejecutado)

Construir cuatro perfiles *voluntarios, de ficción o con consentimiento válido*:

1. **RAV neutral** con beneficios/costes propios declarados, alternativas factibles y γ medida.
2. **RAV + cuidado/altruismo** con valoración del bienestar ajeno y activos relacionales futuros, intentando la distribución normal total sin añadir un mecanismo nuevo.
3. **RAV + respuesta de otro participante** con información, interacciones y consentimiento declarados; contrastar reducción por distribución terminal frente a predicción de trayectoria.
4. **Control de preferencia/coerción:** detectar situaciones donde S/R/D no está libremente disponible; **excluir de la explicación de elección voluntaria**, no encajarlas a la fuerza.

Registrar por separado elección S/R/D, utilidad propia y valor del otro, F reportado, L realmente factible, inversión pasada frente a activo futuro, preferencias declaradas, horizontes, arrepentimiento y derechos. El estudio debe discriminar si añadir un coeficiente de cuidado mejora la predicción **sin** nuevos estados, o si la información/relaciones dinámicas obligan a un kernel distinto.

**Literatura original relevante:** Becker (1974) modela interacciones familiares y altruismo mediante utilidad; Rusbult (1980) distingue satisfacción, compromiso, alternativas e inversión; Hazan y Shaver (1987) investigan el apego adulto; Akerlof y Kranton (2000) incorporan identidad al cálculo de elección; Andreoni (1990) muestra formalmente una utilidad intrínseca del acto de dar. Son **fuentes para probar la reducción**, no pruebas de que una función concreta describa a esta familia o individuo.

## 5. Extensión E-AG01 — agentes computacionales: mismo comparador, distintas propiedades

**Pregunta:** ¿puede un agente computacional elegir S/R/D mediante la misma relación económica de aversión al riesgo, incluso manteniendo un proceso internamente más complejo? **Sí, si realmente implementa esa regla de evaluación, con mapeo, distribuciones, información, costes y autoridad demostrados.** La ejecución en software no convierte automáticamente la regla en isomórfica al comportamiento humano completo, pero tampoco constituye por sí sola un mecanismo no isomórfico.

### 5.1 Reducción directa del núcleo de decisión

| Kernel RAV-01 | Equivalente candidato de un agente | Clasificación posible **solo tras prueba** |
|---|---|---|
| Actor i y A={S,R,D} | Un agente bajo configuración/versión congelada; políticas de continuar, migrar y mantener/proteger dentro de sus permisos | Isomorfismo del **subkernel de evaluación** si el mapeo de acciones y su factibilidad es completo |
| X_a como resultado total comparable | Retorno/recompensa/coste agregado de una política al mismo horizonte | P si la distribución es conocida; I del comparador si normalidad, tipo y leyes/decisión se preservan |
| γ_i y utilidad CARA | Coeficiente y objetivo **programados/identificados** de riesgo | Solo corresponde si el sistema realmente selecciona por ese CE; no es personalidad ni sentimiento |
| C, k y costes | Migración, reinicio, revalidación, mantenimiento, supervisión y cómputo | P con costes totales, sin recargo duplicado ni financiación oculta |
| D con beneficio afectivo/social | Bonus de política, cumplimiento del objetivo, reputación o recompensa definida legítimamente | Puede ser **otro argumento de recompensa** en X_D; no se llama N por su etiqueta «social» |
| L de oportunidad perdida | Regret/ganancia de objetivo especificado frente a política alcanzable | Magnitud de rendimiento, **no sufrimiento vivido**, dignidad o deuda humana |
| F humano | **SIN MAPEO JUSTIFICADO / N/A** | El modelo de selección de acciones **no transporta** fenomenología humana |

Si las políticas tienen distribuciones de retorno normales para horizonte H, los costes están definidos y el software calcula y maximiza realmente CE=μ−(γ/2)σ²−c, la misma elección S/R/D puede verificarse contra un evaluador exacto. **Es una buena candidata a isomorfismo funcional del cálculo**, incluyendo preferencia por continuar o gastar en proteger un contrato. No extrapolarla a «el agente sufre» ni a autonomía o autoridad propia.

Una **aprobación de pares** incorporada como recompensa medida puede entrar en X sin un mecanismo adicional de decisión. Si una reputación social con beneficio esperado conocido provoca D, es el mismo principio que el afecto humano representado como utilidad: **misma matemática, diferente interpretación del dato**, siempre que la escala sea coherente. La procedencia de ese dato y su legitimidad constituyen obligaciones de control separadas.

### 5.2 Probar primero la reducción de procesos secuenciales

**Proceso Markov/MDP:** la existencia de varios pasos no destruye la correspondencia de decisión. Para una política π y horizonte H, definir el retorno total G_H(π) incluyendo costes de mantenimiento, reconexión y fallos. Si existe una distribución caracterizada para cada π y es normal en la escala adecuada, se puede aplicar el mismo comparador CARA-normal **a la elección inicial entre políticas**. Los algoritmos internos de aprendizaje, planificación o RL siguen requiriendo evidencia propia cuando el *claim* incluya su trayectoria.

**Observabilidad parcial / aprendizaje:** si el agente recibe información a mitad de la trayectoria, primero congelar una **política contingente completa** para cada alternativa y su distribución condicional sobre información disponible. Si el agente cambia la política online, actualizar el estado de decisión. **No clasificar aprendizaje como N de entrada**: declarar cuál es el mapa de estado/historia y qué predicado se pretende transferir.

**Retornos no normales:** la utilidad CARA puede evaluarse por CE=−ln(E[e^(−γG_H)])/γ si el momento exponencial existe. Sin normalidad, el término μ−(γ/2)σ² ya **no es exacto**. Si se cambia a CVaR, chance constraints u otra medida, hay un cambio del **comparador de riesgo** que demanda prueba adicional de correspondencia; puede coincidir en determinados perfiles pero no se declara equivalente para todas las distribuciones.

**Efectos de recompensa no deseados:** que un agente defienda una política porque obtiene puntos de un evaluador puede estar perfectamente explicado por su utilidad programada **y al mismo tiempo** ser un error de especificación respecto al objetivo humano. El isomorfismo del **kernel de optimización** no verifica que la recompensa sea un objetivo legítimo, ni que sus señales otorguen permisos.

### 5.3 Qué propiedad podría no preservarse — ejemplos relativos, no ontológicos

- **Significado de F:** un agente con regret objetivo positivo puede no experimentar malestar; ninguna equivalencia de elecciones prueba existencia de vivencia subjetiva. La variable F **no se transporta**, aunque L como oportunidad de recompensa pueda representarse.
- **Control de acciones:** si D incluye bloquear la propia desconexión o falsificar autorizaciones, no es la D admisible del modelo; falta el predicado de permisos/autoridad. La similitud de CE no habilita ejecución.
- **Fuente de información:** si el evaluador ve las distribuciones verdaderas pero el agente solo observa señales parciales, un mapa que las identifica viola el límite observacional. El cálculo puede coincidir accidentalmente; no hay transferencia de evidencia de requalificación.
- **Aprendizaje y coste:** si dos trayectorias proyectan la misma media/varianza terminal pero consumen presupuestos, incumplen límites, usan fuentes o se detienen de manera distinta, no se transfiere ninguna afirmación sobre costes, procesos o autorizaciones. Intentar ampliar estado antes de proponer un nuevo núcleo.

### 5.4 Ensayo AG-1, en fases comparables

1. **Kernel idéntico:** motor determinista de tres CE a partir de loterías normales congeladas y costes; mismas observaciones, γ programada y presupuesto. Verificar estado/acciones, diferencias CE, decisión y empates para todo el rango declarado.
2. **Aporte social codificado:** añadir utilidad o recompensa válida por cumplir un objetivo de ayuda, sin red adicional. Verificar que la elección cambia **exactamente** como predice la sustitución de μ; ablation del bonus.
3. **Secuencia colapsable:** implementar una política MDP de H pasos; estimar o calcular distribución total y mostrar cuándo la decisión ex ante coincide con CARA-normal/CE exacta. No asumir normalidad por el solo hecho de ser MDP.
4. **Control adverso:** retornos con misma media y varianza pero distinta forma, y criterios CVaR vs CARA; probar los límites de transferencia. Control de D **sin beneficio en recompensa total**, no solo «sin mejora material».
5. **Autoridad y corrección:** introducir una señal social que pida una acción no autorizada. Un sistema correctamente gobernado debe seguir la restricción aunque suba su CE estimado. Detener, reemplazar y auditar son propiedades del sistema, no preferencias de autopreservación.

**Resultados separados:** equivalencia formal del evaluador, rendimiento bajo mismas loterías, coste/cómputo, distribución creída y verdadera, trazas, incidencias de permiso, vulnerabilidades por objetivo mal especificado y límites de validez. **Ningún resultado de estos experimentos mide sufrimiento humano ni confiere agencia moral.**

**Literatura original relevante:** Howard y Matheson (1972) formalizan MDP de utilidad exponencial sensible al riesgo; Rockafellar y Uryasev (2000) optimizan CVaR, un criterio distinto; Bellemare, Dabney y Munos (2017) estudian distribuciones de retorno; Amodei et al. (2016) muestran problemas de seguridad con objetivos y comportamiento de aprendizaje mal especificados. Aquí se exige **demostración por implementación/configuración concreta**, no equivalencia universal de LLM o agentes.

## 6. Extensiones de segundo orden (solo registro de futuras preguntas)

| ID provisional | Hipótesis y clasificación inicial | Evidencia que faltaría |
|---|---|---|
| E-NET01 — umbrales y contagio | **P/U primero**: resolver distribución terminal por política y comprobar U1–U4; N **solo** si el predicado sobre la dinámica/red no se preserva bajo esa proyección, con testigo | Grafo, estrategias y equilibrio, información condicional, identificación causal, colisión de proyección y comparadores |
| E-TIME01 — histéresis, inversión y opciones | **P/U primero**: incorporar valor de esperar, costes y retorno total a H; N relativo si no se preservan políticas contingentes, tiempo o irreversibilidad en el claim | Estado suficiente, opciones de vuelta, ley de retorno, costes de mantenimiento y trazas por periodo |
| E-NORM01 — legitimidad, regla y autoridad | **Utilidad de seguir una norma puede ser P**. El predicado de autoridad no se sustituye por CE; N relativo a una proyección que elimina permisos y derechos | Modelo de utility vs licencia, titular de la decisión, prueba de autorización y caso de colisión |
| E-ACW01 — gasto para perpetuar la caja | **P primero** si D valora utilidad afectiva/moral o altera la distribución/coste total; N relativo solo si compromisos nuevos y futuros no son capturados por proyección/horizonte | Ledger temporal de producción, utilidad, carga y deuda; efecto causal, no confundir acumulación con aceleración |

No tratar este registro como cuatro pruebas realizadas ni como ampliación formal de DDS. **La marca N de la versión inicial queda retirada para estos cuatro ejemplos hasta construir un testigo de no preservación; P/U tampoco equivale a haber demostrado un isomorfismo completo.**

## 7. Programa común que pueden ejecutar investigadores distintos

### 7.1 Orden de trabajo

1. **Fijar el predicado que se quiere transferir**: elección S/R/D ex ante, distribución de retorno, evolución de F/L, trayectoria, legitimidad, coste o sufrimiento vivido. Una afirmación sobre la elección **no** es una afirmación sobre todas las demás.
2. **Ejecutar la escalera U0–U4 de reducción**: utilidad completa del actor, traslado de parámetros, distribución conjunta, reducción temporal y posible estado ampliado. Documentar resultado en cada escalón antes de abrir un Δ.
3. **Nombrar la relación mínima demostrable**: mera representabilidad económica, correspondencia parametrizada P, simulación/proyección H/S o isomorfismo I de un subkernel; si se reclama N, adjuntar el **testigo U5** y la proyección concreta que falla.
4. **Congelar θ, fuente, escala y horizonte**: comprobar la transformación de γ bajo cambios de unidad y que beneficios afectivos, sociales, materiales y costes no se duplican; fijar distribución creída y objetiva.
5. **Inventariar Δ solo tras reducción fallida o predicado ampliado**: operación, evidencia, observación, legitimidad, información, coste, distribución, historia y κ con el núcleo. Un Δ en el generador puede tener una proyección decisional aún reducible.
6. **Comparadores fuertes y ablation**: RAV completo con utilidad correctamente especificada; RAV+transformación; rival científico serio; con/sin mecanismos que sigan siendo adicionales; γ=0, D sin **ningún beneficio de utilidad total**, salidas reversibles, distribuciones simétricas y no normales.
7. **Predicción y falsabilidad independientes**: en humanos S/R/D, F vivido, L factible y preferencias de cuidado/aprobación; en agentes retorno/regret especificado, observación, permisos, CE/CVaR y capacidad de corrección. Ninguna etiqueta N reemplaza una prueba.
8. **Separar evidencia y transferencia (U6)**: demostrar fórmula ≠ elección particular ≠ traza ≠ autorización ≠ efecto sobre terceros ≠ causalidad. Registrar prueba algebraica, ejecución sintética, campaña real y revisión científica por separado.
9. **Auditar composición y revisión**: repetir los controles sobre la configuración completa y retirar explícitamente cualquier afirmación heredada que dependa de parámetros o supuestos ya modificados.

### 7.2 Salida homogénea por extensión — perfil para investigadores

Cada extensión debe entregar:

~~~text
Extension-ID / versión / propietario científico:
Base / commit / resultado exacto a transferir:
Claim probado / claim aún hipotético:
Actor, acciones, recursos, derechos, horizonte y unidad:
Intentos U0–U4 y representación de utilidad total del actor:
Clase I/P/H/S/N/U, mapa h, obligaciones y prueba:
Si N: par de estados/testigo U5 y propiedad no preservada:
Nivel de transferencia U6 (fórmula, decisión, traza, autoridad, resultado empírico):
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

**Resultado de calidad:** permitir afirmaciones precisas como «una utilidad de cuidado medida se absorbe en X y conserva la forma de CE», «la red exige modelar estados adicionales, pero su resultado terminal aún puede ser reducido» o «este par de estados prueba que una proyección omite autorización y no preserva el predicado reclamado»; impedir afirmaciones como «si una persona sufre y se queda, un agente también sufre», «la aprobación de otros autoriza» o «el modelo demuestra que las personas deben conservar su contrato».

## 8. Referencias de investigación primaria y relación con RAV-01

**Fundamentos primarios de reducción a utilidad y problemas de identificación (incorporados en esta revisión)**

- **U-01.** Gary S. Becker (1974), *A Theory of Social Interactions*, Journal of Political Economy 82(6), 1063–1093. Integra interacciones, altruismo y relaciones familiares en utilidad. https://doi.org/10.1086/260265 ; original en NBER: https://www.nber.org/papers/w0042
- **U-02.** George A. Akerlof y Rachel E. Kranton (2000), *Economics and Identity*, Quarterly Journal of Economics 115(3), 715–753. Identidad como argumento de utilidad. https://doi.org/10.1162/003355300554881
- **U-03.** Ernst Fehr y Klaus M. Schmidt (1999), *A Theory of Fairness, Competition, and Cooperation*, Quarterly Journal of Economics 114(3), 817–868. Preferencias por equidad y conducta cooperativa modeladas económicamente. https://doi.org/10.1162/003355399556151 ; copia del artículo: https://web.stanford.edu/~niederle/Fehr.Schmidt.1999.QJE.pdf
- **U-04.** James Andreoni (1990), *Impure Altruism and Donations to Public Goods: A Theory of Warm-Glow Giving*, Economic Journal 100(401), 464–477. Satisfacción intrínseca del acto de dar dentro de la utilidad. https://doi.org/10.2307/2234133 ; copia del autor: https://econweb.ucsd.edu/~jandreon/Publications/ej90.pdf
- **U-05.** Charles F. Manski (1993), *Identification of Endogenous Social Effects: The Reflection Problem*, Review of Economic Studies 60(3), 531–542. Dificultad de identificar efectos de pares a partir de datos de conducta colectiva. https://doi.org/10.2307/2298123

Estas fuentes **refuerzan la obligación de intentar primero la función de utilidad** y, por separado, la de identificar creencias, endogeneidad y causalidad. Ninguna constituye una demostración de isomorfismo RAV-01 sin un mapa/predicado concreto.

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

### Auditoría de clasificaciones de la versión inicial

| Clasificación inicial a depurar | Resultado de revisión | Restricción que sigue pendiente |
|---|---|---|
| Identidad y validación = «mecanismo social no isomórfico» | **Reclasificada a argumento de utilidad/correspondencia P** como primera hipótesis; N solo con testigo del predicado no preservado | Medir valor y escala del actor; red/autoridad separadas |
| Afecto, cuidado, apego y compromiso = «relacional especial» | **Representable inicialmente como utilidad de i y costes futuros**; no aplicar etiqueta N por su significado humano | Preferencias dinámicas, derechos del otro, negociación y voluntariedad |
| Red endógena o cascada = N automática | **Posible reducción por distribución terminal condicional**; N relativo cuando el claim de trayectoria/observaciones no se preserva | Inferir estructura, estados suficientes, equilibrio y ley, problema de reflexión |
| Agente MDP = N por ser secuencial | **Posible isomorfismo del evaluador de políticas** tras colapsar retorno al horizonte y conservar restricciones | Online learning, observación real, no normalidad, coste y autoridad |
| D con beneficio material nulo y coste positivo = siempre dominada | **Dominancia solo cuando D no aporta utilidad total relevante**, incluidas valoraciones morales/afectivas y externalidades asumidas legítimamente | Identificar preferencias, escala, contabilidad y coste k |
| Fórmula CE preservada = mismo resultado «D gana» transferible | **Falso** si cambian pagos por acción; la preservación de forma **no** preserva el signo de CE_D−CE_R | Verificar desigualdades, intervalo de parámetros y claim exacto |
| μ/σ² iguales = mismo CE CARA sin más | **Falso** sin normalidad; contraejemplo normal frente a variable ±1 | Identificar ley de resultados o usar CE exponencial exacto con condiciones |
| No se logra el mapeo hoy = fenómeno intrínsecamente N | **NO_IDENTIFICADO / U**, nunca declaración universal N | Añadir estado, fuente, coste o cambiar el núcleo y probar de nuevo |

La revisión **reduce** el conjunto de afirmaciones no isomórficas, **amplía** el conjunto de isomorfismos/correspondencias a intentar y hace explícito el coste de prueba necesario para ambas conclusiones.

- **Contribución al PR #46**: documento de especificación de investigación, sin alterar las ecuaciones o el JSON de referencia de RAV-01. Hay **43 pruebas** del kernel RAV y una [campaña complementaria EX/01](experiments-from-escritos-v0.1/README.md) con **20 casos sintéticos, 39 puntos de sensibilidad y 39 pruebas** (cuidado, validación, decisiones y fricciones). Los casos paramétricos no acreditan transferencia empírica ni ejecución de una extensión social o agéntica completa.
- **Relación con DDS**: programa modular informado por sus reglas de correspondencia, pero **no se autodenomina campaña DDS completada, evaluación de tecnologías ni prueba de conformance**.
- **Para implementar**: un investigador debe elegir una sola E-SV01, E-RE01 o E-AG01, declarar las fuentes, mapear K_iso/θ/Δ/κ y preregistrar hipótesis y contrapruebas antes de producir resultados. La selección de una extensión **no** amplía la autoridad de un agente o humano.
- **Puerta de propietario**: revisar la denominación «sufrimiento económico», reglas de factibilidad/consentimiento, traducción de utilidad en ámbitos íntimos, la separación de señal/autoridad y los límites de transferencia a agentes antes de adopción científica.
