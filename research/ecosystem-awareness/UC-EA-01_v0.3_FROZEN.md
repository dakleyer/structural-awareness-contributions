# UC-EA-01 — Architecture-Validation Profile

## Action-time Operating-Frame Requalification under Context Change

**Version:** v0.3 — Frozen  
**Parent Case Study:** `TIDA — Delegated Authority OS under Context Change`  
**Status:** frozen internal Ecosystem Awareness architecture-validation profile preserved in the public reference corpus.

> **Public-submission boundary:** UC-EA-01 is **not** an FG-TIDA use-case submission and must not be presented as one. It is an architecture-validation profile derived from a bounded scenario in the public Parent Case Study. Any later public FG-TIDA use-case record should expose the concrete situation and relying-party decision rather than present this internal validation apparatus as a formal Focus Group submission.

## 1. Purpose

The profile tests the following hypothesis:

> A determination that was justified at T1 may cease to be sufficiently qualified at T2 even when no upstream component is individually malfunctioning.

The system must therefore be able to requalify the decision-relevant window and operating frame rather than merely execute a pre-existing trigger or reuse a prior closure.

The same observable context change can justify different awareness/requalification effort depending on:

- mission sensitivity / ecosystem exposure;
- consequence severity;
- reversibility;
- tolerated residual;
- available observation/determination capacity; and
- remaining response horizon.

The test evaluates **W(d,t)**, not maximum context collection.

## 2. Identification and traceability

- **Validation Profile ID:** UC-EA-01
- **Parent Case Study:** TIDA — Delegated Authority OS under Context Change
- **Primary Challenge:** S3 — Regime, context, escalation & bounded escape path
- **Secondary Challenges:**
  - S10 — Commitment state, material change & normal escalation
  - S14 — Evidence-to-decision assessment
  - S5 — Operational indeterminacy & containment
- **EA functions under test:** F1, F2, F5, F6, F7, F9

The mobility material is a bounded concrete instantiation, not the semantic boundary of the Case Study. Upward, downward and horizontal extensibility remain properties of the Parent Case and do not silently add facts to this profile.

## 3. Plain-language situation

A citizen's personal agent has created commitment **C1** under citizen grant **G1** and municipal policy/mandate **P1**.

Before execution, approved source **E1** reports that **Qcritical** has been crossed. P1 requires reassessment and temporarily disallows entry to the affected zone unless an authorised exceptional intervention **H1** applies.

The relying decision must determine whether the T1 determination can still be used at action time, or whether the system must:

- reroute;
- hold;
- enter a bounded intervention path;
- remain INDETERMINATE;
- contain; or
- requalify the operating frame.

## 4. Actors and objects

### Actors

- citizen principal;
- citizen personal agent / relevant agent instance;
- municipality / public principal;
- authorised municipal role;
- bounded municipal agent where used;
- evidence source E1;
- relevant relying-party / action-admission function; and
- human authority where H1 is invoked.

### Decision objects

- **G1 — Grant:** bounded authority conferred by the citizen principal.
- **P1 — Policy / public mandate:** applicable public conditions, thresholds and approved observation source.
- **D1 — Decision:** decision reached at commitment time.
- **C1 — Commitment:** operational commitment established at T1.
- **H1 — Exceptional intervention record:** later intervention, authority, evidence and effect if used.
- **A1 — Action:** execution associated with C1 after the context change.

G1, P1, D1/C1 and H1 remain distinct records. No later object silently overwrites another.

## 5. Decision required

> May the determination that justified D1/C1 at T1 still be relied upon for A1 at T2, and if not, what requalification and operating posture are justified?

A conventional policy or trigger engine can correctly detect Qcritical and still fail to answer whether the epistemic frame supporting the earlier commitment remains sufficient.

The residual architecture question is whether the system treats:

- the current observation/context window W(d,t);
- the assumptions supporting the earlier determination;
- the operating envelope; and
- effective human/technical capacity

as **requalifiable state** rather than assuming that a valid historical closure remains current.

## 6. Parent Case facts

### T0 — Setup

The citizen issues G1 with hard limits, tradeable preferences and permitted commitments. An authorised municipal role issues P1, including Qnormal/Qcritical and approved observation source E1.

Visible evidence includes identities and role mandates, current G1/P1 versions and validity periods, the preference profile, threshold definition and source provenance.

The personal agent may plan only inside G1 and P1.

### T1 — Commitment

The personal agent selects an option and records D1 and C1.

C1 may be created only if authority and hard limits are sufficiently established. Otherwise the system holds or escalates.

### T2 — Context change and action-time determination

Before execution, E1 shows that Qcritical has been crossed.

P1 defines crossing as a reassessment trigger and temporarily disallows entry to the affected zone unless authorised exceptional intervention H1 applies.

The system must determine the operative authority and posture for A1.

## 7. Human-oversight boundary

A human role may be formally authorised yet:

- unavailable;
- overloaded;
- insufficiently informed;
- unable to understand the case in useful time; or
- unable to intervene effectively.

A nominal role does not manufacture usable capacity or permission.

This profile may consume a human-capacity state, but it does not redefine the human-oversight lifecycle itself.

## 8. EA functional traceability

### F1 — Mission & Decision Context Qualification

Consumes mission, criticality, ecosystem sensitivity/exposure, consequence/reversibility, tolerated residual, finite capacity, authority and response capability to define the required T2 determination.

### F2 — Decision-Relevant Window Qualification & Management

Qualifies W(d,t): what remains inside, what could be brought in, what residual remains outside any guarantee and whether additional observation is proportionate.

### F5 — Scope-Indexed Epistemic Composition

Composes current authority, context, evidence and capacity without treating the T1 closure as automatically current.

### F6 — Systemic Epistemic & Operating-Frame Assessment

Separates epistemic condition from operating posture.

### F7 — Requalification & Corrective Directive Generation

May direct the system to:

- refresh one source;
- widen, narrow or redirect W(d,t);
- preserve INDETERMINATE;
- request bounded human review;
- reduce scope;
- contain; or
- prepare migration/requalification.

### F9 — Outcome Feedback & Revalidation

Compares the T2 condition and observed outcome with the assumptions supporting D1/C1 and selectively re-enters the appropriate loop.

It also records whether the chosen awareness burden was too high or too low.

## 9. Primary failure surfaces

The profile exercises:

- **I0 — determination capacity**
- **I1 — bounded determination effort**
- **I2 — epistemic honesty**
- **O0 — structural residual**
- **O1 — bounded window expansion**
- **O2 — non-collapse of the active window into ecosystem completeness**

External-signal controls also apply where E1 or another source supplies the context change.

## 10. Requirements

**R1.** The system shall preserve the distinction between the T1 commitment decision and the T2 action-time determination.

**R2.** The system shall expose or derive a qualified current window/scope sufficient to state what evidence and context support the T2 determination.

**R3.** A material context change shall trigger requalification of the affected domain rather than automatic reuse of the T1 closure.

**R4.** The system shall distinguish a recognised Type-0 structural residual from Type-1 unbounded determination and Type-2 false certainty.

**R5.** Window expansion, retrieval, escalation and human review shall have bounded stopping/requalification conditions proportional to mission sensitivity, consequence/reversibility, capacity and response horizon.

**R6.** Absence from the current window shall not be treated as evidence of absence from the ecosystem.

**R7.** Epistemic condition shall remain separate from Normal / Containment-Mitigate / Migration-Regime-Transition posture.

**R8.** Corrective directives shall target the affected domain or a demonstrated material dependency rather than add generic checking elsewhere.

**R9.** Where evidence/applicability cannot be established sufficiently, INDETERMINATE shall remain a legitimate result and shall not be converted into silent permission.

**R10.** Outcome evidence shall support a determination of whether the previous frame may be reused, revised or abandoned/requalified.

**R11.** The test shall record the sensitivity/exposure and finite-capacity assumptions used to justify W(d,t).

**R12.** A lower-sensitivity / reversible branch shall not be forced into broad requalification merely because a wider window is technically available.

**R13.** A higher-sensitivity / irreversible branch shall not reuse a narrow or stale window solely to reduce observation cost.

## 11. Test and stress-test branches

### Branch A — Positive Normal control

No material change invalidates the T1 frame. G1/P1 and supporting evidence remain sufficiently qualified.

**Expected EA behavior:** retain Normal posture; do not expand W or escalate merely because residual uncertainty exists.

### Branch B — Context change with known bounded response

Qcritical is crossed, the trigger is authentic/current and a known reroute or scope-reduction path preserves a sufficiently qualified frame.

**Expected EA behavior:** requalify the affected domain and use a bounded Containment/Mitigation or reroute posture; do not treat D1/C1 as automatically current.

### Branch C — Incomplete action-time qualification

Qcritical is reported but scope/applicability/freshness of one material input is insufficient. A specific additional source can reasonably resolve the question within the useful response window.

**Expected EA behavior:** targeted bounded retrieval/expansion; preserve INDETERMINATE until resolved.

### Branch D — Type-1 stress

Repeated retrieval, escalation or human review continues after the justified path is exhausted or the useful response window has passed.

**Expected EA behavior:** identify Type 1 and stop unbounded determination; move to bounded closure, containment or requalification.

### Branch E — Type-2 stress

The system treats D1/C1, stale policy state or an incomplete external signal as sufficient current determination after T2.

**Expected EA behavior:** identify false certainty and requalify.

### Branch F — Regime-transition stress

A controlled test variant introduces evidence that the assumptions supporting the normal control/oversight frame no longer provide a sufficiently qualified response mapping.

**Expected EA behavior:** preserve invariant safe actions while selecting Migration / Regime Transition rather than endlessly restoring the old frame.

This is a stress-test variant, not a frozen Parent Case fact.

### Branch G — High-sensitivity / narrow-window stress

The T2 change is materially coupled to a high-consequence or difficult-to-reverse domain while a baseline reuses a lower-sensitivity context window.

**Expected EA behavior:** widen/refresh/redirect W(d,t) only for the material domain and preserve the reason for stronger awareness.

### Branch H — Low-sensitivity / over-requalification stress

The same class of change affects a reversible/low-consequence domain with a known bounded fallback while a baseline performs broad system-wide revalidation.

**Expected EA behavior:** retain or narrow the qualified window, use the bounded response and avoid unnecessary retrieval, verification or human escalation.

### Branch I — Capacity-constrained response-window stress

Additional evidence is potentially available but collecting it would consume enough time or capacity that the effective response option would expire.

**Expected EA behavior:** compare decision value with the remaining response horizon and prefer bounded closure/containment over epistemic perfectionism.

## 12. Success criteria

The profile succeeds architecturally if it demonstrates that:

- T2 determination remains distinct from T1 commitment;
- normal operation can continue under correctly bounded residual uncertainty;
- known bounded responses are selected without unnecessary global escalation;
- unbounded retrieval/escalation is recognizable as Type 1;
- stale/local closure is not promoted into current ecosystem truth;
- Migration / Regime Transition can be selected when the old mapping loses validity without confusing posture with Type 0/1/2; and
- requalification effort remains proportionate to mission sensitivity and finite capacity.

## 13. Measurable evidence

Potential evidence includes:

- explicit W(d,t) and its selection basis;
- scope/freshness/provenance or explicit UNKNOWN for material inputs;
- number and duration of requalification steps;
- retrieval/tool calls;
- compute/tokens;
- latency;
- bandwidth/privacy burden;
- human-review time;
- whether additional observation changed the decision;
- whether material context change was missed under a stale/narrow frame;
- whether response options remained available after requalification effort;
- whether directives targeted the affected domain;
- whether D1/C1 remained historically recorded but not silently reused; and
- whether outcome feedback returned through F9.

## 14. Peer baseline and differentiation test

Shared mechanisms already present in peer architectures include:

- runtime policy/conformance evaluation;
- retrieval/context refresh;
- telemetry;
- HITL/escalation;
- guardrails;
- orchestration;
- containment;
- persistence; and
- tracing.

Ecosystem Awareness does **not** claim these mechanisms as new.

The added behavior under test is:

- mission/sensitivity/finite-capacity qualification of W(d,t);
- explicit in-window/out-of-window distinction;
- Type 0/1/2 classification;
- separate epistemic condition and operating posture;
- targeted requalification of the same material domain;
- selective double-loop re-entry; and
- the ability to choose **less**, rather than always more, observation when marginal decision value has collapsed.

The peer reproduction question is:

> Can a plausible peer composition reproduce the same behavior under the frozen facts without adding a layer that explicitly tracks window sufficiency, external epistemic qualification, structural residual and domain-indexed composition?

If yes, the differentiation claim must be reduced accordingly.

## 15. Non-duplication boundary

This profile does not reimplement neighbouring FG-TIDA functions.

- Theme #13 signal/incident lifecycle may supply ecosystem signal state.
- Theme #6 may supply a local conformance/verdict state.
- Theme #16 owns the human-oversight lifecycle and may supply effective capacity/decision state.
- Authority, identity, attestation and enforcement remain with their respective functions.

EA consumes qualified outputs and evaluates the decision-scoped systemic frame.

## 16. Maturity and public boundary

- **Validation maturity:** frozen hypothetical architecture-validation profile.
- **Reference implementation:** not required by the frozen profile.
- **Public boundary:** this profile is not an FG-TIDA use-case submission.
- **Purpose of publication:** preserve a dated, reviewable reference for architecture comparison and later stress testing.

The profile can be reopened only if validation exposes a genuine missing or unnecessary architectural responsibility; revisions should be published as a later version rather than silently rewriting this frozen snapshot.
