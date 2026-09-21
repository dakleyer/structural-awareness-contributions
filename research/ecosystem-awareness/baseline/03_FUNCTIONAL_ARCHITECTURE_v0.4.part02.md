 explicit structural residual assumption;

\- window-selection basis: sensitivity/exposure, consequence, reversibility, tolerated residual and capacity assumptions;

\- observation-burden / capacity-binding state where material;

\- marginal expansion/refresh stop condition where represented;

\- qualified acquisition-pathway candidate(s) and decision scope where APQ is invoked;

\- material pathway-property qualification/UNKNOWNs and supporting basis where needed for selection;

\- alternate/independent acquisition path request or no-further-acquisition condition where justified.

&nbsp;

Primary controls

I0, O0, O1, O2.

&nbsp;

Primary interfaces

RAG/retrieval, sensors/observability, memory/context manager, tool layer, external discovery, F7 corrective directives.

&nbsp;

## F3 — Local Epistemic State Qualification

Purpose

Qualify certainty, uncertainty and closure emitted by local agents, humans and subsystems before those outputs are treated as system-level evidence.

&nbsp;

Inputs

\- local operational result, verdict or closure;

\- reported confidence, uncertainty or indeterminate state;

\- scope/window descriptor where available;

\- evidence and provenance state;

\- freshness/as-of;

\- unresolved dependencies;

\- determination-capacity state: human, compute, evidence, authority and time;

\- inherited uncertainty already carried by the local component;

\- current Window Profile for the relevant domain.

&nbsp;

Required behaviour

F3 applies the six internal epistemic controls to the local state. It determines whether the subsystem has correctly represented Type 0, whether Type 1 unbounded determination is occurring, and whether Type 2 certainty collapse has occurred inside or outside its window.

&nbsp;

F3 does not redo the domain task. It does not decide whether a policy verdict, model prediction or human decision is substantively correct. It qualifies what that result allows the wider system to claim epistemically.

&nbsp;

Outputs

\- Qualified Local Epistemic State QL(d);

\- A/B/C/D classification by relevant domain;

\- Type 0 condition markers where applicable;

\- Type 1 / Type 2 fault markers;

\- closure and determination state;

\- missing or unknown qualifiers;

\- capacity-binding state;

\- local requalification candidates.

&nbsp;

Primary controls

I0, I1, I2, O0, O1, O2.

&nbsp;

Primary interfaces

Worker agents, evaluators/critics, policy engines, human-oversight functions, domain controllers, local measurement functions.

&nbsp;

## F4 — External Epistemic Signal Qualification

Purpose

Qualify claims of certainty, uncertainty, determination or indeterminacy received from external agents, organisations, services or other independently governed sources.

&nbsp;

F2.APQ and F4 operate on different objects. F2.APQ asks whether a pathway is sufficiently qualified to obtain decision-relevant evidence for the current need; F4 asks what a particular received signal/result from that pathway actually establishes. Pathway sufficiency does not pre-validate a signal, and a valid signal does not establish that its pathway is globally preferable.

&nbsp;

Inputs

\- external claim/result;

\- reported confidence or uncertainty;

\- declared proposition/domain and scope;

\- source identity and provenance where available;

\- source window/coverage description where available;

\- freshness/as-of;

\- source role and method where available;

\- inherited uncertainty;

\- source dependence / common-source information;

\- integrity, authenticity or adversarial indicators where available.

&nbsp;

Required behaviour

F4 treats a received epistemic signal as a claim about the source's epistemic state, not as the receiver's own state and not as ecosystem truth.

&nbsp;

If a source reports “uncertainty \= 0.3”, F4 preserves what is actually known: who reported it, about what proposition, over what disclosed scope, with what qualifiers. Missing qualifiers remain unknown. They are not silently filled with assumed values.

&nbsp;

F4 distinguishes in-window uncertainty from claims about out-of-window residual, direct observation from inherited representation, and corroboration from repeated dependence on the same upstream evidence.

&nbsp;

Outputs

\- Qualified External Epistemic Evidence QE(d);

\- source-attributed claim and scope;

\- qualified uncertainty/determinacy semantics;

\- unknown-qualifier set;

\- inherited-indeterminacy state;

\- provenance/freshness/dependency class;

\- corroboration versus duplication indication;

\- received-signal Type 0 / Type 1 / Type 2 qualification.

&nbsp;

Primary controls

E0-I, E1-I, E2-I, E0-O, E1-O, E2-O.

&nbsp;

Primary interfaces

Peer agents, external services, third-party assessments, shared signal infrastructures, supply-chain actors, public or regulated evidence sources.

&nbsp;

## F5 — Scope-Indexed Epistemic Composition & Coupling Assessment

Purpose

Compose local and external epistemic states without averaging away their scope, dependency structure or failure modes.

&nbsp;

Inputs

\- QL(d) from F3;

\- QE(d) from F4;

\- Window Profiles from F2;

\- material-domain map from F1;

\- domain coupling/dependency map;

\- source-dependency and provenance graph;

\- human/agent/resource capacity states;

\- current inherited-indeterminacy graph.

&nbsp;

Required behaviour

F5 implements the General Law of Epistemic Composition.

&nbsp;

For every material domain d, it maintains:

E(d) \= \[A\_d, B\_d, C\_d, D\_d\]

&nbsp;

A control or cautious state in d2 does not compensate an epistemic error in d1 unless d2 materially requalifies d1 or a demonstrated dependency through which d1 is inferred.

&nbsp;

Coupling qualification is explicit. The decision-relevant dependency space is open and potentially interdependent: absence of a represented dependency is not evidence of independence. Cross-domain requalification is permitted only when F5 can identify a represented dependency path and state how a change in the epistemic state of d2 would change the determination or qualification in d1. The evidential basis must exist before compensation is applied, or newly discovered coupling must trigger explicit requalification of the earlier composition. If coupling is not established, F5 preserves the scopes separately and carries coupling as UNKNOWN where material; UNKNOWN justifies neither compensation nor independence.

&nbsp;

Where evidence arrives through nominally different acquisition pathways, F5 evaluates evidence lineage separately from pathway identity. Different transports, providers or signalling mechanisms do not constitute independent corroboration when their material claims derive from the same upstream evidence. If the lineage relationship cannot be established, independence remains UNKNOWN rather than being inferred from pathway diversity.

&nbsp;

F5 must detect:

\- cross-domain compensation fallacy;

\- closure laundering;

\- correlated or duplicated evidence presented as corroboration;

\- conflicting local closures;

\- incompatible scopes;

\- inherited uncertainty lost across handoffs;

\- locally coherent but globally fragmented epistemic positions.

&nbsp;

Agent count, vote count and compute volume are not treated as substitutes for independence or scope-aware corroboration.

&nbsp;

Outputs

\- System Epistemic Map E\*(d);

\- domain coupling map with material dependencies;

\- inherited-indeterminacy graph;

\- contradiction/divergence state;

\- source-concentration and double-counting indicators;

\- coupled epistemic imbalance map;

\- composition-validity state;

\- domains requiring requalification.

&nbsp;

Primary controls

I2, O2, E0-I, E1-I, E2-I, E0-O, E2-O, plus the General Law of Epistemic Composition.

&nbsp;

Primary interfaces

Orchestrator/aggregator, multi-agent coordination layer, evidence-fusion functions, decision synthesis.

&nbsp;

## F6 — Systemic Epistemic & Operating-Frame Assessment

Purpose

Determine whether the composed epistemic state is sufficient to justify the current operating frame and identify the appropriate high-level posture.

&nbsp;

Inputs

\- System Epistemic Map E\*(d);

\- composition-validity state from F5;

\- Operation Context Profile from F1;

\- current Window Profiles;

\- current qualified operating envelope Q;

\- response capabilities and capacity state;

\- current ecosystem-sensitivity/exposure and observation-burden profile;

\- regime/mode validity assumptions;

\- current posture;

\- time remaining before relevant response options expire.

&nbsp;

Required behaviour

F6 performs two assessments separately.

&nbsp;

First, it determines the epistemic state by domain in two parts: a management verdict (Sound, Type 1, Type 2 or Mixed) and any relevant Type 0 structural qualification.

&nbsp;

Second, it determines whether the active mission remains inside a sufficiently qualified operating frame and emits a posture assessment: Normal, Containment/Mitigation, or Migration/Regime Transition.

&nbsp;

A Type 0 residual is compatible with Normal when it is explicitly represented and bounded within the accepted operating frame. Type 1 and Type 2 create corrective pressure but do not mechanically imply Containment or Migration. The posture is contextual.

&nbsp;

F6 must also distinguish epistemic state from risk/resource consequence. Type 1 may be epistemically honest yet operationally hazardous because repeated observation, compute or human escalation is exhausting the capacity needed to act. Type 2 may be computationally cheap yet increase hidden exposure because the active frame is narrower or staler than the mission's sensitivity justifies.

&nbsp;

Outputs

\- epistemic condition by domain;

\- Type 0 structural conditions;

\- Type 1 and Type 2 management faults;

\- current operating posture;

\- affected domains and dependencies;

\- operating-frame validity statement;

\- response-window/actionability state;

\- sensitivity/capacity mismatch where the current observation burden is materially too high or too low for the qualified mission;

\- reasons and qualifiers supporting the assessment;

\- requalification requirement.

&nbsp;

Primary interfaces

Planner/orchestrator, safety/action controller, human oversight, containment/recovery functions, strategy or migration functions.

&nbsp;

## F7 — Requalification & Corrective Directive Generation

Purpose

Convert epistemic assessment into targeted requests that restore or preserve a sound epistemic position.

&nbsp;

Inputs

\- F6 epistemic condition and posture;

\- coupled imbalance map from F5;

\- domain and dependency map;

\- available evidence, compute, human and authority capacity;

\- current Window Profiles;

\- available response capabilities;

\- mission criticality and deadlines.

&nbsp;

Required behaviour

F7 is what makes Ecosystem Awareness an operational capability rather than an auditor.

&nbsp;

It does not simply say “add more control.” It selects the smallest relevant requalification action for the domain in which the imbalance exists. That action may intentionally reduce observation effort when the system is in Type 1, or increase/redirect observation when the current frame is too narrow for the mission's ecosystem sensitivity.

&nbsp;

Candidate directives include:

\- widen, narrow or redirect W(d);

\- request a specific missing evidence class;

\- retrieve or inspect a primary source;

\- obtain genuinely independent corroboration;

\- refresh stale provenance, policy, authority or dependency state;

\- downgrade or rescope reliance on an external source;

\- preserve INDETERMINATE rather than force binary closure;

\- stop, narrow or redirect further search/escalation when determination effort has become Type 1 or its marginal information value is no longer proportionate to remaining capacity/time;

\- request human review only when human capacity is relevant, reachable and actionable;

\- reduce autonomy, exposure or scope;

\- request known containment mechanisms;

\- initiate preparation for migration/requalification of the operating frame;

\- rerun a local evaluation on the same affected domain;

\- select or request an alternative acquisition pathway when the current pathway cannot satisfy a material scope, freshness, evidence-basis, independence or response-window requirement;

\- decline additional acquisition through a pathway whose expected marginal epistemic contribution is not proportionate to its burden or the remaining time in which evidence can change the decision.

&nbsp;

F7 issues epistemic and control requests. It does not itself own enforcement authority or execute every corrective action.

&nbsp;

Outputs

\- domain-targeted requalification directives;

\- window-change requests;

\- evidence/corroboration requests;

\- capacity/authority refresh requests;

\- bounded stop conditions;

\- containment or scope-reduction requests;

\- migration/requalification preparation requests;

\- re-evaluation triggers and success criteria.

&nbsp;

Primary controls

I0, I1, I2, O1, O2, E1-I, E2-I, E1-O, E2-O.

&nbsp;

Primary interfaces

Orchestrator, retrieval/research agents, human oversight, policy/authority service, safety controller, containment/recovery, migration/strategy functions.

&nbsp;

## F8 — Epistemic Statement & Envelope Generation

Purpose

Expose the system's qualified epistemic position to internal consumers and, where appropriate, external peers without disclosing the complete private window or reasoning state.

&nbsp;

Inputs

\- F5 System Epistemic Map;

\- F6 condition/posture assessment;

\- disclosure/privacy policy;

\- recipient role and required scope;

\- relevant provenance, freshness, dependency and capacity qualifiers.

&nbsp;

Required behaviour

F8 creates a bounded statement that another function can safely interpret.

&nbsp;

The internal statement may be richer than the external envelope. Neither should serialize prompts, private memory or chain-of-thought. The purpose is sufficient preservation of decision-relevant epistemic qualification.

&nbsp;

The envelope should preserve, at an implementation-appropriate abstraction level:

\- proposition/domain/scope;

\- closure state;

\- determinacy / uncertainty class;

\- relevant Type 0 residual or unknown qualifier;

\- freshness/as-of;

\- provenance/dependency class;

\- inherited indeterminacy;

\- capacity binding where material;

\- operating-frame qualification or posture where relevant;

\- response/actionability window where relevant.

&nbsp;

A published signal changes evidence for the receiver. It does not create authority for the receiver.

&nbsp;

Outputs

\- Internal Epistemic Statement;

\- External Epistemic Envelope;

\- validity/freshness metadata;

\- scope and dependency qualifiers;

\- inherited-indeterminacy markers;

\- recipient-appropriate disclosure profile.

&nbsp;

Primary interfaces

Internal orchestrator/decision synthesis, observability, audit/trace functions, signal transport/exchange infrastructure, external peers.

&nbsp;

## F9 — Outcome Feedback & Revalidation

Purpose

Close both loops by comparing observed consequences with the assumptions and epistemic qualifications under which the system acted.

&nbsp;

Inputs

\- observed operational outcomes;

\- expected outcome/response assumptions;

\- new drift, anomaly or measurement evidence;

\- containment or migration results;

\- changed human/agent/compute/authority capacity;

\- changed dependencies or source availability;

\- external corrections or resolution signals;

\- elapsed validity and freshness intervals.

&nbsp;

Required behaviour

F9 determines whether the previous frame remains valid after action and time.

&nbsp;

A material mismatch can trigger:

\- F3/F4 requalification if an input or source changed;

\- F5 recomposition if dependency relationships changed;

\- F2 window requalification if coverage or relevance changed;

\- F1 mission/context requalification if objectives, criticality, ecosystem sensitivity/exposure, tolerated residual, observation/determination capacity or response capability changed;

\- F6 direct reassessment when a posture or regime assumption expires.

&nbsp;

The architecture therefore learns operationally without assuming that previous confidence survives material change. F9 also feeds back whether the selected observation burden was too high or too low: wasted search/escalation and capacity depletion are evidence for tightening future Type-1 bounds; missed material changes, stale-frame surprises and hidden exposure are evidence for widening, refreshing or redirecting future W(d,t).

&nbsp;

Pathway learning remains scope-indexed. F9 may retain evidence that an acquisition pathway was useful, stale, redundant, costly or independently informative for a stated domain, decision/context and time profile, but it must not convert repeated historical success into a portable global trust or quality score for that pathway. Historical usefulness is evidence for a new qualification; it does not substitute for current scope, provenance, freshness, source dependence, property basis or response conditions.

&nbsp;

Outputs

\- revalidation triggers;

\- updated validity assumptions;

\- expected/observed mismatch state;

\- source/dependency freshness changes;

\- required re-entry point in Loop A or Loop B;

\- retained state history for subsequent assessment;

\- scoped acquisition-pathway performance/history evidence where APQ has been exercised, indexed to the relevant domain/decision/context rather than as a global pathway score.

&nbsp;

Primary interfaces

Observability/monitoring, TEVV/evaluation, incident/resolution lifecycle, orchestrator, F1–F6.

Validation coverage. Validation coverage is maintained in the UC Family. APQ behavior is exercised in UC-EA-02 and UC-EA-04; APQ-specific F9 learning is exercised through the repeated-run step in UC-EA-02.

&nbsp;

# 5\. Generic component interfaces

The functio