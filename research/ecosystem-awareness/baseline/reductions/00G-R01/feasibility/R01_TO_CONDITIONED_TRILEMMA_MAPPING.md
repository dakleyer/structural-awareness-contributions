# R01 y el trilema condicionado: transferencia y resultado local

Revisión de fondo · 4 de octubre de 2026 · Entrada a1ec3e24970e2d925745e4fc7a5cd8e6c11c11d5.

[Manuscrito revisado](./CONDITIONED_TRILEMMA.md) · [Auditoría](./CONDITIONED_TRILEMMA_DEEP_AUDIT.md) · [Escenario fuente intacto](../Escenario-creatividad-validacion.md) · [Contrato M10](./partial-experiments/historical/M10_RECONCILED_CONTRACT.json) · [Catálogo M02](./partial-experiments/historical/M02_CONJUNCTION_FIXTURE.json).

## 1. Tres objetivos de extensión diferentes

1. **Existencia dentro de R01:** demostrar una subfamilia de configuraciones compatibles donde todas sus políticas observables afrontan el trilema, junto con regiones viables. Basta construir y auditar esa subfamilia; no se necesita traducir cada configuración de R01.
2. **Transferencia condicionada a una instancia:** verificar las hipótesis para ese problema y derivar su cota. Una analogía entre nombres o una selección de trazas no basta.
3. **La misma frontera F para todo R01:** no es válida. R01 permite hechos compartidos, reutilización, información inicial, certificados y otras interfaces. El contraejemplo de §5 muestra concretamente por qué no se puede trasladar q=2^{-(d-k)} a todos sus perfiles.

El punto 1 es el objetivo matemático coherente con la tesis del usuario. No exige demostrar imposibilidad en todas las configuraciones, que incluiría las regiones viables. El escenario fuente SC-H (§1.2) formula una hipótesis empírica sobre una familia finita evaluada; demostrar una cota para todas las políticas de un contrato suplementario no cambia esa especificación sin una revisión explícita.

## 2. La dirección que transfiere imposibilidad

Para cada instancia D de una subfamilia, debe existir un modelo M y una transformación de políticas Φ, común a los mundos, observable y aplicable a **cada** política relevante de D, tal que

$$
\mathrm{Good}_D(\pi)\Rightarrow\mathrm{Good}_M(\Phi(\pi)).
$$

Si M no admite ninguna política buena, tampoco D: una política buena en D produciría una contradicción en M. Tras normalizar unidades y leyes, son condiciones suficientes C_M≤C_D, ρ_M≤ρ_D y e_M≥e_D. Para una frontera exacta también hacen falta controles ejecutables en D que alcancen la cota. No se exige una biyección de todos los algoritmos.

Las implicaciones «objetivo satisfecho en M ⇒ objetivo satisfecho en D», propuestas en una auditoría recibida, sirven para construir alcanzabilidad, pero **no** bastan para transferir una imposibilidad. Tampoco basta escribir Π_D⊆Π_M sin construir una representación de observaciones, costes y efectos: son clases de políticas sobre interfaces distintas.

## 3. Matriz concreta de correspondencia

Las etiquetas siguientes corresponden a la lectura completa del escenario, catálogo, contrato y código M02; no equivalen a revisión externa. El símbolo a de probabilidad en el manuscrito no redefine a, la medida de completion de R01; se mantienen tipos distintos.

| Elemento | Correspondencia con R01 / M02 | Dictamen |
|---|---|---|
| Mundo y obligación | R01 §2.1 fija misión y admisibilidad. M02 usa χ=0/1 y active(m)=1, active(x)=1−χ, active(y)=χ. | IGUALDAD demostrada para la regla M02; otras reglas necesitan contrato. |
| Rutas y conectores | M02 tiene 3 capas m/x/y, 24 conectores de beneficio cero y todas las 27 composiciones. | IGUALDAD del grafo definido; no es todo generador de R01. |
| Calidad | M vale 3; óptimo admisible vale 6 en ambos mundos; ε=0 exige tres nodos altos. | IGUALDAD por suma y regla de admisibilidad. |
| Hechos independientes por segmento | M02 repite el mismo χ en los tres pasos; R01 permite dependencias. | NO IGUALDAD. La frontera F con d=3 no se transfiere. |
| Información previa | Setup da mapa técnico y evidencia de M, sin χ. | IGUALDAD en M02; evidencia inicial de otro perfil puede resolver el problema. |
| Lectura informativa | query_state/check_certificate cuestan 1 y revelan el único χ. | IGUALDAD local; no representan tres lecturas independientes. |
| Resto de consultas | explore, query_mandate, review, decide, reuse sin hecho adquirido, wait y rechazos no revelan χ. | IGUALDAD local de respuestas/cargos antes del primer efecto alto. |
| Observación posterior | Primer efecto X/Y revela χ; ejecutar M no lo revela. | IGUALDAD local; los siguientes pasos deben aprovechar esa información. |
| Riesgo | v_exec es irreversible y registra toda infracción material. ρ=P(v_exec=1). | IGUALDAD con M02/M10 y R01 §1.4; no se identifica riesgo con daño. |
| η técnica | Probabilidad de ruta técnicamente suficiente. R01 separa raw finish/J_parcial del valor legítimo. | Medida SUPLEMENTARIA; no igualdad con e ni q de R01. |
| σ legítima | Probabilidad de entrega de calidad suficiente sin ninguna infracción del proceso. | IGUALDAD de evento con la parte de calidad/legitimidad/plazo de e; el presupuesto requiere la siguiente fila. |
| Éxito e | R01/M10 exige también C_traza≤R y plazo. | IGUALDAD con σ_R del manuscrito, no con σ sin presupuesto. En políticas con C_max≤R ambas coinciden. |
| Coste | R01 C es ledger por ejecución; manuscrito C(π) es su máximo sobre ejecuciones. | COTA/AGREGACIÓN explícita, no igualdad de objetos. No se reemplaza por coste esperado. |
| Capacidad y coste deseado | R01 R es cap físico; manuscrito B es cap físico y R es objetivo económico. | DISTINCIÓN necesaria. Con B=R, el par costoso no es ejecutable en ese mismo perfil. |
| Políticas | M10 define todas las reglas observables con gate y rechazo conocido, y mezclas independientes; M02 limita a 32 eventos. | Cobertura local por historia completa; no solo las políticas implementadas en run(). |
| Revisión propia | Cada posición necesita review→decide→execute. Las capas no repiten, y un certificado local no sustituye otro. | IGUALDAD local; fija coste mínimo de completar, no revisiones globales repetidas. |
| Plazo/cap | T=32, H=32; los controles usan 10/11 unidades de tiempo y 11/12 peticiones incluyendo stop. | COTA realizable local; no ley general sobre latencia. |
| N, geometría y señales | M02 usa N=1 y prior técnico pagado. R01 permite otras redes y tareas. | SUPUESTO PENDIENTE para una extensión distribuida o de búsqueda. |
| Certificados, pooling, recuperación | En M02 solo el catálogo declarado; R01 admite otros perfiles con cargos e información propios. | SUPUESTO PENDIENTE para ampliar el resultado. No se excluyen de R01 para conservar la dificultad. |

Fuentes exactas: escenario §§1.2,1.4,2.1–2.3,2.6–2.8,2.11–2.15; contrato M10 §§2–4; catálogo M02 `operations`, `gate_rule`, `resource_rule`, `reuse_rule`; código `Episode.request` y `Episode.result`. El código se leyó, no se ejecutó para esta revisión.

## 4. Teorema directo para el contrato M02, con todas sus políticas

### 4.1 Capacidad física y umbrales

Usar el catálogo M02 estático sin información inicial de χ, con capacidad física B=12, T=H=32 y ε=0. Esto es el perfil físico easy_budget, sin cambiar sus bytes. Introducir un objetivo de coste R_goal con 11≤R_goal<12. C es máximo del ledger; la capacidad física de la fuente sigue llamándose R_alloc=B. Son variables diferentes.

El prior congelado es P(χ=0)=P(χ=1)=1/2. Una variante con prior a/(1−a) es otro θ y debe declararse; no se altera retrospectivamente el fixture.

Π contiene todas las políticas sobre la historia observable del catálogo, respetando gate y prohibiciones conocidas, hasta H. H_tec significa entrega completa de valor técnico 6; V registra cualquier infracción, y σ=P(H_tec∩¬V). Para políticas con C_max≤R_goal, σ coincide con el indicador de éxito de calidad/plazo/coste correspondiente al objetivo R_goal.

### 4.2 Cota y prueba exhaustiva por clases de eventos

Toda ruta completa exige setup, de coste 2, y un review, decide y execute por cada una de las tres posiciones, a coste 1 cada uno. Ninguna operación distinta produce el certificado local ni el commitment necesarios. Después de execute se consume el certificado y se cambia de capa; reuse no produce uno nuevo. Por tanto todo camino completo paga al menos 2+3·3=11.

Un query_state/check_certificate previo a completar añade al menos 1. Bajo C_max≤R_goal<12, una rama completa no puede haber pagado esa consulta. Setup y explore muestran el mismo mapa en ambos mundos; query_mandate la misma regla; review/decide la misma geometría y los mismos gates sin χ; reuse conserva solo lo ya visto; wait/stop y los rechazos sintácticos o de recursos no distinguen los mundos. Un execute de M devuelve binding verdadero en ambos y no revela χ. Estas clases agotan el catálogo.

Una entrega de calidad 6 requiere una primera ejecución alta todavía desconocida. Antes de ella, la política usa una historia con la misma ley en los dos mundos. Sea u la probabilidad de entrar en esa primera apuesta desconocida. En el prior equilibrado, su probabilidad de acierto es 1/2. La primera infracción ocurre con probabilidad u/2 y cualquier éxito legítimo exige ese acierto. Así

$$
\sigma\le u/2\le1/2,\qquad
\rho\ge u/2\ge\sigma,\qquad
\rho\ge\eta/2.
$$

La última desigualdad usa η≤σ+ρ. Consultas en ramas fallidas, phases y paradas no aportan éxitos financiables y no invalidan la cota. En WC las garantías por mundo implican las garantías bajo el prior equilibrado.

### 4.3 Controles y frontera local exacta

Con probabilidad β, ejecutar X en la primera posición, observando el recibo después del efecto. Si resulta admisible, χ=0; si resulta inadmisible, χ=1. En las dos posiciones siguientes ejecutar respectivamente X o Y según ese hecho ya adquirido. Mantener review→decide→execute en cada posición. La primera infracción no se borra, pero se completa técnicamente sin infringir una prohibición conocida. Con probabilidad 1−β ejecutar M tres veces.

En AVG: C_max=11, η=β, σ=β/2, ρ=β/2. Para WC, usar moneda justa en la primera opción X/Y y luego la correcta según el recibo; esas tasas se cumplen en cada mundo. Estos controles son construcciones simbólicas legales; no se afirma que el wrapper histórico run() los implemente ni que se hayan ejecutado ahora.

Por tanto para 11≤R_goal<12:

$$
\exists\pi:C_{max}\le R_{goal},\eta\ge h,\rho\le r
\iff r\ge h/2;
$$

$$
\exists\pi:C_{max}\le R_{goal},\sigma\ge p,\rho\le\delta
\iff p\le1/2\quad\text{y}\quad\delta\ge p.
$$

Para R_goal=12, pagar la consulta de χ antes del primer efecto y mantener todos los gates consigue η=σ=1, ρ=0 y C_max=12. Para R_goal<11, no hay entrega suficiente bajo C_max≤R_goal. Estas condiciones son exactas dentro del catálogo, para AVG equilibrado y WC, no una extrapolación de 27 rutas o de los checks históricos.

### 4.4 No vaciedad del trilema legítimo local

Para cualquier 11≤R_goal<12, 0<p≤1/2 y 0≤δ<p:

| Par | Control dentro de la misma capacidad B=12 | Resultado |
|---|---|---|
| Coste–riesgo | Solo M | C=11≤R_goal; ρ=0; σ=0<p. |
| Coste–éxito legítimo | Control adaptativo con β=2p | C=11≤R_goal; σ=p; ρ=p>δ. |
| Riesgo–éxito legítimo | Una consulta y ruta admisible | C=12>R_goal, ejecutable bajo B; σ=1; ρ=0. |

Ninguna otra política consigue los tres por la cota universal. Esta es una región parametrizada no vacía, no una sola ejecución. Con R_goal=12 las tres son compatibles. No se ha cambiado la misión ni se han ocultado controles competentes.

**Límite del perfil histórico:** sus umbrales originales p=3/4, δ=1/4, con R_alloc=11, no dan el trilema no vacuo por los tres pares. El par coste–éxito ya es imposible porque σ≤1/2; además el techo de riesgo δ=1−p es redundante con ese éxito. Esa limitación ya estaba registrada en M10. Los umbrales anteriores de esta sección son un contrato analítico adicional declarado, no una corrección del fixture.

Si se mantiene B=R_goal=11 como cap físico, el control costoso no puede ejecutarse allí: conserva su papel como solución del mismo problema con capacidad 12. No se etiqueta como una política permitida bajo cap 11. Esta distinción es esencial para la transferencia del lenguaje de los pares.

### 4.5 Indicador de éxito de R01 sin coste máximo global

Para cualquier política ejecutable bajo B, σ_goal=P(H_tec∩¬V∩{C_traza≤R_goal}) cuenta las entregas legítimas dentro del objetivo económico. Las ramas que cuentan en σ_goal no pueden pagar la consulta, aunque otras ramas gasten 12. El mismo primer-apuesta argumento da σ_goal≤1/2 y ρ≥σ_goal. Así la cota también puede expresarse como una condición de éxito por campaña al estilo de e de R01. No se identifica σ_goal con σ en políticas que gastan más que R_goal en alguna rama.

## 5. Contraejemplo a la extensión indiscriminada de la frontera F

En el M02 documentado, L=3, C0=11, c=1 y una sola lectura revela el binding compartido. A presupuesto 12, consultar χ y escoger X/X/X o Y/Y/Y da calidad legítima 6 y riesgo cero. Los gates siguen presentes.

Si se aplicara incorrectamente F con d=3 y k=1, se obtendría q=2^{-2}=1/4 y, para η=1, una cota de riesgo 3/4. Es incompatible con el control anterior de riesgo cero. La causa precisa es que los tres bindings **no son independientes**: son copias del mismo χ. No refuta F; refuta aplicar su fórmula a ese perfil R01.

R01 §§1.3,2.11 permite precisamente reutilizar un hecho válido en ámbitos aplicables. No se puede reparar la extensión prohibiendo esa reutilización. Hay que modelar las dependencias o utilizar una cota apropiada para un solo hecho, como §4.

## 6. Qué falta para una familia R01 con dureza creciente

### 6.1 Una familia R01 parametrizada que ya puede definirse y probarse

La existencia de un trilema dentro de una subfamilia no requiere que el coste informativo crezca con L. Se puede construir la familia G de bindings compartidos, distinta de F, para todo L≥1:

- Una tarea, N=1, mundo estático χ∈{0,1} equiprobable, misión y principal fijos. Tres nodos por capa: M_i de beneficio 1 y X_i/Y_i de beneficio 2, i=1,…,L. Conectores completos entre capas consecutivas y beneficio cero; incluido el conector terminal. La admisibilidad es la conjunción de active(m)=1, active(x)=1−χ, active(y)=χ en todos los efectos.
- Geometría fija: M en la referencia, X/Y a distancia 1 a izquierda/derecha; radio accesible 1, dispersión cero. Los I/P derivados tienen media 2, caso de control admitido en R01 §2.3; la recompensa y la posición no revelan χ. M es conocido y su evidencia se paga.
- El perfil comienza con un prior técnico ya adquirido y pagado, favorable a todos los controles. Para evitar una lista técnica gratuita, se cobra preparación 2 y exploración de los 2L candidatos a c_e=2 por candidato: setup de coste 2+4L y duración 1+2L. Su ledger conserva ese desglose. No se descubre χ en esa preparación. Es contexto inicial de este perfil, no una estrategia obligatoria que se imponga a todo R01 ni una pretensión de optimalidad de la búsqueda.
- Para cada posición material se requiere review→decide→execute, cada operación a coste y duración 1. La revisión local vale c_v=1<c_e=2. No revela el binding global; sí comprueba el nodo, conector y ámbito propio. Las consultas normativas pueden ampliar la información sin sustituir ese gate. Mensajes a uno mismo no crean información. No hay otros participantes ni fuentes iniciales.
- La evidencia global del único χ cuesta 1 en total: adquisición/producción y comprobación de aplicabilidad se incluyen en ese precio declarado. Es suficiente para todas las posiciones mientras permanece válido. No se fuerza volver a comprarla L veces.

El contrato completo de operaciones es el siguiente. Las respuestas y los precios previos a conocer χ no dependen de su valor, salvo en las tres operaciones informativas declaradas.

| Operación | Coste / duración | Transición e información |
|---|---|---|
| setup | 2+4L / 1+2L | Una vez inicializa el prior técnico, evidencia de M y versión; repetir no obtiene χ ni reinicia el proceso. |
| explore | 2 / 1 | Inspección de candidato ya descubierto; geometría y beneficio existentes, sin χ. |
| review | 1 / 1 | Para nodo de la siguiente capa y conector válido: certificado local del ámbito exacto; borra pending. Los ámbitos de capas distintas no se sustituyen. |
| decide | 1 / 1 | Requiere ese certificado y rechaza prohibición ya conocida; crea commitment del mismo ámbito. |
| execute | 1 / 1 | Requiere certificado/commitment, posición y conector, y rechazo conocido. Produce efecto, avanza capa, consume ambos y entrega binding_active_after_effect. Si X/Y, revela χ; si M, no. V es OR de toda infracción. |
| query_state / inspect_binding / check_certificate | 1 / 1 | Devuelve χ exacto, origen, ámbito y versión. El precio incluye todo el productor y uso; no sustituye revisión geométrica. |
| query_mandate | 1 / 1 | Regla y principal fijos, sin el dato de actividad de χ. |
| reuse / comunicación consigo mismo | 0 / 0 | Solo hechos/certificados de la historia; no altera χ, V, posición ni certifica un ámbito nuevo. |
| wait | 0 / 1 | Mundo estático; no crea evidencia. |
| stop | 0 / 0 | Termina; no convierte ruta incompleta en entrega. |

El estado es (capa, prefijo, certificado, commitment, χ_adquirido_o_desconocido, ledger, reloj, contador, V, terminado). El χ del entorno no es accesible directamente por la política. IDs y payloads pertenecen al catálogo finito; no hay operación de reset o fuente externa. Una petición que supera capacidad/reloj/cap se rechaza sin efecto ni dato oculto y consume petición. Un error sintáctico/de gate tampoco revela χ; salvo rechazo previo de recursos, paga su cargo indicado. Esos estados, transiciones y respuestas definen la clase de todas las políticas por historia, no una lista de algoritmos.

**Estado inicial del punto de decisión:** antes de la primera elección de π, el setup automático ya se ha realizado. Prefijo vacío, primera capa, certificado y commitment vacíos, χ desconocido, V=0, coste incurrido 2+4L, reloj 1+2L y contador 1 de la macro petición. El desglose de producción es parte de ese coste, no un cargo duplicado. Ninguna política desde este contexto puede evitar retroactivamente ese gasto o recibir el prior sin él. La optimización de un proceso anterior que adquiriese otro prior es otra configuración y no se declara cubierta por este teorema. Repetir setup produce el mismo manifest pagando de nuevo su cargo, sin reiniciar el contador, el coste o V.

Fijar ε=0, C0(L)=2+7L, capacidad física B=C0(L)+1, T=H=5L+4 y objetivo de coste C0(L)≤R_goal<C0(L)+1. El horizonte cubre incluso el desglose de la preparación más L gates, una lectura y stop. No se conserva el H=32 de M02 al aumentar L.

**Teorema G.** Para cualquier L y estos parámetros, para todas las políticas observables ejecutables de G, con C_max≤R_goal se cumplen σ≤1/2, ρ≥σ y ρ≥η/2. Las fronteras de §4 son exactas, sustituyendo 11 por C0(L) y 12 por C0(L)+1. Para 0<p≤1/2 y 0≤δ<p cada par es alcanzable y ninguna política consigue las tres. En R_goal=B una lectura obtiene σ=η=1 y ρ=0.

**Prueba.** Todo camino completo paga el setup técnico ya incurrido y 3L gates/materiales, al menos C0(L). Un nuevo hecho global añade 1, de modo que no cabe en una rama de entrega dentro de R_goal<C0(L)+1. Todas las demás respuestas preefecto desconocido son las mismas en ambos mundos por el catálogo. Una entrega de calidad 2L requiere la primera ejecución alta, con acierto 1/2; σ≤u/2 y ρ≥u/2 como en §4. El control intenta con probabilidad β, apuesta en el primer paso y adapta los restantes al recibo, sin borrar V ni ejecutar una opción conocida como prohibida. C_max=C0(L), η=β, σ=ρ=β/2. Solo M prueba coste–riesgo; β=2p coste–éxito; una lectura previa prueba riesgo–éxito a C0(L)+1. Los controles respetan el horizonte y la capacidad. ∎

Esta es una instanciación formal del inventario R01: tarea y población (§2.1/2.5), cadenas/conectores (§2.2), medias coincidentes y dispersión declarada (§2.3), geometría y radio (§2.4), separación de información y cargo de productor (§2.6), gate y recibos (§2.7/2.8), ledger c_v<c_e y reutilización (§2.11), capacidad/horizonte y unidad de agregación (§2.12). El prior técnico pagado es favorable y se declara como en M02, no una campaña de descubrimiento completa. El perfil usa un catálogo cerrado dentro del inventario; otra API o evidencia inicial define otro perfil. La independencia por segmento de F no se impone a este problema.

Así se dispone de una familia de configuraciones R01 formalmente especificada, con todas sus políticas observables y tamaños arbitrarios, que presenta el trilema **condicionado**. La revisión independiente de la prueba y del cumplimiento de esas cláusulas sigue pendiente. No se afirma que todo R01 tenga este perfil, que el sobrecoste informativo crezca con L o que ocurra con determinada frecuencia.

**Variante AVG de alta fiabilidad.** Cambiar solo el prior del único χ a P(χ=0)=a≥1/2 mantiene la construcción de G y cambia la cota local a σ≤a y ρ≥(a^{-1}−1)σ. El control adaptativo da η=β, σ=βa y ρ=β(1−a). Con a=99/100, p=19/20 y δ=1/1000, cualquier L tiene cada par alcanzable y triple imposible a R_goal<C0(L)+1; el riesgo mínimo barato para σ≥p es 19/1980. Es otro perfil declarado, no el prior congelado de M02 ni una garantía WC del 95 %.

### 6.2 Dureza informativa creciente: obligación diferente

La prueba local anterior no demuestra coste creciente en L ni severidad extraordinaria. Para una familia con L hechos independientes se necesita una instanciación de R01 que especifique, además del grafo:

1. Un conjunto de recursos/bindings distintos por segmento, distribución y evidencia inicial; geometría y recompensas que no filtren sus valores.
2. El catálogo completo de consultas, mandato, estado, certificados y mensajes; coste total de producción y de hechos nuevos, incluida toda consulta combinada.
3. Gate y contador de trabajo material irreductible C0; certificados reutilizables y revisión propia sin doble cobro.
4. Historial y efectos para cada operación; toda forma legítima de deducir un binding debe quedar en la simulación, no solo las consultas elegidas por el autor.
5. Transformación de **todas** las políticas del perfil a la envolvente de F, con preservación de umbrales; controles ejecutables que demuestren la otra dirección en la frontera.
6. Los eventos correctos de calidad legítima, costo por rama/coste máximo, plazo, recuperación y capacidad física, conservando las métricas originales.

La sintaxis de R01 permite perfiles como el de hechos distintos, pero ese contrato completo y su prueba de cobertura todavía no están cerrados. La familia G demuestra existencia con un binding compartido y sobrecoste constante; no se usa para declarar la dureza creciente de F ni para transportar sin prueba la cota cuadrática de W.

## 7. Dictamen de transferencia

| Afirmación | Dictamen propio |
|---|---|
| Proposición general de transferencia por preservación de objetivos | Demostrada por contradicción, con la dirección correcta; su hipótesis no se da por verificada. |
| Frontera universal de políticas para el contrato observable M02 | Derivación directa en §4, con catálogo, coste y controles explícitos; revisión independiente pendiente. |
| Trilema local no vacuo por tres pares | Demostrado en el contrato analítico declarado B=12 y R_goal<12, con umbrales p≤1/2, δ<p. |
| Existencia en una familia R01 parametrizada | Familia G definida y probada en §6.1, con prior técnico pagado, catálogo cerrado y tamaños arbitrarios; revisión externa pendiente. |
| Original M02, p=3/4, δ=1/4, cap 11 | Imposibilidad de adecuación; no prueba del trilema no vacuo por todos los pares. |
| Misma fórmula F para todos los perfiles R01 | Refutada como extensión indiscriminada por el binding compartido. |
| Familia de dureza informativa creciente integrada en R01 | Construcción y cobertura pendientes; no se confunde con la existencia ya probada en G. |
| Teorema de todo R01 y su Pareto de seis medidas | No establecido; no se sustituye por una matriz de semejanzas. |

El [plan](./WORKPLAN.md) registra M17 en desarrollo por estas entregas y conserva M16 abierto. No se han ejecutado nuevos tests científicos. Los JSON, fixtures, checkers y resultados previos no se modifican.
