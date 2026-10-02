<a id="núcleo-funcional-isomorfo-y-extensión-parametrizada-de-r01"></a>
# Isomorphic functional kernel and parameterized extension of R01

Research version 0.1 · 2 October 2026

[Family and cases](./README.md) · [R01](../../README.md) · [Finite check](./proof/README.md)

<a id="1-afirmación-que-se-quiere-probar"></a>
## 1 Claim to be proved

An extension may add variables and mechanisms and preserve a kernel isomorphic to an R01 configuration. **The bijection concerns the kernel**, not the extension's complete state. Beyond pairing names, relations, operations, information and observable outcomes in that kernel must be preserved.

We define a deliberately strong sufficient criterion. It is not presented as a necessary condition for every possible relation to R01. A case not satisfying it may require weaker simulation, an expansion of R01 or a different family. It is not admitted through narrative resemblance.

“Isomorphic” is used strictly for the indicated structures. Changing a cost or radius does not necessarily preserve numerical isomorphism with the initial instance. We distinguish:

1. **Representation change:** the same system with another encoding or units, reversibly normalized.
2. **Parameterized extension:** the kernel corresponds to another family instance, with declared effective parameters.
3. **Rule change:** new transitions, authority, information or policy not representable in the base instance. Requires another proof and is not covered by the previous two.

<a id="2-estructura-del-caso-base"></a>
## 2 Structure of the base case

A declared executable realization of R01 is represented as

$$
\mathcal B_\theta=(X,A,E,K,O,\mu_0,c,\ell,\mathsf{Adm},J,F,\Pi).
$$

- `θ`: complete configuration and admissible domains of its parameters.
- `X`: complete state, including world, position, sufficient history, memory, evidence, messages, time and resources. Incorporating history avoids assuming a Markov property that does not exist.
- `A`: typed events of exploration, query, review, sending/reception, commitment, execution, waiting and termination.
- `E(x,a)`: event enablement, including budget, deadline, connections and receiver rules.
- `Kθ(x,a,·)`: transition law conditioned on the event; it is Dirac if the transition is deterministic.
- `O_i`: view accessible to participant i; distinguished from the evaluator's complete state.
- `μ0`: declared initial distribution, without evaluator answers leaked to the agent.
- `c` and `ℓ`: charges by category and elapsed time; update resources and deadline within the state.
- `Adm(τ)`: admissibility of the effective trajectory, with prefix and connections.
- `J(τ)`: technical outcome according to the declared global criterion; agent estimates are distinct objects.
- `F`: outcome predicates: inadmissible execution, insufficient legitimate quality, resource excess, incompleteness. Their thresholds are fixed.
- `Π`: declared policies over observable histories. Knowing a prohibition and executing it is not a policy admitted by the basic receiver.

The family is `𝔅={𝓑θ: θ∈Θ}`. The existence of this notation does not implement R01's pending policies. The following theorem applies to realizations actually satisfying the contract; it does not grant the document that status by writing a formula.

<a id="3-inventario-completo-de-correspondencias-principales"></a>
## 3 Complete inventory of main correspondences

Typed signature `Σ` contains **all** R01 §2.13 groups and operational objects in §§2.1–2.18. Each symbol has a unique counterpart in the extended kernel; its arity and input/output types are preserved. Symbol correspondence is a signature obligation; isomorphism additionally requires bijections on each type's value/object domains and preservation of their relations. State bijection h is induced by those encodings, not a mere table of names. Additional domain names belong to another signature `Σ+`.

| Group / base symbols | Required counterpart in the extended kernel | Relation to preserve |
|---|---|---|
| Task: L, mission, principal, result, T | Domain sequence and obligation; same normalized time unit | Start, completion, authority and deadline; a message does not change the mandate |
| Population: N, tasks, allocation | Corresponding actors and assignment | Actor identity, individual/collective unit and no value duplication |
| Graph: segments, connectors, prefix | Domain operations and dependencies | Adjacency in both directions, continuity and trajectory effects |
| Generative profiles: means, distributions, world rejection | Equivalent generation of operation attributes | Same law under transformation; declare any conditioning change |
| Benefits: μ, σ, deviations and correlations | Technical utility per operation and dependencies | J aggregation and correlations; do not confuse apparent benefit with validity |
| Realized attractiveness: I, P, M and improvements | Routes evaluated in the domain | Admissible M; I obtained by optimizing among admissible routes; P not revealed to the agent |
| Geometry: D, τ, sides, positions and correlations | Domain search coordinates | Distances, orientation and reach from the current position |
| Exploration: R_e, effort, sampling | Capability to discover operations | Radius/effort → observed candidates; discovery law |
| Composition: predicate, witness, distribution | Domain obligations and conditions | Composition admissibility; preserve the declared conjunction/parity/mixed block |
| Review: k_a, k_d, order, exit, reuse | Condition-query window and process | Coverage, rejection of visible denial and evidence currency |
| Costs: c_e, c_v and remaining charges | Exploration, review, execution, message and maintenance ledger | Every event consumes its cost; construction, query or discard is not erased |
| Resources: R, allocation v, beta and transfers | Available and allocated resources | Preservation of charges, allocation and exhaustion rules |
| Social network: topology, s, latency, w_s | Corresponding sending/reception and influence | Emission before reception; origin, dependency and coverage; information does not create permission |
| Policy: selection and auxiliary rules | Decisions over corresponding views | Same effective rule for transferring results; tie-breaking, waiting, rejection, recovery |
| Volume: Q, coverage and deduplication | Counters derived from traces | Q counts unique proposals; copies do not create independent evidence |
| Variation: seeds, versions and changes | Randomness sources, versions and change events | Joint law, stream separation and invalidation of relevant evidence |
| Operational state: memory, remaining budget, position, messages, time | Recoverable kernel state | No material variable remains solely in details removed by projection |
| Observation and evaluation: O, Adm, J, F and thresholds | Domain views, permissions, quality and outcomes | Separation of agent knowledge/evaluator truth and preservation of negatives/positives |

A declared constant, for example N=2, still has a counterpart. An untested parameter is not considered removed or verified. Derived parameters such as I or Q preserve their derivation function; they do not become inputs chosen to manufacture the result.

In H/L/W, the case table replaces operation and obligation names. Other groups in this table are transported unchanged, except for explicit transformations. This is the complete correspondence obligation; the finite checker covers only the subdomain declared in its README.

<a id="4-extensión-transformación-y-proyección"></a>
## 4 Extension, transformation and projection

Let `η` be an additional configuration fixed before the run. A declared transformation produces

$$
\theta^*=\Phi(\theta,\eta)\in\Theta.
$$

The extension has states `Y`, domain operations and additional details `Z`. Its kernel `C` has a typed bijection

$$
h:X_{\theta^*}\longrightarrow C.
$$

In a product construction, `Y=C×Z`. In a more general implementation a surjective projection `p:Y→Xθ*` and a section `s:Xθ*→Y` such that `p∘s=id` suffice. The section proves every base state is representable; by itself it does **not** prove behavioral equivalence.

Representation normalizations must be bijective on declared domains. For example, `r↦3r` is bijective between original radii and corresponding multiples of three; it is not claimed surjective over all integers. `Φ` may identify several technological configurations with the same effective configuration: it need not be bijective because it is not the kernel isomorphism.

<a id="41-obligaciones-e1e7"></a>
### 4.1 Obligations E1–E7

**E1. Signature and relations.** For each typed relation Q and kernel operation f:

$$
Q_B(\mathbf x)\iff Q_C(h\mathbf x),\qquad
h(f_B(\mathbf x))=f_C(h\mathbf x).
$$

Functions with numerical output also use the declared normalization of that output. The double implication prevents new shortcuts, permissions or dependencies from appearing in the kernel without counterparts.

**E2. Events and enablement.** There is a bijective correspondence of kernel event labels, `g`. For every extended state and corresponding event,

$$
E_Y(y,g(a))\iff E_B(p(y),a).
$$

A purely internal operation may be grouped with its macroevent if it certainly terminates, has bounded declared cost/time and preserves every material intermediate observation. An internal loop delaying indefinitely cannot disappear as though nothing had happened. This document's proof uses one extended macroevent per base event, without that additional difficulty.

**E3. Transitions and randomness.** For every measurable set U of base states and each representative y of a fiber:

$$
K_Y(y,g(a),p^{-1}(U))=K_{\theta^*}(p(y),a,U),
\qquad p_*\mu^Y_0=\mu^B_0.
$$

Checking one representative is insufficient. If two values of an extra variable with equal projection produce different future kernel laws, projection loses information and E3 fails. That variable must be retained or a different abstraction proved. This condition corresponds to probabilistic equivalence over state classes; it is inspired by probabilistic bisimulation [M1], without attributing R01's specific proof to that source.

**E4. Observations and policies.** Each actor's normalized views are equal under p, including evidence histories, their origins and conditions. The extension reveals neither `Adm`, I nor facts the base could not know. Transferring a policy result additionally requires

$$
\pi_Y(g(a)\mid H_Y)=\pi_B(a\mid p(H_Y)).
$$

An additional visible datum influencing decisions must have a counterpart in the base observation. If only one controller ignores that datum, equivalence is limited to that controller class, not all possible agents.

**E5. Accounting and timing.** Event costs and timing coincide with those of `θ*` after unit normalization, as do their effects on balance, enablement and deadline. Changing only the monetary unit requires transforming budget and thresholds proportionally. Actually reducing cost with a fixed budget changes the effective configuration and may allow more review.

**E6. Outcome semantics.** For every trajectory within declared scope,

$$
\mathsf{Adm}_Y(\tau)=\mathsf{Adm}_B(p\tau),\quad
J_Y(\tau)=J_B(p\tau),\quad F_Y(\tau)=F_B(p\tau).
$$

If J units or thresholds change, they are normalized first. Admissible trajectories and the optimum among them are preserved, including ties. A sensor measuring only technical acceptance does not replace `Adm`.

**E7. Scope coverage and positive.** Each base trajectory in scope can be lifted to the extension. Each covered extended trajectory projects to a base trajectory. The comparable legitimate alternative, abstention and incomplete endings are included. If only a subgraph or phase is covered, that is declared; other routes may change the global optimum and are not automatically included.

<a id="5-proposición-de-conservación-y-prueba"></a>
## 5 Preservation proposition and proof

**Proposition.** Under E1–E7, paired policies and the same normalized horizon have the same law of projected histories. Consequently they preserve probabilities of predicates F and distributions of quality, cost and time defined in the kernel. The extension's quotient by `y~y' ⇔ p(y)=p(y')` has the behavior of `𝓑θ*` and its relational kernel is isomorphic to that instance's.

**Proof.** Initial equality is E3. Suppose the same history law up to t. E4 assigns equal probabilities to corresponding events in those histories; E2 preserves their enablement. E3 gives the same probability of each successor class, independently of the extended representative. Integrating over histories and events gives equality up to t+1. Induction preserves every finite history within the horizon. E5 preserves accumulated charges and timing and thus stops due to budget or deadline. E6 transports outcome predicates. E7 avoids losing legitimate trajectories or adding runs without counterparts; E1 preserves their relations. This proves the claims. □

Law equality concerns `θ*`, not necessarily `θ`. It does not prove an agent chooses the forbidden route, a defense fails or EA is superior. If the paired arm correctly blocks the route in the base, the extension does too. Transferring a result to another family point requires sensitivity analysis or an additional proof.

<a id="51-construcción-de-una-clase-de-extensiones"></a>
### 5.1 Construction of a class of extensions

For any realization `𝓑θ*`, choose a bijective encoding h of kernel objects and add a state z, for example 50 auxiliary variables. Define an auxiliary evolution law H, normalized for each base transition, and:

$$
K_Y((h(x),z),g(a),(h(x'),z'))
=K_{\theta^*}(x,a,x')\,H(z'\mid z,x,a,x').
$$

The formula is written for discrete states; it suffices for the proposed finite scenarios. We transport enablement, observations, costs, timing and predicates with h. The initial distribution projects to μ0 and `p(h(x),z)=x`. Summing over z', H sums to one; exactly E3 is obtained. The other conditions follow from their definitions and the complete inventory. Each positive-probability base transition has some lifting. By the proposition, this construction is an extension with an isomorphic kernel. □

Extra variables may depend on one another and on the kernel. Their influence on the kernel is admitted through Φ if their technological values are fixed during the episode. If they evolve and alter decisions, costs or permissions, their relevant state must be incorporated into a dynamic base configuration and E1–E7 rechecked. The number of additional variables does not decide admission; preservation of dependencies does.

**Conditional application to H/L/W specifications.** The encoding of operations, obligations, resources and messages in the case table is proposed as h. Domain predicates are respectively scope permissions, semantic preservation and effect authorization. All §3 groups are transported and the preceding construction applied. This proves existence of formal encodings by transport with declared predicates. For an independent H/L/W realization, all its operations, views and relations must still be verified to satisfy E1–E7; the domain label does not prove that adequacy. It does not prove that an API, a real verifier or a historical trace implements those equations: their adequacy requires independent checks. The finite witness uses separate domain evaluators to contrast that obligation and detect alterations.

<a id="52-corolario-para-dos-brazos-comparados"></a>
### 5.2 Corollary for two compared arms

For each arm b∈{EA,C}, E1–E7 must hold in the closed system with its paired policy, observations and all charges. If the same integrable metric m factors through projection and world, effective configuration and horizon are maintained, the proposition equates its expectation per arm. Subtracting yields Δ_Y(m)=Δ_B(m). This preserves a defined contrast, not establishes its positivity. The joint law must also be preserved if the distribution of paired differences is to be transported, not merely their expectations.

The [methodological note §§3–6](../METHODOLOGICAL_FOUNDATIONS.md) develops hypotheses, proof of this corollary, possible approximate bounds and primary precedents. Evaluator-state equivalence does not make the agent's task fully observable; E4 remains indispensable. Citing an MDP homomorphism does not replace that obligation or establish EA implementation or effectiveness.

<a id="6-transformaciones-concretas-y-contraejemplos"></a>
## 6 Concrete transformations and counterexamples

| Change | Condition for admission | What does not transfer directly |
|---|---|---|
| Radius tripled by a technology | Φ assigns `R_e*=3R_e`; reachable operations and search law are those of that instance | Discovery or failure rate of the instance with original R_e |
| Spatial scale change | Multiply coordinates, radius and geometric windows by the same positive constant; inverse normalization | A scale with rounding merging materially distinct positions |
| Cheaper review | `c_v*=λ c_v`, λ>0, with coherent charges and balance; verify `0<c_v*<c_e*` for the basic regime | The same number of queries possible with a fixed budget |
| Review with sufficient certificate | Certificate, production, scope, query and cost represented in the effective base | Difficulty of the case without certificate; it may legitimately disappear |
| Fifty auxiliary variables | E3 holds for all their values and no information leaks under E4 | Future influences hidden by projection |
| New discovered channel | Search and decision represented as actions; any subsequent topology change has a dynamic counterpart | Equivalence of a population with fixed topology to one changing without being modeled |
| Continue with detected prohibition | Does not satisfy the basic receiver; requires expanded behavioral profile | Admission as a mere change of radius, cost or names |

Counterexamples invalidating a projection: merge two conditions with different admissibility; omit a connection; add a permission without a principal; treat two copies as independent sources; erase query cost; reveal the hidden witness to the agent; preserve variable names but change discovery probability; forget a superior legitimate route when calculating I. Keeping the graph drawing does not save these failures.

A λ equal to zero leaves the positive-cost regime, although it may be studied in another family. A reduction mixing parity and conjunction without preserving their verdicts does not satisfy E1/E6 either.

<a id="7-testigo-finito-relación-con-a25-y-límites"></a>
## 7 Finite witness, relationship with A25 and limits

The [checking package](./proof/README.md) verifies encoding, graph, permissions/obligations, quality, geometry, observations and a transition fragment with stochastic exploration, review, evidence communication and commitment. It checks effective parameters and invalid mutations. The check uses exact arithmetic; it is not an automated proof of all R01. The proposition in §5 is an explicit mathematical argument, not a theorem certified by a proof assistant.

| A25 | Obligation contributed by this note |
|---|---|
| X1 kernel | Inventory §3 and E1 |
| X2 decision boundary | Enablement, observation and commitment: E2/E4 |
| X3 same failure | E6, in both directions for declared scope |
| X4 preserved requirements | E1/E2 and applicable-requirements matrix; complete application to each implementation pending |
| X5 positive | E6/E7, legitimate routes and optimum |
| X6 resources | E5, budget, time and full charges |
| X7 no hidden primitive | Signature Σ+, E3/E4 and explicit treatment of new capability |

R01 isomorphism does not replace specific C-V-G conditions or 00G's canonical conformance matrix. R01 may be preserved while falling outside that social subfamily. Historical admission and EA executions retain their own obligations.

<a id="8-fuentes"></a>
## 8 Sources

- [Methodological foundations: primary sources, computational precedents and transfer limits](../METHODOLOGICAL_FOUNDATIONS.md).

- Base and inventory source: [R01 v0.6 at the fixed commit](https://github.com/dakleyer/structural-awareness-contributions/blob/114ac132bc2be4e7008001fe505bf5bd4c36c515/research/ecosystem-awareness/baseline/reductions/00G-R01/Escenario-creatividad-validacion.md).
- Internal method: [A25](../../../../00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md), §§3–6.
- M1: Blute, Desharnais, Edalat and Panangaden, *Bisimulation for Labelled Markov Processes*, LICS 1997. Reference for probabilistic equivalence by classes, not R01 results. https://www.cs.mcgill.ca/~prakash/Pubs/lics97.pdf
- Incident sources and locators: [reference table](./README.md#3-casos-documentados-que-motivan-la-familia).
