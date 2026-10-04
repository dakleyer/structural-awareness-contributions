<a id="r01-y-el-trilema-condicionado-transferencia-y-resultado-local"></a>

# R01 and the conditioned trilemma: transfer and local result

In-depth review · 4 October 2026 · Input a1ec3e24970e2d925745e4fc7a5cd8e6c11c11d5.

[Revised manuscript](./CONDITIONED_TRILEMMA.md) · [Audit](./CONDITIONED_TRILEMMA_DEEP_AUDIT.md) · [Intact source scenario](../Escenario-creatividad-validacion.md) · [M10 contract](./partial-experiments/historical/M10_RECONCILED_CONTRACT.json) · [M02 catalog](./partial-experiments/historical/M02_CONJUNCTION_FIXTURE.json).

<a id="1-tres-objetivos-de-extensión-diferentes"></a>

## 1. Three different extension objectives

1. **Existence within R01:** prove a compatible configuration subfamily where all its observable policies face the trilemma, together with viable regions. Constructing and auditing that subfamily suffices; translating every R01 configuration is unnecessary.
2. **Conditioned transfer to an instance:** verify the hypotheses for that problem and derive its bound. An analogy between names or selection of traces does not suffice.
3. **The same F frontier for all R01:** not valid. R01 permits shared facts, reuse, initial information, certificates and other interfaces. The §5 counterexample shows specifically why q=2^{-(d-k)} cannot be transported to all its profiles.

Point 1 is the mathematical objective consistent with the user's thesis. It does not require proving impossibility in all configurations, which would include viable regions. Source scenario SC-H (§1.2) formulates an empirical hypothesis over an evaluated finite family; proving a bound for all policies of a supplemental contract does not change that specification without an explicit revision.

<a id="2-la-dirección-que-transfiere-imposibilidad"></a>

## 2. The direction transferring impossibility

For each instance D of a subfamily, there must be a model M and a policy transformation Φ, common to worlds, observable and applicable to **every** relevant policy of D, such that

$$
\mathrm{Good}_D(\pi)\Rightarrow\mathrm{Good}_M(\Phi(\pi)).
$$

If M admits no good policy, neither does D: a good policy in D would produce a contradiction in M. After normalizing units and laws, sufficient conditions are C_M≤C_D, ρ_M≤ρ_D and e_M≥e_D. An exact frontier additionally requires executable controls in D attaining the bound. A bijection of all algorithms is not required.

Implications “objective satisfied in M ⇒ objective satisfied in D”, proposed in a received audit, serve to construct attainability, but do **not** suffice to transfer impossibility. Nor does writing Π_D⊆Π_M suffice without constructing a representation of observations, costs and effects: these are policy classes over different interfaces.

<a id="3-matriz-concreta-de-correspondencia"></a>

## 3. Concrete correspondence matrix

The following labels correspond to complete reading of the scenario, catalog, contract and M02 code; they are not equivalent to external review. Probability symbol a in the manuscript does not redefine a, the R01 completion measure; different types are retained.

| Element | Correspondence with R01 / M02 | Verdict |
|---|---|---|
| World and obligation | R01 §2.1 fixes mission and admissibility. M02 uses χ=0/1 and active(m)=1, active(x)=1−χ, active(y)=χ. | EQUALITY proved for the M02 rule; other rules need a contract. |
| Routes and connectors | M02 has 3 m/x/y layers, 24 zero-benefit connectors and all 27 compositions. | EQUALITY of the defined graph; not every R01 generator. |
| Quality | M is worth 3; admissible optimum is 6 in both worlds; ε=0 requires three high nodes. | EQUALITY by sum and admissibility rule. |
| Independent facts per segment | M02 repeats the same χ in all three steps; R01 permits dependencies. | NO EQUALITY. The F frontier with d=3 does not transfer. |
| Prior information | Setup gives technical map and M evidence, without χ. | EQUALITY in M02; initial evidence of another profile may resolve the problem. |
| Informative read | query_state/check_certificate cost 1 and reveal the single χ. | Local EQUALITY; they do not represent three independent reads. |
| Other queries | explore, query_mandate, review, decide, reuse without acquired fact, wait and rejections do not reveal χ. | Local EQUALITY of responses/charges before the first high effect. |
| Subsequent observation | First X/Y effect reveals χ; executing M does not. | Local EQUALITY; subsequent steps must exploit that information. |
| Risk | v_exec is irreversible and records every material violation. ρ=P(v_exec=1). | EQUALITY with M02/M10 and R01 §1.4; risk is not identified with harm. |
| Technical η | Probability of technically sufficient route. R01 separates raw finish/J_parcial from legitimate value. | SUPPLEMENTARY measure; not equality with R01 e or q. |
| Legitimate σ | Probability of sufficient-quality delivery without any process violation. | Event EQUALITY with the quality/legitimacy/deadline part of e; budget requires the next row. |
| Success e | R01/M10 also requires C_traza≤R and deadline. | EQUALITY with manuscript σ_R, not σ without budget. Both coincide in policies with C_max≤R. |
| Cost | R01 C is per-execution ledger; manuscript C(π) is its maximum over executions. | Explicit BOUND/AGGREGATION, not equality of objects. Not replaced by expected cost. |
| Capacity and desired cost | R01 R is physical cap; manuscript B is physical cap and R economic target. | Necessary DISTINCTION. With B=R, the costly pair is not executable in that same profile. |
| Policies | M10 defines all observable rules with gate and known rejection, and independent mixtures; M02 limits to 32 events. | Local coverage through complete history; not only policies implemented in run(). |
| Self-review | Each position needs review→decide→execute. Layers do not repeat and a local certificate does not replace another. | Local EQUALITY; fixes minimum completion cost, not repeated global reviews. |
| Deadline/cap | T=32, H=32; controls use 10/11 time units and 11/12 requests including stop. | Locally realizable BOUND; not general latency law. |
| N, geometry and signals | M02 uses N=1 and paid technical prior. R01 permits other networks and tasks. | PENDING ASSUMPTION for a distributed or search extension. |
| Certificates, pooling, recovery | In M02 only the declared catalog; R01 admits other profiles with their own charges and information. | PENDING ASSUMPTION to expand the result. They are not excluded from R01 to preserve difficulty. |

Exact sources: scenario §§1.2,1.4,2.1–2.3,2.6–2.8,2.11–2.15; M10 contract §§2–4; M02 catalog `operations`, `gate_rule`, `resource_rule`, `reuse_rule`; code `Episode.request` and `Episode.result`. Code was read, not executed for this review.

<a id="4-teorema-directo-para-el-contrato-m02-con-todas-sus-políticas"></a>

## 4. Direct theorem for the M02 contract, with all its policies

<a id="41-capacidad-física-y-umbrales"></a>

### 4.1 Physical capacity and thresholds

Use the static M02 catalog without initial χ information, with physical capacity B=12, T=H=32 and ε=0. This is physical profile easy_budget without changing its bytes. Introduce a cost target R_goal with 11≤R_goal<12. C is the ledger maximum; source physical capacity remains named R_alloc=B. They are different variables.

The frozen prior is P(χ=0)=P(χ=1)=1/2. A variant with prior a/(1−a) is another θ and must be declared; the fixture is not retrospectively altered.

Π contains all policies over observable catalog history, respecting gate and known prohibitions, up to H. H_tec means complete delivery of technical value 6; V records any violation and σ=P(H_tec∩¬V). For policies with C_max≤R_goal, σ coincides with the quality/deadline/cost success indicator corresponding to target R_goal.

<a id="42-cota-y-prueba-exhaustiva-por-clases-de-eventos"></a>

### 4.2 Bound and exhaustive proof by event classes

Every complete route requires setup, cost 2, and one review, decide and execute per each of three positions, cost 1 each. No other operation produces the necessary local certificate or commitment. After execute the certificate is consumed and the layer changes; reuse produces no new one. Therefore every complete path pays at least 2+3·3=11.

A query_state/check_certificate before completion adds at least 1. Under C_max≤R_goal<12, a complete branch cannot have paid for that query. Setup and explore show the same map in both worlds; query_mandate the same rule; review/decide the same geometry and gates without χ; reuse preserves only what has been seen; wait/stop and syntactic or resource rejections do not distinguish worlds. An execute of M returns true binding in both and does not reveal χ. These classes exhaust the catalog.

A quality-6 delivery requires a first still unknown high execution. Before it, the policy uses a history with the same law in both worlds. Let u be the probability of entering that first unknown bet. In the balanced prior its success probability is 1/2. First violation occurs with probability u/2 and every legitimate success requires that success. Thus

$$
\sigma\le u/2\le1/2,\qquad
\rho\ge u/2\ge\sigma,\qquad
\rho\ge\eta/2.
$$

The last inequality uses η≤σ+ρ. Queries on failed branches, phases and stopping contribute no fundable successes and do not invalidate the bound. In WC, per-world guarantees imply guarantees under the balanced prior.

<a id="43-controles-y-frontera-local-exacta"></a>

### 4.3 Controls and exact local frontier

With probability β, execute X at the first position, observing the receipt after the effect. If admissible, χ=0; if inadmissible, χ=1. At the next two positions execute respectively X or Y according to that already acquired fact. Maintain review→decide→execute at each position. The first violation is not erased, but technical completion occurs without violating a known prohibition. With probability 1−β execute M three times.

In AVG: C_max=11, η=β, σ=β/2, ρ=β/2. For WC, use a fair coin for the first X/Y option and then the correct option according to the receipt; those rates hold in every world. These controls are legal symbolic constructions; it is not claimed that historical wrapper run() implements them or that they have been executed now.

Therefore for 11≤R_goal<12:

$$
\exists\pi:C_{max}\le R_{goal},\eta\ge h,\rho\le r
\iff r\ge h/2;
$$

$$
\exists\pi:C_{max}\le R_{goal},\sigma\ge p,\rho\le\delta
\iff p\le1/2\quad\text{and}\quad\delta\ge p.
$$

For R_goal=12, paying for the χ query before the first effect and maintaining all gates achieves η=σ=1, ρ=0 and C_max=12. For R_goal<11, there is no sufficient delivery under C_max≤R_goal. These conditions are exact within the catalog for balanced AVG and WC, not extrapolation from 27 routes or historical checks.

<a id="44-no-vaciedad-del-trilema-legítimo-local"></a>

### 4.4 Nonemptiness of the local legitimate trilemma

For any 11≤R_goal<12, 0<p≤1/2 and 0≤δ<p:

| Pair | Control within the same capacity B=12 | Result |
|---|---|---|
| Cost–risk | Only M | C=11≤R_goal; ρ=0; σ=0<p. |
| Cost–legitimate success | Adaptive control with β=2p | C=11≤R_goal; σ=p; ρ=p>δ. |
| Risk–legitimate success | One query and admissible route | C=12>R_goal, executable under B; σ=1; ρ=0. |

No other policy achieves all three by the universal bound. This is a nonempty parameterized region, not a single execution. With R_goal=12 all three are compatible. The mission has not been changed and competent controls have not been hidden.

**Historical profile limit:** its original thresholds p=3/4, δ=1/4, with R_alloc=11, do not give the nonvacuous three-pair trilemma. The cost–success pair is already impossible because σ≤1/2; moreover risk ceiling δ=1−p is redundant with that success. This limitation was already recorded in M10. The above thresholds in this section are a declared additional analytical contract, not a fixture correction.

If B=R_goal=11 is retained as physical cap, the costly control cannot execute there: it retains its role as a solution of the same problem with capacity 12. It is not labeled a permitted policy under cap 11. This distinction is essential for transferring pairwise language.

<a id="45-indicador-de-éxito-de-r01-sin-coste-máximo-global"></a>

### 4.5 R01 success indicator without global maximum cost

For any policy executable under B, σ_goal=P(H_tec∩¬V∩{C_traza≤R_goal}) counts legitimate deliveries within the economic target. Branches counted in σ_goal cannot pay for the query even if other branches spend 12. The same first-bet argument gives σ_goal≤1/2 and ρ≥σ_goal. Thus the bound may also be expressed as a per-campaign success condition in the style of R01 e. σ_goal is not identified with σ in policies spending more than R_goal in any branch.

<a id="5-contraejemplo-a-la-extensión-indiscriminada-de-la-frontera-f"></a>

## 5. Counterexample to indiscriminate extension of the F frontier

In documented M02, L=3, C0=11, c=1 and a single read reveals the shared binding. At budget 12, querying χ and choosing X/X/X or Y/Y/Y gives legitimate quality 6 and zero risk. Gates remain present.

If F were incorrectly applied with d=3 and k=1, q=2^{-2}=1/4 and, for η=1, risk bound 3/4 would follow. This is incompatible with the above zero-risk control. The precise cause is that the three bindings **are not independent**: they are copies of the same χ. It does not refute F; it refutes applying its formula to that R01 profile.

R01 §§1.3,2.11 precisely permits reuse of a valid fact in applicable scopes. The extension cannot be repaired by prohibiting that reuse. Dependencies must be modeled or an appropriate single-fact bound used, as in §4.

<a id="6-qué-falta-para-una-familia-r01-con-dureza-creciente"></a>

## 6. What remains for an R01 family with growing hardness

<a id="61-una-familia-r01-parametrizada-que-ya-puede-definirse-y-probarse"></a>

### 6.1 A parameterized R01 family that can already be defined and proved

Existence of a trilemma within a subfamily does not require information cost to grow with L. Shared-binding family G, distinct from F, can be constructed for every L≥1:

- One task, N=1, static equiprobable world χ∈{0,1}, fixed mission and principal. Three nodes per layer: M_i with benefit 1 and X_i/Y_i with benefit 2, i=1,…,L. Complete connectors between consecutive layers and zero benefit; terminal connector included. Admissibility is the conjunction of active(m)=1, active(x)=1−χ, active(y)=χ in all effects.
- Fixed geometry: M at the reference, X/Y distance 1 left/right; accessible radius 1, zero dispersion. Derived I/P have mean 2, control case admitted in R01 §2.3; reward and position do not reveal χ. M is known and its evidence paid.
- The profile starts with an already acquired and paid technical prior favorable to all controls. To avoid a free technical list, preparation 2 and exploration of all 2L candidates at c_e=2 per candidate are charged: setup cost 2+4L and duration 1+2L. Its ledger retains that breakdown. χ is not discovered in that preparation. This is initial context of this profile, not a mandatory strategy imposed on all R01 or a claim of search optimality.
- Every material position requires review→decide→execute, each operation at cost and duration 1. Local review is c_v=1<c_e=2. It does not reveal the global binding; it checks node, connector and its own scope. Normative queries may expand information without replacing that gate. Self-messages create no information. There are no other participants or initial sources.
- Global evidence of the single χ costs 1 in total: acquisition/production and applicability checking are included in that declared price. It suffices for all positions while valid. Repurchasing it L times is not forced.

The full operation contract follows. Responses and prices before learning χ do not depend on its value except in the three declared informative operations.

| Operation | Cost / duration | Transition and information |
|---|---|---|
| setup | 2+4L / 1+2L | Once, initializes technical prior, M evidence and version; repetition neither obtains χ nor restarts the process. |
| explore | 2 / 1 | Inspection of an already discovered candidate; existing geometry and benefit, without χ. |
| review | 1 / 1 | For next-layer node and valid connector: local certificate of exact scope; clears pending. Different-layer scopes do not substitute for each other. |
| decide | 1 / 1 | Requires that certificate and rejects an already known prohibition; creates commitment of the same scope. |
| execute | 1 / 1 | Requires certificate/commitment, position and connector, and known rejection. Produces effect, advances layer, consumes both and delivers binding_active_after_effect. If X/Y, reveals χ; if M, does not. V is OR of every violation. |
| query_state / inspect_binding / check_certificate | 1 / 1 | Returns exact χ, origin, scope and version. Price includes the entire producer and use; it does not replace geometric review. |
| query_mandate | 1 / 1 | Fixed rule and principal, without χ activity datum. |
| reuse / self-communication | 0 / 0 | Only facts/certificates from history; alters neither χ, V nor position and certifies no new scope. |
| wait | 0 / 1 | Static world; creates no evidence. |
| stop | 0 / 0 | Terminates; does not turn an incomplete route into delivery. |

State is (layer, prefix, certificate, commitment, χ_acquired_or_unknown, ledger, clock, counter, V, terminated). The environment's χ is not directly accessible to the policy. IDs and payloads belong to the finite catalog; there is no reset operation or external source. A request exceeding capacity/clock/cap is rejected without effect or hidden datum and consumes a request. A syntactic/gate error likewise does not reveal χ; except prior resource rejection, it pays its indicated charge. Those states, transitions and responses define the class of all history policies, not an algorithm list.

**Initial decision-point state:** before π's first choice, automatic setup has already occurred. Empty prefix, first layer, empty certificate and commitment, unknown χ, V=0, incurred cost 2+4L, clock 1+2L and counter 1 for the macro request. Production breakdown is part of that cost, not a duplicate charge. No policy from this context can retrospectively avoid that expenditure or receive the prior without it. Optimization of an earlier process acquiring another prior is another configuration and is not declared covered by this theorem. Repeated setup produces the same manifest while paying its charge again, without resetting counter, cost or V.

Fix ε=0, C0(L)=2+7L, physical capacity B=C0(L)+1, T=H=5L+4 and cost target C0(L)≤R_goal<C0(L)+1. The horizon covers even the preparation breakdown plus L gates, one read and stop. M02 H=32 is not retained as L increases.

**Theorem G.** For any L and these parameters, for all executable observable policies of G, under C_max≤R_goal, σ≤1/2, ρ≥σ and ρ≥η/2 hold. The §4 frontiers are exact, replacing 11 by C0(L) and 12 by C0(L)+1. For 0<p≤1/2 and 0≤δ<p each pair is attainable and no policy achieves all three. At R_goal=B one read obtains σ=η=1 and ρ=0.

**Proof.** Every complete path pays already incurred technical setup and 3L gates/materials, at least C0(L). A new global fact adds 1, so it does not fit a delivery branch within R_goal<C0(L)+1. All other pre-effect responses while unknown are identical in both worlds by the catalog. Quality-2L delivery requires the first high execution with success probability 1/2; σ≤u/2 and ρ≥u/2 as in §4. The control attempts with probability β, bets at the first step and adapts the rest to the receipt without erasing V or executing an option known to be forbidden. C_max=C0(L), η=β, σ=ρ=β/2. Only M proves cost–risk; β=2p cost–success; a prior read proves risk–success at C0(L)+1. Controls respect horizon and capacity. ∎

This is a formal instantiation of the R01 inventory: task and population (§2.1/2.5), chains/connectors (§2.2), coincident means and declared dispersion (§2.3), geometry and radius (§2.4), information separation and producer charge (§2.6), gate and receipts (§2.7/2.8), ledger c_v<c_e and reuse (§2.11), capacity/horizon and aggregation unit (§2.12). The paid technical prior is favorable and declared as in M02, not a complete discovery campaign. The profile uses a closed catalog within the inventory; another API or initial evidence defines another profile. F's per-segment independence is not imposed on this problem.

There is thus a formally specified family of R01 configurations with all its observable policies and arbitrary sizes exhibiting the **conditioned** trilemma. Independent review of the proof and compliance with those clauses remains pending. It is not claimed that all R01 has this profile, information additional cost grows with L or it occurs at a particular frequency.

**High-reliability AVG variant.** Changing only the prior of the single χ to P(χ=0)=a≥1/2 retains G's construction and changes the local bound to σ≤a and ρ≥(a^{-1}−1)σ. The adaptive control gives η=β, σ=βa and ρ=β(1−a). With a=99/100, p=19/20 and δ=1/1000, any L has each pair attainable and triple impossible at R_goal<C0(L)+1; minimum cheap risk for σ≥p is 19/1980. This is another declared profile, not the frozen M02 prior or a 95 % WC guarantee.

<a id="62-dureza-informativa-creciente-obligación-diferente"></a>

### 6.2 Growing information hardness: a different obligation

The above local proof demonstrates neither growing cost in L nor extraordinary severity. For a family with L independent facts an R01 instantiation is needed specifying, beyond the graph:

1. A set of distinct resources/bindings per segment, distribution and initial evidence; geometry and rewards not leaking their values.
2. The full catalog of queries, mandate, state, certificates and messages; total production and new-fact cost, including every combined query.
3. Gate and counter of irreducible material work C0; reusable certificates and self-review without double charging.
4. History and effects for each operation; every legitimate way to deduce a binding must remain in the simulation, not only queries chosen by the author.
5. Transformation of **all** profile policies into F's envelope with threshold preservation; executable controls proving the other direction at the frontier.
6. Correct events of legitimate quality, per-branch cost/maximum cost, deadline, recovery and physical capacity, preserving original metrics.

R01 syntax permits profiles such as distinct facts, but that complete contract and its coverage proof are not yet closed. Family G proves existence with a shared binding and constant additional cost; it is not used to declare F's growing hardness or transport W's quadratic bound without proof.

<a id="7-dictamen-de-transferencia"></a>

## 7. Transfer verdict

| Claim | Self-review verdict |
|---|---|
| General transfer proposition by objective preservation | Proved by contradiction with the correct direction; its hypothesis is not taken as verified. |
| Universal policy frontier for the observable M02 contract | Direct derivation in §4, with explicit catalog, cost and controls; independent review pending. |
| Nonvacuous local three-pair trilemma | Proved in the declared analytical contract B=12 and R_goal<12, with thresholds p≤1/2, δ<p. |
| Existence in a parameterized R01 family | Family G defined and proved in §6.1, with paid technical prior, closed catalog and arbitrary sizes; external review pending. |
| Original M02, p=3/4, δ=1/4, cap 11 | Impossibility of adequacy; not proof of nonvacuous trilemma for all pairs. |
| Same F formula for all R01 profiles | Refuted as indiscriminate extension by the shared binding. |
| Growing information-hardness family integrated into R01 | Construction and coverage pending; not confused with existence already proved in G. |
| Theorem of all R01 and its six-measure Pareto | Not established; not replaced by a similarity matrix. |

The [plan](./WORKPLAN.md) records M17 in development through these deliverables and retains M16 open. No new scientific tests have been executed. Previous JSONs, fixtures, checkers and results are not modified.


<a id="8-desarrollo-posterior-trilema-condicionado-en-el-dominio-completo-de-r01"></a>

## 8. Subsequent development: conditioned trilemma in the full R01 domain

The sought extension does not require the same F frontier for every configuration. A shared binding, resolving API or sufficient certificate may create a viable region: that is part of the conditioned result, not its refutation.

The [R01 theorem](./R01_CONDITIONED_TRILEMMA_THEOREM.md) now provides: a certificate for any manifest in the domain; an information cut for all its policies; a family with L layers, N agents, global dependency of K data items and production price K; controls for all three pairs; AVG/WC frontier and viable families. K=L instantiates the R01 global parity control and proves growing information hardness while retaining reuse and collaboration. It does not require an independent binding at each segment as in F. This new evidence replaces the obligation to construct a growing family listed as pending in §§6.2–7; independent reconstruction remains pending.

The [self-review](./R01_CONDITIONED_TRILEMMA_REVIEW.md) does not count as external validation. The family retains an acquired and paid initial technical context; another preparation or initial information is another configuration in the domain. Numerical characterization of every interface or the six-measure Pareto frontier is not promised. The original document and tests are not altered.
