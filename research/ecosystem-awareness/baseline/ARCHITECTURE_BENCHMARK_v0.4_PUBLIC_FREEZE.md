# Ecosystem Awareness — Architecture Benchmark & Novelty Audit

**Version:** v0.4 — public reference freeze, 11 September 2026  
**Status:** provisional architecture benchmark and differentiation audit  
**Boundary:** internal research audit preserved publicly for traceability; **not** an ITU-T deliverable, proof of novelty, implementation superiority or competitive advantage.

## 1. Audit question

The benchmark asks two distinct questions:

1. **Completeness:** does the current Ecosystem Awareness functional/interface architecture cover the responsibilities required by a realistic agentic system without inventing unnecessary functions?
2. **Differentiation:** does the architecture perform a coherent function that is not already present as a first-class capability in current agent frameworks, interoperability protocols, security architectures or uncertainty-propagation research?

The benchmark intentionally separates:

- architectural distinctiveness;
- prior-art / peer overlap; and
- measurable value.

The presence of familiar primitives does not establish novelty.

## 2. Current conclusion

**Current result: provisionally complete and materially differentiated.**

No peer reviewed in this pass exposed a missing responsibility requiring a new generic core function beyond the current functional set. The recommendation at this stage is to avoid adding new core functions or interfaces until use-case testing exposes a concrete uncovered responsibility.

This is a **novelty hypothesis, not a novelty proof**.

## 3. Strong peer coverage already exists

The architecture explicitly recognises strong existing work in the following areas.

### Agent architectures and interoperability

- **A2A** — agent discovery, capability description, tasks, messages, artifacts and transport.
- **Model Context Protocol (MCP)** — context/resource/tool access and host/server security boundaries.
- **OpenAI Agents SDK** — orchestration, tools, handoffs, sessions, guardrails, HITL and tracing.
- **LangGraph** — durable execution, state, checkpointing, interrupts and human review.
- **AutoGen** — multi-agent workflows, messages, human input, termination and observability.
- **Semantic Kernel / Microsoft Agent Framework** — multiple orchestration patterns and runtime coordination.
- **Anthropic context/agent patterns** — context as a finite resource, progressive disclosure and compact task-relevant context.

### Trust, attestation and runtime controls

- **RATS / RFC 9334** — producer / verifier / relying-party separation and attestation-result semantics.
- **OWASP Agent Control Standard and agentic security work** — runtime control hooks, instrumentation and policy enforcement.
- **NIST agent-security work** — identity, authorization, auditing, secure/interoperable agent ecosystems and related security controls.
- **FG-TIDA emerging trust stack** — identity, authority/delegation, attestation, conformance, appraisal, accountability, human oversight, population evaluation, privacy, ecosystem signals and enforcement.

### Uncertainty and epistemic research

- **DebUnc** — explicit confidence/uncertainty communication between agents.
- **PropUQ-MAS** — communication-graph uncertainty propagation and inherited uncertainty.
- **MATU and related work** — uncertainty across multi-agent trajectories and interaction topologies.
- **Runtime Bayesian MAS uncertainty monitoring** — calibrated uncertainty propagation through multi-agent workflows.
- **Artificial epistemic-agent / trust research** — provenance, falsifiability and socio-epistemic infrastructure.

The benchmark therefore rejects broad novelty claims such as “multi-agent uncertainty is new”, “uncertainty should be propagated”, “context should be bounded”, or “human oversight is part of integrity”.

## 4. Candidate differential combination

The current architecture preserves seven candidate differentiators as a **combined runtime functional/interface architecture**.

### A. Four-position epistemic state by domain

The architecture distinguishes:

1. sufficiently determined in-window state;
2. defined in-window indeterminacy;
3. recognised potentially knowable out-of-window state; and
4. structural residual whose exhaustive elimination cannot be presumed.

### B. Twelve epistemic control surfaces

The Type 0/1/2 logic is applied both to locally produced epistemic state and to externally received claims. Correct local uncertainty handling is not presumed to survive composition automatically.

### C. General Law of Epistemic Composition

Epistemic positions are **scope-bound and non-fungible**.

Confidence or caution in one domain does not compensate for unresolved uncertainty or false certainty in another domain unless the dependency is materially established.

This blocks false “global balance” produced by averaging complementary epistemic biases.

### D. Agentic epistemic decoupling

Role-specialized agents can remain functionally coherent while maintaining incompatible epistemic postures across domains. Local correctness can therefore coexist with stable global epistemic fragmentation.

### E. Risk/capacity-indexed double-loop requalification

The system first qualifies the decision-relevant window from mission sensitivity, consequence, reversibility, tolerated residual, finite capacity and response horizon. It then re-evaluates local/external epistemic emissions and can re-enter window qualification when:

- the frame loses validity;
- ecosystem sensitivity changes;
- new evidence becomes materially valuable; or
- awareness effort becomes disproportionately expensive.

The correct response may be **more** observation or **less** observation.

### F. Orthogonal epistemic condition and operating posture

Type 0/1/2 are not equivalent to Normal / Containment / Migration states.

Correctly represented residual uncertainty can coexist with Normal operation. Conversely, Type 1/2 can trigger targeted correction without automatically implying system-wide migration.

### G. Transport-neutral epistemic handoff

The architecture does not require a shared internal reasoning model or common uncertainty algorithm. It requires sufficient preservation of:

- proposition / determination;
- scope;
- window qualification;
- uncertainty semantics;
- inherited indeterminacy;
- residual state;
- relevant dependency; and
- capacity/response constraints.

The purpose is to prevent downstream epistemic collapse while remaining transport-neutral.

## 5. Important non-novel elements

The benchmark does **not** support claiming that any of the following is new by itself:

- uncertainty quantification;
- uncertainty propagation;
- confidence signalling;
- context engineering;
- resource-bounded search;
- adaptive observation;
- value-of-information source acquisition;
- source selection, routing or service discovery;
- human oversight;
- provenance;
- attestation;
- observability;
- multi-agent orchestration;
- containment; or
- epistemic-agent framing.

Any public differentiation claim must remain at the **composition and architectural-role** level unless later empirical evidence supports something stronger.

## 6. Functional benchmark summary

The current functional architecture tests the following responsibilities:

- mission and decision-context qualification;
- decision-relevant window qualification and management;
- local epistemic-state qualification;
- external epistemic-signal qualification;
- scope-indexed epistemic composition and coupling assessment;
- systemic epistemic and operating-frame assessment;
- targeted requalification and corrective-directive generation;
- epistemic statement / envelope generation; and
- outcome feedback and selective revalidation.

The distinctive test is not whether peer architectures can perform retrieval, HITL, guardrails, tracing, attestation or UQ. They often can.

The question is whether a peer composition can preserve and requalify **epistemic position by domain** — including window sufficiency, external epistemic claims, structural residual and non-fungible composition — without adding an equivalent architectural layer.

## 7. Current peer comparison implications

### A2A

A2A provides excellent transport, discovery and interaction primitives. Ecosystem Awareness should ride beside these mechanisms, not reproduce them.

The benchmark did not find first-class semantics for source-window qualification, structural residual, inherited epistemic uncertainty or systemic epistemic requalification.

### MCP

MCP strongly supports bounded context/resource boundaries and minimum disclosure. It does not itself define whether the selected context is epistemically sufficient, what residual remains outside it or how epistemic state composes across independent domains.

### Agent SDKs and orchestration frameworks

OpenAI Agents SDK, LangGraph, AutoGen and Semantic Kernel provide many mechanisms Ecosystem Awareness would use: tools, state, handoffs, guardrails, HITL, routing, interruption and tracing.

The benchmark treats these as **implementation substrate**, not competitors to be replaced.

### RATS

RATS supplies a strong structural precedent: producer claim ≠ verifier result ≠ relying-party decision. Ecosystem Awareness generalizes a similar qualification discipline beyond attestation evidence into wider epistemic composition.

### Uncertainty-propagation research

DebUnc, PropUQ-MAS, MATU and related work materially narrow any claim around “communicating uncertainty”. Ecosystem Awareness must demonstrate value in scope/window qualification, residual management, non-fungibility, bounded determination and operating-frame requalification rather than merely uncertainty transmission.

## 8. FG-TIDA positioning boundary

The architecture is designed to consume and return qualified state across neighbouring functions without taking ownership of those functions.

Examples:

- identity / principal binding remains an identity function;
- authority / delegation provenance remains an authority function;
- local conformance/appraisal remains a local verdict function;
- operational human oversight remains a human-oversight function;
- ecosystem incident signalling remains a signal lifecycle;
- enforcement / containment remains an enforcement function.

Ecosystem Awareness sits across these boundaries to qualify system-level determinacy, capacity, residual state and operating-frame validity.

Public Theme #13 discussion currently provides the closest ecosystem-level home for this contributor work, but this is **pre-standardization positioning**, not formal adoption.

## 9. Validation sequence

The benchmark recommends a small number of adversarial/diagnostic validation profiles rather than one use case per control.

The current family includes four architecture-validation profiles:

1. **UC-EA-01 — Action-time operating-frame requalification under context change**
2. **UC-EA-02 — Bounded determination under incomplete, conflicting or partially scoped evidence**
3. **UC-EA-03 — Human oversight under bounded effective capacity and non-curative approval**
4. **UC-EA-04 — Scope-indexed composition of locally valid determinations**

The profiles should test the architecture against plausible peer compositions using conventional orchestration, UQ, HITL, guardrails, provenance and containment.

The architecture should change only if a validation case exposes:

- an uncovered responsibility;
- an unnecessary function;
- a peer mechanism that reproduces the claimed behavior; or
- evidence that the proposed risk/resource adaptation does not improve the relevant operating frontier.

## 10. Comparison protocol

Every validation case should document both similarity and difference:

- peer baseline architecture;
- functions/mechanisms shared by both;
- shared interfaces/artifacts;
- peer strengths reused rather than replaced;
- added Ecosystem Awareness behavior being tested;
- EA responsibilities absent as first-class peer functions;
- peer responsibilities intentionally outside EA ownership;
- whether the peer can reproduce the same behavior without an EA-equivalent layer;
- observed outcome under the same frozen facts;
- ecosystem sensitivity and consequence assumptions;
- observation/determination budget;
- actual awareness-resource consumption; and
- whether more observation materially changed the decision or merely consumed capacity.

## 11. Freeze recommendation

The architecture should be treated as **provisionally frozen for validation**, not as a final standard or completed implementation.

The public freeze in this repository serves a different purpose: it fixes a traceable reference point so that later changes can be compared against a dated corpus rather than silently rewriting the earlier architecture.

## 12. Claim discipline

A positive validation result is not “the peer lacks HITL, retrieval, provenance, attestation, UQ, guardrails, observability or containment.” Those mechanisms are expected to exist.

A positive result would instead show that the combined Ecosystem Awareness semantics add useful behavior that plausible peer compositions do not reproduce without adding an equivalent epistemic layer.

Until such evidence exists, public claims should remain phrased as **candidate**, **designed to**, **can**, **working hypothesis** or **provisional architecture** rather than validated superiority.
