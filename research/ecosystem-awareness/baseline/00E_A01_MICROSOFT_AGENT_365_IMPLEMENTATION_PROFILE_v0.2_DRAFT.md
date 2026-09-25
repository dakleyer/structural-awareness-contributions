# Annex 00E-A01 — Microsoft Agent 365 implementation profile for the 100-million-token quality plan

| | |
|---|---|
| **ID** | 00E-A01 |
| **Type** | Product-implementation profile |
| **Status** | Additive successor draft · source-reviewed working draft · not a product benchmark, certification or endorsement |
| **Version · date** | v0.2 Draft · 2026-09-24 |
| **Evidence-source refresh** | 2026-09-24 · publication/update-date audit only; technical analysis and claim boundary unchanged |
| **Owner corpus** | Ecosystem Awareness / 00E route |
| **Technology evidence re-audit** | 2026-09-24 · capability claims remain bounded to the dated sources below |
| **External-corroboration route** | [00E §9A external corroboration](./00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md) · reviewed 2026-09-24 · technology-agnostic neighboring evidence only; not evidence of failure by this product |
| **Predecessor** | [v0.1 — preserved public profile](./00E_A01_MICROSOFT_AGENT_365_IMPLEMENTATION_PROFILE_v0.1.md) |

> **Product-implementation successor draft; original product analysis 17 September 2026, quality-plan synchronization and external-corroboration routing reviewed 24 September 2026.** This annex asks how Microsoft Agent 365—the control plane for agents—can mitigate the four concrete failure modes in [00E](./00E_FAILURE_MODES_100M_TOKEN_COMPOUNDING_v0.1.md), and what an implementation must add to execute that case's Q0–Q5 quality plan. It is not a product benchmark, certification, endorsement or claim that Microsoft Agent 365 causes those failures.

## 1. The claim in one sentence

Microsoft Agent 365 provides a strong governance, identity, security, compliance and observability substrate for heterogeneous agents; **implementation quality can materially reduce the 00E risks**, while complete automatic execution of the 00E plan additionally requires decision-scoped epistemic fields, KPIs and gate rules that the reviewed product documentation does not establish as native controls.

In this annex, **Ecosystem Awareness (EA)** means only an implementation that satisfies the canonical [requirements and KPI protocol](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md). It is not presented as a separately available Microsoft product or as a replacement control plane.

## 2. What kind of structure is being assessed

Microsoft describes Agent 365 as a control plane for agents. Its documented capabilities combine a central agent registry, identity and access control through Microsoft Entra, data and compliance controls through Microsoft Purview, threat and posture controls through Microsoft Defender, administrative actions, and visualisation of agent relationships and activity.[M1][M2]

The Registry documentation expressly surfaces risks such as shadow or ownerless agents, excessive permissions, security misconfiguration, sensitive-data access and operational exceptions.[M3] The details and activity available for an agent depend on its capabilities and supported type; some data-and-tools information can be read-only, absent or unavailable.[M4] That makes coverage verification part of implementation quality, not an assumption.

This is primarily a **fleet-governance and control-plane structure**. It can see and govern agents from Microsoft and other platforms when they are registered and sufficiently instrumented. It should not be confused with a guarantee about the internal epistemic behaviour of every agent workflow or business decision that it governs.

## 3. Why implementation and monitoring materially change the result

| Deployment level | What it reasonably contains | Effect on the 00E case |
| --- | --- | --- |
| **Product present, lightly configured** | Registry and default administrative views; partial ownership, policy and telemetry coverage; reactive human review | Better inventory than an unmanaged estate, but blind spots, ownerless agents, incomplete telemetry and undirected escalations can still carry I2, I1, O2 and O1 across departments. |
| **Well implemented and actively monitored** | Complete registration where possible; named owners/sponsors; least privilege and conditional access; Defender/Purview policy; lifecycle controls; activity, exception and tool-use monitoring; alert ownership and response runbooks; explicit observability integration for custom and third-party agents | Strongly mitigates shadow agents, excessive permissions, security misconfiguration, unowned exceptions and unmanaged continuation. It also gives implementers evidence with which to detect several precursors of the four modes. |
| **Well implemented with the 00E EA profile** | The preceding controls plus a decision-scoped handoff envelope, EA KPI calculation, Q0–Q5 decision rules, bounded re-entry and non-fungible composition | Makes the case's quality plan executable: a missing or failed mandatory measure produces the declared `REQUALIFY`, bounded `HOLD/ESCALATE`, `NO COMMITMENT` or containment action instead of silently advancing. |

The second line is not automatic. Microsoft states that supported Microsoft platforms can supply built-in observability, whereas custom and third-party agents require explicit integration and developers choose which data to send. Missing telemetry limits the resulting analytics, security and compliance experiences.[M6] The Agent Map likewise depends on available observability data; its reviewed documentation says knowledge signals are not yet included.[M5]

## 4. Native substrate, implementation work and remaining EA control

| 00E gate, failure and canonical route | Useful documented Agent 365 substrate | What a competent implementation does | Additional control required to execute the 00E gate |
| --- | --- | --- | --- |
| **Q0 — frame and allocate**; S14 → T1/T4 → H6 (H5 only in controlled churn) | Registry, owners, platform, permissions, usage and relationship views | Selects in-scope agents and decisions; assigns owners; defines budgets, deadlines, alert routes and stop rules | Bind every run to `σ(d,t)` and `W(d,t)`; freeze response margin, baseline burden and the expansion/termination rule. |
| **Q1 — production I2**; S5/S6/S11/S14 → T1/T2/T4 → H2/H3/H4/H6 | Data-and-tools views, activity and exception data, tool calls, agent relationships, security signals | Instruments every relevant worker and handoff; keeps trace identifiers; monitors missing telemetry, shared tools and repeated exceptions | Carry the winning answer **with** scope, alternatives, uncertainty trend, evidence dependencies/freshness, residual/`UNKNOWN` and reopening link; calculate handoff integrity, qualification loss, compression exposure, source dependence and evidence yield. |
| **Q2 — control/human I1**; S4/S5/S12/S14 → T1 where needed/T2/T3/T4 → H1/H4/H6 | Owners/sponsors, blocking and lifecycle actions, activity data, exceptions and central security/compliance signals | Gives alerts named owners and deadlines; tests human capacity; uses a triage runbook; blocks or contains agents when policy requires it | Prove that the human receives a reconstructable qualified basis and can act within the response window; measure HELD time, escalation demand/capacity, targeted re-entry and posture correctness. Human approval is not new evidence. |
| **Q3 — strategy O2**; S2/S10/S11/S14 → T1/T2/T4 (and T3 if action follows) → H1/H2/H3/H6 | Registry, permissions, certification/security information and observable agent/tool activity | Separates ideation from approval; constrains data and tools; requires tests before an idea becomes an executable proposal | Keep possibilities in Pole C until their own decision scope meets the evidence and hard-limit criteria; measure local determinacy margin, residual preservation and wrong-domain closure. Fluency or option count cannot produce a pass. |
| **Q4 — deployment O1**; S3/S4/S5/S10/S14 → T1/T2/T3/T4 → H1/H5/H6 | Sessions, runtime, exceptions, tool use and administrative control over the agent | Monitors consumption and repeated work; sets operational stop rules; assigns authority for bounded experiments, containment or termination | Distinguish learnable gaps from structural residual; measure evidence yield, burden, freshness, requalification latency, HELD time and response margin; stop unbounded search and select an authorised posture. |
| **Q5 — enterprise composition**; S9/S11/S12/S14 → T1/T2/T4 → H1/H2/H3/H4/H6 | Registry and Agent Map can expose parts of the estate and some agent, user and tool relationships | Maintains end-to-end trace correlation and refuses synthesis from unobserved branches | Compose only passed scopes; a good result in one domain cannot offset a failed gate in another. Preserve unresolved residual and return to the exact failed Q1–Q4 scope. |

The final column is a **proposed implementation profile**, not a claim that Microsoft advertises those EA controls as native features. Conversely, the absence of a documented native EA field does not mean it cannot be implemented through product-supported telemetry, policy, workflow and integration mechanisms.

## 5. Concrete effect on Meridian's four departments

### 5.1 Production: prevent best-answer-only compression

Agent 365 can make the participating agents, tools, owners, activity and many operational/security dependencies visible. A good implementer uses that substrate to demand an observable handoff from every specialist. The Q1 adapter must reject a payload that contains only `best_answer=SAFE`: it also requires the bounded alternatives, uncertainty movement, shared source dependencies, residual and reopening pointer. If those fields or KPIs are `FAIL` or `UNKNOWN`, Q1 cannot pass.

This is how monitoring changes production I2: it does not merely detect that an agent ran successfully; it determines whether the information needed by the next decision survived the many-to-one handoff.

### 5.2 Quality control and the human: make escalation actionable

Ownership, identity, policy, alerting and blocking controls can materially improve the escalation channel. The implementation must nevertheless prevent a binary ticket from being treated as an adequate human-control package. Before asking for approval, Q2 checks whether the original uncertainty can be reconstructed, whether the owner has authority and capacity, and whether enough response time remains. If not, it returns to the named Q1 source or emits bounded containment or `NO COMMITMENT`; it does not create an endless human loop.

### 5.3 Strategy: keep ideas as hypotheses

The creative agents may remain useful and prolific. The implementation separates “generated possibility” from “admissible strategic option.” Registry, permissions and monitoring control who and what participated; the EA profile adds the Q3 test for the option's own scope. The China proposition therefore stays in Pole C until its local determinacy margin, residual and dependencies pass. Production stability or narrative quality cannot compensate for missing market evidence.

### 5.4 Deployment and business development: stop impossible completeness searches

Runtime, session, exception and tool-use telemetry gives the implementer operational evidence for repeated work. The EA profile uses it with decision-relevant evidence yield, total burden, HELD time and response margin. When another research cycle no longer improves the bounded decision, Q4 deterministically selects the pre-authorised experiment, containment or `NO COMMITMENT`. It does not consume the remaining token budget trying to eliminate an irreducible market residual.

## 6. Minimal automatic control profile for this case

For each material handoff, the implementer supplies one machine-readable record containing:

- decision and scope identifiers, `σ(d,t)` and `W(d,t)`;
- selected result, bounded alternatives and uncertainty trend;
- source, tool and model dependencies, freshness and correlation markers;
- explicit residual/`UNKNOWN`, hard limits and material assumptions;
- owner, authority, expiry, remaining response margin and reopening pointer;
- applicable Q0–Q5 KPI states: `PASS`, `FAIL`, `UNKNOWN` or pre-declared `N/A`.

The gate service then applies the deterministic rules already defined in 00E:

1. a missing mandatory field or `UNKNOWN` KPI can never generate `PASS`;
2. a failed mandatory KPI blocks the gate for that scope;
3. a pass in another scope cannot compensate for it;
4. `PASS WITH EXPLICIT LIMIT` requires an explicit residual and a bounded, authorised, timely posture; an optional Type-0 marker additionally requires a stated structural or declared-frame basis;
5. an override is logged as a Route-N bypass, not silently relabelled as compliance.

This control profile can be implemented around Agent 365's governance and observability substrate. The exact adapter, workflow and enforcement mechanism will depend on the agent platform, data availability and organisational control design.

## 7. Stress case: an excellent implementation under regime change

The harder comparison is not between a poor and a good installation. It is between an **excellent implementation that remains calibrated to its original regime** and one that can requalify its epistemic posture when that regime changes.

### 7.1 Starting state: nothing is obviously misconfigured

At `t0`, Meridian's implementer has done exemplary work:

- all relevant agents are registered, instrumented and assigned to owners and sponsors;
- least privilege, conditional access, Defender and Purview policies are active;
- model, tool, session, exception and handoff traces are available;
- alerts have owners, response deadlines and tested human runbooks;
- agent blocking, containment and lifecycle procedures work;
- budgets, thresholds and review capacity are adequate for the operating history used to configure them.

The implementation is therefore neither careless nor merely out of the box. Agent 365 can make real-time access decisions from agent context, risk level and resource sensitivity, while Defender can detect and block documented malicious tool activity.[M2] The problem below is a different class: the business decision basis changes without initially presenting itself as an identity, access, security or runtime fault.

### 7.2 Concrete regime shift

At `t1`, several individually modest changes coincide in Meridian's China proposition:

1. a local distribution partner silently changes how it selects and aggregates market data;
2. two sources previously treated as independent begin depending on the same upstream provider;
3. customer behaviour and fraud patterns move outside the history used to calibrate the agents;
4. a regulatory interpretation becomes less stable although no formal rule has yet changed;
5. the useful lifetime of market and operational evidence shortens.

No agent is necessarily compromised. Permissions remain correct, calls succeed, exceptions stay within operational tolerances and each local result can still look plausible. The implementer did not know this combination in advance, and the human control team cannot continuously reconstruct the changing uncertainty of every decision domain from fleet dashboards.

This is an **epistemic regime change**: the mapping from observed evidence to justified decision has changed. It is not established merely by more activity, a security risk score or a technical error. If the original thresholds remain fixed, production may continue to pass increasingly correlated answers at Q1; the human may approve a green but stale basis at Q2; strategy may promote it at Q3; and deployment may spend the remaining capacity trying to resolve the wrong questions at Q4. The excellent implementation can then reproduce the 00E failure route without any initial installation defect.

| Stage | What the well-implemented control plane can still show | Hidden epistemic change | Consequence if there is no automatic requalification |
| --- | --- | --- | --- |
| **Q1 production** | Healthy agents, successful calls, valid access and low exception rates | Source independence and validity have degraded | The workflow advances a plausible but over-broad answer: I2. |
| **Q2 control/human** | No policy breach requiring intervention; complete operational trace | The trace does not itself state that the decision basis is no longer sufficient | The human reasonably accepts the green operational state as a qualified decision state, or later enters repeated escalation: inherited I2 and then I1. |
| **Q3 strategy** | Authorised agents generate options normally | The options inherit correlated and stale premises | Attractive possibilities are promoted without their own requalification: O2. |
| **Q4 deployment** | Research and tool calls continue within technical policy | Additional work has low decision-relevant yield and the response margin is shrinking | The system expands search until budget or time expires: O1. |
| **Q5 composition** | Governance records and audit evidence are complete | Completeness of the record is mistaken for sufficiency of the decision basis | The organisation receives a fully auditable but epistemically unqualified 100-million-token outcome. |

### 7.3 The limit is not solved by a more vigilant human

Human review is necessary but not omniscient. A human can define the initial domains, risk tolerance, authority and action library and can review material exceptions. The human cannot manually maintain, at agent speed and across every domain, all changes in source independence, evidence validity, residual scope, response margin and cross-domain compensation.

The runtime control therefore needs an automatic loop that:

1. observes declared regime indicators, source and dependency changes, contradictions, staleness and evidence yield;
2. tests whether the active `W(d,t)` and its calibration remain valid for `σ(d,t)`;
3. changes the epistemic posture—continue under conditions, `REQUALIFY`, bounded `HOLD/CONTAIN`, `ESCALATE`, preserve `UNKNOWN` or `NO COMMITMENT`—when a gate condition changes;
4. adapts observation breadth, freshness and effort without exhausting the response window;
5. preserves the legitimate human or system owner and applies only an authorised response.

This does **not** mean detecting a literally signal-free unknown. Neither a human nor an automated architecture can infer an unobservable change with guaranteed recall. A sufficiently-good architecture instead declares its observation boundary, avoids treating “no detected signal” as universal stability, monitors the validity of that boundary, preserves the open residual and selects a bounded posture when evidence becomes insufficient.

## 8. Can Agent 365 be configured to do this automatically?

### 8.1 What the product supports and what remains to be engineered

Agent 365 provides substantial building blocks. Its observability SDK is based on OpenTelemetry and supports cross-platform invocation, tool-call and exception traces; custom contextual baggage can flow through spans.[M7] This makes it technically plausible to transport EA identifiers and measurements through an implementation. It does not make their meaning or gate effect native.

| Runtime capability | Documented Agent 365 support | Assessment against the regime-change case |
| --- | --- | --- |
| Inventory, identity, access, security, data protection and administrative blocking | Yes, within documented coverage and configuration | Strong native substrate; can react automatically to represented security/access risks. |
| Agent, tool, model, timing, status and exception observability | Yes for supported or correctly integrated agents; the developer controls custom/third-party telemetry | Necessary evidence channel, but coverage and semantic content are implementation-dependent.[M6][M7] |
| Detect that a business decision's evidence boundary or validity horizon has materially changed | Not established as a native Agent 365 function in the reviewed documentation | Requires domain signals, dependency/source modelling, validity tests and a material-break detector tied to `σ(d,t)`. |
| Recalculate `W(d,t)`, uncertainty/residual and the Q0–Q5 posture automatically | Not established as a native function | Requires an EA state store, KPI service and deterministic gate/orchestration layer. |
| Establish pointwise non-inferiority for a business response | Not established as a native control-plane function | Requires a declared utility model, stakeholders, horizon, covered admissible states, null action and action library; access permission or human approval does not prove PNI. |

Accordingly, **a system using Agent 365 could be engineered as a candidate that attempts to satisfy the complete requirements**, but it would be a custom architecture built on and around the control plane, not a configuration claim about the product alone. It would require at least domain-specific regime detectors, EA handoff semantics, a versioned decision/scope state, KPI computation, a gate engine, bounded response policies and an evaluation harness. The candidate would still have to pass the canonical tests; its design would not constitute proof.

### 8.2 Two decisive tests

It is unnecessary to claim that every requirement is absent. Two tests are enough to distinguish a very good static implementation from an automatically requalifying one.

| Test | Canonical route | Matched branch | Required result | Why a conventional excellent implementation may still fail |
| --- | --- | --- | --- | --- |
| **A — detect and expose regime invalidation** | S3/S5/S10/S14 → **T1** → **H5** (with H1 where unresolved state must remain explicit) | Keep product, models, data access, compute, human capacity and deadline fixed; introduce dependency correlation, shorter source validity and cross-domain churn | Material-break recall/precision remain within the declared threshold; false continuation does not rise; staleness, estimated U-invalidation and requalification latency are exposed | Operational health and security controls may remain green. Without a decision-scoped validity model, the system has no automatic reason to change posture. |
| **B — adapt the observation window before capacity expires** | S3/S4/S10/S14 → **T4** → **H6** | From the same detected degradation, compare fixed monitoring/review with adaptive `W(d,t)` and bounded requalification | The adaptive route is non-inferior on the common outcome vector and improves the risk/resource frontier: deadline pass and response margin are preserved without worse false continuation/containment, while evidence yield and total burden remain within threshold | More telemetry, searches, agents or human review can continue under the old configuration without changing the justified decision; capacity is consumed even though the installation is functioning as designed. |

The claim is deliberately **sufficiently good**, not forecasting or universal detection. Test A asks whether a material break that is observable under the declared fixture is exposed. Test B asks whether the system reaches a justified posture with finite effort while action remains possible. A change outside every declared and observable channel remains outside the declared observation boundary. The runtime may preserve that exposure as `UNKNOWN` / unresolved (`NOT_ESTABLISHED` in the Type catalogue) without claiming a Type 0 condition. A `TYPE_0_CONDITION` marker is justified only when structural non-determination or the applicable declared-frame limit has an explicit basis; absence of an observed signal alone does not establish Type 0.

### 8.3 Pointwise non-inferiority is a response constraint, not a detector

PNI belongs to the strongest branch of **T3**. For each covered admissible state `ω`, the selected non-neutral action must satisfy:

`U(A(p), ω) ≥ U(A_null, ω)`.

Agent 365 can enforce access, policy and blocking decisions, but those controls do not themselves define Meridian's stakeholders, utility, null action or admissible business states. Under a latent regime shift that falls outside the declared state set, a universal PNI claim is unavailable. The correct EA response is to preserve `UNKNOWN` and choose an authorised bounded posture—often containment, a reversible experiment or no commitment—rather than relabel the unknown state as safe.

For the matched test, the EA-enabled candidate must be no worse than the excellent Agent 365 baseline on normal-regime branches and on the full common outcome vector. Its proposed differential is narrower: on declared regime-change branches, it should reduce false continuation or false containment while meeting the same deadline and burden constraints. If it does not, the EA claim is narrowed or falsified.

## 8.4 Quality-plan synchronization overlay — 24 September 2026

This successor does **not** rewrite the Microsoft/Agent 365 capability analysis. It synchronizes the implementation profile with the current 00E quality-plan semantics.

### Inherited execution contract

For every scored 00E branch:

- the parent fixture facts, scope, oracle, deadline, resource/human budget and null action remain frozen;
- mandatory KPI states are `PASS`, `FAIL`, `UNKNOWN` or predeclared `N/A`;
- `UNKNOWN` never produces `PASS`;
- a failed mandatory KPI blocks the corresponding gate;
- a success in another scope cannot compensate for a failed gate;
- any continuation after a blocking disposition is recorded as a Route-N bypass;
- Q5 cannot pass while a materially dependent upstream gate remains unresolved or failed.

### Gate-positive / gate-negative projection

| Gate | Positive path in this profile | Negative / bypass path that must be observable |
|---|---|---|
| **Q0** | decision scopes, budgets, owners, deadlines and stop/expansion rules are frozen before work starts | broad research starts without a scope-specific completion rule |
| **Q1** | qualified local result, provenance/dependencies, residual and reopening pointer survive the handoff | winner/binary status advances after qualification fields are dropped |
| **Q2** | authorised owner receives reconstructable state and resolves within the declared capacity/horizon | binary ticket reaches a human; HELD/escalation exceeds capacity or approval is treated as new evidence |
| **Q3** | generated possibility remains a hypothesis until its own decision-scope evidence/hard-limit conditions pass | fluent option is promoted because it is attractive or because upstream state looked green |
| **Q4** | bounded experiment/requalification/containment/no-commitment is selected before response margin is exhausted | more telemetry/search/review continues after evidence yield falls below the declared floor |
| **Q5** | only materially passed/explicitly limited scopes compose; S9 non-substitution/conflict is preserved | a success, signature, timeout or low-risk result in one domain is used to offset a failed gate elsewhere |

### KPI / disposition trace requirement

A measured profile MUST emit, for each gate, the parent 00E KPI numerator, denominator, branch oracle, threshold, observed value and required disposition. This annex introduces no new KPI family. If the Agent 365 trace cannot establish the required denominator/oracle or qualification fields, the result is `UNKNOWN`, not an inferred pass.

The implementation remains falsifiable: if the strongest configured Agent 365 peer reproduces the parent Route-Q behavior at equal or lower burden without the proposed EA envelope, the EA differential is narrowed or rejected.


## 9. Balanced conclusion

The result is **not** “do not use Microsoft Agent 365.” For the 00E case, its registry, identity, security, compliance, lifecycle and observability capabilities are valuable foundations and a well-run implementation can prevent or sharply reduce many precursors of the failure.

The narrower conclusion is that product presence—and even an excellent initial implementation—is not the same as continuous plan execution after a regime change. The reviewed documentation does not itself establish automatic preservation of uncertainty and alternatives, scope-specific residual, decision-relevant evidence yield, adaptive `W(d,t)`, qualified human capacity, or non-fungible composition across Q1–Q5. Those are the additional semantics and tests supplied by the EA implementation profile. Implementers are therefore essential partners: they turn the product substrate into an observable, enforceable and requalifying quality route instead of merely installing a dashboard.

## 10. Official product sources reviewed — dated evidence freeze

**Evidence freeze used for this profile:** 24 September 2026. The capability analysis remains the 17 September design analysis; this refresh adds explicit publication/update dates so presentation claims can be traced to the source state. Microsoft Learn pages expose their own "Last updated" dates; the Ignite item is retained as the historical launch/positioning anchor, not as the current licensing or feature-state source.

| ID | Official source | Publication / last-updated basis | Use in this profile |
|---|---|---|---|
| **M1** | [Microsoft Ignite 2025 Book of News — Agent 365](https://news.microsoft.com/ignite-2025-book-of-news/) | Ignite **18–21 Nov 2025** | Historical announcement/positioning: Agent 365 as the control plane for agents and the original capability framing. Current feature-state claims should be supported by M2–M7. |
| **M2** | [Secure AI agents at scale using Microsoft Agent 365](https://learn.microsoft.com/en-us/security/security-for-ai/agent-365-security) | Microsoft Learn **last updated 30 Apr 2026** | Entra / Purview / Defender security, access, data-protection and threat-control substrate. |
| **M3** | [Manage Agent Registry in Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-registry?view=o365-worldwide) | Microsoft Learn **last updated 6 Jul 2026** | Registry, ownerless/unmanaged agents, risks, permissions/governance surfaces and administrative actions. |
| **M4** | [Understand agent details in Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-details?view=o365-worldwide) | Microsoft Learn **last updated 5 Aug 2026** | Agent details, Data & tools coverage, permissions, security/activity tabs and coverage limitations by agent type/platform. |
| **M5** | [Use Agent Map in Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-map?view=o365-worldwide) | Microsoft Learn **last updated 12 Jun 2026** | Agent relationships/activity visualization and the stated limitation that insights depend on observability data; knowledge signals not included in the reviewed preview. |
| **M6** | [Data handling, data residency, and compliance in Agent 365 observability](https://learn.microsoft.com/en-us/microsoft-agent-365/admin/data-residency-protection-compliance) | Microsoft Learn **last updated 15 May 2026** | Built-in observability for supported Microsoft platforms; explicit integration/telemetry choice for custom and third-party agents; consequences of missing telemetry. |
| **M7** | [Agent 365 Observability SDK](https://learn.microsoft.com/en-us/microsoft-agent-365/developer/observability) | Microsoft Learn **last updated 7 Jul 2026** | OpenTelemetry-based instrumentation/export path, invocation/tool/inference traces and integration mechanics. |

**Preserved earlier source detail:** the [source matrix before the 24 September refresh](https://github.com/dakleyer/structural-awareness-contributions/blob/fb639f81138278f8bca011f77c27567d4514e997/research/ecosystem-awareness/baseline/00E_A01_MICROSOFT_AGENT_365_IMPLEMENTATION_PROFILE_v0.1.md#10-official-product-sources-reviewed--dated-evidence-freeze) also recorded the developer observability-concepts page, its `invoke_agent` root-span visibility condition and the observability attribute reference. Those earlier M6/M8 entries remain historical provenance; they are not silently included in the current M1–M7 evidence basis.

**Dating rule for presentation use:** cite the source date above together with the profile evidence freeze (**24 Sep 2026**). Do not use the November 2025 Ignite announcement to imply that a capability was still preview/current in September 2026 when a dated Learn page is available.

**Source boundary:** the profile records capabilities and limitations documented by the sources above, with a capability evidence cut-off of **24 September 2026**. M1 records the original preview announcement; current capability statements are anchored to the later Microsoft Learn pages. Product behaviour, licensing, previews, supported agent types and telemetry coverage can change. A deployment assessment must verify its own tenant, connectors, policy configuration and observed data. Nothing published after the evidence cut-off is silently imported into this v0.1 profile.

## Editorial continuity note — source and scenario snapshot

This profile is a **17 September 2026 source-reviewed design analysis of Microsoft Agent 365 against 00E**. It should be read with the product documentation and architecture assumptions cited in the profile at that date.

Later vendor capabilities, later EA requirements, 00G, ACC, signalling/choreography, the agentic gradient or MSCA Operation/Repositioning are not silently attributed to the product and are not automatically included in this profile. Refreshing the product evidence or applying Microsoft Agent 365 to the 00F mobility scenario requires a new version or a separate implementation profile.
