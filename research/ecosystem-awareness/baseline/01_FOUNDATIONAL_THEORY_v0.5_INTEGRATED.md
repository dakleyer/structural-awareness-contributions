# Ecosystem Awareness — Integrated Foundational Theory of Bounded Uncertainty and Ecosystem Change

**Status:** public integrated working successor v0.5, 15 September 2026; not a replacement of the controlled v0.4 freeze, an ITU-T deliverable, an adopted standard, or completed validation.

**Conservation rule:** the earlier v0.4 §§1–18 are included below once each, with their prose retained and source-section labels visible. The earlier five split files and the additive 01A note remain intact as historical source files. New work is integrated by the two linked origins and their architectural consequences; external programmes remain separate interfaces, not adopted implementations.

## 1. Foundational problem: two related, non-identical origins

Ecosystem Awareness (EA) addresses two conditions that must be kept distinguishable. First, no operational actor should presume that its bounded representation exhausts all potentially mission-relevant ecosystem state, even when its represented frame is well constructed. Second, the ecosystem on which an otherwise justified operation depends can change during the observation, decision or control cycle. The first is an epistemic and capacity limit; the second is a temporal and relational qualification problem. Their interaction creates the architectural need for bounded, continuously requalified awareness. Neither condition alone implies that every decision must stop or that the complete ecosystem must be reconstructed.

### 1.1 Residual indeterminacy and the epistemic posture

This subsection **conserves rather than replaces** the current v0.4 derivation. The present Foundational Theory, §§1–18, remains the complete technical treatment; the following is an entry statement and reading route, not a compressed substitute.

Every agent, human, model or subsystem acts from a finite and selective representation. Let Ω name an *open class* of potentially decision-relevant ecosystem state, U the bounded operational universe actually represented for a decision, and R_U the open decision-relevant residual relative to U. R_U is **not** a known, exhaustively enumerated set complement of U. Inside U, a defined entity, variable, source, dependency or required human role may still be unresolved. Outside U, relevant actors, categories or relationships may not yet have been identified at all. Good uncertainty quantification for identified objects inside U therefore does not establish completeness outside U; probability and residual indeterminacy are not synonyms.

The observation window W(d,t) must be selected and repeatedly qualified for the decision, mission and time. Selection is not unrestricted context accumulation. Observation, retrieval, verification, computation, communication, response and escalation consume finite capacity; human attention and availability belong to the combined human–agent system rather than being treated as free external resources. The justified window depends on mission sensitivity, severity of error, reversibility, freshness, available capacity and the remaining time in which evidence could affect the response. Epistemic balance is dynamic and risk-indexed, **not** an equal distribution over the four epistemic positions.

Those positions must remain separate: sufficiently determined state; explicitly unresolved state within the active representation; recognized potentially knowable state that may justify bounded window expansion; and structural residual that cannot be presumed exhaustively discoverable. The latter positions are epistemic qualifications relative to the active scope, not a closed partition or an identity that makes the residual enumerable. A local closure must retain its scope, freshness, unresolved qualifiers and provenance when passed to another participant. Recursive propagation of an apparently clean binary result without those qualifiers can turn locally defensible decisions into unjustified ecosystem-level certainty.

The canonical taxonomy distinguishes **Condition Type 0**, structural non-determination despite correct local management, from **Failure Type 1**, acknowledged uncertainty without bounded legitimate closure, and **Failure Type 2**, suppressed uncertainty promoted into false certainty. Type 0 is not a third management failure and is not removed by wishing for more data. Type 1 includes indefinite HOLD, search or escalation that consumes the capacity and response time needed to act; HOLD is not invariably a safe terminal state. Type 2 includes forced binary closure, stale-frame reuse, scope extension, or silently discarded missing inputs. Both failures can arise inside U and in relation to R_U. A smaller, restricted problem can remain solvable even where a global property is not sufficiently determinable; local correctness never proves global determination.

The operational posture is therefore to obtain **bounded, justified closure**: investigate only while the expected decision value of additional determination warrants its cost; represent genuine UNKNOWN or INDETERMINATE conditions; restrict, decompose, defer, contain or requalify where appropriate; preserve inherited uncertainty and authority boundaries; and never confuse a sufficient local control with exhaustive knowledge. Signalling from other participants can improve a limited view but cannot create knowledge that no source possesses, erase upstream uncertainty, or itself authorize intervention.

The technical derivation, examples, formal limits, Pole A–D qualifications, Type 0/1/2 treatment, agentic amplification, hypotheses H1–H6, candidate measurements and claim boundaries remain in the unchanged [v0.4 Foundational Theory](./01_FOUNDATIONAL_THEORY_v0.4.part01.md), continued in [part 2](./01_FOUNDATIONAL_THEORY_v0.4.part02.md), [part 3](./01_FOUNDATIONAL_THEORY_v0.4.part03.md), [part 4](./01_FOUNDATIONAL_THEORY_v0.4.part04.md) and [part 5](./01_FOUNDATIONAL_THEORY_v0.4.part05.md). In particular, §§16–18 govern recursive-window and structural-limit interpretations. This note neither deletes nor silently supersedes those sections.

#### Detailed source derivation for 1.1 — represented uncertainty, residual and recursive window limits

#### Source v0.4 §1 — Foundational premise — no operational actor has the complete ecosystem

Every agent, person, model or subsystem operates from a bounded representation of reality. It may have extensive sensors, retrieval, memory, human input, external services and models, but its effective decision universe is still finite and selective.

&nbsp;

Foundational contradiction — awareness under finite risk and capacity. A sound actor would like to account for every ecosystem condition capable of materially altering the mission, but it cannot continuously enumerate, observe, retrieve, process and verify the complete ecosystem. Observation itself consumes resources and can change latency, cost, privacy exposure, compute use, bandwidth and human attention. The actor therefore operates not from 'where it objectively is' in a complete sense, but from a bounded and revisable representation of the ecosystem in which it currently believes the mission is situated.

This representation is participant-local rather than an assumed shared ecosystem model. Different participants may hold different represented universes, active windows and qualified positions at the same time. Where objectives, mandates, policies or governance constraints are externally owned, the participant holds only a qualified local representation or reference of them; it does not thereby become their owner. [Annex 01H](./01H_PARTICIPANT_LOCAL_ECOSYSTEM_POSITIONING_AND_DECISION_SCOPED_EPISTEMIC_OPPORTUNITY_v0.1.md) makes this distributed-positioning reading explicit. [Annex 01I](./01I_AGENTIC_CITIZENSHIP_CONTRACT_HUMAN_GOVERNED_PARTICIPATION_PROFILE_v0.1.md) treats optional human-governed participation constraints as a separate neighbouring layer outside the EA core.

&nbsp;

This creates a permanent design problem: choose and continuously requalify an observation window W(d,t) that is sufficient for the mission's sensitivity to ecosystem change, consequence severity and required response horizon, while remaining feasible within the combined system's available observation, determination and response capacity. The combined system includes relevant humans: repeated escalation or requests for more context consume human capacity just as retrieval consumes compute and latency.

&nbsp;

Epistemic balance is therefore dynamic and risk-indexed, not a 25/25/25/25 distribution over the four later epistemic poles. A low-sensitivity, reversible decision may legitimately operate with a smaller or less expensive window and larger explicit residual. A high-sensitivity, irreversible or mission-critical decision may require a wider, fresher or more independently corroborated window. In both cases the categories of known, unresolved, potentially knowable and structural residual must remain distinct.

&nbsp;

Let Ω denote the open class of potentially decision-relevant ecosystem state: actors, dependencies, environmental conditions, future configurations and interactions that may materially affect a decision. Ω is not assumed to be a closed or exhaustively enumerable set; it is an open decision-relevant class whose relevant membership may expand as the ecosystem, mission and represented dependencies change.

&nbsp;

Let U denote the bounded operational universe actually represented for the current decision. U contains the entities, variables, sources, dependencies, controls and actors that the system has explicitly brought inside its working decision boundary.

&nbsp;

The foundational relation is intentionally not a closed set partition:

&nbsp;

**U is bounded and represented; Ω remains open.**

**R\_U denotes the open residual relative to U; it is not defined as a closed set complement.**

**No finite U is presumed to exhaust the decision-relevant class Ω.**

**R\_U denotes decision-relevant state not represented in U, including state not yet enumerated or categorized.**

&nbsp;

R\_U is the open decision-relevant residual relative to the represented universe U. It is an epistemic/architectural residual, not an assertion that the remainder of Ω has itself been exhaustively enumerated.

&nbsp;

This distinction is more important than a simple “known versus unknown” vocabulary. Inside U, the entities are defined. They may be incompletely measured, unavailable, stochastic, computationally expensive, contradictory or dependent on unavailable human capacity, but the architecture at least knows what the relevant entity or variable is.

&nbsp;

Outside U, the problem is different. Relevant entities, dependencies or states may not be listed at all. The architecture may not know how many there are, which ones matter, or even what categories are missing. Ω is therefore not assumed to be fully enumerable.

&nbsp;

A system can have excellent uncertainty quantification inside U and still have a large R.

&nbsp;

#### Source v0.4 §2 — Uncertainty as the operational manifestation of a contradiction

For this architecture, uncertainty becomes operationally important when two requirements cannot simultaneously be satisfied under the current boundary and resources.

&nbsp;

The generic contradiction is:

&nbsp;

A determination is important or required for the decision.

The available evidence, access, computation, measurement, time or authority is insufficient to establish that determination to the required degree.

&nbsp;

This contradiction must be managed. It cannot be eliminated merely by requiring certainty.

&nbsp;

Uncertainty management means acknowledging both sides of the contradiction and defining a bounded operational closure that preserves the unresolved epistemic state.

&nbsp;

Within uncertainty management there are two fundamental management failure modes. Condition Type 0 remains separate: it is structural non-determination despite correct management, not a third failure mode.

&nbsp;

##### Failure Type 1 — unresolved contradiction / paralysis

The system refuses to close because the required knowledge has not been obtained. It continues waiting, escalating, searching or expanding the determination effort without a bounded escape condition. Operationally, this appears as indefinite HOLD, escalation deadlock, epistemic hunger or paralysis.

&nbsp;

Type 1 is also a resource-allocation failure when the marginal value of further observation or determination no longer justifies the capacity consumed. The window can become too wide, too deep or too frequently refreshed for the mission. More retrieval consumes compute and latency; more verification consumes processing; more external consultation consumes communication; more human escalation consumes attention and may reduce the future capacity of the extended human-agent system. Type 1 can therefore become self-reinforcing: unresolved state → more observation/escalation → less remaining capacity/time → greater unresolved pressure.

HOLD is not necessarily a safe terminal state. In a live system, a prolonged HOLD can itself change the interaction pattern: it may trigger other agents or controllers, transfer effective control to a timeout or fallback, allow environmental dynamics to continue, or force another actor to intervene. Type 1 therefore remains epistemically distinct from Type 2, but under time or mission pressure it can still move the ecosystem into a worse downstream state or loss of coherent control.

&nbsp;

&nbsp;

##### Failure Type 2 — suppressed contradiction / false certainty

The system closes by discarding the fact that the required knowledge was not obtained. Missing input is treated as if it existed, low confidence is promoted to certainty, a local result is treated as globally valid, or an unresolved dependency is silently removed from the decision. Operationally, this appears as forced PASS/FAIL, YES/NO, fabricated completeness or false closure.

&nbsp;

Type 2 is also an exposure/risk failure when the observation frame is too narrow, stale or insufficiently sensitive for the mission. The system under-observes the ecosystem, underestimates relevant change or treats unavailable risk information as non-risk. The operational signature is overconfidence: the apparent cost of observation is low because relevant residual has been suppressed, while the actual exposure can rise beyond the qualified frame.

&nbsp;

These two failure types apply to both uncertainty domains. The object of uncertainty changes; the failure logic does not.

&nbsp;

#### Source v0.4 §3 — Domain U — uncertainty among defined entities inside the operational universe

##### 3.1 Object

Domain U contains the uncertainty that exists inside the explicitly represented decision universe.

&nbsp;

The defining property is not that the system knows the answer. The defining property is that the entity, variable, dependency or required input is already identified as part of the decision model.

&nbsp;

Examples include:

* a named human approver whose input is required but unavailable within the useful decision window;  
* a known sensor whose measurement is missing or noisy;  
* a known dependency that does not answer;  
* a known variable with a probabilistic or non-deterministic value;  
* two hypotheses that remain observationally indistinguishable;  
* a defined computational problem for which the available compute or time budget is insufficient;  
* an explicitly represented source whose evidence is incomplete or contradictory;  
* a known regulatory or operating constraint whose applicable state cannot yet be resolved.

&nbsp;

The key distinction is: the uncertainty concerns a defined object inside U.

&nbsp;

##### 3.2 Characteristic contradiction

The Domain-U contradiction is:

&nbsp;

“I know that this entity or determination matters.”

“I cannot determine it sufficiently now.”

&nbsp;

For example:

&nbsp;

Human input is required for a mission-critical decision.

The authorised human is part of U and the escalation path is defined.

The human is unavailable within the useful intervention window.

&nbsp;

Nothing about this case requires the human to be “outside the context window.” The human, role and required input are explicitly inside the model. The uncertainty arises because determination capacity is insufficient, not because the relevant entity is absent from U.

&nbsp;

The same logic applies to compute, measurement, evidence retrieval and non-deterministic outputs.

&nbsp;

##### 3.3 Uncertainty management in Domain U

Management begins with acknowledgement.

&nbsp;

The system must be able to represent, as a valid operational fact:

&nbsp;

“I cannot determine this sufficiently within the available boundary, resources and time.”

&nbsp;

It then requires bounded closure rules. These may include:

* an explicit INDETERMINATE state;  
* HELD with a defined timeout or capacity threshold;  
* deferred action;  
* reduced-scope operation;  
* containment;  
* safe fallback;  
* human escalation when reachable;  
* additional evidence or computation when proportionate;  
* or another explicitly bounded posture appropriate to mission criticality.

&nbsp;

The vocabulary is secondary. The architectural requirement is that operational closure and epistemic determination remain separate.

&nbsp;

A system may have to act while still stating that a relevant condition remains insufficiently determined.

&nbsp;

##### 3.4 Failure Type 1 in Domain U — indefinite HOLD

The system treats the importance of the missing determination as proof that the determination must eventually be obtained.

&nbsp;

critical condition

→ must know

→ request more evidence / compute / human input

→ required resource unavailable

→ continue waiting or escalating

&nbsp;

The failure is not the request for more information. The failure is the absence of a bounded capacity model and escape condition.

&nbsp;

In time-critical systems, epistemic perfectionism can itself become an operational hazard.

&nbsp;

##### 3.5 Failure Type 2 in Domain U — forced certainty

The system has two facts:

&nbsp;

it must act;

it has not obtained sufficient determination.

&nbsp;

A badly designed architecture removes the contradiction by suppressing the second fact.

&nbsp;

Examples:

* the human did not answer, but the workflow records approval-equivalent progress;  
* evidence is insufficient, but the classifier is forced to output PASS;  
* confidence is below the required threshold, but the state is converted to YES;  
* a dependency is unavailable, but its last known status is silently treated as current.

&nbsp;

This is false closure. The need to act has been mistaken for certainty.

&nbsp;

**Domain-U rule:**

**A correct local architecture must be able to say both “I have to act” and “I do not know this sufficiently.”**

&nbsp;

#### Source v0.4 §4 — Residual domain relative to U — uncertainty outside the represented universe

##### 4.1 Object

Residual indeterminacy begins where U ends.

&nbsp;

Even if every defined entity inside U is managed perfectly, the local inference remains conditional on U. Relevant ecosystem state may exist outside that boundary.

&nbsp;

Examples include:

* participants not represented in the local dependency graph;  
* future ecosystem configurations not represented in the current model;  
* unknown co-dependencies;  
* unobserved population segments;  
* hidden incentives;  
* unlisted third parties;  
* unmeasured environmental conditions;  
* regime shifts;  
* new agents or services created after the last ecosystem qualification;  
* interactions that the architecture has not represented;  
* and categories of relevant state that have not yet been conceived.

&nbsp;

The defining property is therefore different from Domain U:

&nbsp;

inside U, the relevant entity is defined but may be indeterminate;

inside R, the relevant entity or dependency may not be defined or enumerable at all.

&nbsp;

##### 4.2 Characteristic contradiction

The residual contradiction is:

&nbsp;

“A sound decision should account for all materially relevant ecosystem conditions.”

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

##### 4.3 Probability is not the residual

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

##### 4.4 Uncertainty management in the residual domain

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

##### 4.5 Failure Type 1 in the residual domain — epistemic paralysis

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

##### 4.6 Failure Type 2 in the residual domain — collapse Ω into U

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

#### Source v0.4 §5 — One failure taxonomy across both uncertainty domains

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

#### Source v0.4 §6 — Agentic amplification mechanism — compositional compression expands or obscures R

##### 6.1 Why this is not a third uncertainty domain

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

##### 6.2 Source-selection example

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

##### 6.3 Information-preservation anchor

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

##### 6.4 Incentives and deliberate restriction

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

#### Source v0.4 §16 — Out-of-window indeterminacy — Problem 1: recursive window selection cannot create decidability

&nbsp;

##### 16.1 Observation window and out-of-window indeterminacy

&nbsp;

From this section onward, “out-of-window indeterminacy” is used as the operational term for decision-relevant state outside the current observation window. This is a vocabulary refinement for the analysis that follows; it does not modify the definitions or notation used in preceding sections.

&nbsp;

Let W denote the current observation window: the finite set of entities, variables, evidence, dependencies and representations actively available to the decision process.

Relation to U. U is the bounded represented operational universe used in the foundational development. W(d) is the active, domain-scoped working observation/context frame used by the current functional architecture. W refines the operational boundary at domain and decision time; it does not introduce a second closed universe or an exhaustive partition of Ω. A relevant entity may remain inside the working frame even when its current value or input is unavailable. The later W notation is therefore a refinement for window selection and requalification, not a redefinition of Ω as a closed set.

&nbsp;

Represented observable field versus active window. For explanatory purposes, O\_rep(d,t) may denote the state that is currently technically accessible, observable, discoverable or retrievable to the system for domain d at time t. O\_rep(d,t) is itself a bounded represented field: it is not Ω and it is not the complete ecosystem. W(d,t) is the bounded portion of that represented field admitted to active interpretation for the current decision. Information may therefore be technically available without being active decision context, and material change may justify moving previously excluded observable state into W(d,t). This distinction does not close Ω or imply that everything outside W is enumerated in O\_rep.

&nbsp;

Relation of C/D to the residual. Pole C and Pole D are epistemic classifications relative to the active scope/window; they are not set-theoretic subsets whose union is defined to equal R\_U, and no normative identity R \= C ∪ D is assumed. C denotes recognized potentially knowable out-of-window state that may justify bounded expansion; D denotes structural residual whose exhaustive discovery cannot be presumed. O1 governs bounded expansion toward C-type state, O0 preserves D-type residual awareness, and O2 prevents the current window from being promoted into ecosystem completeness. These controls operate on epistemic qualification, not on a closed partition of Ω.

&nbsp;

&nbsp;

Out-of-window state is decision-relevant state that may exist beyond W and is therefore not represented in the current determination process.

&nbsp;

The architectural question is no longer only:

&nbsp;

“How uncertain am I inside the window?”

&nbsp;

It is also:

&nbsp;

“How was this window selected from a much larger, only partially accessible ecosystem?”

&nbsp;

##### 16.2 Recursive window selection as complexity-reduction technology

&nbsp;

Agentic systems rarely construct W directly from the complete ecosystem. They commonly obtain it through other agents, services, organizations, models, rankings, summaries and retrieval mechanisms.

&nbsp;

A simplified chain is:

&nbsp;

Ω → W₀ → m₀ → W₁ → m₁ → … → Wₙ → closure

&nbsp;

where each mᵢ \= fᵢ(Wᵢ) is the representation passed across an intermediary boundary, and each downstream window is constructed from the received representation plus locally available context.

&nbsp;

Where fᵢ is many-to-one, materially different upstream states may map to the same downstream representation.

&nbsp;

The chain therefore acts as recursive window-selection technology. It reduces complexity until a finite, decision-capable observation window is obtained.

&nbsp;

This is not inherently a defect. In large ecosystems, selection is unavoidable. A carefully designed selection chain may be efficient, accurate and operationally appropriate, particularly when the relevant problem class is well characterized and the operating regime is stable.

&nbsp;

The theoretical question is stronger:

&nbsp;

Under what conditions can such recursion support a guarantee that the final selected window is sufficient for the global property being decided?

&nbsp;

##### 16.3 Conditions for a global correctness guarantee

&nbsp;

At minimum, two distinct conditions must hold before recursive window selection can support a general global correctness claim:

&nbsp;

1\. The target property must be decidable, or be restricted to a domain in which a defensible bounded-error or decision procedure exists.

2\. The operating regime must remain sufficiently stable that relevance or sufficiency of the selected window does not expire while it is constructed, communicated or reused.

&nbsp;

These conditions are necessary, not sufficient. Even when both hold, the specific selector must preserve the information required by the target decision.

&nbsp;

This section addresses only the first condition. Regime instability is a separate problem and is deliberately deferred.

&nbsp;

##### 16.4 Problem 1 — an undecidable global property

The argument below establishes an impossibility of guarantee, not a claim about the difficulty of typical instances. It assumes that the recursive selection chain and final decision procedure are themselves effective procedures. Its architectural consequence is narrow: for a formally undecidable target class, sophistication of the selection mechanism cannot establish a universal guarantee that the selected window is decision-sufficient.

##### 

&nbsp;

An undecidable problem is not merely a decidable problem with a large amount of missing information.

&nbsp;

For a formally undecidable property, there is no general effective procedure guaranteed to produce the correct decision for every admissible instance.

&nbsp;

Rice’s theorem supplies a precise anchor for one important class: every non-trivial semantic property of the function computed by an arbitrary program is undecidable in general.

&nbsp;

This does not imply that every complex real-world question is undecidable. Its architectural relevance is narrower and stronger.

&nbsp;

Assume P is a global binary semantic property over arbitrary programs in a Turing-complete model and P is undecidable.

&nbsp;

Suppose a recursive window-selection architecture could always:

&nbsp;

\- reduce relevant ecosystem state to a finite final window W\*;

\- preserve exactly the information required to determine P; and

\- produce the correct YES/NO answer for every admissible instance.

&nbsp;

Then the selector plus the final decision procedure would itself constitute a general decider for P.

&nbsp;

That contradicts undecidability.

&nbsp;

Therefore, for such a problem class, no recursive window-selection architecture can guarantee that it will always identify a decision-sufficient window and return the correct global determination.

&nbsp;

##### 16.5 Why the problem is structural, not merely residual

&nbsp;

For an incomplete but decidable problem, more evidence, computation or observation may in principle move the system toward determination.

&nbsp;

For an undecidable property, no general algorithmic path guarantees that more selection, recursion, agents or ordinary computation will resolve every instance.

&nbsp;

Window selection can reduce complexity. It cannot change the decidability class of the underlying problem.

&nbsp;

In the guarantee sense, recursion has not solved the global determination problem. It has produced a smaller representation on which an operational decision may be made.

&nbsp;

The distinctions are fundamental:

&nbsp;

\- heuristic usefulness ≠ decidability;

\- empirical accuracy ≠ general correctness guarantee;

\- convergence on a window ≠ proof that the window is sufficient; and

\- agreement among agents ≠ proof that the underlying property is determined.

&nbsp;

The structural risk is that successful complexity reduction is represented as epistemic resolution.

&nbsp;

##### 16.6 A precise binary example

&nbsp;

The generic question “Is A or B more probable?” is not, by itself, an undecidable problem. Undecidability depends on the formal property and domain.

&nbsp;

A cleaner example is:

&nbsp;

“Given an arbitrary program or sufficiently expressive computational agent, will it eventually exhibit semantic behavior A?”

&nbsp;

If A denotes a non-trivial semantic property of the computed function, Rice’s theorem means that no general algorithm decides it correctly for every arbitrary program.

&nbsp;

Now place an arbitrarily sophisticated recursive chain of agents before the final answer. Each agent filters, summarizes or selects the “most relevant” observation window before the chain returns YES or NO.

&nbsp;

If that chain were guaranteed to be correct for every arbitrary program, the chain as a whole would be a general decider.

&nbsp;

Recursion may still be useful for restricted subclasses, empirical performance, evidence surfacing and operational closure.

&nbsp;

It cannot manufacture a universal correctness guarantee that the underlying problem does not admit.

&nbsp;

##### 16.7 What undecidability does not imply

&nbsp;

Undecidability does not imply:

&nbsp;

\- every individual instance is unknowable;

\- every observation window is useless;

\- the alternatives are necessarily 50/50;

\- no prior, empirical distribution, restricted-domain result or independent observation can make one outcome more plausible; or

\- systems should stop acting.

&nbsp;

“Total blindness” would therefore be too strong without an additional epistemic condition: that no defensible asymmetry, prior, restricted-domain result or independent evidence exists.

&nbsp;

The stronger defensible conclusion is:

&nbsp;

Some problem classes admit no recursive window-selection architecture that can guarantee that the final observation window resolves the global property correctly for all admissible instances.

&nbsp;

##### 16.8 Architectural consequence

&nbsp;

The first structural problem of out-of-window indeterminacy is therefore:

&nbsp;

Recursive window selection can reduce complexity without reducing structural indeterminacy.

&nbsp;

The chain may narrow the observation space, lower visible local uncertainty and yield operational closure. None of those facts proves that the global property was decidable or that the final window was sufficient.

&nbsp;

For an undecidable target property, no recursive selection architecture can provide a universal correctness guarantee.

&nbsp;

This creates a first non-residual failure surface:

&nbsp;

The system may successfully select a window and still have no general basis for claiming that the selected window resolves the global decision problem.

&nbsp;

The second structural problem — whether a previously sufficient window remains sufficient when the operating regime changes — is deliberately deferred to the next section.

&nbsp;

### 1.2 Ecosystem change and loss of frame qualification

An *ecosystem*, in the working sense developed in the [Theme #13 public comment](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5585387513), is a dynamic mesh of participants, dependencies and environmental conditions whose interactions materially affect one another's ability to operate. It is not necessarily one agent or one system; it may be centrally controlled, partly coordinated or independently governed. Interdependence, not universal reciprocity or net contribution, is the defining property. Competitors, adversaries, observers and indifferent participants can matter when they alter the dependency mesh. Existing cyber-ecosystem, system-of-systems and trust-relationship terminology provides reference anchors; EA does not invent the general concept of an ecosystem.

Ecosystem dependency itself is not new. The change is that an operational cycle cannot always treat the relevant surrounding frame as effectively stable. A useful *historical approximation*, not a universal law, is T_ecosystem ≫ T_system: the relevant ecosystem changes more slowly than the protected system's decision/control cycle. In agentic arrangements, agents, models, tools, providers, delegations, human review capacity, memory/context sources and temporary interaction structures may appear, disappear or reconfigure on comparable or shorter timescales: T_ecosystem ≈ T_system, sometimes T_ecosystem < T_system. These are qualitative timescale relations, not measured constants or a claim that every deployment has crossed the same threshold.

A decision may be correctly authenticated, authorized, attested and approved under its *local* rules, yet rely on a dependency, capacity, source, human availability or response mapping that has materially changed. Its former sufficiency was conditional on a frame whose validity lifetime has ended. Change must therefore trigger a question different from “was the local computation correct?”: **does the current ecosystem frame still sufficiently support the mission-level operation?** Change can invalidate an assumption without adding an identifiable new variable to U, and residual indeterminacy can exist without a contemporaneous regime change. The two origins must not be collapsed into a single “more uncertainty” axis.

The architecture should distinguish ordinary variation inside a qualified operating envelope Q from a transition beyond Q. Known modes inside Q can have qualified applicability conditions and response mappings. A *regime change*, as treated in v0.4 §17.4, arises when membership or mission-level response validity can no longer be established sufficiently under that envelope. This does not mean every action becomes unknown: invariant safety, restriction or containment controls may remain qualified. Operationally, transition ends only when a newly or again qualified frame sufficiently supports the active mission. An incident's closure does not by itself prove ecosystem requalification.

The broad postures in the public Theme #13 formulation are **Normal** (continue under a sufficiently qualified frame), **Containment** (reduce exposure, autonomy or scope while preserving a known workable frame), and **Migration / Regime Transition** (prepare for a possible critical bifurcation and transition toward an as-yet unknown or newly qualified frame when the existing mapping cannot be relied on). Preparation, invariant safety or containment must not be mistaken for authorization to perform ordinary mission operations in an unqualified destination. They are *top-level postures*, not a mandatory finite-state machine or exhaustive catalogue of actions; controls inside them remain bounded by evidence and legitimate authority. Incompatible local closures—HOLD, distinct emergency responses and continued NORMAL operation—can coexist during a transition. Their divergence is an ecosystem-level warning signal, not proof by itself of a global state.

EA therefore tracks the validity and freshness of selected windows, dependency assumptions, human and technical capacity, qualified response mappings and the unresolved state carried through participant handoffs. It requalifies the frame when necessary without claiming to enumerate Ω or reconstruct the complete ecosystem. Ecosystem change can increase, decrease or restructure operational uncertainty; the residual must not be represented as a fixed weight. This extension reads with unchanged v0.4 §§7, 9, 17 and 18.

#### Detailed source derivation for 1.2 — agentic ecosystem dynamics and regime transition

#### Source v0.4 §7 — Why agentic ecosystems intensify the residual problem

##### 7.1 Ω becomes larger and more dynamic

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

##### 7.2 More agents do not automatically mean more uncertainty

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

##### 7.3 Recursive local correctness can still produce systemic indeterminacy

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

#### Source v0.4 §17 — Failure taxonomy extension and regime-transition amplification

##### 17.1 One structural condition and two failure classes

The preceding analysis distinguishes two failures of uncertainty management. This section adds a structural Type 0 so that the taxonomy separates what cannot be removed by correct local management from what is caused by incorrect uncertainty management.

&nbsp;

Condition Type 0 — structural non-determination

Type 0 is not a management error. It is the condition in which the global property remains non-determined under the available system class even when uncertainty is acknowledged and handled correctly. This includes formally undecidable classes and operationally intractable cases for which no available procedure can produce a sufficiently reliable global determination within the relevant resources and time.

**Foundational distinction; not a runtime oracle.** A formally or otherwise structurally established limit is not the same claim as present-frame infeasibility, and neither follows merely from persistent non-resolution. The first concerns the admitted problem class; the second concerns the declared evidence, capacity and useful response horizon; the third may remain simply unresolved. An operational architecture is not required to know in advance whether more effort would eventually succeed. It is required to preserve the unresolved state, bound further effort and select an authorised posture before the useful horizon expires. A Type-0 marker therefore needs a stated structural or frame-relative basis; otherwise the runtime state remains unresolved rather than being promoted to an ontological conclusion. This clarification adds no failure class and no demand that an agent prove undecidability online.

The failure associated with Type 0 is not its presence but its misclassification. Treating a structurally non-determinable condition as if further effort were guaranteed to resolve it produces Type 1 pressure; treating it as if it were already resolved produces Type 2\. Type-0 controls therefore exist to prevent misclassification and to support restriction, decomposition or requalification—not to remove the structural condition.

&nbsp;

&nbsp;

Type 0 can coexist with useful local decisions. A smaller or more constrained subproblem may become tractable even while the larger ecosystem problem remains unresolved. For example, two vehicles may receive incompatible route-level directions while local collision-avoidance control still prevents impact. The local safety problem has been reduced to a sufficiently small and solvable frame; that does not imply that the global traffic or ecosystem state has become determined.

&nbsp;

Failure Type 1 — unmanaged unresolved contradiction / paralysis

Type 1 occurs when the system recognizes uncertainty but fails to bound the determination effort or define a legitimate closure. It remains in HOLD, escalates indefinitely, or continually expands the observation/search effort.

&nbsp;

Failure Type 2 — suppressed contradiction / false certainty

Type 2 occurs when the system closes by suppressing the unresolved side of the contradiction. It treats a bounded or uncertain result as if it were sufficiently determined for a wider scope.

##### 17.1.1 Type 1 and Type 2 as endpoints with hybrid trajectories

Type 1 and Type 2 remain the two management-failure classes; they are not pure, permanent personalities of a subsystem. A Type-1 path can collapse into Type 2 when a timeout, default, queue pressure, defensive approval or exhausted reviewer forces closure without new qualifying evidence. A Type-2 path can collapse into Type 1 when a confident compressed closure is later contradicted but the discarded uncertainty, alternatives or dependencies cannot be reconstructed, causing repeated HOLD, search or escalation.

False convergence is principally Type 2 when several actors inherit or imitate the same insufficiently supported closure. Divergence can combine Type 1 and Type 2 when some actors remain unresolved while others close falsely. Oscillation is a repeated transition between the two when posture changes lack a material-evidence rule, expiry discipline or hysteresis. A cascade describes propagation or abrupt system-level consequence; it is not a third failure type. Defensive `UNKNOWN`, qualifier saturation and adversarial doubt injection are likewise operational mechanisms: they create Type 1 when they generate unbounded delay or containment, and Type 2 when pressure, habituation or a default suppresses the unresolved state and forces closure.

&nbsp;

The three-way distinction is therefore:

Type 0: structural non-determination despite correct management.

Type 1: uncertainty acknowledged but not bounded into legitimate closure.

Type 2: uncertainty suppressed or promoted into false certainty.

&nbsp;

##### 17.2 Architecture-induced Type 2 through agent cascades

The agentic compression mechanism described earlier maps directly onto Failure Type 2\.

&nbsp;

Suppose upstream agent A reaches an operational closure while retaining uncertainty, scope limitations, unresolved dependencies and provenance. If A transmits only the closure and downstream agent B receives that closure as a determined fact, the architecture has removed the unresolved side of A’s contradiction before B reasons over it.

&nbsp;

B may then behave exactly as a Type-2 system even if B is locally faithful to the information it received.

&nbsp;

This is an architecture-induced Type 2: false certainty created by lossy inter-agent transmission rather than by deliberate downstream disregard.

&nbsp;

The practical implication is important. Ecosystem signaling is not merely descriptive metadata. Preserving boundary, uncertainty, provenance, freshness and unresolved dependency state is a control against architecture-induced Type 2 failure.

&nbsp;

##### 17.3 Systemic divergence under heterogeneous windows

Type 0 and out-of-window indeterminacy can produce a systemic condition in which locally justified closures become mutually incompatible.

&nbsp;

Under the same global ecosystem condition, different participants may rationally reach:

HOLD

Emergency Plan A

Emergency Plan B

NORMAL

&nbsp;

The critical point is that these local closures do not have to be individually irrational. Each may be justified inside its own observation window and local control model.

&nbsp;

The systemic error surface appears when local confidence is mistaken for ecosystem-level determination, or when the system lacks sufficient shared knowledge about the scope, freshness and uncertainty of the different windows.

&nbsp;

High local confidence can therefore coexist with low global determination.

&nbsp;

This is not eliminated by adding more agents by itself. More agents can add information, but they can also add more heterogeneous windows, more compression boundaries and more incompatible locally valid closures unless the ecosystem-level state is sufficiently qualified.

&nbsp;

##### 17.4 Regime change — transition beyond the qualified operating envelope

For this architecture, “regime change” is a defined technical term. It does not mean ordinary movement between already characterized operating states.

Let Q denote the currently qualified operating envelope. Inside Q, the ecosystem may contain multiple known operating modes M₁, M₂, …, Mₖ. Each mode has sufficiently characterized applicability conditions and a qualified response mapping from relevant inputs or states to expected actions, counter-actions or controls.

A transition from Mᵢ to Mⱼ while both remain inside Q is therefore a mode change, not a regime change. The system may alter behavior substantially, but it is still operating inside a known response space.

A regime change occurs when the ecosystem moves to a state for which the currently qualified envelope can no longer establish a sufficiently valid mission-level response mapping. Formally, if x denotes the current ecosystem state, a regime change is present when x leaves Q, or when membership in a qualified mode and the validity of its response mapping can no longer be established to the required degree.

Operational definition:

A regime change is a transition from a qualified operating envelope into an unqualified ecosystem state in which the correct mission-relevant response mapping is not yet sufficiently known or qualified.

**Foundational terminology boundary.** Evidence that observable dynamics have departed from a declared regime and a conclusion that a decision frame no longer supports its former response mapping are related but distinct claims. A Regime Awareness detector may supply representation-relative departure evidence for a specified observation map, context and threshold; EA assesses what that evidence, together with other dependencies, means for one mission-level decision frame. Neither claim requires access to a unique, globally observable “true regime,” and neither may be inferred solely from the other. This is an explanatory distinction, not an additional runtime state or detector requirement.

Accordingly, a test must predeclare which proposition it measures: **dynamical departure** from characterized state-transition or statistical behaviour, **decision-frame invalidation** of the former response mapping, or both. Increased uncertainty alone does not establish dynamical departure, and a detected departure alone does not establish that the mission response mapping has failed. Where only the second is evidenced, the operational record should say `decision-frame invalidation` or `insufficiently qualified frame` rather than using regime change as a self-validating label.

Under this definition, uncertainty is not merely a common consequence of regime change. It is its epistemic signature. If the correct response mapping for the new state were already sufficiently known and qualified, the transition would belong to the known operating envelope and would be classified as a mode change instead.

The uncertainty may be brief. A regime change can be abrupt and externally clean: immediately before the transition the current mode and response mapping are valid; immediately after it, the system can recognize that the previous mapping is no longer sufficient without yet knowing which new mapping is correct.

This is the point at which the transition can become a potential critical bifurcation. Multiple response paths may become locally plausible before the new state is sufficiently qualified, and different participants may therefore select incompatible closures. “Potential critical bifurcation” is used here operationally; it does not claim that every regime change is a mathematical bifurcation.

The resulting uncertainty may appear both inside and outside the observation window. The event itself may be visible inside W while the correct response relation is unqualified, and simultaneously relevant causes, dependencies or consequences may remain out of window. Regime change therefore need not begin out of window, although out-of-window exposure can materially increase during the transition.

A regime change also does not imply that no safe action is possible. Invariant controls may remain qualified across regimes: stopping, collision avoidance, containment, rate limiting or another conservative safety posture may still be valid. Knowing a safe fallback is different from knowing the correct regime-specific mission response.

The regime-change interval ends, for operational purposes, when the ecosystem has been requalified sufficiently for the active mission: the relevant state can again be mapped into one or more qualified operating modes with bounded uncertainty and justified response rules.

##### 17.5 Regime-transition amplification of Failure Types 0, 1 and 2

A regime transition can amplify the structural Type 0 condition and both failure classes.

&nbsp;

Type 0 amplification: by definition, a regime change creates at least a temporary structural non-determination of the mission-level response mapping until sufficient requalification is achieved. This does not imply that every action is unknown, because invariant safety or containment controls may remain qualified.

&nbsp;

Type 1 amplification: systems that are highly sensitive to uncertainty may enter widespread HOLD, escalation or search expansion as both local and out-of-window indeterminacy increase.

&nbsp;

Type 2 amplification: systems that continue to apply previously qualified windows, response mappings, closure rules or compressed upstream decisions after the state has left their validity envelope may produce confident but invalid actions.

&nbsp;

The especially dangerous case is mixed-mode propagation: one part of the ecosystem enters HOLD, another executes Emergency Plan A, another executes Emergency Plan B, and another continues NORMAL operation. Local safety mechanisms may prevent some immediate failures, but the ecosystem can remain globally incoherent.

&nbsp;

##### 17.6 Why Ecosystem Awareness exists

This gives Ecosystem Awareness a more precise root problem.

&nbsp;

Ecosystem Awareness does not eliminate structural indeterminacy and cannot make an undecidable global problem decidable.

&nbsp;

Its role is to determine whether the current ecosystem frame remains sufficiently qualified for justified operation; to detect when observation windows, dependencies and closure assumptions are losing validity; and to support containment, restriction, requalification or migration into a smaller or newly qualified operating frame.

&nbsp;

When a previously global Type-0 exposure becomes operationally manageable, the reason is not that structural undecidability disappeared. The active mission has been restricted, decomposed or requalified into a domain in which sufficient determination and safe closure are again possible.

&nbsp;

The central control objective is therefore:

&nbsp;

Do not confuse local solvability with global determination, and do not continue operating under a regime whose observation window and closure assumptions are no longer sufficiently qualified.

&nbsp;

This is the point at which Ecosystem Awareness becomes a system-level control function rather than an information-sharing feature.

&nbsp;

##### 17.7 Why out-of-window indeterminacy matters now — two aggravants

&nbsp;

The current importance of out-of-window indeterminacy is driven by two different aggravating mechanisms that should remain conceptually separate.

&nbsp;

Structural aggravant — ecosystem expansion, churn and generativity

&nbsp;

The decision-relevant ecosystem is becoming harder to bound because the number of agents, services, dependencies and interaction paths can increase, while their operational lifetime and validity can shorten. Agentic participants may also generate new behaviours, delegations, response strategies and dependency structures during operation. The relevant state space is therefore not only potentially larger; it can be reconstituted more rapidly.

&nbsp;

A useful working formulation is:

&nbsp;

decision-relevant state space ↑

observation-window validity lifetime ↓

out-of-window exposure and invalidation pressure ↑

&nbsp;

This does not mean that adding agents automatically increases uncertainty in every system. It means that, under fixed observation, verification and communication capacity, increasing scale, churn and generativity can increase both the amount of potentially decision-relevant state outside the active window and the rate at which a previously sufficient window loses validity.

&nbsp;

Architectural aggravant — Type-2 multiplication through agentic compression

&nbsp;

The second aggravant is architectural rather than structural. Where agent boundaries transmit closure without preserving the uncertainty, scope, provenance, freshness or unresolved dependencies that qualified that closure, the downstream architecture converts bounded uncertainty into apparent determination.

&nbsp;

In simplified form:

&nbsp;

closure \+ uncertainty \+ scope → closure

&nbsp;

Repeated recursively, this acts as a Type-2 multiplier. The downstream agent may remain locally faithful to its received input while the architecture as a whole progressively removes the epistemic qualifications required to interpret that input correctly.

&nbsp;

Candidate coordination-distortion hypothesis

&nbsp;

Under comparable underlying evidence, honest propagation of uncertainty should require greater epistemic separation between participant windows before strongly incompatible operational closures emerge. Type-2 compression may lower that threshold: by collapsing uncertainty into apparently determined binary outputs, a smaller or less heterogeneous ecosystem may reproduce systemic divergence similar to that which structural Type-0 non-determination would otherwise require under much greater separation.

The same compression can also produce the opposite visible pattern: premature convergence on one unsupported closure when actors reuse correlated evidence, observe one another's actions or treat prior closures as stronger than their own residual information. Subsequent contradiction may reopen that Type-2 convergence as Type-1 search/HOLD, generate oscillation, or produce an abrupt cascade when several dependent closures reverse together. Which pattern appears depends on source dependence, window heterogeneity, communication topology, authority, payoff and arbitration rules. Divergence, false convergence, oscillation and cascade are therefore candidate observable trajectories of Type 1/Type 2 management failures, not additional error classes.

&nbsp;

This is a research hypothesis, not an established law. It can be tested by varying ecosystem size, window heterogeneity, source correlation, propagation depth, uncertainty preservation, compression rate, timeout/default policy and arbitration rules, and measuring false convergence, incompatible closures, Type-1/Type-2 transitions, oscillation and cascade onset.

&nbsp;

Mission-critical severity — when HOLD is not a safe terminal state

&nbsp;

Failure Type 1 remains epistemically distinct from Type 2\. Type 1 fails to reach bounded closure; Type 2 reaches unjustified closure. However, in mission-critical systems their operational consequences can converge if HOLD is not itself an admissible safe terminal state.

&nbsp;

If a process must continue and no qualified human, controller or safe fallback takes over, a prolonged HOLD eventually yields control to something else: a timeout, lower-level controller, environmental dynamics, fallback mechanism, external actor or uncontrolled state transition. The original uncertainty remains unresolved while operational authority changes.

&nbsp;

Therefore the structural Type 0 condition and the two failure classes remain distinct:

&nbsp;

Type 0 — structural non-determination despite correct management.

Type 1 — uncertainty acknowledged but not bounded into legitimate closure.

Type 2 — uncertainty suppressed or promoted into false certainty.

&nbsp;

But under sufficient mission criticality they can converge on the same ecosystem-level consequence: loss of coherent coordinated control. Local safety mechanisms may still prevent individual failures, but local solvability does not establish that the ecosystem remains coherently controlled.

&nbsp;

### 1.3 Integration and boundaries with neighbouring approaches

The two origins are **independent but coupled**. In a stable ecosystem, residual non-determination, finite capacity and false closure can still matter. In a changing ecosystem, a previously qualified dependency or response mapping may expire even if the local actor reports no newly discovered uncertainty. Together they require an architecture that selects a mission- and risk-sensitive **minimum sufficient observation and control position**, preserves residual and inherited uncertainty, and repeatedly tests whether the operating frame remains sufficiently qualified. “Minimum” does not mean a fixed smallest sensor set or least governance effort: what is sufficient changes with consequence, reversibility, response horizon, evidence freshness and capacity. More awareness is not automatically better; less is not automatically safer.

The working distinction in the [Theme #13 comment, §2.1](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5585387513) is specifically **system security versus ecosystem security**. System security asks whether a local system, component, interaction or action satisfies identity, authority, policy, attestation and applicable control requirements. Ecosystem security asks whether surrounding dependency and capacity conditions still make that locally valid action appropriate and sufficiently supported. “Systemic” describes a cross-system condition or consequence; it should not silently replace “system security” in this distinction. This is a research-working distinction, **not a proposed normative taxonomy**, and local correctness does not establish ecosystem-level validity.

EA does not replace cybersecurity, supply-chain risk management, systems-of-systems engineering, observability/telemetry, context engineering, uncertainty quantification, provenance, distributed sensing, adaptive control, resilience, incident exchange, reputation, Byzantine fault tolerance or human oversight. Each addresses a real portion of the problem. The candidate contribution is a **functional composition and interoperability capability**, which may be distributed across existing control mechanisms rather than installed as a mandatory module, data format or central control plane. It selects and qualifies mission-scoped evidence, composes assessments, and requests targeted control requalification through actors holding the relevant authority; a small, scope-qualified representation can carry whether a determination remains sufficient, what frame produced it, what residual or inherited uncertainty remains, what has changed, and which actor retains authority to act. Epistemic positions are domain- and scope-indexed and are not fungible: a control in domain d2 cannot cancel an epistemic fault in d1 without a demonstrated coupling. Multiple pathways are not independent corroboration merely because they are numerous; they may share upstream evidence, and unknown source dependence remains UNKNOWN. This functional capability must be implementation-neutral and preserve source-native semantics; it is not a demand that every external component be relabelled into EA states.

Context engineering already establishes the value of finite context selection. Multi-agent confidence and uncertainty studies show that calibrated signalling can change outcomes and that poorly calibrated confidence can cause premature convergence. Propagation-aware uncertainty work is a close precedent for retaining inherited uncertainty through communication graphs. Provenance representations and A2A interoperability provide adjacent substrates, not by themselves a decision-scoped ecosystem qualification function. Signals may be cooperative, competitive, deceptive or adversarial; their freshness, source diversity, provenance, scope and epistemic limitations must be assessed. The possibility of incentive or evolutionary effects in competing ecosystems remains a hypothesis for study, not an established benefit of EA.

### Neighbouring architectures and EA's candidate differential

**EA's potentially differential contribution is the coupling of four functions into a decision-scoped, requalifiable architectural contract across independently governed components:** (1) select and qualify only the evidence material to the declared mission and response window; (2) preserve open residual, inherited uncertainty, scope and source dependence when results cross boundaries; (3) test whether the ecosystem/dependency frame and available human–technical capacity still justify the receiving decision; and (4) request the smallest relevant requalification or control review when that support changes, while leaving authorization and execution with their owners. The functional contract may be distributed across existing mechanisms; it does not require a new central controller, universal ontology or mandatory protocol.

That combination is more specific than mentioning “ecosystems” or adding another uncertainty score. It asks whether a locally correct and authorized result is **still mission-sufficient in the current ecosystem frame**, and carries the answer's limits forward so that another component cannot silently widen its claim. Existing architectures address important parts of this problem; EA proposes an explicit composition and handoff point for their results. Whether a peer integration already meets the same obligations, and whether EA improves outcomes beyond it, must be tested rather than assumed.

| Neighbouring approach | Existing architectural treatment or capability | Question EA adds to the comparison |
|---|---|---|
| [Systems-of-systems engineering (INCOSE)](https://www.incose.org/docs/default-source/se-vision-2025/se-vision-2025/incose-se-vision-2025.pdf?sfvrsn=602663c7_2) and [systems-security engineering / resilience (NIST SP 800-160 v2r1)](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final) | Architectural treatment of interdependent systems, emergence, limited control and dynamic verification/adaptation; not a claim of universal deployed practice. | Which evidence and dependency assumptions still justify **this receiving decision** after the relevant frame changes? EA does not claim to originate continual adaptation. |
| [Cybersecurity supply-chain risk management (NIST SP 800-161)](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final) and [ecosystem trust relationships (ITU-T X.1812)](https://www.itu.int/epublications/publication/itu-t-x-1812-2022-05-security-framework-based-on-trust-relationships-for-the-imt-2020-ecosystem) | Ecosystem-level dependencies, trust/security relationships and risk treatment. | Does a locally valid action remain sufficiently supported by the wider **decision-relevant** dependency and capacity frame? “Ecosystem security” is not an EA invention. |
| [Finite context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) and [observability (OpenTelemetry)](https://opentelemetry.io/docs/concepts/observability-primer/) | Curated context, telemetry and diagnosis in distributed operation. | Is the selected window sufficient for the mission, what remains outside it, and when has its validity expired? EA does not claim these fields ignore unknowns. |
| [Uncertainty propagation (PropUQ-MAS)](https://arxiv.org/abs/2608.22130), [W3C PROV](https://www.w3.org/TR/prov-o/) and [PROV-AGENT](https://arxiv.org/abs/2508.02866) | Direct antecedents for inherited uncertainty and agent/workflow provenance. | How do inherited uncertainty and shared upstream lineage affect sufficiency **by domain and scope** under a changing response frame? EA does not invent propagation or provenance. |
| [A2A interoperability](https://a2a-protocol.org/latest/specification/), [RATS attestation architecture (RFC 9334)](https://www.rfc-editor.org/rfc/rfc9334.html), and current RATS work-in-progress on [AR4SI](https://datatracker.ietf.org/doc/draft-ietf-rats-ar4si/) / [EAT Attestation Results](https://datatracker.ietf.org/doc/draft-ietf-rats-ear/) | Extensible exchange between agents plus reusable attestation/appraisal results and contextual frame-of-reference metadata. | What *candidate minimum semantics* should accompany a producer-neutral result so the receiving decision does not silently expand its claim? EHD does not claim result-plus-context carriage as new; its candidate differential is decision-scoped preservation of scope, UNKNOWN and dependency semantics across result types beyond attestation. EHD is not an adopted protocol or proven minimum. |
| [Adaptive resilience (NIST SP 800-160 v2r1)](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final) and the [Theme #13 incident/signal discussion](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5508513343) | Anticipation, response, recovery and incident signalling/coordination. | What epistemic requalification is needed **with or without an incident** before continuing or requesting an authorised control change? EA does not own containment or incident resolution. |

**Potential benefits, if the coupled functions are implemented and validated, are concrete:** fewer false ecosystem-level closures when local verdicts or duplicated evidence are overgeneralized; less wasted observation, search, escalation and control effort by directing capacity to decision-relevant gaps; more useful cross-vendor or cross-agent handoffs because scope, provenance, residual and validity travel with a result without exposing private reasoning; and faster, narrower requalification after material change rather than automatic whole-workflow restart or indiscriminate control expansion. These are testable benefits, not reported effects.

The proposed differential is thus an identifiable **functional composition and interoperability surface**, not a claim to have invented uncertainty propagation, observability, resilience or ecosystem security. Comparative validation should ask whether this joint contract is absent, equivalent or better implemented in a concrete peer architecture, and whether the expected benefits appear under matched cases. The frozen v0.4 benchmark's peer observations remain bounded to its reviewed set; they neither prove exclusive novelty nor erase the architectural proposition.

The incident/signal line currently discussed under Theme #13 and EA are candidate independently testable mechanisms; the precise Theme boundary remains open to contributor confirmation. Incident signals can inform EA's assessment of context, affected scope, blast radius and response window; EA can return a decision-scoped qualification, explicit UNKNOWN, capacity constraint or targeted requalification request. Neither assessment nor signalling grants containment or “kill switch” authority. An operational dependency graph and an epistemic dependence graph may reuse evidence without merging ownership. The **general EA architecture** is not restricted to Theme #13 or any one focus group's ToR; that thread is a public implementation/interface discussion and provenance anchor.

This is an architectural research proposition, not evidence of effectiveness, universal necessity, standards adoption, certification or exclusive novelty. Its testable questions include whether explicit scope/residual preservation reduces false certainty, whether bounded window selection avoids unproductive determination effort, and whether requalification detects frame invalidity early enough to support an authorized response. Existing standards and neighbouring research narrow rather than erase the claim. References in the Theme #13 comment include the [NIST cyber-ecosystem glossary](https://csrc.nist.gov/glossary/term/cyber_ecosystem), [NIST system-of-systems glossary](https://csrc.nist.gov/glossary/term/system_of_systems), [ITU-T X.1812](https://www.itu.int/epublications/publication/itu-t-x-1812-2022-05-security-framework-based-on-trust-relationships-for-the-imt-2020-ecosystem) and [NIST SP 800-161 Rev. 1 Update 1](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final). The comment's selected research references and the unchanged v0.4 §14 remain the detailed neighbouring-work routes.

#### Detailed source derivation for 1.3 — EA discipline, hypotheses, measurements and boundaries

#### Source v0.4 §8 — Ecosystem Awareness

##### 8.1 Problem statement

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

##### 8.2 What Ecosystem Awareness must preserve

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

##### 8.3 Ecosystem signaling is mitigation, not resolution

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

##### 8.4 Current working gap hypothesis

The predecessor review identifies many neighboring mechanisms: observability, uncertainty quantification, provenance, supply-chain visibility, trust relationships, multi-agent uncertainty communication, signaling and resilience.

&nbsp;

The current working hypothesis is narrower:

&nbsp;

there is not yet a clearly established architectural mechanism in the reviewed corpus whose primary object is continuous qualification of the boundary between U and a rapidly changing Ω, while explicitly retaining R as an operationally relevant state.

&nbsp;

This should remain a research-gap hypothesis, not an assertion that no such mechanism exists anywhere.

&nbsp;

#### Source v0.4 §9 — Operational closure and ecosystem posture

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

#### Source v0.4 §10 — Architectural principles

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

The system may need to act without pretending that unresolved conditions were determined.

&nbsp;

Principle 6 — The two fundamental management failure types are paralysis and false certainty.

Every uncertainty-control design should be tested against both management failure types while separately preserving any correctly represented Type 0 structural condition.

&nbsp;

Principle 7 — Compression can reduce visible local uncertainty while increasing hidden residual.

A cleaner downstream message is not necessarily a better-informed downstream decision.

&nbsp;

Principle 8 — Signaling preserves; it does not create knowledge.

Communication can reduce avoidable loss but cannot eliminate the structural open residual beyond any current bounded representation.

&nbsp;

Principle 9 — Awareness should be bounded, risk-indexed and capacity-aware.

More observation is not automatically better. Observation, verification, communication and human attention have costs. A larger window is justified only when the expected reduction in decision-relevant exposure is material relative to those costs and the remaining response horizon.

&nbsp;

Principle 10 — The correct target is minimum sufficient ecosystem awareness.

The required awareness budget depends on mission criticality, sensitivity to ecosystem change, consequence severity, reversibility, tolerated residual, observation/determination capacity and available response capability. The target is dynamic: the same mission may need a different W(d,t) as ecosystem sensitivity, capacity or response options change.

&nbsp;

<a id="candidate-research-hypotheses"></a>

<a id="candidate-research-hypotheses"></a>
#### Source v0.4 §11 — Candidate research hypotheses

**Domain-scoped reading rule (applies to H1–H6; it is not a seventh hypothesis).** In this section, a **[decision domain](#decision-domain)** `d` is the material subject–proposition–decision boundary for which evidence and a result are being qualified. It is not the whole enterprise, the whole ecosystem or every item of context that a system could retrieve. **[Scope](#scope)** states the coverage to which a claim applies. Each hypothesis is therefore evaluated for a declared decision `d`, time `t` and active [`W(d,t)`](./00_CANONICAL_ARCHITECTURE_TOPOLOGY.md#1-canonical-topology), under comparable evidence and finite compute, bandwidth, time, privacy and human-attention capacity.

**Cross-domain non-fungibility.** A result, control or additional context in domain `d1` does not improve, compensate for or close an epistemic gap in domain `d2` unless a material dependency between them is established and the new evidence actually requalifies `d2`.

**Non-monotonicity of context growth.** Increasing tokens, observations, signals, agents or retrieved context is not monotonically equivalent to increasing decision-relevant determination. Expansion outside the material domain can consume the time and capacity required to preserve or improve the original A–D position: sufficiently determined state can become stale or unresolved, potentially obtainable state can fall beyond the useful response horizon, structural residual remains, and the remaining response capacity decreases. A system may therefore hold more raw information while occupying a worse decision state. This is an explanatory consequence of H5 and H6, not an additional hypothesis and not a claim that every context expansion is harmful.

##### H1 — Boundary-aware local closure

Systems that explicitly represent insufficient determination inside U and finite determination resources will avoid some deadlock and false-certainty failures that arise when every local closure is forced into a binary determined state.

&nbsp;

##### H2 — Residual-scope explicitness

Separating confidence conditional on U from the open residual R\_U beyond that bounded representation will reduce unjustified local-to-global confidence inflation in downstream decisions.

&nbsp;

##### H3 — Compositional residual expansion

Under comparable underlying evidence and computational resources, systems in which critical downstream decisions depend solely on lossy compressed representations will exhibit greater hidden residual and/or false confidence than systems with better context preservation or independent-source access.

&nbsp;

##### H4 — Bounded preservation

A bounded determinacy/context envelope can preserve enough decision-relevant information to reduce architecture-induced residual without requiring disclosure of full internal state.

&nbsp;

##### H5 — Dynamic ecosystem pressure

For a fixed observation and verification budget, increasing participant/dependency churn and shortening ecosystem-state validity will increase the operational importance of residual-state preservation and requalification even when local algorithms remain unchanged.

&nbsp;

##### H6 — Risk-capacity calibrated window selection

Systems that adapt observation-window breadth, freshness and determination effort to mission sensitivity, consequence severity, available capacity and response horizon will achieve a better risk/resource frontier than systems using either fixed broad observation or fixed narrow observation under otherwise comparable conditions.

&nbsp;

**Domain-qualified interpretation of the unchanged hypotheses**

| Hypothesis | Reading by declared decision domain |
|---|---|
| **H1** | Assess local closure separately for each material domain `d`. Explicit unresolved state and capacity limits remain attached to the decision they qualify; determination elsewhere does not turn this closure into a justified binary result. |
| **H2** | Confidence remains conditional on U and `W(d,t)` for the declared domain. Confidence in `d1` cannot be promoted to global confidence or used to cancel residual uncertainty in `d2`. |
| **H3** | Compare systems for the same downstream decision domain and under comparable evidence and resources. A representation is materially lossy when it drops scope, provenance, dependency, freshness or unknowns that could change that decision. |
| **H4** | The bounded envelope is defined for the declared domain and carries the minimum A–D qualification and reliance conditions needed downstream. “Bounded” does not mean universal context or disclosure of full internal state. |
| **H5** | Churn pressure is evaluated in each material domain and dependency capable of invalidating the current frame. It justifies targeted preservation and requalification, not indiscriminate global refresh. |
| **H6** | Window breadth, freshness and determination effort adapt for each domain and decision according to risk, capacity and response horizon. A better frontier means better support for the same scoped decision under comparable conditions, not maximum observation. |

These are research hypotheses, not established results.

&nbsp;

#### Source v0.4 §12 — Candidate measurements

Possible measurements carried forward and reorganized under this model include:

* local determinacy margin;  
* frequency of explicit indeterminate outcomes;  
* human-capacity binding and escalation demand;  
* time spent in HELD or unresolved states;  
* evidence and sample coverage inside U;  
* known versus unmeasured dependencies;  
* estimated rate of U invalidation under ecosystem change;  
* local-to-global confidence inflation;  
* information retained or discarded at inter-agent boundaries;  
* number and criticality of downstream decisions dependent on one compressed source;  
* source diversity and primary-source retrievability;  
* propagation depth of compressed closures;  
* inherited-indeterminacy detection;  
* systemic decision error;  
* false confidence caused by recursive closure reuse;  
* freshness and staleness;  
* latency, bandwidth, privacy and disclosure cost;  
* containment frequency and recovery success;  
* observation-window breadth and churn by domain;  
* compute, token, bandwidth, latency and privacy cost attributable to awareness;  
* human attention consumed by escalation, verification and context requests;  
* capacity depletion caused by repeated Type-1 determination effort;  
* missed ecosystem changes attributable to Type-2 under-observation;  
* risk/sensitivity mismatch between the qualified window and observed downstream consequences;  
* and marginal decision value obtained from additional context or corroboration where measurable.

&nbsp;

#### Source v0.4 §13 — Claim boundaries

This architecture does not claim:

* that probability and indeterminacy are synonyms;  
* that every residual is quantifiable as probability mass;  
* that Ω can be exhaustively enumerated;  
* that every system-level property is formally undecidable;  
* that more agents automatically imply more information loss;  
* that distributed systems are inherently inferior to monolithic systems;  
* that ecosystem signaling creates knowledge nobody possesses;  
* that complete ecosystem-state sharing is desirable;  
* that Ecosystem Awareness replaces observability, uncertainty quantification, provenance, formal methods, resilience, incident exchange, trust management or human oversight;  
* or that FG-TIDA, NIST or another standards body has adopted this architecture.

&nbsp;

**The narrower claim is:**

&nbsp;

**Agentic systems require an architecture that distinguishes uncertainty among defined entities inside U from the open decision-relevant residual R\_U relative to that bounded representation; manages both without falling into paralysis or false certainty; and recognizes that compositional compression and rapid ecosystem evolution can expand or conceal the residual even when local decisions remain individually justified.**

&nbsp;

#### Source v0.4 §14 — Foundations and neighboring anchors carried forward

The predecessor architecture identified the following anchors for later formal development:

&nbsp;

The 6–8 September deep conceptual lineage — including the Objective Envelope, MCA, Good Enough Early Warning, Semantic Window, Level-1/Level-2 adaptation and signalling-without-required-cooperation formulations — is preserved separately in “Ecosystem Awareness — Deep Conceptual Lineage and Derivation Map”. These are explanatory/research antecedents unless explicitly mapped into the current architecture.

* Turing — computability limits and the hard boundary of general effective decision procedures;  
* Rice — undecidability of non-trivial semantic properties of programs in general;  
* Cover & Thomas — information theory and the Data Processing Inequality;  
* NIST cyber-ecosystem and system-of-systems concepts;  
* NIST SP 800-161 — distributed ICT/OT supply-chain risk and visibility limits;  
* ITU-T X.1812 — ecosystem trust relationships, stakeholders and security boundaries;  
* context engineering — context as a finite resource to curate rather than maximize;  
* DebUnc and ConfMAD — explicit uncertainty/confidence communication in multi-agent settings;  
* Demystifying Multi-Agent Debate — confidence and viewpoint diversity;  
* PropUQ-MAS — propagation-aware inherited uncertainty across multi-agent communication graphs.

&nbsp;

These anchors do not establish the full Ecosystem Awareness architecture. They constrain the claims and provide established foundations for individual parts of the problem.

&nbsp;

#### Source v0.4 §15 — Next theoretical step

The next step is not to invent a new metric immediately.

&nbsp;

The next step is to formalize the relationship among:

* U — the explicitly represented operational universe;  
* R\_U — the open decision-relevant residual relative to the bounded representation U;  
* D — finite determination capacity;  
* C — operational closure;  
* and M — inter-agent representations that may preserve or discard decision-relevant state.

&nbsp;

**The central research question is:**

&nbsp;

**What is the minimum information about U, R, determination capacity, ecosystem sensitivity, observation cost and inherited uncertainty that must be preserved across agent boundaries so that a system can select and requalify a minimum-sufficient W(d,t), reach justified operational closure, and avoid both resource-exhausting Type 1 and exposure-inflating Type 2 as Ω changes?**

&nbsp;

**That question is the theoretical core of Ecosystem Awareness.**

&nbsp;

&nbsp;

#### Source v0.4 §18 — Ecosystem Awareness as an architectural discipline for uncertainty management

&nbsp;

##### 18.1 Core definition

Ecosystem Awareness is not an attempt to know or reconstruct the complete ecosystem. It is an architectural discipline for managing uncertainty correctly across the current observation window and the decision-relevant state that remains out of window.

&nbsp;

Its purpose is to maintain justified operation by continuously determining whether uncertainty is being represented, propagated and managed in a way that correctly represents structural Type 0 and avoids the two management failure classes defined above:

&nbsp;

Type 0 — structural non-determination: the current frame does not support sufficient determination of the mission-level problem even under correct uncertainty handling.

Type 1 — unbounded unresolved uncertainty: the system recognizes the uncertainty but fails to reach a legitimate bounded closure.

Type 2 — false certainty: the system suppresses, loses or overextends uncertainty and closes as if sufficient determination existed.

&nbsp;

The operational role of Ecosystem Awareness is therefore not to eliminate all uncertainty. It is to detect which of these conditions is present and apply the appropriate architectural response: reframe or requalify for Type 0, establish bounded closure for Type 1, and restore uncertainty, scope and provenance for Type 2\.

&nbsp;

##### 18.2 In-window uncertainty management

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

##### 18.3 Out-of-window uncertainty management

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

##### 18.4 Uncertainty must remain a dynamic state variable

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

##### 18.5 Ecosystem Awareness as principles, not a mandatory named component

Ecosystem Awareness should not be defined as a single software module, product, protocol or control plane that every system must explicitly identify by name.

&nbsp;

It is better treated as a set of architectural principles and control requirements that can be implemented through different mechanisms depending on the system.

&nbsp;

A system may satisfy Ecosystem Awareness through combinations of Human Capacity Awareness, adaptive context selection, uncertainty-preserving inter-agent messages, freshness and provenance controls, bounded search and escalation, requalification triggers, independent observation, safe fallback, containment and other mechanisms.

&nbsp;

The common requirement is that these mechanisms jointly preserve the distinction between what is determined, what remains uncertain inside the current window, what may remain decision-relevant outside the window, and whether the current operating frame is still sufficiently qualified.

&nbsp;

##### 18.6 Minimal architectural statement

Ecosystem Awareness is the set of architectural principles and control mechanisms by which a system maintains justified operation through the correct management of uncertainty inside and outside its current observation window, including detection and handling of Type 0, Type 1 and Type 2 conditions and requalification of the decision frame when its assumptions cease to be sufficient.

&nbsp;

## Reader's dictionary — scope-qualified, non-normative

This dictionary is a reader aid, **not** an EA taxonomy imposed on other Themes, a replacement for their producer-owned terminology, a protocol specification, or evidence of FG-TIDA agreement. Terms from the v0.4 theory describe the current **working EA model**; Theme-numbered entries below are **provisional EA-side readings**, open to correction by their producers. Different local states must remain distinguishable when they cross a boundary. The cross-Theme discussion draft used to check these distinctions is not posted and is neither quoted here as public provenance nor linked as a published artifact.

### A. Foundational and temporal terms

- **Ecosystem:** A dynamic mesh of materially interdependent participants, dependencies and conditions. It need not be a single system, reciprocally beneficial network or centrally governed entity.
- **Ecosystem Awareness (EA):** The distributed-capable architectural function that tests whether the present decision frame remains sufficiently qualified and manages uncertainty inside and beyond its selected observation window. It does not imply a mandatory named software module.
- **Ω (open decision-relevant class):** Potentially material actors, conditions, dependencies and configurations. Ω is not assumed closed or exhaustively enumerable.
- **U (represented operational universe):** The bounded set of entities, variables, sources, actors and controls explicitly included in the current decision model.
- **R_U (open residual relative to U):** Potentially decision-relevant state not represented in U, including state not yet enumerated or categorized. It is not a computed, complete set complement.
- **W(d,t) (observation window):** The selected, time-sensitive information boundary for decision `d`; it can be expanded, restricted or requalified, but not costlessly.
- **Inside-U uncertainty:** An identified entity or determination inside U remains unresolved—for example a named but unavailable authorised human, a noisy sensor or contradictory evidence.
- **Out-of-window uncertainty:** Decision-relevant state may lie beyond W/U; some of it may be recognized as potentially obtainable, and some may remain structural residual.
- **Four epistemic positions (Poles A–D):** Sufficiently determined; explicitly unresolved; recognized potentially knowable beyond the active window; and structural residual. These are decision-relative qualifications, not equal proportions or a closed partition of Ω.
- **Type 0 (structural non-determination):** A mission-level/global property cannot be sufficiently determined under the available class, resources or response horizon despite correct uncertainty management. This is a condition, not a third management failure; restricted local subproblems may still be solvable.
- **Type 1 (unbounded non-closure):** Uncertainty is acknowledged but search, HOLD or escalation lacks a bounded legitimate escape condition and may exhaust compute, time or human capacity.
- **Type 2 (false closure):** Missing or inherited uncertainty, stale scope or a material dependency is suppressed so an insufficiently supported result appears certain or globally valid.
- **Minimum sufficient awareness/control:** The observation, determination and control position adequate for *this* mission and risk, feasible within finite capacity and time. It is neither maximum information nor a universal smallest configuration.
- **Qualified operating envelope Q:** The currently supported range of operating conditions/modes for which applicability and mission-relevant response mappings have sufficient evidence.
- **Regime change:** A transition in which Q no longer supports a sufficiently valid mission-level response mapping. Ordinary change within Q is not automatically a regime change.
- **Requalification:** Renewed assessment of the evidence, dependencies, window, capacity and response mapping needed to justify a decision or renewed operation. Incident resolution or another actor's approval does not by itself complete it.
- **Normal / Containment / Migration–Regime Transition:** Broad, decision-scoped operating postures: continue in a qualified frame; reduce exposure/scope while preserving a workable frame; or prepare for a possible critical bifurcation and a still unknown or newly qualified frame. They are not an exhaustive action list and do not themselves grant enforcement authority.
- **Posture(D_receiver):** Posture indexed to the receiving decision's mission, scope and evidence. Different receivers may legitimately have different postures; no global posture or scalar EA score follows automatically.
- **Response window / response capacity:** Time in which new evidence can still alter the outcome, and the available technical and human ability to observe, decide and act. Further inquiry can consume both.
- **Epistemic versus operational closure:** A system may legitimately restrict, defer, contain or hand off an operation while acknowledging unresolved knowledge; an operational outcome is not proof of epistemic certainty.

### B. Producer-owned states — provisional EA-side readings

The labels below remain owned by the producing Theme. They are not interchangeable synonyms for generic “uncertainty” and must not be silently transformed into an EA verdict.

- **Theme #6 `INDETERMINATE` (action-side conformance):** The relevant evaluation occurred, but its evidence/reference/scope does not sufficiently support an ordinary action verdict. This does not declare the whole ecosystem indeterminate or authority invalid.
- **Theme #6 attested absence of evaluation:** The specified conformance evaluation did not occur and no verdict was issued, with that absence itself legible. This is not #6 `INDETERMINATE`, PASS/FAIL or an evidence-side no-assertion.
- **Theme #22 / RATS-AR4SI `no-assertion` (evidence-side):** The attestation/appraisal path does not assert the claim under the available evidence and appraisal semantics. It is not an action-side conformance result or operational permission.
- **Theme #16 `HELD` (human-oversight lifecycle):** Operation is not currently proceeding while an applicable intervention, authority, evidence or reconciliation condition is handled. The state alone does not say whether the epistemic question is solved.
- **Theme #16 `INDETERMINATE` (execution/admission):** The execution/admission outcome cannot be established after provider entry may have occurred. It blocks blind retry or automatic restoration pending authenticated reconciliation; it is not #16 `HELD` or #6 `INDETERMINATE`.
- **Theme #21 population residual:** A population-level claim remains limited by the declared population, observation architecture and evaluator-family assumptions. A structural limitation is not necessarily cured by more samples; the finding does not choose an operational response.
- **Theme #5/#9 absent, fuzzy or contested authority:** Grant, standing, provenance or scope cannot be established crisply. Downstream approval, conformance or containment must not silently repair that authority basis.
- **Theme #13 incident/signal state:** In the current #13 discussion line, incident detection, signal lifecycle, corroboration/amendment, affected scope, response coordination and locally authorised containment workflow are treated as the incident-side mechanism, independently testable from EA. The precise Theme scope remains open to contributor confirmation.
- **Theme #13 unresolved incident qualifier or edge (`UNKNOWN`):** A material affected-scope, provenance or blast-radius relation is not established. This does not make the entire incident false or become an EA system-level determination.
- **Locally authorised containment:** Execution remains with the actor or mechanism holding the relevant authority. Neither a signal nor an EA assessment creates a new permission, human decision or containment command.

A single action may consistently carry `#6 INDETERMINATE`, `#16 HELD`, `#22 no-assertion` and an established authority basis at the same time. The receiving decision qualifies their *combined significance*; it does not replace their native meanings.

### C. Cross-boundary composition and handoff terms

- **Producer semantics/profile reference:** A versioned reference, or inline equivalent, identifying what the producing mechanism normally means by its fields, evidence boundaries and states. It is not a demand to reveal internal prompts or reasoning.
- **Producer Epistemic Profile:** Stable, source-attributed coverage/claim/qualifier semantics and default validity rules, when such a profile exists.
- **Decision-Relevant Handoff:** The current result's small, decision-material delta against its profile. It should not become a mandatory full-history export.
- **Epistemic Handoff Descriptor (EHD):** A candidate, implementation-neutral semantic handoff whose candidate six-element semantic kernel is: (1) profile/semantic reference and version, (2) subject/proposition/decision domain with scope, (3) producer/issuer, (4) operational result/closure, (5) determination/state kind, and (6) explicit material unknown qualifiers. Values may be `UNKNOWN`; Theme-specific details remain conditional.
<a id="decision-domain"></a>
- **Subject / proposition / decision domain:** Respectively the entity/action concerned, the claim being assessed, and the domain of the receiving decision. Conflating them can promote a source-native result beyond its boundary.
<a id="scope"></a>
- **Scope:** The coverage to which a statement applies. `scope = UNKNOWN` is preferable to invented completeness.
- **Operational result versus determination state:** What happened or was operationally closed is distinct from what the producer established. `HELD`, no-assertion and conformance indeterminacy therefore cannot be flattened into one outcome.
- **Explicit unknown qualifier:** A material property the producer did not establish, such as source independence, affected scope, response reach or freshness. Honest partiality is a usable handoff, not automatic contract failure.
- **Unknown reason versus not applicable:** `not_observed`, `not_tracked`, `unavailable`, `privacy_restricted`, `unsupported` and `not_established` can explain an unknown when known; the reason itself may remain `UNKNOWN`. `not_applicable` is a determination, not an unknown.
- **Conditional qualifier:** Freshness, provenance, confidence, capacity, observation window or similar state carried only when its absence could change the relying decision. It is not a universal required field.
- **Inherited indeterminacy:** Unresolved state or source dependence passed through an upstream actor, conclusion or compressed output. A downstream closure does not erase it.
- **Corroboration versus pathway diversity:** Several reports or acquisition routes are not independent evidence merely because there are many; they may share upstream lineage. Dependence not established remains `UNKNOWN`.
- **Epistemic non-fungibility:** A control or approval in domain `d2` does not compensate for a knowledge fault in `d1` without demonstrated coupling and fresh evidence that actually requalifies `d1`.
- **Operational blast-radius graph:** Incident-side representation of agents, services, actions or assets observed or potentially affected and the response/containment reach.
- **Epistemic dependency graph:** EA-side representation of which relying conclusions inherit uncertainty or dependence across those relationships. The two graphs can share evidence without merging ownership.
- **Affected scope versus decision scope:** What an incident may affect is not automatically the scope for which a receiving decision may rely on a signal.
- **Theme #13 determinacy-envelope profile:** The four context-specific fields `closure`, `determinacy_margin`, `capacity_binding` and `inherited_indeterminacy` can be read as a candidate #13 profile of the more general EHD—not a replacement for the existing Use Case #4 Requirement 20 or a vocabulary required of other Themes. This mapping remains open to contributor confirmation.
- **Targeted requalification request:** A bounded request to refine the particular source, graph branch, evaluation or human path whose resolution could materially change the receiving decision before its response window closes.
- **System security versus ecosystem security:** Working, non-normative distinction: local identity/authority/policy/attestation/control compliance versus whether surrounding dependencies and capacities still support the locally valid operation. “Systemic” describes a wider condition or consequence, not a substitute label for the first term.
- **Source-native ownership:** Each producer retains its verdicts, evidence semantics, authority and decision logic. EA qualifies what those outputs support *for the receiving decision*; it does not score or certify the producer globally.

**Reader rule:** carry the producer's native state, reference, scope and material unresolved qualifiers first; assess the decision-relative significance second; authorize or execute action only through the existing authority path. These three steps are related but not interchangeable.

## Source-control appendix — earlier v0.4 preface and 01A conservation register

The following source-control text preserves the previous paper's framing and the working companion's conservation record. Its historical source-status wording is not the status of this integrated successor.

### Ecosystem Awareness — Foundational Theory of Bounded Uncertainty

#### Working foundational architecture

#### Version: v0.4 working foundational paper — final reconciliation, conservation and readability release

#### 

&nbsp;

### Status and purpose

This document is a new foundational working paper for Ecosystem Awareness. It does not modify or replace the earlier “Ecosystem Awareness — Three Dimensions of Indeterminacy — Working Technical Architecture.” It reorganizes the theoretical core of that work around two uncertainty domains and a separate agentic amplification mechanism.

&nbsp;

This is not an ITU-T deliverable, not evidence of FG-TIDA adoption, and not a NIST submission. It is a working architecture and research object intended to make the problem boundary precise before implementation mechanisms, standardization language, or external submissions are proposed.

&nbsp;

The core claim remains deliberately modest. Probability, uncertainty quantification, computability limits, information loss, systems-of-systems, supply-chain visibility, provenance, resilience and multi-agent signalling are established fields. The candidate architectural contribution is to separate:

* uncertainty inside a bounded, explicitly represented operational universe U;  
* the open residual of decision-relevant state not represented in that bounded universe, denoted R\_U;  
* and the agentic/compositional mechanisms that can make R larger, less visible, or more consequential while simultaneously making local closure appear cleaner.

&nbsp;

The objective is not omniscience. The objective is justified operational closure without confusing local sufficiency with global determination.

&nbsp;

v0.2 governing integration. The epistemic problem is conditioned from the beginning by a second, equally fundamental constraint: the system would benefit from knowing every ecosystem condition capable of materially changing its decision, but it has finite observation, computation, communication, time, privacy and human-attention capacity. Ecosystem Awareness must therefore manage not only what is known and unknown, but also how much of the ecosystem it is proportionate and feasible to bring into the active window for the current mission.

&nbsp;

The resulting target is not maximum awareness. It is a dynamically qualified minimum-sufficient awareness position: wide and fresh enough for the system's current sensitivity to ecosystem change and consequences of error, but bounded enough to remain executable within available determination and response capacity. This integration does not introduce a new failure class. It makes explicit the risk/capacity condition under which Type 0, Type 1 and Type 2 are managed.

Current taxonomy note. The current canonical model distinguishes one structural condition and two failures of epistemic management: Condition Type 0 — structural non-determination despite correct management; Failure Type 1 — uncertainty acknowledged but not bounded into legitimate closure; and Failure Type 2 — uncertainty suppressed or promoted into unjustified certainty. Earlier sections that develop two fundamental failure modes should be read as the derivation of Type 1 and Type 2; Type 0 is a structural condition that the later analysis makes explicit, not a third management failure.

Claim-boundary preview. This architecture does not claim that Ω is exhaustively enumerable, that probability and indeterminacy are synonyms, that every real-world property is formally undecidable, that signaling creates knowledge nobody possesses, that more agents are inherently worse, or that FG-TIDA/ITU-T has adopted this architecture. The full claim-boundary register remains in §13 and governs interpretation of the formal sections.

&nbsp;

Current model at a glance. Ecosystem Awareness is a bounded, continuously requalified capability for maintaining justified operation when the decision-relevant ecosystem is larger, more dynamic and less completely knowable than the representation available to any one agent or system. It keeps four epistemic positions (Poles A–D) distinct — what is sufficiently determined, what is explicitly unresolved, what could potentially be brought into the active window, and what remains structural residual — and calibrates awareness effort to mission sensitivity, consequences, reversibility, finite capacity and remaining response time. The compact normative register is maintained in the Epistemic Safety Principles & Control Matrix; this Foundation explains the derivation and deeper theory.

&nbsp;

Reading note. Sections 1–15 provide the foundational derivation and research framing. Sections 16–18 extend that derivation into recursive window selection, structural Type-0 limits, regime transition and the current operational statement of Ecosystem Awareness. These sections form one model rather than competing definitions.

&nbsp;

&nbsp;

&nbsp;

## Conservation and provenance register

This document is additive. It does **not** move, delete, renumber or edit any frozen baseline file. The mapping below is a reader route and an independent-audit checklist, not a declaration that the new note replaces the mapped text.

| This note | Preserved v0.4 material | Public Theme #13 material |
|---|---|---|
| §1.1 | §§1–6; §8; §§10–16; §§17.1–17.3; §§18.1–18.3, 18.5–18.6; Type 0/1/2, Pole A–D, hypotheses, measurements and claim boundaries | Residual-indeterminacy relation; §3 bounded optimization |
| §1.2 | §§7, 9, 17.4–17.7, 18.3–18.4 | §§1–2 and §2.2: ecosystem, timescale change, system/ecosystem distinction, top-level postures |
| §1.3 | §§6, 8–15, 17–18 and the unchanged Epistemic Safety Principles & Control Matrix, Functional Architecture and Interfaces | §§2.1, 3–4: security distinction, mission-dependent minimum sufficiency, signalling, neighbouring disciplines and selected references |

The 8 September 2026 comment also contains links to public discussions across Themes #6, #10, #13, #16, #18, #19 and #21, a call for foundational use cases, and an explicit reservation of consolidated inputs/outputs and high-level interfaces for later discussion. Those **discussion-history and work-programme statements remain in the comment itself**; this general foundation neither erases them nor turns them into an adopted FG-TIDA architecture. Later architecture/interface work must cite the specific public artifacts and retain the general-versus-Theme-specific boundary.

**Source integrity rule:** the controlled Google Drive freeze/maintenance manifests remain the exact internal anchors for the six v0.4 release-baseline documents. This note is a newly authored public working companion; it has no controlled-freeze status or Drive revision anchor until separately reconciled. The public mirror's completeness status in `CANONICAL_CORPUS_MANIFEST.md` is unchanged by this addition.
