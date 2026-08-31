# TIDA — Delegated Authority OS under Context Change

## Public pre-freeze working package

- **Updated:** 1 September 2026
- **Status:** Public working material linked to the FG-TIDA theme-development discussion; not an adopted or endorsed FG-TIDA deliverable
- **Purpose:** Present the current candidate case and its annexes in one readable, linkable Markdown package for collaborative pre-freeze review.

## Start here

1. **Current main review file:** [Main case v0.8 — TIDA — Delegated Authority OS under Context Change](01_TIDA_Delegated_Authority_OS_under_Context_Change_v0.8.md)
   - [Purpose — what this working case is for](01_TIDA_Delegated_Authority_OS_under_Context_Change_v0.8.md#purpose)
   - [Ideal pre-freeze conditions — 3 + 1](01_TIDA_Delegated_Authority_OS_under_Context_Change_v0.8.md#prefreeze-conditions)
   - v0.8 deliberately puts the purpose and the 3 + 1 design conditions before the logistics instantiation.
2. **Prior main version:** [v0.7](01_TIDA_Delegated_Authority_OS_under_Context_Change_v0.7.md)
3. **Earlier main version:** [v0.6](01_TIDA_Delegated_Authority_OS_under_Context_Change_v0.6.md)

## Supporting documents

- [Annex I v0.3 — Minimal Operational Case Outline](02_ANNEX_I_Minimal_Operational_Case_Outline_v0.3.md)
- [Annex II v1.2 — Why the Minimal Case Is Extensible](03_ANNEX_II_Case_Extensibility_Upward_Downward_Horizontal_v1.2.md)
- [Annex III v1.3 — Challenges Exposed by the Case](04_ANNEX_III_PostFreeze_Solution_Challenges_v1.3.md)
- [Annex IV v1.0 — FG-TIDA ToR Mapping and Traceability](05_ANNEX_IV_FG-TIDA_ToR_Mapping_and_Traceability_v1.0.md)
- [Annex V v1.1 — Adjacent Standards and Research Relevance](06_ANNEX_V_Adjacent_Standards_and_Research_Relevance_v1.1.md)

The package is intentionally modular. The main case defines the common test surface and current pre-freeze design view; Annex I fixes the minimal operational instantiation; Annex II tests bounded extensibility; Annex III preserves the solution-challenge surface; Annex IV maps those challenges to the FG-TIDA Terms of Reference; and Annex V identifies controlled interfaces with adjacent standards and research work.

## Current 3 + 1 design view

v0.8 treats the following as **ideal design conditions for a candidate intended for possible shared/cross-theme use, not as agreed FG-TIDA requirements or exclusion rules for other cases**:

1. **Multi-audience intelligibility** — a shared reference case gains value when its core problem remains understandable to the audiences expected to use it.
2. **Bounded extensibility** — desirable for reusable/shared cases; the case should reveal how far its core concepts survive controlled changes and where another case is preferable. A narrow sector-specific case may still be highly valuable without this property.
3. **FG-TIDA mandate adequacy and traceability** — material presented as an FG-TIDA case should remain defensibly connected to the ToR and existing theme interfaces.
4. **Declared governing regime(s) for authority determinations** — following [Pam Dixon’s Theme #16 clarification](https://github.com/FG-TIDA/themes/issues/16#issuecomment-5481112607), a governing regime should be declared whenever validity, standing, scope, revocation or act-time authority is being tested. A single-regime case is valid; materially different regimes can form a controlled family of variants.

This view is compatible with **one broadly reusable case, a family of regime-specific variants, narrowly bounded sector cases, or several complementary cases**.

## Why the case is solution-neutral

The candidate case fixes common facts, authority objects, decisions, interfaces, evidence and validation questions needed for comparable testing. It does **not** prescribe a vendor, product, agent framework, protocol, identity technology, model, optimizer, digital twin, data architecture or implementation stack.

That leaves companies, research teams, open-source communities and other solution providers room to propose and compare concrete technologies while existing FG-TIDA themes test whether their requirements compose against the same facts.

## Provenance note

Operational lineage: **xSeil (field deployment, 2016–2017) → Car Evolution (urban-mobility formalization, 2023) → Tegrity.AI Minimal Agentic Control Architecture / Minimum Sufficient Control (2026) → current candidate case**. This is provenance only; readers do not need those projects to use the case, and validation does not transfer between stages. The related FG-AI4SSC contribution was posted as Input Document `FGAI4SSC-I-097`; posting does not imply adoption or endorsement.

## Source custody and version continuity

| Review document | Continuity note |
|---|---|
| Main case v0.8 | Reorders the public narrative so purpose and 3 + 1 ideal conditions come first; compresses provenance to a note; preserves the substantive restricted case and challenge surface |
| Main case v0.7 | Introduced the neutral 3 + 1 readiness framing and Pam Dixon governing-regime clarification |
| Main case v0.6 | Preserved source-lineage and solution-neutral boundary |
| Annex I v0.3 | Controlled minimal operational case outline |
| Annex II v1.2 | Controlled bounded-extensibility analysis |
| Annex III v1.3 | Controlled challenge surface |
| Annex IV v1.0 | Controlled FG-TIDA ToR mapping |
| Annex V v1.1 | Controlled adjacent-standards/research interface note |

Earlier versions remain public and unchanged. Git history records the delta between review versions.

## Current review questions

- Does the opening make clear that the artifact is a shared test surface before readers encounter the logistics instantiation?
- Are D1 and D2 appropriately framed as ideal qualities rather than exclusion criteria?
- Are D3 and the governing-regime +1 condition stated narrowly enough for FG-TIDA use?
- Does the case remain small enough for cross-theme discussion while exposing authority, context-change and oversight seams?
- Where should this case stop and a narrower or different complementary case be preferred?

## Claim boundary

This package records a proposal for review. It makes no claim of FG-TIDA or FG-AI4SSC adoption, endorsement, validation, agenda inclusion or incorporation into an ITU-T deliverable. Publication in this repository and a discussion link do not constitute an ITU submission or formal contribution number.
