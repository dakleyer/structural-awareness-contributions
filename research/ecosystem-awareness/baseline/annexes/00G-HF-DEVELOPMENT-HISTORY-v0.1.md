# Anexo — Desarrollo e historial de experimentos 00G-HF

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
