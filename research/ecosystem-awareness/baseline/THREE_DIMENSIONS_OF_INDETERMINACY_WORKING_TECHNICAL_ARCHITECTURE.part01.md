# Ecosystem Awareness — Three Dimensions of Indeterminacy

## Working technical architecture

&nbsp;

# Status and scope

&nbsp;

This is an internal working technical architecture. It consolidates the public FG-TIDA discussion on Ecosystem Awareness and the controlled research notes into a clearer taxonomy of where indeterminacy appears in agentic systems, how each form can be managed well or badly, and why the architecture becomes more important as the surrounding ecosystem changes on operational timescales.

&nbsp;

This is not an ITU-T deliverable, not evidence of FG-TIDA adoption, and not a NIST submission. It should be treated as a working architecture and research object.

&nbsp;

The core claim is deliberately modest: this note does not propose a new theory of uncertainty. Probability, uncertainty quantification, computability limits, information loss, systems-of-systems, supply-chain visibility, provenance, resilience and multi-agent signalling are established fields. The candidate contribution is architectural: separate three distinct dimensions of indeterminacy that are often collapsed together, define their characteristic failure modes, and specify what a system needs to preserve so that operational closure is not mistaken for global certainty.

&nbsp;

# 1\. Architecture at a glance

&nbsp;

The same decision can contain three different kinds of indeterminacy at once.

&nbsp;

Dimension 1 — In-window / local indeterminacy

What can I actually determine from the context, evidence and resources available to me now?

&nbsp;

Dimension 2 — Residual / out-of-window indeterminacy

What relevant state remains outside what I can currently observe, model, measure or enumerate?

&nbsp;

Dimension 3 — Intermediation / compositional indeterminacy

What relevant state may already have been removed, compressed or transformed by the intermediaries through which my information arrived, and how much downstream decision-making depends on those compressed representations?

&nbsp;

These are not maturity levels. They are three locations of indeterminacy. A system may manage one correctly and another badly. Correct operation requires different controls for each.

&nbsp;

A compact architectural principle follows:

&nbsp;

local bounded knowledge

\+ explicit residual outside that knowledge

\+ preservation of decision-relevant information across boundaries

→ justified operational closure without false certainty.

&nbsp;

# 2\. Foundational model

&nbsp;

Let W\_i denote the context window available to agent or subsystem i. W\_i includes the observations, sample, retrieved evidence, working memory, local model, applicable operating regime and accessible dependency information actually available for the decision.

&nbsp;

Let U\_i denote the portion of the relevant world represented within W\_i. U\_i is not the whole universe. It is the subsystem’s operationally accessible universe for the current decision.

&nbsp;

Let D\_i denote the subsystem’s determination capacity: computation, algorithms, time, evidence-retrieval capacity, sensor or source access, dependency visibility and effective human-oversight capacity.

&nbsp;

Let Ω\_i denote the extended decision-relevant environment: the larger population, future states, external dependencies, actors, environmental conditions and interactions that may materially affect the decision, whether or not they are currently represented inside U\_i.

&nbsp;

The subsystem attempts to determine a decision-relevant property X using W\_i and D\_i. It may reach a sufficiently supported conclusion, a probabilistic result, a confidence estimate, or an explicit indeterminate state.

&nbsp;

Two outputs must therefore remain conceptually separate:

&nbsp;

Operational closure — what the subsystem decides to do now.

Epistemic determination — what the subsystem has actually established about X.

&nbsp;

A system can close operationally and still remain partially indeterminate.

&nbsp;

# 3\. Dimension 1 — In-window / local indeterminacy

&nbsp;

## 3.1 Object

&nbsp;

Dimension 1 is the indeterminacy inside W\_i itself: uncertainty or non-determination about the evidence, sample, state or condition the subsystem can actually see and reason about.

&nbsp;

This is the most familiar case. The agent may know the relevant variables only probabilistically; evidence may be insufficient; two hypotheses may remain observationally indistinguishable; computation may be exhausted; a dependency may not answer; or an authorised human may be required but unavailable.

&nbsp;

## 3.2 Correct management

&nbsp;

Correct Dimension-1 management accepts that sufficient determination may not be obtainable inside the real operating boundary.

&nbsp;

The subsystem should define:

\- what degree of determination is sufficient for the current decision and criticality;

\- which additional evidence, computation or verification is worth obtaining;

\- when human escalation is required;

\- whether the required human capacity is actually reachable within the useful decision window; and

\- what operational state applies when sufficient determination remains unavailable.

&nbsp;

A valid local outcome can therefore be determined, indeterminate, held, deferred, reduced-scope, contained, safe-fallback or another explicitly bounded state. The vocabulary is secondary. The essential architectural property is that “I cannot determine this sufficiently” is itself a legitimate operational fact.

&nbsp;

## 3.3 Failure mode 1A — epistemic hunger / escalation deadlock

&nbsp;

A subsystem may refuse to accept indeterminacy because the decision is important:

&nbsp;

critical condition → must know → request more evidence / escalate → required resource unavailable → continue waiting or escalating.

&nbsp;

The classic human-oversight version is straightforward. A mission-critical action requires an authorised human to resolve an ambiguity. The system escalates correctly, but the authorised human is not available within the useful intervention window. If the architecture treats human review as effectively unlimited, the system can remain HELD indefinitely.

&nbsp;

The error is not that it requested more information. The error is the absence of a bounded capacity model and a correct escape/closure condition when the required determination resource is unavailable.

&nbsp;

In a time-critical system, epistemic perfectionism can itself become an operational hazard.

&nbsp;

## 3.4 Failure mode 1B — forced certainty / masked indeterminacy

&nbsp;

The opposite failure occurs when two requirements conflict:

&nbsp;

the system must act;

the system has not obtained sufficient determination.

&nbsp;

A badly designed architecture resolves the contradiction by silently dropping the second fact. Insufficient evidence, low confidence or unavailable human authority is converted into PASS / FAIL / YES / NO and operation continues as though the underlying condition had been determined.

&nbsp;

This is false closure. The need to act has been mistaken for certainty.

&nbsp;

Dimension-1 rule:

A correct local system must be able to say both “I have to act” and “I do not know this sufficiently.”

&nbsp;

# 4\. Dimension 2 — Residual / out-of-window indeterminacy

&nbsp;

## 4.1 Object

&nbsp;

Dimension 2 begins where W\_i ends.

&nbsp;

Even if Dimension 1 is managed perfectly, the local inference is conditional on U\_i. Relevant state may remain outside it: unobserved population segments, future conditions not represented by the sample, unmeasured co-dependencies, unknown participants, unavailable data, changed environmental conditions, hidden incentives, regime shifts, or interactions the local model does not represent.

&nbsp;

The system may therefore make the best possible estimate inside U\_i while still facing residual indeterminacy about whether U\_i adequately represents the larger condition on which the decision depends.

&nbsp;

## 4.2 Probability is not the residual

&nbsp;

Suppose the subsystem reports q \= 0.85 based on its observed sample, context window and model.

&nbsp;

That can be a valid confidence or probability statement about the modelled evidence. It does not automatically mean “0.85 probability over every relevant state of the extended world.”

&nbsp;

The residual is not necessarily missing numerical probability mass. Some of Ω\_i \\ U\_i may be insufficiently specified even to support a defensible probability assignment.

&nbsp;

Dimension 1 asks:

How uncertain am I about what I can currently observe and compute?

&nbsp;

Dimension 2 asks:

What relevant uncertainty remains because the boundary of observation/model itself is incomplete?

&nbsp;

## 4.3 Correct management

&nbsp;

Correct Dimension-2 management makes the inference boundary explicit.

&nbsp;

It distinguishes:

\- observed population, sample, time window and context;

\- measured versus assumed dependencies;

\- relevant dependencies that remain unmeasured or unavailable;

\- direct conclusions versus extrapolations;

\- known unknowns;

\- areas where the state space is not sufficiently specified for a probability claim; and

\- residual state that remains relevant after the local operational decision.

&nbsp;

Correct management does not require omniscience. It requires refusing to transform a bounded inference into an unbounded certainty claim.

&nbsp;

## 4.4 Failure mode 2A — local-to-global confidence inflation

&nbsp;

A confidence statement valid inside U\_i is promoted into confidence about the complete relevant environment.

&nbsp;

Example:

0.85 confidence over observed/modelled evidence

becomes

0.85 confidence that the real-world condition is true across unobserved populations, dependencies and future states.

&nbsp;

The numerical value has not become wrong; its scope has become unjustifiably enlarged.

&nbsp;

## 4.5 Failure mode 2B — epistemic paralysis

&nbsp;

The opposite failure is to conclude that because Ω\_i can never be known completely, no action can ever be justified.

&nbsp;

That converts residual indeterminacy into permanent inaction.

&nbsp;

Correct operation lies between false certainty and epistemic paralysis: act using the best supported local determination, criticality and risk policy while explicitly retaining what remains outside the determination boundary.

&nbsp;

## 4.6 Harder limits: computability and resource-bounded determination

&nbsp;

Not every unresolved condition is formally undecidable. Most operational indeterminacy is more mundane: finite evidence, finite time, finite computation, finite human capacity or incomplete observation.

&nbsp;

However, classical computability establishes a harder boundary behind the architecture. Turing’s computability framework shows that there are well-defined decision problems for which no general effective procedure can exist. Rice’s theorem strengthens this for program semantics: non-trivial semantic properties of programs are not decidable in general.

&nbsp;

These results should not be over-applied. They do not prove that every ecosystem property is undecidable. Their role here is narrower: they rule out an architectural assumption that sufficient determination can always be manufactured merely by allocating more ordinary computation. Some indeterminacy may be reducible; some may remain because the resources available are insufficient; and some classes of semantic questions encounter formal limits.

&nbsp;

Therefore operational closure must be designed to coexist with unresolved remainder rather than treating full determination as a universal precondition.

&nbsp;

# 5\. Dimension 3 — Intermediation / compositional indeterminacy

&nbsp;

## 5.1 Object

&nbsp;

An agent rarely observes the world directly. It consumes representations produced by other agents, models, organisations, sensors, documents, summaries and services.

&nbsp;

