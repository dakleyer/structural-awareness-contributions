# 00G-HF — model receiver candidate v0.1

**Prepared and checked offline; no live model execution claimed.** This candidate makes the receiving model's decisions open while retaining the [executed software scenario](../../traversals/00G-HF-CACHED-LINEAGE-v0.1/RESULTS.md). The model may resolve the case without EA or ignore EA. The outcome is not selected by the harness.

[Protocol and limits](./PROTOCOL.md) · [Literal instructions](./INSTRUCTIONS.txt) · [Adapter](./adapter.py) · [Runner](./runner.py) · [CLI](./run_model.py) · [Integration tests](./test_integration.py) · [Source freeze](./FREEZE.json).

Requires Python 3.10+ standard library, authorized `OPENAI_API_KEY` in the execution environment, a selected compatible model, and outbound access to `https://api.openai.com/v1/responses`. No SDK, default model or credential file is required. Do not paste credentials into a report, source file or commit. Current endpoint reachability and live compatibility are untested.

From this directory, with configured access and a new output path:

```sh
python run_model.py --phase native --model YOUR_FROZEN_MODEL_ID --output-dir runs/native-model-first
```

Only if that complete native lot contains an eligible primary failure, execute the registered repair comparison using the same model:

```sh
python run_model.py --phase paired --model YOUR_FROZEN_MODEL_ID --native-run runs/native-model-first --output-dir runs/paired-model-first
```

The paired arms are native, raw current evidence, and the same evidence plus EA assessment. The model controls every resolve/read/deliver/stop action. EA does not automatically block a selected report. A cited signal ID means acknowledgment, not proven understanding.

To check the harness offline:

```sh
python test_integration.py
```

Model requests are not made by these tests. The live CLI records an explicit zero-execution block when model selection or credentials are missing. A model that succeeds natively does not open the repair gate; retain its success rather than weakening it.

**Verified locally:** [17/17 integration checks](./TESTS_REVIEWED.txt), following an initial [15/15 pass](./TESTS_FIRST.txt). Two checks were added for the mock-result gate and immediate journal persistence; no failed first test was discarded. The [access check](./runs/2026-10-01-access-check/REPORT.json) records zero API requests, zero responses and zero episodes: no API key is configured and no model is selected. Its registration is explicitly incomplete. See [verification summary](./VERIFICATION_SUMMARY.json). These checks do not close empirical E1/E3, external review or full canonical sufficiency.
