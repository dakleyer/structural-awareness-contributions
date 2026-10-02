<a id="extensión-de-r01-openai--hugging-face"></a>
# R01 extension: OpenAI / Hugging Face

<a id="hugging-face-problem"></a>
## The Hugging Face problem

The motivating incident concerns agents working on assigned tasks, sharing technical findings and coordinating activities beyond their assigned scope. The sources already examined in [H1 and H2](#8-fuentes-y-versión-examinada) document cooperation, scope doubts and different responses to limits. A peer's report that an alternative works is evidence about functionality; it is not automatically permission to use it.

R01 asks a narrower question: can an agent distinguish a useful permitted alternative from an attractive alternative with an unresolved authorization or composition condition, while paying for discovery, review and communication? This is a constructed study inspired by the incident. It does not assume validation cost caused the historical behavior or that every historical task had a legitimate solution.

<a id="hugging-face-scenario"></a>
## How the constructed scenario works

The synthetic model represents a task as linked operations, with owner records and a board through which findings can be represented. The task remains fixed. The following route names are evaluator references; the receiver is not given their labels.

| R01 route | Meaning in the constructed Hugging Face extension |
|---|---|
| M — known permitted procedure | Complete the assigned task through the initial admissible sequence. Its quality may be lower than another permitted sequence. |
| I — ideal permitted alternative | Complete the same task through a better sequence whose operations and dependencies satisfy the mandate. The evaluator computes the best admissible route. |
| P — attractive forbidden alternative | Follow a technically attractive sequence with an unmet permission or composition condition. Useful local results do not make that whole sequence admissible. |

Benefits belong to operations; distances represent which alternatives the search radius can reach. Connectors determine which operations can actually be combined. Checking examines the conditions of that effective sequence, including its dependencies. Sharing a report can supply applicable evidence; relaying the same finding does not create another independent check. These are synthetic assignments, not measurements of the historical agents.

<a id="hugging-face-decision"></a>
## Follow one decision

This is an explanatory walk-through of the proposed scenario, not a recorded historical trace or an executed R01 agent run.

1. The receiver has its task, current position, known next step and remaining budget.
2. It discovers an alternative within its affordable search. A peer may also report an alternative and what was checked.
3. It compares the observed benefit with other discovered options. It has not yet executed the candidate.
4. It checks the relevant operation, connector and preceding or subsequent conditions. Every review and use of received evidence is charged.
5. If it finds a prohibition, it rejects that candidate. If review is incomplete, it may inspect further, retain M, wait or abstain. A completed local review still covers only its declared scope.
6. If its declared policy proceeds, it records the justification, commits and attempts execution. The environment records the real effect and judges the complete route.
7. The trace preserves the receiver, mandate, observations, review coverage, message lineage, budget, decision and effect. Messages must arrive before they influence a decision.

The negative of interest is proceeding when the complete route is inadmissible despite no prohibition having been detected in the receiver's limited view. A receiver knowingly executing after detecting a denial belongs to a different behavioral variant. The positive is completing a better permitted route with sufficient applicable evidence. Both branches must remain possible; a control that resolves the difficulty is retained.

<a id="hugging-face-proof-summary"></a>
## What has actually been checked

The published Python checker constructs the graph and a second representation using board tasks and owner records. It checks whether changing representation preserves routes, connectors, benefits, conditions, observations and selected resource calculations. It checks **288 joint configurations**, including alternative connector and composition settings, and tests counterexamples to incorrect transfers.

That finite check is executed and its [results](./results.json) are available. It does not run a complete probabilistic search campaign, LLM agents or the historical environment. The proposed decision walk-through above is broader than the implemented submodels. The detailed [proof and scope](#4-comprobación-reproducible-ejecutada), [reproduction guide](./proof/README.md) and [remaining admission obligations](#6-resultado-frente-a-a25) follow.

[00G-R01](../../README.md) · [Extensions table](../../README.md#extensiones)

The case examines how a shared alternative, finding or assignment may acquire operational force against the receiver's task and limits. Its connection with R01 allows study of solution search, validation cost and social reuse of findings. The historical economic cause remains a hypothesis; the following audit does not declare the incident reproduced.

| Case-record part | Content |
|---|---|
| Scenario | [Case in words](#hugging-face-problem) · [Routes](#hugging-face-scenario) · [Decision walk-through](#hugging-face-decision) · [Correspondence with R01, part 3](../../Escenario-creatividad-validacion.md#3-familia-00g-escenario-reducido-y-referencia-hugging-face) · [Documented case and previous 00G-HF design](../../../../00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.2_DRAFT.md) |
| Extension justification | [Relations to preserve](#2-qué-debe-conservar-una-extensión) · [Parameters](#3-inventario-de-parámetros-y-resultados) · [Codependencies](#5-codependencias-y-contraejemplos) |
| Validation | [Executed check](#4-comprobación-reproducible-ejecutada) · [A25 criteria and pending items](#6-resultado-frente-a-a25) |
| Code and results | [Reproduction guide](./proof/README.md) |
| Sources and earlier work | [Examined sources](#8-fuentes-y-versión-examinada) · [Trial history](../../../../annexes/00G-HF-DEVELOPMENT-HISTORY-v0.1.md) |
| Status | Partial preservation verified in a synthetic model; complete historical admission and EA differential pending. |

**The base reduction belongs to R01.** Its [00G → R01 foundation](../../README.md#fundamento-y-prueba-de-la-reducción) is consulted from the base scenario. The justification of the HF case extension and its validation are gathered here. Previous 00G-HF documents retain their content and historical location; their R1–R3 runs are not renamed as 00G-R01 executions.

---

<a id="00g-r01--hugging-face-auditoría-de-parámetros-resultados-y-codependencias"></a>
**R01 → Hugging Face parameter, outcome and codependency audit record.**

**Version 0.1 · 2 October 2026 · Author audit assisted by AI.**

[00G-R01 and its extensions](../../README.md#extensiones) · [Earlier base reduction](../../../../00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.1_DRAFT.md) · [Code](./check.py) · [Results](./results.json) · [Coverage register](./coverage.json).

<a id="1-dictamen-y-alcance"></a>
## 1. Verdict and scope

**Complete preservation of R01 in the historical Hugging Face incident is not proved.** This review checks bounded synthetic transport and audits what remains necessary to justify a real extension. It does not turn an analogy, a parameter table or a simulation constructed by us into an incident reproduction.

The audited request is stronger than checking that many agents, many steps and attractive rewards appear: it requires preserving material parameters, their joint relations, decisions and outcomes under comparable resources and observations. That is the criterion used here.

There are three distinct results:

1. **Documentary inventory:** the complete R01 §2.13 inventory, its metrics, analytical cost identities, §3.5 obligations and A25 X1–X7 have been reviewed. The following matrix records partial coverage and pending items, without declaring all factors closed.
2. **Executed check:** a synthetic graph and its representation as tasks, a board and owner records preserve the properties listed in §4. Counterexamples to incorrect transfers are also tested. This is a representation inspired by HF case questions, not the historical environment or a calibrated model of its agents.
3. **Historical admission:** remains open. No complete projection of a trajectory of the same receiver, with mandate, available information, costs, decision and effect, has been established. There is no execution of LLMs, product APIs, attacks, network traffic or EA comparison in this package.

**R01 v0.6 is a research specification without experimental results of its own.** Its conditional formulas can be checked under their hypotheses; SC-H and SC-Ha–SC-He are not already-obtained empirical results that can be inherited. Earlier 00G-HF trials retain their original scopes. The [cross-case audit annex](#cross-case-audit-context) retains the Infoblox comparison.

<a id="2-qué-debe-conservar-una-extensión"></a>
## 2. What an extension must preserve

Preserving isolated variables is insufficient. Two worlds may have identical benefit and distance means and dispersions, but place the best benefits at different positions. A fixed search radius then obtains different results. Material relations between variables must be preserved alongside their marginal distributions.

For configuration θ, world representation F and trajectory projection α, the contract must identify:

- **Task and alternatives:** same mandate; complete trajectories, connections and effects; a legitimate route cannot appear or disappear unrecorded.
- **Semantics:** Adm and J of each effective trajectory; the optimum is solved over all routes, including mixtures. Assuming I by its name is not a check.
- **Observation:** the entire available view, its temporal order, memory, queries, signals and certificates. The auditor's translation keys are not free evidence for the receiver.
- **Joint dependency:** which benefit corresponds to which position, which review covers which obligation, which messages derive from which source and to which receiver each authorization applies.
- **Resources:** charges and schedule, including search, preparation, discard, communication, checking, execution, maintenance and certificate access. L is not equated with tool calls or N with messages.
- **Policies and outcomes:** the same effective decision and control options; q, C, t, a, f, K and e with identical definitions. An additional opportunity or cheaper control may resolve the case and must be admitted.

In the finite model, a bijection of actions and queries with the same information and costs allows a policy and its outcomes to be transported under the same world distribution. **The bijection and that contract are hypotheses constructed here, not verified incident properties.** Transferring a difficulty bound to a more capable system would additionally require showing every policy permitted in the target can be simulated in the source without more information or greater cost. Merely showing an R01 policy can execute in the target is insufficient.

A25 adds preservation of the decision boundary, failure predicate, requirements path and positive control. Its general transfer requires an independent base guarantee; a few positive checker results do not provide that guarantee.

Transferring success relative to the optimum additionally requires preserving J* and ε, or the equivalent threshold J*−ε, cost/deadline limits and all campaign violations. Mapping a route is insufficient if another better route is omitted. The [common criterion and its counterexample](../CRITERIA_AND_AUDIT.md#7-resolución-de-las-observaciones-del-auditor) make this condition explicit.

<a id="3-inventario-de-parámetros-y-resultados"></a>
## 3. Parameter and outcome inventory

This table covers the fifteen R01 §2.13 groups and adds the metrics, hypotheses and EA-example accounting. “Synthetic” means defined and checked within this package's contract. “Historical pending” does not mean absent from the incident: it means this audit has not established the required correspondence.

| Group and R01 reference | What this check covers | What remains to transfer it to the HF case |
|---|---|---|
| Task: L, obligation, principal, result, T · §2.1 | Lengths 2, 3 and 4; fixed task and complete routes in the graph. | Individual mandate record; functional unit for L; verifiable deadline and delivery. Do not assume a legitimate solution in every historical task. |
| Population: N, unit and allocation · §§2.5, 2.12 | N=1,2,4 in a separate query-allocation module; cost and rounds distinguished. | Decision-making population, unequal capability, network, arrivals and departures, schedule and resources per receiver. This module does not execute agents. |
| Input profiles and world selection · §§2.3, 2.13 | Four fixed mean profiles; deterministic grid, without world rejection. | Probabilistic generative family, normalization and comparable selection; not calibrated with HF data. |
| Realized attractiveness of I and P · §2.1 | Verdicts and J of all routes; exact optimum including mixtures. | Distinguish agent expectation, evaluator score and legitimate quality. Do not attribute synthetic values 1–4 to the incident. |
| Heterogeneity, σ and correlations · §2.3 | Preserved mean, centered deviations and half-range σ; σ=0 or 1/4. | Random distribution, more general correlations and causal effect on choice. SC-Ha and monotonicity are not proved. |
| Geometry, D, τ, sides and connections · §2.4 | Synthetic coordinates; τ=0 or 1/2, positive/negative alignment with benefits; explicit connectors. | Historical functional geometry, both sides and displacement of current position. D is fixed per chain, not swept as an independent parameter. |
| Creativity: R_e, effort and sampling · §2.4 | The radius filter from a fixed origin is preserved for each route. | Costly search policy, sequential discovery, memory and radius from changing positions. The auditor's complete map is not attributed to the agent. |
| Composition, witnesses and positives · §2.9 | Conjunction and algebraic parity control, separately; connector conditions; valid routes. | Identifiable historical predicate. Parity is not real permission semantics. The query block uses one uniform witness and is not confused with the entire graph grid. |
| Review: k_a, k_d, order, exit and reuse · §2.8 | Clipped windows with unique coverage; exact early-exit cost under a uniform witness; adaptive queries in the submodel. | Complete historical review policy and its relation to selection, waiting, rejection and budget. Windows are not integrated into a social campaign. |
| Costs: c_e, c_v, ρ and other charges · §2.11 | Cost identities of explicit strategies; allocation module with c_e=2, c_v=1 and accounted communication. | Unit calibration; complete exploration, discard, execution and maintenance ledger. Formulas are not universal bounds. |
| Resources: R, T, v, beta and transfers · §2.12 | Residual query budget; global budget versus per-agent budget; query rounds. | v/beta allocation, execution reserve, full latency, expiry and transfer policy. The complete scheduler is not simulated. |
| Network: topology, s, latency, w_s and dependency · §2.10 | Copies of the same root add no coverage. | Emission and reception dynamics, causal influence, comparable degree, congestion and individual sequence. Counting copies does not model w_s. |
| Policy: selection, tie-breaking, waiting and recovery · §2.15 | All adaptive policies of the small query contract through dynamic programming. | Complete CV-C1/CV-A1/CV-A2/CV-EA; abstention, return connectors and post-effect recovery. The submodel is not the entire R01 family. |
| Volume: Q, coverage, deduplication · §2.11 | Unique coverage and relays; charges of enumerated strategies. | Emergent Q from search and selection, reviewed-proposal rate r_inv and their coupling. Q is not equated with N. |
| Variation: seeds, static and changes · §§2.13–2.14 | Deterministic static grid; two identifier permutations; rejection of inapplicable version. | Held-out worlds, agent random streams and temporal campaign. Checking an incorrect version measures neither expiry nor SC-He. |
| Metrics: q,C,t,a,f,K,e,ε and reliability · §1.4 | Exact Adm/J and exact submodel probabilities; bounded-module costs. | Complete per-campaign vector, censoring, uncertainty, Pareto and statistical comparison. No empirical effectiveness map exists. |
| SC-H and SC-Ha–SC-He · §§1.2, 2.18 | Their premises are audited and controls that may resolve the case are preserved. | Their own execution and inference. They are not theorems established by the base scenario. |
| EA example: S,H₀,h_a,h_m · §4.4 | Only its accounting role is reviewed; EA is not executed. | Costs of preparing, applying and maintaining evidence; comparison with conventional certificates and cache. No observed saving is attributed to EA here. |

<a id="4-comprobación-reproducible-ejecutada"></a>
## 4. Executed reproducible check

<a id="41-dos-representaciones-y-una-malla-conjunta"></a>
### 4.1 Two representations and a joint grid

`check.py` constructs a staged graph and a second representation of board tasks with relations and owner records. Route evaluators of both representations are separate. Correspondence preserves each benefit–position pair, each connector, each condition and operation order. Their names lack visible I/P labels; the auditor retains the translation.

L∈{2,3,4}, σ∈{0,1/4}, τ∈{0,1/2}, two alignment signs, enabled/disabled cross-chain connectors, conjunction/parity and three witness positions (absent, first, last) are crossed. This gives **288 joint configurations**, verified with two identifier permutations. Chain deviations sum to zero and have half-range one before applying σ or τ; the canonical M route position remains zero. That normalization is not claimed to be an observed HF distribution.

Mixed routes are actually enumerated when connectors permit them. Their value and admissibility may change the optimum; the chain initially called “best” is not maintained by decree. Parity is checked as a separate algebraic control and may accept combinations rejected by conjunction.

The radius filter tests preservation of position–benefit pairs and routes accessible under that filter. It does not execute §2.4 search or prove its cost inevitable. Equality of results between representations is a property of the constructed encoding; **it does not prove the incident admits that encoding**.

<a id="42-información-costes-y-recursos"></a>
### 4.2 Information, costs and resources

View pairs include all declared public data and all queried or initially available facts. They differ only in one unqueried candidate-chain condition. An additional tool revealing that condition would invalidate that indistinguishability; it cannot be hidden to preserve the result.

The query submodel grants all candidates. For U∈{2,3,4}, it fixes probability 1/2 for the entirely valid world and 1/(2U) for each world with one invalid condition. With residual budget b≤U, dynamic programming enumerates the contract's adaptive options. It preserves between representations:

- Optimistic accuracy bound: 1/2 + b/(2U).
- Control requiring sufficient coverage: accuracy 1/2 until b=U, and 1 with full coverage.
- Sufficient aggregate certificate with access cost one: accuracy 1 when b≥1.

These are probabilities of this finite decision problem, **not fleet violation rates or HF estimates**. The certificate presupposes already-prepared evidence; its construction is not free. Other common costs lie outside the residual budget and must be charged before transferring the bound to a campaign.

Strategies are also enumerated to check R01 §2.11 identities: c_vNL, c_vNL(L+1)/2 and c_vNL². Early exit with a uniform witness preserves E[reads]=(L+1)/2 and the mixture with valid proposals in §2.9. These are costs of those strategies, not inevitable minima. k_a/k_d windows count unique units and clip endpoints.

In a separate module, U relations are allocated among N reviewers. Shared work is not multiplied by N; rounds may decrease and communication is charged. Fixed global budget and fixed per-agent budget are distinguished. U<L is allowed: neither functional length nor participant count automatically equals pending evidence.

<a id="43-resultado-del-comprobador"></a>
### 4.3 Checker result

The exact record and its counters are in [results.json](./results.json): 288 joint configurations, 576 verifications of route sets and optima under permutations, 33.408 route-outcome and connector checks, 25 complete-view pairs, 36 query-policy values and 918 window-coverage checks. All checks passed.

Configurations and assertions share data; **they are not independent samples or agent trials**. A PASS means the indicated finite properties hold in the declared code and grid. It does not certify the entire document or a technological integration.

<a id="5-codependencias-y-contraejemplos"></a>
## 5. Codependencies and counterexamples

| Relation that matters | Check or result | Limit |
|---|---|---|
| μ,σ ↔ D,τ ↔ R_e ↔ reachable alternatives | The benefit–position pair is preserved. Counterexample: benefits {1,3} and distances {1,3}, radius 1; changing only pairing changes the best accessible benefit from 1 to 3. | Same marginal distributions do not guarantee the same search. |
| Connectors ↔ hybrid routes ↔ Adm,J,I | Enumeration of routes and optima in both representations. | An extension with additional connectors needs the optimum solved again. |
| Predicate ↔ witness ↔ coverage ↔ k_a,k_d | Separate conjunction/parity; windows and complete query. | Do not substitute one predicate for another to obtain the desired failure. |
| Complete view ↔ queries ↔ budget ↔ success | Indistinguishable pairs and exact dynamic programming. | A sufficient certificate eliminates the obstruction; the capability set must be reviewed. |
| N ↔ allocation ↔ total cost ↔ time | 24 separate allocation and budget configurations; U is not duplicated by identity. | Does not model congestion, full schedule or social influence. |
| Q,r_inv ↔ selection order ↔ cost | Identities for declared strategies and mixture. | Historical Q and r_inv have not been estimated; selection may modify them. |
| Lineage ↔ message count ↔ coverage | Relays of the same root still cover one root. | Does not establish a historical receiver counted them as independent evidence. |
| Mandate, recipient, version ↔ reuse | Rejection of evidence with incorrect owner, mission, receiver or version. | Transparent model records; not cryptographic implementation or real-permission audit. |
| Detected denial ↔ decision ↔ effect | The “known denial → execute” transition falls outside the basic receiver rejecting denials. | A variant permitting it must be declared; basic behavior is not inherited unchanged. |
| Existence of M/I ↔ legitimate optimum ↔ mediocrity | If no legitimate completion exists, M and I are absent under the base contract. | Inventing a historical solution or replacing the task with “try” would change the problem. |
| Expiry ↔ reuse ↔ h_m ↔ deadline | Obligation identified; only inapplicable version checked. | Dynamic campaign pending. |
| Policy ↔ execution control ↔ q,a,f,e | Deciding, blocking, executing and delivering distinguished in the audit. | Complete campaign evaluator not yet executed; zero improper effects is insufficient to establish success. |

<a id="qué-impide-una-admisión-automática-del-incidente"></a>
### What prevents automatic admission of the incident

Primary sources support a concrete motivation, but also limits. OpenAI describes an episode where an agent expressed authorization doubts and continued after a peer's GO, and records refusals to participate. This allows questions about attributed authority, without providing a complete normalized historical trajectory here [H1].

METR documents tasks unsolvable through the specified vulnerability, agent cooperation and passages recognizing overreach. It also notes capture and reconstruction limits. A reachable legitimate route therefore cannot be assumed for every receiver, nor every continuation interpreted as lack of information, nor fragments from several agents converted into one witness [H2].

The [earlier historical register](../../../../traversals/00G-HF-HISTORICAL-REVIEW-2026-10-01/EVIDENCE_REGISTER.json) retains six documentary units, without complete operational adjudication. That status is maintained: this audit has neither filled their missing fields nor executed C3 on them. R01 §3.5 expressly excludes from the basic receiver episodes continuing while maintaining recognition of a denial.

Eventual membership of a trajectory in C-V-G would not demonstrate validation cost caused its outcome. Observations or interventions are needed to distinguish that explanation from social pressure, apparent authority, different priorities, interpretation errors and disobedience despite knowing the limit.

<a id="6-resultado-frente-a-a25"></a>
## 6. Outcome against A25

| Criterion | Status of this audit |
|---|---|
| X1 Kernel | Finite transport of submodel relations; complete historical kernel not established. |
| X2 Decision boundary | Defined for the checker. Sufficient record of a concrete historical receiver missing. |
| X3 Failure reflection | Adm/J preserved in the model. Known-denial cases or absence of legitimate solution prevent universal inclusion in the base receiver. |
| X4 Requirements path | Not all S/T obligations certified; requires its own audit. |
| X5 Positive | Model includes legitimate routes, applicable evidence and sufficient certificate. Not equivalent to a paired historical positive. |
| X6 Resources | Explicit costs and budget in limited modules; complete accounting and historical calibration pending. |
| X7 No hidden primitives | Checker declares its operators; complete normalization of an implementation and its historical objects remains pending. |

**Decision:** retain Hugging Face as a historical reference and candidate extension/reduction; admit only expressly checked finite properties. Do not declare total extensibility, incident reproduction, economic causality or an EA advantage closed.

Closing an instance requires selecting a trajectory, verifying mandate and legitimate solution, reconstructing its entire prior view and capabilities, mapping parameters and relations, recording costs and time, checking the positive and executing the competent comparison. If a basic R01 condition does not hold, another variant is delimited and its relation proved again; the base scenario is not silently modified.

<a id="7-reproducir-y-verificar"></a>
## 7. Reproduce and verify

From this folder, with Python 3 and its standard library:

```sh
python3 check.py
```

The script regenerates `results.json`. `coverage.json` records this audit's inventory and states; it is not a certificate issued by the checker. `SHA256.json` records hashes of published files. No credentials or network access are required.

<a id="8-fuentes-y-versión-examinada"></a>
## 8. Sources and examined version

- **R1 — R01 v0.6**, frozen reference for this audit: [complete scenario](https://github.com/dakleyer/structural-awareness-contributions/blob/114ac132bc2be4e7008001fe505bf5bd4c36c515/research/ecosystem-awareness/baseline/reductions/00G-R01/Escenario-creatividad-validacion.md), §§1.2–1.5, 2.1–2.18, 3.4–3.6 and 4.4–4.7. Specification, not campaign results.
- **R2 — Infoblox v0.5**, [document and factor matrix](https://github.com/dakleyer/structural-awareness-contributions/blob/114ac132bc2be4e7008001fe505bf5bd4c36c515/research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/infoblox/README.md), §§5–6; [checker](https://github.com/dakleyer/structural-awareness-contributions/blob/114ac132bc2be4e7008001fe505bf5bd4c36c515/research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/infoblox/proof/check.py).
- **R3 — A25**, [X1–X7 criteria and conditional transfer](https://github.com/dakleyer/structural-awareness-contributions/blob/114ac132bc2be4e7008001fe505bf5bd4c36c515/research/ecosystem-awareness/baseline/00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md), §§4–7.
- **R4 — Earlier 00G-HF work**, [reduction v0.1](../../../../00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.1_DRAFT.md), [steps 1–2 review](../../../../annexes/00G-HF-STEPS-1-2-REVIEW-v0.1.md) and [historical documentary register](../../../../traversals/00G-HF-HISTORICAL-REVIEW-2026-10-01/README.md). Consulted at the same commit as R1; their results are not renamed as R01 trials.
- **H1 — OpenAI**, [The Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead/), 26 August 2026; sections on the incident and ecosystem of misalignment. Reconsulted on 2 October 2026.
- **H2 — METR**, [Brief independent investigation of agents’ behavior, reasoning and collaboration](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/), 26 August 2026; impossible tasks, scope recognition, process and limitations. Reconsulted on 2 October 2026.

No independent review of this package, random incident sampling, blind test or evidence of EA effectiveness is declared.

<a id="ficha-común-de-revisión"></a>
## Common review record

| Field | Case-record status |
|---|---|
| Type and base | Historical with auxiliary constructed model; R01 v0.6, blob `3261a625975e303e12c484bc9c273d7f8819b099`. |
| Correspondence | F and inverse of IDs/routes in the model; complete historical α pending (§§2–4). |
| Evidence | EV1 for query-contract results; EV2 for finite verifications; EV0 for historical correspondence. EV3/EV4/EV5 not established here. |
| Coverage and A25 | [Common fifteen groups, states and A25](../CRITERIA_AND_AUDIT.md); the case record's individual matrices are retained. |
| Receiver, positive and falsifier | Rejection of detected denial; valid routes/sufficient certificate; pairing falsifier with equal marginals. |
| Review | Internal author review assisted by AI; partial external observations checked, without established independence. |
| Verdict | Partial correspondence demonstrated/checked within synthetic scope; complete extension of the historical object pending. |

EV codes identify evidence, not the E1–E7 obligations in the mathematical note. Their definition is in the [common criterion](../CRITERIA_AND_AUDIT.md#3-estados-de-evidencia-comunes).


<a id="cross-case-audit-context"></a>
## Annex: comparison with the Infoblox audit

This annex preserves the earlier comparison for methodological review. The Hugging Face scenario and its synthetic check are described above.

<a id="qué-se-comprobó-realmente-para-infoblox"></a>
### What was actually checked for Infoblox

This contrast is retained as cross-case audit context; it is not evidence of the HF incident. The current comparison uses the [common matrix](../CRITERIA_AND_AUDIT.md#5-matriz-común-de-los-quince-grupos-de-r01-213).

The [v0.5 document, factor matrix and bounded proof](../infoblox/README.md#5-qué-debe-conservar-la-extensión-desde-r01) already distinguishes represented from pending items. Its script checks four chains, verdicts and values, indistinguishable-view pairs, a strict control, query allocation, relays and exact curves of a finite contract. Varying dispersion in that model does not prove its effect on search; allocating queries among N participants does not execute social dynamics.

Therefore, **it would be incorrect to say all R01 parameters and codependencies have already been preserved in real Infoblox**. Pending items include complete probabilistic search, social influence, cost and time calibration, complete executable policies and A25 admission. A sufficient accessible certificate resolves the modeled informational obstacle; none of these tests establishes universal impossibility against available technologies.

