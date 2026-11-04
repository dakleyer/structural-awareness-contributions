# Perspective Beyond / Atlas — Procedimiento operativo de ítems, nodos, etiquetas y recorridos

**Versión:** 0.2 · 4 de noviembre de 2026  
**Estado:** procedimiento de referencia **para el piloto experimental Atlas fase 2**; sujeto a pruebas y revisión. Es canónico **dentro de esta rama de trabajo**, pero **no** modifica documentos controlados, definiciones A/B/C/D, especificaciones de Ecosystem Awareness, MSCA ni estados institucionales.  
**Precedencia local:** este procedimiento v0.2 prevalece sobre instrucciones operativas contradictorias del README experimental v0.1. Conserva los ejemplos anteriores como historial.  
**Artefactos:** `TAG_DICTIONARY_v0.1.json` (lenguaje descargable), `examples/language-v02-pilot.json` (ejemplo trazable) y `scripts/validate-language-v02.mjs` (validación estructural).  
**Separación:** un descriptor metodológico no constituye evidencia sobre el mundo; una fuente histórica, una interpretación y una hipótesis deben conservar estados separados.

## 0. Contrato de alcance y vocabulario

El Atlas representa un **grafo conceptual único** que admite múltiples constelaciones, clústeres y modos de lectura, con fuentes y áreas comerciales/no comerciales conectables. En esta fase no redefine esa arquitectura de publicación. Aquí se define el **protocolo incremental de minado y estructuración**.

Los nombres tienen significados distintos:

| Nombre | Identidad | Definición operativa | Qué NO significa |
|---|---|---|---|
| **Ítem** | `item_id` | Cosa real o imaginaria **referible**, desde persona/empresa/software hasta documento, URL, página, párrafo o fragmento; también un caso sintético declarado como tal. Tiene ficha y un *hook* para recuperar o reevaluar su referencia. | No es el nodo; un título o mención sin ancla no prueba que el objeto o la afirmación exista. |
| **Nodo** | `node_id` | Posicionamiento o unidad de descripción conceptual, con ficha semiestructurada, una descripción libre y vínculos a ítems. | No recibe una etiqueta A/B/C/D universal; puede participar en muchas perspectivas. |
| **Etiqueta** | `key` estable | Unidad de vocabulario para describir fichas de ítems, nodos y relaciones; admite valor estructurado, sinónimos, traducciones y reutilización. | No es por sí sola evidencia, tema o arista entre nodos. |
| **Relación de nivel 1** | `edge_id` | Vínculo conceptual entre nodos, con predicado, evidencia/razón y semántica de dirección, sin distancia epistemológica todavía. | No es una inferencia transitiva ni un paso obligatorio de proceso. |
| **Recorrido de nivel 2** | `walk_id` | Secuencia dirigida y ordenada de aristas de nivel 1 desde un origen, actividad, pregunta y capacidad de evaluación, calificada paso a paso. | No es un atributo fijo de cada arista. |
| **Clúster conceptual principal** | `cluster_id` | Región de alcance funcional A, interpretada en un discurso/posicionamiento, con fronteras y superposiciones documentadas. | No es el componente conexo de todo el grafo ni una ontología universal. |
| **Tema** | `theme_id` | Eje legible y diferenciado, descubierto **después** de recorridos y clústeres, con ficha descriptiva y asociación ponderada a nodos. | No determina retrospectivamente el significado de A/B/C/D. |

**Regla invariable de orden:** (0) anclar ítems y nodos → (1) mapear relaciones conceptuales → (2) calificar distancia A/B/C/D por recorrido → (2b) aplicar JF.F1–JF.F4 cuando corresponda → (3) identificar clústeres principales → (4) descubrir temas y elaborar sus fichas → (5) consolidar, revisar y publicar datos versionados. Las fichas se crean desde la fase 0 y pueden enriquecerse en cada ciclo; no se exige completarlas antes del mapa. **MSCA** es una proyección opcional posterior o bajo demanda, no una etapa obligatoria que reordene la minería.

## 1. Lenguaje canónico de **etiquetas**: flexible, compartible y versionado

### 1.1 Lo que se fija y lo que permanece abierto

1. **Fijo:** IDs estables, tipo de objeto, formato JSON, hook localizable de ítem, referencias, estado de evidencia, semántica de origen/dirección del recorrido, enumeraciones A/B/C/D, JF.F1–JF.F4 y razones de revisión.
2. **Flexible:** redacción de `description`, selección y número de etiquetas descriptivas, valores textuales, tipo de nodo, campos semánticos adicionales y nuevas etiquetas propuestas. **No imponer MSCA** como formulario de todo nodo.
3. **Un mismo diccionario** gobierna las etiquetas aplicables a ítem, nodo, relación, clúster y tema, pero cada entrada especifica sus `applies_to`. No toda etiqueta resulta pertinente a todo objeto.
4. El diccionario es **descargable como JSON** e incorpora versión, claves estables, descripción, ejemplos, restricciones, sinónimos, traducciones y estado de cada entrada. El lenguaje crece por revisión, no por multiplicar términos equivalentes.

### 1.2 Rutina obligatoria de un bot antes de extraer o escribir

1. Leer el manifiesto/README del Atlas y descargar la **versión identificada** de `TAG_DICTIONARY_v0.1.json`. Verificar su versión y no mezclar silenciosamente diccionarios distintos.
2. Leer las entradas relevantes con `key`, `definition`, `value_type`, `applies_to`, `examples`, `translations`, `aliases`, `state`, `constraints` y `replaces` si existe. **La clave estable**, no su traducción, es la que se guarda.
3. Al extraer una propiedad, buscar primero coincidencia de **sentido** con una clave existente. Un sinónimo sirve para encontrar una clave, no para asumir identidad semántica cuando hay varios candidatos.
4. Si la clave existente encaja, reutilizarla con el tipo correcto y vincular el dato al ítem/hook o a la interpretación que lo produjo. No crear sinónimos nuevos como claves por cada idioma, estilo o bot.
5. Si no encaja ninguna, proponer una etiqueta `proposed:<slug>` con definición, tipo, objetos a los que aplica, diferencia respecto a las más próximas, ejemplos, contraejemplo, idioma de origen y autor/revisión. Puede emplearse localmente **como propuesta visible**, no como etiqueta compartida ya ratificada.
6. Registrar si una propiedad procede de la fuente, es inferencia, analogía, hipótesis, negación o ausencia de información. No convertir una etiqueta de posibilidad en un hecho.
7. En debates entre bots, comparar las **definiciones y usos**, no votar sólo nombres. Resolver: `reusar`, `crear`, `alias`, `separar`, `fusionar`, `deprecar` o `aplazar`. Dejar decisión, evidencia, responsable y fecha/versionado. Una deprecación preserva la clave antigua y su ruta de migración.
8. Releer el objeto completo tras normalizar etiquetas para comprobar que **la compresión no ha eliminado negaciones, condiciones, tiempo, incertidumbre ni procedencia**. Mantener el texto libre original y las anclas. No declarar compresión sin pérdida por el solo hecho de usar etiquetas.

### 1.3 Sintaxis y traducción

Cada ficha admite `etiquetas: [{"key": "node:role", "value": "herramienta de diagnóstico", "basis": "source", "item_refs": [...] }]`. El `value` puede ser texto, número, booleano, lista u objeto conforme a `value_type`. Las claves usan namespace (`core:`, `trace:`, `evidence:`, `node:`, `edge:`, `walk:`, `cluster:`, `theme:`, `proposed:`); nunca se traducen. La presentación muestra `translations.es`, `translations.en` y, más adelante, otras lenguas. Las traducciones no crean otra identidad de etiqueta.

Los campos estructurales `hook`, `description`, `item_refs`, `position`, etc. **también son conceptos del diccionario** (por ejemplo `trace:hook`), pero se materializan en su **ruta JSON reservada** para lectura eficiente. No duplicar un hook completo dentro de `etiquetas` y a la vez en `/hook`: la entrada del diccionario declara el `json_path`. Las etiquetas flexibles viven en `/etiquetas`.

### 1.4 Control de colisiones

- La letra **C** en `ABCD.C` no es `MSCA.C` (alcance de coordinación). Usar namespaces.
- `JF.F1`–`JF.F4` pertenece a **Jumps & Falls**, no a los factores F de otros documentos, Theme #13, pruebas de Ecosystem Awareness ni a la herramienta JUBAP denominada JUMP UP. Jumps & Falls y JUBAP son arquitecturas relacionadas pero distintas.
- Una etiqueta de tema `theme:*` no debe convertirse en tema definitivo antes de la fase 4. Una etiqueta descriptiva como `node:mechanism` **no es un eje temático**.
- Dos nodos que comparten etiquetas **no quedan conectados automáticamente**: necesitan una relación conceptual explícita y justificada de nivel 1.

## 2. Fase 0 — Crear fichas semiestructuradas de **ítem** y **nodo**

### 2.1 Ítem: ficha, hook y prueba de identidad

**Mínimos para un ítem anclado:** `id`, `kind`, `description`, `hook.uri`, `hook.locator`, `hook.observed_at` o revisión verificable, `evidence_status`, `version`, `etiquetas` (puede ser `[]`). Los otros componentes del hook son opcionales pero recomendables: `revision`, `content_hash`, `language`, `access`, `retrieved_at`, `owner`. La fuente puede ser un registro externo, objeto físico/documental o dato privado permitido, no sólo una URL pública.

**Tipos de localizador:** URL + sección/fragmento; fichero + revisión Git + línea/JSON Pointer; PDF + página; identificador de registro; ID de organización con emisor; referencia física catalogada + ubicación y estado; artefacto sintético propio + versión. Una cadena “persona X” sin mecanismo de identificación es un **candidato por anclar**. No publicar DNI, documentos de identidad ni registros restringidos para satisfacer la trazabilidad: guardar un token/ID protegido y sus permisos.

**Ficha del ítem = descripción del objeto referible**, no opinión sobre el nodo. Puede haber ítems dentro de ítems y relaciones ítem–ítem. Conservar identidad de ítem y vínculo `part_of`, `version_of` u otro predicado cuando el origen lo justifique; no duplicar todos sus fragmentos sin necesidad.

**Si falta hook:** conservar el candidato con `evidence_status: "pending_anchor"`, no promocionarlo a evidencia. **Si cambia hook:** guardar nueva revisión y disparar reevaluación de los nodos/aristas/rutas/clústeres/temas que dependan de él; no cambiar la fuente antigua a escondidas.

### 2.2 Nodo: ficha libre organizada por etiquetas

**Mínimos:** `id`, `label`, `description` autosuficiente, `item_refs` con función de cada fuente, `version`, `evidence_status`, `etiquetas` (puede estar vacío). Se recomiendan etiquetas `node:role`, `node:mechanism`, `node:scope`, `node:distinction`, `node:observable`, `node:condition` **sólo cuando sean útiles y estén sustentadas**. Es válido que un nodo carezca de mecanismo o de un resultado explícito; no rellenar con contenido imaginado.

Un vínculo `item_refs` indica **cómo** apoya la fuente: definición directa, uso histórico, ejemplo, observación, testimonio, refutación, hipótesis, analogía, o candidato. La presencia de una URL no prueba que todas las propiedades del nodo estén contenidas en ella; cuando importa una afirmación, registrar `locator` y el alcance de lo que respalda.

**Secuencia editorial:** mantener redacción libre de la ficha → identificar propiedades que se repiten → buscar clave existente en el diccionario → extraer etiquetas sustentadas → revisar que la ficha sigue autosuficiente → registrar versión y dependencias. La etiqueta **no sustituye** la descripción ni debe forzar un análisis MSCA por defecto.

## 3. Fase 1 — Mapa general de **relaciones conceptuales** (nivel 1)

1. Para cada nodo, generar candidatos vecinos por proximidad semántica, fuente compartida, pertenencia, uso, analogía, dependencia, oposición, secuencia, mediación, capacidad y preguntas de contraste. El barrido ha de ser amplio, por lotes, sin cerrar clústeres por anticipado.
2. Para cada candidato, preguntar **qué relación existe**, **por qué**, **dónde consta**, **con qué alcance**, **en qué dirección tiene sentido el predicado** y **qué falta comprobar**. No conectar sólo por similitud vectorial o coincidencia de etiquetas.
3. Si existe un vínculo defendible, crear **una arista de nivel 1** con `source`, `target`, `predicate`, `semantic_direction` (`directed`, `symmetric`, `inverse_available`), `reason`, `item_refs`, `evidence_status`, `etiquetas`, `version`. Si el vínculo no es defendible, rechazar candidato y guardar su motivo opcionalmente; **no** crear arista ni llamarlo D.
4. El nombre del predicado se normaliza con el diccionario (`edge:relation_type`) cuando resulte útil, pero preservar una explicación natural libre. Conservar divergencias: `causó`, `pudo contribuir` y `se articuló con` no son equivalentes.
5. Se permiten aristas transversales y entre clústeres; pertenencia a una constelación o ámbito de publicación **no** las prohíbe. No hacer una relación global de todos contra todos: generar candidatos localmente, revisar nuevas fronteras y almacenar enlaces confirmados/candidatos.
6. **Invariante:** una arista de nivel 1 **no** tiene `abcd`, `jf_roles`, `status: "A"` ni distancia global. Guarda semántica conceptual y evidencia, no la calificación de una posición.

**Salida:** `edges[]` como mapa neutral. Una arista puede ser recorrida a favor o en sentido inverso **solo cuando el predicado admite una lectura inversa defendible** (por ejemplo, `incluye` ↔ `pertenece a`); invertir `causa` no autoriza inferir causalidad inversa.

## 4. Fase 2 — **Distancia epistemológica** desde cada posicionamiento (nivel 2)

### 4.1 Declarar posición antes de caminar

Cada recorrido identifica `position.origin` (nodo inicial), `activity` (proceso, función o uso que se examina), `question` (pregunta delimitada), `scope`, `capability` (método, autoridad, observación, acceso, recursos para evaluar), `as_of` y `dictionary_version`. No iniciar una calificación sin una pregunta y sin precisar la capacidad efectiva de evaluación. La posición **no exige conocer aún el tema**.

Cada paso `steps[]` contiene `edge_id`, `from`, `to`, `direction` (`forward`/`reverse` respecto a la arista base), `abcd` y `abcd_reason`, más las referencias utilizadas. El algoritmo considera **todo el prefijo acumulado**: origen → ... → paso actual. Una arista que es A desde JUBAP puede ser C desde Focus ON; se conservan **ambas evaluaciones** sin sobrescribir el nivel 1.

### 4.2 Decisión A/B/C/D (lectura fiel de 00M v0.8 §1)

**A — explotación activa:** el proceso, bajo su pregunta y alcance, **efectivamente emplea/produce** esa función o resultado. No basta con que dos nodos estén asociados en nivel 1. La primera relación conceptualmente encontrada no pasa a A por decreto cuando se juzga un hilo concreto.

**B — reserva de explotación caracterizada:** opción pertinentemente descrita y **evaluable** mediante variables/método/medios identificados, pero no usada necesariamente. No equivale a obligación de ejecutar; puede existir junto a A.

**C — frontera de exploración:** conexión potencialmente relevante y **fundada**, pero aún sin caracterización suficiente de mecanismo, condiciones, alcance, coste o valoración defendible. Puede haber C interior y C consecutivos; no declarar que todo C es D ni que todo C invalida el recorrido.

**D — influencia/residual más allá de evaluación efectiva:** algo potencialmente **material** para la pregunta del proceso, situado fuera de su capacidad real de determinar/evaluar bajo el método, autoridad, acceso o tiempo declarados. **D no significa “sin relación” ni simple contraste**. En D se para **ese recorrido**. Si el salto es irrelevante o no puede justificarse como relación conceptual pertinente, cortar como `CUT_NO_RELEVANCE`, no clasificarlo D.

**UNKNOWN / REVIEW_PENDING:** cuando todavía no hay base suficiente para elegir. No forzar A, B, C o D; abrir revisión. Las cuatro categorías son roles de un proceso situado, no casillas mutuamente excluyentes del universo ni probabilidad numérica.

### 4.3 Algoritmo de recorrido reproducible

1. Seleccionar origen y pregunta. Tomar las **aristas de nivel 1** pertinentes como candidatos de salida; respetar `semantic_direction`.
2. Formar prefijo con nodos/aristas ya recorridos y revisar fuentes/etiquetas, su temporalidad y contradicciones.
3. Preguntar primero si el próximo paso **mantiene vínculo con la actividad y todo el prefijo**. Si no, cortar por falta de pertinencia. No fabricar un D.
4. Si mantiene vínculo, evaluar por orden de significado **A, B, C, D**: ejecución efectivamente demostrada; reserva caracterizada; exploración fundada no caracterizada; residual potencialmente material fuera de evaluación. No son fases cronológicas de un proceso y **pueden saltarse categorías**.
5. Guardar `abcd`, razón precisa, evidencia/hook, tramo/dirección, evaluador, confianza explicada y fecha. La confianza de una propuesta no se presenta como probabilidad científica.
6. Si es D, marcar `terminal_kind: "D"`, guardar **qué capacidad falta** y detener **sólo esa rama**. Si es A/B/C, considerar expansiones del nodo alcanzado y conservar el nuevo prefijo.
7. Admitir revisiones: un C puede volverse B/A con evidencia o método nuevos, o degradarse; **registrar nueva versión/posición y causa del cambio**. No renombrarlo silenciosamente por haber seguido caminando.
8. Prevenir ciclos de recorrido, aunque el grafo base conserve anillos; asignar presupuesto explícito de profundidad/ramas/tokens/tiempo y guardar paradas `CYCLE`, `BUDGET`, `END_OF_GRAPH`, `REVIEW_PENDING`. **Una ruta limitada por presupuesto no es D.**

### 4.4 Fase 2b — Aplicar **Jumps & Falls (JF.F1–JF.F4) después de ABCD**

**Jumps & Falls es una arquitectura de análisis de valor distinta de JUBAP; no es el etiquetado F de FG-TIDA.** Es una *segunda lectura funcional*, no una corrección automática de A/B/C/D. Requiere que el posicionamiento tenga una actividad/transformación y una pregunta a la que esos factores aporten sentido.

| Factor | Función de lectura | Pregunta de minado | Posible evidencia |
|---|---|---|---|
| `JF.F1` | **Entrada / Cost of Clarity** | ¿Qué información entra, qué entendemos, cuánto cuesta obtener claridad utilizable y cuáles son las dependencias? | Fuente, calidad, adquisición, distinción, acceso, costes. |
| `JF.F2` | **Procesamiento / Processing Proportionality** | ¿Qué mecanismo transforma esa entrada? ¿Es proporcional y realizable? | Secuencia, acción, método, dependencias, medios, esfuerzo. |
| `JF.F3` | **Salida / objetivo y valor obtenido** | ¿Qué resultado se pretende o se ha observado? ¿Se logra el objetivo declarado? | Producto, resultado, efecto medible, objetivo y alcance. |
| `JF.F4` | **Efectos colaterales** | ¿Qué cambia directa o indirectamente fuera de la cadena principal, incluso por el mero intento? | Impactos humanos, sociales, reputacionales, regulatorios, proveedores, externalidades. |

**F1→F2→F3 es una cadena de lectura; F4 es una dimensión transversal**, no un cuarto paso obligatorio. Los resultados *Jump/Walk/Fall*, cuando se analicen, son otra clasificación y **no** equivalen a F1/F2/F3/F4.

**Reglas:** (a) `JF.Fx` pertenece a la función de **un paso en su recorrido**; no se fija globalmente en el nodo o la arista; (b) un paso puede tener cero, uno o varios roles, cada uno con razón; (c) el bot considera candidatos F1–F4 después de escribir/revisar ABCD; (d) `JF.F4 ≠ D`: un efecto colateral puede ser A, B, C o D; (e) `JF.F3 ≠ A`: un objetivo de salida hipotético puede ser C; (f) si no aplica la lente de transformación, `jf_roles: []` con `jf_applicability: "not_applicable"`, diferente de `"not_assessed"`; (g) no inferir eficacia empresarial por haber asignado F2/F3.

**Ejemplos de lectura:** desde JUBAP, Focus ON puede aportar `JF.F1` como entrada diagnóstica, roleplay `JF.F2` como medio de procesamiento, transformación organizativa `JF.F3` como resultado buscado, y liberación emocional `JF.F4` como efecto potencial **C**, no D automático. Desde Focus ON, la arista JUBAP–Kotter podría pasar a **C** aun cuando desde JUBAP fuese **A**; su rol JF requiere esa posición, no la etiqueta global de Kotter.

### 4.5 Criterio de término y costo

Una ruta sólo se declara `complete_to_D` cuando **D es el último paso** y se expresa por qué la influencia es material e inabordable bajo la capacidad declarada. Otros terminales son rutas parciales, revisables. No suponer que detenerse en D controla por sí solo la complejidad: contar ramas, expansión, revisiones, coste de inferencia, cambios de hooks, diversidad de orígenes y C pendientes. Cachear por `(origin, activity, question, scope, capability, evidence_revision, path_prefix)`; nunca cachear un A/B/C/D universal por arista.

## 5. Fase 3 — Clústeres conceptuales principales

1. Con los recorridos versionados, agrupar por **posicionamiento y pregunta**, no por grado bruto del grafo.
2. Examinar el alcance de A de cada núcleo, conectividad, densidad de mecanismos, diversidad de fuentes, fronteras B/C/D y solapamientos con otros núcleos. Una zona A amplia **propone** un clúster principal; no lo demuestra automáticamente.
3. Probar cambios de perspectiva: el embrague puede ser un núcleo en mecánica y periférico en normas de tráfico. Conservar la relatividad del concepto; no duplicar nodos por cada perspectiva.
4. Guardar `cluster_id`, `core_node_ids`, `position_refs`, `a_reach`, `boundary_walk_refs`, `description`, `item_refs`, `etiquetas`, `review_status`, `version`. El clúster describe un alcance **comprobable en las rutas existentes**, no exhaustividad del mundo.
5. Permitir superposición y enlaces entre clústeres; no clausurar constelaciones por pertenencia temática o comercial.

## 6. Fase 4 — Ejes temáticos y **fichas de tema**

**Decisión de trabajo propuesta, pendiente de aprobación final:** **sí, reutilizar el mismo diccionario de etiquetas y el mismo JSON semiestructurado**, extendido con entradas `theme:*` sólo si aportan distinciones reales. Mantener ficha textual libre; no abrir un segundo lenguaje paralelo para temas. La taxonomía ayuda a indexar, **pero un tema no es sinónimo de etiqueta**: el tema es una perspectiva editorial/intelectual sobre conjuntos de clústeres.

1. Tras revisar clústeres, proponer pocos **ejes temáticos legibles**; preguntar qué discurso ordenan y cuáles quedan fuera.
2. Contrastar entre sí **distinción** (no duplicación), **cobertura** (qué clústeres quedan atendidos), **coherencia** (no agrupar solo por palabras), **trazabilidad** (desde qué nodos/ítems) y **legibilidad humana**.
3. Crear ficha `theme_id`, `title`, `description` libre, `scope`, `distinction_from` cuando sea útil, `cluster_refs`, `node_associations` ponderadas, `item_refs` de apoyo si procede, `etiquetas`, `version` y `review_status`.
4. En esta versión asignar, cuando la clasificación temática esté madura, **un tema principal de peso 1** por nodo del ámbito evaluado; secundarios **sólo justificados y de menor peso**, sin poner todos los temas en todos los nodos. No convertir esta ponderación en una probabilidad de verdad ni adelantarla a la fase 2.
5. Una ficha temática es autosuficiente en lenguaje natural, aunque legible como JSON; no exigir tres páginas, número fijo de párrafos ni MSCA. Puede generarse una vista HTML/PDF distinta **desde los mismos datos** sin crear otra fuente canónica.

## 7. ¿Dónde entra MSCA? — proyección opcional de control, documentada en v0.1

**Acuerdo de diseño en prueba:** MSCA se trata como una **capa adicional seleccionable por objetivo y actividad**, no como cinco casillas obligatorias para fichas de ítem, nodo, tema o clúster. Su interfaz completa, supuestos, reglas, ejemplo y pruebas están en **[MSCA como capa adicional del Atlas v0.1](./MSCA_CAPA_ADICIONAL_ATLAS_v0.1.md)**. Es un **adaptador experimental**: no cambia la [arquitectura canónica MSCA](../../../standards/minimum-sufficient-control/00_CANONICAL_MSCA_ARCHITECTURE.md).

### 7.1 Cuándo se abre una vista MSCA

1. Partir de un posicionamiento, clúster y/o tema útil, **con referencias a recorridos e ítems**; no basta una etiqueta temática o la amplitud A del nodo.
2. Formular un **problema de control** y una pregunta de suficiencia para **un Objective Envelope** delimitado. Identificar su titular legítimo; si no se conoce, dejar `owner_status=UNKNOWN`, `binding_status=UNBOUND` y `S=UNKNOWN`.
3. Crear **una entidad independiente `msca_view`** con referencias al Atlas y representación parcial `X=[S,E,C,P,M]`. No copiar literalmente ABCD/JF a esos campos. Reutilizar el **mismo diccionario de etiquetas** para notas e índices; los cinco campos MSCA conservan sus significados canónicos.
4. Conservar `POPULATED` (valor cualificado), `UNKNOWN` y `UNPOPULATED` por campo, con fuentes, condiciones y tiempo. El estado de suficiencia es **independiente**: `UNASSESSED | SUPPORTED | FAILED | UNRESOLVED`.
5. Solo después de especificar S/E y evidencias valorar configuraciones C/P/M y carga justificada; una vista sin evaluación **no** acredita control. Autoridad, ejecución y medida de efecto son fronteras externas.
6. Varias vistas pueden usar el mismo clúster bajo objetivos/mandatos diferentes. **Nunca** fusionar S o trasladar `SUPPORTED` entre vistas por compartir nodos o etiquetas.

### 7.2 Encaje con los recorridos A/B/C/D y JF

- **A/B/C/D** siguen siendo **calificaciones de pasos de un hilo Atlas acumulado**. Que un método aparezca en **A** no lo convierte en intervención suficiente; un **C** abre una pregunta; **D** cierra ese hilo situado y limita extrapolaciones.
- **JF.F1–JF.F4**, añadidos **después** de ABCD, aportan pistas sobre entradas, mecanismos, salidas y efectos laterales. No existe mapeo automático `F1→M`, `F2→P`, `F3→S` o `F4→E`: cada correspondencia requiere proceso/objetivo, fuentes y evaluación.
- `MSCA.C` es **alcance de coordinación** y `ABCD.C` es **frontera de exploración**. MSCA tiene una posición cualificada propia `Π_MSCA=[A_X,B_X,C_X,D_X]`, evaluada sobre **su** arquitectura de control, no copiada del recorrido Atlas.
- El ejemplo [JUBAP / dos vistas MSCA](./examples/msca-view-v01.json) enlaza dos preguntas controladas sobre el mismo clúster. En ambas `S` no está legitimado y el resultado es `UNASSESSED`; véase [validador](./scripts/validate-msca-view-v01.mjs).

**Lugar procedimental:** tras los clústeres/temas, como **fase opcional a demanda**; también se puede abrir una vista parcial antes de cerrar un tema si ya existe la pregunta de control. No retrasa ni obliga a reestructurar las fases 0–4. La revisión de un hook puede invalidar selectivamente una vista MSCA dependiente sin recalcular todo el mapa.

## 8. Reevaluación, custodia y verificación

### 8.1 Cadena de dependencia ante cambio de fuente

`item hook/revisión → enlaces ítem–nodo → fichas de nodo → aristas de nivel 1 → recorridos afectados nivel 2 (ABCD, después JF) → clústeres candidatos → temas/fichas/asociaciones → **vistas MSCA dependientes** (si existen)`. Recalcular únicamente descendientes afectados cuando sea justificable; conservar historial y revisor. Cambios cosméticos pueden no alterar semántica: registrar la decisión. Las aristas y calificaciones no se invalidan indiscriminadamente porque comparten una palabra.

### 8.2 Control de calidad por fase (no sólo JSON válido)

| Puerta | Requisito mínimo | Bloqueo / registro si falla |
|---|---|---|
| Ítems | Hook resoluble o estado pendiente explícito; versión/fecha; alcance de evidencia. | `pending_anchor`; no usar como prueba histórica. |
| Nodos | Descripción autosuficiente, ítems referidos y etiquetas tipadas; sin suposición no declarada. | `review_pending` o `candidate`. |
| Nivel 1 | Motivo/predicado, dirección semántica, evidencia o hipótesis identificada; sin ABCD/JF global. | Rechazar arista o dejar candidato no publicado. |
| Nivel 2 | Posición completa; continuidad de flechas; cada paso con ABCD+razón; D terminal genuino; cortes diferenciados. | Ruta parcial con terminal real. |
| JF | Se ejecuta después de ABCD; factor motivado por función; F4 transversal; namespace correcto; abstención permitida. | `not_assessed` / `not_applicable`, nunca inventar. |
| Clústeres | Alcance A contextual, revisión de límites y solapamientos; no solo centralidad numérica. | Candidato pendiente. |
| Temas | Diferenciación/cobertura, ficha libre, etiquetas del mismo diccionario y peso primario revisable. | Etiquetas temáticas provisionales. |
| MSCA (opcional) | Vista delimitada por objetivo/actividad, campo S/E/C/P/M con procedencia y estados, assessment independiente, autoridad separada. | Si falta legitimación/prueba: `UNKNOWN` / `UNASSESSED`; nunca `SUPPORTED` automático. |
| Diccionario | Claves únicas/versionadas; alias sin colisión silenciosa; traducciones sin alterar identidad; migración rastreable. | Propuesta pendiente o conflicto documentado. |

### 8.3 Prueba mínima repetible

- [ ] El bot interpreta sin ambigüedad el diccionario antes de crear fichas, reutiliza claves existentes y propone una nueva sin elevarla a canónica automáticamente.
- [ ] El mismo caso JUBAP–Kotter conserva su arista de nivel 1: desde JUBAP es **A** y desde Focus ON puede ser **C**.
- [ ] Un hilo recorre **C→C→D** sin degradar los C por el solo hecho de continuar y se detiene en D.
- [ ] Otro hilo se detiene por falta de pertinencia o presupuesto **sin declararlo D**.
- [ ] Un ejemplo de **JF.F4 con ABCD.C** prueba que JF.F4 ≠ D, y la validación rechaza F1–F4 como estado de nivel 1.
- [ ] Nodo sin MSCA obligatorio y ficha temática con el mismo diccionario se serializan y se leen sin perder descripción libre.
- [ ] Dos vistas MSCA del mismo clúster conservan problemas/objetivos separados; un recorrido Atlas A no produce evaluación `SUPPORTED`. Ejecución: `node scripts/validate-msca-view-v01.mjs`.
- [ ] El ejemplo distingue hechos publicados, interpretación y aristas hipotéticas de enseñanza.
- [ ] Al alterar un hook se obtiene lista de dependencias por revisar; no se finge que existe aún un motor de reevaluación automático.

El validador adjunto **solo** revisa estructura. La calidad semántica, la clasificación epistemológica, la utilidad de JF, el ajuste del diccionario y el coste de inferencia requieren revisión humana y futuras pruebas comparativas.

## 9. Fuentes y precedencia documental

1. **A/B/C/D:** `research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md`, §1 — léxico adoptado; **no se modifica**.
2. **MSCA:** `standards/minimum-sufficient-control/README.md` y sus documentos controlados — este procedimiento sólo propone una interfaz futura, no reescribe MSCA.
3. **Linaje y caso:** https://jubap.eu/nestle-case-study-where-jubap-was-first-named/ y https://jubap.eu/the-jubap-framework/; uso histórico no valida transferencias hipotéticas.
4. **Programa:** https://tegrity.ai/structural-awareness-program/ y las Field Notes aplicables; su condición editorial no equivale a estandarización adoptada.
5. **Ensayo anterior:** `README.md` y `examples/phase2-fixtures.json`, v0.1; conservar como comparación, no sobrescribir sus fuentes o etiquetas.
6. **Diccionario y caso v0.2:** archivos vecinos. Los ejemplos sintéticos y las propuestas no son evidencia empírica ni documento controlado del corpus EA.

**Criterio de evolución:** incorporar mejoras por cambios aditivos, aliases/versionado y revisiones locales; no renombrar silenciosamente claves, ítems, nodos, historias ni afirmaciones. Ante conflicto entre fuente y ficha, anotar la discrepancia y revisar la ficha, no silenciarla.
