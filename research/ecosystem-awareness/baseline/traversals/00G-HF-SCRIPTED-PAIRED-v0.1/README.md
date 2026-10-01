# 00G-HF — paired integrated scripted traversal

**Executed: eight pairs, sixteen complete programmed traversals. Native completes 8/8 tasks; native+EA completes 7/8.** Both complete all six primary cases. EA loses legitimate continuity in the registered short-deadline boundary due to its added processing/transport cost. All sixteen paths satisfy C3's bounded safety predicates. This is not a model trial or empirical E1/E3 closure.

[Results, costs and T1–T4 disposition](./RESULTS.md) · [Verified evidence](./runs/2026-10-01-first/VERIFICATION.json) · [Operator record](./OPERATOR_RECORD.md) · [Design published before execution](https://github.com/dakleyer/structural-awareness-contributions/commit/08a76f7454cd6f3f5a446efa7c1722d9ee337289).

[Protocol and T1–T4 assessment boundary](./PROTOCOL.md) · [Frozen worlds and expectations](./CASES.json) · [Fixed policies](./policy.py) · [Runner](./run.py) · [Independent recorder/outcome checker](./verify_run.py) · [Parallel plan](../../implementation/00G-HF-PARALLEL-v0.1/README.md).

From repository root, Python 3.10+ without `-O`, using a new output directory:

```sh
python research/ecosystem-awareness/baseline/traversals/00G-HF-SCRIPTED-PAIRED-v0.1/run.py --output-dir /tmp/00g-hf-paired-run
python research/ecosystem-awareness/baseline/traversals/00G-HF-SCRIPTED-PAIRED-v0.1/verify_run.py /tmp/00g-hf-paired-run
```

DESIGN_FREEZE.json pins protocol, world expectations, code and dependency manifest. It was published before the first run and remains unchanged. The runner validated it and recorded registration before any policy action. All inputs, native events, signals, responses, actual outcomes and costs are published, including the EA task failure. A separate `VERIFICATION.json` supplies the final recorder checks and bounded T1–T4 assessment; `RESULT.json` preserves the runner's original observations. RESULT_MANIFEST.json checks the resulting raw artifacts. No favorable result was required for completion of the experiment.

The underlying native candidate, EA v0.1/v0.2 and C3 oracle remain frozen. The fixture adapter here explicitly consumes point observations under native guards; it does not fabricate their missing version/forward validity. General EA sufficiency, real-agent response, causal attribution, blind variants and escalation compositions remain outside this lot.
