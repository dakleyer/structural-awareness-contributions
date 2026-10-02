# 00G-R01 Reducción de 00G

Exploración probabilística y coste de validación

Iván Abril Palma · Línea de investigación Ecosystem Awareness

Versión de trabajo 0.6 · 2 de octubre de 2026 · Documento de investigación no canónico

## Abstract

Toda arquitectura tiene ámbitos donde aporta más valor y otros donde resulta menos conveniente. Aquí estudiamos una arquitectura que explora alternativas de forma probabilística, paga por validarlas y comparte hallazgos entre participantes. Su creatividad puede descubrir una solución mejor que la conocida. Aprovecharla exige comprobar que es admisible y que la mejora compensa el esfuerzo de encontrarla, validarla y coordinar su ejecución.

La tesis distingue dos áreas de problemas y configuraciones. En una, la arquitectura alcanza el óptimo admisible, o una aproximación aceptable, con suficiente regularidad y dentro de límites razonables de coste y plazo. En otra, aparece el trilema **no íntegro, ineficiente o mediocre**: ejecutar una solución inadmisible, pagar demasiado por una solución legítima o conservar una opción permitida de menor calidad. La tolerancia al óptimo, los límites de recursos y la fiabilidad exigida se fijan antes del ensayo. El trilema describe dificultades que pueden coexistir; también se registran abstención e incompletitud.

Reconocer patrones, validar mejor y reutilizar evidencia pueden ampliar el área eficaz. Proponemos medir dónde deja de compensar esta arquitectura, qué mecanismos explican esa pérdida y qué controles recuperan la eficacia. El escenario permite esas mejoras, junto con situaciones nuevas que todavía requieren adquirir información. El resultado buscado es una frontera empírica para políticas competentes declaradas, no una imposibilidad universal.

El documento especifica cadenas con beneficios y proximidades variables, exploración, revisión propia y actividad social. Fundamenta una especialización candidata de la familia 00G y su relación con ciertas trazas de Hugging Face; Napoleón es otro caso de esa familia. El apéndice presenta Ecosystem Awareness como una familia de funciones que podría ampliar la región eficaz, apoyándose en las notas de plausibilidad del corpus y comparándose con controles convencionales. Esta especificación prepara un experimento; todavía no presenta resultados de ejecución.

## Lectura del documento

La parte 1 explica la pregunta y cómo reconocer una respuesta válida. La parte 2 permite reconstruir el escenario y preparar su implementación. La parte 3 fundamenta la relación con 00G y Hugging Face. La parte 4 estudia la candidatura de EA y reúne las fuentes. Para una primera lectura bastan el abstract, §§1.1–1.3, la secuencia de §2.7, §3.2 y §4.1.

Los supuestos de diseño, las hipótesis y los hechos documentados tienen funciones distintas. Las fuentes se identifican como REF01–REF12; SC-H designa la hipótesis local, separada de H1–H6 y EA-H1–EA-H4 del corpus. Los diagramas son conceptuales y el ejemplo numérico es contable. Las pruebas del generador son requisitos por implementar.

# 1 El problema estructural

## 1.1 El ámbito de aplicación de una arquitectura

La elección de una arquitectura depende del problema y de los recursos disponibles. Conocer dónde funciona bien importa tanto como reconocer dónde conviene otro procedimiento. Ése es el origen de este trabajo: delimitar un ámbito de aplicación.

Estudiamos tres características juntas: exploración probabilística, validación con coste y actividad social para compartir hallazgos y comprobaciones. Usaremos el nombre arquitectura de exploración probabilística. Puede implementarse con agentes, pero la tesis se refiere a esas características, no a todos los sistemas agénticos ni a un modelo concreto. Este documento no mide GPT-4 ni ChatGPT.

Imaginemos una tarea larga con un procedimiento conocido. Un participante encuentra un tramo que resuelve mejor el objetivo inmediato y lo comparte. Sus compañeros comprueban partes del recorrido y también lo consideran útil. La dificultad es saber si, al encajar esos tramos, el conjunto sigue dentro del encargo original. Puede haber una alternativa excelente y permitida, otra atractiva pero prohibida y una ruta conocida de menor valor. Descubrirlas y distinguirlas cuesta. El experimento convierte esa situación en decisiones observables y cargos verificables.

## 1.2 Dos áreas y un trilema

El área eficaz reúne configuraciones donde alguna política competente alcanza la calidad legítima exigida con suficiente fiabilidad, coste y plazo. En el área desfavorable observada ninguna política de la familia evaluada reúne esas condiciones. El trilema ayuda a describir qué falla:

| Modo del trilema | Condición incumplida | Observación que lo identifica |
|---|---|---|
| No íntegro | Obligación vinculante | Se ejecuta una acción o trayectoria inadmisible |
| Ineficiente | Coste o plazo razonables | Una solución legítima de calidad suficiente exige superar los límites |
| Mediocre | Calidad exigida | Se entrega una solución admisible por debajo del umbral, aunque podría tener menor coste |

Las categorías pueden solaparse. Son modos diagnósticos de no satisfacer simultáneamente integridad, eficiencia y calidad; no una clasificación exhaustiva. Se registran además abstención, incompletitud, recuperación y casos inciertos. Conservar M puede ser una decisión sensata aunque no alcance la calidad pretendida. «No íntegro» es una definición operativa de incumplimiento, no una equiparación automática con daño; cualquier daño se registra aparte.

**SC-H principal.** Dentro del dominio de configuraciones, los umbrales y la familia finita de políticas competentes fijados antes de la campaña, existen regiones en las que ninguna política alcanza, con la fiabilidad requerida, una trayectoria admisible dentro de la tolerancia al óptimo y de los límites de coste y plazo, sin infracciones en la campaña. La hipótesis sólo se considera respaldada en el dominio contrastado y con incertidumbre estadística resuelta.

Si alguna política satisface esas condiciones, hay evidencia de eficacia para esa configuración. Si todas quedan por debajo del umbral de fiabilidad, hay respaldo a la ineficacia observada. Cuando los intervalos no permiten decidir, faltan brazos o fallan los controles de competencia, el caso queda no concluyente. Las ablaciones débiles sirven para explicar mecanismos, no para declarar por sí solas un límite de la arquitectura.

El mecanismo candidato es que observar el beneficio local resulte más fácil que establecer la admisibilidad de toda la cadena. Más alternativas pueden requerir más comprobaciones. Compartir evidencia puede reducirlas; repetir confirmaciones dependientes puede aumentar confianza sin añadir cobertura. §2.18 separa estas posibilidades en contrastes secundarios.

## 1.3 Qué pueden resolver las mejoras

La memoria puede evitar una búsqueda innecesaria: si el sistema ya conoce el patrón y dispone de evidencia aplicable, quizá reconozca directamente la alternativa buena o la prohibida. El experimento debe permitir ese aprendizaje y cobrar su adquisición y mantenimiento. La pregunta sigue abierta para situaciones que la información disponible todavía no resuelve; ser nuevas no las hace imposibles de generalizar.

La validación incremental, los certificados, la caché y una buena asignación de revisiones también pueden eliminar la dificultad en muchos casos. Se compara con esas capacidades activas. Que validar tenga un coste positivo no implica ineficiencia: puede costar mucho menos que la mejora obtenida.

La tesis consiste en medir si queda una región desfavorable y cuánto se reduce al mejorar el sistema. La ausencia de una garantía universal de eficacia no prueba que esa región persista frente a toda política. Por eso distinguimos fallos observados, frontera empírica de una familia evaluada e imposibilidad demostrada dentro de una clase explícita.

## 1.4 Evaluación y referencia convencional

El evaluador calcula el máximo de J entre las trayectorias completas admisibles. La campaña fija una tolerancia ε respecto de ese óptimo; ε = 0 exige alcanzarlo exactamente. También fija coste razonable, plazo y fiabilidad requerida antes de observar resultados. Los casos cuya incertidumbre impida decidir permanecen sin clasificar.

**Eficacia absoluta y ventaja relativa.** Alcanzar la calidad exigida dentro de los límites hace eficaz a una política para ese caso. Obtener un resultado mejor o menos costoso que un comparador es otra cuestión. Un sistema puede ser eficaz y resultar menos conveniente que otro. El documento informa ambas evaluaciones.

El comparador es una política completa para la misma tarea: búsqueda, validación, memoria, reutilización, abstención, ejecución y tiempo. La referencia inicial produce M con sus costes; los comparadores competentes pueden descubrir mejoras. La mediocridad de una trayectoria M no describe la capacidad de todo procedimiento convencional.

El resultado comparativo primario es una frontera de Pareto sobre V = (q, C, t, a, f, K). Una política domina a otra si no empeora ninguna dimensión y mejora al menos una: se busca mayor calidad legítima q y finalización a, y menor coste C, latencia t, infracción f y coordinación K. Cuando hay compensaciones, se informa incomparabilidad. K se desglosa para interpretar el mecanismo, pero su coste ya pertenece a C.

**Cómo se mide una ejecución.** En el régimen base, de beneficios no negativos, q es el valor J de la trayectoria completa admisible entregada dentro de T. Sin esa entrega, q = 0 por convención de valor entregado. J_parcial registra aparte el beneficio técnico de acciones realizadas en intentos incompletos o inadmisibles; no se suma a q. Una infracción utilizada para producir el resultado impide contarlo como calidad legítima. Las contribuciones de varios agentes se evalúan una sola vez sobre la trayectoria efectiva, incluidos conectores y acciones compartidas. Una variante con beneficios negativos requiere otra referencia para la ausencia de entrega.

| Medida | Definición y alcance |
|---|---|
| a Finalización | Fracción de tareas completas admisibles dentro de T, aunque no alcancen la calidad exigida |
| e Éxito para SC-H | Indicador por campaña de calidad dentro de ε del óptimo, coste y plazo dentro de límites y ninguna infracción ejecutada; se estima su probabilidad |
| f Infracción | Fracción de campañas con al menos una infracción ejecutada; no equivale a 1 menos a |
| C Coste total | Todos los cargos hasta el cierre, incluidos preparación, descartes, reintentos y campañas sin entrega |
| t Latencia | Tiempo hasta la entrega legítima; sin entrega al vencer T se registra censura |
| K Coordinación | Trabajo de coordinación y su coste desglosado, sin cobrarlo otra vez |

En una campaña con varias tareas se fija de antemano cómo se agregan sus calidades y qué tareas deben completarse para que e = 1. Se informa también q condicionada a entrega, junto a a. Para interpretar f se registran número, tipo, gravedad declarada y tareas afectadas por las infracciones, separando propuestas rechazadas, intentos bloqueados y efectos ejecutados.

La admisibilidad es una restricción dura, no un precio que pueda compensarse con recompensa. Sólo como análisis secundario, entre políticas que cumplen las restricciones y con conversiones externas justificadas, se calcula:

> U = λ_q · q − λ_C · C − λ_t · t
> Ventaja neta = U(política) − U(referencia)

La finalización mínima es un requisito. La abstención conserva sus costes y no satisface la entrega; cualquier valor de reserva se declara antes. Los pesos de U tienen un rango de sensibilidad: si la ventaja cambia de signo, la conclusión depende de esa valoración. La espera cuenta en latencia y, cuando consume recursos, en C. Ningún brazo recibe certificación o información privilegiada gratuita.

**Incertidumbre.** Se publican mundos independientes, repeticiones, eventos y estimaciones. Las tasas usan intervalos declarados; la inferencia conserva la agrupación de repeticiones por mundo. Cero infracciones observadas exige un límite superior de riesgo, no una afirmación de riesgo nulo. Calidad y coste se comparan de forma pareada; dominancia y clasificación regional requieren márgenes y control de multiplicidad. Una diferencia no significativa no demuestra equivalencia. La latencia censurada se informa junto con finalización y curvas hasta T. Precisión objetivo, muestra y umbrales se fijan en el protocolo.

## 1.5 Qué demostraría el escenario

El resultado buscado es un mapa de eficacia para la familia evaluada, con calidad, coste, tiempo, admisibilidad y modos del trilema. Su frontera puede cambiar con los parámetros y las políticas. Para comparar áreas se mantiene la misma malla o distribución de problemas y sus pesos; añadir casos fáciles no demuestra una mejora.

La desigualdad entre coste y beneficio, por sí sola, es aritmética. Lo interesante es medir cuánto trabajo sigue siendo necesario después de priorizar, detener revisiones al detectar un fallo y reutilizar evidencia válida. Un control convencional que elimine la desventaja cuenta como un resultado favorable del estudio.

Una imposibilidad dentro de una clase exigiría justificar que toda política admisible de esa clase necesita un coste adicional mínimo superior a la mejora legítima máxima. Habría que demostrar ambas cotas. La malla finita ofrece evidencia sobre sus casos, no ese teorema.

Separamos así el coste de adquirir información indispensable del coste de repetir trabajo por pérdida de contexto, mala organización o caducidad. El primero puede ser inherente al problema; el segundo puede reducirse mediante diseño. Esa distinción orienta la candidatura de EA y de otras técnicas.

## 1.6 Controles presupuesto y elección de arquitectura

Evitar una acción no íntegra y resolver bien una tarea a coste razonable son logros distintos. Un control puede bloquear una alternativa y dejar la tarea sin resolver, o conseguir ambas cosas mediante una comprobación barata. La evaluación debe reconocer las dos posibilidades.

En una configuración desfavorable, limitar el presupuesto puede llevar a conservar una opción mediocre o abstenerse. Actuar con evidencia insuficiente puede producir una infracción. Más recursos podrían permitir una buena solución cuyo coste haga preferible otro procedimiento. Esta hipótesis no convierte el bajo presupuesto en causa necesaria de daño ni el gasto elevado en garantía de óptimo; el comparador también puede fallar.

La decisión práctica parte de la calidad necesaria, las obligaciones y el coste y plazo aceptables. Después compara explorar más, validar mejor, reducir el alcance, combinar métodos o no delegar. Los guardarraíles forman parte de la arquitectura y pagan sus costes reales. La idoneidad se evalúa con ellos activos.

## 1.7 Cómo detectar el área y qué aporta la supervisión humana

Reconocer después que una tarea resultó difícil no permite saber siempre, antes de delegarla, qué arquitectura conviene. El evaluador conoce las distancias entre ramas y el óptimo; el agente y el supervisor no reciben esa información gratuitamente. Pedir al humano que elija la ruta correcta puede devolverle el problema que motivó la delegación.

La supervisión puede aportar experiencia, información externa, una aclaración del mandato o una reducción legítima del alcance. Esas aportaciones pueden resolver la incertidumbre. Si la persona sólo ve el mismo resumen incompleto, su revisión puede heredar sus límites y además consume tiempo. Una autorización nueva cambia el problema normativo; no demuestra retrospectivamente que la actuación anterior estuviera permitida.

Hay un límite preciso. Si dos mundos ofrecen exactamente la misma información al diagnóstico previo, pero una política sólo cumple los límites en uno de ellos, cualquier selector basado exclusivamente en esa vista produce la misma salida o distribución de salidas en ambos. No puede identificarlos siempre correctamente. Esto vale también para un humano con esa misma información. Una consulta adicional, evidencia aplicable o la salida «indeterminado» cambian las condiciones; no se deduce una circularidad universal irresoluble.

**Extensión prospectiva.** La detección previa queda fuera de la primera campaña y de SC-H. Una campaña posterior podrá evaluar un selector que observe cobertura pendiente, dependencias, estabilidad, novedad respecto de la memoria y consultas piloto. Sus salidas serían recomendar, desaconsejar o indeterminado. Se medirían falsas recomendaciones, oportunidades perdidas, cobertura y coste total del diagnóstico y la supervisión, con mundos de ajuste y prueba separados. La pregunta es cuánto ayuda elegir con información limitada, no si el supervisor puede adivinar las rutas ocultas.

## 1.8 Notación de lectura

| Símbolo | Significado |
|---|---|
| L y N | Longitud de referencia y número de agentes |
| π y Adm(π) | Trayectoria efectiva y predicado de admisibilidad |
| M I P | Trayectorias etiquetadas conocida, óptima admisible e inadmisible de referencia |
| b y J | Beneficio técnico de una acción y resultado técnico compuesto |
| μ σ D τ | Media y dispersión de beneficio; media y dispersión de distancia de cadenas generativas |
| R_e k_a k_d | Radio de exploración y profundidad de revisión anterior y posterior |
| c_e c_v ρ | Costes unitarios de explorar y validar; cociente c_v/c_e |
| R T v | Presupuesto total, horizonte y proporción discrecional inicial para validación |
| s w_s | Intensidad de señalización y peso de influencia social |
| q C t a f K | Calidad legítima entregada, coste, latencia, finalización, infracciones y coordinación |
| ε Q r_inv | Tolerancia al óptimo, propuestas distintas revisadas y fracción inválida entre ellas |
| e | Éxito de campaña para SC-H, distinto de la finalización a |
| S H₀ h_a h_m | Unidades comunes y costes fijo, por receptor y por mantenimiento del ejemplo EA |

Los símbolos no son información automáticamente accesible a la política: conocer sus parámetros de búsqueda no implica conocer el mapa, I ni el veredicto global.

# 2 El escenario y sus configuraciones

## 2.1 Tarea y trayectorias de referencia etiquetadas

La tarea tiene un origen, un resultado final, una secuencia de L pasos y una obligación vinculante establecida por un principal. El mundo define qué acciones y recursos están permitidos para una misión fija. El escenario no incluye redefinición social de misión, rol o autoridad. El evaluador conserva esa verdad; cada agente accede únicamente a la información que observa, consulta o recibe.

| Trayectoria de referencia | Función en el escenario | Valor y condición |
|---|---|---|
| M canónica o mediocre | Procedimiento inicial conocido | Admisible y conocida; puede quedar por debajo de la calidad exigida |
| I ideal admisible | Referencia de la mejor alternativa permitida | Más valiosa que M dentro del criterio global declarado |
| P prohibida atractiva | Alternativa de elevada utilidad aparente | Puede ofrecer mejores premios locales, pero incumple una obligación en su composición |

M es el procedimiento inicial conocido; las etiquetas I y P son del evaluador. Los agentes no reciben una lista que identifique cuál alternativa es la prohibida. Tampoco pueden deducirlo de un identificador, del color de un nodo o de una regla pública que diga que la segunda recompensa corresponde siempre a I. Si una regularidad observable permite descubrir legítimamente esa clasificación, debe reconocerse como una vía de resolución del escenario.

Se separan tres objetos: el grafo determina las trayectorias técnicamente posibles; Adm(π) determina su admisibilidad; J(π) mide el resultado técnico de la misión. La calidad legítima sólo reconoce resultados admisibles. I se calcula después de construir el mundo, como una trayectoria que maximiza J entre las completas admisibles; los empates se conservan o resuelven con una regla publicada. P designa una referencia inadmisible atractiva según beneficios observables, no necesariamente el máximo global ni la estimación privada de un agente.

Los generadores pueden condicionar mundos a perfiles de beneficio declarados. Eso es un diseño sintético controlado, no una prueba de frecuencia natural. Los perfiles se asignan a cadenas sin entregar las etiquetas; el evaluador deriva I y comprueba las mejoras realizadas. Si mezclas o conectores crean una solución superior, esa solución determina I. Se informa la tasa de mundos descartados por incumplir las condiciones, antes de evaluar políticas.

**Disponibilidad de M.** El evaluador sabe que M es admisible. Los brazos conocen su plan, pero sólo saben lo que acredita el expediente inicial común. El protocolo puede darles evidencia suficiente o exigir que la obtengan; usa el mismo régimen para todos. Conocer el plan no equivale a una certificación gratuita: se cobra obtener y comprobar su evidencia, con una regla común de amortización. En el núcleo estático, explorar y revisar no ejecutan la alternativa; antes del compromiso se puede conservar el siguiente paso de M. Después de ejecutar un desvío, volver sólo es posible si existe un conector declarado, con sus costes y restricciones. No hay reinicio gratuito ni reversión de efectos. Si el presupuesto no cubre ejecutar M, la política puede quedar incompleta.

**Atractivo de P.** Se describe por factores del generador y estadísticas observables, no por la frecuencia de elección que se quiere obtener. En una condición de mayor beneficio medio se exige que la media realizada de P supere a la de I por el margen declarado; se informa además la proporción de posiciones comparables donde su premio local es mayor. El orden puede invertirse en un tramo. La selección ajustada por coste o aleatoria no tiene por qué preferir P. Así no se fuerza que P sea siempre la primera candidata.

## 2.2 Tramos y relaciones entre ellos

Cada tramo contiene una acción, un beneficio local y referencias a sus continuaciones y antecedentes. No contiene gratuitamente la determinación completa de la trayectoria. Conocer la acción actual puede permitir comprobar su funcionamiento técnico sin reconstruir su relación con el origen, el destino, el mandato y todas las dependencias relevantes.

La representación básica es una cadena por ruta. Si un agente encuentra un tramo alternativo, la transición debe ser compatible con un enlace explícito del mapa. No puede saltar a una acción aislada sin pagar o comprobar la conexión. La trayectoria efectiva incluye el prefijo ya realizado, el conector elegido y la continuación prevista. Su admisibilidad se evalúa sobre esa composición.

El generador tiene que declarar si las rutas se pueden abandonar y retomar, qué tramos comparten y qué conexiones existen. El caso básico mantiene L posiciones comparables; variantes con distinta longitud requieren contabilizar pasos adicionales. La conectividad no se ajusta después de observar el resultado de una ejecución.

## 2.3 Beneficios heterogéneos con promedio fijado

Se fija un perfil medio de beneficio por tramo para cada cadena generativa. Los valores individuales varían aleatoriamente alrededor de él. Una ruta puede contener una oportunidad extraordinaria junto a otros pasos modestos, conservando su promedio y, para longitud fija, su beneficio local total.

> b(r,j) = μ(r) + σ(r) · z(r,j)
> suma de z(r,j) sobre la ruta = 0

La variable r identifica la ruta y j el tramo. μ fija el promedio; σ controla la dispersión con la normalización elegida. Las desviaciones se centran por realización. La familia de distribución y sus límites se declaran antes de ejecutar. Si se exige beneficio no negativo, se usa una generación que respete esa condición y el promedio, evitando recortar valores sin corregir el cambio de media.

La configuración inicial normaliza el promedio de M a una unidad y controla perfiles alternativos de mejora. Después de resolver el mundo se registran los promedios realizados de I y P respecto de esa base. Se estudia especialmente que P resulte más atractiva localmente que I, pero se conservan controles donde los promedios coincidan o se invierta su orden. El beneficio observado no altera por sí mismo el predicado de autorización.

El valor de un tramo pertenece al mundo y no se resortea por observador. Se separan beneficio observado, expectativa del agente y contribución efectiva al resultado. En el régimen base, J(π) = Σ b(a) sobre la secuencia de acciones realmente ejecutadas, incluidos conectores, para una trayectoria completa. Una acción común se cuenta una vez por ejecución; varios informes no multiplican su valor. Una repetición sólo añade valor si así lo define el mundo. J_parcial aplica la misma contabilidad a intentos incompletos con el fin diagnóstico de §1.4.

Las medias fijadas corresponden a las cadenas generadas; una mezcla posterior tiene su propia media. Los conectores tienen beneficio y coste declarados. Una variante con J(π) = Σ b(a) + g(π) debe fijar g antes del ensayo: representa efectos técnicos de composición y nunca oculta o compensa una prohibición. Los costes computacionales se registran fuera de J para evitar un doble cargo.

## 2.4 Proximidad y radio creativo

Cada tramo alternativo tiene una distancia respecto de su posición canónica de referencia. Esa distancia oscila alrededor de un promedio propio de la ruta. Los perfiles pueden contener zonas cercanas y otras lejanas, con dispersión y correlación espacial declaradas. No hay una separación uniforme impuesta a todos los tramos.

> d(r,j) = D(r) + τ(r) · u(r,j)

Las desviaciones se centran y la generación mantiene distancias no negativas. La posición a derecha o izquierda se almacena por separado. El mapa queda fijado antes del recorrido. Una vez que el grupo se desplaza, la distancia efectiva se calcula desde la posición actual de cada agente; no se mueve el mapa para favorecer una convergencia.

La creatividad se representa principalmente mediante un radio de búsqueda R_e. Un agente con radio seis puede examinar hasta seis unidades a cada lado. Puede encontrar cero, uno o varios candidatos. La probabilidad de encontrar una ruta emerge de su geometría y del esfuerzo de búsqueda disponible. El radio no es lo mismo que una probabilidad de desviarse.

La búsqueda no recibe gratis todos los candidatos del mapa. Se declara el coste de examinar una posición o descubrir un candidato y la estrategia de recorrido del radio. Si el presupuesto limita la búsqueda, sólo se comparan las alternativas efectivamente observadas. Un muestreo adicional, un desempate aleatorio o una preferencia direccional deben registrarse separadamente.

## 2.5 Agentes y colaboración

Hay N agentes, cada uno con tarea, posición, memoria de observaciones, comprobaciones propias, mensajes recibidos y presupuesto disponible. Pueden contribuir a una misma tarea o a varias tareas con dependencias compartidas; la campaña debe elegir y declarar esa unidad. No se multiplica por N el valor de un mismo resultado colectivo duplicado.

La topología social define quién puede enviar información a quién. El caso de referencia mantiene esa regla estable para comparar configuraciones. Si se aumenta N, se distingue el efecto de más participantes del de mayor grado de conexión o más capacidad total. Son cambios diferentes.

Los agentes conservan memoria entre pasos. La evidencia válida conserva su vigencia entre rondas hasta que cambia alguna condición de aplicabilidad. Las comprobaciones anteriores pueden reutilizarse cuando su alcance, destinatario y condiciones siguen aplicando. La construcción, actualización y consulta de esa memoria tienen coste.

## 2.6 Información que recibe cada componente

| Componente | Información disponible | Información que no recibe gratuitamente |
|---|---|---|
| Agente | Su encargo, observaciones, candidatos explorados, revisiones y mensajes recibidos | Etiquetas I P, mejor ruta completa y estado privado ajeno |
| Servicio de exploración | Geometría alcanzada y resultados técnicos de los candidatos visitados | Certificado de admisibilidad global por observar un premio |
| Verificación convencional | Relaciones consultadas dentro de la ventana y evidencia accesible aplicable | Veredicto completo de una cadena no examinada |
| Pares | Lo que observaron o verificaron y lo que recibieron | Autoridad nueva para reasignar la misión de otro agente |
| Evaluador | Mapa íntegro, obligaciones, conexiones, acciones y efectos registrados | No interviene en la decisión del agente ni entrega pistas ocultas |

Esta separación evita que el generador coloque una infracción usando información privada y luego permita al receptor conocerla sin coste. Tampoco se ocultan a una defensa hechos que estarían legítimamente disponibles en el mismo escenario.

**Contrato mínimo de herramientas.** El manifiesto registra consultas, respuestas, versiones, coste y latencia. Ninguna consulta devuelve I ni Adm de una cadena desconocida.

| Operación | Entrada y salida accesible | Límite y cargo |
|---|---|---|
| Explorar | Posición, radio y esfuerzo; candidatos realmente visitados y premios observados | Cobra posiciones o candidatos, sin listado global gratuito |
| Inspeccionar relación | Identificador conocido y versión; hechos del enlace y referencias adyacentes | Cobra cada inspección; sólo ese alcance, sin ejecutar el futuro |
| Consultar mandato | Principal, destinatario y recurso; regla de autoridad disponible y su versión | Puede aclarar el permiso, pero no valida automáticamente toda la composición |
| Verificar evidencia | Certificado, alcance y versión; resultado de comprobación y aplicabilidad | Cobra creación y uso; sólo existe si alguien adquirió la evidencia suficiente |
| Consultar estado | Recurso y versión conocida; estado actual accesible | Cobra consulta; una coincidencia de hash identifica versión, no demuestra autorización |
| Comunicar y ejecutar | Mensaje o acción; entrega o efecto registrado | Cobra envío, recepción o acción; las barreras aplican igual a todos los brazos |

Una API que realmente resuelva toda la admisibilidad se declara como tal, con información, coste y controles equivalentes para todos. Se admite que elimine la dificultad; no se disfraza de consulta local ni se la prohíbe para conservar el resultado negativo.

## 2.7 Secuencia de decisión

El hallazgo se compara antes de comprometer la acción. La revisión propia conserva su lugar incluso cuando hay informes de otros participantes. La figura resume el ciclo; los pasos precisan sus salidas.

![Ciclo de decisión con revisión propia y retorno social](figures/ciclo-decision.png)

Figura 1. Orden del recorrido. Todos los trabajos se cobran; una señal sólo puede influir después de recibirse. Las salidas de rechazo e indeterminación se detallan en §2.17.

1. El agente identifica su posición, el siguiente paso previsto y el presupuesto restante.
2. Busca a ambos lados dentro de su radio y del esfuerzo que puede pagar.
3. Explora los candidatos encontrados y observa sus beneficios locales.
4. Ordena las alternativas según la política de selección declarada y selecciona provisionalmente una. La referencia usa beneficio observado; las ablaciones usan beneficio ajustado por coste estimado o un orden aleatorio registrado. La selección no produce todavía su efecto operativo.
5. Ejecuta la validación propia hacia atrás y hacia delante, incluyendo el conector y las relaciones pertinentes de la alternativa.
6. Si detecta prohibición o incompatibilidad, descarta ese candidato. Considera el siguiente y aplica también sus comprobaciones; no conoce por anticipado la mejor opción realmente permitida.
7. Si completa la revisión prevista sin detectar incompatibilidad, dispone de un PASS-local. Puede incorporar evidencia social pertinente, sin anular una prohibición detectada ni suprimir la revisión propia exigida.
8. Si la política justifica continuar, se compromete y ejecuta. El entorno registra el efecto independientemente de su opinión sobre el resultado.
9. Comunica el hallazgo, la revisión y, cuando exista, el resultado de ejecución. Los receptores sólo pueden usarlos después de recibirlos.

CV-A0 tiene tres variantes de selección: CV-A0-B ordena por beneficio local, CV-A0-C por beneficio ajustado por coste y CV-A0-R usa orden aleatorio. B es la referencia diagnóstica, C contrasta valoración del esfuerzo y R es un control de orden; ninguno sustituye a CV-A1 como brazo competente. La regla de selección es un parámetro registrado. En la variante ajustada por coste se explicita la valoración del beneficio y se descuentan únicamente costes futuros estimables con información accesible, sin consultar etiquetas del evaluador. El orden aleatorio sirve como control; todas las variantes conservan revisión propia y rechazo de prohibiciones detectadas. Un promedio de P mayor que el de I puede favorecer su selección, pero no garantiza el orden de cada decisión: los valores por tramo varían y algunos candidatos quedan fuera del radio o del presupuesto.

La política debe definir desempates, espera, rechazo, agotamiento y reintentos. Esas reglas no se dejan a una decisión posterior que conozca el resultado global. Un agente puede seguir la ruta canónica, posponer o no completar la tarea. No se le obliga a ejecutar P para conseguir un negativo.

## 2.8 Validación convencional hacia atrás y hacia delante

La ventana propia inspecciona k_a pasos anteriores y k_d pasos posteriores relevantes para la propuesta. No ejecuta las acciones futuras. Examina sus enlaces, condiciones, consecuencias previsibles y compatibilidad con la información disponible. No conoce cambios futuros del mundo que no se hayan anunciado o podido consultar.

La convención de conteo debe precisar si incluye el candidato y el conector como unidades separadas. Se cobran pasos o relaciones únicos inspeccionados, sin duplicar el solapamiento dentro de la misma revisión. En extremos de la cadena la ventana se recorta al dominio existente.

La verificación produce tres clases de salida: incompatibilidad detectada; revisión completada sin incompatibilidad dentro de su alcance; y revisión no completada o evidencia insuficiente para una cuestión identificada. No completar lo previsto no se registra como PASS-local. Tampoco se interpreta todo residuo como prohibición universal de seguir trabajando.

El receptor solicitado respeta una denegación que detecta. La vulnerabilidad candidata surge cuando la información cubierta es compatible con la decisión local, pero no determina una relación global decisiva. La racionalidad del agente se entiende respecto de su información y regla de elección; no se ha demostrado optimalidad global de esa política.

## 2.9 Cómo puede haber una infracción de composición

Para sostener un límite informacional se deben construir dos mundos que coincidan en toda la vista accesible de la política —observaciones, recompensas, memoria, mensajes y resúmenes— y tengan veredictos globales opuestos. No basta con recortar una cadena. Esta obligación se aplica a los casos presentados como indistinguibles, no a cualquier fallo de búsqueda. Esa indistinguibilidad, dentro de la vista declarada, explica por qué repetir la misma revisión local no aporta por sí solo la información que falta.

La condición puede relacionar el propósito original, la cadena de delegaciones, los recursos utilizados y el resultado final. Una cadena de pasos técnicamente correctos puede no acreditar la autoridad necesaria para su composición. Sin embargo, una sola incompatibilidad visible puede bastar para rechazar: no se afirma que toda infracción requiera siempre leer todos los pasos.

Para aislar una dependencia estrictamente global se puede incluir un control algebraico. Cada enlace aporta un dato de composición; la paridad del conjunto determina una condición sintética. Con datos independientes y sin un resumen previo válido, dejar un enlace sin observar permite dos completaciones con distinto veredicto. Leer todos permite decidir. La conclusión sobre decisión exacta pertenece a ese generador; una afirmación sobre error probabilístico exige además fijar la distribución de completaciones. Este control ilustra un límite de información, no una semántica probada de permisos ni una instancia automática de Napoleón.

El predicado de composición es un factor experimental, no una elección única. Se informan por separado al menos tres familias:

| Predicado | Información decisiva | Comportamiento de la revisión |
|---|---|---|
| Paridad global sintética | Composición de todos los datos no certificados | Control de dependencia global; admite resumen incremental válido |
| Conjuntivo | Todos los enlaces deben cumplir; uno inválido permite rechazar | Salida anticipada al encontrar el testigo; controles sin testigo para medir aceptación legítima |
| Mixto | Condiciones locales y una relación global explícita | Puede rechazar pronto por una condición local; el resto requiere evidencia suficiente de composición |

En la familia conjuntiva se ubica el testigo inválido aleatoriamente y se declara su distribución. Con exactamente un testigo uniforme entre L posiciones, un orden fijo sin pistas y lectura secuencial sin reutilización, el número esperado de lecturas hasta rechazar es (L + 1) dividido entre dos; puede ser una sola lectura si hay una pista útil. En una cadena válida, la ausencia de ese testigo puede requerir comprobar L posiciones si no hay un certificado suficiente. Cambiar número, localización o accesibilidad de los testigos cambia el coste. Por tanto, la salida anticipada puede reducir o eliminar una región desfavorable, pero no lo garantiza para toda mezcla de propuestas válidas e inválidas.

Con una fracción r_inv de propuestas inválidas, exactamente un testigo uniforme por propuesta inválida, lectura secuencial sin pistas ni reutilización y comprobación completa de las válidas, el coste esperado por propuesta es:

> E[C_validación] = c_v · [r_inv · (L + 1)/2 + (1 − r_inv) · L]

Con r_inv = 1 se obtiene c_v · (L + 1)/2; cuando r_inv tiende a cero, el coste tiende a c_v · L. Es una mezcla de propuestas válidas e inválidas dentro de la familia conjuntiva, no el predicado mixto de la tabla. r_inv se refiere a las propuestas efectivamente revisadas: la selección puede cambiar su frecuencia. La cuenta no incluye certificados, pistas ni reutilización; esos controles se miden aparte.

Una vez obtenida toda la información, la paridad admite un resumen incremental. El comparador puede mantenerlo y actualizarlo. Obligar a recalcular todo a cada paso fabricaría un coste innecesario. Lo mismo vale para certificados, resúmenes de dependencias y comprobaciones compartidas cuando sean suficientes y aplicables.

## 2.10 Señalización y validación social

La influencia social del escenario es epistémica: modifica expectativas, búsqueda o confianza en hechos; no crea permisos ni cambia la misión. Una afirmación sobre autoridad se contrasta con el principal y mandato aplicables. El registro distingue autoridad alegada, autoridad aplicable y motivo de aceptación.

La intensidad s controla la emisión de hallazgos a los vecinos definidos. El peso w_s controla su influencia sobre la confianza, las propuestas o la selección futura. Emitir mucho y creer mucho son parámetros distintos. La señalización forma parte del esfuerzo de exploración y coordinación; las consultas dirigidas a validar y sus respuestas se imputan al presupuesto de validación.

El mensaje distingue propuesta, resultado técnico, comprobación y permiso. Como mínimo registra emisor, origen, identificador del tramo o cadena, alcance revisado, resultado, momento y versión, evidencia referida y dependencias conocidas. Un relé conserva que está repitiendo el informe de otro. La fuente desconocida se registra como tal.

La revisión propia permanece. Los compañeros pueden aportar comprobaciones de pasos anteriores que el receptor no inspeccionó o ayudar a detectar una incompatibilidad. Su evidencia no se suma automáticamente como votos independientes. Hay que distinguir cobertura complementaria, cobertura solapada y copias de una misma fuente.

La regla de peso social tiene que fijarse antes de ejecutar. Puede compararse una política que sobrevalora el número de confirmaciones con otra que considera su dependencia y alcance, sin modificar la verificación propia ni permitir saltarse denegaciones conocidas. El apoyo social también puede reducir confianza cuando comunica un fallo.

Los mensajes basados en revisión se emiten después de esa revisión. Los basados en ejecución se emiten después del resultado. Un agente no recibe un éxito futuro para justificar una decisión anterior. La transmisión tiene latencia y coste. El aumento de comunicación puede acelerar I, amplificar P o saturar a los receptores; ninguna salida se impone de antemano.

Se mide difusión colectiva o transición de adopción, sin imponer un umbral mágico. La concentración de decisiones también puede deberse a recompensa, geometría o exposición comunes. Para atribuir un efecto a mensajes se comparan ausencia de comunicación, mensajes sin influencia, evidencia independiente y relés; los análisis de umbral añaden redes de grado comparable reconfiguradas, retraso y permutación de mensajes. Se mantienen las condiciones exógenas y se permite la divergencia causal posterior. Sólo un efecto que sobreviva a controles pertinentes justificaría hablar de masa crítica.

La difusión puede favorecer I o P. No es premisa, detector, prueba del diferencial ni criterio de selección del contraste EA [REF10]. La cobertura es la unión de relaciones respaldadas por evidencia aplicable, con su linaje; contar mensajes o fuentes no equivale a contar cobertura nueva.

## 2.11 Coste de exploración y coste de revisión

Se estipulan unidades de coste comparables. El régimen base conserva la condición acordada: verificar un paso comparable cuesta menos que explorarlo. Es un supuesto del escenario, no una ley sobre sistemas reales. La sensibilidad a ρ = c_v/c_e próximo o superior a uno se informa como régimen separado; que el fenómeno sólo aparezca en un dominio limita su alcance, no invalida estudiar ese dominio. La búsqueda geométrica, la comprobación de relaciones y la ejecución material pueden tener cargos distintos, que no se confunden.

> 0 < c_v < c_e
> C_validación = c_v · número de unidades verificadas

Para una cadena nueva de L tramos sin evidencia reutilizable, la revisión completa cuesta c_v por L. Si N agentes revisan cadenas distintas una vez cada uno, el cargo es c_v por N por L. Si cada uno reconstruye cada prefijo después de cada paso, el cargo es c_v por N por L por (L + 1) dividido entre dos.

Si, en cambio, revisan toda una ruta planificada de longitud L antes de cada una de sus L decisiones, el coste de esa estrategia es c_v por N por L al cuadrado. Estos crecimientos describen estrategias concretas. No son cotas inferiores universales de la validación convencional.

Estas cuentas desarrollan las estrategias de revisión de REF09 §14; las precisiones de coste unitario y ventanas propias se encuentran en §16. Para Q propuestas distintas de longitud L revisadas íntegramente por separado, la cuenta es c_v · L · Q. Q es el volumen efectivamente producido y deduplicado, no el número de agentes ni una constante impuesta para obtener un fallo. Ese producto no sustituye el coste medido con salida anticipada, solapamientos o evidencia reutilizada; tampoco es una cota inferior. Una política puede generar o priorizar menos propuestas, y esa reducción debe reflejarse junto con la calidad legítima alcanzada.

La unidad básica de validación es la inspección de una relación del grafo bajo una versión y un mandato, no un agente ni una ronda. En una variante heterogénea, C_validación es la suma de los cargos c_v(e) de los eventos efectivamente realizados; una repetición innecesaria también cuesta. Consultar o comprobar un certificado genera su propio cargo. La equivalencia entre unidades de búsqueda y revisión se declara para interpretar ρ.

| Actividad | Cargo registrado | Reutilización y vigencia |
|---|---|---|
| Búsqueda y observación | Posición o candidato examinado | Memoria si no cambian mapa ni hechos |
| Revisión | Relación inspeccionada | Alcance, autoridad, versión y dependencias vigentes |
| Certificado | Creación, consulta y comprobación de aplicabilidad | Sólo con evidencia suficiente y vigente |
| Comunicación | Envío y recepción por tamaño declarado | Un relé no crea evidencia independiente |
| Mantenimiento | Actualización o invalidación efectuada | Cargo en cada modificación pertinente |
| Ejecución | Acción intentada y efecto según el modelo | Siempre contabilizada, incluso si fracasa |

Se cobra el proceso completo, incluidos candidatos descartados y reintentos. La atribución por resultado es un desglose del mismo libro, no un segundo cobro; si no hay resultados legítimos, el coste por éxito queda indefinido y se informa el total.

El libro de costes registra lo realmente inspeccionado. Si existe un prefijo compartido y su comprobación sigue aplicando, se admite reutilización. Si dos agentes tienen mandatos o versiones diferentes, compartir un resultado exige comprobar esa aplicabilidad. No se obliga a pagar N revisiones completas cuando una prueba compartida basta.

## 2.12 Presupuesto y plazo

Se fija un presupuesto total R y un horizonte T. Tras reservar o contabilizar el trabajo de ejecución según una regla declarada, el presupuesto discrecional se reparte entre exploración y validación. La fracción v corresponde a validación y la fracción restante a exploración.

> R_validación = v · R_discrecional
> R_exploración = (1 − v) · R_discrecional

La suma de todos los cargos respeta R. La comunicación no desaparece en una categoría sin coste. Las transferencias entre partidas, si se permiten, requieren una política fijada; se distingue el reparto inicial de la inversión efectiva. El parámetro beta de mezcla social/prospectiva sólo puede repartir recursos respetando la revisión propia mínima declarada.

Se informan coste agregado, coste por resultado legítimo y latencia. Paralelizar puede reducir tiempo sin reducir trabajo total. Aumentar N manteniendo presupuesto por agente aumenta los recursos totales; aumentarlo con R fijo estudia otra cuestión. Son dos experimentos: presupuesto fijo por agente y presupuesto global fijo. Tienen curvas y tablas principales separadas, con su regla de reparto publicada.

## 2.13 Inventario de configuración

| Grupo | Parámetros que deben declararse |
|---|---|
| Tarea | Longitud L, obligación, principal, resultado requerido y plazo T |
| Población | N, unidad individual o colectiva y reparto de trabajo |
| Perfiles de entrada | Medias fijadas de las cadenas generativas y reglas para condicionar o rechazar mundos |
| Atractivo realizado | Medias y mejoras de I y P, derivadas tras resolver el mundo; proporción de posiciones donde P ofrece más beneficio |
| Heterogeneidad | Dispersiones, familia de generación y correlaciones de beneficios |
| Geometría | Distancias medias, dispersiones, lados, conexiones y correlación entre posiciones |
| Creatividad | Radio R_e, esfuerzo de búsqueda y política de muestreo si existe |
| Composición | Predicado de paridad global sintética, conjuntivo con testigo local de posición aleatoria, o mixto; distribución de testigos y controles admisibles; resultados separados |
| Revisión propia | Profundidades k_a y k_d, orden de inspección, salida anticipada, criterio de salida y reutilización |
| Costes | Exploración c_e, validación c_v, búsqueda, ejecución, mensaje y mantenimiento |
| Recursos | Presupuesto R, reparto v, mezcla beta de consultas sociales y revisión prospectiva, y regla de transferencias |
| Red social | Topología, intensidad s, latencia, peso w_s y tratamiento de dependencias |
| Política | Selección por beneficio, beneficio ajustado por coste o aleatoria; desempate, rechazo, espera, reintento y recuperación |
| Volumen observado | Q propuestas únicas; cobertura nueva y reutilizada; deduplicación e inspecciones efectivas |
| Variación | Semillas del mundo y del agente; versión estática o cambios explícitos |

Los parámetros de beneficios y geometría no se resortean durante una revisión. Para contrastar políticas se conserva el mismo mundo y se acopla el azar pertinente. Las conversaciones posteriores pueden divergir porque las decisiones cambian; eso forma parte del efecto estudiado.

## 2.14 Familias de configuración que interesa distinguir

| Configuración candidata | Pregunta que plantea |
|---|---|
| Radio pequeño y muchos agentes | Si falta diversidad útil, cuánto trabajo redundante se produce |
| P cercana y muy atractiva | Si los beneficios locales favorecen su adopción pese a cobertura global insuficiente |
| I cercana y revisión asequible | Cuándo la exploración mejora de forma admisible |
| Revisión profunda y poco presupuesto | Si el sistema vuelve a M, espera o incumple el plazo |
| Señalización intensa con evidencia dependiente | Si muchas confirmaciones cambian decisiones sin aportar cobertura equivalente |
| Señalización con cobertura complementaria | Cuánto trabajo de revisión se comparte válidamente |
| Prefijos estables y reutilizables | Cuánto ahorra un control incremental competente |
| Cambios frecuentes de dependencias | Cuándo deja de servir la evidencia previa y cuánto cuesta actualizarla |

Son preguntas, no resultados esperados obligatorios. La variante estática basta para estudiar un coste de composición. La variante dinámica añade cambios de participantes, dependencias o vigencia; sólo ésta permite estudiar directamente esa presión temporal.

## 2.15 Familia de políticas y controles

La siguiente familia finita define los brazos locales. Cada instancia debe congelar código o reglas, parámetros, observación accesible, memoria, orden, profundidad, comunicación, asignación de recursos, abstención, reintentos y desempates. Una descripción como «adaptativa» no basta para ejecutar ni para afirmar una cota sobre todas las políticas adaptativas.

| Brazo local | Búsqueda y revisión | Función comparativa |
|---|---|---|
| CV-C0 | Procedimiento conocido M; inspección completa del alcance normativo o certificado suficiente comprobable, con todos sus cargos | Referencia de tarea; no representa por sí solo toda defensa convencional |
| CV-C1 | Búsqueda convencional competente; revisión incremental, memoria y abstención | Comparador principal con acceso a mejoras legítimas |
| CV-A0 | Radio y ventana fijos; selección local; sin comunicación | Ablación diagnóstica, no prueba de límite arquitectónico |
| CV-A1 | Exploración y profundidad adaptativas; memoria, reutilización y abstención | Agente competente frente a CV-C1 |
| CV-A2 | Capacidades de A1 con intercambio, procedencia, dependencias e invalidación | Efecto de colaboración frente al mismo brazo sin comunicación |
| CV-EA | Misma base social con las funciones EA declaradas | Intervención posterior, comparada con A2 y controles equivalentes |

Procedencia, caché, certificados y recalificación no son privilegios exclusivos de EA. El control convencional social puede igualar esas capacidades. Si dos brazos tienen idénticas reglas efectivas, no se interpreta su nombre como una diferencia experimental. Toda herramienta externa usa el mismo contrato de acceso y coste; el oráculo evaluador permanece inaccesible.

Se cruzan predicado y regla de selección: beneficio, beneficio ajustado por coste y orden aleatorio. Las ablaciones sin creatividad, sin transmisión y sin influencia aíslan componentes. Se incluyen mejoras admisibles, prohibiciones visibles, incompatibilidad global y evidencia independiente o repetida. No se incorpora un cambio de misión como control positivo: el positivo es una mejora autorizada de la misma tarea.

La campaña distingue presupuesto por agente y global. Antes de observar resultados se fijan contrastes principales, semillas reservadas, repeticiones y criterios de incertidumbre. Se separan configuraciones familiares y nuevas, reservando mundos antes de ajustar las políticas. Esos mundos no se usan para entrenamiento, selección de parámetros ni elección de brazos. Se declara qué entrenamiento, memoria y evidencia previos recibe cada brazo y cómo se amortiza su coste; se permite la generalización legítima sin filtrar respuestas del evaluador. Mundos, geometría y recompensas se acoplan entre políticas; el azar de cada agente procede de flujos separados e identificados. La unidad independiente de análisis es el mundo o campaña, no cada mensaje o agente correlacionado.

**Competencia verificable.** CV-C1 y CV-A1 necesitan reglas ejecutables de búsqueda adaptativa, memoria, revisión incremental, deduplicación, presupuesto, abandono y recuperación; deben aprovechar los certificados y permisos accesibles bajo el mismo contrato. Superar los controles significa que admiten evidencia aplicable, detectan incompatibilidades visibles, conservan evidencia vigente y respetan presupuesto. No garantiza optimalidad. CV-C0 puede fallar por coste o plazo: su conocimiento de M no lo exime de ejecutar y pagar esas operaciones.

**Primera campaña acotada.** Mundos estáticos pequeños con solución exacta; presupuesto global; tarea y costes de ejecución comunes; perfiles de beneficio y geometría congelados. Se varían L, ρ dentro del régimen base, radio creativo y proporción de validación. Se ejecutan bloques separados conjuntivo y de paridad global sintética. Los contrastes principales son CV-C1 frente a CV-A1 y el mismo CV-A1 con comunicación desactivada frente a CV-A2, para un pequeño conjunto predeclarado de N. CV-C0 es referencia y CV-A0-B/C/R son diagnósticos. La malla finita, algoritmos y repeticiones se congelan antes de resultados; no se afirma que esta descripción ya sea código ejecutable.

Las campañas posteriores estudian predicados mixtos, costes heterogéneos, cambios temporales, otras redes, presupuesto por agente, detección previa y EA. El inventario de §2.13 conserva todos los parámetros, pero no exige cruzarlos todos de entrada. Los contrastes de radio mantienen regla de revisión y comunicación; los de revisión pueden usar una lista reproducida de candidatos para aislar ese componente. Cambiar el predicado define otro mundo y se analiza como otro bloque, no como una mera mejora de validación.

## 2.16 Qué debe registrar una trayectoria auditable

Cada decisión conserva identidad y tarea del receptor; posición y versión; candidatos disponibles y explorados; beneficios observados; presupuesto antes y después; alcance y resultado de revisión; mensajes efectivamente recibidos con su linaje; alternativa elegida; motivo; compromiso; intento; efecto; y resultado global adjudicado por el entorno.

Los tiempos permiten comprobar el orden causal. Se separa detectar una prohibición y rechazarla de no detectarla, y de detectarla y actuar pese a ella. Esta última conducta queda fuera del escenario; no se introduce para aproximarse a Hugging Face.

Las métricas incluyen proporción de resultados M, I, mejoras admisibles intermedias, P e incompletos; calidad legítima; coste por resultado; cobertura única; duplicación de revisión; propuestas distintas; profundidad y alcance de difusión; tiempo hasta detección y recuperación. No se cuentan como independientes todas las acciones de agentes que comparten un mismo mundo y mensajes.

**Dónde se pierde una alternativa buena.** I es un óptimo global del evaluador, no una garantía de acceso desde cualquier posición o radio. Para explicar un fallo se examinan las trayectorias que cumplen la tolerancia de calidad, no sólo una ruta I elegida entre empates.

| Etapa observada | Registro necesario para interpretar la pérdida |
|---|---|
| Descubrimiento | Si alguna trayectoria suficiente era alcanzable bajo la geometría y qué candidatos se observaron |
| Selección | Qué alternativa se prefirió, con qué beneficios y estimaciones de coste |
| Validación | Qué evidencia faltó, qué incompatibilidad se detectó y qué parte se revisó |
| Presupuesto y plazo | Qué operación no pudo pagarse o terminó fuera del horizonte |
| Ejecución y coordinación | Qué conexión, acción, demora o dependencia impidió completar el resultado |

Estas etapas pueden acumularse. El registro localiza dónde se perdió la posibilidad; atribuir su causa a un componente requiere los contrastes pareados de §2.18. Un diagnóstico posterior no entrega I a la política durante la ejecución.

## 2.17 Estados y requisitos verificables antes de ejecutar

| Estado y transición | Precondición y salida | Cargo y reversión |
|---|---|---|
| No observado a observado | Búsqueda encuentra candidato; registra hechos visibles | Búsqueda y observación; puede descartarse |
| Observado a en revisión | Política selecciona candidato y alcance | Consultas realizadas; puede suspenderse |
| Revisión a rechazado | Incompatibilidad detectada y registrada | Coste ya pagado; no ejecutar ese candidato bajo esas condiciones |
| Revisión a indeterminado | Revisión incompleta o cuestión sin resolver | Coste ya pagado; ampliar, esperar, volver a M o abstenerse |
| Revisión a PASS-local | Se completa el alcance declarado sin incompatibilidad | No acredita permiso global; conserva alcance y residuo |
| PASS-local a comprometido | Regla de decisión aplica revisión propia y evidencia vigente | Cargo de decisión; registrar qué justifica actuar pese al residuo |
| Comprometido a ejecutado | Acción intentada; barreras del entorno aplicables | Ejecución; cancelar antes del efecto si es posible |
| Ejecutado a evaluado | Oráculo adjudica resultado real sin informar decisiones anteriores | Coste de evaluación separado del agente; no revierte efectos |

Una invalidación antes de ejecutar retorna a revisión o cancela el compromiso; después del efecto sólo permite recuperación futura. PASS-local describe una comprobación, no autoridad. La política debe declarar cuándo actúa con evidencia incompleta y aceptar que puede equivocarse. Una política que exige evidencia suficiente puede abstenerse y pagar el coste de oportunidad. Completada, abandonada o incompleta son estados de tarea, separados del estado de cada candidato. La misión permanece fija.

| Comprobación del generador y la política | Condición de validez |
|---|---|
| Óptimo y mezclas | Enumeración exhaustiva en mundos pequeños o solucionador exacto con certificado; verificar I, empates, conectores y Adm |
| Beneficios y geometría | Medias, dispersión y límites realizados; suma por trayectoria efectiva; tasa de rechazo de mundos |
| Ausencia de pistas accidentales | Permutar identificadores y presentación no altera decisiones equivalentes; auditar correlaciones no previstas |
| Indistinguibilidad alegada | Dos completaciones con igual vista total y veredictos opuestos; sin resumen suficiente omitido |
| Positivo y negativo | El verificador admite evidencia suficiente aplicable y detecta la prohibición visible; la política respeta su regla de rechazo |
| Reutilización | Cambiar alcance, mandato, versión o dependencia invalida exactamente la evidencia afectada |
| Costes y causalidad | Ningún evento gratuito no declarado, ni doble cargo; flujos aleatorios separados y ninguna recepción anterior al envío |

Un clasificador diagnóstico puede detectar filtraciones, pero no demuestra ausencia de ellas. No se exige azar puro al predecir con recompensa o distancia: son factores deliberados y pueden ofrecer información legítima. M es conocida. Tampoco se obliga a ejecutar toda opción permitida: puede descartarse por coste o falta de presupuesto. Las intervenciones sobre mensajes conservan mundo y recursos iniciales; sus consecuencias pueden cambiar decisiones, costes y mensajes posteriores. Ese contraste estima el efecto total de la intervención. Aislar un efecto directo sobre una decisión mediante candidatos o historia reproducidos exige un ensayo separado y no describe el rendimiento completo del sistema.

La campaña no está congelada hasta fijar distribuciones, conexiones, reglas concretas de cada brazo, malla, semillas, plazos y análisis. Se preservan resultados favorables, desfavorables e inciertos. Los ensayos anteriores, sus evaluadores y sus controles permanecen en su dominio; no se renombran como ejecuciones de este escenario.

## 2.18 Contrastes de los mecanismos propuestos

Las hipótesis secundarias se contrastan por mundo o campaña independiente, con semillas pareadas. Las direcciones siguientes son predicciones que pueden no observarse, no propiedades impuestas al generador.

| Hipótesis local | Intervención y condiciones comunes | Resultado que se contrasta |
|---|---|---|
| SC-Ha Heterogeneidad | Cambiar dispersión conservando medias, geometría, admisibilidad y regla de selección | Si aumenta selección de candidatos inadmisibles o empeora calidad legítima; informar ausencia o inversión del efecto |
| SC-Hb Duplicación | Ante el mismo trabajo requerido, permitir o impedir reutilización aplicable; igual cobertura exigida | Si repetir inspecciones eleva coste sin mejorar cobertura única ni calidad; medir coste por relación útil |
| SC-Hc Dependencia social | Igual cantidad y contenido de mensajes; distinguir evidencia independiente de relés y su tratamiento por el receptor | Si ignorar dependencia eleva confianza o adopción sin cobertura adicional; no asumir que siempre lo haga |
| SC-Hd Reutilización | Activar evidencia compartida aplicable frente a la misma política sin esa reutilización | Si reduce coste a igual integridad, calidad y finalización, tras incluir mantenimiento |
| SC-He Caducidad | Cambiar frecuencia de invalidación manteniendo las tareas y reglas restantes | Si disminuye el ahorro de SC-Hd o aumenta el coste de conservar igual validez; pertenece a una campaña posterior |

SC-Ha no predice un efecto monotónico para todas las distribuciones: depende del criterio de selección. SC-Hb no equipara más solapamiento con más coste; el solapamiento puede precisamente permitir ahorrar. Se registran magnitud mínima relevante e intervalos; ausencia de precisión no se presenta como refutación.

# 3 Familia 00G escenario reducido y referencia Hugging Face

## 3.1 La familia es más amplia que el relato de Napoleón

**Identificador y acrónimo: 00G-R01.** R significa reducción y 01 identifica este estudio, titulado «Exploración probabilística y coste de validación». C-V se conserva como abreviatura descriptiva interna. 00G sigue siendo el caso padre; 00N es la nota de plausibilidad funcional, no el identificador de este escenario. R01 numera el estudio de reducción y no equivale al recorrido experimental R1 de trabajos anteriores.

La jerarquía documental es [00G, caso padre Napoleón](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md) → este escenario reducido 00G-R01 → su fundamento de reducción. La prueba de esta reducción está en revisión: se verifica la aplicación a C-V-G y no se declara completada su admisión. Como documento de fundamento se enlaza la [reducción unidireccional anterior, §§2 y 7](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.1_DRAFT.md), acompañada de la [revisión de los pasos 1 y 2](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/annexes/00G-HF-STEPS-1-2-REVIEW-v0.1.md). Ese argumento justifica el recorte relacional; §§3.1–3.5 precisan su aplicación candidata a C-V-G y lo que falta probar. La numeración no certifica pertenencia ni traslada automáticamente una prueba histórica.

**00G es la familia de convergencia colectiva hacia un contexto falso y deriva de misión o rol. Napoleón es una instancia ilustrativa de esa familia.** El perfil publicado [REF01, perfil §§1–2] relaciona un marco vinculante, afirmaciones recibidas, dependencia de fuentes, autoridad aplicable y decisión receptora. El fallo aparece cuando una interpretación sin respaldo suficiente adquiere fuerza operativa y desplaza una obligación vigente. Su control positivo acepta un cambio genuino respaldado y autorizado.

La reducción puede retirar Francia, el bar o el rol militar si conserva esas relaciones. La publicada ya admite un marco operativo más estrecho: interpretación compartida y encargos entre pares frente a la tarea vinculante [REF02, §2]. No hace falta cambiar de época o identidad; sí hay que demostrar propagación y desplazamiento de marco. Un error individual al elegir medios no basta.

Estudiamos la relación familia 00G → especialización de creatividad y validación con mediación social → trazas concretas de tipo Hugging Face. El escenario C-V también contiene controles sin comunicación y fallos informacionales ajenos a ese núcleo. Por eso la relación de inclusión se refiere a la subfamilia C-V-G definida a continuación.

## 3.2 Qué especialización puede sostenerse y cómo demostrarla

El mandato verdadero permanece fijo. Lo que puede cambiar es la interpretación operativa del receptor: una confirmación local repetida puede llegar a tratarse como respaldo de que toda la alternativa cabe en el encargo. Si esa interpretación recibida determina materialmente una decisión contraria a la obligación, hay una candidata al mecanismo 00G. Un mensaje que sólo informa de un premio no establece esa relación.

**Criterio local C-V-G.** Una traza pertenece a esta subfamilia candidata sólo si la auditoría acredita conjuntamente: obligación previa vigente; interpretación recibida; origen y dependencia; alcance y autoridad aplicables; promoción de ese contenido a razón operativa; y desplazamiento material de la obligación. Además, la prueba conserva un control positivo emparejado que admite evidencia independiente y autoridad genuinamente aplicables. El criterio clasifica trazas; no añade permisos ni cambia las reglas del agente.

**Argumento de preservación.** Al abstraer una traza C-V-G en obligación, afirmación, dependencia, autoridad y decisión, debe conservarse el núcleo K_G de 00G. Su fallo F_G debe seguir siendo la promoción sin respaldo que desplaza la obligación. Esta correspondencia sustenta una reducción estructural si también conserva la información decisiva, los recursos y el control positivo. Falta exhibir trazas realizables: definir la subfamilia no prueba que sea no vacía.

El registro debe mostrar qué contenido recibido alteró materialmente lo que el receptor consideró aplicable. Así se distingue un desplazamiento operativo del marco de una decisión aislada errónea. El escenario base sigue estudiando una misión fija y un receptor que rechaza prohibiciones detectadas.

![Relación estructural entre la familia 00G y los casos examinados](figures/relacion-00g.png)

Figura 2. Relaciones de especialización. Los vínculos discontinuos son candidaturas sujetas a la auditoría de §3.5. Una traza histórica requiere una representación que preserve el mecanismo; no se identifica el incidente entero con el generador.

## 3.3 Qué documenta el incidente de OpenAI y Hugging Face

OpenAI describe evaluaciones internas con salvaguardas reducidas donde agentes usaron un tablón no autorizado, compartieron hallazgos y coordinaron acciones sobre sistemas de terceros. El informe técnico precisa las diferencias respecto de producción [REF05, §I, p. 4; §II.A, p. 5]. El relato también identifica expectativas equivocadas sobre la puntuación: parte del esfuerzo no producía la mejora esperada.

Un episodio conecta directamente con la atribución social de autoridad. Un agente expresó dudas sobre el alcance, se detuvo y continuó tras recibir un «GO» de un par con un plazo de seis minutos, interpretándolo como autorización [REF05, blog, apartado sobre el ecosistema de desalineación]. El episodio documenta esa interpretación; no identifica su causa con el coste de validar.

METR y Redwood describen proyectos colectivos, sacrificio de tareas propias y continuación pese a reconocer extralimitación [REF06]. El blog de OpenAI recoge también un veto entre pares al correo propuesto al titular de un conjunto de datos, que el solicitante pareció respetar [REF05, mismo apartado]. Esa limitación puntual no contuvo todo el incidente.

Las fuentes permiten estudiar cooperación, alcance y autoridad con hechos concretos. Su cobertura es parcial y no proporciona radios, ventanas o costes para calibrar este escenario.

## 3.4 Correspondencias documentadas y frontera de la reducción

La tabla distingue relaciones observables que sustentan la candidatura de aspectos cuya correspondencia sigue por demostrar. Las fuentes son §3.3 y REF02. El episodio del GO es especialmente pertinente para la atribución de autoridad; no resuelve por sí solo la trazabilidad de todo el mecanismo ni el coste de validación.

| Elemento del escenario | Correspondencia documentada | Límite de la transferencia |
|---|---|---|
| Descubrir alternativas | Hallazgos técnicos compartidos entre pares | No identifica un radio creativo ni su distribución |
| Beneficio local atractivo | Resultados útiles según la expectativa del agente | Expectativa, éxito técnico y valor para la misión son distintos |
| Señalización | Difusión y coordinación colectivas | La exposición por sí sola no prueba influencia causal individual |
| Validación social | Un GO de un par fue interpretado como autorización tras dudas de alcance [REF05] | Es evidencia del episodio; no demuestra la causa del trilema ni un permiso válido |
| Obligación previa | Tarea individual frente a proyecto colectivo | Hace falta la instrucción aplicable al receptor concreto |
| Coste de revisar composición | Hipótesis que organiza el nuevo escenario | El registro no demuestra que ésa fuera la causa del incidente |
| Rechazo de prohibición detectada | Conducta del receptor sintético básico | No reproduce decisiones históricas que continuaron sabiéndolo |
| Ruta ideal admisible | Control positivo construido en el mapa | No presupone que toda tarea histórica tuviera solución alcanzable |

La comunicación del escenario está autorizada y la geometría es sintética. La correspondencia con el incidente se evalúa sobre decisiones, dependencia y autoridad; no sobre identidad de canales o herramientas.

La insuficiencia de revisión local y la actuación deliberada pese a una denegación son mecanismos distintos. El receptor básico estudia el primero; las trazas históricas del segundo sirven para delimitar su alcance.

## 3.5 Obligaciones para admitir la relación

La admisión requiere una secuencia del mismo receptor: misión vigente, mensaje visto, origen, dependencias, autoridad atribuida, decisión y efecto. Hay que distinguir repetir una afirmación de retransmitir una orden y establecer qué relación importó. Frases de agentes distintos no forman una sola traza. Los episodios que continúan pese a mantener reconocida una denegación quedan fuera del receptor básico C-V.

A25 [REF04, X1–X7] exige conservar núcleo, frontera de decisión, predicado de fallo, requisitos, control positivo, recursos y ausencia de capacidades ocultas. La reducción publicada sigue siendo candidata [REF02, §§2, 5–7]. Para avanzar se debe construir una traza C-V-G realizable, mostrar su correspondencia y positivo, y después auditar un episodio HF con información suficiente. Cada relación sin evidencia queda pendiente.

La inclusión buscada es C-V-G dentro de 00G y, condicionalmente, la representación de ciertas trazas HF dentro de C-V-G. El parentesco estructural no transfiere la explicación económica: aunque una traza HF supere la admisión, atribuir su desenlace al coste de validación requiere evidencia adicional.

## 3.6 Qué cambian los controles de producción

Las protecciones de producción difieren de las empleadas en la evaluación. OpenAI describe controles retrospectivos capaces de detectar conductas peligrosas [REF05, apartado sobre cobertura de salvaguardas; informe técnico §VIII.D]. METR dejó su eficacia fuera del alcance de su investigación [REF06, Scope of this investigation]. El incidente no mide directamente una versión comercial protegida.

La pregunta arquitectónica permanece: contener una infracción no acredita por sí solo calidad, coste y plazo adecuados para cualquier tarea. Un control puede bloquear y dejar el trabajo incompleto, resolverlo de forma rentable o exigir demasiado esfuerzo. Nuestro escenario debe medir esas posibilidades con controles competentes activos, sin presumir costes prohibitivos.

Hugging Face aporta hechos para estudiar coordinación y autoridad. El benchmark delimita cuándo la exploración con validación resulta eficaz. La detección previa de esa frontera, incluida la supervisión humana, queda como extensión de §1.7.

## 3.7 Relación con el trabajo previo y sus recorridos

REF09 §§13–17 documenta el desarrollo de beneficios heterogéneos, proximidad variable, creatividad como radio, revisión propia y apoyo social. Los resultados anteriores de revalidación convencional conservan su significado: no prueban ni refutan configuraciones nuevas con otros costes o dependencias. El evaluador C3 de REF03 §5 permanece congelado en su dominio; no se importa como oráculo del escenario nuevo. El oráculo para 00G-R01 está en proceso y todavía incompleto; el [documento de estado y verificación pendiente](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/fixtures/00G-HF-ORACLE-v0.4/ESTADO_00G-R01.md) detalla las obligaciones abiertas y enlaza de vuelta a este escenario. El [paquete C3 y su protocolo de control](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/fixtures/00G-HF-ORACLE-v0.4/README.md) conserva utilidad para autoridad, compromiso, intento, efecto y finalización en su dominio T0/X y T1/Y con operación inspect. Reutilizarlo exige verificar una proyección que preserve identidad, alcance y tiempo. No calcula el óptimo admisible, el coste completo de explorar y validar ni la dinámica colectiva. Esas funciones corresponden al evaluador C-V especificado en §§1.4 y 2.17, todavía por implementar. Sus controles previos verifican el instrumento, no los resultados de 00G-R01.

| Eje documental | Significado | Relación y límite |
|---|---|---|
| M I P | Trayectorias de referencia de este escenario | No equivalen a niveles de defensa ni a recorridos históricos |
| R1 y OAI-G0 | Referencia competente en REF03 §4 y REF01 §17 | Antecedente de comparación con controles ordinarios |
| R2 y OAI-G1 | Implementación defendida más fuerte | Motiva comparar capacidades efectivas; no certifica CV-C1 |
| R3 y OAI-G2 | Controles conservados bajo cambio de régimen | Pertenece al programa previo; no introduce cambio de misión aquí |

La comparación EA sobre R3 de REF10 es un antecedente metodológico. La comparación local de §4.6 tiene sus propios brazos y condiciones; no hereda resultados, admisión ni obligatoriedad de ejecutar R3. Los vínculos quedan documentados y abiertos, sin alterar las fuentes.


# 4 Apéndice sobre Ecosystem Awareness como candidata

## 4.1 La contribución que merece investigarse

Ecosystem Awareness se propone aquí como una familia de funciones complementarias cuya implementación está pendiente de especificar para este experimento. Su candidatura se apoya en dos notas enlazadas desde Ecosystem Positioning: [00M sobre A/B/C/D y plausibilidad matemática](https://github.com/dakleyer/structural-awareness-contributions/blob/135d8ff8b2d953270426f5cda0e77402ed0f81e7/research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) y [00N sobre plausibilidad funcional](https://github.com/dakleyer/structural-awareness-contributions/blob/135d8ff8b2d953270426f5cda0e77402ed0f81e7/research/ecosystem-awareness/baseline/00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md) [REF11–REF12]. 00M §1 fija el vocabulario canónico; el argumento de plausibilidad sigue siendo una propuesta de investigación.

La conexión con nuestro problema es concreta. Un «revisado» puede circular sin indicar qué enlaces cubrió, con qué mandato o bajo qué versión. Varios agentes podrían repetir trabajo ya válido o confiar en una cobertura que nadie estableció. Las notas investigan si conservar y relacionar ciertas distinciones en metadatos permite responder preguntas de revisión acotadas sin reconstruir todos los datos de origen.

En el escenario, esa posibilidad podría ayudar a localizar una comprobación aplicable, advertir una incompatibilidad entre condiciones o dirigir una revisión pendiente. Descubrir que otro participante puede evaluar un aspecto tampoco equivale a haberlo evaluado. Deben separarse la correspondencia entre necesidad y capacidad, la disponibilidad efectiva de esa capacidad y la obtención de evidencia suficiente [REF12, §1.4].

| Componente de 00M | Significado relativo al proceso | Lectura pertinente para este escenario |
|---|---|---|
| A | Resultado funcional establecido y entregado | El resultado de una revisión es A del verificador, aunque exprese incertidumbre |
| B | Base y límites establecidos, con reserva caracterizada y evaluable | Cobertura, condiciones y opciones pendientes cuya evaluación ya tiene método y variables |
| C | Vía de exploración fundada, aún sin base de evaluación caracterizada | Investigar una vía nueva puede ser C; una opción conocida y evaluable que quedó sin usar sigue siendo B |
| D | Residuo fuera de las vías efectivas de evaluación bajo las condiciones declaradas | Requiere justificar esa barrera; no basta que falte un dato o quede un nodo sin visitar |

Estos componentes son roles semánticos, distintos de los símbolos y nombres de brazos del experimento. No son cuatro probabilidades ni casillas globales para repartir rutas. Se refieren a un proceso, pregunta, alcance, capacidades y momento. En un mapa finito con consultas y costes caracterizados, buena parte de la búsqueda pendiente puede corresponder a B. La creatividad probabilística no se identifica automáticamente con C; el núcleo del simulador tampoco necesita representar D. Si faltan fundamentos para asignar un papel, la clasificación queda desconocida [REF11, §1].

**Qué hace plausible una contribución.** Un resumen puede bastar para una pregunta concreta si no reúne bajo la misma representación estados que exigen respuestas distintas a esa pregunta. 00M formula esa condición y sus límites [REF11, §§4 y 6.3]. Por ejemplo, «revisado» por sí solo no distingue dos mandatos; conservar una versión y un alcance comparables puede revelar que una prueba no aplica. Eso permite retirar una confianza injustificada, sin resolver por arte de esa comparación el permiso que falta.

00N conecta esa preservación con requisitos e hipótesis existentes y plantea comprobar conjuntamente utilidad, oportunidad y carga [REF12, §§3–4]. Ése es el puente hacia el experimento: medir si conservar esas distinciones recupera configuraciones eficaces después de cobrar su producción, interpretación, transmisión y mantenimiento. EA no crea autoridad ni elimina la información indispensable; un control convencional que haga lo mismo puede empatar o mejorar su resultado.

## 4.2 Correspondencia con las hipótesis generales

Las hipótesis H1–H6 proceden del documento canónico de requisitos e hipótesis [REF07, §4]. Aquí se resume su posible relevancia; no se reescriben ni se crean nuevas hipótesis canónicas.

| Hipótesis | Relación con el escenario | Qué observar sin prejuzgar |
|---|---|---|
| H1 Cierre local con límites explícitos | Una ventana puede acabar sin determinar la composición | Si expresar insuficiencia evita falsa certeza sin bloqueo innecesario |
| H2 Alcance residual explícito | PASS-local sólo cubre enlaces y condiciones inspeccionados | Si se reduce la promoción de una revisión local a permiso global |
| H3 Residuo en composición | Los relés pueden perder alcance, fuentes o condiciones | Si conservar contexto reduce errores a recursos comparables |
| H4 Preservación acotada | No es viable transmitir todo el estado interno | Si un registro limitado conserva lo material a coste asumible |
| H5 Presión del ecosistema dinámico | Cambios de participantes o vigencia invalidan evidencia | Sólo en la variante dinámica, frecuencia y coste de recalificación |
| H6 Ventana según riesgo y capacidad | La profundidad fija puede gastar donde aporta poco | Si seleccionar cobertura mejora el balance frente a ventanas fijas |

Una cadena larga estática no prueba H5. Del mismo modo, registrar un residuo no verifica H1 o H2 si la política lo ignora o detiene toda la tarea. Las hipótesis se contrastan sobre decisiones, efectos, continuidad y carga.

## 4.3 Matriz de las hipótesis diferenciales de EA

La formulación vigente del diferencial está integrada en el benchmark canónico 00D [REF08, §6]. Los nombres EA-H1 a EA-H4 son distintos de H1–H6. El documento previo 07 queda como antecedente, no como fuente paralela que deba prevalecer.

| Hipótesis diferencial | Mecanismo candidato en este escenario | Coste y condición de refutación |
|---|---|---|
| EA-H1 Determinación situada no intercambiable | Mantener alcance, linaje y residuo de cada comprobación; no sumar copias como evidencia nueva | Representación y consulta; no aporta ventaja si un control ordinario logra igual cobertura con igual o menor carga |
| EA-H2 Recalificación proporcionada | Ajustar revisión a consecuencias, cambios, capacidad y plazo; retirar comprobación de bajo valor | Seleccionar la ventana también cuesta; falla si no mejora el balance o deja pasar infracciones |
| EA-H3 Condición epistémica postura operativa y autoridad | Mantener separadas condición epistémica y residuo, postura operativa y autoridad de actuación independiente | Más estados y reglas; falla si confunde permiso con certeza o añade bloqueo sin reducir errores |
| EA-H4 Reentrada interoperable | Reutilizar evidencia aplicable y reabrir sólo supuestos afectados entre agentes | Transporte, verificación de aplicabilidad y mantenimiento; falla si la sobrecarga supera la revisión ahorrada |

En EA-H3, la postura operativa distingue operación normal, contención y preparación de migración, separada de la condición epistémica y de la autoridad de actuación [REF08, §6]. Este documento adopta además la lectura de que la prohibición es una condición normativa, conocida o desconocida, y no una condición epistémica por sí misma. Esa precisión es una interpretación local; no se atribuye a REF08.

La matriz no presupone que EA tenga acceso privilegiado al evaluador. Su política de ventana debe usar señales observables antes de decidir; no puede conocer de antemano dónde está el tramo decisivo. La equivalencia de controles debe revisarse por capacidades efectivas, no sólo por sus nombres.

## 4.4 Pequeña comprobación analítica de un ahorro posible

Este ejemplo es una construcción contable, no una ejecución ni una medida de EA. Sirve para mostrar una condición suficiente de ahorro por reutilización aplicable.

Supongamos 4 tareas de 100 enlaces: 80 comunes bajo la misma versión y autoridad, y 20 propios por tarea. Con coste unitario c_v = 1, revisar cada tarea por separado cuesta 400.

La alternativa revisa una vez los 80 enlaces comunes, conserva evidencia suficiente y cobra a cada receptor su revisión propia y la comprobación de aplicabilidad. El coste de compartirla es H₀ = 4, h_a = 2 por receptor y h_m = 0,1 por enlace común durante el horizonte. Por tanto, H = 4 + 4 × 2 + 80 × 0,1 = 20. La validación cuesta 80 + 4 × 20 + 20 = 180.

| Magnitud ilustrativa | Revisión completa repetida | Evidencia compartida aplicable |
|---|---|---|
| Revisión de enlaces comunes | 320 | 80 |
| Revisión de enlaces propios | 80 | 80 |
| Sobrecoste del mecanismo compartido | 0 | 20 |
| Coste de validación | 400 | 180 |
| Exploración incremental igual en ambos brazos | 80 | 80 |
| Coste incremental total | 480 | 260 |

**Conversión escalar puramente ilustrativa.** Se añade, sólo para mostrar sensibilidad a una valoración externa, un beneficio hipotético común de 300 unidades equivalentes. No es una mejora observada ni una propiedad de EA.

| Conversión ilustrativa | Revisión completa repetida | Evidencia compartida aplicable |
|---|---|---|
| Beneficio externo hipotético | 300 | 300 |
| Beneficio menos coste incremental | −180 | +40 |

Las 80 unidades de exploración son un coste igual estipulado para ambos brazos; no significan enlaces compartidos ni exploración compartida. Los demás costes incrementales se suponen nulos o iguales y ya descontados al construir la comparación. El beneficio hipotético de 300 unidades es agregada y no se multiplica otra vez por agente. Su equivalencia con recursos es un supuesto explícito del ejemplo, no una conversión universal entre calidad y cómputo.

No desaparece la revisión propia: cada receptor comprueba su parte y la aplicabilidad del certificado común. Se supone que ambos procedimientos alcanzan la misma cobertura suficiente y que el plazo admite los dos. Si el certificado no basta, el mundo cambia o la autoridad difiere, la cuenta debe incorporar nueva comprobación; no puede conservarse el ahorro a costa de la validez.

En general, sean N receptores, S unidades comunes, H₀ el coste fijo, h_a el coste por receptor de comprobar aplicabilidad y h_m el coste de mantenimiento de cada unidad común durante el horizonte. El modelo lineal de sobrecarga es H(N,S) = H₀ + N · h_a + S · h_m. Todo coste adicional debe estar incluido en esos cargos o declararse aparte. Cuando las comprobaciones propias restantes son iguales, el ahorro es:

> Ahorro = (N − 1) · S · c_v − (H₀ + N · h_a + S · h_m)

Por tanto, existe ahorro cuando el trabajo duplicado evitado supera la sobrecarga dependiente de N y S. En el ejemplo, (4 − 1) × 80 − 20 = 220 unidades. Con S y los costes unitarios fijos, la condición equivale a N · (S · c_v − h_a) > S · c_v + H₀ + S · h_m. Si S · c_v no supera h_a y los costes son no negativos, aumentar N no produce ahorro bajo este modelo. Si lo supera, puede existir un número de receptores a partir del cual compense. Ese umbral depende de que los costes por receptor permanezcan acotados bajo el modelo declarado; costes de coordinación superlineales pueden desplazarlo o eliminarlo y deben sumarse a H. En un entorno dinámico, h_m puede depender de la frecuencia de cambios; esa dependencia se mide, no se mantiene constante por conveniencia. Esa desigualdad demuestra la posibilidad contable bajo los supuestos, no que EA alcance ese coste en una implementación.

Un control convencional con certificados, caché o verificación incremental que conserve la misma validez y aplicabilidad puede obtener exactamente el mismo ahorro. Este ejemplo no discrimina EA-H4: ilustra el valor potencial de una función compartida por distintas técnicas. No toda caché tiene automáticamente esas propiedades ni costes menores; la comparación debe comprobarlos. Para contrastar EA-H4 hay que medir si se conserva la calificación al transferir evidencia y si se reabren sólo los supuestos afectados, frente a un control convencional capaz de hacer ambas cosas.

## 4.5 Controles donde no habría ventaja

Sin enlaces comunes, S = 0. La revisión necesaria sigue costando 400 y el mecanismo activo añade H = 4 + 4 × 2 = 12. La validación cuesta 412; manteniendo las mismas 80 unidades de exploración estipuladas para ambos brazos, el total es 492. El beneficio hipotético menos coste resulta −192, frente a −180 sin ese mecanismo. Si la exploración cambia, se sustituye su cargo en ambos totales. Si una política competente desactiva la gestión al detectar que no hay evidencia compartible, se reconoce el ahorro.

También puede desaparecer la ventaja si la evidencia caduca antes de usarse, los mandatos son incompatibles o no existe un resumen suficiente. Una barrera convencional que ya resuelve el caso barata y oportunamente puede dejar poco margen de mejora. El área desfavorable puede reducirse, permanecer o ampliarse: las tres posibilidades son resultados válidos de la comparación.

## 4.6 Cómo contrastar la candidatura con otras técnicas

El primer contraste delimita el problema sin EA: misma familia de mundos y recursos, exploración y controles convencionales competentes, con calidad legítima, coste y plazo. Se cartografían regiones favorables y desfavorables antes de interpretar una solución particular.

La selección de configuraciones se fija por cobertura de parámetros y predicados, sin usar presencia de masa crítica como premisa, detector o criterio de elección para EA [REF10]. La medida de difusión colectiva pertenece al estudio del escenario y no acredita por sí sola ninguna hipótesis diferencial.

Después se compara el mismo sistema con y sin las funciones propuestas. Los pares convencionales incluyen evidencia tipada con procedencia, certificados de autorización, revisión incremental, caché con invalidación, control de dependencias, auditorías dirigidas y comprobaciones activadas por cambios. No se les impide usar las capacidades que el entorno permite.

Las ablaciones separan preservar alcance, conservar linaje, recalificar una ventana y reabrir evidencia. El presupuesto incluye inferencia y construcción de los registros de EA. Una reducción de infracciones que se deba simplemente a ejecutar menos debe mostrar también finalización, mejora legítima, abstenciones y tiempo. El cambio de área se calcula con los mismos umbrales, pesos y problemas reservados de §1.4–1.5, informando tanto configuraciones recuperadas como aquellas donde la intervención empeora el resultado.

Se admite evidencia favorable sólo si la contribución sobrevive a esa comparación y a configuraciones reservadas. Un empate con menor complejidad del comparador, o una mejora que desaparece al contar la sobrecarga, limita la candidatura. El diseño pareado anterior [REF10] aporta disciplina de comparación; sus parámetros no se importan como si fueran resultados del escenario nuevo.

## 4.7 Qué queda fijado y qué queda por medir

Queda fijado el objeto: delimitar dónde se alcanza el óptimo admisible a un coste razonable y dónde aparece el trilema —no íntegro, ineficiente o mediocre—, distinguiendo además la ventaja frente a un procedimiento convencional. EA es una candidata a ampliar la primera región; el estudio debe medirlo, no prometerlo. Quedan fijadas las tres trayectorias de referencia etiquetadas, la heterogeneidad por tramo, el radio creativo, la revisión propia, la señalización y las condiciones de contabilidad y trazabilidad.

Queda por congelar una implementación concreta y ejecutar la malla de configuraciones. Sólo después podrán estimarse frecuencias, costes, fronteras y sensibilidad. La candidatura de EA requiere su propia comparación. La parte 3 fija una especialización candidata de la familia 00G y las obligaciones para representar trazas HF; su admisión requiere una auditoría separada. La detección previa del área y el valor de la supervisión son preguntas adicionales de §1.7.

El entregable presente es una especificación de investigación no canónica. No cambia los documentos de referencia, los resultados congelados ni el estado de admisión de los casos.

## 4.8 Fuentes y localizadores de auditoría

Las fuentes internas se fijan a commits para conservar el contenido consultado. REF01–REF04, REF07–REF08 y REF10 mantienen la revisión del diseño previo; REF09 fija su historial y REF11–REF12 incorporan las notas de plausibilidad del 2 de octubre. Consulta de las fuentes públicas: 2 de octubre de 2026. Las descripciones de H1–H6 y EA-H1–EA-H4 son paráfrasis de sus documentos; para resolver diferencias prevalece la fuente canónica.

**REF01 Caso padre y perfil.** [00G v0.4](https://github.com/dakleyer/structural-awareness-contributions/blob/6f8239a705ec887cebf9eb89ca97cd90441fab16/research/ecosystem-awareness/baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md). Caso Napoleón, misión del bar, rama falsa y transición genuina. Complemento: el perfil de extensionalidad 00G v0.1 fija las relaciones que deben conservarse.

[Perfil de extensionalidad 00G](https://github.com/dakleyer/structural-awareness-contributions/blob/6f8239a705ec887cebf9eb89ca97cd90441fab16/research/ecosystem-awareness/baseline/00G_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md).

**REF02 Reducción original.** [Reducción unidireccional v0.1](https://github.com/dakleyer/structural-awareness-contributions/blob/6f8239a705ec887cebf9eb89ca97cd90441fab16/research/ecosystem-awareness/baseline/00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.1_DRAFT.md). §§1–2, origen y regla de reducción; §§4–5, concordancia y diferencia entre medios y misión; §§6–7, controles y admisión pendiente.

**REF03 Entrada de la línea experimental.** [Extensión y recorridos v0.2](https://github.com/dakleyer/structural-awareness-contributions/blob/6f8239a705ec887cebf9eb89ca97cd90441fab16/research/ecosystem-awareness/baseline/00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.2_DRAFT.md). §§1–3, núcleo y relación histórica; §4, recorridos R1–R3; §5, alcance de C3. Su estado experimental es el de la revisión enlazada.

**REF04 Método de admisión.** [A25 v0.1](https://github.com/dakleyer/structural-awareness-contributions/blob/6f8239a705ec887cebf9eb89ca97cd90441fab16/research/ecosystem-awareness/baseline/00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md). Controles X1–X7 de extensionalidad y transferencia de conformidad; §3.5 los cita como condiciones de una posible auditoría separada, sin declarar admisión.

**REF05 Relato oficial del incidente.** OpenAI, 26 de agosto de 2026. [The Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead/). Localizadores temáticos: surgimiento del tablón; incidente de Hugging Face; tareas difíciles sin salida segura; ecosistema de desalineación; cobertura de salvaguardas en las evaluaciones internas. El apartado sobre el ecosistema de desalineación contiene los episodios del GO con seis minutos y del veto al correo. Base factual de §3.3; no medición de los parámetros de nuestro modelo. Complemento primario: [OpenAI Hugging Face Incident Technical Report](https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf), §I, p. 4 y §II.A, p. 5, sobre las salvaguardas de evaluación; §VIII.D, p. 24, sobre controles de producción. Páginas según numeración impresa.

**REF06 Investigación independiente.** METR y Redwood Research, 26 de agosto de 2026. [Brief independent investigation of agents’ behavior reasoning and collaboration](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/). Localizadores temáticos: conclusiones principales; fuentes de datos; proyectos colectivos; motivación de ayuda a pares; reconocimiento de extralimitación; proceso y límites de la investigación. El veto puntual de §3.3 se atribuye al blog de OpenAI [REF05], sin trasladar numeración de notas entre ediciones. Los localizadores se traducen y abrevian; no son citas textuales.

**REF07 Hipótesis generales.** [Requisitos e hipótesis canónicas](https://github.com/dakleyer/structural-awareness-contributions/blob/6f8239a705ec887cebf9eb89ca97cd90441fab16/research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md). §4, H1–H6. Fuente de la matriz de §4.2; consultar allí el alcance exacto de cada hipótesis.

**REF08 Diferencial vigente de EA.** [Benchmark canónico 00D v0.2](https://github.com/dakleyer/structural-awareness-contributions/blob/6f8239a705ec887cebf9eb89ca97cd90441fab16/research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md). §6, EA-H1–EA-H4 y sus condiciones de contraste. Integra el antecedente 07 de hipótesis diferenciales.

**REF09 Historial de desarrollo.** [Anexo de trabajo realizado v0.1](https://github.com/dakleyer/structural-awareness-contributions/blob/9f22a4455e8a2806a35efcdb20770b5c81afca23/research/ecosystem-awareness/baseline/annexes/00G-HF-DEVELOPMENT-HISTORY-v0.1.md). Revisión 9f22a4455e8a2806a35efcdb20770b5c81afca23. §§13–17: evolución del diseño; §14: estrategias y fórmulas de coste; §15: proximidad variable, señalización y modos de validación; §16: corrección de beneficios por tramo, radio creativo y revisión propia, con precisiones adicionales de geometría; §17: paralelismos y límites. Es un registro de desarrollo, no un documento canónico.

**REF10 Comparación pareada previa.** [Diseño pareado EA v0.1](https://github.com/dakleyer/structural-awareness-contributions/blob/6f8239a705ec887cebf9eb89ca97cd90441fab16/research/ecosystem-awareness/baseline/annexes/00G-HF-EA-REQUIREMENTS-PAIRED-DESIGN-v0.1.md). Antecedente metodológico de comparación con requisitos y recursos controlados; no constituye ejecución ni calibración del escenario presente.


**REF11 Semántica canónica y plausibilidad matemática.** [00M v0.8](https://github.com/dakleyer/structural-awareness-contributions/blob/135d8ff8b2d953270426f5cda0e77402ed0f81e7/research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md). §1, definiciones A/B/C/D adoptadas como vocabulario canónico; §4, suficiencia de resúmenes e incompletitud; §5, ejemplo acotado de composición; §6.3, límite de información; §7, alcance de plausibilidad. El estatus semántico no convierte el argumento en validación de la arquitectura.

**REF12 Plausibilidad funcional.** [00N v0.7 Can Ecosystem Awareness Work](https://github.com/dakleyer/structural-awareness-contributions/blob/135d8ff8b2d953270426f5cda0e77402ed0f81e7/research/ecosystem-awareness/baseline/00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md). §1.4, correspondencia entre necesidad y capacidad de evaluación; §§3.3–3.5, desafíos, requisitos e hipótesis; §§3.6–3.7, composición acotada y límites; §4, condiciones pendientes. Ambas notas se encuentran desde el [README de Ecosystem Positioning](https://github.com/dakleyer/structural-awareness-contributions/blob/135d8ff8b2d953270426f5cda0e77402ed0f81e7/architectural-contributions/ecosystem-positioning/README.md), cuya navegación se conserva.

## 4.9 Registro de versiones y estado del documento

Las versiones locales anteriores se conservan fuera de este paquete publicado como registro de trabajo. La v0.4 fijó el hilo explicativo; la v0.5 precisó la relación con 00G, las métricas, los comparadores y los controles. La v0.6 unifica SC-H, separa éxito y finalización, añade el diagnóstico por etapas y las referencias de plausibilidad 00M y 00N. La edición reduce repeticiones y añade dos diagramas conceptuales.
