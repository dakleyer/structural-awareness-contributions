# Regime Awareness as a Precondition for Trust and Human Oversight

> **Public traceability ID:** `FG-TIDA-T16-TEGRITY-01`
>
> **Current discussion entry:** [FG-TIDA themes issue #16](https://github.com/FG-TIDA/themes/issues/16)
>
> **Status:** Public working contribution by Ivan Abril / Tegrity.AI. The identifier above is self-assigned for traceability; it is not an official ITU contribution number, adopted text, endorsement or acceptance.

## Core contribution

**Trust and escalation remain meaningful only while the assumptions, evidence and intervention conditions on which they depend are still valid in the current operating regime.** Regime awareness should therefore be treated as a precondition for trust decisions, escalation and return to operation—not as an optional monitoring layer added afterwards.

The same test exposes the limits of human oversight. A human may be formally present and authorized while no longer having sufficiently current evidence, enough time, adequate review capacity or an intervention path capable of changing the outcome. At that point the architecture should recognize degraded or insufficient oversight rather than continue to describe the arrangement as human-controlled.

## The operational gap

The current FG-TIDA discussion usefully develops bounded human authority at the agent-action boundary: exact action, relying party, policy version, validity interval, mandate and reconciliation. A prior question must also be answered: **is the system still operating in a regime in which those trust and oversight mechanisms remain valid and effective?**

The same trust event may require different responses under normal, degraded, congested or adversarial conditions. A trigger, escalation route and formally authorized reviewer do not by themselves establish effective oversight when:

- the available evidence is stale, incomplete or ambiguous;
- the affected scope has grown beyond the reviewer’s reachable control surface;
- the authorized intervention is no longer available or cannot propagate far enough;
- the review queue exceeds the available human capacity;
- the time needed to decide is longer than the interval in which the action remains preventable or reversible; or
- the system has no safe fallback when timely review is impossible.

This is not a proposal for a single oversight architecture. It is a proposal to require explicit evidence that the **trust basis, escalation path and human oversight capacity remain valid** under the current operating condition.

## Proposed assessment chain

**trust or runtime event → evidence confidence and freshness → operating condition → affected and reachable scope → available intervention and capacity → response deadline → human authority → bounded mandate → permitted action, refusal or indeterminate state → safe fallback → evidence and reconciliation → return-to-operation condition**

This structure links four distinct questions:

1. **Is the trust basis still valid?** The system must know which assumptions, reference conditions and evidence windows support the current trust decision.
2. **Has the operating regime changed?** Observable departures must be able to invalidate or qualify trust, escalation and return-to-operation decisions.
3. **Can the human-led process still decide in time?** Evidence quality, review capacity, queue depth, criticality and decision latency must remain compatible with the response window.
4. **Can the decision still change the outcome?** The authorized intervention must reach the relevant actors, actions or infrastructure before the effect becomes irreversible.

## Candidate requirements

An implementation-neutral requirements matrix could ask systems to:

1. declare the operating regime, reference conditions and evidence-validity assumptions supporting trust and human review;
2. identify observable triggers that invalidate those assumptions, qualify trust or move the system into a degraded oversight state;
3. distinguish affected scope from the scope the reviewer and available controls can actually reach;
4. record review capacity, intervention latency and the last responsible decision time for critical event classes;
5. distinguish the **presence** of a human escalation route from its demonstrated **effective capacity**;
6. define refusal, hold, restricted-operation, automated containment or other safe fallback when timely informed review is not possible; and
7. require reevaluation of evidence, regime, action and mandate before returning to automated operation.

## Why this belongs in FG-TIDA

The [FG-TIDA Terms of Reference](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx) explicitly include runtime trust control mechanisms, trust lifecycle management, human oversight and behavioural trust signals. The contribution therefore stays within the Focus Group’s technical pre-standardization scope: it proposes operational properties and assessment questions for trust architectures rather than general AI governance.

The note is intended to complement work on bounded authority, identity, attestation, policy, action admission and trust evidence. Exact-action authority can be correctly designed while the broader oversight path is still too slow, under-informed or unable to reach the affected system. Conversely, adequate capacity does not make an unauthorized or poorly evidenced intervention legitimate. Both layers are necessary.

## Research lineage

- [Structural Awareness Programme](https://tegrity.ai/structural-awareness-program/)
- [Regime Awareness in Adaptive Systems](https://tegrity.ai/series/regime-awareness-in-adaptive-systems/)
- [The Limits of AI Oversight](https://tegrity.ai/the-limits-of-ai-oversight/)

These sources provide the conceptual and operational lineage of the contribution. They do not imply adoption by FG-TIDA or validation by ITU.

---

**Ivan Abril / Tegrity.AI**

[ivan.abril@tegrity.ai](mailto:ivan.abril@tegrity.ai)
