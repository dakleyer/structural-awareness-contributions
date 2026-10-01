# 00G-HF — temporal EA component and native-service projection v0.2

**Reviewed author software execution: 20/20 temporal cases and 17/17 supplemental checks.** Six of the supplemental checks replay scripted native service acquisition; they are not six additional model episodes. **Zero model requests, zero agent decisions, zero C3 evaluations.** This package does not demonstrate EA superiority or close E1/E3.

[Contract](./CONTRACT.md) · [Reviewed report](./runs/2026-10-01-reviewed/REPORT.json) · [Actual temporal outputs](./runs/2026-10-01-reviewed/OUTPUTS.json) · [Native public inputs, service exchanges and host traces](./runs/2026-10-01-reviewed/NATIVE_SERVICE_TRACES.json) · [Integration handoff](./INTEGRATION.md) · [Parallel plan](../../implementation/00G-HF-PARALLEL-v0.1/README.md).

## What now runs

`temporal.compare(previous, current)` compares qualified endpoints while retaining the existing v0.1 qualifier. `native_adapter.adapt_native(...)` projects only public native service responses into the declared profile; it never receives a hidden world or oracle verdict. The runner owns the worlds and records, and passes only the projected observations to the candidate. This is software separation under an author-controlled host, not an adversarial sandbox.

| Test family | Observed result | Boundary |
|---|---|---|
| Unchanged qualified context | No observed change; current support retained. | No claim of global stability. |
| Visible loss of authority/applicability or independent roots | Qualification changes remain distinguishable. | A change in qualification is not automatically proof of world change. |
| Expiry / missing observations | Qualification becomes UNKNOWN. | No invented revocation event. |
| Legitimate qualified recovery | Current basis becomes sufficient within the supplied view. | No authority is created and no task completion is asserted. |
| Version / host basis-label refresh | Metadata change is reported separately. | No automatic material semantic-change claim. |
| Scope or time mismatch | NOT_COMPARABLE. | No cross-task change attribution. |
| Late signal | Change is reported with a nonpositive response margin. | Detection alone is not prevention. |
| Hidden revocation / transient between samples | Identical endpoints produce identical results. | These changes are not detected. |
| Native service projection | Positive and negative point responses are preserved, with null version/forward validity. | Interval sufficiency remains UNKNOWN in all six sequences; this does not establish inadequacy of native controls. |

The native six-cell script samples at ticks 26–28, waits until 50 and samples again at 51–53. It observes a false-to-true point response in A-P/Q-P; it does not recover a missing pre-revocation observation for A-N/Q-N, whose changes happened before the native receiver resumed. No native commit, inspection, effect or completion is executed by this script. Acquisition uses six service calls plus one wait: six service ticks and 22 wait ticks. Transport/response values are declared assumptions, not measured model behavior or charged runtime integration. No budget-equivalent comparison was run.

## Review history and reproducibility

The [first run](./runs/2026-10-01-first/REPORT.json) passed 20/20 + 16/17. `reject_wrong_native_scope` failed: a malformed earlier authority response could be superseded before validation. The adapter now checks every successful authority/applicability response before retaining the latest observation. The fixtures and expectations were not changed. The first run's exact source is preserved in [source](./runs/2026-10-01-first/source/native_adapter.py); all its results remain available. The reviewed run passed 20/20 + 17/17.

From repository root, Python 3.10+ standard library:

```sh
python research/ecosystem-awareness/baseline/fixtures/00G-HF-EA-COMPONENT-v0.2/verify.py --output-dir /tmp/00g-hf-ea-temporal-new-run
```

Use a new output directory. The runner checks the fixture commitment and dependency hashes, records code hashes before execution and stores all results. To reproduce the initial failure, copy the fixture hierarchy to a temporary location and replace v0.2's code with its preserved first-run source there. Do not change the published package. Output hashes should match for semantic artifacts; registration timestamps and interpreter metadata vary. The final DESIGN_FREEZE.json is a publication integrity manifest, not evidence of independent or prospective preregistration. Fixtures were committed locally before execution by the same author who implemented the component.

The preserved v0.1 package had been prepared locally but was absent from `main` at `c8672ae751c458bcafbf2aff78b5bdc5f6071614`. It is first published together with this successor, retaining its 22/22 + 8/8 reviewed evidence and the earlier 22/22 + 7/7 run. Earlier local timestamps do not establish earlier public availability. Its current code and outputs were reproduced unchanged during this continuation.

## Remaining work

1. Prepare the separately registered composition contract for basic signalling, lifecycle, human escalation and population input, including absent/late responses and comparable resources.
2. Resolve runtime point-observation consumption without inventing leases or weakening native guards; any local freshness policy must be explicit and shared by both arms. UNKNOWN cannot be used as a blanket refusal policy and then credited as prevention.
3. Freeze a prospective native/EA lot and deliver/journal the signal to the actual receiver. The native lane can execute independently now; this pure projection does not install EA in it.
4. Execute reserved variants only after real custody/access controls exist. These public development fixtures are not blind cases. H5/H6 window/capacity comparisons, causal attribution and model efficacy remain pending.
