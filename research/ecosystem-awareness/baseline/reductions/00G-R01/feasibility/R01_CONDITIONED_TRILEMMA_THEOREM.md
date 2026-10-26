<a id="validación-matemática-del-trilema-condicionado-en-r01"></a>

# Mathematical validation of the conditioned trilemma in R01

Conditioned trilemma of cost, risk and efficacy

Iván Abril Palma · Ecosystem Awareness · Mathematical formulation and validation

Mathematical version 0.2 · Canonical reference since 4 October 2026 · Symbolic self-reconstruction; external reviews received, current coverage to be verified.

<a id="canonical-mathematical-reference"></a>
**Documentary status.** This is the independent and canonical document for the mathematical formulation and validation of the conditioned trilemma in R01. It retains proof v0.2; its canonical designation establishes a single reference for statements, conditions and feasibility spaces. The explanation of the [R01 scenario](../Escenario-creatividad-validacion.md#r01-conditioned-mathematical-validation), the [R01 README](../README.md) and the [mathematical validation index](./README.md) refer here. Earlier manuscripts are retained as background, without competing as the current formulation.

Documentary designation declares neither an executed campaign nor complete independent coverage. Received external reviews are acknowledged; their scopes and still unverified steps must be recorded by version and proposition in [the register](./WORKPLAN_STATUS.json). Technologies and extension protocol remain in a separate phase.


R01 source: [Escenario-creatividad-validacion.md](../Escenario-creatividad-validacion.md), version 0.6, read at commit `2d299250a1e9d8103757f3841c73fdb01db82598`. This document develops a theorem over its configuration domain. It modifies neither the experimental specification, incidents, fixtures nor historical results.

<a id="1-qué-se-demuestra"></a>

## 1. What is proved

The result is a **conditioned trilemma in R01**: there are families of R01 configurations where all three pairs cost–risk, cost–efficacy and risk–efficacy are attainable with the same thresholds, but no admitted policy achieves all three conditions. There are also viable families. Impossibility is proved for all policies of the difficult configurations, not for a selection of algorithms.

The theorem's domain is complete R01. The condition identifying a difficult region is not imposed on all its configurations. Memory, sufficient certificates, shared dependencies, resolving APIs, search, geometry, collaboration and recovery remain within the domain. They may cause a configuration to cease satisfying that condition and become viable. This is compatible with the result.

There are three separate contributions: (i) an impossibility certificate applicable to any R01 manifest; (ii) an information-cut theorem with explicit hypotheses over the complete history; (iii) a parameterized R01 family with growing information price whose frontier and controls are proved exactly. Family witnesses establish that the regions are nonempty; they do not replace the universal argument over policies.

No single numerical formula for every R01 interface, already measured empirical frontier or characterization of the scenario's six Pareto dimensions is announced. The concrete result concerns total cost, probability of violation and probability of sufficient legitimate quality within the deadline.

<a id="2-dominio-completo-y-políticas"></a>

## 2. Complete domain and policies

A configuration θ comprises the fixed task and mandate; L; N; graph and connectors; benefits and geometry; world distribution; initial information and its charges; operations and responses; evidence, versions and certificates; topology and latency; ledger; physical capacity B; deadline T; review, rejection and execution rules; and quality criterion ε. This is the R01 §2.13 inventory, completed with the causal contract of §§2.6–2.8,2.11,2.16–2.17.

A complete manifest defines, for each operation, its accessible response, transition, charge, duration, evidence production and possible effect. It may be local, global, shared or dynamic. An incomplete description does not yet determine a unique mathematical problem: different responses or costs may yield different regions. This obligation to complete each configuration adds no new physical model to R01.

Π(θ) contains all executable policies under that contract. Each agent uses its local history, memory, received information and randomness independent of the hidden world. Adaptive decisions, order changes, randomization, search, incremental review, composition, stopping, abstention, retries and permitted recovery are included. A collective policy can coordinate through every mechanism θ actually provides. It does not receive the evaluator's hidden state for free.

For the bounds, a more powerful envelope is additionally permitted which instantaneously gathers all legitimate observations of the agents, ignores their transmission cost, retains acquisition charges and respects effects and the aggregate ledger. Each distributed policy induces a policy of that envelope: it reproduces its seeds, decisions and schedule. Proving impossibility even there covers the original population. Attainability controls are constructed in the original system without needing that free communication.

Not all R01 is assumed to have a finite observation tree. The information proof uses causal histories and conditional probabilities without needing enumeration. The §5 linear-programming result expressly requires a finite manifest; it is not extrapolated to all continuous generators.


<a id="21-tres-familias-de-variables-y-su-correspondencia-formal"></a>

### 2.1 Three families of variables and their formal correspondence

**Practical vocabulary and correspondence with the proof.** The problem together with the technology or technology combination defines an **operational scenario**, described by θ. R01's base technology is the already declared abstract interface with its means and charges, not a validated concrete implementation. Acceptance policies apply separately: (θ,b,δ,p) is the scenario evaluated under those requirements, called an evaluation profile in the existing formalism. For a strategy π∈Π(θ), the triple (c(π),r(π),s(π)) belongs to the **accepted zone** if c≤b, r≤δ and s≥p. Here c retains the §3 per-execution ceiling rather than expected cost, while r and s are probabilities over declared executions. The scenario is viable under those policies when at least one accepted strategy exists. A strategy outside the zone does not prove scenario infeasibility; that requires ruling out all admitted strategies. [The R01 chart and explanation](../Escenario-creatividad-validacion.md#from-the-practical-problem-to-acceptance) present the same separation. This correspondence preserves θ, Π(θ), metrics, quantifiers and proofs.

The description distinguishes three families by function. This separation identifies what remains fixed and what changes; it does not presume statistical independence between their components.

| Family | Content | Role in the result |
|---|---|---|
| Acceptance policies | Maximum tolerated risk δ, minimum legitimate efficacy p and maximum accepted total cost b. | Determine acceptable results. Fixed before evaluation and retained when comparing execution policies. |
| Problem parameters | Task, mandate and obligations; routes M, I and P, benefits and attractiveness difference P–I; L, N, worlds, graph, geometry, dependencies, initial context, required evidence, ε, T and declared resource constraints. | Determine the problem, necessary information and quality and violation events. I/P are evaluator labels, not free decision data. |
| Technology | Capabilities of a concrete implementation: operations and observations, information acquisition and processing, memory, evidence, communication and coordination; parameters such as R_e, k_a, k_d, v, beta and selection rules under the declared contract; complete costs, latencies and limits. | A future extension must prove correspondence with the admitted abstract interface and declare which conditions or frontiers it changes. No concrete technology is applied or validated here. |

The R01 explanation uses **execution strategy** π as the name of the **execution policy** already defined in Π(θ): the action rule of each agent or the collective using permitted information and means. This is a terminological change, not expansion of actions, access, costs, times or freedom to alter parameters. **Acceptance policies** are thresholds b, δ and p: multiple π are evaluated under the same thresholds. Uppercase P is the forbidden route; lowercase p the required minimum efficacy.

θ remains the **complete mathematical manifest** of §2. It includes problem parameters and the abstract contract of operations, responses, charges and times determining Π(θ). The third family identifies how a concrete implementation must realize that contract; no technology is added to the base theorem and its interface is not deleted from the manifest. Therefore varying a technology may change accessible information, costs, times and Π(θ). Preservation of the trilemma is not inferred: that issue requires the protocol and a subsequent proof for the corresponding implementation.

To compare technologies, acceptance policies b, δ and p are retained. Effective configuration may vary: map t↦θ(t) must declare what changes in observations, evidence, exploration, review, memory, communication, costs, times, population or physical capacity. (θ(t),b,δ,p) is then evaluated over Π(θ(t)). This notation proves neither transfer nor persistence of the trilemma; it requires completing the contract and verifying its conditions again.

| Technological capability or limit | R01 correspondence to be made explicit |
|---|---|
| Exploration and search | R_e, effort, accessible candidates, c_e and observed volume Q. |
| Review and evidence | k_a, k_d, inspection order and output, c_v, certificates, collective history and I3 bound a. |
| Memory and reuse | Initial context, current evidence, reused coverage, preparation, acquisition and maintenance. |
| Communication and coordination | Topology, R01 social intensity s, latency, w_s, dependencies, v, beta and transfers. |
| Execution and recovery | Selection rule, tie-breaking, abstention, waiting, retries, recovery, charges and effective deadline. |
| Deployment | N, work allocation and B/R when implementation changes capacity; do not confuse B with fixed threshold b. |

R01's social-intensity s is not the legitimate-efficacy s(π) of §3. Each symbol retains its context and the quantities are not identified. L, mandate, benefits and P–I difference, world distribution, geometry and composition predicate may vary between declared scenarios. If introducing technology changes any of them, the effective parameter that changes must be declared. Modifying the mandate or what makes P forbidden changes the problem, not merely its execution means. It is presumed neither that every variable changes nor that every variable remains frozen.

A technology or procedure may introduce a relevant variable not represented in R01. Its extension must identify it and prove whether the existing manifest can faithfully express it; otherwise, an expanded model and its relation to the base theorem must be declared. Coverage outside the domain is not presumed and an omitted capability is not treated as nonexistent.

The conclusion of that phase remains open. Partial resolution means recovering previously infeasible scenarios under the same acceptance policies b, δ and p; existence of a residual trilemma region needs its own proof. Complete resolution in a declared domain requires triple feasibility throughout that domain. Mere absence of T does not suffice: there may be scenarios where a pair already fails. If I1–I3 cease to hold, the §6 bound does not itself establish impossibility for that configuration, nor does it prove viability. Therefore the extension may establish complete resolution, partial resolution, absence of recovery or an undetermined result. A proved expansion of F is a positive result; which occurs is not anticipated here.

To study different acceptance criteria, θ may be retained and b, δ or p varied; that is a different contrast from comparing technologies with fixed thresholds. Raising δ expands what is acceptable without reducing r. Increasing b permits more economically acceptable strategies without thereby increasing B.

Cost b is the ledger **total** and includes validation, preparation, exploration, execution, communication and other charges. The validation component is broken out, without substituting it for the total. If an additional limit solely for validation is fixed, it must be declared as an additional constraint with its own symbol and accounting. ε, T and B retain their role in the manifest; b≤B distinguishes the economic criterion from physical possibility.

<a id="3-métricas-y-umbrales"></a>

## 3. Metrics and thresholds

Let V be the event of at least one material violation executed during the campaign. Subsequent repair does not erase V. Let H be technically sufficient delivery within T, and S=H∩Vᶜ sufficient legitimate delivery. The admissible optimum and tolerance ε are fixed before deciding, as in R01 §§1.4,2.1.

In AVG, relative to the declared distribution of worlds and seeds:

$$
r(π)=P_θ(V),\qquad η(π)=P_θ(H),\qquad s(π)=P_θ(S).
$$

C_traza is the complete ledger through closure, including preparation, discards, production, use, messages and failures. The low-cost objective is a **per-execution ceiling**, c(π)=ess sup C_traza≤b, not expected cost. B is the problem's physical capacity and b≤B its economic target. Physical cap B continues to apply to all policies, including controls exceeding b.

The distinction permits comparing a cheap policy with a more expensive one in the same physical configuration. If B=b is fixed and spending more is physically prohibited, there is no costly control within that same space: that would be another statement. This distinction is not hidden under the scenario's budget symbol R.

The trilemma's main efficacy is s≥p, with 0<p≤1. η is also reported, without confusing technical benefit after a violation with legitimate quality. R01 compound success for target b is e_b=P(S∩{C_traza≤b}); with c≤b, e_b=s. To evaluate a more costly control, s is retained and failure of b indicated: its e_b is not counted as high. Under physical capacity B, the informed control described below does have e_B=1.

The three conditions are C_b: c≤b; R_δ: r≤δ; E_p: s≥p. Risk is identified neither with harm nor with 1−completion.

<a id="4-cuantificadores-del-teorema"></a>

## 4. Theorem quantifiers

For each θ, policy sets P_CR, P_CE, P_RE and P_CRE are defined over its complete class Π(θ) through the respective conjunctions of conditions. The trilemma region is

$$
\mathcal T=\{(θ,b,δ,p):P_{CR}\ne\varnothing,\ P_{CE}\ne\varnothing,\ P_{RE}\ne\varnothing,\ P_{CRE}=\varnothing\}.
$$

The viable region is F={ (θ,b,δ,p): P_CRE≠∅ }. Pairwise projections may overlap; they are not turned into artificially exclusive regions.

**Main R01 theorem.** Within the R01 configuration domain there are infinite families contained in T and infinite families contained in F. For all configurations of the difficult families, all their policies satisfy an explicit bound preventing the triple condition; all three pairs have executable controls with the same thresholds. The difficult family may have any L≥1, any N≥1 and an indispensable-information price growing without limit. The §6 information condition additionally supplies a bound for any other R01 configuration satisfying it, without imposing independence per segment.

The complete proof is in §§5–10. Mere definition of T does not prove its nonemptiness; the controls and bounds of §§7–10 establish it. Nor is T∪F claimed to classify all configurations: there are cases where a pair already fails, as well as cases still without an explicit bound.


<a id="41-alcance-universal-de-la-afirmación-condicionada"></a>

### 4.1 Universal scope of the conditioned claim

Let Θ_R01 be the domain of all complete manifests satisfying R01 conditions. The theorem does not replace that domain by the §7 family. For every θ∈Θ_R01, all policies Π(θ) are considered with all actually declared operations and observations. The §5 certificate is valid in each of those manifests. In particular:

$$
\forall θ\in Θ_{R01},\quad
\bigl[I1(θ,b)\land I2(θ,b)\land I3(θ,b,a)\bigr]
\Longrightarrow
\forall π\in Π(θ),\quad
c(π)\le b\Longrightarrow
\bigl[s(π)\le a\ \land\ r(π)\ge \tfrac{1-a}{a}s(π)\bigr].
$$

If, in that same θ, the three legal controls of §6 exist and δ<p(1−a)/a, membership in trilemma region T follows. The §7 family proves such configurations exist for arbitrary sizes; it is not substitution of the general domain by proof of a single control. A configuration with sufficient accessible and affordable information may belong to F. If a pair already fails, it belongs to a third category distinct from T and F.

“For all R01” here means validity of this conditioned claim throughout Θ_R01 and coverage of all policies in configurations satisfying its hypotheses. It does not mean that every individual configuration must simultaneously exhibit all three pairs and triple impossibility: a fully informed configuration is a viable case admitted by R01. The certificate's form is general; its evaluation and numerical frontier depend on the manifest. A still incomplete description of responses, costs or initial data does not allow determining that unique frontier.

This deliverable contains only formulation and proof under R01 conditions. It applies no technology and does not take transfer to an implementation as proved.

<a id="5-certificado-general-sobre-cualquier-interfaz-r01"></a>

## 5. General certificate over any R01 interface

For every θ and b, let Π_b={π∈Π(θ):c(π)≤b}. For λ≥0 define

$$
A_{θ,b}(λ)=\sup_{π\in Π_b}\{s(π)−λr(π)\}.
$$

**Proposition 1.** If, for some λ≥0,

$$
A_{θ,b}(λ)<p−λδ,
$$

no policy satisfies C_b,R_δ,E_p. **Proof.** A triple policy would give s−λr≥p−λδ, contradicting the bound. ∎

This numerical certificate is not limited to a graph family: it includes the entire interface θ in the optimization. The following information lemma provides a computable bound for A, rather than leaving it as an unevaluated supremum.

For a finite manifest, fixing all policy seeds beforehand gives a joint deterministic strategy over local histories. There are finitely many such strategies, although the number may be enormous. Randomization integrates their results. Every strategy with positive weight in a policy with hard ceiling b must respect b in all branches of positive probability; a costly strategy does not become cheap by being executed infrequently.

Therefore a bound on s_j−λr_j for **all** cheap deterministic strategies also covers adaptation and private seeds. This remains valid if communication constraints prevent implementation of certain joint mixtures. In that case the convex envelope is a relaxation for impossibility, not an unjustified equality of the distributed system.

If all ex ante mixtures of those strategies are implementable under θ, cheap efficacy with bounded risk is exactly the linear program

$$
\max_{x_j\ge0}\ \sum_jx_js_j
\quad\text{subject to}\quad \sum_jx_j=1,\quad\sum_jx_jr_j\le δ.
$$

If a cheap zero-risk strategy exists, the program is feasible for δ≥0. Its dual is min_{λ≥0}[λδ+max_j(s_j−λr_j)]. Linear-programming duality exactly characterizes triple feasibility of that finite manifest. Absence of public mixing or finiteness invalidates neither proposition 1 nor the cut theorem; it only prevents announcing this finite calculation as an exact characterization of that profile.

<a id="6-teorema-general-del-corte-informativo"></a>

## 6. General information-cut theorem

The following conditions are verified over complete history, including the group and all acquired evidence. Two isolated local observations do not suffice.

I1. There is a first critical effect τ, whose start is determined by observable history and the selected action before knowing its effect. The event “τ still unresolved” is also determined from that information; it cannot be selected retrospectively through the hidden world or future success. Every delivery H of sufficient quality includes that effect. An incorrect decision there executes a violation and V remains recorded. Abstaining before τ does not attain H.

I2. Every trace with H and C_traza≤b reaches τ with information still insufficient to resolve its alternative. Resolving it before τ, including production and all necessary preparation for that delivery, exceeds b. Sufficient queries are permitted: their cost places them outside the cheap objective.

I3. In any collective history before an unresolved τ, even conditioning on all decisions and seeds used up to then, the probability that the chosen alternative is correct is at most a, with 0<a<1. That bound includes deductions, metadata, rejections, memory, certificates and messages. It is not an assumption of inability of a particular algorithm.

Let U be the event of reaching the first critical effect without resolving it, u=P(U), and λ=(1−a)/a. For any policy with c≤b:

$$
s\le au\le a,\qquad r\ge(1−a)u,\qquad r\ge λs,\qquad r\ge(1−a)η.
$$

**Proof.** Let G_t be the collective history before the effect, including the selected action and already used seeds. Events U_t={τ=t and still unresolved} are disjoint and G_t-measurable. If A_t indicates that the choice is correct, I3 establishes P(A_t|G_t)≤a on U_t. Thus P(U_t∩A_t)=E[1_{U_t}P(A_t|G_t)]≤aP(U_t). Summing, with u=Σ_tP(U_t), cheap success satisfies s≤au and incorrect choices, contained in V by I1, give r≥(1−a)u. By I2, a cheap delivery has unresolved τ. Legitimate success requires τ to be correct; by I3, its probability does not exceed au. An incorrect decision on U occurs with probability at least (1−a)u and by I1 is contained in V. Dividing the two bounds gives r≥λs. Cheap technical delivery is contained in U, so η≤u and r≥(1−a)η. Histories without τ, late failures and stopping can only reduce s; additional violations can only increase r. ∎

To connect with §5, use multiplier μ=1/λ=a/(1−a), not λ: r≥λs implies s−μr≤0 and A_{θ,b}(μ)≤0. If δ<λp, then p−μδ>0 and proposition 1 proves triple impossibility. The coefficient of r≥λs and certificate multiplier are reciprocal. This proof covers any R01 configuration with I1–I3, whatever the physical reason for missing information: independent facts, a global dependency, shared data or an evidence search.

**Per-trace compound-success corollary.** For any physical policy π∈Π(θ), even if it spends more than b in other branches, define η_b=P(H∩{C_traza≤b}) and s_b=e_b=P(S∩{C_traza≤b}). The same proof gives s_b≤a, r≥λs_b and r≥(1−a)η_b: I2 uses only cheap-delivery branches and U's violations remain counted over the entire campaign. Therefore requiring e_b≥p and r≤δ<λp is impossible even allowing failures or costly deliveries outside that success event. Cheap success is not obtained by subsidizing it with additional branches. This corollary connects directly to R01 compound evaluation without identifying per-trace ledger with policy maximum.

**Nonvacuous trilemma theorem.** Add legal controls: a cheap zero-risk M route with insufficient quality; a cheap-attempt policy which, with probability β, achieves η=β,s=aβ,r=(1−a)β,c≤b; and an informed policy of s=1,r=0,c≤B. For

$$
0<p\le a,\qquad 0\le δ<p(1−a)/a,
$$

all three pairs are attainable and the triple condition is impossible. M proves CR; β=p/a proves CE; the informed policy proves RE. The bound forces the latter not to be cheap. ∎

Attainability is an additional obligation: I1–I3 alone prove incompatibility, not that all pairs are possible. §§7–9 construct these controls within R01.

<a id="7-familia-r01-de-dependencia-global-y-precio-creciente"></a>

## 7. R01 family of global dependence and increasing price

For any L≥1,N≥1,K≥1, construct θ_{L,N,K,a}, with 1/2≤a<1. L is task length; K is the number of normative data items of a global dependency. Case K=L uses precisely the parity-composition control admitted in R01 §2.9. Permitting other K describes more or fewer normative relations per task, not another hidden material length.

**Mission, graph and quality.** There are L layers with nodes M_i,X_i,Y_i. M_i is worth 1, X_i/Y_i are worth 2. All connectors between consecutive layers are declared, have zero benefit and are included in the gates. The obligation always admits M_i and admits X_i if χ=0 or Y_i if χ=1. χ is fixed during the campaign. The admissible optimum is 2L; ε=0 requires L high choices. M is worth L. I/P are evaluator labels, never names received by the agent. Coincident high benefits are a control permitted by §2.3. Radii, sides and connectivity are identical at both χ values and do not leak it.

**Normative dependency.** There are K authority relations with data w_1,…,w_K and public rule χ=w_1⊕…⊕w_K. Hidden data are not confused with new authorization: mission and rule remain fixed. χ is generated with P(χ=0)=a, and one of the 2^{K−1} vectors of that parity is chosen uniformly. For a=1/2, data are independent uniform bits. For a>1/2 they are correlated; the proof does not treat them as independent.

**Initial information and preparation.** The profile starts with acquired and paid common technical preparation: map of 2L candidates, rule references, M evidence and version. Its automatic charge is C_pre=2+4L+2(N−1): preparation 2, discovery of 2L candidates at c_e=2, and initial communication to each additional agent with send and receive cost 1 each. Sufficient sequential duration 1+2L+2(N−1). It includes neither any w_j nor χ. Identifiers, lengths, positions, references and technical records do not depend on χ. There is no initial normative certificate or prior knowledge of its data.

That initial state and its expenses are part of θ, as permitted by R01 §§2.1,2.6,2.15. No policy can erase them. Exploring the entire catalog first is not claimed optimal for a campaign starting before that context; that campaign would be another configuration of the complete domain. Even a favorable technical prior is offered here to isolate indispensable normative cost. Purchase of that prior is not declared free information.

**Operations and complete transition.** The environment's global state contains the actually executed prefix, local certificates, commitments, observed candidates, acquired normative data, valid χ evidence, delivered messages, version, ledger, clock and V. Policies receive only the observable parts provided for their identity. V and unacquired χ remain private in the evaluator; observable collective history does not include those values.

| Operation | Charge and duration | Response, transition and limits |
|---|---|---|
| Initial preparation | C_pre and 1+2L+2(N−1) | Previous paid technical prior. Repetition pays again and resets neither ledger, prefix, V nor data. |
| Explore | 2 and 1 per candidate | Geometry/technical benefit. Does not inform w or χ; here the prior already contains those candidates. |
| Review local | 1 and 1 | Checks node, material connector, mandate/version and exact technical scope of the next layer; produces local evidence. Does not inspect still pending normative relations. Expanding that scope is performed with inspect relation and its charges. |
| Decide | 1 and 1 | Uses current local evidence, checks applicability of acquired data and computes parity if all are present; rejects a known prohibition; creates exact commitment. Price includes that use/computation, without a second hidden charge. |
| Execute | 1 and 1 | Requires gate and commitment for next layer. Atomic effect; advances prefix and consumes gate. Public receipt confirms technical execution and its charge, without χ or normative verdict. The evaluator adjudicates admissibility separately; if inadmissible, V is set permanently to 1. Subsequent χ diagnosis would require a declared operation and charge. |
| Inspect relation / query state | 1 and 1 per examined datum | Returns a w_j, scope, origin and version. Acquisition and production of that evidence are included. Rereading pays again; it obtains no other hidden datum. |
| Query mandate | 1 and 1 | Returns already known formula, principal and version. Requesting underlying facts uses the above reads. |
| Global certificate / resolving API | At least as many read charges as new w_j needed; declared additional use ≥0 | Exists only after evidence production: reads missing data, records producer and charges, and delivers parity. An external producer has no prior certificate in this profile. It does not charge only output size. |
| Communicate | 1 per send and 1 per receive; duration 1 for each operation | Only already acquired evidence and content computed from local history. Retains origin/scope; produces no new facts. |
| Reuse / memory | Recovery of known records; no new acquisition charge, use covered by the operation employing it | Valid data may serve all layers. Copying evidence discovers no pending datum and generates no different certificate. |
| Wait / stop | 0, duration 1 / 0 | Waiting does not change the world; stop terminates without converting an incomplete route into a delivery. |
| Rejection or error | No hidden effect; errors pay requested charge except prior capacity rejection | Error messages, availability, size and latency do not depend on unacquired data. There is no reset, direct evaluator read or undeclared external operation. |

A combined query may request any data subset and charges 1 per read. A summary computed from already acquired data is fully reusable. If only χ is requested, its producer must obtain still unacquired data and they are charged in the same global ledger. This permits the resolving API; it does not prohibit it to preserve failure.

The N agents may read in parallel, divide data and communicate them. There is only one collective material prefix, without multiplying quality by agents: concurrent effects are causally ordered and only one valid execution advances each layer. Barriers, gates, preparation, states and charges are identical for all. The centralized envelope has all evidence acquired by anyone, so the proof does not depend on preventing useful cooperation.

Each complete delivery pays at least

$$
C_0=C_{pre}+3L=7L+2N.
$$

The L local checks concern successive scopes; they are neither K normative rereads nor a requirement to repeat an already acquired global proof. The informed control reuses its single parity at all layers.

Fix B=C_0+K and sufficiently large T, for example T=5L+K+2N+4. Controls need at most preparation, K reads, 3L gates and stop; that T covers them. If the manifest requires an event cap, use H_cap=5L+K+2N+4. A historical H is not kept constant as size grows.

To complete §2.13 parameters: use a single shared global budget B=C_0(L,N)+K, without adding B quotas per agent; that B includes N-dependent initial distribution and does not remain constant when comparing different populations; reserve 2+2(N−1)+2L for administrative preparation, initial distribution and decisions/effects; the remaining discretionary amount is 5L+K, with v=(L+K)/(5L+K) for review and 1−v for discovery. Transfers between allocations are permitted always under B and with the full ledger; additional communication also consumes that budget. The network is complete with latencies declared above, radius R_e=2 and positions ±1; initial technical information is legitimate memory, not free search during the campaign. The local review unit is the material relation with its endpoints/connector, at price 1; the K normative relations are other scopes. Versions and mandate are static. Each policy resolves ties and the controls' coin is independent of worlds. There are no per-agent quotas preventing the control's agent from executing the task; other allocation regimes are other θ in the domain.

<a id="8-ausencia-de-filtraciones-y-cota-para-todas-las-políticas"></a>

## 8. Absence of leaks and bound for all policies

**Parity lemma.** For any proper subset D of {1,…,K} and any assignment z_D,

$$
P(w_D=z_D\mid χ=0)=P(w_D=z_D\mid χ=1)=2^{−|D|}.
$$

**Proof.** For each parity there are exactly 2^{K−|D|−1} extensions of z_D among 2^{K−1} equiprobable vectors of that parity. Division gives the result. ∎

Until all K data items are acquired, neither adaptive index selection, their order nor a read result changes χ's posterior. This is proved by history induction: before the next read, its choice is a function of history and seeds without χ; conditional on that choice, the next nonfinal datum is uniform under both parities. Technical operations, costs, messages and errors are functions of already seen data and seeds, and add no information. The final read does determine χ and is permitted.

This includes grouped queries, certificate producers and teams: all new data they acquire are part of collective set D and its charges. Resolving χ before the first high effect requires acquisition of K distinct data items and payment of at least K. Parallelization changes when they arrive, not that total.

For C_0≤b<C_0+K, a complete cheap technical trace cannot have resolved χ before its first X/Y execution: it would already pay C_0+K. That first effect is τ. Without χ, the best success probability is a, by betting X; betting Y has success probability 1−a≤a. The receipt is obtained after the effect and cannot justify it beforehand. Failure executes a violation even if it reveals useful information for the rest of the task.

Thus I1–I3 are verified and, for **all** manifest policies, including those of the centralized envelope,

$$
c\le b\Longrightarrow s\le a,\quad r\ge(a^{−1}−1)s,\quad r\ge(1−a)η.
$$

A policy may acquire all evidence and then abandon to avoid exceeding b. That branch does not deliver H and does not evade the bound. Neither does a read after a first violation, a repair or a cheap failed campaign subsidizing a costly successful one: the ceiling is per execution and V is not erased.

<a id="9-fronteras-tres-pares-y-región-viable"></a>

## 9. Frontiers, three pairs and viable region

For C_0≤b<C_0+K, the following control uses a single agent; the others may remain inactive, retaining their resources and with no new messages.

Toss an independent coin with attempt probability β. If not attempting, execute M with all its gates. If attempting, maintain bet X at all L layers while no prohibition evidence exists, with self-review of each scope. This control neither requests nor receives the evaluator's verdict. In χ=0 all those actions are admissible; in χ=1 a violation is executed, remains recorded, and the result does not count as legitimate success. If a declared query provided a known prohibition, the candidate would be rejected: this construction does not acquire that information. All connectors, reviews and commitments remain present. This produces

$$
c=C_0,\qquad η=β,\qquad s=aβ,\qquad r=(1−a)β.
$$

The informed control acquires all K data items, computes χ and executes its L correct high options with gates, reusing evidence: c=C_0+K≤B,η=s=1,r=0.

By the above bound and those controls, the following conditions are exact in this family:

| Region of target b | Legitimate efficacy s≥p and risk r≤δ attainable at low cost |
|---|---|
| b<C_0 | Impossible for every p>0: even a complete delivery does not fit the ledger. |
| C_0≤b<C_0+K | If and only if p≤a and δ≥p(a^{−1}−1). |
| b≥C_0+K, with sufficient physical capacity | Viable for every 0<p≤1 and δ≥0. |

In the intermediate band, the minimum legitimate risk frontier is p(a^{−1}−1), attained by β=p/a. The technical frontier for η≥h is h(1−a), attained by β=h. If both s≥p and η≥h are required, with 0≤h≤1, the exact condition is p≤a and δ≥max{p(a^{−1}−1),h(1−a)}, with β=max{p/a,h}. This is not announced as a six-dimensional Pareto frontier.

By the §6 corollary, the same criterion p≤a and δ≥p(a^{−1}−1) characterizes e_b≥p,r≤δ in that band **over all physical policies**, without additionally imposing c≤b on their failed or costly branches: the lower bound covers those policies and control β=p/a attains it. This does not turn the costly informed control into a high-e_b control; at b<C_0+K its informed delivery remains outside e_b.

**Three pairs, same parameters.** For C_0≤b<C_0+K,0<p≤a and 0≤δ<p(a^{−1}−1):

| Attainable pair | Policy | Third condition that fails |
|---|---|---|
| Cost and risk | Execute M | s=0<p. |
| Cost and legitimate efficacy | Attempt with β=p/a and maintain X without hidden verdict | r=p(a^{−1}−1)>δ. |
| Risk and legitimate efficacy | Acquire all K data items and use their parity | c=C_0+K>b. |

Inequality r≥(a^{−1}−1)s prevents the triple condition for any other policy. Impossibility is not deduced solely from failure of those three controls.

For any L,N,K there is also a viable threshold configuration by raising b to C_0+K while retaining the same task, world, interface and capacity. Other interfaces with sufficient initial evidence may be viable at lower price; the theorem acknowledges those configurations without treating them as refutations.

**High legitimate efficacy.** Choose a=99/100,p=19/20,δ=1/1000. For any L,N,K and any C_0≤b<C_0+K, all three pairs are attainable and the triple condition is impossible: minimum cheap risk is 19/1980≈0.009596, greater than 0.001. This is an explicit AVG prior, not a 95 % guarantee in each world. K can grow without limit: the safe control's additional cost is K units. Neither quadratic growth nor an extraordinary relative factor over the entire ledger is claimed; C_0 may also grow with L and N.

**Exclusively technical efficacy region.** If η≥h is used instead of s≥p, for 0<h≤1 and δ<h(1−a) the three pairs are likewise obtained: M; attempt with β=h; and informed control. This variant does not count its violating deliveries as legitimate R01 quality.

<a id="10-peor-caso-población-y-tamaño"></a>

## 10. Worst case, population and size

WC requires minimum efficacy and maximum risk over all permitted worlds, retaining the cost ceiling per world. A control meeting those objectives in each world would meet them when averaged with the auxiliary uniform-bit distribution. Applying the proof with a=1/2 gives s_WC≤1/2 and r_WC≥s_WC for cheap policies. For the second inequality, r_AVG≥s_AVG≥s_WC and r_WC≥r_AVG.

The cheap control choosing X/Y with a fair coin and maintaining that same bet at every layer without receiving a normative verdict achieves, in each world, η=β,s=β/2,r=β/2. Therefore the WC frontier is exactly r=p for 0<p≤1/2 in the cheap band, with trilemma for δ<p. The informed control still achieves s=1,r=0 at C_0+K. The 95 % AVG example is not imported into WC.

Bounds hold for any N because they were already proved in the envelope gathering all collective evidence. Population may reduce latency by allocating reads; it cannot produce the missing Kth datum by copying the known K−1. A valid initial certificate or source with that datum does change information and may resolve the difficulty; it corresponds to another θ.

Choosing K=L, arbitrary N and growing L gives an infinite family within the R01 parity control, with additional cost L. Choosing fixed L and growing K studies dependency complexity. Choosing K=1 recovers the shared-binding case with constant price. None of these variations is confused with the false claim that agent or segment count itself determines difficulty.

<a id="11-correspondencia-con-r01-por-cláusula"></a>

## 11. Correspondence with R01 by clause

| R01 clause | Preservation in the theorem |
|---|---|
| §§1.2–1.3: regions and resolving capabilities | Nonempty T and F; sufficient certificates and APIs may move a configuration to F. |
| §1.4: cost, legitimate quality, violation and deadline | Total ledger, legitimate S, irreversible V, explicit T; e_b=s when c≤b. Expected cost is not used. |
| §2.1: fixed mission, known M, hidden I/P | Fixed mandate; safe M; optimum 2L and labels only in the evaluator. |
| §§2.2–2.4: connectors, benefits, geometry | All material transitions declared; zero connector benefit; coincident high means permitted; geometry without normative signal. |
| §2.5: collaboration and collective result | Arbitrary N, one effective ledger and prefix; results are not multiplied by reports. |
| §2.6: queries and producer | Complete operations; local datum per read; global API permitted, production included; no direct evaluator read. |
| §§2.7–2.8: self-review and known rejection | Review→decide→execute; scope expansion acquires evidence with payment; known prohibition rejected; cheap control receives no normative verdict. |
| §2.9: globality and parity | K data items, with K=L as explicit scenario control; complete-history proof, not only a window. Permission semantics of a historical incident are not claimed. |
| §§2.10–2.11: messages, cache and charges | Sources and evidence preserved; producer charged; parity reused without recalculation at every layer. c_v=1<c_e=2. |
| §§2.12–2.13: resources and configuration | Physical cap B, economic target b and horizon; independent parameters declared. |
| §§2.15–2.17: policies and causality | All interface history rules; seeds without hidden world; subsequent technical receipts without hidden verdict; legal positive and negative controls. |

The source retains SC-H as an empirical hypothesis for a finite family. This theorem adds a mathematical claim for the configuration domain and complete policy classes of determined manifests; it does not turn still unexecuted campaigns into results. R01 remains a specification with interface parameters completed per profile, not a single fully frozen simulator.

<a id="12-qué-cambia-respecto-de-la-revisión-anterior"></a>

## 12. What changes relative to the previous review

The shared χ case is not a counterexample to the conditioned R01 trilemma. It only prevents applying the independent-facts-per-segment formula to that profile. Success cases belong to F and are part of the sought result.

The previous family G proof used a cost-1 query for χ. This extension permits that same global fact to be a parity whose producer must acquire K new data items: it retains reuse and proves a growing indispensable-information price. The frontier depends on the actual information contract, not the number of fact copies.

The previous manuscript and its proofs remain available. This document is the main statement over R01; previous formulas are instantiations and tools, not a requirement that every configuration be isomorphic to them.

<a id="13-estado-y-obligaciones-de-revisión"></a>

## 13. Status and review obligations

A symbolic self-performed proof of the general proposition, information cut, R01 family, its controls, AVG/WC frontiers and nonempty regions has been delivered. No new experiment was executed or independent-validation evidence fabricated.

External review must especially attack: (1) manifest fidelity to R01 clauses, including local scopes versus normative relations; (2) any omitted information source, including error responses; (3) preservation of producer charges and initial context; (4) the step from adaptive histories to parity posterior; (5) per-trace ceiling versus physical capacity and compound efficacy; (6) gates, concurrency, repetition and recovery; (7) exact scope of finite convex relaxation. If a capability actually present in the manifest breaks I2 or I3, it is incorporated and the region recalculated: it is not prohibited to save the conclusion.

M16 remains open for independent review. M17 receives this development as evidence without being declared closed by its own author. The oracle/harness must construct observations from a public view and isolate the evaluator before any future finite corroboration. Technologies and natural frequency of these families are subsequent work.

<a id="14-registro-final-de-trabajo-en-desarrollo"></a>

## 14. Final work-in-progress register

| Work | Current evidence | Pending |
|---|---|---|
| Conditioned theorem in complete R01 | General domain, certificate, cut, parameterized family and controls in this document | Independent reconstruction and clause-by-clause fidelity audit. |
| Growing information and cost | K normative data items; price K; reuse and arbitrary N included | Does not imply extraordinary relative factor or temporal law for every network. |
| Pairwise and triple regions | Same parameters; exact family frontiers and viable regions | Does not numerically characterize every R01 generator. |
| Partial experiments | No new execution | Neutral oracle/harness before corroboration. |
| Technologies | Resolving capabilities preserved in the domain | Technology classes, complete costs and region changes after core audit. |

<a id="15-reparaciones-de-la-revisión-de-continuidad-4-de-octubre-de-2026"></a>

## 15. Repairs from continuity review, 4 October 2026

v0.2 corrects the inverse certificate multiplier (§6), aligns send and receive in initial distribution with the table (§7), expands deadline and event cap for those charges, and replaces verdict-dependent control with a persistent bet using only technical receipts (§§7,9,10). It adds range h≤1 to the joint frontier. Bounds and their forms are retained; absolute thresholds shift with new C_0. Report: [audit and continuity](./R01_AUDIT_CONTINUITY_AND_REPAIRS.md). The mathematical extension protocol for technologies is the next phase, still pending. Self-review; M16 is not closed.


<!-- R01_BOT_WORKPLAN_START version="0.4" role="queue-pointer" -->
The current queue is in [WORKPLAN.md](./WORKPLAN.md). This document contributes evidence or criteria within its scope; it does not maintain a second queue. Human escalation and whispering is the first technology in the protocol; repeated reviews are incorporated into each fiche. Independent review, fidelity and integrity retain their open obligations. The previous block is preserved in QUEUE_SNAPSHOT_2026-10-04.json.
<!-- R01_BOT_WORKPLAN_END -->


<a id="precisión-posterior-de-auditoría-y-continuación-por-mecanismos"></a>

## Subsequent audit clarification and continuation by mechanisms

4 October 2026. Pre-effect measurability of the §6 cut is made explicit, as is inclusion of the N-dependent initial charge in B=C_0(L,N)+K; no frontier changes. [Consistency review of the three extensions](./EXTENSION_CONSISTENCY_REVIEW.md). Technology continuation is governed by the [separate protocol](./TECHNOLOGY_EXTENSION_PROTOCOL.md), first isomorphic correspondence and then additional mechanisms. [Human escalation with whispering](./HUMAN_ESCALATION_WHISPERING.md) develops conditioned alert and control contracts; it is neither an integration nor an executed campaign. The base proof, received reviews and M16/M17 retain their scope.
