# Plan de trabajo — revisión para personas

**Versión vigente del procedimiento: 1.2 · 6 de octubre de 2026.**  
**Este es el plan de trabajo al que se refiere Iván:** el procedimiento de revisión del corpus enlazado desde el [README de Ecosystem Positioning](../architectural-contributions/ecosystem-positioning/README.md). Se mantiene este mismo documento y su misma ruta.

> **La revisión se escribe para que una persona pueda comprender el corpus, valorar sus argumentos y continuar el examen después. Su centro es la idea y el contenido. La trazabilidad ayuda a esa lectura; los códigos, etiquetas, hashes y comprobaciones automáticas se mantienen como apoyo adicional.**

Esta instrucción de Iván gobierna las pasadas que siguen. No basta contar enlaces, clasificar archivos o certificar que un registro está bien etiquetado. Hay que explicar qué sostiene el documento, por qué lo sostiene, qué demuestra su evidencia y qué dificultades encontrará un lector. Quien revisa conserva su identidad real: si interviene un asistente de IA, lo indica; escribir para personas no significa atribuirse una revisión humana que no ha ocurrido.

## Cuatro pasadas distintas en cada documento

Estas son las cuatro pasadas fijadas para **este corpus**. No se presentan como una norma universal de auditoría. Cada una tiene una pregunta, un trabajo y un resultado diferente; repetir el mismo escaneo con otro nombre no cuenta como otra pasada.

| Pasada | Qué se examina | Qué debe quedar escrito en la VNext del documento |
|---|---|---|
| **1. Fondo y lógica** | Qué problema aborda; cuál es su tesis; qué significan sus conceptos; qué supuestos necesita; si el razonamiento conduce a la conclusión; circularidad, saltos, ambigüedades, contraejemplos y límites. | Una explicación en lenguaje corriente del argumento, lo que se sostiene, dónde falla o queda abierto y por qué. No declarar una teoría válida porque esté bien estructurada. |
| **2. Evidencia y relaciones entre documentos** | Cada afirmación importante frente a su fuente: qué evidencia la respalda, qué versión se usó, qué grado de conclusión permite y qué documentos dependen de ella. Contrastar definiciones, hipótesis, requisitos, pruebas, resultados y consumidores. | Relaciones explicadas con pasajes concretos, evidencia pertinente y límites. Señalar dónde una conclusión se amplifica al pasar a otro documento o una premisa no está respaldada. |
| **3. Edición, estructura y formato** | Orden de exposición, títulos, párrafos, repetición, referencias, tablas, diagramas, notación matemática y consistencia editorial. Si el formato oculta una distinción o rompe el argumento, explicarlo. | Propuestas editoriales localizadas y su efecto sobre la comprensión. Distinguir una corrección de forma de una alteración de sentido; ambas permanecen como propuestas antes/después. |
| **4. Legibilidad y comprensión humana** | Leer como una persona nueva en el proyecto: qué entiende, dónde se pierde, qué términos necesita, si los ejemplos ayudan, si se explica la importancia y qué lectura debe seguir. Aplicarlo especialmente a los README. | Un relato de la experiencia de lectura y propuestas que permitan entender la idea sin conocer chats, códigos internos o la historia del repositorio. Registrar si la prueba fue una simulación de lectura por el mismo agente o participación efectiva de otra persona. |

### Cómo se trabaja de uno en uno

Para cada documento lógico, localizar su VNext existente; crear una sola si no hay. Leer la fuente y realizar una pasada definida, publicando su registro en esa misma VNext antes de avanzar. Repetir el examen con la pregunta de la siguiente pasada. Puede trabajarse en rondas sobre varios documentos cuando una dependencia lo requiera, pero cada documento conserva **cuatro registros distintos** y su propio estado. Un examen de otro documento no completa automáticamente una pasada de este.

La sección de auditoría de cada VNext se organiza con los títulos humanos de las cuatro pasadas. Debajo de cada título se acumulan las entradas y respuestas de revisores. Una pasada puede repetirse: conservar la entrada anterior y explicar qué nueva pregunta, evidencia o lectura aporta la repetición. No abrir una VNext por pasada ni una VNext de la propia VNext.

Cada entrada necesita solo lo suficiente para que otro lector la pueda continuar:

- quién la hizo y cuándo;
- qué fuente y parte leyó, y desde qué pregunta;
- qué encontró, con un pasaje o ejemplo concreto;
- por qué importa, qué evidencia lo apoya y qué sigue sin comprobarse;
- qué propone o qué desacuerdo deja abierto.

La identificación técnica detallada de fuentes, commits y resultados se conserva en una referencia o anexo breve. El texto principal cuenta lo que el lector necesita entender. No se generan cadenas de firmas ni registros sobre registros. La segunda lectura del mismo agente se identifica como tal, sin simular independencia.

## Pasadas de evidencia entre documentos

La segunda pasada incluye revisiones **cruzadas**, no solo la bibliografía interna de cada archivo. Pueden repetirse sobre una pareja o una cadena de documentos cuando aparezca un hallazgo nuevo. Por ejemplo: comprobar si una hipótesis llega a un requisito, si una prueba realmente respalda la interpretación del README, o si un resultado de alcance limitado se convierte en una afirmación general al reutilizarse.

Cada revisión cruzada debe decir en lenguaje corriente:

1. qué afirmación sale del documento de origen y en qué condiciones;
2. cómo la utiliza el documento receptor;
3. si conserva su significado, evidencia, alcance y limitaciones;
4. qué cambia en la conclusión si esa relación falla.

Registrar el resultado en **las VNext de los documentos afectados**, enlazando el mismo examen. Puede haber un relato completo en la VNext del origen y una respuesta o consecuencia concreta en la del receptor; no se exige copiar páginas iguales. Los hallazgos permanecen visibles en ambos lados. Un enlace que abre correctamente no prueba que la relación intelectual sea correcta.

## Conciliación final del corpus

Después de las cuatro pasadas de los documentos del alcance definido, realizar una última pasada conjunta. Su relato general vive en [README VNext](../architectural-contributions/ecosystem-positioning/README_VNext.md); cada consecuencia particular vuelve a la VNext del documento afectado. No sustituye las pasadas anteriores ni se cierra solo con un comprobador de enlaces.

La conciliación pregunta si el corpus sigue transmitiendo una idea coherente y comprensible. Debe buscar:

- **Enlaces rotos y trazas rotas:** tanto una ruta inexistente como una cadena fuente → argumento → requisito → prueba → conclusión que pierde significado, procedencia o alcance.
- **Documentos sueltos:** contenido sin una ruta de lectura clara, dependencias que nadie mantiene y textos valiosos desconectados. Proponer su ubicación de lectura sin mover ni borrar originales.
- **Confusión de versiones y autoridad:** borradores, antecedentes, deltas, exportaciones o hipótesis presentados como canónicos; versiones incompatibles que distintos lectores toman como vigentes.
- **Deriva de la teoría central:** textos que cambian una definición, premisa o propósito, o desarrollan una teoría distinta sin declararlo. Explicar exactamente en qué se apartan y si son extensión, alternativa, antecedente o conflicto. No forzar artificialmente su equivalencia ni descartar una alternativa valiosa.
- **Contradicciones y amplificación de evidencia:** resultados locales convertidos en suficiencia general, diseño presentado como ejecución, aceptación de un proceso presentada como adopción, o pruebas que se citan para una conclusión distinta de la que examinan.
- **Lectura humana del conjunto:** README que se vuelven índices crípticos, introducciones que no explican qué es y por qué importa, rutas repetidas que confunden y términos que cambian de sentido al pasar de una página a otra.

El resultado final debe permitir a una persona contar la idea central, identificar lo que se sostiene y lo que sigue abierto, recorrer su evidencia y reconocer las ramas del trabajo sin reconstruir conversaciones previas. Debe dejar también explícitas las exclusiones o fuentes que no pudieron revisarse. «Corpus conciliado» no implica que todas sus hipótesis sean verdaderas ni que sus propuestas ya estén incorporadas.

## Control técnico adicional

Comprobar enlaces, anclas, archivos, preservación y versiones sigue siendo necesario, pero se registra **como apoyo adicional**. Un número de checks, hashes o documentos no sustituye ninguna de las cuatro pasadas. Las etiquetas sirven para distinguir estados reales; no se crean nuevas capas de etiquetado como objetivo de la revisión. Conservar los originales y una única VNext por documento sigue siendo obligatorio.

## Cómo se registra el avance y cómo se termina

Cada VNext muestra, con los nombres anteriores, si la pasada está pendiente, parcial o terminada **en su alcance declarado**. No se cambia un estado a terminada por haber recuperado el archivo o añadido una nota. La revisión cruzada y la conciliación muestran sus límites de la misma manera. Una nueva evidencia puede reabrir una pasada ya realizada.

Las propuestas de modificación quedan al final de la VNext, con texto antes/texto después y las instrucciones de Iván correspondientes. Explicar primero el problema y su efecto sobre la idea o la lectura; adjuntar después la referencia técnica necesaria. Publicar una auditoría no autoriza a corregir el cuerpo canónico. La incorporación posterior continúa bajo las reglas de preservación y decisión concreta de Iván.

**Situación real al fijar este plan:** las seis VNext ya publicadas recibieron una exploración documental mixta. Es trabajo aprovechable, pero **no completa las cuatro pasadas de cada documento ni la conciliación final**. No se renombra aquella exploración para aparentar que esos trabajos ya se hicieron. El siguiente trabajo se registra con la pregunta de pasada que efectivamente se examine.

---

<details>
<summary>Procedimiento anterior y reglas de preservación — conservados íntegros como historia</summary>

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


</details>


## Redistribución de archivos y tres niveles de README — instrucción de Iván

**Adición vigente del plan, revisión 1.3 · 6 de octubre de 2026.** Esta aclaración conserva el texto anterior y gobierna las propuestas de organización del corpus.

Toda intención de redistribuir archivos, cambiar su ubicación, dividir o reunir documentos, modificar jerarquías o cambiar relaciones de lectura, dependencia o propiedad se examina **dentro de la revisión de los README**, en la **VNext del README que organiza los documentos afectados**. No se ejecuta como limpieza automática ni se decide solo en el VNext de un archivo aislado.

El corpus se entiende con **tres niveles de lectura**:

1. **Ecosystem Positioning:** entrada y explicación del conjunto.
2. **Awareness:** entrada a la parte correspondiente de la arquitectura y sus preguntas.
3. **Índices técnicos del corpus:** acceso ordenado a documentos, pruebas, casos y evidencia, como el índice del corpus de Ecosystem Awareness.

Los otros corpus vinculados conservan su función y su propietario; no se trasladan ni se subordinan de nuevo por esta nota. Sus rutas deben respetar ese límite de profundidad. Las referencias al programa padre o a fuentes externas dan contexto; no justifican una escalera interminable de README. Los README existentes de paquetes, fixtures o archivos históricos pueden ser documentación local, pero no crean automáticamente niveles cuarto, quinto o siguientes de navegación pública.

Cuando una propuesta afecte varias rutas, se registra en **las VNext de todos los README afectados**, con una explicación conjunta en README VNext de Ecosystem Positioning si cambia la organización del conjunto. Se reutiliza el expediente existente; se crea uno solo si hace falta. DOCUMENT_CONTROL registra el resultado autorizado y la conservación, sin reemplazar el lugar donde se examina la propuesta.

La revisión debe explicar para una persona:

- qué problema de comprensión o de relación se quiere resolver;
- cómo se lee y se relaciona el material hoy, y cómo se propone leerlo después;
- qué documentos, definiciones, pruebas y consumidores resultan afectados;
- qué enlaces y trazas podrían romperse, y cómo se conservarán los originales y la distinción entre vigente, borrador y antecedente;
- cuál es el cambio concreto antes/después y qué decisión de Iván permite incorporarlo.

La auditoría de un documento puede detectar una relación errónea y explicarla en su VNext. **Si propone cambiar la organización o relación entre archivos, debe devolver esa propuesta al README VNext propietario y a los demás README VNext afectados.** Una relación de contenido revisada no autoriza por sí sola mover archivos o crear nuevos niveles.

No se crea un README por cada carpeta ni un nuevo nivel por cada paquete. Cuando falte una ruta legible, se propone una adición al índice apropiado dentro de los tres niveles. Cualquier redistribución real sigue pendiente de la revisión y autorización concreta de Iván. El README de Ecosystem Positioning permanece solo-adición hasta esa revisión; no se borra, sustituye, reorganiza ni reformatea su texto existente.

Las denominaciones de niveles guardadas en controles o auditorías anteriores quedan como historia y deben conciliarse con esta instrucción actual. La propuesta antigua de describir Ecosystem Positioning como “Level 4” no debe aplicarse al modelo de lectura de este corpus. Esta adición no ejecuta ninguna redistribución ni cambia los documentos técnicos.


---

## Cuándo puede darse por terminada una revisión

**Adición al plan, revisión 1.4 · 6 de octubre de 2026.** Iván exige continuar ahora y comprobar la coherencia y vinculación del conjunto. Esta aclaración conserva todas las entradas anteriores.

Una pasada no se termina por rellenar cuatro casillas. Cada registro debe decir qué texto se leyó, qué pregunta distinta examinó, qué fuentes contrastó y qué queda pendiente. “Lectura de fondo realizada” puede ser cierta mientras evidencia, consumidores o figuras sigan abiertos. Ese documento no está cerrado.

Para el cierre de cada documento lógico hacen falta las cuatro lecturas documentadas, el contraste de sus afirmaciones con sus fuentes, el examen de quienes lo consumen y de los límites que conserva, y una respuesta concreta a cada hallazgo. Cuando el acceso solo permite un abstract o un fragmento, se registra ese alcance; no se cuenta como lectura completa del paper. No se borra una obligación pendiente bajo una etiqueta de aprobado.

La conciliación completa no consiste solo en probar que existe una ruta. Debe conservar significado, autoridad, versión y grado de evidencia a lo largo de cada relación material; explicar copias antiguas y documentos fuera de ruta; y revisar los README para una persona. Una fuente histórica válida puede seguir confundiendo al lector si parece actual.

La [conciliación de navegación](./review/EP_REVIEW_NAVIGATION_2026-10-06.md) amplía el recorrido transitorio y sus excepciones. El [inventario existente](./review/EP_REVIEW_COVERAGE_2026-10-06.tsv) conserva las épocas de cobertura. Ninguno afirma que la lectura semántica de todos los documentos esté terminada.

El avance se publica dentro de las VNext únicas y continúa desde el pendiente real. Se conservan originales, fuentes congeladas, instrucciones de Iván y propuestas exactas; no se aplican correcciones al canon, no se simula un revisor humano y no se repiten firmas como prueba de independencia.


---

## Alcance confirmado: todo Contributions y sus integraciones

**Adición al plan, revisión 1.5 · 6 de octubre de 2026.** Iván aclara que el corpus incluye todos los documentos que salen del README de Ecosystem Awareness y **todo el repositorio `dakleyer/structural-awareness-contributions`**, incluidas Ecosystem Positioning, Ecosystem Awareness, la rama de control MSCA y Regime Awareness. Esta instrucción amplía el criterio de alcance de §2: no se excluye un archivo por no ser alcanzable desde el README de EP.

El inventario debe cubrir el árbol completo del repositorio, no solo los enlaces de una entrada. Entran documentos vigentes, borradores, antecedentes, anexos, casos, submissions, interfaces, imágenes, presentaciones, PDF/DOCX, manifiestos, datos, resultados y código de soporte relevante. Cada archivo mantiene su clase y procedencia; inventariarlo no equivale a auditarlo ni lo convierte en canon.

Las copias históricas y los fragmentos se relacionan con su documento lógico y se examinan como procedencia/presentación. Los instrumentos de esta revisión permanecen sujetos a control de conservación y coherencia; no generan VNext de VNext ni una auditoría duplicada por copia. No se borran ni se descartan por esta clasificación.

Los candidatos antes descritos como “fuera del recorrido textual” quedan **incluidos en el alcance de revisión**. La ausencia de enlace es un hallazgo de navegación que hay que explicar, no una autorización para excluirlos. El [inventario de cobertura existente](./review/EP_REVIEW_COVERAGE_2026-10-06.tsv) recibe una época del árbol completo; el [mapa de alcance](./review/EP_REVIEW_REPOSITORY_SCOPE_2026-10-06.md) explica su lectura.

### Preservar las integraciones que ya existen

La revisión de una relación se hace en ambos extremos: qué produce la fuente, qué entiende el consumidor y qué conserva el retorno o feedback. Se cotejan significado, propietario, identidad de la operación/decisión, scope, versiones, tiempo/validez, dependencias, evidencia, autoridad y carga. Que un enlace resuelva o un campo conserve el nombre no prueba compatibilidad semántica.

La [conciliación de integraciones](./review/EP_REVIEW_INTEGRATIONS_2026-10-06.md) empieza por EA ↔ MSCA, EA ↔ RA y la composición conjunta 01D, y se extiende a Cartografía, signalling, ACC, operación/repositioning, interfaces de aplicación y pruebas. Cada hallazgo vuelve a las VNext de fuentes y consumidores afectados y a las VNext de los README propietarios.

Antes de incorporar una propuesta se necesita un análisis concreto de sus consumidores: qué comportamientos preserva, qué interpretaciones cambiarían y qué comprobaciones de compatibilidad hacen falta. Se conserva el contrato y la evidencia originales; no se renombran campos, cambian estados, recalculan manifests ni sustituyen interfaces durante la auditoría. Una precisión editorial también necesita este cotejo si altera el significado de una integración.

El alcance global no transfiere autoridad: EA, RA, MSCA, ACC y los propietarios externos conservan sus funciones. Las referencias entre ellos son relaciones de integración y lectura, no subordinación universal. Se mantienen los tres niveles acordados: **Ecosystem Positioning → Awareness → índices técnicos**, con enlaces laterales entre ramas.

Esta adición no declara que las integraciones estén todas revisadas ni que exista una validación de ejecución conjunta. Sus fuentes, evidencias y excepciones deben quedar cubiertas antes del cierre global. Los documentos canónicos se preservan y sus propuestas siguen pendientes de Iván.
