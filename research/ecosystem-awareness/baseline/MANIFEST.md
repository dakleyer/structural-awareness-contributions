# Ecosystem Awareness — Publication Freeze Manifest

**Freeze date:** 11 September 2026  
**Repository:** `dakleyer/structural-awareness-contributions`  
**Path:** `research/ecosystem-awareness/`

## Purpose of this freeze

This directory is a **public reference freeze**. Its purpose is to create a stable, dated and citable point in the development of Ecosystem Awareness so later changes can be compared against a preserved architecture rather than silently rewriting the earlier record.

The freeze applies to the **published corpus snapshot**, not to all future research.

It does not mean:

- final architecture freeze;
- implementation validation;
- standards adoption;
- ITU-T endorsement;
- NIST acceptance;
- conformance certification; or
- a claim of proven novelty.

## Frozen artifacts

1. `README.md` — canonical public index and high-level statement.
2. `FOUNDATIONAL_THEORY_v0.4_PUBLIC_FREEZE.md` — public preservation of the v0.4 foundational theory.
3. `ARCHITECTURE_BENCHMARK_v0.4_PUBLIC_FREEZE.md` — public preservation of the v0.4 architecture benchmark and differentiation audit.
4. `UC-EA-01_v0.3_FROZEN.md` — frozen architecture-validation profile for action-time operating-frame requalification.
5. `PUBLIC_PROVENANCE_2026-09-08.md` — controlled public provenance snapshot.
6. `MANIFEST.md` — this publication-control record.

## Status by source artifact

| Artifact | Source status preserved by this publication |
|---|---|
| Foundational Theory v0.4 | Working foundational architecture; public snapshot frozen for citation |
| Architecture Benchmark v0.4 | Provisional completeness/differentiation audit; novelty hypothesis, not proof |
| UC-EA-01 v0.3 | Frozen internal architecture-validation profile; not FG-TIDA submission |
| Public Provenance 2026-09-08 | Controlled living evidence snapshot; this dated edition is preserved |

## Change rule

The list above identifies the **11 September 2026 publication snapshot**, not immutable ownership of the current pathname forever. In particular, `README.md` means the README state captured by that snapshot and recoverable through Git history; the current routed README may evolve later under `DOCUMENT_CONTROL.md` without rewriting the historical freeze.

These frozen files should not be silently rewritten to reflect later architecture decisions.

Material evolution should be published as a later version or later dated snapshot, with the earlier freeze retained in repository history.

Minor corrections that do not alter substantive meaning should still be made through ordinary Git commits so the public provenance remains visible.

For controlled Drive-backed sources, use the applicable freeze/maintenance manifest's Drive file ID + `revisionId` as the historical exact-content anchor. For current public working successors and routed pages, cite the Git commit containing the public state used. See [Canonical Corpus Manifest — Provenance bridge](./CANONICAL_CORPUS_MANIFEST.md#provenance-bridge--controlled-source-anchors-versus-current-public-citations).

## Public claim rule

When referencing this corpus externally, use formulations such as:

- “candidate pre-standardization architecture”;
- “working architecture”;
- “public reference freeze”;
- “contributor-level FG-TIDA work”; or
- “research / architecture-validation profile”.

Do not represent this corpus as an adopted standard, formal ITU-T deliverable or certified implementation.

## Stewardship

The corpus is maintained in the public research context of **Tegrity.AI**, an initiative of **The Integral Management Society, a Swiss non-profit association**.
