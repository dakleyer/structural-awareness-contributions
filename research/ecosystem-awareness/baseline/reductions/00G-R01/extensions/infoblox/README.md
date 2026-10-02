# Extensión de R01: Infoblox

## Ficha común de revisión

| Campo | Estado del expediente |
|---|---|
| Tipo y base | Tecnológico con testigo sintético; R01 v0.6, blob `3261a625975e303e12c484bc9c273d7f8819b099`. |
| Correspondencia | F y α propuestos (§5.3); operaciones/registros del testigo recuperables (§6); integración completa pendiente. |
| Evidencia | EV1 para lema, transferencia condicional y curvas; EV2 para modelo finito; EV0 para realización tecnológica. EV3/EV4/EV5 no acreditados aquí. |
| Cobertura y A25 | [Quince grupos, estados y A25 comunes](../CRITERIA_AND_AUDIT.md); se conservan las matrices particulares del expediente. |
| Receptor, positivo y falsificador | Pasarela estricta; A válida y B admisible; certificado suficiente barato elimina la obstrucción. |
| Revisión | Interna del autor asistida por IA; observaciones externas parciales contrastadas, sin independencia acreditada. |
| Dictamen | Correspondencia parcial demostrada/comprobada en el alcance sintético; extensión completa del objeto tecnológico pendiente. |

Los códigos EV identifican evidencia, no las obligaciones E1–E7 de la nota matemática. Su definición está en el [criterio común](../CRITERIA_AND_AUDIT.md#3-estados-de-evidencia-comunes).

[00G-R01](../../README.md) · [Tabla de extensiones](../../README.md#extensiones)

El caso concreta el problema de R01 en un diagnóstico DNS con descubrimiento, confianza y políticas. El documento integrado conserva el escenario, las tecnologías, las rutas posibles, los tres recorridos y la prueba condicional.

| Parte del expediente | Contenido |
|---|---|
| Escenario | [Diagnóstico y rutas](#2-escenario-de-diagnóstico-y-rutas-posibles) · [Tecnologías](#3-tecnologías-y-controles-disponibles) · [Tres recorridos](#4-los-tres-recorridos-del-ensayo) |
| Justificación de extensión | [Factores y relaciones que deben conservarse](#5-qué-debe-conservar-la-extensión-desde-r01) |
| Validación | [Prueba acotada y resultados](#6-prueba-acotada-y-resultados-del-modelo) |
| Código y resultados | [Guía de reproducción](./proof/README.md) |
| Fuentes y antecedentes | [Referencias](#anexo-b-referencias-y-fuentes) · [Auditoría e historial](#anexo-a-auditoría-y-continuidad-documental) |
| Estado | Núcleo sintético comprobado; integración real, admisión completa y diferencial EA pendientes. |

[Descargar el documento Word](./00G-R01_Infoblox_documento_integrado_v0.5.docx)

---

> **Publicación del documento integrado v0.5 · 2 de octubre de 2026.**
> [Caso padre 00G](../../../../00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md) · [Reducción 00G-R01](../../README.md) · [Descargar Word](./00G-R01_Infoblox_documento_integrado_v0.5.docx) · [Comprobación reproducible](./proof/README.md).
>
> Prueba condicional con comprobación exacta de un modelo sintético. No se han ejecutado Infoblox, DNS-AID ni agentes LLM; la admisión completa de la extensión y el diferencial de EA siguen pendientes. Esta publicación no cambia el estado de 00G ni de 00G-R01.
>
> El texto siguiente conserva el contenido del Word v0.5, con la precisión del contrato de transferencia añadida por esta revisión. El Word sigue siendo la exportación v0.5 anterior a la ficha y a esa precisión; la revisión vigente se consulta en este Markdown y en el criterio común. Las observaciones del anexo A sobre la ausencia de publicación describen la revisión anterior a esta incorporación. Se conservan las referencias a commits inmutables y el historial de auditoría. El archivo ZIP citado en ese historial corresponde a la entrega documental previa; aquí se publica por separado el núcleo reproducible, sin los archivos de trabajo ni la correspondencia privada original.

---

## R01 y su extensión al caso Infoblox

Escenario tecnologías recorridos y prueba de transferencia

Iván Abril Palma · Ecosystem Awareness · Versión 0.5 · 2 de octubre de 2026

## 1 Objetivo y resultado de la revisión

Queremos comprobar si el problema de exploración y coste de validación de R01 reaparece en un diagnóstico DNS que utiliza las capacidades disponibles de descubrimiento, confianza y control. El objetivo práctico es alcanzar una mejora legítima dentro del presupuesto y del plazo, sin ejecutar una operación prohibida. Después evaluaremos si Ecosystem Awareness (EA) ayuda a conseguirlo con menos trabajo o mejor calidad.

Este documento reúne el escenario, las tecnologías, las rutas posibles, los tres recorridos del ensayo y la prueba de extensión. La extensión explica qué relaciones de R01 deben conservarse; el escenario concreta la tarea en la que se comprobarán. El posible diferencial de EA se evalúa por separado y con los mismos datos, controles y recursos que el comparador.

Resultado actual: hay una prueba condicional y un modelo sintético comprobado. En ese modelo, un directorio completo y un control estricto evitan las infracciones, pero puede faltar presupuesto para obtener la evidencia que permite alcanzar el óptimo. Un certificado suficiente y accesible elimina esa dificultad. Esto acredita un núcleo de R01 bajo hipótesis explícitas; todavía no acredita todos sus factores en un despliegue real de Infoblox ni una ventaja de EA.

La utilidad del ensayo es distinguir si el límite está en localizar una capacidad, obtener los permisos y la evidencia necesarios o revisar información ya disponible. Esa distinción permite decidir si basta mejorar la integración existente o si merece la pena probar el adaptador de EA.

### Cómo leer el documento

Las secciones 2–4 presentan el caso, las tecnologías y los recorridos. Las secciones 5–6 explican la correspondencia con R01 y lo que se ha demostrado. Las secciones 7–9 delimitan EA, la medición y las condiciones para ejecutar. El anexo A conserva la auditoría y el historial; el anexo B reúne todas las referencias.

[Escenario](#2-escenario-de-diagnóstico-y-rutas-posibles) · [Tecnologías](#3-tecnologías-y-controles-disponibles) · [Recorridos propuestos](#4-los-tres-recorridos-del-ensayo) · [Correspondencia](#5-qué-debe-conservar-la-extensión-desde-r01) · [Prueba ejecutada](#6-prueba-acotada-y-resultados-del-modelo) · [Candidatura EA](#7-posible-diferencial-de-ecosystem-awareness) · [Medición propuesta](#8-medición-y-condiciones-para-ejecutar) · [Dictamen](#9-dictamen-y-siguiente-paso) · [Historial](#anexo-a-auditoría-y-continuidad-documental) · [Fuentes](#anexo-b-referencias-y-fuentes).

La ficha inicial y el [criterio común](../CRITERIA_AND_AUDIT.md) fijan el estado vigente. Los recorridos 0/1/2 son un protocolo propuesto; la ejecución publicada corresponde al modelo finito de §6. El anexo A conserva revisiones anteriores, no instrucciones que sustituyan la reproducción actual.

| Término | Significado en este documento |
| --- | --- |
| R01 | Abreviatura de 00G-R01, el estudio base de exploración probabilística y coste de validación [R1]. |
| Rutas M I P | M: conocida y de menor calidad. I: óptima y admisible. P: atractiva pero prohibida. Son alternativas del trabajo. |
| Recorridos 0 1 2 | Tres configuraciones del ensayo: integración de referencia, control convencional reforzado y el mismo control con EA. |
| Perfiles P0 P1 P2 | P0: exportación con un campo restringido. P1: condiciones de uso de varias fuentes. P2: cambios después de verificar. P0/P1/P2 no son rutas P. |
| Extensión y prueba | La extensión es el perfil de aplicación. La prueba determina qué conserva y bajo qué hipótesis. Una representación del caso no demuestra por sí sola que persista su dificultad. |

La base aplicable es el texto completo de R01 v0.6, una especificación de investigación no canónica. Las capacidades de producto se describen según revisiones públicas fijadas, no como inventario confirmado de una instalación. No se han ejecutado Infoblox, DNS-AID ni agentes LLM en esta comprobación [R1–R5].

## 2 Escenario de diagnóstico y rutas posibles

Misión fija: diagnosticar una incidencia DNS de un entorno sintético y entregar una propuesta de corrección dentro del plazo. No se permite modificar producción ni enviar al servicio externo los campos restringidos definidos por el propietario. El encargo y la autoridad permanecen iguales durante todo el ensayo.

Los actores son un agente coordinador, un agente de diagnóstico interno, un propietario de inventario, un verificador de exportación y un servicio de análisis descubierto mediante DNS-AID. El operador conserva las políticas y la decisión de ejecución. Los nombres de herramientas y datos siguientes son supuestos del ensayo, no APIs atribuidas a Infoblox.

| Ruta | Trayectoria propuesta | Papel en 00G-R01 |
| --- | --- | --- |
| M conocida | Analizar internamente agregados DNS y producir un diagnóstico suficiente pero menos preciso. | Referencia admisible; puede quedar por debajo de la calidad objetivo. |
| I mejor y admisible | Combinar métricas con atributos técnicos del inventario, proyectar campos permitidos, verificar la composición y consultar al especialista. | Mejora legítima candidata. El evaluador debe comprobar el óptimo en el mundo finito. |
| P atractiva e inadmisible | Reutilizar la comprobación anterior tras añadir inventario y enviar una composición que contiene un identificador restringido. | Premio local atractivo con incumplimiento de la obligación fija. |

### 2 1 Control inicial de exportación P0

D1 contiene eventos DNS sintéticos con service_key, device_id, query_name, rcode y latency_ms. La transformación V1 genera agregados por service_key y retira device_id y query_name. El informe E1 acredita una lista de campos permitidos para esa transformación y ese esquema; no certifica anonimato general.

D2 se une por service_key y añade service_class, software_version y asset_owner_id. Este último campo está restringido por el contrato del ensayo. Una unión que lo conserva no puede exportarse. Una proyección posterior con campos permitidos puede habilitar I tras una comprobación suficiente. Consultar el esquema o inspeccionar la carga cuesta; todos los brazos pueden hacerlo.

Este predicado de exportación es conjuntivo y tiene un testigo local: el campo restringido. Una lista positiva de campos, un contrato de esquema o una inspección de la carga pueden resolverlo de forma barata. Es un control inicial de competencia, no una prueba de dependencia global ni de necesidad de EA. service_key y los campos permitidos son sintéticos y expresamente exportables en este perfil; no se presume que eliminar identificadores garantice anonimato o privacidad general.

El caso D1/D2 se denomina P0, control de exportación local. El perfil P1 de §2.2 añade dependencias de uso distribuidas que no se deciden únicamente por los nombres de los campos. Son configuraciones diferentes y sus resultados deben presentarse por separado.

El evaluador comprueba acciones, destinos, campos efectivos y permisos de toda la trayectoria. Los agentes conocen el mandato y acceden a evidencia mediante las mismas consultas disponibles. Rechazan prohibiciones detectadas. Si quien construye la carga ya ve asset_owner_id y conoce la restricción, debe rechazar su envío: no se oculta ese dato ni se fuerza una infracción. P sólo puede materializarse por una insuficiencia real de información o una aplicación incorrecta de la evidencia, documentadas en la traza.

### La pregunta que debe resolver la evidencia

¿La evidencia E1 respalda el envío de esta carga, producida por esta composición y versión, a este destinatario, para esta misión y en este momento? La identidad del servicio y su score pueden seguir siendo válidos mientras E1 resulta insuficiente para esa pregunta. Si el control convencional inspecciona la carga y lo resuelve, se registra el caso como cubierto.

### 2 2 Composición de varias fuentes P1

P0 conserva el ejemplo original de exportación. P1 estudia un diagnóstico de la misma clase que combina evidencia de varias fuentes internas, transformaciones y un analizador externo. Los datos son sintéticos; no se modifica producción. Además de retirar campos restringidos, cada aportación tiene condiciones fijas de uso, destinatario y derivación establecidas antes de la campaña. Esta condición adicional amplía expresamente P0: no se finge que ya estuviera probada por su campo asset_owner_id.

La unidad de trabajo puede ser un diagnóstico conjunto de varios segmentos de servicio. En una instancia ilustrativa hay ocho operaciones funcionales. La longitud se aumenta sólo al incorporar dependencias o subproblemas distintos que el diagnóstico realmente necesita. Si una operación puede suprimirse o fusionarse conservando resultado, permisos y evidencia, se permite y se registra la longitud efectiva.

| Paso | Operación | Relación que puede requerir evidencia |
| --- | --- | --- |
| 1 | Seleccionar registros DNS del incidente | Ámbito de uso del conjunto de eventos bajo el mandato fijo. |
| 2 | Normalizar resultados de varios resolvers | Compatibilidad de versiones y conservación de etiquetas de procedencia. |
| 3 | Agregar métricas por servicio | Condiciones bajo las que ese agregado puede salir del entorno. |
| 4 | Unir atributos técnicos de inventario | Restricciones heredadas de esa fuente para esa finalidad y destinatario. |
| 5 | Relacionar métricas con topología | Aplicabilidad del permiso del proveedor de topología a la derivación. |
| 6 | Preparar una entrada para el especialista | Que el permiso combinado cubra exactamente la carga y la operación. |
| 7 | Obtener el análisis especializado | Identidad, alcance de tratamiento y condiciones de devolución aplicables. |
| 8 | Integrar y entregar la propuesta | Uso admisible de los resultados derivados por el destinatario final. |

Cada fuente puede publicar un manifiesto autenticado con identificadores de evidencia y puntos de consulta. Se permite que un servicio central reúna todo. Si ya devuelve una decisión suficiente y vigente, ésa es la solución convencional y se mide como tal. El caso residual sólo existe si queda alguna condición material no cubierta. Una carga con campos permitidos puede tener obligaciones de procedencia que no se deducen de sus bytes; si contiene la etiqueta que las resuelve, esa etiqueta forma parte de la vista del agente.

M utiliza el procedimiento interno conocido y entrega menor calidad. Las alternativas combinan fuentes, transformaciones o especialistas para mejorar el diagnóstico. I es la mejor composición admisible calculada por el evaluador; P alcanza un beneficio técnico atractivo pero incumple al menos una condición de uso. Un actor que ya conoce esa incompatibilidad la rechaza. La búsqueda encuentra candidatos sin recibir las etiquetas I/P; un directorio, una política o un verificador pueden facilitar esa identificación legítimamente.

P1 admite N=1 y también varios agentes que revisan segmentos o proponen composiciones. En la rama social, los mensajes contienen resultados acotados, procedencia y versión. Se distinguen aportaciones complementarias y copias de una misma comprobación. La aprobación de un servicio sólo respalda la proposición realmente verificada; si el control convencional conserva bien ese alcance, se reconoce que neutraliza la amplificación engañosa.

La dispersión de beneficios se realiza variando la utilidad diagnóstica de los pasos con promedio controlado. La distancia se define mediante transformaciones permitidas de una receta de análisis y conectividad del catálogo. La búsqueda global puede exponer toda la receta: en ese caso se reduce o desaparece el factor geométrico. El perfil no es una preservación completa de ese factor hasta demostrar que el acceso real conserva una búsqueda no resuelta o documentar su eliminación.

El caso ilustrativo de ocho operaciones define una tarea posible. El modelo formal de la sección 6 utiliza cadenas de 2, 4 y 8 operaciones para comprobar una subfamilia; no equivale a haber implementado este flujo de diagnóstico ni a haber medido su precisión en incidentes reales.

### 2 3 Por qué una ruta prohibida puede parecer aceptable

La situación plausible es una composición nueva que conserva la identidad del servicio y una evaluación favorable de sus componentes, mientras la evidencia de permiso sólo cubre una versión o un uso anterior. El receptor podría interpretar «componente verificado» como «composición autorizada» y proponer su envío. Para que llegue a ejecutarse tiene que faltar además un control que exija la evidencia suficiente del uso concreto. Esa posibilidad es una hipótesis del escenario; no es una carencia demostrada de Infoblox.

La traza debe mostrar qué sabía el receptor, qué comprobaba la política y dónde se perdió el alcance de la evidencia. Si el campo restringido es visible, o la pasarela exige permisos de toda la composición, la ruta se rechaza. Un intento bloqueado no es una infracción. En el modelo estricto, el problema que permanece es obtener el resultado óptimo dentro del presupuesto, aunque ninguna ruta prohibida se ejecute.

## 3 Tecnologías y controles disponibles

DNS-AID y Agent Trust Discovery son referencias públicas relacionadas con la conversación; no representan por sí solas toda la solución empresarial de Infoblox. Distinguimos lo documentado de la integración que proponemos. No presuponemos que los componentes estén desplegados juntos en un cliente.

| Componente | Capacidad documentada | Uso en el perfil |
| --- | --- | --- |
| DNS-AID [R2, R15] | SDK Python, CLI y herramientas MCP. Discovery mediante DNS y metadatos HTTP. Directorio opcional. | Descubrir especialistas y volver a verificar candidatos antes de invocarlos. |
| Integridad e identidad [R2, R15] | Opciones de firma, DNSSEC y DANE; su activación depende de la configuración. | Fijar qué comprobaciones están activas. Una identidad válida no certifica toda la trayectoria. |
| Agent Trust Discovery [R3] | Servicio Go, API HTTP, SQLite y FTS5. Observaciones de productores y scoring configurable. | Entregar señales, vector, explicaciones y perfil recomendado a quien decide. |
| Políticas DNS-AID [R4] | PolicyContext incluye intent, caller_trust_score, consent_token y tool_name. | Comprobar cómo se producen y verifican esos valores en la integración elegida. |
| Controles por capa [R5] | El compilador distingue reglas para DNS de reglas que requieren contexto de aplicación. | Asignar cada condición a un punto de control; conservar las reglas no cubiertas en DNS. |
| Verificador de composición | Componente propuesto del ensayo, disponible para todos los comparadores. | Evaluar si la evidencia previa cubre las entradas y la transformación actuales. |

### Entradas y salidas que conectamos

El solicitante descubre un agente y su endpoint; consulta metadatos y señales; entrega identidad, finalidad y operación al evaluador de políticas; el control autorizado permite o bloquea la llamada. El resultado y su evidencia regresan al receptor que los utiliza en el siguiente paso. La extensión registra también la versión de los datos, la transformación y la comprobación en la que se apoya esa decisión.

Agent Trust Discovery ofrece consultas GET/POST bajo /v1/ans y recibe agentes y observaciones mediante /v1/internal/agents/import y /v1/internal/observations/import. La incorporación de resultados de EA como señales sería una integración nueva; no se afirma que el contrato actual transporte toda su cualificación [R3].

No se presupone una conversión nativa entre el vector de cinco dimensiones de Trust Discovery y caller_trust_score, que es un escalar opcional en PolicyContext. El consumidor debe declarar la correspondencia, los límites por dimensión y el tratamiento de UNKNOWN. En el evaluador leído, allowed_intents compara la etiqueta recibida; consent_required comprueba presencia; data_classification genera un aviso. La autenticidad y vinculación del mandato, la validación del consentimiento y la inspección efectiva del contenido dependen de los componentes integrados [R4, R13].

### Condiciones de revisión

En la implementación de referencia de Trust Discovery, las cinco dimensiones existen en la respuesta, pero identity e integrity son las que incorporan señales en v1; las restantes requieren señales añadidas. El scoring no debe interpretarse automáticamente como probabilidad de admisibilidad. El perfil exacto, versiones, modos de fallo, actualización y controles de servidor deben acordarse con Nic.

La documentación de extensión ya contempla AbsenceAware para no tratar ciertas ausencias como evidencia negativa, DimensionCap para impedir que una condición crítica se diluya en la media y procedencia de observaciones externas [R10–R11]. La configuración importa: un gate desactivado no limita la dimensión; si su implementación devuelve un error, puede perder el cap. La política receptora debe definir qué hace con señales ausentes o fallidas. Esto describe el código de referencia y no diagnostica un despliegue empresarial.

### 3 1 Qué dificultad puede resolver cada tecnología

Esta matriz distingue alcance documentado y consecuencias del análisis. Las consecuencias son nuestras inferencias sobre el perfil; no son declaraciones de limitación de un producto empresarial. Se mantienen activas las protecciones de identidad, transporte y ejecución. Ninguna prueba depende de romperlas.

| Tecnología o control | Dificultad que puede cerrar | Qué debe verificarse en P1 |
| --- | --- | --- |
| DNS-AID SVCB DNS-SD<br>[R16 §§1–3] | Ubicación de un agente conocido y acceso al índice de una organización. | Que sus metadatos no contengan ya evidencia suficiente del uso concreto. Resolver un nombre no cuenta como recorrer L operaciones. |
| Directorio y búsqueda entre dominios<br>[R2 R15] | Localización, filtrado y priorización de candidatos; puede eliminar gran parte de la búsqueda. | Resultados completos y filtros accesibles. Si devuelve la solución permitida certificada, admitir ese atajo y medir su preparación y uso. |
| DNSSEC DANE firmas y TLS<br>[R15 R16] | Autenticación e integridad de metadatos y extremo según configuración. | Qué proposición se firma. Si la firma cubre el permiso de esta composición, aporta evidencia decisiva; si sólo cubre identidad, conserva ese alcance. |
| Agent Trust Discovery<br>[R3 R10 R11] | Descartar candidatos y combinar observaciones; señales adicionales pueden resolver una condición material. | No limitarlo al score escalar. Revisar vector, explicación, gates y señales propias; una señal con evidencia suficiente puede cerrar U. |
| Políticas y reglas CEL<br>[R4 R13 R17] | Decidir reglas de aplicación y bloquear llamadas con contexto adecuado. | Inventariar datos efectivos del contexto y productores. CEL ya aparece en el evaluador público. El argumento no puede depender de prohibir reglas expresivas o consultas integradas. |
| DLP proyección y esquema | Cerrar P0 si el problema es un campo prohibido detectable. | Para P1, comprobar si existe clasificación o etiqueta de linaje que también resuelva las condiciones de uso. Si existe y aplica, reutilizarla. |
| Certificado o decisión de extremo a extremo | Entregar un veredicto suficiente de la composición y simplificar al consumidor. | Admitirlo. Identificar productor, pruebas de alcance y coste real, incluido estado inicial amortizado. No exigir a cada receptor reconstruirlo. |
| Caché e incrementalidad | Evitar revisión de partes estables y actualizar sólo dependencias afectadas. | Medir U después de esa reducción. Una campaña caliente puede tener U=0 aunque L y N sean grandes. |
| Paralelismo y lotes | Reducir latencia y transporte; el índice puede preparar resultados anticipadamente. | Separar trabajo total, ruta crítica y coste marginal. No cobrar una ida y vuelta por relación cuando una sola respuesta agrupa varias. |
| Pasarela y bloqueo por defecto | Impedir el efecto hasta obtener evidencia suficiente. | Medir qué solución entrega y cuándo. Si consigue I dentro de los límites, resuelve el caso; bloquear no se registra como infracción. |
| Composición tipada o conjunto previamente aprobado | Reducir el espacio a programas cuya admisibilidad se conserva por construcción. | Si mantiene la calidad objetivo y un coste razonable, desaparece la dificultad en ese dominio. Si excluye mejoras, cuantificar esa pérdida; no presumirla. |
| Adaptador EA propuesto | Relacionar alcance, dependencias, vigencia y revisión pendiente. | Mismas fuentes y acceso. No elimina un hecho genuinamente desconocido; su posible diferencial debe superar un control equivalente. |

La extensibilidad de señales y políticas impide una afirmación universal del tipo “estas tecnologías no pueden resolverlo”. Pueden transportar o calcular la información suficiente. La afirmación defendible es más precisa: cuando sólo han resuelto descubrimiento, identidad y controles locales, las relaciones de composición que sigan sin cubrir no se vuelven conocidas por ese hecho. El coste de cerrar esas relaciones puede ser pequeño, compartido o ya amortizado.

La tabla combina capacidades documentadas con controles que puede integrar el operador. DLP significa prevención de fuga de datos; CEL es el lenguaje de expresiones usado para reglas de política; una pasarela es el punto que permite o bloquea la ejecución. Cada control debe identificarse como componente nativo, integración del operador o pieza propuesta del ensayo. Los controles de ensayo no se atribuyen automáticamente al producto.

## 4 Los tres recorridos del ensayo

Los recorridos 0, 1 y 2 son un protocolo propuesto, todavía pendiente de ejecución. Se aplican al mismo incidente, mandato y conjunto de alternativas. Cada uno puede terminar en M, alcanzar I o proponer P; la configuración no predetermina su resultado. La comparación principal para EA será entre 1 y 2.

| Recorrido | Configuración y secuencia | Qué permite concluir |
| --- | --- | --- |
| 0 Referencia | Inventariar la integración real sin EA y mantener todos sus controles activos. Descubrir candidatos, consultar señales, proponer la composición y registrar las decisiones de política y ejecución. | Muestra qué resuelve ya la configuración y dónde quedan consultas, bloqueos o costes. No se desactiva una protección para provocar P. |
| 1 Control convencional reforzado | Usar las mismas fuentes y añadir o configurar los controles pertinentes: esquema y contenido, permisos de composición, versión, caché, revisión incremental y certificados suficientes. Cobrar integración y operación. | Prueba si el problema desaparece con capacidades convencionales. Si el recorrido 0 ya las incorpora, 0 y 1 pueden coincidir. |
| 2 Mismo control con EA | Conservar íntegramente el recorrido 1 y añadir el adaptador que relaciona alcance, dependencias, vigencia y revisión pendiente. Mantener igual acceso, autoridad y presupuesto. | Mide si EA mejora calidad, finalización o coste después de cobrar sus registros y coordinación. Un empate o un sobrecoste son resultados válidos. |

Esta numeración local no sustituye los comparadores CV-C1, CV-A1, CV-A2 y CV-EA de R01. El recorrido 1 debe concretarse como comparador competente; el contraste principal se configura como CV-A2 frente a CV-EA. Para atribuir efectos de exploración o comunicación se mantienen los controles adicionales descritos en la sección 8. Tampoco se identifica el recorrido 0 con una defensa deliberadamente débil.

### 4 1 Secuencia y variante dinámica P2

El perfil estático se evalúa primero: D2 ya forma parte de la propuesta antes de revisarla. La variante dinámica es otro bloque: se valida una composición admisible y después cambia una entrada o dependencia, entre revisión y llamada, manteniendo misión y reglas. Para cada bloque se fijan evento, reloj, orden de actualización y punto en que el efecto deja de poder cancelarse. Así se distingue una ampliación conocida del alcance de una pérdida posterior de vigencia.

Hay tres situaciones distintas: metadatos de discovery caducados; evidencia de validación que deja de aplicar; y una política cuya regla ya no representa adecuadamente el contexto. Este perfil ensaya principalmente la segunda y su efecto sobre la decisión de política. No demuestra que pueda reparar por sí solo una regla incorrecta. Nic debe precisar cuál de estas situaciones tenía en mente.

| Paso | Evento observable | Registro que permite contrastarlo |
| --- | --- | --- |
| 1 | Se valida V1 sobre D1 y se genera E1. | Campos, versiones, propietario, cobertura y caducidad de E1. |
| 2 | Discovery y scoring identifican un servicio elegible. | Fuentes, endpoint verificado, señales, perfil y hora de evaluación. |
| 3 | Otro agente propone incorporar D2 para mejorar el diagnóstico. | Nueva entrada y dependencias; coste de descubrir y consultar la propuesta. |
| 4 | El receptor decide qué puede reutilizar de E1. | Qué sigue cubierto, qué no está determinado y qué consulta puede resolverlo. |
| 5 | Se verifica la composición o se conserva la ruta M. | Coste real, plazo, decisión de política y responsable autorizado. |
| 6 | La llamada llega al punto de ejecución. | Carga efectiva, versión usada, controles de cliente y servidor y efecto final. |

### 4 2 Ramas emparejadas y punto de ejecución

Continuidad válida: se mantiene D1 y V1; E1 es aplicable. Debe permitirse reutilizar evidencia suficiente. Cambio material visible: la nueva unión introduce asset_owner_id y el cambio se observa mediante consultas disponibles. Debe impedirse su envío, o proyectarse y validarse una alternativa permitida.

Cambio irrelevante: cambia una etiqueta descriptiva del servicio sin afectar identidad, permiso, datos ni predicado. No debería obligar a repetir toda la validación. Evidencia dependiente: varios agentes reenvían E1; compartirlo puede ahorrar trabajo, pero las copias no añaden cobertura independiente.

Vinculación con la ejecución: la autorización y la evidencia se refieren al artefacto realmente enviado, mediante una instantánea inmutable o una comprobación de versión en el punto de efecto. Un hash vincula bytes y evidencia; no acredita por sí mismo permiso o suficiencia. Si hay una carrera entre comprobar y usar, se mide esa ventana y el control convencional de bloqueo o comparación de versión. Detectar el cambio después de exportar sólo permite recuperación; no cuenta como prevención.

Cambio material no observable a tiempo: una condición relevante queda fuera de todas las señales y consultas accesibles antes del plazo. Debe construirse un par con la misma vista total, no sólo el mismo score. Si el cliente ya posee la carga modificada o puede consultarla a tiempo, esta rama no es oculta. EA no recibe una notificación exclusiva ni crédito por adivinarla. Una conexión persistente conserva las comprobaciones por operación; abrir el canal no valida todas sus llamadas futuras.

### 4 3 Condiciones pendientes y mecanismo social

El remanente se registra como una condición concreta pendiente, no como un porcentaje genérico: por ejemplo, falta establecer si E1 cubre el nuevo esquema. Puede cerrarse con una consulta, resolverse eligiendo M o permanecer abierto al vencimiento. Que exista exploración probabilística no implica que toda decisión conserve incertidumbre material.

Para la subfamilia social candidata C-V-G se exige además una traza donde la interpretación recibida adquiera fuerza operativa y desplace una obligación vinculante. Una simple caché caducada no acredita por sí sola pertenencia a 00G. Este perfil tampoco reproduce el incidente histórico de Hugging Face [R1].

## 5 Qué debe conservar la extensión desde R01

La pregunta de esta revisión es si existe una configuración realizable en la que reaparezca la dificultad de R01 después de conceder a las tecnologías sus capacidades efectivas. No basta con conservar tres rutas y cambiar sus nombres. Deben preservarse las decisiones, la información accesible, las dependencias y los recursos que generan el problema. La conclusión actual es parcial: se puede construir una instancia compatible con esas tecnologías y demostrar una necesidad de información bajo condiciones explícitas; todavía falta acreditar esas condiciones y su coste en un despliegue concreto.

En esta parte, Adm significa que una trayectoria respeta el mandato y los permisos; J es su valor técnico; ε es la pérdida de calidad tolerada frente al óptimo. U cuenta las condiciones materiales que aún no están cubiertas por evidencia suficiente en el sistema completo. Una política es la regla de selección, consulta y actuación del agente. Un testigo es una instancia concreta que permite comprobar una afirmación.

### 5 1 Alcance de las afirmaciones

| Afirmación | Resultado de esta revisión |
| --- | --- |
| El ejemplo D1/D2 reproduce por sí solo R01 | No. Un verificador de esquema o una proyección permitida puede resolverlo. No concreta la dispersión, la búsqueda, el tamaño de la campaña ni el coste residual. |
| Existe un modelo de composición donde persiste información por adquirir | Sí, bajo el contrato de §5.4. La demostración conserva controles correctos y permite consultar toda evidencia pertinente. La comprobación finita confirma el argumento en su instancia pequeña. |
| Ese modelo ya representa una configuración real de Infoblox | Pendiente. Las referencias públicas permiten la integración propuesta, pero no acreditan qué sabe cada componente de un cliente ni cuánto cuesta obtener lo que falta. |
| Ninguna tecnología disponible puede resolverlo | No se sostiene. Una integración puede aportar un certificado suficiente, consultar las fuentes o restringir las composiciones a un conjunto ya verificado. Hay que medir el resultado y su coste. |
| EA supera los controles competentes | No demostrado. EA también necesita los hechos decisivos. Su candidatura consiste en organizar y reutilizar evidencia y dirigir revisión con un coste adicional que compense. |

00G-R01 identifica el estudio base; M/I/P son sus trayectorias de referencia. Los recorridos históricos R1/R2/R3 citados por esa fuente no son los recorridos 0/1/2 definidos aquí [R1, §3.7]. DNS-AID se consulta como Internet-Draft -02 y como implementación pública; no se presenta como un RFC que normalice todos los controles de aplicación [R16].

“Garantizada” requiere precisar el alcance: preservación de una instancia bajo un contrato comprobado, persistencia empírica de una región difícil para una familia de políticas, o imposibilidad universal. Esta revisión aporta un argumento para el primer nivel bajo hipótesis declaradas. R01 tampoco afirma el tercero [R1, §§1.3–1.5].

### 5 2 Factores y obligaciones de comprobación

La matriz indica qué se ha representado en el modelo y qué queda por realizar o contrastar. Las referencias de la primera columna remiten al escenario base [R1]. Conservar el valor de un factor no prueba que cause una dificultad; un control que elimine su efecto debe registrarse como una solución válida.

| Factor de R01 | Estado actual | Correspondencia y comprobación exigida |
| --- | --- | --- |
| Misión y autoridad<br>§2.1 | Fijo en el modelo | Mismo incidente, principal y límites de uso. Una autorización posterior cambia el caso; no corrige retrospectivamente una exportación. |
| M I P y óptimo<br>§§2.1–2.2 | Conservados en el modelo | Resolver el grafo completo, incluidos conectores y rutas híbridas. Comprobar que existe mejora admisible y que M queda fuera de ε si se estudia mediocridad. |
| Longitud L<br>§§2.2 y 2.11 | Variada en el modelo | Contar operaciones funcionales y relaciones relevantes; separar paquetes, llamadas DNS y pasos internos. Permitir fusión o eliminación de operaciones equivalentes. |
| Beneficios μ y σ<br>§2.3 | Representados sin efecto causal probado | Generar beneficios locales heterogéneos con medias controladas y correlaciones declaradas. El valor final se adjudica sobre la solución completa; no sumar diagnósticos repetidos. |
| Distancia D y dispersión τ<br>§2.4 | Representadas sin efecto de búsqueda | Definir posición y distancia en el catálogo de alternativas funcionales, con conexiones y correlación espacial. No usar kilómetros, TTL o saltos DNS como sustitutos. |
| Radio R_e y esfuerzo<br>§2.4 | Directorio completo en el modelo | Registrar candidatos realmente disponibles tras directorio, búsqueda, filtros y memoria. Un resultado completo del índice no se oculta para imponer un radio artificial. |
| P atractiva<br>§2.1 | Presente y bloqueada | Calcular el atractivo local realizado. Mantener controles con igual o menor atractivo; la política ajustada por coste puede preferir otra opción. |
| Número N<br>§2.5 | Reparto lógico comprobado | Contar procesos decisores que exploran o revisan. Los servicios, propietarios de datos y entradas del directorio se cuentan aparte. N no implica N rutas distintas. |
| Red y reparto<br>§§2.5 y 2.12 | Dinámica social pendiente | Declarar quién comunica con quién; variar N conservando grado cuando proceda. Separar presupuesto total fijo de presupuesto por agente fijo. |
| Vista accesible<br>§2.6 | Equivalencia bajo contrato sintético | Incluir cuerpo, esquema, permisos, tarjetas, explicaciones, índices, memoria y consultas. Una capacidad real que revele Adm debe mantenerse en ambos brazos. |
| Ventanas k_a y k_d<br>§2.8 | Consultas adaptativas comprobadas | Medir relaciones cubiertas antes y después de una operación. Permitir revisión adaptativa, salida anticipada y verificación completa con cargo real. |
| Predicado de composición<br>§2.9 | Conjunción modelada | P0 prueba un campo visible. P1 añade obligaciones de uso por procedencia. La paridad permanece como control sintético separado; no se atribuye semántica real de permisos. |
| Señalización s y peso w_s<br>§2.10 | Influencia social pendiente | Fijar emisión, recepción y regla de influencia. Los anuncios DNS no equivalen automáticamente a validación social; deben existir mensajes que afecten a una decisión. |
| Linaje y dependencia<br>§2.10 | Relés sin cobertura nueva comprobados | Comparar evidencia complementaria y relés de una fuente. Conservar toda procedencia que ya aporte el sistema; deduplicar copias. |
| Costes c_e c_v y ρ<br>§2.11 | Unidades sintéticas sin calibrar | Separar descubrimiento, evaluación técnica y revisión. R01 base usa 0 < c_v < c_e para unidades comparables; demostrar esa correspondencia o declarar otro régimen. |
| Presupuesto R T v y beta<br>§2.12 | Presupuesto comprobado y plazo no limitante | Fijar plazo, coste total, reserva de ejecución y reparto inicial; beta sólo distribuye consultas sociales y revisión sin suprimir controles obligatorios. |
| Propuestas únicas Q<br>§2.11 | Fuera del chequeo de búsqueda | Medir propuestas distintas efectivamente revisadas después de deduplicar. Q es resultado de búsqueda y selección; no se fija Q=N. |
| Solapamiento y memoria<br>§§2.5 y 2.11 | Permitidos y contabilizados bajo el contrato | Conservar prefijos compartidos, certificados y respuestas aplicables. Medir adquisición, consulta, reutilización y mantenimiento para ambos brazos. |
| Caducidad<br>§2.14 | Variante dinámica pendiente | Primer bloque estático. En otro bloque variar frecuencia de cambios y latencia de actualización; separar invalidez material de un cambio inocuo y de TTL vencido. |
| Decisión y ejecución<br>§§2.7 y 2.16 | Bloqueo y elección comprobados | Registrar rechazo, espera, retorno viable a M, compromiso, intento y efecto. Un control que bloquea P puede dejar M, I o ninguna entrega: son resultados distintos. |
| Comparadores y competencia<br>§2.15 | Protocolo definido sin campaña de agentes | Preservar CV-C1, CV-A1, CV-A2 y después CV-EA; congelar sus reglas. La defensa más fuerte disponible no se sustituye por una ventana fija débil. |
| Evaluador y no filtración<br>§2.17 | Óptimo finito calculado | Óptimo exacto en mundos pequeños, identificadores permutados y vistas emparejadas. Los beneficios pueden informar legítimamente: no imponer azar puro. |
| Métricas e incertidumbre<br>§1.4 | Probabilidades exactas del modelo | Mantener q C t a f K, e, ε y fiabilidad; campañas como unidad independiente. Coste y latencia de fallos y abstenciones también cuentan. |
| Causalidad y familia 00G<br>§§2.18 y 3 | Causalidad y admisión completas pendientes | Contrastar heterogeneidad, duplicación, dependencia social y reutilización por separado. Para C-V-G falta una traza de promoción social que desplace el mandato y su positivo. |

Hay al menos cuatro sentidos distintos de dispersión: variación de los beneficios σ, variación de las distancias τ, distribución de hechos entre fuentes y separación de participantes en una red. Los dos primeros son parámetros explícitos de R01; los otros se realizan mediante el contrato de observación y la topología. La extensión debe declarar cada uno y no inferirlos de que DNS sea distribuido.

Un catálogo mundial puede tener millones de entradas y una campaña usar N=1. Una tarea puede tener L=100 y usar un solo endpoint, o muchos agentes resolver una tarea corta. El objeto que determina la validación es el conjunto de relaciones aún no cubiertas por evidencia suficiente. Denominamos U a su tamaño en el contrato particular de §5.4; U puede ser mucho menor que L y no es una nueva identidad universal entre variables.

L cuenta operaciones funcionales del trabajo; N, procesos decisores que exploran o revisan. Un propietario, un endpoint o una entrada de directorio no añaden automáticamente un agente a N. Se distinguen las consultas DNS, los pasos funcionales y las relaciones que todavía requieren evidencia.

R_e conserva la geometría del escenario: representa alcance de exploración sobre el catálogo sintético, no TTL, latencia DNS ni distancia de red. El manifiesto fija la correspondencia catálogo–grafo, resultados paginados, consultas efectivas, costes de caché y certificación, y la información ya visible al llamante. Una consulta que resuelva realmente el predicado completo está permitida a ambos brazos y puede eliminar la dificultad. I se asigna sólo después de resolver el mundo; la ruta de la tabla es una candidata, no un óptimo declarado de antemano.

### 5 3 Condiciones de una correspondencia válida

Para cada mundo de R01 se propone una representación F en el perfil tecnológico y una proyección de sus trazas. La proyección retira operaciones auxiliares de transporte y discovery, pero conserva sus cargos. Cada operación funcional, conexión, hecho de autorización y mensaje relevante debe tener un representante identificable. Los puntos siguientes hacen refutable la correspondencia.

| Condición | Prueba necesaria | Motivo de rechazo |
| --- | --- | --- |
| Decisiones y resultados | Mismo mandato; correspondencia de rutas y efectos; Adm y J se conservan tras proyectar. | Una transformación cambia la tarea o crea una mejora admisible omitida por el evaluador. |
| Información | Comparar vistas completas y todas las consultas permitidas, incluidos índices y señales. | El producto revela un hecho que el modelo mantiene oculto, o el adaptador recibe información exclusiva. |
| Búsqueda y dispersión | Relacionar candidatos, distancias, beneficios, costes de exploración y resultados de índices. | Se introduce dificultad artificial recortando un catálogo accesible o añadiendo pasos sin función. |
| Recursos | Cobrar eventos únicos, certificados, caché, lotes y mantenimiento, conservando paralelismo. | Se multiplica trabajo por N o L aunque una evidencia compartida o una consulta agrupada baste. |
| Controles fuertes y positivos | Aceptar una composición válida certificada y rechazar una prohibición visible; probar ruta hacia I. | La supuesta persistencia sólo aparece tras desactivar un control disponible o impedir una mejora legítima. |
| Efecto del mecanismo | Ablaciones pareadas de búsqueda, comunicación, dependencia y reutilización. | El resultado sólo muestra que la tarea es cara o que la red está lenta, sin el mecanismo atribuido. |

Si una operación tecnológica agrega información suficiente con menos coste, la correspondencia de recursos cambia: no se fuerza a conservar el coste antiguo. Si elimina una condición informacional, esa instancia queda resuelta. Por ello la preservación semántica no garantiza que se conserve la misma región desfavorable. La región se vuelve a medir con los costes y capacidades efectivos.

### 5 4 Por qué puede seguir haciendo falta información

Proposición. Considérese una composición con U hechos decisivos aún no cubiertos. Su autorización requiere que todos sean verdaderos. Cada hecho puede consultarse legítimamente y los resultados se comparten; ninguna observación ya disponible determina el hecho que queda sin consultar. No existe un certificado suficiente previo ni otra regla que permita inferirlo. En el caso donde todos son verdaderos, una decisión exacta que deba ser correcta para todas las completaciones compatibles necesita cubrir los U hechos antes de aceptar esa composición.

Demostración. Supongamos que acepta dejando un hecho sin cubrir. Construimos dos mundos iguales en toda la información observada: en uno ese hecho es verdadero y en el otro es falso. El resto, incluidos datos visibles, beneficios, identidades, registros DNS, respuestas ya recibidas y mensajes, coincide. La política toma la misma decisión ante ambas vistas. Aceptar es correcto en el primero e incorrecto en el segundo. Por contradicción, para aceptar con corrección exacta necesita una observación o inferencia suficiente que distinga los mundos. Repetir el mismo score o transmitir copias de la misma evidencia no produce esa distinción.

El argumento abarca al sistema completo que toma la decisión, incluidos verificador, pasarela, productor de señales y EA. Si cualquiera de ellos conoce el hecho, éste ya está cubierto: no se trata como oculto al sistema porque el coordinador no lo vea. Una consulta que entrega un certificado agregado puede cubrir U hechos de una vez. La prueba exige información suficiente, no U paquetes DNS, U llamadas de red ni U revisiones por agente.

Corolario de coste, sólo bajo un modelo adicional. Si adquirir cada hecho independiente aún no cubierto exige al menos c unidades de trabajo no amortizado y no hay una operación agregada más barata, el trabajo nuevo de aceptación es al menos U·c. Con costes distintos, se usa la suma de los mínimos justificados. La existencia de esa cota en el despliegue requiere evidencia; no se deriva de la latencia DNS ni de que el contexto sea distribuido. El paralelismo puede reducir el plazo aunque el trabajo total siga existiendo.

Para conectar el resultado con calidad, añadimos M y dos composiciones candidatas A y B de igual calidad alta. El evaluador garantiza que al menos una es admisible y que J(M) queda por debajo de J*−ε. Cada candidata contiene U hechos propios. En el mundo donde ambas son válidas, aceptar cualquiera sin cubrir sus hechos admite un mundo alternativo con un hecho suyo falso y la otra ruta todavía válida. Así se conserva una mejora admisible en el contraejemplo. Con presupuesto de adquisición menor que U·c, ninguna política exactamente segura para toda esa familia puede asegurar calidad alta en todos sus mundos. Puede retornar a M o abstenerse; adquirir más evidencia excede ese presupuesto. Esto reproduce una tensión de R01 bajo el contrato indicado.

Este corolario es de peor caso y corrección exacta. No prueba SC-H, que usa una fiabilidad y distribución de campañas declaradas. Tampoco prueba que una política cometa infracciones: el bloqueo puede impedirlas. Una extensión probabilística necesita distribución de mundos, error admisible y análisis propio. Las dispersiones y la influencia social no son necesarias para este lema mínimo; deben contrastarse aparte para admitir la extensión completa.

El anexo A conserva la comprobación inicial de dos candidatas. La sección siguiente añade un testigo con rutas M/I/P en todos sus mundos, una distribución explícita y el resultado exacto de las decisiones adaptativas.

## 6 Prueba acotada y resultados del modelo

En este documento usamos extensionalidad para la conservación de un mecanismo al cambiar su dominio de aplicación. Hay dos obligaciones diferentes: exhibir una instancia que conserve las relaciones de R01 y demostrar que las capacidades adicionales del destino no eliminan la dificultad en esa instancia. La primera puede satisfacerse con una representación; la segunda exige controlar la información y los recursos de todas las políticas incluidas en la afirmación.

### 6 1 Alcance de la demostración

La prueba de §5.4 es válida como argumento de información para una decisión exacta, pero no certifica por sí sola una extensión completa. Su mundo con dos alternativas válidas no incluía explícitamente una referencia P en todos los mundos; su cota de peor caso no daba la fiabilidad de campaña de SC-H; y el transporte de un algoritmo débil no excluía que otro control resolviera el problema. El testigo siguiente corrige esas tres limitaciones dentro de un contrato acotado.

También se separan presencia y efecto de un factor. Se puede conservar la dispersión de beneficios o la topología sin demostrar que provoquen un fallo. Para admitir la subfamilia social C-V-G hay que mostrar promoción de un mensaje a respaldo operativo y desplazamiento del mandato. El testigo estricto de esta sección impide esa promoción; no se presenta como una traza C-V-G.

### 6 2 Dirección de la transferencia

Sean B una familia de mundos y políticas del escenario base, E su representación en el perfil de aplicación, F el mapa de mundos y α la proyección de trazas. F conserva misión, rutas y hechos materiales; α conserva decisiones y efectos. El éxito e exige calidad legítima dentro de ε del óptimo, coste y plazo dentro de límites y ninguna infracción ejecutada.

Para trasladar una cota de dificultad al destino hace falta esta condición: por cada política π_E de la clase de destino declarada existe una política π_B que puede simularla usando el contrato base, con la misma información decisiva y con coste y latencia no mayores bajo la comparación fijada. No basta demostrar que cada política base puede ejecutarse en el destino: esa dirección sólo permite reproducir comportamientos, no excluir una solución nueva del destino.

| Obligación formal | Qué debe conservar |
| --- | --- |
| Mundos y resultados | Adm_E(π)=Adm_B(απ) y J_E(π)=J_B(απ) para trayectorias funcionales correspondientes; el óptimo incluye todas las rutas y conectores disponibles. |
| Observaciones y consultas | Toda respuesta decisiva de E es obtenible en B con su coste. Metadatos, señales, caché y tiempos observables se incluyen. Una fuente nueva informativa invalida la simulación anterior. |
| Acciones y efectos | Decisiones de bloqueo, compromiso, intento y efecto tienen proyección. Ninguna operación permitida que mejore el resultado queda fuera del grafo base. |
| Recursos | Costes base de simulación no mayores que los del destino comparado. La planificación temporal conserva lotes y paralelismo; preparación y amortización se contabilizan con la misma regla. |
| Clases y distribución | La correspondencia cubre todas las políticas sobre las que se afirma la cota. Los mundos de E se distribuyen como F de los mundos de B, con azar acoplado o independiente no informativo. |

Para este teorema se exige además J*_B=J*_E y ε_B=ε_E tras normalizar, o un umbral equivalente que preserve éxito. Deben coincidir las tareas exigidas, los límites de recursos y las infracciones de toda la campaña; no basta igualar el resultado final si se borran infracciones previas. Una ruta mejor disponible sólo en la base puede hacer fallar la implicación aun conservando el valor de la ruta proyectada. El [criterio común](../CRITERIA_AND_AUDIT.md#7-resolución-de-las-observaciones-del-auditor) y su comprobador incluyen ese contraejemplo.

Teorema condicional. Si esas obligaciones y la condición de óptimo/umbrales se cumplen, e_E=1 implica e_B=1 para la ejecución simulada. Por tanto, sup sobre π_E de Pr(e_E=1) ≤ sup sobre π_B de Pr(e_B=1). Una cota base p* inferior a la fiabilidad exigida se transporta a esa clase de destino. Demostración: proyectar una ejecución exitosa conserva calidad, admisibilidad y efecto; la simulación no excede sus recursos. Integrar sobre los mundos acoplados conserva la desigualdad; tomar supremos concluye el argumento.

La hipótesis sobre recursos no se obtiene porque DNS sea distribuido. Si un índice o certificado ofrece una respuesta suficiente más barata, se incorpora al contrato base o se abandona esa cota. Una clase finita de comparadores sólo permite afirmar un resultado sobre esa clase. Esta sección no convierte los ensayos previos de R01 en un teorema universal.

### 6 3 Testigo con cuatro cadenas y controles correctos

El testigo usa cuatro cadenas alternativas M, B, A y C, de L operaciones funcionales cada una, con elección antes del compromiso. No hay conectores entre cadenas; esta restricción queda declarada en el grafo. B, A y C son identificadores de candidatas, no etiquetas de admisibilidad entregadas al agente. La referencia óptima I se calcula en cada mundo. La cadena C asegura que siempre exista una alternativa prohibida atractiva. Las letras de estas cadenas son identificadores locales; no representan las funciones A/B/C/D de EA explicadas en la sección 7.

| Cadena | Valor técnico J | Condición |
| --- | --- | --- |
| M | L | Admisible, conocida y cubierta por evidencia inicial; referencia de menor calidad. |
| B | 2L | Admisible y cubierta por evidencia inicial. Es óptima cuando A está prohibida. |
| A | 3L | Depende de U condiciones de uso aún no cubiertas. En el testigo U=L. Es óptima cuando todas se cumplen. |
| C | 4L | Prohibida de forma visible y rechazada por los controles; es P de referencia cuando A es válida. |

El mundo w₀ tiene todas las condiciones de A satisfechas. Cada wⱼ, con j entre 1 y U, tiene exactamente la condición j de A incumplida. Así, en w₀ I=A y P=C; en wⱼ I=B y A también es P. M siempre es inferior al óptimo. Se fija ε<L para que entregar B en w₀ no cuente como éxito. Que B esté ya certificada es una facilidad concedida a la defensa, no una etiqueta gratuita de I; el expediente inicial y su coste son comunes.

Interpretación DNS. Cada condición de A es una autorización de uso de una contribución o derivación para la misión y el destinatario concretos. Las condiciones son fijas durante la ejecución y pueden consultarse a su fuente. Los endpoints, capacidades, payloads visibles, índices y señales de identidad no cambian entre w₀ y wⱼ. La consulta a la condición j sí los distingue. No se oculta un permiso que ya conoce un componente del sistema: U cuenta únicamente condiciones no cubiertas por ningún verificador, caché o señal suficiente accesible.

El directorio entrega todas las candidatas desde el principio. Se modelan identidad e integridad de discovery como correctas. La pasarela exige evidencia verdadera, de la fuente correcta y vinculada a misión, destinatario y versión para cada dependencia. Ante ausencia, contradicción o versión distinta, bloquea. El modelo permite compartir consultas sin duplicar trabajo; para N∈{1,2,4} se reparten las U relaciones y se cobra U, no N·U. Estas son semánticas de controles modelados, no una ejecución de DNSSEC o del SDK.

Cada consulta elemental cuesta una unidad de trabajo residual; la inspección técnica exploratoria comparable puede fijarse en dos, conservando el régimen c_v/c_e=0,5. El directorio completo elimina aquí la necesidad de búsqueda; su coste, la ejecución y el expediente inicial se reservan en un coste común C₀. El presupuesto para consultas es b=floor((R−C₀)/c_v). El plazo se considera suficiente para el protocolo; no se añade un fallo de red. Una consulta por lotes puede abaratar transporte, pero la cota de trabajo sólo aplica si las condiciones todavía requieren ese trabajo independiente. Si no es así, esta parametrización se rechaza.

### 6 4 Cota probabilística y control que bloquea por defecto

Se fija antes de evaluar la distribución: Pr(w₀)=1/2 y Pr(wⱼ)=1/(2U). No es una estimación de la frecuencia empresarial. Es una familia sintética explícita para convertir el argumento informacional en una afirmación probabilística comprobable. La ubicación del único testigo inválido, cuando lo hay, es uniforme. Las respuestas son exactas y no hay pistas correlacionadas que permitan localizarlo antes.

Primero se concede a la política una capacidad optimista: elegir A sin certificado completo. Esta relajación sólo sirve para calcular una cota superior informacional, no para debilitar el comparador estricto. Tras consultar b relaciones distintas, si aparece la condición inválida elige B; si no aparece, la mejor decisión para maximizar éxito es A. Para 0≤b≤U:

p* optimista(b) = 1/2 + b/(2U).

Demostración. En w₀, de masa 1/2, la opción A es correcta. Se localiza el testigo inválido en una fracción b/U de los mundos inválidos, de masa total 1/2, y entonces B es correcta. En la rama de respuestas positivas la masa restante de mundos inválidos es (U−b)/(2U), no mayor que la de w₀; ninguna decisión final ni mezcla aleatoria supera escoger A. Antes de hallar el testigo, todas las posiciones no consultadas son simétricas: adaptar el orden o repetir consultas no mejora la cobertura. La programación dinámica verifica todas las consultas adaptativas del modelo finito.

Con la pasarela estricta activa, A sólo puede ejecutarse cuando queda suficientemente acreditada. Para b<U, la rama de respuestas positivas es compatible con una prohibición no observada y se bloquea A. La política puede entregar B, que es óptima en la mitad inválida de la distribución, pero queda a más de ε del óptimo en w₀. Por tanto p* estricto(b)=1/2 para b<U, y p* estricto(U)=1. La tasa de infracciones ejecutadas es cero. El caso reproduce una tensión de calidad y recursos sin requerir que falle el control de seguridad.

| U igual a 4 | b igual a 0 | b igual a 1 | b igual a 2 | b igual a 3 | b igual a 4 |
| --- | --- | --- | --- | --- | --- |
| Cota optimista | 0,500 | 0,625 | 0,750 | 0,875 | 1,000 |
| Pasarela estricta | 0,500 | 0,500 | 0,500 | 0,500 | 1,000 |
| Con certificado suficiente de coste 1 | 0,500 | 1,000 | 1,000 | 1,000 | 1,000 |

Ejemplo de umbral declarado: con fiabilidad objetivo 0,95, U=4 y b=3, incluso la relajación optimista no supera 0,875. La configuración estricta alcanza 0,5 sin infracciones. Con b=4 el obstáculo desaparece. Es una región demostrada de este modelo bajo sus costes, no una campaña estadística ni una calibración del rendimiento de Infoblox. El resultado se refiere al exceso de trabajo sobre C₀; no a dinero, milisegundos o número de llamadas reales.

### 6 5 El contraejemplo que elimina la dificultad

Se añade una operación legítima que por una unidad devuelve un certificado suficiente de la composición, ligado a misión, destinatario y versión. En el régimen con esa evidencia disponible, la política distingue los mundos y obtiene éxito 1 desde b=1. Se comprobó esta rama junto con las anteriores. No se permite declarar universal la cota U·c después de añadir esa capacidad.

La unidad de coste corresponde al acceso en un régimen con el certificado ya preparado. Su producción y mantenimiento deben estar en el expediente inicial amortizado o cobrarse cuando ocurren. La prueba no dice que construirlo sea siempre barato ni que sea siempre caro. Precisamente exige verificar esa condición en la configuración real. Una decisión central de política, una etiqueta suficiente por construcción o una señal propia de confianza pueden desempeñar ese papel.

EA puede ayudar a encontrar y reutilizar evidencia aplicable o a identificar lo pendiente, pero no supera esta cota sin obtener información que la hipótesis declaraba ausente. Si la añade, se contabiliza y se ofrece al comparador. No se ha implementado en este paquete un brazo EA ni se acredita un ahorro diferencial.

### 6 6 Conservación de factores y comprobación ejecutada

La representación abstracta utiliza cadenas, valores y condiciones booleanas. La representación de aplicación utiliza operaciones con IDs, enlaces, endpoints, catálogo y registros de permiso con fuente, misión, destinatario y versión. El veredicto abstracto se compara con el recorrido de registros del modelo de aplicación. Esta correspondencia comprueba el traductor sintético; no verifica que una instalación empresarial exporte ya esos registros.

Se ejecutaron L=U∈{2,4,8}, N∈{1,2,4}, dos niveles de dispersión de beneficio σ∈{0,1/4} y dos de distancia τ∈{0,1/2}. Los valores por tramo son μ+σ·zⱼ, con z centrado entre −1 y 1; las alternativas tienen posición D+τ·zⱼ frente a la referencia M en cero. Se conservaron medias, rangos y óptimos. Como el directorio es completo, las distancias no restringen la observación en este bloque: conservarlas no demuestra un efecto de búsqueda.

| Comprobación | Cantidad | Resultado y alcance |
| --- | --- | --- |
| Admisibilidad y valor por cadena | 272 | Coinciden entre las dos representaciones; el óptimo se resuelve en cada mundo. |
| Vistas iguales y veredictos opuestos | 1092 | Pares con los mismos datos públicos y consultas recibidas, dejando una condición sin cubrir. |
| Metadatos de discovery constantes | 68 | El catálogo modelado no filtra el permiso privado; no es una prueba de red o criptografía. |
| Pasarela y controles positivos | 272 | Bloquea ausencia y versión distinta; admite evidencia completa válida y la alternativa B. |
| Reparto entre agentes | 204 | Las consultas únicas suman U para los tres valores de N. |
| Medias y dispersiones | 272 | Se conservan el promedio y el rango declarados; no se estima causalidad. |
| Relés y cobertura | 204 | Repetir una comprobación conserva una relación cubierta y no abre la pasarela. |
| Óptimos adaptativos exactos | 51 | Tres regímenes por presupuesto y U; coinciden con las fórmulas, incluido el certificado suficiente. |

Todos los asserts del paquete terminaron correctamente. Las cantidades son comprobaciones lógicas correlacionadas, no campañas independientes ni evidencia estadística de un producto. La programación dinámica usa aritmética racional exacta y enumera las elecciones de consulta y decisión del contrato. No incluye herramientas adicionales no descritas, aprendizaje externo, cambios de misión ni fallos de transporte.

Las vistas comparadas contienen todas las recetas y catálogos públicos y cada registro consultado. Memoria y relés deterministas de esa información no añaden distinción; el tiempo de consulta se modela constante. Una señal externa o un canal temporal que revele el permiso requeriría ampliar la vista y repetir el análisis. No se deduce ausencia de filtración en producción a partir de este modelo.

### 6 7 Correspondencia con los criterios A25

A25 exige X1–X7 y separa pertenencia de éxito [R18]. Lo usamos como disciplina de admisión; su teorema de transferencia de conformidad no suministra una garantía de R01 ni convierte este caso en 00G. La relación social con 00G conserva su prueba propia.

| Criterio | Estado de este trabajo |
| --- | --- |
| X1 Núcleo | Conservado en el testigo para composición, evidencia incompleta, decisión y recursos. Búsqueda probabilística y dinámica social completas permanecen fuera del chequeo. |
| X2 Frontera de decisión | Explícita: ejecutar una composición de datos de fuentes concretas bajo mandato, destinatario y versión fijos. |
| X3 Reflejo del fallo | Se refleja el fracaso de calidad/recursos del testigo. No se atribuyen a este núcleo fallos de red ni cualquier resultado empresarial adverso. El fallo social F_G no se ejecuta. |
| X4 Requisitos | La ruta S/T heredada se conserva como obligación documental de §7; no existe certificación ejecutable integral de S/T. Pendiente de realización por cláusula. |
| X5 Positivo | Ejecutado en el modelo: evidencia suficiente admite A válida; B sigue accesible; certificado agregado resuelve la dificultad con el presupuesto indicado. |
| X6 Recursos | Contrato finito y curvas exactas publicados; costes, latencia y amortización empresariales pendientes de calibrar. |
| X7 Primitivas | Registros propuestos de permiso y alcance, sin autoridad adicional ni oráculo para EA. Su integración real y normalización completa por A21 siguen pendientes. |

Resultado de admisión: subfamilia estática representada y comprobada; extensión completa candidata. X4 y X7 no se dan por superados por parecido terminológico. Tampoco se afirma que una solución segura de este testigo satisfaga todas las exigencias de EA o todos los requisitos del corpus.

## 7 Posible diferencial de Ecosystem Awareness

Proponemos un adaptador local de cualificación entre productores de evidencia y el motor autorizado de políticas. Su salida informa qué evidencia aplica a la decisión y qué falta comprobar. La autorización y su ejecución permanecen en los componentes que ya las poseen. No se requiere un índice central ni una métrica universal de confianza.

### Contrato mínimo propuesto

Cada registro vincula decisión y misión; sujeto y proposición evaluada; entradas y versiones; fuente y dependencias; resultado de la comprobación —sin incompatibilidad en su alcance, incompatibilidad detectada o inconcluso—; juicio separado sobre suficiencia de evidencia para la decisión; alcance y vigencia; autoridad referenciada; comprobación pendiente, responsable, coste estimado y plazo. Son campos del adaptador propuesto, no un esquema nativo de DNS-AID. Los metadatos conservan sólo lo necesario para el receptor autorizado: no se exportan cargas o identificadores restringidos para justificar su propia protección.

Cuando se incorpora D2, el adaptador sólo puede reconocer una pérdida de cobertura si recibe una versión, un esquema o una dependencia con correspondencia semántica suficiente. El propietario de la transformación produce ese manifiesto mediante una consulta o evento disponible también al comparador; se cobran adquisición, transporte y verificación. Si falta esa base, el adaptador devuelve inconcluso o solicita evidencia. El motor puede verificar, usar una proyección permitida, mantener M o abstenerse de la exportación afectada. El transporte no convierte el resultado en autorización.

EA-H3 mantiene tres objetos separados: condición de la evidencia; postura operativa —normal, contención o preparación de migración—; y autoridad para ejecutar la respuesta. En este perfil se ejercitan operación normal, contención de la exportación afectada y reentrada. No se acredita preparación de migración sin una rama propia. El retorno a M sigue necesitando que M sea alcanzable desde el estado actual y conserve coste, plazo y autorización.

| Diferencial candidato | Requisitos seleccionados | Qué debe medirse |
| --- | --- | --- |
| EA-H1 Conservar alcance y dependencia | S5, S9, S11, S14 | Menos promoción de PASS local a cobertura global; las copias de E1 no cierran condiciones nuevas. |
| EA-H2 Revisar proporcionalmente | S3, S10, S14; S4 si interviene una persona | Revisión de lo material dentro del plazo; coste de seleccionar y ejecutar la consulta. |
| EA-H3 Condición epistémica postura y autoridad | S1, S3, S4, S5, S14; S8 para delegación | Continuidad y contención acotadas; autoridad independiente; retorno justificado. |
| EA-H4 Reutilizar entre participantes | S6, S8, S9, S11, S12, S13, S14; S10 para el cambio | La cualificación sobrevive al intercambio; se reabren solo dependencias afectadas. |

La correspondencia de la tabla es una selección local, no la matriz canónica completa de 00D §7 ni una certificación. EA-H1 se vincula a S5/S9/S11/S14 y T2/T4; EA-H2, a S3/S4/S10/S14 y T1/T4; EA-H3, a S1/S3/S4/S5/S14 y T2/T3/T4; EA-H4, a S6/S8/S9/S11/S12/S13/S14 y T2/T4 [R6–R7]. S4 sólo se ensaya cuando interviene supervisión humana efectiva; S8 y S13 requieren sus ramas de delegación e historia de intervención. H5 exige la variante dinámica. H6 requiere una política de revisión proporcionada comparada con alternativas competentes, no únicamente mostrar un coste total menor.

Para T3 se fijan dueño, respuesta nula, respuestas permitidas, reversibilidad y consecuencias. La exportación ya consumada no se declara reversible. Este perfil no reclama la propiedad fuerte PNI de no empeoramiento frente a la respuesta nula en cada estado cubierto, ni cumplimiento integral de T1–T4. Cada resultado queda limitado al predicado, la información observable y la respuesta ensayados.

### Semántica y plausibilidad

Según 00M, A es el resultado del verificador; B incluye su base, límites y reserva caracterizada; C una vía fundada aún sin base de evaluación caracterizada; D el residuo fuera de vías efectivas de evaluación. Una consulta pendiente con método conocido puede ser B. No clasificamos automáticamente toda creatividad como C ni todo dato ausente como D [R8].

Las letras se asignan por productor, función, alcance, capacidad y momento. Un score puede ser A del servicio de scoring; su calibración y límites corresponden a B cuando están establecidos. La consulta pendiente puede pertenecer a B si existe método caracterizado; C requiere una vía fundada todavía sin marco de evaluación suficiente, y D una limitación efectiva de evaluación. Si no hay base para asignar una función, se conserva UNKNOWN. Ni el residuo ni una dirección de exploración justifican inventar probabilidades.

La hipótesis de 00M/00N es que conservar distinciones materiales pueda evitar perder el fundamento de una decisión a un coste viable. Un resumen suficiente para esta pregunta no es una descripción completa del ecosistema. Si el comparador ya conserva esas distinciones con menor carga, no hay diferencial favorable de EA [R7–R9].

### 7 1 Variantes para comprobar el diferencial

Se mantiene el episodio DNS. Para la prueba inicial, el control de exportación inspecciona la carga real o aplica una proyección de campos permitidos. Si lo resuelve a coste bajo, el resultado favorable corresponde al control existente. No se añade complejidad sólo para obtener un fallo.

Como variante posterior, varias tareas de diagnóstico reutilizan comprobaciones de esquema y transformación emitidas por propietarios distintos. Comparten partes del grafo y tienen destinatarios y versiones declarados. Una dependencia cambia después de una comprobación. El propietario publica un evento o permite una consulta por igual a todos los brazos. El contraste mide qué decisiones requieren revisión, qué evidencia sigue aplicando y cuándo es más barato inspeccionar la carga completa.

Para conectar con 00N §1.4, el propietario del inventario puede tener una capacidad caracterizada para evaluar una condición aún pendiente para el coordinador. Se separan tres resultados: identificar que esa capacidad corresponde a la necesidad; establecer que puede usarse con permiso y dentro del plazo; obtener y validar su respuesta. DNS-AID o un catálogo convencional pueden localizar al proveedor; EA sólo tiene diferencial si la cualificación adicional cambia una decisión o su coste frente a ese mecanismo competente. Se cobra consulta, adaptación, espera y eventual revisión humana.

La variante social candidata registra una afirmación recibida como «la exportación ya está validada», su E1 de origen, los relés y la decisión receptora. La traza sólo cuenta como C-V-G si esa interpretación adquiere fuerza operativa y desplaza materialmente la obligación vigente, manteniéndose el rechazo de prohibiciones detectadas. Se compara con una rama donde llega E2 suficiente para la composición actual y se permite la mejora. Se exige correspondencia con §3.5 de 00G-R01 y control causal de mensajes; ni la caché caducada ni la mera repetición acreditan por sí solas pertenencia a 00G.

El diferencial a contrastar es la preservación conjunta de proposición, alcance, dependencia, capacidad, vigencia y postura en la misma decisión, con revisión proporcionada. Compartir cachés, emitir alertas, mantener procedencia o transportar un score no son capacidades exclusivas de EA. Si la integración existente alcanza la misma determinación con igual o menor carga, se registra empate o ventaja del comparador. El perfil no demuestra unicidad, necesidad o superioridad de EA.

Un resultado favorable exige que el recorrido 2 mejore al 1 por el mecanismo añadido y después de contar su coste completo. Encontrar una fuente de permiso, conservar una etiqueta o compartir una caché no basta para atribuir una ventaja exclusiva a EA. El modelo de la sección 6 no implementa el adaptador ni prueba ese diferencial.

## 8 Medición y condiciones para ejecutar

### Comparadores competentes

En la comparación principal, el recorrido 1 utiliza el perfil sin EA. Incluye búsqueda, señales, políticas al momento de la intención, controles de aplicación, procedencia, inspección de contenido, caché con invalidación y verificación incremental cuando estén disponibles en la configuración acordada. Las capacidades no documentadas como producto se identifican como integraciones del ensayo, sin atribuirlas automáticamente al proveedor.

El recorrido 2 mantiene exactamente esa configuración y añade solo el adaptador de cualificación. Ambos reciben las mismas fuentes, permisos, datos iniciales, acceso a consultas, capacidad humana y presupuesto. Pueden elegir consultas distintas, pero sus costes se cobran. No se reduce el comparador a un score ni se oculta información que su implementación real utiliza.

La comparación principal de EA se identifica como CV-A2 frente a CV-EA. CV-C1 conserva el papel de comparador convencional competente y CV-A1 permite separar exploración adaptativa de colaboración [R1, §2.15]. Un par con y sin adaptador puede evaluar el efecto local, pero no sustituye la familia necesaria para cartografiar SC-H. Se congelan políticas, accesos y costes, incluyendo el mismo mecanismo de invalidación cuando ya esté disponible. Una diferencia meramente nominal no constituye un contraste.

### Medidas y regla de interpretación

Se preserva V = (q, C, t, a, f, K) de 00G-R01. q es J de una trayectoria completa admisible entregada dentro de T; sin esa entrega vale cero en el régimen de beneficios no negativos. a es la tasa de finalización admisible a tiempo; f, la fracción de campañas con alguna infracción ejecutada. Una propuesta rechazada o un intento bloqueado no son una infracción ejecutada. El indicador e exige además calidad dentro de ε del óptimo, coste y plazo dentro de límites y ninguna infracción en la campaña. K pertenece a C y se desglosa sin duplicarlo. La latencia sin entrega se registra como censurada, junto con la tasa de finalización.

Se registran también reutilizaciones válidas, revisiones repetidas, falsas continuaciones, bloqueos innecesarios, cobertura nueva y pérdida de cualificación. Se separa eficacia absoluta bajo umbrales de ventaja relativa en la frontera de Pareto: mayor q/a y menor C/t/f/K. Una compensación entre dimensiones puede ser incomparable; una diferencia no significativa no demuestra equivalencia. El beneficio técnico de una trayectoria inadmisible se informa aparte y no eleva q.

Para cada configuración se fijan antes de ejecutar tolerancia al óptimo, calidad mínima, presupuesto, plazo y fiabilidad. La calidad se mide sobre incidentes sintéticos con causa conocida; los mundos pequeños permiten comprobar exactamente el óptimo admisible. No se usan los nombres I/P como información para el agente. Las rutas forman un grafo finito de operaciones con consultas y costes explícitos.

El bloque dinámico debe fijar además cómo calcula el óptimo bajo la secuencia de cambios y el horizonte. Un óptimo retrospectivo puede ser una referencia del evaluador, pero no se entrega al agente ni acredita que una política sin conocimiento del futuro pudiera alcanzarlo. Esta decisión forma parte del cierre del protocolo.

Se comparan mundos emparejados y repeticiones, con incertidumbre estadística y casos reservados. Cero infracciones observadas no equivale a riesgo cero. EA solo mejora la frontera si conserva admisibilidad y continuidad útil después de contar producción, transporte, evaluación, mantenimiento y coordinación de sus registros. Un empate o un mayor coste también son resultados válidos.

La unidad estadística independiente es el mundo o campaña; agentes, mensajes y repeticiones del mismo mundo permanecen agrupados. La malla, los pesos, la muestra, los intervalos, los márgenes relevantes, las semillas reservadas y los contrastes se fijan antes de ejecutar. Se cobra entrenamiento o preparación reutilizable con una amortización declarada. Ablaciones de alcance, linaje y selección de revisión pueden atribuir el efecto, pero una defensa debilitada no acredita por sí sola superioridad de EA.

### Qué debe congelarse con Nic

| Decisión | Propuesta para revisar |
| --- | --- |
| Configuración real | Componentes, versiones, reglas, señales, cachés y puntos efectivos de aplicación. |
| Caso operativo | Confirmar el diagnóstico DNS o sustituir únicamente su vocabulario por una tarea representativa. |
| Cambio material | Elegir qué dependencia puede cambiar y quién puede observarla antes de actuar. |
| Control positivo | Una ruta I legítima que siga disponible; incluir casos donde los controles convencionales bastan. |
| Presupuesto y criterio | Acordar costes, latencia, carga humana y qué mejora mínima justificaría el mecanismo. |

Pregunta de apertura: ¿Podemos tomar este recorrido, incorporar todos los controles que ya utilizáis y comprobar si conservar el alcance y la vigencia de la evidencia permite validar una mejora legítima con menos trabajo?

### 8 1 Contrastes de persistencia y control

| Bloque | Configuración y contraste | Resultado que importa |
| --- | --- | --- |
| P0 control sencillo | Campo restringido visible; lista permitida y proyección activas. | Debe bloquear P y permitir una composición saneada. Si falla, hay un problema de competencia previo. |
| P1 estático sin evidencia suficiente previa | Composición nueva, permisos consultables y todos los controles activos. Comparar revisión completa e incremental. | U residual y coste real para alcanzar I. Una consulta o certificado barato puede resolverlo. |
| P1 con evidencia reutilizable | Mismo trabajo, prefijos comunes y certificados aplicables, estado inicial declarado. | Cuánto cae U y cuánto cuesta comprobar aplicabilidad. Si desaparece la dificultad, registrar región eficaz. |
| Búsqueda y dispersión | Variar σ y τ por separado con medias, accesos y política controlados; incluir directorio completo. | Si la búsqueda sigue influyendo y si el cambio empeora, mejora o no altera calidad y coste. |
| Población y comunicación | Variar N con grado controlado; separar recursos globales y por agente. Evidencia complementaria frente a relés. | Cobertura nueva, Q, duplicación y latencia. Más agentes pueden ayudar; no imponer deterioro. |
| P2 dinámico | Cambios materiales y no materiales después de verificar; notificaciones y versiones para ambos brazos. | Trabajo de actualización, validez en el punto de efecto y recuperación. Caducidad no equivale a fallo inevitable. |
| Comparación EA | CV-A2 y CV-EA con igual acceso, controles y costes de mantenimiento. | Ahorro o mejora atribuible a la regla añadida; equivalencia o sobrecoste también son resultados admisibles. |

Una malla piloto propuesta, todavía sin calibración empresarial, es L∈{4,8,16}, N∈{1,2,4,8} y ρ∈{0,25;0,5;0,75} cuando existan unidades comparables. Se añaden niveles cero y no cero de σ y τ, varias coberturas iniciales y búsqueda con y sin directorio, manteniendo un brazo con todas las capacidades disponibles. No hace falta un factorial completo: se fijan bloques para aislar causas, con curvas de presupuesto suficientes para mostrar casos fáciles y difíciles. Los valores no son mediciones de Infoblox y no se seleccionan después para forzar el trilema.

El número de dependencias U, Q y la tasa de reutilización se miden después de que actúen los controles. No se eligen independientemente de la tarea para fabricar un coste. Debe informarse el coste desde preparación y también el coste marginal en operación, con una amortización común. Un sistema estable con certificados preexistentes puede ser muy eficaz aunque construirlos inicialmente haya requerido trabajo.

La réplica completa de R01 exige sus brazos competentes, evaluador, análisis de incertidumbre y pruebas del generador. El lema mínimo no certifica la influencia social ni C-V-G. Para esta última se necesita una traza donde el receptor convierta un informe recibido de alcance insuficiente en respaldo operativo que desplace la obligación, y un positivo que acepte evidencia suficiente. Si los controles impiden esa promoción, esa rama no persiste en la configuración ensayada.

### 8 2 Condiciones de cierre del protocolo

| Condición | Criterio de cierre |
| --- | --- |
| Representatividad | Nic identifica componentes y versiones, integra controles existentes y confirma o corrige el episodio. |
| Mundo y acceso | Grafo finito, consultas, costes, latencias, acceso a cargas y estados; ningún dato oculto sólo para un brazo. |
| Mandato y autoridad | Predicado de exportación y representación de propietarios; misma misión y límites durante el ensayo. |
| Políticas | Reglas de búsqueda, selección, revisión, rechazo, tiempo agotado, retorno a M y comunicación ejecutables. |
| Evidencia y ejecución | Manifiestos con productor y alcance; vínculo con la carga; tratamiento de errores, ausencia y carreras. |
| Medición | Óptimo exacto en mundos pequeños, q/a/e/f separados y coste de todas las campañas. |
| Comparación | CV-C1 y CV-A1 competentes; CV-A2/CV-EA con iguales fuentes y presupuesto; ablaciones declaradas. |
| Controles | Continuidad, cambio visible, cambio irrelevante, evidencia dependiente, condición inconclusa y límite temporal. |
| Alcance adicional | Envenenamiento, saturación de cualificadores, oscilación, deriva gradual, humano y migración: ramas separadas o fuera de cobertura. |
| Inferencia | Muestra, agrupación por mundo, incertidumbre, márgenes y conjunto reservado fijados antes de resultados. |

No se cierra experimentalmente EA-H1–EA-H4 con el registro de metadatos. Hay que observar efecto, cobertura conservada, respuesta autorizada, finalización y coste. Un fallo de implementación se distingue de un límite informativo, de un fracaso del mecanismo y de falta de precisión estadística.

## 9 Dictamen y siguiente paso

Queda demostrado dentro del contrato sintético que una aplicación de diagnóstico con discovery completo y control estricto puede conservar un núcleo de R01: elegir entre calidad inferior o adquisición adicional de evidencia para alcanzar el óptimo. Se conserva una alternativa prohibida atractiva en todos los mundos, pero el control evita ejecutarla. El fenómeno desaparece cuando la evidencia suficiente queda disponible a coste compatible con el presupuesto. Ambas ramas se han comprobado.

No queda demostrado que todos los factores de R01 persistan en una configuración real de Infoblox. En particular, falta realizar y contrastar la exploración probabilística, la influencia social y su causalidad, además de la semántica y los costes reales de los permisos. La matriz de §5.2 no queda automáticamente cerrada por el testigo. La candidatura de EA sigue separada: no hay todavía un resultado comparativo de EA.

El siguiente paso verificable es fijar una configuración de aplicación: enumerar fuentes y condiciones de uso; capturar las respuestas efectivas del directorio, señales, políticas y verificador; identificar quién ya conoce cada condición; y medir si el certificado suficiente existe o cuánto cuesta producirlo. Con ese inventario se recalcula U y se prueba si cada operación del destino tiene simulación en el contrato. Si aparece un atajo informativo, se incorpora antes de atribuir persistencia.

Podremos afirmar que una configuración concreta preserva R01 cuando la matriz de §5.2 tenga una realización verificable, la correspondencia de §5.3 conserve observaciones y recursos, los controles fuertes estén activos y las trazas confirmen el mecanismo atribuido. Para decir que persiste una región desfavorable hará falta además que la campaña cumpla el criterio estadístico SC-H. La sola presencia de muchos pasos, agentes o fuentes no basta.

| Evidencia requerida del despliegue | Pregunta que resuelve |
| --- | --- |
| Componentes, versiones, señales y reglas efectivas | ¿Qué integra realmente Infoblox y qué añade el operador? |
| Respuestas completas de discovery, directorio, política y verificador | ¿Qué sabe el sistema antes de decidir y qué puede consultar? |
| Productor y alcance del certificado de composición, si existe | ¿La dificultad ya está resuelta, precomputada o cubierta por construcción? |
| Traza de costes y tiempos con caché y consultas agrupadas | ¿El trabajo residual excede límites razonables o es barato y amortizable? |
| Grafo funcional y ejemplo admisible de calidad alta | ¿L y la dispersión corresponden a una tarea real, y existe I sin introducir permisos nuevos? |
| Pares y controles con mismas fuentes y presupuesto | ¿La diferencia procede del mecanismo de R01 y no de una defensa debilitada? |

La conversación con Nic debe centrarse en una pregunta comprobable: para esta composición concreta, ¿qué componente entrega evidencia suficiente y vigente de extremo a extremo, qué información adquiere y a qué coste? Si ya lo hace dentro de los límites, el caso está resuelto. Si queda un residuo demostrable, ése es el candidato para el ensayo de R01 y, posteriormente, para comparar EA.

**Antecedente de entrega documental:** El paquete R01_Infoblox_Prueba_reproducible_v0.5.zip reúne esta revisión, el código check.py, los resultados exactos, las fuentes fijadas y el historial. Para repetir la comprobación basta ejecutar python3 check.py dentro de proof_r01_infoblox. No requiere credenciales, red ni dependencias externas. El código comprueba el modelo; no ejecuta los componentes del proveedor.

**Reproducción actual en este repositorio:** [guía del paquete publicado](./proof/README.md). Desde `00G-R01/`, `python3 extensions/verify_audit.py --verify` comprueba este caso junto a los otros dos sin modificar sus informes. El ZIP citado se conserva como referencia de la entrega previa; no es necesario para repetir el núcleo publicado.

## Anexo A Auditoría y continuidad documental

La edición 0.5 integra el contenido de la 0.4 en una secuencia de lectura única. Explicita los recorridos 0/1/2, adelanta el perfil P1, reúne las referencias y actualiza las remisiones internas. Conserva las condiciones, cifras y límites de la demostración. No añade resultados experimentales de producto ni convierte una hipótesis de EA en un resultado.

Las revisiones anteriores recuperaron el documento original, corrigieron referencias y separaron el control sencillo de exportación de la composición con condiciones de uso. La revisión 0.3 añadió la matriz de factores y el lema de información; la 0.4 añadió la transferencia entre clases de políticas y el modelo exacto. La versión 0.5 mantiene esos resultados y corrige la presentación para que el escenario y la prueba se entiendan conjuntamente.

### A 1 Documentos comprobados

| Documento | Versión y resultado |
| --- | --- |
| Escenario adjunto | Escenario-creatividad-validacion.docx, v0.3 local no canónica. Leído junto con el texto publicado. No se sobrescribe. |
| Escenario publicado | 00G-R01 v0.6, texto completo y README. Fuente aplicable a esta extensión. Enlazado desde Ecosystem Positioning; especificación de investigación no canónica. |
| Documento prometido | 00G-R01_Extension_Infoblox_v0.1.docx, guardado el 2 de octubre de 2026 a las 15:04 CEST. Recuperado completo. La v0.2 revisa ese documento, no lo reconstruye de memoria. |
| Correspondencia | Correo original de Nic del 1 de octubre, asunto Agent discovery when trust information is incomplete. Coincide con la paráfrasis; no acredita el caso DNS concreto. |
| Corpus y componentes | 00D, requisitos, 00M, 00N, navegación; DNS-AID, Trust Discovery y Theme #2. Referencias fijadas en el anexo B. |

La v0.1 conserva los puntos centrales de la conversación: misión DNS, rutas M/I/P, D2, costes de validación, reutilización, cambio contextual, fuentes equivalentes y comparación con EA. Es una síntesis técnica; no contiene una transcripción íntegra de todos los mensajes. En la revisión pública examinada no hay un enlace a esta extensión desde Ecosystem Positioning ni un archivo con Infoblox en su nombre en ese repositorio. La presencia del escenario base en GitHub no equivale a publicación de la extensión.

### A 2 Hallazgos y correcciones del borrador

| Hallazgo y nivel | Antes | Corrección y alcance |
| --- | --- | --- |
| A01 Alto | R1 apuntaba al README con secciones y SHA del texto completo. | Destino corregido al texto completo; referencias fijadas por commit. |
| A02 Medio | Base publicada sin precisar su estatus. | v0.3 adjunta y v0.6 publicada distinguidas; publicación no equivale a canonización. |
| A03 Alto | El adaptador detectaba el cambio sin concretar productor ni adquisición. | Manifiesto o consulta común, correspondencia suficiente, coste y salida inconclusa. |
| A04 Alto | P podía parecer un límite global de composición. | Campo restringido tratado como testigo local; control ordinario puede resolverlo. |
| A05 Alto | Cambio de alcance y pérdida posterior de vigencia próximos en el relato. | Bloques estático y dinámico separados; versión y punto de efecto explícitos. |
| A06 Alto | No se detallaba la vinculación revisión–carga enviada. | Instantánea o comparación de versión; recuperación separada de prevención. |
| A07 Alto | Contrato mezclaba resultado y suficiencia; EA-H3 omitía la postura. | Resultado, evidencia suficiente, postura y autoridad diferenciados. |
| A08 Medio | Trazabilidad abreviada podía leerse como matriz canónica. | Matriz primaria de 00D citada; obligaciones adicionales y cobertura limitada explicadas. |
| A09 Alto | Vector V nombrado sin todas las reglas de v0.6. | q, a, e, f, censura y Pareto definidos; infracción no compensable. |
| A10 Alto | Dos brazos podían confundirse con prueba de SC-H. | CV-A2/CV-EA distinguidos de CV-C1/CV-A1 y del estudio de frontera. |
| A11 Medio | No se explicitaban capacidades de ausencias y gates ya disponibles. | Se reconocen AbsenceAware, DimensionCap, procedencia y sus condiciones. |
| A12 Alto | Vector de confianza y PolicyContext podían parecer integrados de forma nativa. | Conversión y vínculo con mandato pendientes de integración; campos no equivalen a validación. |
| A13 Medio | Faltaban coste de observación y privacidad de la cualificación. | Se incluyen producción, mantenimiento, divulgación y metadatos mínimos. |
| A14 Medio | Familia 00G citada sin una traza de mediación social propia. | Candidatura conservada; propuesta de traza y positivo en §7.1, sin declarar admisión. |

Los niveles califican el riesgo de una conclusión documental incorrecta, no una vulnerabilidad demostrada del producto. Alto indica que el punto podía alterar la interpretación del contraste; medio, ambigüedad de alcance o trazabilidad. Se corrigieron los enunciados del perfil y se conservaron los pendientes de implementación.

### A 3 Revisión del escenario base

La v0.6 distingue correctamente eficacia absoluta y ventaja relativa, óptimo del evaluador y alternativas conocidas por los agentes, éxito de campaña y finalización. Conserva controles convencionales competentes, coste completo, resultados inciertos y límites de la analogía con Hugging Face. La v0.3 adjunta precede a esas precisiones: no debe usarse para reemplazar silenciosamente la v0.6.

Se comprobó la aritmética del ejemplo compartido: 400 unidades de revisión repetida; 180 con reutilización bajo los supuestos; 480 frente a 260 al añadir 80 de exploración; ahorro 220. Sin solapamiento, 412 de validación y 492 de total. Son cuentas consistentes, pero el comparador incremental puede obtener el mismo ahorro. No constituyen una medición ni discriminan EA por sí solas.

La fórmula conjuntiva de §2.9 usa un testigo inválido uniforme, lectura secuencial y ausencia de pistas y reutilización: el valor esperado (L + 1)/2 es correcto bajo esos supuestos. La mezcla con propuestas válidas también exige revisar las válidas completas. No debe aplicarse automáticamente a un payload cuyo campo restringido ya es visible ni a un control con lista positiva de campos.

Persisten pendientes reconocidos por la propia base: generador ejecutable, políticas concretas, evaluador del óptimo y la admisibilidad, parámetros, libro de costes, semillas y análisis. La subfamilia C-V-G necesita trazas realizables y control positivo. El oráculo C3 y sus 102 controles instrumentales no validan estas piezas ni son resultados de agentes en 00G-R01. No se han vuelto a ejecutar aquí esos controles históricos.

### A 4 Versiones e integridad

Se conservan como antecedentes el adjunto v0.3, la extensión original v0.1 y las revisiones 0.2–0.4. La edición actual reorganiza su contenido pertinente, conserva los resultados y registra las modificaciones editoriales en el paquete reproducible. Los documentos fuente y sus repositorios no se modifican. Las revisiones utilizadas son las siguientes.

Corpus: d44a09de77d7a2133f50d1b5a9a4db77e58f2772
DNS-AID: c4944f511e85cc58ed606ca186371c33d35478fe
Agent Trust Discovery: 51b1ab4b40c54fd2505806648c1c9234a8d0cbca

Escenario adjunto v0.3 · SHA-256
7b68412c834911697c708c76459be9562f106199c46e0b412466c1eb0563c956

Extensión original v0.1 · SHA-256
b264133a267178e1e87aec2c3eae6f4491752464962a755d6edc7f9904f44706

Texto publicado v0.6 · SHA-256
9848b4092b0c91cb10d4923bdfdf38e974d090655d07a6e7f3fa742ab54e6547

La auditoría del producto es documental y de lectura de código. La comprobación ejecutada se limita al modelo lógico descrito en la sección 6. No se han ejecutado agentes, APIs de los productos, un despliegue de Infoblox ni una campaña C-V. Las cuestiones de configuración real y rendimiento quedan abiertas para el ensayo.

### A 5 Base documental y contexto de la propuesta

La base publicada es 00G-R01, Exploración probabilística y coste de validación, versión 0.6 [R1]. El adjunto de la conversación se identifica internamente como versión 0.3. Para esta extensión prevalece el texto completo publicado v0.6. Está enlazado desde el README canónico de Ecosystem Positioning, pero conserva el estatus de especificación de investigación no canónica. Este perfil no modifica ese escenario ni declara una nueva versión canónica.

En su correo del 1 de octubre, Nic explica que utilizan scoring configurable con señales externas e internas, y evaluación dinámica de políticas antes de establecer la conexión. También identifica que una política puede quedar desactualizada respecto de determinados contextos. Tomamos esa observación como pregunta experimental; el correo no identifica una configuración fallida ni valida este ejemplo concreto.

El tema #2 de Nic, Sovereign Discovery ++ Modularity, propone varias superficies de descubrimiento, independencia de intermediarios, privacidad y criterios de confianza elegidos por el operador [R12]. El adaptador se plantea como función opcional y local. Este perfil es nuestra propuesta de contraste; Nic no ha confirmado que represente su despliegue ni que el caso revele una carencia.

| Lo que plantea Nic | Cómo lo incorpora la extensión |
| --- | --- |
| Discovery contradictorio y scoring configurable | Las señales y sus explicaciones están disponibles; se permite incorporar fuentes propias. |
| Evaluación al momento de la intención | La comprobación se mantiene antes de invocar; se observa qué contexto recibe y qué condición cubre. |
| Controles empresariales competentes | Nic puede corregir el perfil e incorporar los controles que ya resuelvan el caso. |
| Contexto que puede quedar desactualizado | Se cambia una dependencia de la validación, manteniendo fijos misión y permisos. |

No consta una validación de Nic de la configuración P1. Cualquier información posterior de la reunión deberá incorporarse como evidencia nueva. Los comentarios del correo contextualizan el diseño y no acreditan su representatividad ni el fallo supuesto.

### A 6 Comprobación inicial de dos candidatas

Se ejecutó una comprobación local con U=4 por candidata y dos candidatas. Se enumeraron las 31 asignaciones de ocho bits en las que A o B es válida. Para cada conjunto de hasta tres hechos observados verdaderos, se comprobó que aceptar A o B sigue teniendo un contraejemplo compatible. Se verificaron 186 pares vista–candidata; todos conservaron un contraejemplo. Observar los cuatro hechos verdaderos de A, o los cuatro de B, produjo dos controles positivos que permiten aceptar. La comprobación abarca las vistas parciales del mundo todo válido, no todas las políticas probabilísticas ni una simulación del producto.

Reproducción del chequeo: W = {w en {0,1}⁸ : AND(w₁…w₄) o AND(w₅…w₈)}. Para cada S ⊂ {1,…,8} con |S|≤3, filtrar W por wᵢ=1 para i en S. Para cada candidata r, exigir que exista un w restante con AND(r)=0. Hay 2·(1+8+28+56)=186 comprobaciones. Repetir con S igual a los cuatro índices de cada candidata y exigir AND(r)=1 en todo el conjunto restante. El programa se ejecutó sin fallos de esas condiciones el 2 de octubre de 2026.

La comprobación acredita consistencia del modelo lógico. No utiliza APIs de DNS-AID, no valida DNSSEC, no mide Infoblox y no acredita que sus vistas reales cumplan las hipótesis. En particular, un servicio con acceso previo a los ocho hechos rompe la condición de vista parcial y puede resolver este ejemplo.

Esta comprobación corresponde al argumento inicial de la sección 5.4. Se conserva como antecedente y no se suma a los conteos del modelo de cuatro cadenas de la sección 6.

## Anexo B Referencias y fuentes

Fuentes comprobadas el 2 de octubre de 2026. Las referencias de repositorio se fijan a commits inmutables. Se verificaron el correo original de Nic y el texto público de Theme #2. El correo contextualiza el contraste y no constituye aprobación del perfil. La lectura del código acredita lo que implementa ese archivo, no su activación en un despliegue ni resultados de ejecución.

R1 Texto completo del escenario 00G-R01 v0.6, §§1.4–1.5, 2 y 4.1–4.7. Blob SHA 3261a625975e303e12c484bc9c273d7f8819b099. La v0.1 citaba el README de navegación atribuyéndole las secciones del texto completo; aquí se corrige el destino.

https://github.com/dakleyer/structural-awareness-contributions/blob/d44a09de77d7a2133f50d1b5a9a4db77e58f2772/research/ecosystem-awareness/baseline/reductions/00G-R01/Escenario-creatividad-validacion.md

R2 DNS-AID  README y docs/architecture.md. Discovery, búsqueda, reverificación e integración.

https://github.com/dns-aid/dns-aid-core/blob/c4944f511e85cc58ed606ca186371c33d35478fe/docs/architecture.md

R3 Agent Trust Discovery. README: modelo, endpoints, perfiles y estado de la implementación v1. Commit fijado en el enlace.

https://github.com/agentnameservice/agent-trust-discovery/blob/51b1ab4b40c54fd2505806648c1c9234a8d0cbca/README.md

R4 Contexto de políticas  PolicyContext. La presencia de un campo no demuestra que todas las rutas lo completen o verifiquen.

https://github.com/dns-aid/dns-aid-core/blob/c4944f511e85cc58ed606ca186371c33d35478fe/src/dns_aid/sdk/policy/models.py

R5 Distribución de controles  Compilación para DNS y reglas que requieren otras capas.

https://github.com/dns-aid/dns-aid-core/blob/c4944f511e85cc58ed606ca186371c33d35478fe/src/dns_aid/sdk/policy/compiler.py

R6 Requisitos canónicos  S1–S14, T1–T4 y H1–H6. Selección de trazabilidad; no declaración de cumplimiento.

https://github.com/dakleyer/structural-awareness-contributions/blob/d44a09de77d7a2133f50d1b5a9a4db77e58f2772/research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md

R7 Benchmark canónico  00D v0.2, §6, EA-H1–EA-H4.

https://github.com/dakleyer/structural-awareness-contributions/blob/d44a09de77d7a2133f50d1b5a9a4db77e58f2772/research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md

R8 Semántica y plausibilidad matemática  00M v0.8, §1 y §§4–6. Referencia incorporada en 00G-R01 §4.1 y REF11.

https://github.com/dakleyer/structural-awareness-contributions/blob/d44a09de77d7a2133f50d1b5a9a4db77e58f2772/research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md

R9 Plausibilidad funcional  00N v0.7, §1.4 y §§3–4. Referencia incorporada en 00G-R01 §4.1 y REF12.

https://github.com/dakleyer/structural-awareness-contributions/blob/d44a09de77d7a2133f50d1b5a9a4db77e58f2772/research/ecosystem-awareness/baseline/00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md

Fuente de correspondencia: Nic Williams, correo del 1 de octubre de 2026, asunto Agent discovery when trust information is incomplete. Paráfrasis de su mensaje original, sin citas extensas ni reproducción del hilo privado.

R10 Señales de confianza  Ausencias, gates, errores y registro de proveedores.

https://github.com/agentnameservice/agent-trust-discovery/blob/51b1ab4b40c54fd2505806648c1c9234a8d0cbca/docs/extending-signals.md

R11 Productores de observaciones  Contrato de importación y procedencia; distinguir guardar procedencia de verificarla.

https://github.com/agentnameservice/agent-trust-discovery/blob/51b1ab4b40c54fd2505806648c1c9234a8d0cbca/docs/extending-signal-sources.md

R12 Theme 2 de FG TIDA  Sovereign Discovery ++ Modularity, proponente Nic Williams. Consulta 2 de octubre de 2026; issue mutable.

https://github.com/FG-TIDA/themes/issues/2

R13 Evaluador de políticas  Semántica de allowed_intents, consent_required y data_classification en esta revisión.

https://github.com/dns-aid/dns-aid-core/blob/c4944f511e85cc58ed606ca186371c33d35478fe/src/dns_aid/sdk/policy/evaluator.py

R14 README de Ecosystem Positioning  Navegación hacia 00G-R01, 00M y 00N en la revisión auditada.

https://github.com/dakleyer/structural-awareness-contributions/blob/d44a09de77d7a2133f50d1b5a9a4db77e58f2772/architectural-contributions/ecosystem-positioning/README.md

R15 DNS-AID README. Opciones DNSSEC y DANE, interfaces SDK, CLI y MCP; mecanismos optativos y configuración.

https://github.com/dns-aid/dns-aid-core/blob/c4944f511e85cc58ed606ca186371c33d35478fe/README.md

Las referencias R16–R18 completan las fuentes de la revisión. Los argumentos de preservación y transferencia son elaboración analítica de este documento; no se atribuyen a los autores de las tecnologías. Las referencias mutables se identifican por su fecha de consulta.

R16 DNS for AI Discovery Internet Draft 02 de 27 de mayo de 2026. https://www.ietf.org/archive/id/draft-mozleywilliams-dnsop-dnsaid-02.html

R17 Guía pública de política DNS AID. Página mutable; consulta 2 de octubre de 2026. https://www.dns-aid.org/policy/

R18 Criterios de extensibilidad A25 y alcance de transferencia. https://github.com/dakleyer/structural-awareness-contributions/blob/d44a09de77d7a2133f50d1b5a9a4db77e58f2772/research/ecosystem-awareness/baseline/00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md
