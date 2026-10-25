# Annex 01K-A02 — Human Intelligence Debt: aceleración económica y experimentos de segundo orden

**Status:** research note v0.1 · 25 October 2026 · *PROPOSED / NOT RUN* para la batería nueva. **Autoría conceptual:** Iván Abril Palma / The Integral Management Society. **Dominio propietario:** [01K — Human Capacity / Human Intelligence Debt](01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md). **Modelo económico receptor:** [ACC — núcleo técnico del modelo económico abierto](01I-artifacts/acc-auxiliary-model-v0.1/ECONOMIC_MODEL_TECHNICAL_CORE_v0.1.md).

**Alcance:** hipótesis, objeto económico, fórmulas, diseños de contraste, controles, criterios de falsación y agenda de instrumentación de la serie HID. No amplía el contrato operativo [01K-A01](01K_A01_HUMAN_CAPACITY_HID_COMPONENT_SPEC_v0.1.md), no adopta una ley económica, no añade un test congelado UC21/R01 ni acredita Stage B/C de DDS. «Human Intelligence Lab» puede designar el trabajo experimental; las definiciones y el contrato de medida continúan siendo **Human Intelligence Debt (HID) en 01K**.

## A. Qué se pretende averiguar

El modelo económico abierto distingue **producir más** de **estar más lejos de una alternativa técnicamente mejor hoy**. El problema de segundo orden pregunta algo adicional:

> ¿Puede la incorporación de capacidades productivas aproximadamente lineal causar, mediante interdependencias, mapas incompletos, asignación de crédito, reglas de retiro y costes de reajuste, un **crecimiento acelerado del trabajo humano compensatorio evitable por período**? ¿Cuándo detectan esa diferencia los controles, y puede corregirse sin perder servicio ni derechos?

Hay cuatro posibles resultados, todos legítimos:

1. Hay curvatura y un mecanismo específico la explica frente a alternativas competentes.
2. Hay curvatura, pero el mecanismo fue incorporado artificialmente en la topología o es explicable por un modelo rival.
3. Aumenta la carga o la exposición acumulada, **sin** aceleración del flujo.
4. La coordinación, interoperabilidad, retiro o el valor protector de los controles eliminan la deuda neta o la ventaja de la hipótesis.

La mera existencia de distancia económica G o de una fracción HID_observed>0 no responde a la pregunta dinámica.

## B. Separar familias: producción, brecha, obligación y capacidad humana

Para una población, servicio íntegro Y_t, frontera, tecnología, horizonte e información ex ante congelados:

| Símbolo | Objeto | Unidad / precaución |
|---|---|---|
| B_t | Valor productivo bruto incremental, antes de costes excluidos expresamente | Unidades de producto o utilidad declaradas; nunca llamar automáticamente bienestar |
| G_t | Brecha frente a una alternativa conjunta, válida en t | Unidad de utilidad o recursos; puede ser vector/rango |
| O_t, N_t, R_t | Obligaciones e interfaces vigentes, nuevas y retiradas | IDs únicos; O_(t+1)=O_t+N_t−R_t; no son deuda HID por sí |
| M_t | Coste de mantener/verificar O_t | Horas, dinero y riesgo con conversión explícita |
| H_ACW,t | Trabajo humano de compensación **verificadamente evitable** | Horas/episodios reales, con sustituto seguro y servicio equivalente |
| H_GIC,t, H_NEO,t, H_UNKNOWN,t | Contribución, oversight necesario, no clasificado | Taxonomía del 01K; no mezclar con ACW |
| d_t | Diferencia de trabajo compensatorio respecto de un contrafactual válido **por período** | Horas ACW evitables / período, comparables y deduplicadas |
| D_T | Exposición acumulada durante T períodos | Σ_t d_t Δt; si d_t se expresa como horas por período, Δt es un período unitario |
| d̂_t | Previsión registrada antes del período, con el mapa e información disponibles | Misma unidad de d_t; no acceso al oráculo futuro |
| e_t=d_t−d̂_t | Error de previsión | Descomponer en omisión de enlaces, probabilidad, retiro y coste, cuando sea identificable |
| ρ∞ | Fracción hipotética de capacidad liberada convertida realmente en GIC | Parámetro condicional de recuperación de 01K; no presumir su valor |

Las métricas fuente no se sustituyen:

~~~text
HID = HICT − HICR           (contrato conceptual original)
HICR_time = H_GIC/H_total
HID_observed = H_ACW/H_total
HICT = HICR + H_releasable/H_total
F-HICT = HICR + ρ∞·H_releasable/H_total
HID_spent = (1−ρ∞)·H_releasable/H_total
NOI = H_added − H_removed
~~~

Estas expresiones sólo se usan con denominador, evidencia y unidades compatibles. **d_t no es HID_observed**, ni O_t es HID. La eliminación de cinco horas ACW no demuestra cinco horas adicionales de contribución genuina, ni pérdida permanente de una habilidad.

Diferencias temporales:

~~~text
Δd_t = d_t − d_(t−1)
Δ²d_t = d_t − 2d_(t−1) + d_(t−2)
D_T = Σ d_t·Δt
e_t = d_t − d̂_t
~~~

Una D_T creciente sólo significa trabajo acumulado; una d_t creciente puede tener Δ²d_t=0; la curvatura Δ²E[d_t]>0 indica **aceleración de la carga en esperanza**, pero tampoco prueba causa ni pérdida de bienestar. Un efecto causal de segundo orden aparece cuando una decisión cambia conexiones, incentivos, reglas, información o capacidades que afectan el coste de decisiones siguientes; puede existir sin curvatura positiva.

## C. Familias de mecanismos que deben competir

**H0-L, carga lineal:** una capacidad entra por período, B_t=b·t, y E[d_t]=a+c·t. No hay curvatura sostenida en el flujo. Una carga total grande y persistente sigue siendo relevante, sin confirmar H1.

**H1-I, densificación e incompatibilidad:** cada incorporación aumenta el número de interacciones efectivas; incompatibilidades evitables persisten más tiempo del que el sistema las retira. Si la densidad crece y la pérdida por interacción no decrece suficientemente, Δ²E[d_t] puede ser positiva. Hay que medir enlaces reales; no inferirlos del número de aplicaciones.

**H2-F, mapa frente a flujo:** la representación decisoria registra menos enlaces que el flujo real. La predicción hecha *desde ese mapa* puede seguir siendo lineal mientras d_t se curva. Un pronosticador con inventario completo, mejor muestreo o revisión adaptativa puede eliminar el diferencial: fallo condicionado de observabilidad, no incapacidad universal de prever.

**H3-A, crédito y retiro:** una divergencia entre contribución real C_i y atribución formal A_i podría influir en incentivos, autoridad o financiación de retirar interfaces que una alternativa segura vuelve innecesarias. Hay explicaciones rivales: resiliencia, soporte, seguridad, regulación, conocimiento tácito o dependencia real. No atribuir mala fe ni equacionar toda recompensa con veto.

**H4-IF, retroacción informacional:** actuar sobre un mapa Mapa_t divergente de Flujo_t cambia el flujo y puede aumentar posteriormente las obligaciones o la insuficiencia del mapa. Es un feedback que debe aislarse del mero aumento exógeno de enlaces.

**H5-S, previsión, aceptación y retorno:** una condición de bienestar neto puede aprobar ΔŴ≥0 y observar después ΔW_real<0. Las reglas de revisión, nuevos titulares de derechos, costes hundidos y sustitutos determinan si puede revertirse. El límite se refiere a información disponible y gobernanza del escenario, no a que el bienestar deba gobernar universalmente.

**H6-H, capacidad y recuperación:** una mediación persistente puede desplazar práctica genuina y, quizá, reducir competencia autónoma o la capacidad de reconversión. Hay que medir habilidades, práctica, empleabilidad/uso efectivo y ρ separadamente. Desuso no equivale a atrofia demostrada; liberar trabajo puede generar ocio, cuidado u otros beneficios elegidos fuera de GIC.

**H7-C, economía del reajuste:** más propuestas locales favorables pueden requerir nuevas revisiones, transferencias presupuestarias o contratos. La pregunta no es sólo cuántas se rechazan, sino **cuántas pasan inmediatamente, cuántas después de reajuste y a qué coste**, frente a una coordinación convencional capaz. C_adj incluye verificación necesaria y gasto evitable; sólo la parte comparativamente evitable es candidata a ACW o pérdida recuperable.

Las series HID, Attribution Gap, Informational Friction, Cost of Clarity y el puente monetario son fuentes **conceptuales relacionadas del mismo programa**, no cinco replicaciones independientes.

## D. Primera construcción de posibilidad: mapas iguales, flujos distintos

**Procedencia:** anexo experimental v0.1 de [Notas completas del modelo ACC](01I-artifacts/acc-auxiliary-model-v0.1/model/01_NOTAS_COMPLETAS.md) (24-10-2026). Es un toy sintético; no representa datos reales de una organización.

Fijar t=1,…,20; incorporación de una capacidad por ciclo; B_t=10t; cada incompatibilidad persistente genera h=3 horas compensatorias por ciclo; probabilidad marginal p=0,20; mismo output final y una sustitución segura **supuestos** para la comparación.

| Brazo | Relaciones y mecanismo | Esperanza de carga por período | Para qué sirve |
|---|---|---|---|
| L, disperso | Una interacción nueva visible/ciclo | E[d_L,t]=0,6t | Control lineal |
| N, denso oculto | t relaciones nuevas/ciclo, sólo una visible | E[d_N,t]=0,3t(t+1) | Carga con curvatura; mismo mapa declarado que L |
| E, estándar | Topología densa, interoperabilidad p_t=0,20/t | E[d_E,t]=0,6t | Ablación de incompatibilidad sin reducir nodos |
| R, retiro | Densidad N, retiro de obligaciones antiguas r=0,15/ciclo | E[d_R,t]=0,85E[d_R,t−1]+0,6t | Ablación de persistencia |

En L y N se ve la misma secuencia declarada de una relación por capacidad y la misma producción. El **investigador/simulador** sí conoce la topología real N; el decisor con información restringida no. En un estudio empírico habrá que demostrar la equivalencia de información y que N no introduce recursos extra en secreto.

Consecuencias analíticas:

~~~text
E[Δ²d_L,t]=0
E[Δ²d_N,t]=0,6 horas por ciclo²
d̂_t = 0,6t        (pronóstico restringido al mapa)
E[e_N,t]=0,3t(t−1)
Σ_(t=1..20) E[d_N,t] = 924 horas de exposición
Σ_(t=1..20) d̂_t = 126 horas previstas
Divergencia acumulada esperada = 798 horas
~~~

En t20, el valor esperado es d_N=126 horas/ciclo, frente a 12 previstas. Con λ=1 unidad de utilidad por hora y sin otros costes, V_t=10t−0,3t(t+1), de modo que V_16=78,4 y V_20=74: producción +40, valor neto −4,4 entre esos puntos. La variación marginal en t20 es 10−0,6×20=−2, aunque el mapa local estima 10−0,6=+9,4. La desigualdad **resulta de los parámetros**; no es un dato social.

### Evidencia y procedencia (no confundir)

- Los manuscritos declaran **10.000 réplicas sintéticas xorshift32** y medias muestrales: N en t20 ≈126,06 horas/ciclo, R ≈58,12; alrededor de 58,6 % de márgenes marginales negativos al final. Sus registros originales y el código histórico **no están autenticados** en el PR.
- La [recreación analítica nueva](01I-artifacts/acc-auxiliary-model-v0.1/studies/synthetic-recreation-v0.1/README.md), con código y resultados propios, obtiene E[d_N,20]=126, E[d_R,20]≈58,211883, D_20=924 y probabilidad binomial de margen negativo ≈58,8551 %. No «reproduce» la ejecución histórica original; **recalcula las consecuencias de sus parámetros**.
- El [piloto económico determinista separado](01I-artifacts/acc-auxiliary-model-v0.1/studies/economic-pilot-v0.1/results/RESULTS.md) hizo 18 casos para otro subconjunto de preguntas: los dos procedimientos competentes empataron y existe un FAIL compartido. **No** es la ejecución de esta batería de aceleración.
- Un sistema real con interoperabilidad creciente, actualizaciones de mapa, alternativas caras o retirements correctos puede seguir L/E/R y neutralizar la aparente trampa; esa salida debe conservarse.

## E. Construcción distinta: Attribution Gap → derechos de retiro

En el toy de crédito se mantienen incorporación, topología, producto, incompatibilidad y riesgo constante. Cada obligación técnicamente retirable puede pertenecer a una fracción q_attr de atribución formal positiva pese a una contribución diferencial nula **bajo el contrafactual del toy**; el titular ejerce un bloqueo de retiro supuesto. Las demás obligaciones tienen hazard de retiro r=0,15 por ciclo:

~~~text
E[d_t | q_attr]
 = q_attr·0,3t(t+1) + (1−q_attr)·E[d_R,t]
E[d_R,t] = 0,85E[d_R,t−1] + 0,6t
~~~

En t20: q_attr=0 → ≈58,21 h/ciclo; q_attr=0,5 → ≈92,11; q_attr=0,8 → ≈112,44 **como expectativas analíticas**. Las notas históricas reportan otras medias muestrales cercanas de 10.000 réplicas, no autenticadas. q_attr **no es** la probabilidad q de aprobación por veto soberano de otros toys.

Esto prueba sólo que **una regla de bloqueo de retiro asumida produce la diferencia que se le atribuye matemáticamente**. No observa atribución real, no estima causalidad en empresas y no prueba que el reconocimiento ilegítimo sea la única razón de conservar arquitectura. Retirar algo puede ser imprudente aunque parezca redundante.

## F. Diseño propuesto de experimentos de segundo orden (NOT RUN)

Ningún ID siguiente amplía automáticamente los IDs de pruebas canónicas UC21, R01 o los de 01K-A01. Se pre-registra por estudio modelo, implementación, reloj, oráculo, fuente, recursos, semillas, criterio de evidencia y análisis de sensibilidad antes de correr.

| ID local | Intervención / comparadores competentes | Variable primaria y refutador |
|---|---|---|
| HID2-01 TOPO | Red estrella, modular y completa con mismo servicio y recursos; variante densa interoperable | E(n), ACW por episodio, Δ²E[d_t]; refuta H1 si la carga no se acelera o la red densa produce valor neto mayor |
| HID2-02 RETIRO | Mismo N,p,h; hazard 0 / 0,15 / retiro adaptativo seguro | d_t, D_T, valor protector y coste de sustitución; refuta persistencia necesaria si retiro corrige sin pérdida de servicio |
| HID2-03 MAPA | L/N con mismo mapa, mapa completo, auditoría bajo presupuesto, predictor topológico/adaptativo | Error e_t, falsas decisiones, tiempo/coste de información; refuta fallo inevitable si se distinguen mundos a tiempo |
| HID2-04 ATRIB | Crédito A_i y contribución C_i **medidos independientemente**; incentivos/control de retiro cruzados con dependencia legítima | Tasa de retiro seguro; refuta mecanismo atribucional si el diferencial desaparece tras controlar seguridad, regulación, necesidad y riesgo |
| HID2-05 BACK-ACTION | Política basada sólo en mapa vs verificación independiente vs robusta, mismas acciones legítimas | Divergencia mapa/flujo posterior, nuevas obligaciones, ACW; resultado nulo si feedback corrige a tiempo |
| HID2-06 SOBERANÍA | Condición W informativa/vinculante × mapa completo/parcial × revisión sí/no × rollback viable/caro | Falsas aprobaciones y denegaciones, utilidad preservada y pérdida no reversible; controles pueden evitar el fallo |
| HID2-07 CAPACIDAD | Igual flujo final con distintos historiales de mediación, retirada segura y recuperación/mentoría | Pruebas ciegas de competencia, GIC real, ACW, ρ; refuta atrofia si habilidades y conversión se recuperan |
| HID2-08 GRAVAMEN | Nuevos compromisos con IDs, reglas de retiro alternativas, mantenimiento por vínculo y coste de garantías | Relación N,R,O,M, producción y utilidad neta; refuta aceleración si hay economía de escala, valor protector o buen retiro |
| HID2-09 AJUSTE | Marketing/Sistemas/Finanzas con autoridad, presupuestos, compensación y arbitraje variables; planificador convencional fuerte | No-brainers locales/conjuntos, C_adj necesario/evitable, G recuperable y ACW; resultado contrario si FinOps habitual resuelve mejor |
| HID2-10 UC21-BRIDGE | Adaptador DDS aislado de acciones locales con PASS y efectos sistémicos posteriores; oráculo de fuente congelado | Separar resultado UC21 original de resultado social receptor; NULO si controles y coordinación competentes preservan ambos |

Los modelos analíticos, el piloto económico existente y los diseños de arriba tienen **estados diferentes**. HID2-01…10 siguen *NOT RUN* hasta que existan protocol/freeze, implementación, runs, trazas y revisión del oráculo. Un toy puede ejecutarse en una primera etapa de especificación; no se declara automáticamente un Stage C operativo.

### Diseño factorial mínimo antes de afirmar aceleración

1. Congelar servicios Y, calidad, tecnología, recursos, riesgo, derechos, población, horizonte y coste de integración **para todos los brazos**.
2. Medir n capacidades, E(n) conexiones **reales**, densidad, horas por interacción y obligaciones con identificadores. Separar crecimiento de capacidad productiva de densidad de dependencias.
3. Cruzar topología × p × retiro × q_attr × información × coste de reajuste. Los brazos de información comparten exactamente las observaciones admisibles cuando se declara indistinguibilidad.
4. Congelar predicciones y criterio de continuidad **antes** de observar efectos. Tener un procedimiento de coordinación convencional bien financiado con las mismas fuentes y facultades.
5. Introducir controles positivos (mejora legítima, continuidad con requisitos satisfechos) y negativos (sin exceso ACW, mapa bueno, retiro suficiente, sin veto real, protección necesaria).
6. Medir valor neto y resultados por actor, no sólo horas; contabilizar costes de interoperabilidad, mantenimiento del comparador y amortización del cambio.
7. Ejecutar sensibilidad de λ, b, c, h, p, correlación, densidad, horizonte y tasa de retiro. Mostrar zonas de ventaja, empate y pérdida y efectos de saturación.
8. Reportar UNKNOWN/NOT MEASURED y resultados adversos. No declarar aceleración social por haber simulado una parábola.

### Capa de medición humana 01K

Un estudio empresarial de HID exige primero la validación del instrumento (Study 0 de 01K/Paper 5): taxonomía GIC/NEO/ACW/UNKNOWN, muestreo, evaluadores independientes, acuerdo entre codificadores, trazas objetivas y auditoría de reemplazabilidad Tier 1–3. La propuesta fuente contempla aproximadamente 300 episodios, al menos tres evaluadores y α≥0,80 como umbral de la campaña; **no** afirmar que ese diseño se realizó aquí ni convertirlo en un estándar universal.

La capa experimental de mayor alcance requiere después: baseline y referencia comparables, intervención o retiro aleatorizable cuando sea legítimo, seguimiento histórico, medición de cambio de habilidad y tasa de recuperación ρ. No deducir pérdida de capacidades de HID_observed o de una lista de aplicaciones.

## G. Contabilidad y soberanía: el vínculo con el modelo económico

La pérdida de oportunidades y los costes de reajuste se clasifican una sola vez:

- G_vis: distancia respecto de alternativa visible y declarada.
- D_bruta: suma de propuestas frustradas **antes** de compatibilidad.
- G_recuperable: mejor paquete materialmente y jurídicamente factible, descontando costes pertinentes, **no** suma de rechazos.
- C_adj: costes reales de descubrir, verificar, negociar, contratar y ejecutar, divididos en necesarios y evitables mediante alternativa competente.
- d_t y HID: trabajo humano **específicamente compensatorio y evitable**, con contrato 01K; no todos los C_adj son HID.
- F: experiencia subjetiva, medida independientemente si la pregunta incluye bienestar. No se deduce de G ni se resta dos veces.

La regla soberana W como puerta económica constituye **un brazo opcional de prueba**, no una obligación jurídica ni un sustituto de control humano legítimo. Un control con información sólo local puede aprobar válidamente sus pruebas y, sin embargo, no observar un efecto posterior; un control de sistema suficientemente instrumentado puede resolverlo. La política puede abstenerse (HOLD/ASK), aprender, negociar o retirar compromisos, contando su coste real.

**Separación de UC21:** la evidencia social añadida nunca reetiqueta los PASS/FAIL congelados de sus escenarios ni sustituye sus comparadores; se documenta como **evaluación receptora** vía DDS y en otro ámbito de autoridad.

## H. Registro de evidencia y falsación

| Proposición | Estado al publicar A02 | Evidencia suficiente para avanzar |
|---|---|---|
| HID=HICT−HICR; GIC/NEO/ACW | Contrato conceptual/operacional heredado de 01K | Cumplimiento del método de medición; no por esta nota |
| E[d_N,t]=0,3t(t+1) bajo topología N | Derivación analítica condicional | Verificación de ecuación, código y parámetros |
| Historial de 10.000 réplicas del 24-10 | **Declarado en fuente; no autenticado** | Código original, hashes/salidas originales, seeds, comparaciones |
| Recreación paramétrica nueva | Disponible en PR de ACC, separada | Revisión y reproducción independiente del código actual |
| H1–H7 causales en organizaciones | **Sin contraste empírico** | Protocolos pre-registrados, intervención/ablación, medición independiente |
| Curvatura ⇒ efecto de segundo orden | **No se sigue** | Mecanismo identificado, cambios temporalmente encadenados y rivales refutados |
| Paper 4: atrofia, ρ∞<1, histéresis | Hipótesis abierta | Observación longitudinal y prueba independiente de capacidad |
| Compatibilidad con UC21/R01/DDS | Plan de acoplamiento | Adaptador versionado y aceptación en sus propias fuentes |
| Valor social neto positivo/negativo | No establecido globalmente | Servicio, derechos, utilidad, costes, preferencias y afectados medidos |

**Refutación fuerte:** una arquitectura equivalente y legítima muestra ACW no creciente tras controlar por enlaces y productividad; la curvatura desaparece al retirar obligaciones o mejorar interoperabilidad; un comparador bien informado predice correctamente; las relaciones preservadas producen un valor protector superior a su coste; la diferencia atribucional no se observa; o la pérdida neta desaparece bajo conversiones plausibles. No reinterpretar un resultado así como «dimensión invisible adicional» sin predicción nueva.

## I. Puentes, fuentes y próxima ejecución

- **Serie madre y requisitos de evidencia:** [01K](01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md), su [componente A01](01K_A01_HUMAN_CAPACITY_HID_COMPONENT_SPEC_v0.1.md) y el [estudio de medición de Human Intelligence Debt](https://tegrity.ai/meassuring-human-intelligence-debt/).
- **Desarrollo formal económico:** [ACC — núcleo técnico](01I-artifacts/acc-auxiliary-model-v0.1/ECONOMIC_MODEL_TECHNICAL_CORE_v0.1.md) y [Notas completas con anexos fuente](01I-artifacts/acc-auxiliary-model-v0.1/model/01_NOTAS_COMPLETAS.md).
- **Recreación y límites:** [estudio sintético analítico](01I-artifacts/acc-auxiliary-model-v0.1/studies/synthetic-recreation-v0.1/README.md) y [estado de las afirmaciones ACC](01I-artifacts/acc-auxiliary-model-v0.1/RESEARCH_STATUS.md).
- **Puentes intelectuales sin mezcla de métricas:** Human Intelligence Debt Papers 1–5, Attribution Gap, Informational Friction y Cost of Clarity, ya documentados en 01K §§8–10 y §§21–23. Para obligaciones monetarias, conservar la cautela del modelo: altas, retiros y mantenimiento constituyen el mecanismo, **no** el interés financiero como causa automática de crecimiento exponencial.
- **Antes del primer nuevo run:** protocolo HID2-01/02 con servicios comparables, oráculo y forecast sellados; tests analíticos; aprobación del plan de evidencias; ejecución en **una rama o paquete de estudio versionado propio**. La fase de investigación no requiere alterar 01K-A01, congelados UC21/R01 ni el contrato normativo de ACC.

**Decisión editorial:** esta nota es un anexo de investigación técnica de HID dentro de 01K. La reflexión de Magnifica Humanitas sobre elección, autonomía y solidaridad permanece en los libros de contexto originales; aquí sólo se trata la facultad de aceptación como condición económica/operacional cuando forma parte del escenario.
