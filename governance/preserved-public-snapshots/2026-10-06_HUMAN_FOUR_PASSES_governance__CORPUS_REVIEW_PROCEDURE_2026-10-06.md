# Revisión segura del corpus de Ecosystem Positioning

**ID:** EP-CORPUS-REVIEW-PROCEDURE · **Versión del procedimiento:** 1.1 · **Fecha:** 6 de octubre de 2026  
**Responsable de las decisiones:** Iván Abril Palma  
**Entrada humana:** [Ecosystem Positioning](../architectural-contributions/ecosystem-positioning/README.md) · **Control de navegación:** [DOCUMENT_CONTROL](../DOCUMENT_CONTROL.md)

Este procedimiento permite revisar a fondo un documento y sus relaciones sin cambiar lo que el lector puede utilizar hoy. Primero se conserva la fuente. Después se audita, se conversa sobre los hallazgos y se escriben propuestas exactas. Iván decide qué se incorpora. Una auditoría, por extensa que sea, nunca se convierte por sí sola en una nueva versión canónica.

## 1. Las instrucciones de Iván

Instrucciones recibidas el 6 de octubre de 2026. Iván corrigió después el nombre a **VNext**; las citas siguientes normalizan únicamente ese nombre. Los siguientes fragmentos son citas de su petición, no aprobaciones futuras:

> «no toques los documentos. Esa es la regla número uno».
>
> «crear una VNext si es que no la hay y solo una VNext de cada documento».
>
> «primero con una auditoría del documento y de la relación con otros documentos».
>
> «texto antes, texto después, de manera quirúrgica».
>
> «Pueden haber múltiples auditorías dentro del documento».
>
> «siempre con instrucciones de Iván ahí puestas dentro de la VNext».

También pidió una nota al principio que enlace la VNext correspondiente, un README humano y una adición que conecte este procedimiento sin reescribir el README.

La única excepción editorial de esta fase es **añadir la nota de versión/revisión y su enlace**. No permite corregir, resumir, reordenar, reformatear ni sustituir el cuerpo existente. La VNext permanece separada de la versión vigente: puede identificarla como fuente auditada, pero no la reemplaza, no cambia su autoridad y no es una dependencia normativa que el lector deba adoptar.

## 2. Qué entra en la revisión completa

La entrada es el README de Ecosystem Positioning. Desde una revisión Git fijada, se sigue su red de enlaces a Ecosystem Awareness, Regime Awareness, MSCA, arquitectura, requisitos, interfaces, hipótesis, casos, benchmark, pruebas, evidencia, presentaciones y antecedentes. Se incluyen las dependencias transitivas relevantes y las referencias entrantes a los documentos afectados; no basta con leer los enlaces directos.

Antes de declarar la revisión completa, crear un inventario con una fila por documento lógico: ID, título, ruta vigente, versión declarada o «no declarada», commit y blob/hash, propietario semántico, clase de fuente, relaciones, única VNext, ubicación de su nota, auditorías realizadas, cobertura, hallazgos pendientes y decisión de Iván. Registrar aparte enlaces externos, rutas ausentes, archivos no legibles y documentos fuera de alcance. Un archivo encontrado o una nota añadida no significa que haya sido auditado.

No seguir enlaces indefinidamente hacia todo Internet o todo GitHub. Cada dependencia externa se clasifica como fuente consultada, dependencia necesaria pendiente o contexto excluido con razón. Los enlaces al programa padre son contexto; su dependencia material se evalúa, no se presupone. Un enlace no transfiere propiedad semántica ni evidencia entre corpora.

El inventario de cobertura vive junto a este procedimiento y se enlaza aquí cuando exista. **Esta versión establece el método; no certifica una auditoría completa ni la creación de VNext para todo el corpus.** Su primer ejemplo operativo es la [VNext del README de Ecosystem Positioning](../architectural-contributions/ecosystem-positioning/README_VNext.md).

## 3. Conservar primero

1. Leer los controles aplicables y la fuente actual en GitHub. Fijar commit, ruta, versión y blob/hash. No sustituirla por una copia local atrasada.
2. Antes de añadir algo a un documento vivo, conservar una copia exacta y verificable del estado intacto en `old/` o en el archivo de preservación autorizado. Anotar su ubicación y comprobar igualdad. Git history complementa esta copia; no se reconstruye una fuente después de editarla.
3. Buscar si ya existe una VNext, vNext o Review & Delta para ese mismo documento lógico. Reutilizarla y preservar todo su contenido previo. El nombre existente no tiene que cambiar.
4. Añadir únicamente la nota permitida y registrar esa operación por separado de cualquier propuesta sustantiva.
5. Verificar que quitar exclusivamente la nueva nota reproduce exactamente los bytes anteriores. No normalizar saltos de línea, BOM, espacios ni codificación.

**Fuentes protegidas:** no insertar notas dentro de documentos congelados, firmados, pre-registrados, enviados, históricos, resultados, datos, manifests de evidencia ni archivos cuya identidad dependa de hashes. Para PDF, DOCX, PPTX, imágenes y otros binarios, tampoco reexportar ni alterar el contenedor para añadir el cuadro. Usar una ficha externa del documento, con el cuadro al principio, que enlace original y VNext; el inventario señala esta excepción. Un router editable puede enlazar esa ficha. Código y fixtures se inspeccionan como soporte técnico, sin introducir prosa ni ejecutar pruebas como parte de esta preparación.

La nota de revisión no incrementa silenciosamente la versión técnica del documento ni recalcula un manifest congelado. Tiene su propia fecha/revisión de navegación. El archivo de control puede registrar adiciones mediante una entrada fechada sin reescribir encabezados históricos.

## 4. Una sola VNext por documento

VNext es el espacio acumulativo de auditoría y propuestas de **un documento lógico**, no una copia corregida de su texto. El inventario establece esa identidad y evita duplicados por auditor, fecha, pasada o número de versión. Se mantiene la misma ruta durante sucesivas revisiones; la historia se conserva dentro del archivo y en Git. No crear `VNext2`, `VNext_final`, ni una nueva VNext por cada auditor.

Si hay varios candidatos previos, registrar la colisión y pedir a Iván cuál será la única VNext activa. No borrar, fusionar ni renombrar archivos para ocultar el conflicto. Una revisión de un documento de varias partes usa una VNext si esas partes forman una sola unidad; documentos semánticamente distintos conservan identidades distintas.

Cuando cambia la fuente vigente, abrir una nueva época de auditoría **dentro de la misma VNext**, conservando el commit anterior, los comentarios y las decisiones. Las propuestas del estado antiguo quedan pendientes de revalidación; no se aplican a ciegas a la nueva fuente.

Cada VNext contiene, en este orden:

1. Identidad y estado de la fuente; carácter no canónico; alcance y límites de cobertura.
2. Instrucciones de Iván, fechadas y con referencia verificable cuando exista. Distinguir cita, interpretación operativa y autorización concreta.
3. Auditoría del documento y de sus relaciones.
4. Conversación acumulativa de auditorías y respuestas.
5. Decisiones e instrucciones posteriores de Iván.
6. **Al final**, propuestas quirúrgicas, con texto antes y texto después.

Para evitar una recursión sin fin, la nota, la VNext, su plantilla y el inventario son instrumentos de control de esta revisión; no generan VNext de VNext. Una modificación posterior del propio procedimiento debe conservar su predecessor y registrar explícitamente la propuesta y decisión; esta excepción no convierte los instrumentos de control en fuentes técnicas canónicas.

## 5. El cuadro al principio

Para Markdown editable, colocar una nota breve antes del cuerpo original. No mover el título ni quitar introducciones para hacer sitio. Adaptar las rutas reales y comprobarlas:

```text
Nota de revisión — [fecha; revisión de la nota]
Estado: cuerpo vigente preservado; auditoría [pendiente/parcial/completa en alcance definido].
VNext de este documento: [enlace real a su única VNext].
Procedimiento: [enlace real a este procedimiento].
La VNext contiene auditorías y propuestas; no sustituye esta versión.
```

No declarar «auditoría completa» en la nota porque exista la VNext. Para una fuente inmutable o binaria, el mismo cuadro va en su ficha externa y dice expresamente «nota externa; original intacto».

## 6. Auditar el documento y sus relaciones

Leer el documento completo en su versión fijada. Para cada hallazgo, registrar pasaje exacto, fuente, consecuencia, alcance, evidencia y lo que queda sin verificar. Revisar al menos:

| Dimensión | Pregunta de revisión |
|---|---|
| Propósito y lectura humana | ¿Se entiende qué es, para quién sirve y qué pregunta responde? ¿Se conserva la explicación? |
| Definiciones y propiedad | ¿Cada término conserva el sentido de su fuente propietaria? ¿Hay divergencias entre versiones? |
| Argumentación | ¿La conclusión se sigue de las premisas? ¿Hay circularidad, supuestos ocultos, contraejemplos o falsadores omitidos? |
| Requisitos e interfaces | ¿La derivación, entrada/salida, alcance, autoridad y responsabilidad se pueden reconstruir? |
| Evidencia | ¿Se distinguen diseño, ejecución simbólica, ejecución de producto, comparación e independencia? ¿Una cita respalda realmente la afirmación? |
| Dependencias y consumidores | ¿Qué consume este documento y qué documentos, pruebas o presentaciones dependen de él? ¿Qué cambiaría aguas arriba y abajo? |
| Versiones y procedencia | ¿La ruta corresponde a la edición citada? ¿Se confunden congelado, vigente, borrador y antecedente? |
| Navegación | ¿Resuelven enlaces y anclas? ¿Hay fuentes desconectadas o referencias entrantes que quedarán obsoletas? |
| Límites de afirmación | ¿Se infiere aceptación, adopción, certificación, eficacia o endorsement sin evidencia? |
| Reproducción y cobertura | ¿Qué se comprobó, con qué método y resultado? ¿Qué falta para cerrar el hallazgo? |

Los defectos descubiertos se documentan; no se reparan en la fuente mientras se audita. Una relación propuesta se distingue de una relación observada. Un cambio en otro documento se referencia por su VNext y no se inserta indirectamente desde esta.

## 7. Conversación de auditoría

Cada entrada empieza por **«Auditoría realizada por…»** e incluye nombre/identificador real, fecha, fuente fijada, alcance leído, método, conflictos/dependencias y hallazgos con IDs estables. Si no se conoce el modelo o una identidad externa, indicar «no verificado»; no inventarlos.

Otro auditor puede responder al hallazgo por ID: acuerdo, discrepancia, evidencia adicional, contraejemplo o pregunta abierta. Debe registrar qué fuente leyó. Una segunda pasada del mismo agente se identifica como auto-revisión, no como auditor independiente. La participación de varios agentes o personas no se simula mediante varias firmas.

La conversación es acumulativa. No borrar una auditoría porque otra la contradiga; añadir una rectificación fechada y enlazada. Mantener visibles desacuerdos, hallazgos rechazados, retirados o reabiertos y las razones. Más auditorías no equivalen por sí mismas a validación.

## 8. Instrucciones y decisión de Iván

Toda propuesta cita la instrucción que autoriza prepararla. Su estado inicial es **propuesta; incorporación pendiente**. En una sección separada se registran las decisiones auténticas de Iván: fecha, alcance, IDs autorizados/rechazados y condiciones. Una sugerencia del auditor, silencio, archivo llamado «final», resultado de test o aprobación de otro auditor no sustituye esa decisión.

La petición del 6 de octubre autoriza preparar y conectar este procedimiento y la nota del README. No autoriza a incorporar propuestas técnicas futuras, alterar originales ni ejecutar automáticamente toda tarea enlazada. La revisión y una eventual publicación de cambios sustantivos deben respetar su autorización concreta.

## 9. Propuesta final: texto antes / texto después

Cada cambio tiene ID propio y una ficha completa:

```text
ID y estado:
Documento lógico, ruta, versión, commit y blob/hash auditados:
Instrucción de Iván que autoriza preparar la propuesta:
Hallazgos/auditorías relacionados:
Localización: sección/ancla + contexto exacto; líneas solo como ayuda.
Tipo: inserción / sustitución / supresión explícitamente propuesta.

TEXTO ANTES
[fragmento literal completo; sin elipsis ni paráfrasis]

TEXTO DESPUÉS
[fragmento literal completo que se propone dejar]

Razón y efecto semántico:
Fuentes y evidencia:
Dependencias afectadas y otras VNext relacionadas:
Comprobaciones necesarias y límites:
Decisión de Iván: pendiente, o referencia verificable a la instrucción concreta.
Incorporación: no ejecutada, o commit/versión y comprobaciones reales.
```

Para una inserción, citar el ancla intacta en ANTES y repetirla después del texto añadido en DESPUÉS. Para una supresión, reproducir todo lo que se propone quitar y expresar el resultado exacto. No usar «mejorar esta sección», resúmenes de páginas ni reemplazos globales ambiguos. Si hay varias coincidencias, añadir contexto hasta identificar una sola. En documentos binarios, precisar párrafo/tabla/celda/diapositiva y conservar su fuente; un extracto legible no reemplaza al original.

Las alternativas incompatibles conservan IDs separados. La propuesta consolidada final dice cuáles recomienda y qué conflictos siguen abiertos; no es una autorización para aplicar todas.

## 10. Incorporación posterior y cierre

Solo después de una instrucción explícita de Iván sobre los cambios concretos: releer la fuente actual, comprobar que ANTES sigue coincidiendo, conservar el predecessor, aplicar exclusivamente los IDs autorizados y verificar el diff y los consumidores afectados. Para fuentes congeladas, preparar el successor autorizado sin alterar la edición congelada. Registrar nueva versión, commit, controles, resultados y límites reales. Una carrera de edición bloquea la aplicación hasta revalidar; no se fuerza un reemplazo.

Actualizar la VNext existente con el resultado y abrir, si hace falta, una nueva época. Conservar auditorías, propuestas y decisiones anteriores. Verificar navegación y el control de documentos; un cambio de enlace no justifica reescribir un README.

La revisión global solo puede declararse completa con inventario cerrado, fuentes y relaciones cubiertas, excepciones explícitas, conversación atribuida y propuestas exactas para todos los hallazgos accionables. «Revisión completa» y «cambios incorporados» son estados distintos.

**Resultado de esta preparación:** método establecido y ejemplo del README abierto; resto del corpus pendiente de inventario y revisión bajo estas reglas.
