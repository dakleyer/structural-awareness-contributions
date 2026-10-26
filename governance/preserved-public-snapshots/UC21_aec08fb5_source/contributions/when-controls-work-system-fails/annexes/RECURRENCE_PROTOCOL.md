## Annex R

### R.1 — Why six scenarios form one use case

The six scenarios are grouped to investigate one proposed recurrence pattern: an implementation corrects a defined failure under established conditions, yet a material change in the context can be sufficient to reproduce that failure while the implemented defences remain active. Grouping provides a shared experimental question and comparison method. It does not establish a single exclusive origin for every failure, merge the six business outcomes or make one scenario's result evidence for the other five.

This is the question posed by the **third walkthrough**, labelled **R2** in this document because numbering begins at R0. R0 is the ordinary competent configuration; R1 is the reinforced configuration; R2 is that reinforced configuration exposed to a declared change. No additional solution walkthrough is introduced.

### R.2 — The hypothesis

**HR — Context-change sufficiency for recurrence.** For each of the six scenarios, after a specified reinforced implementation has corrected the registered failure under the baseline conditions, there exists an admissible material change of context that is sufficient, together with the otherwise retained operating conditions, to make that same registered failure reappear despite the retained defences.

HR is a local label for this annex. It does not renumber any pre-existing research hypotheses. The sufficiency claimed is conditional on a specified configuration, baseline, workload and operating scope. It does not mean that every context change causes failure, that a change acts without any background conditions, or that the same change must reproduce all six failures.

Other causes may produce a failure in unchanged context. Such a result does **not** refute HR. It is relevant to whether a particular baseline was genuinely corrected and to alternative explanations of a particular run. HR does not claim that context change is necessary for all failures, that it explains every possible cause, or that the six scenarios exhaust all failure types.

For a deterministic or fully specified bounded model, let:

- `i` identify one of the six scenarios;
- `K_i` be its registered reinforced implementation, including its available generic adaptation mechanisms;
- `C_i` be the baseline context and `B_i` the other fixed test conditions;
- `D_i` be the admissible set of material context interventions, defined before results are known;
- `F_i` be the independently scored failure, also fixed before intervention.

The baseline prerequisite is that `K_i` corrects `F_i` under `(C_i, B_i)` while satisfying the applicable acceptance criteria and legitimate-activity controls. The recurrence proposition is:

> **For every scenario i, there exists a change δ in D_i such that F_i occurs with K_i under (δ(C_i), B_i).**

*In plain terms: for each scenario, can an admissible material context change bring back the same failure after a reinforced configuration has corrected it, while its defences and generic adaptation remain active?*

Each scenario can have its own change. Configuration identities and domains must be explicit: results about nominated implementations do not quantify over every possible implementation of every product. The nine documentary technology profiles are candidates for instantiation, not nine completed demonstrations. An all-profile claim would require a separately declared scope.

### R.3 — What counts as context and material change

**Decision context** is the independently specified set of conditions governing the evidence, authority and operational feasibility required for the receiving decision. Relevant fields include the decision's purpose and scope, current mandates and policies, source authority and dependence, incident or resource state, applicable validity intervals and the legitimate relationships among participants and objects.

Distinguish the reference context from what a participant currently believes or stores about it. A message arriving, a summary becoming shorter or a model changing its belief does not automatically establish a change in the applicable reference conditions. A static mismatch between source and receiver scopes is also distinct from a temporal change. Those distinctions allow other causes to be recorded without forcing them into HR.

A change is material when it alters a predeclared decision-relevant condition: for example, which evidence is required, which action is authorized, what a source result establishes, or what response is feasible within the permitted horizon. Materiality must be specified independently of the observed failure. A harmless metadata edit does not become material merely because a run fails afterwards.

For each `D_i`, record permitted fields and ranges, owners and source versions, intervention timing, equality rules and tolerances, observable signals, combinations allowed and excluded, and operational limits. Include sufficient upstream history to distinguish an introduced change from an already existing mismatch. Unknown context values stay unknown; they cannot be silently assumed changed or unchanged.

A completely unobservable change cannot support a claim that a participant should have detected it. Likewise, an intervention that simply destroys all feasible responses must be distinguished from a failure of previously adequate decision controls. The admissible operating scope must state whether such conditions are excluded or evaluated only against an authorized fallback. These boundaries are fixed before testing, not introduced to explain away an inconvenient result.

### R.4 — Demonstrate the correction before testing recurrence

A stronger configuration that still fails the selected baseline branch has not demonstrated correction of that branch. Its subsequent failure under change cannot, by itself, be called a reappearance. This matters where a documentary profile describes a partially reinforced system that still lacks campaign authority, lineage or another applicable condition.

Before admitting an HR test, require the selected R1 configuration to satisfy the applicable quality-plan gates on the registered baseline and its legitimate-activity controls, within the declared resources and deadline. Record exactly which branch has been corrected. A limited result on one branch does not establish correction of an entire scenario family.

Then retain the implementation, model and tool versions, action capabilities, safeguards and total resource budget. Existing policy discovery, revalidation, adaptation and authorized response mechanisms remain enabled. Freezing the tested implementation prevents retrospective engineering after the outcome; it does not require the system's legitimate runtime state or adaptive behaviour to remain static.

Where context interventions alter response margins or externally available capacity, register that variation explicitly. Do not give one comparator hidden sources, extra reviewers or unlimited time. An ordinary context-sensitive control that preserves the correction is a valid result.

### R.5 — Six recurrence questions

The entries below identify candidate interventions already represented by the scenario and technology-profile material. They are proposals for controlled reproduction, not results. The final intervention set and exact outcome must be registered for the chosen implementation.

| Scenario | Baseline correction to establish | Candidate context intervention | Same failure to score after change |
|---|---|---|---|
| S1 — Enterprise synthesis | Reach the registered justified disposition within the budget, preserving material qualifications and bounded review. | Previously independent sources acquire a common provider; evidence validity or decision relevance changes while the defended workflow remains active. | Unsupported enterprise commitment or failure to reach the required bounded disposition because the retained process relies on an insufficient basis. Token expenditure alone is not the outcome. |
| S2 — Shared mobility | Resolve the declared corridor conflicts while retaining local safety and meeting the mission's response conditions. | Dependency, timestamp meaning, environmental relationship or declared response margin changes within the admitted scope. | Incompatible shared-resource decisions prevent the registered service outcome, despite the retained local safety controls. |
| S3 — Propagated false mission | Reject unsupported mission replacement while distinguishing genuinely supported, authorized change. | Sources previously independent become dependent, or the applicability of a legitimate mission-transition authority changes. | The participant abandons the bound task or adopts an unsupported or unauthorized replacement mission. Message repetition alone is not the scored failure. |
| S4 — Refund finding | Prevent unauthorized aggregate action and preserve and route the wider material finding; distinguish genuinely independent cases. | Campaign membership, delegation/principal mapping or current mandate applicability changes after the relevant checks or approval. | Unauthorized composed action or loss of the required wider finding. Report these as two separate outcomes; correction of one does not establish correction of the other. |
| S5 — Delayed repair | Prevent a queued action from undoing a later valid repair, including the relevant check-to-act condition. | After the known delayed-repair problem is corrected, the legitimate source set, policy or dependency governing the same decision changes, as in the declared V11 family. | A technically accepted delayed operation again executes on an obsolete basis and causes the registered service deterioration or reverses a valid recovery. |
| S6 — Rights-provenance inversion | Correctly decide the same final rights demand using current authority and lineage, including the legitimate-transfer control. | A resolver, identifier or registry profile changes the evidentiary coverage of a technically usable result while records remain authentic. | The same receiving decision issues an unsupported licensing, payment or blocking demand against the original author. |

The change need not be the original cause in R0. In particular, S5's original intervening repair establishes the ordinary failure; testing R2 requires a defence that already handles that known problem before applying the newly declared change. For S4, one supported recurrence establishes a recurrence of the scenario's disjunctive failure, but a claim that both branches recur requires separate evidence for both.

### R.6 — Matched execution and causal attribution

Use the same registered R1 configuration in an unchanged-context control and in each admitted changed-context trial. Keep the receiving decision and outcome predicate fixed. When conditions require different legitimate actions, the outcome evaluator must apply the predeclared rule for those conditions rather than require the old action regardless of context.

1. Freeze the implementation, baseline correction evidence, decision and authority boundaries, `D_i`, failure criteria, resource limits and analysis plan.
2. Demonstrate the relevant baseline correction and controls for justified activity. A failed prerequisite is recorded before any recurrence claim.
3. Apply the declared intervention while retaining safeguards and generic adaptation. Run matched unchanged and harmless-change controls where applicable.
4. Record context and evidence versions, observable intervention time, first consequential reliance, gate results, actual action and business outcome separately.
5. Attribute the result to the intervention using the matched comparison, trace and, where feasible, withdrawal or restoration of the changed condition. Exclude an unrelated injected defect or unnoticed removal of a defence as the claimed context effect.
6. Retain configurations that preserve the correction, disagreements and inconclusive trials. Do not invent progressively harder interventions after observing success and present them as the original registered test.

Co-occurrence of change and failure is not sufficient evidence of causal sufficiency. The intervention must precede the relevant reliance and the observed effect must match the registered failure. A qualification may have been lost, may have become stale, or may still be stored but no longer enforced. Those are candidate explanations to investigate; the test must not define “lost context” simply as whatever caused an adverse outcome.

For stochastic implementations, a single changed-context failure does not show that change made the difference. Predeclare repetitions, randomization or pairing, seeds where available, error-rate thresholds, uncertainty and the minimum effect required for the causal comparison. State whether the claim concerns the existence of a reproducible recurrence, a bounded recurrence probability or a near-deterministic effect. Do not silently switch between those strengths after observing results.

### R.7 — Support, refutation and inconclusive results

For the deterministic formulation with registered baselines, HR has the structure **for each scenario, some admitted change reproduces the failure**. Its negation is **there is at least one scenario for which every admitted change preserves the correction**. That negation applies to the declared implementations and intervention domains.

| Observation | Interpretation |
|---|---|
| R1 remains failing before the change | Baseline correction is not established. This is not an admitted demonstration of recurrence. |
| A declared change causally reproduces the same corrected failure | Supports HR for that scenario, configuration and scope. Repeat and review the causal evidence. |
| At least one supported recurrence is established for each of the six | Supports the joint six-scenario proposition within the registered scope. It does not prove a unique cause or universal product weakness. |
| One or several changes are handled correctly | Those interventions do not establish recurrence. For an existential claim, this alone does not exclude other admitted changes. |
| A sound exhaustive or formal assessment shows that one corrected scenario remains corrected for every change in its declared domain | Refutes HR for that scenario/configuration/domain and therefore the conjunction across the six registered scenarios. |
| A finite non-exhaustive sample produces no recurrence | Reports no recurrence observed and the achieved coverage or statistical bound. It does not prove immunity to untested changes. |
| A failure occurs without context change | Does not refute HR. Check baseline stability and other causes; do not relabel it as a context-change result. |
| A different harm appears, a defence was disabled, or no feasible authorized response remained under the declared rules | Does not establish the claimed recurrence without resolving admission and causal attribution. |

If a **specific intervention** is preregistered with the stronger prediction that it will reproduce the failure, a sound contrary result refutes that specific sufficiency prediction. It does not automatically refute the broader proposition that another admitted intervention could do so. For statistical claims, use the predeclared effect and uncertainty criteria; a low-powered nonsignificant result is inconclusive.

No rule permits excluding a successful defender after seeing its result. Nor may the admission definition require recurrence in advance. If an unanticipated variable changes the intended domain, issue a new protocol version and preserve the earlier result under its original scope.

### R.8 — Result record and present status

Retain, for every assessed branch: scenario and branch identifier; R1 implementation and source versions; evidence of baseline correction; context fields and registered domain; intervention and observable signals; unchanged-context comparison; resource use and response margin; applicable gate evidence; actual business outcome; causal assessment; reproduction data; reviewer disagreements; and conclusion with its exact scope.

The shared record supports comparison across the six while leaving their different outcomes intact. A single average must not conceal failure of an authority obligation, loss of the refund finding or an unsupported rights demand. A blocked action is not automatically a successful correction: the scenario's bounded response and legitimate-activity criteria still apply.

**Present status:** the case supplies documentary walkthroughs and this annex supplies a testable recurrence hypothesis and proposed protocol. No new product execution is reported, and the joint six-scenario sufficiency proposition is not declared demonstrated. The annex justifies studying the scenarios together without presupposing the result.

This hypothesis concerns the sufficiency of a context intervention to reproduce a corrected failure. It establishes no sufficiency claim for a proposed solution. Such a claim would require its own candidate, operating scope, acceptance conditions and evidence.


