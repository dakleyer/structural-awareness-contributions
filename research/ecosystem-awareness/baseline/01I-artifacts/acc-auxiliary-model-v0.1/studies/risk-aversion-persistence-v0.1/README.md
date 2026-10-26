# RAV-01 — Permanencia racional con sufrimiento creciente bajo riesgo de transición

**26 de octubre de 2026 · autor conceptual: Iván Abril Palma / The Integral Management Society.**
**Estado:** extensión auxiliar de investigación, numérica y matemáticamente condicional. PR apilado sobre #45 (a su vez #44 → #43 → #42). **No fusionado, no validado empíricamente y sin cambio a los contratos normativos ACC, 00M/00N, 01K/HID, DDS o UC21.**

## 1. Pregunta delimitada

¿Puede un agente **seguir teniendo más bienes y servicios**, **sufrir más que antes**, pensar que el futuro del régimen actual será peor y, sin embargo, **elegir racionalmente no abandonarlo** aun cuando el rediseño ofrezca **mayor retorno esperado**?

**Sí, como posibilidad matemática condicionada.** No requiere que el agente desee sufrir ni que aumente su aversión al riesgo; basta una distribución de resultados de salida suficientemente más dispersa que la de permanencia, bajo un criterio declarado de preferencia ante riesgos.

Esto NO prueba que ocurra así en un país, una generación o toda sociedad. Tampoco demuestra que **más producción cause** más varianza: la relación entre escala, interdependencia, brecha y riesgos es hipótesis separada que habría que identificar.

### Frontera con el modelo existente

- El [núcleo técnico, §8.1](../../ECONOMIC_MODEL_TECHNICAL_CORE_v0.1.md) mantiene Gᵀ/Gᴳ como brechas a configuraciones conjunta y legítimamente factibles; G no es el retorno esperado de salir.
- F es malestar humano **independientemente medido**; en este toy se introduce un F numérico *estipulado* solo para comprobar compatibilidad algebraica, sin pretender medir personas ni derivarlo de G.
- B y W=B−F requieren que B no contenga ya F; no sumar dos veces C, HID, trabajo compensatorio, incomodidad ni costes financieros.
- Una trayectoria futura R pertenece al análisis decisional sólo cuando su factibilidad material y derechos están declarados. Un cálculo CE favorable no autoriza acciones o redistribuciones. La probabilidad de elección no es la probabilidad de éxito.
- Los PR #42–#45 ya contienen rendimientos, utilidad no monótona, acoplamientos, observabilidad y sufrimiento estructural. **RAV-01 no los redefine ni introduce otro esquema Pareto.**

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

## 5. Qué podría refutar la explicación

| Control | Mantener constantes | Variación / expectativa | Consecuencia |
|---|---|---|---|
| Riesgo neutral | Medias, costes, viabilidad | γ=0 | Si Δμ>C, R se prefiere; desaparece la prima |
| Salida igual de predecible | Medias, γ y C | Var(R)=Var(S) | Si Δμ>C, R se prefiere |
| Rediseño reversible/protegido | Medias, γ | Menor Var(R) y/o menor C | Puede volverse preferible R |
| Retorno esperado mucho mayor | Varianzas, γ y C | Aumentar μ_R | Se invierte preferencia |
| Pronóstico actual negativo | Horizonte y escala | μ_S futura por debajo del resultado actual | Permanencia sigue siendo posible, no necesaria |
| Ganancias netas y malestar | B y F independientes | F crece con curvatura, B lo supera por intervalos | W puede seguir aumentando; no es identidad universal |
| Incertidumbre abierta | B/C/D cualificaciones | No existe distribución calibrada | NO asignar γ·σ² inventado ni tasas de salida |
| Derechos y factibilidad | Conjuntos Fᵀ/Fᴳ | Ruta R no autorizable o no alcanzable | No inferir elección libre entre dos opciones equivalentes |

### Identificación empírica pendiente

Registrar antes del experimento horizonte, persona/población, bienestar y recursos, distribución objetiva y distribución **creída**, incertidumbre no probabilizable, transición real, su reversibilidad, costes, derechos y decisión observada; medir F con instrumento humano independiente. Distinguir utilidad relativa y absoluta, aversión al riesgo γ, sensibilidad κ y vínculos/identidad. Comparar con modelos de utilidad alternativa (p. ej. CRRA), colas pesadas, pérdidas de subsistencia, aversión a pérdidas y valor de esperar; todos pueden cambiar o derrotar el testigo.

Para afirmar *causalidad* del tamaño de la cordillera sobre permanencia hacen falta evidencias adicionales: crecimiento de la dispersión **diferencial** del cambio respecto a seguir, sin confundirlo con mera volatilidad temporal o aumento de G. El resultado social puede ser subóptimo pese a una elección individual localmente racional. No inferir bienestar humano, aprobación institucional ni aplicación operativa desde este toy.

## 6. Reproducción y propiedad

- [risk_model.py](risk_model.py): módulo estándar puro (sin paquetes externos) con resultados esperados, equivalentes ciertos, prima de riesgo y logit opcional, validación de parámetros.
- [test_risk_model.py](test_risk_model.py): **24 controles deterministas** de identidades, casos adversos, mala predicción compatible y contrapruebas que favorecen salir.
- [REFERENCE_SYNTHETIC_RESULTS.json](REFERENCE_SYNTHETIC_RESULTS.json): salida reproducible marcada como `SYNTHETIC_CONDITIONAL_NOT_EMPIRICAL`.

Ejecutar desde la raíz del repositorio:

```bash
python -B -m unittest discover -s research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/risk-aversion-persistence-v0.1 -p test_risk_model.py -v
python -B research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies/risk-aversion-persistence-v0.1/risk_model.py
```

La prueba de integridad documental de la PR compara salida JSON y ejecuta los tests. **Fuentes de investigación previas**: [PR #42](https://github.com/dakleyer/structural-awareness-contributions/pull/42) → [#43](https://github.com/dakleyer/structural-awareness-contributions/pull/43) → [#44](https://github.com/dakleyer/structural-awareness-contributions/pull/44) → [#45](https://github.com/dakleyer/structural-awareness-contributions/pull/45). Referencia narrativa privada: «La generación de las rotondas» v0.6 en Escritos. La referencia no transfiere el ensayo privado al repositorio público.

**Puerta de promoción:** revisión del propietario de la interpretación de «sufrimiento» y de los límites de la distribución, CI real y revisión de genealogía apilada. No fusión automática.
