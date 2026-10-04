# R01 — Mathematical extension protocol by technology mechanisms

Documentary version 0.3 · 4 October 2026 · M13 in development.
Single base: [R01 mathematical validation v0.2](./R01_CONDITIONED_TRILEMMA_THEOREM.md).
Reviewed precedent: [consistency of the three extensions](./EXTENSION_CONSISTENCY_REVIEW.md).
First mathematical application: [human escalation with whispering](./HUMAN_ESCALATION_WHISPERING.md).

## 1. What is compared

Fix problem x: task, mandate, worlds and their law, sufficient quality, evaluation horizon, actual violation and accounting rule. Declare technology t and complete manifest θ_t=θ(x,t). Admissible strategies are Π(θ_t), without access to the evaluator's private state.

The accepted region remains:

$$
\mathcal A_{b,\delta,p}=\{(c,r,s):c\le b,\ r\le\delta,\ s\ge p\}.
$$

The attainable set is F_t(x)={(c(π),r(π),s(π)):π∈Π(θ_t)}. It is not the accepted region. The scenario admits acceptance when F_t(x)∩A is nonempty. Technology comparisons keep b,δ,p fixed; changes in B, latency, initial information, price or capabilities are declared.

For problem domain D, define Acc_t={x∈D:∃π, performance_t(π)∈A}. A recovered scenario belongs to Acc_t\Acc_0. Resolving all D requires Acc_t=D. Failure to prove impossibility does not prove acceptance.

The task is not changed to present an improvement: authorizing a previously forbidden action or accepting lower quality changes x or acceptance policies. This may be studied but is recorded separately.

## 2. Step one: identify the isomorphic kernel

First provide a table of objects, relations, events, observations, authority, charges, latency and outcomes. Calling the correspondence an isomorphism requires [E1–E7](../extensions/family/KERNEL_AND_PROOF.md#41-obligaciones-e1e7), including optimum and quality threshold.

| Correspondence type | Required proof | Available conclusion |
|---|---|---|
| Reversible representation or unit change | Bijection of kernel, events/views/laws/outcomes and normalization of budgets and deadlines. | Equal normalized performance for the same scenario. |
| Correspondence with effective parameters θ* | E1–E7 relative to θ*, with its prices, radius, network and resources. | Preservation relative to θ*, not θ_0. |
| One-way simulation | For every destination strategy, an observable base strategy with useful inequalities. | Transfer of impossibility or a bound in the proved direction; not isomorphism. |
| Analogy | Proposed table without proof of relations and dynamics. | Motivation and pending obligations. |

A message renaming evidence may be representation. A message arriving earlier because of reduced latency corresponds to a different parameter. A new certificate distinguishing previously indistinguishable worlds is additional information. These three cases are kept separate.

## 3. Step two: inventory additional mechanisms

Each mechanism receives a separate profile:

1. Concrete operation, who can invoke it and what observation it produces before or after the effect.
2. Information source; producer, scope, recipient, version and validity.
3. Transition change: veto, pause, resumption, recovery or confined effect.
4. Work, money if used, latency, queue and maintenance; evidence production and consumption price.
5. Interactions and maximum budgets; what remains the same task.
6. Verifiable hypotheses and exact modification of I1, I2 or I3.
7. Bound for every strategy of the contract, attainable control or an undetermined result.

“Human escalation” or a framework name is insufficient. The human may use the same information, acquire new facts, provide legitimate authority or arrive after the effect. These capabilities induce different scenarios.

Composition is studied after the profiles: detector–pause–human–broadcast interaction may be decisive even when no isolated component suffices. Merely observing the combination does not attribute a benefit to one component.

## 4. Step three: transfer impossibility in the correct direction

**Transfer proposition.** For every π_t∈Π(θ_t), suppose an observable strategy Φ(π_t) exists in base scenario M with coupled worlds and

$$
c_M(\Phi\pi_t)\le c_t(\pi_t),\qquad
r_M(\Phi\pi_t)\le r_t(\pi_t),\qquad
s_M(\Phi\pi_t)\ge s_t(\pi_t).
$$

If M admits no strategy in the accepted region at the compared thresholds, neither does θ_t.

**Proof.** By the three inequalities, an accepted strategy of θ_t would induce an accepted strategy of M, contradicting base impossibility. ∎

The inequalities permit a more powerful relaxation for proving the lower bound. They must preserve the definition of success and violations across the entire campaign. A projection omitting a superior alternative can change J* and break the inequality for s.

Attainability uses a different direction: implement an abstract strategy in θ_t and bound its actual charges, times, effects and quality. This control does not require a bijection of all strategies. Nor does the isolated control transfer impossibility.

## 5. Step four: prove acceptance movements

An optional mechanism with avoidable cost preserves previous strategies: Acc_0⊆Acc_t if it can reproduce them with equal information, resources and outcomes. This inclusion requires a concrete simulation. Adding mandatory review with overhead can lose scenarios through budget or deadline.

Strict improvement requires a nonempty set R⊆D such that:

- An all-policy bound proves x∉Acc_0 for every x∈R.
- A legal construction proves x∈Acc_t for every x∈R.
- Full cost and time fit the same b,T.

An exact frontier formula requires necessity and controls for every announced point. A better strategy provides an attainable point or upper bound; it does not by itself establish the optimal frontier.

The technology need not recover every scenario. Distinguish proved recovery, proved absence of recovery, loss through cost/deadline and undetermined cases.

## 6. Step five: persistence of the conditioned trilemma

Persistence is proved over technology class C defined by capabilities and prices:

$$
\forall t\in C\ \exists \Theta_t\ne\varnothing\
\forall\theta\in\Theta_t:
\Bigl[\exists\pi_{CR},\pi_{CE},\pi_{RE}\Bigr]\land
\Bigl[\neg\exists\pi\in\Pi(\theta): (c,r,s)\in\mathcal A\Bigr].
$$

Each pair's controls use the same scenario thresholds. If CE is already impossible, this nonvacuous three-pair trilemma has not been established.

For classes only processing/communicating acquired facts, simulation through collective history applies the parity bound when necessary producer work remains outside b. Additional information requires recalculating the posterior or mass of resolved histories. Barriers require separate proof of whether they preserve efficacy and at what cost.

**There is no universal law that every technology leaves an unreachable region.** A perfect affordable prior oracle selecting a sufficient legitimate route, with search, execution and deadline also affordable throughout D, can yield Acc_t=D. A perfectly safe barrier alone guarantees only absence of violations; efficacy or resources may remain unresolved. Absence of the three-pair trilemma likewise does not imply acceptance of every scenario.

## 7. Step six: proof, oracle, harness and campaign

| Stage | Deliverable | What it verifies |
|---|---|---|
| Mathematical proof | Contract, quantifiers, lemmas, bounds and controls. | Every strategy of the contract under explicit hypotheses. Does not require executing Python. |
| Evaluation oracle | World and optimum calculated by an independent method; adjudication of effects, quality and charges. | What actually happened in an episode. Its private state does not reach the agent or human. |
| Test harness | Executes strategies/adapters, clock, queue, messages, interruptions and recorder against the environment. | Operational compliance of interfaces and measurements. May initially use a simulator. |
| Campaign | Scenarios, versions, seeds, resources, comparators and analysis registered before execution. | Empirical performance, uncertainty, robustness and limits of transfer to real systems. |

An **evaluation** oracle is not the **solving oracle offered to the agent** in §6. The first adjudicates privately; the second changes capabilities and must be charged as technology.

A harness does not turn finite sampling into universal proof. Running a real technology helps test its assumptions and empirical usefulness without definitively proving a theorem for infinitely many configurations. Formal program verification can provide a further universal result within a specification, with its own scope.

Archived scripts may inspire controls and tests for the future harness. Their parameters do not calibrate the product and their outputs are not technology campaigns.

<a id="technologies-to-study"></a>
## 8. Technologies to study and work order

The first profile is human escalation with whispering. The review order remains: isomorphic correspondence; information mechanism; pause mechanism; human mechanism; dissemination and concurrency; composition; frontiers; evaluation protocol. Obligations are not skipped because of the technology's name.

### 8.1 Technology registry

**Human escalation and whispering is the first concrete technology of this protocol**, comprising detection, direct notification by any agent, group dissemination, human intervention and execution coordination. Its existing profile contains mathematical results for the contract; checking implementation membership belongs to the pending technology review.

| Order | Technology | Existing work | Pending within this extension |
|---|---|---|---|
| 1 | [Human escalation and whispering](./HUMAN_ESCALATION_WHISPERING.md) | H0/H1 and studies H2–H4; proposed kernel and additional mechanisms separated. | General explanation and virtual R1/R2/R3 incorporated. Verify E1–E7 of the actual realization, calibrate sources/cost/deadline and extend to other candidates. |
| 2 | LangGraph | Previously registered candidate; received pause/resumption and state analysis. | Apply the same profile to a pinned version; pausing one graph does not establish a collective barrier. |
| 3 | OpenAI Agents SDK | Previously registered candidate; received approval, guardrails, handoffs and trace analysis. | Review kernel and additional mechanisms against sources for the selected version; do not turn the received annex into admission. |
| 4 | smolagents | Previously registered candidate; received tool, callback and plan-review analysis. | Apply the same profile; preserve execution surfaces and native controls. |

The last three are candidate frameworks, not already validated technologies. Their historical documentation and original criteria remain in the [preserved registry](../extensions/hugging-face/REMAINING_TASKS.txt). This order permits successive review; it does not rank performance or schedule three simultaneous implementations.

### 8.2 Virtual traversals of technology extensions

For each candidate, the presentation follows this sequence: explain and justify **why it could help generally**, check the isomorphic kernel, separate additional mechanisms, and traverse R1/R2/R3 as the contract's final virtual examination. This precedes the harness and real technology.

- **R1:** competent reference with ordinary controls, alternatives and quality, without adding the mechanism under study.
- **R2:** same problem and thresholds, declared mechanism and quality plan, including detection, evidence, intervention, effects, continuity, cost and deadline.
- **R3:** same frozen R2, changed environmental condition and no subsequent repair; retain positive controls for legitimate change and authorized continuity.

The 00G/00H traversal structure is reused without confusing a traversal with an experimental arm. Passing R1/R2/R3 supports the scope covered by the traversal; resolving all configurations additionally requires quantified proof, not three examples. Failure of one controller does not establish impossibility for all strategies. The [first profile](./HUMAN_ESCALATION_WHISPERING.md#virtual-traversals) provides both layers: virtual controls and all-policy bounds for R1 and R3-A; R2 recovers scenarios under the same acceptance budget.

The first profile also makes explicit the recognition/escalation chain, human availability and comprehension, admissible intervention and corrected reentry. R3 examines full cost, stopping incompatible with the mission and restarting without sufficient evidence. A kill switch is not automatically legitimate; restart does not erase charges, deadline, alerts or past violations. Every candidate checks positive continuation, not just the order to stop.

### 8.3 Partial preparation annexes

[Rehearsal inventory](./partial-experiments/README.md) · [Received originals, executions and counterexamples](./partial-experiments/received/2026-10-04/README.md).

| Material | Permitted use in profiles | Status |
|---|---|---|
| Received Annex T | Mechanism leads for the three frameworks and proposals X1–X14. | Partial design annex; claims to verify, without canonical admission. |
| testA_budget.py | Budget and mixture exercises. | Preliminary rehearsal; general formula challenged. |
| testB_oracles.py | Query and noise exercises. | Preliminary rehearsal; does not cover the entire policy class. |
| testC_killswitch.py | Containment and canary exercises. | Preliminary rehearsal; does not erase past violations. |
| testD_human_and_sharing.py | Human cost and sharing exercises. | Preliminary rehearsal; does not execute humans, whispering or an actual collective barrier. |

These annexes remain subordinate to protocol profiles. Their results are preserved but create no new task queues and replace neither proofs nor real campaigns.

| Work tracked at the end | Status |
|---|---|
| Previous review of the three extensions | Completed as the author's review. |
| Protocol | Defined; do not schedule its creation again. |
| First technology | Human escalation and whispering; continue its existing profile. |
| Other technologies | Candidates registered for successive mechanism review. |
| Oracle / harness / campaign | Later stages; no real implementation validated by this cleanup. |
| Tasks | [Single queue](./WORKPLAN.md): M13, M16, M17 and P08; previous rehearsals remain partial annexes. |
