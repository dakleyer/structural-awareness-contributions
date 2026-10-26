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


---

## Prioridades del plan de cambios — revisión del corte

**Revisión realizada por Codex, 6 octubre de 2026, mismo asistente de IA.** Se revisan las auditorías y propuestas ya registradas para valorar impacto esperado, riesgo y esfuerzo. La fuente pública del corte es `7500dd5ee05c1a5052a28d35a8cefaf2c530707f`; los viejos y pares anteriores permanecen íntegros. Esta revisión no completa las pasadas pendientes ni la sexta.

El [plan 1.11](../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#prioridad-de-cada-cambio--impacto-riesgo-y-esfuerzo) explica los criterios y el [listado completo](../../../governance/review/change-priorities-2026-10-06/priorities.json) conserva las fuentes y los pares. La prioridad sirve para preparar tandas de decisión; la incorporación depende de Iván y de las comprobaciones indicadas.


## Recepción de 01J y significado de D — contraste cruzado

**Auditoría realizada por Codex, mismo asistente de IA, 6 de octubre de 2026.** Se leyó completo01J y se cotejó con00M§§1.4–1.5 y su ejemplo de telemetría. La definición propietaria no se propone cambiar: §1.4/1.5 ya distingue barrera efectiva, reserva evaluable, exploración y UNKNOWN sin clasificación. El conflicto está en el consumidor genérico 01J, mientras su ejemplo ya conserva el significado.

[01J VNext](01J_VNext.md) conserva el relato, contraejemplos propios y pares68/69/70, con impactoAlto/riesgoAlto/esfuerzoMedio/prioridadPrimera. Misma regla en prosa, síntesis y esquema; cotejar campos materiales y consumidores antes de decidir. No se aplicó ninguna propuesta ni se transformó la relectura en auditoría independiente. Quinta específica de01J realizada en alcance declarado; segunda material y sexta global permanecen abiertas. [Evidencia](../../../governance/review/Signalling-full-2026-10-06/evidence.json).


---

## Revisión a fondo de los planes de cambio — 6 octubre 2026

**Evaluación realizada por Codex, mismo asistente de IA, para que una persona pueda decidir.** Se revisan el plan, sus motivos de auditoría, pares literales, impacto, riesgo, esfuerzo y dependencias; no es la sexta pasada científica global ni acredita el cierre de las cinco. Fuente de este cotejo: commit `03db21016d6a0831a43d7a99d3640854ab549777`, [documento propietario](00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md), blob `c97353991117f63983feba24bf8344cf52e9f1e7`. Los registros anteriores y sus viejos completos permanecen íntegros.

La valoración actual distingue una mejora documental de una modificación conceptual o de contrato. **Candidato para revisión documental significa preparado para leer y decidir, no autorizado para incorporar.** Los originales siguen en sólo lectura; no se ejecuta ninguno de estos pares.


[Visión conjunta y tandas en EP README VNext](../../../architectural-contributions/ecosystem-positioning/README_VNext.md#revisión-a-fondo-de-los-planes-de-cambio--6-octubre-2026). Mantener tres niveles de README, fuentes congeladas, resultados y binarios. Reorganización, nueva campaña, experimentos e incorporación canónica permanecen fuera de esta entrega.

**Revisión cruzada de la nueva alternativa 71:** 71 resume el papel de la calificación para un lector del README. Concuerda con 00M §4.1 si conserva pregunta, scope y suficiencia condicional; no convierte una lectura nueva en prueba de resultados anteriores. El par nuevo no cambia 00M ni su evidencia. [Viejo y propuesto completos en EP](../../../architectural-contributions/ecosystem-positioning/README_VNext.md#revisión-a-fondo-de-los-planes-de-cambio--6-octubre-2026).


---

## Relación material con posicionamiento local e interfaz EA/MSCA — 6 octubre 2026

**Auditoría cruzada realizada por Codex, mismo asistente.** Fuente de esta ampliación: `fa2c411c810950fb94924caae38938c52dfd5014`;01H § §1–9,01B § §1–8 y 01D § §1–7 completos, ArticleII completo como procedencia; no experimentos o audiencia humana independiente.

Se leyó completo 01B v0.2. Su cabecera y tabla §4 conservan A como resultado funcional, pero el párrafo que distingue x deA aún dice «situated assertion/scope». El candidato 72 mantiene la distinción devariables y sustituye sólo ese parentético por el resultado funcional del proceso. Contexto protegido, no error runtime universal; impacto/riesgo/esfuerzoMedio y decisión opcional.01H § §2/2.1 ya usa la lectura actual. Ninguna prueba antigua ni la semántica adoptada de 00M se cambia.

La explicación de origen y los límites están en [01H VNext](01H_VNext.md) y [01B VNext](01B_VNext.md). La segunda pasada se amplía en esta relación; fuentes urbanas/funcionales/perfiles pendientes siguen visibles. Un enlace compatible no establece ejecución. Se mantienen los originales y las conversaciones anteriores; quinta/sexta mantienen su estado real.


---

## Relación material con funciones y taxonomía — 6 octubre 2026

**Codex, mismo asistente, contraste nuevo de evidencia.** Fuente `f7d8ed0846b301617197ade855d5237cbd2280f9`;03partes 1–3 completas,ArticleIVpartes 1–2 completas como procedencia y Foundation 1.1A/ § §2/3.4/3.5 focales. No otra firma independiente ni nueva ejecución.

Las notas actuales de 03remiten a 00M alinterpretar rótulos históricos dentro/fuera de ventana; no se renombra elmapaI/O/Type. F2/APQ conserva vía suficiente distinta de mensaje válido; F5 noinfieredeindependencia por diversidad detransportes. La nueva Foundation 1.1AconservaA probabilístico legítimo yrework separado,pero debe leer los casos Type 1/2 concausalidad y scope:73propone no exigir ampliación. NingúnA/B/C/D oproofse adopta de nuevoporesta lectura.

Elorigen delcontraste está en [03 Functional VNext](03_FUNCTIONAL_VNext.md) y [Foundation VNext](01_FOUNDATIONAL_VNext.md). Allí se conserva laversión/fuente,explicación humana ylímites. Las demás lecturas previas no se repiten como si fueran nuevas; quinta ysexta mantienen sus estados reales. Canon,programas y resultados intactos.

---

## Foundation integrada completa — alcance del proceso y del observador

**6 octubre 2026, Codex, mismo asistente; `409bfa9eff2b3e24e7350021db9e587861583de8`.** Foundation v0.5 completa, 135.021 caracteres, cotejada con 00M §1 actual. [Origen y límites](01_FOUNDATIONAL_VNext.md).

Foundation §16 distingue campo representado de ventana activa, y su diccionario conserva sujeto/proposición/dominio. Eso concuerda con fijar productor, función, pregunta, scope, capacidad y tiempo en 00M: el resultado de un monitor puede ser A de ese proceso sin tornar evaluable D del receptor. No se reconstruye un reparto porcentual ni se actualizan pruebas antiguas con nuevas definiciones.

La quinta de Foundation añade un contraste útil para una lectura abreviada de §1.7: procesar información ya disponible puede mejorar su aprovechamiento por un observador limitado; no recuperar información descartada. Utilidad del resultado y preservación de sus límites se examinan por separado. No transforma C en reserva B calculada ni un indicator en capacidad efectiva; no añade una métrica universal.

73 sigue siendo propuesta de exposición/taxonomía en su fuente, no una modificación de A/B/C/D. Se cumple la lectura integral del sucesor pero faltan derivaciones y consumidores; no se cierra una prueba o H06 por esta relación. Ningún texto original se modifica.

---

## Fuentes, receptores y cambios del corpus — 12 octubre 2026

**Codex, mismo asistente; `17b597bf91acb0f37daebc716e8f23f65daa23eb`.** El resultado de un monitor sobre la falta de justificación puede ser A de ese proceso sin establecer B/C del objeto o eliminar D. HF v0.6 codifica un diagnóstico confiable estipulado y conserva fallos con observer silencioso o deshabilitado. No demuestra autocertificación, universalidad o mejor coste. Se mantiene el contraejemplo del peer fuerte.

Los datos y límites están en [EP VNext](../../../architectural-contributions/ecosystem-positioning/README_VNext.md#nueva-revisión-integral-de-cambios-y-consistencia--12-octubre-2026). Los 49 pares pendientes mantienen su viejo localizado; eso no prueba compatibilidad o cierre científico. Sin otra firma independiente, experimentos o cambios a originales.


---

<a id="ola2-cambio-10"></a>



## Third independent source review — 00M branch correction, 14 October 2026

The isolated source reviewer has sealed the first bounded judgement below before opening previous audit bodies. It finds a justified correction in an internal 00M branch: finite termination does not establish delivery within an operational deadline. It recommends preserving that correction, with no current replacement candidate. This is a partial source judgement, not completion of 00M, its downstream integrations, the restoration/organization plan or the whole corpus.

The coordinator verified the three authentic Git blobs and commit ancestry. These are internal Contributions branch versions, not a main deletion or an adopted successor inferred from their filenames. The complete old/successor paragraphs below are historical evidence; they are **not** a new before/proposed-after pair against the current canonical source.

| Internal version | Exact source | Git blob | Relationship to the fixed main cut |
|---|---|---|---|
| `4d201926cacc` | [Full source](https://github.com/dakleyer/structural-awareness-contributions/blob/4d201926caccc64886334bab615ab5ede5d5418c/research/ecosystem-awareness/baseline/00M_CANONICAL_ABCD_SEMANTICS_AND_REQUALIFICATION_FEASIBILITY_v0.1.md) | `52a63de27c978c0417ce53026980224f23c30e52` | Branch work; not in main ancestry |
| `ef177d3a928f` | [Full source](https://github.com/dakleyer/structural-awareness-contributions/blob/ef177d3a928f7aef75ab8ff15e46e414ecb0c6e8/research/ecosystem-awareness/baseline/00M_CANONICAL_ABCD_SEMANTICS_AND_REQUALIFICATION_FEASIBILITY_v0.1.md) | `5e147aa13d668dcbe1f4218c14d38f28e9880730` | Branch work; not in main ancestry |
| `f5932a8f5f1b` | [Full source](https://github.com/dakleyer/structural-awareness-contributions/blob/f5932a8f5f1b7c75edf18dc66882f0633c01d778/research/ecosystem-awareness/baseline/00M_CANONICAL_ABCD_SEMANTICS_AND_REQUALIFICATION_FEASIBILITY_v0.1.md) | `b134301a7e6fdeb76b1eaefb5f83fc70701c3eb4` | Branch work; not in main ancestry |

First judgement sealed at `2026-10-14T20:45:10.903294+00:00`. Markdown SHA-256 `897da242f2621fb356a57abddd23e1881afa25028f7a8e3391d88876c15c29e9`; accompanying source/reading/exposure snapshot SHA-256 `f68001b1d25cf4f72c916d5fea624877b7e6c7d4137f82a6f0e25d079ba11957`. The original sealed private records remain immutable. The public source judgement follows verbatim; private operational records are not copied into the corpus. The coordinator's authentication is a custody check, not a second independent source review.

<details>
<summary>Sealed first source judgement and its own plan — full text</summary>

# First scoped judgement: branch finite termination correction

Sealed UTC: 2026-10-14T20:45:10.903294+00:00

This is an immutable first judgement on an internal branch correction. The larger source cohort and corpus review remain incomplete.

The three original 00M semantic/feasibility revisions are branch work, not main-ancestry history. Their actual parent chain is recorded in the JSON. No rename, main deletion or main acceptance is inferred from similar dates or titles.

Disposition: **justified correction/supersession**. A finite input with decidable compatibility and finite comparisons admits termination; that fact supplies no useful-response elapsed-time bound. The revision retains the constructive route and states what its assumptions do not establish.

Complete old paragraph (`52a63de27c978c0417ce53026980224f23c30e52`, section 3):

This is a **constructive existence witness**: finite typed records, partial translations, lineage tracking and bounded comparison admit a terminating implementation for a declared finite input and response budget. It does **not** claim a universal matching algorithm, a complete Ω, an optimal decision, a probability for C/D or positive net value in a deployment. On a given implementation, semantic mapping, privacy, metadata capture, adversarial sources and processing may cost more than the warning is worth.

Complete successor paragraph (`5e147aa13d668dcbe1f4218c14d38f28e9880730`, section 3):

This is a **conditional constructive witness**: finite typed records, supplied decidable partial translations, lineage tracking and a finite comparison rule admit a terminating implementation. Finite termination alone does **not** establish that the result arrives within an operational deadline. Nor does the construction supply the semantic mappings or materiality rule, a universal matching algorithm, a complete Ω, an optimal decision, a probability for C/D or positive net value in a deployment. Semantic mapping, privacy, metadata capture, adversarial sources and processing may cost more than the warning is worth.

Plan: preserve the authentic branch history and the corrected limitation. No current edit is justified by this internal correction; there is no fabricated replacement candidate. Impact Medium, risk Low, effort Low for interpreting this correction. The benefit is preventing a termination argument from becoming a deadline-feasibility claim. The material risk is overextending this limited judgement to unexamined receivers. Broader DDS integration effort remains unestimated.

The original document’s section 7 reconciliation claims are disclosed source assertions, still untested against the actual interfaces, mapping cases and proofs. Main-source compatibility is not proof of whole reception. Read and exposure ledgers are frozen in the accompanying JSON.


</details>


## Third independent source review — first current-text reading, 14 October 2026

The following is the isolated reviewer's own source-first account from its first execution boundary, preserved before continuation. Previous audit bodies were not opened. This is a **partial documentary reading**, not completion of this logical document, its historical/receiver integrations or the entire restoration/organization plan. The full first report is held unchanged under custody, SHA-256 `639141a6f7f283ec024fc59ce3847184dcb0a78045d776434cb4394e16cf3d4e`. Continuation uses the same isolated session and its own records; the coordinator supplies no previous findings.

### Source reading reported by the isolated reviewer

00M v0.8 ownsthe adopted A/B/C/D vocabulary while its mathematical argument remains research. A is the actual functional result, which can be probabilistic. B preserves established support, known limitations and characterized evaluation reserve. C requires grounds for an uncharacterized exploration avenue. D concerns a material effect beyond this process's effective evaluation routes; monitoring an associated indicator does not evaluate that effect. UNKNOWN is lack of grounds for assignment, not a forced C/D label. These components are relative to producer, function, question, capability, scope and time, not a closed partition or four percentages.

The note's exact sufficiency implication ranges over the modeled profile class: equal summaries must imply equal independently specified review answers. Factorization does not supply computability, compression or net economy. The compatible-answer set and its sound superset are explicitly distinct; a nonempty approximation need not prove the exact set nonempty. The union counterexample retains two attributed declarations while rejecting the inference that they provide independent originating evidence. The twenty-door example gives 40–60 additive minutes only under compatible scope/method and excluding travel/setup; it establishes neither cat population nor permission. Interval difference supports only a property-specific sign. Identical metadata cannot universally distinguish disagreeing hidden targets, including under identical randomized output laws. These are coherent bounded documentary claims; external paper support and profile implementation remain unverified.

Coordinator's scope clarification: the reviewer's use of "adopted" describes the current source's vocabulary and its explicit authorial adoption statement. This partial reading has not established the procedural authority of every historic adoption or the reception of all branch material.

For the source-to-functional-conditions relationship, the paired first account is in [00N VNext](./00N_VNext.md#third-independent-source-review--first-current-text-reading-14-october-2026).


### Restoration and organization at this evidence level

No current replacement is proposed from this partial reading. Full source-history reception and actual contracts, proofs, implementations and downstream readers must still be checked before deciding an omission or destination. The independently sealed 00M branch timing correction is recorded in [00M VNext](./00M_VNext.md#third-independent-source-review--00m-branch-correction-14-october-2026): preserve the justified correction, with no rollback of the older timing implication. The current absence of another justified candidate is unfinished review work, not a claim that no useful restoration exists.

The current note does not apply changes. A warranted incorporation must supply complete current before/proposed after, useful benefit, impact/risk/effort, dependencies and Iván's named wave/passages GO. Current sources, their earlier bodies and negative/comparator evidence remain preserved.


## 01A-A01: causal priority before the 00M plausibility argument — 24 October 2026 (proposal only)

**Reviewer: Codex (AI); instruction from Iván on 24 October 2026.** The upstream [01A-A01 two-hypothesis research note](./01A_A01_MISSION_DRIFT_CAUSAL_PRIORITY_AND_EPISTEMIC_ECONOMY_HYPOTHESES_v0.1_RESEARCH_NOTE.md) proposes **FH-C** (comparatively more unjustified mission drift from *unawareness of material knowledge limits* than from lacking additional object-domain facts) and **FH-E** (a possibly lower-computation means of equivalent mission-pivot qualification using bounded epistemic metadata, despite potentially greater engineering complexity).

**Before:** [00M §4.1](00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) proves a *conditional factorization of independently stated review answers through a summary*, and §4.3 and §7 explicitly withhold computation and net economy conclusions.  
**After (proposed, not written into 00M):** add an upstream reading pointer distinguishing **(i)** substantive truth about a new world-domain mission from **(ii)** the review answer “the available legitimate basis does not establish this mission change.” A small, sound summary may suffice for (ii) without solving (i). FH-E is an **additional empirical cost conjecture**, never a consequence of factorization alone.

**Benefits:** makes the new causal premise, decision-relative math and optional compute economy traceable. **Risks:** circular summary definition, pretending D is enumerable, neglecting costs of metadata creation/freshness or confounding A with raw retrieved facts. **Open evidence:** specify non-circular review function, soundness limits, full compute/resource ledger and matched comparator. [01A source](01A_FOUNDATIONAL_DUAL_ORIGIN_NOTE_v0.1.md) ← [this bridge](./01A_A01_MISSION_DRIFT_CAUSAL_PRIORITY_AND_EPISTEMIC_ECONOMY_HYPOTHESES_v0.1_RESEARCH_NOTE.md) → [00N source](00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md). Source 00M unchanged; proposal awaits a passage-specific GO.


### Editorial adoption and owner reception — 24 October 2026

**Iván's current instruction:** promote FH-C and FH-E as canonical statements of **research hypotheses** and keep each VNext reachable through its own source only. The incorporation is now recorded in the [current integrated Foundation](01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md), the [01A-A01 hypothesis source](./01A_A01_MISSION_DRIFT_CAUSAL_PRIORITY_AND_EPISTEMIC_ECONOMY_HYPOTHESES_v0.1_RESEARCH_NOTE.md), the [corpus README](README.md), the [corpus manifest](CANONICAL_CORPUS_MANIFEST.md) and relevant original source-level reading pointers. Earlier “proposed/not applied” paragraphs above are historical proposal receipts; their editorial promotion is now applied.

**Scientific status unchanged:** FH-C is not validated causal dominance; FH-E is not validated compute saving. No frozen requirements, H1–H6, controlled historical texts or old tests are reinterpreted as proof. Cross-document navigation added in this work points to **source texts** rather than another source's VNext.

## 00M / ACC optional information / UC21 falsification — proposed reception, 26 October 2026

**Source and status:** owner-requested research bridge, NOT a correction to the canonical mathematical note and NOT a claim that 00M §7 now proves general lower cost. The original mathematical plausibility, the finite ACC model and UC21's technological refutation discipline are **three compatible statements of different strengths/scopes**. This cumulative proposal belongs in the sole active 00M VNext; do not create a second 00M shadow.

**Before:** [00M §4](./00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) states exact task-sufficiency by factorization and retains open residual, and §7 stops at plausibility, without resource or engineering advantage. [FH-E](./01A_A01_MISSION_DRIFT_CAUSAL_PRIORITY_AND_EPISTEMIC_ECONOMY_HYPOTHESES_v0.1_RESEARCH_NOTE.md) adds a conditional cost hypothesis.

**After (proposal for future owner-approved incorporation, NOT applied to 00M):** add one scoped research reading pointer to the [ACC / 00M / UC21 bridge](./01I-artifacts/acc-auxiliary-model-v0.1/studies/00m-acc-uc21-bridge-v0.1/README.md). Its *separate* social-model result says that, under **zero incremental cost, optional access, constant rights/response and same objective**, preserving valid qualified Q about B/C/D retains every A-only policy, so the best attainable result **weakly** dominates discarding Q. This is not a proof that a real Q channel costs zero, improves social welfare for all agents, or has a unique EA implementation advantage.

**Third and orthogonal validation object:** the existing [UC21 R0/R1/R2 and DDS test contract](./01I-artifacts/acc-auxiliary-model-v0.1/studies/parametric-economic-toy-v0.1/UC21_DDS_FALSIFIABILITY_CONTRACT.md) and preserved [UC21 Annex R](https://github.com/dakleyer/structural-awareness-contributions/blob/main/governance/preserved-public-snapshots/UC21_aec08fb5_source/contributions/when-controls-work-system-fails/annexes/RECURRENCE_PROTOCOL.md) allow technology-favorable results. A valid PASS for **one preregistered δ** refutes the predicted failure for that δ; it does **not** eliminate the existential search for some other δ unless a complete declared domain is established. An equivalent conventional solution can defeat **a branded or strict comparative** EA claim without refuting the open-world plausibility in 00M.

**Benefit:** explicit, non-circular transitions between mathematical sufficiency, resource-constrained policy inclusion and credible technological falsifiers. **Risks:** quietly replacing general plausibility with a toy, confusing a mathematical inclusion with lower lifecycle cost, confusing R0/R1/R2 with DDS stages, post-hoc changing source gates, or claiming that one defender pass refutes every possible recurrence.

**Owner decision proposed:** review and approve a *single bounded crossreading pointer* in 00M or retain this VNext record only. No 00M semantic paragraphs, H1–H6, UC21 source bytes or frozen DDS evidence are altered by this draft.


---

## 15 octubre 2026 — plausibilidad de asignación de explotación mediante contexto compuesto (propuesta 00M §6.4)

**Estado: propuesta matemática del autor para la única VNext de 00M, NO aplicada al 00M v0.8 publicado.** La definición semántica vigente continúa en [00M §1](./00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md); [00N §§1.2–1.3, 3.6–3.7](./00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md) conserva su desarrollo funcional. Esta ampliación distingue dos problemas que no deben confundirse: (i) el conjunto de composiciones **en principio computables** por un sistema dado; (ii) qué partes **elige explotar** un conjunto de agentes con tiempo, atención y recursos limitados. No es un nuevo teorema de computabilidad ni evidencia de un despliegue EA.

### A. La reserva no explotada es una diferencia de selección, no una nueva clase de computabilidad

Fijados un instante \(t\), una familia de capacidades de agentes \(\mathcal F_{i,t}\), sus contratos de entradas/salidas, permisos y reglas de admisión \(\mathrm{Adm}_t\), podemos definir una envolvente idealizada de composiciones finitas admisibles:

\[
\mathcal K_t=\operatorname{Cl}_{\circ}^{\mathrm{Adm}_t}
 \Bigl(\bigcup_i\mathcal F_{i,t}\Bigr).
\]

Esta **clausura composicional** es una construcción relativa a los contratos realmente admitidos: no afirma que todo programa termine, que conozcamos todas las composiciones posibles, que exista un algoritmo para decidir su equivalencia, ni que su ejecución sea barata o llegue a tiempo. Las transformaciones metamórficas obligan a indexar tanto capacidades como contratos y observaciones por versión y tiempo. Es incorrecto situar algo en C solo porque exceda una máquina aislada si una **composición legítima y caracterizada** ya permite su evaluación dentro del sistema.

Para una familia declarada de preguntas \(Q_t\), sea \(\mathcal R_t\subseteq Q_t\) la porción con método, variables, alcance y elegibilidad **suficientemente caracterizados** para evaluación usando la capacidad disponible. Sea \(\mathcal X_t\subseteq\mathcal R_t\) la selección de evaluaciones efectivamente emprendidas bajo el presupuesto disponible; no toda evaluación emprendida ha de terminar con una respuesta satisfactoria. Los resultados emitidos por su actividad son **A**; el soporte caracterizado, los límites y las oportunidades \(\mathcal R_t\setminus\mathcal X_t\) forman parte de **B**, la reserva de explotación. No se escribe literalmente \(A\subseteq B\): A es el resultado funcional, B su fundamento y reserva; la inclusión correcta es \(\mathcal X_t\subseteq\mathcal R_t\) entre **operaciones/preguntas**, no entre dos salidas del mismo tipo.

C es una **vía de exploración fundada** cuyo marco de evaluación todavía no está caracterizado; no se representa como el complemento calculado \(Q_t\setminus\mathcal R_t\) ni como un inventario cerrado. D representa **efectos potencialmente materiales fuera de la evaluación efectiva** del proceso bajo sus condiciones; la imposibilidad de control no equivale por sí sola a D si el efecto sí puede evaluarse. UNKNOWN se conserva cuando tampoco hay fundamentos para asignar rol. Que exista una frontera relativa a un universo mayor no demuestra que todo sistema posea un C concretamente observado ni que se pueda enumerar D.

### B. Hipótesis no oracular: conservar las posiciones, no decidir lo indecidible

Cada agente entrega su resultado operativo \(A_i\) y, cuando existe fundamento, una descripción contextual \(\mu_i\) de sus bases, reservas, vías de exploración y límites de evaluación. La representación intercambiada puede ser \((A_i,\mu_i)\), pero **\(\mu_i\) no contiene los valores desconocidos de C o D**, no transfiere autoridad y no garantiza que la pregunta original sea decidible. Un mismo canal físico podría transportar ambos; no son **fungibles semánticamente** ante un receptor que solamente entiende el tipo A.

Supongamos que \(\mu_i\) es computable a partir de trazas finitas, contratos y bases ya establecidas por los productores, y que la composición de mensajes es computable. Bajo ese supuesto, una capa EA **no aumenta la clase de funciones parciales computables por el sistema ideal**. Sí puede aumentar la observabilidad efectiva de un receptor que antes veía únicamente los \(A_i\), porque se evita descartar cualificaciones en el handoff. Un A producido por la función de revisión contextual NO convierte retrospectivamente el C o D irresuelto del productor en un A suyo. Ningún oráculo de Turing es supuesto ni suministrado.

### C. Proposición condicional exacta: mayor conjunto de políticas de asignación

Sea \(\theta\) una situación operativa en una distribución de ensayo predeclarada; \(A\) el conjunto de resultados transportados; \(M\) las cualificaciones contextuales legítimas, con su tiempo, alcance y fuente; \(\mathcal U\) una misma familia de acciones/evaluaciones **ya elegibles** y \(J(u,\theta)\) el beneficio o cumplimiento de una pregunta de *revisión y asignación de recursos*, NO una declaración de verdad sobre lo irresoluble.

Para políticas con el mismo límite de coste de ejecución, un receptor que observa \((A,M)\) puede siempre ignorar \(M\). Por tanto, si el coste de capturar/interpretar \(M\) no se contabiliza todavía:

\[
V_{A,M}=\sup_{\pi\in\Pi_{A,M}}\mathbb E[J(\pi(A,M),\theta)]
\ \ge\
V_A=\sup_{\pi\in\Pi_A}\mathbb E[J(\pi(A),\theta)],
\quad \Pi_A\subseteq\Pi_{A,M}.
\]

**Prueba:** toda política de \(\Pi_A\) también pertenece a \(\Pi_{A,M}\) al ignorar \(M\). Es una dominancia **débil** elemental por ampliación de observaciones, no una nueva teoría. La desigualdad solo es **estricta** cuando el metacontexto modifica de modo beneficioso la decisión óptima en escenarios con peso positivo. El **valor neto** puede ser menor o negativo al introducir los costes completos de instrumentación, envío, validación y composición, o cuando un sistema convencional ya posee el mismo contexto. No se afirma una mejora universal, ni que añadir etiquetas por sí solo genere correlación con el objetivo.

**Testigo finito para falsación:** dos productores comunican siempre el mismo A=«7». El próximo control tiene **un solo turno de evaluación** y dos rutas \(u_L,u_R\), ambas existentes en la envolvente componible, pero solo una dispone del método/permiso actualmente aplicable. En la mitad de estados de prueba \(u_L\) es aplicable y en la otra mitad \(u_R\). Una cualificación B legítima que indica cuál ruta está ya caracterizada permite elegir correctamente el turno en ambos casos. Un receptor que solo ve A no distingue los casos: con priori equiprobable, no puede superar probabilidad \(1/2\) de elegir una **ruta aplicable**, mientras el receptor contextual alcanza \(1\), **sin resolver aún el resultado de la propia evaluación**. Es un ejemplo de **asignación**, no una predicción de autorización, de la población desconocida en C ni de los riesgos reales en D. Si el receptor ordinario ya conoce el registro de rutas aplicables, también alcanza \(1\): resultado nulo para cualquier ventaja exclusiva de EA.

Un beneficio específico de C/D exige una pregunta distinta: por ejemplo, detectar una **brecha de base suministrada**, justificar una abstención o dirigir una búsqueda hacia otro agente que tenga una capacidad B compatible, sin asignar una probabilidad ficticia a la extensión C ni computar el efecto D. C o D pueden orientar acciones sin revelar el valor de la respuesta original. Un beneficio estricto requiere su propio testigo y coste; no se hereda del caso de B.

### D. Qué cambia —y qué NO cambia— en los teoremas de imposibilidad

- **Arrow:** la inexistencia de una función de bienestar social que satisfaga simultáneamente dominio irrestricto, ordenación social, Pareto, independencia y no dictadura sigue intacta con esos axiomas, aun si todo el espacio de funciones del tipo exigido es computable. Un contexto puede orientar qué problema de elección formular, qué condición reconsiderar o cuándo **no** producir una ordenación; esto cambia el contrato de evaluación, **no refuta Arrow**. [Definición y alcance](https://plato.stanford.edu/entries/arrows-theorem/).
- **Kleinberg:** ninguna función de clustering plano satisface simultáneamente invariancia de escala, riqueza y consistencia bajo sus axiomas. El metacontexto puede orientar una partición condicionada o una revisión de régimen si se modifica explícitamente el perfil, **no satisfacer simultáneamente los tres axiomas originales**. [Artículo](https://web.stanford.edu/~rezab/discrete/Notes/Kleinberg%20-%20impossibility%20theorem.pdf).
- **Rice:** la indecidibilidad **uniforme** de propiedades semánticas no triviales de programas no implica que cada problema individual sea indecidible. Una ejecución agotada por tiempo o memoria tampoco demuestra no computabilidad. Se puede mejorar la elección de ensayos y recursos sin decidir universalmente la propiedad. [Enunciado formal](https://plato.stanford.edu/entries/recursive-functions/).
- **Wonham y Pam Dixon:** una interfaz contextual puede cambiar el conjunto de observaciones y ayudar a reconocer **qué condición de autoridad necesita ser revisada**; la suficiencia para una decisión futura todavía requiere un criterio propio y evidence/standing admitidos. Ningún metadato crea un mandato originario ni su autorización. La composición de incertidumbre es diferente de resolver la autorización. [Pam, respuesta directa](https://github.com/FG-TIDA/themes/issues/9#issuecomment-6179863862).

La tesis defendible no es «los imposibles se vuelven posibles» en el mismo modelo y con los mismos axiomas, sino que la arquitectura **puede usar conocimiento ya caracterizado sobre sus propias fronteras** para reasignar explotación y mejorar decisiones de revisión dentro de las capacidades existentes, en escenarios donde una interfaz A-only lo perdería. Los teoremas generales siguen imponiendo sus límites; cambia la **política efectiva bajo recursos finitos**, el tipo de salida contextual y, a veces, la observación legítimamente disponible.

### E. Antes/después localizado propuesto para 00M; NO incorporado

**Ubicación si Iván da GO de incorporación:** tras **00M §6.3** (límite de información con estados indistinguibles), antes de §7 (alcance de la plausibilidad), como **§6.4 “Compositional capacity versus resource-bounded exploitation”**. No cambiar §1 canónica, §§4.1–4.3, ejemplos, referencias fijadas ni el nombre de la v0.8 original; si se autoriza una versión nueva, preservar la publicación actual y documentar el sucesor con su propio control de cambios.

**Antes (00M §6.3 final, cuerpo actual intacto):** «This elementary indistinguishability argument is stated here directly. Braverman et al. [R5] provides quantitative communication lower bounds for particular statistical models; it is relevant context, not the source of this generic two-state argument or an EA validation.»

**Después propuesto, núcleo de una adición (sin sustituir el texto anterior):**

> A result-only interface can be sufficient for the producer's selected operation yet omit already-characterized reserves, exploration routes and effective determination limits that matter to a different review question. For a fixed typed family of permissible agent operations, admissible finite compositions do not become non-computable merely because the agents exchange qualified context. The proposed gain is **resource-bounded and question-relative**: qualified positions may improve the selection of which already-assessable operation to run, where to inspect an uncharacterized frontier or when to preserve an unresolved limit. For a fixed admissible action family, policies able to ignore metadata include all A-only policies, so gross optimal value cannot decrease solely from observing additional valid context. Strict and net benefit require source-eligible, timely, decision-relevant qualifiers and measured total cost, and must be compared with a competent baseline that already retains them. C/D are not assumed enumerable or calculable and no oracle decides them; Arrow, Kleinberg and Rice remain valid within their original formal hypotheses.

**Falsadores y DDS propuesto:** fijar agentes y sus composiciones; identificar las preguntas y el presupuesto; construir al menos dos estados con el mismo A y distinta acción óptima de revisión fundamentada; contrastar A-only, EA contextual y un incumbente con información equivalente; medir utilidad, coste total, tiempo, errores de falsa continuación, abstención justificada y procedencia/autoridad. Si los agentes no aportan diferencias útiles, si la comparación ordinaria ya transporta el mismo contexto, si la cualificación llega tarde o si el coste destruye el beneficio, el diferencial es **nulo o negativo**. Ningún experimento DDS Stage A/B/C real queda ejecutado por esta nota.

**Gobernanza y fuentes:** esta sección es **una ampliación propuesta en 00M_VNext, no una edición del documento 00M v0.8 ni de sus requisitos congelados**. No se publican notas históricas privadas, originales de Drive ni supuestas aprobaciones de FG-TIDA; el trabajo formal y el diálogo con Pam siguen fuentes distintas. Sin validación matemática independiente ni un GO para sustituir la versión pública de 00M. La evaluación puede avanzar aunque nunca se apruebe la incorporación.


### F. Punto y seguido — pérdida muchos-a-uno, contexto cualificado y potencial de triangulación

**Nota abierta del autor, 16 de octubre de 2026 — primera base de un argumento de ganancia neta, NO su demostración.** Esta continuación forma parte de la propuesta de §6.4 anterior; no sustituye las hipótesis ni solicita incorporar hoy la VNext en 00M. El autor desarrollará la parte restante en un siguiente intercambio.

**1. La pérdida tiene lugar en la elección/composición, no en un mundo oculto que se haya inventariado.** En cada productor, varias alternativas, trazas, bases, intentos, condiciones de operación o posibilidades de explotación ya caracterizadas pueden desembocar en un solo resultado funcional A. Si una proyección \(a:S\to\mathcal A\) identifica estados \(s\neq s'\) que antes eran distinguibles, la interfaz A sola no reproduce esa distinción. El ejemplo de «el contador entrega 7» es distinto de transmitir qué cobertura, dependencias, reserva B o rutas C/D se han caracterizado al producir 7. Un receptor puede estar interesado en una pregunta distinta de la pregunta inicial del contador.

La **relación con B/C/D es funcional, no una igualdad de conjuntos**: B refiere a la base y reserva evaluable ya caracterizada que puede no haberse seleccionado; C a direcciones de exploración fundadas pero todavía no caracterizadas para evaluación; D a efectos potencialmente materiales fuera de la evaluación efectiva. Lo enviado es una **representación parcial, atribuida y lícita de estas posiciones**, no los contenidos totales de C/D ni una lista completa de opciones descartadas. Una proyección muchos-a-uno puede haber eliminado distinciones respecto de B o señales de C/D, pero el mero hecho de ser muchos-a-uno NO demuestra que haya eliminado alguna cualificación útil: todas las diferencias descartadas podrían ser irrelevantes para el receptor.

**2. Información retenida y relevancia para otra pregunta son dos cantidades distintas.** Para una variable discreta \(S\) de estados/trazas fuente observados en un perfil delimitado, \(A=a(S)\), metacontexto \(M=m(S)\) y pregunta receptora predeclarada \(R=r(S)\):

\[
L_{\mathrm{source}}=H(S\mid A),
\qquad
G_{\mathrm{retained}}=I(S;M\mid A),
\qquad
G_{\mathrm{review}}=I(R;M\mid A).
\]

Una proyección no inyectiva sobre estados de **probabilidad positiva** hace posible \(H(S\mid A)>0\); si M separa realmente esos estados, \(I(S;M\mid A)>0\). Por la regla de la cadena y las cotas de entropía, \(0\leq G_{\mathrm{review}}\leq H(R\mid A)\leq H(S\mid A)\) si R es función de S. Así, la pérdida fuente impone una **cota superior del espacio de ganancia**, no una ley de recuperación proporcional ni una ganancia garantizada. Incluso un \(H(S\mid A)\) enorme puede coexistir con \(I(R;M\mid A)=0\) cuando lo perdido no es relevante para R. Los indicadores que describen una frontera pueden ser útiles para elegir una revisión aunque aporten cero información sobre la respuesta oculta original. Para el exterior abierto C/D sin distribución validada, no se calcula una entropía fingida.

**3. Dos vías que no deben mezclarse.** (a) Reconstruir escenarios contrafácticos («¿qué ocurriría si el agente hubiese seleccionado también la alternativa 2, 3, ...?») exige nuevas evaluaciones y recursos; EA no lo obtiene gratuitamente. (b) Conservar las declaraciones parciales, condiciones de validez, razones conocidas de descarte, posiciones y fronteras ya advertidas en los productores permite que un receptor COMPONGA INFORMACIÓN CONTEXTUAL SIN EJECUTAR TODOS LOS CONTRAFÁCTICOS. El coste de (b) puede ser menor o mayor que la repetición, según instrumentación, cantidad, proveniencia, latencia, derechos y necesidad de interpretación. No equivale a una clonación Docker/Kubernetes ni a un oráculo para resolver C o D.

**4. Hipótesis de triangulación multiagente, explícitamente aún no demostrada.** Si tres productores trabajan en habitaciones o ventanas diferentes y transmiten A junto con observaciones cualificadas acerca de sus fronteras, las relaciones entre sus posiciones podrían permitir a un receptor establecer una incompatibilidad, una correspondencia de alcance, un solapamiento o una brecha de observación que ninguna A aislada determina. La analogía geométrica de triangulación requiere referencias comunes, superposición justificada, tiempo coherente, atribución y un mecanismo de inferencia correcto; sin ello, «varios puntos de vista» no determina un entorno común. «No puede ver fuera» no identifica qué hay fuera. Los agentes pueden compartir una misma fuente o describir el mismo punto ciego sin que ello constituya evidencias independientes. La estricta ganancia epistémica de esa triangulación es una cuestión de prueba, no una premisa.

**5. Por qué "más pérdida ⇒ más ganancia neta" sigue abierta.** La intuición del autor es que un ecosistema cuyas salidas A comprimen muchas elecciones tiene más **margen potencial** para recuperar distinciones por composición. La relación propuesta es investigable, pero no admite hoy ni universalidad, ni proporcionalidad, ni monotonía: una compresión mayor puede descartar solamente ruido o diferencias sin valor para la pregunta receptora. Para hablar de beneficio neto necesitamos distinguir medidas en bits de magnitudes de utilidad, coste, tiempo y riesgo. Definir, para un mismo horizonte y acciones elegibles, \(U_{\mathrm{net}}=\Delta U_{\mathrm{decisional}}-C_{\mathrm{captura,transporte,interpretación,verificación,coordinación}}\), con unidades de utilidad comparables. Puede ser positiva, cero o negativa; hay que compararla con una arquitectura convencional competente que ya transmita las mismas cualificaciones.

**6. Supuestos pendientes para una futura ley condicional (no asumirlos como satisfechos):** (i) algún productor conserva cualificaciones pertinentes no deducibles de su A; (ii) el receptor dispone de un contrato semántico para composiciones entre actores y preguntas; (iii) alcance, procedencia, tiempo, fiabilidad y acceso se justifican; (iv) la triangulación efectivamente distingue estados/revisiones relevantes y no infiere el contenido oculto de C/D; (v) coste completo y ventana temporal permiten un beneficio neto; (vi) se fija una alternativa fuerte con igual acceso; (vii) la hipótesis de utilidad se prueba en un perfil específico y admite contraejemplos. Estos son **requisitos por investigar**, no afirmaciones de que EA ya los cumple.

**Punto de continuación:** aislar primero el vínculo verificable «compresión de la selección → cualificaciones descartadas → relación entre ventanas → nueva distinción para una pregunta receptora»; después investigar si existe una clase no trivial de perfiles con triangulación estricta y beneficio neto acotado. No cerrar la tesis, no simular resultados y no introducir esta nota como teorema o conclusión en el 00M canónico.

**Nexos:** [00M §4 y §6](./00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) · [00N §§2.1–2.3, 3.6–3.7](./00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md) · [revisión actual de la hipótesis sobre explotación bajo recursos](#15-octubre-2026--plausibilidad-de-asignación-de-explotación-mediante-contexto-compuesto-propuesta-00m-64).


### G. Cartografía abierta — U, U′ y metadatos primados locales (sin procesarlos)

**16 octubre 2026 — formulación del autor, versión cartográfica inicial.** Es una **continuación de la propuesta** del PR borrador, no una enmienda al 00M v0.8 vigente, ni una inferencia de triangulación o utilidad neta. El autor pide por ahora **definir los objetos, no procesar ni componer las primas**. Esta nota no supone sensores nuevos, algoritmos de inferencia de fronteras ni oráculos.

#### G.1 Higiene de tipos: A–E son máquinas, no los roles A/B/C/D de 00M

La notación informal del autor llama **A, B, C, D, E** a cinco máquinas reales. Para no confundirlas con los **roles de cualificación** A (resultado), B (reserva caracterizada), C (frontera de exploración) y D (residual), aquí escribimos las cinco máquinas \(\mathsf M_A,\mathsf M_B,\mathsf M_C,\mathsf M_D,\mathsf M_E\). Sus salidas funcionales son \(a_A,\ldots,a_E\), y sus registros primados son \(A',B',C',D',E'\), respectivamente. Los primados son **registros o declaraciones parciales sobre contexto**, no conjuntos de todo lo que falta a la salida ni nuevas respuestas funcionales.

#### G.2 El universo de composabilidad \(U\) y un exterior \(U'\) solo relativo a un marco

Sea \(I=\{A,B,C,D,E\}\). Cada máquina dispone, en un instante y régimen \(t\), de una familia de funciones computables \(\mathcal F_{i,t}\). Fijadas las reglas \(\mathrm{Adm}_t\) (tipos, contratos, precondiciones, capacidades y permisos), definimos el horizonte ideal de composiciones finitas **admisibles**:

\[
U_t:=\mathrm{Cl}_{\circ,\mathrm{Adm}_t}\!\left(\bigcup_{i\in I}\mathcal F_{i,t}\right).
\]

Las capacidades \(\mathcal F_{i,t}\) están dentro de \(U_t\) por construcción; una «máquina», entendida como hardware/actor, no es literalmente un elemento de un conjunto de funciones salvo que se la represente formalmente como tal. \(U_t\) es el universo **componible de esos productores**. No es el universo físico, no es necesariamente conocido ni enumerado por ellos, y no afirma que exista un algoritmo que decida si una tarea arbitraria pertenece a su clausura.

Para hablar de exterior hace falta fijar **un marco envolvente de posibilidades del mismo tipo** \(\mathscr W\). Entonces:

\[
U'_t:=\mathscr W\setminus U_t.
\]

La afirmación \(U'_t\ne\varnothing\) exige \(\mathscr W\supsetneq U_t\); **no se deduce de que el sistema tenga cinco máquinas ni de negar una «máquina universal»**. Existen máquinas de Turing universales para las funciones efectivamente computables: «universal» no significa decidir HALT ni abarcar todas las funciones matemáticas o la totalidad del mundo abierto.

**Testigo condicional para existencia de exterior:** si \(\mathscr W\) es el conjunto de todas las funciones totales \(\mathbb N\to\{0,1\}\), y \(U_t\) contiene solo funciones implementables por descripciones finitas sin oráculos (y de ese tipo), entonces \(U_t\) es a lo sumo numerable y \(\mathscr W\) es no numerable por Cantor. Por tanto \(U'_t\ne\varnothing\). Este teorema sobre funciones no demuestra que los agentes conozcan **qué elemento específico** está en su exterior práctico, ni identifica C/D, ni convierte \(\mathscr W\) en un inventario del mundo físico. Si \(\mathscr W=U_t\), el exterior relativo es vacío. El máximo teórico respecto al marco es \(\mathscr W=U_t\cup U'_t\), no \(U'_t\) por sí solo.

#### G.3 Qué significa precisamente cada prima

Fijamos un espacio de **descripciones** \(\mathscr L\), distinto del espacio de funciones y estados del entorno. Cuando existe documentación o instrumentación legítima, cada máquina \(i\) puede proporcionar un registro \(m_i\in\mathscr L\). Por convención del autor:

\[
A':=m_A,\quad B':=m_B,\quad C':=m_C,\quad D':=m_D,\quad E':=m_E.
\]

Ejemplos de información que **podría** estar ya conservada: tipos y contrato de entrada; población declarada «gatos domésticos»; condiciones de operación y calibración; excepciones observadas; requisitos de memoria/tiempo; exclusiones conocidas; una vía exterior indicada como «gatos monteses no evaluados»; un riesgo ambiental cuya incidencia no se sabe evaluar. El registro solo afirma lo que su fuente realmente justifica. Puede contener referencias B, algunas pistas C y D del *proceso*, sin enumerar las regiones C/D. No todos los campos existen por defecto.

**Prohibición explícita de complementos ficticios:**

\[
A'\ne\overline{a_A},\quad A'\ne \mathscr W\setminus\mathrm{Dom}(\mathsf M_A),\quad A'\ne U'_t.
\]

Estas expresiones pertenecen además a **tipos diferentes**: un registro de límites no es el conjunto de todas las funciones, casos o mundos externos. Análogamente para \(B',C',D',E'\). Una prima puede referirse a un límite y a una vecindad epistemológica sin conocer el exterior completo. No debe inferirse, a partir de un límite declarado, ni la existencia de todos los ejemplos vecinos ni su computabilidad. Tampoco se ha probado una cobertura exhaustiva de \(U'_t\) al reunir las cinco primas.

#### G.4 Tesis a probar / contraejemplo: tener un límite formal no equivale a conservar internamente un mapa de ese límite

Toda función parcial \(f\) **posee** un dominio matemático \(\mathrm{Dom}(f)=\{x:f(x)\downarrow\}\), y un contrato de aplicación puede declarar una frontera semántica. Pero **no se sigue que todo programa compute, almacene o conozca una descripción de esa frontera**. Si se siguiera que existe un procedimiento universal capaz de decidir, desde cualquier código de programa, todos los miembros de su dominio de terminación, resolveríamos HALT; esa conclusión es falsa.

**Contraejemplo aún más sencillo de autoconocimiento semántico:** el programa \(p(x)=7\) para toda cadena \(x\), sin metadatos de dominio, produce exactamente las mismas trazas si una persona lo denomina «contador de gatos domésticos» o «contador de cualquier animal» a nivel de uso externo. Si el contrato de aplicación no entra en el código ni en sus fuentes observables, ninguna función del solo \((p,\text{traza})\) identifica legítimamente cuál era la frontera de aplicación imaginada por esa persona. La máquina no tiene forzosamente un dato «gatos monteses quizá» escondido que podamos copiar sin trabajo.

**Resultado condicional sí defendible:** si cada productor incluye o posee accesibles un contrato, precondiciones, declaraciones de cobertura, registros de fallos o metadatos \(m_i\) ya establecidos, es posible **preservar esos registros tal cual** sin ejecutar las alternativas que no se exploraron ni resolver sus incertidumbres. Esta conservación es un objetivo de ingeniería documentable, no una ley de toda máquina teórica. Un registro vacío o meramente «scope not declared» también puede ser honesto, pero no garantiza una información exterior nueva.

#### G.5 Mapa estático, sin ninguna composición de primas por ahora

\[
\begin{array}{c}
\mathscr W:\text{marco de referencia más amplio}\\
\underbrace{U_t=\mathrm{Cl}_{\mathrm{Adm}_t}(\mathcal F_A\cup\cdots\cup\mathcal F_E)}_{\text{máquinas y sus funciones componibles}}
\qquad
\underbrace{U'_t=\mathscr W\setminus U_t}_{\text{exterior relativo}}\\
\mathsf M_A\mapsto(a_A,A'),\;\mathsf M_B\mapsto(a_B,B'),\ldots,\mathsf M_E\mapsto(a_E,E').
\end{array}
\]

Los \(a_i\) constituyen la interfaz **funcional**; los registros \(A',\ldots,E'\) constituyen una interfaz **contextual**, con significado dependiente de su productor, alcance y momento. Por decisión expresa del autor, **el depósito colectivo en esta etapa únicamente conserva los registros; NO los intersecta, triangula, clasifica globalmente, computa contrafácticos ni reetiqueta C/D como A**. No se postula ningún sensor capaz de observar \(U'_t\).

#### G.6 Coste: «ningún cómputo funcional nuevo» no significa coste físico total cero

Con los \(m_i\) ya generados y disponibles **sin una evaluación nueva**, las funciones productoras pueden quedar idénticas y la cantidad de computación necesaria para resolver sus problemas funcionales no cambia. En este sentido restringido, el metarregistro no exige explorar más gatos ni evaluar gatos monteses. Pero copiar, registrar, serializar, transmitir, autenticar y almacenar metadatos sigue teniendo coste de recursos y normalmente consume operaciones. Enviar físicamente una carga de \(L\) bits requiere transportar esos bits (salvo referencias/deduplicación con un almacén compartido y costes desplazados al acceso). Puede evitarse recomputación semántica adicional, **no** afirmar coste computacional/energético total nulo.

Si la prima no se creó ni se mantuvo originalmente, reconstruir una frontera significativa sí puede exigir cómputo, inspección humana o experimentación. No procede asumir por definición que estaba almacenada. El supuesto de metadatos ya disponibles es el fundamento bajo el que se podrá estudiar un coste **incremental** relativamente pequeño.

#### G.7 Qué queda demostrado y qué debe permanecer abierto

**Por construcción:** \(U_t\) contiene las composiciones admisibles de las capacidades declaradas; cada prima es una descripción parcial **si** el productor dispone de esa descripción; los primados no son complementos ni un inventario de \(U'\); copiar registros existentes no exige resolver los contenidos no evaluados.

**Condicionalmente demostrado:** \(U'_t\neq\varnothing\) para la envolvente no numerable de todas las funciones binarias frente a un sistema sin oráculos descrito finitamente. No hay demostración universal de \(U'\) para cualquier marco de referencia.

**NO demostrado:** que toda máquina ya tenga un \(m_i\) útil; que todas las primas sean no vacías; que estén totalmente determinadas sin trabajo; que describan de modo completo una frontera epistemológica; que reúnan conocimiento suficiente sobre \(U'\); que el traslado sea gratis; o que la triangulación posterior aumente información o beneficio neto.

**Punto de continuidad:** primero fijar matemáticamente **tipos, dominios, admisibilidad, significado de cada prima y custodia**; todavía no efectuar composición de las primas, probabilidad de triangulación, optimización de recursos ni una «ley de ganancia neta». El siguiente incremento del autor tratará esos procesos. **00M, 00N y las fuentes publicadas quedan intactos; esta nota vive en la VNext propuesta del PR borrador.**


## Reception of the 1 October proposal — 26 October 2026

Iván authorized the corrections proposed in the PR audit. The [earlier A/B/C/D proposal](./00M_CANONICAL_ABCD_SEMANTICS_AND_REQUALIFICATION_FEASIBILITY_v0.1.md) is retained as a complete historical antecedent. Current reader routes continue to use 00M v0.8, its declared assumptions and its existing review. The earlier functional-result/basis/frontier/residual distinction and conditional finite-construction argument remain useful lineage; they are not a competing current canon. The old §7 identifies dated reconciliation questions, not a present instruction to reapply all of them. The current 04 review retains the producer-mapping/H06 obligations; this historical disposition closes none of those scientific or implementation questions. The PR remains a reviewable historical-retention proposal.
