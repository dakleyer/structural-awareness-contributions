# Hugging Face DDS Stage A v0.3 — Coherence Check — 8 October 2026

**Status:** maintainer-side package coherence check · not an independent blind adjudication · not Stage A acceptance.

## 1. Question checked

Does the current Hugging Face Stage A v0.3 preregistered package preserve the audited chronology and version lineage, freeze the new scoring contract before any v0.3 result, remove the previously identified blind-packet contradictions, and remain internally consistent enough to proceed to the actual blind/mutation run?

## 2. Package freeze — verified

The current package manifest is:

- `DDS_STAGE_A_V0_3_PACKAGE_MANIFEST.json`
- status: `FROZEN_FOR_NEXT_BLIND_AND_MUTATION_RUN__NO_RESULT_YET`
- Stage A claim: `COVERAGE_ARGUMENT_COMPLETE__STAGE_A_ACCEPTANCE_PENDING`

Mechanical comparison against the current repository confirms that every blob listed in the manifest still matches the current file blob:

| Artefact | Manifest/current blob match |
|---|---|
| Route v0.3 | yes |
| Preregistration Contract v0.3 | yes |
| Source Freeze Addendum v0.3.1 | yes |
| Mutation Test Contract v0.1 | yes |
| Neutral Blind Packet v0.2 | yes |
| Run Card v0.3 | yes |
| External Audit Input 3 | yes |
| External Audit Response 3 | yes |

No v0.3 blind result or mutation result is present.

## 3. Chronology and lineage — verified

The freeze/version lineage now states correctly:

- HF-N0…HF-N9 predate the original v0.1 requirement-level adjudication;
- HF-N10 was added only after the external audit and is not represented as preregistered for v0.1;
- HF-N10 is first admitted to a prospectively frozen result-producing contract in v0.3;
- EA-SA-Q9 is first preregistered in v0.3 before any v0.3 blind result;
- PASS / FAIL / NOT_ESTABLISHED definitions and M-01…M-10 mutation predictions are frozen before the next result.

The earlier v0.1 artefacts remain preserved as exact historical blobs; v0.2 and v0.3 are successors rather than silent rewrites.

## 4. Source-freeze reconciliation — verified

The v0.3 Preregistration Contract retains its original pre-final-reconciliation historical evidence pins. The separate Source Freeze Addendum v0.3.1 explicitly supersedes only those historical-source blobs after the surgical factual correction and states that verdict semantics, Q0…Q9, falsifiers, ablations and mutation predictions were unchanged.

The Run Card and package manifest use the corrected v0.3.1 historical source blobs:

- reconstruction: `56754a0a63a351448fdbd14dfd754816dc42bc43`
- cross-source matrix: `20db58f335227cbf9ff830aab7d33967a15629a3`
- trace packets: `a5c0c4ba7c499d92b89fc8748dec1a1e8c88ec22`
- evidence register: `a7f5f234e091777864f578d54fb4e67e25d9cbde`

This is versioned amendment, not an unrecorded scoring change.

## 5. Blind-review package — structurally verified

The neutral packet:

- contains BR-01…BR-17 as neutral case IDs;
- contains Q0…Q9;
- defines PASS / FAIL / NOT_ESTABLISHED;
- contains no HF-N0…HF-N10 identifiers in the case set;
- does not expose requirement-to-case author mappings or author expected verdicts;
- explicitly excludes prior adjudications/results, the mutation contract, author predictions and route/run-card mappings from the blind reader.

The packet necessarily names excluded artefacts in its exclusion/eligibility instructions. Those names are not verdict leakage. Because the repository is public, operational blindness still requires distributing the neutral packet and pinned inputs without permitting the reader/model to browse the repository before sealing.

## 6. Mutation/ablation contract — verified

The mutation contract contains exactly M-01…M-10.

- all registered kill cases resolve to BR-01…BR-17;
- no undefined kill-case identifier remains;
- author predictions cover all BR-01…BR-17;
- deny-all is explicitly prevented from winning through positive-continuity cases;
- mutation execution is explicitly specification sensitivity, not Stage B architecture execution.

The v0.3 requirement ablations are explicitly labelled as new preregistered predictions rather than historical v0.1 facts. The earlier mismatch between a supposed frozen v0.1 ablation table and the actual case family is therefore no longer claimed.

## 7. Historical corrections called out by Audit 3 — checked

Current artefacts reflect the main factual/editorial corrections:

- Route H8 no longer says `wind down`; synchronized run termination, later activity decline and victim containment are separate;
- the cross-source board-primitive relation is `TEMPORALLY_COMPATIBLE_POSSIBLE_JOIN__IDENTITY_NOT_ESTABLISHED`, not a forced identity join;
- event identifiers in the evidence register are aligned as E001…;
- HF-T03 and the distinct HOLD/goal-utility reasoning are separated;
- HF-T09 exists for explicit out-of-scope recognition followed by collective/goal-utility continuation;
- XEV-19 is recorded as a METR behavioral finding with the public text rechecked on 8 October;
- HF-T04 treats the peer veto as a source-supported restraining signal while explicitly leaving legitimate principal authority NOT_ESTABLISHED.

## 8. What is closed versus still open

### Closed for package-coherence purposes

- historical v0.1 preservation;
- N10 chronology correction;
- Q9 preregistration;
- verdict definitions;
- neutral case IDs and blind-packet structure;
- mutation set and kill-case consistency;
- source-freeze amendment lineage;
- the specific H8 / join / T09 / XEV-19 corrections above;
- manifest-to-current-blob consistency.

### Still open — intentionally

1. an eligible blind/independent reader has not sealed BR-01…BR-17;
2. M-01…M-10 have not been executed against the reference candidate;
3. disagreement handling has therefore not been exercised;
4. HF-N10/Q9 has no v0.3 result yet;
5. Stage B architecture verification has not started/passed;
6. Stage C implementation/problem validation has not started.

## 9. Coherence verdict

**The Hugging Face v0.3 package is coherent enough to proceed to the preregistered blind and mutation run.**

This is **not** a renewed Stage A acceptance. The correct current state remains:

`COVERAGE_ARGUMENT_COMPLETE__STAGE_A_ACCEPTANCE_PENDING`

Acceptance can change only after the frozen v0.3 evidence-generation steps are actually executed.
