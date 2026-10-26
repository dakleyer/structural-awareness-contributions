# DDS Stage A — Source Freeze Addendum v0.3.1

**Status:** source-freeze successor only · scoring semantics unchanged from [Preregistration Contract v0.3](./DDS_STAGE_A_PREREGISTRATION_CONTRACT_v0.3.md) · frozen before any v0.3 blind-reader result.

**Date:** 8 October 2026.

## 1. Why this addendum exists

The v0.3 preregistration contract was committed before the final **surgical factual reconciliation** prompted by External Audit 3 was completed. No blind-reader result has been produced.

Rather than silently editing the preregistration contract, this addendum freezes the corrected evidence artefacts while preserving the v0.3 scoring/verdict/Q9/ablation semantics exactly as committed.

The corrections covered:

- alignment of E001… event identifiers between narrative and machine register;
- the board-primitive conflict status;
- separation of HF-T03 apparent-authority evidence from the distinct HOLD/goal-utility example;
- addition of source-grounded HF-T09 for conscious out-of-scope continuation;
- explicit source-ceiling inheritance in trace packets;
- public-source recheck of XEV-19 and the 38148C veto attribution.

No PASS/FAIL/NOT_ESTABLISHED definition, Q0…Q9 gate, falsifier, ablation or mutation prediction was changed by these evidence corrections.

## 2. Corrected historical source freeze

The v0.3 blind/mutation run SHALL use these blobs for historical provenance:

| Artefact | Frozen blob SHA |
|---|---|
| `HISTORICAL_INCIDENT_RECONSTRUCTION_v0.1.md` | `56754a0a63a351448fdbd14dfd754816dc42bc43` |
| `CROSS_SOURCE_EVENT_MATRIX_v0.1.md` | `20db58f335227cbf9ff830aab7d33967a15629a3` |
| `FIRST_HISTORICAL_TRACE_PACKETS_v0.1.md` | `a5c0c4ba7c499d92b89fc8748dec1a1e8c88ec22` |
| `HISTORICAL_INCIDENT_EVIDENCE_v0.1.json` | `a7f5f234e091777864f578d54fb4e67e25d9cbde` |

## 3. Specification input freeze remains unchanged

Canonical requirements:

- commit `96cbc94921aa5f2f16463faaf4a2f165175383a0`
- blob `4fe3d69b50fef1e82ba7f889324b70a7f6b1a81c`

Specification-preparation ownership/maturity map:

- pinned commit `a18bb0f32bed`
- blob `38d64f61ef81a300a20d9d89cda65e5bb6ba5b22`

The moving main version of the preparation map, including later Hugging-Face-derived §15A text, is **not** part of the v0.3 specification input.

## 4. Preregistered scoring artefacts remain unchanged

- Preregistration contract blob: `89c227175a17338b09d50d513b01195975bff1ae`
- Mutation-test contract blob: `de603f7f52f06291971ec0c6bfcb5377a1b143a1`
- Neutral blind-reader packet blob at creation: `950a8f69c17cd91cee27122d02405759a0fcf725`
- Stage A route v0.3 blob at creation: `607599c10a42497d1ca61741a282decb100298b4`

The neutral packet contains case facts directly and does not require the blind reviewer to browse the historical route/evidence corpus.

## 5. Amendment rule

Any further material factual change that would alter a BR case fact, Q0…Q9 meaning, author prediction, mutation kill set, verdict definition or ownership/maturity interpretation requires a successor preregistration version before a blind result.

Editorial corrections that do not alter any frozen case fact may be logged separately but must not silently change the supplied blind packet.

## 6. Current status

No blind v0.3 result has been received.

No mutation-test v0.3 result has been executed.

Stage A remains:

`COVERAGE_ARGUMENT_COMPLETE__STAGE_A_ACCEPTANCE_PENDING`
