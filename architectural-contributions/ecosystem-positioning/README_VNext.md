# Continuación del plan — lectura del README y fundamentos

**6 de octubre de 2026 · revisión acumulativa 1.5.** La revisión sigue en este mismo chat con una continuación programada cada hora. El objetivo es completar las pasadas de todos los documentos del alcance y la conciliación final; publicar avances no cierra ese objetivo. Los estados siguientes describen trabajo real, no la mera existencia de una VNext.

| Documento | Fondo y lógica | Evidencia y relaciones | Edición/formato | Lectura humana |
|---|---|---|---|---|
| Este README | Lectura lógica realizada; validación de fuentes queda separada | Parcial: 00M/00N/A17 contrastados; otras cadenas y semánticas antiguas pendientes | Inspección textual realizada; render/exportaciones pendientes | Relectura simulada realizada; lector independiente pendiente |
| [00M y su VNext](../../research/ecosystem-awareness/baseline/00M_VNext.md) | Texto completo examinado | Soporte limitado de seis referencias y relación con 00N/README examinado; no papers completos ni transferencia de todos los proofs | Texto y notación examinados; figuras aparte | Relectura simulada examinada |
| [00N y su VNext](../../research/ecosystem-awareness/baseline/00N_VNext.md) | Texto completo examinado | Parcial; faltan once contrastes primarios | Markdown examinado; figura aparte | Relectura simulada examinada |

00M/00N tienen hashes de publicación: sus originales permanecen intactos y la nota de revisión está en [la ficha externa de 00M](../../research/ecosystem-awareness/baseline/00M_REVIEW_CARD.md) y [la de 00N](../../research/ecosystem-awareness/baseline/00N_REVIEW_CARD.md). Se abrió una sola VNext por nota, al comprobar que no había ninguna. La revisión cruzada 00M→00N queda explicada en ambos expedientes.

**Siguiente trabajo concreto:** terminar la segunda pasada de 00N sobre sus once fuentes; después examinar la fidelidad entre la semántica actual de 00M y las premisas de A23/otras pruebas antiguas, sin modificar esos resultados. Los demás documentos conservan su ciclo pendiente. La conciliación global sigue abierta.

---

> [!NOTE]
> **Revisión para personas · instrucción de Iván del 6 de octubre de 2026.** Revisión acumulativa 1.3. El [plan de trabajo](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md) exige cuatro pasadas diferentes, registradas en esta misma VNext: **fondo y lógica; evidencia y relaciones; edición y formato; legibilidad humana**. Después habrá una conciliación del corpus, con consecuencias en cada VNext afectada. El centro es comprender y cuestionar la idea; códigos y comprobaciones técnicas quedan como apoyo. La exploración mixta publicada antes se conserva, pero no se cuenta como cuatro pasadas terminadas.

### Estado del ciclo de revisión de este documento

| Pasada | Estado al adoptar el plan |
|---|---|
| Fondo y lógica | Parcial: hay observaciones exploratorias; falta su examen diferenciado completo. |
| Evidencia y relaciones entre documentos | Parcial: relaciones seleccionadas; faltan revisiones cruzadas completas. |
| Edición, estructura y formato | Pendiente como pasada propia. |
| Legibilidad y comprensión humana | Pendiente como pasada propia. |
| Conciliación final del corpus | Pendiente. |

**Cómo se continúa:** añadir cada pasada y sus respuestas en la sección de auditoría de esta VNext, explicando hallazgos y consecuencias para un lector. Conservar los registros anteriores y terminar con propuestas antes/después. Esta nota organiza el trabajo; no afirma que esas pasadas se hayan realizado ni altera el texto canónico.

---

> [!NOTE]
> **VNext · revisión acumulativa 1.2 · 6 de octubre de 2026.** Primera pasada secuencial de seis expedientes publicada y comprobada. El resumen de cierre de pasada está después de las épocas anteriores y las propuestas continúan pendientes. Se conservan todos los textos previos; «primera pasada» no significa auditoría completa del corpus.

> [!NOTE]
> **VNext · revisión acumulativa 1.1 · 6 de octubre de 2026.** Primera pasada documental publicada con autorización de Iván. El expediente 1.0 que sigue se conserva íntegro como historia; sus estados «pendiente» describen aquella entrega. La nueva auditoría y las propuestas pendientes aparecen después de ese expediente. Fuente vigente del README auditado: commit `1d24b7bfe88fa366e6c619fa88f6f7904d1380db`, blob `9c31f225b5364d0d681df455d6e5d809786470e3`. No se cambia el README canónico.

## Visión general — qué se revisa y en qué orden

Ecosystem Positioning propone que un participante siga situado cuando cambian evidencia, dependencias, rol o autoridad. EA califica lo que puede sostenerse; Regime Awareness examina la vigencia del marco; MSCA evalúa suficiencia de control y encauza reposicionamiento bajo autoridad legítima. Un resultado local correcto no demuestra por sí solo que la decisión compuesta siga justificada.

El corpus tiene tres cadenas relacionadas, con obligaciones diferentes:

1. **Fundamentos → principios → requisitos:** explicar el problema, formular invariantes y declarar S1–S14/T1–T4/H1–H6 con criterios de falsación. Una relación de trazabilidad no es una demostración causal.
2. **Arquitectura → interfaces → aplicación:** EA/RA/MSCA, cartografía, signalling, ACC y gradiente; 04 genérico → 05 ideal FG-TIDA → 05A filtro de estado público. La proyección ideal no acredita disponibilidad o adopción.
3. **Escenarios → fixtures/oracle → ejecución → comparación:** seis familias 00E–00J, pruebas simbólicas y extensibilidad condicionada. A23 mantiene P3/P5/P6 abiertos; ejecuciones simbólicas no certifican superioridad del producto ni comparación independiente.

**Mapa inicial reproducible:** [inventario de rutas y cobertura de esta pasada](../../governance/review/EP_REVIEW_COVERAGE_2026-10-06.tsv) y [alcance/método legible por máquina](../../governance/review/EP_REVIEW_SCOPE_2026-10-06.json). Son índices por archivo, no un inventario definitivo de documentos lógicos.

El README contiene 212 ocurrencias de enlaces según el extractor declarado, 102 destinos locales distintos (95 Markdown), ocho URL externas distintas y 16 referencias locales con ancla. Las rutas locales y esas anclas no presentan ausencias en esta comprobación estática. La exploración de enlaces de los 95 Markdown reúne 1.903 referencias locales hacia 420 destinos; 229 destinos Markdown de esa segunda frontera no habían sido recuperados en ese corte. Esto mide navegación, no lectura semántica completa. Se excluyen los nuevos enlaces de este propio informe de esos recuentos, fijados al commit de partida.

### Secuencia: reutilizar cada VNext existente

| Orden | Espacio existente | Trabajo de esta primera pasada |
|---|---|---|
| 1 | Este README VNext | Visión general, límites, relaciones y auditoría del router. |
| 2 | [Requirements VNext](../../research/ecosystem-awareness/baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) | Coherencia de la revisión, claridad de alcance y correspondencia con S/T/H. |
| 3 | [04 VNext](../../research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) | Requisitos → interfaz genérica; candidates frente a baseline. |
| 4 | [05 Ideal VNext](../../research/ecosystem-awareness/fg-tida/interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) | Proyección ideal y propiedad semántica de Themes. |
| 5 | [05A Current VNext](../../research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) | Evidencia y fecha del filtro de estado público. |
| 6 | [Benchmark v0.3, VNext de diseño ya existente](../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md) | Auditoría en el mismo borrador; no abrir un benchmark VNext paralelo. |

Cada paso se publica y verifica antes de editar el siguiente. La tabla es una secuencia, no una afirmación de que todos los pasos estén cerrados. Las fuentes congeladas y el resto del corpus siguen pendientes de sus auditorías de profundidad y expedientes correspondientes.

---

# Ecosystem Positioning README — VNext

**ID:** EP-README-VNEXT · **Revisión de este expediente:** 1.0 · **Fecha:** 6 de octubre de 2026  
**Estado:** expediente único de auditoría y propuestas; no canónico; no successor aprobado.  
**Fuente auditada:** `architectural-contributions/ecosystem-positioning/README.md`  
**Commit de partida:** `b8f935f2a1fbac17f8aac24be60a3e65cd2c2b98`  
**Blob de partida:** `551eb4d55eb0e4efdfe3d81f506da81a1e93e8ab`  
**Versión técnica declarada por el README:** no declarada; no se inventa un número Ve.  
**Procedimiento:** [revisión segura del corpus](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md).

Esta VNext identifica la fuente para poder auditarla; no sustituye su versión vigente ni le transfiere autoridad. Contiene una revisión de preparación y una adición de navegación autorizada. **La auditoría técnica completa del README y de sus dependencias está pendiente.** Ninguna auditoría global se da por terminada aquí.

## 1. Instrucciones de Iván

Petición del 6 de octubre de 2026: preservar los documentos; abrir una sola VNext por documento si no existe; auditar primero el documento y sus relaciones; permitir auditorías sucesivas y respuestas entre auditores; registrar quién realizó cada auditoría; terminar con propuestas exactas de texto antes/texto después y mantener aquí las instrucciones de Iván. Pidió crear el procedimiento y conectar su ruta desde el README mediante una adición, conservando su lectura humana y todo su texto previo.

**Corrección posterior de Iván:** «VNext». Este expediente usa esa denominación.

**Autorización concreta de esta entrega:** crear y publicar el procedimiento, abrir esta VNext y añadir al inicio del README la nota que enlaza ambos. La actualización aditiva de DOCUMENT_CONTROL registra la ruta y el nuevo blob protegido exigidos por sus controles. Esta autorización no incorpora cambios técnicos futuros ni activa experimentos o tareas enlazadas.

## 2. Auditoría de preparación y relaciones

### Auditoría realizada por Codex — EP-README-AUD-001

**Fecha:** 6 de octubre de 2026. **Identidad:** agente Codex de este chat; sin designación como auditor externo independiente. **Modelo:** no verificado. **Método:** lectura del README público y DOCUMENT_CONTROL, comparación de sus blobs con el árbol Git del commit de partida, inventario de nombres vNext existentes y verificación prevista de adiciones, enlaces y conservación.

**Alcance:** controles de preservación, ubicación del procedimiento y de esta VNext, separación de propuesta/versión vigente y duplicación de expedientes. No es una evaluación técnica completa de cada afirmación, prueba ni dependencia transitiva del README.

| Hallazgo | Observación | Consecuencia / disposición |
|---|---|---|
| EP-README-F001 | La copia local pertenece al commit `c8672ae751c458bcafbf2aff78b5bdc5f6071614`; GitHub main está en el commit de partida indicado arriba. | Preparar la adición sobre la fuente publicada y fijada, sin sobrescribir la copia local atrasada. |
| EP-README-F002 | No existe `README_VNext.md` ni otro expediente vNext de este README en el árbol completo consultado. | Abrir solo este expediente; no crear uno por auditor. |
| EP-README-F003 | Existen Review & Delta para Requirements, 04, 05 y 05A. | Reutilizarlos en sus respectivas auditorías; no crear duplicados. No se modifican en esta entrega. |
| EP-README-F004 | DOCUMENT_CONTROL protege el cuerpo humano del README y exige registrar el nuevo blob ante una adición autorizada. | Añadir nota breve, preservar todo el cuerpo y añadir una entrada fechada al control, sin reescribir su historial. |
| EP-README-F005 | El README enlaza requisitos, arquitectura, escenarios, evidencias, interfaces y presentaciones con propietarios distintos. | La revisión completa requiere inventario transitivo, relaciones entrantes/salientes y límites de evidencia; esta preparación no la cierra. |
| EP-README-F006 | Añadir una nota interna a fuentes congeladas o binarias alteraría su identidad. | El procedimiento exige ficha externa y original intacto para esas fuentes. |

**Relaciones de este expediente:** README de Ecosystem Positioning → procedimiento de revisión → VNext única del README. DOCUMENT_CONTROL registra este nuevo soporte de revisión sin añadir un router ni cambiar la jerarquía del programa. El vínculo a la fuente auditada es procedencia; esta VNext no aporta nuevos requisitos, pruebas ni definiciones a EA, Regime Awareness o MSCA.

## 3. Conversación de auditoría

Esta sección acumulará entradas identificadas y fechadas. Las respuestas citarán los IDs de auditoría y hallazgo, la fuente realmente leída y la evidencia. Se preservarán discrepancias y rectificaciones. **No hay una segunda auditoría independiente registrada todavía.** Una comprobación posterior del mismo agente se rotula como auto-revisión.

## 4. Decisiones e instrucciones posteriores de Iván

| ID | Fecha | Instrucción / alcance | Estado |
|---|---|---|---|
| IVAN-20261006-EP-REVIEW-SETUP | 6 de octubre de 2026 | Crear el procedimiento, conectarlo al README mediante adición y preservar el cuerpo de los documentos. | Autorización de preparación y conexión; no aprobación de deltas técnicos futuros. |
| IVAN-20261006-VNEXT-NAME | 6 de octubre de 2026 | «VNext». | Denominación aplicada. |

## 5. Propuesta quirúrgica final

### EP-README-DELTA-001 — nota de versión/revisión y enlace

**Tipo:** inserción de navegación al inicio. **Fuente:** ruta, commit y blob indicados en la cabecera. **Localización:** antes de la primera línea exacta `<div align="center">`. **Instrucción:** IVAN-20261006-EP-REVIEW-SETUP y corrección IVAN-20261006-VNEXT-NAME. **Hallazgos relacionados:** F002, F004 y F005.

**TEXTO ANTES**

```markdown
<div align="center">
```

**TEXTO DESPUÉS**

```markdown
> [!NOTE]
> **Review note · 6 October 2026 · navigation addition only.** The existing text below is preserved verbatim. Read the [corpus review procedure](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md) before proposing a change. This README has one [VNext audit and before/after workspace](./README_VNext.md), kept separate from the current canonical text. Audits and proposals do not change the canonical corpus; substantive changes require Iván's explicit instruction.

<div align="center">
```

**Razón:** dar acceso humano al método y al único expediente de este documento. **Efecto semántico técnico:** ninguno; no se modifica ninguna afirmación existente. **Dependencias afectadas:** dos enlaces nuevos, este expediente y el procedimiento; DOCUMENT_CONTROL registra el blob resultante. **Comprobaciones:** igualdad exacta del cuerpo anterior, resolución de rutas nuevas, ninguna eliminación/alteración de líneas anteriores, diff limitado al alcance autorizado y ausencia de VNext duplicada.

**Decisión de Iván:** la adición de conexión está autorizada por la petición de este chat. **Incorporación:** consultar el registro de publicación/verificación de esta entrega en DOCUMENT_CONTROL; si no existe confirmación de commit y readback, no dar la publicación por realizada.

### Propuestas sustantivas

**Ninguna preparada o autorizada en esta entrega.** Los hallazgos técnicos futuros se auditarán y propondrán aquí con sus propios IDs, texto antes/después, evidencia, dependencias e instrucción de Iván. Esta ausencia no equivale a que el corpus carezca de defectos.


---

## Nueva época — auditoría del README y de sus relaciones

### Auditoría realizada por Codex — EP-README-AUD-002

**Fecha:** 6 de octubre de 2026. **Naturaleza:** continuación y auto-revisión del mismo agente; no auditoría independiente. **Fuente:** README completo del commit `1d24b7bfe88fa366e6c619fa88f6f7904d1380db`, blob `9c31f225b5364d0d681df455d6e5d809786470e3`. **Método:** lectura íntegra del router en tres tramos, contraste con DOCUMENT_CONTROL y pasajes de Requirements/A23; extracción estática de enlaces y anclas de sus destinos Markdown. Se recuperaron textos para navegación; recuperación no se contabiliza como auditoría semántica.

**Instrucción de Iván:** «Primero des una visión general»; trabajar «de uno en uno» sobre la VNext existente y crear «esta revisión de auditoría en primer lugar». Autoriza publicar los expedientes de revisión. No se interpreta como aceptación automática del texto propuesto para fuentes canónicas.

| ID | Hallazgo, evidencia y consecuencia | Estado |
|---|---|---|
| EP-README-F007 | En «Where to go deeper — Level 3» aparece literalmente «This page is intentionally the complete **Level-2 orientation**». DOCUMENT_CONTROL §3 exige «complete Level-4 human landing page» y §1 reserva Level 2 al programa Structural Awareness. La nomenclatura de niveles es inconsistente; no afecta por sí sola las definiciones arquitectónicas. | Propuesta editorial DELTA-002 pendiente; no se corrige la fuente. |
| EP-README-F008 | «Technical proof map» y «Canonical reuse route» mantienen A23 parcial y exigen BaseGuarantee + X3/X4. A23 confirma retirada del cierre all-six y contraejemplos P3/P5/P6 del modelo parcial. Esa consistencia es positiva, pero este auditor no reproduce las pruebas ni certifica su fidelidad matemática. | Correspondencia documental comprobada; prueba/reachability y ejecución pendientes. |
| EP-README-F009 | Las nuevas definiciones A/B/C/D se remiten a 00M y los PPTX se etiquetan exportaciones anteriores. Cambiar la lectura de un término no revalida los proofs/results antiguos; Requirements VNext también conserva esa advertencia. | Rastrear las traducciones y premisas en auditorías por documento; no afirmar invalidación o revalidación general. |
| EP-README-F010 | Los 1.903 enlaces locales de la primera frontera tienen destinos en el árbol, pero la frontera adicional no está completamente leída ni clasificada por propiedad semántica. Los documentos binarios se verificaron solo como rutas/blobs, no por su contenido. Las URL externas no se comprobaron en vivo. | Cobertura abierta, incluida atribución de referencias entrantes fuera del subconjunto explorado. |
| EP-README-F011 | El expediente anterior fijó el README anterior a la nota publicada. En esta época el baseline es el README con esa adición ya publicada, no una nueva versión técnica inventada. | Procedencia aclarada en la nota actual; se preserva la época anterior. |

### Conversación / respuesta a la preparación anterior

**Codex, 6 de octubre de 2026, respuesta a AUD-001/F002/F004:** se confirma la publicación del setup en [commit 1d24b7b](https://github.com/dakleyer/structural-awareness-contributions/commit/1d24b7bfe88fa366e6c619fa88f6f7904d1380db). DELTA-001 es una inserción de navegación ya aplicada, no una propuesta técnica pendiente. El estado de la entrega anterior se conserva literalmente como historia. Esta segunda pasada añade profundidad y límites; no constituye la segunda auditoría independiente solicitada como posibilidad del procedimiento.

### Decisión de Iván — IVAN-20261006-START-SEQUENTIAL-AUDITS

Iván aceptó el procedimiento y autorizó continuar/publicar. Alcance observado: visión general en la VNext existente y auditorías secuenciales dentro de los espacios existentes. La publicación de auditorías está autorizada; la incorporación de correcciones al corpus canónico sigue pendiente de decisión sobre sus IDs concretos.

## Propuestas quirúrgicas de esta época — incorporación pendiente

### EP-README-DELTA-002 — nivel de lectura del router

**Fuente:** README del commit y blob fijados en AUD-002. **Localización:** sección «Where to go deeper — Level 3», oración única. **Hallazgo:** F007. **Preparación:** autorizada por IVAN-20261006-START-SEQUENTIAL-AUDITS. **Tipo:** sustitución editorial propuesta; no aplicada.

**TEXTO ANTES**

```markdown
This page is intentionally the complete **Level-2 orientation**. Technical ownership remains below it.
```

**TEXTO DESPUÉS**

```markdown
This page is intentionally the complete **Ecosystem Positioning architectural-contribution orientation (Level 4 in DOCUMENT_CONTROL)**. Technical ownership remains with the linked corpora.
```

**Razón/efecto:** hacer coincidir la nomenclatura con el control de navegación sin modificar ownership, requisitos ni evidencia. **Dependencias:** DOCUMENT_CONTROL §1/§3; título «Where to go deeper — Level 3» deberá examinarse junto con esta propuesta antes de incorporarla, pues se conserva por ahora. **Comprobación requerida:** una sola coincidencia del texto anterior y revisión de todo el vocabulario de niveles. **Decisión de Iván sobre incorporación:** pendiente. **Incorporación:** no ejecutada.

### Otras propuestas

No se propone cierre de A23, modificación de A/B/C/D ni promoción del benchmark. F008–F010 son obligaciones de revisión pendientes, no justificación para cambiar fuentes sin evidencia. La auditoría del README queda **parcial** por dependencias, fuentes externas y binarios pendientes, aunque su cuerpo fue leído completo.


---

## Cierre de primera pasada secuencial — EP-README-AUD-003

**Auditoría realizada por Codex:** auto-revisión de conservación y publicación del mismo agente, 6 de octubre de 2026. No hay segundo auditor independiente. Esta sección consolida estados; no amplía el alcance semántico de cada auditoría.

| Orden | VNext existente | Commit de su auditoría | Estado |
|---|---|---|---|
| 1 | [README / visión general](../../architectural-contributions/ecosystem-positioning/README_VNext.md) | [c8294165](https://github.com/dakleyer/structural-awareness-contributions/commit/c82941651347dfa1294e27d66c3dda35a975c6b2) | Auditoría R1 publicada; source correction pendiente. |
| 2 | [Requirements](../../research/ecosystem-awareness/baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) | [400e1cc0](https://github.com/dakleyer/structural-awareness-contributions/commit/400e1cc048e26652b46e6276e7c9b365961c2bad) | Auditoría R1 publicada; source correction pendiente. |
| 3 | [04 genérico](../../research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) | [9e785ab7](https://github.com/dakleyer/structural-awareness-contributions/commit/9e785ab76f7cfacbccbfa8280f3ef0c4ef476c1d) | Auditoría R1 publicada; source correction pendiente. |
| 4 | [05 Ideal](../../research/ecosystem-awareness/fg-tida/interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) | [bf3e0109](https://github.com/dakleyer/structural-awareness-contributions/commit/bf3e0109843471ab7646141d3508fcc1b5e651b9) | Auditoría R1 publicada; source correction pendiente. |
| 5 | [05A Current](../../research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) | [b16bcba8](https://github.com/dakleyer/structural-awareness-contributions/commit/b16bcba8946c75eb608e2458fa5d4fe241fccc60) | Auditoría R1 publicada; source correction pendiente. |
| 6 | [Benchmark v0.3](../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md) | [8c5d22fb](https://github.com/dakleyer/structural-awareness-contributions/commit/8c5d22fb81c0abf0b33f912ce4c40497f798771f) | Auditoría R1 publicada; source correction pendiente. |

Cada auditoría fue publicada y leída de vuelta antes de editar la siguiente. Se conservaron los cuerpos anteriores y una copia exacta de cada expediente previo en el archivo público. No se abrió otro VNext para ninguno de esos seis documentos. Se verificaron **1.095 blobs originales distintos de esos expedientes** sin cambios frente al commit de inicio; entre ellos están el README canónico, Requirements congelado, 04 baseline, 05partes/05A bridge, presentaciones, resultados y fixtures.

**Resultado de esta pasada:**

- Navegación: discrepancia Level2/Level4 y mapa inicial de rutas, con frontera todavía abierta.
- Requirements: recuento de escenarios y fecha de cobertura ambiguos; coverage mapping no implica suficiencia; CAND-R4 requiere adjudicación.
- 04: H06/A_ref, roles producer-relative y 176 entradas pendientes de revalidación; no promotion por una tabla ilustrativa.
- 05: 00I simultáneamente existente y «None committed»; peer characterization con reserva pública; owner/process approval no equivale a contrato adoptado.
- 05A: consulta de comentarios separada de reproducción de cifras; fechas/revisiones porfila y sources faltantes pendientes.
- Benchmark: W1mapping presente frente a gate declarado pendiente, Q0/exclusión post-outcome, C15 sin etapa y protocoloscomparativos aún sin freeze.

Se leyeron catorce comentarios públicos identificados de Themes13/16/21/23. La comprobación se limita a sus afirmaciones y metadatos, sin afirmar revisión completa de threads, rawdatasets, attachments o implementaciones. [Registro de pasada](../../governance/review/EP_REVIEW_PASS1_2026-10-06.json).

**Reproducción del mapa:** [verificador offline](../../governance/review/EP_REVIEW_LINK_SCAN_2026-10-06.mjs). Se ejecutó contra un export local de las fuentes del baseline y pasó: 212 links, 102 destinos locales, 95 Markdown, 16 anchors locales, 1.903 refs de primera frontera y420 destinos; sin rutas ausentes ni anclas directas sospechosas. El input guarda los95 textos de la primera frontera; la consulta adicional a DOCUMENT_CONTROL se registra porruta para reproducir el recuento229. El input público-local no se duplica completo en GitHub: se reconstruye desde las rutas/blobs y commit del ScopeJSON. El escáner es comprobación de enlaces, no prueba de semántica ni test experimental.

### Instrucciones y siguiente profundidad

La autorización de Iván para publicar las auditorías se ha ejecutado. Las propuestas de fuentes permanecen pendientes de aceptación por ID; no se asumió autorización de aplicar correcciones técnicas o editar fuentes congeladas.

La próxima profundidad es por documento lógico: identificar VNext existente o crear una sola cuando no exista, fijar su fuente y propietario, auditar definiciones/argumentos/consumidores y conversar sobre los hallazgos ya abiertos. Primero son materiales 00M/00N/traceability y A23/00I/H06; el inventario de esta pasada no asigna aún ownership ni expediente a cada uno de los420 archivos. Binarios y frozen sources necesitan fichas externas. La frontera transitiva y los inboundlinks del repositorio completo quedan abiertos; no se declara revisión global terminada.

## Consolidación de propuestas — siguen pendientes

Las propuestas nuevas de esta pasada están al final de cada VNext propietario y tienen sus textos ANTES/DESPUÉS e instrucciones de Iván. En este README VNext permanece **EP-README-DELTA-002** sobre la frase Level2; no se ha incorporado. DELTA-001 de la época inicial fue la nota de navegación ya publicada. AUD-003 no añade un cambio técnico nuevo ni convierte una recomendación en aprobación.


---

## Primera pasada del README — fondo y lógica

**Revisión realizada por Codex, 6 de octubre de 2026:** lectura completa del README canónico y relectura dirigida a su argumento, límites de evidencia y relaciones. Es el mismo agente, no una firma independiente.

La idea central se entiende mejor como una pregunta de dependencia: una identidad, permiso o resultado puede seguir siendo válido localmente mientras cambian las condiciones que lo hacían suficiente para una decisión conjunta. El README propone conservar una vista calificada, detectar cuándo necesita revisión y dejar la actuación a su propietario legítimo. Es una tesis sobre el límite de la corrección local; no equivale a afirmar que toda composición falla ni que EA la resuelve ya.

El argumento distingue explicar el fallo, derivar principios, formular requisitos, diseñar una implementación y probarla. Las fórmulas de transferencia de casos exigen una garantía de base y conservación de conformance; el texto reconoce que A23 no la suministra para los seis principios. La lectura es internamente coherente cuando esas condiciones se mantienen junto a la conclusión. No las convertimos en un teorema de éxito para cualquier industria.

Los ejemplos de robots, movilidad, refunds y derechos cumplen una función explicativa. Sus tecnologías están ligadas a perfiles de diseño; no se debe leer la narración como resultado de un producto real. La misma cautela rige “self-healing”: el texto lo define como recuperación de operación justificada, con actuación autorizada aparte, y describe una posibilidad de arquitectura. El lector no debe deducir eficacia demostrada a partir del término.

**Fondo pendiente:** verificar las premisas y correspondencias de cada cadena científica es parte de las VNext propietarias. La coherencia del relato del README no acredita automáticamente esas fuentes.

## Segunda pasada del README — evidencia y relaciones

**Revisión realizada por Codex, 6 de octubre de 2026:** contraste dirigido de 00M completo, 00N completo y el aviso de alcance de A17. Otras cadenas del README siguen pendientes; no se renueva la cifra de enlaces como prueba semántica.

La referencia a 00M sostiene el significado actual de A/B/C/D, no un certificado de la composición. En [00M VNext](../../research/ecosystem-awareness/baseline/00M_VNext.md) se examinó la diferencia entre conservar una respuesta a una pregunta declarada y conseguir una implementación útil. [00N VNext](../../research/ecosystem-awareness/baseline/00N_VNext.md) conserva que utilidad, plazo, costo y respuesta autorizada necesitan condiciones adicionales. El README debe llevar esa frontera consigo cada vez que vuelve desde “plausibility” al diseño o a las pruebas.

[A17](../../research/ecosystem-awareness/baseline/00K_A17_DOCUMENTATION_REPRODUCIBILITY_AND_PROOF_MAP_v0.1.md) explicita que los proofs/fixtures conservan su vocabulario de origen. Añadir 00M como definición actual no demuestra que el resultado antiguo se transfiera a la nueva frontera B/C. Esa es una traza intelectual que todavía requiere trabajo, aun cuando sus enlaces abran y sus cifras de tests permanezcan intactas. El hallazgo se mantiene también en la VNext de 00M; la investigación de los proofs mismos queda para sus expedientes.

La diferencia de hashes de 00M también fue rastreada: el registro corresponde al payload publicado en d855f8d, mientras el actual incorpora la adopción semántica de 135d8ff. Ambos estados son reconstruibles y se explican en 00M VNext; un filename v0.8 por sí solo no identifica esos bytes. No se modifica el manifest histórico.

Esta segunda pasada sigue **parcial**. La cuenta de casos/regresiones es reconstruible como registro, pero no sustituye el examen de fidelidad de cada fórmula, cada oracle y cada comparación. Tampoco implica replicación independiente de una hipótesis completa.


### Conciliación del alcance R01 — tareas 1 y 2, 6 de octubre de 2026

**Codex /root, chat 01a11096-57f0-72b2-bd57-7d8816673410; mismo asistente, no revisor externo.** Instrucción de Iván: «realiza las tareas 1 y 2», referida al plan del oráculo. Se registra la consecuencia en este router según el procedimiento 1.2; no modifica el alcance de la continuación global de este expediente.

La [VNext del oráculo R01](../../research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/README_VNext.md#r01-tasks12-status) contiene cuatro pasadas diferenciadas del README, publicadas en orden, y una matriz de transferencia para Q1a/CTv1, 00K, 00L, 00I/S5, C3, primer R01, runners 00G-HF y Nelson/UC4. La cuarta pasada es relectura simulada del mismo asistente. Doce fuentes vecinas tienen registro cruzado parcial en sus únicas VNext; sus restantes pasadas no se dan por terminadas.

La conciliación mantiene el argumento: comparar una realización con referencia acotada y recursos, conservando observación/autoridad/decisión/intento/efecto. Detecta tres pérdidas posibles al pasar de fuente a router: confundir un PASS batch con entrega real; tratar normalización CTv1 como identidad total de contratos; presentar controles o redes correlacionadas como población independiente. La matriz impide esas promociones y reconoce resultados convencionales favorables.

Se conserva la época de versiones y evidencia. El paquete dinámico 00G-HF tiene resultados posteriores que completan la campaña, pese al README de preparación “pendiente”; las métricas de su malla y los limits de continuidad no validan R01/EA. Los pointers de freeze v0.4/v0.8/v0.9 identifican objetos o épocas diferentes y no se renumeran para uniformarlos.

**Resultado para este README de conjunto:** R01 dispone ahora de revisión documental y contrato de transferencia acotados; no oracle universal, validación UC4, aceptación de fuente, campaña real ni ventaja EA. Se conservan los originales y siete deltas del README R01 pendientes. **La conciliación global de todo el corpus continúa abierta**: este registro concilia únicamente el alcance local, sin sustituir las cuatro pasadas de los demás documentos.

[Fuentes y comprobaciones](../../governance/review/r01-oracle-tasks12-2026-10-06/REVIEW_EVIDENCE.json). La microcomprobación CTv1 comprende 28 ejemplos/propiedades de un prototipo de importación; no nuevo run científico de los harness ni adapter admitido.

## Tercera pasada del README — edición, estructura y formato

**Revisión realizada por Codex, 6 de octubre de 2026:** relectura del orden de exposición, encabezados, tablas, notas y diagramas en el Markdown. No se certifica el render de todos los decks o imágenes.

La página combina un relato de arquitectura, una biblioteca de casos y un mapa técnico. Esa amplitud preserva información, pero el lector cambia de tarea varias veces: conoce el problema, pasa a la hipótesis, a la prueba, a los mecanismos y vuelve a la entrada de corpus. “The corpus spine” reaparece después de una exposición de Foundation→Principles→Requirements→Tests. No es necesariamente contenido duplicado; sin orientación, sí puede sentirse como dos inicios distintos.

Hay cinco diagramas Mermaid y varias tablas largas. Su posición ayuda a resumir relaciones, pero un diagrama no debe ser el único lugar donde se explique una responsabilidad. La matriz “Owns / Emits / Never” preserva límites importantes; conviene anunciar por qué la tabla compacta y la detallada coexisten, en vez de pedir al lector que infiera una diferencia de versión.

El defecto de niveles ya registrado —Level2 frente a Level4— permanece como propuesta pendiente. También hay dos usos de P1/P2/P3: miembros de los seis principios y etiquetas de postura MSCA. Son namespaces distintos, pero una persona que haya entrado por el README puede confundirlos antes de llegar al documento propietario. La solución propuesta es una aclaración en palabras, no otra capa de códigos.

**Formato pendiente:** inspección visual de exports, diagrams y tablas según el visor. Esta pasada textual no la sustituye. Ningún párrafo canónico se mueve ni elimina por estas observaciones.

## Cuarta pasada del README — comprensión humana

**Revisión realizada por Codex, 6 de octubre de 2026:** recorrido simulado desde preguntas de una persona que llega sin conocer los códigos. Es una simulación del mismo agente, no ensayo con lectores externos.

**¿Qué es esto?** La pregunta del participante/decisión/momento ofrece una buena entrada, y las seis escenas hacen visible el problema. Antes de llegar a ellas, el lector recibe varias rutas de credibilidad y papers; puede pensar que necesita entender sus siglas para acceder a la idea. Una orientación corta antes de “Choose your route” ayudaría.

**¿Por qué importa?** Los fallos son memorables, pero pueden parecer exageraciones si el lector no distingue la escena pedagógica de su mecanismo estructural. Explicar que se conserva una relación de fallo para convertirla en un caso comprobable ayuda a conectar la historia con el trabajo técnico.

**¿Qué significa “calificar”?** No debería obligar a leer F1–F9 para saberlo. Una descripción de qué se sabe, bajo qué condiciones y cuándo volver a examinarlo basta para la primera lectura. El detalle técnico puede seguir después.

**¿Qué está demostrado y qué no?** El README tiene esas fronteras, pero están distribuidas por una página extensa. El escaneo textual cuenta 8.415 elementos separados por espacio; es un tamaño descriptivo, no una medición de duración ni calidad. Las rutas de “5 minutos /20 minutos /technical review” señalan partes distintas, no tiempos demostrados. La siguiente edición debe comprobar con lectores si esa promesa orienta de verdad.

**¿Dónde sigo?** Un lector de arquitectura puede ir a mecanismos; otro que quiera cuestionar el argumento debe ir a Requirements y pruebas, y quien quiera valorar la plausibilidad a 00M/00N. Es útil mantener esas preguntas junto a las rutas, sin convertir el README en una colección de etiquetas.

## Conversación y continuidad

El trabajo anterior era exploratorio; estas entradas separan ahora las preguntas. Se aprovecha sin borrar ni fingir una segunda persona. Una revisión humana independiente podrá objetar el recorrido y sus propuestas. La continuación programada sigue el próximo pendiente real en las VNext; no aplica las propuestas canónicas por el solo hecho de que la auditoría esté publicada.

## Propuestas antes/después de esta continuación — no aplicadas

La instrucción de Iván de continuar el plan permite prepararlas y publicar el examen. La incorporación al README canónico sigue pendiente.

### Explicar la idea antes de elegir una ruta

**Texto antes — bloque de idea central, oración única**

```markdown
> **The key idea:** local correctness does not guarantee ecosystem validity. The architecture is about preserving enough qualified state to know when a locally valid position must be reconsidered.
```

**Texto después**

```markdown
> **The key idea:** local correctness does not guarantee ecosystem validity. The architecture is about preserving enough qualified state to know when a locally valid position must be reconsidered.
>
> In ordinary terms, ask what a participant can rely on, under which conditions, and what changed before the next decision. A useful local answer is only one part of that question; its scope, dependencies and authority still matter. Start with the scenarios for the problem, the mechanism section for the proposed architecture, and the proof map for what has actually been tested.
```

**Por qué:** dar una entrada humana sin simplificar los límites ni quitar el cuerpo existente. **Pendiente:** comprobar la claridad de las rutas con una persona y validar los enlaces de la futura edición. No aplicado.

### Separar plausibilidad actual de resultados bajo vocabulario anterior

**Texto antes — oración única de la ruta 00M/00N**

```text
These research notes provide conditional plausibility arguments, not evidence of engineering feasibility, product prevention or requirements fulfilment; publication does not silently promote a new canonical baseline.
```

**Texto después**

```text
These research notes provide conditional plausibility arguments, not evidence of engineering feasibility, product prevention or requirements fulfilment; publication does not silently promote a new canonical baseline. Earlier proof and fixture records retain the vocabulary and assumptions under which they were produced. A link to the current A/B/C/D definitions does not establish that their results transfer to the revised B/C boundary; that correspondence remains a separate review obligation.
```

**Por qué:** conservar visible el límite de A17 cuando un lector pasa de definitions a tests. **Dependencias:** 00M, A17 y VNext de cada proof; no se invalida ni revalida un resultado de manera automática. No aplicado.

### Evitar confusión entre principios y posturas

**Texto antes — encabezado único**

```markdown
## How the pieces divide responsibility
```

**Texto después**

```markdown
## How the pieces divide responsibility

Reading note: the six epistemic principles P1–P6 and the MSCA posture labels P1 Normal / P2 Containment / P3 Migration are different uses of the same letters. A posture is an operating choice under legitimate authority; it is not a proof that the correspondingly numbered principle has been satisfied.
```

**Por qué:** la colisión de letras no debe confundir una decisión operacional con una invariance claim. **Pendiente:** comprobar vocabulario con los propietarios de principios y MSCA; podría ser suficiente una nota local sin cambiar los IDs históricos. No aplicado.


---

## Organización del corpus — tres niveles y revisión desde los README

**Instrucción de Iván, 6 de octubre de 2026.** La lectura del corpus se organiza en tres niveles: **Ecosystem Positioning → Awareness → índices técnicos del corpus**. Una carpeta adicional o un README de paquete no crea otro nivel de lectura.

Cualquier propuesta de redistribuir archivos o cambiar su jerarquía, ubicación o relación se examina en **la VNext del README que los organiza**. Si afecta a varias rutas, se documenta también en las VNext de los otros README afectados; aquí se mantiene la explicación del conjunto cuando corresponda. Debe explicar el problema para el lector, la relación actual y la propuesta, la evidencia, las dependencias y cómo se conservarán enlaces, trazas y versiones.

La [adición al plan de trabajo](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#redistribución-de-archivos-y-tres-niveles-de-readme--instrucción-de-iván) recoge la regla. La auditoría de un archivo puede aportar un hallazgo, pero no decide por sí sola una redistribución. La estructura real y los textos canónicos quedan intactos hasta una revisión concreta de Iván.

### Qué ocurre con la propuesta anterior de niveles

La propuesta **EP-README-DELTA-002** que sugería describir esta entrada como “Level 4” se conserva en su registro anterior, pero queda **sin efecto para incorporación** tras esta aclaración de Iván. Surgía del control antiguo de navegación; el criterio vigente para este corpus es el de tres niveles. No se corrige el README por sustitución ni se oculta la discrepancia histórica.

### Resultado de esta anotación

Se actualiza la regla de revisión y se enlaza el plan; no se mueve, renombra, divide, elimina o reordena ningún archivo. Las futuras propuestas estructurales se registrarán aquí o en la VNext del README propietario, con sus consecuencias en las demás rutas. La conciliación final verificará también que no se haya reconstruido una jerarquía infinita de README.


---

## Continuación de la revisión completa — fuentes, consumidores y navegación

**Auditoría realizada por Codex, 6 de octubre de 2026.** Mismo asistente de IA, para revisión posterior de personas. Iván pidió no confundir cuatro lecturas locales con coherencia y vinculación completas del corpus, y continuar de inmediato. **El corpus todavía no está cerrado.**

El recorrido se amplió al texto completo de 529 Markdown del snapshot `2db5a8c17f58008f9268c23c681ba6e14c8dfbdc`; 464 se alcanzan desde esta entrada mediante los enlaces extraídos. Es un mapa de búsqueda y cobertura, no 464 auditorías semánticas realizadas. Se preservan las incorporaciones concurrentes de R01 y sus VNext, sin duplicarlas ni atribuir a este examen sus resultados.

### Qué se examinó a fondo en esta continuación

- [00N VNext](../../research/ecosystem-awareness/baseline/00N_VNext.md): contraste de R1–R9 en pasajes primarios y R10–R11 en vistas del editor; consumidores del argumento, límites de transferencia y PNG/SVG de requisitos. Los artículos completos de R10/R11 y consumidores extensos siguen pendientes.
- [00M-A01 VNext](../../research/ecosystem-awareness/baseline/00M_A01_VNext.md): cuatro lecturas del texto completo y contraste de su tabla con S/T/H. La correspondencia no se convierte en cumplimiento.
- [Addendum VNext](../../research/ecosystem-awareness/baseline/00N_ADDENDUM_VNext.md): cuatro lecturas del texto completo, conocimiento previo frente a comunicación, información frente a desempeño y costos compartidos. Tres estudios tienen acceso parcial; se conserva esa excepción.
- [UC-EA-03 VNext](../../research/ecosystem-awareness/baseline/UC-EA-03_VNext.md): cuatro lecturas del perfil completo, aprobación no curativa, capacidad finita, fallback y responsabilidad de respuesta. La revisión de todas sus fuentes/consumidores continúa abierta.

Los límites que interesan al lector son concretos: un monitor puede no observar la condición perdida; un mapa de conocimiento puede mejorar la conversación sin elevar el resultado; un fallback necesita autoridad y calificación de efectos; un enlace a una demostración antigua no demuestra transferencia al vocabulario actual.

### Conciliación de la relación entre archivos

La [VNext del README técnico](../../research/ecosystem-awareness/baseline/README_VNext.md) recibe las propuestas de ruta y las discrepancias entre copias. Mantiene **EP → Awareness → índices técnicos**, sin mover archivos ni crear niveles nuevos.

Una copia parcial de UC-EA-03 corta una URL entre sus partes; el documento completo coincide con la concatenación y su ruta principal funciona. La copia antigua de 05A en baseline comparte el nombre v0.1 con la de interfaces, aunque sus textos difieren. Ambos asuntos se documentan para decidir presentación/procedencia sin modificar los originales.

La posible adición de 00M-A01 como ayuda opcional se propone en el README VNext propietario. La aclaración de los companion links históricos se propone en la VNext del addendum. Ninguna se aplica al canon desde esta revisión.

### Resultado del examen de enlaces y qué no demuestra

La [conciliación de navegación](../../governance/review/EP_REVIEW_NAVIGATION_2026-10-06.md) registra 4.265 relaciones internas extraídas, el fragmento de URL señalado, los 80 destinos históricos comprobados en 30 commits y 65 archivos candidatos fuera de la ruta textual. No se declara que esos 65 sean huérfanos ni que todas las fuentes externas hayan sido validadas.

El [plan, adición 1.4](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#cuándo-puede-darse-por-terminada-una-revisión) exige que las pasadas documenten trabajo real y que el cierre cubra significado, fuentes y consumidores. El README canónico de EP y la estrategia no se reescriben; permanecen solo-adición hasta revisión de Iván.

### Conversación y trabajo restante

**Codex responde a su registro anterior:** las lecturas atribuidas siguen conservadas, pero no autorizan declarar coherencia total. La bibliografía y la conciliación avanzan con excepciones precisas. Sigue pendiente el traslado semántico desde definiciones actuales a las pruebas anteriores, la lectura completa de los índices y consumidores restantes y la revisión de binarios/evidencia.

Las nuevas propuestas antes/después están al final de las VNext de cada documento. Las anteriores siguen pendientes salvo una decisión auténtica de Iván; publicar el examen no las incorpora.


---

## Alcance global confirmado por Iván — todo Contributions

**Instrucción del 6 de octubre de 2026:** el corpus comprende todo `dakleyer/structural-awareness-contributions`, también los documentos que salen del README de Ecosystem Awareness, MSCA y Regime Awareness. Se revisan todas las ramas, no solo lo alcanzado desde esta página. La [adición 1.5 al plan](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#alcance-confirmado-todo-contributions-y-sus-integraciones) lo establece.

El [mapa del árbol completo](../../governance/review/EP_REVIEW_REPOSITORY_SCOPE_2026-10-06.md) inventaría 1.203 archivos en el snapshot anterior a esta adición. Los documentos sin una ruta textual también están incluidos; “no alcanzado” no equivale a “fuera de revisión”. Copias históricas, binarios, código, manifests y evidencia conservan su clase y procedencia.

### Auditoría realizada por Codex — continuidad de integración

Mismo asistente de IA. Se contrastaron los pasajes de la ruta EA ↔ RA ↔ MSCA y se leyó completo el perfil conjunto 01D. La [conciliación de integraciones](../../governance/review/EP_REVIEW_INTEGRATIONS_2026-10-06.md) distingue comparación documental de ejecución validada.

Un hallazgo concreto afecta a RA: su README aún resume B_RA como confianza/intensidad, mientras 01C v0.2 explica fundamento y reserva evaluable y separa confianza de magnitud física. MSCA Operation conserva también un resumen corto “direction/intensity/capability/residual”. Los campos conservan el nombre; el significado del resumen necesita conciliación con las definiciones actuales. No se corrige la fuente ni se declara incompatibilidad de todas las implementaciones por esas frases.

Los expedientes de los README afectados son [EA](../../research/ecosystem-awareness/README_VNext.md), [RA](../../research/regime-awareness/README_VNext.md) y [MSCA](../../standards/minimum-sufficient-control/README_VNext.md); el [README técnico EA](../../research/ecosystem-awareness/baseline/README_VNext.md) conserva su expediente existente. Las revisiones de [01C](../../research/ecosystem-awareness/baseline/01C_VNext.md) y [MSCA Operation](../../standards/minimum-sufficient-control/04_OPERATION_VNext.md) registran el cotejo de productor y consumidor. Ninguna se presenta como ciclo completo cuando falta lectura o evidencia.

### Protección de las relaciones

Las propuestas deben mantener trazables los inputs, outputs y retornos: misma decisión/operación, scope, versiones, vigencia, dependencias, dueño, permiso y carga. 01D deja claro que SUPPORTED no es un permiso y que un RA no requerido no debe vetar una acción independiente. Documentarlo no demuestra que la integración ya esté ejecutada.

La ampliación no transfiere autoridad entre ramas ni abre una jerarquía nueva: se conservan **EP → Awareness → índices técnicos** y los enlaces laterales. El README canónico EP, la estrategia y los contratos originales permanecen intactos. La revisión total y la compatibilidad de todos los consumidores siguen abiertas.


---

## Quinta pasada — investigación externa, diferencial y reutilización

**Instrucción de Iván, 6 de octubre de 2026. Estado: contraste específico pendiente.** Esta quinta pasada se realiza después de las cuatro y queda dentro de esta misma VNext. No se crea otro expediente ni se incorporan propuestas a la fuente por esta anotación.

**Pregunta de este documento:** Comparar la composición del conjunto con arquitecturas externas de confianza, autorización, evaluación y coordinación. Identificar qué ya resuelven los vecinos y si el beneficio alegado depende de una integración efectivamente distinta, con la misma tarea, autoridad, recursos y plazo.

Se fijarán trabajos primarios de FG-TIDA y de otras líneas relevantes, incluidos antecedentes y actualizaciones posteriores, con autor, versión, fecha y alcance realmente leído. Aquí se justificará qué coincide, qué diferencia podría sostenerse y qué pieza concreta conviene reutilizar, con sus condiciones de atribución, adaptación y compatibilidad.

El [mapa externo preparatorio](../../governance/review/EP_EXTERNAL_RESEARCH_REVIEW_2026-10-06.md) aporta fuentes iniciales; no completa esta pasada. El [plan 1.6](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#quinta-pasada--trabajos-externos-diferencial-y-reutilización) gobierna método y cierre. Las cuatro lecturas previas mantienen sus estados reales y se reabren si aparece evidencia que las afecte. Codex, mismo asistente de IA; anotación de alcance, sin independencia externa.


### Continuidad del plan con cinco pasadas

Iván añade la investigación externa después de las cuatro lecturas: **fondo/lógica → evidencia/relaciones → edición/formato → legibilidad → trabajos externos/diferencial/reutilización**, y después la conciliación del conjunto. El alcance sigue siendo todo Contributions.

Esta actualización incorpora la obligación a los 31 expedientes activos identificados, incluido el benchmark v0.3 existente. Sus preguntas son propias de cada documento. Tres expedientes reciben un contraste preparatorio adicional (oráculo R01, 04 Interfaces y 00M); no se declara terminada la quinta ni las cuatro anteriores cuando estaban abiertas.

El [mapa externo](../../governance/review/EP_EXTERNAL_RESEARCH_REVIEW_2026-10-06.md) distingue propuestas FG-TIDA, trabajos cerrados como fuera de alcance, investigación, protocolos y derechos por pieza. La aportación propia, una fuente citada o un código disponible no se convierte en evidencia independiente del diferencial. Las piezas seleccionadas podrán orientar prioridades de desarrollo después del cotejo de sus condiciones y consumidores.

Ningún original técnico, field, fixture o resultado cambia por esta preparación. Las propuestas previas conservan su estado y cualquier candidato nuevo requiere fuente exacta, antes/después y decisión concreta de Iván.


---

## Publicación del trabajo preparado — instrucción de Iván

**Auditoría realizada por Codex, 6 de octubre de 2026.** Iván pide publicar todo el trabajo de revisión ya realizado dentro de los VNext, sin conservarlo como un pendiente solo local. Esta instrucción autoriza publicar auditorías, resultados parciales, evidencia y propuestas; no aplica los cambios propuestos a las fuentes canónicas.

La frase anterior “GitHub no fue afectado” describía un error de escritura en los registros operativos locales que se restauraron desde sus copias auténticas. Las publicaciones del corpus sí se habían realizado y se verificaron. Ese error no alteró los documentos ni commits de Contributions.

### Qué se ha conciliado con GitHub

Se compararon los 52 destinos preparados en las últimas tres entregas con el árbol de main en `65517160658e6485f2dd63415a7365674e9bd6ea`: coinciden exactamente con los blobs publicados. Las copias textuales de entregas anteriores también se examinaron: los hallazgos están presentes; las diferencias detectadas corresponden a saltos de línea, un espacio en blanco, una revisión de cabecera o estados de R01 actualizados por lecturas posteriores. No se reintroducen estados antiguos como si fueran actuales.

| Entrega publicada | Trabajo que contiene |
|---|---|
| [e80846a](https://github.com/dakleyer/structural-awareness-contributions/commit/e80846a0f9cf3b97cf222ed3d1e28b31d145ad3e) | Fuentes de 00N, 00M-A01, addendum, UC-EA-03, propuestas y recorrido de navegación. |
| [fdb530e](https://github.com/dakleyer/structural-awareness-contributions/commit/fdb530e739a7647d70ab258071d03f1941844c6a) | Todo Contributions dentro del alcance; cotejo EA/RA/MSCA; VNext de entradas, 01C/01D y Operation. |
| [6551716](https://github.com/dakleyer/structural-awareness-contributions/commit/65517160658e6485f2dd63415a7365674e9bd6ea) | Quinta pasada en 31 expedientes activos, mapa de investigación externa y contrastes preparatorios. |

Los resultados de apoyo que estaban explicados en mapas separados se incorporan **también dentro de este VNext** a continuación. Sus originales públicos se conservan; aquí solo se adaptan los enlaces relativos para que funcionen desde este expediente.

### Lo que ya puede revisar una persona

00M mantiene roles relativos a proceso/pregunta/scope y separa reserva evaluable de exploración. 00N conserva plausibilidad condicionada y la distinción entre información, utilidad, tiempo y autorización. Las propuestas exactas siguen en sus VNext.

La integración registra una discrepancia de explicación: B_RA no se reduce a intensidad física o confianza, y B_Cart no se reduce a un número. Se conserva la propiedad de Cartografía, la selección de postura y la actuación autorizada. 01D exige que evidencia, configuración y permiso hablen de la misma operación, versiones y ventana.

UC-EA-03 distingue aprobación de evidencia y capacidad efectiva. Su copia por partes corta una URL, mientras el documento completo conserva el contenido. La copia antigua de 05A no se borra ni se confunde automáticamente con la ruta actual.

Las fuentes externas identifican vecinos y piezas candidatas, sin diferencial del conjunto demostrado. Los derechos, versiones y compatibilidad de cada pieza permanecen explícitos. El detalle de estos exámenes está dentro de los desplegables siguientes y de las VNext propias de cada documento.


<details>
<summary>Navegación: resultados completos del recorrido y sus excepciones</summary>

**Procedencia:** [informe público conservado](../../governance/review/EP_REVIEW_NAVIGATION_2026-10-06.md), blob `1b980d54bbcd11224a75135a70862639063d4e77` leído en `65517160658e6485f2dd63415a7365674e9bd6ea`. Incorporación de resultados dentro de esta VNext; no una auditoría nueva independiente.

# Conciliación de navegación — avance verificable, 6 de octubre de 2026

Este registro sirve para que una persona vea qué falta en la revisión del corpus. No certifica su coherencia semántica. Depende del [plan de trabajo](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md) y de [EP README VNext](README_VNext.md).

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

**Archivos sin ruta textual desde EP.** Hay 65 candidatos fuera del recorrido extraído. Incluyen licencias/contribuciones generales, submissions de otros temas, ediciones anteriores, fragmentos cuyo documento completo sí está enlazado y fichas nuevas. No se les llama “huérfanos” por defecto: hay que decidir su pertenencia, función y ruta útil antes de proponer una adición. La [evidencia complementaria](../../governance/review/EP_REVIEW_NAVIGATION_2026-10-06.json) conserva la lista exacta.

## Qué sigue abierto

La conciliación semántica debe comprobar que cada consumidor conserva definiciones, dueños, condiciones y grado de evidencia de su fuente; que cada teoría derivada se presenta como derivación propuesta; y que las diferencias temporales de fuentes congeladas no se esconden bajo el mismo número de versión.

El trabajo actual examinó las fuentes de 00N, la tabla 00M-A01, su addendum y UC-EA-03, con alcances y excepciones dentro de sus VNext. No extiende ese examen a los 464 documentos alcanzados. Las figuras de 00M, las fuentes externas pendientes y los consumidores extensos requieren sus propias lecturas.

Toda propuesta de reorganización se examina en la VNext del README propietario dentro de **EP → Awareness → índices técnicos**. Este registro no cambia la jerarquía ni crea otro nivel.

## Método y conservación

Los conteos describen el snapshot anterior a las nuevas adiciones de esta misma auditoría. Una publicación posterior puede agregar fichas/controles; los conteos no se extrapolan silenciosamente. El inventario mantiene épocas fechadas: repetir una ruta con nuevo commit documenta su estado posterior, no crea un segundo documento lógico o una segunda VNext.

La comprobación completa es reproducible desde el snapshot y el grafo preservados localmente; el JSON público es una ayuda compacta, no copia de todo el texto del corpus. Las fuentes técnicas, binarios, pruebas y resultados permanecen intactos.


</details>


<details>
<summary>Integraciones: cotejo realizado, hallazgos y compatibilidad pendiente</summary>

**Procedencia:** [informe público conservado](../../governance/review/EP_REVIEW_INTEGRATIONS_2026-10-06.md), blob `a5efbca1943a2dbaf7046292ab2646351494f20d` leído en `65517160658e6485f2dd63415a7365674e9bd6ea`. Incorporación de resultados dentro de esta VNext; no una auditoría nueva independiente.

# Conciliación de integraciones — EA, Regime Awareness y MSCA

**Auditoría realizada por Codex, 6 de octubre de 2026.** Mismo asistente de IA, para que una persona examine la relación y sus propuestas. [Plan 1.5](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#alcance-confirmado-todo-contributions-y-sus-integraciones) · [alcance completo](../../governance/review/EP_REVIEW_REPOSITORY_SCOPE_2026-10-06.md).

La revisión comprende todo Contributions. Esta primera matriz examina la unión central; las demás interfaces, aplicaciones y pruebas siguen dentro del alcance y pendientes de sus propias lecturas. Se conserva una VNext por documento lógico y todos los originales.

## Qué se cotejó

Fuente fijada: commit `e80846a0f9cf3b97cf222ed3d1e28b31d145ad3e`. Se leyó completo 01D y los README RA/MSCA; EA router y las especificaciones vecinas se cotejaron en pasajes declarados en sus VNext. Los artículos externos, las especificaciones completas aún pendientes y los runtimes no se dan por revisados con este registro.

| Relación | Qué debe conservar el productor y el consumidor | Resultado documental de esta entrada |
|---|---|---|
| EA ↔ MSCA, 01B | Posición calificada frente a assessment de configuración; mismo S/E, scope y versión; permiso separado. | El pasaje de 01B y 01D conservan SUPPORTED ≠ permiso. Resto de 01B y realizaciones pendientes. |
| EA ↔ RA, 01C | Evidencia de régimen limitada por representación/contexto, frente a calificación de decisión; P_RA mínimo y Δ_RA amplio diferenciados. | 01C explicita soporte/reserva, exploración y barrera efectiva. El resumen del README RA es más estrecho y debe conciliarse. |
| Cartografía ↔ RA | Cart_i y Δ_Cart,i calificados hacia RA; delta/overlay/requests de vuelta; persistencia en Composition & Control. | Los pasajes cotejados coinciden en el dueño de persistencia. No se ha probado actualización operacional ni cobertura de todas las versiones. |
| RA → MSCA Operation | Δ_RA con significado, scope, contexto, versiones y vigencia conservados. | El input está atribuido a RA; su resumen “intensity/capability/residual” necesita cotejo con 01C y sus consumidores. |
| EA + RA + MSCA + autoridad, 01D | Mismo identificador de operación/decisión, objetivo, alcance, versiones y ventana; legitimidad y ejecución separadas. | 01D completo conserva binding, dependencia condicional, UNKNOWN no neutral, costo sin doble conteo y effect distinto de receipt. No aporta un run. |
| Delta amplio ↔ perfil mínimo de 01D | Declarar la especialización o mapping utilizado, sin fabricar P_RA ni heredar una garantía por compartir nombre. | La introducción de 01D menciona Δ_RA; sus reglas usan P_RA mínimo. Falta hacer explícita la relación para perfiles amplios; candidato en su VNext. |
| Señales/ACC → operación, feedback y siguiente ciclo | Fuente, identidad, authority response, permiso, efecto y nueva vigencia sin convertir señal en comando. | Ruta identificada. Lectura integral de 01H/01I/01J, ACC, gradient y sus implementaciones sigue pendiente. |
| General interfaces → aplicaciones → casos/tests | Propietario semántico, requisitos y grado de evidencia conservados; ninguna aplicación redefine el canon genérico. | Se mantienen los expedientes existentes 04/05/05A. La ampliación no declara terminadas sus fuentes o pruebas. |

Una coincidencia textual puede ser correcta y aun así no cubrir un consumidor particular. El examen continúa por perfiles y versiones reales, no por firmas repetidas o cantidad de enlaces.

## Tres problemas concretos para conciliar

**Confianza y magnitud del cambio.** B_RA contiene fundamento y reserva caracterizada; confianza califica evidencia. El README RA todavía dice confianza/intensidad y MSCA Operation mantiene una abreviatura similar. Puede inducir una implementación que trate confianza como magnitud física o pierda una reserva evaluable.

**Una capacidad no equivale siempre a C.** Las opciones conocidas y evaluables que no se usaron permanecen B. Una frontera de exploración C requiere grounds y ausencia de un marco de evaluación ya caracterizado. Unknown no es automáticamente D. Estas diferencias deben sobrevivir el handoff.

**Dos representaciones RA requieren una relación explícita.** 01D preserva bien el contrato del detector mínimo, pero un perfil que consuma el delta amplio necesita declarar qué parte consume y bajo qué mapping. No se presume que una proyección semántica preserve cada afirmación de detección o seguridad.

Los candidatos exactos quedan en [RA README VNext](../../research/regime-awareness/README_VNext.md), [MSCA README VNext](../../standards/minimum-sufficient-control/README_VNext.md), [MSCA Operation VNext](../../standards/minimum-sufficient-control/04_OPERATION_VNext.md) y [01D VNext](../../research/ecosystem-awareness/baseline/01D_VNext.md). [01C VNext](../../research/ecosystem-awareness/baseline/01C_VNext.md), [EA README VNext](../../research/ecosystem-awareness/README_VNext.md) y [EP README VNext](README_VNext.md) conservan el contraste de fuentes, consumidores y lectura.

## Qué significa proteger una integración antes de cambiarla

Una propuesta debe identificar a sus consumidores y comprobar ejemplos en ambos sentidos: entrada válida, dato ausente, contradicción/dependencia común, cambio de versión o scope, vencimiento, permiso viejo, capacidad/plazo insuficientes, retorno y resultado no establecido. Se distingue preservación de semántica, payload, comportamiento y evidencia; ninguna se infiere automáticamente de otra.

Las comprobaciones de esta fase son documentales y de conservación. No se renombró ningún field, se modificó un contrato técnico, se recalculó un manifest congelado, se ejecutó un harness o se activó un experimento. La validación de compatibilidad de las realizaciones queda abierta.

**Estado:** cotejo central iniciado, discrepancias documentadas y propuestas pendientes; integraciones completas del repositorio todavía no cerradas.


</details>


<details>
<summary>Fuentes externas: mapa leído, diferencial y candidatos de reutilización</summary>

**Procedencia:** [informe público conservado](../../governance/review/EP_EXTERNAL_RESEARCH_REVIEW_2026-10-06.md), blob `43d04be7a874d20e96f011949465a5cfca54cbd1` leído en `65517160658e6485f2dd63415a7365674e9bd6ea`. Incorporación de resultados dentro de esta VNext; no una auditoría nueva independiente.

# Primera preparación de la quinta pasada — trabajos externos y piezas aprovechables

**Consulta de fuentes realizada por Codex, 6 de octubre de 2026.** Asistente de IA del mismo chat. [Plan, quinta pasada](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#quinta-pasada--trabajos-externos-diferencial-y-reutilización). Este mapa prepara comparaciones dentro de las VNext; no declara realizada la quinta en todos los documentos ni sustituye su juicio propio.

La pregunta es qué ya existe, qué puede servir y qué tendría que probarse todavía. Se buscaron propuestas actuales de FG-TIDA y trabajos sobre memoria/autoridad, evaluación, protocolos e identidad. La selección es inicial y no una revisión sistemática exhaustiva.

## Trabajos de FG-TIDA y novedades relativas a los documentos

Se leyeron los cuerpos de las propuestas y comentarios indicados mediante la API pública; autores, fechas y disposición se fijan en la [evidencia de consulta](../../governance/review/EP_EXTERNAL_RESEARCH_EVIDENCE_2026-10-06.json). Las referencias son aportaciones de sus autores, no adopción del grupo.

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


</details>


### Comprobaciones y trabajo que todavía queda

Se publican como apoyo de este VNext el [estado de publicación](../../governance/review/publication-reconciliation-2026-10-06/publication_status.json), los [fragmentos antes comprobados](../../governance/review/publication-reconciliation-2026-10-06/surgical_validation.json), las [comprobaciones de conservación](../../governance/review/publication-reconciliation-2026-10-06/preservation_checks.json), las [lecturas de vuelta](../../governance/review/publication-reconciliation-2026-10-06/readback_receipts.json) y el [grafo completo del snapshot](../../governance/review/publication-reconciliation-2026-10-06/link_graph_snapshot_2db5a8c.json). El [verificador de enlaces reproducible](../../governance/review/publication-reconciliation-2026-10-06/link_review.mjs) contiene el algoritmo utilizado y un wrapper de lectura offline de objetos Git; no modifica el checkout ni ejecuta los programas del corpus.

El grafo y sus resultados pertenecen al commit que indican. Un archivo encontrado, descargado o publicado no se cuenta como una auditoría semántica completa. Los originales ya accesibles en Git y las copias de operación no se duplican como nuevas teorías o revisiones; los resultados útiles y su procedencia quedan públicos.

**Pendiente de hacer:** completar lecturas, fuentes y consumidores, la quinta comparación específica y la conciliación global. **Pendiente de decisión de Iván:** incorporación de los candidatos exactos. Esos pendientes no significan que se retengan auditorías ya terminadas o propuestas preparadas sin publicar.

Las próximas entregas publicarán su trabajo sustantivo en la VNext correspondiente aunque el ciclo siga parcial, con alcance y límites reales. Los canónicos se preservan; la revisión continua no espera al cierre de todo el corpus para hacerse visible.


---

## Sexta pasada unificadora — preparación y continuidad

**Instrucción de Iván, 6 de octubre de 2026. Preparación registrada por Codex, mismo asistente de IA. Estado: pendiente de lanzamiento después de las cinco pasadas del corpus.** Esta anotación organiza el trabajo futuro; no declara una auditoría unificadora realizada ni cambia el estado de las lecturas anteriores.

**Pregunta de consolidación de este documento:** Reconstruir la idea central del conjunto, sus ramas y sus límites, y conciliar las propuestas de todos los propietarios sin convertir enlaces laterales en subordinación.

Los hallazgos concretos se comentarán aquí y en las VNext de los documentos relacionados, conservando respuestas y desacuerdos. Se cotejarán las propuestas con la fuente actual y sus consumidores antes de presentar candidatos consolidados antes/después. La [sexta pasada del plan](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#sexta-pasada-unificadora-y-consolidación) fija el lanzamiento y el método. Se preservan fuente, historia y decisión de Iván para incorporar cambios.

### Consolidación del conjunto

Esta será la conciliación final ya prevista, ahora explícita como sexta pasada. Se lanzará después de completar los cinco exámenes reales del corpus completo, incluidas sus ramas e integraciones. Los 31 expedientes existentes conservan una sola VNext y reciben preguntas propias; su existencia no representa todo Contributions auditado.

El relato común explicará qué idea sostiene el conjunto, qué sigue abierto y qué propuestas resultan compatibles o alternativas. Cada comentario material volverá a la VNext del origen y del receptor; los README propietarios conservarán sus consecuencias. No basta un mapa de enlaces ni una lista de etiquetas.

Se dará prioridad a contradicciones o transferencias de evidencia que cambien una conclusión, a integraciones y decisiones que dependan unas de otras y, después, a la presentación. Ante un hallazgo nuevo se reabre la pasada afectada y se vuelve a conciliar esa relación. Las propuestas consolidadas tendrán antes literal de la versión vigente, después, razón, evidencia, dependencias y decisión pendiente; la historia anterior se conserva.

La continuación programada mantendrá este orden y publicará los resultados parciales dentro de cada VNext. La autorización para publicar ya existe; el canon no recibe cambios por ejecutar la consolidación. Se mantienen los tres niveles EP → Awareness → índices técnicos y la revisión de toda redistribución en los README VNext afectados.


---

## Plan de cambios — el texto viejo siempre permanece visible

**Instrucción de Iván, 6 de octubre de 2026, registrada por Codex.** Después de las cinco pasadas y la unificadora, el plan de cambios quedará dentro de la única VNext de cada documento. Cada cambio mostrará **Texto antes — viejo**, literal y completo del pasaje afectado, seguido de **Texto después — propuesto**, también completo; después explicará razón, dependencias, prioridad e instrucciones y decisión de Iván.

El viejo no se reemplazará por un resumen, un enlace o solo un diff. El original canónico y las propuestas anteriores se conservan. Si cambia la fuente, se añade un nuevo par identificado y se mantiene el anterior. Para adiciones se muestra el contexto existente y el bloque a añadir; README y estrategia siguen append-only hasta la revisión de Iván.

Aquí se explicará el orden del conjunto y los cambios que deben decidirse juntos. Los pares concretos estarán en las VNext de sus documentos, con consecuencias en fuentes, consumidores y README afectados. El [plan 1.9](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#plan-de-cambios-dentro-de-cada-vnext--texto-viejo-siempre-visible) fija este formato para todo el corpus, incluidas las VNext que se abran después.

**Estado real:** instrucción y método publicados; el plan consolidado final depende de completar las cinco pasadas y la sexta. Los pares ya preparados se publican como parciales. Esta adición no ejecuta cambios ni elimina texto anterior.


---

## Organización autorizada del trabajo adicional — 6 octubre de 2026

**Lectura y registro realizados por Codex, mismo asistente de IA.** Iván pide explicar y enlazar el material fuera de la ruta principal y conservar los documentos sueltos, sin abrir nuevas auditorías de cada uno. Se mantienen las tres capas canónicas y se usan tres hojas auxiliares no canónicas: [EA y transversal](../../research/ecosystem-awareness/baseline/non-canonical/README.md), [RA](../../research/regime-awareness/ADDITIONAL_WORK_README.md) y [MSCA](../../standards/minimum-sufficient-control/ADDITIONAL_WORK_README.md). EA reutiliza su índice existente; RA y MSCA añaden hojas de trabajo, sin crear propietarios nuevos.

El [plan 1.10](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#trabajo-fuera-de-la-ruta-principal--lectura-adicional-sin-nuevas-auditorías) registra la instrucción más reciente. El inventario del corte 4ebb0c89722f1dc36adc11bec031c9d88b07737c tiene 1.306 archivos, 155 snapshots y 1.151 vivos: 800 alcanzables por enlaces de archivo y 351 sin esa ruta, incluidos 62 Markdown. Las fichas, partes y mirrors no se cuentan como 62 nuevas teorías. Los catálogos explican propósito, relaciones y límites y enlazan todos los archivos del corte; las listas exhaustivas quedan plegadas.

Los originales sueltos, canon, código, datos, freezes y binarios no reciben correcciones. Estar en el catálogo no altera autoridad. La lectura es de orientación y organización; no sustituye las cinco pasadas de una fuente vigente ni una dependencia material del argumento.

### Hallazgos de lectura que orientan la organización

Los cinco pares NIST entre raíz y submissions son copias exactas por versión. Huella pública, Public Provenance, EA-ITP-01 y partes 2/3 de 05 también tienen pares exactos. 05A, parte 1 de 05 y masterclass DAOS no son idénticos como blobs: conservar sus rutas y versiones, no fusionar por título.

Las partes de UC-EA-04 y de la familia de perfiles concatenan exactamente al lector completo. UC-EA-01 y UC-EA-02 difieren; el lector completo contiene banners semánticos que no están en ese punto del split. La falta de enlace de una parte no basta para excluir su fuente lógica de la ruta vigente.

RA no tiene Markdown local sin ruta; su catálogo distingue el contexto y la revisión cuantitativa ya accesibles. En MSCA la nota UNECE WP.5 y sus originales son práctica adicional que faltaba conectar. Las propuestas y auditorías previas se conservan; la nueva instrucción evita abrir ciclos adicionales sobre los sueltos.


Los antes/después de las tres adiciones de navegación están en las VNext propietarias de baseline, RA y MSCA. Esta entrada relaciona la organización del conjunto y conserva toda la conversación anterior.


---

## Prioridades del plan de cambios — revisión del corte

**Revisión realizada por Codex, 6 octubre de 2026, mismo asistente de IA.** Se revisan las auditorías y propuestas ya registradas para valorar impacto esperado, riesgo y esfuerzo. La fuente pública del corte es `7500dd5ee05c1a5052a28d35a8cefaf2c530707f`; los viejos y pares anteriores permanecen íntegros. Esta revisión no completa las pasadas pendientes ni la sexta.

El [plan 1.11](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#prioridad-de-cada-cambio--impacto-riesgo-y-esfuerzo) explica los criterios y el [listado completo](../../governance/review/change-priorities-2026-10-06/priorities.json) conserva las fuentes y los pares. La prioridad sirve para preparar tandas de decisión; la incorporación depende de Iván y de las comprobaciones indicadas.

| Cambio | Prioridad / tanda | Impacto esperado | Riesgo | Esfuerzo | Estado |
|---|---|---|---|---|---|
| 1 · Nota de acceso a revisión de EP | Histórico · Histórico | Medio | Bajo | Bajo | Ya publicado |
| 2 · Antigua propuesta de convertir EP en Level 4 | Histórico · Histórico | No vigente | Alto | No procede | Descartado |
| 3 · Explicar la idea central antes de elegir una ruta | Siguiente · 4 — Lectura humana y rutas | Medio | Medio | Bajo | Pendiente de decisión |
| 4 · Separar semántica actual y resultados históricos | Primera · 1 — Claridad de evidencia y estado | Alto | Medio | Medio | Pendiente de decisión |
| 5 · Distinguir principios P1–P6 y posturas P1–P3 | Siguiente · 4 — Lectura humana y rutas | Medio | Medio | Bajo | Pendiente de decisión |

### Cambio 1 — Nota de acceso a revisión de EP

**Impacto esperado: Medio. Riesgo: Bajo. Coste/esfuerzo: Bajo. Prioridad: Histórico.** Hacer visible el expediente de auditoría.

**Qué podría quedar desactualizado o afectado:** Repetir la nota ya publicada duplicaría la entrada del README.

**Qué cuesta prepararlo:** No requiere nueva edición; mantener el vínculo.

**Dependencias conocidas:** [CORPUS_REVIEW_PROCEDURE_2026-10-06.md](../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md). La lista es el mapa conocido para preparar la decisión, no certificación de todos los consumidores.

**Estado y condición:** Ya publicado. Fuera de tandas pendientes. No volver a ejecutar: el texto después está presente.

**Viejo y nuevo:** el par literal sigue en [la entrada anterior](README_VNext.md#ep-readme-delta-001--nota-de-versiónrevisión-y-enlace); el viejo tiene una coincidencia en [la fuente actual](README.md), blob `ed97dbe9f34758219863511717c4f237b48bedf3`. El bloque añadido está presente; no se repite la ejecución.

### Cambio 2 — Antigua propuesta de convertir EP en Level 4

**Impacto esperado: No vigente. Riesgo: Alto. Coste/esfuerzo: No procede. Prioridad: Histórico.** No se evalúa como beneficio actual: contradice los tres niveles canónicos acordados.

**Qué podría quedar desactualizado o afectado:** Reabrirla expandiría la jerarquía y confundiría los catálogos auxiliares con canon.

**Qué cuesta prepararlo:** No invertir en ejecución; conservar la historia.

**Dependencias conocidas:** [DOCUMENT_CONTROL.md](../../DOCUMENT_CONTROL.md). La lista es el mapa conocido para preparar la decisión, no certificación de todos los consumidores.

**Estado y condición:** Descartado. Fuera de tandas pendientes. Retirada por la instrucción de tres niveles; los tres catálogos auxiliares no la reactivan.

**Viejo y nuevo:** el par literal sigue en [la entrada anterior](README_VNext.md#ep-readme-delta-002--nivel-de-lectura-del-router); el viejo tiene una coincidencia en [la fuente actual](README.md), blob `ed97dbe9f34758219863511717c4f237b48bedf3`. Se conserva la historia; este par queda fuera del top actual.

### Cambio 3 — Explicar la idea central antes de elegir una ruta

**Impacto esperado: Medio. Riesgo: Medio. Coste/esfuerzo: Bajo. Prioridad: Siguiente.** Dar a una persona una pregunta corriente antes de los índices.

**Qué podría quedar desactualizado o afectado:** La inserción literal propuesta toca el cuerpo EP protegido; el texto debe adaptarse a una adición al final y evitar repetición con la introducción.

**Qué cuesta prepararlo:** Una explicación breve y comprobación de lectura; la adaptación de ubicación tiene que mostrarse antes/después.

**Dependencias conocidas:** [README.md](README.md) · [DEVELOPMENT_STRATEGY.md](DEVELOPMENT_STRATEGY.md). La lista es el mapa conocido para preparar la decisión, no certificación de todos los consumidores.

**Estado y condición:** Pendiente de decisión. Reformular como adición append-only. Reformular para append-only o recibir decisión concreta de Iván sobre el cuerpo.

**Viejo y nuevo:** el par literal sigue en [la entrada anterior](README_VNext.md#explicar-la-idea-antes-de-elegir-una-ruta); el viejo tiene una coincidencia en [la fuente actual](README.md), blob `ed97dbe9f34758219863511717c4f237b48bedf3`. Localizar el viejo no prueba compatibilidad de la propuesta ni autoriza incorporación.

### Cambio 4 — Separar semántica actual y resultados históricos

**Impacto esperado: Alto. Riesgo: Medio. Coste/esfuerzo: Medio. Prioridad: Primera.** Evitar que enlazar la nueva definición A/B/C/D parezca revalidar pruebas antiguas.

**Qué podría quedar desactualizado o afectado:** Una precisión local puede dejar que otros README, decks o pruebas continúen amplificando el resultado; tampoco autoriza reescribir evidencia histórica.

**Qué cuesta prepararlo:** Adición explicativa de EP y cotejo de notas 00M/00N y proof map; no repetir o modificar pruebas.

**Dependencias conocidas:** [00M_VNext.md](../../research/ecosystem-awareness/baseline/00M_VNext.md) · [00N_VNext.md](../../research/ecosystem-awareness/baseline/00N_VNext.md) · [00K_A17_DOCUMENTATION_REPRODUCIBILITY_AND_PROOF_MAP_v0.1.md](../../research/ecosystem-awareness/baseline/00K_A17_DOCUMENTATION_REPRODUCIBILITY_AND_PROOF_MAP_v0.1.md). La lista es el mapa conocido para preparar la decisión, no certificación de todos los consumidores.

**Estado y condición:** Pendiente de decisión. Reformular como adición append-only. Adaptar a append-only en EP; mantener versión, premisas y límites de cada resultado.

**Viejo y nuevo:** el par literal sigue en [la entrada anterior](README_VNext.md#separar-plausibilidad-actual-de-resultados-bajo-vocabulario-anterior); el viejo tiene una coincidencia en [la fuente actual](README.md), blob `ed97dbe9f34758219863511717c4f237b48bedf3`. Localizar el viejo no prueba compatibilidad de la propuesta ni autoriza incorporación.

### Cambio 5 — Distinguir principios P1–P6 y posturas P1–P3

**Impacto esperado: Medio. Riesgo: Medio. Coste/esfuerzo: Bajo. Prioridad: Siguiente.** Impedir que una etiqueta de postura se lea como principio demostrado.

**Qué podría quedar desactualizado o afectado:** Cambiar IDs o solo una explicación dejaría referencias incompatibles; la inserción propuesta está en el cuerpo EP protegido.

**Qué cuesta prepararlo:** Nota breve con lectura cruzada de Requirements y Operation; no renombrar etiquetas.

**Dependencias conocidas:** [00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md](../../research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) · [04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md](../../standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md). La lista es el mapa conocido para preparar la decisión, no certificación de todos los consumidores.

**Estado y condición:** Pendiente de decisión. Reformular como adición append-only. Adición append-only; conservar nombres y aclarar sus dueños.

**Viejo y nuevo:** el par literal sigue en [la entrada anterior](README_VNext.md#evitar-confusión-entre-principios-y-posturas); el viejo tiene una coincidencia en [la fuente actual](README.md), blob `ed97dbe9f34758219863511717c4f237b48bedf3`. Localizar el viejo no prueba compatibilidad de la propuesta ni autoriza incorporación.

### Qué cambios destacan y cómo decidir las tandas

Se revisaron los 31 expedientes activos y 42 pares concretos. **37 siguen pendientes, cuatro son adiciones ya presentes y uno es la antigua propuesta canónica de Level 4 descartada.** Todos los viejos se localizaron una vez en su fuente vigente; en las tres adiciones de catálogos el bloque está publicado y solo difiere la separación en blanco del contexto del par. Nueve líneas de Requirements/oráculo permanecen por concretar, sin par literal. El corpus conserva las auditorías pendientes.

Los cambios de mayor beneficio sustantivo se agrupan así:

1. **Evidencia comprensible y bien atribuida:** self-test versus resultado de tecnología (26), límites de dominio/independencia del oráculo (27), reporte Theme21 versus reproducción (31), versión/fecha de fuentes (32), W1 versus adopción (40), semántica actual versus proofs históricos (4). Varios son precisiones acotadas; 4 requiere append-only y 40 cotejar estados relacionados.
2. **Integración RA–EA–MSCA:** resumen RA, entrada Operation y B_Cart (35/37/38), junto al mapping P_RA/Δ_RA (17). Impacto alto; se preparan como tanda porque una corrección aislada puede dejar consumidores con otro significado.
3. **Contratos de uso y evaluación:** binding recheck→ejecución (16), full-result/A_ref (19) y admisión previa con conservación de fallos (41). Son cambios de alto impacto y riesgo, con trabajo de adjudicación/versiones/perfiles; no se ejecutan como retoques editoriales.
4. **Capacidad humana y dueño de la respuesta:** UC03 (22/23). Se necesita un successor o ficha que preserve el freeze y una conciliación con T3/T4 y Operation.
5. **Comprensión y lectura:** orientación, ejemplos, versiones y rutas en EP/00M/00N/baseline/R01. Se eligen en bloques pequeños; las inserciones de EP deben adaptarse al permiso append-only.

### Top del corte — vista de impacto

Este orden usa impacto, prioridad y desempates de riesgo/esfuerzo. No libera una propuesta por figurar arriba; ver la preparación de la última columna.

| Cambio | Impacto | Riesgo | Esfuerzo | Qué falta antes de decidir |
|---|---|---|---|---|
| [Self-test verde distinto de tecnología que pasa](../../research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/README_VNext.md#r01-oracle-delta-003--distinguir-self-test-del-instrumento-y-aceptación-del-candidato) (26) | Alto | Bajo | Bajo | Candidato para revisión documental concreta |
| [Reporte Theme21 distinto de reproducción propia](../../research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md#if05a-r1-delta-001--precisión-de-la-evidencia-numérica) (31) | Alto | Bajo | Bajo | Candidato para revisión documental concreta |
| [Fecha y versión de fuente para promociones 05A](../../research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md#if05a-r1-delta-002--fecharevisión-de-fuente-en-la-ficha-de-promoción) (32) | Alto | Bajo | Bajo | Candidato para revisión documental concreta |
| [Tabla W1 presente distinta de todos los gates cerrados](../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md#bench-r1-delta-001--distinguir-tablaw1-presente-de-gates-restantes) (40) | Alto | Medio | Bajo | Completar comprobaciones específicas antes de decisión |
| [Separar semántica actual y resultados históricos](README_VNext.md#separar-plausibilidad-actual-de-resultados-bajo-vocabulario-anterior) (4) | Alto | Medio | Medio | Reformular como adición append-only |
| [Condicionar el tamaño y coste del contexto útil](../../research/ecosystem-awareness/baseline/00N_VNext.md#presentar-el-tamaño-del-contexto-como-una-posibilidad-condicionada) (11) | Alto | Medio | Medio | Preparar ficha o successor preservando fuente |
| [Límite de dominio e independencia del oráculo](../../research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/README_VNext.md#r01-oracle-delta-004--delimitar-diversidad-de-referencia-dominio-y-validación-externa) (27) | Alto | Medio | Medio | Candidato para revisión documental concreta |
| [Dos peers como propuesta, no arquitectura FG adoptada](../../research/ecosystem-awareness/fg-tida/interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md#if05-r1-delta-002--carácter-propuesto-de-los-peers) (34) | Alto | Medio | Medio | Completar comprobaciones específicas antes de decisión |
| [Mostrar todo B_Cart en el índice MSCA](../../standards/minimum-sufficient-control/README_VNext.md#propuesta-antesdespués--expresar-todo-bcart) (38) | Alto | Medio | Medio | Conciliar contrato y consumidores |
| [Explicar la correspondencia P_RA y delta RA](../../research/ecosystem-awareness/baseline/01D_VNext.md#propuesta-antesdespués--declarar-el-puente-de-representación) (17) | Alto | Alto | Medio | Conciliar contrato y consumidores |

### Primera tanda para revisar contigo

Empezaría por **26, 27, 31 y 32**: aclarar qué significa un self-test, hasta dónde llega la referencia, qué es un reporte de tercero y con qué fecha/versión se sustenta una relación. Son candidatos documentales de alto beneficio; 27 requiere cotejo de dominio y referencias, y el resto precisa fuentes fijadas. Pueden revisarse sin cambiar código, resultados ni contratos comunes.

Después prepararía conjuntamente **35/37/38/17**, por su impacto en significado e integraciones. **16/19/41 y 22/23** necesitan una decisión sobre alcance y compatibilidad; tener su texto candidato no cierra ese trabajo.

La tanda de correcciones **14/15** es pequeña y se decide junta; evita incoherencia de conteo e independencia implícita dentro del registro. Los accesos a catálogos y nota inicial EP ya publicados quedan fuera de la cola.

### Cómo sacar otra lista top

La [tabla CSV](../../governance/review/change-priorities-2026-10-06/priorities.csv) permite filtrar Estado = pendiente y comparar impacto/riesgo/esfuerzo/tanda. El [registro JSON](../../governance/review/change-priorities-2026-10-06/priorities.json) incluye razones, fuentes, todos los viejos y nuevos y los límites de cobertura. El [extractor](../../governance/review/change-priorities-2026-10-06/extract_top.py) ofrece vistas **impact** y **decision**, y filtro por tanda; lee archivos, no ejecuta programas del corpus.

La vista **decision** selecciona los candidatos a revisión documental concreta. Los trabajos sin par literal aparecen solo si se pide incluir planificación. Las adiciones ya publicadas y la propuesta descartada se excluyen por defecto. El ranking es provisional y se actualiza con nuevas entradas cuando cambien fuentes o decisiones.


---

## Continuación de 01C — payloads y separación de propietarios

**Auditoría cruzada realizada por Codex, 6 octubre de 2026; mismo asistente de IA.** Continuación sustantiva: 01C completo examinado en fondo/lógica, edición textual y relectura simulada; evidencia ampliada a los payloads y relaciones 01D/Role/Composition/Operation. Evidencia primaria completa/consumidores/perfiles y quinta siguen abiertas. Dos fronteras nuevas: compartir A/B/C/D no transfiere justificación de Cart_i a RA, y rol vinculado no es conducta observada. Candidatos 52/53/54, impacto alto/riesgo alto/esfuerzo medio, originales intactos. La sexta no se lanza.

La explicación, cobertura y viejos/nuevos están en [01C VNext](../../research/ecosystem-awareness/baseline/01C_VNext.md#lectura-de-los-payloads-y-sus-propietarios--continuación-sustantiva-de-01c), con el extremo productor en [Composition VNext](../../standards/minimum-sufficient-control/03_COMPOSITION_VNext.md) y [Role VNext](../../standards/minimum-sufficient-control/02_ROLE_VNext.md). Se preservan todas las conversaciones anteriores, decisiones y riesgos. No se declara ejecución o nueva validación independiente.

El registro de prioridades añade **52/53/54** sin modificar las 51 entradas anteriores; 55 identifica solo la adición de acceso a fichas de esta entrega. Los tres cambios técnicos nuevos siguen pendientes, dentro de la tanda de integración, no se ejecutan como correcciones aisladas. [Soporte del contraste](../../governance/review/01C-payload-ownership-2026-10-06/evidence.json). Los dos nuevos expedientes son de fuentes principales Role/Composition; su apertura no extiende la campaña a los materiales adicionales.


---

## Lectura completa de Role y Composition — reevaluación de la auditoría

**Auditoría/reevaluación realizada por Codex, 6 octubre de2026; mismo asistente de IA.** Se avanzó en dos fuentes principales completas: Role y Composition. El contexto matiza la auditoría previa: Role también usa la frase del consumidor y Composition conserva los qualifiers por input.52–54 bajan a impacto/riesgo Medio, prioridad Siguiente, esfuerzo Medio. El registro y exportador aplican la evaluación vigente conservando historia.56 es candidato editorial de título. Fuentes intactas, evidencia/quinta parciales y sexta pendiente.

[Role VNext](../../standards/minimum-sufficient-control/02_ROLE_VNext.md#pasadas-propias-de-role--lectura-completa-y-contraste-del-rol-estático) · [Composition VNext](../../standards/minimum-sufficient-control/03_COMPOSITION_VNext.md#pasadas-propias-de-composition--leer-el-mapa-completo-y-sus-límites) · [Fuentes/cobertura](../../governance/review/MSCA-role-composition-2026-10-06/evidence.json). La conversación anterior permanece visible; relectura del mismo agente no es independencia externa.

El [registro](../../governance/review/change-priorities-2026-10-06/priorities.json) conserva todas las entradas originales; aplica reevaluaciones fechadas antes de obtener el top. La [tabla CSV](../../governance/review/change-priorities-2026-10-06/priorities.csv) muestra valoración vigente y el [extractor](../../governance/review/change-priorities-2026-10-06/extract_top.py) usa esas mismas actualizaciones.52/53/54 permanecen pendientes opcionales de prioridad Siguiente. Esto evita que la conversación nueva y el ranking técnico den prioridades contradictorias.

**Actualización concurrente conservada:** la base de publicación avanzó a `6881dfe920a30ef6d00334f15059ab1dd931c8d4` con materiales DDS/HEW y sus expedientes de otro trabajo. Role/Composition y los destinos de esta revisión no cambiaron. No se ejecutan ni califican esos nuevos programas/resultados en esta pasada, ni se cuenta su presencia como auditoría concluida. El árbol contiene 39 expedientes VNext/candidato benchmark identificables;33 pertenecen al programa ya registrado y 6 nuevos no fueron examinados aquí.


---

## Continuación sustantiva — kernel, ACC y comparación del gradiente

**Auditoría realizada por Codex, 6 de octubre de 2026; mismo asistente de IA.** Cinco fuentes principales nuevas leídas completas: Architecture, perfilACC, Operation,01I y Gradient. Fondo/lógica, edición textual y legibilidad simulada registrados por separado; evidencia cruzada ampliada a sus extremos y quinta específica realizada en los nuevos expedientes/Operation. Segundas pasadas abiertas por perfiles y evidencia aún pendientes; no cierre del corpus ni sexta lanzada.

**El nuevo hallazgo de fondo:** admitir varios objetivos y un riesgo vectorial no suministra por sí solo un “mejor” movimiento. Gradient§§5/7/9 abrevia signo/argmax y Operation§9 repite dualidad fuera de su condición binaria explícita. El contraejemplo propio y los viejos/nuevos están en [Gradient VNext](01_GRADIENT_VNext.md); el receptor en [Operation VNext](../../standards/minimum-sufficient-control/04_OPERATION_VNext.md).57/58/59 se preparan juntos: **impactoAlto, riesgoAlto, esfuerzoMedio, prioridad Primera**. Es insuficiencia de especificación para los perfiles generales admitidos, no fallo runtime observado ni refutación de la idea.

[Architecture](../../standards/minimum-sufficient-control/00_ARCHITECTURE_VNext.md) y [ACC](../../standards/minimum-sufficient-control/01_ACC_VNext.md) preservan kernel/linaje; [01I](../../research/ecosystem-awareness/baseline/01I_VNext.md) mantiene gobernanza y preguntas colectivas futuras. Role/Composition reciben comentarios de la relación, sin rehacer pasadas ya realizadas.60 aclara opcionalmenteP3;61 propone corregir un título duplicado. Toda incorporación permanece pendiente de decisión concreta de Iván.

**Fuentes externas y límites:** comparación específica deRATS/credenciales/delegación/organizaciones normativas/optimización vectorial en los expedientes respectivos. ATHENA body/comentarios públicos leídos; elWord deTD236-WP1 está restringido y no leído. No se confunde metadata/propuesta con contenido técnico, adopción o ensayo realizado. Fuente urbanaTegrity no recuperada en este intento; seguirá visible como pendiente.

El índice de prioridades conserva los 56 registros anteriores y añade cinco pares técnicos y dos adiciones de navegación de esta entrega; estas últimas se marcan ya publicadas sólo tras publicar y leer de vuelta. Los expedientes nuevos son fuentes principales/integraciones materiales, no auditorías nuevas de los documentos sueltos. READMEEP/estrategia, fuentes, freezes, binarios, resultados y programas intactos; índices propietarios sólo reciben las breves rutas de fichas.


## Reapertura por actualización concurrente — capacidad humana y preservación

**Codex, mismo asistente,6 de octubre de 2026.** Main avanzó a`8757ba614c94f962206912d4896c119a18a924fa` añadiendo01K y sus fronteras enOperation/01J/índices. Se conserva esa versión; Operation§4.1 y01K completos leídos,01J§5.2 contrastado. [01K VNext](../../research/ecosystem-awareness/baseline/01K_VNext.md) publica la nueva pregunta de ledger y64/67; [01J VNext](../../research/ecosystem-awareness/baseline/01J_VNext.md) registra el receptor con lectura restante pendiente.65/66 son precisiones del índice, publicadas como propuestas.

**Comprobación de preservación:** el cambio concurrente deEP insertó01K dentro del cuerpo; la versión anterior no es un prefijo byteexacto de la actual. En esta revisión no se escribió eseREADME ni se revierte el nuevo material. La autorización particular de ese otro trabajo no fue examinada aquí; la política append-only de Iván sigue vigente y la excepción necesita quedar explícita antes de validar ese cambio comoconforme. Se conserva la fuente actual y se registra la pregunta; no bloquea otras lecturas independientes.

Los pares59/60 anteriores siguen visibles y vuelven amostrarse contra el nuevo blob de Operation; lospasajes son literalmente iguales, pero se examina el nuevo contexto de escalada. Eltrabajo pendiente siguevisible: perfiles/materiales,quinta deRole/Composition/Signalling y demás fuentes principales, ysexta global. Ningún número de fichas/pasadas parciales certifica elcierre.


---

## Recepción de 01J y significado de D — contraste cruzado

**Auditoría realizada por Codex, mismo asistente de IA, 6 de octubre de 2026.** Se leyó completo01J y se cotejó con00M§§1.4–1.5 y su ejemplo de telemetría. La lectura completa de01J añade un problema de fondo concreto: tres reglas genéricas fuerzan D por incertidumbre de traducción, mientras la definición y el ejemplo requieren barrera efectiva. No se corrige la teoría central para acomodar un consumidor; se prepara una tanda compatible68/69/70.

[01J VNext](../../research/ecosystem-awareness/baseline/01J_VNext.md) conserva el relato, contraejemplos propios y pares68/69/70, con impactoAlto/riesgoAlto/esfuerzoMedio/prioridadPrimera. Misma regla en prosa, síntesis y esquema; cotejar campos materiales y consumidores antes de decidir. No se aplicó ninguna propuesta ni se transformó la relectura en auditoría independiente. Quinta específica de01J realizada en alcance declarado; segunda material y sexta global permanecen abiertas. [Evidencia](../../governance/review/Signalling-full-2026-10-06/evidence.json).


---

## Garantía de trabajo — una VNext y originales de sólo lectura

**Instrucción reiterada de Iván, 6 de octubre de 2026:** «sólo hay un vnext para cada archivo» y «no cambias los archivos canónicos originales». Auditoría de unicidad realizada por Codex, mismo asistente de IA, contra el árbol `e08e4f12ffd3f1dff64bc08df6af62c943992831`.

Se vincularon los **45 archivos con nombre VNext y el benchmark v0.3**, que ya es su propio expediente, a **46 fuentes lógicas distintas**. No se encontró una fuente con dos VNext activas. Las partes de una misma fuente y las versiones anteriores siguen dentro de su expediente existente. Las copias auténticas de preservación son historia, no nuevos espacios de auditoría; no se crean pasadas en ellas.

Antes de abrir una VNext se comprobarán tanto ruta como fuente, versiones, partes y posibles nombres alternativos. Si ya existe, todas las pasadas, respuestas, evidencia, propuestas y repeticiones se añaden allí. No abrir una VNext por pasada, un segundo expediente de la misma fuente, una revisión de la VNext, otro README o fichas redundantes. El material adicional mantiene sus tres catálogos y la instrucción de no fabricar nuevas auditorías.

**Originales en lectura:** no aplicar propuestas ni escribir dentro de archivos canónicos originales, incluso nuevas notas o enlaces. Las autorizaciones anteriores permitieron breves adiciones de navegación a índices; sus cuerpos previos se preservaron, pero esta instrucción más reciente impide continuar añadiendo al original. Las observaciones y nuevos accesos de revisión se acumulan en las VNext existentes. La estrategia y el README EP originales mantienen además su protección explícita; resultados, fuentes congeladas, código y binarios no se modifican por revisar.

Los controles de las entregas de esta revisión verificaron diff acotado, predecesores auténticos y lectura pública de vuelta. Esa comprobación no certifica otros cambios concurrentes ni significa que se hayan terminado las cinco pasadas o la conciliación global. La revisión pendiente continúa con estos límites.


---

## Verificación del día — enlaces VNext, cajas y conservación de originales

**Verificación realizada por Codex, mismo asistente de IA, 6 de octubre de 2026.** Se interpreta «playlists» como VNext por el contexto de Iván. Ventana del día de Madrid desde el 5 de octubre a las 22:00 UTC (00:00 de Madrid del 6 de octubre), corte público `5469e5fc3d89ae9f36a1d515e681b1a9963df50d` (6 de octubre, 16:45:05 UTC / 18:45:05 de Madrid). Base previa al día `b8f935f2a1fbac17f8aac24be60a3e65cd2c2b98` (5 de octubre, 18:31:22 UTC). Se examinaron **los 83 commits completos** y ambos árboles, sin omitir modificaciones intermedias por mirar sólo el último diff. El compare agregado devolvía sólo 300 de 432 rutas: se complementó con árboles y archivos de cada commit.

**Resultado de conservación: no pasa la condición “sólo la caja”.** Hay cambios de contenido y navegación adicionales en originales públicos. La inspección anterior de unicidad/alcance propio no certificaba todo lo que otros commits incorporaron durante el día. Un mensaje que diga “owner-authorized” no verifica por sí solo la orden concreta de Iván; esta comprobación no atribuye un commit a una sesión por el nombre de la cuenta.

### Los 46 expedientes y sus enlaces

Los 46 expedientes activos siguen asignados a46 fuentes distintas: no se detectó duplicación. Antes de esta verificación, **39 enlazaban directamente a su fuente y 7 carecían de ese hipervínculo**. Se añade una pequeña nota con enlace **sólo a esas 7 VNext existentes**, conservando íntegro debajo su texto anterior; ningún original se toca para esa corrección y no se crea otro expediente.

En los originales, **11 tienen una caja de revisión enlazada a su propia VNext dentro de las primeras 30 líneas**, contando las notas de introducción después del título; sólo 6 están estrictamente antes de todo el cuerpo. **35 no tienen esa caja introductoria enlazada**. 12 originales contienen un enlace directo en algún lugar; elDDS lo tiene como párrafo sin caja. Las fichas externas de fuentes congeladas/identificadas se conservan como alternativa histórica; su existencia no se presenta como una caja dentro del original. Añadirlas ahora dentro de esos originales está fuera de esta comprobación de lectura.

<details>
<summary>Comprobación de cada fuente y su VNext</summary>

| Fuente | Única VNext | VNext→fuente al iniciar | Caja introductoria del original→VNext | Conservación en este día |
|---|---|---|---|---|
| [01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md](01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md) | [01_GRADIENT_VNext.md](01_GRADIENT_VNext.md) | Sí | No | Blob idéntico |
| [README.md](README.md) | [README_VNext.md](README_VNext.md) | Sí | Sí, línea 1 | Cambios adicionales |
| [README.md](../../research/ecosystem-awareness/README.md) | [README_VNext.md](../../research/ecosystem-awareness/README_VNext.md) | Sí | Sí, línea 1 | Cambios adicionales |
| [00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md](../../research/ecosystem-awareness/baseline/00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md) | [00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1_VNext.md](../../research/ecosystem-awareness/baseline/00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1_VNext.md) | Sí | No | Blob idéntico |
| [00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1.md](../../research/ecosystem-awareness/baseline/00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1.md) | [00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1_VNext.md](../../research/ecosystem-awareness/baseline/00D_A03_RS_00E_Q1A_STAGE_0_DETERMINISTIC_HARNESS_DESIGN_v0.1_VNext.md) | Sí | No | Blob idéntico |
| [README.md](../../research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/README.md) | [README_VNext.md](../../research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/README_VNext.md) | Sí | No | Blob idéntico |
| [00M_A01_MECHANISM_TO_REQUIREMENTS_TRACEABILITY_v0.1_WORKING_PROPOSAL.md](../../research/ecosystem-awareness/baseline/00M_A01_MECHANISM_TO_REQUIREMENTS_TRACEABILITY_v0.1_WORKING_PROPOSAL.md) | [00M_A01_VNext.md](../../research/ecosystem-awareness/baseline/00M_A01_VNext.md) | Sí | Sí, línea 1 | Sólo caja inicial |
| [00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md](../../research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) | [00M_VNext.md](../../research/ecosystem-awareness/baseline/00M_VNext.md) | Sí | No | Blob idéntico |
| [00N_RESEARCH_NEIGHBOURS_AND_EXPERIMENTAL_PRECEDENTS_v0.1_ADDENDUM.md](../../research/ecosystem-awareness/baseline/00N_RESEARCH_NEIGHBOURS_AND_EXPERIMENTAL_PRECEDENTS_v0.1_ADDENDUM.md) | [00N_ADDENDUM_VNext.md](../../research/ecosystem-awareness/baseline/00N_ADDENDUM_VNext.md) | Sí | No | Blob idéntico |
| [00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md](../../research/ecosystem-awareness/baseline/00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md) | [00N_VNext.md](../../research/ecosystem-awareness/baseline/00N_VNext.md) | Sí | No | Blob idéntico |
| [00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md](../../research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) | [00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md](../../research/ecosystem-awareness/baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) | Sí | Sí, línea 16 | Blob idéntico |
| [01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md](../../research/ecosystem-awareness/baseline/01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md) | [01C_VNext.md](../../research/ecosystem-awareness/baseline/01C_VNext.md) | Sí | No | Blob idéntico |
| [01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md](../../research/ecosystem-awareness/baseline/01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md) | [01D_VNext.md](../../research/ecosystem-awareness/baseline/01D_VNext.md) | Sí | No | Blob idéntico |
| [01I_AGENTIC_CITIZENSHIP_CONTRACT_HUMAN_GOVERNED_PARTICIPATION_PROFILE_v0.1.md](../../research/ecosystem-awareness/baseline/01I_AGENTIC_CITIZENSHIP_CONTRACT_HUMAN_GOVERNED_PARTICIPATION_PROFILE_v0.1.md) | [01I_VNext.md](../../research/ecosystem-awareness/baseline/01I_VNext.md) | Sí | No | Blob idéntico |
| [01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md](../../research/ecosystem-awareness/baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md) | [01J_VNext.md](../../research/ecosystem-awareness/baseline/01J_VNext.md) | Sí | No | Cambios adicionales |
| [01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md](../../research/ecosystem-awareness/baseline/01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md) | [01K_VNext.md](../../research/ecosystem-awareness/baseline/01K_VNext.md) | Sí | No | Creado hoy; sin fuente previa al día |
| [04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md](../../research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md) | [04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md](../../research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) | Sí | Sí, línea 9 | Blob idéntico |
| [README.md](../../research/ecosystem-awareness/baseline/README.md) | [README_VNext.md](../../research/ecosystem-awareness/baseline/README_VNext.md) | Sí | Sí, línea 1 | Cambios adicionales |
| [UC-EA-03_v0.4_MAINTENANCE_FREEZE.md](../../research/ecosystem-awareness/baseline/UC-EA-03_v0.4_MAINTENANCE_FREEZE.md) | [UC-EA-03_VNext.md](../../research/ecosystem-awareness/baseline/UC-EA-03_VNext.md) | Sí | No | Blob idéntico |
| [README.md](../../research/ecosystem-awareness/baseline/fixtures/00G-HF-ORACLE-v0.4/README.md) | [README_VNext.md](../../research/ecosystem-awareness/baseline/fixtures/00G-HF-ORACLE-v0.4/README_VNext.md) | Sí | No | Blob idéntico |
| [README.md](../../research/ecosystem-awareness/baseline/fixtures/00I-STATEFUL/README.md) | [README_VNext.md](../../research/ecosystem-awareness/baseline/fixtures/00I-STATEFUL/README_VNext.md) | Sí | No | Blob idéntico |
| [README.md](../../research/ecosystem-awareness/baseline/fixtures/00K-SUITE/README.md) | [README_VNext.md](../../research/ecosystem-awareness/baseline/fixtures/00K-SUITE/README_VNext.md) | Sí | No | Blob idéntico |
| [README.md](../../research/ecosystem-awareness/baseline/fixtures/RS-00E-Q1a/README.md) | [README_VNext.md](../../research/ecosystem-awareness/baseline/fixtures/RS-00E-Q1a/README_VNext.md) | Sí | No | Blob idéntico |
| [COMPUTABILITY_AND_ORACLE_PLAN.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/COMPUTABILITY_AND_ORACLE_PLAN.md) | [COMPUTABILITY_AND_ORACLE_PLAN_VNext.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/COMPUTABILITY_AND_ORACLE_PLAN_VNext.md) | Sí | No | Blob idéntico |
| [Escenario-creatividad-validacion.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/Escenario-creatividad-validacion.md) | [Escenario-creatividad-validacion_VNext.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/Escenario-creatividad-validacion_VNext.md) | Sí | No | Blob idéntico |
| [FENCING_CONFUSED_DEPUTY_EXTENSION.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/FENCING_CONFUSED_DEPUTY_EXTENSION.md) | [FENCING_CONFUSED_DEPUTY_EXTENSION_VNext.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/FENCING_CONFUSED_DEPUTY_EXTENSION_VNext.md) | Faltaba; enlace añadido aquí a su VNext | No | Creado hoy; sin fuente previa al día |
| [HUMAN_ESCALATION_WHISPERING.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/HUMAN_ESCALATION_WHISPERING.md) | [HUMAN_ESCALATION_WHISPERING_VNext.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/HUMAN_ESCALATION_WHISPERING_VNext.md) | Faltaba; enlace añadido aquí a su VNext | No | Cambios adicionales |
| [RATS_EXTENSION.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/RATS_EXTENSION.md) | [RATS_EXTENSION_VNext.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/RATS_EXTENSION_VNext.md) | Faltaba; enlace añadido aquí a su VNext | No | Creado hoy; sin fuente previa al día |
| [SPIFFE_SPIRE_EXTENSION.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/SPIFFE_SPIRE_EXTENSION.md) | [SPIFFE_SPIRE_EXTENSION_VNext.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/SPIFFE_SPIRE_EXTENSION_VNext.md) | Faltaba; enlace añadido aquí a su VNext | No | Creado hoy; sin fuente previa al día |
| [STAMP_STPA_EXTENSION.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/STAMP_STPA_EXTENSION.md) | [STAMP_STPA_EXTENSION_VNext.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/STAMP_STPA_EXTENSION_VNext.md) | Faltaba; enlace añadido aquí a su VNext | No | Creado hoy; sin fuente previa al día |
| [TECHNOLOGY_EXTENSION_PROTOCOL.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/TECHNOLOGY_EXTENSION_PROTOCOL.md) | [TECHNOLOGY_EXTENSION_PROTOCOL_VNext.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/TECHNOLOGY_EXTENSION_PROTOCOL_VNext.md) | Faltaba; enlace añadido aquí a su VNext | No | Cambios adicionales |
| [README.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/partial-experiments/README.md) | [README_VNext.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/partial-experiments/README_VNext.md) | Sí | No | Blob idéntico |
| [README.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/README.md) | [README_VNext.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/README_VNext.md) | Sí | No | Blob idéntico |
| [UC4_INTEROPERABILITY_PROFILE.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/UC4_INTEROPERABILITY_PROFILE.md) | [UC4_INTEROPERABILITY_PROFILE_VNext.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/UC4_INTEROPERABILITY_PROFILE_VNext.md) | Sí | No | Blob idéntico |
| [README.md](../../research/ecosystem-awareness/baseline/traversals/00G-HF-DYNAMIC-REVIEW-v0.1/README.md) | [README_VNext.md](../../research/ecosystem-awareness/baseline/traversals/00G-HF-DYNAMIC-REVIEW-v0.1/README_VNext.md) | Sí | No | Blob idéntico |
| [05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md](../../research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md) | [05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md](../../research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) | Sí | Sí, línea 5 | Blob idéntico |
| [05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md](../../research/ecosystem-awareness/fg-tida/interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md) | [05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md](../../research/ecosystem-awareness/fg-tida/interfaces/05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) | Sí | Sí, línea 13 | Blob idéntico |
| [README.md](../../research/regime-awareness/README.md) | [README_VNext.md](../../research/regime-awareness/README_VNext.md) | Sí | Sí, línea 1 | Cambios adicionales |
| [00_CANONICAL_MSCA_ARCHITECTURE.md](../../standards/minimum-sufficient-control/00_CANONICAL_MSCA_ARCHITECTURE.md) | [00_ARCHITECTURE_VNext.md](../../standards/minimum-sufficient-control/00_ARCHITECTURE_VNext.md) | Sí | No | Blob idéntico |
| [01_ACC_LINEAGE_IDENTITY_AUTHORITY_BINDING_PROFILE.md](../../standards/minimum-sufficient-control/01_ACC_LINEAGE_IDENTITY_AUTHORITY_BINDING_PROFILE.md) | [01_ACC_VNext.md](../../standards/minimum-sufficient-control/01_ACC_VNext.md) | Sí | No | Blob idéntico |
| [02_MSCA_ARCHITECTURAL_ROLE.md](../../standards/minimum-sufficient-control/02_MSCA_ARCHITECTURAL_ROLE.md) | [02_ROLE_VNext.md](../../standards/minimum-sufficient-control/02_ROLE_VNext.md) | Sí | No | Blob idéntico |
| [03_MSCA_ECOSYSTEM_COMPOSITION_AND_CONTROL.md](../../standards/minimum-sufficient-control/03_MSCA_ECOSYSTEM_COMPOSITION_AND_CONTROL.md) | [03_COMPOSITION_VNext.md](../../standards/minimum-sufficient-control/03_COMPOSITION_VNext.md) | Sí | No | Blob idéntico |
| [04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md](../../standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md) | [04_OPERATION_VNext.md](../../standards/minimum-sufficient-control/04_OPERATION_VNext.md) | Sí | No | Cambios adicionales |
| [README.md](../../standards/minimum-sufficient-control/README.md) | [README_VNext.md](../../standards/minimum-sufficient-control/README_VNext.md) | Sí | Sí, línea 1 | Cambios adicionales |
| [00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md](../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) | [00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md](../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md) | Sí | Sí, línea 14 | Blob idéntico |
| [DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md](../../research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md) | [DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md](../../research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md) | Faltaba; enlace añadido aquí a su VNext | No | Creado hoy; sin fuente previa al día |

</details>

### Originales de esos expedientes que cambiaron más allá de la caja

| Original | Cambio observado | Commits de contenido o navegación adicionales |
|---|---|---|
| [README.md](README.md) | Caja inicial, enlace final de estrategia y sección 01K dentro del cuerpo; esa sección fue después sustituida parcialmente. | [6c93994](https://github.com/dakleyer/structural-awareness-contributions/commit/6c93994c02959c0c0061c08b96983ed5c4afdfbe) · [39af310](https://github.com/dakleyer/structural-awareness-contributions/commit/39af310284c0ec84798814ad380473ae1d23f18c) · [8a2860a](https://github.com/dakleyer/structural-awareness-contributions/commit/8a2860a3dd3db128710504b444a642ad222dbfa6) · [7150279](https://github.com/dakleyer/structural-awareness-contributions/commit/715027943eefb372fdb4541a23d288bffdedbdb2) |
| [README.md](../../research/ecosystem-awareness/README.md) | Caja inicial, nueva secciónDDS y sustitución del párrafo de extensiones al incorporar01K/HID. | [d56e2e9](https://github.com/dakleyer/structural-awareness-contributions/commit/d56e2e9e37cf3a24ef076ff5913260fa830040c0) · [11fbc6e](https://github.com/dakleyer/structural-awareness-contributions/commit/11fbc6ee02a54afc8b0e6277e4266b590c725d25) · [b04fb86](https://github.com/dakleyer/structural-awareness-contributions/commit/b04fb86db8c0ef90e2d7aeb5ed7262e82bfbd1f2) |
| [01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md](../../research/ecosystem-awareness/baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md) | Nueva §5.2 sobre alertas/capacidad humana y cambio posterior de su descripciónHID. | [cf4fc5f](https://github.com/dakleyer/structural-awareness-contributions/commit/cf4fc5ff002d673ed6b4b5d4358dab9c8860a722) · [36e11da](https://github.com/dakleyer/structural-awareness-contributions/commit/36e11da213ceae7375b2257744f6b02a52f3f07d) |
| [README.md](../../research/ecosystem-awareness/baseline/README.md) | Caja, catálogos/fichas de navegación, rutasDDS y modificaciones del cuerpo para 01K/HID. | [a251f83](https://github.com/dakleyer/structural-awareness-contributions/commit/a251f837e83ae1ab9345c38a774b84710bf54a6f) · [985d661](https://github.com/dakleyer/structural-awareness-contributions/commit/985d661b1637284c552565af87a6c312918f3a4f) · [de681e8](https://github.com/dakleyer/structural-awareness-contributions/commit/de681e8d88b6d810502df2ea813f59058ed5934d) · [8757ba6](https://github.com/dakleyer/structural-awareness-contributions/commit/8757ba614c94f962206912d4896c119a18a924fa) · [b04fb86](https://github.com/dakleyer/structural-awareness-contributions/commit/b04fb86db8c0ef90e2d7aeb5ed7262e82bfbd1f2) · [7500dd5](https://github.com/dakleyer/structural-awareness-contributions/commit/7500dd5ee05c1a5052a28d35a8cefaf2c530707f) · [e80846a](https://github.com/dakleyer/structural-awareness-contributions/commit/e80846a0f9cf3b97cf222ed3d1e28b31d145ad3e) |
| [HUMAN_ESCALATION_WHISPERING.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/HUMAN_ESCALATION_WHISPERING.md) | Cambio de encabezado/edición y nuevas seccionesDDS con correspondencias, escenarios y resultados de modelo. | [6881dfe](https://github.com/dakleyer/structural-awareness-contributions/commit/6881dfe920a30ef6d00334f15059ab1dd931c8d4) · [b04fb86](https://github.com/dakleyer/structural-awareness-contributions/commit/b04fb86db8c0ef90e2d7aeb5ed7262e82bfbd1f2) |
| [TECHNOLOGY_EXTENSION_PROTOCOL.md](../../research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/TECHNOLOGY_EXTENSION_PROTOCOL.md) | Cambio de versión y nuevas seccionesDDS/protocolo de estudios y mecanismos. | [6881dfe](https://github.com/dakleyer/structural-awareness-contributions/commit/6881dfe920a30ef6d00334f15059ab1dd931c8d4) · [b04fb86](https://github.com/dakleyer/structural-awareness-contributions/commit/b04fb86db8c0ef90e2d7aeb5ed7262e82bfbd1f2) |
| [README.md](../../research/regime-awareness/README.md) | Caja inicial y sustitución de la explicación de Human Intelligence Debt. | [68fb9de](https://github.com/dakleyer/structural-awareness-contributions/commit/68fb9de8b115ad76ed617ec9a1c146e7a03bee70) |
| [04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md](../../standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md) | Nueva §4.1 de signalling/capacidad humana; dos revisiones posteriores del párrafo 01K/HID. | [41b51bf](https://github.com/dakleyer/structural-awareness-contributions/commit/41b51bffc6be37a15fbdd00ab034a2207a31f384) · [4c921c5](https://github.com/dakleyer/structural-awareness-contributions/commit/4c921c527daed5522e8f733a949a2ced387a46de) · [f2a3050](https://github.com/dakleyer/structural-awareness-contributions/commit/f2a305011dda679ec6ecd6b16e7791381033a37f) |
| [README.md](../../standards/minimum-sufficient-control/README.md) | Caja inicial y navegación adicional al final; el cuerpo previo se conserva, pero hay más que la caja. | [de681e8](https://github.com/dakleyer/structural-awareness-contributions/commit/de681e8d88b6d810502df2ea813f59058ed5934d) · [ee55859](https://github.com/dakleyer/structural-awareness-contributions/commit/ee55859f6a398249196db218ba6bbdad569692a4) · [7500dd5](https://github.com/dakleyer/structural-awareness-contributions/commit/7500dd5ee05c1a5052a28d35a8cefaf2c530707f) |

De las 40 fuentes que ya existían antes del día, 30 tienen exactamente el mismo blob, 1 sólo recibió la caja inicial (00M-A01), y 9 presentan cambios adicionales. Hay 6 fuentes nuevas del día: 01K, DDS y las cuatro extensiones técnicas. No se afirma que hayan sido “preservadas desde el inicio del día” cuando todavía no existían.

**01K necesita una mención propia:** se creó a las 15:42 UTC; después cambió en `2816aa1` y `9f397df`. Esta última revisión registra 918 líneas añadidas y 213 eliminadas. Es una sustitución/ampliación de contenido, no una caja. A las 16:42 UTC también se añadió a ese original el acceso a un paquete HC-HID nuevo, seguido de schema, vectores y verificación. Las nuevas versiones/decisiones que aparecen en sus VNext se conservan; esta verificación no las adopta como autorización para editar.

### Otros originales del repositorio que también cambiaron

El árbol inicial tenía 1097 archivos y el corte 1501: 28 preexistentes cambiaron, 404 se añadieron y ninguno se borró. Las 404 adiciones incluyen auditorías, preservaciones y artefactos de otros trabajos; el conteo no certifica originalidad, autoridad o cierre. El diario de los 83 commits toca exactamente esas 432 rutas, sin rutas modificadas y revertidas que se hayan ocultado en el diff final.

Fuera de las 46 fuentes asignadas, también hay adiciones dentro de 00K-A11, 00K-A15 y elREADME del fixture P5, actualización de índices/manifest/WORKPLAN y cambios enworkflow/scripts. Algunas rutas son VNext ya existentes y son legítimos espacios de revisión; no se confunden con el original. Los dos documentos P5 recibieron explicaciones en el cuerpo: tampoco son únicamente cajas iniciales. Se conserva evidencia del antes/después y commit sin ejecutar sus programas.

**Binarios preexistentes:** no aparece ningún cambio deblob en PDF, DOCX, PPTX, XLSX, ZIP o imágenes preexistentes en el árbol/diario del corte. Esto verifica bytesGit de esas fuentes, no equivalencia con originales externos de Drive ni validez de nuevas ejecuciones o artefactos creados hoy.

### Qué queda corregido y qué requiere decisión

Se corrigen los 7 hipervínculos dentro de VNext, sin ampliar sus afirmaciones de validación. Las 35 cajas ausentes en originales y los cambios de contenido permanecen diagnosticados, **sin insertar, restaurar o reescribir originales**. Para una restauración haría falta elegir cada versión/pasaje concreto y conservar antes/después; no se usa esta verificación como permiso de rollback, movimiento o eliminación.

Esta verificación documental no cierra las cinco pasadas ni la sexta unificadora. La continuidad de revisión mantiene originales en lectura, una VNext por unidad y resultados/fuentes/código congelados preservados. Ninguna modificación de fuente se oculta bajo la expresión “solamente navegación” o “solamente caja”.


---

## Revisión a fondo de los planes de cambio — 6 octubre 2026

**Evaluación realizada por Codex, mismo asistente de IA, para que una persona pueda decidir.** Se revisan el plan, sus motivos de auditoría, pares literales, impacto, riesgo, esfuerzo y dependencias; no es la sexta pasada científica global ni acredita el cierre de las cinco. Fuente de este cotejo: commit `06931f0b19b8df777e251091eccf5e3ee4ca9fbb`, [documento propietario](README.md), blob `641693f5a56e610fc1e76ae79ad41b96bd903f00`. Los registros anteriores y sus viejos completos permanecen íntegros.

La valoración actual distingue una mejora documental de una modificación conceptual o de contrato. **Candidato para revisión documental significa preparado para leer y decidir, no autorizado para incorporar.** Los originales siguen en sólo lectura; no se ejecuta ninguno de estos pares.

| Cambio | Calidad/estado actual | Impacto esperado | Riesgo | Esfuerzo | Prioridad |
|---|---|---|---|---|---|
| 1 | Ya publicado; Ya publicado | Medio | Bajo | Bajo | Histórico |
| 2 | Descartado; Descartado | No vigente | Alto | No procede | Histórico |
| 3 | Reformular; Reformulado; alternativa conjunta 71 | Medio | Medio | Bajo | Siguiente |
| 4 | Reformular; Reformulado; alternativa conjunta 71 | Alto | Medio | Medio | Primera |
| 5 | Reformular; Reformulado; alternativa conjunta 71 | Medio | Medio | Bajo | Siguiente |

**Cambio 1 — Ya publicado.** Hacer visible el expediente de auditoría.

**Beneficio esperado:** Hacer visible el expediente de auditoría. **Riesgo concreto:** Repetir la nota ya publicada duplicaría la entrada del README. **Coste de preparar y mantener:** No requiere nueva edición; mantener el vínculo.

**Localización actual:** viejo completo 1 coincidencia(s); texto propuesto 1 coincidencia(s), fuente actual completa. No se interpreta una cita o una subcadena del encabezado como modificación aplicada.

**Condición y orden de decisión:** No volver a ejecutar: el texto después está presente. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

**Cambio 2 — Descartado.** No se evalúa como beneficio actual: contradice los tres niveles canónicos acordados.

**Beneficio esperado:** No se evalúa como beneficio actual: contradice los tres niveles canónicos acordados. **Riesgo concreto:** Reabrirla expandiría la jerarquía y confundiría los catálogos auxiliares con canon. **Coste de preparar y mantener:** No invertir en ejecución; conservar la historia.

**Localización actual:** viejo completo 1 coincidencia(s); texto propuesto 0 coincidencia(s), fuente actual completa. No se interpreta una cita o una subcadena del encabezado como modificación aplicada.

**Condición y orden de decisión:** Retirada por la instrucción de tres niveles; los tres catálogos auxiliares no la reactivan. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

**Cambio 3 — Reformular.** No intervenir en el bloque central: el hallazgo de comprensión es válido, pero el lugar propuesto incumple append-only. Se integra con 4/5 en 71.

**Beneficio esperado:** Dar a una persona una pregunta corriente antes de los índices. **Riesgo concreto:** La inserción literal propuesta toca el cuerpo EP protegido; el texto debe adaptarse a una adición al final y evitar repetición con la introducción. **Coste de preparar y mantener:** Una explicación breve y comprobación de lectura; la adaptación de ubicación tiene que mostrarse antes/después.

**Localización actual:** viejo completo 1 coincidencia(s); texto propuesto 0 coincidencia(s), fuente actual completa. No se interpreta una cita o una subcadena del encabezado como modificación aplicada.

**Condición y orden de decisión:** Antes de decidir71, cotejar la explicación con 00M y los propietarios EA/RA/MSCA; conservar3 como historia. Revisar junto con 71. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

**Cambio 4 — Reformular.** La separación entre lectura semántica actual y evidencia histórica es importante. Insertarla dentro de la lista del README dejaría de conservar sus bytes;71 ofrece adición al final.

**Beneficio esperado:** Evitar que enlazar la nueva definición A/B/C/D parezca revalidar pruebas antiguas. **Riesgo concreto:** Una precisión local puede dejar que otros README, decks o pruebas continúen amplificando el resultado; tampoco autoriza reescribir evidencia histórica. **Coste de preparar y mantener:** Adición explicativa de EP y cotejo de notas 00M/00N y proof map; no repetir o modificar pruebas.

**Localización actual:** viejo completo 1 coincidencia(s); texto propuesto 0 coincidencia(s), fuente actual completa. No se interpreta una cita o una subcadena del encabezado como modificación aplicada.

**Condición y orden de decisión:** Verificar que71 no renueva pruebas, freezes ni adopción y que el texto previo completo permanece idéntico. Revisar junto con 71. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

**Cambio 5 — Reformular.** P1–P6 y posturasP1–P3 son listas distintas. La precisión sirve al lector, pero no debe sustituir o interrumpir el apartado anterior;71 reúne la aclaración.

**Beneficio esperado:** Impedir que una etiqueta de postura se lea como principio demostrado. **Riesgo concreto:** Cambiar IDs o solo una explicación dejaría referencias incompatibles; la inserción propuesta está en el cuerpo EP protegido. **Coste de preparar y mantener:** Nota breve con lectura cruzada de Requirements y Operation; no renombrar etiquetas.

**Localización actual:** viejo completo 1 coincidencia(s); texto propuesto 0 coincidencia(s), fuente actual completa. No se interpreta una cita o una subcadena del encabezado como modificación aplicada.

**Condición y orden de decisión:** Leer ambos usos deP y decidir la nota conjunta al final; ninguna renumeración. Revisar junto con 71. La decisión concreta de Iván sigue siendo necesaria para incorporar; publicar esta evaluación no la sustituye.

[Visión conjunta y tandas en EP README VNext](README_VNext.md#revisión-a-fondo-de-los-planes-de-cambio--6-octubre-2026). Mantener tres niveles de README, fuentes congeladas, resultados y binarios. Reorganización, nueva campaña, experimentos e incorporación canónica permanecen fuera de esta entrega.

### Imagen conjunta: qué planes son adecuados y cuáles todavía no

Se examinaron **las 47 VNext existentes**:22 contienen los 70 renglones del registro (61 pares y 9 líneas por concretar); otras 8 contienen 32 pares DDS/tecnología que no estaban incluidos en la vista anterior;17 no contienen un candidato literal propio. Los títulos y tablas no se contaron como lecturas científicas terminadas. Las aportaciones DDS0.1.2 y0.1.3 publicadas durante esta revisión también se cotejaron. Los cuatro nuevos pares0.1.3 y sus límites se documentan en la misma VNext DDS.

El registro anterior conserva 49 pares pendientes, aunque su resumen aún decía 53. Cuatro renglones ya habían pasado a superados/resueltos:64/67 y 65/66. En esta evaluación3/4/5 quedan reformulados en una **sola alternativa 71**, aditiva al final de EP. La cola efectiva queda en **47 pares pendientes**,7 ya publicados,1 descartado,2 superados,2 resueltos por otra edición y 3 reformulados; siguen 9 líneas sin par. El historial anterior de 70 entradas no se borra.

En las ocho VNext DDS/tecnología hay 32 pares históricos:25 coinciden literalmente con un después actual,3 tienen la sección incorporada con un separador diferente,1 mantiene su contenido con una adición posterior al preámbulo,1 quedó sustituido por otro preámbulo y 2 son bloques idénticos de conservación. No son 32 nuevos trabajos pendientes. En DDS, la sección 10B sí tiene par; la adición introductoria se describe aparte y no debe presentarse ese par como delta exhaustivo.

La lectura de los planes revela tres límites concretos:

- **Planes parciales:**18/33 corrigen sólo algunas frases de una misma época;40 corrige un estado W1 pero deja otras secciones por conciliar.25 es una tabla de reutilización, no una adaptación ya especificada.43–51 y parte de los expedientes sin candidato necesitan decisiones de alcance antes de un par. No están listos para aplicar.
- **Propuestas conceptuales acopladas:**35/37/38,57/58/59 y 68/69/70 están motivadas y tienen viejos localizados, pero requieren cotejo de los receptores y casos límite. El esfuerzo de 17,22/23,57–59 y 68–70 sube a **Alto** por lectura, validación y mantenimiento; redactar pocas líneas no mide ese coste.
- **Aclaraciones opcionales:**8 y 38 bajan a impacto **Medio** porque el contexto ya contiene parte de la reserva;52/53/54 mantienen su valoración vigente Medio/Medio/Medio.42/60 también pueden no incorporarse si el contexto basta. No se presume que toda adición sea mejor.

Un escaneo de texto completo encontraba el después en las citas de las propias propuestas 14/15/18/31/32/33/34/40/41. Se cotejaron los pasajes originales **fuera de esos bloques**: cada viejo sigue localizado una vez y el después no está aplicado allí.56/61 tienen un título limpio como subcadena de otro defectuoso; tampoco eso prueba incorporación.

### Tandas pequeñas y orden estratégico

| Tanda | Preparación que aporta valor | Impacto / riesgo / esfuerzo | Condición antes de una decisión |
|---|---|---|---|
|1 — Claridad de evidencia y estado |26/27: self-test y falta de independencia;31/32: reporte externo y fuente fechada;71: lectura conjunta al final de EP |Alto; riesgo Bajo/Medio; esfuerzo Bajo/Medio |Viejo actual, evidencia atribuida y límites completos. Son candidatos documentales; ninguna publicación de auditoría autoriza incorporarlos.|
|2 — Coherencia entre RA, EA y MSCA |35→37/38 y 01D;68/69/70 con 00M y el mismo receptor |Alto; riesgo Alto en cambios de clasificación; esfuerzo Alto para la conciliación |B reserva evaluable,C exploración fundada,D barrera efectiva y UNKNOWN sin forzar rol; mismo proceso/pregunta/scope/versión/tiempo.38 contextual no prueba fallo de todo el sistema.|
|3 — Contratos y protocolo |57→58→59;16/19 y candidatos 43–45;22/23 en successor;41 y pasos46–51 según gates |Alto; riesgo Alto; esfuerzo Alto o no estimable para campaña/realización |Comparación/empates/incomparabilidad/no máximo, autoridad y evidence limits; admisión anterior al outcome y fallos retenidos. No pesos, nuevos permisos, APIs o fallback universales.|
|4 — Lectura y rutas |6/7/9/10/12/13/20/28/30;56/61 y aclaraciones opcionales |Medio/Bajo; riesgo Bajo salvo anclas/autoridad; esfuerzo Bajo/Medio |Ediciones identificadas se preservan; navegación no promueve autoridad.56/61 necesitan compatibilidad de ancla.30 tiene cinco destinos, corrigiendo el cálculo anterior de cuatro.|

**Dos vistas, dos usos:** mayor impacto pendiente muestra qué preparar primero; candidato a revisión documental muestra pares con alcance concreto para leer/decidir. Un cambio de alto impacto/alto riesgo puede aparecer primero en la primera vista y seguir fuera de la segunda. Las precedencias57→58→59 y 46→47→48→49→50→51 prevalecen sobre un ranking individual;35/37/38 y 68/69/70 se leen juntos. El nuevo componente HC-HID se conserva y debe examinarse con su fuente vigente: no se vuelve al antiguo ledger64/67.

**Límite del cierre de esta entrega:** queda concluida esta evaluación de los planes disponibles en el corte, con un juicio publicado en cada una de las 47 VNext. **Las cinco pasadas materiales de todo el corpus y la sexta unificadora siguen abiertas.** Ni los 47 pares pendientes ni las fuentes nuevas se consideran validados o incorporados. Se mantiene la continuación sustantiva del programa.


**Revalidación del último avance concurrente:** `06931f0b19b8df777e251091eccf5e3ee4ca9fbb` añadió la VNext del contrato01K-A01. Se revisó su único par y se conserva la distinción fuente01K de investigación frente a contratoA01 de implementación; no son dos VNext de una misma fuente lógica. El corte final contiene47 expedientes y32 pares DDS/tecnología/componente adicionales al registro. El riesgo de esa aclaración de autoridad se valoraMedio; no se infiere implementación, calibración humana o réplica externa de nombrar un canon interno.

### Plan vigente para EP: alternativa aditiva conjunta71

Las propuestas 3/4/5 conservan sus textos anteriores y propuestos históricos, pero se dejan fuera de la cola de incorporación por su ubicación dentro del cuerpo protegido.71 reúne las aclaraciones al final: **impacto esperado Alto, riesgo Medio, esfuerzo Medio, prioridad Primera, tanda 1**. Beneficio: leer responsabilidades, evidencia y las dos listasP sin alterar lo anterior. Riesgo: abreviar de más la arquitectura o aparentar renovación de evidencia; coste: cotejar fuentes y comprensión, además de la redacción.

**Instrucciones de Iván:** sólo añadir al README y estrategia hasta su revisión; después, originales en sólo lectura, una VNext por fuente, siempre viejo completo y decisión concreta para incorporar. Este par es una propuesta futura; no modifica el README.

**Fuente y ubicación:** `architectural-contributions/ecosystem-positioning/README.md`, blob `641693f5a56e610fc1e76ae79ad41b96bd903f00`, commit `06931f0b19b8df777e251091eccf5e3ee4ca9fbb`. El bloque viejo es toda la sección final Development strategy; aparece una vez y llega al fin del archivo. Se conservaría completo y se añadiría el bloque nuevo después. No se sustituye la estrategia ni se crea otro README.

**Texto antes — viejo literal completo del contexto final**

~~~~markdown
## Development strategy and next advances

The next phase focuses on clarifying the evidence behind the architecture, developing a small end-to-end profile, defining a demanding comparison and extending only what can be supported. The [development strategy and priorities](./DEVELOPMENT_STRATEGY.md) (Spanish working proposal) explains these directions, where specialist knowledge can help and the external research that informs them.

This is a separate strategy document. It complements the architecture and its review programme; it does not replace the explanations above or turn planned work into a validation result.
~~~~

**Texto después — contexto conservado completo y adición propuesta**

~~~~markdown
## Development strategy and next advances

The next phase focuses on clarifying the evidence behind the architecture, developing a small end-to-end profile, defining a demanding comparison and extending only what can be supported. The [development strategy and priorities](./DEVELOPMENT_STRATEGY.md) (Spanish working proposal) explains these directions, where specialist knowledge can help and the external research that informs them.

This is a separate strategy document. It complements the architecture and its review programme; it does not replace the explanations above or turn planned work into a validation result.


## Reading the architecture and its evidence

A participant can receive an apparently correct output while the conditions that made it relevant have changed. Ecosystem Awareness qualifies what a process can support for a declared question and scope; Regime Awareness examines qualified changes in the applicable basis or regime; MSCA assesses sufficient configurations and possible repositioning. Qualification, permission, execution and confirmed effect remain separate responsibilities.

Use the current semantic notes to understand the architecture, and keep each frozen proof, scenario and result attached to its own assumptions, version and evidence limits. A current reading does not retrospectively validate an older proof or turn symbolic execution into a completed comparative experiment. The requirements express obligations to examine; traceability to them does not itself demonstrate fulfilment.

The labels P1–P6 name the semantic principles of Ecosystem Awareness. P1–P3 in the positioning discussion name operating postures. Read each label with its own definition and owner; they are different lists, and neither grants authority to act. The [review workspace](./README_VNext.md) records proposed clarifications and the decisions still needed.
~~~~

**Comprobación y decisión pendiente:** igualdad del viejo actual y del prefijo de todos los bytes originales; lectura conjunta con 00M,RA y MSCA y sus VNext; mismo significado de responsabilidades y límites. Iván puede aceptar la adición, pedir otro texto o decidir no incorporarla. El original permanece intacto durante esta revisión.


---

## Continuación sustantiva — posicionamiento local e interfaz EA/MSCA

**6 octubre 2026, Codex, mismo asistente; fuentes en `fa2c411c810950fb94924caae38938c52dfd5014`.** Se leyeron completos 01H,01B actual y 01D para examinar productor–consumidor–retorno; ArticleII completo se contrastó como procedencia. Las cuatro lecturas textuales propias de 01H/01B tienen explicaciones diferenciadas en sus únicas [01H VNext](../../research/ecosystem-awareness/baseline/01H_VNext.md) y [01B VNext](../../research/ecosystem-awareness/baseline/01B_VNext.md). Segunda material yquinta ampliada permanecen abiertas; no se declara cinco pasadas cerradas ni sexta global lanzada.

La cadena conserva una idea humana: tener una representación, evaluar si basta elcontrol, tener permiso yhaber logrado efecto son cosas distintas. Elestado vacío puede ser válido como representación yseguir UNASSESSED. Una oportunidad para obtener evidencia tampoco decide unatransición autorizada. Se registró la consecuencia en 00M,01C,01D, Architecture, Composition, Gradient y Operation, sin convertir ArticleII histórico en otro kernel o dueño actual.

**Hallazgo nuevo 72:**01B conserva enuna explicación local la antigua descripción deA como aserción/scope aunque cabecera ypayload ya usan elresultado funcional de 00M. Elpar literal íntegro está en 01B VNext: impacto/riesgo/esfuerzoMedio, prioridadSiguiente, aclaración opcional; original intacto. No se cambia la primera tanda 26/31/32 ni se acepta por defecto la propuesta nueva.

El contraste externo de 01H distingue Distributed Situation Awareness, los dos artículos de ValueofInformation de 2022 y Knowledge Gradient;01B contrasta RFC9334 yla propuestaFG-TIDA ATHENA. Se declara elalcance leído, derechos ypiezas candidatas; no diferencial o adopción demostrado, imports o pruebas nuevas. Un registro NIST mezcla título Concepts/CaseStudies con DOI delartículo Behavioral/Social; se identificaron los originales del editor en la auditoría, sin inventar por ello uncambio a 01H.

Se abrieron sólo dos VNext porque estas dos fuentes principales carecían deexpediente.01B v0.1/v0.2 comparten una unidad; no hay fichas, nuevos índices, otroREADME o VNext porpasada. Corpus actual 49 expedientes;48 pares pendientes y 9 líneas porconcretar enelregistro. Esos conteos no son cierre científico.

**Siguiente examen sustantivo:** completar ArticleIV yla arquitectura funcional para esta cadena, obtener elpaper urbano o su fuente auténtica identificada, yexaminar los perfiles/realizaciones que materialmente usan las condiciones. La búsqueda limitada fallida del sitio no desacredita su contenido. Mantener elcanon enlectura ycontinuar trabajo no dependiente de decisiones deincorporación.
