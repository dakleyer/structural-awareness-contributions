ns above map naturally onto common agentic-system components without requiring any particular implementation topology.

&nbsp;

Planner / Orchestrator

Provides mission, task, criticality and dependency context to F1. Consumes F6 posture and F7 requalification directives. It remains responsible for ordinary workflow/orchestration decisions.

&nbsp;

Worker agents / Domain models / Tools

Produce operational results and local epistemic state for F3. They receive targeted re-evaluation or evidence requests from F7.

&nbsp;

RAG / Retrieval / Research / Discovery

Provides candidate evidence and context to F2/F3. It executes bounded context-expansion requests from F7. More retrieval is not assumed to be automatically better.

&nbsp;

Policy / Identity / Authority

Provides applicable constraints, authority provenance and validity information. It may receive refresh/requalification requests. Ecosystem Awareness consumes authority state; it does not create authority.

&nbsp;

Human Oversight

Provides human-capacity and decision state as one dependency input. It receives scoped review requests only where human intervention is relevant and reachable. Human approval is not treated as retroactive validation of the world model presented to the human.

&nbsp;

Observability / Monitoring / Evaluation

Provides drift, anomaly, freshness, performance and evidence signals. Ecosystem Awareness interprets their epistemic significance but does not replace the underlying measurement method.

&nbsp;

External Peers / Third Parties

Provide epistemic signals to F4 and may receive the bounded envelope from F8. Their internal methods can remain independently governed.

&nbsp;

Safety / Action Control / Containment

Consumes F6/F7 state and requests. It owns the mechanisms and authority that actually restrict, isolate, rate-limit, suspend or otherwise contain behaviour.

&nbsp;

Migration / Strategy / Reconfiguration

Consumes Migration/Regime-Transition assessment and prepares or executes transition to another qualified operating frame. Ecosystem Awareness determines the epistemic need for requalification; it need not own the migration mechanism.

&nbsp;

Signal Transport / Exchange

Carries external epistemic envelopes and incident/evidence signals. Signal lifecycle and transport remain separable from the Ecosystem Awareness assessment itself. Transport/signalling infrastructure owns the mechanism and its operational semantics. EA may qualify whether a particular available route is sufficient for a receiving decision, but does not certify the transport or signalling mechanism globally.

&nbsp;

# 6\. Coverage of the twelve epistemic control surfaces

The functional model must be complete against the already fixed twelve control surfaces.

&nbsp;

I0 — F3 identifies local determination limits; F6 assesses systemic consequence; F7 selects bounded response.

&nbsp;

I1 — F3 detects unbounded local determination; F7 imposes a bounded stop/requalification path.

&nbsp;

I2 — F3 detects false local certainty; F5 prevents that closure from being laundered through composition; F6 assesses material impact.

&nbsp;

O0 — F2 preserves structural residual; F3/F6 prevent it from disappearing during local or systemic assessment.

&nbsp;

O1 — F2 bounds window expansion; F7/F9 control when expansion continues, redirects or stops.

&nbsp;

O2 — F2 preserves the boundary of W(d); F5/F6 prevent the current window from becoming ecosystem truth.

&nbsp;

E0-I — F4 preserves whether the source's inability to determine is structural, incomplete or unknown; F5 retains that distinction.

&nbsp;

E1-I — F4 identifies bounded versus open-ended upstream uncertainty; F5/F7 prevent propagation of unbounded HOLD/search.

&nbsp;

E2-I — F4 identifies suppressed or unqualified upstream uncertainty; F5 prevents inheritance as false certainty.

&nbsp;

E0-O — F4 distinguishes in-window uncertainty from any claim about the source's structural residual; F5/F6 preserve unknown scope.

&nbsp;

E1-O — F4 identifies unbounded external search/unknown generation; F7 does not automatically reproduce it.

&nbsp;

E2-O — F4 preserves source window and scope; F5/F6 prevent a source-specific conclusion from becoming ecosystem truth.

&nbsp;

The General Law of Epistemic Composition is implemented primarily by F5 and enforced again by F6 and F7.

&nbsp;

# 7\. The three healthy operating postures

## Normal

The current qualified operating envelope remains valid for the mission. The system may contain Type 0 residual, explicit unknowns and bounded local uncertainty. Normal does not mean omniscient or uncertainty-free; it means that uncertainty is being managed correctly and the current response mapping remains sufficiently qualified.

&nbsp;

## Containment / Mitigation

The current epistemic state no longer supports unrestricted normal operation, but a known bounded response can preserve or restore a qualified frame. Typical effects may include reduced autonomy, reduced scope, temporary isolation of an input, targeted revalidation, increased observation or use of a known fallback. Ecosystem Awareness supplies the reason and target; the appropriate control function executes the action.

&nbsp;

## Migration / Regime Transition

The active mission has left, or can no longer establish, a sufficiently qualified response envelope. The correct mission-relevant response mapping is not yet sufficiently known or qualified. The system should preserve invariant safety actions where available while preparing or executing requalification into a new operating frame.

&nbsp;

These postures are outputs of correct epistemic management. Type 1 and Type 2 are not alternative postures; they are management faults that Ecosystem Awareness must make visible and attempt to requalify.

&nbsp;

# 8\. What Ecosystem Awareness explicitly does not own

Ecosystem Awareness does not require:

\- one universal uncertainty metric;

\- one mandatory window-selection algorithm;

\- one centralized ecosystem observer;

\- one global world model;

\- one consensus mechanism;

\- one mandatory signal transport;

\- disclosure of prompts, private memory or chain-of-thought;

\- ownership of policy or authority;

\- ownership of human intervention;

\- ownership of containment or enforcement;

\- ownership of migration execution;

\- proof that every system-level property is formally undecidable;

\- global ranking, scoring, certification or approval of acquisition/signalling mechanisms. EA may determine that a pathway is sufficient or insufficient for a particular decision scope and operating condition; that qualification is not a general certification of the mechanism.

&nbsp;

An implementation may centralize several functions or distribute them across agents and services. Conformance is functional: the architecture must preserve the required behaviours, distinctions and information properties, not a prescribed component topology.

&nbsp;

# 9\. Minimal end-to-end flow

1\. A planner supplies a mission, criticality, ecosystem-sensitivity/exposure context, constraints, finite observation/determination capacity and available response capability.

2\. F1 identifies the material decision domains, required determination level, sensitivity/consequence profile, tolerated residual and proportionate observation/determination burden.

3\. F2 establishes and continuously requalifies W(d,t) for each material domain, recording its boundaries, residual, selection basis and capacity/stop assumptions; where evidence must be acquired, F2.APQ also qualifies which available pathway or combination of pathways is sufficient for the current evidence need without treating pathway identity as evidence independence.

4\. Worker agents, humans, tools and external peers operate and emit results.

5\. F3 qualifies local certainty/uncertainty; F4 qualifies external epistemic signals.

6\. F5 composes those states by domain and dependency without cross-domain cancellation.

7\. F6 emits both an epistemic condition and an operating posture.

8\. F7 sends only the requalification directives relevant to the affected domain.

9\. F8 exposes a bounded internal statement and, where appropriate, an external epistemic envelope.

10\. F9 compares outcomes with assumptions and re-enters the appropriate point in either loop when material change occurs.

&nbsp;

The architectural objective is not to maximize caution, confidence, human review, search or agent diversity. It is to keep the system's epistemic position correctly classified and scope-bound while providing the rest of the architecture with enough information to operate, contain or migrate on a justified basis.

&nbsp;