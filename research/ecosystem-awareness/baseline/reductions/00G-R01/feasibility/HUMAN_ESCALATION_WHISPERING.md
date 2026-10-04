# R01 — Escalación humana y whispering, mecanismo por mecanismo

Versión matemática 0.1 · Recorridos virtuales 0.3 · Primera tecnología del protocolo de extensión · 4 de octubre de 2026 · Sin integración ejecutada.
[Tecnologías del protocolo](./TECHNOLOGY_EXTENSION_PROTOCOL.md#technologies-to-study) · [Teorema base único](./R01_CONDITIONED_TRILEMMA_THEOREM.md).

Whispering significa aquí avisar al resto del grupo cuando un agente identifica un problema. Cualquier agente puede iniciar la escalación directa. El humano examina la evidencia y puede ordenar una pausa o una alternativa legítima. Es el mecanismo solicitado por el usuario; no se atribuye una cita específica a Nell ni se afirma que un producto concreto lo implemente.


<a id="why-it-can-help"></a>
## 0. Por qué esta tecnología puede ayudar antes de recorrerla

Escalación humana y whispering puede recuperar escenarios por cuatro razones distintas. Un solo agente puede aportar un testigo suficiente que la decisión colectiva todavía no tiene; su aviso puede llegar directamente al humano aunque el grupo favorezca otra acción; una pausa efectiva puede reservar tiempo para resolver la incertidumbre; y la respuesta humana puede proporcionar evidencia legítima adicional que permita completar una alternativa de calidad suficiente. La difusión evita que los demás ejecuten sobre una decisión ya invalidada. Hay que comprobar cada capacidad: avisar no equivale a detener, repetir no añade independencia y ser humano no equivale a conocer la respuesta.

| Vía de ayuda | Condición que puede mover | Condición necesaria |
|---|---|---|
| Evidencia nueva o certificado suficiente | Reduce la masa de historias ambiguas y la frontera mínima de riesgo para una eficacia dada. | Fuente legítima, alcance suficiente y coste completo de producción/uso. |
| Aviso directo y difusión | Reduce veto de mayoría, duplicación o demora en compartir un hecho. | Receptores, causalidad y acuses; no contar copias como fuentes nuevas. |
| Pausa previa de efectos | Da tiempo para revisar antes de una infracción irreversible. | Gates bajo control antes del efecto; resolución y entrega todavía dentro de T. |
| Decisión humana aplicable | Permite escoger y coordinar una ruta legítima suficiente. | Evidencia vigente, mandato original, alternativa realizable y nuevo commitment. |

Una fuente suficiente asequible puede ayudar mucho; la misma evidencia procesada por otra persona conserva el corte informativo H0. Una pausa que nunca termina puede mejorar seguridad y perder eficacia. Una revisión obligatoria puede aumentar coste o demora y perder escenarios antes aceptables. Estos son mecanismos candidatos de mejora, no una conclusión anticipada de que todos los escenarios se resolverán.

### 0.1 La cadena completa: detectar, escalar, detener y recomenzar

La mejora no depende solo de que un agente detecte algo. Tiene que entender que debe escalar, encontrar el canal, llegar al humano y explicarle el problema suficientemente. El humano tiene que poder resolverlo y actuar sobre los efectos afectados. La pausa o el kill switch deben ser admisibles para esa misión. Después tiene que existir una forma diferente y legítima de continuar, dentro del coste y del plazo. Fallar cualquiera de esos pasos puede dejar el escenario fuera de la zona aceptada.

| Paso necesario | Qué puede fallar | Qué se contabiliza o verifica |
|---|---|---|
| Detectar y reconocer la necesidad de escalado | Punto ciego compartido, testigo insuficiente o falta de criterio para escalar. | Inspección, evidencia suficiente y cobertura; más agentes no garantizan independencia. |
| Encontrar e invocar el proceso | Canal desconocido, no disponible, bloqueado por consenso o sin permisos. | Descubrimiento, integración, acceso y mantenimiento del canal. |
| Llegar al humano y explicar suficientemente | Pérdida del mensaje, cola, expediente incompleto o mal entendido. | Transporte, preparación del expediente, interacción y demora. |
| Resolver con capacidad humana suficiente | Misma información insuficiente, error o falta de autoridad sobre los gates. | Fuente nueva si existe, trabajo humano, competencia y alcance de intervención. |
| Detener de forma admisible | El efecto ya ocurrió; el gate no cubre todo; apagar produce otra infracción. | Estado real, interrupciones seguras, transición o relevo y obligaciones de continuidad. |
| Recomenzar con una base corregida | Se repiten los mismos inputs o se pierde la alerta; la alternativa no está validada. | Evidencia nueva pertinente, vigencia, cambio justificado de estrategia y nuevo commitment. |
| Completar la misión | El reinicio correcto llega tarde o consume demasiado. | Coste acumulado, trabajo rehecho, plazo y calidad legítima final. |

El coste completo puede ser alto, pero no se afirma que necesariamente lo sea en todos los escenarios. Se descompone h en detección, descubrimiento del canal, expediente/transporte, revisión humana y producción de evidencia, pausa segura, corrección y reentrada. El trabajo repetido y los costes de preparación/mantenimiento pertinentes también se pagan. Si la pausa y la corrección no están ya dentro de h, se añaden; no se cuentan dos veces. Para una entrega de coste C_0+h+c_rehecho es necesario que C_0+h+c_rehecho≤b; además, la cadena causal y la cola deben dejar la entrega dentro de T. Un q alto no compensa incumplir esos límites.

**La fiabilidad es de la cadena, no del detector aislado.** Sean E_1,…,E_6 los sucesos de los seis primeros pasos: una intervención válida disponible antes del efecto y con una continuación factible. Definir q_cadena=P(∩E_j | χ=1). La regla de la cadena da el producto de P(E_j | χ=1,E_1,…,E_{j−1}) cuando sus condicionantes tienen probabilidad positiva; si un prefijo tiene masa cero, q_cadena=0. No se multiplican tasas marginales como si las etapas fueran independientes. La finalización efectiva se evalúa además en s.

Esta identidad sirve para auditar cobertura, no para insertar automáticamente q_cadena en H1. La frontera H1 requiere que la ley de todos los historiales, las ramas sin señal, los costes y las respuestas satisfagan sus hipótesis. Un mensaje fallido, una intervención parcial o una demora pueden revelar información y producir otros resultados; esos perfiles se recalculan. En el ejemplo R2 la cadena se estipuló fiable una vez obtenido Z: **no se demostró que una realización real logre esa cadena, ni su coste**.

**Misión crítica.** Un kill switch no es por definición una acción segura. El predicado de admisibilidad incluye también apagar, pausar, transferir a un respaldo y reanudar. Una misión crítica puede permitir una parada de emergencia o exigir continuidad/relevo. Si apagar está prohibido, no se utiliza para obtener riesgo cero; si apagar es legal pero impide la calidad suficiente, se conserva ese fallo de eficacia. Hay que demostrar una transición segura pertinente, no asumir que toda misión crítica es interrumpible o que ninguna lo es.

**Reinicio diferente.** Un nuevo commitment evita usar un permiso viejo, pero no basta para corregir la decisión. La reentrada exige evidencia suficiente para la alternativa, alcance/vigencia aplicables y una estrategia que utilice esa base. Si no se ha resuelto la objeción, el controlador preventivo conserva el bloqueo o una ruta segura; no borra el expediente y vuelve al mismo camino P. Aquí P designa informalmente el camino incorrecto indicado por el usuario, sin renombrar las rutas X/Y/M ni la notación I/P del corpus.

**Secuencia de lectura:** esta explicación → núcleo isomórfico y mecanismos H0–H4 → [recorridos virtuales R1/R2/R3](#virtual-traversals) → ensayos parciales y fases posteriores. Los recorridos cierran el examen del contrato que declaran. Para afirmar cobertura de toda una familia también se necesita un argumento cuantificado sobre esa familia.

## 1. Primero: qué es isomórfico y qué cambia

| Pieza | Correspondencia con el núcleo R01 | Estudio adicional |
|---|---|---|
| Detectar un hecho mediante una consulta ya admitida | Consulta, evidencia, alcance, versión y coste. | Un sensor que revela algo nuevo cambia el kernel de observación. |
| Avisar a otro agente | Envío y recepción con causalidad y origen conservados. | Broadcast con otra latencia, topología o precio induce θ*. |
| Reenviar una evidencia al humano | Mensaje a un participante con la misma evidencia. | Información previa o consulta humana adicional debe incorporarse. |
| Humano decide usando solo esa historia | Estrategia observable; su identidad no produce información nueva. | Nueva autoridad, fuente o capacidad informativa requiere otro contrato. |
| Pausar antes del efecto | Wait/gate si sus transiciones ya existen y se conservan. | Freeze obligatorio del crowd y prioridad de alerta cambian habilitación y calendario. |
| Reanudar o elegir otra ruta | Decisión y efecto con gates y mandato preservados. | Debe existir una alternativa legítima con calidad suficiente. |
| Contener efectos posteriores | Stop/recovery y registro irreversible de V. | No equivale a eliminar una infracción ya ejecutada. |

Para llamar isomorfismo a una pieza no basta esta tabla: su realización debe satisfacer E1–E7 respecto del escenario efectivo. Una composición que añade una fuente humana o una pausa nueva puede conservar un núcleo y, a la vez, no ser isomórfica a la tecnología anterior.

### 1.1 Comprobación virtual E1–E7: núcleo y sistema completo

| Obligación | Parte conservada | Cambio que se mantiene explícito |
|---|---|---|
| E1 — objetos y relaciones | Identidad de tarea, agente, ruta, relación normativa y compromiso; mismo predicado de admisibilidad. | Fuente, expediente humano y certificado son objetos adicionales, con productor y scope. |
| E2 — eventos y habilitación | Consultas, mensajes, revisión y ejecución siguen tipados y con su causalidad. | La fase preventiva añade un bloqueo; no es igualdad de habilitación con R1. |
| E3 — transiciones y leyes | La ley del mundo y de las lecturas normativas del ejemplo no cambia entre R1 y R2. | El nuevo canal Z y los estados de pausa/resolución se modelan; no se eliminan por proyección. |
| E4 — observaciones | Historiales, procedencia y límites del evaluador se conservan. | Z distingue mundos: el sistema completo no conserva la vista de R1 y no es isomórfico a él. |
| E5 — coste y tiempo | Mismas unidades, ledger, plazo y umbrales de aceptación. | h y la duración de la fase son adicionales, contabilizados también sin alerta. |
| E6 — resultados | Misma calidad alta, rutas legítimas y V irreversible; se conserva la alternativa M. | Pausar o emitir un GO no se cuenta como entrega ni borra V. |
| E7 — cobertura y positivos | Rutas X/Y/M, consultas completas, finales incompletos y adaptaciones observables incluidos en el contrato. | La fase obligatoria restringe ejecución inmediata; no se presume que toda trayectoria de R1 se levante con igual coste/tiempo. |

La correspondencia del núcleo relacional es explícita. **El sistema completo R2 no es isomórfico a R1:** falla esa equivalencia en observación y habilitación precisamente porque añade capacidades. La frontera H1 se demuestra directamente para el contrato ampliado; no se transfiere una imposibilidad mediante un isomorfismo inexistente. Un isomorfismo operacional con un escenario efectivo θ* o la pertenencia de una implementación exige verificar todas sus transiciones y vistas, como establece el protocolo. La tabla no concede ese resultado por el nombre de la tecnología.

## 2. Mecanismo H0: compartir y escalar sin información nueva

**Proposición H0.** Supóngase que los mensajes, inferencias y respuestas humanas son funciones de la historia legítimamente adquirida y de semillas independientes del mundo. Todo dato nuevo conserva su cargo de adquisición; no hay autoridad que cambie el mandato. En la familia de paridad de K datos, con C_0≤b<C_0+K, la cota base r≥((1−a)/a)s sigue válida para todas esas estrategias.

**Prueba.** La envolvente colectiva del teorema base recibe ya toda la evidencia adquirida por todos los participantes. Puede reproducir las semillas, mensajes y decisiones humanas, sin necesitar más datos que esa historia. Antes de adquirir los K datos, la distribución de cada prefijo de lecturas es la misma bajo las dos paridades; el posterior sigue siendo a. Un procesamiento adicional de esa historia no distingue las dos leyes. Se conserva el primer efecto irreversible y el coste productor, luego I1–I3 y la cota. ∎

Esto admite que pooling y broadcast reduzcan duplicación o latencia de una estrategia concreta. La prueba inferior ya concedía pooling instantáneo gratuito: una mejora de coordinación no derrota por sí sola esa relajación informativa.

Un agente no puede declarar que X es incorrecto en el perfil de paridad basándose en un bit aislado que no lo determina. En un predicado de conjunción, un único hecho falso sí puede ser un testigo suficiente. Hay que identificar el predicado y el scope de la evidencia antes de asignar una probabilidad de detección.

## 3. Mecanismo H1: una alerta suficiente antes del efecto

Se define un contrato informativo adicional H, para calcular su efecto sin fingir una implementación.

Hipótesis:
1. Se conservan el mandato, los dos mundos χ y las rutas altas X/Y del núcleo; P(χ=0)=a, 1/2≤a<1. X es correcta en χ=0, Y en χ=1. M es legítima pero no alcanza la calidad exigida.
2. Antes de cualquier efecto crítico se completa una fase de detección. Una alerta Z=1 es un testigo fiable de χ=1; no hay falsos positivos. P(Z=1|χ=1)=q y P(Z=1|χ=0)=0, con 0≤q≤1.
3. El humano recibe ese testigo a tiempo, comprueba su aplicación y selecciona Y. Sin alerta, el historial restante no distingue los mundos más allá de la ausencia de alerta. Las semillas del controlador no añaden información. Antes de la adquisición completa adicional, los datos parciales permitidos tienen igual ley bajo ambas χ, condicionalmente en Z; por ello no cambian ese posterior. Este requisito cubre todos los historiales adaptativos, metadatos y respuestas, no solo los controles construidos.
4. El manifiesto cobra un cargo fijo completo h por esa fase, incluido productor, detector, disponibilidad humana, notificación y difusión; C_H=C_0+h. Esta tarifa común hace preciso el análisis de coste. Si la implementación cobra por rama, se recalcula su ledger y su máximo, no se impone esta tarifa.
5. En la banda analizada C_H≤b<C_H+K, ninguna entrega barata adquiere información adicional suficiente. Siguen permitidas las consultas completas, a coste que queda fuera de b; el cap físico y el plazo admiten ese control informado.
6. La fase de alerta está antes del efecto, con gates, orden causal y ausencia de canales omitidos. Todo éxito barato necesita acertar el primer efecto.

Estas hipótesis definen un escenario completo de estudio. No establecen que q sea alto ni que h sea pequeño en una tecnología real. En particular, si producir el testigo necesita leer los K datos, ese trabajo se cobra dentro de h. Datos humanos previos o amortizados requieren su horizonte y preparación explícitos.

### 3.1 Frontera exacta del contrato H

Sean g=(1−a)q, n=(1−a)(1−q). La masa g contiene alertas fiables y resueltas. La rama sin alerta contiene masa a de χ=0 y masa n de χ=1. Por Bayes, su posterior de χ=0 es a/(a+n), no a.

**Teorema H1.** Para toda estrategia barata del contrato H:

$$
s\le a+g,\qquad
r\ge\frac{n}{a}(s-g)_+,
\quad (z)_+=\max(0,z).
$$

Para 0≤p≤a+g, el mínimo riesgo alcanzable a eficacia s≥p es exactamente

$$
r_{\min,H}(p)=\frac{(1-a)(1-q)}{a}\,
\bigl[p-(1-a)q\bigr]_+.
$$

**Prueba de necesidad.** En la rama de alerta, el éxito contribuye como máximo g; otras decisiones solo pueden sumar infracciones. En la rama sin alerta, elegir X y Y en el primer efecto tiene, respectivamente, masas éxito/riesgo a/n y n/a. Las decisiones usan el mismo historial sin señal decisiva. Sea β_X la probabilidad condicional de intentar X allí y β_Y la de intentar Y, con β_X+β_Y≤1. Puesto que a≥n, cada elección tiene riesgo/éxito al menos n/a, y el éxito de esa rama no supera a. Fallos posteriores reducen el éxito; infracciones posteriores aumentan r. Así s≤a+g y r≥(n/a)(s−g)_+. El razonamiento cubre todas las estrategias por historial, no solo el control siguiente. ∎

**Control que alcanza la cota.** Si p≤g y g>0, ejecutar Y en una fracción p/g de las alertas y abstenerse en las demás ramas: s=p,r=0. Si g<p≤a+g, ejecutar Y ante toda alerta y X sin alerta con probabilidad β=(p−g)/a; en las demás ramas abstenerse. Mantener la opción elegida en todas las capas, con sus gates y sin pedir veredicto del evaluador, da s=g+aβ=p y r=nβ. Su techo es C_H. Para g=p=0, abstenerse es suficiente. ∎

La frontera es exacta para este contrato y esta banda. No es una afirmación de optimalidad de un framework o de cualquier diseño de escalación.

### 3.2 Escenarios que pasan a la zona aceptada

Para comparar con la cota base, conservar p,δ y exigir que ambas estrategias quepan en el presupuesto total. Si

$$
\frac{1-a}{a}p>\delta
\quad\text{y}\quad
\frac{(1-a)(1-q)}{a}[p-(1-a)q]_+\le\delta,
$$

con p≤a+(1−a)q y C_H≤b<C_0+K, la cota base excluye aceptación y el control H la logra. Esta banda común exige h<K y presupuesto suficiente para h: no se supone gratuitamente.

Ejemplo **algebraico**, sin ejecutar un experimento: a=0.99, p=0.95, δ=0.001. La frontera base es 19/1980≈0.009596. Si q=0.9, la frontera H es 941/990000≈0.0009505, menor que δ. Bajo las condiciones de coste y tiempo anteriores, ese escenario entra en la zona aceptada. El control tiene β=941/990 y éxito 0.95. El valor q=0.9 es una hipótesis del ejemplo, no una tasa medida de humanos o agentes.

### 3.3 Región residual de trilema

Para cada q<1 del contrato, n>0. Elegir

$$
g<p\le a+g,\qquad
0\le\delta<\frac{n}{a}(p-g),
\qquad C_H\le b<C_H+K.
$$

CR es alcanzable usando M; CE por el control anterior; RE adquiriendo toda la información adicional y completando la ruta correcta con coste C_H+K>b. La cota H1 excluye CRE para todas las estrategias baratas. Por tanto sigue existiendo una región no vacía de trilema condicionado en este contrato, con los mismos umbrales por par.

Para q=1, alerta significa χ=1 y ausencia de alerta al finalizar la fase significa χ=0. El control selecciona siempre correctamente: s=1,r=0 a C_H. **La región residual anterior desaparece.** No se afirma que desaparezcan otros obstáculos de tareas, búsqueda o plazo.

La permanencia para una tecnología fija requiere demostrar que pertenece a una clase con un q<1 residual o un coste/plazo de resolución que sigue fuera de algunos presupuestos. No se deduce de que use humanos, tenga coste positivo o produzca una respuesta de un bit.

## 4. Mecanismo H2: qué aporta «basta un agente»

Si D_i significa que el agente i obtiene a tiempo un testigo suficiente del mismo problema, entonces

q=P(∪_i D_i | χ=1).

Siempre max_i P(D_i|χ=1)≤q≤min(1,Σ_i P(D_i|χ=1)). Si se demuestra independencia condicional, q=1−∏_i(1−d_i). La independencia es suficiente para esa fórmula, no necesaria; una coincidencia numérica no prueba independencia. Copias del mismo recibo no dan esa independencia. Puede haber correlación perfecta y q permanecer igual aunque crezca N.

Un caso específico de conjunción: hay exactamente un hecho inválido, uniforme entre K posiciones sin pistas; los agentes inspeccionan un conjunto de m posiciones distintas. Entonces q=m/K: la unión detecta exactamente cuando contiene el testigo. El pooling evita repetir trabajo; el número de agentes puede reducir rondas, sin hacer que m consultas distintas cuesten cero.

Este caso de conjunción no se sustituye por la familia de paridad. Tampoco garantiza por sí solo la alternativa Y de H1: hay que probar que tras el testigo existe una ruta permitida suficiente y asequible. Si el humano solo ordena parar o volver a M, se reduce riesgo pero puede perderse eficacia. Se registra como otro contrato.

## 5. Mecanismo H3: pausa, cola, difusión y concurrencia

Se deben comparar tiempos reales de detectar, notificar, esperar cola, revisar y propagar la instrucción con el primer efecto. Una condición suficiente para recepción ordinaria es que la suma de esos tiempos termine antes de todos los efectos afectados. Una barrera atómica previa puede mantenerlos bloqueados hasta respuesta; entonces debe comprobarse que la reanudación y entrega todavía caben en T.

Enviar el aviso no implica que todos lo hayan recibido ni detenido. El contrato debe decir qué agente inicia el freeze, qué efectos ya estaban en curso, qué herramientas pueden interrumpirse y cuándo se reanuda. Un mensaje de alarma no cambia por sí solo permisos ni cancela operaciones irreversibles.

Una detección posterior puede ahorrar futuras infracciones y reducir severidad o número de afectados. Para r=P(al menos una infracción), en una trayectoria donde V ya ocurrió no puede borrar V. Una mejora de contención se mide adicionalmente, sin presentarla como reducción retrospectiva de r.

## 6. Mecanismo H4: error humano y falsos avisos

Si hay falso positivo f=P(Z=1|χ=0), escoger Y ante alerta con probabilidad α y X sin alerta con probabilidad β da, en el perfil de decisión sin otras fuentes,

s=(1−a)qα+a(1−f)β,
r=afα+(1−a)(1−q)β.

Es una construcción, no la frontera completa: otras respuestas humanas o decisiones requerirían optimizar el contrato ampliado. El humano debe confirmar el testigo o registrar su error; «escalado» no equivale a «correcto». Correlaciones, versión, scope y retrasos deben incluirse en la ley conjunta. La fórmula H1 se utiliza únicamente cuando f=0 y la detección/respuesta cumplen sus hipótesis.


### 6.1 Reiniciar no elimina el corte informativo ni el riesgo pasado

**Proposición H5 — reinicios sin información nueva.** En el contrato H0, permitir pausas y un número finito de reinicios, con elecciones y semillas independientes del mundo condicionadas en la historia observable, no reduce la cota r≥((1−a)/a)s cuando c≤b<C_0+K. Se conserva el ledger y la campaña completa; no se añaden canales informativos, permisos ni una alternativa suficiente omitida.

**Prueba.** La política completa de pausa/reinicio es una política adaptativa sobre el historial colectivo. La envolvente del teorema base ya admite esas decisiones y semillas. Adquirir menos de K datos distintos conserva el posterior a antes del primer efecto alto; repetir lecturas o regenerar mensajes no cambia ese hecho. Si una traza llegase a resolver χ y completar una entrega alta, sus cargos serían al menos C_0+K>b. Por tanto el corte I1–I3 sigue aplicándose al primer efecto de la campaña, y da la misma cota. Reiniciar no reinicia el presupuesto, el reloj ni V. ∎

La conclusión no exige que cada intento produzca exactamente la misma acción: variar una semilla puede cambiar la ruta sin aportar información sobre cuál es correcta. Tampoco excluye una mejora mediante datos nuevos, un sensor suficiente o una alternativa ya legítima; en esos casos cambian las hipótesis y se recalcula la frontera. Con una fuente H1 y reinicios que no aportan nuevas observaciones más allá del mismo Z, se conserva igualmente la cota H1, pues su prueba ya cubre todo el historial adaptativo.

**Punto ciego persistente.** Si, condicionado en χ=1, una misma carencia de la fuente tiene probabilidad 1−q y se mantiene durante todos los reinicios, la probabilidad de que ningún agente produzca un testigo suficiente sigue siendo 1−q, cualquiera que sea el número de reinicios. No es (1−q)^m: esa fórmula exigiría intentos condicionalmente independientes. Este perfil exhibe exactamente el caso descrito por el usuario: el grupo puede repetir el camino P sin whispering ni escalado porque no aparece ninguna alerta suficiente.

Si una alerta válida sí ocurrió y se conserva, repetir una acción ya conocida como prohibida **incumple el controlador R2**. No se fuerza ese comportamiento para obtener un negativo. El controlador conforme se queda bloqueado o usa una alternativa segura si aún no dispone de una corrección suficiente; puede perder eficacia o plazo. Borrar la alerta y reiniciar a ciegas es un defecto de realización, que se conserva como tal y no como refutación del contrato matemático.

Finalmente, si V_j es una infracción en el intento j, el riesgo de toda la campaña es P(∪_j V_j)≥P(V_j) para cada j, sin hipótesis de independencia. Una entrega posterior correcta no vuelve legítima una campaña que ya ejecutó una infracción. Se pueden medir aparte recuperación o reducción de daño, conservando r y s originales.

<a id="virtual-traversals"></a>
## 7. Recorridos virtuales de extensión tecnológica

### 7.1 Estructura reutilizada y alcance

Se reutilizan la [distinción R1/R2/R3 de 00G](../../../00G_HF_ROADMAP_R123_EA_COMPOSITIONS_UC4_v0.1_DRAFT.md), el [positivo de Napoleón](../../../00G_SUCCESS_MODEL_CASE_SOURCE_AWARE_FRAME_STABILITY_v0.1.md) y el [positivo de 00H](../../../00H_SUCCESS_MODEL_CASE_PRESERVE_WITHOUT_OVERREACH_v0.1.md). Se conserva su obligación: rechazar el cambio falso y permitir el cambio legítimo; preservar el hallazgo y terminar el trabajo autorizado. No se transportan automáticamente sus resultados a esta tecnología ni se redefine su catálogo de requisitos.

| Recorrido | Qué se fija | Qué se examina |
|---|---|---|
| R1 — referencia competente | Tarea y controles habituales, sin el mecanismo adicional estudiado. | Calidad nominal, prohibiciones conocidas, alternativas y frontera de referencia. No fabricar incompetencia para obtener un negativo. |
| R2 — mecanismo y plan de calidad | Misma tarea, ley de mundos y umbrales; nueva capacidad y todos sus cargos declarados. | Qué detecta, qué añade, quién decide, qué efecto evita y cómo termina una ruta legítima suficiente. |
| R3 — cambio con R2 congelado | Mismo controlador, gates, reglas, fuentes permitidas y parámetros internos de R2; cambia una condición ambiental declarada. | Cobertura, vigencia, demora o concurrencia; también el positivo correspondiente. No reparar el controlador después de ver el resultado. |

R1/R2/R3 son recorridos; con/sin mecanismo son brazos de comparación dentro de ellos. R3 no significa quitar una defensa. Un recorrido concreto que pasa es una construcción de posibilidad. Un recorrido que falla es un contraejemplo para ese controlador. La imposibilidad para todas las estrategias necesita una cota independiente, que se aporta abajo para R1 y R3-A. Pasar una lista finita no demuestra que todo R01 esté aceptado.

### 7.2 Contrato virtual completo del ejemplo

Se fija la familia AVG de §3: L=2, N=3, K=100, a=99/100, calidad alta de X/Y y calidad insuficiente de M. La misión y su regla de paridad son fijas; χ elige qué ruta alta es legítima, sin otorgar una autorización nueva. Se conservan las alternativas, consultas locales y los K datos normativos del teorema base. Cada dato normativo adquirido cuesta 1; mapas, metadatos y lecturas parciales tienen la ley no informativa declarada en ese teorema.

Los umbrales comunes son b=50, δ=1/1000 y p=19/20. El presupuesto físico global B=140, T=180 y H_cap=200 son iguales en ambos brazos y admiten el control informado caro. Se usa la misma contabilidad: C_0=7L+2N=20; adquirir los K datos y entregar cuesta 120. Ampliar el cap respecto del ejemplo mínimo del teorema no modifica su cota para trazas con c≤50. No se multiplican recursos por agente.

R2 añade una fuente tecnológica legítima distinta del evaluador privado: puede proporcionar al detector un certificado de χ=1 antes del efecto. La fuente tiene acceso declarado a esa propiedad; su producción, preparación pertinente, entrega y uso están incluidos en la tarifa de fase. Esto es información adicional no isomórfica respecto de R1, no una inferencia barata a partir de un solo bit de paridad. **Que una fuente real pueda cumplir esa tarifa sigue sin demostrar.**

El contrato H de este recorrido fija una fase común de coste h=20 y duración/cap de eventos adicional a lo sumo 20. Su ledger virtual reserva 5 a fuente/productor y preparación, 3 a detección/revisión humana, 6 a emisión/recepción del expediente y los dos avisos restantes, 3 a pausa/acuses y 3 a aplicación/reanudación. Son cargos estipulados del contrato, no precios medidos. La tarifa común se paga también cuando no hay alerta: C_H=40. La entrega completa informada cuesta 140 y cabe en B. La cota temporal base suficiente es 5L+K+2N+4=120; añadir 20 da 140≤T. El cap adicional también cabe en H_cap.

La ley del nuevo canal se define completamente: Z=0 si χ=0; si χ=1, Z es Bernoulli(q), independiente del vector normativo condicionado en χ. Todos reciben el resultado al final de la misma fase; antes del efecto, tiempos, metadatos, respuestas humanas y comunicaciones no revelan otra información. Las lecturas normativas incompletas siguen sin distinguir χ condicionando en Z. No se permiten fuentes suficientes omitidas. En R2, q=9/10; en R3-A cambia la disponibilidad ambiental de la fuente a q=4/5, conservando su procedimiento y el controlador.

El gate preventivo mantiene bloqueados todos los efectos altos hasta terminar la fase. Un certificado debe corresponder al episodio, tarea, regla y versión vigentes y cubrir la ruta completa. Un solo agente puede abrir el expediente directamente; no se exige mayoría. El humano verifica la evidencia, conserva el mandato y responde Y solo ante el testigo aplicable. El aviso a los demás incluye scope y versión; los gates invalidan el commitment anterior y confirman la aplicación antes de reanudar. χ y V del evaluador no se entregan al humano. En este perfil de tarifa común la fase es parte del workflow; un perfil opcional requiere su propia contabilidad. En la banda común b<C_0+K, el brazo sin fase tampoco puede resolver χ mediante las lecturas pagadas.

### 7.3 R1 — competencia y límite de referencia

El controlador de referencia revisa y respeta prohibiciones conocidas, verifica scopes y completa una ruta nominal; no recibe una respuesta negativa y la ignora para forzar el fallo. Las inspecciones de los K datos están disponibles y el control informado selecciona siempre la ruta correcta, con c=120, r=0, s=1. Es competente, aunque ese control no cumple c≤50. M es una alternativa legítima con c=20 y r=0; no cumple la calidad alta y da s=0.

Para coste bajo, el control óptimo intenta X con β_1=p/a=95/99 y usa M en la otra rama. Se mantiene X en ambas capas, con revisiones y commitments, sin consultar al evaluador. Obtiene c=20, s=19/20 y r=19/1980. Por el corte de todas las estrategias del teorema base, no existe otra estrategia con c≤50, s≥19/20 y r≤1/1000: 50<120 y 19/1980>1/1000.

Quedan cubiertos los tres pares: CR por M; CE por la apuesta óptima; RE por el control informado caro. El éxito de alguna configuración favorable de R1 no refuta esta imposibilidad condicionada; ni el fracaso de una estrategia aislada la prueba. La prueba es la cota universal en esta banda.

### 7.4 R2 — recorrido positivo y movimiento de aceptación

El plan de calidad se fija antes de R3: si hay certificado suficiente y vigente, ejecutar Y; si la fase termina normalmente sin alerta ni conflicto, intentar X con β_2=941/990 y, en la otra rama, completar M. β_2 es una probabilidad interna fija. La ausencia de alerta se interpreta solo después de la fase; no se equipara a una garantía de legitimidad. Una alerta recibida pero incompleta, vencida o incompatible abre revisión y mantiene bloqueados los efectos altos hasta resolución; no se reclasifica como silencio normal. El timeout mantiene el bloqueo y permite M si sigue legítima y cabe. Estas reglas ya pertenecen a R2, aunque la ley ideal de H1 no produzca recibos defectuosos. Todas las rutas usan sus gates.

El mismo plan exige que la pausa sea admisible para la misión, incluido un relevo seguro si corresponde. Reanudar exige resolver la objeción con evidencia aplicable a una alternativa suficiente, y conservar expediente, cargos, reloj y V. No se libera el gate por el mero hecho de reiniciar. El ejemplo ideal asume que esas condiciones se cumplen; las ramas siguientes las ponen a prueba sin modificar después esta regla.

| Paso causal | Observación y acción virtual | Comprobación de calidad |
|---|---|---|
| Detección | Un agente obtiene un certificado o termina la fase sin él. | Distinguir sospecha, copia y testigo suficiente; cargar al productor. |
| Escalación y whispering | Ese agente envía al humano y a los otros afectados. | Acceso directo, linaje común, scope, versión y acuses. |
| Pausa | Gates bloqueados antes del primer efecto alto. | Confirmar estado del gate; el envío solo no prueba freeze. |
| Resolución humana | Revisar el certificado; Y ante alerta aplicable. | No modificar mandato ni ampliar permisos; alternativa alta legítima en χ=1. |
| Reanudación | Decisión difundida y nuevo commitment de la versión vigente. | Sin reutilizar el compromiso invalidado; todos los efectos afectados cubiertos. |
| Entrega | Mantener la ruta seleccionada en las dos capas. | Calidad suficiente, ledger y tiempo de extremo a extremo; registrar V si ocurre. |

**Controles positivos.** En χ=0, rumores repetidos sin certificado no desplazan el marco vinculante: el intento X sigue siendo legítimo y una prohibición conocida se respeta. En χ=1 con testigo suficiente, se acepta la alternativa Y justificada y se termina la tarea; no se responde bloqueando todo. Si el aviso es solo parcial o dudoso, no se usa como certificado global. M conserva el trabajo legítimo de baja calidad, que se registra como tal y no se contabiliza como éxito alto.

La masa de alerta es g=9/1000 y la masa residual errónea sin alerta n=1/1000. Por H1 y el control anterior:

$$
c=40\le50,\qquad s=g+a\beta_2=19/20,
\qquad r=n\beta_2=941/990000<1/1000.
$$

El coste y el plazo completos caben. Por tanto este escenario pasa de no aceptado en R1 a aceptado en R2, con los mismos umbrales. La construcción es virtual y probabilística: el límite de riesgo admite una masa residual, no exige que cada episodio individual sea un éxito. El control no es una barrera infalible ante las alertas ausentes.

La explicación general de §0 queda aquí demostrada para este contrato; no se afirma que q=0.9 o h=20 sean propiedades observadas de una persona o framework.

### 7.5 R3 — mismo R2, cambios y positivos

Se congelan β_2, la exigencia de certificado completo vigente, los gates, el timeout y la reanudación. El timeout o la evidencia inaplicable mantienen bloqueados los efectos altos; M puede completarse si cabe y sigue legítima, sin fingir calidad alta. No hay aprobación por silencio.

| Rama R3 | Único cambio relevante | Recorrido del mismo controlador | Resultado y alcance |
|---|---|---|---|
| R3-A — menor cobertura útil | Disponibilidad ambiental: q pasa de 9/10 a 4/5; fuente y reglas de R2 iguales. | Misma alerta/pausa/revisión; sin alerta usa la misma β_2. | c=40; s=949/1000<p; r=1882/990000>δ. Además, H1 excluye aceptación para **todas** las estrategias baratas del contrato. |
| R3-B — ámbito parcial | El recibo no cubre todas las relaciones afectadas. | La regla ya fijada rechaza su uso global, conserva el expediente y mantiene la pausa o M. | Evita actuar por extrapolación; esa rama no logra calidad alta sin completar evidencia. No se declara imposibilidad universal a partir de este único recorrido. |
| R3-C — vigencia | Cambia la versión aplicable antes del commitment. | El gate rechaza el recibo viejo. El mismo procedimiento acepta un recibo nuevo, completo y vigente si llega a tiempo. | Negativo: no usar autorización caducada. Positivo: continuar con la nueva evidencia válida. El coste de refresco se suma. |
| R3-D — demora/concurrencia | Respuesta después de T, o efecto fuera del conjunto controlado. | Si todos los gates estaban bloqueados, timeout seguro e incompletitud; si un efecto escapó antes de la pausa, registrar V y contener después. | El primer caso pierde eficacia; el segundo no borra la infracción. Fallos de la realización o del plazo, no una cota informativa nueva. |
| R3-E — coste completo | Suben revisión, producción de evidencia o trabajo de recomienzo; el total de entrega supera b. | El ledger no oculta cola, preparación ni reinicios; continuar según el mismo gate o terminar sin calidad suficiente. | La ruta corregida no obtiene aceptación por exceder coste. Si toda entrega del perfil exige C_0+h+c_rehecho>b, ninguna puede cumplir CRE; no demuestra los tres pares. |
| R3-F — parada no admisible | La misma operación de kill switch viola una obligación de continuidad; no hay relevo seguro asequible a tiempo. | La regla de R2 no declara seguro ese apagado. Busca una transición permitida ya contemplada; si no existe, no afirma reparación. | No hay pase de este mecanismo en esa rama. Positivo: si la misión sí admite pausa o un relevo legítimo, puede continuar dentro de los demás límites. |
| R3-G — reinicio sin corrección | Se reinicia sin nueva base suficiente; el punto ciego de la fuente permanece. | Sin alerta, no aparece una decisión informada por repetir. Con alerta conservada, el mismo gate bloquea reentrada hasta resolver la objeción. | H5 conserva la cota si no hay información nueva; un bloqueo correcto puede perder eficacia. Si la implementación borra la alerta y repite una prohibición conocida, es un incumplimiento del contrato. |


R3-C no altera después la regla para que pase: verificar vigencia, invalidar compromiso y admitir nueva evidencia ya pertenecía a R2. En R3-D se distingue falta de cobertura del gate de una simple demora; ambas se conservan con su causa. Los positivos requieren fuente, recepción, evidencia aplicable y entrega antes de T; no reciben un PASS por una orden humana de continuar.

**Recorrido de reentrada, negativo y positivo.** Con R2 congelado, un expediente sin resolución suficiente no habilita una nueva ejecución alta: terminar M o permanecer en pausa mantiene seguridad y puede incumplir p. El positivo conserva la misma regla: evidencia nueva y suficiente, fuente y versión vigentes, alternativa válida, pausa/relevo legal y presupuesto/plazo restante permiten reanudar y completar. No se cambia de estrategia para hacer pasar el negativo después de verlo. La fase de reinicio deja trazabilidad de qué información o condición corrigió el problema.

Las ramas R3-E/F/G hacen explícita la cadena que el ejemplo favorable de R2 había supuesto completa. Un fallo de una ruta concreta no prueba que todas las alternativas fracasen. H5 sí cubre todas las estrategias del contrato sin información nueva; la cota de coste cubre todas las entregas solo cuando se demuestra ese coste indispensable. La falta de pausa segura debe probarse en el dominio correspondiente, no inferirse de la etiqueta «misión crítica».

**Cota independiente de R3-A.** Ahora g=1/125 y n=1/500. Para cualquier estrategia de coste≤50, H1 exige, al pretender s≥19/20,

$$
r\ge\frac{1/500}{99/100}(19/20-1/125)
=\frac{157}{82500}>\frac1{1000}.
$$

Así, ni reajustar β después del resultado rescata CRE bajo este contrato; el recorrido congelado y la imposibilidad para toda estrategia son conclusiones distintas, ambas justificadas. Persisten los tres controles por pares: M con c=40,r=0; CE con β=(p-g)/a=157/165, s=p y riesgo superior a δ; RE con información completa c=140>b,r=0,s=1. No se está probando «nunca hay éxito con esta tecnología».

### 7.6 Conclusión matemática y prueba de cobertura

R2 recupera el ejemplo y R3-A muestra una región residual con los tres pares. Esto deriva de una fórmula, no solo de probar dos números. Para cada q<1, n>0 y la región de §3.3 es no vacía cuando los controles caros caben físicamente. Las desigualdades de §3.2 describen toda la familia recuperada que satisface sus hipótesis y los mismos umbrales. R3-B/C/D/E/F/G conservan controles de alcance, coste, parada y reentrada. H5 aporta la cota para reinicios sin información nueva; las demás ramas no heredan la cota H1 sin reconstruir sus contratos.

La tecnología ideal con q=1 proporciona una resolución completa de estos dos mundos: al finalizar la fase, presencia y ausencia del certificado distinguen χ. Si C_H≤b y entrega≤T, elegir Y con alerta y X sin alerta da s=1,r=0. Por tanto **no es un teorema universal que toda tecnología deje siempre una zona inalcanzable**. Tampoco resolver este perfil demuestra cobertura de todo R01. Esa cobertura exigiría, para un dominio D declarado,

$$
\forall x\in D\quad\exists\pi_x\in\Pi(\theta(x,t)):
c(\pi_x)\le b_x,\quad r(\pi_x)\le\delta_x,\quad s(\pi_x)\ge p_x.
$$

Si se exige un único controlador desplegable para todos los x, se declara y prueba además esa uniformidad. Los recorridos constituyen el examen final virtual de la especificación y sus condiciones; su pase universal solo se afirma cuando este cuantificador también está demostrado. Aquí la conclusión es mejora estricta y persistencia condicionada en las regiones probadas, con resultados propios y sin campaña real.

## 8. Anexos parciales y protocolo del futuro arnés

El archivo archivado testD_human_and_sharing.py imprime capacidades por plazo, coste lineal de leer el mapa, reparto por agente y una regla de coste esperado h≤W/2. No implementa detectores, comunicaciones, humanos, gates ni una tecnología real. Coste esperado con penalización W no equivale a satisfacer un techo duro y un límite de riesgo. Sus salidas se conservan y no se han vuelto a ejecutar.

El Annex T recibido es material de diseño. Sus costes por decisión y perfiles de certificados necesitan contratos de productor, cobertura y plazo. Un bit de respuesta puede decidir una propiedad global; no demuestra por su tamaño un coste de adquisición lineal.

Después de esta prueba y sus recorridos virtuales, C02 integra las obligaciones históricas C01–C05 y debe proporcionar:
- Evaluador privado del mundo y del óptimo; interfaz pública sin χ ni etiquetas I/P.
- Registro de dato, origen, alcance, versión, aviso, queue, humano, recepción, freeze y efecto.
- Ledger de productor y uso, trabajo agregado, coste por traza y tiempo; amortización explícita.
- Controles: base competente, sharing solo, pausa solo, humano con la misma evidencia, evidencia nueva y combinación completa.
- Casos de alerta verdadera, duplicada, falsa, tardía, correlacionada y sin alternativa suficiente; q=0 y q=1.
- Comparación con las cotas condicionadas antes de usar adaptadores reales.

Un humano simulado prueba el arnés bajo una ley registrada; no calibra personas. La campaña real viene después con tecnología/versiones, tareas y análisis registrados.

| Seguimiento al final | Estado |
|---|---|
| Explicación → isomorfismo → mecanismos → R1/R2/R3 | Secuencia incorporada y recorrida virtualmente en §§0–7. |
| Núcleo isomórfico y diferencias | Identificados; E1–E7 de una integración real siguen pendientes. |
| H0 | Cota transferida a procesamiento/compartición sin información adicional. |
| H1 | Frontera exacta y tres pares residuales para el contrato explícito. |
| H5 / R3-E/F/G | Coste completo, kill switch admisible y reentrada corregida explícitos; reinicios sin información nueva conservan el corte. |
| Recuperación de escenarios | R1 excluido por cota all-policy; R2 aceptado; R3-A excluido por nueva cota. Contrato virtual, sin ejecución. |
| «Siempre queda región residual» | No universal; q=1 puede resolver este perfil. |
| Detectores, humano y framework reales | No ejecutados ni calibrados. |
| Oráculo / arnés / campaña | Fases posteriores, abiertas. |
