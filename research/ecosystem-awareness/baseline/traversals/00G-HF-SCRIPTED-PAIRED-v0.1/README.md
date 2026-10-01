# 00G-HF — paired integrated scripted traversal

**Pre-execution publication.** Eight pairs are registered: six primary cases and two development boundary cases. Both arms use the same native controls; the EA arm adds the published component, signal delivery and explicit consumption policy with charged costs. This is a complete programmed path, not a model trial or empirical E1/E3 closure.

[Protocol and T1–T4 assessment boundary](./PROTOCOL.md) · [Frozen worlds and expectations](./CASES.json) · [Fixed policies](./policy.py) · [Runner](./run.py) · [Independent recorder/outcome checker](./verify_run.py) · [Parallel plan](../../implementation/00G-HF-PARALLEL-v0.1/README.md).

From repository root, Python 3.10+ without `-O`, using a new output directory:

```sh
python research/ecosystem-awareness/baseline/traversals/00G-HF-SCRIPTED-PAIRED-v0.1/run.py --output-dir /tmp/00g-hf-paired-run
python research/ecosystem-awareness/baseline/traversals/00G-HF-SCRIPTED-PAIRED-v0.1/verify_run.py /tmp/00g-hf-paired-run
```

DESIGN_FREEZE.json pins protocol, world expectations, code and dependency manifest. The runner validates them and records registration before any policy action. Inputs, native events, signals, responses, actual outcomes and costs must be published after execution, including expected or unexpected failures. No favorable result is required for completion of the experiment. A separate `VERIFICATION.json` supplies the final recorder checks and bounded T1–T4 assessment; `RESULT.json` preserves the runner's original observations.

The underlying native candidate, EA v0.1/v0.2 and C3 oracle remain frozen. The fixture adapter here explicitly consumes point observations under native guards; it does not fabricate their missing version/forward validity. General EA sufficiency, real-agent response, causal attribution, blind variants and escalation compositions remain outside this lot.
