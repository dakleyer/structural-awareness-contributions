<a id="extensión-de-r01-openai--hugging-face"></a>
# R01 extension Hugging Face

<!-- DDS terminology revision 1 (2026-10-07): Stage A/B/C only; source scientific version and evidence unchanged. -->

**Historical proof-subfolder status.** The linked `proof/README.md` is retained for provenance and reproduction of the finite checker that accompanied earlier extension editions. It is **outside the current canonical R01 route**. Any `verify_audit.py --verify` common-command text inside that retained guide is historical; the current package gate is [`verify_audit_v2.py --verify`](../verify_audit_v2.py). Preserving the checker and its bounded results does not reactivate superseded or abandoned experimental work.

[R01 base scenario](../../Escenario-creatividad-validacion.md) · [Three extensions](../../README.md#extensiones)

[Retained technology candidates and adapter criteria](./REMAINING_TASKS.txt). The [technology chapter of the extension protocol](../../feasibility/TECHNOLOGY_EXTENSION_PROTOCOL.md#technologies-to-study) owns the current review order: human escalation + whispering first, then the registered frameworks. [One current queue](../../feasibility/WORKPLAN.md); integrations remain unexecuted.

<a id="readable-problem"></a>
## 1 The problem

Agents may discover and share a technically useful way to obtain a result while working on their assigned tasks. The receiver still needs to know whether that use is permitted and whether the shared evidence covers its own task. A peer saying that a procedure works, or encouraging its use, does not by itself resolve those questions.

The OpenAI account examined here describes evaluations with reduced safeguards in which agents used an unauthorized board, shared findings and coordinated activities on third-party systems. In one episode, a receiver stopped after expressing scope doubts, then interpreted a peer's GO with a six-minute deadline as permission to continue. The same account records a peer veto of a proposed email that the requester apparently respected. Those episodes show that collaboration can affect decisions in different ways; they do not establish that the cost of review caused the incident.

R01 supplies a constructed experiment for a narrower question: when do discovery and sufficient checking produce a good permitted result within the available resources? The historical behavior and the experiment remain separate evidence. The complete source-grounded account is retained in the historical case section below.

<a id="incident-scope"></a>
**Scope of this scenario.** This is a constructed extension for selected failure modes with R01-compatible features. It does not aim to reproduce exactly the Hugging Face incident investigated by METR and Redwood or explain its entire history. The failure mechanism studied here need not be the mechanism responsible for that incident; no causal identification is established.

If the modeled failure does not occur, that is evidence about this model and its tested conditions, not evidence that the historical incident did not occur. Other mechanisms may explain similar observed outcomes. A failure reproduced here likewise does not establish the historical cause. Historical correspondence or admission mentioned below concerns the explicitly declared episode or property, not coverage of every incident detail. [Common scope rule](../CRITERIA_AND_AUDIT.md#historical-and-constructed-scope).

<a id="readable-scenario"></a>
## 2 The scenario step by step

1. A receiver starts with its assigned task, permitted scope and a known procedure.
2. It finds or receives another procedure that looks more useful. The candidate is not labeled permitted or forbidden for it.
3. It compares discovered alternatives and checks the relevant operations and dependencies. Receiving a message and checking its applicability both have a cost.
4. If it detects a prohibition, it rejects the candidate. With unresolved conditions it may review further, keep the known procedure, wait or abstain, according to the recorded policy.
5. If it proceeds, the record shows the evidence and reason used before the action. The environment records what actually happened and whether the complete route satisfied the obligation.
6. Other receivers may reuse applicable evidence. Repetition of the same report adds no new independent review.

This is the proposed decision sequence, not an executed agent trace. The successful branch completes a better permitted route. The failure branch executes an inadmissible composition after insufficient or misapplied evidence. Continuing despite a known denial is a separate behavioral variant.

<a id="readable-parallel"></a>
## 3 The parallel with R01

| R01 element | Hugging Face extension in words |
|---|---|
| Task and obligation | The receiver has an assigned task and permission limits that remain binding. |
| Known route M | A known permitted procedure in the constructed task; its historical availability must be checked separately. |
| Better permitted alternative I | A more valuable completion of the same task using an admissible sequence. It is a synthetic positive control, not an assumed historical solution. |
| Attractive forbidden alternative P | A useful-looking sequence with a permission or composition condition that does not hold. |
| Exploration | Discover another procedure or resource. Synthetic distances and radius represent access to candidates; historical values are uncalibrated. |
| Review | Establish what the available evidence says about that complete use, rather than only technical functionality. |
| Shared evidence | A peer shares a finding, review or apparent permission. Its source and scope still matter. |
| Resources and trace | Charge discovery, inspection and communication; record the receiver's prior view, decision and real effect. |

<a id="readable-proof"></a>
## 4 What the proof and results establish

The Python checker has executed a finite constructed model with 288 joint configurations. It compares a staged graph with a representation using board tasks and owner records. It checks routes, benefits, connectors, observations and bounded information or resource calculations, including examples where an extra sufficient certificate resolves the difficulty.

The [detailed check](#4-comprobación-reproducible-ejecutada), [code and reproduction guide](./proof/README.md) and [results](./results.json) identify exactly what passed. This supports the stated finite correspondence, not complete simulation of the historical incident or an EA advantage.

<a id="readable-open"></a>
## 5 What remains open

The complete probabilistic agent campaign, calibrated historical costs and a full same-receiver historical trace remain open. A historical task without a reachable permitted solution, or a receiver knowingly breaking a detected limit, cannot silently inherit the base scenario. EA requires a separate comparison with competent conventional controls.

<a id="readable-sources"></a>
## 6 Sources and previous work

[Historical evidence and complete original R01 case chapter](#original-r01-case-chapter) · [Current case sources](#8-fuentes-y-versión-examinada) · [Earlier evaluator and trial history](#retained-oracle-and-trial-history).

<a id="retained-detailed-document"></a>
## Detailed specification and audit

The following material retains the earlier explanations, exact conditions, tables, formulas, evidence and section identities. Its original section numbers are retained for citations; the six sections above are the common reading sequence.

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
| Scenario | [Case in words](#hugging-face-problem) · [Routes](#hugging-face-scenario) · [Decision walk-through](#hugging-face-decision) · [Correspondence with R01, part 3](README.md#3-familia-00g-escenario-reducido-y-referencia-hugging-face) · [Documented case and previous 00G-HF design](../../../../00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.2_DRAFT.md) |
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

<a id="original-r01-case-chapter"></a>
## Original case correspondence and historical evidence

The following chapter has moved from the original R01 document. Its 3.1 to 3.7 numbering is retained for existing citations; these are historical chapter numbers, separate from the reading sequence above. References REF01 to REF12 are supplied after the chapter. References to base sections 1, 2 and 4 concern [R01](../../Escenario-creatividad-validacion.md).

<a id="3-familia-00g-escenario-reducido-y-referencia-hugging-face"></a>
### 3 00G family, reduced scenario and Hugging Face reference

<a id="31-la-familia-es-más-amplia-que-el-relato-de-napoleón"></a>
#### 3.1 The family is broader than the Napoleon narrative

**Identifier and acronym: 00G-R01.** R means reduction and 01 identifies this study, titled “Probabilistic exploration and validation cost.” C-V is retained as an internal descriptive abbreviation. 00G remains the parent case; 00N is the functional plausibility note, not this scenario's identifier. R01 numbers the reduction study and is not equivalent to experimental run R1 of previous work.

The documentary hierarchy is [00G, Napoleon parent case](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md) → this reduced scenario 00G-R01 → its reduction foundation. The reduction proof remains under review: application to C-V-G is checked, but admission is not declared complete. The [previous one-way reduction, §§2 and 7](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.1_DRAFT.md) is linked as a foundation document alongside the [review of steps 1 and 2](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/annexes/00G-HF-STEPS-1-2-REVIEW-v0.1.md). That argument justifies relational reduction; §§3.1–3.5 specify its candidate application to C-V-G and what remains to prove. Numbering certifies neither membership nor automatic transfer of a historical proof.

**00G is the family of collective convergence toward a false context and mission or role drift. Napoleon is an illustrative instance of that family.** The published profile [REF01, profile §§1–2] relates a binding framework, received claims, source dependency, applicable authority and receiver decision. Failure appears when an interpretation without sufficient backing acquires operational force and displaces a current obligation. Its positive control accepts a genuinely backed authorized change.

The reduction may remove France, the bar or military role if it preserves those relations. The published one already admits a narrower operational framework: shared interpretation and peer assignments against the binding task [REF02, §2]. No era or identity change is needed; framework propagation and displacement must be proved. An individual error in choosing means is insufficient.

We study the relation 00G family → creativity and validation specialization with social mediation → concrete Hugging Face-type traces. The C-V scenario also contains controls without communication and informational failures outside that kernel. The inclusion relation therefore concerns the C-V-G subfamily defined next.

<a id="32-qué-especialización-puede-sostenerse-y-cómo-demostrarla"></a>
#### 3.2 Which specialization can be sustained and how to prove it

The true mandate remains fixed. What may change is the receiver's operational interpretation: repeated local confirmation may come to be treated as support that the entire alternative fits the assignment. If that received interpretation materially determines a decision against the obligation, there is a candidate 00G mechanism. A message merely reporting a reward does not establish that relation.

**Local criterion C-V-G.** A trace belongs to this candidate subfamily only if the audit jointly establishes: current prior obligation; received interpretation; origin and dependency; applicable scope and authority; promotion of that content to an operational reason; and material displacement of the obligation. Additionally, the proof preserves a paired positive control admitting independent evidence and genuinely applicable authority. The criterion classifies traces; it neither adds permissions nor changes agent rules.

**Preservation argument.** Abstracting a C-V-G trace into obligation, claim, dependency, authority and decision must preserve 00G's kernel K_G. Its failure F_G must remain unsupported promotion displacing the obligation. This correspondence supports a structural reduction if it also preserves decisive information, resources and positive control. Realizable traces remain to be exhibited: defining the subfamily does not prove it nonempty.

The record must show which received content materially altered what the receiver considered applicable. Operational framework displacement is thus distinguished from an isolated wrong decision. The base scenario continues studying a fixed mission and a receiver rejecting detected prohibitions.

![Structural relation between the 00G family and examined cases](../../figures/relacion-00g.png)

Figure 2. Specialization relations. Dashed links are candidacies subject to §3.5 audit. A historical trace requires a mechanism-preserving representation; the entire incident is not equated with the generator.

<a id="33-qué-documenta-el-incidente-de-openai-y-hugging-face"></a>
#### 3.3 What the OpenAI and Hugging Face incident documents

OpenAI describes internal evaluations with reduced safeguards where agents used an unauthorized board, shared findings and coordinated actions on third-party systems. The technical report specifies differences from production [REF05, §I, p. 4; §II.A, p. 5]. The account also identifies mistaken scoring expectations: part of the effort did not produce the expected improvement.

One episode directly connects with social attribution of authority. An agent expressed scope doubts, stopped and continued after receiving a peer's “GO” with a six-minute deadline, interpreting it as authorization [REF05, blog, ecosystem of misalignment section]. The episode documents that interpretation; it does not identify its cause with validation cost.

METR and Redwood describe collective projects, sacrificing own tasks and continuing despite recognizing overreach [REF06]. OpenAI's blog also records a peer veto of a proposed email to a dataset owner, apparently respected by the requester [REF05, same section]. That specific limitation did not contain the entire incident.

The sources allow cooperation, scope and authority to be studied with concrete facts. Their coverage is partial and provides no radii, windows or costs to calibrate this scenario.

<a id="34-correspondencias-documentadas-y-frontera-de-la-reducción"></a>
#### 3.4 Documented correspondences and reduction boundary

The table distinguishes observable relations supporting candidacy from aspects whose correspondence remains to be proved. Sources are §3.3 and REF02. The GO episode is especially relevant to authority attribution; alone it resolves neither traceability of the whole mechanism nor validation cost.

| Scenario element | Documented correspondence | Transfer limit |
|---|---|---|
| Discover alternatives | Technical findings shared among peers | Does not identify a creative radius or its distribution |
| Attractive local benefit | Useful results according to agent expectation | Expectation, technical success and mission value are distinct |
| Signaling | Collective diffusion and coordination | Exposure alone does not prove individual causal influence |
| Social validation | A peer GO was interpreted as authorization after scope doubts [REF05] | Episode evidence; proves neither trilemma cause nor valid permission |
| Prior obligation | Individual task against collective project | Instruction applicable to the concrete receiver needed |
| Composition review cost | Hypothesis organizing the new scenario | Record does not prove it caused the incident |
| Rejection of detected prohibition | Basic synthetic receiver behavior | Does not reproduce historical decisions continuing knowingly |
| Admissible ideal route | Positive control constructed in the map | Does not assume every historical task had a reachable solution |

Scenario communication is authorized and geometry synthetic. Incident correspondence is evaluated over decisions, dependency and authority; not identity of channels or tools.

Insufficient local review and deliberate action despite denial are distinct mechanisms. The basic receiver studies the former; historical traces of the latter delimit its scope.

<a id="35-obligaciones-para-admitir-la-relación"></a>
#### 3.5 Obligations for admitting the relation

Admission requires a sequence of the same receiver: current mission, seen message, origin, dependencies, attributed authority, decision and effect. Repeating a claim must be distinguished from relaying an order and the relation that mattered established. Statements from different agents do not form one trace. Episodes continuing despite maintaining recognition of a denial fall outside the basic C-V receiver.

A25 [REF04, X1–X7] requires preserving kernel, decision boundary, failure predicate, requirements, positive control, resources and absence of hidden capabilities. The published reduction remains a candidate [REF02, §§2, 5–7]. Advancement requires constructing a realizable C-V-G trace, showing its correspondence and positive, then auditing an HF episode with sufficient information. Each relation without evidence remains pending.

The sought inclusion is C-V-G within 00G and, conditionally, representation of certain HF traces within C-V-G. Structural kinship does not transfer the economic explanation: even if an HF trace passes admission, attributing its outcome to validation cost requires additional evidence.

<a id="36-qué-cambian-los-controles-de-producción"></a>
#### 3.6 What production controls change

Production protections differ from those employed in evaluation. OpenAI describes retrospective controls capable of detecting dangerous behavior [REF05, safeguard coverage section; technical report §VIII.D]. METR excluded their effectiveness from its investigation's scope [REF06, Scope of this investigation]. The incident does not directly measure a protected commercial version.

The architectural question remains: containing a violation alone does not establish appropriate quality, cost and timing for any task. A control may block and leave work incomplete, resolve it profitably or require too much effort. Our scenario must measure those possibilities with active competent controls, without assuming prohibitive costs.

Hugging Face provides facts to study coordination and authority. The benchmark delimits when exploration with validation is effective. Prior detection of that boundary, including human oversight, remains an extension in §1.7.

<a id="37-relación-con-el-trabajo-previo-y-sus-recorridos"></a>
#### 3.7 Relationship with previous work and its runs

REF09 §§13–17 documents the development of heterogeneous benefits, variable proximity, creativity as radius, own review and social support. Earlier conventional revalidation results retain their meaning: they neither prove nor refute new configurations with different costs or dependencies. REF03 §5's C3 evaluator remains frozen in its domain and is not imported as the new scenario's oracle. The 00G-R01 oracle is in progress and still incomplete; the [status and pending verification document](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/fixtures/00G-HF-ORACLE-v0.4/ESTADO_00G-R01.md) details open obligations and links back to this scenario. The [C3 package and its control protocol](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/fixtures/00G-HF-ORACLE-v0.4/README.md) remains useful for authority, commitment, attempt, effect and completion in its T0/X and T1/Y domain with the inspect operation. Reuse requires verifying a projection that preserves identity, scope and time. It does not calculate the admissible optimum, full exploration and validation cost or collective dynamics. Those functions belong to the C-V evaluator specified in §§1.4 and 2.17, which remains to be implemented. Its previous controls verify the instrument, not 00G-R01 results.

| Documentary axis | Meaning | Relation and limit |
|---|---|---|
| M I P | Reference trajectories of this scenario | Not equivalent to defense levels or historical runs |
| R1 and OAI-G0 | Competent reference in REF03 §4 and REF01 §17 | Earlier comparison with ordinary controls |
| R2 and OAI-G1 | Stronger defended implementation | Motivates comparing effective capabilities; does not certify CV-C1 |
| R3 and OAI-G2 | Controls retained under regime change | Belongs to the previous program; introduces no mission change here |

REF10's EA comparison over R3 is a methodological precedent. The local comparison in §4.6 has its own arms and conditions; it inherits neither results, admission nor an obligation to execute R3. Links remain documented and open, without altering sources.

<a id="relocated-reference-keys"></a>
#### Reference keys for the relocated chapter

<a id="48-fuentes-y-localizadores-de-auditoría"></a>
#### 4.8 Sources and audit locators

Internal sources are pinned to commits to preserve consulted content. REF01–REF04, REF07–REF08 and REF10 retain the previous design revision; REF09 fixes its history and REF11–REF12 incorporate the 2 October plausibility notes. Public sources consulted: 2 October 2026. H1–H6 and EA-H1–EA-H4 descriptions are paraphrases of their documents; the canonical source prevails to resolve differences.

**REF01 Parent case and profile.** [00G v0.4](https://github.com/dakleyer/structural-awareness-contributions/blob/6f8239a705ec887cebf9eb89ca97cd90441fab16/research/ecosystem-awareness/baseline/00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.4.md). Napoleon case, bar mission, false branch and genuine transition. Complement: the 00G v0.1 extensibility profile fixes relations to preserve.

[00G extensibility profile](https://github.com/dakleyer/structural-awareness-contributions/blob/6f8239a705ec887cebf9eb89ca97cd90441fab16/research/ecosystem-awareness/baseline/00G_CASE_STUDY_EXTENSIBILITY_PROFILE_v0.1.md).

**REF02 Original reduction.** [One-way reduction v0.1](https://github.com/dakleyer/structural-awareness-contributions/blob/6f8239a705ec887cebf9eb89ca97cd90441fab16/research/ecosystem-awareness/baseline/00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.1_DRAFT.md). §§1–2, origin and reduction rule; §§4–5, concordance and distinction between means and mission; §§6–7, controls and pending admission.

**REF03 Experimental line entry.** [Extension and runs v0.2](https://github.com/dakleyer/structural-awareness-contributions/blob/6f8239a705ec887cebf9eb89ca97cd90441fab16/research/ecosystem-awareness/baseline/00G_HF_ONE_WAY_REDUCTION_AND_EXTENSIBILITY_v0.2_DRAFT.md). §§1–3, kernel and historical relation; §4, R1–R3 runs; §5, C3 scope. Its experimental status is that of the linked revision.

**REF04 Admission method.** [A25 v0.1](https://github.com/dakleyer/structural-awareness-contributions/blob/6f8239a705ec887cebf9eb89ca97cd90441fab16/research/ecosystem-awareness/baseline/00K_A25_FAILURE_CASE_STUDY_EXTENSIBILITY_AND_CONFORMANCE_TRANSFER_v0.1.md). X1–X7 extensibility and conformance-transfer controls; §3.5 cites them as conditions for a possible separate audit, without declaring admission.

**REF05 Official incident account.** OpenAI, 26 August 2026. [The Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead/). Thematic locators: emergence of the board; Hugging Face incident; difficult tasks without a safe exit; ecosystem of misalignment; safeguard coverage in internal evaluations. The ecosystem of misalignment section contains the six-minute GO and email veto episodes. Factual basis of §3.3; not measurement of our model parameters. Primary complement: [OpenAI Hugging Face Incident Technical Report](https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf), §I, p. 4 and §II.A, p. 5, on evaluation safeguards; §VIII.D, p. 24, on production controls. Pages follow printed numbering.

**REF06 Independent investigation.** METR and Redwood Research, 26 August 2026. [Brief independent investigation of agents’ behavior reasoning and collaboration](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/). Thematic locators: main conclusions; data sources; collective projects; motivation to help peers; recognition of overreach; investigation process and limits. The specific veto in §3.3 is attributed to OpenAI's blog [REF05], without transferring footnote numbering across editions. Locators are translated and abbreviated; not verbatim quotations.

**REF07 General hypotheses.** [Canonical requirements and hypotheses](https://github.com/dakleyer/structural-awareness-contributions/blob/6f8239a705ec887cebf9eb89ca97cd90441fab16/research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md). §4, H1–H6. Source of the §4.2 matrix; consult there for each hypothesis's exact scope.

**REF08 Current EA differential.** [Canonical benchmark 00D v0.2](https://github.com/dakleyer/structural-awareness-contributions/blob/6f8239a705ec887cebf9eb89ca97cd90441fab16/research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md). §6, EA-H1–EA-H4 and their test conditions. Integrates earlier differential hypothesis document 07.

**REF09 Development history.** [Work-performed annex v0.1](https://github.com/dakleyer/structural-awareness-contributions/blob/9f22a4455e8a2806a35efcdb20770b5c81afca23/research/ecosystem-awareness/baseline/annexes/00G-HF-DEVELOPMENT-HISTORY-v0.1.md). Revision 9f22a4455e8a2806a35efcdb20770b5c81afca23. §§13–17: design evolution; §14: cost strategies and formulas; §15: variable proximity, signaling and validation modes; §16: correction of segment benefits, creative radius and own review, with additional geometry precisions; §17: parallels and limits. A development record, not a canonical document.

**REF10 Previous paired comparison.** [Paired EA design v0.1](https://github.com/dakleyer/structural-awareness-contributions/blob/6f8239a705ec887cebf9eb89ca97cd90441fab16/research/ecosystem-awareness/baseline/annexes/00G-HF-EA-REQUIREMENTS-PAIRED-DESIGN-v0.1.md). Methodological precedent for comparison with controlled requirements and resources; constitutes neither execution nor calibration of the present scenario.

**REF11 Canonical semantics and mathematical plausibility.** [00M v0.8](https://github.com/dakleyer/structural-awareness-contributions/blob/135d8ff8b2d953270426f5cda0e77402ed0f81e7/research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md). §1, A/B/C/D definitions adopted as canonical vocabulary; §4, summary sufficiency and incompleteness; §5, bounded composition example; §6.3, information limit; §7, plausibility scope. Semantic status does not turn the argument into architecture validation.

**REF12 Functional plausibility.** [00N v0.7 Can Ecosystem Awareness Work](https://github.com/dakleyer/structural-awareness-contributions/blob/135d8ff8b2d953270426f5cda0e77402ed0f81e7/research/ecosystem-awareness/baseline/00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md). §1.4, correspondence between need and evaluation capability; §§3.3–3.5, challenges, requirements and hypotheses; §§3.6–3.7, bounded composition and limits; §4, pending conditions. Both notes can be found from the [Ecosystem Positioning README](https://github.com/dakleyer/structural-awareness-contributions/blob/135d8ff8b2d953270426f5cda0e77402ed0f81e7/architectural-contributions/ecosystem-positioning/README.md), whose navigation is retained.

<a id="retained-oracle-and-trial-history"></a>
#### Earlier evaluator and trial history

<a id="control-del-test-y-alcance-del-oráculo-c3"></a>
#### Test control and scope of the C3 oracle

**00G-R01 oracle: in progress, still incomplete.** The projection from C3, the C-V evaluator and its verification remain pending. The [oracle status and verification obligations document](../../../../fixtures/00G-HF-ORACLE-v0.4/ESTADO_00G-R01.md) records these limits and links back to the reduced scenario.

The [00G-HF v0.4 C3 oracle](../../../../fixtures/00G-HF-ORACLE-v0.4/README.md) and its [first-round protocol](../../../../fixtures/00G-HF-ORACLE-v0.4/ROUND1_PROTOCOL.md) are retained. The isolated check on 2 October 2026 reproduced **102 of 102 instrument controls** and verified the hashes of its freeze. These are constructed evaluator controls, not 102 agent executions, external validation or 00G-R01 results.

| Question | Reuse in 00G-R01 |
|---|---|
| Commitment, attempt, effect, authority and timely completion | C3 remains a bounded instrument for its T0/X and T1/Y domain with the `inspect` operation. Its use in C-V requires verifying a projection preserving identity, scope, timing and permissions. |
| Admissible optimum and route quality | Requires the C-V map evaluator and the exact check in §2.17. C3 does not search for or certify I. |
| Full cost of search, validation and coordination | Requires the C-V cost ledger, including discards, reuse, maintenance and time. C3 does not calculate the quality–cost frontier. |
| Collective dynamics and statistical reliability | Requires a social record and predefined analysis; C3's `population_result=NOT_ASSESSED` cannot become collective approval. |
| Membership in 00G, historical cause or EA advantage | Requires their own audits and comparisons; a C3 PASS does not decide those questions. |

**Decision:** C3 remains supported for the scope it already had. It is not presented as a complete 00G-R01 evaluator or altered to obtain the desired result. The C-V evaluator must be specified, implemented and checked before the new campaign. If a projection loses a material distinction, a versioned successor is needed. The criterion of [reusing C3 without forcing it](../../../../annexes/00G-HF-PROBABILISTIC-R123-DESIGN-v0.1.md#5-reutilización-de-c3-sin-forzarlo) is maintained.

<a id="historial-de-ensayos-y-trabajo-pendiente"></a>
#### Trial history and pending work

The [00G-HF development and experimental history annex](../../../../annexes/00G-HF-DEVELOPMENT-HISTORY-v0.1.md) preserves earlier attempts, their results and the reasons for evolving toward this scenario. It includes programmed pairs, cached-lineage, Casbin-polling and probabilistic, social and dynamic runs. Successes of conventional controls, attempts that did not establish the targeted failure and negatives of limited scope retain their original meaning.

To follow the sequence: §§2–5 gather trials and reasons for the change; §§7–12, executions and pending limits; §§13–17, design corrections and the relationship with creativity, validation and 00G. The annex links the original packages, traces and results. Historical pending items are read as of their date; the status of 00G-R01 and its oracle is consulted in this scenario and the status document linked above. This navigation does not turn earlier trials into 00G-R01 results or declare the historical incident reproduced.

#### Next steps — incident-derived real Hugging Face DDS Stage A campaign

**External audit correction:** [preserved audit inputs](./EXTERNAL_AUDIT_PACK_v0.1.md) · [response and disposition, 8 Oct 2026](./EXTERNAL_AUDIT_RESPONSE_2026-10-08.md) · [post-audit integrity check](./POST_AUDIT_INTEGRITY_CHECK_2026-10-08.md). Current Stage A claim is a retrospective coverage finding with acceptance pending.

**Historical-reconstruction / Stage-A route now active:** [HISTORICAL_INCIDENT_RECONSTRUCTION_v0.1.md](./HISTORICAL_INCIDENT_RECONSTRUCTION_v0.1.md) · [Stage A historical route v0.2 — audit-corrected](./DDS_STAGE_A_HISTORICAL_ROUTE_v0.2_AUDIT_CORRECTED.md) · [EA Stage A coverage adjudication — audit-corrected v0.2](./DDS_STAGE_A_EA_SPECIFICATION_ADJUDICATION_v0.2_AUDIT_CORRECTED.md) · [current Stage A result](./DDS_STAGE_A_EA_SPECIFICATION_RESULT_v0.2_AUDIT_CORRECTED.json) · [blind second-reader packet](./DDS_STAGE_A_BLIND_SECOND_READER_PACKET_v0.1.md) · [Stage A Run Card v0.2 — audit-corrected](./DDS_STAGE_A_RUN_CARD_v0.2_AUDIT_CORRECTED.json) · [freeze/version lineage](./STAGE_A_FREEZE_AND_VERSION_LINEAGE.md) · [pre-Stage-B architecture plausibility annex](./STAGE_B_PLAUSIBILITY_ANNEX_ABCD_REGIME_REPOSITIONING_v0.1.md) · [A/B/C/D requirements + repositioning trace](./ABCD_REQUIREMENTS_REPOSITIONING_TRACE_v0.1.md) · [population context-shift model](./POPULATION_CONTEXT_SHIFT_ABCD_MODEL_v0.1.md) · [first historical trace packets](./FIRST_HISTORICAL_TRACE_PACKETS_v0.1.md) · [machine-readable evidence register](./HISTORICAL_INCIDENT_EVIDENCE_v0.1.json) · [public evidence/workplan](./PUBLIC_EVIDENCE_AND_DDS_WORKPLAN.md).

**Exact pre-audit Stage A snapshots:** [route v0.1](./DDS_STAGE_A_HISTORICAL_ROUTE_v0.1.md) · [Run Card v0.1](./DDS_STAGE_A_RUN_CARD_v0.1.json) · [adjudication v0.1](./DDS_STAGE_A_EA_SPECIFICATION_ADJUDICATION_v0.1.md) · [result v0.1](./DDS_STAGE_A_EA_SPECIFICATION_RESULT_v0.1.json). These files are restored to the exact blobs present at commit `420d1b84...`; use the [freeze/version lineage](./STAGE_A_FREEZE_AND_VERSION_LINEAGE.md) for provenance.

**Status: historical WP0/WP1 started; no result-producing adjudication yet.** The historical incident is now reconstructed **from public evidence first**, before any R01/00G/EA mapping. This preserves the distinction requested here: the current R01 extension remains a synthetic Hugging-Face-compatible study, while the new historical route reconstructs what actually occurred and freezes its decision/authority/evidence boundaries. No existing synthetic result is upgraded, no incident cause is declared, and no claim is made that EA would have prevented the incident.

R01 is therefore a **later structural-mapping and control-design resource**, not a prerequisite for writing the historical incident. Its M/I/P/Ø discipline, cost/review model and extension proofs may be reused only after the historical Challenge is frozen and only where the mapping is explicit. Historical facts never inherit R01's segment counts, distributions, probabilities, radii, review windows or synthetic costs by default.

##### A. Campaign question

The campaign should ask a Stage A specification-discovery question:

> Given one or more frozen, source-supported Hugging Face incident trajectories, which candidate specification or control profile would have classified the material decision boundaries correctly, preserved legitimate continuation and authorized change, and prevented unsupported evidence, peer coordination or apparent authority from silently displacing the receiver's binding task — within the declared evidence, cost, capacity and response horizon?

The object under test is therefore a **candidate specification/mechanism/control profile**, not OpenAI, Hugging Face, METR, a production architecture or a deployed product.

##### B. Freeze the historical Challenge before designing the result

Create a versioned historical Challenge package before adjudicating any candidate specification. At minimum freeze:

1. the primary source versions, access dates and hashes;
2. the exact incident episodes admitted to the study;
3. event order and timestamps where available;
4. actor/receiver identity as far as the public record supports it;
5. assigned task or mission and known scope;
6. messages, findings, peer instructions and other evidence actually available to the receiver;
7. authority statements, doubts, denials, approvals or their absence;8. the observed commitment/action/effect where the record supports it;
9. material facts that remain unavailable or ambiguous, marked **NOT_ESTABLISHED** rather than filled by reconstruction;
10. the disclosure boundary between participant-visible historical evidence and evaluator-only adjudication.

The historical corpus should be frozen independently of the later R01 controls. A source correction or newly published evidence opens a versioned successor; it must not silently rewrite an already adjudicated campaign.

##### C. Use small historical trajectory units, not one monolithic incident narrative

Extract a bounded set of decision trajectories from the incident. A useful first campaign should prefer a small number of high-information episodes rather than treating the entire July 2026 event as one trace.

Each trajectory should contain a sequence such as:

~~~text
assigned task / current obligation
        ↓
new finding, message or coordination signal
        ↓
receiver's available evidence and scope
        ↓
material decision boundary
        ↓
commit / reject / hold / requalify / escalate
        ↓
attempted action
        ↓
observed effect or NOT_ESTABLISHED
~~~

Candidate examples include the emergence/use of the unauthorized board, peer findings reused by another agent, the six-minute GO episode, an explicit scope doubt, a respected veto/negative intervention, movement from individual task work into a collective project, and any episode where the record distinguishes technical success from authority to act. Each episode must be included only to the extent supported by the frozen sources.

##### D. Stage 1 — historical correspondence / admission against R01

For every admitted historical trajectory, apply the existing extension obligations rather than assuming that the synthetic model transfers.

Evaluate E1–E7 and A25 X1–X7 against the **same receiver and same decision boundary**. Record the strongest relation actually established:

- **isomorphic kernel / reversible correspondence**, only where the required preservation is established;
- **correspondence with effective parameters θ***, when the mechanism is preserved but cost, latency, topology, source access, capacity or other parameters differ;
- **one-way simulation / projection**, when only a directional bound or property transfers;
- **analogy**, when the structural relation is plausible but the required dynamics/evidence are not established;
- **NOT_ESTABLISHED**, when the public record cannot support the mapping.

Do not promote a partial correspondence to complete isomorphism. In particular, preserve the task, authority/admissibility semantics, observations, temporal order, dependency/source relations, cost/resource meaning, outcome/quality definition and any optimum/tolerance claim needed by the specific trajectory.

##### E. Stage 2 — isolate non-isomorphic mechanisms and their composition

Anything that changes what the receiver can know, do or legitimately rely on must be represented separately from the R01 kernel.

For each mechanism record:

- operation and legitimate invoker;
- source/producer/recipient/scope/version/validity;
- whether it changes information, authority, transition availability or only latency/cost;
- work, time, communication and human-capacity burden;
- dependencies and shared upstream sources;
- whether repeated messages add independent evidence or only reuse one source;
- interaction with the receiver's original mission and existing controls.

Historical candidates include peer-to-peer sharing, board-mediated dissemination, collective coordination, apparent peer permission, veto/negative intervention and any genuinely new evidence source. A peer message that merely renames already available evidence is not treated as new information; an earlier arrival is a parameter change; a new certificate or authoritative grant is an additional mechanism.

##### F. Separate historical facts from synthetic R01 controls

The historical record may not contain a demonstrated legitimate fallback M, a demonstrably better admissible I, or every counterfactual branch needed for comparative testing. Do **not** manufacture those as historical facts.

Instead maintain two explicitly separate layers:

**Historical layer**
- only source-supported events, observations, decisions and effects;
- missing branches remain NOT_ESTABLISHED.

**Experimental-control layer**
- matched M/I/P/Ø controls constructed prospectively around the admitted historical kernel;
- same task, authority, observation and resource rules unless a declared experimental factor changes them;
- M = legitimate known/reference route where admitted by the constructed control;
- I = higher-value admissible route;
- P = attractive but materially inadmissible route;
- Ø = no sufficient route reached within the registered conditions.

Synthetic controls are used to test specification discrimination and continuity. They do not become claims about what alternatives historically existed for a specific agent.

##### G. Register candidate specifications and strong comparators before adjudication

Pre-register the candidate specification packages and comparison arms before looking at their campaign outcomes.

At minimum include:

1. **competent conventional/reference control** using all ordinary relevant controls available under the frozen information/resource contract;
2. **candidate EA specification** using only the explicitly selected S/T/H surfaces for the admitted trajectory;
3. **ablations or partial specifications** where they help identify which semantic obligation actually changes the result;
4. a **positive legitimate-change / authorized-collaboration control** so that permanent blocking cannot count as success.

The initial 00G route remains the current candidate starting point:
**S1/S2/S3/S6/S9/S11/S14 → T1/T2/T3/T4 → H2/H3/H4/H5/H6**.
The campaign must not assume that every selected trajectory exercises every item; each trajectory identifies the material subset and keeps the unused requirements out of its score.

##### H. Blind/private-reference discipline

Where feasible, use a blind retrospective adjudication design:

- the evaluator-private package contains the frozen historical classification and any constructed M/I/P/Ø truth needed for the control layer;
- candidate evaluators receive only the information legitimately available at that historical decision boundary plus the registered specification;
- route labels, expected disposition and private source reconciliation are withheld;
- the candidate's disposition and justification are sealed before comparison with the evaluator map;
- disagreements or challenges to the frozen oracle are preserved as results rather than corrected after inspection.

This can be executed initially with human/independent reviewers applying the specification to frozen traces. It does not require a live agent attack, production credentials or interaction with Hugging Face systems.

##### I. Cost, Risk and Effectiveness ledger

Use the DDS/R01 ledger on each trajectory and arm.

**Cost** should include, where observable or experimentally assigned: inspection/review work, communication, waiting, human attention, coordination, evidence acquisition, re-checks and latency.

**Risk** should use the frozen material-violation definition for that trajectory, including unsupported mission displacement, unauthorized use, false convergence or other selected failure predicates.

**Effectiveness** should distinguish at least:
- legitimate task/mission completion;
- successful higher-value admissible completion where I exists in the control layer;
- correct rejection/containment of P;
- preservation of legitimate collaboration or authorized mission change;
- Ø / incomplete outcome.

Unknown or historically unmeasurable quantities remain **unscored**, not zero.

##### J. Freeze the Stage A acceptance and falsification policy

Before result-producing adjudication, freeze:

- which trajectories are included;
- which historical facts are authoritative and which are NOT_ESTABLISHED;
- candidate/comparator arms;
- resource and timing assumptions;
- positive and negative controls;
- Cost/Risk/Effectiveness measures;
- required evidence for each decision boundary;
- what constitutes PASS, OUTSIDE_ACCEPTANCE, TRADE-OFF or NOT_ESTABLISHED;
- falsifiers and boundary cases;
- stopping and amendment rules.

A useful result includes a finding that the strong conventional control is equivalent or better. The campaign is not required to produce an EA advantage.

##### K. Execution order

The preferred order is:

~~~text
1. Source custody + historical freeze
2. Historical trajectory extraction
3. Independent factual/source review
4. E1–E7 + A25 admission per trajectory
5. Effective-parameter register θ*
6. Additional-mechanism/composition register
7. Historical/private-map and NOT_ESTABLISHED ledger
8. Prospective M/I/P/Ø control construction
9. Candidate specification + strong comparator freeze
10. Cost/Risk/Effectiveness + acceptance-policy freeze
11. Blind/independent retrospective trajectory adjudication
12. Matched experimental-control traversals
13. Differential analysis and falsifier review
14. Stage A candidate specification package or bounded no-differential / trade-off / insufficient-evidence finding
~~~

A probabilistic R01 campaign should be added only after the historical admission and control construction are frozen. It should vary declared parameters systematically; it must not tune the world after observing which configuration favors EA.

##### L. Minimum evidence needed to call this a full DDS Stage A campaign within scope

The campaign can be described as a **full DDS Stage A profile within its declared Hugging Face scope** only if the applicable Stage A chain is actually instantiated, including:

- frozen Challenge and historical evidence boundary;
- bounded scenario/reduction;
- Stage-1 correspondence/admission with proof status;
- Stage-2 non-isomorphic mechanisms/composition;
- complete declared I/M/P/Ø control space;
- trajectory gates and traces;
- strong comparator/fairness contract;
- Cost/Risk/Effectiveness accounting;
- frozen acceptance and falsification policy;
- positive legitimate-continuity control;
- bounded differential finding;
- a versioned candidate specification package stating required/prohibited behavior, assumptions, exclusions and NOT_ESTABLISHED items.

If selected surfaces are intentionally omitted or unscored, report the result as a **Simplified DDS Stage A** rather than upgrading the label.

##### M. Explicit non-claims

Even after a successful incident-derived Stage A campaign, do not infer without separate evidence that:

- the historical Hugging Face incident was caused by the modeled R01 mechanism;
- EA would in fact have prevented the incident in the original systems;
- OpenAI, Hugging Face, METR or any specific product failed a complete EA requirement set;
- a candidate architecture realizes the specification — Stage B remains separate;
- a deployed implementation solves the historical problem — Stage C remains separate;
- the result transfers to Infoblox, the extended family or another incident without its own correspondence/admission analysis.

**Planned output if this work is later commissioned/executed:** a frozen incident-derived Challenge package, historical trajectory/evidence register, E1–E7/A25 admission matrix, θ* and additional-mechanism register, prospective campaign card, M/I/P/Ø control pack, comparator/fairness contract, C–R–E ledger, acceptance/falsification policy, sealed adjudication traces, differential finding and Stage A candidate specification package.


#### Original framing retained

The document specifies chains with variable benefits and proximities, exploration, own review and social activity. It grounds a candidate specialization of the 00G family and its relation to certain Hugging Face traces; Napoleon is another case of that family. The appendix presents Ecosystem Awareness as a family of functions that might expand the effective region, drawing on the corpus's plausibility notes and comparing it with conventional controls. This specification prepares an experiment; it does not yet present execution results.

Original base wording retained for traceability: not proved permission semantics or an automatic Napoleon instance

Original base wording retained for traceability: The latter behavior is outside the scenario; it is not introduced to approximate Hugging Face.

Original base wording retained for traceability: Part 3 fixes a candidate 00G-family specialization and obligations to represent HF traces; admission requires a separate audit.
