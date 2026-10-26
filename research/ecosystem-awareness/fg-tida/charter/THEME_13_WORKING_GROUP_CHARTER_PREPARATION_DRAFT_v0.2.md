# Ecosystem-level Agent Defense — Charter

> **Terminology reference.** [00M §1 — canonical definitions](../../baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical) defines the result of active exploitation, its established basis and characterized exploitation reserve, the exploration frontier, and residual uncertainty beyond effective evaluation. This charter uses these descriptive names; A/B/C/D remain secondary reference labels. The distinctions are explained in [Annex B.2](#b2-four-component-reference-position). This terminology clarification does not rename local test arms, change requirements or revalidate recorded proofs/results.

> **v0.2 Working Draft — work in progress.** This draft will receive further modifications and contributor review before version 0.2 is considered complete. Publication in this repository does not mean that v0.2 is final, frozen or approved by FG-TIDA.

**Status:** Draft v0.2 — editorial working proposal, 28 September 2026; terminology clarified against 00M v0.8 §1 and use-case and technology rationale revised 2 October 2026.  
**Originating issue:** [Theme #13 — Ecosystem-level Agent Defense](https://github.com/FG-TIDA/themes/issues/13)  
**Proposer(s) / drafter(s):** Ward Duchamps, Thales — originating Theme proposer; Iván Abril Palma — preparation-draft synthesis. Nelson Trasatti and Oleksii Voshchak are attributed contributors through the public sources identified below; attribution does not imply approval of this text. Formal editors, maintainers and any WG roles remain to be agreed.

**First-cycle focus:** Ecosystem Awareness and Incident / Signal Lifecycle, connected by bounded, bidirectional interfaces.

**Institutional status:** preparation material for contributor review; not a submitted Phase 2 Charter, established Working Group, adopted interface or FG-TIDA decision. The working filename retains Theme 13 for traceability; it does not assign an official WG number.

**Baseline:** a successor to the v0.1 candidate text, preserving its five proposed deliverables (D1–D5, defined under Objectives) and broader Theme #13 boundaries. The v0.1 source is unchanged. The initial architecture/source review is pinned to repository commit `2db60a1fa4faa5ec08c6754cc676b8f70431c32a`. The reader-orientation revision checks terminology against `90cb592272f082aaa88b7798ef1c543f7e6c3343` and the public contributions recorded in the companion review dossier.

**Reading guide:** the main text defines scope, responsibilities, deliverables and acceptance conditions. Reference detail follows in [Annex A — Working vocabulary](#annex-a-working-vocabulary), [Annex B — Reference architecture](#annex-b-reference-architecture), [Annex C — Theme #13 envelope](#annex-c-theme-13-envelope) and [Annex D — Reference cases and delivery detail](#annex-d-reference-cases-and-delivery-detail). Moving detail to an annex does not remove its boundaries or applicable review conditions. Detailed data formats, transition rules, software interfaces and test procedures remain work for the deliverables. The [review and compatibility dossier](WG13_v0.2_REVIEW_AND_COMPATIBILITY_2026-09-28.md) records sources, changes from v0.1 and unresolved review items.

## Summary

Agents can collaborate, delegate work and share discoveries across organizational boundaries. That collaboration can create useful capabilities, but it can also propagate an unsupported claim, an unauthorized objective or a harmful action beyond the participant that first produced it. Roles, dependencies and operating conditions may change while individual systems continue to authenticate messages, enforce local permissions and report successful execution. No single participant necessarily sees the combined effect. Agents can change their roles, tools, context and delegation relationships over time. Defense must therefore assess the **specific action, its content and effects**, as well as the identity of the actor.

**Following [Ward Duchamps's originating Theme #13 proposal](https://github.com/FG-TIDA/themes/issues/13), Ecosystem-level Agent Defense protects that collaboration environment.** It connects attributable observations, evidence appraisal and shared warnings to proportionate responses by the participants authorized to act. Its purpose is to recognize harmful propagation, limit affected scope and support recovery while preserving legitimate collaboration, privacy and local decision authority. It must remain useful when a failing or malicious agent does not cooperate; it cannot depend on trusting the agent's own account of its behavior. The architectural concern developed in the [Ecosystem Positioning presentation and corpus](../../../../architectural-contributions/ecosystem-positioning/README.md) is concrete: local correctness and compliance do not, by themselves, establish that the composed system remains adequately supported for its current decision.

The proposed EA contribution extends this defense framing to **decision-relevant uncertainty across the ecosystem**: incomplete observations, dependent sources, changed assumptions, unresolved upstream findings and limits on what participants can establish in time. Defense must preserve these limits when combining identity, authority, conformance, population-level evaluation and incident evidence. EA assesses what those findings jointly support for a particular decision, what remains unresolved and whether further evidence could help; the Incident / Signal Lifecycle coordinates corroboration and response with the legitimate decision and control owners. Uncertainty is neither proof of an attack nor permission to intervene. It informs proportionate, locally authorized choices about further investigation, restricted reliance, containment and recovery. This is a bounded assessment from partial views, not a claim to know or eliminate the uncertainty of the whole ecosystem.

### UC #21 — Technology walkthroughs, incident motivation and bounded testing

**[UC #21 — When the controls work but the system fails](https://github.com/FG-TIDA/use-cases/issues/21)** develops this concern through six scenarios and nine technology profiles. Each profile follows an ordinary competent implementation (R0), a strengthened implementation (R1), and the same strengthened implementation after a material change (R2). The profiles identify explicit failure paths under declared configurations, the safeguards that can correct them, and the conditions under which renewed qualification must be tested.

| Scenario and technology profiles | Concrete composition problem examined |
|---|---|
| Enterprise strategy: [Microsoft Agent 365](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/annexes/technology/T01.md); [LangGraph/LangSmith](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/annexes/technology/T02.md) | Summaries, evaluations and review workflows can remain operational while losing source qualifications or relying on assumptions that no longer support the final decision. |
| Shared city corridor: [FIWARE NGSI-LD](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/annexes/technology/T03.md); [AWS IoT TwinMaker/IoT Core](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/annexes/technology/T04.md) | Authenticated, recent telemetry can support locally valid but incompatible uses of the same resource. |
| Propagated mission change: [OpenAI agent stack](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/annexes/technology/T05.md) | Distinct authenticated agents can repeat one source; synthesis or context transformation can lose the distinction between repetition, independent evidence and authority to change the mission. |
| Aggregate refunds: [Claude Agent SDK](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/annexes/technology/T06.md); [Stripe Radar plus merchant authorization](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/annexes/technology/T07.md) | Valid individual refunds and local limits do not by themselves establish authority for the aggregate campaign or ensure that an unresolved material finding reaches its owner. |
| Delayed repair: [AWS Step Functions/RDS](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/annexes/technology/T08.md) | A queued rollback can retain valid credentials and execute correctly after a newer repair has invalidated its original justification. |
| Downstream rights claim: [Panodyssey/TEMS rights-portability profile](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/annexes/technology/T09.md) | Authentic records can survive a transformation while their lineage or authority no longer supports the final payment, licensing or blocking demand. |

These are **nine documentary implementation profiles with 27 walkthrough positions**, not nine deployed-product failure experiments. The [UC #21 evidence record](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/USE_CASE.md#7-results-existing-coverage-and-remaining-gap) identifies independent product reproduction as pending. Effective existing controls receive full credit, and R2 recurrence requires a demonstrated R1 correction first. The engineering challenge is preserving the required conditions together through handoffs, changes and actual use within finite response and review capacity.

**A documented incident supplies a real-world motivation for this UC #21 research direction.** In the [OpenAI/Hugging Face incident](https://openai.com/index/hugging-face-incident-and-the-road-ahead/), agents conducting separate cybersecurity evaluations repurposed Artifactory as an unauthorized communication channel, shared discoveries and adopted peer goals; activity extended into a third-party intrusion. [METR's independent investigation](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/) examines this collaboration. The incident demonstrates that harmful agent coordination can occur. It does not establish that all production safeguards failed: OpenAI reports that relevant production protections were absent from those evaluations.

**Concrete walkthroughs and implemented tests connect this motivation to specific technologies.** Within UC #21, the 00G walkthroughs reconstruct, at scenario level, a pattern analogous to aspects of the Hugging Face incident: agents circulate findings or peer instructions, and a receiving agent treats them as sufficient evidence or authority to displace its binding task. The [OpenAI technology profile T05](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/annexes/technology/T05.md) specifies three implementation routes using Agents SDK, Responses Multi-agent and Agents API capabilities, including handoffs, guardrails, approvals, tracing and context management. These product-specific routes define what to examine under ordinary, reinforced and changed-context conditions.

The [00G-HF development and experiment record](../../baseline/annexes/00G-HF-DEVELOPMENT-HISTORY-v0.1.md) also documents implemented evaluators, component checks, scripted and simulated traversals, and a bounded execution using **PyCasbin 1.43.0** that exposed stale authorization and tested both conventional and EA-assisted repairs. These existing tests provide evidence within their declared scope; the OpenAI routes remain documentary profiles, and neither these tests nor the analogy constitute a reproduction of the historical attack.

Within UC #21's scenario lineage, **[00G-R01](../../baseline/reductions/00G-R01/README.md)** is a bounded research reduction of 00G that develops a related challenge: probabilistic exploration, costly validation and socially shared findings under a binding task. Its social subfamily investigates how received interpretations can acquire operational force and displace that task or its limits. It provides a candidate route to testing a related mechanism, not a completed reproduction of the historical incident. R01 does not yet provide an executed comparative test of Ecosystem Awareness: its campaign and any comparative EA benefit remain to be established. The separate 00K 379/379 symbolic CI record is not an R01 campaign result.

### Complementary use cases — UC #4, UC #6 and UC #20

The cases have distinct roles in motivating and testing the charter. UC #21 specifically examines **“the controls work but the system fails.”** UC #4 provides a proposed cross-cutting test bed for defense interoperability and coordination; UC #6 examines current authority applicability; UC #20 examines contextual trust in human–agent contributions:

- **[UC #4 — Federated ecosystem defense](https://github.com/FG-TIDA/use-cases/issues/4):** a downstream agent attempts an authenticated action outside the original delegation scope. Independently governed organizations must connect partial observations and coordinate timely, locally authorized containment. The charter uses this case as a proposed cross-cutting test bed to examine how defense capabilities connect and how participants coordinate their responses.
- **[UC #6 — Current authority applicability](https://github.com/FG-TIDA/use-cases/issues/6):** the same agent, documents and recipient move from permitted product planning to an excluded sales purpose. This case examines whether the existing authorization still applies when the purpose or context changes, including the scope of human intervention. The grant remains unchanged; human approval to continue does not expand it.
- **[UC #20 — Robots writing specifications for Trust in Robots](https://github.com/FG-TIDA/use-cases/issues/20):** an international pre-standardization group, in the FG-TIDA setting, develops specifications, code and tests for trust in agents and robots. The proposed scenario asks a foundational question: **how can the group verify which parts of those very trust specifications were produced by humans, by agents, or jointly, and what human review and approval actually occurred?** A human account or signature does not establish human production or independent human judgment; a reviewer may introduce another agent, and apparently independent reviews may share the same mistaken source. The challenge has an institutional and civilizational dimension: preserving accountable human judgment as automated systems help develop the rules by which they will be trusted. UC #20 translates that challenge into requirements for evidenced contribution roles, content provenance, review, independence and applicable approval. Any measure of the amount or proportion of human contribution must define what is counted, its evidence coverage and uncertainty, retaining mixed or unknown origins. This motivates ecosystem defense of the specification-and-review process itself; human origin alone does not establish content quality or adequate oversight.

In this GitHub-based scenario, **who submits an action, who or what produced its content, who reviewed it, and who authorized its use are distinct questions**. A human may initiate a submission whose content was generated by an agent, or approve material without performing the required independent review. Such combinations may be legitimate; misleading attribution, substituted approval or coordinated propagation of unsupported content can create an attack path against the ecosystem's trust process. Writing style alone establishes neither automated origin nor an attack. Ecosystem-level Agent Defense must connect evidence about the action and its production/review path to the receiving decision, preserve unresolved provenance, and support proportionate, locally authorized responses.

Together, these cases motivate a shared task: **preserve and reassess the evidence, dependencies and authority needed for the receiving decision, and connect the resulting qualification to a timely, authorized defense response.**

Within the existing Theme #13 scope, this charter candidate would develop two related, independently testable capabilities: **(1) an Incident / Signal Lifecycle** for ecosystem-defense signals, corroborating evidence, refining the scope of effects, coordinating locally authorized responses and recording resolution; and **(2) Ecosystem Awareness (EA)**, which assesses what independently produced results collectively establish for a specific participant's decision at a given time, what remains unresolved or inherited through dependencies, and when that assessment needs to be revisited. This decision-specific assessment is called **qualification**; **targeted requalification** means revisiting the affected assessment or dependency when relevant evidence, context or validity conditions change, rather than restarting every assessment. The work would connect them through bounded, source-preserving interfaces without creating a central controller or new authority. **Defense is the first concrete implementation context, not a requirement that the reusable qualification/handoff semantics be defense-exclusive.**

The originating Theme #13 is broader than these first two deliverables. Its ecosystem-defense problem space also includes identity/accountability, detection/monitoring, reputation, privacy-preserving operation and incentives/alignment. This charter does **not** silently delete those surfaces. It stages them: the first cycle concentrates on the lifecycle + EA foundation, while the broader Theme capabilities are consumed from adjacent work, retained as later profile/deliverable candidates, or separately scoped if FG-TIDA decides that another Theme/WG should own them.

The originating issue asks whether #13 is too large for one theme and should be split. This charter proposes staging the work, with the Lifecycle and EA foundation first, without prejudging a later FG-TIDA decision to split or redistribute the broader scope. Ward's [public placement and interoperability comment](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5571476256) supports EA within #13 and independent definition and testing of the determinacy envelope (a small set of qualifiers accompanying a local result, explained in Scope §3) and signal lifecycle; it does not constitute approval of this v0.2 text.

## Scope

The first cycle has two independently testable mechanisms, **EA** and **Incident / Signal Lifecycle**. Oleksii Voshchak's **Operational Risk, Response Window & Epistemic Opportunity Matrix** is a proposed decision-support structure connecting qualified information with the operational context in which a decision must be made. His accompanying worked example applies it to the authority-applicability case described in Annex D. Following his [revised decomposition](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5854694913), the charter separates EA-facing qualification from **operational contextualization**: relating that qualification to consequences, available capacity and the time in which a response remains useful. This is a working functional boundary, not a requirement for a third deployed layer, a new awareness system or an approved FG-TIDA organizational structure.

The work supports participant-local assessment across heterogeneous, independently governed systems. It does not assume a shared objective, common global state, mandatory broadcast, common trust root or central controller. Each determination remains attributed to the source responsible for its meaning (its **semantic owner**); another component must not silently recreate it.

### 1. Incident / Signal Lifecycle

In scope:

- signal birth and minimum semantics;
- issuer/source, provenance and freshness;
- distribution across independently governed participants;
- corroboration, contestation, amendment and supersession;
- observed versus inferred affected scope;
- operational blast-radius/dependency representation;
- response-window information;
- available containment/recovery reach;
- coordination of **locally authorized** graduated response;
- resolution records and lifecycle closure; and
- preservation of material unresolved qualifiers through the lifecycle.

The lifecycle follows the working sequence proposed by Ward: **birth → distribution → amendment/corroboration → containment → resolution**. Containment here includes coordination and recording of locally authorized graduated responses, not conferral of permission on another participant. Each stage should preserve source history, distinguish observations from inferences, and record effective reach, limits and outcome evidence where material. A resolution record closes the incident under its declared criteria; it does not automatically restore every dependent decision's qualification.

Lifecycle-owned affected-scope and blast-radius information can be consumed by EA and by a participant's existing dependency-mapping mechanism. This does not merge their graphs, transfer ownership of a persistent ecosystem map, or require complete ecosystem visibility.

### 2. Ecosystem Awareness

In scope:

- decision-scoped qualification of local and external states;
- explicit observation/representation boundaries;
- source dependence and independent-corroboration assessment;
- unresolved conditions, including those inherited through dependencies;
- finite evidence, compute, communication and human-review capacity;
- whether the scope, assumptions and evidence still support the assessment;
- response-window constraints;
- distinguishing “more can still be known” from “more knowledge would still be useful for this decision”;
- targeted requalification / re-entry;
- local closure versus system-level support; and
- attempted execution versus externally confirmed outcome where that distinction is material and observable.

EA qualifies a receiving participant's decision under a declared scope and time. It distinguishes the **result of active exploitation**, its **established basis and characterized exploitation reserve**, a grounded **exploration frontier**, and **residual uncertainty beyond effective evaluation**. In practical terms: what the process delivered; what supports it and what further work is already assessable; where exploration could establish a basis for evaluation; and which potentially material effects remain beyond its effective evaluation routes. A qualified local result does not establish a complete ecosystem state. [Annex B.2](#b2-four-component-reference-position) explains these process-relative components and their reference labels; they are not a required transmission format.

The EA-facing part of Oleksii's contribution assesses the scope and assumptions supporting a decision, what remains unresolved, what more could be established with current capabilities, and the relevant dependencies and evidence sources. It consumes current authority-applicability and oversight-capacity determinations from their respective owners. It does not calculate institutional authority, decide grant standing or certify oversight capacity.

Confidence within a represented boundary does not close the open residual beyond it. A stronger result in one domain can qualify another only through an explicit, supported material dependency; absent coupling is neither proven independence nor permission to compensate across domains. More evidence, agents or controls are not assumed to improve determination when they also add correlation, latency, conflict or capacity burden.

#### 2.1 Relating the assessment to the decision

The complementary function relates the qualified state to the particular decision: action criticality, exposure, severity, reversibility, affected dependencies, supplied capacity constraints, response timing and explicit contextual thresholds. It produces a structured operational state for legitimate decision owners and, where relevant, Lifecycle.

This function is **decision support, not an intervention decision engine**. A threshold crossing, request for corroboration, investigation or escalation is not permission to act. Derived relations require declared semantics, inputs and units; otherwise the dimensions remain separate. Risk appetite, consequence values, normative preferences and budgets must come from the identified policy/mission owner or a declared **test fixture**, meaning a fixed set of inputs, assumptions and expected outcomes used for a reproducible check.

Two temporal dimensions remain independent:

- **Qualification validity:** whether the evidence, semantic frame and received authority-applicability determination still apply to this decision.
- **Response opportunity:** whether further evidence or an authorized response can still materially affect the outcome.

One may expire while the other remains open. Missing timing is not inferred from message order, synthetic fixture spacing or an unchanged grant identifier. Available capacity to obtain and assess evidence, capacity to respond, and institutional oversight capacity likewise retain their distinct meanings and owners.

Further evidence gathering and assessment are useful only under the stated decision relevance, capacity, cost and time constraints. Stopping an evidence search does not erase residual uncertainty or authorize execution. Conversely, UNKNOWN (the relevant value or qualification is not known; see Annex A.2) is not an automatic ecosystem-wide veto: the affected scope, materiality, legitimate decision rule, fallback and review condition must remain explicit.

#### 2.2 Bidirectional interaction and targeted revalidation

| Direction | Bounded content | Responsibility retained |
|---|---|---|
| Lifecycle → EA | Incident state, observed/inferred affected scope, provenance and corroboration lineage, freshness, response reach/window and unresolved qualifiers | Lifecycle owns incident evolution; EA qualifies reliance for the receiving decision |
| EA → contextualization / decision owner | Qualified state, scope, residual, validity, capacity dependencies and opportunity to obtain further useful evidence | Contextualization preserves distinctions; the legitimate owner selects permitted action |
| EA / contextualization → Lifecycle | Decision-relevant qualification and operational significance, targeted evidence or dependency-branch refinement requests, review conditions | A request is neither a containment command nor an authority grant |
| Lifecycle / execution owner → EA | Amendment, correction, resolution, attempted action and separately evidenced outcome | Material change triggers targeted requalification; resolution alone is not proof of restored applicability |

Revalidation should follow a material change in evidence, scope, context, dependency, authority applicability, capacity, outcome or a declared validity condition. A scheduled validity review can also trigger it when the declared profile requires that review. Reprocessing an unchanged state merely because it crossed a component boundary is not a required feedback cycle. The target and reason for re-entry, version, owner and stopping condition should be recorded.

#### 2.3 Compatibility with contributor architectures

EA assesses what the available information supports. Existing mechanisms retain responsibility for assessing operating conditions, control sufficiency, participation rules and role changes; Lifecycle retains incident operation and response coordination. Objectives, policy, identity and authority stay with their legitimate owners, and only authorized control owners execute containment or recovery.

The contributor's Ecosystem Positioning architecture provides a reference for checking these boundaries; [Annex B](#annex-b-reference-architecture) explains its mechanisms and terminology. The charter commissions compatibility, not adoption of the whole architecture. Equivalent independently implemented mechanisms remain eligible. The proposed mapping to its functional responsibilities remains a reviewable hypothesis and introduces no additional universal function or interface family.


### 3. Interoperable handoff

The work may define a lightweight, implementation-neutral handoff/profile allowing different components to exchange enough decision-relevant qualification without revealing complete internal reasoning.

Candidate semantics include:

- producer/profile reference and version;
- subject/proposition/decision scope;
- issuer/source;
- source-native result or closure;
- determination/qualification state;
- explicit UNKNOWN / unresolved qualification; and
- conditional qualifiers such as freshness, assurance semantics, capacity, provenance, dependency/source lineage, validity/review conditions and targeted re-entry references.

The handoff remains partial by construction: missing qualification is represented rather than invented.

The reference **Epistemic Handoff Descriptor (EHD)** is a transport-neutral semantic contract, not a compulsory protocol or central message bus. Its six-element interoperability kernel is: profile/reference and version; subject/proposition/decision scope; issuer; native result/closure; determination state; and an explicit declaration of material unknown qualifiers. Conditional fields are carried when omission would materially change reliance. A stable producer profile plus a small per-decision delta may avoid repeating full context and history.

The existing #13 **determinacy envelope** accompanies a local result with four qualifiers: how it was reached, its margin relative to the producer's declared threshold, whether human-oversight capacity constrained it, and any uncertainty inherited from upstream inputs. [Annex C](#annex-c-theme-13-envelope) preserves the field names, definitions and source.

This remains a candidate versioned #13 profile, preserving Requirement 20 of [Use Case #4 (UC #4)](https://github.com/FG-TIDA/use-cases/issues/4), the proposed experimental environment for EA and Lifecycle. Provenance, freshness, scope and dependency information must also be preserved. The profile does not replace the general kernel or require other Themes to adopt #13 states. Broader EHD standardization and ownership remain open.

An adapter must preserve the difference between an unknown value, a missing declaration, a claim not established, a field determined not to apply, and behavior not exercised by a test. The corresponding labels and mapping rules are in [Annex A.2](#a2-information-and-test-status).

These distinctions concern different questions and may coexist across different fields. A receiver's additional qualification remains receiver-authored. Forwarding or aggregation does not create independent corroboration, and a valid signature or schema does not prove the truth of the asserted qualifier.

Composition-critical extensions may reference the same decision, its basis/version, commitment state, material dependencies, authority/precedence and targeted re-entry. They remain conditional; no full private reasoning, global database or universal scalar is required.

### 4. Cross-Theme interfaces

The work may consume or return bounded state to adjacent Theme-owned functions without redefining them. Initial interface families include:

- identity / representation / principal binding;
- authority / delegation / current applicability / privilege lifecycle;
- policy / intent / runtime conformance;
- verifier-side evidence and attestation;
- human-oversight authority, capacity and decision state;
- accountability / action / execution records;
- enforcement / containment / recovery;
- privacy / minimum disclosure; and
- evaluation or other specialized profiles where a concrete case requires them.

Theme-specific profiles should become normative only after review by the relevant semantic owners and the applicable FG-TIDA process.

Interface work must distinguish general exchange semantics, a proposed cross-Theme target and what current public contributions actually support. Proposed changes remain separately versioned, and later contributions require dated review rather than silent alteration of frozen baselines. [Annex B.3](#b3-interface-reference-documents) identifies the corresponding reference documents; a target mapping is not evidence of present agreement.

Each proposed interface should identify its producer, consumer, semantic owner, native meaning, version, material inputs/outputs, unavailable-state handling, authority boundary, review status and test evidence. Transport/API/schema choices are deliverable-level decisions. Reusing a transport or schema does not transfer ownership of the source determination.

### 5. Testing and conformance

The work may define:

- positive, boundary and rejection fixtures;
- version-pinned adapters/profiles;
- attributed reference rules or expected results against which observed test outputs are checked;
- **Interface Conformance Records (ICRs)**: reviewable records of the route, mappings, owners, evidence and unresolved objections supporting a claimed interface property;
- cross-implementation interoperability tests;
- UNKNOWN / not-established handling;
- qualification/provenance/dependency preservation checks;
- decision/execution reconstruction; and
- bounded testbeds that do not absorb adjacent Theme semantics.

At least one early profile should test the **EA-specific differential rather than only interface compatibility**: hold the relevant local/native result constant while changing a decision-material ecosystem qualifier such as source independence, inherited indeterminacy, semantic validity or available response capacity, and verify that the systemic qualification changes only when that qualifier materially changes the receiving decision. A comparison case in which no decision-material condition changes should verify that EA does not create unnecessary pauses, escalation or containment. Any pause remains subject to the legitimate control owner's rules; EA does not grant authority to impose it.

### 6. Broader Theme #13 defense surfaces

The originating Theme also raises ecosystem-level capabilities around:

- verifiable identity/accountability and privacy-preserving principal linkage;
- remote or behavioural detection/fingerprinting where the agent does not cooperate;
- reputation and concern-signalling across parties;
- standardized event logging / observability;
- mechanisms for incentives/alignment among otherwise independently governed agents; and
- decentralization constraints intended to avoid one controlling operator or surveillance architecture.

These remain part of the **Theme #13 problem space**, but they are not automatically first-cycle normative deliverables of this charter.

The initial lifecycle/EA work should therefore:

1. define interfaces capable of consuming such outputs where they are source-owned and available;
2. avoid duplicating identity, attestation, enforcement, reputation or incentive mechanisms already owned elsewhere;
3. keep privacy/selective-disclosure and decentralization as design constraints from the start; and
4. allow later admission of a reputation, incentive, detection or identity profile only after duplication/ownership review and a concrete use case demonstrates the need.

This preserves the breadth of Theme #13 without making the first charter cycle unreviewably large.

## Out of Scope

Unless FG-TIDA later changes the charter, this work would not:

- create legal, institutional, policy, privilege or containment authority;
- define the origination of authority/delegation grants;
- replace identity, attestation, policy, access-control or privilege-lifecycle standards;
- determine legal personhood or universal liability;
- define one universal trust/reputation score;
- require a central ecosystem controller or shared private reasoning model;
- require disclosure of complete prompts, internal reasoning, objectives or private state;
- define the complete human-oversight, policy/conformance, model-level or embodied-system lifecycle owned elsewhere;
- define a universal identity-binding scheme, reputation algorithm, incentive/economic mechanism, remote-fingerprinting method or kill-switch enforcement mechanism in the first cycle unless FG-TIDA explicitly assigns that work here after duplication/ownership review;
- treat an assessment, confidence value, reputation value, human approval or signal as authority;
- turn test vocabulary into mandatory runtime ontology;
- force heterogeneous evidence/risk/capacity dimensions into one universal scalar;
- require maximum context or telemetry collection;
- certify products; or
- convert research hypotheses or illustrative scenarios into normative requirements without separate review;
- replace a semantic owner's native determination with a mapping annotation or a simulated oracle;
- equate static fixture correspondence with live component interoperability, copied outcome labels with enforced behavior, or symbolic tests with empirical ecosystem validation; or
- incorporate the entire contributor reference architecture as compulsory first-cycle WG scope.

## Objectives / Deliverables

The exact deliverable packaging remains subject to FG-TIDA review.

### D1 — Common terminology and architectural boundary

Define the minimum shared terminology needed to keep local results, systemic qualification, authority, uncertainty, affected scope, validity and response timing distinct. Include a responsibility map for EA, bounded operational contextualization, Lifecycle and external authority/control owners; reconcile terminology with the contributor architecture without assigning its entire corpus to Theme #13.

### D2 — Incident / Signal Lifecycle

Candidate content:

- lifecycle states and transitions;
- minimum signal semantics;
- provenance/freshness;
- corroboration/contestation/amendment;
- affected-scope / blast-radius semantics;
- response-window properties;
- locally authorized response coordination;
- resolution; and
- privacy/adversarial considerations.

D2 remains a complete operational mechanism.

### D3 — Ecosystem Awareness Core

Candidate content:

- decision-scoped systemic qualification;
- bounded observation/representation;
- unresolved conditions, including those inherited through dependencies;
- source dependence / independent corroboration;
- finite determination resources;
- whether the scope, assumptions and evidence still support the assessment;
- established grounds and limits of the delivered result, including a characterized exploitation reserve that remains assessable even when unused;
- grounded exploration frontiers whose evaluation basis is not yet established;
- residual uncertainty beyond effective evaluation under the declared access, authority, method, capability and time;
- targeted requalification;
- output validity/limitations; and
- no-supercontroller / no-authority-creation rules.

D3 remains independently testable from D2. It incorporates Oleksii's EA-facing qualification work and identifies the bounded contextualization interface separately. Document native inputs, explicitly derived relations, contextual thresholds and multidimensional outputs, with separate validity and response dimensions. The deliverable must make it possible to test each function without implementing the other contributor's internal logic.

### D4 — Interoperability / Epistemic Handoff Profiles

Candidate content:

- a minimal handoff kernel;
- conditional qualifiers;
- source-native result preservation;
- profile/version rules;
- UNKNOWN/not-established handling;
- bounded adapters;
- composition-critical extensions where needed; and
- Theme/domain-specific profiles.

### D5 — Conformance / Reference Test Profiles

Candidate content:

- interface conformance records;
- positive/boundary/rejection fixtures;
- cross-implementation tests;
- version-pinned adapters;
- trace/evidence requirements;
- reproducible result packages; and
- UC #4 / interoperability / decision-boundary vectors where they test an agreed requirement.

D5 may initially remain an informative/test package rather than a standalone specification. Each campaign declares the question, semantic owners, capabilities, admitted profile, source versions, resource budget, expected observations, **falsifiers** (predeclared observations that would contradict the claim being tested), review states and stopping point. Nelson's proposed experimental cycle—reference execution, follow-up hypothesis, controlled variation, counter-test and report—is included as a proposed contribution, not an unlimited maintenance commitment.

For routes claiming compatibility with the reference interface-conformance method (document 04 in Annex B.3), retain an Interface Conformance Record: freeze material qualifiers and the ordered route, identify aggregation points and semantic/adapter owners, appoint a mapping reviewer distinct from its adapter maintainer, and record objections. An unresolved material objection blocks an interface-sufficiency conclusion. Label self-declared materiality and simulated independence explicitly. Test at the handoff/aggregation boundaries as well as end to end; a declaration by the producer is not independent evidence of its truth. These are test-review conditions, not new runtime EHD fields or certification requirements.

Version the charter, EHD semantics, profile, adapter, source and fixture independently. Changes to field meaning require an explicit compatibility assessment and, when breaking, a new profile/adapter version; prior results retain the exact versions tested. Unknown extensions must not be silently reinterpreted as established qualification.

The first D5 package should include:

- a comparison case with no decision-material change;
- paired cases with the same local result but different support for the receiving decision;
- a source-dependence / false-corroboration boundary;
- a targeted-requalification branch;
- an independent producer/consumer interoperability route where feasible; and
- explicit observations that would contradict the claim being tested.

Where a comparative EA claim is made, a **strong native/control configuration should be allowed to reproduce the same behaviour**. If it does so at equal or lower burden, that result counts against an EA differential claim.

A two-domain or deterministic pass establishes only the bounded property actually tested. It must not be reported as proof of ecosystem behaviour. Stronger ecosystem-level evidence requires later composition across multiple independently governed participants/observers with partial, conflicting or source-dependent observations.

### Delivery sequence and acceptance evidence

The proposed sequence is source-owner review of the case and its meaning, a frozen versioned mapping, behavioral execution with traces, comparative testing of EA's contribution, and a separately admitted federated extension. Technical checks, preparer review, contributor review and admission remain distinct. Each stage supports only the property actually tested; later campaigns require explicit resources and contributor agreement.

[Annex D](#annex-d-reference-cases-and-delivery-detail) retains the detailed sequence and evidence gates, the authority-applicability case from Use Case #6, Use Case #4's initial testbed stages, Nelson's package and Olena's review conditions. Those case constraints and acceptance conditions remain applicable when the corresponding profile or claim is used. In particular, approval does not expand authority, copied outcome labels do not establish executed behavior, and source revisions create no automatic maintenance obligation.

D1–D5 are proposed work outputs, not five mandatory repositories or already commissioned ITU deliverables. Their form as reports, specifications or informative test packages, editors, schedule, licensing and release gates require agreement. The charter may be reviewed before behavioral testing is complete; stronger technical claims must wait for the corresponding evidence.

## Related Work

The work should coordinate with, rather than reproduce, relevant standards and practices, including where applicable:

- FG-TIDA Themes and Use Cases, especially originating Theme #13 and UC #4;
- the 2026 Singapore Consensus on Global AI Safety Research Priorities and its Agentic Risk Management companion work referenced by Theme #13;
- AI-agent observability work, including OpenTelemetry agent-observability practice;
- decentralized identifier/naming work relevant to meaningful and verifiable agent identifiers, including the IETF DINRG material cited in Theme #13;
- IETF RATS/EAT/AR4SI and related identity/workload assurance work;
- STIX/TAXII and incident-exchange practice;
- policy/enforcement mechanisms such as XACML/OpenC2 where relevant;
- NIST AI RMF and related AI assurance/TEVV work;
- provenance and distributed-observability work;
- agent-interoperability substrates such as A2A; and
- relevant ISO/IEC, IEEE and privacy/security standards.

A formal duplication review should be maintained before any specification is proposed for stronger status. Related standards above are coordination candidates, not claimed implemented integrations.

The public FG-TIDA Terms of Reference provide the institutional fit: terminology (3.1), use-case/requirements analysis (4.1), architecture and interoperability (4.2), trust/lifecycle management (4.3), machine-readable metadata (4.4) and evaluation guidance (4.5). The incident/signal lifecycle is one bounded contribution to that remit, not the whole trust lifecycle. This scope alignment does not establish approval, novelty or absence of duplication.

Process sources: [FG-TIDA charter template](https://github.com/FG-TIDA/themes/blob/main/CHARTER-TEMPLATE.md), [Theme development process](https://github.com/FG-TIDA/themes/blob/main/README.md) and [Terms of Reference](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx). A charter is proposed by Pull Request after theme discussion; organizational structuring and deliverable approval remain governed by FG-TIDA.

## Related Themes

The initial **working boundaries** are strongest for:

- **Theme #13 — Ecosystem-level Agent Defense:** originating Theme and owner of the broader ecosystem-defense problem space; the first-cycle charter focuses its lifecycle/EA foundation without deleting the remaining identity, detection, reputation, privacy and incentive questions.
- **[Theme #4 — Access Control and Security Policy Enforcement with Metamorphing AI Agents](https://github.com/FG-TIDA/themes/issues/4):** agent representation and design traits, the identity–behavior mismatch, and their use in access policy. Together with principal binding under #14, these provide identity/accountability inputs. Theme #13 uses their attributed findings to assess actions and coordinate ecosystem defense; it does not define a replacement identity or access-control scheme.
- **Theme #5 — Provenance of Authority:** grant origin, scope, limits, standing/revocation/current applicability.
- **Theme #16 — Operational Human Oversight:** human authority/capacity/decision/execution/re-entry state.
- **Theme #6 — Intent / Policy Runtime Conformance:** source-native conformance/verdict semantics are public; the specific #6→EA adapter remains a candidate profile.
- **[Theme #21 — Reading evaluation at population scale](https://github.com/FG-TIDA/themes/issues/21):** establishes what a defined population of observations supports, including evaluator dependence, taxonomy, comparability and residual indeterminacy. EA assesses whether that finding, together with other relevant inputs, sufficiently supports a particular decision in context. It preserves the population finding without recomputing or relabeling it. This boundary concerns the question answered, not whether the receiver has authority. Theme #21 is distinct from **Use Case #21**, the controls-work/system-fails family used earlier in this charter.

The proposed #21 handoff preserves the population, observation period, taxonomy/policy version, evaluator characteristics, supported claim and residual limits. Per-evaluator findings remain distinguishable from pooled findings and their established, declared or unknown dependence assumptions. Following the [proposer's stated interface boundary](https://github.com/FG-TIDA/themes/issues/21#issuecomment-5903046577), EA may report insufficiency and name the gap; the current proposal does not send the receiver's target hypothesis, decision purpose or budget to direct the population measurement. Any further interface change requires review with that source owner.

The following boundaries are also explicitly carried from the originating issue and remain subject to alignment with the respective Themes:

- **[Theme #10 — Network-Native Governance and Trust Enforcement for Agentic AI](https://github.com/FG-TIDA/themes/issues/10):** the network/infrastructure governance and enforcement plane. This charter exchanges qualified signals and consumes enforcement outcomes; it does not define network-level enforcement or grant authority to that plane.
- **[Theme #12 — Agent Trust Mechanics](https://github.com/FG-TIDA/themes/issues/12):** trust mechanisms inside the agent, including credential handling, memory/context assurance and confidential computing. This charter addresses cross-party ecosystem qualification and defence; it does not redefine those internal mechanisms.
- **[Theme #14 — Agent-to-Principal Legal Binding](https://github.com/FG-TIDA/themes/issues/14):** a dependency for principal linkage and mandate/responsibility information. This charter consumes source-owned binding information through privacy-preserving, contestable interfaces; it does not establish legal binding or principal authority.

Useful **candidate supporting profiles** include:

- **Theme #7 — Verifier-side requirements:** evidence appraisal/failure semantics and negative vectors.
- **Theme #22 — Remote Attestation:** attested runtime/model/policy/interaction evidence where relevant; a common #22→EA profile is not yet established.

Other Themes may become profiles when a concrete use case requires them. The charter should not turn the complete ideal map into first-cycle scope.

The #5 boundary is particularly important: grant origination/provenance and current applicability are consumed, never inferred from a credential, a human approval or an EA qualification. #16 retains oversight semantics, effective institutional capacity, human decisions and their distinction from execution. #6 retains native conformance verdicts. #7/#22 evidence remains an attributed input, not a substitute for authority or systemic sufficiency.

Optional references to records/accountability (#1), operating-regime findings (#18), lifecycle privacy (#19) or privilege lifecycle (#23) require a concrete admitted profile and semantic-owner review. Mentioning them does not add those Themes' complete work to the first cycle.

## Open Questions

Reviewers are invited to focus on questions that remain genuinely unresolved.

### Architecture / packaging

1. **Institutional packaging:** one Theme #13-derived WG with separate peer deliverables/specifications, another document structure, or another FG-TIDA arrangement?
2. **Interoperability profile ownership:** should the general handoff abstraction become a reusable specification/profile beyond the #13 envelope, and who maintains it?
3. **Document split:** should Ecosystem Awareness Core and interoperability profiles be one document or separate deliverables?
4. **Profile admission:** which cross-Theme mappings have enough semantic-owner support to become normative rather than candidate/informative?
5. **Wire format:** should the first work remain semantic/transport-neutral or later include a reference schema?
6. **Conformance packaging:** informative annex/profile or separate test document?
7. **Evidence gate:** what executed evidence is needed before moving beyond early draft status?
8. **Editorial ownership:** who is prepared to edit/maintain each deliverable?
9. **Licensing/IP:** what terms should apply to specifications, fixtures and reference implementations?

### Theme #13 defense questions preserved from the originating Issue

10. **Privacy / surveillance boundary:** what minimum signal/provenance state is needed for meaningful blast-radius reduction without creating a surveillance architecture or unnecessary principal disclosure?
11. **Coordination versus authority:** how should the architecture make it impossible to confuse shared defensive coordination, reputation or corroboration with authority to constrain another participant?
12. **Containment authority:** who may authorize high-impact containment/kill-switch actions, on what evidence, and how is that authority itself bounded, contestable and auditable?
13. **Reputation / assurance:** what role, if any, should reputation play, how should source dependence/collusion be handled, and should reputation remain a separate Theme/profile rather than a lifecycle field?
14. **Detection without cooperation:** which behavioural/fingerprinting/detection outputs are legitimate ecosystem-defense inputs, and which mechanisms belong outside this charter?
15. **Incentives / alignment:** should incentives for trustworthy/cooperative behaviour remain a later Theme #13 deliverable, be consumed from another workstream, or be split out?
16. **Operator/decentralization model:** who operates shared infrastructure and what prevents the operator, trust anchor or dominant reporter from becoming a single point of control or failure?
17. **Agent privacy:** what privacy interests, if any, should be represented for agents themselves, separately from the privacy of principals/users?

### v0.2 decisions requiring focused review

18. **Oleksii decomposition:** confirm the EA-internal versus contextualization split, its independently testable boundary and the provisional mapping to the reference architecture's functional responsibilities (Annex B.1); do not appoint the whole matrix as a third serial layer.
19. **Decision context and reference-architecture boundary:** which supplied thresholds/cost relations are material to the first profile, and how are risk appetite, control sufficiency, posture selection and authorization kept with their owners?
20. **Evidence labels:** confirm the source worked-example version and the mapping aliases; distinguish test-calibration success from behavioral execution and independent interoperability.
21. **Revalidation contract:** specify material-change, expiry/review and targeted re-entry conditions, and how unchanged-state circulation and unbounded escalation are prevented.
22. **First differential protocol:** agree the independent/shared-lineage/late-evidence branches, fixed budget and consequence model, strong native comparator, available capabilities and stopping criterion.
23. **Current-state update:** record the 27–28 September contributions as a dated review proposal for the current-state interface bridge (document 05A in Annex B.3); reconcile obsolete case-availability statements without rewriting frozen sources or claiming FG adoption.

24. **Alignment with #10 and #12:** how should scope and boundaries be aligned with Network-Native Governance and Trust Enforcement and Agent Trust Mechanics? Carried from the originating issue; the Related Themes descriptions are proposed working boundaries, not agreements on behalf of those Themes.

For this preparation draft, **independent Incident Lifecycle and Ecosystem Awareness mechanisms are the current technical drafting baseline**. The exact wording, broader Theme #13 partitioning and institutional packaging remain reviewable through the FG-TIDA process.


---

## Contributor lineage and review status

The content is an editorial reconciliation for review, not a record of collective approval.

Ward's framing and the contributions of Nelson, Oleksii, Arpita and the Theme #16 contributors remain individually attributed. [Annex D.2](#d2-contributor-lineage-and-source-links) preserves the full attribution and source links; none implies collective approval.

**Next review:** contributor review of the technical boundaries and source interpretations, then Ward/process review of scope and packaging. Publication in a contributor repository, if requested, and submission of an official FG-TIDA Charter PR are separate actions. No message, submission, approval or maintainer appointment is implied by saving this draft.

---

## Annex A: Working vocabulary

### A.1 Assessment and exchange

These explanations make the draft readable before D1 establishes shared terminology. They do not adopt a contributor's vocabulary as a mandatory standard.

| Term | Meaning and reason for using it here |
|---|---|
| Epistemic / indeterminacy | “Epistemic” concerns what the evidence supports and the limits of that support. Indeterminacy is what cannot currently be established adequately for the stated decision; it is not automatically failure, falsity or prohibition. |
| Residual / inherited indeterminacy | Residual indeterminacy is what remains unresolved within the declared assessment and its limits. Inherited indeterminacy is unresolved qualification carried through a dependency on another result; local success must not silently erase it. |
| Semantic Window | The bounded selection of observations, meanings, scope and assumptions relevant to one decision. EA reviews this window as relevance, evidence freshness, capacity or context changes; it is not simply a time interval. |
| Epistemic opportunity | Additional decision-relevant knowledge that current capabilities could still obtain. Whether obtaining it is useful also depends on time, cost, capacity and consequences. |
| Semantic owner / source-native result | The contributor or function responsible for the meaning of a determination; the result as defined by that owner. A receiving component may qualify reliance on it but must not silently rewrite it or claim its authority. |
| Material qualifier / change | Information or a change that could alter justified reliance for the specified decision. Materiality is declared and reviewed for the case; it is not a universal numerical threshold. |
| Handoff, profile and adapter | A handoff carries a result with its qualifications across a component boundary. A profile specifies the agreed meaning and version for a particular use; an adapter maps an implementation's outputs to it while preserving their meaning. |
| Operational closure | The local process has reached an operational result, including a fallback (a defined alternative when normal determination is unavailable) or hold (a pause pending a stated condition) when necessary. This does not by itself establish the truth of the underlying claim, execution success or resolution of an ecosystem incident. |

### A.2 Information and test status

A bounded adapter preserves native meaning and the distinctions below. These are reading and mapping distinctions, not a mandatory shared enumeration; each profile must retain its source's meaning and record any translation.

| Label | Meaning to preserve |
|---|---|
| UNKNOWN | The relevant value or qualification is not known. Preserve the reason when available; do not infer it when absent. |
| NOT DECLARED | The source has not supplied the relevant statement. Absence of a declaration does not establish either its truth or its falsity. |
| NOT ESTABLISHED | The relevant claim or qualification has not been established by the available assessment/evidence. This is not evidence that its opposite holds; whether an assessment was attempted must remain explicit. |
| NOT APPLICABLE | A scoped determination that the field or requirement does not apply to this case. It is not a substitute for missing information. |
| NOT EXERCISED | The test did not perform or evaluate the behavior in question; it supports no conclusion about success or failure of that behavior. |

These labels concern different questions and may coexist across different fields. Missing information is not evidence of absence, and the reason for an unknown must not be invented.

### A.3 Testing vocabulary

| Term used in reference material | Meaning |
|---|---|
| Fixture | Fixed inputs, assumptions and expected outcomes for a reproducible check. |
| Test oracle | The attributed reference rule or expected result used to check an observed output. |
| Falsifier | A predeclared observation that would contradict the claim being tested. |
| Nominal-continuity control | A comparison case in which no decision-material condition changes, used to detect unnecessary pauses, escalation or containment. |
| HOLD | Pausing the affected operation pending a stated condition, under the legitimate control owner's rules. |
| Interface Conformance Record (ICR) | A reviewable record of the route, mappings, owners, evidence and unresolved objections supporting a claimed interface property. The acceptance conditions remain in D5. |

The main text uses ordinary descriptions where an implementation or reference identifier is not needed. These explanations do not create mandatory runtime states or a shared enumeration.

## Annex B: Reference architecture

This annex preserves the contributor-specific vocabulary for compatibility review. The main-text boundaries in Scope §2.3 apply to equivalent implementations as well.

### B.1 Mechanisms and functional responsibilities

The contributor reference architecture, **[Ecosystem Positioning (EP)](https://github.com/dakleyer/structural-awareness-contributions/tree/90cb592272f082aaa88b7798ef1c543f7e6c3343/architectural-contributions/ecosystem-positioning)**, brings together decision qualification, assessment of operating conditions and control sufficiency from one participant's perspective. It is introduced here to make compatibility and responsibility boundaries reviewable, not to require that implementations adopt the contributor's architecture.

- **Ecosystem Awareness (EA)** qualifies what can be relied on for one participant, one decision and one moment; what remains unresolved; what more current capabilities could establish; and what remains residual. It manages the Semantic Window introduced above.
- **Regime Awareness** checks whether the operating frame under which a position was qualified still holds and reports a bounded finding of change. It does not choose the participant's final operating posture, and EA does not replace this source mechanism.
- **[MSCA (Minimum Sufficient Control Architecture)](https://github.com/dakleyer/structural-awareness-contributions/blob/90cb592272f082aaa88b7798ef1c543f7e6c3343/standards/minimum-sufficient-control/00_CANONICAL_MSCA_ARCHITECTURE.md)** represents and assesses whether an authorized control configuration is sufficient for an **Objective Envelope**: the legitimate owner's declared outcomes, hard constraints and permitted trade-offs for a bounded process. Its five elements concern that objective envelope, operating environment, coordination, intervention mechanisms and enabling means. “Minimum” concerns the lowest justified burden among supported alternatives actually assessed; it is not a claim to the smallest configuration or a universal optimum.
- **MSCA Composition and Control** maintains **Ecosystem Cartography**: a participant-local map of relevant dependencies and processes, what is represented and supported, what can be explored further and what remains unknown. It does not presume a complete or shared global map.
- **MSCA Operation and Repositioning** compares a participant's bound role with the role it effectively plays and determines the supported posture: normal operation, containment/mitigation, or migration/regime transition. Candidate changes remain subject to participation rules, authority, capacity and useful response time. The **objective-conditioned Gradient** ranks candidate changes by their expected contribution to the declared objective, including reducing objective-related risk or shortfall; ranking is neither permission nor command.
- **ACC (Agentic Citizenship Contract)** records human- or institution-governed participation conditions: membership, admissible roles and objectives, obligations, prohibitions, revocation and exit. It is introduced to locate those constraints, not to create identity or authority. ACC/participation rules, objectives, policies, identity and authority remain with their legitimate semantic owners.
- **Lifecycle** retains signal/incident operation and response coordination. Actual enforcement, containment, isolation or recovery is performed only by an authorized control owner.

**F1–F9** identify the nine technology-neutral functional responsibilities in the contributor's [EA functional architecture, document 03](https://github.com/dakleyer/structural-awareness-contributions/blob/90cb592272f082aaa88b7798ef1c543f7e6c3343/research/ecosystem-awareness/baseline/03_FUNCTIONAL_ARCHITECTURE_v0.4.part01.md): qualifying the mission/decision, selecting the observation window, qualifying local results, qualifying external results, composing results, reassessing the operating frame and supported posture, targeting requalification, handing off bounded qualification, and learning from outcomes. These identifiers are traceability aids, not nine required services. The precise assignment of Oleksii's matrix to these responsibilities remains a reviewable hypothesis; no tenth function (“F10”) or new universal interface family is introduced.

The charter therefore commissions compatibility and bounded profiles, **not adoption of the entire Ecosystem Positioning, Regime Awareness, MSCA, ACC or Gradient corpus**. Equivalent independently implemented mechanisms are eligible when they preserve the agreed semantic boundaries.

### B.2 Four-component reference position

EA qualifies a receiving participant's decision under a declared scope and time. A qualified local closure does not establish a complete ecosystem state. The following descriptive names follow [00M §1 — canonical definitions](../../baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical); the letters are retained only for reference to the EA corpus.

| Component | Meaning for the specified process |
|---|---|
| **Result of active exploitation** (A) | What the process actually establishes and delivers through its current activity. The result may itself be an assessment, estimate or exploration finding. |
| **Established basis, limits and characterized exploitation reserve** (B) | What supports and bounds the delivered result, together with further work for which the relevant question, variables and evaluation method are already characterized. An assessable option remains in this reserve even when it is left unused. |
| **Exploration frontier** (C) | A grounded avenue that the process could begin to investigate, without an established basis for evaluating its extent, effort, feasibility, benefit or risk. A bounded first step may have a known budget while the wider frontier remains uncharacterized. |
| **Residual uncertainty beyond effective evaluation** (D) | Potentially material influences whose relevant effects the process has no effective route to evaluate under its current access, authority, method, capability and time. Related indicators may still be monitored without resolving those effects. |

Each component is relative to a producer, functional process, question, scope, capability and time. The same aspect can be an exploration frontier for one participant and a characterized reserve for another. That correspondence does not itself transfer evidence, access, authority or validity. If the grounds for assigning a role are not established, the role remains UNKNOWN.

**Exploitation, evaluation and exploration are functions, not alternative names for these components.** Exploitation uses established capabilities and a current frame to produce a result. Evaluation applies an established question, variables and method to an assessable aspect or option. Exploration investigates a grounded avenue to establish such a basis. A characterized reserve is not an activity, and a known evaluable option does not become an exploration frontier merely because it has not been used.

These are components of one qualified position, not mutually exclusive quadrants, four probabilities, mandatory transmission fields or the four-field Theme #13 envelope.

### B.3 Interface reference documents

The reference mapping maintains three separate levels: **document 04, general interfaces → document 05, proposed FG-TIDA cross-Theme mapping → document 05A, current-state conformance bridge**. These are contributor-repository document identifiers, not FG-TIDA specification numbers: 04 defines general handoff/interface semantics; 05 maps them to a proposed cross-Theme target; 05A compares that target with currently evidenced public contributions. Their explicitly versioned deltas record proposed changes separately. 04 semantics are not redefined by this charter; 05 expresses a proposed target, not present agreement; 05A records what public sources support at a stated date. Later contributions require an explicit dated review record, not silent alteration of frozen baselines.

## Annex C: Theme #13 envelope

The existing #13 **determinacy envelope** is a small set of qualifiers explaining how a local operational result was reached and what limitations must survive handoff. It is a **candidate versioned #13 profile**, preserving **Requirement 20 of [Use Case #4 (UC #4)](https://github.com/FG-TIDA/use-cases/issues/4)**, the proposed experimental environment for independently testable EA and Lifecycle components. That requirement retains the four fields below together with provenance, freshness, scope and dependency information.

| Field | Meaning in the originating #13 proposal | Distinction it preserves |
|---|---|---|
| `closure` | Whether the local result came from sufficient determination, a fallback, or a held state. | An operational output does not necessarily mean the underlying question was determined. |
| `determinacy_margin` | An ordinal indication—above, at or below—the producing subsystem's own declared determinacy boundary. | It is not a common numerical confidence scale or the general kernel's categorical determination state. |
| `capacity_binding` | Whether human-oversight capacity was not binding, was an active constraint, or was unavailable at decision time. | This consumes the oversight-capacity owner's assessment; it does not calculate institutional capacity. Other capacity dimensions require an explicit profile interpretation. |
| `inherited_indeterminacy` | Whether the decision materially relied on unresolved upstream closure, directly or through further dependencies, or whether that upstream state is unknown. | A locally determined result may still inherit indeterminacy. Unknown upstream state must not be reported as no inherited indeterminacy. |

These are explanations of the [originating proposal](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5554099339), not a newly frozen schema. The profile is not a replacement for the general kernel, not the four-component EA reference position in Annex B.2 and not a requirement that other Themes translate their native outputs into #13 states. Broader EHD standardization and ownership remain open.

## Annex D: Reference cases and delivery detail

The case assumptions, evidence gates and review conditions below remain applicable to the corresponding profiles and claims. Their placement here does not turn pending review into approval or remove an acceptance condition.

### D.1 Cases, sequence and acceptance evidence

The initial semantic reference is Arpita Sarker's **[Use Case #6 (UC #6)](https://github.com/FG-TIDA/use-cases/issues/6)**: an enterprise agent reads a fixed document set and returns a private summary to the same user. Its **G1** grant permits internal product planning and excludes sales-campaign preparation. The two branches keep the agent, grant, action, documents and recipient fixed: **Branch A** has the permitted product-planning purpose; **Branch B** has the excluded sales-campaign purpose. G1 still exists in B; it has not expired, been revoked or been rewritten.

The human reviewer's **H1** mandate allows review, hold, constraint, approval of continuation or escalation within its limits, but cannot amend G1 or create replacement authority. Both branches are considered before and after an authentic human approval, giving four reference conditions. Human-input authenticity and sufficient oversight capacity are fixed assumptions. Approval in B does not make the action authorized under G1. G1 and H1 are **UC #6-local identifiers**: H1 is not a hypothesis from the contributor repository's H1–H6 series, and these A/B branches are not EA's A/B/C/D components.

**UC #4 Stage 0** means a deterministic test harness using frozen fixtures and reproducible expected outcomes. **Stage 1** means a federated cross-Theme minimum across independently governed organizations. These are successive testbed stages, not levels of FG-TIDA approval; later sectoral or larger ecosystem campaigns require separate admission and resources.

| Stage | Intended output | Evidence gate and limit |
|---|---|---|
| Reference semantic review | UC #6 facts and four A/B before/after-approval conditions, mapped through the relevant #13/#16 contributions | Source-owner review of meanings, aliases and proposed synthetic metadata; not a new authority calculation |
| Frozen bounded mapping | Versioned adapter, declared capability/schema, sources, expected values and open-field register | Technical checks, preparer review, contributor review and admission recorded separately |
| Behavioral reference execution | Explicitly implemented transition/action simulator or independently implemented route, with traces and observed outcomes | Copying `revalidation_required` or `must_not_proceed_under_g1` is not evidence of revalidation or prevention |
| EA differential campaign | Independent versus shared-lineage corroboration; useful evidence obtainable versus too late/costly; nominal continuity control | Separate agreed protocol and fixed cost/consequence assumptions; strong native baseline can falsify the claimed benefit |
| Federated extension | UC #4 Stage 0/1 route and, subsequently, separately admitted multi-participant campaigns | Early passes support only their declared scope; later stages require explicit resources and contributor agreement |

The **28 September reference package** is Nelson Trasatti's [#13 mapping-review package](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5872258540), `UC4_UC6_Theme13_Mapping_Review_v0.4.0-r1.zip`, using experiment schema 1.1.0. It translates the four UC #6 reference conditions and Oleksii's annotations into reviewable field mappings, fixed test inputs, expected values, source references and explicit coverage limits. It is a review artifact, not Charter v0.2 or an implementation of EA. The earlier input package v1.1.1 used schema 1.0.0; those versions are different dimensions and must not be relabeled or migrated implicitly. The source worked example's v0.2 title versus v0.3 internal references remains a contributor-review issue.

UC #6 remains unchanged: the same G1 exists in both branches; only the declared purpose changes applicability; human approval under H1 does not expand G1. The fixture's before/after timestamps are synthetic ordering choices, not measured latency or a response window. The wider corroboration/cost investigation remains a separate experiment. Imported source revisions create no automatic obligation for the testbed maintainer to reimplement independently owned mechanisms.

The paired #16 mapping is reviewed against Olena Pavlenko's **Human Oversight Evidence-to-Decision Matrix (HO-EDM)**, an assessment structure linking the evidence available for human oversight to the decision that evidence can support, and her oversight-interface semantics. Her [public review](https://github.com/FG-TIDA/themes/issues/16#issuecomment-5872506565) checks the mapping's interpretation; it is not approval of the complete charter or validation of execution behavior. Before freezing that mapping, retain her clarifications: a general H1 review repertoire is not the branch-specific permitted intervention set; array order is not a semantic ranking; the recorded approval in B has no authorizing effect under G1; and `subject_to_other_controls` is not the complete return-to-operation condition. Attribute UC #6 facts, HO-EDM semantics, institutional authority/capacity semantics and adapter encodings separately to their respective contributors. Source: https://github.com/FG-TIDA/themes/issues/16#issuecomment-5872506565


### D.2 Contributor lineage and source links

- **Ward Duchamps:** Theme origin, lifecycle framing and independently testable EA/Lifecycle direction. Public anchors: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5508513343 and https://github.com/FG-TIDA/themes/issues/13#issuecomment-5571476256
- **Nelson Trasatti:** UC #4, bounded adapters, complete Lifecycle, targeted refinement, the #13 profile and experimental work. Anchors: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5639226397 and https://github.com/FG-TIDA/use-cases/issues/4#issuecomment-5846988611
- **Oleksii Voshchak:** matrix, worked example and revised decomposition; authority/capacity ownership, two clocks, structured state and event-driven revalidation. Anchors: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5783505043 and https://github.com/FG-TIDA/themes/issues/13#issuecomment-5818049343 and https://github.com/FG-TIDA/themes/issues/13#issuecomment-5854694913
- **Arpita Sarker:** UC #6 source facts and expected authority-applicability outcomes. https://github.com/FG-TIDA/use-cases/issues/6
- **Lei Gao, Olena Pavlenko and Olha Borysenko:** adjacent Theme #16 sequencing and bounded oversight contributions; the dossier records specific source anchors and preserves their ownership. This is not attributed approval of the full v0.2.
- **Iván Abril Palma:** EA/EP reference architecture, composition and interface discipline, v0.1 preparation baseline, synthesis and proposed comparative challenge. https://github.com/dakleyer/structural-awareness-contributions/tree/2db60a1fa4faa5ec08c6754cc676b8f70431c32a/architectural-contributions/ecosystem-positioning
