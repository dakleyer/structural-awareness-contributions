# ACC — A/B/C/D intrínseco al modelo social: composición recursiva, coste de comprensión y residual abierto

**Estado:** propuesta de investigación computacional v0.1, 26 de octubre de 2026. **Autor conceptual:** Iván Abril Palma / The Integral Management Society. **No** constituye un nuevo significado canónico de 00M A/B/C/D, un requisito de ACC, una medición HID/01K, una validación de UC21/DDS, ni una medición humana o universal de la complejidad. **Laboratorio:** modelo finito deliberadamente cerrado para demostrar fenómenos locales; la realidad física/social y sus fronteras B/C/D no quedan clausuradas por el laboratorio.

**Pregunta:** al componer sistemas previamente codependientes mediante funciones de inputs/outputs, ¿podemos derivar un residual de información relevante para el próximo agente **sin un velo ad hoc**? ¿Y puede resultar económicamente más conveniente explotar A con una cualificación limitada, o no explorar, que ampliar A hasta reconstruir todos los subsistemas, manteniendo un B/C/D parcial no fungible?

## 1. Mecanismo estructural: la interfaz como resultado de composición

Definimos un árbol finito de subsistemas. Cada hoja `i` tiene capacidad física `c_i` y entrega `y_i(d_i)=min(d_i,c_i)`. Cada subsistema agregado `g` entrega:

\[y_g(d)=\min\{K_g,\sum_{h\in hijos(g)} y_h(d_h)\}\]

con `K_g` una capacidad de paso limitada, o sin límite cuando su valor es `None`. Esta saturación es física/modelada y verificable, **no** un ocultamiento artificial de estado. El receptor sólo obtiene una respuesta a la demanda actual: `A = y_raíz(d0)`. El experimento le concede además gratuitamente una **topología de nombres/versions estable, sin capacidades** (un comparador más exigente que A-only puro); ni siquiera ella basta para resolver la respuesta futura. Cuando tampoco existe esa topología registrada, el coste de justificarla y transmitirla debe incluirse en B. El modelo finito privado conoce `c_i`, `K_g`; el receptor **no recibe** necesariamente esas variables ni sus valores. No se concede al receptor una función `oracle(world)` por ejecutarse el laboratorio.

Tomamos `d0_i=8`, 16 hojas y una composición recursiva en varios niveles. Dos mundos con la misma entrega `A=128` pueden responder de forma diferente a una demanda posterior que eleva la hoja 3 de 8 a 10: sin restricción compartida adicional, la entrega conjunta pasa a `130`; con límite efectivo de 128 en la raíz, continúa siendo `128`. Los dos mundos son consistentes con el mismo A anterior. El hecho de que la función local sea monótona no implica crecimiento estricto ni capacidad marginal ilimitada: `min(d,c)` deja de crecer tras la saturación.

Este efecto se deriva de un cambio material de la pregunta junto a una interfaz que retuvo sólo la entrega actual. **No se infiere que ningún receptor que posea telemetría, contratos suficientemente ricos o monitorización pueda saberlo.** Tal receptor debe recibir crédito como un comparador competente.

## 2. Insuficiencia de A y suficiencia de la cualificación para una pregunta concreta

Sea `w` el estado privado del subsistema, `E(w)=A` la interfaz a demanda actual y `r_q(w)` la respuesta a la pregunta receptora `q` de demanda futura. El receptor A-only puede decidir exactamente `q` en todos los mundos admitidos sólo si `r_q` es constante sobre cada fibra `E⁻¹(a)`. Si existen `w1,w2` con `E(w1)=E(w2)` y `r_q(w1)≠r_q(w2)`, **ningún procesamiento posterior exclusivamente de A** resuelve ambos. Este es el criterio de factorización de 00M §4 y de *The Given Universe*, no una declaración de incomputabilidad universal.

Una fuente con acceso **legítimo** y una base ya caracterizada puede emitir `B_q`, un certificado acotado sobre la capacidad marginal para la pregunta `q`. Aquí incluye **el trayecto completo relevante** hoja → raíz, su versión, plazo, emisor y la respuesta incremental afirmada. No basta conocer la capacidad de una hoja si hay un cuello común en un antecesor: eso produciría un falso optimismo. El certificado se calcula desde el **registro nativo de outputs actuales de cada componente** y los márgenes de capacidad caracterizados a lo largo del trayecto (no desde una simulación omnisciente de todos los futuros): la hoja aporta su margen disponible y cada antecesor puede reducirlo a su propio margen de paso. Los otros hijos permanecen a demanda fija durante esa pregunta; si una influencia externa puede alterarles, la afirmación debe reabrirse. La producción del registro tiene costes de instrumentación y conservación que se incluyen en el contrato económico, y la fuente tiene que disponer realmente de esos registros. El certificado original es B respecto de la actividad de explotación del productor; generar ese certificado es A de una función de cualificación distinta. Su aceptación por el receptor exige una relectura de alcance y procedencia; la presente prueba sólo valida declaraciones de formato, identidad convencional y versión, **no firmas independientes, verdad ni libertad de coacción**.

Si `B_q` aporta una distinción real sobre una pregunta q, la información admitida pasa de `E(w)` a `(E(w),B_q(w))`, separando algunas fibras; **no** determina el contenido completo del interior ni del exterior. Dos copias del mismo testimonio, B de fuentes dependientes o una similitud semántica vectorial no son dos pruebas independientes ni cubren un D residual.

## 3. A/B/C/D aparecen por las capacidades de evaluación del proceso, no por clasificar un universo completo

El modelo no divide todos los subsistemas en cuatro conjuntos enumerables. Estas son POSICIONES sobre **declaraciones de procesos**, relativas a actor, función, pregunta, acceso, método y horizonte:

- **A:** entrega efectiva del proceso a la demanda actual, p. ej. 128 unidades. Si el proceso de cualificación entrega un nuevo certificado como su resultado, **ése es A de ese segundo proceso**, sin transformar retrospectivamente el A productivo.
- **B:** fundamento conocido y *reserva de evaluación caracterizada*, p. ej. contrato de interfaces, capacidad de evaluar un trayecto de subsistemas y condiciones de soporte, vigencia y coste **del alcance declarado**. No es un inventario exhaustivo del ecosistema ni de todas las reservas.
- **C:** pista fundada de otra vía potencialmente explorable, p. ej. un interlocutor con capacidades prometedoras de diagnóstico, pero sin marco caracterizado de targets, variables, esfuerzo y retorno. **C no viene con ROI ex ante calculable** bajo el contrato 00M. Un ensayo acotado puede producir un nuevo A sobre qué se descubrió y quizá una nueva reserva B; puede también fracasar.
- **D:** testimonio de una influencia material que afecta posiblemente a la actividad receptora y cuya evaluación efectiva está fuera de su acceso/método/autoridad/tiempo actuales, aunque otra entidad quizá pueda tratarla. D admite monitorización de algunos signos sin estimación de efectos. **Ninguna señal** sobre una dependencia no permite inventarle una etiqueta D: su papel sigue `ROLE_NOT_ESTABLISHED`.

Un productor puede tener B sobre su propia capacidad y el receptor tener C sobre esa misma cuestión. O una influencia puede ser D para el receptor y B para otro actor. Nunca se suman 'cantidades de C y D' no identificadas. La función `plan_from_public(PublicView, ...)` utiliza sólo A, el esqueleto sin capacidades, evidencia B/C/D recibida y un presupuesto finito; no tiene acceso a secretos privados. Sólo `score_public_plan(world, plan)` evalúa a posteriori el efecto real del experimento, sin realimentar el plan con la verdad. La envolvente `receiver_decision` encadena ambas fases para el estudio reproducible. El `private oracle` del experimento puntúa después si acertó.

## 4. Coste de comprensión y regla de inversión limitada

La ampliación exhaustiva de A, para una consulta, exige adquirir y validar toda la estructura interna en una simulación finita. Introducimos un coste CONTABLE supuesto `C_full=c_n·N`, con `N` nodos del árbol. El coste de una cualificación situada `C_B=c_path·L+c_transmisión+c_mantenimiento`, con `L` nodos del trayecto necesarios para q. El coste de inspección dirigida `C_target` representa el MEJOR comparador convencional pertinente si dispone del mismo acceso. Preparar, acreditar, transportar, revisar y mantener B **no es gratis**; tampoco el coste de observación/verificación se sustituye por el número de bits de Shannon.

Una decisión puntual puede producir a lo sumo `Vmax=Δy_max·v` unidades monetarias del juguete. Si `C_full>Vmax` y A-only puede mantener sin coste el servicio actual, la exploración exhaustiva de todas las interfaces no puede mejorar la utilidad neta para **esta sola pregunta**, incluso si resuelve toda la información del laboratorio. Esa es una desigualdad simple bajo un presupuesto cerrado y valor acotado, NO una prueba de que toda exploración sea inútil ni de que D sea matemáticamente inaccesible. El juicio de C, cuyo ROI es aún no caracterizable, no se fuerza dentro de esa ecuación.

**Caso sintético verificado, n=16:** el sistema observa A=128; el valor bruto de entregar las 2 unidades adicionales de la demanda elegida es 10; hay 32 nodos modelados y coste de revisar todos de 32; adquirir B para la pregunta cuesta 2,25; una revisión convencional dirigida cuesta 3. Con capacidad 130 real en el mundo de ensayo:

| Modo | Coste explícito | Valor bruto observado | Valor neto |
|---|---:|---:|---:|
| A-only, conservador | 0 | 0 | 0 |
| A + B situado, verificado por alcance/versión | 2,25 | 10 | **7,75** |
| Exploración convencional dirigida | 3 | 10 | **7** |
| Ampliación completa de A (32 nodos) | 32 | 10 | **−22** |

En el mundo alternativo con cuello en la raíz, A sigue siendo 128, pero **el mismo tipo de B situado declara incremento 0**, no incremento 2. La capacidad local de la hoja **no** compensa la falta de capacidad del subsistema superior. Si no hay acceso, `FULL_SCOPE_NOT_ACCESSIBLE`/`TARGETED_NO_EFFECTIVE_ROUTE` impiden fingir evaluación. Cuando la capacidad marginal es cero, pagar por B o por inspección puede crear una pérdida neta: **no hay ganancia garantizada**. Un certificado falso con forma válida puede producir una promesa errónea; los controles adversos lo muestran.

**Comparador indispensable:** cuando la inspección convencional dirigida cuesta sólo 0,1, supera a B; cuando la inspección completa es muy barata, puede superar a B; cuando existen muchas preguntas futuras que exigen conocer todas las ramas, la revisión de todo el sistema puede amortizarse. No hay ventaja diferencial de EA demostrada ni monopolio sobre conservar metadatos. El estudio pretende identificar condiciones donde la cualificación situada es económicamente preferible y sus condiciones negativas.

## 5. Una relación informacional verificable sin clausura del exterior

En un LABORATORIO binario con n capacidades futuras independientes, la entrega actual idéntica admite `2^n` perfiles completos de respuestas futuras. Responder correctamente **todas las n preguntas individuales con un único mensaje exacto fijo** exige distinguir `2^n` perfiles y requiere al menos n bits. Responder sólo a una pregunta binaria escogida requiere como máximo uno (además de la identidad de la pregunta acordada); responder al conteo agregado de capacidades extra admite n+1 respuestas posibles, y necesita `ceil(log2(n+1))` bits bajo el mismo juego completo. Estas son cotas de **comunicación de un experimento finito**, no de tiempo de ejecución universal ni de entropía ontológica D. La estructura de la consulta modifica qué constituye suficiencia.

Con una distribución `P` explícita sobre los estados instrumentados se podría calcular `H(R|A)−H(R|A,Q)=I(R;Q|A)`; sin una distribución identificada esa cifra **no existe como observación**. No se atribuye distribución, cardinalidad ni entropía a todo el exterior abierto. Tampoco se generaliza a 'todo sistema suficientemente complejo es irresoluble': algunas composiciones se analizan por técnicas polinómicas, herramientas especializadas o interfaces convenientes.

## 6. Integración intrínseca con ACC y el modelo social (sin dar propiedades nuevas al exterior)

El subsistema social que entrega un vector de producción y utilidades bajo restricciones de recursos y coordinación puede integrarse en el suprasistema como una unidad de producción `A_i`. Su capacidad de ampliar producción puede depender de cuellos internos y autorizaciones que la interfaz actual NO caracteriza completamente. Un nuevo agente necesita un input X pero sólo observa X−200 o X−100 sin conocer el mecanismo pertinente: la salida actual puede ser correcta y su expectativa de desarrollo futuro, insuficientemente fundada. Este testimonio es un **ejemplo narrativo del autor**, no un resultado económico empírico.

La estructura de ACC ya distingue la viabilidad de estados finales, alcanzabilidad de transiciones, brechas objetivas G y capacidades humanas 01K. La qualificación Q modifica lo que el receptor puede justificar e investigar, NO el mundo físico ni las disponibilidades presupuestarias por sí misma. En algunos escenarios Q puede permitir identificar y coordinar una reasignación real; en otros solo permite abstenerse, corregir una predicción o declarar que no hay camino. Una evaluación humana de sufrimiento estructural exigiría además una alternativa conjuntamente realizable, una contribución reconocida y la experiencia/agencia del sujeto, **no** inferible de haber detectado D.

El proceso económico tiene ahora cuatro estrategias competidoras (A-only; B situado; inspección dirigida; inspección exhaustiva) y dos fronteras abiertas (C fundada pero no evaluable todavía; D material sin ruta efectiva). Eso hace que A/B/C/D emerja **del funcionamiento, los costes y la capacidad del proceso** en vez de añadirse como etiqueta a un inventario de mundo. La tipificación de las evidencias protege contra errores pero no prueba completitud; C y D siguen abiertos. Se debe mantener a un comparador convencional competente con interfaces y fuentes equivalentes.

## 7. Método y límites de validación

Ejecución reproducible en Python estándar: `python -B -m unittest discover -s . -p 'test_*.py' -v`; `python -B intrinsic_abcd.py > REFERENCE_SYNTHETIC_RESULTS.json`. El CI del PR comprobará que la salida generada coincide con el JSON publicado, además de ejecutar las pruebas negativas. Todas las métricas del laboratorio están en valores hipotéticos declarados y separan fuente, adquisición, decisión y efecto observado.

**Condiciones para revisión y promoción:** (1) preservar semántica 00M/00N B≠C≠D, procesos relativos y no exhaustivos; (2) demostrar que `A_current` es exactamente igual entre brazos; (3) contabilizar costes de fuente, adquisición/almacenamiento y transferencia; (4) documentar capacidad de reevaluación, vencimientos y revisiones; (5) negar la equivalencia 'más complejidad ≡ más D/entropía'; (6) admitir victorias del comparador convencional y fallos de B; (7) nunca valorar el sufrimiento humano o HID con bits o unidades de valor sintético; (8) auditar verdad/identidad de Q en estudio posterior; (9) preservar casos históricos con su contexto en [registro de ejemplos del PR #42](../bounded-traps-v0.1/EXAMPLE_LEDGER.md).

## 8. Referencias de fuente en el mismo corpus

- [00M §1 y §4, definiciones canónicas de roles y suficiencia](../../../../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md)
- [00N, composición funcional y alcance](../../../../00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md)
- [01A-A01, FH-C/FH-E](../../../../01A_A01_MISSION_DRIFT_CAUSAL_PRIORITY_AND_EPISTEMIC_ECONOMY_HYPOTHESES_v0.1_RESEARCH_NOTE.md)
- [ACC model core](../../ECONOMIC_MODEL_TECHNICAL_CORE_v0.1.md), [ACC exposition](../../MODEL.md).
- [Nested-composition and structural-suffering model](../nested-composition-suffering-v0.1/README.md) (parent study, 32 tests).
- [Shannon/preimages and 2025 PEF/D1–D3 documents](https://docs.google.com/document/d/1qpBDFBZa7nGKlTD2D5poYuStCf0oJcAogBtUuzEjD90/edit) (historical literature; no universal entropy equivalence established).

## 9. Auditoría interna del alcance

[Revisión de afirmaciones, supuestos, fuentes y controles negativos](SCIENTIFIC_REVIEW_AND_NEGATIVE_CONTROLS.md). Incluye el coste de conservar los logs operacionales fuente, la autenticación aún no implementada y los ámbitos donde **el comparador convencional gana** o el residual sigue no establecido. Es una auditoría del mismo equipo asistido, no un dictamen científico independiente.

## 10. Anteriores resultados sobre unawareness, abstracción y procedencia

La [revisión comparada](EXTERNAL_RESEARCH_NOVELTY_REVIEW_2026-10-26.md) identifica investigación existente de Heifetz–Meier–Schipper (desconocimiento interactivo), Cousot–Cousot (interpretación abstracta), Blackwell (valor de información) y W3C PROV-O (procedencia). La novedad **no** es clasificar lo desconocido ni añadir metadatos conocidos: la contribución candidata a probar es el coste y la corrección de la **cualificación situada producida por la fuente** al integrarse en una decisión social/económica específica. Mantener comparación fuerte con inspección convencional dirigida, costes de ciclo de vida, fuentes falsas y verdaderos no resultados.



## 11. Salida física nativa reproducible (K-03; 28 de octubre de 2026)

La función fuente `private_selected_response(world, target, minimum=8, extra=2)`
evalúa la **misma pregunta individual q** en dos estados de demanda y devuelve un
`PrivateSelectedResponse` inmutable con `current_A`, `selected_output` y
`gain = selected_output - current_A`. Reutiliza `base_demand`,
`selected_demand` y la entrega material recursiva `deliver`; **no cambia
el mecanismo** ni interpreta la ganancia física como bienestar humano.

El contrato queda integrado en tres consumidores originales:

- `policy`: compara políticas usando la salida física del simulador, manteniendo
  por separado los costes y las promesas de cada brazo.
- `score_public_plan`: puntúa *después* la planificación hecha con `plan_from_public`,
  sin entregar el oráculo al receptor.
- `sample_report`: obtiene las ganancias +2/0 a partir de las respuestas
  ejecutadas, sin números escritos a mano.

**Frontera conservada:** `upstream_B` sigue emitiendo una cualificación para
una sola pregunta a partir de logs operacionales de la fuente y holguras del
trayecto; no llama al oráculo de futuro. `plan_from_public` sigue recibiendo
únicamente la vista pública y los certificados válidos. Esta función privada
no fusiona B de preguntas diferentes ni concede al receptor nuevos datos.

El nuevo `test_native_selected_response.py` verifica la ecuación de
conservación en **6720 preguntas materiales distintas**, la concordancia con
todos los brazos, la separación entre emisión pública y evaluación privada,
la inmutabilidad y que el informe consume resultados computados. No cambia
`REFERENCE_SYNTHETIC_RESULTS.json`, pues los dos mundos originales siguen
dando exactamente 128→130 y 128→128.

**Reutilización transversal:** el [comparador económico social/agéntico del
PR #66](https://github.com/dakleyer/structural-awareness-contributions/pull/66)
consume la respuesta pública de cada política y su puntuación nativa, no
reimplementa `deliver` ni adopta este oráculo como criterio de decisión.
Cada nuevo adaptador conserva la función de respuesta y la pregunta de su
propio sistema.
