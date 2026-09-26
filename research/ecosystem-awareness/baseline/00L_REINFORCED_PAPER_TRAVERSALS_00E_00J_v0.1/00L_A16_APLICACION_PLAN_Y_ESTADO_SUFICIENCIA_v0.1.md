# Aplicación del plan y estado de suficiencia

26 de septiembre de 2026. Plan [A15](./00L_A15_PLAN_CAMBIOS_Y_EFECTO_EN_LA_TESIS_v0.1.md); seguimiento [A12](./00L_A12_REGISTRO_MEJORAS_ARTICULO_README_v0.1.md).

## Cambios aplicados

- Artículo `When_the_Controls_Work_but_the_System_Fails_Parts_I_II.docx`: versión 2 → **versión 3**, 22 páginas. Una frase añadida en la Parte II y una nota final de evidencia. Parte I: 183 elementos XML conservados, 18 páginas idénticas píxel a píxel. Se conservan las 229 relaciones originales del documento.
- Código y documentación: commit [5b0ac924](https://github.com/dakleyer/structural-awareness-contributions/commit/5b0ac924b8646215348e58076230c42f499e8823), 12 archivos verificados contra GitHub byte a byte. Se añaden nueve diagnósticos; los 11 controles A23 anteriores y su certificado quedan intactos.
- [Revisión semántica F02](../fixtures/00K-FORMAL/requirement-sufficiency/SEMANTIC_BRIDGE_REVIEW.md): evidencia ejecutable acotada para P3/P5/P6, sin cambiar requisitos congelados ni declarar suficiencia general. F01, el puente completo de A22, permanece abierto.

## Validación publicada

Los cuatro workflows activados por `5b0ac924` terminaron con éxito:

- [00K y campaña 379](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36224710527): el log confirma 379/379, 68 tests full-cube y 20 tests A23 en familias separadas.
- [Regresiones de corrección](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36224710546).
- [Recorridos emparejados 00L](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36224710532).
- [Integridad documental](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36224710549).

Estas validaciones reproducen las pruebas y sus límites; no convierten el resultado en suficiencia general ni en validación de productos. Stage-0 no fue modificado en este bloque.

## Nota incorporada al artículo

Evidence update following the adversarial audit

26 September 2026

The argument in Part I remains that locally valid controls may fail to preserve the justification of a combined decision after material change. The subsequent audit corrected the supporting test implementations and narrowed several claims about what their results establish. These changes do not establish product effectiveness, universal sufficiency or an EA-specific comparative advantage.

For Sections 6 and 9, the correction commit preserves the original 379 symbolic regression assertions and adds 77 separate correction checks. All pass. Handoff checks now compare received information with a pre-adapter snapshot; failed candidates, runtime errors and invalid trace values retain diagnostic records. Residual preservation is counted by field, and symbolic costs are checked against event steps and declared limits. Mixed-campaign authority, action-time validity, peer scope and input validation have also been corrected. These are bounded implementation and instrumentation results.

The 00L equality condition described in Section 6 belongs to the historical verifier. The corrected replay scores each arm against the declared expected disposition and retains disagreements. The short negative 00E stream ends after three evidence steps with capacity six; it therefore does not demonstrate resource exhaustion or an efficiency advantage. Shared-logic peers remain regression controls rather than independent architectural comparators.

For Section 7, A22 realizes 64 signatures in its simplified executable model. The counting argument remains valid for 64 distinguishable signatures; applying that result to the full A20 background theory requires the still-open semantic bridge. A23 retains finite-projection implications for P1/P2/P4 and countermodels under semantic review for P3/P5/P6. Its clause-local guard does not by itself establish the source fidelity or non-circularity of the complete bundle. Those countermodels do not automatically establish defects in the canonical requirements.

R2/V11 in Section 2 remains a proposed drift test, with execution pending. The corrected Stage-0 replay is a post-audit instrumentation revision, distinct from the historical preregistered execution. A12, A13 and 00L-A14 identify the versions, corrections, traces and remaining obligations. Independently implemented matched candidates are still needed to test the proposed EA benefit under regime change and comparable decision burden.

Semantic follow up and remaining sufficiency work

The subsequent semantic follow-up distinguishes an authorized response from continuation on the unresolved proposition, and qualified correlated evidence from false independent corroboration. A separate candidate action-time interlock was checked over 5,460 event sequences of lengths one to six: none executed on an unqualified or outdated basis, and 1,836 admitted execution. Removing the interlock exposed stale or unqualified execution in 3,212 sequences. This bounded model assumes observable material changes, one decision, fixed authority and successful qualification events; it is not a proof of full canonical conformance or production behaviour. The 11 existing A23 audit tests and nine new semantic diagnostics pass while preserving the original countermodels.

Passing a traversal establishes the expected result for its declared facts and implementation. Sufficiency asks whether the applicable requirements, faithfully interpreted, entail the relevant properties throughout the declared scope. The current traversals and bounded diagnostics support the first claim; they do not close the second.

Evidence and reproduction references

A12 cumulative article and README record

A13 adversarial audit

00L A14 corrections and verification

A23 semantic bridge review and reproducible traces

Code correction commit 3cf10a6

Las referencias activas de la nota están fijadas al commit `5b0ac924`: [A12](https://github.com/dakleyer/structural-awareness-contributions/blob/5b0ac924b8646215348e58076230c42f499e8823/research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A12_REGISTRO_MEJORAS_ARTICULO_README_v0.1.md), [A13](./00L_A13_AUDITORIA_TRANSVERSAL_PRUEBAS_v0.1.md), [00L-A14](./00L_A14_CORRECCIONES_AUDITORIA_v0.1.md), [revisión semántica](../fixtures/00K-FORMAL/requirement-sufficiency/SEMANTIC_BRIDGE_REVIEW.md) y [correcciones de código](https://github.com/dakleyer/structural-awareness-contributions/commit/3cf10a670093fd8f71b32371440266914f5d2ca3).

## Constancia de conservación

```json
{
  "source_version": 2,
  "source_sha256": "d58e471fa732f7824afcca4893cb1e92f57d7a54274b76e5f42cb43e3b898f6b",
  "output_sha256": "5b18e21a83bd0097fdf882194f47c222392d27461ee1cd236638dbfb13353d68",
  "frozen_part_I_body_elements_identical": 183,
  "existing_relationships_preserved": 229,
  "original_body_elements_changed": [
    191
  ],
  "change": "one additive sentence in Part II plus separate evidence update",
  "repository_evidence_commit": "5b0ac924b8646215348e58076230c42f499e8823",
  "frozen_part_I_render_pages_identical": [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18
  ],
  "rendered_pages": 22
}
```
