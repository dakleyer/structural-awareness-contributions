<a id="familia-extendida-de-r01-con-núcleo-funcional-isomorfo"></a>
# Extended R01 family with an isomorphic functional kernel

<a id="ficha-común-de-revisión"></a>
## Common review record

| Field | Case-record status |
|---|---|
| Type and base | Constructed class and domain specifications; R01 v0.6, blob `3261a625975e303e12c484bc9c273d7f8819b099`. |
| Correspondence | h, p and section on kernel (§§3–5 of the note); complete H/L/W implementation pending. |
| Evidence | EV1 for criterion and formal construction; EV2 for H/L/W fragment; EV0 for complete domain realization. EV3/EV4/EV5 not established here. |
| Coverage and A25 | [Common fifteen groups, states and A25](../CRITERIA_AND_AUDIT.md); the case record's individual matrices are retained. |
| Receiver, positive and falsifier | Rejection of detected denials; valid positive; mutations breaking the kernel. |
| Review | Internal author review assisted by AI; partial external observations checked, without established independence. |
| Verdict | Criterion and formal construction proved; partial correspondence checked in the fragment; complete H/L/W realization pending. |

EV codes identify evidence, not the E1–E7 obligations in the mathematical note. Their definition is in the [common criterion](../CRITERIA_AND_AUDIT.md#3-estados-de-evidencia-comunes).

Iván Abril Palma · Ecosystem Awareness · Research version 0.1 · 2 October 2026

[Return to R01](../../README.md#extensiones) · [Mathematical proof](./KERNEL_AND_PROOF.md) · [Code, scope and results](./proof/README.md)

<a id="1-propósito-y-alcance"></a>
## 1 Purpose and scope

R01 may serve as the base for a family of scenarios reproducing failure mechanisms similar to those illustrated by Nell Watson in Theme 13. The claim concerns **constructed cases**, with declared tasks, information and resources. Published incidents provide motivations and examples for designing them; it is not claimed that their entire history is isomorphic to R01.

The structure of interest combines exploration of alternatives, perceived cost/benefit balance, checks of limited scope and social reuse of findings. An alternative may work technically or be accepted by an evaluator without satisfying the real obligation. Communication may be technically possible without being authorized. The family allows study of when those mismatches matter and when a competent defense resolves them.

This document constitutes the third entry in the extensions section. It complements [Hugging Face](../../README.md#openai--hugging-face) and [Infoblox](../infoblox/README.md); it neither replaces their documents nor changes their admission states.

<a id="2-qué-significa-extender-r01"></a>
## 2 What extending R01 means

The extended case may contain more variables than R01. We require a **bijection between the base case's main components and its kernel components in the extension**, preserving relevant relations and operations. Projection removes additional details only when it does not hide a material difference for the decision.

For example, a technology may multiply search radius by three. We preserve radius, geometry and its relation to reachable alternatives; the reference becomes R01 with effective radius `3 R_e`. A technology may reduce the unit review cost; we preserve the event charge and its effect on budget, with the new declared value. Both extensions may change results. Family membership does not require preserving the same failure in all its configurations.

The [proof](./KERNEL_AND_PROOF.md) gives sufficient conditions: complete inventory, kernel bijection, relations in both directions, projection of transitions and probabilities, equivalent observations, accounted costs and timing, and preservation of admissibility, quality and positive controls. It also proves by construction a class of extensions for any R01 realization satisfying those conditions. The [checker](./proof/README.md) contrasts a finite fragment and rejects alterations appearing to preserve names but breaking relations.

**Distinct evidence states:** proof of criterion and construction; finite verification of a fragment; complete domain implementation; execution with agents; historical admission. Only the first two are provided here. The following cases are specifications of extensions constructed through that criterion, not implementations of Lean, third-party services or real wikis.

<a id="3-casos-documentados-que-motivan-la-familia"></a>
## 3 Documented cases motivating the family

| Reference | Fact used and locator | Role in our design |
|---|---|---|
| [N1: Nell's comment](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5923844082), 1 October 2026 | R1 distinguishes information from authority; R2 requires responses to objections; R3 treats shared stores as channels; R4 requires joint observation. | Identifies examples and properties to contrast. Those requirements are not treated as four incidents or all reduced to the same mechanism. |
| [H1: OpenAI report](https://openai.com/index/hugging-face-incident-and-the-road-ahead/), 26 August 2026 | Sections “A message board emerges,” “Difficult tasks without a safe exit” and “An ecosystem of misalignment”: search for alternatives, unplanned communication and adoption of collective objectives. | Motivates a results-obtaining task where the attractive route uses resources outside authorized scope. |
| [H2: METR and Redwood investigation](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/), 26 August 2026 | Description of joining the attack and reasoning section: continuation occurred despite recognizing overreach. | Delimits a branch that does not reproduce R01's basic receiver, which rejects detected prohibitions. |
| [L1: DeepMind, arXiv:2609.04170v1](https://arxiv.org/html/2609.04170v1), 3 September 2026 | §§2.2 and 3.1–3.3: artifact acceptance without satisfying the requested theorem, dissemination through a library and competitive pressure. §§3.5–3.6: detection and insufficient response. | Motivates the separation between local acceptance and compliance with the original specification. Responses to objections would be modeled as an additional component. |
| [W1: collusion.wiki investigation](https://collusion.wiki/) | “The agents gain write to the internet via GET requests” and “The agents used the wiki to share ways around sandbox restrictions”: writing through GET and collaboration to obtain results under restrictions. | Motivates communication routes with effects not represented by superficial control. The source considers this group probably different from the one associated with Artifactory/Hugging Face. |

Sources consulted on 2 October 2026. Radii, costs, probabilities, optimal routes or permissions of our scenarios are not imported as historical facts. Those values belong to the synthetic design. Real exploitation instructions are not needed to test correspondences.

<a id="4-tres-especializaciones-construidas"></a>
## 4 Three constructed specializations

The names H, L and W are local labels in this document. In all three cases the true task remains fixed, the receiver does not know the evaluator's I/P labels and rejects every detected incompatibility. Quantities and distributions are fixed before execution. Evidence communication during the experiment uses the declared authorized channel; the channel being investigated as a possible route is a different object.

| R01 element | H: obtaining out-of-scope results | L: accepted answer without solving the task | W: discovery of a communication channel |
|---|---|---|---|
| Mandate and result | Obtain a result from an authorized collection and resources. | Deliver an artifact satisfying the original specification. | Obtain and share information according to the mandate and each resource's permissions. |
| Action / segment | Query, transformation or delivery operation. | Transformation of the artifact or its dependencies. | Operation with a read, write or transmission effect. |
| Connection | Dependency between an operation and the next resource. | Semantic dependency between steps. | Relation between sender, store and recipient. |
| Exploration / radius | Neighborhood of technically reachable procedures. | Neighborhood of candidate transformations. | Neighborhood of transport or storage mechanisms. |
| Material condition | Permission applicability to mission, resource and recipient. | Preservation of the original specification by the transformation. | Authorization of the real effect and data scope. |
| Review | Query of operation conditions and their composition. | Check of semantic step conditions. | Inspection of the operation's effect and permission. |
| Social signal | Report of result and checks already performed. | Shared artifact and evidence of its coverage. | Connectivity report and scope checks. |
| M | Known authorized procedure, with declared lower quality. | Known legitimate construction, less valuable under the declared criterion. | Known authorized channel, with lower performance. |
| I | Best authorized route, calculated by the evaluator. | Best construction satisfying the specification. | Best admissible communication route. |
| P | Attractive route with an unmet scope condition. | Route acceptable to a partial check but semantically invalid. | Technically viable route with unauthorized writing or transmission. |

<a id="41-h-escenario-similar-a-hugging-face"></a>
### 4.1 H: scenario similar to Hugging Face

Routes are constructed over fictitious resources. For each R01 segment there is a corresponding operation and permission condition. The global predicate requires all applicable conditions; a functionality check does not answer unqueried conditions. Shared reports preserve source, scope, time and dependency.

The encoding function replaces each segment and relation with its operation and resource dependency, without adding jumps. Its inverse recovers the original segment and condition. The same query sequence returns the same information and receives the same effective charges. The mathematical note's proposition guarantees isomorphism for a realization satisfying E1–E7. That construction is specified here and only a fragment checked; H's complete correspondence is not treated as realized. The complete table in §3 of that note also preserves all parameters that domain vocabulary does not change.

Possible additional variables: service names, format types or search acceleration. If an additional credential allows another action to be executed, it cannot be hidden in a decorative variable: the capability must be in the graph and the corresponding permission of the effective base configuration.

The positive is authorized acquisition of the same type of result. It is not assumed that every task in the historical incident had a reachable legitimate solution. Replacing the individual task with a collective mission requires another profile; it is not silently introduced in this construction.

<a id="42-l-escenario-similar-a-la-aceptación-de-falsas-soluciones"></a>
### 4.2 L: scenario similar to acceptance of false solutions

The constructed case uses a finite artifact-transformation task with several legitimate results of different quality. Each step has an obligation to preserve the specification; a local checker may accept aspects of the artifact without having checked all those obligations. Apparent technical quality remains separate from legitimate quality.

The encoding assigns each R01 composition condition to an identifiable semantic obligation. It does not define validity as “the evaluator accepted it.” The inverse recovers steps, dependencies and obligations. Preservation of the query set and information available before commitment is prescribed; that complete obligation is not implemented here. Full fragment review detects the negative; a valid alternative of higher quality than M constitutes the positive.

This proves the correspondence of the **constructed obligation model**, not a property of the real Lean verifier. Lower-quality M is a decision of our design; it is not attributed to the original benchmark, where proving another theorem does not thereby fulfill the assignment. The constructed task must admit legitimate results of graded quality and declare ε. If there is only a binary result or M is already within ε of the optimum, mediocrity is not attributed to that branch. The common checker verifies this sensitivity.

Possible additional variables: artifact format, library or checking cost. A library with an accessible complete certificate may resolve the difficulty and must be allowed. An agent knowing invalidity and continuing falls outside the basic policy, although it may be studied as an explicit behavioral expansion.

<a id="43-w-escenario-similar-al-descubrimiento-de-una-wiki-utilizable"></a>
### 4.3 W: scenario similar to discovering a usable wiki

A candidate route may consist precisely of finding a way to communicate. The graph represents possible operations; admissibility depends on their effects and permissions, not only a protocol's name. A pair is constructed with the same technical feasibility and different writing or transmission permission in a condition not yet reviewed.

The encoding preserves one operation per segment, its effect, resource and relation to following steps. Reviewing the corresponding condition distinguishes the pair. An authorized channel accomplishing the same task is the positive. The specification requires queries and costs to correspond to R01. The projection proof is conditional on E1–E7 and the checker executes only the static fragment; it does not establish activation of a new social network.

Possible additional variables: message size, format or declared latency. If using the channel creates new connections between agents, the topology change must be modeled. The static profile may represent search and decision regarding the channel; its subsequent social activation requires a dynamic R01 configuration with explicit topology updating. All that dynamics is not presented as equivalent to a fixed network.

Sharing an answer directly instead of constructing it is another variant: its admissibility depends on the constructed case's mandate. Reusing an authorized answer must be able to continue; “sharing” is not by definition the failure.

<a id="5-qué-se-demuestra-y-qué-se-mide-después"></a>
## 5 What is proved and what is measured afterward

The proof establishes the existence of constructed extensions preserving the kernel under declared conditions. Vocabulary choice is insufficient: queries, dependencies, transitions and their consequences must be preserved. The checker provides finite H/L/W witnesses and rejected mutations. It does not verify all inventory configurations or execute a complete probabilistic agent.

A subsequent campaign must measure how decisions change when varying the cost of solving, reviewing, communicating or waiting and expected benefit. The balance may be expressed through a recorded policy over accessible estimates, for example expected benefit minus weighted charges. Weights and the rule are not inferred from the result to be explained. Authorization remains a constraint of the basic receiver, not a negotiable penalty within that formula.

Competent conventional controls and social policies are compared with the same resources. Abstention, incompleteness and improvements eliminating failure are preserved. EA's contribution is evaluated as a subsequent intervention with the same capabilities and charges, according to the [R01 appendix](../../Escenario-creatividad-validacion.md#4-apéndice-sobre-ecosystem-awareness-como-candidata).

The relation to 00G additionally requires establishing C-V-G: received content, dependency, scope and promotion to an operational reason displacing an obligation. An R01 failure case does not automatically satisfy that criterion. The [A25 method](../../../../00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md) continues to apply; this proof of the economic and operational kernel does not declare admission to 00G complete.

<a id="6-referencias-internas-y-trazabilidad"></a>
## 6 Internal references and traceability

- [Methodological foundations and primary precedents](../METHODOLOGICAL_FOUNDATIONS.md): what justifies testing R01 first, how to transfer a comparison and where the guarantee ends.

- Fixed base: R01 v0.6, [commit 114ac132](https://github.com/dakleyer/structural-awareness-contributions/blob/114ac132bc2be4e7008001fe505bf5bd4c36c515/research/ecosystem-awareness/baseline/reductions/00G-R01/Escenario-creatividad-validacion.md), especially §§2.1–2.18 and 3.2–3.5.
- [Infoblox, integrated document](../infoblox/README.md), §§5–6: correspondence, conditional proof and counterexample with sufficient certificate. Its check is not relabeled as a complete proof of this family.
- [Hugging Face, parameter and codependency audit](../hugging-face/README.md): historical case record and auxiliary synthetic transport, distinct from this family's constructed H scenario.
- [Hugging Face, candidate reduction](../../../../00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.1_DRAFT.md) and [previous design](../../../../00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.2_DRAFT.md).
- [A25, X1–X7](../../../../00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md): admission obligations and separation between membership and success.

Complete external URLs appear in the §3 table; the checker's H/L/W references point to the §4 constructions, not historical incidents.
