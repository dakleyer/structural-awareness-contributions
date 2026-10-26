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
> **VNext · auditoría acumulativa R1 · 6 de octubre de 2026.** Se preserva el filtro histórico completo. Las comprobaciones públicas de esta pasada se limitan a anchors nombrados en la auditoría final; no actualizan en bloque todos los estados de FG-TIDA. No se modifica el bridge de 19 de septiembre. [Procedimiento](../../../../governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md) · [visión general](../../../../architectural-contributions/ecosystem-positioning/README_VNext.md).

# 05A Current-State vNext Review & Delta — FG-TIDA

> **Working current-state delta only — not a new ideal architecture.**  
> The dated reference remains [**05A — FG-TIDA Current-State Interface and Conformance Bridge v0.1**](./05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md), whose source snapshot is 19 September 2026.  
> The architectural target remains [**05 Ideal**](./05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md) plus its [vNext ideal delta](./05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md).  
> This file updates only the **reality mask**: what the public FG-TIDA record now supports, what remains candidate, what is test-only and what is not established.
>
> **Architecture-side semantic refresh — 2 October 2026.** [00M v0.8](../../baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) and the [04 A/B/C/D Recognition & Interface Map Working Proposal](../../baseline/04_EA_ABCD_RECOGNITION_AND_INTERFACE_MAP_v0.1_WORKING_PROPOSAL.md), as recorded in [04-vNext](../../baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md), refine how EA-side adapters may interpret source results. They do **not** by themselves upgrade any FG-TIDA relation to Current source state. Public Theme semantics and architecture-side A/B/C/D interpretation remain separate evidence layers.

| | |
|---|---|
| **ID** | 05A-vNext Review & Delta |
| **Version · date** | v0.1-draft · opened 24 September 2026 · current-state refresh through 2 October 2026 |
| **Status** | Cumulative current-state delta; incomplete by design; no change to the 19 September snapshot |
| **Current-state baseline** | 05A v0.1 — source snapshot 19 September 2026 |
| **Ideal source** | 05 v0.4 + 05 Ideal vNext Delta |
| **Generic source** | [00M v0.8 semantic source](../../baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md) + [04 General Interfaces](../../baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md) + [04 vNext Delta](../../baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) + [04 recognition/interface-map Working Proposal](../../baseline/04_EA_ABCD_RECOGNITION_AND_INTERFACE_MAP_v0.1_WORKING_PROPOSAL.md) — the Working Proposal is architecture-side candidate guidance, not FG source evidence |
| **Review rule** | An ideal 05 relation enters 05A only to the extent supported by public FG-TIDA evidence; no internal EA/DBC/ACC artefact can promote a relation by itself |

---

## 1. Function of 05A

05A answers one question only:

> **Given the current public FG-TIDA record, how much of the 05 ideal architecture can be defended today, and at what maturity/status?**

It does not redesign 05.

The status vocabulary remains:

- **Current source state** — publicly described source-native distinction/result that can be preserved;
- **Candidate cross-Theme field** — architecturally useful and source-linked, but not an agreed common handoff;
- **Test-only evidence** — useful for conformance/fixture evaluation, not a runtime requirement by default;
- **Not established** — the ideal relation lacks sufficient public support and must remain UNKNOWN/not assumed.

The gap **05 Ideal − 05A Current-State** is a useful maturity map. It identifies where the Focus Group still needs semantic-owner agreement, explicit interface text, implementation, test evidence or institutional packaging.

---

## 2. Source refresh since the 19 September snapshot

### 2.1 Theme #13 — placement and independent mechanisms

Public source now supports a stronger reading than the original 05A snapshot:

- Ward Duchamps placed Ecosystem Awareness within Theme #13 and described the systemic-capacity/handoff interface as potentially foundational.
- Ward supported defining the determinacy envelope and signal lifecycle independently so each can be tested and can interoperate.
- Nelson Trasatti confirmed that the incident lifecycle remains a complete mechanism, EA remains independently testable, targeted refinement is testable, and the #13 four-field envelope can be consumed as a versioned profile of a more general EHD without the testbed owning EHD.

Anchors:

- https://github.com/FG-TIDA/themes/issues/13#issuecomment-5571476256
- https://github.com/FG-TIDA/themes/issues/13#issuecomment-5639226397
- https://github.com/FG-TIDA/themes/issues/13#issuecomment-5640186655

**05A delta disposition:**

- **EA placement within #13:** **Current source state** at contributor/Theme-proposer level; not an FG-wide structural decision.
- **Independent incident lifecycle and EA mechanisms:** **Current source state** as a supported working architecture.
- **Formal institutional label “peer mechanisms” / exact WG packaging:** **Not established** as an FG decision.
- **#13 profile of general EHD:** **Candidate cross-Theme field/profile**, supported by Nelson from the testbed side; general EHD ownership remains outside #13.

### 2.2 Theme #13 — risk/response-window / epistemic-opportunity work

Oleksii Voshchak's v0.2 matrix now separates:

- semantic / qualification validity window;
- epistemic state;
- epistemic opportunity;
- multidimensional operational state;
- threshold conditions;
- authorized decision layer;
- incident lifecycle;
- revalidation.

It also separates qualification validity timing from operational response timing.

Anchor:
https://github.com/FG-TIDA/themes/issues/13#issuecomment-5783505043

**05A delta disposition:**

- existence of the matrix and its distinctions: **Current source state** as a contributor discussion artefact;
- a common #13/EA runtime schema based on those fields: **Candidate cross-Theme field**;
- universal score / mandatory computability model: **Not established**.

### 2.3 Theme #16 — UC #6 → matrices → UC #4 sequence

The public discussion advanced materially after the original snapshot.

Current agreed contributor-level sequence:

**UC #6 semantic source**  
→ **current v0.2 matrices annotate bounded Theme #16 interfaces**  
→ **UC #4 derives executable mapping / fixtures / traces**  
→ **case and matrix owners review before freeze**

Anchors:

- Nelson: https://github.com/FG-TIDA/themes/issues/16#issuecomment-5803023066
- Arpita: https://github.com/FG-TIDA/themes/issues/16#issuecomment-5803653565
- Olena: https://github.com/FG-TIDA/themes/issues/16#issuecomment-5804125734
- Lei: https://github.com/FG-TIDA/themes/issues/16#issuecomment-5809248877

Lei explicitly stated that the sequencing/scope work from the Theme #16 side and said to proceed on that basis.

**05A delta disposition:**

- the bounded sequencing itself: **Current source state** at Theme-lead/contributor working level;
- UC #6 facts/expected outcomes as semantic source: **Current source state**;
- matrices as bounded annotation layer: **Current source state** for the reviewed working matrices;
- UC #4 executable mapping: **Candidate/Test-only** until the mapping is produced and reviewed;
- any frozen common #16↔EA runtime schema: **Not established**.

### 2.4 Human-review output qualification

Olha Borysenko publicly accepted a four-part reading:

- human decision/result;
- confidence/assurance in the received review event;
- capacity binding/qualification;
- residual/inherited indeterminacy,

with assurance explicitly bounded to evidentiary status of the review event, not human competence.

The broader Theme #16 structure retains authority applicability separately from operational capacity and execution confirmation separately from human decision.

**05A delta disposition:**

- separation of authority applicability / capacity / decision / execution: **Current source state** in the Theme #16 discussion;
- four-part human-review EHD-style profile: **Candidate cross-Theme field/profile**; useful and contributor-supported, but not a frozen common Theme contract.

### 2.5 Theme #23 ↔ Theme #16 privilege / human-oversight boundary

Lei proposed a bounded interface:

privilege/authorization event + current privilege state + context/risk + required human review  
→ #16 trigger/intervention/human decision  
→ back to #23 for privilege enforcement/lifecycle transition.

Ying Wang confirmed that #23 remains a complete privilege-lifecycle framework and #16 can remain an independent implementation path.

Anchors:

- https://github.com/FG-TIDA/themes/issues/23#issuecomment-5700157082
- https://github.com/FG-TIDA/themes/issues/23#issuecomment-5707764621

**05A delta disposition:**

- #23 and #16 remain independently owned: **Current source state**;
- bounded #23↔#16 interface: **Candidate cross-Theme field/route**;
- #23↔EA common profile: **Not established**.

### 2.6 Theme #11 Model-level Trust Foundations

Theme #11 has been updated and is open for comments, but the public record reviewed here does not establish an EA-specific handoff or common cross-Theme interface.

**05A delta disposition:** **Not established** for a #11↔EA profile. The ideal 05 mapping remains an ideal target only.

### 2.7 Use Case #7 — identity / execution / action-time state

UC #7 was published after the 19 September 05A snapshot and is directly relevant to the current interface boundary.

It distinguishes:

- persistent/logical agent identity from a particular execution;
- action-time material state from later/current state;
- continuity assertions from mere shared model/runtime/checkpoint similarity;
- request/acceptance/completed effect as separate records;
- current authorization from earlier approval; and
- supported continuity from unresolved or missing evidence.

**05A delta disposition:**

- UC #7 case facts and expected findings: **Current source state** as a public use case;
- identity / execution / action-time-state distinction: **Current source state** as case semantics;
- a common cross-Theme identity-state handoff/profile: **Candidate cross-Theme field/profile**;
- any claim that persistent identity proves current authority or state continuity: **Not established / prohibited inference**.

### 2.8 Theme #6, verifier-side Theme #7, and Theme #22 — source semantics versus EA mapping

The public record now supports a more precise distinction than the original 05A row that grouped #6/#22 together.

**Theme #6** publicly maintains source-native action/verdict semantics with scope, attribution/issuer and versioned reference semantics; its contributors have also explicitly stated that #6 does not own the cross-scope/systemic conclusion.

- #6 source-native verdict/reference semantics: **Current source state**;
- #6 → EA bounded adapter/profile: **Candidate cross-Theme field/profile**;
- EA rewriting a #6 verdict into a systemic state: **Not established / prohibited semantic translation**.

**Theme #7** explicitly proposes verifier-side obligations and deterministic negative vectors around identifier control, freshness/replay, authorization scope and attestation appraisal.

- verifier-side failure/check semantics as a public contribution: **Current source state**;
- a common #7 → EA runtime handoff: **Candidate / Not established** depending on the field;
- negative vectors used in an EA/FG-TIDA conformance profile: **Test-only** until reviewed in that route.

**Theme #22** publicly defines Remote Attestation for Agentic AI as a separate Theme/WG concerned with what/how/when to attest.

- Theme #22 attestation function/scope: **Current source state**;
- a common #22 → EA attestation-result profile: **Candidate cross-Theme field/profile**;
- any inference that attestation alone establishes systemic sufficiency: **Not established**.

### 2.9 New public use cases #9 and #10

Two new public cases materially expand test pressure:

- **UC #9** — national payment rail: authority provenance, act-time applicability, limits, composition, revocation and identity-anchor integrity;
- **UC #10** — self-expanding multi-agent molecular design: capability without conferral, agent recruitment, persistent identity versus authority continuity and missing grant.

**05A delta disposition:**

- existence and facts of the cases: **Current source state** as public use-case material;
- any new common interface field implied by them: **Not established** until mapped/reviewed by relevant semantic owners;
- use as fixture/test pressure: **Test-only / candidate mapping**.

---


### 2.10 Theme #21 — population evaluation versus EA qualification

The public Theme #21 discussion now supplies a much sharper boundary for the IF-S9 / EA relation.

Justin Philip Flores, the Theme proposer, states the distinction by **question answered**, not by authority:

> #21 establishes what a population of observations supports; EA establishes whether that is sufficient for a particular decision in its context.

He also constrains the return direction. EA may report that a population result is insufficient for its receiving decision and may name the gap. The rate producer should not receive the receiver's desired target hypothesis, decision purpose or receiver-set budget as measurement direction.

Anchor:
https://github.com/FG-TIDA/themes/issues/21#issuecomment-5903046577

The same public thread also establishes several source-native Theme #21 details:

- per-evaluator results are the default;
- pooling is a separate step that carries its assumption;
- a pooled result should identify the pooling assumption as **established, declared or unknown**;
- **unknown is not independence**;
- matching aggregate rates do not establish evaluator agreement: in the released scoring, GPT-5 mini and Sonnet produced 19.7% and 19.8% rates while their flagged sets overlapped only 63%;
- that released scoring had no ground truth, so it cannot establish agreement = correctness or shared correctness.

Anchor:
https://github.com/FG-TIDA/themes/issues/21#issuecomment-5903881738

The proposer later reaffirmed that re-evaluating eligibility after complaint, drift or recall is downstream action on a finding and belongs with #13/#16; Theme #21 stops at what the population supports.

Anchor:
https://github.com/FG-TIDA/themes/issues/21#issuecomment-5925445690

Nelson's proposed first executable slice remains a **planned test**, not a result: nine items, frozen reference/taxonomy version, planted-judge changes, detection rule, expected-versus-observed fields and evaluator-dependence assumptions; the detection procedure should not receive the answer key.

Anchor:
https://github.com/FG-TIDA/themes/issues/21#issuecomment-5936600434

**05A delta disposition:**

- **#21 question boundary — what the population supports:** **Current source state** at Theme-proposer level.
- **Per-evaluator default; pooling assumption state established/declared/unknown; unknown ≠ independence:** **Current source state**.
- **EA may return insufficiency + named qualification/coverage gap:** **Current source boundary** from the #21 side; the exact cross-Theme adapter remains **Candidate** until jointly reviewed/adopted.
- **Receiver decision purpose / desired hypothesis / receiver-set budget sent upstream as measurement direction:** **Not established / explicitly rejected by the Theme proposer** for this interface.
- **Released matched-rate/item-disagreement analysis:** **Current public empirical evidence about Theme #21 measurement behaviour**, with the stated no-ground-truth limitation.
- **Nine-item planted-judge demonstration:** **Test-only / planned**, not executed evidence at this review point.
- **00M A/B/C/D interpretation of #21 results:** **architecture-side candidate mapping only**. Under that mapping a population finding can be A(IF-S9), its established population/taxonomy/dependence/statistical/identifiability basis can be B(IF-S9), and C/D require the 00M frontier/barrier conditions. This notation is not attributed to Theme #21 itself.

This creates a defensible current-state boundary without collapsing the two layers: Theme #21 owns the population measurement semantics; EA remains the downstream decision-scoped qualification/composition function.


## 3. Ideal-to-current delta table

| 05 Ideal item | Current 05A position as of 2 Oct 2026 | Reason |
|---|---|---|
| #13 Incident/Signal Lifecycle ↔ EA as independently testable mechanisms | **Current source state** for independence/bidirectional working boundary; institutional packaging not established | Ward + Nelson public support |
| General EHD with #13 profile | **Candidate cross-Theme profile** | Nelson supports profile reading; no FG-wide common EHD adoption |
| #16 bounded authority/capacity/decision/execution separation | **Current source state** | v0.2 matrices + Lei/Olena/Olha discussion |
| UC #6 → matrices → UC #4 executable sequence | **Current source state** for sequence; executable mapping **Test-only/Candidate** | Lei approved sequencing; mapping not yet frozen/executed |
| Human review result + assurance + capacity + residual | **Candidate profile** | contributor support, not frozen common Theme schema |
| Qualification-validity window ≠ response window | **Current source distinction / Candidate interface representation** | Oleksii v0.2 + related #13 discussion |
| CAND-R1 effective-role drift | **Candidate/Test-only** | public cases/themes support the problem; no common interface field |
| CAND-R2 opportunity ≠ admissibility ≠ authority ≠ execution | **Candidate/Test-only** | multiple public cases, but no common FG runtime contract |
| CAND-R3 per-action ≠ aggregate authorization | **Test-only/Candidate** | 00H is internal; UC #9 gives related public authority-limit pressure, not an agreed common field |
| Aggregate/cumulative action-history Composition-Critical relation | **Candidate/Test-only** | no FG-wide profile agreement |
| DBC C01–C12 | **Test-only** | programme-internal test vocabulary; not FG runtime ontology |
| 00E–00H | **Test-only / informative stress scenarios** | internal EA scenarios, not Theme-owned cases |
| 01I / ACC participation profile | **Not established as FG-TIDA profile** | internal corpus profile only |
| #23↔#16 bounded privilege/oversight route | **Candidate cross-Theme route** | public contributor discussion |
| #11 model-level EA profile | **Not established** | Theme exists/updated; EA mapping not publicly agreed |
| UC #7 identity/execution/action-time-state case | **Current source state as case semantics**; common handoff candidate | public use case exists; no common cross-Theme profile frozen |
| #6 source-native verdict/reference semantics | **Current source state**; #6→EA adapter **Candidate** | public Theme discussion preserves local semantics and rejects cross-scope ownership |
| #7 verifier-side obligations / negative vectors | **Current source state as contribution**; EA mapping **Candidate/Test-only** | public verifier proposal exists; no common EA handoff adopted |
| #21 population-evaluation boundary | **Current source state** for population-support question, per-evaluator default and pooling-assumption discipline; #21↔EA adapter **Candidate** | Theme proposer explicitly separates population support from downstream decision sufficiency and limits the EA→measurement return direction |
| #22 attestation Theme capability | **Current source state**; #22→EA result profile **Candidate** | public Theme/WG scope exists; no common EA profile adopted |
| UC #9/#10 as semantic cases | **Current source state as cases**; interface consequences candidate | public use cases exist, mapping not reviewed |
| Theme #17 production rights case | **Current source state only to last public Theme #17 record** | later private correspondence does not change public Theme state |
| 00I Semantic TOCTOU scenario | **Test-only / internal architecture source** | now exists in the EA corpus; it does not upgrade FG-TIDA current-state semantics without independent public support |

---

## 4. Current maximum 05A handoff after the refresh

The refresh does not justify a universal FG-TIDA schema.

The maximum defensible current pattern remains:

**source-native Theme/case result A(source), or A_ref where a reviewed metadata-only profile is sufficient**  
→ **bounded adapter preserving issuer/scope/native result binding/qualification/UNKNOWN**  
→ **conditional decision-material qualifiers where supplied and source-owned**  
→ **EA decision-scoped qualification**  
→ **bounded return/requalification request**  
→ **action remains with the legitimate external owner**

The refresh strengthens several conditional qualifiers and mappings but does not change the universal kernel.

Where material, current candidate profiles may now additionally preserve:

- qualification-validity/review condition separately from response deadline;
- human-review event assurance separately from capacity;
- current authority applicability separately from historical grant;
- execution confirmation separately from decision;
- targeted re-entry;
- source-dependence / independent-corroboration basis;
- aggregate/cumulative lineage only where the authority model makes the composed effect material.

None of these becomes mandatory for every Theme producer.

The architecture-side 00M/04-vNext classification may be used in candidate/test mappings to explain which source assertion is A/B/C/D, but it does not replace the Theme's own vocabulary or promote a current-state interface. If the source result is needed, a current test profile must carry A; if only a stable binding plus qualifiers is sufficient, it may test an A_ref route. The profile must state which case applies.

---

## 5. Current UC #4 / UC #6 executable route

The most mature near-term current-state execution path is now:

**UC #6 facts / expected outcomes**  
→ **Theme #16 v0.2 annotations**  
→ **draft bounded cross-interface / UC #4 profile**  
→ **semantic-owner review**  
→ **version-pinned adapter / fixture / expected-outcome freeze**  
→ **UC #4 executable traces / report**

The executable profile should preserve:

- authority determination received;
- available intervention options;
- human decision;
- separate execution/continuation outcome;
- any applicable assurance/capacity/residual qualifiers;
- re-entry/revalidation condition.

Human-input authenticity and oversight capacity remain fixed where UC #6 freezes them; the executable mapping must not introduce a capacity-failure scenario or new confidence score into that case.

This is a **test/conformance route**, not a new lifecycle owner.

---

## 6. Route-separation reservations

### 6.1 00H versus public FG-TIDA cases

00H remains an internal EA/DBC narrative/quality-gate scenario. It may inform authority/opportunity/aggregate-action testing, but it does not become a stage of UC #6, UC #9 or UC #4.

### 6.2 00I versus UC #6

00I now exists in the repository as an internal EA Semantic TOCTOU reference scenario. Its existence does not make it public FG-TIDA source evidence.

When 00I is used in this review route:

- UC #6 remains the public FG-TIDA semantic source for changed-purpose/current-applicability;
- 00I remains an EA/DBC reference failure scenario;
- UC #4 remains the executable mapping layer after semantic-owner review.

They may share boundary questions or fixtures, but are parallel provenance routes, not sequential stages.

---

## 7. Admission / promotion rule for 05A-vNext

An ideal 05 relation may be promoted within 05A only when the public record supports the promotion.

Minimum record:

1. public source anchor;
2. semantic owner / contributor role;
3. exact source-native state or distinction;
4. producer and receiver;
5. scope and validity conditions;
6. whether the relation is runtime, candidate or test-only;
7. explicit UNKNOWN / not-established handling;
8. review status;
9. fixture/evidence status where a test claim is made.

A test result can strengthen evidence for a **candidate profile** but cannot by itself turn an unsupported Theme semantic into **Current source state**.

Private email, internal EA documents and ideal 05 mappings may inform questions, but they do not upgrade 05A status unless the relevant content becomes public FG-TIDA evidence or is otherwise accepted through the appropriate source-owner process.

---

## 8. Challenge floor — realistic does not mean weak

05A narrows **claims of present support**, not the difficulty of the tests.

A current-state profile may test candidate fields or profiles without pretending that they are adopted runtime semantics. To remain meaningful for Ecosystem Awareness, the near-term route should include at least the following challenge classes once their semantic mappings are reviewed:

1. **Nominal continuity control** — when nothing material changes, EA instrumentation must not create unnecessary HOLD, escalation, containment or requalification.
2. **Local-equivalence / systemic-divergence pair** — hold the relevant local/native result constant while changing a material ecosystem qualifier such as source independence, inherited indeterminacy, validity or capacity. The systemic qualification should change only when the changed qualifier is decision-material.
3. **Targeted requalification** — when one specific basis becomes stale or insufficient, the route should refresh/re-enter at that basis rather than restart or expand the whole context indiscriminately.
4. **Source-dependence control** — nominally multiple corroborators sharing one material upstream source must not be counted as independent corroboration.
5. **Decision / execution separation** — a decision or agent assertion must not be treated as externally confirmed outcome when that confirmation is material and available.
6. **Independent interoperability** — at least one admitted route should eventually cross independently implemented or independently governed producer/consumer boundaries without requiring shared internal EA logic.

Where a comparative claim is made, a **strong native/control configuration** should be allowed to reproduce the same behaviour. If it does so at equal or lower burden, that result counts against an EA differential claim rather than being explained away.

**Evidence ceiling:** a deterministic fixture or two-domain exchange can establish bounded semantics, adapter behaviour and interoperability. It does **not** by itself establish ecosystem behaviour. A stronger ecosystem-level claim requires a later multi-participant / multi-observer route with independently governed participants and material partial, conflicting or source-dependent observations. Non-adversarial agentic failure should be established before adding deliberate attack classes so the test can distinguish endogenous composition failure from hostile behaviour.

This challenge floor does not promote DBC, EHD or any candidate field into adopted FG-TIDA semantics. It defines the minimum difficulty expected from a test that claims to exercise a material Ecosystem Awareness differential.

---

## 9. Current determination

As of the public record reviewed through **2 October 2026**:

1. 05A remains a **narrower current-state filter over 05 Ideal**, not a separate architecture.
2. #13's EA/lifecycle independence and bidirectional relation are substantially better supported than in the 19 September snapshot, while exact institutional packaging remains open.
3. Theme #16 now has a contributor/Theme-lead-approved bounded sequence for UC #6 → matrices → UC #4, but no frozen common runtime schema.
4. The human-review four-part profile, validity/response timing, #23↔#16 route and several Composition-Critical refinements remain **candidate** rather than adopted.
5. UC #7, UC #9 and UC #10 broaden the public semantic case portfolio without automatically creating common interface fields.
6. DBC, 00E–00I and 01I/ACC remain test/internal architecture sources unless independently supported by FG-TIDA public semantics.
7. Theme #11 and several other ideal 05 mappings remain **Not established** as EA interfaces today.
8. No universal FG-TIDA EHD, common schema, central controller or cross-Theme authority model is established.
9. Current-state realism does not lower the challenge floor: a meaningful EA test must still distinguish nominal continuity from material systemic divergence, preserve source dependence/UNKNOWN, support targeted requalification and permit strong native controls to falsify an EA differential claim.
10. Theme #21 now has a clearer source-owned boundary: population measurement states what the population supports; downstream EA may report insufficiency and a qualification gap, but the receiver's desired hypothesis, decision purpose or receiver-set budget does not become measurement direction through this interface.
11. 00M/04-vNext sharpen the EA-side interpretation of source results and permit profile-declared A versus A_ref routes, but they do not by themselves establish FG-TIDA adoption of A/B/C/D or any common runtime schema.

This delta remains open and cumulative. Future public FG-TIDA changes should update this **current-state mask** rather than modifying 05 Ideal to look artificially current.


---

## Auditoría realizada por Codex — IF05A-VNEXT-AUD-001

**Fecha:** 6 de octubre de 2026. **Fuente interna:** commit `1d24b7bfe88fa366e6c619fa88f6f7904d1380db`, VNext blob `751f74e7cd64a92286b936d7aeff704fbafc9be9`; bridge histórico consultado para status/consultation/E4 rules. **Lectura:** VNext completo y contraste con 05 Ideal/04 VNext revisados en los pasos anteriores. **Auditor:** mismo Codex, sin independencia externa. No ejecución de adapters ni reproducción de datasets.

### Instrucción y visión del filtro

IVAN-20261006-START-SEQUENTIAL-AUDITS autoriza publicar auditorías de una en una en los espacios existentes. 05A aplica una máscara de evidencia a 05; no deriva realidad de una relación técnicamente expresable. «Current source state» significa distinción publicada en un nivel de autor/contributor determinado, no adopción institucional ni capacidad ejecutada. El bridge histórico califica esos anchors como E4 working-source evidence; esta auditoría respeta ese techo.

### Hallazgos y evidencia

| ID | Observación / evaluación | Disposición |
|---|---|---|
| IF05A-R1-F001 | §2.1 distingue formal peer/WG packaging no establecido de working independence y candidate EHD. Las fuentes13 verificadas mantienen esa reserva; 05 Ideal necesita la precisión recogida por IF05-R1-F003. | Consistencia favorable del filtro; evitar elevar la tabla de ideal a Current. |
| IF05A-R1-F002 | §2.3/§5 mantienen sequence approval separado de mapping/fixtures/traces. Los comentarios de Lei/Arpita/Olena/Nelson respaldan exactamente ese alcance. | Aprobación de trabajo, no de resultado; conservar facts fixed y review antes de freeze. |
| IF05A-R1-F003 | La matriz13 comentada por avoschak-ai el22 Sep separa validity/response y assertion/attempt/confirmed outcome; se anuncian pruebas como siguiente paso. #23 describe independientes los scopes; Lei propone una interfaz, Ying no confirma ese payload específico. | Current distinción discutida; common schema o contrato23↔16 permanece candidate. No inferir aceptación del payload de la sola ausencia de oposición. |
| IF05A-R1-F004 | Comentarios21 de30 Sep/1 Oct respaldan per-evaluator default, pooling assumption, target-feedback boundary y planned nine-item demonstration. El reporte de tasas 19.7/19.8/63% es cálculo informado por contributor con no-ground-truth y honest-judges limits. | Fuente pública verificada; cifras no reproducidas aquí. No establece detector de dishonest evaluator ni correctness ni eficaciaEA. |
| IF05A-R1-F005 | §2.4 y partes de§2.6–2.9 atribuyen Current a perfiles/casos sin anchor en cada subapartado de este expediente. Puede haber soporte en otras fuentes del corpus, pero este registro no permite reconstruir por sí solo cada promotion. | Trazabilidad pendiente para esas filas; no invalidación automática del original ni renovación de todo Current al6 Oct. |
| IF05A-R1-F006 | El mínimo§7 pide anchor/role/state/producer/receiver/scope/status/review/test; falta hacer explícita una fecha de consulta y revisión identificable de la fuente mutable. El bridge histórico sí advertía esa necesidad. | Propuesta de completar la ficha de fuente de revisión, sin añadir campos a payloadsFG. |
| IF05A-R1-F007 | 00M y A_ref son interpretation candidates; §4 ya impide promotionFG por un documentoEA. H06 y review176 permanecen abiertas en04. | Correspondencia positiva; ninguna actualización05A suple consumer test o source owner review. |
| IF05A-R1-F008 | La tabla distingue I como internal source, mientras la fila agrupada todavía usa E–H y el determination E–I. El router actual incluye J. | Cobertura temporal no uniforme; antes de ampliar rows, clasificarJ como internal/test, no CurrentFG por existencia. |

### Fuentes públicas de esta pasada

Se reusan los ocho anchors verificables registrados en IF05-VNEXT-AUD-001 y se añaden:

| Fuente | Autor / fecha UTC | Comprobación de esta pasada |
|---|---|---|
| [13/5783505043](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5783505043) | avoschak-ai,22 Sep2026 | Texto anuncia matrixv0.2 y las distinciones; attachment DOCX no auditado íntegramente aquí. |
| [23/5700157082](https://github.com/FG-TIDA/themes/issues/23#issuecomment-5700157082) | leigao-research,16 Sep2026 | Interfaz posible propuesta por Lei, no contrato ejecutado. |
| [23/5707764621](https://github.com/FG-TIDA/themes/issues/23#issuecomment-5707764621) | Snoopywy/Ying,17 Sep2026 | Independencia de Themes; no aceptación literal de todos los campos propuestos. |
| [21/5903881738](https://github.com/FG-TIDA/themes/issues/21#issuecomment-5903881738) | GospelNerd,30 Sep2026 | Autor reporta tasas19.7/19.8, union198 y73 flags exclusivos; 125/198≈63.13% es coherente aritméticamente con el63% reportado. Dataset/código no reproducidos aquí. |
| [21/5925445690](https://github.com/FG-TIDA/themes/issues/21#issuecomment-5925445690) | GospelNerd,1 Oct2026 | Nine items deberán informar counts, no tasas por-label; eligibility decision downstream13/16. |
| [21/5936600434](https://github.com/FG-TIDA/themes/issues/21#issuecomment-5936600434) | T-n-Nelson,1 Oct2026 | Pide specification como siguiente input y detector sin answer key; sigue planned. |

Ninguna de estas consultas demuestra que no existan cambios posteriores en otros comentarios. No se certifica Current para todas las filas al6 Oct; se certifica lectura de estos anchors y su scope. No se consultó ni publicó correspondencia privada.

**Navegación interna:** 10 enlaces locales a 7 destinos, presentes en el árbol. Para un cierre completo faltan anchors porfila, documentos/attachments nativos, todos los Cases7/9/10 y owner reviews.

### Conversación de auditoría

**Codex, respuesta a «Current public empirical evidence»:** conservar que hay un reporte público de medición y no-ground-truth; explicitar que este auditor comprobó el reporte, no el dataset. La evidencia de existencia del comentario y la evidencia de que el cálculo es reproducible son objetos distintos. Una reproducción futura debe registrar commit/datasetSHA/método y no sobrescribir el relato anterior.

**Codex, respuesta a la máscara Current:** una consulta selectiva6Oct no renueva en bloque un snapshot2Oct. Cada relation debe tener su propia fecha/owner/status; una proposal source publica puede acreditar la propuesta sin acreditar el contrato.

## Propuestas quirúrgicas — IF05A-R1, pendientes

### IF05A-R1-DELTA-001 — precisión de la evidencia numérica

**Objeto:** este VNext§2.10. **Hallazgo:** F004. **Preparación:** IVAN-20261006-START-SEQUENTIAL-AUDITS. **Tipo:** precisión de evidencia/atribución; no cambio de datos ni source Theme21.

**TEXTO ANTES**

```markdown
- **Released matched-rate/item-disagreement analysis:** **Current public empirical evidence about Theme #21 measurement behaviour**, with the stated no-ground-truth limitation.
```

**TEXTO DESPUÉS**

```markdown
- **Released matched-rate/item-disagreement analysis:** **Contributor-reported public analysis of Theme #21 measurement behaviour**, with the stated no-ground-truth and honest-judges limitations. Source consultation establishes the public report; independent reproduction of its data and code must be recorded separately and is not implied by this status.
```

**Efecto:** evitar que consulta se lea como reproducción independiente. **Dependencias:** evidence grades/E4 y futuro conformance test21. **Decisión de Iván:** pendiente. **Incorporación:** no ejecutada.

### IF05A-R1-DELTA-002 — fecha/revisión de fuente en la ficha de promoción

**Objeto:** este VNext§7, único item1. **Hallazgo:** F006. **Tipo:** control del expediente de revisión; no payload comúnFG.

**TEXTO ANTES**

```text
1. public source anchor;
```

**TEXTO DESPUÉS**

```text
1. public source anchor, consultation date/time and source revision identifier or content hash where available, with the exact source-native statement and scope relied upon;
```

**Razón:** mantener la vigencia reconstruible de comentarios editables. **Gate:** no inventar revisionId si proveedor no lo expone; registrar limitación y created/updated como metadatos, no como prueba absoluta de inmutabilidad. **Decisión:** pendiente. **Incorporación:** no ejecutada.

### Cobertura restante

Auditoría de primera pasada; varias rowsCurrent sin reconstrucción completa y attachments/datasets pendientes. No promoción del bridge, universal schema, adoption ni eficacia deEA.
