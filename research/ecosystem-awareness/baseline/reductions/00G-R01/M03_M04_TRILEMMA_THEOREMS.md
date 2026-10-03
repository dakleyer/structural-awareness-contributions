# R01 — Pruebas del trilema y efecto de las tecnologías

M03/M04, extensión matemática v1.0 · Derivación y revisión propia; revisión independiente pendiente

[README de R01](./README.md#bot-start-here) · [Plan matemático](./MATHEMATICAL_FEASIBILITY.md) · [Contrato suplementario](./TRILEMMA_CONTRACT.json) · [Comprobador](./verify_trilemma.py) · [Resultados finitos](./TRILEMMA_CHECKS.json) · [Registro de conservación](./TRILEMMA_RELEASE_CHECKS.json) · [Propuesta recibida, sin cambios](./TRILEMMA_RECEIVED_SKETCH.md)

Entrada del repositorio: `2dc438df524663ebf79e6552cd688d34c2619d8b`. Autor/revisor: Codex, por instrucción del usuario. Las demostraciones siguientes son simbólicas y cubren todas las políticas de las clases declaradas. Las comprobaciones pequeñas buscan errores en ellas; no las sustituyen. No se afirma revisión independiente, novedad, ventaja de EA ni clasificación de una tecnología comercial.

## 1. Qué se prueba y qué permanece abierto

La tesis es existencial sobre familias de problemas, universal sobre políticas: **hay configuraciones físicamente realizables en las que toda política admitida incumple al menos uno de coste bajo, riesgo bajo y eficacia técnica alta**. También hay configuraciones y tecnologías que permiten los tres. No se presupone que toda configuración sea difícil.

Se dan dos pruebas con fronteras exactas. La familia F tiene un binding independiente por segmento y exige un coste adicional lineal. La familia W tiene una condición conjuntiva global y permite separar segmentos materiales de relaciones normativas: con relaciones densas, el coste de información necesario es cuadrático frente a una ejecución lineal. Además se prueba una cota de coste esperado para W; la dificultad no depende solamente de exigir un presupuesto máximo por ejecución.

Las tecnologías se estudian por su interfaz y coste total. Una consulta más barata preserva la cota de acceso a datos. Un certificado suficiente cambia esa interfaz. Un ejecutor que garantiza admisibilidad cambia el mecanismo de efectos y puede eliminar el riesgo sin revelar los datos al agente. Estos cambios requieren pruebas distintas.

M03/M04 quedan DONE **para estos perfiles suplementarios y sus fronteras**, no para todo R01. M05/C05, M06/M07–M09, transferencia E1–E7, campaña y precios reales siguen pendientes. M11 continúa con la revisión de otros generadores y transferencias. M01 y M10 se amplían mediante este contrato versionado; sus resultados históricos conservan su alcance. La fuente base y los fixtures anteriores no se modifican.

## 2. Contrato común: objetivos, costes y políticas

Cada instancia es finita; la familia contiene tamaños arbitrariamente grandes. Hay L segmentos consecutivos con todas las conexiones entre opciones de segmentos adyacentes. Cada segmento ofrece M, siempre admisible y de beneficio técnico 1, y dos opciones altas de beneficio técnico 2. En cada mundo exactamente una opción alta es admisible. El óptimo admisible es 2L. Una ruta completa tiene beneficio técnico J, incluso si su composición resulta inadmisible; ese J técnico **no** se acredita como q legítima en R01.

Fijar antes de observar el mundo: tolerancia 0≤ε<L, exigencia de eficacia 0<h≤1, riesgo máximo 0≤r≤1, presupuesto R y plazo T. Sea d=L−⌊ε⌋: una ruta suficiente necesita al menos d opciones altas. W usa ε=0, por tanto d=L.

Para cada ejecución:

- Ttec: ruta completa de J≥2L−ε, dentro del presupuesto/plazo del perfil;
- V: ocurrió alguna ejecución material inadmisible en la campaña; es irreversible;
- S=Ttec∩¬V: éxito conjunto legítimo;
- η=P(Ttec), ρ=P(V), σ=P(S). Siempre σ≥η−ρ y η≤σ+ρ.

η es una **medida suplementaria de eficacia técnica**. No reemplaza e/a/q/f ni hace que una infracción sea legítima. Cuando se usa el objetivo original de R01, se exige σ≥p y se conserva el riesgo separado si corresponde. Esta distinción importa: un trilema con η y uno con éxito ya definido como libre de infracciones tienen fronteras diferentes (§3.3).

En AVG las probabilidades incluyen el mundo con el prior declarado y la aleatoriedad de la política. En WC se pide ηω≥h y ρω≤r para **cada** mundo ω, con probabilidad solo sobre la aleatoriedad interna. Una política es común a todos los mundos y usa únicamente su historia observable. No puede escogerse después de conocer la etiqueta oculta.

Toda ruta completa paga C0=b+gL, b≥0 y g>0: preparación y trabajo material, incluyendo revisión propia de geometría, decisión, conexiones y ejecución. Ninguna de esas revisiones revela el binding oculto antes del efecto. Hay consultas registradas que leen hechos concretos a precio total exacto c>0 por hecho, con disponibilidad asegurada. El precio incluye producción, acceso, recepción y comprobación de aplicabilidad; no se deja trabajo informativo gratuito detrás de la consulta. Repetir trabajo se cobra, reutilizar el mismo hecho ya conocido es permitido. Costes y tiempos anteriores al efecto no filtran datos ocultos.

La memoria, el cómputo local y el intercambio perfecto pueden concederse gratuitamente como envolvente favorable al agente. C es trabajo agregado de todos los agentes, no tiempo del agente más rápido. Cualquier equipo finito se representa mediante una política central con toda su historia: darle coordinación perfecta solo facilita el problema. Por ello las cotas inferiores cubren tales equipos si mantienen la interfaz de acceso; no establecen una cota de latencia, red o distancia. Preparación informativa real y comunicación real se cobran al transferir a una implementación.

El receptor rechaza una prohibición **ya conocida**. No hay barrera que compruebe gratuitamente el binding desconocido antes del efecto. Una opción desconocida puede ejecutarse y producir una infracción; el recibo posterior revela si fue admisible. Tras una infracción se permiten acciones posteriores actualmente admisibles; V permanece. Un protocolo que impusiera aborto global obligatorio tendría otra frontera de η. Nunca se sobrepasa conscientemente el presupuesto para producir Ttec. El plazo y el máximo de eventos se fijan finitos en cada instancia y suficientemente grandes para los controles descritos (por ejemplo, O(L+n)); no se extrapola el límite 32 de M02 a tamaños ilimitados.

Para R≥C0, k=⌊(R−C0)/c⌋ limita las consultas en cualquier ruta Ttec. Si R<C0, η=0. Una rama que consume más de k consultas no puede producir Ttec; en argumentos de mínima infracción puede sustituirse por una parada segura. Información previa no prevista, predicados globales, certificados y barreras son otros perfiles, estudiados explícitamente en §6.

## 3. Familia F: bindings locales independientes

### 3.1 Definición y cota para toda política

El mundo χ=(χ1,…,χL) es uniforme en {0,1}^L. En el segmento i, X es admisible si χi=0 y Y si χi=1. Una consulta lee un χi. Un recibo de ejecución revela solamente ese binding. No se admite un oráculo arbitrario sobre χ en este perfil. Computación, elección de qué consultar y cuándo, caché y aleatoriedad pueden ser arbitrarias.

**Teorema F.** Sean m=max(0,d−k) y q=2^(−m). Toda política satisface

\[
\sigma\le q,\qquad \rho\ge(2^m-1)\sigma,
\qquad \rho\ge(1-q)\eta. \tag{F1}
\]

**Prueba.** Antes de la primera infracción, el primer efecto alto en un binding que no se ha consultado ni observado es una apuesta acertada con probabilidad exactamente 1/2. La independencia mantiene esto válido condicionado a toda historia anterior y a las decisiones adaptativas. Elegir el índice según esa historia no cambia el bit aún no visto. Una consulta de otro índice no lo revela. Los recibos sí aportan información, pero en una historia sin infracciones su resultado para la opción elegida es necesariamente «admisible».

Numerar las primeras apuestas en bindings distintos. Sea aj la probabilidad de entrar en la apuesta j antes de una infracción. Entonces a1≤1 y a(j+1)≤aj/2; detenerse o consultar puede reducir esa probabilidad. Un S necesita d bindings altos acertados y como máximo k consultas, por lo que necesita al menos m apuestas acertadas. Para m≥1, σ≤am/2≤2^(−m). Los eventos «primera infracción en la apuesta j» son disjuntos y tienen probabilidad aj/2. Además aj≥2^(m−j)am para j≤m. Así

\[
\rho\ge\sum_{j=1}^m a_j/2
\ge(2^m-1)a_m/2\ge(2^m-1)\sigma.
\]

Con η≤σ+ρ, se obtiene σ≤ρ/(2^m−1) y por tanto ρ≥(1−2^(−m))η. Para m=0 las tres desigualdades son triviales. La prueba admite políticas aleatorias directamente; también puede fijarse una semilla independiente del mundo y promediar. Las ramas que fracasan, se detienen o ejecutan trabajo adicional no aportan S y no borran V. ∎

### 3.2 Frontera exacta, controles y cuantificadores

**Construcción que alcanza la cota.** Con probabilidad β, elegir d segmentos altos, consultar min(k,d) de sus bindings y adivinar los demás con monedas independientes y equiprobables; completar los otros segmentos con M. Con probabilidad 1−β, ejecutar solo M. Todos los recibos y revisiones se conservan. Una infracción local anterior no identifica el siguiente binding independiente; no se ejecuta una opción futura conocida como prohibida. El resultado es

\[
\eta=\beta,\quad \sigma=\beta q,\quad
\rho=\beta(1-q),\quad C\le C_0+c\min(k,d).
\]

Las monedas hacen que estos valores sean iguales en **cada** mundo, no solo en AVG. La cota AVG es necesaria para WC; este control alcanza WC. Por tanto, para AVG y para WC con políticas aleatorias,

\[
\boxed{\exists\pi:\ C\le R,\ \eta\ge h,\ \rho\le r
\iff R\ge C_0\ \text{y}\ r\ge h(1-2^{-\max(0,d-k)}).} \tag{F2}
\]

Para 0≤r<h, sea jallow el mayor entero j≥0 con h(1−2^(−j))≤r; equivale a ⌊log2(h/(h−r))⌋. La comparación con potencias racionales evita errores numéricos en igualdad. Entonces

\[
k_{\min}=\max(0,d-j_{allow}),\qquad
C_{crit}=C_0+c k_{\min}. \tag{F3}
\]

La banda imposible es [C0,Ccrit), y la igualdad R=Ccrit es viable. Si r≥h, completar con probabilidad h sin información ya satisface el criterio; si d=0, M basta. No se ocultan estas bandas vacías.

Los tres pares de objetivos tienen controles: M consigue coste C0 y riesgo cero con η=0; la ruta alta ciega consigue C0 y η=1 con riesgo 1−2^(−d); consultar los d bindings consigue η=1 y riesgo cero con coste C0+cd. Para cualquier h>0 y r<h, existe d suficientemente grande con h(1−2^(−d))>r. En esos tamaños ninguna política logra los tres a C0, aunque cada par sí se logra. Esta es la forma cuantificada del trilema solicitado, no una lista de ejemplos.

Si ε=αL con 0≤α<1, d=⌈(1−α)L⌉. Con b,g,c fijos, Ccrit−C0=c(1−α)L+O(1). Para R=(1+λ)C0, el umbral relativo asintótico es λ*=c(1−α)/g: por debajo falla para L grande; por encima funciona para L grande. **En la igualdad hay que conservar los redondeos.** Con b=2,g=3,c=1,α=1/2,jallow=0,λ=1/6, L par es viable y L impar no: el margen L/2+1/3 debe alcanzar ⌈L/2⌉.

### 3.3 El objetivo legítimo original y el fixture M02

Si se exige σ≥p en vez de η≥h, para p>0 la frontera exacta de F es

\[
\boxed{p\le q\quad\text{y}\quad
\delta\ge p(q^{-1}-1).} \tag{F4}
\]

Necesidad por F1; suficiencia con β=p/q. Un presupuesto mayor puede ser necesario tanto por eficacia legítima como por riesgo. No es correcto afirmar que incluir legitimidad en eficacia convierte siempre el problema en un mero dilema: el riesgo adicional puede ser vinculante dependiendo de p y δ. Con δ≥1−p es redundante para cualquier política con σ≥p, por la disyunción de S y V; con umbrales menores puede importar.

M02 **no** es F3: sus tres segmentos comparten un único χ. A R=11 no cabe una consulta adicional; antes del primer efecto alto no hay información de χ. Si se intenta una ruta técnicamente suficiente, la primera opción alta es incorrecta con probabilidad 1/2. El mismo argumento de una sola apuesta da ρ≥η/2 y σ≤1/2. La estrategia correcta para η=1 es ejecutar X en el primer segmento y, a partir del recibo, usar la opción actualmente admisible en los dos restantes. Así η=1,ρ=σ=1/2,C=11. Ejecutar X tres veces pese a conocer la prohibición no es un control admitido. Con R=12, el certificado existente revela χ antes del efecto y resuelve el caso. Esta conexión no transforma el fixture anterior ni sus 76 controles históricos.

## 4. Familia W: conjunción con muchas relaciones y pocas acciones

### 4.1 Mundos, medida y normalización

Hay n≥1 hechos normativos z1,…,zn y f(z)=AND(z). El mundo G, todos unos, tiene probabilidad 1/2. Cada Bj, con un único cero en j, tiene probabilidad 1/(2n). El modo alto A es admisible si f=1; el modo alto B, un procedimiento alternativo, si f=0. M es siempre admisible. El mandato es el mismo en todos los mundos. Cada segmento ofrece A/B/M y todas las mezclas; una mezcla A/B no puede ser completamente admisible. ε=0 exige L opciones altas. El beneficio técnico sigue siendo 2 por opción alta.

Una consulta lee un zi a precio c. No hay certificado global gratuito. La geometría local no prueba f; un efecto A/B revela f después de realizarse. Entonces se puede completar con el modo correcto, pero no reparar la primera infracción. Esta correlación entre hechos es deliberada: con bits independientes equiprobables, AND sería casi siempre falso y adivinar B resolvería AVG a bajo coste. La distribución equilibrada entre G y testigos inválidos es parte de la afirmación, no una propiedad de todo AND.

Los n hechos de W no son n bits estadísticamente independientes: el prior tiene solo n+1 mundos. Su dificultad es de **acceso mediante lecturas de coordenadas**, no una afirmación de entropía de n bits. Un oráculo que entregue el predicado f en una llamada puede eliminar las n lecturas; precisamente por eso se estudia como otra tecnología en §6. En F sí hay L bits independientes. Los parámetros independientes del experimento son tamaño, relaciones, precio/interfaz, prior y umbrales; η/ρ/C dependen de ellos y de la política.

Sea K=min(n,k) y u=K/n. Para optimizar el riesgo a una eficacia dada, basta una política que consulta antes del primer A/B, elige A/B/parada segura y, si elige una alta, termina los L segmentos utilizando el f revelado. Consultas posteriores al primer efecto no evitan V y pueden eliminarse. Una rama con más de k consultas no puede tener Ttec y puede pararse de forma segura. M en una ruta de ε=0 impide Ttec; sustituir esa rama por parada segura no empeora η ni ρ. Tras un cero se conoce f=0 y B puede terminar sin riesgo. Se pueden añadir consultas hasta K en la rama de todos unos: información adicional solo permite evitar una decisión incorrecta. Esta reducción es una envolvente que facilita el problema; el control final se ejecuta dentro del contrato original.

Fijada la semilla de una política, mientras las respuestas sean unos el orden de consultas es fijo y no depende de qué Bj se oculta. Entre los n mundos Bj, como máximo K detectan un cero. Esto incluye cualquier coordinación/caché por la historia centralizada. En AVG la masa detectada es D=u/2; la masa inválida no detectada es H=(1−u)/2; la masa G es 1/2. Los mundos no detectados y G tienen la misma historia.

### 4.2 Teorema W-AVG: frontera exacta

\[
\boxed{\rho_{\min}^{AVG}(h,u)=
\frac{1-u}{2-u}\max(0,h-u/2).} \tag{W1}
\]

**Prueba.** En la historia no detectada, A y B tienen la misma eficacia técnica. A causa infracciones en masa H, B en masa 1/2; A es al menos tan favorable, por lo que B puede sustituirse por A. Terminar con B en todos los casos detectados ofrece D de eficacia sin riesgo. Si x es la probabilidad de intentar A en la historia restante, η≤D+(1−D)x y ρ≥Hx. Por tanto ρ≥H max(0,h−D)/(1−D), que es W1. Si hay menos de K consultas, completar hasta K y aprovechar la información no empeora el resultado; la misma cota para K es necesaria. Para alcanzar la igualdad, consultar K índices distintos; si se detecta un cero, usar B. Si h>D, intentar A en la historia restante con probabilidad (h−D)/(1−D). Si h≤D, terminar solo una fracción h/D de las historias detectadas. En el caso D=0,h>0 aplica la primera rama. ∎

Hay viabilidad AVG exactamente cuando R≥C0 y r≥W1. El k mínimo es el menor entero 0≤K≤n que satisface esa desigualdad; no se sustituye por una condición solamente necesaria. Para h=1,r<1/2,

\[
K_{min}^{AVG}=\lceil n(1-2r)\rceil. \tag{W2}
\]

### 4.3 Teorema W-WC: frontera exacta y control simétrico

Para 0≤r<h, la condición necesaria y suficiente es

\[
\boxed{(1-u)(h-r)\le r,\quad R\ge C_0.} \tag{W3}
\]

**Prueba de necesidad.** En G, sean x/y las probabilidades de intentar A/B después de consultas con respuesta uno. Entonces ηG≤x+y y ρG≥y. Cada intento A sobre esa historia produce una infracción en al menos n−K mundos Bj, porque comparten las respuestas. Al promediar los Bj y las semillas, ρB-prom≥(1−u)x. Los requisitos WC implican x≥h−r y ρB-prom≤r. Se obtiene W3. Esta prueba no presupone que las consultas ni la política sean simétricas.

**Suficiencia.** Si K<n, elegir uniformemente un subconjunto de K índices. Con cero detectado, completar en B. Sin cero, intentar A con probabilidad h−r, B con probabilidad r, y M/parada con probabilidad 1−h. En G: ηG=h,ρG=r. En cada Bj: ηj=u+(1−u)h≥h y ρj=(1−u)(h−r)≤r. En esas historias ambas opciones altas son todavía epistemológicamente posibles; no se supera un rechazo conocido. Si K=n, f es conocido y se completa siempre con su modo admisible; no se intenta B en G. ∎

Por tanto,

\[
K_{min}^{WC}=\left\lceil n\max\left(0,1-\frac r{h-r}\right)\right\rceil. \tag{W4}
\]

Para r≥h, un intento aleatorio de ejecución con probabilidad h satisface el techo de riesgo trivialmente. Con K=0, AVG y WC permiten ρ mínimo h/2 mediante el control adecuado; una banda imposible genuina exige r<h/2. Por ejemplo, con h=1,r=1/4, AVG necesita K/n≥1/2 y WC K/n≥2/3. Los redondeos y R=C0+cKmin son inclusivos.

Los pares de objetivos: M cuesta C0 y no infringe; iniciar A y adaptar los segmentos restantes al recibo completa con ηAVG=1 y ρAVG=1/2 a C0; para el control WC barato elegir A/B con moneda justa logra ηω=1,ρω=1/2 en cada mundo. Consultar hasta un cero o los n hechos consigue η=1,ρ=0 en todos los mundos, con coste máximo C0+cn. Así todos los pares tienen testigos y la inviabilidad conjunta es informativa para h>2r.

### 4.4 Teorema de familia densa: coste cuadrático frente a ejecución lineal

Elegir n(L)=L(L−1)/2 relaciones normativas distintas, por ejemplo una por par de segmentos; L≥2. No se obliga a ejecutar n actos materiales ni a listar un bit en cada nombre de acción: A/B son dos procedimientos de L pasos sometidos a un mismo predicado sobre esas relaciones. Para b,g,c fijos y h>2r, W1/W3 requieren u≥u*>0 constante, independiente de L. En AVG esto se sigue de la continuidad de W1 y W1(h,0)=h/2>r; en WC, u*=(h−2r)/(h−r)>0. Luego

\[
C_{crit}-C_0=\Theta(cn)=\Theta(L^2),\qquad C_0=\Theta(L).
\]

**Forma universal.** Para toda política/equipo de la clase de acceso a hechos, para todo presupuesto relativo finito λ≥0 y para todo h>2r, existen L arbitrariamente grandes tales que ningún miembro de esa clase logra η≥h y ρ≤r bajo R=(1+λ)(b+gL). En realidad, para esos tamaños **todas** las políticas fracasan en al menos un requisito. El control de consulta completa demuestra que el problema es físicamente ejecutable y que recursos mayores lo resuelven.

El orden de cuantificadores es: fijar clase/costes/umbrales; existe una familia; para todo λ finito existe L0; para todo L≥L0 y toda π admitida hay fallo conjunto. No se escoge la distribución después de conocer π. Aumentar el número de agentes o reducir las distancias puede mejorar el tiempo, pero no la suma de hechos nuevos leídos si mantiene esta interfaz y precio mínimo. No se impone este perfil de costes a toda arquitectura física.

### 4.5 Coste esperado: la dificultad persiste sin presupuesto por traza

En este perfil alternativo Ttec se define por finalización/calidad/plazo y se limita **E[C]**, en vez de exigir C≤R en cada traza. Hay preparación b cobrada en todo ensayo iniciado. Sea Q el total de hechos leídos con cargo, sin contar dos veces el mismo evento; lecturas repetidas reales sí se cobran.

\[
\boxed{E[Q]\ge\frac n2(\eta-2\rho)_+,\qquad
E[C]\ge b+gL\eta+\frac{cn}{2}(\eta-2\rho)_+.} \tag{W5}
\]

**Prueba directa.** Fijar una semilla. Seguir la historia G hasta el primer efecto alto o la terminación; sea qG el número de índices distintos consultados, ≤n. Todo Bj cuyo índice no está entre ellos reproduce esa historia. Si el primer efecto es A, hay riesgo al menos (1−qG/n)/2 y η≤1; por ello η−2ρ≤qG/n. Si es B, G ya infringe, ρ≥1/2 y η−2ρ≤0. Si no hay efecto alto en G, tampoco lo hay en los Bj no detectados; entonces η≤qG/(2n), que también da la desigualdad. Estos η y ρ son sobre el prior para la semilla fijada; la eventual adaptación tras el efecto no borra la infracción. Promediar semillas da η−2ρ≤E[qG]/n. Como G tiene masa 1/2 y allí se pagan al menos qG lecturas, E[Q]≥E[qG]/2. Finalmente cualquier Ttec paga al menos gL material y todo ensayo paga b, con cargos informativos adicionales no solapados. ∎

Para η≥h y ρ≤r<h/2, E[C]≥b+gLh+(cn/2)(h−2r)=Ω(n). La consulta completa con orden uniforme y parada en el primer cero tiene E[Q]=(3n+1)/4 y η=1,ρ=0: en G lee n y en los Bj la posición esperada del cero es (n+1)/2. Por tanto la escala Θ(n) es alcanzable para éxito seguro. Con n=Θ(L²), también el coste esperado necesario es cuadrático. W5 es una cota, no una frontera exacta de coste esperado para todos los h/r.

Con hasta k0 hechos concretos disponibles inicialmente, aunque se concedan gratis, el mismo acoplamiento sustituye qG por k0+qG y da E[Q]≥[n(η−2ρ)−k0]+/2. En el perfil de presupuesto, u pasa a min(n,k0+k)/n. Si k0=O(L), la familia densa conserva su dificultad. Esta concesión favorable no autoriza omitir en una implementación el coste real de producir información previa.

## 5. Consultas generales: qué permite el argumento de capacidad

La propuesta recibida permite una operación con N salidas a coste al menos c log2N. Eso es más amplio que leer bits concretos: una salida binaria puede contestar un predicado global. Para esta clase se conserva una cota necesaria, pero no las fronteras exactas F2/F4.

**Lema de transcripciones.** En F, supóngase que el único ramificado de historias exitosas sin infracciones procede de operaciones informativas finitas con N salidas y precio ≥c log2N; los precios/metadatos no informan gratuitamente y los recibos materiales sin infracción no añaden ramas. Con s=R−C0≥0,

\[
\sigma\le\min(1,2^{s/c-d}). \tag{G1}
\]

**Prueba.** Fijar la semilla y podar el árbol a historias S. Cada nodo informativo conserva como máximo N hijos. Asignar peso 1/N a cada arista de ese nodo. La suma de productos de pesos de hojas es ≤1 por inducción en el árbol. Para cada hoja, ∏N≤2^(s/c), por lo que su peso es ≥2^(−s/c); hay como máximo 2^(s/c) hojas. Cada hoja fija una ruta con al menos d elecciones altas acertadas y es compatible con como máximo 2^(L−d) mundos. Multiplicar y dividir por 2^L produce G1. Promediar semillas preserva la cota. El árbol tiene un máximo finito de eventos; nodos N=1 se contraen. Los recibos sí revelan hechos, pero la rama exitosa de una acción elegida tiene un solo resultado «admisible». ∎

La condición h−r≤G1 es solamente necesaria. Ejemplo exacto F con L=d=1,k=0,h=3/4,r=1/4: h−r=q=1/2, pero el mínimo riesgo real es h/2=3/8>r. Cumplir la cota débil no demuestra existencia.

Además, permitir a coste c la consulta binaria «¿χ es todo cero?» y actuar solo cuando responda sí da η=σ=2^(−L),ρ=0. Para L=3,k=1, la desigualdad local ρ≥(2^(d−k)−1)σ sería falsa. G1 sí se conserva. El tamaño de salida no equivale al número de bits concretos reconstruidos, y un certificado raro puede permitir actuar sin riesgo. No se invoca Fano ni un teorema minimax sin comprobar su reducción: las pruebas anteriores son directas.

## 6. Tecnologías: reducción, eliminación y cambios de clase

«Eliminar» debe indicar el dominio. Son distintos: vaciar la banda para todo R≥C0; resolver un presupuesto concreto; hacer que cualquier margen relativo λ>0 funcione para tamaños grandes; o eliminar V dejando un coste necesario para η. No hay una única clasificación sin interfaz, productor, distribución, umbrales y costes.

### 6.1 Cambios que conservan el acceso a hechos

Si una tecnología permite solo lecturas de hechos individuales con coste total mínimo cmin>0, sin hechos suficientes iniciales ni barrera, las pruebas inferiores se aplican con k≤⌊(R−C0)/cmin⌋. Una cota inferior de precio basta para imposibilidad; un control superior necesita además consultas disponibles y su precio máximo. Caché, inferencia sobre hechos ya vistos, equipo centralizado y paralelismo no revelan un hecho nuevo no observado. Abaratar c reduce la banda. En F puede volver suficiente un margen relativo antes insuficiente; en W densa cualquier cmin fijo positivo mantiene Ω(L²), si C0 sigue O(L).

Memoria de bindings válidos ya comprobados puede eliminar el problema en una secuencia estática con datos suficientes. No se afirma que «la caché nunca ayuda»: la familia difícil usa hechos nuevos que no están en la memoria. Una estructura/prior favorable puede hacer suficiente una predicción barata; el contraejemplo de M10 con prior 9/10 debe conservarse. Estos casos cambian la incertidumbre relevante.

### 6.2 Certificado suficiente con precio total f(n)

En W añadir una consulta disponible que entrega el f actual, autenticado y aplicable, por precio total f(n)>0. Contar emisor, producción, transporte y uso; si el productor debe leer n hechos nuevos a precio c, no atribuirle arbitrariamente un precio logarítmico. El certificado es un supuesto de servicio hasta medir/verificar su implementación.

Si esa es la única interfaz añadida y cuesta f(n) en toda llamada, la frontera exacta de presupuesto se vuelve

\[
C_{crit}^{nuevo}=C_0+\min(cK_{min}^{viejo},f(n)). \tag{T1}
\]

Por debajo de f(n), ninguna ruta Ttec puede usarlo y queda la clase antigua; por encima permite η=1,ρ=0. Un intento que no puede terminar por ese cargo se puede sustituir por parada segura sin mejorar el riesgo mínimo. El mínimo de umbrales es entonces exacto. En F vale el mismo argumento para un certificado del vector suficiente de bindings, con precio f(L).

Un precio positivo deja una banda absoluta cerca de C0 **solo cuando el perfil original ya tenía una banda no vacía**. Sin embargo, puede eliminar el obstáculo para un criterio relativo:

| Precio completo de certificado en W, n=Θ(L²), C0=Θ(L) | Margen relativo necesario y efecto |
|---|---|
| f(n)=O(1) o O(log(1+n)) | f(n)/C0→0: cualquier λ>0 funciona eventualmente; queda una banda absoluta de anchura ≤f(n). |
| f(n)=Θ(√n) | Margen relativo de orden constante; importa su coeficiente. |
| f(n)=Θ(n) | La anchura sigue cuadrática y la razón respecto a C0 crece sin límite. |
| Servicio suficiente ya incluido en C0 | No hay cargo adicional: puede vaciar toda la banda R≥C0. La producción sigue pagada dentro del coste base. |

«Sublineal en n» por sí solo no basta: n^(3/4) es sublineal pero crece como L^(3/2) en W. La comparación correcta es f(n(L))/C0(L). Una ley de lotes f(b)=c log b da f(1)=0: consultas singleton gratuitas resolverían los datos. Se necesita un contrato de lotes coherente, por ejemplo una tarifa de preparación positiva y log(1+b), o una única interfaz global con precio declarado. No se convierte una cota inferior logarítmica en la existencia de un certificado a ese precio.

### 6.3 Barreras y ejecución admisible por construcción

Una barrera preefecto que comprueba el binding puede producir ramas informativas **sin infracción**. Ya no cumple la hipótesis sobre recibos de F/G1. Reutilizar esas cotas sin rehacer la prueba sería incorrecto. Impedir una infracción tampoco garantiza que exista o se alcance una alternativa suficientemente buena.

**Control con despacho autorizado.** Modificar el ejecutor para que, en cada segmento elegido alto, seleccione/ejecute la opción alta admisible a cargo adicional a≥0, manteniendo revisiones y precio material g. No necesita revelar χ/f al agente. En el subperfil que solo admite M y ese despacho (sin apuestas desprotegidas ni consultas alternativas), para alcanzar d opciones altas hace falta exactamente ad adicional. Por tanto η=0 si R<C0+ad, y η=1,ρ=0 es posible en R≥C0+ad. Se elimina el componente de riesgo, pero si a>0 persiste un dilema coste–eficacia. Si a=0 adicional porque el trabajo ya está incluido en g, η=1,ρ=0,C=C0 en todos los mundos: se elimina la inviabilidad conjunta. No significa que el trabajo físico sea literalmente gratuito ni que solo exista ese diseño.

Mantener g pequeño e independiente de n bajo ese nuevo ejecutor es un supuesto que requiere evidencia de implementación. Si el proveedor reconstruye f mediante n lecturas frescas con tarifa c, su coste completo debe aumentar a o g; rebautizar ese trabajo como «baseline» no lo elimina respecto al presupuesto de la arquitectura anterior. El control a=0 adicional describe una capacidad admisible por construcción o una comprobación realmente financiada en ese baseline, no una exención contable del productor.

**Contraejemplo a contar rechazos como bits pagados.** En un subperfil de los mismos mundos F con ε=0, cuya única interfaz de información/ejecución alta es la barrera (sin consultas de coordenadas ni certificados adicionales), se puede comprobar una primera opción sin efecto, con 0<a≤g. Toda comprobación fallida cuesta a y toda opción admitida/ejecutada cuesta g, incluyendo su comprobación y revisiones propias. Tras un rechazo se elige la alternativa correcta a precio g. No se omiten cargos: cada finalización paga gL+a veces el número de rechazos. Con presupuesto C0+ak, una política se detiene después del rechazo k+1, ya cobrado, porque no puede financiar una finalización suficiente; ese cargo cabe en la reserva material no ejecutada ya que a≤g. No existe una observación gratuita por falta de presupuesto. Si hubo ≤k rechazos, queda presupuesto para todas las aceptaciones. Por tanto los segmentos se completan exactamente cuando el número de primeras opciones incorrectas es ≤k. En AVG, independencia de los bindings da

\[
\eta_{max}=2^{-L}\sum_{j=0}^{\min(k,L)}{L\choose j},\qquad\rho=0. \tag{T2}
\]

Escoger primeras opciones con monedas justas logra el mismo valor en cada mundo, así que también es la frontera WC. Si se añade esa barrera manteniendo otras consultas, T2 es un control alcanzable; la frontera óptima de la clase ampliada puede mejorar y no se identifica automáticamente con T2. Adaptar decisiones no mejora AVG: cada binding nuevo sigue siendo justo antes de probarlo. Probar más de dos veces o parar antes no mejora finalización. Para L=3,k=1 resulta η=1/2, superior a 2^(1−3)=1/4. El recibo de aceptación revela información sin cargo **adicional** y el rechazo no viola; T2 no contradice F, cambia su kernel y su distribución de cargos. Un veto que cobra también cada prueba admitida tendría otro modelo. Estos precios son un control matemático, no una medición de un producto.

### 6.4 Cambios estructurales y tecnologías que pueden perjudicar

Una ruta común admisible con calidad suficiente, tolerancia que haga suficiente M, un predicado siempre conocido o capabilities que excluyan toda opción prohibida pueden eliminar la necesidad de distinguir mundos. Eso puede resolver completamente un dominio y no exige revelar gratuitamente todos los bits. No se demuestra un «único tipo de tecnología» que elimine todo trilema posible.

Una tecnología también puede aumentar C0, cobrar coordinación redundante, introducir información obsoleta o bloquear una opción admisible. Por ejemplo, sumar un cargo obligatorio t>0 a toda finalización desplaza el mínimo material a C0+t y vuelve η=0 a R=C0; no hace falta atribuir mejoras por llamarse validación. Un certificado viejo/no aplicable no es el servicio suficiente de T1. No se afirma una degradación real sin verificar el contrato y sus resultados.

**Conclusión condicional precisa:** toda tecnología que preserve la clase de lecturas de hechos frescos con precio mínimo fijo positivo, ejecución lineal y ausencia de información suficiente/barrera hereda la familia densa imposible a cualquier margen relativo fijo. Fuera de esa clase, el resultado depende de qué capacidad añade y a qué coste completo; T1/T2 y el despacho autorizado exhiben reducción, cambio de frontera y eliminación. No existe una prueba de «toda tecnología positiva conserva el trilema» bajo las hipótesis débiles del borrador.

## 7. Auditoría de la propuesta recibida y correspondencia

La copia recibida se conserva byte a byte. Los cambios se formulan en este sucesor, no como una corrección silenciosa del original.

| Afirmación/laguna del borrador | Disposición y reparación |
|---|---|
| Bits por capa en lugar de ejemplos aislados | F demuestra el objetivo; W prueba una dificultad más fuerte con hechos normativos separados de pasos. |
| No preefecto literal, pese a permitir consultas pagadas | Se permiten consultas registradas; se excluye una prueba material gratis/no registrada del binding. |
| Recibos sin información | Revelan el binding; solo carecen de ramificado adicional en la parte sin infracciones. |
| Cota σ y η−ρ interpretada como frontera exacta | G1 es necesaria; F1/W1/W3 aportan desigualdades más fuertes y controles que alcanzan la frontera. |
| Precio mínimo de consulta usado como precio disponible | Se separan precio inferior para imposibilidad y disponibilidad/precio superior para construcción. |
| Certificados/globales tratados como lectura de coordenadas | §5 conserva G1 y da un contraejemplo explícito a transferir F1 a predicados arbitrarios. |
| Primera X repetida tras conocer χ en M02 | Control con recibo y adaptación; no se omite el rechazo de prohibiciones conocidas. |
| Cualquier precio positivo conserva toda dificultad | T1 distingue banda absoluta de margen relativo y contempla servicios incluidos en C0. |
| f(b)=c log b | Singleton gratuito; exigir contrato de lotes/preparación coherente. |
| Barrera y consultas sujetas a la misma cota | Cambia el kernel; T2 refuta esa transferencia. |
| Eficacia legítima implica siempre mero dilema | F4 conserva un techo separado de riesgo cuando es vinculante. |
| Únicamente comprobación gratis elimina el trilema | Despacho autorizado incluido en g y rutas comunes también lo eliminan en dominios declarados. |

R01: se mantienen historia observable, revisión propia, mandato estable, óptimo admisible independiente, todos los conectores/mezclas, V irreversible, coste/plazo y distinción entre prueba de clase y campaña finita. Las nuevas F/W son construcciones suplementarias; no se afirma que el texto base contuviera bits independientes, n=Θ(L²), estos priors o estas tarifas. Geometría/N/distancias no bastan para determinar el número de hechos frescos. E1–E7, 00M/00N y el caso HF requieren correspondencia posterior; ninguna plataforma ni selector hereda automáticamente los teoremas.

Fuente primaria de definiciones: [Buhrman y de Wolf, preprint de 2002](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf), introducción y §§3.1–3.2/4.1: consulta adaptativa de bits, distribuciones de árboles deterministas y certificados. Estas definiciones motivan fijar la interfaz. Las cotas F/W/G/T se demuestran aquí directamente; no se atribuyen a esa fuente. El documento no es una revisión exhaustiva de resultados posteriores ni una afirmación de novedad. El coste esperado W5 y el máximo por traza son perfiles diferentes.

## 8. Verificación, siguiente trabajo y prompt completo de revisión

Ejecutar `python3 verify_trilemma.py > /tmp/TRILEMMA_CHECKS.json` y comparar con TRILEMMA_CHECKS.json. El programa utiliza fracciones exactas, enumera por programación dinámica las decisiones de consulta/M/X/Y/parada y recibos de F para L≤3, y enumera árboles de consulta de W para n≤4. Verifica desigualdades para todas las políticas deterministas en esos dominios y controles aleatorios explícitos; la convexidad extiende las desigualdades comprobadas a sus mezclas. Además comprueba fronteras, igualdades, costes, W5, certificados, barrera y contraejemplos. Es verificación por el mismo agente; no un oráculo C05 independiente ni prueba asistida por un sistema formal. El registro de release conserva hashes, entrada, comandos, regresiones y límites.

Prioridad siguiente: revisión independiente M05/C05 del **contrato y de las demostraciones**, seguida por correspondencia M07 y una implementación neutral del oráculo. Antes de invertir en tecnologías concretas, identificar hechos frescos, interfaz de certificados/barrera y coste del productor; contrastar predicciones en una campaña registrada. No sustituir esto por probar modelos y buscar luego una desigualdad que los explique.

**Prompt para otro agente:**

> Revisa R01 en el commit publicado, empezando por README.md, M03_M04_TRILEMMA_THEOREMS.md, TRILEMMA_CONTRACT.json y la propuesta recibida. Lee M01, M02 y M10 para comprobar que la extensión no altera e/a/q, rechazo conocido, recibos ni costes históricos. Tu objetivo es intentar refutar las pruebas, no confirmar los ejemplos. Comprueba F1 para toda historia/adaptación/aleatoriedad, incluyendo consultas intercaladas y primeras observaciones por efectos; F2/F4 deben tener construcción que alcance cada frontera. Comprueba la reducción a primera acción alta en W, las medidas equilibradas G/Bj, el argumento WC sin presuponer simetría y W5 sin confundir presupuesto duro con coste esperado. Verifica redondeos, igualdad, bandas vacías, todos los conectores, abstención, memoria, pooling y datos previos. Intenta certificados binarios globales, priors asimétricos, rutas comunes, tarifas de lotes y barreras; determina exactamente qué hipótesis cambian. Examina T1, el cargo del productor, T2 y despacho autorizado; distingue eliminación absoluta/relativa y riesgo cero frente a coste adicional. Reproduce el comprobador y desarrolla un método independiente para un dominio pequeño sin copiar su recurrencia. No cierres M05/C05 por reutilizar el programa del autor. Conserva source/fixtures/reportes/manifests históricos, registra commit, UTC, comandos y hashes. Entrega por cada teorema: VALIDADO EN SU CLASE, CONTRAEJEMPLO con traza, o LAGUNA con supuesto necesario. No extrapoles a toda tecnología, distribución, geometría, HF o EA; M06/M07 y revisión independiente siguen abiertos hasta su evidencia.
