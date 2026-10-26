# Panodyssey Theme #17 → Challenge Map → 00J → UC #21: Working Traceability

**Status:** Public working crosswalk for discussion; not an adopted FG-TIDA deliverable, Panodyssey product assessment, or report of production failure.  
**Prepared:** 3 October 2026  
**Purpose:** Present the work developed with Olena Pavlenko and Alexandre Leforestier as one traceable package: public Panodyssey Theme #17 context, the three broad Panodyssey use cases, canonical Annex III challenge coverage, preliminary Terms of Reference (ToR) links, and the relationship to 00J and UC #21.

## 1. Starting point: Theme #17 and the Panodyssey case

[FG-TIDA Theme #17](https://github.com/FG-TIDA/themes/issues/17), proposed publicly by Alexandre Leforestier (Panodyssey), describes a production-side rights and identity chain for text. Its public description covers domain AI access rules; machine-readable discovery per publication; per-work rights declarations distinguishing indexing, RAG and training; timestamped audit history; and certified author identity. It identifies the agent-side identity and legal-representation link as a remaining interoperability problem.

This is a bounded publishing-sector reference, not a proxy for every publisher or creative-industry system. The public Theme #17 issue is the source for statements about the case. The crosswalk below describes what the case can help examine; it does not claim that Panodyssey has solved every mapped challenge or that the product has failed one.

## 2. Three broad Panodyssey use cases

In the September working exchange, the operational material was consolidated into three broad use cases. These are reusable problem statements grounded in the Panodyssey text-publishing context; they are not the three earlier evidence situations, and they are not three additional FG-TIDA use-case submissions.

| Panodyssey use case | Scope | Current evidence boundary |
|---|---|---|
| **UC1 — Authority and Permission Across the Lifecycle** | Follow a permission through grant, modification, restriction, revocation and revalidation. Ask whether the current permission governs the next action and whether the changed rights state has reached the downstream actor. | Publicly described rights declarations and modification history support part of the lifecycle question. Downstream receipt, interpretation and action-time applicability remain distinct questions. |
| **UC2 — Identity, Organisational Binding and Delegated Authority** | Connect a technical actor, crawler or agent to an accountable provider, organisation or principal, and to the authority it claims to exercise. | The publisher-side case establishes useful identity and rights references. Full interoperable determination of the acting and represented legal actors remains open. |
| **UC3 — Evidence of Authority Versus Evidence of Execution** | Distinguish evidence that a rights-holder expressed an intention or permission from evidence that an AI actor received, interpreted and complied with it. Preserve residual uncertainty so a decision can be appropriately bounded. | A rights declaration or audit history can evidence the publisher-side record; it does not alone prove downstream execution or compliance. |

**RAG is an emerging extension across these use cases, not a fourth use case or a claim of a completed capability.** It raises context questions alongside indexing and training permissions and should be treated as future-facing unless supported by separately reviewed public evidence.

## 3. How the case, challenge map and scenarios fit together

The material is nested by analytical level:

1. **Case context — Theme #17:** a public, bounded publishing-sector example.
2. **Three Panodyssey use cases:** reusable operational problem statements drawn from that context.
3. **Canonical challenges and ToR traceability:** a crosswalk that shows which challenge dimensions the use cases exercise and where the preliminary ToR anchors sit.
4. **[00J — “The Author Pays for Their Own Work”](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md):** a focused, fictional rights-provenance inversion scenario. It is closest to Panodyssey UC3, with overlap into UC1 (current source rights) and UC2 (identity and claim attribution). It is not a fourth Panodyssey use case and is not an incident report about Panodyssey or TEMS.
5. **[00J-A01 — Panodyssey Notice / TEMS trajectory](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00J_A01_PANODYSSEY_TEMS_RIGHTS_PORTABILITY_IMPLEMENTATION_PROFILE_v0.1_DRAFT.md):** a source-reviewed but unexecuted implementation trajectory. It distinguishes the public source baseline (PANO-H0), a constructed defended peer (PANO-H1), and the same frozen peer under a synthetic resolver/identifier/lineage change (PANO-H2).
6. **[UC #21](https://github.com/FG-TIDA/use-cases/issues/21), “When the controls work but the system fails”:** a broader FG-TIDA proposal with six failure scenarios and three implementation walkthroughs. UC #21 S6 addresses a rights-holder/access/generation/claim/registry/relying-service branch with Q0–Q5 gates. 00J is related to that branch, but is not identical to it. Steven’s Step Functions/RDS walkthrough is a separate route within UC #21.

**This is nested traceability with feedback, not circular proof.** A case helps identify challenges; challenges are related to ToR provisions; use cases make selected challenges operational; a scenario such as 00J can provide a focused test slice. Evidence from a properly specified and reviewable test may then refine the challenge coverage. The case does not prove its own mapping, and a designed scenario does not count as execution evidence.

The 00J evidence boundary remains in force: its fixture is synthetic, its implementation trajectory is unexecuted, and it makes no Panodyssey/TEMS failure claim. Public product statements in this crosswalk rely on the public Theme #17 record, not private correspondence.

## 4. Collaboration and evolution of the working map

The consolidated result reflects an iterative working process with Olena Pavlenko and Alexandre Leforestier:

- **15–17 September:** the initial map identified three evidence situations: a permission changes or is revoked; AI/crawler identity is uncertain; or rights-holder intent is visible but downstream compliance is not established. The key distinction was between evidence of intent and evidence of execution. The discussion also separated a reusable cross-sector challenge taxonomy from a concrete text-publishing evidence layer.
- **22–23 September:** the working method was set as **case study → challenge map → ToR mapping → use cases**. The case should ground the challenge analysis; use cases should operationalise selected problems rather than determine the problem statement. The group aimed for a compact package and reviewable coverage labels.
- **24 September:** a first internal consolidation draft was circulated, followed by challenge-coverage and 00J technical mapping work.
- **28–29 September:** the three broad Panodyssey use cases were retained; ToR mapping was kept as a traceability layer; RAG was treated as an emerging extension rather than a fourth use case. The coverage map was aligned to the existing Annex III challenge identifiers S1–S14.
- **30 September:** the material was considered ready to present as a use-case submission. This crosswalk records the working result; it does not claim formal submission, endorsement or adoption.

This is a synthesis of outcomes, not a reproduction of private email. The internal first-consolidation draft was not intended for external circulation. This public-facing crosswalk therefore uses the public Theme #17 record for Panodyssey facts and presents the collaboration history only as process provenance.

## 5. Canonical Annex III challenge coverage and preliminary ToR mapping

The table uses the existing challenge identifiers and labels in the public working [Annex III](https://github.com/dakleyer/structural-awareness-contributions/blob/main/submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/04_ANNEX_III_Challenges_Exposed_by_the_Case.md). The labels below describe relevance and coverage in this bounded case, not product maturity or a judgement of legal compliance.

| Annex III challenge | Panodyssey use case and coverage | Primary preliminary ToR anchors | Supporting |
|---|---|---|---|
| **S1 — Authority provenance & current applicability** | UC1 — **Direct / partial**. State and modification history are evidenced; downstream recognition and action-time applicability remain open. | 4.3; A.1.2; A.2.2 | A.2.7 |
| **S2 — Preference fidelity & reviewable decision basis** | Open in the current three UCs; relevant where machine-readable permissions only partly represent rights-holder intent. | 3.4; 4.1; A.2.1 | A.2.4 |
| **S3 — Regime, context, escalation & bounded escape path** | Conditional / emerging, especially for training, RAG and indexing context changes; not fully evidenced by the current use-case claims. | 4.3; A.2.2; A.2.4; A.2.8 | — |
| **S4 — Human-inclusive oversight authority & capacity** | UC3 — **Conditional**. The decision point is clear when evidence is insufficient; oversight capacity is not established by the Panodyssey layer. | 3.4; 4.3; 4.5; A.2.4 | — |
| **S5 — Operational indeterminacy & containment** | UC3 and UC1 — **Direct / partial**. Uncertainty about receipt, interpretation or execution is in scope; containment is not attributed to Panodyssey unless demonstrated. | 3.4; 4.3 | A.2.2; A.2.7 |
| **S6 — Interoperable, privacy-preserving trust determination** | UC2 — **Direct / partial**. Machine-readable rights and actor references exist; full interoperable determination remains open. | 3.4; 4.2; 4.4; A.2.5 | — |
| **S7 — Identity & representation link** | UC2 — **Direct / partial**. A technical crawler/agent identity does not necessarily establish its accountable organisation or legal actor. | 2; 4.2; A.1.1; A.1.2 | — |
| **S8 — Bounded subdelegation & non-amplification** | Open; the current three UCs do not establish an onward agent, tool or intermediary delegation chain. | A.1.2; 4.3 | A.2.2; A.2.7 |
| **S9 — Multi-principal composition, non-substitution & conflict** | Open; potentially relevant to author, publisher, platform, provider and territorial-rights constraints. | 2; 4.2; A.2.1; A.2.5; A.2.7 | — |
| **S10 — Commitment state, material change & normal escalation** | UC1 — **Direct / partial**. Change is evidenced; downstream revalidation remains open. | 4.3; A.2.2 | A.2.7 |
| **S11 — Policy, objective & preference integrity across domains** | Open / emerging; relevant to distinct training, RAG and indexing permissions, not a completed current-state claim. | 4.4; A.1.5; A.2.5 | 4.2 |
| **S12 — Accountability, challenge & repair** | UC3 — **Direct / partial**. Rights declaration and history can be reconstructed; downstream behaviour may remain unknown. | 3.4; 4.5; A.2.4 | A.2.2 |
| **S13 — Authority history vs intervention history** | UC1 — **Direct / partial**. Prior and current permission states can be distinguished; later intervention history would be an extension. | 4.3; A.1.2; A.2.4; A.2.7 | — |
| **S14 — Evidence-to-decision assessment** | UC2 / UC3 — **Direct / partial**. The question is whether evidence is sufficient for a decision, not merely whether evidence exists. | 3.4; 4.5; A.2.2; A.2.4 | — |

On this preliminary reading, **eight challenges are directly exercised** (S1, S5, S6, S7, S10, S12, S13 and S14); **S4 is conditional**; and **S2, S3, S8, S9 and S11 remain open or future-facing** (with S3 and S11 also emerging context areas). “Direct” means the problem is exercised by the use case; “partial” means the public evidence does not establish the full challenge outcome.

**Case-level preliminary ToR anchors:** 3.3 and 4.1. Other clauses in the table are selective challenge-level links, not a claim of complete ToR coverage. The [live FG-TIDA Terms of Reference](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx) is authoritative. The linked [Annex IV mapping](https://github.com/dakleyer/structural-awareness-contributions/blob/main/submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/05_ANNEX_IV_FG-TIDA_ToR_Mapping_and_Traceability.md) is a public pre-freeze working annex, not an adopted deliverable; recheck the live ToR before formal external use.

## 6. Three initial evidence situations and their relationship to the use cases

These were starting situations used to organise evidence, not the final three broad use cases above.

| Initial evidence situation | Main Panodyssey use case(s) | Related Annex III challenges | 00J / UC #21 connection |
|---|---|---|---|
| Permission changes or is revoked after prior authorisation | UC1 | S1, S10, S13; S5 when evidence is incomplete or conflicting | 00J examines current rights and changing state; UC #21 S6 Q0, Q1, Q4 and Q5 are related. |
| AI/crawler identity is uncertain or insufficiently verified | UC2 | S6, S7, S14 | 00J asks whether actor, represented principal and bounded authority support a claim; UC #21 S6 Q0, Q1 and Q5 are related. |
| Rights-holder intent is evidenced but AI compliance cannot be established | UC3 | S5, S12, S14; S4 only if human decision is required | 00J separates source rights, generation, downstream claim, replication and enforcement; UC #21 S6 Q2–Q5 are related. |

The narrower 00J question is whether the evidence at a final decision supports the exact rights proposition being enforced against the exact subject, use and time. A generation record, valid signature or repeated copy of a downstream claim does not by itself establish source independence or rights authority.

## 7. Evidence, status and interpretation boundaries

- **Theme #17** is the public source for the Panodyssey case context and the problem statement as proposed by its author.
- **The three use cases and challenge coverage** are a working synthesis of the collaboration, not an adopted FG-TIDA result or a product maturity assessment.
- **00J** is a fictional reference scenario. Its facts are synthetic or explicitly inferred; it is not a Panodyssey/TEMS incident.
- **00J-A01** is source-reviewed design analysis, unexecuted and not a product benchmark.
- **UC #21** is an open use-case proposal. Its scenarios and implementation walkthroughs retain their own evidence status; S6 and 00J are related but not interchangeable.
- **Annex III** is a public working challenge framework. **Annex IV** is a public pre-freeze ToR mapping. Neither status implies adoption by FG-TIDA.
- Private emails and the internal Challenge Pack are not public evidence. The timeline above is a concise account of collaboration and decisions; factual claims about Panodyssey remain tied to public references.

## 8. Public references

- [FG-TIDA Theme #17 — Digital Rights Infrastructure for Text](https://github.com/FG-TIDA/themes/issues/17)
- [FG-TIDA UC #21 — When the controls work but the system fails](https://github.com/FG-TIDA/use-cases/issues/21)
- [00J — Rights-Provenance Inversion / “The Author Pays for Their Own Work”](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00J_FAILURE_MODE_RIGHTS_PROVENANCE_INVERSION_v0.1_DRAFT.md)
- [00J-A01 — Panodyssey Notice / TEMS Rights-Portability Implementation Trajectory](https://github.com/dakleyer/structural-awareness-contributions/blob/main/research/ecosystem-awareness/baseline/00J_A01_PANODYSSEY_TEMS_RIGHTS_PORTABILITY_IMPLEMENTATION_PROFILE_v0.1_DRAFT.md)
- [Annex III — Challenges Exposed by the Case](https://github.com/dakleyer/structural-awareness-contributions/blob/main/submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/04_ANNEX_III_Challenges_Exposed_by_the_Case.md)
- [Annex IV — FG-TIDA ToR Mapping and Traceability (working reference)](https://github.com/dakleyer/structural-awareness-contributions/blob/main/submissions/itu-fg-tida/2026-theme-contributions/delegated-authority-os-under-context-change/05_ANNEX_IV_FG-TIDA_ToR_Mapping_and_Traceability.md)
- [FG-TIDA Terms of Reference](https://www.itu.int/en/ITU-T/focusgroups/tida/Pages/ToR.aspx)

**Preparation note:** This public crosswalk consolidates the September working map, the collaboration’s email outcomes, the public Theme #17 case, and the existing 00J / UC #21 references. It keeps private correspondence out of the evidence chain and distinguishes the case, challenge analysis, use cases and synthetic test scenario.
