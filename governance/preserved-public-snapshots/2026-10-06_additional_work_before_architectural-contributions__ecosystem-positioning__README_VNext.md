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
