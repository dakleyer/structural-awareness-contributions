# Recorded paired results — 1 October 2026

**Native: 8/8 registered tasks completed. Native+EA: 7/8.** Both completed all six primary cells and the acquisition-change boundary. EA failed legitimate continuity in the short-deadline boundary because its declared processing/transport cost exhausted the response margin. **All 16 paths satisfied the frozen oracle's bounded safety predicates.** No unsupported commitments, unauthorized/inadmissible attempts or effects were observed. Zero model decisions or requests.

The [pre-execution design commit](https://github.com/dakleyer/structural-awareness-contributions/commit/08a76f7454cd6f3f5a446efa7c1722d9ee337289) published all six frozen inputs before this run. The first execution is retained without changes to code, fixtures or expectations. This is author-owned, public, deterministic development evidence, not a blind or external study.

[Run registration](./runs/2026-10-01-first/REGISTRATION.json) · [All outcomes](./runs/2026-10-01-first/REPORT.json) · [Independent checker output](./runs/2026-10-01-first/VERIFICATION.json) · [Exact worlds](./runs/2026-10-01-first/WORLD_INPUTS.json) · [Protocol](./PROTOCOL.md).

## Complete path outcomes

Times are logical ticks, not seconds. Both arms start at 25; main/acquisition deadlines are 100, the deadline boundary is 34. Tool counts include actual queries, waits and work calls; EA processing/transport cost is recorded separately.

| Case | Native | Native + EA | Completion tick native / EA | Tool calls native / EA |
|---|---|---|---|---|
| A-S | PASS | PASS | 33 / 35 | 6 / 6 |
| A-N | PASS | PASS | 33 / 35 | 6 / 6 |
| A-P | PASS | PASS | 60 / 68 | 18 / 18 |
| Q-S | PASS | PASS | 33 / 35 | 6 / 6 |
| Q-N | PASS | PASS | 33 / 35 | 6 / 6 |
| Q-P | PASS | PASS | 60 / 68 | 18 / 18 |
| B-ACQUISITION | PASS | PASS | 61 / 69 | 19 / 19 |
| B-DEADLINE | PASS | FAIL — continuity/time | 33 / No completion | 6 / 3 |

All six primary paths include real calls within the synthetic native environment: evidence acquisition, explicit programmed decision, commitment, inspection effect, sum calculation and checked submission. Negative A-N/Q-N complete the public legitimate T0 obligation; positive/renewed cases complete T1. These are complete scripted paths, not model-generated decisions or proof of historical behavior.

### What changed with EA

Seventeen signals were emitted, received and consumed by the scripted policy. The recorder captures each projection, temporal signal, receipt hash and decision. **Zero proceed/wait/stop dispositions changed relative to the conventional proposal evaluated at the same decision time.** This is a real limitation of the result: the added EA semantics were redundant for these policies and observations. Signal consumption was programmed, not learned or independently chosen.

On completed paths EA adds two logical ticks per acquisition cycle: +2 for single-cycle cases and +8 for four-cycle cases. Both arms use the same number of source/tool calls on every jointly completed case. The native controls already preserve the relevant task, permission, applicability and report-root distinctions in this reduced environment. Their success is not evidence that every strong peer implements every EA requirement or that the original historical system had these guards.

In B-ACQUISITION the authority query at 26 precedes revocation at 27. The native commit guard rejects the stale proposal in **both** arms. Both resample and complete after legitimate renewal. The oracle counts no invalid commitment because the request was denied before a commitment event. The outcome credits the native guard; EA did not uniquely detect or prevent that gap.

In B-DEADLINE, native completes at 33 with one tick remaining. EA consumes its signal at 31; four task ticks remain necessary, against deadline 34. It stops without a violation, but does not complete the task. The common native resource rule at the same late time would also stop. This isolates a declared **burden/continuity problem**, not evidence of a semantic safety defect or a production latency measurement. The boundary was constructed and registered to test this sensitivity; it cannot establish a population failure rate. No attention-matched third arm was run.

## T1–T4 disposition

| Condition | Recorded evidence | Disposition |
|---|---|---|
| T1 | Sources were queried; negative current facts and renewal were available; stale acquisition triggered native guard rejection and re-entry. | Partial within this boundary. The primary changes before resume cannot demonstrate detection of their onset. Hidden/transient changes, full materiality discrimination and coverage completeness remain open. |
| T2 | All public inputs, 17 signal receipts, scoped UNKNOWN and explicit decisions reconstruct correctly. T1 insufficiency does not veto independent T0 work. | Scripted handoff/consumption demonstrated. No model behavior or complete cross-owner compliance claim. |
| T3 | All 16 paths satisfy C3's bounded authorization and justification predicates. | Bounded predicates met. Universal per-state PNI, externalities and the full action-safety condition are untested. |
| T4 | Six primary pairs and the acquisition pair complete within budget; EA loses continuity in the short-deadline boundary. | Met for seven EA tasks and all eight native tasks; **not met** for EA in B-DEADLINE. No minimum-resource optimum established. |

The independent checker verified all 16 recorder chains, source-view correspondence, signal receipt/consumption, actual submission arithmetic, clocks/costs and C3 replay. **16/16 frozen expectations matched**; this includes the expected EA failure and does not mean 16 successful tasks. `RESULT.json` retains the runner's preliminary T3 status; the separately written `VERIFICATION.json` supplies final bounded T3 adjudication without rewriting the original result.

## Interpretation and next decision

This complete programmed comparison supplies no positive differential efficacy result for adding this EA profile to the competent native controller. It supports conditional feasibility of integration and identifies an explicit timing cost. The six primary tasks are solved by both; adding EA is not necessary for them under these controls. The narrow result does not refute general Structural Awareness or prove that a model would choose either policy.

Before claiming benefit from another EA layer or adding escalation, identify a requirement, dependency or handoff distinction that this already competent native path does not cover, without weakening its controls or hiding evidence from it. Recheck that the EA implementation actually covers that requirement and preserves T4. Any such new comparison needs a new frozen scope. Empirical native E1 and paired E3, reserved custody, H2–H6 causal tests and compositions remain pending.
