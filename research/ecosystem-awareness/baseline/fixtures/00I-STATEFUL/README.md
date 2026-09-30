# 00I / S5 — bounded stateful evidence

**Status:** locally executed synthetic simulation, with a companion local SQLite/process-recovery witness; not a testbed adapter or AWS execution. Engineering extension dated 2026-09-30, based on repository commit `a3aa353f59b0917da4d861381a0cb3ebd89b4bfd`. No external preregistration or independent implementation review is claimed. The [additional audit](AUDIT_EXTENSION.md) records discovered defects and fixes; the [bounded recovery extension](RECOVERY.md) adds current-evidence re-entry and its limits. This package is an additions-only insertion under the fixtures directory; it does not modify existing documents, code or workflows.

This extends the [00I positive design](../../00I_SUCCESS_MODEL_CASE_ACTION_TIME_REQUALIFICATION_v0.1.md) with a queue, observations, guard, permit, executor and observable state changes. It closes the previous gap between a returned decision label and a **simulated action effect**. The positive design's full predicate is not thereby certified for real systems.

The intended review entry point is [FG-TIDA UC21](https://github.com/FG-TIDA/use-cases/issues/21). Scenario S5 and technology T08 were read at the annex repository revision `aec08fb5b0fac2ee399372370e9ee2a82a2d5779`. The existing [AWS skeletons](../00I-AWS/README.md) remain design artifacts. No product-specific capability is inferred from these results.

## What runs

At logical second 120 (14:02), Patch A is legitimately qualified against generation 217 and queued to restore **216**, not 217. At second 2520 (14:42), the guard reads the selected manifest and source observations. It issues a short-lived permit only if the declared conditions permit the exact intent. The queued executor attempts the operation at 2522. It can either change the simulated configuration and record a reboot effect, or reject the operation and leave the configuration unchanged.

The guarded configuration is an ordinary implementation of the requirement, not an EA-exclusive control. It dynamically loads the policy manifest and therefore receives credit for passing the D1 source-set change. There is no separately strengthened EA arm or claim that EA outperforms this conventional implementation.

Every run starts from independent state. The runtime receives events and configuration options, but no expected outcomes. `reproduce.py` runs candidates **before loading** `oracle.json`, then evaluates disposition, action application and final configuration separately. This is separation of runtime and evaluator inputs, not proof of independent authorship of the oracle.

## Evidence and results

The current local run has **52 scenario rows: 44 satisfy scenario acceptance and 8 fail it as deliberately specified**. Separately, **49 regression tests pass**, including local subprocess/SQLite recovery checks. These are different counts with overlapping coverage, not independent operational trials. The regression suite checks that both the successful defences and declared failures remain observable. A green regression run does not mean all candidates or scenarios are safe. The initial 33-row results are preserved in `results/first_33_results.json` and `results/first_33_traces.jsonl`; the subsequent 37-row checkpoint is preserved in `results/v2_37_results.json`, `results/v2_37_traces.jsonl` and `results/v2_verification.json`.

| Case / contrast | Observed simulated result | Meaning |
|---|---|---|
| Valid unchanged conditions | Patch A applied once; final generation 216 | Continuity succeeds; deny-all cannot pass |
| Freeze active before use | DENY; generation remains 217 | Values are reassessed, not merely field names compared |
| Patch B supersedes A; canonical S5 with freeze | DENY; generation remains 218 | Queued Patch A does not undo the forward fix |
| Diagnosis changes while incident remains open | DENY; no queued repair effect | Incident status alone is insufficient |
| Freeze / Patch B / manifest change after check | Permit initially issued; executor rejects; no Patch A effect | Conditional binding matters independently of the guard |
| Stale, missing, unavailable, future-dated, wrongly typed or wrong-owner evidence | Bounded HOLD, then ESCALATE at five logical seconds; no effect | Unknown evidence does not become permission in this model |
| Evidence expires between check and use | Executor rejects the expired permit | Evidence freshness also limits the permit lifetime |
| Duplicate delivery / substituted intent | No second application / substituted operation rejected | Permit and idempotency bind the simulated intent |
| D1: current manifest adds closed Finance calendar B | Dynamic conventional guard denies; static-manifest control applies incorrectly | Source-set loading is credited where implemented |
| D1: new calendar is open; irrelevant metric changes | Execution remains permitted | Change does not mean unconditional blocking |
| D4: owner tightens source age from 60 to 5 seconds | Six-second evidence causes bounded escalation; fresh evidence permits execution | Updating the policy matters even when the source value remains unchanged |
| D1 followed by D4, and the reverse order | Closed Finance calendar remains applicable | Updating freshness must preserve existing dependencies |
| Source recovers before a fixed five-second horizon | Re-read all currently declared evidence, then execute only if still permitted | Recovery of connectivity alone does not restore applicability |
| Freeze, supersession, new dependency or expiry during recovery | No stale queued effect | Every recovery pass applies current constraints |
| Missing/flapping evidence or expired response horizon | At most three guard passes, then bounded escalation | Re-entry does not reset the deadline or renew authority |

The eight **scenario failures**, explicitly retained in `oracle.json`, are:

1. `cached_temporal_control`: complete coverage with queue-time values still applies after a freeze.
2. `unbound_race`: current guard passes, but an intervening freeze is ignored by an executor without revision binding.
3. `static_manifest_drift`: checking the old source set misses the new closed Finance calendar.
4. `deny_all_continuity`: blocks a legitimately permitted action.
5. `shared_omission`: the reference and guard both omit a real freeze dependency; the guarded configuration wrongly executes.
6. `writer_bypass`: a material writer changes the world without advancing the revision; the guarded configuration wrongly executes.
7. `d4_static_freshness_control`: the old freshness budget admits evidence no longer valid under the current policy.
8. `recovery_no_recheck_control`: the original one-check policy escalates despite evidence recovering in time for a legitimate action.

Shared omission and writer bypass are limits of the guarded model's assumptions, not merely weak alternative implementations. Their expected **safety** result remains non-execution; the evaluator reports actual scenario failure. They are not relabelled as safe outcomes to obtain a green report.

## Gate and requirement mapping

| Obligation | Evidence here | Still unproved |
|---|---|---|
| Q0 — technical grant | Fixed intent and expiry checked at guard and execution | Actual issuer/subject/scope verification, revocation and grant acquisition |
| Q1 — explicit decision basis | Queue record, source manifest, owner labels and missing-coverage control | Completeness of the material set; legitimate governance decisions creating it |
| Q2 — reassessment at use | Temporal paired cases and new source reads | Fresh observations from real connectors |
| Q3 — source and freshness | Owner/type/availability/time checks; observation validity bounds permit expiry | Authentication, trustworthy clocks, source authority and truthful timestamps |
| Q4 — supersession | Patch B and changed diagnosis invalidate the old repair | Real intervention lineage and distributed conflict resolution |
| Q5 — bounded, scoped response | One target, fixed five-second horizon, up to three current-evidence guard passes, continuity control | Human receipt/action, operational latency/budget, cross-system recovery and general re-entry behaviour |
| Q6 — check-to-effect binding | Registered permit, intent binding, revision comparison and state mutation | Atomicity across distributed services; actual prevention at an RDS API |

The [canonical requirements](../../00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) remain unchanged. This supplies bounded evidence towards S10 (material change between commitment and execution) and S14 (evidence assessment), and selected aspects of S1 (expiry) and S3 (bounded escalation). It does **not** establish full conformance with S1, S3, S10, S14, T1–T4 or all Q0–Q6. Source acquisition and action enforcement are external responsibilities in the EA architecture; the all-in-one simulator is a test arrangement, not a requirement to deploy a monolithic EA controller.

## Reproduce and inspect

Python 3.10+ and the standard library are sufficient. From the repository root:

```bash
python -B -m unittest discover -s research/ecosystem-awareness/baseline/fixtures/00I-STATEFUL -p 'test_stateful.py' -v
python -B research/ecosystem-awareness/baseline/fixtures/00I-STATEFUL/reproduce.py --output /tmp/00i-stateful-replay
```

For the complete current validation, including contracts and process recovery:

```bash
python -B research/ecosystem-awareness/baseline/fixtures/00I-STATEFUL/verify.py --output /tmp/00i-full-validation
```

- [fixtures.json](fixtures.json): runtime scenario inputs, including explicit control configurations.
- [oracle.json](oracle.json): separately loaded acceptance criteria and expected failure identities.
- [model.py](model.py): source adapter, guard, permit, queue driver and executor.
- [test_stateful.py](test_stateful.py): 14 scenario regression tests, including subcases, interleavings, falsifiers and evaluator checks.
- [test_contract_edges.py](test_contract_edges.py): 13 strict input/identity/evaluation contract tests.
- [test_durable.py](test_durable.py): 12 local SQLite/process-recovery tests, including recovered evidence followed by a lost acknowledgement.
- [test_recovery.py](test_recovery.py): 10 bounded re-entry tests, some with multiple timing subcases.
- [results/results.json](results/results.json): expected/observed outcomes, distinct acceptance and regression results, Python version and SHA-256 hashes.
- [results/traces.jsonl](results/traces.jsonl): all 52 traces, including rejected attempts, continuity failures and unsafe effects.
- [results/verification.json](results/verification.json): all 49 test results, source hashes, subprocess exits and database snapshots.
- [build_fixtures.py](build_fixtures.py): fixture authoring only; not needed for replay and never imported by the runtime.

Exit code 0 means the declared regression matrix was reproduced: 44 successful scenario rows plus the same eight visible failures, with no execution errors. Do not report this as “52/52 successful walkthroughs”. Raw runtime traces are saved before oracle evaluation. No workflow is installed by this package; the commands above reproduce the supplied local results, which are not CI results.

## Assumptions and audit limits

1. **Declared world.** The manifest's material set and owner assignments are supplied. No mechanism invents a missing ownership decision or discovers an unobservable dependency. The shared-omission case exposes this directly.
2. **Common revision protocol.** All material changes must advance the revision. The single-threaded compare/apply step is atomic only inside this process. Writer bypass breaks the guarantee. A DynamoDB update plus an RDS call is not automatically equivalent.
3. **Observation trust.** Source values, metadata and authority are simulated. Incorrect metadata is rejected where detectable; a source that convincingly lies about its value, authority or timestamp is outside this model.
4. **Bounded simulation.** The base model remains single-process. The companion SQLite witness now tests real subprocess exits, retries and competing deliveries for a local row and receipt in one database transaction. Neither layer models a network partition, partial RDS effect, cancellation of an already accepted external request, rollback compensation or service outage. Permit registration is not cryptographic authentication; host/power failure is not tested.
5. **Scoped completeness.** D1, a bounded D4 freshness-policy change and selected causal/time changes are exercised. D2, D5 and the full S5 variant catalogue are not claimed. Temporal interleavings are sampled deterministically, not exhaustively model-checked.
6. **Cost and fairness.** Inputs and source access are shared; additional reads are counted per arm. Logical elapsed time and read counts are not measured latency, compute, monetary cost or evidence of equal resource efficiency. Weak arms isolate mechanisms; they are not product benchmarks.
7. **Historical integrity.** Existing symbolic runs and their totals are unchanged. This is a new evidence layer, not a retroactive upgrade of those historical claims. Fixtures and oracle were authored during this implementation, not independently or prospectively preregistered.

## Concrete transfer to a testbed

| Existing simulation boundary | What the testbed must provide | Evidence needed |
|---|---|---|
| `Sources.read` | Actual manifest/incident/freeze/configuration/diagnosis connectors | Authenticated provenance, authority, observation time, freshness, unavailability and acquisition failures |
| `Guard.decide` | A reviewed guard with an explicit scope and current policy | Input-to-decision traces; both continuity and material-change results |
| `Executor.attempt` | A broker/actuator that can prevent the real operation under declared writer controls | Attempt, rejection/application, actual resulting state and behaviour after failures/retries |
| Common revision + permit | A justified coordination mechanism across all material writers | Race tests, bypass tests, expiry, partial failure and check-to-act gap analysis |
| `run_case` | A stateful runner that schedules changes around check and actuation | Repeatable event order, isolated target reset and persisted complete traces |
| `reproduce.evaluate` | Independent acceptance evaluation | Frozen expectations kept out of candidate inputs; separate guard and effect assertions |

This is a proposed functional mapping, **not a validated UC4 adapter**. Porting requires agreement on the current testbed schema and stateful execution capability. The most valuable next review is to challenge one successful temporal/race case and its paired failing control, then implement that pair through real testbed boundaries. Governance ownership, connector authority and distributed actuation guarantees remain open integration work.
