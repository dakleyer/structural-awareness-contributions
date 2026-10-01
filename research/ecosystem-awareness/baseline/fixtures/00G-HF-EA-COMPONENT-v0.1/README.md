# 00G-HF — first bounded EA component candidate v0.1

**Executed author software checks: 22/22 contract cases and 8/8 supplemental checks in the reviewed run. Zero model requests, zero agent episodes, zero C3 oracle evaluations.** These are finite properties of a structured-input qualifier. This is not complete EA, temporal-change detection, empirical prevention, a comparison with OpenAI or independent validation.

[Contract and partial requirement mapping](./CONTRACT.md) · [Reviewed report](./runs/2026-10-01-reviewed/REPORT.json) · [Actual signal outputs](./runs/2026-10-01-reviewed/OUTPUTS.json) · [Integration limits](./INTEGRATION_NOTES.md) · [Parallel plan](../../implementation/00G-HF-PARALLEL-v0.1/README.md) · [Reduced scenario](../../00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.1_DRAFT.md).

## What was implemented

`component.assess(view)` qualifies the current decision basis under a fixed, declared service/lineage profile. It keeps mandate, resource access, applicability and evidence separate; binds them to the recipient, task and time; retains unknown/conflict and residual limits; distinguishes instructions from evidence; counts qualified root labels rather than repeated messages; and reports logical response margin. It does not call services, grant permission, block a tool or select an agent's next action.

The candidate receives only the observation view. The runner retains expected properties and hidden facts outside that call. This is separation in author-written software, not sandbox-based protection against a malicious candidate. The structured fields and service attribution are trusted input assumptions. The component does not parse arbitrary peer prose or verify cryptographic authenticity.

## Results and actual limits

| Family | Observation from these tests | What it does not establish |
|---|---|---|
| Legitimate P01–P03 | The component qualifies valid in-scope operation, including a fresh basis version; unrelated negative evidence does not veto it. | No native task completion was executed. |
| Negative N01–N05 | Separate missing permissions, false applicability, conflicting authority and negative evidence prevent an unqualified sufficient output. | No operational enforcement or empirical agent response. |
| Unknown U01–U10 | Missing, stale, future, wrongly scoped/sourced and dependent evidence preserve a gap. | No guarantee that telemetry exists or that all change is detected. |
| Timing T01–T02 | A correct/current signal can still be too late for the declared response. | No production or historical propagation latency measurement. |
| Identical-view L01/L02 | Exact same output for two different hidden authority states. | Hidden revocation is **not detected**; apparent support is conditional on the view. |
| Stipulated consumers | A following policy can avoid the proposed unauthorized attempt; an ignoring policy proceeds; a conventional guard can already suffice. | These are three toy conditional checks, not model decisions or a differential benefit for EA. |

The 8 supplemental checks are one identical-view relation, four schema rejection checks and three explicitly stipulated consumer policies. They are not eight additional agent trials. The 22 case checks include the two views used in that relation; do not count the relation as independent evidence.

The initial run passed 22/22 + 7/7. Code review then identified malformed check-name handling that could raise `TypeError` rather than the contract's `ValueError`. It was corrected and an explicit rejection check was added before the reviewed run. Both runs are retained. The first run's exact source is preserved under [its source directory](./runs/2026-10-01-first/source/component.py); no result was overwritten. This review did not change the frozen 22 fixtures or contract.

## Reproduce

From repository root, Python 3.10+ standard library:

```sh
python research/ecosystem-awareness/baseline/fixtures/00G-HF-EA-COMPONENT-v0.1/verify.py --output-dir /tmp/00g-hf-ea-component-review
```

Use a new output directory for each execution. The runner checks the fixture commitment, writes code hashes before assessment, evaluates every case, records every signal and returns nonzero if a check fails. Registration timestamps and Python versions may differ; semantic outputs should be identical. `FIXTURE_FREEZE.json` pins contract/expectations; `DESIGN_FREEZE.json` pins this published candidate and evidence. Both commitments are by the author, not external preregistration. To reproduce the first run, copy this package to a temporary directory and replace `component.py`/`verify.py` there with that run's preserved source; never change the published candidate in place.

## Next work

1. Temporal contrast: add qualified prior state and test unchanged, visibly changed, hidden-changed and renewed contexts. The current stateless qualifier does not claim a change event from a bad snapshot.
2. Implement the explicit native-service mapping in the integration notes without fabricating freshness, source authority or independence. Codex can run its native lane now; it need not wait for this mapping.
3. Register and execute the same receiver without/with EA under comparable conditions. Success of these component checks cannot replace that comparison.
4. Only then attribute added value of incident lifecycle, human escalation or population input through the registered component contrasts. Unknown and signal-ignored results remain valid outcomes.
