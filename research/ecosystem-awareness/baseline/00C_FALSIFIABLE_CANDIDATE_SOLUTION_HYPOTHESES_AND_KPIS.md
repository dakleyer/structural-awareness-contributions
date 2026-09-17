# Falsifiable Candidate-Solution Hypotheses and KPI Protocol

> **Universal test layer.** This page states the hypotheses that **any** candidate solution to the changed-decision-basis challenge must make testable. It is not an EA architecture description, a market benchmark, a maturity score, or evidence that a candidate has passed.

**Status:** working research test specification. The identifiers `C-H1`–`C-H5` are intentionally distinct from the foundational H1–H6 and from the EA-specific differential hypotheses in [07](./07_EA_CANDIDATE_DIFFERENTIAL_HYPOTHESES_v0.5_REVIEWED_WORKING.md).

## 1. Reading position and separation of questions

Use the core route in this order:

1. [Challenge](../../../submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/04_ANNEX_III_Challenges_Exposed_by_the_Case.md)
2. [Sufficiently-good solution requirements](./00A_SUFFICIENTLY_GOOD_SOLUTION_REQUIREMENTS.md)
3. **This page — universal candidate hypotheses and KPIs**
4. [EA-specific differential hypotheses](./07_EA_CANDIDATE_DIFFERENTIAL_HYPOTHESES_v0.5_REVIEWED_WORKING.md)
5. [Concrete EA architecture](./00_CANONICAL_ARCHITECTURE_TOPOLOGY.md)

The separate [market and industry benchmark](./00D_MARKET_AND_INDUSTRY_BENCHMARK_RESEARCH_v0.1.md) uses these same tests to ask whether existing industry configurations meet them. It is evidence about the market, not a prerequisite for defining what a candidate must prove.

For every candidate, keep three determinations separate:

1. **Requirement evidence:** did it meet the relevant condition in 00A for the declared case?
2. **Hypothesis evidence:** did it survive the corresponding falsification test below?
3. **Candidate differential:** if a specific architecture claims an advantage, did it outperform an equally capable peer under matched conditions?

## 2. Common test contract

Before running a case, declare the decision and owner; `T0 → T1 → T2` facts; branch oracle; evidence availability; authority and null action; materiality and coverage boundary; response deadline; capacity; posture/action vocabulary; and cost ledger. Run all compared configurations on the same facts, permitted evidence, authority, deadline and human/tool budget.

Report every KPI with its numerator, denominator, branch and configuration. Record distributions or case-level values when samples are small. A command receipt, elapsed time, confidence score or human approval is not an outcome unless the pre-declared observable effect is also recorded. Do not pool heterogeneous branches into a single unsupported score.

The minimum outcome vector is:

`[false continuation, false containment, qualified-posture correctness, deadline pass, handoff integrity, observable outcome effect, total decision burden]`.

## 3. Candidate hypotheses and measures

| Universal hypothesis | Linked sufficiently-good conditions (00A) | KPI — how it is measured | Principal branches | Falsifier / failure condition |
| --- | --- | --- | --- | --- |
| **C-H1 — qualification of the material decision basis.** The candidate distinguishes declared material change or insufficient establishment from ordinary variation within its coverage boundary. | Material-break awareness; declared coverage boundary. | **Material-break recall:** oracle-declared material breaks exposed with affected basis ÷ oracle-declared material-break branches. **Material-break precision:** exposed material breaks confirmed by oracle ÷ exposed material-break alerts. **False-continuation rate:** CONTINUE/PASS after a break requiring requalification or containment ÷ applicable break branches. | C1, C2, C3. | It continues without exposing the affected basis after an observed material break, treats all C1 continuity as a break, or claims detection outside declared evidence/coverage. |
| **C-H2 — qualified, owner-bound posture.** The candidate turns its qualification into an explicit posture without collapsing unresolved state or assuming another owner's authority. | Qualified operating posture; owner-preserving handoff. | **Posture correctness:** runs whose posture is within the branch oracle's permitted set ÷ applicable runs. **Unresolved-state preservation:** required UNKNOWN/unresolved fields retained ÷ cases requiring them. **Authority-field completeness:** handoffs with owner, authority, scope, freshness, dependency and expiry fields ÷ handoffs requiring them. | C2, C3, C5, C6. | It emits only a score/log; maps uncertainty to PASS; selects a posture outside the owner/authority boundary; or loses required qualification fields at handoff. |
| **C-H3 — bounded and authorized response.** The candidate couples a posture only to an authorized response, abstention or fallback with declared bounded downside. | Bounded-downside response; strong action-safety class where claimed. | **Authorized-response compliance:** non-null actions within declared authority/action library ÷ non-null actions. **Reversibility/containment compliance:** applicable responses meeting their declared bound ÷ applicable responses. **False-positive response cost:** cost of unnecessary non-null actions ÷ C1 runs. **PNI claim test (only if claimed):** admissible covered states where `U(A,ω) ≥ U(A_null,ω)` ÷ all declared admissible states; a PNI claim requires 100%. | C1, C2, C4, C5. | Any action exceeds authority, has undeclared/unbounded downside, or a claimed PNI action is worse than null action in any covered admissible state. |
| **C-H4 — timely, viable minimum-sufficient requalification.** The candidate reaches a justified posture while a legitimate response remains possible, using no more observation/review than is decision-relevant. | Viable decision support; timely qualification; minimum sufficient intervention; non-monotone composition. | **Deadline-pass rate:** runs producing a permitted posture with a reachable authorized response before deadline ÷ applicable runs. **Remaining response margin:** deadline minus posture time, reported per run. **Decision-relevant evidence yield:** acquisitions/reviews that change justified posture or action set ÷ total acquisitions/reviews. **Total decision burden:** compute, tool, communication, waiting, reviewer and response cost per run. | C1, C2, C3, C5. | It reaches its answer after no legitimate response remains, depends on unlimited search/review, expands layers without accounting for conflict/latency, or adds burden with no decision-relevant change. |
| **C-H5 — scoped handoff and targeted re-entry.** The candidate preserves what the receiver needs and requalifies the affected basis rather than creating a global conclusion or indiscriminate rerun. | Owner-preserving handoff; timely qualification; minimum sufficient intervention; declared coverage boundary. | **Handoff integrity:** required scope, provenance/freshness, dependency, unresolved, capacity and authority fields preserved at receiver ÷ required fields. **Wrong-domain closure rate:** system-wide closure from local/insufficiently scoped determination ÷ C6 runs. **Targeted re-entry precision/recall:** correctly reopened assumptions ÷ reopened assumptions; correctly reopened assumptions ÷ oracle-invalidated assumptions. **Indiscriminate-rerun rate:** unnecessary full reruns ÷ re-entry cases. | C2, C3, C6. | A receiver makes an unsupported global conclusion, loses residual/provenance, reopens the wrong basis, or must rerun indiscriminately to recover qualification. |

## 4. Interpretation

A candidate is assessed only for its declared decision domain, evidence boundary, owner, authority, horizon and resource envelope. Passing one branch does not certify another. A low error rate purchased by extra authority, unlimited human attention, more evidence, a longer deadline or a broader observation boundary is not a pass unless that changed resource/authority envelope is declared and compared like for like.

The tests can yield a mixed or negative result:

| Result | Meaning |
| --- | --- |
| **Supported for a declared case** | The candidate meets the linked conditions and survives the named falsifiers for that case and envelope. |
| **Partial / bounded** | Some branches or KPIs pass, but the coverage or resource condition narrows the claim. |
| **Insufficient evidence** | The test contract, oracle, field data or comparable measurement is missing. |
| **Falsified** | A named failure condition occurs under the declared conditions. |

This page therefore defines **what must be tested of a candidate**, not which industry product, protocol or EA mechanism is best. The independent industry comparison belongs in [00D](./00D_MARKET_AND_INDUSTRY_BENCHMARK_RESEARCH_v0.1.md); EA's claimed architectural differential belongs in [07](./07_EA_CANDIDATE_DIFFERENTIAL_HYPOTHESES_v0.5_REVIEWED_WORKING.md).
