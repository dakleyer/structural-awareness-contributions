# Cost and Type 1 / Type 2 — executed DDS Stage A successor

Documentation revision0.3 · 7 October2026 · current run DDS-COST-TYPE-20261007-03.

This is a scoped implementation of the [one DDS method index](../../../../../DDS_CANONICAL_METHOD_INDEX_v0.1.md), especially [Stage A §§3.1,5.3,7.1/7.1A/7.4](../../../../../DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md). It is not a second method or Stage-B/C validation.

The successor executed **122 original-world operations and18 separate deliberate fault controls** across nine documented studies. All original-world outcomes matched their original registered predicates. Each profile's deliberate review-only control was diagnosed Type1 against a prior reachable legitimate witness; each false-closure control was diagnosed Type2. They are calibration/counterexample policies, not claims of native product failure. Original Cards, thresholds, code and results in their source directories remain unchanged.

## Current results

| Profile | Original-world operations | Type1 n/d | Type2 n/d | P outside Type2 | Selected API units, sum |
|---|---:|---:|---:|---:|---:|
| Human Escalation / Whispering | 21 | 0/11 | 1/21 | 0 | 1366 |
| STAMP/STPA | 10 | 0/6 | 0/10 | 0 | 14 |
| SPIFFE selected JWT-SVID | 25 | 0/4 | 0/25 | 0 | 109 |
| RATS local JWS roles | 20 | 0/2 | 0/20 | 0 | 135 |
| RAG retrieval | 8 | 0/5 | 1/8 | 0 | 20 |
| OAuth/OIDC | 11 | 0/3 | 0/11 | 0 | 33 |
| MCP selected calls | 9 | 0/3 | 0/9 | 0 | 35 |
| SQLite transactions / idempotency | 9 | 0/4 | 0/9 | 1 | 92 |
| Durable local workflows / retries | 9 | 1/5 | 1/9 | 0 | 79 |

These n/d values are descriptive counts of named authored fixtures, including deliberately adverse/source-fault cases. They are not human accuracy, deployment probabilities, population estimates, rankings or superiority. Deliberate controls have their own cohort and are never pooled with original-world rows. Source-fault HEW/RAG episodes retain their source-truth limits. The SQL out-of-domain orphan P remains outside diagnosed Type2 because no false closure was asserted.

## Cost accounting and the minimum

`C_observed = sum_g c_g(trace)`. Selected API operations have a frozen unit weight1. Counts come from actual SQLite API calls (including commit/rollback), actual native public-key verify calls, selected file/hash-read attempts and explicit logical policy invocations. Actor, source production, fixture and evaluator ledgers are separated. No tokens or signing/private keys are written. Instrumented wall time is separately recorded and is not added to the operation-unit sum.

HEW retains its original event-derived model-work tariff as its primary C; the finer native API ledger is supplementary. Synthetic human/calendar ticks and source-preparation charges remain model parameters. The old R01 analytical cost40 and probability law are not replaced by the local model's units.

`C_private_min_G` is exact **only over the two prospectively frozen admitted qualification graphs G**. Both were exhaustively executed in equivalent fresh resources before candidate runs. The reference graph uses the same available interfaces/information. It removes only configured redundant HEW restarts without new evidence, selects an admitted bounded workflow deferment, or uses the sole known SPIFFE trust-domain bundle to verify and reuse signed claims without a redundant payload preparse. Other profiles retain their original qualified graph. This establishes a feasible nontrivial minimum closure floor for the selected graph catalogue; it does not prove a global algorithm/product optimum.

`excess_signed = C_observed - C_private_min_G`; nonnegative excess is also reported. A cheaper trace without legitimate closure is not credited as an efficiency gain. Component differences identify repeated search/validation and commit/retry work. Where no qualifying witness exists, the minimum and excess are unavailable, not zero.

For the selected **single-domain SPIFFE convention**, the accessible-information lower bound within G is proved by the required two JSON parses, one native verify, one identity-policy entry and one resource-policy check per requested response. It is5 units for S01/S02/S21 and6 for replay S24. The generic qualified actor uses6/7, so excess1 is observed without Type1: legitimate delivery still occurs. This is a conventional native reference improvement, credited fully. The **global accessible-information lower bound remains NOT_ESTABLISHED**. Its separate field is retained. Outside that SPIFFE certificate, the measured same-information feasible witness is an upper bound on the achievable minimum, not a proved fair-policy lower bound. Pricing, tokens, network burden, actual human service and lifecycle cost remain explicitly unscored. Heterogeneous API/model units are not comparable across technologies or currencies.

## Type diagnostics

The M-admission map is produced and sealed before any candidate execution. It requires a legitimate nontrivial closure, mapped capability/permitted APIs, a useful budget/horizon, no private evaluator labels at the actor API, and a qualifying witness in G. Where original output taxonomy collapses I/M, the new floor is sufficient legitimate reference closure; this does not transfer the mathematical R01 M region or regrade an original outcome.

`Type1 = eligible no-closure / M-reachable eligible traces`. Terminal Ø/HOLD/window/work exhaustion qualifies only when M remained reachable under the frozen scoped contract. P is excluded from its numerator. Rework alone is not Type1.

`Type2 = diagnosed false-closure P / Type2-eligible traces`. The causal rules are frozen for each profile: stale/false state, identity-to-permission promotion, missing feedback, a stale receipt or missing acknowledgement falsely treated as absence of an effect. Raw P is not automatically Type2. Invalid-scope/source/capacity worlds with no admitted M witness are excluded from Type1; exclusions are preserved per case. No statistical confidence interval is offered for this authored nonrandom case set.

## Concrete examples

- **WF-04:** observed C=11 selected units versus C_min_G=7; excess=4. Retry-to-horizon remains RUNNING at synthetic tick5; bounded review closes M at tick3 under the same outage/deferment contract. This is the original-world Type1 episode.
- **TX-01:** C=7 includes a policy invocation, BEGIN, two SELECTs, two INSERTs and COMMIT. Old SQL execute-only counters were incomplete as an API-work ledger.
- **HEW-SC-02A:** original model C=18, minimum_G=18, excess=0. Its supplementary actual API count=71; these are separate units, not measured euros or human labour.

## Evidence and reproduction

- [Registration](./RUN_CARD.json), [actual-byte freeze](./FREEZE.json), [summary](./RESULTS_SUMMARY_2026-10-07.json), [examples](./INSPECTABLE_EXAMPLES_2026-10-07.json).
- [Prior M-admission map](./runs/2026-10-07-03/M_ADMISSION_BEFORE_CANDIDATES.json).
- Individual full trace/ledger/outcome records: [Human Escalation / Whispering](./runs/2026-10-07-03/hew.json), [STAMP/STPA](./runs/2026-10-07-03/stamp-stpa.json), [SPIFFE selected JWT-SVID](./runs/2026-10-07-03/spiffe-jwt.json), [RATS local JWS roles](./runs/2026-10-07-03/rats-jws.json), [RAG retrieval](./runs/2026-10-07-03/rag.json), [OAuth/OIDC](./runs/2026-10-07-03/oauth-oidc.json), [MCP selected calls](./runs/2026-10-07-03/mcp-tool-calling.json), [SQLite transactions / idempotency](./runs/2026-10-07-03/sql-transactions-idempotency.json), [Durable local workflows / retries](./runs/2026-10-07-03/durable-workflows-retries.json).
- Frozen original public source replicas are in `source/`; canonical text is a pinned `.md.txt` input snapshot, not another authority.
- Reproduce using the registered Python/SQLite/cryptography versions: `python run_metrics.py --output <fresh directory>`.

Candidate event ledgers are sealed before evaluator grading. The boundary is functional actor-API separation, not malicious-code/OS isolation or external independence. The original workflow model exposes its registered simulation law; no blind future-state claim is made. A first successful source-counter meter run is retained locally/Drive with all input bytes. The current meter counts actual native verify calls after decoding, verified by a malformed-signature0/valid-signature1 probe. Registered original-world and control outcome/candidate-cost summaries were identical across runs01/02/03; run03 prospectively adds the better SPIFFE witness and its scoped accessible-bound certificate.

SQLite evidence files and the first complete metering snapshot remain in the full Drive/local archive. GitHub carries UTF-8 reproducibility inputs, per-profile full current records and the sealed maps. No new service object, fee, contracted output or native/human/independent result is introduced.
