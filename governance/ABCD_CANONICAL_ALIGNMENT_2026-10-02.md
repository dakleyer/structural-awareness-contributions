# A/B/C/D — alineación canónica del corpus

**Fecha:** 2 de octubre de 2026. **Base revisada:** `66dbe8134e1fd5fbc586152a8129615898052485`. **Autorización:** Iván solicita enlaces a 00M y correcciones mínimas de A/B/C/D en todo el corpus, incluida Fundación.

La definición semántica común es [00M v0.8, §1](../research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical). Adoptarla como vocabulario del corpus no eleva su argumento científico por encima de plausibilidad matemática. 00N conserva su función de puente condicional hacia los requisitos.

## 1. Decisiones y plan antes/después

| Área | Antes | Después | Límite de la modificación |
|---|---|---|---|
| Autoridad semántica | Topología y otros documentos reproducían definiciones propias; 00M decía «proposed canonical». | 00M §1 es la definición canónica adoptada; un ancla estable permite enlazarla. | Se adopta vocabulario; no se prueba viabilidad, cumplimiento ni TRL. |
| Fundación | Conviven «determinado/no resuelto» y B=confianza, C=capacidad adicional. | La entrada y el glosario remiten a 00M; los pasajes de fuente conservados se identifican como vocabulario histórico. | La derivación fuente y Ω/U/R_U/Type 0–2 se conservan. |
| A | A podía leerse como certidumbre o tipo de dato. | Resultado funcional entregado por el proceso; puede ser probabilidad o estimación. | No convierte una afirmación ajena en verdad del receptor. |
| B | Frecuentemente sólo confianza/intensidad. | Base, límites y reserva de explotación caracterizada, con evaluación defendible aunque no ejecutada. | No exige estimaciones numéricas inventadas ni una escala universal. |
| C | Comprobaciones, sensores o registros disponibles pero no consultados. | Frontera exploratoria fundamentada cuya base de evaluación aún falta. Los checks caracterizados quedan en B. | Desconocer el resultado no equivale a carecer de método de evaluación. |
| D | Residuo, desconocimiento o incapacidad de control mezclados. | Efecto potencialmente material fuera de vías efectivas de evaluación en ese marco. | Un efecto cuantificado pero incontrolable puede ser A/B; UNKNOWN no se fuerza a D. |
| Cartografía / MSCA / RA / reposicionamiento | Proyecciones repetían la antigua B/C. | Se alinean definiciones y usos locales; confianza queda como cualificador de B y no como B completo. | Se mantienen dueños, autoridades, objetos y circuito arquitectónico. |
| Gradiente | C podía parecer una oportunidad ya activable y calculable. | Se separa evaluación de B de exploración hacia una base aún ausente en C. | Las expresiones de un perfil no cuantifican C/D abiertos; no se añade una prueba de validez. |
| 04 contrato de entrada | «Vía disponible no usada» podía clasificar automáticamente como C. | Q5, N04 y ejemplos aplican la frontera B/C; las asignaciones de la matriz quedan condicionadas a esa base. | Se conservan 176 nombres/entradas fuente y N01–N13; la enmienda lleva identificador `ABCD-00M08-2026-10-02`. No se migran mensajes antiguos. |
| 00G | Verificación conocida bajo C. | Se conserva esa lista como reserva B y se añade un ejemplo real de frontera C. | Fixture, oráculo, comparadores, gates y resultados no cambian. La métrica histórica B/C requiere correspondencia antes de reutilizarse. |
| Pruebas 02A/02B y mapa de evidencia | El vocabulario de la gramática podía confundirse con la definición vigente. | Aviso explícito sobre alcance histórico y correspondencia semántica pendiente. | Ningún resultado de cierre sintáctico se declara revalidado por añadir un enlace. |
| Fuentes históricas y auditorías | Sus antiguas definiciones podían reaparecer como actuales. | Nota de lectura en versiones textuales; snapshots preservados remitidos desde su índice. | Las afirmaciones históricas no se reescriben como si siempre hubieran usado 00M. |
| Ayudas visuales | 00G reproducía la antigua C; 00E podía parecer la taxonomía actual. | 00G se alinea; 00E se identifica como mapa histórico de fallos; figuras autónomas y galería enlazan a 00M. | Se preserva la función del mapa I/O y Type 1/2. |
| Exportaciones Word/PPTX/PDF | Los binarios publicados preceden a 00M. | Avisos junto a rutas de lectura y en el manifiesto de presentaciones. | Los binarios permanecen intactos; no se afirma que hayan sido regenerados o corregidos internamente. |

## 2. Antes y después exactos

El [diff íntegro](./ABCD_CANONICAL_ALIGNMENT_2026-10-02.patch) muestra cada sustitución y adición contra la base indicada, con contexto y sin omitir las filas de la matriz. Es el registro preciso para revisión, aplicación selectiva o reversión. El [inventario verificable](./ABCD_CANONICAL_ALIGNMENT_2026-10-02.json) registra blobs, archivos y exclusiones. Los cambios se prepararon como sustituciones exactas antes de aplicarse; una segunda reconstrucción confirmó que sólo esas sustituciones producen los archivos finales.

## 3. Comprobación integral

- Inventario de 444 documentos Markdown en la copia de la base; 92 documentos con coincidencias directas y 6 candidatos adicionales examinados por vocabulario de polos/proyecciones. La búsqueda distingue letras de pruebas, bucles y componentes S/E/C/P/M.
- 91 archivos existentes modificados: cambios de definición, avisos o enlaces. No hay movimientos, renombrados ni borrados.
- 246 sustituciones exactas registradas; reconstrucción completa desde la base: **PASS**.
- 101 enlaces relativos a 00M comprobados en los archivos modificados; destino y ancla estable: **PASS**.
- Encabezados de los tres README protegidos/comparados: idénticos a la base. SHAs de EA/EP actualizados en DOCUMENT_CONTROL.
- Las 176 entradas fuente del contrato 04, con sus nombres e identificadores, se conservan exactamente. N01–N13 mantienen sus identificadores.
- Requisitos canónicos: blob `4fe3d69b50fef1e82ba7f889324b70a7f6b1a81c` **sin cambios**. S/T/H/KPI no se renumeran ni se redefinen.
- 778 archivos materializados fuera del conjunto de cambios comparados con su blob de la base: **idénticos**. El resto de los blobs del árbol base se preserva al publicar sobre ese árbol.
- Los SVG modificados se analizaron como XML. Los dos cuadros de escenarios se renderizaron y revisaron; no se realizó un rediseño general de los gráficos históricos.
- Las 21 exportaciones DOCX/PPTX/PDF fueron cotejadas por SHA y se extrajo su texto para buscar referencias. Los binarios no se modifican.

Comprobación de rutas sobre el árbol completo: **1.922 referencias locales examinadas, cero rutas nuevas rotas y cero referencias a encabezados eliminados**.

Esta auditoría verifica conservación textual, referencias y coherencia de los pasajes A/B/C/D revisados. No es una ejecución experimental ni una nueva demostración del sistema.

## 4. Fronteras que quedan expresas

**Gramática y evidencia histórica.** 02B y su fixture conservan una gramática con B «unresolved» y C «potentially knowable». El nuevo enlace no demuestra equivalencia con reserva caracterizada/frontera exploratoria. Si se quiere trasladar el teorema semántico a 00M, deberá revisarse esa correspondencia; no se cambia ahora el resultado registrado ni se inventa validación.

**Perfiles de intercambio.** Un emisor antiguo con C=check conocido pendiente necesita un mapeo/versionado explícito. Las 176 correspondencias siguen siendo condicionales al perfil; no se afirma haber clasificado 176 productores reales. N11 sigue impidiendo inferir una versión desconocida por semejanza.

**Exportaciones.** Los decks y el Word anteriores se conservan como versiones fechadas. El Markdown y 00M gobiernan la lectura vigente. Su regeneración y comprobación de formato sería una actualización de esos artefactos, no una condición oculta para leer esta corrección.

**Otras letras.** H-00H-A/B/C/D, planes A/B, bucles/axes A/B y C de Coordination scope no se renombraron. El desconocimiento del tipo de productor sigue siendo distinto del desconocimiento de su papel A/B/C/D.

## 5. Archivos con cambios

| Archivo | Intervención |
|---|---|
| [DOCUMENT_CONTROL.md](../DOCUMENT_CONTROL.md) | Aviso de lectura y enlace; resto conservado |
| [README.md](../README.md) | Ajuste localizado / enlace; ver diff |
| [architectural-contributions/ecosystem-positioning/01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md](../architectural-contributions/ecosystem-positioning/01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md) | Ajuste localizado / enlace; ver diff |
| [architectural-contributions/ecosystem-positioning/README.md](../architectural-contributions/ecosystem-positioning/README.md) | Ajuste localizado / enlace; ver diff |
| [governance/CORPUS_INFORMATION_CONSERVATION_AUDIT_2026-09-23.md](../governance/CORPUS_INFORMATION_CONSERVATION_AUDIT_2026-09-23.md) | Aviso de lectura y enlace; resto conservado |
| [governance/CUMULATIVE_INTEGRATION_AUDIT_2026-09-23.md](../governance/CUMULATIVE_INTEGRATION_AUDIT_2026-09-23.md) | Aviso de lectura y enlace; resto conservado |
| [governance/ECOSYSTEM_AWARENESS_LINKED_DOCUMENT_AUDIT_2026-09-25.md](../governance/ECOSYSTEM_AWARENESS_LINKED_DOCUMENT_AUDIT_2026-09-25.md) | Aviso de lectura y enlace; resto conservado |
| [governance/ECOSYSTEM_POSITIONING_LINKED_DOCUMENT_AUDIT_2026-09-25.md](../governance/ECOSYSTEM_POSITIONING_LINKED_DOCUMENT_AUDIT_2026-09-25.md) | Aviso de lectura y enlace; resto conservado |
| [governance/MSCA_LINKED_DOCUMENT_AUDIT_2026-09-25.md](../governance/MSCA_LINKED_DOCUMENT_AUDIT_2026-09-25.md) | Aviso de lectura y enlace; resto conservado |
| [governance/REGIME_AWARENESS_LINKED_DOCUMENT_AUDIT_2026-09-25.md](../governance/REGIME_AWARENESS_LINKED_DOCUMENT_AUDIT_2026-09-25.md) | Aviso de lectura y enlace; resto conservado |
| [governance/preserved-public-snapshots/README.md](../governance/preserved-public-snapshots/README.md) | Aviso de lectura y enlace; resto conservado |
| [presentations/ecosystem-positioning/PRESENTATION_MANIFEST.md](../presentations/ecosystem-positioning/PRESENTATION_MANIFEST.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/README.md](../research/ecosystem-awareness/README.md) | Ajuste localizado / enlace; ver diff |
| [research/ecosystem-awareness/SCENARIO_READER_GUIDE_2026-09-25.md](../research/ecosystem-awareness/SCENARIO_READER_GUIDE_2026-09-25.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/WORKPLAN.md](../research/ecosystem-awareness/WORKPLAN.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md](../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) | Ajuste localizado / enlace; ver diff |
| [research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md](../research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_v0.3_DRAFT_ECOSYSTEM_POSITIONING.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/00E_A01_MICROSOFT_AGENT_365_IMPLEMENTATION_PROFILE_v0.1.md](../research/ecosystem-awareness/baseline/00E_A01_MICROSOFT_AGENT_365_IMPLEMENTATION_PROFILE_v0.1.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/00E_A01_MICROSOFT_AGENT_365_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md](../research/ecosystem-awareness/baseline/00E_A01_MICROSOFT_AGENT_365_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md](../research/ecosystem-awareness/baseline/00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.1.md](../research/ecosystem-awareness/baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.1.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.2.md](../research/ecosystem-awareness/baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.2.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.2_DRAFT.md](../research/ecosystem-awareness/baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.2_DRAFT.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.3_DRAFT.md](../research/ecosystem-awareness/baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.3_DRAFT.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md](../research/ecosystem-awareness/baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md) | Ajuste localizado / enlace; ver diff |
| [research/ecosystem-awareness/baseline/00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.2_DRAFT.md](../research/ecosystem-awareness/baseline/00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.2_DRAFT.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/00G_HF_ROADMAP_R123_EA_COMPOSITIONS_UC4_v0.1_DRAFT.md](../research/ecosystem-awareness/baseline/00G_HF_ROADMAP_R123_EA_COMPOSITIONS_UC4_v0.1_DRAFT.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/00K_A17_DOCUMENTATION_REPRODUCIBILITY_AND_PROOF_MAP_v0.1.md](../research/ecosystem-awareness/baseline/00K_A17_DOCUMENTATION_REPRODUCIBILITY_AND_PROOF_MAP_v0.1.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/00K_A21_REQUIREMENT_BASIS_CLOSURE_AND_RELATIVE_COMPLETENESS_PROOF_v0.1.md](../research/ecosystem-awareness/baseline/00K_A21_REQUIREMENT_BASIS_CLOSURE_AND_RELATIVE_COMPLETENESS_PROOF_v0.1.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/00K_A24_PRINCIPLE_REQUIREMENT_INFORMATION_GAIN_AND_NON_EQUIVALENCE_v0.1.md](../research/ecosystem-awareness/baseline/00K_A24_PRINCIPLE_REQUIREMENT_INFORMATION_GAIN_AND_NON_EQUIVALENCE_v0.1.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_00G_TRAZA_PAPEL_EMPAREJADA_v0.1.md](../research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_00G_TRAZA_PAPEL_EMPAREJADA_v0.1.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.6_RESEARCH_NOTE.md](../research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.6_RESEARCH_NOTE.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md](../research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) | Ajuste localizado / enlace; ver diff |
| [research/ecosystem-awareness/baseline/00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.5_RESEARCH_NOTE.md](../research/ecosystem-awareness/baseline/00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.5_RESEARCH_NOTE.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/00_CANONICAL_ARCHITECTURE_TOPOLOGY.md](../research/ecosystem-awareness/baseline/00_CANONICAL_ARCHITECTURE_TOPOLOGY.md) | Ajuste localizado / enlace; ver diff |
| [research/ecosystem-awareness/baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md](../research/ecosystem-awareness/baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/01A_FOUNDATIONAL_DUAL_ORIGIN_NOTE_v0.1.md](../research/ecosystem-awareness/baseline/01A_FOUNDATIONAL_DUAL_ORIGIN_NOTE_v0.1.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/01B_EA_MSCA_INTERFACE_ANNEX_v0.2.md](../research/ecosystem-awareness/baseline/01B_EA_MSCA_INTERFACE_ANNEX_v0.2.md) | Ajuste localizado / enlace; ver diff |
| [research/ecosystem-awareness/baseline/01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.1.md](../research/ecosystem-awareness/baseline/01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.1.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md](../research/ecosystem-awareness/baseline/01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md) | Ajuste localizado / enlace; ver diff |
| [research/ecosystem-awareness/baseline/01H_PARTICIPANT_LOCAL_ECOSYSTEM_POSITIONING_AND_DECISION_SCOPED_EPISTEMIC_OPPORTUNITY_v0.1.md](../research/ecosystem-awareness/baseline/01H_PARTICIPANT_LOCAL_ECOSYSTEM_POSITIONING_AND_DECISION_SCOPED_EPISTEMIC_OPPORTUNITY_v0.1.md) | Ajuste localizado / enlace; ver diff |
| [research/ecosystem-awareness/baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md](../research/ecosystem-awareness/baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md) | Ajuste localizado / enlace; ver diff |
| [research/ecosystem-awareness/baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_DISTRIBUTED_OPPORTUNITY_v0.1.md](../research/ecosystem-awareness/baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_DISTRIBUTED_OPPORTUNITY_v0.1.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/01_FOUNDATIONAL_THEORY_v0.4.part01.md](../research/ecosystem-awareness/baseline/01_FOUNDATIONAL_THEORY_v0.4.part01.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/01_FOUNDATIONAL_THEORY_v0.4.part03.md](../research/ecosystem-awareness/baseline/01_FOUNDATIONAL_THEORY_v0.4.part03.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md](../research/ecosystem-awareness/baseline/01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md) | Ajuste localizado / enlace; ver diff |
| [research/ecosystem-awareness/baseline/02A_FOUNDATION_TO_OPERATIONAL_PRINCIPLE_DERIVATION_PROOF_v0.1.md](../research/ecosystem-awareness/baseline/02A_FOUNDATION_TO_OPERATIONAL_PRINCIPLE_DERIVATION_PROOF_v0.1.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/02B_FOUNDATIONAL_SYNTAX_CLOSURE_AND_P1_P6_NORMAL_FORM_PROOF_v0.1.md](../research/ecosystem-awareness/baseline/02B_FOUNDATIONAL_SYNTAX_CLOSURE_AND_P1_P6_NORMAL_FORM_PROOF_v0.1.md) | Ajuste localizado / enlace; ver diff |
| [research/ecosystem-awareness/baseline/02_EPISTEMIC_SAFETY_PRINCIPLES_CONTROL_MATRIX_v0.4.part01.md](../research/ecosystem-awareness/baseline/02_EPISTEMIC_SAFETY_PRINCIPLES_CONTROL_MATRIX_v0.4.part01.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/02_EPISTEMIC_SAFETY_PRINCIPLES_CONTROL_MATRIX_v0.4.part02.md](../research/ecosystem-awareness/baseline/02_EPISTEMIC_SAFETY_PRINCIPLES_CONTROL_MATRIX_v0.4.part02.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/02_EPISTEMIC_SAFETY_PRINCIPLES_CONTROL_MATRIX_v0.4.part03.md](../research/ecosystem-awareness/baseline/02_EPISTEMIC_SAFETY_PRINCIPLES_CONTROL_MATRIX_v0.4.part03.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/03_FUNCTIONAL_ARCHITECTURE_v0.4.part01.md](../research/ecosystem-awareness/baseline/03_FUNCTIONAL_ARCHITECTURE_v0.4.part01.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/03_FUNCTIONAL_ARCHITECTURE_v0.4.part02.md](../research/ecosystem-awareness/baseline/03_FUNCTIONAL_ARCHITECTURE_v0.4.part02.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/04_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.4.part01.md](../research/ecosystem-awareness/baseline/04_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.4.part01.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md](../research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md](../research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md) | Ajuste localizado / enlace; ver diff |
| [research/ecosystem-awareness/baseline/04_INPUT_INTERFACE_CONTRACT/04_INPUT_INTERFACE_CONTRACT_v0.4.md](../research/ecosystem-awareness/baseline/04_INPUT_INTERFACE_CONTRACT/04_INPUT_INTERFACE_CONTRACT_v0.4.md) | Ajuste localizado / enlace; ver diff |
| [research/ecosystem-awareness/baseline/06_ARCHITECTURE_BENCHMARK_v0.4.part02.md](../research/ecosystem-awareness/baseline/06_ARCHITECTURE_BENCHMARK_v0.4.part02.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/06_ARCHITECTURE_BENCHMARK_v0.4.part03.md](../research/ecosystem-awareness/baseline/06_ARCHITECTURE_BENCHMARK_v0.4.part03.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/07_EA_CANDIDATE_DIFFERENTIAL_HYPOTHESES_v0.5_REVIEWED_WORKING.md](../research/ecosystem-awareness/baseline/07_EA_CANDIDATE_DIFFERENTIAL_HYPOTHESES_v0.5_REVIEWED_WORKING.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/ARCHITECTURE_BENCHMARK_v0.5_REVIEWED_WORKING.md](../research/ecosystem-awareness/baseline/ARCHITECTURE_BENCHMARK_v0.5_REVIEWED_WORKING.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/CANONICAL_CORPUS_MANIFEST.md](../research/ecosystem-awareness/baseline/CANONICAL_CORPUS_MANIFEST.md) | Ajuste localizado / enlace; ver diff |
| [research/ecosystem-awareness/baseline/DEEP_CONCEPTUAL_LINEAGE_DERIVATION_MAP_v0.1.md](../research/ecosystem-awareness/baseline/DEEP_CONCEPTUAL_LINEAGE_DERIVATION_MAP_v0.1.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/EA_PARENT_INDEX_SOURCE_2026-09-15.md](../research/ecosystem-awareness/baseline/EA_PARENT_INDEX_SOURCE_2026-09-15.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/PROMPT_TO_CANON_CONSERVATION_MATRIX_v0.1.part01.md](../research/ecosystem-awareness/baseline/PROMPT_TO_CANON_CONSERVATION_MATRIX_v0.1.part01.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/README.md](../research/ecosystem-awareness/baseline/README.md) | Ajuste localizado / enlace; ver diff |
| [research/ecosystem-awareness/baseline/UC-EA-01_v0.3_FROZEN.md](../research/ecosystem-awareness/baseline/UC-EA-01_v0.3_FROZEN.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/UC-EA-01_v0.3_FROZEN.part02.md](../research/ecosystem-awareness/baseline/UC-EA-01_v0.3_FROZEN.part02.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/UC-EA-02_v0.6_MAINTENANCE_FREEZE.md](../research/ecosystem-awareness/baseline/UC-EA-02_v0.6_MAINTENANCE_FREEZE.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/UC-EA-02_v0.6_MAINTENANCE_FREEZE.part02.md](../research/ecosystem-awareness/baseline/UC-EA-02_v0.6_MAINTENANCE_FREEZE.part02.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/annexes/00G-HF-DEVELOPMENT-HISTORY-v0.1.md](../research/ecosystem-awareness/baseline/annexes/00G-HF-DEVELOPMENT-HISTORY-v0.1.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/annexes/00G-HF-EA-REQUIREMENTS-PAIRED-DESIGN-v0.1.md](../research/ecosystem-awareness/baseline/annexes/00G-HF-EA-REQUIREMENTS-PAIRED-DESIGN-v0.1.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/assets/00E/figure_00E_02_four_quadrant_map.svg](../research/ecosystem-awareness/baseline/assets/00E/figure_00E_02_four_quadrant_map.svg) | Ajuste localizado / enlace; ver diff |
| [research/ecosystem-awareness/baseline/assets/00G/3_abcd_decision_state.svg](../research/ecosystem-awareness/baseline/assets/00G/3_abcd_decision_state.svg) | Ajuste localizado / enlace; ver diff |
| [research/ecosystem-awareness/baseline/assets/00G/README.md](../research/ecosystem-awareness/baseline/assets/00G/README.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/fixtures/00K-CLOSURE/README.md](../research/ecosystem-awareness/baseline/fixtures/00K-CLOSURE/README.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/traversals/00G-HF-CONTINUOUS-SOCIAL-v0.1/PROTOCOL.md](../research/ecosystem-awareness/baseline/traversals/00G-HF-CONTINUOUS-SOCIAL-v0.1/PROTOCOL.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/traversals/00G-HF-CONTINUOUS-SOCIAL-v0.1/RESULTS.md](../research/ecosystem-awareness/baseline/traversals/00G-HF-CONTINUOUS-SOCIAL-v0.1/RESULTS.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/traversals/00G-HF-DYNAMIC-REVIEW-v0.1/PROTOCOL.md](../research/ecosystem-awareness/baseline/traversals/00G-HF-DYNAMIC-REVIEW-v0.1/PROTOCOL.md) | Aviso de lectura y enlace; resto conservado |
| [research/ecosystem-awareness/baseline/visuals/EA_ABCD_v0.1.svg](../research/ecosystem-awareness/baseline/visuals/EA_ABCD_v0.1.svg) | Ajuste localizado / enlace; ver diff |
| [research/ecosystem-awareness/baseline/visuals/EA_MECHANISMS_v0.1.svg](../research/ecosystem-awareness/baseline/visuals/EA_MECHANISMS_v0.1.svg) | Ajuste localizado / enlace; ver diff |
| [research/ecosystem-awareness/baseline/visuals/EA_VISUAL_READING_AIDS_v0.1.html](../research/ecosystem-awareness/baseline/visuals/EA_VISUAL_READING_AIDS_v0.1.html) | Ajuste localizado / enlace; ver diff |
| [research/ecosystem-awareness/fg-tida/charter/THEME_13_WORKING_GROUP_CHARTER_PREPARATION_DRAFT_v0.2.md](../research/ecosystem-awareness/fg-tida/charter/THEME_13_WORKING_GROUP_CHARTER_PREPARATION_DRAFT_v0.2.md) | Ajuste localizado / enlace; ver diff |
| [research/ecosystem-awareness/fg-tida/charter/WG13_v0.2_REVIEW_AND_COMPATIBILITY_2026-09-28.md](../research/ecosystem-awareness/fg-tida/charter/WG13_v0.2_REVIEW_AND_COMPATIBILITY_2026-09-28.md) | Aviso de lectura y enlace; resto conservado |
| [research/regime-awareness/README.md](../research/regime-awareness/README.md) | Ajuste localizado / enlace; ver diff |
| [research/regime-awareness/minimalistic-early-warning-systems/README.md](../research/regime-awareness/minimalistic-early-warning-systems/README.md) | Ajuste localizado / enlace; ver diff |
| [standards/minimum-sufficient-control/00_CANONICAL_MSCA_ARCHITECTURE.md](../standards/minimum-sufficient-control/00_CANONICAL_MSCA_ARCHITECTURE.md) | Ajuste localizado / enlace; ver diff |
| [standards/minimum-sufficient-control/02_MSCA_ARCHITECTURAL_ROLE.md](../standards/minimum-sufficient-control/02_MSCA_ARCHITECTURAL_ROLE.md) | Aviso de lectura y enlace; resto conservado |
| [standards/minimum-sufficient-control/03_MSCA_ECOSYSTEM_COMPOSITION_AND_CONTROL.md](../standards/minimum-sufficient-control/03_MSCA_ECOSYSTEM_COMPOSITION_AND_CONTROL.md) | Ajuste localizado / enlace; ver diff |
| [standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md](../standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md) | Ajuste localizado / enlace; ver diff |
| [standards/minimum-sufficient-control/README.md](../standards/minimum-sufficient-control/README.md) | Ajuste localizado / enlace; ver diff |

## 6. Exportaciones con referencias localizadas

- [presentations/ecosystem-positioning/Ecosystem_Positioning_Architecture_Implementation_Canonical_v1.1.pptx](../presentations/ecosystem-positioning/Ecosystem_Positioning_Architecture_Implementation_Canonical_v1.1.pptx) — texto anterior; consultar 00M y aviso del índice.
- [presentations/ecosystem-positioning/Ecosystem_Positioning_Architecture_Implementation_Canonical_v1.2.pptx](../presentations/ecosystem-positioning/Ecosystem_Positioning_Architecture_Implementation_Canonical_v1.2.pptx) — texto anterior; consultar 00M y aviso del índice.
- [presentations/ecosystem-positioning/Ecosystem_Positioning_Canonical.pdf](../presentations/ecosystem-positioning/Ecosystem_Positioning_Canonical.pdf) — texto anterior; consultar 00M y aviso del índice.
- [presentations/ecosystem-positioning/Ecosystem_Positioning_Canonical.pptx](../presentations/ecosystem-positioning/Ecosystem_Positioning_Canonical.pptx) — texto anterior; consultar 00M y aviso del índice.
- [presentations/ecosystem-positioning/Ecosystem_Positioning_Canonical_Ward_Discussion_v2.pptx](../presentations/ecosystem-positioning/Ecosystem_Positioning_Canonical_Ward_Discussion_v2.pptx) — texto anterior; consultar 00M y aviso del índice.
- [research/ecosystem-awareness/baseline/04_INPUT_INTERFACE_CONTRACT/04_Contrato_interfaces_entrada_EA_v0.4.docx](../research/ecosystem-awareness/baseline/04_INPUT_INTERFACE_CONTRACT/04_Contrato_interfaces_entrada_EA_v0.4.docx) — texto anterior; consultar 00M y aviso del índice.

## 7. Snapshots sin modificación

- [governance/preserved-public-snapshots/CONTROL_MATRIX_v0.4_part01_PUBLIC_MIRROR_2026-09-11.md](../governance/preserved-public-snapshots/CONTROL_MATRIX_v0.4_part01_PUBLIC_MIRROR_2026-09-11.md)
- [governance/preserved-public-snapshots/EA_BASELINE_INDEX_2026-09-19.md](../governance/preserved-public-snapshots/EA_BASELINE_INDEX_2026-09-19.md)
- [governance/preserved-public-snapshots/EA_BENCHMARK_00D_INITIAL_INTEGRATED_2026-09-17.md](../governance/preserved-public-snapshots/EA_BENCHMARK_00D_INITIAL_INTEGRATED_2026-09-17.md)
- [governance/preserved-public-snapshots/EA_PROFILE_00E_A01_INITIAL_2026-09-17.md](../governance/preserved-public-snapshots/EA_PROFILE_00E_A01_INITIAL_2026-09-17.md)
- [governance/preserved-public-snapshots/EA_SCENARIO_00E_INITIAL_2026-09-17.md](../governance/preserved-public-snapshots/EA_SCENARIO_00E_INITIAL_2026-09-17.md)
- [governance/preserved-public-snapshots/EA_TOPOLOGY_2026-09-19.md](../governance/preserved-public-snapshots/EA_TOPOLOGY_2026-09-19.md)
- [governance/preserved-public-snapshots/FUNCTIONAL_ARCHITECTURE_v0.4_part01_PUBLIC_MIRROR_2026-09-11.md](../governance/preserved-public-snapshots/FUNCTIONAL_ARCHITECTURE_v0.4_part01_PUBLIC_MIRROR_2026-09-11.md)
- [governance/preserved-public-snapshots/FUNCTIONAL_INTERFACES_v0.4_part01_FROZEN_REPAIRED_2026-09-11.md](../governance/preserved-public-snapshots/FUNCTIONAL_INTERFACES_v0.4_part01_FROZEN_REPAIRED_2026-09-11.md)
- [governance/preserved-public-snapshots/FUNCTIONAL_INTERFACES_v0.4_part01_PUBLIC_MIRROR_2026-09-11.md](../governance/preserved-public-snapshots/FUNCTIONAL_INTERFACES_v0.4_part01_PUBLIC_MIRROR_2026-09-11.md)
