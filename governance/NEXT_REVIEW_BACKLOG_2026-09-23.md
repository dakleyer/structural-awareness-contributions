# Next Review Backlog — 23 September 2026

> **Maintenance backlog only.** This is not a canonical architecture document, benchmark result or publication-status statement. It records items deliberately deferred from the 23 September surgical coherence/integrity pass.

**Conservation audit:** [Corpus Information Conservation Audit — 23 September 2026](./CORPUS_INFORMATION_CONSERVATION_AUDIT_2026-09-23.md) · [Preserved Public Snapshots](./preserved-public-snapshots/README.md)

## 1. Baseline / FG-TIDA duplicate disposition — conservation audit completed

The duplicate pairs were reviewed during the [Corpus Information Conservation Audit](./CORPUS_INFORMATION_CONSERVATION_AUDIT_2026-09-23.md) before Priority B. **No copy was deleted, stubbed or shortened.**

| Baseline copy | FG-TIDA copy | Audit finding | Current conservation decision |
|---|---|---|---|
| `baseline/DAOS_EA_USE_CASES_MASTERCLASS_v0.1.md` | `fg-tida/cases/DAOS_EA_USE_CASES_MASTERCLASS_v0.1.md` | Same substantive text; blob difference is relative-link rebasing after package relocation | FG-TIDA path is the current package reader; retain baseline copy as compatibility/source copy |
| `baseline/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md` | `fg-tida/interfaces/05A_FG_TIDA_CURRENT_STATE_CONFORMANCE_BRIDGE_v0.1.md` | Same substantive bridge; differences are rebased links and the current general-interface target | FG-TIDA path is the application-package reader; retain baseline copy |
| `baseline/FG_TIDA_ECOSYSTEM_AWARENESS_PUBLIC_FOOTPRINT_2026-09-08.part01.md` | `fg-tida/provenance/FG_TIDA_ECOSYSTEM_AWARENESS_PUBLIC_FOOTPRINT_2026-09-08.part01.md` | Byte-identical | Retain both pending any later explicit physical deduplication |
| `baseline/PUBLIC_PROVENANCE_2026-09-08.md` | `fg-tida/provenance/PUBLIC_PROVENANCE_2026-09-08.md` | Byte-identical | Retain both pending any later explicit physical deduplication |
| `baseline/EA-ITP-01_v0.1_FROZEN.md` | `fg-tida/tests/EA-ITP-01_v0.1_FROZEN.md` | Byte-identical frozen artifact | Retain both; do not change freeze/source ownership casually |

This closes the immediate **information-loss risk**, not the future storage-normalization question. A later deduplication pass may choose a single physical home only if it preserves the historical/freeze route and does not discard information.

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

### Priority B — completed 23 September 2026

Executed only after the independent conservation audit. All four changes were additive; the pre-existing explanatory text remains in place.

- **P03** root evidence-boundary table added beneath the existing evidence-boundary bullets — commit `b3143bb`.
- **P02** root architecture Mermaid added as a supplementary navigation aid over the existing Technical Gates text — commit `2009716`.
- **P07** corpus-at-a-glance table added above the full annotated reading route — commit `42846a9`. **The long route was deliberately not collapsed or removed.**
- **P09** topology reading-rule Mermaid added beneath the existing written reading rule — commit `a811725`.

The baseline / FG-TIDA duplicate review found no semantic-content conflict requiring deletion, so P07 could be added without choosing a destructive physical deduplication.

### Priority C — executed conservatively 23 September 2026

- **P01 completed** — root licence/status/validation/citation badges added without replacing the title or navigation text — commit `50f23f1`.
- **P11 completed for the current working route/evidence annexes** — uniform document cards added in two additive commits: core current route `6589075`; current evidence/implementation annexes `e335c61`. Controlled/frozen documents and preserved predecessors were deliberately not edited.
- **P13 approved, externally blocked** — Iván explicitly approved Priority C on 23 September 2026. The repository now contains [RELEASE_CANDIDATE_SA_WORKING_2026-09.md](./RELEASE_CANDIDATE_SA_WORKING_2026-09.md), commit `16c5943`, with the exact release boundary and execution sequence. The available GitHub connection does not expose GitHub Release creation and no Zenodo/DOI connector is available, so `CITATION.cff` and the root README intentionally contain **no fabricated DOI or release metadata**. Execute the external release/Zenodo step only when real tooling/credentials are available.

### Already addressed before Priority A

- **P08 substance:** canonical notation / owner / `(d,t)` reconciliation added to the topology page.
- **P12 substance:** predecessor / controlled-source banners added to the priority predecessor/source set.
- **P14 substance:** Ecosystem Positioning working-process order now runs through effective-role drift / Type catalogue / P1–P3 before the objective-conditioned Gradient from `Role_effective`.

### Visual aids — completed as a live navigation layer; PowerPoint still separate

The GitHub visual layer is now implemented through [research/ecosystem-awareness/VISUAL_GUIDE.md](../research/ecosystem-awareness/VISUAL_GUIDE.md) and routed from the root, EA, baseline, Ecosystem Positioning, Regime Awareness and MSCA READMEs.

The live guide uses current Markdown/Mermaid rather than importing the companion visual pack wholesale. It includes:

- cumulative programme/corpus evolution;
- architecture ownership;
- current positioning cycle;
- requirements → evidence → execution maturity;
- 00E/00F/00G and the 2+2 implementation-profile matrix;
- DAOS / UC-EA / EA-ITP / reference-scenario distinctions;
- 04 general → 05 ideal → 05A current FG-TIDA layering;
- question-to-document navigation and status rules.

The older SVG/PNG visual pack remains useful for slides/PDFs but was verified against commit `4093bc6`; it is therefore not treated as a second semantic source for the evolving Git corpus.

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

