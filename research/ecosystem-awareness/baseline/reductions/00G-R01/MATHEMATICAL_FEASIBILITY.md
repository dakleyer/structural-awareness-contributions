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

All tasks below are OPEN. Execute M01–M06 in order; M07–M09 are mandatory closure passes. Record owner, UTC date, input commit, assumptions, evidence paths, commands/results where applicable, disposition and remaining limitations. A plan or a desired result cannot close a proof task. Use OPEN, IN_PROGRESS, BLOCKED or DONE; explain blockers and the next action.

| ID | Stage and dependency | Evidence needed to close |
|---|---|---|
| M01 | Freeze scope and quantifiers. Read current R01 §§1.2–1.5, 2.13–2.18 and 00M §6.3. | Exact domain, policy class, probability law or worst-case criterion, thresholds and F/U definitions. Clarify empty regions and unresolved evidence. |
| M02 | Construct candidate hard and easy worlds after M01. | Full ground truth, observations, legitimate optimum including mixtures, and feasible control. Show why no common permitted high-quality shortcut already settles the hard pair. |
| M03 | Derive information and resource bounds after M02. | Argument covering every policy claimed, including randomization, adaptive review, cache, certificates, coordination and prior knowledge. Separate work from wall-clock delay. |
| M04 | Establish or reject a parameter region after M03. | Explicit inequalities, boundary/equality cases, scope and nonemptiness witness; justify any positive-measure claim. Retain an empty-region or failed-proof outcome. |
| M05 | Connect to executable witnesses with C02–C05. | Independent finite checks of the proposition's instances and a mapping to all relevant R01 assumptions. A fixture pass must not be called a universal proof. |
| M06 | Deepen sources and attack the proof adversarially. | Search and verify primary work on query/communication bounds for the chosen predicate; try sufficient summaries, dominant safe routes, pooling, learned information and cheap certificates. Record counterexamples and narrow or withdraw claims as needed. |
| M07 | Audit corpus and transfer coherence after M06. | Versioned correspondence to R01, 00M/00N, E1–E7 and the HF case; separate constructed extension, concrete technology and historical incident. No unsupported EA advantage. |
| M08 | Review editorial quality, readability and visual aids. | A reader can identify assumptions, claim, evidence and limits. If a region plot is added, distinguish proved, measured and unresolved areas; label conceptual figures and show axes/units. |
| M09 | Preserve and release after M01–M08. | Diff showing no unintended removal, valid links/anchors, preserved prior task IDs and results, scoped hash report, and final adversarial self-audit. Record unresolved package-audit issues; do not overwrite historical manifests. Obtain independent review separately before calling it independent. |

Next bot starts at M01. A negative finding changes the claim, not the evidence.
<!-- R01_BOT_WORKPLAN_END -->
