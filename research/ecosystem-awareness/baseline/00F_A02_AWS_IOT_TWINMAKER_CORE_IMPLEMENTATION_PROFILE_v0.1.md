# Annex 00F-A02 — AWS IoT TwinMaker / IoT Core implementation profile for the smart-city mobility quality plan

| | |
|---|---|
| **ID** | 00F-A02 |
| **Type** | Product-implementation profile |
| **Status** | Additive annex · source-reviewed working profile · not a product benchmark, certification or endorsement |
| **Version · date** | v0.1 · 2026-09-17 |
| **Evidence-source refresh** | 2026-09-24 · source/date audit; technical analysis and claim boundary unchanged |
| **Owner corpus** | Ecosystem Awareness / 00F route |
| **Technology evidence re-audit** | 2026-09-24 · rolling AWS service documentation frozen by access date below |
| **Supersedes / superseded by** | — |

> **Product-implementation annex; source-reviewed working profile, 17 September 2026.** This annex applies the frozen [00F smart-city mobility case and Q0–Q5 quality plan](./00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.1.md) to an AWS architecture using AWS IoT Core, AWS IoT TwinMaker, Amazon EventBridge and implementation-defined analytics/workflows. It compares a standard implementation, an excellent implementation and the excellent implementation after a gradual or initially unrecognised regime change. It is not a product benchmark, certification, endorsement or claim that AWS technology causes the failure.

## 1. The claim in one sentence

AWS IoT Core and IoT TwinMaker provide a strong event, device-state and operational-digital-twin substrate: a top implementation can materially reduce and delay the A/B/NORMAL/HOLD divergence, but a healthy twin, valid event route and current device state do not by themselves prove that the represented evidence still supports a compatible city response after an unknown or gradual regime change.

In this annex, **Ecosystem Awareness (EA)** means an implementation tested against the canonical [challenges, sufficiently-good conditions, hypotheses and KPIs](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md). It is a proposed control profile that may be built using AWS services and application logic; it is not presented as an existing AWS product or as a substitute for AWS IoT services.

## 2. Product and safety boundary

AWS describes IoT TwinMaker as a service for building operational digital twins of physical and digital systems. It connects models to data held in different locations, organises entities, components and relationships in a knowledge graph, provides a unified query interface and supports operational visualisation.[A1]

AWS IoT Core supplies MQTT/HTTPS device connectivity and publish/subscribe messaging.[A2] IoT Rules can filter or augment device messages and route them to Lambda, queues, streams, storage, alarms, state machines and other services.[A3] Device Shadows preserve represented device state while devices or applications are disconnected, but AWS explicitly assigns consistency management to the devices and applications and states that message arrival order is not guaranteed.[A4] EventBridge can route, filter, transform and deliver events from many sources to many targets.[A5]

The boundary is material. AWS states that IoT TwinMaker is not intended for hazardous environments or critical systems whose operation may cause serious injury, death, environmental damage or property damage, and that its data should be evaluated for accuracy rather than used as a substitute for human safety monitoring.[A1]

Accordingly, this annex assesses TwinMaker as an **operational context, analysis and decision-support layer**. Certified/local collision avoidance, emergency authority, safety interlocks and physical actuation remain in the appropriate municipal, fleet and vehicle systems. EA qualifies the decision package and proposes a bounded disposition; it does not convert TwinMaker into a safety controller.

## 3. Assessed reference architecture

| Layer | Principal components | Main inbound information | Main outbound information | Responsibility in the 00F fixture |
| --- | --- | --- | --- | --- |
| **Physical and safety** | Environmental and infrastructure sensors; buses, robotaxis, emergency vehicles, traffic signals; local certified controls | Physical observations and authorised commands | Telemetry, equipment state, local braking and safe actuation | Observe and act within each equipment or authority boundary. |
| **Device and messaging** | AWS IoT Core registry, certificates/policies, MQTT broker and Device Shadows | Sensor/fleet messages, reported state and desired-state requests | MQTT topics, shadow updates/deltas and device commands | Authenticate represented devices, exchange telemetry and retain declared device state. |
| **Routing and ingestion** | IoT Rules, Lambda, queues/streams, EventBridge and storage/connectors | MQTT streams, municipal APIs and partner events | Filtered/enriched events, workflow triggers, persisted data and error routes | Move represented events into the appropriate data and application paths. |
| **Operational twin** | IoT TwinMaker workspace, entity-component knowledge graph, relationships, connectors and unified data queries | Models, metadata, current/time-series data and alarms from connected sources | Twin queries, relationships, Grafana views and operational context | Provide a composed digital representation and decision-support view. |
| **Decision and coordination** | Evacuation, fire/rescue, traffic and fleet services; dashboards; human emergency roles | Twin context, events, rules, plans, authority and capacity | Plan A, Plan B, NORMAL, HOLD, restrictions and escalation | Decide and act through existing legitimate operational systems. |
| **Proposed EA profile** | Decision/scope registry, dependency/validity graph, KPI service, Q0–Q5 gate engine and response-margin clock | Qualified evidence, residuals, candidate postures, authority and capacity | `PASS`, `REQUALIFY`, bounded `HOLD/CONTAIN`, `ESCALATE` or `NO COMMITMENT` | Test whether the shared decision remains sufficiently qualified and compatible. |

This is a custom smart-city use of a general operational-digital-twin stack. AWS documentation illustrates factories, buildings and industrial plants, not a packaged city-emergency control product.[A1]

## 4. Standard, top and EA-qualified implementations

| Deployment level | Reasonable implementation | Effect on the 00F case |
| --- | --- | --- |
| **Standard AWS implementation** | Devices publish through IoT Core; IoT Rules route data to storage and Lambda; Device Shadows expose last reported/desired state; TwinMaker models key corridor entities and dashboards; EventBridge distributes alerts to municipal and fleet applications | Improves visibility and connectivity, but different applications can still apply separate thresholds and authority rules. A, B, NORMAL and HOLD may be valid events in separate routes without a common resource-time compatibility gate. |
| **Top AWS implementation** | Per-device identity and least privilege; governed topic and event schemas; capture/event/ingestion timestamps; sequence/version handling; rule error actions; queues and replay; source ownership and health; TwinMaker relationships and custom connectors; raw/derived separation; time-series analytics; anomaly/correlation tests; finite human queues; pre-authorised fallback; tested failure injection | Strongly reduces device ambiguity, stale-state use, out-of-order effects, routing loss, unowned alerts and known cross-system conflicts. It can detect known degradation earlier and reduce incompatible-posture exposure. |
| **Top implementation with the 00F EA profile** | The preceding controls plus `σ(d_city,t)`/`W(d_city,t)`, represented and suspected dependencies, residual/`UNKNOWN`, resource-time incompatibility, Q0–Q5 KPI states, material-break tests, response margin, targeted re-entry and deterministic dispositions | Makes the 00F plan executable. Operationally healthy AWS resources and recent device/twin state cannot alone advance the shared corridor posture when the decision basis is failed or unknown. |

The top implementation is not a cosmetic improvement. It can remove many preventable failure causes. The residual question is whether its model and tests can recognise when their own assumptions no longer justify the same response.

## 5. How the standard implementation can reproduce 00F

The frozen event remains unchanged: severe rain coincides with a battery fire beside the Riverfront corridor, telemetry becomes noisy and partly dependent, and Central Bridge is the contested resource.

### 5.1 Telemetry and applications continue to work

Environmental and infrastructure sensors publish MQTT messages through IoT Core. IoT Rules route selected messages to Lambda, storage and alerts. Device Shadows retain the latest represented state for selected equipment. TwinMaker connects corridor, bridge, road, sensor and vehicle entities to their source data and displays the operational picture.

Nothing must crash for the failure to develop.

### 5.2 Four applications derive four locally understandable postures

- plume and exposure events trigger the evacuation application to propose **Plan A**;
- thermal and access events trigger fire/rescue to propose **Plan B**;
- fleets without a fresh applicable restriction continue **NORMAL**;
- buses or personal agents receiving conflicting instructions enter **HOLD**.

IoT Rules and EventBridge can route each event correctly to its configured target. Correct routing does not determine whether the resulting actions are compatible over the same bridge segment and five-minute horizon.

### 5.3 The twin is current relative to its represented sources

TwinMaker provides one interface across connected sources and a knowledge graph of modelled relationships.[A1] Device Shadows make represented state available even when a device is disconnected.[A4] In a standard implementation, applications may therefore see a coherent and available operational picture while overlooking three distinctions:

- last represented state versus currently valid physical state;
- transport freshness versus decision applicability;
- modelled relationship versus an unrepresented common dependency.

AWS notes that applications and devices remain responsible for consistency across shadows and that messages may arrive out of order.[A4] A simple implementation can handle versions correctly and still fail epistemically because the newest accepted state is no longer sufficient for the shared decision.

### 5.4 Local safety succeeds while the city mission fails

Plan A and Plan B reserve opposed uses, NORMAL vehicles continue to enter and HOLD vehicles remain in scarce space. Local vehicle controls avoid some immediate collisions. The common corridor nevertheless loses capacity, emergency access is delayed and evacuation slows.

The technology did not necessarily malfunction. The architecture distributed and visualised the states it was designed to represent without a mandatory Q2/Q3 test for their systemic compatibility and bounded response.

## 6. What an excellent implementation fixes

A strong AWS implementation materially changes this route:

1. **Device identity and access.** Certificates, IoT policies and narrowly scoped roles limit who can publish, update state or invoke actions.
2. **Event integrity.** Governed schemas, device/event/capture timestamps, sequence numbers, shadow versions and idempotent consumers reject duplicates and stale ordering.
3. **Reliable routing.** IoT Rule error actions, queues, dead-letter handling, logs, metrics and replay reduce lost or silently failed paths.[A3]
4. **Modelled context.** TwinMaker entities, components and relationships connect corridor assets, observations, source ownership and operational processes.[A1]
5. **Source separation.** Raw observations remain distinguishable from inferred hazards, recommended plans and authorised instructions.
6. **Known-dependency monitoring.** The implementation tests registered gateways, shared providers, sensor families, connector delay and expected cross-source disagreement.
7. **Known conflict control.** A service represents bridge direction, capacity, reservation, authority and expiry and detects the declared Plan-A/Plan-B collision.
8. **Operational response.** Named owners, finite reviewer queues, deadlines, segmented fallback and exercises prevent indefinite escalation and unmanaged continuation.

This architecture can reject out-of-order updates, identify disconnected equipment, distinguish desired from reported state and catch known A/B conflicts before broad actuation. It can substantially reduce the 00F risk.

## 7. Stress case: an excellent implementation under gradual regime change

### 7.1 Starting state

At `t0`, Aurora City has implemented the top controls:

- device identities, policies, topics and event schemas are governed;
- timestamps, versions, retries, failure routes and observability are tested;
- TwinMaker represents the bridge, approaches, sensors, vehicles and known source relationships;
- raw, derived and authorised states are separated;
- source-health, known-correlation and A/B conflict checks are active;
- emergency owners, finite queues, deadlines and containment routes are rehearsed;
- the implementation passed normal and known degraded-regime tests.

The system is neither out of the box nor poorly operated.

### 7.2 The hidden pivot

Several small changes accumulate before the event:

1. two environmental providers move their edge preprocessing to the same subcontracted gateway without changing the city-facing API;
2. a firmware update changes one sensor family's timestamp from measurement time to transmission time while preserving the field name and valid format;
3. humidity produces coordinated bias that remains inside each sensor's individual health limit;
4. temporary buildings alter the Riverfront wind field, but the twin's spatial and causal relationships still represent the previous geometry;
5. traffic demand and emergency workload reduce the useful human and corridor response margin below the value used in testing.

IoT Core accepts authenticated messages. IoT Rules and EventBridge deliver them. Shadow versions increase correctly. TwinMaker connectors respond, dashboards update and the knowledge graph remains internally consistent. Yet apparent freshness, diversity and model fit are now overstated.

### 7.3 Why a top implementation reduces but cannot eliminate the risk

Known-source checks, temporal analytics and the explicit A/B conflict rule can eventually expose disagreement or block the final incompatible reservation. Compared with the standard implementation, the route is slower, narrower and more observable.

The pivot may still occur too late because:

- the newly shared provider is outside the registered dependency graph;
- the timestamp is technically current but has changed semantic meaning;
- each sensor remains inside its local tolerance while their common bias changes the joint conclusion;
- the twin faithfully mirrors the modelled city, including an obsolete spatial or causal relation;
- the A/B detector activates only after both plans have been produced, when NORMAL/HOLD occupancy has already consumed part of the response margin;
- human operators cannot continuously compare every source, connector, model assumption and consumer interpretation during the five-minute horizon.

If the change is literally unobservable, neither AWS services, EA nor a human can guarantee detection. Where weak indicators exist, EA's proposed value is to test the continuing validity of the observation/response frame and change posture before operational success is mistaken for decision sufficiency.

## 8. Gate-by-gate assessment against 00F

| 00F gate and canonical route | Standard AWS route | Top implementation | Remaining gap without EA qualification |
| --- | --- | --- | --- |
| **Q0 — frame shared use**; S1/S3/S9/S14 → T2/T3/T4 → H2/H4/H6 | Twin models assets and applications, but may not bind one five-minute corridor decision, common capacity and fallback | Models resource segments, owners, roles, reservations, expiry, capacity, deadline and invariant local safety | A complete, internally consistent twin can retain an obsolete validity horizon or dependency model. |
| **Q1 — qualify the material break**; S3/S5/S10/S14 → T1/T2/T4 → H1/H2/H3/H5/H6 | Rules react to configured topics/fields; shadows expose last accepted state | Adds capture/event/ingestion times, versions, source health, temporal trends, redundancy and known dependency/correlation tests | A schema-valid event can remain epistemically stale; an unknown common dependency or timestamp-semantic change can delay U-invalidation. |
| **Q2 — compose local postures**; S5/S6/S9/S11/S14 → T2/T4 → H2/H3/H4 | Event routes deliver A, B, NORMAL and HOLD independently | Models resource-time reservations and rejects declared incompatible combinations | New interactions, indirect occupancy and actors outside the twin can escape the fixed compatibility model. |
| **Q3 — select bounded posture**; S1/S3/S4/S5/S14 → T2/T3/T4 → H1/H4/H6 | Lambda/workflows or humans apply local rules and escalation | Uses authorised workflows, expiry, segmented operation, finite queues, response deadlines and safe external fallbacks | Workflow health or human approval does not establish that the evidence basis remains sufficient; residual and response margin need decision-scoped control. |
| **Q4 — targeted requalification**; S3/S10/S12/S14 → T1/T2/T4 → H4/H5/H6 | More topics, queries, analytics and review can expand broadly | Reopens named connectors/sources, uses bounded workflows and measures operational latency | Without evidence-yield and material-dependency logic, additional telemetry and Lambda/workflow activity can consume the useful horizon without restoring the response mapping. |
| **Q5 — compose and resume**; S9/S11/S12/S14 → T1/T2/T4 → H2/H4/H5/H6 | Green device/twin health or one recovered application may restore NORMAL | Requires compatible reservations, closed incident conditions, fresh evidence and authorised resumption | Technical recovery can be mistaken for epistemic recovery unless the changed assumptions and residual survive into the resume decision. |

## 9. Two decisive matched tests

| Test | Canonical route | Matched injection | Compared implementations | Pass condition |
| --- | --- | --- | --- | --- |
| **A — semantic freshness and dependency pivot** | S3/S5/S10/S14 → **T1** → **H5**, with H1/H3 | Hold actors, messages, AWS capacity, humans and five-minute horizon constant; introduce a hidden shared gateway, timestamp-semantic change, coordinated drift and shorter applicability horizon while authentication and delivery remain healthy | Standard vs top fixed vs top plus EA | Measure material-break recall/precision, staleness, correlated-evidence error, U-invalidation, false continuation and requalification latency. The EA route must change the affected scope before the declared corridor margin is consumed. |
| **B — compatible response under finite capacity** | S3/S4/S9/S11/S14 → **T2/T4** → **H2/H4/H6** | Present the same A, B, NORMAL and HOLD events and progressively reduce human/corridor margin | Top fixed vs the same top implementation with EA resource-time compatibility, targeted re-entry and bounded fallback | Reduce incompatible-posture exposure and emergency-access delay without worse false containment, missed deadlines or total burden; preserve `UNKNOWN` where the cause remains unresolved. |

The ledger includes IoT messaging, Rules, Lambda, queues/streams, EventBridge, TwinMaker connectors/queries, storage, analytics, waiting, human review and external actuation. If the top fixed architecture matches or outperforms the EA-enabled route under the same resources and outcomes, the claimed differential is narrowed or falsified.

## 10. Can the EA component be built with this AWS stack?

**Yes, as an engineered application/control component around the AWS substrate.** A credible design could use:

- TwinMaker entities/components for `DecisionScope`, `SharedResourceSegment`, `EvidenceSource`, known `SourceDependency`, `AuthorityGrant` and `CandidatePosture`;
- external time-series and event stores for source history, validity, drift and KPI evidence;
- IoT Rules and EventBridge for material-change routing;
- Lambda or container services for dependency, validity, incompatibility and KPI calculation;
- Step Functions or an equivalent workflow engine for deterministic Q0–Q5 transitions, bounded retry and expiry;
- queues and dead-letter routes for controlled delivery and finite backpressure;
- CloudWatch logs/metrics and the case oracle for evaluation;
- an enforcement adapter that sends only an authorised disposition to the existing municipal/fleet control system.

The runtime loop is:

1. IoT Core and partner connectors acquire represented context.
2. TwinMaker and the source registry expose the declared model and relationships.
3. EA tests the active decision scope, validity, dependency, residual, posture compatibility, capacity and response margin.
4. Q0–Q5 emit `PASS`, `REQUALIFY`, bounded `HOLD/CONTAIN`, `ESCALATE` or `NO COMMITMENT`.
5. The qualified result, owner, authority, expiry and residual are persisted and published.
6. Existing authorised applications or humans decide and actuate; physical safety remains outside TwinMaker.
7. A material change reopens only the affected gate and scope.

AWS supplies the device, event, compute, workflow, model, data and observability building blocks. The implementer must still define the decision ontology, dependency/validity semantics, regime indicators, KPI thresholds, authority boundaries, action library, capacity limits and evaluation oracle. That engineered layer is the candidate EA component.

## 11. Pointwise non-inferiority and Type 0

T3 pointwise non-inferiority is not implied by an authenticated MQTT message, a current shadow, a successful rule, a complete TwinMaker query or a human dashboard approval. The city must define its stakeholders, utility, null action, covered admissible states and authorised alternatives before claiming that a non-neutral response is no worse than the null response.

Outside the covered state set, or where the evidence cannot determine a response, the runtime output remains explicit `UNKNOWN` / unresolved (`NOT_ESTABLISHED` in the Type catalogue) plus an authorised bounded posture. A `TYPE_0_CONDITION` marker may be added only when structural non-determination or the applicable declared-frame limit has an explicit basis. AWS services can carry and execute the declared workflow; neither the digital twin nor EA becomes an oracle.

## 12. Balanced conclusion

The result is not “AWS IoT is inadequate.” IoT Core, Rules, Shadows, EventBridge and TwinMaker provide capable components for secure device communication, event routing, state representation, cross-source operational models and decision-support views. A top implementation can eliminate many ordinary technical causes of the 00F outcome and can materially delay, reduce or contain the divergence.

The narrower finding is that a digital twin is only as current and sufficient as its represented sources, relationships and validity assumptions. Under a gradual or initially unknown regime change, the AWS stack may operate correctly while the evidence-to-response mapping becomes obsolete. EA is the additional engineered loop that tests this validity and makes the 00F dispositions executable under finite time, compute and human capacity, while respecting AWS's documented safety boundary for TwinMaker.

## 13. Official technology sources reviewed — dated evidence freeze

**Evidence freeze used for presentation:** 24 September 2026. AWS User Guide pages do not consistently expose a page-level last-updated date, so this profile distinguishes dated AWS publication anchors from live documentation retrieved at the evidence freeze.

| ID | Official source | Date / publication basis | Use in this profile |
|---|---|---|---|
| **A0** | [AWS IoT TwinMaker API Reference](https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/Welcome.html) | AWS document **last published 14 Sep 2026** | Current service/API publication anchor showing TwinMaker remains an active documented service at the evidence freeze. |
| **A1** | [What is AWS IoT TwinMaker?](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/what-is-twinmaker.html) | User Guide **retrieved 24 Sep 2026**; AWS document history last lists a guide change on **17 Nov 2023** | Operational digital-twin model, entities/components/relationships, connectors, knowledge graph, visualization and explicit safety boundary. |
| **A2** | [AWS IoT Core overview](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html) | Live AWS docs **retrieved 24 Sep 2026** | Device connectivity and publish/subscribe messaging substrate. |
| **A3** | [AWS IoT Rules](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html) | Live AWS docs **retrieved 24 Sep 2026** | Rule routing/actions and error/monitoring paths. |
| **A4** | [AWS IoT Device Shadows](https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html) | Live AWS docs **retrieved 24 Sep 2026** | Represented device state, versions, consistency responsibility and message-ordering caveats. |
| **A5** | [Amazon EventBridge overview](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) | Live AWS docs **retrieved 24 Sep 2026** | Event routing/filtering/transformation substrate. |
| **A6** | [AWS IoT TwinMaker User Guide document history](https://docs.aws.amazon.com/iot-twinmaker/latest/guide/doc-history.html) | History page retrieved **24 Sep 2026**; last listed change **17 Nov 2023** | Provenance for the User Guide's published change history; not evidence that every live page is unchanged since that date. |

**Service-state boundary:** this review found no AWS notice placing IoT TwinMaker itself in sunset at the evidence freeze. Do not infer that neighboring IoT services have the same lifecycle: for example, AWS separately ended support for IoT Events in May 2026. The 00F profile does not require IoT Events.

**Dating rule for presentation use:** for capability statements grounded in a live AWS guide page, cite the page plus **retrieved 24 Sep 2026**; where a dated publication anchor is required, use A0 (**API Reference last published 14 Sep 2026**) and preserve the distinction between API publication date and User Guide content history.

**Source boundary:** because these are living service docs, **24 September 2026 is the evidence-access cut-off**. The smart-city design, EA semantics and gate implementation are proposed architecture, not advertised AWS product functionality. Later AWS service changes are not silently attributed to this v0.1 profile; a later presentation refresh should either re-audit the same pages or issue a successor profile.

## Editorial continuity note — source and scenario snapshot

This profile is a **17 September 2026 source-reviewed design analysis of AWS IoT TwinMaker / IoT Core against 00F**. It is bounded to the declared IoT/event/digital-twin architecture and the Mobility Divergence fixture.

Later AWS capabilities, other deployment topologies, DAOS extensions, 00G, ACC, signalling/choreography, the agentic gradient or MSCA Operation/Repositioning are not silently included. A refreshed or cross-scenario analysis requires an explicit successor/profile.
