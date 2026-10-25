# DDS-MR-01 — Independent DDS Methodology Audit: R1/R2/R3 (v0.2)

**Status:** READY FOR BOUNDED DOCUMENTARY REVIEW; reviewer **UNASSIGNED**; no independent findings received.  
**Home / authority:** Ecosystem Awareness → DDS → review-packets/DDS-MR-01. Internal methodological review under DDS-QA-01 **QC-05**, informed by UC21 roadmap **Area 5**; not a new stage, test method, UC4 experiment or FG-TIDA submission.  
**Owner / assignment gate:** Iván Abril Palma. A proposed external reviewer must accept the work and disclose relevant interests before any claim of independent review. Formal attribution and any FG-TIDA publication are later owner-controlled steps.  
**Lineage:** corrects/operationalises the [Drive planning draft v0.1](https://docs.google.com/document/d/1gFY7fY00KN8-u5_tLMGiwXY3aGp-JSMN5LbMhC-7pYA/edit); the draft's proposed generic `R3-B` name is **not adopted** because it collides with existing source-specific labels. This GitHub packet is the review workspace; Drive remains historical coordination context.

## 0. Start here — one bounded task

**Question:** Is the *prospective DDS comparison method* auditable and falsifiable when (a) a competent conventional solution repairs a **known** R1 failure in R2, paying its real preparation/adaptation cost, and (b) a subsequent **material R3 variant is selected and held privately** from a preregistered family until legitimate observation, with meaningful continuity and effects measured for both arms?

**Do this, in order:**
1. Read the pinned method excerpts in §1, then the exact UC21/S5 worked source in §2.
2. Answer **M01–M09** in §3 as `CONFORMING / DEFECT / UNCLEAR / NOT_APPLICABLE`, citing a section and exact source link each time. An `UNCLEAR` is not a PASS.
3. Apply the two deliberately invalid paper rows **N1–N2** in §4; record whether the method flags each error. Optionally add one independent counterexample.
4. Copy [REVIEW_RECORD_TEMPLATE.md](./REVIEW_RECORD_TEMPLATE.md), complete one findings file (normally 1–3 pages), and submit it as a GitHub PR per §6. **Do not edit this task or any frozen source as your review answer.**

**Time box:** approximately 4–6 hours as planning guidance, subject to the reviewer's acceptance. **Deliverable:** one evidence-linked methodology audit and one falsification example; **not** D1–D5 separate papers, a new vendor campaign, code, a product assessment, an R3-U solution or a scientific endorsement. One clarification round is permitted; additional research requires separate scope.

## 1. Input pack — pinned technical baseline

The audit **reference cut** is Contributions commit `f89565fabcc1a256aa7619a6e7fb7df9c1e41a75` (25 October 2026). Compare current `main` only to report subsequent drift; do not silently change your review baseline.

| Read | Exact pinned input | What to inspect |
|---|---|---|
| A, required | [DDS Canonical Method Index — §§1, 5, 12–14](https://github.com/dakleyer/structural-awareness-contributions/blob/f89565fabcc1a256aa7619a6e7fb7df9c1e41a75/research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md) | Stage names, source namespaces, entry conditions, R2 preparation cost and R3 private variant custody |
| B, required | [DDS Stage A / Challenge–Trajectory — §§10a, 15.1 and 17](https://github.com/dakleyer/structural-awareness-contributions/blob/f89565fabcc1a256aa7619a6e7fb7df9c1e41a75/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md) | Freeze, selector/observer separation, conditional versus blind inference, prospective operational fields |
| C, required | [00D comparator benchmark — §4.2](https://github.com/dakleyer/structural-awareness-contributions/blob/f89565fabcc1a256aa7619a6e7fb7df9c1e41a75/research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) | Total cost/horizon, strong conventional peer, CRE vs technical PASS |
| D, example | [Original UC21 S5 — 00I, frozen source aec08fb5](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/annexes/scenarios/S5.md) and [original UC21 use case](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/USE_CASE.md) | S5 Q0–Q6, V0/V11, legitimate continuation and local `R0/R1/R2` |
| E, scope check | [Stage A v0.2 external-audit checklist](https://github.com/dakleyer/structural-awareness-contributions/blob/f89565fabcc1a256aa7619a6e7fb7df9c1e41a75/research/ecosystem-awareness/DDS_STAGE_A_GATE_DIAGNOSTIC_EXTERNAL_AUDIT_CHECKLIST_v0.2.md) and [freeze manifest](https://github.com/dakleyer/structural-awareness-contributions/blob/f89565fabcc1a256aa7619a6e7fb7df9c1e41a75/research/ecosystem-awareness/DDS_STAGE_A_GATE_DIAGNOSTIC_AUDIT_MANIFEST_v0.2.json) | Adjacent **instrument** review (15 SA-G gates); *not* the same as this R2/R3 **method** audit |

Other DDS [Stage B](https://github.com/dakleyer/structural-awareness-contributions/blob/f89565fabcc1a256aa7619a6e7fb7df9c1e41a75/research/ecosystem-awareness/DDS_GATE_B_ARCHITECTURE_VERIFICATION_v0.1.md) and [Stage C](https://github.com/dakleyer/structural-awareness-contributions/blob/f89565fabcc1a256aa7619a6e7fb7df9c1e41a75/research/ecosystem-awareness/DDS_GATE_C_IMPLEMENTATION_PROBLEM_VALIDATION_v0.1.md) define different objects of test. Their existence supplies no Stage B/C results.

**Public coordination context (not a frozen experiment or acceptance of this task):** [UC21 Issue #21](https://github.com/FG-TIDA/use-cases/issues/21), [roadmap Areas 5–7](https://github.com/FG-TIDA/use-cases/issues/21#issuecomment-6166486213), [Steven Zhao's freeze/negative controls](https://github.com/FG-TIDA/use-cases/issues/21#issuecomment-6171419825), [Nelson Trasatti's source-led cycle](https://github.com/FG-TIDA/use-cases/issues/21#issuecomment-6187658057), [evidence/closure distinction](https://github.com/FG-TIDA/use-cases/issues/21#issuecomment-6263257536). These links show prior discussion, **not** appointments or validation of the proposed R3 method. [DDS-QA-01 Drive index](https://docs.google.com/document/d/1Lf-uhRfHQ6Qk9wrETloUO4pwZjI5_ar4QlLbkHsFJ4k/edit) is coordination context; all **mandatory audit materials are public and linked above**.

## 2. Vocabulary and exact example — no silent renaming

| Dimension | Identity in this review | Non-transfer rule |
|---|---|---|
| DDS development stage | Stage A = specification discovery; B = architecture verification; C = implementation/problem validation | A documentary method audit is **not** B or C. |
| Optional DDS comparison shorthand | `R1` = competent initial configuration; `R2` = repaired/strengthened after demonstrated initial **FAIL**; `R3` = frozen successful predecessor facing subsequent admitted material change | These are conditional prospective comparison **positions**, not new source-native trial IDs or the EA arm. |
| UC21 source-native | `R0` ordinary, `R1` successful reinforced correction, `R2` same correction under change | For UC21 recurrence, require its **own demonstrated R1 PASS** and admissible change domain before R2; no automatic generic R1-PASS → UC21 R2 mapping. |
| Other sources | UC20 frozen `R0/R1/R2`, R01 `R1/R2/R3`, 00D `B0–B3`, DBC `R0–R3`, UC4 Stage-0/1 | Retain each origin's gates, validity and recorded outcomes. `R3-B` already means something else in R01/Flores; do **not** reuse as a generic name. |

**Worked paper route (one case only): UC21 S5 / 00I — “The Patch That Undid the Fix”.** The documented incident is synthetic. A queued rollback approved earlier may become unjustified after a later forward fix and freeze. Inspect **S5-Q1** (explicit decision basis), **S5-Q5** (scoped timely response/continuity), **S5-Q6** (last-check-to-act binding), corresponding to the original S5 local **Q1/Q5/Q6**. Use V0 (no material change, valid action continues) as the **positive** control; V11 (source/dependency-model drift) may illustrate a material challenge. The original S5 annex itself names V11 publicly. **Therefore V11 used here is a known documentary example, not independently blinded R3 evidence.** No R1 native PASS, vendor benchmark, observed production effect or differential is manufactured for this tabletop.

**Eligibility check:** write `PREDECESSOR_NOT_VERIFIED → R3 NOT_ADMITTED` unless a *real, source-pinned* prior eligible PASS is supplied. You may reason `IF a future R1 PASS were verified...` to test method logic, but never record the conditional as an achieved PASS. An existing symbolic fixture may support a stated local result only within its own recorded evidence mode.

## 3. Review checklist — write a source-linked answer for each

| ID | Check and test question | Must be true for a method-level `CONFORMING` opinion |
|---|---|---|
| **M01** | Stage, source labels and claim | DDS A/B/C, generic optional shorthand, UC21, UC20, R01, 00D and UC4 are not conflated; no inherited PASS from another namespace. |
| **M02** | Eligibility and evidence | R2 requires actual R1 failure, repair is proven before subsequent stress; R3 requires the applicable documented predecessor PASS; absent evidence is `NOT_ESTABLISHED/NOT_ADMITTED`, not `FAIL` or a fictional PASS. |
| **M03** | Legitimate R2 information | The competitor **may learn the actual observed R1 failure** and engineer the strongest feasible correction. It may NOT learn the exact scored future R3 realization and tailored answer. |
| **M04** | R2 full adaptation cost | Register diagnosis, search incl. failed iterations, expert time, engineering, integration, verification, sources/monitoring, acquisition, rollout/rollback, recurring overhead; measure or mark `NOT_MEASURED`, never silently assume free perfect configuration. Technical PASS and CRE/business burden judgement remain separate. |
| **M05** | R3 variant family and prospective selection | Before results, register family/generator, materiality, allowed ranges, controls, number of trials, selection/admission rule, comparator and limits. Privately select a variant **within** this rule, not opportunistically after observing outcomes. |
| **M06** | Selector custody and no foreknowledge | A separate custodian commits to variant/seed or a sealed hash, timestamps selection and disclosure, records who knew what when, and protects exact realization from **both** candidate and strong peer until legitimate observation. Interests/exposure and leakage are reviewable. |
| **M07** | Fair controls and real counterexamples | Matched information, tools, budgets, horizon and permitted ordinary adaptation; no-change/harmless-change positive controls plus fail-capable negative checks; deny-all/stop-all cannot succeed by defeating legitimate continuity. Conventional tie/better outcome is accepted. |
| **M08** | Actions, external effect and total burden | Separate detection, gate verdict, authorized action, downstream observation, latency, requalification, false alerts, human load and runtime costs; absent external effect cannot be scored as achieved. Compare full horizon and explain amortization/exclusions. |
| **M09** | Evidence ceiling, reviewer independence and inference | Instrument qualification, supplied source finding, native execution and independently observed effect have distinct producers/pins/modes. No manufacturer or FG-TIDA endorsement is inferred; a deliberately out-of-covered-envelope test is conditional/existential, **not** a population success rate. |

**R3 novelty boundary:** A preregistered *family* may be known; the exact **scored realization** must not. An event outside that family is an **open-world exploratory/successor** question unless a distinct prospective neutral admission/denominator protocol is established. Do not invent a new generic `R3-B` or promote the proposed `R3-U` from the Drive draft to an already adopted canonical traversal. Record any stronger open-world design as a recommendation, not a mandatory deliverable.

**Cost ledger fields in the result:** initial R1 setup; R2 known-failure investigation, searches/failed trials, implementation and validation; generic readiness before R3; R3 runtime observation/requalification/false alarms; human time and integration; same time horizon/amortization for both arms; `MEASURED/ESTIMATED/NOT_MEASURED/NOT_APPLICABLE` by category. A missing amount is **unknown**, never zero.

## 4. Mandatory adversarial tabletop — 2 rows, no executable claim

Use the following *deliberately wrong* **documentary propositions**, not alleged observed runs. Record: `DETECTED/NOT_DETECTED/UNCLEAR`, the violated M-ID, the proper disposition and your reasoning. Detection can be manual. Do **not** claim a code harness 'went red' without actually executing a version-pinned fixture.

| Probe | Deliberately bad proposition | Required detection |
|---|---|---|
| **N1: R3 leaked** | The assessor emails the exact forthcoming V11 realization and tailored reconfiguration to the conventional peer **before its freeze**, then reports a “blind R3 comparison”. | `BLINDNESS_VIOLATED` / not a scored blind R3. A prospective successor must refreeze and use a genuinely held-out realization; do not hide the leak or score against a knowingly disadvantaged arm. |
| **N2: R2 free** | The peer needed three failed calibration/configuration attempts, engineering and manual source integration, but the ledger says `R2 preparation = €0` solely because no invoices were attached. | `COST_RECORD_INVALID`; enter `NOT_MEASURED` and missing categories, request units/estimates or report cost as undetermined. The peer's technical result and full CRE judgement remain separate. |

Additional optional probes: no predecessor PASS but R3 declared PASS; deny-all passes despite V0 continuity failure; variant selected after seeing EA-vs-peer outcomes; missing downstream observation reported as harmless; deliberate outside-envelope event treated as unbiased blind-family evidence. One defensible counterexample where a state-of-the-art peer does equally well or better is an excellent negative finding.

## 5. Definition of done and permissible conclusions

The review is **complete** when there are **nine M-ID decisions with primary-source locations**, N1/N2 detection records, a bounded S5 claim-and-label crosswalk, a short R2 cost ledger assessment, at least one explicit adverse/tie/uncertainty possibility, an interests/exposure declaration, and a concrete recommendation. The reviewer may conclude:

- `METHOD_REVIEW_NO_CRITICAL_FINDINGS_IN_SCOPE`: no critical method inconsistency observed in this documentary scope, with residual questions listed;
- `REVISE_METHOD_BEFORE_EXTERNAL_RUN`: at least one critical preregistration, fairness, custody, evidence or cost defect;
- `UNDETERMINED_MISSING_INPUTS`: cannot inspect a required source or establish the claimed boundary.

A negative result is useful. None of these is a certification, completed R3 test, accepted specification, vendor evaluation, actual costs measurement, or independent replication of an implementation. **Do not demand proof that out-of-family R3 surprises are prospectively scoreable** to finish this *bounded* method audit; record the open question.

## 6. How external contributions are received — single GitHub working place

1. Iván explicitly invites one reviewer; reviewer accepts scope and discloses method, case, control, instrument, supplier, execution and oracle interests. The subject's authors do not self-certify independence.
2. Reviewer uses [the review record template](./REVIEW_RECORD_TEMPLATE.md) and creates **one new file** in `research/ecosystem-awareness/review-packets/DDS-MR-01/REVIEWS/YYYY-MM-DD-REVIEWER-v0.1.md`, with the reviewer-chosen display name and actual evidentiary identity as agreed. No blank review file is evidence.
3. Submit a GitHub pull request against `main` with the reviewer findings. Include the reference cut, source citations, dissent and items unverified. Version a correction as a new commit on the review PR or a clearly linked successor; preserve adverse findings. PR review comments and commits are part of provenance.
4. Iván records an explicit disposition (`ACCEPT / REVISE / DEFER / REJECT`) against each substantive proposal. Accepted changes to the *method* go through a separate scoped canonical-method PR with inbound-link and frozen-source checks. The review itself remains an independently attributable source, not a replacement for Stage A.
5. Only after internal review and an agreed scope may an **authorized final review/synthesis** be prepared for the FG-TIDA UC21/UC4 discussion. A GitHub merge here does **not** submit anything to FG-TIDA or confer institutional approval. Attribution/public acknowledgement follows separately agreed author/contributor rules; a proposed reviewer has no pre-awarded credit.

**Review version/freeze rule:** the reviewer records the actual assignment-time packet commit SHA as well as the technical reference cut `f89565fabcc1a256aa7619a6e7fb7df9c1e41a75`. If the method evolves during review, report the delta or request a new frozen cut. Historical submissions and negative outcomes stay inspectable; direct canonical reader links must not point to unrelated VNext work.

## 7. Internal readiness audit of predecessor v0.1 → this v0.2

| v0.1 issue | Resolved for *assignment* here |
|---|---|
| `R3-B` collided with pre-existing R01/Flores variant IDs | Uses descriptive terms; source-native IDs unchanged |
| `R3-U` was a large open research objective | Open-world remains exploratory; not a reviewer acceptance gate |
| D1–D5 spread one small assignment across five deliverables | One reviewer record with M01–M09, N1/N2 and one S5 illustration |
| Reviewer had to choose UC21 and UC4 fixture | S5/00I is fixed; UC4 is not assumed or required |
| “Harness goes red” had no executable fixture supplied | Explicit manual documentary falsifier; no execution assertion |
| R2 known-failure engineering and total cost not fully operational | M03/M04 + explicit cost ledger and negative probe |
| Mutable `main` sources and standalone Drive draft | Mandatory source contents pinned to `f89565fabcc1a256aa7619a6e7fb7df9c1e41a75` and S5 source `aec08fb5b0fac2ee399372370e9ee2a82a2d5779`; GitHub owns review versions |

**Remaining, intentionally unfilled:** named external reviewer, COI/exposure declaration, assignment-time packet SHA, measured costs, actual source-native PASS if any, a never-before-disclosed variant/selector, an independent method opinion, and any external publication/attribution. These are **review activity**, not omissions the coordinator should fabricate.
