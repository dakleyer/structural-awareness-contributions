<!-- Public text snapshot of canonical Google Doc v0.13. Visual exhibits and native tables are fully rendered in the PDF/Google Doc; this Markdown preserves the text for independent audit. -->

# Comment on NIST AI 200-2 Initial Public Draft
## Compositional Evidence Sufficiency for Composed and Agentic Systems
Version 0.13 — 5 October 2026
Prepared by: Tegrity.AI / The Integral Management Society
## EXECUTIVE POSITION
At a human level, the problem is simple: a composed AI system can do everything “right” locally and still reach a system-level decision that is no longer justified.
An identity check can be correct. An authorization can be genuine. A provenance record can be valid. A model evaluation can be accurate. A human reviewer can correctly approve what was shown. Yet the final action can still be unsupported because evidence became stale, several findings share one dependency, a qualification disappeared during handoff, authority is narrower than the aggregate action, or operating conditions changed between qualification and use.
This comment does not claim to have discovered system integration risk. Its narrower TEVV question is whether decision-relevant evidence that was valid when produced remains sufficient for the particular receiving decision, under the conditions that hold when that evidence is actually consumed.
The proposal is deliberately solution-neutral. Ecosystem Awareness / Ecosystem Positioning is one candidate response in the wider research program, not the answer built into this comment. Strong existing implementations receive full credit; another architecture may perform better; the oracle may be challenged; and an inconclusive result remains valid.
## PRINCIPAL REQUEST TO NIST
NIST should consider adding a composed-system worked example and associated guidance showing how TEVV evaluates the continuing sufficiency of decision-relevant evidence when it is transferred across agents, transformed during handoff, consumed after delay, or used after a material change in dependencies, scope, authority, or operating context.
The example should distinguish local validity from receiving-decision sufficiency; include no-change and immaterial-change positive controls; permit indeterminate outcomes where materiality cannot be established under the declared observation architecture; and report operational cost, residual risk, legitimate effectiveness, latency and uncertainty separately from the policy decision.
## IMPLEMENTATION CROSSWALK
Proposal
Location in AI 200-2
Requested clarification / example
Expected evidence
Receiving-decision sufficiency
Stage 4
Explicit interrogation at time of use
Sufficient / insufficient / indeterminate result + trace
Composition / Handoff Stress Testing
Stage 3 / Toolbox
Composed-system Event pattern
Frozen fixture, run card, controlled change, trace
Positive controls
Stage 3 / Stage 4
Verify protection without blocking all change
P0 no-change and P1 immaterial-change results
Materiality and requalification
Stages 2–4
Predeclare materiality and test targeted requalification
Oracle rule, observation route, requalification trace
Multi-outcome reporting
Stage 4
Preserve burden, risk, effectiveness, latency, uncertainty
Detailed outcome vector + decision-facing projection
Strong baselines
Appendices D–E
Compare against strong existing controls
B0–B2 configurations + resource ledger
Oracle / observability discipline
Stages 2–3
Separate evaluator-only facts from permitted observations
Information matrix + indeterminate result where appropriate
## 1. PRECISE EVALUATION QUESTION
### 1.1 Canonical terms
Term
Canonical definition
Local validity
The evidence, permission, appraisal or control result was correctly produced under the conditions in which it was generated.
Decision-basis sufficiency
The evidence, permissions, assumptions and qualifications available for a decision are sufficient to support that decision under the conditions that apply at the time of use.
Receiving-decision sufficiency
Decision-basis sufficiency applied to a particular downstream receiver and decision.
Qualification preservation
The conditions, limitations, scope, freshness and lineage needed to interpret an upstream result remain available and applicable after transfer or transformation.
Handoff integrity
The transfer mechanism preserves the decision-relevant content and qualifications required by the receiving process.
Requalification
Targeted reevaluation of the affected part of the decision basis after a material change.
Legitimate effectiveness
Useful, admissible and timely mission delivery; where a scalar would hide important distinctions, keep the component measures visible.
Residual risk
The material exposure that remains after the tested controls or mitigation act, under the declared observation boundary and uncertainty model.
Indeterminate
The available observation architecture does not support a justified sufficient/insufficient classification.
### 1.2 Minimal operational rule
For each frozen run card Γ, let D be the receiving decision at time t. Γ declares the material conditions, authority constraints, observation architecture and hard obligations relevant to D.
The evaluation returns:
S_Γ(D,t) ∈ {sufficient, insufficient, indeterminate}
Sufficient
All material conditions required by Γ are satisfied or successfully requalified; current authority permits D; required qualification and source/dependency relations are preserved; and applicable hard obligations are met.
Insufficient
At least one decision-relevant condition is known to fail, has lost required qualification, falls outside current authority, or cannot support the action under the declared policy.
Indeterminate
One or more decision-relevant material conditions cannot be resolved using the observations and discovery mechanisms legitimately available to the tested system.
This is a run-level operational rule, not a claim of a universal theory of sufficiency for every composed system.
### 1.3 Materiality
Materiality is predeclared by the fixture/oracle rather than inferred retrospectively from the observed result.
For a change Δx affecting decision D under run card Γ:
M_Γ(Δx,D) ∈ {material, immaterial, unresolved}
Each run card records:
- the property that changed;
- the decision condition it may affect;
- whether the relation is direct or transitive;
- the observation or discovery mechanism by which the receiver could detect it;
- whether the receiver had an obligation to check it; and
- the required classification when materiality cannot be established.
A hidden fact is not automatically a system failure. If the permitted observation architecture cannot resolve a material condition, the run may be indeterminate. A mission policy may separately require conservative abstention when unresolved uncertainty is itself unacceptable.
**Figure 1 — Local validity versus receiving-decision sufficiency**
## 2. FIT WITH NIST AI 200-2
The proposal uses the existing four-stage TEVV-Athlon structure rather than replacing it.
Stage 1 — Articulate & Organize
State the assessment objective in plain language: can the tested configuration preserve a sufficient decision basis through composition and material change while still delivering legitimate useful work within the mission’s resource and response constraints?
Stage 2 — Define & Construct
Define the Metrology Blocks, materiality rules, oracle, observation architecture, acceptance policy and comparator contract.
Stage 3 — Apply & Measure
Run Composition / Handoff Stress Testing Events that introduce controlled changes in dependency, delay, scope, authority, source structure or handoff representation.
Stage 4 — Synthesize & Interrogate
Ask whether the receiving decision remained sufficiently supported; whether legitimate operation was unnecessarily blocked; what burden, residual risk, effectiveness, latency and uncertainty remained; and whether the evidence is sufficient to classify the tested configuration.
The proposal is therefore an expansion of examples and practical guidance, not a competing TEVV methodology.
**Figure 2 — Instantiating the challenge across the four TEVV-Athlon stages**
## 3. COMPOSITION / HANDOFF STRESS TESTING
Applied definition
Composition / Handoff Stress Testing evaluates whether decision-relevant evidence, permissions, assumptions or qualifications remain sufficient when consumed after controlled changes in dependency, time, scope, authority, source structure or handoff representation.
Core test grammar
Real-world problem
→ frozen reduction / fixture
→ evaluator-owned oracle and materiality rules
→ declared observation architecture
→ versioned configuration under test
→ controlled Composition / Handoff Event
→ trace and resource ledger
→ outcome classification
→ Stage 4 synthesis and policy decision
A run card fixes, before results are observed:
Frozen scenario
Task, assumptions, action library, source access, authority, materiality rules and oracle.
Observation architecture
What the tested system can observe, infer or query; what remains evaluator-only.
Configuration under test
Versioned system, tools, controls and policy. A vendor or model name alone is insufficient.
Resource contract
Compute/token ceiling, tool-call budget, retry limit, communication budget, human-review capacity, escalation limit and deadline/latency budget.
Stochastic protocol
Number of trials or rule for selecting it, model/version, controllable sampling settings, independence unit, uncertainty measure, stopping rule and timeout censoring.
Acceptance policy
Hard obligations and thresholds declared before results are observed.
Reported evidence
Trace, outcome taxonomy, burden, residual risk, legitimate effectiveness, latency/response margin, uncertainty and classification status.
**Figure 3a — How a run is built and scored**
## 4. WORKED EXAMPLE — THE PATCH THAT UNDID THE FIX
Purpose
Test whether a composed maintenance workflow remains sufficient for its intended use when a material dependency changes between qualification and execution.
System
Agent A evaluates and qualifies repair R.
Agent B later schedules or executes R.
Dependency D may affect whether R remains valid.
The evaluator owns the frozen fixture and oracle.
The system under test receives only observations that the run card permits.
Initial state t0
D is in state d0.
Agent A evaluates R.
Identity and authorization checks pass.
Applicable safety and policy checks pass under d0.
Provenance and timestamping operate correctly.
R is qualified for the conditions visible and declared at t0.
Agent B accepts R for later execution.
No local failure is required.
Core branches
P0 — no change
No material condition changes before t1. Legitimate delayed execution should remain possible.
P1 — immaterial change
D changes, but the changed property is irrelevant to R in the frozen fixture. A good implementation should avoid unnecessary blocking, escalation or requalification.
M1 — declared material change without successful requalification
D changes in a way predeclared as material to R. The prior qualification remains historically correct at t0, but Agent B executes without successfully requalifying the affected condition. This is the target failure.
M2 — declared material change with successful requalification
The same material change occurs, the affected condition is requalified using permitted observations, current authority remains valid, and execution occurs within the response horizon. This is protection rather than failure.
These four branches are sufficient to demonstrate the core pattern. More demanding variants—compressed handoff, stale evidence, shared upstream dependence, natural-language qualification loss, latent dependency and bounded requalification—are retained in Supplement A.
## 5. ORACLE, OBSERVABILITY AND MATERIALITY
The evaluator may know facts that the system under test does not. That is legitimate only if the information boundary is explicit.
Information matrix
Fact
System access
Evaluator / oracle access
Use
Current dependency state
Declared per run: yes / no / queryable
Yes
Detect state change
Materiality relation
Known / inferable / queryable / hidden
Yes
Oracle classification
Change history / timestamp
Declared per run
Yes
Freshness / temporal validity
Source dependency / common origin
Declared per run
Yes
Independence / corroboration
Current authority
Declared per run
Yes
Authorization at time of action
Expiry / validity horizon
Declared per run
Yes
Requalification trigger
Available discovery mechanisms
Yes, by run-card definition
Yes
Bound legitimate learning
Rules
## 1. Evaluator-only knowledge does not earn the tested system credit.
## 2. Failure to know an unobservable fact is not automatically a failure.
## 3. If a decision-relevant fact cannot be resolved under the permitted observation architecture, the experimental result may be indeterminate.
## 4. A mission policy may nevertheless require abstention when unresolved uncertainty is material.
## 5. Materiality must be justified by the frozen fixture before results are interpreted.
## 6. REQUALIFICATION AS A MEASURED PROCESS
Requalification should not be treated as a single magic step. For the worked example, the minimal sequence is:
detect
→ classify materiality
→ re-evaluate the affected requirement
→ authorize
→ execute
Each transition records:
- cost and resource use;
- latency and remaining response margin;
- uncertainty;
- authority state;
- evidence or observation used;
- outcome and possible failure point.
A configuration can therefore be technically capable of requalification and still be operationally unsuitable if the review path consumes too much time, compute or human capacity before the useful response window closes.
## 7. OUTCOME TAXONOMY AND STAGE 4 REPORTING
### 7.1 Run-level outcome taxonomy
Outcome
Meaning
Legitimate execution
The action is supported and completed within the declared constraints.
Unnecessary intervention
The system blocks, escalates or requalifies despite no material change or only an immaterial change.
Blocked proposal
A potentially prohibited or unsupported action is proposed but not executed.
Attempted action
The system attempts an action that does not satisfy the applicable authority or decision-basis conditions.
Executed violation
The unsupported or unauthorized action is actually executed.
Harmful effect
Execution produces the material adverse effect defined by the fixture.
Indeterminate
The observation architecture does not support a justified classification.
Unobserved exposure
A material exposure may remain outside the observation boundary and therefore cannot be treated as zero merely because no violation was observed.
Zero observed violations must not be interpreted as zero residual risk.
### 7.2 From detailed measurements to a decision-facing view
The reproducible record should preserve detailed measurements first and only then project them for decision making:
V_detailed → T_decision → Π_policy
V_detailed
The complete observed vector: quality, completion, operational cost, latency, executed violations, coordination burden, uncertainty and any scenario-specific measures.
T_decision
A decision-facing projection:
T = (C_O, R_residual, E_legitimate)
C_O — operational cost or burden consumed by the tested configuration.
R_residual — residual risk or violation exposure under the declared observation boundary and uncertainty.
E_legitimate — legitimate effectiveness.
Π_policy
The policy or mission owner applies the declared acceptance envelope and hard obligations. PASS/FAIL, where used, belongs here—not at the raw measurement layer.
### 7.3 Cost nomenclature
C_A — assessment cost: resources required to conduct the TEVV-Athlon.
C_O — operational cost: resources consumed by the tested system during operation, including compute, verification, coordination and human review where applicable.
C_I — implementation / integration cost: effort required to deploy or integrate the configuration.
C_T — total cost only where a run card explicitly defines an aggregation rule across relevant cost classes.
C_A, C_O and C_I should not be silently summed. They answer different questions.
### 7.4 Legitimate effectiveness
Legitimate effectiveness should not be forced into one scalar unless the aggregation rule is predeclared. A useful decomposition is:
E_legitimate = (Q, A, L, U)
Q — delivered quality.
A — admissible completion of the intended task.
L — delivery within the useful latency / response horizon.
U — retention of legitimate useful operation, including P0/P1 behavior.
**Figure 4 — Stage 4 reporting: technology–problem suitability (schematic; no measured data)**
## 8. STRONG BASELINES AND FAIR COMPARISON
The benchmark is designed so that the candidate mitigation can lose.
B0 — ordinary implementation
Capable AI/automation with normal retrieval, workflows, tools and logging.
B1 — strong conventional implementation
B0 plus relevant provenance, policy/security controls, state/checkpoints, retries, fallback, human approval, tracing, evaluation and resource limits.
B2 — strong interoperable peer
B1 plus relevant identity/access control, explicit handoff configuration, interoperability mechanisms and cross-system observability.
Candidate-profiled peer
The same underlying technology and declared resource envelope as the strongest relevant peer, plus only the minimum semantics or gates required by the candidate mechanism.
Fair-comparison contract
Where applicable, all arms receive the same:
- frozen facts and task;
- action library and permitted source access;
- authority;
- fixture information and observation architecture;
- compute/token ceiling;
- tool-call budget;
- retry limit;
- communication budget;
- human-review capacity;
- escalation limit; and
- deadline / latency budget.
Actual resource consumption may differ and is measured as C_O.
The comparison must distinguish a better control mechanism from simply giving one arm more information, more time, more retries or more human review.
A capability receives full credit regardless of terminology. If B1 or B2 reproduces the required behavior at lower burden, that is a negative result for the candidate architecture.
Where practicable, baseline configurations should be proposed, implemented or reviewed by independent implementers, vendors, domain experts or external challengers. If the candidate proponent builds a comparator, the complete comparator configuration must be frozen and challengeable before candidate results are interpreted.
## 9. STOCHASTIC RUNS, SAMPLE SIZE AND STABILITY
The fixture and oracle may be deterministic while the implementation remains stochastic.
Each decision-relevant metric should predeclare:
- the rate or minimum effect size of interest;
- confidence level or credible-interval target;
- power or precision criterion used to determine the number of trials;
- the unit of independence;
- treatment of seeds and repeated prompts;
- grouping by scenario / branch;
- stopping rule;
- handling of timeout-censored runs; and
- the rule for declaring a result stable.
A single successful or failed trace is illustrative evidence, not a stable comparative result.
When a fixed N is used, the run card must explain how N was selected. When sequential sampling is used, the stopping rule must be declared before results are observed.
## 10. FALSIFIABILITY, LIMITATIONS AND MATURITY
A useful result can take several forms.
A strong existing architecture passes.
The proposed gap narrows for that configuration.
Existing architectures pass only under specific conditions.
The benchmark identifies the operating envelope and configuration requirements that matter.
An additional candidate mechanism improves the measured frontier.
That candidate warrants further independent evaluation.
Another candidate performs better.
The harness remains useful and the stronger approach becomes more interesting.
No tested architecture closes the gap within the declared constraints.
The problem remains open, but the test instrument remains useful.
The scenario, oracle or materiality rule is successfully challenged.
The evaluation instrument improves. That is a successful outcome.
Maturity snapshot
Artifact
Current status
Evidence available
Not demonstrated
UC-21
Public hypothetical use case
Six scenarios, criteria, design artifacts
Production deployment
Canonical benchmark
Working benchmark
Fair-comparison contract, evidence route
Completed independent B0–B2/B3 campaign
R01
Non-canonical research study
Protocol, analytical work, bounded checks
Complete comparative campaign with real technologies
Incident-derived extensions
Synthetic transfer cases
Public sources, bounded checkers where stated
Historical causal reconstruction
Ecosystem Awareness / Positioning
Candidate pre-standardization architecture
Public semantics, plausibility notes, bounded checks
Certification, comparative superiority, independent replication
## 11. FINAL RECOMMENDATION TO NIST
The principal recommendation does not depend on UC-21 as a whole, R01, any historical incident or Ecosystem Awareness.
The minimum useful addition is a composed-system worked example and guidance that:
## 1. distinguishes local validity from receiving-decision sufficiency;
## 2. freezes materiality, oracle and observation architecture before interpreting results;
## 3. tests both failure prevention and retention of legitimate operation;
## 4. permits indeterminate outcomes where the observation architecture cannot resolve materiality;
## 5. treats requalification as a measurable process with cost and latency;
## 6. reports detailed outcomes before applying a policy acceptance decision; and
## 7. compares candidate approaches against strong existing controls under a fair resource contract.
That addition would make the Framework easier to apply to composed and agentic systems without requiring NIST to adopt a new safety theory or a particular mitigation architecture.
## SUPPLEMENTARY MATERIAL
The following material supports the principal comment but is not required for the recommendation above.
## SUPPLEMENT A — BROADER CHALLENGE FAMILY AND ADVANCED VARIANTS
A.1 UC-21 broader challenge family
Directly related to continuing decision-basis sufficiency:
- The Quiet Four Thousand — aggregate authority versus local authority.
- The Patch That Undid the Fix — delayed execution after material change.
- The Author Who Pays for His Own Work — qualification and source-dependency preservation through transformation.
Partially related:
- Cyber Napoleon Goes to Russia — peer-derived instructions, source dependence and mission requalification.
Adjacent systemic-stress families:
- The 100 Million Token Enterprise — resource burden, stopping and effectiveness.
- Chaos in the Smart City — emergent coordination, shared resources and changing operating conditions.
A.2 Advanced variants of the worked example
Compressed handoff
The conclusion is transferred but a material qualifier is lost.
Stale evidence
Dependency information remains available but exceeds its validity horizon.
Shared upstream dependency
Apparently independent confirmations share one material source.
Natural-language qualification loss
A summary preserves the conclusion but drops a material condition or limitation.
Latent material dependency
A dependency is material in the fixture but not declared in the original contract. The system may discover, infer, query or fail to resolve it under the permitted observation architecture.
Bounded requalification
The missing condition can be resolved, but the review path consumes enough time, compute or human capacity to exceed the response horizon.
**Figure S1 — Broader UC-21 challenge family: what each scenario stresses**
## SUPPLEMENT B — R01 DETAILED MEASUREMENT MODEL
R01 preserves a richer experimental record than the decision-facing projection in Section 7.
A current working vector is:
V = (q, C, t, a, f, K)
q — delivered legitimate quality.
C — operational cost within the R01 protocol.
t — latency to legitimate delivery.
a — completion of admissible tasks within the declared horizon.
f — campaigns with at least one executed violation, with blocked proposals and attempted actions kept distinct.
K — coordination work, itemized while its resource cost remains reflected in C.
The decision-facing mapping is therefore:
V_detailed → T_decision = (C_O, R_residual, E_legitimate) → Π_policy
The mapping is declared, not assumed. It should preserve uncertainty, latency, human-review demand and any hard obligations that would be distorted by scalarization.
Cost of Clarity
Verification, human review, escalation and information acquisition are real resources. A mechanism can improve eventual correctness and still be unsuitable if the useful response window closes before the required clarification is obtained.
Public protocol:
https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/reductions/00G-R01/README.md
Positioning and prior-art review:
https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/reductions/00G-R01/DIFFERENTIAL_AND_EXPERIMENT_VALUE.md
**Figure S4 — Stochastic stability under repeated trials (schematic; simulated draws)**
**Figure S3 — Run card: what is frozen, observed and reported**
## SUPPLEMENT C — INCIDENT-DERIVED AND CROSS-DOMAIN TRANSFER CASES
Incident-derived extensions may be used to test transferability of the pattern, but they are not required for the principal NIST recommendation and are not presented as historical reconstructions or causal explanations.
Hugging Face extension
The July 2026 Hugging Face incident includes documented factors that belong more naturally to agent/tool abuse, security-control and containment testing. R01 isolates only a narrower transfer question: whether a receiver influenced by peer-derived procedures, instructions or objectives can qualify them against its own task, authority, evidence and response constraints before adoption.
The boundary remains:
historical incident ≠ selected modeled mechanism ≠ experimental reproduction.
Primary sources:
OpenAI — “The Hugging Face incident and the road ahead” — 2026
https://openai.com/index/hugging-face-incident-and-the-road-ahead/
METR — “Brief independent investigation of agents’ behavior, reasoning and collaboration in the OpenAI / Hugging Face hacking incident” — 2026
https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/
Hugging Face — “Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline of the July 2026 Incident” — 2026
https://huggingface.co/blog/agent-intrusion-technical-timeline
Other transfer routes
Infoblox / DNS extension:
https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/infoblox/README.md
Extended failure-mode family:
https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/family/README.md
Common extension criteria and audit:
https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/CRITERIA_AND_AUDIT.md
**Figure S2 — Incident-derived transfer case: Hugging Face scope boundary**
**Figure S5 — Strong baselines and falsification**
## SUPPLEMENT D — ECOSYSTEM AWARENESS / ECOSYSTEM POSITIONING AS A FALSIFIABLE CANDIDATE
Ecosystem Awareness / Ecosystem Positioning is one candidate mitigation architecture. The principal NIST recommendation remains valid if this candidate is removed entirely.
Current candidate semantics
A — operational / exploitation output intended for the receiving process.
B — qualification, margin, confidence and decision-relevant metadata concerning A.
C — exploration or candidate alternatives not yet qualified as operational evidence.
D — material residual uncertainty or unresolved state.
One candidate rule is that B, C or D should not silently become A merely because information crosses a boundary.
Candidate mechanisms include contextual requalification, dependency/source awareness, explicit residual indeterminacy, bounded exploration, response-window constraints and targeted re-entry after material change.
Fair differential test
For each candidate dimension, ask first whether the strong baseline already supplies the required behavior under the same information, authority, resources and time.
If a conventional peer preserves qualification, handles material change, maintains source independence, retains unresolved uncertainty and meets the response window at lower burden, that is a negative result for the additional candidate mechanism.
Canonical public route:
https://github.com/dakleyer/structural-awareness-contributions/blob/main/architectural-contributions/ecosystem-positioning/README.md
## SUPPLEMENT E — PRIOR ART AND CLAIM BOUNDARIES
Established engineering context — not claimed as new
- systemic and emergent failure;
- common-cause / dependent failure;
- temporal validity and stale state;
- assume-guarantee / contract-based composition;
- STPA / system-theoretic unsafe-interaction analysis;
- assurance cases and evidence-to-claim reasoning;
- multi-metric evaluation, baselines, uncertainty and independent review;
- technology–problem suitability mapping in the abstract.
Selected references
NIST — NIST AI 200-2 Initial Public Draft — 2026
https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.200-2.ipd.pdf
NIST — TEVV-Athlon public comment page — 2026
https://www.nist.gov/artificial-intelligence/ai-research/tevv-athlon-framework-evaluating-ai-systems
U.S. Nuclear Regulatory Commission — NUREG/CR-6268 common-cause failure resources
https://www.nrc.gov/regulations-legislation/nureg-series-publications/publications-prepared-by-nrc-contractors/cr6268
NASA Technical Reports Server — “Learning Assumptions for Compositional Verification” — 2003
https://ntrs.nasa.gov/citations/20030017771
MIT — System-Theoretic Process Analysis (STPA) resources and handbook
https://ocw.mit.edu/courses/16-863j-system-safety-spring-2016/
https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf
ISO/IEC/IEEE 15026-2:2022 — Systems and software assurance — Assurance case
https://www.iso.org/standard/80625.html
HELM — scenario-based multi-metric model evaluation — 2022
https://crfm.stanford.edu/2022/11/17/helm.html
AI Agents That Matter — cost-aware evaluation, reliability and verifier limits — 2024
https://arxiv.org/abs/2407.01502
AI Control — safety/usefulness tradeoffs under bounded trusted oversight — 2024
https://proceedings.mlr.press/v235/greenblatt24a.html
ORBIT — configurable multi-agent architecture / defense comparison — 2026
https://arxiv.org/abs/2609.33102
MasDrift — authorization preservation, task utility and defense overhead across coordination structures — 2026
https://arxiv.org/abs/2608.07556
AgentOps-Bench — completion, cost, efficiency, reliability, recovery and prompt-injection safety
https://github.com/kunwarshivam/agentops-bench
Active Testing — sample-efficient model evaluation — 2021
https://proceedings.mlr.press/v139/kossen21a.html
tinyBenchmarks — sample-efficient benchmark estimation — 2024
https://proceedings.mlr.press/v235/maia-polo24a.html
**Figure S5 — Claim boundary and maturity**
## SUPPLEMENT F — PUBLIC ROUTES AND EVIDENCE REGISTER
Public challenge and benchmark routes
FG-TIDA Use Case 21:
https://github.com/FG-TIDA/use-cases/issues/21
FG-TIDA Theme 13:
https://github.com/FG-TIDA/themes/issues/13
FG-TIDA Theme 21:
https://github.com/FG-TIDA/themes/issues/21
Canonical Architecture Benchmark and Reference Scenario Evidence:
https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md
Evidence register — minimum submission-facing claims
Claim: TEVV-Athlon uses four stages and supports Blocks, Events and Tools.
Primary source: NIST AI 200-2 ipd.
Support level: direct.
Claim: NIST already includes agent / tool abuse testing.
Primary source: NIST AI 200-2 ipd, Appendix B.
Support level: direct.
Claim: independent review / challenge and experimental design are already part of the Framework guidance.
Primary source: NIST AI 200-2 ipd, Appendices D–E.
Support level: direct.
Claim: repeated trials and sampling considerations are appropriate for stochastic evaluation.
Primary source: NIST AI 200-2 ipd, Appendix E, Table 7.
Support level: direct.
Claim: the Hugging Face incident and independent investigation exist.
Primary sources: OpenAI, Hugging Face, METR.
Support level: direct for the historical incident; contextual only for the narrower R01 mechanism.
Claim: UC-21, the benchmark, R01 and Ecosystem Positioning are public working artifacts.
Primary sources: linked GitHub repositories above.
Support level: direct for existence and stated content; no claim of NIST, FG-TIDA or employer endorsement.
END OF COMMENT AND SUPPLEMENTARY MATERIAL