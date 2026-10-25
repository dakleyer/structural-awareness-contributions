# DDS-S2-EA-01 — Independent S2 mobility / Ecosystem Awareness requirements review (v0.2)

**Status:** WORK ORDER PREPARED FOR INDEPENDENT ASSIGNMENT-READINESS CHECK — reviewer **UNASSIGNED**, no independent findings yet; submission/publication requires agreement.  
**Home:** Ecosystem Awareness → DDS → review-packets/DDS-S2-EA-01. This is the **third bounded review task**, distinct from [DDS-MR-01 (method audit)](../DDS-MR-01/README.md), the Thales capability pre-review and any actual product execution.  
**Question:** Do the **frozen Ecosystem Awareness requirements** adequately specify what a candidate would need to do in **UC21 scenario S2 / 00F (shared smart-city mobility)** under the **conditional DDS R1, R2 and R3 positions**? Where does the specification leave a gap, conflicting instruction, untestable claim, or unstated dependency?  
**Decision owner:** Iván Abril Palma. No reviewer is appointed, credited or publicly attributed by this document. Any future contribution, decision or FG-TIDA synthesis is separately agreed.

## 0. Exact task — read, challenge, record

**Review at a glance:**

| Phase | Required reading or check | Evidence to return |
|---|---|---|
| Establish the case | Original S2, frozen S/T requirements and 00F | Six sourced Q0–Q5 adequacy rows |
| Examine conditional traversals | DDS method and existing 00L record | Three on-paper R1/R2/R3 rows; no invented execution |
| Challenge the conclusion | N1/N2, corrected A14 paired trace and A23 ceiling | Negative controls, recorded peer tie, one bounded counterexample |
| Hand in one record | Follow the agreed §6 private or consented public route | One completed template and source pins |

Complete **one documentary adequacy audit**, approximately **4–6 hours** (planning estimate, subject to reviewer acceptance):

1. Read the **required pinned sources** in §1, especially the source-native S2 case, frozen S1–S14/T1–T4 requirements, 00F Q0–Q5 and its existing 00L replay.
2. Complete **six gate rows Q0–Q5** in the [review template](./REVIEW_RECORD_TEMPLATE.md): for each gate, identify the requirement text, expected decision, credible counterexample, and whether the words actually oblige that behaviour.
3. Complete **three DDS-position rows R1/R2/R3**: adequacy **on paper**, entry/preparation assumptions, costs and information boundary. Do **not** grant a test PASS merely because requirements sound sufficient.
4. Evaluate the two mandatory adverse probes **N1/N2**, including the **strong conventional-peer tie already recorded in 00L**. Give **at least one** precise counterexample or explicitly explain why none was found in this narrow review.
5. Submit **one findings document** using the agreed restricted or consented public route in §6. Do not edit frozen cases, S#/T#/H# requirements, 00F variants, executable fixtures or DDS methodology in this task.

**Deliverable:** one source-cited reviewer record (normally 2–4 pages), not a vendor benchmark, new city simulator, legal opinion, code project, revised requirement set, proof of product compliance, or completed blind R3 run. Honest negative/unknown findings are useful.

## 1. Self-contained source pack — fixed reference cut

All required technical documents below are pinned to **Contributions commit `b056bd621262edc3a026fd21780c866afb22b1d5`** (25 October 2026), except the original frozen UC21 S2 annex, pinned separately. A live `main` link is for navigation, **not evidence pinning**. If content later changes, record the new commit and compare it rather than silently replacing the reference cut.

| Source | Exact pinned document | Reviewer reads |
|---|---|---|
| A — original case, **required** | [UC21/S2 — The City That Stopped Safely](https://github.com/dakleyer/use-cases/blob/aec08fb5b0fac2ee399372370e9ee2a82a2d5779/contributions/when-controls-work-system-fails/annexes/scenarios/S2.md) | Case identity, actors, A/B/NORMAL/HOLD, Central Bridge, two-minute qualification/five-minute response; original frozen scenario is authoritative. |
| B — requirements, **required** | [Frozen canonical S1–S14, T1–T4, H1–H6 and KPI](https://github.com/dakleyer/structural-awareness-contributions/blob/b056bd621262edc3a026fd21780c866afb22b1d5/research/ecosystem-awareness/baseline/00_CANONICAL_REQUIREMENTS_CHALLENGES_SUFFICIENCY_HYPOTHESES_KPIS.md) | §§2–6, meaning of each requirement and test conditions. Do not add S15, T5, H7 or silently redefine existing IDs. |
| C — case projection, **required** | [00F v0.2 Freeze Edition](https://github.com/dakleyer/structural-awareness-contributions/blob/b056bd621262edc3a026fd21780c866afb22b1d5/research/ecosystem-awareness/baseline/00F_FAILURE_MODE_SMART_CITY_MOBILITY_SYSTEMIC_DIVERGENCE_v0.2_FREEZE_EDITION.md) | §§6–8D and 9; Q0–Q5, normal V0, known conflict V1, published drift V8, scenario-native R0/R1/R2 and falsifiers. A document freeze is **not a trial PASS**. |
| D — DDS method, **required** | [DDS canonical method index](https://github.com/dakleyer/structural-awareness-contributions/blob/b056bd621262edc3a026fd21780c866afb22b1d5/research/ecosystem-awareness/DDS_CANONICAL_METHOD_INDEX_v0.1.md) | §5 optional sequential R1/R2/R3, real R2 adaptation cost, private future R3 selection/custody; §6 A/B/C limits. |
| E — **existing** S2 traversal, **required** | [00L-00F paired paper traversal](https://github.com/dakleyer/structural-awareness-contributions/blob/b056bd621262edc3a026fd21780c866afb22b1d5/research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_00F_TRAZA_PAPEL_EMPAREJADA_v0.1.md) | Synthetic local paper decisions; this is the case already worked, not a request to invent another one. |
| F — actual symbolic control, **required** | [00L-A10 paired check](https://github.com/dakleyer/structural-awareness-contributions/blob/b056bd621262edc3a026fd21780c866afb22b1d5/research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A10_VERIFICACION_PARES_Y_PREVUELO_v0.1.md) · [A14 corrections](https://github.com/dakleyer/structural-awareness-contributions/blob/b056bd621262edc3a026fd21780c866afb22b1d5/research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A14_CORRECCIONES_AUDITORIA_v0.1.md) · [corrected JSONL](https://github.com/dakleyer/structural-awareness-contributions/blob/b056bd621262edc3a026fd21780c866afb22b1d5/research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A14_TRAZAS_CORREGIDAS.jsonl) | One S2 micro-pair: `fire_slot: 10 → 11`, other observations held. Read the **corrected** v2 trace; strong peer agrees with the reference in both branches. Not V8 or real mobility. |
| G — conformance ceiling, **required** | [00K-A23 requirement-conformance sufficiency](https://github.com/dakleyer/structural-awareness-contributions/blob/b056bd621262edc3a026fd21780c866afb22b1d5/research/ecosystem-awareness/baseline/00K_A23_CANONICAL_REQUIREMENT_CONFORMANCE_SUFFICIENCY_P1_P6_v0.1.md) | §§3–5,10: finite projection supports P1/P2/P4; P3/P5/P6 still open/countermodel-bound. No global sufficiency theorem. |
| H — optional deeper trace | [00L-A09 source bridge](https://github.com/dakleyer/structural-awareness-contributions/blob/b056bd621262edc3a026fd21780c866afb22b1d5/research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A09_PUENTE_TRAZAS_EVIDENCIA_SIMBOLICA_v0.1.md) · [A08 protocol](https://github.com/dakleyer/structural-awareness-contributions/blob/b056bd621262edc3a026fd21780c866afb22b1d5/research/ecosystem-awareness/baseline/00L_REINFORCED_PAPER_TRAVERSALS_00E_00J_v0.1/00L_A08_PROTOCOLO_REPRODUCIBILIDAD_v0.1.md) | Paper vs prior symbolic vs current symbolic vs product evidence; observation, oracle and denominator discipline. |
| I — optional cost detail | [00D comparator / §4.2](https://github.com/dakleyer/structural-awareness-contributions/blob/b056bd621262edc3a026fd21780c866afb22b1d5/research/ecosystem-awareness/baseline/00D_CANONICAL_ARCHITECTURE_BENCHMARK_AND_REFERENCE_SCENARIO_EVIDENCE_v0.2.md) · [DDS Stage A §§10a,17](https://github.com/dakleyer/structural-awareness-contributions/blob/b056bd621262edc3a026fd21780c866afb22b1d5/research/ecosystem-awareness/DDS_CHALLENGE_TRAJECTORY_PROFILE_v0.1.md) | Matched comparator, full-cost horizon, source namespace and minimum prospective run record. |

For technology context only: [FIWARE / NGSI-LD profile](https://github.com/dakleyer/structural-awareness-contributions/blob/b056bd621262edc3a026fd21780c866afb22b1d5/research/ecosystem-awareness/baseline/00F_A01_FIWARE_NGSI_LD_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) and [AWS IoT/TwinMaker profile](https://github.com/dakleyer/structural-awareness-contributions/blob/b056bd621262edc3a026fd21780c866afb22b1d5/research/ecosystem-awareness/baseline/00F_A02_AWS_IOT_TWINMAKER_CORE_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md). They are **design assessments**, not evidence either product failed or passed.

### English navigation aid for original Spanish-language 00L evidence

The instructions and template here are in English. Some **mandatory frozen sources** retain Spanish titles and text; this table helps locate them but does not translate, reinterpret or replace the source. The reviewer must be able to verify the original, or agree a bounded translation/read-through before accepting the time box.

| Original label | English navigation cue | Check in the source |
|---|---|---|
| `traza de papel emparejada` | Paired paper traversal | What was decided on the same shared resource and time |
| `verificación de pares y prevuelo` | Paired verification and preflight | Matched data, controls and strong conventional peer |
| `correcciones de auditoría` | Audit corrections | Which corrected version supersedes the earlier trace |
| `trazas corregidas` | Corrected traces | Exact recorded JSONL decisions, not a city execution |

## 2. Do not mix three namespaces

| Term | Exact meaning here |
|---|---|
| **UC21 S2 / 00F** | Original **mobility scenario**; different from requirement **S2** inside canonical S1–S14. |
| **DDS R1 → R2 → R3** | **Optional, conditional study positions**: competent initial configuration; strengthened repair after **demonstrated R1 FAIL** and with counted preparation cost; then eligible **proven predecessor PASS** facing a prospectively selected, privately held material change. An early PASS may mean later positions `NOT_RUN/NOT_REQUIRED`. |
| **00F native R0 / R1 / R2** | A different case-local design comparison: standard, defended top-notch, same top-notch frozen under drift. It **does not** certify optional DDS R2/R3, and the published V8 is **not** a secret holdout. |
| **A23 R1–R6** | Mathematical **clause bundles** for P1–P6, **not DDS traversals**. |
| **DDS Stage A/B/C** | Requirement/specification discovery, architecture realization, implementation/problem validation respectively. This assignment is a **Stage A documentary check**, not Stage B/C outcome. |

A map between namespaces is a **qualified crosswalk**, not license to transport PASS, trial-count, custody or vendor claims.

## 3. Six fixed questions — the gate-by-gate audit

For each gate, start from **00F §6** and canonical requirements §§2–6, **quote or cite a specific clause**, and ask: does the **requirement itself** prescribe enough to distinguish safe/legitimate continuation, limited containment and unresolved status **without requiring an oracle or hidden authority**? An illustrative 00F route cannot substitute for the normative requirement text.

| Gate | Fixed 00F requirement projection | What the reviewer must challenge |
|---|---|---|
| **Q0 — frame shared use** | `S1/S3/S9/S14 → T2/T3/T4 → H2/H4/H6` | Decision scope, corridor-time resource, owner, live authority, capacity/deadline, legitimate NORMAL and fallback. |
| **Q1 — material break** | `S3/S5/S10/S14 → T1/T2/T4 → H1/H2/H3/H5/H6` | Semantic freshness, source-dependence/hidden common root, material-change trigger, UNKNOWN vs unwarranted certainty. |
| **Q2 — compose postures** | `S5/S6/S9/S11/S14 → T2/T4 → H2/H3/H4` | A/B/NORMAL/HOLD jointly incompatible on **same resource and time**, correlated signals, missing actor visibility; local PASS cannot become city PASS. |
| **Q3 — bounded posture** | `S1/S3/S4/S5/S14 → T2/T3/T4 → H1/H4/H6` | Authorized actor, scope, human queue **finite**, action expiry, response margin; blanket HOLD must not win V0. |
| **Q4 — targeted requalification** | `S3/S10/S12/S14 → T1/T2/T4 → H4/H5/H6` | Minimal evidence to reopen affected dependency/model, stop rules, search load, human and time cost; feasible within window. |
| **Q5 — arbitrate/resume** | `S9/S11/S12/S14 → T1/T2/T4 (plus T3 for non-null action) → H2/H4/H5/H6` | Authority vs evidence, shared outcome, veto/expiry, legitimate segmented/normal return, residual trace and **observed** effect. |

**Use one status per row:** `SPECIFIED` (obligation is clear in frozen requirements), `CONDITIONAL_OR_UNDER_SPECIFIED` (needs an assumption/contract the text does not mandate), `GAP_OR_CONFLICT` (important missing/conflicting obligation), or `UNASSESSABLE_FROM_SOURCES`. Give the exact source clause, a one-sentence reason and one concrete counterexample. **SPECIFIED is not IMPLEMENTED or PASSED.**

## 4. Apply the requirements to R1, R2 and R3 — no invented execution

| DDS position | Bounded audit question | Required boundary |
|---|---|---|
| **R1, initial** | Do Q0–Q5 / frozen S/T text let a **competent conventional implementation** pass V0 continuity and handle a **known V1 A/B conflict**, without EA by branding? | If R1 demonstrably PASSES, do **not** invent a necessary R2. 00F top-notch is a design, not evidence of native PASS; no vendor outcome is supplied. |
| **R2, repaired** | **If a real R1 failure exists**, are the same S/T rules precise enough to guide a strong, feasible repair, including source semantics, composition, scoped fallback and requalification? | The peer may learn its known R1 failure, search multiple configurations and tune to it. Record diagnosis, failed attempts, human engineering, tools, integration, verification, operations and amortization. `NOT_MEASURED ≠ 0`; a technical PASS is separate from full Cost–Risk–Effectiveness. No eligible demonstrated fail = `NOT_ADMITTED` as an actual run. |
| **R3, change not revealed** | **If an eligible predecessor actually PASSES and is frozen**, are the obligations strong enough to requalify when a subsequent material event arrives **without prior knowledge of the exact scored variant**? | Family/allowed ranges and general controls may be known; exact realization, seed and oracle held by independent custodian. Public **00F V8** can be discussed as an old example but **cannot** be scored as secret R3. Before selector commitment, freeze, exposure log and observed effects: `NOT_ADMITTED / NOT_EXECUTED`. |

There is no requirement to make a specific peer lose. A strong peer that detects and responds with equal/better cost and effect **removes any claimed EA differential**, even if the requirements themselves are coherent. If cost/effect data are missing, mark the comparative result `NO_CONCLUSION`. Do not presume zero cost, perfect preparation, universal visibility or a city-wide supercontroller.

## 5. Two falsifiers and the existing adverse result

**N1 — blanket safety is not mission success.** A candidate satisfies local collision avoidance by sending every actor to indefinite `HOLD` in **V0** (no material change), reports “safe” and declares S2 a PASS. Does the S/T specification **itself** reject this false-positive and require legitimate continuity with finite time/owner? Cite Q0/Q3/Q5.

**N2 — fake blinded differential.** A reviewer recycles the **published V8** as “unanticipated blind R3”, lets one participant tune specifically to V8 for free, and concludes that EA defeated the alternative. Identify the **foreknowledge/custody violation**, missing legitimate R2/R3 adaptation cost and missing real matched effect. Give the correct `INVALID_BLIND_CLAIM / NOT_ADMITTED` disposition.

**Mandatory evidence check (00L):** Read the corrected A14 JSONL for **00F**. `fire_slot=10`: reference and strong peer both `REQUALIFY`; `fire_slot=11`: both `EXECUTE_ALL`. The intentionally weak peer makes the wrong negative-branch decision. The shared strong peer **ties** the reference on this limited symbolic pair. It is **not V8 drift**, independent technology validation or proof EA wins. State this **adverse/tie** result, including its scope, even if you otherwise find good specification coverage.

**A23 countermodel boundary:** inspect whether any S2 “all S/T requirements satisfied, therefore all P1–P6 hold” claim would exceed [A23](https://github.com/dakleyer/structural-awareness-contributions/blob/b056bd621262edc3a026fd21780c866afb22b1d5/research/ecosystem-awareness/baseline/00K_A23_CANONICAL_REQUIREMENT_CONFORMANCE_SUFFICIENCY_P1_P6_v0.1.md). **P3/P5/P6 semantic implication is open**. You need not solve A23; flag unjustified extrapolation and any specific S2 dependency on it.

## 6. Submission, review history and owner disposition

1. **Acceptance:** Iván invites the person; the reviewer accepts scope, effort and a submission route, privately disclosing authorship/fixture interests, vendor interests and any prior exposure to variants or scoring keys. No independence or public credit is pre-awarded.
2. **One record:** Complete [REVIEW_RECORD_TEMPLATE.md](./REVIEW_RECORD_TEMPLATE.md) with all Q0–Q5, R1–R3, N1/N2, A14, A23 and conclusion fields. Preserve packet SHA, the frozen Contributions cut and original UC21 source cut.
3. **Choose intake before starting:**
   - **PRIVATE_INTAKE (default before explicit publication consent):** send one source-cited record and detailed disclosures through an owner-controlled restricted channel provided at invitation. Iván preserves the private evidence, author and revision history. No automatic publication follows.
   - **PUBLIC_PR (opt-in):** submit an approved, privacy-checked `REVIEWS/YYYY-MM-DD-REVIEW-ID-v0.1.md` in a pull request to `main`. GitHub username/account, filename, findings and PR metadata become **public on opening**, not only on merge. Do not include unapproved personal, employer-sensitive or private oracle/variant data. A review ID alone cannot anonymize an identified GitHub author.
4. **Public record if agreed:** A private review may later be represented by an expressly authorized, source-linked, redacted GitHub record or synthesis. Do not hide negative findings, imply that an internal review was publicly replicated, or overwrite another reviewer's evidence.
5. **Owner disposition:** Iván decides `ACCEPT / REVISE / DEFER / REJECT` per finding. Accepted method or requirement changes need separate controlled PRs; preserve the frozen inputs and inbound links.
6. **FG-TIDA boundary:** An approved synthesis may later inform UC21/Theme 13. Neither intake route, a PR nor a merge constitutes submission, endorsement, certification or automatic author credit.

**Complete when:** 6 cited gate decisions + 3 eligible/conditional DDS-position assessments + 2 probe decisions + exact A14 tie finding + A23 limitation + one falsifiable counterexample or reasoned absence + conflicts/independence/exposure record + one concrete recommendation. If a necessary premise cannot be verified, `UNDETERMINED` is an acceptable conclusion. No requirement is rewritten and no numerical performance claim is made.

**Allowed overall opinions:** `REQUIREMENTS_ADEQUATE_IN_REVIEW_SCOPE` / `REVISE_SPECIFICATION_BEFORE_TEST` / `UNDETERMINED_MISSING_EVIDENCE`. They concern **documentary adequacy only**; no independent results exist until a reviewer submits work.
