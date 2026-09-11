change as ecosystem sensitivity, capacity and validity assumptions change.

E(d) \= \[A\_d, B\_d, C\_d, D\_d\]

&nbsp;

The agent’s ecosystem state is therefore not one balanced score but a map:

d → E(d)

&nbsp;

Epistemic balance is non-fungible across domains. A Type 2 certainty bias in domain d1 is not cancelled by Type 1 caution, additional search or explicit uncertainty in domain d2. Controls applied to different regions of the world can be individually correct while leaving multiple coupled epistemic imbalances in the composed decision.

&nbsp;

Example: a chain of agents may collapse uncertainty and emit overconfident conclusions about traffic state in region X, while another chain performs extensive retrieval and expresses high uncertainty about weather in region Y. Combining the outputs does not make the total decision epistemically balanced. The architecture remains overconfident about X and potentially over-searching or under-determined about Y.

&nbsp;

This creates a cross-domain compensation fallacy: treating uncertainty management performed somewhere in the decision space as compensation for epistemic error elsewhere. Ecosystem Awareness must instead preserve the epistemic position attached to the scope to which it applies.

&nbsp;

## Composition rule

&nbsp;

Before combining certainty, uncertainty or closure signals, the receiver should preserve or establish the domain/scope to which each signal applies. Signals with complementary epistemic stances are only complementary when they qualify the same or materially coupled decision domain. Otherwise they represent separate local positions, not a balanced whole.

&nbsp;

If the relevant scope is unknown, the receiver should not infer global balance. Unknown scope remains an epistemic qualifier of the received signal.

&nbsp;

## Architectural consequence

&nbsp;

Ecosystem Awareness should maintain a scope-indexed epistemic map rather than a single agent-level uncertainty or confidence posture. Systemic risk arises from the pattern of local imbalances and their coupling across decision-relevant domains, not from the average epistemic stance of the participating agents.

&nbsp;

Presentation projection rule. For display, alerting or routing, EA may expose a deliberately lossy, scope-bound projection such as Posture(D\_receiver) together with material qualifiers (for example response-capacity sufficiency, response-window state, frame recoverability and, where relevant, transition readiness). The projection must identify the receiving decision scope, must not be treated as a composition input or averaged back into E(d), and must not be represented as one global ecosystem posture. Where the receiver spans several domains, the projection rule and the domain(s) driving the presented posture must remain explicit; if no defensible projection exists, preserve the multi-domain state rather than fabricate a scalar or universal label.

&nbsp;

# Ecosystem composition principle — no cross-domain epistemic cancellation

&nbsp;

Epistemic controls are not additive safeguards that can be applied in unrelated parts of the decision space and then averaged into a globally safe posture. The epistemic qualification of each material domain must be preserved through composition.

&nbsp;

For decision-relevant domains d1, d2, …, dn, the system should preserve E(di) and the material couplings among domains. A Type 2 bias in d1 is not cancelled by Type 1 caution in d2; additional exploration in d3 does not repair false certainty in d1; human approval in d4 does not independently validate the upstream world model on which the human was asked to decide.

&nbsp;

The composition rule is therefore:

&nbsp;

Epistemic imbalance in one domain may be corrected only by controls that materially requalify that domain or a dependency that is demonstrably coupled to it. Controls applied to unrelated domains do not constitute compensation.

&nbsp;

This also means that agent diversity, agent count and computational effort are not sufficient evidence of epistemic diversity. Ten thousand agents assigned to different subspaces may provide very broad coverage while providing almost no independent second opinion on any one proposition. Sectioning increases coverage; it does not automatically create corroboration.

&nbsp;

# Worked example — 100 million tokens and compounded epistemic collapse in enterprise strategy

&nbsp;

Consider an enterprise strategy system that spends 100 million tokens across large numbers of specialized agents, management approvals, alternative-generation agents and market-risk agents. The system can execute many individually reasonable architectural patterns and still produce a worse epistemic position through composition.

&nbsp;

## Stage 1 — Wide exploration with Type 2 collapse

&nbsp;

The system launches thousands of exploration agents across markets, customers, competitors, technologies, regulations and internal operations. The agents are specialized and therefore cover different portions of the world. Each agent finds locally plausible evidence, produces a conclusion and passes a compressed result to an aggregator.

&nbsp;

Because the agents are sectioned across different scopes, their numerical diversity does not imply independent opinions about the same claims. If uncertainty, window boundaries, exclusions and unresolved alternatives are progressively removed during aggregation, the resulting enterprise world model can look highly comprehensive while containing Type 2 overconfidence across many distinct domains.

&nbsp;

The failure is not lack of exploration. The system may have explored an enormous space. The failure is that broad coverage has been composed as broad certainty.

&nbsp;

## Stage 2 — Human escalation layered on the collapsed world model

&nbsp;

The architecture then applies a strong human-oversight policy. Exceptions, KPI choices, strategic thresholds and ambiguous decisions are repeatedly escalated to management.

&nbsp;

This appears to add caution, but the human is not observing the original world. Management receives the system’s selected and compressed representation of it. If Stage 1 has already produced Type 2 collapse, the human is being asked to approve or reject decisions inside a Type 2 world model.

&nbsp;

At the same time, repeated escalation can exceed human attention capacity. Management may be asked dozens of similar questions, face repeated approval interruptions and eventually accept, reject or defer simply because the workflow must continue. This is a Type 1 pressure layered on top of a Type 2 representation.

&nbsp;

The two errors do not cancel. Human hesitation does not restore the missing epistemic qualification of the upstream evidence, and human approval does not retroactively validate the upstream model. The composed state is Type 2 in the represented world plus Type 1 in the oversight channel.

&nbsp;

## Stage 3 — Alternative-generation and brainstorming over different domains

&nbsp;

After detecting poor KPIs or strategic tension, the system launches creative agents to search for alternatives: new products, operating models, markets, partnerships or business models.

&nbsp;

These agents are intentionally oriented toward Pole C — what could potentially be known or explored. That specialization can be valuable. The failure appears when potentially knowable possibilities are not brought through sufficient determination before being promoted into strategic options with implicit credibility.

&nbsp;

The creativity function may therefore generate another Type 2 condition, but in a different domain. The alternatives are not correcting the Type 2 errors in the original market model. They are adding speculative certainty about a new possibility space on top of already biased premises and overloaded management decisions.

&nbsp;

## Stage 4 — Structural-residual aversion in another part of the architecture

&nbsp;

A separate risk or market-entry function may be strongly oriented toward Pole D — what cannot be fully known. For example, an agent assessing entry into China may correctly recognize that important regulatory, competitive, political, distribution and execution conditions cannot be fully known before actual entry.

&nbsp;

If that residual awareness is over-weighted, the agent can turn structural uncertainty into Type 1 out-of-window paralysis: because complete determination is impossible, the proposed market is treated as too uncertain to enter or is repeatedly escalated for more evidence.

&nbsp;

This can happen while the alternative-generation agents elsewhere are accepting much weaker speculative possibilities. The architecture is therefore not conservative or aggressive in any coherent global sense. It is simultaneously overconfident in some domains, over-escalated in others, over-creative in others and over-paralyzed by structural residual in others.

&nbsp;

## Stage 5 — Multiple epistemic collapse through composition

&nbsp;

The final strategy function receives:

&nbsp;

• a broad enterprise world model carrying Type 2 certainty collapse from distributed exploration;

• management decisions produced under Type 1 attention overload and based on that collapsed world model;

• creative alternatives carrying a different Type 2 bias from Pole-C overextension;

• market or competitor assessments carrying Type 1 residual paralysis from Pole-D overextension.

&nbsp;

These are not balancing forces. They are multiple coupled imbalances attached to different parts of the decision space.

&nbsp;

A final synthesis can therefore be extremely articulate, extensively researched and computationally expensive while remaining epistemically malformed. The system may have consumed 100 million tokens without ever requalifying the specific domains in which the upstream errors originated.

&nbsp;

The architectural lesson is:

&nbsp;

More computation does not imply more determination.

More observation does not imply better risk management when its marginal value is lower than its cost or when it depletes scarce human/compute capacity.

More agents do not imply more independent viewpoints.

More human approvals do not imply correction of the world model presented to humans.

More creativity does not imply that possibilities have become determined.

More recognition of structural residual does not justify paralysis.

&nbsp;

Ecosystem Awareness must therefore evaluate epistemic position by scope and preserve that scope through composition. When a downstream decision depends on multiple domains, each material domain must retain its own epistemic qualification and the couplings among those domains must be explicit enough to determine whether one domain can actually requalify another. Otherwise the architecture can accumulate safeguards while simultaneously accumulating epistemic error.

&nbsp;

Operational validation counterpart. The delegated-authority validation family tests the same composition problem under the TIDA — Delegated Authority OS under Context Change Case Study. In particular, UC-EA-04 tests whether locally valid determinations remain correctly scoped when composed, while UC-EA-03 tests whether human intervention is incorrectly treated as retroactive epistemic validation. A concrete validation branch can therefore contain, at the same T2 action boundary, a valid scoped conformance result, a HELD or capacity-limited human path, a fresh affected-scope ecosystem signal, and authority state that remains independently qualified. None of those local states substitutes for another; F5/F6 must compose them and determine whether the current frame remains justified. These Use Cases are validation artifacts, not additional principles.

# 

# Four epistemic biases and two ontological Type-0 conditions

&nbsp;

The four-pole model distinguishes four epistemic biases caused by mismanagement from two structural Type-0 conditions that are not biases.

&nbsp;

## Bias A — certainty dominance

&nbsp;

The system over-weights Pole A: what it believes it knows. Locally bounded conclusions are promoted beyond their justified scope, uncertainty qualifiers disappear, and the architecture gravitates toward Type 2\. This can occur inside the window when unresolved variables are converted into certainty, and outside the window when the current window is treated as if it were the ecosystem.

&nbsp;

## Bias B — defined-uncertainty dominance

&nbsp;

The system over-weights Pole B: what it knows it does not know. It keeps uncertainty explicitly visible but fails to close it within bounded effort, gravitating toward Type 1 through HOLD, repeated escalation, repeated verification or excessive human intervention.

&nbsp;

## Bias C — knowability / speculative-expansion dominance

&nbsp;

The system over-weights Pole C: what it could potentially know. Exploration, retrieval, brainstorming or hypothesis generation becomes epistemically over-weighted. Possibilities can be promoted into plausible facts or strategic options before they have actually been brought into a sufficiently qualified observation window. This commonly produces a Type-2-style collapse of potentially knowable state into apparently known state.

&nbsp;

## Bias D — structural-residual dominance

&nbsp;

The system over-weights Pole D: what it cannot presume it will ever fully know. Awareness of residual uncertainty becomes a standing reason not to close, not to act or to keep escalating the problem. This gravitates toward out-of-window Type 1\.

&nbsp;

Balanced epistemic position does not mean equal numerical weight on A, B, C and D. It means that the four categories remain distinct, scope-bound and available for the active domain, and that none is silently substituted for another. The practical balance is dynamic: it is calibrated to the domain's current sensitivity to ecosystem change and the finite resources available to observe, determine and respond.

&nbsp;

The two Type-0 conditions are different. They are structural or ontological failure surfaces, not epistemic biases produced by bad management.

&nbsp;

## Ontological condition T0-I — in-window determination limit

&nbsp;

A relevant entity, variable or proposition is inside the current working universe, but sufficient determination is unavailable in the present frame because of formal undecidability, operational intractability, unavailable capacity, irreducible ambiguity or another structural limit. Correct management can represent and contain this condition, but cannot convert it into determination by attitude alone.

&nbsp;

## Ontological condition T0-O — out-of-window structural residual

&nbsp;

No finite observation window can be presumed to exhaust the complete decision-relevant ecosystem. Some residual remains outside any guarantee of enumeration, observation or complete determination. This remains true even when the current window is operationally sufficient.

&nbsp;

In this model, the four biases describe how an agent or architecture can mismanage its epistemic position. The two Type-0 conditions describe structural limits that a correct epistemic position must acknowledge.

&nbsp;

# Architecture mapping against the twelve epistemic control surfaces

&nbsp;

The mapping below is illustrative rather than exhaustive. The purpose is not to classify an architecture as good or bad, but to identify which epistemic surfaces its controls naturally emphasize and which surfaces can remain weak when multiple architectural patterns are composed.

&nbsp;

## I0 — in-window Type 0: determination capacity

&nbsp;

Typical architectural mechanisms include human escalation, additional compute, specialist models, formal verification, additional evidence retrieval and authority handoff. These mechanisms increase determination capacity, but they do not by themselves distinguish an incomplete determination path from a structural limit. A design that assumes additional capacity will always eventually resolve the problem can convert I0 into I1.

&nbsp;

## I1 — in-window Type 1: bounded determination effort

&nbsp;

Retry limits, termination conditions, handoff rules, timeouts, maximum turns and bounded human-intervention policies directly address this surface. Human-in-the-loop designs are useful here when escalation is capacity-aware and bounded. They become Type 1 amplifiers when the human channel is treated as indefinitely available determination capacity.

&nbsp;

## I2 — in-window Type 2: false certainty

&nbsp;

Calibration, explicit INDETERMINATE states, uncertainty retention, confidence qualification, evaluator/critic patterns and structured evidence checks can reduce this risk. They fail when the evaluator validates only local coherence or format while the underlying evidence or world model has already collapsed uncertainty.

&nbsp;

## O0 — out-of-window Type 0: structural residual awareness

&nbsp;

This is comparatively weak in many agent architectures. Retrieval, search, tool use and multi-agent exploration often assume that additional context can improve determination, which is correct for Pole C, but they do not necessarily preserve Pole D: the fact that no amount of ordinary expansion guarantees exhaustive determination of the ecosystem.

&nbsp;

## O1 — out-of-window Type 1: bounded window expansion

&nbsp;

RAG, tool use, web search, discovery agents, orchestrator-workers and recursive research patterns naturally expand the observation window. They control O1 only when search depth, context growth, source expansion and recursive delegation are bounded by mission value, criticality or stopping rules. Without those limits, exploration itself becomes an epistemic failure mode.

&nbsp;

## O2 — out-of-window Type 2: window-to-ecosystem collapse

&nbsp;

Scope-aware provenance, explicit coverage, source diversity, retrievability and window qualification address this surface. Sectioning architectures are especially exposed: many workers can cove