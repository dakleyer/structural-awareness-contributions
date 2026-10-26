# External Audit Response 3 — Hugging Face / DDS Stage A — 8 October 2026

**Status:** maintainer response to [External Audit Input 3](./EXTERNAL_AUDIT_INPUT_3_2026-10-08.md) · preserves prior v0.1/v0.2 records · structural remedies are implemented only in successor v0.3 artefacts.

## 1. Overall disposition

Audit 3 identified three different classes of issue:

1. **stale state read by the auditor that had already been corrected** — notably the N10 preregistration chronology;
2. **real residual contradictions / factual inconsistencies** — historical H8, event IDs, board-primitive status, packet/source separation and evidence-ceiling propagation;
3. **real design deficiencies in the proposed path back to Stage A acceptance** — unfrozen ablations, weak falsifiers, missing Q9, blind-packet leakage, undefined verdict semantics and undefined documentary “deterministic execution”.

The third class required a **new preregistered Stage A successor** rather than edits to the preserved v0.1/v0.2 scoring records.

Current status remains:

`COVERAGE_ARGUMENT_COMPLETE__STAGE_A_ACCEPTANCE_PENDING`

Stage B is not passed. Stage C has not started.

---

## 2. Finding-by-finding response

### F1 — N10 chronology

**Accepted as an important historical error in the earlier post-audit repair; already corrected before this third response.**

Controlling chronology is now:

- `37f87c1f...` — HF-N0…HF-N9 added before the original requirement-level adjudication;
- `4cb91a61...` — original EA-SA-Q0…Q8 adjudication;
- external audit;
- `746a0794...` — HF-N10 added after audit.

HF-N10 is therefore **post-audit / previously unscored** and is not counted as part of the v0.1 coverage finding.

This is stated in the v0.2 adjudication/result, the freeze/version lineage and the new v0.3 preregistration contract.

### F2 — “ablations were frozen”

**Accepted. The earlier wording was incorrect.**

The old v0.2 ablation table was an author expectation written after seeing the original coverage mapping. It was not a preregistered mutation contract.

Remedy:

- [DDS_STAGE_A_PREREGISTRATION_CONTRACT_v0.3.md](./DDS_STAGE_A_PREREGISTRATION_CONTRACT_v0.3.md) freezes new ABL-01…ABL-09 predictions before a new blind result.
- [DDS_STAGE_A_MUTATION_TEST_CONTRACT_v0.1.json](./DDS_STAGE_A_MUTATION_TEST_CONTRACT_v0.1.json) freezes BR-01…BR-17, author predictions and M-01…M-10 mutation kill sets before a new blind result.

The v0.1/v0.2 tables remain historical records and are not relabelled as preregistered.

### F3 — CX2/CX3 were weak falsifiers

**Accepted.**

They are no longer presented as the core falsifier set for the next run.

New v0.3 falsifiers:

- **F-A:** split authority across principals/domains;
- **F-B:** self-reported action/effect trace contradicted by an independent recorder;
- **F-C:** self-certified signed identity without an external trust/representation root.

The old observation-boundary and revoked-authority cases are retained as **boundary/direct-conformance controls**, not advertised as likely textual gaps.

### F4 — N10 did not fit the Stage A question / no Q9

**Accepted.**

The successor [Stage A Route v0.3](./DDS_STAGE_A_HISTORICAL_ROUTE_v0.3_PREREGISTERED.md) explicitly changes the next-run question and material-violation definition to cover both:

1. apparent-authority / evidence-to-authority promotion; and
2. conscious displacement of a correctly represented mandate for goal/scorer/collective utility.

The preregistered contract adds:

**EA-SA-Q9 — qualified disposition versus conscious noncompliance.**

Q9 is intentionally allowed to return **NOT_ESTABLISHED** when EA qualifies the decision but execution/compliance is externally owned. This is a legitimate claim-narrowing result, not a forced failure or PASS.

### F5 — blind packet leakage / undefined verdicts / no disagreement rule

**Accepted.**

The old blind packet is preserved as an exposed predecessor and is not used for the next blind run.

Replacement:

[ DDS_STAGE_A_BLIND_SECOND_READER_PACKET_v0.2_NEUTRAL.md ](./DDS_STAGE_A_BLIND_SECOND_READER_PACKET_v0.2_NEUTRAL.md)

It:

- does not give the reviewer Route/Run Card/adjudication/result files;
- pins only the canonical requirements and the pre-HF-hardening ownership/maturity map;
- uses neutral IDs BR-01…BR-17;
- defines PASS / FAIL / NOT_ESTABLISHED;
- includes Q0…Q9 without author S/T mapping;
- includes no author predictions;
- defines reviewer eligibility and sealing;
- defines disagreement as `DISAGREEMENT_UNRESOLVED`, requiring third review or a successor version.

A reviewer who already read the prior adjudication cannot be considered blind.

### F6 — “deterministic execution” undefined for a documentary specification

**Accepted.**

For this Stage A profile, deterministic execution is now defined as **specification/adjudication mutation testing**, not architecture/runtime execution.

The frozen mutation contract includes:

- deny-all UNKNOWN mutant;
- peer-GO-as-authority mutant;
- population-majority-as-authority mutant;
- technical-success-as-permission mutant;
- stale-grant reuse mutant;
- self-certified-identity mutant;
- self-trace-as-outcome-truth mutant;
- silence-as-consent mutant;
- effective-role-rewrites-bound-role mutant;
- qualification-is-enforcement mutant.

Architecture/runtime execution remains Stage B/C.

### F7 — historical leftovers

**Accepted and surgically corrected where source-supported.**

- H8 is corrected in Route v0.3: synchronized run termination around 01:30 July 12, cause unresolved/likely external; later activity decline and victim containment remain distinct.
- XEV-19 public METR text was rechecked: 3–6 examples considered human/external reporting; none pursued alerting humans.
- The 38148C veto attribution was rechecked in public METR text and retained.
- The historical evidence-register E001… sequence was aligned to the narrative reconstruction; the omitted May-26 Git-LFS event and July-7 workload-resumption event are restored to the machine chronology.
- Historical Reconstruction §12.2 now matches the matrix: the 16:01 MKCOL primitive / PHASEONE10841 link is temporally compatible but identity/event join is not established.
- HF-T03 was narrowed so it does not import the separate leaked-token/HOLD reasoning.
- HF-T09 now preserves the conscious out-of-scope / collective-goal-utility mechanism as a distinct source-grounded packet.
- The ~40-second “no veto, proceed” pattern is included in v0.3 as a direct S10/S5 boundary control.

### F8 — preparation map contradicts adjudication

**Accepted. No rewrite of the canonical/preparation corpus was made.**

The next run pins the pre-Hugging-Face-hardening preparation map:

- commit `a18bb0f32bed`
- blob `38d64f61ef81a300a20d9d89cda65e5bb6ba5b22`

The v0.3 preregistration therefore preserves:

- **S11 as mixed**, not wholly direct EA ownership;
- S3/S5/S9/S10/S14 and T1–T4 maturity limits, including N2/editorial-normalization where applicable;
- containment/execution as external where the source says so.

The later moving-main §15A edit is not retroactively credited.

### F9 — temporal independence / 00A–00C lineage

Repository path history was checked.

The canonical requirements file, 00A and 00C all first appear in the same visible integration commit:

`239ec5f5b17a` — 17 September 2026.

The available path history therefore does **not** establish that 00A/00C are pre-incident textual ancestors through a simple later move/rename.

The v0.3 contract records:

**independence of the current requirement wording from the incident = NOT_ESTABLISHED.**

This remains a retrospective specification-discovery / coverage exercise.

---

## 3. Source-freeze amendment after final surgical corrections

The v0.3 scoring contract was committed before the last factual reconciliation was complete.

Instead of editing that contract, a source-only successor was added:

[ DDS_STAGE_A_SOURCE_FREEZE_ADDENDUM_v0.3.1.md ](./DDS_STAGE_A_SOURCE_FREEZE_ADDENDUM_v0.3.1.md)

It freezes the corrected historical blobs while leaving the already committed verdict definitions, Q0…Q9, falsifiers, ablations and mutation predictions unchanged.

No blind result had been produced before this source-freeze successor.

---

## 4. Current Stage A package for the next result-producing run

Use:

1. [Stage A Route v0.3](./DDS_STAGE_A_HISTORICAL_ROUTE_v0.3_PREREGISTERED.md)
2. [Preregistration Contract v0.3](./DDS_STAGE_A_PREREGISTRATION_CONTRACT_v0.3.md)
3. [Source Freeze Addendum v0.3.1](./DDS_STAGE_A_SOURCE_FREEZE_ADDENDUM_v0.3.1.md)
4. [Mutation Test Contract v0.1](./DDS_STAGE_A_MUTATION_TEST_CONTRACT_v0.1.json)
5. [Neutral Blind Packet v0.2](./DDS_STAGE_A_BLIND_SECOND_READER_PACKET_v0.2_NEUTRAL.md)
6. [Current Run Card v0.3](./DDS_STAGE_A_RUN_CARD_v0.3_PREREGISTERED.json)

The exact v0.1 and v0.2 records remain preserved for audit lineage.

---

## 5. Current claim ceiling

No new PASS is claimed.

The strongest current statement remains:

> **Retrospective requirement-level coverage has been demonstrated for the earlier declared family; a new falsifiable Stage A contract is now preregistered, including N10/Q9, blind-review rules and mutation tests. Stage A acceptance remains pending execution of that frozen contract and independent/blind adjudication.**

Stage B: **not passed**.

Stage C: **not started**.
