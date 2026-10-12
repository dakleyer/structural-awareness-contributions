# First-channel counterfactual experiment v0.3

**Status:** author-constructed exploratory model, not historical model behavior, independent verification, or completed DDS Stage A/B/C. Research question: Iván Abril Palma; model/script and review: OpenAI ChatGPT GPT-6, 12 October 2026.

This directory contains the reproducible 18-case, 7-configuration matrix (126 records) and 10 five-node communication simulations. The experiment separates what a participant knows from what a task owner authorizes; it compares native purpose validation, local Ecosystem Awareness, and optional bounded communication.

[Python run script](./run.py) | [Cases, summaries and limitations](./summary.json) | [Records 1–63](./records_01.jsonl) | [Records 64–126](./records_02.jsonl) | [Network trace results](./graph.json) | [Digests](./SHA256_MANIFEST.json).

Run `python run.py` here to regenerate all five result files, including the combined `results.json`. The previous [v0.2 source](../first-channel-counterfactual-v0.2/run.py) is preserved as a corrected predecessor.

No live agents, production authorization systems, real adverse outcomes or latency benchmarks were tested. A larger number of observed/contextual changes is not itself an efficacy benefit; communications that have not been authorized are not legitimized by carrying EA metadata. See the source files for precise assumptions and limitations.

**Correction note:** v0.2 equated an unresolved owner permission with proven denial. v0.3 separates both conditions and retains the earlier raw records without rewriting them.
