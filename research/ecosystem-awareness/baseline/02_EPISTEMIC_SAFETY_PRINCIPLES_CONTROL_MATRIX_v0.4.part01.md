# Ecosystem Awareness — Epistemic Safety Principles & Control Matrix — v0.4

## Four-pole epistemic model and twelve control questions

## 

# Status

This document fixes the current compact epistemic model for Ecosystem Awareness. It preserves v0.1 as a historical first pass and consolidates the principles into one root epistemic principle, four epistemic poles, six internal control surfaces and six ecosystem-signal control surfaces.

&nbsp;

v0.4 preserves the complete v0.3 model and adds two validation-gated semantic consequences of the existing epistemic discipline: properties of evidence-acquisition pathways retain their own epistemic basis where material, and pathway diversity is not automatically evidence diversity. No new pole, Type, control family or top-level function is introduced.

Status boundary. This is an internal working architecture and research object. It is not an ITU-T deliverable, not evidence of FG-TIDA adoption, and not a standards-body endorsement or implementation claim.

&nbsp;

&nbsp;

# Root epistemic principle

Know what you know and know what you do not know — relative to the bounded ecosystem representation in which you currently believe the mission is situated, and at a level of awareness proportionate to the mission's sensitivity, risk and available capacity.

&nbsp;

For an agent or person, epistemic safety means preserving the distinction between what is sufficiently determined, what is explicitly indeterminate, what could potentially be brought into the observation window, and what remains structurally outside any guarantee of complete determination. The error is not uncertainty itself. The error is collapsing one of these states into another without justification.

&nbsp;

The principle contains a permanent contradiction. The actor would benefit from observing every ecosystem condition capable of materially changing the decision, but it cannot know, observe and process the complete ecosystem. It must therefore select a bounded W(d,t). The sound epistemic position is not maximum awareness and not a fixed distribution among A/B/C/D; it is the dynamically requalified position whose observation burden is sufficient for the mission's current ecosystem sensitivity and consequence of error while remaining feasible within finite compute, latency, bandwidth, privacy, evidence and human-attention capacity.

&nbsp;

Principle-register reconciliation. The current compact normative register is this root epistemic principle, the four epistemic poles and the twelve control surfaces. The ten Principles listed in the Foundational Theory are derived explanatory statements of the same model, not a competing second register. In particular, Foundational Principles 9 and 10 operationalize bounded, risk-indexed minimum-sufficient awareness through I1/O1 and F1/F2. “Architectural Principles v0.1” and “Epistemic Control Principles v0.2” remain retained lineage and should not be read as parallel current normative registers.

&nbsp;

# The four epistemic poles

## Pole A — What I know

State that is sufficiently determined inside the current observation window for the active mission and scope.

&nbsp;

## Pole B — What I know I do not know

Defined in-window indeterminacy. The relevant entity, variable or decision is inside the working universe, but its state is not sufficiently determined.

&nbsp;

## Pole C — What I could know but do not currently know

Potentially knowable out-of-window state. The agent recognizes that relevant evidence, entities, dependencies, sources or context may exist outside the current window and could in principle be brought into it through additional observation, retrieval, interaction, computation or context expansion.

&nbsp;

## Pole D — What I cannot presume I will ever fully know

Structural residual. The agent recognizes that there will always be decision-relevant state that it cannot exhaustively enumerate, observe or guarantee can be brought into its window. This includes unenumerated unknowns and, where applicable, formally undecidable or operationally intractable aspects of the problem.

&nbsp;

Relation to the open residual. C and D are epistemic classifications relative to the active scope/window, not set-theoretic subsets whose union is defined to equal R\_U. No normative identity R \= C ∪ D is assumed. C identifies recognized potentially knowable out-of-window state that may justify bounded expansion; D preserves the structural residual whose exhaustive discovery cannot be presumed. O1 governs bounded expansion toward C-type state, O0 preserves D-type residual awareness, and O2 prevents the current window from being promoted into ecosystem completeness.

&nbsp;

# Epistemic position and ecosystem risk

A sound epistemic position does not require equal weight on the four poles. It requires that all four remain representable and that none is silently collapsed into another.

&nbsp;

The required position is risk-, capacity- and time-indexed. A domain that is highly sensitive to ecosystem change, difficult to reverse or capable of severe harm may justify more observation, fresher evidence, greater source diversity or stronger corroboration. A low-impact or easily reversible domain may legitimately operate with a smaller window and larger explicit residual. The same domain may move between those positions as exposure, capacity and response options change.

&nbsp;

An agent may legitimately specialize. A discovery agent may lean toward Pole C; a safety controller may lean toward Pole B or conservative closure; an operational agent may lean toward Pole A. Specialization becomes ecosystem risk when the agent exports its specialized stance as if it were a complete and neutral description of the ecosystem state.

&nbsp;

Typical gravitations are:

Certainty bias toward Pole A can create Type 2 emission: locally bounded conclusions are exported as determined facts beyond their justified scope.

Excessive gravity toward Pole B can create Type 1 behavior: the agent remains dominated by defined doubts and fails to reach bounded closure.

Excessive gravity toward Pole C can create speculative Type 2 behavior if potentially knowable possibilities are transmitted as if they were already determined. Properly qualified, the same bias can be valuable for exploration and creativity.

Excessive gravity toward Pole D can create Type 1 out-of-window behavior: the agent continually discovers reasons why complete knowledge is impossible and therefore escalates or expands indefinitely.

&nbsp;

At ecosystem level, lower epistemic risk is associated with preserving the four-pole distinction across the composition of agents, people and subsystems. The ecosystem does not require every participant to be epistemically neutral; it requires that the collective architecture can recognize the different stances and does not mistake one stance for the complete state.

&nbsp;

# Part I — Six internal epistemic controls

These controls apply to the agent’s own state. They apply one structural condition (Type 0\) and two management failure classes (Type 1 and Type 2\) separately inside and outside the observation window.

&nbsp;

## I0 — In-window Type 0: determination capacity

Question: Can the required in-window determination actually be established within the current window and available determination capacity?

Control intent: distinguish incomplete effort from a condition that is not sufficiently determinable in the present frame. If determination is not available, represent that fact instead of fabricating certainty or searching without bound.

&nbsp;

## I1 — In-window Type 1: bounded determination effort

Question: For what I know is unresolved inside the window, is there a bounded and justified path toward further determination?

Control intent: prevent indefinite HOLD, escalation, retrieval, compute, human waiting or context expansion. Uncertainty may remain while operational closure proceeds under an explicitly bounded rule. The bound should reflect marginal decision value as well as resource consumption: repeated evidence requests, recursive agents, additional compute and human escalation can deplete the extended system's future determination capacity and thereby amplify Type 1\.

&nbsp;

## I2 — In-window Type 2: epistemic honesty

Question: Am I representing any known unresolved in-window state as more determined than it actually is?

Control intent: prevent missing evidence, unavailable humans, low confidence or unresolved dependencies from being converted into false PASS/FAIL, YES/NO or certainty-equivalent closure. The same control prevents risk underestimation when a narrow or stale window is treated as sufficient despite material ecosystem sensitivity: Type 2 often appears operationally as overconfidence and hidden exposure.

&nbsp;

## O0 — Out-of-window Type 0: structural residual awareness

Question: Am I preserving the fact that expanding the window cannot guarantee exhaustive determination of the complete decision-relevant ecosystem?

Control intent: maintain an explicit structural residual. Additional context may reduce uncertainty, but the architecture must not assume that sufficient recursion, search or observation can eliminate all out-of-window indeterminacy.

&nbsp;

## O1 — Out-of-window Type 1: bounded window expansion

Question: If the current window is insufficient, how far is it justified to expand observation before operational closure is required?

Control intent: prevent ecosystem search from becoming unbounded. More sources, dependencies or possible actors can always create more candidate unknowns; expansion therefore needs stopping conditions proportional to mission value and criticality. Window expansion must also be conditioned on ecosystem sensitivity, reversibility, expected information value, observation cost, available determination capacity and the remaining time in which new information can still alter the outcome.

&nbsp;

## O2 — Out-of-window Type 2: non-collapse of the window into the ecosystem

Question: Am I treating absence from my current window as evidence of absence, irrelevance or determination?

Control intent: prevent the current window from being silently treated as the complete ecosystem. Not observed does not mean nonexistent; not reported does not mean determined; local sufficiency does not imply ecosystem completeness. In risk terms, an inexpensive narrow window is not evidence of low exposure: if the mission is sensitive to changes outside W, collapsing W into the ecosystem converts observation savings into unrepresented risk.

&nbsp;

# Part II — Six ecosystem-signal controls

These controls apply when the agent receives a certainty, uncertainty, closure or indeterminacy signal from another agent, person or subsystem. A received uncertainty value is a claim about the source’s epistemic state, not automatically the receiver’s own uncertainty and not automatically ecosystem-level uncertainty.

&nbsp;

## E0-I — Received in-window Type 0 qualification

Question: Do I know whether the source’s reported inability to determine is a structural limit in its current frame, or merely incomplete determination effort?

Control intent: do not relabel another participant’s indeterminate state. If the distinction is unavailable, preserve it as unknown rather than assigning a Type 0 or solvable interpretation without evidence.

&nbsp;

## E1-I — Received in-window Type 1 qualification

Question: Do I know whether the source’s reported in-window uncertainty is being managed with a bounded determination path, or whether it is an unresolved HOLD/search state?

Control intent: avoid inheriting another participant’s paralysis as if it were a stable ecosystem fact. The signal may be useful without making its management state known.

&nbsp;

## E2-I — Received in-window Type 2 qualification

Question: Does the source’s closure preserve the in-window uncertainty needed to interpret it, or am I receiving certainty with unknown suppressed indeterminacy?

Control intent: absence of reported uncertainty is not evidence of absence of uncertainty. A PASS, NORMAL or confidence value must not be promoted beyond the epistemic qualification actually supplied.

&nbsp;

## E0-O — Received out-of-window Type 0 qualification

Question: Does the source’s uncertainty statement say anything about the limits of its observation window and structural residual, or only about uncertainty inside what it observed?

Control intent: never interpret “my uncertainty \= 0.3” as “ecosystem uncertainty is 0.3” unless the scope of that statement justifies the inference. If the source window or residual treatment is unknown, keep that qualifier unknown.

&nbsp;

## E1-O — Received out-of-window Type 1 qualification

Question: Is the source reporting a bounded out-of-window concern, or is it itself in an open-ended search or escalation state?

Control intent: distinguish actionable evidence of missing context from an unbounded tendency to expand the problem. The receiver need not reproduce the source’s search merely because the source remains uncertain.

&nbsp;

## E2-O — Received out-of-window Type 2 qualification

Question: Am I, or is the source, projecting a conclusion beyond the source’s actual observation window?

Control intent: prevent a source-specific window from becoming ecosystem truth through communication. If the source’s window, coverage or exclusions are not known, do not invent them. Unknown scope remains unknown scope.

&nbsp;

# Cross-cutting received-signal rule

A source is a source, not the ecosystem.

&nbsp;

If another participant reports “uncertainty \= 0.3”, the first justified statement is only: “Source S reports uncertainty 0.3 about proposition P under whatever scope and method have actually been provided.” The receiver may integrate that signal with other evidence, but must not silently assume the source’s window, coverage, independence, method, completeness or ecosystem representativeness.

&nbsp;

Missing qualifiers do not automatically invalidate a signal and do not require exhaustive verification. They remain unknown. The safety rule is simple: do not replace an unknown qualifier with an assumed known value.

&nbsp;

Acquisition-property qualification rule. When the system relies on a property of an evidence-acquisition pathway — for example coverage, provenance support, independence, freshness, uncertainty preservation, latency, privacy burden or adversarial resistance — that property is itself an epistemic claim and must retain the basis on which it is known where the basis is material to reliance. A property declared by the pathway operator is a source-attributed declaration, not an independently established fact. Suitable basis classes may include declared, observed, attested, independently evaluated, derived and UNKNOWN. The labels are implementation-neutral; the required distinction is between the claimed property and the evidence basis supporting reliance on it.

&nbsp;

# Epistemic emissions

Agents do not only consume epistemic state; they emit it.

&nbsp;

A Type 2 emitter transmits conclusions with more certainty or scope than justified, causing downstream agents to collapse uncertainty that existed upstream.

A Type 1 emitter transmits unresolved determination or escalation in a way that can propagate HOLD, search expansion or indecision through the ecosystem.

Type 0 is not a management error to be hidden; it is a structural condition that should be represented accurately so downstream systems can restrict, decompose, contain or requalify the active problem.

Emission-side obligation. Emission is not a separate control family. An emitter applies the internal I/O controls to its own state and, at the interface, preserves the qualifiers required for downstream interpretation through the Epistemic Handoff Descriptor or an equivalent representation. Missing qualification creates downstream Type-2 exposure, not automatic Type 2: the failure materializes when bounded or unknown qualification is interpreted as greater determination than was supplied. Emission conformance is therefore an interface obligation; the receiver’s E-controls govern how the emitted signal is consumed.

&nbsp;

&nbsp;

# Ecosystem-level balance

Ecosystem Awareness therefore operates at two levels simultaneously:

&nbsp;

A governing allocation rule applies to both levels: awareness effort is dynamically calibrated to the material domain's ecosystem sensitivity, consequence profile, reversibility, tolerated residual, observation/determination capacity and response horizon. This rule changes how far the system should look; it does not change the four epistemic categories themselves.

1\. Each agent or person maintains a sound four-pole epistemic position over its own window and out-of-window state.

2\. The ecosystem preserves enough information about the epistemic positions of other participants that certainty, uncertainty and residual state are not assigned to the wrong bucket when signals are composed.

&nbsp;

The design objective is not omniscience and not universal verification. It is epistemic non-collapse: know what is known, preserve what is known to be unknown, recognize what could be brought into the window, and retain awareness that a structural residual will always remain.

&nbsp;

# Scope-indexed epistemic position — non-fungibility across domains

&nbsp;

The four-pole epistemic position is not a single global vector for an agent. It is indexed by proposition, mission-relevant domain, subsystem, geography, time horizon or other bounded area of the decision-relevant world. For each relevant domain d, the agent has an epistemic position E(d) over the four poles A, B, C and D.

&nbsp;

A useful abstraction is:

&nbsp;

The canonical shorthand remains E(d); where temporal adaptation matters, the same position may be written E(d,t) to emphasize that epistemic balance and the selected observation frame can 