> **Controlled v0.4 release source.** Preserved for release provenance. The current reader successor is [01 — Integrated Foundational Theory v0.5](./01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md); use the successor for current reconciled semantics while retaining this source for the controlled v0.4 record.

nt for all materially relevant ecosystem conditions.”

“The complete materially relevant ecosystem cannot be fully enumerated, observed or kept current.”

&nbsp;

This is not simply a larger version of local uncertainty.

&nbsp;

Domain U asks:

How uncertain am I about the entities I have explicitly represented?

&nbsp;

Residual R asks:

What decision-relevant state may exist beyond the representation itself?

&nbsp;

## 4.3 Probability is not the residual

Suppose a subsystem reports q \= 0.85 based on its sample, evidence, model and explicitly represented dependencies in U.

&nbsp;

That can be a valid statement about U.

&nbsp;

It does not automatically mean 0.85 probability over Ω.

&nbsp;

R is not necessarily missing numerical probability mass. Parts of the open residual beyond the current bounded representation may be insufficiently specified even to support a defensible probability assignment.

&nbsp;

The error occurs when confidence conditional on U is silently promoted into confidence over Ω.

&nbsp;

## 4.4 Uncertainty management in the residual domain

Residual management does not require the impossible task of enumerating Ω completely.

&nbsp;

It requires explicit boundary awareness.

&nbsp;

A managed architecture distinguishes:

* what is represented in U;  
* what is measured versus assumed;  
* which dependencies are known but currently outside the active decision representation;  
* where extrapolation is being used;  
* which known unknowns remain;  
* where the state space is insufficiently specified for a probability claim;  
* how fresh the current representation is;  
* and what residual remains relevant after local operational closure.

&nbsp;

The central rule is:

&nbsp;

A bounded inference must remain bounded.

&nbsp;

A local conclusion may be operationally sufficient without becoming a claim that Ω has been determined.

&nbsp;

## 4.5 Failure Type 1 in the residual domain — epistemic paralysis

The system recognizes that Ω cannot be fully known and therefore concludes that no action can ever be justified.

&nbsp;

The search boundary keeps expanding:

new source

→ new dependency

→ new possible actor

→ new scenario

→ new uncertainty

→ no closure

&nbsp;

This is the residual-domain form of Failure Type 1\.

&nbsp;

The architecture confuses incomplete ecosystem knowledge with inability to act.

&nbsp;

## 4.6 Failure Type 2 in the residual domain — collapse Ω into U

The opposite failure is to treat the represented universe as if it were the complete relevant ecosystem.

&nbsp;

U is treated as Ω.

&nbsp;

The system effectively states:

&nbsp;

“If it is not in my represented universe, it is not decision-relevant.”

&nbsp;

This can produce:

* local-to-global confidence inflation;  
* unjustified generalization;  
* silent removal of unknown dependencies;  
* false claims of completeness;  
* and reuse of locally valid closure as globally valid truth.

&nbsp;

The numerical result inside U may be correct. Its scope has been enlarged without justification.

&nbsp;

**Residual-domain rule:**

**Operational sufficiency inside U must not be represented as exhaustive determination of Ω.**

&nbsp;

# 5\. One failure taxonomy across both uncertainty domains

The architecture therefore has two uncertainty domains, one structural Type 0 condition, and two fundamental management failure types.

&nbsp;

Failure Type 1 — keep the contradiction active without bounded closure.

In Domain U: wait indefinitely for a defined input, human, measurement, computation or answer.

In Residual R: keep expanding the ecosystem search because complete Ω cannot be established.

Systemic effect: paralysis, deadlock, unbounded escalation, excessive observation cost.

&nbsp;

Failure Type 2 — suppress one side of the contradiction and close falsely.

In Domain U: pretend the missing or insufficient defined input is adequately determined.

In the residual domain: pretend U is the whole relevant universe and ignore the open decision-relevant residual beyond the bounded representation.

Systemic effect: false certainty, confidence inflation, hidden exposure, fragile downstream decisions.

&nbsp;

Uncertainty management sits between these failures:

* acknowledge the contradiction;  
* bound the determination effort;  
* preserve the unresolved state;  
* and close operationally according to mission criticality and risk.  
* &nbsp;  
* Correct management therefore sits between two asymmetric resource/risk errors. Type 1 tends toward over-protection through excessive observation, verification, waiting or escalation; Type 2 tends toward overconfidence through under-observation, stale-frame reuse or suppression of residual exposure. The sound position is not a fixed midpoint. It is the dynamically requalified point at which the expected decision value of additional awareness no longer justifies its cost, given ecosystem sensitivity, consequence severity, reversibility, tolerated residual, available capacity and remaining response time.

&nbsp;

# 6\. Agentic amplification mechanism — compositional compression expands or obscures R

## 6.1 Why this is not a third uncertainty domain

An agent rarely observes the world directly. It consumes representations produced by other agents, humans, models, sensors, organisations, APIs, documents, summaries and services.

&nbsp;

This creates an additional architectural effect, but not a third uncertainty domain.

&nbsp;

Let upstream agent A operate on U\_A while retaining an open residual R\_A relative to that bounded representation.

&nbsp;

Let S\_A denote the richer state available to A: evidence coverage, confidence, unresolved dependencies, source provenance, freshness, human-capacity state and local assumptions.

&nbsp;

Let A export a message:

&nbsp;

m\_A \= g\_A(S\_A)

&nbsp;

If g\_A is lossy or many-to-one, materially different states can produce the same downstream message.

&nbsp;

The same PASS can represent:

* high-margin determination;  
* low-margin determination;  
* fallback because evidence was unavailable;  
* fallback because human input was unavailable;  
* a stale but still accepted state;  
* or a result containing inherited unresolved dependencies.

&nbsp;

If downstream agent B receives only PASS and incorporates it into U\_B as a determined fact, B’s local uncertainty may decrease while its hidden residual increases.

&nbsp;

The omitted elements of S\_A are not a new category of uncertainty. From B’s point of view they remain in the open residual beyond B’s bounded representation U\_B.

&nbsp;

**This is the compositional compression effect:**

**compression can make U look cleaner while making R larger, less visible or harder to reconstruct.**

&nbsp;

## 6.2 Source-selection example

Suppose seven primary sources are potentially relevant.

&nbsp;

The downstream architecture retrieves only one.

&nbsp;

The issue is not merely that “six sources are missing.” The architecture has made a selection that determines the effective U available for reasoning.

&nbsp;

The agent may reason perfectly over the one selected source. Yet the unrepresented perspectives, evidence, contradictions and dependencies associated with the other sources remain outside U.

&nbsp;

If an intermediary first consolidates seven sources into one summary and the downstream agent sees only that summary, the same effect occurs at a different boundary.

&nbsp;

Source restriction, ranking, summarization, access control, incentive structure and model mediation can therefore alter the boundary between U and R.

&nbsp;

## 6.3 Information-preservation anchor

This effect is consistent with the standard information-preservation problem already carried in the predecessor architecture.

&nbsp;

Under the usual Data Processing Inequality formulation, if X → Y → Z, processing cannot increase the information the downstream representation contains about the upstream variable: I(X;Z) ≤ I(X;Y).

&nbsp;

The architectural implication is narrow but strong:

&nbsp;

Once decision-relevant information has been discarded by a lossy transformation, further processing of that same representation cannot recreate the discarded information by itself.

&nbsp;

* Independent observations can add information.  
* Corroboration can add information.  
* Primary-source retrieval can add information.  
* A richer upstream message can preserve information.

&nbsp;

But repeating, rephrasing or recursively reusing the same compressed closure does not restore what was removed.

&nbsp;

## 6.4 Incentives and deliberate restriction

Compression is not always accidental.

&nbsp;

Participants may have legitimate or strategic reasons not to expose full state:

* privacy;  
* security;  
* intellectual property;  
* bandwidth and latency;  
* commercial competition;  
* organizational boundaries;  
* legal restrictions;  
* limited disclosure authority;  
* or adversarial incentives.

&nbsp;

Therefore the architecture should not assume that all participants will expose all relevant uncertainty even when signaling mechanisms exist.

&nbsp;

The objective is not maximum disclosure. It is sufficient preservation for the downstream decision.

&nbsp;

# 7\. Why agentic ecosystems intensify the residual problem

## 7.1 Ω becomes larger and more dynamic

In a relatively stable architecture, the ecosystem can often be approximated as changing more slowly than the system’s own decision cycle.

&nbsp;

A useful working heuristic from the predecessor architecture is:

&nbsp;

Traditional approximation:

T\_ecosystem \>\> T\_system

&nbsp;

Agentic condition:

T\_ecosystem ≈ T\_system

&nbsp;

and sometimes:

T\_ecosystem \< T\_system

&nbsp;

This is not a physical law. It expresses an architectural condition.

&nbsp;

Agents, models, tools, providers, delegations, memories, context sources, human reviewers and temporary interaction structures can appear, disappear, change authority or change behavior on timescales comparable to the system’s own control cycle.

&nbsp;

The consequence is structural:

* Ω expands;  
* the dependency graph changes;  
* the validity period of U becomes shorter;  
* and the open residual R\_U relative to the bounded representation can grow or change faster than the system can characterize it.

&nbsp;

## 7.2 More agents do not automatically mean more uncertainty

The important variable is not raw agent count.

&nbsp;

A highly distributed system can preserve context and uncertainty well.

A small system can lose information catastrophically if one compressed representation becomes authoritative for many critical downstream decisions.

&nbsp;

Residual risk grows particularly when:

* critical decisions depend on compressed upstream messages;  
* consumers lack primary-source access;  
* one representation becomes authoritative;  
* the same closure is recursively reused;  
* signals become stale faster than they are requalified;  
* source diversity is low;  
* or the ecosystem changes faster than dependency assumptions are refreshed.

&nbsp;

## 7.3 Recursive local correctness can still produce systemic indeterminacy

Several agents can each manage Domain-U uncertainty correctly and still compose into a globally difficult state.

&nbsp;

After a material ecosystem change:

* one group may correctly enter critical path A;  
* another may correctly enter incompatible critical path B;  
* another may correctly continue normal operation because its local conditions remain inside its validated U;  
* another may correctly remain HELD because required authority or determination capacity is unavailable.

&nbsp;

None of these local closures must be individually wrong.

&nbsp;

The systemic problem is that local correctness does not determine what the collection of those closures means under a changing, partially represented Ω.

&nbsp;

# 8\. Ecosystem Awareness

## 8.1 Problem statement

Ecosystem Awareness begins from the recognition that R is structural and, in agentic systems, can expand or change rapidly.

&nbsp;

It is not an attempt to know Ω completely.

&nbsp;

Working definition:

&nbsp;

**Ecosystem Awareness is a bounded assessment capability that determines whether the human, agentic and environmental dependencies required for the current mission remain sufficiently determined, capable and current to justify the present operating mode, while preserving relevant residual indeterminacy where they do not.**

&nbsp;

**In v0.2, 'bounded' also means risk- and capacity-qualified. Ecosystem Awareness continuously relates the mission's sensitivity to ecosystem change and consequence of error to the observation/determination burden needed to maintain a sufficiently qualified frame. It seeks a minimum sufficient observation/control architecture for the current mission, not maximum knowledge of the ecosystem.**

&nbsp;

The function is bounded because no participant can observe and process the complete recursive ecosystem.

&nbsp;

The architectural objective is minimum sufficient awareness for the mission and criticality.

&nbsp;

## 8.2 What Ecosystem Awareness must preserve

A useful Ecosystem Awareness function should make visible, to the extent proportionate:

* the current boundary U;  
* the existence and relevance of residual R;  
* confidence qualified by the boundary on which it was produced;  
* source and provenance;  
* coverage;  
* freshness;  
* known unresolved dependencies;  
* inherited uncertainty from upstream agents;  
* human-capacity constraints;  
* and the degree to which downstream decisions depend on compressed representations.

&nbsp;

It does not need full internal-state sharing.

&nbsp;

## 8.3 Ecosystem signaling is mitigation, not resolution

Ecosystem signaling can preserve and distribute information that participants observe and are willing or able to expose.

&nbsp;

It can carry:

* confidence;  
* uncertainty;  
* provenance;  
* freshness;  
* affected scope;  
* human-capacity state;  
* inherited indeterminacy;  
* dependency relevance;  
* and divergent observations.

&nbsp;

This can mitigate architecture-induced expansion or concealment of R.

&nbsp;

It cannot:

* create information that no participant possesses;  
* guarantee that every relevant participant has been identified;  
* force independent, competing or adversarial participants to reveal information;  
* guarantee truthful, complete or timely signals;  
* recover information already destroyed by an unavailable upstream mapping;  
* or eliminate the open residual beyond the current bounded representation.

&nbsp;

Therefore signaling is principally preservational and coordinative, and may be defensive or adaptation-enabling: it can reduce local epistemic isolation by making qualified observations or traces from elsewhere available to a receiver, but it does not create authority, manufacture truth or remove the need for scope/source qualification.

&nbsp;

Preservation does not mean informational irrelevance. A signal can make previously unavailable evidence available to a receiver and thereby support requalification or adaptation; the constraint is that this contribution remains source-attributed, scope-bound and epistemically qualified rather than being treated as knowledge created by communication itself.

&nbsp;

It is a mitigation mechanism against avoidable information loss. It is not a mechanism for eliminating the structural residual.

&nbsp;

## 8.4 Current working gap hypothesis

The predecessor review identifies many neighboring mechanisms: observability, uncertainty quantification, provenance, supply-chain visibility, trust relationships, multi-agent uncertainty communication, signaling and resilience.

&nbsp;

The current working hypothesis is narrower:

&nbsp;

there is not yet a clearly established architectural mechanism in the reviewed corpus whose primary object is continuous qualification of the boundary between U and a rapidly changing Ω, while explicitly retaining R as an operationally relevant state.

&nbsp;

This should remain a research-gap hypothesis, not an assertion that no such mechanism exists anywhere.

&nbsp;

# 9\. Operational closure and ecosystem posture

Two outputs must remain conceptually separate:

&nbsp;

Operational closure — what the subsystem decides to do now.

Epistemic determination — what the subsystem has actually established.

&nbsp;

A system can close operationally and still retain unresolved Domain-U uncertainty and residual R.

&nbsp;

At ecosystem level, three top-level postures from the predecessor architecture remain useful:

&nbsp;

Normal — residual and systemic uncertainty remain within known and validated operating parameters.

&nbsp;

Containment — ecosystem conditions have moved beyond normal parameters, but exposure, autonomy or scope can be reduced while maintaining a known workable frame.

&nbsp;

Migration / Regime Transition — the system can no longer rely on enough historical information or known parameters to characterize where the ecosystem is moving, and must prepare for a newly qualified operating frame or critical bifurcation.

&nbsp;

These postures are not additional uncertainty domains. They are operating-frame assessments that consume boundary, capacity, determinacy and residual-state information.

&nbsp;

# 10\. Architectural principles

Principle 1 — Defined does not mean determined.

An entity can be fully represented inside U and still be epistemically unresolved.

&nbsp;

Principle 2 — Unrepresented does not mean irrelevant.

Absence from U is not evidence that a dependency does not exist in Ω.

&nbsp;

Principle 3 — Unknown is not none.

Absence of transmitted residual information must not be interpreted as evidence that no residual exists.

&nbsp;

Principle 4 — Local correctness is conditional.

A valid determination inside U must retain the boundary on which it is valid.

&nbsp;

Principle 5 — Operational closure is not epistemic certainty.

The 