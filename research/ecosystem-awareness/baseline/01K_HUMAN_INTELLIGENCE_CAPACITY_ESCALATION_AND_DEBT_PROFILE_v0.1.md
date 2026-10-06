# Annex 01K — Human Intelligence Capacity, Escalation and Debt Profile

**Status:** additive public working extension, v0.1, 6 October 2026. This is an **Ecosystem Positioning-related Human Intelligence / Human Escalation extension hosted in the EA folder for lineage and routing**. It remains outside the EA core, outside the controlled/frozen baseline and outside the semantic ownership of Ecosystem Signalling, Regime Awareness, MSCA or Repositioning. It does not define a universal cognitive metric, a staffing standard, a mandatory human-in-the-loop architecture, an ITU-T deliverable or an adopted FG-TIDA requirement.

**Terminology boundary:** humans are not tokens. **Human Intelligence Tokens (HIT)** are a working accounting unit for demand placed by a system on scarce, qualified human cognitive capacity. They are not a unit of human worth, headcount, labour time or legal responsibility.

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

## 2. Human Time and Human Intelligence are different resources

For a human-review path, retain at least two different resource dimensions:

~~~text
HumanCapacity_j(W) = [
  HumanTime_j(W),
  HumanIntelligenceCapacity_j(W)
]
~~~

where W is the relevant response window.

**Human Time** represents temporal availability consumed by the system.

**Human Intelligence Capacity** represents qualified cognitive capacity usable for the required judgement in the declared case, including where relevant interpretation, synthesis, contradiction checking, contextual reasoning, evidence assessment and decision formation.

The dimensions are deliberately non-fungible.

A person may spend sixty minutes repeatedly observing a screen and clicking "Yes" on routine cases. That can consume substantial Human Time while producing little new qualified human intelligence. Repetitive low-value monitoring may also reduce the effective cognitive reserve available for a later difficult intervention.

Conversely, a short intervention may require high cognitive demand if it requires specialized competence, contextual reconstruction, conflicting evidence assessment or consequential judgement.

Therefore:

~~~text
HumanTime consumed
!=
HumanIntelligence consumed or produced
~~~

and headcount alone establishes neither.

## 3. Human Intelligence Tokens (HIT)

A **Human Intelligence Token (HIT)** is a normalized, deployment-relative accounting unit for demand on qualified human cognitive capacity.

For case i:

~~~text
Demand_i = [
  t_i,
  h_i
]
~~~

where:

- `t_i` = Human Time demand;
- `h_i` = Human Intelligence Token demand.

HIT is intentionally not defined as a universal biological or psychological constant. A deployment may calibrate it using its own task classes, reviewer competence, complexity, evidence volume, ambiguity, consequence and observed service characteristics.

A useful implementation may initially use ordinal or normalized classes rather than pretending to possess a precise universal cognitive scale.

The architectural requirement is the separation, not one mandatory numeric calibration.

## 4. Qualified capacity, degradation and debt

For a reviewer or reviewer pool J in response window W:

~~~text
HIT_available,J(W)
=
HIT_nominal,J(W)
-
HIT_committed,J(W)
-
HIT_degradation,J(W)
~~~

The degradation term is a working representation of capacity loss associated with fatigue, sustained monitoring, context switching, repetitive approval work or other declared factors. This annex does not prescribe one physiological model.

A bounded working definition of **Human Intelligence Debt (HID)** is:

~~~text
HID(W)
=
max(
  0,
  HIT_demand_committed(W) - HIT_available(W)
)
~~~

Human Intelligence Debt means that the system has committed, queued or generated qualified cognitive demand that cannot presently be satisfied within the relevant response window under the declared reviewer pool and assumptions.

It does not mean that the organization lacks employees.

An organization may have enough nominal reviewers and reviewer-hours while still carrying Human Intelligence Debt.

## 5. Human Escalation as an existing architectural consumer/producer

Human Escalation is not owned by this annex and is not inserted as a new core EA function.

The current architecture already permits human-review and escalation paths as external or downstream capabilities. This annex only makes their finite capacity more explicit.

A Human Escalation path may:

- **consume** a qualified alert, objection, RepositionIntent, requalification request or other bounded signal;
- **consume** EHD-carried context required for meaningful review;
- **produce** acknowledgement, evidence, decision, refusal, request-for-evidence, escalation or no-valid-response state;
- **produce** a capacity state where the implementation exposes it;
- **return** its result through existing signalling / authority-response / requalification paths.

A successful route-to-human event is therefore not equivalent to a successful human intervention.

The path remains subject to competence, authority, information sufficiency, Human Time, HIT capacity, latency and the useful response horizon.

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
AND required HumanTime fits W
AND required HIT fits W
~~~

If capacity is not established, Repositioning must not manufacture it by naming a human.

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

The question is not "is there a human?" but:

> **Is there a qualified human path with enough time and Human Intelligence capacity for this alert to change the outcome inside the useful response window?**

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

ACC does not calculate HIT.

This annex does not issue ACC.

The coupling is:

~~~text
ACC defines admissible participation / escalation obligations
+
01K qualifies human capacity where used
+
01J/EHD transports the bounded signal
+
Repositioning/authority consumes the result without bypassing legitimacy gates
~~~

## 12. Validation route and evidence boundary

The existing [UC-EA-03](./UC-EA-03_v0.4_MAINTENANCE_FREEZE.md) remains the natural architecture-validation profile because it asks whether human oversight is actually authorized, informed, capacitated and timely and what the human action legitimately changes.

The [R01 Human Escalation / Whispering](./reductions/00G-R01/feasibility/HUMAN_ESCALATION_WHISPERING.md) line is the current richer virtual/analytical experimental route. It already accounts for human review, queue, time, cost and completion constraints. HIT/HID can be tested there as an additional declared capacity model without retroactively converting the existing virtual results into human-validated measurements.

No claim is made here that HIT is empirically calibrated, that HID predicts real reviewer performance, or that this extension outperforms competent conventional queueing/workforce models.

A useful falsifier is straightforward:

> If reviewer-minutes / conventional workload models explain the same bounded intervention outcomes with equal or lower burden, HIT adds no demonstrated differential for that case.

## 13. Canonical thesis

Human oversight is not an infinite external fallback.

But humans are also not a privileged interrupt inserted above the rest of the architecture.

The useful architectural distinction is:

> **Ecosystem Positioning may consume a Human Intelligence / Human Escalation extension to qualify whether a human-directed trigger is operationally meaningful. The trigger still travels through bounded signalling, is requalified by its receiver, may update Cartography and Regime Awareness, and remains subject to ACC, authority and response-window constraints during Repositioning.**

Human Time and Human Intelligence are separate resources.

A system may consume much Human Time while obtaining little qualified Human Intelligence.

A named human does not create capacity.

A routed alert does not create authority.

A human response does not erase contrary evidence.

And a repositioning proposal remains only a proposal until its required ACC / authority transition is legitimately established.
