The existing public Theme \#13 discussion gives a useful candidate envelope for interoperability. Its value is not that every implementation must compute determinacy in the same way. Its value is that different internal systems can express enough of the result for ecosystem-level reasoning.

&nbsp;

Candidate fields already explored publicly include:

&nbsp;

closure \= determined | fallback | held

&nbsp;

determinacy\_margin \= above | at | below

&nbsp;

capacity\_binding \= not\_binding | binding | unavailable

&nbsp;

inherited\_indeterminacy \= none | direct | transitive | unknown

&nbsp;

The key invariant is that an upstream unknown must never silently become none.

&nbsp;

This can be extended cautiously with scope, freshness, provenance, response capacity or relevant posture, but the interface should remain minimal. The objective is interoperability through bounded semantics, not an attempt to serialize the complete internal state of every agent.

&nbsp;

10\. RELATION TO THEME \#13 SIGNAL LIFECYCLE

&nbsp;

The determinacy envelope and signal lifecycle should remain independently testable.

&nbsp;

The signal lifecycle answers how an ecosystem-relevant claim is born, distributed, corroborated or amended, used in containment and eventually resolved.

&nbsp;

The determinacy envelope answers what system-level sufficiency or uncertainty state an implementation needs to communicate.

&nbsp;

A signalling implementation can carry another assessment model. A determinacy implementation can be transported by another signalling mechanism.

&nbsp;

This separation is strategically and technically important because it allows competing designs to interoperate rather than forcing one monolithic architecture.

&nbsp;

11\. RELATION TO THEME \#16 HUMAN OVERSIGHT

&nbsp;

Theme \#16 should not own Ecosystem Awareness merely because human capacity is one of its inputs.

&nbsp;

The clean boundary developed in current discussion is:

&nbsp;

Theme \#16 manages human oversight and intervention locally: authority, trigger qualification, available reviewers, evidence-to-decision, exceptional intervention and return to operation.

&nbsp;

Ecosystem Awareness can consume human-capacity state as one dependency among many when determining overall system capacity and determinacy.

&nbsp;

Thus human oversight capacity remains a Theme \#16 concern, but ecosystem-level qualification of whether the combination of human and agentic dependencies remains sufficient is a separate system-level function.

&nbsp;

This makes \#16 a consumer and contributor to Ecosystem Awareness rather than the owner of the entire assessment.

&nbsp;

12\. WHAT THE FOCUS GROUP SHOULD STANDARDIZE OR PRE-STANDARDIZE

&nbsp;

A bounded work package could produce five classes of output.

&nbsp;

A. Vocabulary and conceptual model

&nbsp;

Define ecosystem, Ecosystem Awareness, Objective Envelope, Semantic Window, warning sufficiency, containment, migration, system-level determinacy and inherited indeterminacy carefully enough for consistent discussion.

&nbsp;

B. Minimal interface semantics

&nbsp;

Define the minimum fields or semantic properties needed for ecosystem-level reasoning without prescribing internal algorithms.

&nbsp;

C. Architectural property framework

&nbsp;

Define dimensions for observation, warning, containment, migration, authority, feedback, signalling assurance, privacy and residual uncertainty.

&nbsp;

D. Test profiles

&nbsp;

Define reproducible cases in which implementations can be compared under benign, degraded and adversarial conditions.

&nbsp;

E. Interoperability / conformance questions

&nbsp;

Define what an implementation must demonstrate to claim that its ecosystem-level information can be safely consumed by another independently governed participant.

&nbsp;

13\. TEST PROFILES

&nbsp;

A useful test programme should begin simple and become adversarial.

&nbsp;

Profile 1 — normal heterogeneous operation

&nbsp;

Several independently governed agents operate with different MCA configurations. Test whether they can exchange ecosystem-level determinations without sharing internal logic.

&nbsp;

Profile 2 — noisy evidence

&nbsp;

Introduce stale observations, missing data and non-malicious disagreement. Test confidence, freshness, contradiction handling and window adaptation.

&nbsp;

Profile 3 — correlated failure

&nbsp;

Several sources depend on the same hidden upstream dependency. Test whether apparent corroboration incorrectly becomes certainty.

&nbsp;

Profile 4 — capacity degradation

&nbsp;

Human or agentic response capacity becomes binding or unavailable. Test whether a locally correct determination can still expose system-level insufficiency.

&nbsp;

Profile 5 — rapid regime transition

&nbsp;

The ecosystem crosses a boundary faster than normal review cycles. Test warning margin, containment and migration readiness.

&nbsp;

Profile 6 — adversarial signalling

&nbsp;

Introduce spoofing, replay, Sybil reporters, collusion, reputation poisoning or false attribution. Test signal assurance and graceful degradation.

&nbsp;

Profile 7 — partial participation

&nbsp;

Some participants refuse to signal or disclose only minimum information. Test whether the architecture remains useful without assuming cooperation.

&nbsp;

Profile 8 — competing objectives

&nbsp;

Participants have legitimate but conflicting goals. Test whether shared signals improve determination without creating a fictitious global objective.

&nbsp;

14\. WHAT SHOULD REMAIN OUTSIDE THE FG

&nbsp;

The Focus Group should not need to standardize:

&nbsp;

\- the globally optimal MCA configuration;

\- proprietary Semantic Window selection algorithms;

\- proprietary risk models;

\- one universal Early Warning predictor;

\- one global utility function;

\- one mandatory peer-to-peer transport protocol;

\- one mandatory consensus mechanism;

\- one centralized ecosystem observer;

\- proprietary methods for discovering local or Pareto-efficient configurations;

\- implementation-specific machine-learning models;

\- or IMSV's deeper research theory where interoperability does not require common semantics.

&nbsp;

Those are research and implementation spaces.

&nbsp;

The FG should define the information and properties necessary for heterogeneous solutions to coexist and be testable.

&nbsp;

15\. WHY THIS AVOIDS A TAUTOLOGY

&nbsp;

The proposition is not 'better systems survive better.'

&nbsp;

Specific, falsifiable hypotheses can be formulated.

&nbsp;

Example 1: Under comparable disturbances, implementations that preserve source independence and inherited uncertainty across ecosystem signals will produce fewer unjustified high-confidence determinations than implementations based only on unqualified aggregation.

&nbsp;

Example 2: An adaptive Semantic Window that can widen under confidence degradation can preserve warning sufficiency with lower steady-state observation burden than a permanently maximal window, under defined workload and threat conditions.

&nbsp;

Example 3: Systems that explicitly relate warning horizon to reachable response capacity will identify more cases of operationally useless detection than systems that evaluate detection quality independently of intervention timing.

&nbsp;

Example 4: MCA configurations with different allocations of sensing, containment and migration can all remain inside the same Objective Envelope, demonstrating that one universal architecture is unnecessary.

&nbsp;

Example 5: Ecosystem signalling can improve local adaptation even among competing participants when signals preserve sufficient provenance and scope, while low-assurance propagation can worsen collective determination under adversarial or correlated conditions.

&nbsp;

These are empirical and architectural questions, not philosophical restatements.

&nbsp;

16\. PROPOSED WORK-PACKAGE THESIS

&nbsp;

A concise work-package thesis could be:

&nbsp;

Ecosystem Awareness should define the minimum information, architectural properties and evaluation dimensions required for independently governed systems to determine whether their local control assumptions remain sufficient under changing ecosystem conditions, and to exchange ecosystem-relevant determinations without requiring common internal logic, common objectives or a central orchestrator.

&nbsp;

That thesis is broad enough to connect Semantic Window, Early Warning, MCA, determinacy and signalling, but narrow enough to remain about interfaces, sufficiency and testability.

&nbsp;

17\. CENTRAL ARCHITECTURAL PRINCIPLES

&nbsp;

1\. Local correctness does not establish ecosystem-level validity.

&nbsp;

2\. Complete ecosystem awareness is impossible; sufficiency is the target.

&nbsp;

3\. The Semantic Window is a deliberate subset of observable reality.

&nbsp;

4\. Warning quality is meaningful only relative to reachable response capacity.

&nbsp;

5\. Minimum Control Architecture is a configuration space, not one fixed stack.

&nbsp;

6\. Multiple sufficient or Pareto-efficient MCA configurations can coexist.

&nbsp;

7\. Ecosystem signalling reduces local epistemic isolation but does not eliminate indeterminacy.

&nbsp;

8\. Signals do not create authority.

&nbsp;

9\. Unknown must not silently become none across handoffs.

&nbsp;

10\. The architecture must operate under partial participation, competition and adversarial behavior.

&nbsp;

11\. Normal, Containment and Migration provide simple response postures; technical regime or bifurcation assessments remain distinct.

&nbsp;

12\. Interoperability should standardize what must be understood across boundaries, not how every participant reasons internally.

&nbsp;

18\. CONCLUSION

&nbsp;

The conceptual line now has a coherent hierarchy.

&nbsp;

The ecosystem is the dynamic dependency environment in which a bounded system must achieve its mission. Because agentic ecosystems can change as fast as the systems that depend on them, ecosystem state can no longer be treated as stable background context. The system therefore needs Ecosystem Awareness, but complete awareness is structurally impossible.

&nbsp;

That contradiction produces a sufficiency architecture.

&nbsp;

The Objective Envelope defines what must be preserved. Response capabilities determine how much advance warning is required. The Early Warning requirement determines what Semantic Window is sufficient. Ecosystem Awareness qualifies whether the resulting operating frame remains valid. MCA selects the minimum sufficient control configuration. Normal, Containment and Migration describe the resulting response posture. Ecosystem signalling allows local discoveries and regime-relevant observations to become partially reusable across the ecosystem without demanding cooperation or central control.

&nbsp;

The Focus Group opportunity is not to select one optimal architecture. It is to define the common language, minimal interfaces, assurance properties and test conditions under which many architectures can reason together without surrendering their independence.

&nbsp;

That is a concrete standardization problem.

&nbsp;

SOURCE / PROVENANCE NOTES

&nbsp;

FGAI4SSC-I-097 publicly establishes the Minimum Sufficient Control direction as an ITU-T FG-AI4SSC input; posting does not imply adoption or endorsement.

FG-TIDA Theme \#13 publicly scopes ecosystem-level defense, shared signals, reputation, logging, privacy, decentralized control and minimum-signal questions.

The current Theme \#13 public discussion includes the determinacy/capacity envelope, signal lifecycle, adversarial testbed ideas and Ward Duchamps' statement that Ecosystem Awareness belongs within \#13 and that the interface may become a foundational architectural building block. These remain contributor proposals and discussion, not adopted FG architecture.

