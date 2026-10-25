# Panodyssey corpus-migration QA — source fidelity and open gates

**Local-preparation audit date:** 25 October 2026. **Base GitHub main:** `733749040565cab79ce7af291a7f58cb28024fa2`. **Change state:** uncommitted owner-review branch. **Source provenance:** Google Docs observed revisions in [SOURCE_MANIFEST.json](./SOURCE_MANIFEST.json).

## 1. Content conservation — checked

| Check | Result | Basis |
|---|---|---|
| Current operational Panodyssey source map | **1 / 1 present** | SOURCE-00 independent of the expanded derivative Challenge |
| Current assembled package 00–08 | **9 / 9 present** | Full source text, not summaries |
| **All source records** | **10 / 10 exact at normalized text level** | Reconstructed Google Docs native paragraph and table-cell text order; removed only exported Markdown heading, hyperlink and table syntax and collapsed whitespace |
| Native Google Docs tables | **11 / 11** | Shape and cell order checked against native Docs readback |
| Table rows | **121 / 121** | Original table headings and all native data rows remain |
| Table cells | **566 / 566** | Every original cell appears in the exported table |
| Linked native text-run targets | **185 / 185 present in exported files** | Existing source URLs retained; no cross-Doc link deleted |
| Normalized source-text footprint | **224,869 characters** | Counts all ten source documents' body text including cells, with whitespace normalized |
| Original prior versions | **Not silently replaced** | Historical `/old` Drive folder and its v0.3/v0.4 snapshots preserved externally; current Docs cited by ID/revision |
| Original GitHub 00J/00J-A01/A25/A26/R01 files | **No source rewrite** | Extension is additive; parent remains separately routed |

Content conservation is a **mechanical equivalence check of the visible text**, not a claim of identical Google Docs typography, paginated layout, or scientific correctness. Source-native tables became Markdown tables with the same row/column structure and all text. Each rendered file contains the original source title, Doc URL, observed revision and an export SHA-256 in the manifest. Google Docs internal links remain as historical provenance; all ten documents are also reachable locally from the extension's README.

## 2. Method and interface review

- The extension is **partially**, not globally, isomorphic: `E=(K_iso, Δ, κ)`. Existing A25/A26 family admission and R01 reduction-projection methodology are referenced rather than silently declared proven.
- Source-owned Panodyssey single Challenge/T-UC1–3, PAN-S1–S14 and T-UC3 E1–E5 remain separate from EA-S1–S14, UC21-S6, 00J Q0–Q5, DDS and UC4 IDs.
- Legacy `00J-A01` H0/H1/H2 frozen-source terms and DDS R1/R2/R3 conventions are not substituted for the three Panodyssey native trajectories.
- Conditional legal references and exact triggers are retained in 02 and 03. No compliance certification or separate external legal-advice task is introduced.
- Evaluator independence, acceptance/parity, assessment permissions, positive controls, conflicts, re-adjudication and new dependency re-opening are retained in 04/06/07 and made independently addressable by [DDS_UC4_READINESS](./DDS_UC4_READINESS.md).
- PanO-v6 and any reduced-case test reuse are explicitly **conditional examples** in 08/TRANSFER_LEDGER, not fresh executions or verified PASS.

## 3. Navigation and file controls — checked / to recheck

- A new `00J-extensions/README.md` routes to the unique candidate extension, and `PANODYSSEY-EXT-01/README.md` routes to every source/method/audit artifact.
- Surgical source-preserving **one-row** entry proposed in `baseline/README.md`; **one-line** reference proposed in `baseline/CANONICAL_CORPUS_MANIFEST.md`. No change to canonical frozen requirement IDs.
- Relative package links were tested locally. One route to `governance/CORPUS_REVIEW_PROCEDURE_2026-10-06.md` appeared absent **only because sparse checkout excluded governance**; the exact canonical file was independently confirmed present through the GitHub connector.
- At final commit review, rerun link checker against the complete Git tree, verify immutable source SHA-256 from the manifest, and reconcile repository main drift. Do not create a competing active VNext.

## 4. Blockers that remain open, not technical export failures

| Gate | State | Closure evidence required |
|---|---|---|
| Public disclosure of internal Doc content | **HOLD** | Explicit owner decision: publish, redact or keep private; include source rights / attribution and third-party consent boundaries |
| Final editorial corpus promotion | **HOLD** | Owner reviews diff, nomenclature, scope and primary canonical reader; no unrequested edits to historical sources |
| 00J A25/A26 extension admission | **NOT ESTABLISHED** | Per-claim X1–X7/Y1–Y7 evidence, typed projection and coupling checks |
| Transferred PanO-v6 result | **NONE VERIFIED** | Unique executed/proved source result + source hash + parameter/horizon/comparator match; independent reviewer ledger |
| DDS Stage A / B / C, UC4 Stage-0/1 | **NOT SCORED / NOT EXECUTED** | Fixture and criteria freeze, candidate/peer, assessor, permissions and signed test authorization |
| Legal/technical requirement applicability | **CONDITIONAL / UNKNOWN WHERE STATED** | Exact factual predicate if a particular claim is later assessed; no claim of global legal compliance |
| Reviewer conflicts / hidden dependencies | **PROTOCOL PREPARED** | Actual adjudication/reopen events only if observed; historic results unchanged |

**Audit conclusion:** suitable for a **private owner-review branch with no commit**. Not yet suitable for public-branch content publication, external submission, legal/conformance claims or experimental transfer admission. Remaining gates belong to the next review, not to the mechanical transfer.
