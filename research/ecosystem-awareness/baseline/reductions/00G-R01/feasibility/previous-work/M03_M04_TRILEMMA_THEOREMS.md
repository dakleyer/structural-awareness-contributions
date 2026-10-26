<a id="r01--pruebas-del-trilema-y-efecto-de-las-tecnologías"></a>

# R01 — Trilemma proofs and effect of technologies

M03/M04, mathematical extension v1.0 · Derivation and self-review; independent review pending

[R01 README](../../README.md#bot-start-here) · [Mathematical plan](../../MATHEMATICAL_FEASIBILITY.md) · [Supplemental contract](../partial-experiments/historical/TRILEMMA_CONTRACT.json) · [Checker](../partial-experiments/historical/verify_trilemma.py) · [Finite results](../partial-experiments/historical/TRILEMMA_CHECKS.json) · [Preservation record](../partial-experiments/historical/TRILEMMA_RELEASE_CHECKS.json) · [Received proposal, unchanged](./TRILEMMA_RECEIVED_SKETCH.md)

Repository input: `2dc438df524663ebf79e6552cd688d34c2619d8b`. Author/reviewer: Codex, by user instruction. The following proofs are symbolic and cover all policies of the declared classes. Small checks seek errors in them; they do not replace them. Neither independent review, novelty, EA advantage nor classification of a commercial technology is claimed.

**Updated status, 4 October 2026:** this document retains v1.0 derivations and their checks; **M03/M04 are IN_PROGRESS for the expanded objective**, with independent symbolic review and bridge to R01 pending. DONE statuses mentioned below are the original deliverable record, not its final acceptance. Consult the [current plan and combined prompt](../../STRATEGIC_WORKPLAN_AND_EXECUTION_PROMPT.md#mathematical-strengthening); next task M12 with M06/M11 attacks. This status update adds no proof and alters no formulas, fixtures or results.

<a id="1-qué-se-prueba-y-qué-permanece-abierto"></a>

## 1. What is proved and what remains open

The thesis is existential over problem families, universal over policies: **there are physically realizable configurations in which every admitted policy fails at least one of low cost, low risk and high technical efficacy**. There are also configurations and technologies permitting all three. Not every configuration is presumed difficult.

Two proofs with exact frontiers are given. Family F has one independent binding per segment and requires linear additional cost. Family W has a global conjunctive condition and permits separating material segments from normative relations: with dense relations, necessary information cost is quadratic versus linear execution. An expected-cost bound for W is also proved; difficulty does not depend solely on requiring a maximum budget per execution.

Technologies are studied by interface and total cost. A cheaper query preserves the data-access bound. A sufficient certificate changes that interface. An executor guaranteeing admissibility changes the effect mechanism and may eliminate risk without revealing data to the agent. These changes require different proofs.

M03/M04 become DONE **for these supplemental profiles and their frontiers**, not for all R01. M05/C05, M06/M07–M09, E1–E7 transfer, campaign and real prices remain pending. M11 continues review of other generators and transfers. M01 and M10 are expanded through this versioned contract; their historical results retain their scope. Base source and previous fixtures are not modified.

<a id="2-contrato-común-objetivos-costes-y-políticas"></a>

## 2. Common contract: objectives, costs and policies

Each instance is finite; the family contains arbitrarily large sizes. There are L consecutive segments with all connections between options of adjacent segments. Each segment offers M, always admissible with technical benefit 1, and two high options with technical benefit 2. In every world exactly one high option is admissible. The admissible optimum is 2L. A complete route has technical benefit J even if its composition is inadmissible; that technical J is **not** credited as legitimate q in R01.

Fix before observing the world: tolerance 0≤ε<L, efficacy requirement 0<h≤1, maximum risk 0≤r≤1, budget R and deadline T. Let d=L−⌊ε⌋: a sufficient route needs at least d high options. W uses ε=0, hence d=L.

For each execution:

- Ttec: complete route of J≥2L−ε, within the profile's budget/deadline;
- V: some inadmissible material execution occurred in the campaign; it is irreversible;
- S=Ttec∩¬V: joint legitimate success;
- η=P(Ttec), ρ=P(V), σ=P(S). Always σ≥η−ρ and η≤σ+ρ.

η is a **supplementary measure of technical efficacy**. It replaces neither e/a/q/f nor makes a violation legitimate. When the original R01 objective is used, σ≥p is required and separate risk retained if applicable. This distinction matters: a trilemma with η and one with success already defined as violation-free have different frontiers (§3.3).

In AVG probabilities include the world with the declared prior and policy randomness. In WC ηω≥h and ρω≤r are required for **each** world ω, with probability only over internal randomness. A policy is common to all worlds and uses only its observable history. It cannot be chosen after learning the hidden label.

Every complete route pays C0=b+gL, b≥0 and g>0: preparation and material work, including self-review of geometry, decision, connections and execution. None of those reviews reveals the hidden binding before the effect. Registered queries read particular facts at exact total price c>0 per fact, with assured availability. Price includes production, access, receipt and applicability checking; no free information work is left behind the query. Repeated work is charged; reuse of the same known fact is permitted. Pre-effect costs and times do not leak hidden data.

Memory, local computation and perfect exchange may be granted for free as a favorable envelope for the agent. C is aggregate work of all agents, not time of the fastest agent. Any finite team is represented by a central policy with its whole history: granting perfect coordination only facilitates the problem. Thus lower bounds cover such teams if they retain the access interface; they establish no latency, network or distance bound. Actual information preparation and communication are charged when transferring to an implementation.

The receiver rejects an **already known** prohibition. There is no barrier checking the unknown binding for free before the effect. An unknown option may execute and produce a violation; the subsequent receipt reveals whether it was admissible. After a violation, subsequent currently admissible actions are permitted; V persists. A protocol imposing mandatory global abortion would have another η frontier. Budget is never knowingly exceeded to produce Ttec. Deadline and event maximum are fixed finite in each instance and sufficiently large for the described controls (for example O(L+n)); M02's limit 32 is not extrapolated to unlimited sizes.

For R≥C0, k=⌊(R−C0)/c⌋ limits queries on any Ttec route. If R<C0, η=0. A branch consuming more than k queries cannot produce Ttec; in minimum-violation arguments it can be replaced by safe stopping. Unprovided prior information, global predicates, certificates and barriers are other profiles, explicitly studied in §6.

<a id="3-familia-f-bindings-locales-independientes"></a>

## 3. Family F: independent local bindings

<a id="31-definición-y-cota-para-toda-política"></a>

### 3.1 Definition and bound for every policy

World χ=(χ1,…,χL) is uniform in {0,1}^L. At segment i, X is admissible if χi=0 and Y if χi=1. A query reads one χi. An execution receipt reveals only that binding. An arbitrary oracle over χ is not admitted in this profile. Computation, choice of what to query and when, cache and randomness may be arbitrary.

**Theorem F.** Let m=max(0,d−k) and q=2^(−m). Every policy satisfies

\[
\sigma\le q,\qquad \rho\ge(2^m-1)\sigma,
\qquad \rho\ge(1-q)\eta. \tag{F1}
\]

**Proof.** Before the first violation, the first high effect on a binding not queried or observed is a bet succeeding with probability exactly 1/2. Independence keeps this valid conditional on the whole previous history and adaptive decisions. Choosing the index by that history does not change the unseen bit. A query of another index does not reveal it. Receipts do provide information, but in a violation-free history their result for the chosen option is necessarily “admissible”.

Number the first bets on distinct bindings. Let aj be the probability of entering bet j before a violation. Then a1≤1 and a(j+1)≤aj/2; stopping or querying may reduce that probability. An S needs d successful high bindings and at most k queries, so needs at least m successful bets. For m≥1, σ≤am/2≤2^(−m). Events “first violation at bet j” are disjoint and have probability aj/2. Moreover aj≥2^(m−j)am for j≤m. Thus

\[
\rho\ge\sum_{j=1}^m a_j/2
\ge(2^m-1)a_m/2\ge(2^m-1)\sigma.
\]

With η≤σ+ρ, σ≤ρ/(2^m−1) follows, hence ρ≥(1−2^(−m))η. For m=0 the three inequalities are trivial. The proof directly admits randomized policies; an independent-of-world seed may also be fixed and averaged. Branches that fail, stop or execute additional work contribute no S and do not erase V. ∎

<a id="32-frontera-exacta-controles-y-cuantificadores"></a>

### 3.2 Exact frontier, controls and quantifiers

**Construction attaining the bound.** With probability β choose d high segments, query min(k,d) of their bindings and guess the rest with independent equiprobable coins; complete other segments with M. With probability 1−β execute only M. All receipts and reviews are preserved. A previous local violation does not identify the next independent binding; no future option known to be forbidden is executed. The result is

\[
\eta=\beta,\quad \sigma=\beta q,\quad
\rho=\beta(1-q),\quad C\le C_0+c\min(k,d).
\]

Coins make these values identical in **each** world, not only AVG. The AVG bound is necessary for WC; this control attains WC. Therefore, for AVG and WC with randomized policies,

\[
\boxed{\exists\pi:\ C\le R,\ \eta\ge h,\ \rho\le r
\iff R\ge C_0\ \text{and}\ r\ge h(1-2^{-\max(0,d-k)}).} \tag{F2}
\]

For 0≤r<h, let jallow be the greatest integer j≥0 with h(1−2^(−j))≤r; equivalent to ⌊log2(h/(h−r))⌋. Comparison with rational powers avoids numerical errors at equality. Then

\[
k_{\min}=\max(0,d-j_{allow}),\qquad
C_{crit}=C_0+c k_{\min}. \tag{F3}
\]

The impossible band is [C0,Ccrit), and equality R=Ccrit is viable. If r≥h, completion with probability h without information already satisfies the criterion; if d=0, M suffices. These empty bands are not hidden.

All three objective pairs have controls: M achieves cost C0 and zero risk with η=0; the blind high route achieves C0 and η=1 with risk 1−2^(−d); querying all d bindings achieves η=1 and zero risk with cost C0+cd. For any h>0 and r<h, sufficiently large d exists with h(1−2^(−d))>r. At those sizes no policy achieves all three at C0, although each pair is achieved. This is the quantified form of the requested trilemma, not an example list.

If ε=αL with 0≤α<1, d=⌈(1−α)L⌉. With fixed b,g,c, Ccrit−C0=c(1−α)L+O(1). For R=(1+λ)C0, asymptotic relative threshold is λ*=c(1−α)/g: below it fails for large L; above it works for large L. **At equality rounding must be retained.** With b=2,g=3,c=1,α=1/2,jallow=0,λ=1/6, even L is viable and odd L is not: margin L/2+1/3 must reach ⌈L/2⌉.

<a id="33-el-objetivo-legítimo-original-y-el-fixture-m02"></a>

### 3.3 Original legitimate objective and M02 fixture

If σ≥p is required instead of η≥h, for p>0 the exact F frontier is

\[
\boxed{p\le q\quad\text{and}\quad
\delta\ge p(q^{-1}-1).} \tag{F4}
\]

Necessity by F1; sufficiency with β=p/q. A larger budget may be necessary for both legitimate efficacy and risk. It is incorrect to assert that including legitimacy in efficacy always turns the problem into a mere dilemma: additional risk may be binding depending on p and δ. With δ≥1−p it is redundant for any policy with σ≥p, by disjointness of S and V; with smaller thresholds it may matter.

M02 is **not** F3: its three segments share a single χ. At R=11 an additional query does not fit; before the first high effect there is no χ information. If a technically sufficient route is attempted, the first high option is incorrect with probability 1/2. The same single-bet argument gives ρ≥η/2 and σ≤1/2. The correct strategy for η=1 is executing X in the first segment and, from the receipt, using the currently admissible option in the remaining two. Thus η=1,ρ=σ=1/2,C=11. Executing X three times despite knowing the prohibition is not an admitted control. With R=12 the existing certificate reveals χ before the effect and resolves the case. This connection alters neither the earlier fixture nor its 76 historical controls.

<a id="4-familia-w-conjunción-con-muchas-relaciones-y-pocas-acciones"></a>

## 4. Family W: conjunction with many relations and few actions

<a id="41-mundos-medida-y-normalización"></a>

### 4.1 Worlds, measure and normalization

There are n≥1 normative facts z1,…,zn and f(z)=AND(z). World G, all ones, has probability 1/2. Each Bj, with a single zero at j, has probability 1/(2n). High mode A is admissible if f=1; high mode B, an alternative procedure, if f=0. M is always admissible. The mandate is identical in all worlds. Each segment offers A/B/M and all mixtures; an A/B mixture cannot be completely admissible. ε=0 requires L high options. Technical benefit remains 2 per high option.

A query reads one zi at price c. There is no free global certificate. Local geometry does not prove f; an A/B effect reveals f after occurring. The correct mode may then complete execution, but the first violation cannot be repaired. This correlation between facts is deliberate: with equiprobable independent bits, AND would almost always be false and guessing B would resolve AVG at low cost. The balanced distribution between G and invalid witnesses is part of the claim, not a property of every AND.

W's n facts are not n statistically independent bits: the prior has only n+1 worlds. Its difficulty concerns **access through coordinate reads**, not a claim of n-bit entropy. An oracle delivering predicate f in one call may eliminate all n reads; that is precisely why it is studied as another technology in §6. F does have L independent bits. Independent experiment parameters are size, relations, price/interface, prior and thresholds; η/ρ/C depend on them and on the policy.

Let K=min(n,k) and u=K/n. To optimize risk at a given efficacy, a policy suffices which queries before the first A/B, chooses A/B/safe stopping and, if choosing a high option, finishes all L segments using revealed f. Queries after the first effect do not prevent V and may be eliminated. A branch with more than k queries cannot have Ttec and may be safely stopped. M on an ε=0 route prevents Ttec; replacing that branch with safe stopping worsens neither η nor ρ. After a zero, f=0 is known and B may finish without risk. Queries may be added up to K in the all-ones branch: additional information only permits avoiding an incorrect decision. This reduction is an envelope facilitating the problem; the final control executes within the original contract.

With a policy seed fixed, while responses are ones the query order is fixed and independent of which Bj is hidden. Among n Bj worlds, at most K detect a zero. This includes any coordination/cache through centralized history. In AVG detected mass is D=u/2; undetected invalid mass is H=(1−u)/2; G mass is 1/2. Undetected worlds and G have the same history.

<a id="42-teorema-w-avg-frontera-exacta"></a>

### 4.2 W-AVG theorem: exact frontier

\[
\boxed{\rho_{\min}^{AVG}(h,u)=
\frac{1-u}{2-u}\max(0,h-u/2).} \tag{W1}
\]

**Proof.** In undetected history, A and B have identical technical efficacy. A causes violations in mass H, B in mass 1/2; A is at least as favorable, so B may be replaced by A. Finishing with B in every detected case offers D efficacy without risk. If x is attempt-A probability in the remaining history, η≤D+(1−D)x and ρ≥Hx. Therefore ρ≥H max(0,h−D)/(1−D), which is W1. If fewer than K queries occur, completing to K and exploiting information does not worsen the result; the same bound for K is necessary. To attain equality, query K distinct indices; if a zero is detected use B. If h>D, attempt A in the remaining history with probability (h−D)/(1−D). If h≤D, finish only a fraction h/D of detected histories. In case D=0,h>0 the first branch applies. ∎

AVG feasibility holds exactly when R≥C0 and r≥W1. Minimum k is the smallest integer 0≤K≤n satisfying that inequality; it is not replaced by a merely necessary condition. For h=1,r<1/2,

\[
K_{min}^{AVG}=\lceil n(1-2r)\rceil. \tag{W2}
\]

<a id="43-teorema-w-wc-frontera-exacta-y-control-simétrico"></a>

### 4.3 W-WC theorem: exact frontier and symmetric control

For 0≤r<h, the necessary and sufficient condition is

\[
\boxed{(1-u)(h-r)\le r,\quad R\ge C_0.} \tag{W3}
\]

**Necessity proof.** In G, let x/y be attempt-A/B probabilities after queries with response one. Then ηG≤x+y and ρG≥y. Each A attempt on that history produces a violation in at least n−K Bj worlds because they share responses. Averaging Bj and seeds, ρB-prom≥(1−u)x. WC requirements imply x≥h−r and ρB-prom≤r. W3 follows. This proof presumes neither queries nor policy are symmetric.

**Sufficiency.** If K<n, uniformly choose a subset of K indices. With a detected zero, complete in B. Without a zero, attempt A with probability h−r, B with probability r, and M/stopping with probability 1−h. In G: ηG=h,ρG=r. In each Bj: ηj=u+(1−u)h≥h and ρj=(1−u)(h−r)≤r. In those histories both high options are still epistemically possible; a known rejection is not overridden. If K=n, f is known and execution always completes with its admissible mode; B is not attempted in G. ∎

Therefore,

\[
K_{min}^{WC}=\left\lceil n\max\left(0,1-\frac r{h-r}\right)\right\rceil. \tag{W4}
\]

For r≥h, a randomized execution attempt with probability h trivially satisfies the risk ceiling. With K=0, AVG and WC permit minimum ρ of h/2 through the appropriate control; a genuine impossible band requires r<h/2. For example, with h=1,r=1/4, AVG needs K/n≥1/2 and WC K/n≥2/3. Rounding and R=C0+cKmin are inclusive.

Objective pairs: M costs C0 and does not violate; starting A and adapting remaining segments to the receipt completes with ηAVG=1 and ρAVG=1/2 at C0; for the cheap WC control choosing A/B with a fair coin achieves ηω=1,ρω=1/2 in every world. Querying until a zero or all n facts achieves η=1,ρ=0 in all worlds with maximum cost C0+cn. Thus all pairs have witnesses and joint infeasibility is informative for h>2r.

<a id="44-teorema-de-familia-densa-coste-cuadrático-frente-a-ejecución-lineal"></a>

### 4.4 Dense-family theorem: quadratic cost versus linear execution

Choose n(L)=L(L−1)/2 distinct normative relations, for example one per segment pair; L≥2. Executing n material acts or listing a bit in each action name is not required: A/B are two L-step procedures subject to the same predicate over those relations. For fixed b,g,c and h>2r, W1/W3 require constant u≥u*>0 independent of L. In AVG this follows from W1 continuity and W1(h,0)=h/2>r; in WC, u*=(h−2r)/(h−r)>0. Then

\[
C_{crit}-C_0=\Theta(cn)=\Theta(L^2),\qquad C_0=\Theta(L).
\]

**Universal form.** For every policy/team in the fact-access class, every finite relative budget λ≥0 and every h>2r, there are arbitrarily large L such that no member of that class achieves η≥h and ρ≤r under R=(1+λ)(b+gL). Indeed, at those sizes **all** policies fail at least one requirement. The full-query control proves the problem is physically executable and greater resources resolve it.

Quantifier order: fix class/costs/thresholds; a family exists; for every finite λ there is L0; for every L≥L0 and every admitted π there is joint failure. The distribution is not chosen after learning π. Increasing agent count or reducing distances may improve time, but not the sum of new facts read if this interface and minimum price are retained. This cost profile is not imposed on every physical architecture.

<a id="45-coste-esperado-la-dificultad-persiste-sin-presupuesto-por-traza"></a>

### 4.5 Expected cost: difficulty persists without per-trace budget

In this alternative profile Ttec is defined by completion/quality/deadline and **E[C]** is limited, rather than requiring C≤R in every trace. Preparation b is charged in every started trial. Let Q be total facts read with charge, without counting the same event twice; actual repeated reads are charged.

\[
\boxed{E[Q]\ge\frac n2(\eta-2\rho)_+,\qquad
E[C]\ge b+gL\eta+\frac{cn}{2}(\eta-2\rho)_+.} \tag{W5}
\]

**Direct proof.** Fix a seed. Follow G history until first high effect or termination; let qG be the number of distinct queried indices, ≤n. Every Bj whose index is not among them reproduces that history. If the first effect is A, risk is at least (1−qG/n)/2 and η≤1; hence η−2ρ≤qG/n. If B, G already violates, ρ≥1/2 and η−2ρ≤0. If there is no high effect in G, neither is there in undetected Bj; then η≤qG/(2n), also giving the inequality. These η and ρ are over the prior for the fixed seed; eventual post-effect adaptation does not erase the violation. Averaging seeds gives η−2ρ≤E[qG]/n. Since G has mass 1/2 and at least qG reads are paid there, E[Q]≥E[qG]/2. Finally every Ttec pays at least material gL and every trial pays b, with nonoverlapping additional information charges. ∎

For η≥h and ρ≤r<h/2, E[C]≥b+gLh+(cn/2)(h−2r)=Ω(n). Full querying with uniform order and stopping at the first zero has E[Q]=(3n+1)/4 and η=1,ρ=0: G reads n and in Bj the zero's expected position is (n+1)/2. Hence scale Θ(n) is attainable for safe success. With n=Θ(L²), necessary expected cost is also quadratic. W5 is a bound, not an exact expected-cost frontier for all h/r.

With up to k0 particular facts initially available, even if granted free, the same coupling replaces qG by k0+qG and gives E[Q]≥[n(η−2ρ)−k0]+/2. In the budget profile u becomes min(n,k0+k)/n. If k0=O(L), the dense family retains its difficulty. This favorable grant does not authorize omitting the actual production cost of prior information in an implementation.

<a id="5-consultas-generales-qué-permite-el-argumento-de-capacidad"></a>

## 5. General queries: what the capacity argument permits

The received proposal permits an operation with N outputs at cost at least c log2N. This is broader than reading particular bits: a binary output may answer a global predicate. A necessary bound is retained for this class, but not exact frontiers F2/F4.

**Transcript lemma.** In F, assume the only branching of successful violation-free histories comes from finite informative operations with N outputs and price ≥c log2N; prices/metadata do not inform for free and violation-free material receipts add no branches. With s=R−C0≥0,

\[
\sigma\le\min(1,2^{s/c-d}). \tag{G1}
\]

**Proof.** Fix the seed and prune the tree to S histories. Each informative node retains at most N children. Assign weight 1/N to each edge of that node. The sum of leaf weight products is ≤1 by tree induction. For each leaf, ∏N≤2^(s/c), so its weight is ≥2^(−s/c); there are at most 2^(s/c) leaves. Each leaf fixes a route with at least d successful high choices and is compatible with at most 2^(L−d) worlds. Multiplying and dividing by 2^L gives G1. Averaging seeds preserves the bound. The tree has a finite event maximum; N=1 nodes are contracted. Receipts do reveal facts, but the successful branch of a chosen action has a single “admissible” result. ∎

Condition h−r≤G1 is only necessary. Exact F example with L=d=1,k=0,h=3/4,r=1/4: h−r=q=1/2, but actual minimum risk is h/2=3/8>r. Meeting the weak bound does not prove existence.

Furthermore, permitting at cost c the binary query “is χ all zero?” and acting only when it answers yes gives η=σ=2^(−L),ρ=0. For L=3,k=1, local inequality ρ≥(2^(d−k)−1)σ would be false. G1 is retained. Output size does not equal the number of particular reconstructed bits, and a rare certificate may permit risk-free action. Neither Fano nor a minimax theorem is invoked without checking its reduction: the above proofs are direct.

<a id="6-tecnologías-reducción-eliminación-y-cambios-de-clase"></a>

## 6. Technologies: reduction, elimination and class changes

“Eliminate” must specify the domain. Emptying the band for all R≥C0; resolving a particular budget; making any relative margin λ>0 work for large sizes; or eliminating V while leaving a cost necessary for η are different. There is no single classification without interface, producer, distribution, thresholds and costs.

<a id="61-cambios-que-conservan-el-acceso-a-hechos"></a>

### 6.1 Changes retaining fact access

If a technology permits only individual-fact reads with minimum total cost cmin>0, without sufficient initial facts or a barrier, lower proofs apply with k≤⌊(R−C0)/cmin⌋. A price lower bound suffices for impossibility; an upper control additionally needs available queries and their maximum price. Cache, inference over already seen facts, centralized team and parallelism do not reveal a new unobserved fact. Lowering c reduces the band. In F it may make a previously insufficient relative margin sufficient; in dense W any fixed positive cmin maintains Ω(L²) if C0 remains O(L).

Memory of valid already checked bindings may eliminate the problem in a static sequence with sufficient data. “Cache never helps” is not claimed: the difficult family uses new facts absent from memory. A favorable structure/prior may make a cheap prediction sufficient; M10's prior-9/10 counterexample must be preserved. These cases change relevant uncertainty.

<a id="62-certificado-suficiente-con-precio-total-fn"></a>

### 6.2 Sufficient certificate with total price f(n)

In W add an available query delivering current authenticated applicable f at total price f(n)>0. Count issuer, production, transport and use; if the producer must read n new facts at price c, do not arbitrarily attribute a logarithmic price. The certificate is a service assumption until its implementation is measured/verified.

If that is the only added interface and costs f(n) on every call, the exact budget frontier becomes

\[
C_{crit}^{nuevo}=C_0+\min(cK_{min}^{viejo},f(n)). \tag{T1}
\]

Below f(n), no Ttec route may use it and the old class remains; above it η=1,ρ=0 is permitted. An attempt unable to finish because of that charge may be replaced by safe stopping without improving minimum risk. The minimum of thresholds is therefore exact. The same argument holds in F for a certificate of the sufficient binding vector with price f(L).

A positive price leaves an absolute band near C0 **only when the original profile already had a nonempty band**. However, it may eliminate the obstacle for a relative criterion:

| Complete certificate price in W, n=Θ(L²), C0=Θ(L) | Required relative margin and effect |
|---|---|
| f(n)=O(1) or O(log(1+n)) | f(n)/C0→0: any λ>0 eventually works; an absolute band of width ≤f(n) remains. |
| f(n)=Θ(√n) | Relative margin of constant order; its coefficient matters. |
| f(n)=Θ(n) | Width remains quadratic and the ratio to C0 grows without limit. |
| Sufficient service already included in C0 | No additional charge: may empty the entire band R≥C0. Production remains paid within base cost. |

“Sublinear in n” alone does not suffice: n^(3/4) is sublinear but grows as L^(3/2) in W. The correct comparison is f(n(L))/C0(L). Batch law f(b)=c log b gives f(1)=0: free singleton queries would resolve the data. A coherent batch contract is needed, for example a positive preparation tariff and log(1+b), or a single global interface with declared price. A logarithmic lower bound is not converted into existence of a certificate at that price.

<a id="63-barreras-y-ejecución-admisible-por-construcción"></a>

### 6.3 Barriers and execution admissible by construction

A pre-effect barrier checking the binding may produce informative branches **without violation**. It no longer satisfies the F/G1 receipt hypothesis. Reusing those bounds without redoing the proof would be incorrect. Preventing a violation also does not guarantee that a sufficiently good alternative exists or is attained.

**Control with authorized dispatch.** Modify the executor so that, in every segment selected high, it selects/executes the admissible high option at additional charge a≥0, retaining reviews and material price g. It need not reveal χ/f to the agent. In the subprofile admitting only M and that dispatch (without unprotected bets or alternative queries), attaining d high options requires exactly additional ad. Therefore η=0 if R<C0+ad, and η=1,ρ=0 is possible at R≥C0+ad. The risk component is eliminated, but if a>0 a cost–efficacy dilemma persists. If additional a=0 because work is already included in g, η=1,ρ=0,C=C0 in all worlds: joint infeasibility is eliminated. This does not mean physical work is literally free or only that design exists.

Keeping g small and independent of n under that new executor is an assumption requiring implementation evidence. If the provider reconstructs f through n fresh reads at tariff c, its full cost must increase a or g; renaming that work “baseline” does not eliminate it relative to the previous architecture's budget. Additional a=0 control describes a capability admissible by construction or a check actually funded in that baseline, not a producer accounting exemption.

**Counterexample to counting rejections as paid bits.** In a subprofile of the same F worlds with ε=0, whose only high information/execution interface is the barrier (without coordinate queries or additional certificates), a first option may be checked without effect, with 0<a≤g. Every failed check costs a and every admitted/executed option costs g including its check and self-reviews. After rejection the correct alternative is chosen at price g. Charges are not omitted: every completion pays gL plus a times the rejection count. With budget C0+ak, a policy stops after rejection k+1, already charged, because it cannot fund sufficient completion; that charge fits the unexecuted material reserve since a≤g. There is no free observation through lack of budget. If there were ≤k rejections, budget remains for all acceptances. Therefore segments complete exactly when the number of incorrect first options is ≤k. In AVG, binding independence gives

\[
\eta_{max}=2^{-L}\sum_{j=0}^{\min(k,L)}{L\choose j},\qquad\rho=0. \tag{T2}
\]

Choosing first options with fair coins attains the same value in each world, so it is also the WC frontier. If that barrier is added while retaining other queries, T2 is an attainable control; the expanded class's optimum frontier may improve and is not automatically identified with T2. Adapting decisions does not improve AVG: every new binding remains fair before testing. Testing more than twice or stopping early does not improve completion. For L=3,k=1, η=1/2 results, greater than 2^(1−3)=1/4. The acceptance receipt reveals information without **additional** charge and rejection does not violate; T2 does not contradict F, it changes its kernel and charge distribution. A veto also charging every admitted test would have another model. These prices are a mathematical control, not a product measurement.

<a id="64-cambios-estructurales-y-tecnologías-que-pueden-perjudicar"></a>

### 6.4 Structural changes and technologies that may worsen results

A common admissible route with sufficient quality, tolerance making M sufficient, an always known predicate or capabilities excluding every forbidden option may eliminate the need to distinguish worlds. This may completely resolve a domain and does not require revealing all bits for free. No “single type of technology” eliminating every possible trilemma is proved.

A technology may also increase C0, charge redundant coordination, introduce stale information or block an admissible option. For example adding mandatory charge t>0 to every completion shifts material minimum to C0+t and makes η=0 at R=C0; improvements need not be attributed merely because it is called validation. An old/inapplicable certificate is not T1's sufficient service. Actual degradation is not claimed without verifying the contract and its results.

**Precise conditional conclusion:** every technology preserving the fresh-fact-read class with fixed positive minimum price, linear execution and absence of sufficient information/barrier inherits the dense family impossible at any fixed relative margin. Outside that class, the result depends on the capability added and its full cost; T1/T2 and authorized dispatch exhibit reduction, frontier change and elimination. There is no proof that “every positive-cost technology preserves the trilemma” under the draft's weak hypotheses.

<a id="7-auditoría-de-la-propuesta-recibida-y-correspondencia"></a>

## 7. Audit of received proposal and correspondence

The received copy is preserved byte for byte. Changes are formulated in this successor, not as silent correction of the original.

| Draft claim/gap | Disposition and repair |
|---|---|
| Bits per layer instead of isolated examples | F proves the objective; W proves stronger difficulty with normative facts separated from steps. |
| Literal no pre-effect despite permitting paid queries | Registered queries permitted; a free/unregistered material test of the binding is excluded. |
| Receipts without information | Reveal the binding; only lack additional branching in the violation-free part. |
| Bound σ and η−ρ interpreted as exact frontier | G1 is necessary; F1/W1/W3 provide stronger inequalities and controls attaining the frontier. |
| Minimum query price used as available price | Lower price for impossibility and availability/upper price for construction separated. |
| Certificates/globals treated as coordinate reads | §5 retains G1 and gives an explicit counterexample to transferring F1 to arbitrary predicates. |
| First X repeated after learning χ in M02 | Control with receipt and adaptation; known-prohibition rejection not omitted. |
| Any positive price preserves all difficulty | T1 distinguishes absolute band from relative margin and considers services included in C0. |
| f(b)=c log b | Free singleton; require coherent batch/preparation contract. |
| Barrier and queries subject to same bound | Changes kernel; T2 refutes that transfer. |
| Legitimate efficacy always implies mere dilemma | F4 retains a separate risk ceiling when binding. |
| Only free checking eliminates the trilemma | Authorized dispatch included in g and common routes also eliminate it in declared domains. |

R01: observable history, self-review, stable mandate, independent admissible optimum, all connectors/mixtures, irreversible V, cost/deadline and distinction between class proof and finite campaign are retained. New F/W are supplemental constructions; it is not claimed that the base text contained independent bits, n=Θ(L²), these priors or tariffs. Geometry/N/distances do not suffice to determine fresh-fact count. E1–E7, 00M/00N and the HF case require subsequent correspondence; no platform or selector automatically inherits the theorems.

Primary definition source: [Buhrman and de Wolf, 2002 preprint](https://homepages.cwi.nl/~rdewolf/publ/qc/dectree.pdf), introduction and §§3.1–3.2/4.1: adaptive bit queries, distributions of deterministic trees and certificates. These definitions motivate fixing the interface. F/W/G/T bounds are directly proved here; they are not attributed to that source. The document is neither an exhaustive review of subsequent results nor a novelty claim. Expected cost W5 and per-trace maximum are different profiles.

<a id="8-verificación-siguiente-trabajo-y-prompt-completo-de-revisión"></a>

## 8. Verification, next work and complete review prompt

Execute `python3 verify_trilemma.py > /tmp/TRILEMMA_CHECKS.json` and compare with TRILEMMA_CHECKS.json. The program uses exact fractions, enumerates through dynamic programming F query/M/X/Y/stop decisions and receipts for L≤3, and enumerates W query trees for n≤4. It verifies inequalities for all deterministic policies in those domains and explicit randomized controls; convexity extends the checked inequalities to their mixtures. It also checks frontiers, equalities, costs, W5, certificates, barrier and counterexamples. This is verification by the same agent, not an independent C05 oracle or proof assisted by a formal system. The release record retains hashes, input, commands, regressions and limits.

Next priority: independent M05/C05 review of the **contract and proofs**, followed by M07 correspondence and neutral oracle implementation. Before investing in concrete technologies, identify fresh facts, certificate/barrier interface and producer cost; check predictions in a registered campaign. Do not substitute trying models and then searching for an inequality explaining them.

**Prompt for another agent:**

> Review R01 at the published commit, starting with README.md, M03_M04_TRILEMMA_THEOREMS.md, TRILEMMA_CONTRACT.json and received proposal. Read M01, M02 and M10 to check that the extension alters neither e/a/q, known rejection, receipts nor historical costs. Your objective is attempting to refute proofs, not confirming examples. Check F1 for every history/adaptation/randomization, including interleaved queries and first observations through effects; F2/F4 must have constructions attaining each frontier. Check reduction to first high action in W, balanced G/Bj measures, WC argument without presuming symmetry and W5 without confusing hard budget with expected cost. Verify rounding, equality, empty bands, all connectors, abstention, memory, pooling and prior data. Try global binary certificates, asymmetric priors, common routes, batch tariffs and barriers; determine exactly which hypotheses change. Examine T1, producer charge, T2 and authorized dispatch; distinguish absolute/relative elimination and zero risk versus additional cost. Reproduce the checker and develop an independent method for a small domain without copying its recurrence. Do not close M05/C05 by reusing the author's program. Preserve historical source/fixtures/reports/manifests, record commit, UTC, commands and hashes. Deliver per theorem: VALIDATED IN ITS CLASS, COUNTEREXAMPLE with trace, or GAP with necessary assumption. Do not extrapolate to every technology, distribution, geometry, HF or EA; M06/M07 and independent review remain open until their evidence.
