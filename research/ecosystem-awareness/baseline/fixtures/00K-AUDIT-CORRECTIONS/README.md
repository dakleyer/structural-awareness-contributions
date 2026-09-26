# Audit correction regressions — 26 September 2026

Companion to [A14](../../00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A14_CORRECCIONES_AUDITORIA_v0.1.md), following the [A13 audit](../../00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A13_AUDITORIA_TRANSVERSAL_PRUEBAS_v0.1.md).

The [77 regression checks](./test_audit_corrections.py) exercise corrected boundaries and inject handoff loss, wrong decisions, runtime exceptions, mismatches and non-deterministic repeats. They include positive controls. They are separate from the original **379** assertion campaign; no existing campaign test was edited.

- [Before](./before_results.json): the same test file against `28b7666d8db26634a0f92458146b86f6b25c304f` yields 65 failures / 12 passes. Some failures concern newly required APIs and trace contracts, not distinct semantic bugs.
- [After, with commands and source hashes](./results.json): 77/77 new checks and 379/379 existing regressions pass locally; byte comparisons target the newly versioned 00L and Stage-0 outputs.
- [Execution logs](./execution_logs.txt): output from each command, including integrity gates and P5 blind-signature tests now included in CI.
- [Reproducer](./reproduce.py): writes logs, a JUnit report, generated traces and source hashes to an explicitly selected output directory.

From the repository root:

```bash
python -m pytest -q research/ecosystem-awareness/baseline/fixtures/00K-AUDIT-CORRECTIONS
python research/ecosystem-awareness/baseline/fixtures/00K-AUDIT-CORRECTIONS/reproduce.py --output /tmp/audit-corrections-replay
```

This is implementation/harness correction evidence. It does not establish independent comparator implementations, product performance, the full A22 background-theory bridge or complete A23 semantic fidelity. Historical A13 probes and traces are immutable snapshot evidence; replay those on the audited commit, not as acceptance tests for this corrected implementation.
