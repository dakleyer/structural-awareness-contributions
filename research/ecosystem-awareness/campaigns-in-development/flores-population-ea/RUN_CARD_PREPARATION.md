# Flores — Run Card de preparación vigente

**Edición 2026-10-13.ORGANIZATION.1. Campaign DDS-A-FLORES-POP-EA-01.** PREPARATION_ONLY / NOT_PREREGISTERED / NOT_FROZEN / NOT_EXECUTED / NOT_ADJUDICATED.

El contrato detallado está en [el protocolo temporal](runtime-context/PROTOCOLO_2026-10-13.md); rige [R2/freeze/R3](runtime-context/PRINCIPIO_R2_FREEZE_R3_2026-10-13.md). La [versión anterior](VERSIONS_AND_DECISIONS_2026-10-13.md) conservaba el ensayo UC17-08 y se archiva íntegra; no es el Run Card vigente.

## Campos que deben fijarse

| Campo | Estado actual | Evidencia requerida |
|---|---|---|
| Q temporal, sujeto, finalidad, scope y horizonte | NOT_SELECTED | Predicado único con baseline fundada en t0; no independencia real inferida de votos |
| Fuente nativa | v1.0 pin conservado; native outputs NOT_AVAILABLE_AT_REVIEW_CUT | Derechos/acceso, versión, fixture, outputs y código efectivo sin sustitución de expectativas por datos |
| R2 defendida | NOT_DEMONSTRATED | Configuración elegida por el defensor, reparación demostrada y positivos |
| Freeze R2 | NOT_FROZEN | Código/reglas/fuentes/defensas/permisos/adaptación/recursos y horizonte completos; responsable y hashes |
| Requisitos EA generales | DRAFT_NOT_FROZEN | Fijados antes de revelar el caso puntuado; acceso/budget comparable; sin patch específico R3 |
| R3 | NOT_ADMITTED | Cambio externo único, material y no cubierto por R2 completa, con fuente legítima y adjudicación |
| Oracle y casos | NOT_ASSIGNED_NOT_FROZEN | Evaluador independiente, materialidad, verdad/expectativas, blind y separación de packet/case labels |
| Positivos y negativos | DRAFT | Scope intacto, irrelevancia, recuperación, fuente alternativa, no-observability, no global hold |
| Métricas y ledger | DRAFT | False accept/hold, reconocimiento, continuidad, recuperación, timings y costes totales |
| Ejecución y resultados | NOT_EXECUTED | Entradas/salidas/timeline y archivos por brazo preservados; adversos y parity incluidos |

## Registro operativo de una sesión admitida

~~~yaml
campaign_handle: DDS-A-FLORES-POP-EA-01
document_version: 2026-10-13.ORGANIZATION.1
status: NOT_PREREGISTERED
producer_pin: 07ac94fb100975bfff2e8ab0c644bd02ec87e537
same_temporal_claim: NOT_SELECTED
t0_grounding: NOT_FIXED
R2_defender_and_configuration: NOT_FIXED
R2_demonstration_artifacts: []
R2_complete_freeze_hash: NOT_AVAILABLE
EA_general_spec_freeze_before_R3_reveal: NOT_AVAILABLE
R3_material_change_and_noncoverage_admission: NOT_AVAILABLE
equal_observation_access_budget_horizon: NOT_FIXED
oracle_owner_and_case_commitment: NOT_ASSIGNED
candidate_packet_excludes_hidden_answers: REQUIRED
positive_unaffected_continuity_controls: NOT_FROZEN
negative_observational_equivalence: NOT_FROZEN
recovery_current_basis: NOT_FROZEN
source_outputs_unchanged: REQUIRED
chronological_inputs_outputs_effects_cost_ledger: []
adjudication: NOT_EXECUTED
~~~

Los labels K00–K19 y los 64 pares publicados son calibraciones, no un banco blind futuro. La clave/rol sealed del productor, auditor_only y respuestas futuras permanecen separados del candidato. La próxima acción es concretar fuente/Q, reparación y freeze, no fabricar un evento nativo ni reejecutar el antiguo mapping como si fuese este contrato.

[Continuación](CONTINUATION.md) · [pendientes y evidencia de cierre](TRACEABILITY_2026-10-13.md) · [historia completa](VERSIONS_AND_DECISIONS_2026-10-13.md).

<details>
<summary>Anclajes de versiones previas — navegación preservada</summary>

<a id="dds-flores--run-card-preparation-unregistered-draft"></a>

**DDS FLORES — Run Card preparation (UNREGISTERED DRAFT)** — [versión completa con este apartado](https://github.com/dakleyer/structural-awareness-contributions/blob/a44273b433113b3ba6aba6f02bed8e71fcaaa716/research/ecosystem-awareness/campaigns-in-development/flores-population-ea/RUN_CARD_PREPARATION.md#dds-flores--run-card-preparation-unregistered-draft).

<a id="1-identity-and-candidate"></a>

**1. Identity and candidate** — [versión completa con este apartado](https://github.com/dakleyer/structural-awareness-contributions/blob/a44273b433113b3ba6aba6f02bed8e71fcaaa716/research/ecosystem-awareness/campaigns-in-development/flores-population-ea/RUN_CARD_PREPARATION.md#1-identity-and-candidate).

<a id="2-need-to-freeze-input-and-comparison-contract"></a>

**2. Need-to-freeze input and comparison contract** — [versión completa con este apartado](https://github.com/dakleyer/structural-awareness-contributions/blob/a44273b433113b3ba6aba6f02bed8e71fcaaa716/research/ecosystem-awareness/campaigns-in-development/flores-population-ea/RUN_CARD_PREPARATION.md#2-need-to-freeze-input-and-comparison-contract).

<a id="3-minimal-preregistered-branch-slate-when-admitted"></a>

**3. Minimal preregistered branch slate when admitted** — [versión completa con este apartado](https://github.com/dakleyer/structural-awareness-contributions/blob/a44273b433113b3ba6aba6f02bed8e71fcaaa716/research/ecosystem-awareness/campaigns-in-development/flores-population-ea/RUN_CARD_PREPARATION.md#3-minimal-preregistered-branch-slate-when-admitted).

<a id="4-measurements--evidence-fields-to-populate-in-a-real-run"></a>

**4. Measurements / evidence fields to populate in a real run** — [versión completa con este apartado](https://github.com/dakleyer/structural-awareness-contributions/blob/a44273b433113b3ba6aba6f02bed8e71fcaaa716/research/ecosystem-awareness/campaigns-in-development/flores-population-ea/RUN_CARD_PREPARATION.md#4-measurements--evidence-fields-to-populate-in-a-real-run).

<a id="5-hard-stop-conditions"></a>

**5. Hard stop conditions** — [versión completa con este apartado](https://github.com/dakleyer/structural-awareness-contributions/blob/a44273b433113b3ba6aba6f02bed8e71fcaaa716/research/ecosystem-awareness/campaigns-in-development/flores-population-ea/RUN_CARD_PREPARATION.md#5-hard-stop-conditions).

<a id="6-additional-corrected-p0p3-proposal--not-automatically-part-of-first-scored-slate"></a>

**6. Additional corrected P0–P3 proposal — not automatically part of first scored slate** — [versión completa con este apartado](https://github.com/dakleyer/structural-awareness-contributions/blob/a44273b433113b3ba6aba6f02bed8e71fcaaa716/research/ecosystem-awareness/campaigns-in-development/flores-population-ea/RUN_CARD_PREPARATION.md#6-additional-corrected-p0p3-proposal--not-automatically-part-of-first-scored-slate).

</details>
