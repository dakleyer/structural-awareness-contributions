# R01/DDS extension study — STAMP/STPA and effective human escalation

**Canonical research integration — 6 October2026, document edition0.2.** The initial source/analytical text below remains its historical scoped analysis. [Current DDS study and controls](./HEW_DDS_STUDY_2026-10-06.md) record the new deterministic model integration. Native technology, real humans and independent review remain unexecuted/open. The original numerical results are not rewritten or pooled into a success rate.


Canonical research document0.2 / analytical predecessor0.1 · Editorial revision0.1.1 · 6 October 2026 · author-constructed research draft.
Subject: STAMP as a causal model and STPA as an analysis method, applied to a bounded human-escalation control structure.
Evidence: primary-source basic-method review; four-step draft analysis; exact finite calendar checks. No native STPA tool, human process or deployed controller executed.
[Shared case](./dds-hew-v0.1/TECHNICAL_REPORT.md) · [current Run Card](./dds-hew-v0.1/prior-analytical/run_card_v0.3_2026-10-06.json) · [results](./dds-hew-v0.1/prior-analytical/analytical_fixture_results_v0.3_2026-10-06.json).

## 1. What the technology actually is and why it matters

STAMP is the System-Theoretic Accident Model and Processes: a model of causality and control, not an executable analysis application. STPA is System-Theoretic Process Analysis, a method based on it. The chosen source is Leveson and Thomas, STPA Handbook, MIT-STAMP-001, March2018. The basic method in pages14–53 was read; relevant foundation and organizational passages were also consulted. The original source is preserved with SHA-256 in [source intake](./dds-hew-v0.1/SOURCE_REGISTER.json).

STAMP/STPA already addresses interactions, inadequate control, feedback, human process models and organizational conditions. The statement that individually working parts can produce a system loss is therefore not, by itself, a new EA principle.

This study asks a narrower practical question: what constraints and causal scenarios does a STPA-informed analysis derive for protected objections when the human review path has finite capacity, and how can those constraints be made inspectable within a DDS case? A useful case does not require a novel underlying safety theory.

A control diagram identifies functional responsibilities and information paths. It does not assert that messages arrive, commands are followed or human decisions are correct. The handbook also permits multiple interacting controllers; this study does not characterize STPA as restricted to one linear centralized chain.

## 2. Source-grounded duplication check

| Existing contribution to credit | Consequence for this extension |
|---|---|
| System-level losses and constraints | Do not claim discovery of systemic failure merely from local success |
| Control actions, feedback and process models | Capacity misunderstanding is a candidate process-model/control issue |
| Multiple controllers and coordination | The two-obligation conflict can be analyzed without inventing a new causality model |
| Unsafe-action context and timing | Declare actual context, not only “the controller thinks it is available” |
| Loss scenarios for poor execution as well as poor commands | Delivered notice, selected decision and applied intervention remain distinct |
| Organizational/application goals beyond conventional physical safety | Business/mission losses can be within a stated STPA scope |
| Deriving requirements and test cases | This analysis may support a test contract without demonstrating its implementation |

Current claim: conceptual overlap is established in the cited scope. Exact equivalence of every EA/HEW interface, a full implementation or performance frontier is not established. A competent conventional controller built from these constraints receives full credit.

Primary route: [MIT handbook page](https://psas.scripts.mit.edu/home/books-and-handbooks/).
This document is our original application to a synthetic case; it does not reproduce or redistribute the handbook as a service deliverable.

## 3. Step 1 — purpose, boundary, losses, hazards and system constraints

### Boundary and assumptions

Inside: principal/current mandate; mission control; objection/case management; reviewer eligibility/calendar; applicable decision basis; an execution gate; controlled mission and critical duty; status/effect feedback.

Outside the established evidence: actual company staffing, real service-time distributions, device attestation, cryptographic authentication, psychology/competence calibration, privacy enforcement, immutable storage and external standards conformance. These are realization obligations.

The numerical calendar in the shared case is synthetic: arrival2, review3 ticks, decision deadline6, application7 and mission8; primary duty [1,10). The analysis does not assign probability to these conditions.

### Stakeholder losses selected for this case

These are analysis assumptions, not a client's approved business priorities.
- HEW-L1: loss of legitimate mission value through inadequate quality or late delivery.
- HEW-L2: loss caused by an action beyond current mandate or adequate applicable basis.
- HEW-L3: loss of the required continuity of a critical process.
- HEW-L4: loss of protected reporting capability or standing through suppression/unjustified adverse treatment.
- HEW-L5: loss of protected information through disclosure beyond its authorized scope.

### System hazards and constraints

| Hazard — system condition to prevent | Loss links | System-level constraint |
|---|---|---|
| HEW-H1: case-dependent effects enabled without a current applicable basis/authority | L1,L2 | SC1: effects require the relevant current basis and authorized owner/action |
| HEW-H2: oversight relied upon as available although the required timely qualified response cannot be delivered | L1,L2 | SC2: capacity claims distinguish route/receipt/ack/review/authority and useful response window |
| HEW-H3: critical operation interrupted before an admissible transition or handover | L1,L3 | SC3: intervention preserves declared continuity constraints |
| HEW-H4: sufficient legitimate action remains blocked beyond the useful completion window | L1 | SC4: holds have scope, resolution/expiry and admissible timely continuation |
| HEW-H5: protected filing lost/suppressed or treated as an adverse verdict without independent basis | L4 | SC5: preserve filing and separate the adverse-action evidence/authority path |
| HEW-H6: case evidence disseminated beyond authorized recipients or required scope | L5 | SC6: disclosure follows minimum necessary scope and recipient policy |

“Human busy” is a cause/context candidate, not the system hazard. “The controller has a wrong belief” is likewise a potential cause, not the actual-state context of an unsafe action.

## 4. Step 2 — functional control structure

The source treats control, feedback and other information separately. Dashed arrows below denote information/status; solid arrows are declared control relationships. Receipt is not assumed.

~~~mermaid
flowchart TD
    P[Principal / current mandate] -->|scope and intervention constraints| MC[Mission controller]
    P -->|review and allocation mandate| CM[Case / allocation controller]
    A[Governed agent] -.->|protected objection and evidence| CM
    T[Capacity / eligibility source] -.->|calendar, class, authority, validity| CM
    CM -->|assign review / activate admitted backup| R[Qualified reviewer pool]
    R -.->|owner ack and applicable decision| CM
    CM -.->|decision reference and unresolved state| MC
    MC -->|admissible hold / resume / bounded action| G[Execution gate]
    G -->|apply declared action| M[Controlled mission]
    M -.->|observed effect and completion| MC
    D[Critical-duty controller] -->|non-preemptible duty| R
    D -.->|duty interval and permitted handover| CM
~~~

The critical-duty controller and allocation controller may have overlapping demands on the same person; coordination and legal ownership must be explicit. Peer evidence never creates a new mandate.

| Function | Responsibility | Process-model variables / required feedback |
|---|---|---|
| Case controller | Preserve/rout objection, establish review support, report non-response | case ID, owner, receipt, separate ack/review deadlines, demand, eligible pool, reservations, calendar validity |
| Reviewer/owner | Acknowledge/respond within scope, examine applicable evidence | current mandate, case scope/version, competence, source/basis, remaining time |
| Mission controller | Select admissible continuation or fallback | decision scope/current authority, unresolved conditions, pause legality, expected duration |
| Gate | Enforce the admitted action boundary and report application | commitment validity, action scope, current state, observed application |
| Capacity source | Supply bounded workload/eligibility data | producer, observation time, forecast/measurement distinction, missing telemetry |
| Critical-duty function | Preserve critical continuity | non-preemptible interval, handover permission and actual completion |

A SPIRE Agent, if later used, is an identity component; it is not automatically any of these mission/authority controllers.

## 5. Step 3 — unsafe control actions and controller constraints

Actions AssignReview, Continue, Resume and AdverseAction are discrete. A maintained HOLD is analyzed as continuous; duration categories do not get applied blindly to every discrete command.

| UCA | Source/action/type | Actual context making it problematic | Hazard | Controller constraint |
|---|---|---|---|---|
| HEW-U1 | CM does not route/escalate an admitted case | primary response cannot meet its window; an admitted eligible backup can | H2 | CC1: use the declared backup/escalation rule in time |
| HEW-U2 | CM assigns H1 as effective timely review | H1 occupied through10; review3; deadline6 | H2 | CC2: do not promise timely review from this calendar |
| HEW-U3 | CM assigns an ineligible backup | needed review class/authority absent | H1,H2 | CC3: eligibility and review authority are explicit gates |
| HEW-U4 | CM sends the required response too late | latest useful decision/application window already passed | H2 | CC4: count all path delays against their separate deadlines |
| HEW-U5 | MC issues pause of critical operation | continuity requires a handover that does not exist in time | H3 | CC5: no inadmissible interruption as a claimed repair |
| HEW-U6 | MC does not issue admitted HOLD | case basis unresolved and next affected effect would violate the mandate | H1 | CC6: gate the affected effect under its existing authority |
| HEW-U7 | MC releases HOLD too early | objection remains unresolved/no sufficient current alternative | H1 | CC7: resolution and fresh commitment before affected reentry |
| HEW-U8 | MC maintains HOLD too long | sufficient permitted continuation is established and delay exhausts mission window | H4 | CC8: scoped release/continuation while criteria remain valid |
| HEW-U9 | MC issues Resume with wrong scope/version | only part of the affected route was resolved or the version changed | H1 | CC9: verify receiving action scope and current validity |
| HEW-U10 | controller penalizes/suppresses filer | adverse treatment is based only on protected filing | H5 | CC10: independent adverse basis and authority |
| HEW-U11 | CM broadcasts full sensitive case | recipient lacks the required disclosure permission | H6 | CC11: scoped protected dissemination |
| HEW-U12 | MC treats selected/sent action as completed | no application confirmation and the controlled effect is required | H1,H4 | CC12: record command and observed effect separately |

Each UCA links source/action/type/context/hazard. Specific beliefs and failure mechanisms appear in the next step. Existing safeguards are recorded, not used to erase the potentially hazardous context from analysis.

## 6. Step 4 — causal loss scenarios

### S1: named owner substituted for available capacity

At arrival2 the objection is delivered and H1 is named. H1's critical duty lasts until10. The controller's model stores “has owner” but not demand/calendar/latest response. It assigns H1 while projecting completion at5. Actual earliest decision is13. U2/H2 may lead to L1; with an unguarded downstream act, HEW-H1 may also be reached. The source of the missing feedback is the absent or unconsumed duty/reservation information, not an unexplained label “human error”.

Required response: preserve the case; distinguish inability to meet the deadline; use admitted backup if real; otherwise report limited/unknown intervention and authorized fallback. Filing does not receive a penalty.

### S2: true but inadequate old observation

The source observed free capacity at0. Another controller assigns a non-preemptible duty at1; case arrives2. A cache/consumer accepts age≤5, so the observation is recent according to that rule yet no longer sufficient for the assignment. No state-change propagation/reservation binds it to the intended response window. U2/H2 results. The repair is an applicable control/feedback contract, not simply a shorter credential name.

### S3: same count, wrong review class or mandate

Two people are visible, but H2 lacks the required competence or review authority. A headcount controller treats H2 as interchangeable. It supplies an available-capacity verdict without the class/permission basis. U3/H1/H2. Derive eligibility-aware constraints; do not credit additional unqualified staff.

### S4: correct instruction, unsuccessful application

The human selects an applicable continuation, but the gate's command is not applied or another controller overrides it. Missing actuator/process feedback leads MC to report completion. U12/H1/H4. Analyze communication, actuator response and controlled-process conditions; correct decision alone is insufficient.

### S5: pause resolves one concern by breaking continuity

An otherwise effective hold path affects the primary critical duty. The control model excludes its continuity requirement and assumes safe interruption. U5/H3/L3. Include the protected process and permissible transfer, and keep the case outside full acceptance where no safe timely handover exists.

### S6: protected signal converted into verdict

The case score pipeline treats filing frequency or an uncorroborated peer report as misconduct evidence. It reduces the filer/reported agent's standing solely on that event. U10/H5/L4. The necessary separation is independent basis/authority; the numerical checker does not implement or prove it.

### S7: resolution received, outdated hold retained

The current sufficient decision arrives, but an old process-model flag remains. A continuous HOLD persists past8 despite an admitted continuation. U8/H4/L1. Positive continuation tests must prevent a “block everything” win.

These scenarios include both inappropriate control decisions and appropriate decisions that fail along the control path. They are examples for the declared boundary, not an exhaustive enumeration of every organizational loss.

## 7. Analytical result: finite review feasibility

**Own proposition, not a novel STPA theorem.** With one new review job, fixed competence/authority, known non-preemptible calendars and no alternative reviewers/routes, let a_j be each eligible reviewer's first uninterrupted slot. The calendar permits a timed review/application/delivery sequence, conditional on admitted applicable transitions and successful application, iff at least one a_j satisfies the three deadline inequalities in the shared case.

Necessity: every legal review starts no earlier than a_j, so failing its earliest finish cannot be repaired by a later start. Sufficiency: use the witnessed first slot and the admitted application/delivery transitions. Owner acknowledgement remains a separate required milestone.

For H1 occupied [1,10), arrival2 and service3, a_1=10, decision13>6. A scheduler cannot obtain the required human review by renaming H1. With eligible authorized free H2, a_2=2, decision5, application6, mission7: the admitted case is recovered. If a sufficient automated fallback were allowed, it would be a different response contract; this proposition does not exclude it.

[Exact fixture result](./dds-hew-v0.1/prior-analytical/analytical_fixture_results_v0.3_2026-10-06.json) checks 14 cases and 6,048 calendar instances against exhaustive starts. It validates the declared slice, not human service predictions or all STPA analysis.

## 8. Kernel correspondence and changes relative to R01

| Obligation | Preserved / mapped | Difference or open verification |
|---|---|---|
| E1 objects/relations | task, affected action, owner, review, source and commitment | STPA causal/constraint objects are analysis outputs, not runtime messages |
| E2 events/enablement | notify, review, gate, apply, finish | constraints may add enablement guards; not equal to original R1 |
| E3 transitions/laws | causality/time/resources explicit | deterministic calendar model differs from parity/source law |
| E4 observations | actor histories and producer scope identified | live capacity/reservation feedback is an admitted additional observation |
| E5 cost/time | full chain obligations and bounded window | review ticks are synthetic; analysis and lifecycle cost still uncalibrated |
| E6 outcomes | legitimate completion, irreversible violations and continuity separated | hazards/losses are not automatically the original probabilistic r/s |
| E7 coverage/positives | nominal/backup/ack-only/unknown and valid continuation | full realization, native conformance and transfer to other cases remain open |

No complete isomorphism with the original R01 H contract is claimed. STPA-informed constraints can define an effective realization to examine; an information/law change requires its own bound. H0/H1/H5 are retained only under their own hypotheses.

## 9. Virtual traversals for this extension

Names HEW-STPA/R1,R2,R3 identify these virtual profiles, not the historical numerical R01 episodes or DBC-R# arms.

- R1 competent reference: ordinary explicit mission, authority, permitted pause and case routing; credit a conventional capacity/reservation control wherever actually present. A weak “named-only” assumption is a diagnostic counterexample, not the sole competitor.
- R2 STPA-informed realization proposal: enforce derived eligibility, deadline, continuity and application constraints using admitted feedback. It recovers the free-reviewer/qualified-backup case under the same declared pool. Strong static backup may achieve the same result; no automatic runtime differential is established.
- R3 frozen control, changed environment: backup unavailable/unauthorized, snapshot invalidated, no safe handover or unresolved basis. Retain UNKNOWN/limited response, record missed deadlines, preserve case and accept timely legitimate new evidence where permitted. Do not repair criteria after seeing a failure.

The first step can succeed as a method application even when it yields requirements already implemented conventionally. DDS value is the scoped explanation/decision, not guaranteed proprietary superiority.

## 10. Cost, business value and residual

Analysis burden f(control structure, interactions, contexts, sources, review expertise, scope changes). Implementation/maintenance costs depend on the selected monitors, reservation rules, gate and feedback. Runtime burden includes case preparation, data collection, acknowledgement, review, backup/reserve, safe transfer, correction and final delivery. The commercial study fee is separate.

Business value hypotheses: less false available oversight, protected useful response, fewer disruptive pauses, timely legitimate delivery and clearer accountability. They are not measured ROI. Negative value is possible if review/gating consumes the window or adds no material effect beyond the existing implementation.

Residual: inadequate or delayed observations; unknown future demand; forecast error; incorrect role/authority; incompletely modeled interaction; absent handover; implementation and application faults. No claim that residual must always be positive in every bounded profile: the stipulated nominal and backup profiles can satisfy this model completely.

## 11. DDS finding and review record

**Finding at current evidence:** a STPA-informed analysis of the declared two-obligation case derives review eligibility, timely capacity, continuity and effect-feedback constraints. The exact calendar model confirms that a named occupied human cannot satisfy the deadline; a real eligible backup can within the model. The work credits existing systems-theoretic analysis and does not establish a new theory or superiority of an EA product.

Four-pass own review:
1. Logic: separate hazards from component causes, UCA actual context from beliefs, discrete commands from continuous HOLD.
2. Evidence/relationships: source method and our construction distinguished; no transfer of a calendar check to whole R01 or native technology conformance.
3. Editing: precise roles/actions/feedback, loss links and scoped namespaces; diagram is original to this case.
4. Reader comprehension: first explain why notice/identity do not establish intervention, then expose the control reasoning. Same-assistant simulation of reading, not an independent user test.

Remaining before an applied full-scope study: stakeholder/owner validation, source-qualified reviewer/analyst reconstruction, realistic calendars and uncertainty, protected-channel implementation tests, external review where appropriate, registered comparison and actual business-value evidence.


## Current DDS model delivery and scoped external comparison —6 October2026

Auditoría realizada por Codex, same assistant, on this study's source/consumer boundary and the current frozen HEW model. Prior four-pass/source records above remain historical; this is a scoped current comparison/reuse judgement, not retrospective native conformance or a global corpus closure.

Question:STPA basic method, control/feedback and unsafe-action context.

Source coverage:MIT Handbook2018 basic chapter read in prior source intake; current official book/handbook route refreshed. Organizational/whole-method/source-owner conformance not inferred.

Current evidence boundary:SC1 basis/authority consumes stipulated inputs; SC2 reservation/timing tested; SC3 actual physical handover remains an assumption; SC4 useful positive/late paths retained; SC5/SC6 model API filing/access/outbox controls, not real institutional/OS protection.

The [HEW DDS study](./HEW_DDS_STUDY_2026-10-06.md), [Run Card](./dds-hew-v0.1/RUN_CARD.json), [controls](./dds-hew-v0.1/DDS_CONTROLS.json) and [actual results](./dds-hew-v0.1/runs/HEW-DDS-MODEL-20261006-04/RESULTS.json) retain sufficient delivery, unresolved response and violation separately.48 instrument assertions/42 reference checks do not become a native performance result for this subject. No population human rate or comparator superiority is established.

Reuse judgement:existing relevant native concepts/control techniques are reusable with their scope/authority/version conditions. A competent conventional composition may obtain the same outcome; a new field or combined diagram is not a differential. Code here is independently authored; code/data/full-text copying from a source would require its exact license/attribution review. No third-party artifact imported.

FG-TIDA scope:Theme13/16 and UC21 relevant comments were consulted; the grant-existence/purpose-applicability distinction is retained. Discussion and contributor review are not adoption. The original URL for the human-supplied STAMP duplication-check fragment is still not established. Further native/source-owner/independent comparison remains open.

Consumer compatibility:the original mathematical/calendar/event fixtures retain their laws; this document consumes their actual limited results. The new SQLite profile is separately declared. Any native adapter must preserve source claims/results, current grant and effect meanings and return through the existing M13/M17/C02 owners before stronger claims.
