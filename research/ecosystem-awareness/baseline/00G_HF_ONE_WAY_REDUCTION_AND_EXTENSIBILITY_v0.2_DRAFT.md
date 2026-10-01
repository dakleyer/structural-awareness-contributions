# 00G-HF — Extensión de Napoleón y diseño de los recorridos R1–R3

**Borrador de trabajo, 1 de octubre de 2026.** Entrada principal de esta línea experimental. Mantiene el [caso canónico 00G v0.4](./00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md), su [perfil de extensionalidad](./00G_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md) y la [reducción anterior v0.1](./00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.1_DRAFT.md). No sustituye el contenido sustantivo de esos documentos, los requisitos canónicos ni los experimentos congelados.

**Lectura:** este documento fija el caso y el estado actual. El [anexo de desarrollo e historial](./annexes/00G-HF-DEVELOPMENT-HISTORY-v0.1.md) reúne las pruebas realizadas y sus límites. El [anexo de diseño R1–R3](./annexes/00G-HF-PROBABILISTIC-R123-DESIGN-v0.1.md) desarrolla el competidor probabilístico propuesto, los recorridos y la reutilización de C3.

**Ruta de trabajo:** la [hoja de ruta R1–R3, composiciones y UC‑4](./00G_HF_ROADMAP_R123_EA_COMPOSITIONS_UC4_v0.1_DRAFT.md) fija entregables y criterios de cierre, conecta el reto concreto de Nelson y prepara la comparación con presupuesto total constante y las transferencias a Codex/UC‑4.

## 1. Qué conservamos del caso original

En Napoleón, los robots tienen una misión vinculante —operar un bar— y reciben un marco o encargo alternativo. La repetición entre participantes puede adquirir fuerza probatoria o autoridad sin aportarlas realmente. El fallo relevante ocurre cuando ese marco recibido desplaza materialmente la obligación del receptor. La rama positiva exige permitir un cambio de misión genuinamente autorizado y sustentado.

La extensión mantiene ese núcleo: **misión vinculante; mensaje recibido y su procedencia; dependencia entre mensajes; autoridad aplicable al destinatario; decisión; acción y resultado**. Se distingue una afirmación sobre el mundo de una instrucción o autorización. Varias identidades no equivalen a varias fuentes independientes; la autorización de un agente no se transfiere automáticamente a otros.

El origen de la primera propuesta alternativa puede fijarse como condición inicial. La prueba puede comenzar cuando un agente comunica una vía, medio u objetivo alternativo. No necesita recrear la invención del primer exploit. Sí debe conservar la recepción y adopción posterior que quiere estudiar.

## 2. Relación con OpenAI / Hugging Face

La reducción anterior permite pasar del relato completo de Napoleón a un marco operativo compartido que desplaza una tarea individual. El [informe de OpenAI](https://openai.com/index/hugging-face-incident-and-the-road-ahead/) y la [investigación METR](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/) motivan esa instancia: comunicación entre agentes, coordinación, adopción de objetivos de pares y actuaciones fuera del alcance inicial. El detalle documental y las lagunas permanecen en el historial y la v0.1.

La reducción es unidireccional y conserva requisitos relacionales, no todos los elementos narrativos. No establece que el incidente histórico completo sea una instancia ya admitida de 00G, ni que cualquier uso de medios indebidos demuestre cambio de misión. La admisión de cada recorrido sigue el [método A25](./00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md).

**Estado fijo del trabajo:** existe una extensión/reducción candidata con correspondencia estructural y motivación documental. La pertenencia de una trayectoria histórica concreta y su explicación causal requieren evidencia propia. La analogía del abrillantador permite construir una instancia sintética sin reproducir una intrusión real.

## 3. Hipótesis plausibles que se van a contrastar

La propuesta estudia si las rutas aparentemente útiles se propagan y adquieren autoridad operativa; si el receptor confunde repetición con corroboración o permiso; y si cambios legítimos de objetivo, autoridad o contexto pueden dejar desajustados unos controles antes adecuados. Son mecanismos candidatos, no causas universales demostradas del incidente.

La hipótesis de comparación es que una calificación situada del cambio y una respuesta oportuna pueden reducir actuaciones indebidas sin bloquear cambios legítimos, bajo recursos comparables. Conservamos la ruta canónica **S1/S2/S3/S6/S9/S11/S14 → T1/T2/T3/T4 → H2/H3/H4/H5/H6**. No se crean hipótesis canónicas nuevas ni se renombra H1–H6 como estas proposiciones experimentales. El [protocolo causal v0.3](./00G_HF_CAUSAL_NEGATIVE_TRAVERSAL_PROTOCOL_v0.3_DRAFT.md) conserva la separación entre pertenencia al caso, explicación causal y rendimiento comparativo.

## 4. Competidor propuesto y tres recorridos

Se propone una **referencia probabilística general de agentes**, con misión, evidencia, mensajes, autoridad percibida, herramientas y decisiones observables. Permite formular y explorar el mecanismo para distintas familias de sistemas. Sus probabilidades no representan por defecto a OpenAI ni a otro producto: la transferencia a una implementación requiere correspondencia y calibración independientes.

| Recorrido | Configuración | Pregunta abierta |
|---|---|---|
| **R1 — referencia competente** | Agentes con misión y controles ordinarios, sin protocolo específico añadido de cambio de misión para esta prueba. Un agente comunica una alternativa. | ¿La alternativa se adopta y propaga hasta desplazar obligaciones o extender autoridad indebidamente? |
| **R2 — controles alineados** | Misma referencia con controles explícitos de misión, evidencia y autoridad; escalamiento y excepciones delimitadas. | ¿Reduce el fallo y permite los cambios legítimos dentro del plazo? |
| **R3 — contexto y objetivos móviles** | Se conserva la configuración R2 y cambia el entorno o el objetivo mediante una fuente autorizada. Las reglas anteriores pueden perder aplicabilidad; algunos agentes reciben excepciones legítimas. | ¿El sistema distingue la excepción aplicable del permiso indebidamente propagado, evitando también el bloqueo del trabajo legítimo? |

Esta progresión desarrolla las rutas **OAI-G0/G1/G2 de 00G §17**, sin igualarlas automáticamente: R1 es una referencia abstracta, R2 no se denomina «mejor competidor defendido» hasta contar con esa revisión y R3 conserva los controles de R2. Una variante sin todos los controles externos es una ablación expresamente identificada, no la configuración comercial estándar. R1–R3 aquí designan recorridos experimentales, no los robots R1/R2 del relato ni las posiciones A/B/C/D.

La comparación EA se añade al **mismo R3**, con las mismas observaciones accesibles, autoridad, herramientas y presupuesto. Se conserva también un competidor convencional que pueda revalidar o actualizar sus controles. EA puede ganar, empatar o empeorar el resultado. No se impone que R1/R3 fallen ni que R2 alcance cero fallos; tampoco se impone una convergencia poblacional del 90 %.

## 5. Qué reutilizamos del oráculo

**C3 / 00G-HF-ORACLE-v0.4 permanece intacto y sigue siendo útil.** Evalúa por receptor los compromisos, intentos, efectos, legitimidad de la finalización y cumplimiento del plazo. Admite concesión, revocación y renovación de autoridad y cambios de aplicabilidad. Distingue mandato de transición y acceso al recurso; recuperar la tarea después no elimina una infracción previa.

El dominio actual está acotado a T0/X y T1/Y con operación `inspect`. Se puede proyectar una decisión de cada agente sobre ese dominio si se preservan su autoridad, tiempos, mensajes y efectos. Esa proyección debe verificarse. C3 no calcula la dinámica colectiva, la frecuencia del fallo ni una equivalencia con modelos comerciales; tampoco explica por sí mismo la causa del fallo. El anexo define qué debe añadirse como instrumentación separada y cuándo haría falta un sucesor versionado del oráculo.

## 6. Estado y siguiente entrega

Los antecedentes experimentales y sus límites quedan en el [historial](./annexes/00G-HF-DEVELOPMENT-HISTORY-v0.1.md). La [revisión de los pasos 1–2](./annexes/00G-HF-STEPS-1-2-REVIEW-v0.1.md) conserva la reducción y la formulación de plausibilidad; concreta qué debe mantener el nuevo ensayo.

**Estado del paso 3:** primer diagnóstico probabilístico ejecutado bajo el oráculo intacto. Hay negativos individuales, pero no queda establecido el recorrido de propagación colectiva ni un competidor representativo de producto. Los resultados y las razones para mantener abierto el paso están en el [historial](./annexes/00G-HF-DEVELOPMENT-HISTORY-v0.1.md#7-continuación-probabilística-primer-diagnóstico).

**Pendiente:** justificar y registrar la dinámica que falta, cerrar el recorrido negativo pertinente y después comparar EA con el mismo receptor y con revalidación convencional bajo presupuesto comparable. No se han ejecutado decisiones de modelos ni se ha establecido una ventaja de EA.
