# VNext — Interfaz de evidencia, suficiencia y autoridad entre EA y MSCA

**6 de octubre de 2026 · Codex, mismo asistente de IA, revisión para una persona.** Una sola VNext del documento lógico 01B: [v0.2 actual](01B_EA_MSCA_INTERFACE_ANNEX_v0.2.md), texto completo § §1–8, commit `fa2c411c810950fb94924caae38938c52dfd5014`, blob `53c08ab1644d031ab0f7b53de5efa24ef5c8520f`; [v0.1 preservada](01B_EA_MSCA_INTERFACE_ANNEX_v0.1.md) comparte este expediente y no recibe otra VNext. Se comprobaron árbol/alias/expedientes activos. [Procedimiento](../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md). Canon intacto, propuestas pendientes de Iván.

## Primera pasada — qué aporta la interfaz

Texto completo examinado. Saber algo, tener una configuración suficiente, pertenecer legítimamente, tener un permiso y haber producido efecto son preguntas distintas. § §1/2/5.1 impiden que una capa responda por todas.

S/E/C/P/M parcial puede expresar el problema sin afirmar que esté resuelto. SUPPORTED se califica por objetivo, condiciones, evidencia, alcance, versión ytiempo; puede seguir sin autorización. Receipt y efecto se separan en §3/ §7; una emisión de comandos no completa por sí sola la misión.

La frontera multiobjetivo de §2 conserva restricciones no compensables y alternativas realmente examinadas. No proporciona un mínimo global ni compensa pérdida de calidad por ahorro. La idea es coherente como contrato propuesto; no prueba una integración funcionando.

Hallazgo acotado: al explicar por qué x no se llamaA, §2 conserva «situated assertion/scope».00M §1.1 defineA como resultado funcional entregado, y la cabecera/tabla §4 de 01B ya siguen esa lectura. Es una descripción local atrasada, no defecto demostrado de todo el payload o runtime.72 prepara una aclaración opcional.

## Segunda pasada — productor, consumidor y vuelta de evidencia

Cotejo material realizado con 01H y 01D completos,00M §1, ArticleII completo como procedencia y los contratos MSCA ya examinados. Las tablas se leyeron en ambas direcciones.

- **EA→MSCA, §4:** misión, ventana, soporte/reserva, exploración, residual y frescura deben referirse a la pregunta receptora. No originanS ni permisos. F6 aporta evidencia de postura histórica; el cierre operativo actual pertenece a Operation.
- **MSCA→EA, §5:** UNASSESSED, FAILED y UNRESOLVED son respuestas distintas, no se esconden para exportar sólo SUPPORTED. Capacidad/coste pueden cambiar qué evidencia conviene obtener; F2 conserva la propiedad de su ventana.
- **01H §5 ↔ 01B § §1/5:** representación vacía válida permanece UNASSESSED. Conectividad, exportar el esquema o recibir un EHD no acreditan alcance decontrol.
- **01B §7.1 ↔ 01D § §2/3/6:** si una acción usa RA como fundamento, su scope/versión/ventana y seguridad entran en la dependencia requerida. Un RAadvisory fuera de esa dependencia no veta por defecto una acción independiente. Nuevo permiso no cura RA desconocido; nuevo RA no renueva permiso.
- **01B §5.1 ↔ 01D § §3/6:** «MSCA permit» en 01D se interpreta como permiso asociado a esa operación, no emitido por el assessment. El dueño de autorización está expresamente separado en ambos textos. Conviene preservar esta lectura en cualquier aplicación; la abreviatura no demuestra por sí sola que una implementación conceda permisos erróneos.
- **ArticleII→Architecture/01B:** se conserva su pluralidad y procedencia; su vectorA(t) y sentido amplioMCA no sustituyen el kernel actual ni elA resultado funcional. No se edita el artículo histórico para que coincidan letras.

[01H VNext](01H_VNext.md), [01D VNext](01D_VNext.md), [00M VNext](00M_VNext.md), [Architecture](../../../standards/minimum-sufficient-control/00_ARCHITECTURE_VNext.md), [Composition](../../../standards/minimum-sufficient-control/03_COMPOSITION_VNext.md) y [Operation](../../../standards/minimum-sufficient-control/04_OPERATION_VNext.md) reciben las consecuencias.

**Límite:** el sitio del working paper urbano no fue recuperable en este intento. No se atribuye lectura de sus § §5.1/5.2 a lo que el propio 01B resume; fidelidad de esa tabla sigue pendiente. Tampoco se cierran todas las partes funcionales congeladas, perfiles de compatibilidad, fuente de RA, anexosDAOS o pruebas propuestas. Segunda abierta. v0.1 se verificó como predecessor rotulado; no se declara lectura completa de todas sus afirmaciones históricas.

## Tercera pasada — estructura y formato

Texto íntegro examinado. La lista de preguntas precede a los objetos; tablas de ida/vuelta y la secuencia final ayudan a reconocer responsabilidades. El estado de fuente versus candidato está visible antes de los payloads. Los IDs no se convierten en nuevos fields obligatorios.

La referencia semántica inicial protege gran parte de la lectura; el parentético de §2 merece precisión, sin renumerar componentes. La sección de extensibilidad introduce cuatro familias y enumera tres porque el perfil contractual está en §6.1: leer ambas juntas, no fabricar una familia omitida. No hubo render ni modificación de binarios.

## Cuarta pasada — comprensión humana

Relectura simulada, no participante independiente. Una explicación simple puede seguir un caso: hay información nueva, se evalúa si aún basta el control, se pide/valida permiso, se actúa y se comprueba el efecto. Un rechazo depermiso puede coexistir con SUPPORTED; UNRESOLVED tampoco equivale aFAIL.

El lector no debe interpretar la tabla urbana como topología obligatoria para todos. La fuente lo aclara; su fidelidad al paper sigue necesitando examen. La representación vacía y el retorno deestado negativo son parte del contrato, no errores de formato que haya que limpiar.

## Quinta — fuentes externas, alternativas y reutilización

**Contraste específico realizado, ampliación abierta.** [RFC9334](https://www.rfc-editor.org/rfc/rfc9334.html), Birkholz, Thaler, Richardson, Smith yPan, enero 2023, Informational: § §4.2/8.4/8.5/10 y aviso de derechos consultados. Resultado del Verifier y política del RelyingParty están separados; freshness conserva una posible carrera tras generar evidencia. Es un vecino reutilizable para frontera de evidencia y política, no prueba de suficiencia MSCA o delivery. Adaptación concreta necesita sujeto/scope, autoridad, versión e invalidación; no basta añadir un timestamp. TextoIETFTrust/BCP78 y componentes de código con licencia indicada por RFC; no se importa texto extenso/código/datos.

[ATHENA#34](https://github.com/FG-TIDA/themes/issues/34), Scalone,1octubre 2026, open: texto de la propuesta y dos comentarios leídos. Puede aportar una cadena acotada de delegación y revocación; la solicitud de un casoUC4 no es experimento realizado o protocolo adoptado. No resuelveSUPPORT/efecto ni recupera automáticamente credenciales. Fuente restringida XSTR no leída, derechos de una implementación no establecidos.

Juicio para 01B: proveedor de evidencias/credenciales y decisión receptora ya tienen antecedentes. La aportación candidata integra también suficiencia decontrol, estados parciales y retorno deefecto. Esa integración necesita fidelidad/perfil y comparación igualada; no diferencial demostrado frente a una composición competente. Las ocho pruebas de §7 siguen propuestas, no resultados.

## Conversación de auditoría

**Codex, respuesta al contraste:** leer completos los dos lados confirma condiciones que antes estaban citadas sólo por fragmentos. No convierte el enlace en interoperabilidad.72 acota una mejora deexposición; no autoriza corregir freezes ni cambiar un formato de intercambio.

El hallazgo de la referencia NIST en 01H se resuelve identificando en la auditoría los dos artículos del editor; no es motivo para fabricar un cambio a 01B. El siguiente trabajo sustantivo es ArticleIV/funciones y fuente urbana, conservando alcance real. Primera/tercera/cuarta textuales realizadas; segunda y quinta ampliada abiertas; sexta global pendiente.

## Plan de cambios — candidato 72, pendiente de Iván

**Ubicación:** último párrafo de §2 de 01B v0.2; viejo literal único verificado en el blob indicado. **Impacto esperado Medio; riesgo Medio; esfuerzo Medio; prioridad Siguiente; tanda 2 de coherencia EA/RA/MSCA.** El contexto ya preserva parte de la distinción; no se presume que este cambio sea necesario.

**Beneficio:** Evitar que la explicación local de la notación reduzca el resultado funcional A a una aserción/scope, cuando la cabecera y el propio payload ya usan 00M vigente.
**Riesgo:** El contexto ya conserva la semántica actual; sustituir una frase no debe parecer una taxonomía nueva, cambiar el payload o renombrar A(t) histórico de ArticleII.
**Coste:** Cotejar la cabecera, tabla §4,00M §1 y receptores antes de decidir si la precisión mejora lectura; mantener versiones y no cambiar pruebas antiguas.
**Orden/compatibilidad:** cotejar cabecera, tabla §4,00M §1 y 01D/Architecture; no alterar ArticleII ni tipos locales de pruebas. Decisión concreta pendiente; publicación de auditoría autorizada, incorporación no.

**Texto antes — viejo literal completo**

~~~~markdown
The symbol **x** is deliberately used for a candidate control configuration. It must not be called **A**, because A is already a component of the canonical EA qualified-position tuple (situated assertion/scope).
~~~~

**Texto después — propuesto completo**

~~~~markdown
The symbol **x** is deliberately used for a candidate control configuration. It must not be called **A**, because A is already the delivered functional result component of the canonical EA qualified position, interpreted for the declared producer, process, question, scope, capability and time. A claim or scope declaration can be part of that result, but does not define the whole A component.
~~~~

**Instrucciones de Iván:** preservar originales, unaVNext por unidad lógica, viejo completo, impacto/riesgo/esfuerzo y propuesta quirúrgica. Ningún cambio incorporado a la fuente por esta publicación; la decisión puede ser no modificarla.


---

## Relación material con funciones y taxonomía — 6 octubre 2026

**Codex, mismo asistente, contraste nuevo de evidencia.** Fuente `f7d8ed0846b301617197ade855d5237cbd2280f9`;03partes 1–3 completas,ArticleIVpartes 1–2 completas como procedencia y Foundation 1.1A/ § §2/3.4/3.5 focales. No otra firma independiente ni nueva ejecución.

03F3/F4 consume resultado/claimademás de susqualifiers; esto apoya no sustituir unresultado por una referencia opaca sin perfil. F7 ylas interfaces de §5 separan petición depermit/ejecución, y F9 conserva mismatches. La recepción de estado parcial en 01B no crea control suficiente. La lectura completa de 03/ArticleIV amplía el contraste previo; fidelidad urbana, matrices yrealizaciones pendientes no se cierran.73no cambia la aclaración opcional 72 deA.

Elorigen delcontraste está en [03 Functional VNext](03_FUNCTIONAL_VNext.md) y [Foundation VNext](01_FOUNDATIONAL_VNext.md). Allí se conserva laversión/fuente,explicación humana ylímites. Las demás lecturas previas no se repiten como si fueran nuevas; quinta ysexta mantienen sus estados reales. Canon,programas y resultados intactos.
