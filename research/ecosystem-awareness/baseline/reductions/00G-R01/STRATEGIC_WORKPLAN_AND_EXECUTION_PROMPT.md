# R01 — Revisión estratégica y prompt completo de ejecución

Iván Abril Palma, Tegrity.AI · Revisión del plan v0.2 · 3 de octubre de 2026

[README de R01](./README.md#bot-start-here) · [Viabilidad matemática](./MATHEMATICAL_FEASIBILITY.md) · [Computabilidad y oráculo](./COMPUTABILITY_AND_ORACLE_PLAN.md) · [Diferencial y valor](./DIFFERENTIAL_AND_EXPERIMENT_VALUE.md) · [Integraciones](./extensions/hugging-face/REMAINING_TASKS.txt) · [Evidencia de esta revisión](./WORKPLAN_REVIEW_EVIDENCE_2026-10-03.json)

## Dictamen y alcance de la revisión

Los cuatro planes tienen una base sólida: distinguen pruebas, comprobaciones finitas, campañas, admisión tecnológica y causalidad histórica; conservan resultados negativos y exigen evidencia para cerrar tareas. El principal defecto es de ejecución estratégica: algunas revisiones llegan demasiado tarde y faltaban tareas concretas para la campaña estadística y la evaluación posterior de pilotos como instrumento de selección de arquitectura.

Se mantienen las 38 tareas originales y sus criterios. Se añaden 11: M10–M11, C11–C14, P10–P12 y T11–T12. Al crearse esta revisión, las 49 estaban abiertas. Estado actual: M01/M02/M03/M04/M10/P03 están DONE para sus alcances declarados (M03/M04: perfiles suplementarios F/W); M06/M11/P10 están IN_PROGRESS y quedan 40 tareas OPEN. [Pruebas universales, fronteras y tecnologías](./M03_M04_TRILEMMA_THEOREMS.md). La revisión independiente M05/C05 sigue pendiente. Se aclara el orden sin exigir terminar toda la prueba matemática antes de construir un evaluador neutral. Las revisiones de fuentes, contraejemplos, coherencia y conservación se repiten durante el trabajo, además de su cierre final.

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

## Prioridad estratégica y orden real

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

<!-- R01_BOT_WORKPLAN_START version="0.2" scope="STRATEGIC_WORKPLAN_AND_EXECUTION_PROMPT.md" -->

Trabaja en `dakleyer/structural-awareness-contributions`, desde `research/ecosystem-awareness/baseline/reductions/00G-R01/README.md`. Revisa y ejecuta el plan de R01 por etapas hasta obtener evidencia suficiente para cada entrega. El objetivo es determinar dónde una arquitectura satisface calidad legítima, fiabilidad, coste y plazo, y después comprobar si un piloto pequeño permite elegir arquitectura con valor adicional. Admite resultados favorables, adversos, vacíos o indeterminados.

### 1. Entrada, reglas y registros

Lee las instrucciones aplicables del repositorio y los cuatro planes actuales: `MATHEMATICAL_FEASIBILITY.md`, `COMPUTABILITY_AND_ORACLE_PLAN.md`, `DIFFERENTIAL_AND_EXPERIMENT_VALUE.md` y `extensions/hugging-face/REMAINING_TASKS.txt`. Lee los apartados pertinentes del escenario, 00M §6.3, 00N, requisitos canónicos, C3 y E1–E7. La tabla de tareas de abajo organiza la ejecución; cada documento especializado conserva los criterios completos de sus IDs. Si hay una contradicción, regístrala y resuélvela antes de cerrar la tarea afectada.

Fija el commit de entrada real y comprueba si ha cambiado desde esta revisión. Conserva contenido y resultados anteriores. Usa exclusivamente los marcadores `R01_BOT_WORKPLAN_START` y `R01_BOT_WORKPLAN_END` para descubrir planes. Mantén todos los IDs. No borres candidatos ni tareas por estar bloqueados.

Registra para cada tarea: OPEN, IN_PROGRESS, BLOCKED o DONE; responsable aceptado o UNASSIGNED; fecha UTC real; commit; alcance y supuestos; versiones; evidencia y comandos; resultado; revisión; límites y siguiente acción. Un plan redactado o una prueba con otro alcance no cierra una tarea. Reabre las tareas afectadas por cambios materiales de contrato. Documenta las revisiones parciales sin declararlas cierre total.

### 2. Etapas y puertas de decisión

**G0 — Línea base y pregunta.** Empieza por P08/C01 y M01/P03/P10; realiza una revisión dirigida inicial P01/P02/M06. Reproduce comprobaciones existentes, separa fallos de código, informes e integridad documental y define la decisión que buscamos informar. No sobreescribas congelados históricos. Si un fallo impide verificar una evidencia, esa evidencia queda sin comprobar; un fallo documental acotado no bloquea automáticamente trabajo neutral con una línea base explícita.

**G1 — Contratos y oráculo mínimo.** Fija M10/C02/C11 y los requisitos iniciales C13. Construye C03/C04 y comprueba C05 con una referencia implementada de forma independiente. Trabaja M02–M04/M06/M11 en paralelo lógico, dentro de sus dependencias. G1 requiere testigos permitidos, prohibidos, bloqueados e incompletos, óptimo con mezclas/conectores y costes completos. Una referencia desconocida por timeout conserva UNKNOWN, sin convertirse en fallo del agente.

**G2 — Primera campaña base.** Tras C05–C07/C11/C13 y P03/P04, ejecuta C12 con políticas competentes y registro previo. Fija precisión, unidad independiente, semillas, contrastes, criterios de exclusión/reintento y límites de recursos antes de observar resultados. Publica lo medido para esas políticas y tamaños. No conviertas su fracaso en imposibilidad para todas las políticas.

**G3 — Tecnología concreta.** Califica las tres candidatas mediante T01/T02/T11. Elige la primera implementación por evidencia de acceso, control, trazabilidad y coste; conserva el orden y estado de las otras dos. Ejecuta T03–T08 por tecnología con el evaluador comprobado. Transferencia de un teorema exige sus obligaciones; una ejecución útil puede publicarse con alcance propio cuando la transferencia siga abierta. No presentes fixtures como comportamiento autónomo.

**G4 — Piloto para elegir arquitectura.** Especifica P11; después de C12, ejecuta C14 y revisa P12. Usa solamente observaciones elegibles del piloto, separa ajuste y evaluación y compara selectores más simples. Mide recomendaciones erróneas, oportunidades perdidas, indeterminación, cobertura y coste diagnóstico. Si falta precisión o correspondencia a escala, conserva el resultado indeterminado.

**G5 — Revisión y entrega del alcance anunciado.** Repite las revisiones de coherencia, legibilidad, ayudas visuales, conservación y adversariales en cada entrega. Una entrega del instrumento puede salir con la campaña y G4 pendientes, explícitamente. Una entrega de campaña necesita G2; una afirmación prospectiva de selección necesita G4. No afirmes integridad completa mientras P08 conserve fallos aplicables. No describas revisión propia como independiente.

### 3. Registro completo de las 49 tareas

Prioridades: P0 = comenzar y fijar contratos; P1 = desbloquear evidencia mínima; P2 = ejecutar con instrumentos comprobados; P3 = segunda etapa y transferencia más amplia; R = revisión recurrente y cierre de la entrega. La prioridad no elimina dependencias. Todas las tareas siguientes están OPEN al aprobarse esta revisión documental.

**Viabilidad matemática — 11 tareas**

| ID | Prioridad | Actividad y resultado exigido |
|---|---|---|
| M01 | P0 | Fijar dominio, políticas, cuantificadores, distribución o peor caso, umbrales y regiones F/U; permitir regiones vacías. **DONE — formulación de alcance**, [resultado](./M01_SCOPE_AND_QUANTIFIERS.md). |
| M02 | P1 | Construir mundos difíciles y control viable con ground truth, observaciones, óptimo y mezclas; descartar un atajo común suficiente. **DONE — construcción y controles**, [resultado](./M02_WORLDS_AND_CONTROLS.md). |
| M03 | P1 | Derivar la información y recursos necesarios, cubriendo adaptación, aleatoriedad, memoria, certificados y colaboración de la clase afirmada. **DONE — perfiles F/W**, [Pruebas universales, fronteras y tecnologías](./M03_M04_TRILEMMA_THEOREMS.md). |
| M04 | P1 | Demostrar o rechazar una región mediante desigualdades, fronteras y testigo de no vaciedad; conservar el intento fallido. **DONE — perfiles F/W**, [Pruebas universales, fronteras y tecnologías](./M03_M04_TRILEMMA_THEOREMS.md). |
| M05 | P1 | Contrastar testigos con C02–C05 y mapear supuestos; la enumeración finita cubre su dominio declarado. |
| M06 | P1/R | Verificar fuentes y atacar la prueba con contraejemplos; iniciar búsqueda dirigida temprano y completar la auditoría del argumento. **IN_PROGRESS — entrada de fuentes**, [registro](./M06_PRIMARY_SOURCE_INTAKE.md). |
| M07 | R | Revisar correspondencia con R01, 00M/00N, E1–E7 y extensiones; separar escenario, tecnología e incidente histórico. |
| M08 | R | Revisar claridad y visuales; distinguir región probada, medida y sin resolver, con ejes y unidades. |
| M09 | R | Conservar contenido, enlaces y congelados; cerrar la entrega matemática con evidencia y límites. |
| M10 | P0 | Unificar éxito/riesgo, observación y cuantificadores antes de M03; no confundir fallo empírico con imposibilidad universal. **DONE — reconciliación de contrato**, [resultado](./M10_P03_CONTRACT_AND_MEASUREMENT_AUDIT.md). |
| M11 | P1/R | Atacar fronteras, casos degenerados, priors, certificados y controles; comprobar sensibilidad y límites superiores constructivos cuando existan. **IN_PROGRESS — controles de costes y priors**, [registro](./M10_P03_CONTRACT_AND_MEASUREMENT_AUDIT.md). |

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
| C12 | P2 | Ejecutar campaña base y análisis pareado: q/e/a/f/C/t/K, incertidumbre, ablaciones y regiones para políticas evaluadas. |
| C13 | P1 | Auditar pistas accidentales, ajuste/memoria, comparadores y flujos de aleatoriedad; completar control antes de la campaña. |
| C14 | P3 | Implementar y evaluar selector de arquitectura con pilotos y conjuntos separados; comparar reglas simples y conservar indeterminación. |

**Diferencial, valor y decisión — 12 tareas**

| ID | Prioridad | Actividad y resultado exigido |
|---|---|---|
| P01 | P1/R | Profundizar fuentes primarias y congelar locatores; matriz afirmación–fuente y límites de la búsqueda. |
| P02 | P1/R | Intentar obtener el mismo valor con métodos existentes y alternativas simples; falsar cada contribución superviviente. |
| P03 | P0 | Auditar medidas y casos límite; conservar costes sin entrega, indeterminación y restricciones sin compensación por recompensa. **DONE — auditoría de medidas**, [resultado](./M10_P03_CONTRACT_AND_MEASUREMENT_AUDIT.md). |
| P04 | P1/R | Revisar el contrato y evidencia del oráculo C; no crear un segundo trabajo duplicado bajo otro nombre. |
| P05 | P1/R | Verificar requisitos, terminología, autoridad, versiones y límites de transferencia con el corpus vigente. |
| P06 | R | Comprobar legibilidad para investigación y decisión de arquitectura sin perder distinciones técnicas. |
| P07 | R | Evaluar ayudas visuales; toda figura conceptual se identifica y ninguna frontera inventada se presenta como medida. |
| P08 | P0/R | Diagnosticar integridad al inicio y reparar con sucesor explícito; conservar historia y verificar navegación/contenido. |
| P09 | R | Auditar el valor y la afirmación más fuerte de la entrega; registrar límites y distinguir revisión propia de independiente. |
| P10 | P0 | Definir decisión, alternativas, valor incremental falsable y techo de inversión; puertas de continuar, acotar, reformular o parar. **IN_PROGRESS — decisión inicial de continuar/acotar**, [registro](./M10_P03_CONTRACT_AND_MEASUREMENT_AUDIT.md). |
| P11 | P3 | Diseñar el estudio de selección antes de C14: información elegible, referencia independiente, error, coste y particiones. |
| P12 | P3/R | Comprobar mejora en decisiones o esfuerzo y límites a escala; un oráculo correcto no demuestra utilidad prospectiva del piloto. |

**Integración tecnológica — 12 tareas**

| ID | Prioridad | Actividad y resultado exigido |
|---|---|---|
| T01 | P1 | Fijar tres configuraciones de smolagents, LangGraph y OpenAI Agents SDK, versiones, modelos, controles y acceso real. |
| T02 | P1 | Mapear E1–E7, parámetros, trazas y operaciones no cubiertas; admitir, restringir o rechazar correspondencias con evidencia. |
| T03 | P2 | Implementar adaptadores y recorder por tecnología; comprobar replay, duplicación, orden y efectos inesperados. |
| T04 | P2 | Comprobar fixtures permitidos, prohibidos, bloqueados, incompletos, tardíos y agotados; separar fixture de conducta. |
| T05 | P2 | Ejecutar recorridos registrados con modelo/política, trazas reales y evaluación independiente; conservar errores y abstenciones. |
| T06 | P2 | Emitir veredicto por tecnología y medir costes/latencias; justificar transferencia exacta, aproximada, rechazada o abierta. |
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

Comienza en G0. La primera entrega es una línea base verificable, una pregunta precisa y contratos medibles. La segunda es un oráculo pequeño independiente. La campaña, las integraciones y la selección prospectiva se apoyan en esas entregas y conservan sus propias pruebas pendientes.



### Actualización de ejecución — M01

M01 está DONE únicamente para formular el alcance matemático. [Contrato y revisión adversarial](./M01_SCOPE_AND_QUANTIFIERS.md) · [Evidencia y límites](./M01_SCOPE_CHECKS.json) · [Cálculos diagnósticos reproducibles](./verify_m01_scope.py). La declaración anterior de todas las tareas OPEN corresponde a la aprobación del plan, no al estado posterior a esta ejecución.

El primer objetivo usa un agente y una pareja de mundos estáticos equiprobables. No redefine la campaña de población de R01 ni demuestra que exista una región inviable. M02 es el siguiente paso; M10, P03, los argumentos, las implementaciones y las campañas conservan sus pendientes. Un hallazgo material puede reabrir M01. La revisión ha sido propia, no independiente.



### Actualización de ejecución — M02

M02 está DONE para construir y comprobar el candidato conjuntivo y sus controles. [Mundos, costes, atajos y límites](./M02_WORLDS_AND_CONTROLS.md) · [Fixture completo](./M02_CONJUNCTION_FIXTURE.json) · [Comprobador](./verify_m02_worlds.py) · [76 comprobaciones y trazas](./M02_WORLD_CHECKS.json) · [Aceptación y conservación](./M02_RELEASE_CHECKS.json).

Se incluyen las 27 rutas y sus mezclas; el único camino permitido en ambos mundos entrega 3 frente a los óptimos 6. El control con información completa funciona con R=11. Consultar el dato o su certificado permite entregar el óptimo con R=12; con epsilon=3 basta M y R=11. Se conservan estos casos que resuelven el candidato. Esto no demuestra inviabilidad para todas las políticas ni una ventaja de EA o tecnología concreta.

El siguiente trabajo es reconciliar M10/P03 y abrir la revisión dirigida de fuentes/contraejemplos M06 antes de desarrollar M03. M03 deberá cubrir información tras los efectos, certificados de una unidad, caché, decisiones adaptativas y aleatorización; M04 deberá revisar fronteras y controles. Quedan 47 tareas OPEN. La revisión es propia; no sustituye C05/M05 ni la revisión independiente. La fecha UTC real, commit de entrada y límites están en el registro de evidencia.



### Actualización de ejecución — M10/P03 y revisión inicial

M10 y P03 están DONE para reconciliar el contrato y auditar las medidas. [Resultado, límites y prompt para otro agente](./M10_P03_CONTRACT_AND_MEASUREMENT_AUDIT.md) · [Contrato](./M10_RECONCILED_CONTRACT.json) · [Comprobador](./verify_m10_measurements.py) · [35 nuevas comprobaciones](./M10_MEASUREMENT_CHECKS.json) · [Fuentes primarias M06](./M06_PRIMARY_SOURCE_INTAKE.md) · [Evidencia de aceptación/conservación](./M10_RELEASE_CHECKS.json). Se reproducen también las 76 comprobaciones históricas de M02 sin cambios. La revisión es propia, no independiente.

M02 depende de un solo dato global y de precios/revisión fijados. Producir y comprobar el certificado queda incluido explícitamente en su unidad de coste. Con revisión local positiva de 2/3 por paso, consultar y entregar el óptimo cuesta 11; cambiar el prior a 9/10,1/10 permite al control ciego cumplir AVG, pero no WC. Se conservan estos controles en configuraciones distintas. La formulación no justifica un coste de información creciente con L ni una frontera para todas las arquitecturas.

M06/M11/P10 quedan IN_PROGRESS para completar fuentes, ataques al argumento/fronteras y la decisión de valor/inversión. El siguiente trabajo matemático es M03 con el contrato reconciliado; después M04 revisa región, fronteras y controles. C02/C11, oráculo independiente, campañas, tecnologías y selector mantienen sus propios pendientes. Estado global: 4 DONE, 3 IN_PROGRESS, 42 OPEN. Ningún resultado empírico, ventaja de EA ni teorema universal está cerrado por esta actualización.



### M03/M04 execution record — family trilemma and technology interfaces

**M03/M04 DONE for the versioned supplemental F/W profiles, with same-agent review.** [Full symbolic proofs, boundaries, technology changes and reviewer prompt](./M03_M04_TRILEMMA_THEOREMS.md) · [Supplemental contract](./TRILEMMA_CONTRACT.json) · [Received proposal preserved](./TRILEMMA_RECEIVED_SKETCH.md) · [Exact finite checker](./verify_trilemma.py) · [Diagnostic output](./TRILEMMA_CHECKS.json) · [Release/preservation](./TRILEMMA_RELEASE_CHECKS.json).

The proofs cover all admitted observable-history adaptive/randomized policies, effect receipts, known denials, irreversible V, prior facts, caching and centrally shared team histories. F establishes exact linear information-cost frontiers; W establishes separate exact AVG/WC frontiers and a quadratic-vs-linear dense family, plus an expected-work lower bound. The fixed prior/query interface is essential. Neither the one-binding M02 fixture nor canonical R01 has been silently changed into that family. Technical efficacy eta is supplementary; original legitimate e/a/q and joint success sigma remain intact. This contract explicitly extends the earlier M01/M10 scope for these constructions; it does not claim campaign-level closure or reprice historical operations.

Matching safe/full-information and cheap/high-effect controls exhibit each pair of objectives. Certificates, cheaper positive queries, baseline-included authorized execution, paid preeffect barriers and structural common routes are treated as distinct interfaces. A lower bound on output capacity alone gives a necessary condition, not an exact frontier. Positive technology cost alone does not prove persistence; the new document retains explicit counterexamples and absolute/relative-cost distinctions.

The checker exhaustively handles F history quotients for L<=3 and W normal-form policies for n<=4, with exact fractions and additional boundary/barrier controls; symbolic proofs provide all-size coverage. M02's 76 checks and M10's 35 checks reproduce byte-identically. The same-agent checker is not C05; M05 remains OPEN. M06/M11/P10 remain IN_PROGRESS; M07–M09, corpus/transfer, neutral oracle and campaign gates remain OPEN. Owner/reviewer: Codex by user instruction; actual UTC/input commit/hashes are in the release record. Current aggregate status: **6 DONE, 3 IN_PROGRESS, 40 OPEN**. Next: independent M05/C05 proof-and-contract review, continued M06/M11 attack, then M07 correspondence and neutral oracle contracts C02/C11/C13 before campaign/integration investment.

<!-- R01_BOT_WORKPLAN_END -->
