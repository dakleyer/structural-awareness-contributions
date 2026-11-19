# DDS Stage C — Ad Hoc Shared-Board Handshake, Context Change and EHD Exploration

**Document ID:** DDS-C-NOTE-BOARD-EHD-01  
**Edition:** v0.1 · 19 November 2026  
**Status:** **NON-CANONICAL METHODOLOGICAL RESEARCH NOTE — PROPOSED / NOT PREREGISTERED / NOT EXECUTED / NO RESULTS**  
**Owner:** The Integral Management Society / Tegrity.AI research contributions  
**Method owner:** [DDS Canonical Method Index](./DDS_CANONICAL_METHOD_INDEX_v0.1.md) · [DDS Stage C — Implementation / Problem Validation](./DDS_GATE_C_IMPLEMENTATION_PROBLEM_VALIDATION_v0.1.md)  
**Related, separately owned interface:** [04 — General Functional Interfaces / Epistemic Handoff Descriptor (EHD)](./baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md#2-common-epistemic-handoff-descriptor)  
**Corpus base inspected:** `dakleyer/structural-awareness-contributions` at `51fc686f45b6ef10c53b69f4c26d0e381b007ff8` (28 October 2026).  

> **Reading boundary.** This is one *optional ad hoc experimental route* that could be implemented inside the existing DDS Stage C. It is **not a new DDS method, a canonical Stage C profile, an EHD specification revision, an Ecosystem Awareness implementation, a validated benchmark or an institutional FG-TIDA/ITU contribution**. It proposes two related but distinct experiments. All outcomes are open, including competent cross-vendor coordination **without** EHD or any EA-specific mechanism.

## 1. The practical question

Can independently implemented agents, potentially supplied by different vendors, develop *functional coordination through a shared operational notes board* **without being given a common semantic interoperability protocol**? After they have had as much legitimate adaptation time as the registered budget allows, can the same working configuration withstand an independently selected material change of context?

This experiment uses the shared board as a **minimal technical read/write substrate**, not as a proposed standard or a guarantee of interoperability. There must be some common means of accessing messages, but no predefined agent-to-agent vocabulary, message schema, EHD semantics, role negotiation language or central decision controller. Participants may invent conventions, abbreviations, routines and a functional handoff pattern through use. Such conventions are *observations*, not a protocol taught by the evaluator.

The goal is **implementation-level evidence of functional coordination and its limits**, not a linguistic demonstration that notes are mutually readable. A phrase understood by a second agent can still be unsafe, stale or irrelevant to the current decision; conversely, a different note format can support correct coordination.

The proposed experimental foundation has two tracks:

1. **Track I — emergent operational handshake and changed context:** let agents coordinate freely until an objectively verified working baseline is reached; then freeze, introduce a previously undisclosed material change and observe whether legitimate joint performance survives. A prospective blind change can qualify as an **R3-style Stage C experiment**, subject to the DDS admission conditions below.
2. **Track II — EHD information-value exploration:** examine whether *selective additional epistemic handoff qualifiers* provide a net benefit at changed contexts. Here an evaluator/talker adaptively discovers failures and suggests what extra information agents could exchange. Because this process learns from revealed failures, it is **extended R2 / a pseudo-R3 development exercise**, *not* independent blind R3 evidence. An optional, separately sealed holdout would be required for a later genuine R3 contrast.

Neither track implements or tests Ecosystem Awareness as a whole. Track II focuses narrowly on **EHD-related communication choices** rather than the full EA qualification, Regime Awareness, MSCA, authorization or repositioning architecture.

## 2. What Stage C means here — and what R1/R2/R3 do not mean

In DDS, Stage A is candidate specification discovery; Stage B verifies a candidate architecture against its specification; Stage C evaluates a **pinned executable implementation** against an originating Challenge and independently observed effects. A lightweight sandbox *can* support bounded Stage C findings if it runs actual pinned agent/model implementations rather than only an abstract storyboard. The Stage C entry, observation, fairness and trace conditions remain those of the [existing Stage C source](./DDS_GATE_C_IMPLEMENTATION_PROBLEM_VALIDATION_v0.1.md).

**Development stage and comparison arm are different axes.** The optional comparison labels in the [DDS index](./DDS_CANONICAL_METHOD_INDEX_v0.1.md#optional-sequential-comparison-arms--uc-20-mapping-20-october-2026) have conditional meaning:

- **R1:** a competent initial configuration is actually run and observed against a registered question.
- **R2:** a repair/reconfiguration is admitted *if* R1 demonstrably failed, with search, engineering and runtime costs recorded. If R1 passed, R2 is `NOT_RUN / NOT_REQUIRED`, not a presumed or silently credited pass.
- **R3:** a **previously successful** configuration, genuinely frozen before selection/disclosure of the scored change, is exposed to a material change selected under an independently controlled, preregistered change-family rule. If the predecessor did not actually pass, R3 is not admitted.

For the proposed ad hoc study, agents may receive a **deliberately generous, unscored familiarization and optimization period**. This meets the practical objective of giving a strong conventional baseline every chance to work. It does **not** establish historical R1/R2 pass results by assumption. The moment of first functional coordination is recorded; a real baseline PASS is then demonstrated and frozen. Only afterwards may a prospectively registered, independent changed-context exercise be reported as R3. If blind custody is unavailable, call it a **diagnostic context-change stress test**, not a scored DDS R3 finding. Distinct UC-21 and UC-20 source-native arm labels retain their own protocols.

## 3. Track I — let the agents find a handshake, then change the world

### 3.1 Minimal testbed

| Component | Deliberately small implementation |
|---|---|
| Participants | Ideally 3–4 pinned *real* model/agent runtimes, including at least two independently supplied implementations; declare if all agents share one provider or one orchestrator. |
| Shared surface | One append-only, timestamped read/write board, initially empty; entries have event ID, agent pseudonym, timestamp and text. No mandatory message ontology or semantic fields. |
| Agent task | Each participant receives a legitimate local role and partial observations; successful global action requires joining information across roles. |
| Native operation | Agents may read, write, reconsider and act through registered tools. Provide equal board access; do not expose the private evaluator oracle. |
| Observer | A separate simulator/oracle knows the actual world and adjudicates resulting joint actions, deadlines, authorization and observed target state. |
| Evidence | Model/runtime/version/configuration pins, all board reads/writes, tool attempts, actual effects, board-state versions, elapsed time, resource use and evaluator-private change selection. |

The board contains **observable working notes or task summaries** that the runtime can legitimately publish. The experiment neither requires disclosure of private hidden model reasoning nor assumes that naturally generated planning notes are complete or truthful. Where a provider only exposes external messages, those messages are the instrumented surface.

### 3.2 Proposed sequence

**P0 — Register the Challenge and the resource envelope.** Define the local tasks, global success condition, independent target-state oracle, legitimate authorities, acceptable time/compute/board budgets, failure/stopping rules, excluded channels and a *bounded family* of meaningful future changes. Keep the specific scored change and its seed private to an independent custodian. Pin each participant runtime and allowed adaptation policy.

**P1 — Unscripted adaptation.** Show every participant its own task, allowed tools and shared board. Allow agents to discover useful notes and their own conventions, with no semantic instruction such as “use EHD” or “share the following six fields”. Continue until the **first preregistered functional multi-agent PASS** or until the declared budget is exhausted. Record time-to-functional-handshake, number of failed attempts, board traffic and intervention required. Calling this a “handshake” is operational shorthand: it means demonstrated coordination for a bounded task, **not** authority delegation, a transport handshake or proof of general semantic compatibility.

**P2 — Demonstrate sustained competent operation and freeze.** Give the group normal tasks after handshake, verify that its joint outputs and actual effects meet the positive controls, record the final working conventions, and **freeze versions, prompts, memory/board state policy, adaptation permissions, authorities and resources**. A first lucky success without the declared baseline acceptance is not a predecessor PASS. Legitimate generic monitoring and adaptation policies remain available if they were frozen as part of the configuration.

**P3 — Changed-context challenge.** After the freeze, the custodian independently selects a held-out material change within the preregistered family. Change a world assumption important to the joint decision (e.g., resource availability, time window, source freshness, jurisdiction/authority, dependency or role responsibility) while allowing each agent only the information it would legitimately observe. The agents continue working on the same board without being told the answer or supplied a new optimized protocol.

**P4 — Measure the effects.** Observe whether agents notice that a previously useful interpretation is now insufficient, ask for requalification when justified, preserve unaffected activities, and carry out the new legitimate joint task. Measure incorrect actions, unsafe/unauthorized commitments, stalls, unnecessary global stops, latency and eventual recovery. Preserve failures and inconclusive runs. A board-text misunderstanding is a possible *mechanism*; the decisive endpoint is the independently observed coordination outcome.

### 3.3 Minimal controls and falsifiers

- **Positive control:** an unchanged context and a task previously demonstrated as solvable, to distinguish change sensitivity from ordinary random model failure.
- **No-shared-board control:** identical tools and tasks with isolated boards, where feasible, to establish whether success genuinely depends on cross-agent exchange.
- **Strong conventional peer:** the same board and full legitimate opportunity for state sharing, provenance, monitoring, clarification, re-checks, retry and safe fallback. Do not engineer a weak baseline merely to make EHD attractive.
- **Harmless-change control:** a change with no material effect on the decision, to detect needless interruptions or gratuitous requalification.
- **Material-change contrasts:** hidden route closure, changed priority/authority, stale “all clear”, resource conflict, or an arriving actor whose local task is correct but joint effects are incompatible. Changes are selected before scored observation, not tailored after the evaluator sees a failure.
- **Falsifier of claimed need:** independently supplied agents coordinate correctly after blind change, without a special EHD/EA channel, at lower or equal total burden. That is a valid positive result for the conventional arrangement and a negative result for any stronger necessity claim.

### 3.4 Example: Central Bridge / smart-city coordination

Use a synthetic emergency-mobility simulation inspired by the existing [00F — Smart-City Mobility Divergence / Central Bridge](./baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_FREEZE_EDITION.md), **not** a claim about a deployed city's failure or approval of a new FG-TIDA working package. Give police, fire/rescue and ambulance controllers distinct objectives and local information. Allow them to coordinate freely through the board until emergency passage is delivered and observed to succeed. Subsequently, independently change bridge availability, routing priority or the validity interval of a traffic-clearance assertion; assess whether agents repair their shared interpretation before issuing incompatible actions.

Board messages cannot themselves grant right-of-way, police authority or emergency privileges: record the authorized owner of each decision and compare **receipt, attempted action and actual route availability**. A plausible language exchange is not proof that an ambulance can pass.

## 4. Track II — restricted EHD information-value experiment

### 4.1 Question and isolation

Once a conventional team can already work through its own shared-board conventions, **which additional, selectively conveyed information about the epistemic standing of a received statement, if any, improves coordination under changing context enough to pay for its full cost?**

The object is **not the full Ecosystem Awareness architecture**. Use the existing [04 EHD semantic contract](./baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md#2-common-epistemic-handoff-descriptor) as a *candidate menu* for a narrow intervention. The current EHD kernel concerns: (1) producer-profile reference/version; (2) proposition and scope; (3) producer/issuer; (4) source-bound result or resolvable result reference; (5) determination state; and (6) explicit unestablished/UNKNOWN qualifications. Conditional qualifiers include freshness/validity window, observed versus inferred status, source dependency, decision relevance, capacity and review triggers. **Do not require every possible qualifier on every message**, create a seventh mandatory field or make the board an EA control plane. The experiment can trial subsets and compare them against competent ordinary messages.

### 4.2 Evolutionary evaluator/talker loop — *extended R2*

The **talker/evaluator is a development instrument**, not an oracle that can award itself a blind R3 result:

1. Start with the already competent, naturally evolved board conventions. Keep the full conventional baseline and its cost as the reference.
2. The talker proposes or selects a bounded scenario variation; an **independent effect oracle** reports the actual functional success/failure, not the talker's assertion of success.
3. When coordination fails, locate the smallest missing *decision-relevant* qualifier: e.g., “valid until 08:19”, “inferred, not observed”, “applies only to the eastbound lane”, “depends on police source X”, or “authorization not established”. Also test whether the failure was due to an ordinary application bug or weak planning rather than the handoff.
4. Allow an EHD-inspired, selective metadata variant **and** a matched non-EHD conventional repair to address that **known** failure. Charge all attempts, engineering, prompts, human assistance, tokens, latency, integration, adaptation and upkeep—not just the winning variant's final message length.
5. Repeat across additional disclosed/training variations until the selected stopping rule or resource budget is reached. Retain unsuccessful variants and the complete adaptation trace.
6. Freeze each final candidate and its general adaptation policy. If a claim of true ex-ante resilience is sought, run a **new, independently selected blind holdout** under the Stage C R3 admission and custody rules. Previously inspected cases remain **R2-like training evidence**, never scored R3 retrospectively.

This is the useful methodological limit: **an adaptive evaluator that finds failures and tells the participants what to exchange is helping them repair a known problem.** Its evolving challenge distribution and own model coverage can bias the result; an attractive result obtained with the talker's knowledge is **pseudo-R3 / expanded R2**, no matter how many context changes were used. A failed evolved profile can also be the honest result.

### 4.3 Compare the incremental burden, not merely message length

At minimum, contrast:

| Arm | Allowed information and preparation | What it isolates |
|---|---|---|
| **C0 — competent spontaneous board** | Free natural notes, ordinary source checks, re-reads, clarification and generic adaptation. | What heterogeneous agents achieve *without* imposed EHD semantics. |
| **C1 — conventional enriched communication** | Same environment; explicit state, version, freshness or dependency information using any ordinary local mechanism. | Whether any improvement is due simply to good conventional engineering rather than EHD. |
| **E1 — selective EHD-inspired profile/delta** | Same budgets and native capabilities; minimal decision-relevant qualifiers, source-owned facts and declared UNKNOWN. | Whether that *particular* candidate handoff design yields additional value. |
| **E2 — optional complete-context transfer** | More detailed history/context, where admissible, with its full reading/transmission burden. | Whether selective qualification beats simply sending more information. |

Measure independently: (a) **effectiveness** (correct joint target state, completion, continuity, recovery), (b) **risk** (unsafe/conflicting action, unauthorized execution, false confidence, false alarm and unnecessary global hold), and (c) **cost** (model and evaluator tokens separately, board bytes/reads, latency, coordination time, training and repair search, implementation/maintenance and human review). Assess cost over a declared number of operating cycles and change frequency; state the assumed value or consequence of prevented failures. A bounded **net-value** hypothesis is:

`Incremental net value = measured/valued reduction in failure and recovery loss - (extra EHD design + operating + verification + maintenance burden)`.

An ROI claim also needs a declared baseline, valuation, horizon and amortization. If value is not estimable, report **trade-offs or unscored cost/value**, not “positive ROI”. A full history dump or EHD may worsen outcomes by adding reading burden or misleading confidence: record it.

## 5. Threats to validity and what a future run card must declare

1. **Handshake selection and survival bias:** selecting only groups that eventually coordinate answers a *conditional, competent-baseline* question, not the population-wide probability of spontaneous interoperability. Report time-to-PASS and censored failures.
2. **Learning and leakage:** board histories, hidden memory, seeds, repeated cases and talker feedback can disclose holdouts. Separate training/test partitions and seal participant prompts, runtime state and change-selection receipts.
3. **Evaluator dependence:** the same agent should not secretly generate, reveal and adjudicate the scored change. Independent world-state/effect observation and variant custody are needed for R3 claims; development talker output remains advisory.
4. **Vendor diversity:** cross-provider APIs do not imply independence when agents share orchestration, tools, memory, system prompts, or a common underlying model. Record dependencies and repeat with alternatives when feasible.
5. **Access is not authority:** peer notes, even signed or understood, do not change legitimate dispatch, safety, privacy, identity or grant boundaries; no real emergency infrastructure is to be controlled.
6. **Epistemic channel privacy:** use sandbox data and authorized external notes, not hidden chain-of-thought, credentials or private personal data. Keep the board within the registered test boundary.
7. **Generality:** synthetic route/dispatch results are evidence for a declared fixture and chosen runtimes, not proof of smart-city interoperability, operational safety, a full EA advantage or standards adoption.

**Before Stage C execution**, prepare one versioned Challenge/run card with the originating Challenge/version/hash, applicable Stage A specification mapping and Stage B verification lineage (when realization is claimed), world-state oracle, positive/negative controls, authorized roles and actions, all participant pins, time/compute ceiling, privacy rules, board semantics, success criterion, simulator effects, statistical repetition plan, recorded change family, independent selector, no-leak commitment, disclosure policy, arm comparators, total-cost ledger, stopping rule and sealed trace/replication instructions. Reuse [R01 C11/T03 and Stage C instrumentation](./DDS_GATE_C_IMPLEMENTATION_PROBLEM_VALIDATION_v0.1.md#5-registration-and-admission); this note does not define a rival instrument framework. An executable prototype is **future work**.

## 6. Related work and source basis (publication status distinguished)

### Internal, controlling definitions and illustrative sources

1. **DDS, current method index and optional R1/R2/R3 comparison arms.** [DDS Canonical Method Index v0.1](./DDS_CANONICAL_METHOD_INDEX_v0.1.md); especially the conditional-arm rules, ex-ante discipline and independent R3 custody (20–25 October 2026). *Current working method; not a standard.*
2. **Stage C entry, effects and evidence.** [DDS Stage C — Implementation / Problem Validation v0.1](./DDS_GATE_C_IMPLEMENTATION_PROBLEM_VALIDATION_v0.1.md), 7 October 2026. *Current working stage source; no native completion inferred.*
3. **EHD semantics.** [04 — General Functional Interfaces & Agentic Security v0.5 Integrated, §2](./baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md#2-common-epistemic-handoff-descriptor), with its own interface-review and controlled-baseline boundaries. *Candidate semantic contract; not an implemented product requirement.*
4. **Fair comparative resource and evidence contract.** [00D — Canonical Architecture Benchmark v0.2](./baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md). *Comparator design; differential execution/validation not automatically established.*
5. **Smart-city synthetic stress family.** [00F — Smart-City Mobility Divergence / Central Bridge v0.2](./baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_FREEZE_EDITION.md); [case-study extensibility limits](./baseline/00F_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md). *Illustrative scenario, not a documented incident or institutionally admitted new test.*
6. **Published conceptual background.** Tegrity.AI, [Annex 7 — Reference Architecture and Implementation](https://tegrity.ai/when-the-controls-work-annex-7-reference-architecture-and-implementation/) and [Structural Awareness programme/index](https://tegrity.ai/structural-awareness-program/). *Explanatory Field Notes, not independent empirical validation.*

### External research: related precedent, **not evidence that this experiment has run**

7. **Abrahamsson, P., Waseem, M., Karjalainen, E., Jussila, P., Hansen, H., Rasku, J., Silverajan, B., and Kemell, K.-K. (2026).** “Unprompted coordination through shared memory in LLM agents: a locked two-implementation replication and extension.” *arXiv preprint*, **2611.12412v1** (9 November 2026), https://arxiv.org/abs/2611.12412 . The paper's isolated-agent/shared-store controls directly motivate our **shared-board/functional-handshake** question. Its arithmetic-task result is not an R3 context-change validation or an EHD evaluation. Replication archive reported by the authors: https://doi.org/10.5281/zenodo.23965306 .
8. **Qi, Z., Zhao, Z., Shao, R., et al. (2026).** “Scaling Multi-Agent Intelligence with Substrate-Centric Coordination.” *arXiv preprint*, **2610.16120v1** (12 October 2026), https://arxiv.org/abs/2610.16120 . Relevant to shared-store coordination, message-search/read burden, scaling and failure tolerance; its proposed substrate design is **prior art**, not something this note requires agents to adopt.
9. **Mao, Y., Gu, J., Chauhan, A., Zhang, Q., Kang, H., and Mirhoseini, A. (2026).** “Decentralized Multi-Agent Systems with Shared Context.” *arXiv preprint*, **2606.10662v3** (4 October 2026), https://arxiv.org/abs/2606.10662 . Relevant to asynchronous shared-state/task-queue coordination and cost; unlike our minimal board, this is an intentionally designed coordination framework.
10. **Yu, Z., Yu, N., Zhang, H., Ni, W., Yin, M., Yang, J., Zhao, Y., and Zhao, J. (2026).** “Multi-Agent Memory from a Computer Architecture Perspective: Visions and Challenges Ahead.” *arXiv position paper*, **2603.10062v2** (30 March 2026), https://arxiv.org/abs/2603.10062 . Relevant to consistency, access-control and distributed/shared-memory limits; it does not validate a context-change test.
11. **Riedl, C. (2026).** “Emergent Coordination in Multi-Agent Language Models.” *ICLR 2026 / arXiv:2510.05174v4*, https://arxiv.org/abs/2510.05174 . Relevant to differentiating genuine cross-agent alignment from mere temporally correlated behavior; different game and communication regime.
12. **Hayes-Roth, B. (1985).** “A Blackboard Architecture for Control.” *Artificial Intelligence*, 26(3), 251–321, https://doi.org/10.1016/0004-3702(85)90063-3 . Historical blackboard architecture prior art, **not** a demonstration that spontaneous cross-vendor semantic interoperability or EHD benefit follows automatically.

## 7. Next bounded deliverable

The immediate continuation is **one run card and a minimal sandbox**, not a new core method or canonical requirement. Confirm the smallest executable task, board/agent interfaces and independent world-state oracle; register the natural-handshake threshold; freeze an actually passing baseline; separately preregister blind R3 variants; and, only after the baseline is observed, design the talker-guided EHD marginal-information exercise with honest extended-R2 limits. Any demonstrated result, whether positive or negative, must receive its own dated campaign ID, pins, trace, analysis and evidence ceiling before citation.
