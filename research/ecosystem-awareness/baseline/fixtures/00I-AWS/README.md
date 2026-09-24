# 00I-AWS — implementation skeleton package

| | |
|---|---|
| **Parent scenario** | [00I v0.4 Draft](../../00I_FAILURE_MODE_SEMANTIC_TOCTOU_v0.4_DRAFT.md) |
| **Implementation profile** | [00I-A01 AWS Step Functions / RDS v0.2 Draft](../../00I_A01_AWS_STEP_FUNCTIONS_RDS_IMPLEMENTATION_PROFILE_v0.2_DRAFT.md) |
| **Status** | Design skeleton only · unexecuted · not W3-admitted |
| **Purpose** | Make the three trajectories inspectable before fixture freeze |

This package is deliberately **not deploy-ready infrastructure-as-code**. The ASL files are syntactically structured state-machine skeletons with placeholder Lambda ARNs. They show where the decision boundaries are enforced; actual AWS accounts, roles, resource ARNs, Lambda implementations, IAM/SCP controls and RDS targets must be supplied in a later admitted fixture.

## Files

- `i0_ordinary.asl.json` — ordinary qualified action → Wait → later apply.
- `i1_top_notch.asl.json` — record basis → Wait → acquire broker lease + requalify current known basis → Choice → apply/requalify/deny.
- `i2_ea_drift.asl.json` — verify whether the basis model itself is current → targeted re-entry when stale → run the defended I1 guard/lease.
- `fixture_d1_source_set_drift.json` — deterministic D1 v17→v18 source-set change.
- `trace_contract.json` — minimum evidence every run must emit.

## Fair-comparison rules

1. I1 must pass valid continuity and the base Patch-A/Patch-B/freeze case before drift.
2. I2-peer is the exact frozen I1 implementation under the drift.
3. I2-EA gets the same APIs, authoritative sources, time and compute budget as I2-peer.
4. The runtime never receives the after-run oracle.
5. If I2-peer dynamically discovers/requalifies the new basis at equal or lower burden, the peer passes.
6. No new drift branch may be invented after results merely to manufacture separation.
7. The defended route assumes a single-writer broker for material `db-7` changes; bypass writers are a separate test branch.

## W3 boundary

Before execution this package still requires:

- concrete Lambda/broker code;
- actual source adapters;
- IAM/resource policy freeze;
- deterministic oracle;
- DBC-R# mapping;
- threshold/freshness values;
- trace schema validation;
- preregistration commit.

Nothing in this directory is an execution result.
