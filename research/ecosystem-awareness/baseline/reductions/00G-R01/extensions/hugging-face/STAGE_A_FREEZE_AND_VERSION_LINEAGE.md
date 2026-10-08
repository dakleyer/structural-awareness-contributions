# Hugging Face DDS Stage A — Freeze and Version Lineage

**Purpose:** preserve exact pre-audit Stage A artefacts while allowing audit-corrected successors. This file changes no scientific claim, requirement, historical fact or architecture semantics.

## 1. Exact pre-audit snapshot

The first external-audit pack was created at repository commit:

- **Repository snapshot:** `420d1b84304e8ffc96cd6656bac578f976c6b309`
- **Date:** 8 October 2026

The following v0.1 files have been restored **byte-for-byte to the blob content present at that snapshot**:

| Artefact | Restored blob SHA |
|---|---|
| `DDS_STAGE_A_HISTORICAL_ROUTE_v0.1.md` | `df8733c3cdd8193a4c5aa88d9af8b03d208d06f9` |
| `DDS_STAGE_A_RUN_CARD_v0.1.json` | `fcb2ae7cd0c40d44c7e57b7496ceb96e3ebcd296` |
| `DDS_STAGE_A_EA_SPECIFICATION_ADJUDICATION_v0.1.md` | `9fb85288cc7b1cd0dfb9e6976d419ecb79bdc1d8` |
| `DDS_STAGE_A_EA_SPECIFICATION_RESULT_v0.1.json` | `9e36ccb609e8489a9d4c8ff120c7f052454ef6a1` |

For audit of what the authors had actually published before the external-audit corrections, use the **commit permalink** at `420d1b84...`, not a moving `main` link to dependent files.

## 2. Audit-corrected successors

Current successors are:

- [Stage A Historical Route v0.2 — Audit-Corrected](./DDS_STAGE_A_HISTORICAL_ROUTE_v0.2_AUDIT_CORRECTED.md)
- [Stage A Run Card v0.2 — Audit-Corrected](./DDS_STAGE_A_RUN_CARD_v0.2_AUDIT_CORRECTED.json)
- [Stage A Specification Coverage Adjudication v0.2 — Audit-Corrected](./DDS_STAGE_A_EA_SPECIFICATION_ADJUDICATION_v0.2_AUDIT_CORRECTED.md)
- [Stage A Result v0.2 — Audit-Corrected](./DDS_STAGE_A_EA_SPECIFICATION_RESULT_v0.2_AUDIT_CORRECTED.json)
- [Blind Second-Reader Packet](./DDS_STAGE_A_BLIND_SECOND_READER_PACKET_v0.1.md)
- [External Audit Response](./EXTERNAL_AUDIT_RESPONSE_2026-10-08.md)

Current Stage A status:

`COVERAGE_ARGUMENT_COMPLETE__STAGE_A_ACCEPTANCE_PENDING`

## 3. Chronology relevant to preregistration

- `e0794209...` — original deterministic Run Card / oracle design.
- `37f87c1f...` — **HF-N0…HF-N9** anti-overfitting family added before the requirement-level adjudication.
- `4cb91a61...` — requirement-level EA-SA-Q0…Q8 adjudication and original verdicts created.
- `f2cb8113...` — architecture/specification ownership correction.
- external audit occurs.
- `746a0794...` — **HF-N10** conscious out-of-scope collective-utility variant added **after** external audit.

Therefore:

- HF-N0…HF-N9 predate the v0.1 requirement adjudication.
- HF-N10 does **not** predate it and is not part of the original v0.1 coverage result.
- EA-SA-Q0…Q8 and the requirement-level acceptance rule were introduced inside the v0.1 adjudication itself.
- deterministic execution remains pending.

## 4. Versioning rule going forward

- Frozen/result-producing artefacts are never silently rewritten after audit.
- Factual corrections to working historical evidence may remain in-place only while the document explicitly remains a working/in-progress evidence product.
- Any material change to a frozen route, Run Card, oracle, acceptance policy, negative-family kernel or scored specification creates a successor version.
- Earlier versions remain readable and auditable.
