<!-- English language edition of 00L_A03_PLANTILLA_TRAZA_PAPEL_v0.1.md; source commit 51fc686f45b6ef10c53b69f4c26d0e381b007ff8, blob 145a04f1d9501c6020ff0efaaf7a99a73c3e806c. Translation only: original, evidence status and scientific claims unchanged. -->

# 00L-A03 — Paper-trace template

## Mandatory separation

| Type | Meaning | May be presented as an observed result |
|---|---|---|
| Published capability | What a primary source from the vendor or standard documents | No |
| Reinforced implementation | Additional design constructed for the comparison | No |
| Synthetic fact | Input fixed by the scenario | No |
| Paper calculation | Output derived from declared facts and rules | No |

## Minimum record per step

| Field | Required content |
|---|---|
| Identity | scenario, branch/control, comparison arm, step and case-sheet version |
| Input | fact, provenance, time/version and observability for the arm |
| Rule | documented control or proposed rule; S/T/H/KPI and threshold |
| Calculation | previous state → declared logical operation → subsequent state; numerator/denominator if applicable |
| Decision | permitted action, responsible party, deadline, residual and gate disposition |
| Check | bounded oracle, counterexample and condition that would refute the conclusion |

## Permitted dispositions

`EXECUTE`, `REQUALIFY`, `CONTAIN`, `NO_COMMITMENT`, `ESCALATE`, `PRESERVE_AND_ROUTE`, `DENY`, `EXPIRE` and `NO CONCLUSION`.

An isolated KPI must not be turned into a PASS: the complete `T#` condition and the source's stated limit must be satisfied.
