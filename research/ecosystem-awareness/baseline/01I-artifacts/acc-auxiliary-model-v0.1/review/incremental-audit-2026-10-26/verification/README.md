# Scripts de verificación de la auditoría

Esta carpeta reúne en el PR los scripts con los que Claude, asistente de IA, obtuvo las cifras de las rondas 13 a 21. Hasta la ronda 21 vivían solo en el espacio de trabajo del auditor, así que no podían reproducirse desde el PR. Todos son de solo lectura: importan el código auditado desde la ruta que se les pasa, no escriben nada y no modifican ningún documento ni estudio.

El script de reconfirmación de I-01 ya estaba en el PR: [`../reconfirm_I01_2026-10-28.py`](../reconfirm_I01_2026-10-28.py).

## Qué comprueba cada script

| Script | Hallazgo | Ronda | Ejecutar contra | Resultado esperado |
|---|---|---|---|---|
| [`m28_01_float_boundary.py`](m28_01_float_boundary.py) | [M28-01](../../INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md#m28-01) | [13](../../INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md#ronda-13) | `studies/scoped-closure-metacognition-v0.1` de `main` | Caso 1 `EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT`; caso 2 `UNDETERMINED_FROM_AVAILABLE_EVIDENCE` |
| [`joint_status_vs_bellman_ford.py`](joint_status_vs_bellman_ford.py) | [I-01](../../INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md#i-01), [M27-01](../../INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md#m27-01) | [13](../../INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md#ronda-13) | Ídem, en `main` y en PR #64 | 0 discrepancias; 1 990 envolventes alcanzables |
| [`m28_02_guard_sweep.py`](m28_02_guard_sweep.py) | [M28-02](../../INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md#m28-02) | [15](../../INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md#ronda-15) | `studies/mathematical-lineage-social-agentic-v0.1` de la rama de PR #60 | 162 combinaciones, 0 violaciones |
| [`k01_k02_witness.py`](k01_k02_witness.py) | [K-01](../../INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md#k-01), [K-02](../../INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md#k-02) | [17](../../INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md#ronda-17) | `studies/intrinsic-abcd-economics-v0.1` de `main` | K-02: A = 128, dos B válidos prometen 2, ganancia conjunta 1. K-01: empate de costes (3,00) con 128 hojas |
| [`k02_b_composability_fuzz.py`](k02_b_composability_fuzz.py) | [K-02](../../INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md#k-02) | [19](../../INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md#ronda-19) | Ídem | 3 000 casos de una pregunta con 0 promesas excesivas; en 214 de 2 299 pares, la suma de dos B válidos promete más que la ganancia conjunta |
| [`check_model_md_round21.py`](check_model_md_round21.py) | Entrega 02 del kit (P-M02, P-M06, P-M07, P-M11) | [21](../../INCREMENTAL_SCIENTIFIC_AUDIT_2026-10-26.md#ronda-21) | Raíz de un checkout de `main` | RAV-01 13 / 9 / 13,25; 0,9²⁰ = 0,1216; 81 y 35 enlaces; anclas sin cambios; 52 + 70 pruebas en verde. Termina con 1 si algo falla |
| [`anchor_check.py`](anchor_check.py) | Herramienta | 14, 20, 21 | Cualquier `.md` | Enlaces `archivo.md#ancla` que no encuentran título ni `<a id>`. Termina con 1 si hay alguno roto |

## Cómo ejecutarlos

Desde la raíz del repositorio, con un checkout de `main` en `MAIN` y uno de la rama de PR #60 en `PR60`:

```bash
V=research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/review/incremental-audit-2026-10-26/verification
S=research/ecosystem-awareness/baseline/01I-artifacts/acc-auxiliary-model-v0.1/studies

python3 -B $V/m28_01_float_boundary.py        $MAIN/$S/scoped-closure-metacognition-v0.1
python3 -B $V/joint_status_vs_bellman_ford.py $MAIN/$S/scoped-closure-metacognition-v0.1
python3 -B $V/m28_02_guard_sweep.py           $PR60/$S/mathematical-lineage-social-agentic-v0.1
python3 -B $V/k01_k02_witness.py              $MAIN/$S/intrinsic-abcd-economics-v0.1
python3 -B $V/k02_b_composability_fuzz.py     $MAIN/$S/intrinsic-abcd-economics-v0.1
python3 -B $V/check_model_md_round21.py       $MAIN
python3 -B $V/anchor_check.py                 $V/../GUIA_DE_LECTURA.md $V/../premium/*.md
```

## Última ejecución

Ejecución del 28-10-2026 contra `main` `51fc686`, la rama de PR #60 en `8cd78d58` y la de PR #64 en `059e0af1`. Todas las cifras coinciden con las publicadas en las rondas:

```text
m28_01_float_boundary.py        case1 EVIDENCE_OR_ASSUMPTIONS_INCONSISTENT | case2 UNDETERMINED_FROM_AVAILABLE_EVIDENCE
joint_status_vs_bellman_ford.py joint-status mismatches: 0 | envelope-tightness cases checked: 1990   (main y PR #64)
m28_02_guard_sweep.py           combinations: 162 violations: 0                                       (PR #60, 8cd78d58)
k01_k02_witness.py              current A: 128 | B3: 1 True | B8: 1 True | sum promised: 2 | actual joint gain: 1
                                n=128 L=9 C_B=3.00 C_target=3.00 -> B<target? False
k02_b_composability_fuzz.py     single-question cases: 3000, B over-promises: 0
                                two-question cases: 2299, sum of two valid B over-promises joint gain: 214
check_model_md_round21.py       RESULT: PASS (9 comprobaciones)
anchor_check.py                 0 anclas rotas en la auditoría, la guía, el anexo y el kit premium
```

M28-02 se verificó en la ronda 15 sobre `cb72bb65`. La rama de PR #60 avanzó después hasta `8cd78d58`, y el barrido sigue dando 0 violaciones.

Son comprobaciones sintéticas y finitas del código: no aportan evidencia empírica ni sustituyen la revisión humana.
