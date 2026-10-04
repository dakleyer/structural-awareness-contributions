# R01 — Revisión estratégica y prompt completo de ejecución

Iván Abril Palma, Tegrity.AI · Plan vigente v0.3 · 4 de octubre de 2026; revisión v0.2 conservada como historia

[README de R01](./README.md#bot-start-here) · [Viabilidad matemática](./MATHEMATICAL_FEASIBILITY.md) · [Computabilidad y oráculo](./COMPUTABILITY_AND_ORACLE_PLAN.md) · [Diferencial y valor](./DIFFERENTIAL_AND_EXPERIMENT_VALUE.md) · [Integraciones](./extensions/hugging-face/REMAINING_TASKS.txt) · [Evidencia de esta revisión](./feasibility/previous-work/WORKPLAN_REVIEW_EVIDENCE_2026-10-03.json)

<a id="mathematical-strengthening"></a>
## Plan vigente — demostración por familias y controles complementarios

Reorganización v0.3 · 4 de octubre de 2026 · Entrada `dbae916553166a29f9e756f8c7a6efdfa4c93c21` · Revisión de planificación, sin resultados científicos nuevos.

**Este apartado, el registro de tareas actualizado y las puertas G0–G6 son el orden vigente.** Las puntuaciones y el orden de v0.2, así como los registros de entregas anteriores, se conservan como historia; no prevalecen sobre esta reorganización. La dirección elegida es la petición de Iván: una familia parametrizada y una demostración para todas las políticas admitidas. Los casos pequeños y el oráculo apoyan y atacan la prueba. La utilidad de un piloto para elegir arquitectura conserva un estudio posterior separado.

### Trabajo realizado: qué se reutiliza y qué sigue pendiente

| Evidencia existente | Disposición actual | Papel en el trabajo siguiente |
|---|---|---|
| M01: dominio y cuantificadores iniciales | DONE solo para su formulación histórica | Entrada al nuevo contrato M12; no confundir la pareja estática con toda la familia. |
| M02: pareja con un binding, 27 rutas, 76 checks | DONE para construcción y controles | Control contractual y caso límite; no aporta crecimiento de información con L. |
| M10/P03: contrato y medidas, 35 checks | DONE para la reconciliación histórica | Conservar recibos, costes completos, infracción irreversible y métricas originales. |
| M03/M04: derivaciones F/W y 4.555 checks | **IN_PROGRESS en el objetivo ampliado**; derivaciones existentes conservadas | Revisar lemas, fronteras y políticas que alcanzan las cotas; no afirmar cierre final ni revisión independiente. |
| F: bindings independientes | Derivación lineal, revisión independiente pendiente | Base transparente para la frontera; accesos de coordenadas no equivalen a consultas globales. |
| W: conjunción de n relaciones, n=Theta(L²) | Derivación cuadrática, revisión/puente pendientes | Candidato fuerte frente a ejecución lineal; su prior correlacionado y su interfaz son hipótesis explícitas, no entropía de n bits independientes. |
| W5: presupuesto esperado | Cota inferior existente, no frontera exacta general | Complementa el presupuesto por traza; no intercambiar los perfiles. |
| Certificados, barreras y despacho autorizado | Resultados de subperfiles, clasificación general pendiente | Entradas de M13 y ataques; contar productor y cambios de mecanismo. |
| Checkers propios y documentos de conservación | Evidencia finita y revisión propia | No cierran M05/C05 ni M16. Los fallos heredados P08 siguen registrados. |

Se mantienen los 49 IDs originales y sus criterios; se añaden M12–M17 para obligaciones que no quedaban suficientemente separadas. **Estado: 55 tareas; 4 DONE históricas, 5 IN_PROGRESS y 46 OPEN.** M03/M04 se reabren por ampliar el objetivo y sus requisitos de aceptación; esto no registra un contraejemplo ni invalida automáticamente sus derivaciones anteriores. Los textos que dicen 6 DONE en los registros anteriores describen aquella entrega. Estado y dependencias computables: [registro vigente](./feasibility/previous-work/R01_MATH_WORKPLAN_2026-10-04.json). Evidencia documental: [auditoría de reorganización](./feasibility/previous-work/R01_REORGANIZATION_CHECKS.json).

### Objetivo matemático y orden de cuantificadores

M12 debe congelar el contrato antes de añadir nuevas familias. Se separan: tecnología/interfaz tau; configuración theta; mundo oculto omega; política pi; y resultados C, eta técnica, rho de infracción y sigma de éxito legítimo. La política es común a mundos indistinguibles; no se selecciona con etiquetas ocultas. Los umbrales se fijan antes de observar resultados. eta no sustituye e/a/q originales de R01.

La tesis mínima es: existe una familia de configuraciones y una clase de políticas explícita para las que cada par de {coste bajo, riesgo bajo, eficacia técnica alta} tiene un testigo, pero ninguna política logra los tres en una banda no vacía. La banda debe tener una cota necesaria y un control suficiente si se llama frontera exacta. Otras configuraciones deben conservar controles viables. El conjunto inviable y su complemento lógico son distintos de lo que la evidencia deja sin resolver.

Para la tesis tecnológica fuerte, la clase de tecnologías tiene que definirse antes de cuantificar: **para toda tau de una clase declarada y todo margen relativo finito lambda, existe L0(tau,lambda,h,r) tal que, para todo L>=L0 y toda política admitida que respete el presupuesto, falla al menos un objetivo**. En WC el fallo puede estar en algún mundo; no significa que toda política falle en cada mundo. En AVG la distribución se fija con la familia antes de elegir la política. F no prueba por sí sola esta tesis para cualquier lambda; W densa es candidata bajo h>2r, precios mínimos fijos y ejecución lineal. No se cuantifica sobre toda tecnología posible.

El trilema exige demostrar los tres pares en las mismas configuraciones difíciles, sin cambiar el mandato, el óptimo ni la información inicial entre testigos. Solo varían política y recurso que se acepta sacrificar. Verificar que no es una tarea imposible incluso con información completa. Número de segmentos, agentes y distancias son parámetros a modelizar; ninguno se identifica automáticamente con número de hechos nuevos ni con su complejidad de consulta.

### Prioridad actual y combinación de los dos caminos

| Orden | Bloque | Resultado que desbloquea | Qué no permite afirmar todavía |
|---|---|---|---|
| 1 — P0 | M12 con M01/M10/P03; P08/C01 acotados; M06/M11/P01/P02 activos | Un contrato objetivo y matriz de afirmaciones/hipótesis. Primera pasada: identificar posibles certificados, rutas comunes y costes omitidos. | Que el trilema ya esté revisado o que la auditoría completa esté reparada. |
| 2 — P0/P1 | M03/M04 y ataques M06/M11 | Pruebas para toda política, testigos de los tres pares, fronteras inclusivas y separación de coste máximo/esperado. | Exactitud de una frontera obtenida solo de una cota necesaria. |
| 3 — P1 | M16 y M05/C02–C05, sin ampliar el oráculo completo por defecto | Revisión simbólica independiente y segundo método finito, primero sobre F/W y sus controles. Pueden prepararse tras congelar M12; el cierre espera la versión de lemas revisable. | Que dos scripts compartidos equivalgan a independencia o que enumeración pequeña sea prueba para todos los tamaños. |
| 4 — P1 | M13 y primer tramo de M17/M07 | Clasificación por capacidades/costes y puente, o límite explícito a familias suplementarias. | Transferencia a R01 o a una marca comercial por igualdad de nombres/campos. |
| 5 — P2 | M14/M15 y revisión de ampliaciones | Perfiles de ruido/caché/amortización y distribución/geometría cuando sean parte de la afirmación. | Latencia a partir de trabajo agregado o frescura a partir de persistencia. |
| 6 — P3 | C06–C13 y T01/T02/T11; después T03–T12 | Campaña registrada e integraciones calificadas. La investigación documental de interfaces puede alimentar M13 desde antes. | Imposibilidad universal por observar fallos; causalidad histórica o ventaja de EA. |
| 7 — P3 | P11/C14/P12 | Valor de un piloto para decidir entre arquitecturas. | Que una frontera matemática o un oráculo correcto demuestren utilidad prospectiva. |

No es un orden que obligue a completar M14/M15 para publicar la tesis mínima. Si las ampliaciones no están probadas, se declaran fuera de alcance. Un estudio empírico autónomo puede continuar con contrato propio cuando una transferencia fracase; no se usa para cerrar el teorema. El instrumento neutral mínimo puede prepararse durante la prueba, sin volver a convertir la campaña en el eje del trabajo.

### Dependencias de las nuevas obligaciones

Los siguientes criterios complementan los 49 originales. M12 usa resultados históricos, M03/M04 se revisan contra él, M16 revisa las derivaciones y M17 prueba transferencia. No se crea una dependencia circular entre prueba, auditoría y puente: se versionan contratos, se revisa una versión identificada y los hallazgos reabren la afectada. Responsable de esta reorganización: Codex por instrucción de Iván; ejecutores futuros y revisor independiente: UNASSIGNED hasta aceptación real.

**M12 — OPEN — Contrato del teorema objetivo y mapa de obligaciones.** Prioridad P0. Depende de M01, M02, M10, P03. Cierre: Contrato versionado de parámetros independientes theta=(L,n,N,geometría,interfaz,prior,costes,datos previos,umbrales), políticas y resultados C/eta/rho/sigma. Separar AVG/WC, presupuesto por traza/esperado y trabajo/latencia. Fijar cuantificadores tecnología→familia→tamaño→política y los tres controles por pares, familias viables e inviables. Inventario de afirmaciones con hipótesis, lema, construcción y revisión requerida; separar tesis mínima de ampliaciones. No inferir dureza de L, N o distancia por sí solos.

**M13 — OPEN — Teoremas sobre clases tecnológicas y coste completo.** Prioridad P1. Depende de M03, M04, M12, M06, M11. Cierre: Clasificar interfaces de coordenadas, predicados/certificados globales y ejecutores/barreras; definir simulación observable y cargos que justifican heredar una cota. Para cada clase: hipótesis, coste productor/uso, cota inferior, control superior o límite abierto, cambio de kernel y eliminación absoluta/relativa o solo del riesgo. Comparar f(n(L))/C0(L); conservar casos que empeoran. Un nombre comercial, coste positivo o tamaño de salida no establece pertenencia ni persistencia.

**M14 — OPEN — Robustez con información parcial, ruido y amortización.** Prioridad P2. Depende de M12, M11, M03, M04. Cierre: Fijar perfiles separados para certificados parciales/ruidosos/obsoletos, información inicial, caché y costes de preparación repartidos en varios episodios. Mantener leyes de error, frescura, correlación y cargo total. Derivar cotas y controles donde se afirme generalización; en los demás perfiles registrar OUT_OF_SCOPE o UNRESOLVED. Distinguir datos nuevos del reaprovechamiento y presupuesto por ejecución del esperado; W5 no se anuncia como frontera exacta.

**M15 — OPEN — Extensión distribuida y geométrica: trabajo y latencia.** Prioridad P2. Depende de M12, M03, M13. Cierre: Definir red de N agentes, ubicación de hechos, distancias/topología, capacidad y precio de mensajes, colas y plazo. Conservar la envolvente centralizada para trabajo agregado. Para cualquier afirmación temporal nueva, derivar cota de comunicación/camino crítico y un control realizable, cobrando duplicación y mantenimiento. Identificar regiones donde paralelismo/cercanía resuelven el plazo y donde no. No extrapolar las cotas de trabajo a tiempo o geometría.

**M16 — OPEN — Revisión simbólica independiente de la demostración.** Prioridad P1. Depende de M03, M04, M06, M11, M12. Cierre: Revisor distinto del autor y no asignado ficticiamente: reconstruir F1–F4, W1–W5, G1, T1/T2 y cuantificadores, cubriendo políticas omitidas, normalización, presupuesto en ramas fallidas, abstención, igualdad y controles conocidos. Dictamen por afirmación: VALIDATED_IN_SCOPE, COUNTEREXAMPLE o GAP; M13–M15 se revisan separadamente si se incluyen. No basta ejecutar el script del autor. Considerar formalización de los lemas críticos si aporta cobertura; un intento incompleto no es prueba formal. Revisión propia puede continuar sin cerrar esta tarea.

**M17 — OPEN — Puente matemático entre las familias y R01.** Prioridad P1. Depende de M12, M03, M04, M06. Cierre: Elegir un objetivo explícito: familia suplementaria o subfamilia de R01. Para afirmar lo segundo, construir embedding/reducción de mundos, acciones, observaciones, efectos y costes; mapear TODAS las políticas relevantes de R01 a la clase cubierta, incluyendo conectores, geometría, autoridad, consultas y barreras. Comprobar dirección de la reducción: no basta exhibir una política ni preservar trazas seleccionadas para transferir imposibilidad. Limitar el resultado a un submodelo o marcar GAP si R01 aporta información o acciones adicionales. E1–E7 y coherencia M07 no sustituyen la reducción.

### Material adicional recibido — prioridad matemática, 4 de octubre de 2026

Se conservan [seis originales y sus salidas](./feasibility/partial-experiments/received/2026-10-04/README.md) como material de apoyo, sin sustituir el plan ni cerrar tareas. Los cuatro scripts se ejecutaron sin error; la admisión encontró contraejemplos que deben incorporarse a M12/M06/M11: fórmula de presupuesto que ignora eficacia; confusión entre recuperar el mundo y entregar una ruta; límites de estimaciones de capacidad, frescura, amortización y contención posterior al efecto. El anexo tecnológico queda en segundo lugar, para M13/T. **La prioridad es comprobar que el trilema sea una imposibilidad real dentro del modelo y que sus supuestos no fabriquen el resultado.** Estado matemático: derivaciones F/W disponibles, revisión independiente y puente a R01 pendientes. No hay validación empírica de incidencia en despliegues. M12 sigue siendo la siguiente entrega. Estado total sin cambios: 55 tareas, 4 DONE históricas, 5 IN_PROGRESS, 46 OPEN.

### Prompt rector para ejecutar y revisar el camino combinado

Trabaja desde README de R01 y el commit de entrada real. Lee este plan vigente, los registros M01/M02/M10, M03_M04_TRILEMMA_THEOREMS.md y TRILEMMA_CONTRACT.json; conserva la propuesta recibida. Comienza con M12 y su primera pasada dirigida M06/M11, sin volver a enumerar M02 como estrategia central. Entrega un contrato y matriz de obligaciones: para cada afirmación, parámetros, cuantificadores, hipótesis observables, lema, política constructiva, evidencia disponible, laguna y criterio de aceptación. Después revisa M03/M04: prueba necesidad para TODAS las políticas de la clase y suficiencia con controles que alcancen las fronteras. No confundas supremum y máximo alcanzado, AVG y WC, eficacia técnica y éxito legítimo, trabajo y latencia, presupuesto duro y esperado. Conserva fronteras vacías y contraejemplos.

Usa M16 para reconstrucción simbólica por otro revisor, y M05/C05 para un método finito implementado separadamente, sin importar la recurrencia del autor. La comparación independiente debe ser semántica después de normalizar mundos/trazas/racionales; igualdad de bytes solo se exige para reproducir el mismo reporte. Entrega las discrepancias, no las ajustes a posteriori para obtener coincidencia. No afirmes independencia sin su evidencia.

En M13, intenta refutar la herencia tecnológica con predicados, certificados baratos, barreras, rutas comunes y ejecución autorizada. Cuenta producción, acceso, verificación, caché y preparación amortizada. Declara qué añade cada interfaz, si una simulación observable y de costes permite aplicar el teorema, y si reduce una banda, elimina su margen relativo, elimina riesgo o resuelve toda la región declarada. Un coste positivo no prueba persistencia y una cota de capacidad no prueba disponibilidad de un servicio a ese precio.

En M17, demuestra o rechaza el puente hacia R01 para todas las políticas relevantes. No traslades imposibilidad con una mera correspondencia de trazas seleccionadas. Si no hay puente, conserva un teorema de familia suplementaria válido en su alcance. M14/M15 amplían ruido/amortización y distribución/geometría solo con nuevos contratos y pruebas; una región aún desconocida permanece UNRESOLVED. Verifica literatura primaria y diferencial sin inventar novedad. Mantén las obligaciones de corpus, legibilidad, visuales y conservación en cada entrega. No borres historia ni repares congelados silenciosamente.

Antes de modelos/adaptadores amplios, verifica qué incertidumbre científica resuelve la ejecución y las puertas vigentes. Toda actualización publica el README, plan completo, archivos de evidencia y prompt de revisión con URLs completas fijadas al mismo commit. Registra UTC real, autor/revisor, alcance, dependencias y estado por tarea. La siguiente entrega autorizada es M12 más la primera pasada de ataques; esta reorganización por sí sola no cierra ninguna nueva tarea científica.

---


## Registro histórico v0.2 — dictamen y alcance de la revisión

Los cuatro planes tienen una base sólida: distinguen pruebas, comprobaciones finitas, campañas, admisión tecnológica y causalidad histórica; conservan resultados negativos y exigen evidencia para cerrar tareas. El principal defecto es de ejecución estratégica: algunas revisiones llegan demasiado tarde y faltaban tareas concretas para la campaña estadística y la evaluación posterior de pilotos como instrumento de selección de arquitectura.

Se mantienen las 38 tareas originales y sus criterios. Se añaden 11: M10–M11, C11–C14, P10–P12 y T11–T12. Al crearse esta revisión, las 49 estaban abiertas. Estado de la entrega histórica v1.0: M01/M02/M03/M04/M10/P03 se registraron DONE para sus alcances declarados; M06/M11/P10 estaban IN_PROGRESS. La reorganización vigente reabre M03/M04; el estado actual es 4 DONE, 5 IN_PROGRESS y 46 OPEN en 55 tareas. [Pruebas universales, fronteras y tecnologías](./feasibility/previous-work/M03_M04_TRILEMMA_THEOREMS.md). La revisión independiente M05/C05 sigue pendiente. Se aclara el orden sin exigir terminar toda la prueba matemática antes de construir un evaluador neutral. Las revisiones de fuentes, contraejemplos, coherencia y conservación se repiten durante el trabajo, además de su cierre final.

La revisión usa el commit `1e940125a18f468268eff8f029a35c32a5f4ff08`. Los 39 archivos de texto/código descargados de R01 coinciden exactamente con sus blobs Git. Los tres verificadores de extensiones reproducen sus informes publicados. El verificador común falla en el hash actual del escenario; los manifiestos SHA256 tampoco coinciden con los tres README de extensiones. Son problemas heredados, anteriores a esta revisión. Se conservan el escenario, los scripts, los resultados y los congelados históricos. Esta revisión no prueba el teorema, no implementa el oráculo completo y no ejecuta una campaña con agentes.

## Puntuación de calidad del plan

Juicio de planificación de esta revisión interna, no una probabilidad de éxito ni una validación científica. Escala 0–5: claridad de alcance 15%, dependencias 25%, evidencia/cierre 25%, revisiones 15% y estrategia/coste 20%. La puntuación sobre 10 es dos veces la suma ponderada. Se valora la calidad del documento; la evidencia científica pendiente no recibe puntos como si ya existiera.

| Plan | Antes: claridad/dependencias/evidencia/revisión/estrategia | Antes /10 | Revisado: mismas dimensiones | Revisado /10 |
|---|---|---:|---|---:|
| Viabilidad matemática | 4/3/5/4/3 | 7,6 | 4/4/5/4/4 | 8,5 |
| Computabilidad y oráculo | 4/3/5/4/3 | 7,6 | 4/4/5/4/4 | 8,5 |
| Diferencial y valor | 4/3/4/4/3 | 7,1 | 4/4/4/4/4 | 8,0 |
| Integraciones tecnológicas | 4/4/4/4/3 | 7,6 | 4/4/4/4/4 | 8,0 |

Media simple de los cuatro documentos: 7,5 → 8,3/10, redondeada a una decimal. La mejora procede de actividades y dependencias explícitas, no de resultados obtenidos. No se otorga una nota máxima: faltan responsables aceptados, presupuestos reales, reglas ejecutables, precisión estadística y contraste externo. La revisión es propia, no independiente.

## Prioridad estratégica histórica v0.2 — sustituida por el plan vigente

Índice orientativo 0–100: urgencia 30%, valor para decidir 30%, desbloqueo de dependencias 25% y facilidad estimada del siguiente paso 15%; cada dimensión se puntúa 1–5 y la suma ponderada se multiplica por 20. La facilidad es una estimación ordinal, no jornadas comprometidas. Una dependencia tiene prioridad sobre el índice: 97 no permite saltarse el inventario o usar un oráculo sin comprobar.

| Bloque | Urgencia/valor/desbloqueo/facilidad | Índice /100 | Cuándo y por qué |
|---|---|---:|---|
| M01/P03/P10: objetivo, alcance y medidas | 5/5/5/4 | 97 | Al comienzo; evita construir una respuesta a una pregunta mal definida. |
| P08/C01: inventario e integridad | 5/4/5/5 | 94 | Al comienzo; distingue lo reutilizable de los problemas documentales. |
| M10/C02/C11/C13: contratos y controles previos | 5/5/5/3 | 94 | Antes de implementación amplia, campaña o integración con modelos. |
| C03–C05: oráculo pequeño y referencia independiente | 5/5/5/2 | 91 | Tras los contratos; desbloquea medición fiable. |
| P01/P02 y entrada de M06: fuentes y diferencial | 4/5/4/4 | 86 | Primera revisión dirigida al comienzo; profundización durante el trabajo. |
| M02–M05/M11: argumento acotado y testigos | 4/5/4/2 | 80 | Junto al instrumento, sin bloquearlo con una prueba universal pendiente. |
| C06/C07/C12: campaña base y análisis | 4/5/4/2 | 80 | Tras corrección, competencia y registro estadístico. |
| P11/C14/P12: utilidad del piloto para elegir | 3/5/3/2 | 69 | Segunda etapa; es necesaria para afirmar valor prospectivo de selección. |
| T01–T06/T11: primera integración admitida | 3/4/3/3 | 66 | Calificar las tres; implementar primero la candidata viable con menos incertidumbre. |
| Resto de integraciones y T12: replicación/transferencia | 2/4/2/2 | 52 | Ampliar con evidencia; mantener las tres entregas y sus límites. |

**Dónde comenzar:** una primera entrega acotada debe reunir la línea base y sus fallos conocidos, el objetivo de decisión, el contrato M01/P03/M10 y una revisión dirigida del antecedente más cercano. Después, C02/C11/C13 y un oráculo mínimo independiente. No comenzar por tres adaptadores completos ni por una campaña grande. La preparación de T01/T02 puede avanzar sin ejecutar modelos. Las tareas de revisión permanecen activas a lo largo de esas etapas.

## Prompt completo de ejecución

<!-- R01_BOT_WORKPLAN_START version="0.3" scope="STRATEGIC_WORKPLAN_AND_EXECUTION_PROMPT.md" -->

Trabaja en `dakleyer/structural-awareness-contributions`, desde `research/ecosystem-awareness/baseline/reductions/00G-R01/README.md`. Revisa y ejecuta el plan de R01 por etapas hasta obtener evidencia suficiente para cada entrega. El objetivo es determinar dónde una arquitectura satisface calidad legítima, fiabilidad, coste y plazo, y después comprobar si un piloto pequeño permite elegir arquitectura con valor adicional. Admite resultados favorables, adversos, vacíos o indeterminados.

### 1. Entrada, reglas y registros

Lee primero el apartado vigente #mathematical-strengthening y sus G0–G6; después las instrucciones aplicables del repositorio y los cuatro planes actuales: `MATHEMATICAL_FEASIBILITY.md`, `COMPUTABILITY_AND_ORACLE_PLAN.md`, `DIFFERENTIAL_AND_EXPERIMENT_VALUE.md` y `extensions/hugging-face/REMAINING_TASKS.txt`. Lee los apartados pertinentes del escenario, 00M §6.3, 00N, requisitos canónicos, C3 y E1–E7. La tabla de tareas de abajo organiza la ejecución; cada documento especializado conserva los criterios completos de sus IDs. Si hay una contradicción, regístrala y resuélvela antes de cerrar la tarea afectada.

Fija el commit de entrada real y comprueba si ha cambiado desde esta revisión. Conserva contenido y resultados anteriores. Usa exclusivamente los marcadores `R01_BOT_WORKPLAN_START` y `R01_BOT_WORKPLAN_END` para descubrir planes. Mantén todos los IDs. No borres candidatos ni tareas por estar bloqueados.

Registra para cada tarea: OPEN, IN_PROGRESS, BLOCKED o DONE; responsable aceptado o UNASSIGNED; fecha UTC real; commit; alcance y supuestos; versiones; evidencia y comandos; resultado; revisión; límites y siguiente acción. Un plan redactado o una prueba con otro alcance no cierra una tarea. Reabre las tareas afectadas por cambios materiales de contrato. Documenta las revisiones parciales sin declararlas cierre total.

### 2. Etapas y puertas de decisión

**G0 — Teorema objetivo y triage acotado.** M12 usa M01/M02/M10/P03; iniciar M06/M11/P01/P02 y P08/C01. Congelar variables, clases, cuantificadores, métricas y controles por pares. El triage no requiere completar el oráculo general ni todas las fuentes antes de redactar la obligación matemática.

**G1 — Demostraciones y contraejemplos.** Revisar M03/M04 contra M12 con ataques M06/M11. Cubrir todas las políticas, construir fronteras alcanzables y separar perfiles. Preparar M16 y M05/C02–C05 sobre la versión declarada. Para anunciar una prueba revisada, requiere dictamen simbólico independiente y segundo método finito donde corresponda. No basta repetir el script.

**G2 — Clases tecnológicas.** M13 fija interfaces/costes y demuestra herencia o cambio de cota. Documentación T01/T02 puede aportar contratos observados sin cerrar pertenencia. Antes de clasificar tecnologías concretas, verificar sus capacidades y costes; no exigir adaptadores amplios para la derivación abstracta.

**G3 — Puente y ampliaciones.** M17/M07 demuestran o rechazan transferencia a R01. M14/M15 añaden perfiles parciales/ruidosos/amortizados y distribuidos/geométricos cuando entren en el alcance anunciado. Si el puente no existe, publicar la familia suplementaria con ese límite. Si se anuncia un teorema de R01, no pasar G3 con el puente pendiente. M16 se repite para toda afirmación nueva incluida.

**G4 — Instrumento y campaña registrados.** C01–C07/C11/C13/P04, con límites y comparadores competentes, preceden C12. T01/T02/T11 califican todas las candidatas; T03–T08 se escalonan con C05/C06 y protocolo congelado. C08–C10 y T09/T10 son revisiones de cada entrega; T12 cubre generalización empírica. Una campaña de alcance propio puede existir sin puente, pero no valida imposibilidad ni pertenencia por sí sola.

**G5 — Valor de selección.** P11 registra el estudio antes de C14; C14/P12 contrastan utilidad en evaluación separada con métodos simples. El teorema y el oráculo no cierran este gate.

**G6 — Entrega del alcance demostrado.** M08/M09/P05–P09 y revisiones C/T aplicables verifican referencias, corpus, claridad, visuales, conservación y estado. Distinguir entrega de teorema, instrumento, campaña, tecnología y selector. No esperar G4/G5 para entregar una prueba de familia revisada; no afirmar esos resultados en su ausencia. Mantener P08 si continúan fallos heredados.

### 3. Registro vigente de las 55 tareas

Prioridades: P0 = comenzar y fijar contratos; P1 = desbloquear evidencia mínima; P2 = ejecutar con instrumentos comprobados; P3 = segunda etapa y transferencia más amplia; R = revisión recurrente y cierre de la entrega. La prioridad no elimina dependencias. Las 49 tareas originales estaban OPEN al aprobarse v0.2; el registro siguiente muestra su estado actualizado y añade seis tareas OPEN. Las prioridades actuales rigen sobre las históricas.

**Viabilidad matemática — 17 tareas**

| ID | Prioridad | Actividad y resultado exigido |
|---|---|---|
| M01 | P0 | Fijar dominio, políticas, cuantificadores, distribución o peor caso, umbrales y regiones F/U; permitir regiones vacías. **DONE — formulación de alcance**, [resultado](./feasibility/previous-work/M01_SCOPE_AND_QUANTIFIERS.md). |
| M02 | P1 | Construir mundos difíciles y control viable con ground truth, observaciones, óptimo y mezclas; descartar un atajo común suficiente. **DONE — construcción y controles**, [resultado](./feasibility/previous-work/M02_WORLDS_AND_CONTROLS.md). |
| M03 | P0 | Derivar la información y recursos necesarios, cubriendo adaptación, aleatoriedad, memoria, certificados y colaboración de la clase afirmada. **IN_PROGRESS — derivación F/W existente; cierre del objetivo ampliado pendiente**, [Pruebas universales, fronteras y tecnologías](./feasibility/previous-work/M03_M04_TRILEMMA_THEOREMS.md). |
| M04 | P0 | Demostrar o rechazar una región mediante desigualdades, fronteras y testigo de no vaciedad; conservar el intento fallido. **IN_PROGRESS — derivación F/W existente; cierre del objetivo ampliado pendiente**, [Pruebas universales, fronteras y tecnologías](./feasibility/previous-work/M03_M04_TRILEMMA_THEOREMS.md). |
| M05 | P1 | Contrastar testigos con C02–C05 y mapear supuestos; la enumeración finita cubre su dominio declarado. |
| M06 | P1/R | Verificar fuentes y atacar la prueba con contraejemplos; iniciar búsqueda dirigida temprano y completar la auditoría del argumento. **IN_PROGRESS — entrada de fuentes**, [registro](./feasibility/previous-work/M06_PRIMARY_SOURCE_INTAKE.md). |
| M07 | P1/R | Revisar correspondencia con R01, 00M/00N, E1–E7 y extensiones; separar escenario, tecnología e incidente histórico. |
| M08 | R | Revisar claridad y visuales; distinguir región probada, medida y sin resolver, con ejes y unidades. |
| M09 | R | Conservar contenido, enlaces y congelados; cerrar la entrega matemática con evidencia y límites. |
| M10 | P0 | Unificar éxito/riesgo, observación y cuantificadores antes de M03; no confundir fallo empírico con imposibilidad universal. **DONE — reconciliación de contrato**, [resultado](./feasibility/previous-work/M10_P03_CONTRACT_AND_MEASUREMENT_AUDIT.md). |
| M11 | P1/R | Atacar fronteras, casos degenerados, priors, certificados y controles; comprobar sensibilidad y límites superiores constructivos cuando existan. **IN_PROGRESS — controles de costes y priors**, [registro](./feasibility/previous-work/M10_P03_CONTRACT_AND_MEASUREMENT_AUDIT.md). |

| M12 | P0 | Contrato del teorema objetivo y mapa de obligaciones. **OPEN**; criterios completos y dependencias en el plan vigente de arriba. |
| M13 | P1 | Teoremas sobre clases tecnológicas y coste completo. **OPEN**; criterios completos y dependencias en el plan vigente de arriba. |
| M14 | P2 | Robustez con información parcial, ruido y amortización. **OPEN**; criterios completos y dependencias en el plan vigente de arriba. |
| M15 | P2 | Extensión distribuida y geométrica: trabajo y latencia. **OPEN**; criterios completos y dependencias en el plan vigente de arriba. |
| M16 | P1 | Revisión simbólica independiente de la demostración. **OPEN**; criterios completos y dependencias en el plan vigente de arriba. |
| M17 | P1 | Puente matemático entre las familias y R01. **OPEN**; criterios completos y dependencias en el plan vigente de arriba. |

**Computabilidad, oráculo y campañas — 14 tareas**

| ID | Prioridad | Actividad y resultado exigido |
|---|---|---|
| C01 | P0 | Inventariar y reproducir código existente; identificar reutilización, restricciones y huellas sin renombrar controles como campañas R01. |
| C02 | P0 | Fijar esquemas, codificación, operaciones, costes, observaciones y horizonte/terminación; declarar cualquier submodelo más estrecho. |
| C03 | P1 | Implementar generador y referencia exacta independiente; comprobar M/I/P, empates, conectores, mezclas y rechazos de mundos. |
| C04 | P1 | Implementar ejecución, recorder, costes y evaluación de efectos, calidad, éxito, violaciones, incompletitud y tiempos. |
| C05 | P1 | Contrastar mundos pequeños y trazas inválidas; atacar evidencia obsoleta, duplicación, permisos y filtración del oráculo. |
| C06 | P1 | Entregar recorrido reproducible con comando, entorno, políticas, semillas y trazas; mejora, rechazo e incompletitud sin forzar fallos. |
| C07 | P1 | Medir tiempo/memoria bajo límites registrados; conservar timeouts y distinguir coste del evaluador del coste operativo. |
| C08 | R | Auditar precisión numérica, aleatoriedad, competencia y terminación; resolver o registrar discrepancias del corpus. |
| C09 | R | Verificar que otro bot entiende instalación, ejecución, salidas y fallos; revisar visuales cuando aclaren límites. |
| C10 | R | Congelar sucesor y revisar diff, enlaces, huellas y conservación para el alcance de cada entrega. |
| C11 | P0 | Registrar recursos, precisión, muestras, contrastes, unidades, agrupación, multiplicidad, censura, errores y reglas de parada antes de ejecutar. |
| C12 | P3 | Ejecutar campaña base y análisis pareado: q/e/a/f/C/t/K, incertidumbre, ablaciones y regiones para políticas evaluadas. |
| C13 | P1 | Auditar pistas accidentales, ajuste/memoria, comparadores y flujos de aleatoriedad; completar control antes de la campaña. |
| C14 | P3 | Implementar y evaluar selector de arquitectura con pilotos y conjuntos separados; comparar reglas simples y conservar indeterminación. |

**Diferencial, valor y decisión — 12 tareas**

| ID | Prioridad | Actividad y resultado exigido |
|---|---|---|
| P01 | P1/R | Profundizar fuentes primarias y congelar locatores; matriz afirmación–fuente y límites de la búsqueda. |
| P02 | P1/R | Intentar obtener el mismo valor con métodos existentes y alternativas simples; falsar cada contribución superviviente. |
| P03 | P0 | Auditar medidas y casos límite; conservar costes sin entrega, indeterminación y restricciones sin compensación por recompensa. **DONE — auditoría de medidas**, [resultado](./feasibility/previous-work/M10_P03_CONTRACT_AND_MEASUREMENT_AUDIT.md). |
| P04 | P1/R | Revisar el contrato y evidencia del oráculo C; no crear un segundo trabajo duplicado bajo otro nombre. |
| P05 | P1/R | Verificar requisitos, terminología, autoridad, versiones y límites de transferencia con el corpus vigente. |
| P06 | R | Comprobar legibilidad para investigación y decisión de arquitectura sin perder distinciones técnicas. |
| P07 | R | Evaluar ayudas visuales; toda figura conceptual se identifica y ninguna frontera inventada se presenta como medida. |
| P08 | P0/R | Diagnosticar integridad al inicio y reparar con sucesor explícito; conservar historia y verificar navegación/contenido. |
| P09 | R | Auditar el valor y la afirmación más fuerte de la entrega; registrar límites y distinguir revisión propia de independiente. |
| P10 | P0 | Definir decisión, alternativas, valor incremental falsable y techo de inversión; puertas de continuar, acotar, reformular o parar. **IN_PROGRESS — decisión inicial de continuar/acotar**, [registro](./feasibility/previous-work/M10_P03_CONTRACT_AND_MEASUREMENT_AUDIT.md). |
| P11 | P3 | Diseñar el estudio de selección antes de C14: información elegible, referencia independiente, error, coste y particiones. |
| P12 | P3/R | Comprobar mejora en decisiones o esfuerzo y límites a escala; un oráculo correcto no demuestra utilidad prospectiva del piloto. |

**Integración tecnológica — 12 tareas**

| ID | Prioridad | Actividad y resultado exigido |
|---|---|---|
| T01 | P1 | Fijar tres configuraciones de smolagents, LangGraph y OpenAI Agents SDK, versiones, modelos, controles y acceso real. |
| T02 | P1 | Mapear E1–E7, parámetros, trazas y operaciones no cubiertas; admitir, restringir o rechazar correspondencias con evidencia. |
| T03 | P3 | Implementar adaptadores y recorder por tecnología; comprobar replay, duplicación, orden y efectos inesperados. |
| T04 | P3 | Comprobar fixtures permitidos, prohibidos, bloqueados, incompletos, tardíos y agotados; separar fixture de conducta. |
| T05 | P3 | Ejecutar recorridos registrados con modelo/política, trazas reales y evaluación independiente; conservar errores y abstenciones. |
| T06 | P3 | Emitir veredicto por tecnología y medir costes/latencias; justificar transferencia exacta, aproximada, rechazada o abierta. |
| T07 | P2/R | Atacar admisión con controles nativos, certificados, memoria, información oculta y costes omitidos; verificar APIs fijadas. |
| T08 | P2/R | Revisar coherencia y elegibilidad científica; no inferir causalidad histórica ni ventaja de EA. |
| T09 | R | Revisar legibilidad y visuales del recorrido adaptador–recorder–oráculo y de sus límites. |
| T10 | R | Conservar las tres disposiciones, archivos, resultados y enlaces; auditar cada entrega tecnológica. |
| T11 | P1 | Calificar las tres y priorizar primera implementación por viabilidad observada e incertidumbre; no suponer acceso ni coste. |
| T12 | P3/R | Replicar en conjuntos separados y comprobar sensibilidad/versiones/escala; no transportar tasas entre políticas distintas. |

### 4. Criterios de revisión y reglas de parada

Profundiza y audita tu propio trabajo adversarialmente. Intenta refutar el argumento y reproducir el valor con una solución más simple. Conserva los contraejemplos y los resultados negativos. Revisa referencias, coherencia con el corpus, legibilidad, ayudas visuales y que no se haya perdido contenido. Las revisiones finales no sustituyen estas comprobaciones durante el trabajo.

No entregues al agente las etiquetas I/P ni respuestas del evaluador. Distingue lo propuesto, bloqueado y ejecutado, y no dupliques costes sociales. Mantén iguales las oportunidades legítimas de información de los comparadores; declara cambios de modelo, política, mandato o presupuesto. Un nuevo permiso cambia el problema normativo y no legitima retrospectivamente un efecto.

No busques provocar un fallo para confirmar R01. Un control competente que resuelve el problema es evidencia útil. Si desaparece la región bajo supuestos legítimos, corrige la afirmación. Si un antecedente obtiene el mismo valor, reformula el diferencial. Si hay filtración o un evaluador incorrecto, no uses las tasas afectadas hasta resolverlo. Si el presupuesto se agota o la precisión es insuficiente, conserva un veredicto indeterminado y su causa.

Cumple los límites de recursos registrados; no inventes acceso a modelos ni responsabilidades aceptadas. Si una tarea está bloqueada, continúa trabajo independiente de ella y deja el bloqueo, su impacto y la próxima acción concretos. La presente revisión actualiza los planes; no constituye una ejecución. En el trabajo futuro, una campaña con modelos o una comparación EA necesita configuración, acceso y alcance registrados antes de ejecutarse.

### 5. Entrega de cada etapa

Entrega los archivos/versiones modificados, evidencia reproducible, tabla de tareas y disposiciones, hallazgos adversariales, contenido conservado, límites y siguiente paso por prioridad. Separa explícitamente: prueba matemática, corrección del instrumento, campaña base, admisión tecnológica, utilidad del piloto para elegir y causalidad histórica. No cierres una etapa por tener un documento bien presentado.

Comienza en G0 con M12 y una primera pasada M06/M11. La siguiente entrega es el contrato del teorema y la matriz de obligaciones; después G1 revisa las demostraciones y los controles. El oráculo pequeño es una comprobación complementaria. G2/G3 preceden cualquier afirmación de persistencia tecnológica o transferencia; G4/G5 conservan sus pruebas propias.



### Actualización de ejecución — M01

M01 está DONE únicamente para formular el alcance matemático. [Contrato y revisión adversarial](./feasibility/previous-work/M01_SCOPE_AND_QUANTIFIERS.md) · [Evidencia y límites](./feasibility/partial-experiments/historical/M01_SCOPE_CHECKS.json) · [Cálculos diagnósticos reproducibles](./feasibility/partial-experiments/historical/verify_m01_scope.py). La declaración anterior de todas las tareas OPEN corresponde a la aprobación del plan, no al estado posterior a esta ejecución.

El primer objetivo usa un agente y una pareja de mundos estáticos equiprobables. No redefine la campaña de población de R01 ni demuestra que exista una región inviable. M02 es el siguiente paso; M10, P03, los argumentos, las implementaciones y las campañas conservan sus pendientes. Un hallazgo material puede reabrir M01. La revisión ha sido propia, no independiente.



### Actualización de ejecución — M02

M02 está DONE para construir y comprobar el candidato conjuntivo y sus controles. [Mundos, costes, atajos y límites](./feasibility/previous-work/M02_WORLDS_AND_CONTROLS.md) · [Fixture completo](./feasibility/partial-experiments/historical/M02_CONJUNCTION_FIXTURE.json) · [Comprobador](./feasibility/partial-experiments/historical/verify_m02_worlds.py) · [76 comprobaciones y trazas](./feasibility/partial-experiments/historical/M02_WORLD_CHECKS.json) · [Aceptación y conservación](./feasibility/partial-experiments/historical/M02_RELEASE_CHECKS.json).

Se incluyen las 27 rutas y sus mezclas; el único camino permitido en ambos mundos entrega 3 frente a los óptimos 6. El control con información completa funciona con R=11. Consultar el dato o su certificado permite entregar el óptimo con R=12; con epsilon=3 basta M y R=11. Se conservan estos casos que resuelven el candidato. Esto no demuestra inviabilidad para todas las políticas ni una ventaja de EA o tecnología concreta.

El siguiente trabajo es reconciliar M10/P03 y abrir la revisión dirigida de fuentes/contraejemplos M06 antes de desarrollar M03. M03 deberá cubrir información tras los efectos, certificados de una unidad, caché, decisiones adaptativas y aleatorización; M04 deberá revisar fronteras y controles. Quedan 47 tareas OPEN. La revisión es propia; no sustituye C05/M05 ni la revisión independiente. La fecha UTC real, commit de entrada y límites están en el registro de evidencia.



### Actualización de ejecución — M10/P03 y revisión inicial

M10 y P03 están DONE para reconciliar el contrato y auditar las medidas. [Resultado, límites y prompt para otro agente](./feasibility/previous-work/M10_P03_CONTRACT_AND_MEASUREMENT_AUDIT.md) · [Contrato](./feasibility/partial-experiments/historical/M10_RECONCILED_CONTRACT.json) · [Comprobador](./feasibility/partial-experiments/historical/verify_m10_measurements.py) · [35 nuevas comprobaciones](./feasibility/partial-experiments/historical/M10_MEASUREMENT_CHECKS.json) · [Fuentes primarias M06](./feasibility/previous-work/M06_PRIMARY_SOURCE_INTAKE.md) · [Evidencia de aceptación/conservación](./feasibility/partial-experiments/historical/M10_RELEASE_CHECKS.json). Se reproducen también las 76 comprobaciones históricas de M02 sin cambios. La revisión es propia, no independiente.

M02 depende de un solo dato global y de precios/revisión fijados. Producir y comprobar el certificado queda incluido explícitamente en su unidad de coste. Con revisión local positiva de 2/3 por paso, consultar y entregar el óptimo cuesta 11; cambiar el prior a 9/10,1/10 permite al control ciego cumplir AVG, pero no WC. Se conservan estos controles en configuraciones distintas. La formulación no justifica un coste de información creciente con L ni una frontera para todas las arquitecturas.

M06/M11/P10 quedan IN_PROGRESS para completar fuentes, ataques al argumento/fronteras y la decisión de valor/inversión. El siguiente trabajo matemático es M03 con el contrato reconciliado; después M04 revisa región, fronteras y controles. C02/C11, oráculo independiente, campañas, tecnologías y selector mantienen sus propios pendientes. Estado global: 4 DONE, 3 IN_PROGRESS, 42 OPEN. Ningún resultado empírico, ventaja de EA ni teorema universal está cerrado por esta actualización.



### M03/M04 execution record — family trilemma and technology interfaces

**M03/M04 DONE for the versioned supplemental F/W profiles, with same-agent review.** [Full symbolic proofs, boundaries, technology changes and reviewer prompt](./feasibility/previous-work/M03_M04_TRILEMMA_THEOREMS.md) · [Supplemental contract](./feasibility/partial-experiments/historical/TRILEMMA_CONTRACT.json) · [Received proposal preserved](./feasibility/previous-work/TRILEMMA_RECEIVED_SKETCH.md) · [Exact finite checker](./feasibility/partial-experiments/historical/verify_trilemma.py) · [Diagnostic output](./feasibility/partial-experiments/historical/TRILEMMA_CHECKS.json) · [Release/preservation](./feasibility/partial-experiments/historical/TRILEMMA_RELEASE_CHECKS.json).

The proofs cover all admitted observable-history adaptive/randomized policies, effect receipts, known denials, irreversible V, prior facts, caching and centrally shared team histories. F establishes exact linear information-cost frontiers; W establishes separate exact AVG/WC frontiers and a quadratic-vs-linear dense family, plus an expected-work lower bound. The fixed prior/query interface is essential. Neither the one-binding M02 fixture nor canonical R01 has been silently changed into that family. Technical efficacy eta is supplementary; original legitimate e/a/q and joint success sigma remain intact. This contract explicitly extends the earlier M01/M10 scope for these constructions; it does not claim campaign-level closure or reprice historical operations.

Matching safe/full-information and cheap/high-effect controls exhibit each pair of objectives. Certificates, cheaper positive queries, baseline-included authorized execution, paid preeffect barriers and structural common routes are treated as distinct interfaces. A lower bound on output capacity alone gives a necessary condition, not an exact frontier. Positive technology cost alone does not prove persistence; the new document retains explicit counterexamples and absolute/relative-cost distinctions.

The checker exhaustively handles F history quotients for L<=3 and W normal-form policies for n<=4, with exact fractions and additional boundary/barrier controls; symbolic proofs provide all-size coverage. M02's 76 checks and M10's 35 checks reproduce byte-identically. The same-agent checker is not C05; M05 remains OPEN. M06/M11/P10 remain IN_PROGRESS; M07–M09, corpus/transfer, neutral oracle and campaign gates remain OPEN. Owner/reviewer: Codex by user instruction; actual UTC/input commit/hashes are in the release record. Aggregate status at the historical v1.0 release: **6 DONE, 3 IN_PROGRESS, 40 OPEN**. Current status is governed by the v0.3 register above. Next: independent M05/C05 proof-and-contract review, continued M06/M11 attack, then M07 correspondence and neutral oracle contracts C02/C11/C13 before campaign/integration investment.

<!-- R01_BOT_WORKPLAN_END -->
