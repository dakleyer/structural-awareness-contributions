> **Estado de lectura: HISTORIA / AUDITORÍA DE SU CORTE.** El diseño vigente es [R2 → freeze → R3](./runtime-context/PRINCIPIO_R2_FREEZE_R3_2026-10-13.md). Consulte [las versiones y decisiones](./VERSIONS_AND_DECISIONS_2026-10-13.md) y [la trazabilidad](./TRACEABILITY_2026-10-13.md). El texto anterior se conserva completo debajo; sus antiguas prioridades no gobiernan la continuación. No contiene resultados nativos de la nueva instancia.

# Auditoría integral de trazabilidad y cambio metodológico — FLORES, 13 octubre 2026

**Alcance:** dossier propio `research/ecosystem-awareness/campaigns-in-development/flores-population-ea/`, método canónico DDS, fuentes originales Theme #21/CTGT/UC-4/UC-21, biblioteca RESIDENCIA (documentación del 11–12 oct) y obligaciones del usuario.  
**Tipo:** revisión por el mismo asistente que participó en la reconstrucción anterior, **NO auditoría independiente**.  
**Corte GitHub externo:** 13 octubre 2026; fuente Flores `Himalogic/FG-TIDA-analysis` head `07ac94fb100975bfff2e8ab0c644bd02ec87e537` (los dos blobs de `planted-judge/` permanecen iguales).  
**Criterio de aprobación:** adecuación documental/linaje, no Stage A científica ni verificación de implementación.

## I. Hallazgo crítico: el drift de aproximación no tenía expediente propio

La primera publicación de campaña, aunque incorporó P0–P3, v0.2–v0.5 y los controles de fuentes, narraba el trabajo **como una cadena de revisiones documentales**. No registraba claramente la **decisión del 12 octubre de abandonar el crecimiento de un benchmark autocentrado para examinar un único cambio controlado dentro de la continuación natural de Flores**, con pérdida y recuperación de apoyo a una inferencia del receptor, costos y B2 equiparado. El documento también podía leerse como si “v0.5 de siete casos” fuese el experimento principal definitivo, ignorando la decisión posterior de reentrada mínima UC17-08.

**Corrección documental:** [APPROACH_DRIFT_2026-10-12_13.md](APPROACH_DRIFT_2026-10-12_13.md) hace explícito el antes/después, instrucciones del titular de investigación, causa del giro, legado a conservar, fronteras y estado. [PRIMARY_TRIAL_PROTOCOL_DRAFT_v0.1.md](PRIMARY_TRIAL_PROTOCOL_DRAFT_v0.1.md) da una secuencia que podría transformarse en Run Card, con un solo cambio causal en adaptador y control de recuperación. La v0.5 sigue preservada y no se edita su fuente.

## II. Hallazgos de integridad, ciencia y proceso

| ID | Severidad | Hallazgo | Decisión en esta revisión |
|---|---|---|---|
| **F-A01** | CRÍTICA | **D0 drift de estrategia** no trazado como evento de decisión distinto de D3 cambio real de identificabilidad | Documento de pivot y estado añadido; sin atribuir D3 no observado |
| **F-A02** | CRÍTICA | Q0→Q1 (nueva pregunta), UC17-08 ausencia→permit (corrupción del consumidor) y real R3 mismo-claim se estaban aproximando como “drift” indiferenciado | Separamos D1/D2/D3, con negativos y condiciones de observabilidad |
| **F-A03** | ALTA | P0–P3 autoajuste/recuperación como ambición original, pero viejo Q-bind per-round aleatorio ya caracterizable; riesgo de descartar todo el objetivo o darlo falsamente por cumplido | Conservamos la ambición y sus negativas; reconstrucción nueva t0/t1/t2 se limita al *handoff* semántico |
| **F-A04** | ALTA | v0.5 corrección de auditoría puede confundirse con última decisión de ejecución, aunque después se privilegió un ensayo mínimo fuente-nativo | v0.5 `CANDIDATE_UNFROZEN` como control y posible lote futuro, ensayo mínimo identificado como prioridad prospectiva |
| **F-A05** | ALTA | “Totalmente trazable” no se cumplía: seis archivos históricos eran resúmenes, no el texto recuperado íntegro | Ahora se publica el **texto legible completo** de seis fuentes originales (11–12 oct), con manifiesto de origen; ver III |
| **F-A06** | ALTA | Archivo ZIP v0.2/v0.5 completo y binarios PDF no recuperados, aunque fuentes se nombraban | Registro explícito de falta de paridad original y paquetes privados; ninguna falsa huella de ZIP verificado |
| **F-A07** | ALTA | Riesgo de confundir los seis jueces `scripted`, código `expected.py` y un experimento ejecutado | Confirmado dos archivos en upstream main; sin `generate/detect/unblind`, sin resultados de seis runs verificados |
| **F-A08** | ALTA | Una prueba “ausencia→permit” trivially detectable puede ganarla B2 sin aportar EA diferencial | Peer fuerte con misma información, coste y horizonte; equivalencia se publica como tal, no como éxito exclusivo |
| **F-A09** | ALTA | Cálculo de pérdida/recuperación de discriminabilidad sin t0 legítimo ni t1 fuente externa; CTGT REF 1.1 y mezclas de labels no prueban R3 | Real R3 queda `NOT_ADMITTED`; nueva prueba no presume regresión 4→3 de misma afirmación |
| **F-A10** | ALTA | Instrumento v0.4 débil, claves/expected leaks, independencia del auditado, B/D no adjudicados | Se preservan 13 reparos y v0.5; sin publicar carpetas privadas de siete casos ni claves |
| **F-A11** | MEDIA | Pérdida de conceptos E1–E8, #21 población vs UC-21 nuestro caso, R01 E1–E7 y UC-4 vs DDS Stage | Tabla `FLO-E1..FLO-E8` separada; trabajo de Flores/#21 intacto; nombres normalizados con origen |
| **F-A12** | MEDIA | Posible apropiación de roles/acuerdos: Flores, Cyril, Olena, Nelson, Steven y auditores | Autores/propietarios diferenciados; propuesta local **no** representa aceptación externa |
| **F-A13** | MEDIA | CDA2.0 y RA-AAI/S5 aparecen en continuación, pero son experimentos diferentes | Solo relaciones en `CONTINUATION`; no los convertimos en datos de Flores ni en esta Stage A |
| **F-A14** | MEDIA | Campaña en desarrollo sin `Run Card`/stopping rule concreto puede parecer admitida o cerrada | [RUN_CARD_PREPARATION.md](RUN_CARD_PREPARATION.md) recoge campos obligatorios y sus `NOT_ESTABLISHED`; status machine-readable diferenciada |
| **F-A15** | ALTA | No estaba comprobado que las notas recuperadas reprodujeran un original binario TXT/PDF byte por byte | Los nuevos archivos dicen solo “texto del lector completo”; no equivalencia binaria, ni paridad PDF ni ZIP |
| **F-A16** | MEDIA | El índice DDS y el control documental deben permitir reentrada directa por “Flores” y explicar el drift | Documentos de inicio, mapa, estado JSON e índices revisados para localizar pivot, ensayo, revisiones, fuentes, próximos pasos |

Las resoluciones anteriores son **documentales**. F-A06 y las obligaciones de validación del protocolo mantienen bloqueos abiertos; no se declara “auditoría científica completa” por encontrarlos.

## III. Custodia de fuentes de 11–12 octubre recuperada

Se leyeron **seis fuentes de la biblioteca: cuatro PDF y dos TXT** (total seis): [manifiesto](history/recovered-text/RECOVERY_MANIFEST.json), [texto completo recuperado](history/recovered-text/). La recuperación transfiere el **texto legible tal como se obtuvo del lector**, no una exportación binaria autenticada del archivo original.

| Fuente histórica | Contenido que antes se resumía | Archivo de texto recuperado |
|---|---|---|
| 12 Oct `EA_FLORES_RECUPERACION_Y_VERIFICACION` | Reentrada realista Q0/Q1, 05 BIS UC17-08, E1–E8, versiones y falsadores | [recovery-source](history/recovered-text/EA_FLORES_RECUPERACION_Y_VERIFICACION_2026-10-12_SOURCE_TEXT.txt) |
| 12 Oct `EA_FLORES_ADDON_MINIMO` | Intervención singular y B2 | [recovery-source](history/recovered-text/EA_FLORES_ADDON_MINIMO_2026-10-12_SOURCE_TEXT.txt) |
| 12 Oct `01_EA_STAGE_A_REVISED_SCIENTIFIC_CHALLENGE_EN.pdf` | v0.5 Stage A siete casos y admisión | [PDF-reader text](history/recovered-text/01_EA_STAGE_A_REVISED_SCIENTIFIC_CHALLENGE_EN_2026-10-12_PDF_TEXT.txt) |
| 12 Oct `02_EXTERNAL_AUDIT_RECONCILIATION_EN.pdf` | Disposición de trece problemas de v0.4 | [PDF-reader text](history/recovered-text/02_EXTERNAL_AUDIT_RECONCILIATION_EN_2026-10-12_PDF_TEXT.txt) |
| 11 Oct `02_MINIMAL_EA_FRAME_QUALIFIER_STAGE_A_EN.pdf` | v0.3 candidato, B/C/D y R3 condicional | [PDF-reader text](history/recovered-text/02_MINIMAL_EA_FRAME_QUALIFIER_STAGE_A_EN_2026-10-11_PDF_TEXT.txt) |
| 11 Oct `01_AUDIT_RECONCILIATION_EN.pdf` | Objeciones a Q-bind, cálculo contra-factual y errores | [PDF-reader text](history/recovered-text/01_AUDIT_RECONCILIATION_EN_2026-10-11_PDF_TEXT.txt) |

Su suma legible registrada en recuperación fue **105.576 caracteres** (datos devueltos por Files durante esa sesión). Las posteriores relecturas del servicio de Library a veces respondieron sin texto; por tanto **no se afirma una segunda comprobación independiente origen→publicación** ni un SHA-256 del original binario. Los archivos recuperados se mantienen como derivadas fechadas con sus Git blobs, y el texto de seis fichas de síntesis previas queda preservado aparte. Quedan sin autenticar los ZIP v0.2 y v0.5, y cualquier pack de claves `auditor_only`. No debe descargarse ni publicarse en abierta la clave para sustituir este hueco.

## IV. Verificaciones de fuente externa realizadas

- [Flores upstream](https://github.com/Himalogic/FG-TIDA-analysis/tree/07ac94fb100975bfff2e8ab0c644bd02ec87e537/planted-judge): exactamente `README.md` (blob `6be3c731...`) y `expected.py` (blob `3c147fd...`) en `main` del corte consultado. Los tres scripts mencionados permanecían previstos, no verificados como presentes; no hay reporte observable de ejecución de sus seis runs.
- [Publicación y review](https://github.com/FG-TIDA/themes/issues/21#issuecomment-6105480177), [Nelson](https://github.com/FG-TIDA/themes/issues/21#issuecomment-6132482219) y [Flores](https://github.com/FG-TIDA/themes/issues/21#issuecomment-6136280636) confirman separación UC17-08/09, protocolo guionizado, revisión hasta 18 octubre y resultados previstos para 25 octubre, **no recibidos a 13 octubre**.
- [Cyril](https://github.com/FG-TIDA/themes/issues/6#issuecomment-5984029028) define exacto la ausencia, rechazo, resultado remediado y supersesión. [Fixture 0.2](https://github.com/FG-TIDA/themes/issues/6#issuecomment-6028662270) corrige el canal a email, mantiene DC-SEND: no equivale a permiso ni es t1 posterior.
- [Olena](https://github.com/FG-TIDA/themes/issues/21#issuecomment-5532364422) establece los cuatro pasos de inferencia; [Flores](https://github.com/FG-TIDA/themes/issues/21#issuecomment-5903046577) conserva separación productor/consumidor; [Iván](https://github.com/FG-TIDA/themes/issues/21#issuecomment-5998217280) registra recalificación sin recomputación.
- [DDS Method Index](../../DDS_CANONICAL_METHOD_INDEX_v0.1.md), [Stage A](../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md), [Document Control](../../../../DOCUMENT_CONTROL.md), [plan de migración v0.2 de biblioteca] y navegación de UC21 fueron contrastados; raíz `dds/` no estaba creada, sin permiso de migrar todo el corpus.
- [Drive Candidate Case Validation Evolution](https://docs.google.com/document/d/1Ttha28cGAvNtL0vF848NVECToO472533sIbLU_RdoSU/edit) y [registro de atribuciones](https://docs.google.com/document/d/1bDQ3kc_C1DVCrdSrhVb3Lt0wGwZ-vEV0P2FDnqw_mpA/edit) aportan contexto y procedencia, no una campaña ejecutada.

## V. Criterios de paridad del repositorio tras publicar la auditoría

Se verificarán en el commit final:

1. **Ninguna eliminación ni traslado** de archivos preexistentes; las modificaciones de índice/control/propuesta son aditivas o se identifican y comparan expresamente.
2. **Ningún archivo científico congelado** alterado en baseline, Flores upstream, CTGT, UC-4, UC-21.
3. Manifest y `CAMPAIGN.json` parsean; campañas en desarrollo tienen **un** Stage A candidato y estados pendientes distintos de la decisión de drift investigativo.
4. Todos los **enlaces relativos** nuevos de la campaña y sus índices llegan a archivos vivos del repo.
5. Los **seis textos recuperados** siguen etiquetados como derivadas de Library (no PDFs o ZIP binarios exactos).
6. El protocolo conserva un único cambio causal en el brazo primario, el caso positivo, recuperación, y el negativo de no-observabilidad; B2 tiene pleno acceso al mismo fundamento.
7. Ninguna de las respuestas del usuario ni de terceros se presenta como firma de Run Card, permiso del testbed, resultado o adopción oficial.

## VI. Dictamen

**Antes:** buena base de fuentes y correcciones, pero **insuficiente representación del cambio de aproximación**, fidelidad documental parcial y riesgo de leer la v0.5 como sustituto del experimento quirúrgico.

**Después de las correcciones de esta auditoría:** expediente de campaña Stage A **en desarrollo y científicamente distinguido**; el giro 12–13 tiene su propio historial, prueba mínima especificada, controles y limitaciones, y textos legibles recuperados. **Sin ejecución científica todavía** y sin inferir un R3 real. La auditoría documental es una base de continuación, no un certificado de aceptación por un tercero.

**Bloqueos pendientes reales:** obtener/autenticar ZIP originales y PDF binarios si se exige paridad archivística; constatar release de Flores; identificar y acordar dueño de decisión/adaptador y canal; escoger/aceptar el desafío mínimo; preregistrar instrumentos/comparadores/criterios/costes; encargar adjudicación verdaderamente independiente; ejecutar y preservar los resultados, también si B2 empata o gana.

## VII. Supplemental findings after publication — concurrent P0–P3 technical package

**New discovery:** commit [c6858fd](https://github.com/dakleyer/structural-awareness-contributions/commit/c6858fd2110fe7debd93b20dc4fdfa5b6302f8ea) added a [substantial technical component](technical/TECHNICAL_INDEX.md) **within** the same Flores campaign. It contains a corrected P0 blind→P1 authorized unblind→P2 local receiver-proof association loss→P3 restoration (no source modification), G00–G12, EHD 04/05A and source A boundaries, nine-item residual/alternative B2, mutable comment hashes, historical ZIP hashes and a 21-assertion authored mock checker. **A separate detailed review** [TECHNICAL_INTEGRATION_AUDIT_2026-10-13.md](TECHNICAL_INTEGRATION_AUDIT_2026-10-13.md) discloses five specific findings T-A01…T-A05.

**Correction to earlier F-A06 archival scope:** “ZIPs not recovered” referred to **the initial dossier-creation runtime**. The concurrent technical owner reported that the original archives were *present in another authoring runtime*, and recorded SHA-256 from those local files. I **did not** obtain or independently rehash the private ZIPs in this audit, and their binary contents remain outside public GitHub. Their reported hashes improve custody without turning their confidential reviewer-only contents into a publicly reproducible byte archive.

**Technical findings:** (T-A01 HIGH) `test_qualifier.py`'s “indistinguishable observation” test sets `independent_key_truth` to its already-present `NOT_ESTABLISHED` value, so it compares *identical visible facts* without differing hidden ground truth; (T-A02 MEDIUM) older reproduction paths were obsolete, now corrected in a historical addendum; (T-A03 HIGH) 21 author-written mock assertions are not a native Flores run, independent two-world test or EA superiority demonstration; (T-A04 MEDIUM) seal refutation defeats a *key-relative comparison* only, not objective authored-key truth; (T-A05 HIGH) mocked source receipts cannot attest the unpublished source flags/unblind reports.

**Scientific reconciliation:** [FLO-F0…F4](PRIMARY_TRIAL_PROTOCOL_DRAFT_v0.1.md), the owner-preferred single-point UC17-08 downstream semantic mapping, and [P0…P3](technical/PROTOCOL_P0_P3.md), the detailed corrected receiving-proof test, are **two distinct prospective designs in one campaign**, not two executed campaigns. Both remain study candidates; a scientific reviewer has NOT frozen the selection, baseline, oracle or scored result. The 12–13 October methodological pivot remains a documented owner decision, **not an observed native R3**. Earlier adverse versions and all source references are retained.

**Audit closeout:** documentary and code inspection for the named sources is substantially reconciled. Complete binary archive parity, truly independent assessment, a legitimate completed Flores source result and any actual B2/EA comparison remain open. Do not state the source experiment, dynamic R3, Stage A, B or C passed.
