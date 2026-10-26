# R01 information-preservation audit — 4 October 2026

[R01 current entry](./README.md) · [Trace-layer policy](./TRACE_POLICY.md) · [Version-aware verifier](./extensions/verify_audit_v2.py) · [Current work register](./feasibility/WORKPLAN_STATUS.json)

## Purpose and boundary

This is a documentary preservation audit of the R01 Git history and the current repository state. It asks whether reorganizations, translations, queue cleanup and later status/editorial repairs dropped earlier information. It is **not** an independent scientific reconstruction of the R01 theorem, an M16 review, an M17 source-clause audit, or an executed R01/EA campaign.

The external review received immediately before this pass examined an earlier R01 README blob (`9a9784a6…`) structurally and by verified fragments; it explicitly did not perform a byte-for-byte read of the complete README or execute the verifiers. Its findings are therefore treated as review input, not as a certificate of the current edition.

## Historical chain reviewed

The audit followed the repository from the original R01 publication through the current reading route, with special attention to commits that reorganized or deleted substantial text:

| Milestone | Preservation concern | Evidence checked |
|---|---|---|
| `172582db` — initial R01 publication | Original scenario and entry material | Git compare to the current line shows the original R01 files as modified, not silently removed; later material is additive or separately preserved. |
| `8efc19c9` — complete English edition | Translation could alter structure, formulas, links or numbers | `TRANSLATION_TRACE.json` records one-to-one content-line correspondence, heading hierarchy, ordered link destinations, tables, numerical values, formulas and code preservation for the translated package. |
| `e90bdebf` — base/reduction/extensions separation | Moving material out of the base could lose case or reduction content | `ORGANIZATION_TRACE.json` embeds the preceding texts and hashes. Its historical embedded translation snapshot was restored byte-for-byte after the later accidental modification was detected. |
| `02314464` and `8502ff4c` — pilot objective and incident-scope clarification | Later clarification could overwrite earlier reading editions | `PILOT_OBJECTIVE_TRACE.json` and `INCIDENT_SCOPE_TRACE.json` preserve their before-files, hashes and reversible edits. |
| `85f1692c` / `3c9db810` — feasibility reorganization | Moving proof/work-plan assets could orphan or truncate earlier work | `RELOCATION_MANIFEST.json` records 40 moves: 34 byte-exact and the remaining Markdown moves limited to relative-navigation changes at relocation time. `PRESERVATION_CHECKS.json` records the canonical scenario/extensions unchanged by that relocation and 491 relative-link checks. |
| `d8fbfa48` → `ae710f7d` — queue cleanup | Large deletion of superseded queues could erase criteria or experimental history | `QUEUE_SNAPSHOT_2026-10-04.json` contains 20 complete pre-cleanup file snapshots. This audit fetched all 20 files at `d8fbfa48`; every recorded Git blob SHA matches the repository blob at that commit. Current `WORKPLAN_STATUS.json` retains the 55 historical task IDs/criteria and points superseded tasks to their owning delivery or preserved snapshot. |
| `7881cc72` → `73e4d986` / `872a78df` — theorem repair and canonicalization | Mathematical repair could silently replace prior claims | `R01_AUDIT_CONTINUITY_RELEASE.json` records prior theorem sections preserved with minimal enumerated repairs; the status register records original inventory rows, mathematical sections, equation blocks and all 55 task states as preserved. M16/M17 remain open. |
| `d8fbfa48` onward — technology extension | New mechanism work could be mistaken for replacement of the base theorem | `TECHNOLOGY_EXTENSION_REVIEW_RELEASE.json` records the base theorem version, unchanged original frontier formulas, protected paths and no real technology execution. |
| `275d7882` → `eccb5f24` / `ce62e84e` — English continuation | In-place language cleanup could lose task state or mathematics | `TECHNOLOGY_EXTENSION_ENGLISH_RELEASE.json` records 55 task IDs and historical criteria preserved, unchanged task states, no base-theorem change, and only prose connective translation inside displayed mathematics. The later corruption of one embedded historical snapshot was separately repaired to the original blob. |
| Current v2 gate | Known historical drift could mask a new mismatch | `verify_audit_v2.py` now freezes the known documentary drift baseline. Normal CI passes only the known baseline; an injected new mismatch is required to fail as `UNRECORDED_DOCUMENTARY_DRIFT`. |

## Direct preservation checks performed in this pass

### Pre-cleanup snapshot

`QUEUE_SNAPSHOT_2026-10-04.json` identifies `d8fbfa48581df366081143872ec4c16360c51635` as its input commit and stores 20 file blobs. Each of those 20 recorded blob SHAs was compared with the corresponding GitHub file at that exact commit. Result: **20/20 blob matches**.

This includes the pre-cleanup copies of the R01 README, strategic prompt, mathematical-feasibility plan, oracle plan, differential/value note, Hugging Face remaining-tasks file, Hugging Face case README, the current-work documents, technology protocol, human-escalation study, conditioned theorem material, received-material README, and the three wider corpus planning/visual-review files captured by the snapshot.

### Relocated historical material

The relocation manifest identifies the earlier source path and immutable source commit for moved feasibility material. Git compare from the pre-relocation line shows the machine-readable fixtures, scripts and received artifacts as renames or byte-identical moves. Two historical Markdown paths are no longer present at their old locations because their material was moved into `feasibility/previous-work/` or `feasibility/partial-experiments/`; their source revisions remain addressable by the immutable URLs recorded in the manifest.

### Queue cleanup

The large cleanup at `ae710f7d` removed repeated active queue text from several documents, but the deleted queue material is present in the pre-cleanup snapshot. The current register retains each original criterion as historical metadata instead of pretending every old queue is still active. This is deliberate supersession, not information deletion.

### Current documentary gate

The current version-aware audit reports:

- substantive finite-check reproduction: PASS;
- historical substantive report match: true;
- substantive mismatches: none;
- known extension drift: the three current extension READMEs;
- known logical trace drift: the nine frozen path-level items;
- unrecorded documentary drift: none.

CI also performs a deliberate negative probe by modifying an unlisted historical-review path in the runner. The verifier returns `FAIL / UNRECORDED_DOCUMENTARY_DRIFT`, proving that the known-drift baseline does not authorize arbitrary future drift.

## Current versus historical material

The current route is governed by the root README, current scenario, conditioned theorem v0.2, technology-extension protocol/current workplan, C02 oracle-design preparation, current case documents and the version-aware verifier.

Historical snapshots, old queue bodies, superseded feasibility plans, received rehearsal material, and the three extension `proof/README.md` guides remain available for provenance. They do not become active research obligations merely because they are retained or linked as evidence.

## Findings

1. **No documentary information loss was detected in the reviewed R01 history.** High-risk reorganizations have either reversible before-files, immutable source commits, byte-exact relocation evidence, complete queue snapshots, or explicit release records preserving the prior mathematical/task structure.
2. The previously detected corruption of the embedded `TRANSLATION_TRACE.json` snapshot inside `ORGANIZATION_TRACE.json` was a real preservation defect. It has been repaired to the original historical blob rather than normalized to the current edition.
3. The queue cleanup intentionally removed repeated active-plan text from current documents; the full pre-cleanup bodies remain preserved in `QUEUE_SNAPSHOT_2026-10-04.json`, and current tasks retain their historical criteria.
4. Translation and later editorial changes do not establish scientific validation. M16 independent coverage and M17 source-clause fidelity remain open; P08 remains the documentary-integrity closure task.
5. This audit supports information preservation, not the truth of every scientific claim. In particular, it does not independently reconstruct the adaptive-history-to-parity step identified as still requiring independent coverage.

## Rule for the next editorial/readability pass

Only current-route prose is eligible for visual/readability editing. Historical snapshots, manifests, frozen results/checkers, received originals and superseded proof guides remain untouched.

For current-route prose, edits must be local and paragraph-preserving. The next pass must retain headings/anchors, link destinations, equations, code, tables, numerical tokens, stated conditions, evidence status and claim boundaries. After the pass, the version-aware gate, canonical navigation/anchor checker and a dedicated before/after preservation check must pass before the editorial changes are accepted.
