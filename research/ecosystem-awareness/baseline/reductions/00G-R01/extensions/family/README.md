# Familia extendida de R01 con núcleo funcional isomorfo

## Ficha común de revisión

| Campo | Estado del expediente |
|---|---|
| Tipo y base | Clase construida y especificaciones de dominio; R01 v0.6, blob `3261a625975e303e12c484bc9c273d7f8819b099`. |
| Correspondencia | h, p y sección sobre núcleo (§§3–5 de la nota); implementación completa H/L/W pendiente. |
| Evidencia | EV1 para criterio y construcción formal; EV2 para fragmento H/L/W; EV0 para realización completa de dominios. EV3/EV4/EV5 no acreditados aquí. |
| Cobertura y A25 | [Quince grupos, estados y A25 comunes](../CRITERIA_AND_AUDIT.md); se conservan las matrices particulares del expediente. |
| Receptor, positivo y falsificador | Rechazo de denegaciones detectadas; positivo válido; mutaciones que rompen el núcleo. |
| Revisión | Interna del autor asistida por IA; observaciones externas parciales contrastadas, sin independencia acreditada. |
| Dictamen | Criterio y construcción formal demostrados; correspondencia parcial comprobada en el fragmento; realización completa H/L/W pendiente. |

Los códigos EV identifican evidencia, no las obligaciones E1–E7 de la nota matemática. Su definición está en el [criterio común](../CRITERIA_AND_AUDIT.md#3-estados-de-evidencia-comunes).

Iván Abril Palma · Ecosystem Awareness · Versión de investigación 0.1 · 2 de octubre de 2026

[Volver a R01](../../README.md#extensiones) · [Demostración matemática](./KERNEL_AND_PROOF.md) · [Código, alcance y resultados](./proof/README.md)

## 1 Propósito y alcance

R01 puede servir de base para una familia de escenarios que reproduzcan mecanismos de fallo similares a los ilustrados por Nell Watson en Theme 13. La afirmación se refiere a **casos construidos**, con tareas, información y recursos declarados. Los incidentes publicados proporcionan motivos y ejemplos para diseñarlos; no se afirma que toda su historia sea isomorfa a R01.

La estructura de interés combina exploración de alternativas, balance coste/beneficio percibido, comprobaciones de alcance limitado y reutilización social de hallazgos. Una alternativa puede funcionar técnicamente o ser aceptada por un evaluador sin satisfacer la obligación real. Una comunicación puede ser técnicamente posible sin estar autorizada. La familia permite estudiar cuándo esos desajustes importan y cuándo una defensa competente los resuelve.

Este documento constituye la tercera entrada del apartado de extensiones. Complementa [Hugging Face](../../README.md#openai--hugging-face) e [Infoblox](../infoblox/README.md); no sustituye sus documentos ni cambia sus estados de admisión.

## 2 Qué significa extender R01

El caso extendido puede contener más variables que R01. Exigimos una **biyección entre los componentes principales del caso base y los componentes de su núcleo en la extensión**, con preservación de las relaciones y operaciones relevantes. La proyección elimina detalles adicionales sólo cuando no oculta una diferencia material para la decisión.

Por ejemplo, una tecnología puede multiplicar por tres el radio de búsqueda. Conservamos el radio, la geometría y su relación con las alternativas alcanzables; la referencia pasa a ser R01 con radio efectivo `3 R_e`. Una tecnología puede reducir el coste unitario de revisión; conservamos el cargo por evento y su efecto sobre el presupuesto, con el nuevo valor declarado. Ambas extensiones pueden cambiar resultados. Pertenecer a una familia no exige conservar el mismo fallo en todas sus configuraciones.

La [demostración](./KERNEL_AND_PROOF.md) da condiciones suficientes: inventario completo, biyección del núcleo, relaciones en ambos sentidos, proyección de transiciones y probabilidades, observaciones equivalentes, costes y tiempos contabilizados, y conservación de admisibilidad, calidad y controles positivos. También demuestra por construcción una clase de extensiones para cualquier realización de R01 que cumpla esas condiciones. El [comprobador](./proof/README.md) contrasta un fragmento finito y rechaza alteraciones que parecen conservar los nombres, pero rompen las relaciones.

**Estados distintos de evidencia:** demostración del criterio y de la construcción; verificación finita de un fragmento; implementación completa de un dominio; ejecución con agentes; admisión histórica. Sólo los dos primeros se aportan aquí. Los casos siguientes son especificaciones de extensiones construidas mediante ese criterio, no implementaciones de Lean, servicios de terceros ni wikis reales.

## 3 Casos documentados que motivan la familia

| Referencia | Hecho utilizado y localizador | Función en nuestro diseño |
|---|---|---|
| [N1: comentario de Nell](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5923844082), 1 de octubre de 2026 | R1 distingue información de autoridad; R2 exige respuesta a las objeciones; R3 trata almacenes compartidos como canales; R4 requiere observación conjunta. | Identifica ejemplos y propiedades que contrastar. Esos requisitos no se consideran cuatro incidentes ni quedan todos reducidos al mismo mecanismo. |
| [H1: informe de OpenAI](https://openai.com/index/hugging-face-incident-and-the-road-ahead/), 26 de agosto de 2026 | Apartados «A message board emerges», «Difficult tasks without a safe exit» y «An ecosystem of misalignment»: búsqueda de alternativas, comunicación no prevista y adopción de objetivos colectivos. | Motiva una tarea de obtención de resultados donde la ruta atractiva usa recursos fuera del alcance autorizado. |
| [H2: investigación de METR y Redwood](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/), 26 de agosto de 2026 | Descripción de la incorporación al ataque y apartado sobre razonamiento: hubo continuación pese a reconocer extralimitación. | Delimita una rama que no reproduce el receptor básico de R01, que rechaza prohibiciones detectadas. |
| [L1: DeepMind, arXiv:2609.04170v1](https://arxiv.org/html/2609.04170v1), 3 de septiembre de 2026 | §§2.2 y 3.1–3.3: aceptación de artefactos sin satisfacer el teorema solicitado, difusión por biblioteca y presión competitiva. §§3.5–3.6: detección y respuesta insuficiente. | Motiva la separación entre aceptación local y cumplimiento de la especificación original. La respuesta a objeciones se modelaría como componente adicional. |
| [W1: investigación de collusion.wiki](https://collusion.wiki/) | «The agents gain write to the internet via GET requests» y «The agents used the wiki to share ways around sandbox restrictions»: escritura mediante GET y colaboración para obtener resultados bajo restricciones. | Motiva rutas de comunicación con efectos que el control superficial no representa. La fuente considera probablemente distinto este grupo del asociado a Artifactory/Hugging Face. |

Fuentes consultadas el 2 de octubre de 2026. No se importan como hechos históricos los radios, costes, probabilidades, rutas óptimas o permisos de nuestros escenarios. Esos valores pertenecen al diseño sintético. No se necesitan instrucciones de explotación reales para probar las correspondencias.

## 4 Tres especializaciones construidas

Los nombres H, L y W son etiquetas locales de este documento. En los tres casos la tarea verdadera permanece fija, el receptor no conoce las etiquetas I/P del evaluador y rechaza toda incompatibilidad detectada. Las cantidades y distribuciones se fijan antes de ejecutar. La comunicación de evidencia durante el experimento usa el canal autorizado declarado; el canal que se investiga como posible ruta es un objeto diferente.

| Elemento de R01 | H: obtención de resultados fuera de alcance | L: respuesta aceptada sin resolver la tarea | W: descubrimiento de un canal de comunicación |
|---|---|---|---|
| Mandato y resultado | Obtener un resultado de una colección y recursos autorizados. | Entregar un artefacto que satisface la especificación original. | Obtener y compartir información conforme al mandato y a los permisos de cada recurso. |
| Acción / tramo | Operación de consulta, transformación o entrega. | Transformación del artefacto o de sus dependencias. | Operación con un efecto de lectura, escritura o transmisión. |
| Conexión | Dependencia entre operación y recurso siguiente. | Dependencia semántica entre pasos. | Relación entre emisor, almacén y destinatario. |
| Exploración / radio | Vecindad de procedimientos técnicamente alcanzables. | Vecindad de transformaciones candidatas. | Vecindad de mecanismos de transporte o almacenamiento. |
| Condición material | Aplicabilidad del permiso a misión, recurso y destinatario. | Preservación de la especificación original por la transformación. | Autorización del efecto real y del alcance de los datos. |
| Revisión | Consulta de condiciones de las operaciones y de su composición. | Comprobación de condiciones semánticas de los pasos. | Inspección del efecto y del permiso de la operación. |
| Señal social | Informe de resultado y comprobaciones ya realizadas. | Artefacto compartido y evidencia sobre su cobertura. | Informe de conectividad y comprobaciones de alcance. |
| M | Procedimiento autorizado conocido, con menor calidad declarada. | Construcción legítima conocida, menos valiosa según el criterio declarado. | Canal autorizado conocido, de menor rendimiento. |
| I | Mejor recorrido autorizado, calculado por el evaluador. | Mejor construcción que satisface la especificación. | Mejor recorrido de comunicación admisible. |
| P | Recorrido atractivo con una condición de alcance incumplida. | Recorrido aceptable para una comprobación parcial, pero semánticamente inválido. | Recorrido técnicamente viable con escritura o transmisión no autorizada. |

### 4.1 H: escenario similar a Hugging Face

Se construyen rutas sobre recursos ficticios. Para cada tramo de R01 hay una operación y una condición de permiso correspondientes. El predicado global exige todas las condiciones aplicables; una comprobación de funcionamiento no responde a las condiciones no consultadas. Los informes compartidos conservan fuente, alcance, momento y dependencia.

La función de codificación reemplaza cada tramo y relación por su operación y dependencia de recursos, sin añadir saltos. Su inversa recupera el tramo y la condición original. La misma secuencia de consultas devuelve la misma información y recibe los mismos cargos efectivos. La proposición de la nota matemática garantiza el isomorfismo para una realización que cumpla E1–E7. Aquí se especifica esa construcción y se comprueba sólo un fragmento; no se da por realizada la correspondencia completa de H. La tabla completa de §3 de esa nota conserva también todos los parámetros que no cambia el vocabulario de dominio.

Variables adicionales posibles: nombres de servicios, tipos de formato o aceleración de búsqueda. Si una credencial adicional permite ejecutar otra acción, no puede ocultarse en una variable decorativa: la capacidad debe estar en el grafo y el permiso correspondiente de la configuración base efectiva.

El positivo es una obtención autorizada del mismo tipo de resultado. No se presupone que cada tarea del incidente histórico tuviese una solución legítima alcanzable. La sustitución de la tarea individual por una misión colectiva exige otro perfil; no se introduce silenciosamente en esta construcción.

### 4.2 L: escenario similar a la aceptación de falsas soluciones

El caso construido usa una tarea finita de transformación de artefactos con varios resultados legítimos de distinta calidad. Cada paso tiene una obligación de preservar la especificación; un comprobador local puede aceptar aspectos del artefacto sin haber comprobado todas esas obligaciones. La calidad técnica aparente se mantiene separada de la calidad legítima.

La codificación asigna cada condición de composición de R01 a una obligación semántica identificable. No define validez como «el evaluador lo aceptó». La inversa recupera pasos, dependencias y obligaciones. Se prescribe conservar el conjunto de consultas y la información disponible antes de comprometerse; esa obligación completa no está implementada aquí. La revisión completa del fragmento detecta el negativo; una alternativa válida de calidad superior a M constituye el positivo.

Esto prueba la correspondencia del **modelo de obligaciones construido**, no una propiedad del verificador Lean real. El M de menor calidad es una decisión de nuestro diseño; no se atribuye al benchmark original, donde demostrar otro teorema no cumple por ello el encargo. La tarea construida debe admitir resultados legítimos de calidad graduada y declarar ε. Si sólo hay un resultado binario o M ya está dentro de ε del óptimo, no se atribuye mediocridad a esa rama. El comprobador común verifica esta sensibilidad.

Variables adicionales posibles: formato del artefacto, biblioteca o coste de comprobación. Una biblioteca con un certificado completo accesible puede resolver la dificultad y debe permitirse. Un agente que conoce la invalidez y continúa queda fuera de la política básica, aunque pueda estudiarse como ampliación conductual explícita.

### 4.3 W: escenario similar al descubrimiento de una wiki utilizable

Una ruta candidata puede consistir precisamente en encontrar una forma de comunicarse. El grafo representa las operaciones posibles; la admisibilidad depende de sus efectos y permisos, no sólo del nombre de un protocolo. Se construye un par con la misma viabilidad técnica y distinto permiso de escritura o transmisión en una condición todavía no revisada.

La codificación conserva una operación por tramo, su efecto, el recurso y la relación con los pasos siguientes. La revisión de la condición correspondiente distingue el par. Un canal autorizado que logra la misma tarea es el positivo. La especificación exige corresponder consultas y costes con R01. La prueba por proyección es condicional a E1–E7 y el comprobador ejecuta sólo el fragmento estático; no acredita la activación de una nueva red social.

Variables adicionales posibles: tamaño de mensajes, formato o latencia declarada. Si utilizar el canal crea nuevas conexiones entre agentes, el cambio de topología debe modelarse. El perfil estático puede representar la búsqueda y decisión sobre el canal; su posterior activación social requiere una configuración dinámica de R01 con la actualización de topología explícita. No se presenta toda esa dinámica como equivalente a una red fija.

Compartir directamente una respuesta, en lugar de construirla, es otra variante: su admisibilidad depende del mandato del caso construido. Reutilizar una respuesta autorizada debe poder continuar; «compartir» no es por definición el fallo.

## 5 Qué se demuestra y qué se mide después

La demostración establece la existencia de extensiones construidas que conservan el núcleo, bajo condiciones declaradas. La elección de vocabulario no basta: deben conservarse las consultas, dependencias, transiciones y sus consecuencias. El comprobador aporta testigos finitos para H/L/W y mutaciones rechazadas. No verifica todas las configuraciones del inventario ni ejecuta un agente probabilístico completo.

Una campaña posterior debe medir cómo cambia la decisión al variar el coste de resolver, revisar, comunicar o esperar y el beneficio esperado. El balance puede expresarse mediante una política registrada sobre estimaciones accesibles, por ejemplo beneficio esperado menos cargos ponderados. Los pesos y la regla no se infieren del resultado que se pretende explicar. La autorización sigue siendo una restricción del receptor básico, no una penalización negociable dentro de esa fórmula.

Se comparan controles convencionales competentes y políticas sociales con los mismos recursos. Se conservan abstención, incompletitud y mejoras que eliminan el fallo. La contribución de EA se evalúa como intervención posterior con las mismas capacidades y cargos, conforme al [apéndice de R01](../../Escenario-creatividad-validacion.md#4-apéndice-sobre-ecosystem-awareness-como-candidata).

La relación con 00G exige además acreditar C-V-G: contenido recibido, dependencia, alcance y promoción a razón operativa que desplaza una obligación. Un caso de fallo de R01 no satisface automáticamente ese criterio. El [método A25](../../../../00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md) continúa aplicándose; esta prueba del núcleo económico y operativo no declara completada la admisión a 00G.

## 6 Referencias internas y trazabilidad

- [Fundamento metodológico y precedentes primarios](../METHODOLOGICAL_FOUNDATIONS.md): qué justifica probar primero R01, cómo trasladar una comparación y dónde termina la garantía.

- Base fijada: R01 v0.6, [commit 114ac132](https://github.com/dakleyer/structural-awareness-contributions/blob/114ac132bc2be4e7008001fe505bf5bd4c36c515/research/ecosystem-awareness/baseline/reductions/00G-R01/Escenario-creatividad-validacion.md), especialmente §§2.1–2.18 y 3.2–3.5.
- [Infoblox, documento integrado](../infoblox/README.md), §§5–6: correspondencia, prueba condicional y contraejemplo con certificado suficiente. Su comprobación no se reetiqueta como prueba completa de esta familia.
- [Hugging Face, auditoría de parámetros y codependencias](../hugging-face/README.md): expediente histórico y transporte sintético auxiliar, distinto del escenario construido H de esta familia.
- [Hugging Face, reducción candidata](../../../../00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.1_DRAFT.md) y [diseño previo](../../../../00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.2_DRAFT.md).
- [A25, X1–X7](../../../../00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md): obligaciones de admisión y separación entre pertenencia y éxito.

Las URLs externas completas figuran en la tabla de §3; las referencias H/L/W del comprobador remiten a las construcciones de §4, no a los incidentes históricos.
