# Puente matemático ampliado: Universo Dado → A/B/C/D → reducción agéntica

**Anexo de investigación a PR #57 · 26-10-2026 · Stage A · hipótesis, proposiciones y contraejemplos bajo supuestos explícitos.** No modifica 00M/00N ni convierte pruebas sintéticas en validación empírica. Preserva íntegros AG-R1 (contratos parciales), AG-R2 (frustración operacional de misión) y AG-R3 (metacoordinación/reconfiguración dentro de las capacidades declaradas). Los artículos del linaje se citan según la afirmación concreta reutilizada; una auditoría posterior **no** acredita automáticamente todas las proposiciones originales de un artículo.

## 1. Resultado central que buscamos y sus tres niveles

Hay que separar tres afirmaciones distintas:

1. **Construcción**: el modelo ejecutable AG01–AG30 introduce A, B, C y D en los fixtures. Reproduce un caso compatible con 00M **por diseño**; esto comprueba consistencia y alcance de decisiones, no la frecuencia natural de la estructura.
2. **Emergencia condicionada de un límite A**: si un contrato comprime más distinciones relevantes de las que puede representar, la insuficiencia de A respecto a una familia de decisiones sigue matemáticamente, aunque **nadie haya definido B/C/D en la construcción del sistema**. Este es el puente útil de *The Given Universe*, §4.
3. **Disponibilidad y valor de B/C/D**: la colisión de A por sí sola **no prueba** que haya B accesible, una exploración C, un residual D material o que el metaprotocolo produzca un beneficio neto. Cada cual exige hipótesis, evidencias y costes adicionales. Las categorías son roles epistémicos relativos a productor, receptor, pregunta, derechos y momento (00M), no cuatro subconjuntos que deban estar todos poblados.

El punto diferencial defendible sería **valor de decisión neto bajo evidencia parcial cualificada y capacidad autorizada de transición**. No se ha demostrado una ventaja exclusiva de agentes de IA ni una superioridad sobre un coordinador convencional con los mismos contratos, certificados y costes.

## 2. Teorema de colisión de contratos: vínculo exacto con *The Given Universe*

Fijemos una ventana finita de decisión y un dominio de estados admisibles W (puede ser enorme). Sea E: W → R el evento de formalización/contrato efectivamente visible en A. Sea
r=(r_1,…,r_k):W→Y una **firma de k preguntas realmente relevantes** para una misión; no pretende codificar todas las preguntas del universo.

**Proposición P1 (suficiencia por fibras; resultado estándar).** Existe una respuesta perfecta V sobre el registro disponible, r=V∘E en el dominio admitido, **si y solo si**

\[
E(w)=E(w')\Longrightarrow r(w)=r(w')\quad\text{para todo }w,w'\text{ admitidos}.
\]

Prueba: si V existe, entradas idénticas obligan a salidas idénticas. En sentido inverso, sobre cada fibra no vacía de E, r tiene el mismo valor; esa asignación define V en la imagen de E. No exige que V sea computable ni que pueda probarse desde dentro que el evento E es fiel al mundo. Para exigencia **algorítmica** de V hacen falta supuestos efectivos adicionales.

**Proposición P2 (insuficiencia por capacidad finita; derivación específica de este anexo).** Supongamos K=|im(r)| firmas de decisión distintas y M=|im(E)| registros distintos posibles en la ventana. Si K>M, existen dos estados admisibles w,w' con E(w)=E(w') y r(w)≠r(w'). Por P1 no existe un decisor perfecto exclusivamente sobre A para la familia r.

**Prueba.** Si r fuese constante en cada fibra de E, entonces habría un mapa de los M registros hacia las K firmas que cubriera todas las firmas realizadas; requeriría K≤M. Contradicción.

**Corolario de contrato acotado:** si el estado observable total de A tiene a lo sumo b bits y el número de firmas de misión distingue K>2^b casos, hay una colisión relevante forzosa. El presupuesto b debe contar **todo** el historial, consultas y metadatos efectivamente observables dentro de la ventana, no solo el tamaño de un mensaje.

Esto convierte «ecosistema suficientemente complejo» en una proposición verificable: **complejidad de decisiones relevantes K superior a la capacidad informativa observable M**, no mero número de empresas, agentes, líneas de código o nodos.

**Contraejemplo obligatorio:** mil millones de estados internos pueden compartir la misma respuesta binaria «¿debo detener esta operación?»; si E emite precisamente ese bit correcto, K=M=2 y A es suficiente para esa pregunta. Tamaño enorme ≠ B/C/D forzosos. También un contrato de b bits puede distinguir todos los casos relevantes si K≤2^b y su partición está bien elegida. La condición K>M es suficiente para demostrar pérdida; K≤M **no** garantiza fidelidad.

**Origen y auditoría:** *The Given Universe*, §1 y especialmente §4 (*Factorization fact / Projection loss*) explica el evento W→R y el criterio de fibras; §6 separa la partición **efectivamente realizada** de un «omnidistinguidor» imposible por Cantor y de un decidor semántico universal condicionado por Rice. [Original en Drive](https://drive.google.com/file/d/1ePHBGgco-qiQ4S0BmsCNTTFdd2C1JgCd/view). [Auditoría independiente D21 del manuscrito](https://docs.google.com/document/d/1yI9GStxe3zEmXHKcIUtsYLY0_h8YXKdoi1z0TImyIo4/edit): no trasladar Cantor/Rice a cualquier API finita y no afirmar que toda pérdida sea irremediable con sensores o nuevas fuentes. El teorema de capacidad P2 es una **consecuencia nuestra de P1 y el principio de las casillas**, no un resultado presentado textualmente como P2 en el original. Comparador matemático anterior: [Blackwell, *Equivalent Comparisons of Experiments* (1953)](https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-24/issue-2/Equivalent-Comparisons-of-Experiments/10.1214/aoms/1177729032.full).

## 3. Composición real de contratos, refinamiento B y el metaoráculo parcial

En una cadena de transformaciones E_1, E_2, …, el posprocesamiento determinista **no puede separar** estados que E_1 ya fusionó:

\[
\ker(E_1)\subseteq\ker(E_2\circ E_1).
\]

Este orden de indistinguibilidad procede de P1; da un mecanismo de **límite emergente** cuando proveedores independientes publican interfaces más estrechas que el espacio de preguntas del receptor. No atribuye falsedad a todo contrato ni asegura pérdida relevante para cada misión.

Si otra fuente autorizada expone Q:W→Z, la información conjunta (E,Q) puede refinar la partición de E. Formalmente hay una ventaja de **decisión perfecta para r** cuando simultáneamente:

\[
\ker(E)\not\subseteq\ker(r), \qquad
\ker(E,Q)\subseteq\ker(r).
\tag{P3}
\]

P3 no garantiza que Q exista, sea veraz, accesible o barata; identifica qué certificado de **valor informacional estricto** se necesitaría. Si Q=f(E), no separa ninguna fibra: es una simple reformulación de A.

**Proposición P4 (valor débil de información, con supuestos).** Dadas las mismas acciones factibles, idéntica función de pérdida y una distribución de estados *explícita*, si una política con (E,Q) puede ignorar Q, su **riesgo óptimo bruto** no puede superar el riesgo óptimo con E:

\[
\min_{\pi(E,Q)}{\mathbb E}[L]\ \leq\ \min_{\pi(E)}{\mathbb E}[L].
\]

Prueba: las políticas basadas en E son un subconjunto de las políticas permitidas sobre (E,Q). **Sin distribución no existe esta magnitud probabilística**; las distancias/posibilidades C/D de 00M no quedan convertidas en probabilidades. Tampoco hay garantía de ganancia **neta**: el coste de Q, verificación, coordinación y transformación puede superar la reducción de pérdida.

**Ejemplo mínimo estricto:** dos mundos igualmente probables w₀,w₁; E(w₀)=E(w₁)=READY; acciones x₀,x₁ con pérdida 1 si se elige la acción incorrecta. Con A la pérdida mínima esperada es 1/2; con Q verdadero que revela cuál de los dos mundos se da, es 0 **antes de costes**. Un controlador convencional con el mismo Q logra exactamente el mismo resultado: prueba el mecanismo informacional, no exclusividad agéntica.

**No-oráculo, sino meta-protocolo parcial:** responde sobre **preguntas y fuentes elegibles** con certificados, límites y abstención; no devuelve el estado universal, no decide lo indecidible ni transforma automáticamente C/D en B. Puede ser un protocolo, verificador, tabla de decisiones o servicio convencional, no otro «agente mágico». La metamorfosis y cesión de recursos deben **estar ya autorizadas dentro de A**.

## 4. Algoritmos propios reutilizables del linaje: resultados auditados y límites

| Investigación y fuente trazable | Algoritmo/resultado concreto que sobrevive | Traslado exacto a AG/ACC, sin inflación de novedad |
|---|---|---|
| **R03 — Primalidad y Lógica**, [revisión y códigos](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R03_PRIMALIDAD_Y_LOGICA_v0.1.md) | Cobertura finita de pares de estados relevantes: seleccionar pruebas con coste mínimo de modo que las observaciones elegidas separen cada par que la decisión r debe distinguir (criterio de fibras). | **Motor de adquisición selectiva Q**: minimizar coste autorizado de certificados y consultas que distinguen pares de mundos previamente confundidos por A. Es problema de *weighted set cover* en universo finito; óptimo computable por enumeración finita, **no solución eficiente universal** en dominios ilimitados. |
| **R04 — Álgebra de Posicionamientos**, [revisión](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R04_ALGEBRA_DE_POSICIONAMIENTOS_v0.1.md) | Traducción parcial tipada de perspectiva, autoridad, propósito, fuente y fecha; composición puede resultar indefinida. | Evitar «Q verdadera en origen ⇒ Q válida para ejecutar en destino». Mantener trazabilidad de cambio de rol y consentimiento. |
| **R05 — Formalización del Meta Sistema**, [revisión](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R05_FORMALIZACION_META_SISTEMA_v0.1.md) | Evaluación acotada con estados ENTAILED/REFUTED/UNDERDETERMINED/INCONSISTENT_FRAME; admitir UNKNOWN exterior, no adjudicación absoluta. | Núcleo de **metaoráculo limitado** que discrimina suficiente evidencia, conflicto de marcos y abstención; preserva C/D en vez de rellenarlos. |
| **R07 — Practical Incompleteness**, [revisión](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R07_PRACTICAL_INCOMPLETENESS_v0.1.md) | En familias de programas suficientemente expresivas, cada caso concreto puede tener dominio decidible mientras **no existe un decidor uniforme calculable desde el código del programa** para la familia construida (reducción al problema de parada). | Límite de pretender un validador semántico universal para cualquier vendor; **no** aplica sin más a contratos o flujos finitos/decidibles. Separa límites de interoperabilidad de una incapacidad intrínseca de toda API. |
| **R10 — Projected Infinite Paradox**, [revisión y variantes originales](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R10_PROJECTED_INFINITE_PARADOX_v0.1.md) | Los algoritmos de poblaciones cambiantes muestran que convergencia por **participante fijo** no obliga a convergencia **uniforme o de proporción poblacional** (ver §5). | Falsador macro: todos los agentes estables pueden mejorar localmente mientras siguen entrando nuevos agentes/fuentes y persiste el límite ecosistémico. No implica que toda misión fracase ni que el malestar aumente. |
| **R11 y R13 — Primitiva Entrópica / Mathematical Repair Dialogues**, [R11](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R11_PRIMITIVA_ENTROPICA_v0.1.md), [R13](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R13_MATHEMATICAL_REPAIR_DIALOGUES_v0.1.md) | Búsqueda entrelazada / *dovetailing*: una traza positiva finita es testigo válido; ausencia en presupuesto k **no certifica** ausencia en todos los recursos. R13 da contraejemplo exacto a umbrales «no visto ⇒ permanentemente imposible». | Planificador de exploración acotada del meta-protocolo; prueba positiva local o «aún no determinado», nunca C/D resueltos por agotamiento arbitrario. |
| **R12 — Primitiva Entrópica, TeX compilado**, [única revisión específica autorizada](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R12_PRIMITIVA_ENTROPICA_COMPILED_TEX_v0.1.md) | Teorema de reutilización cualificada de verificaciones: ahorro neto = suma de costes evitados menos revalidaciones y coordinación (ver §6). | **Coste real del meta-protocolo**: reutilizar evidencia/proofs y reasignar verificaciones; fuente, receptor, efecto, privacidad, versión y tiempo obligatorios. |
| **R18 y R02 — Conservación de Consistencia / Tríada Fundamental**, [R18](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R18_CONSERVATION_OF_CONSISTENCY_v0.1.md), [R02](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R02_TRIADA_FUNDAMENTAL_v0.1.md) | Átomos mínimos de particiones conjuntas que conservan distinciones de fuentes y lógica bilaterada (apoyos positivos/negativos) que no explota ante conflicto. | **No fusionar dos testimonios contradictorios en una verdad única**, preservar origen y no confundir los cuatro valores de Belnap con A/B/C/D de 00M. |
| **R20 — Magic Sphere**, [revisión y prueba de 1.099 casos finitos](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R20_MAGIC_SPHERE_FINITE_CLOSURE_COMPACTNESS_SELF_CERTIFICATION_v0.1.md) | Sin límite externo autenticado ni marcador END completo, ningún prefijo finito de k registros prueba que no haya k+1. El certificado de clausura **sí** es posible en alcance finito con cota/verificación terminal competente. | El protocolo debe devolver OPEN/UNKNOWN al observar solo un prefijo. **No** declarar «inventario completo» o «no hay B adicional» sin cierre certificado. |
| **R09 — Projection Mechanism v4**, [revisión](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R09_PROJECTION_MECHANISM_V4_v0.1.md) | Cola de obligaciones no resueltas U_(t+1)=max(0,U_t+a_t−s_t), con arribos, capacidad de saneamiento y cualificación de fuentes explícitos. | Dinámica observable de **deuda de misión/integridad**, distinta del sufrimiento humano y distinta de categoría B; crecimiento requiere arribos persistentemente mayores que resoluciones. |
| **R14 y R16 — Distorsión Entrópica / Exergía Computacional**, [R14](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R14_DISTORSION_ENTROPICA_v0.1.md), [R16](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R16_COMPUTATIONAL_EXERGY_v0.1.md) | Cobertura finita certificada permite cotas logarítmicas; compresión cuantifica representaciones, no suficiencia de decisión. | No usar un «número de bits comprimidos» como medida automática de distancia al óptimo, C/D, entropía física, frustración ni calidad del metaoráculo. |

**Proveniencia y reproducibilidad:** los algoritmos asociados incluyen fuentes ejecutables y JSON en el [directorio de review-tests](https://github.com/dakleyer/structural-awareness-workbench/tree/main/02-workstreams/ecosystem-awareness/07-field-notes/review-tests). No son pruebas formales generales ni ensayos con agentes de proveedores; cada revisión establece sus resultados numéricos finitos y sus límites.

## 5. Contraste dinámico no tautológico: el algoritmo R10

Sea p_i^(k) la posición/estado del participante i en la etapa poblacional k, con participantes i≤k. En una edición del algoritmo R10, para i fijo:
\[
p_i^{(k)}=(1-2^{-i})\,2^{-(k-i)}\xrightarrow[k\to\infty]{}0,
\]
mientras que el máximo de la etapa se acerca a 1: los participantes antiguos se aproximan al valle, pero participantes nuevos siguen ocupando la cima. En otra edición explícita:
\[
p_i^{(k)}=\frac{i}{k}(1-2^{-k}),\quad i\le k.
\]
De nuevo cada i fijo converge a 0; sin embargo, la fracción poblacional con p_i^(k)>1/4 converge a **3/4**, no a cero.

La inferencia
\[
(\forall i\ {\lim}_{k\to\infty}p_i^{(k)}=0)
\;\not\Rightarrow\;
{\lim}_{k\to\infty}\max_{i\le k}p_i^{(k)}=0
\]
es **matemáticamente válida como contraejemplo de intercambio de cuantificadores**; R10 tiene además afirmaciones históricas más fuertes que el propio estudio refuta, por lo que no se trasladan. **Lectura agéntica**: resultados/pérdidas locales por agente y resultados de un ecosistema con entrada/salida/versiones no pueden identificarse sin imponer una condición de uniformidad o controlar la población. Esta parte NO fue fabricada dentro de AG01–AG30, y permite diseñar un ensayo generativo independiente.

Fuente de algoritmo y correcciones: [R10 dossier](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R10_PROJECTED_INFINITE_PARADOX_v0.1.md); [algoritmo de prueba por edición](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/review-tests/R10_EDITION_SPECIFIC_FIXED_VS_MOVING_POPULATION_2026-10-10.mjs).

## 6. Coste neto de reconfigurar: recuperación matemática de R12

Para verificaciones independientes j=1,…,m, con coste c_j de repetir la prueba, r_j∈{0,1} de elegibilidad de reutilización, v_j de revalidación y h de coordinación, el teorema contable **bajo aditividad, permisos y versiones válidas** es:
\[
C_{\rm separado}=C_A+\sum_j c_j,\qquad
C_{\rm coordinado}=C_A+\sum_j[(1-r_j)c_j+r_jv_j]+h,
\]
\[
\operatorname{Ahorro}=\sum_{j:r_j=1}(c_j-v_j)-h.
\tag{P5}
\]

Es una identidad de costes **abstractos**, no ley física. Puede ser negativa aunque B añada información correcta; c_j distintos invalidan usar como proxy «porcentaje de certificados» en vez de suma de costes. R12 demuestra un ejemplo original 7+5(1−0,4)=10 solo para tareas homogéneas y sin sobrecostes; la revisión exhibe 7+9+1=17 separado y 7+2+1+1=11 con certificado costoso revalidado, ahorro de seis unidades, siempre sujeto a derechos de fuente/receptor.

Para el modelo agéntico, P5 debe **sumarse** a los costes de traspaso de recursos y pérdida de oportunidad del donante; no sustituirlos ni duplicar el mismo overhead. La condición para preferir meta-coordinación es explícita:

\[
\underbrace{\Delta L_{\rm decisión}}_{\text{reducción esperada de pérdida}}
+\underbrace{\operatorname{Ahorro}_{\rm pruebas}}_{\text{P5}}
>
\underbrace{C_{\rm transformación}+C_{\rm transición\ de\ rol}}_{\text{recurso y oportunidad}},
\]

con todos los términos en **las mismas unidades de valor**, política de actuación permitida y base probabilística solo si se justifica. Es posible que A-only sea óptimo o que una inspección convencional sea más barata. No hay garantía de que reprogramar un agente cueste menos que reconfigurar microservicios ni de que el tiempo humano tenga la misma función de coste.

Origen: [R12 TeX — §2–3](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/REVIEW_R12_PRIMITIVA_ENTROPICA_COMPILED_TEX_v0.1.md); [tests R12](https://github.com/dakleyer/structural-awareness-workbench/blob/main/02-workstreams/ecosystem-awareness/07-field-notes/review-tests/R12_QUALIFIED_REUSE_COMPOSITION_AND_ENTROPY_SCOPE_2026-10-11.mjs).

## 7. Esqueleto de algoritmo de segundo orden que sí puede ejecutarse sin omnisciencia

No descubre la distribución verdadera del mundo por introspección ni llena C/D. Opera con certificaciones y fines definidos; su elemento matemático es P1–P5 junto con pruebas de clausura acotada, no la etiqueta «oráculo».

~~~text
Entrada: pregunta de misión r; contrato A=E(w);
         fuentes candidatas Q_j con origen, permiso, versión, ventana;
         acciones que A ya permite; costes/capacidad; plazo.

1. Fijar pregunta r, alcance, objetivo, propietario y fecha.
2. Enumerar/distanciar SOLO pares de estados distinguibles por
   el referee/supuesto de investigación, NO inventar estados D.
3. Verificar para cada Q_j contenido, fuente, derecho de uso,
   independencia, pertinencia para r y plazo; clasificar inválida,
   desconocida o elegible. Si no hay trazabilidad, abstenerse.
4. Para un universo finito justificado, elegir consultas con coste
   mínimo que cubran pares de decisión aún indistinguibles
   (R03 set cover). Sin universo certificado, no declarar clausura.
5. Componer evidencias sin ocultar contradicciones (R02/R18);
   tipar traducción receptor/autoridad (R04);
   devolver certificado, subdeterminación, conflicto o UNKNOWN (R05).
6. Calcular acción factible y valor marginal neto con el mismo
   presupuesto y coste de prueba/reconfiguración (R12 + AG-R3).
7. Elegir actuar, buscar un testigo, esperar, escalar o abstenerse.
   Registrar fronteras C/D residuales y obligación U_t;
   revalidar si cambia contrato, población o versión (R10/R09).
Salida: decisión acotada + fuente + prueba + coste + autoridad
        + frontera residual + condición de revocación.
~~~

Este algoritmo puede implementarse como **protocolos convencionales, monitores, validadores tipados o agentes**. Cuánto gana depende de lo que ya resuelve el comparador fuerte. El término *segundo orden* indica que decide **qué información, revisión o coordinación ejecutar** sobre los procesos de primer orden; no le otorga una nueva fuente omnisciente.

## 8. Experimentos y falsadores para pasar de un A/B/C/D construido a estructura observada

| Experimento propuesto | Hipótesis independiente | Resultado que la invalidaría |
|---|---|---|
| **E1: contratos generados sin etiquetas A/B/C/D** | Generar mundos/cuestiones r antes de diseñar API; imponer b bits y comprobar K>2^b. La colisión debe aparecer por P2; etiquetar reservas B/C/D solo después con reglas 00M y evidencias. | Una implementación E realmente tiene M≥K o r factoriza por A; el tamaño del ecosistema no causó pérdida de decisión. |
| **E2: más capacidad de interfaz** | Repetir exactamente las mismas preguntas elevando b y ofreciendo la fuente completa donde sea viable. | Si A completa y legítima funciona con menor coste total, desaparece cualquier ventaja específica de B/EA. |
| **E3: Q fuerte vs Q falsa/caducada/revocada** | Medir P3 y P4, autenticidad, exactitud, coste, derechos y latencia, incluyendo peer convencional con exactamente la misma Q. | Peer fuerte empata/supera; Q redundante, falsa o no disponible; ganancia bruta pero valor neto negativo. |
| **E4: población cambiante (R10)** | Contrastar política que monitorea cada i fijo con política que rastrea masa, máximos, grupos nuevos y versiones. | No hay discordancia local/global bajo la dinámica real o el controlador estándar detecta igual de bien los cambios. |
| **E5: certificados y cierre (R11/R20)** | Intentar declarar «ya no existe otra fuente o mejor opción» con prefijos no certificados; introducir final auténtico y límites confiables. | La solución declara exhaustividad sin testigo, o el comparador convencional de clausura certificada iguala resultados. |
| **E6: coste y deuda (R12/R09)** | Medir ahorro permitido de pruebas, reconfiguración, tasa de llegada de obligaciones y capacidad de resolución sin convertirlos en dolor humano. | La sobrecarga supera beneficios o backlog cae; la supuesta aceleración no sigue de los datos. |

**Estándar probatorio siguiente**: revisión independiente de las demostraciones P1–P5, auditoría del código Rxx y de sus versiones históricas, pre-registro de E1–E6 con generación independiente del selector, adversarios y comparador maduro, semillas/referencias congeladas y luego agentes/vendors reales solo tras autorización. Un fixture sintético que inserta Q acertada y la usa para acertar **no es** verificación independiente de que esa Q exista en un ecosistema.

## 9. Diferencia entre isomorfismo y resultados nuevos — veredicto acotado

- **Isomórfico / matemática previa:** E y fibras, suficiencia decisional, refinamiento por Q, valor débil de información, cobertura de pruebas, certificados y políticas con acciones permitidas; todo ello está en matemáticas clásicas y mecanismos convencionalmente programables. No se presenta como nueva ley ni como distinción exclusiva de LLM.
- **Nueva instancia modelada e hipótesis plausible:** varios vendors con contratos parciales, movilidad/metamorfosis declarada, misión operativa y costes de coordinación diferentes. Con suficientes firmas de decisión respecto a capacidad E, A pierde necesariamente distinciones por P2; hace falta probar **empíricamente** cuántas veces se cumple esa premisa.
- **Resultado agéntico todavía abierto:** que una política metacoordinada A+Q obtenga sistemáticamente una mejora **neta y replicable** frente al mejor sistema convencional igualmente informado, con costes de cambio reales más bajos y derechos/autoridad conservados.
- **Límite crucial:** el modelo AG reproduce la clasificación 00M por construcción; E1 y R10 ayudan a someter a prueba una pérdida de información **independiente de la parametrización A/B/C/D**, mientras R12 y E3 prueban el valor añadido sin esconder los costes ni crear poderes nuevos.

**Estado final:** puente formal preliminar, con pruebas elementales condicionadas P1–P5, contraejemplos y algoritmos históricos auditados, **pendiente de revisión matemática externa**, replicación independiente y validación con datos reales. No se solicita por este anexo promoción automática a canon ni reetiquetado de los experimentos AG01–AG30 como empíricos.
