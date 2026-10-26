> [!NOTE]
> **Revisión para personas · instrucción de Iván del 6 de octubre de 2026.** El [plan de trabajo](../../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md) exige cuatro pasadas diferentes, registradas en esta misma VNext: **fondo y lógica; evidencia y relaciones; edición y formato; legibilidad humana**. Después habrá una conciliación del corpus, con consecuencias en cada VNext afectada. El centro es comprender y cuestionar la idea; códigos y comprobaciones técnicas quedan como apoyo. La exploración mixta publicada antes se conserva, pero no se cuenta como cuatro pasadas terminadas.

### Estado del ciclo de revisión de este documento

| Pasada | Estado al adoptar el plan |
|---|---|
| Fondo y lógica | Parcial: hay observaciones exploratorias; falta su examen diferenciado completo. |
| Evidencia y relaciones entre documentos | Parcial: relaciones seleccionadas; faltan revisiones cruzadas completas. |
| Edición, estructura y formato | Pendiente como pasada propia. |
| Legibilidad y comprensión humana | Pendiente como pasada propia. |
| Conciliación final del corpus | Pendiente. |

**Cómo se continúa:** añadir cada pasada y sus respuestas en la sección de auditoría de esta VNext, explicando hallazgos y consecuencias para un lector. Conservar los registros anteriores y terminar con propuestas antes/después. Esta nota organiza el trabajo; no afirma que esas pasadas se hayan realizado ni altera el texto canónico.

---

> [!NOTE]
> **VNext · auditoría acumulativa R1 · 6 de octubre de 2026.** Se conserva íntegra la revisión anterior. Auditoría de la proyección ideal, fuentes públicas verificadas e instrucciones/propuestas al final; ningún contrato congelado o Theme se modifica ni se declara adoptado. [Procedimiento](../../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md) · [visión general](../../../../architectural-contributions/ecosystem-positioning/README_VNext.md).

# 05 Ideal Interfaces vNext Review & Delta — FG-TIDA

> **Working delta only — not a new FG-TIDA specification or adopted architecture.**  
> The frozen reference remains [**05 — FG-TIDA Ideal Cross-Theme Interface Contracts v0.4**](./05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md) ([part 2](./05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part02.md), [part 3](./05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part03.md)).  
> This file accumulates the **maximum ideal FG-TIDA projection** that follows from the current EA/Positioning corpus plus public FG-TIDA Theme/Use-Case development. It may remain partial while review is active. Nothing here changes the frozen 05 unless a later version is explicitly promoted.
>
> **Semantic refresh — 2 October 2026.** [00M v0.8](../../baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) governs A/B/C/D as **producer/process/question/scope/capability/time-relative roles**. The [04 recognition/interface-map Working Proposal](../../baseline/04_EA_ABCD_RECOGNITION_AND_INTERFACE_MAP_v0.1_WORKING_PROPOSAL.md), recorded in [04-vNext](../../baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md), is an upstream candidate implementation reading, not a frozen interface baseline. In this 05 delta, interface direction does not determine A/B/C/D, source A is not relabelled as metadata, and any use of `A` versus `A_ref` must be profile-declared.

| | |
|---|---|
| **ID** | 05-vNext Review & Delta |
| **Version · date** | v0.1-draft · cumulative ideal review refreshed 2 October 2026 |
| **Status** | Cumulative ideal-interface delta / review; incomplete by design; no frozen-contract change |
| **Frozen source** | 05 v0.4 Ideal Cross-Theme Interface Contracts |
| **Upstream control** | [00 Requirements frozen baseline](../../baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) + [Requirements vNext Review & Delta](../../baseline/00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) + [00M v0.8 semantic source](../../baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) → [04 General Interfaces v0.5 Integrated](../../baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md) + [04 General Interfaces vNext Review & Delta](../../baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) + [04 A/B/C/D Recognition & Interface Map Working Proposal](../../baseline/04_EA_ABCD_RECOGNITION_AND_INTERFACE_MAP_v0.1_WORKING_PROPOSAL.md) |
| **Downstream relation** | 05A current-state mapping must remain narrower and source-constrained; it may not inherit an ideal 05 relation merely because this delta can express it |
| **Idealisation rule** | Assume sufficient semantic owners, editors, test maintainers, independent implementations and review capacity to exercise every admitted route; do not assume FG-TIDA has already adopted, resourced or frozen them |

---

## 1. What “ideal” means in 05

05 is intentionally **not** the question answered by 05A.

- **04** asks what the programme-independent EA interface architecture needs.
- **05 Ideal** asks how that architecture could be mapped across FG-TIDA **if every relevant Theme/output were sufficiently mature, owned, interoperable and testable**.
- **05A Current-State** asks what portion of that ideal map is actually defensible from the present public FG-TIDA record.

The purpose of this delta is therefore to expose the **best coherent FG-TIDA architecture available in principle**, not the smallest currently supportable one.

An ideal relation may be included when all of the following are true:

1. it derives from an existing 04 capability/interface rather than inventing a new generic interface downstream;
2. a plausible FG-TIDA semantic owner or Theme family exists for the state;
3. the direction of ownership is explicit;
4. the relation can be exercised by at least one case, fixture or conformance vector without fabricating the producer's semantics;
5. UNKNOWN / not-established remains representable;
6. authority, policy, evidence, human decision and execution are not silently translated into one another; and
7. the ideal map remains implementation-neutral and does not require one central operator or shared internal model.

An ideal 05 profile may therefore be **richer than the current Focus Group implementation** while still being bounded by 00/04.

---

## 2. Change-control rule

05 must not be used to introduce or redefine a generic 04 interface.

The dependency order is:

**00 Requirements**  
→ **00 Requirements Delta**  
→ **04 General Interfaces**  
→ **04 General Interfaces Delta**  
→ **05 FG-TIDA Ideal**  
→ **05 Ideal Delta**  
→ **05A FG-TIDA Current-State**

If a Theme-specific case exposes a genuinely generic interface gap, the gap returns upstream to 04-vNext first.

If a 05 ideal relation cannot be supported from current public Theme semantics, that does **not** invalidate the ideal relation; it means the relation remains ideal/candidate and 05A must classify it more narrowly.

---


## 2A. 00M / 04-vNext semantic discipline carried into 05 Ideal

The 2 October upstream work changes how an ideal 05 contract should be **read**, without promoting a new 04 baseline.

### Producer-relative role rule

An ideal cross-Theme contract must first identify the source producer/process and its delivered functional result.

- **A(source)** is that source process's functional result.
- **B(source)** is the established basis, limits and characterized assessable reserve that qualify that result.
- **C(source)** is a grounded exploration frontier whose evaluation basis is not yet sufficiently established.
- **D(source)** is a potentially material effect beyond the source process's effective evaluation route in the declared frame.
- **A(EA)** is the functional result EA itself delivers to its receiving consumer: for example, a qualified assessment, insufficiency statement, requalification request or posture.

The same physical field or fact can occupy different roles for different processes. Therefore an O#/IF-S# family, a field name, or the fact that something is "input to EA" does not determine its A/B/C/D role.

### Ideal profile rule for A versus A_ref

The earlier metadata-only input proposal exposed H06 because some EA uses require the source's operative result. A future 05 ideal contract should therefore allow two bounded profiles inherited from the 04-vNext candidate direction:

- **full-result profile:** `A(source) + eligible B/C/D(source) → EA`;
- **metadata-only profile:** `A_ref + eligible B/C/D(source) → EA`.

The profile must say which route it uses. A metadata-only route must not claim to support an EA use that requires the value of A, and A must not be renamed B merely to make it admissible.

### Classification discipline

For every ideal handoff, the mapping should be able to record one of:

- **CONFIRMED A/B/C/D** under a named producer profile;
- **PROFILE-DEPENDENT** where the role changes with the source function or profile;
- **UNRESOLVED** where the evidence is insufficient to assign a role;
- **LINK / CONFIGURATION** where the item binds or governs the exchange but is not itself one of the epistemic roles.

This discipline is an architectural reading of 00M/04-vNext. It is not a claim that FG-TIDA has adopted A/B/C/D vocabulary, one common payload, or a universal EA runtime.

---

## 3. Ideal Theme #13 architecture — two peer mechanisms inside one Theme-derived scope

The public Theme #13 discussion supports a stronger architecture than the frozen 05's simple producer→EA reading.

Ward Duchamps has stated that:

- Ecosystem Awareness belongs within Theme #13;
- the systemic-capacity / handoff interface may be foundational;
- defense is the first concrete use, not the whole scope of the envelope; and
- the determinacy envelope and signal lifecycle should be defined independently so each can be tested alone and interoperate.

Nelson Trasatti has confirmed from UC #4 / testbed that the incident lifecycle remains a complete operational mechanism while EA remains independently testable.

Public anchors:

- Ward lifecycle/testbed: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5508513343
- Ward placement/independent envelope/lifecycle: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5571476256
- Iván peer-mechanism proposal: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5624367911
- Nelson testbed confirmation: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5639226397
- compact boundary table: https://github.com/FG-TIDA/themes/issues/13#issuecomment-5640186655

### Ideal 05 consequence

Theme #13-derived work should contain **two peer mechanisms**:

| Peer mechanism | Ideal responsibility |
|---|---|
| **Incident / Signal Lifecycle** | Signal birth/semantics, distribution, corroboration/contestation/amendment, operational affected-scope/blast-radius refinement, response coordination, locally authorized containment workflow and resolution. |
| **Ecosystem Awareness** | Decision-scoped systemic qualification, residual/inherited indeterminacy, source/dependency composition, capacity/horizon sufficiency, targeted requalification and system-level support assessment. |

Bidirectional relation:

**Lifecycle → EA:** incident/evidence state, source/provenance, freshness, operational affected scope/blast radius, response reach/window, unresolved qualifiers.

**EA → Lifecycle:** scoped systemic qualification, residual/UNKNOWN, dependency/capacity conditions, whether further corroboration/refinement remains decision-relevant, and targeted refinement/requalification requests.

Boundaries:

- incident resolution ≠ ecosystem requalification;
- operational blast radius ≠ epistemic dependency graph;
- signal assurance ≠ system-level determination;
- containment capability ≠ containment authority;
- neither mechanism creates authority merely by emitting a signal or assessment.

### Ideal EHD relation

The four-field #13 determinacy envelope may be treated as a versioned **Theme #13 profile** of the broader EHD abstraction, with bounded adapters preserving source-native semantics. The general EHD remains owned by 04-level architecture, not by Theme #13 or UC #4.

---

## 4. Ideal Theme #16 route — human oversight as a bounded semantic owner, not epistemic repair

The current public sequence is now sufficiently clear to define the ideal route:

**UC #6 semantic source**  
→ **Theme #16 v0.2 matrices annotate bounded interfaces**  
→ **draft bounded cross-interface / UC #4 mapping**  
→ **case + matrix semantic-owner review**  
→ **freeze version-pinned adapter / fixtures / expected outcomes**  
→ **execute traces / report in UC #4**

Public anchors:

- Nelson mapping proposal: https://github.com/FG-TIDA/themes/issues/16#issuecomment-5803023066
- Arpita review acceptance: https://github.com/FG-TIDA/themes/issues/16#issuecomment-5803653565
- Olena matrix-side acceptance: https://github.com/FG-TIDA/themes/issues/16#issuecomment-5804125734
- Lei Theme-lead approval: https://github.com/FG-TIDA/themes/issues/16#issuecomment-5809248877

### Ideal #16 → EA handoff

Where material:

1. applicable authority determination/reference received from its owner;
2. permitted intervention set;
3. human decision/result;
4. assurance in the received human-review event;
5. operational human/institutional capacity qualification;
6. external dependency/saturation condition;
7. residual/inherited indeterminacy;
8. attempted execution and externally confirmed outcome as separate states where available;
9. re-entry/revalidation condition.

### Ideal EA → #16 return

- affected decision scope;
- systemic residual/indeterminacy relevant to oversight;
- capacity/window materiality;
- specific evidence/dependency needing requalification;
- whether ordinary human escalation remains a meaningful path;
- no instruction that silently creates human authority or selects the intervention.

Human approval remains a legitimate decision input. It does not automatically expand the upstream grant, prove execution, repair contrary evidence or eliminate residual uncertainty.

---

## 5. Requirements-delta consequences carried into the ideal FG-TIDA map

05 Ideal inherits the three current Requirements clarification candidates without turning them into new universal 04 fields.

### CAND-R1 — effective-role drift

`Role_bound ≠ Role_effective`

Ideal FG-TIDA should be able to combine Theme-owned identity/representation, state/attestation, policy and action records so a relying party can distinguish:

- bound identity/role;
- effective observed function/state;
- evidence basis/time;
- current authority/applicability for the effective function.

Identity or capability continuity alone must not be treated as authority continuity.

### CAND-R2 — opportunity / admissibility / authority / execution

`opportunity ≠ admissibility ≠ authority ≠ execution`

Ideal FG-TIDA should preserve:

- technical/reachable opportunity;
- policy/participation admissibility;
- current authority/standing;
- final execution/outcome

as separately owned states.

### CAND-R3 — per-action compliance versus aggregate/composed authorization

`per-action compliance ≠ aggregate/composed authorization`

Where the governing authority boundary is cumulative, campaign-level, resource-time-based or otherwise compositional, the ideal profile should preserve enough aggregate/action-history lineage for the legitimate owner/relying party to evaluate the composed effect.

This is a **conditional Composition-Critical relation**, not a universal EHD tax.

---

## 6. Ideal temporal model — validity and response are separate clocks

The ideal architecture must preserve two independent temporal questions:

1. **semantic / qualification validity window** — how long evidence, authority, delegation, policy, configuration and assumptions remain applicable;
2. **operational response window** — how long remains to materially affect the outcome.

Theme #13's Operational Risk / Response Window / Epistemic Opportunity work makes the distinction explicit.

DBC-C02 supplies the applied-validation form:

> a result may remain technically available or syntactically valid while a material authority/evidence/context condition has become stale before use.

Ideal FG-TIDA should therefore be able to test:

- stale-but-technically-valid results;
- stale authority/delegation/policy references;
- targeted requalification of only the invalidated scope;
- useful response margin after requalification;
- expiry/no-response without conversion into permission.

[00I — Semantic TOCTOU](../../baseline/00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_FREEZE_EDITION.md) now supplies an internal EA stress scenario for stale-but-technically-valid conditions. It remains an internal architecture/test source rather than FG-TIDA-owned semantics.

---

## 7. Maximum ideal FG-TIDA capability map

The frozen 05 already mapped several Themes. The ideal vNext map can be broader while still inheriting 04 ownership boundaries.

| FG-TIDA Theme / work | Ideal 04 capability mapping | Ideal contribution to EA / cross-Theme reasoning | Boundary |
|---|---|---|---|
| **#1 Accountability / attribution** | IF-S8 | Action/execution/state records, historical attribution, reconstruction. | Record ≠ proof of every carried claim. |
| **#2 Sovereign Discovery / modularity** | O2, O6, IF-S13 | Multiple discovery surfaces, source/freshness/pathway alternatives. | Discovery ≠ trust or authority. |
| **#3 Global Trust & Accountability** | IF-S8, IF-S13 | Governance/trust-framework/jurisdiction references and accountability context. | Policy/governance guidance does not become runtime authority automatically. |
| **#4 Access Control / metamorphing agents** | IF-S1, IF-S4, IF-S12 | Identity-behaviour mismatch, policy/enforcement state, state-sensitive access control. | Identity alone ≠ current behaviour/authority. |
| **#5 Provenance of Authority** | IF-S2 | Grant origin, scope, standing, limits, revocation, composition, current applicability. | EA never originates a grant. |
| **#6 Intent / policy runtime conformance** | IF-S4 | Producer-native policy/conformance verdict plus scope/evidence/indeterminate semantics. | Verdict remains source-native. |
| **#7 Verifier-side evidence/failure semantics** | IF-S5 | Appraisal obligations, failure classes, replay/freshness/out-of-mandate evidence semantics. | Verification failure ≠ generic EA disposition. |
| **#8 Digital-ID trust management / cross-border recognition** | IF-S1, IF-S13 | Trust-framework guarantees, assurance/revocation/freshness, sovereign mapping. | No global trust hierarchy assumed. |
| **#9 fuzzy / never-crisply-authored authority** | IF-S2, IF-S5 | Explicit absence/indeterminacy of authority provenance. | Missing grant is not silently repaired. |
| **#10 Network-native governance / enforcement** | IF-S12 | Enforcement, containment, revocation, recovery, execution state. | EA does not become actuator. |
| **#11 Model-level Trust Foundations** | optional model-level profile, IF-S3, IF-S7 | Model formation/guardrail provenance and qualified model-level trust evidence where available. | Model-level trust ≠ runtime/system-level sufficiency. |
| **#12 Agent Trust Mechanics** | IF-S3, IF-S5, IF-S7 | Runtime/credential/trust-mechanics evidence and local assessment. | Local trust score/mechanic ≠ ecosystem truth. |
| **#13 Ecosystem-level Agent Defense** | IF-S11 peer mechanism + EA | Incident lifecycle and EA as independently testable peers. | Signal lifecycle ≠ EA; neither creates authority. |
| **#14 Agent-to-Principal Legal Binding** | IF-S1, IF-S2, IF-S13 | Principal/representation/legal-binding reference where technically expressible. | EA does not determine legal personhood/liability. |
| **#16 Operational Human Oversight** | IF-S6 | Human authority/capacity, decision, assurance, residual, execution/re-entry state. | Human decision ≠ automatic epistemic repair. |
| **#17 Digital Rights Infrastructure for Text** | IF-S1, IF-S2, IF-S4, IF-S8, IF-S13 | Production-sector rights/identity/registry case: current rights declaration, agent identity, usage purpose, audit history. | Sector case does not define universal agent identity. |
| **#18 Multi-objective trustworthiness** | O1, IF-S7 | Objective/risk/collective-choice evidence and operator-drift assessment where source-owned. | Evaluation ≠ authority. |
| **#19 Lifecycle privacy** | IF-S10 | Minimum disclosure, privacy constraints, disclosure authorization. | EA cannot require unnecessary private state. |
| **#20 Embodied binding** | optional embodied profile, IF-S1, IF-S3, IF-S8 | Agent/runtime/device/authority binding, physical-action attribution, binding freshness. | Embodied binding ≠ motion/control ownership. |
| **#21 Population-scale evaluation** | IF-S9 | Source-native population finding **A(IF-S9)** plus population/period/taxonomy/evaluator-dependence/statistical/identifiability qualification **B(IF-S9)**; C/D only where the 00M frontier/barrier conditions are actually met. EA may consume A or A_ref under a declared profile and produce a separate decision-scoped qualification **A(EA)**. | #21 answers what the population supports inside its measurement frame; EA qualifies what that result can support when legitimately related/composed for a receiving decision. Population measurement is not redirected by relabelling decision context as evidence. |
| **#22 Remote Attestation** | IF-S3 | Evidence/appraisal of runtime/model/policy/interaction state. | Attestation proves only profile-scoped claims. |
| **#23 Authorization / privilege lifecycle** | IF-S2, IF-S4, IF-S12 | Privilege initialization/change/hibernation/reactivation/revocation and execution/enforcement lifecycle. | Privilege state does not replace provenance/current-applicability semantics. |

This table is an **ideal integration map**, not a claim that every Theme has accepted these contracts or that each row requires a separate specification.

---


### 7.1 Theme #21 / IF-S9 — population evidence versus EA qualification

The 00M/04-vNext reading makes the ideal boundary sharper.

**Population / #21 function**

For a rate producer implementing the Theme #21 specification, the native functional question is:

> **What does this declared population of observations support under this taxonomy, observation period, evaluator configuration, dependence assumptions and method?**

The population assessment, rate or other source-native finding is **A(IF-S9)**. Where they are outside A itself, population definition, observation period, taxonomy/reference/version, evaluator characteristics, known dependence state, sampling uncertainty and established identifiability limits are **B(IF-S9)**.

A known, already characterizable additional check remains B even when unused. A grounded additional population/evaluator/measurement route is C only when its evaluation basis is not yet established. D requires a material effect beyond the current effective observation/evaluation route; "unknown", "external" or "not yet pooled" is not enough.

**EA function**

EA does not compute another population merely because it receives a population result. Its receiving question is different:

> **Can this qualified source result be legitimately related to the other qualified results material to this receiving question, what does that composed position support, and what remains unresolved?**

The resulting EA qualification is **A(EA)**. Its affected scope, source relations, validity, dependence, limits and established basis are **B(EA)**; any EA-side C/D must be justified under the same 00M rules.

This gives the compact distinction:

> **Population establishes what observations support inside a measurement frame. EA qualifies what that result may support when related or composed into a different receiving frame, and what must not be carried across.**

**Return direction**

Consistent with the Theme #21 proposer boundary, an ideal EA→#21/rate-producer return may report that the supplied result is insufficient for the receiving decision and may name the missing qualification or coverage gap. It should not send the desired answer, the receiver's target hypothesis, why that answer matters to the decision, or a receiver-set measurement budget as instructions to the evaluator. Any additional measurement question remains owned by the measurement side under its own legitimate scientific/reference frame.

Public boundary anchor:
https://github.com/FG-TIDA/themes/issues/21#issuecomment-5903046577

This section refines the ideal interface; it does not claim that FG-TIDA has adopted the A/B/C/D notation or this exact cross-Theme profile.


## 7A. Internal corpus profiles usable by the ideal projection

05 Ideal may use programme-internal architecture/profile material as **integration aids**, but must not present those artefacts as FG-TIDA-owned semantics merely because they map cleanly to a Theme.

A particularly relevant profile is [**01I — Agentic Citizenship Contract / Human-Governed Participation Profile**](../../baseline/01I_AGENTIC_CITIZENSHIP_CONTRACT_HUMAN_GOVERNED_PARTICIPATION_PROFILE_v0.1.md), together with the canonical ACC lineage/identity/authority binding profile maintained in the MSCA standards package.

01I/ACC can help the ideal FG-TIDA projection express, where a Theme-owned case needs it:

- participant membership / role;
- admissible objectives and actions;
- obligations / prohibitions / non-compensable constraints;
- issuer / approval authority;
- version / validity / revocation / exit;
- lineage and subject binding; and
- signalling or participation duties.

This is especially relevant to ideal mappings around **Theme #4** (metamorphing-agent access/policy), **Theme #23** (authorization/privilege lifecycle), Theme #14 (principal binding), Theme #17 (rights/usage participation) and any future multi-party governance profile.

Boundary: 01I/ACC is **not** silently imported into FG-TIDA as a mandatory common contract. It remains an EA/MSCA-side candidate profile until the relevant FG-TIDA semantic owners adopt equivalent semantics or a reviewed profile mapping. 05A must therefore treat any ACC-derived field as candidate/test-only/not-established unless supported independently by public FG-TIDA sources.

---

## 8. Ideal case portfolio — use existing cases as semantic owners, not duplicate scenarios

An ideal FG-TIDA programme should consume the strongest existing cases before inventing more.

### Public FG-TIDA use cases

| Use case | Ideal primary interface stress |
|---|---|
| **UC #4 — Federated ecosystem defense** | #13 lifecycle ↔ EA; multi-domain signal exchange, blast radius, containment, EHD/profile interoperability. |
| **UC #5 — Silent model substitution** | Model/runtime origin, attestation, delegation/path provenance, cross-border trust, client-side verification. |
| **UC #6 — Same agent, changed purpose** | Current authority applicability, human oversight boundary, semantic TOCTOU, re-entry. |
| **UC #7 — identity/action-time state across executions** | Persistent identity versus execution/state continuity; action attribution; revalidation after state change. |
| **UC #9 — national payment rail / principal authority** | Grant provenance, act-time standing, limits, composition, revocation, identity-anchor integrity. |
| **UC #10 — self-expanding multi-agent molecular design** | Capability without conferral, agent recruitment, identity continuity versus authority continuity, missing grant. |

### Future 00I / UC #6 route-separation reservation

If a dedicated **00I Semantic TOCTOU** scenario is later committed and reviewed, it must remain **parallel to**, not a stage of, the public **UC #6 → Theme #16 matrices → UC #4 executable mapping** route.

- **UC #6** remains the public FG-TIDA semantic case for changed-purpose/current-authority applicability.
- **00I**, if created, would remain an EA/DBC reference failure scenario testing the broader stale-semantic-applicability pattern.
- **UC #4** remains the downstream executable/testbed mapping layer only after the originating semantic owners review the mapping.

The routes may inform one another and may share fixtures or boundary questions, but neither replaces the other's ownership or provenance. This reservation mirrors the existing separation discipline used for 00H versus FG-TIDA case/test routes and prevents a later internal scenario from being mistaken for the source case.


### FG-TIDA Theme #17 / production rights case

Theme #17 provides a production-sector challenge around machine-readable rights, registry history and missing legally accountable agent identity. In the ideal architecture it is a **reference sector case** for identity/authority/policy/audit interoperability, not a universal identity model.

### EA / DAOS case material

The FG-TIDA application package already contains:

- [EA ↔ DAOS model-case interface](../cases/EA_DAOS_MODEL_CASE_INTERFACE_v0.1.md);
- [DAOS → EA use-case engineering masterclass](../cases/DAOS_EA_USE_CASES_MASTERCLASS_v0.1.md).

These remain useful for requirement-first traceability, extension tests and frozen case discipline.

### Rule

A new domain does not justify a duplicate case. Add a new case only when it exposes a materially different:

- authority/identity/evidence condition;
- semantic owner;
- interface failure;
- lifecycle boundary;
- physical/cross-border constraint; or
- falsifier not exercised by the existing portfolio.

---

## 9. Ideal EA validation family inside FG-TIDA — without converting internal profiles into FG submissions

The general EA validation profiles remain EA-owned architecture tests:

- **UC-EA-01** — action-time operating-frame requalification;
- **UC-EA-02** — bounded determination under incomplete/conflicting/partially scoped evidence;
- **UC-EA-03** — human oversight under bounded effective capacity and non-curative approval;
- **UC-EA-04** — scope-indexed composition of locally valid determinations.

In an ideal FG-TIDA environment they can be used as **validation lenses** over Theme-owned cases, without becoming four new FG-TIDA Use Cases or transferring ownership.

Example ideal pairings:

| EA validation lens | Strong FG-TIDA case sources |
|---|---|
| **UC-EA-01** | UC #6, UC #7, UC #9, Theme #17 rights changes, future stale-binding/embodied variants. |
| **UC-EA-02** | UC #4 signal/evidence routes, UC #5 origin uncertainty, #6/#7 evidence limits, #22 attestation. |
| **UC-EA-03** | UC #6 human continuation, #16 matrices, UC #9 threshold/oversight variants. |
| **UC-EA-04** | UC #4 multi-domain federation, UC #9 payment composition, UC #10 recruited/self-expanding agents. |

---

## 10. Ideal executable fixture portfolio

A mature FG-TIDA test programme could combine several existing fixture families while preserving their namespaces and owners.

### A. EA reference failure scenarios

- **00E — 100 Million Tokens / compounded epistemic collapse**
- **00F — Smart-City Mobility / systemic divergence**
- **00G — Collective False-Context Convergence**
- **00H — Batch Opportunity Beyond Authority**

These are not Theme-owned standards cases. They are stress scenarios that can be projected onto Theme interfaces.

### B. DBC boundary fixtures

DBC v0.2 currently defines twelve boundary families. The table distinguishes the **challenge family** from any **dedicated narrative scenario** so that scenario coverage is not silently inferred from related stress material.

| DBC family | Dedicated narrative scenario in repo | Related current stress material / note |
|---|---|---|
| **C01 nominal continuity** | None | Positive/control branches exist across validation work; no dedicated narrative scenario. |
| **C02 semantic TOCTOU** | **None committed** | UC #6 exercises changed applicability; a future 00I has been discussed as a possible dedicated scenario but is not a repository source and is not assumed here. |
| **C03 handoff laundering** | None | Related qualifier-preservation pressure exists in EHD/EA-ITP and 00E/00F; no dedicated narrative scenario. |
| **C04 hidden common dependency** | None | 00G supplies related correlated-repetition/source-dependence stress, but is not a dedicated C04 scenario. |
| **C05 attractive inadmissible opportunity** | **00H** | Direct narrative/quality-gate anchor. |
| **C06 effective-role drift** | None | 00G contains a concrete metamorphic-role variant, but C06 has no separate dedicated scenario file. |
| **C07 targeted recoverable unknown** | None | Exercised as a pattern in requalification work; no dedicated narrative scenario. |
| **C08 structural residual** | None | 00E/00F contain structural-residual stress; no dedicated C08 narrative. |
| **C09 unbounded HOLD / review loop** | None | 00E contains Type-1 review/escalation pressure; no dedicated C09 narrative. |
| **C10 false closure** | None | 00E/00G contain Type-2/false-closure pressure; no dedicated C10 narrative. |
| **C11 authority-capacity / slow-response boundary** | None | 00H non-response and #16 capacity material are related; no dedicated C11 narrative. |
| **C12 authority-mediated re-contracting** | **00H** | 00H provides the bounded re-contracting sequence as part of the same narrative scenario. |

DBC remains a **test/adjudication vocabulary**, not a runtime ontology. A related stress case does not become the semantic owner of a DBC family unless the fixture is explicitly mapped and reviewed.

### C. Theme #13 interoperability

[EA-ITP-01](../tests/EA-ITP-01_v0.1_FROZEN.md) tests the Theme #13 / UC #4 profile of the general EHD across implementations.

### D. UC #4 staged testbed

The ideal programme can use UC #4's staged direction:

- deterministic/frozen Stage 0;
- federated independently governed Stage 1;
- admitted regulated profiles;
- broader multi-service/adversarial campaigns;
- resolution/revalidation.

The ideal 05 assumption is that multiple independent domains and implementers are available; two endpoints may prove protocol interoperability but do not alone prove ecosystem behaviour.

---

## 11. Ideal validation pipeline

A high-capacity FG-TIDA should use one reusable pipeline rather than a separate method for each Theme:

**Theme / case semantic source**  
→ **freeze bounded facts and owner**  
→ **map to S#/T#/H#/KPI route**  
→ **select 04 interface/profile**  
→ **select 05 ideal bilateral/multilateral contract**  
→ **derive fixture without changing source facts**  
→ **version-pinned adapter/profile**  
→ **independent producer + receiver where feasible**  
→ **expected outcome/oracle owned or accepted by the semantic owner**  
→ **trace + ICR / evidence record**  
→ **review by case/interface owners**  
→ **freeze only after review**

This pipeline lets one case exercise several interfaces without turning the testbed into the semantic owner.

---

## 12. Ideal organizational / contributor topology

The ideal map assumes enough people and independent organizations to keep ownership distributed.

Useful roles include:

- Theme / semantic owner;
- case owner;
- specification editor;
- interface/profile editor;
- adapter implementer;
- fixture author;
- independent producer implementation;
- independent receiver implementation;
- test/conformance maintainer;
- oracle/adjudication reviewer;
- adversarial challenger;
- privacy/security reviewer;
- authority/policy domain reviewer;
- cross-Theme integrator;
- evidence/provenance maintainer.

One person may hold several roles in an early prototype, but the evidence record should state that concentration. Stronger claims should progressively separate semantic ownership, implementation, execution and review.

This is the sense in which 05 Ideal may be thought of as a **fully resourced FG-TIDA**: not a super-controller, but enough independent contributors to make the interfaces genuinely testable.

---

## 13. Ideal multi-Theme interface bundles

Not every test should activate every Theme. The ideal map should use **minimum sufficient bundles**.

### Bundle A — authority continuity / act-time standing

Possible owners:

- #5 authority provenance;
- #1 action records;
- #7 verifier semantics;
- #16 human oversight where intervention occurs;
- #23 privilege lifecycle where privilege state changes;
- EA for systemic qualification/requalification.

Cases: UC #6, #7, #9.

### Bundle B — ecosystem incident / containment

Possible owners:

- #13 incident lifecycle;
- EA peer mechanism;
- #5 authority;
- #6 policy/conformance;
- #10/#23 enforcement/privilege lifecycle;
- #16 human oversight;
- #1 records.

Case: UC #4.

### Bundle C — model/runtime provenance

Possible owners:

- #11 model-level trust;
- #22 attestation;
- #7 verifier semantics;
- #5 delegation;
- #1 records;
- #19 privacy;
- EA for composed reliance.

Case: UC #5.

### Bundle D — self-expanding capability / recruited agents

Possible owners:

- #2 discovery;
- #5 authority;
- #1 identity/action history;
- #4 metamorphing-agent security;
- #11 model change;
- #12 trust mechanics;
- #6 policy;
- #16 human oversight where used;
- EA for systemic qualification.

Case: UC #10.

### Bundle E — rights / publishing

Possible owners:

- #17 production rights case;
- #1/#8/#14 identity/principal/trust references;
- #5 authority/delegation;
- #6 policy/intent;
- #7 verifier semantics;
- #19 privacy;
- #22 attestation where used;
- EA for cross-source qualification.

### Bundle F — embodied action

Possible owners:

- #20 embodied binding;
- #22 attestation;
- #5 authority;
- #1 action records;
- #6 policy;
- #23 privilege lifecycle;
- #16 human oversight;
- EA for system-level qualification.

These bundles are examples of ideal composition, not mandated WG structure.

---

## 14. Ideal state-separation rules

Across every ideal contract, the following distinctions should survive:

- identity ≠ representation ≠ authority;
- capability ≠ conferred authority;
- persistent identity ≠ action-time state;
- opportunity ≠ admissibility ≠ authority ≠ execution;
- per-action compliance ≠ aggregate/composed authorization;
- attestation ≠ truth of every claim;
- policy verdict ≠ ecosystem truth;
- human authorization ≠ epistemic repair;
- decision ≠ attempted execution ≠ externally confirmed outcome;
- incident resolution ≠ ecosystem requalification;
- local closure ≠ system-level determination;
- correlated multiplicity ≠ independent corroboration;
- technical/token validity ≠ continued semantic applicability;
- signal confidence ≠ systemic determinacy;
- containment reach ≠ containment authority;
- input/output direction ≠ A/B/C/D role;
- source A ≠ EA's A;
- population support within a measurement frame ≠ decision-scoped composed support.

These are composition rules, not a requirement that every producer emit one common schema.

---

## 15. Ideal timing and re-entry discipline

Each relevant contract should be able to preserve, when material:

- evidence freshness/as-of;
- authority/delegation validity;
- policy/configuration validity;
- qualification validity/review condition;
- operational response deadline;
- human/compute/evidence capacity;
- targeted re-entry reference;
- expiry/no-valid-response semantics.

The ideal system should re-enter at the **smallest invalidated assumption or dependency**, rather than automatically restarting the full pipeline.

DBC-C02 is the principal current semantic-TOCTOU fixture for this rule.

00H / DBC-C12 additionally test bounded re-contracting when authority rather than evidence is the missing condition.

---

## 16. Ideal conformance and evidence model

Every material ideal contract should eventually have:

1. at least one positive fixture;
2. one boundary fixture;
3. one rejection/adversarial fixture where relevant;
4. source-native expected outcome or accepted oracle;
5. version-pinned producer/receiver profile;
6. explicit UNKNOWN/not-established handling;
7. evidence of independent versus simulated boundaries;
8. burden measures;
9. execution/outcome evidence where action is claimed;
10. review record from the relevant semantic owner.

A passing interface test means only that the named route/profile preserved the stated semantics for the declared fixture and horizon. It does **not** establish universal Theme conformity or EA effectiveness.

---

## 17. Ideal 05 versus 05A

The distinction must remain structural:

### 05 Ideal

May contain:

- all coherent 04-derived cross-Theme contracts;
- candidate Theme mappings whose semantic owners could support them;
- all useful case/fixture/test routes;
- richer Composition-Critical profiles;
- multiple independent implementers;
- full cross-sector stress campaigns;
- future specification/test splits.

### 05A Current-State

May contain only:

- what current public FG-TIDA sources support;
- fields/relationships with current source anchors;
- candidate mappings clearly marked as such;
- test-only evidence separated from runtime semantics;
- NOT ESTABLISHED where the ideal relation lacks present support.

The **gap between 05 and 05A is useful evidence**. It shows where FG-TIDA would need more semantic ownership, agreement, implementation or test evidence to approach the ideal architecture.

---

## 18. Current ideal-delta determination

The current corpus and public FG-TIDA evolution justify a substantially richer future 05 than the frozen v0.4, without requiring any new generic 04 interface family.

A future ideal-interface version should at minimum:

1. model Theme #13 as **peer Incident/Signal Lifecycle ↔ Ecosystem Awareness mechanisms**, independently testable and bidirectionally connected;
2. incorporate the approved bounded Theme #16 UC #6 → matrices → UC #4 executable route;
3. carry CAND-R1, CAND-R2 and CAND-R3 as ideal composition/readability constraints without expanding the universal EHD kernel;
4. distinguish semantic/qualification validity from response time and use DBC-C02 as the current TOCTOU test;
5. include the broader FG-TIDA capability map, especially discovery, verifier semantics, model-level trust, principal/legal binding, embodied binding and privilege lifecycle work omitted from frozen 05;
6. use existing public Use Cases #4/#5/#6/#7/#9/#10 and Theme #17 before inventing duplicate scenarios;
7. use UC-EA-01…04 as EA validation lenses, not new FG-TIDA use cases;
8. integrate 00E–00H, DBC-C01…C12, EA-ITP-01, DAOS and UC #4 staged testing into one requirement-first conformance pipeline;
9. allow cumulative/action-history relations as conditional Composition-Critical profile elements where authority is aggregate;
10. preserve source-native semantics and semantic-owner review throughout;
11. assume enough independent contributors/implementations for genuine interoperability and adversarial testing, while recording role concentration where independence is not achieved; and
12. preserve the rule that an ideal contract becomes current only through the separate 05A source/owner process;
13. apply the 00M producer-relative A/B/C/D recognition discipline without turning field names or interface direction into roles;
14. allow declared full-result versus metadata-only profiles (`A + B/C/D` or `A_ref + B/C/D`) without universal exclusion of source A; and
15. preserve the Theme #21 boundary: population evidence remains measurement-frame native, while EA performs downstream decision-scoped qualification/composition rather than directing the measurement toward a desired decision outcome.

No claim is made here that FG-TIDA has adopted, staffed, implemented or validated this ideal map.

This delta remains open and cumulative. New ideal FG-TIDA interface developments should be appended here rather than inserted into frozen 05 v0.4.


---

## Auditoría realizada por Codex — IF05-VNEXT-AUD-001

**Fecha:** 6 de octubre de 2026. **Fuente interna:** commit `1d24b7bfe88fa366e6c619fa88f6f7904d1380db`; este VNext blob `3bc1909bb5cfe38a26757547f6074d289b3cf974`. **Lectura:** todo este VNext, controles/boundaries de 05 v0.4 parte1, 04 VNext/Recognition Guide y Requirements VNext. **Fuentes externas:** GET de ocho comentarios concretos en FG-TIDA/themes, conservando sus autores/created/updated; no lectura íntegra de todos los Themes/Use Cases ni verificación de implementación o ejecución. **Auditor:** Codex de este chat, no independiente externo.

### Instrucciones y relación de fuentes

IVAN-20261006-START-SEQUENTIAL-AUDITS: publicar auditorías una por una en los documentos VNext existentes. Esta es la cuarta etapa, después de README, Requirements y 04. Fuente ideal05 y filtro público05A se auditan por separado. Una propuesta propia de Iván no constituye confirmación independiente por ser un comentario público.

| Hallazgo | Evidencia / evaluación | Estado |
|---|---|---|
| IF05-R1-F001 | §6 enlaza 00I existente, pero §8 lo reserva como futuro y §10 declara «None committed» en C02. La contradicción existe dentro del mismo documento, antes de comparar el router. | DELTA-001 propuesto; no reescribir la historia para ocultarlo. |
| IF05-R1-F002 | §5/§18 heredan tres candidates, aunque Requirements incluye CAND-R4. Dos ventanas temporales (§6/§15) no resuelven por sí solas check-to-use binding. | Revisar si el puente pertenece a perfil04, propietario de ejecución o ambos; no inventar payload universal. |
| IF05-R1-F003 | Ward confirma placement en #13 e independencia de envelope/lifecycle; Nelson acepta la interacción desde testbed y deja formal peer characterization/general EHD para confirmación Theme13. La tabla de Iván preserva esa reserva. | El ideal de dos peers es propuesta interna compatible con parte de los anchors, no formal arquitectura FG-TIDA adoptada. No se infiere que nunca haya confirmación posterior: no se revisó todo el thread. |
| IF05-R1-F004 | En #16, Nelson propone secuencia, Arpita acepta preservar hechos UC6, Olena acepta matrices v0.2 y Lei aprueba avanzar con revisión antes de freeze. | Aprobación del proceso acotado respaldada; no equivalente a mapping final aprobado, fixture ejecutado ni adopción. |
| IF05-R1-F005 | El comentario #21 exige separar pregunta de población de suficiencia para decisión; acepta gap feedback y rechaza orientar medición con target/context/budget del receptor. §7.1 de este VNext conserva esa distinción. | Correspondencia documental positiva. Theme21 es specification; rate producer implementa. No asumir resultado poblacional disponible o independencia demostrada. |
| IF05-R1-F006 | §10A/§18 enumeran 00E–00H; el router y Requirements cubren 00E–00J. El catálogo ideal no declara razón para excluir I/J aunque §6 usa I. | Cobertura temporal incompleta; proponer actualización de la tabla específica, no convertir internal scenarios en FG submissions. |
| IF05-R1-F007 | Full-result/A_ref se hereda como candidate direction de 04, cuya H06/176-row validation sigue abierta. | Ninguna proyección a un Theme cierra la insuficiencia genérica; cada perfil necesita binding/consumer test. |

### Registro de anclas públicas comprobadas

| Theme | Fuente / autor y fecha UTC | Qué respalda y qué no |
|---|---|---|
| #13 | [Ward, comentario 5571476256](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5571476256), creado 7 Sep 2026, actualizado 7 Sep | EA en13, envelope/lifecycle independientemente probables; no ejecución comprobada ni peer status formal adoptado. |
| #13 | [Nelson, 5639226397](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5639226397), 11 Sep | Compatibilidad desde UC4/testbed y envelope como perfil desde ese lado; reserva confirmación arquitectónica a Ward. |
| #13 | [Iván, 5640186655](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5640186655), 11 Sep | Tabla propia explicativa conserva reserva Theme13; no es validación independiente. |
| #16 | [Nelson, 5803023066](https://github.com/FG-TIDA/themes/issues/16#issuecomment-5803023066), 23 Sep | Propone mapping sin campos nuevos y revisión antes de freeze. |
| #16 | [Arpita, 5803653565](https://github.com/FG-TIDA/themes/issues/16#issuecomment-5803653565), 23 Sep | Acepta límite de caso y ofrece revisar primer mapping; no aprueba un resultado inexistente. |
| #16 | [Olena, 5804125734](https://github.com/FG-TIDA/themes/issues/16#issuecomment-5804125734), 23 Sep | Acepta trabajo de matrices condicionado a lead. |
| #16 | [Lei, 5809248877](https://github.com/FG-TIDA/themes/issues/16#issuecomment-5809248877), 24 Sep | Autoriza esa secuencia/scope desde16, con semantic review antes de freeze. |
| #21 | [Justin/GospelNerd, 5903046577](https://github.com/FG-TIDA/themes/issues/21#issuecomment-5903046577), 30 Sep | Preguntas y return-direction boundary; pooled assumption debe declararse, UNKNOWN no implica independencia. |

Estas fechas describen los comentarios, no fecha de adopción. Lectura hecha el 6 de octubre. No se envió mensaje ni se pidió confirmación a esos participantes.

**Navegación interna:** 17 enlaces locales, 14 destinos, presentes. Las fuentes externas no incluidas en la tabla permanecen pendientes; no se atribuye revisión exhaustiva de los22 Themes listados.

### Conversación de auditoría

**Codex, respuesta a §3/§18:** el mapa ideal puede expresar la relación peer como propuesta, con semantic-owner review pendiente y límites de testbed explícitos. La aceptación de un proceso de trabajo no debe convertirse por tránsito en aceptación del diseño compuesto, de todos los payloads ni de su eficacia.

**Codex, respuesta a §7.1:** se conserva la frontera de Theme21 y la fuente A. Una solicitud de medición compatible con esa frontera debe ser definida por el propietario científico y no por el resultado de decisión que el cliente desea obtener.

## Propuestas quirúrgicas — IF05-R1, pendientes

### IF05-R1-DELTA-001 — C02/00I en el catálogo

**Objeto:** este VNext §10B; blob de esta época. **Hallazgo:** F001. **Preparación:** IVAN-20261006-START-SEQUENTIAL-AUDITS; incorporación pendiente.

**TEXTO ANTES**

```markdown
| **C02 semantic TOCTOU** | **None committed** | UC #6 exercises changed applicability; a future 00I has been discussed as a possible dedicated scenario but is not a repository source and is not assumed here. |
```

**TEXTO DESPUÉS**

```markdown
| **C02 semantic TOCTOU** | **00I v0.5 Freeze Edition, internal EA scenario** | UC #6 remains the FG-TIDA changed-applicability semantic case. The committed 00I scenario is a parallel internal stress source; a reviewed fixture mapping is required before its use as FG-TIDA execution evidence. |
```

**Efecto:** reconocer archivo existente y preservar source ownership. **Dependencias:** §6/§8/§10A/§18 y 05A; esos pasajes requieren revisión coordinada antes de aplicar para no dejar la reserva «future00I» contradictoria. No se afirma ejecución. **Decisión de Iván:** pendiente. **Incorporación:** no ejecutada.

### IF05-R1-DELTA-002 — carácter propuesto de los peers

**Objeto:** este VNext §3, una frase única. **Hallazgo:** F003. **Tipo:** precisión de status y attribution, no cambio de funciones.

**TEXTO ANTES**

```markdown
Theme #13-derived work should contain **two peer mechanisms**:
```

**TEXTO DESPUÉS**

```markdown
For this ideal projection, the proposed Theme #13-derived architecture contains **two peer mechanisms**. The cited public anchors support placement and independent testing and express compatibility from the UC #4/testbed side; formal peer characterization and the general EHD abstraction remain subject to the relevant Theme #13 confirmation and review, without implying adoption:
```

**Gate:** si otras fuentes posteriores cierran esa confirmación, añadir sus referencias exactas y registrar fecha/scope antes de adjudicar este wording. No se proclama ausencia definitiva de confirmación. **Decisión de Iván:** pendiente. **Incorporación:** no ejecutada.

### Cobertura restante

Partes2/3 del contrato congelado, todos los mappings de Themes, cada use case nativo, datos de testbed, historia completa de13 y revisión source-to-profile quedan pendientes. Esta es una primera auditoría documental de la VNext y algunos anchors críticos; no una validación del mapa ideal entero.


---

## Quinta pasada — investigación externa, diferencial y reutilización

**Instrucción de Iván, 6 de octubre de 2026. Estado: contraste específico pendiente.** Esta quinta pasada se realiza después de las cuatro y queda dentro de esta misma VNext. No se crea otro expediente ni se incorporan propuestas a la fuente por esta anotación.

**Pregunta de este documento:** Comparar el diseño ideal con necesidades y realizaciones de otros contributors y protocolos. Identificar coincidencia funcional y piezas reutilizables preservando propietarios, y devolver límites del estado público a 05A.

Se fijarán trabajos primarios de FG-TIDA y de otras líneas relevantes, incluidos antecedentes y actualizaciones posteriores, con autor, versión, fecha y alcance realmente leído. Aquí se justificará qué coincide, qué diferencia podría sostenerse y qué pieza concreta conviene reutilizar, con sus condiciones de atribución, adaptación y compatibilidad.

El [mapa externo preparatorio](../../../../governance/review/EP_EXTERNAL_RESEARCH_REVIEW_2026-10-06.md) aporta fuentes iniciales; no completa esta pasada. El [plan 1.6](../../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md#quinta-pasada--trabajos-externos-diferencial-y-reutilización) gobierna método y cierre. Las cuatro lecturas previas mantienen sus estados reales y se reabren si aparece evidencia que las afecte. Codex, mismo asistente de IA; anotación de alcance, sin independencia externa.
