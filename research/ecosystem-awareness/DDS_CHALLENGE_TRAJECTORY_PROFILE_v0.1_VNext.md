# DDS Stage A — VNext

<!-- DDS terminology revision 3 (2026-10-07): Stage A/B/C only; source scientific version and evidence unchanged. -->

**Owning source:** [DDS Stage A — Specification Discovery / Challenge–Trajectory Profile v0.1](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md)  
**DDS method router:** [DDS Canonical Method Index v0.1](./DDS_CANONICAL_METHOD_INDEX_v0.1.md)  
**Current review date:** 8 October 2026.  
**Status:** current Stage A review ledger only. Historical incorporated proposals have been removed from this VNext because Git history already preserves them.

## 1. Current Stage A state

Stage A is now explicitly separated from the complete DDS method.

The live Stage A source currently provides:

- canonical identity as **DDS Stage A — Specification Discovery**;
- explicit A/B/C stage taxonomy for a reader entering this file;
- distinction between **DDS Stages** and local **trajectory gates**;
- full versus **Simplified DDS Stage A** coverage semantics;
- Challenge and bounded reduction;
- blind evaluator/private-map discipline;
- technology/configuration mapping;
- Stage 1 technology–problem extension/isomorphism profiling;
- Stage 2 non-isomorphic mechanism study;
- I/M/P/Ø route/outcome semantics;
- Type-0/1/2 and M-admission diagnostics where admitted;
- Cost/Risk/Effectiveness accounting;
- acceptance and optional Business Value projection;
- proportionality and material-assumption checks;
- reduced coverage / delivery separation;
- current R01, extension and HEW research relationships;
- evidence/claim boundary;
- minimum Stage A citation block;
- explicit Stage A entry, exit and handoff contract to Stage B.

The latest reader-orientation/handoff incorporation is commit `27938fa70a82c2fa07f79c60eed34ab4c2d9f267`.

### Conservation check for that incorporation

The Stage A clarification commit added **125 lines and deleted 0 lines**. No prior Stage A scientific text, mathematics, result, threshold, evidence record or source relationship was removed by that change.

## 2. Incorporated — no longer pending

The following items are incorporated in the live Stage A source and are intentionally **not repeated as before/after proposals in this VNext**:

- canonical-boundary / meaning-of-canonical clarification;
- reduced-coverage and delivery clarification 0.1.2;
- Stage 1 extension/isomorphism + Stage 2 non-isomorphic-mechanism clarification 0.1.3;
- HEW / executed-companion evidence parity;
- proportionality clarification 0.1.4;
- material-assumption check;
- bibliography / research-basis route;
- scoped-study completion route;
- Type-0/1/2, M-admission and blind-reference refinements already present in Stage A;
- split from one monolithic DDS file into Index + Stage A + Stage B + Stage C;
- Stage A reader taxonomy and scope boundary;
- Stage A entry/exit package and Stage B handoff contract.

Their detailed historical text remains available in Git history. They are not active work items.

## 3. Pending Stage A changes

**No rewrite of the canonical v0.1 source is pending. One additive successor proposal is active: the gate-diagnostic subprofile described below.**

The existing Stage A science, reader taxonomy, entry/exit boundary, Simplified coverage semantics, Stage B handoff contract and profile mapping are incorporated in the live source. The gate-diagnostic proposal adds a result/diagnostic layer without changing those frozen semantics.

The former `GA-P01` is complete:

- the authoritative cross-stage/current-corpus registry now lives in the [DDS Canonical Method Index](./DDS_CANONICAL_METHOD_INDEX_v0.1.md#8-current-dds-profile-and-support-registry);
- Stage A §11 now contains Stage A examples only and links to that registry;
- the previous detailed Cost/Risk/Effectiveness/Acceptance/BV/evidence information was moved into the Index registry rather than discarded;
- frozen historical results were not rewritten.

## 4. Cross-corpus work status — outside Stage A ownership

The following taxonomy/routing work has now been incorporated and is **not pending**:

- EA router and canonical-corpus README enter through the DDS Canonical Method Index;
- Canonical Corpus Manifest registers Index + Stages A/B/C as the DDS method set;
- DBC and 00D are classified as DDS support artefacts rather than parallel methods;
- R01 is routed as the richest current probabilistic Stage A reference instantiation;
- R01 C02 Oracle/harness is classified as shared DDS test-infrastructure qualification;
- RS-00E-Q1a Stage-0 is classified as bounded Simplified Stage A deterministic evidence while preserving historical version lineage;
- 00D-A01/A03 are classified as DDS test-design/support infrastructure;
- HEW, STAMP/STPA, SPIFFE, RATS and the current RAG/OAuth/MCP/SQL/durable-workflow studies are routed through Stage A with their evidence ceilings preserved;
- current 00E/00F/00G/00H/00I/00J technology/implementation trajectories are explicitly classified as Stage A or Stage A Challenge inputs as applicable;
- current human-readable study/completion/exercise reports point to the DDS Index while frozen Run Cards/FREEZE/RESULTS keep their execution-time identity;
- WORKPLAN and VISUAL_GUIDE state that W2/W3 and Stage-0/1/2 are workstream/evidence-maturity axes, not parallel DDS methods or DDS Stages;
- the public Ecosystem Positioning README points technical reviewers to the DDS Canonical Method Index;
- the authoritative global profile/support registry has moved from Stage A §11 to the DDS Index.

### Remaining work belongs elsewhere

| Remaining work | Owner |
|---|---|
| Stage B contract evolution and first 00I/S5 architecture-verification pilot | DDS Stage B |
| Stage C contract evolution and C11/T03 real-implementation validation route | DDS Stage C |
| Any further common cross-stage rule consolidation | DDS Canonical Method Index |
| Any future repository-wide stale-link cleanup discovered outside the current active routes | owning document / corpus maintenance |

None of these is a Stage A pending item.

## 5. Stage A review checks before any future incorporation

Any future Stage A change should pass all of these:

1. **Object check:** the object under test is still a candidate specification/mechanism/control profile, not architecture realization or product validation.
2. **Reference check:** the authoritative reference remains the frozen Challenge / Stage A acceptance and falsifier contract.
3. **Namespace check:** DDS Stage A/B/C is not confused with trajectory gates, gate policy, Stage-0/Stage-1 or C02/C11/T03.
4. **Evidence check:** evidence mode does not silently change Stage identity.
5. **Conservation check:** no frozen result, hash, theorem or historical evidence is strengthened or erased.
6. **Coverage check:** a Simplified Stage A profile declares selected and omitted surfaces.
7. **Handoff check:** any Stage B-ready result identifies a sufficiently frozen Stage A specification package.
8. **Closed-proposal check:** retire fully applied proposal fiches from this active VNext after preserving the exact predecessor and application decision in Git history. Keep substantive audit discussion, dissent and unresolved proposals visible.

## 6. Current decision

**The canonical Stage A v0.1 source remains unchanged. The only active Stage A successor work is the additive gate-diagnostic subprofile below.**

The live Stage A source remains the canonical Specification-Discovery Stage. The gate-diagnostic work is deliberately isolated in versioned draft artefacts so no historical Stage A result, theorem or acceptance record is silently reinterpreted.

After the gate-diagnostic subprofile is independently reviewed and exercised with frozen result tables, a separate promotion decision can determine whether any part belongs in a future Stage A version. Stage B and Stage C work remain independently owned.


---

## Gate-diagnostic successor work — 8 October 2026

A new additive Stage A diagnostic subprofile has been drafted to address a limitation exposed by the current requirement-level audits: a single Stage A acceptance state does not show which properties pass, which are merely declared, which depend on unresolved prerequisites, or what minimum remediation would unlock downstream properties.

Current draft artefacts:

- [DDS Stage A Gate Diagnostic Profile v0.1 Draft](./DDS_STAGE_A_GATE_DIAGNOSTIC_PROFILE_v0.1_DRAFT.md)
- [DDS Stage A Gate Catalog v0.1 Draft](./DDS_STAGE_A_GATE_CATALOG_v0.1_DRAFT.json)
- [DDS Stage A Gate Diagnostic Validation Plan v0.1](./DDS_STAGE_A_GATE_DIAGNOSTIC_VALIDATION_PLAN_v0.1.md)
- [DDS Stage A Gate Diagnostic Validation Run v0.1](./DDS_STAGE_A_GATE_DIAGNOSTIC_VALIDATION_RUN_v0.1.md)
- [DDS Stage A Gate Diagnostic Result Template v0.1](./DDS_STAGE_A_GATE_DIAGNOSTIC_RESULT_TEMPLATE_v0.1.json)
- [Deterministic gate checker](./gate-diagnostic/check_gate_profile.py)
- [FG-TIDA Decision Boundary Evaluation Profile v0.2 Draft](./fg-tida/tests/FG_TIDA_DECISION_BOUNDARY_EVALUATION_PROFILE_v0.2_DRAFT.md)

The proposal is **not another DDS method and does not modify frozen Stage A results**. It adds a gate-by-gate output layer with separate own verdict, specification level, dependency/effective status, test role, root-blocker analysis, potential-unlock diagnosis and a Stage-B handoff queue. The core catalog is technology-neutral.

An initial maintainer-side structural portability run now covers the planned historical, mathematical/reduction and non-HF technology families. It found and repaired one false-blocking defect in the first dependency example. Promotion still requires independent review and actual frozen result tables; the catalog therefore remains draft.

A **v0.2 audit-candidate successor package is now frozen for external review**, while v0.1 remains preserved:
- [Profile v0.2 Audit Candidate](./DDS_STAGE_A_GATE_DIAGNOSTIC_PROFILE_v0.2_AUDIT_CANDIDATE.md)
- [Catalog v0.2 Audit Candidate](./DDS_STAGE_A_GATE_CATALOG_v0.2_AUDIT_CANDIDATE.json)
- [Result Template v0.2](./DDS_STAGE_A_GATE_DIAGNOSTIC_RESULT_TEMPLATE_v0.2.json)
- [Checker v0.2](./gate-diagnostic/check_gate_profile_v0.2.py)
- [Audit Manifest v0.2](./DDS_STAGE_A_GATE_DIAGNOSTIC_AUDIT_MANIFEST_v0.2.json)
- [External Audit Checklist v0.2](./DDS_STAGE_A_GATE_DIAGNOSTIC_EXTERNAL_AUDIT_CHECKLIST_v0.2.md)

This successor makes profile-required gates explicit, requires fail-capable preregistered cases for discriminating gates, machine-evaluates conditional named-claim dependencies, and defines PROFILE_PASS / PROFILE_PARTIAL / PROFILE_FAIL / PROFILE_COVERAGE_ONLY without introducing an aggregate score. It is frozen for **instrument audit**, not yet independently accepted and not a candidate-technology result.

No canonical v0.1 gate semantics are changed by this VNext entry.


---

## Audit implementation follow-up — G03.b / T06 (Plan 2.0, executed 10 October 2026)

**Source:** Reconciled audit v3.1 `G03.b / T06`, confirmed source defect. **Strategy:** v3.3 DS-12 source conservation, DS-02 one DDS method, B-minimal scoped changes. **Priority:** P1 for a Stage A instrument result, not an assertion of runtime product failure. **Decision:** programme owner requested immediate application of audit-derived corrections. **Actual status:** candidate successor and seven unit controls published; **T06 remains PARTIAL** pending end-to-end original-catalog replay, frozen preregistration evidence and external source-owner acceptance.

**Immutable predecessor:** [v0.2 checker](./gate-diagnostic/check_gate_profile_v0.2.py) blob `0aa51e7b050123c4a09967a5fae52bf290b6c8a5`, unchanged.


In this passage, N/A is checked for enum/verdict consistency but `applicability_rationale` is not checked.


**Source pin:** [proposed v0.3 checker](./gate-diagnostic/check_gate_profile_v0.3_audit_candidate.py), blob `97430b0cd933f080a31bc3118d6871f7256c61ed` and [commit](https://github.com/dakleyer/structural-awareness-contributions/commit/f76c732d8dafd72263df1fca4fd39a8fe6f1576f).

**Negative controls:** [seven tests](./gate-diagnostic/test_na_rationale_v03.py), blob `9b73180f5aef82b0e38fe790d0e6278cc619db5c`, [test commit](https://github.com/dakleyer/structural-awareness-contributions/commit/e1b7619e702775ed38ef7f7a1a159c93e75d0121). Author-side isolated pre-check tests returned `Ran 7 tests ... OK`; this is **not** a full v0.2 catalog replay or independently signed audit.

**Unchanged scientific/technical claims:** The v0.2 catalog, checker, audit manifest, Stage A v0.1 profile, all frozen fixtures and historical results retain their original bytes. `NOT_APPLICABLE` still needs a preregistered, materially justified out-of-scope decision: the successor verifies a nonblank text field only and **cannot** establish when the rationale was written. It does not close G03.a runtime-claim propagation, G03.c positive fixture/multihop work or G03.d L4 calibration.

**Next actual gate:** execute both v0.2 and v0.3 against the same fully registered catalog and input, with a PASS control, missing-rationale mutant, raw input/output hashes and named reviewer. Only then propose promotion; no freeze is overwritten.

---

## T05 — applied G03.a cross-stage claim output projection (Plan de Cambios 2.1, 10 October 2026)

**Source/audit**: [Reconciled audit G03.a/T05](https://github.com/dakleyer/structural-awareness-contributions/tree/main/research/ecosystem-awareness) · objective: prevent Stage A specification PASS from being read as Stage B runtime enforceability. **Strategy:** DS-02, DS-08 and DS-12: one DDS method, affirmative scoped result, add an auditable successor rather than revising frozen evidence.

**Authority:** User explicitly authorized the five-phase change process. **State:** `T05_IMPLEMENTED_AUTHOR_TESTED; INDEPENDENT_AGENT_REVIEW_NOT_PERFORMED`. This is not Stage B approval or independent external audit.

**Old checker blob:** `97430b0cd933f080a31bc3118d6871f7256c61ed` (v0.3 T06 predecessor). **New checker blob:** `69c3bafe024d99a534ba8896ef12e0ba277ab8f6`, [commit](https://github.com/dakleyer/structural-awareness-contributions/commit/9393375a5a459ca9c55fd4acb81fff2cd7676990).



### TEXTO ANTES — insertion location after `load_frozen_checker()`

**No cross-stage projection function existed** between `load_frozen_checker()` and `compile_successor()`.




### Regression source and five-phase record

**Test file:** [T05 16-test module](./gate-diagnostic/test_t05_cross_stage_v03.py) at blob `2146b303e2a17719cd98ec95f8f1847a67ba40b8`, initially published in [commit 246b0311](https://github.com/dakleyer/structural-awareness-contributions/commit/246b03119ffc00a8e45568234b689bdbb6330a12) and corrected in [commit 2b0b7872](https://github.com/dakleyer/structural-awareness-contributions/commit/2b0b7872d8143a3ae84a2c7502c4d8590cf49c23) to use the **actual published checker filename**. The only change in the test correction was that import target.

1. **Exact plan:** unchanged old description and function documented above; additional helper and full replacement shown, unmodified frozen v0.2 and v0.2 catalog.
2. **Pre-application challenge:** local author tests 16/16 and six injected mutants detected 6/6, performed in separate subprocesses. This is an independent *execution process*, not an independent agent or external review.
3. **Application:** 3 GitHub commits changed only the v0.3 checker and the new T05 test file. Source-owner promotion has not occurred.
4. **Source integrity:** old/new file blobs re-read; frozen v0.2 checker `0aa51e7b050123c4a09967a5fae52bf290b6c8a5`, catalog `92e1c2b1f4316f77636f669c8b62a1d53091c372` and Stage A v0.1 remain unchanged.
5. **Readability/semantic review:** native Stage A result remains in `stage_a_declaration_status`; runtime-named claim `status` is conditional rather than plain PASS; profile-wide result carries `profile_outcome_scope=DDS_STAGE_A_ONLY`; T06 NA-rationale rule remains. A separate full 15-gate frozen catalog replay and named external review remain open.

**External reviewer/agent needed:** inspect original catalog and compare emitted Stage A data with Stage B handoff requirements, test consumer interpretation, sign the source pins and audit the new projection contract. `PROFILE_PASS` explicitly remains *a Stage A profile result only*.

---

## G02.b / T04 — Prospective review, freeze, amendment and dispute envelope (Change Plan 4.0; 10 October 2026)

**Status:** EDITORIAL_PROPOSAL_PUBLISHED; prospective template only; NOT_FROZEN; NOT_INDEPENDENTLY_REVIEWED; T04_NOT_CLOSED. This section is an append-only governance proposal in the *owning Stage A VNext*, not a change to Stage A v0.1, the frozen v0.2 diagnostic instrument, DDS Stage B/C, a scientific result, or an external source-owner contract.

**Why this is proposed:** The reconciled audit v3.1 classifies G02.b/T04 as a review/freeze/dispute minimum-envelope gap. G02.a/T03 separately concerns attributable reviewer independence. The documentary strategy v3.3 calls for source-owned, minimal, conserved revisions (DS-12), without retroactively rewriting frozen material. The controlling full audit and strategy must be read before asserting formal T04 closure.

### T04-E1. Minimum prospective review record (one version per frozen review)

For each future review, create a dated record using the following *field names and null semantics*. Empty values, `UNKNOWN`, `NOT_ESTABLISHED`, and merely author-reported claims cannot be promoted into evidence of independence, freeze, or acceptance.

```yaml
review_id: REQUIRED_UNIQUE_ID
review_version: 0.1
object_stage: STAGE_A | STAGE_B | STAGE_C | MIXED_UNCLASSIFIED
review_target: REPOSITORY_PATH_OR_STABLE_EXTERNAL_ID
target_git_commit: REQUIRED_PINNED_COMMIT_OR_NOT_ESTABLISHED
target_blob_sha: REQUIRED_PINNED_BLOB_OR_NOT_ESTABLISHED
review_question_and_claim_ceiling: REQUIRED_BEFORE_FREEZE
review_owner: REQUIRED_NAMED_RESPONSIBLE_PARTY
reviewer_identity: NOT_ESTABLISHED
reviewer_affiliation_and_role: NOT_ESTABLISHED
reviewer_relationship_to_authors: NOT_ESTABLISHED
conflict_of_interest_declaration: NOT_ESTABLISHED
independence_status: NOT_ESTABLISHED
criteria_and_acceptance_ref: NOT_ESTABLISHED
criteria_version_or_hash: NOT_ESTABLISHED
frozen_inputs_and_versions: []
freeze_time_utc: NOT_ESTABLISHED
freeze_actor: NOT_ESTABLISHED
blind_information_boundary: NOT_ESTABLISHED
adversarial_and_positive_controls: []
execution_or_document_review_record: NOT_RUN
raw_input_hashes: []
raw_output_hashes: []
findings_and_dispositions: []
reviewer_dissent_and_objections: []
dispute_resolution_authority: NOT_ESTABLISHED
amendment_history: []
reviewer_signoff: NOT_ESTABLISHED
owner_disposition: PENDING
external_acceptance: NOT_ESTABLISHED
```

The record is a proposed *minimum information envelope*, not an executable validation claim and not a declaration that a reviewer has been engaged. If `object_stage=MIXED_UNCLASSIFIED`, the review must separately identify the tested objects and governing references before any stage-specific acceptance.

### T04-E2. Freeze and change-control rules

1. **Before outcomes:** identify the review target, acceptance criteria, input versions, positive/adversarial controls, reviewer relationship, and information boundary; record the freeze timestamp, responsible actor and immutable source pins. If any necessary field is missing, classify the review `ENVELOPE_INCOMPLETE`, not accepted.
2. **During review:** distinguish the original raw observations from interpretations; preserve reviewer dissent even when the owner disagrees. A second script, separate prompt or repeated author pass does **not** establish a second independent reviewer.
3. **After freeze:** a changed target, criterion, fixture, input, reviewer identity, or material conflict opens an explicitly linked **successor review version**; do not alter the predecessor to make its earlier result look preregistered.
4. **Dispute:** log objected-to claim, evidence pins, disagreeing parties, proposed resolution, authorized decision maker and the final status. An unanswered objection stays `UNRESOLVED`, even if editorial text was published.
5. **Promotion:** publishing this template does not close G02.b/T04. A future claim of closure requires a named reviewer, dated pre-outcome freeze, independently held raw inputs and outputs as applicable, adjudication of dissent, owner disposition and an attributable signed acceptance record. No Stage B/C, UC-4 or product result follows from Stage A documentary review.

### T04-E3. Adversarial acceptance checks (future execution; NOT_RUN here)

- **A — retroactive freeze mutant:** change a criterion after the first observed outcome; expected result: `INVALID_PRE_REGISTRATION` and a new version required.
- **B — nominal reviewer mutant:** omit conflict/relationship or reuse author identity while asserting independence; expected result: `INDEPENDENCE_NOT_ESTABLISHED`.
- **C — disappearing dissent mutant:** omit a recorded objection from a later summary; expected result: `LOSS_OF_REVIEW_HISTORY`.
- **D — silent input replacement mutant:** change a source blob without changing its pin; expected result: `SOURCE_MISMATCH`.
- **E — false-stage promotion mutant:** interpret Stage A document PASS as realized runtime assurance; expected result: `STAGE_BOUNDARY_VIOLATION`.
- **F — controlled positive review:** freeze a complete, accurately attributable record, preserve controls and disagreement status, and report only the claim ceiling actually examined; expected result: `ELIGIBLE_FOR_REVIEWER_DECISION`, **not** automatic approval.

### T04-E4. Acceptance and ownership limits

**Present effect:** a review-envelope proposal is available in the existing owner-ledger, with no historical text replaced. **Still open:** a direct reading of the full v3.1 T04 audit card by a named independent reviewer; final selection of required/optional fields, actual freeze/adversarial runs, raw evidence custody, dispute resolution and source-owner acceptance. T03 reviewer-independence questions remain separately open. Future T04 implementers must compare the proposal with those primary sources, preserve this version, and record an exact BEFORE/AFTER successor before any normative incorporation.

**Result:** `T04_PROPOSAL_PUBLISHED_IN_VNEXT`; `T04_AUDIT_CLOSURE=NOT_ESTABLISHED`; `SCIENTIFIC_CORPUS_UNCHANGED_BY_THIS_EDITORIAL_INSERTION`.

---

## Auditorías anteriores frente al corpus vigente — 12 octubre 2026

**Codex, mismo asistente; `17b597bf91acb0f37daebc716e8f23f65daa23eb`.** Se cotejaron Index/Stages A-B-C, Stage A antes/después, UC4/oráculo y checkers v0.2/v0.3. Especificación, arquitectura y ejecución mantienen referencias distintas. T05/T06 tienen un sucesor publicado con su estado de autor; no se repiten como nuevos arreglos pendientes. No se ejecutó ningún instrumento.

La regla 8 de retirar propuestas contradice la conservación del viejo, discusión y desacuerdo. Git mantiene el ledger del 6 de octubre; no se reconstruye ni se reaplica su historia. Las nuevas reglas T04 sobre conservar dissent no devuelven automáticamente lo retirado.

El nuevo guard NA comprueba un motivo, pero no el tipo de `na_substitute_satisfied`. v0.2 usa truthiness y v0.3 hereda ese flujo. Una fila NA con motivo no vacío y el string `"false"` puede satisfacer la rama. Es razonamiento estático, no reproducción experimental o diagnóstico de todo el instrumento. [EP VNext](../../architectural-contributions/ecosystem-positioning/README_VNext.md#nueva-revisión-integral-de-cambios-y-consistencia--12-octubre-2026) registra el conjunto y los receptores.

### Cambio 74 — Rechazar sustitutos NA de tipo string antes de adjudicar

**Aplicado — autorización de Iván, 12 octubre 2026.** Cambio74 incorporado en `research/ecosystem-awareness/gate-diagnostic/check_gate_profile_v0.4_audit_candidate.py`. Fuera de pendientes. El par y su ficha anteriores se conservan en Git, predecessor `9fb9421711521decde6843b04914a143a1f04c35`.

### Cambio 75 — Mantener auditorías y viejos publicados al cerrar propuestas

**Beneficio:** Resolver la contradicción entre eliminar propuestas incorporadas y conservar audit conversation/antes-después visible que Iván pidió.
**Fuente:** `research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md`, blob `985845b1876652a60a0cadfff40201085f40be0d`, snapshot `17b597bf91acb0f37daebc716e8f23f65daa23eb`. Regla8 delledger; no se reabre el estado deincorporación.
**Impacto Alto; riesgo Medio; esfuerzo Medio; prioridad Primera; 1 — Claridad de evidencia y estado.**
**Riesgo concreto:** Confundir historia con cola vigente o reabrir cambios ya incorporados; restaurar debe usar textos auténticos y estados fechados, sin tocar canon.
**Coste:** Conciliar reglas, recuperar/citar las épocas auténticas y mantener su disposición actual. Redactar una línea no devuelve por sí solo las auditorías retiradas.
**Dependencias y orden:** Conservar estados de incorporación y decisiones actuales; no reaplicar incorporados ni reconstruir viejos de memoria. Decidir presentación histórica y restitución auténtica dentro de la única VNext.


**Instrucciones de Iván:** una VNext por unidad, originals en lectura, conservar conversaciones y viejo completo. Auditoría publicable, incorporación pendiente de su decisión concreta. Contradicción documental confirmada; regla propuesta, recuperación de épocas pendiente


---

## Consistencia de DDS y sus receptores — 12 octubre 2026

**Auditoría por Codex, mismo asistente de IA, para revisión humana.** Corte público `eb5d66d7e22dc18f093ee33fcd564e1fac6d2338`. No hay un commit público posterior al corte de la revisión integral anterior. Se releen completos Index y Stages A/B/C y se contrastan sus pasajes con EA/EP, R01, Oracle/UC-4, HF y HC-HID/MSCA. Se verificó la disponibilidad por blob de los 2.194 archivos del árbol; ese control de custodia y la búsqueda de referencias no equivalen a una nueva lectura científica de todos ellos. No se ejecutaron programas, modelos, productos o experimentos.

**Juicio:** la estructura principal sigue siendo consistente. Stage A compara especificaciones/mecanismos con el Challenge; B verifica una realización contra el paquete A congelado; C contrasta una implementación fijada con el Challenge y efectos observados. Simplified declara cobertura; el modo de evidencia es otro eje. Ninguno de estos nombres cambia los A/B/C/D epistemológicos de 00M, los Stage-0/1 de UC-4, las etiquetas locales de brazos o el significado de C02/C11/T03.

### Lecturas cruzadas y límites

- **Index ↔ Stage A:** Index §§1–6 y Stage A §§2.1/6/10/17 preservan objeto, referencia, paquete de salida y no promoción. La nota inicial de Stage A todavía dice “explicit DDS stages” para Stage1/Stage2; §13.1 conserva el vocabulario de extensión anterior. Index §5 reserva DDS Stage A/B/C para el desarrollo y su registro llama Stage1/Stage2 disciplina interna de A. Hay una ambigüedad de lectura al entrar, no evidencia de que hayan aparecido otras dos etapas ni cambiado las obligaciones. La propuesta 76 aclara sólo el primer párrafo; mantiene títulos, anchors e identificadores históricos.
- **Stage A ↔ B ↔ C:** B §§2/4/13 exige congelar el paquete antes de adjudicar, conserva fallos y abre un sucesor A cuando la especificación necesita revisión. C §§2/4/7/15 exige configuración, referencia y observación adecuadas; un producto previo puede entrar por correspondencia explícita. La ruta A→B→C no es una promoción automática, ni exige inventar diseño DDS previo para todo producto. Un modelo ejecutable no se convierte en C por ejecutarse.
- **C02/UC-4 ↔ DDS:** el Oracle README identifica instrumentación compartida; UC-4 §4.1 es una nota de diseño y conserva el alias anterior “Architecture Conformance”. Su contenido usa el paquete A como referencia y distingue efectos; no crea una autoridad rival a Stage B. Los instrumentos/calendarios locales no demuestran B/C ni admisión externa. No se necesita una corrección a un registro congelado para uniformar ese alias.
- **HF ↔ requisitos ↔ MSCA:** los dos textos del 12 de octubre distinguen recalificación local y arquitectura completa. S3/S10/T1 y F2/APQ pueden sostener una pregunta de detección/recalificación; S1/S14 no son sensores ni actuadores por su sola definición. CH-01…CH-08 son casos futuros, no añadidos al paquete ciego v0.3. MSCA §4.1 mantiene señal, capacidad y autoridad separadas; observar una novedad no impone migración de rol. Ver [comentario receptor en HF VNext](./baseline/reductions/00G-R01/extensions/hugging-face/README_VNext.md#consistencia-con-dds-y-msca--12-octubre-2026) y [Operation VNext](../../standards/minimum-sufficient-control/04_OPERATION_VNext.md#consistencia-con-dds-y-recalificación-local--12-octubre-2026).
- **Coste humano ↔ comparación DDS:** HC-HID §7A conserva vector cuando las magnitudes no son conmensurables y exige regla explícita para sumar/normalizar. Operation §4.1 exige mismo Challenge, calidad y autoridad; una ruta M más barata no acredita llegar al mismo I. Esa compatibilidad conceptual no mide capacidad humana, latencia real, ROI ni eficacia.

La frase del Index fechada el 7 de octubre sobre HF preparado no invalida las ejecuciones sintéticas posteriores: el lector HF distingue aquellas aproximaciones de la adjudicación histórica/prerregistrada pendiente. No se propone una etiqueta de “Stage A superado” para resolver una diferencia de fechas. [EA VNext](./README_VNext.md#consistencia-de-la-ruta-dds--12-octubre-2026) y [EP VNext](../../architectural-contributions/ecosystem-positioning/README_VNext.md#consistencia-del-corpus-en-torno-a-dds--12-octubre-2026) recogen las consecuencias para lectores.

### Auditorías anteriores que conservan vigencia

**74** sigue siendo una propuesta de admisión booleana del futuro checker: el código publicado no cambió desde el corte anterior, no se reprodujo aquí el contraejemplo y no se invalidan retrospectivamente resultados. **75** sigue identificando pérdida de historia visible frente a la instrucción de conservación; T04 exige preservar desacuerdos pero no devuelve por sí mismo lo retirado. T05/T06 mantienen autoría, independencia no establecida y replay completo pendiente. No se reabre su incorporación como si no hubiera sucedido, ni se declara cierre de T03/T04 o de las cinco/sexta científicas.

## Registro de aportaciones y frontera del método — 12 octubre 2026

**Codex, mismo asistente; nuevo corte `f437c95cce3645a05ba45f52f521f6b9692e0aa7`.** Tras la publicación del cotejo anterior entró el [registro de veinte aportaciones potenciales](./DDS_POTENTIAL_CONTRIBUTIONS_REGISTER_v0.1.md), leído completo. El Index incorpora un banner de ruta hacia él; Index anterior recuperable por su snapshot y por retirada exacta del único banner. A/B/C, checker, catálogo, resultados y requisitos no cambiaron en ese merge.

**Consistencia mantenida:** todas las propuestas se vinculan a un propietario actual; un mecanismo o prueba no hereda automáticamente una aceptación. Las piezas de suficiencia, permiso receptor, mapas parciales, contradicción, computabilidad, cierre, cache/dependencias y cambio temporal mantienen sus distintos objetos y restricciones. Los tres ejemplos son construcciones ilustrativas con costes hipotéticos, no ahorros medidos o demostraciones de los artículos originales. Un peer fuerte puede empatar o ganar. [EA VNext](./README_VNext.md#nuevo-registro-de-aportaciones-dds--cotejo-del-merge-del-12-octubre-2026) registra el juicio específico de cada familia y sus fuentes pendientes.

**Dos condiciones a explicitar al concretar perfiles, sin cambiar el texto ahora:**

1. **DDS-PC-010, “C measured instrument if admitted”.** Si se califica el instrumento usado para medir otra tecnología, es infraestructura y no un resultado sustantivo C de esa tecnología. Si la tecnología objeto del Challenge es un instrumento real, su implementación puede ser objeto de C bajo el contrato de Stage C. La tabla común §2 mantiene esa frontera, pero la tarjeta deberá escoger y nombrar el objeto antes de SPECIFICATION_READY. Pregunta pendiente: ¿se prueba el evaluador o una implementación de medición como tecnología candidata? No se fabrica un par de reemplazo mientras no se haya elegido ese alcance.
2. **DDS-PC-011/012/020, humanos.** Un scheduler o ledger técnico puede evaluarse bajo un perfil declarado; disponibilidad, causalidad de carga y retención reales exigen validación de constructo, fuentes humanas y protocolo propios. Stage C de software no cierra ese estudio. Las tarjetas ya conservan esta separación; no añadir un requisito universal o un precio/hora sintético para suplir datos.

P1/P2/P3 son prioridad de desarrollo, no DDS Stage ni autorización de ejecución o cambios mínimos de bajo riesgo. Las veinte PROPOSED no son veinte modificaciones quirúrgicas listas y no subsanan T03/T04/T05/T06, ni 74/75/76. La propuesta 76 sigue contra el mismo blob de Stage A; el nuevo banner del Index no cambia su viejo. No se modifica el register adicional, se crea otro expediente o se activa campaña. Canon en lectura y pasadas científicas pendientes conservan su estado real.


---

## Acotar el cambio de conservación — 12 octubre 2026

**Codex, mismo asistente; corte `21c3946009af4a14433d7240eddce939e4ff9599`, este ledger blob `83bf1e5cb96805669c803a2bba3dc2cf7ce895c1`.** Iván pide planes al final de las VNext, alto impacto y bajo riesgo con muy poco texto. El cambio75 completo incluye recuperar/reconciliar historia auténtica y mantiene riesgo/esfuerzo Medio. El74 cambia admisión del checker y sigue riesgo Medio; no se presenta como arreglo textual de bajo riesgo. T04 y las auditorías anteriores permanecen.

La alternativa siguiente se limita a evitar retiradas futuras mediante una regla. No recupera las propuestas ya retiradas, no convierte un antecedente reconstruido en auténtico, no reabre lo incorporado y no cierra75/T04. Es una variante del75, no un nuevo hallazgo ni otro expediente. Su impacto Alto corresponde a preservar evidencia visible para revisiones y decisiones futuras; su riesgo Bajo corresponde exclusivamente a ese alcance documental.



## Propuestas aplicadas retiradas

Por autorización de Iván del 12 octubre 2026 se retiran las fichas completas de cambios ya incorporados: textos, títulos, justificaciones, valoraciones y filas de prioridad. Las auditorías y las propuestas pendientes permanecen. Las decisiones y fichas completas se consultan en la [predecesora de esta limpieza](https://github.com/dakleyer/structural-awareness-contributions/blob/884e892a6fe1d0deffea493931c9fc5acf8e0258/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md).

## Revisión del diseño de consolidación DDS por campañas — 12 octubre 2026

**Auditoría realizada por Codex, mismo asistente; revisión documental sobre el corte `07c83653babec79f387bdfd5fc4b93e4ac21b533`.** Iván solicita analizar el borrador autocontenido v0.2 de reorganización, no ejecutar la migración. Se leyó el plan completo y se contrastaron la navegación controlada, el método A/B/C, los contratos HF v0.3 y v0.3.1, sus ocho bindings de paquete, el catálogo de extensiones y los recorridos bot v0.6. El documento recibido permanece fuera del repositorio; aquí se publican las conclusiones de revisión.

El diseño coincide con DDS en distinguir objetos A/B/C y modos de evidencia, conserva los inputs y no convierte un resultado A en B/C. La regla organizativa «una campaña, una etapa» debe declararse como política prospectiva del registro, compatible con el método. No se exige dividir expedientes históricos ni alterar su identidad. Separar identidad de campaña, versiones materiales del contrato, runs y sucesores; registrar una campaña no equivale a aceptarla.

No recomiendo crear una segunda fuente metodológica mantenida en dds/canonical. El Index actual contiene enlaces ./baseline/..., y su copia literal a otra ubicación resolvería a destinos diferentes. Usar referencias inmutables al original; si posteriormente se requiere snapshot, identificarlo como copia y conservar su contexto. REGISTRY.json organiza campañas; el Index clasifica el método, el catálogo clasifica estudios, el registro de claims mantiene consumidores y el de aportaciones es backlog. Falta especificar sincronización/propietario de datos comunes.

La aceptación del plan dice rechazar «Stage retrospectivo», mientras otras secciones permiten clasificación histórica documentada. Hay que precisar: se admite clasificar retrospectivamente por objeto/evidencia; se rechaza atribuir un prerregistro, ejecución, aceptación o Stage más fuerte que lo demostrado. Esa distinción ya está en Index §7.

Preservación exige versiones exactas de inputs, no sólo estado actual. El expediente HF ilustra un mapa FG-TIDA fijado a blob38d64f61ef81a300a20d9d89cda65e5bb6ba5b22 distinto de main. La salida científica de una campaña se versiona por su contrato; el nombre de carpeta no le otorga aprobación. Una réplica archivística de una VNext no abre un expediente nuevo; toda conversación continúa en la única VNext propietaria.

[EP VNext](../../architectural-contributions/ecosystem-positioning/README_VNext.md) concentra el juicio estratégico y las condiciones; [EA VNext](./README_VNext.md) y [HF VNext](./baseline/reductions/00G-R01/extensions/hugging-face/README_VNext.md) registran las relaciones. Primera tanda sugerida de indexación: impacto Alto/riesgo Bajo/esfuerzo Medio. La copia y adopción operativa permanecen propuestas separadas; no se añade todavía canon, código, carpetas, pruebas o campañas.


## UC-21 y DDS: dos entradas enlazadas — 12 octubre 2026

**Revisión por Codex, mismo asistente.** Iván precisa que UC-21 es el caso con objetivos y campañas, y DDS el método de investigación. Se mantiene esta distinción y se ajusta el orden del diseño de consolidación: primero probar la navegación desde UC-21 usando sus ejercicios existentes; después comprobar su generalidad con HF y otra familia. No se crea una nueva campaña S5 ni se mueve el caso al corpus metodológico.

La entrada pública [UC-21](https://github.com/FG-TIDA/use-cases/issues/21) remite en su cuerpo al snapshot `aec08fb5b0fac2ee399372370e9ee2a82a2d5779`. Su cuerpo no nombra DDS; sus comentarios sí lo explican en [S5](https://github.com/FG-TIDA/use-cases/issues/21#issuecomment-6109154445) y [S4/CDA](https://github.com/FG-TIDA/use-cases/issues/21#issuecomment-6111953753). README y USE_CASE coinciden entre aquel snapshot y la rama de revisión `76ac39bae74d10f4586f5fb787f69deaf7f59add`, pero S6 de la rama es un adapter hacia 00J/00J-A01. Por eso publicar una propuesta en la rama no modifica lo que alcanza el lector del enlace congelado. Una futura actualización de la entrada debe añadir una ruta explícita al seguimiento y mantener el envío anterior. La Issue y sus comentarios no se modifican aquí.

El [autor de S5](https://github.com/FG-TIDA/use-cases/issues/21#issuecomment-6115830369) propone cerrar en el alcance evidenciado. Se comprobó su README externo v0.1.3, blob`4b0d2a673c8ee945bd6c52248390a3c595b9285a`: declara `I2-complete` completo para las ramas seleccionadas dentro del modelo y separa predicates enforced/assumed upstream. Esto explica el estado de esa discusión; no constituye una nueva aceptación conjunta ni un rerun. La organización conserva el ejercicio y sus pins, sin reiniciarlo para llenar el registro.

**Relación propuesta:** entrada UC-21 → explicación del caso y objetivos → escenarios/hipótesis → ejercicios existentes → contrato DDS aplicable → runs/evidencia → conclusión para el objetivo UC-21 → posible selección posterior de especificaciones. Desde DDS se recorre la misma relación por método → campañas de distintos casos → fuente del Challenge → evidencia → resultado. El registro futuro debe apuntar a los expedientes reales y sus propietarios, con varias relaciones por campaña; no duplicarlos bajo ambas entradas.

**Asignación de funciones:** UC-21 mantiene su problema, objetivos, HC/HR/HS/H1–H6 y gates. DDS mantiene método y A/B/C. El expediente del estudio mantiene contrato, versión, comparadores, ejecución y conclusión. EA, RA, MSCA y otros componentes conservan fuentes y decisiones de incorporación. Objetivo, R0/R1/R2, Stage A/B/C, modo de evidencia y estado de ejecución son dimensiones separadas. Un resultado del caso no demuestra automáticamente necesidad de EA ni selección de una especificación.

**Preservación:** enlaces actuales, snapshot enviado, anexos, escenarios, figuras, pruebas, denominadores y autoría conservados. Toda relación estructural se revisa en las VNext de README correspondientes; tres niveles EP→Awareness→índices técnicos, con expedientes de campaña como documentos de trabajo. Mantener una sola VNext lógica aunque un registro enlace varias rutas. La copia física posterior sigue pendiente de matriz de versiones/dependencias; no es necesaria para implementar la lectura propuesta.

**Prioridad:** puente de lectura inicial de alto impacto esperado y riesgo Bajo; esfuerzo Medio por contraste entre repositorios y épocas. La precisión de trazabilidad de campañas en el caso tiene impacto Alto y riesgo Medio: debe concordar con la matriz de objetivos y plantilla RUN_RECORD antes de adoptarse como campo obligatorio. No se activan campañas, adopción canónica, cambios de Issue ni redistribución por publicar esta revisión.

**Prueba de compatibilidad:** los comentarios UC-21 ya usan Simplified Stage A para S5 y describen S4/CDA como posible mapping posterior, con DDS útil incluso cuando no se selecciona una especificación EA. Ese antecedente impide diseñar la consolidación como una teoría que absorba el caso o abra de nuevo S5. La campaña DDS clasifica el objeto y contrato del estudio, no los R0/R1/R2 del caso ni sus condiciones causales A–D.

La declaración de una campaña futura debe identificar: caso/versión/objetivo seleccionado, contrato y fuentes, Stage aplicable, comparadores, evidencia y retorno al resultado del caso. Un caso puede alimentar varias campañas; una campaña puede declarar varias fuentes del Challenge dentro de un scope explícito. El registro indexa, los expedientes originales gobiernan. La selección posterior de especificaciones es una decisión separada.

[UC-21 USE_CASE VNext](https://github.com/dakleyer/use-cases/blob/when-controls-work-system-fails-v0.9.3/contributions/when-controls-work-system-fails/USE_CASE_VNext.md) contiene el antes/después de esta relación y [README VNext](https://github.com/dakleyer/use-cases/blob/when-controls-work-system-fails-v0.9.3/contributions/when-controls-work-system-fails/README_VNext.md) el puente humano. [EP VNext](../../architectural-contributions/ecosystem-positioning/README_VNext.md) registra el orden común. Sin cambios metodológicos, nueva campaña, clasificación retrospectiva más fuerte o ejecución.


## Puente UC-21–DDS incorporado — 12 octubre 2026

Iván confirma continuar con UC-21→objetivos→ejercicios existentes→DDS→resultados del caso. Se aplicaron los dos pasajes completos preparados en las VNext del README y USE_CASE: [publicación 56eb0252c63cedc7aa578e7c3a5c897cc9669c5e](https://github.com/dakleyer/use-cases/commit/56eb0252c63cedc7aa578e7c3a5c897cc9669c5e). El README explica caso/método/corpus y enlaza discusiones S5/S4; USE_CASE relaciona objetivo, contrato, Stage, evidencia y conclusión. Se conserva el resto de bytes de ambas fuentes mediante verificación inversa exacta. R0/R1/R2, A/B/C, criterios, hipótesis, anexos, figuras, freezes, código y resultados no cambiaron.

Las dos fichas aplicadas se retiraron de sus VNext activas y quedaron en Git/custodia auténtica; las auditorías y otras propuestas pendientes permanecen. Sólo cuatro archivos cambiaron en la rama: los dos lectores y sus dos VNext;73otrosblobs idénticos,0 nuevos/eliminados. La plantilla RUN_RECORD y la matriz EO anteriores no se aplicaron. SHA256SUMS.txt conserva su época anterior y no certifica los dos lectores nuevos. Main use-cases y el envío congelado permanecen intactos.

La Issue pública mantiene sus enlaces de envío. El [README VNext](https://github.com/dakleyer/use-cases/blob/when-controls-work-system-fails-v0.9.3/contributions/when-controls-work-system-fails/README_VNext.md) deja preparado un único párrafo adicional con antes/después literal, Alto impacto/Bajo riesgo/Bajo esfuerzo, para enlazar seguimiento y DDS manteniendo el snapshot. Es una edición externa pendiente de decisión concreta. No se modificó la Issue, abrió otra campaña S5, creó carpetaDDS ni ejecutó migración o experimento. Este estado supersede las menciones previas a esas dos inserciones como pendientes; no altera los otros gates abiertos.


<details>
<summary>Historial de las propuestas incorporadas</summary>

<a id="texto-antes--existing-v02-rule-complete-affected-validation-passage"></a>
<a id="texto-después--successor-candidate-complete-new-source"></a>
<a id="texto-antes--original-module-description"></a>
<a id="texto-después--published-module-description"></a>
<a id="texto-después--full-new-cross-stage-projection-function"></a>
<a id="texto-antes--complete-previous-compile_successor"></a>
<a id="texto-después--complete-published-compile_successor"></a>
<a id="cambio-76--precisión-de-la-primera-nota-de-stage-a"></a>
<a id="plan-de-cambios-al-final--variante-textual-del-75"></a>
<a id="ola-2--cambio-6-dds-tres-etapas-y-dos-fases-internas-de-stage-a"></a>
<a id="nota-extension-stage-clarification013-al-principio"></a>
<a id="ola-2--redacción-directa-del-cambio-6"></a>
<a id="nota-extension-stage-clarification013-al-principio-1"></a>
<a id="aplicaciones-confirmadas--12-octubre-2026"></a>
<a id="bloques-aplicados-retirados"></a>
<a id="ola2-cambio-06"></a>
<a id="ola2-redaccion-06"></a>

Las fichas retiradas se conservan completas en la [edición anterior](https://github.com/dakleyer/structural-awareness-contributions/blob/884e892a6fe1d0deffea493931c9fc5acf8e0258/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md). Los enlaces anteriores siguen llevando a este historial.

</details>


## Tanda 1 de navegación: adición al índice DDS — 12 octubre 2026

**Comprobación terminológica previa.** Se leyeron UC-21 Conventions/Extensionality, DDS A §3/§6/§10A, DDS B/C, R01, el protocolo de extensiones, kernel E1–E7, HEW Technical Report, DBC, 00D, Requirements y los índices RA/MSCA pertinentes. La búsqueda pública de usos complementó esas lecturas; no equivale a leer cada documento histórico. Challenge define problema/familia; el escenario delimitado lo instancia. UC-21 mantiene S1–S6 y sus familias 00E–00J. HEW usa escenario como descripción humana con instancia formal. Campaña de investigación, campaña operativa de S4 y unidad de campaña R01 no son intercambiables. Ejercicio se usa como entrada de lectura para estudios/recorridos existentes, no como nuevo tipo normativo. A/B/C DDS, A–D causales, A/B/C/D epistemológicos, R0/R1/R2 UC-21 y R01-R1/R2/R3 siguen con sus fuentes. La adición inicial que identificaba escenario con problema se corrigió antes de publicarse.

Iván autoriza ejecutar adiciones de navegación conservando contenido. El índice mantiene su autoridad y body; el añadido reúne rutas propietarias y trece reportes ya existentes, sin agruparlos como una sola campaña. La terminología inicialmente simplificada se corrigió antes de publicar. Faltan lecturas terminológicas de todos los documentos históricos: esta adición cita fuentes, no impone nombres universales nuevos. [EP VNext](https://github.com/dakleyer/structural-awareness-contributions/blob/main/architectural-contributions/ecosystem-positioning/README_VNext.md) contiene plan y gates. Estado de estas adiciones: autorizadas para incorporación, todavía no aplicadas en esta versión de revisión.


**Aclaración de Iván — ruta ratificada:** UC-21→objetivos→Challenges→DDS→campañas→resultados. Dentro de DDS, escenario de evaluación designa la aplicación de una tecnología/configuración a un Challenge. Se conserva la distinción de la fuente entre instancia/base delimitada y technology mapping/profile; no se sustituyen los nombres de los originales ni se transforma la campaña operativa S4 en campaña de investigación.


**Hallazgo de versión:** el paquete de revisión S5 enlazado en la discusión no está en el árbol main90a3135. Su README sí se recupera íntegro en el pin2c7f545 citado originalmente. La nueva ruta conserva ese enlace inmutable y no inventa una copia vigente. La segunda tanda debe registrar también dependencias de commits anteriores, no sólo archivos del head.


## Incorporación de la primera tanda de lectura — 12 octubre 2026

Iván autoriza ejecutar la ruta UC-21→objetivos→Challenges→DDS→campañas→resultados. Las adiciones descritas aquí se incorporan conservando todos los bytes previos y vínculos de las fuentes. La terminología de lectura remite a sus propietarios: Challenge, escenario base, escenario de evaluación/perfil tecnológico y campañas/operaciones mantienen sus contextos. No se renombra un archivo, se modifica un contrato o se ejecuta una campaña.

La ficha de esta tanda aplicada se retira de la cola activa; sus textos completos están en la [versión de preparación](https://github.com/dakleyer/structural-awareness-contributions/blob/ccf0d4b897eb56498de8fd64d97bf94af496e614/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md). El plan de las tandas 2–6 sigue vigente: inventario de dependencias/versiones, agrupación con unidad explícita, informes de campaña y conciliación. La entrada de Issue se actualiza después de verificar las fuentes publicadas. Sus enlaces de envío se conservan.


## Tanda 2 — inventario de rutas, versiones y dependencias · 12 octubre 2026

**Revisión realizada por Codex, mismo asistente.** Iván confirma que «no cambiar nada» significa conservar la información: autoriza continuar las ayudas de navegación, sin borrar contenido. El UC-21 en PDF y su entrada pública quedan para el final. La ruta de trabajo sigue UC-21 → objetivos → Challenges → DDS → campañas → resultados.

Se obtuvieron los árboles completos y los bytes de los cortes Contributions `af344bd93d8e0ae0e9912dbc08055ded3b25cd25` (2.200 archivos) y rama UC-21 `aafc9a49346a7b2030563d3b8c1bde51de3c6446` (77 archivos). Cada uno de los 2.277 blobs se cotejó contra su identidad Git. Se extrajeron enlaces Markdown de las 967 páginas de Contributions y las 38 de la rama del caso; el análisis distingue documentos actuales, VNext y archivos preservados. Las rutas explícitas y fragmentos examinados en los Markdown actuales resolvieron; no se extiende ese resultado a todos los enlaces web, comandos o formatos de manifiesto.

La lectura humana detecta 19 documentos actuales sin enlace Markdown entrante: dos documentos del diagnóstico, un perfil FG-TIDA, cuatro guías de la segunda serie, tres guías/recapitulaciones compartidas y nueve explicaciones de coste/tipos. Las nueve últimas ya están referidas por los registros JSON; falta acceso directo para el lector. Se añaden tres accesos desde el índice DDS y dieciséis desde el índice de extensiones. La modificación es navegación, no una nueva prueba científica.

Los trece CURRENT_STUDY_RECORD conservan su pregunta y Stage A/Simplified. Se comprobaron 186 referencias de archivo explícitas dentro de esos registros, con cero ausentes. Se verificaron 173 bindings SHA-256 de los mapas `files` de FREEZE/MANIFEST en extensiones, sin divergencias en ese alcance, y los cinco blobs del instrumento diagnóstico v0.2 coinciden con su freeze. El perfil FG-TIDA v0.2 consume expresamente el diagnóstico v0.1: se explica esa relación, sin reemplazar su dependencia por v0.2 o v0.3.

La custodia de 92 copias al pin409bfa9 sigue identificando su origen auténtico. En el receptor actual, 70 permanecen idénticas y 22 evolucionaron: 16 documentos y seis revisiones. Se cotejaron las diferencias documentales: lectura A/B/C, sucesores coste/tipos y aclaraciones de resultados, sin convertir las copias en campañas independientes. Las 16 fuentes correspondientes en feasibility mantienen sus blobs originales. Las seis VNext tienen evolución propia; no se abre otro expediente ni se declara independencia por duplicación.

Se verificaron los árboles de 39 referencias históricas de estos dos repositorios, recuperando cada destino citado por Markdown actual. Incluyen el envío UC-21 aec08fb5, la custodia409bfa9 y el paquete S5 en2c7f545, ausente del main actual. La existencia y ubicación del paquete S5 están comprobadas; su ZIP no se ejecutó aquí. Los enlaces externos de otros propietarios mantienen sus versiones y quedan para la revisión de las relaciones materiales, sin asimilarlos a archivos del head.

**Prioridad Primera; impacto Alto; riesgo Bajo para estas adiciones; esfuerzo Medio.** Beneficio: el lector llega a guías, evidencia y versiones sin depender de claves JSON o de adivinar carpetas. Riesgo concreto: confundir un documento actualizado con el input de un run; se conserva el pin/freeze y se explica la distinción. Coste: lectura de los materiales identificados, cotejo de destinos y mantenimiento de tres pequeñas adiciones. La auditoría de identidad no cierra las pasadas científicas ni las tandas 3–6.

El [plan común](https://github.com/dakleyer/structural-awareness-contributions/blob/main/architectural-contributions/ecosystem-positioning/README_VNext.md) sigue fijando el orden. No se reubica, renombra o elimina un archivo; el contenido previo se conserva byte por byte. Los before/after completos se registran en las VNext propietarias antes de incorporar las adiciones. La ficha aplicada se retira de la cola activa y permanece en Git history.


## Tanda 2 aplicada — decisión concreta de Iván, 12 octubre 2026

Iván responde «Adelante, muy bien» a la solicitud que identifica las tres adiciones a DDS_CANONICAL_METHOD_INDEX_v0.1.md, extensions/README.md y README UC-21. Se incorporan exactamente esos bloques y se conserva cada byte anterior de las fuentes. Esta decisión resuelve el bloqueo registrado antes; el PDF y la entrada externa siguen para el final.

Se retiran únicamente las fichas literales de esas adiciones ya incorporadas. Sus pares completos siguen en la edición de preparación publicada: https://github.com/dakleyer/structural-awareness-contributions/blob/b8729701ff0303363d48fe63a629587d4b12a6e2/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md. Auditoría, explicaciones, instrucciones y propuestas anteriores abiertas permanecen. Cero archivos creados, eliminados, movidos o renombrados; código, resultados, fuentes congeladas y manifiestos íntegros. Continúa la tanda 3 sobre objetivos, Challenges y escenarios/ejercicios, dentro de las VNext actuales.


## Tanda 3 — objetivos, Challenges y escenarios de evaluación · 12 octubre 2026

**Revisión realizada por Codex, mismo asistente.** Iván autoriza las tres adiciones concretas de la tanda2 y pide preparar y continuar la siguiente. Esas adiciones ya están publicadas en Contributions `2ff085688de77938aeaa5a3c0e7edbb607247d58` y la rama UC-21 `285ca77fc4cc5d69f3ea78aeda820777c647d0da`, con todos los bytes anteriores de las fuentes conservados. El PDF y la entrada pública se reservan para el final. Esta tanda publica revisión y cuatro propuestas; su incorporación requiere el GO de esta tanda.

Se cotejaron los cinco objetivos reunidos en README/USE_CASE, las 37 condiciones de los planes del caso, los núcleos/admisión X1–X7 de Annex X, selección de HC/HR/HS/H1–H6, las condiciones de recurrencia y los nueve perfiles T01–T09. Las lecturas de escenarios y perfiles se centraron en problema, plan, variantes, comparadores y fuentes/versiones relevantes al itinerario; no se declara una nueva auditoría completa de cada apéndice histórico. Se contrastaron los trece registros actuales por su propia pregunta/configuración/closure, y el README externo S5 al pin a9eca743df5a5c1fbef5dc6f792ea08f8add29e0, blob4b0d2a673c8ee945bd6c52248390a3c595b9285a. No se ejecutaron productos, simuladores o experimentos.

**Qué se sostiene.** La línea común es la decisión receptora con evidencia, autoridad, tiempo, capacidad y efecto. Las seis familias mantienen mecanismos diferentes: síntesis, composición de recurso compartido, misión/fuentes, hallazgo versus autoridad, validez al actuar y proposición de derechos. Sus 37 gates, nueve perfiles y27posiciones documentales no son37/9/27resultados ejecutados. La nueva lectura «Challenge» organiza las familias y «escenario de evaluación» relaciona tecnología/configuración con condiciones; se conservan S1–S6, escenarios base y los nombres existentes.

**Qué hay que conciliar.** El índice baseline abre00H v0.2, mientras v0.5 y el S4 del paquete desarrollan el núcleo de sobrealcance/pérdida y V19/V20. No es pérdida física de información: ambas versiones existen. Es una ruta inicial incompleta para esa lectura. Se propone un enlace explícito al sucesor y conservación del antecedente, sin reasignar resultados delfreeze. S3 declara su copia obsoleta y remite a00G mantenido; S6 ya es adapter a00J. No se restaura una segunda fuente ni se elimina la historia.

**Comparaciones que no se pueden fusionar.** R0/R1/R2 del caso distingue configuración ordinaria, corrección reforzada y recurrencia con esa misma corrección retenida. El S5 externo declara I0 ordinario, I1 parcialmente defendido que aún falla, e I2 que corrige ramas conocidas del modelo suministrado. Su I2 no es AWS-I2/R2, ni su I1 prueba una corrección previa apta para HR. Los A–D causales, A/B/C/D epistemológicos y Stages DDS son dimensiones separadas. La frontera «blind» del simulador es acceso del candidato a inputs; no acredita un auditor humano independiente.

**Reutilización con sentido.** Los trece registros responden preguntas locales distintas y se declaran Stage A/Simplified completos dentro de esa pregunta. Hay mecanismos útiles para evidencia, identidad, uso temporal, receipts, continuidad y respuesta, pero esos registros no declaran por sí mismos pertenencia a una familia UC-21 ni ejecución de HC/HR/HS para ella. El paso de reutilización especifica mapa de relaciones, failure predicate, control positivo y recursos usando X1–X7 y DDS§4. No se exige volver a ejecutar una batería universal ni se suman denominadores heterogéneos.

**Criterio estratégico.** Cuatro adiciones de lectura, Alto impacto esperado/Bajo riesgo/Medio esfuerzo. El beneficio es elegir la pregunta, versión y evidencia correcta antes de crear un ejercicio. Riesgo: el lector puede confundir una ruta vigente con una edición ejecutada o heredar conclusiones por parecido; las propuestas identifican la versión, pregunta y contrato. El esfuerzo incluye cotejo de fuentes, enlaces y mantenimiento, además de redacción. No cambian requisitos, gates, umbrales, hipótesis, fuentes congeladas o resultados. Prioridad Primera; ejecutar como una tanda coherente sólo tras GO: baseline00H → guía del caso → DDS selección → preguntas de extensiones.

### Juicio del contrato DDS

DDS§3 define Challenge independiente de tecnología y escenario/fixture/reducción delimitado. §4 exige declarar correspondencia, cambios de parámetros y mecanismos adicionales; llamar isomorfismo al parecido no está admitido. §6 distingue perfil, traversal, trace y campaña. §10A ya separa los I0/I1/I2 externos y AWS; la propuesta de índice hace esa distinción legible, sin duplicar la norma. La selección del caso y claim precede la asignación de Stage por objeto/referencia. No se propone modificar el contrato Stage A ni su namespace.


Relación revisada en ambos extremos: [plan EP](https://github.com/dakleyer/structural-awareness-contributions/blob/2ff085688de77938aeaa5a3c0e7edbb607247d58/architectural-contributions/ecosystem-positioning/README_VNext.md), [DDS VNext](https://github.com/dakleyer/structural-awareness-contributions/blob/2ff085688de77938aeaa5a3c0e7edbb607247d58/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md), [baseline VNext](https://github.com/dakleyer/structural-awareness-contributions/blob/2ff085688de77938aeaa5a3c0e7edbb607247d58/research/ecosystem-awareness/baseline/README_VNext.md), [extensiones VNext](https://github.com/dakleyer/structural-awareness-contributions/blob/2ff085688de77938aeaa5a3c0e7edbb607247d58/research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/README_VNext.md) y [caso VNext](https://github.com/dakleyer/use-cases/blob/285ca77fc4cc5d69f3ea78aeda820777c647d0da/contributions/when-controls-work-system-fails/README_VNext.md). Las entradas se atribuyen al mismo asistente; no se inventa consenso ni una revisión independiente.


## Tanda 3 aplicada — GO de Iván, 12 octubre 2026

Iván autoriza continuar después de la entrega de las cuatro propuestas de la tanda3. Se incorporan exactamente sus adiciones a baseline README (sucesor00H), README UC-21 (seis Challenges), DDSIndex (elección del ejercicio) y extensions README (preguntas de trece estudios). Todos los bytes previos de esas cuatro fuentes permanecen íntegros, con sus enlaces. No se modifica otro pasaje ni el PDF.

Las cuatro fichas incorporadas salen de la cola activa; su antes/después completo está en la [preparación publicada](https://github.com/dakleyer/structural-awareness-contributions/blob/db248c134318c8786471eec1ef0ead2248b360a6/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md). Auditorías y decisiones anteriores se conservan. Cero archivos nuevos, movidos, renombrados o eliminados y ninguna VNext nueva. Los estudios conservan registros, inputs, resultados, código, freezes y manifiestos. Continúa la tanda4: método, instrumentos, comparadores y oráculo/harness, con propuestas nuevas pendientes del GO correspondiente.


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

Iván autoriza continuar después de la tanda4 y pide que todas las tandas aprobadas estén en main. Se incorporan exactamente las cuatro adiciones a DDSIndex, oracle README, UC4 bridge y adapter guide. Sus bytes anteriores y enlaces permanecen íntegros. Las cuatro fichas incorporadas salen de pendientes; los pares completos quedan en la [preparación publicada](https://github.com/dakleyer/structural-awareness-contributions/blob/bb432e8a9e2809612d2b721b3660974362c34879/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md). Se conservan auditorías y otras decisiones abiertas.

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

### Plan aplicado — Mapa de informes por unidad de investigación

Aplicado en main por autorización de Iván del 12 octubre 2026. El par completo se conserva en el predecessor Git `77fc61447d3f278072d13f566bbedd7ccfe245d3`; queda fuera de la cola pendiente.

## 15. Recorded work and its owning reports

Read the report that owns the question before its run data. The routes below collect existing work without making a new campaign out of a folder, replay or file count.

| Recorded work | Owning report / evidence route | Unit and reading purpose |
|---|---|---|
| Thirteen local technology studies | [Study and successor lineage](./baseline/reductions/00G-R01/extensions/README.md#follow-the-evidence-from-original-study-to-successor) | Bounded questions, original cases, cost/type and repair successors. |
| Six-principle symbolic work | [00K campaign summary](./baseline/00K_A04_SIX_PRINCIPLE_SYMBOLIC_EXECUTION_CAMPAIGN_SUMMARY_v0.1.md#current-regression-count--12-october-2026) and [execution router](./baseline/fixtures/00K-SUITE/README.md) | Regression assertions over declared fixtures and their retained falsifiers. |
| Six-family paper/symbolic traversals | [00L reports](./baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/README.md) | Conditional paper traces, symbolic records and correction/reproduction history. |
| S5 state/effect and recovery | [00I-STATEFUL report](./baseline/fixtures/00I-STATEFUL/README.md) | Local synthetic stateful execution and its SQLite/process-recovery companion. |
| HF receiver comparisons | [HF report-selection guide](./baseline/reductions/00G-R01/extensions/hugging-face/README.md#recorded-comparisons-and-their-results) | Paired programmed receiver paths, cached-lineage and configured Casbin-polling findings. |
| HF probabilistic/social/dynamic work | [R123](./baseline/traversals/00G-HF-PROBABILISTIC-R123-v0.1/RESULTS.md), [social propagation](./baseline/traversals/00G-HF-CONTINUOUS-SOCIAL-v0.1/RESULTS.md), [dynamic review](./baseline/traversals/00G-HF-DYNAMIC-REVIEW-v0.1/results/RESULTS.md) | Networks and receiver/checkpoint records in different constructed campaigns; these lots contain no EA arm. |
| Instrument calibration | [R01 calibration v0.9](./baseline/reductions/00G-R01/oracle/SELFTEST_RECORD_v0.9.md) | Controls of the evaluator infrastructure, kept separate from technology-study outcomes. |

[UC-21's maintained package on main](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/README.md) connects objectives and Challenges to these routes. A case conclusion cites the particular report/version and evidence it uses. Existing registrations retain the names, units and stopping rules under which their work was recorded.
````


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
| 74 | Rechazar sustitutos NA de tipo string antes de adjudicar | research/ecosystem-awareness/gate-diagnostic/check_gate_profile_v0.4_audit_candidate.py | Aplicado en sucesor |

El checker v0.4 conserva la delegación a v0.2 y las proyecciones T05/T06 de v0.3. Treinta controles locales pasan: siete C74 con los tipos y la dependencia real true/false/ausente, siete T06 y dieciséis T05. El string `false` se rechaza antes de la compilación; el booleano false bloquea la dependencia y true la satisface. Los dos checkers previos, registros y resultados permanecen intactos. No se ejecuta una campaña DDS. [Código sucesor](./gate-diagnostic/check_gate_profile_v0.4_audit_candidate.py) · [controles C74](./gate-diagnostic/test_na_substitute_v04.py).



## Tanda 6 — conciliación de navegación UC-21 / DDS · 12 octubre 2026

Revisión por Codex, mismo asistente. Iván pide preparar y continuar la siguiente tanda. Corte: Contributions `582a1b87b18c651beff8dd8a8f2d590cf50aace6` y use-cases main `e9efbda5e0cc002793a4df82484a6b3f47a79976`. Las 31 incorporaciones anteriores están publicadas; esta tanda prepara seis ajustes nuevos, sin incorporarlos a las fuentes. Es la sexta tanda del plan de navegación, no la sexta auditoría científica del corpus.

### Lectura desde el caso y retorno de evidencia

DDS conserva los trece estudios y sus rutas a 00K, 00L, 00I, HF y R01. En §§11/13, siete referencias presentadas como actuales abren aún la rama anterior de UC-21. Sus destinos existen en `188f319`; el README mantiene allí la redacción anterior al cambio de snapshot en main. El cambio77 lleva esas entradas a main y conserva las siete URI como historia. El cambio81 distingue envío, paquete mantenido, freeze del estudio y versión del instrumento, y enlaza el checker v0.4 ya publicado. El manifest v0.2 y el perfil FG-TIDA que consume v0.1 mantienen sus contratos.

El retorno al caso conserva scope y claims. El S5 externo mantiene el pin v0.1.3 y sus predicados asumidos upstream; su autor recomienda cierre acotado. S4/CDA sigue siendo una propuesta separada del baseline R0/R1. El comentario nuevo de Iván plantea transformar un hallazgo delimitado en otro control candidato; sus pasos A–F no son etapas DDS. Una versión posterior del checker no rediagnostica los runs anteriores.

Las 186 referencias y 173 bindings congelados seleccionados conservan sus destinos y bytes. El cotejo de enlaces apoya esta conciliación de navegación; el ciclo científico completo se sigue evaluando en sus expedientes.

### Revisiones en ambos extremos

[Visión conjunta EP](https://github.com/dakleyer/structural-awareness-contributions/blob/main/architectural-contributions/ecosystem-positioning/README_VNext.md) · [DDS](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md) · [baseline](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/README_VNext.md) · [extensiones](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/README_VNext.md) · [puente UC4](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/reductions/00G-R01/oracle/UC4_INTEROPERABILITY_PROFILE_VNext.md) · [UC-21 README](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/README_VNext.md) · [caso](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/USE_CASE_VNext.md).

### Cambio 77 — Leer UC-21 desde main en las siete rutas DDS

**Aplicado en main — autorización de Iván, 12 octubre 2026.** Cambio 77 incorporado y fuera de pendientes. El par completo y su ficha anterior se conservan en el predecessor Git de esta aplicación.

### Cambio 81 — Dar acceso al checker corregido manteniendo la edición congelada

**Aplicado en main — autorización de Iván, 12 octubre 2026.** Cambio 81 incorporado y fuera de pendientes. El par completo y su ficha anterior se conservan en el predecessor Git de esta aplicación.



## Migración conservadora completada en los repositorios — 12 octubre 2026

Iván autoriza completar la migración y preservar toda la información y sus rutas. Se incorporan los seis cambios77–82 mediante sus trece pasajes exactos, con nueve enlaces de orientación actualizados y sus referencias anteriores conservadas. No se mueve ni renombra ningún archivo. Las fuentes mantienen todo el contenido fuera de esos pasajes; los anexos añadidos son bloques al final.

El cotejo encontró dos archivos históricos del paquete S5 que ya faltaban de main antes de esta tanda: README y ZIP. Ambos vuelven a sus rutas originales con los mismos blobs del commit2c7f545. El ZIP conserva123.884bytes y SHA2569ea1ac54378018e60809f6dff63613fc41d6c0cf53c4ac952345f1e927c51bb8; sus25miembros pasan comprobación CRC, sin ejecutar scripts. La restauración se presenta en la hoja adicional EA, con su edición y finalidad histórica. El paquete v0.1.3 de Steven y sus límites posteriores mantienen su propio registro.

El README UC-21 añade al final acceso a todos los archivos de su paquete, los materiales de envío y los archivos de trabajo del registro. El anexo adicional EA enlaza el soporte compartido, los originales R01 y la historia de revisión. Las tres hojas auxiliares EA/RA/MSCA mantienen su organización; no se crea una colección de índices ni niveles nuevos. El envío aec08fb5, los freezes y los resultados siguen con sus identidades.

Comprobación final compartida:2.283rutas accesibles por los lectores y carpetas enlazadas;2.006destinos anteriores conservados en los cinco documentos intervenidos;13sustituciones inversas exactas, cero cambios fuera de alcance; README/ZIP históricos restaurados idénticos. El detalle permanece en EP VNext.


## Informe auditable de la reestructuración UC-21 / DDS — 13 octubre 2026

Iván autoriza publicar el [informe completo de la sesión](https://github.com/dakleyer/structural-awareness-contributions/blob/main/governance/review/migration-audit-2026-10-13/Informe_auditable_DDS_y_corpus_sesion_2026-10-13.html) como trazabilidad de los cambios de navegación y de las incorporaciones aprobadas. Reúne 75 commits consultados, 304 rutas y 76 pares literales antes/después, con razones, autores, versiones, restauraciones y comprobaciones de conservación. El HTML se puede descargar y leer sin recursos externos; su [manifiesto SHA-256](https://github.com/dakleyer/structural-awareness-contributions/blob/main/governance/review/migration-audit-2026-10-13/Informe_auditable_DDS_y_corpus_sesion_2026-10-13_MANIFEST.json) identifica el archivo exacto entregado.

El informe documenta las actuaciones del 6 al 12 de octubre, con cortes `9056ed78e3e79c025f253cfbc823ccc0293064a4` (Contributions) y `0d32667ccce1dd3e568459a64a89e83987d92d4e` (use-cases). La publicación parte de `b5d126cc877c7e4c6bb7fe45bfa7173a128a6023` y conserva las incorporaciones posteriores. Es un registro retrospectivo de la reestructuración; el estado de cada investigación se consulta en su expediente vigente. No constituye otra VNext ni otro nivel de README.


## Cierre de entrada UC-21 — 13 octubre 2026

### Qué se volvió a leer y qué cambió

Revisión documental por Codex, mismo asistente, 13 octubre 2026. Fuentes: raíz y paquete UC-21 en use-cases `0d32667ccce1dd3e568459a64a89e83987d92d4e`; Contributions `fc90cdc78e8c593ddb848f988962e27b00f00c93`; README de FG-TIDA `5ae72ac3094a2712d8b9b75d11bbb928b6859fe6`. Se consultaron la Issue y sus 36 comentarios; updated_at de la Issue `2026-10-13T10:36:49Z` no se toma como fecha de modificación de cada campo.

La tabla oficial omite UC-21 aunque la Issue existe. En el fork hay una entrada de paquete al final, pero tampoco fila 21 en Submissions. El README del caso mezcla una cabecera de envío de septiembre, vínculos de integración de de677309 y navegación mantenida posterior. Sus objetivos, Challenges y acceso completo ya funcionan: se mejora la entrada, no se crea otro dueño ni se repite la matriz EO descartada.

La revisión anterior alcanzaba 33 comentarios. Ahora constan Nelson #6132541771, Matías #6138082870 e Iván #6143678176. Nelson delimita coordinación y colaboración opcional; Matías informa su candidato y sus controles; Iván propone secuencia paralela y separación de funciones. La lectura del tag CDA v0.1.3 resolvió el commit `7b6b24d416bf78a7e2599ccda932745ebe839fff`; se leyó su README. No se ejecutó su software ni se verificaron independientemente los conteos que comunica el autor.

La recomendación S5 de Zhao #6115830369 sigue siendo cierre al alcance evidenciado del modelo. Se conserva ese resultado y las hipótesis upstream; no se reabre su ejercicio por el solo hecho de preparar una colaboración. El puente R01 mantiene R01-BRIDGE-DRAFT: los nuevos comentarios no revisan su schema ni conceden UC4-SOURCE-REVIEWED.

La Issue conserva once casillas sectoriales frente a cuatro en el formulario fuente; es una discrepancia ya documentada. Este cierre de navegación deja las casillas intactas. Una corrección o ampliación sectorial necesita la decisión específica de Iván; no impide enlazar el caso ni se resuelve copiando ciegamente el formulario.

La propuesta de adición al final de la Issue del 12 de octubre sigue como historia. El candidato 90 es su alternativa vigente de presentación al principio, preparado contra el cuerpo actual. No aplicar ambos. El anterior bloqueo 403 y rechazo de revisión automática se conservan como hechos de ejecución; esta preparación no reintenta la escritura externa.

La relación de recepción vuelve al caso; no modifica la metodología ni sus etapas. El registro Flores mantiene su dueño y estado de desarrollo.

### Cambio 88 — Conciliar en DDS las condiciones del seguimiento UC-4 / CDA

**Impacto Alto · riesgo Bajo · esfuerzo Medio · prioridad Primera. Estado: preparado, pendiente de GO; no aplicado.**

Beneficio: El receptor metodológico encuentra las mismas fuentes y condiciones de R1/R2, coordinación y revisión independiente que el caso.

Riesgo concreto: No alterar Stages A/B/C, freezes, contratos o resultados; la devolución del hallazgo se selecciona por pregunta y no crea dependencias por defecto.

Coste de lectura/validación/mantenimiento: Un párrafo de actualización que conserva íntegro su contexto anterior; cotejo con el receptor UC-4.

Dependencias: 85, 86. Revalidar fuente y pares, recibir GO de Iván sobre estos textos y comprobar el diff y lectura de vuelta.

**Pasaje 1:** `dakleyer/structural-awareness-contributions` → `research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md`. Ubicación: §11, párrafo de comparación específico UC-21; contextos posteriores Flores intactos. Fuente: commit `fc90cdc78e8c593ddb848f988962e27b00f00c93`; blob `88b78f386047a76e0e2da905bd951ada06e5602b`. Viejo localizado una vez.

**Texto antes — viejo literal completo del pasaje**

````markdown
For a UC-21-specific comparison, consult the [existing external S5 exercise](https://github.com/zhaoxinghua09-cell/silent-failure-catalog/blob/a9eca743df5a5c1fbef5dc6f792ea08f8add29e0/examples/S5-Qregister/README.md), [research-side audit packet](https://github.com/dakleyer/structural-awareness-contributions/blob/2c7f545e2610e154b2e7d11fe827722bbf3c5658/research/ecosystem-awareness/review-packets/2026-10-11-steven-s5/README.md) and [separate 00I-STATEFUL companion](./baseline/fixtures/00I-STATEFUL/README.md). The [S4/CDA follow-up](https://github.com/FG-TIDA/use-cases/issues/21#issuecomment-6111953753) retains its proposed state. These links do not combine their outcomes into one campaign.
````

**Texto después — propuesta completa**

````markdown
For a UC-21-specific comparison, consult the [existing external S5 exercise](https://github.com/zhaoxinghua09-cell/silent-failure-catalog/blob/a9eca743df5a5c1fbef5dc6f792ea08f8add29e0/examples/S5-Qregister/README.md), [research-side audit packet](https://github.com/dakleyer/structural-awareness-contributions/blob/2c7f545e2610e154b2e7d11fe827722bbf3c5658/research/ecosystem-awareness/review-packets/2026-10-11-steven-s5/README.md) and [separate 00I-STATEFUL companion](./baseline/fixtures/00I-STATEFUL/README.md). The [S4/CDA follow-up](https://github.com/FG-TIDA/use-cases/issues/21#issuecomment-6111953753) retains its proposed state. These links do not combine their outcomes into one campaign.

The [12–13 October UC-4 scope clarification](https://github.com/FG-TIDA/use-cases/issues/21#issuecomment-6132541771), [CDA v0.1.3 report](https://github.com/FG-TIDA/use-cases/issues/21#issuecomment-6138082870) and [UC-21 research sequence and independent-review roles](https://github.com/FG-TIDA/use-cases/issues/21#issuecomment-6143678176) define the current proposed follow-up. UC-4 retains its experimental coordination and source semantics. A selected UC-21 R2 follows a demonstrated and frozen R1 correction; R2 preparation and DDS Stage A review may proceed in parallel. Findings return to a separately reviewed candidate specification, preserving successful controls and unresolved observation limits. Read the [case's next investigations](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/README.md#next-investigations-and-evidence-decisions) for the work and decisions still required.
````



## Direct UC-21 entry in Contributions — 13 October 2026

Ivan selects one maintained research corpus: **FG-TIDA Issue #21 → Contributions → UC-21 research questions → Challenge sources → DDS → registered studies and results**. The fork is a source archive, not another maintained canonical reader entry. New public preparation is written in English.

The prior fork-based changes 83–90 are superseded as a proposed wave and must not be applied as prepared. Their old/proposed text and audit history remain intact. The official-index row may be re-proposed separately if needed; updating a fork index is no longer part of the current route.

Current tree: Contributions `f960f6f5a627993643512b816430a485227f9118`, 2,249 files. DDS, 00E–00J source families, instruments and reports already exist here. The maintained fork still contains the full UC-21 case, twenty annexes, claim/recurrence protocols, assets and templates. This review has not found a complete second copy of that case package in Contributions. Replacing links alone is not a full source migration; no copied corpus or new repository is created to hide that distinction.

The proposed first step reuses the existing DDS Canonical Method Index. It presents the five questions and six current Challenge sources while retaining original source protocols as pinned historical dependencies. The official Issue would then receive the exact primary-link replacement below. This preserves the submitted edition without routing current research through a moving fork branch. A later decision to integrate the entire case would first classify identical sources, unique content and necessary paths in a manifest; no archive or source is deleted or moved by this preparation.

**Order:** incorporate and verify 92, then incorporate 91 at the official Issue with its owner's access and approval of the exact text. Complete source-package consolidation is a separate unresolved decision, not an accomplished migration. The official Issue remains unchanged during preparation; prior 403/automatic-review history is retained without an attempted bypass.

### Exact change plan

### Change 92 — Make the existing DDS index the Contributions reader entry for UC-21

**Expected impact: high. Risk: medium. Effort: medium. Status: prepared, not applied.**

Benefit: Five existing research questions and six Contributions Challenge sources become directly readable in the one existing method router; live fork links become preserved source/history references.

Risk: Case-specific protocols and general DDS contracts must retain their meaning. The complete twenty-annex package is not silently presumed to exist in Contributions; its pinned source records stay accessible.

Validation and maintenance cost: Ten identified passages, full inverse comparison, source-version and fragment checks, and reciprocal reader review. A later full integration requires a content manifest and its own exact proposals.

Order and decision: Ivan approves these exact reader passages. No physical migration, file deletion, normative protocol replacement or new README is authorized by this pair set.

**Passage 1.** §11, after the reader-route paragraph. Source `research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md`; commit `f960f6f5a627993643512b816430a485227f9118`, blob `88b78f386047a76e0e2da905bd951ada06e5602b`. Old text occurs once.

**Text before — complete literal passage**

`````markdown
The reader route is **UC-21 → objectives → Challenges → DDS → campaigns → results**. Within DDS, the technology/version/configuration is mapped to a Challenge through a specified evaluation scenario/profile. The source method records the bounded base scenario and technology mapping separately; its original meaning, frozen facts and labels remain intact.
`````

**Text after — complete proposed passage**

`````markdown
The reader route is **UC-21 → objectives → Challenges → DDS → campaigns → results**. Within DDS, the technology/version/configuration is mapped to a Challenge through a specified evaluation scenario/profile. The source method records the bounded base scenario and technology mapping separately; its original meaning, frozen facts and labels remain intact.

### UC-21 research questions

The [official UC-21 case record](https://github.com/FG-TIDA/use-cases/issues/21) supplies the case and acceptance conditions. Contributions is the maintained research corpus. Select the question first, then its Challenge, technology/configuration and evidence contract.

| Objective | Research question |
|---|---|
| Decision correctness and legitimate continuity | [Case acceptance plans](USE_CASE.md#6-six-quality-plans-visible-acceptance-criteria) | |
| Effectiveness of existing controls | [R0/R1/R2 comparisons](USE_CASE.md#5-select-prepare-and-run-one-experiment) | |
| Recurrence after correction | [HR recurrence protocol](annexes/RECURRENCE_PROTOCOL.md#annex-r) | |
| Common causal pathway | [HC causal protocol](annexes/HYPOTHESES.md#2-the-principal-hypothesis-of-causal-sufficiency) | |
| Sufficient common response | [HS response protocol](annexes/HYPOTHESES.md#9a-the-hypothesis-of-a-sufficient-common-response) | |

The source-specific HC, HR, HS and H1–H6 protocols retain their registered meaning. Their complete case texts are preserved in the submitted and pre-consolidation case snapshots, linked as source records below. This guide connects the existing Contributions research; it does not claim that the complete twenty-annex case package has already been integrated into this repository.

### UC-21 Challenge sources

The S1–S6 slots correspond to the following Contributions sources. Choose the exact edition consumed by a study; a current reader source does not replace its earlier freeze.

| Challenge slot | Failure family | Contributions source |
|---|---|---|
| S1 / 00E | Enterprise synthesis | [00E](./baseline/00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) |
| S2 / 00F | Shared mobility | [00F](./baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_DRAFT.md) |
| S3 / 00G | Propagated false mission | [00G](./baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md) |
| S4 / 00H | Finding beyond authority | [00H](./baseline/00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.5_DRAFT.md) |
| S5 / 00I | Delayed repair | [00I](./baseline/00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_READER_EDITION.md) |
| S6 / 00J | Rights-provenance inversion | [00J](./baseline/00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md) |

`````

**Passage 2.** Existing reader passage: | What is UC-21 trying to establish? |. Source `research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md`; commit `f960f6f5a627993643512b816430a485227f9118`, blob `88b78f386047a76e0e2da905bd951ada06e5602b`. Old text occurs once.

**Text before — complete literal passage**

`````markdown
| What is UC-21 trying to establish? | [UC-21 public entry](https://github.com/FG-TIDA/use-cases/issues/21) and [current objectives and reader guide](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/README.md#research-objectives) |
`````

**Text after — complete proposed passage**

`````markdown
| What is UC-21 trying to establish? | [Official UC-21 case record](https://github.com/FG-TIDA/use-cases/issues/21) and [research questions in this corpus](#uc-21-research-questions) |
`````

**Passage 3.** Existing reader passage: | Which scenario, reduction or extension supplies the problem? |. Source `research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md`; commit `f960f6f5a627993643512b816430a485227f9118`, blob `88b78f386047a76e0e2da905bd951ada06e5602b`. Old text occurs once.

**Text before — complete literal passage**

`````markdown
| Which scenario, reduction or extension supplies the problem? | [UC-21 scenarios](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/annexes/README.md), [R01 reference scenario](./baseline/reductions/00G-R01/Escenario-creatividad-validacion.md), [technology extension protocol](./baseline/reductions/00G-R01/extensions/TECHNOLOGY_EXTENSION_PROTOCOL.md) and [kernel/proof obligations](./baseline/reductions/00G-R01/extensions/family/KERNEL_AND_PROOF.md) |
`````

**Text after — complete proposed passage**

`````markdown
| Which scenario, reduction or extension supplies the problem? | [UC-21 Challenge sources](#uc-21-challenge-sources), [R01 reference scenario](./baseline/reductions/00G-R01/Escenario-creatividad-validacion.md), [technology extension protocol](./baseline/reductions/00G-R01/extensions/TECHNOLOGY_EXTENSION_PROTOCOL.md) and [kernel/proof obligations](./baseline/reductions/00G-R01/extensions/family/KERNEL_AND_PROOF.md) |
`````

**Passage 4.** Existing reader passage: For terminology, use [Stage A §3]. Source `research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md`; commit `f960f6f5a627993643512b816430a485227f9118`, blob `88b78f386047a76e0e2da905bd951ada06e5602b`. Old text occurs once.

**Text before — complete literal passage**

`````markdown
For terminology, use [Stage A §3](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md#3-challenge-first): the Challenge is the problem or failure family, and a bounded scenario, fixture or reduction instantiates it. [Stage A §6](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md#6-segments-trajectory-gates-traversals-and-traces) distinguishes profile, traversal, trace and DDS battery/campaign. [UC-21 conventions](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/annexes/CONVENTIONS.md) retain the scenario and route labels. A research campaign, an S4 business campaign and R01's operational campaign are different source contexts and accounting units. Reduction/extension transfer follows its owning proof or family-admission contract; navigation does not merge them.
`````

**Text after — complete proposed passage**

`````markdown
For terminology, use [Stage A §3](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md#3-challenge-first): the Challenge is the problem or failure family, and a bounded scenario, fixture or reduction instantiates it. [Stage A §6](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md#6-segments-trajectory-gates-traversals-and-traces) distinguishes profile, traversal, trace and DDS battery/campaign. [preserved UC-21 conventions](https://github.com/dakleyer/use-cases/blob/724d69f9cf69aaadd2f84f50934db9cf77fcc1f1/contributions/when-controls-work-system-fails/annexes/CONVENTIONS.md) retain the scenario and route labels. A research campaign, an S4 business campaign and R01's operational campaign are different source contexts and accounting units. Reduction/extension transfer follows its owning proof or family-admission contract; navigation does not merge them.
`````

**Passage 5.** Existing reader passage: The [submitted UC-21 snapshot]. Source `research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md`; commit `f960f6f5a627993643512b816430a485227f9118`, blob `88b78f386047a76e0e2da905bd951ada06e5602b`. Old text occurs once.

**Text before — complete literal passage**

`````markdown
The [submitted UC-21 snapshot](https://github.com/dakleyer/use-cases/tree/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails), the [maintained package on main](https://github.com/dakleyer/use-cases/tree/main/contributions/when-controls-work-system-fails), a registered study freeze and an instrument successor answer different version questions. Follow the cited snapshot for a recorded result and main for current reading. The [earlier case branch](https://github.com/dakleyer/use-cases/tree/when-controls-work-system-fails-v0.9.3/contributions/when-controls-work-system-fails) retains its preceding preparation. The [existing DDS review](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md) records the inventory and version decisions.
`````

**Text after — complete proposed passage**

`````markdown
The [submitted UC-21 snapshot](https://github.com/dakleyer/use-cases/tree/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails) and the [pre-consolidation case snapshot](https://github.com/dakleyer/use-cases/tree/724d69f9cf69aaadd2f84f50934db9cf77fcc1f1/contributions/when-controls-work-system-fails) preserve the original package and later reader work. Contributions hosts the current research route. A registered study freeze and an instrument successor retain their own edition; this navigation change does not revise a recorded result. The [existing DDS review](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md) records the source inventory and any integration still required.
`````

**Passage 6.** Existing reader passage: A case supplies the question and acceptance conditions. DDS supplies t. Source `research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md`; commit `f960f6f5a627993643512b816430a485227f9118`, blob `88b78f386047a76e0e2da905bd951ada06e5602b`. Old text occurs once.

**Text before — complete literal passage**

`````markdown
A case supplies the question and acceptance conditions. DDS supplies the study method. Read the [UC-21 Challenge guide](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/README.md#choose-a-challenge-and-its-evaluation-scenario), then select the bounded scenario, technology/configuration and evidence contract.
`````

**Text after — complete proposed passage**

`````markdown
A case supplies the question and acceptance conditions. DDS supplies the study method. Read the [UC-21 Challenge sources](#uc-21-challenge-sources), then select the bounded scenario, technology/configuration and evidence contract.
`````

**Passage 7.** Existing reader passage: | Objective and scientific claim |. Source `research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md`; commit `f960f6f5a627993643512b816430a485227f9118`, blob `88b78f386047a76e0e2da905bd951ada06e5602b`. Old text occurs once.

**Text before — complete literal passage**

`````markdown
| Objective and scientific claim | [UC-21 claim selection](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/annexes/HYPOTHESES.md#13-claim-selection) | Case acceptance, HC, HR, HS or the selected H1–H6 contrast. |
`````

**Text after — complete proposed passage**

`````markdown
| Objective and scientific claim | [UC-21 research questions](#uc-21-research-questions) and [official case assessment criteria](https://github.com/FG-TIDA/use-cases/issues/21#6-assessment-criteria) | Case acceptance, HC, HR, HS or the selected H1–H6 contrast; use the original claim-specific protocol identified by the study. |
`````

**Passage 8.** Existing reader passage: | Challenge and admitted variant |. Source `research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md`; commit `f960f6f5a627993643512b816430a485227f9118`, blob `88b78f386047a76e0e2da905bd951ada06e5602b`. Old text occurs once.

**Text before — complete literal passage**

`````markdown
| Challenge and admitted variant | [Family admission X1–X7](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/annexes/EXTENSIONALITY.md#4-admission-test-for-an-extension) and [DDS technology mapping](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md#4-technology-mapping) | Kernel, receiving boundary, failure predicate, inherited acceptance, positive control, resources and declared additions. |
`````

**Text after — complete proposed passage**

`````markdown
| Challenge and admitted variant | [Preserved case-family admission X1–X7](https://github.com/dakleyer/use-cases/blob/724d69f9cf69aaadd2f84f50934db9cf77fcc1f1/contributions/when-controls-work-system-fails/annexes/EXTENSIONALITY.md#4-admission-test-for-an-extension) and [DDS technology mapping](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md#4-technology-mapping) | Kernel, receiving boundary, failure predicate, inherited acceptance, positive control, resources and declared additions. |
`````

**Passage 9.** Existing reader passage: | Implementation comparison |. Source `research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md`; commit `f960f6f5a627993643512b816430a485227f9118`, blob `88b78f386047a76e0e2da905bd951ada06e5602b`. Old text occurs once.

**Text before — complete literal passage**

`````markdown
| Implementation comparison | [UC-21 R0/R1/R2](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/USE_CASE.md#5-select-prepare-and-run-one-experiment) | The tested configuration and, for recurrence, the demonstrated R1 correction retained in R2. |
`````

**Text after — complete proposed passage**

`````markdown
| Implementation comparison | [Preserved UC-21 R0/R1/R2](https://github.com/dakleyer/use-cases/blob/724d69f9cf69aaadd2f84f50934db9cf77fcc1f1/contributions/when-controls-work-system-fails/USE_CASE.md#5-select-prepare-and-run-one-experiment) | The tested configuration and, for recurrence, the demonstrated R1 correction retained in R2. |
`````

**Passage 10.** Existing reader passage: [UC-21's maintained package on main]. Source `research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md`; commit `f960f6f5a627993643512b816430a485227f9118`, blob `88b78f386047a76e0e2da905bd951ada06e5602b`. Old text occurs once.

**Text before — complete literal passage**

`````markdown
[UC-21's maintained package on main](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/README.md) connects objectives and Challenges to these routes. A case conclusion cites the particular report/version and evidence it uses. Existing registrations retain the names, units and stopping rules under which their work was recorded.
`````

**Text after — complete proposed passage**

`````markdown
[The official UC-21 case record](https://github.com/FG-TIDA/use-cases/issues/21) connects to the [research questions](#uc-21-research-questions), [Challenge sources](#uc-21-challenge-sources) and recorded work in Contributions. A case conclusion cites the particular report/version and evidence it uses. Existing registrations retain their original names, units, protocols and stopping rules.

<details>
<summary>Earlier fork-based reader passages — retained navigation history</summary>

The following passages retain the earlier links and wording for traceability. The active route is the official case record and Contributions above.

| What is UC-21 trying to establish? | [UC-21 public entry](https://github.com/FG-TIDA/use-cases/issues/21) and [current objectives and reader guide](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/README.md#research-objectives) |

| Which scenario, reduction or extension supplies the problem? | [UC-21 scenarios](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/annexes/README.md), [R01 reference scenario](./baseline/reductions/00G-R01/Escenario-creatividad-validacion.md), [technology extension protocol](./baseline/reductions/00G-R01/extensions/TECHNOLOGY_EXTENSION_PROTOCOL.md) and [kernel/proof obligations](./baseline/reductions/00G-R01/extensions/family/KERNEL_AND_PROOF.md) |

For terminology, use [Stage A §3](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md#3-challenge-first): the Challenge is the problem or failure family, and a bounded scenario, fixture or reduction instantiates it. [Stage A §6](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md#6-segments-trajectory-gates-traversals-and-traces) distinguishes profile, traversal, trace and DDS battery/campaign. [UC-21 conventions](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/annexes/CONVENTIONS.md) retain the scenario and route labels. A research campaign, an S4 business campaign and R01's operational campaign are different source contexts and accounting units. Reduction/extension transfer follows its owning proof or family-admission contract; navigation does not merge them.

The [submitted UC-21 snapshot](https://github.com/dakleyer/use-cases/tree/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails), the [maintained package on main](https://github.com/dakleyer/use-cases/tree/main/contributions/when-controls-work-system-fails), a registered study freeze and an instrument successor answer different version questions. Follow the cited snapshot for a recorded result and main for current reading. The [earlier case branch](https://github.com/dakleyer/use-cases/tree/when-controls-work-system-fails-v0.9.3/contributions/when-controls-work-system-fails) retains its preceding preparation. The [existing DDS review](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1_VNext.md) records the inventory and version decisions.

A case supplies the question and acceptance conditions. DDS supplies the study method. Read the [UC-21 Challenge guide](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/README.md#choose-a-challenge-and-its-evaluation-scenario), then select the bounded scenario, technology/configuration and evidence contract.

| Objective and scientific claim | [UC-21 claim selection](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/annexes/HYPOTHESES.md#13-claim-selection) | Case acceptance, HC, HR, HS or the selected H1–H6 contrast. |

| Challenge and admitted variant | [Family admission X1–X7](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/annexes/EXTENSIONALITY.md#4-admission-test-for-an-extension) and [DDS technology mapping](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md#4-technology-mapping) | Kernel, receiving boundary, failure predicate, inherited acceptance, positive control, resources and declared additions. |

| Implementation comparison | [UC-21 R0/R1/R2](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/USE_CASE.md#5-select-prepare-and-run-one-experiment) | The tested configuration and, for recurrence, the demonstrated R1 correction retained in R2. |

[UC-21's maintained package on main](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/README.md) connects objectives and Challenges to these routes. A case conclusion cites the particular report/version and evidence it uses. Existing registrations retain the names, units and stopping rules under which their work was recorded.

</details>
`````

### Change 91 — Link the official UC-21 entry directly to Contributions

**Expected impact: high. Risk: medium. Effort: medium. Status: prepared, not applied.**

Benefit: The public reader reaches the maintained research corpus directly, while the submitted case and complete annexes remain available as historical source records.

Risk: External case presentation; preserve all original fields, title, state, comments and frozen links. The new headings must exist before changing the Issue.

Validation and maintenance cost: Readback of the entire Issue and all four new destinations; owner access and literal approval of the replacement.

Order and decision: Ivan approves this exact Issue replacement after 92 is incorporated and checked; owner/mantainer access must be available. No external write is attempted by preparation.

**Passage 1.** The three opening snapshot links; keep the banner and all remaining fields. Source `https://github.com/FG-TIDA/use-cases/issues/21`; Issue updated_at `2026-10-13T10:36:49Z`; body SHA-256 `42a01df4e67c73a56c39544d6ce8a44dbbcb6d592f840b2ca5588ebf74122428`. Old text occurs once.

**Text before — complete literal passage**

`````markdown
**[Read the case](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/USE_CASE.md)** · **[Explore the complete package](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/README.md)** · **[Open the 20 annexes](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/annexes/README.md)**
`````

**Text after — complete proposed passage**

`````markdown
**[Current UC-21 research guide](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md#11-reader-route-from-cases-to-studies-and-results)** · **[Objectives](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md#uc-21-research-questions)** · **[Challenges](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md#uc-21-challenge-sources)** · **[Recorded studies and results](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md#15-recorded-work-and-its-owning-reports)**

UC-21 is recorded here in FG-TIDA; the current research route is maintained in Contributions. Follow the objectives and Challenge sources into DDS, registered studies, evidence and results.

<details>
<summary>Original submitted case, package and twenty annexes — preserved source snapshot</summary>

**[Read the case](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/USE_CASE.md)** · **[Explore the complete package](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/README.md)** · **[Open the 20 annexes](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/annexes/README.md)**

</details>
`````



## UC-21 twenty annexes — location and source-content reconciliation, 13 October 2026

**Correction to the previous location-only answer:** saying that the annexes were only in the fork was too broad. The twenty compiled UC-21 files are retained there, but most of their substantive sources already exist in Contributions. This audit maps that relation instead of proposing another package copy.

The actual count is **six scenario annexes, nine technology profiles and five common annexes**. `CONVENTIONS.md` and the reading index are additional reader aids, not part of the twenty. Current cuts: Contributions `d06956aa937d4e837da4dffa4e28a7647d1b3fb6` and case fork `724d69f9cf69aaadd2f84f50934db9cf77fcc1f1`.

All twenty paths remain present. All twenty current blobs are unchanged from the verified 12 October case main cut `0d32667ccce1dd3e568459a64a89e83987d92d4e`. Against the submitted `aec08fb5` cut, eighteen are byte-identical. S3 has an added obsolete-copy/source notice while retaining the prior body; S6 is now an adapter to Contributions, with its original full text still retrievable from the submitted commit. No annex disappears from either inventory by the recent navigation work.

Across all 2,249 Contributions files there is no identical Git blob for any of the twenty complete annex files. That finding alone says nothing about their substantive source coverage. The content review authenticated 2,167 current textual blobs, completed the changed/new Markdown readbacks, compared 676 non-snapshot research Markdown files, and read five source Word documents. The two public ZIPs were checked by member inventory and CRC; neither bundles the full case annex package. No scripts were run. Text comparisons identify shared source passages and concrete differences; they do not certify semantic interchangeability or a scientific pass.

### Where each annex leads

| UC-21 annex | Where its source/content is in Contributions | Relationship and remaining difference |
|---|---|---|
| HYPOTHESES | [Original causal/refutation protocol](https://github.com/dakleyer/structural-awareness-contributions/blob/d06956aa937d4e837da4dffa4e28a7647d1b3fb6/architectural-contributions/ecosystem-positioning/documents/2026-09-29/Common_Cause_Hypothesis_and_Refutation_Protocol.docx); [H1–H6 explanatory antecedent](https://github.com/dakleyer/structural-awareness-contributions/blob/d06956aa937d4e837da4dffa4e28a7647d1b3fb6/architectural-contributions/ecosystem-positioning/documents/2026-09-29/Common_Causal_Explanation_and_H1_H6.docx); [Canonical H1–H6](https://github.com/dakleyer/structural-awareness-contributions/blob/d06956aa937d4e837da4dffa4e28a7647d1b3fb6/research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) | The three source blobs explicitly named in Annex H are all present. HC/HS source material is already in Contributions. Annex H adds the case reading boundary and §13 claim-selection protocol; those additions are not an identical copy of the source Word. |
| RECURRENCE_PROTOCOL | Related R1/R2 conditions appear in the six family/profile sources and DDS, but no complete counterpart of this dedicated Annex R was located. | The HR quantified claim, admission/correction conditions, finite-versus-exhaustive refutation rules and result record remain in the preserved UC-21 edition. Similar research vocabulary is not a replacement for this protocol. |
| EXTENSIONALITY | [00K-A25 extension/admission](https://github.com/dakleyer/structural-awareness-contributions/blob/d06956aa937d4e837da4dffa4e28a7647d1b3fb6/research/ecosystem-awareness/baseline/00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md) and the six `00E…00J_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md` files in the same baseline | Extension directions, kernels, X1–X7 and family profiles have existing source counterparts. The compiled UC-21 edition uses its own inherited case gates and admission record. No single complete identical counterpart was found. |
| RELATED_CASES | The FG-TIDA source Issues/PR remain external; related research appears in FG-TIDA mappings, but no complete copy of this dated Annex N table was located. | The six-row neighbour comparison is a 29 September case-specific compilation, not a new DDS method or a discarded source. |
| EVIDENCE_AND_PROTOCOL | [Canonical KPI/requirement source](https://github.com/dakleyer/structural-awareness-contributions/blob/d06956aa937d4e837da4dffa4e28a7647d1b3fb6/research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md); [DDS study contract](https://github.com/dakleyer/structural-awareness-contributions/blob/d06956aa937d4e837da4dffa4e28a7647d1b3fb6/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md); family profiles and owning instruments | Metrics and evidence disciplines have related sources. E.6 combines HC/HR/HS, causal conditions, R0/R1/R2 and hypothesis conclusions into a UC-21 run record. That complete compilation is not established as duplicated in Contributions. |
| S1 | [00E](https://github.com/dakleyer/structural-awareness-contributions/blob/d06956aa937d4e837da4dffa4e28a7647d1b3fb6/research/ecosystem-awareness/baseline/00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) | Direct failure-family source. The annex is a case-scope edition with retained narrative, gates and case-specific terminology; differences must be preserved, not erased by assuming equality. |
| S2 | [00F](https://github.com/dakleyer/structural-awareness-contributions/blob/d06956aa937d4e837da4dffa4e28a7647d1b3fb6/research/ecosystem-awareness/baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_DRAFT.md) | Direct failure-family source. The annex is a case-scope edition with retained narrative, gates and case-specific terminology; differences must be preserved, not erased by assuming equality. |
| S3 | [00G](https://github.com/dakleyer/structural-awareness-contributions/blob/d06956aa937d4e837da4dffa4e28a7647d1b3fb6/research/ecosystem-awareness/baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md) | Current maintained 00G source. The fork adds an obsolete-copy notice; its previous body remains below that notice. |
| S4 | [00H](https://github.com/dakleyer/structural-awareness-contributions/blob/d06956aa937d4e837da4dffa4e28a7647d1b3fb6/research/ecosystem-awareness/baseline/00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.5_DRAFT.md) | Direct failure-family source. The annex is a case-scope edition with retained narrative, gates and case-specific terminology; differences must be preserved, not erased by assuming equality. |
| S5 | [00I](https://github.com/dakleyer/structural-awareness-contributions/blob/d06956aa937d4e837da4dffa4e28a7647d1b3fb6/research/ecosystem-awareness/baseline/00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_READER_EDITION.md) | Direct failure-family source. The annex is a case-scope edition with retained narrative, gates and case-specific terminology; differences must be preserved, not erased by assuming equality. |
| S6 | [00J](https://github.com/dakleyer/structural-awareness-contributions/blob/d06956aa937d4e837da4dffa4e28a7647d1b3fb6/research/ecosystem-awareness/baseline/00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md) | The fork file is a source adapter pointing here, to 00J-A01 and to case traceability; its original full case text remains at the submitted snapshot. |
| T01 | [00E_A01_MICROSOFT_AGENT_365](https://github.com/dakleyer/structural-awareness-contributions/blob/d06956aa937d4e837da4dffa4e28a7647d1b3fb6/research/ecosystem-awareness/baseline/00E_A01_MICROSOFT_AGENT_365_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) | Direct technology-profile counterpart, with substantial shared text. The UC-21 edition adds/adjusts scenario-local R0/R1/R2 alignment and references; not a byte-identical source. |
| T02 | [00E_A02_LANGGRAPH_LANGSMITH](https://github.com/dakleyer/structural-awareness-contributions/blob/d06956aa937d4e837da4dffa4e28a7647d1b3fb6/research/ecosystem-awareness/baseline/00E_A02_LANGGRAPH_LANGSMITH_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) | Direct technology-profile counterpart, with substantial shared text. The UC-21 edition adds/adjusts scenario-local R0/R1/R2 alignment and references; not a byte-identical source. |
| T03 | [00F_A01_FIWARE_NGSI_LD](https://github.com/dakleyer/structural-awareness-contributions/blob/d06956aa937d4e837da4dffa4e28a7647d1b3fb6/research/ecosystem-awareness/baseline/00F_A01_FIWARE_NGSI_LD_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) | Direct technology-profile counterpart, with substantial shared text. The UC-21 edition adds/adjusts scenario-local R0/R1/R2 alignment and references; not a byte-identical source. |
| T04 | [00F_A02_AWS_IOT_TWINMAKER_CORE](https://github.com/dakleyer/structural-awareness-contributions/blob/d06956aa937d4e837da4dffa4e28a7647d1b3fb6/research/ecosystem-awareness/baseline/00F_A02_AWS_IOT_TWINMAKER_CORE_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) | Direct technology-profile counterpart, with substantial shared text. The UC-21 edition adds/adjusts scenario-local R0/R1/R2 alignment and references; not a byte-identical source. |
| T05 | [00G_A01_OPENAI_AGENTS_STACK](https://github.com/dakleyer/structural-awareness-contributions/blob/d06956aa937d4e837da4dffa4e28a7647d1b3fb6/research/ecosystem-awareness/baseline/00G_A01_OPENAI_AGENTS_STACK_IMPLEMENTATION_PROFILE_v0.1_DRAFT.md) | Direct technology-profile counterpart, with substantial shared text. The UC-21 edition adds/adjusts scenario-local R0/R1/R2 alignment and references; not a byte-identical source. |
| T06 | [00H_A01_CLAUDE_AGENT_SDK](https://github.com/dakleyer/structural-awareness-contributions/blob/d06956aa937d4e837da4dffa4e28a7647d1b3fb6/research/ecosystem-awareness/baseline/00H_A01_CLAUDE_AGENT_SDK_IMPLEMENTATION_PROFILE_v0.4_DRAFT.md) | Direct technology-profile counterpart, with substantial shared text. The UC-21 edition adds/adjusts scenario-local R0/R1/R2 alignment and references; not a byte-identical source. |
| T07 | [00H_A02_STRIPE_RADAR](https://github.com/dakleyer/structural-awareness-contributions/blob/d06956aa937d4e837da4dffa4e28a7647d1b3fb6/research/ecosystem-awareness/baseline/00H_A02_STRIPE_RADAR_IMPLEMENTATION_PROFILE_v0.4_DRAFT.md) | Direct technology-profile counterpart, with substantial shared text. The UC-21 edition adds/adjusts scenario-local R0/R1/R2 alignment and references; not a byte-identical source. |
| T08 | [00I_A01_AWS_STEP_FUNCTIONS_RDS](https://github.com/dakleyer/structural-awareness-contributions/blob/d06956aa937d4e837da4dffa4e28a7647d1b3fb6/research/ecosystem-awareness/baseline/00I_A01_AWS_STEP_FUNCTIONS_RDS_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) | Direct technology-profile counterpart, with substantial shared text. The UC-21 edition adds/adjusts scenario-local R0/R1/R2 alignment and references; not a byte-identical source. |
| T09 | [00J_A01_PANODYSSEY_TEMS_RIGHTS_PORTABILITY](https://github.com/dakleyer/structural-awareness-contributions/blob/d06956aa937d4e837da4dffa4e28a7647d1b3fb6/research/ecosystem-awareness/baseline/00J_A01_PANODYSSEY_TEMS_RIGHTS_PORTABILITY_IMPLEMENTATION_PROFILE_v0.1_DRAFT.md) | Direct technology-profile counterpart, with substantial shared text. The UC-21 edition adds/adjusts scenario-local R0/R1/R2 alignment and references; not a byte-identical source. |

### Material findings and consolidation consequence

**Fifteen direct source counterparts already exist**: S1–S6 map to 00E–00J, and T01–T09 map to 00E-A01/A02, 00F-A01/A02, 00G-A01, 00H-A01/A02, 00I-A01 and 00J-A01. They live under `research/ecosystem-awareness/baseline/`, not in a physically migrated root `dds/` package. DDS indexes and study routes refer to those existing owners. S3 and S6 already explicitly return the reader to Contributions.

**Annex H also has its main original sources in Contributions**, under `architectural-contributions/ecosystem-positioning/documents/2026-09-29/`, with canonical H1–H6 in baseline. The named Git blobs `524fe4cc1091d622f18d37a2441464c263bfe265`, `ab187dd929f65550c966ed139e48c9412d67079d` and `4fe3d69b50fef1e82ba7f889324b70a7f6b1a81c` all match the current tree. Case-specific claim selection and source-local protocol additions still need separate reconciliation.

**The other four common annexes are not established as complete standalone duplicates in Contributions.** X and Evidence reuse existing family/admission/KPI disciplines but compile case-specific acceptance and recording rules. R is the dedicated HR recurrence protocol; N is the dated neighbour-case comparison. Their absence as identical compiled files does not mean their sources were thrown away, nor does scattered related terminology establish that every obligation has been integrated.

The correct next step is to reuse the existing fifteen source owners and hypothesis originals, then identify and preserve only the case-specific differences/compilations that are still needed. In particular, do not lose H §13, R's refutation rules, X's case admission record, Evidence E.6 or the dated N source boundary while redirecting the public reader. Do not create a second maintained copy of all twenty annexes, and do not replace a case protocol with a vaguely similar DDS section. The one Contributions entry must explain these real dependencies and source versions.

This is a location, content-lineage and preservation review by Codex, the same assistant. It amends the earlier map; it is not an independent scientific audit, source adoption, new campaign or completion of the corpus's five/sixth passes. No original case, Contributions source, Word, ZIP, test or result is edited by this note.


Publication custody: the review was rebased onto concurrent commit 49aa7b9eb00acf27de7b1bbd80b23df14a544902. Its Flores runtime-context additions do not change these two VNext or the baseline and hypothesis source counterparts examined above. The content comparison remains explicitly attached to its stated d06956a cut; no new Flores result is inferred from this annex check.
