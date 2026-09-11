Ecosystem Awareness — Architecture Benchmark & Novelty Audit — v0.4

Peer-architecture completeness and differentiation review

&nbsp;

Status and question

This note audits the current Ecosystem Awareness architecture before use-case validation and architectural freeze.

Status boundary. This is an internal working architecture and research audit. It is not an ITU-T deliverable, not evidence of FG-TIDA adoption, and not proof of novelty, implementation superiority or competitive advantage.

&nbsp;

&nbsp;

It asks two separate questions:

1\. Completeness: do F1–F9 and O1–O6 / S1–S13 cover the functions and interfaces that a realistic agentic architecture requires, without creating unnecessary functions?

2\. Differentiation: does Ecosystem Awareness perform a coherent architectural function that is not already present as a first-class capability in current agent frameworks, interoperability protocols, security architectures or uncertainty-propagation research?

&nbsp;

Reading rule. This benchmark keeps three judgments separate: whether EA behavior is architecturally distinct, whether that distinction is already present in strong peers/prior art, and whether any remaining difference produces measurable value. Candidate differentiators remain A–G. APQ is tested as a consequence/application of the existing General Law and risk/capacity model, not as a new H item. If a strong peer reproduces the behavior, the EA differentiation claim shrinks. UC-EA-01…04 are architecture-validation profiles, not public FG-TIDA use-case submissions.

&nbsp;

The review deliberately avoids claiming mathematical or market novelty from the presence of familiar primitives. Most primitives are established. The candidate contribution is the way they are assembled into a scope-indexed epistemic requalification architecture.

&nbsp;

v0.2 added a conservative benchmark refinement: risk-based decision making, resource-bounded search, context budgeting, adaptive observation and value-of-information reasoning all have substantial prior art and must not be claimed as novel individually. v0.4 preserves that boundary and adds the validation-gated APQ benchmark surface. Source selection, routing, service discovery, QoS selection, trust/reputation scoring, cost-aware retrieval and value-of-information source acquisition are established techniques and are not EA novelty. The narrower APQ hypothesis is whether the existing EA scope/open-residual/non-fungibility model can select additional evidence for its marginal epistemic contribution to the currently unresolved domain while preserving pathway-property basis, source lineage, UNKNOWNs, resource burden and response horizon. APQ is treated as an application of the General Law plus risk/capacity-indexed requalification, not as a new novelty category.

&nbsp;

1\. Audit conclusion

Current result: provisionally complete and materially differentiated.

&nbsp;

No peer reviewed in this pass exposes a missing responsibility that requires an F10 or a new external interface beyond O1–O6 / S1–S13. The risk/sensitivity-capacity integration strengthens F1/F2/F6/F7/F9 and existing O1/O4/S6/S7/S12 interfaces rather than creating another function or plane.

&nbsp;

One completion adjustment was justified: O4 was broadened from Context, Memory, Retrieval & Research to Context, Memory, State, Retrieval & Research so that session/checkpoint/persistent state has an explicit producer interface for F9 Outcome Feedback & Revalidation. This is a refinement of an existing interface, not a new architectural responsibility.

&nbsp;

Everything else observed in peers maps cleanly into existing interfaces: sandbox/runtime isolation into O3/S3/S12; middleware/control hooks into S12; model/runtime versioning into O3/S3/S7; capability negotiation into O2/O6; session persistence into O4; traces/evaluation into S7; appraisal into S5; authority into S2; action records into S8; privacy/minimum disclosure into S10.

&nbsp;

Recommendation at this stage: do not add further functions or interfaces before use-case testing exposes a concrete uncovered responsibility.

&nbsp;

2\. Peer coverage — operational agent architectures

&nbsp;

A2A

Strong coverage: O2 Agent Discovery & Capability Description; O6 Task, Message, Artifact & Inter-Agent Transport; parts of S1 authentication/security.

A2A provides Agent Cards, capabilities/skills, interaction requirements, Tasks, Messages, Artifacts, context identifiers, status, streaming/push updates and protocol extensions while explicitly supporting opaque agent internals.

EA does not need to reproduce these capabilities. The Epistemic Handoff Descriptor / Epistemic Envelope can in principle ride beside ordinary results through an extension or equivalent transport.

Not found as first-class A2A semantics in the reviewed specification: source-window qualification, uncertainty type/scope, structural residual, inherited epistemic uncertainty, scope-indexed epistemic composition or systemic epistemic requalification.

&nbsp;

MCP

Strong coverage: O4 Context/Memory/State/Retrieval; O5 Tool/Resource Access & Action Execution; parts of O1/O6 capability negotiation and host coordination.

MCP explicitly separates host, clients and servers; servers expose focused tools/resources/prompts, clients maintain isolated server sessions, and the host controls orchestration/security boundaries. This strongly supports the EA design choice not to create one universal monolithic agent.

MCP also reinforces minimum disclosure: servers should not see the whole conversation or other servers by default.

Not found as first-class MCP semantics: an epistemic position over the selected context, why a context/window was judged sufficient, out-of-window residual, inherited uncertainty across server/tool results, or cross-domain epistemic composition.

&nbsp;

OpenAI Agents SDK

Strong coverage: O1 orchestration; O3 agents/models; O4 sessions/context; O5 tools; O6 handoffs; S6 HITL; S7 tracing; local guardrail/enforcement hooks.

The SDK deliberately uses few primitives and supports manager/handoff patterns, sessions, tools, guardrails, HITL and comprehensive traces.

Overlap with EA: orchestration feedback, local validation, persistent state, human intervention and tracing.

Not found as a first-class SDK function: persistent classification of what an agent knows/does not know by scope, qualification of external uncertainty signals, domain-indexed non-fungible epistemic composition, structural residual management or an interoperable epistemic envelope.

&nbsp;

LangGraph

Strong coverage: O1 orchestration/state graph; O4 persistence/checkpointing; S6 HITL interrupts; F7-like routing/interrupt mechanics; S7 observability through the broader LangSmith ecosystem.

LangGraph is intentionally a low-level orchestration/runtime framework. It provides durable execution, persistence, state, interrupts and human review but leaves application semantics to the developer.

Therefore EA functions could be implemented on top of LangGraph, but LangGraph itself does not supply the EA semantics.

&nbsp;

AutoGen

Strong coverage: O1 multi-agent teams/selection/workflows; O3 agents; O4 memory/RAG/state; O6 messages; S6 HITL; S7 tracing/observability; bounded termination mechanisms.

Important overlap with EA Type 1 controls: AutoGen explicitly recognizes that synchronous human input can block a team and recommends bounded/appropriate use, and provides maximum-turn/termination mechanisms.

Not found as a first-class AutoGen layer: window sufficiency, structural residual, external epistemic-signal qualification or scope-indexed composition of epistemic positions.

&nbsp;

Semantic Kernel / Microsoft Agent Framework

Strong coverage: O1 orchestration via sequential, concurrent, handoff, group-chat and magentic patterns; data transforms between agents; HITL in supported patterns; runtime coordination.

This reinforces the need for EA composition semantics because different orchestration patterns compose outputs differently, but no reviewed pattern establishes that complementary controls apply to the same epistemic domain or correct upstream epistemic collapse.

&nbsp;

Anthropic agent/context patterns

Strong overlap with F2: context is treated as finite, curated and dynamically retrieved; the objective is a minimal high-signal working context rather than maximal context. Agentic search progressively discloses context and sub-agents deliberately isolate detailed search context before returning compressed summaries.

This is close prior art for deliberate window selection and for the fact that compaction/summary can discard relevant state.

Difference: the guidance optimizes context for task performance. It does not establish a runtime architecture that preserves an explicit out-of-window residual, classifies Type 0/1/2, qualifies upstream epistemic emissions, or composes domain-indexed epistemic positions. The v0.2 EA hypothesis also ties context/window burden to mission-specific ecosystem sensitivity, consequence/reversibility and finite response capacity, while allowing the correct response to be either more or less observation.

&nbsp;

3\. Peer coverage — trust and security architectures

&nbsp;

RATS / RFC 9334

Strong coverage: S3 Remote Attestation; S5 Evidence Appraisal; clear producer/verifier/relying-party separation.

RATS is the strongest structural precedent for the EA rule that evidence should be consumed through a qualified result rather than by assuming that raw claims are truth. Evidence, reference values, endorsements and appraisal policy are processed by a Verifier, which produces Attestation Results for a Relying Party that applies its own policy.

Important architectural lesson retained in EA: producer claim \!= verifier result \!= relying-party decision.

Difference: RATS is deliberately scoped to attestation evidence. It does not provide a generic epistemic model for all agent decisions, local uncertainty, potentially knowable external state, structural residual, or cross-domain epistemic composition.

&nbsp;

OWASP Agent Control Standard and Agentic Security work

Strong coverage: S12 runtime enforcement/control hooks; S7 observability/instrumentation; security concerns across identity, memory, tools, human oversight and multi-agent interaction.

ACS explicitly targets inspectability, traceability, instrumentation and portable runtime safety-policy enforcement through middleware hooks.

EA should not duplicate that. F7 can emit a targeted requalification/control request; S12/ACS-like mechanisms remain responsible for interception and enforcement.

Difference: ACS answers where/how controls are hooked and enforced, not whether the epistemic basis feeding those controls is balanced, scope-correct or compositionally valid.

&nbsp;

NIST agent-security work

Current NIST activity strongly emphasizes agent identity, authorization, auditing/non-repudiation, prompt-injection mitigation and secure/interoperable agent ecosystems. These map into S1, S2, S7, S8 and S12 rather than requiring new EA functions.

The reviewed NIST material does not yet present a competing runtime epistemic-composition architecture equivalent to F1–F9.

&nbsp;

FG-TIDA emerging stack

The current repository gives the closest security/trust decomposition to our external interface model:

\- identity/principal binding;

\- provenance of authority/delegation;

\- remote attestation;

\- intent/policy and runtime conformance;

\- verifier/appraisal semantics;

\- accountability/action records;

\- operational human oversight;

\- population-level evaluation;

\- privacy/minimum disclosure;

\- ecosystem signal exchange/defence;

\- enforcement/containment and trust-framework context.

&nbsp;

This strongly validates interface completeness. EA fits as a transversal consumer/producer of scoped determinacy/capacity information without taking ownership of these functions.

&nbsp;

Current FG-TIDA positioning — \#13, \#5/\#9 and \#16

&nbsp;

Theme \#13 is the closest current ecosystem-level operational peer, but it addresses a different primary object. Its current direction is incident-signal exchange and defence: signal birth/distribution/amendment, corroboration, blast-radius representation, containment and resolution. Ecosystem Awareness should therefore treat \#13/S11 as a producer and consumer of qualified ecosystem signals, not as a theme to be duplicated or split merely to create an EA home.

&nbsp;

The strongest differentiation test is a non-incident case: all agents and subsystems may be honest and locally correct, while their composed epistemic positions remain globally fragmented or insufficiently qualified. Such a case can require EA even when \#13 has no malicious or incident condition to detect. Regime/context change is one important EA trigger, but EA is broader than regime observability: its core object is the qualification and composition of epistemic state and operating-frame validity across domains.

&nbsp;

Themes \#5 and \#9 define an upstream authority boundary rather than an EA responsibility. Provenance, standing and the existence or absence of a crisply authored grant should be supplied as qualified authority state; EA consumes that state and must not recreate the authority model. Theme \#16 similarly owns the human-oversight/intervention lifecycle and supplies effective human-capacity and decision state; EA consumes and composes those outputs without converting human approval into epistemic validation.

&nbsp;

This positioning is already consistent with the current public discussions: \#13 can develop its incident-signal/blast-radius architecture in parallel, while EA remains a cross-theme systemic-capacity/epistemic-composition hypothesis. The two should be compared on shared Case Study/Challenge surfaces rather than forced into premature convergence.

&nbsp;

4\. Peer coverage — uncertainty and epistemic research

&nbsp;

DebUnc

Direct overlap: communicates confidence/uncertainty between debating agents and changes downstream behavior based on that uncertainty.

What it demonstrates: uncertainty communication can materially improve multi-agent reasoning and miscalibrated confident outputs can mislead peers.

What it does not cover as a full architecture: source-window qualification, out-of-window residual, Type 0/1/2 taxonomy, non-fungibility across domains or general-purpose external interfaces.

&nbsp;

PropUQ-MAS

Closest technical peer identified.

Direct overlap: represents multi-agent execution as a communication graph and combines local uncertainty with uncertainty inherited from upstream messages. This is very close to F3/F5 and to inherited-indeterminacy preservation.

What remains different in EA: PropUQ-MAS is an uncertainty-quantification method for message-propagation reliability. EA is an architectural control model that also asks what window the uncertainty is conditional on, what lies outside that window, whether further determination is bounded, whether a structural residual remains, whether different domains are being improperly compensated, and what operating-frame requalification follows.

This peer materially reduces any novelty claim around “propagating uncertainty between agents.” EA must not claim that as new.

&nbsp;

MATU / multi-agent uncertainty quantification

MATU and related 2026 work explicitly quantify uncertainty across entire multi-agent trajectories and communication topologies rather than only final outputs. This further confirms that system-level UQ and interaction-aware uncertainty are active research areas.

EA differentiation therefore cannot be “multi-agent uncertainty exists” or “uncertainty should be propagated.”

&nbsp;

Runtime Bayesian MAS uncertainty monitoring

Recent work uses Bayesian networks to propagate calibrated uncertainty through a central multi-agent workflow. This overlaps with F3/F5/F6 at implementation-method level.

EA remains more general because it does not require one probabilistic model, one hub, or even numerical comparability across heterogeneous components.

&nbsp;

Architecting Trust in Artificial Epistemic Agents

This work explicitly treats AI systems as epistemic agents and calls for epistemic competence, falsifiability, provenance and socio-epistemic infrastructure.

This is conceptually adjacent to our epistemic-safety motivation and should be treated as neighboring prior art.

The reviewed work is a normative/governance framework, not a function/interface architecture equivalent to F1–F9 plus the EHD.

&nbsp;

5\. F1–F9 benchmark

&nbsp;

F1 Mission & Decision Context Qualification

Common antecedents: objectives, tasks, policies, risk/criticality and response constraints exist in essentially every agent/control architecture.

Differential element: F1 uses those inputs specifically to define how much epistemic determination and observation are sufficient by domain before window selection. v0.2 makes explicit that this qualification is indexed by ecosystem sensitivity/exposure, consequence severity, reversibility, tolerated residual, available observation/determination capacity and response horizon rather than by a universal risk score.

Assessment: familiar inputs, differentiated role.

&nbsp;

F2 Decision-Relevant Window Qualification & Management

Common antecedents: context engineering, retrieval, memory pruning, progressive disclosure and context budgeting are established.

Differential element: W(d,t) is not just context optimization; it carries an explicit boundary, selection basis, expandable outside state and structural residual, and is requalified against mission sensitivity/risk, observation/determination burden and response capacity. The architecture must support both widening when under-observation creates hidden exposure and narrowing/stopping when further awareness has become Type-1 resource consumption.

Assessment: strong partial prior art; architecture-level extension is potentially differentiated.