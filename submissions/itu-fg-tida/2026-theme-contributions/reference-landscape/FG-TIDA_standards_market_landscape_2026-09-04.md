# FG-TIDA Standards & Market Landscape
## Competitive whitespace for systemic trust, regime awareness, human response capacity and containment

**Status:** Canonical internal reference baseline - 4 September 2026  
**Purpose:** Durable landscape reference for the FG-TIDA / Theme #16 cross-theme work. Preserve as a baseline; future updates should be versioned rather than silently replacing this snapshot.  
**Audience:** Iván Abril Palma / Codex working context. Not an adopted FG-TIDA contribution or formal ITU position.

---

## Executive conclusion

The relevant market is **not empty**. In 2026 there is intense work on agent identity, authorization, runtime control, observability, human oversight, risk management and enterprise agent control planes. However, the work is structurally fragmented.

The strongest remaining whitespace is **not another protocol, another agent identity mechanism, another vendor control plane, another generic risk framework, or another composite trust score**. It is a **vendor-neutral, cross-domain semantic layer** that allows heterogeneous agentic systems to determine and communicate:

1. whether effective human response capacity is still available;
2. whether the operating/control frame remains valid or a potential critical bifurcation is emerging;
3. what residual indeterminacy means in the current operational context - i.e. when uncertainty becomes operational risk;
4. what containment, restriction, transition or revalidation posture is justified; and
5. what minimum information must be handed off so independent actors can coordinate without assuming a single orchestrator or prescribing the underlying detector, risk method, enforcement mechanism or transport protocol.

This whitespace is directly aligned with FG-TIDA's own ToR, which asks for dynamic trust lifecycle management, human oversight integration, trust control-plane architecture, behavioural trust signals and - explicitly - exploration of **additional conceptual layers beyond protocol-level interactions** [S1].

The market evidence supports the need. NIST's 2026 post-deployment monitoring study describes the field as vast and fragmented, identifies lack of trusted standards, fragmented logging, an immature information-sharing ecosystem and difficulty scaling human monitoring alongside rapid AI rollouts [S2]. At the same time, Microsoft and IBM are already commercializing enterprise **agent control planes** [S13-S16], OpenID provides continuous shared-signal transport semantics [S9], ISO is standardizing controllability and human oversight [S4-S5], and IETF experimentation is already reaching human escalation protocols [S11]. The missing piece is the **common systemic semantics that allow these layers to compose**.

**Bottom line:** FG-TIDA is entering a crowded ecosystem at the right abstraction level. The opportunity is strongest if the work remains at the reference-architecture / semantic-interface layer and deliberately avoids competing with protocol, transport, product-control-plane and generic risk-management standards.

---

## 1. Method and scope

This landscape compares two bodies of evidence as of 4 September 2026:

- **FG-TIDA public GitHub work**, especially Themes #1, #5, #6, #7, #13, #16, #18, #19, #20 and #21, including the emerging cross-theme boundaries [G1-G16].
- **External standards and market activity**, prioritizing official ITU, NIST, ISO/IEC, OpenID, IETF, IEEE and OWASP sources, plus leading enterprise control-plane and observability products [S1-S19].

The central question is not whether adjacent work exists. It clearly does. The question is narrower:

> **Is there already a mature, dominant standard or product-neutral specification covering the same compositional layer that FG-TIDA is now converging on?**

The answer from this review is **no**. There are strong partial overlaps and at least one close protocol-level experiment, but no dominant specification currently closes the full gap.

---

## 2. What FG-TIDA is actually building in GitHub

### 2.1 Per-action / per-record foundations

The current discussion has already separated several responsibilities that are often collapsed in ordinary AI-governance frameworks:

- **Theme #5 - authority provenance:** where authority originates, standing, scope, composition, revocation and act-time applicability [G12].
- **Theme #6 - runtime evaluation:** evaluation of an action against an intent/policy reference, with a five-state vocabulary including `INDETERMINATE`, carried with scope and attribution [G11].
- **Theme #7 - verifier/appraisal semantics:** whether a record is entitled to carry a state at all; rejection classes and frozen negative vectors [G14].
- **Theme #1 - record/accountability:** what can be reconstructed later and what properties a carried claim needs [G13].

This forms an emerging local chain:

**authority/reference -> action evaluation -> evidence appraisal -> attributable record**

The important limitation is already explicit in the GitHub work: a locally sound determination does not necessarily establish the state of the system as a whole.

### 2.2 From local indeterminacy to systemic condition

The cross-theme discussion around #6 and #16 makes a sharp distinction between an **action-level `INDETERMINATE` result** and a **system-level potential critical bifurcation** [G3-G5]. A critical bifurcation is not merely an anomalous sample. It is a condition in which assumptions supporting normal controls, thresholds, recovery paths or oversight structures may no longer reliably contain future system trajectories [G1].

This matters because multiple local reviewers or subsystems may each be correct within their partial frames while the global operating frame is already failing. Theme #16 therefore treats design-boundary qualification as a condition for deciding whether normal oversight remains meaningful [G1-G2].

### 2.3 Human oversight is being reframed as capacity, not presence

The #16 synthesis explicitly rejects a simplistic "human in the loop" interpretation. Human oversight capacity includes availability of appropriately qualified authority, information quality, system-level visibility, review and coordination time, workload/backlog/latency, case criticality and the remaining response window [G2].

This is a material distinction:

> **A human may exist, may even be formally authorized, and still be operationally incapable of changing the outcome in time.**

The work therefore distinguishes **detection sufficiency** from **intervention sufficiency** [G6]. Detection of an anomaly or threat does not prove that sufficient authority, evidence, response time, containment reach or human capacity exists to act effectively.

### 2.4 External evaluation and residual indeterminacy

Theme #18 adds a different dimension: the declared operating regime/operator may not be uniquely identifiable from observed behaviour. The emerging discussion separates:

1. search for justified determination;
2. characterization of residual indeterminacy; and
3. contextual evaluation of what that residual indeterminacy means for a real production process [G9].

The key boundary is:

**epistemic determination != operational determination**

An external evaluator may establish what the evidence supports and what remains unresolved. It should not automatically decide whether the system should continue, restrict, hold or stop.

### 2.5 Population-scale reading

Theme #21 then adds a further axis: some claims that are undecidable in one record may become falsifiable across a population of records. It focuses on rates, evaluator diversity, comparability and what a population can justify concluding [G10].

Critically, #21 distinguishes its reader from #16's reader:

- #21 asks **what can be known?**
- #16 asks **what should be done?**

A population-level rate or finding may therefore become an input to an authorized operational decision, without #21 itself claiming decision authority.

### 2.6 Distributed signal exchange and containment

Theme #13 addresses the ecosystem layer. The design discussion is moving toward incident-signal exchange, corroboration, blast-radius representation, response windows, graduated containment and federated testbeds [G6-G8]. The critical architectural question is how heterogeneous participants coordinate an effective response **without a common central controller**.

Ward's signal-lifecycle framing - birth, distribution, amendment/corroboration, containment and resolution - is especially relevant because it turns local observations into a distributed process while preserving local decision authority [G8].

### 2.7 The emerging stack

The public GitHub work is therefore converging toward a structure approximately like this:

**#5 Authority / reference**  
**#6 Local action determination**  
**#7 Evidence appraisal**  
**#1 Attributable record**  
↓  
**#18 External measurement / regime or operator determination**  
**#21 Population-scale reading**  
**#13 Distributed correlation / blast radius / containment**  
↓  
**#16 Systemic condition + human response capacity + contextual risk + authorized operational response**  
↓  
**#3 / governance and policy frameworks**

Theme #19 acts as a cross-cutting privacy/minimum-disclosure constraint, and Theme #20 extends identity/authority/evidence questions into embodied systems [G15-G16].

This is already more specific than a generic "trust framework". The key question is whether an external standard or product already owns this middle layer.

---

## 3. The lower layer is crowded - and FG-TIDA should not compete there

### 3.1 Identity and lifecycle governance

Microsoft Entra Agent ID already provides enterprise identity, lifecycle governance, sponsors/owners and access management for AI agents [S15]. Microsoft requires accountable human sponsors for agent identities and explicitly supports lifecycle and incident-response responsibilities.

This is strong coverage of **who the agent is, who is accountable for it and how its access lifecycle is governed**. It does not provide a vendor-neutral systemic semantics for whether human response capacity is currently adequate or whether the operating frame itself has ceased to be reliable.

### 3.2 Authorization decision interfaces

OpenID AuthZEN Authorization API 1.0 is already a Final Specification. It standardizes communication between Policy Decision Points and Policy Enforcement Points without requiring them to know each other's internals [S10]. This is a mature example of the correct architectural principle: standardize the **decision interface**, not the internal policy engine.

It is directly relevant as a design precedent, but its decision object is authorization. It does not define systemic trust-state, critical bifurcation, human-capacity degradation or containment/transition posture.

### 3.3 Runtime control hooks

OWASP's Agent Control Standard (September 2026) defines portable middleware hooks and declarative safety-policy enforcement across agent frameworks [S12]. This is explicitly runtime enforcement.

Again, this is below the target layer. FG-TIDA should be able to map a systemic posture into runtime controls, but should not reinvent those controls.

### 3.4 Shared signal transport

OpenID SSF/CAEP already demonstrates a mature pattern for continuous cross-system signaling. Transmitters send security-state changes to Receivers, which can attenuate access for humans, robotic users, devices, sessions and applications [S9].

This proves an important point: **FG-TIDA does not need to invent signal transport**. A future systemic-awareness signal could be mapped onto existing or future event frameworks. The unresolved question is the meaning of the systemic state, not how bytes travel.

---

## 4. The upper layer is also crowded - generic governance is not the whitespace

### 4.1 AI risk management

ISO/IEC 23894 already provides general guidance for integrating AI risk management into organizational processes [S6]. NIST AI RMF likewise provides a cross-sector governance/risk structure [S3, S6].

Therefore the WP should not attempt to become another risk-management framework. Its value is the **technical-operational bridge** from evidence and residual indeterminacy to the risk context in which an authorized decision is made.

### 4.2 Impact assessment

ISO/IEC 42005:2025 covers AI system impact assessment across the lifecycle [S7]. It addresses potential impacts on individuals, groups and society.

The FG-TIDA question is narrower and more runtime-oriented: **given the current system state, what does the remaining indeterminacy mean now, and what response posture is justified?**

### 4.3 Human oversight obligations

EU AI Act Article 14 requires high-risk AI systems to support effective human oversight, including monitoring, interpretation, override/reversal and safe interruption [S8]. ISO/IEC FDIS 42105 is now at final-draft stage and provides lifecycle guidance for human oversight, extending ISO/IEC TS 8200 [S5].

These are significant neighbors. They establish that human oversight is a real regulatory and standards requirement. They do not, however, appear to define an interoperable agentic-AI semantics for **current oversight capacity under distributed, time-bounded, multi-agent conditions**.

---

## 5. The middle layer is becoming commercially important - but remains proprietary and fragmented

### 5.1 Microsoft Agent 365

Microsoft explicitly markets Agent 365 as **"the control plane for agents"** [S13-S14]. It provides registry, agent maps, agent analytics, emerging risk signals, cross-platform discovery and governance actions. It is already aggregating native and partner risk signals and prioritizing them for administrators.

This validates the commercial need for fleet/system-level visibility and response. But the semantics remain part of Microsoft's management plane. A Microsoft "risk signal" is not automatically a vendor-neutral systemic trust state that IBM, an external evaluator or a sovereign regulator can interpret identically.

### 5.2 IBM Agentic Control Plane

IBM watsonx Orchestrate likewise provides an **Agentic Control Plane** for end-to-end visibility, governance, security, agent health, performance and operational control [S16].

Again, the existence of the product validates demand; it does not close the standards gap. A product control plane can consume a common semantic layer, but it is not itself that common layer.

### 5.3 LangSmith and production evaluation

LangSmith provides tracing, online evaluation, anomaly detection, alerting and production feedback loops for agent applications [S17]. It operates at run/thread/evaluator level and can detect recurring failure patterns.

This is a strong source of evidence, but it does not specify what a detected degradation means for system-wide trust, intervention capacity or authorized containment.

### 5.4 AgentMesh regime detection

Microsoft's Agent Governance Toolkit includes a specific `RegimeChangeAlert` based on KL-divergence between recent and historical action distributions [S18]. This is important because it shows that **"regime change" is already entering operational tooling**.

But it is a detector-specific definition: a statistical threshold over action distributions. FG-TIDA's critical-bifurcation concept is broader: **whether assumptions supporting the control frame are still reliable**, regardless of whether the evidence came from KL divergence, local indeterminates, human reports, population rates, external evaluation or an incident graph.

---

## 6. Closest standards competitor: IETF HEM - important but not equivalent

The closest technical overlap found in this review is Tom Sato's individual Internet-Draft, **Human Escalation Mechanism (HEM) for Agentic AI Systems** [S11]. HEM defines a normative protocol and concrete state machine for what a Governance Execution Controller does when an agent session requires human judgment. It includes escalation triggers, `HEM_PENDING`, designation chains, human decision types, containment, timeout behavior and a Human Readiness Score.

HEM is important for three reasons:

1. It independently validates the need for formal human-escalation semantics.
2. It shows that human readiness/capacity is already a live standards problem.
3. It creates a plausible future implementation mapping for part of Theme #16.

However, it does **not** close the FG-TIDA whitespace:

- it is a **protocol**, whereas the FG-TIDA opportunity is an implementation-neutral conceptual/interface layer;
- it assumes a specific Governance Execution Controller / kernel model;
- it works primarily at agent-session and designated-principal level;
- it does not provide the broader cross-domain composition of population findings, distributed incident correlation, systemic control-frame validity, contextual operational risk and heterogeneous containment/transition mechanisms;
- and it is currently an **individual Internet-Draft with no formal IETF WG standing** [S11].

Strategic implication: HEM should be monitored and mapped, not duplicated. A HEM implementation could be one producer/consumer of a higher-level FG-TIDA systemic-awareness interface.

---

## 7. White-space analysis by WP component

### 7.1 Effective human response capacity - **partially occupied, still open at system level**

Existing work:

- EU AI Act Art. 14: human monitoring, interpretation, override, interruption [S8].
- ISO/IEC 42105: human oversight guidance [S5].
- ISO/IEC TS 8200: control transfer, uncertainty and controllability [S4].
- IETF HEM: human escalation and readiness at session/principal level [S11].
- Microsoft Entra: human sponsors and lifecycle accountability [S15].

Remaining gap:

> **Is sufficient human capability actually reachable, informed, authorized and timely enough to change the outcome across a distributed agentic system?**

This is stronger than nominal human presence or formal assignment. It is an operational capacity state.

### 7.2 Operating-frame validity / critical bifurcation - **strong whitespace**

Existing work:

- monitoring/anomaly/drift tooling [S2, S17];
- specific regime detectors such as AgentMesh [S18];
- ISO controllability and state transition [S4].

Remaining gap:

> **A detector-independent semantics for when the assumptions supporting normal controls, thresholds, recovery paths and oversight arrangements can no longer be relied upon.**

This is the heart of the critical-bifurcation contribution [G1, G3-G5].

### 7.3 Residual indeterminacy -> contextual operational risk - **strong interface whitespace**

Existing work:

- ISO 23894 and NIST AI RMF manage risk [S6];
- ISO 42005 assesses impacts [S7];
- #18 is developing epistemic determination and residual indeterminacy [G9].

Remaining gap:

> **A technical interface that preserves the difference between "what remains unknown" and "what risk that uncertainty creates in this process, at this moment, given criticality, reversibility, reliance, exposure and available response capacity."**

This avoids the incorrect shortcut `INDETERMINATE = HIGH RISK`.

### 7.4 Containment, transition and revalidation posture - **market activity, no common semantics**

Existing work:

- vendor control planes can block/restrict agents [S13-S16];
- OWASP ACS exposes runtime control hooks [S12];
- HEM specifies a particular escalation/containment path [S11];
- OpenID shared signals can trigger access attenuation [S9].

Remaining gap:

> **Vendor-neutral semantics for choosing and communicating a posture such as continue, reduce interaction, restrict autonomous scope, contain, hold, safe-mode transition, broader-authority escalation, revalidate or resume.**

The WP should specify the meaning and minimum conditions for those postures, not their transport or enforcement implementation.

### 7.5 Cross-domain handoff semantics - **the strongest compositional whitespace**

This is the most defensible unique layer.

A heterogeneous system needs a common way to carry enough information for independent readers to understand a finding without sharing architecture. Candidate fields already emerging across #6/#13/#16/#21 include:

- determination / condition type;
- scope and affected domain;
- provenance / issuer / authority context;
- evidence confidence and freshness;
- residual indeterminacy;
- observation period or population (where applicable);
- available response / containment reach;
- useful response window;
- current human/automated response capacity;
- contextual criticality or risk reference;
- requested or recommended posture;
- revalidation conditions.

The external ecosystem already has transport, policy and product-control mechanisms. **What it lacks is agreement on this semantic contract.**

---

## 8. Competition heat map

| Layer / problem | Current landscape | Competition | FG-TIDA opportunity |
|---|---|---:|---|
| Agent identity / authentication | Entra Agent ID; emerging protocol work | High | Consume / map |
| Agent authorization/delegation | OAuth/IETF/AuthZEN | High | Consume / map |
| Runtime policy hooks | OWASP ACS; vendors | High | Consume / map |
| Shared signal transport | OpenID SSF / CAEP | Medium-high | Reuse transport pattern |
| Per-run observability/evaluation | LangSmith and many vendors | High | Treat as evidence source |
| Human oversight guidance | AI Act; ISO 42105 | Medium-high | Agentic operational specialization |
| Human escalation protocol | IETF HEM (individual draft) | Emerging | Map, do not duplicate |
| Human response capacity at system level | fragments only | Low-medium | **Strong opportunity** |
| Fleet / agent control plane | Microsoft, IBM, others | High product competition | Define vendor-neutral semantics above products |
| Distributed incident/blast radius | #13 and security work | Emerging | Cross-theme composition |
| Population epistemic reading | #21 | Very emerging | Interface to operational layer |
| Regime/operator drift | #18, research/toolkits | Emerging | Detector-independent control-frame semantics |
| Critical bifurcation of operating frame | partial analogies/detectors | Low | **Strong opportunity** |
| Indeterminacy -> contextual operational risk | generic risk frameworks only | Low at agentic interface | **Strong opportunity** |
| Cross-domain containment/transition posture | products and protocol-specific mechanisms | Low-medium | **Strong opportunity** |
| **All of the above as a composable semantic layer** | no dominant standard found | Low | **Primary whitespace** |

---

## 9. What FG-TIDA should deliberately *not* build

To preserve strategic differentiation and avoid direct competition, the work should avoid becoming:

1. **A new agent communication protocol.** Transport already has active ecosystems; FG-TIDA ToR explicitly positions itself beyond protocol-level interactions [S1].
2. **A vendor control plane.** Microsoft and IBM are already shipping those [S13-S16].
3. **A generic AI risk framework.** ISO 23894 and NIST AI RMF already occupy that space [S6].
4. **A universal trust score.** IEEE P8000.1 is already developing seven trustworthiness scores and a potential trust-rating/certification model [S19]. Composite scoring also risks hiding policy choices in weights.
5. **A single detector for regime change.** Specific detectors such as AgentMesh already exist [S18]; FG-TIDA should standardize what a finding means, not mandate the detector.
6. **A mandatory universal runtime state machine.** HEM is already exploring one prescriptive path [S11]. FG-TIDA has more leverage if it defines interoperable requirements and semantics that multiple state machines can satisfy.

---

## 10. Recommended positioning of the emerging WP

A defensible working formulation is:

> **A vendor-neutral, cross-domain systemic-awareness and response-capacity interface for agentic AI trust systems.** It defines how heterogeneous subsystems express and consume evidence that effective human response capacity, systemic determinability or operating assumptions have degraded; how residual indeterminacy is related to the current operational context; and how containment, transition or revalidation posture can be communicated without prescribing the underlying detector, risk method, control mechanism or transport protocol.

This formulation has five advantages:

- it aligns directly with FG-TIDA A.2.1/A.2.2/A.2.4/A.2.7/A.2.8 [S1];
- it composes rather than competes with #6, #13, #18 and #21;
- it can map to OpenID SSF/CAEP, AuthZEN, HEM, ACS and vendor control planes rather than replacing them;
- it is stable against technological churn because it specifies semantics and invariants rather than current framework mechanics;
- and it is legible to regulators, operators and researchers because it answers simple system questions: **Can we still trust the frame? Can a human still act? What does the uncertainty mean here? What posture is justified now?**

---

## 11. Why the timing is unusually favorable

Three independent signals align:

1. **Standards bodies are moving now.** NIST launched an AI Agent Standards Initiative in February 2026 [S3]. ISO human-oversight guidance is at FDIS stage [S5]. OpenID finalized Authorization API 1.0 in January 2026 [S10]. OWASP published ACS in September 2026 [S12].
2. **Products are moving from experimentation to fleet control.** Microsoft and IBM now market enterprise agent control planes [S13-S16].
3. **The monitoring layer is explicitly recognized as fragmented.** NIST AI 800-4 identifies missing trusted guidance/standards, fragmented logging, immature information sharing and the difficulty of scaling human monitoring [S2].

This combination is precisely when a reference architecture or semantic layer can become valuable: enough implementations exist to expose interoperability problems, but no dominant common semantics has yet stabilized.

---

## 12. Standardization path and durability

The likely value of FG-TIDA is not that its first draft becomes a permanent standard unchanged. Focus Groups are pre-standardization environments. The durable value is that a well-formed semantic model can later be refined, cut down, split or progressed through SG17.

The most durable outputs would be:

- common terminology and state/condition semantics;
- explicit producer/consumer interfaces across trust layers;
- minimum handoff information requirements;
- invariants (e.g. a local `INDETERMINATE` does not imply system failure; human approval does not repair contradictory evidence; detection does not prove intervention sufficiency);
- mapping profiles to existing protocols/products;
- conformance-oriented case studies and stress tests;
- and a gap analysis identifying where normative protocol work belongs elsewhere.

These artifacts can survive changes in LLMs, agent frameworks and transport protocols because they describe **control-system properties**, not implementation fashion.

---

## 13. Watchlist - areas that could close the gap later

The whitespace is real but not protected. The following should be monitored continuously:

- IETF HEM and related agent-governance drafts - especially cross-domain escalation and human readiness [S11].
- ISO/IEC 42105 after publication - assess whether it introduces stronger runtime capacity semantics than the current public abstract indicates [S5].
- OpenID Shared Signals / CAEP extensions into AI-agent state events [S9].
- Microsoft Agent 365 and IBM Agentic Control Plane - particularly whether they publish portable risk/state schemas [S13-S16].
- NIST AI Agent Standards Initiative outputs and any new profile on post-deployment agent monitoring [S2-S3].
- IEEE P8000.1 - especially if trust ratings begin to absorb operational/systemic state [S19].
- Agent governance toolkits and safety-control proposals defining generalized regime-change or trust-contagion semantics [S18].

If one of these projects begins specifying the same semantic layer, FG-TIDA should map and collaborate rather than duplicate.

---

## 14. Outreach value

This landscape also explains why the emerging WP can support high-quality research outreach. The unresolved questions are not merely vendor implementation issues; they sit at the intersection of:

- control theory and complex systems;
- resilience and safety engineering;
- human factors and supervisory control;
- AI evaluation and uncertainty;
- distributed systems and incident coordination;
- risk and decision theory;
- identity, authority and technical governance.

A future outreach note can therefore approach top researchers with a **specific open interface problem inside a public pre-standardization process**, not a generic request to review an individual's theory. The strongest outreach objects are likely to be: control-frame validity / critical bifurcation, operational human-response capacity, and the bridge from residual indeterminacy to contextual operational risk.

---

## 15. Final assessment

**Competition is high around the FG-TIDA work, but low at the exact compositional layer now emerging.**

The important distinction is:

- **Below:** protocols, identity, authorization, runtime hooks and signal transport are crowded.
- **Above:** risk management, impact assessment, governance and human-oversight obligations are crowded.
- **In the middle:** vendors are building proprietary control planes and researchers are producing specific detectors, but a common cross-domain semantics for systemic trust state, human response capacity, control-frame validity, contextual risk and containment/transition posture is not yet dominant.

That middle layer is where FG-TIDA's public GitHub discussion is increasingly converging. The strongest strategic position is therefore not to claim a universal new trust architecture, but to define a **small, composable semantic interface** that makes existing and future mechanisms interoperable.

If that boundary is preserved, the work has credible potential to become more than another reference paper: it can become the vocabulary and handoff model by which multiple identity systems, evaluators, control planes, human-oversight mechanisms and governance frameworks understand the same systemic condition.

---

## Sources - external landscape

- **[S1] ITU-T FG-TIDA Terms of Reference.** https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx
- **[S2] NIST AI 800-4 - Challenges to the Monitoring of Deployed AI Systems.** https://www.nist.gov/publications/challenges-monitoring-deployed-ai-systems-center-ai-standards-and-innovation
- **[S3] NIST AI Agent Standards Initiative.** https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative
- **[S4] ISO/IEC TS 8200:2024 - Controllability of automated AI systems.** https://www.iso.org/standard/83012.html
- **[S5] ISO/IEC FDIS 42105 - Guidance for human oversight of AI systems.** https://www.iso.org/standard/86902.html
- **[S6] ISO/IEC 23894:2023 - AI risk management.** https://www.iso.org/standard/77304.html
- **[S7] ISO/IEC 42005:2025 - AI system impact assessment.** https://www.iso.org/standard/42005
- **[S8] EU AI Act Article 14 - Human oversight.** https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14
- **[S9] OpenID Shared Signals Working Group specifications (SSF / CAEP / RISC).** https://openid.net/wg/sharedsignals/specifications/
- **[S10] OpenID AuthZEN Authorization API 1.0 Final Specification.** https://openid.net/specs/authorization-api-1_0.html
- **[S11] IETF individual Internet-Draft: Human Escalation Mechanism (HEM) for Agentic AI Systems, -05.** https://datatracker.ietf.org/doc/html/draft-sato-soos-hem-05
- **[S12] OWASP Agent Control Standard (ACS).** https://genai.owasp.org/resource/agent-control-standard-acs/
- **[S13] Microsoft Agent 365 - control plane for agents.** https://www.microsoft.com/en-us/microsoft-agent-365
- **[S14] Microsoft Agent 365 May 2026 update - registry, map, risk signals and governance.** https://techcommunity.microsoft.com/blog/agent-365-blog/what%E2%80%99s-new-in-agent-365-may-2026/4516340
- **[S15] Microsoft Entra Agent ID documentation.** https://learn.microsoft.com/en-us/entra/agent-id/
- **[S16] IBM watsonx Orchestrate Agentic Control Plane.** https://www.ibm.com/new/announcements/introducing-the-agentic-control-plane
- **[S17] LangSmith Evaluation / production monitoring.** https://docs.langchain.com/langsmith/evaluation
- **[S18] Microsoft Agent Governance Toolkit - AgentMesh Identity and Trust 1.0, regime detection.** https://microsoft.github.io/agent-governance-toolkit/specs/AGENTMESH-IDENTITY-TRUST-1.0/
- **[S19] IEEE P8000.1 - Draft Standard for a Method and Criteria to Assess AI Trustworthiness.** https://standards.ieee.org/ieee/8000.1/12593/

## Sources - FG-TIDA public GitHub

- **[G1] FG-TIDA Theme #16 - Regime-aware and capacity-aware human oversight.** https://github.com/FG-TIDA/themes/issues/16#issuecomment-5462496736
- **[G2] FG-TIDA Theme #16 - Consolidated Working Structure v1.** https://github.com/FG-TIDA/themes/issues/16#issuecomment-5479999938
- **[G3] FG-TIDA Theme #6 - critical bifurcation distinction.** https://github.com/FG-TIDA/themes/issues/6#issuecomment-5507796005
- **[G4] FG-TIDA Theme #6 - distributed recognition boundary.** https://github.com/FG-TIDA/themes/issues/6#issuecomment-5510682694
- **[G5] FG-TIDA Theme #6 - transversal questions and lightweight handoff interface proposal.** https://github.com/FG-TIDA/themes/issues/6#issuecomment-5527510165
- **[G6] FG-TIDA Theme #13 - detection sufficiency vs intervention sufficiency.** https://github.com/FG-TIDA/themes/issues/13#issuecomment-5462867033
- **[G7] FG-TIDA Theme #13 - Nelson bounded WP proposal.** https://github.com/FG-TIDA/themes/issues/13#issuecomment-5497054659
- **[G8] FG-TIDA Theme #13 - Ward signal lifecycle / testbed response.** https://github.com/FG-TIDA/themes/issues/13#issuecomment-5508513343
- **[G9] FG-TIDA Theme #18 - determination, residual indeterminacy and contextual operational risk.** https://github.com/FG-TIDA/themes/issues/18#issuecomment-5501700348
- **[G10] FG-TIDA Theme #21 - Reading evaluation at population scale.** https://github.com/FG-TIDA/themes/issues/21
- **[G11] FG-TIDA Theme #6 - Intent-based security policies and runtime verification.** https://github.com/FG-TIDA/themes/issues/6
- **[G12] FG-TIDA Theme #5 - Provenance of Authority.** https://github.com/FG-TIDA/themes/issues/5
- **[G13] FG-TIDA Theme #1 - Accountability and attribution after an agent has acted.** https://github.com/FG-TIDA/themes/issues/1
- **[G14] FG-TIDA Theme #7 - Verifier-side requirements and failure semantics.** https://github.com/FG-TIDA/themes/issues/7
- **[G15] FG-TIDA Theme #19 - Lifecycle-wide privacy protection.** https://github.com/FG-TIDA/themes/issues/19
- **[G16] FG-TIDA Theme #20 - Trust and identity binding with embodied systems.** https://github.com/FG-TIDA/themes/issues/20
