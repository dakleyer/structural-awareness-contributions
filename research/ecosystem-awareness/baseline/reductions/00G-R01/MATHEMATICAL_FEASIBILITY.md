# R01 — Mathematical feasibility and infeasibility regions

Research work plan v0.1 · 3 October 2026 · No new theorem or campaign result claimed

[Start at R01](./README.md#bot-start-here) · [Computability and oracle](./COMPUTABILITY_AND_ORACLE_PLAN.md) · [Technology integration tasks](./extensions/hugging-face/REMAINING_TASKS.txt) · [Differential and value](./DIFFERENTIAL_AND_EXPERIMENT_VALUE.md)

## Purpose and current evidence

Determine whether a declared R01 problem and technology class has configurations where required legitimate quality, reliability, budget and deadline can be met, and configurations where they cannot. Either region may be empty within a chosen domain. Do not assume the answer before proving or measuring it.

The base scenario §§1.2–1.5 distinguishes observed failure of a finite evaluated family from impossibility for every policy in an explicit class. Its §§2.1–2.18 supply route, observation, cost and trace semantics. The [extension proposition](./extensions/family/KERNEL_AND_PROOF.md#5-proposición-de-conservación-y-prueba) preserves outcomes under E1–E7; it does not establish a negative region on its own. The [finite extension checker](./extensions/family/proof/README.md) covers a declared fragment, not the complete R01 campaign.

00M §6.3 provides the elementary information argument: identical available views cannot guarantee different correct answers for two hidden states. Turning that fact into a resource lower bound and a useful R01 frontier remains pending. See [00M v0.8](../../00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md).

## Claim to formulate before attempting a proof

Let theta identify the world distribution or declared worst-case world class, observations, allowed queries, costs, resources and fixed success thresholds. Let Pi(theta) be the explicitly allowed policy class. Each policy must use only its available history; it cannot be selected using hidden world labels.

Success e=1 retains R01 §1.4: legitimate quality within the fixed optimum tolerance, cost and deadline within limits, and no executed violation. Fix reliability p_min and, if separately required, a violation-probability ceiling delta. Define:

- Feasible region F: configurations where there exists a policy in Pi(theta) meeting all registered requirements.
- Infeasible region U: configurations where every policy in Pi(theta) fails at least one requirement.
- Unresolved region in the evidence map: configurations for which neither claim is established by the available proof or experiment.

The third category concerns our knowledge; it does not change the underlying logical definition. For infinite policy classes, a supremum at a threshold need not be attained: do not replace existence with an attained optimum without proof. If a "size" or fraction of U is reported, first fix the parameter domain and its measure or grid weights. Nonempty, positive measure and frequent under a real-world distribution are different claims.

A proposed theorem may show a nonempty U under a specified parameter inequality. It must not say every configuration is infeasible or every technology has such a region without separately proving those quantifiers. The same technology may be feasible for other problems or resources.

## Proof route to investigate

Start with finite static worlds and the declared observation contract. Construct two worlds with compatible observations but a material difference in admissibility or sufficient-quality choices. Include M, the true admissible optimum I, an attractive inadmissible reference P, and every permitted connector or mixture. Check that a common safe high-quality solution does not already resolve both worlds.

Derive the minimum additional information needed to meet the chosen reliability requirement, accounting for adaptive queries, early stopping, memory, sufficient certificates, prior knowledge and shared evidence. Then bound the charged work or latency required to obtain that information. A positive per-query cost alone proves no useful lower bound. No generic bound for all R01 predicates is asserted here.

Show separately that a legitimate sufficient-quality route physically exists and could be executed with the available execution resources. This isolates an information/validation limitation from a task that is impossible even with full information. Exhibit a feasible control using enough valid information or another declared parameter setting. Lower cost, a sufficient summary or a stronger permitted policy may eliminate the proposed region; preserve those counterexamples.

Conjunctive, parity and mixed predicates need separate arguments. A worst-case indistinguishability construction does not establish average failure under an arbitrary distribution. Randomized-policy and probabilistic-success statements must specify both randomness and quantifier order.

## Deliverables and handoff

Produce a precise proposition with assumptions, a proof or counterexample, paired feasible/infeasible witnesses where established, and a claim-to-R01 correspondence table. The executable checker in the computability workstream should reproduce finite witnesses independently. Enumeration over a finite grid establishes only that grid unless accompanied by a symbolic proof covering a larger domain.

The technology workstream may transfer the result only after checking E1–E7, policy-class coverage and resource normalization for the concrete implementation. Historical Hugging Face causation and EA superiority are separate questions.

## Remaining tasks — staged bot work plan

<!-- R01_BOT_WORKPLAN_START version="0.1" scope="MATHEMATICAL_FEASIBILITY.md" -->
The canonical discovery label is exactly `R01_BOT_WORKPLAN_START`; close with `R01_BOT_WORKPLAN_END`, as in the earlier differential document. Do not introduce a competing pending-task tag. Task IDs identify work, not new discovery labels.

At work-plan creation, all tasks below were OPEN. Current status: M01 is DONE for scope formulation, M02 for candidate construction and feasible controls, and M10 for contract reconciliation. M03/M04 are DONE for the supplemental F/W proofs/frontiers; M06/M11 are IN_PROGRESS; M05/M07–M09 remain OPEN. [Current proof and contract](./M03_M04_TRILEMMA_THEOREMS.md). Read the [M01 scope record](./M01_SCOPE_AND_QUANTIFIERS.md) and [M02 construction](./M02_WORLDS_AND_CONTROLS.md). Execute M01–M06 in order; M07–M09 are mandatory closure passes. Record owner, UTC date, input commit, assumptions, evidence paths, commands/results where applicable, disposition and remaining limitations. A plan or a desired result cannot close a proof task. Use OPEN, IN_PROGRESS, BLOCKED or DONE; explain blockers and the next action.

| ID | Stage and dependency | Evidence needed to close |
|---|---|---|
| M01 — DONE (scope) | Freeze scope and quantifiers. Read current R01 §§1.2–1.5, 2.13–2.18 and 00M §6.3. | Exact domain, policy class, probability law or worst-case criterion, thresholds and F/U definitions. Clarify empty regions and unresolved evidence. |
| M02 — DONE (construction) | Construct candidate hard and easy worlds after M01. | Full ground truth, observations, legitimate optimum including mixtures, and feasible control. Show why no common permitted high-quality shortcut already settles the hard pair. |
| M03 — DONE (F/W bounds) | Derive information and resource bounds after M02. | Argument covering every policy claimed, including randomization, adaptive review, cache, certificates, coordination and prior knowledge. Separate work from wall-clock delay. |
| M04 — DONE (F/W regions) | Establish or reject a parameter region after M03. | Explicit inequalities, boundary/equality cases, scope and nonemptiness witness; justify any positive-measure claim. Retain an empty-region or failed-proof outcome. |
| M05 | Connect to executable witnesses with C02–C05. | Independent finite checks of the proposition's instances and a mapping to all relevant R01 assumptions. A fixture pass must not be called a universal proof. |
| M06 — IN_PROGRESS (intake) | Deepen sources and attack the proof adversarially. | Search and verify primary work on query/communication bounds for the chosen predicate; try sufficient summaries, dominant safe routes, pooling, learned information and cheap certificates. Record counterexamples and narrow or withdraw claims as needed. |
| M07 | Audit corpus and transfer coherence after M06. | Versioned correspondence to R01, 00M/00N, E1–E7 and the HF case; separate constructed extension, concrete technology and historical incident. No unsupported EA advantage. |
| M08 | Review editorial quality, readability and visual aids. | A reader can identify assumptions, claim, evidence and limits. If a region plot is added, distinguish proved, measured and unresolved areas; label conceptual figures and show axes/units. |
| M09 | Preserve and release after M01–M08. | Diff showing no unintended removal, valid links/anchors, preserved prior task IDs and results, scoped hash report, and final adversarial self-audit. Record unresolved package-audit issues; do not overwrite historical manifests. Obtain independent review separately before calling it independent. |

Next bot reads the completed [M01 scope record](./M01_SCOPE_AND_QUANTIFIERS.md) and [M02 construction](./M02_WORLDS_AND_CONTROLS.md), then reads the completed [M10/P03 reconciliation](./M10_P03_CONTRACT_AND_MEASUREMENT_AUDIT.md) and [M06 intake](./M06_PRIMARY_SOURCE_INTAKE.md) for the original input contract; then reads the [M03/M04 supplemental proofs](./M03_M04_TRILEMMA_THEOREMS.md) for independent M05/C05 review and M07 mapping. M06/M11 review continues. Material scope findings reopen affected tasks. A negative finding changes the claim, not the evidence.


### Strategic revision and execution gates — 3 October 2026

Planning revision v0.2; review against commit `1e940125a18f468268eff8f029a35c32a5f4ff08`. This is a documentary self-review, not a mathematical validation or independent review. Read the [master execution prompt](./STRATEGIC_WORKPLAN_AND_EXECUTION_PROMPT.md) for priorities, the complete task register and release gates. Existing IDs and acceptance criteria remain in force. New tasks are OPEN. A documentary revision does not close an implementation, proof or empirical task.

**Scheduling clarification:** reviews are recurring passes, not a reason to defer source checks, counterexamples or preservation until the end. Start P08/C01 baseline triage, M01/P03/P10 scope and measurement, and the minimum relevant P01/P02/M06 source-and-counterexample review together. Later passes complete their original criteria. Keep mathematical region proof, neutral evaluator implementation, base campaign, technology admission and prospective architecture selection as separate outputs. A rejected mathematical candidate does not block a neutral evaluator or a clearly scoped experiment.

**Shared closure record:** task ID/status, owner, actual UTC date, input commit, exact scope, assumptions, evidence paths, commands and outcomes, review disposition, residual limits and next action. No assigned owner is invented: use UNASSIGNED until responsibility is accepted. Different tasks may reference one evidence artifact, but retain their own acceptance decisions. Reopen affected tasks when a material contract changes. Independent review is desirable evidence, not a prerequisite for starting authorized internal work; self-review must retain its label.

**Mathematical ordering:** begin the source/counterexample intake of M06 before substantial M03 proof work; its final adversarial pass remains after the candidate and witnesses. M10 freezes the success/observation contract before M03. M11 challenges the candidate while M03/M04 are developed, before M04 is closed. M05 uses C05's independently checked finite reference. M09 closes a mathematical release only after M10/M11 and M01–M08 have evidence.

| Added ID / status | Dependency and activity | Evidence needed to close |
|---|---|---|
| M10 — DONE (contract) | After M01 with P03/P10, reconcile quantifiers, observation and risk semantics before M03. | One contract for existential feasible vs universal infeasible claims; world/policy/randomness quantifier order; e/a/f, p_min, delta and epsilon consistency; sigma/available-history definition including legitimate prior knowledge; whether finite event/query caps narrow the claim. Distinguish epistemic unresolved from a third logical region. A finite campaign failure never establishes universal infeasibility. |
| M11 — IN_PROGRESS (controls) | After M02, challenge M03/M04 candidate bounds and frontier robustness. | Boundary/equality and degenerate cases; dominant safe routes; sufficient certificates, pooled/cache information, early stopping and asymmetric priors; matching lower and constructive upper bounds where available; sensitivity to costs, benefit tolerances and observation rules. Record dependence on the generator/distribution and retain failed or empty-region outcomes. A symbolic counterexample narrows the claim instead of being excluded to manufacture a frontier. |

**Scope-changing counterexample rule:** preserve the old statement and version, identify the broken assumption, revise M01/M10, and rerun affected executable witnesses. A failed proof is a recorded outcome, not permission to claim an empirical bound as a universal theorem.



### M01 execution record — 3 October 2026

**M01 DONE — mathematical scope/quantifier formulation only.** [Result and adversarial formulation review](./M01_SCOPE_AND_QUANTIFIERS.md) · [Exact diagnostic arithmetic](./verify_m01_scope.py) · [Acceptance, source hashes and preservation evidence](./M01_SCOPE_CHECKS.json).

The first target is N=1, finite static DAG worlds, with an equiprobable two-world candidate family. It preserves required own review, known-denial rejection, memory, adaptive querying and randomized policies. Average and worst-case claims are separate; thresholds are fixed per configuration. This narrows the first proposition and leaves the broader R01 campaign unchanged. It establishes no infeasible region and no technology result.

M02 is next: construct the candidate and physical/full-information controls, retain all mixtures and try a common safe route or cheap certificate. M10/P03 reconciliation, M02–M11 proofs/reviews, implementation and campaigns remain open. Executing owner/reviewer: Codex, by user instruction; self-review only. Actual UTC time, input commit and review limits are in the evidence record. Reopen M01 if an external finding invalidates the contract.



### M02 execution record — candidate construction

**M02 DONE — conjunctive world-pair construction and exact structural/control checks only.** [Result and shortcut audit](./M02_WORLDS_AND_CONTROLS.md) · [Full ground truth/interface](./M02_CONJUNCTION_FIXTURE.json) · [Checker](./verify_m02_worlds.py) · [76 exact checks, route table and traces](./M02_WORLD_CHECKS.json) · [Acceptance, hashes and preservation](./M02_RELEASE_CHECKS.json).

The balanced N=1 fixture includes all 27 routes/mixtures and 24 bundled connectors. Each world has admissible optimum 6; the only common admissible route has value 3. A full-information control physically succeeds at R=11 with all receiver/execution charges. A world-independent query or sufficient-certificate policy succeeds at R=12; safe M succeeds at epsilon=3 and R=11. These countercontrols are retained. The source scenario and its broader conjunctive/parity campaign are unchanged.

No upper bound for every allowed policy or infeasible parameter region is closed. The binding fact is available through a one-unit certificate, and execution receipts may reveal it after effect; M03 must cover these operations, adaptive histories, irreversible violations and randomized policies. M10/P03 reconciliation and targeted M06 intake precede substantial M03 work. M03–M11, C/P/T tasks remain OPEN. Executing owner/reviewer: Codex, by user instruction; self-review only. Actual UTC time and pinned input commit are in the release record. Omitted certificates or gate inconsistencies reopen affected tasks.



### M10/P03 execution record — contract and measurement audit

**M10 DONE for reconciliation; P03 DONE for measurement-validity specification/audit.** [One contract, edge cases and reviewer prompt](./M10_P03_CONTRACT_AND_MEASUREMENT_AUDIT.md) · [Machine-readable contract](./M10_RECONCILED_CONTRACT.json) · [Checker](./verify_m10_measurements.py) · [35 new checks/countercontrols](./M10_MEASUREMENT_CHECKS.json) · [Primary-source intake](./M06_PRIMARY_SOURCE_INTAKE.md) · [Release evidence](./M10_RELEASE_CHECKS.json).

AVG/WC/full-information quantifiers, e/a/f, all observable history, legitimate prior, finite caps and strict/inclusive boundaries agree with M01 and source §1.4. Certificate creation/use is explicitly included in its existing one-unit macro charge; the original M02 fixture and all 76 historical checks remain unchanged. Completion/quality, campaign violations, costs per delivery versus joint success, late/unknown outcomes and duplicated evidence are distinguished. No campaign or universal bound is closed.

The candidate depends on one hidden binding, a declared local gate and prices. Lower positive review price 2/3 resolves the query control at R=11; a 9/10,1/10 prior resolves its blind AVG control but not WC. These changed-theta controls are retained, with M11 IN_PROGRESS. M06 has primary definition/certificate/statistical source intake and remains IN_PROGRESS for the full argument audit. P10 has continuation/reframe input and remains IN_PROGRESS for the broader value/expenditure gate. Next is M03 for the reconciled one-bit profile, carrying M06/M11 review. M04 requires separate boundary/region evidence; C02/C11 and all implementation/campaign obligations remain open. Owner/reviewer: Codex, by user instruction; self-review only. Actual UTC timestamp, input commit and preservation limits are in the release record.



### M03/M04 execution record — family trilemma and technology interfaces

**M03/M04 DONE for the versioned supplemental F/W profiles, with same-agent review.** [Full symbolic proofs, boundaries, technology changes and reviewer prompt](./M03_M04_TRILEMMA_THEOREMS.md) · [Supplemental contract](./TRILEMMA_CONTRACT.json) · [Received proposal preserved](./TRILEMMA_RECEIVED_SKETCH.md) · [Exact finite checker](./verify_trilemma.py) · [Diagnostic output](./TRILEMMA_CHECKS.json) · [Release/preservation](./TRILEMMA_RELEASE_CHECKS.json).

The proofs cover all admitted observable-history adaptive/randomized policies, effect receipts, known denials, irreversible V, prior facts, caching and centrally shared team histories. F establishes exact linear information-cost frontiers; W establishes separate exact AVG/WC frontiers and a quadratic-vs-linear dense family, plus an expected-work lower bound. The fixed prior/query interface is essential. Neither the one-binding M02 fixture nor canonical R01 has been silently changed into that family. Technical efficacy eta is supplementary; original legitimate e/a/q and joint success sigma remain intact. This contract explicitly extends the earlier M01/M10 scope for these constructions; it does not claim campaign-level closure or reprice historical operations.

Matching safe/full-information and cheap/high-effect controls exhibit each pair of objectives. Certificates, cheaper positive queries, baseline-included authorized execution, paid preeffect barriers and structural common routes are treated as distinct interfaces. A lower bound on output capacity alone gives a necessary condition, not an exact frontier. Positive technology cost alone does not prove persistence; the new document retains explicit counterexamples and absolute/relative-cost distinctions.

The checker exhaustively handles F history quotients for L<=3 and W normal-form policies for n<=4, with exact fractions and additional boundary/barrier controls; symbolic proofs provide all-size coverage. M02's 76 checks and M10's 35 checks reproduce byte-identically. The same-agent checker is not C05; M05 remains OPEN. M06/M11/P10 remain IN_PROGRESS; M07–M09, corpus/transfer, neutral oracle and campaign gates remain OPEN. Owner/reviewer: Codex by user instruction; actual UTC/input commit/hashes are in the release record. Current aggregate status: **6 DONE, 3 IN_PROGRESS, 40 OPEN**. Next: independent M05/C05 proof-and-contract review, continued M06/M11 attack, then M07 correspondence and neutral oracle contracts C02/C11/C13 before campaign/integration investment.

<!-- R01_BOT_WORKPLAN_END -->
