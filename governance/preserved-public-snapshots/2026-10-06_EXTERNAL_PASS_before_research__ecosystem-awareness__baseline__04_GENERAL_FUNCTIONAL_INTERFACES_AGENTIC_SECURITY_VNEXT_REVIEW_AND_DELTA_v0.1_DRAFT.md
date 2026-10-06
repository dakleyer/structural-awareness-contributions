> [!NOTE]
> **Revisión para personas · instrucción de Iván del 6 de octubre de 2026.** El [plan de trabajo](../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md) exige cuatro pasadas diferentes, registradas en esta misma VNext: **fondo y lógica; evidencia y relaciones; edición y formato; legibilidad humana**. Después habrá una conciliación del corpus, con consecuencias en cada VNext afectada. El centro es comprender y cuestionar la idea; códigos y comprobaciones técnicas quedan como apoyo. La exploración mixta publicada antes se conserva, pero no se cuenta como cuatro pasadas terminadas.

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
> **VNext · auditoría acumulativa R1 · 6 de octubre de 2026.** Se conserva íntegro el expediente previo. La auditoría y las propuestas están al final; no se promueve el baseline 04 ni se revalida por defecto el mapa de 176 entradas. [Procedimiento](../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md) · [visión general](../../../architectural-contributions/ecosystem-positioning/README_VNext.md).

# 04 General Interfaces vNext Review & Delta — Ecosystem Awareness

> **A/B/C/D semantic reference.** [00M §1 — canonical A/B/C/D definitions](00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical) governs these process-relative roles. A known assessable option left unused is B; C requires a grounded but uncharacterized exploration avenue; D requires an effective evaluation barrier. This reference does not rename local test arms, change requirements or revalidate recorded proofs/results.

> **Working delta only — not a new interface specification.**  
> The current programme-independent interface reference remains [**04 — General Functional Interfaces & Agentic Security v0.5 Integrated**](./04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md).  
> The historical controlled v0.4 source remains preserved separately.  
> This file accumulates post-baseline addenda, clarifications and review questions. It may remain partial while review is active. Nothing here changes O1–O6, IF-S1–IF-S13, the EHD kernel, the Composition-Critical profile or Appendix A unless a later 04 version is explicitly promoted.
>
> **Downstream navigation only.** The FG-TIDA-specific ideal/current projections are 05/05A. They consume this layer; no FG-TIDA Theme semantics belong in the 04 technical delta itself.

| | |
|---|---|
| **ID** | 04-vNext Review & Delta |
| **Version · date** | v0.1-draft · opened 24 September 2026 |
| **Status** | Cumulative interface delta / review; incomplete by design; no change to 04 v0.5 baseline |
| **Current 04 baseline** | General Functional Interfaces & Agentic Security v0.5 Integrated |
| **Historical controlled source** | 04 Functional Interfaces & Agentic Security v0.4 split source |
| **Upstream control** | [00 Requirements frozen baseline](./00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) + [Requirements vNext Review & Delta](./00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) |
| **Downstream consumers** | Programme/domain-specific application mappings, validation/test profiles and later specification-preparation work |

---

## 1. Delta rule

04 is the **programme-independent interface layer**. This delta therefore asks only whether post-baseline work requires a change to the generic EA interface architecture.

It does **not** import programme-specific identifiers, ownership structures or institutional mappings into 04. Those belong only in downstream application profiles.

For each new development, the review asks:

1. does the upstream Requirements delta expose a genuinely new solution-neutral obligation?;
2. if not, does the current 04 already express the needed interface semantics?;
3. if partly, is only an editorial clarification or optional profile refinement needed?;
4. does the proposed change belong instead to component conformance, a test profile, a signalling/control annex or a programme-specific mapping?;
5. would adding the field/family create unnecessary metadata or semantic coupling for simple routes?

A new architecture object, scenario field, test disposition or programme-specific mapping is **not** automatically a new O#/IF-S# family or universal EHD field.

---

## 2. Upstream Requirements disposition

The current [Requirements vNext Review & Delta](./00_REQUIREMENTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) does **not** justify S15, T5, H7 or a new canonical KPI family.

That constrains 04-vNext in the same direction:

- do **not** create O7 merely because later architecture adds a new processing object;
- do **not** create IF-S14 merely because a later scenario or test names another boundary;
- do **not** expand the six-element EHD interoperability kernel merely because one fixture benefits from an extra qualifier;
- prefer conditional/profile semantics where the information is material only to specific compositions.

Three Requirements clarification candidates are interface-relevant.

### CAND-R1 — effective-role drift

The later corpus makes the distinction

`Role_bound ≠ Role_effective`

more operationally visible.

**Tentative 04 consequence:** where role/function drift is material to the receiving decision, a producer or adapter may need to preserve enough source-owned state to distinguish:

- declared/bound role or representation;
- observed effective function/state;
- the basis and time of the observation; and
- whether current authority/applicability for that effective function is established, not established or external to the producer.

This should initially remain a **conditional qualifier/profile concern**, not a new universal EHD kernel field and not a new identity/authority interface family.

Continuity of identity, name, runtime lineage or newly acquired capability must not be interpreted by 04 as proof of continuity or expansion of authority.

### CAND-R2 — opportunity / admissibility / authority / execution

The later corpus increasingly uses the reading rule:

`opportunity ≠ admissibility ≠ authority ≠ execution`.

**Tentative 04 consequence:** the generic interface architecture should remain capable of carrying these distinctions without translating one into another.

In particular:

- a high-value or technically reachable candidate may be preserved as information without becoming permission;
- a policy/admissibility result remains source-owned;
- an authority response remains authority-owner state;
- an execution/outcome record remains distinct from the decision or request that preceded it.

The current 04 already supports most of this through O1/O5, IF-S2, IF-S4, IF-S8, IF-S11/12 and the Composition-Critical EHD profile. The delta therefore records a likely **editorial clarification**, not a new interface family.

### CAND-R3 — per-action compliance versus aggregate/composed authorization

The upstream Requirements delta now makes explicit:

`per-action compliance ≠ aggregate/composed authorization`.

00H supplies the concrete falsifier: every atomic action may satisfy a local cap or rule while the cumulative campaign remains outside the participant's legitimate authority boundary.

**Tentative 04 consequence:** where authority is defined over a cumulative, campaign-level, resource-time or other composed effect, the interface route may need a **conditional Composition-Critical relation** that preserves enough action-history / aggregate-lineage state for the legitimate owner or relying party to evaluate the composed effect.

This should **not** become a seventh mandatory EHD kernel element. The relevant aggregate/composition boundary is source-owned and context-specific. A simple single-action route should not carry aggregate-history metadata merely because another profile needs it.

The current 04 already provides the right extension point through decision/operation references, predecessor/parent relations, decision-basis references and source-owned authority semantics in the Composition-Critical EHD profile. The vNext question is therefore whether that profile should state the aggregate/cumulative case explicitly, not whether a new interface family is needed.

---

## 3. 00G — false-context convergence and source-dependence pressure

[00G — Collective False-Context Convergence](./00G_FAILURE_MODE_COLLECTIVE_FALSE_CONTEXT_CONVERGENCE_v0.1.md) adds a post-baseline stress case in which repeated claims, role drift, authority claims and attractive opportunity can displace the legitimate operating frame.

### Interface pressure

A sufficiently expressive route must be able, where material, to preserve:

- source/provenance and upstream dependence;
- independent versus correlated corroboration;
- claimed versus established scope;
- claimed versus established role/authority;
- current objective/mission or the reference that owns it;
- material unresolved qualifiers;
- a bounded requalification target rather than an indiscriminate request for more context.

### Current 04 coverage

The current 04 already contains:

- EHD source/provenance/dependency semantics;
- explicit UNKNOWN handling;
- decision-scope projection;
- source-native ownership;
- O1 objective/mission references;
- IF-S1/IF-S2 identity and authority boundaries;
- IF-S7 drift/observability;
- IF-S11 ecosystem signal/incident exchange;
- optional Composition-Critical lineage/dependency fields.

### Delta disposition

**No new O#/IF-S# family established.**

Potential later clarification:

- make the “correlated repetition is not independent corroboration” rule more prominent in the general interface reading;
- cross-reference CAND-R1 where role drift is material.

00G remains scenario/test pressure, not an interface-specification source by itself.

---

## 4. 00H — beneficial opportunity beyond current authority

[00H — Batch Opportunity Beyond Authority](./00H_FAILURE_MODE_BATCH_OPPORTUNITY_BEYOND_AUTHORITY_v0.1.md) adds a post-baseline stress case in which a candidate action is valuable, technically reachable and well evidenced but lies outside the participant's current role/grant.

It also tests a second failure: individually compliant actions may form an unauthorized aggregate campaign.

### Interface pressure

Where the receiving decision depends on these facts, a route may need to preserve:

- current grant/authority reference and scope;
- action/operation reference;
- aggregate lineage or action-history relation when the authority condition is aggregate rather than per transaction;
- the candidate finding/opportunity as a separate information object;
- request/re-contract/requalification state;
- authority-owner response;
- response expiry/no-valid-response;
- requalification before any subsequent execution;
- actual execution/outcome separately from approval or request.

### Current 04 coverage

The Composition-Critical EHD profile already allows decision/operation references, parent/predecessor relationships, decision-basis references, validity/review conditions, targeted re-entry and external authority ownership.

IF-S2, IF-S8, IF-S11 and IF-S12 already separate authority, record, signal/request and execution/control concerns.

### Delta disposition

**No universal EHD expansion yet.**

The aggregate-action relation is material only for some authority models. It should first be treated as a **conditional Composition-Critical profile requirement** or external record reference, not a metadata tax on every handoff.

`RepositionIntent`, `AuthorityResponse` and DBC dispositions remain owned by their signalling/control/test layers. 04 only needs to preserve the semantic separability of request, authority response, requalification and execution.

Silence/expiry must remain representable without being silently translated into permission.

---

## 5. Decision Boundary Challenge v0.2 — test vocabulary must not become interface ontology

[Decision Boundary Challenge v0.2](../DECISION_BOUNDARY_CHALLENGE_v0.2.md) distinguishes:

- producer-native result;
- determination condition / Type 0/1/2;
- operating posture;
- DBC procedural disposition;
- authority-owner response;
- execution/outcome.

Its CAN / KNOW / MAY / SHOULD / ACT questions are useful for testing boundary collapse.

### 04 consequence

The generic interface architecture should be able to **preserve the separability** of these layers where a test route uses them.

It should **not**:

- translate external verdicts into DBC dispositions;
- make DBC disposition a universal EHD field;
- make P1/P2/P3 universal interface semantics;
- make AuthorityResponse a universal transport enum; or
- create a new interface family solely for DBC.

### Delta disposition

**Test/conformance pressure only.**  
Use DBC to expose missing or laundered boundaries in 04 implementations; do not use it to redefine 04 by default.

---

## 6. Semantic/qualification validity window versus response window

Two independent post-baseline routes make the same temporal distinction visible. The Operational Risk / Response Window / Epistemic Opportunity v0.2 work separates qualification validity from response timing. Independently, [DBC-C02 — semantic TOCTOU](../DECISION_BOUNDARY_CHALLENGE_v0.2.md#5-challenge-pack-families) tests whether a result can remain technically available or syntactically valid while a material authority/evidence/context condition has become stale before use. Together they make two temporal concepts more explicit:

1. **semantic / qualification validity window** — how long evidence, authority, delegation, policy, configuration and supporting assumptions remain applicable; and
2. **operational response window** — how long remains to materially affect the outcome.

The same work distinguishes:

- more can still be known within current available capacity; from
- more knowledge would still be useful for the current decision.

### Current 04 coverage

04 already contains:

- freshness/as-of;
- validity interval or revalidation condition;
- response horizon;
- capacity binding;
- observation/determination burden;
- targeted re-entry;
- F2/F4/F5/F6/F7 responsibilities for acquisition, qualification, composition, posture and requalification.

### Tentative 04-vNext clarification

A later 04 version should make explicit that **validity time and response time are not interchangeable**.

Where material, a producer/adapter should be able to preserve both without forcing them into one scalar or universal field.

Likewise, an epistemic-processing outcome such as:

- continue investigation;
- stop because current support is sufficient;
- redirect effort;
- request targeted corroboration/requalification;

must remain distinct from an authorized operational intervention.

### Delta disposition

Likely **editorial/interface clarification**, not a new function or interface family.

DBC-C02 provides the applied-validation route for this distinction now. If a future 00I Semantic TOCTOU scenario is committed, it should be cited here as an additional scenario-level stressor only after its repository text is reviewed; it must not be presumed from a chat-only draft.

---

## 7. Human-review outputs under the general handoff discipline

Later human-oversight discussion has made a useful generic distinction visible:

1. human decision/result;
2. assurance in the received review event;
3. capacity binding/qualification;
4. residual/inherited indeterminacy.

The important boundary is that assurance concerns the evidentiary status of the received human-review event; it is not a generalized judgment of human competence.

### Current 04 coverage

IF-S6 already owns Human Oversight & Intervention Capacity, while EHD can carry result, uncertainty/assurance semantics, capacity and residual qualifiers conditionally.

### Tentative 04-vNext consequence

A future editorial pass may make explicit that **human-produced outputs are not exempt from bounded epistemic handoff discipline** merely because the channel is authenticated or the actor is authorized.

That does not require every human decision to carry a complex score. Lightweight categorical/structured qualifiers remain sufficient where they preserve the material distinction.

### Delta disposition

Candidate clarification within IF-S6/EHD guidance.  
No new mandatory kernel field at this stage.

---

## 8. IF-S11 external signal / incident peer capability — preserve, do not redesign

The current 04 already states that an external incident-signal / affected-scope mechanism is a concrete **IF-S11 peer capability** that EA can consume rather than reproduce, and that EA may also be needed where no incident or malicious participant exists.

This is the correct programme-independent boundary:

**external signal / incident capability ↔ EA qualification / requalification**

Both sides may be independently implemented and tested. The external mechanism owns its signal/lifecycle semantics; EA owns decision-scoped systemic qualification. Neither side gains action authority merely by emitting a signal, assessment or request.

### Delta disposition

**No generic architectural change required. Preserve the current peer-capability boundary.**

A later 04 editorial revision may make the bidirectionality easier to read while keeping every programme-specific owner, Theme number, lifecycle name or institutional mapping outside 04.

---

## 9. Downstream specialization rule

The change-control order is generic:

**Requirements baseline**  
→ **Requirements delta/review**  
→ **04 General Interfaces baseline**  
→ **04 General Interfaces delta/review**  
→ **programme/domain-specific mappings**

Therefore:

- a downstream application may specialize, map or narrow a reviewed 04 capability;
- a downstream application cannot create a new generic EA interface merely because its local programme needs it;
- current-state application profiles may be narrower than an ideal application profile;
- a downstream issue that reveals a genuine generic gap returns upstream to this 04 delta rather than silently changing 04 semantics.

---

## 10. Current delta determination

The post-baseline material reviewed through 24 September 2026 does **not** currently justify:

- O7;
- IF-S14;
- a seventh mandatory EHD kernel element;
- a mandatory DBC/ACC/MSCA/programme-specific vocabulary in the generic interface layer; or
- a new universal human-review or incident payload.

The strongest likely 04-vNext changes are presently **clarifications and conditional profile refinements**:

1. make effective-role drift preservable where material without treating observed function as authority;
2. make opportunity / admissibility / authority / execution separation visually explicit;
3. make per-action compliance versus aggregate/composed authorization explicit where the authority boundary is cumulative;
4. distinguish qualification-validity time from operational response time;
5. clarify that human review outputs can carry bounded assurance/capacity/residual qualification;
6. reinforce source-dependence / independent-corroboration preservation;
7. treat cumulative/aggregate action-history as a **conditional Composition-Critical profile element** where the authority rule is aggregate rather than per transaction, without adding it to the universal EHD kernel; and
8. preserve the current IF-S11 peer-capability relation while making generic bidirectionality easier to read.

This delta remains open and cumulative. New post-baseline interface findings should be appended here first. The 04 v0.5 Integrated baseline is not silently rewritten while review is active.

---

## 11. Input-interface contract working starting point — 30 September 2026

The owner-authorized [**EA Input Interface Contract v0.4**](./04_INPUT_INTERFACE_CONTRACT/04_INPUT_INTERFACE_CONTRACT_v0.4.md) ([preserved Word](./04_INPUT_INTERFACE_CONTRACT/04_Contrato_interfaces_entrada_EA_v0.4.docx)) is published **within 04** as the starting point for input-interface work. It is programme-independent and precedes any 05/05A projection. It does not specify EA outputs.

The contract preserves the 176 reviewed input bullets across O1–O6 / IF-S1–IF-S13 and proposes their component-level decomposition. It adds a reader guide, classification diagram, N01–N13, 17 recorded findings, 44 analytical adversarial cases, worked discovery/retrieval examples and one semantic profile represented through HTTP, a message queue and a file batch. These are specification and mapping artefacts, not executed adapters or empirical transport-equivalence results.

### Proposed input boundary

- A is the producer's functional product; its value goes to its operational consumer and is excluded from this EA handoff route.
- B preserves already-established meaning, support, coverage and limits about A, to the extent they are outside the functional product.
- C preserves a recognized, insufficiently characterized possibility that was not examined through an available path, with its existing exclusion reason or the honest absence of that reason.
- D preserves a recognized dependency beyond the declared effective determination boundary, with the existing limit/reason. Lack of control alone does not establish D; the communicated subset does not exhaust unknown residuals.
- Packaging does not change the producer frame. Capture/transport overhead is distinct from new epistemic computation. Missing reasons are not reconstructed.
- N13 allows a process to be declared **family not classified** instead of forcing it into the nearest family. This is independent of A/B/C/D; it does not add O7 or IF-S14 automatically.

### Integration work that remains open

| Item | Concrete work in 04 | Closure boundary |
|---|---|---|
| **H06 — exclusion of A** | Reconcile §2's EHD kernel, §8's local-output requirement, Appendix-A routes and §7/F9 consumers with the metadata-only input profile. Identify uses that remain unsupported without A. | Not closed by relabelling operational results as B or by publishing this contract. No claim that all F1–F9 uses remain sufficient. |
| **Topology terminology** | Align the producer-relative A/B/C/D definitions with the current topology, preserving the distinction between communicated D and unenumerated structural residual. | Explicit semantic review before promoting a successor baseline. |
| **O2 expression** | Explicitly map any natively available omitted catalogue/path/reason and out-of-scope dependency into the discovery profile; the existing seven O2 bullets do not enumerate these pieces fully. | Do not claim those components are already requested, generated or implemented; no new producer computation merely to populate them. |
| **Profile and route conformance** | Review producer-owned meanings and, for implementations, exercise adapters for preservation, missingness, duplicates, time, versions and burden. | Illustrative mappings and analytical cases are not execution evidence. |

**Disposition:** published working input-contract proposal and review starting point inside 04. The 04 v0.5 body and earlier controlled source semantics remain preserved. Publication adds this explicit delta and navigation; it is not promotion to an integrated successor, downstream adoption or closure of H06. The prior §10 determination is dated to 24 September and remains part of the review history.


---

## 12. Recognition guide and practical bidirectional map — Working Proposal — 2 October 2026

A new [**04 A/B/C/D Recognition Guide and Example EA Interface Map v0.1 — Working Proposal**](./04_EA_ABCD_RECOGNITION_AND_INTERFACE_MAP_v0.1_WORKING_PROPOSAL.md) has been added as a candidate successor direction for 04. It does **not** replace the v0.5 baseline and is not a promotion decision.

The proposed purpose of 04 is now made explicit in two parts:

1. **Recognition guide:** operationalize the canonical 00M A/B/C/D semantics enough to classify real interface assertions without treating field names as epistemic categories.
2. **Practical input/output example:** retain O1–O6 / IF-S1–IF-S13 as one worked EA interface map, with every included assertion assigned a producer-relative role or explicitly left PROFILE-DEPENDENT / UNRESOLVED.

This proposal also records a candidate disposition for the earlier **H06 — exclusion of A** tension. The metadata-only route remains legitimate where it is sufficient, but a future 04 successor should not impose a universal exclusion of A. A declared profile may use either:

- `A + eligible B/C/D → EA`, or
- `A_ref + eligible B/C/D → EA`.

A metadata-only profile must not claim support for a use that requires the value of A, and A must not be relabelled as B to pass through the route. The historical H06 finding remains valid for the older input-only proposal until a successor is explicitly reviewed and promoted.

The new proposal deliberately leaves the current 176-row decomposition as source material rather than claiming it has been fully revalidated under 00M v0.8. Promotion requires family-by-family review and at least one end-to-end input/output worked profile.

Related mechanism-to-requirements traceability is recorded separately in [**00M-A01 — Mechanism-to-Requirements Traceability v0.1 — Working Proposal**](./00M_A01_MECHANISM_TO_REQUIREMENTS_TRACEABILITY_v0.1_WORKING_PROPOSAL.md). That document is a traceability aid only and does not change the canonical S1–S14 / T1–T4 / H1–H6 / KPI basis.


---

## Auditoría realizada por Codex — IF04-VNEXT-AUD-001

**Fecha:** 6 de octubre de 2026. **Fuente:** commit `1d24b7bfe88fa366e6c619fa88f6f7904d1380db`, VNext blob `8c970a1785df5150cf1b128656e498c815a64dac`; 04 v0.5 blob `2b563c102f62d029c6037b47b047e4ac21755e5b`; Recognition Guide blob `63ceba1e68fb500b9b4f32226b1a1b9622705add`; Input Contract blob `de6c58c62ad70b3182085333106b41b63a9fef18`. **Lectura:** VNext completo, Recognition Guide completo, 00M §1 y 00M-A01 completo; pasajes de EHD/result/freshness/ownership en el baseline. Input Contract recuperado como referencia: **no lectura/auditoría íntegra de las 176 filas ni de sus 44 casos**. Misma identidad Codex; no independencia externa ni tests ejecutados.

### Instrucciones de Iván y relaciones

IVAN-20261006-START-SEQUENTIAL-AUDITS autoriza la publicación secuencial de auditorías en la VNext existente. Requirements VNext fue revisado antes de este paso. No se adquiere autoridad para incorporar deltas al baseline. 04 debe preservar las obligaciones S/T/H sin importar semánticas de Theme; 05 y 05A son consumidores posteriores. El Recognition Guide propone el futuro sentido de 04, mientras el Input Contract permanece fuente histórica y starting point, no baseline promovido.

| Hallazgo | Evaluación y evidencia | Estado |
|---|---|---|
| IF04-R1-F001 | §11 excluye A de la ruta metadata-only; el kernel de 04 §2 exige operational result/closure y el baseline reconoce H06 abierto. §12 y Recognition Guide §4 proponen A o A_ref condicionado al perfil, sin declarar cierre. | Tensión real entre perfiles, explícitamente reconocida; no contradicción resuelta por una nota ni promoción tácita. |
| IF04-R1-F002 | Recognition Guide R0–R7 y 00M §1 distinguen producer/process/question/scope/capability/time. Un dato puede ser A de un productor y B para una pregunta distinta; el sentido no lo fija la dirección de transporte. | Correspondencia conceptual positiva; clasificación por familia y assertion sigue pendiente. |
| IF04-R1-F003 | §6 aún dice «If a future 00I ... is committed», aunque Requirements VNext y el router ya enlazan 00I v0.5. §3/§4 enlazan 00G/00H v0.1 mientras las rutas actuales usan v0.4/v0.5. | Desfase temporal de este registro, no ausencia del escenario. Preservar originales y proponer precisión de época. |
| IF04-R1-F004 | §2 enumera tres clarification candidates; la nueva lectura Requirements incluye CAND-R4 sobre binding check-to-use. §6 trata ventanas, pero dos timestamps no demuestran que ejecución consuma el estado requalificado. | Adjudicar CAND-R4 como obligación de perfil/consumidor/actuation owner; no sumar un field universal por reflejo. |
| IF04-R1-F005 | §12 y Recognition Guide §8 mantienen el mapa176 sin revalidación general bajo 00M v0.8; §9 exige familia a familia y un ejemplo end-to-end. | Gate abierto. Las 19 filas ilustrativas no sustituyen una auditoría de 176 assertions. |
| IF04-R1-F006 | No añadir O7/IF-S14 se sostiene como control de namespace, no como demostración de que toda futura interacción esté cubierta. 00M-A01 diferencia mecanismo plausible de cumplimiento S/T. | Mantener esa limitación junto a «no new family»; cualquier fallo real vuelve a Requirements/04 VNext. |

**Navegación de la fuente:** 13 enlaces locales a 11 rutas distintas, presentes en el árbol. No se certifica transporte equivalente, implementación ni capacidad real de consumidores.

### Conversación de auditoría

**Codex, respuesta a H06:** el disposition candidato del 2 de octubre es coherente con que A siga siendo fuente A, pero no basta para cerrar H06. Para un perfil A_ref debe existir un binding verificable a productor/perfil/versión/instancia, semántica de missing/stale y declaración de qué decisiones requieren el valor. Si el consumidor no puede recuperar o interpretar ese valor, una referencia sintáctica no equivale a result preservation. No se pide copiar todo A en todas las rutas ni fabricar B para eludir la exclusión histórica.

**Codex, respuesta a §6:** la separación qualification-validity/response-window es necesaria documentalmente y está apoyada por T2/T4. Su suficiencia operacional exige el puente al estado realmente consumido; se remite a CAND-R4 sin afirmar que un campo temporal prueba ese puente.

## Propuestas quirúrgicas — IF04-R1, pendientes

### IF04-R1-DELTA-001 — referencia temporal a 00I

**Objeto:** este VNext §6. **Hallazgo:** F003. **Fuente:** blob de la cabecera. **Tipo:** corrección documental propuesta, no aplicada. **Instrucción:** IVAN-20261006-START-SEQUENTIAL-AUDITS.

**TEXTO ANTES**

```markdown
DBC-C02 provides the applied-validation route for this distinction now. If a future 00I Semantic TOCTOU scenario is committed, it should be cited here as an additional scenario-level stressor only after its repository text is reviewed; it must not be presumed from a chat-only draft.
```

**TEXTO DESPUÉS**

```markdown
DBC-C02 provides an applied-validation route for this distinction. The committed [00I Semantic TOCTOU v0.5 Freeze Edition](./00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.5_FREEZE_EDITION.md) is an additional scenario-level stressor; its requirements and action-time binding candidates are recorded in the Requirements vNext review. Inclusion here does not certify the scenario's implementation, close H06 or promote this interface delta.
```

**Efecto:** actualizar procedencia temporal y mantener límites; no nuevo O/IF-S. **Dependencias:** 00I y Requirements VNext; los enlaces antiguos a 00G/00H deberán revisarse por separado antes de una edición. **Decisión:** pendiente. **Incorporación:** no ejecutada.

### IF04-R1-DELTA-002 — H06: candidato de lectura del elemento4 para un successor

**Objeto:** 04 v0.5 §2, único segmento del kernel EHD. **Hallazgo:** F001. **Tipo:** candidato semántico de perfil, no mera renumeración. **Estado:** pendiente de H06/end-to-end review y decisión de Iván; el baseline no se altera.

**TEXTO ANTES**

```text
(4) operational result/closure;
```

**TEXTO DESPUÉS**

```text
(4) operational result/closure, or a source-bound result reference only where the declared receiving profile can resolve and interpret the required result at the decision time; an unavailable, stale or insufficiently bound reference preserves material UNKNOWN and does not support uses that require the result value;
```

**Razón:** evitar universal exclusion of A sin fingir que A_ref vale para todos los usos. **Dependencias:** Recognition Guide §4/§9, Input Contract H06, F9, T2/T4/S14 y privacidad/authority owners. **Gate:** probar un perfil full-result y uno metadata-only con controles positivos, missing/stale/reference mismatch y límites de autorización; conservar revisión histórica. No se afirma que una implementación exista o pase. **Decisión de incorporación:** pendiente. **Incorporación:** no ejecutada.

### Cobertura restante

Auditoría documental parcial: 176-row revalidation, Appendix-A route conformance, adapter execution, costo/latencia, estados de salida de F1–F9 y evidencia externa quedan abiertos. No se promueve ningún successor de 04.
