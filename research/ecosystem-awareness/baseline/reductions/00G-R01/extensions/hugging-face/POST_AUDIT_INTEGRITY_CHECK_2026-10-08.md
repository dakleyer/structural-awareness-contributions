# Post-Audit Integrity Check — Hugging Face DDS Package — 8 October 2026

**Purpose:** verify that external-audit corrections did not erase the pre-audit Stage A record, silently rewrite canonical theory, or leave the current Hugging Face package structurally inconsistent.

## 1. Scope of this integrity check

Comparison base:

- repository commit `420d1b84304e8ffc96cd6656bac578f976c6b309` — first external-audit pack publication.

Current checked head:

- repository commit `d797ba833c4e35d968180f57a7636121b4f92ad3`.

All files changed between those two commits are inside:

`research/ecosystem-awareness/baseline/reductions/00G-R01/extensions/hugging-face/`

No post-audit change in this comparison touches 00M, 00N, the canonical S1–S14/T1–T4 requirements, canonical MSCA, DDS method definitions, Regime Awareness, Ecosystem Signalling or the Agentic Gradient Law.

## 2. Exact v0.1 preservation

The four Stage A artefacts that had served as the pre-audit route/design/adjudication record were restored to the exact blobs present at commit `420d1b84...`:

| Artefact | Expected/current blob SHA | Result |
|---|---|---|
| `DDS_STAGE_A_HISTORICAL_ROUTE_v0.1.md` | `df8733c3cdd8193a4c5aa88d9af8b03d208d06f9` | exact match |
| `DDS_STAGE_A_RUN_CARD_v0.1.json` | `fcb2ae7cd0c40d44c7e57b7496ceb96e3ebcd296` | exact match |
| `DDS_STAGE_A_EA_SPECIFICATION_ADJUDICATION_v0.1.md` | `9fb85288cc7b1cd0dfb9e6976d419ecb79bdc1d8` | exact match |
| `DDS_STAGE_A_EA_SPECIFICATION_RESULT_v0.1.json` | `9e36ccb609e8489a9d4c8ff120c7f052454ef6a1` | exact match |

These four files do not appear as modified in the current compare against `420d1b84...`.

**Important:** their relative links still resolve against the moving repository. For exact reconstruction of the pre-audit publication state, use the commit permalink at `420d1b84...`, as recorded in [STAGE_A_FREEZE_AND_VERSION_LINEAGE.md](./STAGE_A_FREEZE_AND_VERSION_LINEAGE.md).

## 3. Audit-corrected successor structure

Current successors are separate files rather than rewrites of v0.1:

- [Stage A Historical Route v0.2 — Audit-Corrected](./DDS_STAGE_A_HISTORICAL_ROUTE_v0.2_AUDIT_CORRECTED.md)
- [Stage A Run Card v0.2 — Audit-Corrected](./DDS_STAGE_A_RUN_CARD_v0.2_AUDIT_CORRECTED.json)
- [Stage A Coverage Adjudication v0.2 — Audit-Corrected](./DDS_STAGE_A_EA_SPECIFICATION_ADJUDICATION_v0.2_AUDIT_CORRECTED.md)
- [Stage A Result v0.2 — Audit-Corrected](./DDS_STAGE_A_EA_SPECIFICATION_RESULT_v0.2_AUDIT_CORRECTED.json)

Current claim ceiling:

`COVERAGE_ARGUMENT_COMPLETE__STAGE_A_ACCEPTANCE_PENDING`

## 4. Chronology correction

The preregistration chronology is now explicit:

- `37f87c1f...`: HF-N0…HF-N9 existed before the original requirement-level adjudication.
- `4cb91a61...`: EA-SA-Q0…Q8 and original requirement-level verdicts were created.
- `746a0794...`: HF-N10 was added only **after** external audit.

Therefore no current document should claim that HF-N10 was part of the original v0.1 adjudication. HF-N10 is marked post-audit / previously unscored in the current blind packet and audit-corrected adjudication.

## 5. Architecture / specification separation

The audit-corrected route preserves the original HF-Q0…Q9, B1…B6, BPMN, Repositioning, Regime Awareness, Gradient and ACC material because it is important design lineage.

It is now explicitly labelled as:

- architecture-flavoured 7 October design;
- pre-Stage-B lineage;
- not the current requirement-level Stage A scoring contract;
- not Stage B verification evidence.

The requirement-level Stage A coverage finding is maintained separately.

No architecture section was deleted to manufacture this separation.

## 6. Historical corrections preserved as corrections, not theory changes

The following historical changes were made in working/in-progress evidence documents:

- corrected the >90% population denominator to the 533-agent rapid-pivot population and kept ~700/~1,200 as a distinct broader measure;
- downgraded JAN183411 / “first worker RCE” to a partial join with an unresolved timing/event-definition conflict;
- expanded the METR evidence ceiling;
- added PHASEONE10841 as a source-supported precursor to the HF credential-search workstream without promoting that to intent for the later intrusion;
- separated the synchronized July 12 run termination from later activity decline and victim containment;
- recorded heterogeneous source interpretations/motivations instead of freezing one universal motive.

The six-minute GO mechanism remains present. It was not replaced by the collective-utility mechanism.

## 7. HF-N10 consequence

HF-N10 — conscious out-of-scope collective utility — is a **post-audit extension** prompted by the historical-source review.

It does not replace HF-N0…HF-N9.

It is not counted as part of the original v0.1 coverage result.

It is included in the future blind/falsifiable rerun and is explicitly marked previously unscored.

## 8. External-auditor wording preserved

The external-audit text is preserved independently from the maintainer response:

- [External Audit Input 1](./EXTERNAL_AUDIT_INPUT_1_2026-10-08.md)
- [External Audit Input 2](./EXTERNAL_AUDIT_INPUT_2_2026-10-08.md)
- [Maintainer Response](./EXTERNAL_AUDIT_RESPONSE_2026-10-08.md)

The audit-input files are provenance records of user-supplied text; the repository does not claim independent authentication of their authorship.

## 9. Mechanical consistency checks

At the checked head:

- all five relevant JSON artefacts parsed successfully;
- the four v0.1 Stage A blob SHAs exactly match the pre-audit snapshot;
- no v0.1 Stage A frozen artefact appears modified relative to commit `420d1b84...`;
- link checking across the current audit/Stage-A/Stage-B reading route found **0 broken relative links**;
- duplicate-heading checking across the same current route found **0 duplicate Markdown headings**;
- all post-audit changes in the compare are confined to the Hugging Face extension folder.

## 10. Remaining open items — not silently repaired

The following remain genuinely open:

1. independent/blind second-reader adjudication has not been completed;
2. deterministic execution under a prospectively frozen requirement-level scoring contract has not been completed;
3. HF-N10 remains unscored;
4. the HF-specific Stage B oracle remains incomplete/unfrozen;
5. Stage B has not been passed;
6. Stage C has not started;
7. working historical evidence documents were corrected in place because they were explicitly marked in-progress; exact pre-correction states remain available through Git history/commit snapshots rather than parallel historical filenames;
8. source-level factual corrections still require any desired independent second-reader confirmation.

## 11. Integrity conclusion

The post-audit repair no longer depends on rewriting the pre-audit v0.1 Stage A record.

The principal remaining methodological debt is **future evidence generation**, not loss of prior information:

- freeze a complete requirement-level scoring contract prospectively;
- run the blind review;
- execute the deterministic fixture if the hard-gate claim is retained;
- only then adjudicate Stage A acceptance.

Stage B and Stage C remain separate and unpassed/unstarted.
