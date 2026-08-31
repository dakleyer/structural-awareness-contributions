# TIDA — Delegated Authority OS under Context Change

- **Descriptive subtitle:** A candidate shared case for testing trust, identity, delegated authority and preference fidelity across existing FG-TIDA themes
- **Version:** 0.8
- **Status:** Public pre-freeze working draft; neither the case facts nor the challenge set are frozen
- **Scope:** Requirements-level trust, identity, delegation, authority, oversight and assessment. “OS” denotes the operating system of delegated-authority decisions in this case; it does not ask FG-TIDA to design a Smart City platform or prescribe a technical architecture.

<a id="purpose"></a>
## 1. What this working case is for

This document is intended first as a **shared test surface**, not as a proposal for a new theme, a new authority model, a prescribed architecture or one universal frozen case.

Its purpose is to let existing FG-TIDA themes examine the **same stable facts** and ask whether their requirements compose when delegation, authority, policy, context change, evidence, human oversight and return to operation meet in one operational sequence. Different themes or implementations should be able to test the same case without changing its facts to make a preferred solution pass.

The mobility/logistics setting is the **concrete instantiation**, not the point of the document. The broader structural question is:

> When a human or organization delegates decisions to an agent, what must independent systems be able to establish when context changes: **who is represented, which authority applies now, which preferences and hard limits remain binding, what evidence supports the determination, and whether the action may proceed, must be restricted, requires escalation or must be held?**

The case is deliberately small and solution-neutral. It fixes only the common structure needed to make comparison meaningful: principals, roles and agents; grants and authority; relevant preferences, policies and commitments; context-change events; evidence; required determinations; interfaces; and validation questions.

A shared case gains value when it can be reused across themes or domains, but **reusability is not an admission rule for every useful case**. A deliberately narrow or sector-specific case may be valuable precisely because it exposes one difficult boundary in depth. The aim here is to mature this particular candidate toward broad shared use while leaving room for alternative and complementary cases.

<a id="prefreeze-conditions"></a>
## 2. Ideal pre-freeze conditions — 3 + 1

The following are **ideal design conditions being used to mature this candidate case for possible shared/cross-theme use**. They are **not agreed FG-TIDA requirements and not exclusion criteria for other cases**.

They should be read differently depending on the condition:

- **D1 and D2** are desirable qualities that increase the usefulness and reuse value of a shared case.
- **D3** is a mandate boundary: material presented as an FG-TIDA case should remain defensibly within the FG-TIDA Terms of Reference.
- **+1** applies whenever a case asks participants to determine legal or authority validity, standing, scope, revocation or act-time binding.

### D1 — Multi-audience intelligibility

A shared case should retain its essential meaning for the audiences expected to use it: citizens or service users; policy and public decision makers; architects and standards contributors; and implementers or developers.

At the appropriate level, readers should be able to identify:

- who acts for whom;
- what was delegated;
- what changed;
- which evidence matters; and
- why the resulting action proceeds, is limited, escalated or held.

The principle is not that every case must be equally simple for every audience. It is that a case intended as a **shared reference object** becomes more useful when its core problem does not depend on specialist knowledge available only to its authors.

### D2 — Bounded extensibility

For a case intended to be reusable across themes or domains, it is desirable to know **how far the same core concepts survive controlled changes in scale or setting without changing meaning**.

The test is bounded rather than universal:

- can the case grow by adding actors, roles, grants, constraints or commitments without redefining the core semantics;
- can it shrink to a smaller deployment while preserving the problem it is meant to expose; and
- can it move horizontally into another service domain while preserving the same structural distinctions?

Where that stops being true, the boundary should be recorded and another case used rather than forcing the present one to appear universal.

This is an **ideal quality for a reusable/shared case, not a requirement for every valuable case**. A highly specific production case may be more useful than an extensible one when the objective is to test a particular failure mode, sector or boundary.

[Annex II](03_ANNEX_II_Case_Extensibility_Upward_Downward_Horizontal_v1.2.md) develops the upward, downward and horizontal extension tests in more detail.

### D3 — FG-TIDA mandate adequacy and traceability

Relevant case facts and challenges should remain defensibly linked to the official [FG-TIDA Terms of Reference](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx) and to the interfaces of existing themes rather than creating parallel scope.

The strongest ToR anchors include terminology and definitions (3.1), the pre-standardization roadmap (3.2), use cases (3.3), assessment criteria and benchmarks (3.4), use-case and requirements analysis (4.1), architectures and interoperability interfaces (4.2), trust lifecycle management (4.3), and technical-policy and machine-readable trust metadata (4.4).

The mapping is many-to-many. A shared case gives existing themes a common test surface; it does **not** require every theme to solve the whole case or create a separate workstream.

In scope here are representation, authentication, authorization, delegation, discovery, grant lifecycle, act-time applicability, interoperable trust determination, technical-policy metadata, runtime trust decisions, privacy, escalation, oversight capacity, traceability, accountability and assessment.

Out of scope are city optimization, routes and fleets as an optimization problem, appointment scheduling, pricing and payments, negotiation mechanisms, vehicle protocols, substantive municipal policy, national digital-identity content and any prescribed credential, signature, blockchain or implementation technology.

### +1 — Declared governing regime(s) for authority determinations

Following the Theme #16 authority-interface discussion, and especially [Pam Dixon’s clarification](https://github.com/FG-TIDA/themes/issues/16#issuecomment-5481112607), any mandate whose validity, standing, scope, revocation or act-time binding is being tested should have its **governing legal regime declared as a case fact**.

The applicable regime determines what can and cannot be conferred, when standing may change and with what continuing effect. Without that fact, some authority questions do not have a determinate answer.

This does **not** mean that every useful case must be multijurisdictional. A single-regime case can be entirely valid. Where the same structural core is tested under materially different governing regimes, the more precise representation is a **controlled family of regime-specific variants**, each with its own declared legal facts, rather than one supposed universal legal answer.

This +1 condition does not create a parallel authority model. Authority origination, standing, composition, contextual applicability, revocation and act-time validity remain determinations of the relevant authority/provenance requirements layer; the case declares the facts required to exercise those requirements.

### Working 3 + 1 view

For this candidate shared case, the ideal is therefore to be:

1. **intelligible enough to be shared;**
2. **boundedly extensible enough to reveal what is invariant and where another case is preferable;**
3. **traceable enough to remain within the FG-TIDA mandate and existing theme interfaces; and**
4. **legally determinate enough that authority questions have an answer under the declared governing regime.**

These conditions are deliberately neutral among cases. The present logistics case is one working object against which they can be tested; sector-specific production cases, narrowly bounded cases or several complementary cases may be equally useful for different purposes.

### Supporting package

- [Package index and source custody](README.md)
- [Annex I — Minimal Operational Case Outline](02_ANNEX_I_Minimal_Operational_Case_Outline_v0.3.md)
- [Annex II — Why the Minimal Case Is Extensible](03_ANNEX_II_Case_Extensibility_Upward_Downward_Horizontal_v1.2.md)
- [Annex III — Challenges Exposed by the Case](04_ANNEX_III_PostFreeze_Solution_Challenges_v1.3.md)
- [Annex IV — FG-TIDA ToR Mapping and Traceability](05_ANNEX_IV_FG-TIDA_ToR_Mapping_and_Traceability_v1.0.md)
- [Annex V — Adjacent Standards and Research Relevance](06_ANNEX_V_Adjacent_Standards_and_Research_Relevance_v1.1.md)

### Provenance note

Operational lineage: **xSeil (field deployment, 2016–2017) → Car Evolution (urban-mobility formalization, 2023) → Tegrity.AI Minimal Agentic Control Architecture / Minimum Sufficient Control (2026) → this candidate case**. This lineage records where the example came from; readers do not need those projects in order to use the case, and validation at one stage does not transfer to another. The related FG-AI4SSC contribution was posted by the Secretariat as Input Document `FGAI4SSC-I-097`; that identifier records receipt/posting, not adoption or endorsement.

## 3. Candidate case — deliberately restricted core

The committed core contains only:

1. a **citizen**, acting as human principal, and the citizen’s independent personal agent;
2. a **municipal principal** and, where relevant, a bounded municipal agent;
3. one mobility or service commitment created under a citizen grant and applicable public conditions; and
4. one material change between commitment and action time that requires authority to be determined again.

For a defined period, such as a day or week, the citizen authorizes the personal agent to organize and commit a plan. The grant may define purpose, duration, applicable domains, hard limits, tradeable preferences, financial and timing limits, permitted commitment types, subdelegation, renewal, revocation and evidence requirements.

The agent may decide within a space larger than the list of actions individually approved by the citizen; otherwise useful delegation would disappear. It may not change the citizen’s preferences or enlarge its authority, and any sub-agent must inherit rather than amplify the original limits.

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

## 4. Concepts and contextual layers

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

## 5. Required determinations

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

## 6. Authority history, intervention history and uncertainty

An authority or grant record such as `G1` and a later intervention record such as `H1` are different historical objects. `G1` records origination, grantor standing, purpose, scope, delegation conditions, duration, expiry, revocation and applicability. `H1` records who intervened, under which authority, on what evidence and with what operational effect. Neither record overwrites the other.

They must nevertheless support one unambiguous current question: **what authority is operative for action `A1` now?** Separate histories must not create competing operative permissions.

If evidence is incomplete or conflicting, the output may be **INDETERMINATE**. That is a clear determination about the evidentiary state, not permission. It must trigger an appropriate bounded response: restrict the action, use a predefined escalation path or hold. The record should retain the source and degree of uncertainty and prevent unverified assumptions from propagating through subdelegations or later decisions as hallucinated authority, collective sycophancy or loss of the original preferences and limits.

Human oversight is therefore more than routing to a nominal role. A person may be formally authorized yet unavailable, overloaded, unable to understand the case in time or unable to intervene effectively. The requirements must represent who can receive an escalation, what that person may decide, the time available and whether effective capacity exists. A role without usable capacity cannot manufacture permission.

This creates a clean cross-theme interface: shared authority/provenance requirements establish what authority originated and remains applicable; a human-intervention lifecycle consumes that determination and records intervention without recreating a parallel authority model.

## 7. Provisional solution-challenge architecture

These requirements challenges preserve the current map. They are not fourteen workstreams; a first frozen sequence may exercise only a subset, and the list may be merged, split or refined before freeze.

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

## 8. Assessment and illustrative freeze path

A shared case is useful only if contributors can show how requirements behave against the same facts. A cross-cutting assessment view may therefore state, for each material transition: the **assessment claim**, **required evidence**, **assessment criterion**, **evidence status** and **decision outcome**.

This view does not create authority, replace technical verification or define a runtime state machine. The proposed Human Oversight Evidence-to-Decision Matrix (HO-EDM) is one possible assessment method for Theme #16, not mandatory case architecture; equivalent structures remain possible. What matters is a reviewable path from **facts and evidence → assessment → supported determination**.

One illustrative pre-freeze sequence for this case is:

1. test whether the case is useful to one or more existing themes;
2. review the D1 intelligibility objective for the relevant audiences;
3. use the extension envelope, where useful, to test D2 and document the boundary of reuse;
4. confirm D3 ToR and theme-interface traceability;
5. declare the governing regime for each mandate whose authority is being tested and define regime-specific variants where materially different legal facts are required;
6. select the first subset of S1–S14;
7. define the evidence available at each event in the restricted sequence;
8. test positive, negative, indeterminate and adversarial variants; and
9. freeze a numbered version only when the facts are stable enough to compare requirements consistently.

This sequence is illustrative rather than a proposed FG-TIDA governance procedure. It does not require agreement on one case before other cases can be developed. The current case can continue to mature while alternative or complementary cases are proposed.

The case is intended as a common requirements surface for existing themes. It does not claim a finished framework, universal architecture, formal validation, adoption or endorsement.

## Version history

### 0.8 — Purpose and ideal pre-freeze conditions moved to the front

- Reorganized the main document so readers first see **what the shared case is for** and the **3 + 1 ideal pre-freeze conditions** before the logistics instantiation.
- Clarified that D1 and D2 are desirable qualities for shared/reusable cases rather than exclusion criteria for every valuable case.
- Kept D3 as the FG-TIDA mandate/traceability boundary and the +1 governing-regime condition for authority determinations.
- Reduced the xSeil → Car Evolution → MACA / Minimum Sufficient Control lineage to a short **provenance note**; no substantive understanding of those projects is required to use the case.
- Preserved the deliberately restricted case, authority/intervention structure, S1–S14 challenge surface and illustrative freeze path without substantive expansion.
- Preserved v0.7 unchanged for public version continuity.

### 0.7 — Neutral pre-freeze readiness conditions and governing-regime clarification

- Reframed D1–D3 as proposed ideal pre-freeze readiness conditions for discussion, applicable equally to the current case, alternative cases or several complementary cases.
- Incorporated [Pam Dixon’s Theme #16 governing-legal-regime clarification](https://github.com/FG-TIDA/themes/issues/16#issuecomment-5481112607) as a +1 condition for authority determinations.
- Made explicit that multijurisdictionality is not mandatory: a single-regime case can be valid, while materially different legal regimes can be represented as a controlled family of regime-specific variants.
- Preserved the solution-neutral boundary and the possibility of alternative or complementary cases.

### 0.6 — Verified lineage and solution-neutral boundary

- Made the lineage explicit as xSeil (2016–2017) → Car Evolution (2023) → Tegrity.AI MACA / formal FG-AI4SSC Input `FGAI4SSC-I-097` (2026) → the current FG-TIDA candidate case.
- Distinguished the descriptive MACA label from the formal *Minimum Sufficient Control* contribution title and preserved the no-adoption/no-endorsement boundary.
- Explained why the case must be minimal and solution-neutral so participating companies and other implementers retain space to propose and compare concrete technologies.
- Reconciled the main challenge map with Annex III by including S13 and S14.

### 0.5 — Concise case with a deliberately restricted commitment

- Renamed the candidate case **TIDA — Delegated Authority OS under Context Change** and made the meaning and boundary of “OS” explicit.
- Condensed the full v0.4 content into a discussion-length case without dropping the conceptual distinctions, design gates, extension tests, challenge map, authority/intervention interface, indeterminacy rule, assessment layer or ToR boundary.
- Made explicit that broad variants are possible tests of extensibility outside the restricted case commitment, not additional committed scenarios or workstreams.
