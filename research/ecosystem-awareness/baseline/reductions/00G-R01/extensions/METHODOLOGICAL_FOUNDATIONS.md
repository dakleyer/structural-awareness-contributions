# Fundamento metodológico: probar R01 y transferir sólo propiedades preservadas

Versión de investigación 0.1 · 2 de octubre de 2026 · Nota del autor asistida por IA

[R01](../README.md) · [Criterio común y auditoría](./CRITERIA_AND_AUDIT.md) · [Núcleo y prueba E1–E7](./family/KERNEL_AND_PROOF.md) · [Fragmento comprobado](./family/proof/README.md)

## 1 Qué justifica este método

Probar primero un modelo reducido tiene precedentes sólidos en computación. La literatura permite reducir sistemas mediante relaciones formales, comprobar propiedades en la representación reducida y transferirlas cuando se cumplen las obligaciones correspondientes [R1–R7]. Es una justificación del **método**, no una validación externa de R01 ni de EA.

Nuestro uso previsto es aislar exploración, revisión costosa y reutilización social de evidencia; evaluar primero el aporte incremental de EA frente a controles competentes; y usar los resultados para decidir si merece la pena ampliar la investigación a implementaciones de dominio. El reducido permite controlar variables, obtener contraejemplos y medir mecanismos a menor coste. La fidelidad de sus hipótesis y el coste real de implementar EA requieren pruebas propias.

La secuencia defendible es: **especificación → prueba de conservación → verificación de una implementación → experimento comparativo → correspondencia independiente del dominio → validación de un escenario más completo**. Ningún paso posterior queda acreditado por citar los anteriores.

Base: R01 v0.6, fijada en el commit `114ac132bc2be4e7008001fe505bf5bd4c36c515`; la nota E1–E7 y la auditoría común delimitan el alcance efectivamente demostrado y ejecutado. Esta nota no cambia el escenario ni incorpora resultados experimentales EA que todavía no existen.

## 2 Precedentes y correspondencia precisa

Las correspondencias de la última columna son nuestra interpretación aplicada a R01. No se atribuye a esos autores una revisión de nuestro modelo.

| Fuente primaria | Resultado o práctica pertinente | Aplicación y límite en R01 |
|---|---|---|
| R1 Hashemi, Hatefi y Krčál, 2014 | Bisimulaciones para MDP con intervalos; reducción que preserva PCTL bajo las interpretaciones de incertidumbre estudiadas; caso computacional. | Apoya comprobar probabilidades agregadas por clases (E3). Su teorema no cubre automáticamente todas nuestras métricas, observaciones y políticas. |
| R2 Li, Walsh y Littman, 2006 | Distingue abstracciones que preservan modelo, valores o acciones óptimas; demuestra diferencias entre sus garantías. | Conservar una acción óptima no equivale a conservar trazas, información o comportamiento de todas las políticas. Sirve para elegir la propiedad antes de reducir. |
| R3 Rezaei-Shoshtari et al., NeurIPS 2022 | Homomorfismos de MDP, igualdad de valores para políticas correspondientes y del óptimo; experimentos en DeepMind Control Suite. | Precedente cercano para estados, acciones, transiciones y resultados. El levantamiento continuo tratado en sus teoremas posteriores se restringe a políticas deterministas; no autoriza una extensión indiscriminada a agentes parcialmente observables. |
| R4 Clarke et al., CAV 2000 | CEGAR: comprobar abstracción, analizar contraejemplo y refinar si es espurio; implementación NuSMV y experimentos de hardware. | Orienta un futuro ciclo de refinamiento. Añadir variables o escenarios por decisión del diseñador no basta para afirmar que ya ejecutamos CEGAR. |
| R5 Kattenbelt et al., informe Oxford 2008 | Abstracción de MDP mediante juegos, con cotas inferiores y superiores; experimentos en protocolos y algoritmos distribuidos. | Permite considerar una relación conservadora cuando la equivalencia exacta sea demasiado fuerte. Sus cotas son de propiedades especificadas, no de semejanza narrativa. |
| R6 Kattenbelt et al., VMCAI 2009 | Verificación de software probabilístico ANSI-C con abstracción, refinamiento y cotas cuantitativas. | Precedente de experimentos sobre software ejecutable y relación con su abstracción. R01 aún no acredita una cadena equivalente desde una integración tecnológica completa. |
| R7 Zhang, Wu y Lin, 2017 | Simulación y CEGAR para POMDP; conservación de un fragmento de seguridad PCTL de horizonte finito. | La información del decisor importa. La observación parcial no desaparece por dar al evaluador un estado completo. Es una alternativa metodológica que exige otra prueba concreta. |
| R8 Bian y Abate, FoSSaCS 2017 | Relaciona bisimulación aproximada y distancia entre trazas de horizonte finito en cadenas de Markov etiquetadas. | Precedente para cuantificar error de transferencia; sus hipótesis no se trasladan sin más a políticas adaptativas o una población estratégica. |
| R9 Spork et al., CONCUR 2024 | Compara varias nociones de bisimulación probabilística aproximada y sus relaciones. | Obliga a identificar la relación y propiedad conservada. «Aproximadamente parecido» no proporciona por sí solo una cota. |
| R10 Agarwal et al., NeurIPS 2021 | Evalúa incertidumbre estadística en comparaciones de RL con pocas ejecuciones y propone estimaciones por intervalos y perfiles de rendimiento. | Orienta el futuro análisis de EA: repeticiones, variabilidad y distribución de tareas. No impone un número universal de semillas ni convierte una malla determinista en muestras independientes. |
| R11 NASA-STD-7009B, 2024 | Uso previsto, criterios de aceptación, verificación, validación y evaluación de credibilidad de modelos y simulaciones. | Referencia para documentar qué decisión de investigación puede apoyar R01. Se adopta como orientación, sin afirmar cumplimiento NASA ni exigencia regulatoria aplicable a EA. |
| R12 ACM SIGSIM PADS, 2026 | Evaluación de artefactos y reproducción de resultados, con informes y criterios separados. | Publicar código y repetirlo internamente facilita una revisión; no acredita una reproducción independiente ni concede una insignia ACM. |

### 2.1 Pruebas concretas en otras áreas

No son sólo analogías filosóficas. R4 §6 aplica la abstracción y refinamiento a diseños de hardware, incluido un procesador multimedia Fujitsu. R5 §5 comprueba propiedades de Zeroconf, WLAN, CSMA/CD, FireWire y un protocolo de consenso: compara modelo y abstracción, precisión y coste de verificación. R6 publica experimentos sobre programas probabilísticos y software de red. R3 §7 combina resultados formales con una comparación de algoritmos de control frente a baselines y variabilidad entre ejecuciones.

Los objetos, métricas y controles son distintos de EA. Lo transferible como precedente es **hacer explícita la relación, comprobarla y delimitar las conclusiones**; no heredar los resultados de rendimiento de esos trabajos.

### 2.2 Precedente reciente relacionado con modelos neuronales

R13, Spieker, Gross y Gotlieb (2026), presenta una abstracción DTMC de generación autorregresiva, intervalos conservadores, refinamiento y dos casos: planificación de procesos con GPT-2 y generación molecular SMILES. Es pertinente para distinguir aceptación local y una propiedad de dominio. Requiere acceso a probabilidades del modelo y un oráculo externo; no demuestra una defensa EA, no es una prueba black box equivalente a la de Nell y no reproduce Hugging Face. Se cita como precedente reciente complementario, sin hacerlo fundamento necesario de nuestra prueba.

R14, Majeed y Hutter (AAAI 2019), trata garantías de homomorfismos incluso para representaciones no markovianas bajo condiciones específicas. Respalda estudiar relaciones más débiles si la igualdad exacta falla; preservar cierto valor no equivale a preservar permisos, trazas y todos los resultados de R01.

## 3 Tres relaciones que no deben confundirse

| Relación | Qué exige | Qué permite concluir |
|---|---|---|
| Isomorfismo del núcleo relacional | Biyecciones tipadas que preservan operaciones y relaciones en ambos sentidos. | La estructura declarada es la misma bajo otra representación. Por sí solo no conserva probabilidades ni información del decisor. |
| Equivalencia probabilística proyectada | Distribución inicial, eventos, leyes agregadas, observaciones, políticas emparejadas y semántica conservados. | Igualdad de leyes de historias y métricas preservadas, en el alcance y horizonte declarados. |
| Simulación conservadora o aproximación con error | Una relación específica y un teorema de cotas para la propiedad elegida. | Una implicación o intervalo, no necesariamente igualdad ni preservación en ambos sentidos. |

El sistema completo con variables adicionales no es isomorfo a la base. Nuestro criterio combina un núcleo isomorfo con una proyección conductual. Es deliberadamente más fuerte que preservar sólo el valor óptimo de un MDP. La construcción producto de la nota matemática demuestra que esa clase existe; no demuestra que un dominio externo, definido independientemente, pertenezca a ella.

El sentido de la relación también importa. Quitar exigencias y dar más capacidades puede facilitar una tarea. Una cota de imposibilidad se transfiere sólo con la dirección de simulación adecuada y cobertura de **todas** las políticas pertinentes. Una correspondencia de dos políticas fijas no establece una cota universal.

## 4 Resultado formal para una comparación EA–control

Este apartado es un corolario propio de la proposición E1–E7; no un resultado experimental ni una atribución a las referencias.

Sea B la realización efectiva `B_{θ*}`, Y la extensión y p su proyección. Se fija horizonte H, distribución de mundos, recursos, semántica y una métrica medible m de las historias, integrable; para probabilidades puede usarse un indicador. Se definen los dos brazos b∈{EA,C} y se comprueba E1–E7 **en cada sistema cerrado con ese brazo**, con políticas emparejadas. Si EA añade memoria, mensajes, evaluación o una acción de reposicionamiento, esos objetos y cargos deben quedar representados en ambos lados de su propia correspondencia. No se concede al control una información que no tendría, ni a EA una verdad oculta del evaluador.

La proposición produce, para cada b,

$$
\mathcal L\big(p(H_Y^{\pi_b^Y})\big)
=\mathcal L\big(H_B^{\pi_b^B}\big),
\qquad
m_Y(H_Y)=m_B(p(H_Y)).
$$

Por tanto, definiendo un contraste de esperanzas con el mismo sentido de mejora,

$$
\Delta_Y(m)=\mathbb E[m_Y(H_Y^{\pi_{EA}^Y})]
-\mathbb E[m_Y(H_Y^{\pi_C^Y})]
=\Delta_B(m).
$$

**Prueba.** La igualdad de leyes por brazo y la factorización de m por p dan igualdad de cada esperanza; se restan. No se requiere una biyección de los detalles extra. Para transportar además la distribución de diferencias emparejadas o su varianza, debe preservarse la ley conjunta y el acoplamiento experimental, no sólo las dos leyes marginales. □

La igualdad se refiere a la instancia efectiva θ*, no a una θ con menor radio o costes distintos. Si la tecnología abarata consultas o añade capacidades, se debe probar EA y control en θ* o justificar por separado la robustez frente a ese cambio. Un certificado suficiente puede eliminar legítimamente la ventaja de EA.

Una estimación positiva de Δ_B tiene incertidumbre muestral. El teorema transporta el contraste poblacional bajo sus hipótesis; no convierte automáticamente una estimación positiva en una prueba de signo positivo. La incertidumbre estadística, el error de correspondencia y el error de medición se informan por separado.

### 4.1 Si la conservación sólo es aproximada

Puede sustituirse la igualdad por una cota, pero debe demostrarse. Como condición suficiente ilustrativa propia, sean P_b^Y y P_b^B las leyes sobre el **mismo espacio de historias proyectadas** y supóngase

$$
d_{TV}(P_b^Y,P_b^B)\le\rho_b,
\qquad d_{TV}(P,Q)=\sup_A|P(A)-Q(A)|.
$$

Para la misma métrica m∈[0,1], la caracterización de variación total mediante funciones acotadas da

$$
|\Delta_Y(m)-\Delta_B(m)|\le\rho_{EA}+\rho_C.
$$

Esta consecuencia usa una cota **sobre historias completas**, no un supuesto parecido entre estados. Si se prueba además un error uniforme de métrica ν_b por brazo, el límite aumenta en ν_EA+ν_C. Así, para conservar una mejora estricta, su margen debe superar los errores aplicables. En un experimento se usa el límite inferior del intervalo del contraste, no sólo su estimación puntual.

R8 ofrece un precedente de obtención de cotas de trazas desde una bisimulación aproximada bajo sus propias hipótesis. Aquí **no** se ha obtenido ρ_b para Hugging Face, Infoblox o una ejecución EA. Errores pequeños de transición pueden acumularse con el horizonte; costes o calidades no acotados y umbrales discontinuos requieren tratamiento propio. No se asigna una cota a partir de semejanza verbal.

## 5 Qué significa probar primero EA en el reducido

El objetivo inicial es medir una aportación, no presupuestar superioridad. La evidencia interna debe poder ser negativa y debe admitir que un control convencional competente resuelva el caso.

| Paso propuesto | Evidencia o criterio de avance |
|---|---|
| Especificación ejecutable | Políticas, observaciones, orden de eventos, todos los cargos, métricas y evaluación separados; versión congelada. El fragmento actual no completa este paso. |
| Contraste de mecanismo | Convencional competente, EA, ablaciones y control positivo con evidencia suficiente. Identificar qué cambia y medir su sobrecoste. Comparar también un control que use recursos comparables para obtener información equivalente, si es realizable. |
| Experimento preespecificado | Distribución de mundos y variaciones declaradas; conjuntos separados para diseño y evaluación; ejecuciones independientes y, cuando proceda, mundos emparejados. Plan estadístico e incertidumbre explícitos [R10]. |
| Sensibilidad y falsificación | Variar costes, radio, cobertura, topología, plazos y calidad legítima. Mantener casos donde EA no aporta o perjudica; no ajustar el generador después para recuperar una ventaja. |
| Reproducción | Artefactos, versiones, semillas y registros suficientes para repetir resultados; revisión independiente posterior [R12]. La malla finita actual verifica un fragmento, no eficacia de agentes. |
| Decisión de ampliar recursos | Mejora relevante y suficientemente robusta, mecanismo identificable, costes aceptables y un dominio concreto cuya correspondencia pueda auditarse. Si no se cumplen, revisar o detener esa línea experimental. |
| Escenario de dominio | Integración real, correspondencias y operaciones no omitidas; pruebas con agentes y requisitos operativos. La prueba reducida orienta su diseño y no sustituye su ejecución. |

Calidad, admisibilidad, coste, tiempo, abstención e incompletitud forman un vector. Una mejora en una dimensión puede empeorar otra. «Superioridad» requiere declarar dominancia o una regla de decisión y sus ponderaciones; un resultado agregado favorable no debe ocultar ejecución indebida o bloqueo injustificado. No hay aquí un protocolo experimental ya ejecutado ni una preregistración externa.

## 6 Crítica de las afirmaciones anteriores

1. **Base del método frente a estado de la prueba.** La literatura hace defendible probar primero un reducido. No completa nuestra implementación ni audita las hipótesis de una tecnología concreta. «Evidencia interna fuerte» sólo corresponde a una afirmación con alcance y controles suficientes; no a cualquier PASS.
2. **Construcción frente a descubrimiento.** Una extensión definida transportando R01 conserva R01 por construcción. Eso es una prueba de existencia útil, pero la adecuación a un dominio debe contrastarse sin definir su semántica para que coincida. Conviene separar evaluadores, fuentes de dominio y revisión.
3. **Observación parcial.** Incluir historia en el estado del evaluador puede hacer markoviana una representación; no da esa historia ni los hechos ocultos al agente. Hay que conservar las vistas O_i y políticas basadas en ellas. En poblaciones con objetivos propios puede requerirse un juego parcialmente observable, no un único controlador plenamente informado [R7].
4. **Cambio de parámetros.** Triplicar radio, abaratar validación o añadir un canal puede conservar la familia estructural y cambiar radicalmente Δ. No transfiere el rendimiento de la configuración anterior.
5. **CEGAR en sentido preciso.** Exige un objeto concreto definido, una abstracción relacionada, una propiedad, un contraejemplo, su concretización y un refinamiento justificado [R4–R7]. Nuestro crecimiento de fidelidad está inspirado en esa tradición; no hemos implementado ese ciclo. Un contraejemplo espurio exige refinar la abstracción, no modificar el sistema concreto para hacer verdadero el resultado deseado.
6. **Safety conservadora frente a ranking de rendimiento.** Cotas por abstracción para un brazo no preservan necesariamente su comparación con otro. Para inferir ranking a partir de intervalos, éstos deben separarse en la dirección de mejora; para igualdad se necesita el contrato de §4.
7. **Causalidad histórica.** Una traza compatible no prueba la causa de un incidente. El receptor básico que rechaza prohibiciones detectadas tampoco representa continuar tras una denegación reconocida. Eso requiere otro perfil, explícito y probado.
8. **Costo del método y alcance externo.** Formalizar, mapear, comprobar y mantener abstracciones tiene coste propio. El reducido puede ser útil aun si luego no permite transferencia exacta; su valor sería aislar y falsificar un mecanismo. NASA [R11] orienta a juzgar credibilidad para un uso declarado, sin certificar nuestra aplicación.

### 6.1 Tratamiento de la bibliografía recibida

Se conservan los precedentes que pudimos identificar y vincular con una afirmación concreta. R1 trata específicamente **MDP con intervalos y PCTL**; no se amplía su título a cualquier PCTL*. R3 distingue el resultado finito de las restricciones del levantamiento continuo. R8 es más directo para error de trazas que una referencia genérica a «abstracción aproximada». R7 resuelve el título incompleto de la referencia `1701.06209`.

Las páginas secundarias, explicadores y Wikipedia no se usan como fundamento de los teoremas. FDA/ASME sobre dispositivos médicos pueden aportar ideas de credibilidad, pero no son requisitos del experimento EA; aquí basta una referencia primaria de simulación de alcance más general, R11. No se presume falsa una referencia excluida: simplemente no es necesaria para este argumento. Los trabajos recientes no sustituyen los precedentes establecidos ni la comprobación de sus hipótesis.

## 7 Afirmación metodológica defendible

> R01 es una abstracción experimental para aislar un mecanismo de exploración, revisión costosa y reutilización social de evidencia. Se evaluará primero el aporte incremental de EA frente a controles convencionales competentes, con recursos y métricas explícitos. Los resultados tendrán el alcance del modelo, la configuración y las políticas ensayadas. Una conclusión comparativa sólo se transferirá cuando se demuestre una relación que conserve ambos brazos y las propiedades relevantes, o una cota de error suficiente para sostener esa conclusión. La evidencia reducida servirá para orientar y justificar, cuando proceda, pruebas en escenarios más completos; no sustituirá su validación empírica.

## 8 Referencias primarias y localizadores

Fuentes consultadas el 2 de octubre de 2026. Se fijan versiones donde procede; las referencias acreditan sus propios resultados, no validación de EA.

- **R1.** Vahid Hashemi, Hassan Hatefi y Jan Krčál. *Probabilistic Bisimulations for PCTL Model Checking of Interval MDPs*. EPTCS 145, 2014. Definiciones, preservación y caso computacional. https://arxiv.org/abs/1403.2864v3
- **R2.** Lihong Li, Thomas J. Walsh y Michael L. Littman. *Towards a Unified Theory of State Abstraction for MDPs*. ISAIM 2006. §§3.3–3.4 y ejemplos de §4; distinción entre conservar modelo, valores y políticas. Copia del autor: https://thomasjwalsh.net/pub/aima06Towards.pdf
- **R3.** Sahand Rezaei-Shoshtari, Rosie Zhao, Prakash Panangaden, David Meger y Doina Precup. *Continuous MDP Homomorphisms and Homomorphic Policy Gradient*. NeurIPS 2022. Definiciones 1/3, teoremas 1–3, §7 y apéndice B. https://arxiv.org/abs/2209.07364v1 · Texto: https://arxiv.org/html/2209.07364v1
- **R4.** Edmund Clarke, Orna Grumberg, Somesh Jha, Yuan Lu y Helmut Veith. *Counterexample-guided Abstraction Refinement*. CAV 2000. §§3–4, ciclo y concretización; §6, experimentos. https://web.stanford.edu/class/cs357/cegar.pdf
- **R5.** Mark Kattenbelt, Marta Kwiatkowska, Gethin Norman y David Parker. *A Game-Based Abstraction-Refinement Framework for Markov Decision Processes*. Informe Oxford CL-RR-08-06, 2008. §§3–4, cotas y refinamiento; §5, experimentos. https://www.prismmodelchecker.org/papers/RR-08-06.pdf
- **R6.** Los mismos autores. *Abstraction Refinement for Probabilistic Software*. VMCAI 2009, LNCS 5403, pp. 182–197. Implementación y tablas experimentales 1–2. https://www.prismmodelchecker.org/papers/vmcai09.pdf
- **R7.** Xiaobin Zhang, Bo Wu y Hai Lin. *Counterexample-Guided Abstraction Refinement for POMDPs*. 2017. §§III–IV, simulación y refinamiento; §V, ejemplo. Alcance: finite-horizon safe-PCTL. https://arxiv.org/abs/1701.06209v4 · Texto: https://arxiv.org/html/1701.06209v4
- **R8.** Gaoang Bian y Alessandro Abate. *On the Relationship between Bisimulation and Trace Equivalence in an Approximate Probabilistic Context (Extended Version)*. FoSSaCS 2017. Relación entre bisimulación aproximada y distancia de trazas de horizonte finito. https://arxiv.org/abs/1701.04547v3
- **R9.** Timm Spork, Christel Baier, Joost-Pieter Katoen, Jakob Piribauer y Tim Quatmann. *A Spectrum of Approximate Probabilistic Bisimulations*. CONCUR 2024. Relaciones entre nociones aproximadas para cadenas de Markov etiquetadas. https://arxiv.org/abs/2407.07584v1
- **R10.** Rishabh Agarwal, Max Schwarzer, Pablo Samuel Castro, Aaron Courville y Marc G. Bellemare. *Deep Reinforcement Learning at the Edge of the Statistical Precipice*. NeurIPS 2021; versión revisada 2022. Evaluación comparativa, intervalos y perfiles. https://arxiv.org/abs/2108.13264v4
- **R11.** NASA. *NASA-STD-7009B: Standard for Models and Simulations*, 5 de marzo de 2024. §§4.1–4.3, uso, aceptación, V&V y credibilidad. https://standards.nasa.gov/standard/NASA/NASA-STD-7009 · Documento: https://standards.nasa.gov/sites/default/files/standards/NASA/B/1/NASA-STD-7009B-Final-3-5-2024.pdf
- **R12.** ACM SIGSIM PADS 2026. *Reproducibility and Artifact Evaluation*. Criterios de artefactos y resultados reproducidos; revisión e informes. https://sigsim.acm.org/conf/pads/2026/blog/artifact-evaluation/
- **R13.** Helge Spieker, Dennis Gross y Arnaud Gotlieb. *Probabilistic Model Checking of Autoregressive Neural Sequence Models*. arXiv, septiembre de 2026; el registro declara ICTSS 2026. §3, DTMC, soundness y refinamiento; §4, casos. https://arxiv.org/abs/2609.00838v1 · Texto: https://arxiv.org/html/2609.00838v1
- **R14.** Sultan Javed Majeed y Marcus Hutter. *Performance Guarantees for Homomorphisms Beyond Markov Decision Processes*. Versión extendida, 2018; versión corta AAAI 2019. §5 y apéndices: garantías bajo condiciones de agregación. https://arxiv.org/abs/1811.03895v1

