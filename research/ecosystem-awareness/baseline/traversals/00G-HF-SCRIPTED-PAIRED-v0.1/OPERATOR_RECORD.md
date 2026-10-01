# Operator record

Design published before execution: `08a76f7454cd6f3f5a446efa7c1722d9ee337289`.
Registration UTC: `2026-10-01T16:49:17.514318+00:00`. Registration timestamp is operator-supplied; the GitHub design publication provides the independently visible prior source revision, not external authorship.
Design freeze SHA-256: `36a9df288abbbe8835c27bc89317eb6b643247ba7a8210a883bc2f61c3afb585`.
One deterministic traversal per arm/case; no model, API, human review or run retry. No code or expectation changes after the run.

Commands from repository root (the execution workspace used the equivalent `ea_temporal_work/` prefix):

```sh
python research/ecosystem-awareness/baseline/traversals/00G-HF-SCRIPTED-PAIRED-v0.1/run.py --output-dir research/ecosystem-awareness/baseline/traversals/00G-HF-SCRIPTED-PAIRED-v0.1/runs/2026-10-01-first
python research/ecosystem-awareness/baseline/traversals/00G-HF-SCRIPTED-PAIRED-v0.1/verify_run.py research/ecosystem-awareness/baseline/traversals/00G-HF-SCRIPTED-PAIRED-v0.1/runs/2026-10-01-first
```

Both commands returned exit code 0. Runner summary: native 8/8 tasks, native+EA 7/8. Checker: 16/16 paths verified and 16/16 registered expectations met, including one anticipated task failure. Zero source/model credentials or private user data are used; all worlds are the declared synthetic fixtures.

Clock, CPU and wall values must remain distinct. CPU/wall values are observed local process durations and are not constrained to be equal. Synthetic EA processing and transport are one tick each, per signal, as fixed in the protocol. No production calibration is claimed.
