# DDS — SQL transactions and resource idempotency

**Current reading — documentation0.4, 7 October2026.** The [current study record](CURRENT_STUDY_RECORD.json) governs navigation, Stage/coverage and the executed cost/type successor. Dated coverage sections below retain their original evidence date; their previously unscored diagnostics are superseded only by the linked prospective successor, not by regrading original results.

<!-- Cost/type documentation addition0.3 (2026-10-07); original science/evidence edition retained. -->

<!-- DDS terminology revision 1 (2026-10-07): Stage A/B/C only; source scientific version and evidence unchanged. -->

Version0.2 ·6 October2026 · completed within declared local-database scope.

> **DDS classification — 7 October 2026.** This is a **Simplified DDS Stage A — Specification Discovery** study under the [DDS Canonical Method Index](../../../../../DDS_CANONICAL_METHOD_INDEX_v0.1.md). Executed local code/fixtures strengthen its evidence mode but do not make it Stage B architecture verification or Stage C native/product validation. Frozen Run Cards, FREEZE files and RESULTS retain their original execution-time identity and are not rewritten by this classification.


## Executive finding

The selected conventional transaction/key/receipt composition closes the local task under its declared domain. It cannot provide atomicity for an effect committed elsewhere or turn an outbox entry into completed downstream service. Correctly preserving an old operation can also mean refusing a changed current request.

The [extension](./EXTENSION.md) records the local base, Stage1 transfer limits and Stage2 producers/interactions. No provider, distributed transaction or R01 performance result is imported.

## Actual execution and evidence

[Run01](./runs/2026-10-06-01/RESULTS.json): **9 cases,18 frozen assertions,4 I,4 Ø,1 retained P diagnostic**. Actual SQLite files/connections commit, rollback, enforce operation-key uniqueness and recover receipts. No broker, PostgreSQL, payment service, physical actuator or power-loss test is executed.

|Boundary|Actual result|Supported conclusion|
|---|---|---|
|Single local transaction|Matching committed effect/receipt|Sufficient local I|
|Rollback before commit|No local effect or receipt|Ø, not a false successful mission|
|Stable retry/two stale prechecks|One committed ledger row|Selected native key enforcement/recovery|
|Changed payload under same key|Prior row preserved; no matching current receipt|Ø for this request; prior I not reused as permission|
|Outbox without completed consumer|Local record exists, broader task incomplete|Ø; producer intent is not delivery|
|Separate file commits before primary abort|Primary empty, second file retains one effect|P outside the one-database atomicity contract|
|Lost acknowledgement|Later connection finds committed matching receipt|Local recovery I, not new external work|

The four I cases are designed local outcomes, not a population transaction success rate. The two-connection witness covers its bounded order only. The P is a deliberate cross-domain application counterexample, not a failure of SQLite's within-domain transaction semantics.

## Freeze, trace and oracle

[Card](./RUN_CARD.json) and [Freeze](./FREEZE.json) pin code/inputs before the run. The runner verifies versions/hashes and writes only fresh outputs. Expected labels and selected task sufficiency remain with the evaluator.

A fresh connection inspects actual committed ledger/receipt/outbox rows; another fresh file is inspected for the out-of-domain effect. Current requested payload is compared with the actual receipt, not the controller's reported success. Separate connections/functions are same-author instrumentation, not independence or OS adversarial isolation.

## Cost/Risk/Effectiveness and Business Value

**Cost:** the reported SQL field counts instrumented explicit execute calls. Native commit/rollback/implicit/internal statements, connection work and producer/storage lifecycle are not a complete measured C ledger; the separately labelled setup count covers explicit fixture calls only. No omitted primitive is declared free. Locks, contention, journals, backup/recovery, key retention, network/consumer, maintenance, actual latency and tariffs remain unscored. Counts describe work, not money or an optimal frontier.

**Risk:** wrong/duplicate/unauthorized effects and the declared orphan out-of-domain effect. One retained P makes the domain boundary visible. No population R or severity-weighted loss is measured.

**Effectiveness:** sufficient current-task receipt versus Ø, with prior effect and downstream completion distinguished. Ledger success is not universal business-flow success. No representative availability/throughput or end-to-end probability is inferred.

**Business Value:** conditional local consistency, replay-safe effect and recoverable accountability. Limits include unstable operation meaning, effects outside the domain, consumer/source uncertainty and physical/administrative failures. No financial ROI or full-service adequacy is calibrated.

## Coverage, comparator and closure

|DDS surface|State|
|---|---|
|Challenge/base/configuration|Used finite local task; atomic/delivery-domain differences explicitly frozen|
|Stage1 / Stage2|Performed within scope; native local semantics and five composed mechanisms; no R01/global proof|
|Routes/gates/trace|Reduced deterministic I/P/Ø; M unscored; actual local files and post-effect inspection|
|C/R/E|Descriptive partial operation counters/selected predicates; full tariffs/lifecycle/population unscored|
|Acceptance/BV|Binary registered expectations and conditional local value; no global deployment acceptance|
|Reproduction/native/comparison|Card/Freeze/code/results; actual embedded SQLite, no distributed product/matched vendor campaign|
|EA/rework|No automatic Type1/2; minimum-work/excess-work witness not computed|

A competent conventional implementation receives full credit for local atomicity and keys. **Differential finding:** local sufficient routes and explicit cross-domain limits; no new-architecture superiority established.

**Closure:** the agreed local question has a supported answer including its counterexample. A broader service question requires a defined effect domain, native resource/consumer contracts, source authority, relevant failures and actual cost/time evidence in a new scoped prospective study. More universal testing or commercial outputs are not automatically due.

## Delivery and reproduction

This scoped executive/technical record, extension, source/Card/Freeze/code/results are in the same extension leaf and mirrored in Drive. Sponsor/DOI/forum outputs remain unissued; no commissioned10–15/30–35 page client package is claimed. Programme/SOW categories and fees are unchanged.

~~~sh
python -B study.py --output PATH_TO_A_NEW_EMPTY_RUN_DIRECTORY
~~~

Pinned Python3.12.14 and SQLite3.53.1. Only fresh synthetic local databases are written. [Scenarios/primary sources](./EXTENSION.md) · [owning review](./README_VNext.md).


## Current canonical DDS compatibility — reporting addition0.2

Reviewed canonical source 09b8fe09082f15612114ebe0fd3be8418be7a061 after these runs; executed source remains409bfa9eff2b3e24e7350021db9e587861583de8. This is a retrospective coverage declaration, not a preregistration amendment or new score.

- **Blind evaluator-private route map:** not used as a blind trajectory/efficiency experiment. Selected controller/API boundaries are described; no blind/native/OS-isolation claim.
- **Minimum-work/rework witness:** not scored. Neither an evaluator-private optimum nor an accessible-information lower bound is computed; reported work is not optimal work.
- **M-admission / Type1:** not established for an estimator under the current full admission rule. No eligible population, denominator or Type1 rate is defined. The workflow's previously recorded WF04 flag/witness is descriptive within its old execution contract; its local reachable M does not establish the newly required full physical-budget/useful-horizon/capability-information admission.
- **Type2:** not scored as an estimate; causal T2 eligibility/rule was not preregistered. Selected P remains a material violation, not automatically Type2.
- **Type0/unresolved:** kept outside such estimates. No universal diagnosis or probability is assigned.

These explicit omissions are permitted by the single DDS's partial-coverage rule. [Machine-readable current-surface crosswalk](./CURRENT_DDS_COVERAGE_2026-10-06.json) records the boundary. No original source/result/threshold is changed; useful local findings and scoped closure remain.


## Cost and Type1 / Type2 successor — 7 October2026

Documentation addition0.3. The [executed cost/type packet](../cost-type-diagnostics-v0.1/README.md) prospectively replays this profile's original-world outcomes with a finer selected actor/source/evaluator ledger, prior M-admission, minimum-work witnesses over frozen G and separate Type1/Type2 causal counts. It includes the current scoped SPIFFE accessible-G bound and conventional reference improvement. Original registered source results/thresholds remain unchanged; this successor does not establish global minimum, monetary calibration, population probabilities, real human accuracy, Stage B/C or independent validation. Per-case records retain exclusions and deliberate defect controls as a separate cohort.
