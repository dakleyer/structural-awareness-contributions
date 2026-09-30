# Additional local audit — 2026-09-30

**Publication scope:** one consolidated, additions-only package in Contributions. Existing documents, code and workflows are unchanged. All execution evidence below is local; no CI execution or deployment is claimed.

## Findings before fixes

The initial 33-row suite did not exercise malformed source contracts or multiple permit/operation identities. On the implementation from local commit `5033c4b`, the additional 13 contract tests produced **9 assertion failures, 3 execution errors and 1 pass**. These are test outcomes, not a claim of 12 independent architectural defects. The exact output and hashes are retained in [audit_v2_before.json](results/audit_v2_before.json).

| Finding | Previous behaviour | Correction |
|---|---|---|
| Empty manifest | Vacuous loop issued a permit | A usable manifest must be nonempty and structurally valid |
| Source identity and provenance | Requested-source identity, blank version and integer revision type were not enforced | Validate identity, nonblank version and positive integer revision |
| Availability/type/metadata | Text `"false"` was truthy; missing timestamp or malformed budget raised errors | Strict boolean availability; typed metadata; unknown evidence returns HOLD |
| Permit identity | Every permit used `permit-1`, so a second intent overwrote the first | Monotonic unique permit identifiers within the simulated world |
| Reused operation identifier | A completed ID with a different payload returned ALREADY_APPLIED | Preserve and compare the exact completed intent; report conflict |
| Evaluator | Empty expectations could pass vacuously; `1 == True` could satisfy application evidence | Mandatory typed outcome fields and strict output typing |

The original source and added tests are saved in [audit/before-5033c4b](audit/before-5033c4b). To reproduce the historical failures in a fresh process from this directory:

```bash
python -B -m unittest discover -s audit/before-5033c4b -p 'test_contract_edges.py' -v
```

That command is **expected to exit nonzero**. It is a historical falsifier, excluded from the current acceptance runner. The zero-budget check already passed before correction and remains a regression control.

## Composed policy changes

Adding a D4 freshness-policy update initially reused the manifest version as the selector for D1's Finance dependency. Changing the version to the freshness revision unintentionally removed Finance B. The composed D1→D4 branch incorrectly executed although B remained closed.

The failure is preserved in [d1_d4_composition_before.json](results/d1_d4_composition_before.json), with the failing model in [audit/d1_d4_before_model.py](audit/d1_d4_before_model.py). Dependency applicability and freshness budget are now independent state variables. The regression tests both event orders, and the D1→D4 branch has a separately scored scenario trace. This is evidence that passing each isolated change did not establish correctness of their composition.

## Persistent local executor and crash evidence

[durable_executor.py](durable_executor.py) stores the target row, permits and completed-operation receipts in SQLite. A guard-issued permit is registered through a trusted local interface. An execution transaction checks intent identity, expiry and revision, then updates the local target and inserts its receipt together. The protected operation is **this row update**, not an external API call.

The 11 additional tests use separate Python processes and actual process termination (`os._exit(73)`) at declared points:

| Experiment | Observed local result |
|---|---|
| Terminate before effect | No effect or receipt; retry applies once |
| Terminate after row update but before transaction commit | Both changes roll back; retry applies once |
| Terminate after commit but before acknowledgement | Effect and receipt remain; retry returns ALREADY_APPLIED without another effect |
| Four competing deliveries of the same intent | Exactly one application and three acknowledgements of the prior result |
| Two different intents sharing an old revision | One applies; the other is rejected as stale |
| Material change after guard | Old permit rejected; newer configuration preserved |
| Same ID with a changed payload after process restart | Explicit conflict; original effect unchanged |
| Modified permit or exact expiry | No effect |
| Deliberately split effect and receipt transactions, then terminate | Effect remains without receipt; safe retry rejects the stale permit but cannot acknowledge the missing result |

The last row is a **negative control**. Its regression test passes by establishing the unwanted state, not by declaring that executor safe. The complete request parameters, subprocess exit codes, output and observed database snapshots are recorded in [verification.json](results/verification.json).

## Current result and limits

**Historical v2 checkpoint below.** These results are preserved in `results/v2_verification.json` and `results/v2_37_results.json`. The subsequent [recovery extension](RECOVERY.md) and main README contain the current totals.

- **38/38 regression tests pass:** 14 scenario tests, 13 contract tests, 11 persistent-executor tests. Some contain subcases and overlap; these counts must not be added to scenario rows as independent experiments.
- **37 scenario rows:** 30 satisfy the declared acceptance criteria and 7 fail as expected controls or exposed assumptions. The original 33-row run is preserved without rewriting its historical result.
- **Two evidence levels:** deterministic in-memory scenario execution, and actual local process/SQLite transaction behaviour. Neither is a cloud deployment or a validated UC4 connector.

The extension improves evidence for strict input handling, time-of-use changes, conditional actuation, local retry handling and selected policy composition. It does not prove completeness of the governance reference, trustworthiness of external sources, cryptographic grants, distributed atomicity, an exactly-once external effect, recovery after host/power loss, acknowledgement by a human escalation owner, or full conformance to S1/S3/S10/S14.

The current model intentionally retains failures for a shared reference omission and a writer that bypasses the revision protocol. Removing these failures without adding legitimate information or enforcement would conceal an assumption, not complete the architecture.

## Remaining high-value work before integration

1. Bounded recovery/re-entry when evidence becomes available, with a current decision and no duplicate effect. **Subsequently exercised in the scoped local recovery extension; distributed recovery remains open.**
2. Explicit D2 dependency changes and their authoritative discovery signal, without giving one arm hidden information.
3. External actuation with uncertain outcomes and reconciliation: the local SQLite transaction cannot establish this property.
4. An independently reviewed testbed mapping and separate source/actuator adapters with real authority and freshness evidence.

Further work should target these open claims rather than enlarge the test count by repeating already covered branches.
