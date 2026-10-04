<a id="r01--viabilidad-matemática-del-trilema-por-configuraciones"></a>

# R01 — Mathematical feasibility of the trilemma by configurations

M12 in development · Version 0.1 · 4 October 2026 · No new technology interventions.

[Study entry point](./README.md) · [Plan](./WORKPLAN.md) · [Continuation and review](./CONTINUATION_PROMPT.md) · [Preserved scenario](../Escenario-creatividad-validacion.md#213-inventario-de-configuración).

This formulation incorporates the user's correction: there are configurations attaining all three conditions; there are families where each pair is attainable and the third condition prevents the conjunction. The proof must quantify over **all** admitted policies. Archived examples and diagnostics are bounded corroborations. A symbolic derivation for family F is offered here, with necessity and sufficiency, and mathematical transfer to the complete R01 scenario is retained as pending.

<a id="1-configuración-mundo-política-y-resultados"></a>

## 1. Configuration, world, policy and results

Configuration θ, hidden world ω and policy π are distinguished. θ determines the problem and its resources; ω determines facts the policy does not yet know; π uses only its observable history. A common policy must operate without knowing ω's label. Internal randomness is independent of the world before observation.

The scenario inventory already contains these dimensions; it is not replaced by a new collection of isolated cases:

| R01 dimension | Parameters | Role in the proof |
|---|---|---|
| Task and population | L steps/segments, N agents, obligation, principal, individual/collective unit | F uses a collective task and L independent facts; it does not presume N distinct tasks. |
| Geometry | Distances, sides, dispersion, connections, position correlation | F's geometry does not reveal normative facts; no hardness law in distance is proved here. |
| Benefits and worlds | Means, dispersion, correlations, prior, seeds/versions | F fixes benefits 1/2 and a uniform prior; benefits do not leak the binding. |
| Composition | Parity, conjunction, mixing; number n and location of relations/witnesses | These are distinct families. L does not itself determine n or the amount of decisive information. |
| Resources and charges | Aggregate budget R, deadline T, c_e, c_v, execution, messages, maintenance | Total work is distinguished from latency and maximum budget from expected cost. |
| Network | Topology, latency and communication availability | Granting perfect coordination facilitates F; its work bound is not a temporal bound. |
| Policy controls | Radius R_e, effort, k_a/k_d, inspection order, v, beta, s, w_s, memory, reuse, rejection, retry, abstention | If the claim covers all policies, these decisions belong to π; an incompetent window is not frozen to produce the result. |
| Derived quantities | Q unique proposals, coverage, duplication, cost, risk, efficacy | Results of the world and π; not independent variables selected afterward to force a conclusion. |

Reference: §§2.6 and 2.11–2.15 of the [scenario](../Escenario-creatividad-validacion.md). Submodel F requires basic reading of facts, with declared cost, without initial global certificates or free barriers. That is the base class; technologies are not yet compared.

Let Cθ(π) be the maximum cost of an execution, ρθ(π) the probability of at least one material violation and ηθ(π) the probability of completion with sufficient technical quality. Fix R≥0, 0≤r≤1 and 0<h≤1 before execution. Write:

\[
B_C=[C_\theta(\pi)\le R],\qquad
B_R=[\rho_\theta(\pi)\le r],\qquad
B_E=[\eta_\theta(\pi)\ge h].
\]

η is supplementary **technical** efficacy: a violation is not credited as legitimate R01 success. If legitimate success is required, σ=P(sufficient quality and no violation) is used, with another threshold and another frontier. The two theorems are not mixed.

Π(θ) contains finite legal policies for that interface, including those that would spend more than R. The cost objective is imposed through B_C: restricting Π to cheap policies in advance would make it impossible to express the risk–efficacy control at high cost correctly. Constructed controls have a sufficient deadline fixed in θ, common to the comparisons.

<a id="2-regiones-y-cuantificadores-correctos"></a>

## 2. Correct regions and quantifiers

For a subset S of {C,R,E}, define

\[
A_S=\{\theta:\exists\pi\in\Pi(\theta)\quad
\bigwedge_{i\in S} B_i(\theta,\pi)\}.
\]

The viable region is V=A_CRE. The requested pairwise regions are

\[
U_{CR}=A_{CR}\setminus V,\quad
U_{CE}=A_{CE}\setminus V,\quad
U_{RE}=A_{RE}\setminus V.
\]

For example, θ∈U_CR means that a cheap and safe policy exists, and **no** cheap and safe policy attains the required efficacy. It does not mean efficacy is impossible if paying more is permitted.

The minimum objective is V≠∅ and U_CR,U_CE,U_RE≠∅, with explicit parameterized families. A stronger form, satisfied by F, is:

\[
\exists\mathcal U\ne\varnothing\quad
\forall\theta\in\mathcal U:\quad
\left(\bigwedge_{S\in\{CR,CE,RE\}}\exists\pi_S\ B_S\right)
\ \land\
\left(\forall\pi\in\Pi(\theta)\ \neg(B_C\land B_R\land B_E)\right).
\]

The three policies π_S may differ. Regions U_CR, U_CE and U_RE may overlap; they do not necessarily form three disjoint areas. Having a strategy for each pair does not provide a common strategy for all three. Nor is every execution of every policy required to violate: what is unattainable is the joint guarantees in that configuration.

<a id="3-familia-f-contrato-sin-intervenciones"></a>

## 3. Family F: contract without interventions

L≥1 segments, with complete connectivity between options of adjacent segments. Each segment has M, safe with benefit 1, and X/Y with benefit 2. Binding χ_i∈{0,1} determines which of X/Y is admissible. The L bindings are independent and equiprobable. The admissible optimum is 2L in every world.

Tolerance 0≤ε<L requires J≥2L−ε on a complete route; therefore d=L−⌊ε⌋≥1 high options are needed. Each complete route pays C0=b+gL, b≥0,g>0. Reading a particular binding costs c>0, including all access stages. Reusing acquired facts is valid. No metadata, geometry, messages, benefit or free review reveal a new binding. Local computation and perfect coordination are admitted as a favorable envelope for any finite N, charging aggregate information work.

An unknown high option may be executed. The effect reveals its binding after occurring. A material violation is not erased even if execution continues and technically completes. Every option already known to be forbidden is rejected. Mandatory abortion altering the definition of efficacy is not imposed. Each instance has a finite horizon sufficiently broad to read all d facts and complete the task.

In AVG the uniform prior and π's randomness are averaged. In WC η_ω≥h and ρ_ω≤r are required in each world with the same randomized π. AVG impossibility implies WC impossibility; the sufficiency control will give the same rates in each world.

<a id="4-teorema-de-frontera-exacta-para-toda-política"></a>

## 4. Exact-frontier theorem, for every policy

For R≥C0, define

\[
k=\left\lfloor\frac{R-C_0}{c}\right\rfloor,\quad
m=\max(0,d-k),\quad q=2^{-m}.
\]

**Theorem F.** For AVG and WC with randomized policies,

\[
\boxed{\theta\in V\quad\Longleftrightarrow\quad
R\ge C_0\ \text{and}\ r\ge h(1-2^{-\max(0,d-k)}) .}
\]

**Necessity.** If R<C0 there is no fundable sufficient route and η=0. For R≥C0, any history of technical success without violation needs d high effects and can fund at most k paid reads. It must win at least m first bets on distinct still unknown bindings.

Before the first violation, each bet of this kind succeeds with probability 1/2 conditional on the entire previous history. Independence, adaptive selection, memory and queries to other indices do not change that fact. A new read may avoid a bet but does not inform another coordinate for free. Receipts of previous bets are admitted in full.

Let a_j be the probability of entering bet j before any violation. a_1≤1 and a_{j+1}≤a_j/2 hold. Stopping or querying between bets may reduce that probability. If σ=P(technical success without violation), for m≥1:

\[
\sigma\le a_m/2\le 2^{-m}.
\]

The events of first violation in each bet are disjoint and have probability a_j/2. Since a_j≥2^{m-j}a_m for j≤m,

\[
\rho\ge\sum_{j=1}^m a_j/2
\ge(2^m-1)a_m/2
\ge(2^m-1)\sigma.
\]

Moreover η≤σ+ρ. Therefore ρ≥(1−2^{-m})η≥(1−2^{-m})h. For m=0 the lower risk condition is trivial. Branches spending too much cannot contribute fundable success; stopping them before further bets eliminates no success and can only reduce risk. The proof directly covers randomized and adaptive policies. For WC, per-world guarantees imply AVG guarantees, so the same condition is necessary.

**Sufficiency.** With probability h attempt a route with d high options: read min(k,d) bindings and choose their admissible options; in the remaining m choose X/Y with independent coins; use M in the other segments. With probability 1−h execute M. Receipts are preserved and no future option known to be forbidden is executed. Maximum cost is C0+c min(k,d)≤R, and in each world

\[
\eta_\omega=h,\quad
\sigma_\omega=h2^{-m},\quad
\rho_\omega=h(1-2^{-m}).
\]

The control attains the lower bound exactly, including equality. ∎

This proves a frontier, not merely failure examples. The proof uses the declared interface, prior and charges. Validity within F and transfer to the complete scenario are different obligations.

<a id="5-regiones-viables-tres-pares-y-no-vaciedad"></a>

## 5. Viable regions, three pairs and nonemptiness

If 0≤r<h, define j_allow as the greatest integer j≥0 satisfying h(1−2^{-j})≤r. Then

\[
j_{allow}=\left\lfloor\log_2\frac h{h-r}\right\rfloor,
\qquad C_{crit}=C_0+c\max(0,d-j_{allow}).
\]

Equalities are decided using the original inequality, not a numerically rounded logarithm. For this profile, V is R≥Ccrit; the trilemma band is C0≤R<Ccrit. If r≥h, the band disappears and R≥C0 suffices. Boundary R=Ccrit is viable. A nonempty band is not claimed where the thresholds make it empty.

In the nonempty band U={θ:C0≤R<Ccrit}, these controls attain the pairs:

| Attained pair | Constructive policy | Cost, risk and efficacy | Third objective |
|---|---|---|---|
| Cost and risk | Execute M in all segments | C=C0≤R; ρ=0; η=0 | η<h. By the theorem, no policy preserving cost and risk attains h. |
| Cost and efficacy | Execute d high options without queries, with fair coins; M elsewhere | C=C0≤R; η=1; ρ=1−2^{-d} | ρ>r in this band. No cheap and effective policy respects ceiling r. |
| Risk and efficacy | Read all d bindings and execute admissible options | C=C0+cd; ρ=0; η=1 | C>R. No safe and effective policy also meets the budget. |
| All three | Theorem control with sufficient queries and attempt probability h | C≤R; ρ≤r; η=h | Exists at R≥Ccrit; does not contradict the previous band. |

**Nonemptiness and arbitrary sizes.** Fix b≥0,g>0,c>0,0<h≤1 and 0≤r<h. Choose any integer d>j_allow, L≥d, ε=L−d and R=C0. Then m=d and h(1−2^{-d})>r, so θ∈U_CR∩U_CE∩U_RE. There are infinitely many sizes by choosing ε=0 and L>j_allow. For the same sizes, changing only R to C0+cd permits all three in all worlds. Infeasible and viable families are thus proved without changing objectives after seeing results.

For any finite N, the same argument covers allocation of reads among agents with perfect coordination if C is aggregate and there are no additional prior facts. It is not concluded that more agents or greater distance make the problem difficult by themselves. Per-agent budget, latency and geometric-search regimes require their own contract.

<a id="6-qué-significa-solo-una"></a>

## 6. What “only one” means

In the space of pairs (θ,π), the eight compliance signatures (B_C,B_R,B_E) can be classified. A signature with only one good objective describes a policy and its results; it **does not prove** that another policy in that configuration cannot achieve a pair.

To assert that a configuration permits only objective i among all its policies, θ∈A_i but θ∉A_CR∪A_CE∪A_RE would need to be proved. That is an additional obligation. In F, abstaining with zero cost and no effects is cheap and safe for R≥0,r≥0: θ∈A_CR always. Therefore this exclusive “only one” region is empty within the current contract. If minimum delivery is required to consider a policy admissible, the contract changes and its lemmas must be proved again; that requirement is not introduced to manufacture a conclusion.

The plan retains both interpretations: result signatures and possibility regions. The pairwise trilemma proof does not require eight exclusive configuration regions to exist.

<a id="7-estado-de-validación-y-obligaciones-restantes"></a>

## 7. Validation status and remaining obligations

| Claim | Current evidence | Missing validation |
|---|---|---|
| F has a band with all pairs attainable and triple impossible | Above symbolic derivation for all policies in its class, control attaining the frontier and nonemptiness proof | Independent symbolic reconstruction and audit M16; not declared performed. |
| F also has viable regions | Explicit control with sufficient queries, including the boundary | Audit together with necessity. |
| The above is a theorem of complete R01 | Partial correspondences and preserved scenario | M17: embedding/reduction of worlds, all observations, policies, effects and costs; not now proved. |
| The trilemma occurs with a particular frequency in real systems | No recorded campaign establishes it | Neutral harness, competent controls and campaign with frozen configuration. |
| Some technologies reduce or eliminate it | Historical derivations and material preserved | Subsequent review of their contracts; not part of this base proof. |

Family W and its previous frontiers are preserved in [the F/W draft](./previous-work/M03_M04_TRILEMMA_THEOREMS.md). Their review is a second mathematical obligation; it is not automatically incorporated into the R01 theorem by adding dense relations. [Partial diagnostics](./partial-experiments/README.md) close none of the universal, independence or transfer obligations.


<a id="manuscrito-independiente-del-trilema-condicionado"></a>

## Independent manuscript of the conditioned trilemma

The previous formulation is preserved. The [independent manuscript](./CONDITIONED_TRILEMMA.md) develops the argument without requiring repository reading: hypotheses, universal lemma, necessity and sufficiency, regions, quantifiers and efficacy measures. It explicitly extends F to independent facts with prior a in AVG; for WC it retains q=2^{-m}. It includes a family with a 95 % legitimate-success target in AVG, without counting violations as success, and delimits when that result does not transfer to WC. [Symbolic self-review](./CONDITIONED_TRILEMMA_SELF_REVIEW.md); independent review and bridge to R01 pending. It changes neither fixtures nor historical results.
