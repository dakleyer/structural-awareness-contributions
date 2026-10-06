# VNext — Linaje, identidad y autoridad del ACC

> **Expediente de revisión; no sustituye la fuente actual.** Una sola VNext del documento lógico. Auditoría realizada por **Codex, asistente de IA**, 6 de octubre de 2026. Se escribe para que una persona entienda el argumento y pueda continuar la revisión; no es una lectura humana independiente.

**Fuente:** [Linaje, identidad y autoridad del ACC](01_ACC_LINEAGE_IDENTITY_AUTHORITY_BINDING_PROFILE.md), texto completo, §§1–16; commit `26eb9ee1e5cccb348abe26a71f37d18a947af6bb`, blob `6059423eb0e2eca5a1281225e117f9f5017e3286`. [Plan de trabajo de Iván](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md) y [alcance y fuentes consultadas](../../governance/review/MSCA-kernel-lineage-gradient-2026-10-06/evidence.json). Cuerpo original preservado. Publicar auditorías está autorizado; incorporar propuestas requiere decisión concreta de Iván.

## Primera pasada — continuidad sin autoautorización

**Lectura de fondo y lógica realizada.** El perfil pregunta qué familia de contrato es ésta, quién está vinculado, quién puede emitir un sucesor y si sigue vigente. No confunde el identificador estable de familia con una lista de permisos que puede cambiar. Dos sujetos del mismo linaje pueden tener contratos diferentes; una comunicación entre linajes no crea ciudadanía común.

La división de §§5–9 es coherente: identidad del sujeto, facultad de emitir/mutar, admisibilidad contractual y permiso de ejecución no son intercambiables. Un contrato auténtico puede ser incompatible con el kernel; uno compatible puede no ser válido o autorizado. La continuidad necesita una autoridad externa establecida, no se demuestra por incluir un parent_id.

La mutación “self-mutable” está acotada por delegación explícita. No sirve para hacer que una oportunidad o una reducción de carga apruebe una ampliación de autonomía. Lo desconocido sobre linaje permanece UNRESOLVED_LINEAGE; ese resultado es una respuesta legítima.

## Segunda pasada — fuente, consumidores y evidencia

**Relaciones principales cotejadas; evidencia de realizaciones abierta.** Se leyó íntegramente 01I, la fuente de participación/governanza; su nota de reconciliación distingue el perfil de linaje y el MSCA disponible del ACC ligado a un rol. Architecture §§7.4/8 conserva exactamente esa composición. Role §§7/8 y Operation §§12–14 exigen vinculación y proceso de sucesor; ni el rol observado ni RepositionIntent son aprobación. Estas relaciones quedan registradas en sus VNext. [Architecture VNext](00_ARCHITECTURE_VNext.md) · [ACC VNext](01_ACC_VNext.md) · [Role VNext](02_ROLE_VNext.md) · [Composition VNext](03_COMPOSITION_VNext.md) · [Operation VNext](04_OPERATION_VNext.md) · [Gradient VNext](../../architectural-contributions/ecosystem-positioning/01_GRADIENT_VNext.md) · [01I VNext](../../research/ecosystem-awareness/baseline/01I_VNext.md).

Un conflicto de contratos sin dueño legítimo no se resuelve inventando precedencia. §11 lo conserva explícito. El pequeño estado ilustrativo de §13 omite varios campos de la tabla amplia; por ser ejemplo no obligatorio, no prueba que pueda omitirse una relación material de conflicto en una realización. No lo convierto en un esquema universal por esta revisión.

§12 enumera seis familias de mecanismos. Se contrastaron específicamente VC2 y los límites de delegación de RFC8693; no se certificó todo OIDC/OAuth/NIST, adaptadores, trust roots, revocación real ni autorización de organizaciones concretas. Esas comprobaciones y la cadena de evidencia de los perfiles mantienen abierta la segunda pasada. El texto es un contrato arquitectónico, no evidencia de que ese contrato se cumpla.

## Tercera pasada — tabla y ciclo

**Revisión del texto completo realizada.** La tabla de objetos precede al ciclo de mutación y la tabla de vecinos viene después: el lector sabe qué significado necesita antes de buscar tecnología. El ejemplo compacto no es un wire format obligatorio. “Same citizenship” se explica como continuidad de familia, sin identidad legal ni igualdad de permisos.

No hace falta añadir más IDs, formatos o una tabla de autoridad de autoridad. Los contratos externos citados deben llevar su propia versión y alcance cuando se seleccione una pieza; el cuerpo ya permite referencias. No preparo pares ficticios para una edición sin defecto demostrado.

## Cuarta pasada — lectura humana

**Simulación por Codex.** Una persona puede contar el caso así: el empleado sigue siendo el mismo, su participación tiene un contrato vigente, y cambiar una preferencia autorizada es distinto de concederse una función nueva. La herramienta que verifica identidad tampoco decide por sí sola la legitimidad de la nueva función.

Es útil leer §§5/6 antes de copiar el ejemplo§13. Una instancia UNBOUND es una plantilla disponible, no un participante autorizado. El perfil explica esos casos sin exigir que el lector conozca un proveedor concreto.

## Quinta pasada — credenciales, delegación y FG-TIDA

**Contraste específico realizado.** [VC Data Model2.0, W3C Recommendation15mayo2025](https://www.w3.org/TR/2025/REC-vc-data-model-2.0-20250515/), editores Sporny, Thibodeau, Herman, Cohen y Jones; §§4.9/4.10/5.9 y cabecera de derechos consultados. Validity/status pueden transportar afirmaciones ACC; §5.9 es no normativo y exige un marco de autorización acompañante. La pieza candidata es un perfil de afirmaciones sobre sujeto/emisor/vigencia/estado, no un contrato que apruebe mutaciones. Texto bajo licencia documental W3C indicada; implementación y datos no seleccionados, no importados. Debe definir fuente/status, criterios de confianza y extensión antes de su uso. Coincidencia existente en§12; no diferencial demostrado.

[FG-TIDA#34 ATHENA](https://github.com/FG-TIDA/themes/issues/34), Scalone/flyingeng, propuesta abierta1octubre2026: texto y dos comentarios leídos. La pregunta de cadena acotada/revocación es relevante; solicitar requisitos o un experimento no significa ejecutarlo o adoptarlo. [ITU TD236-WP1](https://www.itu.int/md/T25-SG17-260601-TD-WP1-0236/en), Co-RapporteurQ10/17,7junio2026, es metadata de propuesta con Word restringido aTIES: **su contenido no se leyó**. No se afirma que ATHENA implemente ACC. Derechos para importar texto/código y datos de esa pieza no establecidos; sólo comparación atribuida. La recuperación de un agente no se equipara a reinstalar una credencial revocada ni se adopta una interpretación jurídica de comentarios ajenos.

## Plan de cambios y estado

**Sin par nuevo para modificar este perfil.** La comparación aporta candidatos de adaptador, no demuestra un defecto del linaje. La aclaración60 pertenece a Operation: evita usar “autoriza” para la postura P3, cuyos otros gates ya son correctos. Incorporación pendiente de Iván; ningún contrato, autoridad o credencial real cambiado. Primera, tercera y cuarta textuales realizadas; segunda abierta; quinta específica realizada en alcance declarado. Sexta global pendiente.
