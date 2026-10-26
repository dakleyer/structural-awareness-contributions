# Primera preparación de la quinta pasada — trabajos externos y piezas aprovechables

**Consulta de fuentes realizada por Codex, 6 de octubre de 2026.** Asistente de IA del mismo chat. [Plan, quinta pasada](../CORPUS_REVIEW_PROCEDURE_2026-10-06.md#quinta-pasada--trabajos-externos-diferencial-y-reutilización). Este mapa prepara comparaciones dentro de las VNext; no declara realizada la quinta en todos los documentos ni sustituye su juicio propio.

La pregunta es qué ya existe, qué puede servir y qué tendría que probarse todavía. Se buscaron propuestas actuales de FG-TIDA y trabajos sobre memoria/autoridad, evaluación, protocolos e identidad. La selección es inicial y no una revisión sistemática exhaustiva.

## Trabajos de FG-TIDA y novedades relativas a los documentos

Se leyeron los cuerpos de las propuestas y comentarios indicados mediante la API pública; autores, fechas y disposición se fijan en la [evidencia de consulta](./EP_EXTERNAL_RESEARCH_EVIDENCE_2026-10-06.json). Las referencias son aportaciones de sus autores, no adopción del grupo.

| Fuente primaria | Relación que merece contraste | Pieza candidata y límite |
|---|---|---|
| [Theme #31](https://github.com/FG-TIDA/themes/issues/31), Haoran Deng, 30 septiembre | Conservación de restricciones durante memoria, resumen y handoff; vecino de requisitos, interfaces, 00M/00N y 00G. | Puede orientar contrastes propios entre grant y representación recibida. Falta cotejar los controles y mappings completos; no es una interfaz común ya implementada. |
| [Theme #34](https://github.com/FG-TIDA/themes/issues/34), Gianpaolo Angelo Scalone, 1 octubre | Identidad arraigada, delegación limitada y lifecycle; vecino de ACC, MSCA Operation y autoridad. | Referente de arquitectura y casos de delegación. El documento XSTR.ATHENA citado por la propuesta no se leyó aquí; no se transfiere su eventual estatus al corpus. |
| [Theme #35](https://github.com/FG-TIDA/themes/issues/35), Duncan Sparrell, 3 octubre | Dependencias y supply chain; vecino de Cartografía, vigencia y evidencia de componentes. | Un inventario de componentes puede alimentar una vista parcial de dependencias. No describe por sí solo su efecto material sobre cada decisión; sus referencias X.2105/X.2106 quedan pendientes. |
| [Propuesta #33](https://github.com/FG-TIDA/themes/issues/33) y [comentario de disposición](https://github.com/FG-TIDA/themes/issues/33#issuecomment-5947703119), 1–2 octubre | Reevaluación por nueva evidencia, restricción y restauración; vecino de requalification y operación. | Ideas para comparar temporalidad, registros y restoration. Está cerrada y el comentario la declara fuera de alcance; no se presenta como workstream adoptado. Las afirmaciones jurídicas del proponente no se validaron ni se reutilizan aquí. |
| [Contribución #30](https://github.com/FG-TIDA/themes/issues/30) y [disposición](https://github.com/FG-TIDA/themes/issues/30#issuecomment-5947715148), 30 septiembre–2 octubre | Controles de respuesta conocida y fallos del verificador; vecino de oráculos y benchmark. | Puede orientar método de evaluación. Se declara construida/ilustrativa, con partes de diseño y atribución propia. Está cerrada como fuera de alcance; código y contenido tienen derechos distintos. |

Estas fuentes son posteriores a varias especificaciones de septiembre del corpus, pero no a todos sus documentos. Cada VNext debe comparar sus fechas reales; un comentario editado no demuestra una prioridad histórica. Se consultaron también [UC4](https://github.com/FG-TIDA/use-cases/issues/4) y [UC6](https://github.com/FG-TIDA/use-cases/issues/6) como casos externos: no se admitió una campaña ni se probó equivalencia.

## Investigación y mecanismos externos

| Fuente y alcance efectivamente leído | Qué aporta al contraste | Qué podría aprovecharse; qué no se hereda |
|---|---|---|
| [Louck, preprint arXiv:2606.24322v1](https://arxiv.org/html/2606.24322v1), 23 junio 2026; §§I–IV, evaluación/related work y límites seleccionados | Separa contenido, origen y autoridad en memoria; ofrece un monitor y pruebas bajo supuestos explícitos. El modelo acotado y la argumentación paramétrica no son una prueba universal de todos los sistemas. | Candidato a comparador fuerte y a inspección de artefactos. La atribución de valores, el monitor confiable, la independencia y el alcance de memoria importan. Corroboración no sustituye el mandato de nuestro principal. Resultados reportados no reproducidos aquí. |
| [Petersen, versión arXiv v1](https://arxiv.org/html/2412.10039v1) y [publicación UAI/PMLR 2025](https://proceedings.mlr.press/v286/petersen25a.html); planteamiento y resultados centrales leídos | Los controles contra azar ayudan a interpretar métricas que parecen altas. Las fórmulas de precisión/recall se refieren a estimación de skeletons de grafos. | Aprovechable como disciplina de control y contexto de la métrica. No se importan sus distribuciones a R01 ni a una prueba de autoridad sin establecer el modelo correspondiente; PDF final no recuperado. |
| [A2A, especificación 1.0.0](https://a2a-protocol.org/latest/specification/), apartados de versión, conceptos y autorización | Ofrece comunicación, tareas y reglas de acceso; el modelo de autorización sigue definido por el agente. | Candidato para transporte, adapters y comparación. Task/context IDs o el éxito de transporte no prueban binding semántico, permiso vigente o efecto. No se leyó toda la especificación ni se probó un SDK. |
| [MCP, autorización 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization), recursos/audiencias, token handling y challenges | Vincula tokens a recursos y define tratamiento de autorización. | Candidato de infraestructura y peer competente. No demuestra por sí solo que el resumen conserve todas las condiciones de una decisión; implementación y versión concreta pendientes de evaluar. |
| [Proyecto NCCoE/NIST de identidad y autorización](https://www.nccoe.nist.gov/projects/software-and-si-agent-identity-and-authorization), página de estado | Mantiene una exploración basada en estándares y recursos de consulta. | Referencia de alcance y necesidades; no se presenta como una norma completa, demostración concluida o validación de nuestra arquitectura. Los recursos individuales necesitan lectura propia. |

## Derechos y versión de la pieza

Se leyeron los archivos de licencia públicos; no se copió código, dataset o catálogo al corpus.

- [A2A LICENSE](https://github.com/a2aproject/A2A/blob/main/LICENSE): Apache-2.0; se debe fijar la pieza y versión antes de reutilizarla.
- [MCP LICENSE](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/LICENSE): transición de licencias. Distingue contribuciones nuevas, material anterior y documentación; no cabe declarar todo el repositorio bajo una sola licencia sin examinar la pieza.
- [mem-inv-bench LICENSE](https://github.com/yedidel/mem-inv-bench/blob/main/LICENSE): código bajo MIT según el archivo consultado; datos y materiales de terceros requieren comprobación separada.
- [silent-failure-catalog LICENSE](https://github.com/zhaoxinghua09-cell/silent-failure-catalog/blob/main/LICENSE) y [LICENSE-CONTENT](https://github.com/zhaoxinghua09-cell/silent-failure-catalog/blob/main/LICENSE-CONTENT): código y prosa/casos tienen condiciones diferentes. La consulta no autoriza importar, adaptar o republicar el catálogo.

La versión main del catálogo no se identifica automáticamente con el tag v0.1.0 recomendado en la discusión. El pin de release y su licencia siguen pendientes de resolución; la consulta de ese pin no llegó a completarse. No se importó una pieza basándose en ese estado incompleto.

## Juicio inicial de diferencial y prioridades

Las fuentes muestran coincidencias materiales: conservación de restricciones, reevaluación temporal, controles, delegación y seguridad de transporte ya tienen vecinos. **No se ha establecido un diferencial del conjunto mediante este mapa.** Tampoco se deduce equivalencia de una coincidencia de título: hay que comparar función, premisas, autoridad, recursos, plazo y resultado útil.

La oportunidad inmediata es formar comparadores competentes y seleccionar métodos/infraestructura aprovechables. La contribución que todavía se investigue deberá ser precisa: qué calificación o relación añade, qué necesidad cubre que el peer no cubre bajo las mismas condiciones y cuál es su carga. Si el peer la cubre, corresponde reconocerlo y estudiar reutilización.

Las VNext reciben preguntas particulares, el alcance leído y sus decisiones. El registro de fuentes compartido evita repetir consultas; no crea un canon externo, elimina autores o transfiere resultados a EA. Sigue pendiente la quinta completa por documento, además de las cuatro lecturas y la conciliación global.
