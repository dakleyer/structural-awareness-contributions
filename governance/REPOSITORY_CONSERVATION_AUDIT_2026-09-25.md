# Repository conservation audit — 25 September 2026

**Scope:** `dakleyer/structural-awareness-contributions`, published `main` history from 29 August to 25 September 2026, anchored at `ba68bbe` immediately before these audit repairs. This is a conservation and navigation audit, not an independent proof of the architecture or its empirical performance.

## Method and coverage

- Cloned the complete reachable Git history at that anchor and checked connectivity: **1,711 commits**, one published branch, **427 blobs at the audit anchor**, and **46 distinct paths that had been deleted at some point in that history**. Deleted historical blobs remain retrievable by commit SHA.
- Scanned the numstat and patches of the entire history, including every Markdown edit. Reviewed **38 individual Markdown path changes with a net reduction of at least 20 lines**, then inspected the major removals, replacements and canonical successors.
- Checked all current Markdown local links and image paths outside `governance/preserved-public-snapshots/`. Those historical snapshots retain their original relative links and are deliberately excluded from active-route integrity checks.
- Inspected slide XML across all four historical revisions of the combined Ecosystem Positioning deck and both current split decks. The combined deck progressed **10 → 10 → 9 → 17 slides**; the current split decks have **8 architecture** and **12 requirements** slides. Current combined and split decks contain their distinct architecture and evidence routes; the manifest explicitly labels the combined repository binary as a v1.10 mirror pending v1.11 sync.

## Confirmed navigation losses and repairs

| Historical change | Finding | Repair |
|---|---|---|
| [`e83d958`](https://github.com/dakleyer/structural-awareness-contributions/commit/e83d9581df) | A four-line ablation update removed 251 lines from the Ecosystem Positioning README, including its corpus, mechanisms, interfaces, use cases, fixtures and benchmark route. This was an accidental loss from the reader-facing architecture page. | The mechanisms/interfaces/use-case/fixture/benchmark sections were restored in [`ba68bbe`](https://github.com/dakleyer/structural-awareness-contributions/commit/ba68bbe4024d5f1c41c7907e2cfdc95cbd9c7e3f). This audit restores the remaining **corpus spine** without removing the newer proofs. |
| [`f684eeb`](https://github.com/dakleyer/structural-awareness-contributions/commit/f684eeb1cd) | A 90-line reduction in the EA README removed the concise reference-scenario route and 00F/00H/00I reader walkthroughs. Detailed scenario documents remained, but the integrated route disappeared. | Preserved the original route in [`SCENARIO_READER_GUIDE_2026-09-25.md`](../research/ecosystem-awareness/SCENARIO_READER_GUIDE_2026-09-25.md) and linked it from the architectural README. The EA README is not modified. |
| Existing local links | Four active relative links were broken: two pointed to a `TESTBED_METHOD.md` that has never existed in the published repository; two proof-fixture READMEs had one too few parent-directory segments. | Linked the architectural account to the actual canonical benchmark methodology and corrected the two proof-fixture paths. Active local references now resolve. |

## Other large historical reductions

- The root README was substantially rewritten in [`97795b0`](https://github.com/dakleyer/structural-awareness-contributions/commit/97795b0dbacd3c7b9a572c0ab17c8052edc8caaf) and [`204b54e`](https://github.com/dakleyer/structural-awareness-contributions/commit/204b54eb5e). The current root again contains the four programme parts, engineering lineage and architectural route. The old text remains in Git history.
- The FG-TIDA `01G` baseline file became a routing pointer in [`ac4dc81`](https://github.com/dakleyer/structural-awareness-contributions/commit/ac4dc81552); the active charter is in `research/ecosystem-awareness/fg-tida/charter/`. That charter was substantially rewritten in [`7934866`](https://github.com/dakleyer/structural-awareness-contributions/commit/7934866e87). It still covers the two peer mechanisms, 05/05A boundary, deliverables, test sequence and open institutional decisions. **It is a revision, not a line-for-line relocation**; earlier drafts remain accessible through Git history.
- Deleted 00J, 02B, A21, A25, Decision Boundary and ablation files have named working successors or canonical copies. Their old versions remain in Git history. Several successors are substantive rewrites; the existence of a successor should **not** be described as exact textual conservation. We have not reinstated deprecated proofs or duplicate harnesses as authoritative material.
- Staging chunks and one-off publication workflows were removed after publication; the current decks and Markdown corpus remain in the repository.

## Continuous check

[`scripts/check_document_integrity.py`](../scripts/check_document_integrity.py), run by [`document-integrity.yml`](../.github/workflows/document-integrity.yml) on pushes and pull requests, checks current local routes, eight load-bearing architectural sections and the presence/minimum content of all three presentation decks. This catches the same class of accidental mass deletion in the README and slide content loss while allowing intentional edits after the guard is updated deliberately. It does not certify semantic correctness, external URLs, or the equivalence of a rewritten draft to every historical version.

**Verification on this revision:** Git connectivity passed; current active Markdown local routes and images resolve; `git diff --check` passed; document integrity check passed. The historical snapshots retain broken relative routes by design because they preserve the original publication context.
