# 05A Current-State vNext Review & Delta — FG-TIDA

> **Working current-state delta only — not a new ideal architecture.**  
> The dated reference remains [**05A — FG-TIDA Current-State Interface and Conformance Bridge v0.1**](./05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md), whose source snapshot is 19 September 2026.  
> The architectural target remains [**05 Ideal**](./05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_v0.4.part01.md) plus its [vNext ideal delta](./05_FG_TIDA_IDEAL_CROSS_THEME_INTERFACE_CONTRACTS_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md).  
> This file updates only the **reality mask**: what the public FG-TIDA record now supports, what remains candidate, what is test-only and what is not established.

| | |
|---|---|
| **ID** | 05A-vNext Review & Delta |
| **Version · date** | v0.1-draft · opened 24 September 2026 |
| **Status** | Cumulative current-state delta; incomplete by design; no change to the 19 September snapshot |
| **Current-state baseline** | 05A v0.1 — source snapshot 19 September 2026 |
| **Ideal source** | 05 v0.4 + 05 Ideal vNext Delta |
| **Generic source** | [04 General Interfaces](../../baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md) + [04 vNext Delta](../../baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_VNEXT_REVIEW_AND_DELTA_v0.1_DRAFT.md) |
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

## 3. Ideal-to-current delta table

| 05 Ideal item | Current 05A position as of 24 Sep 2026 | Reason |
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
| #22 attestation Theme capability | **Current source state**; #22→EA result profile **Candidate** | public Theme/WG scope exists; no common EA profile adopted |
| UC #9/#10 as semantic cases | **Current source state as cases**; interface consequences candidate | public use cases exist, mapping not reviewed |
| Theme #17 production rights case | **Current source state only to last public Theme #17 record** | later private correspondence does not change public Theme state |
| Future 00I Semantic TOCTOU scenario | **Not established / nonexistent in repo** | must not be assumed until committed and reviewed |

---

## 4. Current maximum 05A handoff after the refresh

The refresh does not justify a universal FG-TIDA schema.

The maximum defensible current pattern remains:

**source-native Theme/case result**  
→ **bounded adapter preserving issuer/scope/native result/qualification/UNKNOWN**  
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

### 6.2 Future 00I versus UC #6

No 00I file exists in the repository at this review point.

If a future 00I Semantic TOCTOU scenario is committed and reviewed:

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

This challenge floor does not promote DBC, EHD or any candidate field into adopted FG-TIDA semantics. It defines the minimum difficulty expected from a test that claims to exercise a material Ecosystem Awareness differential.

---

## 9. Current determination

As of the public record reviewed through **24 September 2026**:

1. 05A remains a **narrower current-state filter over 05 Ideal**, not a separate architecture.
2. #13's EA/lifecycle independence and bidirectional relation are substantially better supported than in the 19 September snapshot, while exact institutional packaging remains open.
3. Theme #16 now has a contributor/Theme-lead-approved bounded sequence for UC #6 → matrices → UC #4, but no frozen common runtime schema.
4. The human-review four-part profile, validity/response timing, #23↔#16 route and several Composition-Critical refinements remain **candidate** rather than adopted.
5. UC #7, UC #9 and UC #10 broaden the public semantic case portfolio without automatically creating common interface fields.
6. DBC, 00E–00H and 01I/ACC remain test/internal architecture sources unless independently supported by FG-TIDA public semantics.
7. Theme #11 and several other ideal 05 mappings remain **Not established** as EA interfaces today.
8. No universal FG-TIDA EHD, common schema, central controller or cross-Theme authority model is established.
9. Current-state realism does not lower the challenge floor: a meaningful EA test must still distinguish nominal continuity from material systemic divergence, preserve source dependence/UNKNOWN, support targeted requalification and permit strong native controls to falsify an EA differential claim.

This delta remains open and cumulative. Future public FG-TIDA changes should update this **current-state mask** rather than modifying 05 Ideal to look artificially current.
