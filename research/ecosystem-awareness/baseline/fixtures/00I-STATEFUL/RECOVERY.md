# Bounded recovery and current-evidence re-entry

**Status:** locally executed evidence, included in the consolidated test package. This extends the stateful model's optional recovery policy; it does not change the historical one-check configurations or claim that real connectors have been implemented.

## Gap and falsification

The preceding implementation read once and escalated five logical seconds later. Even if a source recovered earlier, it did not read again. This was a safe non-execution outcome for persistent uncertainty, but insufficient to establish recovered continuity.

Ten new test methods run before implementation produced **11 failed assertions, including timing subtests, and zero execution errors**. This count is not 11 independent defects. Results are retained in [recovery_before.json](results/recovery_before.json), with the exact prior model and tests in [audit/before-recovery](audit/before-recovery). From this directory, the historical failure is reproducible in a separate process:

```bash
python -B -m unittest discover -s audit/before-recovery -p 'test_recovery.py' -v
```

Nonzero exit is expected for that historical command. It is excluded from the current acceptance runner.

## Declared policy

Recovery is an explicit input configuration (`recovery: true`), available under the same source access as the one-check control. The synthetic action-time horizon is fixed at 2525, five logical seconds after the first check at 2520. Guard passes occur at 2520, 2522 and 2524, with no more than three passes.

- Only an unknown-evidence HOLD is eligible for another pass.
- Each pass reloads the current manifest and all its declared material observations, checks provenance/freshness, and checks authority expiry. Returning connectivity is not permission.
- Events and renewed observations do not reset the horizon. Permits expire no later than that horizon, their source-evidence validity or the grant expiry.
- If the evidence permits the original action before the horizon, the executor may apply that exact action. It still checks the revision and intent binding.
- A clear DENY ends this queued operation. A later new authorised decision is a separate concern; this model does not automatically reopen a denied action.
- Persistent uncertainty, sampled availability oscillation or recovery exactly at the deadline leads to bounded ESCALATE and no new effect.
- The named escalation owner is recorded. Human receipt and resolution are not simulated or assumed to have occurred.

This is ordinary bounded revalidation, not an exceptional authority path, autonomous grant renewal or a complete implementation of S3.

## Paired evidence

Fifteen scenario rows extend the original 37-row matrix. Fourteen meet acceptance; the old one-check configuration remains a declared continuity failure on the recovered-source input.

| Input or intervention | Required and observed outcome |
|---|---|
| No source failure | Execute without extra guard passes |
| Source recovers before first retry / at last retry | Execute once before the horizon |
| Source never recovers / recovers exactly at deadline | Escalate, no effect |
| Freeze or Patch B arrives while waiting | Re-evaluate and deny; preserve the current configuration |
| Current manifest adds closed Finance B | Discover it on re-entry and deny |
| Freshness budget tightens while waiting | Old-enough observations remain insufficient; escalate |
| Source alternates available/unavailable at the declared event times | Stop at the fixed horizon; do not extend it on each event |
| Freeze arrives after recovered check but before actuation | Executor rejects the stale permit |
| Grant expires during the wait | Deny; no authority renewal |
| Duplicate delivery after recovery | One effect, subsequent acknowledgement only |
| Dispatch requested after the horizon | Close at the horizon; no effect; permit is also expired |
| Same recovered source, one-check control | Escalates instead of permitting legitimate continuity: scenario FAIL |

The scenario evaluator still scores expected and observed outcomes independently of the candidate. It never changes a failed control's expected result to disguise a continuity or safety failure.

## Recovery plus persistent executor

An additional integration test connects a permit issued after recovered evidence to the local SQLite executor. A separate worker process applies and commits the local effect, then terminates before acknowledging it. A new worker, even after the response horizon, acknowledges the persisted receipt without performing a second effect. Acknowledging a past committed result does not authorise a new late action.

This joins current-evidence recovery with the previously tested local receipt mechanism. The effect and receipt are in the same SQLite transaction. It supplies no atomicity guarantee for an external RDS operation or another service's state.

## Current evidence

- **49 regression tests pass:** 14 scenario tests, 13 contract tests, 12 local persistent-executor tests and 10 recovery tests.
- **52 scenario rows:** 44 meet acceptance and 8 remain explicit controls or assumption failures.
- The 33-row and 37-row checkpoints, prior failing code and audit outputs remain preserved. Counts overlap and are not independent field trials.
- `results/verification.json` records the complete test log, source hashes, process results and database snapshots. `results/traces.jsonl` records all scenario observations, decisions and effects.

Reproduce the complete current validation from the repository root:

```bash
python -B research/ecosystem-awareness/baseline/fixtures/00I-STATEFUL/verify.py --output /tmp/00i-recovery-validation
```

## Claim boundary and remaining work

The selected model now supplies evidence for normal re-entry under S10/S14 and a bounded-response aspect of S3/Q5. It remains a finite fixture with zero-duration simulated source calls, a trusted logical clock, declared authority and material dependencies, and a common revision protocol. The five-second horizon is a chosen fixture bound, not measured production latency or a generally sufficient timeout.

Additional reads are recorded in the burden ledger; no equal-cost or efficiency advantage is inferred. Three sampled checks do not establish performance across arbitrary availability schedules, and potentially blocking real calls need their own timeouts and cancellation semantics. The original shared-omission and writer-bypass failures remain exposed.

Still open: D2 dependency discovery beyond an explicit policy-source-set change; source authentication and connector behaviour; network partitions and uncertain external actuation; distributed outcome reconciliation; human escalation closure; independently reviewed testbed integration. These require separate tests and cannot be inferred from local recovery success.
