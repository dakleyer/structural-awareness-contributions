# Continuación del plan — lectura del README y fundamentos

**6 de octubre de 2026 · revisión acumulativa 1.4.** La revisión sigue en este mismo chat con una continuación programada cada hora. El objetivo es completar las pasadas de todos los documentos del alcance y la conciliación final; publicar avances no cierra ese objetivo. Los estados siguientes describen trabajo real, no la mera existencia de una VNext.

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
