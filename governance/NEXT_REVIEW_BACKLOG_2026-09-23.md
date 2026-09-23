# Next Review Backlog — 23 September 2026

> **Maintenance backlog only.** This is not a canonical architecture document, benchmark result or publication-status statement. It records items deliberately deferred from the 23 September surgical coherence/integrity pass.

## 1. Deferred priority — baseline / FG-TIDA duplicate disposition

**Not executed in the current pass.** Review case by case before creating stubs, deleting copies or changing ownership.

Exact-name pairs measured in the current tree:

| Baseline copy | FG-TIDA copy | Current relation | Next review question |
|---|---|---|---|
| `baseline/DAOS_EA_USE_CASES_MASTERCLASS_v0.1.md` | `fg-tida/cases/DAOS_EA_USE_CASES_MASTERCLASS_v0.1.md` | Different blobs | Which copy is source/provenance and which is the current package reader? |
| `baseline/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md` | `fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md` | Different blobs | Reconcile content before choosing canonical package location/stub. |
| `baseline/FG_TIDA_ECOSYSTEM_AWARENESS_PUBLIC_FOOTPRINT_2026-09-08.part01.md` | `fg-tida/provenance/FG_TIDA_ECOSYSTEM_AWARENESS_PUBLIC_FOOTPRINT_2026-09-08.part01.md` | Byte-identical at review time | Decide whether baseline remains preserved source or becomes redirect/stub. |
| `baseline/PUBLIC_PROVENANCE_2026-09-08.md` | `fg-tida/provenance/PUBLIC_PROVENANCE_2026-09-08.md` | Byte-identical at review time | Same provenance decision. |
| `baseline/EA-ITP-01_v0.1_FROZEN.md` | `fg-tida/tests/EA-ITP-01_v0.1_FROZEN.md` | Byte-identical at review time | Preserve freeze ownership before deciding which side may be a stub. |

Do **not** assume that `fg-tida/` must always be the only physical home. Frozen/control provenance may justify the inverse relation.

## 2. Presentation finalization — still on hold

Do not replace the repository canonical PPTX/PDF until the final text pass is approved.

Remaining text-only items:

1. Cover attribution / licence:  
   `CC BY-SA 4.0 · Iván Abril Palma · Tegrity.AI / The Integral Management Society`.
2. Slide 9 evidence boundary: state explicitly that Benchmark v0.2 covers EA / EA-H1–EA-H4; Gradient, Repositioning, Citizenship and choreography do not yet have matched comparator execution.
3. Slide 9 routing: add direct routes to the Objective-Conditioned Agentic Gradient Law and Canonical MSCA Operation & Repositioning; update `PRESENTATION_MANIFEST.md` accordingly.
4. Slide 4: add 00G Bar-to-Napoleon as the role-drift/signalling/repositioning reference scenario, clearly marked synthetic/candidate.
5. Slide 8: change `Act` to `Owner acts` if it still appears in the final editable deck.
6. Final page/section-number consistency check.
7. Only after approval: replace both stable canonical files in `presentations/ecosystem-positioning/` together (PPTX + PDF).

## 3. Evidence-scope follow-up

The current 00D canonical benchmark directly covers the EA differential EA-H1–EA-H4 under B0–B3.

Before presenting Gradient / Repositioning / ACC / choreography as comparatively tested, add a visible boundary stating that those later architectural layers currently have falsification/conformance conditions but **no matched comparator execution in 00D yet**.

Do not silently broaden 00D's evidence claim.

## 4. Readability / credibility backlog

From the presentation-and-credibility plan, defer until the duplicate disposition and remaining semantic checks are closed:

- **P01** root status/licence/validation/citation badges.
- **P02** root architecture Mermaid.
- **P03** root evidence-boundary table.
- **P04** Ecosystem Positioning responsibility matrix with `Owns / Emits / Never`.
- **P05** EA benchmark-status dashboard.
- **P06** EA corpus status legend table.
- **P07** corpus-at-a-glance table + collapsible long route.
- **P09** topology reading-rule Mermaid.
- **P10** Regime Awareness producer/consumer input-output table.
- **P11** uniform document cards — start only with the main reading route, not the whole corpus.
- **P13** tagged release + Zenodo DOI — requires Iván's explicit publication approval.

Already addressed in the current pass:

- **P08 substance:** canonical notation / owner / `(d,t)` reconciliation added to the topology page.
- **P12 substance:** predecessor / controlled-source banners added to the priority predecessor/source set.

## 5. Corpus provenance follow-up

The new provenance bridge distinguishes:

- controlled Drive-backed freezes: Drive file ID + pinned `revisionId` remains the exact controlled-source anchor;
- current public working successors: Git path + commit SHA is the public citation anchor;
- preserved predecessors: cite only for lineage, not current semantics.

Still unresolved by this pass:

- controlled revision / SHA-256 parity inventory explicitly marked pending in `CANONICAL_CORPUS_MANIFEST.md`;
- any decision to materialize the intended single-file v0.4 canonical paths.

Do not claim these verification items are complete.

## 6. Optional editorial follow-up

MSCA 04's end-to-end cycle now defines the canonical runtime order clearly. A later editorial pass may decide whether the physical section order should be rearranged to mirror that execution order exactly. No semantic change is required before that decision.

