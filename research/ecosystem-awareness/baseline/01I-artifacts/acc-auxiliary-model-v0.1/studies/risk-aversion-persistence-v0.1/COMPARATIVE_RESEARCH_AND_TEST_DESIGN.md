# RAV-01 — Investigación comparativa y programa de falsación

**26 de octubre de 2026 · complemento de investigación para el PR #46 · autor conceptual: Iván Abril Palma / The Integral Management Society.**

**Estado epistemológico:** contraste de literatura primaria y formulación de hipótesis; **no** resultado empírico propio, revisión sistemática exhaustiva, valoración clínica ni diagnóstico poblacional. Este documento añade alcance **explicativo y experimental** sin reabrir las definiciones normativas ni las ecuaciones de rendimiento, óptimos, HID o sufrimiento estructural del corpus.

## 1. Pregunta, contribución y definición de los objetos

La proposición a explorar no es solamente que alguien soporte una situación insatisfactoria. Es la **compatibilidad simultánea**, en una secuencia de crecimiento, de:

1. Mayor beneficio material B, y acaso mayor bienestar neto W, que en el pasado.
2. Mayor malestar vivido F y/o mayor **brecha económica individual de utilidad alcanzable no realizada** L; son mediciones distintas, y F puede aumentar no linealmente.
3. Pronóstico pesimista del propio régimen —la media futura de permanecer puede ser inferior al nivel realizado hoy—.
4. Una alternativa creíble de rediseño R con mayor resultado **medio** esperado, que no implica mayor equivalente cierto.
5. Elección de **permanecer pasivamente S** o incluso **invertir recursos en defender D** la continuidad de ese régimen; no basta observar que alguien declara estar de acuerdo con él.

En el esquema económico del ACC ya está la separación Gᵀ/Gᴳ, B, W, F, costes, opción y límites de factibilidad. La contribución **acotada** de RAV-01 es una regla explícita de decisión ante loterías conocidas, seguida de una tercera acción D; no se presenta como descubrimiento de que existe statu quo, sufrimiento, racionalidad limitada ni justificación social.

### Brecha de utilidad perdida, con frontera de identificación

Para la misma persona i, un horizonte y una escala de utilidad cardinal validada y estable en la comparación:

    L_i = max(0, u_i(s_i^cf) − u_i(s_i^real)),  si s_i^cf es conjunta y legítimamente factible.

El contrafactual debe mantener recursos, derechos, restricciones reales y no agregar máximos individuales incompatibles. Si no puede identificarse, **L=NOT_IDENTIFIED; no L=0**. Un salto atractivo pero inalcanzable puede ser una aspiración, no una pérdida económica factible. Transformaciones arbitrarias de la escala de utilidad invalidan comparaciones cardinales entre personas y entre periodos; hay que fijar normalización e instrumento. No sumar L a G: pueden representar el mismo episodio en unidades distintas.

Denominamos **«sufrimiento económico por utilidad no realizada»** a L **solo como convención operativa de este submodelo**. Es una oportunidad perdida desde preferencias del actor, **no una observación automática** de sufrimiento subjetivo. El F del ACC continúa exigiendo medición independiente. Es falsable que quienes reconocen una L mayor reporten, controladas las condiciones relevantes, un F mayor; también es posible no observar asociación o encontrar habituación, esperanza y agencia que la cambien.

El sufrimiento estructural del PR #43 tiene requisitos **conjuntivos propios**: potencial genuinamente bloqueado por una codependencia externa, intención de contribución positiva y componente de indeterminación relacional con misión/derechos preservados. **L, F, S_struct e HID no son sinónimos**. Un L positivo no satisface automáticamente los requisitos del PR #43; un F positivo tampoco. Si B o la utilidad observada ya descuentan F/L, no se vuelven a restar al calcular W.

## 2. Mecanismo con tres acciones y una preferencia estable

En un solo actor, numerario, horizonte y conjunto **caracterizado de riesgos**:

- **S:** continuar sin una intervención protectora adicional.
- **R:** rediseñar/salir; coste determinista de transición C, declarado fuera de la lotería.
- **D:** defender activamente la configuración actual —p. ej., dedicar tiempo, renta o acción colectiva a preservar una regla o amortiguar un riesgo—; coste propio k, contado una vez, y **una distribución de utilidad total defendida** (incluidos valores sociales/afectivos del propio actor cuando se justifiquen) que puede ser distinta de la de S aun con igual resultado **material**.

Bajo utilidad CARA y loterías normales, solo como testigo analítico:

    CE_S = μ_S − (γ/2)·σ²_S
    CE_R = μ_R − (γ/2)·σ²_R − C
    CE_D = μ_D − (γ/2)·σ²_D − k
    D se prefiere a S si (μ_D − μ_S) + (γ/2)·(σ²_S − σ²_D) > k.
    D se elige frente a ambas si CE_D > max(CE_S, CE_R).

γ puede ser idéntica entre periodos. Si D tiene la **misma distribución de utilidad total** que S (no solo los mismos ingresos) y k>0 no duplicado, queda dominada por S **en el submodelo completo declarado**. Si se defiende de todos modos, comprobar primero si faltan argumentos de utilidad personal —identidad, afecto, reconocimiento, cuidado, deber, creencias— o restricciones/derechos; solo tras esa auditoría considerar hipótesis rivales no reducidas. No identificar automáticamente una conducta con sesgo o irracionalidad. **Contracontrol:** mismo material N(14,4) y γ=0,5; D aporta +1 de satisfacción intrínseca no contada en S y cuesta 0,5. CE_D=13,5 > CE_S=13. No reduce el riesgo, **pero sí cambia la utilidad total**.

**Testigo posterior heredado de RAV-01:** γ=0,5; S=(14,4), CE_S=13; R=(25,64), CE_R=9. Añadir D=(14,1), k=0,5: CE_D=13,25. Aunque R ofrece once unidades más de **media**, D es la decisión del testigo. En otra escala/horizonte comparable y **sin inferencia causal**, B=(12,20,30), F=(2,6,13), W=(10,14,17). La persona declara un pronóstico para S de 14 cuando su W actual es 17 y una brecha de utilidad individual factible estipulada L=4. **Más medios, mayor F, peor pronóstico, utilidad no realizada y defensa activa coexisten como posibilidad lógica**, no como datos de españoles, latinoamericanos o de una generación. El k de D no debe aparecer ya dentro de μ_D.

Si se usa el ruido EV1 opcional, la probabilidad modelada de cada **elección** es el softmax de sus tres CE; la probabilidad de REDISEÑAR baja al ofrecer D en el conjunto de opciones y **no equivale** a probabilidad de éxito de R. Las probabilidades B/C/D de estados abiertos de ACC permanecen NOT_IDENTIFIED.

## 3. Comparación con literatura: coincidencias, diferencia comprobable, límite

| Trabajo primario | Lo que comparte con nuestra hipótesis | Diferencia / lo que **no** acredita |
|---|---|---|
| Samuelson y Zeckhauser (1988), sesgo de statu quo | Se observa preferencia por la situación vigente y distintas fuentes de inercia. | No basta atribuir la permanencia a sesgo si CE_S≥CE_R bajo riesgos bien caracterizados; nuestro testigo ofrece una **explicación de elección** y un control de riesgo neutral. Tampoco demuestra que todo sesgo sea económicamente racional. |
| Kahneman y Tversky (1979), teoría prospectiva | La referencia, pérdidas y ponderaciones pueden hacer persistir aun cuando el promedio favorece cambiar. | Nuestro cálculo CARA-normal de media-varianza **no** endogeniza los puntos de referencia, probabilidades ponderadas ni asimetrías de pérdidas. Un efecto de encuadre con medias/varianzas idénticas apoyaría explicaciones fuera de este testigo. |
| McDonald y Siegel (1986), valor de esperar | Esperar ante inversión irreversible e incertidumbre puede tener valor racional pese al retorno esperado. | El valor de opción requiere dinámica y derechos de espera definidos; nuestro S estático no computa valor de aprendizaje ni opciones reales. **Esperar** no equivale a **gastar para defender activamente** las restricciones. |
| Jost y Banaji (1994), justificación del sistema | Las personas pueden legitimar instituciones que contradicen sus intereses; la defensa del régimen es fenómeno reconocido. | No se deriva una **causa psicológica** de la ecuación CE. Pero un valor intrínseco por legitimidad/identidad puede representarse dentro de X_D y conservar el comparador. Las dos explicaciones pueden coincidir observacionalmente: se necesita identificación, no etiquetar la legitimación como N automática. |
| Staw (1976), escalada de compromiso | Los decisores continúan invirtiendo tras malos resultados, especialmente bajo responsabilidad previa. | La inversión hundida como tal **no** justifica D con coste y sin beneficio bajo maximización prospectiva; si intervienen reputación, autoconsistencia o costes de rendición de cuentas, deben medirse. |
| Luttmer (2005), ingreso relativo y bienestar | Mayor prosperidad contextual puede acompañarse de menor bienestar declarado por comparación social. | No identifica por sí sola una oportunidad propia factible L ni explica la decisión de permanecer o defender. Advierte que B y F pueden moverse en direcciones no triviales. |
| Genicot y Ray (2017), aspiraciones e inequidad | Aspiraciones y distancias a metas afectan conductas de inversión y desarrollo de forma no lineal. | Su brecha de aspiración no puede llamarse automáticamente utilidad accesible y no realizada; aquí exigimos factibilidad y separamos L reconocido, F reportado y CE de la transición. |
| Dalton, Ghosal y Mani (2016), fallo de aspiraciones | Restricciones y expectativas pueden reproducir un equilibrio de bajo desempeño. | Allí importa la falta de aspiración frente al potencial; nuestra hipótesis permite **reconocer explícitamente** la oportunidad y la frustración mientras se continúa/defiende por riesgo. No atribuir toda permanencia a aversión al riesgo. |

**Fuentes originales y DOI/autores**:

1. William Samuelson y Richard Zeckhauser, *Status Quo Bias in Decision Making* (1988), https://doi.org/10.1007/BF00055564 ; repositorio de autor: https://rzeckhauser.scholars.harvard.edu/publications/status-quo-bias-decision-making
2. Daniel Kahneman y Amos Tversky, *Prospect Theory: An Analysis of Decision under Risk* (1979), Econometrica 47(2), 263–291; texto: https://msuweb.montclair.edu/~lebelp/KTverskyProspectTheorEc1979.pdf
3. Robert McDonald y Daniel Siegel, *The Value of Waiting to Invest* (1986), Quarterly Journal of Economics, https://doi.org/10.2307/1884175
4. John T. Jost y Mahzarin R. Banaji, *The role of stereotyping in system-justification and the production of false consciousness* (1994), https://doi.org/10.1111/j.2044-8309.1994.tb01008.x ; original: https://banaji.sites.fas.harvard.edu/research/publications/articles/1994_Jost_BJSP.pdf
5. Barry M. Staw, *Knee-Deep in the Big Muddy: A Study of Escalating Commitment to a Chosen Course of Action* (1976), https://doi.org/10.1016/0030-5073(76)90005-2
6. Erzo F. P. Luttmer, *Neighbors as Negatives: Relative Earnings and Well-Being* (2005), https://doi.org/10.1093/qje/120.3.963 ; versión de trabajo del autor: https://www.nber.org/papers/w10667
7. Garance Genicot y Debraj Ray, *Aspirations and Inequality* (2017), Econometrica, texto de trabajo de los autores: https://www.nber.org/system/files/working_papers/w19976/w19976.pdf
8. Patricio S. Dalton, Sayantan Ghosal y Anandi Mani, *Poverty and Aspirations Failure* (2016), https://doi.org/10.1111/ecoj.12210 ; versión autor: https://eprints.gla.ac.uk/96273/

**Balance de originalidad:** la concurrencia de crecimiento, insatisfacción e inercia, y la justificación activa del statu quo tienen antecedentes sólidos. La contribución *candidata* es **juntarlos de manera identificable y refutable**: L factible separado de F, premio por riesgo diferencial a γ fija, comparación simultánea de S/R/D y controles donde esa explicación económica deja de funcionar. No se declara prioridad sobre toda la literatura ni validación experimental antes de ejecutar los ensayos.

## 4. Predicciones expresas y fronteras

| Predicción **condicionada** de RAV-01 | Qué no predice / observación adversa |
|---|---|
| Dado Δμ>0 y γ>0, aumentar la varianza **excedente** de R reduce ΔCE_R-S; puede reducir Pr(R) sin elevar γ. | No predice que crecer B cause necesariamente mayor varianza, ni que el resultado exterior abierto tenga distribución normal. |
| Un F creciente puede coexistir con W creciente cuando ΔB>ΔF en cada tramo, y también con un pronóstico futuro negativo. | No predice que F sea exactamente L ni que perder utilidad produzca siempre malestar consciente o reporte honesto. |
| L>0 reconocido y factible **no fuerza** elegir R cuando su CE es menor. | No equivale a Gᵀ/Gᴳ social ni satisface por sí solo los requisitos de sufrimiento estructural del PR #43. |
| Con D que reduzca suficiente σ² de quedarse **o aporte utilidad total identificada** (p. ej. cuidado valorado), CE_D puede superar S y R pese a F>0. | Si D no cambia la **utilidad total** ni riesgo, creencias ni factibilidad y k>0, CE_D<CE_S. Solo entonces el submodelo especificado es insuficiente. |
| γ=0 y Δμ>C, o igualar varianzas manteniendo Δμ>C, debería inclinarse hacia R si D no aporta un beneficio propio equivalente. | Sesgo de referencia, costos desconocidos, aversión a pérdida, estatus, familia, empleo, información o restricciones pueden invalidar esa inferencia empírica. |
| En un logit/softmax postulado, los cambios de CE se reflejan en cuotas de elección dentro del conjunto de acciones definido. | No son probabilidad de éxito, autorización o legitimidad; introducir D cambia el denominador de S/R. |

**Resultado adverso clave:** si, en elección real o incentivada, D se elige sistemáticamente cuando se verifica **igual distribución de utilidad total del actor** que S (incluidos valores afectivos, morales o de reputación), mayor coste k, alternativas igualmente admisibles y creencias correctamente identificadas, **el submodelo CARA-normal correctamente especificado no basta**. Eso no refuta que D exista: discrimina su posible fuente causal y exige modelos rivales. De igual modo, un aumento subjetivo de F a L constante refuta la ecuación ingenua F=L, que aquí **no** se impone.

## 5. Diseño de prueba pre-registrable

**Unidad:** individuo y decisiones voluntarias, horizonte fijo; no usar una muestra de migrantes o personas vulnerables como si fuese prueba de un comportamiento nacional. No manipular vida, renta, derechos ni traslados reales; estudios de decisiones incentivadas y/o viñetas, con consentimiento.

**Ensayo factorial central (2×2×2) sobre loterías calculadas y comprensibles:**

1. **Brecha de utilidad reconocida y factible L:** baja/alta, tras explicar y verificar comprensión de recurso y referencia. Medir por separado aspiración no factible y F reportado; si solo se varían aspiraciones, no etiquetar L como identificada.
2. **Riesgo diferencial de rediseño:** Var(R)−Var(S) bajo/alto, manteniendo constantes sus medias y γ medido/estratificado; variar también creencias sobre el riesgo para identificar expectativas subjetivas.
3. **Defensa activa disponible:** D reduce realmente —o no reduce— la dispersión/resultados para el actor, con coste k transparente. Control placebo de D sin beneficio.

Registrar antes de elegir expectativas, γ aproximada por tareas de lotería, κ solo si se estima elección estocástica, preferencias declaradas y comprensión. Resultados: elección S/R/D, esfuerzo invertido en D, CE predicho bajo preferencias medidas, F reportado, L identificada, percepción de legitimidad, sentido de agencia y creencia sobre la distribución. Analizar interacciones L×riesgo y riesgo×protección, no solo un promedio agregado.

**Extensión longitudinal (si procede):** múltiples olas que observen B, F, utilidad/aspiraciones, alcance real de alternativas, cambios de μ/σ² subjetivos y objetivos, decisión de transición y defensa. Estimar selección, restricciones migratorias o laborales, vínculos y oportunidades reales. **No** inferir la dirección de una causalidad solo porque B y F crezcan conjuntamente; pre-registrar hipótesis frente a comparadores sin defensa y frente a utilidad dependiente de referencia.

**Falsadores concretos para este mecanismo:**

- Manteniendo distribuciones y costes conocidos, γ medida cercana a cero y R de mayor media elegible, persiste D aun sin beneficio: el mecanismo de riesgo puro falla.
- Si los gastos de defensa no mejoran seguridad/ingresos pero D se elige, **intentar primero la reducción** de afecto, identidad, cuidado, aprobación, sentido del deber y creencias a utilidad total; solo la persistencia tras ese control discrimina otros mecanismos.
- Si no existe contrafactual conjunta y legítimamente factible, la **brecha de utilidad perdida** queda NO IDENTIFICADA; no se reemplaza por deseo o máximo imaginado.
- Si los instrumentos de F no muestran la asociación pre-registrada con L, rechazar esa vinculación empírica sin borrar los valores de L.
- Si una opción R domina en CE y derechos bajo el conjunto caracterizado, la resistencia no se atribuye automáticamente a CARA; revisar especificación de valores no monetarios o hipótesis rival.

**Auditoría metodológica añadida:** el [programa de extensiones e isomorfismo relativo](EXTENSION_ISOMORPHIC_NONISOMORPHIC_RESEARCH_v0.1.md) documenta primero una escalera U0–U6 de reducción a utilidad, pruebas de preservación del comparador, diferencias frente a una equivalencia operacional DDS y testigos relativos de proyecciones insuficientes. Becker (1974), Akerlof y Kranton (2000), Fehr y Schmidt (1999), Andreoni (1990) y Manski (1993) aportan teorías originales que impiden presentar cuidado, identidad o efectos sociales como necesariamente exteriores a la economía. Los DOI y sus límites están registrados en ese documento; aquí conservamos la comparación original de ocho trabajos.

## 6. Trazabilidad y lo que queda fuera del PR

- **#42:** regímenes de producción, óptimo, brechas y no monotonía; no redefinidos.
- **#43:** condición propia y conjuntiva de sufrimiento estructural en composición anidada; no sustituida por L ni por F.
- **#44:** información, cierre parcial y límites de conocer ex ante; no se inventan probabilidades del exterior.
- **#45:** metacognición y solidaridad; no se prueban ni prescriben por maximizar CE.
- **#46 / RAV-01:** una capa económica/comportamental condicionada con S, R y **D** y comparadores falsables.

Es **normativamente inadmisible** inferir que la elección de permanecer o defender legitima imponer cargas a hijos, migrantes u otros actores, o que la defensa es socialmente eficiente. La voluntad humana, titularidad, externalidades, derechos y distribución intergeneracional requieren evaluación separada. El ejemplo del parque infantil financiado para quien aún no lo puede usar es una ilustración crítica en el escrito privado; no constituye aquí dato sobre gobiernos, corrosión o deuda.

**Documentos ejecutables:** [README](README.md), [implementación](risk_model.py), [pruebas deterministas](test_risk_model.py) y [resultados sintéticos declarados](REFERENCE_SYNTHETIC_RESULTS.json). Mantener el PR abierto en borrador hasta revisión y CI.

**Propuestas de extensibilidad investigable:** [RAV-01-EXT: kernel isomórfico, deltas no isomórficos, validación social, vínculos y agentes](EXTENSION_ISOMORPHIC_NONISOMORPHIC_RESEARCH_v0.1.md). El anexo clasifica correspondencias y diseña pruebas futuras; no modifica ni ejecuta el testigo de este documento.
