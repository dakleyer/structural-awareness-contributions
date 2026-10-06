# Annex 01K — Human Intelligence Capacity, Escalation and Debt Profile

**Status:** additive public working extension, v0.1, 6 October 2026. This is an **Ecosystem Positioning-related Human Intelligence / Human Escalation extension hosted in the EA folder for lineage and routing**. It remains outside the EA core, outside the controlled/frozen baseline and outside the semantic ownership of Ecosystem Signalling, Regime Awareness, MSCA or Repositioning. It does not define a universal cognitive metric, a staffing standard, a mandatory human-in-the-loop architecture, an ITU-T deliverable or an adopted FG-TIDA requirement.

**Terminology and lineage boundary:** this annex does not redefine Human Intelligence Debt. **Human Intelligence Debt (HID)**, **Human Intelligence Contribution Ratio (HICR)** and **Human Intelligence Contribution Target (HICT)** are imported from the existing Tegrity.AI Human Intelligence Debt / Human Intelligence Gap series. The present annex only connects that architectural concept to Human Escalation and the Ecosystem Positioning signalling/repositioning interfaces.

## 1. Purpose and architectural boundary

Human escalation is often represented as if a named human, a queue or an approval step automatically created usable oversight capacity. The surrounding corpus already rejects that assumption: human oversight must be authorized, informed, capacitated and timely, and escalation consumes finite resources and response-window time.

This annex adds one bounded extension:

> **separate Human Time from qualified Human Intelligence demand, make human-escalation capacity explicit, and allow that capacity state to be consumed by existing Signalling, Cartography, Regime Awareness and Repositioning paths without turning the human into a privileged system interrupt.**

The extension does **not** insert a new core function into Ecosystem Awareness or Ecosystem Positioning.

It is consumed where useful by the existing architecture.

Principal neighbours:

- [01J — Ecosystem Signalling](./01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md);
- [04 — General Functional Interfaces / EHD](./04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md);
- [01C — EA ↔ Regime Awareness interface](./01C_EA_REGIME_AWARENESS_INTERFACE_ANNEX_v0.2.md);
- [01I — Agentic Citizenship Contract](./01I_AGENTIC_CITIZENSHIP_CONTRACT_HUMAN_GOVERNED_PARTICIPATION_PROFILE_v0.1.md);
- [Canonical MSCA Operation & Repositioning](../../../standards/minimum-sufficient-control/04_CANONICAL_MSCA_OPERATION_AND_REPOSITIONING.md);
- [UC-EA-03 — human oversight under bounded effective capacity](./UC-EA-03_v0.4_MAINTENANCE_FREEZE.md);
- [R01 Human Escalation / Whispering](./reductions/00G-R01/feasibility/HUMAN_ESCALATION_WHISPERING.md).

FG-TIDA public lineage motivating the interface includes the Theme #16 capacity-aware oversight discussion and the Theme #13 objection-channel / accountable-owner discussion:

- Theme #16 — regime-aware and capacity-aware human oversight: https://github.com/FG-TIDA/themes/issues/16#issuecomment-5462496736
- Theme #16 — consolidated working structure with oversight capacity: https://github.com/FG-TIDA/themes/issues/16#issuecomment-5479999938
- Theme #13 — objection-channel requirement: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5923844082
- Theme #13 — agent-originated objection / named accountable owner: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5985312999

These links establish contributor-level working lineage only; they do not imply FG-TIDA or ITU-T adoption of this annex.

## 2. Human Intelligence Debt is an architectural gap

The controlling conceptual source is [Human Intelligence Debt](https://tegrity.ai/human-intelligence-debt/), with the measurement refinement in [Measuring Human Intelligence Debt](https://tegrity.ai/meassuring-human-intelligence-debt/) and the accumulated/partly irreversible interpretation in [Architectural Entropy](https://tegrity.ai/architectural-entropy-how-mediated-systems-spend-human-exergy-and-the-partial-irreversibility-of-human-intelligence-debt/).

The architectural question is not "how much human review demand is waiting in a queue?" It is:

> **How much genuine human contribution could the current technological and architectural frontier make possible, and how much genuine human contribution does the actual socio-technical architecture elicit?**

The source framework defines:

~~~text
HICT_t = ideal Human Intelligence Contribution Target
HICR   = actual Human Intelligence Contribution Ratio

HID_t = HICT_t - HICR
~~~

At task granularity, the measurement programme operationalises the same distinction in cognitive hours and separates:

- **GIC — genuine information contribution:** human work that creates new information/judgement not mechanically obtainable from the available data, rules, models and technology;
- **NEO — necessary execution & oversight:** human work that remains structurally necessary even in a coherent architecture;
- **ACW — avoidable compensatory work:** human work created by fixable architectural fragmentation or mediation; this is the observed debt surface.

The measurement proposal expresses, among other quantities:

~~~text
HICR_time      = H_GIC / H_total
HID_observed   = H_ACW / H_total
HICT           = HICR + H_releasable / H_total
F-HICT         = HICR + rho_inf * (H_releasable / H_total)
HID_spent      = (1 - rho_inf) * (H_releasable / H_total)
~~~

This matters here because a Human Escalation interface can be fully operational in the narrow runtime sense and still be **architecturally debt-producing**.

A person may have time, competence and authority available, and the system may successfully route one hundred low-value confirmations to that person. Runtime capacity has not been exceeded. Yet the architecture may still be using scarce human cognition as compensatory middleware instead of eliciting genuine judgement, strategy, interpretation or exception handling.

That is Human Intelligence Debt in the sense relevant to this annex: **not a temporary queue deficit, but an architectural gap between feasible genuine human contribution and the contribution the designed system actually enables.**

The debt may compound over time. The source series further distinguishes a recoverable component from a spent component: architecture can release some misallocated capacity, while capability that has gone unexercised may require deliberate rebuilding rather than returning automatically.

## 3. Runtime Human Escalation capacity is a different variable

Human Escalation still needs a runtime capacity check, but that check must not be called Human Intelligence Debt.

For a reviewer or reviewer pool J inside response window W, a deployment may maintain a bounded operational state such as:

~~~text
HumanEscalationCapacity_J(W) = [
  qualified reviewer availability,
  Human Time available,
  competence / case fit,
  authority,
  queue / committed work,
  expected decision latency,
  response horizon
]
~~~

This answers:

> **Can this human path meaningfully intervene now?**

It does not answer:

> **Is the architecture using human intelligence well?**

Those are separate questions.

A reviewer may be AVAILABLE at runtime while the surrounding architecture is generating high Human Intelligence Debt.

Conversely, an architecture may be well designed to reserve human cognition for genuine contribution while a particular incident still finds the qualified reviewer temporarily UNAVAILABLE.

## 4. Do not make Human Intelligence Tokens the HID metric

This annex therefore does **not** define HID in Human Intelligence Tokens.

The source framework already has a coherent metric family based on HICR, HICT, cognitive hours, GIC/NEO/ACW, releasable capacity and the recovery coefficient. Introducing a token unit as the definition of HID would create a second construct over the existing one and would blur the distinction between architectural debt and runtime escalation capacity.

A deployment may still use a local normalized workload unit for scheduling or queue admission if useful. If such a unit is informally called a **Human Intelligence Token (HIT)**, it must remain an implementation-local operational ledger and MUST NOT be interpreted as:

- a universal unit of human intelligence;
- a unit of human worth;
- the definition of Human Intelligence Debt;
- a substitute for HICR/HICT;
- evidence that high cognitive load equals high genuine contribution.

The architectural design test is instead whether the interface moves human effort toward **GIC / necessary oversight** and away from **ACW / avoidable compensatory work**.

For Human Escalation, the two gates are therefore:

~~~text
Gate A — Runtime viability
Can a qualified, authorized human intervene inside W?

Gate B — Architectural intelligence use
Is the interface designed to elicit genuine human contribution,
or is it consuming people as compensatory middleware?
~~~

Passing Gate A does not imply passing Gate B.

## 5. Human Escalation as an existing architectural consumer/producer## 5. Human Escalation as an existing architectural consumer/producer

Human Escalation is not owned by this annex and is not inserted as a new core EA function.

The current architecture already permits human-review and escalation paths as external or downstream capabilities. This annex only makes their finite capacity more explicit.

A Human Escalation path may:

- **consume** a qualified alert, objection, RepositionIntent, requalification request or other bounded signal;
- **consume** EHD-carried context required for meaningful review;
- **produce** acknowledgement, evidence, decision, refusal, request-for-evidence, escalation or no-valid-response state;
- **produce** a capacity state where the implementation exposes it;
- **return** its result through existing signalling / authority-response / requalification paths.

A successful route-to-human event is therefore not equivalent to a successful human intervention.

The path remains subject to competence, authority, information sufficiency, Human Time, qualified reviewer availability, latency and the useful response horizon. Separately, its interface design can be assessed against the HID framework to determine whether it elicits genuine contribution or creates avoidable compensatory work.

## 6. Human / systemic alert is a signalling profile, not a fifth signal class

A **Human / Systemic Alert** is a bounded signalling profile over the existing [01J](./01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md) and EHD semantics.

It is not a new primitive signal class and it is not a command.

Candidate trigger sources include:

1. **human-originated alert or objection** — a human identifies a material anomaly, objection, contextual contradiction or unsafe/unsupported condition;
2. **system-originated alert** — an agent, control, monitor or other system identifies a material condition;
3. **Regime Awareness material warning** — a qualified `Δ_RA`, overlay or requalification request indicates material regime/frame change;
4. **repositioning-time trigger** — effective-role drift, failed dependency, unresolved authority/ACC transition or another material condition is detected while Repositioning is already active;
5. **human-capacity trigger** — the Human Intelligence extension establishes that a planned escalation path is DEGRADED, UNAVAILABLE or UNKNOWN inside the useful response window.

These triggers may share one alert profile because they all require bounded routing and receiver-side qualification, but their source semantics remain distinct.

The trigger does not bypass the normal architecture.

A compact route is:

~~~text
human / system / RA / repositioning condition
-> bounded Human/Systemic Alert
-> EHD / Ecosystem Signalling
-> receiver qualification
-> Cart_i update where material
-> RA / local requalification where material
-> Repositioning or other legitimate consumer
~~~

If the alert is raised **during Repositioning**, the cycle may re-enter through the same qualified signalling / cartographic / regime path where the new information changes the represented position. Repositioning need not restart blindly, but it must not treat the alert as privileged truth.

## 7. Human consumers and subscription

A human may be a consumer of EHD / Ecosystem Signalling where the applicable interaction, ACC, policy or signalling profile routes information to that human or role.

A deployment may implement this as subscription, routing, notification, queue membership or another delivery mechanism.

This annex does not require a universal pub/sub system.

Human subscription means only that a declared class of qualified signals can be routed to that human/role under the applicable conditions.

It does **not** mean:

- the human becomes a central orchestrator;
- the human can interrupt or override every awareness/repositioning process;
- signal receipt establishes authority;
- notification establishes review capacity;
- silence implies approval;
- the rest of the architecture blocks until the human responds unless an applicable rule explicitly requires that behaviour.

A human is therefore one possible receiver in the signalling topology, not a privileged architectural super-node.

## 8. Repositioning-time use

Human/Systemic Alert and Human Intelligence capacity can be consumed during Repositioning.

The canonical Repositioning process already distinguishes opportunity, ACC admissibility, authority and response horizon. This extension adds an optional capacity qualification for transitions that materially depend on human intervention.

For candidate transition τ requiring human decision or review:

~~~text
HumanEscalationViable_i(τ,W)
=
qualified route exists
AND applicable human authority exists
AND qualified reviewer/case fit exists
AND required HumanTime fits W
AND expected decision latency fits W
~~~

This is deliberately a runtime-capacity test, not an HID formula.

A second, architectural question may be evaluated before the escalation pattern is adopted or when the interface is reviewed:

~~~text
HumanIntelligenceArchitectureFit_i
=
does the interaction primarily elicit GIC / necessary oversight
rather than ACW created by avoidable architectural fragmentation?
~~~

If runtime capacity is not established, Repositioning must not manufacture it by naming a human. If architectural fit is poor, the fact that a human happens to be available does not make the escalation design efficient or debt-neutral.

Possible bounded outcomes remain the existing ones, including:

- HOLD;
- ESCALATE;
- REQUEST_EVIDENCE;
- RECONTRACT;
- UNRESOLVED;
- an authorized fallback or alternative route where one exists.

In particular, Repositioning may remain **HOLD / UNRESOLVED** while waiting for a legitimate ACC successor, re-contracting decision or authority response. The absence of a new ACC does not authorize the candidate role, and a human alert does not override that contract gate.

## 9. Optional pre-trigger capacity calculation

An Ecosystem Positioning implementation may consume this extension **before** issuing a human-directed communication trigger.

The runtime question is not "is there a human?" but:

> **Is there a qualified, authorized human path with enough time and case-relevant capability for this alert to change the outcome inside the useful response window?**

A separate design-time question precedes that:

> **Should this interaction be asking a human at all, or is the architecture spending human cognition on ACW that a coherent system could remove?**

A preliminary state may be:

~~~text
HumanCapacityState
∈ {
  AVAILABLE,
  DEGRADED,
  UNAVAILABLE,
  UNKNOWN
}
~~~

UNKNOWN must not silently become AVAILABLE.

This state may be attached to or referenced by the alert so that downstream routing can select a backup pool, alternative authority, bounded fallback or explicit unresolved state.

The calculation is optional and extension-owned. Ecosystem Positioning may consume it; Ecosystem Positioning does not thereby become the semantic owner of Human Intelligence measurement.

## 10. Relationship to Regime Awareness

Regime Awareness remains the owner of qualified regime/frame-change assessment.

A material RA output may be selectively signalled through 01J and may become one trigger for downstream repositioning or human review.

This annex does not redefine `Δ_RA=[A_RA,B_RA,C_RA,D_RA]`, does not create a new RA output taxonomy and does not interpret a directional alert as automatic permission to act.

The receiver may incorporate the qualified RA information into its own Cartography and local decision frame before producing another signal or repositioning request.

Thus:

~~~text
RA warning
!= command
!= human escalation
!= repositioning decision
~~~

but a qualified RA warning may trigger any of those downstream processes under the applicable architecture.

## 11. Relationship to ACC

ACC may govern whether and how human escalation is required, permitted or constrained.

An applicable ACC/signalling profile may specify, for example:

- mandatory escalation conditions;
- named or role-based recipients;
- acknowledgement expectations;
- required evidence fields;
- non-retaliation / protected-objection conditions;
- maximum tolerated response delay;
- fallback or alternate-owner requirements;
- constraints on automated reliance on human approval;
- limits or policies for consuming scarce human-review capacity.

ACC does not calculate HID, HICR/HICT or runtime reviewer capacity.

This annex does not issue ACC.

The coupling is:

~~~text
ACC defines admissible participation / escalation obligations
+
01K qualifies runtime human-escalation capacity where used and imports the existing HID architecture test
+
01J/EHD transports the bounded signal
+
Repositioning/authority consumes the result without bypassing legitimacy gates
~~~

## 12. Validation route and evidence boundary

The existing [UC-EA-03](./UC-EA-03_v0.4_MAINTENANCE_FREEZE.md) remains the natural architecture-validation profile because it asks whether human oversight is actually authorized, informed, capacitated and timely and what the human action legitimately changes.

The [R01 Human Escalation / Whispering](./reductions/00G-R01/feasibility/HUMAN_ESCALATION_WHISPERING.md) line is the current richer virtual/analytical experimental route. It already accounts for human review, queue, time, cost and completion constraints. It can therefore test two different propositions without conflating them:

1. **runtime capacity:** whether a qualified human path is actually reachable and usable before the response window closes;
2. **architectural debt tendency:** whether an escalation/interface pattern removes or creates ACW and whether it moves observed human contribution toward the HICT frontier.

The canonical HID measurement programme remains the Tegrity.AI series and requires its own instrument-validation gate before publishing empirical HID values. This annex does not claim that runtime queue measurements are HID measurements, or that a successful human-escalation path reduces Human Intelligence Debt.

A useful architectural falsifier is:

> If an escalation design increases human review while the additional human work is predominantly ACW that a coherent architecture could remove, then successful routing has not demonstrated lower Human Intelligence Debt.

## 13. Canonical thesis

Human oversight is not an infinite external fallback.

But humans are also not a privileged interrupt inserted above the rest of the architecture.

The useful architectural distinction is:

> **Ecosystem Positioning may consume a Human Intelligence / Human Escalation extension to qualify whether a human-directed trigger is operationally meaningful. The trigger still travels through bounded signalling, is requalified by its receiver, may update Cartography and Regime Awareness, and remains subject to ACC, authority and response-window constraints during Repositioning.**

Runtime Human Time/capacity and architectural Human Intelligence Debt are separate constructs.

A system may remain inside its current reviewer-time budget and still increase Human Intelligence Debt if the interface structurally allocates human cognition to avoidable compensatory work rather than genuine contribution.

The architectural objective is not to "use more human intelligence" indiscriminately. It is to move actual contribution (HICR) toward the feasible architectural target (HICT) while preserving necessary execution/oversight and avoiding ACW.

A named human does not create runtime capacity.

A routed alert does not create authority.

A human response does not erase contrary evidence.

And a repositioning proposal remains only a proposal until its required ACC / authority transition is legitimately established.
