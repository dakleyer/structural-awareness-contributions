# Anexo — Desarrollo e historial de experimentos 00G-HF

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
5. El nuevo diseño R1–R3 aún no fue ejecutado. Ningún resultado anterior se renombra retrospectivamente como ejecución de esta propuesta.

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
