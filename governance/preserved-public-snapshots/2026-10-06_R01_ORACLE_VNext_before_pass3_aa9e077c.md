# Oráculo / harness R01 C02 — VNext de auditoría

El oráculo de R01 debe permitir comparar cómo distintas tecnologías encuentran una buena solución permitida, cuánto esfuerzo necesitan y si actúan dentro de su autoridad y plazo. Para hacerlo, separa lo que sabe el evaluador de lo que puede observar el candidato. Un bloqueo no es éxito si también impide la actividad legítima; una etiqueta correcta tampoco demuestra que el efecto sobre el destino haya sido correcto.

La revisión encuentra una base propia considerable: los harness anteriores ya aportan trazas, replay, controles semánticos, ejecución con estado y recuperación. El nuevo R01 puede componer esas piezas mediante adaptadores. La dificultad es conservar el significado de cada escenario y sus costes, sin convertir los resultados anteriores en validación automática de R01 o de EA. Nelson aporta el contrato y el ciclo experimental UC4; ese trabajo complementa los harness propios.

**Método vigente:** procedimiento EP 1.2, leído en commit `2f72751fef47d9f4cf1d270a1f7fa498a26f5760`. Historia inicial: la entrega de comentarios no completó las cuatro pasadas. La instrucción posterior IVAN-R01-ORACLE-20261006-03 abre su ejecución diferenciada; la tabla muestra el avance actual.

| Pasada | Estado de esta VNext |
|---|---|
| Fondo y lógica | Realizada como pasada diferenciada del README y sus límites; validación externa y código completo fuera de este cierre. |
| Evidencia y relaciones entre documentos | Realizada para las afirmaciones del README y cadenas materiales declaradas; fuentes vecinas tienen revisión cruzada parcial, no auditoría íntegra. |
| Edición, estructura y formato | Pendiente como pasada separada; las observaciones y propuestas existentes son insumos. |
| Legibilidad y comprensión humana | Pendiente como pasada separada; no ha participado un lector humano independiente. |

Los comentarios se explican primero en lenguaje corriente. El registro de fuentes, códigos y hashes posterior permite continuar la revisión sin sustituir su contenido.

**ID del documento lógico:** `R01-ORACLE-C02-README`  
**Expediente único:** `README_VNext.md` · **Revisión acumulativa:** 1.3 · **Fecha:** 6 de octubre de 2026  
**Estado:** auditoría documental y de relaciones parcial; propuestas pendientes de decisión por ID.  
**Nota externa:** [ficha de acceso](./README_REVIEW.md) · **Procedimiento:** [revisión segura del corpus](../../../../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md)

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

### Edición, estructura y formato — pendiente como pasada separada

La revisión mixta encontró insumos editoriales: diferenciar versión del schema y del ZIP, explicar el resultado mixto del self-test y hacer visible la infraestructura propia. Las cuatro propuestas exactas del final conservan esos comentarios. No se declara cerrada la edición completa del documento ni se modifica su cuerpo para corregirlos.

### Legibilidad y comprensión humana — pendiente como pasada separada

Un lector que llega sin los chats necesita entender qué significa evaluar una ruta permitida y por qué reaprovechar un harness no transfiere sus conclusiones. El README comienza con C02, Stage 0 y UC4; la VNext añade arriba una explicación para situar esa pregunta. Esto es una observación y simulación de lectura por el mismo asistente, no una prueba con otra persona ni una pasada completa de comprensión humana.

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
| IVAN-R01-ORACLE-20261006-03 | Realizar tareas 1 y 2 del plan. | Cuatro pasadas del README y matriz de compatibilidad, con registro cruzado. | En ejecución; sin incorporar deltas ni ejecutar campañas. |
| IVAN-R01-ORACLE-20261006-02 | Añadir un plan de trabajo recomendado dentro de esta VNext. | Secuencia, entregables, dependencias y criterios de cierre; mantener la cola propietaria. | Ejecutada como documentación del plan; trabajo futuro pendiente. |
| R01-ORACLE-DELTA-001–004 | No hay decisión de incorporación por ID en este chat. | Corrección del README o successor protegido. | **Pendiente de Iván.** |
| Campañas C11/T03 y comunicaciones | No autorizadas por esta instrucción documental. | Experimentos nuevos, integración/aceptación de contribuyentes y mensajes. | No ejecutados. |

La cola activa sigue en [WORKPLAN.md](../feasibility/WORKPLAN.md). Las recomendaciones de esta auditoría no crean una cola paralela ni convierten tareas históricas en activas. No hay autorizaciones inferidas de silencio, resultado verde o nombre de archivo.


## 5.1. Plan de trabajo recomendado para el oráculo y la reutilización

**Recomendación de Codex, mismo agente, 6 de octubre de 2026 · revisión 1.1 del expediente.** Instrucción auténtica **IVAN-R01-ORACLE-20261006-02**: «crea un plan de trabajo (recomendación tuya) dentro de vnext». Se autoriza añadir esta recomendación al expediente; su publicación no ejecuta las integraciones ni incorpora las cuatro correcciones propuestas.

Mi recomendación es consolidar una frontera común de experimento y trazas, con adaptadores pequeños y evaluadores específicos por escenario. Hay suficiente infraestructura propia para evitar empezar de cero. El trabajo decisivo es demostrar qué significado conserva cada adaptación: una ejecución stateful correcta de S5 y una ruta óptima admisible de R01 responden a preguntas distintas.

Priorizaría la compatibilidad comprobable en un dominio pequeño, antes de extender el evaluador a todas las familias o conectar una tecnología real. Nelson aporta la envolvente experimental y la revisión de su contrato; nuestros harness aportan backends, controles y evidencia histórica. La composición debe permitir usar ambos sin trasladar automáticamente sus conclusiones.

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
