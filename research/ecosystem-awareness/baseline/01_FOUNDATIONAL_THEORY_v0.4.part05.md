> **Controlled v0.4 release source.** Preserved for release provenance. The current reader successor is [01 — Integrated Foundational Theory v0.5](./01_FOUNDATIONAL_THEORY_v0.5_INTEGRATED.md); use the successor for current reconciled semantics while retaining this source for the controlled v0.4 record.

resses, loses or overextends uncertainty and closes as if sufficient determination existed.

&nbsp;

The operational role of Ecosystem Awareness is therefore not to eliminate all uncertainty. It is to detect which of these conditions is present and apply the appropriate architectural response: reframe or requalify for Type 0, establish bounded closure for Type 1, and restore uncertainty, scope and provenance for Type 2\.

&nbsp;

## 18.2 In-window uncertainty management

Inside the current observation window W, Ecosystem Awareness requires the architecture to treat indeterminacy as an explicit operational state rather than as an error to be hidden.

&nbsp;

Relevant mechanisms can include:

\- explicit INDETERMINATE or insufficient-determination states;

\- Human Capacity Awareness when a required human role, authority or intervention capability is part of the decision window;

\- bounded determination effort, including limits on additional evidence, computation, escalation and context expansion;

\- context-sensitive and adaptive window selection rather than a fixed observation frame;

\- explicit thresholds for when additional context is proportionate and when the system should instead contain, defer, degrade, requalify or transfer control;

\- separation of operational closure from epistemic certainty;

\- detection of Type-1 patterns such as indefinite HOLD, endless escalation or uncontrolled context expansion;

\- detection of Type-2 patterns such as forced binary closure, stale-state reuse, silent assumption promotion or unjustified scope extension; and

\- recognition that persistent non-determination may indicate a Type-0 condition rather than a need to keep searching indefinitely.

&nbsp;

The governing principle is that uncertainty inside W must be worked only to the level required for justified operation. More determination effort is not automatically better if the marginal information gain is insufficient relative to time, cost, latency, safety or mission constraints. The required level itself is dynamic: it rises or falls with mission sensitivity to ecosystem change, consequence severity, reversibility, available capacity and the time left in which new information could still alter the outcome.

&nbsp;

## 18.3 Out-of-window uncertainty management

Out-of-window management does not require reconstructing all state outside W. It requires the architecture to remain aware that the current window is conditional, selected and potentially temporary.

&nbsp;

Relevant mechanisms can include:

\- inter-agent protocols that preserve uncertainty together with closure;

\- propagation of scope, provenance, freshness, unresolved dependencies and inherited indeterminacy;

\- signaling that distinguishes a locally valid result from a globally determined fact;

\- monitoring of the validity lifetime of the current window and its dependency assumptions;

\- detection of divergence among locally justified closures as a possible ecosystem-level warning signal;

\- independent evidence or primary-source recovery when compressed upstream representations have become decision-critical;

\- requalification triggers when previously sufficient windows or response mappings are losing validity; and

\- explicit recognition of possible Type-0 conditions when no currently available window appears sufficient to support the required global determination.

&nbsp;

This makes uncertainty signaling a control mechanism rather than descriptive metadata. Its function is to prevent the architecture itself from creating Type 2 by transmitting closure while discarding the epistemic state that qualified that closure.

&nbsp;

## 18.4 Uncertainty must remain a dynamic state variable

A central architectural principle is that indeterminacy must not be represented as a fixed residual weight.

&nbsp;

An architecture that assigns a constant value to the unknown — for example treating uncertainty as a stable 0.2 contribution in a decision model — implicitly assumes that the size and relevance of the unresolved state remain approximately stationary.

&nbsp;

That assumption can fail abruptly under ecosystem change or regime transition.

&nbsp;

Let u(t) denote an operational measure or representation of unresolved uncertainty relevant to the active mission. Ecosystem Awareness must allow u(t) to change with evidence coverage, dependency state, source diversity, human capacity, window freshness, agent churn, context change and regime qualification.

&nbsp;

The important property is not the particular numerical form of u(t). The architectural requirement is that uncertainty is allowed to increase, decrease or change structure as the ecosystem changes.

&nbsp;

During a transition beyond the qualified operating envelope, uncertainty may rise sharply because previously valid response mappings, dependency assumptions or window-selection rules no longer apply. An architecture that keeps the residual uncertainty contribution fixed will continue to act as if the old epistemic conditions remain valid and is therefore structurally exposed to Type 2\.

&nbsp;

## 18.5 Ecosystem Awareness as principles, not a mandatory named component

Ecosystem Awareness should not be defined as a single software module, product, protocol or control plane that every system must explicitly identify by name.

&nbsp;

It is better treated as a set of architectural principles and control requirements that can be implemented through different mechanisms depending on the system.

&nbsp;

A system may satisfy Ecosystem Awareness through combinations of Human Capacity Awareness, adaptive context selection, uncertainty-preserving inter-agent messages, freshness and provenance controls, bounded search and escalation, requalification triggers, independent observation, safe fallback, containment and other mechanisms.

&nbsp;

The common requirement is that these mechanisms jointly preserve the distinction between what is determined, what remains uncertain inside the current window, what may remain decision-relevant outside the window, and whether the current operating frame is still sufficiently qualified.

&nbsp;

## 18.6 Minimal architectural statement

Ecosystem Awareness is the set of architectural principles and control mechanisms by which a system maintains justified operation through the correct management of uncertainty inside and outside its current observation window, including detection and handling of Type 0, Type 1 and Type 2 conditions and requalification of the decision frame when its assumptions cease to be sufficient.

&nbsp;