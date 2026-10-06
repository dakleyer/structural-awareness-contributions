# Revisión de 00M — qué puede sostener esta nota y qué falta

**VNext única de 00M.** Revisión realizada por Codex el 6 de octubre de 2026. Es asistencia de IA identificada; la relectura humana de la cuarta pasada es simulada por el mismo agente. Se conserva intacta la [nota v0.8](./00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md). [Ficha externa](./00M_REVIEW_CARD.md) · [plan de trabajo](../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md).

## Qué dice la nota, en lenguaje corriente

Un resultado puede ser útil y aun así no llevar toda la información que otro necesita para confiar en él. Esta nota propone describir qué produjo un proceso, qué base y opciones de evaluación conoce, qué podría explorar sin saber todavía cómo evaluarlo, y qué efectos quedan fuera de su capacidad de evaluación. Después pregunta cuándo pueden compararse esas descripciones y qué conclusiones permite un resumen de ellas.

La aportación más defendible es **una manera de formular revisiones acotadas**, con condiciones explícitas para conservar lo que importa. La nota no demuestra que cualquier conjunto de agentes componga bien, encuentre una respuesta a tiempo o actúe con autoridad. La diferencia importa: una representación matemática posible es el comienzo del trabajo, no su éxito operacional.

## Instrucciones de Iván y estado

Iván ha pedido continuar completamente el plan: cuatro pasadas distintas por documento, revisiones de evidencia entre documentos y conciliación final, con el contenido y la comprensión humana como prioridad. Autoriza publicar estas revisiones; las modificaciones de la fuente siguen como propuestas antes/después pendientes.

| Pasada | Trabajo efectivamente realizado |
|---|---|
| Fondo y lógica | Realizada para el texto completo de 00M y sus argumentos elementales; no certificado formal de EA. |
| Evidencia y relaciones | Realizada para la función limitada de las seis referencias y la relación con 00N, el README y el mapa de pruebas; los papers completos y toda transferencia a proofs antiguos no están auditados. |
| Edición, estructura y formato | Realizada sobre el Markdown y su notación textual; gráficos/slides se reservan a su propia revisión visual. |
| Legibilidad humana | Relectura simulada realizada, con puntos de pérdida de comprensión descritos abajo; falta contraste independiente con una persona. |
| Conciliación global | Pendiente. |

Estas cuatro entradas son distintas y quedan abiertas a nuevas pasadas cuando cambien evidencia o fuentes. Haberlas realizado con el alcance indicado no convierte la investigación en validada ni cierra sus pendientes.

## Primera pasada — fondo y lógica

**Quién y cómo:** Codex, 6 de octubre de 2026; lectura íntegra de v0.8 y examen separado de definiciones, ejemplos y las inferencias matemáticas de §§4–6.

El argumento funciona mejor cuando se lee en tres niveles. Primero fija roles relativos a un proceso, no una partición universal del mundo. Después declara condiciones para comparar dos preguntas y resumir sus estados. Finalmente reconoce que obtener una calificación nueva requiere información, una correspondencia o un cambio de condiciones. Ninguno de esos pasos autoriza a adivinar lo que quedó fuera.

La distinción B/C es coherente en el texto: una opción que ya puede evaluarse sigue siendo B aunque no se use. C exige una vía de exploración cuyo marco de evaluación no está establecido. D necesita una barrera efectiva para evaluar el efecto relevante; no basta que algo sea externo o no esté controlado. El estado UNKNOWN evita forzar una clasificación cuando ni siquiera hay base para atribuir uno de esos roles. No encontré una necesidad lógica de convertirlos en cuatro porcentajes ni en cuatro conjuntos exhaustivos; el propio texto lo impide.

El paso matemático de §4.1 tiene un argumento válido y limitado. Si todos los estados con el mismo resumen dan la misma respuesta a una pregunta fijada independientemente, esa respuesta define una función sobre los resúmenes posibles. En sentido inverso, si la respuesta es una función del resumen, dos resúmenes iguales no pueden producir respuestas distintas. Es una condición de suficiencia para esa pregunta. Conservar todos los datos también la cumple: no demuestra compresión ni ahorro.

En §4.2, distinguir el conjunto exacto de respuestas compatibles de una aproximación conservadora es esencial. Una aproximación puede conservar respuestas que ningún estado real del modelo produce. Incluso si la aproximación deja una única respuesta, hace falta justificar que existe un estado compatible; si el conjunto exacto es vacío, esa única respuesta no acredita certeza. La advertencia está ya en el texto, pero merece un ejemplo para que el lector no pierda esa condición.

El ejemplo de veinte puertas es correcto bajo sus premisas: sumar veinte límites válidos de dos a tres minutos da cuarenta a sesenta minutos. No necesita independencia estadística para sumar esos límites. Sí necesita que el límite sea aplicable a cada puerta y que se respete lo excluido —viaje y preparación—. No estima gatos, beneficios ni permiso para inspeccionar. Esa separación sostiene la modestia del ejemplo.

En §6.2, el límite de la diferencia entre intervalos también es válido: nueva cota inferior menos antigua superior, y nueva superior menos antigua inferior. Si la relación entre valores permite una cota más estrecha, la presentada puede ser conservadora. Un intervalo que toca cero no demuestra cambio estrictamente positivo o negativo. Tampoco es una utilidad global de A/B/C/D.

**Pendiente de fondo:** para una arquitectura concreta faltan un perfil implementable, una correspondencia de alcances justificada, una abstracción útil y comprobable, y una revisión conjunta de costo, plazo y autoridad. La propia nota los mantiene abiertos; no hay razón para convertir su plausibilidad en un teorema de funcionamiento del corpus.

## Segunda pasada — evidencia y relaciones

**Quién y cómo:** Codex, 6 de octubre de 2026; contraste de las afirmaciones asignadas a R1–R6 con fuentes primarias y contraste textual con 00N, README y A17. Se inspeccionaron pasajes pertinentes, abstracts/registro de autores y tablas; no se afirma lectura integral o reproducción de todos los papers.

| Fuente | Qué se comprobó y qué permite afirmar |
|---|---|
| [Cockett y Lack](https://cspages.ucalgary.ca/~robin/FMCS/FMCS_06/RestrictionsI.pdf) | Ofrece una teoría de mapas parciales. No justifica que dos conceptos del mundo real sean comparables ni construye la categoría de EA. |
| [Cousot y Cousot, página de autores](https://www.di.ens.fr/~cousot/COUSOTpapers/POPL77.shtml) | La abstracción puede conservar propiedades relevantes con información incompleta. El precedente no suministra una abstracción sound para cualquier mensaje de un agente. |
| [Shapiro y colaboradores](https://www.lip6.fr/Marc.Shapiro/papers/2011/CRDTs_SSS-2011.pdf) | La convergencia tiene supuestos específicos, incluido el modelo no bizantino. No prueba verdad ni independencia de fuentes. El ejemplo de dos reportes con un solo origen no queda resuelto por idempotencia. |
| [Alon, Matias y Szegedy, copia de autor accesible](https://www.math.tau.ac.il/~nogaa/PDFS/amsz4.pdf) | Trata ahorro/límites de espacio para estadísticas concretas en streams. No es un límite de comunicación general para EA. La ruta original falló en esta consulta; esta alternativa abrió. Eso no demuestra por sí solo que el servidor original esté roto para todos. |
| [Braverman y colaboradores](https://arxiv.org/abs/1506.07216) | Estudia error y comunicación en modelos de estimación específicos. No es fuente de una validación EA ni del argumento elemental de dos estados indistinguibles. |
| [NASA, tabla TRL](https://nodis3.gsfc.nasa.gov/displayDir.cfm?Internal_ID=N_PR_7123_001D_&page_name=AppendixE) | Sustenta el uso limitado de vocabulario de madurez. El documento no recibe un nivel TRL por citarla. |

El soporte asignado a cada referencia es razonablemente acotado. La fortaleza de esta sección está en decir qué **no** se transfiere. Las seis referencias no forman juntas una prueba de EA, y no deben usarse así en otro documento.

### Revisión cruzada: 00M → 00N

[00N §3.2–§3.3](./00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md#32-three-conditions-connect-mathematical-plausibility-to-functional-plausibility) conserva la frontera. Pide una distinción observable que importe, composición que la preserve y uso dentro de una respuesta legítima y viable. 00N reconoce apoyo directo sobre partes de T1/T2, con costo/plazo T4 y respuesta autorizada T3 todavía por demostrar. No toma la equivalencia de §4.1 como cumplimiento de Requirements.

El lector debe poder seguir una frase sencilla: **00M dice qué tendría que conservar un resumen; 00N pregunta si conservarlo serviría para una función útil y bajo qué condiciones.** La ganancia informativa no equivale a una mejora de decisión. Esta lectura también se registra en [00N VNext](./00N_VNext.md), sin duplicar una segunda nota de 00M.

### Revisión cruzada: 00M → README → pruebas anteriores

El [README](../../../architectural-contributions/ecosystem-positioning/README.md) utiliza 00M §1 como significado actual de A/B/C/D. [A17](./00K_A17_DOCUMENTATION_REPRODUCIBILITY_AND_PROOF_MAP_v0.1.md) conserva que los proofs y fixtures tienen su propio vocabulario fuente y que el enlace a la definición nueva no demuestra transferencia. Esta frontera debe seguir visible al presentar el corpus: los resultados antiguos no quedan revalidados por añadir una cita a 00M.

Se registra el mismo problema de lectura en [README VNext](../../../architectural-contributions/ecosystem-positioning/README_VNext.md). Falta la conciliación de las traducciones semánticas de todos los proofs: esta revisión no la da por cerrada.


### Procedencia: por qué dos hashes de 00M no son iguales

Se comprobó el payload de la publicación del 2 de octubre: [commit d855f8d](https://github.com/dakleyer/structural-awareness-contributions/commit/d855f8d46a1b62eb2936f16faeb3c022835786b1) contiene el texto cuyo SHA-256 es `37ac24628214a711caf083d7dc7bf0714ced8e7109259f00c5bd5e0bdd772377`, exactamente el del registro de publicación. El texto actual tiene SHA-256 `7af7ffb02afab0bd9049a942cb8924ed4e61290600c3950381e3655277c39dbd`.

La diferencia queda explicada por [la alineación semántica posterior, commit 135d8ff](https://github.com/dakleyer/structural-awareness-contributions/commit/135d8ff8b2d953270426f5cda0e77402ed0f81e7): añadió la nota de adopción y el ancla canónica y reformuló tres pasajes que aún decían “proposed”. No se deduce una pérdida de custodia de esa diferencia. Sí hay una enseñanza para la lectura: el hash del paquete original y el de la edición pública después de la alineación son estados distintos, aunque el filename siga diciendo v0.8. La cita debe identificar cuál utiliza. 00N conserva el hash del registro de publicación.

Esta comprobación usa fuentes históricas exactas, no reconstruye un predecessor. No revalida pruebas antiguas ni recalcula el manifest histórico. La observación se devuelve también al README VNext para mantener la traza entre semántica y evidencia.

## Tercera pasada — edición, estructura y formato

**Quién y cómo:** Codex, 6 de octubre de 2026; segunda lectura dirigida a orden, tablas, notación y ubicación de aclaraciones en el Markdown.

La organización tiene una ruta razonable: definiciones, gatos, tareas matemáticas, resumen, puertas y requalification. Las tablas de símbolos y de movimientos evitan tratar las fórmulas como decoración. La notación distingue estados fuente, resumen y respuesta, y los explicadores en palabras ayudan a continuar sin dominar teoría de categorías.

La dificultad editorial está en la densidad de §1. La reserva caracterizada de B mezcla soporte de A y evaluación de opciones futuras; el texto explica la unión, pero el lector tiene que retenerla durante varias páginas antes del ejemplo completo. Una lectura corta al comienzo puede orientar esa distinción sin reemplazar la definición técnica. También conviene colocar el ejemplo de consistencia vacía inmediatamente junto a §4.2: una aclaración lejana de §7 llega tarde para esa inferencia.

El título no menciona EA/EP explícitamente aunque la apertura sí. No es necesariamente un defecto: facilita la lectura de la pregunta, pero una cita fuera de contexto necesita retener subtítulo/autor/versión. Las referencias se citan con códigos locales R1–R6, algo habitual en un artículo; no es preciso añadir más etiquetas a cada oración.

La URL alternativa de R4 merece una propuesta de ruta y fecha de consulta. Es mantenimiento de acceso, no modificación de un resultado. No se propone renombrar el archivo, normalizar la fuente ni alterar las figuras. Esta pasada inspecciona estructura textual; falta revisar el render de SVG y las exportaciones como artefactos propios.

## Cuarta pasada — legibilidad y comprensión humana

**Quién y cómo:** Codex, 6 de octubre de 2026; relectura simulada desde cuatro preguntas de una persona nueva. No es una prueba con un lector independiente.

**¿Qué problema se plantea?** Se entiende en la apertura: revisar una decisión con información parcial sin reunir todo. Sin embargo, “partial metadata” puede sugerir un producto o protocolo ya definido. Conviene explicar que son condiciones y ejemplos para futuras implementaciones.

**¿Qué aporta A/B/C/D?** Los gatos ayudan a distinguir resultado, reserva evaluable, exploración y barrera. El lector puede perderse si interpreta “exploitation” como explotación comercial o si entiende D como imposibilidad absoluta de conocer. §1.7 y §1.4 lo corrigen; una orientación corta antes de esa sección reduciría el rodeo.

**¿Qué queda demostrado?** Los argumentos elementales de resumen suficiente, cotas de esfuerzo y límites de indistinguibilidad se pueden seguir. Las referencias muestran herramientas existentes, no una arquitectura integrada ya construida. La nota lo admite, pero esa diferencia debe mantenerse al volver al README.

**¿Adónde debe ir después?** La apertura remite a un “companion note” sin enlace directo en esa frase. El camino está en el README, pero la nota puede circular por sí sola. Proponer un enlace a 00N mejora la lectura humana y no necesita inventar otra categoría de documento.

El resultado de esta pasada es una orientación concreta: conservar la precisión del artículo, añadir una explicación corta y un siguiente paso claro, y no convertirlo en un índice de etiquetas. Las propuestas siguientes están escritas para resolver esos puntos de lectura.

## Conversación y pendientes

Una persona o un auditor distinto podrá responder a cualquiera de estas lecturas citando el pasaje y la razón. La misma persona o el mismo agente podrá repetir una pasada con otra pregunta. No se fabrican varias firmas para presentar independencia.

Quedan abiertos el contraste con lectores reales, las figuras/exportaciones, la construcción de un perfil y la transferencia semántica a las pruebas antiguas. No son defectos automáticamente refutatorios; son condiciones que deben mantenerse visibles antes de formular una afirmación más fuerte.

## Propuestas antes/después — aún no incorporadas

Todas se preparan bajo la instrucción de Iván de seguir el plan humano. La decisión de incorporarlas a 00M permanece pendiente; su fuente no se modifica.

### Orientar la lectura y señalar el siguiente paso

**Lugar:** oración única de §1 que alude al companion note.

**Texto antes**

```text
This vocabulary is specific to the present proposal; its connection to established exploration–exploitation literature is discussed in the companion note.
```

**Texto después**

```markdown
This vocabulary is specific to the present proposal; its connection to established exploration–exploitation literature is discussed in [the companion note, 00N](./00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md). Read 00N next for the functional question: when could these representations help a receiving decision, and which timing, authority and cost obligations still have to be met?
```

**Por qué:** la nota puede leerse sin pasar por el README. El enlace conserva la diferencia entre representación y funcionamiento. **Pendiente:** comprobar el lugar más claro para el siguiente paso en una edición de autor. No aplicado.

### Un ejemplo que evita una falsa certeza

**Lugar:** §4.2, oración única sobre evidencia que no encaja en estados admitidos.

**Texto antes**

```text
If the evidence fits no admitted state, that indicates inconsistency or model inadequacy, not certainty.
```

**Texto después**

```text
If the evidence fits no admitted state, that indicates inconsistency or model inadequacy, not certainty. For example, a model admitting only red and blue observations has no compatible state for a green observation. A conservative approximation may still retain one candidate answer; that does not make the answer supported. Before using a singleton approximation as a determination, the review must also justify that a compatible source state exists.
```

**Por qué:** hace visible una condición lógica ya presente, sin atribuir un algoritmo para decidir consistencia. **Pendiente:** revisar que el ejemplo no se lea como obligación de enumerar todos los estados. No aplicado.

### Facilitar el acceso a R4

**Texto antes**

```text
- R4: https://www.tau.ac.il/~nogaa/PDFS/amsz4.pdf
```

**Texto después**

```markdown
- R4: [author-hosted full text](https://www.math.tau.ac.il/~nogaa/PDFS/amsz4.pdf); [journal publication record](https://cris.tau.ac.il/en/publications/the-space-complexity-of-approximating-the-frequency-moments/). Access checked 6 October 2026; the copy's internal date and the journal publication date should not be conflated.
```

**Por qué:** la ruta original no se abrió con la herramienta usada; la copia alternativa y el registro de publicación sí se localizaron. No se declara rota universalmente la ruta original ni se cambia bibliografía sin revisar la correspondencia. No aplicado.

## Referencia de la fuente revisada

Fuente: commit `2f72751fef47d9f4cf1d270a1f7fa498a26f5760`, blob `c97353991117f63983feba24bf8344cf52e9f1e7`, versión v0.8. Se usa ficha externa porque el registro de publicación conserva hashes de 00M/00N. El texto canónico y esos hashes permanecen intactos. Esta referencia técnica identifica la revisión; no reemplaza las explicaciones anteriores.


---

## Quinta pasada — investigación externa, diferencial y reutilización

**Instrucción de Iván, 6 de octubre de 2026. Estado: contraste específico pendiente.** Esta quinta pasada se realiza después de las cuatro y queda dentro de esta misma VNext. No se crea otro expediente ni se incorporan propuestas a la fuente por esta anotación.

**Pregunta de este documento:** Buscar formalizaciones alternativas de abstracción, composición, correspondencia de scopes y calificación parcial. Identificar construcciones reutilizables y cuáles de sus premisas y preguntas son distintas de los roles A/B/C/D de este documento.

Se fijarán trabajos primarios de FG-TIDA y de otras líneas relevantes, incluidos antecedentes y actualizaciones posteriores, con autor, versión, fecha y alcance realmente leído. Aquí se justificará qué coincide, qué diferencia podría sostenerse y qué pieza concreta conviene reutilizar, con sus condiciones de atribución, adaptación y compatibilidad.

El [mapa externo preparatorio](../../../governance/review/EP_EXTERNAL_RESEARCH_REVIEW_2026-10-06.md) aporta fuentes iniciales; no completa esta pasada. El [plan 1.6](../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#quinta-pasada--trabajos-externos-diferencial-y-reutilización) gobierna método y cierre. Las cuatro lecturas previas mantienen sus estados reales y se reabren si aparece evidencia que las afecte. Codex, mismo asistente de IA; anotación de alcance, sin independencia externa.


### Vecino formal identificado — lectura preparatoria

**Auditoría realizada por Codex, 6 de octubre de 2026. Alcance parcial:** pasajes del [preprint de Louck v1](https://arxiv.org/html/2606.24322v1), sin reproducir su artefacto.

La construcción conserva origen y autoridad a través de memoria transformada. Depende de monitor, canales y atribución de valores; la prueba acotada no equivale a una demostración universal. Su [código](https://github.com/yedidel/mem-inv-bench) es candidato a inspección, no una pieza ya admitida.

**Juicio para 00M:** la existencia de esa realización invita a comparar operaciones y premisas, pero no hace equivalentes sus etiquetas de integridad y nuestros roles funcionales A/B/C/D. Se estudiará qué puede aprovecharse y qué claims de conservación ya tienen precedente; no se afirma novedad ni se trasladan sus resultados al corpus.


---

## Evidencia del contraste de publicación ya realizado — ahora pública

**Auditoría realizada por Codex, 6 de octubre de 2026; conciliación de publicación.** Se incorpora el [resultado de comparación de procedencia](../../../governance/review/publication-reconciliation-2026-10-06/00M_provenance_comparison.json) preparado durante la revisión anterior.

El authored payload de publicación y la lectura posterior no son idénticos: la comparación conserva hashes y los cambios exactos ya identificados. La nota de adopción/enlace y las precisiones de estado pertenecen a la época posterior; el hash histórico se mantiene válido para su fuente. No se modifica un manifest ni se reconstruye el original.

Esta publicación hace accesible la evidencia del examen; no repite una auditoría independiente ni completa el traslado de pruebas antiguas a la semántica actual. El cuerpo de 00M, su VNext anterior y las propuestas permanecen conservados.


---

## Sexta pasada unificadora — preparación y continuidad

**Instrucción de Iván, 6 de octubre de 2026. Preparación registrada por Codex, mismo asistente de IA. Estado: pendiente de lanzamiento después de las cinco pasadas del corpus.** Esta anotación organiza el trabajo futuro; no declara una auditoría unificadora realizada ni cambia el estado de las lecturas anteriores.

**Pregunta de consolidación de este documento:** Comprobar la fidelidad entre los roles relativos al proceso de 00M, las hipótesis de 00N, requisitos, interfaces y pruebas históricas; no transferir un resultado a una definición distinta por conservar su nombre.

Los hallazgos concretos se comentarán aquí y en las VNext de los documentos relacionados, conservando respuestas y desacuerdos. Se cotejarán las propuestas con la fuente actual y sus consumidores antes de presentar candidatos consolidados antes/después. La [sexta pasada del plan](../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#sexta-pasada-unificadora-y-consolidación) fija el lanzamiento y el método. Se preservan fuente, historia y decisión de Iván para incorporar cambios.
