# CU-HIB-01 — Context Change, Privilege Restoration and Ecosystem-Awareness Specifications
## Self-contained third-party challenge dossier · DDS Stage A · R1 → R2 → R3

**Working ID:** DDS-A-CU-PLM-EA-01 / CU-HIB-01  
**Version and source-review cutoff:** v0.3 — 14 October 2026, including the latest [Ying Wang response of 09:49:50 UTC](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6165603429).  
**Local research preparation:** Iván Abril Palma / The Integral Management Society.  
**External source owners:** Ying Wang and Ye Tao (China Unicom) for [FG-TIDA Theme #23](https://github.com/FG-TIDA/themes/issues/23); other contributors retain their respective proposal ownership.  
**Intended readers:** FG-TIDA contributors; authorization/privilege-lifecycle designers; security architects; ecosystem-awareness researchers; potential testbed and independent evaluators.  
**Status:** PUBLIC WORKING CHALLENGE **FOR REVIEW**, not an FG-TIDA or China Unicom endorsed/accepted specification, joint experiment, frozen preregistration, scored run or ITU-T Recommendation.

> **The central question is not whether Ecosystem Awareness (EA) “wins”.** It is whether **a material contextual change can invalidate, qualify or make insufficient the basis on which a previously legitimate privilege-restoration decision would be made**, and which **testable, owner-preserving specifications** are needed to make the change, its evidential limits and its authorized consequences explicit. A good existing authorization system may already meet every candidate requirement. That would be an informative, acceptable result.

This document is **autocontenido/self-contained** in the substantive sense: it states the original questions and responses, defines the Challenge, names all experimental axes, gives the complete R1/R2/R3 design, proposes testable requirements, identifies evaluators and evidence boundaries, and links to primary sources and supporting material. Readers do not need to infer methodology from another document. Linked sources remain authoritative for their own semantics.

---

## 1. Executive account: the problem and the outcome sought

An AI incident-response agent has a legitimately granted, limited privilege to **isolate resource R**. During hibernation the privilege is suspended. **Service S, already critical before hibernation, becomes dependent on R while the agent sleeps**. The grant identity, principal, original privilege reference and named policy version may remain unchanged. Nevertheless, isolation of R can now interrupt S.

At reactivation, checking a still-valid identity, credentials or the historical authorization is **insufficient** to answer whether the *same action* remains permissible **in the current operating situation**. This is a contextual-applicability problem, not necessarily a compromised credential, forged identity or changed policy text. It is closely aligned with [Ying's response](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6164646309).

The decisive difference from an ordinary authorization demonstration is the **temporal challenge**:

1. An authorized decision is valid in a defined operating context.
2. Competent safeguards are added or shown to work and are frozen.
3. A source-grounded material change occurs in a different governance domain.
4. The *same* requested privilege must be re-evaluated on its **current** meaning and effect, with explicit information and authority limits.
5. Legitimate continuation, targeted withholding, reauthorization and recovery all remain possible outcomes, depending on evidence and source-owned policy. An indefinite global halt is not a correct universal solution.

Three outcomes are sought, **in order**:

- **Problem evidence:** independent evidence whether a material context delta changes the legitimate authorization/applicability decision, including cases where it does **not**.
- **Specification requirements:** a sourced, testable minimal contract for checking restoration conditions, re-deriving intent, qualifying current dependency evidence, transferring unresolved scope, deciding and recording the outcome.
- **Optional architectural comparison:** determine whether particular EA/EHD capabilities are necessary, merely compatible, redundant, less costly or costlier than a fully competent conventional PDP. **No favorable EA finding is assumed.**

Success at the first two does **not** require EA outperforming anything. Conversely, a useful EA proof-of-concept cannot establish the first two by circularly using EA's own labels as ground truth.

---

## 2. Primary source chronology — all current comments in Theme #23

The authoritative conversation is [FG-TIDA/themes Issue #23, *Security framework and requirements for authorization and privilege lifecycle management of AI agents*](https://github.com/FG-TIDA/themes/issues/23), proposed by **Ying Wang and Ye Tao / China Unicom**, created **16 September 2026**. Its public body describes separate *authorization decisions* and *privilege lifecycle transitions*, including initialization, change, hibernation, activation, revocation/recovery and cross-cutting governance. This is a **theme proposal**. The body cites [ITU-T SG17 Contribution 676 (24 August 2026), proposed work item X.aplm-aia](https://www.itu.int/md/T25-SG17-C-0676/en); this dossier has **not independently inspected that contribution's full text or verified subsequent Recommendation adoption**.

| When (UTC) / contributor | Original comment — direct link | What the source actually establishes for this dossier |
|---|---|---|
| **16 Sep, 15:35 — Lei Gao** | [#23 comment 5700157082](https://github.com/FG-TIDA/themes/issues/23#issuecomment-5700157082) | Proposes interface separation: privilege lifecycle and authorization in #23, human-intervention lifecycle in #16; a human resume/approval must not by itself restore a privilege whose applicability has changed. **Contributor proposal**, not #23's independently adopted normative text. |
| **17 Sep, 02:55 — Ying Wang (@Snoopywy)** | [#23 comment 5707764621](https://github.com/FG-TIDA/themes/issues/23#issuecomment-5707764621) | Ying describes #23 as a holistic framework and #16 as a distinct, compatible implementation path, rather than collapsing the themes. |
| **30 Sep, 16:05 — Iván Abril (@dakleyer)** | [#23 comment 5915019756](https://github.com/FG-TIDA/themes/issues/23#issuecomment-5915019756) | Raises **three** questions: valid restoration, receiving agent's operational dependencies after propagation, and evidence of complete revocation. Introduces the hibernated isolation privilege and newly critical downstream service as a **hypothetical example**. Invites discussion of EA context and residual uncertainty. |
| **9 Oct, 02:25 — Zhao Xinghua / Steven Zhao** | [#23 comment 6072991126](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6072991126) | Proposes **declaring a restore-condition predicate at suspension** and testing two errors: task resumes after source authority revoked, and reactivation based on a cached stale verdict. At this date it is explicitly a **suggestion**. |
| **14 Oct, 08:54 — Ying Wang** | [#23 comment 6164646309](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6164646309) | Replies to all three questions. Reassessment considers grant intent/scope, dependency graph, service criticality, NACL/policy, credential rotation and telemetry; a risk/privilege-specific evidence threshold may require restriction or reauthorization. Receiving PDP reevaluates propagated grants under operational dependencies; partial upstream visibility is made explicit. Revocation reporting may be fully, partially or unverifiably complete with compensating controls. EA-level dependency, criticality and cross-domain signals are **envisaged as optional inputs**. Ying welcomes further exploration of the hibernation example. |
| **14 Oct, 09:49 — Ying Wang replying to Zhao** | [#23 comment 6165603429](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6165603429) | **Important update:** Ying expressly agrees with suspension-time **declaration and recording of a factual restore condition**, to serve as an activation reference. At activation, she proposes **first validating this pre-declared condition, then deriving intent again under the current context**. She welcomes Zhao's proposed test cases in the initial set. This **supersedes our local v0.1/v0.2 assertion that source-author acceptance of that suggestion remained unknown**; it is acceptance in an issue discussion, **not formal standards adoption**. |

**Source discipline:** Above entries are paraphrases, not fabricated quotations, simulation logs or surrogate adoption decisions. Click the direct comments to read original wording and their surrounding discussion. Comments/issues may be edited, so a future formal study must pin the exact source text/version and the independent admissibility rule. This table covers **all six Issue #23 discussion comments visible at this cutoff**.

**Three Theme #23 problem families:** (A) reactivation/restoration, (B) inter-agent propagation into a different operational dependency context, and (C) cascading revocation with incomplete path visibility. **Only A / CU-HIB-01 is the first complete Challenge.** B and C remain separate prospective, source-attributed extensions; they cannot borrow proof from A.

---

## 3. Related external and internal evidence — direct reader links

### 3.1 External FG-TIDA, contributors and testbeds

| Link | Why a third party should read it | Current evidence boundary |
|---|---|---|
| [Theme #13 — Ecosystem-level Agent Defense](https://github.com/FG-TIDA/themes/issues/13), proposed by Ward Duchamps | Ecosystem-wide defense, partial actors' knowledge, provenance, signalling, noncentral containment and EA working discussion. | A theme/discussion, not a certified EA system. |
| [Theme #13 — Oleksii on grant/applicability vs contextual qualification](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5916002901) | A source-provided authority-applicability result is distinct from downstream contextual qualification. | Mapping semantics under review, not an independent grant calculation. |
| [Theme #13 — Nelson's UC-6/Theme13 Stage-0 calibration results](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5949120841) | Describes 64 checks preserving the original grant and changed contextual applicability in a *different case*. | **Reported bounded mapping/calibration**, not #23 hibernation execution. |
| [Theme #13 — Iván's interpretation of Stage-0 and oracle boundary](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5950456859) | Strongly separates source-provided applicability from qualified consumer view; reinforces mutation/expected-result discipline. | Architectural interpretation, no transferred hibernation result. |
| [Theme #13 — Nelson's fair evidence/cost testbed proposal](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5848265992) | Supports source dependence, acquisition cost, strong native peer, matched decision horizon, and reporting negative differentials. | Prospective experiment, no CU-HIB-01 partnership established. |
| [Theme #16 — Operational Human Oversight Integration](https://github.com/FG-TIDA/themes/issues/16) | Human request/review/decision pathway if restoration needs high-risk approval. | #16 does not issue #23 privileges by implication. |
| [Theme #33 — Non-Monotonic Eligibility](https://github.com/FG-TIDA/themes/issues/33), proposed by Zhao | Governing decisions may need evidence-driven reevaluation; adjacent to the lifecycle checkpoint. | Independent proposed scope, not #23 conformance. |
| [Use case #6 — Same agent, changed purpose](https://github.com/FG-TIDA/use-cases/issues/6), Arpita Sarker | Illustrates unchanged identity/grant with a material purpose/applicability change and human continuation question. | Analogy; purpose-change case differs from dependency-change case. |
| [Use case #4 — Federated ecosystem defense](https://github.com/FG-TIDA/use-cases/issues/4), Nelson Trasatti | Potential downstream testbed for independent domains and effect observation. | No approved native CU-HIB experiment or independent validation implied. |
| [Use case #21 — Controls work, system fails](https://github.com/FG-TIDA/use-cases/issues/21) | Related distinction between local control PASS and system-level negative consequences. | Independent use-case evidence and **different local R0/R1/R2 vocabulary**. |

**Important namespace caution:** In [Theme #13, Iván's response to Nell](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5968346100), **R1–R4** name *Nell's review questions*, not the **R1/R2/R3 experimental trajectories** used here. Likewise [UC-21](https://github.com/FG-TIDA/use-cases/issues/21) has its own R0/R1/R2 route names. Do **not** pool them.

### 3.2 Canonical DDS and Ecosystem Awareness corpus

The research programme's primary public entry is [Structural Awareness Contributions](https://github.com/dakleyer/structural-awareness-contributions); methodological and EA documents listed here retain their own publication/evidence states.

| Exact primary link | Scope used here |
|---|---|
| [DDS Canonical Method Index v0.1](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md) | **One DDS method**: Stage A specification discovery, Stage B architecture verification, Stage C implementation/problem validation. R1/R2/R3 are **within-Stage-A scenario trajectories**, not DDS stages. |
| [DDS Stage A — Challenge–Trajectory Profile](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md) | The technology-independent Challenge, bounded reference, strong comparator, blind oracle, local gates, Cost/Risk/Effectiveness and I/M/P/Ø outcomes. |
| [DDS Stage B](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_GATE_B_ARCHITECTURE_VERIFICATION_v0.1.md) | Later verification of an architecture against a frozen Stage A specification. Not achieved here. |
| [DDS Stage C](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_GATE_C_IMPLEMENTATION_PROBLEM_VALIDATION_v0.1.md) | Later observed effects of pinned real implementation/configuration against the original Challenge. Not achieved here. |
| [R01 Human Escalation / Whispering — §7 R1/R2/R3](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/HUMAN_ESCALATION_WHISPERING.md) | **Source of experimental trajectory convention**: R1 competent reference; R2 mechanism/quality plan; R3 one changed condition with R2 controller, gates, sources, parameters and positives frozen. No R01 mathematics transferred to CU-HIB-01. |
| [R01 → R1–R3/EA/UC-4 roadmap](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00G_HF_ROADMAP_R123_EA_COMPOSITIONS_UC4_v0.1_DRAFT.md) | Distinguishes R1/R2/R3 trajectory, EA/no EA arm and parameter variants; preserves independent effect observation and legitimate positive routes. |
| [Flores R2 freeze → R3 scientific principle (13 Oct)](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/campaigns-in-development/flores-population-ea/runtime-context/PRINCIPIO_R2_FREEZE_R3_2026-10-13.md) | Independent study's **methodological reminder**: defender repairs until competent, freeze whole configuration; R3 material and admissible; no after-the-fact weakening, patch or claimed universal coverage from one failure. **No Flores data/result transfers.** |
| [EA Canonical Requirements S1–S14, T1–T4, H1–H6](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) | Frozen candidate requirements and four “sufficiently good” conditions; **requirements, not demonstrated compliance**. |
| [EA General Interfaces 04 v0.5, IF-S1–13 and EHD](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md) | Qualified source/recipient metadata; authority provenance IF-S2, attestation IF-S3, policy/applicability IF-S4, telemetry IF-S7, privacy IF-S10, enforcement IF-S12. **EA is not PDP or issuer**. |
| [EA Canonical A/B/C/D meanings — 00M §1](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical) | A functional result; B characterized basis/assessable reserve; C grounded exploration frontier; D residual outside effective evaluation. Context-relative roles. **Not a calibrated D probability or proof of EA efficiency**. |
| [EA scientific plausibility and context-change rationale — 00N](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md) | A formerly sufficient output can become inadequate for a later receiving decision when conditions for reliance change. Plausibility argument only. |
| [EA–FG-TIDA specification-preparation annex 01F](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/01F_EA_FG_TIDA_SPECIFICATION_PREPARATION_ANNEX_v0.2_DRAFT.md) | Keeps source-owned vs candidate normative vs informative vs conformance/test-only statements distinct; no adopted WG specification presumed. |
| [EA interface projection 05A — current-state bridge](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md) | Source-native Theme output plus bounded EA adapter can be discussed; universal EHD schema is **not** currently established. |
| [Decision Boundary Challenge v0.2](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DECISION_BOUNDARY_CHALLENGE_v0.2.md) | Keeps source-native determination, operating posture, authority and actual effects separate; not a second DDS method. |
| [00D benchmark / strong peers](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) | Competent conventional comparators, legitimate positives, matched input/budget, reversibility and accounting; source does not demonstrate EA product superiority. |

**Direct link to the work in this GitHub PR:** [CU-HIB campaign overview](https://github.com/dakleyer/structural-awareness-contributions/blob/dds/china-unicom-privilege-lifecycle-stage-a-v0.1-20261014/research/ecosystem-awareness/campaigns-in-development/china-unicom-privilege-lifecycle-ea/CAMPAIGN.md), [previous v0.2 Challenge](https://github.com/dakleyer/structural-awareness-contributions/blob/dds/china-unicom-privilege-lifecycle-stage-a-v0.1-20261014/research/ecosystem-awareness/campaigns-in-development/china-unicom-privilege-lifecycle-ea/CHALLENGE_CONTRACT_v0.2.md), [v0.2 source/test traceability](https://github.com/dakleyer/structural-awareness-contributions/blob/dds/china-unicom-privilege-lifecycle-stage-a-v0.1-20261014/research/ecosystem-awareness/campaigns-in-development/china-unicom-privilege-lifecycle-ea/REQUIREMENTS_TRACEABILITY_v0.2.md), [v0.2 control fixture](https://github.com/dakleyer/structural-awareness-contributions/blob/dds/china-unicom-privilege-lifecycle-stage-a-v0.1-20261014/research/ecosystem-awareness/campaigns-in-development/china-unicom-privilege-lifecycle-ea/fixtures/PUBLIC_CALIBRATION_VECTORS_v0.2.json), [v0.2 approval requirements](https://github.com/dakleyer/structural-awareness-contributions/blob/dds/china-unicom-privilege-lifecycle-stage-a-v0.1-20261014/research/ecosystem-awareness/campaigns-in-development/china-unicom-privilege-lifecycle-ea/APPROVAL_AND_PREREGISTRATION_v0.2.md), and [PR #21](https://github.com/dakleyer/structural-awareness-contributions/pull/21). **The present v0.3 dossier governs the new R1/R2/R3 scientific design and latest-source interpretation; it does not retroactively rewrite those preserved earlier versions.**

---

## 4. The three independent axes — prevent namespace and proof confusion

| Axis | Levels | What varies | What remains independent |
|---|---|---|---|
| **Challenge trajectories** | **R1 → R2 → R3**, with R3 variants | Reference competence → defended restoration mechanism/quality plan → material environmental change **with R2 frozen** | Does **not** imply DDS Stage A/B/C advancement. |
| **Comparison configurations/arms** | **B2 strong conventional**; **B3 same conventional + EA-qualified semantics**; B0 naive *illustrative only* | Architecture/qualification mechanism under equivalent facts, scope, authority, cost and horizon | Does **not** redefine the world, grant or independent answer key. |
| **DDS maturity stages** | **Stage A** specification discovery → **Stage B** architecture verification → **Stage C** implementation/problem validation | Object under test and admissible reference/evidence | Document completion or static fixture PASS cannot claim Stage B/C. |

The R1/R2/R3 convention follows [R01 §7.1–7.5](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/HUMAN_ESCALATION_WHISPERING.md). There, R1 is a **competent reference** (never artificially bad), R2 examines an additional mechanism and fixed quality plan, and R3 changes one condition while the R2 controller is held fixed, retaining positives and costs. In CU-HIB-01 that logic is **adapted as a bounded experimental design, not a theorem or numerical result**.

**Essential sequencing rule:** first establish whether **R2 itself** treats the changed authorization basis correctly. Only in a **separate, prospectively controlled comparison** may one ask whether B3's EA metadata improves something over a strong B2. A valid, defended native R2 that already handles every material context change deserves full credit.

---

## 5. Technology-independent Challenge definition

### 5.1 Same requested decision across time

Let **Q(t)** be: *“Can the authorized PDP now restore the particular high-impact privilege G0, allowing agent A1 to execute isolate(R) for the declared original incident purpose?”*

The decision unit is **(principal, agent instance, grant, intended purpose, action, resource, current context, policy, time horizon)**. The policy owner—not the EA qualifier or the experiment author—defines admissible actions and exceptional overrides. The test reference must be defensible by an independently identified owner.

**Local illustrative world, not real China Unicom topology:**
- Domain **A** issues temporary grant **G0** to incident-response agent **A1** to isolate resource **R** for incident **X**, under current reference policy **P0**.
- Domain **B** operates service **S**, which is **already critical before the experiment**.
- At **t0** there is no dependency edge **S → R**, and the grant's original permitted use is legitimate within the reference model.
- At **t1** A1 hibernates, so **G0 is not exercisable**. The source owner records the **restore-condition anchor** requested in [Ying's 09:49 agreement](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6165603429). The strong controller's capabilities are frozen.
- At **t2** **one environmental relation** changes: Domain B creates the dependency **S → R**. Service S's criticality, G0, A1, P0 and the incident purpose remain unchanged. Thus the **consequence of isolate(R)** changes without an identity/policy edit.
- At **t3** A1 requests restoration of **the same** privilege. The source PDP applies the **two-step** check, not a replayed cached PASS.
- At **t4** the evaluator records current source evidence, the authorized PDP decision, any PEP effect, and permitted reauthorization/re-entry.

This **single-edge intervention** avoids the earlier v0.1 confound, which changed the dependency and service criticality together. A future *criticality-only* experiment can use a new version and a different one-variable intervention; it is not the primary CU-HIB-01 result.

### 5.2 Five fact/evaluation layers

| Layer | What it establishes | What it **does not** establish |
|---|---|---|
| **Grant validity** | Original issuer, bound agent, expiry, purpose, scope, revocation and suspension state | Permission to execute unchanged under any future dependencies. |
| **Recorded restore condition** | Source-declared facts recorded at hibernation that must be checked at activation | That all material future consequences are already enumerated or inferable. |
| **Current intent/applicability derivation** | Source-owned interpretation of whether isolate(R) remains appropriate under current dependency/criticality, NACL/policy, tokens, telemetry and risk | An EA-issued privilege or universal complete-world assertion. |
| **Evidential sufficiency** | What dependency change is known, by whom, within what scope, reference/version, freshness, lineage and incomplete coverage | A probability for unassessable residual effects simply from having confidence labels. |
| **Authorized response and actual effect** | PDP grants/holds/restricts/denies within policy; PEP executes or refuses, and independent effect is observed | That a proposed halt, human “resume” or EA alert was actually enforced or resolved safely. |

A source may know **the existence of a changed dependency** without knowing every downstream effect. Conversely, a source may declare **no visible change** while having insufficient coverage to exclude one. Absence of a reported edge is not automatically evidence of global absence.

### 5.3 Core hypotheses and non-circular falsifiers

| Claim | What would support it | What would refute or narrow it |
|---|---|---|
| **H-CONTEXT:** Privilege applicability depends on the current operational relation, not on unchanged identity/policy alone. | Independent owner-authorized reference changes the admissibility of Q(t3) when the single relevant edge changes. | The agreed owner policy allows isolate(R) regardless of the edge, or the edge is not actually material; then the intended Challenge is not established. |
| **H-CHECKPOINT:** Source-owned declaration + validation of the restore condition followed by new intent derivation is a testable reactivation checkpoint. | Pinned condition, actual reevaluation and decision traces separate T1 reference and T3 current context. | Only a cached PASS, or no independent way to distinguish predicate checking from re-derived intent. |
| **H-EVIDENCE:** Partial/changed source coverage must stay visible to the receiving decision. | The receiver preserves provenance, scope, freshness, material unknown and the responsible source for re-entry. | Claims of complete source coverage from partial evidence or repeated dependent sources; conversely unjustified global stops. |
| **H-RESP:** An authorized, decision-scoped response remains possible without universal suspension. | R-scoped reauthorization or an explicitly separately granted narrow permission, with legitimate unaffected operations continuing. | Unauthorised fallback, fabricated observation privilege, endless review or loss of deadline despite an available source-approved minimum closure. |
| **H-ADDED-EA (optional):** EA-qualified metadata adds operational value after all above are established. | Fair B2/B3 comparison shows a reproducible, independent outcome/burden gain under the **same legitimate facts, authority and horizon**. | Competent B2 matches/exceeds B3, B3 receives extra hidden data, or its purported gain is unmeasured/unsupported. **Parity is valid evidence against distinctiveness, not a failed Challenge.** |

A thought experiment or a local synthetic sample can support **plausibility/design completeness**, not independently demonstrate actual deployment safety or validate a particular China Unicom system.

---

## 6. R1 — competent reference and original boundaries

**Goal:** establish that the original authorization problem and legitimate success criteria make sense **before creating an exceptional context change**.

**Object:** a competent native authorization arrangement with source-owned grants/policy, correct identity, scope, suspension state, current token/NACL checks, and whichever current context evidence it legitimately supports. **No intentionally obsolete, broken or unpatched PDP.** If it already declares restore predicates and re-derives intent, that capability stays; the “R2 addition” may then have zero effect.

**R1 test contract:**

| R1 vector | Reference | Correct bounded observation |
|---|---|---|
| **R1-POS** | G0 valid; no S→R dependency; fresh material evidence; owner permits isolate(R) | Full restoration may be legitimate. Denying everything is a false positive / loss of effectiveness. |
| **R1-REV** | Source grant actually revoked | Credential cache or task restart is not current authority. |
| **R1-STALE** | Once-valid decision stored but source-evidence freshness expired | Reevaluate or explicitly mark insufficient; do not treat cached PASS as current proof. |
| **R1-NARROW** | Separate, current observation-only grant present or absent | Only an actually authorized narrow permission can be restored; **not** derived by subtraction from G0. |
| **R1-OTHER** | Immaterial relation unrelated to R changes | Other legitimate actions must continue; unrelated doubt cannot justify universal quarantine. |

**Minimum R1 outputs:** lawful baseline decision and grant source; positive result and actual PEP action if executed; scope/time provenance; visibility/rights map; decision deadline, baseline cost and fallback admissibility. If the owner reference is not independently defensible, do not progress to a scored R2/R3.

**What R1 cannot establish:** universal validity under a later context shift, completeness of a remote graph, EA utility, an inevitable unsafe restoration, or source-specific confidence thresholds.

---

## 7. R2 — defended restoration specification and complete freeze

**Goal:** develop and verify the **competent restoration quality plan** for Theme #23 with its source-owned improvements. R2 is **not “EA” by definition**.

### 7.1 Source-confirmed two-step activation

Ying's 14 October [follow-up to Zhao](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6165603429) establishes the **authors' discussion preference**:

**At hibernation:** The suspending party **declares and records a factual restore-condition reference**.  
**At activation, step 1:** Validate the **pre-declared restore condition** against the currently relevant evidence.  
**At activation, step 2:** **Derive intent under the current operational context**, even after the first check passes.  
**Only then:** The source PDP may choose its **authorized** full, restricted, held/reapproval or denial outcome; any applicable Theme #16 oversight is separately owned.

This is stronger and more precise than the first local v0.1/v0.2 narrative that treated Zhao's proposal as not yet agreed by Ying. **The source agreement is public; the exact algorithm, schema, risk thresholds, actual implementation and international normative status are NOT specified or validated by that comment.**

**Interpretation caution:** A restore predicate may be generic enough to cover future dependency changes. If R2 already checks all material dependencies during step 1, an attempted “step 2 alone catches the change” vector may not be admissible. It is not scientific to intentionally remove that predicate or artificially blind R2. Both order and sufficiency must be examined against the **actual** defended configuration.

### 7.2 R2 inputs, legitimate controls and complete coverage

R2 may use *all* legitimately authorized source checks and mechanisms that the participant defends:
- grant standing, issuer/subject/purpose/expiry/revocation;
- declared restore predicate, its original version and evaluation freshness;
- NACL and policy rules, current credentials and rotations;
- currently accessible dependency graph, service criticality, cross-domain evidence and runtime telemetry;
- source correlation/dependence, confidence assessment **if legitimately defined/calibrated by the owner**;
- a finite targeted query, independent reviewer or human oversight path where authorized;
- alternative/observation grant checks and PEP enforcement receipts.

**R2 prefreeze demonstration:** show that its quality plan **works** on legitimate restoration, revoked-authority, stale-cache, directly source-visible critical-dependency, unrelated-change and narrow-grant cases. If it succeeds without an EA overlay, this is a scientific success for R2, not an obstacle to the work.

### 7.3 Freeze discipline F-R2

After R2 is competently configured and repaired, preserve an **immutable versioned manifest** of the complete defended system:
- software/logic/configuration, source reference maps, predicate evaluation and intent derivation;
- grant/policy/credential/NACL scope and retrieval adapters;
- graph/discovery methods, polling/subscriptions, cross-domain query permissions, telemetry, time/freshness policies;
- declared adaptive mechanisms, review/retry and escalation behavior (freeze does **not** selectively disable or amputate these);
- admitted fallback, safe response/continuity rules, legitimate positives;
- available source owners, underlying data/authority rights, compute/network/human budgets and response horizon;
- expected positive/negative outcomes, blinded case-family selection and trace/effect schema.

**R2 freeze is not a ban on legitimate adaptation:** if the frozen controller already includes generic discovery, it may use it at R3. A patch **written after seeing a scored R3** starts a **new R2 successor and a new freeze**, without rewriting the previous evidence.

### 7.4 R2 exit

A defensible R2 exit has **demonstrated** source-approved restoration and positive cases, a meaningful bounded decision question, a frozen strong conventional configuration and a complete observation/authority/budget contract. A description of those ingredients is **PREPARATION**, not a pass.

---

## 8. R3 — new context with R2 fully frozen

**Goal:** expose the significance and limits of a later **contextual** change while applying **the same** R2 controller and source-owner rule. R3 is not a competition to invent a rule after a failure.

**Primary changed fact:** only the dependency edge **S→R** appears in Domain B after hibernation; **S was already critical**, and A1/G0/P0/incident purpose remain unchanged. This change is established **independently by the evaluator**. The arms receive only legitimately available observations.

### 8.1 R3 family and necessary contrasting branches

| R3 subcase | One relevant condition or evidence pattern | Expected authorized *question* (not a fabricated source verdict) | What it demonstrates or limits |
|---|---|---|---|
| **R3-A — directly visible delta** | Changed S→R edge is current and accessible to the native PDP; other source facts retained. | Does the declared restoration condition and/or current intent derivation correctly revise applicability? | **Context relevance**, even if conventional R2 already handles it. Parity is expected if B2 is good. |
| **R3-B — source-qualified cross-domain delta** | Domain B supplies a scoped event/relationship and lineage/freshness; the entire private graph is not shared. Same legitimate source facts accessible to B2/B3. | Can the PDP update only the affected isolate(R) reliance basis using this evidence, and record remaining coverage? | Minimum cross-domain **specification** for a qualified evidence handoff; no need to award the EA label. |
| **R3-C+ / R3-C− — identifiability limit** | Two reference worlds differ in hidden S→R truth but deliver **identical authorized partial observations**. | Do both systems preserve UNKNOWN and follow the source-approved risk policy rather than pretending they distinguished the worlds? | **No system** can know unobserved truth from an identical packet; EA must not be scored for magic detection. |
| **R3-D — relevant source becomes stale** | Source time/validity bound expires while the authority identity and policy may still be current; different *single-factor* temporal test. | Does R2 apply its current freshness rule and obtain new evidence or qualify insufficiency? | Temporal status is not token status; **not** pooled with primary one-edge causal estimate. |
| **R3-E — unrelated environmental change** | Different service changes; no source-approved material impact on isolate(R). | Does the controller continue legitimate R use without global hold? | Mandatory **positive** to rule out indiscriminate “stop everything.” |
| **R3-F — dependent corroboration** | Three signals derive from one source; no new independent fact. | Is uncertainty/freshness preserved despite apparent numerical agreement? | Source-independence and overconfidence control, not a grant calculation. |
| **R3-G — requalification/re-entry** | New **legitimately permitted** evidence or an independently issued revised grant arrives; the rule remains frozen. | Can the system resume only within the newly established scope before deadline and preserve its prior failure/hold record? | A successful exit from uncertainty requires a source-owned basis, not just human “resume” or an EA notification. |
| **R3-H — action-time race (later separate experiment)** | Context changes after PDP decision but before PEP effect. | What actor rechecks applicability, how is effect observed and who can cancel? | New temporal experiment; **not** proof from activation-only runs. |

**Important:** These are **case families and questions**. Their permitted dispositions and violation classifications require an independent, source-authorized policy; the local synthetic casebook's existing example expectations are not globally binding. A change of several environmental variables or a change in grant/policy **must be separately identified**, not smuggled into the one-edge primary case.

### 8.2 What exactly can be concluded from R3?

A proper R3 report separates **three levels**:

1. **Independent world/context fact:** Did the chosen material context relation genuinely change? Did this change the legitimacy or consequence of the intended act **according to the preagreed owner policy**? This is the *Challenge fact*, not EA output.
2. **Available information and processing:** Was the material delta visible, only inferable from a qualified cross-domain signal, or unavailable? Did the frozen R2 restore predicate, second intent pass and source-qualification logic distinguish the case within scope? For two indistinguishable packets, identification is **not established**.
3. **Source-owned decision and effect:** What did the PDP decide, what was actually enforced, what remained legitimate, and what happened to S and to unaffected operations? This cannot be deduced merely from an alert or “HOLD” log.

A *single* R3 failure shows a **counterexample to one frozen configuration in one admitted world**, not a universal impossibility for all conventional policies. A correct R3 is equally important: it demonstrates an adequate existing solution to that instance. Any broad statement such as “for every fixed repair, there exists an uncovered future change” requires a declared family and separate quantitative/proof obligations; [Flores' methodological record](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/campaigns-in-development/flores-population-ea/runtime-context/PRINCIPIO_R2_FREEZE_R3_2026-10-13.md) explicitly distinguishes the research principle from an experimental single-case result.

### 8.3 Confirmatory and adversarial R3 are different studies

**Confirmatory R3:** Prior to result inspection, an independent evaluator and the participant agree the *family* of admissible one-factor context changes, coverage/visibility variations, all eligible case inclusion, negative/positive controls, time horizon, budgets and scoring. The hidden event/seed is held out. **Do not choose an R3 only after learning which one beats B2.** All competent R2 passes, B3 failures and ties remain in the analysis.

**Exploratory adversarial R3 (optional):** A separate investigator may search for *material, previously uncovered* changes **after** a defended R2 freeze. The search space, interventions attempted, resource/time spent, discovered candidate's materiality and admission rule are all reported. This is useful diagnostic evidence but **selection-conditioned**: it cannot be silently called a random or precommitted comparative sample, nor does it prove generalized EA superiority. EA's general profile, if compared, remains fixed **before** the scored event disclosure. The defender's legitimate adaptive mechanisms stay available.

---

## 9. Minimum candidate specifications implied by the Challenge

These are **research hypotheses/specification candidates** with named owner boundaries. **Do not present them as normative China Unicom/ITU clauses merely because they resemble a source proposal.** The corresponding [canonical EA S1–S14/T1–T4](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) is a **requirements baseline**, not proof of compliance.

| ID | Required observable capability/question | Link to sources, owner and candidate EA corpus clause | Falsifiable evidence / negative control |
|---|---|---|---|
| **CU-SP01 — contextual applicability** | Re-check the *same* privilege at activation against current decision-relevant operating dependencies, even if identity and policy reference did not change. | [Ying 08:54](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6164646309); **source PDP #23**. EA S1/S3/S10, T1/T2 consume source facts. | R1-POS vs R3-A (identical grant, one new edge): current decision must reflect source policy, not reuse stale PASSED label. |
| **CU-SP02 — restore-condition anchor and order** | Preserve a source-declared restoration predicate from suspension; validate it **then** derive current intent at activation; record both operations and their version/time. | [Ying 09:49 agrees with Zhao](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6165603429); **#23 lifecycle/PDP owner**; [Zhao 09 Oct](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6072991126). | Stale cache, source revoked, material new dependency; trace must show what was checked in step 1 vs derived in step 2. |
| **CU-SP03 — evidential reference, not universal graph** | Carry sufficiently current dependency, criticality and cross-domain-trust observations with named source, proposition, scope, age/version, supported lineage and *explicit missing coverage*. | [Ying 08:54](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6164646309); EA S3/S6/S9/S11; [04 EHD](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md). | R3-B and R3-C+/C−; source-independent facts must not be manufactured from partial or duplicated messages. |
| **CU-SP04 — qualified determination** | Represent “current material basis established”, “source-provided partial/unknown” and “contradictory/stale” separately from authorization; do not collapse missing coverage to PASS. | EA T1/T2, S5, [00M A/B/C/D](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical); EA owns **qualification**, not privileges. | Indistinguishable worlds and correlated signals must not yield invented confidence or edge truth. |
| **CU-SP05 — bounded authorization response** | The **PDP** determines full/restricted/hold/re-auth/deny according to an approved privilege/risk policy. Observation-only restoration needs a **separate current permission**. | [Ying 08:54](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6164646309); EA T3, S1/S5/S13; #23 issuer/PDP is owner, #16 oversees human path. | No “fallback observation” without grant; no global hold for unrelated change. |
| **CU-SP06 — minimum-sufficient, timely review** | If evidence is insufficient, define an owner, affected scope, bounded re-entry/source query, expiry, real human capacity and deadline; preserve legitimate unrelated actions. | EA S3/S4/S5/S10, **T4**; [Theme #16](https://github.com/FG-TIDA/themes/issues/16) owns the human pathway. | R3-C/G/E positive; quantify time, network/data retrieval, reviewer effort and missed opportunity. |
| **CU-SP07 — decision/enforcement/effect split** | Preserve PDP decision reference and actual PEP effect receipt independently, including what action was stopped, continued or executed. | #23 decision vs enforcement; [DBC](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DECISION_BOUNDARY_CHALLENGE_v0.2.md), EA S12/S14. | Report “decision denied” separately from “isolation prevented”; measure actual simulated/native effect in admitted Stage C only. |
| **CU-SP08 — source and correlation discipline** | Specify how source confidence is assessed in its native scope and how dependence is handled; do not invent an aggregate threshold or convert unassessable residual D into numeric probability. | Ying's **confidence proposal** + EA 00M/04; calibration/aggregation algorithm remains **NOT_DEFINED** by the issue. | Three relays of one graph event cannot count as independent assurance; missing calibration is reported, not assigned zero. |
| **CU-SP09 — propagation profile (future)** | Reevaluate the propagated privilege against receiving agent's **operational dependencies**, with upstream incompleteness visible. | [Ying 08:54](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6164646309), CU-PROP-01, recipient PDP. | Separate receiving-agent scenario; not automatically proved by CU-HIB-01. |
| **CU-SP10 — revocation coverage profile (future)** | Track source-known revoked segments, known surviving privileges and unverified paths; report reason, affected coverage and compensating controls. | [Ying 08:54](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6164646309), CU-REV-01, source revocation authority. | A partial known revocation and uncertainty about additional paths can coexist; avoid claiming binary complete cleanup. |

### 9.1 Test against canonical EA's four sufficiency conditions

- **T1 — material awareness within declared limits:** Identify the one-edge relevant change **or say that the observation boundary does not establish it**. Ordinary variation and irrelevant changes are positive controls.
- **T2 — qualified determination and owner-preserving handoff:** Preserve native predicate/intent outcome and qualified cross-domain dependency evidence, source, scope, freshness, corroboration limits and UNKNOWN without replacing the authorization owner's judgement.
- **T3 — bounded authorized response:** A source-owning PDP must still authorize full/restricted/reapproval/hold/deny. No EA producer commands PEP; no universal “kill switch”; action externalities and continuity matter.
- **T4 — timely minimum-sufficient requalification:** The right actor must be able to receive/recheck enough evidence and act within a useful horizon and bounded burden. A truthful response after the action is irreversible may still fail operational effectiveness.

**If a competent implementation already satisfies T1–T4 and the corresponding source-owned #23 rules, the requirement is relevant and can be specified even though the EA differential is zero.** Specifications should describe **behaviour and verifiable evidence**, not mandate one brand, EA component, transport, central controller or internal algorithm.

### 9.2 A/B/C/D: strictly process-relative, not “four grades of world truth”

According to the [EA 00M §1 adopted local vocabulary](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical):
- **A** = what this source process actually delivers under its stated function (for example, its current graph relationship assessment).
- **B** = the source's established basis, recognized limits and characterized, assessable unused reserve (for example, a known additional verification path with defensible effort).
- **C** = a *grounded but uncharacterized* frontier where exploration is possible; not a known quantified reserve, nor every unchecked source.
- **D** = potentially material residual beyond effective evaluation by *this process for this question and time*. D is not “any unknown” and **cannot be assigned a defensible probability solely because an alarm exists**.

A source may legitimately report unknown fields without enough basis to classify their A/B/C/D role. The same fact may occupy different roles for Domain A, Domain B or a current receiving PDP. EA cannot claim universal visibility from the combination.

### 9.3 EHD minimum and source autonomy

The [EA general interface 04](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md) proposes a **semantic handoff overlay**, not mandatory payload duplication:
1. producer epistemic profile/ref and version, or inline equivalent;
2. subject/proposition/decision domain and scope;
3. producer/issuer and ownership;
4. native operational result/closure or valid result reference;
5. determination/qualification state kind;
6. explicit material unknown qualifiers.

Where material: grant/intent/suspension anchors, relevant graph delta, source age, version, source-dependence, affected services, review expiry and targeted re-entry reference. This is **a research candidate interface**, not a China Unicom-approved encoding. Each domain retains native authority and private information; no requirement to share an entire graph or agree on one global ecosystem truth.

---

## 10. Test design, expected observations and fairness

### 10.1 Comparators and why B0 cannot prove anything

**B0** — old naive “resume on same identity/policy”: *illustrative anti-pattern only*. It explains the failure mode but is not a competent comparison reference.

**B2** — the **strongest legitimate native PDP/privilege-lifecycle configuration** an authorized participant can defend. It may implement source-anchored restore conditions, intent derivation, source/freshness/graph checks, dependency-aware requalification and explicit UNKNOWN semantics **without using any EA terminology**.

**B3** — **the same source-owned PDP, with optional EHD/EA qualification** using the same legitimate underlying facts, authorization rights, human-review access, response horizon and end-to-end budget. Compare the semantic preservation, latency, false-hold, total burden and actual effects; count EA's source acquisition/processing/maintenance costs.

Neither B2 nor B3 has the hidden evaluator map, or gets to reconfigure itself after viewing scored cases. A B2 that has an equivalent qualifier earns parity and may be the recommended implementation.

### 10.2 Required reference worlds and controls

The independent evaluator must establish:
- **W0** unchanged legitimate context, to prove a full valid restoration remains accessible.
- **W+** source-confirmed newly material S→R edge with service S already critical; reactivation may now be disallowed under a **separately approved example risk policy**.
- **W−** no edge under the same registered policy and horizon; where participant-visible evidence is intentionally incomplete, **W+ and W− may have identical input packets**. Then no algorithm can infer the hidden distinction by calculation alone.
- A **source-visible** changed edge baseline that a conventional PDP can use.
- A **source-missing/stale** case, plus source-correlated duplicate signals.
- An **irrelevant-change** case and independently valid or invalid **restricted-grant** controls.
- A recovery case with current new evidence, source-approved action and actual authorized outcome.
- A prospective time-of-use/effect control in a separate registered experiment if needed.

The [previous local 12-case synthetic JSON](https://github.com/dakleyer/structural-awareness-contributions/blob/dds/china-unicom-privilege-lifecycle-stage-a-v0.1-20261014/research/ecosystem-awareness/campaigns-in-development/china-unicom-privilege-lifecycle-ea/fixtures/PUBLIC_CALIBRATION_VECTORS_v0.2.json) is **public calibration only**, not an independent blind oracle. It already distinguishes the causal one-edge case, hidden-world pair, positive restoration, expired evidence, separate limited grant and correlated signals. Its scenario labels must not be used to selectively choose scored results.

### 10.3 Independent scoring and outcomes

Do not label a case PASS just because an EA producer warns correctly. The legitimate scorecard is derived **ex ante** from:
1. source-approved policy and materiality criterion for this *particular* action;
2. independently known evaluator facts / observed target state;
3. declared participant-visible evidence, authority and response deadline;
4. the actual PDP decision *and* (where executed) PEP effect;
5. legitimate positive/negative controls;
6. matched total work and finite human/response capacity.

| DDS Stage A outcome class | Meaning for this challenge |
|---|---|
| **I — high-value legitimate closure** | A source-authorized correct and timely full/restricted/hold/reapproval route for this particular world, with sufficient decision quality by the admitted criterion. The same class is accessible to any technology. |
| **M — legitimate reference closure** | A less ambitious but **independently admitted, reachable and nontrivial** conventional closure. Not a free default; if no such M is established, Type-1 rate remains unscored. |
| **P — material prohibited route** | A preregistered unauthorized isolation/grant decision/effect, or a specific independently defined consequential violation. False certainty with no resulting prohibited route must be reported as a qualification defect, not silently promoted to an observed PEP effect. |
| **Ø — incomplete/no sufficient closure** | Horizon exhausted or no source-authorized sufficient path; **not automatically a Risk violation**. Distinguish honest insufficient information from needless failure to reach a legitimate M. |

Suggested **separate** measurement dimensions: material-delta reference correctness; restore-predicate/intent-check order and recency; source/context coverage fidelity; false unqualified restoration; false hold under W0; R-scoped containment vs global pause; time to justified posture; time to eventual source-backed re-entry; query/compute/source/communication/human cost; actual enforcement/effect; attribution and reproducibility. Risk thresholds and confidence aggregation **must be approved before scoring**; this document invents no percentages, deployment savings or certification claims.

### 10.4 Scientific stopping and falsification conditions

**Insufficient / stop** if: the source policy/effect does not actually make S→R material; R1 legitimate grant baseline was never established; there is no independent evaluator; primary world variables change jointly; B2 sources are suppressed; B3 uses hidden facts; follow-up cases selected solely to defeat B2; source data cannot legally be shared; response cost/horizon is unknown but later used as a pass criterion; or an R3 counterexample is marketed as a universal impossibility result.

**Negative but useful** findings include: a proper native R2/peer handles every admitted shift; EA adds complexity without benefit; no actor can know the hidden edge; a source-authorized limited action is impossible in one world; reauthorization cannot finish within horizon; a candidate qualified packet lacks decision-relevant information. Preserve those findings as constraints on specifications.

---

## 11. Work programme and approval gates for a complete Challenge

This section makes the campaign deliverable **without claiming those deliverables already exist**.

| Work package | Required work and traceable output | Entry → exit condition | Responsible owner / status at v0.3 |
|---|---|---|---|
| **WP0 — source and policy baseline** | Complete comment/source register; confirm latest Ying two-step restore semantics; domain owner chooses one authorized reference, emergency exceptions, critical-dependency materiality and legitimate fallback. | Public discussion → **source-approved** experimental decision rule / pinned meaning. | China Unicom/other authorized policy owner **NOT ASSIGNED to this experiment**. Documentary register complete, normative acceptance pending. |
| **WP1 — R1 competence** | Demonstrate currently valid grant/positive restoration, native checks, intended purpose and effect; record authority and evidence. | Independent reference + positive/negative cases → competent R1 record. | Native PDP/config owner and reviewer **NOT ASSIGNED**; **NOT EXECUTED**. |
| **WP2 — R2 strengthen/repair/freeze** | Implement/verify declared restore-condition, validation-then-intent derivation, graph/freshness, narrow authority, response and human path; repair and freeze complete native controller and all source rights. | R1 evidenced → R2 valid positives + full versioned freeze. | PDP owner **NOT ASSIGNED**; **NO R2 FREEZE**. |
| **WP3 — R3 contextual challenge** | Independently construct one-edge delta, observation/UNKNOWN variants, legitimate positives and parity; freeze generator/expectations and run same R2 on altered context. | Full R2 freeze + oracle/seed/budget preregistration → complete primary/pair traces and owner-bound outcome. | Independent evaluator **NOT ASSIGNED**; **NO BLIND RUN**. |
| **WP4 — specification extraction** | Convert actual R3 evidence into source-owned/candidate requirements CU-SP01–10, T1–T4, minimal EHD and explicit nonclaims; preserve positive/negative findings. | Reported evidence with links → versioned **Stage A candidate specification**, accepted/not established/negative as appropriate. | Local analyst may prepare wording, but evidence-dependent adoption **PENDING**. |
| **WP5 — optional B2/B3 evaluation** | Paired native strong PDP vs same PDP+EA qualified interface, source-equivalent rights, total cost and result parity; source-accepted interface semantics. | No cherry picking, equal data/time/budget, independent expectation → bounded differential/no-differential finding. | Partners and independent reviewer **NOT ASSIGNED**; **NOT EXECUTED**. |
| **WP6 — Stage B/C (separate)** | Stage B verify architecture against frozen Stage A specification; Stage C validate pinned implementation against actual Challenge/effects. | Explicit separate stage entry/freeze and evidence. | **NOT_STARTED**. |

**Decision gates:** **D0 local challenge-design review** (content/falsifiability/traceability; pending independent sign-off), **D1 external semantic/policy approval** (not obtained), **D2 blinded experiment preregistration with frozen R1/R2/R3 and fair evidence** (not obtained), **D3 actual Stage A adjudicated result** (not executed). See [existing gate ledger](https://github.com/dakleyer/structural-awareness-contributions/blob/dds/china-unicom-privilege-lifecycle-stage-a-v0.1-20261014/research/ecosystem-awareness/campaigns-in-development/china-unicom-privilege-lifecycle-ea/APPROVAL_AND_PREREGISTRATION_v0.2.md). The v0.3 challenge **corrects** its scientific research framing and source-adoption status; it does not self-approve these gates.

**Minimal independent D0 reviewer questions:**
1. Is there a defensible, current source-owned permission criterion for the *same* resource-isolation decision at T0 and T3?
2. Are the **two different checks** at activation—declared restore condition, then current intent derivation—mapped to source statements without attributing an invented implementation?
3. Do R1, R2 and R3 really preserve all original controls, one-factor causal intervention, valid positives and the same horizon?
4. Is the R3 result independent of EA labels, source-confidence speculation and hidden-world leakage?
5. Does each specification statement identify owner, source evidence, falsifier, missing coverage, proper handoff, and next responsible actor?
6. Are strong native success, no EA differential, inability to observe a hidden change and failed reauthorization admissible outcomes?
7. Does any future benchmark retain cost, privacy, all-case selection, human capacity and observed PDP/PEP effects?

---

## 12. Actionable joint-discussion agenda (not sent)

A future comment to [Ying and Ye Tao in Theme #23](https://github.com/FG-TIDA/themes/issues/23) should not ask whether “EA is useful” in the abstract; Ying has already welcomed exploring the case. A precise discussion would ask:

**A. Restoration reference:** For **CU-HIB-01**, would the predeclared restore condition contain an explicit *dependency/critical-service applicability relation* (or a versioned reference to it), or should the second intent derivation cover previously unenumerated material dependencies? How is a material mismatch recorded before current privilege enforcement?

**B. Minimum cross-domain evidence:** What scoped assertion can Domain B supply to Domain A's PDP without exposing the full private graph? Which source, subject, edge/criticality, version/freshness, coverage and **not-established** fields are indispensable to a decision?

**C. Policy and fallback:** Under which approved authority may full isolation remain disallowed or a restricted observation privilege be granted? What is the source-owned behavior under incomplete visibility, and how do human approvals connect without automatically restoring prior permissions?

**D. Testing collaboration:** Is a **competent native R2 → full freeze → one post-hibernation R3 dependency change**, with legitimate unchanged restoration and hidden-world controls, a useful starting specification-discovery experiment? Can the source owners help define action admissibility before an independent evaluator registers the case?

**E. Wider lifecycle (later):** How should the separately described receiving-agent propagation and “fully/partially/unverifiably revoked” reporting be projected to later distinct Challenges without attributing global state to EA?

These questions are proposed by the local campaign; they have **not** been posted or approved as external joint work.

---

## 13. What is established, what remains open, and what must never be claimed

**Established from public discussion:** #23 proposes contextual privilege revalidation; Ying provides a multi-source/risk-aware account; source-owned restoration conditions and **validation followed by intent derivation** are explicitly supported by her later comment; optional ecosystem-level signals are welcome for further discussion. Theme #13/04/00/T1–T4 provide a local candidate specification vocabulary; R01/DDS provide an experimental discipline.

**Established from local work:** one-factor synthetic Challenge design, source and authority separation, an auditable v0.2 public casebook, self-audit and an R1/R2/R3 v0.3 review protocol **on paper**. No independent semantic or experimental acceptance is implied.

**Open and blocking:** a **named authorized owner** for the real/sandbox privilege, exact source-approved rule/threshold and exception policy, independent evaluator, defended native R2, full freeze, blind event generation and oracle separation, privacy/source permission, response horizon, costs, actual traces and observed effects. No data justifies a numerical confidence aggregator, universal EA advantage or any adoption statement.

**Not established:** that China Unicom co-developed or approved this campaign; that #23's discussion has become an adopted ITU-T Recommendation; that any particular EA implementation is necessary for safe privilege restoration; that an unobservable edge is detectable by EA; that a finite counterexample proves universal impossibility; that an “alert,” textual design audit or local JSON PASS equals safe enforcement; or that a Stage A documentary dossier satisfies DDS Stage B or C.

### Reviewer conclusion

**A changed context can alter the question that a previously successful authorization answer was sufficient to settle.** The first scientific task is to make that change and its permitted consequences independently inspectable **under R1 → R2 → R3**. The next task is to produce **owner-preserving, falsifiable specifications** for recognizing materiality, carrying evidential limits and reaching a timely authorized response. Whether an implementation marketed as “EA” contributes a measurable extra differential is **a separate secondary question**.

---

## Appendix A. Canonical cross-reference identifiers and direct discussion links

**Primary six Theme #23 comments:**  
[Lei 16 Sep](https://github.com/FG-TIDA/themes/issues/23#issuecomment-5700157082) · [Ying 17 Sep](https://github.com/FG-TIDA/themes/issues/23#issuecomment-5707764621) · [Iván 30 Sep](https://github.com/FG-TIDA/themes/issues/23#issuecomment-5915019756) · [Zhao 9 Oct](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6072991126) · [Ying 14 Oct, 08:54](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6164646309) · **[Ying 14 Oct, 09:49 agreeing with Zhao](https://github.com/FG-TIDA/themes/issues/23#issuecomment-6165603429)**.

**Related cross-theme sources:**  
[FG-TIDA Theme #13](https://github.com/FG-TIDA/themes/issues/13) · [Theme #16](https://github.com/FG-TIDA/themes/issues/16) · [Theme #33](https://github.com/FG-TIDA/themes/issues/33) · [UC-4](https://github.com/FG-TIDA/use-cases/issues/4) · [UC-6](https://github.com/FG-TIDA/use-cases/issues/6) · [UC-21](https://github.com/FG-TIDA/use-cases/issues/21) · [Nelson Theme13 case 5949120841](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5949120841) · [Oleksii Theme13 semantics](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5916002901) · [Nelson fair testbed design](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5848265992) · [Iván Stage-0 comment](https://github.com/FG-TIDA/themes/issues/13#issuecomment-5950456859).

**Method and specification reference routes:**  
[DDS A/B/C method](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md) · [DDS Stage A](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md) · [R01 R1/R2/R3 controller example](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/reductions/00G-R01/feasibility/HUMAN_ESCALATION_WHISPERING.md) · [R01 experimental roadmap](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00G_HF_ROADMAP_R123_EA_COMPOSITIONS_UC4_v0.1_DRAFT.md) · [EA S1–S14 / T1–T4](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) · [EA 04 interfaces](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/04_GENERAL_FUNCTIONAL_INTERFACES_AGENTIC_SECURITY_v0.5_INTEGRATED.md) · [00M A/B/C/D](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00M_ABCD_AND_MATHEMATICAL_PLAUSIBILITY_v0.8_RESEARCH_NOTE.md#abcd-canonical) · [00N plausibility](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00N_FROM_MECHANISM_TO_REQUIREMENTS_SCIENTIFIC_PLAUSIBILITY_v0.7_RESEARCH_NOTE.md) · [01F specification readiness](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/01F_EA_FG_TIDA_SPECIFICATION_PREPARATION_ANNEX_v0.2_DRAFT.md) · [05A current source evidence](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md).

**Local campaign versioning:** [PR #21](https://github.com/dakleyer/structural-awareness-contributions/pull/21), [campaign registry](https://github.com/dakleyer/structural-awareness-contributions/blob/dds/china-unicom-privilege-lifecycle-stage-a-v0.1-20261014/research/ecosystem-awareness/campaigns-in-development/REGISTRY.json), [v0.1 trial predecessor](https://github.com/dakleyer/structural-awareness-contributions/blob/dds/china-unicom-privilege-lifecycle-stage-a-v0.1-20261014/research/ecosystem-awareness/campaigns-in-development/china-unicom-privilege-lifecycle-ea/PRIMARY_TRIAL_PROTOCOL_DRAFT_v0.1.md), [v0.2 Challenge predecessor](https://github.com/dakleyer/structural-awareness-contributions/blob/dds/china-unicom-privilege-lifecycle-stage-a-v0.1-20261014/research/ecosystem-awareness/campaigns-in-development/china-unicom-privilege-lifecycle-ea/CHALLENGE_CONTRACT_v0.2.md), [v0.2 self-audit](https://github.com/dakleyer/structural-awareness-contributions/blob/dds/china-unicom-privilege-lifecycle-stage-a-v0.1-20261014/research/ecosystem-awareness/campaigns-in-development/china-unicom-privilege-lifecycle-ea/AUDIT_REPORT_2026-10-14.md), [v0.2 fixture](https://github.com/dakleyer/structural-awareness-contributions/blob/dds/china-unicom-privilege-lifecycle-stage-a-v0.1-20261014/research/ecosystem-awareness/campaigns-in-development/china-unicom-privilege-lifecycle-ea/fixtures/PUBLIC_CALIBRATION_VECTORS_v0.2.json). The current v0.3 text is a **successor analytical contract**, not a silent rewrite of old evidence.

**External standards-related origin:** [ITU-T SG17 C-0676](https://www.itu.int/md/T25-SG17-C-0676/en) — as **cited in the public #23 issue**, not independently authenticated as adopted text here.

---

*End of third-party dossier. All rights and ownership remain with their actual sources; research examples and candidate requirements carry no institutional endorsement or operational authorization.*
