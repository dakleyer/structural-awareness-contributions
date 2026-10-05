# R01 candidate-isolation contract

Working contract v0.1 · 5 October 2026.

This contract applies to **real T03 technology execution**. The Python adapters under `adapters/` are author-constructed instrumentation controls that run in-process; they are **not** an acceptable placement for real candidate decision logic. A small trusted testbed shim may run in-process only when its role is limited to protocol/mapping mediation for an isolated candidate runtime and its code is version-pinned/reviewed.

## Why this boundary is required

Oracle blindness is stronger than omitting fields from the input object. A candidate executing in the same trusted process/filesystem could read:

- `private_world`;
- frozen expected outcomes;
- reference implementations;
- previous oracle results;
- held-out fixtures.

Therefore a real candidate must run outside the oracle trust boundary.

## Admitted isolation modes

A T03 registration must select one of:

- `REMOTE_API_NO_ORACLE_STORAGE_ACCESS` — remote runtime receives only registered requests/tool responses and has no oracle storage access;
- `CONTAINER_NO_ORACLE_MOUNT` — local/container runtime with no oracle, private-world or expected-outcome mount;
- `EXTERNAL_SANDBOX_NO_ORACLE_FS` — external sandbox/process boundary with evidence that the oracle filesystem is not visible.

Candidate decision logic is never admitted in-process with oracle storage. A trusted testbed-owned adapter shim may be in-process if the actual candidate runtime remains behind one of the isolation modes above and the shim cannot turn oracle data into candidate input.

## Required negative properties

For a real run, all of these must be false:

- oracle filesystem visible;
- expected outcomes visible;
- private world visible;
- oracle/evaluator endpoint exposed to the candidate.

The working directory must be isolated and the registration must record any secrets and network destinations made available to the candidate.

## Evidence

The registration records `isolation_evidence`: for example a container mount manifest, sandbox policy, remote API architecture record or equivalent reproducible evidence. A textual claim alone is not sufficient for an admitted T03 campaign.

## Disclosure timing

Oracle-side adjudication and expected outcomes must not be released to a candidate between registered episodes when that release could contaminate later episodes. The registration must choose a disclosure policy such as:

- `AFTER_ALL_REGISTERED_RUNS`;
- `AFTER_CAMPAIGN_SEAL`.

Earlier release requires a new campaign registration because it changes the candidate's available information.

## UC-4 relation

This isolation boundary is R01-specific evaluator hygiene. It does not redefine Nelson Trasatti's UC-4 signal semantics or adapters. It protects the separation assumed by the UC-4 experiment model: source facts/mappings are candidate inputs; expected/reference results remain independently frozen for comparison.
