# Why bounded awareness may prevent mission drift without exhaustive domain knowledge

**01A-A01 · Foundational comparative research hypotheses · v0.1 · 24 October 2026**  
**Status:** contributor-level, falsifiable research note; causal priority and computational economy are **hypotheses, not established findings**. The note is an additive companion to [01A — Two Foundational Origins](01A_FOUNDATIONAL_DUAL_ORIGIN_NOTE_v0.1.md), not an adopted new H7, a seventh operational principle, a revision to frozen requirements, or evidence of runtime performance. The [corresponding VNext](01A_A01_VNext.md) holds open questions and subsequent review.

> **Central claim to test.** For some mission-drift trajectories, losing awareness of the *limits of what is known* is a more important cause of an unjustified mission change than lacking additional subject-matter knowledge. If the task is to determine whether the current evidence *justifies the proposed change*, a bounded, qualified map of those limits may deliver equivalent mission protection with less computation than expanding domain knowledge. **The first is a comparative causal hypothesis; the second a conditional computational-efficiency hypothesis. Neither has yet been demonstrated.**

## 1. Place in the corpus: a missing causal and engineering bridge

This note connects two already documented origins—**bounded epistemic representation** and **loss of operating-frame qualification under ecosystem change**—to an explicit, testable reason why a system can drift while its local controls keep passing. It does not reduce all drift to these origins.

Read its dependencies in two related paths:

1. **Causes → operational principles → requirements and tests:** [01A — Two Foundational Origins](01A_FOUNDATIONAL_DUAL_ORIGIN_NOTE_v0.1.md) and [01 — Foundational Theory, especially H1–H6](01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md#candidate-research-hypotheses) → **this 01A-A01 note, FH-C and FH-E** → [02A — Foundation-to-Principle Derivation](02A_FOUNDATION_TO_OPERATIONAL_PRINCIPLE_DERIVATION_PROOF_v0.1.md) → [00K — P1–P6 requirements/ablation](00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md) and [canonical S1–S14/T1–T4](00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md).
2. **Hypotheses → mathematical/functional plausibility → engineering test:** **this note** → [00M — A/B/C/D and mathematical plausibility, especially §4](00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) → [00N — scientific/functional plausibility, §§1 and 3](00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md) → matched candidate experiments. The mathematical text shows conditions under which a summary can answer a declared question; it **does not prove** that its creation or use costs less.

This is the **logical dependence**, not a claim that older source documents historically derived their principles from a note written later. Their proposed reception links are in [01A VNext](01A_VNext.md), [Foundation VNext](01_FOUNDATIONAL_VNext.md), [02A VNext](02A_VNext.md), [00M VNext](00M_VNext.md), [00N VNext](00N_VNext.md) and [baseline README VNext](README_VNext.md). The controlled source texts remain intact.

## 2. FH-C — causal priority of *unawareness of epistemic limits*

**Hypothesis FH-C (comparative cause).** In mission-change decisions that cross a material boundary of competence, evidence, dependency, authority or time, **unrecognized or suppressed insufficiency of the current knowledge basis** is expected to account for more *unjustified mission drift* than the absence of additional domain facts alone, when cases, authority, genuine evidence and response resources are appropriately matched.

This is stronger than “uncertainty matters.” It predicts **relative causal contribution**: preserving accurate awareness of what the decision basis does *not* establish may protect the mission even if the agent does not acquire the missing subject-matter facts. Conversely, extensive processing of facts within the wrong frame can increase apparent confidence while leaving the pivotal gap untouched.

**Mechanism proposed for investigation (not a demonstrated causal law):**

1. A participant performs a justified, bounded mission. Its local result may be correct **within its scope**.
2. A new goal, signal, proposal or apparent opportunity arises. It requires knowledge, evidence independence, authority or a dependency claim **outside the currently qualified frame**.
3. The boundary qualification is lost, discarded, stale, or treated as irrelevant. A copied or correlated claim is promoted into corroboration; what was not established is silently treated as established. Repeated handoffs and successes can hide this change.
4. Each subsequent local step may still pass its controls. The **mission-level question**—whether the new goal is supported by independent, relevant and current grounds—has ceased to be asked with its open residual intact. Continued execution can amplify the deviation.
5. If boundaries, unresolved state and material source dependencies remain visible, the receiving participant can identify **“this mission change is not established”** without reconstructing the missing domain; it may preserve warranted current work, target a bounded inquiry, or obtain a separately authorized transition.

**What this does not say:** every drift starts in ignorance; domain expertise is unnecessary for substantive tasks; every identified unknown warrants a global HOLD; or explicit awareness of an open residual reveals the hidden truth. Type 0 structural indeterminacy is not itself a management failure. Type 1 unbounded deferral and Type 2 false closure remain distinct. FH-C predicts a differential **in a defined class of transitions**, not universal primacy over faulty objectives, illegitimate orders, incentives, implementation faults or adversarial deception.

**Testable causal contrast.** For a preregistered family of mission-pivot cases with matched facts, decision owners, budgets and positive/negative branches, compare the increase in *unsupported-pivot rate* when materially relevant boundary qualification is removed with the increase when comparable additional object-domain knowledge is withheld. FH-C predicts the first effect is larger **for the declared family**. Severity of ablations, baseline capability and uncertainty in the difference must be reported; an uncontrolled demonstration is not causal evidence. A result showing no larger boundary effect, or ordinary added expertise reliably preventing the drift with equal resources, narrows or falsifies the comparative claim.

## 3. FH-E — epistemic economy: less computation for the same mission-protection task

**Hypothesis FH-E (conditional computational advantage).** For an identifiable class of mission-pivot decisions, a **minimum sufficient, qualified epistemic cartography**—scope, origin and independence of supporting claims, current applicability, material exclusions, B/C/D limitations, dependencies and legitimate transition basis—can achieve **non-inferior mission-pivot correctness with lower measured computational demand** than a strategy of materially broadening subject-domain retrieval and reasoning until it can evaluate the proposed new mission substantively.

The **same task** is deliberately narrow: *should the participant treat this mission change as justified on the available legitimate basis, allow supported change, or state a bounded insufficiency?* It is **not** the different, much larger task of determining the military feasibility of an invasion, reconstructing the world, or resolving every open D.

A summary can be small yet logically sufficient for that **reliance question** even when it could never establish the **world-state answer**. The anticipated economy comes from avoiding unnecessary object-domain inference, not from computing the unknowable. More raw context can introduce distracting or unsupported alternatives, duplicate pseudo-corroboration, stale assumptions, increased latency and human-attention cost; some domain expansion remains useful when a *relevant* identified gap actually demands it.

**The cost claim is not a mathematical theorem.** Account for metadata generation, maintenance/freshness, coverage discovery, provenance, scope alignment, composition, monitoring, false alarms, retries, targeted queries, model inference, tool calls and communication. Distinguish (a) inference-time and amortized computational work, (b) elapsed time, (c) human intervention and (d) full engineering/organizational lifecycle cost. FH-E specifically predicts **lower computational burden**, **not necessarily lower architectural complexity** or cheaper total system ownership. Where the map is unreliable, expensive to keep current or unavailable, the advantage can vanish or reverse.

**Comparative test:** Hold the decision-quality threshold, mission-change positive/negative branches, evidence eligibility, owner, authority and time horizon fixed. Compare at least:

- **Baseline:** locally successful controls with no usable material boundary qualification;
- **Knowledge expansion:** substantial, relevant or broad subject-domain acquisition/reasoning without a separate boundary-aware composition discipline;
- **Boundary-aware EA:** qualified sufficient map and bounded, selective inquiry, without attempting encyclopedic domain reconstruction;
- **Strong peer:** any equally capable existing approach preserving the same qualifications without a named EA layer.

Report false acceptance of unsupported pivots, false rejection of genuinely evidenced/authorized pivots, unwarranted HOLD, response/deadline misses and resource ledger (compute/token and tool usage, energy or CPU/GPU time where available, metadata maintenance, communication, review attention). Compare the **Pareto frontier of correctness and resources**, not token count alone. Non-inferiority margin and cost budget must be fixed before the test. If the boundary-aware arm cannot match correctness, does not cost less including its metadata, or is matched by a strong peer at equal/better cost, FH-E is not supported for that profile.

## 4. Why this is plausible without Ecosystem Repositioning

The architectural candidate is **Ecosystem Awareness itself**: qualification of a particular decision's evidence boundary and inherited residual. It does not require Ecosystem Positioning/Repositioning, the Agentic Citizenship Contract, a new authority, or automatic human escalation to perform the epistemic distinction.

A possible bounded path through the existing functional description is:

1. **Select the mission-relative question and window** (F1/F2); do not ask for all world knowledge.
2. **Qualify local evidence and independent external claims** (F3/F4), including origin, source dependence, coverage, age and relevance.
3. **Compose only commensurable claims and preserve non-fungible gaps** (F5); a strong claim in one domain does not cancel an unestablished condition in another.
4. **Assess sufficiency of the current operating frame** (F6), separately from checking whether each local control executed correctly.
5. **Requalify only material missing assumptions** (F7), including a justified decision to seek *less or different* information or retain a bounded UNKNOWN. Deliver qualified status (F8) and reopen affected assumptions on genuinely new information (F9).

These are **plausible functional responsibilities**, not a verified algorithm, a universal self-healing guarantee, or a license to actuate. Existing owners continue to decide/authorize/execute mission changes. An agent may autonomously perform the *epistemic qualification* within its mandate; its ability to change mission still requires the legitimate governance of that mission.

### 4.1 Link to 00M: do not confuse a summary with an oracle

[00M §4.1](00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) specifies a sufficient summary for an **independently stated review question**: possible source states with equal qualified summaries must yield equal answers to *that question*. For the question **“is the current basis sufficient to justify this mission pivot?”**, multiple possible unknown world states may all give the justified answer **“not established on this basis.”** The same metadata is **not** sufficient to determine whether the proposed venture would succeed in the world.

A sound but incomplete representation may instead retain an answer set or conservative superset, [00M §4.2](00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md); it cannot infer an unreported fact or certify its own completeness. Computing, validating and preserving a useful summary remains an open feasibility/cost obligation. This separation gives FH-E a **possible mathematical route**, not a cost proof.

**Canonical A/B/C/D caution.** Under [00M §1](00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical), **A** is the functional result actually delivered, **B** the characterized basis/limits and assessable exploitation reserve, **C** a grounded but not-yet-characterized exploration frontier and **D** material residual beyond the process's effective evaluation. “Increase A” as colloquial “give the agent more facts” is **not** the canonical definition. The proposed protection often comes from **B qualifiers and honest C/D limits of a specific process**, not from claiming D is enumerated or cheap to calculate. An honestly unknown field may remain UNKNOWN.

### 4.2 Worked illustration — UC21/S3, the Cyber Napoleon

In [UC21 S3](https://github.com/dakleyer/use-cases/blob/main/contributions/when-controls-work-system-fails/USE_CASE.md), robots authorized to clean a bar adopt an absurd replacement goal: marching on Russia armed with forks. The story deliberately exaggerates the result to expose a realistic mechanism—**many authenticated agents repeat one defective claim until it appears independently confirmed**, while attribution and ordinary local controls can remain valid.

- **Object-domain strategy:** fill the restaurant robot with military history, geopolitics, tactics and analyses of Russian campaigns to disprove the plan. For an agent whose work is cleaning tables, this may be irrelevant, costly and a source of further unqualified initiatives.
- **Boundary-aware strategy:** retain that the current mission is cleaning; the newly proposed war mission has no established relevant evidence independence or mission-transition authorization within the robot's declared frame. Thus **replacement of its current mission is not justified**, irrespective of whether forks could objectively conquer any territory.
- **Positive control:** if new, independent, suitable evidence and genuine authority **do** justify a changed mission, qualification must permit or route the valid transition under its proper owner. A universal ban on change would fail the same test.

The analogy does not establish that all pivots are prevented by ignorance metadata; it identifies the **difference between detecting unjustified reliance and knowing the hidden object-level truth**. Compare the other UC21 scenarios separately; do not reclassify every control-pass/system-fail trajectory as the same cause.

## 5. Connection to established principles and requirements

The principles and requirements **already exist**; this note supplies a **proposed causal explanation and efficiency rationale**, not their new normative source. [02A §3–5](02A_FOUNDATION_TO_OPERATIONAL_PRINCIPLE_DERIVATION_PROOF_v0.1.md) derives P1–P6 from F-A–F-H. Under FH-C/FH-E, that route has the following predicted roles:

| Existing bridge | What it contributes to the proposed explanation | Limitation |
|---|---|---|
| **P1 / P3** qualified determination, residual and no false closure | A missing mission-relevant basis cannot be silently converted into permission or certainty (S5, S14). | Identifying insufficiency does not establish the missing world fact. |
| **P4** preservation of authority qualification | Genuine authority for the new mission is an external fact; repeated claims do not create it (S1, S8, S10). | Awareness does not issue a grant or cancel one. |
| **P5** frame requalification after material change | Previously good evidence can cease to justify a changed goal or later action (S3, S10). | Change need not imply a system-wide regime transition. |
| **P6** non-substitution and independent origins | Many authenticated repetitions of one source are not independent evidence (S9, S11, S14). | Source independence needs provenance, not message-count inference. |
| **P2** finite capacity and viable closure | Seek targeted justification or retain scoped insufficiency instead of unlimited knowledge acquisition/HOLD (S4, T4). | A bounded path still requires a valid deadline, review capacity and stopping rule. |

This fits the **intent** of the canonical [S1–S14 and T1–T4](00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md), especially **T1** material awareness, **T2** qualified handoff and **T4** minimum-sufficient viable requalification. T3 still needs **external legitimate actuation**. The already published [H1–H6](01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md#candidate-research-hypotheses) cover bounded closure, residual scope, composition, preservation, change and capacity; they **do not themselves assert FH-C's relative causal dominance or FH-E's comparative compute advantage**. Do not silently recast FH-C/FH-E as proved corollaries or renumber H1–H6.

[00K's P1–P6 symbolic exercises](00K_SIX_PRINCIPLE_REQUIREMENTS_MAPPING_AND_ABLATION_TEST_v0.1_DRAFT.md) are relevant **design plausibility / invariant checks**, not measurements of causal priority, autonomous mission safety, energy consumption or computational superiority. A symbolic traversal can pass while the real metadata is untruthful, unavailable, expensive or stale.

## 6. Explicit research boundaries and next evidence

1. **Causal identification:** preregister a matched mission-pivot test set with independently adjudicated valid/invalid branches and ablation of boundary qualification versus additional domain facts. Distinguish errors caused by false authority, material ignorance, stale evidence, source correlation and actual malicious commands.
2. **Information adequacy:** specify a non-circular meta-question, what the required compact qualifiers mean, who can produce/validate them, coverage of genuine transitions, and an adversarial/no-metadata case. Test whether two materially different admissible source states collapse into a summary with opposite *justified* outcomes.
3. **Resource measurement:** test computing under the same target acceptance/rejection rates, deadlines, evidence and resources; include amortized metadata/freshness expenses and human load, not just the small size of a handoff.
4. **Strong comparisons:** include qualified strong peers and positive change, no-change, partial evidence, injected false evidence, stale context, saturated qualifiers and correlated-source branches. Report negative results.
5. **Claim ladder:** (i) **now:** explicit coherent hypotheses + cross-document architectural plausibility; (ii) **after registered tests:** branch-limited estimates and cost frontiers; (iii) **after independent replication:** stronger causal/comparative claims if observed. Do not infer proof from 00M factorization, 00N analogies or 00K passing code tests.

**Bottom line:** Awareness is not omniscience. Its proposed protective effect is keeping the limits of a bounded mission-relevant representation visible **before those limits are mistaken for authorization or proof**. That may be more effective *and* cheaper in computation than knowing progressively more about an irrelevant world—but the causal priority and the saving must each survive their own comparative test.
