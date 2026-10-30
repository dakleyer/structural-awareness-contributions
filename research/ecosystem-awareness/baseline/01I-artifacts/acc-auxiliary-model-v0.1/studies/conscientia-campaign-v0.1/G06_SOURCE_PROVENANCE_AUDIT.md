# G-06 — Trazabilidad de las fuentes de Conscientia / ACC

**Corte histórico base: 26-10-2026. Conciliación: 30-10-2026.** Registro de evidencia, no una nueva revisión del contenido de Google Docs ni certificación histórica de acceso. Este documento acompaña `SOURCE_REGISTER.json`, el [libro de alegaciones de revisión](SOURCE_REVIEW_CLAIMS.json) y la [función de trazabilidad verificable](source_provenance.py).

## 1. Significado de los tres estados que antes se mezclaban

| Magnitud | Cifra del corte | Fundamento y límite |
|---|---:|---|
| **Fuentes registradas** | **23** | 19 referencias a Google Docs + 4 referencias de GitHub en `SOURCE_REGISTER.json`; no prueba lectura |
| **Google Docs con texto revisado según informe colectivo original** | **17 de 19** | README §1 del corte inicial. No existe en este registro una atestación individual con snapshot/revisor/fecha para cada una. La pertenencia se infiere por exclusión de las dos excepciones nombradas |
| **Excepciones catalogadas por metadatos en el corte inicial** | **2** | `CE-MH-ONEPAGER` y `CE-PRESCIENCE` |
| **Revisión conceptual posterior declarada** | **2** | `SOURCE_COVERAGE_AND_BACKLOG.md` (actualización del 29-10) informa de cribado conceptual posterior de ambas excepciones, sin instantánea archivada que permita acreditar retrospectivamente una lectura completa |
| **Revisión histórica atestiguada por documento individual en este registro** | **0** | Es una cuenta de pruebas documentales independientes, no prueba de que nadie haya leído las fuentes |
| **Fuentes primarias explícitas para casos congelados** | **10** | Derivadas de `CASE_REGISTRY.json.primary_source_id`, **60 casos** |
| **Fuentes diferentes citadas directamente en ambos registros** | **13** | Unión de diez fuentes primarias y `ORIGINAL_EXPERIMENTS.json.source_refs`, **40 casos narrativos**; no se infiere uso de títulos, roles ni tablas contextuales |
| **Párrafos S1 internos** | **12** | `S1-Pxxxx` resueltos y comprobados en `model/01_NOTAS_COMPLETAS.md`. Son anclas de otro artefacto interno, no un 24.º documento del registro |

**La cifra histórica `source_documents_screened=23` está mal rotulada.** Era `len(SOURCE_REGISTER["sources"])`, es decir, 23 **entradas registradas**. Se conserva sin alteración en `REFERENCE_SYNTHETIC_RESULTS.json`, como evidencia del resultado congelado, pero no se publica como «23 documentos leídos» en una ejecución nueva.

## 2. Matriz fuente por fuente, con uso calculado

`R` = revisión textual informada de forma colectiva en la base, sin prueba individual. `M→C` = solo metadatos inicialmente, cribado conceptual posterior informado sin snapshot. `N/A` = referencia GitHub fuera de la población de 19 Google Docs. Los dos últimos campos son **número de referencias de casos**, no número de lecturas.

| ID de fuente | Tipo | Revisión documentada | Casos principales (60) | Casos narrativos (40) |
|---|---|---|---:|---:|
| `CE-NOTES` | Google Doc | R | 10 | 5 |
| `CE-SOLIDARITY-V3` | Google Doc | R | 0 | 0 |
| `CE-DIALOGUE-V4` | Google Doc | R | 5 | 0 |
| `CE-SCHEME` | Google Doc | R | 10 | 0 |
| `CE-ANTS` | Google Doc | R | 0 | 1 |
| `CE-CAPACITY` | Google Doc | R | 5 | 4 |
| `CE-CORRESPONDENCE` | Google Doc | R | 5 | 3 |
| `CE-SOCIAL-WORK` | Google Doc | R | 5 | 3 |
| `AG-D01` | Google Doc | R | 5 | 1 |
| `AG-D02` | Google Doc | R | 0 | 0 |
| `HID-D06` | Google Doc | R | 0 | 2 |
| `IF-D10` | Google Doc | R | 5 | 0 |
| `CC-D17` | Google Doc | R | 5 | 0 |
| `HID-D20` | Google Doc | R | 0 | 0 |
| `ENT-DIST` | Google Doc | R | 0 | 0 |
| `ENT-AUDIT` | Google Doc | R | 0 | 0 |
| `CE-MH-NOTE` | Google Doc | R | 5 | 0 |
| `CE-MH-ONEPAGER` | Google Doc | M→C | 0 | 0 |
| `CE-PRESCIENCE` | Google Doc | M→C | 0 | 0 |
| `00M-CANON` | GitHub | N/A | 0 | 0 |
| `01K-HID` | GitHub | N/A | 0 | 0 |
| `UC21-SOURCE` | GitHub | N/A | 0 | 0 |
| `ACC-EXAMPLES` | GitHub | N/A | 0 | 6 |

**Precisión:** una referencia con cero casos directos puede constituir un contrato semántico, una fuente de contexto o un expediente de medición todavía no instrumentalizado. Cero referencias explícitas no significa que no se consultara o que sea irrelevante. En particular, `00M-CANON`, `01K-HID` y `UC21-SOURCE` conservan su autoridad en sus dominios, aunque no aparezcan como `primary_source_id` de la matriz sintética de 60 casos.

## 3. Modelo ejecutable y controles de integridad

El [evaluador G-06](source_provenance.py) es la única fuente para la cifra **vigente** del informe de campaña: lee registros, comprueba que los 23 IDs están cubiertos exactamente una vez, verifica el tipo por URL y valida que `primary_source_id` y `source_refs` sean identificadores existentes. Las 12 anclas S1 se cotejan contra el comentario y el ancla del documento original. Las referencias desconocidas, duplicadas o con tipo cambiado son errores de integridad.

La cuenta de casos se **deriva**, no se copia a las fuentes, por lo que añadir o corregir un `primary_source_id` cambia automáticamente el informe. No se acreditan inspecciones retroactivas: para promover una fuente a «revisión individual verificable» deben aportarse una versión/exportación autorizada, hash SHA-256 de esa versión, fecha de inspección y responsable; si falta cualquiera, la validación falla. No se ha creado ningún hash ficticio de Google Docs. Los cinco insumos del informe (registro, libro de alegaciones, 60 casos, 40 casos y notas S1) tienen su hash local reproducible.

El informe expone `source_provenance.counts`, `source_level_lineage`, `internal_paragraph_lineage` y `source_input_sha256`. La estructura separa explícitamente **registrado / revisión textual informada / revisión posterior informada / uso directo por caso**. También conserva exactamente las 23 fuentes registradas aunque la evidencia de uso sea parcial.

## 4. Compatibilidad y valor de auditoría

- **No se modifican** los 60 resultados sintéticos, los 40 ejemplos de #68, los 30 escenarios agénticos, las pruebas de #70, los permisos, A/B/C/D, FH-C, ni los objetivos de los participantes.
- El fichero congelado `REFERENCE_SYNTHETIC_RESULTS.json` se conserva intacto; `verify_campaign.py` compara las salidas originales y reconcilia explícitamente su clave erróneamente nombrada.
- El README y la matriz de cobertura reciben una nota cronológica: el texto posterior del 29-10 **no convierte** el corte 17/19 del 26-10 en 19 lecturas completas verificadas.
- La CI reconstruye el registro/casos desde `bootstrap.py`, verifica que no haya divergencia, ejecuta los tests, regenera el JSON vigente y publica un artefacto de trazabilidad. El avance de revisión documental se puede versionar después con evidencia por fuente.

**Estado científico:** respuesta a G-06 y a la incompatibilidad de cifras históricas; una auditoría independiente aún debe comprobar la calidad de los soportes de lectura antes de cerrar el hallazgo. El resultado es un inventario y un grafo de referencias, no una validación empírica de las hipótesis de Conscientia.
