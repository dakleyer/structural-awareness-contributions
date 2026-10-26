# Auditoría de reducción, isomorfismo y límites — ACC → ecosistema agéntico v0.1

**Ámbito:** auditoría científica del PR de investigación, no modificación del canon ACC, de 00M/00N, de 01K-HID ni del protocolo UC21. **Criterio:** la analogía no se declara una nueva capacidad matemática sin señalar un operador nuevo, sus precondiciones y un comparador que pueda refutarla.

## 1. Qué preserva la reducción

La reducción conserva la pregunta económica de ACC: **con los mismos recursos físicos disponibles pueden coexistir un estado operativo A, una mejora técnica posible, una trayectoria no autorizada o no coordinada y costes que hacen preferible mantener A**. No promete acceso al óptimo ni confunde más producción con más bienestar humano.

| Propiedad del modelo social | Imagen en este experimento | Equivalencia y condición | Prueba o límite |
|---|---|---|---|
| Recursos finitos y óptimo condicionado | 10 unidades: proveedor-donante 6 y receptor 4, coordinación `h` incluida | Misma restricción física, bajo escenario simplificado de recurso fungible | AG01 conserva 10; el árbitro conoce el máximo físico, no el planificador |
| Función, permisos, rol y metamorfosis | `public_A`, `metamorph_declared_in_A`, `release_declared_in_A`, consentimiento y autoridad | **Reparametrización de A**, no capacidad extra de B/C/D | AG05–AG08, AG26–AG27 impiden atajos |
| Distancia al óptimo y pérdida de oportunidad | `mission_output_gap_to_same_budget_technical_optimum` | Análogo cuantitativo de brecha de output; **no** identidad con sufrimiento humano ni con deuda exigible | Óptimo del árbitro puede ser inaccesible jurídicamente |
| Declaración cualificada parcial B | Q scoped: fuente, ventana, tasa inferior, límite de transferencia | Señal adicional B sobre una pregunta; **no** exportación exhaustiva de la función interna | AG01/02 mismo A, distinto futuro; AG11 falsa Q |
| C y D | C = indicio no valorable; D = incertidumbre material no evaluable en el alcance | Semántica de 00M v0.8 conservada; no son probabilidades ni tasas ocultas | AG09, AG14–15 y AG30 mantienen abstención |
| Cooperación/cesión solidaria | Permiso y cesión funcional verificables | Se representa como objetivo, derecho y restricción ya descritos; **no** solidaridad moral inferida | AG06–AG08, peer convencional idéntico |
| Coordinación y coste de transición | Protocolo de transferencia y gasto físico `h` | Instancia del mecanismo ACC, ejecutable también de manera convencional | AG04, AG17–18, AG23–24 |
| Evaluación y riesgo de seguir en A | Cota B, verificación incompleta, decisión de no mover | Un cálculo de utilidad/decisión con información parcial; no requiere aversión al riesgo psicológica | A-only puede ganar; Q falsa puede perjudicar |

**Uso estricto del término isomorfismo:** la tabla documenta *correspondencias conservadoras bajo una proyección* de ACC a un dominio tipado. La reducción, en sentido formal, no prueba una biyección entre estados y operadores sociales y computacionales. Las diferencias de semántica personal, justicia, derechos, información y temporalidad impiden afirmar un isomorfismo total. Cuando un mecanismo es ya expresable por función de utilidad, restricción, estado de información o regla de coordinación en ACC, lo tratamos como **instancia/parametrización**, no como nuevo descubrimiento agéntico.

## 2. Tres hipótesis de perfil y qué agregan realmente

### AG-R1: opacidad composicional entre vendedores

Una interfaz puede publicar misión, contrato, entradas, salidas, permisos y capacidad sin exponer la tasa marginal futura ni las dependencias internas de otros proveedores. Es **plausible** en ecosistemas agénticos distribuidos de varios proveedores, no obligatorio. Hay sistemas tradicionales con idéntica opacidad, y agentes con trazabilidad completa. La prueba AG01/AG02 exhibe la posibilidad matemática de estados internos distintos con **A observacionalmente idéntico**, no la frecuencia del fenómeno en el mundo real.

### AG-R2: frustración de misión, no sufrimiento

Se reemplaza el término humano sólo en el indicador técnico: **frustración operacional de misión = brecha respecto de un máximo técnico de laboratorio a igual presupuesto**. Si se estudian humanos, sufrimiento, dignidad, preferencias y legitimidad necesitan instrumentos y criterios independientes; 01K-HID conserva propiedad y límites. Dos registros no aditivos:

- `G1`: brecha técnica del árbitro privado. Puede no ser alcanzable/autorizada con A vigente.
- `G2`: cota **condicional** de mejora cercana que Q afirma y la trayectoria actual no ejecuta. Puede ser falsa, como AG11. **Nunca se suma G2 a G1**.

Esta segunda medida no es una facultad exclusiva agéntica: cualquier sistema con Q y memoria del bloqueo puede registrarla. No atribuimos conciencia, insatisfacción experimentada ni aversión al riesgo subjetiva a un algoritmo.

### AG-R3: metaproceso/oráculo parcial de segundo orden

El candidato realmente operativo es un **protocolo acotado** que utiliza A+Q para proponer, calificar, pedir autorización y coordinar una transición; preserva material D y no reconstruye C/D. Su coste de diseño, consulta y coordinación es real. No crea permisos ni capacidades. Es *de segundo orden* porque trata la **revisión y reasignación de funciones**, no porque resuelva la indeterminación mediante un oráculo total.

**Importante:** un sistema no agéntico que accede a exactamente la misma Q, permisos y recursos puede ejecutar el mismo algoritmo. La diferencia agéntica todavía no probada reside en parámetros y condiciones de despliegue: menor coste de modificar roles e interfaces, frecuencia de reconversión, adaptabilidad, propiedad de las fuentes, coordinación entre jurisdicciones y latencia. Son hipótesis empíricas, no consecuencias lógicas de llamarse «agente».

## 3. Exigencia para declarar una extensión no isomórfica

Para cada futuro factor (validación social, vínculos familiares, preferencia por seguridad, rol, misión moral, reputación o coordinación multiagente):

1. **Intentar primero la codificación ACC:** utilidad (U), restricción, información relativa A/B/C/D, autoridad o coste de transición. Si conserva todas las predicciones pertinentes, es una **parametrización isomórfica para la pregunta**, aunque el ejemplo social sea distinto.
2. **Demostrar residuo:** presentar al menos dos estados con idénticos parámetros ACC relevantes y resultados distintos **que el mecanismo propuesto pueda predecir**. Sólo entonces introducir estado u operador nuevo, con semántica, coste de observación y permisos definidos.
3. **Comparar con igual información:** evaluar el operador nuevo frente a un peer no agéntico capaz, no contra un sistema artificialmente ciego o sin autorización.
4. **Conservar falsadores:** si un peer empata, la fuente Q miente, no hay consentimiento, un D material sigue abierto o A completo sale más barato, **el diferencial no se acredita**.

Por ello, validación social y benevolencia funcional pueden modelarse inicialmente como términos de utilidad; la solidaridad agéntica explícitamente programada puede ser una restricción/objetivo de A. Ninguna es por definición una nueva dimensión no isomórfica.

## 4. Auditoría de comparabilidad y límites de los 55 tests

| Afirmación | Qué sí demuestra la batería | Qué NO demuestra |
|---|---|---|
| Estados no distinguibles con A | AG01/02: mismo contrato A, margen privado distinto | Que agentes reales ocultan siempre sus transformaciones |
| Mejora parcial sin más recursos | AG01: 10 → 11,5, físico total 10, Q sólo hasta 2 | Que el óptimo 13,5 sea gobernable o que el protocolo gane siempre |
| Frustración de segundo orden | AG04 registra oportunidad Q condicional no ejecutada | Que exista dolor o frustración psicológica artificial |
| Falsas ventajas/garantías | AG11/29: Q falsa puede empeorar la misión | Que los metadatos sintácticos autentiquen una fuente |
| Permisos y desconocidos | AG05–09,14–15,26–30: bloqueos y abstención | Que todo C/D sea un bloqueo global para toda pregunta |
| Peer no agéntico fuerte | AG01/22 empate o victoria equivalente; AG18/19 alternativa dirigida/full gana | Que la implementación agéntica aporte un mecanismo intrínsecamente único |
| H5: menores costes agénticos | AG23/24 y grid: resultados varían cuando cambia el overhead `h` | **No** hay experimento empírico ni comparación pareada independiente del coste de reprogramación por arquitectura |

**Observación metodológica crítica:** en el prototipo, `CONVENTIONAL_EQUIVALENT_Q` y `Q_META_PROTOCOL` comparten lógica de propuesta y, en cada caso, el overhead físico. AG23 vs AG24 modifica el escenario, **no identifica causalmente «agentes frente a sistemas tradicionales»**. H5 queda explícitamente **no probada**. Una próxima campaña requiere parejas donde las arquitecturas reciban la misma demanda, Q, derechos y capacidad, pero midan por separado sus costos reales de transformación y coordinación. La familia A-only del prototipo es una política conservadora explícita, **no** el mejor decisor posible basado en A.

El coste de coordinación `h` se resta del **recurso físico** antes de puntuar output. El coste `instrument_cost` se resta posteriormente del **valor de misión en unidades sintéticas compatibles**; no debe interpretarse como consumo adicional de las diez unidades físicas. Ninguno de los valores es un precio de mercado medido.

## 5. Publicación y próxima campaña

Este paquete corresponde a una **investigación Stage A sintética**, posterior y separada del contrato ACC; no promueve resultados UC21 ni modifica el DDS. Antes de una afirmación causal o de promover a un perfil operacional se necesita:

- Congelar servicio, interfaz, objetivo, coste, permisos, fuente Q, proveedor y horizonte de evaluación.
- Medir Q verdadera/falsa y vigencia; incluir B/C/D sin colapsarlos a tasas para fines de optimización.
- Ejecutar seis brazos con un referee independiente y contrafactuales fuertes, más condiciones adversas.
- Incluir coste/latencia de cambio de rol, reprogramación, gasto de coordinación, revocación y mantenimiento.
- Validar si un diferencial persiste **después de igualar información, presupuesto y garantías**; publicar la ausencia de diferencial como resultado legítimo.
- Para extrapolar a personas, nunca traducir automáticamente brecha operativa en sufrimiento vivido, derechos o dignidad.

**Resultado del PR:** plausibilidad lógica, 30 fixtures y 160 variaciones con falsadores; no predicción de que los sistemas agénticos sean universalmente mejores ni solución al óptimo social global.

## 6. Trabajos primarios relacionados: respaldo limitado y diferencial aún abierto

| Trabajo primario | Qué acredita para esta investigación | Qué **no** acredita |
|---|---|---|
| [A2A Protocol — especificación oficial de Agent Cards](https://github.com/a2aproject/A2A/blob/main/docs/specification.md), §8, §§3.1.11/3.3.4 y §13 | Un protocolo de interoperabilidad de agentes puede publicar habilidades, endpoints, capacidades, versiones y credenciales sin publicar el funcionamiento interno; incluso distingue fichas públicas de fichas extendidas sujetas a autorización. Hace **verosímil técnicamente** AG-R1. | No prueba que un contrato A sea siempre insuficiente, que un output sea subóptimo, que una Q concreta sea verdadera ni que toda arquitectura agéntica sea opaca. |
| [Reid G. Smith (1980), *The Contract Net Protocol*](https://cse-robotics.engr.tamu.edu/dshell/cs631/papers/smith80contract.pdf), pp. 1104–1106 | La negociación de tareas, la selección mutua, la reasignación y el cambio dinámico de roles mediante protocolos distribuidos tienen antecedentes formales **no exclusivos de agentes LLM**. Es un antecedente/comparador necesario para AG-R3. | No valida nuestro metaprotocolo específico, nuestra semántica B/C/D ni el coste de implantación. |
| [Bernstein, Givan, Immerman y Zilberstein, *The Complexity of Decentralized Control of Markov Decision Processes*](https://people.cs.umass.edu/~immerman/pub/bgiz.pdf), resumen y §1 | Bajo el formalismo **Dec-POMDP** del artículo, ciertos problemas de control descentralizado con información parcial son complejos en el peor caso; justifica tratar la observabilidad y la coordinación como problemas técnicos serios. | No prueba que nuestro fixture sea un Dec-POMDP, ni que un metaprotocolo A+Q sea óptimo, ni que agentes actuales cuesten menos de reorganizar que microservicios o una organización humana. |

**Conclusión del estado del arte:** hay precedentes sólidos de **interfaces con visibilidad parcial, coordinación distribuida y límites computacionales**. La afirmación investigable de este PR es una combinación contextual y falsable con presupuesto, Q acotada, autoridad y costes; **no** la invención original de la coordinación, de la solidaridad programable o de la frustración humana. La hipótesis de menor coste y mayor plasticidad agéntica requiere una campaña comparativa nueva.
