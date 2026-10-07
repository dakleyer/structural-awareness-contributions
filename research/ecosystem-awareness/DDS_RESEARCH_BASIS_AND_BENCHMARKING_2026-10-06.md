# DDS — Research basis, benchmarking and value proposition

<!-- DDS terminology revision 1 (2026-10-07): Stage A/B/C only; source scientific version and evidence unchanged. -->

Supporting dossier v0.1 · Reviewed:2026-10-06 · Written for technology providers, deployment owners and reviewers.

Review/navigation: [sole owning sourcebook review](./DDS_RESEARCH_BASIS_AND_BENCHMARKING_2026-10-06_VNext.md). Supporting research; the [DDS Canonical Method Index](./DDS_CANONICAL_METHOD_INDEX_v0.1.md) is the method authority, with Gate-specific technical detail owned by Stages A/B/C.

This dossier explains the research basis and documentary positioning of the Deployment Differential Study. The current method entry point is the [DDS Canonical Method Index](./DDS_CANONICAL_METHOD_INDEX_v0.1.md), with [Stage A — Specification Discovery](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md) retaining the challenge–trajectory material reviewed in this dossier at source pin [ba5e8081](https://github.com/dakleyer/structural-awareness-contributions/commit/ba5e8081beff2d4728f043839cb2ea0376a94c57). It is an annotated literature/benchmarking companion, not another canonical method or the 00D comparator/fairness source.

Read the overview and comparison tables first; use the reference annotations for technical due diligence. The review is by the same Codex assistant. Source selection and documentary comparison were completed; shared-fixture commercial/vendor performance comparison and independent validation were not performed.

## 1. The decision a DDS helps answer

A technology can work well and still be a poor fit for a particular decision, workload, authority boundary or response window. A DDS studies one declared technology/configuration against one bounded problem so the reader can see what it enables, what a competent alternative already provides, where its contribution stops and what burden or uncertainty remains.

For a buyer, the useful output is a defensible adoption, redesign, configuration or further-test decision. For a provider, it is a credible account of a capability and its limits under stated conditions. The finding can support improvement, equivalence, a trade-off, no material differential or insufficient evidence. Funding cannot purchase a favorable result.

The proposed premium value is the disciplined integration of problem definition, mechanism/transfer review, strong-reference comparison, traceable evidence and conditional deployment interpretation. It is a service-quality proposition to demonstrate case by case. Literature establishes the relevance of its building blocks; it does not establish exclusive invention or superior performance.

## 2. A deliberately simple method

The core remains: define the question and scenario; map the technology; separate preserved structure from non-isomorphic mechanisms; examine the scoped routes and evidence; report cost/risk/effectiveness and any justified business interpretation; close with the supported finding and limits. A small documentary or analytical study can use only the relevant surfaces and stay traceable to the same DDS.

Stage1 — Technology–problem extension/isomorphism profile: pin the base and configuration, identify preserved correspondence and parameter changes, and state proof/transfer obligations. R01 retains its own E1–E7 contract. Another base requires its own justification.

Stage2 — Non-isomorphic mechanisms: study information, authority, transitions, human intervention or other mechanisms outside the established kernel, including useful/failure cases, cost/time and composition. A proof about a kernel does not automatically prove the whole configuration.

Proportionality is operational: select enough evidence to answer the agreed question; examine the material assumption or boundary that could reverse the finding; state conditionality if it cannot be checked. Closing analysis with a bounded answer does not waive agreed outputs. This literature library introduces no extra mandatory stage, universal battery or client deliverable.

## 3. What the research base supports

The foundation spans risk/quality frameworks, hazard analysis, assurance arguments, formal preservation, experimental design and transparent evaluation. Several sources already support context-specific and proportionate assessment; DDS's contribution is its particular assembly and application. The crosswalk below records our interpretation of how to use those sources, not a declaration that any source endorses DDS.

### Context, risk, quality and appraisal

[R01](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)–[R06](https://www.iso.org/standard/80655.html) provide risk/quality context; [R30](https://www.gov.uk/government/publications/the-green-book--2/the-green-book-2026) supports examining options and decisive assumptions. DDS uses these as selected references. Risk tolerances, business objectives and relevant quality criteria belong to the actual scenario/owner. ISO catalogue access confirms titles and scope only; licensed normative text and evidence are needed for a clause-level alignment claim.

### Causal and formal reasoning

[R07](https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf)–[R11](https://lamport.azurewebsites.net/pubs/simple.pdf) support control/feedback analysis, structured arguments and justified preservation. They serve different purposes. A hazard analysis can expose a causal scenario; an assurance argument links claims to grounds; a formal relation establishes only the proved direction and assumptions. None makes narrative similarity an isomorphism.

### Credible evaluation and evidence records

[R12](https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm)–[R24](https://arxiv.org/abs/1803.09010v8) offer experimental, model/agent evaluation and documentation practices. Choose those relevant to the declared question. Matching resources, avoiding shortcuts, preserving scoring/version decisions and separating instrument failure from evaluated failure make a comparison interpretable. An attractive leaderboard or comprehensive document alone does not establish a deployment result.

### Human and conventional security mechanisms

[R25](https://www.nasa.gov/human-systems-integration-division/nasa-task-load-index-tlx/)–[R29](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) ground workload observation, workload identity, attestation, stale-lock enforcement and scoped delegation. These mechanisms deserve credit in a competent baseline. Authentication, attested state, resource-generation control, human schedulability and factual truth are distinct properties; useful composition requires explicit sources and limits.

## 4. Documentary benchmark of12 adjacent approach families

Each row answers the same four questions: what approach is being considered, what primary source documents it, what it principally evaluates and how a DDS may use or complement it. This is a completed documentary comparison. It does not report a common experiment or infer that an implementation lacks capabilities not described in the selected source.

| Approach | Primary evidence | Established focus | DDS relation / comparison limit |
|---|---|---|---|
| NIST / ISO risk and quality frameworks | [R01](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf) [R05](https://www.iso.org/standard/77304.html) [R06](https://www.iso.org/standard/80655.html) | Context, risks and quality requirements | Use their vocabulary and selected requirements; DDS supplies a scoped technology–problem finding. Alignment needs its own evidence. |
| STAMP/STPA | [R07](https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf) | Hazards, unsafe actions and feedback | Generate/challenge causal scenarios. DDS adds the scoped comparison and declared outcome/cost interpretation; neither replaces industrial hazard analysis. |
| GSN / SACM | [R08](https://scsc.uk/resources/citation_r1386.html) [R09](https://www.omg.org/spec/SACM/2.3/PDF) | Claims, arguments, context and evidence | Present the reasoning/evidence chain. The argument structure does not itself execute a technology or prove the claim. |
| Formal specification / refinement | [R10](https://lamport.azurewebsites.net/tla/book-02-02-27.pdf) [R11](https://lamport.azurewebsites.net/pubs/simple.pdf) | Preservation and directed implementation | Support Stage1 proof discipline. DDS must justify its actual mapping; field-level similarity cannot inherit a theorem. |
| HELM | [R13](https://crfm.stanford.edu/2022/11/17/helm.html) | Model breadth and multiple metrics | Consume relevant model evidence. A deployment scenario still needs its own configuration, assumptions and useful outcome. |
| HAL / agent reliability | [R15](https://arxiv.org/abs/2510.11977) [R16](https://proceedings.mlr.press/v306/rabanser26a.html) | Cost-aware agents, traces and reliability | A strong execution/comparison resource. DDS must show additional decision relevance, not claim cost or reliability evaluation is new. |
| tau-bench / tau2-Bench | [R17](https://arxiv.org/html/2406.12045v1) [R18](https://proceedings.mlr.press/v306/barres26a.html) | Interactive policies and shared-state tasks | Reuse suitable task/score designs. Simulation must stay distinct from real human response capacity. |
| AgentDojo | [R19](https://arxiv.org/abs/2406.13352v3) | Injection resistance and task utility | Useful adversarial test module. Broader deployment findings need the declared non-adversarial and authority context. |
| SWE-bench Verified | [R20](https://www.swebench.com/) | Executable software-repair outcomes | Strong domain outcome testing. Transfer to other tasks requires explicit scope; its score is not an oversight finding. |
| METR time horizons | [R21](https://metr.org/time-horizons/) | Task difficulty and agent success | A reference for reliability at task duration. Human-expert task time is not an escalation response deadline. |
| Inspect AI | [R22](https://inspect.aisi.org.uk/scoring-policy.html) | Configurable execution and scoring | Can implement an admitted DDS harness. The substantive question, acceptance and claim limits remain the study's responsibility. |
| Model Cards / Datasheets | [R23](https://arxiv.org/abs/1810.03993) [R24](https://arxiv.org/abs/1803.09010v8) | Intended use and evidence documentation | Reuse source documentation. Add a scoped argument or execution only when the question requires it. |

The strongest alternatives are often complements or execution substrates. HAL and its reliability work overlap cost, traces and reliability substantially; GSN/SACM overlap traceable reasoning; STPA overlaps causal/systemic analysis. A credible DDS must explain the remaining decision-specific work rather than claim those properties as unique.

## 5. Benchmark of four documented market offerings

The following are public provider descriptions, not purchased engagements or hands-on tests. They show real overlap and strengths to credit. Price, turnaround, actual quality and independence for a particular contract remain unbenchmarked; no cheaper/faster/better claim is made.

| Offering | Primary evidence | Documented strength | DDS positioning / evidence limit |
|---|---|---|---|
| BSI AI Performance | [R31](https://www.bsigroup.com/en-US/products-and-services/standards/ai-performance/) | Independent testing; performance, fairness and reliability; assessment-linked recognition | Documented service. DDS currently cannot claim equivalent independence or recognition; its proposed fit is mechanism/decision-specific research. |
| Giskard Hub | [R32](https://docs.giskard.ai/hub/ui/evaluations) | Custom checks, local/remote/scheduled evaluations and version comparisons | Documented product workflow. Can support scoped execution; DDS's research interpretation must justify value beyond configuring tests. |
| Cisco AI Defense | [R33](https://blogs.cisco.com/ai/agent-validation-explorer-edition) | Agent tool routes, indirect channels and persistent-state security testing | Documented release capability. Credit security/harness coverage; no claim that these testing surfaces are exclusive to DDS. |
| Holistic AI audits | [R34](https://www.holisticai.com/ai-audits) | Bias/privacy/efficacy/robustness/explainability assessment and context-specific reporting | Documented service scope. DDS must be differentiated by the specific engagement and evidence, not by a generic promise of contextual audits. |

A prospective buyer can request the same bounded question, deliverable definition and evidence ceiling from different providers. A scanner or harness may solve the execution portion very well; an independent assessment may be stronger than an internally authored DDS on independence. The DDS proposition must be assessed on its actual scoped research and resulting decision utility.

## 6. The differentiation that can be defended

The existing DDS defines a technology–problem study with a declared base, explicit transfer status and mechanisms outside that base. It preserves source-native semantics while allowing simple reduced studies and richer trajectories. Its ledger separates technical Cost/Risk/Effectiveness from a deployment Business Value projection and from commercial engagement fees.

The distinctive offer is the combination in one bounded research record: suitability for the actual problem, mechanism/composition explanation, full credit for a competent conventional solution, positive and boundary evidence, burden and remaining uncertainty, and a finding useful to a real owner. That is an integration proposition, not a proof that no comparable professional service exists.

Premium quality is earned when an external reviewer can follow a material claim to the exact configuration, source/trace and acceptance rule; reproduce the disclosed result; understand what could change it; and make a better decision with the result. Strong negative findings and no-differential results can have high decision value.

Novelty and superiority are separate research questions. A claim of unique prior art would need a broader, formally delimited prior-art search. A comparative performance claim needs admitted shared conditions, a strong baseline and executed evidence. This review supplies neither a global novelty proof nor an empirical competitor ranking.

## 7. Eight clear questions for an external reviewer

These questions summarize existing DDS/SOW duties. They are a reading guide, not a new mandatory control framework or aggregate score. Use the applicable subset for a reduced study and preserve the stated exclusions.

| Topic | Reviewer question | Inspectable evidence | Existing owner |
|---|---|---|---|
| Question and decision | Which declared decision does this study inform? | A bounded question, configuration and admissibility/quality objective | DDS §§3,4,10B |
| Reference and differential | What does a competent conventional/native configuration already achieve? | A credited reference; intended differences frozen; no superiority from a weak straw baseline | DDS §15;00D/DBC when used |
| Transfer and mechanisms | What is preserved, and what lies outside that preserved part? | Stage1 relation/proof status; Stage2 mechanism/composition evidence and omissions | DDS §13.1 |
| Outcomes and falsifiers | Where does it work, fail, stop or remain unresolved? | Useful and negative/boundary traces; I/M/P/Ø semantics and acceptance matched to scope | DDS §§5,8,13 |
| Cost and value | What burden buys which outcome under these conditions? | Declared units/ledger; readiness and lifecycle costs when material; explicit E→BV assumptions | DDS §§7,9 |
| Evidence and reproducibility | How much of the conclusion was actually demonstrated? | Exact sources/configuration; trace/replay route; documentary/model/native/matched/independent labels | DDS §§6,16,17 |
| Material assumptions | Which plausible change would overturn the finding? | An in-scope boundary check or an explicitly conditional/unestablished conclusion | DDS §10B,clarification0.1.4 |
| Delivery and claim closure | What did the engagement actually deliver and authorize for use? | Included outputs closed as agreed; funding/factual review/independence and external status distinguished | DDS §10B;accepted SOW |

Evaluate each claim within its evidence class: documented design, analytical/virtual reasoning, finite instrument execution, native implementation, matched campaign or independent replication. Missing information stays unresolved; it is not evidence of absence. Do not average away a material violation or reward safe-looking shutdown as sufficient useful delivery.

## 8. Worked example: one reviewer, two obligations

Illustrative analytical example, not a new executed experiment: one qualified and authorized reviewer starts a non-preemptible critical duty at time0; it requires8 minutes and must finish by minute8. A second valid objection arrives at time0, requires6 reviewer-minutes and must be substantively resolved by minute10. Acknowledgement can be immediate, but does not substitute for the second review.

Under this single-reviewer, non-preemptive model, the work requires14 minutes inside the second10-minute window while preserving the first duty. It cannot be completed as stated. The boundary is explicit: after the first8 minutes, at most2 minutes remain for the second task. The finding changes with actual service demand, deadlines, permissible interruption or qualified backup; those assumptions need their own evidence.

Stage1 records the scenario, time units, authority, continuity objective and whether its relation to the selected base is proved, parameterized or merely analogous. Stage2 examines admission, information/whispering, pause where authorized, backup, priority, resumption and feedback; none is assumed to manufacture capacity.

The strong comparator must include competent ordinary/static practice. A qualified pre-provisioned second reviewer could finish the second task in6 minutes while the first continues. A dynamic capacity controller using only the original reviewer cannot create that second reviewer; it may establish unavailability or trigger an admitted fallback. The static route receives full credit if it achieves the same sufficient outcome at equal/lower burden.

An alert-only path is a useful diagnostic but is not automatically the strongest competing system. A real comparison must freeze task facts, source access, authority, quality, deadlines, workloads and resources, declaring exactly which mechanism/capability is varied. Readiness, preparation, coordination, action and rework are charged where in scope. HID architecture burden is a separate optional question, not a synonym for this runtime overload.

The report distinguishes successful objection delivery, timely acknowledgement, qualified availability, sufficient review and actual authorized effect. A missed response is incomplete or a prohibited material violation according to the frozen Challenge; neither classification is invented afterward. This is how a DDS turns an appealing control diagram into a useful, bounded decision.

## 9. What our current examples actually demonstrate

The public study packets below are the inspectable evidence base, pinned to their published research records. Their assertions include expected refusals and retained counterexamples; passing those instrument checks does not mean every scenario succeeds. Different case/context/operation denominators are not pooled.

| Instance | Published finite evidence | Evidence ceiling | Run / record |
|---|---|---|---|
| HEW SQLite companion | 48 functional assertions;42 scheduling checks;21 operations:11 sufficient,9 not delivered,1 retained violation | Actual local persistence/digital effects under fixture source/human/calendar conditions; no real human rates | HEW-DDS-MODEL-20261006-04 |
| STAMP/STPA exercise | 10 cases plus64 contexts;306 assertions;4 I,2 M,4 incomplete;5 unsafe-use diagnostics | Finite executed control model; not full industrial STPA assurance | STPA run02 |
| SPIFFE selected JWT profile | 25 cases;75 assertions;4 I,21 incomplete;5 unsafe-use diagnostics | Actual RSA/JWS fixtures and authored selected-profile validator; no SPIRE/Workload API realization | SPIFFE run01 |
| RATS local software/JWS profile | 20 cases;60 assertions;2 I,18 incomplete;2 stale/false-use diagnostics | Actual local hashes/signatures; synthetic source/trust contracts; no TPM/native attestation product | RATS run01 |
| 01K-A01 HC-HID component | Reusable working specification, schema and12 registered semantic controls | Runtime capacity and HID architecture remain distinct; human/engineering/HID empirical validation open | A01 verification record |

The [HEW research record](./baseline/reductions/00G-R01/feasibility/HEW_DDS_STUDY_2026-10-06.md), [separate technology exercises](./baseline/reductions/00G-R01/feasibility/independent-dds-exercises-v0.1/EXERCISES_REPORT.md) and [single HC-HID component contract](./baseline/01K_A01_HUMAN_CAPACITY_HID_COMPONENT_SPEC_v0.1.md) retain their exact sources and freezes. The published executions are model/selected-profile evidence, not actual human90/95% resolution rates, full SPIRE/TPM realization, matched vendor advantage or external independent validation.

These records show that the programme can construct bounded cases, record sources, execute selected controls, retain adverse results and provide replayable artifacts. The unresolved native/calibration/comparative obligations identify the evidence needed before stronger deployment claims.

## 10. How to benchmark a commissioned DDS without enlarging it

First distinguish three comparison objects: the study method, the studied technology/configuration and the commercial delivery. This dossier compares the first at a documentary level and surveys documented commercial offers. It does not execute the second or prove the complete third.

For an empirical technology differential, use the accepted scope and current00D/DBC comparison contracts when applicable: declare the question and comparison arms, use a strong reference, freeze common conditions and acceptance/falsifiers, execute only admitted cases, retain source/trace and unexpected findings, then report the resulting trade-off or insufficiency. A cheap, material boundary check can be enough; a larger campaign is justified only by the agreed question and evidence claim.

The [current 00D benchmark](./baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) remains the owned DDS comparator/fairness source for its scope, and [DBC](./DECISION_BOUNDARY_CHALLENGE_v0.2.md) remains a cross-stage DDS Challenge/adjudication support module. This supporting dossier creates neither a second 00D nor another DDS method/profile. New claims do not rewrite frozen UC21, R01 or existing run results.

For commercial delivery, compare the accepted outputs and their real closure evidence, not bibliography length. The existing programme's full package includes Sponsor verification/seal, executive report, technical research report, reproducible technical record, DOI research object where disclosure permits and the agreed eligible international contribution. A reduced technical study can support that package; it does not silently remove outputs. The accepted SOW governs inclusion and completion.

Sponsor recognition, DOI preservation and external contribution status are distinct from technical acceptance or accreditation. The [public HEW delivery map](./baseline/reductions/00G-R01/feasibility/dds-hew-v0.1/DELIVERY_MAP.json) records research outputs and remaining delivery objects. Current examples do not demonstrate an issued full commissioned package. A full-service reference case must close its actual dependencies before the complete offering is described as demonstrated.

## 11. Client-facing proposition and language

Suggested proposition: “A Deployment Differential Study examines a specific technology or configuration against a clearly defined operational problem. It explains what the technology genuinely contributes, which conventional capabilities already work, the conditions and costs of achieving the useful outcome, and the residual limits. The result is a traceable research finding that supports an adoption, design or further-test decision.”

A premium commissioned record makes the assumptions and mechanism story intelligible to management while preserving a reproducible technical trail for reviewers. The same scope can produce a favorable, equivalent, conditional, unfavorable or insufficient-evidence finding. It provides research depth and decision clarity within the accepted scope.

Use specific statements tied to artifacts: “demonstrated in this finite fixture”; “documented native capability”; “conditional on this source/deadline”; “no additional contribution established against this reference.” A certification, independently validated advantage, universal ROI or absence of all competing methods requires different evidence and authority. References and funding never supply those statuses.

## 12. Literature review scope, versions and reuse

The review covered34 primary references across risk/quality/assurance, formal and experimental methods, agent benchmarks, human/security mechanisms and documented service offerings. Searches used official institutions, author/publisher records and product documentation; secondary rankings and unsourced market claims were excluded from the evidentiary comparison. Relevant full-text sections were read where accessible; each entry below states its actual access level. This is a curated review of the selected DDS surfaces, not an exhaustive systematic review of all literature.

Four references rely on public catalogue/citation material: ISO31000, ISO/IEC23894, ISO/IEC25059 and GSN3. Full GSN PDF access was blocked; the official citation/abstract was available. Normative ISO clauses were not reviewed. Those entries support context/version identification only and cannot support clause-level conformity.

Version findings matter: the [HELM repository](https://github.com/stanford-crfm/helm) reports maintenance mode from June2026. The [tau2 repository](https://github.com/sierra-research/tau2-bench) records a v1.0.1 banking_knowledge grading correction, with affected earlier/later scores not comparable. HAL's reliability research illustrates why the source/version matters. Refresh and pin an actual tool/dataset version before executing a commissioned comparison. No current frontier-model leaderboard score is reused as a DDS result.

Links, citation metadata and original annotations are supplied here. External books, standards and datasets are not bundled or relicensed. A commissioned execution must check the selected tool/data license and permitted disclosure; source availability is not permission to redistribute a restricted publication.

## 13. Annotated primary bibliography

Access labels state what was checked. Publication year and review date are different; n.d. denotes an undated live page. The accompanying [BibTeX library](./DDS_REFERENCES_2026-10-06.bib) contains the same34 IDs. Each annotation states a use and a boundary, rather than implying that a citation validates DDS.

### R01. Artificial Intelligence Risk Management Framework (AI RMF 1.0)

NIST · 2023. [Primary source](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf).

Read basis: Selected full text: risk context; MEASURE2.1–2.6; MANAGE2.1.

Deployment conditions, traceable measures, residual risk and viable alternatives. Supports contextual evaluation; does not prescribe DDS or validate its results.

### R02. Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile

NIST · 2024. [Primary source](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf).

Read basis: Selected full text: MS-2.5-001/002 and human-AI configuration.

Use generalizability limits and document human contribution. Narrow demonstrations cannot establish broad capability. A risk profile is not a comparative test result.

### R03. Introduction to AI assurance

UK Department for Science, Innovation and Technology · 2024. [Primary source](https://www.gov.uk/government/publications/introduction-to-ai-assurance/introduction-to-ai-assurance).

Read basis: Selected official full text: toolkit, proportionality, certification example.

Distinguishes assurance techniques and supports proportionate selection. DDS can produce evidence for a wider assurance process; citing this guidance does not make DDS an accredited certification scheme.

### R04. ISO 31000:2018 — Risk management — Guidelines

ISO · 2018. [Primary source](https://www.iso.org/standard/31000).

Read basis: Official catalogue/abstract; normative text not reviewed.

Provides a general risk-management reference beyond AI. Use as contextual terminology, not a claim of clause-level conformity.

### R05. ISO/IEC 23894:2023 — Artificial intelligence — Guidance on risk management

ISO and IEC · 2023. [Primary source](https://www.iso.org/standard/77304.html).

Read basis: Official abstract; normative text not reviewed.

Connects AI risk management to organizational activities. An alignment map needs licensed/full clauses and specific evidence before any conformity claim.

### R06. ISO/IEC 25059:2023 — Quality model for AI systems

ISO and IEC · 2023. [Primary source](https://www.iso.org/standard/80655.html).

Read basis: Official abstract/status; normative text not reviewed.

Useful quality vocabulary and completeness questions. Catalogue flags a forthcoming replacement; the cited2023 edition must be pinned and refreshed for commissioned use.

### R07. STPA Handbook

Leveson, Nancy G. and Thomas, John P. · 2018. [Primary source](https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf).

Read basis: Selected full text: purpose/losses, control structure, unsafe actions, causal scenarios.

Established system/human hazard analysis and feedback discipline. Use it to generate or challenge scenarios; an authored finite STPA exercise is not full industrial STPA validation.

### R08. Goal Structuring Notation Community Standard (Version3)

SCSC Assurance Case Working Group · 2021. [Primary source](https://scsc.uk/resources/citation_r1386.html).

Read basis: Official citation/abstract; PDF access blocked in this review.

Supports explicit engineering argument structure. Metadata confirms scope/version only; no clause-level or notation-conformance claim is made from the inaccessible body.

### R09. Structured Assurance Case Metamodel (SACM), version2.3

Object Management Group · 2023. [Primary source](https://www.omg.org/spec/SACM/2.3/PDF).

Read basis: Selected full text: scope/context, argumentation and artifact provenance.

Connect claims, arguments, assumptions and evidence. Provides an established assurance-case substrate; DDS does not automatically conform to the metamodel.

### R10. Specifying Systems: The TLA+ Language and Tools for Hardware and Software Engineers

Lamport, Leslie · 2002. [Primary source](https://lamport.azurewebsites.net/tla/book-02-02-27.pdf).

Read basis: Author preliminary draft; selected sections8.9.4 and composition.

Formal preservation/implementation reasoning supports carefully directed transfers. A source analogy or passed fixture cannot replace the applicable proof obligations.

### R11. Prophecy Made Simple

Lamport, Leslie and Merz, Stephan · 2020. [Primary source](https://lamport.azurewebsites.net/pubs/simple.pdf).

Read basis: Selected full text: section3 implementation/refinement mappings.

A concrete refinement mapping establishes a directed implementation relation. Use to distinguish implication from full isomorphism; DDS/R01 proofs remain separately owned.

### R12. e-Handbook of Statistical Methods — Choosing an experimental design; randomized block designs

NIST and SEMATECH · n.d.. [Primary source](https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm).

Read basis: Official sections5.3 and5.3.3.2.

Blocking and randomization help control nuisance variation in executed comparisons. Apply only when the scoped empirical design warrants it; no universal factorial grid is required.

### R13. Holistic Evaluation of Language Models (HELM)

Liang, Percy and others · 2023. [Primary source](https://crfm.stanford.edu/2022/11/17/helm.html).

Read basis: Author methodology;2023 TMLR citation checked in official repository.

Coverage, incompleteness and multiple metrics are established evaluation principles. Software entered maintenance mode in2026; framework merit and current maintenance are distinct.

### R14. AI Agents That Matter

Kapoor, Sayash and Stroebl, Benedikt and Siegel, Zachary S. and Nadgir, Nitya and Narayanan, Arvind · 2024. [Primary source](https://arxiv.org/html/2407.01502v1).

Read basis: Selected full text: cost, downstream needs, shortcuts, reproducibility.

Control cost and task definition; avoid benchmark shortcuts and weak holdouts. Supports simpler strong baselines and honest deployment transfer.

### R15. Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation

Kapoor, Sayash and others · 2026. [Primary source](https://arxiv.org/abs/2510.11977).

Read basis: Author abstract; official HAL description and ICLR2026 citation.

Existing standardized agent harness, cost-aware comparison and trace inspection deserve full credit. A common harness still needs a deployment-specific question and valid scoring.

### R16. Towards a Science of AI Agent Reliability

Rabanser, Stephan and Kapoor, Sayash and Kirgis, Peter and Liu, Kangheng and Utpala, Saiteja and Narayanan, Arvind · 2026. [Primary source](https://proceedings.mlr.press/v306/rabanser26a.html).

Read basis: ICML2026 publisher abstract; official reliability documentation.

Separates consistency, robustness, predictability and safety. DDS should consume applicable reliability evidence rather than claim these dimensions are new.

### R17. tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

Yao, Shunyu and others · 2025. [Primary source](https://arxiv.org/html/2406.12045v1).

Read basis: Selected full text; ICLR2025 publication;2024 preprint.

State-based scoring, domain policies and repeated-run pass^k. A simulated user is not human-capacity calibration; pass^k and pass@k answer different questions.

### R18. tau2-Bench: Evaluating Conversational Agents in a Dual-Control Environment

Barres, Victor and Dong, Honghua and Ray, Soham and Si, Xujie and Narasimhan, Karthik R. · 2026. [Primary source](https://proceedings.mlr.press/v306/barres26a.html).

Read basis: ICML2026 publisher abstract; current official repository notes.

Shared agent/user actuation and ablation are existing benchmark capabilities. User simulation does not establish actual human readiness, authority or workload.

### R19. AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents

Debenedetti, Edoardo and others · 2024. [Primary source](https://arxiv.org/abs/2406.13352v3).

Read basis: Author abstract and release-change note.

Tool tasks over untrusted data evaluate task utility alongside injection resistance. Relevant to security controls; broader non-adversarial deployment adequacy requires its own scope.

### R20. SWE-bench Verified

SWE-bench team · 2024. [Primary source](https://www.swebench.com/).

Read basis: Official project/dataset description:500 human-filtered instances.

Executable software-repair tasks supply meaningful outcome verification. A coding benchmark result is not general evidence of oversight or business value.

### R21. Task-Completion Time Horizons of Frontier AI Models

METR · n.d.. [Primary source](https://metr.org/time-horizons/).

Read basis: Official methodology/FAQ; Time Horizon1.1 selected.

Human-expert task duration indexes difficulty at a stated success level. It is not the agent's wall-clock duration or the human escalation response window.

### R22. Inspect AI — evaluation framework and scoring policy

UK AI Security Institute · n.d.. [Primary source](https://inspect.aisi.org.uk/scoring-policy.html).

Read basis: Official framework/scoring/sandbox documentation.

Custom tasks, logs and scoring distinguish evaluated failure from instrument failure and unscored samples. Good execution infrastructure; a harness does not decide the substantive research question.

### R23. Model Cards for Model Reporting

Mitchell, Margaret and others · 2019. [Primary source](https://arxiv.org/abs/1810.03993).

Read basis: Author abstract and FAT*2019 venue metadata.

Documents intended use, evaluation and limitations. Reuse available cards as sources; documentation does not itself demonstrate deployment fitness.

### R24. Datasheets for Datasets

Gebru, Timnit and others · 2021. [Primary source](https://arxiv.org/abs/1803.09010v8).

Read basis: Author abstract; CACM2021 publication metadata.

Data motivation, collection, composition and intended use help qualify fixture/source evidence. A datasheet is not a proof that a dataset represents a deployment.

### R25. NASA Task Load Index (TLX)

NASA · n.d.. [Primary source](https://www.nasa.gov/human-systems-integration-division/nasa-task-load-index-tlx/).

Read basis: Official instrument description.

Subjective multidimensional workload measurement can inform a human study. It does not establish competence, authorization, decision accuracy or empirical HID.

### R26. SPIFFE Overview

SPIFFE project · n.d.. [Primary source](https://spiffe.io/docs/latest/spiffe-about/overview/).

Read basis: Official specification overview.

Workload identities and authentication are conventional capabilities. Identity validity alone does not establish claim truth, current authority or timely human intervention.

### R27. RFC9334 — Remote ATtestation procedureS (RATS) Architecture

Birkholz, H. and Thaler, D. and Richardson, M. and Smith, N. and Pan, W. · 2023. [Primary source](https://www.rfc-editor.org/rfc/rfc9334.html).

Read basis: Selected full text: roles, appraisal policies, freshness; Informational RFC.

Attester/verifier/relying-party separation and freshness qualify state evidence. A local JWS fixture is not native device attestation or full RATS conformance.

### R28. The Chubby lock service for loosely-coupled distributed systems

Burrows, Mike · 2006. [Primary source](https://www.usenix.org/legacy/events/osdi06/tech/full_papers/burrows/burrows.pdf).

Read basis: OSDI2006 full text: section2.4 sequencers.

Resource-side sequencer checks reject stale lock use. A strong conventional baseline should receive credit; a generation token without enforcement is insufficient.

### R29. The confused deputy problem — IAM User Guide

Amazon Web Services · n.d.. [Primary source](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html).

Read basis: Official cross-account/cross-service documentation.

Established scoped-delegation safeguards include trust-policy external IDs. Evaluate the actual configured native policy; identity-only failure does not show a competent IAM baseline fails.

### R30. The Green Book: UK government guidance on appraisal

HM Treasury · 2026. [Primary source](https://www.gov.uk/government/publications/the-green-book--2/the-green-book-2026).

Read basis: Selected official full text: objectives/options, uncertainty and switching values.

Comparing options and material assumptions helps qualify value claims. Transfer the appraisal principle proportionately; DDS is not a complete public-sector appraisal or universal ROI calculation.

### R31. AI Performance Assessment — Independent AI verification

BSI · n.d.. [Primary source](https://www.bsigroup.com/en-US/products-and-services/standards/ai-performance/).

Read basis: Official service description; provider claims, no purchased assessment.

Documented independent performance/fairness/reliability assessment and recognition. Credit this established assurance offering; its mark and DDS Sponsor recognition have different meanings.

### R32. AI Agent Evaluation — Giskard Hub

Giskard · n.d.. [Primary source](https://docs.giskard.ai/hub/ui/evaluations).

Read basis: Official product/workflow docs; no hands-on product benchmark.

Custom checks, local/remote/scheduled evaluation and version comparison overlap DDS execution needs. Continuous testing is a documented product strength.

### R33. Introducing Agent Harness Testing in Cisco AI Defense

Cisco · 2026. [Primary source](https://blogs.cisco.com/ai/agent-validation-explorer-edition).

Read basis: Official release description; no hands-on product benchmark.

Tool routes, indirect content and persistent agent state are documented testing surfaces. DDS cannot claim agent-harness evaluation is an unoccupied market.

### R34. AI Audits — Mitigate and Monitor AI Risks

Holistic AI · n.d.. [Primary source](https://www.holisticai.com/ai-audits).

Read basis: Official service description; no purchased audit.

Sociotechnical risk assessments, context-specific reporting and mitigations are established service offerings. Scope and independence need engagement-specific evidence.

## 14. Public source and continuation map

Method authority: [DDS Canonical Method Index](./DDS_CANONICAL_METHOD_INDEX_v0.1.md), with [Stage A](./DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md), [Stage B](./DDS_GATE_B_ARCHITECTURE_VERIFICATION_v0.1.md) and [Stage C](./DDS_GATE_C_IMPLEMENTATION_PROBLEM_VALIDATION_v0.1.md) owning their respective technical contracts. This dossier is a supporting sourcebook with a [single owning review](./DDS_RESEARCH_BASIS_AND_BENCHMARKING_2026-10-06_VNext.md); it creates no new method. R01 retains its [technology-extension protocol](./baseline/reductions/00G-R01/feasibility/TECHNOLOGY_EXTENSION_PROTOCOL.md) and mathematical contracts. The selected research execution records are associated with public releasee08e4f12ffd3f1dff64bc08df6af62c943992831; later source/route edits do not add empirical evidence.

The practical next validation, when commissioned and admitted, is one end-to-end reference case under a concrete provider/deployment scope, with an appropriately strong alternative, source-owner factual review and the exact included deliveries. Its prospective criteria belong to the existing instruments. This bibliography does not launch that case or expand every study into a full campaign.
