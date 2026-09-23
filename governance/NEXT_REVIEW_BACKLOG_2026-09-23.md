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

## 4. Readability / credibility execution waves

**Safety rule for these waves:** preserve the existing substantive prose and source definitions. Presentation changes should be additive or locally structural; do not shorten, silently merge, or replace controlled/frozen meaning. Where a table or visual is added, the existing explanatory text remains available unless a later explicit editorial decision approves a replacement.

### Priority A — completed 23 September 2026

These four items were applied additively after the semantic/coherence pass. Existing prose was retained and the new tables were added as second-layer reading aids:

- **P04** Ecosystem Positioning detailed responsibility matrix with `Owns / Emits / Never` and source routes — commit `57c6bfe`.
- **P05** EA benchmark-status dashboard, including the explicit boundary between EA-H1–EA-H4 matched-comparator work and later positioning layers — commit `0f79c9d`.
- **P06** EA corpus status legend table, without bulk reclassification of existing files — commit `3771998`.
- **P10** Regime Awareness producer/consumer input-output interface table, retaining the original producer list and output prose — commit `d6627cf`.

### Priority B — pending

Execute only after reviewing the affected current text again. Preserve the full existing explanations.

- **P03** root evidence-boundary table tied to E1–E4. This may be added under the existing evidence-boundary bullets rather than replacing them.
- **P07** corpus-at-a-glance table + collapsible long route. **Wait for the baseline / FG-TIDA duplicate disposition** so the compact route does not canonize the wrong physical copy.
- **P02** root architecture Mermaid. The EP/EA hierarchy coherence dependency is now resolved, but this is a visual architecture aid and should be checked against the then-current text immediately before insertion.
- **P09** topology reading-rule Mermaid. Keep the existing written reading rule; the visual is supplementary.

### Priority C — pending / lower urgency

- **P01** root status/licence/validation/citation badges.
- **P11** uniform document cards — start only with the main reading route, not the whole corpus.
- **P13** tagged release + Zenodo DOI — requires Iván's explicit publication approval and should follow a deliberate milestone/freeze decision rather than routine editorial cleanup.

### Already addressed before Priority A

- **P08 substance:** canonical notation / owner / `(d,t)` reconciliation added to the topology page.
- **P12 substance:** predecessor / controlled-source banners added to the priority predecessor/source set.
- **P14 substance:** Ecosystem Positioning working-process order now runs through effective-role drift / Type catalogue / P1–P3 before the objective-conditioned Gradient from `Role_effective`.

### Visual aids and PowerPoint — separate later wave

Do not import the companion visual pack wholesale into the canonical corpus. Reuse an individual table, Mermaid or image only after the corresponding current text has been rechecked and the visual is demonstrably supplementary rather than a competing semantic source.

The canonical PowerPoint/PDF replacement remains a separate finalization step under §2. Do not replace the stable presentation pair until its remaining text-only items are approved and both artefacts can be updated together.

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

