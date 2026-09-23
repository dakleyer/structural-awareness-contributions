# Minimum Sufficient Control / MSCA — canonical corpus entry

> **Status:** controlled MSCA corpus router and canonical entry point. This README defines the reading order and status of the MSCA line. It is not itself the complete MSCA architecture specification.

Minimum Sufficient Control asks which **authorized configuration** of coordination, interventions and enabling means can keep owner-declared outcomes inside an acceptable Objective Envelope under stated operating assumptions — and which supported alternative has the lowest justified burden. It is a conditional, multi-objective sufficiency problem, not one fixed stack or proof of a global optimum. Detection and epistemic qualification matter, but neither automatically grants an intervention permit.

The current common representation is **S/E/C/P/M**:

- **S — Objective Envelope:** owner-declared outcomes, acceptable ranges and non-compensable constraints.
- **E — Operating assumptions / environment:** the conditions under which a sufficiency claim is evaluated.
- **C — Coordination scope:** actors, flows and coverage that can be observed, coordinated, directly controlled or legitimately influenced.
- **P — Intervention mechanisms:** feasible actions available under stated preconditions, authority and timing.
- **M — Enabling means:** observation, communication, interoperability, computation/processing where relevant, actuation and effect-measurement capabilities.

An S/E/C/P/M **representation** may exist before sufficiency can be assessed and may be partial, UNKNOWN or unpopulated. Such a representation supports discovery, comparison and progressive qualification; it is not a supported minimum until the applicable Objective Envelope, assumptions, evidence and authorization justify that status.

Assessment state is separate from representation. Current working semantics distinguish **UNASSESSED**, **SUPPORTED**, **FAILED** and **UNRESOLVED**. A supported configuration is always scoped to its declared S/E conditions, evidence, authority, version and validity boundary; it is not proof of a universal or global minimum.

## Canonical MSCA document set

The corpus is consolidated around three canonical documents. Existing artefacts are linked; pending documents remain deliberately unlinked so that this README never routes to a non-existent file.

1. [**Canonical MSCA Architecture**](./00_CANONICAL_MSCA_ARCHITECTURE.md) — **CURRENT, v0.1 (23 September 2026).**  
   Authoritative generic architecture for the S/E/C/P/M kernel, representation versus sufficiency assessment, authority/evidence boundaries, multi-optima and burden, canonical invariants, downward/upward/horizontal/**normative-contractual** extensibility, and the qualified MSCA position / mechanical alignment with a Regime Awareness delta (A_RA direction, B_RA confidence/intensity, C_RA capability frontier, D_RA residual). It defines ACC coupling as a normative MSCA extension after compatibility/applicability qualification while preserving ACC's separate semantic ownership. Smart-city, DAOS and other domain material remain examples, profiles or provenance rather than definitions of the generic architecture.

2. **Canonical MSCA Operation — PENDING.**  
   This will define how an MSCA instance is operated and changed over time: declaration, representation, qualification, assessment, comparison, selection, authorization, execution, effect measurement, invalidation and requalification. Existing 01B/01D material provides part of this lineage but does not yet constitute the canonical operating specification.

3. **MSCA Control Positioning — PENDING.**  
   This will define how a participant represents its current control-sufficiency position relative to the supported configuration region, alternative configurations, control gaps, transition possibilities, burden, switching cost, authority constraints and response horizon. It is distinct from Ecosystem Awareness epistemic positioning.

### Canonical extension profiles

- [**ACC Lineage, Identity & Authority Binding Profile**](./01_ACC_LINEAGE_IDENTITY_AUTHORITY_BINDING_PROFILE.md) — **CURRENT, v0.1 (23 September 2026).** Defines the minimum ACC root/lineage, subject binding, issuer/approval authority, validity/status, mutation envelope, successor continuity and loading boundary needed to use ACC as a normative MSCA extension. It is a canonical extension profile, **not** another MSCA kernel document and not a universal IAM protocol.

The Architecture document is now the canonical semantic reference. Source papers, interface annexes and cases below remain authoritative only for the portions and provenance they actually own.

## Canonical and source reading route

Read the corpus in this order:

1. [Canonical MSCA Architecture](./00_CANONICAL_MSCA_ARCHITECTURE.md): current generic kernel, invariants and extension contract. **Status: canonical public working architecture.**
2. [Architectural and standards working context](./ARCHITECTURE_AND_STANDARDS_CONTEXT.md): original working note for the Objective Envelope, coordination/mechanism/means/response dimensions, research questions and programme boundaries. **Status: working context / lineage; not the final canonical architecture.**
3. [FG-AI4SSC input FGAI4SSC-I-097](../../submissions/itu-fg-ai4ssc/FGAI4SSC-I-097/README.md): controlled submitted PDF/DOCX and receipt status. **Status: public standards provenance.** Posting records an input, not adoption.
4. [Minimum Sufficient Control Architecture working paper](https://tegrity.ai/minimum-sufficient-control-architecture-for-ai-enabled-urban-systems/): current working architecture developed through the AI-enabled urban-systems / smart-city context, including illustrative component handoffs and staged assessment. **Status: source architecture and domain-oriented working paper; not the generic canonical MSCA specification.** Additional analysis must not be retroactively attributed to the submitted input.
5. [EA research lineage article II — multi-optima](../../research/ecosystem-awareness/baseline/ARTICLE_02_MINIMUM_CONTROL_ARCHITECTURE_MULTI_OPTIMA.md): predecessor exploration of feasible sufficiency regions, plural local/Pareto alternatives, response capability and resource trade-offs. **Status: research lineage.** Its earlier notation is not the canonical S/E/C/P/M schema.
6. [EA ↔ MSCA interface annex 01B v0.2](../../research/ecosystem-awareness/baseline/01B_EA_MSCA_INTERFACE_ANNEX_v0.2.md): current candidate boundary covering S/E/C/P/M representation versus assessment, partial/UNASSESSED state, qualified signalling/compatibility inputs, ACC and authority separation, extensibility and targeted requalification. **Status: candidate interface annex; not the Canonical MSCA Architecture itself.**
7. [Joint operation annex 01D](../../research/ecosystem-awareness/baseline/01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md): same-operation binding across EA, MSCA and Regime Awareness, including scope/version/time compatibility, permit precedence, cost ownership and race tests. **Status: candidate composition profile.**

## Extensibility and domain profiles

The generic MSCA architecture is intended to remain stable while domain-specific and normative representations extend it.

The [Canonical MSCA Architecture](./00_CANONICAL_MSCA_ARCHITECTURE.md) defines four extension directions:

- **downward extensibility / compatibility:** a smaller or legacy implementation may expose only the subset of S/E/C/P/M it can represent, while absent material remains UNKNOWN or UNPOPULATED rather than being invented;
- **upward extensibility:** richer implementations may refine S/E/C/P/M into nested objectives, capabilities, controls, evidence, constraints or domain-specific substructures without redefining the canonical meanings;
- **horizontal extensibility:** the domain may change — urban systems, mobility, manufacturing, cloud, healthcare, finance or another bounded system — while the meanings of S/E/C/P/M remain invariant;
- **normative / contractual extensibility:** richer governance objects such as ACC may be compatibility-checked and loaded as normative extension profiles that constrain S/E/C/P/M and reference external authority objects without becoming MSCA subsets.

A proposed profile is compatible only if it can add structure without redefining the canonical MSCA semantics. If a domain requires different core meanings, that is a boundary of the current architecture rather than evidence that the existing schema is universal.

### Existing examples and source cases

- The [Minimum Sufficient Control Architecture working paper](https://tegrity.ai/minimum-sufficient-control-architecture-for-ai-enabled-urban-systems/) remains the principal current **urban / smart-city source case**.
- The [extensible DAOS case](../../submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/README.md) provides a separate model case with explicit upward, downward and horizontal extension logic. **Status: adjacent extensibility example / fixture; not an MSCA deployment result and not the definition of MSCA.**
- The DAOS extension logic may inform the generic MSCA extensibility specification, but its authority/delegation semantics remain owned by that case and must not be silently imported as MSCA core semantics.

## Interfaces and neighbouring corpora

MSCA owns **control sufficiency**, not epistemic truth, regime detection, participation legitimacy or authority creation.

- [Ecosystem Positioning — Objective-Conditioned Agentic Gradient Law](../../architectural-contributions/ecosystem-positioning/01_OBJECTIVE_CONDITIONED_AGENTIC_GRADIENT_LAW.md): cross-cutting law that projects qualified ecosystem change onto the participant's MSCA and ranks repositioning by objective-conditioned risk reduction.
- [Ecosystem Awareness corpus](../../research/ecosystem-awareness/baseline/README.md): decision-scoped epistemic qualification and requalification.
- [Regime Awareness / Minimalistic EWS corpus](../../research/regime-awareness/minimalistic-early-warning-systems/README.md): observable-regime evidence, regime departure and bounded response-safety questions.
- [EA ↔ MSCA interface annex 01B v0.2](../../research/ecosystem-awareness/baseline/01B_EA_MSCA_INTERFACE_ANNEX_v0.2.md): current candidate EA/MSCA boundary; v0.1 remains preserved in the EA corpus for provenance.
- [Joint EA/MSCA/RA operation annex 01D](../../research/ecosystem-awareness/baseline/01D_EA_MSCA_RA_OPERATION_COMPOSITION_PROFILE_v0.1.md): candidate same-operation composition.
- [Agentic Citizenship Contract 01I](../../research/ecosystem-awareness/baseline/01I_AGENTIC_CITIZENSHIP_CONTRACT_HUMAN_GOVERNED_PARTICIPATION_PROFILE_v0.1.md): separately owned participation/governance semantics that couple to MSCA through the canonical normative-extension mechanism; ACC is not an MSCA subset.
- [ACC Lineage, Identity & Authority Binding Profile](./01_ACC_LINEAGE_IDENTITY_AUTHORITY_BINDING_PROFILE.md): canonical extension profile for lineage/root, identity binding, issuer/approval authority, mutation limits, validity/status and successor continuity.
- [Ecosystem Signalling 01J](../../research/ecosystem-awareness/baseline/01J_ECOSYSTEM_SIGNALLING_SELECTIVE_DISCLOSURE_AND_CHOREOGRAPHED_REPOSITIONING_v0.1.md): bounded qualified signalling and compatibility mapping. **Status: working signalling extension; its architectural boundary with MSCA is defined in the Canonical MSCA Architecture, while runtime operation remains pending.**

The intended boundary is:

> **EA qualifies what can responsibly be relied on; Regime Awareness qualifies whether the operating frame remains valid; ACC/governance constrains admissible participation; legitimate authority grants or withholds permission; MSCA determines whether an authorized control configuration is sufficient under the current S/E frame.**

No layer substitutes for another.

## Canonicalization status

| Area | Current status |
|---|---|
| S/E/C/P/M common representation | **Established working semantics across current sources** |
| Partial / UNKNOWN / unpopulated representation | **Defined in current MSCA router and 01B** |
| UNASSESSED / SUPPORTED / FAILED / UNRESOLVED assessment distinction | **Defined in current working corpus** |
| Multi-optima / feasible sufficiency region / burden | **Developed in research lineage and working architecture** |
| EA ↔ MSCA interface | **Candidate, documented in 01B** |
| EA / MSCA / RA same-operation composition | **Candidate, documented in 01D** |
| Generic upward/downward/horizontal/normative extensibility rules | **DEFINED in Canonical MSCA Architecture v0.1** |
| Generic MSCA architecture specification | **CURRENT — [Canonical MSCA Architecture v0.1](./00_CANONICAL_MSCA_ARCHITECTURE.md)** |
| Qualified MSCA A/B/C/D position and RA delta alignment | **DEFINED architecturally** |
| Objective-conditioned agentic gradient | **DEFINED in Ecosystem Positioning canonical working law; Control Positioning/transition lifecycle still pending** |
| Canonical MSCA operating specification | **PENDING** |
| MSCA Control Positioning specification | **PENDING** |
| ACC normative-extension coupling / Ecosystem Signalling compatibility boundary | **ARCHITECTURALLY DEFINED; runtime operation still pending** |
| ACC lineage / identity / authority / mutation binding | **DEFINED in canonical extension profile v0.1** |
| Completed comparative validation / production certification | **NOT ESTABLISHED** |

## Maintenance rule

This README is the controlled entry point for the MSCA corpus. Whenever an MSCA document is created, renamed, changes canonical status, changes semantic responsibility, or materially changes the MSCA architecture/operation/interface model, **this README must be reviewed and updated immediately afterward** so that no canonical or materially relevant MSCA artefact remains outside the routed reading structure.

Historical submissions and provenance records should remain stable. New architecture should be added through the canonical MSCA documents and explicit profiles/interfaces rather than by retroactively rewriting the meaning of earlier public submissions.

**Claim status:** standards-oriented research and a posted focus-group input; no adopted ITU position, universal minimum, completed comparative validation or production certification.
