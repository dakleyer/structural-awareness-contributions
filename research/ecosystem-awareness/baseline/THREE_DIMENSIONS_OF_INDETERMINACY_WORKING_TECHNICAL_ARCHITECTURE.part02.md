Let S\_j denote the richer information state available to upstream subsystem j.

Let m\_j \= g\_j(S\_j) denote the message or closure state passed downstream.

&nbsp;

Where g\_j is many-to-one, materially different upstream states can map to the same m\_j.

&nbsp;

For example, the same PASS may originate from:

\- high-margin determination;

\- low-margin determination;

\- fallback because evidence was unavailable;

\- fallback because human capacity was unavailable; or

\- a result containing inherited unresolved dependencies.

&nbsp;

If only PASS crosses the boundary, those distinctions can become unrecoverable downstream.

&nbsp;

## 5.2 Information-theoretic anchor

&nbsp;

This is not a new theorem. It is a standard information-preservation problem applied to agentic architecture.

&nbsp;

The Data Processing Inequality states, under the usual Markov-chain formulation, that processing a representation cannot increase the information it contains about an upstream variable: if X → Y → Z, then I(X;Z) ≤ I(X;Y).

&nbsp;

For this architecture, the important implication is limited but strong: once decision-relevant information has been discarded by a lossy transformation, downstream processing of that same representation cannot recreate the discarded information by itself.

&nbsp;

New independent observations can add information. Corroboration can add information. Better source access can add information. But repeating, rephrasing or propagating a compressed closure state does not recover what the upstream boundary already removed.

&nbsp;

## 5.3 The critical risk variable is dependence on compressed information

&nbsp;

The important variable is not the raw number of agents.

&nbsp;

The more precise architectural question is:

&nbsp;

How many downstream decisions depend materially on a compressed representation, how critical are those decisions, and to what extent is that representation their sole or authoritative source?

&nbsp;

Information-loss risk grows when:

\- a message strongly compresses a richer upstream state;

\- many critical downstream agents or organisations depend on it;

\- those consumers lack primary evidence or independent sources;

\- the same compressed result is recursively reused as evidence;

\- the representation becomes stale relative to a changing ecosystem; or

\- compression removed exactly the context needed to assess the downstream property.

&nbsp;

A highly distributed system can preserve information well. A small system can lose information catastrophically if one lossy representation becomes the authoritative source for many critical downstream decisions.

&nbsp;

## 5.4 Failure mode 3A — closure laundering through composition

&nbsp;

Agent A has evidence coverage, confidence, unresolved dependencies and an unavailable human input, but exports only PASS.

&nbsp;

Agent B consumes PASS as authoritative evidence and exports PASS.

&nbsp;

Agent C consumes B’s PASS and exports PASS.

&nbsp;

The system reports PASS.

&nbsp;

The original indeterminacy has not been resolved; it has become invisible.

&nbsp;

The core composition rule is:

&nbsp;

unknown ≠ none.

&nbsp;

Absence of transmitted residual information must not be interpreted as evidence that no residual exists.

&nbsp;

## 5.5 Failure mode 3B — signaling as a false cure

&nbsp;

Ecosystem signaling is valuable, but it is not an omniscience mechanism.

&nbsp;

Signaling can preserve and distribute information that participants observe and are willing or able to expose. It can share confidence, uncertainty, provenance, freshness, affected scope, human-capacity state, inherited indeterminacy and divergent observations.

&nbsp;

It cannot:

\- create information that no participant possesses;

\- guarantee that every participant observes the relevant state;

\- force competitors, independent organisations, parasitic actors or attackers to reveal relevant information;

\- guarantee that signals are truthful, complete, timely or non-adversarial; or

\- recover information already destroyed by an upstream lossy mapping unless a richer source is still reachable.

&nbsp;

Its value is therefore principally preservational, defensive and coordinative.

&nbsp;

## 5.6 Correct management

&nbsp;

Correct Dimension-3 management preserves enough decision-relevant information across boundaries that downstream participants can distinguish compressed closure from the richer state behind it.

&nbsp;

Possible mechanisms include:

\- outcome plus residual determinacy state rather than outcome alone;

\- provenance and source identity;

\- scope, coverage and freshness;

\- dependency relevance;

\- confidence/uncertainty qualified by the observation boundary;

\- retrieval or inspection of primary evidence where appropriate;

\- independent corroboration instead of recursive reuse of one source; and

\- a bounded Semantic Window containing the minimum context needed by the downstream decision.

&nbsp;

The objective is not maximum disclosure. Full internal-state sharing may be impossible or undesirable because of privacy, security, intellectual property, bandwidth, latency and competition.

&nbsp;

The objective is sufficient preservation.

&nbsp;

# 6\. Why this matters more in agentic ecosystems

&nbsp;

## 6.1 Ecosystem dependency is old; continuous awareness is the change

&nbsp;

Systems engineering, cybersecurity and supply-chain risk management already address systems-of-systems, external dependencies, distributed participants and changing environments. NIST, for example, defines a cyber ecosystem as the aggregation and interaction of diverse participants, processes and cyber devices, and NIST SP 800-161 explicitly treats ICT/OT supply chains as complex, globally distributed and interconnected ecosystems where reduced visibility and understanding create risk. ITU-T X.1812 likewise models trust relationships, stakeholder roles and security boundaries across an ecosystem.

&nbsp;

The architectural claim here is therefore not “systems suddenly have ecosystems.”

&nbsp;

The change is timescale and operational coupling.

&nbsp;

A useful working heuristic from the current FG-TIDA discussion is:

&nbsp;

Traditional approximation:

T\_ecosystem \>\> T\_system

&nbsp;

Agentic condition:

T\_ecosystem ≈ T\_system

and sometimes

T\_ecosystem \< T\_system.

&nbsp;

This is not a physical law and should not be presented as one. It expresses an architectural condition: agents, models, tools, providers, delegations, memory/context sources, human reviewers and temporary interaction structures can appear, disappear or change on timescales comparable to the system’s own decision/control cycle.

&nbsp;

## 6.2 Why faster ecosystem change increases the importance of the three dimensions

&nbsp;

Under a fixed observation and determination budget, a faster-changing ecosystem can reduce the fraction and lifetime of relevant external state represented inside W\_i.

&nbsp;

Dimension 1 becomes harder because local evidence and human/dependency availability can change before determination completes.

&nbsp;

Dimension 2 becomes more important because Ω\_i \\ U\_i can become larger, less stable or less characterisable: more dependencies are outside the local view, previous samples age faster, and assumptions about the external population expire sooner.

&nbsp;

Dimension 3 becomes more dangerous because compressed representations can become stale or propagate at machine speed through many consumers before the underlying change is visible. A local closure that was reasonable at t0 may be reused at t1, t2 and t3 by downstream systems whose dependency context has already changed.

&nbsp;

The point is not that agentic systems necessarily contain more uncertainty in every case. The point is that rapid reconfiguration reduces the safety of assuming that yesterday’s external context, dependency graph or source authority remains valid throughout today’s decision cycle.

&nbsp;

This is why Ecosystem Awareness becomes operationally meaningful.

&nbsp;

# 7\. Ecosystem Awareness as bounded architecture, not omniscience

&nbsp;

The current FG-TIDA discussion has moved from the idea of a generic “remaining-indeterminacy handler” toward a more specific function.

&nbsp;

Working definition:

Ecosystem Awareness is a bounded assessment capability that determines whether the human, agentic and environmental dependencies required for the current mission remain sufficiently determined, capable and current to justify the present operating mode, while preserving relevant residual indeterminacy where they do not.

&nbsp;

The function is bounded because no participant can observe and process the complete recursive ecosystem.

&nbsp;

More awareness is not automatically better. A creative brainstorming agent, a personal assistant and an agent reconciling cross-border financial transactions do not require the same observation, verification and signalling budget.

&nbsp;

The architectural objective is minimum sufficient awareness for the mission and criticality.

&nbsp;

That turns Ecosystem Awareness into an optimization problem:

&nbsp;

mission sensitivity to ecosystem change

↔ observation / verification / communication cost

↔ residual indeterminacy tolerated

↔ response capacity available.

&nbsp;

# 8\. Relationship between the three dimensions and Ecosystem Awareness

&nbsp;

Dimension 1 asks:

Within what I can currently see and compute, what can I determine?

&nbsp;

Dimension 2 asks:

What decision-relevant state remains beyond what I can currently see, model or measure?

&nbsp;

Dimension 3 asks:

What decision-relevant state may have been removed or distorted before it reached me, and how much do I depend on that representation?

&nbsp;

They interact.

&nbsp;

A Dimension-3 loss upstream frequently appears to the downstream agent as Dimension-2 residual: relevant information exists somewhere, but it lies outside the downstream context window.

&nbsp;

A Dimension-1 fallback caused by unavailable human capacity can create Dimension-2 residual if the unanswered question remains relevant to the wider operating condition.

&nbsp;

A changing ecosystem can also invalidate or reduce the freshness of the information preserved through Dimension 3, thereby increasing Dimension 2 even if the communication protocol itself remains correct.

&nbsp;

Ecosystem Awareness does not eliminate these dimensions. It makes them legible enough to support a justified operating posture.

&nbsp;

# 9\. Operating postures and the second Ecosystem Awareness module

&nbsp;

The three dimensions above constitute the first foundational module:

&nbsp;

Module A — Indeterminacy and information-preservation awareness.

&nbsp;

The broader Ecosystem Awareness architecture also contains a second, distinct module:

&nbsp;

Module B — Ecosystem lifecycle / operating-frame awareness.

&nbsp;

Module B consumes capacity, determinacy, context and residual-state information to determine whether the ecosystem remains inside a known operating region.

&nbsp;

Three simple top-level postures remain useful:

&nbsp;

Normal — systemic uncertainty remains within known and validated operating parameters.

&nbsp;

Containment — ecosystem conditions have moved beyond normal parameters, but exposure/autonomy/scope can be reduced while maintaining a known workable frame.

&nbsp;

Migration / Regime Transition — the system can no longer rely on enough historical information or known parameters to characterize where the ecosystem is moving, and must prepare for a potential critical bifurcation or newly qualified operating frame.

&nbsp;

Module B should not be collapsed into the three indeterminacy dimensions. It is the operating-frame assessment that uses them.

&nbsp;

# 10\. Formal and neighbouring foundations

&nbsp;

## 10.1 Computability

&nbsp;

