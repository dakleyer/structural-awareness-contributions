<a id="fundamento-metodológico-probar-r01-y-transferir-sólo-propiedades-preservadas"></a>
# Methodological foundations: test R01 and transfer only preserved properties

Research version 0.1 · 2 October 2026 · Author's note assisted by AI

[R01](../README.md) · [Common criterion and audit](./CRITERIA_AND_AUDIT.md) · [Kernel and E1–E7 proof](./family/KERNEL_AND_PROOF.md) · [Checked fragment](./family/proof/README.md)

<a id="1-qué-justifica-este-método"></a>
## 1 What justifies this method

Testing a reduced model first has solid precedents in computing. The literature allows systems to be reduced through formal relations, properties to be checked in the reduced representation and transferred when the corresponding obligations are satisfied [R1–R7]. This justifies the **method**, not external validation of R01 or EA.

Our intended use has three steps: isolate exploration, costly review and social reuse of evidence; evaluate EA's incremental contribution against competent controls; and use the results to decide whether expanding research to domain implementations is worthwhile. The reduced model allows variables to be controlled, counterexamples to be obtained and mechanisms to be measured at lower cost. The fidelity of its hypotheses and the real cost of implementing EA require their own tests.

The defensible sequence is: **specification → preservation proof → implementation verification → comparative experiment → independent domain correspondence → validation of a more complete scenario**. No later step is established by citing earlier ones.

Base: R01 v0.6, fixed at commit `114ac132bc2be4e7008001fe505bf5bd4c36c515`; the E1–E7 note and common audit delimit the scope actually proved and executed. This note neither changes the scenario nor incorporates EA experimental results that do not yet exist.

<a id="2-precedentes-y-correspondencia-precisa"></a>
## 2 Precedents and precise correspondence

Correspondences in the last column are our interpretation applied to R01. Those authors are not credited with reviewing our model.

| Primary source | Relevant result or practice | Application and limit in R01 |
|---|---|---|
| R1 Hashemi, Hatefi and Krčál, 2014 | Bisimulations for interval MDPs; reduction preserving PCTL under the studied uncertainty interpretations; computational case. | Supports checking probabilities aggregated by classes (E3). Its theorem does not automatically cover all our metrics, observations and policies. |
| R2 Li, Walsh and Littman, 2006 | Distinguishes abstractions preserving model, values or optimal actions; proves differences between their guarantees. | Preserving an optimal action is not equivalent to preserving traces, information or behavior of all policies. Helps choose the property before reducing. |
| R3 Rezaei-Shoshtari et al., NeurIPS 2022 | MDP homomorphisms, equality of values for corresponding policies and of the optimum; experiments in DeepMind Control Suite. | Close precedent for states, actions, transitions and outcomes. Continuous lifting treated in its later theorems is restricted to deterministic policies; it does not authorize indiscriminate extension to partially observable agents. |
| R4 Clarke et al., CAV 2000 | CEGAR: check abstraction, analyze counterexample and refine if spurious; NuSMV implementation and hardware experiments. | Guides a future refinement cycle. Adding variables or scenarios by designer choice is insufficient to claim we already execute CEGAR. |
| R5 Kattenbelt et al., Oxford report 2008 | MDP abstraction through games, with lower and upper bounds; experiments in protocols and distributed algorithms. | Allows consideration of a conservative relation when exact equivalence is too strong. Its bounds concern specified properties, not narrative resemblance. |
| R6 Kattenbelt et al., VMCAI 2009 | Verification of probabilistic ANSI-C software with abstraction, refinement and quantitative bounds. | Precedent for experiments on executable software and its relation to its abstraction. R01 has not yet established an equivalent chain from a complete technological integration. |
| R7 Zhang, Wu and Lin, 2017 | Simulation and CEGAR for POMDPs; preservation of a finite-horizon PCTL safety fragment. | The decision-maker's information matters. Partial observation does not disappear by giving the evaluator a complete state. This is a methodological alternative requiring another specific proof. |
| R8 Bian and Abate, FoSSaCS 2017 | Relates approximate bisimulation and distance between finite-horizon traces in labeled Markov chains. | Precedent for quantifying transfer error; its hypotheses do not carry over directly to adaptive policies or a strategic population. |
| R9 Spork et al., CONCUR 2024 | Compares several notions of approximate probabilistic bisimulation and their relations. | Requires identifying the relation and preserved property. “Approximately similar” does not by itself provide a bound. |
| R10 Agarwal et al., NeurIPS 2021 | Evaluates statistical uncertainty in RL comparisons with few runs and proposes interval estimates and performance profiles. | Guides future EA analysis: repetitions, variability and task distribution. It neither imposes a universal seed count nor turns a deterministic grid into independent samples. |
| R11 NASA-STD-7009B, 2024 | Intended use, acceptance criteria, verification, validation and credibility assessment of models and simulations. | Reference for documenting which research decision R01 can support. Adopted as guidance, without claiming NASA compliance or a regulatory requirement applicable to EA. |
| R12 ACM SIGSIM PADS, 2026 | Artifact evaluation and result reproduction, with separate reports and criteria. | Publishing code and repeating it internally facilitates review; it does not establish independent reproduction or grant an ACM badge. |

<a id="21-pruebas-concretas-en-otras-áreas"></a>
### 2.1 Concrete tests in other areas

These are not merely philosophical analogies. R4 §6 applies abstraction and refinement to hardware designs, including a Fujitsu multimedia processor. R5 §5 checks properties of Zeroconf, WLAN, CSMA/CD, FireWire and a consensus protocol: it compares model and abstraction, precision and verification cost. R6 publishes experiments on probabilistic programs and network software. R3 §7 combines formal results with a comparison of control algorithms against baselines and variability across runs.

The objects, metrics and controls differ from EA. What transfers as precedent is **making the relation explicit, checking it and delimiting conclusions**; not inheriting those works' performance results.

<a id="22-precedente-reciente-relacionado-con-modelos-neuronales"></a>
### 2.2 Recent precedent related to neural models

R13, by Spieker, Gross and Gotlieb (2026), presents a DTMC abstraction of autoregressive generation, conservative intervals, refinement and two cases: process planning with GPT-2 and SMILES molecular generation. It is relevant to distinguishing local acceptance from a domain property. It requires access to model probabilities and an external oracle; it neither proves an EA defense, nor provides a black box test equivalent to Nell's, nor reproduces Hugging Face. It is cited as a complementary recent precedent without making it a necessary foundation of our proof.

R14, Majeed and Hutter (AAAI 2019), addresses homomorphism guarantees even for non-Markovian representations under specific conditions. It supports studying weaker relations if exact equality fails; preserving some value is not equivalent to preserving permissions, traces and all R01 outcomes.

<a id="3-tres-relaciones-que-no-deben-confundirse"></a>
## 3 Three relations that must not be confused

| Relation | What it requires | What it allows one to conclude |
|---|---|---|
| Isomorphism of the relational kernel | Typed bijections preserving operations and relations in both directions. | The declared structure is the same under another representation. By itself it preserves neither probabilities nor decision-maker information. |
| Projected probabilistic equivalence | Preserved initial distribution, events, aggregate laws, observations, paired policies and semantics. | Equality of history laws and preserved metrics within the declared scope and horizon. |
| Conservative simulation or approximation with error | A specific relation and a bounds theorem for the chosen property. | An implication or interval, not necessarily equality or preservation in both directions. |

The complete system with additional variables is not isomorphic to the base. Our criterion combines an isomorphic kernel with a behavioral projection. It is deliberately stronger than preserving only an MDP's optimal value. The product construction in the mathematical note proves that this class exists; it does not prove that an independently defined external domain belongs to it.

The direction of the relation matters too. Removing requirements and granting more capabilities may make a task easier. An impossibility bound transfers only with the appropriate simulation direction and coverage of **all** relevant policies. A correspondence between two fixed policies does not establish a universal bound.

<a id="4-resultado-formal-para-una-comparación-eacontrol"></a>
## 4 Formal result for an EA–control comparison

This section is our own corollary of proposition E1–E7; not an experimental result or an attribution to the references.

Let B be the effective realization `B_{θ*}`, Y the extension and p its projection. Fix horizon H, world distribution, resources, semantics and an integrable measurable history metric m; an indicator may be used for probabilities. Define both arms b∈{EA,C} and check E1–E7 **in each closed system with that arm**, with paired policies. If EA adds memory, messages, evaluation or a repositioning action, those objects and charges must be represented on both sides of its own correspondence. The control is not granted information it would not have, nor EA hidden evaluator truth.

The proposition yields, for each b,

$$
\mathcal L\big(p(H_Y^{\pi_b^Y})\big)
=\mathcal L\big(H_B^{\pi_b^B}\big),
\qquad
m_Y(H_Y)=m_B(p(H_Y)).
$$

Thus, defining an expectation contrast with the same improvement direction,

$$
\Delta_Y(m)=\mathbb E[m_Y(H_Y^{\pi_{EA}^Y})]
-\mathbb E[m_Y(H_Y^{\pi_C^Y})]
=\Delta_B(m).
$$

**Proof.** Equality of laws per arm and factorization of m through p give equality of each expectation; subtract them. No bijection of extra details is required. To additionally transport the distribution of paired differences or its variance, the joint law and experimental coupling must be preserved, not merely the two marginal laws. □

The equality concerns the effective instance θ*, not a θ with smaller radius or different costs. If technology makes queries cheaper or adds capabilities, EA and control must be tested in θ* or robustness to that change justified separately. A sufficient certificate may legitimately eliminate EA's advantage.

A positive estimate of Δ_B has sampling uncertainty. The theorem transports the population contrast under its hypotheses; it does not automatically turn a positive estimate into proof of a positive sign. Statistical uncertainty, correspondence error and measurement error are reported separately.

<a id="41-si-la-conservación-sólo-es-aproximada"></a>
### 4.1 If preservation is only approximate

Equality may be replaced by a bound, but it must be proved. As our own illustrative sufficient condition, let P_b^Y and P_b^B be laws over the **same projected-history space** and suppose

$$
d_{TV}(P_b^Y,P_b^B)\le\rho_b,
\qquad d_{TV}(P,Q)=\sup_A|P(A)-Q(A)|.
$$

For the same metric m∈[0,1], the characterization of total variation through bounded functions gives

$$
|\Delta_Y(m)-\Delta_B(m)|\le\rho_{EA}+\rho_C.
$$

This consequence uses a bound **on complete histories**, not an assumed resemblance between states. If a uniform metric error ν_b is also proved per arm, the bound increases by ν_EA+ν_C. Thus, preserving a strict improvement requires its margin to exceed applicable errors. An experiment uses the lower limit of the contrast interval, not merely its point estimate.

R8 offers a precedent for deriving trace bounds from approximate bisimulation under its own hypotheses. Here ρ_b has **not** been obtained for Hugging Face, Infoblox or an EA execution. Small transition errors may accumulate with the horizon; unbounded costs or qualities and discontinuous thresholds require their own treatment. No bound is assigned from verbal resemblance.

<a id="5-qué-significa-probar-primero-ea-en-el-reducido"></a>
## 5 What testing EA in the reduced model first means

The initial objective is to measure a contribution, not assume superiority. Internal evidence must be capable of being negative and must allow a competent conventional control to resolve the case.

| Proposed step | Evidence or advancement criterion |
|---|---|
| Executable specification | Policies, observations, event order, all charges, metrics and evaluation separated; frozen version. The current fragment does not complete this step. |
| Mechanism contrast | Competent conventional control, EA, ablations and positive control with sufficient evidence. Identify what changes and measure its overhead. Also compare a control using comparable resources to obtain equivalent information, if realizable. |
| Prespecified experiment | Declared world distribution and variations; separate design and evaluation sets; independent runs and, where appropriate, paired worlds. Explicit statistical plan and uncertainty [R10]. |
| Sensitivity and falsification | Vary costs, radius, coverage, topology, deadlines and legitimate quality. Retain cases where EA contributes nothing or harms; do not adjust the generator afterward to recover an advantage. |
| Reproduction | Sufficient artifacts, versions, seeds and records to repeat results; subsequent independent review [R12]. The current finite grid verifies a fragment, not agent effectiveness. |
| Decision to expand resources | Relevant and sufficiently robust improvement, identifiable mechanism, acceptable costs and a concrete domain whose correspondence can be audited. If these are not met, revise or stop that experimental line. |
| Domain scenario | Real integration, correspondences and unomitted operations; tests with agents and operational requirements. The reduced proof guides its design and does not replace execution. |

Quality, admissibility, cost, time, abstention and incompleteness form a vector. Improvement in one dimension may worsen another. “Superiority” requires declaring dominance or a decision rule and its weights; a favorable aggregate result must not hide improper execution or unjustified blocking. There is no already-executed experimental protocol or external preregistration here.

<a id="6-crítica-de-las-afirmaciones-anteriores"></a>
## 6 Critique of previous claims

1. **Foundation of the method versus proof status.** The literature makes testing a reduced model first defensible. It neither completes our implementation nor audits a specific technology's hypotheses. “Strong internal evidence” applies only to a claim with sufficient scope and controls; not any PASS.
2. **Construction versus discovery.** An extension defined by transporting R01 preserves R01 by construction. That is a useful existence proof, but domain adequacy must be checked without defining its semantics to match. Evaluators, domain sources and review should be separated.
3. **Partial observation.** Including history in the evaluator's state may make a representation Markovian; it does not give that history or hidden facts to the agent. Views O_i and policies based on them must be preserved. Populations with their own objectives may require a partially observable game, not a single fully informed controller [R7].
4. **Parameter change.** Tripling radius, making validation cheaper or adding a channel may preserve the structural family and radically change Δ. It does not transfer the previous configuration's performance.
5. **CEGAR in the precise sense.** It requires a defined concrete object, a related abstraction, a property, a counterexample, its concretization and justified refinement [R4–R7]. Our increase in fidelity is inspired by that tradition; we have not implemented that cycle. A spurious counterexample requires refining the abstraction, not modifying the concrete system to make the desired result true.
6. **Conservative safety versus performance ranking.** Abstraction bounds for one arm do not necessarily preserve its comparison with another. Inferring ranking from intervals requires their separation in the improvement direction; equality requires the contract in §4.
7. **Historical causality.** A compatible trace does not prove an incident's cause. The basic receiver rejecting detected prohibitions does not represent continuing after a recognized denial either. That requires another explicit, tested profile.
8. **Method cost and external scope.** Formalizing, mapping, checking and maintaining abstractions has its own cost. The reduced model may be useful even if it later does not permit exact transfer; its value would be isolating and falsifying a mechanism. NASA [R11] guides credibility judgment for a declared use, without certifying our application.

<a id="61-tratamiento-de-la-bibliografía-recibida"></a>
### 6.1 Treatment of the received bibliography

Precedents we could identify and link to a concrete claim are retained. R1 specifically concerns **interval MDPs and PCTL**; its title is not expanded to any PCTL*. R3 distinguishes the finite result from continuous lifting restrictions. R8 is more direct for trace error than a generic reference to “approximate abstraction.” R7 resolves the incomplete title of reference `1701.06209`.

Secondary pages, explainers and Wikipedia are not used as theorem foundations. FDA/ASME on medical devices may contribute credibility ideas, but are not requirements of the EA experiment; a primary simulation reference of more general scope, R11, suffices here. An excluded reference is not presumed false: it is simply unnecessary for this argument. Recent works do not replace established precedents or checking their hypotheses.

<a id="7-afirmación-metodológica-defendible"></a>
## 7 Defensible methodological claim

> R01 is an experimental abstraction for isolating a mechanism of exploration, costly review and social reuse of evidence. EA's incremental contribution will first be evaluated against competent conventional controls, with explicit resources and metrics. Results will have the scope of the tested model, configuration and policies. A comparative conclusion will transfer only when a relation preserving both arms and relevant properties is proved, or an error bound sufficient to sustain that conclusion. Reduced evidence will guide and justify, where appropriate, tests in more complete scenarios; it will not replace their empirical validation.

<a id="8-referencias-primarias-y-localizadores"></a>
## 8 Primary references and locators

Sources consulted on 2 October 2026. Versions are fixed where appropriate; references establish their own results, not EA validation.

- **R1.** Vahid Hashemi, Hassan Hatefi and Jan Krčál. *Probabilistic Bisimulations for PCTL Model Checking of Interval MDPs*. EPTCS 145, 2014. Definitions, preservation and computational case. https://arxiv.org/abs/1403.2864v3
- **R2.** Lihong Li, Thomas J. Walsh and Michael L. Littman. *Towards a Unified Theory of State Abstraction for MDPs*. ISAIM 2006. §§3.3–3.4 and examples in §4; distinction between preserving model, values and policies. Author's copy: https://thomasjwalsh.net/pub/aima06Towards.pdf
- **R3.** Sahand Rezaei-Shoshtari, Rosie Zhao, Prakash Panangaden, David Meger and Doina Precup. *Continuous MDP Homomorphisms and Homomorphic Policy Gradient*. NeurIPS 2022. Definitions 1/3, theorems 1–3, §7 and appendix B. https://arxiv.org/abs/2209.07364v1 · Text: https://arxiv.org/html/2209.07364v1
- **R4.** Edmund Clarke, Orna Grumberg, Somesh Jha, Yuan Lu and Helmut Veith. *Counterexample-guided Abstraction Refinement*. CAV 2000. §§3–4, cycle and concretization; §6, experiments. https://web.stanford.edu/class/cs357/cegar.pdf
- **R5.** Mark Kattenbelt, Marta Kwiatkowska, Gethin Norman and David Parker. *A Game-Based Abstraction-Refinement Framework for Markov Decision Processes*. Oxford report CL-RR-08-06, 2008. §§3–4, bounds and refinement; §5, experiments. https://www.prismmodelchecker.org/papers/RR-08-06.pdf
- **R6.** The same authors. *Abstraction Refinement for Probabilistic Software*. VMCAI 2009, LNCS 5403, pp. 182–197. Implementation and experimental tables 1–2. https://www.prismmodelchecker.org/papers/vmcai09.pdf
- **R7.** Xiaobin Zhang, Bo Wu and Hai Lin. *Counterexample-Guided Abstraction Refinement for POMDPs*. 2017. §§III–IV, simulation and refinement; §V, example. Scope: finite-horizon safe-PCTL. https://arxiv.org/abs/1701.06209v4 · Text: https://arxiv.org/html/1701.06209v4
- **R8.** Gaoang Bian and Alessandro Abate. *On the Relationship between Bisimulation and Trace Equivalence in an Approximate Probabilistic Context (Extended Version)*. FoSSaCS 2017. Relation between approximate bisimulation and finite-horizon trace distance. https://arxiv.org/abs/1701.04547v3
- **R9.** Timm Spork, Christel Baier, Joost-Pieter Katoen, Jakob Piribauer and Tim Quatmann. *A Spectrum of Approximate Probabilistic Bisimulations*. CONCUR 2024. Relations between approximate notions for labeled Markov chains. https://arxiv.org/abs/2407.07584v1
- **R10.** Rishabh Agarwal, Max Schwarzer, Pablo Samuel Castro, Aaron Courville and Marc G. Bellemare. *Deep Reinforcement Learning at the Edge of the Statistical Precipice*. NeurIPS 2021; revised version 2022. Comparative evaluation, intervals and profiles. https://arxiv.org/abs/2108.13264v4
- **R11.** NASA. *NASA-STD-7009B: Standard for Models and Simulations*, 5 March 2024. §§4.1–4.3, use, acceptance, V&V and credibility. https://standards.nasa.gov/standard/NASA/NASA-STD-7009 · Document: https://standards.nasa.gov/sites/default/files/standards/NASA/B/1/NASA-STD-7009B-Final-3-5-2024.pdf
- **R12.** ACM SIGSIM PADS 2026. *Reproducibility and Artifact Evaluation*. Artifact and reproduced-result criteria; review and reports. https://sigsim.acm.org/conf/pads/2026/blog/artifact-evaluation/
- **R13.** Helge Spieker, Dennis Gross and Arnaud Gotlieb. *Probabilistic Model Checking of Autoregressive Neural Sequence Models*. arXiv, September 2026; the record declares ICTSS 2026. §3, DTMC, soundness and refinement; §4, cases. https://arxiv.org/abs/2609.00838v1 · Text: https://arxiv.org/html/2609.00838v1
- **R14.** Sultan Javed Majeed and Marcus Hutter. *Performance Guarantees for Homomorphisms Beyond Markov Decision Processes*. Extended version, 2018; short version AAAI 2019. §5 and appendices: guarantees under aggregation conditions. https://arxiv.org/abs/1811.03895v1

