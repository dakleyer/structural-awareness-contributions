# RS-00E-Q1a Fixture Family — Index

> **Navigation:** [Iván Abril Palma](https://github.com/dakleyer/dakleyer) → [Structural Awareness](https://github.com/dakleyer/structural-awareness-contributions) → [Ecosystem Awareness](../../../README.md) → [Canonical corpus](../../README.md) → **RS-00E-Q1a fixture family**


> **Status:** descriptive Stage-0 execution published for Q1a only; B1 and B3 tie in this deterministic fixture. No comparative EA or product result.

The [Stage-0 runner](./stage0_runner.py), [frozen observations](./frozen_observations_v05.json) and [separate post-run oracle](./oracle_reference_v05.json) implement the v0.5 descriptive harness contract. The runner executes the active and detector-disabled Step-0 controls before B1/B3. The [v0.5 execution record](./EXECUTION_RECORD_v0.5.md) reports the run from committed code `41931997b4f8ac2d2cbbdff696705cd610105a71`, with [12 candidate traces, two controls and hashes](./runs/stage0_v05_4193199/manifest.json). The [CI replay workflow](../../../../../.github/workflows/rs-00e-q1a-stage0.yml) checks the committed files byte for byte. Both configurations pass all three branches; this is a self-configured descriptive harness, with no independent reviewer.

## Operative pre-registration

The only operative record for a new RS-00E-Q1a run is:

| Record | Public commit | Use |
| --- | --- | --- |
| [Pre-registration v0.5](./pre_registration_v0.5.md) | `00241c5c3ab554dd732467ef0ae4c175f958d144` | Cite this commit in every Step-0 trace and later fixture-family trace. It adds Canonical Trace v1 and the inverse instrumentation negative control while preserving descriptive Stage-0 scope only; no EA differential conclusion is available without a later record naming a comparator defender and independent reviewer. |

## Historical records — not operative

These records are immutable and retained for public lineage. They must not be cited for a new run.

| Record | Public commit | Status |
| --- | --- | --- |
| [v0.1](./pre_registration_v0.1.md) | `dab01272a8d599b277c20519e9cf35d5344533bd` | Superseded before execution |
| [v0.2](./pre_registration_v0.2.md) | `1b9fed23eb3e4868a29ea86892c52f21983aa742` | Superseded before execution |
| [v0.3](./pre_registration_v0.3.md) | `830148260493bd6b46b5889e2ce326c86544b30f` | Superseded before execution |
| [v0.4](./pre_registration_v0.4.md) | `351923834ea21445dc7d38a1d4ebff968f41587e` | Superseded before execution by v0.5; retained immutable for public lineage |

> **Namespace note:** fixture labels `P1`, `P2` and `C0` in this pre-registration are immutable test-branch identifiers. They are **not** the P1 Normal / P2 Containment / P3 Migration operating-posture namespace defined later in MSCA Operation/Repositioning.

## Next evidence boundary

Independently review and replay the oracle and comparator. A separately pre-registered B0–B3 comparison requires named defenders and a reviewer before claiming a differential. This Stage-0 run covers Q1a only.
