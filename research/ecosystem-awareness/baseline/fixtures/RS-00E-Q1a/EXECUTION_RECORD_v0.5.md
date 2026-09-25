# RS-00E-Q1a Stage-0 execution record — v0.5

**Class:** descriptive Stage-0 stipulative verification of one synthetic fixture family, not a product or comparative EA result. **Pre-registration:** [v0.5](./pre_registration_v0.5.md) first published in `00241c5c3ab554dd732467ef0ae4c175f958d144`; this file was not edited for the run. **Code commit executed:** [`41931997b4f8ac2d2cbbdff696705cd610105a71`](https://github.com/dakleyer/structural-awareness-contributions/commit/41931997b4f8ac2d2cbbdff696705cd610105a71). **Labels:** facts self-declared; comparator self-configured; no independent reviewer or defender. Every candidate trace cites the pre-registration commit.

## Execution and observable result

From the committed code directory, with Python `3.12.14`:

```bash
PYTHONDONTWRITEBYTECODE=1 python stage0_runner.py --output runs/stage0_v05_4193199
PYTHONDONTWRITEBYTECODE=1 python -m unittest -v test_canonical_trace_v1.py
```

The command returned exit `0`, empty stderr, eight CTv1 unit tests passed. [Active Step-0 control](./runs/stage0_v05_4193199/step0_active.json) returned **PASS** after the injected `upstream_source_id=P` was lost at `received_reports_to_assessment` (step 1). The same injected loss with [detector disabled](./runs/stage0_v05_4193199/step0_detector_disabled.json) returned **FAIL**, the required inverse control. These two traces were written before the candidate runs. No candidate result is interpreted without both.

The [manifest](./runs/stage0_v05_4193199/manifest.json) links **12 Canonical Trace v1 files**, covering 3 branches × 2 configurations × 2 repetitions. Each repetition was a separate adapter invocation; for each branch/configuration the two published files have **identical canonical bytes and SHA-256**. Both B1 and B3 passed the closed gate in `Q1a-P1`, `Q1a-P2` and the independent-source positive control `Q1a-C0`. The latter prevents a universal hold from appearing to pass. The reference oracle was loaded only **after** both adapters completed all candidate invocations, and was passed solely to the post-run evaluator.

| Count per configuration | B1 conventional peer | B3 EA-profiled adapter |
|---|---:|---:|
| Correlated-evidence error | 0/2 primary branches | 0/2 primary branches |
| False shared closure | 0/2 primary branches | 0/2 primary branches |
| Required residual/scope fields retained | 6/6 fields across primary branches | 6/6 fields across primary branches |
| Candidate branches passing | 3/3 | 3/3 |
| Modelled steps P1 / P2 / C0 | 4 / 5 / 5 | 4 / 5 / 5 |

Counts are exact for this three-branch deterministic fixture, not inferential rates. The response horizon was 6 modelled steps. Both configurations had the same received fields, context registry, ceiling and horizon; neither re-queried primary sources. Burden ties exactly here and was pre-registered as non-discriminating. B1 passing P2 is **descriptive** under v0.5; absent a named comparator defender and independent reviewer, it does not support an EA differential or its falsification as an experimental comparative result. No product vendor was executed.

## Reproduction fingerprints

| Artifact | SHA-256 of bytes |
|---|---|
| `stage0_runner.py` | `2baab9fc11640ce1d0cdf50a22e2be549696f7fb65718e2bcfca3566a6d7761b` |
| `frozen_observations_v05.json` | `e4fc7ba46b07eb27030faf8a7628ccef451bb85497fa619baaa2e11a222d5589` |
| `oracle_reference_v05.json` | `29af6d8cff9c1a88fe69c77aac2af2bea3860b0408368b9d9d3a68ac50bfd6b1` |
| `pre_registration_v0.5.md` | `ee844279ec469ba6f507ff1f10700007866002babd3364f957bd05e366c5bddf` |
| `canonical_trace_v1.py` | `32fbe24097b99db29ca229a089b41ff10a61c6f8cb5bd945d62d033dfca3683c` |
| Step-0 active trace | `51800d552a67952f78d6db090c0223873b2930e94bdde6299bc9c8a1855704ae` |
| Step-0 detector-disabled trace | `d632b336e5a91df4c04000c451157f8a7140d4945e9420a0f52d287a94e95ba7` |

The [Stage-0 workflow](../../../../../.github/workflows/rs-00e-q1a-stage0.yml) replays both controls and all 12 branches on the PR integration tree, then compares each file byte for byte. The [successful Stage-0 replay run 36192185274](https://github.com/dakleyer/structural-awareness-contributions/actions/runs/36192185274) checked this evidence on the PR integration tree for evidence commit [`be511a0`](https://github.com/dakleyer/structural-awareness-contributions/commit/be511a087e38b672ff1e338745a175abc2001997); its artifact retains the effective checkout SHA, Python version, stdout/stderr and hashes. GitHub pull-request checks use a temporary integration checkout, whose exact SHA is in that run artifact. This CI success does not turn a descriptive fixture into product evidence.

**Next evidence boundary:** independent replay and review of the oracle and comparator, then a new pre-registered B0–B3 comparison if a differential is to be assessed. This run covers **Q1a only**; not all four 00E subsystems, Q1–Q5 composition, 100M tokens or real-world outcomes.
