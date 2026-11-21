# Atlas fase 2 — Temas después del grafo: contrato público, revisión interna y estadística

**Versión:** 0.1 · 5 de noviembre de 2026

**Estado:** decisión de arquitectura del piloto Atlas, sujeta a comprobación empírica; no modifica baselines EA/MSCA ni constituye una taxonomía temática validada.

**Precedencia:** desarrolla la fase 4 del [procedimiento v0.2](./PROCEDIMIENTO_LENGUAJE_Y_RECORRIDOS_v0.2.md); corrige expresamente la antigua pauta experimental «tema principal = 1 más secundarios».

## 1. Regla fundamental: no poner el tema antes del grafo

El orden de producción es **ítems con anclas → fichas de nodo → relaciones conceptuales de nivel 1 → recorridos situados A/B/C/D (y lectura JF cuando proceda) → clústeres descubiertos → temas → asociaciones nodo–tema**. Las comparaciones entre temas y las estadísticas son **resultados posteriores** del grafo, no premisas para construirlo. La clasificación temática nunca redefine retrospectivamente una arista, una ruta, un alcance A o una frontera D.

Una **etiqueta** es vocabulario descriptivo; un **nodo** es una unidad conceptual; un **tema** es el nombre y descripción comprensibles de una materia identificada al examinar el grafo. Compartir palabras, etiquetas o tema **no demuestra relación conceptual**. Los temas pueden superponerse; las conexiones efectivas entre sus nodos se investigan en el grafo.

## 2. Ficha pública de tema: habla del tema, no del mapa

La ficha es **semiestructurada, en JSON, con lenguaje natural autosuficiente** y claves del [diccionario compartido](./TAG_DICTIONARY_v0.1.json). Sus campos mínimos son:

| Campo | Contenido permitido |
|---|---|
| `id` (`theme_id` lógico) | Identidad estable del tema. |
| `title` | Nombre humano, sin inferir parentescos con otras materias. |
| `description` | Qué significa el tema en sí; definición comprensible y suficiente. |
| `scope` (opcional) | Alcance **semántico propio**: a qué se refiere ese término, sin preseleccionar nodos, clústeres ni rutas. |
| `etiquetas` | Descriptores tipados del mismo diccionario, si añaden precisión a la definición. |
| `version`, `review_status` | Revisión del registro y grado de revisión editorial de su descripción. |

Se admiten sinónimos o traducciones de título/descripción como **variantes lingüísticas de la misma identidad**, sin crear nuevas relaciones. No hay longitud fija ni un cuestionario adicional.

**No incluir en la ficha temática** `central_question`, `why_together`, `distinction_from`, comparaciones con otros temas, `cluster_refs`, `node_associations`, `theme_relations`, recorridos A/B/C/D, métricas de centralidad ni explicaciones de por qué pertenecen ciertos nodos. Las preguntas declaradas pertenecen a **recorridos**, las relaciones entre nodos al **nivel 1**, los límites evaluados al **nivel 2**, y los resultados de agrupación al **análisis de grafo**. Esas capas no se trasladan a la definición de la materia.

Una ficha de **nodo**, en cambio, sí puede describir sus propias relaciones y distinciones sustentadas; esto no autoriza a añadirlas a las fichas temáticas. No se exige MSCA ni JF en la definición de un tema.

Ejemplo **ilustrativo de forma**, no resultado del Atlas:

```json
{
  "id": "TH-TRANSFORMATION",
  "title": "Transformación organizativa",
  "description": "Cambios deliberados en prácticas, estructuras o procesos de una organización, incluyendo su preparación y realización.",
  "scope": "Cambio organizativo",
  "etiquetas": [],
  "version": "0.1-example",
  "review_status": "illustrative"
}
```

## 3. Asociación pública independiente: sólo nodo, tema y peso

La proyección pública se guarda **fuera de las fichas**, como registros estrictos con **tres únicos campos**:

```json
[
  {"node_id": "N-01", "theme_id": "TH-TRANSFORMATION", "weight": 0.6},
  {"node_id": "N-01", "theme_id": "TH-DIAGNOSTIC", "weight": 0.4},
  {"node_id": "N-02", "theme_id": "TH-DIAGNOSTIC", "weight": 1.0}
]
```

**Invariante absoluta de toda asignación publicada:** para cada nodo `n` incluido en una proyección temática completa, **Σₜ peso(n,t) = 1**. Cada peso es numérico, finito y estrictamente positivo, como máximo 1. No hay duplicados `(node_id, theme_id)` ni campos `role`, `reason`, `rationale`, `evidence`, `confidence`, `item_refs` u otros; *el peso no es probabilidad de verdad ni fuerza causal*. Un nodo con un tema lleva peso 1; con varios temas se **reparte** el 1. «Principal» y «secundario» no producen un 1 adicional.

**Cobertura sin falsear el total:** si un nodo aún no ha completado la adjudicación temática, no publicar una asociación parcial de él; marcarlo **pendiente fuera de esta tabla**, en el manifiesto/estado de proceso. La proyección señala explícitamente su conjunto de nodos clasificados, su versión y el corte del grafo al que corresponde. El validador comprueba que cada nodo declarado clasificado tiene su **lista completa** con suma 1; no presenta ausencias de clasificación como peso 0 o como tema inventado. La meta posterior es cubrir todo nodo publicable, sin adelantar asignaciones.

La ficha pública del tema y la tabla pública de pesos contienen **datos de lectura mínimos** para que los bots externos continúen explorando el grafo, en lugar de heredar un relato previo de por qué «se relaciona» todo.

## 4. Deliberación de jueces: repositorio/tabla **internos, no públicos**

Se estudia una **tabla de adjudicación separada y de acceso restringido**. Para cada propuesta de `(node_id, theme_id)` conserva: revisión exacta del grafo y del diccionario; los recorridos y clústeres **ya analizados** que se consultaron; dictámenes iniciales **independientes** de varios jueces; alternativas, objeciones y desacuerdos; intercambio de argumentos posterior a los dictámenes; ajuste de ponderaciones; decisión, responsable y fecha; e historial de revisiones. Esas razones **no se copian** a la tabla pública ni a la ficha temática.

El flujo es: análisis previo del grafo → propuestas de asignación → dictámenes independientes sellados → **debate contrastado entre jueces** → resolución documentada → normalización por nodo y validación → publicación de **sólo** los tres campos. La unanimidad numérica no sustituye evidencia. Cuando no hay resolución suficiente, el nodo permanece sin proyección pública, nunca con suma inferior a 1.

El [perfil existente de siete jueces](./SEVEN_JUDGE_ABCD_JF_REVIEW_PROFILE_v0.1.md) se aplica a recorridos situados; puede informar el diseño de revisión, pero **no se declara por ello ejecutado un panel temático** ni se reutilizan automáticamente sus veredictos ABCD como etiquetas.

No introducir aquí juicios reales, identidad de jueces, testimonios privados o razones confidenciales: este documento es sólo el **contrato metodológico público** de la separación.

## 5. Relaciones entre temas y estadísticas: **derivadas, separadas y reproducibles**

Después de la clasificación se pueden producir **vistas analíticas**, siempre fuera de las definiciones temáticas y sin originar aristas de nivel 1:

1. **Coasignación:** dos temas aparecen en un mismo nodo, con sus pesos. Esto mide solapamiento taxonómico, **no** demuestra que dos materias estén conectadas causal o funcionalmente.
2. **Interconexión del grafo:** aristas o recorridos verificables conectan nodos adscritos a temas diferentes. Esta salida conserva IDs de aristas/rutas y posicionamientos, dirección, evidencia, revisión, naturaleza candidata o comprobada y límites de cobertura. **No** se infiere sólo por coincidencia de etiquetas.
3. **Estadísticas de investigación:** cantidad de ítems, nodos, aristas y recorridos; cobertura temática (clasificados, pendientes); distribución de temas por nodo; distribución y concentración de pesos; solapamientos, conectividad intra/intertema, puentes, componentes y sensibilidad de resultados ante cambios de posición/umbral. Separar métricas observadas de inferencias o hipótesis.

Cada informe estadístico registra **ID/revisión/hash o commit del grafo fuente, versión del diccionario, versión de la asignación, población efectiva, fecha, algoritmo/definición de cada métrica y resultados verificables**. Los desacuerdos o la tasa de revisión pueden informarse **agregados** sin exponer el debate privado. No inventar métricas ni presentar una cobertura parcial como totalidad.

## 6. Consumo posterior y prohibiciones de retroalimentación

Una vista MSCA o una lámina cartográfica por agente puede usar pesos temáticos **como índice de entrada**, pero debe recuperar los **nodos, aristas, recorridos y fuentes** que sustentan cada posicionamiento y recorrer los hilos pertinentes hasta sus D reales o declarar cortes parciales. El tema **no es** un Objective Envelope, un clúster, un recorrido, una prueba de suficiencia de control ni un atajo que sustituya la exploración.

**Prueba de aceptación:** ficha temática descriptiva sin relaciones precocinadas; tabla mínima de ternas; cada nodo clasificado suma exactamente 1; asignaciones parciales o con campos explicativos se rechazan; razonamientos de jueces privados; asociaciones entre temas y métricas **derivadas después del grafo**, con procedencia reproducible.
