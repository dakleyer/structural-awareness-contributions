# Corpus Information Conservation Audit — 23 September 2026

> **Purpose:** independently check whether earlier public corpus information was deleted, disconnected, silently compressed or made available only through Git history during the September restructuring and semantic-reconciliation work. This audit is about **information conservation**, not about declaring every earlier formulation current.

## 1. Audit checkpoints

The audit compared the current repository against:

- 1 September 2026 — pre-EA-corpus / FG-TIDA package checkpoint `17a694dd`;
- 11 September 2026 — controlled-public-mirror checkpoint `081ff3b9`;
- 19 September 2026 — substantive EA corpus citation anchor `55fb4da3`;
- 23 September 2026 — pre-presentation-cleanup main `2165e2af`.

The review also inspected removal/move/rewrite commits and the current baseline/FG-TIDA duplicate pairs.

## 2. File-level deletion findings

### 2.1 From the 1 September checkpoint

No file that existed at `17a694dd` is reported as removed from the current tree. Later-created-and-then-removed staging or relocated files require the later checkpoints below.

### 2.2 From the 11 September controlled-public-mirror checkpoint

Three path removals appear:

1. `.corpus-import/part-000.b64` / `part-001.b64` — aborted transfer staging. These are transport residue, not authored corpus semantics.
2. `research/ecosystem-awareness/CANONICAL_CORPUS_MANIFEST.md` — the manifest was relocated and substantially extended under `baseline/CANONICAL_CORPUS_MANIFEST.md`. The earlier exact public blob is now additionally preserved in [preserved-public-snapshots](./preserved-public-snapshots/README.md).
3. `research/ecosystem-awareness/validation/UC-EA-01_v0.3_FROZEN.md` — not lost. The exact earlier blob `e460cb5c...` remains present as `baseline/UC-EA-01_v0.3_EARLIER_PUBLIC_FREEZE.md`; the current continuous/frozen reading route is maintained separately.

**Conclusion:** no identified authored file from this checkpoint is now available only as an unrecoverable deletion.

## 3. Content-level replacement findings

### 3.1 Root Structural Awareness README

The earlier landing page contained a distinct causal-loop Mermaid, a compact workstream/status table, older programme framing and an explicit pre-licence statement. The current root was intentionally rewritten around the four-part Structural Awareness programme and Ecosystem Positioning route.

This is a **real supersession of reader framing**, not a safe line-for-line continuation. To prevent the older information from living only in history, exact 11 September and 19 September root snapshots are now materialized under [preserved-public-snapshots](./preserved-public-snapshots/README.md).

### 3.2 Ecosystem Awareness parent router / baseline reader

The earlier parent router and canonical-reader pages contained publication-completeness routing and intermediate reading structures that were later replaced by the current EA-router / baseline-index split and FG-TIDA package separation.

The current architecture is clearer, but some earlier navigation/status wording is no longer in the live route. Exact 11 September and 19 September EA router snapshots and the 19 September baseline index are therefore materialized for lineage.

### 3.3 A/B/C/D topology reconciliation

The 19 September topology described A/B/C/D as four epistemic **positions**:
- A sufficiently determined;
- B recognized and unresolved;
- C recognized and potentially obtainable;
- D structural residual.

The current topology reconciles A/B/C/D as four components of one qualified position, with B carrying confidence/intensity and an explicit subsection explaining the relation to the earlier coarse wording.

The earlier table is historically and conceptually useful even though it is no longer current semantics. The exact 19 September topology is therefore preserved as a historical snapshot rather than reinserted into the live topology.

### 3.4 00D-A01 “Proof Sketch” predecessor

The earlier 00D-A01 contained the full reference-scenario fixture/oracle design under a “Proof Sketch” title. The current file at that historical filename is intentionally a short alias because the rigor audit judged “Proof Sketch” to overstate the evidence class; the live successor is the Construction & Test Design artifact.

The old detailed artifact is now materialized unchanged as [EA_00D_A01_PROOF_SKETCH_2026-09-19.md](./preserved-public-snapshots/EA_00D_A01_PROOF_SKETCH_2026-09-19.md). The current alias and current successor remain untouched.

## 4. Controlled v0.4 public-mirror audit

The 11 September public mirror and current Git versions of controlled 02/03/04 were compared because later maintenance introduced link rebasing, namespace clarification, source banners and additive clarification.

Findings:

- **02 Control Matrix part 1:** earlier substantive passages remain represented in the current file; observed differences include formatting/escaping and later reconciliation. The exact 11 September public blob is nevertheless preserved separately.
- **03 Functional Architecture part 1:** later audit commits explicitly restored the controlled source after additive clarifications. Earlier substantive passages checked in the audit remain present. The exact 11 September public blob is preserved separately.
- **04 Functional Interfaces parts 1–3:** the current files contain namespace and routing clarifications (for example `S#` → `IF-S#`) and later interface-quality material. Spot tracing confirmed earlier EHD/interoperability, Theme-boundary, signalling, F1–F9 completeness and trust-framework statements remain in the current files or integrated v0.5 successor. Because these files are controlled-source-sensitive and no byte/revision parity claim should be inferred, all three exact 11 September public blobs are now preserved separately.

**Important:** these preserved files prove conservation of the earlier **public Git blobs**, not parity with the controlled Google Drive revisions. The existing manifest correctly keeps Drive revision/SHA verification pending.

## 5. Baseline / FG-TIDA duplicate disposition

Five duplicate pairs were reviewed before compacting any reading route.

| Pair | Finding | Conservation decision |
|---|---|---|
| DAOS EA Use Cases Masterclass | Same substantive text; differences are relative paths after package relocation | Keep both for now; FG-TIDA path is the package reader, baseline copy remains a preserved compatibility/source copy |
| 05A Current-State Conformance Bridge | Same substantive text; differences are path rebasing and current general-interface target | Keep both for now; FG-TIDA path is the application-package reader |
| FG-TIDA Public Footprint | Byte-identical | Keep both until a later explicit deduplication decision |
| Public Provenance | Byte-identical | Keep both until a later explicit deduplication decision |
| EA-ITP-01 Frozen | Byte-identical | Keep both; frozen/source ownership should not be altered casually |

No duplicate is deleted or stubbed by this audit. This resolves the immediate **information-loss risk** without forcing a physical-home decision prematurely.

## 6. Materialized conservation set

The dedicated [preserved-public-snapshots](./preserved-public-snapshots/README.md) folder now contains exact copies of the earlier public blobs judged most vulnerable to becoming history-only:

- root programme readers;
- EA parent routers / baseline index;
- earlier corpus manifests;
- earlier topology;
- earlier 00D-A01 proof-sketch artifact;
- changed controlled-public-mirror source parts for 02, 03 and 04.

Each snapshot is byte-identical at the Git-blob level to the historical source blob named in the snapshot index.

## 7. Remaining open verification

This audit does **not** close:

- controlled Google Drive revision ↔ current Git SHA-256 parity;
- the intended single-file v0.4 canonical materialization;
- future physical deduplication between baseline and FG-TIDA package copies;
- semantic validation of every historical draft as current architecture.

Those remain governance/verification work. The conservation rule is now simpler: **do not delete an earlier public formulation merely because a clearer successor exists; preserve it explicitly as lineage when it contains distinct information or framing.**

## 8. Audit conclusion

Within the audited checkpoints and deletion-bearing files, no known substantive public corpus information now needs to remain only in inaccessible or implicit Git history. Where current semantics superseded or materially reformulated earlier public text, the earlier public blob has been materialized as a clearly non-canonical historical snapshot.

Future cleanup may change routing, but it should not delete these snapshots or silently promote them back into current semantics.
