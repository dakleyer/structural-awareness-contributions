# Trilema condicionado de coste, riesgo y eficacia

## Una prueba por familias de configuraciones

Manuscrito independiente para revisión · Versión 0.1 · 4 de octubre de 2026.

**Estado:** demostración simbólica autocontenida en la clase definida aquí; revisión independiente pendiente. El resultado no se anuncia como teorema de todo R01 ni como una ley de todas las arquitecturas. La denominación «trilema condicionado» se propone para expresar este alcance, sin atribuirle reconocimiento terminológico o novedad científica ya comprobados.

### Resumen

Se estudia una tarea cuya calidad puede mejorarse mediante acciones que requieren establecer hechos de admisibilidad. Obtener esos hechos tiene un coste. Se demuestra una frontera exacta entre presupuesto máximo, probabilidad de infracción y probabilidad de entrega suficiente. La necesidad cubre cualquier política adaptativa y aleatoria con la información permitida; la suficiencia se demuestra mediante una política que alcanza la frontera. Existen familias no vacías donde cada par de objetivos es alcanzable, mediante estrategias distintas, y ninguna estrategia reúne los tres. Existen también familias donde las tres condiciones son compatibles. Se distinguen eficacia técnica y éxito legítimo y se demuestra una frontera para cada uno. La prueba no depende de una enumeración de ejemplos, del fallo de un algoritmo particular ni de prohibir memoria o coordinación competente.

## 1. Qué significa un trilema condicionado

Una configuración θ fija el problema, sus recursos, la información disponible y los objetivos. Un mundo ω fija los hechos ocultos. Una política π decide usando solo observaciones recibidas, memoria y aleatoriedad propia. La misma política se utiliza sin conocer previamente ω.

Sean los objetivos buenos:

$$
B_C(\theta,\pi)=[C_\theta(\pi)\le R],\qquad
B_R(\theta,\pi)=[\rho_\theta(\pi)\le r],\qquad
B_E(\theta,\pi)=[e_\theta(\pi)\ge t].
$$

C es coste máximo por ejecución, ρ riesgo de al menos una infracción material, y e una medida de eficacia definida antes de comparar políticas. R, r y t son umbrales, no resultados seleccionados después de ejecutar.

**Definición.** Una familia U presenta un trilema condicionado cuando U≠∅ y, para toda θ∈U:

$$
\begin{aligned}
&\exists\pi_{CR}: B_C\land B_R,\quad
\exists\pi_{CE}: B_C\land B_E,\quad
\exists\pi_{RE}: B_R\land B_E;\\
&\forall\pi\in\Pi(\theta):\quad
\neg(B_C\land B_R\land B_E).
\end{aligned} \tag{1}
$$

Las tres políticas de los pares pueden ser distintas. Para descartar una incompatibilidad universal, se exige además una familia viable V≠∅ donde exista una política que alcance las tres.

«Condicionado» identifica el dominio de validez y las bandas de recursos. No quiere decir que la prueba sea incompleta dentro de su modelo. «Parcial» sería menos preciso: puede referirse a una ejecución incompleta o a una demostración todavía pendiente.

Las regiones por pares pueden solaparse. Una misma configuración puede admitir una estrategia barata y segura, otra barata y eficaz y otra segura y eficaz, sin admitir una estrategia barata, segura y eficaz. No se pide que toda ejecución falle ni que todos los mundos sean desfavorables para cada política.

## 2. Modelo base: hechos y acciones

### 2.1 Tarea y mundo

Hay L≥1 segmentos consecutivos. En cada segmento se elige una opción; todas las opciones de segmentos consecutivos pueden conectarse. Las opciones son:

| Opción | Beneficio técnico | Admisibilidad |
|---|---|---|
| M | 1 | Siempre admisible. |
| X | 2 | Admisible cuando χ_i=0. |
| Y | 2 | Admisible cuando χ_i=1. |

El mundo es χ=(χ_1,…,χ_L). Los hechos χ_i son independientes, con P(χ_i=0)=a y P(χ_i=1)=1−a, donde 1/2≤a<1. El prior y a son conocidos. a=1/2 es la familia equilibrada; a próximo a uno permite estudiar decisiones cuya opción habitual es admisible con probabilidad alta. No se supone que cualquier problema real tenga este prior.

El óptimo admisible tiene beneficio 2L en todo mundo. Fijar 0≤ε<L. Una entrega técnicamente suficiente es una ruta completa con beneficio J≥2L−ε, equivalente a utilizar al menos

$$
d=L-\lfloor\varepsilon\rfloor\ge1
$$

opciones altas. Ejecutar solo M completa la tarea de referencia, pero no alcanza la calidad exigida.

### 2.2 Información, costes y políticas

Una lectura puede revelar un χ_i concreto antes del efecto, a precio completo c>0. No hay un servicio que devuelva una relación global sobre coordenadas no leídas. Las respuestas son exactas. Repetir una lectura se cobra; reutilizar un hecho adquirido es válido. Geometría, beneficios, duración, precio, identificadores, mensajes y revisiones gratuitas no filtran hechos ocultos.

Ejecutar una opción alta revela su χ_i después del efecto. Si era inadmisible, la infracción ya ocurrió y no se borra al reparar o continuar. Ejecutar M no revela χ_i. Una opción conocida como prohibida se rechaza. La política puede continuar tras una infracción utilizando acciones actualmente admisibles; no se impone aborto automático.

Toda ruta completa cuesta al menos C0=b+gL, con b≥0 y g>0. Hay controles que la completan por ese coste material más las lecturas pagadas. Se cobra todo el proceso, incluidos descartes y trabajo adicional. No se exige reservar C0 en todas las ramas fallidas; basta el hecho de que una rama que completa la tarea lo paga.

Las políticas pueden elegir qué leer y cuándo, recordar, detenerse, aleatorizar y coordinar cualquier número finito N de agentes. Se les concede cómputo local y coordinación perfectos como envolvente favorable, sin información oculta adicional. C es trabajo agregado, no gasto del agente más rápido. Los resultados no son cotas de latencia ni de presupuesto individual.

Cada configuración tiene un horizonte finito común, suficiente para leer d hechos y completar L segmentos. Puede medirse en eventos y fijarse, por ejemplo, T≥L+d+1 para los controles. Π(θ) contiene las políticas de esta interfaz, también las que gastarían más que R: el presupuesto es uno de los objetivos, no una restricción que haga desaparecer de antemano el control seguro y eficaz de mayor coste.

La prueba no fuerza a emplear una ventana fija o una revisión repetitiva. Los supuestos decisivos son independencia de hechos no observados, interfaz de lectura individual, cargo total positivo y efecto material no protegido de una acción todavía desconocida.

## 3. Dos medidas de eficacia y dos regímenes de garantía

Sea H el evento de entrega completa y técnicamente suficiente dentro del horizonte, y V el evento de al menos una infracción material durante el proceso. Definir

$$
\eta=P(H),\qquad \rho=P(V),\qquad
\sigma=P(H\cap\neg V).
$$

η es eficacia técnica; σ es éxito legítimo sin infracciones en el proceso. Una ejecución inadmisible nunca se cuenta en σ. El presupuesto no está incorporado a H: se exige por separado C≤R. Siempre

$$
\eta\le\sigma+\rho. \tag{2}
$$

Dos contratos posibles:

- **Técnico:** η≥h y ρ≤r, con 0<h≤1 y 0≤r≤1.
- **Legítimo:** σ≥p y ρ≤δ, con 0<p≤1 y 0≤δ≤1.

En AVG las probabilidades incluyen el prior del mundo y la aleatoriedad de π. En WC se exigen las cotas en cada mundo, con probabilidad únicamente sobre la aleatoriedad interna de una misma π. Para WC el prior no cambia las garantías.

## 4. Lema universal: el riesgo de los hechos no establecidos

Para una política con C≤R y R≥C0, escribir

$$
k=\left\lfloor\frac{R-C_0}{c}\right\rfloor,\qquad
m=\max(0,d-k),\qquad q=a^m.
$$

**Lema 1, AVG.** Toda política de la clase satisface

$$
\boxed{\sigma\le q,\qquad
\rho\ge(q^{-1}-1)\sigma,\qquad
\rho\ge(1-q)\eta.} \tag{3}
$$

**Demostración.** En una historia sin infracciones, denominar apuesta al primer efecto alto sobre un binding no adquirido mediante lectura ni observado en un efecto alto previo. Condicionada a toda la historia accesible, su probabilidad de ser admisible es a o 1−a, y por tanto no supera a. La independencia mantiene esto aunque el índice y la opción se elijan adaptativamente. Una lectura de otro binding no cambia la ley del que todavía no se ha observado.

Una entrega legítima necesita d bindings altos admisibles. Esa rama paga C0 y puede financiar como máximo k lecturas. En consecuencia, debe acertar al menos m apuestas distintas. Este razonamiento no presupone que todas las ramas, incluidas las fallidas, hagan como máximo k lecturas.

Sea u_j la probabilidad de llegar a la apuesta j antes de una primera infracción. Parar, leer o actuar entre apuestas puede impedir llegar a la siguiente; no puede aumentar la probabilidad de acertar una apuesta más allá de a. Por tanto

$$
u_1\le1,\qquad u_{j+1}\le a u_j.
$$

Para m≥1, el éxito legítimo implica acertar la apuesta m, de modo que

$$
\sigma\le a u_m\le a^m.
$$

Los eventos de primera infracción en las apuestas 1,…,m son disjuntos. Cada uno tiene probabilidad al menos (1−a)u_j. Además u_j≥a^{-(m-j)}u_m. En consecuencia,

$$
\begin{aligned}
\rho&\ge(1-a)\sum_{j=1}^m u_j\\
&\ge(1-a)u_m\sum_{j=1}^m a^{-(m-j)}\\
&=(a^{-m}-1)a u_m\\
&\ge(a^{-m}-1)\sigma.
\end{aligned}
$$

Usando (2), se obtiene ρ≥(1−a^m)η. Si m=0, q=1 y las tres desigualdades son triviales. La prueba incluye políticas aleatorias: su semilla no contiene información inicial del mundo; condicionado a su historia, el binding nuevo conserva la ley indicada. El número finito de eventos permite numerar las apuestas sin asumir un orden fijo de consultas. ∎

La desigualdad σ≤qη no se utiliza: la política puede decidir si completar dependiendo de observaciones recibidas. El lema separa correctamente supervivencia, eficacia y riesgo aun con esa adaptación.

## 5. Fronteras exactas: necesidad y suficiencia

**Teorema 1, AVG.** Si R<C0, no se alcanza ninguno de los contratos de eficacia positiva bajo C≤R. Para R≥C0 y q=a^{max(0,d−k)}:

$$
\boxed{\exists\pi:C\le R,\ \rho\le r,\ \eta\ge h
\quad\Longleftrightarrow\quad r\ge h(1-q).} \tag{4}
$$

$$
\boxed{\exists\pi:C\le R,\ \rho\le\delta,\ \sigma\ge p
\quad\Longleftrightarrow\quad
p\le q\ \text{y}\ \delta\ge p(q^{-1}-1).} \tag{5}
$$

**Necesidad.** (4) y (5) siguen del lema. R<C0 impide toda ruta completa con una política cuyo coste máximo no supere R.

**Suficiencia común.** Con probabilidad β intentar una ruta con d opciones altas. Leer min(k,d) de sus bindings, ejecutar allí la opción admisible y elegir X en las m posiciones restantes. En las demás posiciones usar M. Con probabilidad 1−β ejecutar solo M. Todas las ramas cuestan como máximo C0+c min(k,d)≤R. Las decisiones en segmentos no leídos siguen siendo desconocidas aunque una decisión previa haya revelado otro binding independiente. Los recibos se conservan.

En AVG este control tiene

$$
\eta=\beta,\qquad \sigma=\beta q,\qquad
\rho=\beta(1-q). \tag{6}
$$

Para (4), elegir β=h. Para (5), elegir β=p/q, que está en [0,1] exactamente cuando p≤q. Así se alcanzan las cotas, no solo un límite asintótico. ∎

**Corolario 1, WC.** Para la garantía por mundo, las mismas fronteras (4)–(5) son exactas reemplazando q por q_WC=2^{-m}. La necesidad se obtiene promediando las garantías WC bajo la ley uniforme auxiliar de los mundos y aplicando el lema con a=1/2. Esta ley auxiliar es válida para probar necesidad aunque el prior AVG declarado sea otro. Para suficiencia, adivinar X/Y con monedas independientes equiprobables en las m posiciones no leídas: (6), con q_WC, se cumple en cada mundo. ∎

Las fronteras AVG y WC coinciden cuando a=1/2. Un prior favorable puede ayudar AVG sin garantizar el mismo comportamiento en todos los mundos.

## 6. Existencia del trilema y de configuraciones viables

### 6.1 Eficacia técnica

Para AVG, fijar a,b,g,c,h y r<h. Elegir cualquier entero d con h(1−a^d)>r, poner L≥d, ε=L−d y R=C0. Existe tal d porque a<1. La siguiente tabla establece los tres pares:

| Par | Política | Resultados | Objetivo que se pierde |
|---|---|---|---|
| Coste–riesgo | Solo M | C=C0; ρ=0; η=0 | Eficacia. |
| Coste–eficacia | d opciones altas X sin lecturas; M en las demás | C=C0; η=1; ρ=1−a^d>r | Riesgo. |
| Riesgo–eficacia | Leer d bindings y ejecutar las opciones admisibles | C=C0+cd; η=1; ρ=0 | Coste. |

El teorema demuestra que **ninguna otra política** preserva los tres umbrales. Estos testigos no sustituyen la necesidad universal. Con ε=0 y L suficientemente grande se obtiene una familia de tamaños arbitrarios. Cambiar únicamente el presupuesto a R=C0+cd permite η=σ=1 y ρ=0 en todo mundo: la familia viable también es no vacía.

Para WC se utiliza la misma construcción con a=1/2 en las desigualdades y monedas equiprobables en las decisiones no leídas.

### 6.2 Éxito legítimo: el riesgo sigue siendo un objetivo separado

También existe un trilema con e=σ, sin acreditar resultados inadmisibles como éxito. Para R≥C0, cualquier configuración con

$$
\boxed{p\le q\quad\text{y}\quad
\delta<p(q^{-1}-1)} \tag{7}
$$

permite los tres pares, pero no su conjunción:

| Par | Política | Resultados |
|---|---|---|
| Coste–riesgo | Solo M | C=C0≤R; ρ=0; σ=0<p. |
| Coste–eficacia legítima | Control (6) con β=p/q | C≤R; σ=p; ρ=p(q^{-1}−1)>δ. |
| Riesgo–eficacia legítima | Leer los d bindings | σ=1; ρ=0; C=C0+cd>R. |

La última desigualdad de coste sigue de (7): q=1 la haría imposible; por tanto k<d y R<C0+cd. (5) excluye cualquier política alternativa que reúna los tres.

**Familia con eficacia legítima alta.** Fijar a=99/100, p=19/20 (95 %) y δ=1/1000 (0,1 %). Para cualquier L=d≥1, fijar R=C0+c(d−1), de modo que m=1 y q=99/100. Entonces

$$
p\le q,\qquad
p(q^{-1}-1)=\frac{19}{1980}>\frac1{1000}.
$$

Por (7), para todo tamaño de esta familia hay trilema condicionado AVG con un objetivo de éxito legítimo del 95 %. El control barato y eficaz intenta con probabilidad β=95/99; el riesgo mínimo compatible con ese éxito es 19/1980. Leer el último hecho cuesta c adicional y permite los tres. La familia equilibrada WC también admite (7), por ejemplo con p≤1/2 y δ<p cuando m=1; no se atribuye la tasa del 95 % a ese régimen.

Si δ≥1−p, el riesgo es redundante para cualquier política con σ≥p, pues éxito legítimo e infracción son eventos disjuntos. Que el riesgo sea vinculante exige umbrales que no lo hagan redundante. La condición (7) cumple esa obligación.

## 7. Las regiones y el coste crítico

Sea q_j=a^j en AVG y q_j=2^{-j} en WC. Para el objetivo técnico y r<h, definir

$$
j_T=\max\{j\in\mathbb N_0:h(1-q_j)\le r\},\qquad
C_T=C_0+c\max(0,d-j_T).
$$

La banda técnica con trilema es C0≤R<C_T; R≥C_T es viable. El borde R=C_T pertenece a la región viable. Si r≥h, basta C0 y esa banda es vacía.

Para éxito legítimo, definir

$$
j_L=\max\{j\in\mathbb N_0:p\le q_j,\quad
\delta\ge p(q_j^{-1}-1)\},\qquad
C_L=C_0+c\max(0,d-j_L).
$$

R≥C_L es la región viable legítima. Dentro de su complemento, la región donde **todos los pares** son alcanzables es (7); en otras bandas incluso el par coste–éxito legítimo puede ser imposible. No se etiqueta todo presupuesto insuficiente como trilema no vacuo.

Estas definiciones conservan exactamente las igualdades, sin depender de logaritmos numéricos redondeados. En el modelo equilibrado, j_T=floor(log_2(h/(h−r))).

Para θ, definir A_S={θ: existe π que alcanza los objetivos de S}. Las regiones por pares son U_CR=A_CR\A_CRE, U_CE=A_CE\A_CRE y U_RE=A_RE\A_CRE. En las familias probadas se solapan. Si se desea clasificar ocho combinaciones disjuntas de resultados, debe hacerse sobre (θ,π), no suponer que las proyecciones sobre θ son disjuntas.

Con abstención barata y segura, una configuración no puede tener como posibilidades máximas «solo una» condición: abstenerse ya satisface coste y riesgo. Obtener esa clasificación exigiría otro contrato de admisibilidad, no una reinterpretación del presente teorema.

## 8. Por qué la prueba es sustantiva y qué no demuestra

La incompatibilidad no se introduce como axioma. Se deriva de cuatro hipótesis observables del modelo: hechos no establecidos que conservan incertidumbre, acceso individual con coste total, calidad que exige decisiones altas y riesgo irreversible si una decisión resulta inadmisible. El sistema admite estrategias seguras, eficaces y plenamente informadas; son los umbrales conjuntos de determinadas configuraciones los que las separan.

La prueba cubre adaptación, aleatoriedad, memoria y coordinación. El control alcanza la cota y prueba que no se exige más coste del necesario. La no vaciedad está demostrada con familias arbitrariamente grandes, y el control viable muestra que no se ha decretado una incompatibilidad universal. La segunda definición de eficacia evita sostener el resultado únicamente con entregas inadmisibles.

Eso establece consistencia y una imposibilidad dentro de la clase. No demuestra que todos los problemas reales pertenezcan a ella. Información inicial suficiente, correlaciones aprovechables, lectura de predicados globales o protección antes del efecto cambian el contrato. Su análisis tecnológico requiere otras pruebas y queda fuera de este documento.

En esta familia, adquirir todos los hechos cuesta cd, lineal en el número de decisiones altas. No se afirma que el sobrecoste sea extraordinario en relación con C0 ni se transfiere automáticamente una cota cuadrática de otro generador. El coste esperado, latencia, geometría, presupuestos por agente, cambios temporales y nuevas interfaces no están cubiertos por estas fronteras.

**Utilidad práctica.** Una vez que se demuestre que un problema respeta el contrato, la frontera permite comprobar si sus objetivos de presupuesto, riesgo y eficacia son compatibles, identificar el recurso que falta y comparar una propuesta con un control realizable. No identifica por sí sola una arquitectura ganadora ni estima la frecuencia de infracciones en despliegues.

## 9. Antecedentes y límites de atribución

La prueba de este documento es autocontenida. Como antecedente metodológico, Baldassini, Johnson y Aldridge estudian límites de consultas adaptativas en group testing; su Teorema 3.1 limita la recuperación exacta del conjunto de defectuosos con T tests [1]. Aquí se exige una entrega suficiente, no recuperar el mundo completo: aquel resultado no se utiliza para justificar automáticamente nuestras cotas. Tampoco constituye una validación externa de este trilema. No se afirma novedad sin una revisión bibliográfica más amplia.

[1] L. Baldassini, O. Johnson y M. Aldridge, *The Capacity of Adaptive Group Testing*, ISIT 2013, pp. 2676–2680, arXiv:1301.7023v2. Texto primario comprobado, §III, Teorema 3.1: https://arxiv.org/html/1301.7023v2 ; registro: https://arxiv.org/abs/1301.7023 .

## 10. Revisión y estado del manuscrito

La redacción y la revisión matemática actuales se realizaron con asistencia de IA, examinando explícitamente los supuestos y los casos límite. Se trata de revisión propia; no se presenta como revisión independiente ni como prueba formal verificada por un asistente lógico. No se han ejecutado nuevos tests científicos para producir este manuscrito. Los diagnósticos previos se conservan aparte y no sustentan el cuantificador universal.

Para consolidarlo ante terceros faltan: reconstrucción simbólica por un revisor independiente; comprobación de las hipótesis del problema al que se aplique; y, si se anuncia un teorema de R01, una reducción que preserve todas sus políticas, observaciones, efectos y costes. Una campaña empírica tiene otra finalidad: medir incidencia y utilidad en el ámbito probado. No reemplaza esas obligaciones matemáticas.

<!-- R01_BOT_WORKPLAN_START scope="conditioned-trilemma-independent-manuscript" -->

| Obligación | Evidencia disponible | Pendiente y criterio de cierre |
|---|---|---|
| Contrato y cuantificadores, M12 | §§1–3, separación coste/eficacia, AVG/WC y regiones | Congelar la versión final y su correspondencia de medidas con R01. |
| Necesidad y suficiencia, M03/M04 | Lema 1, Teorema 1, Corolario 1 y familias no vacías | Dictamen adversarial por afirmación; conservar cualquier contraejemplo. |
| Revisión independiente, M16 | Prueba completa revisable, sin dependencia del checker | Revisor distinto reconstruye adaptación, costes de ramas fallidas, generalización a, WC, igualdad y controles. |
| Puente a R01, M17 | Clase y límites explícitos | Embedding/reducción que incluya todas las políticas relevantes; si falta, conservar alcance suplementario. |
| Harness, C01–C05/M05 | Diagnósticos anteriores separados | Contrato y método neutral antes de nuevas ejecuciones científicas. |
| Literatura y novedad, M06 | Una fuente primaria delimitada | Revisión más amplia; no derivar novedad de esta referencia. |
| Tecnología, M13–M15 | Fuera de la prueba actual | Reanudar después de consolidar contrato y lemas base. |

<!-- R01_BOT_WORKPLAN_END -->
