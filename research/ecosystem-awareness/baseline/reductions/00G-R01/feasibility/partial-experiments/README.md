<a id="experimentos-parciales-y-diagnósticos-de-viabilidad"></a>

# Partial experiments and feasibility diagnostics

[Feasibility study](../README.md) · [Current mathematical proof](../PURE_MATHEMATICAL_TRILEMMA.md).

This section retains the checks already performed. They are partial tests and exploratory experiments, not R01's independent oracle/harness, a universal proof or a registered campaign. This reorganization does not rerun scripts or add scientific results. Scripts, fixtures, outputs and JSON manifests are relocated without modifying their bytes. Recorded dates, counts and paths continue to describe their historical deliverables.

| Group | Code and inputs | Preserved outputs | Scope |
|---|---|---|---|
| M01 | [Checker](./historical/verify_m01_scope.py) | [Scope checks](./historical/M01_SCOPE_CHECKS.json) | Initial-contract diagnostic; no bound in L. |
| M02 | [Checker](./historical/verify_m02_worlds.py) · [Fixture](./historical/M02_CONJUNCTION_FIXTURE.json) | [Worlds and routes](./historical/M02_WORLD_CHECKS.json) · [Release](./historical/M02_RELEASE_CHECKS.json) | Finite pair and controls, with original scope. |
| M10/P03 | [Checker](./historical/verify_m10_measurements.py) · [Contract](./historical/M10_RECONCILED_CONTRACT.json) | [Measures](./historical/M10_MEASUREMENT_CHECKS.json) · [Release](./historical/M10_RELEASE_CHECKS.json) | Measurement audit and fixture countercontrols. |
| F/W | [Checker](./historical/verify_trilemma.py) · [Contract](./historical/TRILEMMA_CONTRACT.json) | [Checks](./historical/TRILEMMA_CHECKS.json) · [Release](./historical/TRILEMMA_RELEASE_CHECKS.json) | Self-performed enumeration of small sizes; neither independent review nor proof for all sizes. |
| Received material | [Complete dossier](./received/2026-10-04/README.md) | [Admission](./received/2026-10-04/INTAKE_CHECKS.json) · [Outputs](./received/2026-10-04/runs/executions.json) | Six originals and additional diagnostics; technologies in subsequent queue. |

The four historical checkers and their fixtures remain together in `historical/` to preserve local dependencies. Original hashes are those of the input commit identified in [the manifest](../RELOCATION_MANIFEST.json). Internal literal paths are not updated retrospectively. Commands of previous deliverables describe their original context; for future reproduction identify the commit and execute from the directory containing the script and fixtures. That reproduction does not close C05/M16.

<a id="seguimiento-al-final"></a>

## Tracking at the end

| Work | Status | Next obligation |
|---|---|---|
| Previous diagnostics | Preserved and separated | Use as error clues, with their scope. |
| New scientific examples | Not executed in this deliverable | Freeze contract and harness first. |
| Neutral oracle/harness | Pending C01–C05 | Ground truth, optimum, ledger and measures; independent method and declared coverage. |
| Universal proof | In a separate mathematical document | Audit lemmas and policies; do not infer it from these results. |
