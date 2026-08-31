# TIDA — Delegated Authority OS under Context Change

## Public pre-freeze working package

- **Updated:** 1 September 2026
- **Status:** Public working material linked to the FG-TIDA theme-development discussion; not an adopted or endorsed FG-TIDA deliverable
- **Purpose:** Present the current candidate case and its annexes in one readable, linkable Markdown package for collaborative pre-freeze review.

## Documents for review

1. **Current main review file:** [Main case v0.7 — TIDA — Delegated Authority OS under Context Change](01_TIDA_Delegated_Authority_OS_under_Context_Change_v0.7.md)
   - Direct review point: [Section 6 — Proposed pre-freeze readiness conditions](01_TIDA_Delegated_Authority_OS_under_Context_Change_v0.7.md#6-proposed-pre-freeze-readiness-conditions)
   - v0.7 preserves the substantive v0.6 case while reframing the earlier D1–D3 case-design gates as neutral ideal pre-freeze readiness conditions and adding the governing-regime clarification from the Theme #16 authority-interface discussion.
2. **Prior main version:** [Main case v0.6 — TIDA — Delegated Authority OS under Context Change](01_TIDA_Delegated_Authority_OS_under_Context_Change_v0.6.md)
3. [Annex I v0.3 — Minimal Operational Case Outline](02_ANNEX_I_Minimal_Operational_Case_Outline_v0.3.md)
4. [Annex II v1.2 — Why the Minimal Case Is Extensible](03_ANNEX_II_Case_Extensibility_Upward_Downward_Horizontal_v1.2.md)
5. [Annex III v1.3 — Challenges Exposed by the Case](04_ANNEX_III_PostFreeze_Solution_Challenges_v1.3.md)
6. [Annex IV v1.0 — FG-TIDA ToR Mapping and Traceability](05_ANNEX_IV_FG-TIDA_ToR_Mapping_and_Traceability_v1.0.md)
7. [Annex V v1.1 — Adjacent Standards and Research Relevance](06_ANNEX_V_Adjacent_Standards_and_Research_Relevance_v1.1.md)

The package is intentionally modular: the main case states the candidate shared problem and the current pre-freeze readiness view; Annex I fixes the minimal operational case; Annex II tests bounded extensibility; Annex III preserves the solution-challenge surface; Annex IV maps those challenges to the FG-TIDA Terms of Reference; and Annex V identifies controlled interfaces with adjacent standards and research work.

## Current pre-freeze readiness view: 3 + 1

The v0.7 main note treats the following as **ideal working conditions for discussion, not agreed FG-TIDA requirements** and not criteria designed only for this logistics case:

1. **Multi-audience intelligibility** — the case should remain understandable across user, policy, standards/architecture and implementation audiences.
2. **Bounded extensibility** — the case should be able to grow, shrink or move across domains without silently redefining its core concepts; where that fails, the boundary should be recorded and another case used.
3. **FG-TIDA mandate adequacy and traceability** — relevant facts and challenges should remain defensibly linked to the official ToR and existing theme interfaces.
4. **Declared governing regime(s) for authority determinations** — following [Pam Dixon’s Theme #16 clarification](https://github.com/FG-TIDA/themes/issues/16#issuecomment-5481112607), the governing legal regime for each mandate whose authority is tested should be a declared case fact. A single-regime case can be valid; materially different regimes can form a controlled family of regime-specific variants.

This 3 + 1 view is deliberately compatible with **one case, a family of regime-specific variants, or several complementary cases**. It is a readiness lens, not a proposal that FG-TIDA select one universal frozen case.

## Central lineage to review

> **xSeil (field deployment, 2016–2017) → Car Evolution (urban-mobility formalization, 2023) → Tegrity.AI Minimal Agentic Control Architecture concept / Minimum Sufficient Control (2026) → current FG-TIDA candidate case.**

The formal 2026 smart-cities contribution is *Minimum Sufficient Control as an Architectural Property of AI-enabled Urban Systems*, posted by the ITU-T FG-AI4SSC Secretariat as **Input Document `FGAI4SSC-I-097`**. In this package, **MACA** is a descriptive lineage label for the *Minimal Agentic Control Architecture* concept; it is not an ITU-defined term and must not be presented as adopted, endorsed or validated by ITU.

## Deliberate architecture boundary

The candidate model is intentionally minimal and solution-neutral. It fixes the common facts, authority objects, decisions, interfaces, evidence and validation questions needed for comparable testing. It does **not** prescribe a vendor, product, agent framework, protocol, identity technology, model, optimizer, digital twin, data architecture or implementation stack.

This leaves participating companies, research teams, open-source communities and other solution providers room to propose and compare concrete technologies. FG-TIDA can address terminology, use cases, requirements, assessment, reference architectures and interoperability without selecting the implementation stack; its Terms of Reference explicitly place agentic-AI protocols outside scope. Case-level tests and stress tests likewise do not prescribe detailed AI-model training or testing methods.

## Source custody and version continuity

| Review document | Controlled source / continuity note | Source SHA-256 |
|---|---|---|
| Main case v0.7 | Additive Markdown version based on public v0.6; introduces the neutral 3 + 1 readiness framing and governing-regime clarification; v0.6 remains preserved | Version history and Git commit provide the public delta |
| Main case v0.6 | `tida-delegated-authority-os-under-context-change-v0.5.md`, expanded additively for this review | `1C347F5106E2E34E3AB57067AA21AF51B92369DF7BF314091929D11BC268D0F1` |
| Annex I v0.3 | `02_ANNEX_I_Minimal_Operational_Case_Outline_v0.3.docx` | `332DA783C5A776351361B5A137C085DFDA75B6525E44991DBE4C7852B9293593` |
| Annex II v1.2 | `03_ANNEX_II_Case_Extensibility_Upward_Downward_Horizontal_v1.2.docx` | `6EF93CA9DD7B276F0D87FDAF7455C764B29EFE74FFCBAC3CCA3CEBF27D2ECC86` |
| Annex III v1.3 | `04_Annex_III_PostFreeze_Solution_Challenges_v1.3.docx` | `606C0C0783D0418DB8AFCE15F1B0431CEA01F27D8C951EC383D056FBE1772DFC` |
| Annex IV v1.0 | `05_Annex_IV_FG-TIDA_ToR_Mapping_and_Traceability_v1.0.docx` | `8067F6BB2CD717CE410ED7361262F222C119424E17EA80F15147C619C262ACFB` |
| Annex V v1.1 | `06_Annex_V_Adjacent_Standards_and_Research_Relevance_v1.1.docx` | `D15D3C4AC4BF6C480FD8B95D7F5D4A0273FA766DAE1A26A7A553A4EDC690B7DC` |

The Markdown annexes preserve the substantive text, tables and hyperlinks of the controlled Word sources. The Word files remain the source-format records; these Markdown files are the public review layer. v0.7 is intentionally additive and does not overwrite v0.6.

## Final-review questions

- Are the 3 + 1 readiness conditions useful as neutral ideal conditions for this case and for alternative/complementary cases?
- Is the governing-regime condition stated narrowly enough to support authority determinations without turning multijurisdictionality into a mandatory property of every case?
- Is the case small enough to be shared across themes but deep enough to expose authority, context-change and oversight seams?
- Does the solution-neutral boundary leave sufficient room for companies and other implementers to propose concrete technologies?
- Should Annex III become a set of one-page validation units with specific requirements, evidence, test and stress-test conditions, and criteria, or remain deliberately general as group guidance?
- Which facts and challenge subset should be frozen first in this case, if any, while alternative or complementary cases continue to mature?

## Claim boundary

This package records a proposal for review. It makes no claim of FG-TIDA or FG-AI4SSC adoption, endorsement, validation, agenda inclusion or incorporation into an ITU-T deliverable. Publication in this repository and a discussion link do not constitute an ITU submission or formal contribution number.
