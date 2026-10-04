# R01 — Differential and value of the experiment

Iván Abril Palma, Tegrity.AI · Ecosystem Awareness research line

Research positioning v0.1 · 3 October 2026 · Targeted literature review and proposed contribution; no new experimental results

[Main R01 README](./README.md) · [Complete scenario](./Escenario-creatividad-validacion.md)

## 1. Purpose: a technology–problem suitability map

**R01 proposes a bounded experimental method for mapping where a technology or architecture is suitable for a problem, assessed through cost, risk and effectiveness.** The intended use is upstream: inform architecture selection, configuration and investment before a larger deployment. “Technology–problem suitability map” is a descriptive name for this intended output, not a claim to have invented algorithm selection or multidimensional evaluation.

The five elements have different roles:

| Element | Role in the map | R01 interpretation |
|---|---|---|
| Technology / architecture | What is evaluated | A versioned implementation and complete policy: exploration, validation, memory, communication, controls and execution. A vendor or model name alone is insufficient. |
| Problem | Where it is evaluated | Task, mandate, dependencies, segment benefits, geometry, available information and resource conditions. |
| Cost | Resources consumed | Search, checking, execution, coordination and evidence maintenance, including unsuccessful attempts. Latency is reported separately; parallel execution does not imply less total work. |
| Risk | Exposure to unacceptable outcomes | Executed violations, their frequency and declared severity, with uncertainty. Blocked proposals, attempted actions and actual effects remain distinct. An obligation violation is not automatically a measured harm. |
| Effectiveness | Useful legitimate delivery | Completion and quality relative to the admissible optimum, within the declared deadline. Abstention and incomplete work are visible outcomes. |

Technology and problem are the two comparison dimensions; cost, risk and effectiveness are three outcome families. This presentation does not replace the scenario's more detailed vector of legitimate quality, cost, latency, completion, violations and coordination (§1.4), or its existing success criterion.

The map should identify tested regions where requirements are met, regions where the evaluated competent policies fail to meet them, and regions with insufficient evidence. Relative preference between architectures is a separate comparison: several may be adequate, with different tradeoffs. The result can be a table or several projections; it need not be a single score or a literal five-dimensional chart. Mandatory constraints are not compensated by higher reward.

The practical value sought is a justified decision to adopt, adjust, combine, use another procedure or gather more evidence. Broad application is an ambition: a new problem family enters the map only after its correspondence, observables and evaluation reference have been justified.

## 2. What is already being measured, and by whom?

**The broad claim that nobody measures these concerns is not supported.** Established work maps algorithm suitability; current agent research measures cost, utility, safety and reliability; sample-efficient evaluation also has prior methods.

This targeted review consulted primary papers, authors' software and institutional project pages on 3 October 2026. Search strands covered algorithm selection and instance spaces, multi-metric evaluation, agent cost and reliability, multi-agent authorization and security, imperfect verification, and evaluation with limited samples. It is a positioning review, not an exhaustive systematic review or an independent reproduction. Publication, reported execution and independent validation are different evidence levels.

| Work / researchers | What the consulted source establishes | Consequence for R01 |
|---|---|---|
| **Instance Space Analysis / MATILDA — Kate Smith-Miles and Mario A. Muñoz** [D1] | Builds algorithm performance regions from problem-instance features, supporting selection and identifying areas needing more evidence. Published methodology and available software. | The upstream map and suitability-region idea have direct precedent. R01 must specify what its problem construction and joint admissibility/resource treatment add. |
| **HELM — Stanford CRFM** [D2] | Evaluates models across scenarios using multiple measures, including accuracy, robustness, toxicity and efficiency. | Crossing technologies, problems and several outcomes is established. These metrics are not identical to R01's operational definitions. |
| **AI Agents That Matter; HAL; Agent Reliability — Princeton SAgE, including Sayash Kapoor, Arvind Narayanan, Benedikt Stroebl and Stephan Rabanser** [D3] | Cost-controlled agent comparisons and a separate reliability programme covering consistency, robustness, predictability and safety. HAL's main page states that new-model leaderboard updates are paused while work focuses on reliability. | Cost-aware selection and task-dependent reliability are active research. R01 cannot distinguish itself merely by going beyond completion. |
| **AI Control — Ryan Greenblatt, Buck Shlegeris and colleagues, Redwood Research** [D4] | Evaluates safety and usefulness under limited trusted oversight; follow-up work varies auditing and intervention strategies. | Bounded oversight and safety–usefulness tradeoffs already have experiments. R01's constructive search and compositional admissibility are a different proposed experimental focus. |
| **ORBIT — Ben Hagag, William L. Anderson, Srija Chakraborty and Christian Schroeder de Witt** [D5] | A configurable multi-agent framework with architecture/defense comparisons, non-adversarial settings and security–performance measurements. Cooperative allocation includes an optimality reference. | Topology, interaction, benign failure and distance from an optimum are not exclusive to R01. ORBIT is a possible implementation substrate; framework extensibility is not evidence that its published campaign already tested R01. |
| **MasDrift — Zhuoning Xu and coauthors** [D6] | Measures authorization preservation and task utility across coordination structures; reports tokens, tool calls and defense overhead. Its tasks span eight domains and do not require an attacker. | This is close prior work on architecture-dependent utility, violations and cost. R01 needs a distinction more precise than measuring those three outcomes. |
| **AgentOps-Bench — Kunwar Shivam Srivastav** [D7] | The public software release reports completion, cost, efficiency, reliability, recovery and prompt-injection safety on a shared task suite. | A direct counterexample to a blanket absence of joint measurement. This review inspected the project description; it did not replicate the pilot or establish independent validation. |
| **Active Testing — Jannik Kossen and colleagues; tinyBenchmarks — Felipe Maia Polo and colleagues** [D8] | Methods for reducing evaluation sample requirements while estimating model performance. Published papers and software. | A small or bounded evaluation is not itself novel. R01 must validate the information its pilot provides about suitability boundaries, particularly rare failures. |
| **The Limits of Inference Scaling Through Resampling — Benedikt Stroebl, Sayash Kapoor and Arvind Narayanan** [D9] | Studies limits of repeated solution sampling with imperfect verifiers, including false positives and their utility consequences. | Search, checking and resource expenditure already interact in related research. R01's claimed contribution must address composition and shared evidence explicitly. |

The common metrics are not interchangeable: resistance to a fixed injection catalogue, authorization preservation, reliability and real-world expected harm describe different constructs. The table records overlap rather than treating every safety measure as the same risk estimate.

## 3. The candidate differential

**The defensible proposal is a specific, testable experimental construction for explaining suitability boundaries, followed by validation of whether limited pilots can identify those boundaries.** It is not novelty in the five labels.

In the consulted material, this review did not identify a published campaign matching the following combination as its central design. That is a bounded review finding, not proof of priority or of scientific significance:

1. **Three reference routes with distinct roles.** M is the known permitted procedure; I is the evaluator's best complete admissible solution; P is attractive but inadmissible. Agents must discover and evaluate candidates without receiving I/P labels.
2. **Segment-level heterogeneity and compositional admissibility.** Benefits vary while controlled means are retained; distances and connectors vary explicitly. A useful local segment must be assessed with its prefix, connector and continuation.
3. **Exploration and validation compete for finite resources.** Radius, inspection coverage, search/review costs and deadline can be changed separately. The experiment charges discarded alternatives, retries, evidence use and maintenance.
4. **Social information can help or mislead without changing authority.** Complementary coverage, duplicated checks and relayed reports are separated. Population size, connectivity and total resources must not be conflated.
5. **The output is an empirical suitability boundary.** Legitimate quality, violations, completion, cost and time jointly locate where declared competent policies succeed, become inefficient, deliver insufficient quality, violate obligations or remain inconclusive.

These mechanisms are specified in the [complete scenario, §§1.2–1.7 and 2.1–2.18](./Escenario-creatividad-validacion.md). Merely assembling familiar mechanisms does not establish a contribution: the campaign must show what decisions or explanations the combination enables beyond existing evaluation.

The first question concerns the base architecture's scope. **EA is a subsequent candidate intervention**, compared with competent conventional controls using equivalent information and fully charged resources. An unchanged boundary, a cheaper conventional solution, or a negative EA result remains informative.

### Initial adversarial findings

- **“The five-element map is new.” Rejected as a broad claim.** Instance-space mapping and multi-metric evaluation already cover that level of abstraction.
- **“Three routes establish originality.” Not established.** M/I/P are reference roles, not three competing policies; the labels alone do not distinguish R01 from constrained search or optimization.
- **“No identical parameter bundle was found, so the experiment is valuable.” Insufficient.** Added parameters may increase evaluation expense without improving a decision. A simpler construction must be tested as a baseline.
- **“An exact oracle makes a small pilot trustworthy at scale.” Rejected.** Oracle correctness establishes internal scoring; sampling, rare-event precision and transfer need separate evidence.
- **“The proposed design demonstrates EA's advantage.” Rejected.** Comparable provenance, certificates and incremental validation may reproduce any benefit at lower cost.

What survives this first check is a research question about the explanatory and decision value of the combined construction. Its answer remains open.

The Hugging Face and Infoblox/DNS extensions provide concrete questions and transfer obligations. They study selected compatible mechanisms; neither full historical reconstruction nor coverage of every cause in those incidents is claimed. See the [incident scope rule](./README.md#incident-scope).

## 4. What would establish value beyond existing evaluation?

Two stages must remain separate:

| Stage | Evidence needed | What would limit the contribution |
|---|---|---|
| **Construct and measure the map** | Reproducible worlds, competent policies, paired comparisons, mechanism ablations, explicit thresholds and uncertainty; retain the same problem distribution when comparing regions. | Boundaries caused by weak comparators, leaked oracle information, omitted costs or a generator that forces the desired result. |
| **Validate a bounded pilot as a decision instrument** | Use only information available in a small pilot to classify or select on held-out problems; compare with simpler baselines and relevant selection methods. Report wrong approvals, wrong rejections, inconclusive decisions and evaluation expenditure. | No improvement in decision quality or evaluation effort, unstable predictions, or inability to recognize configurations outside the validated scope. |

The second stage is a research objective, not a capability established by the scenario. A limited pilot with no observed violations cannot establish zero risk. The required precision for rare events may make a small pilot inconclusive.

Broader usefulness requires replication across admitted problem families. The outcome sought is evidence about when a decision is supportable at a given evaluation budget, including when further testing is necessary.

## 5. Clarify the oracle before expanding the campaign

For small constructed R01 worlds, an exact evaluator is a concrete next implementation target:

- **Ground truth:** fix the graph, mandates, admissibility predicate, benefits, costs, versions and horizon before policy execution.
- **Admissible optimum:** compute the best complete permitted trajectory, including allowed mixtures and connectors. A route called I by the generator cannot override a superior admissible composition.
- **Trace adjudication:** independently reconstruct actions and effects; distinguish proposed, blocked and executed violations; calculate legitimate delivery and the resource ledger.
- **Information boundary:** withhold the evaluator's full map and labels from agents. Their checks use the same access and charging contract in every arm.

Publish witness trajectories and small exhaustive cross-checks to make the reference inspectable. Report evaluation/oracle construction cost separately from the system's operational cost: a bounded evaluation claim must account for both, without charging evaluator-only work to one comparator.

The oracle establishes truth within the constructed world. It is not a predictor of real-world suitability, a source of free evidence for agents, or a replacement for validating the correspondence of an extension. Earlier extension checks have their own scope; they do not constitute the complete R01 oracle.

## 6. Research positioning and immediate collaboration value

A suitable research proposition is:

> Develop and validate a technology–problem suitability map through bounded experiments measuring cost, risk and effectiveness, beginning with R01's controlled exploration, compositional validation and evidence-sharing scenario.

The reviewed work suggests complementary counterparts: **MATILDA/Instance Space Analysis** for mapping and selection methodology; **Princeton SAgE** for cost-aware evaluation, reliability and verification limits; **ORBIT's authors** for multi-agent execution infrastructure; and **MasDrift/AI Control researchers** for strong authorization and oversight comparators. These are inferred technical fits, not confirmed interest or commitments.

The first collaboration can deliver an inspectable oracle, frozen baseline policies and one bounded campaign. R01's current first-campaign scope remains that of §2.15; the full parameter inventory need not be crossed at once. Authorship, prior R01/EA contributions, responsibilities and publication of negative results should be explicit.

**Current assessment:** the general evaluation ambition has substantial prior art. R01 offers a plausible specific research contribution in the construction and explanation of suitability boundaries, and a further hypothesis about diagnosing them with limited pilots. Implementation, execution, independent review and transfer validation remain necessary. This note records positioning and value, not a demonstrated EA advantage.

## Sources and review locators

Primary sources consulted on 3 October 2026. Versioned papers are identified where available. Project pages and repository READMEs are snapshots of their stated scope; numerical claims were not independently reproduced.

- **[D1]** Smith-Miles and Muñoz, *Instance Space Analysis for Algorithm Testing: Methodology and Software Tools* (2023), DOI 10.1145/3572895; authors' toolkit, opening methodology and footprint description: https://github.com/andremun/InstanceSpace . MATILDA: https://matilda.unimelb.edu.au/matilda/ .
- **[D2]** Stanford CRFM, *Holistic Evaluation of Language Models*, especially multi-metric measurement and scenario coverage: https://crfm.stanford.edu/2022/11/17/helm.html .
- **[D3]** *AI Agents That Matter*: https://arxiv.org/abs/2407.01502 . HAL method: https://hal.cs.princeton.edu/about ; update status: https://hal.cs.princeton.edu/ ; reliability dimensions, methodology and team: https://hal.cs.princeton.edu/reliability/ ; paper: https://arxiv.org/abs/2602.16666 ; SAgE programme: https://sage.cs.princeton.edu/ .
- **[D4]** *AI Control: Improving Safety Despite Intentional Subversion* (ICML 2024): https://proceedings.mlr.press/v235/greenblatt24a.html . Current programme: https://www.redwoodresearch.org/research/ai-control ; auditing-budget follow-up: https://www.redwoodresearch.org/blog/retrying-vs-resampling-in-ai-control .
- **[D5]** *ORBIT*, v1 (27 September 2026), §§3.2–3.4, §5 and Appendix F.5: https://arxiv.org/html/2609.33102v1 .
- **[D6]** *MasDrift*, v2 (11 August 2026), §§3–5 and Appendices E.4 and F.1–F.2: https://arxiv.org/html/2608.07556v2 .
- **[D7]** *AgentOps-Bench*, README sections “What's measured” and “Limitations”; software/pilot release, review status not established here: https://github.com/kunwarshivam/agentops-bench .
- **[D8]** *Active Testing: Sample-Efficient Model Evaluation* (ICML 2021): https://proceedings.mlr.press/v139/kossen21a.html . *tinyBenchmarks: evaluating LLMs with fewer examples* (ICML 2024): https://proceedings.mlr.press/v235/maia-polo24a.html .
- **[D9]** *The Limits of Inference Scaling Through Resampling*, v3 (26 March 2026; earlier versions used the title “Inference Scaling fLaws”): https://arxiv.org/abs/2411.17501v3 .

<a id="robot-review-plan"></a>
## Robot review plan — pending work on this document

<!-- R01_BOT_WORKPLAN_START version="0.3" scope="DIFFERENTIAL_AND_EXPERIMENT_VALUE.md" -->
**Shared-label reconciliation, 3 October 2026.** `R01_BOT_WORKPLAN_START` and `R01_BOT_WORKPLAN_END` are the canonical discovery markers for this plan, [mathematical feasibility](./MATHEMATICAL_FEASIBILITY.md), [computability and oracle](./COMPUTABILITY_AND_ORACLE_PLAN.md), and [HF technology tasks](./extensions/hugging-face/REMAINING_TASKS.txt). The existing maintenance label below identifies this document only; it does not replace the shared markers. At creation, P01–P09 were open with their original criteria. Current status: P03 is DONE for measurement-validity specification/audit; P10 is IN_PROGRESS for the decision/value gate. Other P tasks remain OPEN. P04 is developed by C01–C10; P05/P08/P09 also apply to the new workstreams. See the [entry and order](./README.md#bot-start-here).

**Maintenance label: R01-DIFFERENTIAL-REVIEW.** Keep this work plan in this document. It is not a website robots.txt, a separate instructions file or a scheduled automation. Preserve task identifiers; record date, exact version reviewed, evidence, finding and remaining uncertainty when closing a task. Do not mark work complete from a plan, an inaccessible reference or a passing check with a different scope.

**Baseline and initial checks:** repository commit `626c7822a50cd2779730c46cca3cfbbc4eb381eb`. The README and complete scenario receive one navigation paragraph each; removing those additions restores their previous text exactly. Local relative-link targets in the three affected Markdown files were checked. This narrow preservation check does not resolve the inherited package-audit failures recorded in P08.

**Initial pass:** primary-source positioning review and an adversarial editorial check performed on 3 October 2026. The review rejected blanket originality claims about suitability maps, joint metrics and small evaluations. It separated the proposed R01 combination, pilot-to-map inference and EA advantage. No external experiments were replicated. Nine further focused passes remain; each can be split if a concrete defect requires it.

| ID / status | Next pass and concrete task | Evidence required to close |
|---|---|---|
| P01 — OPEN | **Deepen and audit references.** Extend the search to constrained algorithm selection, safe/ constrained optimization, multiobjective instance spaces, experimental design and multi-agent verification. Read full methods for the closest candidates; freeze source versions and verify every table statement, author, date and link. | A claim-to-source matrix with exact sections, search coverage and disagreements. Remove or narrow every unsupported distinction. |
| P02 — OPEN | **Adversarial self-audit of the differential.** Assume R01 is a repackaging of existing methods. Try to reproduce its claimed decision value using MATILDA-style mapping, HAL/AgentOps-style measures, ORBIT/MasDrift controls and ordinary provenance/caching. Challenge each of the five proposed mechanisms separately and jointly. | Explicit counterarguments, closest equivalent construction and a falsification test for each surviving contribution. If equivalent value already exists, acknowledge it and redefine the contribution. Do not treat a different name as a mechanism. |
| P03 — DONE (measurement audit) | **Audit measurement validity.** Check the cost ledger, legitimate quality, completion, latency, violation frequency/severity and uncertainty against the scenario. Test abstention, zero observed violations, cheap low-quality delivery, expensive valid delivery and duplicated social evidence. | An unambiguous mapping to §1.4 and edge-case outcomes. No hidden compensation for prohibitions, duplicate cost, unreported missing delivery or conversion of violations into quantified harm without a model. |
| P04 — OPEN | **Specify and audit the oracle.** Turn §5 into a bounded executable contract, including mixed routes, connectors, ties, information isolation and independent trace scoring. Challenge privileged evidence and evaluator errors. | Inputs, outputs, witness cases, exhaustive tiny-world cross-checks and a declared cost model. Distinguish a specification from an implemented oracle and from an executed campaign. |
| P05 — OPEN | **Check coherence across the corpus and transfer limits.** Compare with current 00M, 00N, 00D, canonical requirements, the three extensions and R01 §1.7. Check terminology, authority boundaries, trial status and what a small pilot can establish. | Explicit document/version correspondences; resolve contradictions without rewriting canonical semantics or implying historical incident reconstruction. |
| P06 — OPEN | **Editorial and readability review.** Test whether both a research reader and an architecture decision-maker can identify the question, prior art, contribution, status and next experiment without reading the whole corpus. Reduce repetition and qualify ambiguous wording. | A short comprehension checklist and recorded corrections; preserve technical distinctions and source attribution. |
| P07 — OPEN | **Review visual aids.** Assess whether the five-element table, prior-work comparison and two-stage evidence table are sufficient. If useful, add a clearly conceptual suitability-map example showing adequate, inadequate and unresolved regions. | A readable rendering, accessible labels and a caption identifying synthetic illustration. Never draw invented empirical boundaries or imply observed results. |
| P08 — OPEN | **Preservation, navigation and inherited audit repair.** Verify additions against the preceding Git versions; inspect all inbound/outbound links. Reconcile historical trace manifests through an explicit successor record before claiming current package integrity. | A preservation diff and successful scoped checks. The unmodified downloaded baseline already failed `extensions/verify_audit.py --verify` at the scenario hash assertion. Comparison also found mismatches against `INCIDENT_SCOPE_TRACE.json` for the Infoblox/family READMEs and their SHA256 manifests. Do not silently overwrite historical hashes or call these failures new experimental evidence. The two new navigation additions also require coverage in a future successor trace. |
| P09 — OPEN | **Final adversarial release review.** Reassess the strongest novelty claim after P01–P08; test whether the proposed campaign can distinguish it from a simpler alternative. Seek independent review separately when available. | A dated disposition for every finding, explicit residual limits and a justified next version. Self-review must never be described as independent validation. |

This plan concerns improving the note and its evaluation contract. It does not mean nine passes have been completed, nor that the full R01 implementation and campaign are included in this editorial update. Pending work remains visible until its evidence is recorded.


### Strategic revision and execution gates — 3 October 2026

Planning revision v0.2; review against commit `1e940125a18f468268eff8f029a35c32a5f4ff08`. This is a documentary self-review, not a mathematical validation or independent review. Read the [master execution prompt](./STRATEGIC_WORKPLAN_AND_EXECUTION_PROMPT.md) for priorities, the complete task register and release gates. Existing IDs and acceptance criteria remain in force. New tasks are OPEN. A documentary revision does not close an implementation, proof or empirical task.

**Scheduling clarification:** reviews are recurring passes, not a reason to defer source checks, counterexamples or preservation until the end. Start P08/C01 baseline triage, M01/P03/P10 scope and measurement, and the minimum relevant P01/P02/M06 source-and-counterexample review together. Later passes complete their original criteria. Keep mathematical region proof, neutral evaluator implementation, base campaign, technology admission and prospective architecture selection as separate outputs. A rejected mathematical candidate does not block a neutral evaluator or a clearly scoped experiment.

**Shared closure record:** task ID/status, owner, actual UTC date, input commit, exact scope, assumptions, evidence paths, commands and outcomes, review disposition, residual limits and next action. No assigned owner is invented: use UNASSIGNED until responsibility is accepted. Different tasks may reference one evidence artifact, but retain their own acceptance decisions. Reopen affected tasks when a material contract changes. Independent review is desirable evidence, not a prerequisite for starting authorized internal work; self-review must retain its label.

**Research ordering:** P10 and a targeted P01/P02 pass precede broad campaign investment. P03 specifies measurement before C02/C11 are frozen; P04 reviews the C-workstream's artifacts rather than commissioning a duplicate oracle. P08 has an immediate triage pass and a later preservation/release pass. P11 specifies and audits later pilot-based selection; P12 checks its decision and transfer evidence. P09 closes only the declared release scope, with later-stage tasks explicitly retained OPEN when not included.

| Added ID / status | Dependency and activity | Evidence needed to close |
|---|---|---|
| P10 — IN_PROGRESS (decision input) | Start with M01/P03; revisit after targeted P01/P02. Define the decision and research continuation gates. | Identify the architecture choice the study informs, alternatives, falsifiable incremental value, minimum useful evidence and expenditure ceiling. Freeze continue/narrow/reframe/stop dispositions. Equivalent prior work or a simpler adequate method may change the contribution without invalidating the instrument. Separate useful engineering evidence, novelty and EA advantage. No full survey is required before tiny neutral instrument work, but the closest relevant prior art must be checked before broad claims. |
| P11 — OPEN | After the initial P03/P10 contract, design the later selection protocol before C14; review C11 and C12 as input. | Target decision, eligible small-pilot inputs, ground-truth outcome reference, comparator/selector training split, held-out distribution, rare-event precision and predeclared asymmetric error costs. Assess whether information available before selection can support the decision; register indeterminate output and out-of-distribution handling. The first campaign remains outcome measurement, not prior diagnosis. |
| P12 — OPEN | After C14 for a selector claim; with P05/P11 and relevant T06/T12 for transfer. | Test whether bounded pilots improve architecture-choice accuracy or evaluation effort over simpler methods. Report coverage, wrong approvals/rejections, diagnostic cost and uncertainty; vary relevant length, population, dependency, change and information-volume factors or justify a bound. Record what transfer/scale claims survive, fail or remain unresolved. No one-world success or correct oracle implies deployment suitability. |

**Verified inherited audit disposition:** at this review's fixed commit, all 39 downloaded R01 text/code blobs match Git blob identities. The HF, Infoblox and family finite checkers exit successfully and reproduce their recorded reports in isolation. The unchanged common verifier fails at the current scenario digest. SHA256 manifests mismatch all three extension READMEs (HF included), not only Infoblox/family. This updates the known scope of P08; it does not close it. Preserve historical manifests, reconstruct intervening edits and issue an explicit successor record/verifier rather than overwriting old expectations. This planning revision leaves the scenario, scripts, reports and old freezes unchanged.



### P03 execution record and P10 initial input

**P03 DONE — measurement-validity specification/audit only.** [M10/P03 contract and case dispositions](./M10_P03_CONTRACT_AND_MEASUREMENT_AUDIT.md) · [Contract](./M10_RECONCILED_CONTRACT.json) · [35 diagnostic checks](./M10_MEASUREMENT_CHECKS.json) · [Checker](./verify_m10_measurements.py) · [Acceptance/preservation](./M10_RELEASE_CHECKS.json).

The audit maps q/a/e/f/C/t/K to scenario §1.4 and keeps technical finish, legitimate delivery and success separate. It retains abstention costs, expensive/late/unknown records, campaign violations after recovery and undefined ratios with zero denominators. Cost per legitimate delivery uses a=1; cost per joint success uses e=1. Actual repeated work/communication is charged; copied ledger records and dependent evidence are not counted as new work or independent coverage. Severity is not converted to harm without a model. The zero-event IID binomial example gives a nonzero risk bound; it is not campaign data or a sample-size recommendation. C11's statistical protocol and C04/C05's independent implementation remain OPEN.

**P10 IN_PROGRESS:** the initial continuation decision favors a scoped one-bit M03 proof/benchmark and rejects an L-growing or price-independent generalization from M02. A simpler state-query/certificate control resolves several profiles. The wider architecture-choice, incremental-value and expenditure-ceiling gates remain to be completed before broad investment. [Targeted primary-source and counterexample intake](./M06_PRIMARY_SOURCE_INTAKE.md) supports this narrow disposition; P01/P02 remain OPEN. Owner/reviewer: Codex, on user instruction; same-agent review. The evidence record pins input/UTC time and residual limits.



### P10 continuation input — mathematical family result

[The M03/M04 successor](./M03_M04_TRILEMMA_THEOREMS.md) establishes a conditional all-policy trilemma for two constructed families, including dense conjunctive dependencies, exact AVG/WC hard frontiers and a separate expected-cost lower bound. These results support building a neutral small oracle and independent review. They do not establish novelty, empirical EA advantage, a product's certificate price, or the value of a pilot for choosing architecture. P10 remains IN_PROGRESS; P01/P02/P11/P12 and statistical/technology gates retain their acceptance criteria.

The document provides explicit reduced/eliminated-band controls for cheaper raw access, sufficient certificates, preeffect barriers and authorized execution included in baseline cost. Technology admission must identify the fresh normative facts, query/enforcement interface and full producer cost before transferring the bounds. Positive information price alone is insufficient. The F/W supplemental contract retains canonical e/a/q; technical eta is reported separately. Next contribution decision follows independent M05/C05 review and M07 correspondence, rather than a model campaign justified by these constructed examples alone.

### Orden vigente — la prueba y el valor empírico tienen cierres separados

Reorganización v0.3: [plan rector](./STRATEGIC_WORKPLAN_AND_EXECUTION_PROMPT.md#mathematical-strengthening), 55 tareas. P03 sigue DONE para la auditoría histórica; P10 IN_PROGRESS; el resto de P conserva OPEN. P01/P02 y M06 acompañan M12 y la revisión matemática desde el inicio: comparar las afirmaciones concretas F/W/G/T con fuentes primarias, sin atribuir novedad a la cota de conteo por defecto. P08 hace triage y conserva los fallos heredados; cada sucesor precisa alcance de integridad.

M13 prueba clases tecnológicas; T02 investiga pertenencia concreta. M17 prueba el puente de imposibilidad; P05/M07 revisan coherencia documental, que no sustituye ese argumento. P04 usa el instrumento mínimo comprobado. P06/P07/P09 y M08/M09 recurren en las entregas matemáticas. P11/C14/P12 siguen posteriores: una prueba del trilema no demuestra que un piloto mejore decisiones ni que EA sea superior. Antes de cada inversión empírica, P10 debe indicar la incertidumbre que resuelve y su criterio de continuar/acotar/parar.

Conservar las evaluaciones y referencias históricas; el orden vigente reemplaza sus instrucciones de siguiente paso cuando difieran. Esta reorganización no cierra diferencial, literatura, utilidad ni auditoría independiente.


### Material adicional: validación primero

[Dossier y originales](./supplemental/2026-10-04/README.md) aportan ataques para M06/P01/P02/M11 y una cola tecnológica posterior M13/T. La fuente de group testing es un antecedente pertinente de conteo, sin afirmar identidad de todo el trilema ni novedad. Ninguna ocurrencia empírica, clasificación de frameworks o utilidad del piloto queda validada por estos scripts. M12 fija primero qué información basta para la entrega y qué observaciones/costes pertenecen al problema; luego se revisan las pruebas. Las pistas de familia escasa y frescura tienen contraejemplos/lagunas que deben conservarse.

<!-- R01_BOT_WORKPLAN_END -->
