# Ecosystem Positioning — estrategia de desarrollo del corpus

**Propuesta de desarrollo para revisión de Iván · 6 de octubre de 2026.**  
[Volver a Ecosystem Positioning](./README.md)

La siguiente etapa consiste en convertir una arquitectura explicada y un conjunto de resultados acotados en una propuesta que pueda examinarse, implementarse y compararse con rigor. El avance debe permitir responder una pregunta práctica: **¿qué aporta conservar y revisar el contexto de una decisión, frente a una solución competente que ya dispone de controles, evidencia y supervisión?**

Este documento explica dónde concentrar el trabajo, por qué y qué conocimiento puede hacerlo avanzar. Es una estrategia adicional de desarrollo; el [plan de revisión del corpus](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md) organiza las auditorías y el [workplan técnico](../../research/ecosystem-awareness/WORKPLAN.md) mantiene las tareas operativas. Las tres piezas se complementan. Esta estrategia no sustituye las definiciones, requisitos, pruebas o versiones canónicas.

## Desde dónde partimos

El corpus ya ofrece una explicación del problema, requisitos comunes, mecanismos de arquitectura, escenarios, diseños de comparación y ejecuciones simbólicas registradas. Esto permite discutir cuestiones concretas y conservar también los contraejemplos que han limitado afirmaciones anteriores.

Todavía hay una distancia entre esas piezas y una demostración de funcionamiento del conjunto. La revisión de suficiencia sigue siendo parcial; las notas de plausibilidad no acreditan ingeniería viable; algunos perfiles de interfaz necesitan conciliación; y la comparación independiente del conjunto permanece abierta. La estrategia parte de esa distancia y propone reducirla mediante entregas examinables, sin convertir la publicación de un texto en una prueba de éxito.

## Qué debe avanzar primero

### 1. Asegurar que las afirmaciones conservan su sentido y su evidencia

La prioridad inmediata es terminar el contraste entre las definiciones actuales, las fuentes científicas, los requisitos y las pruebas que las utilizan. Una palabra que cambia de significado puede dejar una demostración bien ejecutada referida a una premisa distinta. También puede perderse una limitación al pasar de una nota técnica a un README o una presentación.

El trabajo concreto empieza por las referencias de [la nota sobre plausibilidad funcional](../../research/ecosystem-awareness/baseline/00N_VNext.md), la relación con [la nota matemática](../../research/ecosystem-awareness/baseline/00M_VNext.md) y la [revisión de suficiencia de los principios](../../research/ecosystem-awareness/baseline/00K_A23_CANONICAL_REQUIREMENT_CONFORMANCE_SUFFICIENCY_P1_P6_v0.1.md). No se necesita ampliar la teoría para resolver primero qué sostiene cada argumento existente.

**Entrega esperada:** un relato claro de lo respaldado, lo condicionado y lo pendiente, con las relaciones intelectuales reconstruibles. Terminar esta entrega significa revisar esas relaciones; no significa demostrar que todo el sistema cumple los requisitos.

### 2. Describir un perfil pequeño de principio a fin

Después, o en paralelo cuando no dependa de una cuestión abierta, conviene desarrollar un perfil que una persona pueda recorrer completo: qué pregunta recibe, qué resultado y condiciones aporta cada participante, cómo se revisan, quién decide y qué efecto se observa.

Un buen punto de partida es una situación pequeña de cambio de base: dos resultados locales siguen siendo válidos, pero una versión, una dependencia o una condición de autoridad cambia antes de utilizarlos juntos. El perfil debe incluir también continuidad válida, información ausente y una respuesta legítima. Así se evita una solución que parezca segura solo porque bloquea todo.

La [revisión de interfaces](../../research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) mantiene abierta una pregunta material: cuándo basta una referencia al resultado de una fuente y cuándo el receptor necesita su valor. Esa cuestión debe quedar resuelta para el perfil elegido, conservando el significado del productor y las condiciones de uso.

**Entrega esperada:** un ejemplo completo, con límites y resultados esperados, que pueda convertirse en una prueba después de su revisión y admisión. No se trata de declarar implementada toda la arquitectura a partir de una tabla de componentes.

### 3. Fijar cómo se decidirá si aporta una mejora

La comparación debe poder dar una respuesta negativa. Antes de optimizar la configuración propuesta, hay que definir qué cuenta como resultado correcto, qué costos importan, cuánto retraso es admisible y qué equivalencia permitiría afirmar que dos soluciones hacen lo mismo.

El [benchmark de desarrollo](../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md) plantea comparadores fuertes, aportación de módulos y costo de reconstruir una decisión. Su valor estratégico está en permitir que una solución convencional gane, y en distinguir qué parte del conjunto aporta algo bajo condiciones determinadas.

**Entrega esperada:** un protocolo de comparación y admisión previo a los resultados, con controles positivos, límites de recursos y reglas para conservar fallos. Tener más componentes, más contexto o más etiquetas no cuenta por sí solo como avance.

### 4. Buscar revisión independiente y ampliar solo lo que pueda transferirse

Cuando exista un perfil suficientemente preciso, el siguiente paso es contrastarlo con personas que conozcan las fuentes, los controles y el dominio de aplicación. La revisión independiente debe poder cuestionar las premisas y fortalecer al comparador, no limitarse a confirmar una lectura interna.

La ampliación a otros casos se justifica si se conserva la relación estructural relevante: pregunta, alcance, evidencia, autoridad, tiempo y condiciones de respuesta. Cambiar el sector o la tecnología no demuestra por sí solo que se haya transferido la solución.

La discusión pública ofrece vías de trabajo acotadas. Por ejemplo, el [comentario de Theme #16 del 24 de septiembre](https://github.com/FG-TIDA/themes/issues/16#issuecomment-5809248877) apoya una secuencia con el caso de origen como referencia y revisión antes de congelar el mapping. Ese acuerdo de proceso no equivale a adopción de Ecosystem Positioning, validación de un contrato o ejecución ya terminada. El [filtro de estado público](../../research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) conserva esas diferencias.

**Entrega esperada:** objeciones y revisiones atribuibles, configuraciones defendidas y, cuando exista autorización y admisión, evidencia independiente del alcance realmente probado. Esta estrategia no activa contactos, experimentos ni compromisos por el hecho de nombrarlos.

## Dónde puede aportar conocimiento una persona

| Área de aportación | Pregunta que puede ayudar a resolver | Prioridad |
|---|---|---|
| Semántica, lógica y métodos formales | ¿La transformación conserva la afirmación que se necesita, y cuáles son sus premisas? | Inmediata: fundamentos y fidelidad de pruebas. |
| Ingeniería de interfaces y sistemas distribuidos | ¿Qué debe cruzar una frontera y qué ocurre si llega tarde, falta o cambia su significado? | Alta: perfil completo y manejo de límites. |
| Diseño experimental y evaluación | ¿El resultado distingue la contribución propuesta de controles ya disponibles? | Alta: comparación antes de ejecución. |
| Conocimiento de un dominio operativo | ¿Qué condición es material, quién tiene autoridad y hasta cuándo sirve una respuesta? | Ligada al perfil elegido. |
| Comunicación técnica y edición | ¿Una persona nueva puede comprender la idea, sus evidencias y lo pendiente? | Continua: todas las entregas y especialmente los README. |

Estas áreas describen aportaciones posibles, no un equipo ya constituido ni acuerdos externos. Una misma persona puede contribuir a varias; la independencia de una revisión se registra según lo que realmente ocurrió.

## Referencias externas que orientan estas prioridades

Las fuentes siguientes apoyan preguntas y herramientas del desarrollo. Ninguna constituye una validación de Ecosystem Positioning ni un respaldo institucional al proyecto.

- **Información que importa a una pregunta.** [Tishby, Pereira y Bialek — Information Bottleneck](https://arxiv.org/abs/physics/0004057) estudian representaciones compactas que conservan información sobre un objetivo definido. Esto ayuda a preguntar qué puede perder un handoff; no prueba que cualquier resumen utilizado por EA sea suficiente.
- **Composición distribuida con supuestos declarados.** [Estella Aguerri y Zaidi — Distributed Information Bottleneck](https://arxiv.org/abs/1709.09082) estudian compresión por varios encoders en modelos específicos. Es un precedente para explorar utilidad conjunta; sus modelos no se trasladan automáticamente a agentes con fuentes compartidas, retroalimentación o comportamiento adversario.
- **Abstracciones y límites.** [Cousot y Cousot — Abstract Interpretation](https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml) proporcionan una base para razonar sobre propiedades de un estado mediante una representación abstracta. Construir una abstracción correcta y útil para el perfil de EA sigue siendo trabajo del proyecto.
- **Convergencia de datos.** [Shapiro y colaboradores — CRDTs](https://www.lip6.fr/Marc.Shapiro/papers/2011/CRDTs_SSS-2011.pdf) muestran condiciones de convergencia en un modelo definido. Converger al mismo estado no establece verdad, independencia de fuentes ni resiliencia frente a participantes bizantinos; esas cuestiones deben examinarse aparte.
- **Vigencia de los supuestos.** [Sokolsky y colaboradores — Monitoring Assumptions in Assume-Guarantee Contracts](https://arxiv.org/abs/1606.00505) estudian monitoreo de condiciones del entorno que una verificación previa no descarga por sí sola. Es una referencia cercana para revisar la base de una decisión en ejecución, con límites de observación y de transformación de interfaces.
- **Evidencia y decisión conservan propietarios distintos.** [RFC 9334 — RATS Architecture](https://www.rfc-editor.org/rfc/rfc9334.html#section-3) diferencia la evaluación de evidencia de la decisión específica de quien confía en el resultado. Orienta la integración con mecanismos existentes; no concede autoridad a EA ni demuestra la suficiencia del conjunto.

Estas referencias fijan un punto de apoyo y un límite. La selección es deliberadamente breve; el contraste detallado de los papers se conserva en las VNext de sus documentos, evitando transformar la estrategia en una segunda bibliografía masiva.

## Qué viene a continuación y cómo reconocer un avance

La secuencia propuesta es: **aclarar una afirmación → describir un perfil completo → fijar la comparación → obtener revisión y evidencia → transferir con límites explícitos**. No es una cascada rígida: edición y lectura humana continúan durante todo el recorrido, y un hallazgo puede exigir volver a una premisa.

El próximo avance reconocible es terminar el examen de las fuentes de 00N y su conexión con la teoría actual, y escoger qué perfil puede desarrollarse sin depender de una afirmación abierta. Después deberán quedar claras las condiciones de interfaz y el protocolo de medición antes de producir nuevos resultados. Ampliar el corpus solo tiene sentido cuando hace más precisa una pregunta o mejor sustentada una respuesta.

La estrategia podrá crecer con nuevas aportaciones, razones para cambiar prioridades y evidencia que las justifique. Hasta la revisión de Iván, este documento y el README de Ecosystem Positioning conservan su contenido existente: las actualizaciones se añaden, sin quitar, sustituir o reorganizar lo anterior. Las correcciones técnicas continúan como propuestas revisables.
