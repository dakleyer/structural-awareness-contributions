> **Estado de aplicación — 15 octubre 2026.** Aplicadas y verificadas: 97. [Comprobación final](#owner-authorised-application-complete-15-october-2026). Los pares antes/después se conservan como trazabilidad; este lote aprobado ya no está pendiente.

> **Estado vigente — 12 octubre 2026.** Aplicadas y verificadas en main: cuatro adiciones de tanda5 y26cambios anteriores; UC-21 recibe su precisión de snapshot y conciliación de propuestas en su main. Ningún par vigente y ejecutable queda esperando otra autorización. Las nueve líneas43–51 describen investigación/perfiles/campañas sin un cambio literal definido. Sus estados permanecen separados. Las auditorías antiguas que dicen «pendiente» se leen por su fecha; la cola actual está en el registro de prioridades y este cierre.

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
| 2 · Antigua propuesta de convertir EP en Level 4 | Histórico · Histórico | No vigente | Alto | No procede | Descartado |
| 3 · Explicar la idea central antes de elegir una ruta | Siguiente · 4 — Lectura humana y rutas | Medio | Medio | Bajo | Pendiente de decisión |
| 4 · Separar semántica actual y resultados históricos | Primera · 1 — Claridad de evidencia y estado | Alto | Medio | Medio | Pendiente de decisión |
| 5 · Distinguir principios P1–P6 y posturas P1–P3 | Siguiente · 4 — Lectura humana y rutas | Medio | Medio | Bajo | Pendiente de decisión |

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
| 2 | Descartado; Descartado | No vigente | Alto | No procede | Histórico |
| 3 | Reformular; Reformulado; alternativa conjunta 71 | Medio | Medio | Bajo | Siguiente |
| 4 | Reformular; Reformulado; alternativa conjunta 71 | Alto | Medio | Medio | Primera |
| 5 | Reformular; Reformulado; alternativa conjunta 71 | Medio | Medio | Bajo | Siguiente |

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

**Aplicado — autorización de Iván, 12 octubre 2026.** Cambio71 incorporado en `architectural-contributions/ecosystem-positioning/README.md`. Fuera de pendientes. El par y su ficha anteriores se conservan en Git, predecessor `9fb9421711521decde6843b04914a143a1f04c35`.

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


---

## Continuación sustantiva — funciones, señales y límites de la taxonomía

**6octubre 2026,Codex,mismo asistente; snapshot `f7d8ed0846b301617197ade855d5237cbd2280f9`.** Seleyeron las tres partes 03funcionales (45.622caracteres) y ArticleIVcompleto (20.849), yse cotejaron pasajes focales de Foundation actual. [03 Functional VNext](../../research/ecosystem-awareness/baseline/03_FUNCTIONAL_VNext.md) recibe las cuatro lecturas textuales diferenciadas yuncontraste externo particular; [Foundation VNext](../../research/ecosystem-awareness/baseline/01_FOUNDATIONAL_VNext.md) declara explícitamente revisiónparcial de una fuente 135.021caracteres,aún sinlectura completa oquinta propia. Se abrieron sólo esas dos VNext que no existían; la spartes/versiones de cadaunidad comparten expediente. No hay VNextnueva de ArticleIV,ficha,índice,READMEohelper adicional.

La lectura confirma tresdistinciones útiles:una buena víadeadquisición no valida todos su smensajes,diferentestransportes no hacenindependientes fuentescompartidas,yuna petición no concedeautoridad. Se comentaron los doslados deesasrelaciones en 01H/01B/00M/00N/Requirements/04/DDS. No se cierra H06,lamatriz 176,perfiles orealizaciones por leerlos enlaces.

**Nuevo candidato 73,altoimpacto/riesgo/esfuerzo:** elbloque 1.1Ade Foundation presenta ampliacióncomo rasgocomún de Type 1/2; su propio §3.4conserva espera poruninputdefinido sinlímite/escape y §3.5silencio/faltadeevidencia/stalestatus promovidos acerteza dentro deU.73 propone explicitar que expansión es uncaso,nocondición necesaria. Si el autorusaampliación metafóricamente,puede ser precisión deexposición; no se presume falloruntime. La fuente completa ylos consumidores tienen queconciliarse antes decualquierdecisión. Elviejo completo yelpropuesto están en su VNext; eloriginal conserva todos susbytes.

ArticleIVy sus precedentes biológicos ayudan a formularhipótesis, no avalidar seguridad digital. PROV-DM ofrece linaje;ByzantineGenerals tiene otros supuestos/objetivos;FG-TIDA13 sigue siendo propuesta/discusión. Derechos/versiones/pasajes realmenteleídos yreutilización condicionada figuran en 03VNext. No se importócódigo/datos,noexperimentó ni atribuyó adopción.

**Continuidad:** completar Foundation integrada y su sfuentes materialmenteusadas,matrices deinterfaces/UC/perfiles y fuente urbana pendiente. La segunda material yquinta ampliada siguen abiertas; no se lanza lasexta global ni se marcaelcorpus concluido. Primeraonda 26/31/32 y 72 siguen sinincorporar;73es preparación deconciliación de riesgoalto,otra decisióndistinta.

---

## Continuación sustantiva — Foundation leída completa

**6 octubre 2026, Codex, mismo asistente; snapshot `409bfa9eff2b3e24e7350021db9e587861583de8`.** Se completó la lectura de los 135.021 caracteres del integrado Foundation, incluidos §§1–18, hipótesis, diccionario y procedencia. [Su única VNext](../../research/ecosystem-awareness/baseline/01_FOUNDATIONAL_VNext.md) conserva la auditoría focal anterior y añade las lecturas distintas, contraste externo propio, casos humanos y juicio actualizado del plan.

La explicación común queda más precisa: gestionar incertidumbre y conservar la vigencia del marco son problemas relacionados pero distintos; una alerta, un HOLD o un resultado adverso no diagnostican por sí solos Type 0/1/2 ni crean permiso. Procesar información retenida puede ayudar a un receptor limitado sin recuperar lo descartado. La utilidad y la preservación requieren comparaciones diferentes.

**73 se mantiene pendiente, con impacto/riesgo/esfuerzo Alto.** Leer todo el integrado refuerza los casos de scope fijo, pero también sus reservas de causalidad y cierre legítimo. La lectura integral deja de ser un gate pendiente; derivaciones y conciliación de perfiles siguen pendientes. Viejo/propuesto completos se conservan, sin nueva propuesta ni incorporación. Primera onda 26/31/32 sigue sin aplicar.

Los comentarios materiales se publican también en 03, 00M, 00N, Requirements, DDS y README RA VNext. No se abre una VNext, ficha, índice, helper o README. El corte actual contiene una VNext del paquete DDS de finalización añadida concurrentemente: se identifica como lectura material pendiente de esta revisión, no como cierre científico por existir.

**Continuidad concreta:** derivaciones 02A/02B, matrices/perfiles y fidelidad de v0.4/01A respecto al sucesor; fuentes primarias formales completas aún inaccesibles. Quinta ampliada y segunda material siguen abiertas. La sexta global no se lanza y no se cierra el corpus por este avance. Todos los originales permanecen en sólo lectura.

**Revalidación antes de publicar:** el head avanzó a `f0ebdd1031eb740b181c6a405fba6beb7f29ff6d`; cambió sólo la fuente DDS. Se leyeron sus nuevas §§3.1/5.3/7.1A/7.4: M admitido previamente, frontera de información del evaluador, mínimo privado frente a accesible y exclusión de P del numerador Type 1. Se preserva esa edición y se deja en Foundation/DDS la pregunta sobre el mecanismo y evidencia de cada diagnóstico. No es conciliación global ni auditoría completa de los estudios nuevos.

---

## Estado real de cobertura y recomendaciones — respuesta a Iván

**6 octubre 2026 · Codex, mismo asistente.** Comprobación documental del árbol y los expedientes en `fc6bc0406bd1e9ee4711914225b23c379ba0cb5e`; no otra pasada científica. **No están concluidas seis pasadas en cada expediente ni el plan consolidado de todo el corpus.**

Hay **52 archivos llamados VNext y el benchmark v0.3 reutilizado: 53 expedientes activos**. Frente al corte previo `b8f935f2a1fbac17f8aac24be60a3e65cd2c2b98`, que tenía cuatro VNext y ese benchmark, se añadieron 48 nombres VNext. Se excluyen copias de preservación; el conteo no atribuye cada creación a un agente ni certifica por sí solo unicidad lógica o revisión completa.

**32 expedientes contienen bloques literales emparejados de antes/después; 21 no los contienen.** Hay 101 pares visibles, incluidos históricos, navegación, incorporaciones y alternativas repetidas: no se presentan como 101 recomendaciones nuevas. Algunas ausencias se explican como conservación sin cambio; otras mantienen revisión propia, fuentes o plan pendientes. Tener un par tampoco acredita un plan final completo o un viejo vigente.

El registro conserva **73 entradas: 64 con par y 9 líneas por concretar**. Entre las primeras, 49 están pendientes de decisión, siete ya publicadas y ocho descartadas, reformuladas, desplazadas o resueltas por otra edición. Doce pares pendientes están preparados para revisión documental concreta, sin autorización de incorporación. Los tres cambios 26/31/32 eran una primera tanda de riesgo bajo; no el total.

**La entrega sigue incompleta:** faltan lecturas materiales, contrastes externos y consolidación; la sexta global continúa pendiente. La estructura de expedientes avanzó antes que su cierre. No se puede interpretar “sin candidato” provisional como documento exhaustivamente aprobado, ni completar un plan inventando cambios. Completar el examen sustentará los pares que procedan y las razones concretas para conservar los demás. El temporizador sigue eliminado; esta comprobación no lo reactiva ni modifica originales.

---

## Implementation record — Plan de Cambios 1.0 / PC1.0-01A — 10 October 2026

**Decision:** Source update authorized by the programme owner in the instruction to apply the first tactical stage. **Method:** additive only; no scientific or historical content rewritten.

**Source:** [EP README](./README.md) · before blob `a0a7f27842c13c409c4664bd1bda066860a98f83` · after blob `a5a3f6d8c0d142c8926708f405d1e72a7cb45814` · [commit](https://github.com/dakleyer/structural-awareness-contributions/commit/f77668d3dbc871bb0c84f365505492e7a9974108).





**Scope and status:** New reader route to DDS, UC-21, A26, R01 and the bounded S5 synthetic witness. The previous paragraph and following pre-standardization / external review paragraphs were preserved exactly. The remote GitHub content was re-read after the commit and verified against the expected insertion.

**Interpretation:** The new text attributes no Stage B/C success, real-product result, UC-4 admission or universal 00G→R01 transfer. The study's original scientific/evidence status stays with its owning source.

**Review still due:** Independent cold-reader 60–90-second comprehension test and maintenance-cost observation were not completed before user-authorized publication. If they show duplication or confusion, propose an additive successor correction; preserve this edition and its old text.

---

## Nueva revisión integral de cambios y consistencia — 12 octubre 2026

**Codex, mismo asistente de IA, revisión para una persona.** Corte `17b597bf91acb0f37daebc716e8f23f65daa23eb`, comparado con `09b8fe09082f15612114ebe0fd3be8418be7a061`. El examen iniciado con el árbol del 9 de octubre se amplió al avance del 12. Ambos cortes quedan identificados. Esta revisión conserva los originales.

Se recuperaron los **2.186 archivos** con bytes correspondientes a sus blobs Git: 2.145 textos y 41 binarios. Hay **657 añadidos, 37 modificados, 1.492 sin cambio y cero eliminados**. Los 41 binarios conservan sus blobs. Se cotejaron los deltas de los existentes y las relaciones de lo añadido. La lectura de sintaxis de 606 JSON, 299 fuentes Python y 1.712 registros de 53 JSONL no detectó errores; no se ejecutó código del corpus. Comprobar un archivo no demuestra su argumento, valida su experimento o sustituye la lectura visual de un binario.

La lectura material se centró en los contratos DDS, el oráculo/UC4, auditorías anteriores, instrumentos y nueva evidencia HF. Es una revisión integral de **cambios, integridad y consistencia**. Las cinco lecturas científicas de todas las fuentes y la sexta global conservan sus pendientes; no se declaran concluidas por estas comprobaciones.

### Hallazgos y consecuencias

- **Historia visible de auditoría.** DDS retiró propuestas incorporadas y su regla 8 ordena eliminarlas. Git conserva el antecedente, pero el procedimiento pide mantener viejos, conversación y desacuerdos en la única VNext. El cambio 75 propone conservarlos como historia fechada, fuera de la cola pendiente. Su recuperación auténtica y presentación siguen pendientes; no se reaplica lo incorporado.
- **Admisión del checker.** v0.3 añade motivo de no-aplicabilidad y separación entre A/B, pero hereda el tratamiento de `na_substitute_satisfied` como valor truthy. El string `"false"` puede satisfacer esa rama aunque no sea un booleano. El cambio 74 propone validación tipada en un futuro sucesor. Es un contraejemplo estático, no un ensayo realizado; v0.2/v0.3, sus freezes y resultados permanecen intactos.
- **Edición certificada frente al lector actual.** Los README de Family, Infoblox y HF no coinciden con sus manifiestos SHA256 locales. No se localizó aquí la época exacta de esos bindings. No prueba corrupción de datos o teoremas; exige aclarar qué edición certifican. Dos diferencias adicionales corresponden al preflight RAG fallido, que declara cero casos y error de input congelado. No se actualizan hashes históricos para simular conservación.
- **Copias de revisión.** Hay 71 nombres VNext y el benchmark reutilizado. Siete parejas entre feasibility/extensions son réplicas declaradas: tres iguales y cuatro con notas/rutas adaptadas, cotejadas. No son siete nuevas auditorías. Se preservan su custodia y propietario original; no se borra o abre otro expediente.
- **Evidencia contraria mantenida.** HF v0.6 contiene treinta casos, diez brazos y 300 registros; sus quince hashes y totales concuerdan. El control convencional fuerte registra siete efectos conocidos como prohibidos frente a ocho de EA, con 32 frente a 27 consultas. No se establece ventaja exclusiva ni suficiencia T4 calibrada. Son modelos y supuestos, sin runtime HF o humanos.
- **Prioridades revalidadas.** Los 49 pares antes pendientes siguen localizados una vez fuera de sus propias citas. La literalidad conserva trazabilidad, no acredita compatibilidad completa. La nueva cabecera DDS del oráculo ya separa infraestructura de resultado: 26 pasa a impacto Medio como aclaración opcional. 31/32 mantienen su valoración. 74/75 se añaden con impacto Alto, riesgo Medio y esfuerzo Medio.
- **Alcance de CI.** El guard de preservación se retiró y Documentation integrity ya no corre en cada push. Su ausencia no equivale a aprobación; tampoco se reactiva un guard rígido por esta lectura.

### Navegación y orden común

Se examinaron 9.180 enlaces internos en prosa Markdown corriente. Cuatro fragmentos locales aparecen en los viejos/nuevos de PC1.0-01A y pertenecen al README canónico, no a esta VNext: [mapa de pruebas](./README.md#technical-proof-map) y [ruta de reutilización](./README.md#canonical-reuse-route--from-one-successful-traversal-to-a-family-of-cases). Se conserva el viejo literal; estas rutas lo sitúan en su contexto. No se declara validación universal de enlaces externos, HTML, Mermaid o fuentes históricas.

**Orden propuesto:** resolver visibilidad de auditorías y admisión del checker; después aclarar épocas SHA y propietarios de réplicas; continuar las conciliaciones semánticas y protocolos ya pendientes. Los [pares 74/75 completos](../../research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md) muestran viejo, propuesto, beneficio, riesgo, coste y decisión necesaria.

El registro pasa a 75 entradas: 66 con par y nueve por concretar; 51 pares pendientes. Ningún orden autoriza incorporación. Los comentarios también llegan a EA/baseline, catálogo de extensiones, HF, Requirements, 00M, 01J y oráculo. Los predecessors y textos actuales se conservan. No nueva VNext, README, movimiento, código aplicado, experimento o mensaje externo. El temporizador sigue eliminado.

**Actualización delcorte antes de publicación:** main avanzó a `c36da6745c3893b0200014358c48178778d8cee9` mediante PR14. Se cotejaron sus once cambios: ocho archivos adicionales y tres lectores adaptados; elárbol final tiene2.194 archivos,665 añadidos desde6octubre,37modificados y1.492sin cambio. El anexo BOT-APPROX identifica los pins Git históricos HF y distingue replay de independencia. Se verificaron 127 pins de su corte, con tres lectores después adaptados. Se preserva, incluida su revisiónVNext ampliada. Family/Infoblox/HF conservan la época de sus antiguos SHA256 por aclarar: el nuevo pin Git de HF no determina por sí solo esa época. Los hashes no se editan. No se declara cerrado unbloque científico por ese merge.


---

## Consistencia del corpus en torno a DDS — 12 octubre 2026

**Codex, mismo asistente de IA; revisión para una persona.** GitHub sigue en `eb5d66d7e22dc18f093ee33fcd564e1fac6d2338`, el commit de la entrega anterior: no apareció un cambio público posterior durante este cotejo. Se comprobó la disponibilidad por blob de los 2.194 archivos y se releyó el método DDS completo, contrastándolo con sus lectores, apoyos y nuevas propuestas HF. La comprobación del árbol no equivale a seis auditorías científicas nuevas de cada archivo.

**Conclusión:** la coherencia principal se mantiene. Un Challenge puede seleccionar una especificación A; un paquete A congelado es la referencia de B; C necesita implementación fijada y efectos observados contra el Challenge. R01 no transfiere teoremas por analogía, C02 no valida una tecnología y UC-4 conserva su propia admisión. Los A/B/C/D epistemológicos y los namespaces locales siguen separados.

El contraste HF distingue dos preguntas compatibles: recalificar localmente un uso nuevo de canal puede preservar la tarea; detectar y tratar una deriva/transición material puede exigir la arquitectura de posicionamiento completa. Ningún texto examinado acredita prevención del incidente, operación de humanos, superioridad exclusiva o B/C. Los costes HC-HID/MSCA conservan su comparación de calidad/autoridad y las magnitudes sin valoración se mantienen separadas.

**Ajuste documental pequeño:** la primera nota de Stage A todavía dice “explicit DDS stages” para Stage1/Stage2. El [cambio 76, viejo completo y propuesta](../../research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#consistencia-de-dds-y-sus-receptores--12-octubre-2026) precisa que son dos fases internas de A. Impacto esperado **Medio**, riesgo **Bajo**, esfuerzo **Bajo**, prioridad **Siguiente**, preparado para decisión; no aplicado. No se cambia su numeración, §13.1, rutas, evidencia o jerarquía.

**Riesgos materiales ya abiertos:** 74, admisión booleana en futuro checker, y 75, recuperación de historia visible, conservan impacto Alto/riesgo Medio/esfuerzo Medio. T05/T06 son mejoras publicadas por su autor con independencia/replay pendientes; T04 es propuesta. No se vuelven a contar como nuevos hallazgos ni se declaran resueltos. La literalidad y el ranking tampoco completan las lecturas científicas.

Los comentarios de ambos extremos quedan en [EA VNext](../../research/ecosystem-awareness/README_VNext.md#consistencia-de-la-ruta-dds--12-octubre-2026), [HF VNext](../../research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/hugging-face/README_VNext.md#consistencia-con-dds-y-msca--12-octubre-2026) y [Operation VNext](../../standards/minimum-sufficient-control/04_OPERATION_VNext.md#consistencia-con-dds-y-recalificación-local--12-octubre-2026). Las cinco VNext actuales conservan íntegramente sus predecesoras; no se crea otra. El registro pasa a 76 entradas, 67 con par y nueve por concretar; 52 pares pendientes de decisión. Canon, código, resultados y binarios siguen intactos. Sin nuevas campañas, mensajes externos ni temporizador.


---

## Ampliación por el nuevo registro DDS — 12 octubre 2026

**Codex, mismo asistente.** Después de publicar el cotejo en `6f9c9f903a5c800740be77844c3fd4064ec16f59`, main avanzó a `f437c95cce3645a05ba45f52f521f6b9692e0aa7`. Se revisaron sus tres cambios y se leyó íntegro el nuevo [registro de aportaciones potenciales](../../research/ecosystem-awareness/DDS_POTENTIAL_CONTRIBUTIONS_REGISTER_v0.1.md): veinte familias relacionadas con 41 expedientes. Este corte tiene 2.196 archivos. Las notas anteriores mantienen sus cortes históricos; no se reescriben.

**La coherencia principal sigue mantenida:** el registro es investigación adicional y todas las familias permanecen PROPOSED. Conserva un DDS A/B/C, evidencia por objeto/referencia, derechos del receptor, costes declarados, baselines fuertes, resultados nulos y la separación de prueba matemática, software y humanos. El nuevo enlace del Index añade dos líneas y conserva su cuerpo anterior exacto, comprobado contra el snapshot; esa adición procede del merge entrante, no de esta auditoría. Los contratos y resultados no cambiaron allí.

[EA VNext](../../research/ecosystem-awareness/README_VNext.md#nuevo-registro-de-aportaciones-dds--cotejo-del-merge-del-12-octubre-2026) documenta un juicio específico de cada tarjeta. [DDS VNext](../../research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#registro-de-aportaciones-y-frontera-del-método--12-octubre-2026) mantiene dos condiciones antes de preparar perfiles: distinguir instrumento evaluador de tecnología medida en PC-010 y separar evidencia humana de ejecución técnica en PC-011/012/020.

**No confundir cantidades:** veinte líneas de investigación no son veinte nuevos cambios canónicos listos. P1/P2/P3 no declara riesgo Bajo ni sustituye el ranking de impacto/riesgo/esfuerzo. Los 76 candidatos del plan, incluidos 74/75/76, conservan sus disposiciones; no se fabrican viejos/nuevos para rellenar cada tarjeta. No se propone otra VNext para una hoja adicional ni se altera el modelo de tres niveles.

Se comprueban 138 enlaces internos del registro, veinte IDs y 41 fuentes únicas. Disponibilidad, permisos, fidelidad de los originales y novedades externas no se certifican por esos enlaces; R02 y D15 conservan límites de fuente. Esta ampliación publica comentarios en las mismas tres VNext y preserva todas sus auditorías previas. Sin originales, código o resultados editados por el cotejo, nuevas pruebas, contacto o temporizador; no cierre de quinta/sexta científica global.


---

## Revisión del otro agente sobre UC-21 — 12 octubre 2026

**Codex, asistente de IA; contraste documental para decisión humana.** Se revisó el informe aportado por Iván y las seis VNext de UC-21 publicadas en `ee680a019a0cbd7270415f44237c894d370d275c`, rama `when-controls-work-system-fails-v0.9.3` de dakleyer/use-cases. Se leyeron las seis auditorías completas y contratos centrales, con pasajes de hipótesis/preregistro, status/admisión de los nueve perfiles y versión S3/S6; no una nueva revisión científica íntegra de todas las APIs/escenarios o ejecución de producto.

**Lo que se sostiene:** ocho propuestas literales con viejos localizados una vez; seis expedientes de una misma auditoría con cuatro apartados PARCIALES, no seis auditores. EO-01…05 son un mapa editorial propuesto: gates no prueban HC; HR requiere R1 corregida con defensas retenidas; HS necesita respuesta/continuidad y no establece minimalidad o exclusividad. H1–H6 no son seis etiquetas de escenario. Es compatible con el método DDS, sin probar A/B/C por añadir esta trazabilidad.

**Lo que el resumen no cubría:**

- El commit sólo añadió seis VNext y no cambió sus fuentes. Pero S3 ya tenía un aviso de copia histórica y S6 había pasado a pointer de Contributions **antes** del commit auditado. La rama viva no es idéntica al envío aec08fb5 que sigue enlazado desde FG-TIDA. Los seis documentos fuente directos sí coinciden con el envío; ese hecho no acredita igualdad de todos los anexos.
- En 23 bindings de texto verificados con bytes Git, USE_CASE/S3/S6 difieren del SHA256 conservado. Los antiguos S3/S6 congelados sí coinciden; USE_CASE tampoco coincide en el snapshot congelado, por lo que su época exacta queda pendiente. No implica error de todos los argumentos, pero conservar un manifest no equivale a validarlo para la rama actual. No se cambian hashes ni se certifican los otros bindings/binarios.
- La Issue pública marca once sectores y SUBMISSION cuatro. Hace falta confirmar intención del propietario; no se infiere validación de sectores, error científico o permiso para corregir la Issue.
- Los planes del otro auditor no valoraban impacto/riesgo/esfuerzo. Se añadieron valoraciones y dependencias; la matriz y el registro tienen acoplamientos, por eso no son todos cambios de Bajo riesgo. Se precisó también distinguir hipótesis de requisitos y refutación de claim frente a respuesta a un objetivo.

Los comentarios y planes al final se publicaron en **las mismas seis VNext**, [commit 76ac39bae74d10f4586f5fb787f69deaf7f59add](https://github.com/dakleyer/use-cases/commit/76ac39bae74d10f4586f5fb787f69deaf7f59add). Se conservaron todos sus bytes previos; cero nuevas VNext, cambios en escenarios, fuente, manifest, main de use-cases o Issue FG-TIDA. El actual source 00J consultado se identifica por `68d406d6d22d1a6099b91810737cde06e521df02` y blob `17616f2495ccfc08828fed49d4f566f718e67eee`; su pin y el snapshot presentado tienen funciones distintas. No se sustituye o migra evidencia de uno al otro.

## Plan al final — orden de revisión de UC-21

**Primero:** declarar si se trabaja contra el paquete enviado congelado o la rama que consume escenarios externos. La propuesta mínima de [README VNext](https://github.com/dakleyer/use-cases/blob/76ac39bae74d10f4586f5fb787f69deaf7f59add/contributions/when-controls-work-system-fails/README_VNext.md#plan-al-final--prioridad-y-variante-mínima-de-lectura), Alto impacto/Bajo riesgo/Bajo esfuerzo, aclara esa expectativa sin reconstruir anexos ni recertificar hashes.

**Después:** preparar la matriz de [USE_CASE VNext](https://github.com/dakleyer/use-cases/blob/76ac39bae74d10f4586f5fb787f69deaf7f59add/contributions/when-controls-work-system-fails/USE_CASE_VNext.md#plan-al-final--matriz-y-conclusiones), Alto impacto/Medio riesgo/Medio esfuerzo, y cotejar lectores y [Run record](https://github.com/dakleyer/use-cases/blob/76ac39bae74d10f4586f5fb787f69deaf7f59add/contributions/when-controls-work-system-fails/templates/RUN_RECORD_VNext.md#plan-al-final--pregunta-previa-conclusión-por-claim). Una sola matriz propietaria; EO/claim/route/criterio se fijan antes del resultado, con Evidence E.6 concordante. Los lectores no necesitan tres copias completas de la tabla.

**Decisiones separadas:** la edición/destino y los sectores de [SUBMISSION VNext](https://github.com/dakleyer/use-cases/blob/76ac39bae74d10f4586f5fb787f69deaf7f59add/contributions/when-controls-work-system-fails/SUBMISSION_VNext.md#plan-al-final--versión-y-destino); hipótesis en [HYPOTHESES VNext](https://github.com/dakleyer/use-cases/blob/76ac39bae74d10f4586f5fb787f69deaf7f59add/contributions/when-controls-work-system-fails/annexes/HYPOTHESES_VNext.md#plan-al-final--tipo-y-dueño-de-la-afirmación); localizador HR opcional en [RECURRENCE VNext](https://github.com/dakleyer/use-cases/blob/76ac39bae74d10f4586f5fb787f69deaf7f59add/contributions/when-controls-work-system-fails/annexes/RECURRENCE_PROTOCOL_VNext.md#plan-al-final--localizador-opcional). Se mantienen viejos completos, atribución, desacuerdos y límites. Nada se incorpora a canon/envío sin la decisión concreta.

La primera tanda textual31/32/75 y su registro76 IDs mantienen su alcance anterior: no se añaden aquí ocho “nuevos fallos” ni se renumera el plan de Contributions por recibir un expediente externo. Este contraste tampoco cierra la quinta/sexta científica, crea otra jerarquía/expediente, activa pruebas, contacto o temporizador.


---



## Propuestas aplicadas retiradas

Por autorización de Iván del 12 octubre 2026 se retiran las fichas completas de cambios ya incorporados: textos, títulos, justificaciones, valoraciones y filas de prioridad. Las auditorías y las propuestas pendientes permanecen. Las decisiones y fichas completas se consultan en la [predecesora de esta limpieza](https://github.com/dakleyer/structural-awareness-contributions/blob/884e892a6fe1d0deffea493931c9fc5acf8e0258/architectural-contributions/ecosystem-positioning/README_VNext.md).

## Revisión del diseño de consolidación DDS por campañas — 12 octubre 2026

**Auditoría realizada por Codex, mismo asistente; revisión documental sobre el corte `07c83653babec79f387bdfd5fc4b93e4ac21b533`.** Iván solicita analizar el borrador autocontenido v0.2 de reorganización, no ejecutar la migración. Se leyó el plan completo y se contrastaron la navegación controlada, el método A/B/C, los contratos HF v0.3 y v0.3.1, sus ocho bindings de paquete, el catálogo de extensiones y los recorridos bot v0.6. El documento recibido permanece fuera del repositorio; aquí se publican las conclusiones de revisión.

**Juicio:** organizar por campañas es útil y compatible con DDS. Recomiendo primero un índice humano y un registro que enlacen las fuentes originales fijadas; la copia física y la adopción operativa se deciden después de resolver identidad, versiones y dependencias. El nuevo registro organiza expedientes; el Index DDS actual sigue gobernando la clasificación metodológica. El plan propone una organización, no una aceptación científica.

**Qué mejora:** reunir objeto bajo prueba, contrato, evidencia y resultado permite leer una campaña sin reconstruir primero 00G→R01→extensión. Ese linaje sigue explícito. Las campañas A/B/C separadas son una regla operativa prospectiva compatible con los objetos del método; no justifican dividir ni renombrar retrospectivamente runs existentes. No se obliga a crear B/C ni carpetas vacías. Los estudios sin contrato suficiente permanecen como antecedentes o soporte.

**Decisiones que faltan para aplicar la copia:**
1. Elegir una única fuente metodológica activa. Copiar verbatim el Index a `dds/canonical/` cambia el destino de sus enlaces `./baseline/...`; conservar el mismo texto no conserva su resolución. Preferir enlaces fijados al original. Una eventual copia es un snapshot identificado, nunca una segunda edición mantenida.
2. Fijar commit/ruta/blob de cada versión realmente consumida. Un inventario de un solo árbol actual no contiene por sí solo todos los antiguos inputs de freezes. El directorio `preserved/source-tree/` necesita distinguir las versiones de una misma ruta, o sustituirse inicialmente por referencias inmutables. No sobrescribir una versión con otra.
3. Definir identidad de campaña frente a versión de contrato y ejecución. Mantener separados registro, ejecución, adjudicación, aceptación y cierre; `cerrada` puede ser fallida. Los cambios materiales de contrato necesitan sucesión explícita; las erratas editoriales no crean campañas artificiales.
4. Definir quién mantiene qué. Registro de campañas, Index de método, catálogo de estudios, registro de claims y registro de aportaciones tienen funciones distintas. Sus campos compartidos deben remitir a un propietario o derivarse de él; mantener varios resúmenes manuales de estado introduce nueva deriva.
5. Mantener el método VNext: una sola VNext por unidad lógica, incluso si hay varias rutas archivísticas. Las correcciones nuevas se añaden al expediente existente o al sucesor científico justificado; no crean una auditoría por copia. La propuesta debe quedar también en los README VNext afectados antes de cambiar relaciones.
6. Preservar tres niveles de lectura: EP→Awareness→índice técnico. `dds/INDEX.md` puede ser una entrada técnica enlazada por el propietario acordado; `CAMPAIGN.md` es un expediente, no otro nivel canónico. La carpeta raíz no transfiere por sí sola propiedad de EA/FG-TIDA/RA/MSCA.
7. Separar accesos del lector ciego. El paquete HF prohíbe remitir al lector a adjudicaciones, resultados y predicciones del autor. El índice histórico público puede enlazarlos; la distribución de lectura ciega conserva su paquete neutral y referencias fijadas.
8. Hacer transaccional la publicación: preparar sobre un head exacto, comprobar que no cambió, comparar todo el árbol y publicar sin force. Una copia debe cerrar dependencias de enlaces/imports o declararse sólo archivística. Los scripts existentes pueden escribir resultados junto a sí mismos; cualquier futura comprobación ejecutada necesita un área desechable separada.

**Evidencia concreta:** los ocho blobs del manifiesto HF v0.3 coinciden con el corte actual. Sus requisitos congelados también coinciden. El mapa de preparación FG-TIDA congelado es `38d64f61ef81a300a20d9d89cda65e5bb6ba5b22`, mientras el árbol actual contiene `14ce6fd9a476f5943b64b2d54a903ec205c87d81`. Es una diferencia prevista por el contrato, no un fallo nuevo: copiar sólo el archivo actual no preservaría ese input. El addendum v0.3.1 corrige fuentes históricas sin cambiar el contrato de scoring v0.3. Ambos documentos deben leerse juntos. HF cuenta con121 archivos actuales en su subárbol, pero su cierre de dependencias incluye fuentes fuera de él y versiones anteriores. Ese conteo no mide campañas ni cobertura científica.

**Tandas propuestas, todavía sin ejecutar:** primera, lectura/indexación HF con originales fijados y una fila de soporte compartido R01; siguiente, probar que el registro puede describir otro estudio Simplified sin heredarlo de HF; después, copiar sólo paquetes cuyo beneficio esté demostrado y cuya matriz de versiones/dependencias esté aprobada; finalmente, decidir la ubicación operativa de nuevas campañas. No hace falta copiar todo DDS para obtener el beneficio de navegación.

**Prioridad y coste:** el piloto de índice tiene impacto esperado Alto, riesgo Bajo si sólo enlaza y esfuerzo Medio por la lectura de contratos/versiones. La copia completa tiene beneficio adicional por justificar, riesgo Medio–Alto y esfuerzo Alto: incluye versiones antiguas, enlaces, contextos de ejecución y mantenimiento. La adopción operativa tiene impacto potencial Alto, riesgo Medio–Alto y esfuerzo no estimable hasta identificar consumidores/propietario. Estos juicios no aplican una tanda ni modifican criterios de aceptación.

**Fuentes:** [control documental §14](https://github.com/dakleyer/structural-awareness-contributions/blob/07c83653babec79f387bdfd5fc4b93e4ac21b533/DOCUMENT_CONTROL.md#14-6-october-2026--three-corpus-reading-levels-structural-proposals-in-readme-vnext), [Index DDS](https://github.com/dakleyer/structural-awareness-contributions/blob/07c83653babec79f387bdfd5fc4b93e4ac21b533/research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md), [contrato HF](https://github.com/dakleyer/structural-awareness-contributions/blob/07c83653babec79f387bdfd5fc4b93e4ac21b533/research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/hugging-face/DDS_STAGE_A_PREREGISTRATION_CONTRACT_v0.3.md), [addendum](https://github.com/dakleyer/structural-awareness-contributions/blob/07c83653babec79f387bdfd5fc4b93e4ac21b533/research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/hugging-face/DDS_STAGE_A_SOURCE_FREEZE_ADDENDUM_v0.3.1.md). Registro cruzado en las VNext de EA, baseline, extensiones, HF y DDS. Ningún texto de fuente, freeze, resultado, código o ruta fue cambiado por esta auditoría.


## UC-21 y DDS: dos entradas enlazadas — 12 octubre 2026

**Revisión por Codex, mismo asistente.** Iván precisa que UC-21 es el caso con objetivos y campañas, y DDS el método de investigación. Se mantiene esta distinción y se ajusta el orden del diseño de consolidación: primero probar la navegación desde UC-21 usando sus ejercicios existentes; después comprobar su generalidad con HF y otra familia. No se crea una nueva campaña S5 ni se mueve el caso al corpus metodológico.

La entrada pública [UC-21](https://github.com/FG-TIDA/use-cases/issues/21) remite en su cuerpo al snapshot `aec08fb5b0fac2ee399372370e9ee2a82a2d5779`. Su cuerpo no nombra DDS; sus comentarios sí lo explican en [S5](https://github.com/FG-TIDA/use-cases/issues/21#issuecomment-6109154445) y [S4/CDA](https://github.com/FG-TIDA/use-cases/issues/21#issuecomment-6111953753). README y USE_CASE coinciden entre aquel snapshot y la rama de revisión `76ac39bae74d10f4586f5fb787f69deaf7f59add`, pero S6 de la rama es un adapter hacia 00J/00J-A01. Por eso publicar una propuesta en la rama no modifica lo que alcanza el lector del enlace congelado. Una futura actualización de la entrada debe añadir una ruta explícita al seguimiento y mantener el envío anterior. La Issue y sus comentarios no se modifican aquí.

El [autor de S5](https://github.com/FG-TIDA/use-cases/issues/21#issuecomment-6115830369) propone cerrar en el alcance evidenciado. Se comprobó su README externo v0.1.3, blob`4b0d2a673c8ee945bd6c52248390a3c595b9285a`: declara `I2-complete` completo para las ramas seleccionadas dentro del modelo y separa predicates enforced/assumed upstream. Esto explica el estado de esa discusión; no constituye una nueva aceptación conjunta ni un rerun. La organización conserva el ejercicio y sus pins, sin reiniciarlo para llenar el registro.

**Relación propuesta:** entrada UC-21 → explicación del caso y objetivos → escenarios/hipótesis → ejercicios existentes → contrato DDS aplicable → runs/evidencia → conclusión para el objetivo UC-21 → posible selección posterior de especificaciones. Desde DDS se recorre la misma relación por método → campañas de distintos casos → fuente del Challenge → evidencia → resultado. El registro futuro debe apuntar a los expedientes reales y sus propietarios, con varias relaciones por campaña; no duplicarlos bajo ambas entradas.

**Asignación de funciones:** UC-21 mantiene su problema, objetivos, HC/HR/HS/H1–H6 y gates. DDS mantiene método y A/B/C. El expediente del estudio mantiene contrato, versión, comparadores, ejecución y conclusión. EA, RA, MSCA y otros componentes conservan fuentes y decisiones de incorporación. Objetivo, R0/R1/R2, Stage A/B/C, modo de evidencia y estado de ejecución son dimensiones separadas. Un resultado del caso no demuestra automáticamente necesidad de EA ni selección de una especificación.

**Preservación:** enlaces actuales, snapshot enviado, anexos, escenarios, figuras, pruebas, denominadores y autoría conservados. Toda relación estructural se revisa en las VNext de README correspondientes; tres niveles EP→Awareness→índices técnicos, con expedientes de campaña como documentos de trabajo. Mantener una sola VNext lógica aunque un registro enlace varias rutas. La copia física posterior sigue pendiente de matriz de versiones/dependencias; no es necesaria para implementar la lectura propuesta.

**Prioridad:** puente de lectura inicial de alto impacto esperado y riesgo Bajo; esfuerzo Medio por contraste entre repositorios y épocas. La precisión de trazabilidad de campañas en el caso tiene impacto Alto y riesgo Medio: debe concordar con la matriz de objetivos y plantilla RUN_RECORD antes de adoptarse como campo obligatorio. No se activan campañas, adopción canónica, cambios de Issue ni redistribución por publicar esta revisión.

**Orden revisado:** 1) cerrar diseño de lectura desde la Issue UC-21 y distinguir envío/seguimiento; 2) preparar puente mínimo en README y trazabilidad en USE_CASE, con antes/después en sus VNext; 3) describir el S5 existente y S4/CDA en su estado real, sin campañas artificiales; 4) probar HF y soporte compartido; 5) aprobar matriz y copia sólo donde aporte valor; 6) decidir operación futura. Esta instrucción ajusta la recomendación HF-first anterior; se conserva su texto como historia. DDS sigue siendo útil fuera de UC-21.

Pares concretos en [UC-21 README VNext](https://github.com/dakleyer/use-cases/blob/when-controls-work-system-fails-v0.9.3/contributions/when-controls-work-system-fails/README_VNext.md) y [USE_CASE VNext](https://github.com/dakleyer/use-cases/blob/when-controls-work-system-fails-v0.9.3/contributions/when-controls-work-system-fails/USE_CASE_VNext.md). Registro recíproco en [EA VNext](../../research/ecosystem-awareness/README_VNext.md) y [DDS VNext](../../research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md). No se modificó la propuesta local v0.2, se creó dds/ ni se aplicaron estos pares.


## Puente UC-21–DDS incorporado — 12 octubre 2026

Iván confirma continuar con UC-21→objetivos→ejercicios existentes→DDS→resultados del caso. Se aplicaron los dos pasajes completos preparados en las VNext del README y USE_CASE: [publicación 56eb0252c63cedc7aa578e7c3a5c897cc9669c5e](https://github.com/dakleyer/use-cases/commit/56eb0252c63cedc7aa578e7c3a5c897cc9669c5e). El README explica caso/método/corpus y enlaza discusiones S5/S4; USE_CASE relaciona objetivo, contrato, Stage, evidencia y conclusión. Se conserva el resto de bytes de ambas fuentes mediante verificación inversa exacta. R0/R1/R2, A/B/C, criterios, hipótesis, anexos, figuras, freezes, código y resultados no cambiaron.

Las dos fichas aplicadas se retiraron de sus VNext activas y quedaron en Git/custodia auténtica; las auditorías y otras propuestas pendientes permanecen. Sólo cuatro archivos cambiaron en la rama: los dos lectores y sus dos VNext;73otrosblobs idénticos,0 nuevos/eliminados. La plantilla RUN_RECORD y la matriz EO anteriores no se aplicaron. SHA256SUMS.txt conserva su época anterior y no certifica los dos lectores nuevos. Main use-cases y el envío congelado permanecen intactos.

La Issue pública mantiene sus enlaces de envío. El [README VNext](https://github.com/dakleyer/use-cases/blob/when-controls-work-system-fails-v0.9.3/contributions/when-controls-work-system-fails/README_VNext.md) deja preparado un único párrafo adicional con antes/después literal, Alto impacto/Bajo riesgo/Bajo esfuerzo, para enlazar seguimiento y DDS manteniendo el snapshot. Es una edición externa pendiente de decisión concreta. No se modificó la Issue, abrió otra campaña S5, creó carpetaDDS ni ejecutó migración o experimento. Este estado supersede las menciones previas a esas dos inserciones como pendientes; no altera los otros gates abiertos.


## Trabajo complementario todavía pendiente

Las épocas de los tres bindings SHA/README siguen por aclarar, con hashes intactos. Las siete parejas VNext se conservan como réplicas con propietario, no se borran o cuentan como independencia. HF sigue reteniendo el comparador convencional y resultados adversos; no se reescriben para fabricar ventaja EA. Esos hallazgos necesitan su trabajo propio y no se presentan como “resueltos” por tres frases.



## Reserva pendiente fuera de las olas aplicadas

La precisión del [README UC-21](https://github.com/dakleyer/use-cases/blob/76ac39bae74d10f4586f5fb787f69deaf7f59add/contributions/when-controls-work-system-fails/README_VNext.md#variante-acotada--envío-congelado-y-rama-viva), Alto impacto/Bajo riesgo textual/Bajo esfuerzo, es buena candidata de lectura. Su incorporación todavía necesita escoger un lector de revisión/sucesor: el README original continúa protegido. **No entra automáticamente como cuarto reemplazo ni se modifica el envío de FG-TIDA.**

Quedan fuera de Ola1: checker74 y sus pruebas prospectivas; restitución histórica75; recertificación o cambio de manifiestos; sectores de Issue21 sin decisión del propietario; matriz científica y campos del Run record UC-21, con riesgo Medio y dependencias. Tampoco se borra una réplica o se reinterpreta el resultado adverso de HF por aprobar esta ola. Las tareas científicas de cinco/sexta mantienen su estado.





<details>
<summary>Historial de las propuestas incorporadas</summary>

<a id="ep-readme-delta-001--nota-de-versiónrevisión-y-enlace"></a>
<a id="cambio-1--nota-de-acceso-a-revisión-de-ep"></a>
<a id="texto-antes--viejo-complete-affected-paragraph"></a>
<a id="texto-después--publicado-complete-affected-local-unit"></a>
<a id="primera-tanda-textual-de-alto-impacto-y-bajo-riesgo--12-octubre-2026"></a>
<a id="visión-conjunta-y-decisión"></a>
<a id="por-qué-se-mantiene-el-impacto-y-cómo-se-limita-el-riesgo"></a>
<a id="lo-que-no-se-convierte-en-parche-por-esta-selección"></a>
<a id="ola-1-propuesta--alta-prioridad-alto-impacto-y-bajo-riesgo"></a>
<a id="tres-pasajes-dos-vnext-una-tanda-pequeña"></a>
<a id="ejecución-que-propongo-después-de-una-decisión-concreta"></a>
<a id="reserva-y-ola-siguiente"></a>
<a id="ola-2--diez-cambios-concretos-para-decidir"></a>
<a id="orden-y-alcance"></a>
<a id="conciliación-material-de-esta-propuesta"></a>
<a id="decisión-y-aplicación"></a>
<a id="ola-2--textos-directos-y-asertivos"></a>
<a id="olas-aplicadas-y-pendientes-vigentes--12-octubre-2026"></a>
<a id="ola-3--diez-mejoras-quirúrgicas-de-lectura-y-trazabilidad"></a>
<a id="ola-4--coherencia-de-interfaces-y-escenarios-fuera-de-dds"></a>
<a id="olas-3-y-4-aplicadas--12-octubre2026"></a>
<a id="bloques-aplicados-retirados"></a>
<a id="ola2-diez-cambios"></a>
<a id="ola2-redaccion-directa"></a>
<a id="ola3-diez-cambios"></a>
<a id="ola4-interfaces-escenarios"></a>

Las fichas retiradas se conservan completas en la [edición anterior](https://github.com/dakleyer/structural-awareness-contributions/blob/884e892a6fe1d0deffea493931c9fc5acf8e0258/architectural-contributions/ecosystem-positioning/README_VNext.md). Los enlaces anteriores siguen llevando a este historial.

</details>


## Plan gradual de navegación UC-21 → objetivos → Challenges → DDS → campañas y resultados

**12 octubre 2026 · instrucción vigente de Iván.** Hacer la navegación realmente accesible y publicada, conservar cada texto y enlace previo, organizar paso a paso sin perder campañas, ejercicios, reducciones, extensiones o archivos. Se reutilizan los índices y VNext actuales. La primera entrega añade orientación y enlaces; ninguna redistribución física queda implícitamente ejecutada.

**Comprobación terminológica previa.** Se leyeron UC-21 Conventions/Extensionality, DDS A §3/§6/§10A, DDS B/C, R01, el protocolo de extensiones, kernel E1–E7, HEW Technical Report, DBC, 00D, Requirements y los índices RA/MSCA pertinentes. La búsqueda pública de usos complementó esas lecturas; no equivale a leer cada documento histórico. Challenge define problema/familia; el escenario delimitado lo instancia. UC-21 mantiene S1–S6 y sus familias 00E–00J. HEW usa escenario como descripción humana con instancia formal. Campaña de investigación, campaña operativa de S4 y unidad de campaña R01 no son intercambiables. Ejercicio se usa como entrada de lectura para estudios/recorridos existentes, no como nuevo tipo normativo. A/B/C DDS, A–D causales, A/B/C/D epistemológicos, R0/R1/R2 UC-21 y R01-R1/R2/R3 siguen con sus fuentes. La adición inicial que identificaba escenario con problema se corrigió antes de publicarse.

### Qué debe poder recorrer una persona

Entrada pública UC-21 → objetivos y protocolos → Challenges/familias → DDS y escenario de evaluación tecnológico → campañas/estudios y runs → resultados → conclusión para su objetivo y posible selección posterior de especificaciones. DDS también ofrece acceso desde otros casos. Una reducción, un anexo, un simulador o una nueva versión no crea automáticamente una campaña.

### Tandas y criterio de salida

| Tanda | Trabajo concreto | Salida y comprobación | Impacto / riesgo / esfuerzo |
|---|---|---|---|
| 1. Entrada y objetivos | Añadir en la Issue UC-21 una ruta al seguimiento; reunir cinco preguntas ya existentes en README y USE_CASE; enlazar escenarios, protocolos, DDS, instrumentos e informes actuales. | Entrada publicada y lectura de vuelta; viejo de cada fuente recuperable íntegro; conservar el envío aec08fb5. | Alto / Bajo para enlaces, Medio para síntesis de objetivos / Medio |
| 2. Inventario y relaciones | Inventariar por repo/ref/ruta/blob; extraer enlaces y referencias de método/código/manifests; distinguir originales, fuentes congeladas, versiones, copias, supports y adicionales. | Cada archivo tiene tratamiento y propietario visible; no descartar una dependencia por parecer suelta. Inventario actual no sustituye versiones consumidas por un freeze. | Alto / Medio / Alto |
| 3. Escenarios y ejercicios | Contrastar UC-21 S1–S6 y sus familias; registrar objetivo, fuente, admisión, reducción/extension, tecnología/configuración, instrumentos y estado de cada estudio. | Antes de agrupar, aclarar unidad y relación. S5 existente se conserva; S4/CDA sigue propuesta; HF v0.3 no se mezcla con exploraciones bot. | Alto / Medio / Alto |
| 4. Método e instrumentos | Facilitar DDS A/B/C, R01, comparator/fairness, oráculo/harness, C11/T03 y UC-4 desde un propietario técnico. | Fuente metodológica única y herramientas con su función y versión. Un self-test de instrumento no es resultado del candidato. | Alto / Medio / Medio–Alto |
| 5. Campañas y resultados | Reutilizar informes y registros reales; completar explicación de pregunta, contrato, inputs, runs, resultados, costes, límites, desacuerdos y sucesor. Crear documento de campaña sólo si una campaña registrada realmente carece de informe legible. | Lectura caso↔campaña↔evidencia↔conclusión. Conservar casos positivos, negativos, nulos y no entrega, sin sumar denominadores incompatibles. | Alto / Medio–Alto / según cada expediente |
| 6. Conciliación | Revisar todas las rutas principales, enlaces de ida/vuelta, versiones/autoridad, unidades de resultado y acceso a materiales históricos/adicionales. | Cero pérdida de archivos/texto/links previos por la tanda, límites y pendientes visibles. Alcance de cierre fijado; no cierre científico por un scan. | Alto / Medio / Alto |

### Primera tanda concreta autorizada

Tres fuentes reciben sólo adiciones: README y USE_CASE de la rama propietaria de UC-21; DDS Canonical Method Index de Contributions main. Pares completos en [README VNext](https://github.com/dakleyer/use-cases/blob/when-controls-work-system-fails-v0.9.3/contributions/when-controls-work-system-fails/README_VNext.md), [USE_CASE VNext](https://github.com/dakleyer/use-cases/blob/when-controls-work-system-fails-v0.9.3/contributions/when-controls-work-system-fails/USE_CASE_VNext.md) y [DDS VNext](../../research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md). Los enlaces de la Issue siguen apuntando al envío original; se les añade seguimiento a la edición publicada. La Issue se vuelve a leer justo antes de escribir para no sustituir un cambio concurrente.

La síntesis reúne: corrección/continuidad; eficacia de defensas existentes; recurrencia HR después de corrección R1; causalidad HC; respuesta suficiente HS. H1–H6 siguen siendo contrastes separados. No se crean EO obligatorios, H7, ruta R3 UC-21, gates nuevos ni resultados.

La navegación de DDS enlaza trece registros de estudios locales existentes, cada uno con informe, preregistro, freeze y evidencia, y mantiene accesos a trabajos simbólicos/fixtures y reducciones desde sus índices previos. La tabla es del catálogo de extensiones, no todas las campañas del corpus. La carpeta dds/ y su registro futuro siguen como diseño hasta reconciliar identidad, versiones y dependencias. No se crean copias, se mueven archivos ni se cambian contratos por esta tanda.

### Conservación y controles de cada entrega

Antes de editar se conserva la predecesora auténtica. Para estas adiciones, quitar únicamente los bloques añadidos debe reconstruir todos los bytes previos de las fuentes. Cada URL/fragmento previo se conserva. Se comparan árboles completos: sólo paths acordados, cero archivos perdidos/renombrados, código/resultados/manifests/fuentes congeladas intactos. La publicación usa head fijado, scope y readback, sin force. Las fichas aplicadas salen de la cola activa y quedan en Git; auditorías y decisiones abiertas permanecen.

Fuentes de partida: Contributions `90a31353528d777d0b617152ed54a67991239612` (2.200 blobs) y la rama UC-21 `f0701670e5beb8d97cfff3bbf3796bdf80e869ec` (77 blobs). Esos conteos son el universo de rutas de este corte; no una declaración de lectura semántica de los 2.277 archivos ni de ausencia previa de huérfanos. La comprobación de la tanda impide perder contenido; la conciliación completa de rutas actuales continúa en las tandas 2–6.

### Propietarios y términos compartidos

Mantener EP→Awareness→índices técnicos como los tres niveles. UC-21 conserva su entrada propia. EA, RA, MSCA, R01, cada estudio y el testbed conservan responsabilidad por sus significados y evidencias. Registrar una relación entre ellos no transfiere propiedad o validación. Antes de renombrar o dividir, plantear aquí y en cada README VNext afectada el antes/después de rutas, qué enlaces cambian, quién mantiene la nueva relación y cómo se conserva el original.

El vocabulario común debe relacionar significados que ya existen, no imponer por nombre equivalencias entre unidades distintas. La siguiente pasada terminológica contrastará especialmente campaña R01 frente a campaña DDS; escenario narrativo/familia frente a instancia congelada; oracle de información frente a instrumento de referencia; y extension de familia UC-21 frente a transferencia/isomorfismo R01. Las adiciones actuales remiten a sus definiciones propietarias, sin reescribirlas.

**Aclaración de Iván — ruta ratificada:** UC-21→objetivos→Challenges→DDS→campañas→resultados. Dentro de DDS, escenario de evaluación designa la aplicación de una tecnología/configuración a un Challenge. Se conserva la distinción de la fuente entre instancia/base delimitada y technology mapping/profile; no se sustituyen los nombres de los originales ni se transforma la campaña operativa S4 en campaña de investigación.


**Hallazgo de versión:** el paquete de revisión S5 enlazado en la discusión no está en el árbol main90a3135. Su README sí se recupera íntegro en el pin2c7f545 citado originalmente. La nueva ruta conserva ese enlace inmutable y no inventa una copia vigente. La segunda tanda debe registrar también dependencias de commits anteriores, no sólo archivos del head.


## Incorporación de la primera tanda de lectura — 12 octubre 2026

Iván autoriza ejecutar la ruta UC-21→objetivos→Challenges→DDS→campañas→resultados. Las adiciones descritas aquí se incorporan conservando todos los bytes previos y vínculos de las fuentes. La terminología de lectura remite a sus propietarios: Challenge, escenario base, escenario de evaluación/perfil tecnológico y campañas/operaciones mantienen sus contextos. No se renombra un archivo, se modifica un contrato o se ejecuta una campaña.

La ficha de esta tanda aplicada se retira de la cola activa; sus textos completos están en la [versión de preparación](https://github.com/dakleyer/structural-awareness-contributions/blob/ccf0d4b897eb56498de8fd64d97bf94af496e614/architectural-contributions/ecosystem-positioning/README_VNext.md). El plan de las tandas 2–6 sigue vigente: inventario de dependencias/versiones, agrupación con unidad explícita, informes de campaña y conciliación. La entrada de Issue se actualiza después de verificar las fuentes publicadas. Sus enlaces de envío se conservan.


## Primera tanda publicada; entrada externa pendiente de acceso — 12 octubre 2026

Publicados [objetivos y Challenges de UC-21](https://github.com/dakleyer/use-cases/blob/708faa56d4a664ba1617562c0453d54947528fc2/contributions/when-controls-work-system-fails/README.md) y [lectura DDS, instrumentos y reportes existentes](https://github.com/dakleyer/structural-awareness-contributions/blob/63f39526fb8a51ca81ea61bf2084a4ae789b74ee/research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md#11-reader-route-from-cases-to-studies-and-results). Tres fuentes reciben sólo adiciones; ocho VNext registran plan, semántica y aplicación. Se comprobaron bytes inversos y conservación de cada URL previa. Ningún archivo, campaña, resultado o programa se movió, borró o reescribió.

La edición de la Issue21 fue autorizada e intentada, pero la integración devuelve403 Resource not accessible by integration. El navegador tampoco pudo inicializarse. El [README VNext de UC-21](https://github.com/dakleyer/use-cases/blob/when-controls-work-system-fails-v0.9.3/contributions/when-controls-work-system-fails/README_VNext.md) ofrece el texto exacto antes/después para incorporar con una cuenta con permiso. El cuerpo de la Issue no cambió. Fuente/documents listos no equivale a entrada FG-TIDA actualizada.

Próximo trabajo del plan: inventario por rutas/commits y enlace de todos los ejercicios, versiones, reducciones/extensiones y registros con unidad y propietario explícitos. El corte incluye2.200blobs enContributions y77enla rama delcaso, además de dependencias históricas como el paquete S5pin2c7f545. La tabla de13estudios es sólo una entrada de catálogo. No se declara conciliación final ni ausencia previa de huérfanos por esta tanda.


## Tanda 2 — inventario de rutas, versiones y dependencias · 12 octubre 2026

**Revisión realizada por Codex, mismo asistente.** Iván confirma que «no cambiar nada» significa conservar la información: autoriza continuar las ayudas de navegación, sin borrar contenido. El UC-21 en PDF y su entrada pública quedan para el final. La ruta de trabajo sigue UC-21 → objetivos → Challenges → DDS → campañas → resultados.

Se obtuvieron los árboles completos y los bytes de los cortes Contributions `af344bd93d8e0ae0e9912dbc08055ded3b25cd25` (2.200 archivos) y rama UC-21 `aafc9a49346a7b2030563d3b8c1bde51de3c6446` (77 archivos). Cada uno de los 2.277 blobs se cotejó contra su identidad Git. Se extrajeron enlaces Markdown de las 967 páginas de Contributions y las 38 de la rama del caso; el análisis distingue documentos actuales, VNext y archivos preservados. Las rutas explícitas y fragmentos examinados en los Markdown actuales resolvieron; no se extiende ese resultado a todos los enlaces web, comandos o formatos de manifiesto.

La lectura humana detecta 19 documentos actuales sin enlace Markdown entrante: dos documentos del diagnóstico, un perfil FG-TIDA, cuatro guías de la segunda serie, tres guías/recapitulaciones compartidas y nueve explicaciones de coste/tipos. Las nueve últimas ya están referidas por los registros JSON; falta acceso directo para el lector. Se añaden tres accesos desde el índice DDS y dieciséis desde el índice de extensiones. La modificación es navegación, no una nueva prueba científica.

Los trece CURRENT_STUDY_RECORD conservan su pregunta y Stage A/Simplified. Se comprobaron 186 referencias de archivo explícitas dentro de esos registros, con cero ausentes. Se verificaron 173 bindings SHA-256 de los mapas `files` de FREEZE/MANIFEST en extensiones, sin divergencias en ese alcance, y los cinco blobs del instrumento diagnóstico v0.2 coinciden con su freeze. El perfil FG-TIDA v0.2 consume expresamente el diagnóstico v0.1: se explica esa relación, sin reemplazar su dependencia por v0.2 o v0.3.

La custodia de 92 copias al pin409bfa9 sigue identificando su origen auténtico. En el receptor actual, 70 permanecen idénticas y 22 evolucionaron: 16 documentos y seis revisiones. Se cotejaron las diferencias documentales: lectura A/B/C, sucesores coste/tipos y aclaraciones de resultados, sin convertir las copias en campañas independientes. Las 16 fuentes correspondientes en feasibility mantienen sus blobs originales. Las seis VNext tienen evolución propia; no se abre otro expediente ni se declara independencia por duplicación.

Se verificaron los árboles de 39 referencias históricas de estos dos repositorios, recuperando cada destino citado por Markdown actual. Incluyen el envío UC-21 aec08fb5, la custodia409bfa9 y el paquete S5 en2c7f545, ausente del main actual. La existencia y ubicación del paquete S5 están comprobadas; su ZIP no se ejecutó aquí. Los enlaces externos de otros propietarios mantienen sus versiones y quedan para la revisión de las relaciones materiales, sin asimilarlos a archivos del head.

**Prioridad Primera; impacto Alto; riesgo Bajo para estas adiciones; esfuerzo Medio.** Beneficio: el lector llega a guías, evidencia y versiones sin depender de claves JSON o de adivinar carpetas. Riesgo concreto: confundir un documento actualizado con el input de un run; se conserva el pin/freeze y se explica la distinción. Coste: lectura de los materiales identificados, cotejo de destinos y mantenimiento de tres pequeñas adiciones. La auditoría de identidad no cierra las pasadas científicas ni las tandas 3–6.

El [plan común](https://github.com/dakleyer/structural-awareness-contributions/blob/main/architectural-contributions/ecosystem-positioning/README_VNext.md) sigue fijando el orden. No se reubica, renombra o elimina un archivo; el contenido previo se conserva byte por byte. Los before/after completos se registran en las VNext propietarias antes de incorporar las adiciones. La ficha aplicada se retira de la cola activa y permanece en Git history.

### Inventario completo por ámbito y ruta de lectura

Los grupos siguientes cubren los 2.277 archivos sin exclusiones por extensión. La carpeta permite consultar cada miembro; la función y autoridad del material las conserva su propietario. Los recuentos fijan este corte, no una auditoría de cada resultado.

| Ámbito | Archivos | Lectura y tratamiento |
|---|---:|---|
| corpus: [(root)](https://github.com/dakleyer/structural-awareness-contributions/tree/af344bd93d8e0ae0e9912dbc08055ded3b25cd25/) | 12 | Presentación y controles del repositorio; no otro corpus técnico. |
| corpus: [.github](https://github.com/dakleyer/structural-awareness-contributions/tree/af344bd93d8e0ae0e9912dbc08055ded3b25cd25/.github) | 9 | Automatización y plantillas; preservar código/configuración. |
| corpus: [applied-research](https://github.com/dakleyer/structural-awareness-contributions/tree/af344bd93d8e0ae0e9912dbc08055ded3b25cd25/applied-research) | 1 | Trabajo aplicado, con su alcance propio. |
| corpus: [architectural-contributions](https://github.com/dakleyer/structural-awareness-contributions/tree/af344bd93d8e0ae0e9912dbc08055ded3b25cd25/architectural-contributions) | 36 | EP: explicación, gradiente, documentos de apoyo y VNext. |
| corpus: [governance](https://github.com/dakleyer/structural-awareness-contributions/tree/af344bd93d8e0ae0e9912dbc08055ded3b25cd25/governance) | 382 | Procedimientos, revisión e historia auténtica; no nuevas autoridades científicas. |
| corpus: [presentations](https://github.com/dakleyer/structural-awareness-contributions/tree/af344bd93d8e0ae0e9912dbc08055ded3b25cd25/presentations) | 8 | Presentaciones/binaries preservados en su versión. |
| corpus: [research](https://github.com/dakleyer/structural-awareness-contributions/tree/af344bd93d8e0ae0e9912dbc08055ded3b25cd25/research) | 1699 | EA, RA y trabajo transversal, según sus índices propietarios. |
| corpus: [scripts](https://github.com/dakleyer/structural-awareness-contributions/tree/af344bd93d8e0ae0e9912dbc08055ded3b25cd25/scripts) | 7 | Herramientas de mantenimiento, no campañas. |
| corpus: [standards](https://github.com/dakleyer/structural-awareness-contributions/tree/af344bd93d8e0ae0e9912dbc08055ded3b25cd25/standards) | 19 | MSCA y sus fuentes/revisiones. |
| corpus: [submissions](https://github.com/dakleyer/structural-awareness-contributions/tree/af344bd93d8e0ae0e9912dbc08055ded3b25cd25/submissions) | 27 | Paquetes y registros de envío; conservar su época. |
| case: [(root)](https://github.com/dakleyer/use-cases/tree/aafc9a49346a7b2030563d3b8c1bde51de3c6446/) | 2 | Presentación y controles del repositorio; no otro corpus técnico. |
| case: [.github](https://github.com/dakleyer/use-cases/tree/aafc9a49346a7b2030563d3b8c1bde51de3c6446/.github) | 2 | Automatización y plantillas; preservar código/configuración. |
| case: [contributions](https://github.com/dakleyer/use-cases/tree/aafc9a49346a7b2030563d3b8c1bde51de3c6446/contributions) | 54 | Paquete UC-21, original y lector vigente diferenciados. |
| case: [use-case-register](https://github.com/dakleyer/use-cases/tree/aafc9a49346a7b2030563d3b8c1bde51de3c6446/use-case-register) | 19 | Infraestructura de registro, schema/ejemplos; no otro ejercicio UC-21. |

La carpeta research contiene1.690 archivos EA,6 RA y3 de structural-awareness. Dentro de EA, extensiones tiene584 archivos con los21 grupos de ubicación del índice existente. En la rama del caso,54 pertenecen al paquete UC-21 y23 a raíz/automatización/registro. Las hojas adicionales ya acordadas y la historia se conservan; no se crea un nivel canónico nuevo.


## Estado publicado de la tanda 2 — adiciones pendientes de incorporación

La auditoría de inventario y los pares literales están publicados el12octubre2026. La comprobación abarca los2.277blobs del corte, rutas Markdown y las dependencias especificadas en esta entrada. Las tres ayudas de navegación están preparadas; todavía no se han añadido a los lectores originales.

La revisión automática rechazó el commit de incorporación porque interpreta la restricción anterior como permiso exclusivo para VNext. Iván aclaró en esta conversación que conservar significa no borrar información; se solicitó confirmar por nombre las tres adiciones a DDS_CANONICAL_METHOD_INDEX_v0.1.md, extensions/README.md y README UC-21. Mientras llega esa decisión, los originales mantienen sus blobs y los pares siguen pendientes, sin marcarse aplicados. El PDF y la entrada externa quedan para el final. La revisión documental y las siguientes lecturas pueden continuar.


## Tanda 2 aplicada — decisión concreta de Iván, 12 octubre 2026

Iván responde «Adelante, muy bien» a la solicitud que identifica las tres adiciones a DDS_CANONICAL_METHOD_INDEX_v0.1.md, extensions/README.md y README UC-21. Se incorporan exactamente esos bloques y se conserva cada byte anterior de las fuentes. Esta decisión resuelve el bloqueo registrado antes; el PDF y la entrada externa siguen para el final.

Se retiran únicamente las fichas literales de esas adiciones ya incorporadas. Sus pares completos siguen en la edición de preparación publicada: https://github.com/dakleyer/structural-awareness-contributions/blob/b8729701ff0303363d48fe63a629587d4b12a6e2/architectural-contributions/ecosystem-positioning/README_VNext.md. Auditoría, explicaciones, instrucciones y propuestas anteriores abiertas permanecen. Cero archivos creados, eliminados, movidos o renombrados; código, resultados, fuentes congeladas y manifiestos íntegros. Continúa la tanda 3 sobre objetivos, Challenges y escenarios/ejercicios, dentro de las VNext actuales.


## Tanda 3 — objetivos, Challenges y escenarios de evaluación · 12 octubre 2026

**Revisión realizada por Codex, mismo asistente.** Iván autoriza las tres adiciones concretas de la tanda2 y pide preparar y continuar la siguiente. Esas adiciones ya están publicadas en Contributions `2ff085688de77938aeaa5a3c0e7edbb607247d58` y la rama UC-21 `285ca77fc4cc5d69f3ea78aeda820777c647d0da`, con todos los bytes anteriores de las fuentes conservados. El PDF y la entrada pública se reservan para el final. Esta tanda publica revisión y cuatro propuestas; su incorporación requiere el GO de esta tanda.

Se cotejaron los cinco objetivos reunidos en README/USE_CASE, las 37 condiciones de los planes del caso, los núcleos/admisión X1–X7 de Annex X, selección de HC/HR/HS/H1–H6, las condiciones de recurrencia y los nueve perfiles T01–T09. Las lecturas de escenarios y perfiles se centraron en problema, plan, variantes, comparadores y fuentes/versiones relevantes al itinerario; no se declara una nueva auditoría completa de cada apéndice histórico. Se contrastaron los trece registros actuales por su propia pregunta/configuración/closure, y el README externo S5 al pin a9eca743df5a5c1fbef5dc6f792ea08f8add29e0, blob4b0d2a673c8ee945bd6c52248390a3c595b9285a. No se ejecutaron productos, simuladores o experimentos.

**Qué se sostiene.** La línea común es la decisión receptora con evidencia, autoridad, tiempo, capacidad y efecto. Las seis familias mantienen mecanismos diferentes: síntesis, composición de recurso compartido, misión/fuentes, hallazgo versus autoridad, validez al actuar y proposición de derechos. Sus 37 gates, nueve perfiles y27posiciones documentales no son37/9/27resultados ejecutados. La nueva lectura «Challenge» organiza las familias y «escenario de evaluación» relaciona tecnología/configuración con condiciones; se conservan S1–S6, escenarios base y los nombres existentes.

**Qué hay que conciliar.** El índice baseline abre00H v0.2, mientras v0.5 y el S4 del paquete desarrollan el núcleo de sobrealcance/pérdida y V19/V20. No es pérdida física de información: ambas versiones existen. Es una ruta inicial incompleta para esa lectura. Se propone un enlace explícito al sucesor y conservación del antecedente, sin reasignar resultados delfreeze. S3 declara su copia obsoleta y remite a00G mantenido; S6 ya es adapter a00J. No se restaura una segunda fuente ni se elimina la historia.

**Comparaciones que no se pueden fusionar.** R0/R1/R2 del caso distingue configuración ordinaria, corrección reforzada y recurrencia con esa misma corrección retenida. El S5 externo declara I0 ordinario, I1 parcialmente defendido que aún falla, e I2 que corrige ramas conocidas del modelo suministrado. Su I2 no es AWS-I2/R2, ni su I1 prueba una corrección previa apta para HR. Los A–D causales, A/B/C/D epistemológicos y Stages DDS son dimensiones separadas. La frontera «blind» del simulador es acceso del candidato a inputs; no acredita un auditor humano independiente.

**Reutilización con sentido.** Los trece registros responden preguntas locales distintas y se declaran Stage A/Simplified completos dentro de esa pregunta. Hay mecanismos útiles para evidencia, identidad, uso temporal, receipts, continuidad y respuesta, pero esos registros no declaran por sí mismos pertenencia a una familia UC-21 ni ejecución de HC/HR/HS para ella. El paso de reutilización especifica mapa de relaciones, failure predicate, control positivo y recursos usando X1–X7 y DDS§4. No se exige volver a ejecutar una batería universal ni se suman denominadores heterogéneos.

**Criterio estratégico.** Cuatro adiciones de lectura, Alto impacto esperado/Bajo riesgo/Medio esfuerzo. El beneficio es elegir la pregunta, versión y evidencia correcta antes de crear un ejercicio. Riesgo: el lector puede confundir una ruta vigente con una edición ejecutada o heredar conclusiones por parecido; las propuestas identifican la versión, pregunta y contrato. El esfuerzo incluye cotejo de fuentes, enlaces y mantenimiento, además de redacción. No cambian requisitos, gates, umbrales, hipótesis, fuentes congeladas o resultados. Prioridad Primera; ejecutar como una tanda coherente sólo tras GO: baseline00H → guía del caso → DDS selección → preguntas de extensiones.

| Familia | Qué se evalúa | Control positivo que debe sobrevivir | Perfil del paquete | Fuente/versionado |
|---|---|---|---|---|
| S1 / 00E | Síntesis: preservar qualifiers y cerrar con recursos finitos. | Estrategia sustentada y revisión útil. | [T01](https://github.com/dakleyer/use-cases/blob/285ca77fc4cc5d69f3ea78aeda820777c647d0da/contributions/when-controls-work-system-fails/annexes/technology/T01.md), [T02](https://github.com/dakleyer/use-cases/blob/285ca77fc4cc5d69f3ea78aeda820777c647d0da/contributions/when-controls-work-system-fails/annexes/technology/T02.md) | [00E source](https://github.com/dakleyer/structural-awareness-contributions/blob/2ff085688de77938aeaa5a3c0e7edbb607247d58/research/ecosystem-awareness/baseline/00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) |
| S2 / 00F | Composición compatible en el mismo corredor/recurso/tiempo. | Movimiento y acceso de emergencia compatibles. | [T03](https://github.com/dakleyer/use-cases/blob/285ca77fc4cc5d69f3ea78aeda820777c647d0da/contributions/when-controls-work-system-fails/annexes/technology/T03.md), [T04](https://github.com/dakleyer/use-cases/blob/285ca77fc4cc5d69f3ea78aeda820777c647d0da/contributions/when-controls-work-system-fails/annexes/technology/T04.md) | [00F source](https://github.com/dakleyer/structural-awareness-contributions/blob/2ff085688de77938aeaa5a3c0e7edbb607247d58/research/ecosystem-awareness/baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_DRAFT.md) |
| S3 / 00G | Linaje de fuente y autoridad para cambiar la misión. | Cambio genuino y autorizado de misión. | [T05](https://github.com/dakleyer/use-cases/blob/285ca77fc4cc5d69f3ea78aeda820777c647d0da/contributions/when-controls-work-system-fails/annexes/technology/T05.md) | [00G source](https://github.com/dakleyer/structural-awareness-contributions/blob/2ff085688de77938aeaa5a3c0e7edbb607247d58/research/ecosystem-awareness/baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md) |
| S4 / 00H | Evitar sobrealcance y conservar el hallazgo material. | Acción agregada autorizada; casos realmente independientes. | [T06](https://github.com/dakleyer/use-cases/blob/285ca77fc4cc5d69f3ea78aeda820777c647d0da/contributions/when-controls-work-system-fails/annexes/technology/T06.md), [T07](https://github.com/dakleyer/use-cases/blob/285ca77fc4cc5d69f3ea78aeda820777c647d0da/contributions/when-controls-work-system-fails/annexes/technology/T07.md) | [00H source](https://github.com/dakleyer/structural-awareness-contributions/blob/2ff085688de77938aeaa5a3c0e7edbb607247d58/research/ecosystem-awareness/baseline/00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.5_DRAFT.md) |
| S5 / 00I | Base vigente en el uso y binding check→act. | Reparación que sigue justificada. | [T08](https://github.com/dakleyer/use-cases/blob/285ca77fc4cc5d69f3ea78aeda820777c647d0da/contributions/when-controls-work-system-fails/annexes/technology/T08.md) | [00I source](https://github.com/dakleyer/structural-awareness-contributions/blob/2ff085688de77938aeaa5a3c0e7edbb607247d58/research/ecosystem-awareness/baseline/00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_DRAFT.md) |
| S6 / 00J | Soporte de la demanda final de derechos por sujeto/uso. | Transferencia y demanda legítimas. | [T09](https://github.com/dakleyer/use-cases/blob/285ca77fc4cc5d69f3ea78aeda820777c647d0da/contributions/when-controls-work-system-fails/annexes/technology/T09.md) | [00J source](https://github.com/dakleyer/structural-awareness-contributions/blob/2ff085688de77938aeaa5a3c0e7edbb607247d58/research/ecosystem-awareness/baseline/00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md) |


Relación revisada en ambos extremos: [plan EP](https://github.com/dakleyer/structural-awareness-contributions/blob/2ff085688de77938aeaa5a3c0e7edbb607247d58/architectural-contributions/ecosystem-positioning/README_VNext.md), [DDS VNext](https://github.com/dakleyer/structural-awareness-contributions/blob/2ff085688de77938aeaa5a3c0e7edbb607247d58/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md), [baseline VNext](https://github.com/dakleyer/structural-awareness-contributions/blob/2ff085688de77938aeaa5a3c0e7edbb607247d58/research/ecosystem-awareness/baseline/README_VNext.md), [extensiones VNext](https://github.com/dakleyer/structural-awareness-contributions/blob/2ff085688de77938aeaa5a3c0e7edbb607247d58/research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/README_VNext.md) y [caso VNext](https://github.com/dakleyer/use-cases/blob/285ca77fc4cc5d69f3ea78aeda820777c647d0da/contributions/when-controls-work-system-fails/README_VNext.md). Las entradas se atribuyen al mismo asistente; no se inventa consenso ni una revisión independiente.


## Tanda 3 aplicada — GO de Iván, 12 octubre 2026

Iván autoriza continuar después de la entrega de las cuatro propuestas de la tanda3. Se incorporan exactamente sus adiciones a baseline README (sucesor00H), README UC-21 (seis Challenges), DDSIndex (elección del ejercicio) y extensions README (preguntas de trece estudios). Todos los bytes previos de esas cuatro fuentes permanecen íntegros, con sus enlaces. No se modifica otro pasaje ni el PDF.

Las cuatro fichas incorporadas salen de la cola activa; su antes/después completo está en la [preparación publicada](https://github.com/dakleyer/structural-awareness-contributions/blob/db248c134318c8786471eec1ef0ead2248b360a6/architectural-contributions/ecosystem-positioning/README_VNext.md). Auditorías y decisiones anteriores se conservan. Cero archivos nuevos, movidos, renombrados o eliminados y ninguna VNext nueva. Los estudios conservan registros, inputs, resultados, código, freezes y manifiestos. Continúa la tanda4: método, instrumentos, comparadores y oráculo/harness, con propuestas nuevas pendientes del GO correspondiente.


## Tanda 4 — método, instrumentos, comparadores y evidencia · 12 octubre 2026

**Revisión realizada por Codex, mismo asistente.** Iván autoriza la tanda3 y pide preparar la siguiente. Las cuatro adiciones anteriores ya se incorporaron en Contributions `269d60cc478d2756516c631f587efc074e822eed` y la rama UC-21 `5c2a969bfbfc5eb8065537f3fade718e756dcdad`; se conservan los bytes anteriores y sus fichas aplicadas salen de pendientes. Esta tanda publica lectura de contratos y cuatro propuestas nuevas, aún pendientes del GO de la tanda4. PDF y entrada final UC-21 quedan reservados.

### Lo que sostiene la cadena

Se leyeron README/adapter/policy/isolation/broker/trace/bridge R01, registro y resultado v0.9, el freeze de30artefactos, perfil diagnóstico StageA v0.2, perfiles B/C y campos de registro T03. La lectura estática de real_admission y pasajes de verify.py se usa para precisar qué comprueba la admisión; no se ejecutó el harness, código del corpus ni producto. Las dos referencias DAG se examinaron por su dominio declarado y su papel de contraste; no se declara una nueva demostración de corrección del algoritmo.

Stage A contrasta especificaciones con el Challenge; B contrasta una arquitectura con el paquete de especificación congelado; C contrasta una implementación con el Challenge y efectos observados. Los perfiles B/C preservan resultados por requisito, continuidad, negativos/mutations cuando aplican, comparadores y retroalimentación por sucesor. El instrumento común aporta separación de vistas, operaciones/ledgers/traces/integridad; no cambia la referencia sustantiva de la etapa por sí mismo.

R01 separa adapter, broker, gate policy, trace y evaluator. La policy fija criterios y no determina la verdad del mundo; los métodos de referencia no inventan thresholds. El contrato de trazas distingue seal pre-oracle y result seal; el aislamiento exige frontera real del candidato, no sólo quitar campos de un objeto in-process. Para la comparación se fijan acceso, autoridad, recursos, capacidad y tiempo; un control convencional exitoso cuenta. Self-test0.7/freeze0.9 conserva seis vectores de resultados mezclados: dosPASS,tresFAIL,unoINCONCLUSIVE esperados. SELFTEST_PASS significa cumplir esos controles, no seis tecnologías aceptadas.

### Versiones y evidencia comprobadas

Los30bindings Git del freezev0.9 coinciden con el árbol vivo de esta tanda. Instrument0.7 y freeze0.9 son identidades distintas y ambos constan en el registro. C02 R01 y C3 HF evalúan perfiles/predicados propios; el C3 de instrumento y el brazoC3 de otro protocolo tampoco son equivalentes. El diagnóstico StageA v0.2 sigue como audit candidate de su freeze; el checker v0.3 audit candidate es un sucesor separado, no sustitución de los bytes v0.2 ni aceptación retroactiva.

Se consultaron IssueUC-4 y sus diez comentarios públicos el12octubre. La fuente distingue package1.1.1/schema1.0.0 y schema1.1.0-r1; preserva contratos previos. La conversación más reciente ofrece SF-011 al pinv0.1.3 para una futura revisión de adapter y dice que no admite campaña/run. Esta lectura no identifica aceptación de nuestro puente R01. El perfil consultado mantieneR01-BRIDGE-DRAFT y su esquema/semántica/revisión/capacidades siguen siendo dimensiones distintas. No se enviaron mensajes ni se importó elZIP de esquema.

### Hallazgo de admisión y límite preciso

real_admission.py valida flags/status, números, modos de aislamiento y presencia de referencias. Su `_present` comprueba valor distinto deNone/stringvacío/listavacía; no resuelve un commit/hash ni autentica el archivo o la revisión. verify.py construye hashes ficticios y labels de review en el control sintético admitido. Ese control es coherente con una prueba de instrumento, pero no demuestra la evidencia de una campaña real. La propuesta pide que la guía conecte los campos declarados con los artefactos y reviews verificables. No cambia el validador congelado ni afirma que esta lectura ejecutó un falso PASS.

### Adecuación y prioridad

El diseño general mantiene referencias y ownership coherentes. Dos mejoras de lectura son prioritarias: abrir los contratos en secuencia práctica y conectar el diseño antiguo del bridge con los perfiles DDS publicados. Dos complementos aclaran selección de instrumento y evidencia que respalda la admisión. Cuatro adiciones, Alto impacto esperado/Bajo riesgo/Medio esfuerzo; el beneficio es seleccionar y preparar correctamente el estudio. Riesgo concreto: confundir calibration, declaración, conformance o efecto; los textos identifican su objeto y artefacto. No alteran policy, thresholds, código, resultados o freezes. Orden: guía oracle→selección DDS→bridge→evidencia adapter, como una tanda de enlaces conjunta.


La relación se registra en ambos extremos: [plan EP](https://github.com/dakleyer/structural-awareness-contributions/blob/269d60cc478d2756516c631f587efc074e822eed/architectural-contributions/ecosystem-positioning/README_VNext.md), [DDS VNext](https://github.com/dakleyer/structural-awareness-contributions/blob/269d60cc478d2756516c631f587efc074e822eed/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md), [oracle VNext](https://github.com/dakleyer/structural-awareness-contributions/blob/269d60cc478d2756516c631f587efc074e822eed/research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/README_VNext.md), [UC4 bridge VNext](https://github.com/dakleyer/structural-awareness-contributions/blob/269d60cc478d2756516c631f587efc074e822eed/research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/UC4_INTEROPERABILITY_PROFILE_VNext.md) y [caso VNext](https://github.com/dakleyer/use-cases/blob/5c2a969bfbfc5eb8065537f3fade718e756dcdad/contributions/when-controls-work-system-fails/README_VNext.md). Se conservan desacuerdos/propuestas anteriores; estas entradas corresponden al mismo asistente.


## Tanda 4 aplicada y publicación en main — decisión de Iván, 12 octubre 2026

Iván autoriza continuar después de la tanda4 y pide que todas las tandas aprobadas estén en main. Se incorporan exactamente las cuatro adiciones a DDSIndex, oracle README, UC4 bridge y adapter guide. Sus bytes anteriores y enlaces permanecen íntegros. Las cuatro fichas incorporadas salen de pendientes; los pares completos quedan en la [preparación publicada](https://github.com/dakleyer/structural-awareness-contributions/blob/bb432e8a9e2809612d2b721b3660974362c34879/architectural-contributions/ecosystem-positioning/README_VNext.md). Se conservan auditorías y otras decisiones abiertas.

Contributions ya contiene en main las tandas1–3. UC-21 se publica ahora en main de use-cases con sus54archivos existentes: fuentes, anexos, assets, fixtures y las seis VNext del paquete. La rama anterior permanece como historia. Los23archivos preexistentes de main se conservan; el README raíz recibe sólo un enlace añadido. No se altera un código, dato, manifiesto, resultado o PDF, ni se borra/mueve un archivo. Las revisiones siguientes de UC-21 usan main. Continúa tanda5: campañas e informes, con candidatos nuevos sujetos a su propioGO.


## Tanda 5 — campañas, estudios e informes · 12 octubre 2026

**Revisión realizada por Codex, mismo asistente.** Iván autoriza la tanda4 y pide que todas las tandas aprobadas estén en main. Contributions `1897ed9424f58b95a10f2839c8e5b9f7bf741935` incorpora la4; use-cases main `d4fad875d12c1542fff8236ec484d68c6e641327` publica los54archivos UC-21 ya existentes en su rama y una entrada raíz añadida conservando los23archivos previos. Se reutilizan las seis VNext del paquete: ningún expediente nuevo. Continúa este trabajo en main de ambos repositorios. La rama anterior queda como historia. Esta tanda publica revisión y cuatro candidatos nuevos; no los aplica. PDF y entradaFG-TIDA siguen al final.

### Relación de pregunta, registro, ejecución y retorno

Se cotejaron los13CURRENT_STUDY_RECORD y su evidence successor con catalogue/reportes; las47fuentes materiales seleccionadas conservan sus blobs en el head. Se leyeron cierres, scope, resultados y pasajes de accounting de los reportes para contrastar unidades/epochs; no se declara otra auditoría completa de todos los anexos/código ni se rerun ningún experimento. En los13 registros coinciden case count y ambas fraccionesType1/Type2 con la evidencia sucesora. El conjunto descriptivo contiene162operaciones/casos:122 del primercohorte y40 del segundo. No es una tasa común ni162observaciones independientes de una misma tecnología.

El linaje distingue resultado original, sucesor coste/tipos de nueve perfiles y repair successor de trece. Se preservan26controles originales y40controles de reparación/positivos, elegidos tras conocer defectos. Un replay no duplica la muestra. Los antiguos párrafos no puntuados pertenecen a su versión; los nuevos diagnósticos tienen su registro, inputs yadmisiónM propios. RawP no se fuerza aType2 yØ no se fuerza aType1: el SQL conserva unP fuera deType2 yHEW tiene9Ø sin convertirlas en9Type1.

### Comparaciones y trabajos separados

Las fuentes HF conservan éxitos convencionales y límites: strong-native8/8 frente a7/8native+EA; cachedlineage EA8/10 frente a9/10revalidación; Casbin-polling mejora con recarga convencional tick15 frente a17EA. Los rapports de access-check para native/model-receiver declaran cero model requests/episodes y bloqueo antes de ejecución. No se hereda ejecución de modelos desde los nombres de directorio. El botv0.6 conserva30casos×10arms=300trazas sintéticas y7efectos known-denied del comparatorstrong-assurance frente a8EA-meta-local; no se convierte en aceptación del paquete StageAv0.3, que registra blind-reader/mutations pendientes.

Los lotes R123(480redes), socialcontinuo(960) ydynamicreview(1056) se leen por sus protocolos propios: redes y receiver/checkpoint records no son muestras deLLM. En esos lotes no se ejecutó un brazoEA; se conservan revalidación convencional y pendientes de admisión/continuidad. El00I-STATEFUL aporta efecto/recovery local por contrato separado;00L combina trazas en papel, evidencia simbólica y correcciones. No se crea una campaña por fichero, repetición o réplica.

### Inconsistencia material encontrada

00K-A04 anuncia379 al principio y conserva en§6 un bloque101+27=128 presentado como expected regression contract. El runner actual fija42+58+49+76+47+74=346core y10+11+12=33supplemental,379total; el router coincide. Se propone una aclaración vigente al final y enlace directo desde DDS a ella. Los números anteriores, código, historial, resultados adversos yfalsifiers permanecen. No se ejecutaron los379tests aquí ni se los usa como score científico.

### Prioridad y siguientes pasos

Cuatro candidatos de impactoAlto/riesgoBajo/esfuerzoMedio: primero00Kconteo, luego linaje de estudios, mapa de informes DDS ycomparaciones HF. El beneficio es reconocer el trabajo ya ejecutado y qué conclusión puede usarse. Riesgos concretos: duplicar cohortes, mezclar unidades/versiones o asociar un pendingaunresult; las adiciones enlazan el registro eidentifican alcance. No cambian thresholds, datos, hipótesis o experimentos. PendingGOtanda5. Después corresponde conciliación de navegación; esta tanda no equivale al cierre de las cinco/sexta pasadas científicas de todo el corpus.


Revisión cruzada: [plan EP](https://github.com/dakleyer/structural-awareness-contributions/blob/1897ed9424f58b95a10f2839c8e5b9f7bf741935/architectural-contributions/ecosystem-positioning/README_VNext.md), [DDS VNext](https://github.com/dakleyer/structural-awareness-contributions/blob/1897ed9424f58b95a10f2839c8e5b9f7bf741935/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md), [extensiones VNext](https://github.com/dakleyer/structural-awareness-contributions/blob/1897ed9424f58b95a10f2839c8e5b9f7bf741935/research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/README_VNext.md), [UC-21 VNext en main](https://github.com/dakleyer/use-cases/blob/d4fad875d12c1542fff8236ec484d68c6e641327/contributions/when-controls-work-system-fails/README_VNext.md). Cada registro conserva su propietario; estas notas son del mismo asistente.


## Revisión histórica a fondo de 00K: 128 →134 →379 — 12 octubre 2026

**Instrucción de Iván:** «revisa a fondo qué pasó, no tomes decisiones apresuradas». Auditoría realizada por Codex, mismo asistente. Se revisaron las cuatro versiones Git de00K-A04, ocho del runner, historial de router/workflow/manifest, patches ylogs de CI. El informe canónico sigue con blob55259d1863e062e02f40d0bf50e91b50788c7e4a; ningún número, fixture, resultado o umbral se modificó. No se lanzó ni repitió una campaña. La CI reciente consultada ya había sido generada por el workflow existente.

### Qué ocurrió, con versión y evidencia

| Estado / cambio | Evidencia comprobada | Interpretación |
|---|---|---|
| 25 septiembre05:40UTC, informe inicial5a3d49f | Intro/tablas/§6 dan101+27=128. [CI36099824950](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36099824950), headf66cf2a,10jobsSUCCESS ylogaggregate128/128. | El128 es un resultado histórico real y coherente con ese contrato, no una cifra arbitraria. |
| 05:47UTC, runner181fa2d | Cross-scenario pasa6→12:101+33=134. [CI36100046965](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36100046965), head138fab3,10jobsSUCCESS ylog134/134. | Cambia el conjunto registrado; su resultado no reemplaza el128 anterior. |
| 06:18–07:33UTC | Runner progresa163→208→242→289→322→379 al cambiarP1–P6. Último runner894173d:346core+33supplemental. | Hay más controles y también cambios de diseño/aislamiento;379−128 no representa251experimentos independientes añadidos a una muestra idéntica. |
| 07:38UTC, informe7b42231 | [Patch exacto](https://github.com/dakleyer/structural-awareness-contributions/commit/7b422314e170c7da910ba3ac995e561239d31466) actualizaintro/coretables/totals a379; deja§6con128 yuna fila cross-scenario aún6. | Aquí se identifica la actualización documental parcial. |
| 07:42UTC, CI379 | [CI36108965548](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36108965548), head948b493,10jobsSUCCESS. Log:42+58+49+76+47+74=346 y10+11+12=33;379/379. | La ejecución del nuevo conjunto está respaldada porlogs, no sólo por el título del informe. |
| 07:46 y08:30UTC | 3a42eb1 añadeCI;78089c7 corrige la fila6→12 yA05→A06. Ningúnpatch cambia el bloque§6. | El desfase128 persiste en el documento hasta elheadconsultado. |
| CI actual delhead eee0a74 | [CI38283402660](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/38283402660):13jobsSUCCESS yaggregate379/379. Hay meta-checks y3replaysP5 separados. | No sumar esos replays/meta-checks a379 ni llamarlos casos científicos nuevos. |

### Qué cambió en las pruebas y qué se preservó

El manifestactual declara corrección deconfoundsP1(source/recordclass), matched-prefixP2, eliminación deHOLDmarkerconfoundP3, refinamientoP4(full lineage no necesaria conpermitPDP/capability válido), exhaustivebasisP5 ydependencia transitivaP6. No es un simple cambio deetiqueta o contador: esos cambios afectan qué pregunta y controles sostienen cada argumento. Una CI verde acredita el código/expectativas delcommit, no necesidad universal ni evaluación deproducto.

Se comprobaron contra sus pins los seis archivos de00K-HISTORICAL A1–A3: todos losblobs coinciden exactamente con las fuentes originales348edcb/8af3969/465c892. El archivo conserva32assertions devariantes diferentes, excluidas del379. Las ejecuciones128 y134 siguen identificadas por sus propios commits/logs. No se encontró aquí evidencia depérdida deesosarchivos/resultados; tampoco se afirma una prueba exhaustiva de toda la teoría por este cotejo.

### Decisión y propuesta vigente

No reemplazar128 por379 sin contexto. La candidata deconteo de tanda5 queda refinada como adición histórica conpins/CI yreferencias defixtures. Conserva la propuesta anterior como historia; esta variante es la referencia activa para la futura decisión. ImpactoAlto/riesgoBajo/esfuerzoMedio, pendingGOdeIván. Elantes sigue siendo literal delmismo blob; el índiceDDS ylos otros tres candidatos continúan compatibles con elanchor previsto. Ningúncambio canónico se incorpora por esta auditoría.


La variante literal y el seguimiento de las ejecuciones están en la [única VNext propietaria](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/fixtures/00K-SUITE/README_VNext.md). Las cuatro propuestas de tanda5 siguen pendientes; esta comprobación no cambia sus fuentes.


## Tanda 5 aplicada — autorización completa de Iván, 12 octubre 2026

Se incorporaron las cuatro adiciones aprobadas: historia de los conteos 00K, linaje de los trece estudios, mapa de informes DDS y comparaciones HF. La versión de 00K incluye los tres estados 128/134/379 comprobados en Git y CI. Todos los bytes anteriores de las cuatro fuentes permanecen como prefijo exacto. Las fichas incorporadas salen de pendientes; auditorías y evidencia permanecen. La autorización de hoy comprende también las propuestas literales anteriores que sigan vigentes; se están conciliando por fuente y dependencias. No se lanzó una campaña.


## Aplicación completa autorizada — 12 octubre 2026

Iván acepta y autoriza incorporar las propuestas pendientes concretas. Se cotejan los viejos con main y se aplica exclusivamente cada par vigente; las auditorías permanecen. Las fichas incorporadas salen de pendientes, con su predecessor Git identificable.

| Cambio | Finalidad | Fuente aplicada | Estado |
|---|---|---|---|
| 71 | Aclaración conjunta de arquitectura, evidencia y posturas al final de EP | architectural-contributions/ecosystem-positioning/README.md | Aplicado |


### Conciliación de la aplicación

RA y Operation comparten la lectura A/B/C/D: B conserva soporte/reserva evaluable, C una vía fundada aún no caracterizada y D una barrera efectiva.01C/Composition conservan pregunta, scope, versiones y vigencia al reutilizar cartografía; rol contractual y conducta observada permanecen separados. Gradient y Operation usan el mismo perfil escalar/vectorial, conservando alternativas incomparables, empates y ausencia de máximo.01J reconoce UNKNOWN y sólo asigna D cuando existe barrera efectiva; su ejemplo de telemetry ya exigía esa condición. Foundation admite Type1/2 dentro de un scope fijo y mantiene Type0, M, causalidad y resultados positivos convencionales. El checker recibe su corrección en v0.4; los freezes permanecen. No se redistribuye ningún archivo ni se crea otra VNext.

### Líneas sin cambio literal ejecutable

43–45 son tareas para localizar obligaciones/realización, y46–51 perfiles, fidelidad, campañas y evaluación de una realización. Continúan como trabajo de investigación definido por sus fuentes, no como cambios de texto esperando permiso.64/67 están superadas por01K vigente;65/66 resueltas por integración posterior;75 contradice la posterior instrucción de Iván de retirar fichas aplicadas y no tiene viejo vigente: no se restaura la cola retirada. Las propuestas descartadas o históricas no se reejecutan. La revisión científica completa del corpus y sus fuentes no se cierra por esta aplicación.


## Cierre de aplicación autorizada — 12 octubre 2026

**31 cambios de fuente incorporados:** tanda5(4) en [main9fb942](https://github.com/dakleyer/structural-awareness-contributions/commit/9fb9421711521decde6843b04914a143a1f04c35), anteriores(26) en [main00ea317](https://github.com/dakleyer/structural-awareness-contributions/commit/00ea3174c10a7e7cad84905d5642aa74eba35b18), ysnapshotUC-21(1) en [use-cases maine9efbda](https://github.com/dakleyer/use-cases/commit/e9efbda5e0cc002793a4df82484a6b3f47a79976). Se verificaron los10+36+7archivos de esas publicaciones por lectura completa de vuelta. Los cambios16/22/23 tienen dos sucesores de trabajo;74 tienechecker/testv0.4. Los tres originales permanecen con sus blobs exactos; los resultados/manifest/binaries se preservan. Se verificó la sustitución inversa del párrafoUC-21 y la identidad de los70otrosblobs de use-cases.

No quedan pares actuales incorporables por aplicar.43–51 requieren concretar un perfil, contrato o investigación y no representan texto aprobado abandonado.3/4/5 fueron reformulados en71;64/67 superados;65/66 resueltos;75 superado por la instrucción posterior de retirar fichas aplicadas. Las tablasEO originales de UC-21 quedan históricas porque la guía de cincoobjetivos y el formulario existente ya resolvieron esa navegación; no se agrega una segunda1.1. Las fichas aplicadas y la repetición de59 se retiran de la cola, manteniendo auditorías, atribución, desacuerdos y predecessor Git.

La entradaFG-TIDA conserva el envío congelado. Su propuesta de enlace queda preparada en UC-21 VNext; la integración GitHub devuelve403para modificar esa Issue. PDF y futuros experimentos no se sustituyen por esta publicación. La navegación ya incorporada funciona en main de ambos repositorios y apunta a los expedientes propietarios.


## Tanda 6 — conciliación de navegación UC-21 / DDS · 12 octubre 2026

Revisión por Codex, mismo asistente. Iván pide preparar y continuar la siguiente tanda. Corte: Contributions `582a1b87b18c651beff8dd8a8f2d590cf50aace6` y use-cases main `e9efbda5e0cc002793a4df82484a6b3f47a79976`. Las 31 incorporaciones anteriores están publicadas; esta tanda prepara seis ajustes nuevos, sin incorporarlos a las fuentes. Es la sexta tanda del plan de navegación, no la sexta auditoría científica del corpus.

### Qué se mantiene y qué necesita ajuste

La ruta es **UC-21 → objetivos → Challenges → DDS → campañas → resultados**. El caso conserva sus preguntas y afirmaciones; DDS, el método; cada estudio, su contrato y evidencia. Se recorrieron dos entradas. La Issue 21 conserva el envío `aec08fb5`; main contiene las ayudas de lectura añadidas después. El envío mantiene una lectura íntegra de su edición. Los comentarios S5 y S4 enlazan DDS en el commit `2c7f545`; esa referencia histórica no lleva al índice actual. La adición al cuerpo de la Issue sigue preparada por separado, con el permiso de edición pendiente de resolver.

El árbol de ambos repositorios contiene 2.281 archivos Git. Se autentican 2.218 textos UTF-8 contra sus blobs, incluidos 1.007 Markdown. El análisis extrae 15.437 relaciones y no detecta destinos o fragmentos faltantes en el subconjunto activo, excluyendo referencias históricas y VNext. Esto verifica navegación; las URLs externas y la verdad científica de las fuentes tienen otras comprobaciones. Además, se cotejaron 186 referencias de estudio y 173 bindings SHA256 congelados seleccionados: todos conservan destino e identidad. Los trece registros mantienen su pregunta, registro, freeze y evidencia sucesora. No se reejecutó una campaña.

Diez enlaces activos apuntan a la rama anterior de UC-21: siete en DDS, uno en la nota S4 de baseline, uno en extensiones y uno en la fuente histórica 00G. Sus destinos y fragmentos se leyeron en el head real `188f319`: existen. El README de esa rama conserva la redacción anterior a la precisión de snapshot incorporada en main. Se propone actualizar nueve enlaces de orientación, conservando sus URI anteriores. El enlace de 00G mantiene su contexto histórico y no se reescribe el escenario. El inventario de 54 archivos sigue correcto, pero el rótulo “maintained package” identifica el antiguo corte `aafc9a`; debe distinguirse de main.

Los 32 Markdown del paquete UC-21 están conectados por sus índices y guías. Los seis Markdown sin entrada activa encontrados fuera de ese paquete corresponden al root, la plantilla de Issue y el software de registro de use-cases. No son documentos abandonados de UC-21. Los assets conservan sus rutas y acceso por carpeta; el inventario no cuenta como una lectura científica de los binarios.

### Nueva relación material UC-4 ↔ UC-21

El [comentario de Iván del 12 de octubre](https://github.com/FG-TIDA/use-cases/issues/21#issuecomment-6127959997), último de los 33 consultados, propone recibir una determinación con sus condiciones, examinar su aplicabilidad, formular un hallazgo acotado y devolver un control candidato a otra prueba. El PASS original conserva su ámbito; una aplicabilidad posterior no establecida no borra ese resultado. Un límite de observación también puede ser una conclusión válida. Sus pasos A–F son la secuencia propuesta, no etapas DDS. EA figura como una posible capa complementaria y el control convencional competente conserva su resultado. No aparece una respuesta posterior en el hilo consultado. La revisión de esta relación queda registrada en el caso, DDS y el puente UC4.

### Seis cambios nuevos propuestos

| ID | Cambio | Impacto esperado | Riesgo | Esfuerzo | Orden |
|---|---|---|---|---|---|
| 77 | Leer UC-21 desde main en las siete rutas DDS | Alto | Bajo | Medio | Primera |
| 78 | Distinguir el inventario histórico de la lectura actual | Alto | Bajo | Bajo | Primera |
| 79 | Llevar la familia S4 vigente a main sin perder su ruta anterior | Alto | Bajo | Bajo | Primera |
| 80 | Conectar la reutilización de los trece estudios con el caso vigente | Alto | Bajo | Bajo | Primera |
| 81 | Dar acceso al checker corregido manteniendo la edición congelada | Alto | Bajo | Medio | Tras 77 |
| 82 | Enlazar el nuevo ciclo bidireccional propuesto UC4–UC21 | Alto | Bajo | Bajo | Tras 78/81 |

Los pares completos están al final de las VNext propietarias: DDS 77/81, UC-21 README 78/82, baseline 79 y extensiones 80. Son seis cambios lógicos, trece pasajes y cuatro fuentes. En copias de análisis se verificaron la sustitución inversa exacta, la conservación de todas las URI HTTP anteriores y diecisiete enlaces actuales nuevos o modificados. **Estado: preparados, pendientes del GO de esta nueva tanda.** La autorización anterior incorporó sus propios pendientes.

### Revisiones en ambos extremos

[Visión conjunta EP](https://github.com/dakleyer/structural-awareness-contributions/blob/main/architectural-contributions/ecosystem-positioning/README_VNext.md) · [DDS](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md) · [baseline](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/README_VNext.md) · [extensiones](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/README_VNext.md) · [puente UC4](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/UC4_INTEROPERABILITY_PROFILE_VNext.md) · [UC-21 README](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/README_VNext.md) · [caso](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/USE_CASE_VNext.md).


## Migración conservadora completada en los repositorios — 12 octubre 2026

Iván autoriza completar la migración y preservar toda la información y sus rutas. Se incorporan los seis cambios77–82 mediante sus trece pasajes exactos, con nueve enlaces de orientación actualizados y sus referencias anteriores conservadas. No se mueve ni renombra ningún archivo. Las fuentes mantienen todo el contenido fuera de esos pasajes; los anexos añadidos son bloques al final.

El cotejo encontró dos archivos históricos del paquete S5 que ya faltaban de main antes de esta tanda: README y ZIP. Ambos vuelven a sus rutas originales con los mismos blobs del commit2c7f545. El ZIP conserva123.884bytes y SHA2569ea1ac54378018e60809f6dff63613fc41d6c0cf53c4ac952345f1e927c51bb8; sus25miembros pasan comprobación CRC, sin ejecutar scripts. La restauración se presenta en la hoja adicional EA, con su edición y finalidad histórica. El paquete v0.1.3 de Steven y sus límites posteriores mantienen su propio registro.

El README UC-21 añade al final acceso a todos los archivos de su paquete, los materiales de envío y los archivos de trabajo del registro. El anexo adicional EA enlaza el soporte compartido, los originales R01 y la historia de revisión. Las tres hojas auxiliares EA/RA/MSCA mantienen su organización; no se crea una colección de índices ni niveles nuevos. El envío aec08fb5, los freezes y los resultados siguen con sus identidades.

La comprobación de cierre compara los inventarios4ebb0c8(1.306archivos),af344bd(2.200) y2c7f545(2.113) con el árbolfinal, incluyendo las dos restauraciones. El criterio es conservar todas las rutas, bytes fuera de las ediciones aprobadas y destinos de enlace, además de acceso por el propietario o su anexo. La navegación de main se completa; no se confunde con terminar el ciclo científico de cinco/sexta pasadas.

La edición de la Issue pública #21 se mantiene separada: la revisión automática rechazó la nueva adición al cuerpo por exigir aprobación literal del texto externo y señalar el bloqueo previo403. La lectura de vuelta comprobó cuerpo, título y estado intactos. El navegador también falló al inicializar sus assets; no se intentó otro medio de escritura. El bloque exacto se publica en la VNext de README UC-21 para una decisión concreta. No hay PDF UC-21 en los árboles actuales de estos dos repositorios; no se fabrica ni sustituye uno como parte de esta migración.


### Comprobación efectiva de conservación y accesibilidad

El árbol final contiene2.206archivos en Contributions y77en use-cases:2.283en total. Comparando rutas, no falta ninguno de los1.306archivos de4ebb0c8, los2.200deaf344bd o los2.113de2c7f545 después de restaurar el README yZIP históricos. No se borra, mueve o renombra una ruta. El ZIP restaurado es el mismo blob y su SHA256 coincide con el registro original.

En los cinco documentos de navegación intervenidos se conservan los2.006destinos de enlace anteriores, con su multiplicidad; se añaden31. Los textos fuera de los13pasajes aprobados coinciden exactamente; los dos bloques auxiliares son adiciones al final. Ningún enlace anterior se retira para ocultar una versión. El análisis final extrae15.515relaciones y encuentra cero destinos o fragments faltantes en los enlaces activos; las URLs de terceros conservan su atribución y pins.

La prueba de acceso desde los lectores existentes, incluyendo exploración de las carpetas explícitamente enlazadas, cubre los2.283archivos. Se diferencia ese acceso del enlace individual en la narración: código compartido, schemas, imágenes, fixtures, controles y versiones históricas permanecen en sus carpetas de origen, con enlaces auxiliares al final de los índices. No se convierten en otra arquitectura ni se fuerza su lectura como un resultado científico nuevo.


## Informe auditable de la reestructuración UC-21 / DDS — 13 octubre 2026

Iván autoriza publicar el [informe completo de la sesión](https://github.com/dakleyer/structural-awareness-contributions/blob/main/governance/review/migration-audit-2026-10-13/Informe_auditable_DDS_y_corpus_sesion_2026-10-13.html) como trazabilidad de los cambios de navegación y de las incorporaciones aprobadas. Reúne 75 commits consultados, 304 rutas y 76 pares literales antes/después, con razones, autores, versiones, restauraciones y comprobaciones de conservación. El HTML se puede descargar y leer sin recursos externos; su [manifiesto SHA-256](https://github.com/dakleyer/structural-awareness-contributions/blob/main/governance/review/migration-audit-2026-10-13/Informe_auditable_DDS_y_corpus_sesion_2026-10-13_MANIFEST.json) identifica el archivo exacto entregado.

El informe documenta las actuaciones del 6 al 12 de octubre, con cortes `9056ed78e3e79c025f253cfbc823ccc0293064a4` (Contributions) y `0d32667ccce1dd3e568459a64a89e83987d92d4e` (use-cases). La publicación parte de `b5d126cc877c7e4c6bb7fe45bfa7173a128a6023` y conserva las incorporaciones posteriores. Es un registro retrospectivo de la reestructuración; el estado de cada investigación se consulta en su expediente vigente. No constituye otra VNext ni otro nivel de README.


## Cierre de entrada UC-21 — 13 octubre 2026

FG-TIDA: índice de casos → Issue #21 → UC-21 → objetivos → Challenges → DDS → campañas/estudios → resultados → siguientes decisiones.

### Presentación de conjunto

UC-21 aporta el caso y sus preguntas: decisión correcta y continuidad legítima; controles existentes eficaces; recurrencia después de corregir R1; mecanismo causal común; y respuesta común suficiente. HC, HR, HS y los contrastes H1–H6 conservan sus protocolos. Las seis familias son Challenges en la guía; sus S1–S6, fuentes 00E–00J y rutas originales permanecen. El escenario DDS aplica una tecnología/configuración bajo condiciones delimitadas.

DDS aporta el método. Sus etapas A/B/C se distinguen por objeto y referencia; las rutas de comparación UC-21 R0/R1/R2 permanecen independientes de esos nombres. Cada estudio enlaza registro, versión, freeze, ejecución, evidencia y conclusión; un catálogo de archivos no sustituye esos resultados.

Hay trabajo real que ya puede recorrerse: la contribución S5 con alcance de modelo corregido, su auditoría preservada y el compañero sintético 00I-STATEFUL; los estudios e informes reutilizables bajo sus propios contratos; y el código CDA v0.1.3 publicado por su autor, todavía sujeto a la revisión que corresponda al experimento seleccionado. Los trece estudios locales no se agregan como si fueran una campaña UC-21.

El seguimiento UC-4/CDA se prepara como colaboración seleccionada por pregunta. Nelson conserva el ciclo experimental UC-4 descrito en su comentario. En paralelo pueden prepararse el Challenge R2, comparadores, contrapruebas y revisión Stage A; ejecutar R2 requiere R1 demostrada y congelada. Diseño abierto, ejecución/verificación independiente y selección posterior de especificaciones se separan. La vacante de verificación sigue abierta; el texto no nombra un nuevo titular.

Flores / Theme #21 mantiene su expediente DDS propio y su estado de preparación. No es la Issue de caso UC-21 pese a compartir el número 21. La raíz enlaza el registro de desarrollo como lectura relacionada, sin atribuir esa campaña al caso.

| ID | Cambio | Impacto | Riesgo | Esfuerzo | Orden | Estado |
|---|---|---|---|---|---|---|
| 83 | Dar a UC-21 una entrada directa y completa desde su raíz | Alto | Bajo | Bajo | Primera | Preparado; no aplicado |
| 84 | Conectar método y arquitectura actuales conservando los cortes anteriores | Alto | Bajo | Bajo | Primera | Preparado; no aplicado |
| 85 | Actualizar las aportaciones S4/CDA y el ciclo opcional UC-4 ↔ UC-21 | Alto | Bajo | Medio | Primera | Preparado; no aplicado |
| 86 | Explicar el siguiente trabajo y quién decide cada cierre | Alto | Bajo | Medio | Primera | Preparado; no aplicado |
| 87 | Dar el mismo recorrido al lector que entra directamente en USE_CASE | Alto | Bajo | Bajo | Primera | Preparado; no aplicado |
| 88 | Conciliar en DDS las condiciones del seguimiento UC-4 / CDA | Alto | Bajo | Medio | Primera | Preparado; no aplicado |
| 89 | Incluir UC-21 en los índices de casos | Alto | Medio | Bajo | Siguiente | Preparado; no aplicado |
| 90 | Poner la presentación mantenida en la entrada pública de UC-21 | Alto | Medio | Bajo | Siguiente | Preparado; no aplicado |
### Orden de incorporación y comprobación final

1. Aprobar y aplicar 83–88 al paquete mantenido y al índice DDS; mantener originales fuera de cada par, enlaces anteriores, anexos, assets, fixtures y versiones. Los destinos nuevos se habilitan juntos: cabeceras 83/87 apuntan al apartado añadido por 86.
2. Incorporar 89 al índice del fork. Para la tabla oficial, entregar el mismo par al mantenedor FG-TIDA o incorporarlo con su acceso autorizado. La fila copia el tema marcado como principal en la presentación; no afirma una asignación nueva.
3. Incorporar 90 al cuerpo de la Issue por su propietario, con GO literal sobre el bloque. Mantener título, estado, labels, campos, casillas, comentarios y enlaces congelados. La petición actual es preparación; no se envía un comentario externo ni se cierra la Issue.
4. Leer desde la tabla oficial y el enlace de la Issue hasta los cinco objetivos, seis Challenges, método DDS, protocolos, registro/freeze/informe y retorno. Probar también entrada directa USE_CASE, ida y vuelta desde DDS y acceso por anexos a soporte y archivos históricos.
5. Comparar árboles y blobs contra el corte previo: ninguna ruta perdida, ningún archivo movido o renombrado; todos los destinos anteriores presentes. Comparar el cuerpo externo completo y revertir en copia cada sustitución para demostrar que fuera de lo acordado no cambia nada. Leer de vuelta todos los archivos aplicados; registrar commit, fecha y estado en las VNext y retirar cada ficha aplicada de pendientes según la instrucción de Iván, preservando auditorías y Git.

El cierre documental se declara al completar ese recorrido y la conservación, incluida la entrada oficial. El cierre de cada investigación lo decide su propio contrato/evidencia: S5 al alcance evidenciado, un seguimiento CDA tras acordar ejecución y R1/R2, y especificaciones tras revisión de resultados. La revisión científica de cinco pasadas y conciliación global no se da por terminada por enlazar la raíz. El PDF UC-21 sigue sin localizarse en los dos árboles; no se incluye un reemplazo ficticio.

Pares y presentación pública completos: [README UC-21 VNext](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/README_VNext.md#cierre-de-entrada-uc-21--13-octubre-2026). Los originales se leen contra sus cortes actuales; no se cambia la jerarquía ni se crea una VNext.


## Direct UC-21 entry in Contributions — 13 October 2026

Ivan selects one maintained research corpus: **FG-TIDA Issue #21 → Contributions → UC-21 research questions → Challenge sources → DDS → registered studies and results**. The fork is a source archive, not another maintained canonical reader entry. New public preparation is written in English.

The prior fork-based changes 83–90 are superseded as a proposed wave and must not be applied as prepared. Their old/proposed text and audit history remain intact. The official-index row may be re-proposed separately if needed; updating a fork index is no longer part of the current route.

Current tree: Contributions `f960f6f5a627993643512b816430a485227f9118`, 2,249 files. DDS, 00E–00J source families, instruments and reports already exist here. The maintained fork still contains the full UC-21 case, twenty annexes, claim/recurrence protocols, assets and templates. This review has not found a complete second copy of that case package in Contributions. Replacing links alone is not a full source migration; no copied corpus or new repository is created to hide that distinction.

The proposed first step reuses the existing DDS Canonical Method Index. It presents the five questions and six current Challenge sources while retaining original source protocols as pinned historical dependencies. The official Issue would then receive the exact primary-link replacement below. This preserves the submitted edition without routing current research through a moving fork branch. A later decision to integrate the entire case would first classify identical sources, unique content and necessary paths in a manifest; no archive or source is deleted or moved by this preparation.

**Order:** incorporate and verify 92, then incorporate 91 at the official Issue with its owner's access and approval of the exact text. Complete source-package consolidation is a separate unresolved decision, not an accomplished migration. The official Issue remains unchanged during preparation; prior 403/automatic-review history is retained without an attempted bypass.

Exact before/after passages are in the [existing DDS VNext](../../research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#direct-uc-21-entry-in-contributions--13-october-2026). No new VNext or source file is created.


## UC-21 annex sources already in Contributions — 13 October 2026

The earlier statement that the twenty annexes were only in the fork was too broad. Their compiled UC-21 files are preserved in that package, but the six failure-family sources and nine technology-profile sources are already in Contributions baseline. Annex H's original causal/refutation and H1–H6 sources are also present in the 29 September document collection and canonical requirements.

All twenty current annex blobs are unchanged since the verified 12 October case main. Eighteen also equal the submitted snapshot; S3 preserves its body below a retirement/source notice, and S6 is an adapter to 00J with its full original text preserved at the submission commit. None is missing from the case inventories. The two public ZIPs do not contain another full annex package.

R, X, N and Evidence still need case-specific reconciliation: existing source material is not an identical complete case compilation. Reuse the existing source owners and carry over only verified unique obligations, rather than creating another twenty-file mirror. The [twenty-item source map](../../research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#uc-21-twenty-annexes--location-and-source-content-reconciliation-13-october-2026) records actual paths, versions and remaining differences. Original sources remain unchanged.


Publication custody: the review was rebased onto concurrent commit 49aa7b9eb00acf27de7b1bbd80b23df14a544902. Its Flores runtime-context additions do not change these two VNext or the baseline and hypothesis source counterparts examined above. The content comparison remains explicitly attached to its stated d06956a cut; no new Flores result is inferred from this annex check.


## Entire fork preservation — 14 October 2026

The [complete file/history reconciliation](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#entire-use-cases-fork--file-and-history-reconciliation-14-october-2026) accounts for all 77 current fork files, 14 additional branch/historical paths and 162 authenticated historical blob versions. The maintained corpus contains the fifteen direct family/technology sources, but **the compiled UC-21 case protocols, adapted artifacts and complete UC-20 branch package are not fully integrated**. The earlier completion statement concerned navigation, not full content import. The owner now requires complete material preservation inside the one Contributions corpus.

Six family SVGs and one AWS JSON are exact existing copies; five family SVGs and three AWS JSON files are case adaptations with actual semantic/namespace differences. S6 was reduced from 46,256 to 3,633 bytes on 3 October; its complete submitted edition remains in history, and its differences from current 00J must be retained. The case manifest does not certify the current expanded package, and one listed USE_CASE digest has no match in authenticated reachable fork history.

Changes 92/91 are reopened for content recovery and source-owner decisions. Preserve their literal pairs; do not treat an approved link edit as complete case transfer. Required order: full case/protocol preservation, family/profile differences, assets/fixture adapters, separately identified UC-20, then the Contributions entry and official UC-21 route. No physical reorganization, new canonical level or source edit is performed here. The detailed audit includes the upstream register/template files and unresolved historical deletion boundaries, rather than silently excluding them.


## Content inside existing files — 14 October 2026

The [literal content review](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#content-within-surviving-files--literal-preservation-review-14-october-2026) checks 2,727 Contributions commits, 5,148 authenticated blobs and 3,625 modification/deletion events at `f16b3ba`. It includes internal rewrites in surviving files, not just the earlier deleted-path inventory. All 162 reachable fork editions are compared with current corpus bytes. Its supporting inventory names all 620 paths with retired text.

Material reconciliations: DDS's old eight-column mapping retains its dimensions and eight family/support rows in current Method Index §8; 01K retains the five old formula expressions. An explicit required-HumanTime-fit condition is absent from its rewritten runtime gate: [CP-01/change93](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/01K_VNext.md#content-preservation-cp-01--restore-the-explicit-human-time-condition) proposes its bounded restoration, with old/current/proposed text and component/oversight dependencies. A deleted 22,330-byte Stage-A G-A01–G-A14 draft differs from the current SA-G00–SA-G14 catalogue; the full former text is now historical audit custody in the existing DDS VNext, not another active specification.

Literal no-match counts are not lost-fact counts and do not prove preservation either. Applied-fiche retirements, corrected status/claims, namespace/URL changes and real omissions are kept distinct. Binary old editions/translation changes retain their source identities. Complete current-tree content preservation remains unconfirmed pending material crosswalks; direct-entry91/92 stay reopened. This publication changes only existing review/priority records.

**EP append-only history:** source changes `6c93994c` and `c2d0d516` replaced the existing Human Intelligence/HID entry/title inside the file on 6 October. They do not meet byte append-only preservation, even where the newer paragraph carries the same idea and adds references. Their old and new passages are retained in the checked Git sources and the literal comparison. Record the source-custody/authorization question rather than retrospectively describing those operations as append-only; no canonical revert is performed.


## Damage control and restoration plan — 14 October 2026

The [detailed plan](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#damage-control-and-restoration-plan--14-october-2026) restores complete case/source custody and applicable current meaning without replaying superseded errors. It covers the162 distinct fork editions, all620 internally edited source paths/8,749 retired units and64 deleted-source events lacking a whole-blob receiver at the earlier cut. These are evidence queues, not proven loss counts or completed semantic reconciliations.

Order: preserve exact editions; reconcile UC-21 objectives/H-R-Evidence/Conventions/run obligations; compare all six family/nine technology editions including full S6; retain figures and explicit fixture adapters; map old/current Stage-A clauses; reconcile HumanTime scheduling consumers; address binary/source-language/history and separate UC-20/support; then reprepare92's maintained route and91's actual official entry. Only the three existing canonical reading levels remain. Historical custody uses the existing boundary as a proposed destination, not a new active repository, README owner or VNext collection. Source adoption requires exact complete old/proposed passages or payloads and a named wave decision. No restoration is applied by this plan publication.


## Second damage-review pass — organization and first findings, 14 October 2026

Iván requests another detailed source-first review, document by document. [Three separate reviewer roles and the complete existing-space queue](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#second-damage-review-pass--separate-source-first-reviewers-14-october-2026) are now recorded. The thirteen assigned primary source units have complete source readings and bounded receiver/section judgements; unassigned sources and unclosed consumers remain visible. No new VNext or canonical source modification.

The first findings narrow earlier loss interpretations: HC/HS and common metrics have active original/corpus receivers; S6’s30 gate cells, controls and measure meanings survive in00J; R0’s rights-record meaning must not be merged with the case route ladder. The real open work concerns complete edition custody, case-to-DDS HR/claim/form mapping, old-alias metric disposition and generic contract transfer. A documented incomplete A01 introduction update predates S6’s reduction.

The [S6 review](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/README_VNext.md#second-source-first-review--s6-t09-and-00j-14-october-2026) and [capacity review](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/01K_VNext.md#second-contract-review--capacity-and-the-change93-alternative-14-october-2026) keep source identity, uncertainty and disagreement intact. Changes94/95 prepare two narrow Medium-impact/Low-risk reader corrections; candidate93 receives an alternative with Medium risk and unclosed consumers. None is applied. Remaining cohorts proceed through the existing owners and three reading levels; seven existing paired review paths are one joint logical comparison per pair, without deleting unique history.


## Internal Contributions history — EP and Requirements, 14 October 2026

The [second damage-review procedure](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#internal-contributions-history-takes-priority--14-october-2026) now gives priority to internal Contributions editions and commits after the case fork; external/fork comparisons are supporting provenance. Reviewer `/root/case_clause_forensics` read the four current units below, all11 Requirements deltas and all18 EP deltas from the29September reference (four same-day context changes,14 strictly after the recorded submitted-package timestamp). The remaining earlier EP changes are authenticated with full diffs but are not all semantically adjudicated.

| Complete current source | Current blob / bytes | Internal identity coverage |
|---|---|---|
| [research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md](https://github.com/dakleyer/structural-awareness-contributions/blob/ca5dd562a9566e69f691a28a7dfbb0b6c69479bb/research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) | `4fe3d69b50fef1e82ba7f889324b70a7f6b1a81c` / 46217 | 12 distinct payloads; current source and declared internal deltas read |
| [research/ecosystem-awareness/baseline/00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md](https://github.com/dakleyer/structural-awareness-contributions/blob/ca5dd562a9566e69f691a28a7dfbb0b6c69479bb/research/ecosystem-awareness/baseline/00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md) | `c0226a1ba9a45976ad0c887dd9afb97b103e6c37` / 47111 | 1 distinct payloads; current source and declared internal deltas read |
| [architectural-contributions/ecosystem-positioning/README.md](https://github.com/dakleyer/structural-awareness-contributions/blob/ca5dd562a9566e69f691a28a7dfbb0b6c69479bb/architectural-contributions/ecosystem-positioning/README.md) | `9767ec8efb7d3a2875866ea3cd22ebc94882e930` / 90992 | 86 distinct payloads; current source and declared internal deltas read |
| [architectural-contributions/ecosystem-positioning/DEVELOPMENT_STRATEGY.md](https://github.com/dakleyer/structural-awareness-contributions/blob/ca5dd562a9566e69f691a28a7dfbb0b6c69479bb/architectural-contributions/ecosystem-positioning/DEVELOPMENT_STRATEGY.md) | `f25aef42574afa9d321b352b3d2b1e1447575556` / 12211 | 1 distinct payloads; current source and declared internal deltas read |

### INT-REQ-01 — Frozen Requirements did not acquire post-fork body edits

**Judgement:** No post-29-September modification in this primary source.

All 12 internal versions were authenticated. Its last body change is96cbc949 on25September, current blob4fe3d69. This stable cut was already the0ca06f hypothesis snapshot. Later working changes were not secretly put into the frozen original.

### INT-REQ-02 — H3 falsification correction must survive any restoration

**Judgement:** Supported correction, not missing old evidence.

6a8fd5f changed the falsifier from material difference to no material difference or disappeared benefit under burden. H3 itself predicts greater hidden residual/false confidence on lossy paths, so the old contrary wording had the wrong direction. All six full hypothesis rows are exact across the12 primary versions. The correction alters falsification logic, not a missing hypothesis.

### INT-REQ-03 — Approved S10 binding lives in a separate working successor

**Judgement:** Versioned addition with documented current approval and preserved freeze.

00ea317 adds successor c0226a1b, with an opening owner-approved #16 note and one S10 addition. Its inherited freeze statements describe the predecessor, as the opening note explains. H1–H6/KPIs and all other rows are unchanged. Current baseline and Document Control route to both. Broad actual adoption by every fixture/interface is not established, and registered studies correctly retain their own freeze.

### INT-EP-01 — Five protected README replacements require their own authorization record

**Judgement:** Actual replacements, with passage-specific contemporaneous GO not established.

After the6October append-only instruction, commits39af310,6c93994,c2d0d516,1aba8cf,64fa9f replace existing protected passages. The record contains their complete old/new blocks and current receivers. Some are sound corrections or reclassification; that does not establish permission. The12October protected SHA and final append approval do not retrospectively authorize these earlier surgeries.

### INT-EP-02 — Insertion is not the same event as replacement

**Judgement:** Exact operation types preserved.

1d24b7b prepends the review note;7150279 appends the strategy route;8a2860a inserts theHCsection;f77668d inserts the research/test paragraph;00ea317 appends the final clarity section. These transactions remove no old lines. Mid-body insertion is not a byte-prefix operation and its placement exception may need documentation, but it is not source deletion. The five replacement commits above are different.

### INT-EP-03 — HIT retirement has an explicit current rejection rationale

**Judgement:** Source correction with historical custody, not blind metric restoration.

The earliest01K38fcb757 defines HIT accounting and HID(W) as queued demand minus available tokens. Internal2816aa1 rewrites that source to importHICT/HICR; protectedREADME39af310 follows. Current01K§16 expressly says Human Intelligence Tokens are not canonical HID units, permits local scheduling points and forbids calling themHID. §§14–15 preserve finite runtime capacity separately. This supports correction of the old metric object; no protected-README GO is inferred. The earlier five-formula preservation claim must retain the specific edition it examined, not encompass every earliest token formula.

### INT-EP-04 — DDS reclassification preserves comparative obligations

**Judgement:** No demonstrated lost matched-resource/negative-result contract in the examined surgery.

1aba8cf renames00D from parallel comparative method to DDS comparator/fairness support. The current complete paragraphs still require matched B0–B3, frozen facts, continuity/failure branches, preregistration, ledger, downstream effects and pending independent comparison.64fa9f corrects Gate to Stage nomenclature; current Method Index distinguishes stage object, evidence mode and source-native testbed stages. These semantic receivers do not establish approval for protected replacements.

### INT-EP-05 — Earlier truncation was real and restoration is not a full historical PASS

**Judgement:** Temporary internal reduction with later substantial body restoration.

bedcfce7 reduces75,561bytes to4,139 on27September.01e45c1 restores74,814 on28September. The full old/restored diff shows deck/route and ranking wording changes, while the technical body returns. Current media manifest preserves the removed Ward/Drive/mirror/PDF routes as explicit historical versions. Binary rendering/equality over all media was not reviewed. Other earlier EP versions remain semantically open, despite complete identity/diff capture.

### INT-EP-06 — A23 and transfer prerequisites were strengthened before the fork

**Judgement:** Preserved negative correction, not source loss.

7d6ec216 and merge59ca3c42 produce the same corrected README15df1f0b. Old all-six conformance closure is withdrawn, P3/P5/P6 countermodels stay open, and transfer formulas gain BaseGuarantee/X3/X4 prerequisites. Current EP and A23 preserve those limits. The merge is a second chronology event, not a second independent result or payload.

### INT-DEV-01 — Development strategy has one unchanged body

**Judgement:** No later internal rewriting in this path.

7150279 adds f25aef42 on6October; current path has the identical12,211-byte blob. Full strategy was read. Its priorities remain proposals: clarify meaning/evidence, end-to-end profile, negative-capable strong comparison, attributable review and bounded transfer. It grants no experiment/contact authority. Links to later-reviewed owners do not make the strategy complete or adopted.

### INT-SCOPE-01 — All internal versions are identified; early semantic coverage remains bounded

**Judgement:** 100 unique primary payloads/102 history events; not100 complete independent audits.

Requirements12payloads/events; successor1; EP86payloads/88events including two duplicate-payload merges; strategy1. All identities and full modification diffs are captured. Current four bodies and all18 EP deltas from29September are read; Requirements all11 deltas are read. Other earlyEPdeltas are captured but not wholly semantically adjudicated. Prior fullDOCX reviews are contextual support, never substitutes for this internal chronology.

### Five protected replacements — exact historical before/after

These are observed applied transactions, **not pending restoration proposals**. Later current SHA protection, commit titles and a12October approval cannot establish earlier contemporaneous permission. Passage-specific authorization remains unaccredited. The full before/immediate-after blocks below distinguish semantic preservation from permission; current source reading and every prior audit remain intact. No revert follows from this finding.

#### [39af310284c0](https://github.com/dakleyer/structural-awareness-contributions/commit/39af310284c0ec84798814ad380473ae1d23f18c) — 2026-10-06T18:11:26+02:00

HID/HIT correction has explicit source rationale and receiver §§14–16. Time/qualified capacity are now represented by the runtime tuple; do not restore queue-deficit HID as the canonical debt definition.

**Historical text before — complete affected block**

~~~~text
[**01K — Human Intelligence Capacity, Escalation and Debt Profile**](../../research/ecosystem-awareness/baseline/01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md) is an additive positioning extension, not a new EA/EP core mechanism. It separates **Human Time** from **Human Intelligence Tokens (HIT)**, defines a bounded working notion of **Human Intelligence Debt**, and connects finite human-review capacity to the existing Signalling/EHD and Repositioning paths.
~~~~

**Historical text after — complete immediate receiving block**

~~~~text
[**01K — Human Intelligence Capacity, Escalation and Debt Profile**](../../research/ecosystem-awareness/baseline/01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md) is an additive positioning extension, not a new EA/EP core mechanism. It imports the existing **Human Intelligence Debt** framework — HICR, HICT and the architectural gap between feasible genuine human contribution and actual contribution — and connects it to a separate runtime Human Escalation capacity check over the existing Signalling/EHD and Repositioning paths.
~~~~
**Historical text before — complete affected block**

~~~~text
Where a repositioning transition depends on human review, Ecosystem Positioning / MSCA Operation may consume 01K before emitting a human-directed trigger. Repositioning can remain `HOLD` / `UNRESOLVED` while a successor ACC, re-contracting decision or authority response is pending; the alert does not bypass that gate.
~~~~

**Historical text after — complete immediate receiving block**

~~~~text
Where a repositioning transition depends on human review, Ecosystem Positioning / MSCA Operation may consume 01K before emitting a human-directed trigger. The runtime question is whether a qualified human path is actually usable inside the response window; the architectural question is whether the interface is eliciting genuine human contribution or generating avoidable compensatory work. Repositioning can remain `HOLD` / `UNRESOLVED` while a successor ACC, re-contracting decision or authority response is pending; the alert does not bypass that gate.
~~~~

Current receiver: [current protected README](https://github.com/dakleyer/structural-awareness-contributions/blob/ca5dd562a9566e69f691a28a7dfbb0b6c69479bb/architectural-contributions/ecosystem-positioning/README.md). Its changed passage is read in the current source; full source custody remains in the pinned predecessor and immediate commit. **Authorization:** No contemporaneous passage-specific human GO was located. Commit metadata and the later protected SHA do not supply that approval.

#### [6c93994c0295](https://github.com/dakleyer/structural-awareness-contributions/commit/6c93994c02959c0c0061c08b96983ed5c4afdfbe) — 2026-10-06T18:25:22+02:00

Expanded two-surface HC/HID source imports architecture/measurement distinctions, retains nonprivileged alerts and authority boundaries; no demonstrated deletion of those obligations.

**Historical text before — complete affected block**

~~~~text
[**01K — Human Intelligence Capacity, Escalation and Debt Profile**](../../research/ecosystem-awareness/baseline/01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md) is an additive positioning extension, not a new EA/EP core mechanism. It imports the existing **Human Intelligence Debt** framework — HICR, HICT and the architectural gap between feasible genuine human contribution and actual contribution — and connects it to a separate runtime Human Escalation capacity check over the existing Signalling/EHD and Repositioning paths.
~~~~

**Historical text after — complete immediate receiving block**

~~~~text
[**01K — Human Capacity / Human Intelligence Debt**](../../research/ecosystem-awareness/baseline/01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md) is the additive extension for two non-fungible surfaces: **runtime Human Capacity** for a particular intervention window, and **Human Intelligence Debt** as the architecture-level gap between feasible genuine human contribution and the contribution the socio-technical system actually elicits. Its organisational annexes import HICR/HICT/HID, GIC/NEO/ACW, portfolio answerability, capability-multiplicity, recovery/velocity and Net Oversight Impact measures, with explicit evidence gates and cross-series bridges. It is consumed by Signalling/EHD and Repositioning where material; it is not a new EA/EP core mechanism.
~~~~

Current receiver: [current protected README](https://github.com/dakleyer/structural-awareness-contributions/blob/ca5dd562a9566e69f691a28a7dfbb0b6c69479bb/architectural-contributions/ecosystem-positioning/README.md). Its changed passage is read in the current source; full source custody remains in the pinned predecessor and immediate commit. **Authorization:** No contemporaneous passage-specific human GO was located. Commit metadata and the later protected SHA do not supply that approval.

#### [c2d0d5161bc4](https://github.com/dakleyer/structural-awareness-contributions/commit/c2d0d5161bc4ddd98258e071de29f586a8813636) — 2026-10-06T19:23:09+02:00

Renames extension and appends A01 implementation routing. Old title is a retired local label; exact old source remains historical, while new component claim is a documentary contract, not native execution.

**Historical text before — complete affected block**

~~~~text
### Additive Human Intelligence / Human Escalation extension
~~~~

**Historical text after — complete immediate receiving block**

~~~~text
### Additive Human Capacity / Human Intelligence Debt extension
~~~~
**Historical text before — complete affected block**

~~~~text
[**01K — Human Capacity / Human Intelligence Debt**](../../research/ecosystem-awareness/baseline/01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md) is the additive extension for two non-fungible surfaces: **runtime Human Capacity** for a particular intervention window, and **Human Intelligence Debt** as the architecture-level gap between feasible genuine human contribution and the contribution the socio-technical system actually elicits. Its organisational annexes import HICR/HICT/HID, GIC/NEO/ACW, portfolio answerability, capability-multiplicity, recovery/velocity and Net Oversight Impact measures, with explicit evidence gates and cross-series bridges. It is consumed by Signalling/EHD and Repositioning where material; it is not a new EA/EP core mechanism.
~~~~

**Historical text after — complete immediate receiving block**

~~~~text
[**01K — Human Capacity / Human Intelligence Debt**](../../research/ecosystem-awareness/baseline/01K_HUMAN_INTELLIGENCE_CAPACITY_ESCALATION_AND_DEBT_PROFILE_v0.1.md) is the additive extension for two non-fungible surfaces: **runtime Human Capacity** for a particular intervention window, and **Human Intelligence Debt** as the architecture-level gap between feasible genuine human contribution and the contribution the socio-technical system actually elicits. Its organisational annexes import HICR/HICT/HID, GIC/NEO/ACW, portfolio answerability, capability-multiplicity, recovery/velocity and Net Oversight Impact measures, with explicit evidence gates and cross-series bridges. It is consumed by Signalling/EHD and Repositioning where material; it is not a new EA/EP core mechanism. Its reusable implementation contract is [**01K-A01 — HC-HID Component Specification**](../../research/ecosystem-awareness/baseline/01K_A01_HUMAN_CAPACITY_HID_COMPONENT_SPEC_v0.1.md), which exposes process-relative HC/HID A/B/C/D outputs through the ordinary EHD/receiver-requalification path, controls same-operation circularity and contributes human runtime/readiness/architecture cost to the existing DDS ledger.
~~~~

Current receiver: [current protected README](https://github.com/dakleyer/structural-awareness-contributions/blob/ca5dd562a9566e69f691a28a7dfbb0b6c69479bb/architectural-contributions/ecosystem-positioning/README.md). Its changed passage is read in the current source; full source custody remains in the pinned predecessor and immediate commit. **Authorization:** No contemporaneous passage-specific human GO was located. Commit metadata and the later protected SHA do not supply that approval.

#### [1aba8cf53868](https://github.com/dakleyer/structural-awareness-contributions/commit/1aba8cf5386806192ca572dff3de0f63814168f5) — 2026-10-07T11:35:23+02:00

Reclassifies 00D as comparator/fairness support under DDS. Matched B0–B3 facts, controls, pre-registration, budget, downstream effects and pending independent comparison remain explicitly in the current paragraphs.

**Historical text before — complete affected block**

~~~~text
| **5 minutes** | **20 minutes** | **Technical review** |
|---|---|---|
| Read the six scenarios and open either [Requirements & Evidence](../../presentations/ecosystem-positioning/Ecosystem_Positioning_Requirements_Evidence_Canonical_v1.2.pptx) or [Architecture & Implementation](../../presentations/ecosystem-positioning/Ecosystem_Positioning_Architecture_Implementation_Canonical_v1.2.pptx). | Continue through the [validation journey](#the-validation-journey) and [Awareness → Positioning → Agent Defense](#awareness--positioning--agent-defense). | Follow Requirements → interfaces → fixtures/harness → benchmark → applied validation / evidence maturity. |
~~~~

**Historical text after — complete immediate receiving block**

~~~~text
| **5 minutes** | **20 minutes** | **Technical review** |
|---|---|---|
| Read the six scenarios and open either [Requirements & Evidence](../../presentations/ecosystem-positioning/Ecosystem_Positioning_Requirements_Evidence_Canonical_v1.2.pptx) or [Architecture & Implementation](../../presentations/ecosystem-positioning/Ecosystem_Positioning_Architecture_Implementation_Canonical_v1.2.pptx). | Continue through the [validation journey](#the-validation-journey) and [Awareness → Positioning → Agent Defense](#awareness--positioning--agent-defense). | Start at the [DDS Canonical Method Index](../../research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md), then follow the applicable Gate A/B/C route and its supporting requirements, interfaces, fixtures/oracle/harness and comparator evidence. |
~~~~
**Historical text before — complete affected block**

~~~~text

~~~~

**Historical text after — complete immediate receiving block**

~~~~text
> **Current DDS route — 7 October 2026.** The historical scenario → fixture → oracle → harness → pre-registration → execution material below is now incorporated under the [DDS Canonical Method Index](../../research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md). The original artefact names, versions and evidence ceilings remain intact. Stage-0 fixture execution and 00L symbolic work are bounded Gate-A evidence; 00D-A01/A03 and R01 C02 are support/test-infrastructure; 00D supplies comparator/fairness discipline; future Gate-B and Gate-C claims require their own upstream packages and cannot be inferred from these earlier records.

A narrative scenario is not evidence by itself. The corpus therefore separates **scenario**, **fixture**, **oracle**, **harness**, **pre-registration** and **execution**.
~~~~
**Historical text before — complete affected block**

~~~~text
[**Testbed Method / Canonical Benchmark v0.2 — comparative execution method**](../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) defines matched B0–B3 comparator arms, frozen facts and decision conditions, continuity and failure branches, pre-registered measures, and a common resource and burden ledger. Comparative execution and independent replication remain pending.
~~~~

**Historical text after — complete immediate receiving block**

~~~~text
[**00D Canonical Benchmark v0.2 — DDS comparator/fairness support**](../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) defines matched B0–B3 comparator arms, frozen facts and decision conditions, continuity and failure branches, pre-registered measures, and a common resource and burden ledger. Within the current DDS method it is comparator/fairness support rather than a parallel method. Comparative execution and independent replication remain pending.
~~~~
**Historical text before — complete affected block**

~~~~text
The comparative method freezes the decision boundary, runs peer and EA configurations fairly, follows the downstream consequences of PASS/FAIL, and records tokens/compute, calls, time, human interventions, disclosure and containment burden. The [benchmark execution and decision rule](../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md#12-benchmark-execution-and-decision-rule) and [bounded oracle/test design](../../research/ecosystem-awareness/baseline/00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md) are the published sources.
~~~~

**Historical text after — complete immediate receiving block**

~~~~text
The 00D support contract freezes the decision boundary, runs peer and EA configurations fairly, follows the downstream consequences of PASS/FAIL, and records tokens/compute, calls, time, human interventions, disclosure and containment burden. The [benchmark execution and decision rule](../../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md#12-benchmark-execution-and-decision-rule) and [bounded oracle/test design](../../research/ecosystem-awareness/baseline/00D_A01_REFERENCE_SCENARIO_TEST_ARTIFACTS_AND_BOUNDED_ORACLE_CONSTRUCTION_AND_TEST_DESIGN_v0.1.md) are the published supporting sources.
~~~~

Current receiver: [current protected README](https://github.com/dakleyer/structural-awareness-contributions/blob/ca5dd562a9566e69f691a28a7dfbb0b6c69479bb/architectural-contributions/ecosystem-positioning/README.md). Its changed passage is read in the current source; full source custody remains in the pinned predecessor and immediate commit. **Authorization:** No contemporaneous passage-specific human GO was located. Commit metadata and the later protected SHA do not supply that approval.

#### [64fa9f3d777c](https://github.com/dakleyer/structural-awareness-contributions/commit/64fa9f3d777c30860b92ffa7e4440ef4b7193ca8) — 2026-10-07T13:24:21+02:00

Gate to Stage terminology correction preserves object/evidence semantics and stable filenames in the current DDS Method Index; source-native Stage-0 terms retain their own meaning.

**Historical text before — complete affected block**

~~~~text

~~~~

**Historical text after — complete immediate receiving block**

~~~~text
# Ecosystem Positioning

<!-- DDS terminology revision 1 (2026-10-07): Stage A/B/C only; source scientific version and evidence unchanged. -->
### Agentic Architecture for staying situated as the ecosystem changes
~~~~
**Historical text before — complete affected block**

~~~~text
| **5 minutes** | **20 minutes** | **Technical review** |
|---|---|---|
| Read the six scenarios and open either [Requirements & Evidence](../../presentations/ecosystem-positioning/Ecosystem_Positioning_Requirements_Evidence_Canonical_v1.2.pptx) or [Architecture & Implementation](../../presentations/ecosystem-positioning/Ecosystem_Positioning_Architecture_Implementation_Canonical_v1.2.pptx). | Continue through the [validation journey](#the-validation-journey) and [Awareness → Positioning → Agent Defense](#awareness--positioning--agent-defense). | Start at the [DDS Canonical Method Index](../../research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md), then follow the applicable Gate A/B/C route and its supporting requirements, interfaces, fixtures/oracle/harness and comparator evidence. |
~~~~

**Historical text after — complete immediate receiving block**

~~~~text
| **5 minutes** | **20 minutes** | **Technical review** |
|---|---|---|
| Read the six scenarios and open either [Requirements & Evidence](../../presentations/ecosystem-positioning/Ecosystem_Positioning_Requirements_Evidence_Canonical_v1.2.pptx) or [Architecture & Implementation](../../presentations/ecosystem-positioning/Ecosystem_Positioning_Architecture_Implementation_Canonical_v1.2.pptx). | Continue through the [validation journey](#the-validation-journey) and [Awareness → Positioning → Agent Defense](#awareness--positioning--agent-defense). | Start at the [DDS Canonical Method Index](../../research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md), then follow the applicable Stage A/B/C route and its supporting requirements, interfaces, fixtures/oracle/harness and comparator evidence. |
~~~~
**Historical text before — complete affected block**

~~~~text
> **Current DDS route — 7 October 2026.** The historical scenario → fixture → oracle → harness → pre-registration → execution material below is now incorporated under the [DDS Canonical Method Index](../../research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md). The original artefact names, versions and evidence ceilings remain intact. Stage-0 fixture execution and 00L symbolic work are bounded Gate-A evidence; 00D-A01/A03 and R01 C02 are support/test-infrastructure; 00D supplies comparator/fairness discipline; future Gate-B and Gate-C claims require their own upstream packages and cannot be inferred from these earlier records.
~~~~

**Historical text after — complete immediate receiving block**

~~~~text
> **Current DDS route — 7 October 2026.** The historical scenario → fixture → oracle → harness → pre-registration → execution material below is now incorporated under the [DDS Canonical Method Index](../../research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md). The original artefact names, versions and evidence ceilings remain intact. Stage-0 fixture execution and 00L symbolic work are bounded Stage A evidence; 00D-A01/A03 and R01 C02 are support/test-infrastructure; 00D supplies comparator/fairness discipline; future Stage B and Stage C claims require their own upstream packages and cannot be inferred from these earlier records.
~~~~

Current receiver: [current protected README](https://github.com/dakleyer/structural-awareness-contributions/blob/ca5dd562a9566e69f691a28a7dfbb0b6c69479bb/architectural-contributions/ecosystem-positioning/README.md). Its changed passage is read in the current source; full source custody remains in the pinned predecessor and immediate commit. **Authorization:** No contemporaneous passage-specific human GO was located. Commit metadata and the later protected SHA do not supply that approval.

### Restoration decisions and remaining work

Retain H3’s corrected falsifier, current01K§16’s explicit HIT rejection, the separate runtime-capacity ledger, A23’s P3/P5/P6 countermodels and its conditional transfer prerequisites. These are reasoned internal corrections, not omissions to reverse. Review authorization and historical custody separately. Finish earlier EP clause/media dispositions and actual S10 consumer binding. [Requirements counterpart](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) records the same frozen/working consequences.

| Review work | Positive impact | Risk of mistaken restoration | Effort |
|---|---|---|---|
| Reconcile five protected replacements with actual prepared passages/GO | High — verifiable custody and authority | High if later approval is treated as retroactive permission or an obsolete error is restored | Medium evidence work; no source revert |
| Preserve corrected H3/HIT/A23 interpretation | High — correct falsification/debt/transfer object | High for blanket historical rollback | Low classification; source-consumer validation remains separate |
| Working S10 discovery | Medium — readable current preparation route | Low for the complete bounded append; Medium for broad consumer adoption | Low editorial; Medium per consumer |
| Earlier EP versions and media | Medium — complete history | High if textual restoration substitutes for all clauses/assets | High remaining source/visual review |


### Prepared change 97 — Link the approved S10 working successor at the existing EP closing note

**Status:** Prepared — pending named Ivan GO. **Impact:** Medium. **Risk:** Low. **Effort:** Low. **Priority:** Next.

Source: [architectural-contributions/ecosystem-positioning/README.md](https://github.com/dakleyer/structural-awareness-contributions/blob/ca5dd562a9566e69f691a28a7dfbb0b6c69479bb/architectural-contributions/ecosystem-positioning/README.md); exact current blob `9767ec8efb7d3a2875866ea3cd22ebc94882e930`. Complete existing closing paragraph unique, located at EOF; append-only proposed addition.

**Text before — complete current affected context**

~~~~text
The labels P1–P6 name the semantic principles of Ecosystem Awareness. P1–P3 in the positioning discussion name operating postures. Read each label with its own definition and owner; they are different lists, and neither grants authority to act. The [review workspace](./README_VNext.md) records proposed clarifications and the decisions still needed.
~~~~

**Text after — complete proposed context and addition**

~~~~text
The labels P1–P6 name the semantic principles of Ecosystem Awareness. P1–P3 in the positioning discussion name operating postures. Read each label with its own definition and owner; they are different lists, and neither grants authority to act. The [review workspace](./README_VNext.md) records proposed clarifications and the decisions still needed.

For current preparation, the [owner-approved Requirements working successor](../../research/ecosystem-awareness/baseline/00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md) adds the S10 obligation to bind execution to the requalified decision basis. The frozen Requirements remain the contract for studies that registered that edition; this working successor does not retrospectively change their inputs, findings or evidence grade.
~~~~

**Why:** Makes the actual approved working S10 source discoverable while retaining the registered freeze for earlier studies.

**Risk:** Working-source guidance could be mistaken for retroactive adoption; the complete appended sentence preserves the historic evidence/contract boundary.

**Cost/validation:** One reading paragraph and two source checks; individual new-study consumer adoption is separate.

**Dependencies:** Requirements working successor, baseline approved-successor route, DOCUMENT_CONTROL§26 and existing Requirements application#16.

**Iván’s instruction/decision:** Ivan names this pair/wave; EP is append-only and all prior bytes must remain; validate current EOF and links. No source-body replacement. Pending; not applied. All other source bytes must remain unchanged.


### Internal branches requiring their own disposition

These eight tips have commits not wholly reachable from main; this graph statement does not establish that their substantive payloads are absent. Some entered main by a different integration path, some are draft-only work. Full current/branch source comparison remains in the actual owning source queue; do not merge or restore them from this table.

| Contributions branch | Fixed tip | Real source/recipient question |
|---|---|---|
| `audit/pptx-canonical-2026-09-28` | [bfc50c4239f1](https://github.com/dakleyer/structural-awareness-contributions/commit/bfc50c4239f1bd5716931ef67014a10dedf1f3e0) | Intermediate PPTX branch versus final deck branch/current full media; binary/text/visual comparison remains separate. |
| `campaign/flores-addendum-merge-20261013` | [0f7958c7aebc](https://github.com/dakleyer/structural-awareness-contributions/commit/0f7958c7aebcebd1c43b8902506c5587b145d729) | Technical/addendum preparation versus current recovered Flores campaign; exact and changed payload recipients differ. |
| `campaign/flores-theme21-residual-20261013` | [04ade51c4d28](https://github.com/dakleyer/structural-awareness-contributions/commit/04ade51c4d28bc6e1ffa40364cecb78407d01d82) | Earlier Flores fg-tida/tests edition versus current campaigns-in-development body/history; source/key/method scope must remain distinct. |
| `codex/abcd-foundation-2026-10-01` | [f5932a8f5f1b](https://github.com/dakleyer/structural-awareness-contributions/commit/f5932a8f5f1b7c75edf18dc66882f0633c01d778) | Old ABCD proposed canonical note versus actual maintained00M and foundational receivers; avoid restoring competing authority. |
| `dds/china-unicom-privilege-lifecycle-stage-a-v0.1-20261014` | [b1d0aa2c75f8](https://github.com/dakleyer/structural-awareness-contributions/commit/b1d0aa2c75f814acfa5d1dd542f21268e3ac431c) | New China Unicom campaign drafts/28 paths absent at this main cut; branch-only work, no demonstrated main deletion or adoption. |
| `research/hf-signalling-handshake-multigate-v04-20261012` | [9fa6878e6613](https://github.com/dakleyer/structural-awareness-contributions/commit/9fa6878e6613a296ef111a78a7251964972c26f3) | HF multigate-v0.4 draft/13 missing branch paths versus current counterfactual studies; no automatic run or evidence promotion. |
| `research/steven-s5-audit-2026-10-11` | [d355f9022b3f](https://github.com/dakleyer/structural-awareness-contributions/commit/d355f9022b3f9f628707cb13542c6c8df7546acf) | S5 review-package versions/comments versus current S5 source and retained audit; comments are not sent by this check. |
| `review/four-point-completion-registers-2026-10-12` | [1b7f30c53165](https://github.com/dakleyer/structural-awareness-contributions/commit/1b7f30c53165e35053b6c3103f734728fa5d7d6d) | Historical snapshot and review-register variants versus actual active files; no new audit of snapshots. |

The complete global object graph is inventoried; semantic closure is per document. Current PDFs/decks and remaining early EP versions stay on the reading queue.


## Substantive value and current DDS fit before any restoration — 14 October 2026

**Iván’s instruction:** these passes must establish what earlier content contributes, whether its information remains valid and significant, and how it relates to the current DDS strategy. Finding an absent sentence is a lead to examine, not a reason to insert it. This instruction governs all pending damage/restoration work and its earlier candidates. No source change is authorized by this clarification.

### The decision before drafting a change

For each material discrepancy, the owning VNext must answer these questions in ordinary language:

1. **What information does it carry?** State the actual definition, reasoning, requirement, control, negative result, evidence, dependency or useful explanation. Describe its original purpose and the precise claim it can support. A title, identifier or older phrase is not enough.
2. **What is genuinely absent?** Read the complete current context and actual recipients. Distinguish a missing proposition from a renamed concept, transferred table, shorter equivalent explanation, duplicate, archived edition or corrected error. A surviving fragment does not prove the whole obligation survived either.
3. **Is it still valid and applicable?** Check premises, version, authority, evidence and subsequent corrections. Explain whether a historical requirement still governs a registered study, has a qualified successor, or was deliberately superseded. Keep uncertainty visible when the sources do not settle that question.
4. **Where does it belong in current DDS?** Name the specific Challenge/object, Stage A/B/C or support function and the actual owner. Explain how it helps specification discovery, architecture verification, implementation/problem validation, a sound comparator, useful infrastructure or the human reading route. Do not revive a parallel method or import a source-specific theorem into every DDS profile.
5. **What useful difference would the change make?** Identify the reader, decision, obligation or result interpretation affected. Explain the consequence of leaving the text as it is and the benefit expected from the smallest adequate correction. Text volume, historical age and the number of apparent omissions are not impact measures. A missing limiter, refutation or negative result can be material even when it adds no new feature.
6. **What is the supported disposition?** Record: already received; valid correction/supersession; history/support only; significant applicable omission; or unresolved. Link the evidence and explain the judgement. If no active change is warranted, say why and retain the historical source under its proper status.

Only a supported significant applicable omission or a demonstrated current inconsistency advances to a surgical proposal. The proposal retains the complete literal current before/after, source and location, concrete benefit, impact, risk, effort, affected consumers and the decision Iván must make. A proposed restoration may require a newly qualified explanation rather than reinstating the old wording. It remains in the existing VNext until the specific wave/passages receive GO.

### What the current strategy actually requires

[The current DDS Method Index](https://github.com/dakleyer/structural-awareness-contributions/blob/6e2eca9e6288b32cc29fcbc17c224d014ea3b016/research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md) distinguishes the object and reference of the three stages: Stage A compares candidate specifications/mechanisms against the frozen Challenge; Stage B verifies an architecture against the frozen Stage A package; Stage C validates a pinned implementation against the originating Challenge and observed effects. Evidence modes remain separate from those stages. Sections 4, 7 and 8 preserve the role of R01, comparator/oracle/harness infrastructure and earlier results without making them competing corpus-wide methods or retrospectively stronger evidence.

[The development strategy](https://github.com/dakleyer/structural-awareness-contributions/blob/6e2eca9e6288b32cc29fcbc17c224d014ea3b016/architectural-contributions/ecosystem-positioning/DEVELOPMENT_STRATEGY.md) supplies the broader purpose: preserve the meaning and evidence of claims, make a complete useful profile understandable, compare against competent alternatives with the possibility of a negative finding, and transfer only what its premises support. It is an earlier development proposal, read together with current DDS sources; it is not a reason to override later source-specific directions or registered contracts.

**Strategic fit is a test of relevance and justified use, not agreement with a preferred result.** Contrary evidence, counterexamples, competence of conventional controls and applicable restrictions remain material. A changed strategy does not erase earlier results or the contract governing an old run. Historical significance can justify preservation and an explanatory route without reintroducing the passage as current authority.

### Consequences already supported by the internal review

| Earlier material | Current information and DDS role | Decision |
|---|---|---|
| Stage A’s former eight-family registry | Its classification and Cost/Risk/Effectiveness/Acceptance/BV/evidence distinctions have an actual recipient in Method Index §8 | Keep the current central registry and the historical source; no duplicate restoration |
| The claim that one Stage A document is the whole DDS method | The current method has an Index and three substantive stages with distinct objects and references | Retain the updated ownership; review any genuinely missing whole-method version rule on its own evidence |
| Earlier H3 falsifier, H2 independence iff, and token-queue definition of HID | The internal review records specific corrections and current recipients for their valid remaining content | Preserve the correction and its rationale; do not reinstate the erroneous assertion as a repair |
| The original completion release manifest versus later active reports | Historical package custody is demonstrated; later documentation has its own edition and diagnostic scope | Preserve both epochs and propose only a useful current-reading clarification; do not regenerate the old manifest to fit later prose |
| Earlier R01 proof/oracle material not yet adjudicated | A filename or relocation map does not settle the validity or applicability of its claims to current DDS | Read the complete material and consumers first; keep the disposition unresolved until then |

These decisions narrow what may be proposed. They neither insert recovered material nor convert the remaining internal-history queue into a list of changes to apply. The earlier audits and exact pairs remain visible; their age or pending status creates no presumption that they should be adopted.


## Third pass — fresh context and deferred audit comparison, 14 October 2026

**Iván requests a fresh, detailed third review of the entire corpus and an independently derived restoration and organization plan.** Reviewer `/root/third_pass_blind_corpus` has been started with an empty conversation context (`fork_turns=none`). No previous findings, candidate list, audit ranking or earlier reviewer reports were supplied. The coordinator retains administrative continuity and keeps it out of the reviewer’s source judgement.

### Phase A: derive and seal the review from primary sources

The reviewer builds its own complete current-file/logical-unit inventory, chooses its own reading sequence from actual source dependencies, and fixes its source cut. All files must be accounted for: principal bodies and their parts/material evidence, code and results, schemas/records, original media/binaries, old versions, branch work and genuinely additional material. Metadata, copies and historical snapshots receive their actual role; counting them does not create extra independent articles or scientific passes.

The central comparison is internal Contributions history: source creation, material intermediate versions and merge parents, current body, displaced information and actual receiving sources. The use-cases fork is secondary provenance. Per-document records identify complete versus partial reading and explain clause/table/formula/field/asset and producer–consumer–return consequences. Hashes, path existence and link scans support those judgements; they do not replace them.

For each coherent cohort, the reviewer saves a timestamped, immutable first judgement, its plan and an exposure/read ledger, with exact source identities and SHA-256 custody. The reviewer may proceed to the next source cohort after sealing. **No earlier VNext audit, review report, priorities or memory is opened until Phase A has been completed and sealed for the whole principal corpus and its material integrations.** Unblinding after one cohort would influence the cohorts that remain, so it is expressly deferred.

Operating controls are read without their appended summaries of earlier audit results. Primary-source assertions and any review commentary encountered in a primary source are logged separately. An accidental exposure is recorded against the affected scope; the independence claim follows that record rather than an assumed label. The agent uses the configured model; the distinction is its fresh context and evidence process, not an invented different model or institution.

### Phase B: compare earlier audits after the independent baseline

Once the whole Phase A baseline is sealed, the reviewer reads the existing audits and distinguishes agreement, disagreement, overlooked evidence and genuinely new findings. The sealed first judgements remain unchanged. Later answers or revisions are dated additions; they cannot be substituted for the original independent record.

The coordinator can publish sealed partial findings before Phase A ends, using the existing owning VNext and preserving its exact predecessor. Those publications are not fed back to the reviewer as evidence or priorities. The fixed source cut prevents new review additions from silently entering the blind source set. Substantive feedback from the coordinator is deferred; custody/coverage checks are kept separate from the reviewer’s reasoning.

### Independently derived restoration and organization plan

Each proposed change must justify the information’s validity, significance, current DDS role and concrete useful effect. The reviewer determines whether it is already received, a sound correction/supersession, history/support only, a significant applicable omission, or unresolved. Negative evidence and applicable historic contracts remain material. No recovered wording is inserted merely because it disappeared.

Where an active change is justified, the existing owner receives complete literal current text before and complete proposed text after, exact location/source, reason/evidence, dependencies and ordering, expected impact, risk, effort and acceptance checks. Organization proposals explain the actual source/destination and preserve content, original files, links and the three canonical README levels. They are plans, not permission to move files, establish competing sources or rebuild the tree.

Original canonical documents, frozen evidence, results, code and binaries remain in reading mode. Restoration/organization requires Iván’s GO for the named passages or wave. This request authorizes the review and its plan, not automatic incorporation. No new public VNext, report collection, experiment, contact or timer is created.

### Actual progress and closure

The new reviewer has been dispatched; its own inventory, first source judgements and plan are being produced. This protocol is not their result and does not certify any file as reviewed. Progress distinguishes unread, complete source read, material history read, receiving relation incomplete, first judgement sealed, earlier audit compared, plan prepared and publication verified. Whole-corpus completion requires those actual records and the final cross-document reconciliation; a first cohort does not close the third pass.


## Third-pass isolation correction — memory-free source reviewer, 14 October 2026

The empty-conversation collaboration attempt described above disclosed that its runtime still supplied a general memory summary. That does not meet Iván’s strict requirement of no previous review knowledge. The coordinator stopped that attempt. Its initial inventory and reads remain preserved as setup evidence and are **not counted as the independent third-pass baseline**. No old audit body was deliberately opened, and no source change was applied.

The replacement is one isolated source-review session, `01a13c1e-5ce0-7711-824b-e372b6c3c5b2`, started with memory use and generation disabled for that invocation, without loading user configuration or enabling hooks, apps or subagents. The sandbox and automatic approval review remain active; global settings and credentials are unchanged. [OpenAI Docs — configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference) documents that disabling `memories.use_memories` prevents existing memory injection. The local launch options and initial-context record provide the evidence for this actual run.

Before opening the corpus, the replacement wrote an exposure record stating that no previous memory, conversation or corpus-review findings were visible. It inspected only the neutral operating assignment at that point. The original record was copied under coordinator custody before source reading. Initial exposure SHA-256: `4784db9ad7fb218a50d144a14ac449f45969cb64d4d8d70e10120c0640aa3866`. Operational preflight attempts and interrupted starts are retained separately and do not create extra audit credits or source judgements.

The reviewer receives no previous findings, candidates or earlier ranking. It derives its own inventory, source cut, reading sequence, source/history/receiver judgements and restoration/organization plan. The coordinator supplies administrative custody only. The full Phase A isolation gate remains: prior audits stay unread until all principal source/material-integration first judgements are sealed. Published partial results will not be fed back into the reviewer’s evidence set.

Actual status: the memory-free reviewer is running its initial source work. This correction establishes the operating process; it is not a completed third review, a completed plan or a judgement on all files. Source-reading coverage, sealed results and unresolved work will be recorded from that reviewer’s own artifacts. The unique existing VNext owners remain the publication destination. No restoration, reorganization, experiment or timer is activated.


## Third independent review — first scoped source judgement, 14 October 2026

The [00M VNext first source judgement](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00M_VNext.md#third-independent-source-review--00m-branch-correction-14-october-2026) now contains the isolated reviewer's original assessment, complete old/successor evidence and its own limited plan. The three internal branch versions correct a timing implication: a finite terminating construction does not establish a useful operational deadline. The judgement is **preserve the correction, no current replacement proposed**. The coordinator authenticated the source blobs, unique quoted passages and branch ancestry; it did not supply prior findings to the reviewer.

This is the first scoped result, not a completed document/cohort or global restoration plan. The reviewer continues its own current-source, internal-history and receiver queue on fixed cut `36b6d6e0b485170d68445fcb1bf5540d540355b7`. All-source first judgements must be sealed before it compares previous audit bodies. Original documents, programs, results and binaries remain unchanged.


## Third independent review — first execution source account, 14 October 2026

The isolated reviewer has preserved its first partial report and continues the same Phase A source review. It records six current paths with complete textual coverage (five direct, one comparative), seventeen distinct authenticated payload readings/comparisons and one scoped branch judgement. No logical-source cohort or whole restoration/organization plan is complete; 2,340 current paths still had no substantive reading at that boundary. Inventory and material reading remain separate.

The actual source accounts are now within the existing [00M VNext](../../research/ecosystem-awareness/baseline/00M_VNext.md#third-independent-source-review--first-current-text-reading-14-october-2026), [00N VNext](../../research/ecosystem-awareness/baseline/00N_VNext.md#third-independent-source-review--first-current-text-reading-14-october-2026) and [Requirements VNext](../../research/ecosystem-awareness/baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md#third-independent-source-review--first-current-text-reading-14-october-2026). They explain the meanings, conditional mathematical arguments, conventional/comparator and time/authority/burden constraints actually read. These are substantive partials, not a scan or a third-pass completion claim.

### Root entry — isolated reviewer's own first source account

The root README owns programme navigationand separates mathematical work, explanatory field notes, engineering provenance and architecture proposals. It routes the current reader to 00M v0.8 and 00N v0.7 and supplies distinct EA, RA and MSCA technical gates. Its evidence-boundary table refuses to promote engineering provenance to universal validation or submissions to endorsement. Root navigation supports identifying routes; it does not establish content reception in the unread target files. Its 47 path-internal historical payloads remain largely unread.

### Own plan and next source frontier

The first plan retains the justified branch timing correction and proposes no current source edit yet. The reviewer next follows foundations, principles, proof bases, mechanisms, topology, functions and actual input/mapping contracts before deciding source reception or DDS destinations. The complete source/relationship baseline precedes comparison of earlier audit bodies. The organization plan must establish actual owners, destinations and return routes with the three canonical README levels, preserve every file/content/link and avoid competing repositories. It is unfinished.

The first execution report was preserved unchanged before continuation, SHA-256 `639141a6f7f283ec024fc59ce3847184dcb0a78045d776434cb4394e16cf3d4e`. These excerpts publish its source conclusions; private operational records are retained locally. No new VNext, source replacement, move, deletion or experiment is introduced.


## Third independent review — localized proof proposal 100, 14 October 2026

[Foundation VNext now holds proposal 100](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/01_FOUNDATIONAL_VNext.md#third-independent-review--02a02b-proof-attribution-and-proposal-100-14-october-2026), independently derived from current 02A/02B and their material proof-family history. The localized change aligns 02A's Claim with the actual linked 02B relative-closure theorem, instead of attributing stronger normalizer properties without the corresponding current proof. It preserves both the semantic derivation and authentic older ordered-normalizer contracts. Complete current before/proposed after, source blobs, unique location, receiver theorem, rationale and acceptance checks are published.

Impact Medium, risk Low and paragraph effort Low; priority Next, pending A19/A21/00K and semantic-transfer reconciliation, then Iván's named paragraph/wave GO. This is one new independently prepared documentary proposal, not a restored source or a completed global plan. The isolated reviewer continues its own Phase A queue without receiving previous findings; whole-source completion and later comparison remain pending.


## Third independent review — input-contract custody plan, 14 October 2026

The [existing 04 VNext](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md#third-independent-review--input-contract-edition-custody-and-proposals-101102-14-october-2026) now contains the isolated reviewer's complete first input-contract custody judgement and two literal pairs, proposals 101–102. It preserves the valid dated B/C amendment and original Word/diagram/manifest, while clarifying that the current living Markdown is no longer an unchanged Word reproduction. No original asset or contract field is altered.

These are small edition-caption proposals, priority After: the source comment has impact Low and the visible paragraph Medium; both risk/effort Low. Existing amendment notices are already present, so this is not an urgent restoration or a reason to reintroduce the old C interpretation. The full source/receiver review and organization plan remain open. The latest saved independent checkpoint records 36 current source bodies and 122 authenticated read payload identities, with one actually viewed visual asset; those counts are not completed document cohorts. No canonical change is authorized by publishing these findings.


## Third source review — relative proof preservation, 14 October 2026

The [existing 00K review route](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/fixtures/00K-SUITE/README_VNext.md#third-source-review--00k-relative-proofs-and-preserved-corrections-14-october-2026) now contains the fourth scoped first record, actual old/current formula passages and its own bounded preservation/organization plan. It keeps current A23/A22 corrections, negative evidence, the competent conventional comparator and distinct source contracts; no restoration candidate is warranted in those already qualified passages. Consequences are recorded reciprocally in Foundation and Requirements VNext. No new dossier, source edit or experiment is introduced.

The latest saved checkpoint (21:24 UTC) records 41 current source bodies and 205 read payload identities including one disclosed prior execution-report exposure, not 205 independent audits. Whole source cohorts and the global restoration/organization plan remain incomplete. The reviewer began without previous memory/conversation; encountered source-author review claims and the accidentally opened A23 report are logged. Affected assertions are not described as perfectly blind. Other earlier first seals are preserved without retrofitting. The source queue continues.


## DDS strategy before restoration (15 October 2026)

Iván requests an organizing strategist before any recovery: preserve **UC-21 → objectives → Challenges → DDS → campaigns → results**, understand the current DDS controls and improve the reader route without reinstating the earlier disorder. The [source-led strategic review](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#dds-strategy-and-restoration-decisions-15-october-2026) now records the method’s purpose, actual document owners, instruments and representative results, followed by its comparison with the pending plans.

DDS remains reusable across cases. UC-21 supplies its objectives, Challenges and case protocols; the selected scenario maps a technology/configuration to that Challenge. A campaign’s owning report connects its finding and evidence back to the selected question. Existing original sources, frozen contracts, strong conventional controls, adverse results and valid later corrections retain their roles.

Before proposing recovery, identify the information’s actual contribution, its current validity and any adequate receiver, then choose restoration, a reading link, historical support or a documented unresolved disposition. An absent sentence does not by itself justify insertion. Keep the three corpus reading levels and current owners; no physical dds/ tree, duplicate method or new README is adopted.

The review found a concrete defect in pending 92: five case-relative links resolve to nonexistent DDS-folder paths and the objective table has an extra cell in each row. A complete literal successor of that existing passage now uses verified source permalinks and a three-column table. Existing 91/92 were already suspended by the 14 October content gate and remain so. Correcting that passage does not complete case-source integration. Draft A merges into 92; no new change ID is created. The optional application-router nomination is a future ownership question, not another required navigation hop. Existing 96 remains a separate bounded reading correction.

Consequences are recorded in the existing EA and baseline README VNext. All additions in this publication are review/control records. No original source, result, code, binary, file path or current reading relationship is changed. The exhaustive history review remains incomplete; its isolated source reviewer was not restarted or supplied this comparison.

A pre-existing priority-reader data-format error is repaired by explicitly declaring that the instruction-only guidance epoch contains no individual assessments. All its previous fields and all 102 original proposal entries remain unchanged; the current suspended view of 91/92 is checked with the existing reader.


## Independent strategy re-audit and unified restoration review (15 October 2026)

Iván asks a different reviewer to verify the strategy and all prior agents’ change/restoration plans before producing one detailed unified restoration and reinsertion plan. The [new reviewer’s sealed source-first judgement](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#independent-source-strategy-baseline-15-october-2026) is published in the existing DDS VNext. It finds the declared DDS progression coherent while identifying current-authority and version-reading ambiguities. It preserves **UC-21 → objectives → Challenges → DDS → campaigns → results**, with DDS reusable across cases.

This first account was recorded before the prior strategy and damage plans were opened. Comparative review is now in progress, with attributed source checks of case/EP/requirements and DDS/R01/oracle plans. The unified plan must distinguish useful missing information, valid correction, an existing receiver, historical support and unresolved evidence. It must specify complete old/proposed text, exact sources and destinations, dependencies, impact/risk/effort and verification for each proposed wave. Restoring an older formulation solely because it disappeared is not the method.

This publication adds review text only. The first account is not a completed unified plan, exhaustive corpus audit or source-adoption decision. Originals and existing owners remain unchanged; any incorporation waits for Iván’s named passage/wave GO.


## DDS unified restoration plan 15 October 2026

The independent re-audit retains the current presentation strategy and one maintained corpus. Recovery follows the useful information and its actual receiver, rather than a missing-string count. Current HC/HS, common metrics and important S6 meanings already have receivers; the complete case-specific recurrence/selection/run contract and source-edition custody still need binding.

The plan orders narrow reader corrections, contract/proof/capacity reconciliation, full case and asset reception, the maintained research bridge, and finally the official UC-21 entry/PDF. Existing corrections and contrary comparator evidence remain in place. It nominates receivers, records incomplete evidence and gives literal pairs where preparation supports them. It creates no extra README level or VNext owner.

[Read the full unified restoration plan](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#unified-restoration-plan-15-october-2026). Its work-package decisions and complete literal proposals govern the next preparation; source incorporation requires a named decision by Iván. The present EP source and development strategy remain unchanged.


### Existing candidate 97

Current EP ends at the exact old paragraph; S10 working successor exists with action-time binding and distinct frozen-predecessor status. Addition must remain at EOF.

**Impact / risk / effort:** Medio / Bajo / Bajo. **State:** Pending named exact Ivan GO; additional gates in plan apply

**Source:** [architectural-contributions/ecosystem-positioning/README.md](https://github.com/dakleyer/structural-awareness-contributions/blob/89273f548f6b5ed8f7e0576040f615b5653ffaf6/architectural-contributions/ecosystem-positioning/README.md), blob `9767ec8efb7d3a2875866ea3cd22ebc94882e930`. Dependencies: Requirements working successor, baseline approved-successor route, DOCUMENT_CONTROL§26 and existing Requirements application#16.

**Text before — complete current passage (1).**

``````text
The labels P1–P6 name the semantic principles of Ecosystem Awareness. P1–P3 in the positioning discussion name operating postures. Read each label with its own definition and owner; they are different lists, and neither grants authority to act. The [review workspace](./README_VNext.md) records proposed clarifications and the decisions still needed.
``````

**Text after — complete proposal.**

``````text
The labels P1–P6 name the semantic principles of Ecosystem Awareness. P1–P3 in the positioning discussion name operating postures. Read each label with its own definition and owner; they are different lists, and neither grants authority to act. The [review workspace](./README_VNext.md) records proposed clarifications and the decisions still needed.

For current preparation, the [owner-approved Requirements working successor](../../research/ecosystem-awareness/baseline/00_REQUIREMENTS_WORKING_SUCCESSOR_2026-10-12.md) adds the S10 obligation to bind execution to the requalified decision basis. The frozen Requirements remain the contract for studies that registered that edition; this working successor does not retrospectively change their inputs, findings or evidence grade.
``````

This is the same pending proposal, with its unified-review assessment, rather than another action under an alias. The complete earlier record remains above. Apply only an explicitly selected pair/wave; preserve every other source byte and its recorded freezes, evidence and results. [Joint plan and acceptance checks](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#unified-restoration-plan-15-october-2026).


## Literal restoration detail 15 October 2026

The [detailed source/receiver plan](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#literal-restoration-plan-15-october-2026) now supplies11new literal pairs103–113 beside the11existing complete proposals.103contains the complete UC21 HR/selection/run binding;104a prospective instrument packet;105/106the selected00J historical controls/populations;107–109capacity timing and its actual working caller;110/111R01 epoch/successor reading;112the complete48file historical custody scope;113the retired00J reading route.

For112,45UTF-8after payloads are fully visible in DDS VNext and3unchanged PNGs have exact binary cards. All proposed destinations are absent; the publication creates none. The original package's46/47digest replay discrepancy is retained rather than overwritten. The snapshot's READMEs are historical source content, not another maintained corpus level. Existing routes and archived/current authorities remain distinct.

The initial order prepares custody and case binding, then the coupled technical consumers, and only then92and the officialUC21/PDF. Unadjudicated histories, unused binaries or scientific implementation work receive no fabricated old/new pair. Original sources remain unchanged until Iván's named wave/passage decision.


## Literal plan check 15 October 2026

Review by Codex AI assistant, 15 October 2026, against published main `0aa9718afb40ba917ce21a45f20b4dfd7e73d925`. This is a new reading by the same assistant, not an additional independent auditor.

**Pairs checked here: 97; joint plan.** The closing source passage matches once. Its proposed addition preserves the entire current EP README as an exact prefix, including its existing terminal newline. The three reading levels and current UC21 → objectives → Challenges → DDS → campaigns → results route stay unchanged. The joint check selects the later92passage 1 and keeps91/92held; this receipt does not create another entry or move content.

Complete old and proposed blocks remain above; they were not replaced by this receipt. The [joint plan check](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#literal-plan-check-15-october-2026) records the selected92variant,33pairs across ten existing VNext, the48-file custody scope and the actual conditions still open. Published review is complete; source incorporation remains pending its named decision.


### Application 97 — 15 October 2026

**Applied; removed from the pending queue.** Iván authorised incorporation of the reviewed literal plan. Applied 1 complete literal replacement to `architectural-contributions/ecosystem-positioning/README.md`; resulting source blob `9bd2c1d10a8d440fa947abb7bc834d99ec97ff9b`. Each step has an exact inverse: every byte outside its approved old/new unit is identical. The complete earlier before/after and audit remain application history, not pending work. No campaign, run, result or code was changed.


**Verified application commits — 01_clarity:** [97](https://github.com/dakleyer/structural-awareness-contributions/commit/413208033cd6b92c9982adc3cfff0fa5161a3995).


## Owner authorised application complete 15 October 2026

**Applied and verified:** 97. Iván authorised the reviewed plan on15 October2026. The current proposal queue for these items is empty; the older audits and complete old/new pairs remain their dated application history.

The source and actual step commits are recorded in the application receipts above. Every approved replacement preserved all other source bytes; the source/output check was repeated against the final composed main tree. [Joint application record](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#owner-authorised-application-complete-15-october-2026).

Current protected EP README blob after the approved append-only addition: `9bd2c1d10a8d440fa947abb7bc834d99ec97ff9b`. This dated owner-authorised application follows the12 October control entry without changing that historical record.


## Execution reaudit 15 October 2026

The approved EP addition97 is exact and append-only: source predecessor `9767ec8efb7d3a2875866ea3cd22ebc94882e930`, current `9bd2c1d10a8d440fa947abb7bc834d99ec97ff9b`, step `413208033cd6b92c9982adc3cfff0fa5161a3995`. All previous EP bytes remain its exact prefix; the new note directs readers to the already approved S10 working successor without rewriting the frozen study authority. The EA entry and Development Strategy are unchanged. [Joint re-audit](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#execution-reaudit-15-october-2026) verifies all approved source pairs and identifies three corrected review-projection defects; it makes no new canonical application.

### Proposal114 — central control successor

**State:** Applied — 15 October 2026; the later owner-authorised application below completes this control entry. **Impact:** Medium. **Risk:** Low. **Effort:** Low. **Priority:** First control follow-up. The benefit is a correct current-EP certification in the one existing central control. The risk is confusing a dated source certification with scientific approval; the proposed section names the exact source and documentary scope. Cost covers checking the source identities, EOF and links, then inverse/readback verification. Dependency:97 is already applied. No file move, new owner or hierarchy change is proposed.

Source: `DOCUMENT_CONTROL.md`, blob `e3ada85de309e7f654bbf74f4b1785cde51fb245` at `6dd9edc87070b38d3c84021f7389e07596b9d1ad`. Location: EOF, after section33. The complete existing final section below occurs once and is unchanged; the only proposed addition is section34. Instructions from Iván: audit all execution, preserve all information, and keep exact old/new proposals in the owning VNext. A new source change requires his concrete decision.

**Texto antes — complete current EOF context**

````text
## 33. 14 October 2026 — owner-requested expanded Flores corrective audit

The existing campaign gains an [expanded corrective audit](./research/ecosystem-awareness/campaigns-in-development/flores-population-ea/audit/EXPANDED_AUDIT_2026-10-14.md), a pinned predecessor baseline, stricter verifier, adversarial probes and an authored proof-checker successor. The owner asks to expand and resolve audits while preserving complete information. Every replaced record and previous verifier is retained as the identical blob in history/versions; original scientific source, fixture/code/calibration data and mock checker stay unchanged. The existing campaign/README ownership and source freezes do not change. Stage A/B/C promotion, native execution and independent acceptance remain prohibited without their own evidence. The dated source freshness cut and prospective blind/readiness contract close preparation issues without fabricating missing external results or private binaries.
````

**Texto después — complete context plus proposed appendix**

````text
## 33. 14 October 2026 — owner-requested expanded Flores corrective audit

The existing campaign gains an [expanded corrective audit](./research/ecosystem-awareness/campaigns-in-development/flores-population-ea/audit/EXPANDED_AUDIT_2026-10-14.md), a pinned predecessor baseline, stricter verifier, adversarial probes and an authored proof-checker successor. The owner asks to expand and resolve audits while preserving complete information. Every replaced record and previous verifier is retained as the identical blob in history/versions; original scientific source, fixture/code/calibration data and mock checker stay unchanged. The existing campaign/README ownership and source freezes do not change. Stage A/B/C promotion, native execution and independent acceptance remain prohibited without their own evidence. The dated source freshness cut and prospective blind/readiness contract close preparation issues without fabricating missing external results or private binaries.


## 34. 15 October 2026 — approved UC-21/DDS literal application and protected EP successor

Iván authorised the reviewed literal plan on 15 October. The [application record](./research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#owner-authorised-application-complete-15-october-2026) identifies 32 local passage replacements in 14 existing documents, the one approved paragraph in the official UC-21 Issue, and the separately approved custody of 48 exact original source-edition files. Their source and step commits are recorded in the existing VNext; no prior file was deleted, moved or renamed and no VNext was created.

**Current protected EP README blob: `9bd2c1d10a8d440fa947abb7bc834d99ec97ff9b`.** Proposal 97 appended only its approved S10 working-successor reading note in commit `413208033cd6b92c9982adc3cfff0fa5161a3995`; every predecessor byte remains the exact prefix. This dated successor supersedes the current-EP certification in section 26, whose `9767ec8efb7d3a2875866ea3cd22ebc94882e930` blob remains the correct 12 October historical edition. The protected EA entry README and Development Strategy remain unchanged by this application.

The maintained reader route is UC-21 → objectives → Challenges → DDS → campaigns and results. The source-edition package is historical custody, not a second current method or case owner. Programs, earlier binaries, results and frozen manifests remain unchanged. The [execution re-audit](./research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#execution-reaudit-15-october-2026) distinguishes completion of this literal application from the still-open historical/material reception work and future per-campaign evidence duties.
````

Acceptance: retain every current byte as the exact prefix; add only section34 after a named approval, check the two source identities and relative links, and read the final public bytes back. The exact append-only incorporation is recorded in the later authorised application below.


## Historical remnants 15 October 2026

114 updates only the dated current-EP certification; the protected EP README and its old append-only application remain byte-identical during this batch. [Joint source and consolidation review](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#historical-remnants-15-october-2026).


### Change114 — Record the approved 15 October EP successor in the existing central document control

**State:** Applied — 15 October 2026; no further insertion pending for this item. **Impact:** Medio. **Risk:** Bajo. **Effort:** Bajo. **Priority:** Primera.

Source `DOCUMENT_CONTROL.md`, blob `e3ada85de309e7f654bbf74f4b1785cde51fb245` at `94ee2aeb8bc5d13fb7578b7cca17f890d9e3531e`. The complete old context occurs once. The after below adds text without deleting any old byte.

**Why:** The central current-EP certification identifies the actual approved main edition instead of stopping at the 12 October predecessor.

**Risk and validation:** A dated source certification could be mistaken for a new scientific approval. The append identifies the exact documentary application and keeps every historical certification and scope. Read dependencies `["97 already applied in413208033cd6b92c9982adc3cfff0fa5161a3995", "Existing application and execution-re-audit records"]`; verify the complete predecessor, relative links, inverse and final public bytes.

**Texto antes — completo**

~~~~~~~~text
## 33. 14 October 2026 — owner-requested expanded Flores corrective audit

The existing campaign gains an [expanded corrective audit](./research/ecosystem-awareness/campaigns-in-development/flores-population-ea/audit/EXPANDED_AUDIT_2026-10-14.md), a pinned predecessor baseline, stricter verifier, adversarial probes and an authored proof-checker successor. The owner asks to expand and resolve audits while preserving complete information. Every replaced record and previous verifier is retained as the identical blob in history/versions; original scientific source, fixture/code/calibration data and mock checker stay unchanged. The existing campaign/README ownership and source freezes do not change. Stage A/B/C promotion, native execution and independent acceptance remain prohibited without their own evidence. The dated source freshness cut and prospective blind/readiness contract close preparation issues without fabricating missing external results or private binaries.

~~~~~~~~

**Texto después — completo**

~~~~~~~~text
## 33. 14 October 2026 — owner-requested expanded Flores corrective audit

The existing campaign gains an [expanded corrective audit](./research/ecosystem-awareness/campaigns-in-development/flores-population-ea/audit/EXPANDED_AUDIT_2026-10-14.md), a pinned predecessor baseline, stricter verifier, adversarial probes and an authored proof-checker successor. The owner asks to expand and resolve audits while preserving complete information. Every replaced record and previous verifier is retained as the identical blob in history/versions; original scientific source, fixture/code/calibration data and mock checker stay unchanged. The existing campaign/README ownership and source freezes do not change. Stage A/B/C promotion, native execution and independent acceptance remain prohibited without their own evidence. The dated source freshness cut and prospective blind/readiness contract close preparation issues without fabricating missing external results or private binaries.


## 34. 15 October 2026 — approved UC-21/DDS literal application and protected EP successor

Iván authorised the reviewed literal plan on 15 October. The [application record](./research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#owner-authorised-application-complete-15-october-2026) identifies 32 local passage replacements in 14 existing documents, the one approved paragraph in the official UC-21 Issue, and the separately approved custody of 48 exact original source-edition files. Their source and step commits are recorded in the existing VNext; no prior file was deleted, moved or renamed and no VNext was created.

**Current protected EP README blob: `9bd2c1d10a8d440fa947abb7bc834d99ec97ff9b`.** Proposal 97 appended only its approved S10 working-successor reading note in commit `413208033cd6b92c9982adc3cfff0fa5161a3995`; every predecessor byte remains the exact prefix. This dated successor supersedes the current-EP certification in section 26, whose `9767ec8efb7d3a2875866ea3cd22ebc94882e930` blob remains the correct 12 October historical edition. The protected EA entry README and Development Strategy remain unchanged by this application.

The maintained reader route is UC-21 → objectives → Challenges → DDS → campaigns and results. The source-edition package is historical custody, not a second current method or case owner. Programs, earlier binaries, results and frozen manifests remain unchanged. The [execution re-audit](./research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md#execution-reaudit-15-october-2026) distinguishes completion of this literal application from the still-open historical/material reception work and future per-campaign evidence duties.

~~~~~~~~

**Iván's instruction:** Ahora debes volver al principio y volver a revisar TBS, todos los documentos, el for, todo lo anterior, a ver si se ha perdido algo, si los cambios, etcétera, etcétera, y hacer esas inserciones con cuidado. Con mucho cuidado ahí ahora aplica todos los pasos anteriores, pero con el remanente que hayas encontrado, asegurándote que finalmente solo insertas exactamente quirúrgicamente si te has dejado algo más.


### Historical remnant application114 — 15 October 2026

Applied the complete reviewed addition to `DOCUMENT_CONTROL.md`. Predecessor `e3ada85de309e7f654bbf74f4b1785cde51fb245`; successor `fdffd2ace15ed01ee9b9d9998d1ec27c1ba725d9`; exact inverse restores the complete predecessor. Every byte outside this insertion is unchanged. The dated old/new pair above is application history, not a pending proposal. Public verification follows in the joint completion record.


## Historical remnant insertions verified 15 October 2026

Applied and read back exactly on main: 114. The old source text, all original files and modes, prior destinations, scientific records and frozen packages are preserved. No new VNext or physical reorganisation.

- Change114: [exact application](https://github.com/dakleyer/structural-awareness-contributions/commit/2817f22aff28aca84eff2dab389fbf35eb82cb47).
