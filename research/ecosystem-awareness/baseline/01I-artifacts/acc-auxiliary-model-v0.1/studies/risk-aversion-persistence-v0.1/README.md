# RAV-01 — Permanencia racional con sufrimiento creciente bajo riesgo de transición

**26 de octubre de 2026 · autor conceptual: Iván Abril Palma / The Integral Management Society.**
**Estado:** extensión auxiliar de investigación, numérica y matemáticamente condicional. PR apilado sobre #45 (a su vez #44 → #43 → #42). **No fusionado, no validado empíricamente y sin cambio a los contratos normativos ACC, 00M/00N, 01K/HID, DDS o UC21.**

## 1. Pregunta delimitada

¿Puede un agente **seguir teniendo más bienes y servicios**, **sufrir más que antes**, pensar que el futuro del régimen actual será peor y, sin embargo, **elegir racionalmente no abandonarlo** aun cuando el rediseño ofrezca **mayor retorno esperado**?

**Segunda pregunta (ampliación):** ¿puede, además, **gastar esfuerzos o recursos en defender activamente el modelo que le hace sufrir**, sin que esto implique satisfacción, optimismo ni mejora del óptimo social? La elección entre S, R y D requiere una hipótesis adicional y verificable sobre el efecto de la defensa.

**Sí, como posibilidad matemática condicionada.** No requiere que el agente desee sufrir ni que aumente su aversión al riesgo; basta una distribución de resultados de salida suficientemente más dispersa que la de permanencia, bajo un criterio declarado de preferencia ante riesgos.

Esto NO prueba que ocurra así en un país, una generación o toda sociedad. Tampoco demuestra que **más producción cause** más varianza: la relación entre escala, interdependencia, brecha y riesgos es hipótesis separada que habría que identificar.

### Frontera con el modelo existente

- El [núcleo técnico, §8.1](../../ECONOMIC_MODEL_TECHNICAL_CORE_v0.1.md) mantiene Gᵀ/Gᴳ como brechas a configuraciones conjunta y legítimamente factibles; G no es el retorno esperado de salir.
- F es malestar humano **independientemente medido**; en este toy se introduce un F numérico *estipulado* solo para comprobar compatibilidad algebraica, sin pretender medir personas ni derivarlo de G.
- B y W=B−F requieren que B no contenga ya F; no sumar dos veces C, HID, trabajo compensatorio, incomodidad ni costes financieros.
- Una trayectoria futura R pertenece al análisis decisional sólo cuando su factibilidad material y derechos están declarados. Un cálculo CE favorable no autoriza acciones o redistribuciones. La probabilidad de elección no es la probabilidad de éxito.
- Los PR #42–#45 ya contienen rendimientos, utilidad no monótona, acoplamientos, observabilidad y sufrimiento estructural. **RAV-01 no los redefine ni introduce otro esquema Pareto.**
- El PR #43 identifica un **sufrimiento estructural** solo con requisitos conjuntivos (potencial bloqueado, contribución positiva, codependencia externa e indeterminación); su resultado no se deduce de F, una brecha genérica o del nuevo L individual.

## 2. Testigo formal que se puede refutar

Para **un mismo actor i**, numerario y horizonte H, comparar las políticas:

- **S:** conservar el contrato, rol o localización actual.
- **R:** rediseñar/salir de él, con coste de transición C≥0 adicional a los resultados declarados.

Sean X_S~Normal(μ_S,σ²_S), X_R~Normal(μ_R,σ²_R): dos loterías de resultados **netos comparables** con distribución explícita. Nada aquí caracteriza el exterior abierto B/C/D; este modelo opera sólo dentro de un riesgo especificado. Supóngase utilidad exponencial u(x)=−exp(−γx), γ>0 constante. Por el momento generador de la normal:

`E[exp(−γX)] = exp(−γμ + γ²σ²/2)`.

La equivalencia cierta resuelve `u(CE)=E[u(X)]` y queda:

`CE(X)=μ−(γ/2)σ²`

`ΔCE=(μ_R−μ_S)−(γ/2)(σ²_R−σ²_S)−C`.

Una persona que maximiza esa utilidad espera si ΔCE<0 incluso cuando μ_R>μ_S. **γ no ha aumentado**; la prima de riesgo adicional es `(γ/2)·(σ²_R−σ²_S)`. Si γ>0, el umbral de permanencia es `Δσ²>2·(Δμ−C)/γ`. A γ=0 se usa la extensión límite CE=μ (agente neutral al riesgo), no la función exponencial degenerada. Una variación de la media suficiente o una reducción de varianza puede revertir el resultado.

Modelo de decisión opcional y **no estimado**: si hay ruido de elección EV1 independiente con escala 1/κ (κ>0), `Pr(R)=logistic(κ·ΔCE)`. Esta frecuencia probabilística propuesta no significa que la persona crea las probabilidades correctas ni mide éxito, ingresos o seguridad real.

## 3. Único ejemplo numérico, dos cortes y un pronóstico adverso

**Cortes sintéticos** (misma γ=0,5, mismo κ=1, C=0; escalas arbitrarias y comparables, ninguna cifra nacional):

| Corte | E[X_S] | Var(X_S) | CE_S | E[X_R] | Var(X_R) | CE_R | Ventaja media de R | Ventaja CE de R | Decisión |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Inicial | 10 | 4 | 9 | 16 | 36 | 7 | +6 | −2 | Permanecer |
| Posterior | 14 | 4 | 13 | 25 | 64 | 9 | +11 | −4 | Permanecer |

Aunque aumenta la ganancia media esperada de R de 6 a 11, permanecer resulta todavía más preferible bajo las mismas preferencias al aumentar la prima de riesgo de 8 a 15. Si se postula el logit κ=1, Pr(R) pasa de 0,119203 a 0,017986, **probabilidades del toy, no observaciones**.

Al mismo tiempo se pueden estipular B=(12,20,30) y F=(2,6,13), con W=(10,14,17): crecen B, F y W, pero F aumenta con curvatura positiva (incrementos 4 y 7). **Más bienes, más bienestar neto y más sufrimiento** coexisten dentro de esas condiciones. No hemos medido F en seres humanos.

Una persona que hoy observa W=17 puede estimar que el futuro de **seguir S** será peor (μ_S futura=14, menor que 17) y **seguir eligiendo S** frente a R por su equivalente cierto 13 frente a 9. Pronóstico negativo ≠ preferencia automática por cambiar.

## 4. Ilustración narrativa única, no estadística

Una persona procedente de Colombia, instalada en España, puede haber pasado años lejos de su familia, vivir con obligaciones hipotecarias, sentirse insatisfecha y evaluar que regresar a Colombia para comprar una vivienda y abrir un negocio ofrecería mayor resultado medio. También puede anticipar la pérdida de estabilidad de ingresos, un negocio fallido o la imposibilidad de volver a su posición. Decide quedarse, quizá criticando y pronosticando el deterioro futuro del sistema en que permanece.

La hipótesis distingue **riesgo del salto** de seguridad real, apego a las personas, cobertura social, derechos, barreras legales, obligaciones, selección migratoria, sesgos o motivos culturales. No presupone que emigrar o retornar sea objetivamente mejor para ninguna persona y no asigna cifras o probabilidades a Colombia o España.

La sierra, las rotondas y el contrato social son metáforas motivadoras, **no variables observadas**. No se necesitan más casos anecdóticos para demostrar esta posibilidad algebraica.


### 4.1. Tercera decisión: defender el contrato y reconocer utilidad no realizada

La explicación de la permanencia no debe confundirse con la defensa activa. Introducimos una tercera política **D**, distinta de no actuar **S** y rediseñar/salir **R**. D supone un coste propio k declarado fuera de su resultado, y una lotería X_D que modifica **de verdad** o, en un ensayo de creencias, **según creencia declarada**, la continuidad para el mismo actor. El testigo compara tres equivalentes ciertos:

~~~text
CE_S=μ_S−(γ/2)σ²_S
CE_R=μ_R−(γ/2)σ²_R−C
CE_D=μ_D−(γ/2)σ²_D−k
D > S si (μ_D−μ_S)+(γ/2)(σ²_S−σ²_D)>k
~~~

En el **mismo corte posterior**, S=(14,4), CE=13; R=(25,64), CE=9; D=(14,1), k=0,5, CE_D=13,25. En este testigo se **defiende activamente** el contrato, aun reconociendo un resultado medio mayor de R, el F sintético creciente y un mal pronóstico del próximo periodo. **D que no cambie la media ni la varianza de la utilidad total** (no solo el dinero), y cueste k>0, está dominada por S dentro del criterio declarado. Si D se elige pero solo se han medido ingresos, hay que comprobar primero afecto, cuidado, reputación, identidad u otros argumentos de utilidad antes de declarar que el modelo económico ha fallado. **Contracontrol:** con el mismo resultado material S=(14,4), una utilidad intrínseca de cuidado +1 en D y coste k=0,5 da D total=(15,4), CE_D=13,5 > CE_S=13, sin protección adicional ni mecanismo no isomórfico demostrado.

Es distinto constatar un sufrimiento vivido **F** de reconocer que, para **esta persona y un mismo horizonte**, una alternativa **conjunta y legítimamente factible** podría ofrecer mayor utilidad cardinal: **L=max(0,u_factible−u_realizada)**. L es una **pérdida económica contrafactual de utilidad**; llamarla «sufrimiento económico» es una convención operacional que **no valida automáticamente** sufrimiento subjetivo. La asociación de L reconocido con F reportado es hipótesis empírica abierta. Si la factibilidad no está acreditada, L es **NOT_IDENTIFIED**. No equipararla con Gᵀ/Gᴳ, HID ni el sufrimiento estructural conjuntivo del PR #43. En el escenario sintético se estipula utilidad realizada 17, referencia factible 21 y L=4; no se han identificado esas magnitudes para personas reales.

**Literatura y delimitación:** [Investigación comparativa y diseño de falsación](COMPARATIVE_RESEARCH_AND_TEST_DESIGN.md) contiene la tabla con ocho trabajos primarios, lo que compartimos, lo que explicamos de otro modo y lo que el PR **no** predice. Los antecedentes ya estudian sesgo de statu quo, opciones de esperar, justificación del sistema, compromiso creciente, ingresos relativos y aspiraciones. El aporte candidato es **formular conjuntamente y someter a contrapruebas** L, F, distribución de riesgo, elección S/R y acción D, sin reivindicar el fenómeno como original.

## 5. Qué podría refutar la explicación

| Control | Mantener constantes | Variación / expectativa | Consecuencia |
|---|---|---|---|
| Riesgo neutral | Medias, costes, viabilidad | γ=0 | Si Δμ>C, R se prefiere; desaparece la prima |
| Salida igual de predecible | Medias, γ y C | Var(R)=Var(S) | Si Δμ>C, R se prefiere |
| Rediseño reversible/protegido | Medias, γ | Menor Var(R) y/o menor C | Puede volverse preferible R |
| Retorno esperado mucho mayor | Varianzas, γ y C | Aumentar μ_R | Se invierte preferencia |
| Pronóstico actual negativo | Horizonte y escala | μ_S futura por debajo del resultado actual | Permanencia sigue siendo posible, no necesaria |
| Defensa sin beneficio en **utilidad total** | Misma μ_D=μ_S y Var(D)=Var(S) del resultado total; k>0 y sin otra diferencia factible | D dominada por S | Si se elige, revisar utilidad/creencias/derechos omitidos antes de postular otro mecanismo |
| Defensa protectora | γ, μ_S, R, costes y unidad | Reducir Var(D) lo suficiente con k observable | Puede elegirse D y no solo S, pero no garantiza eficiencia social |
| Utilidad perdida factible | Referencia personal y derechos/recursos equiparados | Elevar L reconocida sin cambiar automáticamente F | Medir F aparte; sin contrafactual válido L queda NOT_IDENTIFIED |
| Ganancias netas y malestar | B y F independientes | F crece con curvatura, B lo supera por intervalos | W puede seguir aumentando; no es identidad universal |
| Incertidumbre abierta | B/C/D cualificaciones | No existe distribución calibrada | NO asignar γ·σ² inventado ni tasas de salida |
| Derechos y factibilidad | Conjuntos Fᵀ/Fᴳ | Ruta R no autorizable o no alcanzable | No inferir elección libre entre dos opciones equivalentes |

### Identificación empírica pendiente

Registrar antes del experimento horizonte, persona/población, bienestar y recursos, distribución objetiva y distribución **creída**, incertidumbre no probabilizable, transición real, su reversibilidad, costes, derechos y **las tres decisiones S/R/D**; medir F con instrumento humano independiente. Para D, registrar gasto, protección real o percibida, identidad/vínculos y posibles costes impuestos a terceros. Contrastar L solo bajo utilidad cardinal comparable, alternativa factible y derechos preservados. Distinguir utilidad relativa y absoluta, aversión al riesgo γ, sensibilidad κ y vínculos/identidad. Comparar con modelos de utilidad alternativa (p. ej. CRRA), colas pesadas, pérdidas de subsistencia, aversión a pérdidas y valor de esperar; todos pueden cambiar o derrotar el testigo.

Para afirmar *causalidad* del tamaño de la cordillera sobre permanencia hacen falta evidencias adicionales: crecimiento de la dispersión **diferencial** del cambio respecto a seguir, sin confundirlo con mera volatilidad temporal o aumento de G. El resultado social puede ser subóptimo pese a una elección individual localmente racional. No inferir bienestar humano, aprobación institucional ni aplicación operativa desde este toy.

## 6. Reproducción y propiedad

- [risk_model.py](risk_model.py): módulo estándar puro (sin paquetes externos) con resultados esperados, equivalentes ciertos, prima de riesgo, utilidad individual factible perdida, tercera defensa D, logit binario y softmax ternario opcionales, y validación de parámetros.
- [test_risk_model.py](test_risk_model.py): **43 pruebas deterministas** de identidades, permanencia, defensa activa, contrapruebas de defensa inútil, utilidad contrafactual no identificada, controles favorables a salir y tres controles de reducción (afecto como utilidad, bonificación específica por acción y límite de media-varianza sin normalidad).
- [REFERENCE_SYNTHETIC_RESULTS.json](REFERENCE_SYNTHETIC_RESULTS.json): salida reproducible marcada como `SYNTHETIC_CONDITIONAL_NOT_EMPIRICAL`.
- [COMPARATIVE_RESEARCH_AND_TEST_DESIGN.md](COMPARATIVE_RESEARCH_AND_TEST_DESIGN.md): comparación crítica con ocho obras primarias, alcance, no predicciones, matriz factorial 2×2×2 y falsadores.
- [EXTENSION_ISOMORPHIC_NONISOMORPHIC_RESEARCH_v0.1.md](EXTENSION_ISOMORPHIC_NONISOMORPHIC_RESEARCH_v0.1.md): programa **propuesto, no ejecutado** y **auditoría de reducción U0–U6**: antes de afirmar no isomorfismo para validación social, afecto, compromiso o agentes computacionales exige modelar utilidad total, comparar distribuciones y probar exactamente qué predicado se pierde. Incluye lemas formales, contraejemplos, mapas condicionados y falsadores por disciplina. No cambia el testigo histórico ni hereda evidencia automáticamente.
- [**Campaña EX/01: 20 casos de las rotondas**](experiments-from-escritos-v0.1/README.md): 20 configuraciones sintéticas, 39 puntos de sensibilidad, 39 nuevas pruebas; teletrabajo, jardín, plataformas, ciudad/clima, rotondas, parque con deuda intergeneracional, migración/riesgo, sierra y vivienda. Incluye controles donde la opción criticada **sí** genera valor, parámetros versionados y JSON de referencia. No convierte el escrito personal en evidencia estadística ni altera F/G/HID.

Ejecutar desde la raíz del repositorio:

```bash
python -B -m unittest discover -s research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/risk-aversion-persistence-v0.1 -p test_risk_model.py -v
python -B research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/risk-aversion-persistence-v0.1/risk_model.py
python -B -m unittest discover -s research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/risk-aversion-persistence-v0.1/experiments-from-escritos-v0.1 -p test_scenario_campaign.py -v
python -B research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/risk-aversion-persistence-v0.1/experiments-from-escritos-v0.1/scenario_campaign.py
```

La prueba de integridad documental del PR compara **ambas** salidas JSON y ejecuta los **43 tests originales más 39 de la campaña**. La campaña es un instrumento sintético condicionado, no una estimación de preferencias reales. **Fuentes de investigación previas**: [PR #42](https://github.com/dakleyer/structural-awareness-contributions/pull/42) → [#43](https://github.com/dakleyer/structural-awareness-contributions/pull/43) → [#44](https://github.com/dakleyer/structural-awareness-contributions/pull/44) → [#45](https://github.com/dakleyer/structural-awareness-contributions/pull/45). Referencia narrativa privada: «La generación de las rotondas» v0.6 en Escritos. La referencia no transfiere el ensayo privado al repositorio público.

**Puerta de promoción:** revisión del propietario de la interpretación de «sufrimiento» y de los límites de la distribución, CI real y revisión de genealogía apilada. No fusión automática.
