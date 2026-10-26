# ACC — Núcleo técnico del modelo económico abierto (v0.1)

**Autor conceptual:** Iván Abril Palma / The Integral Management Society. **Estado:** formalización de investigación; modelo abierto y falsable, no teoría empíricamente validada ni contrato operativo de ACC. **Edición de consolidación:** 25 de octubre de 2026.

**Función de este documento:** reunir en un solo contrato técnico los desarrollos económicos de los anexos v0.1–v0.6 conservados en [Notas completas](model/01_NOTAS_COMPLETAS.md). El [modelo integrado](MODEL.md) sigue siendo su exposición general; este núcleo es su referencia formal para variables, restricciones, ejemplos, relaciones y falsadores. La nota de [01K sobre experimentos de segundo orden](../../01K_A02_HID_SECOND_ORDER_ECONOMIC_ACCELERATION_RESEARCH_NOTE_v0.1.md) conserva el programa específico de Human Intelligence Debt (HID).

La pregunta principal no es si la producción crece. Es **si la producción puede aumentar mientras crece también la distancia respecto de configuraciones mejores realizables con recursos y tecnología presentes; y qué mecanismos materiales, de información, gobierno y reajuste explican esa diferencia**. El signo no se predetermina: especialización, coordinación competente, protección y aprendizaje pueden producir resultados netos superiores.

## 1. Unidad económica, estados y frontera contrafactual

Una instancia declara antes del contraste:

- Un sistema S_t en el instante t: actores y afectados, tecnología, recursos, capacidades, procesos, redes, información, reglas, permisos, obligaciones, costes, producción y resultados.
- Un horizonte H, una población, territorio, fronteras institucionales, y riesgos/terceros afectados. El mismo servicio Y debe conservar cantidad, calidad, cobertura, oportunidad, continuidad, seguridad, privacidad, derechos, garantías y externalidades pertinentes.
- Un vector de inputs I_t(S) = (I_humano, I_técnico, I_material, I_tiempo, I_coordinación, …), con cantidades y unidades declaradas. Los inputs heterogéneos no se suman sin precios sombra o función de coste justificada.
- Producción P_t(S), utilidad directa por actor u_i,t(S), bienestar W_t(S) y facultades reales de decidir. Producción física, ventas, beneficio, utilidad y bienestar no son sinónimos.
- Dos conjuntos: F^T_t, alternativas **técnica y materialmente factibles** dentro de H, con tecnología y medios disponibles; F^G_t ⊆ F^T_t, alternativas además **accesibles por los mecanismos y autorizaciones vigentes**. Una alternativa en F^T_t \ F^G_t no es físicamente imposible, pero tampoco puede ejecutarse legítimamente por ser atractiva.

Una transición candidata τ: S_t → S′ exige distinguir: existencia técnica; resultado deseable según criterios declarados; propuesta; evaluación y consentimiento; aprobación válida; financiación/reajuste; ejecución; y resultado observado. La referencia no es un óptimo histórico imaginario ni el máximo individual independiente de cada afectado, sino un conjunto conjunto, factible y fechado. Si hay varios estados no dominados, se conserva la **frontera de Pareto** o un rango, no una «distancia única» inventada.

### Los dos ejes económicos que no deben mezclarse

**Eficiencia E:** para exactamente el mismo vector completo Y_t, existe una alternativa que consume menos recursos o sacrificio real. El coste K_t(S | Y_t) usa una unidad común sólo si hay conversión sustentada. Una rebaja a costa de trasladar contaminación, carga humana, inseguridad o interrupciones fuera de perímetro no cuenta.

**Utilidad y distribución D:** entre transiciones factibles se comparan Δu_i para todos los afectados y la posibilidad de redistribuir el beneficio. Una solución eficiente puede perjudicar a alguien; una transferencia puede volverla aceptable sin cambiar la producción total, pero consume recursos de ejecución y puede estar prohibida o ser insuficiente.

La referencia operativa puede tener un eje escalar U, un vector de utilidades (u_1,…,u_m) o un orden parcial. No agregar personas, derechos o dimensiones sin una regla de ponderación declarada.

## 2. Distancia al óptimo accesible, oportunidad y deuda de utilidad

Se reserva G para una **brecha contrafactual económica** y no para una obligación monetaria. Con U_t comparable, escala y población constantes y S_t incluido en el conjunto de referencia:

- G^T_t = max_{S′∈F^T_t} [U_t(S′) − U_t(S_t)] ≥ 0, oportunidad técnicamente accesible.
- G^G_t = max_{S′∈F^G_t} [U_t(S′) − U_t(S_t)] ≥ 0, oportunidad alcanzable con mecanismos vigentes.
- G^G_t ≤ G^T_t. La diferencia identifica el margen afectado por el régimen de acceso bajo esa función U, **no** atribuye por sí misma una causa al veto.
- G_vis,t(S;o) = Σ_{j∈K_vis} λ_j max(0, d_j(o)−d_j(S)), sólo cuando la alternativa **única** o es conjuntamente factible, las escalas son comparables y no hay costes duplicados. La versión vectorial y el conjunto de referencias son preferibles cuando hay alternativas incompatibles o derechos no fungibles.

«Distancia visible» puede representar una oportunidad percibida, no la realmente realizable. «Deuda de utilidad» es la etiqueta de investigación para una brecha persistente y verificable respecto del contrafactual declarado, no automáticamente deuda financiera, pérdida subjetiva o HID. Evitar usar G^T como deuda **recuperable** cuando la única transición técnicamente posible exige cambios legítimamente no autorizables, perjuicios no compensables o costes que anulan la ganancia.

Para un conjunto de propuestas individuales rechazadas, D_bruta = suma de sus valores declarados puede ser sólo **presión de oportunidades propuestas**. La pérdida recuperable se estima sobre el **mejor conjunto compatible** bajo recursos, derechos, plazo, efectos sobre terceros y costes completos. No sumar mejoras mutuamente excluyentes.

### Ejemplo dinámico que el modelo debe conservar

| Instante | Servicio entregado Y_t | Recursos del estado actual | Recursos de una alternativa para **el mismo Y_t** | Brecha de eficiencia G^E_t |
|---|---:|---:|---:|---:|
| t0 | 100 | 100 | 80 | 20 |
| t1 | 140 | 110 | 65 | 45 |

La producción sube de 100 a 140 y el consumo de recursos actual pasa de 100 a 110, pero la distancia frente a lo que se podría conseguir **en cada fecha** crece de 20 a 45. Los números son ilustrativos. G^E son unidades de recursos evitables; no deben publicarse como puntos de bienestar o horas HID sin una conversión adicional. Exige verificar que, en t1, 65 recursos bastan realmente para el mismo vector Y_1=140, con seguridad, derechos y costes de la transición incluidos en la evaluación apropiada.

**Distinción temporal:** G_t es brecha en t, semejante a un estado/stock medido. Σ G_t·Δt es exposición acumulada a la brecha y sólo adquiere interpretación económica con unidad y horizonte coherentes. El mero crecimiento de ese acumulado no demuestra aceleración de G_t.

## 3. Dimensiones abiertas, soberanía y selección de transiciones

D_n={d_1,…,d_n} es un inventario **provisional** de coordenadas evaluadas. Las familias iniciales son E (eficiencia), D (utilidad/distribución), C (coordinación) y A (atribución/reconocimiento); Q denota autoridad/ejecutabilidad y otras coordenadas pueden incluir seguridad, plazos, reversibilidad o información. Cada coordenada fija qué mide, quién o qué queda afectado y cómo se ordena. Ninguna equivale por sí sola a una persona con veto.

Sobre coordenadas conocidas, S′ domina débilmente a S si Δd_j ≥ 0 para todas las j consideradas, con al menos una mejora estricta. Esa dominancia **no** equivale a Pareto de preferencias humanas completas, ni concede ejecución.


### 3.1. Mecanismo primario: codependencia por recursos y saturación funcional

El bloqueo de una transición **no requiere** egoísmo, irracionalidad, un veto jurídico ni una dimensión soberana: puede resultar de un input material, humano, informacional o de coordinación que una función necesita íntegramente para seguir operando. Las familias E (eficiencia/recursos), R (utilidad/distribución), C (coordinación) y V (atribución/crédito) son dimensiones ECONÓMICAS, no A/B/C/D de 00M. El inventario es abierto y relativo a la pregunta del estudio. Cada condición bloqueante exige evidencia de su verdadera necesidad; no convertir preferencias no observadas ni simples señales C/D en requisitos físicos.

Para acciones x, rediseños y y recursos/participación caracterizados, una instancia lineal puede declarar:

~~~text
Recursos E:         a_j · x − g_j · y ≤ b_j
Coordinación C:    c_l · x − h_l · y ≤ k_l
Continuidad R:     u_i(x,y) ≥ u_min,i
Crédito V:         q_i(x,y) ≥ rho_i · Q(x,y), con Q>0
~~~

Los márgenes b_j,k_l pueden valer cero. Si a>0 y a·x≤0, toda acción incremental x≥0 que consume ese input queda bloqueada. Si un rediseño y LEGÍTIMAMENTE FACTIBLE libera capacidad, la condición a·x−g·y≤0 puede habilitar crecimiento sin exigir la desaparición de la función inicial. Coordinación también es un recurso escaso. El umbral de crédito puede proteger acceso/continuidad pero debe acreditarse; no imponerlo como diagnóstico del carácter de un agente. Para Q>0 totalmente repartido, q_i≥rho_i Q admite una distribución si y sólo si Σ rho_i≤1, sin otras cotas ni costes. Pedir 7/10 por sí solo es viable; exigir simultáneamente 7/10 y 4/10 es incompatible.

**Trampa racional con restricciones lineales y utilidades individuales monótonas:** sean x_1,x_2∈{0,1}; exíjase x_1≤x_2 y x_2≤x_1, y u_1=4+x_1, u_2=4+x_2. Los dos estados finales factibles son (0,0) y (1,1), y el segundo domina estrictamente a Pareto al primero. Sin embargo, ningún recorrido de cambios BINARIOS UNILATERALES mantiene la factibilidad en todos los pasos. Una transición conjunta/atómica, si existe realmente, supera el atasco. Esta trampa depende de la indivisibilidad y del PROTOCOLO DE TRANSICIÓN, no de que el objetivo o la restricción sean no lineales. Si ambos agentes pueden variar continuamente y coordinados sobre x_1=x_2, hay una ruta factible.

Así se separan tres objetos: F^T (estados finales materialmente factibles), F^G (estados finales además autorizados) y Reach_Π(S) (estados efectivamente alcanzables desde S bajo un protocolo Π de coordinación y cambios). Puede ocurrir Reach_Π(S)⊊F^G⊆F^T. No introducir Reach como un tercer óptimo canónico ni llamar «subóptimo en F^G» al máximo de Reach si no existe ruta; identificar el conjunto de referencia y la razón del atasco. Una falta material genuina sin alternativa factible no crea deuda recuperable por sí misma.

**Pareto no significa monotonía de funciones.** Pareto compara resultados finales sin imponer u_i'(cantidad)≥0 en todo el dominio. Una curva de manzanas puede aumentar, caer al acumular excedentes y volver a aumentar después de un umbral que habilita venta. El modelo admite utilidades no monótonas, funciones compuestas, umbrales y complementariedades. La aproximación lineal/monótona es una familia útil, no un límite ontológico. Una tabla finita de utilidad puede representarse con selectores binarios o una función evaluable; las funciones generales no convexas pueden requerir otros optimizadores y no existe garantía de coste computacional bajo.

Las reglas de soberanía, aprobación, responsabilidad, consentimiento, compensación y solidaridad elegida que siguen son **una formulación adicional** para transiciones donde efectivamente existen tales facultades. Una restricción material no es un titular de veto, y una preferencia no es automáticamente una necesidad intransferible. Véase el [estudio sintético acotado y sus controles negativos](studies/bounded-traps-v0.1/README.md).

### 3.2. Caso adicional: soberanía, autorización y vetos efectivos

Se distinguen:

- J_B: **condiciones bloqueantes efectivas** con regla, titular material/institucional, competencia, plazo y posibilidad de sustitución/delegación; a_j(τ)∈{0,1}.
- J_N: condiciones informativas, diagnósticas o de negociación **sin veto autónomo**.
- T_estructura(τ) = ∏_{j∈J_B} a_j(τ). El producto representa el toy de requisitos conjuntivos; no cuenta como veto nuevo cada verificador, proveedor o dimensión sin facultad independiente.
- Una restricción física de capacidad eléctrica o vía ferroviaria impide factibilidad; no es preferencia política ni oposición estratégica.

**Apertura n→n+1:** si una mejora de coordenadas conocidas no transita, se puede investigar una condición adicional *con hipótesis que prediga observaciones distinguibles* (distribución, autoridad, límite físico, conocimiento, presupuesto, confianza). También se admite error, datos insuficientes, falta de ejecutor o causa no resuelta. Agregar dimensiones indefinidamente para «salvar» la hipótesis no es validación.

**Estados de propuesta:**

1. No-brainer **local**: favorable para una parte/subconjunto de coordenadas; no acredita solución global.
2. No-brainer **conjunto**: todas las condiciones relevantes evaluadas, costes incluidos, información suficiente, permisos y mecanismo disponibles; procede sin reajuste extraordinario.
3. Mejora **tras reajuste**: negociación, rediseño, compensación o aprobación legítima adicional permiten ejecutarla.
4. **Bloqueada**: puede existir una alternativa favorable, pero falta una condición efectiva o el coste real de ajustarla supera su ganancia; sólo la primera variante con contrafactual neto recuperable es candidata a deuda económica.
5. **No establecido**: evidencia insuficiente para declarar viable o inviable la propuesta; no convertir incertidumbre en impedimento físico ni en un «sí».

### 3.3. Posiciones epistemológicas endógenas de la composición y coste de comprensión

La actividad económica recursiva puede representarse como una composición de funciones productoras. Un componente hoja entrega \(y_i(d_i)=\min(d_i,c_i)\) bajo demanda \(d_i\) y capacidad física caracterizada \(c_i\). Un módulo compuesto \(g\) entrega \(y_g(d)=\min(K_g,\sum_{h\in hijos(g)}y_h(d_h))\), con \(K_g\) una capacidad compartida cuando exista. Esta estructura produce **saturación de output** y codependencia material aun si las respuestas a la demanda son monótonas no decrecientes. El siguiente participante puede recibir sólo \(A_g=y_g(d^0)\), que no determina necesariamente \(y_g(d^1)\) cuando cambia la demanda. No hay que introducir un «velo» aleatorio: la representación contrae una función compuesta a una respuesta situada y elimina distinciones potencialmente necesarias para otras preguntas.

Para el estado interno \(w\), la interfaz observada \(E(w)=A\) y una pregunta receptora \(r_q(w)\), la insuficiencia exacta de A-only se establece con **dos testigos admisibles** \(w_1,w_2\) tales que \(E(w_1)=E(w_2)\) pero \(r_q(w_1)\ne r_q(w_2)\). La familia de preimágenes no es la definición de la totalidad de B/C/D del mundo. Una nueva cualificación \(Q_q\), producida a partir de **fundamentos realmente disponibles en la fuente**, puede distinguir algunos casos sin inventariar todas las preimágenes. No debe inferirse \(Q_q\) sólo del mismo A, ni dar al receptor un oráculo del estado interno del simulador.

Las posiciones de [00M §1](../../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) nacen, por tanto, de qué puede establecer y transmitir cada proceso bajo el coste y la autoridad presentes, y no son una segunda taxonomía cerrada de subsistemas:

- **A:** salida funcional del proceso explotado para la demanda/pregunta vigente. Una evaluación nueva que entregue un certificado produce A de **su propia función**, sin cambiar el A productivo anterior.
- **B:** soporte y reserva de explotación/evaluación **caracterizada**. En esta realización, un productor conserva outputs operacionales nativos de sus componentes y conoce la capacidad marginal de los nodos de un trayecto pertinente hasta el receptor. Puede establecer un límite de capacidad para esa consulta, con alcance, versión, tiempo y procedencia; ello no cierra toda la reserva B ni el exterior.
- **C:** un indicio fundado de que otra inspección o interlocutor podría aportar información, pero sin marco ya caracterizado de objetivos, variables, coste y rendimiento. No se introduce una cifra de ROI ex ante para C en contra de su definición; una exploración acotada puede establecer una base B o no.
- **D:** testimonio de una influencia potencialmente material que el proceso no tiene **ruta efectiva de evaluación** en sus medios, permisos, método y horizonte. D no es un inventario ni un veto de actor, y su impacto no se convierte en variable aleatoria conocida. Una ausencia de indicios permanece sin rol establecido.

**Contabilidad de comprensión con cuatro alternativas reales, bajo pregunta y presupuesto fijados:** explotación A-only; cualificación B relevante ya disponible o producida por fuente con registro/capacidad y costes completos; inspección convencional **dirigida**; ampliación exhaustiva de A a todos los nodos internos cuando sea accesible. Sean \(N\) nodos, \(L_q\) los nodos pertinentes del trayecto de una pregunta y \(v\) el valor declarado de cada unidad marginal de servicio. Las funciones contables \(C_\mathrm{full}=N c_\mathrm{node}\) y \(C_B=L_q c_\mathrm{B}+c_\mathrm{transfer}+c_\mathrm{maintenance}\) son **hipótesis de adquisición del instrumento**, no cotas universales de complejidad. Deben imputarse creación y custodia de los logs nativos si no son recursos ya existentes y contabilizados. El costo de una revisión dirigida \(C_\mathrm{target}\) es un comparador obligado, no una variante artificialmente inferior.

Si una sola decisión tiene mejora máxima físicamente acotada \(V_{\max}\), y \(C_\mathrm{full}>V_{\max}\), inspeccionar **todo** no puede superar a mantener A en utilidad neta para esa única decisión bajo este modelo de coste y sin beneficios adicionales. No se concluye que C sea universalmente inexplorable; la inspección completa puede ser mejor si ya es barata, si hay múltiples preguntas, si el comparador B miente o si la fuente no tiene una cualificación legítima y suficiente. Las certificaciones B incompletas o caducadas no prueban respuesta conjunta; una barrera D material pertinente conserva la insuficiencia para decisiones que la requieren.

**Ensayo sintético reproducible:** 16 productores y 32 nodos; el receptor observa \(A=128\) tanto si una demanda nueva puede elevar la producción a 130 como si una restricción de raíz obliga a permanecer en 128. En un escenario favorable, valor máximo adicional 10 unidades sintéticas; cualificación de seis niveles cuesta 2,25; inspección dirigida cuesta 3; reconstrucción de 32 nodos cuesta 32. El resultado neto ilustrativo es 7,75 / 7 / −22 respectivamente, frente a cero para A-only conservador. **Hay controles donde el competidor convencional gana y donde Q es falsa, caducada, inaccesible o inútil.** La autenticidad criptográfica de Q no está probada por comprobar etiqueta, alcance y versión; el simulador registra su verdad sólo tras tomar la decisión.

En el laboratorio finito, \(n\) ramas independientes con dos capacidades futuras posibles crean \(2^n\) perfiles de respuesta para **todas** las \(n\) preguntas binarias. Un mensaje fijo que responda exactamente todas necesita al menos \(n\) bits en ese experimento, mientras que una consulta binaria elegida necesita como máximo uno adicional y una cuenta agregada de capacidades distingue a lo sumo \(n+1\) respuestas. Es una cota **relativa a consultas e interfaz**, no un límite general de tiempo, ni una entropía medida del C/D abierto. El mismo caso puede resolverse con un comparador convencional que preserve las cualificaciones equivalentes.

La integración con las brechas \(G^T/G^G\) y con el sufrimiento estructural previo requiere **otra prueba causal**: conocer Q puede mejorar una decisión o permitir buscar una reasignación, pero no cambia físicamente los recursos, permisos, preferencias o capacidades ni calcula por sí solo HID (propiedad de 01K) o malestar vivido. Los efectos positivos, negativos, de continuidad y el coste marginal se conservan por separado. Véase [modelo intrínseco A/B/C/D, programa de contraste y auditoría científica](studies/intrinsic-abcd-economics-v0.1/README.md).

### 3.4. Composición abierta no fungible: suficiencia para una pregunta sin clausura del exterior

La composición de subsistemas productivos de §3.3 puede conservar o recibir **cualificaciones parciales no fungibles** acerca del fundamento B, la exploración C y las barreras D. Éstas no son inventarios completos ni categorías permanentes de objetos. El resultado matemático que se propone estudiar es más modesto y verificable: una combinación de declaraciones incompletas puede resolver **una pregunta receptora prefijada** sin revelar todos los elementos del exterior. La condición de suficiencia proviene de [00M §4](../../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) y se aplica con semántica de fuente/proceso de [00M §1](../../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md).

**Nube de puntos no exhaustiva.** Sólo disponemos de un número finito de testimonios recibidos; la cantidad, topología y pertinencia del residual exterior NO están caracterizadas. Supongamos, únicamente para una región R caracterizada, que una función f satisface una cota Lipschitz `|f(x)-f(x')| ≤ λ|x-x'|` con `λ≥0` y que fuentes legítimas dan para cada punto i `x_i∈[a_i,b_i]`, `f(x_i)∈[l_i,u_i]`. Entonces para cada pregunta x∈R definimos:

~~~text
D_i(x) = max(|x − a_i|, |x − b_i|)
L(x)   = max_i { l_i − λ·D_i(x) }
U(x)   = min_i { u_i + λ·D_i(x) }
        L(x) ≤ f(x) ≤ U(x)                 [CONDICIONAL A FUENTE Y REGULARIDAD]
~~~

Si `L(x)≥T`, la pregunta `q: f(x)≥T` está localmente apoyada; si `U(x)<T`, localmente descartada; en caso contrario sigue indeterminada. **No se ha clausurado C/D**: se ha cerrado una pregunta para una clase y región acotadas, con supuestos defendibles. Si falta un supuesto de regularidad o validez de fuentes, una nube finita admite funciones con valores arbitrariamente distintos entre muestras y NO autoriza interpolación. Si `L>U`, las evidencias o premisas son inconsistentes y no deben promediarse. Una D material fuera del marco impide extrapolar ese cierre local a una autorización global; una D no material para q no exige bloquear todo A.

**No fungibilidad y procedencia:** agrupar observaciones conserva `claim_id`, origen, vigencia, alcance y márgenes; duplicar un mensaje no produce corroboración independiente. Una falta de autorización no se compensa sumando precisión estadística, ni una C exploratoria tiene una función ROI caracterizada por el mero hecho de ser mencionada. D puede tener indicadores parciales sin volverse evaluable. `UNKNOWN` permanece cuando no hay fundamento para asignar rol. Una afirmación verdadera y suficiente para q genera un A del **metaproceso que cualifica**, sin cambiar retroactivamente el A de los productores.

**Metacognición decidible, no «oráculo de lo indecidible».** Una función con alcance declarado puede responder «apoyado / descartado / no establecido» respecto de la suficiencia de la base para q. No demuestra ni computa propiedades universales indecidibles de las funciones subyacentes. Si pudiera decidir total y correctamente YES/NO el problema de parada para todas las entradas, contradiciría la indecidibilidad de Turing. Mantener abstención/UNKNOWN es esencial: decidir una **propiedad del conocimiento presentado** no equivale a conocer la verdad subyacente. Un aviso de revisión no emite permisos ni ejecuta cambios de misión.

**Solidaridad libremente elegida y riesgo no cuantificado.** Una persona puede elegir contribuir bajo incertidumbre sin función escalar de rentabilidad; tampoco se sigue que su elección sea necesariamente sacrificio, daño o ganancia. Los derechos no renunciables, autorización competente, consentimiento positivo y garantías sobre terceros permanecen separados. El procedimiento puede emitir `VOLUNTARY_UNQUANTIFIED_RISK_REVIEW_ONLY` como apoyo para una deliberación legítima, NUNCA como acción automática ni como prueba del contenido de D. La mayor conciencia de una brecha puede cambiar el malestar subjetivo en cualquiera de los dos sentidos sin variar la distancia objetiva de desarrollo estipulada en el estudio de sufrimiento estructural del PR #43.

**Economía y falsadores:** el coste total de adquirir, mantener y transmitir cualificaciones B, la inspección dirigida convencional y la ampliación exhaustiva de A deben compararse con la misma pregunta y los mismos derechos/calidad. La suficiencia local no prueba ventaja económica por sí sola. Sistemas existentes de contratos/versiones/procedencia reciben pleno crédito; un peer más barato, un B falso, caduco o contradictorio, o una D material pueden refutar el diferencial propuesto. Ninguna probabilidad, cardinalidad o entropía se atribuye al exterior D sin un marco explícito. [Modelo ejecutable y fuentes](studies/scoped-closure-metacognition-v0.1/README.md) · [Auditoría de los seis bloques del Word del autor](studies/scoped-closure-metacognition-v0.1/PROMPT_COVERAGE_MATRIX.md).

## 4. Economía de la compensación y del reajuste

Una mejora de Marketing/Producción puede generar Δu_M>0 y Δu_O>0, pero imponer nuevas horas, riesgo o pérdida de influencia a Sistemas. Finanzas puede exigir CAPEX/OPEX, reasignación de presupuesto, competencia del CFO, contrato o proveedor homologado. El reto consiste en encontrar una transición conjunta factible, no en decidir por anticipado que Operaciones debe ceder su ahorro.

En el caso **muy fuerte** de utilidades plenamente transferibles y cuasilineales en un numerario común, sin restricciones de transferencia y con costes extraordinarios c_i no contabilizados ya, puede buscarse un vector t_i tal que:

~~~text
Para cada i:      Δu_i + t_i − c_i ≥ 0
Presupuesto:      Σ_i t_i = 0
Existencia:       Σ_i Δu_i ≥ Σ_i c_i
~~~

La última condición es suficiente **sólo bajo esos supuestos** y disponibilidad real del mecanismo. Cardinalidad de las utilidades **sin plena transferibilidad** no basta. Los derechos no renunciables, seguridad, riesgo no compensable, mandatos y el desacuerdo legítimo no se convierten automáticamente en t_i.

Diferenciar:

- **Transferencia t_i:** mueve valor entre actores/centros y suma cero en el agregado del modelo; su importe no es un consumo agregado nuevo de recursos.
- **Coste real de reajuste C_adj:** descubrimiento, verificación, comunicación, negociación, contratos, reconfiguración y resolución de riesgos. Registrar tiempo, gasto, fricción y oportunidad de cada episodio **una vez**.
- **Coste necesario C_nec:** coordinación y garantías válidas que cualquier alternativa competente mantiene.
- **Coste evitable C_evit:** exceso respecto de una alternativa competente, con el mismo vector Y, horizonte y condiciones legítimas. No todo C_adj es deuda.

Una identidad de evaluación admisible es ΔV_neta = ΔB_bruta − C_adj − C_otros_no_contados, **si y sólo si** ΔB_bruta no descontó ya esos costes y todos comparten unidad. Si C_adj supera la ganancia bruta compatible, abstenerse puede ser económicamente correcto.

### Ejemplo mínimo de negociación (valores inventados)

Marketing +60; Operaciones +40; Sistemas −30, **antes** de costes extraordinarios. Ganancia conjunta +70. Un traslado de 35 de Marketing hacia Sistemas deja Marketing +25, Operaciones +40 y Sistemas +5; no fuerza a Operaciones como pagador. Si coordinar y ejecutar consume 15 de valor en total, la ganancia agregada neta es +55 antes de otros costes; distribuir quién los soporta requiere un vector c_i y un nuevo chequeo Δu_i+t_i−c_i≥0. Un contrato o mandato puede impedir el traslado incluso con saldo positivo. No se infiere ejecución ni consentimiento de la suma +55.

Una segunda opinión puede **sustituir** un veto anterior o **añadir** una nueva aprobación; medir el cambio neto en J_B. Más revisores o proveedores no implican automáticamente más vetos. Un buen planificador de planta, una regla de despacho eléctrico o una programación ferroviaria convencional también pueden resolver esas dependencias: el problema económico no exige agentes de IA.

## 5. Producción creciente y oportunidades de interdependencia

La hipótesis **no** es «más dimensiones producen menos». Especialización añade capacidades productivas, propuestas y coordinación útil. Para n capacidades productivas, la parte base puede representarse P_base(n)=b·n, b>0; no tiene por qué agotar la producción total.

### M0 — Unanimidad sobre un número lineal de propuestas

Si cada capacidad plantea una mejora de valor g que requiere aceptación independiente de n−1 condiciones, cada una con probabilidad q∈(0,1):

~~~text
Pr(aprobación) = q^(n−1)
D_veto(n) = g·n·[1−q^(n−1)]
Δ²D_veto(n) = g·q^(n−2)·(1−q)·[(1+q)−n(1−q)]
~~~

Con q=0,90, la curvatura se anula alrededor de n=19. D_veto/n tiende a g: **la unanimidad con g fijo y sólo n propuestas no demuestra aceleración indefinida**. Aceptaciones correlacionadas, autoridad delegada o negociación cambian q y el contrato del toy.

### M1 — Dependencias materiales y pérdida por interacción

Sea E(n) el número de interacciones efectivas y no duplicadas; p la frecuencia marginal de incompatibilidad **persistente y evitable** tras sustitutos; c el coste de una relación, homogéneo y no duplicado:

~~~text
E[D_inter(n)] = p·c·E(n)
Red estrella:  E(n)=n−1                     → crecimiento lineal
Red completa: E(n)=n(n−1)/2                 → crecimiento cuadrático
Red completa: Δ²E[D_inter(n)] = p·c
~~~

Se requiere contrafactual **conjunto** donde las obligaciones puedan evitarse sin perder calidad, derechos ni producción. Un cuello único no se multiplica por el número de caminos. Independencia de enlaces no es necesaria para la **esperanza** de la suma, aunque afecta a la varianza.

### M2 — Sinergias productivas de las propias interacciones

Una interacción no tiene sólo coste. Si genera beneficio a cuando funciona:

~~~text
P_real(n) = b·n + a·(1−p)·E(n)
D_oportunidad(n) = a·p·E(n)   [sólo bajo contrafactual válido]
~~~

En red densa, tanto P_real como D_oportunidad pueden crecer cuadráticamente; la curvatura **absoluta** de la brecha no establece que crezca más rápido que el producto útil. Comparar elasticidades o tasas relativas bajo unidades consistentes, además de utilidad neta y perjuicios.

### M3 — Generación endógena de propuestas

Si cada capacidad origina k(n−1) propuestas distintas, cada una necesita n−1 autorizaciones y q permanece constante:

~~~text
M(n) = k·n(n−1)                             propuestas
A(n) = M(n)·q^(n−1)                         aprobaciones esperadas
R(n) = M(n)·[1−q^(n−1)]                     rechazos esperados
P(n) = b·n + a·A(n)                        producción esperada
D_bruta(n) = v·R(n)                        valor bruto etiquetado
ΔP(n) = b + a·k·n·q^(n−1)·[(1+q)−n(1−q)]
~~~

**R≠G≠HID.** Propuestas rechazadas pueden ser incompatibles, dañinas, duplicadas, legalmente inadmisibles o demasiado caras. Sólo se convierten en deuda *recuperable* tras optimizar un paquete compatible y descontar reajuste. Con b suficientemente alto, P puede seguir creciendo incluso si A cae. Si M(n)=kn en vez de kn(n−1), la parte rechazada tiende a crecimiento lineal.

| n | Base 10n | M, con k=1 | A, con q=0,90 | R | P=10n+A |
|---:|---:|---:|---:|---:|---:|
| 5 | 50 | 20 | 13,122 | 6,878 | 63,122 |
| 10 | 100 | 90 | 34,868 | 55,132 | 134,868 |
| 20 | 200 | 380 | 51,332 | 328,668 | 251,332 |
| 40 | 400 | 1.560 | 25,620 | 1.534,380 | 425,620 |
| 80 | 800 | 6.320 | 1,534 | 6.318,466 | 801,534 |

Son resultados **analíticos del toy**, no frecuencias observadas ni predicción de economía real.

### Contraste complementario: crecimiento relativo condicionado y complejidad representable

Si n capacidades producen b>0 cada una, existe un grafo de interacciones efectivas E(n), y se DEMUESTRA independientemente que una arquitectura conjunta puede realizar g≥0 de beneficio neto adicional por enlace con el mismo horizonte, recursos, calidad, seguridad y derechos, una instancia paramétrica puede definir:

~~~text
P_actual(n) = b·n + alpha·E(n), con alpha ≥ 0
P_conjunta*(n) = P_actual(n) + g·E(n)
G(n) = g·E(n)                          [brecha del toy; NO HID]
G(n)/P_actual(n) = g·E(n)/(b·n+alpha·E(n))
~~~

Con E(n)=n(n−1)/2, alpha=0, b=10, g=0,2: la producción actual crece linealmente, G crece cuadráticamente con segunda diferencia g, y G/P_actual pasa por 4 %, 9 %, 19 %, 39 % en n=5,10,20,40. Son identidades del **contrafactual supuesto**, no una ley social ni una medición de un óptimo real. El numerador sólo puede interpretarse como oportunidad recuperable tras demostrar que las ganancias entre pares son conjuntamente compatibles, ejecutar costes completos y preservar derechos/servicio. Si E(n)=n−1 (estrella), la proporción tiende a g/b; con alpha>0 y red densa tiende a g/alpha; con g=0 desaparece la brecha. Mayor número de dimensiones no implica mayor deuda relativa bajo todos los parámetros.

**Límites matemáticos y epistemológicos:** sistemas con objetivos/restricciones afines y variables continuas pueden admitirse como LP; con decisiones indivisibles, como MILP o búsqueda finita; curvas no monótonas y dinámicas pueden ser expresables, pero no necesariamente convexas ni fáciles de optimizar. Incluso mochila binaria, con objetivo lineal creciente y presupuesto lineal, es NP-difícil en general. Las influencias del mundo fuera de la formalización no se convierten en variables cerradas: 00M conserva B/C/D como cualificaciones parciales, C abierto y D no enumerable. Una entropía calculada bajo un modelo probabilístico explícito no mide el exterior no representado. El [estudio ejecutable de bloqueo racional](studies/bounded-traps-v0.1/README.md) distingue los resultados sintéticos de las obligaciones de prueba social.

## 6. Obligaciones, información, crédito y persistencia

El modelo se hace dinámico al incluir las obligaciones e interfaces que sobreviven a una decisión:

~~~text
O_(t+1) = O_t + N_t − R_t
M_t = coste de mantener y verificar O_t y sus dependencias
~~~

O_t es un inventario **identificado** de obligaciones vigentes; N_t nuevas, R_t retiradas. No es deuda humana por definición. Garantías, contratos, redundancias y controles pueden aportar valor protector superior a su mantenimiento. La tesis falsable es que condiciones de atribución, información deficiente o autoridad fragmentada reduzcan R_t o eleven M_t **más allá de la alternativa segura y útil**.

Los mecanismos candidatos son distintos y requieren observación separada:

1. **Human Intelligence Debt:** la arquitectura consume horas humanas ACW para mediar problemas evitables, reduciendo oportunidades de GIC.
2. **Attribution Gap:** contribución operativa C_i y crédito/autoridad atribuidos A_i divergen; ciertas reglas de reconocimiento podrían bloquear la retirada de obligaciones. No inferir intenciones personales.
3. **Informational Friction:** el mapa decisorio Mapa_t no representa suficientemente el flujo real Flujo_t; actuar sobre el mapa puede añadir trabajo o deformar el flujo.
4. **Cost of Clarity:** descubrir y actualizar la información que permite un acuerdo consume recursos medibles.
5. **Puente monetario:** el mantenimiento de compromisos y la tasa de retiro importan, pero **ni «dinero = deuda» ni «interés positivo ⇒ deuda exponencial»** son identidades adoptadas aquí.

Estas líneas pertenecen al mismo programa intelectual; su afinidad no son cinco confirmaciones independientes.

## 7. Human Intelligence Debt y generación/preservación de capacidades

El modelo productivo abre dimensiones que **generan** capacidad y nuevas interacciones; el modelo HID distingue qué capacidad humana disponible se usa, se bloquea, se libera o se pierde. No son la misma variable. El titular técnico de HID es [Annex 01K](../../01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md), no el contrato normativo de ACC.

**Taxonomía de tareas 01K / Paper 5:**

- GIC: contribución genuina de información, diseño, juicio o creación.
- NEO: ejecución y supervisión humana estructuralmente necesarias; no se cuenta como deuda sólo por ser humana.
- ACW: mediación, reconciliación, reentrada o contexto reconstruido **evitables** bajo un contrafactual seguro y equivalente.
- UNKNOWN: insuficiencia para clasificar, conservar explícitamente.

**Cálculo primario implementado en el optimizador sintético — diferencia directa por cada óptimo comparable:** sea S el estado subóptimo y O_j un óptimo técnico o gobernable dentro de las configuraciones factibles declaradas. Para igual servicio, capacidad, recursos, derechos y mismo vector de contribución informacional humana `h_k`, el resultado por óptimo es:

~~~text
HICR_modelo(S)       = Σ_k h_k(S)   / H_común
HICT_modelo(O_j)     = Σ_k h_k(O_j) / H_común
HID_modelo(S, O_j)   = [Σ_k h_k(O_j) − Σ_k h_k(S)] / H_común
HID_horas(S, O_j)    = Σ_k [h_k(O_j) − h_k(S)]
~~~

Se devuelve el resultado **para cada O_j**, con diferencias por componente y test de dominancia; no se fabrica un vector ideal combinando óptimos distintos. Si la comparación no es válida, HID directo queda **no medido**, no cero. Las horas ACW, NEO, recuperación `ρ` y brechas de utilidad sirven para **explicar/contrastar** el resultado; por sí solas no determinan la diferencia de entradas `h_k`. Esta realización operacional dentro de ACC **no crea un nuevo protocolo de medición de personas**, cuya autoridad permanece en 01K. Véase [auditoría HID por óptimos y experimento ABCD](studies/parametric-economic-toy-v0.1/HID_OPTIMUM_ABCD_AUDIT_v0.1.md).

**Indicadores auxiliares históricos con sus propias unidades y denominadores:**

~~~text
HICR_time = H_GIC / H_total
HID_observed = H_ACW / H_total
HICT = HICR + H_releasable / H_total
HID = HICT − HICR            [con mismo ámbito, base y definición]
F-HICT = HICR + ρ∞·H_releasable/H_total
HID_spent = (1−ρ∞)·H_releasable/H_total
NOI = H_added − H_removed    [trabajo de oversight]
~~~

En el bloque histórico de arriba, `HICT=HICR+H_releasable/H_total` es un **indicador potencial condicionado a recuperación/reemplazabilidad**, no un método para inferir automáticamente el incremento efectivo de `h_k` del óptimo. Su uso no debe sustituir la resta directa entre vectores de contribución informacional cuando estos existen.

HID_observed, HID potencial, capacidad efectivamente recuperada y HID_spent **no son intercambiables**. HICT/HICR siguen el contrato original; las horas y clases de Paper 5 sólo se publican como medida tras su puerta de calidad y evidencia de sustituibilidad. No usar n aplicaciones, n dimensiones, G de utilidad o C_adj como estimador directo de HID.

**Ejemplo de 10 unidades humanas:** S0 dedica 3 a GIC, 2 a NEO necesaria y 5 a ACW. S* mantiene el mismo Y y garantías, sustituye a coste total menor las 5 ACW y las libera. Si esas 5 encuentran una oportunidad factible y elegida de GIC: HICR_time=0,3; HICT_condicional=0,8; HID potencial=0,5. Si sólo 2 se convierten en GIC real, se registra **2/10 recuperado** y 3/10 liberado no convertido, sin llamarlo incremento de producción verificado. Capacidades cualitativamente distintas se reportan en vector y no se «suman» como trabajo intercambiable.

La **preservación de capacidad** requiere observar competencia efectiva, práctica, transmisión, acceso a instrumentos/recursos, condiciones de uso y posibilidad de reejercicio. Pérdida de habilidad por desuso, irreversibilidad, ρ∞<1 y recuperación parcial son **hipótesis longitudinales**; no se deducen de que la deuda o el número de dimensiones aumenten.

La pregunta de producción es independiente y complementaria: una dimensión productiva nueva puede aportar b>0 mientras eleva interacciones E(n), trabajo compensatorio y condiciones de reajuste; o puede aumentar sinergias, reducir ACW y preservar mejor la capacidad. Ambas trayectorias deben poder salir del mismo protocolo.

## 8. Utilidad neta, disconfort, soberanía económica y no duplicación

Definir B como beneficio directo neto de los costes que ya estén contabilizados en él. La brecha G y la frustración F **no** son el mismo objeto:

~~~text
F_t = φ(G_vis,t, información, expectativas, agencia, memoria, contexto)
W_t = B_t − F_t        [sólo si B no incluye ya F]
ΔW = ΔB − ΔF
~~~

Otra construcción de producción neta utiliza V_t=B_t−λd_t−F_residual,t, si B_t es **bruta respecto de esos costes**, λ convierte horas compensatorias a una utilidad declarada y F_residual es independiente y no contabilizada. Nunca sumar indiscriminadamente G + HID + ACW + C_adj + F: pueden ser vistas y valoraciones del mismo episodio.

Un ensayo puede contrastar un régimen donde W es **indicador** y otro donde una autoridad legítima adopta la condición adicional a_W=1[ΔW_prevista≥0]. Esto es una variable de **admisión económica candidata**, no un valor ético adoptado, una facultad ya existente o una sustitución de derechos. Una previsión errónea puede aprobar ΔW_real<0. El estudio debe observar falsos positivos, falsos negativos, opciones perdidas y reversibilidad.

Diferencia: la regla ΔG≤0 y la regla ΔW≥0 no equivalen. Por ejemplo, B:100→130, F:10→50 implica W:90→80, aun con mayor beneficio bruto. El disconfort exige instrumento humano propio; **no** se deduce de la brecha visible de un simulador.

## 9. Efecto primario, segundo orden y tiempo

**Primer orden:** beneficio/coste de la transición en su perímetro declarado y condiciones vigentes. **Segundo orden causal:** una transición modifica conexiones, crédito, obligaciones, capacidad, información o reglas que determinan el coste y la ejecutabilidad de transiciones posteriores. No identificar «segundo orden» con «segunda derivada» como definición.

Para una **carga nueva por periodo** d_t, en horas ACW evitables verificadas y no duplicadas:

~~~text
D_T = Σ_(t≤T) d_t·Δt                  exposición acumulada
Δd_t = d_t − d_(t−1)                 variación de flujo
Δ²d_t = d_t − 2d_(t−1)+d_(t−2)      curvatura discreta
e_t = d_t − previsión_ex_ante,t     error de mapa
~~~

Si Δ²E[d_t]>0 persiste con el mismo contrato de medida, existe aceleración **en esperanza** de la carga por periodo. No se sigue causalidad por observar curvatura ni por acumular una pérdida constante. La prueba causal necesita: cronología, mismo servicio y recursos, predicción sellada con la información ex ante, topología y obligaciones identificadas, control de mantenimiento/retiro, ablaciones y comparador competente.

Los resultados analíticos recreados de 20 ciclos pertenecen a [recreación sintética identificada](studies/synthetic-recreation-v0.1/README.md). Las **10.000 ejecuciones históricas declaradas** en las notas no han sido autenticadas con sus artefactos originales; la recreación no las autentica. No afirmar efecto humano o empresarial ni éxito de UC21/DDS.

## 10. Matriz mínima de observación y falsación

| Variable | Unidad / fuente independiente | Qué impediría concluir |
|---|---|---|
| P, Y, K | Unidades de servicio y recursos; registro de calidad y riesgo | El «mismo Y» resulta distinto; mejoras exportan costes |
| F^T, F^G | Inventario fechado de medios y derechos | S* incorpora tecnología futura, consentimiento inexistente o recurso duplicado |
| Δu_i, t_i, c_i | Actor, numerario, costes y pagos con IDs | Comparación interpersonal injustificada; transferencia inviable |
| J_B, J_N, T | Reglas, firmas, dependencias y sustitutos | Revisiones contadas como nuevos vetos sin independencia |
| G^E, G^U, G_vis | Frontera conjunta, escala y fecha | Suma de máximos individuales o propuestas incompatibles |
| C_adj, C_nec, C_evit | Costes por episodio y alternativa competente | Doble cómputo; coordinación necesaria clasificada como deuda |
| E(n), p, q, M(n), A(n) | Topología y contrato probabilístico | «Aceleración» preescrita por densidad supuesta sin medición |
| O_t, N_t, R_t, M_t | Obligaciones únicas, altas, bajas, coste real | Protección legítima contabilizada como deuda |
| GIC, NEO, ACW, ρ∞ | Tareas y pruebas independientes según 01K | HID numérico sin Study 0 y contrafactual |
| d_t, D_T, Δ²d_t, e_t | Serie de episodios, horizonte, forecast sellado | Acumulación confundida con curvatura o predicción omnisciente |
| W y F | Instrumento de bienestar con población y escala declaradas | Brecha técnica presentada como sufrimiento medido |

**Controles negativos exigidos:** red estrella/dispersa; red densa interoperable; capacidad de retiro; función de coordinación convencional competente; negociación y transferencia baratas; veto sustituido (no añadido); producción de sinergias superior al coste; intereses legítimos y derechos no compensables; mapa actualizado; escenario de estabilidad. Una tasa de complejidad alta con producción neta mejor y ACW no creciente **refuta la generalización fuerte**, no es una excepción que deba ocultarse.

## 11. Estado, propietarios y ruta de estudio

**Realización ejecutable:** [toy económico paramétrico v0.1](studies/parametric-economic-toy-v0.1/README.md): (1) búsqueda de óptimos entre configuraciones conjuntamente factibles; (2) simulador analítico de producción, interdependencias, obligaciones, d_t, D_T, HID condicional y brechas entre trayectorias; (3) M0–M3 con n variable; más CLI, seis ejes de sensibilidad y 34 pruebas deterministas. Los [resultados de referencia](studies/parametric-economic-toy-v0.1/results/REFERENCE_RESULTS_v0.1.json) se derivan del programa publicado. Es un instrumento de estudio, no una inferencia del comportamiento empírico.

- **Formalizado ahora:** objetos, unidades, modelos M0–M3, reglas de admisión, contabilidad de reajuste, diferenciación de deuda y mecanismos rivales.
- **Demostrado sólo dentro de toys:** posibilidad de producir más mientras crecen las brechas bajo parámetros explícitos; saturación de unanimidad; curvatura condicional de redes densas; no se infiere universalidad.
- **Ejecutado por separado:** [primer piloto económico determinista](studies/economic-pilot-v0.1/STUDY_PROTOCOL.md), con 18 casos y dos procedimientos principales que empatan; preserva un límite de información adverso. [Recreación analítica](studies/synthetic-recreation-v0.1/README.md) distinta de autenticación histórica.
- **Pendiente:** medición independiente de S*, G, C_evit y HID; experimentos factoriales de segundo orden en [01K-A02](../../01K_A02_HID_SECOND_ORDER_ECONOMIC_ACCELERATION_RESEARCH_NOTE_v0.1.md); realización posterior con comparadores DDS; observaciones humanas, capacidades longitudinales y generalización.
- **Límite de propiedad:** [01K](../../01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md) conserva definiciones HID; [ACC normativo](../../01I_AGENTIC_CITIZENSHIP_CONTRACT_HUMAN_GOVERNED_PARTICIPATION_PROFILE_v0.1.md), UC21, R01, los requisitos congelados y DDS no se modifican por esta nota.

**Pasajes fuente preservados:** [modelo consolidado v0.1](model/01_NOTAS_COMPLETAS.md#s1-p0518), [distancia y no duplicación](model/01_NOTAS_COMPLETAS.md#s1-p0573), [HID diferencial](model/01_NOTAS_COMPLETAS.md#s1-p0597), [experimentos de aceleración](model/01_NOTAS_COMPLETAS.md#s1-p0702), [anexo matemático v0.2](model/01_NOTAS_COMPLETAS.md#s1-p0805), [propuestas v0.3](model/01_NOTAS_COMPLETAS.md#s1-p0862), [reajuste v0.6](model/01_NOTAS_COMPLETAS.md#s1-p1008). Si un ancla de origen no se resolviese, la cabecera de sección del libro conservado sigue siendo la referencia documental; el texto fuente no se edita retroactivamente.
