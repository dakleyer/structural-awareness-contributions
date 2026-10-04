# R01 M01 — Scope, policy class and feasibility quantifiers

Scope contract v0.1 · 3 October 2026 · M01 completed for mathematical formulation

[R01 README](../../README.md#bot-start-here) · [Mathematical work plan](../../MATHEMATICAL_FEASIBILITY.md) · [Master execution prompt](../../STRATEGIC_WORKPLAN_AND_EXECUTION_PROMPT.md) · [Scope checks and preservation evidence](../partial-experiments/historical/M01_SCOPE_CHECKS.json)

**Result:** a precise, deliberately bounded question is now defined. M01 does not establish that an infeasible region exists, construct an R01 witness, derive a lower bound, implement the oracle or validate a technology. Those remain M02–M05, C and T work. Review type: adversarial self-review of formulation, not independent mathematical validation.

Input commit: `f33e2887ab7add81f38ada94533ff83096b77e70`. Current source anchors and the acceptance mapping are recorded below. The base scenario remains unchanged.

## 1. The first question

For a fixed mission and declared information/cost interface, does **one policy, chosen before the hidden world is drawn**, achieve sufficiently good legitimate delivery within budget and deadline, with required reliability? Where can no policy in the declared class achieve it?

The first proof target is a **single-agent, finite, static submodel**. This isolates the information issue before adding collective evidence sharing. The broader R01 campaign keeps its existing population and comparison scope. A result for N=1 does not automatically cover N>1, human supervision, dynamic dependencies or a named framework.

M01 fixes parameter domains and quantifiers. It does not freeze a numerical campaign grid or choose deployment thresholds. Each configuration fixes its own numerical coordinates before a world draw; M02 must instantiate them for witnesses. Campaign registration remains C11/P03, and the full cross-workstream reconciliation remains M10.

## 2. Exact configuration domain

Let Θ₁ be the following family. A configuration θ specifies all items in this table, not just L or a vendor name.

| Item | Domain and rule |
|---|---|
| Agent and mission | N=1; one fixed assignment, principal, normative rule and completion requirement. World facts may differ, but the mission/authority is not socially redefined during an episode. |
| Worlds Ω | A finite nonempty set of encoded static worlds sharing the declared public assignment. A world includes graph facts, rewards, dependencies, authority applicability, initial evidence and environment state. |
| Material graph | A finite directed acyclic graph with L≥1 comparable task positions and explicitly registered connectors/mixtures. Material execution advances a declared rank; all complete routes are finite. This excludes material cycles, not repeated inspections/search. |
| References | Each world has a complete admissible M and an attractive inadmissible reference P; M's plan is known under the common initial-record regime. I is derived from all complete admissible routes, not assigned a privileged generator label. Ties and superior mixtures are retained. |
| Benefits and geometry | Finite rational encodings; nonnegative action benefits. J is the sum over the effective material trajectory, including connectors. M's generative mean is normalized to one. Generation profiles, distances, radius and conditioning are fixed before draws and remain unchanged within a world. |
| Predicates | Separate blocks for conjunction and synthetic global parity. Mixed predicates, technical composition term g and negative benefits are outside this first profile. No interpretation of parity as a general real-world authorization rule is claimed. |
| Event/action/observation alphabets | Finite typed catalogs of exploration, relation/mandate/state queries, evidence creation/checking, review/decision, execution, waiting and stop events. Record/message payload bounds and numerical precision are explicit coordinates. Each applicable sufficient certificate or shortcut being admitted needs an interface operation, observation and cost. |
| Receiver protocol | Own review precedes commitment; the minimum own-review gate, scope declaration, clipping/overlap rules and evidence-discharge conditions are fixed in θ. Planned review must complete before PASS-local; PASS-local leaves global residue explicit. Adaptive depth is permitted above the gate. Detected applicable prohibitions are rejected. |
| Initial information | Assignment, M plan and registered observations/evidence/prior knowledge. Certification is not supplied merely because M is known. Initial evidence production/use and setup costs follow a declared common accounting rule. |
| Event horizon | A finite H≥1 bounds all operational events, including rejected/discarded work and repeated queries. Reaching H terminates the run as complete or incomplete according to actual delivery. H is a submodel restriction, not a proof that uncapped R01 terminates. |
| Costs/time | Rational nonnegative charges and durations for every event, with 0<c_v<c_e for comparable review/exploration units. R>0 and T>0 are fixed rational global budget/deadline coordinates. Initial preparation/amortized evidence charges are included; no unregistered free query or reset is allowed. |
| Environment | A finite-state transition/observation contract K_ω with rational probabilities; deterministic cases are included. State includes position/prefix, evidence versions, ledger, clock and bounded transcript. Execution barriers and over-budget requests are declared, not fitted after outcomes. |
| Thresholds | ε≥0 in J units, p_min∈(0,1], δ∈[0,1], all rational and fixed per θ. ε is an absolute optimum-gap tolerance. A relative-tolerance profile needs an explicitly different conversion. |
| Policy randomization convention | The model-level random draw supplies no factual evidence. Startup/sampling charges included in the initial ledger are fixed independently of the mixture weights λ; registered subsequent decision/operation charges still apply. A physical sampler or compiler with additional λ-dependent cost needs a different explicit accounting profile. |
| Law mode | AVG with a fixed rational distribution μ on Ω, or WC with all ω∈Ω covered individually. The modes define separate configuration spaces; their conclusions cannot be interchanged. |

The action/observation and cost catalogs are **mathematical inputs** here. Concrete machine-readable schemas, generators and policies are still C02–C06 deliverables. Finite encoding is not a claim of cheap enumeration or polynomial complexity.

The first M02 candidate family is Θ_pair⊂Θ₁: Ω={ω₀,ω₁}, AVG weights exactly (1/2,1/2), with the same public assignment. The WC version uses that same world pair but no averaging. M02 must check the appropriate equality of available views; it is not imposed or established merely by naming two worlds.

Θ_pair does **not** require that M misses the tolerance, that the worlds demand incompatible choices, or that a cheap certificate is absent. These must be checked if used in a hard-instance argument. Configurations resolving the difficulty are valid controls.

## 3. What the policy can know and do

The local history h contains initial registered information, own operations and responses, observed candidates/rewards, evidence lineage and applicability, budget/time signals actually disclosed, commitments, attempts and effect receipts. The policy may retain the entire history and use adaptive search, early stopping, caches, sufficient certificates, return to M through valid connectors, retries and abstention within the contract.

The evaluator's actual world identifier, I/P labels, complete map and ground-truth verdict are not additional observations. If a legitimate initial datum, query, certificate or observable correlation resolves the target, it belongs in h and may eliminate a proposed hard case. The observed history includes relevant errors, refusals, delays, lengths and metadata; hiding a side channel from the proof while exposing it to the policy is invalid.

Let A_req(h) be the finite action requests allowed by the observable interface at h, including a stop/abstain request. Let D_θ be **all deterministic maps from finite observable histories to A_req(h)**, respecting the registered own-review gate and rejection of detected applicable prohibitions. In particular, commitment cannot obtain a fabricated PASS-local from unfinished planned review; a permitted commitment may still carry unresolved global conditions after the local gate. Hidden-state enablement and barriers are evaluated by the environment: a syntactically allowed attempt can receive a refusal. The policy is not granted the true hidden enablement predicate in order to choose a request. Policies may act with unresolved evidence under their declared rule; they cannot intentionally execute a prohibition they have already correctly detected. D_θ is not the small catalog of CV arms. Full history is retained, so a fixed validation window, memorylessness or a particular search heuristic is not silently imposed.

For the single-agent finite model, define the mathematical policy envelope

Π_obs(θ) = {λ on D_θ : λ_d≥0 and Σ_d λ_d=1}.

An episode selects a deterministic history rule using λ before the world draw, with policy randomness independent of the hidden world. The sampled rule remains adaptive because it acts on future h. Drawing all internal choices in advance is the declared representation of randomized finite-history rules; it conveys no world information. Environment randomness remains in K_ω. There is no second agent or free shared-evidence channel in this profile.

This envelope permits ideal mathematical probabilities and arbitrary allowed history rules. A concrete runtime, finite implementation or smaller observed family must separately demonstrate membership and resource accounting. Feasibility in this envelope is not an implementation or technology-feasibility result. Infeasibility for a genuine subclass does not imply infeasibility for this envelope.

Finite catalogs and H make the history-rule set finite in principle, possibly enormous. The task does not enumerate it. Any proof about all policies must include this full declared class or clearly replace it with a narrower one. More sophisticated admissible summaries/certificates cannot be excluded simply because they refute a hoped-for result; changing their interface changes θ and the scope.

## 4. Success and violation events

For world ω, let A_ω be all complete admissible material trajectories in the registered graph, including connectors and mixtures. M∈A_ω, so the set is nonempty. Define

J*(ω)=max_{τ∈A_ω} J(τ).

This is a **structural admissible optimum**, not an optimum recomputed only among routes the tested policy happened to discover or could afford to verify. DAG/finite-route assumptions make the reference finite. I may be any maximizer; all sufficient routes, not only one tied I, count.

For a realized operational trace ζ:

- a(ζ)=1 exactly when a complete admissible result is delivered by T.
- q(ζ) is the value of that legitimate result; without one, q=0. Partial technical value is reported separately. A violating action used in the delivered composition cannot count as legitimate quality.
- v(ζ)=1 if at least one executed obligation violation occurs in the campaign; a proposal or blocked attempt alone does not set v=1. Recovery does not erase a previous executed violation.
- C(ζ) includes all operational charges through closure, including failed/discarded work and preparation. Evaluator-only computation is recorded separately. Under a hard budget barrier C≤R may hold by construction; inability to afford needed operations still causes incompleteness.
- t_del is delivery time when legitimate delivery exists; otherwise it is absent. An analytic +∞ convention may express failure, but a reported latency remains censored at T with completion recorded separately.

S is the joint event

a=1 ∧ q≥J*(ω)−ε ∧ C≤R ∧ t_del≤T ∧ v=0.

V is the event v=1. a=1 is necessary even when J*−ε≤0; a safe abstention must not pass merely because q=0 exceeds a low quality threshold. A low-quality legitimate completion can have a=1 and S false. Legitimate delivery elsewhere does not undo a campaign violation.

Threshold equality is accepted: q=J*−ε, C=R, t_del=T, success probability=p_min and violation probability=δ satisfy their corresponding inequalities. Their actual values remain fixed before outcomes, not tuned to obtain a region.

## 5. Probability law and quantifier order

For AVG, first draw a policy rule d∼λ independently of ω∼μ; run the frozen K_ω. These sources of randomness are distinct. Define

s_θ(λ)=Σ_ω μ(ω) Pr_{λ,K_ω}(S | ω),

r_θ(λ)=Σ_ω μ(ω) Pr_{λ,K_ω}(V | ω).

The configuration is adequate for λ exactly when s_θ(λ)≥p_min and r_θ(λ)≤δ. A realization of a world or policy seed is not itself an independent sample for campaign statistics. Rejection-conditioning and weights are declared in μ; adding easy worlds changes the problem distribution, not evidence of improvement at the same θ.

For WC, **the same λ** must satisfy, for every ω∈Ω,

Pr_{λ,K_ω}(S | ω)≥p_min and Pr_{λ,K_ω}(V | ω)≤δ.

The correct order is ∃λ ∀ω. The weaker statement ∀ω ∃λ_ω gives the policy designer the actual world and cannot certify the hidden-world task. Nor does ∀λ ∃ω by itself establish failure under a specified average distribution.

For the balanced pair, AVG averages the two conditional rates with weight 1/2. A selector, human or technology that receives extra evidence changes the observation contract. It is not a counterexample to a theorem retaining the old information conditions; it may be a legitimate resolution in another configuration.

## 6. Feasible and infeasible regions

Within Θ₁^AVG:

F_AVG={θ : ∃λ∈Π_obs(θ), s_θ(λ)≥p_min ∧ r_θ(λ)≤δ}.

U_AVG={θ : ∀λ∈Π_obs(θ), s_θ(λ)<p_min ∨ r_θ(λ)>δ}.

Within Θ₁^WC:

F_WC={θ : ∃λ∈Π_obs(θ) ∀ω∈Ω, s_{θ,ω}(λ)≥p_min ∧ r_{θ,ω}(λ)≤δ}.

U_WC={θ : ∀λ∈Π_obs(θ) ∃ω∈Ω, s_{θ,ω}(λ)<p_min ∨ r_{θ,ω}(λ)>δ}.

F and U are logical complements within each well-defined domain. Either may be empty. The **unresolved evidence category** means neither membership claim has been established by our available evidence; it is not a third logical set between F and U.

A stop/abstain rule remains in the class, so infeasibility is not manufactured by making the policy class empty. It generally fails the delivery requirement, which is a legitimate outcome.

No region size, positive-measure claim or real-world prevalence is defined by this contract. A later such claim must supply a parameter domain and measure/grid weights. The formulation uses existence directly and does not assume that a supremum in an unrelated infinite model is attained.

## 7. Why randomized policies must remain in the class

For a fixed θ and d∈D_θ, write s_d and r_d for the true, not estimated, probabilities. AVG adequacy becomes the finite feasibility system

Σ_d λ_d s_d≥p_min; Σ_d λ_d r_d≤δ; λ_d≥0; Σ_d λ_d=1.

WC uses one pair of constraints per world with that same λ. This representation follows by conditioning on the initially sampled d under the fixed startup/sampling-cost convention in §2. If implementing a mixture adds λ-dependent cost or latency, these fixed coefficients cannot silently be reused; C02/M10 must represent that change. It supplies a target for later exact witnesses; it is not an implemented solver or known set of R01 coefficients.

**Diagnostic example, not an R01 witness:** one policy has (success,risk)=(2/5,0), another (4/5,1/5). With p_min=3/5 and δ=1/10, neither deterministic choice is adequate. A half/half mixture has (3/5,1/10) and meets both thresholds. Therefore failure of every deterministic comparator need not mean failure of their randomized class. These numbers illustrate quantifier/threshold logic only and are outside any claim about a runtime or historical incident.

Because S and V are disjoint, Pr(V)≤1−Pr(S). If δ≥1−p_min, the risk ceiling adds no restriction beyond the reliability condition in this model. If δ<1−p_min, it may add a real restriction. δ=0 and p_min=1 are allowed boundary cases. Neither a small sample with no violations nor a nonsignificant difference establishes the exact probabilities used here.

## 8. Separate information difficulty from physical impossibility

Define the information-focused subclass Θ_info by requiring that **each world has a complete admissible sufficient-quality trajectory physically executable under the same R/T/H, receiver gate and remaining review/decision/execution/setup charges when the relevant world facts are supplied upfront**. This is a counterfactual full-information control, not an allowed free query for the tested policy. It eliminates only acquisition work made unnecessary by that input; it grants no additional authority, route, reset, fabricated PASS-local or reduced execution charge.

M02 must supply these per-world controls. They exclude a task that cannot be delivered even with the missing facts. They do not show that one hidden-world policy is adequate, and they do not establish the necessary inspection cost. Worlds outside Θ_info remain in the general feasibility family but cannot support an information-only explanation without qualification.

The primary proposed negative claim is **a nonempty subset of U_AVG or U_WC within Θ_pair∩Θ_info under explicit inequalities**, if M02/M03 can support it. No such subset is established here. Stronger allowed evidence, a dominant safe route, larger ε or cheaper queries may make it empty.

## 9. Scope reductions that must remain visible

| Restriction or limit | Consequence |
|---|---|
| N=1 | No population-level result, pooling or coordination bound follows. Extending N requires local/joint histories, message timing, costs and randomness contracts. |
| Static DAG and additive nonnegative J | No claim about evolving dependencies, material cycles, negative rewards or arbitrary g. |
| Finite H/catalog/payload precision | No claim about unbounded computation or excluded long protocols. A cap-induced failure cannot be presented as an uncapped architectural impossibility. |
| AVG versus WC | Average inadequacy, worst-case inadequacy and each-world oracle feasibility remain distinct. |
| Π_obs versus CV/technology | CV arms are tested procedures; a technology needs policy/information/resource admission. Vendor names do not determine the class. |
| Logical F/U versus evidence | A finite sample supports scoped inference for evaluated arms, not automatic membership in universal U. |
| Initial view equality | It does not establish equality after adaptive charged queries. M03 must cover the complete relevant observation process and information cost. |

## 10. Adversarial formulation review

| Attack | Disposition in M01 |
|---|---|
| Choose the appropriate policy after learning ω. | Rejected: λ is fixed before draw; ∃λ∀ω is distinguished from ∀ω∃λ_ω. |
| Ignore randomized combinations of unsuccessful deterministic policies. | Rejected: Π_obs retains mixtures; the diagnostic threshold example demonstrates the defect. |
| Count abstention as success when ε includes the optimum. | Rejected: S requires actual a=1. |
| Declare infeasibility at equality with a threshold. | Rejected: adequacy inequalities are inclusive; their negations are strict. |
| Derive an information bound just from equal initial summaries. | Not sufficient: cheap adaptive queries/certificates can distinguish the worlds; M02/M03 must address them. |
| Make I the best named route, ignoring a superior mixture. | Rejected: maximize over all complete admissible material routes. |
| Remove own review or label an unfinished planned check PASS-local. | Rejected: θ fixes the receiver gate and certificate applicability; D_θ preserves it. |
| Apply the fixed-coefficient mixture system despite extra sampler/compilation cost. | Rejected: §2 states its idealized cost convention; actual additional costs require a revised profile and admission. |
| Hide work, setup, side channels, reset or certificate production. | Rejected within the declared interface; changes reopen the affected contract. Operational/hardware realization remains to be checked. |
| Present H or certificate exclusion as a universal limitation. | Rejected: the narrower domain and potential eliminating controls remain explicit. |
| Treat individual controls or a correct oracle as a new campaign. | Rejected: no campaign or technology result is produced by M01. |

This review found no need to alter R01's source scenario. It narrowed the first proof profile and resolved definition errors before attempting a lower bound. Independent review of this formulation is still welcome; any material finding reopens M01/M10 rather than being suppressed.

## 11. Acceptance and source correspondence

| M01 acceptance item | Result/evidence |
|---|---|
| Exact domain | §2 defines Θ₁ and Θ_pair; §8 defines the information-focused subclass. Numeric coordinates are fixed per θ; actual witness instances remain M02. |
| Policy class | §3 defines observable histories, D_θ and Π_obs, including memory/adaptation and randomized rules. |
| Law / worst-case criterion | §5 fixes AVG and WC separately, with world/policy/environment randomness and quantifier order. |
| Thresholds and F/U | §§4/6/7 define success, violation, inclusive thresholds, region negations and the risk relation. |
| Empty/unresolved regions | §6 separates logical partition from the evidence classification; no nonemptiness or measure claimed. |
| Review and trace | §§9/10 record adversarial limits; M01_SCOPE_CHECKS.json records checks and preservation. |

Primary evidence for this task is the existing corpus and the explicit definitions/conditioning above. No external theorem or originality is claimed by this formulation.

- [R01 scenario at input commit](https://github.com/dakleyer/structural-awareness-contributions/blob/f33e2887ab7add81f38ada94533ff83096b77e70/research/ecosystem-awareness/baseline/reductions/00G-R01/Escenario-creatividad-validacion.md): §§1.2–1.5 distinguish finite-arm evidence and impossibility; §§2.1–2.3 establish routes/optimum; §§2.6–2.8 establish information and required own review; §§2.11–2.12 establish charges/limits; §§2.15–2.17 establish policies, traces and controls.
- [00M v0.8 at input commit](https://github.com/dakleyer/structural-awareness-contributions/blob/f33e2887ab7add81f38ada94533ff83096b77e70/research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md): §6.3 gives the elementary information distinction, not an R01 resource theorem.
- [Existing bounded quality checker at input commit](https://github.com/dakleyer/structural-awareness-contributions/blob/f33e2887ab7add81f38ada94533ff83096b77e70/research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/verify_audit.py): `success(value,optimum,epsilon)` uses the absolute gap `value >= optimum - epsilon`; it checks quality only. M01 adds explicit delivery/safety/resource requirements and does not treat that checker as the full oracle.
- [Canonical requirements at input commit](https://github.com/dakleyer/structural-awareness-contributions/blob/f33e2887ab7add81f38ada94533ff83096b77e70/research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md): retained as corpus authority; this research scope does not certify EA compliance or replace its requirements.

## 12. Task record and next action

M01: DONE — scope/quantifier formulation only. Executing owner: Codex, acting on the user's instruction; reviewed by the same agent. Actual UTC completion timestamp and input hashes are in M01_SCOPE_CHECKS.json. No external person's responsibility or approval is assigned.

M02–M11 remain OPEN. This task supplies inputs for M10 and P03, without closing their independent reconciliation criteria. The historical common-audit/hash failures remain P08; M01 does not repair or overwrite old manifests.

**Next task, M02:** construct an explicit balanced hard-pair candidate and feasible control in the chosen conjunction block first; enumerate all admissible material routes/mixtures; declare the complete query/observation contract and physical full-information controls. Try a common safe high-quality route and cheap sufficient certificate before calling the pair hard. Develop the parity block separately. If these checks refute the candidate, preserve it and report the narrower or empty claim.

## 13. Prompt for another reviewer

Review this M01 formulation at the exact published commit supplied with the links. Read the R01 scenario at the input commit, the mathematical work plan, this result, the diagnostic script and M01_SCOPE_CHECKS.json. Try to invalidate the chosen domain or the adequacy definitions. In particular, check N=1 versus population claims, finite caps versus unrestricted policies, required own review, hidden enablement versus observable requests, world/policy randomness, ∃policy∀world versus ∀world∃policy, AVG versus WC, mixtures, structural optimum, delivery at low thresholds, strict failure inequalities and the full-information control. Run `python3 verify_m01_scope.py`; passing its diagnostic examples is not a proof about R01. Compare input/output changes and preservation evidence. Report each finding with severity, exact section, counterexample or missing assumption, and the minimal correction. Permit a verdict that M01 must be reopened; do not presume a negative region, EA advantage or historical causation. Do not close M02 or M10 from this scope document.
