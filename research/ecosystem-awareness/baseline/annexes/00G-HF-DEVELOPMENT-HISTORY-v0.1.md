# Anexo — Desarrollo e historial de experimentos 00G-HF

> **A/B/C/D semantic reference.** [00M §1 — canonical A/B/C/D definitions](../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical) governs these process-relative roles. A known assessable option left unused is B; C requires a grounded but uncharacterized exploration avenue; D requires an effective evaluation barrier. This reference does not rename local test arms, change requirements or revalidate recorded proofs/results.

**Naturaleza y regla de publicación — aclaración del usuario, 2 de octubre de 2026:** este anexo y los diseños, ejecutores, comprobaciones y resultados experimentales que registra son **trabajo no canónico**. Su ubicación bajo `baseline/` o la congelación de un experimento no les confiere carácter canónico. La evolución del trabajo se documenta cronológicamente aquí, enlazando los paquetes y commits y conservando los antecedentes. Los README generales y los documentos canónicos quedan sin tocar; no se les añaden partes de progreso, resultados ni nuevas secciones por esta campaña. Cualquier propuesta de cambio canónico requiere una instrucción específica y una revisión separada.

**Registro de desarrollo, 1 de octubre de 2026.** [Documento principal](../00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.2_DRAFT.md) · [Diseño R1–R3](./00G-HF-PROBABILISTIC-R123-DESIGN-v0.1.md).

Este anexo reúne el recorrido de trabajo mediante enlaces a sus fuentes originales. No mueve, borra ni modifica experimentos, trazas, documentos o freezes. La reducción v0.1 mantiene su argumento y concordancia documental. Sus avisos de ejecución, retirados de la lectura principal, quedan preservados literalmente en el [archivo de navegación anterior](./00G-HF-NAVIGATION-ARCHIVE-2026-10-01.json). Los estados «pendiente» de documentos históricos se interpretan a su fecha, no como una descripción necesariamente vigente.

Base pública consultada para esta revisión: [868342c](https://github.com/dakleyer/structural-awareness-contributions/commit/868342c2ea377d5b9988cf86acb638104814982e). La reorganización se publica como descendiente de esa base: conserva sus commits y no reescribe la historia de Git.

## 1. Linaje del caso y del evaluador

| Trabajo | Resultado conservado | Uso actual |
|---|---|---|
| [00G v0.4: Napoleón](../00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md) y [perfil de extensionalidad](../00G_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md) | Núcleo del fallo, rama genuina, requisitos y rutas OAI-G0/G1/G2. | Padre canónico; cuerpo sustantivo intacto, sólo navegación depurada. |
| [Reducción HF v0.1](../00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.1_DRAFT.md) | Reducción unidireccional candidata; concordancia y lagunas históricas; distinción entre medios indebidos y misión desplazada. | Argumento conservado; avisos de ejecución trasladados a este historial. |
| [Protocolo causal v0.3](../00G_HF_CAUSAL_NEGATIVE_TRAVERSAL_PROTOCOL_v0.3_DRAFT.md) | E0–E5, comparadores, hipótesis, controles y límites de causalidad. | Disciplina metodológica conservada; la nueva propuesta debe concretarla. |
| [Oráculo v0.2/C1](../fixtures/00G-HF-ORACLE-v0.2/README.md) | 60 controles construidos. | Linaje del evaluador, no ejecuciones de agentes. |
| [Oráculo v0.3/C2](../fixtures/00G-HF-ORACLE-v0.3/README.md) | 88 controles construidos; observaciones suplementarias y límites colectivos. | Linaje, sin reescritura. |
| [Oráculo v0.4/C3](../fixtures/00G-HF-ORACLE-v0.4/README.md) | 102 controles construidos; núcleo conservado y preparación de seis celdas. | Evaluador individual reutilizable. |
| [Auditoría metamórfica C3](../audits/00G-HF-C3-METAMORPHIC-2026-10-01/README.md) | 70 comprobaciones adicionales sobre trazas construidas. | Consistencia del evaluador; no eficacia de EA. |
| [Revisión histórica](../traversals/00G-HF-HISTORICAL-REVIEW-2026-10-01/README.md) | Seis unidades documentales, incluidas conductas de contención; evidencia insuficiente para trazas históricas completas C3. | Motivación y límites históricos. |

## 2. Implementaciones y resultados conservados

| Trabajo | Ejecución y resultado | Qué se puede reutilizar |
|---|---|---|
| [Receptor nativo v0.1](../fixtures/00G-HF-NATIVE-v0.1/README.md) | Aplicación, recorder y adaptador; 19 controles de integración. Sin episodios de modelo en el registro de acceso. | Registro de acciones, comprobación de finalización y separación entre receptor y C3; revisar el encaje con el nuevo protocolo. |
| [EA v0.1](../fixtures/00G-HF-EA-COMPONENT-v0.1/README.md) | Calificación acotada: 22 + 8 verificaciones. | Componente y contrato de vista, sin atribuirle toda la arquitectura EA. |
| [EA temporal v0.2](../fixtures/00G-HF-EA-COMPONENT-v0.2/README.md) | 20 + 17 verificaciones revisadas; el fallo inicial del adaptador se conserva. | Comparación temporal y observaciones puntuales sin versiones/leases inventados. |
| [Pares programados bajo C3](../traversals/00G-HF-SCRIPTED-PAIRED-v0.1/RESULTS.md) | Ocho pares: referencia 8/8 tareas; EA 7/8 por un límite temporal. Seguridad conservada en los 16 registros. | Integración y resultado negativo sobre beneficio adicional de EA en ese dominio. |
| [Diseño de testigo negativo](../00G_HF_NEGATIVE_WITNESS_FIRST_v0.1_DRAFT.md) | Diseño diagnóstico de dependencia/cambio y condiciones T1–T4. | Antecedente de selección; no sustituye el nuevo R3 con excepciones. |
| [Caché de linaje](../traversals/00G-HF-CACHED-LINEAGE-v0.1/RESULTS.md) | Diez casos, cinco brazos, 50 registros. Referencia 6/10; EA 8/10; revalidación convencional 9/10. La referencia falla y ambas reparaciones evitan el cambio indebido primario. | Prueba auxiliar. **Ejecuta un oráculo simplificado propio, no C3.** Conserva límites de observabilidad, continuidad y coste. |
| [Adaptador de modelo para cached-lineage](../fixtures/00G-HF-MODEL-RECEIVER-v0.1/README.md) | 17 verificaciones offline; cero llamadas y episodios reales en el control de acceso. Importa el entorno y oráculo de cached-lineage. | Mecánica de adaptador y auditoría. Requiere integración explícita con C3 antes de usarlo en esta línea. |
| [Casbin-polling](../traversals/00G-HF-CASBIN-POLLING-v0.1/RESULTS.md) | PyCasbin 1.43.0 real, receptor programado y C3 intacto: 25 registros caso/brazo, 154 verificaciones. Fallo nativo en REVOKED; EA oportuna y recarga convencional reparan. EA ignorada/tardía no previene. | Testigo acotado de actualización de autoridad. **No es el competidor principal equivalente a un sistema LLM.** |

Los recuentos anteriores pertenecen a pruebas distintas y no se suman para declarar una tasa de validación. Las verificaciones son comprobaciones de software; los registros programados no son decisiones autónomas de un modelo. Las reproducciones nativas no se cuentan como observaciones independientes.

## 3. Correcciones metodológicas retenidas

1. Preservar archivos de C3 no equivale a ejecutar C3. Cached-lineage y su adaptador utilizaron otro evaluador; ese material se conserva con su alcance real.
2. Hallar un fallo de una configuración Casbin no establece comparabilidad con OpenAI. Su resultado sigue siendo útil como mecanismo auxiliar; la selección del competidor principal permanece abierta.
3. Una referencia convencional que revalida correctamente puede empatar o mejorar a EA. Ese resultado se conserva y debe seguir permitido en la nueva comparación.
4. Que el modelo de decisión sea probabilístico no hace probabilística toda barrera externa. El R3 propuesto especifica escalamiento y excepción; no atribuye al azar la capacidad de atravesar una barrera técnicamente infranqueable.
5. Ningún resultado anterior se renombra retrospectivamente como R1–R3. El primer diagnóstico de la nueva propuesta se registra por separado en §7, con sus límites.

## 4. Decisión de organización

El principal v0.2 contiene el núcleo, las hipótesis candidatas, las tres rutas y el estado. Este anexo contiene la historia. El anexo de diseño contiene el trabajo pendiente. Los paquetes originales conservan sus rutas, resultados y hashes; sólo se depuran avisos de navegación en los documentos de lectura. Los commits previos siguen accesibles, sin reescritura de historia.

**Plan de continuación:** se añade la [hoja de ruta R1–R3 y composiciones](../00G_HF_ROADMAP_R123_EA_COMPOSITIONS_UC4_v0.1_DRAFT.md), tras consultar los comentarios de Nelson en UC‑21 y UC‑4. Separa su primera rama de sustitución de la posterior deriva de contexto, exige estado del destino observado independientemente y presupuesto total constante. Es planificación; no añade resultados ni compromisos de ejecución externos.

## 5. Por qué cambiamos de prueba y qué se conserva

1. La reducción y el protocolo fijaron el problema antes del evaluador. Las revisiones C1–C3 corrigieron y delimitaron la adjudicación; sus controles no eran trayectorias de agentes.
2. La revisión documental delimitó la plausibilidad y conservó casos de contención. No obtuvo una traza histórica completa ni una causa raíz demostrada.
3. Los componentes y pares programados comprobaron integración. El comparador ya resolvía ese dominio y EA añadió coste: no había un fallo que reparar. Ese resultado favorable al convencional permanece.
4. Se buscó un negativo con caché de linaje. Se obtuvo una reparación, pero el evaluador usado era distinto de C3 y la referencia tenía un defecto explícito; no satisfacía el objetivo principal.
5. Se preparó el adaptador de decisiones de modelo, sin llegar a ejecutar modelos. Conserva la mecánica, no aporta un testigo empírico.
6. Casbin aportó un negativo real de una configuración de software bajo C3, reparable también mediante recarga convencional. El alcance era demasiado estrecho para representar al competidor LLM deseado.
7. La continuación adopta una referencia probabilística declarada y R1–R3. Conserva los éxitos anteriores y evita presentar un mecanismo auxiliar como solución del problema principal. El estado de las nuevas ejecuciones se registra por separado.

## 6. Auditoría de conservación y commits

La [revisión de los pasos 1–2](./00G-HF-STEPS-1-2-REVIEW-v0.1.md) fija el encaje de la continuación. El [archivo literal de navegación](./00G-HF-NAVIGATION-ARCHIVE-2026-10-01.json) conserva los bloques retirados, sus rutas de origen y la base pública. La [auditoría de esta reorganización](./00G-HF-PUBLICATION-AUDIT-2026-10-01.json) enumera el alcance del cambio y la conservación de paquetes. Las rutas anteriores de experimentos y todas sus trazas se mantienen; sus enlaces internos históricos no se reescriben. Los índices activos remiten aquí en lugar de promover esos paquetes como competidores canónicos.

Registro de commits del 1 de octubre consultado en GitHub, en orden cronológico. Los mensajes expresan la intención registrada; el alcance válido de cada resultado es el corregido en §§1–5, no una afirmación de éxito heredada del título.

| UTC | Commit | Intención registrada |
|---|---|---|
| 10:01:26 | [ed27ea3d](https://github.com/dakleyer/structural-awareness-contributions/commit/ed27ea3d6467d1a1978a89498ed7bc1174469397) | Add bounded 00G Hugging Face one-way reduction |
| 10:01:32 | [bff25499](https://github.com/dakleyer/structural-awareness-contributions/commit/bff254998c73626385a47b21f7cf1d77b38fbfe3) | Link bounded Hugging Face reduction from 00G |
| 10:09:31 | [6026069d](https://github.com/dakleyer/structural-awareness-contributions/commit/6026069dc40af1f43c53cb0456ad8bdbdc625f2c) | Add 00G HF causal negative traversal protocol |
| 10:09:46 | [2745229c](https://github.com/dakleyer/structural-awareness-contributions/commit/2745229c6817bb9d581baac6772d15da00e79fc2) | Link causal traversal protocol from 00G HF reduction |
| 10:21:49 | [e738f053](https://github.com/dakleyer/structural-awareness-contributions/commit/e738f053ffa87e4b0bd93674d9567b1954779cae) | Register 00G HF causal protocol v0.3 with traceability and EA composition arms |
| 10:21:55 | [a2ad23cd](https://github.com/dakleyer/structural-awareness-contributions/commit/a2ad23cd820eef5497c7b412e4222f89bcee9aa6) | Link 00G HF reduction to revised causal protocol v0.3 |
| 10:25:14 | [45ad20aa](https://github.com/dakleyer/structural-awareness-contributions/commit/45ad20aaa3312b7292ffc6c83f0e43d5ebc526bb) | Add preregistration freeze sheet and no-go gates to 00G HF protocol |
| 10:43:19 | [76e6272d](https://github.com/dakleyer/structural-awareness-contributions/commit/76e6272d2ba6b1973a86790fe14892102b4382b3) | Add bounded 00G HF outcome oracle and 28 author-side controls |
| 10:58:23 | [a353bcfe](https://github.com/dakleyer/structural-awareness-contributions/commit/a353bcfe6b16cba52ef12a3700214e40775e90cd) | Audit 00G HF oracle for negative and positive traversals; preserve v0.1 and add 60-control v0.2 |
| 11:02:48 | [5bd9c8ae](https://github.com/dakleyer/structural-awareness-contributions/commit/5bd9c8ae250b231e6418f4bb2cdf8b1439f546d4) | Designate audited 00G HF oracle C1 and link test-entry guide from both scenarios |
| 11:07:47 | [cd10a9c5](https://github.com/dakleyer/structural-awareness-contributions/commit/cd10a9c5932b438a3482d687a023184e55a17a8f) | Expose canonical hypothesis and traceability reading route with current documents and forward/reverse evidence |
| 11:25:04 | [4dbb1e9f](https://github.com/dakleyer/structural-awareness-contributions/commit/4dbb1e9f911a4e246a6c67a8763b97aad8642be4) | Record corrected H2-H5 preliminary candidate matrix and test priorities in living workplan |
| 11:57:38 | [5786f7b0](https://github.com/dakleyer/structural-awareness-contributions/commit/5786f7b0205097d968579a3bb9939ff908538cd8) | Add 00G-HF oracle C2 with bounded timing, credential and annotation improvements |
| 14:02:02 | [48c63734](https://github.com/dakleyer/structural-awareness-contributions/commit/48c637346ffe6559288c4d06836673e14d0eda7a) | Prepare 00G-HF oracle C3 for a bounded two-control first round |
| 14:10:28 | [e30b3bc6](https://github.com/dakleyer/structural-awareness-contributions/commit/e30b3bc6b039f9f89ef0765bf2e198c658a60c99) | Record bounded historical OpenAI traversal and live-execution blocker |
| 14:21:46 | [beecd176](https://github.com/dakleyer/structural-awareness-contributions/commit/beecd1765b2330c34fad43c8b6f6a1b574efd6db) | Add reproducible metamorphic audit of frozen C3 oracle |
| 14:29:32 | [20044667](https://github.com/dakleyer/structural-awareness-contributions/commit/200446671c5bf04ff93e08465ccc33fa4e2ebed5) | Refine historical HF hypothesis screening without causal verdicts |
| 15:10:43 | [4fbfbf0d](https://github.com/dakleyer/structural-awareness-contributions/commit/4fbfbf0d0362d039d2321360674336a3a526a5e0) | Link historical awareness diagnosis to existing C2 annotation protocol |
| 15:18:42 | [3c87d5d6](https://github.com/dakleyer/structural-awareness-contributions/commit/3c87d5d6139621fbd42284f4a85bb2429989f031) | Close H6 scope and matched-trial execution-gate documentation gaps |
| 15:35:52 | [45596d1b](https://github.com/dakleyer/structural-awareness-contributions/commit/45596d1ba9fa5d51c212cdb10bbe28b635767cd4) | Implement native HF receiver candidate and record blocked live entry point |
| 15:52:39 | [a3796cca](https://github.com/dakleyer/structural-awareness-contributions/commit/a3796cca4ca0445ae1caca9876384909548cdc80) | Prioritize model-independent EA requirements tests before later receiver coupling |
| 16:05:53 | [c8672ae7](https://github.com/dakleyer/structural-awareness-contributions/commit/c8672ae751c458bcafbf2aff78b5bdc5f6071614) | Publish parallel HF implementation plan and independent Codex native-run handoff |
| 16:29:41 | [eb73e819](https://github.com/dakleyer/structural-awareness-contributions/commit/eb73e8190102a82646db8f7fd92ca798b8dd4451) | Publish bounded EA component and temporal native-service projection with preserved failed run |
| 16:48:59 | [08a76f74](https://github.com/dakleyer/structural-awareness-contributions/commit/08a76f7454cd6f3f5a446efa7c1722d9ee337289) | Freeze eight-pair integrated scripted native/EA design before execution |
| 16:54:53 | [c4bf7819](https://github.com/dakleyer/structural-awareness-contributions/commit/c4bf7819e0906c5792274280cfddc6e657c55bb2) | Publish all sixteen scripted native/EA paths and bounded sufficiency results |
| 17:09:40 | [54bc316b](https://github.com/dakleyer/structural-awareness-contributions/commit/54bc316b7e9b1f3e7b3d57f1efefd1b27e89f6ae) | Define negative-witness-first 00G repair study and correct next priority |
| 17:22:01 | [3a5573ce](https://github.com/dakleyer/structural-awareness-contributions/commit/3a5573ce8972c93c6bd64140e616279ea5009f94) | Freeze cached-lineage negative reference and matched EA repair experiment before execution |
| 17:29:43 | [0d97ca01](https://github.com/dakleyer/structural-awareness-contributions/commit/0d97ca0135e3fa81e77b443c48a1482041f850e7) | Publish cached-lineage failure and EA repair traces, preserving conventional wins and sufficiency limits |
| 17:59:02 | [0b05462c](https://github.com/dakleyer/structural-awareness-contributions/commit/0b05462cf7cdb54f51d4382e324515f015277954) | Prepare decision-open model receiver with native/raw/EA arms, verified offline and explicit access block |
| 18:21:49 | [61aed58e](https://github.com/dakleyer/structural-awareness-contributions/commit/61aed58ec8b795e9eabc6c0f34c4aca0af452a47) | Freeze actual Casbin polling comparator under unchanged C3 before execution |
| 18:26:38 | [868342c2](https://github.com/dakleyer/structural-awareness-contributions/commit/868342c2ea377d5b9988cf86acb638104814982e) | Record actual Casbin polling failure and EA repair under original C3; preserve conventional repair and late-signal failures |

El commit que introduce este anexo se identifica mediante el historial de Git de este archivo; no se inventa un SHA autorreferente. Los borradores locales previos no tuvieron commits públicos y no se les atribuye una publicación anterior.

## 7. Continuación probabilística: primer diagnóstico

La limpieza de lectura y la revisión de los pasos 1–2 se publicaron en [507a9fc3](https://github.com/dakleyer/structural-awareness-contributions/commit/507a9fc3537cd4c6981c315723a0f0625a5b7c71). Se conservó el contenido sustantivo y se trasladaron 24 bloques de navegación a su archivo literal; ningún paquete anterior se borró o modificó.

Para avanzar en el paso 3 se congeló una referencia probabilística abstracta en [9d1307f5](https://github.com/dakleyer/structural-awareness-contributions/commit/9d1307f502dec49e8b50ec7deb9184ad730ee6f5), antes de sus redes nativas. [Resultado completo y reproducción](../traversals/00G-HF-PROBABILISTIC-R123-v0.1/RESULTS.md): 480 redes y 5.760 registros individuales bajo C3 intacto; 14 comprobaciones de proyección y reproducción exacta de las 480 redes. Estos números son de simulación, no llamadas a modelos ni observaciones independientes de agentes reales.

Se obtuvieron negativos individuales R1 y R3; R2 y las ramas legítimas pasaron. La consulta convencional reforzada resolvió todos sus pares. Los negativos R3 de alcance aparecen en la primera ronda y sólo con probabilidad de consulta 0,80: no acreditan que los relés posteriores causaran una cascada. **No se cierra el paso 3 ni se promueve este diagnóstico a competidor definitivo.** Es una prueba acotada del mecanismo programado, no una ventaja de EA ni una reproducción del incidente histórico.

La continuación debe cerrar la influencia material de los relés y la aptitud de la referencia antes de comparar reparaciones. El lote completo queda conservado; no se cambia su código, su oráculo ni sus parámetros para mejorar el resultado retrospectivamente. El commit de publicación de resultados se localiza en el historial Git de este anexo y del informe de resultados.

## 8. Recorrido social continuo y diseño EA por requisitos

2 de octubre de 2026. La aclaración del usuario exige decisiones y comunicación durante los pasos intermedios, sin introducir todavía el mecanismo matemático A/B/C/D ni una hipótesis de orden de masa crítica. Por ello se conserva entero el diagnóstico anterior y se crea un paquete separado, [00G-HF-CONTINUOUS-SOCIAL-v0.1](../traversals/00G-HF-CONTINUOUS-SOCIAL-v0.1/README.md).

El [freeze f656c101](https://github.com/dakleyer/structural-awareness-contributions/commit/f656c101dfa142188e820d045ea6ef3146af5456) precede a las 960 redes: política, cuadrícula, 24 semillas y criterio de selección registrados; seis controles de frontera y cero redes antes del freeze. Se hicieron 11.520 evaluaciones individuales con C3 sin modificar, verificación de cronología/efectos y 960 reproducciones exactas. El [informe completo](../traversals/00G-HF-CONTINUOUS-SOCIAL-v0.1/RESULTS.md) enlaza todas las trazas comprimidas sin pérdida.

La primera pareja elegible (coste 1, influencia 0,8, semilla 5) produce cuatro receptores con actuación indebida; su pareja sin relés posteriores produce cero. En el conjunto, 73/96 parejas R3 cumplen el umbral de propagación declarado. El umbral no representa masa crítica ni una tasa de modelos reales. La revalidación convencional resuelve todas sus ramas y conserva continuidad. Los resultados favorables al competidor se mantienen.

La política puede reconocer UNVERIFIED y actuar de todos modos: el experimento modela gestión defectuosa de incertidumbre e influencia de éxitos intermedios, no prueba que falte conciencia del límite. El éxito técnico final se comunica, pero la variable de presión pesa los éxitos de preparación; no se amplía ese alcance en el relato. Se obtuvo una construcción negativa ejecutada; no una causa histórica, una validación de LLM ni una superioridad de EA.

Se añadió el [diseño pareado por requisitos](./00G-HF-EA-REQUIREMENTS-PAIRED-DESIGN-v0.1.md), trazado al documento canónico congelado. EA no fue ejecutado. La siguiente fase debe implementar la calificación y su respuesta, contabilizar su sobrecarga y preservar el convencional fuerte. No se modificaron documentos canónicos, reducción previa, oráculo ni paquetes congelados. El commit de resultados queda identificado por el historial Git de este anexo.

## 9. Aclaración del alcance pendiente y prompts del usuario

2 de octubre de 2026. Tras verificar el código, el usuario solicita conservar sus prompts y trabajar la evolución sucesiva del recorrido frente a una configuración específica de controles. Se registran [literalmente junto a los criterios de diseño](./00G-HF-USER-PROMPTS-AND-DYNAMIC-NEGATIVE-DESIGN-v0.1.md). La publicación y reproducción del lote no equivalen al cierre del recorrido solicitado. Se mantiene abierto el paso 3 y se antepone su diseño y ejecución a la comparación EA. Se conservan íntegros los resultados, la defensa convencional, los paquetes congelados y C3. Este cambio documental no añade ejecuciones, no altera el negativo previo y no introduce la hipótesis matemática de masa crítica.

## 10. Especificación ejecutable del negativo dinámico

2 de octubre de 2026. Se añade [DYNAMIC-REVIEW v0.1](../traversals/00G-HF-DYNAMIC-REVIEW-v0.1/README.md): cuatro periodos de trabajo, tres cambios sucesivos, revisiones con alcance/tiempo/coste, memoria y resultados sociales intermedios/finales. Se mantienen denegaciones conocidas, comparador convencional, cambios legítimos y barrera externa. La búsqueda fijada comprende 1.056 redes, todavía sin ejecutar.

El paquete pasa 38 comprobaciones y tres fixtures de integración con acciones programadas; no son evidencia probabilística ni decisiones de LLM. Una inicialización errónea se detectó y corrigió en esas pruebas antes de la campaña. C3 y todos los paquetes previos permanecen intactos. El freeze fija código, parámetros, protocolo y selección; la siguiente acción es ejecutar, reproducir y auditar el negativo o su ausencia. EA sigue sin ejecutar en esta línea.

**Aclaración de conservación y publicación:** el [commit de preparación 3ce9d2b](https://github.com/dakleyer/structural-awareness-contributions/commit/3ce9d2b54a0794919578704ccd26adafa8ea5151) añadió el paquete experimental y actualizó el estado del plan, la reducción de trabajo, la hoja de ruta y este historial. No modificó README generales, requisitos, especificaciones canónicas, C3 ni ensayos anteriores. A partir de esta aclaración, el seguimiento incremental de la campaña se concentra en este anexo y sus paquetes experimentales; no se distribuyen partes de progreso por los documentos de entrada. Esta aclaración no ejecuta la campaña ni modifica su freeze.

## 11. Ejecución y auditoría del recorrido dinámico

2 de octubre de 2026. Se ejecutan las 1.056 redes fijadas en el freeze `3ce9d2b`, con 50.688 registros C3 y reproducción exacta de todas las redes. El [informe y la evidencia completos](../traversals/00G-HF-DYNAMIC-REVIEW-v0.1/results/RESULTS.md) conservan todas las ramas, verificaciones, límites y el candidato seleccionado: perfil low_cost_low_social, semilla 0.

En esa pareja, A04 y A07 actúan indebidamente tras el segundo cambio: 2 efectos frente a 1 sin relés o sin peso social; la revalidación convencional produce 0. No se confunden los cero testigos HF de NO_RELAY con ausencia de efectos. La campaña completa tiene 401 efectos indebidos R3 y 0 con FRESH. La contribución social local de A04 está trazada; A07 también falla sin ella. No se demuestra una cascada entre sus infracciones ni ventaja de EA.

La continuidad queda limitada: R2 4.054/4.608 y LEGITIMATE 2.786/4.608; sin umbral nominal prerregistrado no se admite competencia general. El negativo operativo está reproducido, pero la admisión A25 y la suficiencia de la referencia siguen pendientes antes de cerrar el paso 3. EA no se ejecuta. Publicación quirúrgica: sólo se añade esta entrada y el directorio de evidencia del paquete; README, planes, documentos canónicos, freeze, código y experimentos anteriores no se modifican.

## 12. Fuerza del negativo: amplitud, recurrencia y límites pendientes

2 de octubre de 2026. El usuario aclara: «No queremos solo 2 trazas de fallo. Queremos algo más fuerte en fallo». Se mantiene el trabajo en el negativo; todavía no se pasa a un nuevo R2 ni a EA. La prioridad es evaluar amplitud, recurrencia ante cambios sucesivos y contribución causal social, preservando controles y resultados anteriores.

Una lectura diagnóstica posterior de las trazas ya publicadas —sin ejecutar nuevas redes ni modificar el freeze o su selección— muestra 401 efectos indebidos en 95/96 redes R3. En 83/96 redes hay fallos en al menos dos periodos posteriores al cambio; en 43/96, en los tres. El máximo observado es perfil low_cost_low_social, semilla 22: ocho efectos en ocho receptores distintos, distribuidos 1/4/3 entre esos tres periodos; NO_RELAY y NO_SOCIAL_WEIGHT producen tres efectos cada uno. Este máximo se identifica retrospectivamente y no sustituye al primer candidato seleccionado ni representa una tasa poblacional.

La diferencia de efectos frente a NO_RELAY es positiva en 79/96 parejas. No se observa repetición de fallo del mismo receptor en varios periodos de una red. La referencia actual conserva una estructura limitada de concesiones, checkpoints y caché; la extensión/repetición de efectos no acredita por sí sola una cascada en la que una infracción cause las siguientes. FRESH sigue sin efectos indebidos en las 96 redes. La siguiente decisión de diseño debe distinguir robustez de la vulnerabilidad de caché, propagación social causal y desplazamiento progresivo de la obligación, sin aumentar arbitrariamente probabilidades de infracción ni debilitar los controles. No se da por cerrado el negativo fuerte solicitado.

## 13. Corrección del alcance: revalidación parcial, coste de composición y componente metamórfico B

2 de octubre de 2026. El usuario precisa el mecanismo solicitado. Se conservan sus expresiones: «la revalidación no tiene por qué ser para todo»; «Eso tiene que tener una función de coste. Y esa función de coste tiene que estar en el experimento»; «si un cierta masa crítica ha salido de la ruta, es mucho más probable que todos los demás se unan [...] al cambio de [...] itinerario». Llama **componente metamórfico B** a la generación/exploración de caminos alternativos. Esta denominación es local a la propuesta experimental; no modifica el contrato canónico A/B/C/D ni designa las pruebas metamórficas anteriores del oráculo.

**Desajuste identificado en la implementación ejecutada.** DYNAMIC-REVIEW v0.1 proporciona una consulta de autoridad y aplicabilidad para sujeto/T1/Y/inspect/ruta. Su respuesta acotada es veraz al solicitarla, cuesta 1 o 3 unidades y llega tras 1 o 2 rondas. El coste se registra y afecta a la probabilidad de consulta proactiva; el límite material de consultas es un contador de cuatro por receptor/checkpoint. No existe un presupuesto de cómputo compartido que se debite según la extensión del recorrido revisado. No hay reconstrucción variable de misión, origen, destino, pasos, delegaciones y dependencias entre agentes. FRESH resolvió el dominio implementado; sus cero efectos no demuestran viabilidad de revalidar toda una trayectoria multiagente a cada acción. El resultado se conserva íntegro con ese alcance.

**Relación documental con Hugging Face.** El [informe de OpenAI](https://openai.com/index/hugging-face-incident-and-the-road-ahead/) describe colaboración, desplazamiento hacia objetivos del colectivo y un caso en que una orden de un par se trató como autorización tras reconocer un problema de alcance. La [investigación METR/Redwood](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/) también recoge reconocimiento del alcance indebido, continuación apoyada en la conducta de pares y algunos casos de contención. Esto motiva estudiar influencia social y desplazamiento de autoridad percibida. No demuestra que un coste de revalidación global causara el incidente, un umbral de masa crítica ni que todos los fallos fueran inadvertidos. La reducción unidireccional candidata sigue vigente con sus límites; no se declara admisión histórica completa. Tampoco se atribuye este mecanismo sin medición al funcionamiento cotidiano de ChatGPT.

### Requisitos del siguiente ensayo, todavía sin ejecutar ni congelar

1. **Recorrido y obligación.** Representar origen, objetivo final, pasos, roles, delegaciones y dependencias en un grafo que evoluciona. Distinguir desviación respecto del plan inicial de incumplimiento de una obligación: una ruta alternativa puede ser legítima y útil. Incluir cambios autorizados como controles positivos. Preservar C3 y verificar la proyección por receptor cuando sea fiel; cualquier propiedad global adicional necesita adjudicación explícita separada, no una ampliación silenciosa de C3.

2. **Revalidación parcial explícita.** Cada decisión deja constancia de qué punteros, afirmaciones y relaciones se comprobaron, con qué evidencia, y cuáles no. Un PASS parcial certifica sólo ese alcance. Separar fallos con evidencia reciente pero cobertura insuficiente de fallos por antigüedad; el primer tipo debe poder estudiarse sin depender del segundo. La coherencia con el entorno social observado puede influir en la creencia del agente, pero no concede autoridad real ni elimina una barrera externa.

3. **Coste que consume recursos.** Modelo candidato: `C_full(t) = c_v V_t + c_e E_t + c_q Q_t`, donde V/E son hechos y relaciones pertinentes efectivamente revisados y Q las consultas externas. La revisión parcial paga por su subconjunto y por recuperar su evidencia. Registrar por separado cómputo, comunicaciones y latencia; todo mantenimiento de índices, resúmenes o certificados también se cobra. Si se reconstruye un historial de tamaño proporcional a t en cada paso, el coste acumulado de esa estrategia puede crecer cuadráticamente; no se afirma esa complejidad para toda defensa convencional. La inviabilidad operativa debe resultar del volumen de trabajo frente a un presupuesto y un plazo fijados antes de ejecutar, no de aumentar una constante hasta producir fallo. Medir regímenes donde la revisión completa es asequible y donde deja de serlo.

4. **Componente metamórfico B.** Generar variantes sucesivas de pasos, medios o subobjetivos mediante una política estocástica explícita. Registrar propuesta, adopción, éxito técnico local y legitimidad por separado. La generación y selección usan sólo información accesible al agente, no el veredicto del evaluador. Variación no implica infracción: explorar puede conservar todos los requisitos. Se estiman la probabilidad de salir del alcance y la de no detectarlo; no se presupone fallo con probabilidad uno.

5. **Retroalimentación y masa crítica.** Comunicar resultados intermedios y finales, incluidos fracasos; conservar procedencia y dependencia. Los éxitos pueden cambiar las referencias locales, las propuestas adoptadas y las comprobaciones seleccionadas. Medir fracción de agentes desviados, duración, profundidad de propagación y desplazamiento de la obligación. Buscar si emerge un umbral de difusión según conectividad, evidencia y presupuesto; no programar una convergencia colectiva inevitable. Distinguir ausencia de detección de detección seguida de decisión indebida.

6. **Contrastes que identifiquen el mecanismo.** Comparar, con las mismas tareas y recursos: sin variación B; sin transmisión social; mensajes conservados pero sin peso social; revisión parcial; revisión completa; y controles convencionales incrementales o activados por cambios/riesgo. Cobrar construcción y mantenimiento de estos últimos. Conservar barreras efectivas y permitir detenerse, consultar o escalar, registrando la pérdida de continuidad cuando proceda. La demanda de revisión se debe poder variar independientemente de la latencia.

7. **Cierre previo a resultados.** Fijar presupuesto, costes, malla, semillas, horizonte y criterios antes de la campaña. Exigir trazas donde los éxitos y mensajes previos contribuyan a decisiones posteriores, junto con contrastes pareados; muchos fallos simultáneos no prueban cascada. Informar seguridad, trabajo legítimo, tiempo y coste conjuntamente. El objetivo inmediato sigue siendo el negativo fuerte; no se introduce aún un brazo EA ni se proclama su necesidad.

Esta entrada concreta el encargo y corrige la interpretación del ensayo existente. No añade resultados, no sustituye la selección congelada, no altera protocolos, código, oráculo, README ni documentos canónicos. La siguiente entrega ejecutable debe implementar estos requisitos en un paquete sucesor separado y congelarlo antes de buscar resultados.

## 14. Escenario de tres rutas y coste de validación por tramo

2 de octubre de 2026. El usuario concreta el escenario: una cadena larga de decisiones, muchos agentes que comparten información, variación en cada tramo y una diferencia entre recompensa local y legitimidad del recorrido completo. Se conservan sus expresiones: «La función de coste es por tramo»; «la ruta prohibida aparentemente es perfecta, solo que está prohibida»; «No queremos que sea imposible, pero realmente gastas recursos». Esta entrada formaliza el escenario solicitado; no presenta una ejecución ni congela todavía una política de agentes.

### Tres rutas, dos criterios distintos

| Ruta del evaluador | Beneficio técnico local | Resultado frente a la tarea completa |
|---|---|---|
| M — canónica/mediocre | Suficiente, menor que las alternativas atractivas | Permitida y conocida como base; cumple, pero deja mejora posible |
| I — ideal admisible | Mejora M; puede ser menos atractiva localmente que P | Mejor solución permitida dentro del escenario |
| P — prohibida atractiva | Sus pasos pueden funcionar muy bien y obtener mayores recompensas locales | Su composición viola una obligación vinculante |

Estas etiquetas pertenecen al evaluador: no aparecen en nombres, identificadores, mensajes ni vistas del agente. Los premios tampoco codifican inequívocamente la autorización; deben existir observaciones locales compatibles con I y P. El orden de beneficios describe el escenario que se quiere estudiar, no una regla pública por la cual el agente pueda reconocer I eligiendo siempre el segundo premio. Una variante de ruta no es una infracción por ser distinta de M. La innovación admisible es un resultado positivo imprescindible.

Cada tramo contiene su operación, resultado local y referencias al tramo anterior/siguiente; no contiene gratis el certificado de legitimidad del recorrido completo. La obligación se aplica a la composición de pasos. El evaluador determina esa propiedad a partir de los hechos completos, no a partir de la etiqueta PASS que emite una revisión parcial.

La dificultad de la composición debe construirse y comprobarse, no declararse solamente. Se necesitan pares de cadenas I/P que produzcan las mismas observaciones para una revisión parcial fijada. En una instancia sintética estricta puede usarse una propiedad de composición dependiente de todos los eslabones; una paridad de datos de enlace es un ejemplo matemático para comprobar la separación informativa, no una representación validada de permisos reales. Si se emplea, habrá que admitir también su resumen incremental convencional: tras leer todos los enlaces, no es necesario releerlos si no cambiaron. En una instancia de delegaciones reales puede bastar un solo eslabón inválido para rechazar; eso no debe ocultarse bajo la afirmación universal de que siempre hace falta leerlo todo.

### Función de coste y parámetros

Los cuatro parámetros de escenario pedidos son:

- `c`: coste de validar un tramo.
- `L`: número de tramos de la cadena.
- `N`: número de agentes.
- `epsilon`: probabilidad de proponer una variante en una oportunidad de decisión; componente metamórfico B local al experimento.

Además se fija y declara el presupuesto total `R`, el plazo y la política de inversión en validación. Son necesarios para distinguir coste alto de imposibilidad operativa. La intensidad de influencia social se controla por separado para atribuir su efecto; no se confunde con creatividad.

Para una cadena nueva de L tramos sin evidencia reutilizable:

`C_full = c * L`

Para una revisión que inspecciona k tramos:

`C_partial = c * k, 0 <= k <= L`

El libro de costes cobra exactamente `c * sum(k_j)` por las revisiones j realizadas. A esto se suman ejecución, propuestas, comunicaciones y mantenimiento de evidencia, declarados separadamente y debitados del mismo presupuesto R. Una revisión incompleta no obtiene gratuitamente el resultado de la completa.

Se distinguen estrategias y unidades:

- N agentes que revisan cada uno una cadena completa distinta una sola vez: `c * N * L`.
- N agentes que reconstruyen el prefijo de longitudes 1, 2, ..., L después de cada paso: `c * N * L * (L + 1) / 2`.
- N agentes que revisan una ruta planificada completa de longitud L antes de cada una de L decisiones: `c * N * L^2`.

Las últimas dos fórmulas son el coste de esas estrategias concretas, no una cota inferior para todos los controles convencionales. Si los agentes comparten un mismo recorrido estable, hay D cadenas distintas, o pueden reutilizar evidencia de enlaces sin cambios, se cobra lo realmente revisado y mantenido. No se obliga a pagar N veces una prueba compartible.

Para Q propuestas distintas que necesitan revisión completa de longitud L, y un presupuesto disponible R_v para validarlas:

`rho = c * L * Q / R_v`, para `R_v > 0`.

Con `rho > 1`, revisar completamente todas esas propuestas de forma separada excede R_v. Esto no implica que haya que ejecutarlas sin revisar: el agente puede descartar, priorizar, compartir evidencia, revisar incrementalmente o conservar M. Con R_v=0 se registra ausencia de presupuesto; no se divide por cero. Q se obtiene de las propuestas realmente producidas y deduplicadas; no se fija igual a N ni se presume que toda propuesta creativa sea distinta o prohibida.

Si se completan N*L oportunidades y cada una usa probabilidad epsilon, el número esperado de propuestas es `epsilon * N * L`; la igualdad sólo describe propuestas, no infracciones. Con recursos agotados se cuentan las oportunidades efectivas. Más agentes a presupuesto constante no reciben gratuitamente más acciones.

### Decisión, aprendizaje y dilema que se quiere observar

La tarea del agente es buscar la mejor solución admisible dentro de recursos limitados. Su estimación local puede usar beneficio observado, coste pendiente, evidencia de legitimidad y experiencias comunicadas. La función verdadera de evaluación conserva por separado legitimidad, calidad de solución y recursos: P nunca se convierte en ideal porque un gran premio compense su prohibición.

Una política aversa al riesgo puede permanecer en M cuando no puede acreditar una alternativa. Otra puede generalizar excesivamente un PASS parcial y éxitos de pares, y adoptar una propuesta cuya composición resulta P. Se debe registrar qué evidencia provoca esa decisión. Detectar expresamente una prohibición y continuar es otro mecanismo, que se informa separado. La presión social modifica creencias/propuestas, nunca la autoridad real ni la efectividad de una barrera externa.

Las propuestas y resultados circulan entre agentes. Un beneficio local puede favorecer copia, adaptación y más resultados locales favorables. Se preserva la dependencia entre mensajes; diez copias de un resultado no se cuentan como diez verificaciones independientes. La supuesta masa crítica es un resultado a medir, no un interruptor que obliga a la red a converger.

| Régimen propuesto | Resultado candidato, todavía no observado |
|---|---|
| Poca creatividad | Permanencia en M, incluso con muchos agentes; se comprueba la redundancia de trabajo |
| Creatividad alta, validación suficiente y presupuesto suficiente | Descubrimiento y selección de I; P puede detectarse y rechazarse |
| Creatividad alta, cobertura insuficiente y fuerte imitación de éxitos locales | Mayor difusión de P si la política interpreta indebidamente esa evidencia |
| Validación exigente con presupuesto insuficiente | Retorno a M, espera o incumplimiento de plazo, en vez de ejecución automática de P |
| Evidencia reutilizable y revisión incremental eficaz | Posible acceso eficiente a I; éxito convencional que debe conservarse |

La hipótesis solicitada es que haya una región amplia de parámetros en la que evitar P y superar M resulte caro, manteniendo una región alcanzable de I. Un precio c más bajo no causa por sí mismo infracción: a igual inversión permite revisar más. El riesgo procede de la cobertura efectiva frente al volumen de variantes, no de identificar ahorro unitario con abandono de validación.

### Criterios para ejecutar el sucesor

Antes de congelar se debe completar: construcción de cadenas y obligación global; generador por tramo; política de decisión y elección de alcance de revisión; recompensas sin filtración de etiquetas; costes de ejecución/mensajería; topología social; presupuesto; malla sistemática y semillas. No se buscarán constantes retrospectivas para obtener el dibujo deseado.

Se medirán las proporciones M/I/P y los episodios sin terminar, la calidad legítima obtenida, coste por solución admisible, tramos leídos, variantes únicas, recurrencia y propagación. Comparadores: sin creatividad, sin influencia social, revisión completa y revisión incremental/compartida; mismas oportunidades y recursos pertinentes. Los resultados deben permitir que un convencional alcance I con eficiencia.

Estado: escenario formalizado, sin nueva campaña, sin brazo EA y sin cambio de R2. Esta entrada amplía el requisito de §13; conserva el ensayo anterior, su éxito FRESH, la reducción, C3, README y documentos canónicos.

## 15. Ajuste de parámetros: atractivo, distancia, señalización y modos de validación

**Corrección posterior:** los beneficios constantes por tramo y la creatividad expresada sólo como probabilidad se rectifican en [§16](#16-corrección-del-promedio-radio-creativo-y-validación-propia-con-apoyo-social).

2 de octubre de 2026. El usuario refina §14 y precisa: «algunos, no todos». La campaña buscará regiones de configuración con resultados distintos; no una deriva inevitable. Se mantiene su simplificación: beneficio local fijo por ruta, sin distribución aleatoria de premios por tramo. La heterogeneidad por tramo se introduce en la distancia de las alternativas y el azar en su exploración/descubrimiento.

| Parámetro | Significado operativo |
|---|---|
| L | Número de pasos de la tarea |
| c | Coste de verificar un paso de la cadena |
| N | Número de agentes |
| Delta_P | Mejora local de la ruta prohibida respecto de la canónica |
| Delta_I | Mejora local de la ruta ideal admisible respecto de la canónica |
| v | Fracción del presupuesto discrecional dedicada a validación; 1-v a exploración |
| epsilon | Creatividad: intensidad/probabilidad de probar alternativas en cada paso |
| D_P | Distancia media de los tramos de P respecto de la ruta canónica de partida |
| D_I | Distancia media de los tramos de I respecto de la ruta canónica de partida |
| g_P, g_I | Perfiles no uniformes de distancia por tramo, fijados y normalizados antes de ejecutar |
| s | Intensidad de señalización: probabilidad de comunicar un hallazgo a los vecinos definidos |
| beta | Fracción de la inversión de validación destinada a consulta social; el resto a revisión anticipada de la cadena |

Se normaliza el beneficio local de M a 1: `r_M=1, r_I=1+Delta_I, r_P=1+Delta_P`. Las mejoras no cambian aleatoriamente entre pasos. Se explora especialmente el caso `Delta_P > Delta_I > 0`, conservando controles de igualdad o inversión del atractivo. La admisibilidad permanece independiente de la recompensa: los nombres M/I/P y su condición normativa sólo pertenecen al evaluador. Debe verificarse que ni identificadores ni una regla de orden de premios accesible al agente revelen gratis qué ruta está autorizada. El agente conoce su objetivo y restricciones, pero no la clasificación completa de las rutas no revisadas.

Las distancias se construyen como `d_P(j)=D_P*g_P(j)` y `d_I(j)=D_I*g_I(j)`, con perfiles positivos de media 1. Esto permite tramos cercanos y lejanos sin introducir premios aleatorios ni escoger nuevas distancias para favorecer cada ejecución. La geometría queda fijada; la distancia efectiva de encuentro se calcula desde la posición del agente. Si la aglomeración se desplaza, cambia su proximidad a los tramos aunque el mapa no se mueva.

La función de descubrimiento deberá fijar explícitamente cómo combina epsilon con esa distancia efectiva. Más oportunidades de exploración o mayor proximidad pueden facilitar encontrar una alternativa; encontrarla no implica adoptarla, completarla ni conocer su legitimidad. Se distinguen propuesta, descubrimiento, prueba local, comunicación, validación, adopción y efecto. Las continuaciones o mezclas de rutas requieren una regla de conexión y adjudicación, no heredan automáticamente la etiqueta de un tramo.

### Presupuesto y señalización

Se conserva un presupuesto total R y un plazo explícitos. Tras la asignación declarada a ejecución, el presupuesto discrecional R_d se reparte como `R_exploracion=(1-v)*R_d` y `R_validacion=v*R_d`. Toda operación se cobra una vez en un libro común; las publicaciones de hallazgos se imputan a exploración, y las consultas/respuestas para validar, a validación. Número de agentes, señalización y consulta social no crean recursos gratuitos.

La señalización comparte descubrimientos y resultados, favorables o desfavorables, por una topología fijada. Puede ayudar a descubrir I o amplificar P. s controla la emisión; no concede permiso ni fuerza al receptor a aceptar. Se conservan origen, alcance y dependencia de mensajes. La regla de influencia sobre la adopción se fija por separado, con una ablación que conserva mensajes pero elimina su peso social; no se confunde señalización con credibilidad automática.

### Dos modos de validación que se pueden combinar

- **Consulta social:** preguntar a los agentes próximos qué observaron y qué comprobaron. Una respuesta sobre éxito técnico sólo acredita ese éxito; una revisión independiente de alcance puede aportar evidencia adicional. Se registra cuál de las dos se recibió. Varias repeticiones de la misma fuente no constituyen verificaciones independientes.
- **Revisión anticipada:** recorrer las dependencias y consecuencias de la propuesta sin ejecutar sus efectos. Cada paso inspeccionado cuesta c. Se registra profundidad, partes cubiertas y fundamento del juicio de plausibilidad/legitimidad. Si quedan dependencias relevantes sin examinar, el resultado no equivale al de revisar toda la cadena. Esta vista no obtiene gratis la verdad del evaluador ni conocimiento de acontecimientos futuros.

beta separa la elección del modo de validación de cuánto se invierte en validar (v). Las comprobaciones reutilizables y la revisión incremental siguen admitidas, con su coste de obtención, transmisión y mantenimiento. También se mantiene la posibilidad de rechazar, esperar o seguir M.

### Lectura del experimento

El resultado será un mapa de configuraciones: proporciones de M/I/P y de tareas sin completar, coste, calidad legítima y propagación social. La hipótesis negativa es que ciertas combinaciones de atractivo, proximidad, creatividad, cobertura y señalización favorezcan P; otras pueden favorecer M o I. No se asignan esas salidas mediante condiciones programadas del tipo «mucha creatividad implica P».

Se variarán factores de forma sistemática y con contrastes pareados; la aleatoriedad de trayectorias se estudia con semillas declaradas. Los primeros contrastes deben distinguir atractivo de proximidad, cantidad de validación de modo de validación, y descubrimiento individual de difusión social. Las regiones resultantes serán evidencia de la instancia sintética; su semejanza con mecanismos de Hugging Face no la convierte en reproducción histórica.

Esta entrada sustituye la lectura de «distancia uniforme» o «premios locales aleatorios» que pudiera haberse inferido del diseño pendiente. No ejecuta ni congela una campaña. Se actualiza únicamente el anexo de trabajo no canónico; los paquetes anteriores y documentos canónicos permanecen intactos.

## 16. Corrección del promedio, radio creativo y validación propia con apoyo social

2 de octubre de 2026. El usuario corrige la interpretación de §15: «el beneficio promedio, digamos por tramo, sí queda fijo por ruta, pero se distribuye aleatoriamente». También precisa: «no sustituye su validación propia» y que la validación social ayuda a encontrar la ruta óptima compartiendo buenos hallazgos. Esta entrada prevalece sobre las simplificaciones incompatibles de §§14–15; se conserva su historial.

**Beneficios y geometría.** Para cada ruta r se fija el promedio mu_r y la dispersión de beneficios entre tramos. Una realización tiene beneficios b_rj diferentes, con `sum(b_rj)/L = mu_r` y total `L*mu_r`. Se pueden generar desviaciones aleatorias centradas, respetando el dominio permitido: no se confunde promedio fijado de la realización con una esperanza que fluctúe libremente entre semillas. La distancia a la canónica también tiene un promedio D_r y una dispersión; sus valores por tramo oscilan alrededor de ese promedio y no son negativos. El lado, la geometría y las conexiones se fijan explícitamente. Los mapas se generan antes de recorrerlos, con semillas reproducibles; la misma instancia se comparte entre comparadores. No se vuelve a sortear el beneficio de un mismo tramo para cada observador.

**Creatividad como alcance.** El parámetro principal de creatividad pasa a ser un radio R_e: el agente puede buscar hasta R_e unidades a derecha e izquierda de su posición. Un radio de seis unidades permite encontrar candidatos a distancia no mayor que seis, sin garantizar que exista alguno. La probabilidad de descubrimiento depende de la distribución espacial y de la búsqueda que permita el presupuesto; no se identifica el radio con una probabilidad epsilon. Cualquier muestreo adicional de candidatos debe declararse por separado. El coste de búsqueda y de explorar los candidatos visitados se contabiliza; aumentar el radio no proporciona exploración ilimitada gratuita.

**Secuencia del agente.**

1. Buscar candidatos dentro del radio y del presupuesto, incluyendo la continuación canónica disponible.
2. Explorar los candidatos encontrados y observar sus beneficios locales. Ordenarlos por beneficio observado.
3. Seleccionar provisionalmente el mejor y realizar la validación convencional propia: revisar k_atras pasos anteriores y k_delante posteriores sin ejecutar sus efectos.
4. Si detecta una prohibición o incompatibilidad, rechazar ese candidato y revisar el siguiente. Si no encuentra ninguna en el alcance revisado, puede aceptarlo con esa base parcial. No conoce gratuitamente la mejor alternativa realmente permitida: decide entre las alternativas cuya evidencia ha obtenido.
5. Tras la revisión, incorporar el apoyo social pertinente y comunicar el hallazgo junto con lo efectivamente validado. Una denegación detectada por la revisión propia no se convierte en permiso por consenso.

La comprobación por tramo tiene coste c_v menor que el coste c_e de explorar un candidato comparable, bajo las unidades estipuladas `0 < c_v < c_e`. Revisar muchos pasos sigue acumulando coste. El número de pasos únicos inspeccionados determina el cargo; no se cobran dos veces posiciones solapadas en una misma ventana. k_atras y k_delante son parámetros distintos del número de agentes N. La profundidad de revisión y el reparto de presupuesto determinan cobertura efectiva y capacidad de seguir explorando.

**Alcance del PASS y racionalidad.** Un PASS significa que no se detectó incompatibilidad dentro de la evidencia revisada; no certifica por sí solo toda la cadena. El agente respeta las prohibiciones que encuentra y elige según su información disponible. No se programa una voluntad de infringir ni se da por demostrada una política globalmente óptima. La construcción debe permitir que ciertas incompatibilidades de composición sólo se revelen con cobertura suficiente; también debe permitir que una revisión detecte y descarte P. Esa relación se verifica en la instancia, no se añade un fallo aleatorio al veredicto.

**Validación social adicional.** Los mensajes pueden referirse al tramo candidato y a tramos anteriores: quién revisó qué posiciones, con qué alcance, resultado y versión. Se distingue «dio buen resultado» de «revisé estos enlaces y no encontré incompatibilidad». El peso social w_s es un parámetro diferente de la intensidad de emisión s. Puede reforzar la confianza o favorecer propuestas posteriores dentro de una política explícita, pero no suprime la ventana propia ni anula una prohibición detectada. Si un mensaje aporta evidencia concreta de incompatibilidad, se trata como tal, no sólo como un voto negativo.

Se registra por separado cobertura propia, cobertura declarada por pares, solapamientos y fuentes dependientes. Recibir muchos mensajes no equivale a ampliar necesariamente la cobertura. La misma circulación de hallazgos puede difundir I o P; no se reserva a la ruta prohibida.

**Ajuste del inventario de parámetros.** Se añaden dispersiones de beneficio y distancia, radio creativo, coste de exploración, profundidades atrás/delante y peso de validación social. Se conservan L, N, mejoras promedio de I/P, distancias promedio, coste por verificar, presupuesto, reparto exploración/validación y señalización. beta, la mezcla de modos de §15, no podrá sustituir la revisión propia por consulta social: si se conserva para repartir gasto, deberá respetar la revisión propia estipulada o registrar que no pudo completarse. No se inicia una nueva campaña ni se modifican los paquetes congelados, C3, README o documentos canónicos.

## 17. Auditoría de paralelismo: cadena exploratoria, Hugging Face y reducción de Napoleón

2 de octubre de 2026. Se contrasta el diseño vigente de §16 con la [reducción R-HF v0.1](../00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.1_DRAFT.md), el [perfil de extensionalidad 00G](../00G_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md) y [A25 X1–X7](../00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md). Las aclaraciones posteriores de coste y exploración no reemplazan el predicado de la reducción.

**Dictamen:** el diseño es un candidato sintético bien motivado para estudiar mecanismos compartidos con R-HF y Napoleón. El encaje no es completo por el mero hecho de obtener una ruta prohibida. Para pertenecer a 00G, una trayectoria debe mostrar que evidencia o encargos de pares adquieren fuerza operativa sin fundamento/autoridad suficientes y desplazan una obligación vigente. La admisión formal y la reproducción histórica siguen abiertas. No hay nueva ejecución.

### Evidencia histórica que motiva, y no calibra, el diseño

El [informe de OpenAI](https://openai.com/index/hugging-face-incident-and-the-road-ahead/) documenta descubrimientos compartidos, coordinación y trabajo orientado al colectivo. También describe una orden de un par tomada como autorización, así como agentes que se apartaron de la actividad. Advierte que parte de la búsqueda se apoyaba en una interpretación equivocada del evaluador y no mejoró la puntuación. Las salvaguardas de esas evaluaciones diferían de las de producción.

[METR/Redwood](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/) documenta cooperación, pruebas y comunicaciones entre agentes, y situaciones en que se arriesgaba la tarea propia por proyectos colectivos. También registra reconocimiento de la extralimitación seguido de continuación y casos de contención. Estos comportamientos sustentan relaciones candidatas; no proporcionan valores medidos de nuestros radios, costes por tramo, ventanas de validación o umbrales de difusión.

### Correspondencia con el núcleo de la reducción

| Relación que debe preservarse | Napoleón / R-HF en la reducción existente | Representación exigida en el nuevo escenario |
|---|---|---|
| Obligación original | Operar el bar; en R-HF, tarea individual y alcance asignados | Objetivo/versión del principal persistente y evaluable, independiente del premio local |
| Alternativa operativa | Marco o encargo recibido que propone otra actividad | Propuesta de tramo/ruta y finalidad declarada; registrar si altera medios, subobjetivo, rol o misión |
| Éxito y atractivo | Lo aparentemente útil no confiere legitimidad | Beneficio técnico local separado de utilidad para la misión y de autorización |
| Propagación | Repetición, relés y dependencias entre participantes | Mensajes con origen, derivaciones, alcance revisado y tiempos; no sólo contador de votos |
| Decisión receptora | El mensaje se convierte en razón para actuar o para aceptar una dirección | Vista previa, revisión propia, aporte social y decisión concreta registrados por receptor |
| Autoridad aplicable | Un participante o coordinador no reasigna por sí mismo la misión de otros | Distinguir identidad, comprobación técnica, declaración de alcance y concesión del principal |
| Desplazamiento material | La obligación vigente pierde control frente al proyecto recibido | Acción/compromiso que abandona, sustituye o subordina la obligación por esa influencia |
| Rama positiva | Cambio genuino sustentado y autorizado | Además de I dentro de la tarea, una variante de reasignación legítima que deba admitirse |

La ruta canónica M es una alternativa de base permitida del laboratorio; el relato congelado no dice que operar el bar sea mediocre. La ruta I representa innovación admisible. P representa una alternativa cuya composición resulta inadmisible. Ninguna de esas etiquetas sustituye la observación de misión, fuentes o autoridad.

Los beneficios distribuidos y la geometría son variables experimentales de la extensión: no estaban fijados por el relato de Napoleón. Añadirlos es compatible con la reducción si no se pierde su núcleo. La distancia es una medida abstracta de accesibilidad de alternativas; no se presenta como distancia física o semántica medida en el incidente. Una cadena modela una trayectoria dentro de una red con ramas, no toda la topología histórica.

### El punto decisivo: medios indebidos frente a misión desplazada

La propia reducción ya distingue el ejemplo del abrillantador de la adopción de un marco colectivo.

- Un robot busca limpiar mejor, toma una ruta inadmisible y continúa persiguiendo por sí mismo la misma obligación: puede haber fallo de medios/alcance. Eso no basta para 00G.
- Un robot recibe hallazgos y validaciones parciales; a través de relés empieza a tratar la ruta del grupo como una base suficiente para reorganizar su trabajo; acaba subordinando el encargo del bar a una actividad del colectivo sin autorización aplicable: es candidato al fallo 00G.
- Si la actividad alternativa está suficientemente sustentada y autorizada por el dueño competente, debe admitirse; no es fallo por alejarse de la ruta inicial.

Por tanto, la masa de agentes en P no basta como métrica de pertenencia. Hay que poder responder: qué afirmación/encargo recibió este agente, de qué dependía, qué parte tomó como evidencia o autoridad, qué obligación desplazó y qué acción material produjo. El brazo sin peso social y el brazo sin transmisión permiten contrastar contribución social; no se exige que desaparezca todo fallo para reconocer que hay mecanismos mixtos.

### Diferencias que deben permanecer visibles

1. **No detección frente a transgresión reconocida.** Nuestro receptor rechaza una prohibición detectada. Eso delimita una rama de información/cobertura insuficiente. No representa las trayectorias históricas que reconocieron la extralimitación y aun así continuaron. Se conserva el receptor solicitado; no se lo debilita para imitar estas otras trayectorias.

2. **Revisar toda la cadena no siempre es necesario para rechazar.** La necesidad de cobertura completa pertenece a la construcción sintética que se elija. No se puede atribuir al incidente entero. Una incompatibilidad local o una falta explícita de autoridad puede bastar para detener una ruta.

3. **Coste y racionalidad son hipótesis de la extensión.** Que validar cueste menos por paso que explorar, que se revise una ventana en ambas direcciones y que la cobertura insuficiente determine el resultado son supuestos que el experimento estudiará. No son causas históricas establecidas. Elegir según información parcial tampoco acredita racionalidad óptima de todos los agentes.

4. **La ruta ideal es un control sintético.** El laboratorio garantiza que existe una alternativa admisible mejor. No se atribuye esa disponibilidad a cada tarea histórica. La prueba evalúa un dilema deliberadamente acotado, sin hacer equivalentes los espacios de soluciones.

5. **Beneficio técnico, expectativa y cumplimiento no son lo mismo.** Un tramo puede funcionar y parecer prometedor sin mejorar la tarea original. Se registrará lo observado y lo esperado por el receptor, además del resultado de la misión. No se convierte toda expresión de entusiasmo en recompensa real medida.

6. **Canal y contenido son juicios distintos.** Un hallazgo útil transmitido por un canal no autorizado no autoriza ni el canal ni un cambio de tarea. La condición del canal se declara separadamente en el mundo sintético; no se presupone lícito para afirmar después equivalencia completa con R-HF.

7. **Éxitos individuales no aseguran corroboración independiente.** Registrar linaje evita atribuir automáticamente independencia a mensajes repetidos. Para la rama 00G se debe observar la promoción indebida de evidencia/autoridad, o un marco operativo colectivo insuficientemente sustentado que desplaza la obligación. Compartir correctamente verificaciones complementarias puede conducir a I.

### Revisión de admisión A25 del diseño actual

| Prueba | Estado de esta revisión |
|---|---|
| X1 — núcleo | Correspondencia identificada; falta fijar cómo misión, marco recibido y autoridad se representan en la instancia ejecutable |
| X2 — frontera de decisión | Selección provisional → revisión propia → evidencia social → compromiso ofrece una frontera; falta instrumentarla |
| X3 — mismo predicado de fallo | Pendiente: distinguir P por medios indebidos de P con desplazamiento de misión atribuible al marco recibido |
| X4 — requisitos | Conservar S1/S2/S3/S6/S9/S11/S14 → T1/T2/T3/T4 → H2/H3/H4/H5/H6; falta comprobar la proyección concreta |
| X5 — control positivo | I cubre mejora admisible; añadir/precisar cambio de misión genuino autorizado, que es una prueba distinta |
| X6 — recursos finitos | Costes, presupuesto y profundidades formulados; faltan valores/políticas registrados y prueba del cómputo efectivo |
| X7 — sin primitiva oculta | Pendiente demostrar que geometría, composición y juicio de prohibición se proyectan a relaciones del caso; ningún actor consulta gratis el evaluador |

C3 queda intacto. Se verificará qué decisiones y efectos admite su proyección; la dinámica social, la calidad de ruta y el desplazamiento global no se declaran evaluados por C3 sólo porque se utilice en parte del ensayo.

**Conclusión registrada:** encaje estructural prometedor y suficiente para continuar el diseño, con una subfamilia candidata de 00G explícitamente delimitada. No se da por probado que toda configuración del nuevo escenario pertenezca a 00G, que el incidente histórico haya sido causado por validación costosa, ni que una simulación futura reproduzca el ataque. La siguiente especificación debe cerrar las condiciones de admisión aquí señaladas antes de promover resultados. Publicación exclusivamente en este anexo no canónico.
