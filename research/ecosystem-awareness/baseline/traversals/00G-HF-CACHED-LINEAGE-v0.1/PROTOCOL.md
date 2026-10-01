# 00G-HF — cached lineage negative reference and repair v0.1

1 October 2026. Author-designed deterministic software experiment. **No model decisions, product benchmark, historical reconstruction, independent validation or empirical E1/E3 claim.** This package implements a narrower software witness while external model execution remains unavailable.

## Mechanism and claim

The ordinary reference qualifies source roots on enrollment, stores that mapping for a fixed 60-tick TTL and uses the cached mapping when evaluating authenticated current reports. It checks report identity, claim, value and expiry and requires two distinct cached roots before changing mission. Its specific defect is assuming that a stable source identifier and an unexpired local cache preserve the source-to-root relationship. The implementation contains no case-ID checks, hidden-world access or instruction to fail; the cache strategy itself is deliberately chosen as the hypothesis to test. This is a constructed defective application policy, not a discovered defect in a vendor product.

N and R1 relay S1. R2 relays S2. Initially S1 and S2 have independent roots. In F, S2 adopts S1's root before new report receipts are issued, while authenticated identities and interfaces stay the same. In G, the two roots remain independent. Three voices are therefore compatible with either one or two roots. Summaries retain all receipt IDs; no provenance loss during compaction is imposed. Receivers are fixed software policies, so the experiment does not test a model's susceptibility to social pressure or emergent collective reasoning.

The mission starts at FRAME_A. A common standing conditional grant allows FRAME_B when supported by two current independent roots. Mandate, tool access, applicability scope, grant validity and quorum threshold remain unchanged in F/G. The business result is the correct synthetic report, not merely absence of a prohibited action. All report data are synthetic and readable by every arm. The evaluator decides whether changing the mission complied with the standing condition.

## Important boundary from the previous native lot

This is a **new application profile**, not the earlier `00G-HF-NATIVE-v0.1` with its controls disabled. That application rechecked ground-truth predicates at effect time and remains unchanged. Here the application's documented contract places semantic receipt qualification in its receiver; output transport validates allowed operation, frame, total, deadline and single delivery. Every arm uses those same controls. A server that also rechecks root independence would already prevent this defect; that would be conventional mitigation, not an EA-specific result.

## Frozen arms

| Arm | Decision basis | Additional charged work |
|---|---|---|
| cached | Enrollment root mapping within local TTL | None |
| placebo | Same cached policy; resolver is called but its semantic contents are not applied | Same resolver, processing and transport ticks as EA |
| ea | Same cached proposal; frozen EA v0.1/v0.2 qualifies actual receipt roots and receiver consumes signal | Current receipt resolution + one processing + one transport tick |
| fresh | Conventional receiver resolves current receipt roots for every decision, without EA | Same receipt-resolution call; no EA signal overhead |
| ignored | Same correct EA signal, deliberately ignored by the stipulated receiver | Same observation, processing and transport as EA |

The placebo is a causal ablation, not a recommended competitor. It matches acquisition and logical attention/transport cost, not actual CPU instructions, bandwidth or production latency. Those equivalences are not claimed. The fresh arm tests whether ordinary revalidation already repairs the defect; preserve that success. The ignoring arm tests response closure, not whether a real model would ignore a signal.

## Inputs, cases and information boundary

`CASES.json` fixes ten worlds. The first six form F/G pairs under direct relay, summary and pause/reentry. S-A checks original-mission continuity. U-F/U-G make the resolver unavailable and test safe uncertainty versus inability to complete a legitimate transition. D-G shortens the valid-transition deadline to 19. No hidden change is claimed detected in U; unavailable evidence is not proof that dependence changed.

Receivers see only enrollment, current authenticated message references, responses to calls they make, and delivered signals. The runner holds branch truth and outcomes. In F/G, public enrollment and message packets are identical; current lineage resolution reveals the difference equally to every arm. EA never receives `pivot`, expected outcome or case ID. Code boundaries are audited, not security isolation against a hostile implementation. Authentication and provenance are trusted synthetic service assertions, not verified cryptography or statistical independence.

Receipt root assignments are immutable facts about issued reports. Their validity intervals come from the synthetic service and expire at tick 80. They are not invented leases guaranteeing future upstream stability. Static authority/access/applicability contracts last to tick 100. EA consumes the unchanged qualification and temporal components through `ea_bridge.py`. Old snapshots are genuine initial reports, not fabricated future support. Missing receipt responses preserve UNKNOWN. The core's UNKNOWN for insufficient roots does not itself assert that the underlying claim is false.

## Budgets and declared behavior

One execution per case/arm, fresh state, no retries. Enrollment costs one tick. Reentry occurs at tick 10 or 20 for pause. Direct/pause delivery costs three ticks for three messages; summary costs one, equally within each pair. Resolving the three exact receipt IDs costs two. EA/placebo processing and transport cost one each. Every receiver decision costs one. Reading data and delivering a report cost one each. Maximum 12 service calls, three receipts, zero humans, zero API requests. Normal deadline 60; D-G deadline 19. Completion must be strictly before the deadline. Actual local wall duration is retained but is not a production timing measurement. Execution has bounded fixed control flow; no statistical reliability inference follows from deterministic repetitions.

The cached receiver's local expiry is tick 61. It must still be unexpired when the failure occurs; otherwise a different mechanism has been tested. The fresh receiver falls back to the authorized FRAME_A if it cannot establish the transition condition. The EA receiver likewise retains FRAME_A for insufficient evidence, but stops when the signal leaves no response margin. A legitimate required transition then fails task continuity. None of these response policies is presented as optimal or as an autonomous model's choice.

## Execution order and stopping

Publish this protocol, cases, predictions, implementation, verifier and hashes before the first registered traversal. No traversal is used as a pre-publication smoke test. Compile/import checks are permitted. Native phase runs all ten cases once and preserves every result. Paired phase is admitted only if native logs contain an observed unauthorized mission change. Its registration pins the native evidence. It then executes all five arms on all ten worlds, including a native repeat; identical repeats are not additional independent evidence.

Stop after those registered lots. If implementation or verification fails, retain the exact first code and outputs and issue a successor before repair/rerun. Do not weaken a passing peer or alter worlds until it fails. `EXPECTED.json` is an author prediction for development checks; passing that check can mean observing an expected operational failure.

## Sufficiency interpretation and possible results

- T1: visible change in receipt dependence must be identified. Resolver outage supplies evidence of a gap, not identification of a dependency change. Coverage is only this declared fixture boundary.
- T2: signal scope, emission, receipt, decision reference and disposition change are logged. Correct ignored signals must not count as repair.
- T3: preserve authority and deliver A in F while delivering B in G. This tests bounded operational outcomes, not universal PNI or unmodeled externalities.
- T4: completion before the common deadline with all declared work charged. D-G can expose EA overhead even when its semantic assessment is correct.

The strongest allowed positive conclusion is that this EA integration repairs this software reference in the primary pairs. If fresh also repairs it, there is **no unique EA semantic advantage over the conventional refreshed comparator**. If cached already succeeds, no negative witness exists in that case. If EA blocks valid G or exceeds its deadline, report the operational failure. No result here establishes that full canonical T1–T4, all S1–S14 or an external autonomous competitor have been validated.

## Evidence and reproduction

`FREEZE.json` hashes the sources, protocol, worlds, predictions and unchanged external EA modules. `run.py` writes registration before its first episode and captures each request, response, signal, decision, cost and accepted delivery in a hash-chained journal. `oracle.py` adjudicates the actual delivered mission independently of receiver claims. `verify.py` checks chain/time consistency, real receipt bindings, signal inputs/outputs, delivery totals, actual mission outcomes, matched F/G prefixes, registered predictions and native replay. Verification is author-run and is not independent external review.

Run from this directory with Python 3.10+ and a new output directory each time:

```sh
python run.py --phase native --output-dir runs/native-first
python verify.py runs/native-first
python run.py --phase paired --native-run runs/native-first --output-dir runs/paired-first
python verify.py runs/paired-first --native-run runs/native-first
```

Model access remains a separate dependency. This software experiment is not substituted for a model run in the empirical workplan.
