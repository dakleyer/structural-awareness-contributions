# ACC — Cierre local de preguntas a partir de indeterminación abierta; metacognición acotada y solidaridad elegida

**Estudio de investigación v0.1 · 26 octubre 2026 · autor conceptual: Iván Abril Palma / The Integral Management Society.** Estado: estudio sintético y matemático, no implementación de un oráculo, no capacidad clínica de medir sufrimiento y no definición sustitutiva de 00M/00N. El PR científico está apilado sobre los PR #42 → #43 → #44 y no cambia los resultados congelados de DDS, UC21 ni la propiedad de 01K sobre HID.

## 0. Pregunta y procedencia

**Fuente primaria de esta adenda:** el documento aportado por el autor «prompts no procesados.docx», recibido el 26-10-2026. Se conserva la secuencia íntegra de su argumento en [PROMPT_COVERAGE_MATRIX.md](PROMPT_COVERAGE_MATRIX.md), con separaciones entre los resultados anteriores y los dos bloques que todavía faltaban: (i) cierre local derivado de composiciones abiertas B/C/D, posiblemente mediante una «nube de puntos» incierta; y (ii) metacognición, deliberación bajo riesgos no cuantificables y solidaridad elegida. Las formulaciones anteriores del autor sobre plátanos, naranjas, hormigas, manzanas/frutería, crédito 7/10, el estudiante de un barrio pobre y el receptor de X−200 continúan identificadas en el [registro de ejemplos del PR #42](../bounded-traps-v0.1/EXAMPLE_LEDGER.md). No deben borrarse ni convertirse en hechos históricos verificados.

**Hipótesis a probar:** un sistema social/económico compuesto pierde distinciones relevantes a través de interfaces legítimamente restringidas; sus participantes pueden compartir cualificaciones parciales no fungibles de los fundamentos, exploraciones y barreras. Aunque el residual continúe abierto, esa composición podría justificar una respuesta **suficiente para una pregunta acotada**, o recomendar un esfuerzo de exploración limitado, a menor coste que reconstruir exhaustivamente el universo de los subsistemas. Puede ayudar a reducir la distancia de desarrollo/producción o, en algunos contextos, simplemente revelar una brecha previamente inadvertida. No hay ventaja garantizada frente a controles convencionales equivalentes.

## 1. Cuatro objetos distintos: no reducir lo abierto a una función total

1. **El sistema físico y social:** personas/agentes, recursos, derechos, contratos y subsistemas productivos. Sus restricciones y funciones realmente caracterizadas se estudian mediante ACC (LP/MILP, sistemas dinámicos, no convexidades, transiciones). La salida operativa de cada proceso es su A situado.
2. **Declaraciones calificadas y parciales:** B aporta fundamentos y reserva evaluable caracterizada; C da una dirección fundada de exploración sin evaluación caracterizada de población/coste/beneficio; D testimonia una influencia potencialmente material sin ruta efectiva de evaluación para este proceso. UNKNOWN permanece cuando no está siquiera fundada esa clasificación. Son posiciones relativas a productor, función, pregunta, alcance, capacidad y tiempo conforme a [00M §1](../../../../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md), no inventarios cerrados de objetos.
3. **La representación del receptor:** una proyección `π: W → M` (donde M contiene sólo la interfaz o síntesis disponible). Si estados distintos dan la misma síntesis y respuestas diferentes a una pregunta previamente especificada, no existe decisión exacta basada sólo en esa síntesis: una consecuencia conocida de la factorización de funciones y el argumento muchos-a-uno/preimagen.
4. **La metapolítica limitada:** un procedimiento que evalúa la suficiencia de evidencia para **una pregunta declarada** y recomienda seguir, rechazar esa transición, revisar o abstenerse sin resolver todas las propiedades del mundo. El resultado de la metapolítica es A de su propio proceso de revisión; no sustituye el A original ni convierte C/D en B por mera anotación.

La condición formal de [00M §4.1](../../../../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) sigue siendo: si π(w)=π(w′), una síntesis exacta para q exige r_q(w)=r_q(w′), dentro de la clase admisible declarada y con la pregunta fijada **independientemente** de π. Una sobreaproximación de respuestas compatibles puede ser útil (00M §4.2) sin ser exacta.

## 2. Proposición de cierre local sin cierre del exterior

**Proposición (decidibilidad de una pregunta bajo un intervalo acreditado).** Fijados una región de decisión R, una pregunta binaria q(x): «¿f(x)≥T?», observaciones legítimas sobre f y un intervalo *sound* [L(x),U(x)] que incluya todos los valores compatibles con **los supuestos de regularidad y fuente** en x∈R:

- Si L(x)≥T, q es verdadera en todos los estados **admitidos por esos supuestos**: cierre afirmativo de esa pregunta.
- Si U(x)<T, q es falsa en todos ellos: cierre negativo de esa pregunta.
- Si L(x)<T≤U(x), la pregunta sigue indeterminada bajo la evidencia y el intervalo.

**Demostración:** todos los valores posibles están contenidos en el intervalo, así que no pueden cruzar el umbral de forma contraria a los dos casos estrictos. El resultado es condicional a que el intervalo sea verdaderamente conservador y la clase represente el alcance de la consulta. No certifica la verdad de hechos sobre el mundo fuera de R ni clausura C/D. El mismo caso puede ser B para quien dispone del procedimiento de evaluación y el cierre calculado A de un evaluador receptor.

La proposición no requiere conocer todos los elementos desconocidos. Y es importante distinguir dos sentidos de «cierre»: **(a) una respuesta suficientemente determinada para q** y **(b) un inventario/exhaustividad del exterior**. El primero puede conseguirse sin el segundo. Un residuo D material para la misma pregunta y no contemplado en los supuestos desautoriza extrapolar el certificado local a esa decisión global; el runner lo marca `MATERIAL_D_NOT_EVALUABLE`.

## 3. Una nube de puntos indeterminada pero aprovechable

El autor describe observaciones incluso heterogéneas, de cantidad total desconocida y con confianza o margen imperfectamente caracterizados. No se modela esa nube como un conjunto completo de elementos de C o D. **Sólo existe un conjunto finito de testimonios disponibles hasta la fecha**, cada uno con fuente, alcance, revisión, tiempo y márgenes de localización y medida; el residual sigue explícitamente abierto.

Con un marco de regularidad **declarado y fundado** (no inferido arbitrariamente de la nube), por ejemplo una cota Lipschitz |f(x)-f(x′)|≤λ|x-x′| en una región R, y para cada punto i coordenada incierta x_i∈[a_i,b_i] y valor f(x_i)∈[l_i,u_i], definimos la distancia superior D_i(x)=max(|x-a_i|, |x-b_i|). Los testimonios verdaderos implican:

\[
  \max_i\{l_i-\lambda D_i(x)\}\;\le\; f(x)\;\le\;\min_i\{u_i+\lambda D_i(x)\}.
\]

La intersección por `max` y `min` es una envolvente CONSERVADORA, válida sólo si los testimonios, las coordenadas y la cota Lipschitz se cumplen, hay un estado compatible y el alcance incluye la pregunta. No es una interpolación probabilística ni un procedimiento universal de descubrimiento del exterior. La procedencia y dependencia entre fuentes permanecen; duplicar el mismo testimonio no aporta corroboración independiente. Si la envolvente resulta vacía, el resultado es **inconsistencia de evidencia o de supuestos**, no un promedio compensatorio.

**Contraejemplo fundamental:** con un número finito de puntos y **sin** regularidad, existen funciones que coinciden en todos los puntos observados y toman valores arbitrariamente distintos en cualquier otro punto. Por tanto, una nube por sí sola no establece un resultado de interpolación válido. Del mismo modo, la etiqueta de «90 % de confianza» no tiene lectura probabilística sin calibración, denominador y un mecanismo de muestreo. El código utiliza **intervalos deterministas**, no distribuciones ficticias ni una probabilidad de D.

Ejemplo ejecutable: dos fuentes sitúan f(0)∈[9,10] y f(2)∈[9,10], se caracteriza λ=1 en [0,2] y la consulta es q(1): f(1)≥7. El intervalo conservador [8,11] permite la respuesta local afirmativa, pese a que no se conoce f(1) exactamente y la familia de hechos fuera del alcance continúa abierta. Sin una cota λ legítima, el resultado es `NO_JUSTIFIED_REGULARITY`. Si una influencia D material no entra en ese marco, el resultado global es `MATERIAL_D_NOT_EVALUABLE`, incluso si la parte calculada parece favorable.

**Relación con entropías:** en un universo de ensayo finito con P explicitada se podría calcular H(R|A) y su reducción al recibir Q; no existe una entropía de Shannon de la nube completa si no hay distribución ni cardinalidad identificadas. El índice de cobertura de preimágenes, Kolmogorov, la dimensión fractal, von Neumann y entropía termodinámica no se convierten por este modelo en la misma magnitud ni en un coste real de sufrimiento.

## 4. Composición no fungible de testimonios: utilidad relacional sin sumabilidad de todo

La unidad de composición es una *afirmación cualificada*, no «una unidad de ignorancia». Cada testimonio conserva `claim_id`, `origin_id`, `scope`, `revision`, `observed_at`, y márgenes. Una copia exacta no cuenta dos veces. Identificadores repetidos con contenido incompatible producen `SOURCE_CONFLICT`; dos fuentes con restricciones incompatibles generan `EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT`. Un mismo origen que emite dos declaraciones no crea independencia por repetirlas. El campo `source_attested` en el toy es **un supuesto sintético de elegibilidad**, no una firma o autenticación criptográfica real.

Las correspondencias entre testimonios se limitan a preguntas y alcances compatibles. Un B bien caracterizado puede complementar una reserva de otro proceso; C, aunque funda una exploración, no añade automáticamente una relación causal probada ni un ROI; D reporta una barrera sin dar la probabilidad de su efecto. Las carencias de legitimidad, acceso o derechos no pueden compensarse sumando mucha precisión en otra dimensión (no fungibilidad).

Ciertos conjuntos de evidencias parciales pueden dejar de ser insuficientes para una consulta particular tras recibir otra declaración compatible. Esto no significa «C/D fueron clausurados». Puede significar que se cerró **un subproblema caracterizado** de modo relativo a la pregunta; el resto conserva sus fronteras abiertas. La cartografía social puede, además, proponer preguntas nuevas y rutas de revisión que sigan abiertas.

## 5. Metacognición calculable sin oráculo total

El autor propone una función superior capaz de decidir algo útil aun sin evaluar la función de base. La formulación correcta es un **certificador limitado de suficiencia o de estado del conocimiento**: su salida puede ser `LOCALLY_SUPPORTED_TRUE`, `LOCALLY_SUPPORTED_FALSE` o `UNDETERMINED_FROM_AVAILABLE_EVIDENCE`, además de `EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT`, `MATERIAL_D_NOT_EVALUABLE`, etc. Esta salida es A del metaproceso y B de un receptor cuando cualifica el resultado productivo de otra función.

**No equivale a decidir una propiedad Turing-indecidible de la función subyacente.** Si existiera un procedimiento total y computable que, para cualquier programa y entrada, retornase correctamente YES/NO al halting problem usando sólo metadatos computables, resolvería el problema de parada, contradicción. El metaproceso puede decidir *si hay una prueba suficiente dentro del perfil* y abstenerse de determinar la propiedad objeto. Abstención legítima ≠ fallo de un oráculo. Un certificador que dice «lo presentado no justifica esta transición» no afirma «la transición resultará físicamente mala».

El módulo `qualify` no recibe estado del mundo ni la función f verdadera. Recibe testimonios, una clase de regularidad expresamente cualificada y una pregunta. El módulo `advisory` devuelve una orientación acotada sin ejecutar acciones ni crear derechos. Incluso si el resultado local es afirmativo, pide autorización del titular y consentimiento pertinente. Una incongruencia de fuentes produce reparación, no una acción improvisada.

Esto es precisamente la aproximación compatible con Ecosystem Awareness, MSCA, gradientes de oportunidad, Ecosystem Positioning o un contrato de ciudadanía agéntica como **arquitecturas candidatas complementarias**: cualificar, señalar, revisar, proponer bajo titularidad y quizá permitir continuar. No establece que un nombre particular de arquitectura sea el único capaz, ni que otro sistema convencional competente no consiga el mismo resultado.

## 6. Solidaridad voluntaria, racionalidad no escalar y riesgo no cuantificado

La decisión solidaria del autor no requiere convertir todo beneficio en una tasa esperada cuantificable. Una persona puede elegir contribuir con información insuficiente para valorar por completo un riesgo, porque valora su participación, sentido, deber de cuidado o relación con otros. Puede **incluso** reportar beneficio propio o económico colectivo; el acto no se define como sacrificio obligatorio. No es irracional simplemente porque falte un ROI ni demuestra que el riesgo sea benigno.

El *mecanismo sintético* distingue: `owner_authorized`, `actor_consent`, `nonwaivable_rights_preserved`, `solidarity_elected`. El algoritmo **no** transforma una negativa o ausencia de consentimiento en permiso, ni compensa un derecho no renunciable con utilidad ajena. Si una decisión permanece indeterminada pero alguien declara solidaridad voluntaria con autorización real y derechos preservados, retorna `VOLUNTARY_UNQUANTIFIED_RISK_REVIEW_ONLY`: **revisión/deliberación pendiente**, no GO automático. No presupone que todo D material pueda aceptarse; los límites de seguridad y daños a terceros requieren legitimidad externa concreta. Nada de esto cambia por sí solo el estado físico o el sufrimiento vivido.

El sentido de *solidaridad elegida* conectado con la reflexión del autor sobre *Magnifica Humanitas* es normativo/interpretativo: dependencia padecida versus participación consciente. No se cita al Papa como validador matemático, no se exige adhesión religiosa ni se iguala dignidad a productividad.

## 7. Sufrimiento estructural y posibilidad de empeorar al saber más

El estudio del PR #43 registra un **constructo estipulado por el autor**, no una medida universal de dolor: brecha positiva entre capacidad desarrollable y actual ante alternativa realizable; intención/aporte genuino del actor y bloqueo externo con base insuficientemente determinable desde su posición. Este estudio puede anotar que un participante *reconoce* una brecha que antes no advertía, sin cambiar la magnitud objetiva de la brecha ni medir bienestar subjetivo. En `structural_exposure`, el campo `new_gap_recognized` varía pero `proxy` sigue igual si la función, la alternativa y el bloqueo siguen iguales.

Podría aumentar el malestar percibido al conocer mejor el bloqueo; también podría disminuirlo al encontrar una causa o una ruta justa. **No hay signo necesario** ni coeficiente impuesto a partir de la entropía, el grado de complejidad o el número de agentes. Se requiere un instrumento humano independiente, custodiado por 01K o la investigación clínica/psicométrica apropiada, para hablar de sufrimiento experimentado.

Caso custodiado: «Una persona extraordinariamente capaz, criada en un barrio socioeconómicamente desfavorecido, cursa un liceo, no logra una plaza universitaria y termina en un trabajo que no le permite desplegar sus capacidades». El ejemplo pertenece a la formulación del autor y NO constituye estadística sobre estudiantes franceses ni prueba de la trayectoria de un individuo concreto. Se preservan capacidades, oportunidades alternativas, restricciones educativas e institucionales, preferencias propias y terceros afectados. No inferir que toda persona en un oficio concreto desea o debería cursar universidad.

## 8. Comparación de coste y controles favorables al competidor

El cálculo de `cost_comparison` sólo representa utilidad neta **si el método entrega la respuesta correcta y legítima**. Con beneficio de diez unidades de una pregunta, Q cuesta 2,25, inspección convencional dirigida 3 y reconstrucción 32: resultados condicionales +7,75 / +7 / −22 frente al cero del A-only conservador. Invirtiendo el coste convencional a 1, éste gana. Un mantenimiento de Q costoso puede hacer que conservar la cartografía no se pague. Sin carácter accesible del estado interno, la reconstrucción se registra como `None`, no como una opción gratuita.

Para estimar ventajas reales faltan: distribución de casos y posibilidad de error **donde sea justificable**; coste de adquisición de cada source qualifier y autenticación; persistencia, caducidad, control de falsa similitud vectorial, presupuesto y plazos; coste de trabajo humano; oportunidades negativas (mantener continuidad) y otros métodos existentes que preservan procedencia/contratos. C no recibe una probabilidad a posteriori por haber sido nombrada; D no se valora sin instrumento. **FH-E** queda como hipótesis de ahorro de cómputo para la *misma pregunta y calidad*, no como ventaja total del sistema.

## 9. Requisitos de falsación

- R1 — Si no hay regularidad válida o testimonio auténtico, el sistema devuelve «no establecido»; cualquier TRUE robusto sería error.
- R2 — Si los testimonios se contradicen, no promedia lo inconmensurable ni convierte silencio en permiso.
- R3 — Una nueva observación compatible puede afinar los límites; una redundante del mismo origen no cuenta como corroboración independiente.
- R4 — Un D material no evaluable que condicione q impide extrapolar el éxito parcial a una decisión general; un D ajeno a la pregunta no bloquea artificialmente todo A.
- R5 — La solidaridad declarada no crea autorización ni sustituye consentimiento; el metaproceso no ejecuta.
- R6 — La percepción de una brecha puede cambiar sin que cambie la brecha; no inventar aumento de sufrimiento.
- R7 — La ampliación de A o el peer convencional debe poder vencer económica y operacionalmente a Q.
- R8 — Un resumen sólo es suficiente para una pregunta previamente declarada; fallar en otra pregunta no invalida automáticamente la primera.
- R9 — No existe en este paquete un algoritmo universal para procesar C/D, una medida del exterior abierto ni una solución del problema de parada.

## 10. Reproducción y revisión

En el directorio de estudio:

```bash
python3 -B -m unittest discover -s . -p 'test_metacognition.py' -v
python3 -B metacognition.py > current.json
python3 -B -c "import json; assert json.load(open('REFERENCE_SYNTHETIC_RESULTS.json')) == json.load(open('current.json'))"
```

Sólo usa la biblioteca estándar de Python. La CI del repositorio ejecuta los mismos checks junto con las pruebas anteriores. Véase [SCIENTIFIC_LIMITS.md](SCIENTIFIC_LIMITS.md) para estado de cada afirmación y [PROMPT_COVERAGE_MATRIX.md](PROMPT_COVERAGE_MATRIX.md) para la concordancia con el Word completo. La corrección algebraica de estas pruebas no equivale a validación de campo ni aprobación de instituciones internacionales.

## 11. Comparación externa de novedad y respuesta estratégica

La [revisión de antecedentes y de casos adversos](EXTERNAL_RESEARCH_NOVELTY_REVIEW_2026-10-26.md) relaciona suficiencia local con Blackwell y Cousot, provenance con W3C PROV-O, cooperación con Ostrom y motivación prosocial con Bénabou–Tirole y Martela–Ryan. **Morris–Shin (2002)** advierte que divulgar más información públicamente en sistemas con complementariedades estratégicas puede alterar el equilibrio y tener un efecto ambiguo sobre bienestar. El lema de no descarte sólo se aplica al problema fijo con políticas previas reproducibles: no certifica por sí solo mayor bienestar social, ni exige difundir Q. El estudio no sustituye consentimiento, ni calcula el residual abierto D.

## 12. Síntesis interdisciplinar de los cuatro PR y programa de validación

La [síntesis transversal de investigación y novedad](CROSS_PR_RESEARCH_NOVELTY_SYNTHESIS_2026-10-26.md) vincula los antecedentes de economía, teoría de juegos, unawareness, capacidades humanas, psicología y medición de bienestar con un programa de pruebas preregistrables de los PR #42–#45. Destaca la precaución sobre valor social de información pública (Morris–Shin), separa brecha de capacidad de dolor informado (OCDE 2025/SDT), exige comparación con soluciones convencionales y conserva todos los ejemplos originales como casos hipotéticos identificados. **No asigna originalidad científica a resultados matemáticos conocidos ni convierte literatura externa en evaluación empírica propia.**
