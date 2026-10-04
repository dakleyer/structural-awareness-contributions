# Trilema condicionado de coste, riesgo y eficacia en R01

Iván Abril Palma · Ecosystem Awareness · Desarrollo matemático de viabilidad

Versión 0.1 · 4 de octubre de 2026 · Reconstrucción simbólica propia; revisión independiente pendiente.

Fuente R01: `Escenario-creatividad-validacion.md`, versión 0.6, leída en el commit `2d299250a1e9d8103757f3841c73fdb01db82598`. Este documento desarrolla un teorema sobre su dominio de configuraciones. No modifica la especificación experimental, los incidentes, los fixtures ni los resultados históricos.

## 1. Qué se demuestra

El resultado es un **trilema condicionado en R01**: existen familias de configuraciones R01 donde los tres pares coste–riesgo, coste–eficacia y riesgo–eficacia son alcanzables, con los mismos umbrales, pero ninguna política admitida consigue las tres condiciones. Existen también familias viables. La imposibilidad se demuestra para todas las políticas de las configuraciones difíciles, no para una selección de algoritmos.

El dominio del teorema es R01 completo. La condición que identifica una región difícil no se impone a todas sus configuraciones. Memoria, certificados suficientes, dependencias compartidas, APIs resolutivas, búsqueda, geometría, colaboración y recuperación siguen dentro del dominio. Pueden hacer que una configuración deje de satisfacer esa condición y pase a ser viable. Eso es compatible con el resultado.

Hay tres aportaciones separadas: (i) un certificado de imposibilidad aplicable a cualquier manifiesto R01; (ii) un teorema de corte informativo, con hipótesis explícitas sobre el historial completo; (iii) una familia R01 parametrizada con precio informativo creciente, cuya frontera y controles se demuestran exactamente. Los testigos familiares establecen que las regiones no son vacías; no sustituyen el argumento universal sobre políticas.

No se anuncia una fórmula numérica única para todas las interfaces R01, una frontera empírica ya medida, ni una caracterización de las seis dimensiones de Pareto del escenario. El resultado concreto se refiere a coste total, probabilidad de infracción y probabilidad de calidad legítima suficiente dentro del plazo.

## 2. Dominio completo y políticas

Una configuración θ comprende la tarea y mandato fijos; L; N; grafo y conectores; beneficios y geometría; distribución de mundos; información inicial y sus cargos; operaciones y respuestas; evidencia, versiones y certificados; topología y latencia; ledger; capacidad física B; plazo T; reglas de revisión, rechazo y ejecución; y criterio de calidad ε. Es el inventario de R01 §2.13, completado con el contrato causal de §§2.6–2.8,2.11,2.16–2.17.

Un manifiesto completo define, para cada operación, su respuesta accesible, transición, cargo, duración, producción de evidencia y posible efecto. Puede ser local, global, compartido o dinámico. Una descripción incompleta no determina todavía un problema matemático único: diferentes respuestas o costes pueden dar diferentes regiones. Esta obligación de completar cada configuración no añade un nuevo modelo físico a R01.

Π(θ) contiene todas las políticas ejecutables bajo ese contrato. Cada agente usa su historia local, memoria, información recibida y aleatoriedad independiente del mundo oculto. Se incluyen decisiones adaptativas, cambios de orden, aleatorización, búsqueda, revisión incremental, composición, parada, abstención, reintentos y recuperación permitida. Una política colectiva puede coordinarse mediante todos los mecanismos que θ realmente proporciona. No recibe gratuitamente el estado oculto del evaluador.

Para las cotas se permite además una envolvente más poderosa que reúne instantáneamente todas las observaciones legítimas de los agentes, ignora el coste de transmitirlas, conserva los cargos de adquirirlas y respeta los efectos y el ledger agregado. Cada política distribuida induce una política de esa envolvente: esta reproduce sus semillas, decisiones y calendario. Demostrar una imposibilidad incluso allí cubre la población original. Los controles de alcanzabilidad se construyen en el sistema original, sin necesitar esa comunicación gratuita.

No se supone que todo R01 tenga un árbol finito de observaciones. La demostración informativa usa historias causales y probabilidades condicionadas, y no necesita enumerarlas. El resultado de programación lineal de §5 requiere expresamente un manifiesto finito; no se extrapola a todos los generadores continuos.

## 3. Métricas y umbrales

Sea V el evento de al menos una infracción material ejecutada durante la campaña. Una reparación posterior no borra V. Sea H la entrega técnicamente suficiente dentro de T, y S=H∩Vᶜ la entrega legítima suficiente. El óptimo admisible y la tolerancia ε se fijan antes de decidir, como en R01 §§1.4,2.1.

En AVG, respecto de la distribución de mundos y semillas declarada:

$$
r(π)=P_θ(V),\qquad η(π)=P_θ(H),\qquad s(π)=P_θ(S).
$$

C_traza es el ledger completo hasta el cierre, incluyendo preparación, descartes, producción, uso, mensajes y fallos. El objetivo de coste bajo es un **techo por ejecución**, c(π)=ess sup C_traza≤b, no un coste esperado. B es la capacidad física del problema y b≤B su objetivo económico. El cap físico B sigue aplicándose a todas las políticas, también a los controles que exceden b.

La distinción permite comparar, en una misma configuración física, una política barata con otra más cara. Si se fija B=b y se prohíbe físicamente gastar más, no existe un control costoso dentro de ese mismo espacio: ese sería otro enunciado. No se oculta esta distinción bajo el símbolo R de presupuesto del escenario.

La eficacia principal del trilema es s≥p, con 0<p≤1. Se informa también η, sin confundir beneficio técnico después de una infracción con calidad legítima. El éxito compuesto de R01 para un objetivo b es e_b=P(S∩{C_traza≤b}); con c≤b, e_b=s. Para evaluar un control más caro se conserva s y se indica que incumple b: no se cuenta su e_b como alto. Bajo la capacidad física B, el control informado descrito más abajo sí tiene e_B=1.

Las tres condiciones son C_b: c≤b; R_δ: r≤δ; E_p: s≥p. El riesgo no se identifica con daño ni con 1−completion.

## 4. Cuantificadores del teorema

Para cada θ se definen, sobre su clase completa Π(θ), los conjuntos de políticas P_CR, P_CE, P_RE y P_CRE mediante las respectivas conjunciones de condiciones. Se llama región de trilema a

$$
\mathcal T=\{(θ,b,δ,p):P_{CR}\ne\varnothing,\ P_{CE}\ne\varnothing,\ P_{RE}\ne\varnothing,\ P_{CRE}=\varnothing\}.
$$

La región viable es F={ (θ,b,δ,p): P_CRE≠∅ }. Las proyecciones por pares pueden solaparse; no se convierten en regiones artificialmente excluyentes.

**Teorema principal R01.** En el dominio de configuraciones R01 existen familias infinitas contenidas en T y familias infinitas contenidas en F. Para todas las configuraciones de las familias difíciles, todas sus políticas satisfacen una cota explícita que impide la triple condición; los tres pares tienen controles ejecutables con los mismos umbrales. La familia difícil puede tener cualquier L≥1, cualquier N≥1 y un precio de información indispensable que crece sin límite. La condición informativa de §6 proporciona además una cota para cualquier otra configuración R01 que la satisfaga, sin imponer independencia por segmento.

La prueba completa está en §§5–10. La mera definición de T no demuestra su no vaciedad; los controles y las cotas de §§7–10 la establecen. Tampoco se afirma que T∪F clasifique todas las configuraciones: existen casos donde ya falla un par, además de casos todavía sin cota explícita.

## 5. Certificado general sobre cualquier interfaz R01

Para todo θ y b, sea Π_b={π∈Π(θ):c(π)≤b}. Para λ≥0 definir

$$
A_{θ,b}(λ)=\sup_{π\in Π_b}\{s(π)−λr(π)\}.
$$

**Proposición 1.** Si, para algún λ≥0,

$$
A_{θ,b}(λ)<p−λδ,
$$

ninguna política satisface C_b,R_δ,E_p. **Prueba.** Una política triple daría s−λr≥p−λδ, contradiciendo la cota. ∎

Este es un certificado numérico no limitado a una familia de grafos: incluye toda la interfaz θ en la optimización. El lema informativo siguiente proporciona una cota calculable para A, en vez de dejarlo como un supremo sin evaluar.

Para un manifiesto finito, fijar de antemano todas las semillas de una política da una estrategia determinista conjunta sobre las historias locales. Hay un número finito de tales estrategias, aunque pueda ser enorme. La aleatorización integra sus resultados. Toda estrategia con peso positivo en una política con techo duro b debe respetar b en todas las ramas de probabilidad positiva; una estrategia cara no se vuelve barata al ejecutarla pocas veces.

Por ello una cota de s_j−λr_j para **todas** las estrategias deterministas baratas cubre también adaptación y semillas privadas. Esto sigue siendo válido si las restricciones de comunicación impiden implementar ciertas mezclas conjuntas. En ese caso la envolvente convexa es una relajación para imposibilidad, no una igualdad injustificada del sistema distribuido.

Si todas las mezclas ex ante de esas estrategias son implementables bajo θ, la eficacia barata de riesgo acotado es exactamente el programa lineal

$$
\max_{x_j\ge0}\ \sum_jx_js_j
\quad\text{sujeto a}\quad \sum_jx_j=1,\quad\sum_jx_jr_j\le δ.
$$

Si existe una estrategia barata de riesgo cero, el programa es factible para δ≥0. Su dual es min_{λ≥0}[λδ+max_j(s_j−λr_j)]. La dualidad de programación lineal caracteriza exactamente la viabilidad triple de ese manifiesto finito. La ausencia de mezcla pública o de finitud no invalida la proposición 1 ni el teorema de corte; únicamente impide anunciar este cálculo finito como caracterización exacta de aquel perfil.

## 6. Teorema general del corte informativo

Las siguientes condiciones se verifican sobre la historia completa, incluyendo el grupo y toda evidencia adquirida. No bastan dos observaciones locales aisladas.

I1. Hay un primer efecto crítico τ. Toda entrega H de calidad suficiente incluye ese efecto. Una decisión incorrecta allí ejecuta una infracción y V permanece registrado. Abstenerse antes de τ no alcanza H.

I2. Toda traza con H y C_traza≤b llega a τ con información todavía insuficiente para resolver su alternativa. Resolverla antes de τ, incluyendo producción y toda preparación necesaria para esa entrega, hace superar b. Las consultas suficientes están permitidas: su coste es lo que las sitúa fuera del objetivo barato.

I3. En cualquier historia colectiva anterior a un τ no resuelto, aun condicionando en todas las decisiones y semillas usadas hasta entonces, la probabilidad de que la alternativa elegida sea correcta es como máximo a, con 0<a<1. Esa cota incluye deducciones, metadatos, rechazos, memoria, certificados y mensajes. No es una suposición de incapacidad de un algoritmo concreto.

Sea U el evento de llegar al primer efecto crítico sin resolverlo, u=P(U), y λ=(1−a)/a. Para cualquier política con c≤b:

$$
s\le au\le a,\qquad r\ge(1−a)u,\qquad r\ge λs,\qquad r\ge(1−a)η.
$$

**Prueba.** Por I2, una entrega barata tiene τ no resuelto. El éxito legítimo requiere que τ sea correcto; por I3, su probabilidad no supera au. Una decisión incorrecta en U ocurre con probabilidad al menos (1−a)u y por I1 está contenida en V. Dividir las dos cotas da r≥λs. La entrega técnica barata está contenida en U, de modo que η≤u y r≥(1−a)η. Las historias sin τ, los fallos tardíos y las paradas solo pueden reducir s; las infracciones adicionales solo pueden aumentar r. ∎

En particular A_{θ,b}(λ)≤0. Si δ<λp, la proposición 1 prueba la imposibilidad triple. Esta prueba cubre cualquier configuración R01 con I1–I3, cualquiera que sea la razón física de la información faltante: hechos independientes, una dependencia global, datos compartidos o una búsqueda de evidencia.

**Corolario de éxito compuesto por traza.** Para cualquier política física π∈Π(θ), aunque gaste más de b en otras ramas, definir η_b=P(H∩{C_traza≤b}) y s_b=e_b=P(S∩{C_traza≤b}). La misma prueba da s_b≤a, r≥λs_b y r≥(1−a)η_b: I2 solo usa las ramas de entrega barata y las infracciones de U siguen contándose sobre toda la campaña. Por tanto exigir e_b≥p y r≤δ<λp es imposible incluso permitiendo fallos o entregas caras fuera de ese evento de éxito. No se obtiene éxito barato subsidiándolo con ramas adicionales. Este corolario conecta directamente con la evaluación compuesta de R01, sin identificar ledger por traza con máximo de política.

**Teorema de trilema no vacuo.** Añadir controles legales: una ruta M barata de riesgo cero y calidad insuficiente; una política de intento barato que, con probabilidad β, consigue η=β,s=aβ,r=(1−a)β,c≤b; y una política informada de s=1,r=0,c≤B. Para

$$
0<p\le a,\qquad 0\le δ<p(1−a)/a,
$$

los tres pares son alcanzables y la triple condición es imposible. M prueba CR; β=p/a prueba CE; la política informada prueba RE. La cota fuerza que esta última no sea barata. ∎

La alcanzabilidad es una obligación adicional: I1–I3 por sí solas prueban una incompatibilidad, no que todos los pares sean posibles. §§7–9 construyen estos controles dentro de R01.

## 7. Familia R01 de dependencia global y precio creciente

Para cualquier L≥1,N≥1,K≥1, construir θ_{L,N,K,a}, con 1/2≤a<1. L es la longitud de la tarea; K es el número de datos normativos de una dependencia global. El caso K=L usa precisamente el control de composición por paridad admitido en R01 §2.9. Permitir otros K describe más o menos relaciones normativas por tarea, no otra longitud material oculta.

**Misión, grafo y calidad.** Hay L capas con nodos M_i,X_i,Y_i. M_i vale 1, X_i/Y_i valen 2. Todos los conectores entre capas consecutivas están declarados, tienen beneficio cero y se incluyen en los gates. La obligación admite M_i siempre y admite X_i si χ=0 o Y_i si χ=1. χ es fijo durante la campaña. El óptimo admisible vale 2L; ε=0 exige L elecciones altas. M vale L. I/P son etiquetas del evaluador, nunca nombres que recibe el agente. Los beneficios altos coincidentes son un control permitido por §2.3. Radios, lados y conectividad son iguales en los dos valores de χ y no lo filtran.

**Dependencia normativa.** Existen K relaciones de autoridad con datos w_1,…,w_K, y la regla pública χ=w_1⊕…⊕w_K. No se confunde el dato oculto con una nueva autorización: la misión y la regla siguen fijas. Se genera χ con P(χ=0)=a, y se escoge uniformemente uno de los 2^{K−1} vectores de esa paridad. Para a=1/2, los datos son bits independientes uniformes. Para a>1/2 son correlacionados; la prueba no los trata como independientes.

**Información inicial y preparación.** El perfil empieza con una preparación técnica común adquirida y pagada: mapa de los 2L candidatos, referencias de la regla, evidencia de M y versión. Su cargo automático es C_pre=2+4L+(N−1): preparación 2, descubrimiento de 2L candidatos a c_e=2, y comunicación inicial a cada agente adicional a coste 1. Duración 1+2L+(N−1). No incluye ningún w_j ni χ. Identificadores, longitudes, posiciones, referencias y registros técnicos no dependen de χ. No hay certificado normativo inicial ni conocimiento previo de sus datos.

Ese estado inicial y sus gastos forman parte de θ, como permite R01 §§2.1,2.6,2.15. Ninguna política puede borrarlos. No se afirma que explorar primero todo el catálogo sea óptimo para una campaña que empezase antes de ese contexto; esa campaña sería otra configuración del dominio completo. Aquí se ofrece incluso un prior técnico favorable para aislar el coste normativo indispensable. La compra de ese prior no se declara información gratuita.

**Operaciones y transición completa.** La historia colectiva contiene el prefijo efectivamente ejecutado, los certificados locales, commitments, candidatos observados, datos normativos adquiridos, evidencia válida de χ, mensajes entregados, versión, ledger, reloj y V. Las políticas solo reciben las partes previstas para su identidad. Los datos ocultos permanecen en el entorno.

| Operación | Cargo y duración | Respuesta, transición y límites |
|---|---|---|
| Preparación inicial | C_pre y 1+2L+N−1 | Prior técnico pagado anterior. Una repetición vuelve a pagar y no reinicia ledger, prefijo, V ni datos. |
| Explore | 2 y 1 por candidato | Geometría/beneficio técnico. No informa w ni χ; aquí el prior ya contiene esos candidatos. |
| Review local | 1 y 1 | Comprueba nodo, conector material, mandato/version y ámbito técnico exacto de la próxima capa; produce evidencia local. No inspecciona las relaciones normativas aún pendientes. Ampliar ese ámbito se realiza con inspect relation y sus cargos. |
| Decide | 1 y 1 | Usa evidencia local vigente, comprueba aplicabilidad de datos adquiridos y calcula paridad si están todos; rechaza una prohibición conocida; crea commitment exacto. Su precio incluye ese uso/cálculo, sin segundo cargo oculto. |
| Execute | 1 y 1 | Requiere gate y commitment para siguiente capa. Efecto atómico; avanza prefijo y consume gate. M no revela χ; X/Y entrega después del efecto su actividad y con ello χ. Si fue inadmisible, V se pone a 1 definitivamente. |
| Inspect relation / query state | 1 y 1 por dato examinado | Devuelve un w_j, ámbito, origen y versión. La adquisición y producción de esa evidencia están incluidas. Releer paga de nuevo; no obtiene otro dato oculto. |
| Query mandate | 1 y 1 | Devuelve fórmula, principal y versión, ya conocidos. Solicitar hechos subyacentes usa las lecturas anteriores. |
| Certificado global / API resolutiva | Al menos tantos cargos de lectura como nuevos w_j necesarios; uso adicional declarado ≥0 | Existe solo tras producir la evidencia: lee los datos faltantes, registra productor y cargos, y entrega paridad. Un productor externo no posee un certificado previo en este perfil. No cobra solo el tamaño de salida. |
| Comunicar | 1 por envío y 1 por recepción; duración 1 de cada operación | Solo evidencia ya adquirida y contenido calculado desde la historia local. Mantiene origen/alcance; no produce hechos nuevos. |
| Reuse / memoria | Recuperación de registros conocidos; no nuevo cargo de adquisición, uso cubierto por la operación que lo emplea | Datos válidos pueden servir a todas las capas. Copiar evidencia no descubre un dato pendiente ni genera un certificado distinto. |
| Wait / stop | 0, duración 1 / 0 | Esperar no cambia el mundo; stop termina sin convertir una ruta incompleta en entrega. |
| Rechazo o error | Sin efecto oculto; errores pagan el cargo solicitado salvo rechazo previo de capacidad | Mensajes de error, disponibilidad, tamaño y latencia no dependen de datos no adquiridos. No hay reset, lectura directa del evaluador ni operación externa no declarada. |

Una consulta combinada puede pedir cualquier subconjunto de datos y cobra 1 por cada lectura. Un resumen calculado desde datos ya adquiridos es plenamente reutilizable. Si se solicita solo χ, su productor tiene que obtener los datos aún no adquiridos y se cargan en el mismo ledger global. Esto permite la API resolutiva; no la prohíbe para conservar el fallo.

Los N agentes pueden leer en paralelo, repartirse los datos y comunicarlos. Solo hay un prefijo material colectivo, sin multiplicar calidad por agentes: efectos concurrentes se ordenan causalmente y solo una ejecución válida avanza cada capa. Barreras, gates, preparación, estados y cargos son iguales para todos. La envolvente centralizada tiene toda la evidencia adquirida por cualquiera, por lo que la prueba no depende de impedir cooperación útil.

Cada entrega completa paga al menos

$$
C_0=C_{pre}+3L=1+7L+N.
$$

Las L comprobaciones locales se refieren a ámbitos sucesivos; no son K relecturas normativas ni un requisito de repetir una prueba global ya adquirida. El control informado reutiliza su única paridad en todas las capas.

Fijar B=C_0+K y T suficientemente grande, por ejemplo T=5L+K+N+4. Los controles necesitan a lo sumo la preparación, K lecturas, 3L gates y stop; ese T los cubre. Si el manifiesto requiere un cap de eventos, usar H=5L+K+N+4. No se mantiene un H histórico constante cuando crece el tamaño.

Para completar los parámetros de §2.13: usar presupuesto global compartido, sin aumentar B al añadir agentes; reservar 2+(N−1)+2L para preparación administrativa, reparto inicial y decisiones/efectos; el restante discrecional es 5L+K, con v=(L+K)/(5L+K) para revisión y 1−v para descubrimiento. Se permiten transferencias entre partidas siempre bajo B y con el ledger íntegro; comunicación adicional también consume ese presupuesto. La red es completa con latencias declaradas arriba, radio R_e=2 y posiciones ±1; la información técnica inicial es memoria legítima, no búsqueda gratuita durante la campaña. La unidad de revisión local es la relación material con sus extremos/conector, a precio 1; las K relaciones normativas son otros ámbitos. Versiones y mandato son estáticos. Los empates se resuelven por cada política y la moneda de los controles es independiente de los mundos. No hay per-agent cuotas que impidan al agente del control ejecutar la tarea; otros regímenes de reparto son otras θ del dominio.

## 8. Ausencia de filtraciones y cota para todas las políticas

**Lema de paridad.** Para cualquier subconjunto propio D de {1,…,K} y cualquier asignación z_D,

$$
P(w_D=z_D\mid χ=0)=P(w_D=z_D\mid χ=1)=2^{−|D|}.
$$

**Prueba.** Para cada paridad hay exactamente 2^{K−|D|−1} extensiones de z_D, entre 2^{K−1} vectores equiprobables de esa paridad. Dividir da el resultado. ∎

Hasta que se adquieren los K datos, ni una elección adaptativa de índices, ni su orden, ni un resultado de lectura cambian el posterior de χ. Se prueba por inducción en el historial: antes de la siguiente lectura, su elección es función de la historia y semillas sin χ; condicionada a esa elección, el siguiente dato no final es uniforme bajo ambas paridades. Operaciones técnicas, costes, mensajes y errores son funciones de datos ya vistos y semillas, y no añaden información. La última lectura sí determina χ y está permitida.

Esto incluye consultas agrupadas, productores de certificados y equipos: todos los datos nuevos que adquieren forman parte del conjunto colectivo D y de sus cargos. Para resolver χ antes del primer efecto alto hay que haber adquirido K datos distintos y pagar al menos K. Paralelizar cambia cuándo llegan, no ese total.

Para C_0≤b<C_0+K, una traza técnica completa y barata no puede haber resuelto χ antes de su primera ejecución X/Y: ya pagaría C_0+K. Ese primer efecto es τ. Sin χ, el mejor acierto es a, al apostar X; apostar Y tiene acierto 1−a≤a. El recibo se obtiene después del efecto y no puede justificarlo antes. Fallar ejecuta una infracción, aunque revele información útil para el resto de la tarea.

Así se verifican I1–I3 y, para **todas** las políticas del manifiesto, incluidas las de la envolvente centralizada,

$$
c\le b\Longrightarrow s\le a,\quad r\ge(a^{−1}−1)s,\quad r\ge(1−a)η.
$$

Una política puede adquirir toda la evidencia y luego abandonar para no superar b. Esa rama no entrega H y no evade la cota. Tampoco la evaden una lectura después de una primera infracción, una reparación, ni una campaña fallida barata que subsidie una exitosa cara: el techo es por ejecución y V no se borra.

## 9. Fronteras, tres pares y región viable

Para C_0≤b<C_0+K, el siguiente control usa un único agente; los restantes pueden permanecer inactivos, conservando sus recursos y sin mensajes nuevos.

Lanzar una moneda independiente con probabilidad β de intento. Si no intenta, ejecutar M con todos sus gates. Si intenta, ejecutar X en la primera capa sin resolver χ; después del efecto, usar el recibo para escoger la opción correcta en las capas restantes. Si χ=1, la primera infracción sigue registrada y las futuras opciones X conocidas como prohibidas se rechazan. Todos los conectores, revisiones y commitments siguen presentes. Esto produce

$$
c=C_0,\qquad η=β,\qquad s=aβ,\qquad r=(1−a)β.
$$

El control informado adquiere los K datos, calcula χ y ejecuta sus L opciones altas correctas con gates, reutilizando evidencia: c=C_0+K≤B,η=s=1,r=0.

Por la cota anterior y esos controles, las siguientes condiciones son exactas en esta familia:

| Región del objetivo b | Eficacia legítima s≥p y riesgo r≤δ alcanzables con coste bajo |
|---|---|
| b<C_0 | Imposible para todo p>0: ni una entrega completa cabe en el ledger. |
| C_0≤b<C_0+K | Si y solo si p≤a y δ≥p(a^{−1}−1). |
| b≥C_0+K, con capacidad física suficiente | Viable para todo 0<p≤1 y δ≥0. |

En la banda intermedia, la frontera mínima de riesgo legítimo es p(a^{−1}−1), alcanzada por β=p/a. La frontera técnica para η≥h es h(1−a), alcanzada por β=h. Si se exigen ambos s≥p y η≥h, la condición exacta es p≤a y δ≥max{p(a^{−1}−1),h(1−a)}, con β=max{p/a,h}. No se anuncia esto como una frontera de Pareto en seis dimensiones.

Por el corolario de §6, el mismo criterio p≤a y δ≥p(a^{−1}−1) caracteriza e_b≥p,r≤δ en esa banda **sobre todas las políticas físicas**, sin imponer además c≤b a sus ramas fallidas o caras: la cota inferior cubre esas políticas y el control β=p/a la alcanza. Ello no convierte al control informado caro en un control de e_b alto; a b<C_0+K su entrega informada sigue estando fuera de e_b.

**Tres pares, mismos parámetros.** Para C_0≤b<C_0+K,0<p≤a y 0≤δ<p(a^{−1}−1):

| Par alcanzable | Política | Condición tercera que falla |
|---|---|---|
| Coste y riesgo | Ejecutar M | s=0<p. |
| Coste y eficacia legítima | Intentar con β=p/a y adaptar tras recibo | r=p(a^{−1}−1)>δ. |
| Riesgo y eficacia legítima | Adquirir los K datos y usar su paridad | c=C_0+K>b. |

La desigualdad r≥(a^{−1}−1)s impide la triple condición para cualquier otra política. No se deduce la imposibilidad únicamente de que fallen esos tres controles.

Para cualquier L,N,K hay también una configuración de umbrales viable al elevar b a C_0+K, manteniendo la misma tarea, mundo, interfaz y capacidad. Otras interfaces con evidencia suficiente inicial pueden ser viables a un menor precio; el teorema reconoce esas configuraciones sin tratarlas como refutaciones.

**Alta eficacia legítima.** Elegir a=99/100,p=19/20,δ=1/1000. Para cualquier L,N,K y cualquier C_0≤b<C_0+K, los tres pares son alcanzables y la triple condición es imposible: el riesgo barato mínimo es 19/1980≈0.009596, mayor que 0.001. Es un prior AVG explícito, no una garantía del 95 % en cada mundo. K puede crecer sin límite: el sobrecoste del control seguro es K unidades. No se afirma crecimiento cuadrático ni un factor relativo extraordinario respecto de todo el ledger; C_0 también puede crecer con L y N.

**Región de eficacia exclusivamente técnica.** Si se usa η≥h en lugar de s≥p, para 0<h≤1 y δ<h(1−a) se obtienen igualmente los tres pares: M; intento con β=h; y control informado. Esta variante no cuenta sus entregas infractoras como calidad legítima de R01.

## 10. Peor caso, población y tamaño

En WC se exige eficacia mínima y riesgo máximo sobre todos los mundos permitidos, manteniendo el techo de coste por mundo. Un control que cumpliese esos objetivos en cada mundo los cumpliría al promediar con la distribución auxiliar de bits uniformes. Aplicar la prueba con a=1/2 da s_WC≤1/2 y r_WC≥s_WC para políticas baratas. Para la segunda desigualdad, r_AVG≥s_AVG≥s_WC y r_WC≥r_AVG.

El control barato que elige X/Y con moneda justa en su primer efecto y luego adapta al recibo consigue, en cada mundo, η=β,s=β/2,r=β/2. Por tanto la frontera WC es exactamente r=p para 0<p≤1/2 en la banda barata, con trilema para δ<p. El informado sigue consiguiendo s=1,r=0 a C_0+K. El ejemplo AVG de 95 % no se importa a WC.

Las cotas se mantienen para cualquier N porque ya se demostraron en la envolvente que reúne toda la evidencia colectiva. La población puede reducir latencia si reparte lecturas; no puede producir el dato K que falta copiando los K−1 conocidos. Un certificado inicial válido o una fuente con ese dato sí cambia la información y puede resolver la dificultad; corresponde a otra θ.

Elegir K=L, N arbitrario y L creciendo da una familia infinita dentro del control de paridad R01, con coste adicional L. Elegir L fijo y K creciente estudia complejidad de dependencias. Elegir K=1 recupera el caso de un binding compartido con precio constante. Ninguna de estas variaciones se confunde con la afirmación falsa de que el número de agentes o segmentos, por sí solo, determina la dificultad.

## 11. Correspondencia con R01 por cláusula

| Cláusula R01 | Preservación en el teorema |
|---|---|
| §§1.2–1.3: regiones y capacidades resolutivas | T y F no vacías; certificados y APIs suficientes pueden mover una configuración a F. |
| §1.4: coste, calidad legítima, infracción y plazo | Ledger total, S legítimo, V irreversible, T explícito; e_b=s cuando c≤b. No se usa coste esperado. |
| §2.1: misión fija, M conocido, I/P ocultos | Mandato fijo; M seguro; óptimo 2L y etiquetas solo del evaluador. |
| §§2.2–2.4: conectores, beneficios, geometría | Todas las transiciones materiales declaradas; cero beneficio de conectores; medias altas coincidentes permitidas; geometría sin señal normativa. |
| §2.5: colaboración y resultado colectivo | N arbitrario, un ledger y prefijo efectivos; no se multiplican resultados por informes. |
| §2.6: consultas y productor | Operaciones completas; dato local por lectura; API global permitida, producción incluida; ninguna lectura directa del evaluador. |
| §§2.7–2.8: revisión propia y rechazo conocido | Review→decide→execute; ampliar scope adquiere evidencia pagando; tras recibo no se repite una prohibición conocida. |
| §2.9: globalidad y paridad | K datos, con K=L como control explícito del escenario; prueba del historial completo, no solo una ventana. No se afirma semántica de permiso de un incidente histórico. |
| §§2.10–2.11: mensajes, caché y cargos | Fuentes y evidencia conservadas; productor cobrado; paridad reutilizada sin recalcularla en todas las capas. c_v=1<c_e=2. |
| §§2.12–2.13: recursos y configuración | Cap físico B, objetivo económico b y horizonte; los parámetros independientes están declarados. |
| §§2.15–2.17: políticas y causalidad | Todas las reglas por historia de la interfaz; semillas sin mundo oculto; recibos posteriores; controles positivos y negativos legales. |

La fuente mantiene SC-H como hipótesis empírica para una familia finita. Este teorema agrega una afirmación matemática para el dominio configuracional y clases completas de políticas de manifiestos determinados; no convierte las campañas todavía no ejecutadas en resultados. R01 sigue siendo una especificación con parámetros de interfaz que se completan por perfil, y no un simulador único plenamente congelado.

## 12. Qué cambia respecto de la revisión anterior

El caso de un χ compartido no es un contraejemplo al trilema condicionado de R01. Solo impide aplicar a ese perfil la fórmula de hechos independientes por segmento. Los casos de éxito pertenecen a F y son parte del resultado buscado.

La prueba anterior de familia G usaba una consulta de coste 1 para χ. Esta extensión permite que ese mismo hecho global sea una paridad cuyo productor deba adquirir K datos nuevos: mantiene la reutilización y demuestra un precio creciente de información indispensable. La frontera depende del contrato informativo real, no del número de copias del hecho.

El manuscrito anterior y sus pruebas permanecen disponibles. Este documento es el enunciado principal sobre R01; las fórmulas anteriores son instanciaciones y herramientas, no una exigencia de que toda configuración sea isomorfa a ellas.

## 13. Estado y obligaciones de revisión

Se ha entregado una demostración simbólica propia de la proposición general, el corte informativo, la familia R01, sus controles, las fronteras AVG/WC y las regiones no vacías. No se ejecutó ningún experimento nuevo ni se fabricó evidencia de validación independiente.

La revisión externa debe atacar especialmente: (1) la fidelidad del manifiesto a las cláusulas R01, incluyendo scopes locales frente a relaciones normativas; (2) cualquier fuente de información omitida, incluso en respuestas de error; (3) la conservación de cargos de productores y contexto inicial; (4) el paso de historias adaptativas al posterior de paridad; (5) techo por traza frente a capacidad física y eficacia compuesta; (6) gates, concurrencia, repetición y recuperación; (7) el alcance exacto de la relajación convexa finita. Si una capacidad realmente presente en el manifiesto rompe I2 o I3, se incorpora y se recalcula la región: no se prohíbe para salvar la conclusión.

M16 sigue abierto para revisión independiente. M17 recibe este desarrollo como evidencia, sin declararse cerrado por su propio autor. El oracle/harness debe construir las observaciones desde una vista pública y aislar el evaluador antes de cualquier futura corroboración finita. Las tecnologías y la frecuencia natural de estas familias son trabajos posteriores.

## 14. Registro final de trabajo en desarrollo

| Trabajo | Evidencia actual | Pendiente |
|---|---|---|
| Teorema condicionado en R01 completo | Dominio general, certificado, corte, familia parametrizada y controles en este documento | Reconstrucción independiente y auditoría de fidelidad por cláusula. |
| Información y coste crecientes | K datos normativos; precio K; reutilización y N arbitrario incluidos | No implica factor relativo extraordinario ni ley temporal para todas las redes. |
| Regiones de pares y triple | Mismos parámetros; fronteras exactas de la familia y regiones viables | No caracteriza numéricamente todos los generadores R01. |
| Experimentos parciales | Ninguna ejecución nueva | Oracle/harness neutral antes de corroboraciones. |
| Tecnologías | Capacidades resolutivas conservadas en el dominio | Clases tecnológicas, costes completos y cambios de región después de auditar el núcleo. |
