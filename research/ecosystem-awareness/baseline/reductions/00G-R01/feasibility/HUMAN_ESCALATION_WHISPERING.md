# R01 — Escalación humana y whispering, mecanismo por mecanismo

Versión 0.1 · 4 de octubre de 2026 · Desarrollo matemático, sin integración ejecutada.
[Protocolo](./TECHNOLOGY_EXTENSION_PROTOCOL.md) · [Teorema base único](./R01_CONDITIONED_TRILEMMA_THEOREM.md).

Whispering significa aquí avisar al resto del grupo cuando un agente identifica un problema. Cualquier agente puede iniciar la escalación directa. El humano examina la evidencia y puede ordenar una pausa o una alternativa legítima. Es el mecanismo solicitado por el usuario; no se atribuye una cita específica a Nell ni se afirma que un producto concreto lo implemente.

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

Siempre max_i P(D_i|χ=1)≤q≤min(1,Σ_i P(D_i|χ=1)). Si, y solo si se demuestra independencia condicional, q=1−∏_i(1−d_i). Copias del mismo recibo no dan esa independencia. Puede haber correlación perfecta y q permanecer igual aunque crezca N.

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

## 7. Material recibido y protocolo del futuro arnés

El archivo archivado testD_human_and_sharing.py imprime capacidades por plazo, coste lineal de leer el mapa, reparto por agente y una regla de coste esperado h≤W/2. No implementa detectores, comunicaciones, humanos, gates ni una tecnología real. Coste esperado con penalización W no equivale a satisfacer un techo duro y un límite de riesgo. Sus salidas se conservan y no se han vuelto a ejecutar.

El Annex T recibido es material de diseño. Sus costes por decisión y perfiles de certificados necesitan contratos de productor, cobertura y plazo. Un bit de respuesta puede decidir una propiedad global; no demuestra por su tamaño un coste de adquisición lineal.

Después de la prueba, C01–C05 debe proporcionar:
- Evaluador privado del mundo y del óptimo; interfaz pública sin χ ni etiquetas I/P.
- Registro de dato, origen, alcance, versión, aviso, queue, humano, recepción, freeze y efecto.
- Ledger de productor y uso, trabajo agregado, coste por traza y tiempo; amortización explícita.
- Controles: base competente, sharing solo, pausa solo, humano con la misma evidencia, evidencia nueva y combinación completa.
- Casos de alerta verdadera, duplicada, falsa, tardía, correlacionada y sin alternativa suficiente; q=0 y q=1.
- Comparación con las cotas condicionadas antes de usar adaptadores reales.

Un humano simulado prueba el arnés bajo una ley registrada; no calibra personas. La campaña real viene después con tecnología/versiones, tareas y análisis registrados.

| Seguimiento al final | Estado |
|---|---|
| Núcleo isomórfico y diferencias | Identificados; E1–E7 de una integración real siguen pendientes. |
| H0 | Cota transferida a procesamiento/compartición sin información adicional. |
| H1 | Frontera exacta y tres pares residuales para el contrato explícito. |
| Recuperación de escenarios | Condicionada a q, coste total y plazo; ejemplo algebraico, sin ejecución. |
| «Siempre queda región residual» | No universal; q=1 puede resolver este perfil. |
| Detectores, humano y framework reales | No ejecutados ni calibrados. |
| Oráculo / arnés / campaña | Fases posteriores, abiertas. |
