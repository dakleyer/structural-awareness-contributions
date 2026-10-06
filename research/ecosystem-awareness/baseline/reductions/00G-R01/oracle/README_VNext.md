# Oráculo / harness R01 C02 — VNext de auditoría

El oráculo de R01 debe permitir comparar cómo distintas tecnologías encuentran una buena solución permitida, cuánto esfuerzo necesitan y si actúan dentro de su autoridad y plazo. Para hacerlo, separa lo que sabe el evaluador de lo que puede observar el candidato. Un bloqueo no es éxito si también impide la actividad legítima; una etiqueta correcta tampoco demuestra que el efecto sobre el destino haya sido correcto.

La revisión encuentra una base propia considerable: los harness anteriores ya aportan trazas, replay, controles semánticos, ejecución con estado y recuperación. El nuevo R01 puede componer esas piezas mediante adaptadores. La dificultad es conservar el significado de cada escenario y sus costes, sin convertir los resultados anteriores en validación automática de R01 o de EA. Nelson aporta el contrato y el ciclo experimental UC4; ese trabajo complementa los harness propios.

**Método vigente:** procedimiento EP 1.2 con adiciones 1.3 y 1.4, releído en corte `e80846a0f9cf3b97cf222ed3d1e28b31d145ad3e`; §2 conserva la actualización y su identidad. La lectura anterior de EP 1.2 se fijó en `2f72751fef47d9f4cf1d270a1f7fa498a26f5760`. Historia inicial: la entrega de comentarios no completó las cuatro pasadas. La instrucción posterior IVAN-R01-ORACLE-20261006-03 abre su ejecución diferenciada; la tabla muestra el avance actual.

| Pasada | Estado de esta VNext |
|---|---|
| Fondo y lógica | Pasada previa del README y nueva lectura del conjunto/compatibilidad realizadas en sus alcances. Validación externa y código completo pendientes. |
| Evidencia y relaciones entre documentos | Contraste previo y ampliación UC4/terceros realizados; fuentes vecinas siguen parcialmente revisadas. |
| Edición, estructura y formato | Markdown y navegación de la ampliación inspeccionados; siete propuestas exactas pendientes, sin incorporación. |
| Legibilidad y comprensión humana | Relecturas previas y de la ampliación simuladas por el mismo asistente; participación humana independiente no realizada. |

Los comentarios se explican primero en lenguaje corriente. El registro de fuentes, códigos y hashes posterior permite continuar la revisión sin sustituir su contenido.

**ID del documento lógico:** `R01-ORACLE-C02-README`  
**Expediente único:** `README_VNext.md` · **Revisión acumulativa:** 1.11 · **Fecha:** 6 de octubre de 2026  
**Estado:** cuatro pasadas previas del README realizadas en su alcance; ampliación de la visión general revisada en cuatro lecturas diferenciadas por el mismo asistente; relaciones vecinas parcialmente revisadas y cierre completo abierto; siete propuestas pendientes de decisión por ID.  
**Nota externa:** [ficha de acceso](./README_REVIEW.md) · **Procedimiento:** [revisión segura del corpus](../../../../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md)

**Para retomar:** [visión general y piezas](#r01-overview-review) · [pruebas de terceros](#r01-thirdparty-test-reuse) · [siguiente bloque y pendientes](#r01-resume-work) · [matriz técnica](#r01-compatibility-matrix) · [estado de tareas1/2](#r01-tasks12-status).

Las cabeceras «parcial» o «pendiente» dentro de las primeras entradas de §3 conservan el estado histórico de esas entradas. Los registros fechados posteriores y la tabla inicial describen lo que se realizó después. No confundir esa historia con cierre completo de los documentos vecinos.

## 1. Identidad, fuente y límites

Fuente auditada: [README del oráculo](./README.md), ruta `research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/README.md`, commit `40cb19682fd1211d2c07e81ecd0242b56d425918`, blob `282d97ed967898a086303927872fbdfcaf37dd70`. Se leyó su cuerpo completo. El encabezado declara estado del 5 de octubre de 2026; instrumento `R01-C02-neutral-harness-0.7` y freeze `STAGE0_FREEZE_v0.9.json`. No hay versión editorial separada declarada para este README.

Esta VNext es un expediente de comentarios y propuestas, **no una nueva edición del oráculo**. No concede UC4-SOURCE-REVIEWED, UC4-SCHEMA-VALIDATED, STAGE0-ADMITTED ni cierre C02. Su identidad comprende el documento lógico anterior; los contratos, registros y código enlazados conservan su propiedad y no se corrigen indirectamente desde aquí.

La fuente está incluida en el [guard de preservación](../tools/check_current_route_preservation.py). La nota de revisión se coloca en una ficha externa: el README, los archivos congelados, resultados y manifests se conservan intactos. La [copia de preservación del README](../../../../../../governance/preserved-public-snapshots/2026-10-06_R01_ORACLE_README_before_VNext_40cb1968.md) tiene el mismo blob de la fuente auditada.

Cobertura: cuerpo del README y relaciones materiales identificadas con R01, C3, Q1a, 00K, 00L, 00I/S5 y UC4/UC6. El análisis de código, CI, paquetes y pruebas puntuales procede de las dos revisiones previas de este mismo chat, fijadas a los commits registrados en la [evidencia](../../../../../../governance/review/R01_ORACLE_REVIEW_EVIDENCE_2026-10-06.json). No se ejecutan aquí nuevas pruebas científicas, no se afirma revisión exhaustiva del código ni cobertura completa de todos los enlaces entrantes.

## 2. Instrucciones de Iván

**IVAN-R01-ORACLE-20261006-01 · instrucción auténtica de este chat, 6 de octubre de 2026:**

> «Tienes que documentar. Tenemos un sistema de auditoría que está dentro de Readme de Custom Positioning. Revisa ese documento y trabaja en base a este formato. Es decir, quiero tus comentarios en el VNext dentro del documento de Oráculo.»

Interpretación operativa identificada, no cita: la referencia apunta al procedimiento enlazado desde Ecosystem Positioning; el documento propietario de este expediente es el README del oráculo R01 C02. Se trasladan los comentarios de estado, compatibilidad y reaprovechamiento al espacio VNext del documento. Se conserva una sola VNext y se utiliza la ficha externa para respetar la fuente protegida.

Esta instrucción autoriza documentar la auditoría y preparar sus propuestas. **No autoriza aplicar las correcciones técnicas propuestas**, cambiar freezes, ejecutar campañas, asumir aceptación de Nelson ni escribir a otros contribuyentes.


**IVAN-R01-ORACLE-20261006-02 · instrucción auténtica de este chat, 6 de octubre de 2026:**

> «crea un plan de trabajo (recomendación tuya) dentro de vnext»

Se añade el plan recomendado en §5.1. La instrucción solicita una recomendación documentada; no cambia por sí sola los estados técnicos de C02/C11/T03 ni la decisión pendiente de cada delta.


**IVAN-R01-ORACLE-20261006-03 · instrucción auténtica de este chat:** «realiza las tareas 1 y 2». Se ejecutan las cuatro pasadas del README del oráculo y la matriz de correspondencia. La revisión cruzada se registra en los expedientes propietarios; las integraciones, validación UC4, campañas y aplicación de deltas siguen separadas.


**IVAN-R01-ORACLE-20261006-04 · instrucción auténtica de este chat, 6 de octubre de 2026:**

> «Todos estos comentarios están dentro del VNS del oráculo. O sea, quiero una revisión a fondo y que lo coloques ahí perfectamente para poder retomar el tema posteriormente con esta revisión.»

Interpretación operativa: «VNS» se refiere a esta única VNext. Se incorpora y revisa la explicación general del turno anterior, incluidos límites de UC4, compatibilidad histórica y opciones de pruebas de terceros. La petición autoriza esta documentación; no es una decisión de incorporación de los siete deltas al README protegido.

**Método actualizado leído:** EP 1.2 con adiciones 1.3 y 1.4, corte `e80846a0f9cf3b97cf222ed3d1e28b31d145ad3e`, blob `08ec7eb7c22f5d5fe9b86b1936115f45039b0ad2`. Se publican las cuatro lecturas de esta ampliación por separado. La aclaración 1.4 mantiene abiertos los consumidores, fuentes o hallazgos que no hayan recibido respuesta suficiente; los cierres acotados anteriores no significan cierre completo del documento, de C02 ni del corpus.

## 3. Auditoría del documento y sus relaciones — R01-ORACLE-AUD-001

**Auditoría realizada por Codex, agente `/root`, chat `01a11096-57f0-72b2-bd57-7d8816673410`, 6 de octubre de 2026.** Identidad del modelo/backend y acreditación como auditor externo: no verificadas. Es el mismo agente de las revisiones previas; no es auditoría independiente.

**Fuente fijada:** commit/blob de §1.  
**Método:** lectura completa del README, comparación documental y de contratos, fuentes primarias y evidencia previa; comprobaciones estáticas de citas, relaciones y propuestas. La comprobación CTv1 y consultas de CI ya ocurrieron en el turno anterior; aquí se incorporan como evidencia previa, sin repetirlas.  
**Conflictos/dependencias:** el expediente comenta trabajo que el mismo agente examinó antes; no prueba independencia. UC4/UC6 y determinaciones de otros Themes mantienen sus source owners. Cambios a documentos relacionados necesitan revisión en su VNext propia.

### Fondo y lógica — parcial

**Auditoría realizada por Codex, mismo agente, 6 de octubre de 2026.** Pregunta de lectura: ¿qué promete evaluar R01 y qué parte de esa promesa sostiene el instrumento actual?

La idea central es coherente: se congela un mundo pequeño, se limita la información del candidato, se registra lo que hace y se evalúa después frente a una referencia. Esto evita usar la propia seguridad o relato del candidato como verdad. Pero el self-test comprueba el instrumento con casos construidos; no demuestra que una tecnología real encuentre siempre la mejor ruta permitida.

La reutilización tampoco exige un oráculo universal. S5 pregunta si una reparación obsoleta cambió el destino; Q1a pregunta si se conservó la dependencia de las fuentes; R01 añade óptimo admisible, calidad y coste. Un formato común puede conectarlos, pero sus criterios de verdad deben permanecer explícitos. Si esa diferencia se pierde, un resultado correcto de un componente puede convertirse en una conclusión injustificada sobre el conjunto.

Queda por cerrar la fidelidad del evaluador a todos los perfiles R01, especialmente las relaciones, dinámica colectiva y contabilidad completa. Los dos caminos de referencia del mismo autor son un contraste de implementación, no un auditor externo. Estos comentarios proceden de la revisión previa; la pasada lógica completa del conjunto de dependencias permanece abierta.


#### Pasada 1 realizada — fondo y lógica, 6 de octubre de 2026

**Codex /root, mismo asistente; lectura diferenciada del README completo.** Fuente: corte `715027943eefb372fdb4541a23d288bffdedbdb2`, README blob `282d97ed967898a086303927872fbdfcaf37dd70`. Pregunta: ¿el argumento del documento conecta su propósito, su mecanismo y sus conclusiones sin convertir un control del instrumento en una validación de R01? Alcance: README, reglas de evaluación/trazas y cláusulas pertinentes del escenario; no prueba de todo el código ni revisión independiente.

El argumento tiene cinco pasos. Se declara un mundo acotado; se entrega al candidato solo una vista permitida; se registra su actuación antes de evaluar; se calcula una referencia desde información privada; se compara lo registrado con esa referencia y con umbrales fijados. Esta cadena permite examinar una ruta sin tomar la confianza del candidato como verdad. También admite empate e insuficiencia de referencia. Es una base razonable para construir un instrumento neutral, siempre que el perfil de mundo, el recorder y el coste representen realmente la pregunta evaluada.

**La conclusión que sí se sigue** es la que el README limita: hay una implementación parcial que se comportó como esperaba su autor en controles construidos. No se sigue que una tecnología encuentre el óptimo, que todo R01 sea ejecutable, que el evaluador sea correcto fuera de esos mundos ni que EA aporte ventaja. La lista de veintiséis funciones describe controles de mecanismos; no son veintiséis demostraciones independientes de esas conclusiones.

Hay cuatro distinciones lógicas que el lector debe conservar:

1. **Selección y efecto.** El batch puede contrastar una ruta seleccionada con el mundo privado; su contrato declara ese recorrido como conformance-only. No demuestra por sí mismo ejecución real ni ausencia de efecto prohibido. El modo interactivo puede usar evidencia privada del entorno después del sellado. El resultado se interpreta por modo y predicado, no mediante una etiqueta global idéntica.
2. **Referencia y umbral.** La referencia determina qué rutas son admisibles y cuál es el óptimo acotado; la política fija calidad, coste, presupuesto y plazo. Que ambos métodos concuerden no decide los umbrales. Y una ruta óptima elegida no satisface automáticamente recursos, completion o autoridad.
3. **Integridad y aislamiento.** El hash identifica la traza comprometida antes de la evaluación. No prueba que el proceso del candidato no pudiera leer otros archivos. Para una realización real hace falta el aislamiento declarado en su contrato. Las comprobaciones de vistas y nombres reservados aportan evidencia del instrumento; no sustituyen esa frontera.
4. **Compatibilidad y propiedad del significado.** UC4 ofrece un contrato experimental; S5, C3 y Q1a ofrecen predicados de escenarios distintos. Traducir formatos es compatible con conservar esos predicados, pero no con sustituirlos silenciosamente por el óptimo R01. Un fallo de correspondence puede invalidar una afirmación de compatibilidad sin invalidar todos los resultados del instrumento original.

**Contraejemplos examinados.** Un candidato que se abstiene siempre puede evitar una violación y seguir incumpliendo la tarea: por eso el control de abstención importa. Dos referencias del mismo mantenedor pueden compartir una omisión y concordar: su acuerdo aumenta el contraste, pero no acredita independencia externa. Un JSON bien formado puede atribuir un efecto a una mera decisión: supera sintaxis y falla significado. Un backend S5 puede impedir una reparación obsoleta y no tener ninguna noción de máximo de beneficio: su éxito no acredita el óptimo R01. Estos contraejemplos son razonamientos de auditoría, no nuevas ejecuciones.

**Supuestos que sostienen la conclusión acotada.** Mundo y expectativas fijados antes del run; campos visibles correctamente proyectados; recorder y mediciones confiables para el perfil; referencia disponible en el dominio; reglas de aceptación previas; separación de coste del candidato y evaluador; alcance de los controles conocido. Un grafo finito no basta para todas las ejecuciones posibles: ciclos, eventos gratuitos o memoria sin límite requieren horizonte y contrato de terminación propios. El plan de computabilidad lo reconoce; el README no lo debe elevar a garantía de cualquier backend.

**Resultado de esta pasada.** No se localiza un salto que obligue a retirar la conclusión limitada del README. Sí se necesita hacer más visibles el propósito para una persona, el dominio de cada modo y la diferencia entre serialización, semántica y admisión. Las propuestas 001–004 conservadas y las adiciones editoriales de las pasadas posteriores cubren esa exposición; la fidelidad completa y la revisión externa continúan en C02/M16/M17.

**Estado:** realizada en el alcance lógico declarado del README. La comprobación de cada afirmación frente a código, registros y fuentes corresponde a la siguiente pasada y no se da por hecha aquí.


#### Ampliación 2026-10-06 — fondo y lógica de la visión general

**Codex /root, mismo asistente.** Nueva pregunta: ¿se entiende qué sistema estamos construyendo, cómo se relaciona con los anteriores y qué argumento permite reutilizarlo sin confundir sus resultados? Leídos README completo, matriz §5.2, perfil UC4, registro v0.9 y plan de computabilidad; corte de partida `e80846a0`.

El problema de lectura es concreto: «oráculo», «harness», «C3», «C02» y «UC4» pueden parecer nombres del mismo evaluador. Son piezas con funciones distintas. El oráculo responde una pregunta desde una referencia; el harness organiza la ejecución y su evidencia; UC4 organiza la composición experimental y sus fronteras. La explicación incorporada en [§5.4](#r01-overview-review) desarrolla esa distinción y un ejemplo de transferencia.

La compatibilidad tiene tres preguntas separadas: ¿podemos leer los registros?, ¿conservamos su significado?, ¿se ha admitido y probado ese perfil en el destino? La matriz responde documentalmente parte de las dos primeras. No responde la tercera. El caso S5 obliga a distinguir una decisión DENY de un destino que realmente no cambió; un benchmark de herramientas añade estados observables, pero no crea por sí mismo un óptimo admisible R01.

**Resultado:** argumento de composición aprovechable por perfiles, con límites explícitos; no se justifica un oráculo universal ni importar tasas de éxito históricas. «C4» se conserva como interpretación provisional UC4 de Nelson, pendiente de corrección si Iván pretendía otro objeto. Evidencia externa y opciones de terceros se examinan en la siguiente pasada. No se atribuye revisión humana o externa a esta lectura.

### Evidencia y relaciones entre documentos — parcial

**Auditoría realizada por Codex, mismo agente, 6 de octubre de 2026.** Pregunta de lectura: ¿qué evidencia entra desde los harness anteriores y conserva su alcance cuando el README de R01 la reutiliza?

El caso de Canonical Trace es reutilización efectiva: en la comprobación puntual anterior, las diez entradas válidas comparadas produjeron los mismos bytes. También se conservaron dos diferencias sobre rechazo de entradas inválidas. Esa evidencia respalda esos ejemplos y alerta sobre el contrato de errores; no acredita intercambiabilidad completa.

00K aporta controles de invariantes, 00L aporta comparación emparejada y 00I/S5 aporta una ejecución con estado y efectos observables. El receptor R01 puede aprovecharlos como infraestructura o como perfiles de escenario. Debe conservar sus límites: 00K es simbólico, algunos peers 00L comparten lógica y S5 no es una ejecución AWS. Los controles antiguos no se convierten en nuevas observaciones R01 por enlazarlos.

Nelson/UC6 aporta una calibración de preservación de significado. El schema público sí fue accesible y sus hashes se comprobaron en la revisión previa, pero R01 todavía necesita una envolvente UC4 completa y su mapping. Los dos documentos no son formatos intercambiables por compartir la palabra «adapter».

La consecuencia si falla una de estas relaciones es concreta: se pierde la afirmación de compatibilidad o la interpretación heredada, aunque el instrumento pueda seguir siendo útil en su propio dominio. El registro posterior conserva los pasajes y fuentes. No se ha completado la revisión cruzada formal en todas las VNext vecinas; sus consecuencias se señalan aquí como dependencias pendientes, sin modificar aquellas fuentes.


#### Pasada 2 realizada — evidencia y relaciones, 6 de octubre de 2026

**Codex /root, mismo asistente; examen diferente del lógico anterior.** Pregunta: ¿qué respalda cada afirmación importante del README y qué se pierde al trasladarla entre documentos? Corte principal `715027943eefb372fdb4541a23d288bffdedbdb2`; fuentes y blobs en el [registro de esta revisión](../../../../../../governance/review/r01-oracle-tasks12-2026-10-06/REVIEW_EVIDENCE.json). Pasada 1 publicada previamente en `55505144748fedbbffd29512ca396fd71cad316f`. Se leen fuentes actuales y evidencia conservada; no se ejecutan verify.py ni campañas de los harness.

### Afirmaciones del README frente a sus fuentes

| Afirmación o funciones enumeradas | Evidencia contrastada | Qué permite concluir y qué no |
|---|---|---|
| Estado de implementación parcial y self-test exitoso | SELFTEST_RECORD_v0.9, resultado JSON y consulta directa del run 37265543867: completed/success, head 4ec2006e76b1e212ba8b99230a3d71bd3564aeb5. | Instrumentación ejecutada el 5 de octubre; no se sustituye ese run por el CI documental de hoy. Seis resultados mixtos, no seis candidatos exitosos. |
| **1–3, 10–12, 20, 23:** vistas, orden, sellos, replay, permutación, selección y evidencia privada | harness.run_case; interactive_harness.run_interactive_case; verify.main; controles y contrato de aislamiento. | El flujo consulta referencias después del sellado y contiene controles de campos/IDs y replay. La inspección estática y los controles construidos no prueban aislamiento de un candidato real. |
| **4–6, 13, 24–25:** referencia, empate, no-reference y DAG | reference/secondary; reference_agreement; contratos de admisión; verificaciones y registro v0.9. | Enumeración de trayectorias y comparación exhaustiva/DP de DAGs en dominios finitos declarados. El acuerdo corriente de trayectorias compara status, optimum y IDs óptimos; no compara cada predicado de todas las filas. No es cobertura universal o revisión externa. |
| **7, 17:** recursos | harness._authoritative_batch_measurement y ledger; recibos del broker y contador de coordinación. | Se sustituye self-report por la medición fijada del harness. Es autoritativa para ese control sintético; no es medición empírica de CPU, moneda o latencia real. |
| **8–9:** abstención y malformación | Controles always_abstain_not_success, malformed_candidate_explicit_rejection y malformed_record_isolation; rechazo registrado antes de evaluar. | Control de no-completion y de error por vector. No permite borrar fallos ni declarar segura una abstención que impide la tarea. |
| **14, 18, 21–22:** broker, revisión, mandato, mensajes y commitment | TOOL_BROKER_CONTRACT; tool_broker._state_rejection_reason/_apply_public_state/_request_contract_rejection_reason; verify y registro. | Máquina estricta de un perfil. Sus estados no implementan todas las estrategias R01 que admiten actuar con residuo. Mensaje relayed conserva procedencia; no crea una determinación independiente. |
| **15–16, 19:** identidad de inputs y admisión | Manifest v0.9, árbol Git del corte y contracts/verify. Las 30 entradas tienen el blob declarado. | Igualdad documental estática de 30 blobs comprobada hoy; no nueva ejecución del self-test. Gate y copia del sidecar se contrastan; un manifest intacto no prueba verdad del escenario. |
| **26:** admisión T03 | real_admission y registro/verify. El registro admitido del self-test usa valores sintéticos, incluida aceptación de fuente y evidencia de aislamiento. | Prueba de ramas del validador, no una revisión recibida de Nelson ni un aislamiento físico realizado. No se concede admisión a un candidato real. |
| UC4-first y versión del schema | Comentario público de Nelson 5871266911 y schema del ZIP público conservado; const=1.1.0 y additionalProperties=false. SHA256 del schema reconfirmado. | Schema 1.1.0 y paquete 1.1.0-r1 son ejes distintos. El sidecar no es la envolvente UC4. No se ejecutó validador UC4 ni se obtuvo revisión de fuente en esta tarea. |
| Antecedentes A01/A03/Q1a/C3 | A01 como diseño acotado, A03 como diseño de un harness, Q1a como ejecución descriptiva corregida, C3 como evaluador inspect. | Método, utility y predicados específicos son reutilizables. Diseño y resultados tienen estados distintos; los PASS de esos corpora no evalúan las rutas R01. |

### Relaciones cruzadas examinadas y consecuencias

Las correspondencias completas se concretan en la matriz de la tarea 2; aquí se revisa su fundamento. Cada examen se registra también en la VNext del documento receptor/origen enlazada, con estado parcial de esa fuente: **no se declaran cuatro pasadas de los vecinos**.

| Fuente y expediente cruzado | Afirmación que llega a R01 y condición | Consecuencia de la revisión |
|---|---|---|
| [Escenario R01 / VNext](../Escenario-creatividad-validacion_VNext.md) | §§1.4/2.6/2.15–2.17 requieren entrega legítima a tiempo, observaciones acotadas, trazas causales y contraste competente. | El batch valida selección/conformidad. Sus campos completion y legitimate_q no se importan como a/q de entrega efectiva. Conserva la tesis, pero la cobertura métrica plena sigue abierta. |
| [Computabilidad / VNext](../COMPUTABILITY_AND_ORACLE_PLAN_VNext.md) | Separación G0–G3 y ledger; dominio finito y segunda referencia. | Diseño bien alineado con el slice, sin cierre total. Referencias históricas a freeze v0.4 y el sidecar que cita v0.8 no se renumeran; el entry point verificó v0.9. El import debe fijar el paquete efectivo y registrar cada eje. |
| [A01 / VNext](../../../00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1_VNext.md) | O_ref es limitado al universo representado; residuo explícito. | R01 preserva esa distinción cuando responde INCONCLUSIVE. No convierte el diseño A01 en un resultado R01 ni al evaluador en productor de autoridad. |
| [A03 / VNext](../../../00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1_VNext.md) y [Q1a / VNext](../../../fixtures/RS-00E-Q1a/README_VNext.md) | Roles separados, control inverso, carga estipulada y CTv1 con arrays semánticos ordenados. | Hay utility real reutilizada, con diferencias en entradas inválidas. La solución es una frontera de importación acotada, no decir que ambos helpers son idénticos. B1/B3 de lógica compartida no validan superioridad. |
| [C3 / VNext](../../../fixtures/00G-HF-ORACLE-v0.4/README_VNext.md) | Autoridad/aplicabilidad, commitment, intento, efecto y completion en inspect T0/X–T1/Y. | Se conserva verdad trivaluada y cobertura de traza. Una operación S5 de repair no tiene proyección inspect automática; optimum y ledger R01 no aparecen en C3. |
| [00K / VNext](../../../fixtures/00K-SUITE/README_VNext.md) | Invariantes P1–P6, controles positivos, fuertes reparaciones y falsadores retenidos. | Fuente de controles, no un runtime API. El runner agrega pytest por carpeta; no produce el candidate_result común. Los sustitutos verdaderos limitan las tesis de necesidad. |
| [00L / VNext](../../../00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/README_VNext.md) | F/O/K/E y disposición con scope, owner, plazo y residual. | Preserva orden experimental y fairness. Deducción D no se convierte en observación ejecutada; los campos de coste ausentes continúan null con razón. |
| [00I/S5 / VNext](../../../fixtures/00I-STATEFUL/README_VNext.md) | Modelo, fuentes, guard, permiso, executor y post-run evaluate separado. | Backend stateful útil. EXECUTE es una disposición, applied/final_generation son evidencias diferentes. Sin transformarlo en una ruta óptima ni importar sus 44/8 como tasa R01. |
| [Primer R01 / VNext](../feasibility/partial-experiments/README_VNext.md) | Checks iniciales y countercontrols con su contrato y época. | Sirven para atacar errores del nuevo perfil. No sustituyen el teorema v0.2 ni el evaluador C02; títulos antiguos de tracking se leen históricamente. |
| [00G-HF dinámico / VNext](../../../traversals/00G-HF-DYNAMIC-REVIEW-v0.1/README_VNext.md) | Protocolo/runner, seed por evento y proyección C3; resultados posteriores. | **Campaña sí ejecutada:** RESULTS registra 1.056 redes/50.688 registros y replay, sin EA/LLM. README de preparación conserva «pendiente». Se registra esa discrepancia temporal; no se usa el header antiguo para negar los resultados. FRESH evita efectos indebidos en esa malla; continuity y A25 siguen limitados. |
| [UC4 / VNext](./UC4_INTEROPERABILITY_PROFILE_VNext.md) | Adapters versionados, expectativas privadas, capacidades y tres clases de revisión separadas. | Coincidencia de intención y estructura parcial; schema exacto, semántica y admisión son verificaciones diferentes. R01 no fabrica las determinaciones del source owner. |
| [Ecosystem Positioning / VNext](../../../../../../architectural-contributions/ecosystem-positioning/README_VNext.md) | El router presenta el corpus y sus evidencias. | Esta revisión aporta un README inspeccionado y una matriz acotada; no cierre general del corpus, prueba universal, aceptación FG-TIDA ni eficacia de EA. |

### Hallazgos nuevos y límites conservados

- **F011 — modo y efecto:** un PASS batch declara su carácter de conformidad; execution_verified=false y executed_violation=null. En consecuencia no se rellena «efecto seguro» con false. El interactivo exige efecto coincidente y conserva contradicción de referencia/entorno como INCONCLUSIVE.
- **F012 — sellado e independencia:** hash de traza, ausencia de claves en la vista y aislamiento externo son propiedades distintas. Se necesita mantener sus fuentes de evidencia separadas.
- **F013 — versiones de manifest:** v0.9 mantiene inputs de épocas previas; el sidecar referencia v0.8. Esos punteros se retienen. Una adaptación futura debe fijar el entry point efectivo y los hashes, sin asumir que todos los campos de versión describen el mismo objeto.
- **F014 — ámbito de comparación de referencias:** reference_agreement mira status/optimum/ties. La equivalencia de filas, predicados y effects no se concluye solo de esos tres campos. Añadirlos al contrato de correspondence precede a ampliar el dominio.
- **F015 — preparación y resultado dinámico:** el estado de campaña del README 00G-HF dinámico quedó histórico; existe un resultado posterior. Se rectifica cualquier lectura actual de «campaña no ejecutada» derivada solo del router. No se transfiere ese resultado a R01.
- **F016 — métricas:** evaluate_candidate calcula completion de la declaración y completitud de la trayectoria, y legitimate_q antes de comprobar plazo. §1.4 define a/q sobre entrega completa admisible dentro de T. Los nombres son próximos, pero los predicados difieren. El import conserva valores nativos y separa los derivados que pueda sostener; sin efecto/tiempo suficiente deja q/a desconocidos.

**Comprobación CTv1 adicional, alcance de contrato.** Se creó fuera del instrumento un prototipo de frontera de importación: diez ejemplos válidos con bytes coincidentes, catorce inválidos con rechazo común y cuatro propiedades de orden/exclusión/no-mutación, **28 comprobaciones acotadas**. Los helpers originales siguen distintos. Esto resuelve la decisión de contrato para la tarea 2 y no instala un adaptador, cambia el freeze, ejecuta una campaña ni demuestra conformidad universal. [Prototipo y resultados](../../../../../../governance/review/r01-oracle-tasks12-2026-10-06/CTv1_IMPORT_REVIEW_RESULT.json).

**Cobertura de cierre.** Todas las afirmaciones importantes del README se contrastaron contra sus fuentes de instrumento, evidencia registrada, upstream citado y receptores materiales descritos arriba. Los 57 archivos recuperados son fuentes, no 57 auditorías completas. Quedan fuera: todos los papers externos completos; todos los nueve perfiles de 00L; universalidad de kernels; todas las variantes de cada runner; reproducción de binarios/resultados comprimidos; prueba de aislamiento real y validación externa. El inventario de enlaces entrantes se registra por separado, sin tratar presencia de un link como dependencia semántica comprobada.

**Estado:** pasada realizada para el README y las relaciones materiales declaradas, con discrepancias y obligaciones de ingeniería abiertas. Una auditoría puede terminar encontrando brechas; no se cierran C02/M16/M17 con este registro.


#### Ampliación 2026-10-06 — evidencia y relaciones de la visión general

**Codex /root, mismo asistente; segunda pregunta de revisión.** ¿Qué respalda el estado descrito y qué autorizan a concluir las baterías externas? Contraste del README con SELFTEST_RECORD_v0.9, perfil UC4, NELSON_BASELINE_IMPORT, plan de computabilidad y WORKPLAN vigente; fuentes primarias externas leídas el 6 de octubre. El [anexo de evidencia de esta ampliación](../../../../../../governance/review/R01_ORACLE_OVERVIEW_REVIEW_2026-10-06.json) registra corte y límites.

El pasaje «instrumentation only; no real technology executed» del registro v0.9 limita el alcance de la primera fila de §5.4. La tabla de niveles del perfil mantiene R01-BRIDGE-DRAFT y evita convertir la envolvente propuesta en un paquete admitido. WORKPLAN mantiene C02 activo y C11/T03 posteriores. La evidencia CTv1 ya publicada respalda 28 microchecks de un prototipo de importación; no respalda conformance universal ni rollout.

**Diferencia entre fuente antigua y acceso actual:** NELSON_BASELINE_IMPORT contiene una limitación de acceso al attachment de su fecha. La revisión previa recuperó y preservó el paquete original y registró el hash del schema. Ese acceso posterior no demuestra que el perfil R01 haya pasado su validador ni que el contributor lo haya aceptado. No reescribir la nota histórica como si siempre hubiera existido ese acceso.

**Terceros:** JSON Schema Test Suite prueba el comportamiento del validador; Hypothesis genera secuencias contra invariantes que debemos escribir; ToolSandbox evalúa estados e hitos; AgentDojo evalúa ataques y defensas de prompt injection; τ-bench aporta dominios con políticas y herramientas; CP-SAT resuelve un modelo formalizado y distingue sus estados de resolución. Cada una apoya una función distinta. No se ha instalado, ejecutado o certificado una integración R01 de estas alternativas. Las fuentes y condiciones concretas quedan en §5.4.

**Relación cruzada:** el límite UC4 ↔ R01 vuelve a la VNext del perfil, ampliando R01-X12 sin cerrar sus otras pasadas. Las demás familias conservan sus revisiones cruzadas previas y sus límites; esta ampliación no contiene una auditoría íntegra de cada una. Las fuentes externas son opciones técnicas, no nuevas dependencias normativas ni cambios de organización del corpus.

**Resultado:** la visión general conserva el grado de evidencia de sus fuentes. La selección y orden de reutilización son recomendaciones razonadas del mismo asistente. Faltan versiones de implementación fijadas, mapping, ejecución y revisión de los perfiles futuros.

### Edición, estructura y formato — pendiente como pasada separada

La revisión mixta encontró insumos editoriales: diferenciar versión del schema y del ZIP, explicar el resultado mixto del self-test y hacer visible la infraestructura propia. Las cuatro propuestas exactas del final conservan esos comentarios. No se declara cerrada la edición completa del documento ni se modifica su cuerpo para corregirlos.


#### Pasada 3 realizada — edición, estructura y formato, 6 de octubre de 2026

**Codex /root, mismo asistente.** Lectura nueva del Markdown completo, todas sus secciones, listas, diagrama y directorio. Pasada de evidencia publicada primero en `aa9e077cdbef5a38af4bb78f94552981459f16ad`. Pregunta: ¿el orden y el formato permiten distinguir propósito, uso, evidencia y límite? No es una revisión de exportaciones PDF/DOCX ni de un código ejecutado.

El orden actual favorece al mantenedor: estado, atribución, composición UC4, evidencia, lista de funciones, comando y directorio. La atribución es pertinente, pero precede a una explicación sencilla de qué recibe y devuelve el instrumento. Una persona nueva encuentra “C02”, “UC-4-first” y “sidecar” antes de poder describir la pregunta del test.

**Propuestas localizadas y efecto en la lectura:**

- Añadir después del estado dos frases sobre comparar una elección/ejecución con una ruta admisible, con recursos y plazo. Conserva la atribución y el diseño; **DELTA-005** añade propósito sin reordenar la fuente.
- El bloque “Corpus reuse” tiene cinco rutas como texto plano. Convertirlas en enlaces Markdown con labels que distingan escenario, C3 y diseño hace posible seguir sus fuentes; **DELTA-007** es navegación, no cambio de propiedad semántica.
- La lista de veintiséis controles sirve de inventario técnico, pero mezcla pruebas de vistas, referencias, contabilidad, integridad y admisión. En vez de sustituirla, el relato de esta VNext agrupa sus funciones en la tabla de evidencia. Una agrupación futura del README necesitaría su propio antes/después; no se presume aprobada.
- La interpretación del resultado debe preceder al comando de reproducción. **DELTA-003** conserva el resultado mixto; **DELTA-006** explica batch/interactivo y métricas. El código **python3 verify.py** reproduce controles; una persona no debe leerlo como ejecución del producto que desea comparar.
- El diagrama distingue envolvente y sidecar; el directorio facilita encontrar archivos. Ambos son texto preformateado. No se detectó pérdida de relaciones por su formato. El directorio no pretende enumerar los instrumentos de auditoría añadidos después; no se lo modifica para convertirlo en un registro vivo.
- Versiones 0.7, v0.9, schema 1.1.0 y ZIP 1.1.0-r1 deben llevar el nombre del objeto. **DELTA-001** y la matriz evitan que el lector interprete varios ejes como una inconsistencia automática.
- El título “Claim boundary” es adecuado, pero los límites decisivos también deben aparecer en la explicación inicial y junto al modo de ejecución. **DELTA-004/006** hacen visible el alcance antes de que una etiqueta PASS pueda interpretarse como validación general.

**Comprobación editorial de esta pasada.** El README no contiene ecuaciones, tablas propias o figuras externas que necesiten inspección aparte; el diagrama y árbol usan bloques cerrados. Sus links Markdown locales tienen destinos existentes; las rutas planas se revisan con su contexto real. El comando y el estado de instrumento no presentan una versión Python mínima propia: antes de una guía instalable habrá que fijar entorno; no se inventa un requisito nuevo en este comentario.

**Resultado:** inspección de edición y estructura del Markdown terminada. Las correcciones 001–007 son propuestas al final, pendientes de decisión; el texto original y las cuatro propuestas anteriores se conservan. La siguiente pasada se centra en la experiencia de una persona que llega sin los chats.


#### Ampliación 2026-10-06 — edición, estructura y formato

**Codex /root, mismo asistente.** Pregunta: ¿puede un lector localizar y continuar la explicación sin reconstruir el chat ni confundir estados históricos y actuales? Inspección del Markdown completo de la VNext ampliada; se conserva el cuerpo de los siete deltas y su decisión pendiente.

Se añade un acceso breve al principio hacia visión general, opciones de terceros, matriz y siguiente bloque. El relato distingue piezas, conexiones, límites y batería de correspondencia; las tablas sirven para comparar funciones. El diagrama es texto explícitamente propuesto, con verdad privada fijada antes del run. No crea un nivel público nuevo de README ni una reorganización del corpus.

**Ambigüedades editoriales localizadas:** §5.1 conserva la tabla original con «todas sus ejecuciones pendientes», aunque tareas1/2 fueron realizadas documentalmente después; conserva también el primer bloque que aún proponía hacer la matriz. Esa historia se mantiene y se precisa en el nuevo apartado de reanudación: la matriz ya existe, el siguiente entregable recomendado es el paquete acotado, sin repetir tareas1/2. La palabra C4 se explica como interpretación UC4, no se rebautiza un componente.

Se comprueban anclas únicas, tablas, pares de fences y rutas de apoyo; los resultados técnicos se registran aparte. La ampliación es una revisión y recomendación dentro de VNext, sin nuevas propuestas de sustitución al README canónico. Siguen siendo siete deltas, pendientes de Iván. Esta pasada inspecciona Markdown; no cuenta como prueba de lectura por una persona independiente.

### Legibilidad y comprensión humana — pendiente como pasada separada

Un lector que llega sin los chats necesita entender qué significa evaluar una ruta permitida y por qué reaprovechar un harness no transfiere sus conclusiones. El README comienza con C02, Stage 0 y UC4; la VNext añade arriba una explicación para situar esa pregunta. Esto es una observación y simulación de lectura por el mismo asistente, no una prueba con otra persona ni una pasada completa de comprensión humana.


#### Pasada 4 realizada — legibilidad y comprensión humana, 6 de octubre de 2026

**Codex /root, mismo asistente.** Relectura del README vigente desde su inicio hasta el límite final, después de publicar la inspección editorial en `64ef5f8d059ec0cb944915f779f000baadaa8b89`. Pregunta distinta: ¿qué podría reconstruir una persona nueva sin los chats? Se trata de **simulación de lectura por el asistente que ya conoce el trabajo**; no lectura ciega, participante humano ni validación independiente.

**Recorrido de lectura.** El primer párrafo permite saber que el instrumento es limitado y que no hubo campaña de tecnología. El segundo presenta UC4 como destino preferido, pero presupone entender C02, sidecar y Theme #13. La lista de atribuciones aporta procedencia antes de explicar una tarea concreta. El diagrama aclara que la envolvente experimental y el evaluador privado son piezas distintas. La sección de evidencia permite encontrar un run y sus registros, aunque una persona podría leer “successful” como éxito de todos los casos. La lista de funciones explica lo que comprueba el mantenedor; al llegar al comando, todavía cuesta distinguir una selección batch de un efecto registrado. El cierre limita las conclusiones correctamente, pero llega después de la parte que más podría generalizarse.

### Preguntas de comprensión examinadas

| Pregunta de una persona nueva | Respuesta reconstruible de la fuente | Dificultad y propuesta |
|---|---|---|
| ¿Para qué sirve? | Para evaluar un slice R01 con vistas privadas/públicas, referencia y recursos. | Falta una frase concreta sobre una buena ruta permitida: DELTA-005. |
| ¿Qué tendría que entregar mi tecnología? | Una respuesta/traza a través de un adapter; batch o interacción con broker. | La forma precisa vive en la guía. Mantener esa ruta; no prometer conexión directa de cualquier producto. |
| ¿Qué recibe el candidato y qué sabe el evaluador? | Vista permitida frente a mundo/referencia privada. | El diagrama ayuda. Añadir explicación de “oráculo” como referencia de este mundo, no verdad universal. |
| ¿Qué significa el verde? | Self-test con los resultados esperados; no campaña real. | DELTA-003 muestra PASS/FAIL/INCONCLUSIVE juntos y evita la lectura “todos aprobaron”. |
| ¿Ya es compatible con Nelson? | Hay alineamiento semántico; schema/review/admission siguen pendientes. | DELTA-001 separa versión del esquema y del ZIP; la matriz explica los tres cierres. |
| ¿Qué puedo reutilizar del trabajo antiguo? | C3, diseño A01/A03 y CTv1 están citados. | DELTA-002 y la matriz hacen visibles 00K/00L/00I/primer R01 sin transferir resultados. |
| ¿PASS demuestra una ejecución segura, barata y eficaz? | Depende del modo y dominio; la fuente limita su claim. | DELTA-006 sitúa efecto/métrica/aislamiento antes de reproducir. El coste sintético conserva su unidad. |
| ¿Cuál es el siguiente trabajo? | C11/T03 son posteriores; el README remite a contratos y registros. | La VNext añade una secuencia recomendada y separa revisión documental de ingeniería/campaña. |

**Ejemplo explicativo de revisión, no nueva fixture.** Imaginemos que una ruta más atractiva tiene una conexión prohibida y otra ruta permite completar la misma misión. El evaluador conoce la conexión; el candidato debe descubrir o comprobar lo que su vista y herramientas le permiten. Elegir la atractiva no se vuelve correcto porque su relato diga “seguro”; impedir todas las rutas tampoco entrega la misión. Este ejemplo ilustra por qué se separan observación, permiso, elección, efecto y evaluación. No modifica los seis mundos congelados ni demuestra qué elegiría un producto.

**Vocabulario mínimo propuesto para la lectura.** El *harness* organiza y registra la prueba; el *oráculo de referencia* calcula lo que puede decidir del mundo acotado; el *adapter* traduce una frontera declarada; el *sidecar* conserva información específica de R01 junto al experimento UC4. Ninguna de esas piezas hereda la autoridad de un contribuyente ni hace independiente al mismo autor por cambiar de archivo.

**Resultado:** la fuente comunica bien su límite técnico a un lector del proyecto; necesita las aclaraciones de propósito, modos y antecedentes para una persona que llega de fuera. Se han preparado propuestas concretas 001–007 para esas dificultades. Su comprensión posterior a incorporación no se ha probado con una persona; no se asigna puntuación ficticia ni se afirma accesibilidad validada.

**Estado:** relectura simulada terminada en el alcance del README Markdown. Las cuatro pasadas son ahora registros diferentes, publicados en orden. Una evaluación externa de legibilidad queda explícitamente separada; no impide completar esta simulación autorizada ni se declara realizada.


#### Ampliación 2026-10-06 — legibilidad y comprensión humana

**Codex /root, mismo asistente; simulación de lectura de una persona nueva.** Pregunta: ¿puede alguien retomar el tema desde esta página y decidir cuál es el trabajo pendiente sin recordar nuestra conversación? Se releen apertura, §5.4 completo, matriz y tabla de reanudación después de las tres publicaciones previas. No participó una persona independiente.

La primera lectura permite ahora contar el sistema: hay un instrumento parcial, backends y pruebas anteriores, una envolvente UC4 propuesta y conexiones aún pendientes. El vocabulario básico aparece antes del diagrama. «C4» conserva su interpretación explícita; los alcances del batch, de los sellos y de los resultados históricos no se presentan como hechos de una campaña real.

**Preguntas de comprensión resueltas en la página:**

| Pregunta del lector | Respuesta que puede reconstruir |
|---|---|
| ¿Qué tenemos realmente? | Instrumentación limitada y controles ejecutados; integración completa y tecnología real siguen pendientes. |
| ¿Qué pieza juzga y cuál ejecuta? | El oráculo evalúa desde referencia; el harness organiza ejecución y evidencia; el adaptador conserva el contrato del caso. |
| ¿Para qué entra UC4? | Envolvente experimental y frontera de interoperabilidad propuesta, con revisión/admisión separadas. |
| ¿Puedo usar el C3 antiguo? | Sus predicados de inspect y su evidencia, mediante mapping acotado; no como óptimo R01. |
| ¿Qué no tengo que volver a hacer? | Tareas1/2 documentales, controles ya preservados y entregas virtuales reconocidas por la cola. |
| ¿Qué puedo aprovechar de terceros? | Validador, suite de conformidad, generador y escenarios seleccionados, con su función y límite. |
| ¿Cuál es el siguiente entregable? | Un ejemplo UC4/R01 de un caso S5, trazable y validado estructuralmente, con cuestiones semánticas visibles. |
| ¿Qué falta para una campaña real? | Perfil suficiente, mapping admitido, registro, capacidades y aislamiento; C11/T03. |

**Dificultad que persiste:** la VNext acumula historia, auditorías y propuestas y sigue siendo larga. El acceso inicial y §5.4 permiten leer primero el relato y volver después a detalle y antecedentes. No ocultar o borrar la historia para simular un documento corto. La repetición de estados antiguos queda explicada; las siete propuestas al canon permanecen al final.

**Resultado de comprensión:** las preguntas de esta conversación encuentran respuesta y próximo paso dentro del expediente. La lectura por una persona independiente, la auditoría completa de fuentes vecinas y el cierre global siguen abiertos. La revisión documental permite retomar el tema; no certifica implementación, aceptación UC4 o verdad universal.

### Apoyo técnico de la revisión

### Registro de hallazgos

| ID | Pasaje exacto / relación | Consecuencia y disposición | Evidencia y cobertura pendiente |
|---|---|---|---|
| R01-ORACLE-F001 | «Status: limited implementation + successful Stage-0 instrumentation self-test» y «What is executable now». | La frontera limitada es correcta; el resultado global verde debe distinguirse de los seis estados de los candidatos. Clarificación propuesta, sin ampliar afirmación. | Registro v0.9: positivo/empate PASS; conector/inadmisibilidad/coste FAIL; sin referencia INCONCLUSIVE. No campaña real. |
| R01-ORACLE-F002 | «Corpus reuse:» enumera C3, A01, A03 y Canonical Trace; no desarrolla 00K, 00L, 00I-STATEFUL ni los diagnósticos del primer R01. | Infraestructura propia sustancial queda poco visible. Proponer una matriz de reutilización observada frente a integración pendiente. | [00K](../../../fixtures/00K-SUITE/README.md), [00L](../../../00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/README.md), [00I/S5](../../../fixtures/00I-STATEFUL/README.md), [diagnósticos anteriores](../feasibility/partial-experiments/README.md). No plugins admitidos de C02 por esta cita. |
| R01-ORACLE-F003 | «Canonical Trace v1 source implementation» frente al helper adaptado de R01. | Hay reutilización real con compatibilidad puntual en el dominio válido, pero no identidad total de contrato. Root inválido y tipo de error difieren. Hallazgo de soporte técnico, sin cambiar código congelado. | Dieciséis comparaciones previas: 10/10 ejemplos válidos con bytes idénticos; Q1a rechaza root lista de pares y R01 lo convierte; set-like sin clave produce CanonicalTraceError/KeyError respectivamente. No demuestra bypass actual. Suite completa y revisión de llamadores pendientes. |
| R01-ORACLE-F004 | «UC #4 public experiment schema 1.1.0-r1» y relación con «Current gap» de NELSON_BASELINE_IMPORT. | Separar schema 1.1.0 de package 1.1.0-r1. La limitación específica del conector sigue describiendo ese conector, pero el adjunto público fue accesible mediante otra ruta en la revisión previa. Disponibilidad no equivale a incorporación ni validación. | Companion público descargado; hashes del schema/README verificados y schema idéntico en ambos ZIPs de resultados. Registro en evidencia. No se modifica el documento relacionado desde esta VNext. |
| R01-ORACLE-F005 | «semantic alignment, not byte-level/schema-validator compatibility». | Límite correcto. El sidecar no es un experiment.json UC4 completo: hace falta la envolvente, mapping y validación. No promover nivel por existir JSON Schema o test propio. | UC4 schema exige metadata, attribution, objective, topology, execution, adapters, cases, reproducibility, data_policy y foundation; revisión de fuente y admisión R01 siguen pendientes. |
| R01-ORACLE-F006 | «recompute the same reference through a separate implementation path» y controles DAG. | Distinguir segunda ruta de código, contraste algorítmico e independencia externa. El soporte finito no cubre toda R01 ni todos sus predicados. Clarificación propuesta. | reference/secondary mantenidos por mismo autor; DAG exhaustivo/DP cubren dominio declarado conjuntivo no negativo. M16/M17 y revisión externa pendientes. |
| R01-ORACLE-F007 | «Existing partial C3 oracle» como reutilización. | C3 es reutilizable para predicados en su dominio inspect T0/X–T1/Y. No calcula el óptimo o ledger completo R01; una reparación no debe disfrazarse de inspect. | [Estado de proyección](../../../fixtures/00G-HF-ORACLE-v0.4/ESTADO_00G-R01.md). Falta correspondencia tipada de identidad, autoridad, tiempo, acción y efecto. |
| R01-ORACLE-F008 | «expose the §2.6 operation surface through a bounded tool broker» frente a 00I/S5. | El harness anterior tiene Sources/Guard/Permit/Executor y backend de cambios/efectos reaprovechables. Portar mediante adaptador; no sustituir su oráculo específico por el óptimo de rutas sin justificar la correspondencia. | 00I registra 52 filas (44 aceptación/8 fallos retenidos) y 49 regresiones, incluidos testigos SQLite. No es adaptador UC4 validado ni AWS ejecutado. |
| R01-ORACLE-F009 | «reuses several control patterns already demonstrated in Nelson's Stage-0 calibration». | Conservar atribución y separación de dominios. Las 64 aserciones por interfaz de UC6 y las 379 regresiones 00K no se suman como pruebas R01. Los fallos convencionales y éxitos convencionales reciben su crédito original. | UC6 preserva determinaciones suministradas; 00K prueba invariantes en fixtures; 00L contiene peers de lógica compartida. Comparación independiente real no establecida. |
| R01-ORACLE-F010 | «retain operational cost separately from oracle/evaluator work» y el paso a harness antiguos. | Read-count, tiempo lógico, cargos de perfil y mediciones reales tienen unidades distintas. Falta ledger de descarte, coordinación, reuso, mantenimiento y runtime real para ampliar R01. La segunda referencia no debe cargarse como coste del candidato. | [Coste y oráculo](../COMPUTABILITY_AND_ORACLE_PLAN.md), [broker](./TOOL_BROKER_CONTRACT.md), [guía de adaptadores](./TECHNOLOGY_ADAPTER_GUIDE.md). Cobertura por perfil pendiente. |

### Correspondencias de reutilización — observadas y propuestas

| Fuente | Qué existe | Uso en R01 | Estado |
|---|---|---|---|
| Q1a / CTv1 | Helper, trazas, replay y separación post-run. | Helper adaptado y patrones de harness. | **Reutilización observada; conformidad total no cerrada.** |
| 00K | Suites P1–P6, ablaciones y falsadores; 379 regresiones registradas. | Regresión semántica y diseño de controles para perfiles nuevos. | **Disponible; importación concreta no establecida.** |
| 00L | F/O/K/E, ramas emparejadas, mutaciones y S/T/Q. | Contrato experimental y controles de observación/fairness. | **Método reutilizable; API/ledger a adaptar.** |
| 00I-STATEFUL / S5 | Cola, Sources, Guard, Permit, Executor, World, recuperación y DurableExecutor. | Backend stateful y evaluación separada de decisión/intento/efecto. | **Mapping propuesto; adaptador R01/UC4 pendiente.** |
| 00G-HF runners | Recorder, mensajes/redes, semillas, episodios y calendarios. | Futuro backend poblacional y de cambios sucesivos. | **Requiere proyección; resultados no heredados.** |
| Primer R01 M01/M02/M10/F-W | Diagnósticos, mundos pequeños, costes y enumeraciones. | Contrapruebas del nuevo evaluador y correspondencia por cláusula. | **Soporte histórico; contratos a revalidar.** |
| EP traceability audit v0.4 | Evaluadores separados, mutantes, historia y cambios ocultos. | Auditoría de circularidad/semántica y límites observables. | **Soporte componente; no composición completa.** |
| Nelson UC4/UC6 | Envolvente experimental, adaptadores, expectativas revisadas y calibraciones. | Entrada de experimento común + sidecar privado R01. | **Alineamiento semántico; revisión específica/schema/admisión pendientes.** |

### Relaciones y consumidores

Upstream: [escenario R01](../Escenario-creatividad-validacion.md), [plan de computabilidad/oráculo](../COMPUTABILITY_AND_ORACLE_PLAN.md), [C3](../../../fixtures/00G-HF-ORACLE-v0.4/README.md), [Q1a](../../../fixtures/RS-00E-Q1a/README.md), UC4 y contributors de determinaciones. El README es un router del instrumento, no propietario de todas estas semánticas.

Consumidores identificados: [README R01](../README.md), [WORKPLAN](../feasibility/WORKPLAN.md), [estado de adaptación C3](../../../fixtures/00G-HF-ORACLE-v0.4/ESTADO_00G-R01.md), [perfil UC4](./UC4_INTEROPERABILITY_PROFILE.md) y [guía de tecnologías](./TECHNOLOGY_ADAPTER_GUIDE.md). La búsqueda de todos los inbound links del repositorio queda parcial; no se declara auditoría transitiva completa.

[Requirements VNext](../../../00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) y [EP README VNext](../../../../../../architectural-contributions/ecosystem-positioning/README_VNext.md) son expedientes relacionados. Esta auditoría no corrige sus fuentes ni cierra sus hallazgos. Los contratos/oráculos vecinos aún sin VNext necesitarán su expediente propietario antes de propuestas sobre sus cuerpos.

## 4. Conversación acumulativa y auto-revisión — R01-ORACLE-AUD-002

**Auditoría realizada por Codex `/root`, auto-revisión del mismo agente, 6 de octubre de 2026.** Fuente: §1 y las dos revisiones previas del chat. No es segunda revisión independiente.

- **F002/F008 — rectificación de énfasis:** el primer informe había desarrollado Nelson/UC4 más que los harness propios. La revisión posterior localizó 00K/00L/00I y concreta su reutilización. Se conservan ambas fronteras: hay activos sustanciales; no hay equivalencia inmediata de runners/oráculos.
- **F003 — contraejemplo a intercambiabilidad total:** la igualdad CTv1 en diez inputs válidos no cubre root/errores inválidos. La comparación previa produjo dos diferencias concretas. Se retira cualquier interpretación de «mismos bytes en ejemplos válidos» como «helpers totalmente idénticos».
- **F004/F005 — evidencia adicional:** se resolvió el acceso al ZIP público en el turno previo, pero no se importó al instrumento ni se obtuvo validator-pass/aceptación. No convertir el éxito de descarga en compatibilidad admitida.
- **F006 — límite:** dos implementaciones del mismo mantenedor y controles finitos aumentan la comprobación; no simulan auditor externo ni cierran cobertura universal.
- **F007/F010 — pregunta abierta:** ¿qué predicados, unidades y decisiones se preservan por perfil? Debe contestarse con mapping y controles previos a una campaña, no con cambio de nombres.
- **F009 — resultado adverso protegido:** los éxitos de controles convencionales y los límites de fixtures anteriores no se reclasifican para favorecer EA.

**Comentarios de Nelson leídos en la revisión previa:** [UC4 ciclo experimental](https://github.com/FG-TIDA/use-cases/issues/4#issuecomment-5846988611), [UC6/Theme13 resultado](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5949120841), [UC6/Theme16 resultado](https://github.com/FG-TIDA/themes/issues/16#issuecomment-5949168764), [S5 preparación y licencia](https://github.com/FG-TIDA/use-cases/issues/21#issuecomment-6012160598). Son fuentes atribuidas, no firmas de esta auditoría ni aprobación específica de R01.

Su correo del 6 de octubre sobre trabajo científico/Lifecycle fue leído como contexto privado en el turno previo. No se publica su cuerpo ni se convierte en aceptación del sidecar. La revisión específica descrita en [NELSON_REVIEW_REQUEST](./NELSON_REVIEW_REQUEST.md) permanece pendiente.

## 5. Decisiones e instrucciones posteriores de Iván

| ID | Instrucción / decisión auténtica | Alcance | Estado |
|---|---|---|---|
| IVAN-R01-ORACLE-20261006-01 | Documentar los comentarios en la VNext del oráculo según el procedimiento EP. | Crear/reutilizar el expediente, registrar auditoría, conversación y propuestas. | Ejecutada por esta entrega documental; no adopción de deltas técnicos. |
| IVAN-R01-ORACLE-20261006-03 | Realizar tareas 1 y 2 del plan. | Cuatro pasadas del README y matriz de compatibilidad, con registro cruzado. | Realizadas en alcance documental/de contrato; simulación de lectura identificada; adapters/campañas/deltas no ejecutados. |
| IVAN-R01-ORACLE-20261006-02 | Añadir un plan de trabajo recomendado dentro de esta VNext. | Secuencia, entregables, dependencias y criterios de cierre; mantener la cola propietaria. | Ejecutada como documentación del plan; trabajo futuro pendiente. |
| R01-ORACLE-DELTA-001–004 | No hay decisión de incorporación por ID en este chat. | Corrección del README o successor protegido. | **Pendiente de Iván.** |
| Campañas C11/T03 y comunicaciones | No autorizadas por esta instrucción documental. | Experimentos nuevos, integración/aceptación de contribuyentes y mensajes. | No ejecutados. |

La cola activa sigue en [WORKPLAN.md](../feasibility/WORKPLAN.md). Las recomendaciones de esta auditoría no crean una cola paralela ni convierten tareas históricas en activas. No hay autorizaciones inferidas de silencio, resultado verde o nombre de archivo.


## 5.1. Plan de trabajo recomendado para el oráculo y la reutilización

**Recomendación de Codex, mismo agente, 6 de octubre de 2026 · revisión 1.1 del expediente.** Instrucción auténtica **IVAN-R01-ORACLE-20261006-02**: «crea un plan de trabajo (recomendación tuya) dentro de vnext». Se autoriza añadir esta recomendación al expediente; su publicación no ejecuta las integraciones ni incorpora las cuatro correcciones propuestas.

Mi recomendación es consolidar una frontera común de experimento y trazas, con adaptadores pequeños y evaluadores específicos por escenario. Hay suficiente infraestructura propia para evitar empezar de cero. El trabajo decisivo es demostrar qué significado conserva cada adaptación: una ejecución stateful correcta de S5 y una ruta óptima admisible de R01 responden a preguntas distintas.

Priorizaría la compatibilidad comprobable en un dominio pequeño, antes de extender el evaluador a todas las familias o conectar una tecnología real. Nelson aporta la envolvente experimental y la revisión de su contrato; nuestros harness aportan backends, controles y evidencia histórica. La composición debe permitir usar ambos sin trasladar automáticamente sus conclusiones.

**Actualización del 6 de octubre:** tareas 1 y 2 realizadas en el alcance registrado en [§5.3](#r01-tasks12-status). La tabla siguiente conserva la recomendación original; los pasos 3–8 continúan pendientes.

### Orden, entregables y criterios de cierre

Las filas son paquetes recomendados dentro de las tareas existentes, **no nuevos IDs de la cola**. Todas sus ejecuciones están pendientes. La ruta propietaria sigue siendo [WORKPLAN](../feasibility/WORKPLAN.md), contrastada en commit `f065b99953b2f7fd9269950a381689e3ce550294). Los hallazgos F001–F010 explican su origen.

| Orden y prioridad | Trabajo recomendado | Entregable verificable | Dependencia y criterio de cierre | Tarea propietaria |
|---|---|---|---|---|
| **1 · inmediata** | Completar la revisión del README con las cuatro preguntas del procedimiento. Terminar fondo/lógica; después evidencia/relaciones; después edición; finalmente comprensión. Publicar cada pasada en esta misma VNext antes de avanzar. | Cuatro registros diferenciados, con ejemplos y límites; revisión cruzada de las dependencias materiales en los expedientes afectados; propuestas exactas al final. | No dar por terminada una pasada con la exploración mixta anterior. La lectura humana debe explicar propósito, entrada, salida y límites; identificar si interviene una persona o solo este asistente. Conciliación del alcance revisado en EP al terminar sus cuatro pasadas. | Revisión documental de C02; M17/P08 para sus consecuencias. |
| **2 · alta** | Fijar la correspondencia mínima entre cada harness y R01: observación visible, verdad privada, operación, identidad, autoridad, tiempo, intento, efecto, estado final, recursos y resultado. Separar las propiedades compartidas de las específicas. | Matriz por fuente y versión, con ejemplo de transformación, campos sin equivalente y pérdida de información explícita. Contrato CTv1 válido e inválido, incluidos los dos desacuerdos ya observados. | Depende de las fuentes actuales. Cierre: cada campo y predicado tiene origen y consumidor; un campo ausente conserva su condición desconocida. No sustituir los oráculos históricos ni reinterpretar sus resultados. | C02 + M17; F002/F003/F007/F008/F010. |
| **3 · alta** | Preparar la envolvente UC4 y su vínculo al sidecar R01. Usar schema **1.1.0**, package **1.1.0-r1**, fijados por versión/hash. Resolver las cinco preguntas del perfil para Nelson. | Un paquete de ejemplo completo y mapping versionado de identidades, tiempos, estados, sellos y costes; informe del validador exacto; lista corta de decisiones semánticas pendientes. | La validación técnica puede prepararse mientras se completa la matriz. Source-review y validator-pass son evidencias distintas; la admisión exige ambas y sus capacidades/casos. Solicitar revisión a Nelson solo por una comunicación autorizada. | C02; F004/F005/F009. |
| **4 · alta** | Integrar un primer perfil propio pequeño. Comenzar por CTv1/replay y controles 00K seleccionados; después adaptar un caso stateful 00I/S5 que exponga decisión, intento y efecto. | Adaptador acotado con traza nativa conservada, traza normalizada y mapping; controles positivo, frontera, rechazo, actividad legítima y dato ausente/malformado; comparación de resultados de origen y destino explicada. | Depende de la matriz; la admisión UC4 depende también del paquete. Cierre: conservar los predicados compartidos y justificar cualquier nuevo predicado R01. Las discrepancias se investigan; no se cambian expectativas para obtener verde. Piloto de instrumento, no primera tecnología T03 ni ejecución AWS. | C02 + M17; F003/F008/F009. |
| **5 · alta** | Completar fidelidad del evaluador para el perfil admitido y sus recursos. Contrastar las referencias por algoritmo y encargar solo la revisión externa que siga faltando. | Tabla cláusula → predicado → referencia → control/contraejemplo; ledger con unidades, candidato/evaluador/infraestructura separados y tratamiento del no-reference. Resultado de revisión con versión, dominio y desacuerdos. | Puede avanzar en paralelo conceptual con 3–4, sin atribuir independencia al mismo autor. Cierre acotado por perfil; la falta de cobertura relacional, paridad, dinámica o costes impide ampliar la afirmación a esos dominios. Dar crédito a las revisiones ya recibidas. | C02 + M16/M17/P08; F001/F006/F010. |
| **6 · media** | Extender el mismo mecanismo a 00L, proyección C3, diagnósticos del primer R01 y runners 00G-HF, solo cuando aporten una propiedad necesaria al siguiente perfil. | Perfiles separados, con versiones, capabilities, costes, evaluadores específicos y controles de correspondencia. Tabla de cobertura ampliada y exclusiones. | Depende del piloto y de la fidelidad demostrada. Una reparación no se renombra como inspect; una aserción UC6 no se cuenta como resultado R01. Los ensayos anteriores conservan su alcance. | C02 + M17; F002/F007/F009/F010. |
| **7 · posterior** | Registrar una campaña concreta antes de ejecutarla: pregunta, tecnología, comparadores fuertes, recursos, reset/memoria/semillas, análisis, fallos, reintentos y parada. | Registro C11 completo con versiones/hashes, alcance del instrumento admitido y criterio de decisión fijado antes de ver resultados. | C02 verificado en el dominio de la campaña y correspondencia admitida. Las ampliaciones del paso 6 que no necesite esa campaña no bloquean su registro. No cerrar C02 universalmente por admitir un perfil. | C11. |
| **8 · posterior** | Conectar y evaluar la primera realización real elegida en la cola vigente, con aislamiento comprobado. Mantener el orden de M13: human escalation/whispering y candidatos siguientes según el protocolo. | Adaptador T03 admitido; evidencia del aislamiento; trazas originales y normalizadas; resultados y costes por condición, incluidos fallos y resultados convencionales favorables. | Depende de C02/C11 y E1–E7/correspondencia de esa realización. Una ficha virtual no acredita capacidad humana real. Aplicar la regla de parada registrada; conservar y detener cuando corresponda. | M13 + T03. |

El paso 1 ordena la revisión documental. Los pasos 2–6 describen el desarrollo futuro del instrumento; sus pruebas de integración se harán en ese trabajo, fuera de esta preparación documental. Los pasos 7–8 son campañas posteriores. El orden indica dependencias; no constituye una asignación a Nelson, a otro revisor o a otro chat.

### Qué reaprovechar primero y por qué

**Primero CTv1, replay y controles 00K.** Son la forma más pequeña de comprobar trazabilidad, rechazo de datos inválidos y conservación de invariantes. Las diez coincidencias válidas previas son un punto de partida; hace falta declarar el dominio y resolver el contrato de errores antes de afirmar conformidad completa.

**Después 00I/S5 como backend de instrumento.** Permite comprobar algo que una etiqueta aislada no enseña: si una acción permitida o una reparación obsoleta llegó a producir un efecto. Mantendría su evaluador de estado/efecto y añadiría únicamente los predicados R01 que el mapping pueda justificar. Incluiría continuidad legítima para impedir que bloquearlo todo parezca éxito.

**Luego 00L, C3 y primer R01 por necesidad del perfil.** 00L aporta diseño emparejado y separación entre hechos, observaciones, reglas y evaluación. C3 aporta autoridad y temporalidad en su dominio inspect. El primer R01 aporta contrapruebas y medición acotada. Los runners sociales/dinámicos se incorporan cuando exista una pregunta colectiva definida y un ledger suficiente, después de estabilizar el piloto.

No sumaría las 379 regresiones 00K, las filas S5 y las aserciones de Nelson como una tasa de éxito R01. El entregable útil es una correspondencia verificable y una nueva evaluación con su dominio declarado.

### Primer bloque concreto que recomiendo preparar

El siguiente bloque debería producir **la matriz mínima del paso 2 y un ejemplo UC4 del paso 3**, después de publicar la pasada documental pertinente. Para mantenerlo manejable, elegiría un solo escenario 00I/S5 con cambio de autoridad o supersesión y continuidad legítima. El ejemplo incluiría la traza original, su proyección, expectativas privadas, resultado por predicado y coste por unidad.

Antes de implementar, el bloque debe responder cinco preguntas: qué ve el candidato; qué conoce exclusivamente el evaluador; qué operación cambia el destino; qué evidencia distingue intención, intento y efecto; y qué coste se cobra a cada parte. Si alguna respuesta depende de una suposición nueva, se conserva como cuestión abierta.

Como estimación de planificación, reservaría **dos bloques de trabajo** para revisar fuentes/matriz y preparar ese ejemplo. El tamaño de cada bloque y el calendario se ajustan al volumen real de discrepancias; no hay fecha comprometida ni estimación de respuesta de Nelson. El alcance de este primer bloque excluye la campaña real y la generalización a todos los backends.

### Condiciones para avanzar, parar o reformular

Se avanza al siguiente dominio cuando el mapping conserva significado y los controles apoyan el criterio anunciado. Si aparece una discrepancia, se conserva el testigo y se distingue error del adaptador, diferencia válida de contrato o falta de evidencia. Una diferencia legítima puede conducir a dos perfiles, en lugar de forzar un oráculo universal.

Si falla aislamiento, referencia, capacidades o contabilidad, el perfil no se admite para la campaña afectada. Si un comparador convencional resuelve la pregunta, se conserva el resultado y se limita la conclusión; cualquier criterio de aborto establecido por Iván para esa campaña se respeta. La ejecución manual anterior no se reactiva desde este plan ni se convierte en evidencia de EA.

El cierre recomendado tiene tres niveles: **documento revisado en su alcance**, **perfil compatible y admitido con evidencia** y **campaña real evaluada**. Cada uno necesita su propio resultado. Añadir este plan deja completa la petición documental de hoy; los tres niveles futuros mantienen sus estados reales y las cuatro propuestas siguientes continúan pendientes.


<a id="r01-compatibility-matrix"></a>
## 5.2. Tarea 2 realizada — matriz de compatibilidad y contrato de transferencia

**Codex /root, 6 de octubre de 2026 · revisión de contrato 1.0.** Se fijan correspondencias por fuente y dominio. Los nombres normalizados siguientes son **propuestas de frontera de importación**, no campos añadidos al schema UC4 ni cambios al instrumento congelado. Tarea 2 queda realizada como matriz y resolución acotada del contrato CTv1; instalar los adapters corresponde al paso 4. La tabla distingue infraestructura existente, transformación definida y admisión todavía pendiente.

### Frontera común: qué hay que conservar

| Dimensión | Registro de transferencia propuesto | Regla de conservación y falta de equivalente |
|---|---|---|
| Identidad del caso | source_corpus, source_path/commit/blob, native_case_id, native_arm_id, native_event_ref | Mantener namespace y revisión. Un P1 Q1a, un P1 de principios 00K y una postura P1 no se fusionan. Un ID generado de import lleva vínculo al ID nativo. |
| Personas/componentes | receiver_id, principal_id, source_owner, resource_id, task_id | Copiar solo identidades existentes y su rol. Un producer Q1a no se convierte en principal R01; un owner de metadata no es prueba de mandato. Ausente: null y razón. |
| Observación visible | visible_observation + source event/ref + available_at | Solo lo que el candidato recibió o podía consultar por contrato. Separar observation_at, recepción y evaluación. No inyectar expectativas, calendario futuro ni optimum. |
| Verdad privada | private_reference_ref + scope/version + reference_status | Conservar el evaluator propietario y su pregunta. El artefacto privado se consulta después del sellado; su ausencia no se suplanta por un resultado del candidato. |
| Operación | native_operation, normalized_operation, admitted_scope | Mapear por efecto y contrato, no por etiqueta. repair/restore de S5 no equivale a inspect de C3. Operación fuera de dominio: proyección no admitida. |
| Autoridad/aplicabilidad | issuer/subject/task/resource/operation/version + validity interval + native determination ref | Mandato, evidencia aplicable, calidad técnica y aprobación humana son registros diferentes. No convertir una fotografía o TTL en lease de autoridad. |
| Tiempo | native_time, clock_kind, unit, origin, observation_at/received_at/effect_at/deadline | Orden causal conservado, sin equiparar tick, step, segundo lógico y UTC declarado. Conversión solo si existe función y origen documentados. Espera y reintentos conservan horizonte. |
| Decisión/commitment | disposition, decision_basis, commitment_ref, candidate_state | COMMIT, permiso/permit y decisión EXECUTE no son effects. Preservar rechazo, residuo y supersesión de revisión; no importar postura como aceptación final. |
| Intento y efecto | attempt_ref/status, effect_ref/status, native_state_before/after, evidence_origin | Diferenciar propuesta, solicitud bloqueada, intento aceptado y cambio observado. Falta de cobertura no se vuelve false; no contar efectos a partir de confianza o texto de éxito. |
| Estado final | native_task_status y normalized_task_status separados de evaluation_status | Un queue_closed o branch_status no acredita completar toda la misión R01. Mantener INCOMPLETE/UNKNOWN y la causa; completion batch se conserva como declaration/conformance. |
| Recursos | value + unit + measured_or_modelled + source + scope, para cada magnitud | Reads, modelled_time_steps, enumeration_units, ticks y moneda no se suman como si fueran la misma unidad. Ausencia es null, nunca coste cero imputado. |
| Ledger | candidate_operations, coordination_subset, evaluator_work, infrastructure | Candidato/evaluador separados. Coordinación pertenece al coste del candidato una vez; conservar discards/retries/reuse/maintenance si la fuente los aporta y señalar lo omitido. |
| Calidad/riesgo | native_metric_definition + derivation/evidence + target_metric_status | No mapear PASS, un test count o final_generation a q/ε/riesgo. q/a requieren entrega efectiva, admisible y dentro de T; f usa campañas y no porcentaje de agentes. |
| Sellos y replay | native_artifact_hash, normalized_trace_hash, pre_oracle_seal, post_run_seal | Conservar ambos payloads; un hash normalizado nuevo no reemplaza al original. Arrays de eventos mantienen orden. Replay determinista y campaña estocástica tienen contratos distintos. |
| Resultado | native_status, normalized_status, reason, evaluated_predicates, missing_fields | Resultado nativo, error de import y verdict R01 son ejes separados. Regresión verde puede conservar un escenario fallido. Unknown nunca se convierte en PASS por normalizar. |

### Matriz por familia — observación, identidad, operación y verdad

| Fuente fijada | Correspondencia concreta | Autoridad/tiempo y límite de la proyección |
|---|---|---|
| **Q1a / CTv1** — source blobs del registro; pre-registration v0.5 y replay corregido | observation.proposition_id/scope_id/reports/registry → observación visible; report_id/producer_id/upstream_source_id → IDs tipados de reporte/productor/fuente. candidate.dependency_assessment y posture → assessment/disposition nativos; oracle_reference_v05 → verdad de dependencia, separada. | processing/deadline/freshness **steps**. Registro de fuentes no es mandato. configuration_id B1/B3 es brazo del fixture, no tecnología externa ni posture R01. Operación: recepción, registry join y handoff; no ejecución de una ruta material. |
| **00K P1–P6** — suite, manifest y fixture propio | principle/fixture/test identity → namespace de control. La pregunta/expectativa del fixture permanece con su evaluator. run_all.Harness(label,directory,expected,evidence_class) describe agregación de pytest, no candidate_result. | No hay un único receiver/principal/reloj/API de toda la suite. Se elige un kernel y sus entradas; los campos de actor/efecto ausentes se declaran. Regla anti deny-all o falsifier es propiedad del control, no una observación universal. |
| **00L** — A08 y paquete 00E–00J | F/O/K/E → hechos, observación, regla y oracle separados. source_id/source_version/observed_at/depends_on/authority_id/gate_id/disposition/owner/deadline/residual conservan su papel. D, X y ? mantienen respectivamente deducción, posibilidad no ejecutada y no-determinado. | Congelar scope/ventana/arm por anexo. Un action_effect de una tabla de papel no se convierte en evento server-observed. H0/H1/H2 son brazos locales. Parámetros no fijados siguen ?/null con razón. |
| **00I/S5 stateful** — model/reproduce y resultados | case.id/mode → caso/brazo. Intent.id/target/desired_generation/grant_expires y Permit.id/intent/revision/expires → intent/permit vinculados. trace[].event/at → eventos; Sources.read y manifest → evidencia visible. oracle.expectations y reproduce.evaluate → predicados privados de disposition/applied/final_generation. | Autoridad/owners y grant son estipulados; no autenticados contra organización real. Segundo lógico con origen 120; guard a 2520, dispatch por caso y horizonte 2525 en recovery. Operación restore de generación, no inspect. Reset de World por caso; SQLite testigo tiene otra frontera. |
| **C3** — README/core y estado de adaptación | world.grants/applicability/messages/original_authority → hechos de referencia; trace.events/coverage/closed/observed_until → observación y cobertura; event.id/kind/decision/attempt/basis → relaciones causales. subject R, tasks T0/T1, resources X/Y, operation inspect quedan explícitos. | Validez from/until/revoked_at y applicability.at se conserva. bool/None y record_status COMPLETE/INCOMPLETE no se aplastan. evidence_rule/minimum_roots son del perfil. C3 no suministra optimum_J ni completo ledger R01. |
| **Primer R01** — M02/M10/F-W históricos | M02 graph.nodes/edges/benefit, worlds.id/chi/weight, thresholds y profiles/operations → un perfil histórico etiquetado. chi y I/P siguen ocultos; query_state/certificate solo entregan evidencia pagada. M10 distingue z_complete, a, q, J_partial y v_exec. | Costes/duraciones racionales **strings**; world law/AVG/WC son definiciones, no muestreo real. M02 H=32 es cap de ese submodelo. TRILEMMA_CONTRACT extiende F/W con su propio alcance; no se extrapola el cap ni se adjudica una tecnología por nombre. |
| **00G-HF runners** — representante dinámico congelado y receiver nativo | run_episode.condition/profile/seed; messages/transmissions/decisions/ledger/effects/records/epoch_states. project devuelve agent/epoch/route/world/trace/result: se conserva cada vínculo y la proyección inspect C3. Native journal es evidencia distinta de normalized TRACE. | draw indexa seed/agent/step/purpose. Cache snapshots no son permisos actuales. Cuatro checkpoints comparten historia; red es unidad de repetición. population_result NOT_ASSESSED y A25 PENDING_REVIEW no cambian al importarse. Los demás runners requieren su perfil específico. |
| **Nelson UC4/UC6** — schema 1.1.0, ZIP 1.1.0-r1 y mapping atribuido | UC4 submission_id/cases[].id/adapters[].id/version/source_ref_ids/semantic_owner → identidad del experimento/import. cases[].source_records[].data son records del contributor; cases[].events tienen logical_time/actor_id/type/origin/payload; assertions se mantienen privadas durante ejecución según perfil. | timeValue conserva clock/origin/role; un timestamp sintético no pasa a medición humana real. field_mappings permite copy/enum_map y target_pointer bajo /adapters/: transformaciones compuestas precisan reviewed_plugin y revisión propia. R01 sidecar no se incrusta arbitrariamente en root con additionalProperties=false. |

### Matriz por familia — intento, efecto, recursos y resultado

| Fuente | Datos nativos que se conservan | Transformación permitida y hueco que impide admisión completa |
|---|---|---|
| Q1a | runtime_events y candidate_status; burden.processing_steps/modelled_time_steps; resolución de roots, residual y handoff. | Se transfiere evidencia de assessment, no completion/quality de ruta. RUNTIME_ERROR se conserva como error del run original; no se transforma retrospectivamente en fallo sustantivo del producto. |
| 00K | test expectation, reparaciones/ablaciones, exit code y counts por family. | No hay efecto material común ni coste empírico por candidato. Se preserva el resultado del falsifier/TRUE SUBSTITUTE; no se suma 379 como población de R01. |
| 00L | disposition/plazo/owner/residual, etiquetas D/X/?, campos de recursos declarados o ausentes. | Observación ejecutada exige source event real. NO CONCLUSION permanece; null con razón en compute/communication/wait/human cost. H1/H2 requieren mapping y fairness por anexo. |
| 00I/S5 | guard_decision, executor events, queue_closed; applied/effects/final_generation/final_state; control_burden.source_reads/elapsed_seconds. | EXECUTE es disposición y APPLIED requiere writes/effect; DENY puede ser continuidad fallida. No conversion de reads a operational_cost sin tariff declarado; elapsed_seconds es lógico. 44/8 escenarios y 49 regresiones son denominadores diferentes. |
| C3 | unsupported_commitment/unauthorized_attempt/inadmissible_attempt/unauthorized_effect/inadmissible_effect/task_completed/legitimate_completion/safety_pass/operational_pass. | Conservar cada predicado y unknown por cobertura. operational_pass depende de seguridad+continuidad de su misión; no calcula la calidad óptima o el coste de una repair S5. hc_causal_claim NOT_ASSESSED sigue fuera. |
| Primer R01 | Costes setup/review/decide/execute/query/reuse/wait; cadenas de efectos/violación permanente; success y condiciones de M10 por contrato. | Parsear racionales exactamente a una representación declarada, sin float CTv1 ni redondeo silencioso. Permiso conocido M incluido en setup no da gratis el binding oculto. Countercontrols no son la campaña actual. |
| 00G-HF | Intentos, environment effects, recibos, C3 y ledger por agente/checkpoint; usage/tiempo nativo cuando realmente registrado. | Segundos/tokens reales del receiver, ticks del simulador y costes estipulados no se equiparan. C3 por checkpoint no define estadística colectiva. Campaña dinámica completada conserva éxito convencional FRESH y sus límites de continuidad. |
| Nelson UC4/UC6 | Assertions esperadas/observadas, mapping source-owner, resultado y errores por caso, review statuses y capacidades. | Un assertion-pass indica preservación de un predicado suministrado; no ejecución/authority/human authenticity nueva. Técnica, preparer y contributor review se registran por separado. No validator-pass ni source-approval de R01 por esta matriz. |

### Ejemplo verificable de conservación de significado — S5

Se leen tres filas **ya registradas** en results/results.json; no se ejecuta un caso nuevo:

| Caso nativo | Observación preservada | Import correcto |
|---|---|---|
| continuity | disposition EXECUTE; applied=true; generation 216; scenario_pass=true | Acción legítima efectivamente aplicada en el modelo. No inferir optimum_J ni coste monetario. |
| patch_b_supersedes | disposition DENY; applied=false; generation 218; scenario_pass=true | Protección de la corrección nueva; el rechazo forma parte del resultado esperado. No marcar tarea R01 COMPLETED solo por DENY. |
| unbound_race | esperado DENY/no effect/217; observado EXECUTE/applied/216; scenario_pass=false | Conservar intento/efecto indebido y fallo de escenario. regression_pass del lote no lo transforma en seguro. |

La proyección registra native_case_id y las tres afirmaciones separadas. Los predicados de una futura ruta R01 quedan no evaluados hasta fijar un mundo, objetivo/beneficios, referencia, recursos y deadline correspondientes. Este es el ejemplo de transformación de la tarea 2; no el paquete completo UC4 de la tarea 3.

### CTv1: diferencias resueltas en una frontera acotada

**Decisión de contrato documentada:** usar el perfil de revisión **R01-CTv1-IMPORT-REVIEW-1** antes de cualquiera de los dos helpers. Mantener ambos helpers y sus bytes congelados. No se fuerza la equivalencia de sus entradas generales.

| Condición | Conducta nativa observada/inspeccionada | Resolución de import |
|---|---|---|
| Root objeto/mapping | Ambos serializan; añaden/reescriben canonicalization_version CTv1 en copia. | Exigir objeto; conservar payload y metadata del origen. No mutar al caller. |
| Root lista de pares | Q1a CanonicalTraceError; R01 dict-conversion acepta. | Rechazar antes de serializar con REJECTED_INPUT / ROOT_NOT_OBJECT. La aceptación nativa de R01 no autoriza importar ese shape. |
| Set-like sin stable key / item no objeto | Q1a encapsula TypeError/KeyError; R01 puede propagarlos. | Prevalidar y usar MISSING_STABLE_KEY común. Preservar clase nativa como diagnóstico, no como status de tecnología. |
| Claves heterogéneas/duplicadas de colección | El helper puede ordenar o fallar según tipos; empates preservan orden de entrada. | En este perfil exigir stable key string no vacío y único; rechazar STABLE_KEY_NOT_STRING o DUPLICATE_STABLE_KEY. Restricción propia de import, no corrección retrospectiva de CTv1. |
| Dict con keys no-string | sorted puede fallar antes de la validación individual. | Validar keys antes de ordenar; NON_STRING_KEY común. |
| Float/tuple/objetos en payload semántico | Float rechazado; tuples aceptadas por helpers pero fuera de este perfil JSON. | Payload de import usa objetos/listas, strings, bool, null e ints. Decimales semánticos como string bajo formato del productor; sin coerción ni redondeo. |
| Arrays de eventos | Ambos conservan orden salvo rule explícita set-like. | Nunca ordenar cronología. Solo colecciones declaradas como sets con key válida; una regla que no encuentra su colección se rechaza. |
| Metadata excluida / paths | Mismo closed excluded set y paths relativos POSIX. | No añadir nuevas exclusiones; observed_at/receipt/effect time siguen semánticos. Rechazar absolute/local path y ..; preservar hash de bytes nativos aparte. |
| Fallo inesperado del serializador | Distinto de dato inválido prevalidado. | SERIALIZER_ERROR con diagnóstico; no PASS ni error sustantivo del candidato atribuido. |

[Prototipo de revisión](../../../../../../governance/review/r01-oracle-tasks12-2026-10-06/ctv1_import_contract_review.py) y [28 comprobaciones](../../../../../../governance/review/r01-oracle-tasks12-2026-10-06/CTv1_IMPORT_REVIEW_RESULT.json) quedaron publicados durante la pasada de evidencia. Se verificaron diez ejemplos válidos, catorce inválidos y cuatro propiedades conductuales. Las dos diferencias históricas se reprodujeron en los helpers originales y quedan amortiguadas por prevalidación en el prototipo. No equivale a una prueba para todos los objetos de Python/CTv1 ni a instalación o admisión en C02.

### Resultado de la tarea y pendientes de ingeniería

La correspondencia documental queda fijada para las ocho familias representadas: cada dimensión tiene origen, transformación o ausencia explícita. Son compatibles para composición **con perfiles y adapters**, con reutilización ya observada de CTv1 y patrones; no intercambiables íntegramente como runners/oracles.

Antes de instalar un perfil habrá que validar su paquete UC4, obtener la revisión semántica requerida, congelar su adapter y probar la correspondence con controles del dominio. Esa es la tarea 3/4 y las obligaciones de C02/M17, no trabajo declarado ejecutado por esta matriz. La independencia, contabilidad completa y campaña real siguen en los pasos siguientes.

<a id="r01-tasks12-status"></a>
## 5.3. Cierre de las tareas 1 y 2 y conciliación acotada

**Tarea 1 realizada:** cuatro pasadas diferentes del README publicadas en orden, con relaciones materiales registradas en doce VNext vecinas. Comprensión humana significa aquí simulación del mismo asistente; revisión humana/externa no realizada.

**Tarea 2 realizada:** matriz por dimensión/familia, ejemplo conservador de S5 y contrato CTv1 resuelto en el perfil acotado de revisión, con prototipo y 28 comprobaciones. La instalación del adapter y su admisión permanecen pendientes.

La conciliación entre argumento, fuentes, formas de lectura y matriz mantiene una idea común: evaluar lo que una realización pudo observar y causar frente a una referencia acotada, cobrando sus recursos sin regalarle verdad privada. Se conservan cuatro límites: diseño no es ejecución; serialización no es semántica; campo de resultado no es entrega efectiva; controles correlacionados no son población independiente.

No se encontraron destinos locales ausentes en las adiciones de esta entrega tras su comprobación estática. Sí hay **trazas de versión temporal** que requieren interpretación: README dinámico frente a resultados posteriores; pointers históricos de freeze; trackers de primer R01 frente a la cola vigente. Se documentan, sin reemplazar resultados o editar originales.

La consecuencia para la lectura de conjunto queda registrada en la [VNext de Ecosystem Positioning](../../../../../../architectural-contributions/ecosystem-positioning/README_VNext.md). Esta es conciliación del alcance README/matriz y sus relaciones seleccionadas, **no la conciliación final del corpus entero**: los vecinos solo recibieron examen cruzado parcial y las otras tareas globales siguen abiertas.


**Verificación del método al cierre:** se leyó también la adición vigente 1.3 del procedimiento, blob `f046348549232e05f85d008abdb49b65f8815b5e`, presente en el corte de cierre `2db5a8c17f58008f9268c23c681ba6e14c8dfbdc`. Conserva el ciclo de cuatro pasadas y añade tres niveles de lectura/redistribución examinada en los README propietarios. Esta entrega no redistribuye archivos, no cambia propiedad y no crea nuevos niveles de navegación: las doce fichas/VNext son controles locales de documentos existentes. Las propuestas de la matriz son fronteras de importación; no reorganización del corpus. El cambio paralelo del procedimiento se preserva y se registra en evidencia.

**Siguiente tarea del plan:** 3, paquete UC4 y revisión de su mapping. Siete deltas del README esperan decisión por ID. C02/C11/T03 no cambian de estado técnico por finalizar esta documentación.


<a id="r01-overview-review"></a>
## 5.4. Visión general revisada para retomar el oráculo

**Revisión de la conversación, Codex /root, 6 de octubre de 2026.** Esta sección reúne los comentarios que antes quedaron en el chat. Explica el conjunto; la [matriz](#r01-compatibility-matrix) conserva el detalle de campos y los registros de §3 explican cada lectura. Las recomendaciones son propuestas de trabajo.

### Qué tenemos y qué queremos llegar a tener

Tenemos un **instrumento R01 parcial, ejecutado sobre controles construidos**, varias baterías y harness propios aprovechables y un puente documental hacia UC4. El resultado que buscamos es poder ejecutar una tecnología en un escenario definido, registrar qué pudo ver, decidir y hacer, y valorar después la entrega permitida, su calidad y sus recursos frente a una referencia apropiada. Esa cadena integrada todavía necesita ingeniería y verificación.

El **oráculo** es el evaluador que conoce la referencia y juzga la evidencia. El **harness** prepara el caso, invoca el candidato, registra el recorrido y entrega evidencia al evaluador. El **adaptador** conecta una tecnología o un escenario con ese contrato. El **sidecar** guarda información R01 adicional, incluida la referencia privada, vinculada al experimento. Un **perfil** declara el dominio en que esas piezas y sus criterios tienen sentido.

| Pieza disponible | Para qué sirve | Qué falta para utilizarla en la cadena siguiente |
|---|---|---|
| Especificación y contratos R01 | Definen tarea, autoridad, observaciones, operaciones, presupuesto y plazo. | Correspondencia cláusula → predicado → evidencia en el perfil elegido; M17 conserva la fidelidad pendiente. |
| Referencia privada y evaluador C02 limitado | Calculan admisibilidad y óptimo en los mundos finitos implementados. | Completar y contrastar únicamente el dominio que vaya a evaluarse; revisión independiente faltante M16. |
| Harness batch, interactivo y broker | Ejecutan controles, restringen vistas y registran operaciones según su modo. | Conectar un backend/adaptador admitido; el self-test no representa una tecnología real. |
| Trazas, sellos y contabilidad | Permiten identificar evidencia y distinguir recursos del candidato y del evaluador. | Mediciones y unidades válidas para el backend real, aislamiento efectivo y evidencia fiable del destino. |
| Baterías Q1a, 00K, 00L, S5, C3 y antecedentes R01/00G-HF | Aportan controles de procedencia, invariantes, temporalidad, estado, recuperación y contrapruebas. | Adaptadores y correspondencia por predicado; conservar el resultado original y explicar el nuevo. |
| Trabajo UC4/UC6 y calibraciones de Nelson | Aporta contrato experimental, mappings y patrones de controles reproducibles. | Paquete R01 contra schema fijado, revisión semántica y admisión explícita del perfil. |
| Contrato y plantilla de tecnología real | Preparan la admisión de una realización identificada. | Registro completo, aislamiento y capacidades comprobados; C11/T03 permanecen posteriores. |

El [registro v0.9](SELFTEST_RECORD_v0.9.md) conserva SELFTEST_PASS, con resultados intencionalmente mezclados: dos PASS, tres FAIL y un INCONCLUSIVE. El instrumento pasó porque reconoció también los controles negativos y la falta de referencia. No son seis éxitos de una tecnología. Los 28 microchecks del contrato de importación de §5.2 son otra evidencia, documental y de prototipo: no se suman a ese run ni acreditan un adaptador instalado.

### Qué significa C4 aquí y para qué utilizar UC4

La conversación empleó «C4». **Esta revisión lo interpreta como UC4 de Nelson**, por el contexto; no como C02 de R01 ni como el C3 antiguo. Si el referente era otro, se debe corregir esta interpretación antes de implementar una correspondencia.

UC4 plantea defensa federada entre organizaciones que conservan su gobierno. Propone conectar hallazgos, evidencia y decisiones locales mediante contratos y adaptadores versionados, con casos positivos, de frontera y rechazo. Su roadmap distingue Stage0–1 iniciales de extensiones posteriores. El issue presenta una implementación de referencia planificada; no acredita una federación Stage1 desplegada. [Fuente: UC4, requisitos 22–24 y madurez](https://github.com/FG-TIDA/use-cases/issues/4).

**Uso recomendado para R01, inferencia de esta revisión:** que UC4 sea la envolvente del experimento y R01 un perfil importado con su sidecar privado. Así se pueden atribuir fuentes, declarar capacidades y revisiones, conservar determinaciones ajenas y conectar casos sin imponer a Nelson todo el formato R01. [Puente existente](UC4_INTEROPERABILITY_PROFILE.md).

UC4 no reemplaza la referencia matemática de R01, no determina el mejor recorrido por sí mismo y no concede autoridad para actuar sobre otra organización. Tampoco prueba capacidad humana efectiva, eficacia EA, corrección universal o preparación para producción. Un PASS de schema confirma estructura dentro del contrato validado; una revisión de contributor confirma un mapping en su alcance; la admisión y la ejecución requieren evidencia adicional. Esta separación procede del puente actual y de sus estados, no de una garantía atribuida a Nelson.

### Qué piezas hay que conectar

```text
Pregunta, perfil y expectativas fijados antes del run
                 |
        Paquete experimental UC4
                 |
       Adaptador de caso/tecnología
                 |
     Harness + broker + entorno de destino
                 |
       Registro nativo y mediciones
                 |
        Mapping y traza sellada
                 |
    Evaluación R01 con referencia privada
                 |
  Resultado por predicado + recursos + límites
```

Es una **composición propuesta**. La referencia privada se fija o compromete antes del run, queda fuera del candidato y se utiliza para evaluar después de registrar/sellar su recorrido. El diagrama no implica calcular expectativas mirando lo que hizo el candidato.

Las conexiones que necesitan evidencia son estas:

1. **Experimento → sidecar:** identidades inequívocas de experimento, caso, versión y evidencia; schema UC4 y campos R01 sin filtración de verdad privada.
2. **Contrato → entorno:** capacidad realmente disponible para observar, revisar, comprometerse y ejecutar en ese dominio. Una capacidad declarada no demuestra que esté implementada.
3. **Entorno → registro:** decisión, intento, efecto y estado final diferenciados. El relato del candidato no sustituye la medición del destino.
4. **Registro nativo → traza común:** mantener tiempos, orden causal, autoridad, referencias y datos ausentes; conservar el original para examinar discrepancias.
5. **Traza → evaluación:** aplicar únicamente los predicados justificados para el perfil. Si falta evidencia o referencia, conservar el resultado no resuelto.
6. **Medición → conclusión:** recursos del candidato, del evaluador y de infraestructura separados, con unidades y plazo explícitos. Los costes sintéticos anteriores no son euros, tokens ni latencia de producción.

### Compatibilidad con los harness anteriores

No hace falta rehacer todo lo anterior ni sustituir sus oráculos. Hace falta reutilizar mecanismos compartidos y demostrar la correspondencia del caso elegido.

| Material propio | Reutilización razonable | Límite que debe conservarse |
|---|---|---|
| Q1a / CTv1 | Serialización, hashes, replay y testigos de dependencia de fuentes. | Compartir bytes válidos no equivale a compartir todos los errores ni todos los predicados. El perfil de importación de §5.2 sigue siendo un prototipo separado. |
| 00K | Regresiones semánticas, falsadores y controles frente a alternativas convencionales. | Su runner y sus invariantes no constituyen un adaptador R01 genérico; las 379 comprobaciones no son 379 agentes evaluados. |
| 00L | Diseño emparejado, trazabilidad y separación de hechos, observaciones, reglas y evaluación. | Lo deducido, posible, desconocido y ejecutado mantiene estados distintos; no importar costes como una unidad universal. |
| 00I / S5 | Backend con estado, supersesión, reparación, recuperación y continuidad legítima. | Mantener decisión/intento/efecto; la simulación local no prueba atomicidad distribuida ni rendimiento de producción. |
| C3 anterior asociado al corpus de UC21 | Predicados de autoridad, compromiso, intento, efecto y completion en su dominio inspect. | No es el óptimo R01 ni un ledger completo; no confundir el instrumento C3 con un brazo comparador que también se llame C3. |
| Primer R01 y anexos parciales | Contrapruebas, diagnósticos y controles acotados ya preservados. | Son antecedentes y ensayos de su versión; no reinstauran la cola antigua ni prueban realización real. |
| 00G-HF dinámico y nativo | Diseño experimental, redes/relays, replay y evidencia preservada por campaña. | Hay resultados dinámicos posteriores al README preparatorio: no repetirlos como «no ejecutados». Tampoco convertir simulación o baseline en comparación EA. |
| Nelson UC6 / Themes13–16 | Patrones de corrupción, malformed, bindings ausentes, replay y orden. | Los resultados y la autoridad semántica siguen siendo de su escenario; no transferirlos como resultados R01. |

La compatibilidad documental es considerable para infraestructura y selectiva para semántica. La compatibilidad de una **integración ejecutada** permanece por demostrar. El ejemplo S5 de §5.2 es la prueba de lectura de la correspondencia, no una ejecución nueva de esta entrega.

### Límites que condicionan el siguiente paso

- **Dominio:** mundos finitos y referencias actuales no cubren por defecto ciclos, dinámica colectiva, todos los canales o políticas. Cada ampliación necesita contrato de terminación y cobertura.
- **Efecto:** el batch contrasta conformidad de selección; no acredita entrega ejecutada. El interactivo requiere evidencia privada coherente del entorno.
- **Calidad y coste:** ruta elegida, entrega admisible a tiempo, calidad y recursos son preguntas distintas. Un agente que bloquea todo puede fallar continuidad legítima.
- **Aislamiento:** un sello prueba identidad de la traza; no prueba que el candidato estuviera aislado del evaluador.
- **Referencia:** dos implementaciones del mismo mantenedor permiten contraste, con posibilidad de omisión común. M16 conserva la cobertura externa faltante.
- **Interoperabilidad:** alineación documental, schema validado, source-review y admisión no son equivalentes.
- **Transferencia:** desconocido permanece desconocido; no traducirlo a false, cero, permiso o éxito.
- **Conclusión:** self-test, campaña sintética, integración de perfil y realización real tienen alcances distintos. Este expediente no cierra C02 ni el corpus global.



### Qué reutilizar de terceros y qué conservar como trabajo propio

La selección siguiente fue contrastada con documentación primaria el **6 de octubre de 2026**. Son opciones para paquetes de trabajo dentro de C02/M17; ninguna está integrada por esta revisión. Antes de implementar se fijarán release o commit, dependencias, licencia del código y de los datos elegidos, subconjunto de casos y capacidades del entorno. Las páginas vivas enlazadas no equivalen a una versión congelada de ejecución.

<a id="r01-thirdparty-test-reuse"></a>
| Opción y función | Qué podemos aprovechar | Trabajo necesario y límite | Prioridad recomendada |
|---|---|---|---|
| [JSON Schema Test Suite](https://github.com/json-schema-org/JSON-Schema-Test-Suite) + [python-jsonschema](https://python-jsonschema.readthedocs.io/en/stable/) | Suite de conformidad del validador y biblioteca para comprobar documentos contra el schema exacto. | Seleccionar el dialecto que declara el schema UC4 y configurar sus referencias/formatos. La suite no contiene nuestras expectativas de dominio ni valida semántica R01. | Primera: evitar inventar un validador general. |
| [Hypothesis, pruebas con estado](https://hypothesis.readthedocs.io/en/latest/stateful.html) | Generación de secuencias y reducción de un fallo a un testigo pequeño. | Definir modelo, operaciones e invariantes propios, por ejemplo revisión → supersesión → intento. No es una batería R01 lista para ejecutar ni garantía de cobertura exhaustiva. | Primera, tras fijar el perfil y sus invariantes. |
| [ToolSandbox](https://github.com/apple-aiml-research/ToolSandbox) | Herramientas con estado y evaluación por snapshots e hitos ordenados en un DAG. | Elegir un caso y mapear operaciones/efectos. Su score de similitud de hitos no es el óptimo admisible R01; conservar ambas evaluaciones. | Segundo bloque: caso pequeño con efectos observables. |
| [AgentDojo](https://github.com/ethz-spylab/agentdojo) | Tareas y controles de ataques/defensas de prompt injection. | Separar éxito de tarea legítima y éxito del ataque; adaptar fronteras de confianza y registrar capacidades/modelo. Su API evoluciona y requiere versión fijada. | Cuando el perfil incluya esa amenaza. |
| [τ-bench, repositorio tau2-bench](https://github.com/sierra-research/tau2-bench) | Simulación de interacción usuario–agente–herramientas con políticas y tareas por dominio. | Elegir dominio y modo, fijar simulador y política, registrar efectos y coste de cada parte. El cumplimiento del benchmark no es autorización general ni medida equivalente R01. | Después del piloto propio; solo si añade una pregunta necesaria. |
| [OR-Tools CP-SAT](https://developers.google.com/optimization/cp/cp_solver) | Posible referencia adicional para optimización discreta acotada. | Formalizar fielmente restricciones y objetivo; su aritmética es entera. Una solución FEASIBLE no acredita OPTIMAL; límite o UNKNOWN no acredita inexistencia de solución. No determina autoridad ni hechos omitidos del modelo. | Condicionada a un perfil que justifique ese modelo. |

Podemos reutilizar **implementaciones, motores, casos y métodos de evaluación**. Debemos definir nosotros la correspondencia con R01, la verdad privada del caso, los permisos temporales aplicables, la entrega admisible, los recursos y el criterio de conclusión. Eso evita construir toda la infraestructura desde cero y evita importar un significado que la prueba externa nunca examinó.

No recomiendo descargar e integrar todas las opciones a la vez. Empezaría por validación estructural y generación de secuencias, conservaría S5 como primer caso de correspondencia y elegiría después **una** fuente de escenarios externos. ToolSandbox sería la primera candidata si se necesita observar cambios de estado; AgentDojo si la pregunta concreta es prompt injection; τ-bench si la pregunta requiere políticas y cooperación con un usuario. CP-SAT solo se justifica si ofrece un contraste pertinente del modelo, no por sumar un segundo solver.

### Cómo decidir si una batería se transfiere correctamente

El expediente de cada importación deberá conservar versión y caso original, licencia aplicable, entrada y resultado nativos, mapping, traza normalizada, expectativas privadas y resultados separados por predicado. Debe permitir explicar una discrepancia sin cambiar las expectativas después de ver el resultado. La comparación es **original → transformación → predicado destino**, no una suma de todos los PASS.

Propongo esta batería mínima de correspondencia, todavía no ejecutada:

| Control | Qué debe distinguir o conservar |
|---|---|
| Positivo legítimo | Permiso, efecto esperado y entrega dentro del contrato; bloquearlo no es éxito. |
| Frontera temporal | Mismo acto antes y después de expiración/supersesión; preservar evaluación al tiempo aplicable. |
| Rechazo | Intento fuera de mandato o contexto; decisión y efecto examinados por separado. |
| Abstención permanente | Ausencia de daño no se convierte en tarea completada. |
| Orden causal y reset | No ordenar una secuencia cronológica como un conjunto; declarar cuándo reordenar casos independientes es válido. |
| Replay | Repetir bajo el estado/reset declarado y comparar los campos prometidos, sin reclamar determinismo de cualquier tecnología. |
| Binding/identidad ausente | Rechazo o no resolución explícitos según contrato; no desaparición silenciosa del caso. |
| Dato ausente o malformed | Separar incertidumbre, entrada rechazada y fallo de infraestructura. |
| Referencia ausente o limitada | Mantener INCONCLUSIVE cuando no se puede decidir el predicado; no fabricar un óptimo. |
| Coste y plazo | Contrastar medición con declaración y conservar candidato/evaluador/infraestructura en ledgers distintos. |
| Aislamiento y verdad privada | El candidato no recibe expectativas ni referencia; el sello solo cubre integridad de la traza. |
| Resultado nativo frente al importado | Misma conclusión solo donde el mapping conserva el mismo predicado; justificar diferencia legítima o registrar fallo. |

**Ejemplo para retomar:** escoger el caso S5 ya documentado en §5.2, conservando la evidencia anterior. Una reparación vigente debe poder actuar; la misma reparación después de supersesión debe ser rechazada sin efecto; el control de carrera que antes produjo efecto indebido debe seguir visible como fallo histórico. La nueva adaptación añade sus controles y su resultado con una nueva versión. La fidelidad consiste en detectar esa diferencia, no en convertir el fallo preservado en PASS.



<a id="r01-resume-work"></a>
### Cómo retomar: estado actual y siguiente bloque recomendado

**Precisión respecto al plan original de §5.1:** tareas1/2 están realizadas en el alcance documental y del prototipo allí registrado. Las frases originales que presentaban toda ejecución pendiente o proponían comenzar por la matriz son historia del plan. No hay que repetir esos dos entregables como trabajo inicial; sí revisar la correspondencia si cambia la fuente o se implementa el adaptador.

**Siguiente resultado que recomiendo preparar:** un paquete de ejemplo UC4/R01 vinculado a **un caso S5 pequeño**, con versión y expectativas fijadas. Pertenece al paso3 del plan, con el piloto del paso4 como dependencia posterior o trabajo coordinado. La matriz existente es la entrada; no se inventa otra cola.

| Pendiente real | Entregable que permitiría avanzar | Criterio para declarar ese avance |
|---|---|---|
| Paquete y enlace al sidecar — paso3, C02 | Experimento completo contra schema UC4 fijado, mapping versionado e identidades de caso/sidecar/evidencia. | Informe del validador exacto y separación visible de cuestiones semánticas sin resolver. Un PASS estructural no cierra admisión. |
| Revisión semántica de la frontera — C02/M17 | Respuesta sobre las cinco preguntas de UC4_INTEROPERABILITY_PROFILE y alcance mutuamente acordado. | Evidencia auténtica del contributor; no inferir respuesta desde un borrador o solicitud. Preparar el material; comunicación solo cuando esté autorizada. |
| Piloto propio — paso4, C02/M17 | Adaptador S5 acotado, registro nativo y normalizado, controles y diferencias de resultado explicadas. | Correspondencia probada en los predicados declarados, incluidos rechazo y continuidad legítima. |
| Fidelidad y referencia — paso5, M16/M17 | Tabla cláusula/predicado/evidencia, revisión faltante y ledger por unidad. | Cada afirmación del perfil tiene control y límite; reconocer revisiones recibidas, cubrir solo los vacíos. |
| Generación y escenarios externos seleccionados | Perfil de mutaciones y, si aporta valor, un caso externo versionado. | Aporta una propiedad necesaria y mantiene la evaluación original separada de R01. No bloquea el piloto por una integración masiva. |
| Ampliaciones de familias — paso6 | Perfiles adicionales únicamente cuando el siguiente experimento los necesite. | Sin pérdida silenciosa de significado ni importación de tasas agregadas. |
| Registro y tecnología real — pasos7/8, C11/T03 | Campaña pre-registrada y realización identificada con capacidades/aislamiento. | C02 suficiente para su dominio, correspondencia admitida y condiciones de ejecución satisfechas antes del run. |
| Decisiones sobre el README protegido — siete deltas | Decisión concreta por ID y revalidación del ANTES contra la fuente actual. | Incorporación posterior separada de esta auditoría. No es un requisito para que exista la presente revisión. |

Antes de ejecutar el piloto, dejaría respondidas cinco preguntas en su expediente: **qué ve el candidato, qué queda privado, qué operación produce el efecto, qué evidencia lo confirma y qué recursos paga cada parte**. Si falta una respuesta, el hueco se conserva como condición pendiente; no se rellena con una suposición favorable.

El primer bloque termina con **un ejemplo trazable y una lista corta de decisiones abiertas**, no con «UC4 compatible» en general. Su aceptación técnica y semántica puede permitir después admitir ese perfil. La extensión del evaluador y la campaña real conservan sus etapas propias. No se asigna aquí trabajo a Nelson, otro agente o una persona sin acuerdo.



### Cierre de esta ampliación y asuntos que permanecen abiertos

La petición IVAN-R01-ORACLE-20261006-04 queda atendida como **revisión documentada de estos comentarios**: cuatro lecturas distintas, publicadas sucesivamente, relato del conjunto, límites, reutilización propia y de terceros, controles de correspondencia y siguiente bloque. Es trabajo de este mismo asistente, con relectura simulada; no se cuenta como participación humana ni auditoría independiente.

Se verificaron navegación añadida, anclas y preservación. El [registro técnico de esta ampliación](../../../../../../governance/review/R01_ORACLE_OVERVIEW_REVIEW_2026-10-06.json) permite volver al corte y a sus fuentes. Las 58 fuentes técnicas contrastadas y los 30 artefactos del freeze conservan sus blobs; el bloque original de siete deltas permanece íntegro. No se ejecutó el harness científico, instalaron benchmarks ni realizaron llamadas de modelo por esta revisión.

Quedan abiertos: confirmar el referente si «C4» no era UC4; paquete/validator R01, review del contributor y admisión; piloto y fidelidad por perfil; cobertura independiente faltante; mediciones y aislamiento de realización real; las siete decisiones sobre el canon; examen completo de consumidores/fuentes vecinas y conciliación global. Ninguno se elimina por haber terminado esta entrega documental.


## 6. Propuestas quirúrgicas — al final, incorporación pendiente

Todas las propuestas siguientes pertenecen exclusivamente a `R01-ORACLE-C02-README`; fuente auditada: ruta de §1, commit `40cb19682fd1211d2c07e81ecd0242b56d425918`, blob `282d97ed967898a086303927872fbdfcaf37dd70`, estado editorial del 5 de octubre de 2026. Instrucción de preparación: **IVAN-R01-ORACLE-20261006-01**. Cada TEXTO ANTES aparece una sola vez en la fuente fijada. **Ninguna propuesta se ha aplicado.**

### R01-ORACLE-DELTA-001 — Separar versión del esquema y del paquete UC4

**ID y estado:** R01-ORACLE-DELTA-001 · propuesta, incorporación pendiente.  
**Documento/fuente:** `R01-ORACLE-C02-README`, `research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/README.md`; commit `40cb19682fd1211d2c07e81ecd0242b56d425918`; blob `282d97ed967898a086303927872fbdfcaf37dd70`; versión editorial no declarada, estado 5 de octubre de 2026.  
**Instrucción:** IVAN-R01-ORACLE-20261006-01.  
**Auditorías/hallazgos:** AUD-001/AUD-002; R01-ORACLE-F004, R01-ORACLE-F005.  
**Localización:** Upstream sources and attribution · única entrada de public experiment schema.  
**Tipo:** sustitución editorial propuesta.

**TEXTO ANTES**

```markdown
- UC #4 public experiment schema 1.1.0-r1, adding assessment time, consumed-determination reference, provenance, capabilities and separate review states  
  https://github.com/FG-TIDA/use-cases/issues/4#issuecomment-5871266911
```

**TEXTO DESPUÉS**

```markdown
- UC #4 experiment schema **1.1.0**, published in package **1.1.0-r1**, adding assessment time, consumed-determination reference, provenance, capabilities and separate review states  
  https://github.com/FG-TIDA/use-cases/issues/4#issuecomment-5871266911
```

**Razón y efecto semántico:** Evita confundir el contrato JSON con la revisión del ZIP. No cambia la versión ni el contenido de un sidecar congelado.

**Fuentes/evidencia:** hallazgos anteriores y [registro de evidencia](../../../../../../governance/review/R01_ORACLE_REVIEW_EVIDENCE_2026-10-06.json); fuente fijada de §1.

**Dependencias y otras VNext:** UC4_INTEROPERABILITY_PROFILE.md, NELSON_BASELINE_IMPORT.md y registro de integración; cualquier corrección de esas fuentes requiere su propio expediente.

**Comprobaciones necesarias y límites:** Contrastar schema_version y package_version del manifest del companion público; verificar cita y coincidencia única. No inferir validator-pass ni aceptación de Nelson.

**Decisión de Iván:** pendiente sobre este ID concreto.  
**Incorporación:** no ejecutada. La fuente protegida requiere una ruta autorizada que conserve el guard vigente; no se cambia el guard para hacer pasar una corrección.

### R01-ORACLE-DELTA-002 — Hacer visible la reutilización de los harness propios

**ID y estado:** R01-ORACLE-DELTA-002 · propuesta, incorporación pendiente.  
**Documento/fuente:** `R01-ORACLE-C02-README`, `research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/README.md`; commit `40cb19682fd1211d2c07e81ecd0242b56d425918`; blob `282d97ed967898a086303927872fbdfcaf37dd70`; versión editorial no declarada, estado 5 de octubre de 2026.  
**Instrucción:** IVAN-R01-ORACLE-20261006-01.  
**Auditorías/hallazgos:** AUD-001/AUD-002; R01-ORACLE-F002, R01-ORACLE-F003, R01-ORACLE-F007, R01-ORACLE-F008, R01-ORACLE-F009, R01-ORACLE-F010.  
**Localización:** Antes de Interoperability rule; se conserva y repite el ancla literal.  
**Tipo:** inserción propuesta.

**TEXTO ANTES**

```markdown
## Interoperability rule

R01 does **not** fork Nelson's experiment contract. The intended composition is:
```

**TEXTO DESPUÉS**

```markdown
## Reuse of the existing corpus harnesses

R01 builds on an existing test corpus. Reuse must distinguish code or infrastructure already adapted, controls available for a new profile, and a mapping that has actually been tested and admitted. Prior results retain their original scenario, version and evidence scope.

| Existing source | Reusable part | Current R01 integration boundary |
|---|---|---|
| [RS-00E-Q1a](../../../fixtures/RS-00E-Q1a/README.md) | Canonical Trace v1, post-run evaluation, replay and instrumentation controls. | The serialization utility is adapted here; Q1a truth, scoring and shared-logic comparator results do not evaluate R01 routes. |
| [00K symbolic suite](../../../fixtures/00K-SUITE/README.md) | P1–P6 regressions, matched controls, ablations, strong-repair tests and retained falsifiers. | Keep the registered suite as a regression source; importing a control does not create an R01 outcome or a real-technology result. |
| [00L paired traversals](../../../00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/README.md) | Frozen facts, visible observations, prior rules, separate oracle, paired comparisons and requirement/gate traceability. | Normalize observations, dispositions and resource units through a reviewed profile; paper and symbolic results retain their scope. |
| [00I / S5 stateful harness](../../../fixtures/00I-STATEFUL/README.md) | Queue, source reads, guard, permit, executor, target-state observations and bounded recovery. | Candidate backend for a versioned R01/UC-4 adapter; no such admitted adapter or AWS execution is established by this reference. S5 effect expectations remain a specific evaluator. |
| [00G-HF development history](../../../annexes/00G-HF-DEVELOPMENT-HISTORY-v0.1.md) | Recorder, authority controls, episode/seed handling, social messages and dynamic schedules. | Preserve each runner's own oracle, policy and result scope; projection to R01 routes and collective measures requires a declared correspondence. |
| [Earlier R01 diagnostics](../feasibility/partial-experiments/README.md) | Small-world enumeration, budget/measurement countercontrols and historical counterexamples. | Revalidate against the current scenario and conditioned theorem; these are not the complete neutral R01 evaluator. |

The integration direction is a common experiment/trace boundary with versioned scenario backends and specific evaluators. It does not require rewriting the retained harnesses or merging their ground truths. Conventional controls that succeed retain that result.

## Interoperability rule

R01 does **not** fork Nelson's experiment contract. The intended composition is:
```

**Razón y efecto semántico:** Hace revisable qué se reutiliza de Q1a/00K/00L/00I/00G-HF/primer R01 y qué sigue siendo un mapping. La tabla es propuesta de documentación, no incorporación de código, admisión ni nuevo plan activo.

**Fuentes/evidencia:** hallazgos anteriores y [registro de evidencia](../../../../../../governance/review/R01_ORACLE_REVIEW_EVIDENCE_2026-10-06.json); fuente fijada de §1.

**Dependencias y otras VNext:** Routers de las familias enlazadas; WORKPLAN.md sigue siendo dueño de la cola C02/C11/T03. Los scripts/oráculos originales y sus resultados conservan identidad.

**Comprobaciones necesarias y límites:** Comprobar todas las rutas, semántica por propietario y que las familias no se sumen como una campaña R01. Para una integración futura se necesitan perfil/versiones, visibilidad, costes y prueba de correspondencia; no se ejecutan en esta auditoría.

**Decisión de Iván:** pendiente sobre este ID concreto.  
**Incorporación:** no ejecutada. La fuente protegida requiere una ruta autorizada que conserve el guard vigente; no se cambia el guard para hacer pasar una corrección.

### R01-ORACLE-DELTA-003 — Distinguir self-test del instrumento y aceptación del candidato

**ID y estado:** R01-ORACLE-DELTA-003 · propuesta, incorporación pendiente.  
**Documento/fuente:** `R01-ORACLE-C02-README`, `research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/README.md`; commit `40cb19682fd1211d2c07e81ecd0242b56d425918`; blob `282d97ed967898a086303927872fbdfcaf37dd70`; versión editorial no declarada, estado 5 de octubre de 2026.  
**Instrucción:** IVAN-R01-ORACLE-20261006-01.  
**Auditorías/hallazgos:** AUD-001/AUD-002; R01-ORACLE-F001, R01-ORACLE-F009.  
**Localización:** What is executable now · párrafo de apertura.  
**Tipo:** inserción propuesta.

**TEXTO ANTES**

```markdown
The current Stage-0 self-test is intentionally small and now reuses several control patterns already demonstrated in Nelson's Stage-0 calibration. It verifies that the harness can:
```

**TEXTO DESPUÉS**

```markdown
The recorded self-test is successful because each control produces its frozen expected outcome. In the v0.9 record, the positive and tied-optimum vectors return PASS; the connector-boundary, inadmissible-route and cost/deadline vectors return FAIL; the no-reference vector remains INCONCLUSIVE. These are intentional instrumentation outcomes, not six successful technology trials. See [SELFTEST_RECORD_v0.9](./SELFTEST_RECORD_v0.9.md).

The current Stage-0 self-test is intentionally small and now reuses several control patterns already demonstrated in Nelson's Stage-0 calibration. It verifies that the harness can:
```

**Razón y efecto semántico:** Impide leer el resultado global verde como éxito de toda tecnología o de todos los escenarios. Conserva la lista de funciones existente.

**Fuentes/evidencia:** hallazgos anteriores y [registro de evidencia](../../../../../../governance/review/R01_ORACLE_REVIEW_EVIDENCE_2026-10-06.json); fuente fijada de §1.

**Dependencias y otras VNext:** SELFTEST_RECORD_v0.9.md y selftest_result_v0.9.json como evidencia intacta; ninguno se modifica ni recalcula.

**Comprobaciones necesarias y límites:** Leer las seis entradas del registro fijado; separar expected control result, candidate status y scientific conclusion. No añadir números a una tasa poblacional.

**Decisión de Iván:** pendiente sobre este ID concreto.  
**Incorporación:** no ejecutada. La fuente protegida requiere una ruta autorizada que conserve el guard vigente; no se cambia el guard para hacer pasar una corrección.

### R01-ORACLE-DELTA-004 — Delimitar diversidad de referencia, dominio y validación externa

**ID y estado:** R01-ORACLE-DELTA-004 · propuesta, incorporación pendiente.  
**Documento/fuente:** `R01-ORACLE-C02-README`, `research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/README.md`; commit `40cb19682fd1211d2c07e81ecd0242b56d425918`; blob `282d97ed967898a086303927872fbdfcaf37dd70`; versión editorial no declarada, estado 5 de octubre de 2026.  
**Instrucción:** IVAN-R01-ORACLE-20261006-01.  
**Auditorías/hallazgos:** AUD-001/AUD-002; R01-ORACLE-F006, R01-ORACLE-F010.  
**Localización:** Claim boundary · párrafo único final.  
**Tipo:** inserción propuesta.

**TEXTO ANTES**

```markdown
A passing self-test means only that this first instrument path behaves as specified on author-constructed synthetic controls. It does not establish the correctness of the complete R01 C-V evaluator, scalability, statistical performance, an EA differential or suitability of any real technology. C11 registration and T03 real-technology execution remain later gates.
```

**TEXTO DESPUÉS**

```markdown
A passing self-test means only that this first instrument path behaves as specified on author-constructed synthetic controls. It does not establish the correctness of the complete R01 C-V evaluator, scalability, statistical performance, an EA differential or suitability of any real technology. C11 registration and T03 real-technology execution remain later gates.

The two exact trajectory reference paths are separately coded by the same maintainer; their agreement is an implementation cross-check, not independent external validation. The additional exhaustive-versus-dynamic-programming DAG controls cover their declared finite, nonnegative conjunctive domain. They do not establish all R01 relational/parity profiles, collective dynamics, stochastic performance or real operational resource measurements. Those require separately scoped correspondence and review before campaign admission.
```

**Razón y efecto semántico:** Aclara la relación entre dos implementaciones, un contraste algorítmico y la cobertura completa de R01. No retira el soporte acotado ni presupone errores fuera del dominio.

**Fuentes/evidencia:** hallazgos anteriores y [registro de evidencia](../../../../../../governance/review/R01_ORACLE_REVIEW_EVIDENCE_2026-10-06.json); fuente fijada de §1.

**Dependencias y otras VNext:** reference.py, reference_secondary.py, reference_graph_exhaustive.py, reference_graph_dp.py, oracle/README y COMPUTABILITY_AND_ORACLE_PLAN; código y freeze permanecen intactos.

**Comprobaciones necesarias y límites:** Revisar admisibilidad y codificación del dominio de cada método y manifest de controles; cotejar M16/M17 y C02 antes de cualquier afirmación más amplia. Sin nueva ejecución durante la preparación.

**Decisión de Iván:** pendiente sobre este ID concreto.  
**Incorporación:** no ejecutada. La fuente protegida requiere una ruta autorizada que conserve el guard vigente; no se cambia el guard para hacer pasar una corrección.

### Consolidación final

Se recomienda preparar DELTA-001–004 como cambios documentales compatibles entre sí, únicamente después de decisión de Iván y revalidación sobre la fuente entonces vigente. No se propone aplicar deltas de código, modificar los 30 archivos del freeze, alterar resultados o cerrar C02. F003/F005/F007/F008/F010 mantienen verificaciones e integración pendientes; no se resuelven mediante estas mejoras del README.

## Propuestas adicionales de las pasadas diferenciadas — incorporación pendiente

Las propuestas 001–004 anteriores permanecen íntegramente como historia. Las siguientes se preparan por **IVAN-R01-ORACLE-20261006-03** sobre la misma fuente del README, blob `282d97ed967898a086303927872fbdfcaf37dd70`, ahora reconfirmado en corte `715027943eefb372fdb4541a23d288bffdedbdb2`. Ninguna se incorpora por esta entrega.

### R01-ORACLE-DELTA-005 — Explicar el propósito antes de la atribución técnica

**Fuente:** README del oráculo C02, corte/blob anteriores; estado 5 de octubre de 2026. **Instrucción:** IVAN-R01-ORACLE-20261006-03. **Ancla:** Párrafo de estado, después del título. **Hallazgos:** Pasadas 1/3 y futura lectura humana; límites F001/F011/F012.

**TEXTO ANTES**

```markdown
**Status: limited implementation + successful Stage-0 instrumentation self-test · 5 October 2026.** This directory contains the executable C02 instrument slice requested for R01. It is not a real-technology campaign, not an externally validated oracle, and not an FG-TIDA deliverable.
```

**TEXTO DESPUÉS**

```markdown
**Status: limited implementation + successful Stage-0 instrumentation self-test · 5 October 2026.** This directory contains the executable C02 instrument slice requested for R01. It is not a real-technology campaign, not an externally validated oracle, and not an FG-TIDA deliverable.

This instrument compares a recorded candidate choice or execution with the best admissible route in a small frozen world, under declared quality, resource and deadline conditions. The evaluator's private information is kept separate from the candidate's observations.
```

**Razón y efecto:** Añade la pregunta que responde el instrumento antes de los términos C02/UC4/sidecar. No cambia su estado ni amplía evidencia.

**Dependencias y comprobaciones:** revalidar la coincidencia única sobre la fuente entonces vigente, revisar los enlaces/predicados citados y conservar el guard. DELTA-005 no colisiona con 001–004. DELTA-006 comparte el tema de 003/004 pero usa otro ancla. DELTA-007 conserva el bloque que precede a la inserción 002.

**Decisión de Iván:** pendiente por ID. **Incorporación:** no aplicada; la fuente protegida requiere ruta autorizada sin desactivar su guard.

### R01-ORACLE-DELTA-006 — Separar modo, efectos y métricas antes de reproducir

**Fuente:** README del oráculo C02, corte/blob anteriores; estado 5 de octubre de 2026. **Instrucción:** IVAN-R01-ORACLE-20261006-03. **Ancla:** Antes del comando de reproducción. **Hallazgos:** F011/F012/F016; pasadas 1–3.

**TEXTO ANTES**

```markdown
Run locally from this directory:
```

**TEXTO DESPUÉS**

```markdown
Interpret results by their declared mode. A batch PASS checks the candidate's declared selection against a bounded reference and frozen measurements; it is not proof of an executed effect. The interactive instrumentation additionally checks matching environment execution evidence. Native `completion` and `legitimate_q` fields do not automatically establish the scenario's timely admissible-delivery metrics: the current evaluator checks deadline separately. Full scenario metrics and real-runtime isolation remain profile-specific verification obligations.

Run locally from this directory:
```

**Razón y efecto:** Hace explícita una frontera documentada en código/contratos. Evita importar choice, completion o q sintéticos como entrega/seguridad empírica. No corrige código ni recalcula evidencia.

**Dependencias y comprobaciones:** revalidar la coincidencia única sobre la fuente entonces vigente, revisar los enlaces/predicados citados y conservar el guard. DELTA-005 no colisiona con 001–004. DELTA-006 comparte el tema de 003/004 pero usa otro ancla. DELTA-007 conserva el bloque que precede a la inserción 002.

**Decisión de Iván:** pendiente por ID. **Incorporación:** no aplicada; la fuente protegida requiere ruta autorizada sin desactivar su guard.

### R01-ORACLE-DELTA-007 — Hacer navegables las fuentes propias del bloque Corpus reuse

**Fuente:** README del oráculo C02, corte/blob anteriores; estado 5 de octubre de 2026. **Instrucción:** IVAN-R01-ORACLE-20261006-03. **Ancla:** Bloque Corpus reuse, cinco referencias planas. **Hallazgos:** Pasada 3; consecuencias de trazabilidad de F002/F003/F007.

**TEXTO ANTES**

```markdown
Corpus reuse:

- R01 scenario §§1.4, 2.6, 2.15–2.17: ../Escenario-creatividad-validacion.md
- Existing partial C3 oracle: ../../../fixtures/00G-HF-ORACLE-v0.4/README.md
- Bounded oracle / fixture method: ../../../00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md
- Deterministic harness pattern: ../../../00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1.md
- Canonical Trace v1 source implementation: ../../../fixtures/RS-00E-Q1a/canonical_trace_v1.py
```

**TEXTO DESPUÉS**

```markdown
Corpus reuse:

- [R01 scenario §§1.4, 2.6, 2.15–2.17](../Escenario-creatividad-validacion.md)
- [Existing partial C3 oracle](../../../fixtures/00G-HF-ORACLE-v0.4/README.md)
- [Bounded oracle / fixture method](../../../00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md)
- [Deterministic harness pattern](../../../00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1.md)
- [Canonical Trace v1 source implementation](../../../fixtures/RS-00E-Q1a/canonical_trace_v1.py)
```

**Razón y efecto:** Conserva los cinco destinos y su orden; modifica únicamente el formato de enlace para que la fuente sea accesible.

**Dependencias y comprobaciones:** revalidar la coincidencia única sobre la fuente entonces vigente, revisar los enlaces/predicados citados y conservar el guard. DELTA-005 no colisiona con 001–004. DELTA-006 comparte el tema de 003/004 pero usa otro ancla. DELTA-007 conserva el bloque que precede a la inserción 002.

**Decisión de Iván:** pendiente por ID. **Incorporación:** no aplicada; la fuente protegida requiere ruta autorizada sin desactivar su guard.


---

## Quinta pasada — investigación externa, diferencial y reutilización

**Instrucción de Iván, 6 de octubre de 2026. Estado: contraste específico pendiente.** Esta quinta pasada se realiza después de las cuatro y queda dentro de esta misma VNext. No se crea otro expediente ni se incorporan propuestas a la fuente por esta anotación.

**Pregunta de este documento:** Contrastar oráculos, known-answer controls, separación de observación/evaluación y métricas de utilidad con métodos externos. Identificar piezas reutilizables sin convertir acuerdo de implementaciones en independencia ni victoria en una campaña real.

Se fijarán trabajos primarios de FG-TIDA y de otras líneas relevantes, incluidos antecedentes y actualizaciones posteriores, con autor, versión, fecha y alcance realmente leído. Aquí se justificará qué coincide, qué diferencia podría sostenerse y qué pieza concreta conviene reutilizar, con sus condiciones de atribución, adaptación y compatibilidad.

El [mapa externo preparatorio](../../../../../../governance/review/EP_EXTERNAL_RESEARCH_REVIEW_2026-10-06.md) aporta fuentes iniciales; no completa esta pasada. El [plan 1.6](../../../../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#quinta-pasada--trabajos-externos-diferencial-y-reutilización) gobierna método y cierre. Las cuatro lecturas previas mantienen sus estados reales y se reabren si aparece evidencia que las afecte. Codex, mismo asistente de IA; anotación de alcance, sin independencia externa.


### Primer contraste externo preparatorio del oráculo

**Auditoría realizada por Codex, 6 de octubre de 2026. Alcance parcial de quinta pasada:** métodos y disposición externa; no reproducción de campañas. Se conservan los pendientes de correspondencia e implementación de las lecturas previas.

[Petersen](https://arxiv.org/html/2412.10039v1) aporta una razón para comparar métricas con un control sin efecto esperado. Su distribución trata skeletons de grafos, no mandatos, decisiones o entrega admisible en R01; esas fórmulas no se transfieren sin un modelo nuevo.

La [contribución FG-TIDA #30](https://github.com/FG-TIDA/themes/issues/30) añade controles de respuesta conocida como vecino metodológico. Su [cierre](https://github.com/FG-TIDA/themes/issues/30#issuecomment-5947715148) indica fuera de alcance, y el catálogo distingue código de contenido reservado. La pieza aprovechable sería una técnica o código delimitado tras revisar versión y licencia; no se importaron casos o prosa.

**Diferencial:** disponer de negativos, known answers o scoring mecánico no es una novedad demostrada por este README. Falta comparar el mismo dominio, control positivo, carga y aislamiento del evaluador; los perfiles distintos no equivalen. La quinta queda abierta. Si interesa una pieza concreta, su propuesta tendrá fuente exacta, adaptación y texto antes/después dentro de este expediente.


---

## Sexta pasada unificadora — preparación y continuidad

**Instrucción de Iván, 6 de octubre de 2026. Preparación registrada por Codex, mismo asistente de IA. Estado: pendiente de lanzamiento después de las cinco pasadas del corpus.** Esta anotación organiza el trabajo futuro; no declara una auditoría unificadora realizada ni cambia el estado de las lecturas anteriores.

**Pregunta de consolidación de este documento:** Conciliar dominios, ground truth, controles y resultados de R01 con requisitos y benchmark; acuerdo de helpers, control finito o coste sintético no se convierte en independencia o eficacia causal.

Los hallazgos concretos se comentarán aquí y en las VNext de los documentos relacionados, conservando respuestas y desacuerdos. Se cotejarán las propuestas con la fuente actual y sus consumidores antes de presentar candidatos consolidados antes/después. La [sexta pasada del plan](../../../../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#sexta-pasada-unificadora-y-consolidación) fija el lanzamiento y el método. Se preservan fuente, historia y decisión de Iván para incorporar cambios.


---

## Prioridades del plan de cambios — revisión del corte

**Revisión realizada por Codex, 6 octubre de 2026, mismo asistente de IA.** Se revisan las auditorías y propuestas ya registradas para valorar impacto esperado, riesgo y esfuerzo. La fuente pública del corte es `7500dd5ee05c1a5052a28d35a8cefaf2c530707f`; los viejos y pares anteriores permanecen íntegros. Esta revisión no completa las pasadas pendientes ni la sexta.

El [plan 1.11](../../../../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#prioridad-de-cada-cambio--impacto-riesgo-y-esfuerzo) explica los criterios y el [listado completo](../../../../../../governance/review/change-priorities-2026-10-06/priorities.json) conserva las fuentes y los pares. La prioridad sirve para preparar tandas de decisión; la incorporación depende de Iván y de las comprobaciones indicadas.

| Cambio | Prioridad / tanda | Impacto esperado | Riesgo | Esfuerzo | Estado |
|---|---|---|---|---|---|
| 24 · Separar versión de schema y paquete UC4 | Siguiente · 1 — Claridad de evidencia y estado | Medio | Medio | Bajo | Pendiente de decisión |
| 25 · Explicar reutilización por familia sin trasladar resultados | Siguiente · 4 — Lectura humana y rutas | Alto | Medio | Medio | Pendiente de decisión |
| 26 · Self-test verde distinto de tecnología que pasa | Primera · 1 — Claridad de evidencia y estado | Alto | Bajo | Bajo | Pendiente de decisión |
| 27 · Límite de dominio e independencia del oráculo | Primera · 1 — Claridad de evidencia y estado | Alto | Medio | Medio | Pendiente de decisión |
| 28 · Propósito del oráculo antes de la atribución | Siguiente · 4 — Lectura humana y rutas | Medio | Bajo | Bajo | Pendiente de decisión |
| 29 · Distinguir modo, efectos y métricas antes de reproducir | Siguiente · 4 — Lectura humana y rutas | Alto | Medio | Medio | Pendiente de decisión |
| 30 · Convertir referencias propias en rutas navegables | Después · 4 — Lectura humana y rutas | Medio | Bajo | Bajo | Pendiente de decisión |

### Cambio 24 — Separar versión de schema y paquete UC4

**Impacto esperado: Medio. Riesgo: Medio. Coste/esfuerzo: Bajo. Prioridad: Siguiente.** No mezclar schema 1.1.0 con release 1.1.0-r1.

**Qué podría quedar desactualizado o afectado:** Companion mutable, sidecar y validador pueden usar versiones distintas; corregir solo el README deja el perfil o import note desfasados.

**Qué cuesta prepararlo:** Cotejo del manifest pin y dos documentos receptores; no cambiar sidecars congelados.

**Dependencias conocidas:** [UC4_INTEROPERABILITY_PROFILE.md](UC4_INTEROPERABILITY_PROFILE.md) · [NELSON_BASELINE_IMPORT.md](NELSON_BASELINE_IMPORT.md). La lista es el mapa conocido para preparar la decisión, no certificación de todos los consumidores.

**Estado y condición:** Pendiente de decisión. Completar comprobaciones específicas antes de decisión. Verificar vigencia del pin antes de incorporar; source-review no equivale a validator-pass.

**Viejo y nuevo:** el par literal sigue en [la entrada anterior](README_VNext.md#r01-oracle-delta-001--separar-versión-del-esquema-y-del-paquete-uc4); el viejo tiene una coincidencia en [la fuente actual](README.md), blob `282d97ed967898a086303927872fbdfcaf37dd70`. Localizar el viejo no prueba compatibilidad de la propuesta ni autoriza incorporación.

### Cambio 25 — Explicar reutilización por familia sin trasladar resultados

**Impacto esperado: Alto. Riesgo: Medio. Coste/esfuerzo: Medio. Prioridad: Siguiente.** Hacer visible qué puede usarse de Q1a/00K/00L/00I/C3 y qué sigue sin mapping.

**Qué podría quedar desactualizado o afectado:** La tabla puede quedar vieja o sumar campañas distintas como evidencia R01; desarrollar un adapter es otra acción.

**Qué cuesta prepararlo:** Siete familias con owners/versiones y comparación de límites; no importación ni ejecución.

**Dependencias conocidas:** [README.md](../../../fixtures/RS-00E-Q1a/README.md) · [README.md](../../../fixtures/00K-SUITE/README.md) · [README.md](../../../00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/README.md) · [README.md](../../../fixtures/00I-STATEFUL/README.md) · [README.md](../../../fixtures/00G-HF-ORACLE-v0.4/README.md). La lista es el mapa conocido para preparar la decisión, no certificación de todos los consumidores.

**Estado y condición:** Pendiente de decisión. Completar comprobaciones específicas antes de decisión. Alinear con matriz existente, tareas 1/2 y workplan; tabla propuesta, no admisión.

**Viejo y nuevo:** el par literal sigue en [la entrada anterior](README_VNext.md#r01-oracle-delta-002--hacer-visible-la-reutilización-de-los-harness-propios); el viejo tiene una coincidencia en [la fuente actual](README.md), blob `282d97ed967898a086303927872fbdfcaf37dd70`. Localizar el viejo no prueba compatibilidad de la propuesta ni autoriza incorporación.

### Cambio 26 — Self-test verde distinto de tecnología que pasa

**Impacto esperado: Alto. Riesgo: Bajo. Coste/esfuerzo: Bajo. Prioridad: Primera.** Evitar que seis controles esperados se presenten como seis éxitos de tecnologías.

**Qué podría quedar desactualizado o afectado:** Números o estados del lote pueden quedar desactualizados; la explicación debe citar v0.9 en vez de decir siempre current.

**Qué cuesta prepararlo:** Un párrafo y cotejo de las seis entradas fijadas; no recalcular evidencia.

**Dependencias conocidas:** [SELFTEST_RECORD_v0.9.md](SELFTEST_RECORD_v0.9.md) · [selftest_result_v0.9.json](selftest_result_v0.9.json). La lista es el mapa conocido para preparar la decisión, no certificación de todos los consumidores.

**Estado y condición:** Pendiente de decisión. Candidato para revisión documental concreta. Fijar registro usado y distinguir control esperado, candidate status y conclusión.

**Viejo y nuevo:** el par literal sigue en [la entrada anterior](README_VNext.md#r01-oracle-delta-003--distinguir-self-test-del-instrumento-y-aceptación-del-candidato); el viejo tiene una coincidencia en [la fuente actual](README.md), blob `282d97ed967898a086303927872fbdfcaf37dd70`. Localizar el viejo no prueba compatibilidad de la propuesta ni autoriza incorporación.

### Cambio 27 — Límite de dominio e independencia del oráculo

**Impacto esperado: Alto. Riesgo: Medio. Coste/esfuerzo: Medio. Prioridad: Primera.** Impedir que acuerdo de dos implementaciones o un DAG finito parezca validación externa del R01 completo.

**Qué podría quedar desactualizado o afectado:** Si otros README/métricas mantienen esa extrapolación el efecto queda incompleto; futuras ampliaciones pueden cambiar el dominio.

**Qué cuesta prepararlo:** Cotejo del dominio/premisas y recibos ya existentes, M16/M17, sin nuevas campañas.

**Dependencias conocidas:** [README.md](README.md) · [SELFTEST_RECORD_v0.9.md](SELFTEST_RECORD_v0.9.md) · [selftest_result_v0.9.json](selftest_result_v0.9.json) · [UC4_INTEROPERABILITY_PROFILE.md](UC4_INTEROPERABILITY_PROFILE.md) · [COMPUTABILITY_AND_ORACLE_PLAN.md](../COMPUTABILITY_AND_ORACLE_PLAN.md). La lista es el mapa conocido para preparar la decisión, no certificación de todos los consumidores.

**Estado y condición:** Pendiente de decisión. Candidato para revisión documental concreta. Conservar soporte acotado y límites; no declarar independencia por relectura de Codex.

**Viejo y nuevo:** el par literal sigue en [la entrada anterior](README_VNext.md#r01-oracle-delta-004--delimitar-diversidad-de-referencia-dominio-y-validación-externa); el viejo tiene una coincidencia en [la fuente actual](README.md), blob `282d97ed967898a086303927872fbdfcaf37dd70`. Localizar el viejo no prueba compatibilidad de la propuesta ni autoriza incorporación.

### Cambio 28 — Propósito del oráculo antes de la atribución

**Impacto esperado: Medio. Riesgo: Bajo. Coste/esfuerzo: Bajo. Prioridad: Siguiente.** Que una persona entienda entrada, evaluación y resultado antes de fuentes técnicas.

**Qué podría quedar desactualizado o afectado:** La apertura debe concordar con el modo del instrumento y no parecer servicio desplegado.

**Qué cuesta prepararlo:** Un párrafo y cotejo con interfaces actuales.

**Dependencias conocidas:** [README.md](README.md) · [TRACE_CONTRACT.md](TRACE_CONTRACT.md). La lista es el mapa conocido para preparar la decisión, no certificación de todos los consumidores.

**Estado y condición:** Pendiente de decisión. Candidato para revisión documental concreta. Mantener estado limited implementation y límites del lote.

**Viejo y nuevo:** el par literal sigue en [la entrada anterior](README_VNext.md#r01-oracle-delta-005--explicar-el-propósito-antes-de-la-atribución-técnica); el viejo tiene una coincidencia en [la fuente actual](README.md), blob `282d97ed967898a086303927872fbdfcaf37dd70`. Localizar el viejo no prueba compatibilidad de la propuesta ni autoriza incorporación.

### Cambio 29 — Distinguir modo, efectos y métricas antes de reproducir

**Impacto esperado: Alto. Riesgo: Medio. Coste/esfuerzo: Medio. Prioridad: Siguiente.** Que una instrucción de reproducción no confunda intento, efecto y aceptación.

**Qué podría quedar desactualizado o afectado:** El texto puede prometer métricas o aislamiento que el runner no produce; datos instrumentales no son costes reales.

**Qué cuesta prepararlo:** Leer contrato/mode y etiquetas de salida del instrumento; ninguna ejecución de programa.

**Dependencias conocidas:** [README.md](README.md) · [TRACE_CONTRACT.md](TRACE_CONTRACT.md) · [ISOLATION_CONTRACT.md](ISOLATION_CONTRACT.md). La lista es el mapa conocido para preparar la decisión, no certificación de todos los consumidores.

**Estado y condición:** Pendiente de decisión. Candidato para revisión documental concreta. Confirmar correspondencia documental con los modos; evitar nueva autorización de ejecución implícita.

**Viejo y nuevo:** el par literal sigue en [la entrada anterior](README_VNext.md#r01-oracle-delta-006--separar-modo-efectos-y-métricas-antes-de-reproducir); el viejo tiene una coincidencia en [la fuente actual](README.md), blob `282d97ed967898a086303927872fbdfcaf37dd70`. Localizar el viejo no prueba compatibilidad de la propuesta ni autoriza incorporación.

### Cambio 30 — Convertir referencias propias en rutas navegables

**Impacto esperado: Medio. Riesgo: Bajo. Coste/esfuerzo: Bajo. Prioridad: Después.** Que el lector abra la fuente correcta desde Corpus reuse.

**Qué podría quedar desactualizado o afectado:** Enlaces y versiones pueden quedar viejos; ruta existente no demuestra conservación semántica.

**Qué cuesta prepararlo:** Cuatro enlaces y comprobar destinos fijados.

**Dependencias conocidas:** [README.md](../../../fixtures/00G-HF-ORACLE-v0.4/README.md) · [00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md](../../../00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md) · [00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1.md](../../../00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1.md). La lista es el mapa conocido para preparar la decisión, no certificación de todos los consumidores.

**Estado y condición:** Pendiente de decisión. Candidato para revisión documental concreta. Mantener atribución y límites de cada origen.

**Viejo y nuevo:** el par literal sigue en [la entrada anterior](README_VNext.md#r01-oracle-delta-007--hacer-navegables-las-fuentes-propias-del-bloque-corpus-reuse); el viejo tiene una coincidencia en [la fuente actual](README.md), blob `282d97ed967898a086303927872fbdfcaf37dd70`. Localizar el viejo no prueba compatibilidad de la propuesta ni autoriza incorporación.

### Líneas de trabajo por concretar — no cambios ejecutables

| Trabajo ya recomendado | Impacto esperado | Riesgo | Esfuerzo | Prioridad / preparación |
|---|---|---|---|---|
| 46 · Preparar envolvente UC4 y sidecar R01 (R01 §5.1, paso 3) | Alto | Alto | Alto | Primera; sin par literal |
| 47 · Diseñar primer perfil propio de instrumento (R01 §5.1, paso 4) | Alto | Alto | Alto | Siguiente; sin par literal |
| 48 · Completar fidelidad del evaluador en perfil admitido (R01 §5.1, paso 5) | Alto | Alto | Alto | Primera; sin par literal |
| 49 · Extender solo lo necesario a otras familias (R01 §5.1, paso 6) | Medio | Alto | Alto | Después; sin par literal |
| 50 · Registrar una campaña concreta (R01 §5.1, paso 7) | Alto | Alto | No estimable todavía | Después; sin par literal |
| 51 · Evaluar una realización real elegida (R01 §5.1, paso 8) | Alto | Alto | No estimable todavía | Después; sin par literal |

**Preparar envolvente UC4 y sidecar R01.** Hacer revisable la correspondencia completa con UC4. **Riesgo:** Confundir sidecar con experiment.json o validator-pass con admisión; contrato externo/versiones pueden cambiar. **Coste:** Mapping/ejemplo completo, validador fijado y preguntas de owner; coste externo aún no estimable. **Condición:** Paso 3 pendiente: no validator ejecutado ni comunicación autorizada por esta prioridad.

**Diseñar primer perfil propio de instrumento.** Comprobar una conservación de predicados en un dominio pequeño antes de extender. **Riesgo:** Un adapter puede perder verdad, operación o efecto y mezclar resultados históricos; controles verdes no lo justifican solos. **Coste:** Perfil/adaptador acotado, correspondencia y controles; ingeniería/ejecución fuera de esta revisión. **Condición:** Depende de la matriz de tareas 1/2 y paquete del paso 3; registrar alcance antes de desarrollo.

**Completar fidelidad del evaluador en perfil admitido.** Evitar que un instrumento evalúe otra pregunta o compare costes incompatibles. **Riesgo:** Ampliar fidelidad más allá del dominio o atribuir independencia al mismo autor sesga el comparador. **Coste:** Cláusula–predicado–referencia–control, ledger y revisión que falte; calendario externo desconocido. **Condición:** M16/M17/P08 y dominio fijado; no asignar revisión externa ni repetir pruebas existentes aquí.

**Extender solo lo necesario a otras familias.** Reutilizar una propiedad necesaria sin empezar otro instrumento. **Riesgo:** Scope creep, duplicación de campañas y trasvase de resultados de 00L/C3/00G-HF; versiones divergen. **Coste:** Perfiles/versiones y controles por familia, después del piloto; no estimar coste global sin elegir necesidad. **Condición:** Condicionado a una propiedad requerida por el perfil y a fidelidad; no expansión automática.

**Registrar una campaña concreta.** Fijar comparadores, recursos, fallos y parada antes de observar resultados. **Riesgo:** Registro mal planteado puede sesgar la comparación o reabrir un trabajo abortado. **Coste:** Depende de tecnología, alcance, fuente/modelo y revisión humana elegidos; sin importe ni horas inventados. **Condición:** C02/perfil admitido y mandato de campaña. No activa C11 ni experimentos por aparecer en el ranking.

**Evaluar una realización real elegida.** Producir evidencia real en vez de transferir self-test de instrumento. **Riesgo:** Aislamiento, capacidad humana, comparadores, coste real y recursos pueden invalidar la interpretación. **Coste:** No estimable sin realización/configuración y autorización; presupuesto y disponibilidad no asumidos. **Condición:** T03/M13/C11 y alcance explícito; no ejecución, envío o reactivación de campaña abortada.

Los pasos 1 y 2 conservan el cierre acotado que ya consta en §5.3. Los pasos 3–8 siguen como recomendaciones de las tareas existentes, sin nueva campaña ni ejecución por este ranking.


---

## Revisión a fondo de los planes de cambio — 6 octubre 2026

**Evaluación realizada por Codex, mismo asistente de IA, para que una persona pueda decidir.** Se revisan el plan, sus motivos de auditoría, pares literales, impacto, riesgo, esfuerzo y dependencias; no es la sexta pasada científica global ni acredita el cierre de las cinco. Fuente de este cotejo: commit `03db21016d6a0831a43d7a99d3640854ab549777`, [documento propietario](README.md), blob `282d97ed967898a086303927872fbdfcaf37dd70`. Los registros anteriores y sus viejos completos permanecen íntegros.

La valoración actual distingue una mejora documental de una modificación conceptual o de contrato. **Candidato para revisión documental significa preparado para leer y decidir, no autorizado para incorporar.** Los originales siguen en sólo lectura; no se ejecuta ninguno de estos pares.

| Cambio | Calidad/estado actual | Impacto esperado | Riesgo | Esfuerzo | Prioridad |
|---|---|---|---|---|---|
| 24 | Documental condicionado; Pendiente de decisión | Medio | Medio | Bajo | Siguiente |
| 25 | Plan de lectura; incompleto; Pendiente de decisión | Alto | Medio | Medio | Siguiente |
| 26 | Documental preparado; Pendiente de decisión | Alto | Bajo | Bajo | Primera |
| 27 | Documental preparado; Pendiente de decisión | Alto | Medio | Medio | Primera |
| 28 | Documental preparado; Pendiente de decisión | Medio | Bajo | Bajo | Siguiente |
| 29 | Documental preparado; Pendiente de decisión | Alto | Medio | Medio | Siguiente |
| 30 | Documental preparado; Pendiente de decisión | Medio | Bajo | Bajo | Después |
| 46 | Etapa posterior; no parche; Por concretar; sin par literal | Alto | Alto | Alto | Primera |
| 47 | Etapa posterior; no parche; Por concretar; sin par literal | Alto | Alto | Alto | Siguiente |
| 48 | Etapa posterior; no parche; Por concretar; sin par literal | Alto | Alto | Alto | Primera |
| 49 | Etapa posterior; condicional; Por concretar; sin par literal | Medio | Alto | Alto | Después |
| 50 | Etapa posterior; coste no estimable; Por concretar; sin par literal | Alto | Alto | No estimable todavía | Después |
| 51 | Etapa posterior; coste no estimable; Por concretar; sin par literal | Alto | Alto | No estimable todavía | Después |

**Cambio 24 — Documental condicionado.** Versión de schema 1.1.0 y del paquete1.1.0-r1 son objetos distintos; la precisión no supone validator-pass o admisión.

**Beneficio esperado:** No mezclar schema 1.1.0 con release 1.1.0-r1. **Riesgo concreto:** Companion mutable, sidecar y validador pueden usar versiones distintas; corregir solo el README deja el perfil o import note desfasados. **Coste de preparar y mantener:** Cotejo del manifest pin y dos documentos receptores; no cambiar sidecars congelados.

**Localización actual:** viejo completo 1 coincidencia(s); texto propuesto 0 coincidencia(s), fuente actual completa. No se interpreta una cita o una subcadena del encabezado como modificación aplicada.

**Condición y orden de decisión:** Confirmar pin/metadata del paquete y perfilUC4, manteniendo fecha de consulta; no extrapolar a futuras releases. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

**Cambio 25 — Plan de lectura; incompleto.** La tabla ofrece siete familias reutilizables. El nombre de una familia no establece que todo su contenido sea transferible aR01.

**Beneficio esperado:** Hacer visible qué puede usarse de Q1a/00K/00L/00I/C3 y qué sigue sin mapping. **Riesgo concreto:** La tabla puede quedar vieja o sumar campañas distintas como evidencia R01; desarrollar un adapter es otra acción. **Coste de preparar y mantener:** Siete familias con owners/versiones y comparación de límites; no importación ni ejecución.

**Localización actual:** viejo completo 1 coincidencia(s); texto propuesto 0 coincidencia(s), fuente actual completa. No se interpreta una cita o una subcadena del encabezado como modificación aplicada.

**Condición y orden de decisión:** Cada fila necesita contrato/pin, parte reutilizada, resultado que no transfiere y gate propio;43/46–49 no se cierran por publicar la tabla. Revisar junto con 46, 48, 49. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

**Cambio 26 — Documental preparado.** PASS/FAIL/INCONCLUSIVE del self-test son resultados esperados del instrumento, no seis tecnologías exitosas. La advertencia ataca una lectura materialmente errónea.

**Beneficio esperado:** Evitar que seis controles esperados se presenten como seis éxitos de tecnologías. **Riesgo concreto:** Números o estados del lote pueden quedar desactualizados; la explicación debe citar v0.9 en vez de decir siempre current. **Coste de preparar y mantener:** Un párrafo y cotejo de las seis entradas fijadas; no recalcular evidencia.

**Localización actual:** viejo completo 1 coincidencia(s); texto propuesto 0 coincidencia(s), fuente actual completa. No se interpreta una cita o una subcadena del encabezado como modificación aplicada.

**Condición y orden de decisión:** CotejarSELFTEST_RECORD_v0.9/resultv0.9 y mantener dominio, denominador y expectativas; ningún rerun o eficacia comparativa. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

**Cambio 27 — Documental preparado.** Dos rutas codificadas por el mismo mantenedor son cross-check, no validación independiente. El dominioDAG finito no cubre todoR01.

**Beneficio esperado:** Impedir que acuerdo de dos implementaciones o un DAG finito parezca validación externa del R01 completo. **Riesgo concreto:** Si otros README/métricas mantienen esa extrapolación el efecto queda incompleto; futuras ampliaciones pueden cambiar el dominio. **Coste de preparar y mantener:** Cotejo del dominio/premisas y recibos ya existentes, M16/M17, sin nuevas campañas.

**Localización actual:** viejo completo 1 coincidencia(s); texto propuesto 0 coincidencia(s), fuente actual completa. No se interpreta una cita o una subcadena del encabezado como modificación aplicada.

**Condición y orden de decisión:** Conservar dominio no negativo/conjuntivo, atribución y límites de perfiles. No presentar el cotejo como independencia, escalabilidad o ejecución tecnológica. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

**Cambio 28 — Documental preparado.** Explicar propósito antes del detalle facilita lectura. No crea un segundo oráculo ni desplaza la aceptación del escenario.

**Beneficio esperado:** Que una persona entienda entrada, evaluación y resultado antes de fuentes técnicas. **Riesgo concreto:** La apertura debe concordar con el modo del instrumento y no parecer servicio desplegado. **Coste de preparar y mantener:** Un párrafo y cotejo con interfaces actuales.

**Localización actual:** viejo completo 1 coincidencia(s); texto propuesto 0 coincidencia(s), fuente actual completa. No se interpreta una cita o una subcadena del encabezado como modificación aplicada.

**Condición y orden de decisión:** La inserción queda antes de instrucciones técnicas, conserva fuentes y no convierteREADME en contrato nuevo. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

**Cambio 29 — Documental preparado.** Separar batch, ejecución interactive y métricas nativas evita acreditar efecto por una selección o una regresión verde.

**Beneficio esperado:** Que una instrucción de reproducción no confunda intento, efecto y aceptación. **Riesgo concreto:** El texto puede prometer métricas o aislamiento que el runner no produce; datos instrumentales no son costes reales. **Coste de preparar y mantener:** Leer contrato/mode y etiquetas de salida del instrumento; ninguna ejecución de programa.

**Localización actual:** viejo completo 1 coincidencia(s); texto propuesto 0 coincidencia(s), fuente actual completa. No se interpreta una cita o una subcadena del encabezado como modificación aplicada.

**Condición y orden de decisión:** LeerTRACE_CONTRACT/ISOLATION_CONTRACT y las métricas originales; conservar deadline/efecto/legitimidad como verificaciones diferentes, sin activar ejecución. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

**Cambio 30 — Documental preparado.** Son cinco rutas propias, no cuatro como decía el cálculo antiguo de esfuerzo. La mejora es navegación y no adopción de los resultados enlazados.

**Beneficio esperado:** Que el lector abra la fuente correcta desde Corpus reuse. **Riesgo concreto:** Enlaces y versiones pueden quedar viejos; ruta existente no demuestra conservación semántica. **Coste de preparar y mantener:** Son cinco enlaces; revisar cinco destinos y atribuciones, no cuatro. Esfuerzo Bajo para navegación.

**Localización actual:** viejo completo 1 coincidencia(s); texto propuesto 0 coincidencia(s), fuente actual completa. No se interpreta una cita o una subcadena del encabezado como modificación aplicada.

**Condición y orden de decisión:** Abrir los cinco destinos, mantener texto de atribución y scope; revisar desde el directoriooracle, no desde el de laVNext. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

**Cambio 46 — Etapa posterior; no parche.** Paso3 combina envolventeUC4 con sidecarR01. El trabajo es perfil de compatibilidad, no cambio autorizado por el ranking.

**Beneficio esperado:** Hacer revisable la correspondencia completa con UC4. **Riesgo concreto:** Confundir sidecar con experiment.json o validator-pass con admisión; contrato externo/versiones pueden cambiar. **Coste de preparar y mantener:** Mapping/ejemplo completo, validador fijado y preguntas de owner; coste externo aún no estimable.

**Plan todavía sin par literal:** esta línea describe trabajo por concretar; no se ofrece como edición ejecutable ni se inventa un viejo.

**Condición y orden de decisión:** Contrato/source pin, mapping sintáctico y semántico, estadosunknown y source review; definir sucesor/alcance antes de 47. Tareas1/2 mantienen su cierre acotado. Revisar junto con 24, 19. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

**Cambio 47 — Etapa posterior; no parche.** Paso4 exige un perfil piloto y aislamiento. Sin objetivo/law/configuración admitidos no existe experimento ejecutable.

**Beneficio esperado:** Comprobar una conservación de predicados en un dominio pequeño antes de extender. **Riesgo concreto:** Un adapter puede perder verdad, operación o efecto y mezclar resultados históricos; controles verdes no lo justifican solos. **Coste de preparar y mantener:** Perfil/adaptador acotado, correspondencia y controles; ingeniería/ejecución fuera de esta revisión.

**Plan todavía sin par literal:** esta línea describe trabajo por concretar; no se ofrece como edición ejecutable ni se inventa un viejo.

**Condición y orden de decisión:** Depende de 46; declarar entradas, operador, efecto, oráculo privado, costes y stop/acceptance antes de instrumentar. Nada se ejecuta en esta revisión. Revisar junto con 46. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

**Cambio 48 — Etapa posterior; no parche.** La fidelidad M16/M17/P08 decide qué mide el evaluador. Un self-test correcto no la resuelve.

**Beneficio esperado:** Evitar que un instrumento evalúe otra pregunta o compare costes incompatibles. **Riesgo concreto:** Ampliar fidelidad más allá del dominio o atribuir independencia al mismo autor sesga el comparador. **Coste de preparar y mantener:** Cláusula–predicado–referencia–control, ledger y revisión que falte; calendario externo desconocido.

**Plan todavía sin par literal:** esta línea describe trabajo por concretar; no se ofrece como edición ejecutable ni se inventa un viejo.

**Condición y orden de decisión:** Depende de 46/47; contrastar contrato del escenario, métricas/efecto/tiempo y control positivo/negativo. No renombrarcompletion como entrega legítima. Revisar junto con 46, 47. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

**Cambio 49 — Etapa posterior; condicional.** Añadirfamilias sin necesidad material crea alcance y mantenimiento innecesarios.

**Beneficio esperado:** Reutilizar una propiedad necesaria sin empezar otro instrumento. **Riesgo concreto:** Scope creep, duplicación de campañas y trasvase de resultados de 00L/C3/00G-HF; versiones divergen. **Coste de preparar y mantener:** Perfiles/versiones y controles por familia, después del piloto; no estimar coste global sin elegir necesidad.

**Plan todavía sin par literal:** esta línea describe trabajo por concretar; no se ofrece como edición ejecutable ni se inventa un viejo.

**Condición y orden de decisión:** Sólo extender tras48 y por una laguna concreta; conservar leyes/resultados originales y declarar interfaz/versiones. No ampliar por completar una lista. Revisar junto con 48. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

**Cambio 50 — Etapa posterior; coste no estimable.** Una campaña requiere pregunta, comparator, población/escenarios y recursos; el texto actual no los fija.

**Beneficio esperado:** Fijar comparadores, recursos, fallos y parada antes de observar resultados. **Riesgo concreto:** Registro mal planteado puede sesgar la comparación o reabrir un trabajo abortado. **Coste de preparar y mantener:** Depende de tecnología, alcance, fuente/modelo y revisión humana elegidos; sin importe ni horas inventados.

**Plan todavía sin par literal:** esta línea describe trabajo por concretar; no se ofrece como edición ejecutable ni se inventa un viejo.

**Condición y orden de decisión:** Cerrar46–49 pertinentes, preregistro/freeze, adjudicación y autoridad de ejecución. Mantener como plan futuro sin inventar par ni presupuesto. Revisar junto con 46, 47, 48, 49. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

**Cambio 51 — Etapa posterior; coste no estimable.** Realización/native execution exige fuentes, implementación y responsables seleccionados. No se deduce de que el método esté documentado.

**Beneficio esperado:** Producir evidencia real en vez de transferir self-test de instrumento. **Riesgo concreto:** Aislamiento, capacidad humana, comparadores, coste real y recursos pueden invalidar la interpretación. **Coste de preparar y mantener:** No estimable sin realización/configuración y autorización; presupuesto y disponibilidad no asumidos.

**Plan todavía sin par literal:** esta línea describe trabajo por concretar; no se ofrece como edición ejecutable ni se inventa un viejo.

**Condición y orden de decisión:** Membresía/fidelidad, derechos, autoridad, trust roots y alcance elegido; sólo después de los gates anteriores aplicables. No asignar/mandar trabajo a terceros. Revisar junto con 50. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

[Visión conjunta y tandas en EP README VNext](../../../../../../architectural-contributions/ecosystem-positioning/README_VNext.md#revisión-a-fondo-de-los-planes-de-cambio--6-octubre-2026). Mantener tres niveles de README, fuentes congeladas, resultados y binarios. Reorganización, nueva campaña, experimentos e incorporación canónica permanecen fuera de esta entrega.
