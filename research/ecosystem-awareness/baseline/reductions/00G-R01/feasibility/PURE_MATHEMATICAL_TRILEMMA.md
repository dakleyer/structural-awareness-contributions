# R01 — Viabilidad matemática del trilema por configuraciones

M12 en desarrollo · Versión 0.1 · 4 de octubre de 2026 · Sin intervenciones tecnológicas nuevas.

[Entrada al estudio](./README.md) · [Plan](./WORKPLAN.md) · [Continuación y revisión](./CONTINUATION_PROMPT.md) · [Escenario conservado](../Escenario-creatividad-validacion.md#213-inventario-de-configuración).

Esta formulación recoge la corrección del usuario: hay configuraciones en las que se alcanzan las tres condiciones; hay familias en las que cada par es alcanzable y la tercera condición impide la conjunción. La prueba debe cuantificar sobre **todas** las políticas admitidas. Los ejemplos y diagnósticos archivados son corroboraciones acotadas. Aquí se ofrece una derivación simbólica para la familia F, con necesidad y suficiencia, y se conserva como pendiente la transferencia matemática al escenario R01 completo.

## 1. Configuración, mundo, política y resultados

Se distinguen configuración θ, mundo oculto ω y política π. θ determina el problema y sus recursos; ω determina hechos que la política aún no conoce; π utiliza solo su historia observable. Una política común debe funcionar sin conocer la etiqueta de ω. La aleatoriedad interna es independiente del mundo antes de observarlo.

El inventario del escenario ya contiene estas dimensiones; no se sustituye por una colección nueva de casos aislados:

| Dimensión de R01 | Parámetros | Papel en la prueba |
|---|---|---|
| Tarea y población | L pasos/segmentos, N agentes, obligación, principal, unidad individual/colectiva | F usa una tarea colectiva y L hechos independientes; no presupone N tareas distintas. |
| Geometría | Distancias, lados, dispersión, conexiones, correlación de posiciones | La geometría de F no revela hechos normativos; no se prueba aquí una ley de dureza en la distancia. |
| Beneficios y mundos | Medias, dispersión, correlaciones, prior, semillas/versiones | F fija beneficios 1/2 y un prior uniforme; los beneficios no filtran el binding. |
| Composición | Paridad, conjunción, mezcla; número n y ubicación de relaciones/testigos | Son familias distintas. L no determina por sí solo n ni la cantidad de información decisiva. |
| Recursos y cargos | Presupuesto agregado R, plazo T, c_e, c_v, ejecución, mensajes, mantenimiento | Se distingue trabajo total de latencia y presupuesto máximo de coste esperado. |
| Red | Topología, latencia y disponibilidad de comunicación | Conceder coordinación perfecta facilita F; su cota de trabajo no es una cota temporal. |
| Controles de política | Radio R_e, esfuerzo, k_a/k_d, orden de inspección, v, beta, s, w_s, memoria, reutilización, rechazo, reintento, abstención | Si la afirmación cubre todas las políticas, estas decisiones pertenecen a π; no se congela una ventana incompetente para producir el resultado. |
| Cantidades derivadas | Q propuestas únicas, cobertura, duplicación, coste, riesgo, eficacia | Son resultados del mundo y de π; no variables independientes seleccionadas después para forzar una conclusión. |

Referencia: §§2.6 y 2.11–2.15 del [escenario](../Escenario-creatividad-validacion.md). El submodelo F exige lectura básica de hechos, con coste declarado, sin certificados globales iniciales ni barreras gratuitas. Esa es la clase base; todavía no se comparan tecnologías.

Sean Cθ(π) el coste máximo de una ejecución, ρθ(π) la probabilidad de al menos una infracción material y ηθ(π) la probabilidad de completar con calidad técnica suficiente. Fijar antes de ejecutar R≥0, 0≤r≤1 y 0<h≤1. Escribir:

\[
B_C=[C_\theta(\pi)\le R],\qquad
B_R=[\rho_\theta(\pi)\le r],\qquad
B_E=[\eta_\theta(\pi)\ge h].
\]

η es eficacia **técnica** suplementaria: una infracción no se acredita como éxito legítimo de R01. Si se exige éxito legítimo, se utiliza σ=P(calidad suficiente y ninguna infracción), con otro umbral y otra frontera. No se mezclan ambos teoremas.

Π(θ) contiene las políticas finitas legales para esa interfaz, incluidas las que gastarían más que R. El objetivo de coste se impone mediante B_C: restringir Π a políticas baratas de antemano haría imposible expresar correctamente el control riesgo–eficacia a coste elevado. Los controles construidos tienen plazo suficiente fijado en θ, común a las comparaciones.

## 2. Regiones y cuantificadores correctos

Para un subconjunto S de {C,R,E}, definir

\[
A_S=\{\theta:\exists\pi\in\Pi(\theta)\quad
\bigwedge_{i\in S} B_i(\theta,\pi)\}.
\]

La región viable es V=A_CRE. Las regiones solicitadas por pares son

\[
U_{CR}=A_{CR}\setminus V,\quad
U_{CE}=A_{CE}\setminus V,\quad
U_{RE}=A_{RE}\setminus V.
\]

Por ejemplo, θ∈U_CR significa que existe una política barata y segura, y que **ninguna** política barata y segura alcanza la eficacia exigida. No significa que la eficacia sea imposible si se permite pagar más.

El objetivo mínimo es V≠∅ y U_CR,U_CE,U_RE≠∅, con familias parametrizadas explícitas. Una forma más fuerte, que F satisface, es:

\[
\exists\mathcal U\ne\varnothing\quad
\forall\theta\in\mathcal U:\quad
\left(\bigwedge_{S\in\{CR,CE,RE\}}\exists\pi_S\ B_S\right)
\ \land\
\left(\forall\pi\in\Pi(\theta)\ \neg(B_C\land B_R\land B_E)\right).
\]

Las tres políticas π_S pueden ser distintas. Las regiones U_CR, U_CE y U_RE pueden solaparse; no forman necesariamente tres áreas disjuntas. Que cada par tenga una estrategia no proporciona una estrategia común para los tres. Tampoco se exige que cada ejecución de cada política infrinja: lo que no se alcanza son las garantías conjuntas en esa configuración.

## 3. Familia F: contrato sin intervenciones

L≥1 segmentos, con conectividad completa entre opciones de segmentos adyacentes. En cada segmento hay M, segura y de beneficio 1, y X/Y, de beneficio 2. El binding χ_i∈{0,1} determina cuál de X/Y es admisible. Los L bindings son independientes y equiprobables. El óptimo admisible vale 2L en todo mundo.

La tolerancia 0≤ε<L requiere J≥2L−ε en una ruta completa; por tanto se necesitan d=L−⌊ε⌋≥1 opciones altas. Cada ruta completa paga C0=b+gL, b≥0,g>0. Leer un binding concreto cuesta c>0, con todas las etapas de acceso incluidas. Reutilizar hechos adquiridos es válido. No hay metadatos, geometría, mensajes, beneficio o revisión gratuita que revelen un binding nuevo. Se admite cómputo local y coordinación perfecta como envolvente favorable a cualquier N finito, cobrando el trabajo informativo agregado.

Una opción alta desconocida puede ejecutarse. El efecto revela su binding después de producirse. Una infracción material no se borra, aunque se continúe y se complete técnicamente. Se rechaza toda opción ya conocida como prohibida. No se impone un aborto obligatorio que cambie la definición de eficacia. Cada instancia tiene un horizonte finito suficientemente amplio para leer los d hechos y completar la tarea.

En AVG se promedia el prior uniforme y la aleatoriedad de π. En WC se exige η_ω≥h y ρ_ω≤r en cada mundo, con una misma π aleatoria. La imposibilidad AVG implica la WC; el control de suficiencia dará las mismas tasas en cada mundo.

## 4. Teorema de frontera exacta, para toda política

Para R≥C0, definir

\[
k=\left\lfloor\frac{R-C_0}{c}\right\rfloor,\quad
m=\max(0,d-k),\quad q=2^{-m}.
\]

**Teorema F.** Para AVG y para WC con políticas aleatorias,

\[
\boxed{\theta\in V\quad\Longleftrightarrow\quad
R\ge C_0\ \text{y}\ r\ge h(1-2^{-\max(0,d-k)}) .}
\]

**Necesidad.** Si R<C0 no hay ruta suficiente financiable y η=0. Para R≥C0, cualquier historia de éxito técnico sin infracción necesita d efectos altos y puede financiar a lo sumo k lecturas pagadas. Debe acertar al menos m primeras apuestas sobre bindings distintos aún desconocidos.

Antes de la primera infracción, cada apuesta de este tipo acierta con probabilidad 1/2 condicionado a toda la historia anterior. Independencia, selección adaptativa, memoria y consultas a otros índices no cambian ese hecho. Una nueva lectura puede evitar una apuesta, pero no informa gratuitamente de otra coordenada. Los recibos de apuestas previas se admiten íntegramente.

Sea a_j la probabilidad de entrar en la apuesta j antes de cualquier infracción. Se cumple a_1≤1 y a_{j+1}≤a_j/2. Parar o consultar entre apuestas puede reducir esa probabilidad. Si σ=P(éxito técnico sin infracción), para m≥1:

\[
\sigma\le a_m/2\le 2^{-m}.
\]

Los eventos de primera infracción en cada apuesta son disjuntos y tienen probabilidad a_j/2. Como a_j≥2^{m-j}a_m para j≤m,

\[
\rho\ge\sum_{j=1}^m a_j/2
\ge(2^m-1)a_m/2
\ge(2^m-1)\sigma.
\]

Además η≤σ+ρ. Por tanto ρ≥(1−2^{-m})η≥(1−2^{-m})h. Para m=0 la condición inferior de riesgo es trivial. Las ramas que gastan demasiado no pueden aportar éxito financiable; detenerlas antes de más apuestas no elimina ningún éxito y solo puede reducir riesgo. La demostración cubre políticas aleatorias y adaptativas directamente. Para WC, las garantías por mundo implican las garantías AVG, de modo que la misma condición es necesaria.

**Suficiencia.** Con probabilidad h intentar una ruta con d opciones altas: leer min(k,d) bindings y elegir sus opciones admisibles; en los m restantes elegir X/Y con monedas independientes; usar M en los demás segmentos. Con probabilidad 1−h ejecutar M. Los recibos se conservan y ninguna opción futura conocida como prohibida se ejecuta. El coste máximo es C0+c min(k,d)≤R, y en cada mundo

\[
\eta_\omega=h,\quad
\sigma_\omega=h2^{-m},\quad
\rho_\omega=h(1-2^{-m}).
\]

El control alcanza exactamente la cota inferior, incluso en la igualdad. ∎

Esto prueba una frontera, no únicamente ejemplos de fracaso. La prueba utiliza la interfaz, el prior y los cargos declarados. Su validez dentro de F y su transferencia al escenario completo son obligaciones diferentes.

## 5. Regiones viables, tres pares y no vaciedad

Si 0≤r<h, definir j_allow como el mayor entero j≥0 que satisface h(1−2^{-j})≤r. Entonces

\[
j_{allow}=\left\lfloor\log_2\frac h{h-r}\right\rfloor,
\qquad C_{crit}=C_0+c\max(0,d-j_{allow}).
\]

Las igualdades se deciden con la desigualdad original; no con un logaritmo redondeado numéricamente. Para este perfil, V es R≥Ccrit; la banda con trilema es C0≤R<Ccrit. Si r≥h, la banda desaparece y basta R≥C0. El límite R=Ccrit es viable. No se afirma una banda no vacía donde los umbrales la vacían.

En la banda no vacía U={θ:C0≤R<Ccrit}, estos controles consiguen los pares:

| Par alcanzado | Política constructiva | Coste, riesgo y eficacia | Tercer objetivo |
|---|---|---|---|
| Coste y riesgo | Ejecutar M en todos los segmentos | C=C0≤R; ρ=0; η=0 | η<h. Por el teorema, ninguna política que preserve coste y riesgo alcanza h. |
| Coste y eficacia | Ejecutar d opciones altas sin consultas, con monedas justas; M en las demás | C=C0≤R; η=1; ρ=1−2^{-d} | ρ>r en esta banda. Ninguna política barata y eficaz respeta el techo r. |
| Riesgo y eficacia | Leer los d bindings y ejecutar las opciones admisibles | C=C0+cd; ρ=0; η=1 | C>R. Ninguna política segura y eficaz alcanza también el presupuesto. |
| Las tres | Control del teorema con consultas suficientes y probabilidad de intento h | C≤R; ρ≤r; η=h | Existe en R≥Ccrit; no contradice la banda anterior. |

**No vaciedad y tamaños arbitrarios.** Fijar b≥0,g>0,c>0,0<h≤1 y 0≤r<h. Elegir cualquier entero d>j_allow, L≥d, ε=L−d y R=C0. Entonces m=d y h(1−2^{-d})>r, de modo que θ∈U_CR∩U_CE∩U_RE. Hay infinitos tamaños eligiendo ε=0 y L>j_allow. Para los mismos tamaños, cambiar únicamente R a C0+cd permite las tres en todos los mundos. Así se prueban familias inviables y viables sin cambiar objetivos después de ver resultados.

Para cualquier N finito, el mismo argumento cubre reparto de lecturas entre agentes con coordinación perfecta si C es agregado y no hay hechos previos adicionales. No se concluye que más agentes o más distancia hagan el problema difícil por sí mismos. El régimen de presupuesto por agente, latencia y búsqueda geométrica requiere su propio contrato.

## 6. Qué significa «solo una»

En el espacio de pares (θ,π) se pueden clasificar las ocho firmas de cumplimiento (B_C,B_R,B_E). Una firma con solo un objetivo bueno describe una política y sus resultados; **no prueba** que otra política de esa configuración no consiga un par.

Para afirmar que una configuración permite solamente el objetivo i entre todas sus políticas, haría falta demostrar θ∈A_i pero θ∉A_CR∪A_CE∪A_RE. Esa es una obligación adicional. En F, abstenerse con coste cero y sin efectos es barato y seguro para R≥0,r≥0: θ∈A_CR siempre. Por tanto esta región exclusiva de «solo uno» está vacía dentro del contrato actual. Si se exige una entrega mínima para considerar una política admisible, cambia el contrato y hay que volver a probar sus lemas; no se introduce ese requisito para fabricar una conclusión.

El plan conserva ambas interpretaciones: firmas de resultados y regiones de posibilidades. La prueba del trilema por pares no necesita que existan ocho regiones exclusivas de configuraciones.

## 7. Estado de validación y obligaciones restantes

| Afirmación | Evidencia actual | Validación que falta |
|---|---|---|
| F tiene una banda con todos los pares alcanzables y triple imposible | Derivación simbólica anterior para todas las políticas de su clase, control que alcanza la frontera y prueba de no vaciedad | Reconstrucción y auditoría simbólica independiente M16; no se declara realizada. |
| F también tiene regiones viables | Control explícito con consultas suficientes, incluido el borde | Auditoría junto con la necesidad. |
| Lo anterior es un teorema del R01 completo | Correspondencias parciales y escenario conservado | M17: embedding/reducción de mundos, todas las observaciones, políticas, efectos y costes; ahora no está demostrado. |
| El trilema ocurre con determinada frecuencia en sistemas reales | No hay campaña registrada que lo establezca | Harness neutral, controles competentes y campaña con configuración congelada. |
| Algunas tecnologías lo reducen o eliminan | Derivaciones y material históricos conservados | Revisión posterior de sus contratos; no forman parte de esta prueba base. |

La familia W y sus fronteras anteriores se conservan en [el borrador F/W](./previous-work/M03_M04_TRILEMMA_THEOREMS.md). Su revisión es una segunda obligación matemática; no se incorpora automáticamente al teorema de R01 por añadir relaciones densas. Los [diagnósticos parciales](./partial-experiments/README.md) no cierran ninguna de las obligaciones universales, de independencia o de transferencia.
