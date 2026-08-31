# TIDA — Delegated Authority OS under Context Change

- **Descriptive subtitle:** A candidate shared case for testing trust, identity, delegated authority and preference fidelity across existing FG-TIDA themes
- **Version:** 0.6
- **Status:** Public pre-freeze working draft; neither the case facts nor the challenge set are frozen
- **Scope:** Requirements-level trust, identity, delegation, authority, oversight and assessment. “OS” denotes the operating system of delegated authority decisions in this case; it does not ask FG-TIDA to design a Smart City platform or prescribe a technical architecture.

### Provenance chain

The conceptual and operational lineage is explicit:

> **xSeil (field deployment, 2016–2017) → Car Evolution (urban-mobility formalization, 2023) → Tegrity.AI Minimal Agentic Control Architecture concept / Minimum Sufficient Control (2026) → this FG-TIDA candidate case.**

- **xSeil — 2016–2017.** [xSeil](https://jubap.net/jubap-net-xseil-whitepaper/) was a field-deployed passenger-transport and logistics operating system in the Riviera Maya, Mexico—not merely a routing algorithm. It supplied the operational experience of coordinating commitments, capacity, actors and changing conditions.
- **Car Evolution — 2023.** The operating logic was formalized in 2023 as the broader urban-mobility model **Car Evolution**, extending the analysis from one deployed logistics environment to a multi-actor mobility system.
- **Tegrity.AI MACA / Minimum Sufficient Control — 2026.** Within this review package, **Minimal Agentic Control Architecture (MACA)** is the descriptive name for the next conceptual step: identifying the minimum observation, coordination, authority and intervention structure required for an agentic system to maintain a declared objective under bounded constraints. The formal contribution submitted to the [ITU-T Focus Group on AI for Smart Sustainable Cities](https://www.itu.int/en/ITU-T/focusgroups/ai4ssc/Pages/default.aspx) retained the title *Minimum Sufficient Control as an Architectural Property of AI-enabled Urban Systems*. The Secretariat posted it as **Input Document `FGAI4SSC-I-097`**.
- **Current FG-TIDA candidate case — 2026.** This document isolates one narrower problem from that lineage: whether delegated authority remains valid and actionable when context changes.

“MACA” is therefore a **descriptive lineage label used in this package**, not an ITU-defined term. `FGAI4SSC-I-097` is the formal input identifier; it does not represent adoption, endorsement, validation or inclusion in an ITU-T deliverable. Likewise, the current adaptation is a candidate shared case for collaborative FG-TIDA discussion, not an adopted deliverable or product proposal. Operational evidence or reception at one stage does not transfer validation to a later stage.

### Why the model is deliberately minimal and solution-neutral

The model should specify only the common structure needed to make the case testable: principals, roles and agents; authority and delegation objects; relevant preferences, policies and commitments; context-change events; evidence; required determinations; interfaces; and validation questions. It should remain **minimal in commitments and neutral among implementations**.

This boundary is substantive, not merely stylistic. A common case becomes more useful when competing solutions can be tested against the same facts without the case preselecting a vendor, product, agent framework, identity protocol, authorization mechanism, model, optimizer, digital twin, data architecture or implementation stack. Concrete technologies and combinations should remain open to participating companies, research teams, open-source communities and other solution providers. Their contribution is to show how a proposed implementation satisfies, fails or refines the common requirements.

That division is consistent with the [FG-TIDA Terms of Reference](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx): the group can develop terminology, use cases, requirements, assessment criteria, reference architectures and interoperability interfaces, while agentic-AI protocols are explicitly outside its scope. The related [FG-AI4SSC Terms of Reference](https://www.itu.int/en/ITU-T/focusgroups/ai4ssc/Documents/Terms-of-Reference-FG-AI4SSC.pdf) similarly support system-level requirements, interfaces, coordination and architectural frameworks while excluding detailed AI-model design and training/testing methods. Accordingly, this case can define testable requirements and case-level stress tests without prescribing the commercial or technical solution. The focus group does not need to select an implementation stack—and this candidate case should not occupy that solution space—in order to expose the common architectural problem.

### Supporting package

- [Package index and source custody](README.md)
- [Annex I — Minimal Operational Case Outline](02_ANNEX_I_Minimal_Operational_Case_Outline_v0.3.md)
- [Annex II — Why the Minimal Case Is Extensible](03_ANNEX_II_Case_Extensibility_Upward_Downward_Horizontal_v1.2.md)
- [Annex III — Challenges Exposed by the Case](04_ANNEX_III_PostFreeze_Solution_Challenges_v1.3.md)
- [Annex IV — FG-TIDA ToR Mapping and Traceability](05_ANNEX_IV_FG-TIDA_ToR_Mapping_and_Traceability_v1.0.md)
- [Annex V — Adjacent Standards and Research Relevance](06_ANNEX_V_Adjacent_Standards_and_Research_Relevance_v1.1.md)

## 1. Question and purpose

When a human or organization delegates decisions to an agent, what must independent systems be able to establish when the context changes: **who is represented, which authority applies now, which preferences and hard limits remain binding, what evidence supports the determination, and whether the action may proceed, must be restricted, requires escalation or must be held?**

This document proposes one deliberately restricted case through which existing FG-TIDA themes can test their requirements against the same facts. The city and mobility setting makes time, constrained capacity, commitments, personal preferences, public conditions and contextual change visible together. Its broader denominator is **agentic coordination of commitments, constrained services or finite capacity across autonomous public and private actors**. It is service context, not a request for FG-TIDA to design urban optimization, pricing, vehicle control, municipal policy or a general agent protocol.

The work is **pre-freeze**. Two things remain separate:

- **Case-design gates D1–D3** determine whether the case is intelligible, boundedly extensible and properly traceable to the FG-TIDA Terms of Reference.
- **Solution challenges S1–S14** identify trust, identity, delegation, oversight and interoperability questions that existing themes may test once the relevant case facts are stable.

A technically interesting challenge list cannot compensate for a case that is unclear, unbounded or outside the mandate.

## 2. Deliberately restricted case commitment

The committed core contains only:

1. a **citizen**, acting as human principal, and the citizen’s independent personal agent;
2. a **municipal principal** and, where relevant, a bounded municipal agent;
3. one mobility or service commitment created under a citizen grant and applicable public conditions; and
4. one material change between commitment and action time that requires authority to be determined again.

For a defined period, such as a day or week, the citizen authorizes the personal agent to organize and commit a plan. The grant may define purpose, duration, applicable domains, hard limits, tradeable preferences, financial and timing limits, permitted commitment types, subdelegation, renewal, revocation and evidence requirements. The agent may decide within a space much larger than the list of actions individually approved by the citizen; otherwise useful delegation would disappear. It may not change the citizen’s preferences or enlarge its authority, and any sub-agent must inherit rather than amplify the original limits.

The citizen’s minimal preference profile contains three potentially competing dimensions:

- **punctuality** and a reliable arrival window;
- **travel autonomy**, such as travelling alone, choosing timing or retaining route flexibility; and
- **economic outcome**, including cost, compensation or a more expensive alternative.

The municipality may establish a valid condition concerning access, scarce capacity, service continuity, air quality or another public objective and may delegate bounded operational decisions. A municipal condition does not silently rewrite the citizen’s preference profile; equally, a personal preference cannot waive a valid applicable public condition. Public objectives are not authority by themselves: they must be translated into applicable policy and valid delegations.

The case distinguishes five lifecycle moments: **recommendation, negotiation, reservation, binding commitment and action**. Authority that was sufficient when a commitment was made may be expired, revoked, restricted or no longer applicable when action is due.

### Minimal event sequence

1. The citizen grants bounded authority `G1` to the personal agent and identifies hard and tradeable preferences.
2. A municipal condition `P1` is valid within a stated context and authority domain.
3. The personal agent selects or negotiates a service and creates commitment `C1` within the authority apparently applicable at that time.
4. Before execution, context `R1` changes materially: capacity collapses, disruption accumulates, an emergency condition arises, a grant changes, or relevant evidence becomes incomplete.
5. The system must reassess which authority and policy remain applicable at action time.
6. A human or technical intervention `H1` may confirm, restrict, suspend or replace what may be done, provided the intervener has the required authority and effective capacity.
7. The resulting determination for action `A1` is **proceed, proceed with limits, escalate through a predefined bounded path, hold, or INDETERMINATE**.

The correct result cannot be obtained by changing a frozen fact to suit a proposed solution. A materially different fact pattern becomes a new version or another case.

## 3. Concepts and contextual layers

The case keeps four actors or structures distinct:

- a **principal** is the human or organization in whose name or interest authority is held;
- a **role** is a bounded function within an authority domain;
- an **agent** is a human or technical actor operating under a grant or mandate; and
- an **authority domain** is the public or private context from which authority originates.

It also separates four decision concepts:

| Concept | Meaning | Authority effect |
|---|---|---|
| Preference | Desired outcome or trade-off declared by a principal | Does not itself confer authority |
| Policy | Condition applicable in a defined context | Requires valid origin and applicability |
| Grant | Authority conferred on an agent within stated bounds | Confers authority only within scope and lifecycle conditions |
| Decision | Selection or commitment made under a grant | Valid only under current grants, policies and context |

A reviewable decision record should identify whose relevant preferences and conditions were considered, their applicable strength or limit, and the source and effect of any override. This requires sufficient fidelity to represented principals, not disclosure of every internal model step.

The service environment may contain three conceptual layers. They are a narrative aid, not a prescribed stack:

| Layer | Service role | Position here |
|---|---|---|
| Orchestration and planning | Routes, timing, capacity, appointments, access and execution | Context only |
| Negotiation and agreements | Alternatives, price, incentives, contracts and commitments | Context only; authority to commit is in scope |
| Trust, identity and authority | Representation, grants, applicability, evidence and act-time determination | Direct subject |

## 4. Required determinations

For a proposed commitment or action, a conforming requirements approach should be able to determine:

1. which public and private principals are represented;
2. which grants, role mandates and conditions were validly originated;
3. whether each remains in standing at commitment and action time;
4. which policy and contextual conditions apply;
5. whether authority from different principals composes, conflicts, is non-substitutable or is incomplete;
6. whether hard limits and permitted preference trade-offs are respected;
7. which evidence and lineage support the determination; and
8. whether the action may proceed, must be limited, requires bounded escalation or must be held.

An employer, operator, provider or public-transport service may later introduce another legitimate principal, role or commitment. Its authority is not substituted by either the citizen grant or municipal policy. Routing an escalation to a role does not confer authority outside that role’s scope.

## 5. Authority history, intervention history and uncertainty

An authority or grant record such as `G1` and a later intervention record such as `H1` are different historical objects. `G1` records origination, grantor standing, purpose, scope, delegation conditions, duration, expiry, revocation and applicability. `H1` records who intervened, under which authority, on what evidence and with what operational effect. Neither record overwrites the other.

They must nevertheless support one unambiguous current question: **what authority is operative for action `A1` now?** Separate histories must not create competing operative permissions.

If evidence is incomplete or conflicting, the output may be **INDETERMINATE**. That is a clear determination about the evidentiary state, not permission. It must trigger an appropriate bounded response: restrict the action, use a predefined escalation path or hold. The record should retain the source and degree of uncertainty and prevent unverified assumptions from propagating through subdelegations or later decisions as hallucinated authority, collective sycophancy or loss of the original preferences and limits.

Human oversight is therefore more than routing to a nominal role. A person may be formally authorized yet unavailable, overloaded, unable to understand the case in time or unable to intervene effectively. The requirements must represent who can receive an escalation, what that person may decide, the time available and whether effective capacity exists. A role without usable capacity cannot manufacture permission.

This creates a clean cross-theme interface: shared authority/provenance requirements establish what authority originated and remains applicable; a human-intervention lifecycle consumes that determination and records intervention without recreating a parallel authority model.

## 6. Pre-freeze case-design gates

### D1 — Multi-audience intelligibility

The same case must retain its meaning when explained to citizens and service users; policy and public decision makers; architects and standards contributors; and implementers and developers. Each audience should be able to identify, at its appropriate level, who acts for whom, what was delegated, what changed, which evidence matters and why an action proceeds, is limited, escalated or held. A case understandable only to its authors fails.

### D2 — Bounded extensibility, outside the committed case

The broad variants below are **not part of the deliberately restricted commitment** and do not create additional workstreams. They remain visible only to test whether the same concepts can extend without changing meaning and to identify where another frozen case would be required:

- private vehicles, taxis/VTC, robotaxis, public transport and shared fleets;
- employer/employee commitments, supervisors and other organizational role chains;
- private life, hobbies, leisure, households and independently selected services;
- public or private appointments, slots, queues, reservations, buffers and constrained capacity, including administrative, healthcare, professional and personal-care services;
- finite-capacity or minimum public services;
- intermunicipal travel, supply, replenishment and external logistics;
- policy, operational, supervisory and exceptional public roles;
- citizen, employer, household, provider and operator principals; and
- independent personal, municipal, provider and sub-agents with concurrent bounded delegation chains.

These are possible extension tests, not claims of universal coverage. Pre-freeze review should establish where adding actors, roles and grants is sufficient, where core meanings break, and where a separate case is needed.

### D3 — FG-TIDA mandate adequacy and traceability

Relevant facts and challenges must remain defensibly linked to the official [FG-TIDA Terms of Reference](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx). The strongest anchors are terminology and definitions (3.1), the pre-standardization roadmap (3.2), use cases (3.3), assessment criteria and benchmarks (3.4), use-case and requirements analysis (4.1), architectures and interoperability interfaces (4.2), trust lifecycle management (4.3), and technical-policy and machine-readable trust metadata (4.4). Relevant Annex A interfaces include identity stacks, delegation artefacts, policy languages, conceptual layers, agentic trust management and lifecycle, human oversight, cross-sector interoperability, runtime trust control and behavioural trust signals.

The mapping is many-to-many. It gives existing themes a shared test surface; it does not require every theme to solve the case or create a standalone workstream.

In scope are representation, authentication, authorization, delegation, discovery, grant lifecycle, act-time applicability, interoperable trust determination, technical-policy metadata, runtime trust decisions, privacy, escalation, oversight capacity, traceability, accountability and assessment. Out of scope are city optimization, routes and fleets, appointment scheduling, pricing and payments, negotiation mechanisms, vehicle protocols, substantive municipal policy, national digital-identity content and any prescribed credential, signature, blockchain or implementation technology.

## 7. Provisional solution-challenge architecture

These requirements challenges preserve the complete current map. They are not fourteen workstreams; a first frozen sequence may exercise only a subset, and the list may be merged, split or refined before freeze.

| ID | Challenge | Requirement tested |
|---|---|---|
| S1 | Authority provenance and current applicability | Origin, scope, standing, composition, expiry, revocation and validity at commitment and action time |
| S2 | Preference fidelity and reviewable decision basis | Continued representation of principals’ preferences, trade-offs and hard limits |
| S3 | Regime and context qualification | Detection that ordinary assumptions no longer apply and authority must be reassessed |
| S4 | Human oversight capacity | Real availability, authority, attention, time and intervention reach rather than a nominal role |
| S5 | Operational indeterminacy and containment | Explicit uncertainty, bounded effects and prevention of propagation as authority |
| S6 | Interoperable, privacy-preserving trust determination | Sufficient real-time verification across independent systems without unnecessary disclosure |
| S7 | Identity and representation link | Distinction among principal, organization or role, acting agent and relevant agent instance or substitute |
| S8 | Bounded subdelegation and non-amplification | Preservation of purpose, scope, time, limits, preferences and revocation through sub-grants |
| S9 | Multi-principal composition, non-substitution and conflict | Concurrent citizen, municipal, employer, provider or operator authority without assuming a universal hierarchy |
| S10 | Commitment state and material change | Distinction among recommendation, negotiation, reservation, commitment and execution, with revalidation triggers |
| S11 | Policy integrity across domains and jurisdictions | Preservation of policy origin, version, scope, conditions and interpretation |
| S12 | Accountability, challenge and repair | Reconstruction, contestability and future correction without rewriting history |
| S13 | Authority history versus intervention history | Distinct historical records that still yield one unambiguous current operative determination |
| S14 | Evidence-to-decision assessment | Explicit claims, required evidence, sufficiency status and the decisions that the evidence can support |

## 8. Assessment and collaborative freeze path

A shared case is useful only if contributors can show how requirements behave against the same facts. A cross-cutting assessment view may therefore state, for each material transition: the **assessment claim**, **required evidence**, **assessment criterion**, **evidence status** and **decision outcome**.

This view does not create authority, replace technical verification or define a runtime state machine. The proposed Human Oversight Evidence-to-Decision Matrix (HO-EDM) is one possible assessment method for Theme #16, not mandatory case architecture; equivalent structures remain possible. What matters is a reviewable path from **facts and evidence → assessment → supported determination**.

The collaborative pre-freeze sequence is:

1. test whether a shared case is useful to existing themes;
2. test D1 across the four audiences;
3. use the extension envelope only to test D2 and document its limits;
4. refine the D3 ToR and theme interfaces;
5. select the first subset of S1–S14;
6. define the evidence available at each event in the restricted sequence;
7. test positive, negative, indeterminate and adversarial variants; and
8. freeze a numbered version only when the facts are stable enough to compare requirements consistently.

The case is intended as a common requirements surface for existing themes. It does not claim a finished framework, universal architecture, formal validation, adoption or endorsement.

## Version history

### 0.6 — Verified lineage and solution-neutral boundary

- Made the lineage explicit as xSeil (2016–2017) → Car Evolution (2023) → Tegrity.AI MACA / formal FG-AI4SSC Input `FGAI4SSC-I-097` (2026) → the current FG-TIDA candidate case.
- Distinguished the descriptive MACA label from the formal *Minimum Sufficient Control* contribution title and preserved the no-adoption/no-endorsement boundary.
- Explained why the case must be minimal and solution-neutral so that participating companies and other implementers retain the space to propose and compare concrete technologies.
- Reconciled the main challenge map with Annex III by including S13 and S14.

### 0.5 — Concise case with a deliberately restricted commitment

- Renamed the candidate case **TIDA — Delegated Authority OS under Context Change** and made the meaning and boundary of “OS” explicit.
- Condensed the full v0.4 content into a discussion-length case without dropping the conceptual distinctions, design gates, extension tests, twelve solution challenges, authority/intervention interface, indeterminacy rule, assessment layer or ToR boundary.
- Made explicit that broad variants are possible tests of extensibility outside the restricted case commitment, not additional committed scenarios or workstreams.
- Preserved v0.4 and the extended rationale as internal traceability sources.
