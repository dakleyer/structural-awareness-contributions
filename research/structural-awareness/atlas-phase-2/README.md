# Perspective Beyond / Atlas — Procedimiento fase 2

**Estado:** procedimiento experimental de referencia, **v0.2** · 4 de noviembre de 2026. El cuerpo v0.1 se preserva como linaje; en caso de discrepancia rige el procedimiento v0.2 enlazado abajo.  
**Alcance:** arquitectura informacional y prueba de recorrido; **no** revisión del corpus canónico, norma ni demostración científica.  
**Ámbito:** Atlas de pensamiento, con un grafo conceptual común y lecturas dependientes del posicionamiento.  
**Compatibilidad:** las definiciones A/B/C/D son las de [00M v0.8 §1](../../ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical). La expresión *distancia epistemológica* ya se desarrolla, sin presuponer una métrica escalar, en [Map, Flow, Epistemic Distance — working programme bridge](../MAP_FLOW_EPISTEMIC_DISTANCE_PROGRAMME_BRIDGE_v0.1_DRAFT.md). Este experimento **no reemplaza ni modifica** esos documentos.

> **Lectura operativa vigente v0.2:** [Procedimiento integral de etiquetas, ítems, nodos y recorridos](./PROCEDIMIENTO_LENGUAJE_Y_RECORRIDOS_v0.2.md) · [Diccionario taxonómico reutilizable y traducible (JSON)](./TAG_DICTIONARY_v0.1.json) · [Ejemplo v0.2](./examples/language-v02-pilot.json) · [Validador v0.2](./scripts/validate-language-v02.mjs). Leer el diccionario **antes** de extraer fichas. El protocolo es referencia sólo para esta rama experimental Atlas; **no** altera el baseline controlado EA/MSCA.

## 1. Decisión de arquitectura

Construir en dos pasos distintos:

1. **Mapa relacional libre:** registrar ítems, nodos y vínculos conceptuales respaldados o propuestos, sin imponer A/B/C/D a cada arista.
2. **Lectura de distancia epistemológica:** desde **cada nodo de origen y una finalidad declarada**, seguir hilos completos del mapa, calificando cada nuevo tramo con respecto al recorrido acumulado. **D detiene ese hilo**, aunque las demás ramas continúan.

Después de caracterizar esos recorridos, identificar los **clústeres conceptuales principales** y finalmente los **temas**. Las fichas de **ítem, nodo y tema** conservan texto libre autosuficiente dentro de JSON con **etiquetas** del mismo diccionario compartible, flexible y versionado. Los temas se describen **después** de los clústeres, no al empezar a construir las rutas.

No introducir ahora más niveles jerárquicos ni etiquetas **MSCA obligatorias** o una ontología rígida. **Sí se incorpora Jumps & Falls JF.F1–JF.F4 como segunda calificación funcional del recorrido, después de ABCD**, sólo cuando corresponda a la actividad. `JF.F4` es efecto colateral transversal y **no** equivale a `D`. La web y el Atlas existentes siguen funcionando mientras esta rama se estudia aparte.

## 2. Modelo de datos mínimo

**Revisión v0.2:** el lenguaje canónico de descripción se denomina **etiquetas**. Hay claves reservadas (`trace:hook`, `core:description`, `trace:item_refs`, etc.) y etiquetas flexibles en `/etiquetas`. El [diccionario](./TAG_DICTIONARY_v0.1.json) registra definición, sinónimos, traducciones y ámbitos; los bots reutilizan claves y sólo proponen nuevas cuando las existentes no alcanzan. No se infiere una relación conceptual por compartir una etiqueta.

| Objeto | Qué representa | Regla vigente |
|---|---|---|
| **Ítem** | Persona, entidad, software, documento, página, sección, párrafo, fragmento, artefacto o caso identificable del mundo o de una fuente. | Debe tener una referencia/hook verificable y versión o estado observado. Puede relacionarse con otros ítems. |
| **Nodo** | Ficha de pensamiento que organiza, explica o interpreta uno o varios ítems y puede formar parte de muchas perspectivas. | Identidad persistente; descripción libre y referencias explícitas a ítems; no es idéntico al objeto externo. |
| **Relación conceptual** | Asociación de nodo con nodo por cualquier vínculo justificable. | Registrar dirección, por qué se asocian y evidencia/candidatura. **No** hereda una calificación A/B/C/D global. |
| **Recorrido** | Secuencia ordenada de relaciones desde un nodo y una cuestión/actividad concreta. | La evaluación de un tramo depende de **todo el prefijo** recorrido, no sólo de sus extremos. |
| **Clúster conceptual principal** | Conjunto que adquiere amplitud funcional por el alcance de A desde un posicionamiento. | Se descubre **después** de calificar recorridos, no por una taxonomía previa ni sólo por grado bruto. |
| **Tema** | Eje humano comprensible para leer y comunicar varios nodos/clústeres. | Se elige **después** de los clústeres; debe diferenciarse de los demás, cubrir el discurso y tener descripción libre. |

Un ítem no es automáticamente una prueba de una afirmación. La relación ítem–nodo conserva el tipo de apoyo: descripción, evidencia primaria, testimonio, hipótesis, refutación, analogía, etc. Un identificador externo de persona o empresa se maneja respetando confidencialidad y acceso; no exige publicar un documento de identidad.

### 2.1 Hooks: los ítems anclan y permiten reevaluar

**Ampliación v0.2:** todo ítem tiene ficha semiestructurada JSON, también su propia `description`, `version`, `evidence_status` y `etiquetas`; su `hook` es el campo estructural reservado correspondiente a la etiqueta `trace:hook`. La ausencia de hook deja un **candidato pendiente de anclaje**, no una prueba. Véase [procedimiento §2](./PROCEDIMIENTO_LENGUAJE_Y_RECORRIDOS_v0.2.md#2-fase-0--crear-fichas-semiestructuradas-de-ítem-y-nodo).

Un hook no es una palabra clave decorativa. Debe permitir volver al **mismo objeto y a su estado**: URL estable más fragmento, ID externo, ruta y versión de repositorio, JSON Pointer, página y párrafo, revisión y hash de contenido, registro fechado o equivalente. Si la ubicación cambia, mantener un alias/mecanismo de resolución. Si una fuente no es accesible, registrar esa limitación: un enlace roto **no** se convierte en evidencia.

Registro mínimo sugerido:

```json
{
  "item_id": "ITEM-NESTLE-CASE-001",
  "kind": "web_article",
  "hook": {
    "uri": "https://jubap.eu/nestle-case-study-where-jubap-was-first-named/",
    "locator": "sección sobre Kotter y el dashboard",
    "source_revision": "captura/versionado pendiente de fijar",
    "content_hash": null
  },
  "observed_at": "2026-11-04",
  "access": "public",
  "notes": "Relato de campo; no validación causal independiente"
}
```

En producción, los campos de revisión/hash se completan por la ingesta. Un ítem de una fuente cambiante debe mantener revisiones o capturas comparables. No inventar hashes ni fechas de publicación.

### 2.2 Fichas de nodo y, posteriormente, tema: JSON semiestructurado

Se adopta **texto libre autosuficiente dentro de JSON, con `etiquetas` flexibles**, no MSCA obligatorio. Este ejemplo simplificado v0.1 se conserva como mínimo legible; la versión operativa completa, con referencias y etiquetas tipadas, está en el [ejemplo v0.2](./examples/language-v02-pilot.json):

```json
{
  "node_id": "NODE-JUBAP-FRAMEWORK",
  "label": "JUBAP · Framework",
  "description": "Texto libre autosuficiente: qué es, cómo se utiliza, límites y matices.",
  "item_refs": [
    {"item_id": "ITEM-NESTLE-CASE-001", "role": "historical_use"}
  ],
  "version": "draft-0.1",
  "epistemic_status": "described_not_independently_validated"
}
```

```json
{
  "theme_id": "THEME-TRANSFORMATION",
  "title": "Transformación",
  "description": "Texto libre que delimita qué preguntas y contenidos se leen bajo este tema.",
  "primary_node_ids": ["NODE-JUBAP-FRAMEWORK"],
  "secondary_node_ids": [],
  "version": "draft-0.1"
}
```

El nodo no necesita forzarse hoy a un número fijo de páginas ni a una estructura de MSCA. **La ficha de tema se elabora tras los clústeres** y reutiliza **el mismo diccionario de etiquetas**; tampoco necesita tres páginas. MSCA queda como **vista analítica opcional pendiente de decisión**, sobre una actividad/clúster/arquitectura de control con objetivo explícito, y no como casillero universal de nodos.

## 3. Procedimiento secuencial

### Fase 0 — Inventariar y anclar los ítems

1. Detectar objetos y fragmentos identificables; no limitar el tamaño de ítem: documento, párrafo o entidad externa son admisibles.
2. Asignar un ID estable, una fuente localizable y un hook preciso. Conservar fecha, revisión y evidencia disponible.
3. Crear o actualizar nodos únicamente cuando puedan explicar **qué representan** y qué ítems sostienen esa lectura.
4. Identificar los ítems sin fuente verificable como **pendientes de anclaje**, sin borrarlos ni promocionarlos automáticamente.

**Salida:** registro de ítems, enlaces ítem–nodo y fichas libres de nodos con versión. Relaciones entre ítems pueden existir, pero son complementarias.

### Fase 1 — Barrido amplio de relaciones conceptuales

1. Desde cada nodo, proponer vecinos mediante lectura textual, similitud semántica, comparación de mecanismos, experiencia de campo y preguntas de contraste.
2. Admitir muchos tipos de conexión: pertenencia, uso, analogía, causa propuesta, instrumento, secuencia, oposición, condición, dependencia y frontera candidata. Conservar el **predicado**, no sólo la etiqueta «relacionado».
3. Preguntar: «¿por qué se relacionan?», «¿desde qué fuente?», «¿es una relación afirmada, sugerida o refutada?». Registrar las respuestas.
4. **Si no hay razón conceptual defendible, no crear la arista.** La asociación lexical o vectorial por sí sola es candidato para revisión, no prueba.
5. Evitar enumerar todas las parejas de nodos: generar candidatos en lotes por vecindad, fuentes, analogía y top-K de similitud; revisar incrementos. Mantener las conexiones transversales importantes.

**Salida:** un grafo de asociaciones explícitas y trazables. En esta fase **ninguna arista se fuerza a A/B/C/D**.

### Fase 2 — Distancia epistemológica condicionada por el recorrido

Definir un posicionamiento:

```text
P = (nodo de origen, actividad o función, pregunta, alcance,
     medios/capacidad de evaluación, tiempo/versión)
```

El tema todavía **no** es necesario: se decidirá después. Un posicionamiento no equivale a una etiqueta temática ni a un nivel ontológico fijo.

Para cada trayectoria, conservar:

```text
W = (P, secuencia ordenada de nodos, secuencia de relaciones,
     conjunto de ítems usados, razones y estado de revisión)
```

Al incorporar la arista siguiente, juzgar **la coherencia del recorrido completo W**, y no solamente si los dos nodos finales tienen un parentesco conceptual. Una misma arista puede ser A desde JUBAP y C desde Focus ON. Una relación A–A local **no es transitiva** por defecto a través de otro origen.

Usar las definiciones de 00M:

- **A — explotación activa:** lo que este proceso o hilo efectivamente establece y utiliza para su actividad/pregunta.
- **B — reserva caracterizada:** ampliación evaluable con método, variables o medios identificados, aunque no se ejecute ni sea obligatoria.
- **C — frontera de exploración:** dirección relevante y fundada, pero todavía sin base para evaluar de forma defendible su alcance, coste o resultado.
- **D — residual fuera de evaluación efectiva:** influencia potencialmente material cuya incidencia sobre la pregunta inicial no puede evaluarse por el hilo con sus medios, autoridad, método y tiempo actuales.
- **Sin calificar:** falta de elementos para siquiera asignar uno de esos roles; no se inventa una categoría.

**Regla de parada:** D cierra **ese recorrido**, dejando su causa escrita y, si es posible, un indicador de vigilancia. No cierra otros caminos ni declara el universo conocido. Si un salto no mantiene una relación defendible con el recorrido, **se corta por falta de pertinencia**, sin llamarlo D automáticamente. Que dos palabras estén asociadas por vectores no demuestra que un salto tenga relevancia para el proceso.

**B y C no son barreras obligatorias en un orden rígido.** Puede aparecer A→C, A→B→C, A→C→C→D o una nueva A después de una revaluación documentada. Un C «interior» no es un error fatal: se conserva, se explora y se vuelve a calificar; no se convierte en A/B sólo porque aparecieron más C. El cambio requiere nuevos ítems, medios o un nuevo posicionamiento.

**Resultado obligatorio del recorrido:** `terminal_kind = D | END_OF_GRAPH | CUT_NO_RELEVANCE | BUDGET | CYCLE | REVIEW_PENDING`. La ruta está **completa hasta D** sólo si su último tramo es D. Otra parada es una cobertura parcial con su propia razón, nunca un D ficticio.

### Fase 2b — Segunda lectura funcional Jumps & Falls

Después de haber calificado los pasos ABCD de cada recorrido, y sin cambiar sus valores, asignar los roles `JF.F1` (entrada/coste de claridad), `JF.F2` (procesamiento/proporcionalidad), `JF.F3` (salida/objetivo) y `JF.F4` (efectos colaterales) cuando resulten pertinentes. **F4 es transversal, no cuarto paso obligatorio; puede coexistir con A, B, C o D.** No mezclar Jumps & Falls con el nombre del framework JUBAP ni con otras series F. La receta verificable y sus condiciones de abstención se documentan en [procedimiento §4.4](./PROCEDIMIENTO_LENGUAJE_Y_RECORRIDOS_v0.2.md#44-fase-2b--aplicar-jumps--falls-jff1jff4-después-de-abcd).

### Fase 2.1 — Trabajo finito y revisión controlada

Un grafo finito no garantiza un número pequeño de caminos: el número de rutas simples puede crecer exponencialmente. La **hipótesis de coste acotado** debe comprobarse; D ayudará, pero no es una prueba de terminación o escalabilidad.

Emplear:

1. **Sin ciclos repetidos en un mismo recorrido** durante la primera prueba. Registrar la arista de retorno como enlace conceptual, no duplicar el hilo indefinidamente.
2. Presupuesto explícito de expansión: profundidad, ramas candidatas, tiempo/tokens y prioridad de revisión. Un corte por presupuesto no es D.
3. Cache por `(origen, función, pregunta, versión de evidencias, prefijo de trayectoria)`; no cache global de etiquetas A/B/C/D por arista.
4. Revisar C consecutivos cuando aparezca un mecanismo nuevo, dejando historial de versiones.
5. Guardar las ramas ya calificadas; procesar sólo aristas o hooks nuevos/invalidados.
6. Medir carga antes de afirmar economía: número de caminos iniciados/completados hasta D, C pendientes, nodos alcanzados en A, ramas truncadas, revisiones por cambio de fuentes, coste de inferencia y errores detectados.

### Fase 3 — Identificar clústeres conceptuales principales

Descubrir núcleos **por alcance funcional A desde cada posicionamiento y discurso**, no sólo por frecuencia de palabras. Un nodo principal debe conservar una región A amplia, recorridos interpretables, evidencia y capacidad de distinguir sus fronteras. La comparación debe declarar pregunta y ámbito.

Ejemplo: **embrague** puede ser núcleo principal en un discurso de mecánica y nodo periférico en uno de normas de tráfico. No se declara una «centralidad universal». Un clúster puede cruzarse con otros y un nodo participar en más de uno sin tener que duplicarse.

La medida exploratoria `A_reach(P)` cuenta nodos alcanzables mediante recorridos A *calificados para ese mismo P*; es un indicador de trabajo, no una prueba automática de que algo es un concepto importante. Revisar densidad, mecanismos distintos, fuentes, solapamiento y condiciones de salida. La decisión de cuáles son los clústeres principales permanece interpretativa y revisable.

### Fase 4 — Descubrir y delimitar los temas

Solo ahora proponer ejes temáticos humanos, relativamente pocos y reconocibles. Hacer un brainstorming asistido y comprobar entre todos:

- **Distinción:** dos temas no deben duplicar indefinidamente el mismo propósito.
- **Cobertura:** las regiones relevantes del corpus deben tener una vía de lectura razonable; no inventar una etiqueta para rellenar vacíos.
- **Legibilidad:** una persona puede explicar en pocas frases qué información va en cada tema.
- **Ponderación:** un nodo tiene un **tema primario** (peso normalizado 1 en esta primera versión) y, sólo si está justificado, algunos secundarios con peso menor. No etiquetar todo con todo.
- **Revisión:** nuevas regiones A o cambios de fuentes pueden exigir reasignar temas.

**Salida:** fichas temáticas de descripción libre y asociaciones ponderadas con nodos. No se usan para volver a etiquetar retroactivamente los recorridos como A/B/C/D.

### Fase 5 — Consolidar fichas JSON y detener el alcance aquí

Publicar como objetos de datos versiones de ítems/hooks, nodos, aristas, recorridos, clústeres principales y temas, conservando la **descripción libre** y las fuentes. Se pueden generar vistas legibles o páginas web desde esos mismos registros. Aquí termina la fase 2 propuesta. No desarrollar por ahora nuevos niveles ontológicos, **MSCA universal**, preguntas editoriales obligatorias ni automatismos de decisión. `JF.F1`–`JF.F4` **sí** se registran en la capa de recorrido como segunda lectura posterior a ABCD.

## 4. Pruebas de interpretación

### 4.1 Gato–ratón: misma línea, no simple pareja de palabras

Posicionamiento: *gato en actividad de caza de ratón*. Una trayectoria sintética puede ser:

**Gato → ratón (A) → persecución (A) → mordedura/arañazo (A) → uña (A) → pelo (C) → contacto con pelo (C) → acariciar (D).**

«Acariciar» **sí** está conectado semánticamente con pelo, pero el recorrido acumulado ya no cuenta con un mecanismo para evaluar ese cambio de actividad desde el modelo de persecución. Para calificarlo D, el ensayo declara además que una transición de persecución a interacción afectiva podría cambiar materialmente el desenlace y que el proceso actual **no** tiene ruta para evaluar tal cambio. Si sólo fuera un homónimo o un elemento ajeno sin relevancia posible, se descartaría el salto, sin D.

El ejercicio es **sintético**, no una observación etológica. C puede repetirse y luego resolverse de forma diferente si entra evidencia nueva.

### 4.2 JUBAP frente a Focus ON: la arista cambia de posición

Fuentes públicas: [JUBAP framework](https://jubap.eu/the-jubap-framework/) y [caso Nestlé](https://jubap.eu/nestle-case-study-where-jubap-was-first-named/).

- Desde **JUBAP** para comprender su articulación histórica: JUBAP → Kotter puede ser **A**, porque el uso está descrito dentro del framework y del caso Nestlé.
- Desde **Focus ON** como instrumento de diagnóstico: Focus ON → JUBAP puede ser **A**, pero la siguiente relación JUBAP → Kotter puede entrar en **C** respecto de la función de Focus ON. La misma arista de base permanece.
- Como **prueba límite, no hecho histórico**: Kotter → traslado fuera del caso observado (**C**) → generalización multisitio (**C**) → condiciones externas no observadas (**D**) obliga a declarar que el hilo no puede evaluar influencias potencialmente decisivas en esas nuevas condiciones. Esos últimos enlaces son hipótesis explícitas, no constataciones de aplicabilidad universal.

Para comprobar la lógica ejecutable, ver [fixtures de fase 2](./examples/phase2-fixtures.json) y el validador [validate-phase2.mjs](./scripts/validate-phase2.mjs).

## 5. Remapeado cuando cambia una fuente: diseño pendiente

La futura ingestión debe comparar `hook` y revisión/hash del ítem. Si un artículo, documento, fragmento, API o entidad externa cambia:

1. Guardar el estado anterior y detectar el cambio, sin sobrescritura silenciosa.
2. Marcar para reevaluación sus vínculos ítem–nodo, descripciones y aristas sustentadas.
3. Invalidar o revisar **sólo** recorridos afectados en el contexto donde esos ítems fueron utilizados.
4. Volver a calcular si procede el alcance A, los clústeres y las asociaciones temáticas.
5. Mantener trazas de por qué una clasificación cambió y quién/cuándo la aprobó.

**Pendiente de diseño detallado:** identidad estable entre revisiones, cambios semánticos vs editoriales, colisiones de hooks, políticas de acceso, coste incremental, caducidad de caché y control de dependencias. No implementado en esta fase.

## 6. Prueba y criterios de aceptación

Comandos locales con Node.js (ambos casos deben conservarse):

```bash
node scripts/validate-phase2.mjs
node scripts/validate-language-v02.mjs
```

El validador debe comprobar: integridad de IDs, hooks, referencias, continuidad direccional de cada recorrido, detección de D terminal, posibilidad de C consecutivos, ausencia de una etiqueta global por arista, distinción entre corte de pertinencia y D, y contraste de una misma arista desde dos orígenes.

Antes de llevar a producción:

- Revisión humana y evidencia para clasificaciones A/B/C/D propuestas.
- Prueba de escala con varios tamaños de grafo, densidad de relaciones y múltiples posicionamientos; medir crecimiento y precisión, no presuponer rendimiento.
- Ensayo real de reevaluación de una fuente cambiada, sin perder la versión anterior.
- Auditoría de selección de clústeres y temas: ¿preservan el discurso o amplifican sesgos de la primera extracción?

## 7. Fuentes, precedencia y límites

**Versiones de esta rama:** el procedimiento integral v0.2 y el diccionario v0.1 son ahora las referencias operativas del Atlas fase 2; los ejemplos y el validador v0.1 permanecen como prueba histórica de la distancia ABCD. Los nuevos ejemplos v0.2 agregan fichas etiquetadas y factores JF sin publicar la base privada. Estado **experimental**, no estándar ni documento EA controlado.

1. [00M v0.8 — A/B/C/D](../../ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical): autoridad terminológica en el corpus EA/EP; no se modifica.
2. [Programme Bridge: Map, Flow, Epistemic Distance](../MAP_FLOW_EPISTEMIC_DISTANCE_PROGRAMME_BRIDGE_v0.1_DRAFT.md): síntesis **no canónica** de distancia epistemológica, sin métrica obligatoria.
3. [EA Canonical Corpus Manifest](../../ecosystem-awareness/baseline/CANONICAL_CORPUS_MANIFEST.md): delimitación de estado y versiones; esta rama Atlas está fuera de su baseline congelado.
4. [JUBAP — framework](https://jubap.eu/the-jubap-framework/) y [Nestlé case study](https://jubap.eu/nestle-case-study-where-jubap-was-first-named/): contexto y uso histórico, no prueba causal independiente.
5. **Atlas conceptual privado v1.0 (2 nov 2026):** 125 nodos, 380 relaciones editoriales. Es fuente de trabajo para la prueba privada; sus datos internos no se copian aquí ni se convierten en publicación pública.

**Separación de alcance:** este protocolo es una hipótesis instrumental para organizar un corpus de pensamiento, no una formalización nueva de Ecosystem Awareness, una declaración de cumplimiento ni una metodología DDS. La prueba interactiva privada del Atlas conserva sus propias extensiones, resultados y accesos.
