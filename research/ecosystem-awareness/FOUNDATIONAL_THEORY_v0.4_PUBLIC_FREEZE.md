# Ecosystem Awareness — Foundational Theory of Bounded Uncertainty

**Version:** v0.4 — public reference freeze, 11 September 2026  
**Source status:** working foundational architecture; final reconciliation / conservation / readability release  
**Publication status:** frozen public reference snapshot for citation and architecture review

> This document is **not** an ITU-T deliverable, not evidence of FG-TIDA adoption and not a NIST submission. It preserves the current foundational model as a public research object before later implementation, interoperability and standards-facing work.

## 1. Foundational premise — no operational actor has the complete ecosystem

Every agent, person, model or subsystem operates from a bounded representation of reality. Sensors, retrieval, memory, human input, external services and models can enlarge that representation, but the effective decision universe remains finite and selective.

A sound actor would like to account for every ecosystem condition capable of materially altering the mission, but it cannot continuously enumerate, observe, retrieve, process and verify the complete ecosystem. Observation itself consumes compute, latency, bandwidth, privacy budget and human attention.

The design problem is therefore not to maximize awareness. It is to choose and continuously requalify a decision-relevant observation window that is:

- wide and fresh enough for the mission's sensitivity to ecosystem change;
- sufficient for the consequence and reversibility profile of the decision;
- feasible within available observation, determination and response capacity; and
- bounded enough to remain operationally executable.

The target is **minimum sufficient awareness**, not omniscience.

## 2. Open ecosystem, bounded representation and residual

Let **Ω** denote the open class of potentially decision-relevant ecosystem state: actors, dependencies, environmental conditions, future configurations and interactions that may materially affect a decision.

Ω is not assumed to be a closed or exhaustively enumerable set.

Let **U** denote the bounded operational universe actually represented for the current decision. U contains the entities, variables, sources, dependencies, controls and actors explicitly brought inside the working decision boundary.

The foundational relation is intentionally not a closed set partition:

- **U is bounded and represented; Ω remains open.**
- **R_U** denotes the open residual relative to U; it is not defined as a closed set complement.
- No finite U is presumed to exhaust the decision-relevant class Ω.

R_U therefore denotes decision-relevant state not represented in U, including state not yet enumerated or categorized.

> **A system can have excellent uncertainty quantification inside U and still have a large R_U.**

Inside U, the relevant object is defined even when its value cannot be determined. Outside U, relevant entities, dependencies or categories may not be listed at all.

This distinction is stronger than a simple known/unknown vocabulary.

## 3. Two uncertainty domains

### 3.1 In-window / represented uncertainty

The relevant entity, variable, dependency or required input is already represented, but it cannot be established sufficiently under the available evidence, access, computation, time or authority.

Examples include:

- an authorised human reviewer who is unavailable within the useful intervention window;
- a known sensor whose measurement is missing or noisy;
- a known dependency that does not answer;
- a probabilistic or non-deterministic value;
- a defined computational problem whose required compute exceeds the available budget;
- contradictory evidence from explicitly represented sources; or
- a known legal or operating constraint whose applicable state cannot yet be resolved.

The characteristic contradiction is:

> **I know that this entity or determination matters. I cannot determine it sufficiently now.**

### 3.2 Open residual / out-of-window indeterminacy

Residual indeterminacy begins where the bounded representation ends.

Relevant ecosystem state may exist outside the active representation even if every represented entity is handled perfectly. Examples include unrepresented participants, unknown co-dependencies, hidden incentives, unlisted third parties, unmeasured environmental conditions, regime shifts, newly created agents or services, future configurations and categories of relevant state not yet conceived.

The characteristic contradiction is:

> **A sound decision should account for all materially relevant ecosystem conditions. The complete materially relevant ecosystem cannot be fully enumerated, observed or kept current.**

The key rule is:

> **A bounded inference must remain bounded.**

A local conclusion can be operationally sufficient without becoming a claim that the complete ecosystem has been determined.

## 4. Structural condition and management failures

The current canonical model distinguishes one structural condition and two failures of epistemic management.

### Type 0 — structural non-determination

Type 0 is not a management error. It is the condition in which the relevant mission-level property remains non-determined under the available system class even when uncertainty is correctly acknowledged and handled.

This may include formally undecidable classes and operationally intractable cases for which no available procedure can produce a sufficiently reliable global determination within the relevant resources and time.

The failure is not the existence of Type 0. The failure is misclassifying it:

- treating it as if further effort were guaranteed to resolve it creates Type-1 pressure;
- treating it as if it were already resolved creates Type-2 false certainty.

### Type 1 — unbounded unresolved uncertainty

The system recognises uncertainty but fails to bound the determination effort or define legitimate closure. It continues waiting, retrieving, escalating, searching or expanding the context without a bounded escape condition.

Operational signatures include:

- indefinite HOLD;
- escalation deadlock;
- epistemic hunger;
- uncontrolled context expansion;
- excessive observation cost; and
- depletion of the human-agent system's remaining response capacity.

Type 1 is therefore also a resource-allocation failure when the marginal decision value of more observation no longer justifies the capacity consumed.

### Type 2 — suppressed uncertainty / false certainty

The system closes by suppressing the unresolved side of the contradiction. Missing input is treated as if it existed, low confidence is promoted to certainty, a local result is treated as globally valid, or an unresolved dependency is silently removed.

Operational signatures include:

- forced PASS/FAIL or YES/NO;
- stale-state reuse;
- fabricated completeness;
- local-to-global confidence inflation; and
- silent removal of residual exposure.

The need to act must not be confused with certainty.

## 5. Sound uncertainty management

Sound management sits between Type 1 and Type 2:

1. acknowledge the contradiction;
2. bound the determination effort;
3. preserve the unresolved epistemic state; and
4. close operationally according to mission criticality, consequence, reversibility, capacity and response horizon.

The correct position is not a fixed midpoint. It is the dynamically requalified point at which the expected decision value of additional awareness no longer justifies its cost.

Operational closure and epistemic determination must remain separate.

A system may need to act while still stating that a relevant condition remains insufficiently determined.

## 6. Observation window W(d,t)

For domain **d** and decision time **t**, let **W(d,t)** denote the bounded active observation/context window used in the current determination process.

W(d,t) is selected from a larger but still bounded represented field and does not exhaust Ω.

The selection of W(d,t) should depend on:

- mission sensitivity to ecosystem change;
- consequence severity;
- reversibility;
- tolerated residual;
- available observation and determination capacity;
- human attention capacity;
- response capability; and
- the remaining time in which new information could still alter the outcome.

A low-sensitivity reversible decision can legitimately operate with a narrower window and larger explicit residual. A high-sensitivity irreversible or mission-critical decision may require a wider, fresher or more independently corroborated window.

More observation is therefore not automatically better.

## 7. Agentic amplification — compositional compression

Agents rarely observe the world directly. They consume representations produced by other agents, humans, sensors, organisations, APIs, documents, summaries and services.

Suppose upstream agent A possesses a richer state including evidence coverage, confidence, unresolved dependencies, source provenance, freshness, capacity state and assumptions, but transmits only a compressed closure such as `PASS`.

If downstream agent B incorporates `PASS` as a fully determined fact, B's visible local uncertainty may decrease while its hidden residual increases.

This is the **compositional compression effect**:

> **Compression can make the represented universe look cleaner while making residual indeterminacy larger, less visible or harder to reconstruct.**

Under ordinary information-preservation constraints, information discarded by a lossy transformation cannot be recreated merely by repeatedly processing the same compressed representation. Independent observations, primary-source retrieval and richer upstream messages can add information; repetition cannot restore what was removed.

The objective is not maximum disclosure. Privacy, security, intellectual property, bandwidth, commercial competition, legal restrictions and limited disclosure authority can all justify bounded transmission.

The requirement is **sufficient epistemic preservation for the downstream decision**.

## 8. Why agentic ecosystems intensify the problem

A useful architectural heuristic is that the ecosystem's change timescale can become comparable to the system's own control timescale.

Agents, models, providers, delegations, memories, context sources, human reviewers and temporary interaction structures can appear, disappear, change authority or change behaviour on timescales comparable to the decision cycle.

Consequently:

- the decision-relevant state space can expand;
- dependency graphs can change;
- the validity lifetime of the current window can shrink; and
- residual exposure can grow or change faster than it can be characterized.

More agents do **not** automatically mean more uncertainty. The material variables are the structure of dependency, source diversity, compression, churn, authority, freshness and the rate at which local assumptions lose validity.

Several agents can each manage local uncertainty correctly and still compose into a globally difficult state.

> **High local confidence can coexist with low global determination.**

## 9. Ecosystem Awareness — working definition

Ecosystem Awareness begins from the recognition that residual indeterminacy is structural and can change rapidly in agentic ecosystems.

A working definition is:

> **Ecosystem Awareness is a bounded assessment capability that determines whether the human, agentic and environmental dependencies required for the current mission remain sufficiently determined, capable and current to justify the present operating mode, while preserving relevant residual indeterminacy where they do not.**

Its objective is minimum sufficient awareness for the mission and criticality.

A useful Ecosystem Awareness function makes visible, to the extent proportionate:

- the current boundary and active observation window;
- what is sufficiently determined;
- what remains unresolved inside that window;
- what potentially relevant state could reasonably be brought into the active window;
- the existence and relevance of structural residual;
- source, provenance and freshness;
- inherited uncertainty from upstream agents;
- human-capacity constraints; and
- the degree to which downstream decisions depend on compressed representations.

It does not require full internal-state sharing.

## 10. Ecosystem signalling — mitigation, not resolution

Ecosystem signalling can preserve and distribute information that participants observe and are able or willing to expose.

It may carry confidence, uncertainty, provenance, freshness, affected scope, human-capacity state, inherited indeterminacy, dependency relevance and divergent observations.

Signalling can reduce avoidable information loss. It cannot:

- create information nobody possesses;
- guarantee that every relevant participant has been identified;
- force independent or adversarial participants to reveal information;
- guarantee truthful, complete or timely signals;
- recreate information destroyed by an unavailable upstream mapping; or
- eliminate the structural residual beyond the bounded representation.

Signalling is therefore preservational and coordinative rather than omniscient.

## 11. Recursive window selection and the limit of complexity reduction

Agentic systems commonly obtain a usable decision window through recursive selection, ranking, retrieval and summarization:

`Ω → W₀ → m₀ → W₁ → m₁ → … → Wₙ → closure`

This can be excellent complexity-reduction technology. It does not guarantee that the final window is globally sufficient.

For a formally undecidable target property, if a recursive selection architecture could always reduce the problem to a finite decision-sufficient window and return the correct result for every admissible instance, the selector plus final procedure would itself constitute a general decider. That contradicts the undecidability assumption.

The architectural consequence is deliberately narrow:

> **Recursive window selection can reduce complexity without eliminating structural indeterminacy.**

Heuristic usefulness is not the same as decidability; empirical accuracy is not a universal correctness guarantee; convergence on a window is not proof of sufficiency; and agreement among agents is not proof that the underlying property has been determined.

## 12. Regime change and requalification

Let **Q** denote the currently qualified operating envelope. Inside Q, multiple known modes may exist, each with sufficiently characterized applicability conditions and response mappings.

A change between known modes inside Q is a **mode change**.

A **regime change** occurs when the ecosystem moves to a state for which the currently qualified envelope can no longer establish a sufficiently valid mission-level response mapping.

Operationally:

> **A regime change is a transition from a qualified operating envelope into an unqualified ecosystem state in which the correct mission-relevant response mapping is not yet sufficiently known or qualified.**

Invariant safety controls can remain valid across regimes. Knowing a safe fallback is different from knowing the correct regime-specific mission response.

The regime-change interval ends operationally when the ecosystem has been requalified sufficiently for the active mission.

This gives Ecosystem Awareness a system-level control role: determine whether the current frame remains sufficiently qualified, identify when windows/dependencies/closure assumptions are losing validity, and support containment, restriction or requalification.

The central objective is:

> **Do not confuse local solvability with global determination, and do not continue operating under a regime whose observation window and closure assumptions are no longer sufficiently qualified.**

## 13. Epistemic and operating posture must remain orthogonal

The epistemic condition must not be conflated with the operating posture.

A system can correctly preserve Type-0 residual indeterminacy and still operate normally when that residual is within the qualified Objective Envelope.

Conversely, Type 1 or Type 2 may require targeted correction without automatically implying full migration.

Useful operating postures include:

- **Normal** — residual uncertainty remains within qualified operating parameters.
- **Containment / Mitigation** — exposure, autonomy or scope is reduced while maintaining a known workable frame.
- **Migration / Regime Transition** — the current frame no longer supplies a sufficiently qualified response mapping and a new frame must be established.

## 14. Architectural principles

The current foundational model preserves ten practical principles:

1. **Defined does not mean determined.**
2. **Unrepresented does not mean irrelevant.**
3. **Unknown is not none.**
4. **Local correctness is conditional.**
5. **Operational closure is not epistemic certainty.**
6. **Paralysis and false certainty are the two fundamental management failure classes; structural Type 0 remains separate.**
7. **Compression can reduce visible local uncertainty while increasing hidden residual.**
8. **Signalling preserves information; it does not create knowledge.**
9. **Awareness should be bounded, risk-indexed and capacity-aware.**
10. **The target is minimum sufficient ecosystem awareness.**

## 15. Candidate research hypotheses

The frozen public reference preserves the following hypotheses for later testing:

- **H1 — Boundary-aware local closure:** explicit insufficient-determination states and bounded resources reduce some deadlock and false-certainty failures.
- **H2 — Residual-scope explicitness:** separating confidence conditional on the represented window from structural residual reduces unjustified local-to-global confidence inflation.
- **H3 — Compositional residual expansion:** systems dependent on lossy compressed upstream representations exhibit greater hidden residual and/or false confidence than systems preserving context or independent-source access.
- **H4 — Bounded preservation:** a compact determinacy/context envelope can preserve enough decision-relevant information to reduce architecture-induced residual without full internal disclosure.
- **H5 — Dynamic ecosystem pressure:** increasing churn and shortening validity lifetimes increase the operational importance of residual preservation and requalification under fixed observation budgets.
- **H6 — Risk-capacity calibrated window selection:** adaptive observation breadth, freshness and determination effort can improve the risk/resource frontier relative to fixed broad or fixed narrow observation.

These are research hypotheses, not established results.

## 16. Candidate measurements

Candidate measurements include:

- local determinacy margin;
- explicit indeterminate-outcome frequency;
- human-capacity binding and escalation demand;
- duration of HELD/unresolved states;
- evidence/sample coverage within the represented window;
- known versus unmeasured dependencies;
- rate of window invalidation under ecosystem change;
- local-to-global confidence inflation;
- information retained or discarded across agent boundaries;
- source diversity and primary-source retrievability;
- propagation depth of compressed closures;
- inherited-indeterminacy detection;
- false confidence from recursive closure reuse;
- freshness and staleness;
- observation/requalification burden in compute, tokens, latency, bandwidth, privacy and human attention;
- capacity depletion caused by repeated Type-1 determination effort;
- missed changes caused by Type-2 under-observation; and
- marginal decision value obtained from additional context or corroboration.

## 17. Claim boundaries

This architecture does not claim:

- that probability and indeterminacy are synonyms;
- that every residual is quantifiable as probability mass;
- that Ω can be exhaustively enumerated;
- that every system-level property is formally undecidable;
- that more agents inherently imply greater information loss;
- that distributed systems are inferior to monolithic systems;
- that ecosystem signalling creates knowledge nobody possesses;
- that complete ecosystem-state sharing is desirable;
- that Ecosystem Awareness replaces observability, uncertainty quantification, provenance, formal methods, resilience, incident exchange, trust management or human oversight; or
- that FG-TIDA, ITU-T, NIST or another standards body has adopted this architecture.

The narrower claim is that agentic systems need an architecture capable of distinguishing uncertainty inside a bounded represented frame from the open decision-relevant residual beyond it; managing both without paralysis or false certainty; and recognising that compositional compression and rapid ecosystem evolution can expand or conceal residual uncertainty even when local decisions remain individually justified.

## 18. Minimum architectural statement

> **Ecosystem Awareness is the set of architectural principles and control mechanisms by which a system maintains justified operation through the correct management of uncertainty inside and outside its current observation window, including detection and handling of Type 0, Type 1 and Type 2 conditions and requalification of the decision frame when its assumptions cease to be sufficient.**

This public freeze preserves the theory for citation and testing. It should not be interpreted as a completed standard, validated implementation or final interoperability specification.
