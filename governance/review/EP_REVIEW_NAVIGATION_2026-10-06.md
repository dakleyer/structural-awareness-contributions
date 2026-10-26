# Conciliación de navegación — avance verificable, 6 de octubre de 2026

Este registro sirve para que una persona vea qué falta en la revisión del corpus. No certifica su coherencia semántica. Depende del [plan de trabajo](../CORPUS_REVIEW_PROCEDURE_2026-10-06.md) y de [EP README VNext](../../architectural-contributions/ecosystem-positioning/README_VNext.md).

**Auditoría realizada por Codex**, mismo asistente de IA. Snapshot `2db5a8c17f58008f9268c23c681ba6e14c8dfbdc`. Se recuperaron completos **529 archivos Markdown**, excluyendo las copias de preservación de esta revisión. Desde el README de EP se alcanzan **464** por los enlaces textuales extraídos. Alcanzar o descargar un archivo no significa haberlo leído semánticamente.

## Qué se comprobó

Se extrajeron enlaces Markdown, referencias por nombre, href/src HTML y direcciones web visibles fuera de bloques de código. Se resolvieron rutas relativas, destinos GitHub del mismo repositorio, versiones actuales y anclas calculadas/expresas. Los fragmentos de propuestas dentro de bloques de código se excluyeron del grafo observado.

En esta extracción hay **4.265 relaciones internas**; no aparecieron anclas faltantes en el Markdown recuperado. Apareció una dirección incompleta en part02 de UC-EA-03, cuya explicación está abajo. Son comprobaciones estáticas: no verifican la carga de cada página web, el comportamiento del navegador o enlaces dinámicos dentro de código, documentos Office/PDF e imágenes.

Las **98 referencias históricas** extraídas corresponden a **80 pares distintos de versión/ruta**. Se resolvieron los **30 commits** y se comprobaron los 80 destinos en sus árboles, sin destinos ausentes. Las anclas históricas no se certifican en bloque. No se cambia una cita histórica por main para que parezca actual.

Las **1.601 referencias externas** extraídas son apariciones por documento, no 1.601 sitios distintos. Su revisión intelectual y disponibilidad no está terminada. El número no acredita validación bibliográfica.

## Hallazgos para una lectura humana

**Una URL cortada en una copia por partes.** El documento completo de UC-EA-03 coincide exactamente con sus tres partes concatenadas. El final de part02 corta la dirección de Annex I y part03 contiene el resto. La ruta principal utiliza el documento completo, donde ese enlace es válido. El defecto afecta la lectura aislada de la copia parcial, no el contenido conservado. [VNext del perfil](../../research/ecosystem-awareness/baseline/UC-EA-03_VNext.md). No se modifica el freeze.

**Un nombre antiguo que puede parecer vigente.** Hay dos archivos llamados 05A v0.1: uno en baseline y otro en fg-tida/interfaces. Sus blobs y textos difieren; la ruta pública actual usa interfaces. El archivo antiguo conserva una cabecera “public working bridge” que, fuera de su contexto histórico, puede confundirse con la edición actual. La clasificación de esa copia y el historial de traslado necesitan conciliación explícita; no se borra ni se fusiona. [Única VNext de 05A](../../research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md).

**Disponibilidad pública y antigüedad no son madurez.** El mapa de Drive leído sigue fechado 11 de septiembre y describe baselines de esa época. Es una orientación con procedencia, no una verificación actual de todo GitHub. Tampoco la disponibilidad de una nota “local draft” convierte el texto en resultado experimental o contrato adoptado.

**Archivos sin ruta textual desde EP.** Hay 65 candidatos fuera del recorrido extraído. Incluyen licencias/contribuciones generales, submissions de otros temas, ediciones anteriores, fragmentos cuyo documento completo sí está enlazado y fichas nuevas. No se les llama “huérfanos” por defecto: hay que decidir su pertenencia, función y ruta útil antes de proponer una adición. La [evidencia complementaria](./EP_REVIEW_NAVIGATION_2026-10-06.json) conserva la lista exacta.

## Qué sigue abierto

La conciliación semántica debe comprobar que cada consumidor conserva definiciones, dueños, condiciones y grado de evidencia de su fuente; que cada teoría derivada se presenta como derivación propuesta; y que las diferencias temporales de fuentes congeladas no se esconden bajo el mismo número de versión.

El trabajo actual examinó las fuentes de 00N, la tabla 00M-A01, su addendum y UC-EA-03, con alcances y excepciones dentro de sus VNext. No extiende ese examen a los 464 documentos alcanzados. Las figuras de 00M, las fuentes externas pendientes y los consumidores extensos requieren sus propias lecturas.

Toda propuesta de reorganización se examina en la VNext del README propietario dentro de **EP → Awareness → índices técnicos**. Este registro no cambia la jerarquía ni crea otro nivel.

## Método y conservación

Los conteos describen el snapshot anterior a las nuevas adiciones de esta misma auditoría. Una publicación posterior puede agregar fichas/controles; los conteos no se extrapolan silenciosamente. El inventario mantiene épocas fechadas: repetir una ruta con nuevo commit documenta su estado posterior, no crea un segundo documento lógico o una segunda VNext.

La comprobación completa es reproducible desde el snapshot y el grafo preservados localmente; el JSON público es una ayuda compacta, no copia de todo el texto del corpus. Las fuentes técnicas, binarios, pruebas y resultados permanecen intactos.
