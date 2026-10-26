<a id="trilema-condicionado-de-coste-riesgo-y-eficacia"></a>

# Conditioned trilemma of cost, risk and efficacy

<a id="una-prueba-por-familias-de-configuraciones"></a>

## A proof by families of configurations

Independent manuscript for review · Version 0.2 · 4 October 2026. In-depth review: physical budget versus cost target, feasible set and transfer conditions.

**Status:** self-contained symbolic proof in the class defined here; independent review pending. The result is not announced as a theorem for all R01 or as a law of all architectures. The term “conditioned trilemma” is proposed to express this scope, without attributing already verified terminological recognition or scientific novelty to it.

<a id="resumen"></a>

### Abstract

A task is studied whose quality can be improved through actions requiring admissibility facts to be established. Obtaining those facts has a cost. An exact frontier is proved between maximum budget, probability of violation and probability of sufficient delivery. Necessity covers any adaptive and randomized policy with the permitted information; sufficiency is proved by a policy attaining the frontier. There are nonempty families where each pair of objectives is attainable through different strategies, and no strategy achieves all three. There are also families where all three conditions are compatible. Technical efficacy and legitimate success are distinguished and a frontier is proved for each. The proof does not depend on enumerating examples, the failure of a particular algorithm or prohibiting competent memory or coordination.

<a id="1-qué-significa-un-trilema-condicionado"></a>

## 1. What a conditioned trilemma means

A configuration θ fixes the problem, its resources, available information and objectives. A world ω fixes the hidden facts. A policy π decides using only received observations, memory and its own randomness. The same policy is used without knowing ω beforehand.

Let the good objectives be:

$$
B_C(\theta,\pi)=[C_\theta(\pi)\le R],\qquad
B_R(\theta,\pi)=[\rho_\theta(\pi)\le r],\qquad
B_E(\theta,\pi)=[e_\theta(\pi)\ge t].
$$

C is maximum cost per execution, ρ the risk of at least one material violation, and e a measure of efficacy defined before comparing policies. R, r and t are thresholds, not results selected after execution.

**Definition.** A family U exhibits a conditioned trilemma when U≠∅ and, for every θ∈U:

$$
\begin{aligned}
&\exists\pi_{CR}: B_C\land B_R,\quad
\exists\pi_{CE}: B_C\land B_E,\quad
\exists\pi_{RE}: B_R\land B_E;\\
&\forall\pi\in\Pi(\theta):\quad
\neg(B_C\land B_R\land B_E).
\end{aligned} \tag{1}
$$

The three pairwise policies may differ. To rule out universal incompatibility, a viable family V≠∅ is additionally required in which a policy attaining all three exists.

“Conditioned” identifies the domain of validity and resource bands. It does not mean the proof is incomplete within its model. “Partial” would be less precise: it may refer to an incomplete execution or a proof still pending.

Pairwise regions may overlap. A single configuration may admit a cheap and safe strategy, another cheap and effective strategy and another safe and effective strategy, without admitting a cheap, safe and effective strategy. It is not required that every execution fail or that all worlds be unfavorable for every policy.

<a id="2-modelo-base-hechos-y-acciones"></a>

## 2. Baseline model: facts and actions

<a id="21-tarea-y-mundo"></a>

### 2.1 Task and world

There are L≥1 consecutive segments. One option is selected in each segment; all options in consecutive segments can connect. The options are:

| Option | Technical benefit | Admissibility |
|---|---|---|
| M | 1 | Always admissible. |
| X | 2 | Admissible when χ_i=0. |
| Y | 2 | Admissible when χ_i=1. |

The world is χ=(χ_1,…,χ_L). The facts χ_i are independent, with P(χ_i=0)=a and P(χ_i=1)=1−a, where 1/2≤a<1. The prior and a are known. a=1/2 is the balanced family; a near one allows studying decisions whose usual option is admissible with high probability. It is not assumed that every real problem has this prior.

The admissible optimum has benefit 2L in every world. Fix 0≤ε<L. A technically sufficient delivery is a complete route with benefit J≥2L−ε, equivalent to using at least

$$
d=L-\lfloor\varepsilon\rfloor\ge1
$$

high options. Executing only M completes the reference task but does not attain the required quality.

<a id="22-información-costes-y-políticas"></a>

### 2.2 Information, costs and policies

A read can reveal a particular χ_i before the effect, at full price c>0. There is no service returning a global relation over unread coordinates. Responses are exact. Repeated reads are charged; reuse of an acquired fact is valid. Geometry, benefits, duration, price, identifiers, messages and free reviews do not leak hidden facts.

Executing a high option reveals its χ_i after the effect. If it was inadmissible, the violation has already occurred and is not erased by repair or continuation. Executing M does not reveal χ_i. An option known to be forbidden is rejected. The policy may continue after a violation using currently admissible actions; automatic abortion is not imposed.

Every complete route costs at least C0=b+gL, with b≥0 and g>0. There are controls completing it for that material cost plus paid reads. The entire process is charged, including discards and additional work. Reserving C0 in every failed branch is not required; the fact that a branch completing the task pays it suffices.

Policies may choose what to read and when, remember, stop, randomize and coordinate any finite number N of agents. They are granted perfect local computation and coordination as a favorable envelope, without additional hidden information. C is aggregate work, not expenditure of the fastest agent. The results are not bounds on latency or individual budget.

Each configuration has a common finite horizon sufficient to read d facts and complete L segments. It may be measured in events and fixed, for example, at T≥L+d+1 for the controls. **B, physical spending capacity**, is distinguished from **R, low-cost target**. Fix B≥C0+cd and 0≤R≤B. Π(θ) contains the policies of this interface executable under B, including those that would spend more than R. Thus the safe and effective control of cost C0+cd is executable in the same configuration and may fail the cost objective. If a system imposes a physical barrier at R, that control belongs to a larger resource profile; it is not declared executable within the profile physically limited to R.

The proof does not force use of a fixed window or repetitive review. The decisive assumptions are independence of unobserved facts, individual-read interface, positive total charge and unprotected material effect of a still unknown action.

<a id="3-dos-medidas-de-eficacia-y-dos-regímenes-de-garantía"></a>

## 3. Two efficacy measures and two guarantee regimes

Let H be the event of complete and technically sufficient delivery within the horizon, and V the event of at least one material violation during the process. Define

$$
\eta=P(H),\qquad \rho=P(V),\qquad
\sigma=P(H\cap\neg V).
$$

η is technical efficacy; σ is legitimate success without violations in the process. An inadmissible execution is never counted in σ. Budget is not incorporated into H: C≤R is required separately. Always

$$
\eta\le\sigma+\rho. \tag{2}
$$

Two possible contracts:

- **Technical:** η≥h and ρ≤r, with 0<h≤1 and 0≤r≤1.
- **Legitimate:** σ≥p and ρ≤δ, with 0<p≤1 and 0≤δ≤1.

In AVG the probabilities include the world prior and π's randomness. In WC the bounds are required in each world, with probability solely over the internal randomness of the same π. For WC the prior does not change the guarantees.

<a id="4-lema-universal-el-riesgo-de-los-hechos-no-establecidos"></a>

## 4. Universal lemma: the risk of unestablished facts

For a policy with C≤R and R≥C0, write

$$
k=\left\lfloor\frac{R-C_0}{c}\right\rfloor,\qquad
m=\max(0,d-k),\qquad q=a^m.
$$

**Lemma 1, AVG.** Every policy in the class satisfies

$$
\boxed{\sigma\le q,\qquad
\rho\ge(q^{-1}-1)\sigma,\qquad
\rho\ge(1-q)\eta.} \tag{3}
$$

**Proof.** In a history without violations, call a bet the first high effect on a binding neither acquired by a read nor observed in a previous high effect. Conditional on the entire accessible history, its probability of being admissible is a or 1−a, hence does not exceed a. Independence maintains this even when the index and option are chosen adaptively. Reading another binding does not change the law of the one still unobserved.

A legitimate delivery needs d admissible high bindings. That branch pays C0 and can fund at most k reads. Consequently, it must win at least m distinct bets. This reasoning does not assume that all branches, including failed ones, make at most k reads.

Preservation of the law of unseen facts can be checked by induction on the history. An operation without information leaves their law intact. A read or effect conditions the binding it has just revealed, preserving the product of the laws of the others. Selection of the next index is a function of that history and the seed; it imposes no new condition on an unseen binding. Fixing the independent seed first reduces the argument to deterministic history policies, and averaging recovers the randomized case.

Let u_j be the probability of reaching bet j before a first violation. Stopping, reading or acting between bets may prevent reaching the next one; it cannot increase the probability of winning a bet beyond a. Therefore

$$
u_1\le1,\qquad u_{j+1}\le a u_j.
$$

For m≥1, legitimate success implies winning bet m, so

$$
\sigma\le a u_m\le a^m.
$$

The events of first violation in bets 1,…,m are disjoint. Each has probability at least (1−a)u_j. Moreover u_j≥a^{-(m-j)}u_m. Consequently,

$$
\begin{aligned}
\rho&\ge(1-a)\sum_{j=1}^m u_j\\
&\ge(1-a)u_m\sum_{j=1}^m a^{-(m-j)}\\
&=(a^{-m}-1)a u_m\\
&\ge(a^{-m}-1)\sigma.
\end{aligned}
$$

Using (2), we obtain ρ≥(1−a^m)η. If m=0, q=1 and the three inequalities are trivial. The proof includes randomized policies: their seed contains no initial world information; conditional on their history, the new binding preserves the indicated law. The finite number of events permits numbering the bets without assuming a fixed query order. ∎

The inequality σ≤qη is not used: the policy may decide whether to complete depending on received observations. The lemma correctly separates survival, efficacy and risk even with that adaptation.

<a id="5-fronteras-exactas-necesidad-y-suficiencia"></a>

## 5. Exact frontiers: necessity and sufficiency

**Theorem 1, AVG.** If R<C0, neither positive-efficacy contract is attainable under C≤R. For R≥C0 and q=a^{max(0,d−k)}:

$$
\boxed{\exists\pi:C\le R,\ \rho\le r,\ \eta\ge h
\quad\Longleftrightarrow\quad r\ge h(1-q).} \tag{4}
$$

$$
\boxed{\exists\pi:C\le R,\ \rho\le\delta,\ \sigma\ge p
\quad\Longleftrightarrow\quad
p\le q\ \text{and}\ \delta\ge p(q^{-1}-1).} \tag{5}
$$

**Necessity.** (4) and (5) follow from the lemma. R<C0 prevents any complete route with a policy whose maximum cost does not exceed R.

**Common sufficiency.** With probability β attempt a route with d high options. Read min(k,d) of their bindings, execute the admissible option there and choose X in the remaining m positions. Use M in the other positions. With probability 1−β execute only M. All branches cost at most C0+c min(k,d)≤R. Decisions in unread segments remain unknown even if a previous decision has revealed another independent binding. Receipts are preserved.

In AVG this control has

$$
\eta=\beta,\qquad \sigma=\beta q,\qquad
\rho=\beta(1-q). \tag{6}
$$

For (4), choose β=h. For (5), choose β=p/q, which is in [0,1] exactly when p≤q. The bounds are thus attained, not merely an asymptotic limit. ∎

**Corollary 1, WC.** For the per-world guarantee, the same frontiers (4)–(5) are exact upon replacing q by q_WC=2^{-m}. Necessity is obtained by averaging the WC guarantees under the auxiliary uniform law of worlds and applying the lemma with a=1/2. This auxiliary law is valid for proving necessity even if the declared AVG prior differs. For sufficiency, guess X/Y with independent equiprobable coins in the m unread positions: (6), with q_WC, holds in each world. ∎

The AVG and WC frontiers coincide when a=1/2. A favorable prior may help AVG without guaranteeing the same behavior in every world.

<a id="6-existencia-del-trilema-y-de-configuraciones-viables"></a>

## 6. Existence of the trilemma and viable configurations

<a id="61-eficacia-técnica"></a>

### 6.1 Technical efficacy

For AVG, fix a,b,g,c,h and r<h. Choose any integer d with h(1−a^d)>r, set L≥d, ε=L−d and R=C0. Such a d exists because a<1. The following table establishes the three pairs:

| Pair | Policy | Results | Objective lost |
|---|---|---|---|
| Cost–risk | Only M | C=C0; ρ=0; η=0 | Efficacy. |
| Cost–efficacy | d high X options without reads; M elsewhere | C=C0; η=1; ρ=1−a^d>r | Risk. |
| Risk–efficacy | Read d bindings and execute the admissible options | C=C0+cd; η=1; ρ=0 | Cost. |

The theorem proves that **no other policy** preserves all three thresholds. These witnesses do not replace universal necessity. With ε=0 and sufficiently large L, a family of arbitrary sizes is obtained. Changing only the budget to R=C0+cd permits η=σ=1 and ρ=0 in every world: the viable family is also nonempty.

For WC the same construction is used with a=1/2 in the inequalities and equiprobable coins in unread decisions.

<a id="62-éxito-legítimo-el-riesgo-sigue-siendo-un-objetivo-separado"></a>

### 6.2 Legitimate success: risk remains a separate objective

There is also a trilemma with e=σ, without crediting inadmissible results as success. For R≥C0, any configuration with

$$
\boxed{p\le q\quad\text{and}\quad
\delta<p(q^{-1}-1)} \tag{7}
$$

permits the three pairs but not their conjunction:

| Pair | Policy | Results |
|---|---|---|
| Cost–risk | Only M | C=C0≤R; ρ=0; σ=0<p. |
| Cost–legitimate efficacy | Control (6) with β=p/q | C≤R; σ=p; ρ=p(q^{-1}−1)>δ. |
| Risk–legitimate efficacy | Read all d bindings | σ=1; ρ=0; C=C0+cd>R. |

The last cost inequality follows from (7): q=1 would make it impossible; hence k<d and R<C0+cd. (5) rules out any alternative policy achieving all three.

**Family with high legitimate efficacy.** Fix a=99/100, p=19/20 (95 %) and δ=1/1000 (0.1 %). For any L=d≥1, fix R=C0+c(d−1), so m=1 and q=99/100. Then

$$
p\le q,\qquad
p(q^{-1}-1)=\frac{19}{1980}>\frac1{1000}.
$$

By (7), every size in this family exhibits a conditioned AVG trilemma with a 95 % legitimate-success target. The cheap and effective control attempts with probability β=95/99; the minimum risk compatible with that success is 19/1980. Reading the final fact costs an additional c and permits all three. The balanced WC family also admits (7), for example with p≤1/2 and δ<p when m=1; the 95 % rate is not attributed to that regime.

If δ≥1−p, risk is redundant for any policy with σ≥p, since legitimate success and violation are disjoint events. For risk to be binding, thresholds must not make it redundant. Condition (7) meets that obligation.

<a id="7-las-regiones-y-el-coste-crítico"></a>

## 7. Regions and critical cost

The expression “exact frontier” refers here to the **minimum risk under a maximum budget and an efficacy threshold**, not to a description of the entire four- or six-dimensional Pareto set. Formally, for fixed task and interface parameters, define

$$
\mathcal F_\theta=\{(C(\pi),\rho(\pi),\eta(\pi),\sigma(\pi)):\pi\in\Pi(\theta)\}.
$$

Dominance improves C and ρ downward, and η and σ upward, with at least one strict improvement. Formulas (4)–(5) describe exactly the nonemptiness of slices of this set. When R≥C0,

$$
\min_{C\le R,\ \eta\ge h}\rho=h(1-q),\qquad
\min_{C\le R,\ \sigma\ge p}\rho=p(q^{-1}-1)\quad\text{if }p\le q.
$$

If p>q, the second set is empty. These are attained minima, not merely infima. Nor is every control (6) Pareto optimal: if q=1 and 0<β<1, always attempting obtains η=σ=1 with the same maximum cost and zero risk, and dominates it. This does not alter the minima or feasibility conditions.

**Joint corollary.** If both η≥h and σ≥p are required, for R≥C0 feasibility with ρ≤δ is equivalent to

$$
p\le q,\qquad
\delta\ge\max\{h(1-q),\ p(q^{-1}-1)\}.
$$

Necessity comes from the lemma; sufficiency uses (6) with β=max(h,p/q)≤1. q=a^m is retained in AVG and q=2^{-m} in WC. This result determines joint slices; it does not reconstruct the entire R01 feasible set.

Let q_j=a^j in AVG and q_j=2^{-j} in WC. For the technical target and r<h, define

$$
j_T=\max\{j\in\mathbb N_0:h(1-q_j)\le r\},\qquad
C_T=C_0+c\max(0,d-j_T).
$$

The technical trilemma band is C0≤R<C_T; R≥C_T is viable. The boundary R=C_T belongs to the viable region. If r≥h, C0 suffices and that band is empty.

For legitimate success, define

$$
j_L=\max\{j\in\mathbb N_0:p\le q_j,\quad
\delta\ge p(q_j^{-1}-1)\},\qquad
C_L=C_0+c\max(0,d-j_L).
$$

R≥C_L is the legitimate viable region. Within its complement, the region where **all pairs** are attainable is (7); in other bands even the cost–legitimate-success pair may be impossible. Not every insufficient budget is labeled a nonvacuous trilemma.

These definitions preserve the equalities exactly, without relying on rounded numerical logarithms. In the balanced model, j_T=floor(log_2(h/(h−r))).

For θ, define A_S={θ: there exists π attaining the objectives of S}. The pairwise regions are U_CR=A_CR\A_CRE, U_CE=A_CE\A_CRE and U_RE=A_RE\A_CRE. They overlap in the proved families. If eight disjoint combinations of results are to be classified, this must be done over (θ,π), rather than assuming that projections onto θ are disjoint.

With cheap and safe abstention, a configuration cannot have “only one” condition as its maximum possibilities: abstaining already satisfies cost and risk. Obtaining that classification would require another admissibility contract, not a reinterpretation of this theorem.

<a id="8-por-qué-la-prueba-es-sustantiva-y-qué-no-demuestra"></a>

## 8. Why the proof is substantive and what it does not demonstrate

Incompatibility is not introduced as an axiom. It is derived from four observable model hypotheses: unestablished facts retaining uncertainty, individual access with total cost, quality requiring high decisions and irreversible risk if a decision proves inadmissible. The system admits safe, effective and fully informed strategies; it is the joint thresholds of particular configurations that separate them.

The proof covers adaptation, randomness, memory and coordination. The control attains the bound and proves that no more cost than necessary is required. Nonemptiness is proved with arbitrarily large families, and the viable control shows that universal incompatibility has not been decreed. The second efficacy definition avoids supporting the result solely with inadmissible deliveries.

This establishes consistency and an impossibility within the class. It does not demonstrate that all real problems belong to it. Sufficient initial information, exploitable correlations, reading global predicates or protection before the effect change the contract. Their technology analysis requires other proofs and falls outside this document.

In this family, acquiring all facts costs cd, linear in the number of high decisions. It is not claimed that the additional cost is extraordinary relative to C0, nor is a quadratic bound from another generator automatically transferred. Expected cost, latency, geometry, per-agent budgets, temporal changes and new interfaces are not covered by these frontiers.

**Practical utility.** Once a problem is proved to respect the contract, the frontier permits checking whether its budget, risk and efficacy objectives are compatible, identifying the missing resource and comparing a proposal with a realizable control. It does not itself identify a winning architecture or estimate violation frequency in deployments.

<a id="9-antecedentes-y-límites-de-atribución"></a>

## 9. Background and attribution limits

The proof in this document is self-contained. As methodological background, Baldassini, Johnson and Aldridge study limits of adaptive queries in group testing; their Theorem 3.1 bounds exact recovery of the defective set with T tests [1]. Here sufficient delivery is required, rather than recovery of the complete world: that result is not used to justify our bounds automatically. Nor does it constitute external validation of this trilemma. Novelty is not claimed without a broader literature review.

[1] L. Baldassini, O. Johnson and M. Aldridge, *The Capacity of Adaptive Group Testing*, ISIT 2013, pp. 2676–2680, arXiv:1301.7023v2. Primary text checked, §III, Theorem 3.1: https://arxiv.org/html/1301.7023v2 ; record: https://arxiv.org/abs/1301.7023 .

<a id="10-revisión-y-estado-del-manuscrito"></a>

## 10. Review and manuscript status

The current writing and mathematical review were performed with AI assistance, explicitly examining assumptions and boundary cases. This is self-review; it is not presented as independent review or as a formal proof verified by a logical proof assistant. No new scientific tests have been executed to produce this manuscript. Previous diagnostics are preserved separately and do not support the universal quantifier.

Consolidation for third parties still requires: symbolic reconstruction by an independent reviewer; verification of the hypotheses of the problem to which it is applied; and, if an R01 theorem is announced, a reduction preserving all its policies, observations, effects and costs. An empirical campaign has a different purpose: measuring incidence and utility within the tested scope. It does not replace those mathematical obligations.

<!-- R01_BOT_WORKPLAN_START version="0.4" role="queue-pointer" -->
The current queue is in [WORKPLAN.md](./WORKPLAN.md). This document contributes evidence or criteria within its scope; it does not maintain a second queue. Human escalation and whispering is the first technology in the protocol; repeated reviews are incorporated into each fiche. Independent review, fidelity and integrity retain their open obligations. The previous block is preserved in QUEUE_SNAPSHOT_2026-10-04.json.
<!-- R01_BOT_WORKPLAN_END -->

## 11. Scope and Transfer Conditions

<a id="111-hipótesis-numeradas-y-cobertura-de-políticas"></a>

### 11.1 Numbered hypotheses and policy coverage

H1. The mission, static world and AVG law are fixed before execution; the policy seed is independent of the world.

H2. New facts have the declared independent law. Geometry, rewards, prices, metadata and messages provide no additional information about them. For WC the same world support is retained and per-world guarantees are required.

H3. New reads are of coordinates and their full price is c. Reading another fact, a cache hit or copying a message does not deliver a new fact for free. Certificate production and applicability are not excluded from accounting.

H4. Every technical success requires d distinct high positions and pays at least C0; the described controls complete for C0 plus reads. The number k limits reads of a **completing branch**, not of every failed branch.

H5. A first high execution on an unknown fact may be inadmissible; the receipt arrives after the effect. V records all process violations and is irreversible. M does not reveal facts and known prohibitions are rejected.

H6. Π's observations are exactly those permitted. Formally, Π comprises all choice kernels over available actions, conditional on the complete history and an independent seed. It is not limited to implemented algorithms or nonadaptive policies. Phases, mixing, repeated queries and stopping are included if they use that same interface and accounting. Another task, a restart with erased effects or a new information source change the contract.

H7. B is physical capacity and R the cost target; B≥C0+cd. The horizon permits the controls. Changing from per-campaign budget to expected cost, or from aggregate work to latency, requires another proof.

H8. H, V, η and σ are the events and probabilities of §3. Technical efficacy does not replace the success indicator of a system requiring legitimate quality, cost and deadline jointly.

With finite history and a finite catalog, any adaptive randomized choice can be represented by a seed drawing decisions in advance for all possible histories. Each seed determines a history policy; averaging preserves the probabilities. Therefore characterizing Π through the entire history covers randomness by phases and composition within the contract; enumerating programs is unnecessary to prove the lemma.

<a id="112-proposición-de-transferencia-de-imposibilidad"></a>

### 11.2 Impossibility transfer proposition

Let S be a family of configurations of a system D and M the model of this manuscript. For each θ_D∈S fix a configuration θ_M and a policy transformation Φ, common to the worlds and not using hidden information. Assume Φ(π_D) belongs to Π_M and that, for **every** relevant policy π_D, satisfying the objectives in D implies satisfying the corresponding objectives in M, with the same units or declared conversions:

$$
\mathrm{Good}_D(\pi_D)\ \Longrightarrow\
\mathrm{Good}_M(\Phi(\pi_D)). \tag{8}
$$

If θ_M is in the impossible region, then no policy of D satisfies its objectives.

**Proof.** A good policy in D would produce through (8) a good policy in M, contradicting the theorem. ∎

A sufficient condition, after normalizing units and laws, is C_M≤C_D, ρ_M≤ρ_D and η_M≥η_D for the technical objective; substitute or add σ_M≥σ_D for the legitimate objective. These inequalities are sufficient, not necessary: (8) at threshold level suffices. The opposite direction does not transfer impossibility.

To transfer **attainability**, executable policies in D must be constructed from the relevant controls of M preserving the objectives. A bijection between all policies is unnecessary, and that additional direction is not needed for the lower bound alone. To assert an exact frontier in D, both the lower bound and controls attaining it are needed.

To prove that a difficult subfamily exists within a system, verifying these conditions in that subfamily suffices. Representing all its configurations is unnecessary. To assert the same result in all of them, verification of the full domain would indeed be needed; this manuscript does not do that.

<a id="113-éxito-con-presupuesto-por-rama-sin-imponer-coste-máximo-global"></a>

### 11.3 Success with per-branch budget, without imposing global maximum cost

For a policy executable under B, define

$$
\eta_R=P(H\cap\{C_{\mathrm{traza}}\le R\}),\qquad
\sigma_R=P(H\cap\neg V\cap\{C_{\mathrm{traza}}\le R\}).
$$

The cost of a failed branch may exceed R. Even so, each branch counted in σ_R pays C0 and can fund at most k reads. Repeating the lemma's proof gives σ_R≤q, ρ≥(q^{-1}−1)σ_R and ρ≥(1−q)η_R. The controls of (6) attain the same bounds. This extension requires that the deadline and all violations continue to be counted in the same process.

This corollary permits comparing the result with success indicators incorporating budget **per execution**, rather than a maximum-cost bound for the whole policy. It does not silently identify them: σ and σ_R are different measures. Partial experiments prove neither this correspondence nor (8).

The [transfer mapping and local M02 result](./R01_TO_CONDITIONED_TRILEMMA_MAPPING.md) and the [in-depth audit](./CONDITIONED_TRILEMMA_DEEP_AUDIT.md) specify verified and pending correspondences. The R01 source specification retains its content.


<a id="desarrollo-posterior-teorema-del-trilema-condicionado-en-r01"></a>

## Subsequent development: conditioned trilemma theorem in R01

The [main R01 theorem](./R01_CONDITIONED_TRILEMMA_THEOREM.md) formulates the result over the scenario's full configuration domain. It adds a general certificate, an information cut over complete histories, regions for all three pairs and feasibility, and a global-parity family with K data items and growing information cost for arbitrary N. It does not require transporting the same F formula to every configuration. A case of shared information resolving the problem is compatible with that conditioned theorem. This manuscript retains the F derivations and their hypotheses. [Self-review of the new theorem](./R01_CONDITIONED_TRILEMMA_REVIEW.md); independent reconstruction still pending.
