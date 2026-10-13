# Flores / Population × EA — technical addendum to the ONE DDS campaign

**Parent and only campaign owner:** [DDS-A-FLORES-POP-EA-01 / CAMPAIGN.md](../CAMPAIGN.md)  
**Component ID:** DDS-A-FLORES-POP-EA-01/RECEIVER-P0-P3  
**Status:** AUTHOR-SIDE TECHNICAL SUBPROFILE / NOT ADMITTED / NOT EXECUTED AGAINST NATIVE FLORES DATA / NOT A SEPARATE DDS CAMPAIGN  
**Date:** 13 October 2026.

This addendum contributes the detailed receiver-side P0→P3 hypothesis and its post-audit correction to the existing, independently published working Flores campaign. It is **not another owner**, another test method, another registered freeze, or a claim that its P2 ablation is real behaviour of Flores's judges. The master campaign also records the alternative **UC17-08 attested-absence→permit** handoff and source-native §13/UC-4 controls; the two experimental candidates remain distinct pending selection by the campaign reviewer.

## Complete technical reading route

1. [Native eight-case experiment and P0→P3 receiving protocol](./PROTOCOL_P0_P3.md) — judge model, sealed output, provenance, blind/unblind, selective loss and recovery, source limitations.
2. [04/05A/EHD and process-relative B/C/D/UNKNOWN](./EHD_04_05A_MAPPING.md) — IF-S9, N07–N10, source A vs EA interpretation, known/unknown/data ownership, feedback, and receiver profile.
3. [Falsifiers, positive controls, strong B2 and burdens](./ACCEPTANCE_AND_B2.md) — 13 technical gates G00–G12; real independent reviewer/freeze not yet assigned.
4. [R0/R1 residual-ledger predecessor](./RESIDUAL_LEDGER.md) — all nine auditor inventory questions, sampling vs structural residual and hypothetical probe correction.
5. [Primary-source SHA1 locks and twenty mutable-comment body digests](./SOURCES_AND_PINS.md) · [machine CSV](./COMMENT_BODY_HASHES_20_2026-10-12.csv).
6. [Adversarial corrections](./AUDIT_RECONCILIATION.md) — rejected Q-bind B→C, source A/BCD, frame location, scorer leakage, key-truth conflation, disputed B/D roles, absent native data.
7. [Historical packet filenames and SHA256](./HISTORY_AND_REPRODUCTION.md) — exact local recovered hashes; original raw historical ZIPs are **not** public here and provisional blind reviewer oracles must remain private.
8. [Machine trace of the requirements](./STAGE_A_GATE_TRACE.csv).
9. [Local reference checker](./code/qualifier.py), [explicitly mock facts and receipts](./code/mock_receipts.json), [author-written consistency tests](./code/test_qualifier.py). A competent B2 can use equivalent proof-graph semantics. Tests are illustrative, not EA success.
10. [An optional English source-owner review brief](./SUBMISSION_BRIEF_EN.md) — **NOT sent** to Flores.
11. [Technical component manifest](./TECHNICAL_COMPONENT_RECORD.json) — references the existing campaign ID; not a second campaign registry.

## Critical technical boundary

- Producer A (Flores flags/post-unblind report) remains source-owned and outside metadata-only EHD. Neither EA nor this checker sees sealed roles before original unblind.
- P0 blind and P1 unblind are observation views already specified by Flores; original generate/detect/unblind results remain unpublished at the verified cut. All local source-receipt booleans are **author mock values**.
- P2 removes an EHD/receiver association from a frozen local receiving view. Its result is **receiver proof NOT_ESTABLISHED (B→UNKNOWN when process-role basis was prior characterized)**; NOT a demonstrated source change or an automatic C.
- P3 restores a justified local basis while retaining the history and all source residual. Removing an irrelevant field or recovering a valid alternate association must not create an alarm.
- Authored-reference agreement ≠ independent truth. Independence of random draws by design ≠ empirically demonstrated independence of evaluator failure modes. UC17-08 absence ≠ permit; UC17-09 content judgment ≠ admissible record.
- A defended B2 can tie or beat the candidate. Complete receiver qualification is an open Stage A scientific comparison, not an accepted test result.

## New custody check, 13 October 2026

Unlike the earlier session that had only Library summaries, the original v0.2 and v0.5 ZIP files were **present in the current working runtime** and SHA-256 was independently recalculated from those bytes (see [History](./HISTORY_AND_REPRODUCTION.md)). This supersedes the *availability status*, NOT the historical original research text; full raw ZIPs including private oracles have not been uploaded to the public branch.

**Retrieval prompt:** “Open the DDS-A-FLORES-POP-EA-01 campaign, then its RECEIVER-P0-P3 technical component and historical audit ledger.”