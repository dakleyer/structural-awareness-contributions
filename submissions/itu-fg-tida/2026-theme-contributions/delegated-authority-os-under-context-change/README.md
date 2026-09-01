# TIDA — Delegated Authority OS under Context Change

## Public pre-freeze working package

- **Prepared:** 31 August 2026
- **Status:** Public working material linked to the FG-TIDA theme-development discussion; not an adopted or endorsed FG-TIDA deliverable
- **Purpose:** Present the current candidate case and its annexes in one readable, linkable Markdown package for collaborative pre-freeze review.

## Documents for review

1. [Main working structure v0.9 — Candidate Shared Frozen Case](01_TIDA_Delegated_Authority_OS_under_Context_Change_v0.9.md)
2. [Annex I v0.3 — Minimal Operational Case Outline](02_ANNEX_I_Minimal_Operational_Case_Outline_v0.3.md)
3. [Annex II v1.2 — Why the Minimal Case Is Extensible](03_ANNEX_II_Case_Extensibility_Upward_Downward_Horizontal_v1.2.md)
4. [Annex III v1.3 — Challenges Exposed by the Case](04_ANNEX_III_PostFreeze_Solution_Challenges_v1.3.md)
5. [Annex IV v1.0 — FG-TIDA ToR Mapping and Traceability](05_ANNEX_IV_FG-TIDA_ToR_Mapping_and_Traceability_v1.0.md)
6. [Annex V v1.1 — Adjacent Standards and Research Relevance](06_ANNEX_V_Adjacent_Standards_and_Research_Relevance_v1.1.md)

The six-document package is intentionally modular: the main case states the candidate shared problem; Annex I fixes the minimal operational case; Annex II tests bounded extensibility; Annex III preserves the solution-challenge surface; Annex IV maps those challenges to the FG-TIDA Terms of Reference; and Annex V identifies controlled interfaces with adjacent standards and research work.

## Central lineage to review

> **xSeil (field deployment, 2016–2017) → Car Evolution (urban-mobility formalization, 2023) → Tegrity.AI Minimal Agentic Control Architecture concept / Minimum Sufficient Control (2026) → current FG-TIDA candidate case.**

The formal 2026 smart-cities contribution is *Minimum Sufficient Control as an Architectural Property of AI-enabled Urban Systems*, posted by the ITU-T FG-AI4SSC Secretariat as **Input Document `FGAI4SSC-I-097`**. In this package, **MACA** is a descriptive lineage label for the *Minimal Agentic Control Architecture* concept; it is not an ITU-defined term and must not be presented as adopted, endorsed or validated by ITU.

## Deliberate architecture boundary

The candidate model is intentionally minimal and solution-neutral. It fixes the common facts, authority objects, decisions, interfaces, evidence and validation questions needed for comparable testing. It does **not** prescribe a vendor, product, agent framework, protocol, identity technology, model, optimizer, digital twin, data architecture or implementation stack.

This leaves participating companies, research teams, open-source communities and other solution providers room to propose and compare concrete technologies. FG-TIDA can address terminology, use cases, requirements, assessment, reference architectures and interoperability without selecting the implementation stack; its Terms of Reference explicitly place agentic-AI protocols outside scope. Case-level tests and stress tests likewise do not prescribe detailed AI-model training or testing methods.

## Source custody

| Review document | Controlled source | Source SHA-256 |
|---|---|---|
| Main working structure v0.9 | `01_Main_Document_Case_Purpose_and_PreFreeze_Working_Structure_v1.0.docx`, preserved as the structural baseline with limited 3+1/provenance updates | Public version note and Git history record the delta |
| Annex I v0.3 | `02_ANNEX_I_Minimal_Operational_Case_Outline_v0.3.docx` | `332DA783C5A776351361B5A137C085DFDA75B6525E44991DBE4C7852B9293593` |
| Annex II v1.2 | `03_ANNEX_II_Case_Extensibility_Upward_Downward_Horizontal_v1.2.docx` | `6EF93CA9DD7B276F0D87FDAF7455C764B29EFE74FFCBAC3CCA3CEBF27D2ECC86` |
| Annex III v1.3 | `04_Annex_III_PostFreeze_Solution_Challenges_v1.3.docx` | `606C0C0783D0418DB8AFCE15F1B0431CEA01F27D8C951EC383D056FBE1772DFC` |
| Annex IV v1.0 | `05_Annex_IV_FG-TIDA_ToR_Mapping_and_Traceability_v1.0.docx` | `8067F6BB2CD717CE410ED7361262F222C119424E17EA80F15147C619C262ACFB` |
| Annex V v1.1 | `06_Annex_V_Adjacent_Standards_and_Research_Relevance_v1.1.docx` | `D15D3C4AC4BF6C480FD8B95D7F5D4A0273FA766DAE1A26A7A553A4EDC690B7DC` |

The Markdown annexes preserve the substantive text, tables and hyperlinks of the controlled Word sources. The Word files remain the source-format records; these Markdown files are the public review layer.

## Final-review questions

- Is the lineage clear without implying that later concepts inherit validation from earlier deployments?
- Is “MACA” useful as a descriptive label, while the formal input title and `FGAI4SSC-I-097` remain unambiguous?
- Is the case small enough to be shared across themes but deep enough to expose authority, context-change and oversight seams?
- Does the solution-neutral boundary leave sufficient room for companies and other implementers to propose concrete technologies?
- Should Annex III become a set of one-page validation units with specific requirements, evidence, test and stress-test conditions, and criteria, or remain deliberately general as group guidance?
- Which facts and challenge subset should be frozen first?

## Claim boundary

This package records a proposal for review. It makes no claim of FG-TIDA or FG-AI4SSC adoption, endorsement, validation, agenda inclusion or incorporation into an ITU-T deliverable. Publication in this repository and a discussion link do not constitute an ITU submission or formal contribution number.
