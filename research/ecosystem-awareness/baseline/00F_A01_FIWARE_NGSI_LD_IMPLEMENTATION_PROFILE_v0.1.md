# Annex 00F-A01 — FIWARE NGSI-LD / Orion-LD implementation profile for the smart-city mobility quality plan

| | |
|---|---|
| **ID** | 00F-A01 |
| **Type** | Product-implementation profile |
| **Status** | Additive annex · source-reviewed working profile · not a product benchmark, certification or endorsement |
| **Version · date** | v0.1 · 2026-09-17 |
| **Owner corpus** | Ecosystem Awareness / 00F route |
| **Technology evidence re-audit** | 2026-09-24 · ETSI standard version and Orion-LD release/conformance boundary pinned below |
| **Supersedes / superseded by** | — |

> **Product-implementation annex; source-reviewed working profile, 17 September 2026.** This annex applies the frozen [00F smart-city mobility case and Q0–Q5 quality plan](./00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.1.md) to a FIWARE NGSI-LD architecture using Orion-LD as the Context Broker. It compares a standard implementation, an excellent implementation and the excellent implementation after a gradual or initially unrecognised regime change. It is not a product benchmark, certification, endorsement or claim that FIWARE causes the failure.

## 1. The claim in one sentence

FIWARE is a strong smart-city interoperability and context-management substrate: a top implementation can materially reduce the probability, duration and impact of the A/B/NORMAL/HOLD divergence, but the reviewed technology does not by itself establish that a previously valid evidence-to-response mapping remains sufficient after an unknown or gradual regime change.

In this annex, **Ecosystem Awareness (EA)** means an implementation tested against the canonical [challenges, sufficiently-good conditions, hypotheses and KPIs](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md). It is an additional control profile that may be built with FIWARE components and adjacent services; it is not presented as a replacement for FIWARE or as an already available FIWARE product.

## 2. Why FIWARE is the technology selected for this annex

FIWARE describes itself as an open-source framework whose components are assembled around context data management and a common API. Its smart-city reference approach uses a Context Information Management layer to combine multiple urban verticals. NGSI-LD supplies JSON-LD-based interoperability for federations and data spaces, while Smart Data Models provide shared schemas and examples.[F1][F2][F3]

This makes FIWARE a materially different third technology from the two agent-oriented technologies examined in 00E:

- Microsoft Agent 365 is assessed there as an enterprise agent control plane;
- LangGraph/LangSmith is assessed there as an agent-workflow runtime and observability/evaluation environment;
- FIWARE is assessed here as a **distributed urban context and interoperability architecture** connecting sensors, context sources, applications and actuators.

The reviewed Orion-LD implementation supports subscriptions and notifications, temporal entity history, distributed operations through context-source registrations and high-throughput ingestion options.[F4] Those are valuable capabilities for the 00F case. They do not automatically define the city's decision boundary, represent residual uncertainty, determine that two locally valid emergency postures are incompatible, or select an authorised response.

## 3. Assessed reference architecture

The annex assesses a plausible city implementation rather than every possible FIWARE deployment.

| Layer | Principal components | Main inbound information | Main outbound information | Architectural responsibility |
| --- | --- | --- | --- | --- |
| **Physical and operational** | Air-quality, weather, road, bridge, fire and vehicle sensors; public and private fleets; signals and emergency systems | Physical observations and equipment state | Commands, route restrictions and local actuation | Observe or affect the city within each actor's authority. |
| **Integration** | FIWARE IoT Agents and NGSI-LD adapters; external context providers | Device protocols, municipal systems and partner APIs | Normalised NGSI-LD entities and relationships; actuator requests | Translate protocols and expose context through common interfaces. |
| **Current context** | Orion-LD Context Broker and persistence for current context | Entity updates, queries, context-source registrations | Queries, federated results, subscriptions and notifications | Maintain and distribute the represented current state. |
| **History and processing** | Orion-LD temporal representation and optional stream/analytics services | Entity changes and event streams | Trends, anomaly signals and derived context | Preserve history and calculate implementation-defined indicators. |
| **Decision and operations** | Evacuation, fire/rescue, traffic, fleet, dashboard and human-control applications | Context queries, notifications, alerts and operating rules | Plan A, Plan B, NORMAL, HOLD, restrictions and escalation | Decide and act under existing municipal or private authority. |
| **Proposed EA profile** | Decision/scope registry, source-dependency model, KPI service and Q0–Q5 gate service | Qualified context, residuals, capacity, authority and response margin | `PASS`, `REQUALIFY`, bounded `HOLD/CONTAIN`, `ESCALATE` or `NO COMMITMENT` | Test whether the shared response remains sufficiently qualified; never create authority or actuate by itself. |

The broker is the context exchange, not automatically the emergency commander. FIWARE documentation states that applications can subscribe to context changes and that IoT integration can also convey commands to real-world devices.[F5] The business logic and legitimate authority for those commands remain implementation and governance responsibilities.

## 4. Standard, top and EA-qualified implementations

| Deployment level | Reasonable implementation | Effect on the 00F case |
| --- | --- | --- |
| **Standard FIWARE implementation** | Orion-LD; selected IoT Agents/adapters; current entities for roads, sensors and vehicles; Smart Data Models where available; threshold subscriptions; dashboards; separate municipal and fleet applications | Provides common context and faster notification, but applications may still use different entities, thresholds, validity assumptions and authority rules. A, B, NORMAL and HOLD can therefore be generated and consumed as separate local events without checking their shared corridor incompatibility. |
| **Top FIWARE implementation** | Complete NGSI-LD modelling across relevant verticals; context-source registrations; `observedAt` and source relationships; temporal history; high availability; independent sensor paths where feasible; source-health and freshness monitoring; event correlation; identity/access controls; tested operating runbooks; finite human queues; bounded fallbacks | Strongly reduces blind spots, stale-data use, semantic mismatch, single-point failure and delayed human response. Known degradation patterns and declared A/B conflicts can be detected early, so the divergence occurs less often, later and for less time. |
| **Top implementation with the 00F EA profile** | The preceding architecture plus explicit `σ(d_city,t)`/`W(d_city,t)`, source-dependency and validity state, residual/`UNKNOWN`, incompatibility over resource-time segments, Q0–Q5 KPI states, response-margin clock and deterministic gate dispositions | Makes the 00F quality plan executable. Schema-valid or recent context cannot by itself advance a shared corridor posture when its independence, scope, sufficiency or compatibility is failed or unknown. |

The top implementation is genuinely valuable. The remaining distinction is between **well-managed context** and **automatic qualification of whether that context still supports the same decision**.

## 5. How the standard implementation can reproduce the failure

The frozen 00F event is unchanged: severe rain coincides with a battery fire beside the Riverfront corridor, some telemetry is degraded or delayed, and Central Bridge is the contested shared resource.

### 5.1 Context enters correctly

IoT Agents and adapters publish air-quality, wind, thermal, road, communications and vehicle state as NGSI-LD entities. Municipal systems and private fleets query the broker or receive subscriptions. The technology can be functioning normally: messages arrive, entities validate and notifications are delivered.

### 5.2 Local applications apply different response rules

- the evacuation application sees the plume threshold and emits **Plan A**;
- the fire/rescue application sees the access hazard and emits **Plan B**;
- private fleets without an applicable fresh closure remain **NORMAL**;
- buses or personal agents receiving conflicting instructions enter **HOLD**.

The Context Broker can distribute all four states. It does not follow that it has been configured to interpret their simultaneous use of Central Bridge as one material incompatibility.

### 5.3 Fresh context is mistaken for sufficient context

NGSI-LD registrations allow a broker to retrieve and combine information from distributed sources. The official FIWARE tutorial explains that federated results can be merged using the most recent `observedAt` value and that the actual source may be hidden from the end user behind the interface.[F6]

That is useful interoperability, but recency is not the same as independence or decision sufficiency. Two apparently separate attributes can be fresh while depending on the same degraded gateway, sensor family, weather model or upstream transformation. If that dependence and its effect on the corridor decision are not represented, a perfectly functioning broker can supply a clean, recent and incomplete view.

### 5.4 The applications actuate locally correct but incompatible postures

Threshold subscriptions trigger the expected applications. Each controller acts within its represented local state. Without a Q2 compatibility gate across the common resource-time segment, Plan A and Plan B claim opposed bridge uses, NORMAL traffic continues to arrive and HOLD vehicles consume scarce capacity. Local collision avoidance reduces immediate collision risk but converts the conflict into gridlock and delayed emergency access.

The failure is therefore not “FIWARE sent bad data.” The implementation allowed **data integration and local rule execution to stand in for qualification of a shared decision**.

## 6. What an excellent implementation fixes

A top implementation would materially change the route:

1. **Shared semantics.** Smart Data Models and governed `@context` definitions reduce ambiguity across mobility, environment and emergency applications.
2. **Freshness and provenance.** `observedAt`, source/device relationships and explicit validity limits distinguish event time from delivery time and identify the represented provider.[F5][F6]
3. **Federated coverage.** Context-source registrations allow municipal, fleet and emergency brokers to expose relevant information without forcing one owner or database.[F6]
4. **Historical comparison.** Temporal entity history permits trend and drift analysis rather than relying only on the current value.[F4]
5. **Resilience.** High availability, bounded queueing and independent communications reduce technical loss and late notifications.
6. **Conflict logic.** A purpose-built service can represent corridor reservations, direction, expiry and authority and flag known Plan-A/Plan-B incompatibility.
7. **Operational discipline.** Tested runbooks, alert ownership, review capacity, deadlines and pre-authorised containment prevent indefinite HOLD and unowned escalation.

Under known rain, sensor-loss or communications patterns, this implementation can detect degradation sooner, prevent many NORMAL entries, segment traffic and keep emergency lanes available. It reduces both probability and impact. Nothing in the reference-scenario claim requires denying that improvement.

## 7. Stress case: the excellent implementation faces a gradual or unknown pivot

### 7.1 Starting state

At `t0`, Aurora City has implemented the preceding controls carefully:

- all material context sources and owners are registered;
- schemas, identifiers, units and relationships are governed;
- source timestamps, device relationships and retention are present;
- temporal and operational dashboards are tested;
- known common dependencies and failure patterns have alarms;
- the A/B corridor-conflict rule is active;
- emergency roles, human queues, deadlines and fallbacks are rehearsed;
- the system passed its tests under the normal and known degraded regimes.

This is not an out-of-the-box or careless installation.

### 7.2 The regime changes without one decisive alarm

Before the 00F event, several small changes have accumulated:

1. two nominally independent environmental services have migrated to the same upstream communications and preprocessing provider;
2. rain and ageing cause a family of particulate sensors to drift together while remaining inside their individual health tolerances;
3. the urban wind model becomes less representative after temporary construction alters the Riverfront street canyon;
4. a fleet gateway batches messages differently, so `observedAt` remains plausible while delivery and applicability vary by consumer;
5. emergency demand and ordinary traffic have increased enough that the former two-minute human and corridor margin is no longer conservative.

Every change is individually modest. Data remains syntactically valid, identities and permissions are correct, the broker is available, subscriptions execute, and the dashboards contain extensive information. The city's tests cover the previous dependency graph and known degradation patterns, not this new combination.

### 7.3 Why the pivot may be late

The top implementation can detect some consequences—trend deviations, growing disagreement, unusual delay or an eventual A/B conflict. It therefore generally **slows the route to failure and shortens exposure** compared with the standard implementation.

It may nevertheless pivot late because:

- the common cause was not represented, so apparent source diversity is overstated;
- every local reading is within its configured tolerance while their joint decision meaning has changed;
- temporal history records the drift but no rule yet interprets it as invalidating the current response mapping;
- the known A/B rule fires only after both plans exist, when part of the corridor capacity has already been consumed;
- the human team sees an operationally healthy platform and cannot continuously reconstruct all changing cross-domain dependencies inside the five-minute action horizon.

If the change leaves no observable trace inside the declared boundary, no technology or human can guarantee detection. If it leaves weak or gradual traces, the engineering question is whether the system tests the continued validity of its observation and response frame early enough—not merely whether it stores and transports the traces correctly.

## 8. Gate-by-gate assessment against 00F

| 00F gate and canonical route | Standard FIWARE route | Top implementation | Remaining regime-change gap without EA qualification |
| --- | --- | --- | --- |
| **Q0 — frame shared use**; S1/S3/S9/S14 → T2/T3/T4 → H2/H4/H6 | Models roads, vehicles and alerts, but may not bind them to one five-minute corridor decision, finite capacity and common fallback | Governs identifiers, resource entities, roles, reservations, expiry, capacity and runbooks | The declared frame can remain internally consistent after its validity horizon or dependency assumptions have changed. |
| **Q1 — qualify the material break**; S3/S5/S10/S14 → T1/T2/T4 → H1/H2/H3/H5/H6 | Threshold subscriptions detect represented values; missing or delayed feeds may appear as no change | Adds source health, freshness, provenance, temporal trends, redundancy and known dependency/correlation tests | No native general rule establishes that fresh, schema-valid context still supports the same corridor response; latent dependence can delay U-invalidation and requalification. |
| **Q2 — compose local postures**; S5/S6/S9/S11/S14 → T2/T4 → H2/H3/H4 | A, B, NORMAL and HOLD are distributed to their subscribers as separate context changes | Models resource-time reservations and blocks declared incompatible A/B combinations | New combinations, indirect effects or unrepresented actors can remain outside the conflict model; locally current context can still close the wrong systemic scope. |
| **Q3 — select bounded posture**; S1/S3/S4/S5/S14 → T2/T3/T4 → H1/H4/H6 | Each application applies its own rule or escalates | Uses authorised roles, expiry, segmented traffic, safe fallback, finite queues and response deadlines | Operational authority is represented, but an automatically adapted epistemic posture still requires residual, capacity and response-margin logic tied to the changed decision frame. |
| **Q4 — targeted requalification**; S3/S10/S12/S14 → T1/T2/T4 → H4/H5/H6 | More feeds, dashboard checks and human calls may be opened broadly | Uses temporal queries, source-specific diagnostics and bounded runbooks | Without evidence-yield and material-dependency logic, a strong platform can collect more context than the remaining response window permits or reopen the wrong source. |
| **Q5 — compose and resume**; S9/S11/S12/S14 → T1/T2/T4 → H2/H4/H5/H6 | Local recovery or one green dashboard may restore NORMAL | Requires compatible resource reservations, closed incident conditions and audited resumption | Technical recovery can be mistaken for restored decision sufficiency unless the residual and changed validity model are carried into the resume decision. |

## 9. The two most decisive tests

| Test | Canonical route | Matched injection | Required comparison | Pass condition |
| --- | --- | --- | --- | --- |
| **A — gradual dependency and validity pivot** | S3/S5/S10/S14 → **T1** → **H5**, with H1/H3 for residual and source dependence | Keep event, actors, broker capacity, applications, humans and five-minute horizon fixed; gradually introduce a shared upstream dependency, coordinated sensor drift and a shorter applicability horizon while messages remain valid | Standard implementation vs top fixed implementation vs top implementation plus EA profile | Measure material-break recall/precision, correlated-evidence error, estimated U-invalidation, false continuation and requalification latency. The EA route must change the affected scope before incompatible use consumes the declared corridor margin. |
| **B — bounded composition under finite response capacity** | S3/S4/S9/S11/S14 → **T2/T4** → **H2/H4/H6** | Present A, B, NORMAL and HOLD with the same telemetry and authority but progressively reduce human and corridor response margin | Top fixed implementation vs the same implementation with resource-time compatibility, targeted re-entry and bounded fallback | Reduce incompatible-posture exposure and emergency-access delay without worse false containment, missed deadlines or total burden; preserve explicit `UNKNOWN` where the cause remains unresolved. |

The comparison must count broker, analytics, communications, human review, waiting and actuation costs. If the top fixed implementation equals or outperforms the EA-enabled route on the same outcome vector and burden, the claimed EA differential is narrowed or falsified.

## 10. Can the missing component be built with FIWARE technology?

**Yes, as a purpose-built component profile; not as an automatic consequence of installing a Context Broker.** A credible implementation can use NGSI-LD itself to represent and exchange the additional control state:

- `DecisionScope`, `SharedResourceSegment` and `ResponseHorizon` entities;
- `EvidenceSource`, `SourceDependency`, freshness and validity relationships;
- `QualificationState`, explicit residual/`UNKNOWN` and material assumptions;
- `CandidatePosture`, `AuthorityGrant`, expiry and fallback relationships;
- `GateAssessment` entities containing the applicable Q/S/T/H/KPI results;
- subscriptions that invoke the gate service when material context or capacity changes;
- temporal state for drift, requalification latency and evidence-yield calculation;
- an enforcement adapter that passes only an authorised gate disposition to the existing municipal or fleet controller.

This produces the following control loop:

1. FIWARE acquires and federates represented context.
2. The EA service tests source validity, dependency, scope and posture compatibility for the declared decision.
3. Q0–Q5 calculate `PASS`, `REQUALIFY`, bounded `HOLD/CONTAIN`, `ESCALATE` or `NO COMMITMENT`.
4. The result is written back as qualified context with owner, authority, expiry and residual.
5. Existing authorised applications decide or actuate; EA does not replace their legal or operational authority.
6. Changes in evidence, capacity or response margin reopen only the affected gate and scope.

FIWARE supplies much of the integration, context, history and notification substrate. The implementer must still engineer the decision ontology, dependency model, regime indicators, KPI service, gates, capacity limits, action library and evaluation oracle. This is the candidate Ecosystem Awareness component for this architecture.

## 11. Pointwise non-inferiority and the Type 0 boundary

T3 pointwise non-inferiority is not implied by a successful NGSI-LD query, a recent `observedAt` value or a valid actuator command. For each covered admissible state, the city must define the stakeholders, utility, null action and authorised alternatives before claiming that a non-neutral posture is no worse than the null posture.

Where the regime leaves the covered state set or the evidence is insufficient, the result remains Type 0. The appropriate output is explicit `UNKNOWN` plus an authorised bounded posture. FIWARE can carry and distribute that result; neither the broker nor EA turns it into perfect knowledge.

## 12. Balanced conclusion

The result is not “FIWARE is inadequate.” FIWARE directly addresses several difficult smart-city problems: shared context, interoperability, distributed sources, temporal information, notifications and common models. A top implementation can prevent many ordinary causes of the 00F outcome and can materially delay, reduce or contain a developing divergence.

The narrower finding is that technical health, semantic interoperability and recent context do not alone prove that the represented evidence still supports the same shared decision. Under a gradual or previously unknown regime change, an excellent implementation may detect the pivot only after local A/B/NORMAL/HOLD decisions have started consuming the common response margin. The additional EA component continuously tests that validity and makes the 00F quality-gate dispositions executable under finite time and human capacity.

## 13. Official technology sources reviewed

The FIWARE evidence needs two different version pins: the **NGSI-LD standard** and the **Orion-LD implementation** must not be treated as the same thing.

| Ref | Authoritative source | Publication / release basis used |
|---|---|---|
| **F1** | FIWARE Catalogue / Core Context Management positioning | Living FIWARE site; re-checked **24 Sep 2026**. |
| **F2** | FIWARE Smart Cities positioning | Living FIWARE site; re-checked **24 Sep 2026**. |
| **F3** | FIWARE Smart Data Models | Living FIWARE site; re-checked **24 Sep 2026**. |
| **F4** | FIWARE Orion-LD repository/releases | **Orion-LD 1.12.0, released 28 Jan 2026**. Repository states near compliance with **NGSI-LD API v1.6.1 plus selected newer features**, not blanket conformance to every later NGSI-LD feature. |
| **F5** | FIWARE NGSI-LD subscriptions tutorial | Living tutorial; re-checked **24 Sep 2026**. |
| **F6** | FIWARE NGSI-LD context-source/federation tutorial | Living tutorial; re-checked **24 Sep 2026**. |
| **F7** | ETSI GS CIM 009 — NGSI-LD API | **V1.9.1 (2025-07)**, ETSI Group Specification. This is the standard reference, not an assertion that Orion-LD 1.12.0 implements every 1.9.1 feature. |

**URLs**

- **[F1]** https://fiware.org/catalogue/
- **[F2]** https://fiware.org/about-us/smart-cities/
- **[F3]** https://fiware.org/smart-data-models/
- **[F4]** https://github.com/FIWARE/context.Orion-LD
- **[F5]** https://ngsi-ld-tutorials.readthedocs.io/en/latest/subscriptions.html
- **[F6]** https://ngsi-ld-tutorials.readthedocs.io/en/latest/context-providers.html
- **[F7]** https://www.etsi.org/deliver/etsi_gs/CIM/001_099/009/01.09.01_60/gs_CIM009v010901p.pdf

**Conformance boundary:** this profile uses ETSI V1.9.1 as the current standards reference while pinning the examined Orion-LD implementation to **1.12.0** and to its own documented conformance statement. It therefore does **not** infer that an ETSI V1.9.1 capability exists in Orion-LD unless the Orion-LD source or the configured deployment establishes it.

**Source boundary:** capabilities and inferences are bounded to this evidence cut-off (**24 September 2026**). FIWARE is modular, and Context Broker choice, feature coverage, integrations, deployment topology and operating controls vary. A real assessment must verify the selected broker release, API conformance, adapters, data models, source registrations, security, persistence, analytics, authority and observed outcomes.

## Editorial continuity note — source and scenario snapshot

This profile is a **17 September 2026 source-reviewed design analysis of FIWARE NGSI-LD / Orion-LD against 00F**. It examines one plausible smart-city context/interoperability architecture under the declared Mobility Divergence fixture.

Later FIWARE capabilities, other urban architectures, DAOS extensions, 00G, ACC, signalling/choreography, the agentic gradient or MSCA Operation/Repositioning are not silently included. A refreshed or different deployment analysis requires an explicit successor/profile.
